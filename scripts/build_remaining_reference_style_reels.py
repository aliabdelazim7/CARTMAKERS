from pathlib import Path
import subprocess, base64
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'social-post-pack-after-pins'
FONT_R=Path('/usr/share/fonts/truetype/noto/NotoSansArabic-Regular.ttf')
FONT_B=Path('/usr/share/fonts/truetype/noto/NotoSansArabic-Bold.ttf')
LOGO_DARK=ROOT/'brand-kit-clean/01-core/logo/cartmakers-primary.svg'
LOGO_LIGHT=ROOT/'brand-kit-clean/01-core/logo/cartmakers-new-logo.webp'
CSS=f'''@font-face{{font-family:Arabic;src:url("{FONT_R.as_uri()}")}}@font-face{{font-family:Arabic;src:url("{FONT_B.as_uri()}");font-weight:800}}*{{box-sizing:border-box}}html,body{{margin:0;width:720px;height:1280px}}body{{font-family:Arabic,Arial;background:#f5f5f2;color:#101828;overflow:hidden}}.scene{{width:720px;height:1280px;position:relative;padding:55px 46px;overflow:hidden;background:#f5f5f2}}.logo{{position:absolute;top:54px;left:46px;width:175px;height:auto}}.tag{{position:absolute;top:70px;right:46px;font:800 14px Arial;letter-spacing:2px;color:#557965}}.hair{{position:absolute;top:142px;left:46px;right:46px;height:1px;background:#10182822}}.title{{position:absolute;right:46px;top:270px;width:635px;text-align:right;font-size:74px;line-height:1.08;font-weight:800;letter-spacing:-2px}}.title span{{color:#557965}}.sub{{position:absolute;right:48px;top:505px;width:520px;text-align:right;font-size:27px;line-height:1.58;color:#344054}}.footer{{position:absolute;bottom:42px;left:46px;right:46px;display:flex;justify-content:space-between;direction:ltr;font:700 15px Arial;color:#667085}}.footer b{{font-family:Arabic;font-size:17px;color:#557965;direction:rtl}}.orb{{position:absolute;border-radius:50%;background:linear-gradient(145deg,#c7f36b,#91b8a0);box-shadow:inset -18px -18px 30px #55796555,18px 24px 28px #10182820}}.orb.one{{width:190px;height:190px;left:28px;top:205px}}.orb.two{{width:102px;height:102px;left:165px;top:128px;background:#101828}}.phone{{position:absolute;right:38px;top:610px;width:360px;height:480px;border:12px solid #101828;border-radius:38px;background:#fff;box-shadow:16px 20px 0 #c7f36b55;transform:rotate(-7deg)}}.phone:before{{content:'';position:absolute;top:0;left:100px;right:100px;height:22px;background:#101828;border-radius:0 0 18px 18px}}.screen{{padding:58px 20px 20px;direction:rtl}}.screen h3{{font-size:24px;margin:0 0 18px}}.product{{height:155px;border-radius:18px;background:linear-gradient(135deg,#101828,#557965);margin-bottom:15px;position:relative}}.product:after{{content:'PRODUCT';position:absolute;bottom:15px;left:16px;color:#fff;font:800 14px Arial;letter-spacing:2px}}.line{{height:12px;background:#e4e7ec;border-radius:10px;margin:11px 0}}.line.short{{width:60%}}.button{{height:44px;margin-top:20px;border-radius:24px;background:#c7f36b;text-align:center;padding:9px;font-weight:800;color:#101828}}.card{{position:absolute;width:305px;min-height:118px;background:#fff;border:2px solid #101828;border-radius:18px;padding:20px;box-shadow:11px 13px 0 #101828;direction:rtl}}.card b{{display:block;font:800 13px Arial;color:#557965;letter-spacing:1px;margin-bottom:9px}}.card h3{{font-size:26px;line-height:1.25;margin:0}}.card.a{{left:28px;top:610px;transform:rotate(7deg)}}.card.b{{left:58px;top:785px;transform:rotate(-5deg);background:#c7f36b}}.card.c{{right:22px;top:800px;transform:rotate(5deg);background:#101828;color:#fff}}.arrow{{position:absolute;font:800 78px Arial;color:#557965}}.a1{{left:210px;top:405px;transform:rotate(18deg)}}.a2{{right:250px;top:555px;transform:rotate(-12deg)}}.blurbar{{position:absolute;left:46px;right:46px;top:1080px;height:9px;background:#10182818;border-radius:5px}}.blurbar:after{{content:'';display:block;width:52%;height:100%;background:#557965;border-radius:5px}}.cta{{position:absolute;right:46px;top:990px;background:#101828;color:#fff;border-radius:30px;padding:17px 28px;font-size:23px;font-weight:800}}.window{{position:absolute;right:35px;top:590px;width:420px;height:390px;border:10px solid #101828;border-radius:24px;background:#fff;box-shadow:15px 18px 0 #c7f36b66;transform:rotate(-4deg);padding:48px 24px 20px;direction:rtl}}.window:before{{content:'●  ●  ●';position:absolute;left:18px;top:10px;font:800 16px Arial;letter-spacing:4px;color:#557965}}.window h3{{font-size:25px;margin:0 0 22px}}.chip{{display:inline-block;border-radius:22px;padding:9px 16px;background:#101828;color:#fff;margin:5px;font-weight:800}}.chip.green{{background:#c7f36b;color:#101828}}.bars{{position:absolute;left:44px;bottom:170px;width:220px;transform:rotate(-8deg)}}.bars i{{display:block;height:24px;border-radius:8px;background:#101828;margin:12px 0}}.bars i:nth-child(2){{width:72%;background:#557965}}.bars i:nth-child(3){{width:47%;background:#c7f36b}}.stack{{position:absolute;right:38px;top:650px;width:330px;height:330px}}.stack .tile{{position:absolute;width:260px;height:105px;border:2px solid #101828;border-radius:18px;padding:17px 20px;font-size:26px;font-weight:800;box-shadow:9px 10px 0 #101828}}.stack .one{{top:0;right:5px;background:#fff;transform:rotate(8deg)}}.stack .two{{top:92px;right:44px;background:#c7f36b;transform:rotate(-4deg)}}.stack .three{{top:184px;right:82px;background:#101828;color:#fff;transform:rotate(5deg)}}.platform{{position:absolute;left:36px;top:610px;width:290px;height:340px;border-radius:28px;background:#101828;color:#fff;padding:34px 24px;transform:rotate(-8deg);box-shadow:15px 18px 0 #c7f36b}}.platform h3{{font:800 38px Arial;margin:0 0 25px}}.platform p{{font-size:25px;line-height:1.6}}'''

REELS={
'02-product-page-checklist':{
 'voice':'reference-demo-voice-energetic.wav','tag':'PRODUCT PAGE SYSTEM','logo':'dark','segments':[
  ('قبل ما تزود<br><span>ميزانية الإعلانات،</span>','راجع صفحة المنتج.','<div class="orb one"></div><div class="orb two"></div><div class="giant">01</div>'),
  ('العميل لازم<br><span>يفهم المنتج بسرعة.</span>','الاسم، الفائدة، والصورة الرئيسية تقود إلى الفهم.','<div class="phone"><div class="screen"><h3>صفحة المنتج</h3><div class="product"></div><div class="line"></div><div class="line short"></div><div class="button">أضف إلى السلة</div></div></div><div class="arrow a1">↗</div>'),
  ('السعر والشحن<br><span>لازم يكونوا واضحين.</span>','المعلومة المتأخرة تضعف القرار.','<div class="card a"><b>PRICE</b><h3>السعر ظاهر</h3></div><div class="card b"><b>SHIPPING</b><h3>الشحن معروف</h3></div><div class="card c"><b>DECISION</b><h3>القرار أسهل</h3></div>'),
  ('صور الاستخدام<br><span>ودليل الثقة.</span>','كل نقطة تجيب عن سؤال حقيقي.','<div class="window"><h3>دليل الثقة</h3><span class="chip green">صور حقيقية</span><span class="chip">مراجعات</span><span class="chip green">ضمان واضح</span></div><div class="bars"><i></i><i></i><i></i></div>'),
  ('خمس نقاط بسيطة،<br><span>لكنها تحدد القرار.</span>','راجع منتجًا واحدًا اليوم.','<div class="cta">راجع المنتج الآن</div><div class="orb one" style="left:430px;top:230px"></div><div class="orb two" style="left:550px;top:170px"></div>')]
},
'03-clean-proof':{
 'voice':'reference-demo-voice-energetic.wav','tag':'CLEAN PROOF SYSTEM','logo':'light','segments':[
  ('المشكلة أحيانًا<br><span>مش في عدد العناصر.</span>','لكن في ترتيبها.','<div class="orb one"></div><div class="orb two"></div><div class="giant">↕</div>'),
  ('الزر مش واضح؟<br><span>العميل هيتردد.</span>','كل خطوة لازم تقود إلى قرار.','<div class="phone"><div class="screen"><h3>اختيار واضح</h3><div class="line"></div><div class="line short"></div><div class="button">اتخذ القرار</div></div></div><div class="arrow a1">↗</div>'),
  ('الشحن بيظهر<br><span>متأخر؟</span>','المفاجأة في النهاية تضعف الثقة.','<div class="stack"><div class="tile one">المنتج</div><div class="tile two">السعر</div><div class="tile three">الشحن</div></div><div class="arrow a2">↘</div>'),
  ('الوصف طويل؟<br><span>اختصر الطريق.</span>','خلّي المعلومة تخدم الاستخدام.','<div class="window" style="top:550px;right:100px;transform:rotate(5deg)"><h3>معلومة واحدة</h3><div class="line"></div><div class="line"></div><div class="line short"></div></div><div class="bars"><i></i><i></i><i></i></div>'),
  ('راجع نقطة واحدة<br><span>في كل مرة.</span>','وخلي كل جزء يخدم قرار الشراء.','<div class="cta">وضّح خطوة واحدة</div><div class="orb one" style="left:430px;top:230px"></div><div class="orb two" style="left:550px;top:170px"></div>')]
},
'04-platform-choice':{
 'voice':'reference-demo-voice-energetic.wav','tag':'PLATFORM DECISION','logo':'dark','segments':[
  ('Shopify ولا<br><span>WooCommerce؟</span>','ده مش أول سؤال.','<div class="platform"><h3>SHOPIFY</h3><p>منصة جاهزة<br>لبداية أسرع</p></div><div class="orb one" style="left:430px;top:230px"></div>'),
  ('ابدأ بـ<br><span>طريقة البيع.</span>','كيف يستقبل العميل الطلب؟','<div class="window"><h3>طريقة البيع</h3><span class="chip green">منتج</span><span class="chip">خدمة</span><span class="chip green">اشتراك</span></div><div class="arrow a1">↗</div>'),
  ('راجع الدفع<br><span>والشحن.</span>','ما الذي يحتاجه التشغيل يوميًا؟','<div class="stack"><div class="tile one">الدفع</div><div class="tile two">الشحن</div><div class="tile three">التشغيل</div></div><div class="arrow a2">↘</div>'),
  ('ومن هيدير<br><span>المتجر؟</span>','المنصة أداة داخل نظام أكبر.','<div class="phone"><div class="screen"><h3>لوحة الإدارة</h3><div class="line"></div><div class="line"></div><div class="line short"></div><div class="button">إدارة الطلبات</div></div></div><div class="bars"><i></i><i></i><i></i></div>'),
  ('اختارها بعد<br><span>ما تفهم الرحلة.</span>','مش قبلها.','<div class="cta">ابدأ من طريقة البيع</div><div class="orb one" style="left:430px;top:230px"></div><div class="orb two" style="left:550px;top:170px"></div>')]
}}

def run(cmd): subprocess.run(cmd,check=True)
def make_sfx(folder):
 click=folder/'reference-click.wav'; whoosh=folder/'reference-whoosh.wav'
 run(['ffmpeg','-y','-hide_banner','-loglevel','error','-f','lavfi','-i','sine=frequency=1300:duration=0.07','-af','afade=t=out:st=0.02:d=0.05,volume=0.28','-ar','48000',str(click)])
 run(['ffmpeg','-y','-hide_banner','-loglevel','error','-f','lavfi','-i','anoisesrc=color=white:duration=0.28:amplitude=0.15','-af','highpass=f=650,lowpass=f=4800,afade=t=in:st=0:d=0.04,afade=t=out:st=0.12:d=0.16,volume=0.36','-ar','48000',str(whoosh)])
 return click,whoosh

def build(slug,data,click,whoosh):
 folder=PACK/slug; frames=folder/'reference-style-frames'; frames.mkdir(exist_ok=True)
 logo_file=LOGO_DARK if data['logo']=='dark' else LOGO_LIGHT
 if logo_file.suffix.lower()=='.svg':
  # browser accepts SVG data URI directly.
  logo_data='data:image/svg+xml;base64,'+base64.b64encode(logo_file.read_bytes()).decode()
 else: logo_data='data:image/webp;base64,'+base64.b64encode(logo_file.read_bytes()).decode()
 scenes=[]
 for i,(title,sub,visual) in enumerate(data['segments'],1):
  scenes.append(f'''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><style>{CSS}</style></head><body><section class="scene">{visual}<img class="logo" src="{logo_data}"><div class="tag">{data['tag']}</div><div class="hair"></div><h1 class="title">{title}</h1><p class="sub">{sub}</p><div class="footer"><span>cart-makers.com</span><b>موشن جرافيك / {i:02d}</b></div></section></body></html>''')
 with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']); page=b.new_page(viewport={'width':720,'height':1280},device_scale_factor=1)
  for i,h in enumerate(scenes,1): page.set_content(h,wait_until='networkidle'); page.screenshot(path=str(frames/f'{i:02d}.png'))
  b.close()
 wav=folder/data['voice']; total=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',str(wav)],text=True).strip())
 weights=[1.08,1.0,1.0,1.0,1.12]; unit=total/sum(weights); ds=[unit*w for w in weights]; trans=.16
 inputs=[]; vf=[]
 for i,d in enumerate(ds):
  inputs += ['-loop','1','-t',f'{d:.3f}','-i',str(frames/f'{i+1:02d}.png')]
  vf.append(f'[{i}:v]zoompan=z=\'min(zoom+0.001,1.06)\':x=\'iw/2-(iw/zoom/2)\':y=\'ih/2-(ih/zoom/2)\':d={round(d*30)}:s=720x1280:fps=30,format=yuv420p,setpts=PTS-STARTPTS[v{i}]')
 current='v0'; offset=ds[0]-trans
 for i in range(1,5):
  out=f'x{i}'; vf.append(f'[{current}][v{i}]xfade=transition=slideleft:duration={trans}:offset={offset:.2f}[{out}]'); current=out; offset+=ds[i]-trans
 audio_inputs=['-i',str(wav),'-i',str(click),'-i',str(whoosh),'-i',str(click),'-i',str(whoosh),'-i',str(click),'-i',str(whoosh),'-i',str(click),'-i',str(whoosh)]
 af=['[5:a]volume=1.0[voice]']; mix=['[voice]']
 for j in range(4):
  ms=round(sum(ds[:j+1])*1000); ci=6+j*2; wi=ci+1
  af += [f'[{ci}:a]adelay={ms}|{ms}[c{j}]',f'[{wi}:a]adelay={ms}|{ms}[w{j}]']; mix += [f'[c{j}]',f'[w{j}]']
 graph=';'.join(vf+af)+f';'+''.join(mix)+f'amix=inputs={len(mix)}:duration=first:normalize=0[a]'
 out=folder/'reference-style-reel.mp4'
 run(['ffmpeg','-y','-hide_banner','-loglevel','error']+inputs+audio_inputs+['-filter_complex',graph,'-map',f'[{current}]','-map','[a]','-t',f'{total:.3f}','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','160k','-ar','48000','-movflags','+faststart',str(out)])
 (folder/'REFERENCE_STYLE_REEL.md').write_text(f'''# Reference Style Reel\n\n- 720×1280 portrait, 9:16.\n- Five editorial motion scenes with large typography and commerce/UI objects.\n- Fast slide transitions ({trans:.2f}s), controlled zoom, and sound effects on each cut.\n- Energetic Egyptian Arabic voice, professional and controlled.\n- Voice source: {data['voice']}\n''',encoding='utf-8')

for slug,data in REELS.items():
 click,whoosh=make_sfx(PACK/slug); build(slug,data,click,whoosh)
(PACK/'REFERENCE_STYLE_REELS_FINAL.md').write_text('''# CartMakers — Reference Style Reels\n\nتم تطبيق نظام النموذج المعتمد على الريلز الثلاثة المتبقية:\n\n- Objects وUI مرتبطة بموضوع كل Reel.\n- Typography كبيرة وسريعة القراءة.\n- انتقالات Slide سريعة وZoom.\n- Sound Effects متزامنة مع نقاط الحركة.\n- صوت مصري حماسي وموحّد.\n- كل Reel محفوظ داخل فولدره مع الـFrames وملف المواصفات.\n''',encoding='utf-8')
print('Built remaining reference-style reels')
