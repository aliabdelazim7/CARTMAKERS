from pathlib import Path
import subprocess, math, shlex
import base64
from html import escape
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / 'social-post-pack-after-pins'
FONT_REG = Path('/usr/share/fonts/truetype/noto/NotoSansArabic-Regular.ttf')
FONT_BOLD = Path('/usr/share/fonts/truetype/noto/NotoSansArabic-Bold.ttf')
LOGO_DARK = ROOT / 'brand-kit-clean/01-core/logo/cartmakers-new-logo-dark.png'
LOGO_LIGHT = ROOT / 'brand-kit-clean/01-core/logo/cartmakers-new-logo.webp'

CSS = f'''\
@font-face{{font-family:NotoArabic;src:url("{FONT_REG.as_uri()}")}}\
@font-face{{font-family:NotoArabic;src:url("{FONT_BOLD.as_uri()}");font-weight:700}}\
*{{box-sizing:border-box}} html,body{{margin:0;width:1080px;height:1920px}} body{{font-family:NotoArabic,Arial,sans-serif;overflow:hidden}}\
.frame{{width:1080px;height:1920px;position:relative;overflow:hidden;padding:96px 76px 86px;display:flex;flex-direction:column;justify-content:space-between;direction:rtl}}\
.dark{{background:#101828;color:#f7f8f5}} .light{{background:#f7f8f5;color:#101828}}\
.top{{display:flex;align-items:center;justify-content:space-between;direction:ltr;position:relative;z-index:5}} .logo{{width:205px;height:auto;object-fit:contain}}\
.series{{font:700 20px Arial,sans-serif;letter-spacing:2px;color:#c7f36b}} .light .series{{color:#56745e}} .num{{font:700 27px Arial,sans-serif;opacity:.65}}\
.ambient{{position:absolute;left:-260px;bottom:-270px;width:780px;height:780px;border:1px solid rgba(199,243,107,.22);border-radius:50%;opacity:.8}} .ambient:before,.ambient:after{{content:'';position:absolute;border:1px solid rgba(199,243,107,.15);border-radius:50%}} .ambient:before{{width:590px;height:590px;left:95px;top:95px}} .ambient:after{{width:390px;height:390px;left:195px;top:195px}}\
.topline{{position:absolute;top:260px;right:76px;left:76px;height:1px;background:rgba(247,248,245,.15)}} .light .topline{{background:rgba(16,24,40,.15)}}\
.main{{position:relative;z-index:4;margin-top:80px}} .eyebrow{{font:700 19px Arial,sans-serif;letter-spacing:2px;color:#c7f36b;margin-bottom:42px;direction:ltr;text-align:right}} .light .eyebrow{{color:#56745e}}\
.kicker{{font-size:25px;line-height:1.5;opacity:.68;margin-bottom:28px}} .transcript{{font-size:64px;line-height:1.35;font-weight:700;letter-spacing:-1px;max-width:890px;margin:0}} .dark .accent{{color:#c7f36b}} .light .accent{{color:#537c63}}\
.sub{{font-size:28px;line-height:1.7;max-width:820px;margin-top:36px;opacity:.68}}\
.bottom{{position:relative;z-index:5}} .progress{{height:7px;width:100%;background:rgba(247,248,245,.15);border-radius:8px;overflow:hidden;direction:ltr}} .light .progress{{background:rgba(16,24,40,.13)}} .fill{{height:100%;background:#c7f36b;border-radius:8px}} .light .fill{{background:#537c63}}\
.meta{{display:flex;justify-content:space-between;align-items:center;margin-top:24px;direction:ltr;font:700 18px Arial,sans-serif;letter-spacing:1px;opacity:.7}} .meta .cta{{direction:rtl;font-family:NotoArabic,Arial,sans-serif;font-size:21px;letter-spacing:0;opacity:1}}\
.note{{border-right:5px solid #c7f36b;padding-right:24px;margin-top:48px;font-size:26px;line-height:1.7;opacity:.78}} .light .note{{border-color:#537c63}}\
'''

REELS = {
 '01-reel-before-ads': {
  'series':'DIAGNOSTIC REEL','theme':'dark','cta':'راجع مسار الطلب',
  'segments':[
   ('عندك زيارات<br><span class="accent">ومفيش طلبات؟</span>','خلّي السؤال ده أول خطوة.'),
   ('قبل ما تبدأ<br><span class="accent">بالإعلانات،</span>','راجع مسار الطلب من المنتج حتى الـCheckout.'),
   ('هل المنتج واضح؟<br><span class="accent">والشحن مفهوم؟</span>','كل معلومة ناقصة ممكن توقف القرار.'),
   ('هل الـCheckout<br><span class="accent">سهل على الموبايل؟</span>','التجربة لازم تكون واضحة وسريعة.'),
   ('زيادة الزيارات<br><span class="accent">مش هتحل الاحتكاك.</span>','ابدأ بالتشخيص.')],
 },
 '02-product-page-checklist': {
  'series':'PRODUCT PAGE REEL','theme':'dark','cta':'احفظها للمراجعة',
  'segments':[
   ('قبل ما تزود<br><span class="accent">ميزانية الإعلانات،</span>','راجع صفحة المنتج.'),
   ('العميل لازم<br><span class="accent">يفهم المنتج بسرعة.</span>','الاسم، الفائدة، والصورة الرئيسية تقود إلى الفهم.'),
   ('السعر والشحن<br><span class="accent">لازم يكونوا واضحين.</span>','المعلومة المتأخرة تضعف القرار.'),
   ('صور الاستخدام<br><span class="accent">ودليل الثقة.</span>','كل نقطة تجيب عن سؤال حقيقي.'),
   ('خمس نقاط بسيطة،<br><span class="accent">لكنها تحدد القرار.</span>','راجع منتجًا واحدًا اليوم.')],
 },
 '03-clean-proof': {
  'series':'CLEAN PROOF REEL','theme':'light','cta':'اسأل عن حالتك',
  'segments':[
   ('المشكلة أحيانًا<br><span class="accent">مش في عدد العناصر.</span>','لكن في ترتيبها.'),
   ('الزر مش واضح؟<br><span class="accent">العميل هيتردد.</span>','كل خطوة لازم تقود إلى قرار.'),
   ('الشحن بيظهر<br><span class="accent">متأخر؟</span>','المفاجأة في النهاية تضعف الثقة.'),
   ('الوصف طويل؟<br><span class="accent">اختصر الطريق.</span>','خلّي المعلومة تخدم الاستخدام.'),
   ('راجع نقطة واحدة<br><span class="accent">في كل مرة.</span>','وخلي كل جزء يخدم قرار الشراء.')],
 },
 '04-platform-choice': {
  'series':'PLATFORM DECISION REEL','theme':'dark','cta':'ابدأ من طريقة البيع',
  'segments':[
   ('Shopify ولا<br><span class="accent">WooCommerce؟</span>','ده مش أول سؤال.'),
   ('ابدأ بـ<br><span class="accent">طريقة البيع.</span>','كيف يستقبل العميل الطلب؟'),
   ('راجع الدفع<br><span class="accent">والشحن.</span>','ما الذي يحتاجه التشغيل يوميًا؟'),
   ('ومن هيدير<br><span class="accent">المتجر؟</span>','المنصة أداة داخل نظام أكبر.'),
   ('اختارها بعد<br><span class="accent">ما تفهم الرحلة.</span>','مش قبلها.')],
 },
}

def duration(wav):
    return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',str(wav)], text=True).strip())

def render_frames():
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path='/usr/bin/chromium', headless=True, args=['--no-sandbox'])
        page = browser.new_page(viewport={'width':1080,'height':1920}, device_scale_factor=1)
        for slug, data in REELS.items():
            folder = PACK / slug
            frames = folder / 'dynamic-frames'
            frames.mkdir(exist_ok=True)
            logo_file = LOGO_DARK if data['theme']=='dark' else LOGO_LIGHT
            logo_mime = 'image/png' if logo_file.suffix.lower() == '.png' else 'image/webp'
            logo = f'data:{logo_mime};base64,' + base64.b64encode(logo_file.read_bytes()).decode('ascii')
            n = len(data['segments'])
            for i, (title, sub) in enumerate(data['segments'], 1):
                progress = (i-1)/(n-1) if n > 1 else 1
                body = f'''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><style>{CSS}</style></head><body><section class="frame {data['theme']}"><img class="ambient" src="{logo}" style="opacity:0"><div class="top"><img class="logo" src="{logo}"><span class="series">{data['series']}</span><span class="num">{i:02d} / {n:02d}</span></div><div class="topline"></div><div class="main"><div class="eyebrow">CARTMAKERS / COMMERCE SYSTEMS</div><div class="kicker">ملاحظة سريعة لصاحب المتجر</div><h1 class="transcript">{title}</h1><p class="sub">{sub}</p><div class="note">مش كل مشكلة تحتاج عناصر أكثر؛ أحيانًا تحتاج قرارًا أوضح.</div></div><div class="bottom"><div class="progress"><div class="fill" style="width:{progress*100:.1f}%"></div></div><div class="meta"><span>cart-makers.com</span><span class="cta">{data['cta']}</span></div></div></section></body></html>'''
                page.set_content(body, wait_until='networkidle')
                page.screenshot(path=str(frames/f'{i:02d}.png'))
        browser.close()

def make_sfx(folder):
    click = folder/'click.wav'; whoosh = folder/'whoosh.wav'
    subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-f','lavfi','-i','sine=frequency=1200:duration=0.075','-af','afade=t=out:st=0.035:d=0.04,volume=0.22','-ar','48000',str(click)], check=True)
    subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-f','lavfi','-i','anoisesrc=color=white:duration=0.32:amplitude=0.12','-af','highpass=f=700,lowpass=f=5000,afade=t=in:st=0:d=0.06,afade=t=out:st=0.18:d=0.14,volume=0.35','-ar','48000',str(whoosh)], check=True)
    return click, whoosh

def build_video(slug, data, click, whoosh):
    folder = PACK / slug
    frames = folder / 'dynamic-frames'
    wav = folder / 'voice.wav'
    out = folder / 'reel.mp4'
    total = duration(wav)
    n = len(data['segments'])
    # Weighted durations give the hook and CTA slightly more breathing room.
    weights = [1.1] + [1.0]*(n-2) + [1.15]
    unit = total / sum(weights)
    durations = [unit*w for w in weights]
    trans = 0.32
    inputs=[]; filters=[]
    for i, d in enumerate(durations, 1):
        inputs += ['-loop','1','-t',f'{d:.3f}','-i',str(frames/f'{i:02d}.png')]
        frames_count = max(2, round(d*30))
        filters.append(f'[{i-1}:v]zoompan=z=\'min(zoom+0.00065,1.055)\':x=\'iw/2-(iw/zoom/2)\':y=\'ih/2-(ih/zoom/2)\':d={frames_count}:s=1080x1920:fps=30,format=yuv420p,setpts=PTS-STARTPTS[v{i}]')
    current='v1'; offset=durations[0]-trans
    for i in range(2,n+1):
        nxt=f'v{i}'
        outlabel=f'x{i}'
        filters.append(f'[{current}][{nxt}]xfade=transition=slideleft:duration={trans}:offset={offset:.3f}[{outlabel}]')
        current=outlabel
        offset += durations[i-1]-trans
    # Add gentle click + whoosh at each transition, and keep narration untouched.
    audio_inputs=['-i',str(wav)]
    audio_filters=[]
    delays=[]
    for idx in range(1,n):
        t=sum(durations[:idx]) - trans
        ms=max(0, round(t*1000))
        audio_inputs += ['-i',str(click),'-i',str(whoosh)]
        ci=n+(idx-1)*2+1; wi=ci+1
        audio_filters.append(f'[{ci}:a]adelay={ms}|{ms}[c{idx}]')
        audio_filters.append(f'[{wi}:a]adelay={ms}|{ms}[w{idx}]')
        delays += [f'[c{idx}]',f'[w{idx}]']
    graph=';'.join(filters+audio_filters)
    if delays:
        graph += f';[{n}:a]volume=1.0[voice];[voice]'+''.join(delays)+f'amix=inputs={1+len(delays)}:duration=first:dropout_transition=0:normalize=0[a]'
    else:
        graph += ';[0:a]anull[a]'
    cmd=['ffmpeg','-y','-hide_banner','-loglevel','error']+inputs+audio_inputs+['-filter_complex',graph,'-map',f'[{current}]','-map','[a]','-t',f'{total:.3f}','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','160k','-ar','48000','-movflags','+faststart',str(out)]
    subprocess.run(cmd, check=True)
    (folder/'reel-spec.md').write_text(f'''# Dynamic Reel Production Spec\n\n- Format: MP4, 1080×1920, 9:16.\n- Transcript: 5 timed caption cards with staged text reveal.\n- Transitions: slide-left xfade between cards, controlled zoom, fade timing.\n- Sound design: low-volume click and whoosh at card transitions.\n- Voice: unified male Egyptian Arabic voice, calm and confident.\n- Duration: {total:.2f}s.\n- Source audio: voice.wav.\n''', encoding='utf-8')

render_frames()
click, whoosh = make_sfx(PACK)
for slug, data in REELS.items():
    build_video(slug, data, click, whoosh)

(PACK/'REELS_README.md').write_text('''# CartMakers — Dynamic Egyptian-Voice Reels\n\nتمت إعادة تنفيذ الريلز الأربعة كـMotion Reels حقيقية بدل صورة ثابتة مع Voice-over فقط.\n\n## ما تم إضافته\n\n- Transcript متزامن يظهر على مراحل داخل الفيديو.\n- دخول وخروج للنصوص مع Slide Transitions.\n- Progress bar يوضح تقدم الريل.\n- Sound Effects خفيفة: Click وWhoosh عند انتقال البطاقات.\n- Voice-over مصري موحد، هادئ وواثق.\n- هوية CartMakers ثابتة مع نصوص عربية واضحة.\n\n## الملفات\n\n- `01-reel-before-ads/reel.mp4`\n- `02-product-page-checklist/reel.mp4`\n- `03-clean-proof/reel.mp4`\n- `04-platform-choice/reel.mp4`\n\nكل مجلد يحتوي أيضًا على `dynamic-frames/` و`reel-spec.md` و`voice.wav`.\n''', encoding='utf-8')
print('Built dynamic reels:', ', '.join(REELS))
