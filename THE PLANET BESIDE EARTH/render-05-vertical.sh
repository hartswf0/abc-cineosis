#!/bin/bash
# ═══════════════════════════════════════════════════════════════════
# RENDER 5: VERTICAL SIDE-BY-SIDE (Original top, Derivative bottom)
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

W=720; H=960; FPS=24; CRF=18
FONT="/System/Library/Fonts/Menlo.ttc"
TOTAL=${#DERIVATIVES[@]}

echo "▶ [5] VERTICAL SIDE-BY-SIDE ($TOTAL pairs)..."
VDIR="$OUT_DIR/_vpairs"
mkdir -p "$VDIR"
VCONCAT="$OUT_DIR/_vpairs.txt"
> "$VCONCAT"

for (( i=0; i<TOTAL; i++ )); do
  f="${DERIVATIVES[$i]}"
  s="${LABELS[$i]}"
  num=$((i+1))
  idx=$(printf "%02d" $num)
  echo "  VPair #${idx} ${s}..."
  # Original on top (720x480), derivative on bottom (720x480), total 720x960
  ffmpeg -y -nostdin -hide_banner -loglevel warning -i "$ORIGINAL" -i "$f" -filter_complex "[0:v]scale=720:480:force_original_aspect_ratio=decrease,pad=720:480:(ow-iw)/2:(oh-ih)/2:black,fps=${FPS},setsar=1,drawtext=fontfile=${FONT}:text='%2300 ORIGINAL':fontsize=14:fontcolor=white:borderw=1:bordercolor=black:box=1:boxcolor=black@0.6:boxborderw=3:x=6:y=6,drawtext=fontfile=${FONT}:text='%2300':fontsize=11:fontcolor=white:borderw=1:bordercolor=black:box=1:boxcolor=black@0.5:boxborderw=2:x=680:y=460[top];[1:v]scale=720:480:force_original_aspect_ratio=decrease,pad=720:480:(ow-iw)/2:(oh-ih)/2:black,fps=${FPS},setsar=1,drawtext=fontfile=${FONT}:text='%23${idx} ${s}':fontsize=14:fontcolor=white:borderw=1:bordercolor=black:box=1:boxcolor=black@0.6:boxborderw=3:x=6:y=6,drawtext=fontfile=${FONT}:text='%23${idx}':fontsize=11:fontcolor=white:borderw=1:bordercolor=black:box=1:boxcolor=black@0.5:boxborderw=2:x=680:y=460[bot];[top][bot]vstack=inputs=2[v];[1:a]aresample=44100,aformat=sample_fmts=fltp:channel_layouts=stereo[a]" -map "[v]" -map "[a]" -c:v libx264 -crf $CRF -preset fast -pix_fmt yuv420p -c:a aac -b:a 128k -shortest "$VDIR/${idx}_vpair.mp4"
  echo "file '$VDIR/${idx}_vpair.mp4'" >> "$VCONCAT"
done

echo "  Concatenating..."
ffmpeg -y -nostdin -hide_banner -loglevel warning -f concat -safe 0 -i "$VCONCAT" -c:v libx264 -crf $CRF -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart "$OUT_DIR/05_VERTICAL_PAIRS.mp4"
echo "  ✅ 05_VERTICAL_PAIRS.mp4"

# Cleanup
rm -rf "$VDIR" "$VCONCAT"
echo "✅ Done — $(date '+%H:%M:%S')"
