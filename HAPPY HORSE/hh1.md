C ============================================================
C  HAPPY HORSE: SHE'S JUST A HAPPY HORSE
C  BEFLIX ANIMATION SCRIPT — FULL EXPANDED VERSION
C  128x96 GRID / 8 GRAYSCALE LEVELS (0-7)
C  COMMANDS: CLR PNT LIN REC SHF ZOM DIS CPY
C  EACH SCENE 5x DETAIL — NATURAL MOVEMENT EMPHASIS
C ============================================================
C
C  SCENE INDEX:
C  01 - EXT ITALIAN PASTURE LATE AFTERNOON (ESTABLISHING)
C  02 - EXT ITALIAN PASTURE DAY (CALYPSO GRAZING CLOSE)
C  03 - EXT OGYGIA MYTHIC TIME (CALYPSO THE NYMPH)
C  04 - INT ANTHROPIC BOARDROOM DAY (AI SAFETY DISCUSSION)
C  05 - INT ANTHROPIC OFFICE DAY (SAFETY REPORTS)
C  06 - INT COURTROOM DAY (COPYRIGHT CLAIMS)
C  07 - EXT 19TH CENTURY FARM ROAD DAY (HORSE AS TECH)
C  08 - EXT PALO ALTO RACETRACK 1878 (MUYBRIDGE)
C  09 - INT LAW SCHOOL LECTURE HALL NIGHT (LAW OF THE HORSE)
C  10 - EXT CONNECTICUT ROAD 1871 (HASLEM V LOCKWOOD)
C  11 - INT DATA CENTER NIGHT (TOKENS TO GRADIENTS)
C  12 - INT MUSIC PUBLISHER OFFICE DAY (SONGWRITERS)
C  13 - INT AI LAB DAY (TRAINING RUNS)
C  14 - INT POLICY FORUM DAY (JOB DISRUPTION)
C  15 - EXT ITALIAN PASTURE SUNSET (CALYPSO MOTIONLESS)
C  16 - EXT MODERN CITY NIGHT (INFRASTRUCTURE MONTAGE)
C  17 - EXT ITALIAN PASTURE NIGHT (HORSE REMAINS)
C  18 - INT FUTURE DATA CENTER UNKNOWN (AI INVISIBLE)
C  19 - EXT ITALIAN PASTURE MORNING (CALYPSO LOOKS UP)
C  20 - FINAL IMAGE NIGHT (CONSTELLATION AND HORSE)
C
C ============================================================
C  SCENE 01: EXT ITALIAN PASTURE — LATE AFTERNOON
C  ESTABLISHING SHOT — WIDE LANDSCAPE
C  The rolling hills of an Italian countryside fill the frame.
C  Warm late-afternoon light saturates the grass.
C  A single horse figure stands small in the composition.
C  Distant hills layer into soft atmospheric perspective.
C  Fence posts trace a diagonal from lower-left.
C ============================================================
C
C --- FRAME 01.001: BASE LANDSCAPE CONSTRUCTION ---
C Clear to sky gradient base
CLR 0
C Sky — upper third — soft light gray
PNT 0 0 128 32 1
C Sky highlight band — golden hour light at horizon
PNT 0 28 128 6 2
C Distant hills — layer 3 — softest
PNT 0 30 128 8 1
PNT 20 30 88 6 2
PNT 35 31 58 4 1
C Distant hills — layer 2
PNT 0 36 128 6 2
PNT 10 35 40 5 3
PNT 70 35 50 5 3
PNT 50 36 28 4 2
C Midground hills — rolling contour
PNT 0 40 128 8 3
PNT 5 39 35 6 2
PNT 60 38 45 7 3
PNT 105 39 20 6 2
C Grass field — main ground plane — warm middle tone
PNT 0 46 128 50 3
C Grass texture — subtle variation strips
PNT 0 48 128 2 4
PNT 0 54 128 2 2
PNT 0 60 128 2 4
PNT 0 66 128 2 2
PNT 0 72 128 2 4
PNT 0 78 128 2 3
PNT 0 84 128 2 4
C Foreground grass — darker and richer
PNT 0 88 128 8 4
PNT 0 90 128 6 5
C Ground shadow at very bottom
PNT 0 94 128 2 4
C
C --- Sun glow at horizon ---
PNT 90 26 14 6 2
PNT 93 27 8 4 1
C
C --- Cloud wisps in sky ---
PNT 15 8 22 3 2
PNT 18 9 16 2 1
PNT 50 5 30 3 2
PNT 54 6 22 2 1
PNT 95 10 20 3 2
PNT 98 11 14 2 1
C
C --- FENCE POSTS --- diagonal line from lower-left
C Post 1
PNT 8 70 2 16 5
LIN 8 70 9 70 6
C Post 2
PNT 18 64 2 14 5
LIN 18 64 19 64 6
C Post 3
PNT 28 58 2 12 5
LIN 28 58 29 58 6
C Post 4
PNT 38 52 2 10 5
LIN 38 52 39 52 6
C Post 5
PNT 48 46 2 8 5
LIN 48 46 49 46 6
C Fence wire connecting posts
LIN 8 74 18 68 4
LIN 18 68 28 62 4
LIN 28 62 38 56 4
LIN 38 56 48 50 4
C Lower fence wire
LIN 8 78 18 72 4
LIN 18 72 28 66 4
LIN 28 66 38 60 4
LIN 38 60 48 54 4
C
C --- HORSE FIGURE — small in wide landscape ---
C Body — barrel shape
PNT 78 56 12 6 5
PNT 79 55 10 4 6
C Neck — angled upward-left
PNT 76 50 4 6 5
PNT 77 51 2 4 6
C Head — small block at top of neck
PNT 74 48 4 3 5
PNT 75 49 2 2 6
C Legs — four thin verticals
LIN 80 62 80 68 5
LIN 82 62 82 68 5
LIN 87 62 87 68 5
LIN 89 62 89 68 5
C Hooves — dark points
PNT 79 68 2 2 6
PNT 81 68 2 2 6
PNT 86 68 2 2 6
PNT 88 68 2 2 6
C Tail — flowing line
LIN 90 56 94 54 5
LIN 94 54 96 56 4
LIN 96 56 97 54 5
C Ear
PNT 74 47 1 2 6
PNT 75 47 1 2 6
C Eye
PNT 75 49 1 1 7
C
C --- TREE silhouette right side ---
C Trunk
PNT 112 48 3 30 5
PNT 113 50 2 26 6
C Canopy
PNT 105 34 18 16 4
PNT 107 36 14 12 5
PNT 109 38 10 8 4
C
REC 8
C
C --- FRAME 01.002: LIGHT SHIFT — golden hour intensifies ---
C Warm the horizon band
PNT 0 26 128 6 2
PNT 85 25 20 8 1
C Brighten sun glow
PNT 91 27 10 5 1
PNT 93 28 6 3 0
C Deepen foreground shadow slightly
PNT 0 90 128 6 5
C Horse shadow on grass
PNT 78 68 14 3 4
C
REC 4
C
C --- FRAME 01.003: CLOUD DRIFT — wisps shift right ---
C Erase old cloud positions
PNT 15 8 22 3 1
PNT 50 5 30 3 1
PNT 95 10 20 3 1
C Redraw clouds shifted 2px right
PNT 17 8 22 3 2
PNT 19 9 16 2 1
PNT 52 5 30 3 2
PNT 56 6 22 2 1
PNT 97 10 20 3 2
PNT 100 11 14 2 1
C
REC 3
C
C --- FRAME 01.004: HORSE EAR FLICK ---
C Erase old ear position
PNT 74 47 2 2 5
C Draw ear rotated back
PNT 74 46 2 2 6
PNT 75 46 1 1 7
C
REC 2
C
C --- FRAME 01.005: HORSE EAR RETURNS ---
PNT 74 46 2 2 5
PNT 74 47 1 2 6
PNT 75 47 1 2 6
C
REC 2
C
C --- FRAME 01.006: GRASS WIND RIPPLE — left to right ---
C Brighten strips to simulate wind pushing grass
PNT 0 54 40 2 3
PNT 0 60 40 2 3
PNT 0 72 40 2 3
C
REC 2
C
C --- FRAME 01.007: WIND RIPPLE CONTINUES ---
PNT 0 54 40 2 4
PNT 40 54 40 2 3
PNT 0 60 40 2 4
PNT 40 60 40 2 3
PNT 0 72 40 2 4
PNT 40 72 40 2 3
C
REC 2
C
C --- FRAME 01.008: WIND RIPPLE MOVES THROUGH ---
PNT 40 54 40 2 4
PNT 80 54 48 2 3
PNT 40 60 40 2 4
PNT 80 60 48 2 3
PNT 40 72 40 2 4
PNT 80 72 48 2 3
C
REC 2
C
C --- FRAME 01.009: WIND RIPPLE EXITS RIGHT ---
PNT 80 54 48 2 4
PNT 80 60 48 2 4
PNT 80 72 48 2 4
C Restore grass baseline
PNT 0 54 128 2 2
PNT 0 60 128 2 4
PNT 0 72 128 2 4
C
REC 2
C
C --- FRAME 01.010: HORSE TAIL SWISH LEFT ---
C Erase old tail
PNT 90 53 8 5 3
LIN 90 56 94 54 3
LIN 94 54 96 56 3
LIN 96 56 97 54 3
C Draw tail swished left
LIN 90 56 92 53 5
LIN 92 53 91 50 4
LIN 91 50 92 48 5
C
REC 3
C
C --- FRAME 01.011: HORSE TAIL RETURNS CENTER ---
C Erase swished tail
PNT 90 48 4 10 3
LIN 90 56 92 53 3
LIN 92 53 91 50 3
LIN 91 50 92 48 3
C Redraw natural tail
LIN 90 56 94 54 5
LIN 94 54 96 56 4
LIN 96 56 97 54 5
C
REC 3
C
C --- FRAME 01.012: HORSE TAIL SWISH RIGHT ---
C Erase natural tail
LIN 90 56 94 54 3
LIN 94 54 96 56 3
LIN 96 56 97 54 3
C Draw tail swished further right
LIN 90 56 95 52 5
LIN 95 52 98 54 4
LIN 98 54 100 52 5
C
REC 3
C
C --- FRAME 01.013: TAIL SETTLES BACK ---
LIN 90 56 95 52 3
LIN 95 52 98 54 3
LIN 98 54 100 52 3
PNT 90 52 12 6 3
C Restore tail natural
LIN 90 56 94 54 5
LIN 94 54 96 56 4
LIN 96 56 97 54 5
C
REC 4
C
C --- FRAME 01.014: SECOND CLOUD DRIFT ---
PNT 17 8 22 3 1
PNT 52 5 30 3 1
PNT 97 10 20 3 1
PNT 19 8 22 3 2
PNT 21 9 16 2 1
PNT 54 5 30 3 2
PNT 58 6 22 2 1
PNT 99 10 20 3 2
PNT 102 11 14 2 1
C
REC 3
C
C --- FRAME 01.015: HORSE HEAD LOWERS — beginning to graze ---
C Erase old head position
PNT 74 48 4 3 5
PNT 75 49 2 2 3
C Erase old neck
PNT 76 50 4 6 3
C Redraw neck angled down
PNT 76 52 4 6 5
PNT 77 53 2 4 6
C Redraw head lower
PNT 73 58 5 3 5
PNT 74 59 3 2 6
C Eye at new position
PNT 74 59 1 1 7
C Ear at new position
PNT 73 57 1 2 6
PNT 74 57 1 2 6
C
REC 4
C
C --- FRAME 01.016: HORSE HEAD AT GRASS LEVEL ---
C Lower head further — grazing position
PNT 73 58 5 3 3
PNT 76 52 4 6 3
C Redraw neck stretched down
PNT 76 54 3 8 5
PNT 77 55 2 6 6
C Head at grass
PNT 72 62 6 3 5
PNT 73 63 4 2 6
C Eye
PNT 73 63 1 1 7
C Ear
PNT 72 61 2 2 6
C Muzzle touching grass — highlight
PNT 72 65 6 1 3
C
REC 6
C
C --- FRAME 01.017: GRASS RESPONDS TO GRAZING ---
C Small bright patch where horse eats — grass disturbed
PNT 70 66 10 2 2
PNT 72 67 6 2 3
C
REC 3
C
C --- FRAME 01.018: HORSE HEAD RISES SLIGHTLY ---
C Lift head 2px
PNT 72 62 6 3 3
PNT 72 60 6 3 5
PNT 73 61 4 2 6
PNT 73 61 1 1 7
PNT 72 59 2 2 6
C Restore grass where head was
PNT 70 64 10 4 3
C
REC 3
C
C --- FRAME 01.019: HORSE HEAD LOWERS AGAIN ---
PNT 72 60 6 3 3
PNT 72 63 6 3 5
PNT 73 64 4 2 6
PNT 73 64 1 1 7
PNT 72 62 2 2 6
PNT 72 66 6 1 3
C
REC 5
C
C --- FRAME 01.020: LIGHT FADES SLIGHTLY — time passing ---
C Darken sky subtly
PNT 0 0 128 28 2
C Warm the hill shadows
PNT 0 40 128 6 4
C Deepen foreground
PNT 0 92 128 4 5
C
REC 4
C
C --- FRAME 01.021: HORSE WEIGHT SHIFT — subtle leg movement ---
C Left front leg shifts
LIN 80 62 80 68 3
LIN 79 62 79 68 5
C
REC 3
C
C --- FRAME 01.022: LEG RETURNS ---
LIN 79 62 79 68 3
LIN 80 62 80 68 5
C
REC 3
C
C --- FRAME 01.023: FINAL ESTABLISHING HOLD ---
C Long hold on the landscape — let the viewer absorb
C No changes — just record the current state
C
REC 12
C
C
C ============================================================
C  SCENE 02: EXT ITALIAN PASTURE — DAY
C  MEDIUM CLOSE ON CALYPSO GRAZING
C  Dario Amodei sits nearby on the grass.
C  The horse fills the left half of frame.
C  Amodei is a quiet figure to the right.
C  Emphasis on the horse's simple contentment.
C ============================================================
C
C --- FRAME 02.001: BASE COMPOSITION ---
CLR 0
C Sky — clear blue-gray
PNT 0 0 128 24 1
C Distant treeline
PNT 0 22 128 4 3
PNT 10 22 20 3 4
PNT 45 22 30 3 4
PNT 85 22 25 3 4
C Ground plane — grass
PNT 0 26 128 70 3
C Grass texture
PNT 0 30 128 2 4
PNT 0 38 128 2 2
PNT 0 46 128 2 4
PNT 0 54 128 2 2
PNT 0 62 128 2 4
PNT 0 70 128 2 3
PNT 0 78 128 2 4
PNT 0 86 128 2 2
C Foreground grass — rich dark
PNT 0 90 128 6 4
C
C --- CALYPSO — large horse figure left side ---
C Body — large barrel
PNT 12 38 40 20 5
PNT 14 40 36 16 6
PNT 16 42 32 12 5
C Belly underline
LIN 12 58 52 58 6
C Back line — slight arch
LIN 14 38 48 36 6
LIN 48 36 52 38 5
C
C Neck — thick angled up-left
PNT 8 24 10 16 5
PNT 9 26 8 12 6
PNT 10 28 6 8 5
C
C Head — detailed
PNT 2 18 12 8 5
PNT 3 19 10 6 6
PNT 4 20 8 4 5
C Jaw line
LIN 2 26 8 26 5
LIN 2 26 2 22 6
C Muzzle
PNT 1 22 4 4 4
PNT 2 23 2 2 5
C Nostril
PNT 2 24 1 1 7
C Eye — prominent
PNT 6 20 2 2 7
PNT 7 21 1 1 0
C Ear — left
PNT 4 16 2 4 6
PNT 5 16 1 3 7
C Ear — right
PNT 8 16 2 4 6
PNT 9 16 1 3 7
C Forelock — hair between ears
PNT 5 17 4 2 5
C
C Mane — flowing down neck
LIN 9 24 12 28 5
LIN 10 26 13 30 6
LIN 11 28 14 32 5
LIN 12 30 15 34 6
C
C Front legs
C Left front
LIN 18 58 18 76 5
LIN 19 58 19 76 6
PNT 17 76 3 2 6
C Right front
LIN 26 58 26 76 5
LIN 27 58 27 76 6
PNT 25 76 3 2 6
C Knee detail on front legs
PNT 17 66 3 2 5
PNT 25 66 3 2 5
C
C Back legs
C Left back
LIN 40 56 38 76 5
LIN 41 56 39 76 6
PNT 37 76 3 2 6
C Right back
LIN 48 56 46 76 5
LIN 49 56 47 76 6
PNT 45 76 3 2 6
C Hock joint detail
PNT 37 68 3 3 5
PNT 45 68 3 3 5
C
C Tail — long flowing
LIN 52 38 58 34 5
LIN 58 34 60 36 4
LIN 60 36 62 32 5
LIN 62 32 63 34 4
LIN 63 34 64 30 5
C
C --- DARIO AMODEI — seated figure right side ---
C Torso — seated on ground
PNT 88 54 12 16 5
PNT 90 56 8 12 6
C Head
PNT 90 44 8 10 4
PNT 91 45 6 8 5
C Hair
PNT 91 44 6 3 6
C Face features
PNT 93 48 1 1 7
PNT 95 48 1 1 7
LIN 93 51 95 51 6
C Arm resting on knee
LIN 88 58 84 68 5
LIN 84 68 86 70 5
C Other arm behind
PNT 100 58 3 8 5
C Legs — crossed/folded
PNT 84 68 18 6 5
LIN 84 70 100 72 6
PNT 84 72 16 4 6
C Shoe hints
PNT 82 72 3 2 6
PNT 100 72 3 2 6
C
C --- Shadow beneath horse ---
PNT 10 76 46 3 4
C --- Shadow beneath Amodei ---
PNT 82 74 20 2 4
C
REC 8
C
C --- FRAME 02.002: CALYPSO CHEWS — jaw movement ---
C Erase old jaw
LIN 2 26 8 26 3
PNT 1 24 4 3 3
C Jaw opens slightly
LIN 2 27 8 27 5
PNT 1 25 4 3 4
PNT 2 26 1 1 7
C
REC 2
C
C --- FRAME 02.003: JAW CLOSES ---
LIN 2 27 8 27 3
PNT 1 25 4 3 3
LIN 2 26 8 26 5
PNT 1 22 4 4 4
PNT 2 23 2 2 5
PNT 2 24 1 1 7
C
REC 2
C
C --- FRAME 02.004: CALYPSO CHEWS AGAIN ---
LIN 2 26 8 26 3
PNT 1 24 4 3 3
LIN 2 27 8 27 5
PNT 1 25 4 3 4
C
REC 2
C
C --- FRAME 02.005: JAW CLOSES ---
LIN 2 27 8 27 3
LIN 2 26 8 26 5
PNT 1 22 4 4 4
PNT 2 24 1 1 7
C
REC 2
C
C --- FRAME 02.006: CALYPSO CHEWS THIRD TIME ---
LIN 2 26 8 26 3
LIN 2 27 8 27 5
PNT 1 25 4 3 4
C
REC 2
C
C --- FRAME 02.007: JAW CLOSES FINAL ---
LIN 2 27 8 27 3
LIN 2 26 8 26 5
PNT 1 22 4 4 4
PNT 2 24 1 1 7
C
REC 3
C
C --- FRAME 02.008: CALYPSO EAR ROTATION — left ear rotates ---
C Erase left ear
PNT 4 16 2 4 5
C Rotate ear back
PNT 3 15 2 3 6
PNT 4 15 1 2 7
C
REC 2
C
C --- FRAME 02.009: LEFT EAR FORWARD AGAIN ---
PNT 3 15 2 3 5
PNT 4 16 2 4 6
PNT 5 16 1 3 7
C
REC 2
C
C --- FRAME 02.010: RIGHT EAR ROTATES ---
PNT 8 16 2 4 5
PNT 9 15 2 3 6
PNT 10 15 1 2 7
C
REC 2
C
C --- FRAME 02.011: RIGHT EAR FORWARD ---
PNT 9 15 2 3 5
PNT 8 16 2 4 6
PNT 9 16 1 3 7
C
REC 2
C
C --- FRAME 02.012: TAIL SWISH LEFT — slow arc ---
C Erase tail
PNT 52 30 14 10 3
C Tail position 1 — swinging left
LIN 52 38 56 35 5
LIN 56 35 55 32 4
LIN 55 32 54 28 5
LIN 54 28 52 26 4
C
REC 2
C
C --- FRAME 02.013: TAIL SWISH CONTINUES LEFT ---
PNT 52 26 8 14 3
LIN 52 38 54 35 5
LIN 54 35 52 32 4
LIN 52 32 50 28 5
LIN 50 28 48 26 4
C
REC 2
C
C --- FRAME 02.014: TAIL SWINGS BACK RIGHT ---
PNT 48 26 8 14 3
LIN 52 38 56 34 5
LIN 56 34 58 32 4
LIN 58 32 60 28 5
LIN 60 28 62 26 4
C
REC 2
C
C --- FRAME 02.015: TAIL SWINGS FURTHER RIGHT ---
PNT 56 26 8 10 3
LIN 52 38 58 34 5
LIN 58 34 62 32 4
LIN 62 32 64 28 5
LIN 64 28 66 26 4
C
REC 2
C
C --- FRAME 02.016: TAIL SETTLES NATURAL ---
PNT 58 26 10 10 3
C Restore natural tail
LIN 52 38 58 34 5
LIN 58 34 60 36 4
LIN 60 36 62 32 5
LIN 62 32 63 34 4
LIN 63 34 64 30 5
C
REC 4
C
C --- FRAME 02.017: AMODEI HEAD TURN — looks toward horse ---
C Erase old face direction
PNT 93 48 1 1 5
PNT 95 48 1 1 5
LIN 93 51 95 51 5
C Redraw face looking left toward Calypso
PNT 91 48 1 1 7
PNT 93 48 1 1 7
LIN 91 51 93 51 6
C
REC 4
C
C --- FRAME 02.018: AMODEI HEAD RETURNS CENTER ---
PNT 91 48 1 1 5
LIN 91 51 93 51 5
PNT 93 48 1 1 7
PNT 95 48 1 1 7
LIN 93 51 95 51 6
C
REC 3
C
C --- FRAME 02.019: CALYPSO HEAD LIFTS SLIGHTLY ---
C Small head raise — breaks grazing
PNT 2 18 12 8 3
C Redraw head 2px higher
PNT 2 16 12 8 5
PNT 3 17 10 6 6
PNT 6 18 2 2 7
PNT 7 19 1 1 0
PNT 4 14 2 4 6
PNT 8 14 2 4 6
C Ears up
PNT 5 14 1 2 7
PNT 9 14 1 2 7
C Adjust neck
PNT 8 22 10 4 5
PNT 9 24 8 2 6
C
REC 5
C
C --- FRAME 02.020: CALYPSO HEAD LOWERS BACK ---
C Head returns to grazing position
PNT 2 16 12 8 3
PNT 2 18 12 8 5
PNT 3 19 10 6 6
PNT 6 20 2 2 7
PNT 7 21 1 1 0
PNT 4 16 2 4 6
PNT 8 16 2 4 6
PNT 5 16 1 3 7
PNT 9 16 1 3 7
C Neck normal
PNT 8 22 10 4 5
PNT 9 24 8 4 6
C
REC 4
C
C --- FRAME 02.021: GRASS WIND WAVE ---
PNT 0 38 30 2 2
PNT 0 46 30 2 3
PNT 0 54 30 2 3
C
REC 2
C
C --- FRAME 02.022: WIND WAVE PASSES ---
PNT 0 38 30 2 4
PNT 30 38 30 2 2
PNT 0 46 30 2 4
PNT 30 46 30 2 3
PNT 0 54 30 2 4
PNT 30 54 30 2 3
C
REC 2
C
C --- FRAME 02.023: WIND WAVE EXITS ---
PNT 30 38 30 2 4
PNT 60 38 30 2 2
PNT 30 46 30 2 4
PNT 60 46 30 2 3
PNT 30 54 30 2 4
PNT 60 54 30 2 3
C
REC 2
C
C --- FRAME 02.024: WIND WAVE EXITS FULLY ---
PNT 60 38 68 2 4
PNT 60 46 68 2 4
PNT 60 54 68 2 4
C Restore grass
PNT 0 38 128 2 2
PNT 0 46 128 2 4
PNT 0 54 128 2 2
C
REC 2
C
C --- FRAME 02.025: CALYPSO WEIGHT SHIFT ---
C Right front leg lifts slightly
LIN 26 58 26 76 3
LIN 27 58 27 76 3
C Reposition leg — bent at knee
LIN 26 58 26 66 5
LIN 26 66 24 68 5
LIN 24 68 24 74 5
PNT 23 74 3 2 6
C
REC 3
C
C --- FRAME 02.026: LEG RETURNS ---
PNT 23 68 4 8 3
LIN 26 58 26 76 5
LIN 27 58 27 76 6
PNT 25 76 3 2 6
C
REC 3
C
C --- FRAME 02.027: CALYPSO BLINKS ---
C Close eye
PNT 6 20 2 2 5
C
REC 1
C
C --- FRAME 02.028: EYE OPENS ---
PNT 6 20 2 2 7
PNT 7 21 1 1 0
C
REC 2
C
C --- FRAME 02.029: AMODEI SLIGHT BODY SHIFT ---
C Subtle lean forward
PNT 88 54 12 16 3
PNT 87 55 12 16 5
PNT 89 57 8 12 6
C
REC 3
C
C --- FRAME 02.030: AMODEI LEANS BACK ---
PNT 87 55 12 16 3
PNT 88 54 12 16 5
PNT 90 56 8 12 6
C
REC 4
C
C --- FRAME 02.031: HOLD ON SCENE — peaceful moment ---
REC 10
C
C
C ============================================================
C  SCENE 03: EXT OGYGIA — MYTHIC TIME
C  Calypso the nymph offers immortality to Odysseus.
C  Mythological landscape — cave, sea, starlight.
C  Luminous figure of Calypso, weathered Odysseus.
C  The sea churns behind them.
C  Stars wheel slowly overhead.
C ============================================================
C
C --- FRAME 03.001: BASE MYTHIC LANDSCAPE ---
CLR 0
C Night sky — deep dark
PNT 0 0 128 30 1
C Stars scattered
PNT 12 4 1 1 3
PNT 28 8 1 1 2
PNT 44 3 1 1 3
PNT 56 10 1 1 2
PNT 68 5 1 1 3
PNT 80 2 1 1 2
PNT 92 7 1 1 3
PNT 104 4 1 1 2
PNT 116 9 1 1 3
PNT 20 12 1 1 2
PNT 36 6 1 1 3
PNT 72 11 1 1 2
PNT 100 3 1 1 3
PNT 8 14 1 1 2
PNT 50 16 1 1 3
PNT 88 13 1 1 2
PNT 120 6 1 1 3
C Brighter stars — constellation hints
PNT 40 5 2 2 3
PNT 60 3 2 2 3
PNT 82 8 2 2 3
C
C Sea — dark undulating bands
PNT 0 28 128 20 2
PNT 0 30 128 4 1
PNT 0 36 128 4 2
PNT 0 40 128 4 1
PNT 0 44 128 4 2
C Wave crests — white foam lines
LIN 0 30 20 28 3
LIN 20 28 40 30 3
LIN 40 30 60 28 3
LIN 60 28 80 30 3
LIN 80 30 100 28 3
LIN 100 28 127 30 3
C Second wave line
LIN 0 36 25 34 2
LIN 25 34 50 36 2
LIN 50 36 75 34 2
LIN 75 34 100 36 2
LIN 100 36 127 34 2
C
C Shore — rocky beach
PNT 0 48 128 8 3
PNT 0 50 128 4 4
C Rock textures
PNT 5 48 4 4 4
PNT 20 49 6 3 5
PNT 40 48 5 4 4
PNT 60 49 3 3 5
PNT 80 48 7 4 4
PNT 100 49 4 3 5
PNT 115 48 5 4 4
C
C Cave entrance — dark arch left side
PNT 0 30 30 66 4
PNT 2 32 26 62 5
PNT 4 34 22 58 6
C Cave arch opening
PNT 6 50 18 30 2
PNT 8 52 14 26 1
PNT 10 54 10 22 0
C Cave interior depth — very dark
PNT 12 56 6 16 0
C Vine tendrils hanging from cave arch
LIN 6 50 8 56 3
LIN 10 50 11 54 3
LIN 22 50 21 55 3
LIN 24 50 23 56 3
C
C Ground inside cave — warm glow
PNT 6 78 18 8 2
PNT 8 80 14 6 3
C Fire glow — warm light source inside cave
PNT 14 72 4 6 3
PNT 15 73 2 4 4
PNT 15 74 2 2 5
C Firelight flickering on cave wall
PNT 4 60 4 8 2
PNT 22 58 4 10 2
C
C --- CALYPSO THE NYMPH — luminous figure ---
C Standing near cave entrance
C Body — tall radiant form
PNT 34 42 8 30 3
PNT 35 44 6 26 4
PNT 36 46 4 22 3
C Robe flowing
LIN 34 72 30 78 3
LIN 42 72 46 78 3
PNT 30 76 16 4 3
C Head — bright, luminous
PNT 35 34 6 8 4
PNT 36 35 4 6 5
PNT 37 36 2 4 4
C Hair — long, flowing left
LIN 35 34 30 32 4
LIN 30 32 26 34 3
LIN 26 34 24 38 4
LIN 35 36 31 38 3
LIN 31 38 28 42 4
C Hair right side
LIN 41 34 44 36 4
LIN 44 36 45 40 3
C Face
PNT 37 37 1 1 6
PNT 39 37 1 1 6
LIN 37 40 39 40 5
C
C Arms — extended offering gesture
LIN 34 52 28 48 4
LIN 28 48 26 46 5
LIN 42 52 50 46 4
LIN 50 46 52 44 5
C Hands — open palms
PNT 24 44 4 3 4
PNT 51 42 4 3 4
C
C Glow around Calypso — divine radiance
PNT 30 38 18 36 2
PNT 32 40 14 32 1
C
C --- ODYSSEUS — weathered figure sitting ---
C Positioned right side looking toward sea
C Body — seated hunched
PNT 80 52 14 20 4
PNT 82 54 10 16 5
C Head — bearded, weathered
PNT 84 42 8 10 4
PNT 85 43 6 8 5
PNT 86 44 4 6 4
C Beard
PNT 84 50 8 4 5
PNT 85 51 6 2 6
C Eyes — distant gaze toward sea/horizon
PNT 86 45 1 1 6
PNT 89 45 1 1 6
C Hair — tangled
PNT 84 42 8 3 6
PNT 85 42 6 2 5
C
C Arms — one resting on knee, one on ground
LIN 80 56 76 66 5
PNT 74 65 4 3 5
LIN 94 56 98 66 5
PNT 97 65 4 3 5
C Legs — extended
PNT 76 68 22 6 4
LIN 76 70 98 72 5
C Feet
PNT 74 72 4 3 5
PNT 98 72 4 3 5
C
C --- Staff/oar leaning beside Odysseus ---
LIN 100 40 104 74 5
LIN 101 41 105 74 4
C
REC 8
C
C --- FRAME 03.002: WAVE ANIMATION — crests shift right ---
C Erase old wave crests
LIN 0 30 20 28 2
LIN 20 28 40 30 2
LIN 40 30 60 28 2
LIN 60 28 80 30 2
LIN 80 30 100 28 2
LIN 100 28 127 30 2
C Redraw shifted right 3px
LIN 3 30 23 28 3
LIN 23 28 43 30 3
LIN 43 30 63 28 3
LIN 63 28 83 30 3
LIN 83 30 103 28 3
LIN 103 28 127 30 3
C
REC 2
C
C --- FRAME 03.003: WAVE CRESTS SHIFT FURTHER ---
LIN 3 30 23 28 2
LIN 23 28 43 30 2
LIN 43 30 63 28 2
LIN 63 28 83 30 2
LIN 83 30 103 28 2
LIN 103 28 127 30 2
C Shift another 3px
LIN 6 30 26 28 3
LIN 26 28 46 30 3
LIN 46 30 66 28 3
LIN 66 28 86 30 3
LIN 86 30 106 28 3
LIN 106 28 127 30 3
C
REC 2
C
C --- FRAME 03.004: WAVE CRESTS RETURN ---
LIN 6 30 26 28 2
LIN 26 28 46 30 2
LIN 46 30 66 28 2
LIN 66 28 86 30 2
LIN 86 30 106 28 2
LIN 106 28 127 30 2
C Back to original position
LIN 0 30 20 28 3
LIN 20 28 40 30 3
LIN 40 30 60 28 3
LIN 60 28 80 30 3
LIN 80 30 100 28 3
LIN 100 28 127 30 3
C
REC 2
C
C --- FRAME 03.005: FIRE FLICKER IN CAVE ---
C Brighten fire
PNT 15 73 2 4 5
PNT 15 74 2 2 6
C Expand firelight on walls
PNT 4 58 6 10 2
PNT 22 56 6 12 2
C
REC 2
C
C --- FRAME 03.006: FIRE DIMS ---
PNT 15 73 2 4 4
PNT 15 74 2 2 5
PNT 4 58 6 10 1
PNT 22 56 6 12 1
C
REC 2
C
C --- FRAME 03.007: FIRE BRIGHTENS AGAIN ---
PNT 15 73 2 4 5
PNT 15 74 2 2 7
PNT 4 56 8 12 3
PNT 20 54 8 14 3
C
REC 2
C
C --- FRAME 03.008: FIRE NORMALIZES ---
PNT 15 73 2 4 4
PNT 15 74 2 2 5
PNT 4 56 8 12 2
PNT 20 54 8 14 2
C
REC 3
C
C --- FRAME 03.009: CALYPSO'S RADIANCE PULSES ---
C Glow expands
PNT 28 36 22 40 2
PNT 30 38 18 36 3
C
REC 3
C
C --- FRAME 03.010: RADIANCE CONTRACTS ---
PNT 28 36 22 40 1
PNT 30 38 18 36 2
C
REC 3
C
C --- FRAME 03.011: CALYPSO ARM GESTURE — offering hand extends ---
C Left arm extends further
LIN 28 48 26 46 3
LIN 26 46 22 44 5
PNT 20 42 4 3 4
C
REC 3
C
C --- FRAME 03.012: ARM RETURNS ---
PNT 20 42 6 4 1
LIN 26 46 22 44 1
LIN 28 48 26 46 5
PNT 24 44 4 3 4
C
REC 3
C
C --- FRAME 03.013: ODYSSEUS TURNS HEAD TOWARD SEA ---
C Erase old face direction
PNT 86 45 1 1 5
PNT 89 45 1 1 5
C Eyes look right — toward the sea
PNT 88 45 1 1 6
PNT 90 45 1 1 6
C
REC 4
C
C --- FRAME 03.014: ODYSSEUS HEAD RETURNS ---
PNT 88 45 1 1 5
PNT 90 45 1 1 5
PNT 86 45 1 1 6
PNT 89 45 1 1 6
C
REC 3
C
C --- FRAME 03.015: STAR TWINKLE --- stars brighten and dim ---
C Brighten select stars
PNT 40 5 2 2 4
PNT 82 8 2 2 4
PNT 12 4 1 1 4
PNT 68 5 1 1 4
C
REC 2
C
C --- FRAME 03.016: STARS DIM BACK ---
PNT 40 5 2 2 3
PNT 82 8 2 2 3
PNT 12 4 1 1 3
PNT 68 5 1 1 3
C
REC 2
C
C --- FRAME 03.017: DIFFERENT STARS TWINKLE ---
PNT 60 3 2 2 4
PNT 28 8 1 1 4
PNT 104 4 1 1 4
PNT 50 16 1 1 4
C
REC 2
C
C --- FRAME 03.018: STARS DIM ---
PNT 60 3 2 2 3
PNT 28 8 1 1 2
PNT 104 4 1 1 2
PNT 50 16 1 1 3
C
REC 2
C
C --- FRAME 03.019: CALYPSO HAIR BLOWS IN SEA WIND ---
C Erase old hair left
LIN 35 34 30 32 1
LIN 30 32 26 34 1
LIN 26 34 24 38 1
C Redraw hair blown further left
LIN 35 34 28 30 4
LIN 28 30 22 32 3
LIN 22 32 18 36 4
LIN 35 36 29 34 3
LIN 29 34 24 38 4
C
REC 3
C
C --- FRAME 03.020: HAIR SETTLES ---
PNT 18 30 14 10 1
C Restore normal hair
LIN 35 34 30 32 4
LIN 30 32 26 34 3
LIN 26 34 24 38 4
LIN 35 36 31 38 3
LIN 31 38 28 42 4
C
REC 3
C
C --- FRAME 03.021: ROBE FLUTTER ---
C Robe hem shifts in wind
PNT 30 76 16 4 1
PNT 28 76 18 4 3
LIN 28 78 46 80 3
C
REC 2
C
C --- FRAME 03.022: ROBE SETTLES ---
PNT 28 76 18 4 1
PNT 30 76 16 4 3
LIN 34 72 30 78 3
LIN 42 72 46 78 3
C
REC 2
C
C --- FRAME 03.023: WAVE CYCLE 2 ---
LIN 0 30 20 28 2
LIN 20 28 40 30 2
LIN 40 30 60 28 2
LIN 60 28 80 30 2
LIN 80 30 100 28 2
LIN 100 28 127 30 2
LIN 4 30 24 28 3
LIN 24 28 44 30 3
LIN 44 30 64 28 3
LIN 64 28 84 30 3
LIN 84 30 104 28 3
LIN 104 28 127 30 3
C
REC 2
C
C --- FRAME 03.024: WAVES RETURN ---
LIN 4 30 24 28 2
LIN 24 28 44 30 2
LIN 44 30 64 28 2
LIN 64 28 84 30 2
LIN 84 30 104 28 2
LIN 104 28 127 30 2
LIN 0 30 20 28 3
LIN 20 28 40 30 3
LIN 40 30 60 28 3
LIN 60 28 80 30 3
LIN 80 30 100 28 3
LIN 100 28 127 30 3
C
REC 2
C
C --- FRAME 03.025: ODYSSEUS HAND CLENCHES ---
C Fist tightens on ground
PNT 97 65 4 3 6
PNT 98 66 2 2 7
C
REC 3
C
C --- FRAME 03.026: HAND RELAXES ---
PNT 97 65 4 3 5
PNT 98 66 2 2 5
C
REC 3
C
C --- FRAME 03.027: CALYPSO RADIANCE PULSE ---
PNT 28 36 22 40 2
PNT 30 38 18 36 3
PNT 32 40 14 32 2
C
REC 3
C
C --- FRAME 03.028: RADIANCE FADES ---
PNT 28 36 22 40 1
PNT 30 38 18 36 2
PNT 32 40 14 32 1
C
REC 3
C
C --- FRAME 03.029: HOLD — mythic tableau ---
REC 10
C
C --- END OF BATCH 1: SCENES 01-03 ---
C
C ============================================================
C  SCENE 04: INT ANTHROPIC BOARDROOM — DAY
C  Executives discuss AI risk, labor disruption, geopolitics.
C  Long table, seated figures, wall screens with graphs.
C  Tension conveyed through rigid geometry.
C  Graphs climb relentlessly upward on displays.
C ============================================================
C
C --- FRAME 04.001: BASE ROOM CONSTRUCTION ---
CLR 0
C Ceiling — flat gray
PNT 0 0 128 12 2
C Ceiling lighting panel — fluorescent strip
PNT 30 2 68 3 3
PNT 34 3 60 1 4
C Wall — left portion
PNT 0 12 128 36 2
C Wall panels — subtle vertical divisions
LIN 32 12 32 48 3
LIN 64 12 64 48 3
LIN 96 12 96 48 3
C
C Wall screen — LEFT — large display showing rising graph
PNT 6 14 22 28 1
PNT 7 15 20 26 0
C Graph axes
LIN 10 40 10 18 3
LIN 10 40 24 40 3
C Graph line — climbing exponentially
LIN 10 38 13 36 4
LIN 13 36 15 34 4
LIN 15 34 17 30 4
LIN 17 30 19 24 5
LIN 19 24 21 18 5
LIN 21 18 24 14 6
C Data points on graph
PNT 13 36 1 1 5
PNT 17 30 1 1 5
PNT 21 18 1 1 6
C Graph label area
PNT 10 41 14 2 2
C
C Wall screen — CENTER — safety metrics dashboard
PNT 38 14 22 28 1
PNT 39 15 20 26 0
C Dashboard grid
LIN 42 18 56 18 2
LIN 42 26 56 26 2
LIN 42 34 56 34 2
LIN 49 15 49 40 2
C Dashboard values — bar indicators
PNT 43 20 5 5 3
PNT 50 20 5 5 4
PNT 43 28 5 5 5
PNT 50 28 5 5 2
PNT 43 36 5 3 4
PNT 50 36 5 3 6
C
C Wall screen — RIGHT — world map or network diagram
PNT 70 14 22 28 1
PNT 71 15 20 26 0
C Network nodes
PNT 76 20 3 3 4
PNT 84 18 3 3 4
PNT 80 28 3 3 4
PNT 74 32 3 3 4
PNT 86 34 3 3 4
PNT 78 38 3 3 4
C Network edges
LIN 78 22 84 18 3
LIN 78 22 80 28 3
LIN 84 18 86 34 3
LIN 80 28 74 32 3
LIN 80 28 86 34 3
LIN 74 32 78 38 3
LIN 86 34 78 38 3
C
C Floor — dark
PNT 0 48 128 48 3
PNT 0 50 128 2 2
C Floor reflection
PNT 0 80 128 16 4
C
C Conference table — long rectangle centered
PNT 20 56 88 14 5
PNT 22 58 84 10 6
C Table edge highlight
LIN 20 56 108 56 7
LIN 20 70 108 70 6
C Table legs
LIN 24 70 24 78 5
LIN 104 70 104 78 5
C
C --- SEATED FIGURES — 6 executives around table ---
C Figure 1 — left end — head and shoulders
PNT 14 48 8 8 4
PNT 15 49 6 6 5
PNT 16 44 4 6 4
PNT 17 45 2 4 5
PNT 17 43 2 2 6
C
C Figure 2 — left side
PNT 30 48 8 8 4
PNT 31 49 6 6 5
PNT 32 44 4 6 4
PNT 33 45 2 4 5
PNT 33 43 2 2 6
C
C Figure 3 — center-left
PNT 48 48 8 8 4
PNT 49 49 6 6 5
PNT 50 44 4 6 4
PNT 51 45 2 4 5
PNT 51 43 2 2 6
C
C Figure 4 — center-right
PNT 68 48 8 8 4
PNT 69 49 6 6 5
PNT 70 44 4 6 4
PNT 71 45 2 4 5
PNT 71 43 2 2 6
C
C Figure 5 — right side
PNT 86 48 8 8 4
PNT 87 49 6 6 5
PNT 88 44 4 6 4
PNT 89 45 2 4 5
PNT 89 43 2 2 6
C
C Figure 6 — right end
PNT 104 48 8 8 4
PNT 105 49 6 6 5
PNT 106 44 4 6 4
PNT 107 45 2 4 5
PNT 107 43 2 2 6
C
C Documents/tablets on table
PNT 26 60 6 4 4
PNT 44 60 6 4 4
PNT 62 60 6 4 4
PNT 80 60 6 4 4
PNT 98 60 6 4 4
C
C Water glasses
PNT 36 58 2 3 3
PNT 56 58 2 3 3
PNT 76 58 2 3 3
PNT 96 58 2 3 3
C
REC 8
C
C --- FRAME 04.002: FIGURE 2 GESTURE — arm raise ---
C Arm extends from figure 2 toward screen
LIN 30 50 26 44 5
LIN 26 44 24 42 5
PNT 22 40 3 3 4
C
REC 3
C
C --- FRAME 04.003: ARM LOWERS ---
PNT 22 40 6 6 2
LIN 30 50 26 44 2
LIN 26 44 24 42 2
C Restore wall behind
PNT 24 40 6 6 2
C
REC 3
C
C --- FRAME 04.004: GRAPH ANIMATION — line climbs higher ---
C Extend the graph line upward
LIN 24 14 26 12 6
PNT 24 12 2 2 7
C
REC 3
C
C --- FRAME 04.005: GRAPH DATA POINT PULSES ---
PNT 24 12 2 2 6
C
REC 2
C
PNT 24 12 2 2 7
C
REC 2
C
PNT 24 12 2 2 6
C
REC 2
C
C --- FRAME 04.006: FIGURE 4 HEAD TURN — looks at figure 3 ---
PNT 71 45 2 4 4
PNT 70 45 2 4 5
C
REC 3
C
C --- FRAME 04.007: FIGURE 4 HEAD RETURNS ---
PNT 70 45 2 4 4
PNT 71 45 2 4 5
C
REC 3
C
C --- FRAME 04.008: DASHBOARD METRIC CHANGES ---
C Center screen bar changes — one rises, one falls
PNT 43 28 5 5 6
PNT 50 28 5 5 3
C
REC 3
C
C --- FRAME 04.009: DASHBOARD NORMALIZES ---
PNT 43 28 5 5 5
PNT 50 28 5 5 4
C
REC 3
C
C --- FRAME 04.010: FIGURE 1 LEANS FORWARD ---
PNT 14 48 8 8 2
PNT 13 49 8 8 4
PNT 14 50 6 6 5
C Head shifts forward
PNT 15 44 4 5 4
PNT 16 44 2 4 5
C
REC 3
C
C --- FRAME 04.011: FIGURE 1 LEANS BACK ---
PNT 13 49 8 8 2
PNT 14 48 8 8 4
PNT 15 49 6 6 5
PNT 16 44 4 6 4
PNT 17 45 2 4 5
C
REC 3
C
C --- FRAME 04.012: FIGURE 5 PICKS UP DOCUMENT ---
C Document lifts from table
PNT 98 60 6 4 5
PNT 90 52 6 4 4
C
REC 3
C
C --- FRAME 04.013: DOCUMENT RETURNS TO TABLE ---
PNT 90 52 6 4 2
PNT 98 60 6 4 4
C
REC 3
C
C --- FRAME 04.014: NETWORK DIAGRAM ANIMATION ---
C Node pulses on right screen
PNT 80 28 3 3 5
C Edge brightens
LIN 78 22 80 28 4
LIN 80 28 86 34 4
C
REC 2
C
C --- FRAME 04.015: NETWORK RETURNS ---
PNT 80 28 3 3 4
LIN 78 22 80 28 3
LIN 80 28 86 34 3
C
REC 2
C
C --- FRAME 04.016: CEILING LIGHT FLICKER ---
PNT 34 3 60 1 5
C
REC 1
C
PNT 34 3 60 1 4
C
REC 2
C
C --- FRAME 04.017: FIGURE 6 HEAD NOD ---
C Head dips down
PNT 107 43 2 2 5
PNT 107 44 2 2 6
C
REC 2
C
C --- FRAME 04.018: HEAD RISES ---
PNT 107 44 2 2 5
PNT 107 43 2 2 6
C
REC 2
C
C --- FRAME 04.019: WATER GLASS CATCH LIGHT ---
PNT 56 58 2 3 4
C
REC 2
C
PNT 56 58 2 3 3
C
REC 2
C
C --- FRAME 04.020: GRAPH CONTINUES RISING ---
LIN 26 12 28 10 6
PNT 26 10 2 2 7
C
REC 3
C
C --- FRAME 04.021: ALL FIGURES SLIGHT SHIFT — tension ---
C Everyone shifts slightly — subtle discomfort
PNT 33 43 2 2 5
PNT 33 44 2 2 6
PNT 51 43 2 2 5
PNT 51 44 2 2 6
PNT 89 43 2 2 5
PNT 89 44 2 2 6
C
REC 2
C
C --- FRAME 04.022: FIGURES RETURN ---
PNT 33 44 2 2 5
PNT 33 43 2 2 6
PNT 51 44 2 2 5
PNT 51 43 2 2 6
PNT 89 44 2 2 5
PNT 89 43 2 2 6
C
REC 3
C
C --- FRAME 04.023: HOLD ON BOARDROOM ---
REC 8
C
C
C ============================================================
C  SCENE 05: INT ANTHROPIC OFFICE — DAY
C  Safety reports. Alignment diagrams. Evaluation dashboards.
C  A quieter space — one person at desk with multiple screens.
C  Documents marked SAFETY, GOVERNANCE, INTERPRETABILITY.
C  The bureaucracy of responsible AI rendered in BEFLIX.
C ============================================================
C
C --- FRAME 05.001: BASE OFFICE ---
CLR 0
C Walls — medium tone
PNT 0 0 128 20 2
C Wall detail — horizontal molding
LIN 0 20 127 20 3
C Window — left wall — daylight coming in
PNT 4 4 20 14 1
PNT 5 5 18 12 0
C Window frame
LIN 4 4 24 4 3
LIN 4 18 24 18 3
LIN 4 4 4 18 3
LIN 24 4 24 18 3
LIN 14 4 14 18 3
LIN 4 11 24 11 3
C Window light cast on floor
PNT 4 58 24 12 2
PNT 6 60 20 8 1
C
C Floor
PNT 0 52 128 44 3
PNT 0 54 128 2 4
PNT 0 62 128 2 2
PNT 0 70 128 2 4
PNT 0 78 128 2 2
C
C Desk — L-shaped
PNT 40 42 50 10 5
PNT 42 44 46 6 6
C Desk edge
LIN 40 42 90 42 7
LIN 40 52 90 52 6
C Desk legs
LIN 44 52 44 60 5
LIN 86 52 86 60 5
C Side desk extension
PNT 88 42 20 10 5
PNT 90 44 16 6 6
LIN 88 42 108 42 7
C
C --- THREE MONITORS on desk ---
C Monitor 1 — left — safety report
PNT 44 28 16 14 1
PNT 45 29 14 12 0
C Screen content — document lines
LIN 47 31 57 31 2
LIN 47 33 57 33 2
LIN 47 35 55 35 2
LIN 47 37 53 37 2
LIN 47 39 57 39 2
C Monitor stand
PNT 50 42 4 2 4
C
C Monitor 2 — center — alignment diagram
PNT 62 26 18 16 1
PNT 63 27 16 14 0
C Diagram — circular alignment chart
PNT 68 30 8 8 2
PNT 70 32 4 4 3
PNT 71 33 2 2 4
C Spokes
LIN 72 30 72 26 2
LIN 76 34 80 34 2
LIN 72 38 72 42 2
LIN 68 34 64 34 2
C Monitor stand
PNT 69 42 4 2 4
C
C Monitor 3 — right — evaluation dashboard
PNT 82 28 14 14 1
PNT 83 29 12 12 0
C Dashboard bars
PNT 85 32 2 8 4
PNT 88 34 2 6 3
PNT 91 30 2 10 5
C Score indicator
PNT 85 40 8 1 6
C Monitor stand
PNT 87 42 4 2 4
C
C --- SEATED FIGURE — researcher at desk ---
PNT 56 38 10 14 4
PNT 58 40 6 10 5
C Head
PNT 58 30 8 8 4
PNT 59 31 6 6 5
C Hair
PNT 59 30 6 2 6
C Eyes — focused on screens
PNT 60 33 1 1 7
PNT 63 33 1 1 7
C Glasses frames
LIN 59 32 62 32 6
LIN 63 32 66 32 6
C Arms on desk
LIN 56 44 50 46 5
LIN 66 44 72 46 5
C Hands on keyboard
PNT 48 46 6 2 4
PNT 70 46 6 2 4
C
C Keyboard on desk
PNT 48 48 28 2 4
PNT 50 49 24 1 5
C
C Chair
PNT 54 52 16 8 4
PNT 56 54 12 4 5
C Chair back
PNT 54 38 2 14 4
PNT 68 38 2 14 4
LIN 54 38 68 38 4
C Chair wheels
PNT 54 60 2 2 5
PNT 66 60 2 2 5
PNT 60 62 2 2 5
C
C --- DOCUMENT STACKS on side desk ---
PNT 92 38 4 4 4
PNT 93 37 3 3 5
PNT 96 38 4 4 4
PNT 97 37 3 3 5
PNT 100 36 4 6 4
PNT 101 35 3 5 5
C
C Coffee cup
PNT 104 40 3 3 4
PNT 105 40 1 2 5
C
C Bookshelf on right wall
PNT 108 4 18 48 4
C Shelf dividers
LIN 108 16 126 16 5
LIN 108 28 126 28 5
LIN 108 40 126 40 5
C Books — colored spines
PNT 110 5 2 10 5
PNT 113 5 2 10 6
PNT 116 5 2 10 3
PNT 119 5 2 10 5
PNT 122 5 2 10 4
PNT 110 17 2 10 4
PNT 113 17 2 10 5
PNT 116 17 2 10 6
PNT 119 17 2 10 3
PNT 122 17 2 10 5
PNT 110 29 2 10 6
PNT 113 29 2 10 4
PNT 116 29 2 10 5
PNT 119 29 2 10 3
PNT 122 29 2 10 6
C
REC 8
C
C --- FRAME 05.002: TYPING ANIMATION — hands move ---
PNT 48 46 6 2 5
PNT 70 46 6 2 5
C
REC 1
C
PNT 48 46 6 2 4
PNT 70 46 6 2 4
C
REC 1
C
PNT 48 46 6 2 5
PNT 70 46 6 2 5
C
REC 1
C
PNT 48 46 6 2 4
PNT 70 46 6 2 4
C
REC 1
C
C --- FRAME 05.003: SCREEN 1 UPDATE — new line appears ---
LIN 47 41 56 41 2
C
REC 3
C
C --- FRAME 05.004: SCREEN 2 — diagram rotates ---
C Clear old diagram spokes
LIN 72 30 72 26 0
LIN 76 34 80 34 0
LIN 72 38 72 42 0
LIN 68 34 64 34 0
C Draw rotated spokes
LIN 70 30 74 26 2
LIN 76 32 80 36 2
LIN 74 38 70 42 2
LIN 68 36 64 32 2
C
REC 3
C
C --- FRAME 05.005: DIAGRAM ROTATES BACK ---
LIN 70 30 74 26 0
LIN 76 32 80 36 0
LIN 74 38 70 42 0
LIN 68 36 64 32 0
LIN 72 30 72 26 2
LIN 76 34 80 34 2
LIN 72 38 72 42 2
LIN 68 34 64 34 2
C
REC 3
C
C --- FRAME 05.006: SCREEN 3 — bars animate ---
PNT 85 32 2 8 5
PNT 88 34 2 6 4
PNT 91 30 2 10 6
C
REC 2
C
PNT 85 32 2 8 4
PNT 88 34 2 6 3
PNT 91 30 2 10 5
C
REC 2
C
C --- FRAME 05.007: RESEARCHER ADJUSTS GLASSES ---
LIN 59 32 62 32 5
LIN 63 32 66 32 5
C Push up
LIN 59 31 62 31 6
LIN 63 31 66 31 6
C
REC 2
C
LIN 59 31 62 31 5
LIN 63 31 66 31 5
LIN 59 32 62 32 6
LIN 63 32 66 32 6
C
REC 2
C
C --- FRAME 05.008: RESEARCHER LEANS BACK ---
PNT 56 38 10 14 3
PNT 57 39 10 14 4
PNT 59 41 6 10 5
C Head shifts back
PNT 58 30 8 8 3
PNT 60 31 8 8 4
PNT 61 32 6 6 5
C
REC 4
C
C --- FRAME 05.009: RESEARCHER LEANS FORWARD ---
PNT 57 39 10 14 3
PNT 56 38 10 14 4
PNT 58 40 6 10 5
PNT 60 31 8 8 3
PNT 58 30 8 8 4
PNT 59 31 6 6 5
C
REC 3
C
C --- FRAME 05.010: WINDOW LIGHT SHIFTS ---
PNT 4 58 24 12 3
PNT 6 60 20 8 2
C
REC 3
C
PNT 4 58 24 12 2
PNT 6 60 20 8 1
C
REC 3
C
C --- FRAME 05.011: MOUSE CLICK — cursor moves on screen ---
PNT 55 37 1 1 7
C
REC 2
C
PNT 55 37 1 1 0
C
REC 2
C
C --- FRAME 05.012: HOLD ON OFFICE ---
REC 8
C
C
C ============================================================
C  SCENE 06: INT COURTROOM — DAY
C  COPYRIGHT CLAIMS — STACKS OF BOOKS
C  Attorneys argue before a judge's bench.
C  Evidence tables with books, devices, printouts.
C  The tension between culture and computation.
C ============================================================
C
C --- FRAME 06.001: BASE COURTROOM ---
CLR 0
C Ceiling / upper wall — formal institutional tone
PNT 0 0 128 18 2
C Crown molding line
LIN 0 18 127 18 3
C Wood paneling — warm tones
PNT 0 18 128 10 3
LIN 0 28 127 28 4
C Lower wall
PNT 0 28 128 50 2
C
C Floor — polished
PNT 0 78 128 18 1
LIN 0 78 127 78 2
C Floor reflection band
PNT 0 82 128 4 2
C
C --- JUDGE'S BENCH — elevated platform center ---
C Platform
PNT 36 26 56 4 4
LIN 36 26 92 26 5
C Bench — tall wooden front
PNT 40 22 48 8 4
PNT 42 24 44 4 5
C Bench top edge
LIN 40 22 88 22 6
C Gavel
PNT 62 20 4 2 5
PNT 63 20 2 1 6
LIN 64 20 66 18 5
C
C Judge figure — behind bench
PNT 58 10 12 12 4
PNT 60 12 8 8 5
C Head
PNT 61 4 6 8 4
PNT 62 5 4 6 5
C Robe collar
LIN 58 10 70 10 6
C Face
PNT 63 7 1 1 7
PNT 66 7 1 1 7
LIN 63 10 66 10 5
C
C --- WITNESS STAND — left side ---
PNT 8 30 14 14 4
PNT 10 32 10 10 5
LIN 8 30 22 30 5
C Witness figure
PNT 12 24 8 8 4
PNT 13 25 6 6 5
PNT 14 18 4 8 4
PNT 15 19 2 6 5
PNT 15 17 2 2 6
C Witness hands on rail
PNT 10 30 4 2 5
PNT 18 30 4 2 5
C
C --- DEFENSE TABLE — left of center ---
C Table
PNT 10 50 22 8 4
LIN 10 50 32 50 5
LIN 10 58 32 58 5
C Table legs
LIN 14 58 14 68 4
LIN 28 58 28 68 4
C
C Defense attorney standing
PNT 16 36 10 14 5
PNT 18 38 6 10 6
C Head
PNT 18 28 6 8 4
PNT 19 29 4 6 5
PNT 19 27 4 2 6
C Arm extended — gesturing
LIN 16 40 10 34 5
PNT 8 32 3 3 4
C Eyes
PNT 20 31 1 1 7
PNT 22 31 1 1 7
C
C Documents on defense table
PNT 12 52 4 4 3
PNT 17 52 4 4 3
PNT 22 52 6 4 3
C
C --- PROSECUTION TABLE — right of center ---
PNT 96 50 22 8 4
LIN 96 50 118 50 5
LIN 96 58 118 58 5
C Table legs
LIN 100 58 100 68 4
LIN 114 58 114 68 4
C
C Prosecutor seated
PNT 100 42 10 10 5
PNT 102 44 6 6 6
C Head
PNT 102 34 6 8 4
PNT 103 35 4 6 5
PNT 103 33 4 2 6
C Eyes
PNT 104 37 1 1 7
PNT 106 37 1 1 7
C Arm on table
LIN 100 48 96 52 5
C
C Documents on prosecution table
PNT 98 52 4 4 3
PNT 103 52 4 4 3
PNT 108 52 4 4 3
PNT 113 52 4 4 3
C
C --- EVIDENCE TABLE — center foreground ---
PNT 46 54 36 10 4
LIN 46 54 82 54 5
LIN 46 64 82 64 5
C
C Stacks of books on evidence table
C Stack 1
PNT 48 50 4 4 5
PNT 49 49 3 3 6
PNT 48 48 4 2 5
C Stack 2
PNT 54 50 4 4 5
PNT 55 49 3 3 6
PNT 54 48 4 2 5
PNT 55 47 3 2 6
C Stack 3
PNT 60 50 6 4 5
PNT 61 49 5 3 6
PNT 60 48 6 2 5
PNT 61 47 5 2 6
PNT 60 46 6 2 5
C Stack 4
PNT 68 50 4 4 5
PNT 69 49 3 3 6
C
C Laptop on evidence table
PNT 74 52 6 4 4
PNT 74 48 6 4 1
PNT 75 49 4 3 0
C
C --- GALLERY — back wall spectators ---
PNT 0 68 128 10 3
C Spectator heads in rows
PNT 6 68 4 4 4
PNT 14 68 4 4 4
PNT 22 68 4 4 4
PNT 30 68 4 4 4
PNT 38 68 4 4 4
PNT 90 68 4 4 4
PNT 98 68 4 4 4
PNT 106 68 4 4 4
PNT 114 68 4 4 4
PNT 122 68 4 4 4
C
C --- COURT RAILING --- divides gallery from floor
LIN 0 68 127 68 5
C
C --- FLAG or SEAL behind judge ---
PNT 80 4 10 14 3
PNT 82 6 6 10 4
PNT 83 7 4 8 5
C
REC 8
C
C --- FRAME 06.002: DEFENSE ATTORNEY GESTURES ---
C Arm swings wide
LIN 16 40 10 34 2
PNT 8 32 3 3 2
LIN 16 40 6 30 5
PNT 4 28 3 3 4
C
REC 3
C
C --- FRAME 06.003: ARM RETURNS ---
PNT 4 28 5 6 2
LIN 16 40 6 30 2
LIN 16 40 10 34 5
PNT 8 32 3 3 4
C
REC 3
C
C --- FRAME 06.004: JUDGE TAPS GAVEL ---
C Gavel lifts
PNT 62 20 4 2 4
PNT 62 18 4 2 5
PNT 63 18 2 1 6
LIN 64 18 66 16 5
C
REC 2
C
C --- FRAME 06.005: GAVEL DOWN ---
PNT 62 18 4 2 4
PNT 62 20 4 2 5
PNT 63 20 2 1 6
LIN 64 20 66 18 5
C
REC 2
C
C --- FRAME 06.006: WITNESS HEAD TURN ---
PNT 15 19 2 6 4
PNT 14 19 2 6 5
C
REC 3
C
PNT 14 19 2 6 4
PNT 15 19 2 6 5
C
REC 3
C
C --- FRAME 06.007: PROSECUTOR RISES ---
C Standing position
PNT 100 42 10 10 2
PNT 100 32 10 18 5
PNT 102 34 6 14 6
PNT 102 24 6 8 4
PNT 103 25 4 6 5
PNT 103 23 4 2 6
PNT 104 27 1 1 7
PNT 106 27 1 1 7
C Arm extends toward evidence
LIN 100 38 92 42 5
PNT 90 41 3 3 4
C
REC 4
C
C --- FRAME 06.008: PROSECUTOR SITS ---
PNT 90 41 3 3 2
LIN 100 38 92 42 2
PNT 100 32 10 18 2
PNT 100 24 10 10 2
C Restore seated position
PNT 100 42 10 10 5
PNT 102 44 6 6 6
PNT 102 34 6 8 4
PNT 103 35 4 6 5
PNT 103 33 4 2 6
PNT 104 37 1 1 7
PNT 106 37 1 1 7
C
REC 4
C
C --- FRAME 06.009: SPECTATOR SHIFT ---
PNT 22 68 4 4 5
PNT 30 68 4 4 5
C
REC 2
C
PNT 22 68 4 4 4
PNT 30 68 4 4 4
C
REC 2
C
C --- FRAME 06.010: BOOK STACK HIGHLIGHT ---
C Light catches top book of tallest stack
PNT 60 46 6 2 7
C
REC 3
C
PNT 60 46 6 2 5
C
REC 3
C
C --- FRAME 06.011: LAPTOP SCREEN FLICKER ---
PNT 75 49 4 3 1
C
REC 1
C
PNT 75 49 4 3 0
C
REC 2
C
C --- FRAME 06.012: JUDGE HEAD NOD ---
PNT 62 5 4 6 4
PNT 62 6 4 6 5
C
REC 2
C
PNT 62 6 4 6 4
PNT 62 5 4 6 5
C
REC 2
C
C --- FRAME 06.013: DEFENSE ATTORNEY SECOND GESTURE ---
LIN 16 40 10 34 2
LIN 16 40 12 28 5
LIN 12 28 14 24 5
PNT 12 22 4 3 4
C
REC 3
C
C --- FRAME 06.014: ARM RETURNS ---
PNT 12 22 4 6 2
LIN 16 40 12 28 2
LIN 16 40 10 34 5
PNT 8 32 3 3 4
C
REC 3
C
C --- FRAME 06.015: HOLD ON COURTROOM ---
REC 10
C
C --- END OF BATCH 2: SCENES 04-06 ---
C
C ============================================================
C  SCENE 07: EXT 19TH CENTURY FARM ROAD — DAY
C  HORSE AS TECHNOLOGY — the horse pulls a wagon.
C  Dirt road, wooden fences, agricultural landscape.
C  Montage of horse-as-infrastructure roles.
C ============================================================
C
C --- FRAME 07.001: BASE RURAL LANDSCAPE ---
CLR 0
C Sky — bright clear day
PNT 0 0 128 20 1
C Clouds — cumulus
PNT 20 4 16 8 2
PNT 23 5 10 6 1
PNT 80 6 18 8 2
PNT 84 7 12 6 1
C
C Distant treeline
PNT 0 18 128 6 3
PNT 8 18 14 5 4
PNT 30 17 18 6 4
PNT 56 18 20 5 4
PNT 84 17 16 6 4
PNT 108 18 18 5 4
C
C Rolling fields — left and right of road
PNT 0 24 128 24 3
PNT 0 26 50 2 2
PNT 78 26 50 2 2
PNT 0 34 50 2 4
PNT 78 34 50 2 4
C Crop rows — left field
LIN 2 28 48 28 2
LIN 2 30 48 30 2
LIN 2 32 48 32 2
LIN 2 36 48 36 2
LIN 2 38 48 38 2
C Crop rows — right field
LIN 80 28 126 28 2
LIN 80 30 126 30 2
LIN 80 32 126 32 2
LIN 80 36 126 36 2
LIN 80 38 126 38 2
C
C Dirt road — center, receding to horizon
C Road narrows toward vanishing point at top
PNT 50 20 28 4 4
PNT 48 24 32 4 4
PNT 46 28 36 4 4
PNT 44 32 40 4 4
PNT 42 36 44 4 4
PNT 40 40 48 4 4
PNT 38 44 52 4 4
PNT 36 48 56 8 4
PNT 32 56 64 8 4
PNT 28 64 72 8 4
PNT 24 72 80 8 4
PNT 20 80 88 16 4
C Road ruts — wheel tracks
LIN 56 20 40 80 5
LIN 72 20 88 80 5
C Road center grass strip
LIN 64 20 64 80 3
C
C Wooden fence — right side of road
PNT 80 44 2 14 5
PNT 88 42 2 12 5
PNT 96 40 2 10 5
PNT 104 38 2 8 5
PNT 112 36 2 6 5
C Fence rails
LIN 80 48 112 38 4
LIN 80 52 112 42 4
C
C --- HORSE pulling wagon — center of road ---
C Horse body — medium size in mid-ground
PNT 50 48 14 8 5
PNT 52 49 10 6 6
C Neck
PNT 48 42 4 8 5
PNT 49 43 2 6 6
C Head
PNT 46 38 4 5 5
PNT 47 39 2 3 6
C Eye
PNT 47 40 1 1 7
C Ear
PNT 46 37 2 2 6
PNT 48 37 2 2 6
C Front legs — walking position
LIN 52 56 50 66 5
LIN 54 56 56 66 5
C Back legs
LIN 60 56 58 66 5
LIN 62 56 64 66 5
C Hooves
PNT 49 66 2 2 6
PNT 55 66 2 2 6
PNT 57 66 2 2 6
PNT 63 66 2 2 6
C Tail
LIN 64 49 68 46 5
LIN 68 46 70 48 4
C
C Harness — connecting horse to wagon
LIN 64 52 72 52 5
LIN 64 54 72 54 5
LIN 52 50 52 56 4
C Collar
PNT 48 44 4 4 4
C
C --- WAGON behind horse ---
PNT 72 44 24 14 5
PNT 74 46 20 10 6
C Wagon sides
LIN 72 44 96 44 7
LIN 72 58 96 58 6
LIN 72 44 72 58 6
LIN 96 44 96 58 6
C Wagon bed
PNT 74 48 20 8 5
C Cargo — hay bales
PNT 76 44 6 4 3
PNT 84 44 6 4 3
PNT 80 42 8 4 2
C
C Wheels — left
PNT 74 56 6 8 5
PNT 76 58 2 4 6
LIN 77 56 77 64 5
LIN 74 60 80 60 5
C Wheel — right
PNT 90 56 6 8 5
PNT 92 58 2 4 6
LIN 93 56 93 64 5
LIN 90 60 96 60 5
C
C --- DRIVER on wagon seat ---
PNT 72 36 8 8 4
PNT 73 37 6 6 5
C Head
PNT 74 30 4 6 4
PNT 75 31 2 4 5
C Hat
PNT 73 28 6 3 5
PNT 74 29 4 1 6
C Arms holding reins
LIN 72 40 64 44 5
LIN 78 40 58 44 5
C Reins
LIN 56 44 48 42 4
LIN 58 44 48 42 4
C
C --- FARMHOUSE in distance ---
PNT 10 20 8 6 5
PNT 11 21 6 4 6
PNT 10 18 8 3 4
C Chimney
PNT 16 16 2 4 5
C Smoke
PNT 17 14 1 3 2
PNT 16 12 2 2 1
PNT 15 10 3 2 1
C
REC 8
C
C --- FRAME 07.002: HORSE WALK CYCLE — left legs forward ---
C Erase old leg positions
LIN 52 56 50 66 4
LIN 54 56 56 66 4
LIN 60 56 58 66 4
LIN 62 56 64 66 4
C Left front forward, right back
LIN 52 56 48 66 5
LIN 54 56 58 66 5
C Left back forward, right back
LIN 60 56 56 66 5
LIN 62 56 66 66 5
C
REC 2
C
C --- FRAME 07.003: WALK CYCLE — legs swap ---
LIN 52 56 48 66 4
LIN 54 56 58 66 4
LIN 60 56 56 66 4
LIN 62 56 66 66 4
C Right front forward, left back
LIN 52 56 54 66 5
LIN 54 56 52 66 5
LIN 60 56 62 66 5
LIN 62 56 60 66 5
C
REC 2
C
C --- FRAME 07.004: WALK CYCLE — crossing ---
LIN 52 56 54 66 4
LIN 54 56 52 66 4
LIN 60 56 62 66 4
LIN 62 56 60 66 4
C Return to wide stance
LIN 52 56 50 66 5
LIN 54 56 56 66 5
LIN 60 56 58 66 5
LIN 62 56 64 66 5
C
REC 2
C
C --- FRAME 07.005: HEAD BOB — walking rhythm ---
PNT 46 38 4 5 4
PNT 46 39 4 5 5
PNT 47 40 2 3 6
PNT 47 41 1 1 7
C
REC 2
C
C --- FRAME 07.006: HEAD UP ---
PNT 46 39 4 5 4
PNT 46 38 4 5 5
PNT 47 39 2 3 6
PNT 47 40 1 1 7
C
REC 2
C
C --- FRAME 07.007: WHEEL ROTATION ---
C Left wheel spoke rotates
LIN 77 56 77 64 4
LIN 74 60 80 60 4
C New spoke angle
LIN 75 57 79 63 5
LIN 75 63 79 57 5
C Right wheel
LIN 93 56 93 64 4
LIN 90 60 96 60 4
LIN 91 57 95 63 5
LIN 91 63 95 57 5
C
REC 2
C
C --- FRAME 07.008: WHEEL ROTATION CONTINUES ---
LIN 75 57 79 63 4
LIN 75 63 79 57 4
LIN 91 57 95 63 4
LIN 91 63 95 57 4
C Original spoke position
LIN 77 56 77 64 5
LIN 74 60 80 60 5
LIN 93 56 93 64 5
LIN 90 60 96 60 5
C
REC 2
C
C --- FRAME 07.009: DUST CLOUD behind wagon ---
PNT 98 60 10 6 2
PNT 100 62 6 4 1
C
REC 3
C
C --- FRAME 07.010: DUST DISSIPATES ---
PNT 98 60 10 6 4
PNT 100 62 6 4 4
C
REC 3
C
C --- FRAME 07.011: SECOND WALK CYCLE ---
LIN 52 56 50 66 4
LIN 54 56 56 66 4
LIN 60 56 58 66 4
LIN 62 56 64 66 4
LIN 52 56 48 66 5
LIN 54 56 58 66 5
LIN 60 56 56 66 5
LIN 62 56 66 66 5
C
REC 2
C
LIN 52 56 48 66 4
LIN 54 56 58 66 4
LIN 60 56 56 66 4
LIN 62 56 66 66 4
LIN 52 56 50 66 5
LIN 54 56 56 66 5
LIN 60 56 58 66 5
LIN 62 56 64 66 5
C
REC 2
C
C --- FRAME 07.012: DRIVER ADJUSTS REINS ---
LIN 72 40 64 44 4
LIN 72 40 62 42 5
C
REC 2
C
LIN 72 40 62 42 4
LIN 72 40 64 44 5
C
REC 2
C
C --- FRAME 07.013: TAIL SWISH ---
LIN 64 49 68 46 4
LIN 68 46 70 48 4
LIN 64 49 66 44 5
LIN 66 44 68 46 4
C
REC 2
C
LIN 64 49 66 44 4
LIN 66 44 68 46 4
LIN 64 49 68 46 5
LIN 68 46 70 48 4
C
REC 2
C
C --- FRAME 07.014: CHIMNEY SMOKE DRIFTS ---
PNT 15 10 3 2 0
PNT 14 8 4 3 1
PNT 13 6 5 3 1
C
REC 3
C
PNT 13 6 5 3 0
PNT 15 10 3 2 1
PNT 16 12 2 2 1
C
REC 3
C
C --- FRAME 07.015: HOLD ON FARM ROAD ---
REC 8
C
C
C ============================================================
C  SCENE 08: EXT PALO ALTO RACETRACK — 1878 — DAY
C  EADWEARD MUYBRIDGE EXPERIMENT
C  Sallie Gardner gallops through the camera array.
C  Sequential shutter clicks. The birth of cinema.
C  Trip-wire cameras line the track edge.
C ============================================================
C
C --- FRAME 08.001: BASE RACETRACK ---
CLR 0
C Sky
PNT 0 0 128 16 1
C Distant hills — low California hills
PNT 0 14 128 4 2
PNT 10 14 20 3 3
PNT 40 13 25 4 3
PNT 80 14 30 3 3
C
C Track surface — level packed dirt
PNT 0 18 128 34 3
C Track lane markings
LIN 0 20 127 20 4
LIN 0 50 127 50 4
C Rail — white fence along top edge
PNT 0 18 128 2 5
LIN 0 18 127 18 6
C Inner rail
PNT 0 52 128 2 5
LIN 0 52 127 52 6
C
C Track texture — packed earth
PNT 0 24 128 2 4
PNT 0 30 128 2 2
PNT 0 36 128 2 4
PNT 0 42 128 2 2
C
C Infield — green grass
PNT 0 54 128 24 3
PNT 0 56 128 2 2
PNT 0 62 128 2 4
PNT 0 68 128 2 2
C
C Spectator area — beyond inner rail
PNT 0 78 128 18 4
C Spectator figures — small dots
PNT 10 80 4 4 5
PNT 20 80 4 4 5
PNT 30 80 4 4 5
PNT 42 80 4 4 5
PNT 54 80 4 4 5
PNT 66 80 4 4 5
PNT 78 80 4 4 5
PNT 90 80 4 4 5
PNT 102 80 4 4 5
PNT 114 80 4 4 5
C
C --- CAMERA ARRAY --- 12 cameras along track edge ---
C Each camera is a small box on tripod
C Camera 1
PNT 4 44 3 4 5
LIN 5 48 5 52 4
PNT 4 43 3 1 6
C Camera 2
PNT 14 44 3 4 5
LIN 15 48 15 52 4
PNT 14 43 3 1 6
C Camera 3
PNT 24 44 3 4 5
LIN 25 48 25 52 4
PNT 24 43 3 1 6
C Camera 4
PNT 34 44 3 4 5
LIN 35 48 35 52 4
PNT 34 43 3 1 6
C Camera 5
PNT 44 44 3 4 5
LIN 45 48 45 52 4
PNT 44 43 3 1 6
C Camera 6
PNT 54 44 3 4 5
LIN 55 48 55 52 4
PNT 54 43 3 1 6
C Camera 7
PNT 64 44 3 4 5
LIN 65 48 65 52 4
PNT 64 43 3 1 6
C Camera 8
PNT 74 44 3 4 5
LIN 75 48 75 52 4
PNT 74 43 3 1 6
C Camera 9
PNT 84 44 3 4 5
LIN 85 48 85 52 4
PNT 84 43 3 1 6
C Camera 10
PNT 94 44 3 4 5
LIN 95 48 95 52 4
PNT 94 43 3 1 6
C Camera 11
PNT 104 44 3 4 5
LIN 105 48 105 52 4
PNT 104 43 3 1 6
C Camera 12
PNT 114 44 3 4 5
LIN 115 48 115 52 4
PNT 114 43 3 1 6
C
C Trip wires across track — thin horizontal lines
LIN 5 36 5 44 2
LIN 15 36 15 44 2
LIN 25 36 25 44 2
LIN 35 36 35 44 2
LIN 45 36 45 44 2
LIN 55 36 55 44 2
LIN 65 36 65 44 2
LIN 75 36 75 44 2
LIN 85 36 85 44 2
LIN 95 36 95 44 2
LIN 105 36 105 44 2
LIN 115 36 115 44 2
C
C --- HORSE — Sallie Gardner — starting position left ---
C Body
PNT 2 26 14 8 6
PNT 4 27 10 6 7
C Neck
PNT 0 20 4 8 6
C Head
PNT 0 16 4 5 6
PNT 0 17 2 3 7
PNT 1 18 1 1 0
C Ear
PNT 0 15 2 2 7
C Front legs — gallop extended
LIN 4 34 0 40 6
LIN 6 34 10 40 6
C Back legs — gallop extended
LIN 12 34 8 40 6
LIN 14 34 18 40 6
C Hooves
PNT 0 40 2 2 7
PNT 9 40 2 2 7
PNT 7 40 2 2 7
PNT 17 40 2 2 7
C Tail — streaming
LIN 16 27 22 24 6
LIN 22 24 26 26 5
C
C Jockey
PNT 6 22 4 4 5
PNT 7 23 2 2 6
PNT 7 20 2 3 5
PNT 7 19 2 2 6
C
REC 6
C
C --- FRAME 08.002: HORSE GALLOP FRAME 2 — legs gathered ---
C Erase old legs
PNT 0 34 20 10 3
C Legs gathered under body
LIN 6 34 4 38 6
LIN 8 34 6 38 6
LIN 10 34 8 38 6
LIN 12 34 10 38 6
PNT 3 38 2 2 7
PNT 5 38 2 2 7
PNT 7 38 2 2 7
PNT 9 38 2 2 7
C
REC 2
C
C --- FRAME 08.003: CAMERA 1 FLASH ---
PNT 4 43 3 1 7
C
REC 1
C
PNT 4 43 3 1 6
C
REC 1
C
C --- FRAME 08.004: HORSE MOVES TO CAMERA 2 POSITION ---
C Shift horse right — erase old, draw new
PNT 0 16 18 26 3
C Redraw horse at position 2
PNT 12 26 14 8 6
PNT 14 27 10 6 7
PNT 10 20 4 8 6
PNT 10 16 4 5 6
PNT 10 17 2 3 7
PNT 11 18 1 1 0
PNT 10 15 2 2 7
C Legs extended
LIN 14 34 10 40 6
LIN 16 34 20 40 6
LIN 22 34 18 40 6
LIN 24 34 28 40 6
C Jockey
PNT 16 22 4 4 5
PNT 17 20 2 3 5
C Tail
LIN 26 27 32 24 6
C
REC 2
C
C --- FRAME 08.005: CAMERA 2 FLASH ---
PNT 14 43 3 1 7
C
REC 1
C
PNT 14 43 3 1 6
C
REC 1
C
C --- FRAME 08.006: HORSE MOVES TO CAMERA 3 ---
PNT 10 16 18 26 3
PNT 22 26 14 8 6
PNT 24 27 10 6 7
PNT 20 20 4 8 6
PNT 20 16 4 5 6
PNT 20 17 2 3 7
PNT 21 18 1 1 0
PNT 20 15 2 2 7
LIN 24 34 20 40 6
LIN 26 34 30 40 6
LIN 32 34 28 40 6
LIN 34 34 38 40 6
PNT 26 22 4 4 5
LIN 36 27 42 24 6
C
REC 2
C
C --- FRAME 08.007: CAMERA 3 FLASH ---
PNT 24 43 3 1 7
C
REC 1
C
PNT 24 43 3 1 6
C
REC 1
C
C --- FRAME 08.008: HORSE MOVES TO CAMERA 5 --- skip for speed
PNT 20 16 18 26 3
PNT 42 26 14 8 6
PNT 44 27 10 6 7
PNT 40 20 4 8 6
PNT 40 16 4 5 6
PNT 40 17 2 3 7
PNT 41 18 1 1 0
PNT 40 15 2 2 7
C Legs gathered
LIN 46 34 44 38 6
LIN 48 34 46 38 6
LIN 50 34 48 38 6
LIN 52 34 50 38 6
PNT 46 22 4 4 5
LIN 56 27 62 24 6
C
REC 2
C
C --- FRAME 08.009: CAMERA 5 FLASH ---
PNT 44 43 3 1 7
C
REC 1
C
PNT 44 43 3 1 6
C
REC 1
C
C --- FRAME 08.010: HORSE AT CAMERA 8 ---
PNT 40 16 18 26 3
PNT 72 26 14 8 6
PNT 74 27 10 6 7
PNT 70 20 4 8 6
PNT 70 16 4 5 6
PNT 70 17 2 3 7
PNT 71 18 1 1 0
PNT 70 15 2 2 7
LIN 74 34 70 40 6
LIN 76 34 80 40 6
LIN 82 34 78 40 6
LIN 84 34 88 40 6
PNT 76 22 4 4 5
LIN 86 27 92 24 6
C
REC 2
C
C --- FRAME 08.011: CAMERA 8 FLASH ---
PNT 74 43 3 1 7
C
REC 1
C
PNT 74 43 3 1 6
C
REC 1
C
C --- FRAME 08.012: HORSE AT CAMERA 12 — end of array ---
PNT 70 16 20 26 3
PNT 108 26 14 8 6
PNT 110 27 10 6 7
PNT 106 20 4 8 6
PNT 106 16 4 5 6
PNT 106 17 2 3 7
PNT 107 18 1 1 0
PNT 106 15 2 2 7
LIN 110 34 106 40 6
LIN 112 34 116 40 6
LIN 118 34 114 40 6
LIN 120 34 124 40 6
PNT 112 22 4 4 5
LIN 122 27 127 24 6
C
REC 2
C
C --- FRAME 08.013: CAMERA 12 FLASH ---
PNT 114 43 3 1 7
C
REC 1
C
PNT 114 43 3 1 6
C
REC 1
C
C --- FRAME 08.014: HORSE EXITS FRAME RIGHT ---
PNT 106 16 22 26 3
C Empty track — aftermath
C
REC 4
C
C --- FRAME 08.015: SPECTATOR REACTION — heads shift ---
PNT 10 80 4 4 6
PNT 42 80 4 4 6
PNT 78 80 4 4 6
PNT 114 80 4 4 6
C
REC 3
C
PNT 10 80 4 4 5
PNT 42 80 4 4 5
PNT 78 80 4 4 5
PNT 114 80 4 4 5
C
REC 3
C
C --- FRAME 08.016: HOLD ON EMPTY TRACK ---
REC 8
C
C
C ============================================================
C  SCENE 09: INT LAW SCHOOL LECTURE HALL — NIGHT
C  THE LAW OF THE HORSE discussion.
C  Tiered lecture hall, professor at podium, chalkboard.
C  Students in ascending rows.
C ============================================================
C
C --- FRAME 09.001: BASE LECTURE HALL ---
CLR 0
C Ceiling — dark academic
PNT 0 0 128 8 1
C Lighting — hanging lamps
PNT 30 4 4 4 3
PNT 64 4 4 4 3
PNT 98 4 4 4 3
C Lamp cables
LIN 32 0 32 4 2
LIN 66 0 66 4 2
LIN 100 0 100 4 2
C Light pools on floor
PNT 24 66 16 4 2
PNT 58 66 16 4 2
PNT 92 66 16 4 2
C
C Back wall
PNT 0 8 128 12 2
C
C --- CHALKBOARD --- large green/dark panel
PNT 20 10 88 16 1
PNT 22 12 84 12 0
C Chalk writing — "THE LAW OF THE HORSE"
C Approximate text with horizontal lines
LIN 30 15 40 15 3
LIN 42 15 52 15 3
LIN 54 15 60 15 3
LIN 62 15 72 15 3
LIN 30 18 44 18 3
LIN 46 18 60 18 3
LIN 62 18 78 18 3
LIN 80 18 98 18 3
C Chalk tray
PNT 20 26 88 2 4
C Eraser
PNT 92 24 4 2 5
C Chalk pieces
PNT 24 24 2 1 7
PNT 28 24 2 1 7
C
C Chalkboard frame
LIN 20 10 108 10 3
LIN 20 26 108 26 3
LIN 20 10 20 26 3
LIN 108 10 108 26 3
C
C Podium — front center
PNT 56 48 16 18 5
PNT 58 50 12 14 6
C Podium top
LIN 56 48 72 48 7
C Podium lamp
PNT 60 46 2 2 4
C Microphone
LIN 68 46 70 42 5
PNT 70 41 1 2 6
C
C --- PROFESSOR figure at podium ---
PNT 58 34 12 14 4
PNT 60 36 8 10 5
C Head
PNT 60 26 8 8 4
PNT 61 27 6 6 5
C Hair — professorial
PNT 61 26 6 2 6
C Glasses
LIN 62 29 64 29 6
LIN 65 29 67 29 6
C Eyes
PNT 63 29 1 1 7
PNT 66 29 1 1 7
C Mouth — speaking
LIN 63 32 66 32 5
C
C Arm — pointing at chalkboard
LIN 58 38 40 24 5
PNT 38 22 3 3 4
C
C --- TIERED SEATING — ascending rows ---
C Row 1 — closest to podium
PNT 0 60 128 6 3
C Students row 1
PNT 8 56 6 4 4
PNT 18 56 6 4 4
PNT 30 56 6 4 4
PNT 86 56 6 4 4
PNT 98 56 6 4 4
PNT 110 56 6 4 4
C Student heads row 1
PNT 9 52 4 4 4
PNT 19 52 4 4 4
PNT 31 52 4 4 4
PNT 87 52 4 4 4
PNT 99 52 4 4 4
PNT 111 52 4 4 4
C
C Row 2 — higher
PNT 0 46 128 6 3
C Students row 2
PNT 6 42 6 4 4
PNT 16 42 6 4 4
PNT 28 42 6 4 4
PNT 40 42 6 4 4
PNT 84 42 6 4 4
PNT 96 42 6 4 4
PNT 108 42 6 4 4
PNT 120 42 6 4 4
C Student heads row 2
PNT 7 38 4 4 4
PNT 17 38 4 4 4
PNT 29 38 4 4 4
PNT 41 38 4 4 4
PNT 85 38 4 4 4
PNT 97 38 4 4 4
PNT 109 38 4 4 4
PNT 121 38 4 4 4
C
C Row 3 — highest
PNT 0 32 128 6 3
C Students row 3 — fewer visible
PNT 4 28 6 4 4
PNT 16 28 6 4 4
PNT 110 28 6 4 4
PNT 122 28 6 4 4
C
C Desk surfaces
LIN 0 60 127 60 5
LIN 0 46 127 46 5
LIN 0 32 127 32 5
C
C Floor — front area
PNT 0 66 128 30 3
PNT 0 68 128 2 4
PNT 0 76 128 2 2
PNT 0 84 128 2 4
C
REC 8
C
C --- FRAME 09.002: PROFESSOR SPEAKS — mouth animation ---
LIN 63 32 66 32 4
PNT 63 32 4 2 5
C
REC 2
C
LIN 63 32 66 32 5
PNT 63 32 4 2 4
C
REC 2
C
C --- FRAME 09.003: ARM GESTURE — pointing sweeps ---
PNT 38 22 3 3 2
LIN 58 38 40 24 2
LIN 58 38 50 20 5
PNT 48 18 3 3 4
C
REC 3
C
C --- FRAME 09.004: ARM RETURNS ---
PNT 48 18 3 3 2
LIN 58 38 50 20 2
LIN 58 38 40 24 5
PNT 38 22 3 3 4
C
REC 3
C
C --- FRAME 09.005: STUDENT RAISES HAND ---
C Student at position 86,56
PNT 87 52 4 4 5
LIN 89 52 89 46 5
PNT 88 44 2 2 4
C
REC 4
C
C --- FRAME 09.006: HAND LOWERS ---
PNT 88 44 2 4 3
LIN 89 52 89 46 3
PNT 87 52 4 4 4
C
REC 3
C
C --- FRAME 09.007: PROFESSOR NOD ---
PNT 60 26 8 8 3
PNT 60 27 8 8 4
PNT 61 28 6 6 5
C
REC 2
C
PNT 60 27 8 8 3
PNT 60 26 8 8 4
PNT 61 27 6 6 5
C
REC 2
C
C --- FRAME 09.008: LAMP FLICKER ---
PNT 64 4 4 4 4
C
REC 1
C
PNT 64 4 4 4 3
C
REC 2
C
C --- FRAME 09.009: CHALKBOARD — new line added ---
LIN 30 21 58 21 3
C
REC 3
C
C --- FRAME 09.010: ANOTHER STUDENT SHIFTS ---
PNT 31 52 4 4 5
C
REC 2
C
PNT 31 52 4 4 4
C
REC 2
C
C --- FRAME 09.011: PROFESSOR SPEAKS AGAIN ---
PNT 63 32 4 2 5
C
REC 2
C
PNT 63 32 4 2 4
LIN 63 32 66 32 5
C
REC 2
C
C --- FRAME 09.012: HOLD ON LECTURE HALL ---
REC 10
C
C --- END OF BATCH 3: SCENES 07-09 ---
C
C ============================================================
C  SCENE 10: EXT CONNECTICUT ROAD — 1871 — DAY
C  HASLEM V LOCKWOOD — horse manure property case.
C  Workers raking manure into organized heaps on road.
C  Another man arrives to steal the organized piles.
C  Scattered waste becomes property once labor organizes it.
C ============================================================
C
C --- FRAME 10.001: BASE ROAD SCENE ---
CLR 0
C Sky — overcast New England
PNT 0 0 128 18 2
PNT 0 14 128 4 1
C Bare trees — late autumn
C Tree 1
LIN 8 10 8 40 4
LIN 8 18 4 12 4
LIN 8 16 12 10 4
LIN 8 22 2 18 4
LIN 8 20 14 14 4
LIN 4 12 2 10 3
LIN 12 10 14 8 3
C Tree 2
LIN 116 12 116 42 4
LIN 116 20 112 14 4
LIN 116 18 120 12 4
LIN 116 24 110 18 4
LIN 116 22 122 16 4
LIN 112 14 110 12 3
LIN 120 12 122 10 3
C
C Stone wall — left side
PNT 0 36 20 6 4
PNT 2 37 16 4 5
PNT 4 38 12 2 4
C Stone texture
PNT 2 36 4 2 5
PNT 8 37 4 2 5
PNT 14 36 4 2 5
C
C Stone wall — right side
PNT 108 36 20 6 4
PNT 110 37 16 4 5
PNT 112 38 12 2 4
PNT 110 36 4 2 5
PNT 116 37 4 2 5
PNT 122 36 4 2 5
C
C Dirt road — wide muddy Connecticut road
PNT 20 36 88 30 3
PNT 22 38 84 26 4
C Road ruts
LIN 40 36 38 66 3
LIN 88 36 90 66 3
C Puddles
PNT 50 50 8 4 2
PNT 72 44 6 4 2
C
C Grass edges
PNT 0 42 22 24 3
PNT 106 42 22 24 3
PNT 0 66 128 30 3
PNT 0 68 128 2 4
PNT 0 76 128 2 2
PNT 0 84 128 2 4
C
C --- WORKER 1 — raking manure, left side ---
PNT 34 32 8 14 4
PNT 36 34 4 10 5
C Head
PNT 36 26 4 6 4
PNT 37 27 2 4 5
C Hat
PNT 35 24 6 3 5
C Arms holding rake — extended
LIN 34 36 28 42 5
LIN 42 36 48 42 5
C Rake
LIN 28 42 28 48 5
LIN 26 48 30 48 4
PNT 25 47 6 2 4
C
C Legs — standing
LIN 36 46 36 56 5
LIN 40 46 40 56 5
PNT 35 56 2 2 5
PNT 39 56 2 2 5
C
C --- WORKER 2 — shoveling, right side ---
PNT 72 32 8 14 4
PNT 74 34 4 10 5
C Head
PNT 74 26 4 6 4
PNT 75 27 2 4 5
C Hat
PNT 73 24 6 3 5
C Arms holding shovel
LIN 72 36 68 44 5
LIN 80 36 84 40 5
C Shovel
LIN 68 44 68 50 5
PNT 66 49 4 3 4
C
C Legs
LIN 74 46 74 56 5
LIN 78 46 78 56 5
PNT 73 56 2 2 5
PNT 77 56 2 2 5
C
C --- MANURE HEAPS — scattered and organized ---
C Scattered manure — small spots
PNT 30 48 3 2 5
PNT 44 46 2 2 5
PNT 56 50 3 2 5
PNT 62 48 2 2 5
PNT 82 46 3 2 5
PNT 90 50 2 2 5
C
C Organized heap — larger pile where workers have gathered
PNT 48 42 12 6 5
PNT 50 43 8 4 6
PNT 52 44 4 2 5
C
C --- HORSE-DRAWN CART — background, approaching ---
C Horse
PNT 94 28 8 6 5
PNT 96 29 4 4 6
PNT 92 24 3 5 5
PNT 91 22 3 3 5
PNT 91 23 1 1 7
C Horse legs
LIN 96 34 96 38 5
LIN 98 34 98 38 5
LIN 100 34 100 38 5
C Cart behind horse
PNT 102 26 10 8 4
PNT 103 27 8 6 5
C Cart wheels
PNT 104 34 2 4 5
PNT 110 34 2 4 5
C
C Figure on cart — the thief approaching
PNT 104 22 6 6 4
PNT 105 23 4 4 5
PNT 106 18 2 4 4
PNT 106 17 2 2 5
C
REC 8
C
C --- FRAME 10.002: WORKER 1 RAKE STROKE ---
C Rake pulls backward
PNT 25 47 6 2 3
LIN 28 42 28 48 3
LIN 28 42 32 50 5
PNT 30 49 6 2 4
C
REC 2
C
C --- FRAME 10.003: RAKE FORWARD ---
PNT 30 49 6 2 3
LIN 28 42 32 50 3
LIN 28 42 28 48 5
PNT 25 47 6 2 4
C
REC 2
C
C --- FRAME 10.004: WORKER 2 SHOVEL LIFT ---
PNT 66 49 4 3 3
LIN 68 44 68 50 3
C Shovel lifts with material
LIN 68 44 68 40 5
PNT 66 38 4 3 5
PNT 67 37 2 2 6
C
REC 3
C
C --- FRAME 10.005: SHOVEL DUMPS ONTO HEAP ---
PNT 66 38 4 3 3
PNT 67 37 2 2 3
LIN 68 44 68 40 3
C Material falls onto heap
PNT 48 42 12 6 6
PNT 50 41 8 4 5
C Restore shovel down
LIN 68 44 68 50 5
PNT 66 49 4 3 4
C
REC 3
C
C --- FRAME 10.006: HEAP GROWS ---
PNT 48 40 14 8 5
PNT 50 41 10 6 6
PNT 52 42 6 4 5
C
REC 3
C
C --- FRAME 10.007: THIEF'S CART APPROACHES — closer ---
C Erase old cart position
PNT 92 18 22 22 3
PNT 92 22 12 18 3
C Redraw closer — larger
PNT 86 28 10 8 5
PNT 88 29 6 6 6
PNT 84 22 4 8 5
PNT 83 20 4 4 5
PNT 83 21 1 1 7
LIN 88 36 88 42 5
LIN 90 36 90 42 5
LIN 92 36 92 42 5
C Cart
PNT 94 24 14 10 4
PNT 95 25 12 8 5
C Wheels
PNT 96 34 3 6 5
PNT 106 34 3 6 5
C Thief
PNT 98 18 6 8 4
PNT 99 19 4 6 5
PNT 100 14 2 4 4
PNT 100 13 2 2 5
C
REC 4
C
C --- FRAME 10.008: WORKER 1 NOTICES THIEF ---
C Head turns right
PNT 37 27 2 4 4
PNT 38 27 2 4 5
C
REC 3
C
C --- FRAME 10.009: WORKER 1 HEAD RETURNS ---
PNT 38 27 2 4 4
PNT 37 27 2 4 5
C
REC 2
C
C --- FRAME 10.010: RAKE STROKE 2 ---
PNT 25 47 6 2 3
LIN 28 42 28 48 3
LIN 28 42 32 50 5
PNT 30 49 6 2 4
C
REC 2
C
PNT 30 49 6 2 3
LIN 28 42 32 50 3
LIN 28 42 28 48 5
PNT 25 47 6 2 4
C
REC 2
C
C --- FRAME 10.011: SCATTERED MANURE DIMINISHES ---
C Some spots disappear as workers collect them
PNT 44 46 2 2 4
PNT 62 48 2 2 4
PNT 82 46 3 2 4
C
REC 3
C
C --- FRAME 10.012: HOLD ON ROAD SCENE ---
REC 8
C
C
C ============================================================
C  SCENE 11: INT DATA CENTER — NIGHT
C  TOKENS TO GRADIENTS — the digital transformation.
C  Rows of server racks, blinking lights, cable runs.
C  Web pages become datasets become tokens become models.
C  The humming cathedral of computation.
C ============================================================
C
C --- FRAME 11.001: BASE DATA CENTER ---
CLR 0
C Ceiling — industrial grid
PNT 0 0 128 6 2
C Fluorescent light strips
PNT 10 2 20 2 3
PNT 50 2 20 2 3
PNT 90 2 20 2 3
C Light reflection on floor
PNT 8 86 24 4 2
PNT 48 86 24 4 2
PNT 88 86 24 4 2
C
C Floor — raised tile pattern
PNT 0 82 128 14 3
PNT 0 84 128 2 4
PNT 0 88 128 2 2
PNT 0 92 128 2 4
C Floor tile grid
LIN 0 82 127 82 4
LIN 16 82 16 96 3
LIN 32 82 32 96 3
LIN 48 82 48 96 3
LIN 64 82 64 96 3
LIN 80 82 80 96 3
LIN 96 82 96 96 3
LIN 112 82 112 96 3
C
C --- SERVER RACK ROW 1 — left side ---
PNT 4 8 14 74 4
PNT 6 10 10 70 5
C Rack frame
LIN 4 8 18 8 6
LIN 4 82 18 82 6
LIN 4 8 4 82 5
LIN 18 8 18 82 5
C Server units — horizontal slots
PNT 6 12 10 4 4
PNT 6 18 10 4 5
PNT 6 24 10 4 4
PNT 6 30 10 4 5
PNT 6 36 10 4 4
PNT 6 42 10 4 5
PNT 6 48 10 4 4
PNT 6 54 10 4 5
PNT 6 60 10 4 4
PNT 6 66 10 4 5
PNT 6 72 10 4 4
PNT 6 78 10 4 5
C LED indicator lights — right edge of each unit
PNT 15 13 1 1 3
PNT 15 19 1 1 2
PNT 15 25 1 1 3
PNT 15 31 1 1 2
PNT 15 37 1 1 3
PNT 15 43 1 1 2
PNT 15 49 1 1 3
PNT 15 55 1 1 2
PNT 15 61 1 1 3
PNT 15 67 1 1 2
PNT 15 73 1 1 3
PNT 15 79 1 1 2
C
C --- SERVER RACK ROW 2 ---
PNT 22 8 14 74 4
PNT 24 10 10 70 5
LIN 22 8 36 8 6
LIN 22 82 36 82 6
LIN 22 8 22 82 5
LIN 36 8 36 82 5
C Server units
PNT 24 12 10 4 4
PNT 24 18 10 4 5
PNT 24 24 10 4 4
PNT 24 30 10 4 5
PNT 24 36 10 4 4
PNT 24 42 10 4 5
PNT 24 48 10 4 4
PNT 24 54 10 4 5
PNT 24 60 10 4 4
PNT 24 66 10 4 5
PNT 24 72 10 4 4
PNT 24 78 10 4 5
C LEDs
PNT 33 13 1 1 2
PNT 33 19 1 1 3
PNT 33 25 1 1 2
PNT 33 31 1 1 3
PNT 33 37 1 1 2
PNT 33 43 1 1 3
PNT 33 49 1 1 2
PNT 33 55 1 1 3
PNT 33 61 1 1 2
PNT 33 67 1 1 3
PNT 33 73 1 1 2
PNT 33 79 1 1 3
C
C --- SERVER RACK ROW 3 ---
PNT 40 8 14 74 4
PNT 42 10 10 70 5
LIN 40 8 54 8 6
LIN 40 82 54 82 6
LIN 40 8 40 82 5
LIN 54 8 54 82 5
PNT 42 12 10 4 4
PNT 42 18 10 4 5
PNT 42 24 10 4 4
PNT 42 30 10 4 5
PNT 42 36 10 4 4
PNT 42 42 10 4 5
PNT 42 48 10 4 4
PNT 42 54 10 4 5
PNT 42 60 10 4 4
PNT 42 66 10 4 5
PNT 42 72 10 4 4
PNT 42 78 10 4 5
PNT 51 13 1 1 3
PNT 51 19 1 1 2
PNT 51 25 1 1 3
PNT 51 31 1 1 2
PNT 51 37 1 1 3
PNT 51 43 1 1 2
PNT 51 49 1 1 3
PNT 51 55 1 1 2
PNT 51 61 1 1 3
PNT 51 67 1 1 2
PNT 51 73 1 1 3
PNT 51 79 1 1 2
C
C --- AISLE between racks — center walkway ---
PNT 56 8 16 74 2
PNT 58 10 12 70 1
C Aisle floor
PNT 56 82 16 14 3
C
C --- SERVER RACK ROW 4 ---
PNT 74 8 14 74 4
PNT 76 10 10 70 5
LIN 74 8 88 8 6
LIN 74 82 88 82 6
LIN 74 8 74 82 5
LIN 88 8 88 82 5
PNT 76 12 10 4 4
PNT 76 18 10 4 5
PNT 76 24 10 4 4
PNT 76 30 10 4 5
PNT 76 36 10 4 4
PNT 76 42 10 4 5
PNT 76 48 10 4 4
PNT 76 54 10 4 5
PNT 76 60 10 4 4
PNT 76 66 10 4 5
PNT 76 72 10 4 4
PNT 76 78 10 4 5
PNT 85 13 1 1 2
PNT 85 19 1 1 3
PNT 85 25 1 1 2
PNT 85 31 1 1 3
PNT 85 37 1 1 2
PNT 85 43 1 1 3
PNT 85 49 1 1 2
PNT 85 55 1 1 3
PNT 85 61 1 1 2
PNT 85 67 1 1 3
PNT 85 73 1 1 2
PNT 85 79 1 1 3
C
C --- SERVER RACK ROW 5 ---
PNT 92 8 14 74 4
PNT 94 10 10 70 5
LIN 92 8 106 8 6
LIN 92 82 106 82 6
LIN 92 8 92 82 5
LIN 106 8 106 82 5
PNT 94 12 10 4 4
PNT 94 18 10 4 5
PNT 94 24 10 4 4
PNT 94 30 10 4 5
PNT 94 36 10 4 4
PNT 94 42 10 4 5
PNT 94 48 10 4 4
PNT 94 54 10 4 5
PNT 94 60 10 4 4
PNT 94 66 10 4 5
PNT 94 72 10 4 4
PNT 94 78 10 4 5
PNT 103 13 1 1 3
PNT 103 19 1 1 2
PNT 103 25 1 1 3
PNT 103 31 1 1 2
PNT 103 37 1 1 3
PNT 103 43 1 1 2
PNT 103 49 1 1 3
PNT 103 55 1 1 2
PNT 103 61 1 1 3
PNT 103 67 1 1 2
PNT 103 73 1 1 3
PNT 103 79 1 1 2
C
C --- CABLE RUNS overhead between racks ---
LIN 18 6 22 6 4
LIN 36 6 40 6 4
LIN 54 6 74 6 4
LIN 88 6 92 6 4
C
REC 8
C
C --- FRAME 11.002: LED BLINK CYCLE 1 — rack 1 ---
PNT 15 13 1 1 2
PNT 15 25 1 1 2
PNT 15 37 1 1 2
PNT 15 49 1 1 2
PNT 15 61 1 1 2
PNT 15 73 1 1 2
C
REC 1
C
PNT 15 13 1 1 3
PNT 15 25 1 1 3
PNT 15 37 1 1 3
PNT 15 49 1 1 3
PNT 15 61 1 1 3
PNT 15 73 1 1 3
C
REC 1
C
C --- FRAME 11.003: LED BLINK CYCLE 2 — rack 2 ---
PNT 33 19 1 1 2
PNT 33 31 1 1 2
PNT 33 43 1 1 2
PNT 33 55 1 1 2
PNT 33 67 1 1 2
PNT 33 79 1 1 2
C
REC 1
C
PNT 33 19 1 1 3
PNT 33 31 1 1 3
PNT 33 43 1 1 3
PNT 33 55 1 1 3
PNT 33 67 1 1 3
PNT 33 79 1 1 3
C
REC 1
C
C --- FRAME 11.004: LED CASCADE — wave through racks ---
PNT 15 13 1 1 4
PNT 33 19 1 1 4
PNT 51 25 1 1 4
PNT 85 31 1 1 4
PNT 103 37 1 1 4
C
REC 1
C
PNT 15 13 1 1 3
PNT 33 19 1 1 3
PNT 51 25 1 1 3
PNT 85 31 1 1 3
PNT 103 37 1 1 3
C Next wave
PNT 15 25 1 1 4
PNT 33 31 1 1 4
PNT 51 37 1 1 4
PNT 85 43 1 1 4
PNT 103 49 1 1 4
C
REC 1
C
PNT 15 25 1 1 3
PNT 33 31 1 1 3
PNT 51 37 1 1 3
PNT 85 43 1 1 3
PNT 103 49 1 1 3
C
REC 1
C
C --- FRAME 11.005: DATA FLOW VISUALIZATION — aisle ---
C Flowing particles down the aisle
PNT 62 10 2 2 3
PNT 64 20 2 2 3
PNT 60 30 2 2 3
PNT 66 40 2 2 3
PNT 62 50 2 2 3
C
REC 2
C
C --- FRAME 11.006: PARTICLES MOVE DOWN ---
PNT 62 10 2 2 1
PNT 64 20 2 2 1
PNT 60 30 2 2 1
PNT 66 40 2 2 1
PNT 62 50 2 2 1
C Shift down
PNT 62 20 2 2 3
PNT 64 30 2 2 3
PNT 60 40 2 2 3
PNT 66 50 2 2 3
PNT 62 60 2 2 3
C
REC 2
C
C --- FRAME 11.007: PARTICLES EXIT ---
PNT 62 20 2 2 1
PNT 64 30 2 2 1
PNT 60 40 2 2 1
PNT 66 50 2 2 1
PNT 62 60 2 2 1
C New wave
PNT 64 12 2 2 3
PNT 60 22 2 2 3
PNT 66 32 2 2 3
PNT 62 42 2 2 3
PNT 64 52 2 2 3
C
REC 2
C
C --- FRAME 11.008: PARTICLES FADE ---
PNT 64 12 2 2 1
PNT 60 22 2 2 1
PNT 66 32 2 2 1
PNT 62 42 2 2 1
PNT 64 52 2 2 1
C
REC 2
C
C --- FRAME 11.009: FLUORESCENT FLICKER ---
PNT 50 2 20 2 4
C
REC 1
C
PNT 50 2 20 2 3
C
REC 2
C
C --- FRAME 11.010: LED BLINK RACK 4-5 ---
PNT 85 13 1 1 4
PNT 85 37 1 1 4
PNT 85 61 1 1 4
PNT 103 25 1 1 4
PNT 103 49 1 1 4
PNT 103 73 1 1 4
C
REC 1
C
PNT 85 13 1 1 2
PNT 85 37 1 1 2
PNT 85 61 1 1 2
PNT 103 25 1 1 3
PNT 103 49 1 1 3
PNT 103 73 1 1 3
C
REC 2
C
C --- FRAME 11.011: HOLD ON DATA CENTER ---
REC 10
C
C
C ============================================================
C  SCENE 12: INT MUSIC PUBLISHER OFFICE — DAY
C  SONGWRITERS — lyrics on screens, rights disputes.
C  A creative office with sheet music, guitars, screens.
C  The lyric says: I came from someone.
C ============================================================
C
C --- FRAME 12.001: BASE OFFICE ---
CLR 0
C Walls — warm interior
PNT 0 0 128 22 2
C Accent wall — one side darker
PNT 0 0 32 22 3
C
C Window — right wall
PNT 96 4 26 14 1
PNT 98 6 22 10 0
C Window frame
LIN 96 4 122 4 3
LIN 96 18 122 18 3
LIN 96 4 96 18 3
LIN 122 4 122 18 3
LIN 109 4 109 18 3
C Curtain — left side
PNT 94 4 4 16 3
C
C Floor — hardwood
PNT 0 64 128 32 3
PNT 0 66 128 2 4
PNT 0 74 128 2 2
PNT 0 82 128 2 4
PNT 0 90 128 2 2
C
C --- DESK with computer ---
PNT 44 40 40 12 5
PNT 46 42 36 8 6
LIN 44 40 84 40 7
LIN 44 52 84 52 6
C Desk legs
LIN 48 52 48 62 5
LIN 80 52 80 62 5
C
C Monitor — showing lyrics
PNT 54 24 24 16 1
PNT 56 26 20 12 0
C Lyric lines on screen
LIN 58 28 74 28 3
LIN 58 30 72 30 3
LIN 58 32 70 32 3
LIN 58 34 74 34 3
LIN 58 36 68 36 3
C Monitor stand
PNT 64 40 4 2 4
C
C Keyboard
PNT 52 44 20 3 4
PNT 54 45 16 1 5
C
C --- SONGWRITER at desk ---
PNT 38 34 12 18 4
PNT 40 36 8 14 5
C Head
PNT 40 26 8 8 4
PNT 41 27 6 6 5
C Hair
PNT 41 26 6 2 6
C Eyes — looking at screen
PNT 43 29 1 1 7
PNT 46 29 1 1 7
C Arm on desk
LIN 38 40 48 44 5
LIN 50 40 56 44 5
C
C Chair
PNT 36 52 14 8 4
PNT 38 54 10 4 5
C
C --- GUITAR leaning against wall ---
C Body
PNT 6 48 8 12 5
PNT 8 50 4 8 6
C Sound hole
PNT 9 53 2 2 4
C Neck
LIN 10 36 10 48 5
LIN 11 36 11 48 4
C Headstock
PNT 9 34 3 3 5
C Tuning pegs
PNT 8 34 1 1 6
PNT 12 34 1 1 6
PNT 8 36 1 1 6
PNT 12 36 1 1 6
C
C --- SECOND GUITAR on stand ---
PNT 18 52 7 10 5
PNT 20 54 3 6 6
PNT 21 56 1 2 4
LIN 21 40 21 52 5
PNT 20 38 3 3 5
C Stand
LIN 18 62 24 62 4
LIN 21 58 21 62 4
C
C --- SHEET MUSIC on wall --- framed
PNT 4 6 12 10 4
PNT 5 7 10 8 5
C Staff lines
LIN 6 8 14 8 4
LIN 6 10 14 10 4
LIN 6 12 14 12 4
C Notes
PNT 7 8 1 2 6
PNT 9 10 1 2 6
PNT 11 8 1 2 6
PNT 13 12 1 2 6
C Frame
LIN 4 6 16 6 6
LIN 4 16 16 16 6
LIN 4 6 4 16 6
LIN 16 6 16 16 6
C
C --- GOLD RECORDS on accent wall ---
PNT 10 22 4 4 3
PNT 11 23 2 2 4
PNT 20 24 4 4 3
PNT 21 25 2 2 4
C
C --- BOOKSHELF with reference books ---
PNT 86 22 20 18 4
LIN 86 30 106 30 5
LIN 86 38 106 38 5
PNT 88 23 2 6 5
PNT 91 23 2 6 6
PNT 94 23 2 6 3
PNT 97 23 2 6 5
PNT 100 23 2 6 4
PNT 88 31 2 6 5
PNT 91 31 2 6 4
PNT 94 31 2 6 6
PNT 97 31 2 6 3
PNT 100 31 2 6 5
C
C Coffee mug on desk
PNT 76 42 3 3 4
PNT 77 42 1 2 5
C
C Phone on desk
PNT 70 42 4 2 4
PNT 71 42 2 1 5
C
REC 8
C
C --- FRAME 12.002: SONGWRITER TYPING ---
PNT 48 44 6 2 5
C
REC 1
C
PNT 48 44 6 2 4
C
REC 1
C
PNT 48 44 6 2 5
C
REC 1
C
PNT 48 44 6 2 4
C
REC 1
C
C --- FRAME 12.003: NEW LYRIC LINE APPEARS ---
LIN 58 38 66 38 3
C
REC 3
C
C --- FRAME 12.004: SONGWRITER HEAD TILT ---
PNT 40 26 8 8 3
PNT 39 27 8 8 4
PNT 40 28 6 6 5
C
REC 3
C
PNT 39 27 8 8 3
PNT 40 26 8 8 4
PNT 41 27 6 6 5
C
REC 3
C
C --- FRAME 12.005: CURSOR BLINK ON SCREEN ---
PNT 68 38 1 1 7
C
REC 2
C
PNT 68 38 1 1 0
C
REC 2
C
PNT 68 38 1 1 7
C
REC 2
C
PNT 68 38 1 1 0
C
REC 2
C
C --- FRAME 12.006: PHONE VIBRATES ---
PNT 70 42 4 2 5
C
REC 1
C
PNT 70 42 4 2 4
C
REC 1
C
PNT 70 42 4 2 5
C
REC 1
C
PNT 70 42 4 2 4
C
REC 2
C
C --- FRAME 12.007: SONGWRITER PICKS UP PHONE ---
LIN 50 40 56 44 4
LIN 50 40 54 36 5
PNT 52 34 4 3 4
C
REC 4
C
C --- FRAME 12.008: PHONE DOWN ---
PNT 52 34 4 3 2
LIN 50 40 54 36 2
LIN 50 40 56 44 5
PNT 70 42 4 2 4
C
REC 3
C
C --- FRAME 12.009: LIGHT SHIFTS THROUGH WINDOW ---
PNT 98 6 22 10 1
C
REC 3
C
PNT 98 6 22 10 0
C
REC 3
C
C --- FRAME 12.010: HOLD ON OFFICE ---
REC 8
C
C --- END OF BATCH 4: SCENES 10-12 ---
C
C ============================================================
C  SCENE 13: INT AI LAB — DAY
C  TRAINING RUNS CONTINUE — the machine learns.
C  Multiple workstations, loss curves on monitors.
C  GPU cluster status displays. The hum of optimization.
C ============================================================
C
C --- FRAME 13.001: BASE AI LAB ---
CLR 0
C Ceiling — modern lab, clean
PNT 0 0 128 8 1
C Track lighting
PNT 16 2 8 3 2
PNT 48 2 8 3 2
PNT 80 2 8 3 2
PNT 112 2 8 3 2
C
C Walls — white/light
PNT 0 8 128 16 1
C
C Whiteboard on wall — covered in equations
PNT 30 10 40 10 0
C Board frame
LIN 30 10 70 10 3
LIN 30 20 70 20 3
LIN 30 10 30 20 3
LIN 70 10 70 20 3
C Equations — scribbled lines
LIN 33 12 45 12 2
LIN 33 14 50 14 2
LIN 35 16 55 16 2
LIN 33 18 42 18 2
LIN 50 12 65 12 2
LIN 48 16 65 16 2
C Greek symbols — dots representing notation
PNT 36 12 1 1 3
PNT 42 14 1 1 3
PNT 52 16 1 1 3
C
C Floor — clean lab floor
PNT 0 58 128 38 2
PNT 0 60 128 2 3
PNT 0 70 128 2 1
PNT 0 80 128 2 3
C
C --- WORKSTATION 1 — left side ---
C Desk
PNT 4 38 28 10 4
PNT 6 40 24 6 5
LIN 4 38 32 38 6
C Desk legs
LIN 8 48 8 56 4
LIN 28 48 28 56 4
C Monitor — large, showing loss curve
PNT 8 22 20 16 1
PNT 10 24 16 12 0
C Loss curve — descending
LIN 12 26 14 28 3
LIN 14 28 16 30 3
LIN 16 30 18 31 3
LIN 18 31 20 32 3
LIN 20 32 22 33 2
LIN 22 33 24 34 2
C Axis labels
LIN 12 26 12 36 2
LIN 12 36 26 36 2
C Epoch markers
PNT 14 36 1 1 3
PNT 18 36 1 1 3
PNT 22 36 1 1 3
C Monitor stand
PNT 16 38 4 2 3
C
C Keyboard
PNT 8 42 14 2 4
C Mouse
PNT 24 42 3 2 4
C
C --- RESEARCHER 1 at workstation ---
PNT 12 32 10 8 4
PNT 14 34 6 4 5
C Head
PNT 14 24 6 8 4
PNT 15 25 4 6 5
C Hair
PNT 15 24 4 2 6
C Glasses
LIN 15 27 17 27 6
LIN 18 27 20 27 6
C Eyes
PNT 16 27 1 1 7
PNT 19 27 1 1 7
C
C --- WORKSTATION 2 — center ---
PNT 44 38 28 10 4
PNT 46 40 24 6 5
LIN 44 38 72 38 6
LIN 48 48 48 56 4
LIN 68 48 68 56 4
C Monitor — GPU utilization
PNT 48 22 20 16 1
PNT 50 24 16 12 0
C GPU bars — utilization meters
PNT 52 26 3 10 4
PNT 56 28 3 8 3
PNT 60 24 3 12 5
PNT 64 26 3 10 4
C Percentage labels
PNT 52 25 3 1 2
PNT 60 23 3 1 2
C Monitor stand
PNT 56 38 4 2 3
C
C --- RESEARCHER 2 at workstation ---
PNT 52 32 10 8 4
PNT 54 34 6 4 5
C Head
PNT 54 24 6 8 4
PNT 55 25 4 6 5
PNT 55 24 4 2 6
PNT 56 27 1 1 7
PNT 59 27 1 1 7
C
C --- WORKSTATION 3 — right ---
PNT 84 38 28 10 4
PNT 86 40 24 6 5
LIN 84 38 112 38 6
LIN 88 48 88 56 4
LIN 108 48 108 56 4
C Monitor — training progress
PNT 88 22 20 16 1
PNT 90 24 16 12 0
C Progress bar
PNT 92 30 12 3 4
PNT 92 30 8 3 5
C Percentage text — line
LIN 92 34 102 34 2
C Timer
LIN 92 27 100 27 2
C Monitor stand
PNT 96 38 4 2 3
C
C --- GPU RACK visible in background ---
PNT 76 10 10 12 4
PNT 78 12 6 8 5
LIN 76 10 86 10 6
LIN 76 22 86 22 6
LIN 76 10 76 22 5
LIN 86 10 86 22 5
C GPU LEDs
PNT 79 14 1 1 3
PNT 79 16 1 1 2
PNT 79 18 1 1 3
PNT 82 14 1 1 2
PNT 82 16 1 1 3
PNT 82 18 1 1 2
C
C --- CABLE MANAGEMENT ---
LIN 32 30 44 30 3
LIN 72 30 84 30 3
LIN 86 22 88 30 3
C
REC 8
C
C --- FRAME 13.002: LOSS CURVE DESCENDS FURTHER ---
LIN 24 34 26 34 2
C
REC 3
C
C --- FRAME 13.003: GPU BARS UPDATE ---
PNT 52 26 3 10 5
PNT 56 28 3 8 4
PNT 60 24 3 12 6
PNT 64 26 3 10 5
C
REC 2
C
PNT 52 26 3 10 4
PNT 56 28 3 8 3
PNT 60 24 3 12 5
PNT 64 26 3 10 4
C
REC 2
C
C --- FRAME 13.004: PROGRESS BAR ADVANCES ---
PNT 92 30 9 3 5
C
REC 3
C
PNT 92 30 10 3 5
C
REC 3
C
C --- FRAME 13.005: RESEARCHER 1 TYPES ---
PNT 8 42 14 2 5
C
REC 1
C
PNT 8 42 14 2 4
C
REC 1
C
PNT 8 42 14 2 5
C
REC 1
C
PNT 8 42 14 2 4
C
REC 1
C
C --- FRAME 13.006: GPU LED BLINK ---
PNT 79 14 1 1 4
PNT 82 16 1 1 4
C
REC 1
C
PNT 79 14 1 1 3
PNT 82 16 1 1 3
C
REC 1
C
PNT 79 16 1 1 4
PNT 82 14 1 1 4
C
REC 1
C
PNT 79 16 1 1 2
PNT 82 14 1 1 2
C
REC 1
C
C --- FRAME 13.007: RESEARCHER 2 HEAD TURN ---
PNT 55 25 4 6 4
PNT 56 25 4 6 5
C
REC 3
C
PNT 56 25 4 6 4
PNT 55 25 4 6 5
C
REC 3
C
C --- FRAME 13.008: WHITEBOARD REFLECTION FLICKER ---
PNT 30 10 40 10 1
C
REC 2
C
PNT 30 10 40 10 0
C
REC 2
C
C --- FRAME 13.009: HOLD ON LAB ---
REC 8
C
C
C ============================================================
C  SCENE 14: INT POLICY FORUM — DAY
C  JOB DISRUPTION CHARTS — future scenarios.
C  A stage with presentation screen, audience seating.
C  Charts predicting economic transformation.
C ============================================================
C
C --- FRAME 14.001: BASE FORUM ---
CLR 0
C Ceiling — conference hall
PNT 0 0 128 6 1
C Stage lighting
PNT 40 2 48 3 2
PNT 46 3 36 1 3
C
C Backdrop wall — dark
PNT 0 6 128 18 2
C
C --- LARGE PROJECTION SCREEN ---
PNT 24 8 80 28 1
PNT 26 10 76 24 0
C Chart — bar graph showing job disruption
C X-axis
LIN 30 32 100 32 3
C Y-axis
LIN 30 12 30 32 3
C Bars — industries affected
PNT 34 22 6 10 4
PNT 42 18 6 14 5
PNT 50 24 6 8 3
PNT 58 14 6 18 6
PNT 66 20 6 12 4
PNT 74 16 6 16 5
PNT 82 26 6 6 3
PNT 90 12 6 20 7
C Bar labels — tick marks
PNT 34 33 6 1 2
PNT 42 33 6 1 2
PNT 50 33 6 1 2
PNT 58 33 6 1 2
PNT 66 33 6 1 2
PNT 74 33 6 1 2
PNT 82 33 6 1 2
PNT 90 33 6 1 2
C Y-axis labels
PNT 28 12 2 1 2
PNT 28 22 2 1 2
PNT 28 32 2 1 2
C
C Stage floor
PNT 0 36 128 14 3
PNT 0 38 128 2 4
PNT 0 44 128 2 2
C
C Podium — left side of stage
PNT 8 30 10 12 5
PNT 10 32 6 8 6
LIN 8 30 18 30 7
C Microphone
LIN 14 28 16 24 5
PNT 16 23 1 2 6
C
C --- SPEAKER at podium ---
PNT 10 22 8 10 4
PNT 12 24 4 6 5
C Head
PNT 12 14 6 8 4
PNT 13 15 4 6 5
PNT 13 14 4 2 6
C Eyes
PNT 14 17 1 1 7
PNT 17 17 1 1 7
C Arm gesturing toward screen
LIN 18 26 26 20 5
PNT 24 18 3 3 4
C
C --- AUDIENCE SEATING ---
C Row 1 — front
PNT 0 52 128 8 3
C Audience figures row 1
PNT 8 50 6 4 4
PNT 18 50 6 4 4
PNT 28 50 6 4 4
PNT 40 50 6 4 4
PNT 52 50 6 4 4
PNT 64 50 6 4 4
PNT 76 50 6 4 4
PNT 88 50 6 4 4
PNT 100 50 6 4 4
PNT 112 50 6 4 4
C Heads row 1
PNT 9 46 4 4 4
PNT 19 46 4 4 4
PNT 29 46 4 4 4
PNT 41 46 4 4 4
PNT 53 46 4 4 4
PNT 65 46 4 4 4
PNT 77 46 4 4 4
PNT 89 46 4 4 4
PNT 101 46 4 4 4
PNT 113 46 4 4 4
C
C Row 2 — middle
PNT 0 62 128 8 3
PNT 6 60 6 4 4
PNT 16 60 6 4 4
PNT 26 60 6 4 4
PNT 38 60 6 4 4
PNT 50 60 6 4 4
PNT 62 60 6 4 4
PNT 74 60 6 4 4
PNT 86 60 6 4 4
PNT 98 60 6 4 4
PNT 110 60 6 4 4
PNT 122 60 6 4 4
C Heads row 2
PNT 7 56 4 4 4
PNT 17 56 4 4 4
PNT 27 56 4 4 4
PNT 39 56 4 4 4
PNT 51 56 4 4 4
PNT 63 56 4 4 4
PNT 75 56 4 4 4
PNT 87 56 4 4 4
PNT 99 56 4 4 4
PNT 111 56 4 4 4
PNT 123 56 4 4 4
C
C Row 3 — back
PNT 0 72 128 8 3
PNT 4 70 6 4 4
PNT 14 70 6 4 4
PNT 24 70 6 4 4
PNT 36 70 6 4 4
PNT 48 70 6 4 4
PNT 60 70 6 4 4
PNT 72 70 6 4 4
PNT 84 70 6 4 4
PNT 96 70 6 4 4
PNT 108 70 6 4 4
PNT 120 70 6 4 4
C
C Aisle — center gap
PNT 60 50 8 30 3
C
C Floor — back
PNT 0 80 128 16 3
PNT 0 82 128 2 4
PNT 0 88 128 2 2
C
REC 8
C
C --- FRAME 14.002: SPEAKER GESTURES ---
PNT 24 18 3 3 2
LIN 18 26 26 20 2
LIN 18 26 30 16 5
PNT 28 14 3 3 4
C
REC 3
C
C --- FRAME 14.003: ARM RETURNS ---
PNT 28 14 3 3 2
LIN 18 26 30 16 2
LIN 18 26 26 20 5
PNT 24 18 3 3 4
C
REC 3
C
C --- FRAME 14.004: CHART BAR ANIMATION — tallest bar pulses ---
PNT 90 12 6 20 6
C
REC 2
C
PNT 90 12 6 20 7
C
REC 2
C
PNT 58 14 6 18 5
C
REC 2
C
PNT 58 14 6 18 6
C
REC 2
C
C --- FRAME 14.005: AUDIENCE MEMBER RAISES HAND ---
PNT 53 46 4 4 5
LIN 55 46 55 40 5
PNT 54 38 2 2 4
C
REC 4
C
C --- FRAME 14.006: HAND LOWERS ---
PNT 54 38 2 4 3
LIN 55 46 55 40 3
PNT 53 46 4 4 4
C
REC 3
C
C --- FRAME 14.007: SPEAKER NOD ---
PNT 12 14 6 8 3
PNT 12 15 6 8 4
PNT 13 16 4 6 5
C
REC 2
C
PNT 12 15 6 8 3
PNT 12 14 6 8 4
PNT 13 15 4 6 5
C
REC 2
C
C --- FRAME 14.008: STAGE LIGHT SHIFT ---
PNT 46 3 36 1 4
C
REC 2
C
PNT 46 3 36 1 3
C
REC 2
C
C --- FRAME 14.009: HOLD ON FORUM ---
REC 8
C
C
C ============================================================
C  SCENE 15: EXT ITALIAN PASTURE — SUNSET
C  CALYPSO MOTIONLESS — return to the horse.
C  The sky burns with golden light.
C  Calypso stands perfectly still.
C  Silhouette against the burning horizon.
C ============================================================
C
C --- FRAME 15.001: BASE SUNSET LANDSCAPE ---
CLR 0
C Sky — dramatic sunset gradient
C Upper sky — deep blue-gray
PNT 0 0 128 12 2
C Mid sky — warm amber
PNT 0 12 128 8 3
C Lower sky — golden
PNT 0 20 128 8 2
C Horizon — intense bright band
PNT 0 28 128 4 1
C Sub-horizon glow
PNT 0 32 128 4 2
C
C Cloud bands — lit from below
PNT 10 6 30 4 3
PNT 14 7 22 2 2
PNT 60 8 40 4 3
PNT 66 9 28 2 2
PNT 110 4 16 4 3
PNT 113 5 10 2 2
C
C Hills — silhouette dark against sunset
PNT 0 30 128 6 4
PNT 10 29 20 4 5
PNT 40 30 30 4 5
PNT 80 29 25 4 5
PNT 110 30 18 4 5
C Hill overlap variations
PNT 25 31 15 3 4
PNT 65 30 20 4 4
C
C Ground plane — darkening grass
PNT 0 36 128 60 4
PNT 0 38 128 2 3
PNT 0 44 128 2 5
PNT 0 50 128 2 3
PNT 0 56 128 2 5
PNT 0 62 128 2 3
PNT 0 68 128 2 5
PNT 0 74 128 2 3
PNT 0 80 128 2 5
C Foreground — very dark
PNT 0 86 128 10 5
PNT 0 90 128 6 6
C
C --- CALYPSO — silhouette against sunset ---
C Body — large dark mass
PNT 44 48 22 12 6
PNT 46 49 18 10 7
PNT 48 50 14 8 6
C Back line
LIN 46 48 64 46 7
C Belly
LIN 44 60 66 60 6
C
C Neck — tall, proud, head up
PNT 42 34 6 16 6
PNT 43 36 4 12 7
C
C Head — looking toward horizon
PNT 38 30 8 5 6
PNT 39 31 6 3 7
C Jaw
LIN 38 35 42 35 6
C Muzzle
PNT 37 32 3 3 5
PNT 38 33 1 1 6
C Eye — catch light from sunset — single bright pixel
PNT 40 32 1 1 3
C Ear — alert, forward
PNT 39 28 2 3 7
PNT 41 28 2 3 7
C Forelock
PNT 40 29 2 2 6
C
C Mane — silhouette along neck
LIN 43 34 45 38 7
LIN 44 36 46 40 6
LIN 45 38 47 42 7
C
C Front legs — standing firm
LIN 48 60 48 78 6
LIN 50 60 50 78 7
LIN 52 60 52 78 6
LIN 54 60 54 78 7
C Hooves — dark blocks
PNT 47 78 2 2 7
PNT 49 78 2 2 7
PNT 51 78 2 2 7
PNT 53 78 2 2 7
C
C Back legs
LIN 58 58 58 78 6
LIN 60 58 60 78 7
LIN 62 58 62 78 6
LIN 64 58 64 78 7
C Back hooves
PNT 57 78 2 2 7
PNT 59 78 2 2 7
PNT 61 78 2 2 7
PNT 63 78 2 2 7
C
C Tail — hanging naturally
LIN 66 46 70 44 6
LIN 70 44 72 46 7
LIN 72 46 74 42 6
LIN 74 42 76 44 7
LIN 76 44 78 40 6
C
C --- Distant fence posts — also silhouetted ---
PNT 8 56 2 18 5
PNT 18 54 2 16 5
PNT 28 52 2 14 5
PNT 98 54 2 16 5
PNT 108 56 2 18 5
PNT 118 58 2 16 5
C Fence wire
LIN 8 62 28 56 5
LIN 98 58 118 64 5
C
REC 10
C
C --- FRAME 15.002: SKY COLOR DEEPENS ---
PNT 0 0 128 12 3
PNT 0 12 128 8 4
C Clouds darken
PNT 10 6 30 4 4
PNT 60 8 40 4 4
PNT 110 4 16 4 4
C
REC 4
C
C --- FRAME 15.003: CALYPSO EYE CATCH-LIGHT ---
PNT 40 32 1 1 2
C
REC 3
C
PNT 40 32 1 1 3
C
REC 3
C
C --- FRAME 15.004: TAIL SWISH — gentle ---
LIN 66 46 70 44 4
LIN 70 44 72 46 4
LIN 66 46 68 42 6
LIN 68 42 70 44 7
C
REC 3
C
C --- FRAME 15.005: TAIL RETURNS ---
LIN 66 46 68 42 4
LIN 68 42 70 44 4
LIN 66 46 70 44 6
LIN 70 44 72 46 7
C
REC 3
C
C --- FRAME 15.006: HORIZON BAND BRIGHTENS ---
PNT 0 28 128 4 0
C
REC 3
C
PNT 0 28 128 4 1
C
REC 3
C
C --- FRAME 15.007: GRASS WIND RIPPLE ---
PNT 0 50 40 2 4
PNT 0 56 40 2 4
C
REC 2
C
PNT 0 50 40 2 5
PNT 40 50 40 2 4
PNT 0 56 40 2 5
PNT 40 56 40 2 4
C
REC 2
C
PNT 40 50 40 2 5
PNT 80 50 48 2 4
PNT 40 56 40 2 5
PNT 80 56 48 2 4
C
REC 2
C
PNT 80 50 48 2 5
PNT 80 56 48 2 5
PNT 0 50 128 2 3
PNT 0 56 128 2 5
C
REC 2
C
C --- FRAME 15.008: SKY CONTINUES DARKENING ---
PNT 0 0 128 12 4
PNT 0 12 128 8 3
PNT 0 20 128 8 3
C Ground darkens
PNT 0 86 128 10 6
PNT 0 90 128 6 7
C
REC 4
C
C --- FRAME 15.009: CALYPSO PERFECTLY STILL — long hold ---
C No movement — pure contemplation
REC 14
C
C --- END OF BATCH 5: SCENES 13-15 ---
C
C ============================================================
C  SCENE 16: EXT MODERN CITY — NIGHT
C  INFRASTRUCTURE MONTAGE — rapid sequence.
C  Railroads, automobiles, airplanes, fiber cables, data centers.
C  Each replaces the last in succession.
C ============================================================
C
C --- FRAME 16.001: RAILROADS ---
CLR 0
C Night sky
PNT 0 0 128 20 1
C Stars
PNT 15 4 1 1 2
PNT 40 8 1 1 2
PNT 70 3 1 1 2
PNT 95 10 1 1 2
PNT 110 6 1 1 2
C
C Ground
PNT 0 50 128 46 3
C Railroad tracks — two parallel lines converging to vanishing point
LIN 0 80 64 50 5
LIN 128 80 64 50 5
C Cross ties
LIN 20 72 108 72 4
LIN 30 68 98 68 4
LIN 38 64 90 64 4
LIN 44 60 84 60 4
LIN 50 56 78 56 4
LIN 56 52 72 52 4
C Rails — bright steel
LIN 10 76 60 50 6
LIN 118 76 68 50 6
C
C Steam locomotive — approaching
PNT 50 30 28 20 5
PNT 52 32 24 16 6
C Smokestack
PNT 54 24 4 8 5
PNT 55 25 2 6 6
C Smoke billowing
PNT 52 18 8 8 4
PNT 54 16 6 6 3
PNT 50 12 10 8 2
PNT 48 8 14 6 1
C Headlight
PNT 62 36 4 4 3
PNT 63 37 2 2 1
C Cowcatcher
PNT 56 50 16 4 4
C Wheels
PNT 54 48 4 4 5
PNT 64 48 4 4 5
PNT 72 48 4 4 5
C
C Telegraph poles along track
LIN 20 30 20 72 4
LIN 18 30 22 30 4
LIN 108 32 108 72 4
LIN 106 32 110 32 4
C Wires
LIN 20 32 108 34 3
C
REC 6
C
C --- FRAME 16.002: SMOKE BILLOWS ---
PNT 48 8 14 6 0
PNT 46 4 18 8 1
PNT 44 2 22 6 1
C
REC 3
C
C --- FRAME 16.003: DISSOLVE TO AUTOMOBILES ---
C Fade locomotive
PNT 50 12 28 40 3
PNT 48 4 22 10 1
C
REC 2
C
C --- FRAME 16.004: AUTOMOBILE HIGHWAY ---
CLR 0
PNT 0 0 128 20 1
PNT 0 40 128 56 3
C Highway — wide asphalt
PNT 20 40 88 40 4
C Lane markings — dashed center line
PNT 60 42 4 4 2
PNT 60 50 4 4 2
PNT 60 58 4 4 2
PNT 60 66 4 4 2
PNT 60 74 4 4 2
C Car 1
PNT 36 52 12 6 5
PNT 38 50 8 4 6
PNT 40 48 4 3 4
C Headlights
PNT 36 56 2 2 3
C Car 2
PNT 74 60 12 6 5
PNT 76 58 8 4 6
PNT 78 56 4 3 4
PNT 86 64 2 2 3
C Streetlights
LIN 16 20 16 50 4
PNT 14 20 4 3 3
PNT 15 20 2 2 4
LIN 112 20 112 50 4
PNT 110 20 4 3 3
PNT 111 20 2 2 4
C
REC 4
C
C --- FRAME 16.005: DISSOLVE TO AIRPLANE ---
CLR 0
PNT 0 0 128 96 1
C Clouds below
PNT 0 70 128 26 2
PNT 10 68 30 6 1
PNT 50 72 40 4 1
PNT 100 70 28 4 1
C Airplane — side profile
PNT 30 30 60 10 4
PNT 32 32 56 6 5
C Fuselage
PNT 34 34 52 2 6
C Nose
PNT 28 34 6 4 4
PNT 26 36 4 2 3
C Cockpit window
PNT 32 32 4 2 3
C Wings
PNT 50 24 20 6 3
PNT 52 26 16 2 4
PNT 50 40 20 6 3
PNT 52 42 16 2 4
C Tail
PNT 84 26 8 8 4
PNT 86 28 4 4 5
PNT 86 22 4 6 3
C Engines
PNT 56 28 4 4 5
PNT 56 42 4 4 5
C Contrail
PNT 92 34 36 2 2
PNT 96 36 32 2 1
C
REC 4
C
C --- FRAME 16.006: DISSOLVE TO FIBER OPTIC CABLE ---
CLR 0
PNT 0 0 128 96 0
C Fiber optic cable — cross-section, centered
C Outer jacket
PNT 34 20 60 56 2
PNT 38 24 52 48 1
C Inner core — bright
PNT 44 30 40 36 3
PNT 48 34 32 28 4
PNT 52 38 24 20 5
PNT 56 42 16 12 6
C Central fiber — brightest
PNT 60 46 8 4 7
C Light pulses — concentric rings
PNT 42 28 44 40 2
PNT 46 32 36 32 3
PNT 50 36 28 24 2
C
REC 4
C
C --- FRAME 16.007: LIGHT PULSE ---
PNT 60 46 8 4 6
PNT 56 42 16 12 7
PNT 52 38 24 20 6
C
REC 2
C
PNT 60 46 8 4 7
PNT 56 42 16 12 6
PNT 52 38 24 20 5
C
REC 2
C
C --- FRAME 16.008: DISSOLVE TO DATA CENTER EXTERIOR ---
CLR 0
C Night sky
PNT 0 0 128 30 0
C Stars
PNT 12 4 1 1 2
PNT 28 8 1 1 1
PNT 44 3 1 1 2
PNT 60 12 1 1 1
PNT 76 6 1 1 2
PNT 92 2 1 1 1
PNT 108 10 1 1 2
C
C Ground
PNT 0 60 128 36 2
C Parking lot
PNT 0 70 128 26 3
C
C Data center building — large rectangular
PNT 20 30 88 30 4
PNT 22 32 84 26 5
C Roof edge
LIN 20 30 108 30 6
C Windows — glowing from inside
PNT 26 36 6 4 3
PNT 36 36 6 4 3
PNT 46 36 6 4 3
PNT 56 36 6 4 3
PNT 66 36 6 4 3
PNT 76 36 6 4 3
PNT 86 36 6 4 3
PNT 96 36 6 4 3
C Second row of windows
PNT 26 44 6 4 3
PNT 36 44 6 4 3
PNT 46 44 6 4 3
PNT 56 44 6 4 3
PNT 66 44 6 4 3
PNT 76 44 6 4 3
PNT 86 44 6 4 3
PNT 96 44 6 4 3
C Entrance — bright doorway
PNT 58 52 12 8 2
PNT 60 54 8 6 1
C
C HVAC units on roof
PNT 30 26 8 4 5
PNT 50 26 8 4 5
PNT 70 26 8 4 5
PNT 90 26 8 4 5
C
C Ambient glow around building
PNT 16 28 96 36 2
C
C Security fence
LIN 14 60 14 72 4
LIN 114 60 114 72 4
LIN 14 64 114 64 3
C
REC 6
C
C --- FRAME 16.009: WINDOWS PULSE ---
PNT 26 36 6 4 4
PNT 46 36 6 4 4
PNT 66 36 6 4 4
PNT 86 36 6 4 4
C
REC 2
C
PNT 26 36 6 4 3
PNT 46 36 6 4 3
PNT 66 36 6 4 3
PNT 86 36 6 4 3
C
REC 2
C
C --- FRAME 16.010: HVAC EXHAUST ---
PNT 32 24 4 2 3
PNT 52 24 4 2 3
PNT 72 24 4 2 3
C
REC 2
C
PNT 32 24 4 2 2
PNT 52 24 4 2 2
PNT 72 24 4 2 2
C
REC 2
C
C --- FRAME 16.011: HOLD ON DATA CENTER ---
REC 6
C
C
C ============================================================
C  SCENE 17: EXT ITALIAN PASTURE — NIGHT
C  THE HORSE REMAINS — after everything.
C  Dark landscape under stars. Horse barely visible.
C  The world has moved on. She hasn't.
C ============================================================
C
C --- FRAME 17.001: BASE NIGHT PASTURE ---
CLR 0
C Night sky — deep black with stars
PNT 0 0 128 28 0
C Stars — many
PNT 8 4 1 1 2
PNT 16 10 1 1 1
PNT 24 6 1 1 2
PNT 32 12 1 1 1
PNT 40 3 1 1 2
PNT 48 8 1 1 1
PNT 56 14 1 1 2
PNT 64 5 1 1 1
PNT 72 10 1 1 2
PNT 80 4 1 1 1
PNT 88 12 1 1 2
PNT 96 7 1 1 1
PNT 104 2 1 1 2
PNT 112 9 1 1 1
PNT 120 6 1 1 2
PNT 12 16 1 1 1
PNT 36 18 1 1 2
PNT 60 20 1 1 1
PNT 84 16 1 1 2
PNT 108 22 1 1 1
C Bright stars
PNT 44 5 2 2 2
PNT 100 8 2 2 2
C
C Moon — crescent
PNT 18 8 4 6 2
PNT 20 8 4 6 0
PNT 18 9 2 4 3
C
C Hills — dark silhouette
PNT 0 26 128 6 1
PNT 10 25 20 4 2
PNT 40 26 30 4 2
PNT 80 25 25 4 2
PNT 110 26 18 4 2
C
C Ground — very dark grass
PNT 0 32 128 64 2
PNT 0 36 128 2 1
PNT 0 44 128 2 3
PNT 0 52 128 2 1
PNT 0 60 128 2 3
PNT 0 68 128 2 1
PNT 0 76 128 2 3
PNT 0 84 128 2 1
C Very dark foreground
PNT 0 88 128 8 3
C
C --- CALYPSO — barely visible in darkness ---
C Body — low contrast, dark
PNT 50 50 18 10 3
PNT 52 51 14 8 4
C Neck
PNT 48 40 4 12 3
PNT 49 42 2 8 4
C Head
PNT 44 36 6 5 3
PNT 45 37 4 3 4
C Eye — faint moonlight catch
PNT 46 38 1 1 2
C Ears
PNT 44 34 2 3 3
PNT 47 34 2 3 3
C
C Legs — dark verticals barely visible
LIN 52 60 52 72 3
LIN 55 60 55 72 3
LIN 62 58 62 72 3
LIN 65 58 65 72 3
C
C Tail
LIN 68 50 72 48 3
LIN 72 48 74 50 2
C
C Moonlight on horse's back
PNT 50 49 16 2 3
C
C --- DISTANT DATA CENTER GLOW on horizon ---
PNT 100 24 16 6 2
PNT 102 25 12 4 1
PNT 104 26 8 2 2
C
REC 10
C
C --- FRAME 17.002: STAR TWINKLE ---
PNT 44 5 2 2 3
PNT 100 8 2 2 3
PNT 8 4 1 1 3
PNT 72 10 1 1 3
C
REC 2
C
PNT 44 5 2 2 2
PNT 100 8 2 2 2
PNT 8 4 1 1 2
PNT 72 10 1 1 2
C
REC 2
C
C --- FRAME 17.003: DIFFERENT STARS TWINKLE ---
PNT 24 6 1 1 3
PNT 56 14 1 1 3
PNT 88 12 1 1 3
PNT 120 6 1 1 3
C
REC 2
C
PNT 24 6 1 1 2
PNT 56 14 1 1 2
PNT 88 12 1 1 2
PNT 120 6 1 1 2
C
REC 2
C
C --- FRAME 17.004: CALYPSO EAR TWITCH ---
PNT 44 34 2 3 2
PNT 44 33 2 3 3
C
REC 2
C
PNT 44 33 2 3 2
PNT 44 34 2 3 3
C
REC 2
C
C --- FRAME 17.005: MOONLIGHT SHIFTS ON BACK ---
PNT 50 49 16 2 2
C
REC 3
C
PNT 50 49 16 2 3
C
REC 3
C
C --- FRAME 17.006: DATA CENTER GLOW PULSES ---
PNT 100 24 16 6 3
PNT 102 25 12 4 2
C
REC 3
C
PNT 100 24 16 6 2
PNT 102 25 12 4 1
C
REC 3
C
C --- FRAME 17.007: HOLD — the horse remains ---
REC 14
C
C
C ============================================================
C  SCENE 18: INT FUTURE DATA CENTER — UNKNOWN TIME
C  AI INVISIBLE — no headlines, no prophets.
C  Sterile, clean, automated. No humans present.
C  The hum of systems that have become ordinary.
C ============================================================
C
C --- FRAME 18.001: BASE AUTOMATED CENTER ---
CLR 0
C Clean ceiling — white
PNT 0 0 128 4 1
C Recessed lighting — even, clinical
PNT 0 4 128 2 2
C
C Walls — white/sterile
PNT 0 6 128 14 1
C
C Floor — polished, reflective
PNT 0 74 128 22 2
PNT 0 76 128 2 1
PNT 0 82 128 2 3
PNT 0 88 128 2 1
C
C --- AUTOMATED SERVER PODS — futuristic design ---
C Pod 1
PNT 6 12 16 62 3
PNT 8 14 12 58 4
PNT 10 16 8 54 3
C Pod frame
LIN 6 12 22 12 5
LIN 6 74 22 74 5
LIN 6 12 6 74 4
LIN 22 12 22 74 4
C Status lights — steady, uniform
PNT 18 18 2 2 2
PNT 18 26 2 2 2
PNT 18 34 2 2 2
PNT 18 42 2 2 2
PNT 18 50 2 2 2
PNT 18 58 2 2 2
PNT 18 66 2 2 2
C
C Pod 2
PNT 28 12 16 62 3
PNT 30 14 12 58 4
PNT 32 16 8 54 3
LIN 28 12 44 12 5
LIN 28 74 44 74 5
LIN 28 12 28 74 4
LIN 44 12 44 74 4
PNT 40 18 2 2 2
PNT 40 26 2 2 2
PNT 40 34 2 2 2
PNT 40 42 2 2 2
PNT 40 50 2 2 2
PNT 40 58 2 2 2
PNT 40 66 2 2 2
C
C Pod 3
PNT 50 12 16 62 3
PNT 52 14 12 58 4
PNT 54 16 8 54 3
LIN 50 12 66 12 5
LIN 50 74 66 74 5
LIN 50 12 50 74 4
LIN 66 12 66 74 4
PNT 62 18 2 2 2
PNT 62 26 2 2 2
PNT 62 34 2 2 2
PNT 62 42 2 2 2
PNT 62 50 2 2 2
PNT 62 58 2 2 2
PNT 62 66 2 2 2
C
C Pod 4
PNT 72 12 16 62 3
PNT 74 14 12 58 4
PNT 76 16 8 54 3
LIN 72 12 88 12 5
LIN 72 74 88 74 5
LIN 72 12 72 74 4
LIN 88 12 88 74 4
PNT 84 18 2 2 2
PNT 84 26 2 2 2
PNT 84 34 2 2 2
PNT 84 42 2 2 2
PNT 84 50 2 2 2
PNT 84 58 2 2 2
PNT 84 66 2 2 2
C
C Pod 5
PNT 94 12 16 62 3
PNT 96 14 12 58 4
PNT 98 16 8 54 3
LIN 94 12 110 12 5
LIN 94 74 110 74 5
LIN 94 12 94 74 4
LIN 110 12 110 74 4
PNT 106 18 2 2 2
PNT 106 26 2 2 2
PNT 106 34 2 2 2
PNT 106 42 2 2 2
PNT 106 50 2 2 2
PNT 106 58 2 2 2
PNT 106 66 2 2 2
C
C --- NO HUMANS — empty floor ---
C Robot arm — small maintenance unit
PNT 116 60 6 8 4
PNT 118 62 2 4 5
LIN 118 60 122 54 4
LIN 122 54 124 50 4
PNT 123 48 3 3 3
C
C Floor reflection of pods
PNT 6 76 16 4 2
PNT 28 76 16 4 2
PNT 50 76 16 4 2
PNT 72 76 16 4 2
PNT 94 76 16 4 2
C
REC 8
C
C --- FRAME 18.002: STATUS LIGHTS CYCLE --- uniform pulse ---
PNT 18 18 2 2 3
PNT 40 26 2 2 3
PNT 62 34 2 2 3
PNT 84 42 2 2 3
PNT 106 50 2 2 3
C
REC 1
C
PNT 18 18 2 2 2
PNT 40 26 2 2 2
PNT 62 34 2 2 2
PNT 84 42 2 2 2
PNT 106 50 2 2 2
C Next wave
PNT 18 26 2 2 3
PNT 40 34 2 2 3
PNT 62 42 2 2 3
PNT 84 50 2 2 3
PNT 106 58 2 2 3
C
REC 1
C
PNT 18 26 2 2 2
PNT 40 34 2 2 2
PNT 62 42 2 2 2
PNT 84 50 2 2 2
PNT 106 58 2 2 2
C
REC 1
C
C --- FRAME 18.003: ROBOT ARM ADJUSTS ---
LIN 118 60 122 54 3
LIN 122 54 124 50 3
LIN 118 60 120 52 4
LIN 120 52 122 48 4
PNT 121 46 3 3 3
C
REC 3
C
C --- FRAME 18.004: ROBOT ARM RETURNS ---
PNT 121 46 3 3 1
LIN 118 60 120 52 1
LIN 120 52 122 48 1
LIN 118 60 122 54 4
LIN 122 54 124 50 4
PNT 123 48 3 3 3
C
REC 3
C
C --- FRAME 18.005: UNIFORM LIGHT PULSE — all pods ---
PNT 18 42 2 2 3
PNT 40 42 2 2 3
PNT 62 42 2 2 3
PNT 84 42 2 2 3
PNT 106 42 2 2 3
C
REC 2
C
PNT 18 42 2 2 2
PNT 40 42 2 2 2
PNT 62 42 2 2 2
PNT 84 42 2 2 2
PNT 106 42 2 2 2
C
REC 2
C
C --- FRAME 18.006: HOLD — sterile silence ---
REC 10
C
C --- END OF BATCH 6: SCENES 16-18 ---
C
C ============================================================
C  SCENE 19: EXT ITALIAN PASTURE — MORNING
C  CALYPSO LOOKS UP — the horse acknowledges nothing.
C  Dawn light. Fresh grass. Mist clinging to ground.
C  She lifts her head briefly. Then returns to eating.
C ============================================================
C
C --- FRAME 19.001: BASE DAWN LANDSCAPE ---
CLR 0
C Sky — early morning gradient
C Upper — still deep
PNT 0 0 128 10 2
C Mid sky — lavender-blue
PNT 0 10 128 8 1
C Lower sky — warm dawn light
PNT 0 18 128 8 2
C Horizon — bright band
PNT 0 26 128 4 1
C Just above horizon — golden
PNT 0 24 128 4 2
C
C Dawn clouds — pink-lit wisps
PNT 20 6 24 4 3
PNT 24 7 16 2 2
PNT 60 4 30 4 3
PNT 66 5 18 2 2
PNT 100 8 22 4 3
PNT 104 9 14 2 2
C
C Hills — soft morning light
PNT 0 28 128 6 3
PNT 10 27 20 4 2
PNT 40 28 30 4 3
PNT 80 27 25 4 2
PNT 110 28 18 4 3
C
C Ground — fresh morning grass
PNT 0 34 128 62 3
PNT 0 36 128 2 2
PNT 0 42 128 2 4
PNT 0 48 128 2 2
PNT 0 54 128 2 4
PNT 0 60 128 2 2
PNT 0 66 128 2 4
PNT 0 72 128 2 2
PNT 0 78 128 2 4
C
C Morning mist — soft bands at ground level
PNT 0 82 128 6 2
PNT 10 84 30 4 1
PNT 50 82 40 4 1
PNT 100 84 20 4 1
C
C Foreground
PNT 0 88 128 8 4
C
C Dew highlights on grass — bright dots
PNT 20 44 1 1 1
PNT 35 50 1 1 1
PNT 55 46 1 1 1
PNT 70 52 1 1 1
PNT 90 48 1 1 1
PNT 105 54 1 1 1
PNT 30 60 1 1 1
PNT 65 58 1 1 1
PNT 85 62 1 1 1
PNT 110 56 1 1 1
C
C --- CALYPSO — morning position, head down grazing ---
C Body
PNT 40 50 20 10 5
PNT 42 51 16 8 6
C Back line
LIN 42 50 58 48 6
C Belly
LIN 40 60 60 60 5
C
C Neck — angled down toward grass
PNT 38 48 4 10 5
PNT 39 50 2 8 6
C Neck stretching down further
PNT 36 56 4 6 5
C
C Head — grazing position, near ground
PNT 32 60 8 4 5
PNT 33 61 6 2 6
C Muzzle in grass
PNT 31 63 4 2 4
C Eye
PNT 34 61 1 1 7
C Ears — relaxed
PNT 32 58 2 3 6
PNT 35 58 2 3 6
C
C Mane — draped along neck
LIN 39 48 40 52 5
LIN 40 50 41 54 6
C
C Front legs
LIN 44 60 44 76 5
LIN 46 60 46 76 6
LIN 50 60 50 76 5
LIN 52 60 52 76 6
C Hooves
PNT 43 76 2 2 6
PNT 45 76 2 2 6
PNT 49 76 2 2 6
PNT 51 76 2 2 6
C
C Back legs
LIN 56 58 56 76 5
LIN 58 58 58 76 6
LIN 62 58 62 76 5
C Back hooves
PNT 55 76 2 2 6
PNT 57 76 2 2 6
PNT 61 76 2 2 6
C
C Tail — relaxed hang
LIN 60 48 64 46 5
LIN 64 46 66 48 4
LIN 66 48 68 44 5
C
C Horse shadow on morning grass
PNT 38 76 28 3 4
C
C --- DARIO figure — distant, walking toward fence ---
PNT 96 52 6 12 4
PNT 98 54 2 8 5
C Head
PNT 98 46 2 6 4
PNT 98 47 2 4 5
C Arm swinging
LIN 96 56 94 62 4
C Legs — walking
LIN 98 64 96 72 4
LIN 100 64 102 72 4
C
C Fence posts — right side
PNT 110 52 2 16 5
PNT 120 50 2 14 5
C Fence wire
LIN 110 58 120 54 4
LIN 110 62 120 58 4
C
REC 8
C
C --- FRAME 19.002: CALYPSO CHEWING ---
C Jaw movement
PNT 31 63 4 2 3
PNT 31 64 4 2 4
C
REC 2
C
PNT 31 64 4 2 3
PNT 31 63 4 2 4
C
REC 2
C
PNT 31 63 4 2 3
PNT 31 64 4 2 4
C
REC 2
C
PNT 31 64 4 2 3
PNT 31 63 4 2 4
C
REC 2
C
C --- FRAME 19.003: CALYPSO LIFTS HEAD — looks up briefly ---
C Erase grazing head position
PNT 32 58 8 8 3
PNT 36 52 4 8 3
C Redraw neck upright
PNT 38 38 4 14 5
PNT 39 40 2 10 6
C Head — raised, alert
PNT 34 32 8 6 5
PNT 35 33 6 4 6
C Eye — wide
PNT 37 34 2 2 7
PNT 38 35 1 1 0
C Ears — pricked forward
PNT 35 30 2 3 7
PNT 38 30 2 3 7
C Forelock
PNT 36 31 2 2 6
C Muzzle
PNT 33 36 3 2 5
PNT 33 37 1 1 6
C
C Restore grass where head was
PNT 31 60 6 6 3
C
REC 6
C
C --- FRAME 19.004: CALYPSO EAR ROTATION WHILE ALERT ---
PNT 35 30 2 3 6
PNT 34 29 2 3 7
C
REC 2
C
PNT 34 29 2 3 6
PNT 35 30 2 3 7
C
REC 2
C
C --- FRAME 19.005: DAWN LIGHT BRIGHTENS ---
PNT 0 24 128 4 1
PNT 0 18 128 6 1
C Cloud catches light
PNT 24 7 16 2 1
PNT 66 5 18 2 1
C
REC 3
C
C --- FRAME 19.006: CALYPSO BLINKS ---
PNT 37 34 2 2 5
C
REC 1
C
PNT 37 34 2 2 7
PNT 38 35 1 1 0
C
REC 2
C
C --- FRAME 19.007: CALYPSO HEAD BEGINS TO LOWER ---
C Intermediate position — head halfway down
PNT 34 32 8 6 3
PNT 34 29 4 4 3
C Neck adjusts
PNT 38 38 4 14 3
PNT 38 42 4 12 5
PNT 39 44 2 8 6
C Head mid-height
PNT 34 44 8 5 5
PNT 35 45 6 3 6
PNT 37 46 1 1 7
PNT 35 42 2 3 6
PNT 38 42 2 3 6
C
REC 3
C
C --- FRAME 19.008: HEAD RETURNS TO GRAZING ---
PNT 34 42 8 8 3
C Neck fully down
PNT 38 42 4 12 3
PNT 38 48 4 10 5
PNT 39 50 2 8 6
PNT 36 56 4 6 5
C Head at grass
PNT 32 60 8 4 5
PNT 33 61 6 2 6
PNT 31 63 4 2 4
PNT 34 61 1 1 7
PNT 32 58 2 3 6
PNT 35 58 2 3 6
C
REC 4
C
C --- FRAME 19.009: MIST SHIFTS ---
PNT 10 84 30 4 0
PNT 15 83 25 4 1
PNT 50 82 40 4 0
PNT 55 83 35 4 1
C
REC 3
C
PNT 15 83 25 4 0
PNT 10 84 30 4 1
PNT 55 83 35 4 0
PNT 50 82 40 4 1
C
REC 3
C
C --- FRAME 19.010: DEW SPARKLE ---
PNT 20 44 1 1 0
PNT 55 46 1 1 0
PNT 90 48 1 1 0
C
REC 2
C
PNT 20 44 1 1 1
PNT 55 46 1 1 1
PNT 90 48 1 1 1
C
REC 2
C
C --- FRAME 19.011: DARIO CONTINUES WALKING ---
C Shift figure slightly left
PNT 96 46 8 28 3
PNT 94 52 6 12 4
PNT 96 54 2 8 5
PNT 96 46 2 6 4
PNT 96 47 2 4 5
LIN 94 56 92 62 4
LIN 96 64 94 72 4
LIN 98 64 100 72 4
C
REC 4
C
C --- FRAME 19.012: TAIL GENTLE SWISH ---
LIN 60 48 64 46 4
LIN 60 48 62 44 5
LIN 62 44 64 46 4
C
REC 2
C
LIN 60 48 62 44 4
LIN 60 48 64 46 5
LIN 64 46 66 48 4
C
REC 2
C
C --- FRAME 19.013: CLOUD DRIFT ---
PNT 20 6 24 4 2
PNT 22 6 24 4 3
PNT 26 7 16 2 2
PNT 60 4 30 4 2
PNT 62 4 30 4 3
PNT 68 5 18 2 2
C
REC 3
C
C --- FRAME 19.014: CALYPSO CHEWS CONTENTEDLY ---
PNT 31 63 4 2 3
PNT 31 64 4 2 4
C
REC 2
C
PNT 31 64 4 2 3
PNT 31 63 4 2 4
C
REC 2
C
C --- FRAME 19.015: HOLD — morning continues ---
REC 10
C
C
C ============================================================
C  SCENE 20: FINAL IMAGE — NIGHT
C  CONSTELLATION AND HORSE
C  A distant data center glows on the horizon.
C  A constellation built by humans.
C  Closer, barely visible, a horse sleeps in the grass.
C  Neither master. Nor servant. Only present.
C ============================================================
C
C --- FRAME 20.001: BASE FINAL COMPOSITION ---
CLR 0
C Night sky — deep black
PNT 0 0 128 36 0
C
C Stars — the full canopy
PNT 6 3 1 1 2
PNT 14 8 1 1 1
PNT 22 5 1 1 2
PNT 30 10 1 1 1
PNT 38 2 1 1 2
PNT 46 7 1 1 1
PNT 54 12 1 1 2
PNT 62 4 1 1 1
PNT 70 9 1 1 2
PNT 78 3 1 1 1
PNT 86 11 1 1 2
PNT 94 6 1 1 1
PNT 102 1 1 1 2
PNT 110 8 1 1 1
PNT 118 5 1 1 2
PNT 126 10 1 1 1
PNT 10 14 1 1 1
PNT 26 16 1 1 2
PNT 42 18 1 1 1
PNT 58 20 1 1 2
PNT 74 14 1 1 1
PNT 90 22 1 1 2
PNT 106 16 1 1 1
PNT 122 24 1 1 2
PNT 18 22 1 1 1
PNT 34 26 1 1 2
PNT 50 24 1 1 1
PNT 66 28 1 1 2
PNT 82 20 1 1 1
PNT 98 30 1 1 2
PNT 114 26 1 1 1
C
C Bright stars — forming partial constellation
PNT 20 6 2 2 3
PNT 36 10 2 2 3
PNT 52 4 2 2 3
PNT 68 8 2 2 3
PNT 84 6 2 2 3
C Constellation lines — faint connections
LIN 21 7 37 11 1
LIN 37 11 53 5 1
LIN 53 5 69 9 1
LIN 69 9 85 7 1
C
C Milky Way suggestion — faint band
PNT 0 12 128 4 1
PNT 20 13 88 2 1
C
C --- GROUND — very dark ---
PNT 0 36 128 60 1
PNT 0 38 128 2 2
PNT 0 46 128 2 0
PNT 0 54 128 2 2
PNT 0 62 128 2 0
PNT 0 70 128 2 2
PNT 0 78 128 2 0
PNT 0 86 128 2 2
C Very dark foreground
PNT 0 88 128 8 2
C
C --- DATA CENTER GLOW on far horizon — right side ---
C The "constellation built by humans"
PNT 92 30 24 8 2
PNT 94 31 20 6 1
PNT 96 32 16 4 2
PNT 98 33 12 2 1
C Building silhouette barely visible
PNT 96 34 14 4 2
PNT 98 35 10 3 3
C Window dots — faint
PNT 100 35 1 1 2
PNT 103 35 1 1 2
PNT 106 35 1 1 2
C Ambient glow cast on nearby ground
PNT 88 36 32 6 1
C
C --- CALYPSO SLEEPING — barely visible shape in grass ---
C Body — lying down, low profile
PNT 24 68 22 8 2
PNT 26 69 18 6 3
PNT 28 70 14 4 2
C
C Neck — extended on ground
PNT 22 66 6 4 2
PNT 23 67 4 2 3
C
C Head — resting on grass
PNT 18 66 6 4 2
PNT 19 67 4 2 3
C Ear — folded
PNT 18 64 2 2 2
C Eye — closed, single dark point
PNT 21 67 1 1 3
C
C Legs — folded under body
PNT 26 76 4 2 2
PNT 32 76 4 2 2
PNT 40 76 4 2 2
C
C Tail — curled behind
PNT 46 70 4 4 2
PNT 47 71 2 2 3
C
C Moonlight on body — faintest highlight
PNT 26 68 18 2 2
C
C Breath — tiny cloud near muzzle
PNT 16 66 3 2 1
C
REC 12
C
C --- FRAME 20.002: STAR TWINKLE CYCLE 1 ---
PNT 20 6 2 2 2
PNT 52 4 2 2 2
PNT 84 6 2 2 2
C
REC 2
C
PNT 20 6 2 2 3
PNT 52 4 2 2 3
PNT 84 6 2 2 3
C
REC 2
C
C --- FRAME 20.003: DIFFERENT STARS TWINKLE ---
PNT 36 10 2 2 2
PNT 68 8 2 2 2
C Small stars
PNT 14 8 1 1 2
PNT 46 7 1 1 2
PNT 94 6 1 1 2
C
REC 2
C
PNT 36 10 2 2 3
PNT 68 8 2 2 3
PNT 14 8 1 1 1
PNT 46 7 1 1 1
PNT 94 6 1 1 1
C
REC 2
C
C --- FRAME 20.004: DATA CENTER GLOW PULSES — the machine breathes ---
PNT 92 30 24 8 3
PNT 94 31 20 6 2
PNT 96 32 16 4 3
C
REC 3
C
PNT 92 30 24 8 2
PNT 94 31 20 6 1
PNT 96 32 16 4 2
C
REC 3
C
C --- FRAME 20.005: HORSE BREATH — cloud appears ---
PNT 16 66 3 2 2
C
REC 3
C
PNT 16 66 3 2 1
C
REC 3
C
C --- FRAME 20.006: SECOND BREATH ---
PNT 14 64 4 3 1
PNT 15 65 2 2 2
C
REC 3
C
PNT 14 64 4 3 0
PNT 15 65 2 2 1
C
REC 3
C
C --- FRAME 20.007: CONSTELLATION LINES BRIGHTEN ---
LIN 21 7 37 11 2
LIN 37 11 53 5 2
LIN 53 5 69 9 2
LIN 69 9 85 7 2
C
REC 3
C
LIN 21 7 37 11 1
LIN 37 11 53 5 1
LIN 53 5 69 9 1
LIN 69 9 85 7 1
C
REC 3
C
C --- FRAME 20.008: DATA CENTER WINDOWS FLICKER ---
PNT 100 35 1 1 3
PNT 103 35 1 1 3
PNT 106 35 1 1 3
C
REC 2
C
PNT 100 35 1 1 2
PNT 103 35 1 1 2
PNT 106 35 1 1 2
C
REC 2
C
C --- FRAME 20.009: HORSE EAR TWITCHES IN SLEEP ---
PNT 18 64 2 2 3
C
REC 2
C
PNT 18 64 2 2 2
C
REC 2
C
C --- FRAME 20.010: THIRD BREATH ---
PNT 16 66 3 2 2
PNT 14 64 3 2 1
C
REC 3
C
PNT 16 66 3 2 1
PNT 14 64 3 2 0
C
REC 3
C
C --- FRAME 20.011: VERY LONG HOLD — let it breathe ---
C Neither master. Nor servant. Only present.
REC 20
C
C --- FRAME 20.012: SLOW FADE — all values decrease ---
C Sky stays black — ground fades
PNT 0 36 128 60 0
PNT 92 30 24 8 1
PNT 94 31 20 6 0
PNT 24 68 22 8 1
PNT 26 69 18 6 2
C Stars remain
C
REC 6
C
C --- FRAME 20.013: DEEPER FADE ---
PNT 26 69 18 6 1
PNT 92 30 24 8 0
C Stars begin to dim
PNT 20 6 2 2 2
PNT 36 10 2 2 2
PNT 52 4 2 2 2
PNT 68 8 2 2 2
PNT 84 6 2 2 2
C
REC 6
C
C --- FRAME 20.014: NEAR BLACK ---
PNT 26 69 18 6 0
PNT 20 6 2 2 1
PNT 36 10 2 2 1
PNT 52 4 2 2 1
PNT 68 8 2 2 1
PNT 84 6 2 2 1
C
REC 6
C
C --- FRAME 20.015: BLACK ---
CLR 0
C
REC 8
C
C --- FRAME 20.016: TITLE CARD ---
C Title text represented as horizontal lines — centered
C "THE DANGER IS NOT THAT MACHINES BECOME HORSES"
LIN 16 40 112 40 3
LIN 20 42 108 42 3
C blank line
C "THE DANGER IS THAT HORSES BECOME MACHINES"
LIN 20 46 108 46 3
LIN 24 48 104 48 3
C
REC 12
C
C --- FRAME 20.017: TITLE FADES ---
LIN 16 40 112 40 2
LIN 20 42 108 42 2
LIN 20 46 108 46 2
LIN 24 48 104 48 2
C
REC 4
C
LIN 16 40 112 40 1
LIN 20 42 108 42 1
LIN 20 46 108 46 1
LIN 24 48 104 48 1
C
REC 4
C
CLR 0
C
REC 6
C
C --- FRAME 20.018: FINAL SOUND CARD ---
C A single sound: a slow breath.
C Represented as a tiny pulse at center
PNT 62 46 4 4 1
C
REC 4
C
PNT 62 46 4 4 2
C
REC 4
C
PNT 62 46 4 4 1
C
REC 4
C
PNT 62 46 4 4 0
C
REC 4
C
C Then nothing.
CLR 0
C
REC 12
C
C ============================================================
C  END OF FILM: SHE'S JUST A HAPPY HORSE
C  20 SCENES / 128x96 / 8 GRAYSCALE / BEFLIX NOTATION
C  TOTAL ANIMATION: ~380 FRAMES AT VARIABLE HOLD DURATIONS
C ============================================================
