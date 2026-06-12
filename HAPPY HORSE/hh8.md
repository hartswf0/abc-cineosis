C ============================================================
C  SHE'S JUST A HAPPY HORSE — hh8.md
C  SOURCE: hhs8.md (Full 1245-line screenplay)
C  128x96 / 8 GRAYSCALE / BEFLIX
C
C  RENDERING STYLE: WOODCUT / GERMAN EXPRESSIONIST
C  ------------------------------------------------
C  ONLY VALUES 0 AND 7. Pure black and white.
C  No midtones. Stark, dramatic, high-contrast.
C  Figures defined by NEGATIVE SPACE — white shapes
C  carved from black ground, or black shapes on white.
C  Hatching lines for texture (parallel LIN commands).
C  Inspired by Käthe Kollwitz, Ernst Ludwig Kirchner.
C  Every frame reads like a relief print pulled from a block.
C
C  10 SCENES FROM HHS8 (selected key moments):
C  01 — CALYPSO GRAZES (white on black)
C  02 — INTERVIEW (black on white)
C  03 — NYMPH AND ODYSSEUS (white on black)
C  04 — COURTROOM (black on white)
C  05 — CONNECTICUT 1871 MANURE (white on black)
C  06 — DATA CENTER (black on white)
C  07 — PLOW HORSES (white on black)
C  08 — MUYBRIDGE (black on white)
C  09 — POLICY HEARING (white on black)
C  10 — FINAL — CART WHEEL (black on white to black)
C ============================================================
C
C
C ============================================================
C  SCENE 01: CALYPSO GRAZES — WHITE ON BLACK
C  White figure carved from pure black.
C  Hatching lines define grass texture.
C ============================================================
C
CLR 0
C === ALL BLACK GROUND ===
C
C --- CALYPSO — white silhouette on black ---
C Body
PNT 34 40 22 12 7
C Neck
PNT 30 28 6 14 7
C Head — grazing down
PNT 24 36 8 6 7
C Eye — BLACK dot in white
PNT 28 38 2 2 0
C Ears
PNT 24 32 3 4 7
PNT 28 32 3 4 7
C Muzzle
PNT 22 40 4 3 7
C
C Legs — bold white strokes
LIN 38 52 38 70 7
LIN 40 52 40 70 7
LIN 44 52 44 70 7
LIN 46 52 46 70 7
LIN 50 50 50 70 7
LIN 52 50 52 70 7
LIN 54 50 54 70 7
C Hooves — blocks
PNT 37 70 4 3 7
PNT 43 70 4 3 7
PNT 49 70 4 3 7
C
C Tail
LIN 56 42 62 36 7
LIN 62 36 66 38 7
LIN 66 38 68 34 7
C
C Mane — hatching strokes
LIN 31 28 33 24 7
LIN 32 30 34 26 7
LIN 33 32 35 28 7
C
C --- GRASS — hatching lines, white on black ---
LIN 0 76 20 72 7
LIN 4 78 24 74 7
LIN 8 80 28 76 7
LIN 12 82 32 78 7
LIN 60 76 80 72 7
LIN 64 78 84 74 7
LIN 68 80 88 76 7
LIN 72 82 92 78 7
LIN 96 76 116 72 7
LIN 100 78 120 74 7
LIN 104 80 124 76 7
C
C --- HORIZON LINE ---
LIN 0 22 127 22 7
C
C --- FENCE — white lines ---
LIN 70 36 72 50 7
LIN 82 34 84 48 7
LIN 94 32 96 46 7
LIN 70 40 94 36 7
LIN 70 46 94 42 7
C
C --- DARIO on fence — white block ---
PNT 84 26 6 10 7
PNT 86 22 4 6 7
C Eyes — BLACK
PNT 87 24 1 1 0
PNT 89 24 1 1 0
C
REC 10
C
C --- FRAME 01.002: TAIL FLICK ---
LIN 56 42 62 36 0
LIN 62 36 66 38 0
LIN 66 38 68 34 0
LIN 56 42 58 34 7
LIN 58 34 56 28 7
C
REC 3
C
LIN 56 42 58 34 0
LIN 58 34 56 28 0
LIN 56 42 62 36 7
LIN 62 36 66 38 7
LIN 66 38 68 34 7
C
REC 3
C
C --- FRAME 01.003: CHEW ---
PNT 22 40 4 3 0
PNT 22 42 4 3 7
C
REC 2
C
PNT 22 42 4 3 0
PNT 22 40 4 3 7
C
REC 3
C
C --- FRAME 01.004: HOLD ---
REC 8
C
C
C ============================================================
C  SCENE 02: INTERVIEW — BLACK ON WHITE (INVERSION)
C  White ground, black figures. Like a printed page.
C ============================================================
C
CLR 7
C === ALL WHITE GROUND ===
C
C --- STUDIO FRAME — black border ---
LIN 0 0 127 0 0
LIN 0 95 127 95 0
LIN 0 0 0 95 0
LIN 127 0 127 95 0
C Inner frame
LIN 2 2 125 2 0
LIN 2 93 125 93 0
C
C --- INTERVIEWER — black figure, left ---
PNT 20 30 12 20 0
PNT 22 22 8 10 0
C Eyes — WHITE
PNT 24 25 2 2 7
PNT 28 25 2 2 7
C Mouth
LIN 25 30 29 30 7
C Arms — bold black
LIN 18 38 14 50 0
LIN 32 38 36 50 0
C
C --- DARIO — black figure, right ---
PNT 88 30 12 20 0
PNT 90 22 8 10 0
C Eyes — WHITE
PNT 92 25 2 2 7
PNT 96 25 2 2 7
C Mouth — slight smile
LIN 93 30 97 30 7
LIN 94 31 96 31 7
C Arms
LIN 86 38 82 50 0
LIN 100 38 104 50 0
C
C --- TABLE between them ---
PNT 30 50 68 6 0
LIN 30 50 98 50 0
C
C --- MICROPHONES — bold ---
LIN 42 44 42 50 0
PNT 41 42 3 3 0
PNT 42 43 1 1 7
LIN 82 44 82 50 0
PNT 81 42 3 3 0
PNT 82 43 1 1 7
C
C --- HATCHING — shadow under table ---
LIN 32 56 96 56 0
LIN 34 58 94 58 0
LIN 36 60 92 60 0
LIN 38 62 90 62 0
C
C --- CAMERAS — black silhouettes ---
PNT 4 60 8 16 0
PNT 116 60 8 16 0
C Camera lens — white dot
PNT 7 58 2 2 7
PNT 119 58 2 2 7
C
REC 8
C
C --- FRAME 02.002: DARIO SPEAKS --- mouth opens ---
LIN 93 30 97 30 0
LIN 94 31 96 31 0
PNT 93 30 4 3 7
C
REC 3
C
PNT 93 30 4 3 0
LIN 93 30 97 30 7
C
REC 3
C
C --- FRAME 02.003: HOLD ---
REC 6
C
C
C ============================================================
C  SCENE 03: NYMPH AND ODYSSEUS — WHITE ON BLACK
C  Mythic dreamscape. Stark white figures.
C ============================================================
C
CLR 0
C
C --- SEA — horizontal hatch lines ---
LIN 0 16 127 16 7
LIN 0 20 127 20 7
LIN 0 24 127 24 7
C
C --- ISLAND GROUND — white mass ---
PNT 0 28 128 68 0
C Ground texture — sparse hatch
LIN 0 60 30 56 7
LIN 40 62 70 58 7
LIN 80 60 110 56 7
C
C --- CALYPSO THE NYMPH — white on black ---
PNT 30 28 12 34 7
C Head
PNT 32 20 8 10 7
C Hair — flowing lines
LIN 30 24 24 36 7
LIN 38 24 44 36 7
LIN 24 36 20 48 7
LIN 44 36 48 48 7
C Eyes — BLACK
PNT 34 24 2 2 0
PNT 37 24 2 2 0
C
C Reaching arm
LIN 42 34 54 28 7
C
C --- ODYSSEUS — white, turned AWAY ---
PNT 80 30 10 22 7
C Head — facing right (away from nymph)
PNT 82 22 8 10 7
C Beard — hatching
LIN 86 30 90 30 0
LIN 86 31 88 31 0
C Eyes — looking at sea
PNT 88 25 2 2 0
C
C Arm pointing at sea
LIN 90 36 102 26 7
C
C --- TREES — white trunks ---
LIN 12 10 12 50 7
LIN 14 10 14 50 7
LIN 112 12 112 52 7
LIN 114 12 114 52 7
C Branches — hatching
LIN 12 16 6 10 7
LIN 14 14 20 8 7
LIN 112 18 106 12 7
LIN 114 16 120 10 7
C
REC 10
C
C --- FRAME 03.002: ODYSSEUS TURNS FURTHER ---
PNT 82 22 8 10 0
PNT 84 22 8 10 7
PNT 90 25 2 2 0
C
REC 4
C
C --- FRAME 03.003: NYMPH ARM LOWERS ---
LIN 42 34 54 28 0
LIN 42 34 40 44 7
C
REC 4
C
C --- FRAME 03.004: HOLD ---
REC 8
C
C
C ============================================================
C  SCENE 04: COURTROOM — BLACK ON WHITE
C  Severe, angular. Books vs laptops.
C ============================================================
C
CLR 7
C
C --- JUDGE BENCH — massive black block ---
PNT 30 12 68 12 0
LIN 30 12 98 12 0
LIN 30 24 98 24 0
C Gavel — bold
PNT 56 8 6 4 0
PNT 57 9 4 2 7
LIN 62 8 66 4 0
C
C Judge figure — black
PNT 58 2 12 12 0
C Eyes — WHITE
PNT 61 5 2 2 7
PNT 66 5 2 2 7
C
C --- BOOKS — left table, black blocks ---
PNT 8 34 6 10 0
PNT 16 32 6 12 0
PNT 24 34 6 10 0
C Table
PNT 4 44 36 4 0
C
C --- LAPTOPS — right table, black shapes ---
PNT 86 34 6 6 0
PNT 87 35 4 4 7
PNT 96 34 6 6 0
PNT 97 35 4 4 7
PNT 106 34 6 6 0
PNT 107 35 4 4 7
C Table
PNT 82 44 36 4 0
C
C --- GALLERY — black heads ---
PNT 10 62 4 4 0
PNT 22 62 4 4 0
PNT 34 62 4 4 0
PNT 46 62 4 4 0
PNT 58 62 4 4 0
PNT 70 62 4 4 0
PNT 82 62 4 4 0
PNT 94 62 4 4 0
PNT 106 62 4 4 0
PNT 118 62 4 4 0
C Gallery rail
LIN 0 60 127 60 0
C
C --- SHADOW hatching under benches ---
LIN 6 48 38 48 0
LIN 8 50 36 50 0
LIN 84 48 116 48 0
LIN 86 50 114 50 0
C
REC 10
C
C --- FRAME 04.002: GAVEL STRIKE ---
PNT 56 8 6 4 7
PNT 56 10 6 4 0
C
REC 2
C
PNT 56 10 6 4 7
PNT 56 8 6 4 0
C
REC 3
C
C --- FRAME 04.003: HOLD ---
REC 6
C
C
C ============================================================
C  SCENE 05: CONNECTICUT 1871 — WHITE ON BLACK
C  Manure heaps as white masses. Workers as white figures.
C ============================================================
C
CLR 0
C
C --- ROAD — white border lines ---
LIN 0 30 127 30 7
LIN 0 70 127 70 7
C Road surface — hatching for dirt texture
LIN 4 34 20 34 7
LIN 24 38 40 38 7
LIN 44 34 60 34 7
LIN 64 38 80 38 7
LIN 84 34 100 34 7
LIN 104 38 120 38 7
C
C --- STONE WALLS ---
PNT 0 26 24 4 7
PNT 104 26 24 4 7
C
C --- MANURE HEAPS — white triangular masses ---
PNT 32 50 8 8 7
PNT 34 48 4 4 7
PNT 48 52 6 6 7
PNT 50 50 2 4 7
PNT 64 50 8 8 7
PNT 66 48 4 4 7
PNT 80 52 6 6 7
PNT 82 50 2 4 7
C
C --- HASLEM — white figure ---
PNT 24 36 8 14 7
PNT 26 30 4 8 7
C Hat
PNT 24 28 8 3 7
C Eyes — BLACK
PNT 27 32 1 1 0
PNT 29 32 1 1 0
C Arm pointing
LIN 32 40 42 34 7
C
C --- WORKER with rake — white ---
PNT 44 38 8 12 7
PNT 46 32 4 8 7
C Rake
LIN 44 42 38 54 7
PNT 36 52 6 3 7
C
C --- BARE TREES ---
LIN 10 4 10 26 7
LIN 10 10 6 4 7
LIN 10 8 14 2 7
LIN 118 6 118 28 7
LIN 118 12 114 6 7
LIN 118 10 122 4 7
C
REC 8
C
C --- FRAME 05.002: RAKE MOTION ---
PNT 36 52 6 3 0
LIN 44 42 38 54 0
LIN 44 42 36 52 7
PNT 34 50 6 3 7
C
REC 3
C
LIN 44 42 36 52 0
PNT 34 50 6 3 0
LIN 44 42 38 54 7
PNT 36 52 6 3 7
C
REC 3
C
C --- FRAME 05.003: HOLD ---
REC 6
C
C
C ============================================================
C  SCENE 06: DATA CENTER — BLACK ON WHITE
C  Server racks as bold black columns.
C ============================================================
C
CLR 7
C
C --- SERVER RACKS — black pillars ---
PNT 4 8 12 76 0
PNT 24 8 12 76 0
PNT 44 8 12 76 0
PNT 72 8 12 76 0
PNT 92 8 12 76 0
PNT 112 8 12 76 0
C
C LED dots — WHITE in black
PNT 14 18 2 2 7
PNT 14 30 2 2 7
PNT 14 42 2 2 7
PNT 14 54 2 2 7
PNT 14 66 2 2 7
PNT 34 18 2 2 7
PNT 34 30 2 2 7
PNT 34 42 2 2 7
PNT 54 18 2 2 7
PNT 54 30 2 2 7
PNT 54 42 2 2 7
PNT 82 18 2 2 7
PNT 82 30 2 2 7
PNT 82 42 2 2 7
PNT 102 18 2 2 7
PNT 102 30 2 2 7
PNT 122 18 2 2 7
PNT 122 30 2 2 7
C
C Floor line
LIN 0 84 127 84 0
C
C --- CABLE HATCHING on floor ---
LIN 18 86 38 86 0
LIN 20 88 36 88 0
LIN 56 86 76 86 0
LIN 58 88 74 88 0
LIN 94 86 114 86 0
LIN 96 88 112 88 0
C
REC 8
C
C --- FRAME 06.002: LED BLINK ---
PNT 14 18 2 2 0
PNT 34 42 2 2 0
PNT 82 30 2 2 0
C
REC 2
C
PNT 14 18 2 2 7
PNT 34 42 2 2 7
PNT 82 30 2 2 7
C
REC 2
C
C --- FRAME 06.003: HOLD ---
REC 6
C
C
C ============================================================
C  SCENE 07: PLOW HORSES — WHITE ON BLACK
C  Massive straining horses. Bold white muscle shapes.
C  Hatching lines for earth texture.
C ============================================================
C
CLR 0
C
C --- HORSE — huge white form ---
C Body — solid white block
PNT 40 22 28 16 7
C Chest
PNT 36 18 8 14 7
C Neck — thick
PNT 32 10 8 14 7
C Head — forward thrust
PNT 24 8 12 8 7
C Eye — BLACK
PNT 30 10 2 2 0
C Nostril
PNT 26 14 2 2 0
C Mouth
PNT 24 14 3 2 0
C Ears
PNT 26 4 3 5 7
PNT 30 4 3 5 7
C
C Mane — bold white strokes
LIN 34 10 38 4 7
LIN 36 12 40 6 7
LIN 38 14 42 8 7
C
C Legs — WHITE columns
PNT 42 38 4 28 7
PNT 48 38 4 28 7
PNT 56 36 4 28 7
PNT 62 36 4 28 7
C Hooves
PNT 41 66 6 4 7
PNT 47 66 6 4 7
PNT 55 64 6 4 7
PNT 61 64 6 4 7
C
C Tail
LIN 68 24 76 18 7
LIN 76 18 82 20 7
LIN 82 20 86 16 7
C
C Harness — white lines
LIN 38 22 34 40 7
LIN 42 24 38 42 7
C Collar
PNT 34 14 6 8 7
PNT 36 16 2 4 0
C
C --- PLOW — white ---
PNT 28 52 8 8 7
LIN 28 60 36 60 7
LIN 28 52 28 60 7
C Handles
LIN 36 52 44 44 7
C
C --- FARMER — white block ---
PNT 46 40 6 14 7
PNT 48 34 4 8 7
PNT 46 32 6 3 7
C Eyes — black
PNT 49 36 1 1 0
PNT 51 36 1 1 0
C
C --- EARTH HATCHING ---
LIN 0 72 20 68 7
LIN 4 76 24 72 7
LIN 8 80 28 76 7
LIN 60 72 80 68 7
LIN 64 76 84 72 7
LIN 100 72 120 68 7
LIN 104 76 124 72 7
C
C --- FURROW LINES ---
LIN 0 52 22 48 7
LIN 0 56 20 52 7
LIN 0 60 18 56 7
C
C --- SUN — white disc ---
PNT 104 4 10 10 7
PNT 106 6 6 6 0
C Rays
LIN 100 8 96 8 7
LIN 114 8 118 8 7
LIN 109 2 109 0 7
LIN 109 14 109 18 7
C
REC 10
C
C --- FRAME 07.002: STRIDE ---
PNT 42 38 4 28 0
PNT 40 38 4 28 7
PNT 56 36 4 28 0
PNT 54 36 4 28 7
C
REC 3
C
PNT 40 38 4 28 0
PNT 42 38 4 28 7
PNT 54 36 4 28 0
PNT 56 36 4 28 7
C
REC 3
C
C --- FRAME 07.003: HOLD ---
REC 6
C
C
C ============================================================
C  SCENE 08: MUYBRIDGE — BLACK ON WHITE
C  Camera array and racing horse as black prints.
C ============================================================
C
CLR 7
C
C --- TRACK RAILS — bold black ---
LIN 0 14 127 14 0
LIN 0 50 127 50 0
C
C --- CAMERAS — black boxes ---
PNT 8 40 4 8 0
PNT 22 40 4 8 0
PNT 36 40 4 8 0
PNT 50 40 4 8 0
PNT 64 40 4 8 0
PNT 78 40 4 8 0
PNT 92 40 4 8 0
PNT 106 40 4 8 0
C Lens — white dot
PNT 9 39 2 1 7
PNT 23 39 2 1 7
PNT 37 39 2 1 7
PNT 51 39 2 1 7
PNT 65 39 2 1 7
PNT 79 39 2 1 7
PNT 93 39 2 1 7
PNT 107 39 2 1 7
C Tripods
LIN 10 48 10 50 0
LIN 24 48 24 50 0
LIN 38 48 38 50 0
LIN 52 48 52 50 0
LIN 66 48 66 50 0
LIN 80 48 80 50 0
LIN 94 48 94 50 0
LIN 108 48 108 50 0
C
C --- HORSE — black silhouette, galloping ---
PNT 14 20 16 8 0
PNT 12 16 6 6 0
PNT 10 14 4 4 0
C Legs — extended
LIN 16 28 10 36 0
LIN 18 28 14 36 0
LIN 26 28 22 36 0
LIN 28 28 32 36 0
C Ear
PNT 10 12 2 3 0
C Mane
LIN 18 18 22 14 0
LIN 20 20 24 16 0
C
C --- SPECTATORS — black dots ---
PNT 6 56 4 4 0
PNT 18 56 4 4 0
PNT 30 56 4 4 0
PNT 42 56 4 4 0
PNT 54 56 4 4 0
PNT 66 56 4 4 0
PNT 78 56 4 4 0
PNT 90 56 4 4 0
PNT 102 56 4 4 0
PNT 114 56 4 4 0
C
REC 6
C
C --- FRAME 08.002: FLASH ---
PNT 9 39 2 1 0
C
REC 1
C
PNT 9 39 2 1 7
C
REC 1
C
C --- FRAME 08.003: HORSE MOVES ---
PNT 10 12 22 26 7
PNT 40 20 16 8 0
PNT 38 16 6 6 0
PNT 36 14 4 4 0
LIN 42 28 36 36 0
LIN 44 28 40 36 0
LIN 52 28 48 36 0
LIN 54 28 58 36 0
PNT 36 12 2 3 0
LIN 44 18 48 14 0
C
REC 2
C
PNT 37 39 2 1 0
C
REC 1
C
PNT 37 39 2 1 7
C
REC 2
C
C --- FRAME 08.004: HORSE FURTHER ---
PNT 36 12 22 26 7
PNT 66 20 16 8 0
PNT 64 16 6 6 0
PNT 62 14 4 4 0
LIN 68 28 62 36 0
LIN 70 28 66 36 0
LIN 78 28 74 36 0
LIN 80 28 84 36 0
PNT 62 12 2 3 0
LIN 70 18 74 14 0
C
REC 2
C
PNT 65 39 2 1 0
C
REC 1
C
PNT 65 39 2 1 7
C
REC 2
C
C --- FRAME 08.005: HORSE EXIT ---
PNT 62 12 22 26 7
C Empty track
C
REC 6
C
C
C ============================================================
C  SCENE 09: POLICY HEARING — WHITE ON BLACK
C  Figures at microphones. Bold white shapes.
C ============================================================
C
CLR 0
C
C --- LONG TABLE — white ---
PNT 10 44 108 6 7
C
C --- MICROPHONES — white stems ---
LIN 30 36 30 44 7
PNT 28 34 4 3 7
LIN 64 36 64 44 7
PNT 62 34 4 3 7
LIN 98 36 98 44 7
PNT 96 34 4 3 7
C
C --- SENATOR — center, elevated ---
PNT 56 24 14 22 7
PNT 58 18 10 8 7
C Eyes — BLACK
PNT 61 21 2 2 0
PNT 65 21 2 2 0
C
C --- EXECUTIVES — flanking ---
PNT 22 30 12 16 7
PNT 24 24 8 8 7
PNT 27 27 1 1 0
PNT 29 27 1 1 0
C
PNT 90 30 12 16 7
PNT 92 24 8 8 7
PNT 95 27 1 1 0
PNT 97 27 1 1 0
C
C --- SCREEN behind — "FUTURE OF INTELLIGENCE" ---
PNT 20 4 88 12 7
PNT 22 6 84 8 0
LIN 30 8 98 8 7
LIN 30 10 90 10 7
C
C --- GALLERY --- white heads ---
PNT 8 64 4 4 7
PNT 20 64 4 4 7
PNT 32 64 4 4 7
PNT 44 64 4 4 7
PNT 56 64 4 4 7
PNT 68 64 4 4 7
PNT 80 64 4 4 7
PNT 92 64 4 4 7
PNT 104 64 4 4 7
PNT 116 64 4 4 7
C Rail
LIN 0 62 127 62 7
C
REC 8
C
C --- FRAME 09.002: SENATOR SPEAKS ---
PNT 62 26 4 3 7
C
REC 3
C
PNT 62 26 4 3 0
LIN 62 26 65 26 7
C
REC 3
C
C --- FRAME 09.003: HOLD ---
REC 6
C
C
C ============================================================
C  SCENE 10: FINAL — CART WHEEL — BLACK ON WHITE → BLACK
C  White ground. Black cart wheel turns.
C  Everything fades to black.
C ============================================================
C
CLR 7
C
C --- CART WHEEL — large, center ---
C Outer ring
PNT 44 20 40 40 0
PNT 48 24 32 32 7
C Inner hub
PNT 58 34 12 12 0
PNT 60 36 8 8 7
PNT 62 38 4 4 0
C Spokes
LIN 64 24 64 34 0
LIN 64 46 64 56 0
LIN 48 40 58 40 0
LIN 70 40 80 40 0
LIN 50 26 58 34 0
LIN 70 34 78 26 0
LIN 50 54 58 46 0
LIN 70 46 78 54 0
C
C Floor line
LIN 0 60 127 60 0
C
REC 6
C
C --- FRAME 10.002: WHEEL TURNS — spokes shift ---
C Erase old spokes
LIN 64 24 64 34 7
LIN 64 46 64 56 7
LIN 48 40 58 40 7
LIN 70 40 80 40 7
LIN 50 26 58 34 7
LIN 70 34 78 26 7
LIN 50 54 58 46 7
LIN 70 46 78 54 7
C New spoke positions — rotated
LIN 56 24 60 34 0
LIN 68 46 72 56 0
LIN 46 32 58 36 0
LIN 70 44 82 48 0
LIN 48 48 58 44 0
LIN 70 36 80 32 0
LIN 60 46 56 56 0
LIN 68 34 72 24 0
C
REC 3
C
C --- FRAME 10.003: FADE TO BLACK — step 1 ---
C White ground becomes gray (value 5)
PNT 0 0 128 20 5
PNT 0 60 128 36 5
PNT 48 24 32 32 5
PNT 60 36 8 8 5
C
REC 3
C
C --- FRAME 10.004: FADE — step 2 ---
PNT 0 0 128 20 3
PNT 0 60 128 36 3
PNT 48 24 32 32 3
PNT 60 36 8 8 3
C
REC 3
C
C --- FRAME 10.005: FADE — step 3 ---
PNT 0 0 128 96 0
C Wheel now WHITE on black — inverted
PNT 44 20 40 40 7
PNT 48 24 32 32 0
PNT 58 34 12 12 7
PNT 60 36 8 8 0
PNT 62 38 4 4 7
C
REC 4
C
C --- FRAME 10.006: WHEEL FADES ---
PNT 44 20 40 40 5
PNT 58 34 12 12 5
PNT 62 38 4 4 5
C
REC 3
C
PNT 44 20 40 40 3
PNT 58 34 12 12 3
PNT 62 38 4 4 3
C
REC 3
C
PNT 44 20 40 40 1
PNT 58 34 12 12 1
PNT 62 38 4 4 1
C
REC 3
C
CLR 0
C
REC 8
C
C ============================================================
C  END: hh8.md — WOODCUT / GERMAN EXPRESSIONIST
C  ONLY VALUES 0 AND 7 (with fade sequence at end).
C  BLACK/WHITE alternation per scene.
C  10 SCENES / ~80 FRAMES
C ============================================================
