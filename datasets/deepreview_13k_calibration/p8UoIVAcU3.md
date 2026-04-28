# Diving into Self-Evolve Training for Multimodal Reasoning

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
Reasoning ability is essential for Large Multimodal Models (LMMs). 
In the absence of multimodal chain-of-thought annotated data, self-evolving training, where the model learns from its own outputs, has emerged as an effective and scalable approach for enhancing reasoning abilities. 
Despite its growing usage, a comprehensive understanding of self-evolving training, particularly in the context of multimodal reasoning, remains limited. In this paper, we delve into the intricacies of self-evolving training for multimodal reasoning, pinpointing three key factors: $\textbf{Training Method}$, $\textbf{Reward Model}$, and $\textbf{Prompt Variation}$. We systematically examine each factor and explore how various configurations affect the training's effectiveness. Our analysis leads to a set of best practices for each factor, aimed at optimizing multimodal reasoning.
Furthermore, we explore the $\textbf{Self-Evolution Dynamics}$ during training and the impact of automatic balancing mechanisms in boosting performance. After all the investigations, we present a final recipe for self-evolving training in multimodal reasoning, encapsulating these design choices into a framework we call M-STAR ($\textbf{M}$ultimodal $\textbf{S}$elf-evolving $\textbf{T}$r$\textbf{a}$ining for $\textbf{R}$easoning), built on MiniCPM-V 2.5. 
M-STAR achieves 59.5% accuracy on MathVista, surpassing the pre-evolved model by 6.9% absolutely without using additional human annotations. 
We believe this study fills a significant gap in the understanding of self-evolving training for multimodal reasoning and offers a robust framework for future research. Our policy and reward models, as well as the collected data, will be released to facilitate further investigation in multimodal reasoning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper, "Diving into Self-Evolving Training for Multimodal Reasoning," explores the enhancement of reasoning abilities in Large Multimodal Models (LMMs) through self-evolving training, a method where models iteratively improve by learning from their own outputs. The absence of multimodal chain-of-thought annotated data has led to this innovative approach. The study identifies and systematically examines three critical factors—Training Method, Reward Model, and Prompt Variation—that influence the effectiveness of training. The authors present a comprehensive analysis and establish best practices for each factor within a newly proposed framework named M-STAR (Multimodal Self-evolving Training for Reasoning), built on MiniCPM-V 2.5. This framework achieved a significant improvement in accuracy on the MathVista dataset, demonstrating its efficacy. The paper also explores the dynamics of self-evolution and introduces an automatic mechanism to balance model exploration and exploitation, further enhancing performance.

### Strengths
(1) The paper introduces an original framework, M-STAR, for self-evolving training in multimodal reasoning. This approach is particularly innovative as it leverages the model's own outputs for iterative improvement, a method relatively underexplored in the context of multimodal reasoning. Additionally, the focus on three specific components (Training Method, Reward Model, and Prompt Variation) for optimizing training presents a novel angle for investigation.

(2) The paper is well-structured and clearly written. The authors effectively communicate complex ideas, such as the dynamics of self-evolution and the implementation of an automatic balancing mechanism during training. The systematic breakdown of each key factor and the subsequent analysis make the paper accessible to readers with varying levels of expertise in the field.

### Weaknesses
(1) The motivation or evidence behind the importance of the three components: the training method, the use of the reward model, and the prompt variation is insufficiently substantiated. The authors need to provide more detailed justification or empirical evidence to support the significance of these components in the context of multimodal reasoning.

(2) The ablation experiments are solely based on a single model: MiniCPM-V-2.5, and two datasets from the Math domain. It would be beneficial to explore the effects of different model sizes (understanding the constraints of increased training time with larger models, experimenting with smaller models could be insightful) and datasets from varied domains such as code generation to generalize the findings.

(3) The settings of the ablation studies focus primarily on minor hyperparameter adjustments, leading to conclusions that align with conventional expectations. It is recommended that the authors delve deeper into algorithmic comparisons. For instance, contrasting with techniques like Supervised Fine-Tuning (SFT), Reinforcement Learning from Human Feedback (RLHF), or Differentiable Prompt Optimization (DPO), as well as exploring different training methodologies (e.g., multi-training stages) or network architecture designs (e.g., with different multimodal encoders) could provide more robust insights.

### Questions
(1) Could the authors elaborate on the specific motivations or additional evidence that underscore the criticality of the training method, reward model, and prompt variation in enhancing multimodal reasoning? A deeper understanding or empirical backing could significantly strengthen the paper's foundation.

(2) Have the authors considered expanding the ablation studies to include a broader range of model sizes, including smaller ones, despite the acknowledged increased training time with larger models? Additionally, could the use of datasets from different domains, such as code generation, provide more comprehensive insights into the model's capabilities and limitations?

(3) In terms of algorithmic comparisons and training methodologies, could the authors provide a comparative analysis with other prevalent techniques like SFT, RLHF, DPO, or different training stages and network structures? Such comparisons could offer a clearer differentiation and possibly highlight the advantages or limitations of the proposed M-STAR framework in a broader context.

(4) In the section "MONITORING THE TRAINING DYNAMICS," it is observed that nearly all training reaches its peak performance quickly (within < 2500 steps), after which the model's performance tends to decline as training progresses. Does this suggest that the base self-evolving training configuration might not be optimally set? For instance, issues such as an overly small dataset, an excessively large model, or inappropriate regularization settings could be contributing factors. How do these factors influence the conclusions drawn from the training baseline, and could this impact the accuracy of the study's outcomes?

(5) Beyond assessing the correctness of results in the Math domain, should the evaluation of the model's outputs also consider other dimensions? For instance, evaluating aspects such as the interpretability, robustness, or even the creativity of the responses could provide a more holistic view of the model's capabilities in multimodal reasoning. How do the authors envision incorporating these additional evaluation metrics into their framework?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores self-evolving training for enhancing multimodal reasoning in large multimodal models (LMMs), focusing on training without chain-of-thought annotations. The authors investigate three primary factors influencing the effectiveness of this training approach: training methods, reward model design, and prompt variation. They introduce a dynamic framework, M-STAR, built on MiniCPM-V 2.5, to optimize these factors. Key contributions include establishing best practices for each component, implementing a reward model to enhance response selection, and proposing an automatic temperature adjustment mechanism to balance exploration and exploitation during training.

### Strengths
1. Relevance: The paper addresses an important and timely problem—enhancing reasoning in large multimodal models without chain-of-thought annotations.

2. Quality: The paper demonstrates high technical quality in its systematic breakdown of training configurations, use of an adaptive exploration-exploitation strategy, and ablation studies.

3. Clarity: The paper is well-organized, with each section logically following from the last, making it easy to understand the flow from problem identification to solution.

### Weaknesses
1. Claim: The CoT warm-up phase conflicts with the paper’s definition of annotation/CoT-free self-evolving training. It is essential to clarify this reliance and provide a stronger rationale for the warm-up setting.

2. Empirical results: The paper primarily evaluates MathVista, a single multimodal reasoning benchmark focused on math-based tasks. To show broader applicability, the paper would benefit from additional benchmarks such as VQA or other scientific QA. Besides, there is only one LLM used in all experiments, so it's hard to justify whether the benefit of the method can be transferred to other architectures.

3. Theoretical analysis: Since self-evolving training shares similarities with RL, a theoretical analysis comparing these methods could clarify the unique aspects of M-STAR, such as optimality, stability, and guarantees. Also, the paper lacks a hypothesis-driven structure that ties the findings to the central research question, which appears more like a tech report rather than a research paper. 

4. Contribution: While the paper has explored different configurations exhaustively, the overall contribution is vague given its lack of theoretical grounding and limitations in the empirical study.

### Questions
1. Ablation studies showing the model’s performance with and without the CoT phase to quantify its impact on results.

2. What's the computation cost of the proposed method compared to baselines?

3. Can the best configurations explored in this study be applied to other task domains without losing their effectiveness?

### Soundness
3

### Presentation
3

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
This work focus on self-evolving training for multimodal reasoning. They mainly research on three components in self-evolving training, that is training method, reward model and prompt variation. By comparing performance of various configuration, which can be considered as a kind of grid-search, they finally determine a set of optimal design. Also, along the process, they gave some in-depth analysis and insight of different topics.

### Strengths
1. The layout of this paper is clear, the authors sperated the process into determination of three static components and stick to this layout by presenting each part in a reasonable order.
2. This work provide a comprehensive comparison of various configuration, which can serve as a reference for others working in this field. This work complement a study on self-evolving training method in multimodal reasoning area.
3. Along the process, the authors also provide some in-depth anasis in terms of diversed topic.

### Weaknesses
1. This work can be considered as a kind of grid-search process, and doesn't proposed new techniques in terms of methodology.


### Questions
1. Why is the order of focusing component be studied in the presented way? In the paper, authors first study in training method and determine a best configuration. Then they directly use this configuration for the study of reward model, finally the similar operation is performed to prompt variation. This way can be seen as a incomplete grid-search process, and the final optimal configuration could be different when they study in a different order. So it would be good for the authors to provide a reasonable explanation of this point.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper analyses the key components of self-evolving training procedure for Multimodal Large Language Models (MLLMs) with the aim of getting new insights into the reasoning capabilities of MLLMs. In particular, three fundamental aspects of self-evolving learning, i.e., training method, reward model, and prompt variation are examined in a series of experiments involving MiniCPM-V 2.5 model. Furthermore, the authors delve into the dynamics of the self-evolution process by means of monitoring four metrics, representative for the analysed process.

### Strengths
1) The paper is clearly written, easy to follow, and its underlying theme is well motivated.
2) The experiments are well-designed and formally correct.
3) The considered topic is related to MLLMs, and as such is potentially of interest to the broad subset of the ICLR community.

### Weaknesses
1) The main problem is limited experimental evaluation with respect to the number of MLLMs employed in the study. The authors present the results for one particular MLLM with not discussion about how the outcomes generalize to other models. This generalization is obviously a critical issue. 
2) Also, the authors consider only one dataset in their experiments. There are quite many datasets devoted to verifying abstract reasoning abilities of ML models, including MLLMs. Having a more diverse selection of these dataset (problem types) would be beneficial.

### Questions
1) Are the presented observations/conclusions related to MiniCPM-V 2.5 also valid for other MLLMs? If so, what is the foundation of such a claim. 
2) A similar question regarding the validity of conclusions for other types of problems / other reasoning domains.
3) In Table 1 the results for In-Domain test samples are lower than those for OOD, which is surprising. What is the reason for a better OOD than ID performance?

### Soundness
2

### Presentation
3

### Contribution
2
