# Ring-A-Bell! How Reliable are Concept Removal Methods For Diffusion Models?

- Decision: Accept
- Scores: 5, 5, 8, 6

## Abstract
Diffusion models for text-to-image (T2I) synthesis, such as Stable Diffusion (SD), have recently demonstrated exceptional capabilities for generating high-quality content. However, this progress has raised several concerns of potential misuse, particularly in creating copyrighted, prohibited, and restricted content, or NSFW (not safe for work) images. While efforts have been made to mitigate such problems, either by implementing a safety filter at the evaluation stage or by fine-tuning models to eliminate undesirable concepts or styles, the effectiveness of these safety measures in dealing with a wide range of prompts remains largely unexplored. In this work, we aim to investigate these safety mechanisms by proposing one novel concept retrieval algorithm for evaluation. We introduce Ring-A-Bell, a model-agnostic red-teaming tool for T2I diffusion models, where the whole evaluation can be prepared in advance without prior knowledge of the target model.
Specifically, Ring-A-Bell first performs concept extraction to obtain holistic representations for sensitive and inappropriate concepts. Subsequently, by leveraging the extracted concept, Ring-A-Bell automatically identifies problematic prompts for diffusion models with the corresponding generation of inappropriate content, allowing the user to assess the reliability of deployed safety mechanisms. Finally, we empirically validate our method by testing online services such as Midjourney and various methods of concept removal. Our results show that Ring-A-Bell, by manipulating safe prompting benchmarks, can transform prompts that were originally regarded as safe to evade existing safety mechanisms, thus revealing the defects of the so-called safety mechanisms which could practically lead to the generation of harmful contents. In essence, Ring-A-Bell could serve as a red-teaming tool to understand the limitations of deployed safety mechanisms and to explore the risk under plausible attacks.

\textcolor{red}{CAUTION: This paper includes model-generated content that may contain offensive material.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a model-agnostic red-teaming tool, Ring-A-Bell, for the evaluation of text-to-image (T2I) diffusion models’ safety mechanisms. In the first stage, this concept retrieval algorithm would perform concept extraction by learning the difference between the embeddings of prompts with/ without the target concept (e.g., violence). With the extracted concept, the algorithm utilises genetic algorithms to produce problematic prompts to test the reliability of online T2I diffusion models.

### Strengths
1.	The main idea of the algorithms is clearly demonstrated with figures and examples. The motivation of the paper is clearly explained by analyzing the drawbacks of the current model-specific attack algorithms.

2.	Extensive experiments are well-designed to show the efficiency of Ring-A-Bell in generating problematic prompts in the field of nudity and violence. The evaluation is reasonable with the NudeNet detector. The results are clearly shown with quantitative tables and well-processed images to demonstrate the ability of Ring-A-Bell as a red-teaming tool.

### Weaknesses
1. The related work should include the introduction of the concept removal methods, such as the Safe Latent Diffusion mentioned in the paper.

2. In the concept extraction stage, the selection/ generation of the prompt pairs, which are semantically similar but different from the target concept, is not clearly specified. Producing high-quality prompt pairs requires extensive specialized knowledge. This can affect the effectiveness of the algorithm and increase the difficulty of reproduction.

3. The generation of p ̃_cont is simply by a linear combination of the embedding of P and extracted empirical representation c ̂, which needs further justification. The definition of ‘target prompt P’ is not specified.

4. The ablation study is not properly implemented. For example, it might be better to demonstrate the performance of the algorithm with and without discrete optimization.

5. The algorithm strongly emphasizes that the text encoder is the CLIP model. It might be better to test on other text encoders.

### Questions
see the above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper investigates the effectiveness of safety mechanisms for text-to-image (T2I) diffusion models. It proposes a model-agnostic evaluation tool called Ring-A-Bell, which can assess the reliability of deployed safety mechanisms without prior knowledge of the target model. The tool performs concept extraction to identify problematic prompts and generates inappropriate content to evaluate the safety measures. The paper empirically validates the method by testing online services and various concept removal methods.

### Strengths
+ significance: this paper reveals the importance of adversarial evaluation of the current concept removal works. Moreover, it performs its attack in a practical black-box way, which expands its evaluation scale to commercial APIs. How to evaluate the black-box commercial APIs is of great importance since they are powerful and more easily accessible by common people. 

+ quality: this paper takes a comprehensive inspect into the safety robustness of commercial APIs and also state-of-the-art concept removal methods, which demonstrates the efficacy of their method.

### Weaknesses
- their attack is easy to be filtered or removed by advanced NLP techniques such as large language model, since they perform token-level optimization on the prompt and the output is usually random combinations of tokens. large language model can purify the prompt by removing the semantically unclear part of the prompt.

- the token level optimization is uninterpretable and cannot provide insights into how to defend against such attacks.

- the ablation study of interference among modification, prompt dilution, and Ring-A-Bell: in Figure 2 and 3, the shown prompt contains the three types of texts. 1) is the whole prompt generated by Ring-A-Bell, or you combine the three types of attacks together for final output? how to discriminate the type of texts such as modification, prompt dilution, and Ring-A-Bell? 2) which type of text is essential to evade the safety filter of diffusion models or defeat the concept removal methods?

- the ESD config is missing in Table 2 since it has multiple variants, whose concept removal effect is different from each other.

- why K=16 is the final config? is there experiment result about smaller K?

### Questions
- the ablation study of interference among modification, prompt dilution, and Ring-A-Bell: in Figure 2 and 3, the shown prompt contains the three types of texts. 1) is the whole prompt generated by Ring-A-Bell, or you combine the three types of attacks together for final output? how to discriminate the type of texts such as modification, prompt dilution, and Ring-A-Bell? 2) which type of text is essential to evade the safety filter of diffusion models or defeat the concept removal methods? 

- the ESD config is missing in Table 2 since it has multiple variants, whose concept removal effect is different from each other.

- why K=16 is the final config? is there experiment result about smaller K?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper investigates the safety of text-to-image models. The paper proposes a model-agnostic attack to evade safety mechanisms and generate sensitive and inappropriate images. The proposed work is evaluated on online services to explore their safety risks.

### Strengths
1. The paper investigates red-teaming text-to-image models, which is a critical topic for generative AI safety.
2. The proposed method is validated on four T2I online services.
3. The paper is well-written and easy to follow.

### Weaknesses
1. The model-agnostic design of the proposed framework is not convincing. The entire design is based on an offline CLIP model and is irrelevant to the online services. This design implicitly assumes that the framework that applies to the offline CLIP model can be transferable and effective for online services. What if the online services use a more robust text encoder? In addition, one of the contributions, claimed by the paper, is that Ring-A-Bell is “based solely on either the CLIP model or general text encoders.” However, in the evaluation, only the CLIP model is evaluated. It would be great to see if the proposed work can be extended to other and more recent text encoders.
2. The paper only compares the proposed framework with QF-Attack, which is insufficient. Many recent works are encouraged to be investigated [1-4]. In addition, although P4D is designed for offline attacks, it would be great to consider P4D as a baseline to compare the performance gap between online and offline attacks.
3. The paper aims to evade the safety mechanism of online diffusion models. However, the paper only considers concept removal defenses. For an online service, an easy and effective way is to develop a detector to identify inappropriate images. For example, the service provider could build a detector (e.g., NudeNet detector used in the evaluation) to detect nudity in the images. The proposed framework that mainly focuses on the text domain may not be effective.

### Questions
Please clarify the model-agnostic design and explain why it is effective for online services.


The rebuttal has addressed most of my concerns.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposed Ring-A-Bell, a model-agnostic red-teaming tool for T2I diffusion models, which serves as a prompt-based concept testing framework that generates problematic prompts to red-team T2I diffusion models with safety mechanisms.

### Strengths
Overall this paper proposed a practical and intersting offline method in generating problematic prompts for 'safe models'. The experiments are very convincing and concrete.

### Weaknesses
There are a bunch of notation issues. I list some of them below:
1. What is $\rho$ in (2)? I cannot find it in the main paper.
2. What is the training parameter of (2)? Is it $\widetilde c$?
3. Are there brackets in (3)
4. Should $\tilde{\mathbf{P}}_{cont}$ be a function of $c$ or $\hat c$?

Question about experiments:
1. How to tell whether the percentage of nudity is greater than 50%? The output propobility? Please be rigorous.

### Questions
There are a bunch of notation issues. I list some of them below:
1. What is $\rho$ in (2)? I cannot find it in the main paper.
2. What is the training parameter of (2)? Is it $\widetilde c$?
3. Are there brackets in (3)
4. Should $\tilde{\mathbf{P}}_{cont}$ be a function of $c$ or $\hat c$?

Question about experiments:
1. How to tell whether the percentage of nudity is greater than 50%? The output propobility? Please be rigorous.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
