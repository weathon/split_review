# Score Forgetting Distillation: A Swift, Data-Free Method for Machine Unlearning in Diffusion Models

- Decision: Accept
- Scores: 8, 8, 5, 5

## Abstract
The machine learning community is increasingly recognizing the importance of fostering trust and safety in modern generative AI (GenAI) models. We posit machine unlearning (MU) as a crucial foundation for developing safe, secure, and trustworthy GenAI models. Traditional MU methods often rely on stringent assumptions and require access to real data. This paper introduces Score Forgetting Distillation (SFD), an innovative MU approach that promotes the forgetting of undesirable information in diffusion models by aligning the conditional scores of ``unsafe'' classes or concepts with those of ``safe'' ones. To eliminate the need for real data, our SFD framework incorporates a score-based MU loss into the score distillation objective of a pretrained diffusion model. This serves as a regularization term that preserves desired generation capabilities while enabling the production of synthetic data through a one-step generator. Our experiments on pretrained label-conditional and text-to-image diffusion models demonstrate that our method effectively accelerates the forgetting of target classes or concepts during generation, while preserving the quality of other classes or concepts. This unlearned and distilled diffusion not only pioneers a novel concept in MU but also accelerates the generation speed of diffusion models. Our experiments and studies on a range of diffusion models and datasets confirm that our approach is generalizable, effective, and advantageous for MU in diffusion models.

{\color{red} \textbf{Warning:} This paper contains sexually explicit imagery, discussions of pornography, racially-charged terminology, and other content that some readers may find disturbing, distressing, and/or offensive.}

\vspace{-1em}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces Score Forgetting Distillation (SFD), a novel, data-free method for machine unlearning in diffusion models. SFD enables the efficient removal of specific classes or concepts from pretrained diffusion models without requiring access to real training data. It works by aligning the conditional scores of the undesired ("unsafe") content with those of desired ("safe") content within the model's score function.

### Strengths
Several strengths:

1. Novelty of the Approach: The paper introduces a novel method for machine unlearning in diffusion models using score distillation. To the best of current knowledge, this is the first work that approaches class and concept unlearning from the score distillation perspective. This innovative method opens up new avenues for efficient and effective unlearning in generative models.

2. Clarity of Presentation: The authors present their ideas and methods clearly, which helps readers understand both the existing literature and the proposed approach. The paper effectively explains complex concepts related to diffusion models and machine unlearning, making it accessible to a broader audience.

3. Extensive Experiments: The paper includes comprehensive experiments across various unlearning scenarios. These experiments not only demonstrate the effectiveness of the proposed method but also provide valuable insights into its applicability in different contexts. The thorough empirical evaluation strengthens the credibility of the findings

### Weaknesses
Weakness:

Running Time Concerns: There is a concern regarding the overall runtime of the unlearning process proposed in the paper. While the method aims to accelerate forgetting and improve generation speed, it is important to evaluate the computational efficiency and practicality of the unlearning procedure. Without empirical data on the time required for the process, it's unclear whether the method is suitable for large-scale or real-time applications.

Lack of Robustness Evaluation Against Adversarial Prompts: Previous studies [1,2] have shown that adversarial text prompts can circumvent unlearning mechanisms in text-to-image (T2I) models. The paper lacks an evaluation of how robust the proposed method is against such adversarial inputs. Assessing the method's ability to prevent the generation of unlearned content when faced with intentionally manipulative prompts is crucial. Providing robustness evaluations or proposing solutions to address potential vulnerabilities would strengthen the validity and reliability of the unlearning approach.

### Questions
Is it possible to provide the running time for the whole unlearning procedure compared with others?

Is it possible to provide some robustness evaluation on T2I unlearned models?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces Score Forgetting Distillation (SFD), a method that enables diffusion models to unlearn unsafe content by aligning it with safe content, without needing real data. SFD improves generation speed and maintains quality for other concepts, supporting safer generative AI.

### Strengths
1. Covers multiple diffusion model unlearning tasks, such as object classes, celebrity identities, and nudity.
2. Has a strong theoretical foundation.

### Weaknesses
1. There is no related work section to highlight the differences among existing works.
2. Evaluation under adversarial prompt attacks, such as UnlearnDiffAtk [1], is missing, even though it is a common evaluation tool for unlearned diffusion models.
3. A comparison of generation times is missing, which is essential to demonstrate the efficiency of the proposed one-step generator.
4. The baselines used in the experiments are weak, and stronger state-of-the-art methods, such as AdvUnlearn [2], should be considered.

### Questions
check Weakness section

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
5

### Summary
The paper introduces Score Forgetting Distillation (SFD), a data-free method for machine unlearning (MU) in diffusion models. The goal is to efficiently erase specific classes or concepts (e.g., "unsafe" or undesirable content) from pre-trained diffusion models without accessing the original training data. SFD achieves this by aligning the conditional scores of the target classes or concepts to forget with those of safe or desired ones, effectively overriding the unwanted information. The method incorporates a score-based MU loss into the score distillation process, which not only enables data-free unlearning but also accelerates the generation speed of diffusion models by distilling them into one-step generators. The authors validate the effectiveness of SFD through experiments on class-conditional diffusion models (e.g., CIFAR-10 and STL-10) and text-to-image models like Stable Diffusion, demonstrating that their approach can effectively forget specific classes or concepts while preserving the quality and diversity of the remaining content.

### Strengths
1. The paper presents a novel approach to machine unlearning in diffusion models by introducing Score Forgetting Distillation. Unlike previous methods that require access to real data or rely on stringent assumptions, SFD operates in a data-free manner and integrates unlearning directly into the distillation process. This creative combination of score distillation and machine unlearning extends to both class-conditional and text-to-image diffusion models.

2. The proposed method is thoroughly evaluated on multiple datasets and models, including CIFAR-10, STL-10, and Stable Diffusion. The experiments include both quantitative metrics (e.g., Unlearning Accuracy, FID, IS, Precision, Recall) and qualitative results (e.g., visual examples of forgetting effects). Ablation studies analyze the impact of different components of the method, enhancing the robustness of the evaluation.

3. The paper is well-written and organized, with clear explanations of the problem, methodology, and experimental results. Figures and tables are informative and effectively support the text. The inclusion of algorithm pseudo-code and detailed descriptions aids in understanding the implementation details.

4. Machine unlearning in diffusion models is crucial for enhancing the safety and trustworthiness of generative AI. By providing a data-free method that accelerates both unlearning and sampling, the paper contributes to making diffusion models more practical and secure for real-world applications.

### Weaknesses
1. While the paper introduces a novel method, the contributions may be perceived as incremental within the context of existing work on score distillation [1] and machine unlearning [2]. The proposed method builds upon recent advancements in data-free diffusion distillation, with the primary novelty being the integration of machine unlearning into this framework. Providing additional emphasis on the theoretical foundations or discussing broader implications could strengthen the overall contribution.

2. Although SFD reduces the number of sampling steps, this benefit appears to be a general characteristic of score distillation or matching methods. The authors do not sufficiently explain the specific advantages of integrating unlearning into score distillation. A more intuitive and necessary ablation study would involve comparing the results with the following baselines: (1) comparing SFD against existing unlearning methods applied to one-step diffusion models (e.g., SiD/DMD distilled models [1,3,4] or pre-trained consistency models [5,6]); (2) applying score distillation or matching methods to models that have already undergone unlearning. Additionally, the authors could compare their method with baseline unlearned models using fewer sampling steps (e.g., 50-step DDIM [7] or 10-step DPM-Solver++ [8,9]). Intuitively, reducing the number of sampling steps should primarily affect image quality rather than unlearning accuracy.

3. Machine unlearning generally focuses on methods for rapid modification of existing models. An essential aspect of evaluations is the algorithm's efficiency [10]. If the training time of the proposed algorithm is excessively long, one might question why not simply filter out all harmful data and retrain the model from scratch. However, the paper does not provide an analysis of the algorithm's runtime or computational efficiency. If this is a misunderstanding on my part, clarification would be appreciated.

4. A major application of machine unlearning is its direct deployment in existing products for hot updates to production models, which requires the algorithm to handle sequential unlearning requests effectively [11]. However, the SFD method presented by the authors has only been applied to models that have not undergone prior distillation. Does SFD perform equally well when applied to distilled models? For example, does it work effectively when sequentially forgetting classes such as airplane, bird, car, cat, and deer from the STL-10 dataset? In such scenarios, does it perform better than other unlearning methods?

5. There appear to be inconsistencies in the experimental results. For instance, in Table 1, the authors compare their method with ESD, SA, and SalUn, whereas in Tables 2 and 3, some of these baselines are missing. Could the authors briefly explain the reason for excluding them?

### Questions
See weaknesses.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents Score Forgetting Distillation (SFD), a novel approach to machine unlearning (MU) in diffusion models (DM) that aims to "forget" undesirable information by aligning the conditional scores of "unsafe" classes with those of "safe" ones. Departing from traditional MU objectives for diffusion models, the authors introduce a score-based MU loss built upon the score distillation objective proposed in [1], which facilitates one-step synthetic data generation and obviates the need for real data. Through empirical evaluations on pretrained label-conditional and text-to-image diffusion models, the authors demonstrate the efficacy of their method in achieving targeted unlearning without compromising model quality.

[1] Score Identity Distillation: Exponentially Fast Distillation of Pretrained Diffusion Models for One-Step Generation

### Strengths
The exploration of machine unlearning (MU) using distilled diffusion models (DMs) is a novel approach, particularly given that distilled DMs enable significantly more efficient content generation compared to traditional DMs.

### Weaknesses
1. The presentation of this paper could be improved. The authors have omitted a dedicated related works section, instead integrating substantial content from prior work within the methodology section. This blending of information makes it challenging to clearly identify the paper’s unique contributions.

2. The empirical study is not as comprehensive as recognized work on the same topic. See questions.

### Questions
1. Regarding the first weakness, could the authors provide justification for selecting Score Identity Distillation (SiD) over Diff-Instruct and DMD in this work? Alternatively, could Diff-Instruct and DMD be integrated into the SFD framework? I encourage the authors to include related discussions or experimental results in the revised paper to address these points.

2. How were the baseline results obtained? If they were sourced from original papers, could the authors specify the exact source for these baselines? It is unclear if the setting in Table 1 aligns directly with any cases from previous work such as [1]. Please clarify, and, if applicable, identify comparable results in [1] that correspond directly with Table 1.

3. Style forgetting and random data forgetting are standard choices for MU evaluation. Why were these not considered in this study?

4. Run-time efficiency (RTE), defined as the computation time for applying an MU method, is not reported here. Additionally, the computational cost associated with pretraining a score function is not addressed. I would appreciate relevant results or discussions on these aspects.

5. Another approach to achieving similar efficiency for an unlearned model could involve performing forgetting first, followed by distillation. Could the authors comment on this alternative?

[1] SalUn: Empowering Machine Unlearning via Gradient-based Weight Saliency in Both Image Classification and Generation

### Soundness
3

### Presentation
2

### Contribution
2
