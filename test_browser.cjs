// End-to-end interaction tests. Answer-key inputs validate scoring software,
// not learner proficiency or psychometric quality.
const fs=require('fs'),path=require('path'),http=require('http'),assert=require('assert');
const {chromium}=require(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES?process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES+'/playwright':'playwright');
const root=__dirname, D=JSON.parse(fs.readFileSync(path.join(root,'data.json')));
const output=process.env.QA_OUTPUT||'/tmp/cmmi-browser-results.json';
let server,browser;const results=[];
function serve(){return new Promise(resolve=>{server=http.createServer((req,res)=>{let filename=path.join(root,decodeURIComponent(req.url.split('?')[0]));if(filename===root+'/')filename+='index.html';if(!filename.startsWith(root+path.sep)||!fs.existsSync(filename)||fs.statSync(filename).isDirectory()){res.writeHead(404);res.end();return}const stat=fs.statSync(filename),ext=path.extname(filename),types={'.html':'text/html','.mp4':'video/mp4','.vtt':'text/vtt','.json':'application/json'};res.setHeader('Content-Type',types[ext]||'text/plain');res.setHeader('Accept-Ranges','bytes');const range=req.headers.range;if(range){const m=/bytes=(\d+)-(\d*)/.exec(range);const start=Number(m[1]),end=m[2]?Math.min(Number(m[2]),stat.size-1):stat.size-1;res.writeHead(206,{'Content-Range':`bytes ${start}-${end}/${stat.size}`,'Content-Length':end-start+1});fs.createReadStream(filename,{start,end}).pipe(res)}else{res.writeHead(200,{'Content-Length':stat.size});fs.createReadStream(filename).pipe(res)}}).listen(0,'127.0.0.1',()=>resolve('http://127.0.0.1:'+server.address().port))})}
async function run(){const local=await serve();const base=process.env.BASE_URL||local;
browser=await chromium.launch({headless:true,...(process.env.CHROMIUM_PATH?{executablePath:process.env.CHROMIUM_PATH}:{}),args:['--no-sandbox','--disable-dev-shm-usage']});
for(const mobile of (process.env.QA_SCREEN==='mobile'?[true]:process.env.QA_SCREEN==='desktop'?[false]:[false,true])){
 const context=await browser.newContext({viewport:mobile?{width:390,height:844}:{width:1440,height:1000},isMobile:mobile,hasTouch:mobile});const p=await context.newPage(),errors=[];p.on('pageerror',e=>errors.push(e.message));
 console.log('START',mobile,base);p.setDefaultTimeout(15000);await p.goto(base);console.log('LOADED');const nav=async route=>{if(mobile&&!await p.locator('.sidebar').evaluate(el=>el.classList.contains('open')))await p.locator('[data-action=menu]').click();await p.locator(`.sidebar [data-route="${route}"]`).click()};
 for(const route of ['home','learn','videos','train','audit','flash','library','glossary','stats','settings']){await nav(route);assert(await p.locator('.content').innerText());assert(await p.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+2),`overflow ${route}/${mobile}`)}
 // Video search remains editable after selecting a result; all 40 reappear.
 await nav('videos');await p.locator('#videosearch').fill('CAR');await p.locator('[data-video-course="PA-CAR"]').click();await p.locator('#videosearch').fill('');assert.equal(await p.locator('[data-video-course]').count(),40);
 await p.waitForFunction(()=>document.querySelector('video')?.readyState>=1);assert.equal(await p.locator('video').evaluate(v=>v.duration),35);await p.locator('[data-video-seek="14"]').click();await p.waitForFunction(()=>Math.abs(document.querySelector('video').currentTime-14)<.2);await p.locator('[data-action=vidspeed]').click();assert.equal(await p.locator('video').evaluate(v=>v.playbackRate),1.25);
 console.log('VIDEO-METADATA-OK');await p.locator('video').evaluate(v=>Promise.race([v.play(),new Promise((_,rej)=>setTimeout(()=>rej(new Error('Playback did not start')),10000))]));await p.waitForFunction(()=>document.querySelector('video').currentTime>14.15);await p.locator('video').evaluate(v=>v.pause());
 // Notes survive grading; matrix and flashcard actions mutate persistent state.
 console.log('VIDEO-PLAYBACK-OK');await nav('audit');await p.locator('#auditNote').fill('Review scope and trace actual work');await p.locator('[data-audit-rate]').first().click();await p.locator('[data-action=validatecase]').click();assert.equal(await p.locator('#auditNote').inputValue(),'Review scope and trace actual work');await p.locator('[data-action=nextcase]').click();await p.locator('[data-action=prevcase]').click();assert.equal(await p.locator('#auditNote').inputValue(),'Review scope and trace actual work');
 await p.locator('[data-route=matrix]').first().click();await p.locator('[data-matrix="CAR"]').selectOption('Solide');const csv=p.waitForEvent('download');await p.locator('[data-action=matrixcsv]').click();assert((await csv).suggestedFilename().endsWith('.csv'));
 console.log('AUDIT-MATRIX-OK');await nav('flash');await p.locator('[data-action=flip]').last().click();await p.locator('[data-review=good]').click();assert(await p.evaluate(()=>Object.keys(JSON.parse(localStorage.getItem('cmmi_academy_2027_v1')).flash).length)>0);
 // Every lesson, every tab, both languages; complete through actual UI controls.
 for(const lang of ['fr','en']){
  await p.locator(`[data-lang="${lang}"]`).click();
  for(const l of [...D.foundations,...D.areas]){
   console.log('LESSON',mobile,lang,l.id);const id=l.domain?'PA-'+l.id:l.id;await nav('learn');await p.locator(`[data-lesson="${id}"]`).first().click();
   assert.equal(await p.locator('.publicPracticeCard').count(),l.publicPracticeLesson?6:l.publicGroupCourse?.entries.length||0);if(l.appliedLesson){assert.equal(await p.locator('.appliedLesson').count(),1);assert((await p.locator('.appliedLesson').innerText()).includes(l.appliedLesson[lang].example));}
   await p.locator('[data-lesson-tab="1"]').first().click();await p.locator('[data-lesson-stage="3"]').click();assert(await p.locator('.diagramExplanation').innerText());
   await p.locator('[data-lesson-tab="2"]').first().click();assert.equal(await p.locator('.caseFile').count(),4);
   await p.locator('[data-lesson-tab="3"]').first().click();const good=(lang==='en'?l.en:l.deep).correct;await p.locator(`[data-lesson-choice="${(good+1)%4}"]`).click();assert.equal(await p.locator('.workshopFeedback.incorrect').count(),1);await p.locator(`[data-lesson-choice="${good}"]`).click();assert.equal(await p.locator('.workshopFeedback.correct').count(),1);
   await p.locator('[data-lesson-tab="4"]').first().click();const qs=l.masteryQuestions[lang];
   // An all-wrong attempt must fail and leave completion disabled.
   for(let i=0;i<5;i++)await p.locator(`[data-master-answer="${i}"][value="${(qs[i].answer+1)%4}"]`).check();
   await p.locator('[data-action=submitmaster]').click();assert((await p.locator('.masterScore').innerText()).includes('0/5'));assert(await p.locator('[data-action=complete]').isDisabled());
   await p.locator('[data-action=retrymaster]').click();
   for(let i=0;i<5;i++)await p.locator(`[data-master-answer="${i}"][value="${qs[i].answer}"]`).check();await p.locator('[data-action=submitmaster]').click();assert((await p.locator('.masterScore').innerText()).includes('5/5'));
   if(l.publicGroupCourse||l.publicPracticeLesson){assert(await p.locator('[data-action=complete]').isDisabled());await p.locator('[data-lesson-tab="0"]').first().click();
    if(l.publicGroupCourse){for(const entry of l.publicGroupCourse.entries){const card=p.locator('.publicPracticeCard').filter({has:p.locator(`[data-pg-check="${entry.groupLevel}"]`)});if(!await card.locator('details').evaluate(el=>el.open))await card.locator('summary').click();await card.locator(`[data-pg-answer="${entry.answer}"]`).click()}}
    else for(let i=0;i<6;i++){const entry=l.publicPracticeLesson.diagnostics[i],card=p.locator('.publicPracticeCard').nth(i);if(!await card.locator('details').evaluate(el=>el.open))await card.locator('summary').click();await card.locator(`[data-pqa-answer="${entry.answer}"]`).click()}
    await p.locator('[data-lesson-tab="4"]').first().click();
   }
   assert(await p.locator('[data-action=complete]').isEnabled());await p.locator('[data-action=complete]').click();
  }
  console.log('PASS',mobile?'mobile':'desktop',lang,'40 lessons, all tabs, 0/5 fail, 5/5 pass, public checks, completion');
  results.push({screen:mobile?'mobile390':'desktop1440',lang,lessons:40,masteryFail:40,masteryPass:40});fs.writeFileSync(output,JSON.stringify({status:'running',results},null,2));
  // Full mock exam A then B; hidden explanations, key scoring, domain totals.
  for(const [form,target] of [['A',120],['B',84]]){
   await nav('train');await p.locator('[data-train-type=exam]').first().click();await p.locator('[data-action=start]').click();assert((await p.locator('.quizProgress').innerText()).includes(form));
   const bank=D.mockExamForms[form][lang];for(let i=0;i<120;i++){
    const stem=await p.locator('.quizQuestion').innerText(),q=bank.find(q=>q.q===stem);assert(q,'unknown question');assert.equal(await p.locator('.feedback').count(),0);
    const choice=i<target?q.answer:(q.answer+1)%4;await p.locator(`[data-choose="${choice}"]`).click();assert.equal(await p.locator('.answer.correct').count(),0);await p.locator('[data-action=nextquestion]').click();
   }
   assert.equal((await p.locator('.resultScore').innerText()).trim(),Math.round(target/120*100)+'%');assert.equal(await p.locator('.domainMeasure').count(),7);assert.equal(await p.locator('.review').count(),120);
   results.push({screen:mobile?'mobile390':'desktop1440',lang,exam:form,expected:target,actual:target,total:120});console.log('PASS',mobile?'mobile':'desktop',lang,'exam',form,target+'/120');fs.writeFileSync(output,JSON.stringify({status:'running',results},null,2));
  }
 }
 // Language toggling and reload retain separate lesson completion and scores.
 await nav('stats');const before=await p.evaluate(()=>JSON.parse(localStorage.getItem('cmmi_academy_2027_v1')));assert.equal(before.completed.length,80);assert.equal(before.mockHistory.length,4);await p.reload();const after=await p.evaluate(()=>JSON.parse(localStorage.getItem('cmmi_academy_2027_v1')));assert.equal(after.completed.length,80);
 await nav('settings');const download=p.waitForEvent('download');await p.locator('[data-action=export]').click();const exportFile=await (await download).path();await p.locator('#importfile').setInputFiles(exportFile);assert.equal(await p.evaluate(()=>JSON.parse(localStorage.getItem('cmmi_academy_2027_v1')).completed.length),80);
 const savedState=await p.evaluate(()=>localStorage.getItem('cmmi_academy_2027_v1'));await p.locator('#importfile').setInputFiles({name:'invalid.json',mimeType:'application/json',buffer:Buffer.from(JSON.stringify({app:'CMMI Academy',progress:{completed:[],attempts:'broken'}}))});assert.equal(await p.evaluate(()=>localStorage.getItem('cmmi_academy_2027_v1')),savedState);
 // Expiry scores unanswered items against the full 120-question denominator.
 await p.clock.install();await nav('train');await p.locator('[data-train-type=exam]').first().click();await p.locator('[data-action=start]').click();await p.clock.fastForward(4*60*60*1000+2000);assert.equal((await p.locator('.resultScore').innerText()).trim(),'0%');await p.clock.resume();
 await p.screenshot({path:'/tmp/cmmi-'+(mobile?'mobile':'desktop')+'-verified.png',fullPage:true});assert.deepEqual(errors,[]);await context.close();
}
fs.writeFileSync(output,JSON.stringify({status:'passed',results,notes:'Synthetic answer-key tests verify application scoring; not a human/expert examination.'},null,2));console.log('ALL BROWSER CHECKS PASSED',output);
}
run().catch(e=>{console.error(e);fs.writeFileSync(output,JSON.stringify({status:'failed',error:String(e),results},null,2));process.exitCode=1}).finally(async()=>{await browser?.close();server?.close()});
