# Motion-Agent: A Conversational Framework for Human Motion Generation with LLMs

- Decision: Accept
- Scores: 6, 8, 5, 6, 6

## Abstract
While previous approaches to 3D human motion generation have achieved notable success, they often rely on extensive training and are limited to specific tasks. To address these challenges, we introduce {\bf Motion-Agent}, an efficient conversational framework designed for general human motion generation, editing, and understanding. 
Motion-Agent employs an open-source pre-trained language model to develop a generative agent, {\bf MotionLLM}, that bridges the gap between motion and text. This is accomplished by encoding and quantizing motions into discrete tokens that align with the language model's vocabulary. With only 1--3\% of the model's parameters fine-tuned using adapters, MotionLLM delivers performance on par with diffusion models and other transformer-based methods trained from scratch. By integrating MotionLLM with GPT-4 without additional training, Motion-Agent is able to generate highly complex motion sequences through multi-turn conversations, a capability that previous models have struggled to achieve.
Motion-Agent supports a wide range of motion-language tasks, offering versatile capabilities for generating and customizing human motion through interactive conversational exchanges. Project page:~\href{https://knoxzhao.io/Motion-Agent}{https://knoxzhao.io/Motion-Agent}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors propose Motion-Agent, a conversational framework for human motion that utilizes large language models (LLMs). By incorporating MotionLLM, a generative agent fine-tuned with adapters, Motion-Agent enables bidirectional motion-text translation and supports multi-turn conversational interactions for tasks such as generation, captioning, and editing. The framework leverages the HumanML3D and KIT datasets to demonstrate its effectiveness, achieving competitive results by integrating GPT-4 for coordination without additional task-specific tuning.

### Strengths
1. The paper introduces Motion-Agent, a conversational framework that leverages pre-trained large language models (LLMs) for bidirectional human motion generation and understanding, achieving competitive results across various motion-language tasks.

2. The authors demonstrate Motion-Agent’s effectiveness through an extensive evaluation of the HumanML3D and KIT datasets, highlighting the model's competitive ability to generate and caption human motion sequences.

### Weaknesses
1. The proposed Motion-Agent framework seems to focus primarily on conversational motion generation, a capability that, according to the authors, could also be achieved using additional datasets for task-specific instruction tuning. While the authors assert that Motion-Agent is efficient, the experiments presented offer insufficient evidence to substantiate this claim. The efficiency claim is not well-supported by quantitative comparisons against other methods, particularly in terms of computational cost and training time. It remains unclear how Motion-Agent's approach to conversational motion generation is more efficient than simply fine-tuning on a task-specific dataset, especially when considering the overhead of using a large language model for conversational control.

2. The authors are encouraged to expand the discussion on the potential advantages of the proposed Motion-Agent framework. For instance, how does the model address out-of-domain motion concepts in comparison with current methods? A more thorough analysis of the model's generalization capabilities would contribute to a deeper understanding of its overall effectiveness. The current discussion lacks a detailed analysis of how the model handles motions that are significantly different from those in the training data. It is not clear how the decomposition of complex prompts into simpler motions is achieved in practice, and what limitations this approach might have.

3. The authors claim that Motion-Agent can theoretically achieve infinite motion generation. However, plots or tables illustrating changes with increasing conversation turns and motion lengths, should be provided to substantiate this claim. The claim of infinite motion generation is not supported by empirical evidence. There is no analysis of how the quality of generated motions degrades with increasing length, or how the model maintains coherence over extended sequences. The practical limitations of this approach, such as memory constraints and potential drift in motion quality, are not addressed.

4. The paper would benefit from ablation studies on the motion tokenizer, as well as comparisons with state-of-the-art RVQ-VAE models, such as MoMask which also employs RVQ-VAE to convert motion into a discrete representation. The lack of ablation studies on the motion tokenizer makes it difficult to assess the impact of this component on the overall performance of the model. Furthermore, a comparison with MoMask is necessary to understand how Motion-Agent's approach to motion representation compares with other state-of-the-art methods.

5. The paper lacks comparisons on additional MotionGPT benchmarks, such as motion composition tasks. Tuning MotionLLM with these task is something that can be easily done. The absence of comparisons on motion composition tasks limits the assessment of Motion-Agent's capabilities. It is unclear how well the model can combine different motion sequences to generate more complex actions, which is a crucial aspect of motion generation.

### Questions
1. Did the authors attempt to fine-tune all parameters of the language models within MotionLLM? If so, what were the resulting outcomes, and how did they compare to the model tuned with LoRA?

2. Is it feasible to extend the Motion-Agent framework to incorporate vision and audio modalities, given that GPT-4o is known to support multimodal inputs? What impact might this integration have on the model's performance and potential applications?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work presents a framework capable of understanding, generating, and editing 3D human motion based on dialogue. Specifically, the model includes a more advanced LLM (GPT-4) play a role of "coordinator" and a motion/language translator fine-tuned from a lightweight language model (LoRA). The experiments (including the ablation study) are thorough, and the results (including the demos) demonstrate excellent performance.

From my perspective, the reason for achieving this performance isn’t due to improvements in the language-motion model itself, but is because the coordinator achieves the high level of understanding, decomposing, and recording the tasks before language-motion model, significantly enhancing the results (or the user’s perceived experience) without change to the existing data or methods. This is very interesting and smart (though perhaps slightly tricky). I am in favor.

### Strengths
+ Very interesting idea and very reasonable design.

+ Thorough experiments and good performance.

+ Good writing.

### Weaknesses
- I am very curious about the long motion sequence generation. As illustrated by authors, "By decomposing descriptions of long motions into a series of short motions using LLMs and subsequently concatenating these short motions into longer sequences, our Motion-Agent
can theoretically achieve infinite motion generation." Though I can generally understand the meaning, the details are unclear. Is "decomposition" done by GPT4 during long motion seq generation? If so, how it is achieved? Could authors provide detailed output of GPT4 of an example (like Figure 3)? Meanwhile, during training, will GPT4 be used to decompose HumanML3D data into shorter atomic units? If so, how does such labeling achieved and how to guarantee the alignment between motion and text?

- An important work is missed in related works as one of the first works that quantize/tokenize motion into GPT: 
Bailando: 3d dance generation by actor-critic GPT with choreographic memory, CVPR 2022; 
Bailando++: 3d dance GPT with choreographic memory, TPAMI 2023

### Questions
see above

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces Motion-Agent, a novel conversational framework for 3D human motion generation, editing, and understanding that leverages large language models (LLMs). The framework employs a pre-trained language model called MotionLLM, which bridges the gap between motion and text by encoding and quantizing motions into discrete tokens aligned with the language model's vocabulary. By fine-tuning only 1–3% of the model's parameters using adapters, MotionLLM achieves performance comparable to diffusion models and other transformer-based methods trained from scratch. Integrating MotionLLM with GPT-4 without additional training, Motion-Agent enables the generation of highly complex motion sequences through multi-turn conversations, a capability previous models lacked. The framework supports a wide range of motion-language tasks, offering versatile capabilities for generating and customizing human motion through interactive conversational exchanges. Experiments demonstrate that Motion-Agent effectively handles intricate, multi-turn interactions and achieves strong results in both motion generation and captioning tasks.

### Strengths
Originality: The paper presents an innovative approach by integrating large language models into 3D human motion generation, a relatively unexplored area. The conversational framework allowing multi-turn interactions for motion generation and editing is particularly novel.
Quality: The proposed method effectively leverages pre-trained LLMs with minimal fine-tuning, demonstrating competitive performance with significantly reduced computational resources compared to models trained from scratch.
Clarity: The methodology is well-articulated, with clear explanations of the motion tokenizer/detokenizer and how MotionLLM integrates with GPT-4. The inclusion of qualitative examples and ablation studies aids in understanding the framework's capabilities.
Significance: The ability to generate complex, customizable human motions through conversational interactions has substantial implications for animation, virtual reality, and human-computer interaction. The framework's versatility enhances its practical relevance in various applications.

### Weaknesses
Evaluation Metrics: The paper primarily presents qualitative results and some standard metrics but lacks comprehensive quantitative comparisons with state-of-the-art models on standardized benchmarks, making it challenging to fully assess performance improvements. Specifically, the paper does not provide detailed comparisons on established datasets for motion generation or captioning tasks, such as Human3.6M or AMASS, which would allow for a more rigorous evaluation against existing methods. The absence of these comparisons makes it difficult to ascertain the true advancement offered by Motion-Agent.
Limited Ablation Studies: While an ablation study is included, more extensive experiments isolating the contributions of each component (e.g., the impact of different LLMs, the motion tokenizer) would strengthen the evaluation. For example, the paper could explore the effect of varying the size of the motion vocabulary or the impact of different quantization methods on the quality of generated motions. Furthermore, an analysis of the performance with different adapter configurations would provide a more complete understanding of the model's behavior.
Dependence on Proprietary Models: Utilizing GPT-4 as the conversational LLM may limit reproducibility and accessibility, as GPT-4 is not openly available to all researchers. This reliance on a closed-source model hinders the ability of the research community to validate and build upon the proposed framework. The paper should explore the feasibility of using open-source alternatives and provide a detailed comparison of their performance.
Scalability and Efficiency: The paper does not thoroughly discuss the computational efficiency and real-time performance of the framework, which is critical for interactive applications. Details on the inference time, memory usage, and the hardware requirements for running Motion-Agent are missing. This lack of information makes it difficult to assess the practical applicability of the framework in real-time scenarios.

### Questions
Can the authors provide more quantitative evaluations comparing Motion-Agent with state-of-the-art models on standard benchmarks?
How does the choice of the pre-trained LLM (e.g., GPT-4 vs. open-source models) impact the performance of the framework? Have experiments been conducted with other LLMs?
What are the computational requirements (e.g., inference time, memory usage) of Motion-Agent, especially for real-time interactive applications?
How does the framework handle motions involving interactions with the environment or multiple agents (e.g., multi-human interactions)?
Are there limitations regarding the diversity or realism of the generated motions when handling highly complex or extended sequences?

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
5

### Summary
Motion Agent introduces a conversational framework for generating, editing, and reasoning about human motion in multiple steps. This framework is built on a MotionLLM fine-tuned with LoRA. With a motion tokenizer-detokenizer and a text detokenizer, Motion Agent can create new motions and generate text that explains or describes the motions in natural language. Fine-tuning the large LLM allows Motion Agent to generalize better than current state-of-the-art methods, produce longer motion sequences, and handle language-guided edits.

### Strengths
1) The paper is well-written and supported by experiments, with a good presentation of ablation studies and applications. The supplementary material includes videos for temporal generations, which helps in reviewing the work better.

2) This research is timely, as using LoRA fine-tuning on LLMs for multimodal human motion generation allows for models that don’t rely on task-specific data. 

3) Multi-turn editing and the ability to generate long motion sequences are valuable directions for the field.

### Weaknesses
1) Lines 280-282: Multiple adapters are mentioned to work together, and fig 2 shows two LoRA adapters after fine-tuning. It looks like they’re applied to the base LLM in separate branches. How does MotionLLM.generate or MotionLLM.caption work—are they called every time during inference, or just when needed? This information would help clarify the pipeline.

2) Line 323 states that there is no ground truth for these tasks, but the videos show apparent issues like body interpenetration, lack of physical constraints (e.g., floor contact), and body deformation. There are also no quantitative metrics for multi-turn edited generations. Even though the motion quality seems better than the current SOTA, these limitations stand out. One way to address this would be to explain why these interpenetrations occur, especially since the motion tokenizer/detokenizer was trained on motion reconstruction losses, which should ideally prevent this. Another approach could be to generate multi-turn prompts based on test set motion sequences and provide metrics like FID, where the test sample could act as a pseudo ground truth.

3) The examples in fig 3 show different genders/body types across three instances. How does Motion Agent choose each identity or gender? Are all identities compatible in terms of body kinematics, or could retargeting cause issues if aiming for consistent identity? This needs more explanation.

4) Figure 5 shows in-betweening, but there’s no quantitative metric to evaluate it. Using a metric like NPSS (e.g., https://arxiv.org/pdf/1809.03036, https://arxiv.org/pdf/2102.04942) could provide useful information on the in-between motion quality.

5) Tab 2 - Generation Task: FID scores are lower than the state-of-the-art. As noted in Lines 416-418, could the motion length be constrained to match other methods to provide a clearer comparison of the FID scores?

### Questions
1) What are the benefits of using VQVAE over other models like diffusion/VAE?

2) Which body joint representations were used for training?

3) The extended motion sequences keep the original motion unchanged. This is visible in all the provided videos. For example, with prompt p1, motion m1 is generated; when p2 is added, it generates a new motion m2, so the combined motion is m1 + m2. How is m1 preserved—does the new generation only respond to the new prompt?

4) Lines 191-192 mention that the motion detokenizer is important for smoothing transitions between different motion sequences. Are the motions generated by MotionLLM concatenated and sent to the motion detokenizer after each prompt?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces Motion-Agent, an efficient framework for general human motion generation, and it also develops a generative agent, Motion LLM, which bridges the gap between motion and text. Experiments show that with few-shot fine-tuning, MotionLLM can achieve state-of-the-art performance. Motion-Agent can generate complex motion sequences.

### Strengths
1. This paper presents a framework to bridge text and motion. This part is novel in the opinion of the reviewer. The proposed motion tokenization approach and Motion-language Agent have some level of novelty.

2. Table 1 summarizes the advantages of this work against several recent competitors. It seems that this work supports multi-turn editing, reasoning, and composition. Also, Motion LLM can generate longer motion, which is superior to previous works.

3. Motions in this work and its supplementary (including video results) look cool. This indicates that the proposed model can generate complex motions.

### Weaknesses
1. The website in the supplementary cannot function well (videos cannot be rendered). The reviewer suggests authors publish their websites on anonymous hosts (such as Google Pages). Moreover, it's better to show case more diverse prompts.

2. More ablation studies are welcomed. For example, different types of tokenizers, detailed comparison between LLaMa and Gemma, etc.

### Questions
1. What's the rendering engine to generate those visualizations?

2. Can this framework benefit down stream tasks such as robotics and policy learning?

### Soundness
3

### Presentation
3

### Contribution
3
