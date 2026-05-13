# Statistical Guarantees for Approximate Stationary Points of Shallow Neural Networks

- Decision: Reject
- Scores: 3, 6, 6, 3

## Abstract
Since statistical guarantees for neural networks are usually restricted to global optima of intricate objective functions, it is unclear whether these theories explain the performances of actual outputs of neural network pipelines. The goal of this paper is, therefore, to bring statistical theory closer to practice. We develop statistical guarantees for shallow linear neural networks that coincide up to logarithmic factors with the global optima but apply to stationary points and the points nearby. These results support the common notion that neural networks do not necessarily need to be optimized globally from a mathematical perspective. We then extend our statistical guarantees to shallow ReLU neural networks, assuming the first layer weight matrices are nearly identical for the stationary network and the target. More generally, despite being limited to shallow neural networks for now, our theories make an important step forward in describing the practical properties of neural networks in mathematical terms.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper establishes generalization guarantees for shallow neural networks corresponding to the stationary points of $\ell_1$-regularized regression problem. When the ground truth is a shallow neural network whose weights have a "reasonable" norm, the authors establish that, for both linear and ReLU shallow nets, the stationary points' population error is almost as good as the ground truth, as long as the stationary points are close to the ground truth.

### Strengths
- The paper studies whether finding stationary points is sufficient for good performance. This is an interesting problem. 
- The paper is written clearly, especially in the appendix where each step in the proofs is described well.

### Weaknesses
1. _Lack of emphasis on the boundedness assumption_: The paper uses the term reasonable stationary points in its theorem statements to indicate that the weight matrices have bounded norm. The boundedness is used repeatedly in the proofs and is the main ingredient needed for the proofs. The term "reasonable stationary point" leads the reader to believe that stationarity is an important component when only the boundedness is. The paper can be improved if the authors are clear about this fact.
2. _Stationarity is not used: The paper's results are uniform results that hold for all points in a bounded set. Indeed both the generalization results that rely on Lemma 1 are uniform generalization bounds. Stationarity is used in line 968 to introduce $\nabla \mathrm{risk}_X$ in the inequality, but the boundedness assumptions would have been sufficient to do so in my view.
3.  _Approximate stationary points_: An alternative definition of approximate stationary point is provided in the paper. Instead of small gradient norms, an approximate stationary point is defined as a point whose objective value is close to an exact stationary point. It is not clear how such a point can be obtained computationally. Without some form of gradient domination conditions, it is difficult to translate optimization results that only guarantee small gradient norms to the paper's definition of approximate stationarity. (For example, in almost flat but slightly slanted regions in the landscape, gradient norms are very small but not necessarily close to a stationary point).
4. _Imprecisitions in proofs_: I find the proof of Lemma 1 to be unclear. This relates to point 1 where the authors choose not to clearly state the boundedness assumption. In the proof $\eta$ plays the role of the bound. Unfortunately, the Case 1 Case 2 split is a little difficult to understand. $\tilde{\beta}$ depends on the data so it is a random quantity, meaning Case 1 and Case 2 are random events, are you conditioning on these events in the derivations?  The result in Lemma 1 is standard if the authors write it with clarity on their boundedness assumption.

### Questions
In my understanding, the paper aims to analyze stationary points but its results are uniform bounds that hold over a bounded ball. A sign that this is the case follows from the fact that $\beta^* = (\gamma ^*, \Theta^*)$ is not required to be the ground truth anywhere in the proof of Theorem 1 for example. The results would hold for any choice in a bounded ball. Can the authors correct my understanding by pointing me to where the optimality of $\beta^* = (\gamma ^*, \Theta^*)$ is used?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper aims to provide statistical guarantees for stationary points of shallow neural networks, both linear and ReLU. The study demonstrates that under certain regularization conditions, these approximate stationary points achieve near-optimal generalization comparable to global optima.

### Strengths
This paper focused on approximate stationary points instead of global minima, which is more relevant to practical deep learning settings. By generalizing the result to ReLU networks, the significance of this result is enhanced. The rigorous mathematical proofs make the result quite solid.

### Weaknesses
1. Some of the expressions in mathematical statements are a bit ambiguous. For example, there are "$\approx$" used in Assumption 2 and Theorem 3. I think using such notation in the explanation part is ok but in mathematical statements it should be more rigorous. I can't even find the rigorous expressions in appendix. Besides, "the second and third parts of Assumption 1 and Assumption 2" in Theorem 3 is not a precise sentence and may cause ambiguity. The use of "$\approx$" introduces a lack of clarity regarding the precise bounds or relationships being established. It's crucial to define what level of approximation is acceptable and how it impacts the subsequent analysis. The absence of rigorous definitions in the appendix further complicates the issue, making it difficult to verify the claims. Furthermore, the reference to "the second and third parts of Assumption 1 and Assumption 2" is vague and could lead to misinterpretations. It would be beneficial to explicitly state which conditions are being referenced, perhaps by assigning labels to each part of the assumptions.
2. The assumption of the part of ReLU nets seems strong since it requires that the stationary point $\tilde{\Theta}$ is close to the ground truth $\Theta^*$, which does not align with the goal of analyzing all approximate stationary points. I think more discussion about the necesity of this assumption can be added. This assumption, requiring $\tilde{\Theta}$ to be close to $\Theta^*$, significantly restricts the scope of the analysis. It essentially assumes that the optimization process will converge to a solution near the true parameters, which is not always the case in practice. The paper should provide a more thorough justification for this assumption, explaining why it is necessary for the current proof approach and what limitations it imposes on the generality of the results. It would also be useful to discuss alternative scenarios where this assumption might not hold and how the analysis would be affected.
3. In Section 6, there are some technical results. Apart from the results, I think how these results are applied in the proof of main theorems are equally important. I cannot easily see the relation between these propositions and the main theorems of the paper so maybe some explanations are needed. The technical results in Section 6, while potentially important, lack clear connections to the main theorems. The paper should explicitly outline how each proposition contributes to the overall proof strategy. For instance, it would be helpful to explain how specific bounds or properties derived in the propositions are used in the subsequent steps of the main theorem proofs. This would enhance the reader's understanding of the logical flow and the role of each technical result.
4. Although this is a theoretical paper, I think more experiment can be added. The experiments in the paper only verify the theoretical results specific to the simple architectures. Since theoretical papers aim to bring insights for more genral settings, experiments on more practical and complicated networks are good to illustrate the genral information of the theory. The experimental section is limited to simple architectures, which raises questions about the practical relevance of the theoretical findings. It would be beneficial to include experiments on more complex and realistic neural network architectures, such as convolutional or recurrent networks. This would help to demonstrate the applicability of the theory to more general settings and provide empirical evidence for the claims made in the paper. The current experiments are insufficient to support the broader implications of the theoretical results.
5. The oracle tuning parameter $r_{orc}$ in line 190 seems vital in the theorems. How is this parameter important in the theorems and why should $r$ be larger than $r_{orc}$? Maybe there can have more discussion. The role of the oracle tuning parameter $r_{orc}$ is not adequately explained. The paper should provide a more detailed discussion of how this parameter influences the theoretical results and why the condition $r > r_{orc}$ is necessary. It would be helpful to explain the intuition behind this parameter and how it relates to the underlying statistical properties of the problem. Without a clear understanding of $r_{orc}$, it is difficult to assess the practical implications of the theoretical findings.

### Questions
See weakness part.

### Soundness
3

### Presentation
2

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
This paper presents a statistical framework for analyzing shallow neural networks, offering guarantees for approximate stationary points rather than global optima. Recognizing the non-convex nature of deep learning objectives and the challenges of finding exact solutions, the authors address an important gap: They demonstrate that practical training outcomes—stationary points or points close to them—can still generalize effectively under certain conditions (Theorems 1-3). By focusing on stationary points, the paper connects statistical theory with real training outcomes, suggesting that approximate optimization may often suffice for effective generalization.

However, it’s worth noting that their analysis is limited to shallow ReLU networks, while practical applications predominantly involve deep networks. Therefore, this analysis remains a step away from the highly complex pipelines in modern deep learning. Nonetheless, as an initial study in this area, the paper is quite valuable. Overall, I think it’s a solid contribution, which is why I rate it a 6, just above the acceptance threshold.

### Strengths
**Clarity:** The paper is generally well-organized, with a clear progression from theoretical background to the main results and implications. Each section is introduced with clear motivations, and notations are consistently defined.

**Significance:** This work provides crucial theoretical support for the practical success of neural networks, showing that networks trained to stationary points can perform nearly as well as those trained to global minima. However, it is important to note that the current analysis is limited to shallow ReLU networks. As an initial study in this area, the paper is highly valuable. Extending this analysis to deeper networks and other activation functions would greatly benefit the deep learning community, particularly in reinforcing the theoretical foundations of deep learning.

### Weaknesses
 **Empirical Limitations:** The empirical results are confined to small-scale simulations and toy models, which may limit the perceived robustness of the theoretical findings. The paper would benefit from experiments on more complex datasets. The current simulations do not adequately demonstrate the practical applicability of the theoretical results. For example, the paper could include experiments on image classification tasks using datasets such as CIFAR-10 or ImageNet, which are standard benchmarks in the field. This would help to validate whether the theoretical guarantees hold in more realistic scenarios. The lack of experiments on real-world datasets makes it difficult to assess the practical relevance of the proposed framework.

**Assumptions for Shallow ReLU Networks:** The assumption of a nearly identity first-layer weight matrix for ReLU networks may restrict the practical relevance of Theorem 3. While the authors acknowledge this limitation, a deeper discussion of how these results might extend beyond isotropic conditions would be beneficial. The paper does not provide a clear justification for why this assumption is reasonable in practice, and it is unclear how sensitive the results are to deviations from this assumption. Furthermore, the analysis does not consider the impact of different initialization schemes, which could significantly affect the behavior of the network and the validity of the theoretical results. The paper should explore the implications of this assumption and discuss potential ways to relax it.

### Questions
**Practicality of the Isotropic Weight Assumption for ReLU Networks:** Could the authors provide more context on the feasibility of using an isotropic first-layer weight matrix in practical shallow ReLU networks? Are there scenarios where this assumption might naturally hold, or is it primarily for theoretical tractability?

**Generalizability to Deeper Architectures:** Would the authors consider extending their results to deeper architectures, such as multi-layer networks with more than one hidden layer? If not, could they elaborate on the technical or computational challenges that arise when moving beyond shallow networks?

**Experiments Limited to SGD Optimization:** The authors mention in Line 2472 that the numerical results in the paper are based solely on the use of the SGD optimizer. Given the range of optimizers commonly used in practice (e.g., Adam), do the authors have insights into how different optimization algorithms might affect the empirical outcomes? Could alternative optimizers potentially achieve better performance or faster convergence at approximate stationary points?

### Soundness
3

### Presentation
4

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
The paper studies the generalization risk for “reasonable” stationary points of the empirical loss function in the scenarios of two layer linear network and two layer ReLU network. With certain data assumptions and requiring a near-identity weight matrix, the paper shows bounded risk for these “reasonable” stationary points.

### Strengths
An interesting consequence of the paper's theory is that if the regularization term is (close to) zero (i.e., r=0) then the generalization error/risk of these “reasonable” stationary points is exactly the same as that of the optimal. 

The theory extends from linear network to a more practical and interesting scenario – two layer ReLU network.

### Weaknesses
Although at first sight the theorems and results look neat, after reading the proof, I found that these results strongly rely on the strong assumptions of data (Assumption 1) and (for ReLU network) the near-identity of weight matrix $\Theta$ (Assumption 2). Without these assumptions (or with milder assumptions) the theoretical results will break.

Note that the setting of Assumption 1 and 2 make the network and optimization problem far from practical. For example, the weight matrix $\Theta$ is never close to identity in practice. I disagree with the paper’s claim that “(the) theories make an important step forward in describing the practical properties of neural networks…” Instead, I feel these conditions make the research direction more deviated from the goal of “describing practical properties of neural networks”.

The paper claims “we focus on regression, which is more general and mathematically more challenging than classification”. This is incorrect. In many deep learning theories, classification turns out to be more challenging to mathematically analyze than regression problems, which is opposite to the paper’s claim. Moreover, the theories of the paper seems not applicable to classification which has a different loss function, hence it is also not reasonable to claim regression is more general than classification.  

The paper says in Line 148 that using $\ell_1$-regularization is to “to mimic deep-learning practice”. In practice, $\ell_1$-regularization is not that often used in practice, especially when compared to other regularization methods, for example, weight decay. I am wondering whether the theory still holds when a different regularization is used.

### Questions
see comments in the Weaknesses section

### Soundness
3

### Presentation
3

### Contribution
1
