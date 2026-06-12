C ============================================================
C  SHE'S JUST A HAPPY HORSE — hh7.md
C  SOURCE: hhs7.md (CinePrompt-style text-to-video prompts)
C  128x96 / 8 GRAYSCALE / BEFLIX
C
C  RENDERING STYLE: DISSOLVE / MORPH
C  ----------------------------------
C  NO HARD CUTS. Every scene TRANSFORMS into the next
C  by gradual pixel-value shifting. Environments morph:
C  pasture → road → racetrack → courtroom → data center.
C  Objects cross-fade by stepping through intermediate
C  grayscale values (7→6→5→4→3→2→1→0 = fade out,
C  0→1→2→3 = fade in). Overlapping dissolves create
C  ghost-images where two realities coexist.
C
C  7 SEQUENCES FROM HHS7 CINEPROMPTs:
C  SEQ 1 — Opening Essay: Calypso grazes, overlays fade in/out
C  SEQ 2 — Horse as Ancient Technology: gallop through time
C  SEQ 3 — Muybridge: cameras, horse fractures into frames
C  SEQ 4 — Who Gathered the Heap: books dissolve into data
C  SEQ 5 — Law of the Horse: surreal courtroom
C  SEQ 6 — Future Infrastructure: data center → pasture
C  SEQ 7 — Final Metaphor: humans become horses pulling cart
C ============================================================
C
C
C ============================================================
C  SEQ 1: OPENING CINEMATIC ESSAY
C  Italian pasture at golden hour. Calypso grazes.
C  Holographic overlays of AI networks, charts, legal docs
C  FADE IN from black. Overlays DISSOLVE in and out.
C ============================================================
C
C --- FRAME 1.001: FADE FROM BLACK — value 1 ghost ---
CLR 0
C Ghost landscape — value 1 only — barely there
PNT 0 0 128 16 1
PNT 0 16 128 80 1
C
REC 3
C
C --- FRAME 1.002: FADE UP — value 2 ---
PNT 0 0 128 16 2
PNT 0 16 128 6 1
PNT 0 22 128 74 2
C Ghost hills
PNT 10 16 25 4 1
PNT 50 15 30 5 1
PNT 90 16 25 4 1
C
REC 3
C
C --- FRAME 1.003: FADE UP — value 3 landscape emerges ---
PNT 0 0 128 14 1
PNT 0 10 128 6 2
PNT 0 16 128 4 2
PNT 0 20 128 76 3
C Hills solidify
PNT 10 18 25 4 2
PNT 50 17 30 5 3
PNT 90 18 25 4 2
C
REC 3
C
C --- FRAME 1.004: FULL LANDSCAPE — Calypso fades in ---
C Sky — warm gold
PNT 0 0 128 14 1
PNT 0 10 128 6 2
PNT 0 16 128 4 2
C Hills
PNT 0 18 128 4 3
PNT 10 18 25 4 2
PNT 50 17 30 5 3
PNT 90 18 25 4 2
C Grass
PNT 0 22 128 74 3
PNT 0 26 128 2 2
PNT 0 34 128 2 4
PNT 0 42 128 2 2
PNT 0 50 128 2 4
PNT 0 58 128 2 2
PNT 0 66 128 2 4
PNT 0 74 128 2 2
C Foreground
PNT 0 82 128 14 4
C
C Olive trees — distant
PNT 20 10 3 10 4
PNT 40 8 3 12 4
PNT 100 10 3 10 4
C
C Calypso — ghost value 2 first
PNT 40 44 16 8 2
PNT 38 36 4 10 2
PNT 34 32 6 5 2
C
REC 3
C
C --- FRAME 1.005: CALYPSO SOLIDIFIES ---
C Horse body — step to value 5
PNT 40 44 16 8 5
PNT 42 45 12 6 6
C Neck
PNT 38 34 4 12 5
PNT 39 36 2 8 6
C Head — grazing
PNT 34 40 6 4 5
PNT 35 41 4 2 6
PNT 34 42 1 1 7
C Eye
PNT 36 41 1 1 7
C Ears
PNT 34 38 2 3 6
PNT 37 38 2 3 6
C Legs
LIN 44 52 44 66 5
LIN 46 52 46 66 6
LIN 50 52 50 66 5
LIN 52 52 52 66 6
LIN 54 50 54 66 5
LIN 56 50 56 66 6
C Hooves
PNT 43 66 2 2 6
PNT 49 66 2 2 6
PNT 53 66 2 2 6
C Tail
LIN 56 45 60 42 5
LIN 60 42 62 44 4
C Shadow
PNT 40 66 18 2 4
C
REC 8
C
C --- FRAME 1.006: OVERLAY DISSOLVES IN — neural network ghost ---
C Holographic overlay — VALUE 1 over sky area — ghostly
PNT 70 2 12 8 2
PNT 74 4 4 4 3
C Network nodes — faint
PNT 72 4 2 2 2
PNT 80 6 2 2 2
PNT 76 10 2 2 2
LIN 73 5 80 6 1
LIN 80 6 76 10 1
LIN 76 10 73 5 1
C
REC 4
C
C --- FRAME 1.007: OVERLAY BRIGHTENS ---
PNT 72 4 2 2 3
PNT 80 6 2 2 3
PNT 76 10 2 2 3
LIN 73 5 80 6 2
LIN 80 6 76 10 2
LIN 76 10 73 5 2
C Chart overlay — stock graph — ghost
LIN 90 8 94 6 2
LIN 94 6 98 4 2
LIN 98 4 102 2 2
C
REC 4
C
C --- FRAME 1.008: OVERLAY DISSOLVES OUT ---
PNT 70 2 14 12 1
PNT 90 2 16 8 1
PNT 72 4 2 2 1
PNT 80 6 2 2 1
PNT 76 10 2 2 1
C Calypso keeps chewing — undisturbed
PNT 34 42 2 2 5
PNT 34 43 2 2 4
C
REC 2
C
PNT 34 43 2 2 5
PNT 34 42 2 2 4
C
REC 2
C
C --- FRAME 1.009: SECOND OVERLAY — legal document ghost ---
C Faint document lines in sky
LIN 6 4 24 4 2
LIN 6 6 22 6 2
LIN 6 8 20 8 2
LIN 6 10 24 10 2
PNT 4 2 22 10 1
C
REC 4
C
C --- FRAME 1.010: DOCUMENT FADES ---
PNT 4 2 22 10 1
LIN 6 4 24 4 1
LIN 6 6 22 6 1
LIN 6 8 20 8 1
LIN 6 10 24 10 1
C
REC 3
C
PNT 4 2 22 10 1
C
REC 3
C
C --- FRAME 1.011: CALYPSO TAIL SWISH ---
LIN 56 45 60 42 3
LIN 56 45 58 40 5
LIN 58 40 56 36 4
C
REC 3
C
PNT 56 36 4 6 3
LIN 56 45 60 42 5
LIN 60 42 62 44 4
C
REC 3
C
C --- FRAME 1.012: WIND THROUGH GRASS ---
PNT 0 34 40 2 3
PNT 0 42 40 2 3
C
REC 2
C
PNT 0 34 40 2 4
PNT 40 34 40 2 3
PNT 0 42 40 2 4
PNT 40 42 40 2 3
C
REC 2
C
PNT 40 34 88 2 4
PNT 40 42 88 2 4
C
REC 2
C
C --- FRAME 1.013: HOLD ON PASTURE ---
REC 8
C
C
C ============================================================
C  SEQ 2: HORSE AS ANCIENT TECHNOLOGY
C  DISSOLVE-MORPH: Pasture transforms into Roman road.
C  Horse gallops as environment changes through eras.
C  Road → railroad → highway → data centers
C  Each transformation = 4-frame dissolve.
C ============================================================
C
C --- FRAME 2.001: BEGIN DISSOLVE — grass dims ---
C Ground values step down from 3 to 2
PNT 0 22 128 60 2
PNT 0 82 128 14 3
C Sky holds
C
REC 3
C
C --- FRAME 2.002: ROMAN ROAD EMERGES — value 2 underneath ---
C Road surface ghost
PNT 30 30 68 40 2
C Stone paving ghost
PNT 34 34 4 4 1
PNT 42 38 4 4 1
PNT 50 34 4 4 1
PNT 58 38 4 4 1
PNT 66 34 4 4 1
PNT 74 38 4 4 1
PNT 82 34 4 4 1
C
C Calypso transforms — from grazing to galloping
C Erase old pose at value 2
PNT 34 32 24 36 2
C
REC 3
C
C --- FRAME 2.003: ROMAN ROAD SOLIDIFIES — horse gallops ---
C Road
PNT 30 30 68 40 4
PNT 32 32 64 36 3
C Paving stones
PNT 34 34 4 4 4
PNT 42 38 4 4 4
PNT 50 34 4 4 4
PNT 58 38 4 4 4
PNT 66 34 4 4 4
PNT 74 38 4 4 4
PNT 82 34 4 4 4
C
C GALLOPING HORSE — mid-stride
PNT 40 26 18 10 5
PNT 42 27 14 8 6
C Neck extended
PNT 36 20 6 10 5
PNT 37 22 4 6 6
C Head
PNT 32 18 6 4 5
PNT 33 19 4 2 6
PNT 34 19 1 1 7
C Ears back
PNT 32 16 2 3 6
C
C Legs — gallop extended
LIN 42 36 36 48 5
LIN 46 36 50 48 5
LIN 52 34 48 48 5
LIN 56 34 60 48 5
C
C Mane streaming
LIN 38 20 42 16 6
LIN 40 18 44 14 5
C
C Aqueduct arches — Roman era marker
PNT 0 12 12 18 3
PNT 2 16 8 12 2
PNT 4 20 4 4 1
C Arch 2
PNT 14 14 12 16 3
PNT 16 18 8 10 2
PNT 18 22 4 4 1
C
REC 4
C
C --- FRAME 2.004: WALK CYCLE FRAME ---
LIN 42 36 36 48 3
LIN 46 36 50 48 3
LIN 52 34 48 48 3
LIN 56 34 60 48 3
C New positions
LIN 42 36 38 48 5
LIN 46 36 48 48 5
LIN 52 34 50 48 5
LIN 56 34 58 48 5
C
REC 2
C
C --- FRAME 2.005: DISSOLVE — ROMAN → RAILROAD ---
C Roman elements fade to value 2
PNT 0 12 28 20 2
C Paving stones fade
PNT 34 34 4 4 3
PNT 50 34 4 4 3
PNT 66 34 4 4 3
PNT 82 34 4 4 3
C
REC 3
C
C --- FRAME 2.006: RAILROAD EMERGES ---
C Paving fully gone
PNT 34 34 52 8 3
C Railroad tracks emerge
LIN 30 46 98 46 5
LIN 30 48 98 48 5
C Cross ties
LIN 38 44 38 50 4
LIN 48 44 48 50 4
LIN 58 44 58 50 4
LIN 68 44 68 50 4
LIN 78 44 78 50 4
LIN 88 44 88 50 4
C
C Telegraph poles — era marker
LIN 20 14 20 46 4
LIN 18 14 22 14 3
LIN 100 16 100 46 4
LIN 98 16 102 16 3
LIN 20 16 100 18 2
C
C Steam in distance — train ghost
PNT 104 20 14 12 2
PNT 106 22 10 8 3
PNT 108 18 8 4 1
C
REC 4
C
C --- FRAME 2.007: HORSE KEEPS GALLOPING — timeless ---
LIN 42 36 38 48 3
LIN 46 36 48 48 3
LIN 52 34 50 48 3
LIN 56 34 58 48 3
C Return to extended
LIN 42 36 36 48 5
LIN 46 36 50 48 5
LIN 52 34 48 48 5
LIN 56 34 60 48 5
C
REC 2
C
C --- FRAME 2.008: DISSOLVE — RAILROAD → HIGHWAY ---
C Tracks fade
LIN 30 46 98 46 3
LIN 30 48 98 48 3
LIN 38 44 38 50 3
LIN 48 44 48 50 3
LIN 58 44 58 50 3
LIN 68 44 68 50 3
LIN 78 44 78 50 3
LIN 88 44 88 50 3
C Telegraph fades
PNT 18 14 4 34 2
PNT 96 14 6 34 2
C
REC 3
C
C Highway emerges — smooth asphalt
PNT 28 36 72 20 4
C Lane markings
PNT 40 46 6 2 2
PNT 54 46 6 2 2
PNT 68 46 6 2 2
PNT 82 46 6 2 2
C Streetlights
LIN 22 16 22 40 4
PNT 20 16 4 2 3
LIN 106 18 106 42 4
PNT 104 18 4 2 3
C
REC 4
C
C --- FRAME 2.009: DISSOLVE — HIGHWAY → DATA CENTERS ---
C Highway fades
PNT 28 36 72 20 3
PNT 40 46 6 2 3
PNT 54 46 6 2 3
PNT 68 46 6 2 3
PNT 82 46 6 2 3
C
REC 3
C
C Data centers emerge as blocky shapes on horizon
PNT 10 26 16 18 4
PNT 12 28 12 14 5
PNT 30 24 20 20 4
PNT 32 26 16 16 5
PNT 60 22 24 22 4
PNT 62 24 20 18 5
PNT 90 24 20 20 4
PNT 92 26 16 16 5
C Window lights
PNT 14 30 2 2 3
PNT 18 30 2 2 3
PNT 34 28 2 2 3
PNT 38 28 2 2 3
PNT 42 28 2 2 3
PNT 64 26 2 2 3
PNT 68 26 2 2 3
PNT 72 26 2 2 3
PNT 76 26 2 2 3
PNT 94 28 2 2 3
PNT 98 28 2 2 3
PNT 102 28 2 2 3
C
C Horse STILL galloping — through ALL eras
C Body unchanged — eternal constant
C
REC 6
C
C --- FRAME 2.010: HOLD — horse amid data centers ---
REC 6
C
C
C ============================================================
C  SEQ 3: THE MUYBRIDGE SEQUENCE
C  DISSOLVE from data centers back to racetrack.
C  Horse fractures into individual photographic frames
C  suspended in space. Frames expand outward.
C ============================================================
C
C --- FRAME 3.001: DISSOLVE — data centers dim ---
C Fade buildings
PNT 10 22 108 26 2
C Keep horse
C
REC 3
C
C --- FRAME 3.002: RACETRACK EMERGES ---
CLR 0
PNT 0 0 128 14 1
PNT 0 14 128 36 3
PNT 0 14 128 2 5
LIN 0 14 127 14 6
PNT 0 50 128 2 5
PNT 0 52 128 44 3
C
C Camera row — value 2 ghosts first
PNT 10 42 4 6 2
PNT 24 42 4 6 2
PNT 38 42 4 6 2
PNT 52 42 4 6 2
PNT 66 42 4 6 2
PNT 80 42 4 6 2
PNT 94 42 4 6 2
PNT 108 42 4 6 2
C
REC 3
C
C --- FRAME 3.003: CAMERAS SOLIDIFY ---
PNT 10 42 4 6 5
PNT 24 42 4 6 5
PNT 38 42 4 6 5
PNT 52 42 4 6 5
PNT 66 42 4 6 5
PNT 80 42 4 6 5
PNT 94 42 4 6 5
PNT 108 42 4 6 5
C Lens highlights
PNT 11 41 2 1 7
PNT 25 41 2 1 7
PNT 39 41 2 1 7
PNT 53 41 2 1 7
PNT 67 41 2 1 7
PNT 81 41 2 1 7
PNT 95 41 2 1 7
PNT 109 41 2 1 7
C Tripod legs
LIN 12 48 12 50 4
LIN 26 48 26 50 4
LIN 40 48 40 50 4
LIN 54 48 54 50 4
LIN 68 48 68 50 4
LIN 82 48 82 50 4
LIN 96 48 96 50 4
LIN 110 48 110 50 4
C
C Horse — sprinting position
PNT 4 22 14 8 6
PNT 6 23 10 6 7
PNT 2 18 4 6 6
PNT 0 16 4 4 6
PNT 1 17 2 2 7
PNT 0 14 2 3 7
C Legs extended
LIN 6 30 2 38 6
LIN 10 30 14 38 6
LIN 14 28 10 38 6
LIN 16 28 20 38 6
C
REC 4
C
C --- FRAME 3.004: CAMERA 1 FIRES — FLASH ---
PNT 11 41 2 1 0
C
REC 1
C
PNT 11 41 2 1 7
C
REC 1
C
C --- FRAME 3.005: HORSE MOVES — cameras fire sequentially ---
C Horse at camera 3
PNT 0 14 22 26 3
PNT 32 22 14 8 6
PNT 34 23 10 6 7
PNT 30 18 4 6 6
PNT 28 16 4 4 6
PNT 29 17 2 2 7
LIN 34 30 30 38 6
LIN 38 30 42 38 6
LIN 42 28 38 38 6
LIN 44 28 48 38 6
C
REC 1
C
PNT 39 41 2 1 0
C
REC 1
C
PNT 39 41 2 1 7
C
C Horse at camera 5
PNT 28 14 22 26 3
PNT 50 22 14 8 6
PNT 52 23 10 6 7
PNT 48 18 4 6 6
PNT 46 16 4 4 6
PNT 47 17 2 2 7
LIN 52 30 48 38 6
LIN 56 30 60 38 6
LIN 60 28 56 38 6
LIN 62 28 66 38 6
C
REC 1
C
PNT 53 41 2 1 0
C
REC 1
C
PNT 53 41 2 1 7
C
C Horse at camera 7
PNT 46 14 22 26 3
PNT 68 22 14 8 6
PNT 70 23 10 6 7
PNT 66 18 4 6 6
PNT 64 16 4 4 6
PNT 65 17 2 2 7
LIN 70 30 66 38 6
LIN 74 30 78 38 6
LIN 78 28 74 38 6
LIN 80 28 84 38 6
C
REC 1
C
PNT 67 41 2 1 0
C
REC 1
C
PNT 67 41 2 1 7
C
REC 1
C
C --- FRAME 3.006: HORSE FRACTURES — dissolve into frames ---
C Horse body breaks into separate rectangles
C Each rectangle = a photographic frame floating
PNT 64 14 22 26 3
C Frame 1 — top left
PNT 10 10 12 8 5
PNT 11 11 10 6 4
PNT 12 12 4 4 5
C Frame 2 — top center
PNT 30 8 12 8 5
PNT 31 9 10 6 4
PNT 32 10 4 4 6
C Frame 3 — top right
PNT 50 6 12 8 5
PNT 51 7 10 6 4
PNT 52 8 4 4 5
C Frame 4 — center
PNT 70 10 12 8 5
PNT 71 11 10 6 4
PNT 72 12 4 4 7
C Frame 5 — right
PNT 90 8 12 8 5
PNT 91 9 10 6 4
PNT 92 10 4 4 6
C Frame 6 — far right
PNT 110 6 12 8 5
PNT 111 7 10 6 4
PNT 112 8 4 4 5
C
REC 4
C
C --- FRAME 3.007: FRAMES EXPAND — dissolve outward ---
C Each frame value steps down — fading to ghost
PNT 10 10 12 8 4
PNT 30 8 12 8 4
PNT 50 6 12 8 4
PNT 70 10 12 8 4
PNT 90 8 12 8 4
PNT 110 6 12 8 4
C
REC 3
C
PNT 10 10 12 8 3
PNT 30 8 12 8 3
PNT 50 6 12 8 3
PNT 70 10 12 8 3
PNT 90 8 12 8 3
PNT 110 6 12 8 3
C
REC 3
C
PNT 10 10 12 8 2
PNT 30 8 12 8 2
PNT 50 6 12 8 2
PNT 70 10 12 8 2
PNT 90 8 12 8 2
PNT 110 6 12 8 2
C
REC 3
C
C --- FRAME 3.008: HOLD — frames as ghosts ---
REC 6
C
C
C ============================================================
C  SEQ 4: "WHO GATHERED THE HEAP?"
C  DISSOLVE from racetrack photos into a vast
C  landscape of books, text, cultural material.
C  Words lift off pages and become floating particles.
C  Particles spiral into neural network shape.
C ============================================================
C
C --- FRAME 4.001: DISSOLVE — everything fades ---
CLR 0
C Pure black with value-1 texture
PNT 0 0 128 96 0
C
REC 3
C
C --- FRAME 4.002: BOOKS MATERIALIZE — value by value ---
C Book shapes — value 1 ghosts
PNT 4 60 6 10 1
PNT 14 56 6 14 1
PNT 24 62 6 8 1
PNT 34 58 6 12 1
PNT 44 54 6 16 1
PNT 54 60 6 10 1
PNT 64 56 6 14 1
PNT 74 62 6 8 1
PNT 84 58 6 12 1
PNT 94 54 6 16 1
PNT 104 60 6 10 1
PNT 114 56 6 14 1
C
REC 3
C
C --- FRAME 4.003: BOOKS VALUE 2 ---
PNT 4 60 6 10 2
PNT 14 56 6 14 2
PNT 24 62 6 8 2
PNT 34 58 6 12 3
PNT 44 54 6 16 2
PNT 54 60 6 10 3
PNT 64 56 6 14 2
PNT 74 62 6 8 3
PNT 84 58 6 12 2
PNT 94 54 6 16 3
PNT 104 60 6 10 2
PNT 114 56 6 14 3
C Spine highlights
PNT 5 61 1 8 4
PNT 15 57 1 12 4
PNT 35 59 1 10 5
PNT 45 55 1 14 4
PNT 65 57 1 12 5
PNT 85 59 1 10 4
PNT 95 55 1 14 5
PNT 115 57 1 12 4
C
REC 4
C
C --- FRAME 4.004: WORDS LIFT OFF — particles rise ---
C Text particles — single pixels floating upward
PNT 8 56 1 1 3
PNT 18 52 1 1 3
PNT 28 58 1 1 3
PNT 38 54 1 1 3
PNT 48 50 1 1 3
PNT 58 56 1 1 3
PNT 68 52 1 1 3
PNT 78 58 1 1 3
PNT 88 54 1 1 3
PNT 98 50 1 1 3
PNT 108 56 1 1 3
PNT 118 52 1 1 3
C
REC 2
C
C --- FRAME 4.005: PARTICLES RISE HIGHER ---
PNT 8 56 1 1 0
PNT 18 52 1 1 0
PNT 28 58 1 1 0
PNT 38 54 1 1 0
PNT 48 50 1 1 0
PNT 58 56 1 1 0
PNT 68 52 1 1 0
PNT 78 58 1 1 0
PNT 88 54 1 1 0
PNT 98 50 1 1 0
PNT 108 56 1 1 0
PNT 118 52 1 1 0
C Higher positions
PNT 10 46 1 1 3
PNT 22 42 1 1 3
PNT 34 48 1 1 3
PNT 46 44 1 1 3
PNT 58 40 1 1 3
PNT 70 46 1 1 3
PNT 82 42 1 1 3
PNT 94 48 1 1 3
PNT 106 44 1 1 3
PNT 118 40 1 1 3
C
REC 2
C
C --- FRAME 4.006: PARTICLES SPIRAL TOWARD CENTER ---
PNT 10 46 1 1 0
PNT 22 42 1 1 0
PNT 34 48 1 1 0
PNT 46 44 1 1 0
PNT 58 40 1 1 0
PNT 70 46 1 1 0
PNT 82 42 1 1 0
PNT 94 48 1 1 0
PNT 106 44 1 1 0
PNT 118 40 1 1 0
C Converging toward center
PNT 40 30 1 1 3
PNT 50 26 1 1 3
PNT 60 32 1 1 3
PNT 70 28 1 1 3
PNT 80 30 1 1 3
PNT 55 24 1 1 4
PNT 65 22 1 1 4
PNT 75 26 1 1 4
C
REC 2
C
C --- FRAME 4.007: NEURAL NETWORK FORMS ---
C Clear particles
PNT 40 22 42 12 0
C Neural shape — dissolves in from center
PNT 56 28 16 8 3
PNT 60 30 8 4 4
PNT 62 32 4 2 5
C Connections radiating
LIN 56 28 48 22 2
LIN 72 28 80 22 2
LIN 56 36 48 42 2
LIN 72 36 80 42 2
LIN 64 28 64 20 2
LIN 64 36 64 44 2
C
REC 4
C
C --- FRAME 4.008: NETWORK PULSES ---
PNT 62 32 4 2 6
C
REC 2
C
PNT 62 32 4 2 5
C
REC 2
C
PNT 62 32 4 2 7
C
REC 2
C
PNT 62 32 4 2 5
C
REC 2
C
C --- FRAME 4.009: GIANT SILHOUETTE FORMS ---
C AI-shaped silhouette from human culture — value 2 outline
PNT 40 10 48 50 1
PNT 48 14 32 42 2
PNT 54 20 20 30 3
C Head shape
PNT 56 6 16 10 2
PNT 60 8 8 6 3
C
REC 6
C
C --- FRAME 4.010: HOLD — the silhouette ---
REC 6
C
C
C ============================================================
C  SEQ 5: LAW OF THE HORSE — SURREAL COURTROOM
C  DISSOLVE from AI silhouette into courtroom.
C  A horse stands in a beam of light at center.
C  Legal documents orbit around the horse.
C  The horse remains perfectly still.
C ============================================================
C
C --- FRAME 5.001: DISSOLVE — silhouette fades ---
PNT 40 6 48 56 1
PNT 48 14 32 42 1
PNT 54 20 20 30 1
PNT 56 6 16 10 1
C
REC 3
C
CLR 0
C
REC 2
C
C --- FRAME 5.002: COURTROOM FADES IN --- value by value ---
C Walls — ghost
PNT 0 0 128 30 1
C Floor — ghost
PNT 0 60 128 36 1
C
REC 3
C
C --- FRAME 5.003: COURTROOM SOLIDIFIES ---
PNT 0 0 128 20 2
PNT 0 20 128 10 3
LIN 0 20 127 20 4
PNT 0 60 128 36 3
PNT 0 62 128 2 4
PNT 0 70 128 2 2
PNT 0 78 128 2 4
C
C Bookshelves — towering
PNT 0 4 16 26 4
PNT 2 6 12 22 5
PNT 112 4 16 26 4
PNT 114 6 12 22 5
C Book spines
PNT 3 7 2 6 3
PNT 6 7 2 6 4
PNT 9 7 2 6 6
PNT 12 7 2 6 3
PNT 115 7 2 6 4
PNT 118 7 2 6 3
PNT 121 7 2 6 6
PNT 124 7 2 6 4
C
C --- BEAM OF LIGHT — center column ---
PNT 52 0 24 60 1
PNT 56 2 16 56 2
PNT 60 4 8 52 1
C
C --- HORSE IN LIGHT BEAM — perfectly still ---
C Body — illuminated
PNT 50 32 20 10 5
PNT 52 33 16 8 6
C Neck
PNT 48 22 4 12 5
PNT 49 24 2 8 6
C Head — still, centered
PNT 44 18 8 6 5
PNT 45 19 6 4 6
PNT 47 20 1 1 7
C Ears
PNT 44 16 2 3 6
PNT 48 16 2 3 6
C Legs — motionless standing
LIN 52 42 52 56 5
LIN 54 42 54 56 6
LIN 58 42 58 56 5
LIN 60 42 60 56 6
LIN 62 40 62 56 5
LIN 64 40 64 56 6
C Hooves
PNT 51 56 2 2 6
PNT 57 56 2 2 6
PNT 61 56 2 2 6
C
C --- ORBITING DOCUMENTS — at different heights ---
C Doc 1 — left
PNT 24 28 8 6 4
PNT 25 29 6 4 5
LIN 26 30 30 30 3
LIN 26 32 29 32 3
C Doc 2 — right
PNT 84 24 8 6 4
PNT 85 25 6 4 5
LIN 86 26 90 26 3
LIN 86 28 89 28 3
C Doc 3 — upper
PNT 56 8 8 6 4
PNT 57 9 6 4 5
LIN 58 10 62 10 3
LIN 58 12 61 12 3
C
C Figures seated — judges, authors, musicians
PNT 20 44 6 10 4
PNT 34 42 6 12 4
PNT 80 44 6 10 4
PNT 96 42 6 12 4
PNT 108 44 6 10 4
C
REC 8
C
C --- FRAME 5.004: DOCUMENTS ORBIT — positions shift ---
C Doc 1 moves right
PNT 24 28 8 6 2
PNT 30 30 8 6 4
PNT 31 31 6 4 5
C Doc 2 moves down
PNT 84 24 8 6 2
PNT 82 32 8 6 4
PNT 83 33 6 4 5
C Doc 3 moves left
PNT 56 8 8 6 2
PNT 44 10 8 6 4
PNT 45 11 6 4 5
C
REC 3
C
C --- FRAME 5.005: DOCUMENTS CONTINUE ORBIT ---
PNT 30 30 8 6 2
PNT 38 34 8 6 4
PNT 82 32 8 6 2
PNT 78 38 8 6 4
PNT 44 10 8 6 2
PNT 32 14 8 6 4
C
REC 3
C
C --- FRAME 5.006: DOCUMENTS FADE — orbit completes ---
PNT 38 34 8 6 3
PNT 78 38 8 6 3
PNT 32 14 8 6 3
C
REC 2
C
PNT 38 34 8 6 2
PNT 78 38 8 6 2
PNT 32 14 8 6 2
C
REC 2
C
C Restore original positions
PNT 38 34 8 6 1
PNT 78 38 8 6 1
PNT 32 14 8 6 1
PNT 24 28 8 6 4
PNT 84 24 8 6 4
PNT 56 8 8 6 4
C
REC 4
C
C --- FRAME 5.007: HORSE STILL — beam flickers ---
PNT 60 4 8 52 2
C
REC 2
C
PNT 60 4 8 52 1
C
REC 2
C
C --- FRAME 5.008: HOLD — horse perfectly still ---
REC 10
C
C
C ============================================================
C  SEQ 6: FUTURE INFRASTRUCTURE
C  DISSOLVE from courtroom → data center → peaceful pasture.
C  AI powers everything invisibly. Nobody notices.
C  Final dissolve: data center → sunset pasture.
C ============================================================
C
C --- FRAME 6.001: COURTROOM DISSOLVES ---
C Everything steps down one value
PNT 0 0 128 20 1
PNT 0 20 128 10 2
PNT 0 60 128 36 2
C Horse fades
PNT 44 16 28 42 2
C
REC 3
C
C All to 1
PNT 0 0 128 96 1
C
REC 3
C
C --- FRAME 6.002: DATA CENTER INTERIOR EMERGES ---
CLR 0
PNT 0 0 128 96 0
C Server racks — value 1 first
PNT 4 10 16 70 1
PNT 24 10 16 70 1
PNT 44 10 16 70 1
PNT 68 10 16 70 1
PNT 88 10 16 70 1
PNT 108 10 16 70 1
C
REC 3
C
C --- FRAME 6.003: RACKS SOLIDIFY ---
PNT 4 10 16 70 3
PNT 24 10 16 70 4
PNT 44 10 16 70 3
PNT 68 10 16 70 4
PNT 88 10 16 70 3
PNT 108 10 16 70 4
C LEDs
PNT 18 20 1 1 3
PNT 18 30 1 1 2
PNT 18 40 1 1 3
PNT 18 50 1 1 2
PNT 18 60 1 1 3
PNT 38 20 1 1 2
PNT 38 30 1 1 3
PNT 38 40 1 1 2
PNT 82 20 1 1 3
PNT 82 30 1 1 2
PNT 82 40 1 1 3
PNT 102 20 1 1 2
PNT 102 30 1 1 3
PNT 102 40 1 1 2
C
REC 4
C
C --- FRAME 6.004: LED PULSE ---
PNT 18 20 1 1 4
PNT 38 30 1 1 4
PNT 82 40 1 1 4
PNT 102 20 1 1 4
C
REC 1
C
PNT 18 20 1 1 3
PNT 38 30 1 1 3
PNT 82 40 1 1 3
PNT 102 20 1 1 2
C
REC 2
C
C --- FRAME 6.005: DISSOLVE — data center → pasture ---
C Racks fade to 2
PNT 4 10 16 70 2
PNT 24 10 16 70 2
PNT 44 10 16 70 2
PNT 68 10 16 70 2
PNT 88 10 16 70 2
PNT 108 10 16 70 2
C
REC 3
C
C --- FRAME 6.006: PASTURE GHOSTS THROUGH ---
C Sky value 1 emerging
PNT 0 0 128 16 1
C Grass value 1
PNT 0 16 128 80 1
C
C Racks fade further to 1
PNT 4 10 16 70 1
PNT 24 10 16 70 1
PNT 44 10 16 70 1
PNT 68 10 16 70 1
PNT 88 10 16 70 1
PNT 108 10 16 70 1
C
REC 3
C
C --- FRAME 6.007: PASTURE TAKES OVER ---
C Racks gone
PNT 0 0 128 16 2
PNT 0 12 128 6 1
PNT 0 18 128 78 3
PNT 0 22 128 2 2
PNT 0 30 128 2 4
PNT 0 38 128 2 2
PNT 0 46 128 2 4
PNT 0 54 128 2 2
PNT 0 62 128 2 4
PNT 0 70 128 2 2
PNT 0 78 128 2 4
C Foreground
PNT 0 82 128 14 4
C
C Sunset colors
PNT 0 12 128 4 2
C
C Calypso — grazing peacefully, FINAL IMAGE
PNT 44 44 16 8 5
PNT 46 45 12 6 6
PNT 42 36 4 10 5
PNT 38 38 6 4 5
PNT 39 39 4 2 6
PNT 40 39 1 1 7
PNT 38 36 2 3 6
LIN 48 52 48 64 5
LIN 50 52 50 64 6
LIN 54 52 54 64 5
LIN 56 50 56 64 5
LIN 58 50 58 64 6
PNT 47 64 2 2 6
PNT 53 64 2 2 6
PNT 57 64 2 2 6
LIN 60 44 64 40 5
C
REC 8
C
C --- FRAME 6.008: CALYPSO CHEWS ---
PNT 38 40 2 2 4
C
REC 2
C
PNT 38 40 2 2 5
C
REC 3
C
C --- FRAME 6.009: HOLD ON PASTURE —- technology invisible ---
REC 12
C
C
C ============================================================
C  SEQ 7: FINAL METAPHOR — "THE DANGER IS THAT WE WILL"
C  DISSOLVE: peaceful pasture darkens.
C  A massive cart appears. Humans pull it.
C  Humans MORPH into horse shapes — gradual dissolve.
C  In the distance, one free horse stands in green.
C ============================================================
C
C --- FRAME 7.001: PASTURE DARKENS — value steps down ---
PNT 0 0 128 16 1
PNT 0 12 128 4 1
PNT 0 18 128 78 2
PNT 0 82 128 14 3
C Calypso fades
PNT 38 36 24 30 2
C
REC 3
C
C --- FRAME 7.002: BARREN LANDSCAPE ---
PNT 0 0 128 20 1
PNT 0 20 128 76 2
PNT 0 80 128 16 3
C
REC 3
C
C --- FRAME 7.003: MASSIVE CART FADES IN ---
C Cart — value 3 ghost
PNT 50 24 40 20 3
PNT 52 26 36 16 4
C Cargo — glowing AI systems
PNT 56 26 12 8 5
PNT 60 28 4 4 3
PNT 72 26 12 8 5
PNT 76 28 4 4 3
C Wheels
PNT 54 42 8 8 4
PNT 56 44 4 4 5
PNT 80 42 8 8 4
PNT 82 44 4 4 5
C
REC 4
C
C --- FRAME 7.004: HUMANS PULLING CART — harness visible ---
C Figure 1 — human shape
PNT 26 30 6 14 4
PNT 28 32 2 10 5
PNT 28 24 4 6 4
PNT 29 25 2 4 5
C Arms pulling rope
LIN 32 34 40 30 5
LIN 40 30 50 26 4
C Legs straining
LIN 28 44 26 54 4
LIN 30 44 32 54 4
C
C Figure 2 — human shape
PNT 14 32 6 12 4
PNT 16 34 2 8 5
PNT 16 26 4 6 4
PNT 17 27 2 4 5
C Arms pulling
LIN 20 36 26 32 5
C Legs
LIN 16 44 14 54 4
LIN 18 44 20 54 4
C
C Harness ropes — taut
LIN 20 36 32 34 4
LIN 32 34 50 28 4
C
REC 6
C
C --- FRAME 7.005: HUMANS BEGIN MORPH — limbs thicken ---
C Figure 1 — body widens, neck extends
PNT 26 30 6 14 5
PNT 26 28 4 8 4
C Head elongates forward
PNT 24 24 8 6 4
PNT 25 25 6 4 5
C
C Figure 2 — same transformation
PNT 14 32 6 12 5
PNT 14 30 4 8 4
PNT 12 26 8 6 4
PNT 13 27 6 4 5
C
REC 4
C
C --- FRAME 7.006: MORPH DEEPENS — becoming horse-shaped ---
C Figure 1 — clearly equine now
PNT 24 24 8 6 5
PNT 25 25 6 4 6
PNT 22 22 4 4 5
PNT 23 23 2 2 6
PNT 22 20 2 3 6
C Four legs replacing two
PNT 26 44 2 12 5
PNT 28 44 2 12 5
PNT 30 44 2 12 5
PNT 32 44 2 12 5
C
C Figure 2 — equine
PNT 12 26 8 6 5
PNT 13 27 6 4 6
PNT 10 24 4 4 5
PNT 11 25 2 2 6
PNT 10 22 2 3 6
PNT 14 44 2 12 5
PNT 16 44 2 12 5
PNT 18 44 2 12 5
PNT 20 44 2 12 5
C
REC 4
C
C --- FRAME 7.007: MORPH COMPLETE — humans are horses ---
C Both figures now clearly horses in harness
C Cart grows heavier — glows brighter
PNT 56 26 12 8 6
PNT 72 26 12 8 6
PNT 60 28 4 4 7
PNT 76 28 4 4 7
C
C Sky fills with data streams — digital constellation
PNT 20 4 2 2 2
PNT 40 6 2 2 2
PNT 60 2 2 2 2
PNT 80 8 2 2 2
PNT 100 4 2 2 2
LIN 21 5 41 7 1
LIN 41 7 61 3 1
LIN 61 3 81 9 1
LIN 81 9 101 5 1
C
REC 6
C
C --- FRAME 7.008: DISTANT FREE HORSE — value 2 ghost ---
C Far right — a small horse shape in a green patch
PNT 104 48 12 8 2
PNT 106 50 8 4 3
C Tiny horse — free
PNT 108 44 6 4 3
PNT 110 42 2 4 3
PNT 108 40 3 3 3
PNT 108 41 1 1 4
C Green patch — untouched
PNT 102 46 16 12 2
C
REC 6
C
C --- FRAME 7.009: FREE HORSE BRIGHTENS — hope ---
PNT 108 44 6 4 4
PNT 110 42 2 4 4
PNT 108 40 3 3 4
PNT 108 41 1 1 5
PNT 102 46 16 12 3
C
REC 4
C
C --- FRAME 7.010: SLOW DISSOLVE TO BLACK ---
C Step 1 — everything drops one value
PNT 0 0 128 20 0
PNT 50 24 40 28 2
PNT 0 20 128 60 1
PNT 102 46 16 12 2
C
REC 4
C
C Step 2 — deeper
PNT 50 24 40 28 1
PNT 0 20 128 60 0
PNT 102 46 16 12 1
C Stars remain
C
REC 4
C
C Step 3 — near black
PNT 50 24 40 28 0
PNT 102 46 16 12 0
PNT 20 4 2 2 1
PNT 40 6 2 2 1
PNT 60 2 2 2 1
PNT 80 8 2 2 1
PNT 100 4 2 2 1
C
REC 4
C
C Step 4 — total black
CLR 0
C
REC 6
C
C --- FRAME 7.011: FINAL TITLE — dissolves in ---
LIN 20 42 108 42 1
LIN 24 44 104 44 1
C
REC 3
C
LIN 20 42 108 42 2
LIN 24 44 104 44 2
C
REC 3
C
LIN 20 42 108 42 3
LIN 24 44 104 44 3
C
REC 6
C
C --- FRAME 7.012: TITLE DISSOLVES OUT ---
LIN 20 42 108 42 2
LIN 24 44 104 44 2
C
REC 3
C
LIN 20 42 108 42 1
LIN 24 44 104 44 1
C
REC 3
C
CLR 0
C
REC 6
C
C ============================================================
C  END: hh7.md — DISSOLVE/MORPH STYLE
C  ALL transitions are gradual value shifts.
C  NO hard cuts in entire film.
C  7 SEQUENCES / ~120 FRAMES
C ============================================================
