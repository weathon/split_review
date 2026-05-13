# Neighborhood and Global Perturbations Supported SAM in Federated Learning:  From Local Tweaks To Global Awareness

- Decision: Reject
- Scores: 3, 3, 5, 5

## Abstract
Federated Learning (FL) can be coordinated under the orchestration of a central server to collaboratively build a privacy-preserving model without the need for data exchange.
However, participant data heterogeneity leads to local optima divergence, subsequently affecting convergence outcomes. Recent research has focused on global sharpness-aware minimization (SAM) and dynamic regularization techniques to enhance consistency between global and local generalization and optimization objectives. Nonetheless, the estimation of global SAM introduces additional computational and memory overhead, while dynamic regularization suffers from bias in the local and global dual variables due to training isolation.
In this paper, we propose a novel FL algorithm, FedTOGA, designed to consider optimization and generalization objectives while maintaining minimal uplink communication overhead. By linking local perturbations to global updates, global generalization consistency is improved.    Additionally, global updates are used to correct local dynamic regularizers, reducing dual variables bias and enhancing optimization consistency.    Global updates are passively received by clients, reducing overhead.
We also propose neighborhood perturbation to approximate local perturbation, analyzing its strengths and limitations. Theoretical analysis shows FedTOGA achieves faster convergence $O(1/T)$ under non-convex functions. Empirical studies demonstrate that FedTOGA outperforms state-of-the-art algorithms, with a 1\% accuracy increase and 30\% faster convergence, achieving state-of-the-art.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents FedTOGA, a Federated Learning (FL) algorithm  designed to prevent the heterogeneity of client data cause the global model to converge to a sharp local minimum. FedTOGA achieves this in a 
communication-efficient way by combining new variants of two techniques: (i) Sharpness-Aware Minimization (SAM) to add perturbations to the training process and (ii) local dynamic regularization. In contrast to existing literature, FedTOGA uses the global gradient update to adjust both the global perturbation and the local regularization. The authors obtain analytic convergence guarantees for their methodology, and show the effectiveness of their approach by conducting extensive experiments.

### Strengths
+ Comprehensive validation: In Sec. 6, FedTOGO is compared against a lot of FL algorithms and is able to outperform all of them.

### Weaknesses
 + In the first contribution bullet point in Sec. 1, the claim about FedTOGA being the first global perturbation technique and first local dynamic regularizer needs to be rephrased to emphasize more on the fact that it is the first to do so using the global update. The current version of this statement overlooks the contributions of FedSMOO, FedLESAM, FedSpeed and papers that use dynamic regularizers, which have developed these ideas but without using global updates.
+ In Sec. 2's Sharpness-Aware Minimization, the parameters \rho and \delta need to clearly defined. Specifically, \rho appears to be a learning rate, but its exact role in the perturbation process is not clear. Similarly, \delta, which seems to be related to the global gradient, needs a more precise definition in the context of the SAM update.
+ In Eq. (4) given in Sec. 2.1, the notation \theta_i seems to imply the different local models for clients in the FL setup. If this is the case, this needs to be clarified by defining \theta_i, which is missing currently. The same comment applies for Eq. (6) in Sec. 4.1, where the minimization is being done over a single vector \theta while there are multiple \theta_i's in the loss function formulation. This inconsistency in notation makes it difficult to understand how the local and global updates are being combined.
+ In Assumption 3 in Sec. 5, can the authors explain why they need a bounded variance of the unit gradient, and why just a bounded variance of the gradient itself is not sufficient? Adding some references which also make this assumption for the unit gradient is recommended. The justification for this assumption is not clear, and it is unclear why the unit gradient is necessary for the convergence proof.
+ In Sec. 6, does FedTOGO and most of the other FL algorithms perform similarly if the data distribution among clients is IID? Currently all experiments are done in non-IID settings and it would be insightful to 
see how these FL methods compare in IID setups. The lack of IID experiments makes it difficult to assess the robustness of the proposed method in different data distributions.
+ The global perturbation used in this paper build heavily on prior research, doing a gradient ascent similar in existing algorithms with the addition of some global update information. The same goes for the local regularizer. While it is interesting to see how much accuracy increase can be achieved by making these adjustments, I am concerned about the novelty of this incremental idea. Alongside other issues mentioned above, I do not think this paper is ready to be published at ICLR in its current version.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

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
The paper proposes a global-aware perturbation method for sharpness-aware minimization (SAM) in federated learning (FL). Compared with existing methods, this paper combines the idea of local dynamical regularizer with global updates to mitigate the effect of data heterogeneity. Convergence of the proposed algorithm is theoretically analyzed with the rate $O(1/T)$. Empirical results are shown to justify the performance of the algorithm.

### Strengths
The main contribution of the paper is to propose a local and global perturbation-based algorithm (FedTOGA) that enjoys communication and computation efficiency for SAM in FL. Both theoretical convergence guarantee and empirical evaluation of the algorithm are provided.

### Weaknesses
1. The novelty and contribution of the paper is limited. I think the main advantage of the proposed algorithm that authors claim is to leverage the global and neighborhood perturbation to reduce communication overhead and computational cost. However, this is not clear in the paper. As in Theorem 2 the authors claim that the rate of $O(1/T)$ is achieved when setting $K=O(T)$, which is faster than existing literature. However, FedSMOO also achieves the same rate $O(1/T)$ and linear speedup in the number of clients without any constraint on $K$. Thus, the advantage of FedTOGA is not clear.

2. The analysis tools look quite similar to those in FedSpeed paper. Thus, the technical contribution of this paper seems limited.

3. The presentation of the paper is not good, which makes the reader hard to follow. There are some mistakes and typos. To list a few, in Line 300,  there is no "Line 16" in the algorithm. In Theorem 2, $z_t$ is not defined and in eq. (11) the LHS should be the sum of $\Vert z_t \Vert^2$.

### Questions
1. Could the authors further explain why their algorithm is better comparing to previous methods in terms of e.g. convergence rate, computational cost, challenge in implementation, etc?

2. What are the technical difficulties of the theoretical analysis, comparing to literature?

3. As in Theorem 2, the choice of learning rate is with order $O(1/\sqrt{T})$ while constants are ignored. However, these neglected constant may significantly influence the actual performances of the algorithms. Could the authors explain why the learning rates are identical for all algorithms? In the above sense, does it cause a fair comparison? If yes, could the authors explain the reason why this renders a fair comparison?

### Soundness
2

### Presentation
1

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
To address the local optima divergence in Heterogeneous Federated Learning, this paper proposes a FedTOGA method by linking the local dynamic regularizer to global updates to enhance the consistency of optimization and generalization. The method efficiently links local perturbations to global updates and achieves a non-convex convergence rate of $\mathcal{O}(1/T)$. The authors also propose neighborhood perturbation to approximate local perturbation. The authors also provide empirical validations of the theoretical results as well.

### Strengths
1. The proposed method is well-motivated, the paper shows that existing methods suffer from the local optima divergence issue, and show how to fix it.
2. The empirical results show that the FedTOGA method is better than other HtFL methods using global sharpness-aware minimization (SAM) and dynamic regularization, as expected.

### Weaknesses
1. In Theorem 2, compared with other methods using global sharpness-aware minimization (SAM) and dynamic regularization, such as [1],  a more distinct summary of the superiority of FedTOGA may be needed. Specifically, it is not clear how the convergence rate of $\mathcal{O}(1/T)$ for FedTOGA is a significant improvement over existing methods that also employ SAM and dynamic regularization. The theoretical analysis should explicitly highlight the specific conditions or assumptions under which FedTOGA achieves a better convergence rate or a tighter bound compared to these methods. A more detailed comparison of the constants and terms within the convergence rate expressions would be beneficial.
2. In addition to CIFAR10/100, the authors should also consider the performance of FedTOGA in the TinyImageNet task. The current empirical evaluation is limited to relatively small datasets. Evaluating the method on a more complex and larger dataset such as TinyImageNet would provide a more robust assessment of its scalability and generalization capabilities. This is particularly important given the heterogeneous nature of federated learning, where performance on diverse and challenging datasets is crucial.
3. In FL research, the local epoch is an important parameter. The authors should study this parameter's impact on performance. The number of local epochs (K) can significantly influence the trade-off between local model convergence and global model aggregation. A sensitivity analysis of the parameter K is needed to understand how it affects the performance of FedTOGA. The analysis should include a discussion on how to choose an appropriate value of K for different datasets and scenarios, and how this choice impacts the convergence and generalization of the model.

### Questions
See in weaknesses.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an improved optimizer based on SAM, which further enhances the global perspective when applying SAM in federated learning (FL) and maintains global generalization. Both the theoretical analysis and extensive experiments confirm the effectiveness of the proposed method.

### Strengths
1. The design motivation of this paper is reasonable. Although there are some flaws in the writing, the overall structure is understandable.

2. The experiments are very thorough, with extensive empirical studies conducted under standard settings to validate the efficiency of the proposed techniques.

3. A convergence analysis was conducted for the proposed method to demonstrate that its convergence remains at the same level as the previous works.

### Weaknesses
1. The section on Methods (Section 4) is quite disorganized. I suggest that the authors include a notation table to explain all the variables that appear later in the text. I noticed that many variables are introduced without explanation, see questions.

2. The definition of Equation (9) seems somewhat obscure and difficult to understand. The vanilla local objective (like FedDyn) adopts the the augmented alternating direction method of multipliers to solve the consensus problem. The term $h_i$ is the dual variable to balance the dual problem. Performing operations on the dual term seems to affect the consistency solution of the primal problem. I suggest that the authors remove the problem formulation related to Equation (9) and directly introduce the use of certain variables to replace or correct the gradient. Actually, from the optimization perspective, the proposed method still solve eq.(8), but with the novel proposed method (momentum-based gradient estimator and SAM-based local optimizer). If the authors modify the entire Lagrangian function, it still need to be proven that the solution of this function is consistent with the solution of the original problem. I believe this is unnecessary for the techniques proposed in this paper.

3. A technical question: in line 245, according to the motivation of FedCM that $\Delta^t\approx \nabla f(\theta^t)$, why local perturbation is not $\delta_k^t=\rho\frac{(1-\kappa)g_{i,k}^t + \kappa\Delta^t}{\Vert (1-\kappa)g_{i,k}^t + \kappa\Delta^t \Vert}$? It looks like a external momentum in current version. Will the current external momentum setting outperform the original inner momentum form estimation of FedCM?

4. I am confused on line 264. What is the term $g_{i,k}$? Why the fusion term performs as $g_{i,k} + \widetilde{g}_{i,k-1}^t + \kappa\Delta^t$?

5. Line 11 in Algorithm 1, what is the term $g_{i,k}^{t}[\widetilde{g}_{i,k-1}^t]$?

6. What is the conection between the term in line 264 and "lookahead" optimizer? Although the paper claims that this form is an extension of lookahead, the authors could provide the corresponding extended formulas to further explain why this form corresponds to lookahead optimizers.

7. Could the authors compute the variance of the SAM perturbations? In fact, if the global perturbation is approached more closely, the variance of their local perturbations should be smaller. Additionally, the authors could calculate the global perturbation at the beginning of each round and compare whether this approach leads to further improvements.

Some typos:

(1) There are issues with the references in this paper. I suggest that the authors distinguish between the \citet and \citep commands to provide correct citations.

(2) Line 901 "waht" to what

### Questions
1. A technical question: in line 245, according to the motivation of FedCM that $\Delta^t\approx \nabla f(\theta^t)$, why local perturbation is not $\delta_k^t=\rho\frac{(1-\kappa)g_{i,k}^t + \kappa\Delta^t}{\Vert (1-\kappa)g_{i,k}^t + \kappa\Delta^t \Vert}$? It looks like a external momentum in current version. Will the current external momentum setting outperform the original inner momentum form estimation of FedCM?

2. I am confused on line 264. What is the term $g_{i,k}$? Why the fusion term performs as $g_{i,k} + \widetilde{g}_{i,k-1}^t + \kappa\Delta^t$?

3. Line 11 in Algorithm 1, what is the term $g_{i,k}^{t}[\widetilde{g}_{i,k-1}^t]$?

4. What is the conection between the term in line 264 and "lookahead" optimizer? Although the paper claims that this form is an extension of lookahead, the authors could provide the corresponding extended formulas to further explain why this form corresponds to lookahead optimizers.

5. Could the authors compute the variance of the SAM perturbations? In fact, if the global perturbation is approached more closely, the variance of their local perturbations should be smaller. Additionally, the authors could calculate the global perturbation at the beginning of each round and compare whether this approach leads to further improvements.



Some typos:

(1) There are issues with the references in this paper. I suggest that the authors distinguish between the \citet and \citep commands to provide correct citations.

(2) Line 901 "waht" to what

### Soundness
3

### Presentation
2

### Contribution
3
