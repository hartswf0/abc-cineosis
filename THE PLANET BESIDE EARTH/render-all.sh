#!/bin/bash
# ═══════════════════════════════════════════════════════════════════
# PLANET BESIDE EARTH — MASTER RENDER SCRIPT
# Generates 4 final video compositions from the Frustrated Operator
# Each video is numbered and labeled with its art style
# ═══════════════════════════════════════════════════════════════════
set -eo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

ORIGINAL="ORIGINAL_FRUSTRATED_OPERATOR_202606250441.mp4"
OUT_DIR="$DIR/RENDERS"
mkdir -p "$OUT_DIR"

# ─── Collect all derivative videos ───
DERIVATIVES=()
for f in *.mp4; do
  [[ "$f" == "$ORIGINAL" ]] && continue
  DERIVATIVES+=("$f")
done

# ─── ART STYLE LABELS (parallel array, 0-indexed) ───
LABELS=()
for f in "${DERIVATIVES[@]}"; do
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

# Settings
W=1280; H=720; FPS=24; CRF=18
FONT="/System/Library/Fonts/Menlo.ttc"
TOTAL=${#DERIVATIVES[@]}

echo "═══════════════════════════════════════════════════"
echo "  PLANET BESIDE EARTH — VIDEO COMPOSITOR"
echo "  Original: $ORIGINAL"
echo "  Derivatives: $TOTAL videos"
echo "═══════════════════════════════════════════════════"
echo ""
echo "  VIDEO MANIFEST:"
for (( k=0; k<TOTAL; k++ )); do
  printf "    #%02d  %s\n" $((k+1)) "${LABELS[$k]}"
done
echo ""
echo "Starting renders at $(date '+%H:%M:%S')..."
echo ""

# ═══════════════════════════════════════════════════════════════════
# RENDER 1: SEQUENTIAL MONTAGE
# ═══════════════════════════════════════════════════════════════════
echo "▶ [1/4] SEQUENTIAL MONTAGE..."
NORM_DIR="$OUT_DIR/_norm"
mkdir -p "$NORM_DIR"
CONCAT="$OUT_DIR/_concat.txt"
> "$CONCAT"

echo "  Encoding #00 ORIGINAL..."
ffmpeg -y -nostdin -hide_banner -loglevel warning -i "$ORIGINAL" -f lavfi -t 10 -i anullsrc=r=44100:cl=stereo -vf "scale=${W}:${H}:force_original_aspect_ratio=decrease,pad=${W}:${H}:(ow-iw)/2:(oh-ih)/2:black,fps=${FPS},drawtext=fontfile=${FONT}:text='%2300 ORIGINAL':fontsize=20:fontcolor=white:borderw=2:bordercolor=black:box=1:boxcolor=black@0.6:boxborderw=4:x=8:y=8,drawtext=fontfile=${FONT}:text='%2300':fontsize=14:fontcolor=white:borderw=1:bordercolor=black:box=1:boxcolor=black@0.5:boxborderw=3:x=w-tw-8:y=h-th-8" -c:v libx264 -crf $CRF -preset fast -pix_fmt yuv420p -c:a aac -b:a 128k -t 10 "$NORM_DIR/00_original.mp4"
echo "file '$NORM_DIR/00_original.mp4'" >> "$CONCAT"

for (( i=0; i<TOTAL; i++ )); do
  f="${DERIVATIVES[$i]}"
  s="${LABELS[$i]}"
  num=$((i+1))
  idx=$(printf "%02d" $num)
  safename="${idx}_$(echo "$f" | sed 's/[^a-zA-Z0-9._-]/_/g')"
  echo "  Encoding #${idx} ${s}..."
  ffmpeg -y -nostdin -hide_banner -loglevel warning -i "$f" -vf "scale=${W}:${H}:force_original_aspect_ratio=decrease,pad=${W}:${H}:(ow-iw)/2:(oh-ih)/2:black,fps=${FPS},drawtext=fontfile=${FONT}:text='%23${idx} ${s}':fontsize=20:fontcolor=white:borderw=2:bordercolor=black:box=1:boxcolor=black@0.6:boxborderw=4:x=8:y=8,drawtext=fontfile=${FONT}:text='%23${idx}':fontsize=14:fontcolor=white:borderw=1:bordercolor=black:box=1:boxcolor=black@0.5:boxborderw=3:x=w-tw-8:y=h-th-8" -c:v libx264 -crf $CRF -preset fast -pix_fmt yuv420p -c:a aac -b:a 128k -ar 44100 -ac 2 "$NORM_DIR/${safename}"
  echo "file '$NORM_DIR/${safename}'" >> "$CONCAT"
done

echo "  Concatenating..."
ffmpeg -y -nostdin -hide_banner -loglevel warning -f concat -safe 0 -i "$CONCAT" -c:v libx264 -crf $CRF -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart "$OUT_DIR/01_SEQUENTIAL_MONTAGE.mp4"
echo "  ✅ 01_SEQUENTIAL_MONTAGE.mp4"
echo ""

# ═══════════════════════════════════════════════════════════════════
# RENDER 2: SIDE-BY-SIDE PAIRS
# ═══════════════════════════════════════════════════════════════════
echo "▶ [2/4] SIDE-BY-SIDE PAIRS..."
PAIR_DIR="$OUT_DIR/_pairs"
mkdir -p "$PAIR_DIR"
PCONCAT="$OUT_DIR/_pairs.txt"
> "$PCONCAT"

for (( i=0; i<TOTAL; i++ )); do
  f="${DERIVATIVES[$i]}"
  s="${LABELS[$i]}"
  num=$((i+1))
  idx=$(printf "%02d" $num)
  echo "  Pair #${idx} ${s}..."
  ffmpeg -y -nostdin -hide_banner -loglevel warning -i "$ORIGINAL" -i "$f" -filter_complex "[0:v]scale=640:360:force_original_aspect_ratio=decrease,pad=640:360:(ow-iw)/2:(oh-ih)/2:black,fps=${FPS},setsar=1[left];[1:v]scale=640:360:force_original_aspect_ratio=decrease,pad=640:360:(ow-iw)/2:(oh-ih)/2:black,fps=${FPS},setsar=1[right];[left][right]hstack=inputs=2,drawtext=fontfile=${FONT}:text='%2300 ORIGINAL':fontsize=13:fontcolor=white:borderw=1:bordercolor=black:box=1:boxcolor=black@0.6:boxborderw=3:x=6:y=6,drawtext=fontfile=${FONT}:text='%23${idx} ${s}':fontsize=13:fontcolor=white:borderw=1:bordercolor=black:box=1:boxcolor=black@0.6:boxborderw=3:x=646:y=6,drawtext=fontfile=${FONT}:text='%2300':fontsize=11:fontcolor=white:borderw=1:bordercolor=black:box=1:boxcolor=black@0.5:boxborderw=2:x=600:y=340,drawtext=fontfile=${FONT}:text='%23${idx}':fontsize=11:fontcolor=white:borderw=1:bordercolor=black:box=1:boxcolor=black@0.5:boxborderw=2:x=1240:y=340[v];[1:a]aresample=44100,aformat=sample_fmts=fltp:channel_layouts=stereo[a]" -map "[v]" -map "[a]" -c:v libx264 -crf $CRF -preset fast -pix_fmt yuv420p -c:a aac -b:a 128k -shortest "$PAIR_DIR/${idx}_pair.mp4"
  echo "file '$PAIR_DIR/${idx}_pair.mp4'" >> "$PCONCAT"
done

echo "  Concatenating..."
ffmpeg -y -nostdin -hide_banner -loglevel warning -f concat -safe 0 -i "$PCONCAT" -c:v libx264 -crf $CRF -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart "$OUT_DIR/02_SIDE_BY_SIDE_PAIRS.mp4"
echo "  ✅ 02_SIDE_BY_SIDE_PAIRS.mp4"
echo ""

# ═══════════════════════════════════════════════════════════════════
# RENDER 3: BLEND / DISSOLVE
# ═══════════════════════════════════════════════════════════════════
echo "▶ [3/4] BLEND COMPOSITIONS..."
BLEND_DIR="$OUT_DIR/_blends"
mkdir -p "$BLEND_DIR"
BCONCAT="$OUT_DIR/_blends.txt"
> "$BCONCAT"

for (( i=0; i<TOTAL; i++ )); do
  f="${DERIVATIVES[$i]}"
  s="${LABELS[$i]}"
  num=$((i+1))
  idx=$(printf "%02d" $num)
  echo "  Blend #${idx} ${s}..."
  ffmpeg -y -nostdin -hide_banner -loglevel warning -i "$ORIGINAL" -i "$f" -filter_complex "[0:v]scale=${W}:${H}:force_original_aspect_ratio=decrease,pad=${W}:${H}:(ow-iw)/2:(oh-ih)/2:black,fps=${FPS},setsar=1,trim=0:10,setpts=PTS-STARTPTS[ov];[1:v]scale=${W}:${H}:force_original_aspect_ratio=decrease,pad=${W}:${H}:(ow-iw)/2:(oh-ih)/2:black,fps=${FPS},setsar=1,trim=0:10,setpts=PTS-STARTPTS[dv];[ov][dv]xfade=transition=dissolve:duration=6:offset=2,drawtext=fontfile=${FONT}:text='ORIGINAL > %23${idx} ${s}':fontsize=18:fontcolor=white:borderw=2:bordercolor=black:box=1:boxcolor=black@0.6:boxborderw=4:x=10:y=10,drawtext=fontfile=${FONT}:text='%23${idx}':fontsize=14:fontcolor=white:borderw=1:bordercolor=black:box=1:boxcolor=black@0.5:boxborderw=3:x=w-tw-10:y=h-th-10[v];[1:a]aresample=44100,afade=t=in:st=0:d=3,afade=t=out:st=7:d=3[a]" -map "[v]" -map "[a]" -c:v libx264 -crf $CRF -preset fast -pix_fmt yuv420p -c:a aac -b:a 128k -shortest "$BLEND_DIR/${idx}_blend.mp4"
  echo "file '$BLEND_DIR/${idx}_blend.mp4'" >> "$BCONCAT"
done

echo "  Concatenating..."
ffmpeg -y -nostdin -hide_banner -loglevel warning -f concat -safe 0 -i "$BCONCAT" -c:v libx264 -crf $CRF -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart "$OUT_DIR/03_BLEND_DISSOLVE.mp4"
echo "  ✅ 03_BLEND_DISSOLVE.mp4"
echo ""

# ═══════════════════════════════════════════════════════════════════
# RENDER 4: 2×2 GRID
# ═══════════════════════════════════════════════════════════════════
echo "▶ [4/4] 2x2 GRID..."
GRID_DIR="$OUT_DIR/_grids"
mkdir -p "$GRID_DIR"
GCONCAT="$OUT_DIR/_grids.txt"
> "$GCONCAT"

grid_num=0
i=0
while (( i < TOTAL )); do
  grid_num=$((grid_num + 1))
  gidx=$(printf "%02d" $grid_num)

  di1=$(( i % TOTAL ))
  di2=$(( (i + 1) % TOTAL ))
  di3=$(( (i + 2) % TOTAL ))
  d1="${DERIVATIVES[$di1]}"; s1="${LABELS[$di1]}"; n1=$(printf "%02d" $((di1+1)))
  d2="${DERIVATIVES[$di2]}"; s2="${LABELS[$di2]}"; n2=$(printf "%02d" $((di2+1)))
  d3="${DERIVATIVES[$di3]}"; s3="${LABELS[$di3]}"; n3=$(printf "%02d" $((di3+1)))

  echo "  Grid $gidx: #00 ORIG | #${n1} ${s1} | #${n2} ${s2} | #${n3} ${s3}"

  ffmpeg -y -nostdin -hide_banner -loglevel warning -i "$ORIGINAL" -i "$d1" -i "$d2" -i "$d3" -filter_complex "[0:v]scale=640:360:force_original_aspect_ratio=decrease,pad=640:360:(ow-iw)/2:(oh-ih)/2:black,fps=${FPS},setsar=1[tl];[1:v]scale=640:360:force_original_aspect_ratio=decrease,pad=640:360:(ow-iw)/2:(oh-ih)/2:black,fps=${FPS},setsar=1[tr];[2:v]scale=640:360:force_original_aspect_ratio=decrease,pad=640:360:(ow-iw)/2:(oh-ih)/2:black,fps=${FPS},setsar=1[bl];[3:v]scale=640:360:force_original_aspect_ratio=decrease,pad=640:360:(ow-iw)/2:(oh-ih)/2:black,fps=${FPS},setsar=1[br];[tl][tr]hstack=inputs=2[top];[bl][br]hstack=inputs=2[bot];[top][bot]vstack=inputs=2,drawtext=fontfile=${FONT}:text='%2300 ORIGINAL':fontsize=12:fontcolor=white:borderw=1:bordercolor=black:box=1:boxcolor=black@0.65:boxborderw=3:x=6:y=6,drawtext=fontfile=${FONT}:text='%23${n1} ${s1}':fontsize=12:fontcolor=white:borderw=1:bordercolor=black:box=1:boxcolor=black@0.65:boxborderw=3:x=646:y=6,drawtext=fontfile=${FONT}:text='%23${n2} ${s2}':fontsize=12:fontcolor=white:borderw=1:bordercolor=black:box=1:boxcolor=black@0.65:boxborderw=3:x=6:y=366,drawtext=fontfile=${FONT}:text='%23${n3} ${s3}':fontsize=12:fontcolor=white:borderw=1:bordercolor=black:box=1:boxcolor=black@0.65:boxborderw=3:x=646:y=366,drawtext=fontfile=${FONT}:text='%2300':fontsize=10:fontcolor=white:borderw=1:bordercolor=black:box=1:boxcolor=black@0.5:boxborderw=2:x=600:y=340,drawtext=fontfile=${FONT}:text='%23${n1}':fontsize=10:fontcolor=white:borderw=1:bordercolor=black:box=1:boxcolor=black@0.5:boxborderw=2:x=1240:y=340,drawtext=fontfile=${FONT}:text='%23${n2}':fontsize=10:fontcolor=white:borderw=1:bordercolor=black:box=1:boxcolor=black@0.5:boxborderw=2:x=600:y=700,drawtext=fontfile=${FONT}:text='%23${n3}':fontsize=10:fontcolor=white:borderw=1:bordercolor=black:box=1:boxcolor=black@0.5:boxborderw=2:x=1240:y=700[v];[1:a]volume=0.35,aresample=44100[a1];[2:a]volume=0.35,aresample=44100[a2];[3:a]volume=0.35,aresample=44100[a3];[a1][a2][a3]amix=inputs=3:duration=shortest:weights=1 1 1[a]" -map "[v]" -map "[a]" -c:v libx264 -crf $CRF -preset fast -pix_fmt yuv420p -c:a aac -b:a 192k -shortest "$GRID_DIR/${gidx}_grid.mp4"
  echo "file '$GRID_DIR/${gidx}_grid.mp4'" >> "$GCONCAT"

  i=$((i + 3))
done

echo "  Concatenating $grid_num grids..."
ffmpeg -y -nostdin -hide_banner -loglevel warning -f concat -safe 0 -i "$GCONCAT" -c:v libx264 -crf $CRF -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart "$OUT_DIR/04_GRID_2x2.mp4"
echo "  ✅ 04_GRID_2x2.mp4"
echo ""

# ═══════════════════════════════════════════════════════════════════
echo "═══════════════════════════════════════════════════"
echo "  ALL RENDERS COMPLETE — $(date '+%H:%M:%S')"
echo "═══════════════════════════════════════════════════"
ls -lh "$OUT_DIR"/0*.mp4 2>/dev/null
echo ""
echo "Cleaning intermediates..."
rm -rf "$OUT_DIR/_norm" "$OUT_DIR/_pairs" "$OUT_DIR/_blends" "$OUT_DIR/_grids"
rm -f "$OUT_DIR/_concat.txt" "$OUT_DIR/_pairs.txt" "$OUT_DIR/_blends.txt" "$OUT_DIR/_grids.txt"
echo "✅ Done."
