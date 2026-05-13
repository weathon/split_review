# Divergence-enhanced Knowledge-guided Context Optimization for Visual-Language Prompt Tuning

- Decision: Accept
- Scores: 6, 6, 6, 5

## Abstract
Prompt tuning vision-language models like CLIP has shown great potential in learning transferable representations for various downstream tasks. The main issue is how to mitigate the over-fitting problem on downstream tasks with limited training samples. While knowledge-guided context optimization (Yao et al.,2023; 2024) has been proposed by constructing consistency constraints to handle catastrophic forgetting in the pre-trained backbone, it also introduces a potential bias toward pre-training. This paper proposes a novel and simple Divergence-enhanced Knowledge-guided Prompt Tuning (DeKg) method to address this issue. The key insight is that the bias toward pre-training can be alleviated by encouraging the independence between the learnable and the crafted prompt. Specifically, DeKg employs the Hilbert-Schmidt Independence Criterion (HSIC) to regularize the learnable prompts, thereby reducing their dependence on prior general knowledge, and enabling divergence induced by target knowledge. Comprehensive evaluations demonstrate that DeKg serves as a plug-and-play module can seamlessly integrate with existing knowledge-guided methods and achieves superior performance in three challenging benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a simple yet effective knowledge-based prompt tuning method that leverages the Hilbert-Schmidt Independence Criterion (HSIC) to regularize learnable prompts. By reducing the reliance on prior general knowledge, this approach enables the prompts to better align with task-specific knowledge. The method is versatile and can be easily integrated into other frameworks. When applied to the TCP method, it demonstrates superior performance across most datasets.

### Strengths
1. This paper is well-organized and easy to follow. Figure 2 effectively illustrates the main idea by clarifying the roles of each loss function: the \( L_{CE} \) loss enforces alignment between text and vision embeddings, the \( L_{kg} \) loss encourages the learnable prompts to align closely with the CLIP textual embeddings, and the core \( L_{HSIC} \) loss ensures independence within the learnable prompt embeddings.

2. The experiments are comprehensive, covering base-to-new generalization, cross-dataset generalization, and few-shot classification. The proposed DeKgTCP method achieves superior results across most datasets.

### Weaknesses
1. Why was the proposed method applied to KgCoOp and TCP rather than other state-of-the-art methods, such as PromptSRC, which performs even better than KgCoOp? Is it more challenging to integrate with PromptSRC, or are the results less effective? Providing additional clarification on this choice would enhance the paper.

2. Figure 4 provides an insight into how the proposed method balances dependence and independence; however, the paper lacks further analysis on this. Expanding on this point would strengthen the reader’s understanding of the method's underlying mechanics.

### Questions
see weakness

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
This paper tackles the inherent issue of knowledge-guided context optimization, which overly biases general knowledge in pre-training. It proposes a novel HISC-based regularization method, DeKg, for encouraging independence between the learnable and the crafted prompts. Extensive experiments demonstrate the superiority of the proposed method in three challenging benchmarks:

### Strengths
+Using the Hilbert-Schmidt Independence Criterion (HSIC) is an interesting topic for encouraging independence between learnable and crafted prompts, which can boost performance in the seen classes.

+Evaluation shows the effectiveness of the proposed method.

+The proposed DeKg integrates seamlessly with existing knowledge-guided methods.

### Weaknesses
-As shown in Figure 1, the proposed DeKg obtains a higher performance than the performance of CoOp for base classes and the zero-shot CLIP for new classes. However, the Hilbert-Schmidt Independence Criterion (HSIC) contained in DeKg is a constraint between the learnable and crafted prompts without injecting additional information. Why can the proposed DeKg obtain a better performance?

-L221: The proposed L_{kd} involves two terms: intra-class relations and inter-class relations. Moreover, the author claims that  penalizing
L_{kd} encourages both intra-class and inter-class independence. Furthermore, the intra-class consistency is formulated between w_i and w_{i}^{clip}, which is the same as the L_{kg}. In other words, the proposed HSIC has contained the knowledge consistency L_{kg}. Therefore, the final objective of Eq.(5) should not contain L_{kg} because L_{kd} has been constrained by the intra-class consistency. However, the results in Table 4 are inconclusive with the above conclusion. Even more unfortunate, L_{kd} performs worse than L_{kg}. Why?

-It is recommended to provide a code.

-Since the proposed HSIC is model-independent, it is suggested that the module's generalization and plug-and-play be verified using more CoOp-based methods.

### Questions
Please see #Weaknesses

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel method called Divergence-enhanced Knowledge-guided Prompt Tuning (DeKg), which employs Hilbert-Schmidt Independence Criterion (HSIC) regularization to maintain a degree of independence between the learnable prompts and pre-trained knowledge, addressing the bias problem caused by over-reliance on pre-trained knowledge. Built upon knowledge-guided context optimization, DeKg introduces an independence constraint, enabling learnable prompts to retain consistency with general knowledge while capturing task-specific features, thus achieving a better balance between base and novel classes.

### Strengths
1. The paper addresses the inherent bias issue in knowledge-guided context optimization by introducing a novel Hilbert-Schmidt Independence Criterion (HSIC)-based regularization that encourages independence between learnable and crafted prompts. 
2. DeKg integrates with existing methods, enhancing class-specific prompt distinction without increasing model complexity.

### Weaknesses
1. The motivation of using HSIC as the constrain is not clearly elaborated. Further analysis of your motivation will be insightful. Specifically, while the paper mentions HSIC's properties like non-parametric nature and computational ease, it lacks a deeper explanation of why HSIC is the *right* choice for measuring independence between learnable and crafted prompts in this particular context. The connection between HSIC's mathematical properties and the specific problem of bias in knowledge-guided context optimization needs to be more explicitly established. For instance, how does HSIC capture the nuances of semantic independence in the embedding space, and what are the limitations of using HSIC in this scenario compared to other independence measures?
2. One of the proposed loss: $L_{kg}$ is already applied in existing methods, such as KgCoOp and PromptSRC, which weakens the novelty of overall method. While the paper acknowledges that $L_{kg}$ is not novel, it does not sufficiently address the concern that the overall method's contribution is diminished by relying on an existing component. The paper should provide a more detailed justification for why the specific combination of $L_{kg}$ with the proposed $L_{kd}$ is a significant contribution, rather than a simple aggregation of existing techniques. A more thorough analysis of how the interaction between these two losses leads to emergent behavior or performance gains beyond what each loss can achieve individually is needed.

### Questions
1. As mentioned in weakness1, more analysis of your motivation concerning why you choose Hilbert-Schmidt Independence Criterion would be insightful.
2. The experiment of domain generalization seems to be missed in your paper, which is conducted by most prompt tuning method. Could you provide Dekg’s performance on this setting.
3. In Tabel 4, it is obvious that the $L_{kg}$ works well in novel, while $L_{kd}$ performs well in base. Dose that mean these two losses are strongly coupled and your proposed $L_{kd}$ is not recommended to use independently? More analysis on above question would be insightful.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes to adapt HSIC as an extra regularization term, which achieves a better trade-off between the performance on base and new classes. The experiments show the effectiveness of this regularization on varies experiment settings. The paper is well written and easy to understand.

### Strengths
1. I think this paper has a reasonable motivation to maximize the independence between learnable prompt and manual prompt. 
2. This paper has a very extensive experiment analysis on varies clip model adaptation task and show good results.

### Weaknesses
1. More analysis is needed to discuss why HISC is chosen as the metrics to measure the prompt independence. Other methods like information bottleneck can do that too. 
2. L_kd and L_kg seems to be a pair of totally contradictive losses. I wonder if this will cause the model to be difficult to converge. It would be better to provide more analysis on how the loss weight of these two losses affect the model convergence. 
3. More performance comparison and analysis on other state-of-the-art prompt tuning method like:
Yubin, et.al, Learning Hierarchical Prompt with Structured Linguistic Knowledge for Vision-Language Models

### Questions
Please refer to the concern in the Weakness section.

### Soundness
3

### Presentation
2

### Contribution
1
