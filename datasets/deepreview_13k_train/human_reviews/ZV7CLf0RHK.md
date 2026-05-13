# Fine-tuning with Reserved Majority for Noise Reduction

- Decision: Accept
- Scores: 8, 8, 8, 6

## Abstract
Parameter-efficient fine-tuning (PEFT) has revolutionized supervised fine-tuning, where LoRA and its variants gain the most popularity due to their low training costs and zero inference latency.
However, LoRA tuning not only injects knowledgeable features but also noisy hallucination during fine-tuning, which hinders the utilization of tunable parameters with the increasing LoRA rank.
In this work, we first investigate in-depth the redundancies among LoRA parameters with substantial empirical studies.
Aiming to resemble the learning capacity of high ranks from the findings, we set up a new fine-tuning framework, \textbf{P}arameter-\textbf{Re}dundant \textbf{F}ine-\textbf{T}uning (\preft), which follows the vanilla LoRA tuning process but is required to reduce redundancies before merging LoRA parameters back to pre-trained models.
Based on this framework, we propose \textbf{No}ise reduction with \textbf{R}eserved \textbf{M}ajority (\norm), which decomposes the LoRA parameters into majority parts and redundant parts with random singular value decomposition.
The major components are determined by the proposed \search method, specifically employing subspace similarity to confirm the parameter groups that share the highest similarity with the base weight.
By employing \norm, we enhance both the learning capacity and benefits from larger ranks, which consistently outperforms both LoRA and other \preft-based methods on various downstream tasks, such as general instruction tuning, math reasoning and code generation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper observes the phenomenon of hallucination caused by the large redundancy in PEFT (Parameter-Efficient Fine-Tuning) and attempts to reduce the redundancy in PEFT parameters from the perspective of rank through random singular value decomposition. It then designs a SIM-SEARCH method to ensure that the selected parameter subspace is as close as possible to the distribution of pretrained parameters, thus avoiding parameters that could damage the model's capability.

### Strengths
1. The writing of this paper is particularly good; the story is clearly told, without over-claiming its contributions, and the logic is very clear.
2. All designs in this paper are centered around a clear goal — reducing redundant PEFT parameters that have large differences from the network distribution. Although this insight did not originally come from this paper, the paper conducted meaningful preliminary experiments to validate it.
3. The experiments in this paper achieved highly competitive results across different tasks. In some tasks where LoRA underperformed, the method in this paper surpassed full-rank fine-tuning, which is not easy to achieve.

### Weaknesses
1. It would be better with more mathematical explanations and analyses. How do the authors view the source of this redundancy in PEFT?
2. Why not design a smaller or uneven rank during training rather than search for it afterward? Or, is there a way to make it more end-to-end?

### Questions
Does increasing the rank to achieve better accuracy hold significant value for your work? Why is it specifically emphasized in such an important place like Figure 1?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a comprehensive method to address the issue in LoRA, where redundant parameters in trained weights can lead to hallucinations in Large Language Models (LLMs). In pilot experiments, the authors investigated whether dropping weights could yield performance gains across different ranks and dropping strategies, providing evidence that redundant parameters induced by LoRA can indeed degrade performance. To tackle this problem, the authors propose a new fine-tuning framework called "Parameter Redundancies Fine-Tuning," which excludes redundant parameters when merging LoRA weights with the base model. They introduce an inter-shearing method named "Noise Reduction with Reserved Majority," which decomposes LoRA weight updates using Random SVD and preserves their main components based on a novel Sim-Search method. This method aims to maximize the subspace similarity between delta LoRA weights and the original weights of the model.

### Strengths
The paper provides ample illustrations to present experiment results and the method pipeline. The authors conducted extensive experiments, demonstrating that the proposed NoRM method generalizes well across various models and datasets. The ablation study further supports the plausibility of searching for the rank based on subspace similarity. Since the paper introduces an improvement for merging the widely-used LoRA method with model weights, the method can significantly benefit individuals who need to train Large Language Models (LLMs) with LoRA.

### Weaknesses
Some equations in the paper deviate from standard notation. For instance, in lines 188 to 190, what follows "such that" is typically a statement (e.g., "we choose $\Delta W$ such that $\Delta W = \ldots$"), but in the paper, it is an "argmax" result. This makes the condition for selecting $\Delta W$ unclear, as it appears to be a result rather than a constraint. Furthermore, the use of argmax without a clear objective function further complicates the interpretation. Additionally, in lines 297 to 298, there appears to be a set-builder notation, but $\tau \cdot s, (\tau + 1) \cdot s, \ldots, r$ does not seem to be a predicate over $c$. The notation suggests a sequence of values, but it's unclear how these values relate to the selection of $c$ within the set. The lack of a clear predicate makes it difficult to understand the logic behind choosing a specific value for $c$. These notational issues hinder the clarity and precision of the method's description.

### Questions
In the "weakness" section, I pointed out some non-standard mathematical notations. Are these abbreviations or special notations? An explanation of the mathematical notations would be appreciated.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a novel fine-tuning methodology named NORM, aimed at reducing noise and parameter redundancy in the fine-tuning of large language models. Central to this approach is the Parameter Redundancies Fine-Tuning framework, which optimizes the parameter efficiency of LLM fine-tuning by minimizing redundancies. NORM advances this framework by employing a technique that decomposes parameters using random singular value decomposition and selects the most significant components through a Sim-Search method, which evaluates subspace similarity with the base model weights. This method has demonstrated superior performance over traditional techniques across various downstream tasks, such as instruction tuning, mathematical reasoning, and code generation, offering a significant advancement in the field of LLM fine-tuning.

### Strengths
The paper on NORM (Noise reduction with Reserved Majority) and the PREFT framework stands out for its originality, quality, clarity, and significance. It introduces a novel methodology combining random singular value decomposition (SVD) with Sim-Search for selective parameter retention, offering a fresh perspective on fine-tuning large language models. The research is rigorously validated across various tasks, demonstrating its robustness and relevance. Structurally, the paper excels in clarity through well-organized sections and informative visuals, making complex concepts accessible and reproducible. Significantly, NORM addresses the critical challenge of efficiently tuning large models, potentially influencing future research in machine learning optimization strategies, thereby marking a noteworthy contribution to the field.

### Weaknesses
1.The paper lacks comprehensive comparisons with the latest advancements in parameter-efficient fine-tuning methods, which could more precisely establish NORM's standing in the research landscape.
2.There is insufficient analysis of the computational demands and efficiency of NORM, including comparisons of resource usage and execution time against other fine-tuning methods.
3.The paper does not discuss the potential long-term effects of applying NORM in continuous learning environments where models undergo multiple fine-tuning cycles.
4.There is no detailed exploration of how NORM's performance is influenced by the choice of hyperparameters, such as the ranks used in SVD, which could affect its robustness and ease of optimization.

### Questions
1.Can the authors provide a more detailed analysis of the computational resources required for implementing NORM compared to traditional fine-tuning methods? This could help in assessing the practicality of NORM in resource-constrained environments.
2.The method's performance may depend on the selection of specific hyperparameters, such as the rank in SVD. Could the authors discuss how sensitive NORM is to these parameters and possibly include a sensitivity analysis or guidelines for selecting optimal hyperparameters?
3.Since the paper does not discuss long-term impacts, could the authors provide insights or preliminary results on how NORM performs in continuous learning setups or multiple iterations of fine-tuning? Understanding the stability and performance over time could significantly add to the method's robustness.
4.Are there recent advancements or other fine-tuning methodologies that were considered but not included in the comparison studies? If so, what was the reason for their exclusion, and could incorporating comparisons with these methods change the perception of NORM’s effectiveness?

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
The paper introduces a parameter-efficient fine-tuning framework called Parameter-Redundant Fine-Tuning (PREFT), focusing on reducing noise in LoRA-tuned models through redundancy management. It proposes Noise Reduction with Reserved Majority (NORM), which enhances LoRA by isolating valuable components while removing redundant parts using singular value decomposition. NORM employs Sim-Search to identify the most relevant parameters for fine-tuning by analyzing their similarity with pre-trained weights, reducing hallucinations that degrade model performance.

### Strengths
1. While many concurrent papers focus on pushing the limits of parameter efficiency, this paper delves into another interesting aspect of LoRA: eliminating redundancies to prevent hallucinations.
2. Experimental results show that this method yields promising outcomes.

### Weaknesses
1. The methodology section is somewhat confusing due to the arbitrary use of notations. For example, in Line 297, does the starting value $s$ have any connection with $s_1, s_2$ mentioned in Line 155? Also, what does $\mathbf{U}_{cr}$ represent in Equation 14?
2. Although the LLM fine-tuning tasks are practical and valuable, the evaluation methods are not very standardized, and therefore the results are not entirely convincing. I recommend that the authors conduct experiments on both the GLUE and VTAB benchmarks to further validate the effectiveness of the proposed method.

3. Having conducted experiments in this area, I have found that the evaluation methods used for fine-tuned LLMs are often unconvincing （e.g., some evaluations rely on asking ChatGPT for a rating). Therefore, I strongly recommend that the authors perform experiments on established benchmarks like GLUE and VTAB to provide more robust evaluations. However, as anticipated, their method did not excel on GLUE. Additionally, the authors offer only intuitive reasons for not conducting experiments on VTAB, which raises doubts about the actual effectiveness of their proposed method. Consequently, I cannot support acceptance of this work in its current form. (**Addressed**)

### Questions
Please refer to the weakness part.

### Soundness
3

### Presentation
2

### Contribution
2
