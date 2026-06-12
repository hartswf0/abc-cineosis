# The Film Begins Before the Frame

*BEFLIX, language models, and the new politics of moving images*

## The Scene

A person asks a language model for BEFLIX code.

That is all.

No camera on a tripod. No actor waiting for light. No hand touching acetate. No timeline full of clips. A prompt enters a chat box, and the model answers with instructions for making an image move.

The answer is not a picture. It is a prescription for a picture. It tells a machine what should appear, how it should alter itself, how long an intermediate state should last before becoming the next one.

That is the uncanny moment.

The user did not draw.  
The model did not film.  
The screen has not moved.

And still, somewhere upstream, cinema has already begun.

The old magic of film used to gather around the frame itself: the photographed instant, the captured face, the cut from one shot to another. The new magic gathers earlier. The moving image is increasingly born in description, in a layer of language that precedes code, and in code that precedes any visible frame. By the time the image arrives, much of the authorship has already happened elsewhere.

## Bell Flicks

Long before prompt videos and image models, Bell Labs engineers and artists were already discovering that motion pictures could be written. In 1963, Kenneth C. Knowlton developed BEFLIX—short for “Bell Flicks”—for making what he called “computer-produced movies” on Bell Labs’ IBM mainframes and Stromberg-Carlson SC-4020 microfilm plotter. MoMA now describes BEFLIX as one of the first languages designed specifically for rendering and animating images; the Computer History Museum notes that the language let a programmer describe shapes and their motions in a 252-by-184 grid of dots, with roughly 25 command types punched onto paper cards. citeturn29view0turn30view0turn18view0

Bell Labs had already learned that equations could become film. Edward Zajac’s 1963 satellite simulation and Frank Sinden’s *Force, Mass and Motion* used computers to animate scientific knowledge for public and technical audiences. BEFLIX emerged from that environment and then migrated into art, especially in Knowlton’s collaborations with Stan VanDerBeek on the *Poemfields* films. citeturn18view0turn17search8

The material details matter because they make the medium feel strange again. Knowlton’s 1965 *Science* article describes a BEFLIX frame as 46,368 picture spots, each with one of eight gray values. A roughly 17-minute film could run to about 25,000 frames, though only about 3,000 were unique images, generated from roughly 2,000 lines of BEFLIX programming and processed over months of work. Film, here, began as arithmetic. Celluloid came later. citeturn2view0

CLR. PNT. LIN. REC. SHF.

The mnemonics feel like fossils from an earlier media theology. Short, hard, imperative. Around them clustered the actual operations of the system: drawing lines and arcs, painting gray regions, copying one area into another, shifting pixel blocks, filling bounded shapes, enlarging, dissolving. The machine did nothing mystical. It obeyed a grammar. Yet from that obedience, something recognizably cinematic appeared. citeturn2view0turn30view0

BEFLIX is best understood as a primitive cinematic spell. A small set of commands turns symbolic instructions into motion. A field clears. A line advances. A region fills. A frame records. The achievement was not that the computer suddenly dreamed in images. The achievement was that image-making became explicitly procedural.

VanDerBeek, working with Knowlton at Bell Labs, later said that making computer films was like learning to draw “by pushing a pencil around with your nose.” The Computer History Museum adds a beautiful and eerie detail: the *Poemfields* animations, made on the IBM 7090 and SC-4020, were often first visible only when fully complete. That deferred visibility now feels uncannily contemporary. The moving image was already upstream then; you just had to wait for the machine to reveal what the code had been doing all along. citeturn30view0turn18view0

## The Old Dream of Control

Cinema has always been a fight over where control lives.

In live-action film, control sits in light, angle, lens, blocking, duration, the cut. In animation, it moves closer to the frame itself: every contour, every interval, every repeat. In code, it shifts one stage earlier again. You no longer manipulate the image alone. You manipulate the conditions under which the image can appear.

Knowlton understood this with unusual clarity. In his 1965 account, he imagined the movie producer wanting to describe pictures in “more sweeping and powerful terms” and let the computer supply the swarms of lower-level instructions required to realize them—as if one could simply say, in effect, “now shoot 150 frames.” That is prompt engineering in embryo. citeturn2view0

BEFLIX made that structure visible. The point was not only efficiency, though it did promise speed, reuse, and the possibility that the second film would be easier once the first had been built. The deeper revelation was philosophical. Cinema did not have to begin with a photographed world. It could begin with a written description of transformations. citeturn2view0turn30view0

That changes the language of film. The frame stops being a little window and starts becoming an executable result. A moving image can now be an argument, a score, a set of rules for becoming. BEFLIX compressed cinema into operations. It pulled the levers into the open.

And because it did that so bluntly, it preserved something current systems often erase: inspectability. In BEFLIX, command and consequence lived close together. You could see where the line came from. You could point to the instruction that cleared the field or shifted the block. The site of control had an address.

## The LLM Reversal

Now enter the language model, and the old architecture flips.

With an LLM, the human often no longer writes the operations. The human writes the request that writes the operations. Contemporary coding systems openly market this layer of indirection: OpenAI’s coding documentation describes Codex as a coding agent that helps users write, review, and debug code from natural-language instructions. Code generation is a product feature, not a party trick. citeturn21search0turn21search2

That means BEFLIX can return in a new form. Ask a language model for a bit of animation logic—whether in Python, Three.js, Processing, shader code, or a BEFLIX-like toy syntax—and the model will often answer with the procedural middle. It gives you the instructions for motion before there is any motion to see. The user becomes less like a camera operator and more like a legislator of appearance.

The same inversion now governs image and video systems. OpenAI’s DALL·E 3 page says that when a user offers an idea, ChatGPT will automatically generate “tailored, detailed prompts” for the image model. OpenAI’s Sora technical report says something even more revealing: GPT is used to turn short user prompts into longer, detailed captions before those captions are sent to the video model. A prompt, in other words, is often no longer the final instruction. It is raw material for another prompt. citeturn31search2turn26view0

One OpenAI whiteboard illustration for 4o image generation renders the chain with startling bluntness: “tokens -> [transformer] -> [diffusion] -> pixels.” The image arrives last. In Sora’s technical description, video is compressed into a machine-readable latent space, decomposed into spacetime patches, conditioned by text, and only then decoded back into pixels. The visible frame is literally downstream of invisible representations. citeturn23view0turn26view0

This is why the BEFLIX scene at the start feels larger than it first appears. A user asking an LLM for BEFLIX code is not indulging in retrocomputing whimsy. The scene is a miniature of the whole generative-media stack. Language addresses a model. The model generates procedural instructions. Those instructions generate motion. The motion becomes what we are still in the habit of calling cinema.

## Sparks

When Microsoft researchers published *Sparks of Artificial General Intelligence* in 2023, the public jolt came from the title. But the more enduring shock was elsewhere. The paper argued that an early version of GPT-4 could move across mathematics, coding, vision, medicine, law, psychology, and other domains without special prompting, suggesting a breadth of competence that exceeded the usual story about autocomplete. GPT-4’s own technical report likewise presented the model as a large-scale multimodal system with unexpectedly broad performance across professional and academic benchmarks. citeturn11view0turn21search12

Whether or not one accepts the paper’s AGI language is not the point here. The term itself remains disputed, and Melanie Mitchell noted in *Science* that AGI has become ubiquitous in business, government, and media discourse even as its meaning remains hotly contested. What matters for this essay is the cultural recognition that language had acquired operational reach. A single interface could now reach into code, diagrams, images, and tasks that had once belonged to separate technical worlds. citeturn28view0turn11view0

The spark was not consciousness. The spark was portability.

BEFLIX had already prefigured the logic. Once moving images can be described as instructions, and once instructions can themselves be generated from ordinary language, the distance between saying and showing collapses. Language stops being commentary on media and becomes a control surface for media.

That is the real reversal. Cinema used to begin with the image. Then it began with the camera. Then it began with the edit. Then it began with code. Now it begins upstream, in language—in the prompt that bends the future image before a single pixel exists.

## The Hidden Director

OpenAI’s Sora prompting guide reads, at moments, like a tiny film school. It tells users to think of prompting as “briefing a cinematographer,” to specify camera framing, depth of field, action beats, lighting, and palette, and to treat the prompt as a “creative wish list, not a contract.” It also says that the same prompt can yield different results on repeated runs, that shorter prompts give the model more freedom, and that longer prompts constrain it more tightly. A prompt does not dictate a frame so much as bend a field of possibilities. citeturn22view0

The guide becomes even more explicit about where authorship is actually distributed. Some attributes, it says, are governed only by API parameters rather than by prose in the prompt: resolution, duration, character references. Other passages advise users to establish style early because it is “one of the most powerful levers” for steering the outcome. Write “1970s film.” Write “IMAX-scale.” Write “16mm black-and-white.” Before the story has happened, the world has already been weighted toward certain textures, pacing, hierarchies of attention, and camera behavior. citeturn22view0

Image systems show the same drift upstream. OpenAI’s 4o image-generation documentation says image generation is native to chat context, so images can be refined across turns while carrying forward earlier text and uploaded visual references. The model is described as following detailed prompts, rendering text precisely, and keeping objects and relations more tightly bound than earlier systems. The prompt is no longer a single utterance. It is a conversation with memory. citeturn23view0

And above that visible conversation there are still other layers. OpenAI’s prompt-engineering documentation speaks of message roles and “differing levels of authority,” specifying that high-level instructions can take priority over the user’s input. Its custom-instructions documentation says those instructions are applied across chats. Its GPTs documentation says custom GPTs are shaped by instructions, knowledge, and selected capabilities. That bureaucratic vocabulary matters. It means the image pipeline has a hierarchy. Some instructions outrank others. Some authors are upstream enough to stay offscreen. citeturn25view0turn25view1turn25view2

A hidden system prompt is a hidden director.

That line is metaphorical, but only slightly. If one layer writes the style, another supplies persistent preferences, another auto-expands the user’s request, another controls model parameters, and another performs generation, then the final image is the product of a chain of custody rather than a single expressive act. DALL·E 3’s prompt expansion, Sora’s GPT-written long captions, and instruction hierarchies in chat systems all point in the same direction: the site of control is moving upward and becoming harder to inspect. citeturn31search2turn26view0turn25view0

This is why narratives now ripple backward. A prompt does not simply ask for a scene. It sets genre before plot, atmosphere before event, and moral weight before action. It nudges who will matter in the frame, what counts as beauty, what counts as realism, what the camera will seem to notice, which clichés will pass for inevitability. The visible image becomes the last event in a much longer invisible sentence.

The shift is now reaching editing as well as generation. In 2024, researchers behind ExpressEdit described a system in which users issue video-editing commands through natural language and sketching, while an LLM- and vision-based pipeline interprets temporal, spatial, and operational references and implements the edit. The edit begins semantically, before the hand touches the cut. citeturn24view0

This is the quieter control problem that cinema reveals. The standard AI control problem imagines a powerful agent and asks how to keep it aligned. The cinematic version asks something subtler and more pervasive: who controls the conditions under which images, stories, and worlds become thinkable in the first place?

BEFLIX is useful because it remains so crude. It lets us see the joints. It was inspectable, severe, explicit. A programmer could point to the command and the effect. The modern generative stack is vastly more capable, but its chains of authorship disappear into model behavior, prompt rewrites, hidden instructions, and latent representations. The more fluent the tool becomes, the less visible the site of control becomes. citeturn30view0turn2view0turn31search2turn26view0turn25view0

Return, then, to the first scene.

A person asks a language model for BEFLIX code.

At the start, it seemed like a toy request. By the end, it looks like a diagram of the entire AI-media condition. The user writes a prompt. The model writes code. The code writes motion. The motion becomes cinema. The cinema teaches the user what they meant.

The prompt is not the new camera. It is older and stranger than that. It is the instruction before the camera, the edit before the footage, the story before the world.

The future of moving images will not be decided only by cameras, actors, editors, or models. It will be decided upstream, in the languages that teach machines what can appear.

## Source Notes

*Kenneth C. Knowlton’s “Computer-Produced Movies” and the Bell Labs record.* The indispensable primary account for BEFLIX is Knowlton’s 1965 *Science* article, which explains frame structure, instruction types, and the production logic of “computer-produced movies.” I paired that with A. Michael Noll’s Bell Labs history at the Engineering and Technology History Wiki for the Bell Labs timeline, the Zajac and Sinden films, and the later BEFLIX collaborations. citeturn2view0turn18view0

*Museum framing of BEFLIX as cinema-language.* MoMA’s Knowlton program note and the Computer History Museum’s *Technology + Art* exhibition material are especially strong for placing BEFLIX inside both media history and art history: one of the first languages built for rendering and animating images, a 252-by-184 grid, about 25 command types, punched cards, and the crucial bridge from technical films to *Poemfields*. citeturn29view0turn30view0

*The “Sparks of AGI” moment.* For the cultural and conceptual force of the phrase, I relied on the original Microsoft Research paper’s abstract and on Melanie Mitchell’s *Science* essay about the wider AGI debate. That combination captures both the paper’s claim—cross-domain performance far beyond ordinary text completion—and the fact that the claim became a flashpoint in public argument about what AI systems are and what language can now control. citeturn11view0turn28view0

*Current evidence for upstream control in generative media.* The strongest primary sources here are OpenAI’s GPT-4 technical report, Codex/code-generation docs, DALL·E 3 page, 4o image-generation page, Sora technical report, Sora prompting guide, and prompt-engineering documentation. Together they show a stack in which prompts can be expanded, instructions can outrank user input, chat context can persist across image iterations, and some audiovisual properties live in API parameters rather than in the prose prompt itself. citeturn21search12turn21search0turn31search2turn23view0turn26view0turn22view0turn25view0turn25view1turn25view2

*Natural-language control migrating into editing.* ExpressEdit, presented at IUI 2024, is a useful marker for the way these ideas are moving from generation into postproduction. It shows an LLM-based pipeline treating natural-language and sketched edit descriptions as inputs for temporal, spatial, and operational video edits. citeturn24view0