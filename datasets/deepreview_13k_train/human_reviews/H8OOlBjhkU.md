# Optimization over Sparse Restricted Convex Sets via Two Steps Projection

- Decision: Reject
- Scores: 3, 3, 6, 8

## Abstract
In sparse optimization,  enforcing hard constraints using the $\ell_0$ pseudo-norm offers advantages like controlled sparsity compared to convex relaxations. However, many real-world applications (e.g., portfolio optimization) demand not only sparsity constraints but also some extra constraint (such as limit of budget). While prior algorithms have been developed to address this complex scenario with mixed combinatorial and convex constraints, they typically require the closed form projection onto the mixed constraints which might not exist, and/or only provide local guarantees of convergence which is different from the global guarantees commonly sought in sparse optimization. To fill this gap, in this paper, we study the problem of sparse optimization with extra $\textit{restricted convex}$ constraints commonly encountered in the literature. We present a new variant of iterative hard-thresholding algorithm equipped with a two-step consecutive projection operator customized for these mixed constraints,  serving as a simple alternative to the Euclidean projection onto the mixed constraint. By introducing a novel trade-off between sparsity relaxation and sub-optimality, we provide global guarantees in objective value for the output of our algorithm, in the deterministic, stochastic, and zeroth-order settings, under the conventional restricted strong-convexity/smoothness assumptions.  As a fundamental contribution in  proof techniques, we develop a novel extension of the classic three-point lemma to the considered two-step non-convex projection operator, which allows us to analyze the convergence in objective value in an elegant way that has not been possible with existing techniques. Finally, we illustrate the applicability of our method on several sparse learning tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript investigated a constrained optimization setting where the goal is to minimize an objective function while satisfying some sparsity constraints. A two-step-projected gradient-based approach is proposed. Their performance is analyzed for both stochastic and non-stochastic settings.

### Strengths
Understanding optimization with sparsity constraint is a long-standing open question. This submission is one of not many works that formulates and provides analysis towards that direction.

### Weaknesses
Technically, there are hidden constraints to the main results that could significantly limit the strength of the proposed results. For example, Theorem 1 and the remarks that follow imply that the proposed two-step projection guarantees the convergence to the global minimum if the minimizer is sparse, which is not true in the most generic case (e.g., when k=1). However, the proof was made possible due to the requirement of $k\geq \frac{4(1-\rho)^2 L_s^2}{\rho^2 \nu_s^2} \overline{k}$, which in fact requires the sparsity constrain has to be weak, i.e., lower bounded by the square of the condition number for the non-trivial case of $\overline{k}\neq 0$. So, no guarantee is provided for the important case of fixed sparsity $k$, even if we allow k to be an arbitrarily large constant. 

Some other minor comments and suggestions:

1. The main results are rather hard to read due to the fact that many needed notations are defined informally inline in different sections, for example, H_k in Theorem 1. Possible ways of improvement include either defining the notations formally in a definition environment or naming the notation so they can be easily searched. 

2. Interpretation of  $\rho$ in the main result: We are generally interested in the achievable result of $R(w_t)$ and the inequality presented in Theorem 1 seems to be a more intermediate result where the role of parameter $\rho$ could be unclear to the readers. For readability, the reviewer suggests that Remarks 3 and 4 should be summarized as a main theorem, then Theorem 1 is presented as a technical result for proving them.

### Questions
As the presented theorem requires a sparsity constraint k that grows unbounded with respect to the condition number. Would it be possible to modify the analysis or the algorithm to extend the results for any large constant k?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies rate of convergence of Iterative Hard Thresholding (IHT) on sparse regression with extra constraints on regression coefficients.

### Strengths
This paper studies rate of convergence of Iterative Hard Thresholding (IHT) on sparse regression with extra constraints on regression coefficients.

### Weaknesses
The work is very much similar to literature (Jain et al., 2014; Nguyen et al., 2017; Li et al., 2016; Shen & Li, 2017; de Vazelhes et al., 2022). The referee is afraid that adding an extra constraint \Gamma of the regression coefficients making any fundamental difference. More importantly, it does not make much sense to enforce an extra constraint \Gamma. The solution only converges to stationary points. And the authors never verify the assumptions with a practical example.

### Questions
The work is very much similar to literature (Jain et al., 2014; Nguyen et al., 2017; Li et al., 2016; Shen & Li, 2017; de Vazelhes et al., 2022). The referee is afraid that adding an extra constraint \Gamma of the regression coefficients making any fundamental difference. More importantly, it does not make much sense to enforce an extra constraint \Gamma. The solution only converges to stationary points. And the authors never verify the assumptions with a practical example.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies sparse optimizations problems where the underlying constraints consist of the intersection of an $\ell_0$ constraint and an extra constraint $\Gamma$. The authors introduce a IHT algorithm for optimizing over such sets, which uses a novel two step projection (TSP) procedure. By deriving an extension of the three point lemma for this setting, convergence guarantees are derived for this algorithm, assuming the objective satisfies the RSC and RSS conditions. The algorithm is extended to the stochastic and zeroth order settings where similar guarantees are derived.

### Strengths
1. The paper is written well overall, with a clear state-of-art, problem description, notation, and exposition.


2. The proposed TSP operator  is novel in my view, and also very natural.  The extension of the three point lemma derived in this paper is interesting, and is the main technical tool for obtaining the convergence guarantees.


3. The convergence results are interesting and I think these would be of interest to those working in the areas of sparse signal recovery.

### Weaknesses
1. At present there is no proof outline, which makes it difficult to understand the novelty in the proof technique compared to the literature. I understand there is a space constraint, but given that the main contributions of the paper are theoretical, this is relevant.

2. In the experiments, there is currently no comparison with existing methods. I think this would have been nice to illustrate on synthetic data, and would also provide an empirical validation of the theoretical results.

3. I think the statement of assumption 3 is currently written in the form of a definition.

4. In Remark 1, the fourth bullet should ideally be the second bullet, just to introduce the notion of convex symmetric sets first.

5. In Algorithm 2, I am a bit confused about the notation $\mathcal{S}$. Shouldn't the index set $\mathcal{S}_t$ be a subset of $[n]$? Also in the summation index, it should be $i_t$ instead of $i$?

6. The convergence results pertain to the objective value, but can something be said for the convergence of the iterates to the global minimum? (provided there is a unique global minimum of course)

### Questions
I have the following minor remarks\questions.

1. I think the statement of assumption 3 is currently written in the form of a definition.

2. In Remark 1, the fourth bullet should ideally be the second bullet, just to introduce the notion of convex symmetric sets first.

3. In Algorithm 2, I am a bit confused about the notation $\mathcal{S}$. Shouldn't the index set $\mathcal{S}_t$ be a subset of $[n]$? Also in the summation index, it should be $i_t$ instead of $i$?

4. The convergence results pertain to the objective value, but can something be said for the convergence of the iterates to the global minimum? (provided there is a unique global minimum of course)

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
Due to a medical emergency, I am unable to assess this article.

### Strengths
N/A

### Weaknesses
N/A

### Questions
N/A

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
