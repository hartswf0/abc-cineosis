C ============================================================
C  SHE'S JUST A HAPPY HORSE — hh4.md
C  SOURCE: hhs4.md (JSON 3-act structure)
C  128x96 / 8 GRAYSCALE / BEFLIX
C
C  RENDERING STYLE: SHADOW PUPPET / WAYANG
C  ----------------------------------------
C  Flat profile silhouettes against a luminous screen.
C  Background = glowing value 3 (the shadow screen).
C  All figures = value 0 (pure black shadow).
C  Articulated joints — limbs move independently.
C  Figures slide LEFT/RIGHT like Javanese puppets.
C  No depth. Pure lateral motion. Profile view ONLY.
C  Thin rods (value 1) connect puppet master to figure.
C
C  3 ACTS FROM HHS4 JSON:
C  ACT I   — Introduction: Calypso + Amodei silhouettes
C  ACT II  — Conflict: Courtroom + data silhouettes
C  ACT III — Resolution: horse as infrastructure
C ============================================================
C
C
C ============================================================
C  ACT I: INTRODUCTION — THE SHADOW SCREEN LIGHTS UP
C  Calypso and Dario as flat profile puppets.
C  The puppet screen is value 3 (warm glow).
C  Frame border = value 1 (the puppet stage).
C ============================================================
C
C --- FRAME I.001: STAGE SETUP ---
CLR 0
C --- PUPPET SCREEN — glowing center ---
PNT 8 8 112 72 3
PNT 10 10 108 68 2
C Border frame — dark wood
PNT 0 0 128 8 1
PNT 0 80 128 16 1
PNT 0 0 8 96 1
PNT 120 0 8 96 1
C Stage decorations — ornamental corners
PNT 8 8 4 4 1
PNT 116 8 4 4 1
PNT 8 76 4 4 1
PNT 116 76 4 4 1
C
C Bottom — puppet master area — pure black
PNT 0 84 128 12 0
C Control rods — thin value 1 lines
LIN 36 78 36 90 1
LIN 80 78 80 90 1
C
REC 6
C
C --- FRAME I.002: CALYPSO PUPPET ENTERS — slides from left ---
C Horse — profile silhouette — VALUE 0 on screen
C Body — flat profile
PNT 14 40 20 12 0
C Neck — angled up
PNT 12 30 4 12 0
C Head — profile, left-facing
PNT 8 28 6 6 0
C Eye cutout — value 3 (light through hole)
PNT 11 30 2 2 3
C Ear — triangular
PNT 8 26 2 3 0
C Muzzle
PNT 6 32 3 2 0
C
C Front leg
PNT 18 52 2 16 0
PNT 22 52 2 16 0
C Back leg
PNT 28 50 2 16 0
PNT 32 50 2 16 0
C Hooves — flat bottom
PNT 17 68 4 2 0
PNT 21 68 4 2 0
PNT 27 68 4 2 0
PNT 31 68 4 2 0
C
C Tail — flat profile curve
PNT 34 40 2 4 0
PNT 36 38 2 4 0
PNT 38 36 2 4 0
C
C Mane — jagged silhouette edge
PNT 12 28 2 4 0
PNT 14 26 2 4 0
PNT 16 28 2 4 0
C
C Control rod — from horse body down
LIN 24 52 24 90 1
C
REC 6
C
C --- FRAME I.003: DARIO PUPPET ENTERS — slides from right ---
C Human profile — flat silhouette
C Body
PNT 92 34 10 20 0
C Head — profile
PNT 92 22 8 12 0
C Eye cutout
PNT 94 26 2 2 3
C Nose — profile bump
PNT 90 28 2 3 0
C Hair
PNT 94 20 6 4 0
C
C Arm — reaching toward horse
PNT 88 38 4 4 0
PNT 86 36 4 4 0
C
C Legs — standing profile
PNT 94 54 2 16 0
PNT 98 54 2 16 0
C Shoes
PNT 93 70 4 2 0
PNT 97 70 4 2 0
C
C Control rod
LIN 96 54 96 90 1
C
REC 6
C
C --- FRAME I.004: CALYPSO WALKS TOWARD CENTER ---
C Erase old position
PNT 6 26 32 46 3
PNT 10 26 28 42 2
C Control rod erase
LIN 24 52 24 90 0
PNT 24 84 1 8 0
C
C New position — shifted right 16px
PNT 30 40 20 12 0
PNT 28 30 4 12 0
PNT 24 28 6 6 0
PNT 27 30 2 2 3
PNT 24 26 2 3 0
PNT 22 32 3 2 0
C Front legs
PNT 34 52 2 16 0
PNT 38 52 2 16 0
C Back legs
PNT 44 50 2 16 0
PNT 48 50 2 16 0
C Hooves
PNT 33 68 4 2 0
PNT 37 68 4 2 0
PNT 43 68 4 2 0
PNT 47 68 4 2 0
C Tail
PNT 50 40 2 4 0
PNT 52 38 2 4 0
PNT 54 36 2 4 0
C Mane
PNT 28 28 2 4 0
PNT 30 26 2 4 0
PNT 32 28 2 4 0
C Rod
LIN 40 52 40 90 1
C
C Front leg walk — one lifts
PNT 34 52 2 16 1
PNT 34 50 2 10 0
LIN 34 60 32 64 0
PNT 31 64 4 2 0
C
REC 3
C
C --- FRAME I.005: WALK COMPLETE — leg down ---
PNT 31 60 6 10 3
PNT 32 62 4 8 2
PNT 34 52 2 16 0
PNT 33 68 4 2 0
C
REC 3
C
C --- FRAME I.006: DARIO ARM RAISES — greeting ---
PNT 86 36 4 4 3
PNT 87 37 2 2 2
C Arm up — profile
PNT 88 30 4 4 0
PNT 86 26 4 4 0
C Hand open — flat profile
PNT 84 24 3 3 0
PNT 84 24 1 1 3
C
REC 4
C
C --- FRAME I.007: ARM LOWERS ---
PNT 84 24 4 8 3
PNT 85 25 2 6 2
PNT 88 38 4 4 0
PNT 86 36 4 4 0
C
REC 4
C
C --- FRAME I.008: HEAD NOD — Dario ---
PNT 92 22 8 12 3
PNT 92 20 8 12 2
PNT 92 24 8 12 0
PNT 94 28 2 2 3
C
REC 2
C
PNT 92 24 8 12 3
PNT 92 22 8 12 2
PNT 92 22 8 12 0
PNT 94 26 2 2 3
C
REC 3
C
C --- FRAME I.009: CALYPSO EAR FLICK ---
PNT 24 26 2 3 3
PNT 24 25 2 3 2
PNT 22 24 2 3 0
C
REC 2
C
PNT 22 24 2 3 3
PNT 22 25 2 2 2
PNT 24 26 2 3 0
C
REC 2
C
C --- FRAME I.010: HOLD — two puppets in tableau ---
REC 10
C
C
C ============================================================
C  ACT II: CONFLICT — COURTROOM PUPPETS
C  Books stack on one side. Laptops on other.
C  Judge puppet descends from above.
C  All flat profile silhouettes.
C ============================================================
C
C --- FRAME II.001: CLEAR — new scene on same screen ---
C Erase figures
PNT 10 10 108 68 2
PNT 12 12 104 64 3
C New rods
LIN 32 78 32 90 1
LIN 64 78 64 90 1
LIN 96 78 96 90 1
C
REC 4
C
C --- FRAME II.002: JUDGE DESCENDS FROM ABOVE ---
C Judge — profile silhouette — enters from top
PNT 56 10 16 8 0
PNT 58 8 12 4 0
C Eyes
PNT 60 10 2 2 3
C Robe — wide
PNT 52 18 24 10 0
C Gavel in hand
PNT 50 14 4 6 0
PNT 49 13 2 2 0
C Rod
LIN 64 28 64 90 1
C
REC 4
C
C --- FRAME II.003: BOOK STACK — slides in left ---
PNT 14 46 8 20 0
PNT 16 44 4 4 0
PNT 14 42 6 4 0
PNT 16 40 4 4 0
C Individual book lines — light through gaps
PNT 14 48 8 1 3
PNT 14 52 8 1 3
PNT 14 56 8 1 3
PNT 14 60 8 1 3
C
C WRITER puppet — profile
PNT 26 36 8 16 0
PNT 26 28 6 10 0
PNT 28 32 2 2 3
C Rod
LIN 30 52 30 90 1
C
REC 4
C
C --- FRAME II.004: LAPTOP — slides in right ---
PNT 100 46 10 8 0
PNT 102 44 6 4 0
PNT 103 45 4 2 3
C
C TECH LAWYER puppet — profile
PNT 90 36 8 16 0
PNT 90 28 6 10 0
PNT 92 32 2 2 3
C Rod
LIN 94 52 94 90 1
C
REC 4
C
C --- FRAME II.005: GAVEL STRIKE — puppet movement ---
PNT 50 14 4 6 3
PNT 50 12 2 2 2
C Gavel raises
PNT 48 8 4 6 0
C
REC 2
C
C Gavel slams
PNT 48 8 4 6 3
PNT 49 9 2 4 2
PNT 50 14 4 6 0
PNT 49 13 2 2 0
C Impact — screen flashes
PNT 10 10 108 68 3
C
REC 1
C
PNT 10 10 108 68 2
C Restore all silhouettes
PNT 56 10 16 8 0
PNT 58 8 12 4 0
PNT 52 18 24 10 0
PNT 50 14 4 6 0
PNT 14 40 8 26 0
PNT 26 28 10 24 0
PNT 90 28 10 24 0
PNT 100 44 10 10 0
C Cutouts
PNT 60 10 2 2 3
PNT 28 32 2 2 3
PNT 92 32 2 2 3
PNT 103 45 4 2 3
PNT 14 48 8 1 3
PNT 14 52 8 1 3
PNT 14 56 8 1 3
PNT 14 60 8 1 3
C
REC 4
C
C --- FRAME II.006: WRITER PUPPET ARM RAISES ---
PNT 24 34 4 4 0
PNT 22 30 4 4 0
PNT 20 26 3 3 0
C
REC 3
C
C --- FRAME II.007: TECH LAWYER RECOILS ---
C Body tilts back — puppet articulation
PNT 90 36 8 16 3
PNT 91 37 6 14 2
PNT 92 36 8 16 0
PNT 94 38 4 12 0
C
REC 3
C
C Recovers
PNT 92 36 8 16 3
PNT 93 37 6 14 2
PNT 90 36 8 16 0
C
REC 3
C
C --- FRAME II.008: HOLD ---
REC 8
C
C
C ============================================================
C  ACT III: RESOLUTION — HORSE BECOMES INFRASTRUCTURE
C  Horse puppet transforms. Cart appears.
C  Horse fades. Cart fades. Only light remains.
C ============================================================
C
C --- FRAME III.001: CLEAR SCREEN ---
PNT 10 10 108 68 2
PNT 12 12 104 64 3
C New rod
LIN 64 78 64 90 1
C
REC 4
C
C --- FRAME III.002: HORSE PUPPET — center, large ---
PNT 40 30 28 14 0
PNT 38 20 6 14 0
PNT 32 18 8 8 0
PNT 35 20 2 2 3
PNT 32 16 2 3 0
PNT 30 24 3 2 0
C Legs
PNT 44 44 2 20 0
PNT 48 44 2 20 0
PNT 56 42 2 20 0
PNT 60 42 2 20 0
C Hooves
PNT 43 64 4 2 0
PNT 47 64 4 2 0
PNT 55 62 4 2 0
PNT 59 62 4 2 0
C Tail
PNT 68 30 2 6 0
PNT 70 28 2 6 0
PNT 72 26 2 6 0
C Mane
PNT 38 18 2 4 0
PNT 40 16 2 4 0
C Rod
LIN 50 44 50 90 1
C
REC 8
C
C --- FRAME III.003: CART APPEARS — attached to horse ---
PNT 76 32 24 12 0
PNT 78 34 20 8 3
C Wheels — cutout circles
PNT 78 42 4 6 0
PNT 80 44 2 2 3
PNT 96 42 4 6 0
PNT 98 44 2 2 3
C Harness connecting horse to cart
LIN 68 36 76 34 0
C
C Cargo — glowing (value 3 in shadow)
PNT 80 34 12 6 3
C
REC 6
C
C --- FRAME III.004: HORSE BEGINS TO FADE — puppeteer lowers ---
C Horse values shift — silhouette becomes less dense
PNT 40 30 28 14 1
PNT 38 20 6 14 1
PNT 32 18 8 8 1
C Legs lighten
PNT 44 44 2 20 1
PNT 48 44 2 20 1
PNT 56 42 2 20 1
PNT 60 42 2 20 1
C Rod lowers
LIN 50 44 50 90 0
C
REC 4
C
C --- FRAME III.005: HORSE NEARLY GONE ---
PNT 30 16 40 50 3
PNT 32 18 36 46 2
C Only the eye cutout remains bright
PNT 35 20 2 2 3
C
REC 4
C
C --- FRAME III.006: HORSE GONE — only cart remains ---
PNT 30 16 40 52 2
PNT 32 18 36 48 3
C Cart still present
PNT 76 32 24 12 0
PNT 78 34 20 8 3
PNT 78 42 4 6 0
PNT 80 44 2 2 3
PNT 96 42 4 6 0
PNT 98 44 2 2 3
C
REC 6
C
C --- FRAME III.007: CART FADES ---
PNT 76 32 24 12 1
PNT 78 42 4 6 1
PNT 96 42 4 6 1
C
REC 4
C
PNT 76 32 24 18 3
PNT 78 34 20 14 2
C
REC 4
C
C --- FRAME III.008: SCREEN GOES FULLY BRIGHT ---
C The technology has disappeared
PNT 10 10 108 68 3
C
REC 4
C
C Brighter
PNT 10 10 108 68 4
C
REC 4
C
C Even brighter
PNT 10 10 108 68 5
C
REC 4
C
C --- FRAME III.009: SCREEN DIMS — end of performance ---
PNT 10 10 108 68 3
C
REC 3
C
PNT 10 10 108 68 2
C
REC 3
C
PNT 10 10 108 68 1
C
REC 3
C
CLR 0
C
REC 6
C
C ============================================================
C  END: hh4.md — SHADOW PUPPET / WAYANG STYLE
C  All figures as flat profile silhouettes (value 0)
C  against luminous screen (value 2-3).
C  Articulated puppet motion. Control rods visible.
C  3 ACTS / ~30 FRAMES
C ============================================================
