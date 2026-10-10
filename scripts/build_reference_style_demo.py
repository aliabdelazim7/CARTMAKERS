from pathlib import Path
import subprocess, base64
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'social-post-pack-after-pins/01-reel-before-ads'
FRAMES=OUT/'reference-demo-frames'; FRAMES.mkdir(exist_ok=True)
VOICE=OUT/'voice.wav'; LOGO=ROOT/'brand-kit-clean/01-core/logo/cartmakers-new-logo.webp'
FONT_R=Path('/usr/share/fonts/truetype/noto/NotoSansArabic-Regular.ttf')
FONT_B=Path('/usr/share/fonts/truetype/noto/NotoSansArabic-Bold.ttf')
logo_data='data:image/webp;base64,'+base64.b64encode(LOGO.read_bytes()).decode()
CSS=f'''@font-face{{font-family:Arabic;src:url("{FONT_R.as_uri()}")}}@font-face{{font-family:Arabic;src:url("{FONT_B.as_uri()}");font-weight:800}}*{{box-sizing:border-box}}html,body{{margin:0;width:720px;height:1280px}}body{{font-family:Arabic,Arial;background:#f5f5f2;color:#101828;overflow:hidden}}.scene{{width:720px;height:1280px;position:relative;padding:55px 46px;overflow:hidden;background:#f5f5f2}}.logo{{position:absolute;top:54px;left:46px;width:175px;height:auto}}.tag{{position:absolute;top:70px;right:46px;font:800 14px Arial;letter-spacing:2px;color:#557965}}.hair{{position:absolute;top:142px;left:46px;right:46px;height:1px;background:#10182822}}.giant{{position:absolute;left:38px;bottom:80px;font:800 190px/0.8 Arial;color:#10182810;letter-spacing:-12px}}.title{{position:absolute;right:46px;top:295px;width:625px;text-align:right;font-size:61px;line-height:1.12;font-weight:800;letter-spacing:-2px}}.title span{{color:#557965}}.sub{{position:absolute;right:48px;top:490px;width:500px;text-align:right;font-size:24px;line-height:1.7;color:#344054}}.footer{{position:absolute;bottom:42px;left:46px;right:46px;display:flex;justify-content:space-between;direction:ltr;font:700 15px Arial;color:#667085}}.footer b{{font-family:Arabic;font-size:17px;color:#557965;direction:rtl}}.orb{{position:absolute;border-radius:50%;background:linear-gradient(145deg,#c7f36b,#91b8a0);box-shadow:inset -18px -18px 30px #55796555,18px 24px 28px #10182820}}.orb.one{{width:175px;height:175px;left:35px;top:220px}}.orb.two{{width:92px;height:92px;left:165px;top:140px;background:#101828}}.phone{{position:absolute;right:46px;top:630px;width:350px;height:470px;border:12px solid #101828;border-radius:38px;background:#fff;box-shadow:16px 20px 0 #c7f36b55;transform:rotate(-7deg)}}.phone:before{{content:'';position:absolute;top:0;left:100px;right:100px;height:22px;background:#101828;border-radius:0 0 18px 18px}}.screen{{padding:58px 20px 20px;direction:rtl}}.screen h3{{font-size:22px;margin:0 0 18px}}.product{{height:150px;border-radius:18px;background:linear-gradient(135deg,#101828,#557965);margin-bottom:15px;position:relative}}.product:after{{content:'PRODUCT';position:absolute;bottom:15px;left:16px;color:#fff;font:800 14px Arial;letter-spacing:2px}}.line{{height:12px;background:#e4e7ec;border-radius:10px;margin:11px 0}}.line.short{{width:60%}}.button{{height:42px;margin-top:20px;border-radius:24px;background:#c7f36b;text-align:center;padding:9px;font-weight:800;color:#101828}}.card{{position:absolute;width:290px;min-height:110px;background:#fff;border:2px solid #101828;border-radius:18px;padding:18px;box-shadow:10px 12px 0 #101828;direction:rtl}}.card b{{display:block;font:800 13px Arial;color:#557965;letter-spacing:1px;margin-bottom:9px}}.card h3{{font-size:23px;line-height:1.3;margin:0}}.card.a{{left:34px;top:620px;transform:rotate(7deg)}}.card.b{{left:65px;top:790px;transform:rotate(-5deg);background:#c7f36b}}.card.c{{right:28px;top:805px;transform:rotate(5deg);background:#101828;color:#fff}}.arrow{{position:absolute;font:800 68px Arial;color:#557965}}.a1{{left:215px;top:420px;transform:rotate(18deg)}}.a2{{right:260px;top:570px;transform:rotate(-12deg)}}.blurbar{{position:absolute;left:46px;right:46px;top:1080px;height:8px;background:#10182818;border-radius:5px}}.blurbar:after{{content:'';display:block;width:52%;height:100%;background:#557965;border-radius:5px}}.cta{{position:absolute;right:46px;top:1000px;background:#101828;color:#fff;border-radius:30px;padding:16px 26px;font-size:20px;font-weight:800}}'''

scenes=[
('01','COMMERCE DIAGNOSTIC','AI? NO','عندك زيارات<br><span>ومفيش طلبات؟</span>','خلّي السؤال ده أول خطوة.','<div class="orb one"></div><div class="orb two"></div><div class="giant">?</div>'),
('02','THE JOURNEY','CLICK → PRODUCT','قبل ما تبدأ<br><span>بالإعلانات،</span>','راجع مسار الطلب من المنتج حتى الـCheckout.','<div class="phone"><div class="screen"><h3>متجر CartMakers</h3><div class="product"></div><div class="line"></div><div class="line short"></div><div class="button">أضف إلى السلة</div></div></div><div class="arrow a1">↗</div>'),
('03','PRODUCT CLARITY','01 / 04','هل المنتج واضح؟<br><span>والشحن مفهوم؟</span>','كل معلومة ناقصة ممكن توقف القرار.','<div class="card a"><b>PRODUCT</b><h3>صورة واضحة</h3></div><div class="card b"><b>SHIPPING</b><h3>التكلفة معروفة</h3></div><div class="card c"><b>TRUST</b><h3>دليل مناسب</h3></div><div class="arrow a2">↘</div>'),
('04','CHECKOUT FRICTION','02 / 04','هل الـCheckout<br><span>سهل على الموبايل؟</span>','التجربة لازم تكون واضحة وسريعة.','<div class="phone" style="top:360px;right:180px;transform:rotate(6deg)"><div class="screen"><h3>تأكيد الطلب</h3><div class="line"></div><div class="line"></div><div class="line short"></div><div class="button">إتمام الطلب</div></div></div><div class="card c" style="top:650px;right:40px;transform:rotate(-8deg)"><b>CHECKOUT</b><h3>أقل احتكاك.<br>قرار أسرع.</h3></div>'),
('05','THE DIAGNOSIS','NEXT STEP','زيادة الزيارات<br><span>مش هتحل الاحتكاك.</span>','ابدأ بالتشخيص.','<div class="orb one" style="left:430px;top:260px"></div><div class="orb two" style="left:540px;top:190px"></div><div class="cta">ابدأ بالتشخيص</div><div class="blurbar"></div>')]

htmls=[]
for num,tag,title,sub,desc,visual in scenes:
 htmls.append(f'''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><style>{CSS}</style></head><body><section class="scene">{visual}<img class="logo" src="{logo_data}"><div class="tag">{tag}</div><div class="hair"></div><h1 class="title">{title}</h1><p class="sub">{sub}</p><div class="footer"><span>cart-makers.com</span><b>موشن جرافيك / {num}</b></div></section></body></html>''')

with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']); page=b.new_page(viewport={'width':720,'height':1280},device_scale_factor=1)
 for i,h in enumerate(htmls,1):
  page.set_content(h,wait_until='networkidle'); page.screenshot(path=str(FRAMES/f'{i:02d}.png'))
 b.close()

# Build a 19-second reel: five visual beats with quick editorial transitions.
click=OUT/'demo-click.wav'; whoosh=OUT/'demo-whoosh.wav'
subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-f','lavfi','-i','sine=frequency=1300:duration=0.07','-af','afade=t=out:st=0.02:d=0.05,volume=0.28','-ar','48000',str(click)],check=True)
subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-f','lavfi','-i','anoisesrc=color=white:duration=0.28:amplitude=0.15','-af','highpass=f=650,lowpass=f=4800,afade=t=in:st=0:d=0.04,afade=t=out:st=0.12:d=0.16,volume=0.36','-ar','48000',str(whoosh)],check=True)

durations=[3.4,3.7,3.6,3.7,3.9]; trans=.28
inputs=[]; vf=[]
for i,d in enumerate(durations):
 inputs += ['-loop','1','-t',str(d),'-i',str(FRAMES/f'{i+1:02d}.png')]
 vf.append(f'[{i}:v]zoompan=z=\'min(zoom+0.001,1.06)\':x=\'iw/2-(iw/zoom/2)\':y=\'ih/2-(ih/zoom/2)\':d={round(d*30)}:s=720x1280:fps=30,format=yuv420p,setpts=PTS-STARTPTS[v{i}]')
current='v0'; offset=durations[0]-trans
for i in range(1,5):
 out=f'x{i}'; vf.append(f'[{current}][v{i}]xfade=transition=slideleft:duration={trans}:offset={offset:.2f}[{out}]'); current=out; offset += durations[i]-trans
# Voice plus effects, with effects delayed at visual cuts.
voice_index=5; audio_inputs=['-i',str(VOICE)]; af=[f'[{voice_index}:a]volume=1.0[voice]']; mix=['[voice]']; input_index=6
for idx in range(4):
 ms=round(sum(durations[:idx+1])*1000)
 audio_inputs += ['-i',str(click),'-i',str(whoosh)]
 af += [f'[{input_index}:a]adelay={ms}|{ms}[c{idx}]',f'[{input_index+1}:a]adelay={ms}|{ms}[w{idx}]']; mix += [f'[c{idx}]',f'[w{idx}]']; input_index+=2
audio_graph=';'.join(af)+f';'+''.join(mix)+f'amix=inputs={len(mix)}:duration=first:normalize=0[a]'
graph=';'.join(vf)+';'+audio_graph
out=OUT/'reference-style-demo.mp4'
subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error']+inputs+audio_inputs+['-filter_complex',graph,'-map',f'[{current}]','-map','[a]','-t','18.3','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','160k','-ar','48000','-movflags','+faststart',str(out)],check=True)
(OUT/'REFERENCE_STYLE_DEMO.md').write_text('''# Reference Style Demo\n\nنموذج تجريبي للريل الأول بأسلوب الفيديو المرجعي:\n\n- Editorial light background with grayscale structure and CartMakers green accent.\n- Animated visual objects: commerce phone, UI cards, checkout card, arrows, and geometric forms.\n- Large kinetic typography with five narrative beats.\n- Slide-left transitions, controlled zoom, progress-like visual movement, and sound effects on cuts.\n- Egyptian Arabic voice-over remains the narrative layer.\n\nThis is a direction test before applying the same visual language to the remaining three Reels.\n''',encoding='utf-8')
print(out)
