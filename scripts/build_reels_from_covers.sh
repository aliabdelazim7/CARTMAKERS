#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/social-post-pack-after-pins"

build_reel() {
  local dir="$1"; local bg="$2"; local cover="$OUT/$dir/01.png"; local voice="$OUT/$dir/voice.wav"; local output="$OUT/$dir/reel.mp4"; local spec="$OUT/$dir/reel-spec.md"
  local duration frames
  duration=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$voice")
  frames=$(python3 - "$duration" <<'PY'
import sys, math
print(max(1, math.ceil(float(sys.argv[1])*30)))
PY
)
  ffmpeg -y -hide_banner -loglevel error \
    -loop 1 -i "$cover" -i "$voice" \
    -filter_complex "[0:v]zoompan=z='min(zoom+0.00045,1.045)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=$frames:s=1080x1350:fps=30,format=yuv420p,pad=1080:1920:0:285:color=$bg,fade=t=in:st=0:d=0.35,fade=t=out:st=$(python3 - "$duration" <<'PY'
import sys
print(max(0,float(sys.argv[1])-.4))
PY
):d=0.4[v]" \
    -map "[v]" -map 1:a -t "$duration" -c:v libx264 -preset medium -crf 19 -pix_fmt yuv420p \
    -c:a aac -b:a 160k -ar 48000 -movflags +faststart "$output"
  cat > "$spec" <<EOF
# Reel Production Spec

- **Format:** MP4, vertical 9:16, 1080×1920.
- **Visual treatment:** Motion graphics built from the approved CartMakers cover; subtle controlled zoom and fade, no generated characters, no distorted logos, no fake claims.
- **Voice:** Same male Egyptian Arabic voice profile across all four Reels (Charon, ar-EG), calm and confident.
- **Duration:** ${duration}s.
- **Audio:** Clean voice-over, no competing background music.
- **Source cover:** 01.png.
- **Voice source:** voice.wav.
EOF
}

build_reel "01-reel-before-ads" "#101828"
build_reel "02-product-page-checklist" "#101828"
build_reel "03-clean-proof" "#f7f8f5"
build_reel "04-platform-choice" "#101828"

cat > "$OUT/REELS_README.md" <<'EOF'
# CartMakers — Generated Egyptian-Voice Reels

تم تحديث الحزمة بأربعة Reels عمودية جاهزة للنشر:

1. `01-reel-before-ads/reel.mp4`
2. `02-product-page-checklist/reel.mp4`
3. `03-clean-proof/reel.mp4`
4. `04-platform-choice/reel.mp4`

## المواصفات

- MP4، مقاس 1080×1920، نسبة 9:16.
- صوت رجل مصري واحد ثابت، هادئ وواثق.
- حركة Motion Graphics خفيفة على التصميمات المعتمدة.
- لا توجد شخصيات أو لقطات مولدة قد تشوّه النص العربي أو الشعار.
- لا توجد موسيقى تنافس التعليق الصوتي.
- ملفات `voice.wav` و`reel-spec.md` محفوظة بجانب كل Reel.

تم اختيار موشن جرافيك منظم بدل لقطات AI عشوائية حتى يبدو المحتوى مصممًا يدويًا بواسطة Agency حقيقية ويحافظ على وضوح الهوية والنص العربي.
EOF
