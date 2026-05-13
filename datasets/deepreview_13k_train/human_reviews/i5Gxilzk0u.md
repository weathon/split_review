# Multi-modal Controlled Coherent Motion Synthesis

- Decision: Reject
- Scores: 5, 5, 5, 6, 8

## Abstract
We walk and talk at the same time all the time. It is just natural for us. This paper tackles the challenge of replicating such natural behaviors in 3D avatar motion generation driven by concurrent multi-modal inputs, e.g., a text description ``a man is walking" alongside a speech audio. Existing methods, constrained by the scarcity of aligned multi-modal data, typically combine motions from individual modalities sequentially or through weighted averaging. These strategies often result in mismatched or unrealistic movements. To overcome these limitations, we propose MOCO, a novel diffusion-based framework capable of processing multiple simultaneous inputs—including speech audio, text descriptions, and trajectory data—to generate coherent and lifelike motions without requiring additional datasets. Our key innovation lies in decoupling the motion generation process. During each denoising step, the diffusion model independently generates motions for each modality from the input noise and assembles the body parts according to predefined spatial rules. The resulting combined motion is then diffused and serves as the input noise for the subsequent denoising step. This iterative approach enables each modality to refine its contribution within the context of the overall motion, progressively harmonizing movements across modalities. Consequently, the generated motions become increasingly natural and fluid with each iteration, achieving coherent and synchronized behaviors. We evaluate our approach using a purpose-built multi-modal benchmark. Experimental results demonstrate that MOCO significantly outperforms existing baselines, advancing the field of multi-modal motion generation for 3D avatars. The code will be released.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes MOCO, a diffusion-based framework for generating coherent motions from multi-modal inputs like text, speech, and trajectory data. It addresses the challenge of simultaneous multi-modal control in 3D avatar motion generation. The key innovation is a decoupled denoising process that generates and combines motions for each modality. Experiments on a custom benchmark show it outperforms baselines.

### Strengths
(1) MOCO is quite straightforward and achieves better realism and coherence compared to existing methods that process modalities through weighted averaging.
(2) Comprehensive evaluation: The use of a purpose-built multi-modal benchmark and a wide range of metrics for evaluation provides a thorough assessment of the method's performance.
(3) The writing of paper is clear without ambiguities.

### Weaknesses
 (1) While the paper mentions trajectory control, the evaluation focuses primarily on text-to-motion and speech-to-gesture tasks. A more comprehensive evaluation of trajectory control, including metrics specific to this modality, would be beneficial. Specifically, the paper should include metrics that assess the accuracy of the generated trajectory in terms of both position and orientation, and consider both average error and final goal error. Furthermore, the evaluation should include a comparison with existing trajectory control methods.

(2) The statistics of Multi-Modal Benchmark are missing.

(3) A Qualitative comparion among different methods (like User Study) are missing.

(4) The results of many evaluation metrics  are not promising at all, also authors only provided a cherry-picked video as demo, the effectiveness of this method is not so convincing. The paper lacks a thorough analysis of why the proposed method does not perform well on certain metrics. The provided video demo, while visually appealing, does not provide sufficient evidence of the method's robustness across a diverse range of inputs. The paper should include a more comprehensive set of qualitative results, including failure cases, to provide a more balanced view of the method's capabilities and limitations.

(5)  Lacking theorical analysis of how decoupled-then-combined denoising works. Also, I am curious whethe is a general paradigm for multi-modal condition generation or only for this setting.

### Questions
(1) How about the performance comparison between "Synchronous" and  "Asynchronous" conditions?

(2) How many clips does your methods support to generate?(each one might be conditioned on several condition), and how the performance changes with the number of clips. Because your Figure 1. and demo video show you support this feature.

### Soundness
3

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
3

### Summary
The paper introduces MOCO, a diffusion-based framework for generating 3D avatar motion driven by simultaneous multi-modal inputs, such as speech audio, text descriptions, and trajectory data. A novel decoupling mechanism that allows upper-body and lower-body motions to be generated separately and integrated cohesively is proposed, ensuring realistic behavior across modalities. Experiments on a purpose-built benchmark show that MOCO outperforms existing methods on generating synchronized and lifelike avatar motions.

### Strengths
1. MOCO introduces the first approach to handle simultaneous multi-modal inputs (speech, text, and trajectory) in motion synthesis, overcoming the limitations of sequential or averaged methods used in previous work.

2. The framework’s decoupling strategy, which independently processes each modality and then integrates them according to spatial rules, ensures high alignment and coherence across modalities, leading to realistic and synchronized avatar behavior.

### Weaknesses
1. Limited Real-World Testing: The experiments primarily focus on controlled benchmarks and do not demonstrate how MOCO performs in real-world or diverse environments, which limits understanding of its practical application. Specifically, the paper lacks evaluation on scenarios with noisy or out-of-domain audio, and how the system handles the complexities of real-world human motion capture data, which often contains artifacts and inconsistencies not present in clean datasets.

2. Analysis of Failure Cases: The paper lacks an in-depth analysis of failure modes or specific situations where MOCO might struggle, such as handling overlapping or conflicting input conditions from different modalities. For example, it is unclear how the system resolves conflicts when the text description implies a static pose while the audio input suggests dynamic movement, or how it handles ambiguous text descriptions that could be interpreted in multiple ways.

3. The paper does not include user studies or subjective assessments to gauge the perceived naturalness and quality of the generated motions, which would add practical validation to the quantitative results. The absence of user studies makes it difficult to assess whether the generated motions are perceived as realistic and coherent by human observers, which is a critical aspect of evaluating motion synthesis methods.

4. Although MOCO excels at combining multiple modalities for coherent motion generation, its joint performance comes at the expense of not achieving the highest scores in any single domain. This raises questions about the trade-offs made in the design of the model and whether it is possible to optimize for both joint and single-modality performance.

5. The paper provides qualitative results but lacks detailed video examples or demonstrations of the generated outputs. The static images provided do not sufficiently convey the temporal dynamics and fluidity of the generated motions, making it difficult to assess the quality of the results.

### Questions
1. While MOCO performs well across joint multi-modal metrics, it does not surpass single-modality baselines in their respective domains. Have you considered methods to optimize modality-specific contributions without compromising joint performance?

2. Have you considered conducting user studies or collecting subjective feedback to assess the perceived naturalness and coherence of MOCO’s generated motions? This would provide additional validation for the results.

3. Could you provide more examples or analysis of specific scenarios where MOCO struggles, such as when input modalities provide contradictory cues or when generating highly dynamic or complex movements?

4. Could you provide video samples to showcase MOCO's performance visually? This would be highly beneficial for evaluating the naturalness and coherence of the synthesized motions.

### Soundness
2

### Presentation
3

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
The paper introduces MOCO, a novel diffusion-based framework for 3D avatar motion synthesis that effectively integrates multi-modal inputs such as text descriptions, speech audio, and trajectory data. By independently modeling each modality using transformer-based denoisers and employing a decoupled denoising process, MOCO generates fluid and coherent motion sequences. The framework splits motion generation into upper-body movements driven by speech and lower-body movements influenced by text, refining each component iteratively. It also incorporates trajectory data to guide global body transitions and manages asynchronous conditions with a timeline-based strategy. Experiments on datasets like HumanML3D, BEATX, and a custom multi-modal benchmark demonstrate that MOCO outperforms baseline models, achieving superior synchronization and coherent motion. The paper suggests potential improvements to address minor limitations such as foot sliding during transitions.

### Strengths
Originality: The paper presents a novel framework that effectively combines multiple modalities for motion synthesis, addressing a significant gap in existing research.
Quality: The decoupled denoising approach is well-designed, allowing for independent modeling of upper-body and lower-body movements, which enhances the coherence and synchronization of generated motions.
Clarity: The methodology is clearly explained, with detailed descriptions of the transformer-based denoisers and how they interact within the framework.
Significance: The ability to synthesize lifelike motion sequences from multi-modal inputs has important implications for virtual avatars, gaming, and animation industries.

### Weaknesses
Computational Complexity: The paper lacks a discussion on the computational efficiency and scalability of the proposed framework, which is crucial for real-time applications. Specifically, the paper does not provide details on the number of parameters, FLOPs, or inference time of the model, making it difficult to assess its practical viability. The absence of this information raises concerns about the feasibility of deploying MOCO in resource-constrained environments or for interactive applications.
Limited Ablation Studies: While an ablation study is mentioned, more extensive experiments isolating the contributions of each component could strengthen the evaluation. The current ablation study does not delve into the impact of individual denoisers or the specific contributions of the decoupled denoising approach. A more thorough analysis, such as varying the number of transformer layers or the dimensionality of the latent spaces, would provide a more granular understanding of the framework's performance.
Dataset Diversity: The datasets used may not cover all possible real-world scenarios, potentially limiting the generalizability of the results. The paper does not address the potential for domain shift when applying MOCO to datasets with different characteristics, such as variations in motion styles or environmental contexts. This lack of evaluation on diverse datasets raises questions about the robustness of the framework in real-world applications.
Minor Artifacts: The issue of foot sliding during transitions is acknowledged but not thoroughly addressed, leaving room for improvement in motion realism. The paper does not provide a detailed analysis of the causes of foot sliding or propose specific solutions to mitigate this artifact. This issue could be particularly noticeable in scenarios involving rapid changes in motion or complex transitions.

### Questions
How does MOCO perform in terms of computational efficiency, especially in real-time applications?
Can the authors provide more details on how the decoupled denoising approach affects the overall computational complexity?
Have the authors considered the integration of additional modalities, such as facial expressions or environmental context?
What strategies could be employed to mitigate the foot sliding issue during motion transitions?
How generalizable is MOCO to scenarios beyond the datasets used, particularly in more complex or varied environments?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work addresses a very specific problem in 3D human motion— speech generation, which involves generating both body movement and detailed facial and hand gestures conditioned on text , speech audio and trajectory. Specifically, the proposed method uses four models to achieve (1) text to lower body motion, (2) speech to upper body motion, (3) speech audio to facial and hand details, and (4) trajectory to global velocity, to synthesize actions for walking and talking simultaneously. Overall, the method is clear, and achieves state-of-the-art results in the benchmark made by mixed HumanML3D and BEATX.

However, I feel that the work’s novelty might be somewhat limited. This work focuses on a specific application. Although it could be useful for speech generation, it doesn’t seem to demonstrate other areas of extensibility. Methodologically, it seems more like a combination and application of existing models, without considering deeper connection between speech content and body movement.

--------
The authors provided experiments that use LLM as a high level guider/coodinator. These experiments seem interesting and inspiring, and they show a potential to broader and easier use of this method. Therefore I raise the score from 5 to 6.

### Strengths
+ The problem of speech motion generation is interesting and has application value (although it may seem somewhat overly specific for a machine learning conference).

+ The writing is clear. Each part of the proposed method is reasonable.

+ The experiments are thorough. The benchmark is well-considered, addressing both movement (HumanML3D) and detailed gestures (BEATX). The ablation study is also comprehensive.

### Weaknesses
 - Although the method is reasonable, it still appears to be a combination of different body parts. These combinations sometimes don’t look entirely natural. For instance, around the 23 second in the demo, when the human starts moving, the upper and lower body seem somewhat unnaturally separate. Normally, human upper and lower movements have some interrelated dynamics (based on physical balance or habit), which I didn't see the authors address in the proposed solution.

- The proposed method seems to rely on precise, pre-arranged text and speech audio clips rather than handling this autonomously. Specifically, given a speech content, the method does not help users plan when to say what or when to perform certain actions, which could limit its application scenarios. Perhaps the authors could consider using LLMs to assist with some high-level planning or text-conditioned generation? I believe doing so would not add too much workload but could make the method much fancier.

- There appears to be a lack of semantic-level coherence between the speech content and the motion. In the demo, gestures seem to change with the rhythm of the speech, but the motion itself seems to lack meaning or understanding. Again, have the authors considered using language models to generate movement details that are more closely aligned with the content of the speech?

- This work involves different modality conditions, one of which is audio to motion. However, some important references on "audio to motion," such as dance generation (e.g., Bailando, CVPR 2022, and EDGE, CVPR 2023), seem to be missing.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a diffusion-based framework aimed at generating realistic and coherent 3D avatar motions driven by concurrent multimodal inputs, such as text descriptions and speech audio. The key innovation of MOCO lies in its decoupled motion generation process, which independently produces motions for each modality from input noise and assembles body parts according to predefined spatial rules. This iterative approach enables each modality to refine its contribution within the context of the overall motion, resulting in increasingly natural and fluid movements that achieve coherence and synchronization across modalities.

The authors tackle the challenge of aligning motions with multiple control signals by proposing a method that simultaneously processes speech audio, text descriptions, and trajectory data, eliminating the need for additional datasets. The MOCO framework is trained on various datasets to ensure it can independently generate motions conditioned on either text or speech inputs. At each denoising step, the model generates distinct motions for the upper and lower body, conditioned on speech and text, respectively, and combines them to produce a cohesive motion that is then diffused for the next iteration. Additionally, the paper introduces a multi-modal benchmark for evaluating the proposed method.

### Strengths
The paper introduces a diffusion-based framework for multi-modal controlled motion synthesis, characterized by its innovative approach to decoupling motion generation. 
- This decoupling facilitates the independent processing of speech audio, text descriptions, and trajectory data, effectively addressing a significant gap in the field where aligned multi-modal data is limited.
- The authors develop a purpose-built multimodal benchmark that enhances the validity of their claims.
- The paper is well-structured and clearly articulated. The introduction presents a compelling motivation.

### Weaknesses
 **Performance in Single-Modality Scenarios:** The paper does not provide a direct comparison of MOCO's performance when operating in single-modality scenarios (text-only or audio-only) against existing text-to-motion (T2M) and audio-to-gesture (A2G) methods. While MOCO is designed for multi-modal input, discussing its performance in these more constrained scenarios is crucial. Specifically, the paper lacks quantitative results demonstrating how MOCO's performance in text-only scenarios compares to state-of-the-art T2M models, and similarly for audio-only scenarios against A2G models. This absence makes it difficult to assess the trade-offs of using a unified multi-modal framework versus specialized single-modality models.

**Conflict Resolution in Multi-Modal Control:** The paper describes a decoupled approach where audio primarily influences upper-body motion and text influences lower-body motion. However, it does not explicitly address how conflicts between modalities are resolved, particularly for the upper body. For instance, if text suggests a specific arm movement while audio cues indicate a different gesture, it is unclear how MOCO would reconcile these instructions. The paper would benefit from a more detailed discussion on conflict resolution strategies, including the specific mechanisms used to prioritize or blend conflicting cues, and potential limitations this might introduce. Experimental analysis demonstrating how such conflicts are handled and the impact on motion coherence would strengthen the paper's contributions. For example, a scenario where text specifies 'raising both arms' while speech implies 'waving one hand' needs clarification on how the model would generate the motion.

**Specificity in Upper Body Motion Control:** While the decoupled approach is innovative, the paper lacks specificity on how upper body motion is controlled when both audio and text are provided. It is not detailed whether the model prioritizes one modality over the other in case of conflict, or if there is a blending strategy that integrates both inputs effectively. The paper should clarify the conditions under which text-based upper body motion control is possible, and how this interacts with audio-driven gestures. Clarifying the control mechanism and its implications on motion realism and coherence is essential for a comprehensive understanding of MOCO's capabilities and limitations. For instance, if the text describes a 'punching' motion while the audio suggests a 'nodding' motion, the paper should detail how the upper body motion is determined.

**Limited visualization results:** Only one demonstration case is provided in the supplementary material. It is recommended to present more generated results as animations to visually assess the generalization ability of the proposed method. The lack of diverse examples makes it difficult to evaluate the robustness of the model across different scenarios and motion styles.

### Questions
- Could the authors provide a comparison of MOCO's performance in text-only and audio-only scenarios with existing T2M and A2G methods?
- How does MOCO address situations in which text and audio provide contradictory motion cues for the same body part? Could the authors provide some examples to illustrate this?
- If users wish to control upper body motions using text, how flexible is MOCO's framework in accommodating such requirements? Can the authors elaborate on the potential modifications needed and any trade-offs involved? How does the framework integrate or prioritize different inputs when there is a mismatch?

### Soundness
4

### Presentation
3

### Contribution
4
