# Algorithmic Stability Based Generalization Bounds for Adversarial Training

- Decision: Accept
- Scores: 6, 5, 6, 8

## Abstract
In this paper, we present a novel stability analysis of adversarial training and prove generalization upper bounds in terms of an expansiveness property of adversarial perturbations used during training and used for evaluation. These expansiveness parameters appear not only govern the vanishing rate of the generalization error but also govern its scaling constant. Our proof techniques do not rely on artificial assumptions of the adversarial loss, as are typically used in previous works. Our bound attributes the robust overfitting in PGD-based adversarial training to the sign function used in the PGD attack, resulting in a bad expansiveness parameter. The peculiar choice of sign function in the PGD attack appears to impact adversarial training both in terms of (inner) optimization and in terms of generalization, as shown in this work. This aspect has been largely overlooked to date. Going beyond the sign-function based PGD attacks, we further show that poor expansiveness properties exist in a wide family of PGD-like iterative attack algorithms, which may highlight an intrinsic difficulty in adversarial training.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Authors study the generalization of adversarial training with projected gradient descent. They provide uniform stability upper bounds of the generalization gap that consider the expansiveness of the adversarial attack operator. In the particular case of replacing the $\text{sign}(x)$ operation in the PGD attack with $\text{tanh}(\gamma\cdot x)$, they can show that their generalization upper bound decays to zero with the number of samples $n$ for a finite value of $\gamma$. The experimental evaluation shows the tradeoff between generalization and robustness given by $\gamma$, where smaller values of $gamma$ obtain good generalization but poor robustness and the opposite happens for larger $\gamma$.

### Strengths
- Simple theory and easy to follow paper. I didn’t read the proofs in full detail, but the main paper is easy to follow and the analysis and experiments are reasonable.

- I found the analysis of the expansiveness of the adversarial attack operator very interesting and up to my knowledge, this has not been considered before.

- When considering finite $\gamma$, authors can show that their generalization upper bound converges to zero with increasing number of training samples $n$.

### Weaknesses
 - Authors claim that their upper bound converges to zero with increasing number of training samples $n$ and the ones of [1,2] do not. This is misleading as [1,2] do not consider the expansiveness of the attack operator and the bound provided in this work, in the same setup as [1,2] does not vanish with $n$ (see lines 369-371). Specifically, the claim that their bound vanishes with $n$ relies on the use of the $\text{tanh}(\gamma \cdot x)$ approximation to the sign function within the PGD attack, and the analysis does not directly apply to the standard sign-based PGD. The paper should clearly state that the vanishing generalization bound is contingent on using the $\text{tanh}$ approximation and does not hold for the standard PGD attack. The current presentation implies a more general result than what is actually proven.

- The difference with the previous bounds is not clearly covered in the paper. The proof technique and assumptions are very similar to [1,2], nevertheless the bounds in [1,2] are not presented in the work and there is no discussion about how to integrate previous bounds with the expansiveness setup introduced in this work, making it difficult to assess the contributions. It would be nice to add a discussion about which role expansiveness plays in the result of [1,2], i.e., can it result in a vanishing upper bound with $n$? It would also be good to have a table comparing the different upper bounds. The paper should explicitly state the approximate smoothness parameter $\eta$ obtained in [2] and how the current work's expansiveness parameter relates to it. A more detailed comparison of the assumptions made in this work and those in [1,2] is needed to fully understand the novelty of the approach. The paper should clarify whether the approximate smoothness parameter $\eta$ in [2] is dependent on the sample size $n$, and if not, this should be explicitly stated to justify why the bounds in [2] do not vanish with increasing $n$.



### Questions
- Some small typos: 
	- Line 190: pernutation -> permutation
	- Line 267: exist -> exists
	- Line 483: It then curious -> It is then curious

- How does the bound in [1,2] change when considering $\text{tahn}_{\gamma}$-PGD?
- Have you tried larger $\gamma$s? $\gamma = 10^{5}$ seems to be very far from sign-PGD in Figure 2 (b).  It would be interesting to see how does $\text{tahn}_{\gamma}$-PGD behave when it’s close to sign-PGD.
- Can you construct an experiment where the dependence on $n$ is displayed? For example taking a smaller number of samples from the studied datasets in order to see how the generalization gap grows. A synthetic distribution could also be employed where more and more samples are drawn and the gap decreases to zero for finite $\gamma$.

**References:**

[1] Wang et al., Data-dependent stability analysis of adversarial training, ArXiv 2024.

[2] Xiao et al., Stability Analysis and Generalization Bounds of Adversarial Training, NeurIPS 2022

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies generalization bounds for robust training by leveraging the framework of uniform stability. The authors analyze $\ell_\infty$ perturbations and derive several upper bounds on the generalization gap of predictors. They then investigate experimentally the performance of adversarially trained models using several algorithms to solve the inner maximization problem of the robust objective.

### Strengths
The paper studies an interesting problem: the large generalization gap of robust empirical risk minimization (adversarial training) in neural networks. This work leverages the framework of uniform stability, which has been rather unexplored in the robust learning community, and could potentially provide insights on this topic. Based on the theoretical analyses, the authors propose a sensible relaxation of the commonly used PGD attack, using the $tanh$ function instead. Finally, I agree with the authors that the optimization algorithm in the inner maximization problem has not received adequate attention in the literature, and thus, its study is welcome (despite its limitations—see below).

### Weaknesses
The paper is unfortunately difficult to follow, making it challenging to assess its content due to presentation issues. Furthermore, the conclusions seem unoriginal to me. In particular, I identified the following weaknesses:

- Poor presentation: There are many instances where the text is not polished, with numerous grammatical errors (see the non-comprehensive list at the end of the Weaknesses). Additionally, the presentation of the technical results could be substantially improved (e.g., Theorem 4.1: remind the reader of the constants $\beta, \Gamma_X$). Furthermore, the authors should mention in the introduction that all of their results are solely about $\ell_\infty$ perturbations.
- Introduction of many ad-hoc terms to denote well-established concepts: In many places, the authors use obscure words to define concepts that are well-defined in learning theory. For instance, lines 258-259: "mis-matched generalization gap" — this is just the standard generalization gap of a predictor trained robustly. Several such choices make it difficult for readers to comprehend the contributions of this work. Similarly, with so-called "RG-PGD" and the "expansiveness property" (a relaxed notion of Lipschitz continuity).
- Unclear contributions: The paper does not clearly describe how the derived bounds differ from those of Xiao et al. (2022b) and Wang et al. (2024). In particular, the bounds from these prior works are not presented, and they are solely critiqued on the basis that they do not vanish with increasing sample size. Furthermore, the criticism of the non-smoothness of the loss function adopted in prior work seems unfounded ("The source of the non-smoothness is, however, not explained in their work"). Even for linear models under $\ell_\infty$ perturbations, a cross-entropy loss is non-smooth. Hence, the property of non-smoothness is well-motivated.
- Unclear motivation for experiments: The authors seem to identify the sign function in the solution of the inner maximization problem in the robust objective as problematic, and they suggest an alternative based on a smooth approximation. However, they do not show any benefits in terms of robustness with the new method. Furthermore, the fact that for small $\gamma$ we do not observe overfitting and the generalization gap is small appears to be a trivial observation, as the evaluation basically approaches the standard case of no perturbations. In short, it is not a good method for finding worst-case $\ell_\infty$ perturbations.
- Results of Section 6: The authors mention the connection between adversarial training and steepest descent methods, but it is clear that this has been the motivation for the iterative solution of the inner maximization problem since the introduction of adversarial training. Furthermore, the experiments fail to highlight anything new, in my understanding (basically optimising an $\ell_\infty$ objective yields better coverage against $\ell_\infty$ attacks).

Grammatical errors (non comprehensive list):
- in the abstract: "These expansiveness parameters appear not only govern the vanishing rate of the generalization error but also govern its scaling constant."
- line 190: "perturnation" -> perturbation
- line 202: "related with" -> related to
- line 241: "draw" -> draws
- line 245, 256: "descend" -> descent
- line 316: "independent with" -> independent of
- lines 536-537: "Like all up-bound based theoretical results, such an approach is adequate for understanding performance guarantees but may be inadequte to explain poor generalization."

### Questions
- Which part of the analysis bypasses prior work and makes the bounds decay as $O(\frac{1}{n})$?
- In the experiments of Section 6, why do you change the threat model (finding different values of $\lambda_p$)? One could imagine experiments with different steepest descent algorithms for the solution of the inner maximization problem, where the threat model does not change (i.e., projecting every time to the same $\ell_\infty$ balls around the original points). Of course, different steepest ascent algorithms (besides the commonly used sign gradient ascent) will perform worse in finding adversarial examples, so the number of inner iterations should be adjusted appropriately. However, I believe this could be an interesting experiment to conduct.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the algorithmic stability of adversarial training with a focus on how the inaccuracy of PGD attack affects the stability. Theoretical analysis are provided to justify that the sign function in PGD updates can significantly harm the stability, leading to a worse generalization (gap).

### Strengths
(1) This paper is clear and easy to understand.

(2) This paper studies the algorithmic stability of adversarial training from an interesting angle of the PGD attack.

(3) Experiments demonstrate that using tanh to replace sign function can improve the generalization performance.

### Weaknesses
 (1) While the paper considers the algorithmic stability of PGD attack, a missing component is the convergence of PGD attack. Intuitively, if we always use a fixed attack direction, then the algorithmic stability is not largely affected by the attack. However, the attack is not efficient. When using PGD attack, there is supposed to have a trade-off: with more iterations, the stability gets worse, but the attack becomes stronger. If at the test stage the attacker uses a very strong attack, e.g., AA attack, then balancing the attack effectiveness and stability is essential to obtain a better robust testing performance. Could the authors elaborate more from this perspective?

(2) Please highlight the technical challenges for the theoretical contributions in this paper.

(3) Please consider using some SOTA methods from RobustBench, e.g., leveraging synthetic data in adv training, to conduct the experiments. While improving the sign function seems to be helpful as illustrated by this paper, there is no enough evidence to demonstrate that this is one of the key issues in adversarial training.

(4) Minor: In one line of research, to save the computation budget of adversarial training, algorithms have been proposed to explore fast adversarial training: instead of calculating the attack at each iteration, they update the attack for each sample for one step at each iteration, e.g., 

Cheng, Xiwei, Kexin Fu, and Farzan Farnia. "Stability and Generalization in Free Adversarial Training." arXiv preprint arXiv:2404.08980 (2024).

I'm wondering if the authors can provide some comments on algorithms of this type.

### Questions
Please address my comments above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper provides a new stability bound for adversarial training, where the inner maximization perturbation $J$ and the evaluation perturbation $\pi$ can be different. The introduced term expansiveness can partly explain robust overfitting and experiments are conducted to validate the theoretical results.

### Strengths
- The new stability theory differs from existing ones in terms of assumptions and the form of bounds. I like the separation of adversarial training perturbation $J$ and the evaluation perturbation $\pi$, which means that the theory in this paper is a more abstract framework and can be applied in many cases.
- The writing is good.

### Weaknesses
 - It seems that the framework in this paper can not provide a proper description for the $Q(c^*)$ term, we need to calculate it according to the concrete choice of $J, \pi$. However, to make this framework more significant, examples of how to calculate $Q(c^*)$ and how to choose $c^*$ should be added. Note: I mean examples in practice but not examples with overly simple assumptions (such as the assumption on the second moment in lines 293-294 and the assumption in Corollary 5.2 that a term is bounded by $B$ with probability 1). Just like the VC dimension, if we can not calculate the VC dimension of some hypothesis classes, the bound with the VC dimension is meaningless.
- Typo: in line 149, it should be "the label space $\mathcal{Y}$ is finite"
- A minor issue: many equations in this paper are numbered, in fact, the equations that are not used later need not be numbered. For example, equation (2) is not used.
- In lines 87-88, the paper says that "the bound convergence to a constant, this helps explain the robust overfitting phenomenon". In fact, a lower bound of the generalization gap that converges to a constant can explain overfitting. However, an upper bound can not because your bound may not be tight enough.

### Questions
In total, I think this is a good paper, but there are some points that can improve this paper. Please refer to the weaknesses part.

### Soundness
3

### Presentation
3

### Contribution
3
