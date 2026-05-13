# Enhancing Deep Symbolic Regression via Reasoning Equivalent Expressions

- Decision: Reject
- Scores: 5, 3, 5, 3, 3

## Abstract
Symbolic regression seeks to uncover physical knowledge from experimental data. Recently a line of work on deep reinforcement learning (DRL) formulated the search for optimal expressions as a sequential decision-making problem. However, training these models is challenging due to the inherent instability of the policy gradient estimator.
We observe that many numerically equivalent yet symbolically distinct expressions exist, such as $\log(x_1^2 x_2^3)$ and $2\log(x_1) + 3\log(x_2)$. 
Building on this, we propose Deep Symbolic Regression via Reasoning Equivalent eXpressions (DSR-Rex). The high-level idea is to enhance policy gradient estimation by leveraging both expressions sampled from the DRL and their numerically identical counterparts generated via an expression reasoning module. 
Our DSR-Rex (1) embeds mathematical laws and equalities into the deep model, (2) reduces gradient estimator variance with theoretical justification and (3) encourages RL exploration of different symbolic forms in the search space of all expressions.
In our experiments, DSR-Rex is evaluated on several challenging scientific datasets, demonstrating superior performance in discovering equations with lower Normalized MSE scores. Additionally, DSR-Rex computes gradients with smaller empirical standard deviation, compared to the previous DSR method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper identifies a problem of deep symbolic regression (DSR) for symbolic regression problems, that failure to capture equivalent expressions results in high variance of gradients and unstable training for the policy gradient estimator. The author proposed to address the problem by appending the symbolic reasoning module to a batch sampling of DSR to capture the equivalent expressions and adopting a new policy gradient method based on the group of equivalent expressions.

### Strengths
**1)** The paper is well written with clear notations, concrete technical details, and illustrative figures to explain the problem.

**2)** The paper is well-motivated by an interesting topic of expression equivalency in the symbolic regression (SR) area, which is promising to attain better performance with existing SR models and develop new SR models.

**3)** Theoretical analysis provides the performance lower-bound as DSR.

### Weaknesses
 **1)** Expression equivalency problems exist in nearly all SR methods. Compared with the large landscape of SR model families, the baseline model DSR is a little bit out-of-date. For example, GPMeld, the successor of DSR in Figure 2, exhibits better performance than DSR, and a similar performance to DSR-REX.  Besides, the benchmarking models adopted in the experiments only encompass Reinforcement Learning (RL) based methods and one RL and genetic programming hybrid method GPMeld. To make stronger conclusions, more types of SR models should be considered, such as AI Feynman 2.0 as cited in the paper which studies similar expression equivalency problems. The current selection of baselines does not provide a comprehensive view of the performance of DSR-REX across different symbolic regression paradigms. Specifically, methods based on genetic programming, gradient-based optimization, and other neural network architectures should be included to validate the general applicability of the proposed approach.

**2)** Figure 3 only compares the efficiency between the steps within the DSR-REX with different architectures. The comparison of efficiency between DSR and DSR-REX would bring in more insights. Furthermore, the analysis of the computational overhead introduced by the symbolic reasoning module is missing. It is crucial to understand how the additional computation impacts the overall training time and resource consumption, especially when dealing with complex expressions. A comparison of the time taken for convergence between DSR and DSR-REX would be beneficial.

### Questions
**1)** Can you include more types of SR models in benchmarking, or explain the advantages of DSR-Rex over AI Feynman 2.0 in capturing equivalent expressions?

**2)** In equation (4), You mentioned that $\mathbb{I}$ \{ $\cdot$ } $=1$ if $\tau$ can be converted to $\phi$, however, according to the definition in line 85, $\phi$ is one specific expression. How do you obtain the probability of the equivalent group? Do you mean $\phi$ represents all equivalent expressions to $\phi$ here? In line 181, "all possible sequences" refers to all the sequences in the same equivalent group, or all the expressions have been sampled?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents Deep Symbolic Regression via Reasoning Equivalent Expressions (DSR-REX), an enhancement to deep reinforcement learning-based symbolic regression (DSR). The key innovation is leveraging numerically equivalent mathematical expressions to reduce policy gradient estimate variance while maintaining unbiasedness. The method incorporates a symbolic reasoning module that generates equivalent expressions through mathematical transformations, leading to improved convergence and performance compared to baseline deep RL methods. The authors provide theoretical guarantees for their approach and demonstrate empirical improvements on several datasets.

### Strengths
* Interesting approach to leveraging equivalent expressions for variance reduction in symbolic regression, with supporting theoretical analysis
* The methods to reason and find equivalent expressions are straightforward and fast, making them easy-to-use for future works.

### Weaknesses
 * Limited evaluation scope using primarily trigonometric datasets and a small subset of Feynman equations, rather than standard benchmarks like SRBench (all Feynman equation, black-box datasets)
* Comparison against outdated baselines (DSR, neural guided GP) rather than current SOTA methods like PySR, uDSR, E2E, TPSR, and SPL
* Insufficient analysis of how the theoretical guarantees translate to practical scenarios, particularly regarding the sampling distribution of equivalent expressions. The theoretical analysis assumes a uniform sampling of equivalent expressions, which is unlikely in practice due to the nature of the reasoning rules. For example, trigonometric identities often yield many more equivalent forms than algebraic manipulations, potentially biasing the learning process towards trigonometric solutions. This discrepancy between theory and practice needs further investigation.
* Lack of ablation studies on the impact of different group sizes and reasoning rules. Specifically, the reasoning rules are not analyzed individually, and the impact of the maximum group size parameter on the variance and bias of the policy gradient estimator is not explored.

### Questions
1. The theoretical guarantees assume fair sampling of all equivalent sequences for each expression, but in practice this may not hold. Consider two expressions φ₁ and φ₂, where φ₁ finds only two equivalent forms, while φ₂ finds N>>2 equivalent forms through the designed reasoning rules. This could lead to q(φ₂) > q(φ₁) simply due to having more discoverable equivalent forms (e.g., there are lots of trigonometric equivalences compared to other operations), rather than actual learning preference. How does this potential bias affect the training process?

2. What is the value of max group size parameter, and how sensitive is the method to this parameter?

3. Could you clarify if the results shown in Fig. 2 (right) are averaged across all benchmark datasets or specific ones?

4. How are the 10 Feynman datasets selected? Why not evaluate on standard benchmarks like SRBench and compare against more recent SOTA methods?

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
2

### Summary
This paper proposes DSR-Rex, which adds a mathematical equivalence reasoning module to deep symbolic regression to improve the efficiency and stability in the training process (variance reduction). Based on a re-expression of the objective after grouping mathematically equivalent but symbolically different equations, the algorithm uses standard encoding/decoding modules of DSR plus a novel reasoning module that enumerates equivalent expressions of the generated equations, and then modifies the training objective of DSR. It is proved the equivalence of objective functions of DSR-Rex and DSR and reduced variance of the estimated objective using DSR. The performance of DSR-Rex is evaluated on Feymann datasets.

### Strengths
1. Improving the performance of symbolic regression is an important problem, and this paper is likely to have impact for the important method of DSR. 

2. The motivating point of addressing equivalent symbolic equations is interesting and insightful. 

3. The paper is clearly structured.

### Weaknesses
1. The presentation clarity of the paper needs to be improved, including notations and method details. Specifically, the notations in the problem setup are not precise. For instance:
- for $\tau=(\tau_1,\dots,\tau_k)$, the meaning and determination of $k$ are unclear. Is it a fixed hyperparameter or dynamically determined? 
- What is each $\tau_i$ -- is each of them a math operator/variable/coefficient? The paper should clearly define the structure and composition of $\tau_i$. 
- In equations (1) and (2), the reward is defined for each sequence $\tau$, but right after that, the notations override previous ones, where $\{\tau_1,\dots,\tau_N\}$ represents multiple sequences. This creates confusion, as each $\tau_i$ now seems to represent a sequence instead of an element within a sequence. 

The paper needs to revise the notations and be rigorous about their meanings throughout the entire text to avoid ambiguity.

2. The motivation needs to be strengthened to justify why numerically equivalent but symbolically different equations will pose challenges to DSR training and why the proposed methods are necessary. While the existence of such expressions is acknowledged, the paper does not provide a convincing explanation of how they negatively affect the stability or efficiency of DSR. Concrete examples or theoretical analysis demonstrating the adverse effects would significantly strengthen the motivation.

3. The experiments can be enhanced by adding more benchmark comparisons. The paper currently only evaluates on 10 tasks selected from the Feymann dataset. While these tasks might be challenging, a broader comparison with established benchmarks like SRBench [1] would provide a more comprehensive evaluation of the proposed method's performance and generalizability.

### Questions
1. Details/notations about problem setup need to be more precise. For instance, 
- for $\tau=(\tau_1,\dots,\tau_k)$, what is $k$? How is it determined? 
- What is each $\tau_i$ -- is each of them a math operator/variable/coefficient? 
- In equations (1) and (2), the reward is defined for each sequence $\tau$, but right after that, the notations override previous ones, where $\{\tau_1,\dots,\tau_N\}$ represents multiple sequences, so here each $\tau_i$ is a sequence, instead of an element in a sequence? 

Please revise the notations and be rigorous about their meanings. 

2. I understand that numerically equivalent but symbolically different expressions exist, and it is reasonable to try to avoid them. However, for the motivation of this work, I was wondering how this might negatively affect DSR. Why does it make it less stable or less efficient, as the authors claim? 

3. Line 196, the sentence "Since we cannot directly use the probability distribution qθ to sample a group of sequences with the
same reward. Instead,..." seems to be grammatically incorrect. 

4. More details of the method for equivalent expressions are needed for clarity: It is claimed that "In practice, equation 7 is not computed by enumerating every expression in Φ (as indicated by the inner summation)." and the details are in Section 3.2. However, Section 3.2 seems difficult to understand. What is the generated equivalent expressions for? How are they used in equation 7? Or is there an equivalent way to compute equation 7 after generating the equivalent expressions? 

5. What if the equivalent expressions in Section 3.2 cannot enumerate all possible choices? What is the consequence, and how would limiting the number of them impact the results? 

6. Setup for Section 5.2: Is Figure 2 the result for one dataset, or aggregating results from multiple datasets? Please consider showing the results for all 10 datasets. 

7. How are the 10 tasks selected from the Feymann dataset? It would also be helpful to consider larger benchmarks like SRBench [1]. 

[1] La Cava, William, et al. "Contemporary symbolic regression methods and their relative performance." Advances in neural information processing systems 2021.DB1 (2021): 1.

8. The high-level idea of addressing numerically equivalent expressions seems widely applicable. Would similar ideas be useful beyond the context of DSR? It would be helpful to have some discussion on the broader scope.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes DSR-REX, which improves the performance of the algorithm by embedding mathematical laws and equalities into deep models. Moreover, the variance of the gradient estimator is theoretically guaranteed to decrease. Finally, in various experimental tests, DSR-REX shows good performance.

### Strengths
##### Strengths

1. In this paper, DSR-REX has achieved good results in comparison with other baselines.
2. Achieving variance reduction of the gradient estimator with a theoretical guarantee.

### Weaknesses
##### Weaknesses

1. I think the chapter arrangement of this article is unreasonable. For example, the related work is actually behind the method, which makes the article very messy.  I spent an hour not understanding what the author was doing.  I think The **Related work** can be put behind the **Introduction**. The  **Motivation ** part of  **METHODOLOGY ** can be appropriately deleted and put into the  **introduction ** part...
2. Many related works are not mentioned.
**Reinforcement Learning for Scientific Discovery.** such as TPSR(Discovering mathematical formulas from data via gpt-guided Monte Carlo tree search), SR-GPT(Discovering mathematical formulas from data via gpt-guided monte carlo tree search),  RSRM(Reinforcement Symbolic Regression Machine)...

**Symbolic Regression with Domain Knowledge:** NSRwH(Controllable neural symbolic
regression), MLLM-SR(MLLM-SR: Conversational Symbolic Regression base Multi-Modal Large Language Models
),  LLM-
SR(LLM-SR: Scientific Equation Discovery via Programming with Large Language Models)...
3. This article only mentioned the symbolic regression method using reinforcement learning, but symbolic regression is not the only one, other methods should appear in the comparison method, e.g. SNIP,(https://doi.org/10.48550/arXiv.2310.02227) MMSR(https://doi.org/10.1016/j.inffus.2024.102681), DSO(NGGP)(https://doi.org/10.48550/arXiv.2111.00053), TPSR(Transformer-based Planning for Symbolic Regression), and so on 
4. The author should test your algorithm on the SRBench dataset.

### Questions
##### Questions

1. The third innovation point of the paper, 'Encours-ages RL exploration of different symbolic forms in the search space of all expres- sions' Is to make the probability of model sampling more random? Like adding entropy loss?
2. Article line 151, additional sequences generated by a symbolic expression reasoning module. How does symbolic expression reasoning module generate additional sequences and what is their role?
3. In Figure 1, the **Reasoned expressions** can improve the performance of the algorithm. Please analyze the reasons for the improvement in the performance of the algorithm more carefully in the article.
4. Although your idea is good, I think it is inappropriate for the words "high-level idea" to appear in an academic paper.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The performance comparison between DSR-REX and previous models like DSR and NGGP highlights its superiority. The complexity of the case study equations effectively showcases the model’s symbolic regression capabilities. Additionally, the paper provides clear details of the algorithm and experimental processes.

Weaknesses:
Questions:

### Strengths
The performance comparison between DSR-REX and previous models like DSR and NGGP highlights its superiority. The complexity of the case study equations effectively showcases the model’s symbolic regression capabilities. Additionally, the paper provides clear details of the algorithm and experimental processes.

### Weaknesses
The paper lacks comparisons with other tasks beyond DSR, such as SPL[1], TPSR[2], and uDSR[3], across different benchmarks like SRbench[4]. It also does not discuss how this method could be applied to these models.

### Questions
1. Could you provide DSR-REX’s results on SRBench[4] or SRSD-Feynman[5] to assess the model's stability under varying noise levels and complexities with scientific implications?

2. What level of improvement might your method bring if applied to other models like SPL[1], TPSR[2], and uDSR[3] for training?

3. Could you share the recovery rate for each expression in Chapter 5.2, Experimental Analysis?

4. Could you include an ablation study on parameters in Appendix Section D?

5. Could you compare DSR-REX with models like SPL, TPSR, and uDSR [1, 2, 3] in the experiments in Chapter 5？

[1]Sun F, Liu Y, Wang J X, et al. Symbolic physics learner: Discovering governing equations via monte carlo tree search[J]. arXiv preprint arXiv:2205.13134, 2022.

[2]Shojaee P, Meidani K, Barati Farimani A, et al. Transformer-based planning for symbolic regression[J]. Advances in Neural Information Processing Systems, 2023, 36: 45907-45919. 

[3]Landajuela M, Lee C S, Yang J, et al. A unified framework for deep symbolic regression[J]. Advances in Neural Information Processing Systems, 2022, 35: 33985-33998. 

[4]La Cava W, Orzechowski P, Burlacu B, et al. Contemporary symbolic regression methods and their relative performance[J]. arXiv preprint arXiv:2107.14351, 2021. 

[5]Matsubara Y, Chiba N, Igarashi R, et al. Rethinking symbolic regression datasets and benchmarks for scientific discovery[J]. arXiv preprint arXiv:2206.10540, 2022.

### Soundness
2

### Presentation
3

### Contribution
2
