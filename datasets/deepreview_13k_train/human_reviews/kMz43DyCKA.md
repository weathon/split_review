# Playing For You: Text Prompt-guided Joint Audio-visual Generation for Narrating Faces using Multi-entangled Latent Space

- Decision: Reject
- Scores: 6, 5, 5, 3, 6

## Abstract
We present a novel approach for generating realistic speaking and taking faces by synthesizing a person’s voice and facial movements from a static image, a voice profile, and a target text. The model encodes the prompt/driving text, a driving image and the voice profile of an individual and then combines them to pass it to the multi-entangled latent space to foster key-vale and query for audio and video modality generation pipeline. The multi-entangled latent space is responsible for establishing the spatiotemporal person-specific features between the modalities. Further, entangled features are passed to the respective decoder of each modality for output audio and video generation. Our experiments and analysis through standard metrics showcase the effectiveness of our model. All model checkpoints, code and the proposed dataset can be found at: https://github.com/Playing-for-you.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel framework for jointly generating the visual and audio cues of talking faces based on a text prompt, an image, and an audio profile. This work addresses issues such as poor lip synchronization and limited expressiveness in previous approaches which synthesize the visual and audio cues separately. This approach introduces a multi-entangled latent space to align audio-visual elements. The model utilizes transformers and diffusion models to achieve precise, person-agnostic synchronization of voice and facial expressions. Quantitative results of this work demonstrates favorable performance over baselines across multiple datasets.

### Strengths
1. Synthesizing audio and video together based on text input addresses a meaningful setting in talking faces generation.
2. The framework design appears reasonable, employing attention mechanisms for effective cross-modal fusion, and the presentation is overall clear.
3. The quantitative results suggest a notable improvement in quality over recent approaches, with favorable scores in metrics like FVD, FID, and FAD.
4. The ablation study shows that key techniques are effective.

### Weaknesses
1. The experiments seems to lack a dedicated evaluation for audio-visual synchronization, which is identified as a problem this paper aims to address. Specifically, while the paper mentions addressing lip synchronization, there isn't a clear metric or analysis that directly quantifies the temporal alignment between the generated audio and the lip movements in the synthesized video. This makes it difficult to ascertain whether the proposed method truly achieves improved synchronization compared to existing methods. 
2. Without qualitative results, such as playable video and audio samples, it’s challenging to fully assess and compare critical aspects like coherence, smoothness, synchronization, realisticness and expressiveness. The two examples provided in the GitHub link are a helpful start, but a broader range of samples would provide a more comprehensive evaluation. The limited examples make it difficult to assess the robustness of the method across diverse subjects and conditions, such as different lighting, head poses, and speech styles.

### Questions
1. The framework consists of many modules. Could you elaborate which of these components use pretrained weights, and which are being trained?
2. Fig.3 and Fig.4 presents frames from generated videos. Could you explain how were these frames sampled?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper presents a novel approach for generating realistic speaking faces by synthesizing a person's voice and facial movements from a static image, a voice profile, and a target text. The model uses a multi-entangled latent space to integrate text, image, and audio data for synchronous audio-video generation. The proposed architecture consists of three phases: encoding, multi-entangled latent space, and decoding. The model demonstrates superior performance compared to state-of-the-art methods across various datasets.

### Strengths
(1) The use of a multi-entangled latent space for integrating multiple modalities is novel and addresses existing limitations in synchronous audio-video generation. (2) The three-phase model (encoding, latent space, decoding) ensures effective processing and generation of audio-visual content. (3) The model shows superior performance on multiple datasets, indicating its robustness and generalization capability.

### Weaknesses
(1) The multi-entangled latent space and cross-modal attention mechanisms seem quite complex. More ablation studies are needed to analyze their individual contributions, specifically regarding the impact of each modality's encoder and attention mechanism on the final generation quality. It's unclear how much each component contributes to the overall performance, and whether simpler architectures could achieve comparable results with less complexity. (2) Computational cost and generation time are not discussed. The multi-stage framework with transformers and diffusion models may be expensive to train and slow during inference. The lack of information about parameter size, FLOPs, and inference time makes it difficult to assess the practical applicability of the model. (3) Dependence on a clean audio profile of the target identity may limit applicability in certain scenarios. Robustness to noise needs to be evaluated, including different types of noise (e.g., background noise, reverberation, and speech overlap) and varying signal-to-noise ratios.

### Questions
(1) How does the model handle diverse accents and languages in the audio input?
(2) What are the computational requirements for training and deploying this model?
(3) Can the model be adapted for real-time applications, and if so, what are the latency implications?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a model designed for generating realistic, synchronized audio and video of a person speaking based on a static image, an audio profile, and a text prompt. The model uniquely integrates visual and audio features within a "multi-entangled latent space," allowing for synchronous facial animation and audio output that align with the speaker’s identity and the specified text. The model outperforms existing methods in video and audio quality, showing improvements in metrics such as FID for visual quality and MCD for audio quality.

### Strengths
1. The paper presents the proposed approach in a clear and comprehensible manner.
2. The method demonstrates strong performance across multiple benchmark datasets.
3. The accompanying code is provided, facilitating reproducibility and further analysis.

### Weaknesses
1. The paper claims that all model checkpoints and the proposed dataset are provided via a GitHub link. However, I was unable to locate these resources.
2. The clarity of several figures, such as Fig. 1, Fig. 3, and Fig. 4, could be improved. The current quality detracts from the overall readability and reader experience.
3. The paper lacks essential technical details, such as the selection of hyperparameters, the number of training iterations, training time, and the balance of loss functions.

### Questions
Please refer to Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper addresses the combined tasks of text-to-speech modeling, which generates audio from text input, and talking face modeling, which produces a video of a person speaking for audio or text as input. In contrast to previous work (Faces that Speak by Jang et al., 2024) that solved this combined task (inputs: text, image. outputs: audio, talking video), this paper incorporates reference audio as an additional input.  That is, the task can be summarized as generating text-to-speech and talking face video with additional conditioning on reference audio (inputs: text, image, reference audio. outputs: audio, talking video)

### Strengths
- This approach has potential applications in real-world scenarios. 
- The experiments demonstrate a measurable performance improvement.

### Weaknesses
 - The technical contributions in the paper are minimal, as the task is primarily addressed by combining existing architectures trained for individual tasks (e.g., Hallo: Hierarchical Audio-Driven Visual Synthesis for Portrait Image Animation Xu et al. (2024a) for video generation, the MEL-spectrogram synthesizer based on the X-Text-to-Speech (XTTS) model by Casanova et al. (2024), and other various input encoders). Given the reliance on these pre-trained networks from prior works, one might question whether the proposed task could have been approached as a zero-shot solution.

- For the proposed architectural components, there is a lack of ablation studies to demonstrate their relevance, particularly concerning the transformer encoders that facilitate interactions between different modalities before proceeding to the generation modules. It would have been beneficial for the authors to include ablation studies that clarify which modality interactions are essential for each generation task and how performance varies as a result. Currently, the ablation study only provides results for removing both encoders and for sharing encoders.


### Questions
- In the prompt-guided transformer encoder attention, how would removing the vision tokens impact audio generation? What role do the vision tokens play in audio generation?
- In Tables 1 and 2, could you clarify which reported performance values of previous works were re-evaluated by you and which were directly taken from the original papers? It seems that many values have been re-evaluated. If all the reported values are re-evaluated, why were at least some commonly used benchmark datasets not employed to allow for direct comparisons with other papers?
- Does using reference audio during training cause the model to develop biases that link specific visual facial features with certain audio profiles? At inference time, can the model overcome these potential biases? For example, if a child’s voice is used as the reference audio but the input image is of an adult male, will the generated voice adapt to match the adult’s appearance, or retain the characteristics of the child’s voice?
Note: If the output does not retain the childlike qualities of the reference audio, this indicates the model has learned a bias.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a multimodal model aimed at generating synchronized audio-visual output based on input prompts. It combines static images, voice profiles, and target texts in a multi-entangled latent space to produce both speech and corresponding facial movements. The model comprises three main phases: encoding, entangled latent space formation, and decoding for generating output audio and video

### Strengths
- Introducing a multi-entangled latent space for synchronizing audio and visual modalities, potentially bridging the gap between current single-modality generation models and real-world applications requiring synchronized outputs.

- The model was ested on multiple datasets (VoxCeleb, CelebV-HQ, HDTF).

### Weaknesses
 - Utilizing HiFi-GAN, Wav2Vec, and multiple Transformers implies significant computational resources, but the paper fails to discuss resource efficiency, scalability, or training costs. This may pose practical limitations, especially in deployment on lower-resource devices.

- The "multi-entangled latent space" concept, while promising, lacks clarity in its practical execution, especially regarding how it manages and aligns the complex temporal features across audio and visual modalities. Detailed insight into the entanglement mechanism would enhance the model's comprehensibility and reproducibility.

- While lip synchronization is briefly mentioned, it lacks thorough quantitative and qualitative analysis. Lip-sync accuracy and expressiveness are critical in applications requiring realistic facial animations, yet these elements are not comprehensively evaluated in the paper.

- Given the potential misuse in generating realistic, personalized talking faces, ethical considerations are necessary. The authors should address potential implications, such as privacy risks, unauthorized identity mimicry, or the generation of deepfakes, to ensure responsible use.

- Missing important previous work

Xu, Chao, et al. "FaceChain-ImagineID: Freely Crafting High-Fidelity Diverse Talking Faces from Disentangled Audio.",CVPR 2024

### Questions
- Can you clarify the role and specifics of the multi-entangled latent space? How does it manage spatiotemporal alignment across the modalities?

- Are there ethical safeguards or limitations implemented to mitigate misuse, given the realistic nature of the generated outputs?

- Missing important previous work

Xu, Chao, et al. "FaceChain-ImagineID: Freely Crafting High-Fidelity Diverse Talking Faces from Disentangled Audio.",CVPR 2024

### Soundness
3

### Presentation
3

### Contribution
3
