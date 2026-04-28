# Personalized Visual Instruction Tuning

- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 8, 6

## Abstract
Recent advancements in multimodal large language models (MLLMs) have demonstrated significant progress; however, these models exhibit a notable limitation, which we refer to as ``face blindness". Specifically, they can engage in general conversations but fail to conduct personalized dialogues targeting at specific individuals. This deficiency hinders the application of MLLMs in personalized settings, such as tailored visual assistants on mobile devices, or domestic robots that need to recognize members of the family. In this paper, we introduce \textbf{\ModelName (\ModelNameAbbre)}, a novel data curation and training framework designed to enable MLLMs to identify target individuals within an image and engage in personalized and coherent dialogues. Our approach involves the development of a sophisticated pipeline that autonomously generates training data containing personalized conversations. This pipeline leverages the capabilities of various visual experts, image generation models, and (multi-modal) large language models. To evaluate the personalized potential of MLLMs, we present a benchmark called \Bench, which encompasses various question types with different levels of difficulty. The experiments
demonstrate a substantial personalized performance enhancement after fine-tuning with our curated dataset.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper tackles personalization issue in MLLM. Current MLLM struggle to recognize and engage with specific people in images, making them less useful for personal AI assistants. The authors propose Personalized Visual Instruction Tuning (PVIT), which lets MLLMs handle personalized conversations by introducing people as a multimodal prefix without needing extra training. They created a streamlined data pipeline to automatically generate large-scale, personalized datasets and a new benchmark, P-Bench, to measure personalization abilities.

### Strengths
1. The proposed Personalized Visual Instruction Tuning (PVIT) MLLMs conduct personalized conversation based on a general MLLM for personalized context without further tuning during test time.
2. The benchmark P-Bench of around 1500 samples could be used on relevant tasks.
3. Good qualitative and quantitative results.
4. The proposal method is easy to follow and the presentation is clear.

### Weaknesses
1. In other work like Yo'llava, the personalization including various types of subjects, while in this work, it is limited to human face, which is different to the claim in the paper such as in the introduction. The paper's claim of addressing general personalization is not fully supported by the experiments, which are exclusively focused on human faces. This narrow focus limits the generalizability of the proposed method and its applicability to diverse personalization scenarios involving non-human objects.
2. For evaluation comparisons, many actual SOTA MLLMs are not included such as GPT-4. I tried those models and found out they perform pretty good in the task. For example, for GPT4o are correct on several examples in Figure 2. The absence of comparisons with state-of-the-art closed-source models like GPT-4o makes it difficult to assess the true performance of the proposed method. The paper's claim of achieving SOTA performance is questionable without these comparisons, especially given that models like GPT-4o demonstrate strong performance on similar tasks.
3. No failure cases analysis. I do not think such method could resolve personalization MLLM perfectly, but it lacks the detailed analysis. The lack of a detailed failure case analysis prevents a thorough understanding of the limitations of the proposed method. It is crucial to identify and analyze scenarios where the method fails to provide insights into its weaknesses and potential areas for improvement.
4. Some proposed mechanisms are already commonly used in previous methods. For example, Personalized Wrapper Tokens basically denote the added information with special token. The use of personalized wrapper tokens, while effective, is not novel, as similar mechanisms are commonly employed in existing methods for incorporating additional information into language models. The paper does not adequately differentiate its approach from these existing techniques.

### Questions
1. Does it work well on non-human objects? 
2. For the MLLM used for comparisons, what are the settings? For example, some models are designed for one image input, how do you use it in multi-image input setting?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Personalized Visual Instruction Tuning (PVIT), a framework that enables MLLM to engage in personalized conversations with specific individuals. PVIT addresses the “face blindness” limitation of MLLMs by training them to recognize individuals within images and generate contextually accurate responses.

NOTE: 

Post-rebuttal: After the first rebuttal round, I have decided to raise my score from 5 to 6 since the author's responses have cleared my most concerns.

### Strengths
1. PVIT presents a novel approach to MLLM personalization by leveraging in-context learning capabilities, avoiding the need for additional training for each individual.
2. A benchmark is proposed for future research on this direction.
3. The paper is well-written and clearly explains the PVIT framework, data generation process, and experimental setup.

### Weaknesses
1. Some typos like Line 191-192 Two special tokens are mentioned, however, only one is described
2. The current implementation focuses primarily on names and faces.
3. The paper primarily focuses on individuals present in the training data. Some investigation on the zero-shot ability would help to understand this framework's ability.
4. This problem is an interesting setting, but the proposed methods is not that novel.
5. Current experiments are not that enough, more experiments as described in questions are welcome.

### Questions
1.  Line 277: More advanced knowledge, such as character, hobbies, and professions can be easily
extended and will be considered in future work. -> About How? Like character would be quite abstract to describe.
2. How about the temporal changes, like inputting a child's image while asking for the same person with quite different ages?
3. How about the twins with similar names and similar faces?
4. What happened to the situations where two different with similar faces yet different names or similar names yet different faces?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Personalized Visual Instruction Tuning (PVIT), a novel framework that enables multimodal large language models (MLLMs) to engage in personalized, coherent dialogues tailored to specific individuals within images. The PVIT framework addresses the limitations of existing MLLMs, which often fail to recognize individuals and deliver contextually accurate, personalized responses. The paper proposes a comprehensive pipeline for personalized multimodal data construction. The experiments demonstrate that models fine-tuned with PVIT show substantial improvements in personalization tasks.

### Strengths
1. PVIT’s multi-phase pipeline is designed to generate personalized training data. By integrating visual expert models, image generation tools, and large language models, the authors ensure a rich and diverse dataset that enhances the personalization capabilities of MLLMs.

2. The authors contribute P-Bench, a novel benchmark designed to evaluate personalization capabilities in MLLMs.

3. Experiments demonstrate that PVIT improves MLLMs’ accuracy in handling personalized queries across various tasks. The ablation studies further validate the impact of component designs in the pipeline, highlighting the framework’s effectiveness.

### Weaknesses
1. Reliance on Pretrained MLLMs and Potential Hallucinations: The pipeline relies heavily on pretrained multimodal large language models (MLLMs) for tasks such as image captioning and textual information generation. However, these models are known to sometimes produce hallucinated details. Without mechanisms to detect or filter out such inaccuracies, the generated data could introduce noise into the training process, leading to degraded model performance or unpredictable responses. To strengthen the pipeline's reliability, the authors should provide examples of failed cases and outline a strategy for identifying and filtering out unreasonable or erroneous data.

2. Ethical and Privacy Concerns in Human Image Sourcing: The paper does not mention the origin or sourcing of human images used for training and testing, which is critical from both ethical and privacy standpoints. Without a clear explanation of how these images were obtained and the measures taken to ensure consent and privacy, the approach may risk ethical violations. The authors should explain more about the original metadata collection.

3. The limitation section, which is required, is missing.

### Questions
1. Which version of LLaVA is finetuned as P-LLaVA?

2. What models are used in dual-level textual information extraction and fusion?

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
This paper tries to tackle the "face blindness" issue of the multimodal large language models. While, it is quite questionable whether you need the model to handle "face blindness" directly, or because it is safety and ethics issues, the model needs some mechanism to handle this issue safely. This is an important question for the motivation of this paper.

Technically, this paper presents a method to collect high-quality data for personalized conversations, then proposes Personalized
Visual Instruction Tuning (PVIT) to enable the MLLMs (LLaVA in the paper) for personalized dialogues. This paper also constructs a P-Bench for evaluation purpose. Empirical experiments on P-Bench show that the P-LLaVA can do well in the personalized setting.

### Strengths
Technical Strengths:

1. This paper proposes a way to curate the personalized instruction conversations, and also introduces a P-Bench for evaluation purpose.

2. It finetuned LLaVA in the personalized setting, and demonstrates proposing results.

### Weaknesses
1. One major issue is there might lack a section to discuss the potential Ethics issues since it involves people in the dataset and models. 

2. Methodologically, the data curation is okay, the model training part is incremental.

### Questions
1. As suggested, one potential major issue is about the ethics issues about the people topic, which needs more discuss. And also need safety evaluation for the data, benchmark and models.

2. One question is - after you adapt the LLaVA model to the personalized setting, how its (P-LLaVA) performance on the original general benchmarks.

3. And one more question is - just curious, how is the performance of GPT-4o or GPT-4v, Gemini or these frontier models on the proposed P-Bench? How they handle this people/face issue.

### Soundness
2

### Presentation
2

### Contribution
2
