C ============================================================
C  SHE'S JUST A HAPPY HORSE — hh3.md
C  SOURCE: hhs3.md (Scene blueprints: 4 characters × 3 states)
C  128x96 / 8 GRAYSCALE / BEFLIX
C
C  RENDERING STYLE: ISOMETRIC / ARCHITECTURAL BLUEPRINT
C  -----------------------------------------------------
C  Everything drawn on a 45° isometric grid.
C  All shapes are diamond/rhombus forms — no flat views.
C  Objects seen from elevated 3/4 angle.
C  Grid lines visible as value 1 underlay.
C  Figures = stacked isometric blocks.
C  Environment = extruded floor planes.
C  BLUEPRINT AESTHETIC: grid lines, measurement marks,
C  annotation lines radiating from objects.
C  Like an architectural rendering or SimCity.
C
C  4 CHARACTERS × 3 TEMPORAL STATES:
C  DARIO — Previous / Current / Update
C  CALYPSO — Previous / Current / Update
C  NARRATOR — Previous / Current / Update
C  HUMANITY — Previous / Current / Update
C ============================================================
C
C
C ============================================================
C  PANEL 1: DARIO — PREVIOUS STATE
C  "Conference rooms, policy forums, screens, reports"
C  Isometric office interior — stacked block figure
C ============================================================
C
C --- FRAME 1.001: ISOMETRIC GRID UNDERLAY ---
CLR 0
C Grid lines — value 1, isometric pattern
C Horizontal iso-lines (diagonal right-down)
LIN 0 0 64 32 1
LIN 0 8 64 40 1
LIN 0 16 64 48 1
LIN 0 24 64 56 1
LIN 0 32 64 64 1
LIN 0 40 64 72 1
LIN 0 48 64 80 1
LIN 0 56 64 88 1
LIN 0 64 64 96 1
C Horizontal iso-lines (diagonal left-down)
LIN 127 0 64 32 1
LIN 127 8 64 40 1
LIN 127 16 64 48 1
LIN 127 24 64 56 1
LIN 127 32 64 64 1
LIN 127 40 64 72 1
LIN 127 48 64 80 1
LIN 127 56 64 88 1
LIN 127 64 64 96 1
C
C --- ISOMETRIC FLOOR PLANE ---
C Diamond floor — value 2
PNT 30 50 68 30 2
C Floor edges — bright
LIN 30 64 64 80 3
LIN 64 80 98 64 3
LIN 98 64 64 48 3
LIN 64 48 30 64 3
C
C --- ISOMETRIC DESK — extruded block ---
C Top face — diamond
PNT 48 44 24 8 3
LIN 48 48 60 54 4
LIN 60 54 72 48 4
LIN 72 48 60 42 4
LIN 60 42 48 48 4
C Left face — darker
PNT 48 48 12 8 4
C Right face
PNT 60 48 12 8 3
C
C Screen on desk — bright face
PNT 54 38 8 6 5
PNT 55 39 6 4 3
LIN 56 40 60 40 2
LIN 56 42 59 42 2
C
C --- DARIO FIGURE — stacked iso-blocks ---
C Body block — iso cube
PNT 76 36 10 12 4
LIN 76 36 82 42 5
LIN 82 42 86 40 5
LIN 86 40 80 34 5
LIN 80 34 76 36 5
C Left face
PNT 76 42 6 8 4
C Right face
PNT 82 42 4 8 3
C
C Head block — smaller iso cube on top
PNT 78 28 6 8 4
LIN 78 28 82 32 5
LIN 82 32 84 30 5
LIN 84 30 80 26 5
LIN 80 26 78 28 5
C Eyes
PNT 80 30 1 1 7
PNT 82 30 1 1 7
C
C --- ANNOTATION LINES — blueprint style ---
LIN 88 34 100 28 2
LIN 100 28 110 28 2
LIN 88 42 100 46 2
LIN 100 46 110 46 2
C Measurement marks
PNT 100 26 1 1 3
PNT 100 28 1 1 3
PNT 100 44 1 1 3
PNT 100 46 1 1 3
C
C --- POLICY DOCUMENTS — small iso rectangles on desk ---
PNT 50 44 4 3 5
PNT 56 44 4 3 5
PNT 62 44 4 3 5
C
REC 8
C
C --- FRAME 1.002: SCREEN FLICKER ---
PNT 55 39 6 4 4
C
REC 2
C
PNT 55 39 6 4 3
C
REC 2
C
C --- FRAME 1.003: DARIO HEAD TURNS ---
PNT 78 28 6 8 3
PNT 77 28 6 8 4
LIN 77 28 81 32 5
PNT 79 30 1 1 7
PNT 81 30 1 1 7
C
REC 3
C
PNT 77 28 6 8 3
PNT 78 28 6 8 4
LIN 78 28 82 32 5
PNT 80 30 1 1 7
PNT 82 30 1 1 7
C
REC 3
C
C --- FRAME 1.004: HOLD ---
REC 6
C
C
C ============================================================
C  PANEL 2: CALYPSO — CURRENT STATE
C  "A tranquil pasture, scent of grass and soil"
C  Isometric landscape — horse as iso-block
C ============================================================
C
C --- FRAME 2.001: NEW GRID ---
CLR 0
C Isometric grid — lighter for outdoor
LIN 0 0 64 32 1
LIN 0 16 64 48 1
LIN 0 32 64 64 1
LIN 0 48 64 80 1
LIN 127 0 64 32 1
LIN 127 16 64 48 1
LIN 127 32 64 64 1
LIN 127 48 64 80 1
C
C --- ISOMETRIC GRASS PLANE --- large diamond
PNT 10 40 108 40 2
LIN 10 60 64 88 3
LIN 64 88 118 60 3
LIN 118 60 64 32 3
LIN 64 32 10 60 3
C
C Grass texture — isometric hatch
LIN 20 56 34 64 2
LIN 40 48 54 56 2
LIN 60 44 74 52 2
LIN 80 48 94 56 2
LIN 100 52 114 60 2
C
C --- FENCE — isometric posts and rails ---
C Posts — vertical iso sticks
LIN 90 38 90 50 4
LIN 100 42 100 54 4
LIN 110 46 110 58 4
C Top rail — iso diagonal
LIN 90 40 100 44 3
LIN 100 44 110 48 3
C Bottom rail
LIN 90 46 100 50 3
LIN 100 50 110 54 3
C
C --- CALYPSO — ISOMETRIC HORSE ---
C Body — iso block, wider than tall
PNT 32 42 24 10 4
LIN 32 42 44 48 5
LIN 44 48 56 44 5
LIN 56 44 44 38 5
LIN 44 38 32 42 5
C Left side — darker
PNT 32 48 12 6 5
C Right side
PNT 44 48 12 6 4
C
C Neck — angled iso block
PNT 28 34 8 10 5
LIN 28 34 34 38 6
LIN 34 38 36 36 6
LIN 36 36 30 32 6
C
C Head — small iso block
PNT 24 30 8 6 4
LIN 24 30 28 33 5
LIN 28 33 32 31 5
LIN 32 31 28 28 5
LIN 28 28 24 30 5
C Eye
PNT 27 31 1 1 7
C Ears — tiny iso peaks
PNT 25 28 2 2 6
PNT 29 27 2 2 6
C
C Legs — iso columns
LIN 36 52 36 62 5
LIN 38 52 38 62 5
LIN 44 52 44 62 5
LIN 46 52 46 62 5
LIN 50 50 50 60 5
LIN 52 50 52 60 5
C Hooves — iso blocks
PNT 35 62 4 2 6
PNT 43 62 4 2 6
PNT 49 60 4 2 6
C
C Tail — iso line
LIN 56 42 60 38 4
LIN 60 38 62 40 3
C
C Shadow — iso diamond on ground
PNT 34 60 20 6 3
LIN 34 64 44 70 2
LIN 44 70 54 66 2
LIN 54 66 44 60 2
C
C --- ANNOTATION ---
LIN 58 36 68 30 2
LIN 68 30 80 30 2
C "Calypso" marker dot
PNT 68 28 1 1 3
PNT 68 30 1 1 3
C
C --- DARIO iso-block — small, on fence ---
PNT 96 34 6 8 4
PNT 98 30 4 4 4
PNT 98 28 4 3 5
PNT 99 30 1 1 7
PNT 101 30 1 1 7
C
REC 8
C
C --- FRAME 2.002: CALYPSO TAIL FLICK ---
LIN 56 42 60 38 2
LIN 56 42 58 36 4
C
REC 3
C
LIN 56 42 58 36 2
LIN 56 42 60 38 4
C
REC 3
C
C --- FRAME 2.003: CALYPSO WEIGHT SHIFT ---
C Left legs shift
LIN 36 52 36 62 3
LIN 35 52 35 60 5
C
REC 3
C
LIN 35 52 35 60 3
LIN 36 52 36 62 5
C
REC 3
C
C --- FRAME 2.004: HOLD ---
REC 8
C
C
C ============================================================
C  PANEL 3: NARRATOR — CURRENT STATE
C  "Conceptual landscape moving between myth, law,
C  AI labs, and rural pastures"
C  ISOMETRIC MULTI-LEVEL: 4 stacked iso-planes
C ============================================================
C
C --- FRAME 3.001: STACKED ISO WORLDS ---
CLR 0
C Grid
LIN 0 0 64 32 1
LIN 0 24 64 56 1
LIN 0 48 64 80 1
LIN 127 0 64 32 1
LIN 127 24 64 56 1
LIN 127 48 64 80 1
C
C --- LAYER 1 (top): MYTHIC — small iso-plane ---
PNT 42 6 44 14 2
LIN 42 12 64 22 3
LIN 64 22 86 12 3
LIN 86 12 64 2 3
LIN 64 2 42 12 3
C Nymph — tiny iso cube
PNT 50 8 4 4 4
PNT 52 9 1 1 7
C Odysseus — tiny iso cube
PNT 72 8 4 4 4
PNT 74 9 1 1 7
C Connector line down to next layer
LIN 64 22 64 28 2
C
C --- LAYER 2: LEGAL — iso-plane ---
PNT 34 24 60 16 2
LIN 34 32 64 46 3
LIN 64 46 94 32 3
LIN 94 32 64 18 3
LIN 64 18 34 32 3
C Gavel — tiny
PNT 58 26 4 3 4
PNT 60 27 1 1 7
C Book stacks
PNT 42 28 3 3 5
PNT 48 28 3 3 5
C Laptop
PNT 78 28 3 3 5
PNT 79 29 1 1 3
C Connector
LIN 64 46 64 52 2
C
C --- LAYER 3: AI LAB — iso-plane ---
PNT 28 48 72 16 2
LIN 28 56 64 72 3
LIN 64 72 100 56 3
LIN 100 56 64 40 3
LIN 64 40 28 56 3
C Server blocks — small iso
PNT 38 52 4 4 4
PNT 48 54 4 4 4
PNT 58 52 4 4 4
C LED dots
PNT 40 53 1 1 3
PNT 50 55 1 1 3
PNT 60 53 1 1 3
C Dashboard
PNT 80 52 6 4 3
PNT 81 53 4 2 4
C Connector
LIN 64 72 64 78 2
C
C --- LAYER 4 (bottom): PASTURE — iso-plane ---
PNT 22 72 84 18 2
LIN 22 82 64 96 3
LIN 64 96 106 82 3
LIN 106 82 64 66 3
LIN 64 66 22 82 3
C Calypso tiny
PNT 54 76 6 4 4
PNT 55 77 1 1 7
C Grass dots
PNT 36 80 1 1 3
PNT 46 82 1 1 3
PNT 68 78 1 1 3
PNT 78 80 1 1 3
PNT 88 82 1 1 3
C
C --- NARRATOR — iso figure floating between layers ---
PNT 110 38 6 10 4
PNT 112 34 4 6 4
PNT 112 32 4 3 5
PNT 113 34 1 1 7
PNT 115 34 1 1 7
C Pen in hand
LIN 108 42 106 46 3
C Connection lines to all layers — annotation
LIN 108 38 86 12 1
LIN 108 42 94 32 1
LIN 108 46 100 56 1
LIN 108 50 106 82 1
C
REC 10
C
C --- FRAME 3.002: LEDs BLINK ---
PNT 40 53 1 1 4
PNT 60 53 1 1 4
C
REC 2
C
PNT 40 53 1 1 3
PNT 60 53 1 1 3
C
REC 2
C
C --- FRAME 3.003: HOLD ---
REC 8
C
C
C ============================================================
C  PANEL 4: HUMANITY — UPDATE STATE
C  "AI embedded in everyday institutions"
C  Isometric cityscape — AI infrastructure invisible
C ============================================================
C
C --- FRAME 4.001: ISOMETRIC CITY ---
CLR 0
C Grid
LIN 0 0 64 32 1
LIN 0 24 64 56 1
LIN 0 48 64 80 1
LIN 127 0 64 32 1
LIN 127 24 64 56 1
LIN 127 48 64 80 1
C
C --- CITY GROUND PLANE ---
PNT 10 50 108 36 2
LIN 10 68 64 96 3
LIN 64 96 118 68 3
LIN 118 68 64 40 3
LIN 64 40 10 68 3
C
C --- BUILDINGS — isometric blocks, varied heights ---
C Building 1 — tall
PNT 20 24 12 30 4
LIN 20 24 28 28 5
LIN 28 28 32 26 5
LIN 32 26 24 22 5
C Windows — grid
PNT 22 28 2 2 3
PNT 22 34 2 2 3
PNT 22 40 2 2 3
PNT 22 46 2 2 3
PNT 26 28 2 2 3
PNT 26 34 2 2 3
PNT 26 40 2 2 3
C
C Building 2 — medium
PNT 36 32 12 22 4
LIN 36 32 42 36 5
LIN 42 36 48 34 5
C Windows
PNT 38 36 2 2 3
PNT 38 42 2 2 3
PNT 42 36 2 2 3
C
C Building 3 — short
PNT 52 40 12 14 4
LIN 52 40 58 44 5
LIN 58 44 64 42 5
C Windows
PNT 54 44 2 2 3
PNT 58 44 2 2 3
C
C Building 4 — tall right
PNT 80 26 12 28 4
LIN 80 26 86 30 5
LIN 86 30 92 28 5
C Windows
PNT 82 30 2 2 3
PNT 82 36 2 2 3
PNT 82 42 2 2 3
PNT 86 30 2 2 3
PNT 86 36 2 2 3
C
C Building 5 — medium right
PNT 96 34 12 20 4
LIN 96 34 102 38 5
LIN 102 38 108 36 5
C Windows
PNT 98 38 2 2 3
PNT 98 44 2 2 3
C
C --- PEOPLE dots — walking on ground plane ---
PNT 44 56 1 1 5
PNT 56 58 1 1 5
PNT 68 54 1 1 5
PNT 76 60 1 1 5
PNT 88 56 1 1 5
C
C --- PARK — green iso-diamond ---
PNT 60 60 16 10 3
C Trees — small iso peaks
PNT 62 58 3 3 4
PNT 68 58 3 3 4
PNT 74 60 3 3 4
C
C --- ANNOTATION: "AI INVISIBLE" ---
LIN 4 20 16 14 2
LIN 16 14 40 14 2
PNT 4 18 1 1 3
PNT 16 12 1 1 3
C
C --- DATA INFRASTRUCTURE HIDDEN UNDERGROUND ---
C Dotted line showing underground layer
LIN 30 70 40 76 1
LIN 44 76 54 82 1
LIN 58 82 68 88 1
C Underground server — faint iso block
PNT 50 82 8 6 1
PNT 52 84 4 2 2
C
REC 8
C
C --- FRAME 4.002: WINDOW LIGHTS CYCLE ---
PNT 22 28 2 2 4
PNT 38 36 2 2 4
PNT 82 30 2 2 4
C
REC 2
C
PNT 22 28 2 2 3
PNT 38 36 2 2 3
PNT 82 30 2 2 3
PNT 26 34 2 2 4
PNT 42 36 2 2 4
PNT 86 36 2 2 4
C
REC 2
C
PNT 26 34 2 2 3
PNT 42 36 2 2 3
PNT 86 36 2 2 3
C
REC 2
C
C --- FRAME 4.003: PEOPLE WALK ---
PNT 44 56 1 1 0
PNT 56 58 1 1 0
PNT 68 54 1 1 0
PNT 76 60 1 1 0
PNT 88 56 1 1 0
C New positions
PNT 46 57 1 1 5
PNT 58 59 1 1 5
PNT 70 55 1 1 5
PNT 78 61 1 1 5
PNT 90 57 1 1 5
C
REC 3
C
C --- FRAME 4.004: UNDERGROUND PULSE ---
PNT 52 84 4 2 3
C
REC 2
C
PNT 52 84 4 2 2
C
REC 2
C
C --- FRAME 4.005: HOLD — AI invisible, life continues ---
REC 10
C
C ============================================================
C  END: hh3.md — ISOMETRIC / ARCHITECTURAL BLUEPRINT
C  ALL forms as 45° isometric blocks and diamonds.
C  Visible grid underlay. Annotation lines.
C  Measurement marks. Multi-level stacked planes.
C  4 PANELS / ~25 FRAMES
C ============================================================
