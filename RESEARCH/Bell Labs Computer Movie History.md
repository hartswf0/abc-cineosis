# Pioneering Pixels: The Genesis of Computer Animation and Digital Art at Bell Telephone Laboratories

## Introduction: The Epistemological Shift in Information Display

In the early 1960s, the trajectory of computational science underwent a
profound metamorphosis at Bell Telephone Laboratories in Murray Hill,
New Jersey. Originally engineered to execute complex numerical
calculations, process ballistics trajectories, and optimize
telecommunications routing, the mainframe computer was abruptly
repurposed as an engine for dynamic visual synthesis.^1^ This transition
was not merely a convenient technological upgrade; it represented a
fundamental epistemological shift in how human beings interacted with,
processed, and understood vast quantities of data. As high-speed digital
computers, such as the IBM 7090 and 7094 series, became capable of
executing millions of operations per second, they precipitated what
researchers colloquially referred to as a \"data flood\"---an
overwhelming deluge of continuous alphanumeric output that vastly
exceeded the cognitive processing bandwidth of human analysts.^3^

The solution to this data flood emerged at the intersection of
electrical engineering, higher mathematics, visual psychology, and
experimental art. Researchers at Bell Labs recognized that by
translating raw numerical matrices into sequences of geometric
visualizations, and subsequently recording these visual states onto
motion picture film, the human visual cortex could intuitively grasp
complex physical and mathematical behaviors that would otherwise remain
opaque within stacks of printouts.^3^ This realization birthed the
discipline of computer animation.

Between 1963 and 1969, an unprecedented convergence of scientific
inquiry and avant-garde aesthetics took place within the industrial
laboratories of Bell Labs.^1^ Engineers such as Edward E. Zajac and
Kenneth C. Knowlton developed the foundational software architectures
and optical pipelines that allowed computers to render moving images.^3^
Simultaneously, perceptual researchers like Leon Harmon investigated the
physiological limits of human vision through digital image processing,
leading to the invention of digital halftoning, gray-scale synthesis,
and algorithmic photomosaics.^6^ These technical breakthroughs rapidly
attracted the attention of the artistic avant-garde, culminating in
historic collaborations with experimental filmmakers like Stan
VanDerBeek and Lillian Schwartz.^8^ Through the development of
Domain-Specific Languages (DSLs) for graphics, Bell Labs democratized
the mainframe, transforming it from a hermetic calculator into a
revolutionary medium for both scientific visualization and contemporary
art.^10^

This exhaustive report provides a granular analysis of the pioneering
computer movie sources originating from Bell Telephone Laboratories. It
dissects the mathematical models of early satellite simulations, the
programmatic architecture of the first animation languages, the
perceptual psychology underlying early gray-scale synthesis, and the
profound cultural impact of the resulting digital artworks that
redefined the boundaries between the mechanical and the aesthetic.

## The Mathematical Foundation: Orbital Dynamics and the Gravity-Gradient Model

The genesis of computer animation is inextricably linked to the
aerospace challenges of the Cold War era. In the early 1960s, Bell Labs
was deeply engaged in the design of passive gravity-gradient attitude
control systems for communication satellites.^11^ The core principle of
a gravity-gradient system relies on the physical reality that the
Earth\'s gravitational field varies slightly over the length of an
orbiting body. This minute variation generates torques that can be
mathematically exploited to keep a satellite\'s axis of minimum inertia
perpetually pointing toward the Earth, ensuring that communication
antennas remain properly oriented without the need for active fuel
expenditure.^11^

However, because these gravity-gradient torques are extraordinarily
weak---typically scaling on the order of
![](RESEARCH/media_history/media/image3.png){width="0.3515627734033246in"
height="0.26884186351706035in"}, where
![](RESEARCH/media_history/media/image10.png){width="0.11116579177602799in"
height="0.2627548118985127in"} represents the moment of inertia and
![](RESEARCH/media_history/media/image7.png){width="0.1547856517935258in"
height="0.2579757217847769in"} represents the orbital rate---satellites
require significant inertia augmentation to withstand environmental
disturbances in orbit.^11^ These disruptive forces include solar
radiation pressure, magnetic torques interacting with the satellite\'s
residual magnetic moment, micrometeorite impacts, and the thermal
bending of structural components.^11^

To achieve this necessary inertia augmentation, engineers designed a
system featuring a long extensible rod (such as a 60-foot STEM rod)
terminating in a heavy tip mass (e.g., 20 pounds).^11^ To damp out
transient perturbations and stabilize the satellite, the system
incorporated two single-degree-of-freedom (single-axis) gyros acting as
an internal dissipative joint or \"anchor\".^11^ These gyros were housed
in gimbal cans mounted on bearings and immersed in a highly viscous
fluid bath; energy dissipation was achieved strictly through the fluid
shear resulting from the relative motion between the gimbal cans and the
satellite body.^11^ Because of their compact size, these dissipative
joints were sealed entirely inside the satellite, isolating them from
the harsh vacuum and thermal extremes of the space environment.^11^

Edward E. Zajac, a mathematician and engineer at Bell Labs, alongside
his colleague J.A. Lewis, undertook the formidable task of
mathematically modeling this specific two-gyro \"roll-vee\"
configuration.^11^ Their analytical study, subsequently published in the
*Bell System Technical Journal* in 1964, required the computation of
massive differential equations divided into two primary kinetic regimes:
small-angle motion and large-angle motion.^11^

For small-angle motion, the researchers developed linearized equations
to govern the minor roll, pitch, and yaw perturbations of the satellite.
The standard axes were defined geometrically: the pitch axis was normal
to the orbit plane, the yaw axis lay along the local vertical
(Earth-pointing), and the roll axis followed the orbital track.^11^ The
gyros were configured to provide three-axis damping. Pitch disturbances
caused the gimbals to move in opposite directions (a \"scissoring\"
motion), while yaw disturbances caused in-phase motion.^11^ Roll
disturbances, while restricted from moving the gyros directly, were
damped indirectly through dynamic coupling with the yaw axis.^11^ Zajac
and Lewis wrote a computer program utilizing the Routh stability
criteria to rapidly calculate the system\'s stability and establish
rigorous mathematical bounds on the asymptotic damping rate
(![](RESEARCH/media_history/media/image6.png){width="0.18343175853018373in"
height="0.2649562554680665in"}) across a wide six-parameter space.^11^

The large-angle motion studies were significantly more complex,
addressing the highly nonlinear dynamics of a satellite far from its
desired orientation, such as during initial orbital injection or
deliberate inversion maneuvers.^11^ To avoid the mathematical
singularities (gimbal lock) inherently associated with Euler angles, the
researchers modeled the kinematics using direction cosines and Euler
parameters.^11^ Furthermore, the system had to account for variable
inertia during the physical deployment of the extensible rod in space.
This required calculating the angular momentum
![](RESEARCH/media_history/media/image1.png){width="0.14599628171478565in"
height="0.27113517060367454in"} for a body of variable mass distribution
via the specific integral:
![](RESEARCH/media_history/media/image4.png){width="2.6479483814523186in"
height="0.2710498687664042in"} where
![](RESEARCH/media_history/media/image2.png){width="0.10253937007874016in"
height="0.2666010498687664in"} represents the radius vector from the
center of mass to the mass element
![](RESEARCH/media_history/media/image12.png){width="0.2996412948381452in"
height="0.2686439195100612in"}.^11^

A critical component of this large-angle study was addressing the
satellite\'s inherent bistability---meaning it possessed two stable
orientations 180° apart about the pitch axis.^11^ The researchers
formulated the \"Roll-Gyro Equilibrium Theorem,\" proving that for a
symmetrical, gravity-oriented, roll-gyro-stabilized body in a circular
orbit, equilibrium positions mandate that the body roll axis be parallel
to either the orbit roll axis or the orbit yaw axis.^11^ To prevent the
satellite from settling into undesirable, skewed equilibrium positions
due to physical gimbal stops, Zajac established that the parameters had
to satisfy strict inequality conditions, such as
![](RESEARCH/media_history/media/image5.png){width="1.7369794400699912in"
height="0.27042760279965006in"}, where
![](RESEARCH/media_history/media/image8.png){width="0.19547462817147856in"
height="0.26749234470691163in"} is the gyro angular momentum and
![](RESEARCH/media_history/media/image13.png){width="0.7583005249343832in"
height="0.27007983377077865in"} is the satellite inertia
differential.^11^

## The Genesis of Scientific Visualization: Zajac\'s Orbital Simulation

The output of these exhaustive mathematical simulations was physically
staggering. The numerical integration of highly nonlinear differential
equations across thousands of discrete orbital time steps resulted in
towering stacks of punch cards and continuous-form line printer outputs
detailing the temporal histories of the satellite\'s pitch, yaw, and
roll.^3^ For a human engineer, interpreting this alphanumeric \"data
flood\" to determine if a specific multi-variable satellite
configuration would ultimately stabilize or tumble wildly was
agonizingly inefficient.^3^

Zajac recognized that the human mind processes complex spatial and
temporal relationships far more effectively through continuous visual
tracking than through discrete numerical reading.^12^ He hypothesized
that the mainframe could be explicitly programmed to calculate the
perspective coordinates of the satellite\'s orientation at each time
step, automatically draw it, and output the sequential results as a
motion picture.^3^

In 1963, utilizing the computational power of the IBM 7090 mainframe at
Bell Labs, Zajac successfully produced *Simulation of a Two-Gyro
Gravity-Gradient Attitude Control System*---recognized historically as
the first computer-animated film.^5^ The technical pipeline developed by
Zajac for this film was revolutionary, establishing the foundational
architecture for all modern scientific visualization.

### The Hardware and Software Pipeline

The creation of the 1963 film necessitated bridging several distinct,
room-sized pieces of mid-century computing hardware. The workflow
proceeded through several rigidly defined stages:

1.  **Programming and Input**: Zajac wrote the core mathematical
    calculations governing the satellite\'s kinematics in the FORTRAN
    programming language.^5^ These calculations were punched onto
    standard IBM punch cards.^5^

2.  **Geometric Translation**: To convert raw coordinate data into a
    visual representation, Zajac utilized a specialized subprogram
    called ORBIT, authored by his Bell Labs colleague Frank Sinden.^5^
    ORBIT translated the numerical orientation data into a
    three-dimensional perspective drawing of a rectangular box, which
    served as a geometric proxy for the satellite body.^5^

3.  **Mainframe Processing**: The punched cards were fed into the IBM
    7090 (or the subsequent 7094 series) computer.^5^ The mainframe
    computed the precise two-dimensional screen coordinates for the
    perspective drawing for each individual frame of the proposed film,
    generating thousands of plotting instructions.

4.  **Magnetic Storage**: Because visual output devices could not
    process data as fast as the IBM 7090 could compute it, the mainframe
    wrote these plotting commands sequentially onto a reel of magnetic
    tape.^3^

5.  **Optical Output via SC-4020**: The magnetic tape was physically
    transported to a General Dynamics Electronics Stromberg-Carlson 4020
    (SC-4020) microfilm recorder.^5^ The SC-4020 was a massive
    peripheral originally designed to rapidly print alphanumeric
    characters onto microfilm.^10^ Inside the SC-4020, an electron beam
    fired through a Charactron cathode-ray tube (CRT), tracing the
    calculated lines of the geometric box onto its phosphorescent
    screen.^3^

6.  **Automated Filming**: A 16mm motion picture camera, with its
    shutter permanently locked open, was mounted directly facing the CRT
    faceplate.^3^ Once the electron beam finished tracing a single
    frame, a digital command embedded on the magnetic tape advanced the
    camera\'s film to the next frame, preparing the system to expose the
    subsequent image.^3^

![](RESEARCH/media_history/media/image9.png){width="6.458333333333333in"
height="5.114583333333333in"}

The resulting black-and-white sound film, with durations cited in
historical literature ranging from a concise 1.25 minutes to an expanded
4-minute narrated version, successfully visualized the satellite
orbiting a rotating Earth against a fixed-star background.^3^

Zajac brilliantly utilized the inherently programmatic nature of the
system to manipulate cinematography in ways impossible with a physical
camera. By altering merely a few data cards, he seamlessly switched the
mathematical projection matrix, generating a secondary sequence from a
vantage point orbiting directly behind the satellite. This alternate
view omitted the Earth entirely to focus purely on the box\'s attitude
relative to its local trajectory.^3^

### The Philosophy of the Scientist-Filmmaker

In his subsequent foundational publications, including his 1964 paper
\"Computer-Made Perspective Movies as a Scientific and Communication
Tool\" in the *Communications of the ACM* and his 1965 article
\"Computer Animation: A New Scientific and Educational Tool\" in the
*Journal of the SMPTE*, Zajac outlined a compelling philosophy regarding
this new medium.^3^ He championed computer animation as an \"exciting,
powerful, and cheap new scientific and educational tool\" capable of
translating esoteric physical dynamics into universally comprehensible
motion.^3^

Zajac argued that computer animation granted the scientist unprecedented
creative autonomy, transforming them into \"scientist-filmmakers.\" By
writing scripts in standard mathematical languages like FORTRAN, the
scientist communicated directly through the film medium, sidestepping
the need to explain complex physics to traditional cel animators.^3^ The
inherent advantages of digital computation---specifically the use of
programming loops---meant that a systematically repeating physical
action only needed to be coded once, regardless of how many frames it
occupied on the final reel.^3^ Furthermore, through parameterized
variables, a single mathematical script could produce an entire \"family
of films\" demonstrating varying physical conditions (such as different
initial spin rates or mass distributions), rather than a single, static
movie.^3^

Financially, this methodology was highly economical. Line-drawing
animation generated via the SC-4020 cost approximately \$50 per minute
of finished film.^3^ This low financial barrier allowed researchers to
use animation iteratively, treating the film not as a final presentation
product, but as an active tool for testing hypotheses and visually
debugging their physical models.^3^

This ecosystem rapidly expanded within Bell Labs. Following Zajac\'s
success, F.W. Sinden produced a 10-minute educational film titled
*Force, Mass, and Motion*, which simulated Newton\'s laws of gravity.
Demonstrating the flexibility of the computer, Sinden easily modified
the code to simulate hypothetical interactions, such as inverse-cube and
direct-cube orbital relationships---scenarios that are exceptionally
difficult to set up in physical experiments but trivial to simulate
digitally.^3^ Similarly, R.N. Shepard and Zajac co-produced *Two
Paradoxes*, a 2-minute film combining visual optical illusions (the
Penrose staircase) with auditory illusions (Shepard tones), marking it
as one of the first films where both the visual animation and the audio
track were entirely generated by a computer algorithm.^3^

  ---------------------------------------------------------------------------
  **Early Bell Labs   **Creator(s)**    **Year**          **Primary Purpose /
  Computer Film**                                         Innovation**
  ------------------- ----------------- ----------------- -------------------
  *Simulation of a    E. E. Zajac       1963              First
  Two-Gyro                                                computer-animated
  Gravity-Gradient                                        film; visualized
  Attitude Control                                        complex satellite
  System*                                                 stabilization
                                                          mathematics via
                                                          perspective
                                                          graphics.^3^

  *A Computer         K. C. Knowlton    1964              Demonstrated the
  Technique for the                                       BEFLIX programming
  Production of                                           language; utilized
  Animated Movies*                                        typographic
                                                          characters to
                                                          simulate grayscale
                                                          shading.^3^

  *Force, Mass, and   F. W. Sinden      c\. 1965          Educational film
  Motion*                                                 simulating
                                                          Newtonian physics,
                                                          including
                                                          hypothetical
                                                          inverse-cube and
                                                          direct-cube orbital
                                                          interactions.^3^

  *Two Paradoxes*     R. N. Shepard &   c\. 1965          First \"pure\"
                      E. E. Zajac                         computer film
                                                          combining
                                                          algorithmic
                                                          animation (Penrose
                                                          staircase) with
                                                          algorithmic audio
                                                          (Shepard tones).^3^

  *Table 1: Key                                           
  pioneering                                              
  computer-animated                                       
  films produced at                                       
  Bell Telephone                                          
  Laboratories during                                     
  the early 1960s,                                        
  illustrating the                                        
  rapid                                                   
  diversification of                                      
  the medium from                                         
  scientific                                              
  simulation to                                           
  educational and                                         
  psychological                                           
  exploration.*                                           
  ---------------------------------------------------------------------------

## Democratizing the Mainframe: Kenneth Knowlton and the BEFLIX Architecture

While Zajac's work irrevocably proved that computers could animate
mathematical models, the methodology was heavily constrained. Generating
films with FORTRAN required the user to be intimately familiar with
geometry, calculus, and matrix algebra to calculate the precise
numerical endpoints of every line segment drawn on the CRT.^3^ This
intense mathematical prerequisite locked computer animation behind a
formidable wall of academic expertise, making it fundamentally
inaccessible to traditional animators, graphic designers, and visual
artists.

This paradigm was shattered by Kenneth C. Knowlton. A polymath with a
background in Engineering Physics from Cornell University and a 1962
Ph.D. in Computer Science from the Massachusetts Institute of Technology
(MIT), Knowlton joined the Techniques Research Department at Bell Labs
and fundamentally redefined how humans instructed computers to
manipulate images.^15^

### The Invention of the Domain-Specific Language

In 1963, Knowlton developed BEFLIX (an acronym for Bell Flicks), widely
recognized by computing historians as the first embedded domain-specific
language (DSL) explicitly designed for computer animation.^10^
Introduced formally at the 1964 Spring Joint Computer Conference in his
seminal 20-page paper, *A Computer Technique for Producing Animated
Movies*, BEFLIX divorced the creation of animation from strict
vector-based mathematical plotting.^1^

Rather than plotting precise coordinate endpoints in an empty Cartesian
space, BEFLIX was architected to simulate the raster scanning of a
television set.^3^ It treated the computer\'s memory as a rigid grid of
discrete picture elements (pixels). Hosted within the FORTRAN II
environment and utilizing the FORTRAN II Assembly Program (FAP) macro
language constructs, BEFLIX allowed users to manipulate vast visual
areas rather than single lines.^10^

The hardware environment executing BEFLIX was formidable. The IBM 7090
was IBM\'s first transistor-based mainframe (a massive technological
leap over earlier vacuum tube models), originally developed for the
scientific, engineering, and aerospace markets, with clients including
NASA and the Jet Propulsion Laboratory.^10^ It featured 32,768 words of
magnetic core memory (utilizing 36-bit words) and a blisteringly fast
memory cycle time of 2.18 microseconds.^10^

Knowlton brilliantly leveraged this 36-bit memory architecture. In
BEFLIX, visual information was encoded at a depth of 3 bits per
pixel.^10^ This highly efficient packing meant that exactly 12 pixels
could be stored in a single 36-bit word.^10^ This optimization was
crucial; it ensured the IBM 7090 had sufficient core memory to hold two
entirely uncompressed \"fine resolution\" frames simultaneously in RAM,
allowing for rapid frame-buffer manipulation without constantly reading
and writing to slow magnetic disks.^10^

### Surfaces, Scanners, and Logical Operations

To abstract the physical memory into something an animator could
conceptualize, BEFLIX organized the core memory into logical
\"surfaces.\" The programmer could choose to work in coarse resolution
(126 by 92 pixels) or fine resolution (252 by 184 pixels).^10^ By
linking contiguous blocks of coarse surfaces, Knowlton allowed
programmers to construct custom aspect ratios---from extreme horizontal
panoramas to tall vertical strips---optimizing the IBM 7090\'s rigid
structure for visual flexibility.^10^

  -----------------------------------------------------------------------
  **Surface         **Resolution**    **Memory          **Valid Pairings
  Designator**                        Allocation        for Extended
                                      Topology**        Grids**
  ----------------- ----------------- ----------------- -----------------
  **WW, XX, YY,     126x92            Coarse            Standard
  ZZ**                                                  low-resolution
                                                        blocks.^10^

  **AA, BB**        252x184           Fine              Standard
                                                        high-resolution
                                                        blocks.^10^

  **PP**            252x92            Horizontal Coarse Merges WW +
                                                        XX.^10^

  **TT**            126x184           Vertical Coarse   Merges YY +
                                                        ZZ.^10^

  **FF**            504x92            Wide Coarse       Merges WW + XX +
                                                        YY + ZZ.^10^

  **EE**            126x368           Tall Coarse       Merges WW + XX +
                                                        YY + ZZ
                                                        vertically.^10^

  *Table 2: The                                         
  architectural                                         
  memory models of                                      
  the BEFLIX                                            
  language.                                             
  Knowlton\'s                                           
  design abstracted                                     
  the mainframe\'s                                      
  36-bit words into                                     
  manipulable                                           
  visual grids,                                         
  allowing                                              
  animators to                                          
  specify frame                                         
  buffers of                                            
  varying                                               
  dimensions.*                                          
  -----------------------------------------------------------------------

To manipulate these surfaces, BEFLIX employed a conceptual mechanism
called \"Scanners\" (named A through Z).^10^ A scanner functioned as a
programmable read/write head that \"lived\" on a designated surface. It
possessed a specific coordinate within the surface and could read the
3-bit value of the pixel beneath it.^10^ Programmers manipulated the
image by conditionally directing these scanners to read, compare, move,
and write pixel values.

A typical BEFLIX script relied on low-level operational logic rather
than algebra. For example, the macro command PLACE sc, surf, x, y would
initialize a scanner at a specific location on a surface.^10^ More
complex logic was achieved through conditional branching, such as the
IFANY command. A programmer could instruct the system with a string
like: IFANY (B,R,10)(B,A,C)(A,E,7)T(A,T,B)\..., which logically
translates to: *If scanner B is to the right of x=10, OR if scanner B is
above scanner C, OR if scanner A is sitting on a value equal to 7, THEN
move scanner A to the same position as scanner B*.^10^

To demonstrate the power and efficiency of the language, Knowlton
produced a 17-minute, silent instructional film titled *A Computer
Technique for the Production of Animated Movies* (1964).^3^ The film
served as a visual manual, showcasing macro-commands intrinsic to
BEFLIX, such as PAINT, ZOOM, and DISOLV, which allowed users to
manipulate entire rectangular blocks of pixels simultaneously.^3^ By
automating repetitive tasks, providing looping structures, and
abstracting the underlying memory management, BEFLIX made computer
animation fundamentally accessible. While calculating the state of every
single pixel point made BEFLIX films computationally more expensive than
Zajac\'s line-drawn vector films, the language required virtually no
mathematical training, opening the mainframe\'s doors to non-scientists
and setting the stage for digital art.^3^

## Spatial Quantization and the Psychology of Perception

While BEFLIX elegantly solved the software accessibility problem, Bell
Labs researchers still faced a stringent hardware limitation that
bottlenecked visual fidelity: the SC-4020 microfilm recorder was an
inherently binary output device.^6^ Its Charactron tube was designed to
expose film microscopically as either solid black or solid white. It
completely lacked the analog capacity to modulate the intensity of its
electron beam to produce continuous-tone shades of gray.^3^

Knowlton initially circumvented this limitation in his 1964 BEFLIX film
through a rudimentary form of typographic mapping. Because the
Charactron tube was optimized to stamp alphanumeric characters onto the
screen rapidly, Knowlton used visually dense letters (like the letter
\"B\" or \"M\") to represent dark shades, and sparse punctuation marks
(like commas, apostrophes, or periods) to represent lighter areas.^3^
While functional for instructional diagrams, this technique was visually
crude.

However, this rudimentary typographic mapping sparked a much deeper,
scientifically rigorous inquiry into spatial quantization, dithering,
and digital halftoning. Working alongside Leon D. Harmon---a brilliant
researcher specializing in mental and neural processing, who had
previously worked with John von Neumann on the IAS machine---Knowlton
sought to formally define the algorithms necessary to derive subjective
gray values from strictly binary output devices.^6^

### The Algorithmic Deconstruction of Tone

Harmon and Knowlton\'s collaborative research, eventually formalized in
seminal papers published in the journals *Computer Graphics and Image
Processing* (1972) and *Visible Language* (1977) under the title
\"Computer-Produced Grey Scales,\" represented a monumental leap in
digital image processing.^6^ They developed sophisticated computational
techniques to quantize physical space into discrete micro-cells, filling
these cells with varying sizes and shapes of black areas on a white
background.^6^

The concept of halftoning was not entirely novel; historical precedents
stretched back to Henry Fox Talbot\'s 1852 patent utilizing folded black
crape gauze for photographic engraving, and even earlier to 1827
punch-card operated looms capable of weaving black and white silk
threads into continuous-tone images with a resolution of 125 threads per
inch.^18^ However, Harmon and Knowlton were pioneering the translation
of this analog concept into the digital realm, utilizing iterative
screen design and computational algorithms to achieve optimal visual
fidelity without human intervention.^18^

Their algorithms divided the image grid into specific classes of black
and white regions, utilizing pseudo-random noise and ordered dither
matrices to artificially smooth out tonal discontinuities and break up
harsh quantization steps.^6^ This allowed a purely binary output device
to trick the human eye\'s physiological limitations, coercing the visual
cortex into perceiving a rich, continuous gradient of gray from a field
of stark black and white pixels.^6^

### ***Studies in Perception I (Computer Nude)***

The most famous, and historically consequential, application of these
grayscale synthesis algorithms occurred in 1966. Harmon and Knowlton
were actively experimenting with photomosaic techniques, testing how the
human brain integrates small, seemingly unrelated micro-patterns into a
coherent macro-image.^7^

For their test subject, they selected a photograph of the avant-garde
dancer and choreographer Deborah Hay, reclining nude.^7^ The
digitization process was painstaking. They scanned the original
photograph with an optical camera, which converted the analog light
voltages into discrete binary numbers. These numerical values were then
processed by their spatial quantization algorithms and mapped to a
specialized set of typographic symbols---ranging from mathematical
operators to custom geometric blocks---based precisely on their
calculated halftone densities.^7^

The resulting output was printed as a massive 12-foot-wide (150 x 370
cm) mural, titled *Studies in Perception I (Computer Nude)*
(1966/1967).^7^ Initially characterized by Knowlton as a \"sophomoric
prank\" meant to be secretly hung in the office of a Bell Labs
executive, the piece was actually a rigorous demonstration of
physiological visual theory.^7^

The composition illustrated the unique ability of the viewer\'s brain to
interpret abstract symbols. Upon close inspection, the mural dissolved
into an incomprehensible matrix of electronics symbols, letters, and
glyphs. However, as the viewer stepped back, increasing the physical
distance, the brain seamlessly integrated the varying micro-densities of
the symbols into the smooth, continuous macroscopic curves of the human
form.^20^

![](RESEARCH/media_history/media/image11.png){width="6.458333333333333in" height="9.0in"}

The cultural and scientific impact of this specific work was immense. It
was published in *The New York Times* on October 11, 1967---making
history as the first full-frontal nude published by the venerable
paper---instantly vaulting computer graphics into the broader public
consciousness.^7^

The success of the nude mural deeply informed Leon Harmon's subsequent,
highly influential research into facial recognition. Harmon sought to
determine the absolute minimum amount of spatial and tonal information
required for the human brain to recognize and discriminate specific
human faces.^22^ By applying these spatial quantization techniques,
Harmon produced a highly pixelated, block portrait of Abraham Lincoln,
consisting entirely of varying shades of gray squares.^7^ This
minimalist portrait illustrated his landmark November 1973 *Scientific
American* article, \"The Recognition of Faces,\" laying the theoretical
groundwork for modern image compression algorithms.^7^ The image was so
striking that in 1976, surrealist Salvador Dalí explicitly utilized
Harmon\'s Lincoln portrait as the basis for his optical-illusion
painting *Gala Contemplating the Mediterranean Sea*, representing one of
the earliest instances of a recognized traditional artist directly
appropriating digital algorithmic output.^7^ Harmon and Knowlton
continued their specific series of perceptional studies in 1969 with the
creation of *Gulls (Studies in Perception II)* and *Gargoyle (Studies in
Perception III)*, further cementing their legacy as pioneers of digital
image synthesis.^16^

## The Avant-Garde Incursion: Stan VanDerBeek and the ***Poemfield*** Series

The highly publicized publication of *Computer Nude* acted as a powerful
catalyst, irrevocably drawing the attention of the New York avant-garde
arts community to the sterile, industrial laboratories of New Jersey.
The artwork played a pivotal role in the formal launch of Experiments in
Art and Technology (E.A.T.), an influential organization founded by
artist Robert Rauschenberg and Bell Labs engineer Billy Klüver
specifically to foster deep collaborations between the engineering and
artistic communities.^8^

Among the earliest and most visionary artists to recognize the profound
potential of the computer as an expressive artistic medium was the
experimental filmmaker Stan VanDerBeek.^23^ VanDerBeek viewed the
computer not merely as an automated drafting tool, but as a
revolutionary mechanism for expressing and engaging human
consciousness.^8^ During the height of the Cold War, he argued that
technology was a necessary tool that humanity had to master to prevent
its own mechanization and destruction.^8^ He envisioned sprawling
multimedia \"experience machines,\" culminating in his architectural
concept of the \"Movie-Drome\"---a proto-cinematic, dome-shaped space
designed to immerse audiences in a barrage of audiovisual data, eerily
anticipating modern concepts of the internet, media saturation, and
algorithmic curation.^23^

Through mutual connections within the E.A.T. network, VanDerBeek began a
formal collaboration with Kenneth Knowlton at Bell Labs in 1966.^8^
Utilizing Knowlton\'s BEFLIX programming language and the massive IBM
7094 mainframe, the duo produced a sequence of groundbreaking,
computer-animated films known collectively as the *Poemfield* series
(created between 1966 and 1971).^8^

### Typography, Geometry, and Machine Semantics

The *Poemfield* series consists of eight documented films, though
various historical sources and retrospectives occasionally reference up
to ten.^15^ These works represent a radical departure from both Zajac\'s
rigid scientific simulations and the character-driven narratives of
traditional animation. They are fundamentally textual, lyrical, and
abstract, exploring the deep intersection of visual poetry, typography,
and machine logic.^24^

In a typical *Poemfield* film (such as *Poemfield No. 2*), the cinema
screen operates as a fluid, highly pixelated canvas.^26^ Thousands of
electrons, guided by the precise logic of the BEFLIX script, generate
twinkling mosaics and kaleidoscopic geometric fields.^8^ From these
abstract, shifting matrices, powerful sequences of words and poems
gradually coalesce into legibility, move dynamically across the frame,
and subsequently dissolve back into the digital noise from which they
emerged.^8^

The text for these films was primarily sourced from VanDerBeek's own
poetry. However, in *Poemfield No. 7*, VanDerBeek utilized words written
by the prominent nonviolent peace activist A.J. Muste.^8^ By programming
these humanist, anti-war, and existential messages into the IBM 7094---a
multi-million dollar mainframe whose primary clientele included NASA and
the U.S. military---VanDerBeek engaged in an early form of conceptual
hacking.^8^ He subverted a technology expressly designed for computing
ballistic trajectories and orbital mechanics, forcing it instead to
render the existential anxieties and poetic aspirations of the Computer
Age.^8^

The physical process of creating the *Poemfield* films was arduous and
highly collaborative. VanDerBeek, heavily informed by his formal
background in painting, designed the visual choreography, while Knowlton
translated these artistic impulses into functional BEFLIX logic.^26^ The
initial visual output was captured by the Stromberg-Carlson 4020
microfilm recorder strictly in black and white.^26^ Because native,
high-fidelity color computer graphics were not yet viable on this
hardware, the vibrant, psychedelic colors seen in the final *Poemfield*
distributions were achieved through complex, post-production optical
printing and tinting processes carried out by VanDerBeek.^26^

These experimental films were rarely exhibited in traditional cinemas.
VanDerBeek distributed them individually, projected them inside his
spherical Movie-Drome, and integrated them into massive, multi-screen
architectural installations such as *Found Forms* (1969) and *Cine
Dreams* (1972).^8^ The *Poemfield* series definitively demonstrated that
computer programming could transcend functional utility to become a
deeply expressive, poetic medium in its own right.

## The Expansion of the Algorithmic Canvas: The Evolution of Domain-Specific Languages

The extraordinary success of the VanDerBeek-Knowlton partnership
established Bell Telephone Laboratories as a vital global nexus for
computational art.^9^ Knowlton, functioning both as a lead software
engineer and a passionate champion of the digital medium, continually
developed new graphics programming languages specifically engineered to
facilitate artistic collaboration and push visual boundaries.^4^

By continuously analyzing the aesthetic limitations of BEFLIX, Knowlton
developed a suite of subsequent Domain-Specific Languages, each
providing entirely different visual affordances:

- **EXPLOR (EXplicit Patterns, Local Operations & Randomness):**
  Developed around 1970, this language was tailored explicitly for
  generating complex, repeating patterns and executing cellular automata
  logic.^15^ Knowlton collaborated extensively with artist Lillian F.
  Schwartz, who utilized the EXPLOR system to create a highly
  influential series of ten abstract animated films between 1968 and
  1974, defining much of the early aesthetic of algorithmic art.^15^

- **SPHERES (System For Efficient Rendering of Ensembles of Spheres):**
  Created around 1981, this advanced system allowed for the
  three-dimensional rendering and intersecting of spherical objects.^15^
  Crucially, it dealt with complex computational issues of pictorial
  depth, realistic roundedness, and object occlusion in 3-space.^17^
  Knowlton collaborated with Emmanuel Ghent on the 1978 film *Baobab*,
  utilizing an early version of the SPHERES system to produce animations
  that dynamically responded to and were rhythmically inspired by
  Ghent\'s electronic music.^15^

- **ATOMS (A Three-dimensional Opaque Molecule System):** Developed in
  collaboration with L. Cherry in 1977, this system was optimized
  specifically for ball-and-stick rendering in chemistry
  visualization.^17^ It returned Knowlton\'s technology to its strict
  scientific roots while maintaining the high aesthetic quality
  developed during his artistic collaborations.^17^

This continuous, iterative loop of feedback---where the creative demands
of avant-garde artists like VanDerBeek and Schwartz pushed Knowlton to
invent entirely new programming architectures, which in turn unlocked
unforeseen creative possibilities for the artists---became the defining
hallmark of the Bell Labs model of industrial research.^4^ Beyond
graphics, Knowlton\'s work in this period also yielded significant
structural contributions to computer science, including the L-6 language
(Low Level Linked List Language) and the \"buddy system\" for fast
storage allocation (binary splitting and recombination of memory
blocks), proving that artistic inquiry could drive fundamental computer
science.^17^

## Institutional Validation and the Museum Context

The radical visual experiments conducted at Bell Labs were not confined
to scientific journals; they were rapidly absorbed into the
institutional framework of the contemporary art world, securing the
computer\'s status as a legitimate artistic tool.

The seminal moment for this high-culture validation was the landmark
1968 exhibition *The Machine as Seen at the End of the Mechanical Age*,
curated by K.G. Pontus Hultén at the Museum of Modern Art (MoMA) in New
York City.^15^ The exhibition sought to explore the historical
relationship between art and technology, provocatively juxtaposing
classical mechanical devices (such as a 1951 Bugatti Royale and a
Chrysler engine fitted into a horse-drawn hearse) with the bleeding edge
of the emerging digital and cybernetic era.^28^

Harmon and Knowlton\'s 12-foot mural, *Studies in Perception I (Computer
Nude)*, was prominently featured in this exhibition, serving as a
striking visual metaphor for the transition from the mechanical age to
the information age.^4^ The image physically demonstrated how
traditional, continuous analog reality (represented by the human body)
was being digitized, quantized, and reconstructed by machine logic.^20^

Furthermore, MoMA integrated the temporal dimension of Bell Labs\'
research into the exhibition\'s public programming. On the evening of
November 21, 1968, MoMA\'s Department of Film, under the sponsorship of
the International Study Center, hosted \"An Evening of Computer-Produced
Films\".^27^ During this 80-minute event, Kenneth Knowlton presented a
comprehensive screening of computer animations generated at Bell Labs,
alongside related works from the Boeing Aircraft Company, Lawrence
Radiation Laboratory, Los Alamos Scientific Laboratory, and MIT.^4^
Knowlton lectured the audience on the underlying programming techniques,
effectively serving as an ambassador for the new medium and demystifying
the mainframe for the cultural elite.^27^

This institutional relationship proved remarkably enduring. Exactly
fifty years later, on Monday, March 26, 2018, MoMA hosted *An Evening of
Computer Films with Ken Knowlton* as part of its *Modern Mondays*
series.^4^ This retrospective event, held in the Roy and Niuta Titus
Theater 2, was programmed in conjunction with the exhibition *Thinking
Machines: Art and Design in the Computer Age, 1959--1989*.^4^ Original
16mm prints of Knowlton\'s BEFLIX-produced works and his collaborative
films were screened, after which Knowlton engaged in a live conversation
with writer Rebekah Rutkoff and MoMA associate media conservator Peter
Oleksik.^4^ The 2018 event cemented the legacy of the Bell Labs
researchers not merely as engineers who solved graphical display
problems, but as foundational pioneers of a dominant global art form.^4^

## Conclusion: The Synthesis of Algorithm and Aesthetics

The body of work generated at Bell Telephone Laboratories during the
1960s represents a unique singularity in the history of media and
technology. The researchers did not initially set out to invent a new
artistic paradigm; their primary mandate was to solve critical
engineering bottlenecks associated with telecommunications and
aerospace. Edward Zajac sought a mechanism to comprehend the
multidimensional stabilization of gravity-gradient satellites, leading
directly to the creation of the first computer animation pipeline.^3^
Kenneth Knowlton recognized that the steep mathematical learning curve
of FORTRAN was an inefficient barrier to widespread visualization,
leading to the creation of BEFLIX, the first graphical abstraction
layer.^3^ Leon Harmon required a rigorous method to test the absolute
physiological limits of human pattern recognition, leading to the
algorithmic synthesis of gray scales and the invention of digital
photomosaics.^7^

Yet, by solving these deeply technical, domain-specific problems, these
engineers inadvertently constructed the foundational vocabulary of
digital media. They proved unequivocally that a computer is not merely a
high-speed calculator, but a universal simulator capable of rendering
Newtonian physics, expressive typography, and the nuances of the human
form. By opening their laboratories and inviting avant-garde artists
like Stan VanDerBeek and Lillian Schwartz into their rigorous
mathematical environments, the Bell Labs engineers ensured that this new
technology was infused with humanist inquiry, poetic semantics, and
aesthetic rigor.^8^ The resulting films and images---from the tumbling
orbit of Zajac\'s satellite box to the pixelated gaze of Harmon\'s
Lincoln and the lyrical geometry of the *Poemfields*---stand today not
just as footnotes in computer science, but as the foundational artifacts
of the digital visual age.

#### Works cited

1.  ICT & Art CONNECT - Timeline - Cheshire Henbury, accessed June 9,
    2026,
    [[https://www.cheshirehenbury.com/ict-art-connect/ict-art-connect-timeline.html]{.underline}](https://www.cheshirehenbury.com/ict-art-connect/ict-art-connect-timeline.html)

2.  Computing Science Technical Report No. 99 A History of Computing
    Research\* at Bell Laboratories (1937-1975), accessed June 9, 2026,
    [[http://research.google.com/pubs/archive/94.pdf]{.underline}](http://research.google.com/pubs/archive/94.pdf)

3.  Zajac - Content: Animation, accessed June 9, 2026,
    [[http://content-animation.org.uk/htmls/zajac_smpte.htm]{.underline}](http://content-animation.org.uk/htmls/zajac_smpte.htm)

4.  An Evening of Computer Films with Ken Knowlton \| MoMA, accessed
    June 9, 2026,
    [[https://www.moma.org/calendar/events/4117]{.underline}](https://www.moma.org/calendar/events/4117)

5.  Edward Zajac Produces the First Computer-Animated Film, accessed
    June 9, 2026,
    [[https://www.historyofinformation.com/detail.php?entryid=1002]{.underline}](https://www.historyofinformation.com/detail.php?entryid=1002)

6.  Computer-Produced Grey Scales \| Visible Language - Journals@UC,
    accessed June 9, 2026,
    [[https://journals.uc.edu/index.php/vl/article/view/5226]{.underline}](https://journals.uc.edu/index.php/vl/article/view/5226)

7.  Leon Harmon - Wikipedia, accessed June 9, 2026,
    [[https://en.wikipedia.org/wiki/Leon_Harmon]{.underline}](https://en.wikipedia.org/wiki/Leon_Harmon)

8.  Poemfield - The BOX Gallery, accessed June 9, 2026,
    [[https://www.theboxla.com/artist.php?id=5703]{.underline}](https://www.theboxla.com/artist.php?id=5703)

9.  Technology + Art - CHM - Computer History Museum, accessed June 9,
    2026,
    [[https://computerhistory.org/exhibits/technology-art/]{.underline}](https://computerhistory.org/exhibits/technology-art/)

10. BEFLIX \| PPTX - Slideshare, accessed June 9, 2026,
    [[https://www.slideshare.net/slideshow/beflix/71664039]{.underline}](https://www.slideshare.net/slideshow/beflix/71664039)

11. A Two-Gyro, Gravity-Gradient Satellite Attitude Control System,
    accessed June 9, 2026,
    [[https://www.content-animation.org.uk/htmls/lewis.htm]{.underline}](https://www.content-animation.org.uk/htmls/lewis.htm)

12. New Scientist 10 February 1966 - Computer Arts Society, accessed
    June 9, 2026,
    [[https://computer-arts-society.com/casarchive/cas/uploads/zajac-new-scientist-1966-8.pdf]{.underline}](https://computer-arts-society.com/casarchive/cas/uploads/zajac-new-scientist-1966-8.pdf)

13. Computer Animation: A New Scientific and Educational Tool (1965,
    accessed June 9, 2026,
    [[https://scispace.com/papers/computer-animation-a-new-scientific-and-educational-tool-3x27kyxpp7]{.underline}](https://scispace.com/papers/computer-animation-a-new-scientific-and-educational-tool-3x27kyxpp7)

14. A pair of paradoxes - Database of Digital Art, accessed June 9,
    2026,
    [[http://dada.compart-bremen.de/item/artwork/645]{.underline}](http://dada.compart-bremen.de/item/artwork/645)

15. Ken Knowlton - Digital Art Museum - DAM, accessed June 9, 2026,
    [[https://dam.org/museum/artists_ui/artists/knowlton-ken/]{.underline}](https://dam.org/museum/artists_ui/artists/knowlton-ken/)

16. Ken Knowlton - Wikipedia, accessed June 9, 2026,
    [[https://en.wikipedia.org/wiki/Ken_Knowlton]{.underline}](https://en.wikipedia.org/wiki/Ken_Knowlton)

17. Selected Papers - Ken Knowlton, accessed June 9, 2026,
    [[https://www.kenknowlton.com/pages/29papers.htm]{.underline}](https://www.kenknowlton.com/pages/29papers.htm)

18. Recent Progress in Digital Halftoning - Imaging.org, accessed June
    9, 2026,
    [[https://www.imaging.org/common/uploaded%20files/pdfs/Papers/1999/RP-0-93/1744.pdf]{.underline}](https://www.imaging.org/common/uploaded%20files/pdfs/Papers/1999/RP-0-93/1744.pdf)

19. Figure 10 from Computer-produced grey scales \| Semantic Scholar,
    accessed June 9, 2026,
    [[https://www.semanticscholar.org/paper/Computer-produced-grey-scales-Knowlton-Harmon/07602fa0f317f7d2d4fa63b7a8a69c64d2d5d01f/figure/6]{.underline}](https://www.semanticscholar.org/paper/Computer-produced-grey-scales-Knowlton-Harmon/07602fa0f317f7d2d4fa63b7a8a69c64d2d5d01f/figure/6)

20. Experiments in Art and Technology, accessed June 9, 2026,
    [[https://www.uni-weimar.de/kunst-und-gestaltung/wiki/images/EAT.pdf]{.underline}](https://www.uni-weimar.de/kunst-und-gestaltung/wiki/images/EAT.pdf)

21. Incredible Machines: Following People Like Us Into the Database \|
    Danny Snelson 2012, accessed June 9, 2026,
    [[https://dss-edit.com/plu/]{.underline}](https://dss-edit.com/plu/)

22. Convolutional Photomosaic Generation via Multi-Scale Perceptual
    Losses - CVF Open Access, accessed June 9, 2026,
    [[https://openaccess.thecvf.com/content_ECCVW_2018/papers/11131/Tesfaldet_Convolutional_Photomosaic_Generation_via_Multi-Scale_Perceptual_Losses_ECCVW_2018_paper.pdf]{.underline}](https://openaccess.thecvf.com/content_ECCVW_2018/papers/11131/Tesfaldet_Convolutional_Photomosaic_Generation_via_Multi-Scale_Perceptual_Losses_ECCVW_2018_paper.pdf)

23. Poemfield No. 1 - Ji.hlava IDFF, accessed June 9, 2026,
    [[https://www.ji-hlava.com/filmy/poemfield-no-1]{.underline}](https://www.ji-hlava.com/filmy/poemfield-no-1)

24. Stan VanDerBeek - Criticism - e-flux, accessed June 9, 2026,
    [[https://www.e-flux.com/criticism/237428/stan-vanderbeek]{.underline}](https://www.e-flux.com/criticism/237428/stan-vanderbeek)

25. Poem Field - Wikipedia, accessed June 9, 2026,
    [[https://en.wikipedia.org/wiki/Poem_Field]{.underline}](https://en.wikipedia.org/wiki/Poem_Field)

26. Poemfield No. 2 by Stan VanDerBeek - YouTube, accessed June 9, 2026,
    [[https://www.youtube.com/watch?v=87VMJEt6Mvw]{.underline}](https://www.youtube.com/watch?v=87VMJEt6Mvw)

27. Sound Recordings in The Museum of Modern Art Archives - MoMA,
    accessed June 9, 2026,
    [[https://www.moma.org/research/archives/finding-aids/SoundRecordingsf]{.underline}](https://www.moma.org/research/archives/finding-aids/SoundRecordingsf)

28. iThe Museum of Modern Art - MoMA, accessed June 9, 2026,
    [[https://assets.moma.org/documents/moma_press-release_326596.pdf]{.underline}](https://assets.moma.org/documents/moma_press-release_326596.pdf)

29. Modern Mondays - MoMA, accessed June 9, 2026,
    [[https://www.moma.org/calendar/film/560]{.underline}](https://www.moma.org/calendar/film/560)
