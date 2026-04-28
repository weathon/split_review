# SoundCTM: Unifying Score-based and Consistency Models for Full-band Text-to-Sound Generation

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
Sound content creation, essential for multimedia works such as video games and films, often involves extensive trial-and-error, enabling creators to semantically reflect their artistic ideas and inspirations, which evolve throughout the creation process, into the sound.
Recent high-quality diffusion-based Text-to-Sound (T2S) generative models provide valuable tools for creators. However, these models often suffer from slow inference speeds, imposing an undesirable burden that hinders the trial-and-error process.
While existing T2S distillation models address this limitation through $1$-step generation, the sample quality of $1$-step generation remains insufficient for production use.
Additionally, while multi-step sampling in those distillation models improves sample quality itself, the semantic content changes due to their lack of deterministic sampling capabilities.
Thus, developing a T2S generative model that allows creators to efficiently conduct trial-and-error while producing high-quality sound remains a key challenge.
To address these issues, we introduce Sound Consistency Trajectory Models (SoundCTM), which allow flexible transitions between high-quality $1$-step sound generation and superior sound quality through multi-step deterministic sampling. 
This allows creators to efficiently conduct trial-and-error with $1$-step generation to semantically align samples with their intention, and subsequently refine sample quality with preserving semantic content through deterministic multi-step sampling.
To develop SoundCTM, we reframe the CTM training framework, originally proposed in computer vision, and introduce a novel feature distance using the teacher network for a distillation loss. 
Additionally, while distilling classifier-free guided trajectories, we introduce a $\nu$-sampling, a new algorithm that offers another source of quality improvement. For the $\nu$-sampling, we simultaneously train both conditional and unconditional student models.
For production-level generation, we scale up our model to 1B trainable parameters, making SoundCTM-DiT-1B the first large-scale distillation model in the sound community to achieve both promising high-quality $1$-step and multi-step full-band (44.1kHz) generation.
Audio samples are available at \url{https://anonymus-soundctm.github.io/soundctm_iclr/}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper presents a diffusion-based text-to-audio generation system within the Consistency Trajectory Model (CTM) framework, named SoundCTM. SoundCTM is developed using distillation loss with a teacher model, and incorporates a novel sampling algorithm that enables Classifier-Free Guidance (CFG) integration with the student model. Experimental results demonstrate that SoundCTM achieves state-of-the-art performance in 1-step and few-step generation for 44.1 kHz full-band samples, offering a practical tradeoff between generation quality and inference speed for real-world applications.

### Strengths
1. Results indicate that the proposed large-scale SoundCTM-Dit-1B achieves state-of-the-art performance in text-to-audio generation in the full-band setting (mono at 44.1 kHz).
2. Instead of using the L2-norm loss between target and output values within the latent domain, this paper introduces a network trained with CTM loss, leveraging a teacher network for feature extraction and measurement. Results show that the proposed teacher loss achieves superior performance.
3. This paper integrates Classifier-Free Guidance (CFG) within the CTM framework by distilling the CFG-related PF ODE trajectory during training and using it as the CFG condition. Additionally, a new sampling strategy has been developed to enable CFG in 1-step generation.

### Weaknesses
1. The comparison results show that the proposed system achieves state-of-the-art performance in single-step sampling, while SoundCTM does not surpass baseline models (e.g., AudioLCM, also a diffusion model with CTM) when increasing the sampling steps (from 2 steps onward). Additionally, there is a lack of comparison in inference speed between different distillation models. Further explanation is required for why baseline models outperform SoundCTM in few-step sampling.
2. Further explanation is required for why baseline models outperform SoundCTM in few-step sampling. Moreover, the CLAP score is the only metric related to semantic alignment (text), yet it does not seem well-aligned with other metrics, such as FAD and IS. It would therefore be beneficial to conduct human evaluations for each experiment to better illustrate performance.
3. The authors claim that SoundCTM-Dit-1B achieves the best results in full-band generation tasks. However, SoundCTM used for comparisons among 16 kHz models employs a UNet-based backbone, resulting in unaligned experiments. The paper lacks sufficient explanations, ablation studies, or comparisons to demonstrate the effectiveness of each submodule. The authors could address this by adding SoundCTM-DIT medium or small models for 16 kHz comparisons and SoundCTM-UNet-1B for full-band comparisons.

### Questions
1. Is the hyperparameter 𝑣 mentioned in Section 3, which is used for sampling, trainable? If not, how did the authors determine its value? The same question applies to the scale of CFG 𝑤
2. For the results in Table 2, what is the best performance SoundCTM can achieve? With additional sampling steps, can SoundCTM surpass the quality of AudioDLM2-large?
3. What are the differences between SoundCTM and AudioLCM, aside from the teacher CTM loss proposed for training? Both systems are diffusion-based generation models employing consistency strategies.
4. The authors also state that SoundCTM and AudioLCM show clear trade-offs in multi-step generation. What is the inference efficiency of these two systems? The authors mentioned early on that the proposed system is intended to overcome the barrier of slow inference speeds encountered during trial-and-error.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes Sound Consistency Trajectory Models (SoundCTM) for improving inference speed and sample quality in Text-to-Sound (T2S) tasks by combining score-based and consistency models. This work mainly adapting existing techniques from image generation for T2S.  From the reported results, SoundCTM can generate sound in few inference step.

### Strengths
1. The paper introduces Sound Consistency Trajectory Models (SoundCTM), an approach that unifies score-based and consistency models for Text-to-Sound (T2S) generation. This combination is interesting and reflects a novel direction within the T2S domain, especially in adapting techniques from image generation. 

2. The paper evaluates SoundCTM at both 16kHz and 44.1kHz, showing an awareness of high-fidelity audio generation.

### Weaknesses
 1. The paper proposes Sound Consistency Trajectory Models (SoundCTM) to improve inference speed. While the concept of combining score-based and consistency models for T2S generation is interesting, the paper does not convincingly establish the novelty of its contributions. Many of the methods, including ν-sampling and trajectory-based distillation, are either borrowed from existing frameworks or lack adequate differentiation from prior work. A clearer and more distinct innovation beyond adapting methods from image-based models is needed to justify the novelty of this work.

 2. The paper emphasizes deterministic sampling as a unique advantage of SoundCTM, particularly for preserving semantic content across sampling steps. However, this advantage remains largely theoretical within the paper, with insufficient empirical evidence demonstrating the effectiveness of deterministic sampling in real production scenarios. The provided spectrograms and subjective evaluations do not strongly support the claimed benefits, and thus, the deterministic aspect feels overstated relative to its demonstrated impact.

 3. The paper highlights full-band sound generation. However, all previous work can support full-band sound generation by simply replacing 16kHz audio data with 44.1kHz data.

 4. In terms of performance, SoundCTM shows some advantages over AudioLCM and ConsistencyTTA. However, as SoundCTM scales to a 1B parameter model, it is difficult to determine whether the improvements are due to model scaling alone.

 5. From an architectural perspective, the proposed DiT framework closely follows the architecture of Stable Audio 2.0.

 6. In the related work section, the paper claims that "when developing sound generative models suitable for production use, LDM-based models present a better choice as the base model." It is difficult to agree with this claim. Previous works, such as AudioGen, have also demonstrated good performance in T2S. For example, DiffSound shows that using a discrete diffusion model yields better performance than an AR-based baseline. After that, AudioGen demonstrates that AR-based models can also achieve good performance with different configurations. Given the rapid development of T2S, it is premature to make such a claim. In the field of image generation, some studies have shown that AR-based models can outperform LDM-based models. Additionally, discrete diffusion models remain an important research direction.

### Questions
Please refer to Weaknesses.

1. What your training dataset?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a new Sound Consistency Trajectory Model (SoundCTM) to accelerate the iterative trial-and-error process of sound design using audio generation models.

Compared with previous 1-step distillation methods, SoundCTM provides deterministic sampling capabilities, which enables acoustic consistency between 1-step and multi-step generations from the same initial noise latent.

Creators can use SoundCTM in the fast 1-step setting for exploratory work while benefitting from the higher quality of multi-step inference once a relevant generated sample has been chosen.

The authors claim the following contributions.
- Adaptation of the computer vision domain CTM training framework to the audio domain (called SoundCTM).
- A novel feature distance for distillation loss computation.
- v-sampling: a new cfg-like approach that consists in training both conditional and unconditional student models.
- SoundCTM-DiT-1B, a large scale distillation model that achieves sota 1-step and multi-step full-band text-to-sound generation on the AudioCaps evaluation dataset.

The results indicate better consistency between 1-step and multi-step generation compared with previous sota.

### Strengths
- Showcasing a potential downstream application of the proposed method is a nice addition to the work.
- Speed and inference consistency between 1-step/multi-step inference is a fundamental problem in the sound design space and this paper properly tackles this problem.

### Weaknesses
 - It is not clear how v-sampling differs from CFG hence it is difficult to appreciate the relevance of the contribution.
- It is unclear why the proposed distilled model outperforms its teacher.
- The explanation of v-sampling lacks clarity regarding the number of student models involved. It's stated that both conditional and unconditional models are used, but the exact implementation details and their interaction are not sufficiently described in section 3.3 and algorithm 2, making it hard to understand the proposed method.
- The paper does not provide a clear explanation of why the distilled model, SoundCTM-DiT-1B, outperforms its teacher model. This raises concerns about the training process and the specific mechanisms that lead to this improvement, which should be further investigated and explained.
- There is an inconsistency between the results presented in Table 1 and Table 2. Specifically, the last row of Table 1 and the second to last row of Table 2, which seem to refer to the same experiment, show different values without a clear explanation for this discrepancy.

### Questions
- In v-sampling, it is not clear whether there is one or two student models involved. From the abstract it seems that there are two but not from section 3.3 and algorithm 2.
- In what sense is v-sampling different than CFG applied to the student model?
- What is the difference between the last row of Table 1 and the second to last row of Table 2? They do not indicate the same values although they seem to relate to the same experiment.
- How do you explain that SoundCTM-DiT-1B outperforms the teacher model?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces SoundCTM, a novel approach to T2S generation that aims to enhance the efficiency and quality of sound creation in multimedia applications such as video games and films. By addressing the limitations of existing diffusion-based T2S models—which often suffer from slow inference speeds and subpar sample quality in 1-step generation—SoundCTM offers a flexible framework that allows for rapid trial-and-error through high-quality 1-step generation and subsequent refinement via multi-step deterministic sampling, all while preserving semantic content. The authors adapt the CTM training framework from computer vision, introducing a new feature distance metric that leverages the teacher network for distillation loss. They also propose a novel ν-sampling algorithm, enhancing the quality of multi-step generation. The model successfully scales up to one billion parameters, achieving promising results in both 1-step and multi-step full-band sound generation.

### Strengths
1. SoundCTM enables creators to quickly generate initial sound samples using high-quality 1-step generation and then refine these samples through multi-step deterministic sampling without altering the semantic content. This flexibility is highly valuable in practical sound design workflows.

2. By introducing a new feature distance metric that uses the teacher's network as a feature extractor for the distillation loss, the model enhances knowledge transfer from the teacher to the student. This approach leads to better performance compared to traditional L2 loss or external models, as it more effectively captures nuanced features relevant to sound generation.

3. The introduction of ν-sampling is a significant contribution. By combining conditional and unconditional student models, ν-sampling improves the quality of multi-step generation and provides another avenue for quality enhancement.

4. The ability to maintain semantic consistency across different sampling steps is crucial for practical applications. SoundCTM effectively addresses this by enabling deterministic sampling, which is essential for sound designers who require consistent outputs during refinement.

### Weaknesses
1. While the authors mention that preliminary experiments with GAN loss did not yield improvements, they do not deeply explore alternative strategies or provide a thorough analysis of why GAN loss integration was unsuccessful. A more detailed investigation, including specific discriminator architectures and training methodologies, could potentially uncover methods to enhance the model's performance, especially in 1-step generation. The lack of exploration into latent space GANs, for example, is a notable gap.

2. Relying on the teacher's network as a feature extractor may limit the model's flexibility, particularly if the teacher and student models are trained on different datasets or domains. This dependency could pose challenges when attempting to generalize the model to new or diverse datasets, and the paper does not sufficiently address the potential for domain shift issues or how the feature space of the teacher might not be optimal for all student training scenarios.

3. The paper briefly demonstrates the application of SoundCTM to downstream tasks like controllable generation but does not explore this in depth. A more comprehensive study on various applications, including a wider range of control mechanisms and a more thorough evaluation of performance in each, could showcase the versatility of the model. The lack of exploration into tasks like audio style transfer or bandwidth extension is a missed opportunity.

4. The paper does not provide a comparison between SoundCTM and flow matching approaches. Such a comparison could offer valuable insights into the advantages or limitations of the proposed method relative to other leading techniques in the field, particularly in terms of computational efficiency and sample quality. A more detailed analysis of the trade-offs between these approaches is needed.

### Questions
1. Do the authors plan to explore alternative GAN architectures or training strategies to effectively integrate GAN loss and potentially enhance the quality of 1-step generation? Understanding the obstacles faced and possible solutions could be beneficial for future work.

2. How does SoundCTM perform when the teacher and student models are trained on different datasets? Additionally, how well does the model adapt to other audio domains such as music generation or speech synthesis? Insights into its generalizability would be valuable.

3. Can the authors provide more detailed insights into the ν-sampling algorithm? Specifically, how does ν-sampling impact the model's performance compared to standard sampling methods, and what are the theoretical underpinnings that justify its effectiveness?

4. Have the authors considered using external pretrained networks as feature extractors for the distillation loss? If so, how might this affect the model's performance and flexibility, especially in scenarios where the teacher network is not available or differs significantly from the student?

5. How does SoundCTM compare with flow matching methods in terms of performance, computational efficiency, and ease of implementation? Are there specific advantages in choosing SoundCTM over flow matching approaches for text-to-sound generation tasks?

6. Beyond text-to-sound generation, can SoundCTM be applied to other audio-related tasks such as speech synthesis, audio style transfer, or sound enhancement? What adaptations would be necessary, and how might it perform compared to specialized models designed for those tasks?

### Soundness
3

### Presentation
3

### Contribution
3
