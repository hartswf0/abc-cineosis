C ============================================================
C  SHE'S JUST A HAPPY HORSE — hh5.md
C  SOURCE: hhs5.md (Screenplay guide JSON)
C  128x96 / 8 GRAYSCALE / BEFLIX
C
C  RENDERING STYLE: PARTICLE FIELD / STIPPLE
C  -------------------------------------------
C  ALL FORMS built from scattered 1x1 pixel dots.
C  No solid fills. No outlines. No LIN commands.
C  Pure PNT 1x1 stipple patterns at varying density.
C  Dense stipple = solid form. Sparse = transparency.
C  Figures COALESCE from dispersed particles and
C  DISPERSE back into noise. Like a pointillist painting
C  or a CRT phosphor display breaking down.
C
C  3 ACTS from hhs5.md screenplay guide:
C  ACT I  — Particles coalesce into Calypso
C  ACT II — Courtroom particles: order vs chaos
C  ACT III — Particles disperse: technology disappears
C ============================================================
C
C
C ============================================================
C  ACT I: PARTICLES COALESCE INTO CALYPSO
C  Random noise → horse shape → Dario shape
C ============================================================
C
C --- FRAME I.001: RANDOM NOISE FIELD ---
CLR 0
C Scatter — random-looking particles, all value 2
PNT 5 7 1 1 2
PNT 12 3 1 1 2
PNT 19 11 1 1 2
PNT 27 5 1 1 2
PNT 33 9 1 1 2
PNT 41 2 1 1 2
PNT 48 14 1 1 2
PNT 55 6 1 1 2
PNT 62 10 1 1 2
PNT 70 4 1 1 2
PNT 77 12 1 1 2
PNT 84 8 1 1 2
PNT 91 1 1 1 2
PNT 98 13 1 1 2
PNT 105 5 1 1 2
PNT 113 9 1 1 2
PNT 120 3 1 1 2
PNT 3 22 1 1 2
PNT 10 28 1 1 2
PNT 18 34 1 1 2
PNT 25 20 1 1 2
PNT 31 40 1 1 2
PNT 38 26 1 1 2
PNT 44 48 1 1 2
PNT 51 32 1 1 2
PNT 58 44 1 1 2
PNT 65 22 1 1 2
PNT 72 50 1 1 2
PNT 79 36 1 1 2
PNT 86 28 1 1 2
PNT 93 46 1 1 2
PNT 100 38 1 1 2
PNT 107 54 1 1 2
PNT 114 30 1 1 2
PNT 121 42 1 1 2
PNT 7 56 1 1 2
PNT 14 62 1 1 2
PNT 22 70 1 1 2
PNT 29 58 1 1 2
PNT 36 74 1 1 2
PNT 43 66 1 1 2
PNT 50 78 1 1 2
PNT 57 60 1 1 2
PNT 64 72 1 1 2
PNT 71 84 1 1 2
PNT 78 68 1 1 2
PNT 85 76 1 1 2
PNT 92 64 1 1 2
PNT 99 80 1 1 2
PNT 106 70 1 1 2
PNT 113 88 1 1 2
PNT 120 74 1 1 2
PNT 8 90 1 1 2
PNT 35 86 1 1 2
PNT 62 92 1 1 2
PNT 89 84 1 1 2
PNT 116 90 1 1 2
C
REC 4
C
C --- FRAME I.002: PARTICLES DRIFT TOWARD HORSE REGION ---
C Clear scattered noise
PNT 5 7 1 1 0
PNT 12 3 1 1 0
PNT 19 11 1 1 0
PNT 27 5 1 1 0
PNT 91 1 1 1 0
PNT 98 13 1 1 0
PNT 105 5 1 1 0
PNT 113 9 1 1 0
PNT 120 3 1 1 0
PNT 8 90 1 1 0
PNT 35 86 1 1 0
PNT 116 90 1 1 0
C
C New positions — converging on center-left
PNT 30 38 1 1 3
PNT 32 42 1 1 3
PNT 28 36 1 1 3
PNT 34 44 1 1 3
PNT 36 40 1 1 3
PNT 38 46 1 1 3
PNT 26 34 1 1 3
PNT 40 48 1 1 3
PNT 24 32 1 1 3
PNT 42 50 1 1 3
PNT 22 30 1 1 3
PNT 44 52 1 1 3
PNT 20 28 1 1 2
PNT 46 54 1 1 2
PNT 48 56 1 1 2
C
REC 3
C
C --- FRAME I.003: HORSE SHAPE — sparse stipple ---
C Clear remaining far particles
PNT 33 9 1 1 0
PNT 41 2 1 1 0
PNT 48 14 1 1 0
PNT 55 6 1 1 0
PNT 62 10 1 1 0
PNT 70 4 1 1 0
PNT 77 12 1 1 0
PNT 84 8 1 1 0
PNT 3 22 1 1 0
PNT 10 28 1 1 0
PNT 107 54 1 1 0
PNT 114 30 1 1 0
PNT 121 42 1 1 0
PNT 113 88 1 1 0
PNT 120 74 1 1 0
C
C Horse BODY stipple — center density
PNT 30 40 1 1 5
PNT 32 41 1 1 5
PNT 34 42 1 1 5
PNT 36 40 1 1 5
PNT 38 41 1 1 5
PNT 40 42 1 1 5
PNT 31 43 1 1 5
PNT 33 44 1 1 5
PNT 35 43 1 1 5
PNT 37 44 1 1 5
PNT 39 43 1 1 5
PNT 41 44 1 1 5
PNT 29 41 1 1 4
PNT 42 40 1 1 4
PNT 43 42 1 1 4
PNT 44 41 1 1 4
C Neck stipple
PNT 26 32 1 1 5
PNT 27 34 1 1 5
PNT 28 36 1 1 5
PNT 25 33 1 1 4
PNT 26 35 1 1 4
PNT 27 37 1 1 4
PNT 28 38 1 1 5
C Head stipple
PNT 22 30 1 1 5
PNT 23 31 1 1 5
PNT 24 30 1 1 5
PNT 21 32 1 1 4
PNT 22 33 1 1 5
PNT 20 31 1 1 4
C Eye — single bright pixel
PNT 23 31 1 1 7
C Ear particles
PNT 22 28 1 1 6
PNT 24 28 1 1 6
C
C Leg stipple — vertical columns of dots
PNT 32 48 1 1 5
PNT 32 50 1 1 5
PNT 32 52 1 1 5
PNT 32 54 1 1 5
PNT 32 56 1 1 5
PNT 32 58 1 1 5
PNT 32 60 1 1 5
PNT 36 48 1 1 5
PNT 36 50 1 1 5
PNT 36 52 1 1 5
PNT 36 54 1 1 5
PNT 36 56 1 1 5
PNT 36 58 1 1 5
PNT 36 60 1 1 5
PNT 42 46 1 1 5
PNT 42 48 1 1 5
PNT 42 50 1 1 5
PNT 42 52 1 1 5
PNT 42 54 1 1 5
PNT 42 56 1 1 5
PNT 42 58 1 1 5
PNT 42 60 1 1 5
C Hooves — denser
PNT 31 62 1 1 6
PNT 32 62 1 1 6
PNT 33 62 1 1 6
PNT 35 62 1 1 6
PNT 36 62 1 1 6
PNT 37 62 1 1 6
PNT 41 62 1 1 6
PNT 42 62 1 1 6
PNT 43 62 1 1 6
C
C Tail stipple
PNT 46 40 1 1 4
PNT 48 38 1 1 4
PNT 50 36 1 1 4
PNT 47 39 1 1 3
PNT 49 37 1 1 3
C
C Grass stipple — value 2 scattered
PNT 6 64 1 1 2
PNT 14 66 1 1 2
PNT 22 68 1 1 2
PNT 50 64 1 1 2
PNT 58 66 1 1 2
PNT 66 68 1 1 2
PNT 74 64 1 1 2
PNT 82 66 1 1 2
PNT 90 68 1 1 2
PNT 98 64 1 1 2
PNT 106 66 1 1 2
PNT 114 68 1 1 2
PNT 10 70 1 1 2
PNT 30 72 1 1 2
PNT 50 70 1 1 2
PNT 70 72 1 1 2
PNT 90 70 1 1 2
PNT 110 72 1 1 2
C
REC 6
C
C --- FRAME I.004: DARIO COALESCES — stipple figure right ---
C Body stipple
PNT 80 36 1 1 4
PNT 82 38 1 1 4
PNT 84 36 1 1 4
PNT 81 40 1 1 4
PNT 83 42 1 1 4
PNT 85 40 1 1 4
PNT 80 42 1 1 3
PNT 84 44 1 1 3
C Head stipple
PNT 81 28 1 1 5
PNT 83 30 1 1 5
PNT 82 29 1 1 5
PNT 80 30 1 1 4
PNT 84 28 1 1 4
C Eyes
PNT 81 30 1 1 7
PNT 83 30 1 1 7
C Legs
PNT 81 48 1 1 4
PNT 81 50 1 1 4
PNT 81 52 1 1 4
PNT 81 54 1 1 4
PNT 81 56 1 1 4
PNT 81 58 1 1 4
PNT 81 60 1 1 4
PNT 84 48 1 1 4
PNT 84 50 1 1 4
PNT 84 52 1 1 4
PNT 84 54 1 1 4
PNT 84 56 1 1 4
PNT 84 58 1 1 4
PNT 84 60 1 1 4
C
REC 6
C
C --- FRAME I.005: BOTH FIGURES — hold ---
REC 10
C
C
C ============================================================
C  ACT II: PARTICLES FORM COURTROOM — ORDER vs CHAOS
C  Dense stipple = the system. Sparse = individuals.
C ============================================================
C
C --- FRAME II.001: ALL DISPERSE ---
CLR 0
C Random scatter — new noise
PNT 3 8 1 1 2
PNT 11 22 1 1 2
PNT 19 44 1 1 2
PNT 27 16 1 1 2
PNT 35 38 1 1 2
PNT 43 52 1 1 2
PNT 51 10 1 1 2
PNT 59 34 1 1 2
PNT 67 58 1 1 2
PNT 75 24 1 1 2
PNT 83 48 1 1 2
PNT 91 12 1 1 2
PNT 99 40 1 1 2
PNT 107 26 1 1 2
PNT 115 54 1 1 2
PNT 123 18 1 1 2
PNT 7 70 1 1 2
PNT 31 76 1 1 2
PNT 55 62 1 1 2
PNT 79 82 1 1 2
PNT 103 68 1 1 2
C
REC 3
C
C --- FRAME II.002: BENCH STIPPLE FORMS — very dense ---
C Judge bench — DENSE stipple (every other pixel)
PNT 40 18 1 1 5
PNT 42 18 1 1 5
PNT 44 18 1 1 5
PNT 46 18 1 1 5
PNT 48 18 1 1 5
PNT 50 18 1 1 5
PNT 52 18 1 1 5
PNT 54 18 1 1 5
PNT 56 18 1 1 5
PNT 58 18 1 1 5
PNT 60 18 1 1 5
PNT 62 18 1 1 5
PNT 64 18 1 1 5
PNT 66 18 1 1 5
PNT 68 18 1 1 5
PNT 70 18 1 1 5
PNT 72 18 1 1 5
PNT 74 18 1 1 5
PNT 76 18 1 1 5
PNT 78 18 1 1 5
PNT 80 18 1 1 5
PNT 82 18 1 1 5
PNT 84 18 1 1 5
PNT 86 18 1 1 5
PNT 41 20 1 1 5
PNT 43 20 1 1 5
PNT 45 20 1 1 5
PNT 47 20 1 1 5
PNT 49 20 1 1 5
PNT 51 20 1 1 5
PNT 53 20 1 1 5
PNT 55 20 1 1 5
PNT 57 20 1 1 5
PNT 59 20 1 1 5
PNT 61 20 1 1 5
PNT 63 20 1 1 5
PNT 65 20 1 1 5
PNT 67 20 1 1 5
PNT 69 20 1 1 5
PNT 71 20 1 1 5
PNT 73 20 1 1 5
PNT 75 20 1 1 5
PNT 77 20 1 1 5
PNT 79 20 1 1 5
PNT 81 20 1 1 5
PNT 83 20 1 1 5
PNT 85 20 1 1 5
C
C Judge — sparse stipple (authority but human)
PNT 62 10 1 1 5
PNT 64 11 1 1 5
PNT 66 10 1 1 5
PNT 63 12 1 1 4
PNT 65 13 1 1 4
PNT 61 14 1 1 4
PNT 67 14 1 1 4
PNT 64 14 1 1 6
PNT 63 10 1 1 7
PNT 66 10 1 1 7
C
REC 4
C
C --- FRAME II.003: GALLERY — sparse scattered figures ---
C Gallery row — very sparse (the public, the masses)
PNT 10 58 1 1 3
PNT 16 58 1 1 3
PNT 22 58 1 1 3
PNT 28 58 1 1 3
PNT 34 58 1 1 3
PNT 40 58 1 1 3
PNT 46 58 1 1 3
PNT 52 58 1 1 3
PNT 58 58 1 1 3
PNT 64 58 1 1 3
PNT 70 58 1 1 3
PNT 76 58 1 1 3
PNT 82 58 1 1 3
PNT 88 58 1 1 3
PNT 94 58 1 1 3
PNT 100 58 1 1 3
PNT 106 58 1 1 3
PNT 112 58 1 1 3
PNT 118 58 1 1 3
C
REC 4
C
C --- FRAME II.004: HOLD ---
REC 6
C
C
C ============================================================
C  ACT III: DISPERSION — TECHNOLOGY DISAPPEARS
C  All particle forms dissolve back into random noise.
C  The horse form is last to go — single pixel remains.
C ============================================================
C
C --- FRAME III.001: BENCH DISPERSES ---
C Every other bench pixel goes dark
PNT 40 18 1 1 0
PNT 44 18 1 1 0
PNT 48 18 1 1 0
PNT 52 18 1 1 0
PNT 56 18 1 1 0
PNT 60 18 1 1 0
PNT 64 18 1 1 0
PNT 68 18 1 1 0
PNT 72 18 1 1 0
PNT 76 18 1 1 0
PNT 80 18 1 1 0
PNT 84 18 1 1 0
C
REC 3
C
C --- FRAME III.002: MORE DISPERSAL ---
PNT 42 18 1 1 0
PNT 46 18 1 1 0
PNT 50 18 1 1 0
PNT 54 18 1 1 0
PNT 58 18 1 1 0
PNT 62 18 1 1 0
PNT 66 18 1 1 0
PNT 70 18 1 1 0
PNT 74 18 1 1 0
PNT 78 18 1 1 0
PNT 82 18 1 1 0
PNT 86 18 1 1 0
C Gallery disperses
PNT 10 58 1 1 0
PNT 22 58 1 1 0
PNT 34 58 1 1 0
PNT 46 58 1 1 0
PNT 58 58 1 1 0
PNT 70 58 1 1 0
PNT 82 58 1 1 0
PNT 94 58 1 1 0
PNT 106 58 1 1 0
PNT 118 58 1 1 0
C
REC 3
C
C --- FRAME III.003: NEARLY EMPTY ---
C Clear remaining bench
PNT 41 20 1 1 0
PNT 45 20 1 1 0
PNT 49 20 1 1 0
PNT 53 20 1 1 0
PNT 57 20 1 1 0
PNT 61 20 1 1 0
PNT 65 20 1 1 0
PNT 69 20 1 1 0
PNT 73 20 1 1 0
PNT 77 20 1 1 0
PNT 81 20 1 1 0
PNT 85 20 1 1 0
C Clear rest
PNT 43 20 1 1 0
PNT 47 20 1 1 0
PNT 51 20 1 1 0
PNT 55 20 1 1 0
PNT 59 20 1 1 0
PNT 63 20 1 1 0
PNT 67 20 1 1 0
PNT 71 20 1 1 0
PNT 75 20 1 1 0
PNT 79 20 1 1 0
PNT 83 20 1 1 0
C
C Judge disperses
PNT 62 10 1 1 0
PNT 64 11 1 1 0
PNT 66 10 1 1 0
PNT 63 12 1 1 0
PNT 65 13 1 1 0
PNT 61 14 1 1 0
PNT 67 14 1 1 0
PNT 64 14 1 1 0
C
C Gallery fully gone
PNT 16 58 1 1 0
PNT 28 58 1 1 0
PNT 40 58 1 1 0
PNT 52 58 1 1 0
PNT 64 58 1 1 0
PNT 76 58 1 1 0
PNT 88 58 1 1 0
PNT 100 58 1 1 0
PNT 112 58 1 1 0
C
REC 3
C
C --- FRAME III.004: SINGLE PIXEL REMAINS — the horse eye ---
C Only one bright pixel in total darkness
PNT 63 10 1 1 7
PNT 66 10 1 1 7
C
REC 6
C
C --- FRAME III.005: EYE FADES ---
PNT 63 10 1 1 5
PNT 66 10 1 1 5
C
REC 3
C
PNT 63 10 1 1 3
PNT 66 10 1 1 3
C
REC 3
C
PNT 63 10 1 1 1
PNT 66 10 1 1 1
C
REC 3
C
PNT 63 10 1 1 0
PNT 66 10 1 1 0
C
REC 6
C
C ============================================================
C  END: hh5.md — PARTICLE FIELD / STIPPLE
C  ZERO solid fills. ZERO LIN commands.
C  EVERY form built from 1x1 PNT dots only.
C  Density = opacity. Spacing = transparency.
C  3 ACTS / ~20 FRAMES
C ============================================================
