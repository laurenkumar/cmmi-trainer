// Exercise actual learner flows: no-JS discovery, app handoff, delayed feedback,
// wrong/correct scoring, persistent drafts, separate languages and export/import.
const fs=require('fs'),http=require('http'),path=require('path'),assert=require('assert');
const {chromium}=require('playwright');
const root=path.join(__dirname,'dist'),out=process.env.QA_OUTPUT||'/tmp/cmmi-workshops-results.json';
let server,browser;const results=[];
function serve(){return new Promise(resolve=>{server=http.createServer((req,res)=>{const u=new URL(req.url,'http://localhost');let f=path.join(root,decodeURIComponent(u.pathname));if(!f.startsWith(root+path.sep)&&f!==root){res.writeHead(404).end();return}if(fs.existsSync(f)&&fs.statSync(f).isDirectory())f=path.join(f,'index.html');if(!fs.existsSync(f)){res.writeHead(404).end();return}const type={'.html':'text/html; charset=utf-8','.css':'text/css','.json':'application/json','.vtt':'text/vtt','.mp4':'video/mp4','.xml':'application/xml','.txt':'text/plain'}[path.extname(f)]||'application/octet-stream';res.setHeader('Content-Type',type);fs.createReadStream(f).pipe(res)}).listen(0,'127.0.0.1',()=>resolve('http://127.0.0.1:'+server.address().port))})}
async function run(){
 const local=await serve(),base=process.env.BASE_URL||local;
 const launch=()=>chromium.launch({headless:true,...(process.env.CHROMIUM_CHANNEL?{channel:process.env.CHROMIUM_CHANNEL}:{}),...(process.env.CHROMIUM_PATH?{executablePath:process.env.CHROMIUM_PATH}:{}),args:['--no-sandbox',...(process.env.CHROMIUM_ARGS||'').split(' ').filter(Boolean)]});
 browser=await launch();
 // Every public page has substantive visible content without JavaScript.
 const nojs=await browser.newContext({javaScriptEnabled:false});const plain=await nojs.newPage();
 const xml=await (await plain.request.get(base+'/sitemap.xml')).text();const paths=[...xml.matchAll(/<loc>(.*?)<\/loc>/g)].map(x=>new URL(x[1]).pathname);
 assert.equal(paths.length,95);
 for(const route of paths){const response=await plain.goto(base+route);assert.equal(response.status(),200,route);assert.equal(await plain.locator('h1').count(),1,route);assert((await plain.locator('body').innerText()).length>100,route)}
 results.push({publicPagesNoJavaScript:95});await nojs.close();await browser.close();
 for(const mobile of (process.env.QA_SCREEN==='mobile'?[true]:process.env.QA_SCREEN==='desktop'?[false]:[false,true])){
  browser=await launch();const context=await browser.newContext({viewport:mobile?{width:390,height:844}:{width:1440,height:1000},isMobile:mobile,hasTouch:mobile});const p=await context.newPage();const errors=[];p.on('pageerror',e=>errors.push(e.message));
  for(const lang of ['fr','en']){
   await p.goto(base+'/');const W=await p.evaluate(()=>window.CMMI_DATA.workshops);assert.equal(Object.keys(W).length,31);
   for(const [id,w] of Object.entries(W)){
    console.log('WORKSHOP',mobile,lang,id);
    // The discoverable lesson has a working handoff to the correct workshop.
    await p.goto(base+'/'+lang+'/lessons/pa-'+id.toLowerCase()+'/');
    if(id==='CAR')await p.screenshot({path:'/tmp/cmmi-public-'+lang+'-'+(mobile?'mobile':'desktop')+'.png',fullPage:true});
    assert.equal(await p.locator('h1').count(),1);assert(await p.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+2),`static overflow ${id}/${lang}`);
    await p.locator('a[href*="workshop='+id+'"]').first().click();await p.locator('.workshopBody').waitFor({state:'visible'});assert.equal(await p.locator('.workshopBody').count(),1);assert.equal(await p.locator('html').getAttribute('lang'),lang);
    const activeStep=p.locator('[data-workshop-step="1"]').first();await activeStep.click();assert.equal(await p.locator('.caseFile').count(),3);
    const analysis='D1 and D2 support a bounded conclusion; check D3 before deciding. '+id;
    await p.locator('#workshop-analysis').fill(analysis);await p.reload();assert.equal(await p.locator('#workshop-analysis').inputValue(),analysis);
    await p.locator('[data-workshop-step="2"]').first().click();assert.equal(await p.locator('.masterReview').count(),0);
    for(let i=0;i<2;i++)await p.locator(`[data-workshop-answer="${i}"][value="${(w.questions[i].answer+1)%4}"]`).check();
    assert.equal(await p.locator('.masterReview').count(),0);await p.locator('[data-action=workshop-grade]').click();assert((await p.locator('.workshopScore').innerText()).startsWith('0/2'));assert.equal(await p.locator('.masterReview.invalid').count(),2);
    await p.locator('[data-action=workshop-retry]').click();assert.equal(await p.locator('.masterReview').count(),0);
    for(let i=0;i<2;i++)await p.locator(`[data-workshop-answer="${i}"][value="${w.questions[i].answer}"]`).check();
    await p.locator('[data-action=workshop-grade]').click();assert((await p.locator('.workshopScore').innerText()).startsWith('2/2'));assert.equal(await p.locator('.masterReview.valid').count(),2);
    await p.reload();assert((await p.locator('.workshopScore').innerText()).startsWith('2/2'));
    await p.locator('[data-workshop-step="3"]').first().click();assert(await p.locator('[data-action=workshop-model]').isDisabled());assert.equal(await p.locator('.workshopModel').count(),0);
    const draft='Decision for '+id+': link observed evidence to a bounded action, name an owner and verify the operational result.';
    await p.locator('#workshop-draft').fill(draft);await p.reload();assert.equal(await p.locator('#workshop-draft').inputValue(),draft);
    await p.locator('[data-action=workshop-model]').click();assert((await p.locator('.workshopModel').innerText()).includes(w.sample[lang]));
    for(let i=0;i<4;i++)await p.locator(`[data-workshop-rubric="${i}"]`).check();
    const state=await p.evaluate(({id,lang})=>JSON.parse(localStorage.getItem('cmmi_academy_2027_v1')).workshops[id+'_'+lang],{id,lang});assert.equal(state.best,2);assert.deepEqual(state.rubric,[true,true,true,true]);assert.equal(state.attempts,2);assert.equal(state.draft,draft);
    assert(await p.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+2),`workshop overflow ${id}/${lang}/${mobile}`);
    if(id==='CAR')await p.screenshot({path:'/tmp/cmmi-workshop-'+lang+'-'+(mobile?'mobile':'desktop')+'.png',fullPage:true});
   }
   results.push({screen:mobile?'mobile390':'desktop1440',lang,workshops:31,wrongAttempts:31,correctAttempts:31,draftsReloaded:62});console.log('PASS',mobile,lang,'31 workshop flows');fs.writeFileSync(out,JSON.stringify({status:'running',results},null,2));
  }
  const stored=await p.evaluate(()=>JSON.parse(localStorage.getItem('cmmi_academy_2027_v1')));assert.equal(Object.keys(stored.workshops).length,62);
  // Test export/import through the app, preserving narrative and per-language attempts.
  const nav=async route=>{if(mobile&&!await p.locator('.sidebar').evaluate(el=>el.classList.contains('open')))await p.locator('[data-action=menu]').click();await p.locator(`.sidebar [data-route="${route}"]`).click()};
  await nav('workshops');assert((await p.locator('.workshopRoadmap').innerText()).includes('31/31'));
  await nav('settings');const download=p.waitForEvent('download');await p.locator('[data-action=export]').click();const f=await (await download).path();
  await p.locator('#importfile').setInputFiles(f);assert.deepEqual(await p.evaluate(()=>JSON.parse(localStorage.getItem('cmmi_academy_2027_v1')).workshops),stored.workshops);
  const saved=await p.evaluate(()=>localStorage.getItem('cmmi_academy_2027_v1'));
  await p.locator('#importfile').setInputFiles({name:'invalid.json',mimeType:'application/json',buffer:Buffer.from(JSON.stringify({app:'CMMI Academy',progress:{completed:[],workshops:{CAR_fr:{step:99,answers:{},rubric:[]}}}}))});
  assert.equal(await p.evaluate(()=>localStorage.getItem('cmmi_academy_2027_v1')),saved);
  await p.locator('#importfile').setInputFiles({name:'unsafe-score.json',mimeType:'application/json',buffer:Buffer.from(JSON.stringify({app:'CMMI Academy',progress:{completed:[],workshops:{CAR_fr:{step:2,answers:{0:1,1:3},rubric:[],score:'<img src=x>',graded:true}}}}))});
  assert.equal(await p.evaluate(()=>localStorage.getItem('cmmi_academy_2027_v1')),saved);
  // Existing progress survives the new feature without an assessment reset.
  await p.evaluate(()=>{let s=JSON.parse(localStorage.getItem('cmmi_academy_2027_v1'));s.completed=['F01_fr'];s.scores=[{at:1,total:2,correct:1}];localStorage.setItem('cmmi_academy_2027_v1',JSON.stringify(s))});await p.reload();assert.deepEqual(await p.evaluate(()=>JSON.parse(localStorage.getItem('cmmi_academy_2027_v1')).completed),['F01_fr']);
  assert.deepEqual(errors,[]);await context.close();await browser.close();
 }
 fs.writeFileSync(out,JSON.stringify({status:'passed',results,limits:'Synthetic UI and scoring checks; no human proficiency or search-engine indexing claim.'},null,2));console.log('ALL WORKSHOP AND PUBLIC PAGE CHECKS PASSED');
}
run().catch(e=>{console.error(e);fs.writeFileSync(out,JSON.stringify({status:'failed',error:String(e),results},null,2));process.exitCode=1}).finally(async()=>{await browser?.close();server?.close()});
