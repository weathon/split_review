# Generalized Resource-Aware Distributed Minimax Optimization

- Decision: Reject
- Avg Score: 5.33
- Scores: 3, 8, 5

## Abstract
Traditional distributed minimax optimization algorithms cannot be applied in resource-limited clients dealing with large-scale models. In this work, we present *SubDisMO*, a generalized resource-aware distributed minimax optimization algorithm. *SubDisMO* prunes the global large-scale model into adaptive-sized submodels to accommodate varying resources during each communication round. However, the randomly pruned submodels are susceptible to *arbitrary submodel sharpness*, which can hinder generalization and lead to slow convergence. To address this issue, *SubDisMO* trains the arbitrarily pruned submodels with perturbations by optimizing the minimax objectives, enhancing the *generalization* performance of the aggregated full model. We theoretically analyze our proposed resource-aware *SubDisMO* algorithm, demonstrating that it achieves an asymptotically optimal convergence rate of $O(1/\sqrt{QT\mathcal{C}^*})$, which is dominated by the minimum covering number $\mathcal{C}^*$. We also show the generalization bound of *SubDisMO*  corresponding to the remaining rate in each layer. Extensive experiments on *CIFAR-10* and *CIFAR-100* datasets demonstrate that *SubDisMO* achieves superior generalization and effectiveness compared to state-of-the-art baselines.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies distributed minimax optimization problem in the context of resource-limited clients. The paper introduces a generalized resource-aware distributed minimax optimization algorithm, which prunes the global large-scale model into adaptive-sized submodels with perturbations to accommodate varying resources during each communication round. The theoretically results demonstrate asymptotically optimal convergence and provide a generalization bound corresponding to the parameters. Experiments on CIFAR-10 and CIFAR-100 demonstrate the superior generalization and effectiveness of the algorithm.

### Strengths
This paper is well-written with clear objectives and contributions. It is the first time that a resource-limited distributed method was proposed for the minimax problem. The proposed algorithm adaptively generates submodels through local resources and trains with perturbations, which enhances the generality of the global model. The theoretical result provides a convergence bound that matches the sota result for full model settings and a generalization bound corresponding to the perturbation and parameter remaining rate in each layer.
Experiments verifies the results.

### Weaknesses
My major concern about this paper lies in the assumptions on the stepsize $\eta_l$ and $\eta_g$ in the theoretical analysis.
i). The conditions in Theorem 1 are somehow self-contradictory. According to line 3 - 6 in the big blanket, $\eta_g\leq\frac{\sqrt{C*}}{8TL\sqrt{N}}$ and $\eta_g\geq 128L$, it follows that L must be a very small number, i.e., $L\leq\frac{1}{32\sqrt{T}}$, and as T increases, L must become increasingly smaller. This is a very strong assumption. 
ii).The values of $\eta_g$ in Corollary 1 do not satisfy the condition $\eta_g \leq \frac{\sqrt{C*}}{8TL\sqrt{N}}$ in Theorem 1.

Besides, the numerical results for the full model version of SubDisMO should be added. Theoretically, the performance of this version should align with that of FedAvg and FedSAM, but these results are not included in Table 1. Adding this comparison would provide a more comprehensive evaluation.

My concern on the parameter $\eta_l$, $\eta_g$ and $L$ are partially addressed. However, I still have the following concerns.

1. You have fixed the proof, and I tried to follow it. However, as you have local update on each node, outer loop iteration and inner loop iteration. It really hard to tell what you referred exactly in the proof, say $\theta_q$, $\tilde \theta_q$ and $\Delta_q^i$ in line. 736-747. I have check both the main text and the appendix, NO exact definition of these variables but some similar definitions $\theta_q^i$ and $\Delta_{q,n}^i$.  Maybe it is obvious, however, as a theoretical paper, the authors must pay more attention to these details and make. these exact, instead of letting the readers to guess.

2. In your analysis, $delta$ would only introduce extra errors. However, the empirical results indicate that the perturbation. is important in achieving the SOTA result. You show $\delta = 0.01$ Acc= 49.73 v.s. $\delta$ = 0.1 Acc=51.23 in Table 2, while in column 2 of Table 1 many baseline method achieve Acc higher than 49.73. There is a great gap here. The empirical performance improvement comes from extra errors in theory. I am confused.

### Questions
1.In Theorem 1, it appears that a smaller $\delta$ leads to a better bound, which is counterintuitive and contradicts the experimental performance. Could you further clarify the impact of $delta$?

2.Why do the performances of FedAvg and FedSAM in your experiments appear to be lower than those reported in the original paper? The original results show that both methods achieve over 80% accuracy on CIFAR-10, whereas your reported results are below 60%.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper introduces SubDisMO, a resource-aware distributed minimax optimization algorithm designed to enhance the generalization capability of global models in resource-limited environments. SubDisMO mitigates model sharpness by using perturbations to adaptively train submodels, thereby improving overall model performance. The authors provide a rigorous theoretical analysis, proving that SubDisMO achieves an asymptotically optimal convergence rate of $O(1/\sqrt{QTC^*})$ under non-convex conditions, along with a tighter generalization bound based on perturbation and parameter retention rates in each layer. Extensive experiments on CIFAR-10 and CIFAR-100 demonstrate that SubDisMO outperforms existing state-of-the-art methods in resource-constrained training scenarios, validating its effectiveness and superior generalization capabilities.

### Strengths
Originality: SubDisMO introduces a novel approach by integrating distributed optimization, model pruning, and adversarial training, addressing the challenge of training large-scale models in resource-constrained environments.

Quality: The research is of high quality, with rigorous theoretical analysis and extensive experiments that validate the algorithm's effectiveness against state-of-the-art methods on standard datasets.

Clarity: The paper is well-organized and clearly articulates the problem, methodology, and results, with figures and tables that effectively support the presentation.

Significance: SubDisMO's ability to train large models efficiently in distributed settings with limited resources is significant for edge computing and privacy-preserving ML, potentially impacting a broad range of applications.

### Weaknesses
## Complexity Analysis:
The paper could further improve by providing a more detailed analysis of the computational complexity of SubDisMO compared to other methods. While the focus is on communication efficiency, understanding the trade-offs in terms of computational resources could provide a more comprehensive view of the efficiency gains. Specifically, a comparison of the number of floating-point operations (FLOPs) and memory usage per client for SubDisMO versus other state-of-the-art methods would be beneficial. This could be presented in a table format for easy comparison, similar to Table 1 in the paper, but focusing on computational metrics.

## Scalability Concerns:
Although the paper addresses the challenge of limited resources, there is room for a deeper discussion on the scalability of SubDisMO in extremely large-scale distributed systems with potentially thousands of clients. Addressing how the algorithm performs as the number of clients grows would be valuable. For instance, the paper could include experiments or theoretical analysis demonstrating the performance and convergence characteristics of SubDisMO with varying numbers of clients, such as 100, 500, and 1000. Additionally, a discussion on potential bottlenecks or challenges that might arise in such large-scale settings would be insightful, such as increased communication overhead or heterogeneity in client computational capabilities.

### Questions
## Computational Complexity:
How does the computational complexity of SubDisMO compare to other state-of-the-art distributed learning algorithms?

## Scalability in Large-Scale Systems:
What are the expected performance and convergence characteristics of SubDisMO when the number of clients increases to several thousands? Are there any bottlenecks or challenges anticipated?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a distributed minimax optimization algorithm, SubDisMO, assigning adaptive-sized submodels to the clients based on the resource budgets, thus enhancing the generalization of the global model by training adaptive submodels with perturbations. Additionally, the paper provides the theoretical analysis of convergence and generalization bound of SubDisMO, and experimental results demonstrate its superior effectiveness compared to state-of-the-art methods.

### Strengths
1. SubDisMO is the first distributed minimax optimization algorithm to account for resource budgets, enabling the training of resource-adaptive submodels with perturbations.
2. The paper provides the theoretical analysis of the convergence rate and generalization bound of SubDisMO.
3. It includes an in-depth analysis of different heterogeneity of client data, minimum covering number and the upper bound of the perturbation to evaluate the effectiveness of SubDisMO.

### Weaknesses
1. The formulation of SubDisMO as a distributed minimax optimization problem needs further clarification. Specifically, in Equation 2 on page 2, it is unclear whether, after altering the constraints of the minimax problem, Equation 2 still can be recognized as a minimax problem. This raises questions about whether SubDisMO functions as a distributed minimax optimization problem or more as a solution to minimax problems. The introduction of resource constraints and adaptive submodels, while practically relevant, seems to deviate from the standard minimax formulation, making it unclear if the core properties of minimax optimization are preserved. The paper should provide a more rigorous justification for why this modified problem still falls under the umbrella of minimax optimization, especially considering the non-standard constraints introduced.
2. While SubDisMO claims that it’s a resource-aware distributed minimax optimization algorithm, it lacks analysis on the impact of varying resource budgets, particularly concerning the influence of mask distribution in SubDisMO. The paper does not provide sufficient detail on how different resource budgets affect the mask selection process and the resulting submodel architectures. It is unclear how the algorithm adapts to scenarios where resource availability varies significantly across clients. A more thorough investigation into the relationship between resource budgets, mask distributions, and model performance is needed. Specifically, the paper should include experiments that systematically vary resource budgets and analyze the resulting impact on the learned models.
3. Some figures in the paper need clearer presentations, for example, Figure 2 and Figure 4 need to be clear enough to see the difference between each method setting. The current presentation makes it difficult to discern the performance differences between the proposed method and the baselines. The figures should use clearer markers, line styles, and potentially include error bars to better visualize the results and their statistical significance. The lack of clarity in these figures hinders the ability to assess the effectiveness of SubDisMO.

### Questions
1. SubDisMO designs a novel distributed minimax optimization problem, which introduces an inner maximization on perturbation $\epsilon_i$ for each client submodel. I have a question about this definition in Eq.2 on page 2: after changing the constraints of the minimax problem, can Eq.2 be recognized as a minimax problem? Is SubDisMO more like a solution for distributed minimax optimization problems?
2. In SubDisMO, the masking policy of the submodel is random, I have a question: if the masking policy is rolling, whether SubDisMO can still work in this setting? It means the performance of rolling mask with perturbation. Is the performance of this combination better than the current random mask with perturbation?

### Soundness
3

### Presentation
2

### Contribution
3
