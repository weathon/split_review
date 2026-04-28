# UniComposer: Band-Level Music Composition with Symbolic and Audio Unification

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3

## Abstract
Multi-track deep music generation has largely focused on pre-specified structures and instruments. However, it remains a challenge to generate "band-level" full-length music that is capable of allocating instruments based on musical features, their expressive potential, and their performance characteristics differences. Moreover, the representations of symbolic music and audio music have been treated as distinct sub-areas, without a unified architecture to join their own advantages. In this work, we introduce $\textbf{UniComposer}$, a novel music generation pipeline that composes at the band level, utilizing a hierarchical multi-track music representation complemented by four cascaded diffusion models which progressively generate rhythm features, and unified features extracted from both symbolic and audio music by autoencoders. Experiments and analysis demonstrate that UniComposer achieves a unified latent space for symbolic and audio music, and is capable of generating band-level compositions with well structured multi-track arrangements, surpassing previous methods in performances.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose a complex system termed UniComposer to generate music in the MIDI multitrack format.
 This whole system is based on a bespoke representation of music and of the compositional process.
A MIDI multitrack is decomposed into Monophony/Polyphony/Percussion, each modality having a detailed and reduced version.
Training the whole system is done in 3 steps and involves training, among others, 4 diffusion models.
The main innovation seems to include an audio encoding encoder, concatenated to a (more classical) symbolic encoder.

### Strengths
A complex system to generate MIDI multitrack.

### Weaknesses
 - With such a complex system, it is hard to understand the contribution. Differences with existing works are not clearly highlighted in the text.

- The most original contribution, which seems to consist in the addition of the audio is questionable:
The audio used as input of the audio encoder is obtained from a rendering of the MIDI file using FluidSynth (MIDI synthesizer). Such audio features are then concatenated to "symbolic features" obtained from the exact same part of the MIDI file. At the end, the model only predicts MIDI data (which are then rendered into audio).
In other words, there seems to be no additional information obtainable by considering these audio features.
 
- The accompanying website (last checked on 11/3/24) only features placeholder content
like
"Where we are today
What has your team accomplished? What are you most proud of? Tell site viewers some of your project's latest accomplishments.
Caption for a recent accomplishment
Caption for a recent accomplishment"

Overall, it seems like an overengineered system with no real novel insights, where the quality of the generations is impossible to evaluate.

### Questions
-

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a multi-track music composition algorithm containing three levels. The top level is a latent feature jointly learned from symbolic and audio sources; the middle level is music reductions of monophonic, polyphonic, and percussion tracks, and the bottom level is the actual generation. The model contains an autoencoder to learn the top-level features and cascaded diffusion models to generate the rest of the levels. Experiments show better objective metrics compared to the selected baseline.

### Strengths
Some of the design of this paper reflects the hierarchical planning involved in music generation. These are: 1) music is generated from "latent" ideas; 2) multi-track music can be categorized into different instrument types; and 3) generation is carried out from coarse-grained to fine-grained; for example, the authors leverage music reduction as an intermediate representation.

### Weaknesses
1. The motivation behind the proposed method could be clarified further. It would be helpful to understand the specific goals of the model---for example, whether it aims to enhance generation quality or address longer-term generation.
2. The demo page appears to be incomplete, which makes it challenging to assess the model’s capabilities and output quality fully. Additionally, there is no subjective evaluation. Objective metrics alone cannot provide a comprehensive understanding of the model's effectiveness.
3. The methodology is difficult to follow. The connections between graphs are unclear, as nodes are not consistently used across them, making it hard to trace the relationships. E.g., Where will the "Note feature" in Figure 3 be in other figures? Additionally, the section introduces many terms without effectively linking them, which obscures the overall approach.

### Questions
1. Could a completed demo page be provided to better assess the model’s capabilities?
2. It would be helpful to provide an explanation and add experiments on how features from symbolic music, audio, and the hierarchical design each contribute to the generation process.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces UniComposer, a diffusion-based music generation model targeting band-level, full-length music. It first introduces a hierarchical music representation from note-level attributes to bar-level encodings. On top of this, a series of diffusion models learn to generate bar encodings on the full-length level. To enhance musical structure comprehension, instruments are classified into three functional categories—monophonic, polyphonic, and percussive—each modeled by separate diffusion modules conditioned on shared melody and musical features. UniComposer also supports audio input for bar encodings, using a unified symbolic/audio latent space. Experimental results demonstrate generation quality based on objective metrics compared to baselines, with ablation studies validating the unique attention mechanism and category-specific diffusion modules.

### Strengths
* This paper presents a working scheme for hierarchical music modelling: from note-level attribute learning, via bar-level encoding, to song-level bar feature prediction. It further illustrates a scheduled training strategy, which realizes each of the three hierarchies effectively.

* By learning a unified audio/symbolic encoding space, the proposed model can also work as a transcriptor for AMT tasks, while instrument and note velocity are supported along with other note attributes.

### Weaknesses
 * Weakness in experiment:

   1. Lack of ablation study on the added audio branch: While this paper aims to "join the advantage" of both sym/audio music, one may expect the added audio branch to actually benefit symbolic music generation (otherwise, the motivation for sym/audio unification seems less sufficient). Therefore, it could be necessary to have an ablation study on the model trained with and without the audio branch. Specifically, the paper should demonstrate whether the inclusion of the audio branch improves the quality or diversity of the generated symbolic music, or if it primarily serves as a transcription pathway. The current results do not clarify the specific benefits of this unified approach for the core task of symbolic music generation.
   2. Baseline models: A few alternative baseline models that may worth refering [1, 2]
   3. Evaluation of music quality: Evaluate music generation using statistical metrics is arguably sufficient. Human study might be necessary to test the naturalness, musicality, and creativity of the generated results. The current evaluation lacks a subjective assessment of the generated music's aesthetic qualities, which is crucial for evaluating generative models in creative domains.

* Weakness in writing:
   1. Clarity in the introduction part could be further improved. The current version states "music generation" broadly, while the specific task seems to be accompaniment generation based on the later part of the paper. In other words, let the readers know the input and output of the task in the first place. This can offer an expectation to help comprehend the whole passage. Another problem lies in Line 058 which states "converts audio into symbolic format." while the model training primarily synthesizes symbolic into audio. The introduction should clearly state that the model generates accompaniment given a symbolic or audio input, and the direction of the audio-symbolic mapping should be clarified.
   2. The division between Mono. and Poly. (Line 164)  might be a bit confusing because Bass, which is mostly monophonic, is apparently grouped into Poly. Maybe here Melodic and Harmonic are better wording to name the two categories. The current grouping based on monophonic and polyphonic is not ideal, as instruments like bass can be both. Using terms like melodic and harmonic would better reflect the functional roles of instruments within the music.
   3. Line 308 introduces the cascaded diffusion models as "Transformer-based." If the reviewer understands correctly, it should actually be U-Net (convolutional) based with added self-attention modules. Note that this architecture has significant distinction from Transformers. The paper should accurately describe the architecture as U-Net based with self-attention, rather than Transformer-based, to avoid confusion.
   4. In the experiment part ( Section 4.4), there is no interpretation on the evaluation results. The paper should provide a detailed analysis of the evaluation results, explaining the significance of the metrics and how they relate to the model's performance. The current lack of interpretation makes it difficult to understand the practical implications of the reported numbers.

* Demo page is not working

### Questions
* Does the UniComposer model support any user control over the generation process? 

* How is the chord of a piece extracted (Line 208)? What is the chord resolution (i.e., #chord per bar)?

* What is the loss for the "Transformer-based" diffusion models (Line 308)? Is it MSE loss over the bar encodings?

* Could A&B (Section 4.2) compare to MT3 [1] on the multi-instrument music transcription task?

* Based on the reviewer's understanding, the Figaro model is a style transfer model, where symbolic features from piece A and audio features from piece B are required (as input) to generate a new piece. How is the Figaro model applied in this work as a baseline?

[1] J. Gardner, et al. MT3: Multi-task multitrack music transcription, in ICLR 2022.

### Soundness
3

### Presentation
1

### Contribution
2
