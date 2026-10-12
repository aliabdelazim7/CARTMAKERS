from pathlib import Path
import re, shutil, subprocess

ROOT=Path('/home/ubuntu/CARTMAKERS')
PACK=ROOT/'CartMakers-social-content-pack-final'

def run(cmd):
    subprocess.run(cmd,check=True)

def clean_caption(path: Path):
    text=path.read_text(encoding='utf-8')
    def section(name, next_names):
        m=re.search(rf'^## {re.escape(name)}\s*\n\n(.*?)(?=^## (?:'+'|'.join(map(re.escape,next_names))+r')\s*$|\Z)', text, re.M|re.S)
        return m.group(1).strip() if m else ''
    hook=section('Hook',['Caption جاهز للنشر','CTA','نسخة قصيرة للحملات','Hashtags','ملاحظة تنفيذية'])
    caption=section('Caption جاهز للنشر',['CTA','نسخة قصيرة للحملات','Hashtags','ملاحظة تنفيذية'])
    cta=section('CTA',['نسخة قصيرة للحملات','Hashtags','ملاحظة تنفيذية'])
    hashtags=section('Hashtags',['ملاحظة تنفيذية'])
    clean='\n\n'.join(x for x in [hook,caption,cta,hashtags] if x)
    clean=re.sub(r'\n{3,}','\n\n',clean).strip()+'\n'
    clean='\n'.join(line.replace('**','').removeprefix('> ') for line in clean.splitlines()).strip()+'\n'
    # A plain-text file is the primary copy/paste version; markdown is also kept plain.
    path.write_text(clean,encoding='utf-8')
    path.with_suffix('.txt').write_text(clean,encoding='utf-8')

# Make every video in the delivery pack upload-ready for Meta feed (4:5).
for src in sorted(PACK.rglob('*.mp4')):
    source_dir=src.parent/'source-9x16'
    source_dir.mkdir(exist_ok=True)
    backup=source_dir/src.name
    if not backup.exists():
        shutil.copy2(src,backup)
    tmp=src.with_suffix('.instagram-tmp.mp4')
    # Keep all pixels of the original vertical video. The side extension is a soft,
    # darkened blur of the same footage, so no brand content is cropped.
    vf=("split=2[bg][fg];"
        "[bg]scale=1080:1350:force_original_aspect_ratio=increase," 
        "crop=1080:1350,boxblur=22:10,eq=brightness=-0.08[bg2];"
        "[fg]scale=759:1350:flags=lanczos[fg2];"
        "[bg2][fg2]overlay=(W-w)/2:0:format=auto,format=yuv420p")
    run(['ffmpeg','-y','-hide_banner','-loglevel','error','-i',str(backup),
         '-vf',vf,'-map','0:v:0','-map','0:a?','-c:v','libx264','-preset','medium',
         '-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','160k','-ar','48000',
         '-shortest','-movflags','+faststart',str(tmp)])
    tmp.replace(src)

# Clean all post captions and final-reel captions.
for p in sorted(PACK.rglob('caption.md')):
    clean_caption(p)
for p in sorted((PACK/'03-final-reference-style-reels'/'captions').glob('*.md')):
    clean_caption(p)

(PACK/'INSTAGRAM_UPLOAD_GUIDE.md').write_text('''# Instagram Upload Guide\n\n## الفيديوهات\n\nكل ملفات MP4 الموجودة في أماكنها الأساسية داخل الحزمة أصبحت جاهزة للرفع على Instagram وFacebook Feed بنسبة **4:5** وبمقاس **1080×1350**.\n\n- استخدم ملف الـMP4 الموجود مباشرة داخل فولدر البوست أو داخل `03-final-reference-style-reels`.\n- لا تستخدم الملفات الموجودة داخل `source-9x16`؛ هذه نسخ احتياطية أصلية بنسبة 9:16.\n- الصوت الأصلي محفوظ داخل كل فيديو.\n\n## الكابشن\n\nكل فولدر يحتوي الآن على: \n\n- `caption.md`: نص نظيف للنسخ المباشر.\n- `caption.txt`: النسخة الأسهل للنسخ واللصق.\n\nالكابشن يبدأ بالـHook وينتهي بالـCTA والهاشتاجات فقط، بدون عناوين Markdown أو ملاحظات تنفيذية.\n''',encoding='utf-8')
print('Instagram-ready videos and copy/paste captions prepared')
