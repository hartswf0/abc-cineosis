#!/bin/bash
# ═══════════════════════════════════════════════════════════════════
# RENDER 6: CHANNEL SURFING
# Each derivative plays for ~10s, separated by TV static "channel change"
# Static burst: random noise video + white noise audio, ~0.4s
# ═══════════════════════════════════════════════════════════════════
set -eo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

ORIGINAL="ORIGINAL_FRUSTRATED_OPERATOR_202606250441.mp4"
OUT_DIR="$DIR/RENDERS"
mkdir -p "$OUT_DIR"

DERIVATIVES=()
LABELS=()
for f in *.mp4; do
  [[ "$f" == "$ORIGINAL" ]] && continue
  DERIVATIVES+=("$f")
  case "$f" in
    *CLAYMATION*)       LABELS+=("CLAYMATION") ;;
    *Cartoon_Network*)  LABELS+=("CARTOON NETWORK") ;;
    *Cel-shaded*)       LABELS+=("CEL-SHADED 3D") ;;
    *Demon_Slayer*)     LABELS+=("DEMON SLAYER") ;;
    *FRUSTRATED_OPERATOR_202606242345*) LABELS+=("FRUSTRATED OP v1") ;;
    *FRUSTRATED_OPERATOR_202606242348*) LABELS+=("FRUSTRATED OP v2") ;;
    *Glitch_art*)       LABELS+=("GLITCH ART") ;;
    *Historical*)       LABELS+=("HISTORICAL DOC") ;;
    *MTV*)              LABELS+=("MTV MUSIC VIDEO") ;;
    *NPR_PAINTERLY*)    LABELS+=("NPR PAINTERLY") ;;
    *Naruto*)           LABELS+=("NARUTO") ;;
    *One_Piece*)        LABELS+=("ONE PIECE") ;;
    *Pixar*)            LABELS+=("PIXAR CGI") ;;
    *Playful*)          LABELS+=("KIDS SHOW") ;;
    *Pok*)              LABELS+=("POKEMON") ;;
    *Psychedelic*)      LABELS+=("PSYCHEDELIC") ;;
    *Rotoscope*)        LABELS+=("ROTOSCOPE") ;;
    *South_Park*)       LABELS+=("SOUTH PARK") ;;
    *Spider-Verse*)     LABELS+=("SPIDER-VERSE") ;;
    *TCM*)              LABELS+=("TCM CLASSIC") ;;
    *Teleshopping*)     LABELS+=("INFOMERCIAL") ;;
    *True_crime*)       LABELS+=("TRUE CRIME DOC") ;;
    *Planet_Earth*)     LABELS+=("PLANET EARTH") ;;
    *)                  LABELS+=("VARIANT") ;;
  esac
done

W=1280; H=720; FPS=24; CRF=18
FONT="/System/Library/Fonts/Menlo.ttc"
TOTAL=${#DERIVATIVES[@]}

echo "▶ [6] CHANNEL SURFING ($TOTAL channels)..."
CHDIR="$OUT_DIR/_channels"
mkdir -p "$CHDIR"
CHCONCAT="$OUT_DIR/_channels.txt"
> "$CHCONCAT"

# ─── Generate TV static clip (0.4 seconds of snow + white noise) ───
echo "  Generating TV static clip..."
# Random noise video + white noise audio
# geq generates random pixels each frame, giving authentic analog TV snow
ffmpeg -y -nostdin -hide_banner -loglevel warning -f lavfi -i "nullsrc=s=${W}x${H}:r=${FPS}:d=0.4,geq=random(1)*255:128:128" -f lavfi -i "anoisesrc=d=0.4:c=white:r=44100:a=0.3" -c:v libx264 -crf 15 -preset ultrafast -pix_fmt yuv420p -c:a aac -b:a 128k "$CHDIR/static.mp4"

# ─── Generate a longer static clip (1.2s) for the opening ───
echo "  Generating opening static..."
ffmpeg -y -nostdin -hide_banner -loglevel warning -f lavfi -i "nullsrc=s=${W}x${H}:r=${FPS}:d=1.2,geq=random(1)*255:128:128" -f lavfi -i "anoisesrc=d=1.2:c=white:r=44100:a=0.4" -c:v libx264 -crf 15 -preset ultrafast -pix_fmt yuv420p -c:a aac -b:a 128k "$CHDIR/static_long.mp4"

# ─── Normalize original with label + silent audio ───
echo "  Encoding #00 ORIGINAL..."
ffmpeg -y -nostdin -hide_banner -loglevel warning -i "$ORIGINAL" -f lavfi -t 10 -i anullsrc=r=44100:cl=stereo -vf "scale=${W}:${H}:force_original_aspect_ratio=decrease,pad=${W}:${H}:(ow-iw)/2:(oh-ih)/2:black,fps=${FPS},drawtext=fontfile=${FONT}:text='CH 00 -- ORIGINAL':fontsize=22:fontcolor=white:borderw=2:bordercolor=black:box=1:boxcolor=black@0.7:boxborderw=5:x=8:y=8,drawtext=fontfile=${FONT}:text='%2300':fontsize=16:fontcolor=white:borderw=1:bordercolor=black:box=1:boxcolor=black@0.5:boxborderw=3:x=w-tw-8:y=h-th-8" -c:v libx264 -crf $CRF -preset fast -pix_fmt yuv420p -c:a aac -b:a 128k -t 10 "$CHDIR/ch_00.mp4"

# Build concat: opening static → original → static → ch1 → static → ch2 → ...
echo "file '$CHDIR/static_long.mp4'" >> "$CHCONCAT"
echo "file '$CHDIR/ch_00.mp4'" >> "$CHCONCAT"
echo "file '$CHDIR/static.mp4'" >> "$CHCONCAT"

# ─── Encode each derivative as a "channel" ───
for (( i=0; i<TOTAL; i++ )); do
  f="${DERIVATIVES[$i]}"
  s="${LABELS[$i]}"
  num=$((i+1))
  idx=$(printf "%02d" $num)
  echo "  Encoding CH ${idx} ${s}..."
  # Channel label in top-left like a TV OSD, number badge bottom-right
  ffmpeg -y -nostdin -hide_banner -loglevel warning -i "$f" -vf "scale=${W}:${H}:force_original_aspect_ratio=decrease,pad=${W}:${H}:(ow-iw)/2:(oh-ih)/2:black,fps=${FPS},drawtext=fontfile=${FONT}:text='CH ${idx} -- ${s}':fontsize=22:fontcolor=white:borderw=2:bordercolor=black:box=1:boxcolor=black@0.7:boxborderw=5:x=8:y=8,drawtext=fontfile=${FONT}:text='%23${idx}':fontsize=16:fontcolor=white:borderw=1:bordercolor=black:box=1:boxcolor=black@0.5:boxborderw=3:x=w-tw-8:y=h-th-8" -c:v libx264 -crf $CRF -preset fast -pix_fmt yuv420p -c:a aac -b:a 128k -ar 44100 -ac 2 "$CHDIR/ch_${idx}.mp4"
  echo "file '$CHDIR/ch_${idx}.mp4'" >> "$CHCONCAT"
  # Add static between channels (except after the last one)
  if (( i < TOTAL - 1 )); then
    echo "file '$CHDIR/static.mp4'" >> "$CHCONCAT"
  fi
done

# Add closing static
echo "file '$CHDIR/static_long.mp4'" >> "$CHCONCAT"

echo "  Concatenating (static → original → 23 channels → static)..."
ffmpeg -y -nostdin -hide_banner -loglevel warning -f concat -safe 0 -i "$CHCONCAT" -c:v libx264 -crf $CRF -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart "$OUT_DIR/06_CHANNEL_SURFING.mp4"
echo "  ✅ 06_CHANNEL_SURFING.mp4"

# Cleanup
rm -rf "$CHDIR" "$CHCONCAT"
echo "✅ Done — $(date '+%H:%M:%S')"
