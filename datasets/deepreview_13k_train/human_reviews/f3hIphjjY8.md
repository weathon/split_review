# $d$-Linear Generation Error Bound for Distributed Diffusion Models

- Decision: Reject
- Scores: 5, 3, 3

## Abstract
The recent rise of distributed diffusion models has been driven by the explosive growth of data and the increasing demand for data generation. However, distributed diffusion models face unique challenges in resource-constrained environments. Existing approaches lack theoretical support, particularly with respect to generation error in such settings. In this paper, we are the first to derive the generation error bound for distributed diffusion models with arbitrary pruning, not assuming perfect score approximation. By analyzing the convergence of the score estimation model trained with arbitrary pruning in a distributed manner, we highlight the impact of complex factors such as model evolution dynamics and arbitrary pruning on the generation performance. This theoretical generation error bound is linear in the data dimension $d$, aligning with state-of-the-art results in the single-worker paradigm.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the iteration complexity of sampling from a diffusion model in the distributed setting. It shows an $O(d)$ bound, which matches the performance in the single-worker setting. The main contribution is a careful analysis of the discrepancy between the distributed optimization of the score matching objective, and the analogous optimization in the serial setting, and the effect of this discrepancy on the final sampling error. It essentially shows that using Q = poly(1/$\varepsilon$) rounds of distributed training suffice to achieve this bound, where $\varepsilon$ is the parameter controlling the final sampling TV error.

### Strengths
This is a very interesting paper that proposes a new setting for theoretical analysis of diffusion models. The bound shown matches the best known bound in the serial worker setting. Moreover, I believe that this paper could open the door to other analyses in the distributed setting that could lead to practical impact. Overall, I appreciate the creativity here.

### Weaknesses
Despite the nice technical contributions, this paper was extremely painful to read. The theorem statements and corollaries are very difficult to parse, and the writing in general is convoluted and unclear. I encourage the authors to consider rewriting the main text of the paper, and to focus on explaining the core intuition crisply. I also recommend significantly simplifying the theorem statements. The paper lacks a clear explanation of its novelty, particularly in relation to existing work on distributed diffusion models. Specifically, the connection and distinction from results such as (Zhou et al, 2024) are not clearly articulated, making it difficult to assess the significance of the contributions. The current presentation makes it challenging to understand the precise technical challenges addressed and the specific innovations introduced to overcome them. The lack of clarity extends to the experimental setup and results, making it difficult to reproduce or validate the claims.

### Questions
- Can you get a bound better than O(d) if you make the assumption that the score is Lipschitz?
- Does your work have any direct practical implications?
- What open problems does your work expose?

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a theoretical framework for distributed diffusion models, specifically focusing on deriving a theoretical error bound for model generation in resource-constrained settings. The authors extend the analysis of score estimation convergence under arbitrary pruning and introduce a theoretical generation error bound that scales linearly with data dimension $d$. The contributions include assessing the convergence of the score estimation model and error propagation in a distributed system with arbitrary pruning.

### Strengths
1. The paper's theoretical analysis highlights the performance of distributed diffusion models under resource limitations such as arbitrary pruning, which is valuable for real-world applications.

2. The derived error bounds align with existing single-worker setup, demonstrating the validity and potential applicability of the proposed framework in distributed settings.

3. It aligns with recent advances in federated diffusion and distributed learning by considering score estimation dynamics, bridging gaps in understanding error bounds across distributed workers.

### Weaknesses
1. **Incremental Contribution:** While the theoretical contributions in the distrusted diffusion models are noteworthy, the paper's essence is to solve a federated learning problem. This approach appears to be incremental when compared to prior works such as Zhou et al. 2024, Benton et al. 2024. See questions below for more details. Specifically, the paper does not adequately address the limitations of existing federated learning approaches when applied to diffusion models, such as the challenges of heterogeneous data distributions and the impact of client drift on the convergence of the score estimation model. The analysis seems to focus on a simplified scenario that does not fully capture the complexities of real-world federated settings.

2. **No Empirical Validation:** The paper lacks empirical results that validate the theoretical error bound derived for distributed diffusion models. Experiments demonstrating the practical impact of pruning and convergence rates in resource-constrained environments would strengthen the claims. The absence of empirical validation makes it difficult to assess the practical relevance and applicability of the theoretical findings. For example, it would be beneficial to see how the derived error bounds translate to actual image generation quality under different pruning levels and distributed training configurations.

3. **Clarity and Accessibility:** The proof in this paper is not self-contained as it lacks some explanations and leaves the gap to the readers. Specifically, the derivation of equation (25) from (24) is not clearly explained, particularly the transition of the double summation term. The reader is left to fill in the gaps, which hinders the accessibility and reproducibility of the theoretical results.

### Questions
1. While the paper includes some comparisons with prior works in the proofs, it does not clearly differentiate its contributions or demonstrate substantial advancements beyond what was previously established. Can the authors provide a clear explanation of the fundamental technical novelty and methodology, especially in comparison to works such as [Zhou et al., 2024; Benton et al., 2024]? Specifically, it would be helpful to understand what unique aspects this work introduces in terms of theoretical framework or analysis techniques that set it apart from these prior results.

2. Could the authors elaborate on how summing (24) around L.811 leads to (25)?

3. The proof of Corollary 2 in Appendix E is not self-contained because the authors rely largely on Theorem 1 in the work [Benton et al. 2024]. Would you please provide a step-by-step explanation of how to adapt Theorem 1 from Benton et al. 2024 to fit this distributed setting, and highlight any required modifications or additional assumptions?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studied the distributed learning problem on diffusion models, where each agent performs multiple local updates on a sparsified diffusion model using sparsified gradients. A convergence analysis is provided.

### Strengths
- The proof sketch is well-presented.

### Weaknesses
 - For clarity, please denote equation numbers for important equations such as those in the Theorem, Corollary and Proof Sketch.
- Also for clarity, I suggest denoting $B_1, B_2, B_3, B_4, B_5$ with their corresponding iteration counter, e.g., $B_{1}^{(q)}$.
- (**Experiment**) This paper lacks a numerical experiment to show the effectiveness of distributed diffusion model training using only sparse local updates, which will help identify the contribution of the proposed theorem.
- (**Theoretical Contribution**) I agree with the authors that the relaxed assumption of this paper improves the theoretical results of [Benton et al., 2024]. However, since the convergence of federated local sparse training is already established in [Zhou et al, 2024] and is orthogonal to the diffusional model aspect, the combination of two techniques makes the contribution of this paper a bit ambiguous. 
- (**Low Practical Contribution**) Unless the authors can point out additional algorithmic design on training diffusion models using (7) as a contribution beyond the classification task as illustrated in [Zhou et al, 2024], the analysis in this paper will not impact the community in advancing distributed diffusion model training.

### Questions
- Using the upper bound $B_3 = \mathcal{O}(\eta^2 \sum_{p=0}^{q-1} \\| \theta_{p+1} - \theta_p \\|^2 + \eta^2 \\| \theta_0 \\|^2 + \eta^4 + \eta^4 \\| \nabla F(\theta_q) \\|^2 )$ from line 428, summing $B_3$ from $q= 0$ to $q= Q-1$ and applying the inequalities from line 350, 357 will give us
$$\frac{1}{Q}\sum_{q=0}^{Q-1} \mathbb{E}[ \\| \nabla F(\theta_q) \\|^2 ] = \tilde{\mathcal{O}}(\mathbb{E}\\| \theta_0 \\|^2)$$
which is different from the $\tilde{\mathcal{O}}(\frac{1}{\eta^2 Q^2}\mathbb{E}\\| \theta_0 \\|^2)$ dependence as claimed in Theorem 1. (I use the notation $\tilde{\mathcal{O}}$ to hide the dependence on other error terms.)
For instance, may I ask for clarification on how does the $\mathcal{O}(\eta Q \mathbb{E}[\\| \theta_0 \\|^2])$ dependence in line 857 reduce to $\mathcal{O}(\frac{1}{\eta Q}\mathbb{E}[\\| \theta_0 \\|^2])$ in line 863.

### Soundness
2

### Presentation
3

### Contribution
1
