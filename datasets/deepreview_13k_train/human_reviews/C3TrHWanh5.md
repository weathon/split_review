# Efficient and Generalizable Second-Order Certified Unlearning: A Hessian-Free Online Model Updates Approach

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Machine unlearning strives to uphold the data owners' right to be forgotten by enabling models to selectively forget specific data. 
Recent advances suggest pre-computing and storing statistics extracted from second-order information and implementing unlearning through Newton-style updates.
However, the Hessian matrix operations are extremely costly and previous works conduct unlearning for empirical risk minimizer with the convexity assumption, precluding their applicability to high-dimensional over-parameterized models and the nonconvergence condition.
In this paper, we propose an efficient Hessian-free unlearning approach. 
The key idea is to maintain a statistical vector for each training data, computed through affine stochastic recursion of the difference between the retrained and learned models. 
We prove that our proposed method outperforms the state-of-the-art methods in terms of the unlearning and generalization guarantees, the deletion capacity, and the time/storage complexity, under the same regularity conditions.
Through the strategy of recollecting statistics for removing data, we develop an online unlearning algorithm that achieves near-instantaneous data removal, as it requires only vector addition.
Experiments demonstrate that our proposed scheme surpasses existing results by orders of magnitude in terms of time/storage costs with millisecond-level unlearning execution, while also enhancing test accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the challenge of certified unlearning, where models are required to forget information at the request of data providers. The authors introduce a novel approach leveraging details tracked during model training to approximate how the training process would have proceeded without the data marked for deletion. Notably, the proposed method circumvents the need for full Hessian computations or inversion by using Hessian-vector products for second-order information. Additionally, it does not assume that the original model is an empirical risk minimizer. The authors' theoretical analysis argues that their method offers enhanced unlearning guarantees, efficient storage and precomputation, faster data deletion, and improved generalization bound, particularly for overparameterized models. Empirical results support the approach's claim of rapid unlearning execution.

### Strengths
1. The idea of tracking algorithmic updates during training to facilitate unlearning is straightforward yet impactful, with sound theoretical analysis for unlearning privacy guarantee and descent empirical evaluation.
2. Removing the assumption that the initial learned model must be an empirical risk minimizer is significant for the practical applicability of the method.
3. The claimed efficiency improvements are particularly relevant for overparameterized deep models where the batch size is comparable to the number of training epochs, probably covering a substantial portion of common machine learning models.

### Weaknesses
1) The claim regarding the efficiency of precomputation and storage (lines 378–387) hinges on two critical assumptions: (i) the model's parameter size $d$ is significantly greater than the training data size $n$, and (ii) the number of epochs $E$ is of the same order as the batch size $|B|$. While the authors state (ii) as typical ("Typically, $E$ and $|B|$ are of the same order"), a reference would strengthen this claim. Moreover, the assumption may not hold in scenarios such as online learning or streaming applications. Qualifying its generality and highlighting this as an assumption similar to Line 299 would be beneficial and avoid misleading readers.

2) The generalization analysis in Section 4.2 considers strong convex loss functions and focuses on excess risk bound. Excess risk bound consist of two terms: the first term comes from (a) the excess risk of the empirical risk minimizer, and the second term comes from (b) unlearning error, (c) optimization error, and (d) the noise for obfuscation (Line 14 of Algorithm 1). There are at least two problems with this analysis and theorem statement.

2.1 In strong convex settings, the assumption that $E$ and $|B|$ are comparable can seem more questionable, especially as the excess risk bound expressed in big-O notations (Line 319) uses this assumption. It might be okay to make this assumption for controlling (b), but $E$ and $B$ also affects (c), i.e. whether the term $C_4$ in Equation 74 is small enough, which conceptually (roughly) translates to whether $w_{E, B}$ is a good empirical minimizer or not. It seems problematic to assert that the number of epoch required for convergence to empirical risk minimizer is the same order of magnitude as batch size. 

2.2 The first term comes from Lemma 9, which cites Shalev-Shwartz et al. (2009). The latter assumes i.i.d. of samples, which should translate to i.i.d. of the set $U$.

### Questions
1. In the abstract (Line 017) and introduction (Line 073), the authors claim that previous work requires strong convexity, while in Line 66 the authors said previous work requires convexity. It seems to me that convexity suffices in Sekhari et al. (2021) because unlearning for a convex loss function can be reduced to a problem with strong convex loss. Could the authors clarify what assumptions are needed in previous work? 
2. In Assumption 1 (Line 299), is the loss assumed to be jointly convex in both $z$ and $w$, only $w$, or only $z$? Similar questions for Lipschitzness and smoothness.

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
The paper proposes a new unlearning algorithm which extracts second-order information in a Hessian-free manner without the need to assume strong convexity. The key idea is to track and remove the impact of a specific sample in the entire update trajectory of the model, which is called affine stochastic recursion between the retrained and learned models in this work. It provides theoretical guarantees on generalization, deletion capacity, and space/time complexities. Experiments are conducted to demonstrate the superiority of the proposed algorithm.

### Strengths
Strengths include:
1) The paper proposes affine stochastic recursion to pinpoint the overall impact of a specific sample on the learned model.
2) It makes the unlearning process efficient via the Hessian-free computation.
3) It provides theoretical guarantees that cover generalization, deletion capacity, and space/time complexities. 
4) Experiments are provided to demonstrate the advantages of the proposed unlearning algorithm.

### Weaknesses
Weaknesses include:
1) The recollection matrix M looks incorrect, based on the derivation given in Appendix C.1. The recursive formulation in the appendix seems to imply that the product of (I - ηH) terms should accumulate from the most recent update *backwards* to the update where the deleted sample was used. However, the matrix M as presented appears to multiply these terms in the opposite direction, which would not correctly capture the influence of the deleted sample across the optimization trajectory.
2) Limitations of the algorithms are not discussed. For example, the proposed algorithm may not perform well on large-scale datasets given the quadratic time complexity in data size. Furthermore, the practical memory requirements for storing the recollection matrix M, especially for long training trajectories and large models, are not addressed. This could be a significant bottleneck in real-world applications.

### Questions
1) Could you explain why NS and IJ can't utilize HVP? Although they involve Hessian inverse, it could be approximated by using like least-square which essentially does HVP as well. 
2) Regarding the correlation metric on loss change, could you tell us what stopping rule you use while calculating those loss changes across different algorithms? I feel this is important for gauging performance.
3) It is unclear whether fine-tuning was used for each of the algorithms in experiments.

### Soundness
2

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
This paper proposes a Hessian-free approach to certified machine unlearning that aims to improve computational efficiency and scalability in removing specific data points from a model without full retraining. Instead of relying on direct Hessian computations, which are computationally prohibitive in high-dimensional and non-convex settings, the method approximates the impact of data removal through affine stochastic recursions that analyze model update discrepancies. The method achieves computational gains, reducing unlearning time to $\mathcal{O}(md)$ and storage to $\mathcal{O}(nd)$, outperforming existing second-order methods.

### Strengths
- Both online learning and certified unlearning are highly significant research areas in machine learning.
 The paper is the first to introduce a Hessian-free approach to certified unlearning, which is a notable change from the dominant reliance on Hessian-based methods in second-order unlearning.

- Experimental validation shows unlearning runtime in milliseconds, robust generalization guarantees, and privacy improvements against membership inference attacks with an added noise mechanism.

- The authors also include relevant code and pseudo-code in the appendix, which is helpful for reproducibility.

### Weaknesses
1. The paper’s theoretical guarantees hinge on assumptions of convexity and smoothness (Assumption 1), which restricts the scope of the analysis to settings that are arguably idealized for real-world applications involving non-convex (e.g. deep learning) models. Thus, the authors likely overstate their contributions.

2. I would say, Hessian-free optimization for second-order (and even higher-order) algorithms is an active research area. Beyond the Machine Unlearning domain discussed in detail on page 3 and in Appendix A, the authors should connect the ideas presented here with a broader body of Hessian-free optimization work in classical parametric optimization. A numerical comparison, if feasible, is also encouraged, as this may better highlight the novelty of this paper’s contributions beyond merely applying existing Hessian-free methods to the Machine Unlearning field.

3. While the authors present some experimental results, they lack diversity in dataset selection and only test the approach on ~5 datasets. The efficacy of this unlearning mechanism remains unclear in large-scale or high-dimensional applications where computational efficiency is critical.


4. The writing quality of this work is limited and the presentation should be improved, for instance

- the (2) is simply one case of (1) by replacing the $\mathcal{D}$ with empirical distribution. i.e., the authors could remove (2) for simplicity, or just start from the (1)

- I think the (3) should be written as $\mathbf{w}_{e, b+1} \leftarrow \mathbf{w}_{e, b}-\eta_{e, b} \sum_{i \in \mathcal{B}_{e, b}} \nabla \ell(\mathbf{w}_{e, b} ; z_i),$ since the linear scaling rule (Goyal et al. 2017) is introduced later in line 163.

- line 156 and algo. 1: as your notation, the total epochs and batches would be $E+1$ and $B+1$. So as your complexity in section 4.4

- when removing the $u_j$, why the normalization constant of $\eta$ in your (5) is $ \mathcal{B}_{e, b(u_j)}$ instead of $ \mathcal{B}_{e, b(u_j)}-1$?

- definition 1: how can you ask a learning algorithm within the (solution) parameter space $\mathcal{W}$? Please revise the definition or rephrase your wording

- in your lemma 2, I don't think there exists a valid $G$ such that $G=\max \left\|\nabla \ell\left(\mathbf{w}_{e, b} ; z\right)\right\|<\infty$. This should be a consequence of the assumption that the grad of $l$ is uniformly upper bounded. Otherwise, this could be derived by your assumption 1, which is imposed later

- Theorem 4 should be $B=\left\lceil \frac{n}{\mathcal{B}} \right\rceil$

- if the intent is for the product to go in reverse order in line 10 of algo. 1, i.e. $\prod_{k=E}^e \prod_{b=B-1}^{b(u)+1}$, the notation should ideally be clarified in the text to avoid misunderstandings

- font size in figures e.g., 1, 2, 7, is too small and needs to be enlarged for clarity

- figure 4 caption: "a comparison comparison between"

### Questions
Please refer to weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a Hessian-free machine unlearning algorithm. The authors theoretically analyze the approximation error for both convex and non-convex loss functions and prove the generalization theory for strongly convex loss functions. Extensive experiments demonstrate the efficiency of the proposed algorithm compared to other Hessian-based algorithms.

### Strengths
1. The authors analyze the training trajectory and propose a machine unlearning algorithm, which is practical and innovative.
2. Compared to other Hessian-based algorithms, the proposed Hessian-free algorithm is efficient, especially for high-dimensional problems.
3. The authors conducted comprehensive experiments to validate the effectiveness of their proposed algorithm, and the experimental results are well presented.

### Weaknesses
Although the authors provide the approximation error analysis, there is no theoretical guarantee for the generalization performance of the unlearning model in the non-convex case.

### Questions
1. The authors propose using HVP to avoid directly calculating the Hessian matrix and reduce computational complexity, as discussed in Section 4.4. Could other algorithms discussed in Section 4.4 also benefit from HVP? For example, for IJ, $H^{-1}\nabla \ell $ can be approximately computed using $K$ steps of the conjugate gradient method, where each step HVP can be applied. Could this approach enable IJ to achieve lower complexity and experiment time, considering the entire process of precomputation and unlearning?  In this case, how does the proposed algorithm compare to IJ?
2. The authors discuss in Appendix E that a small step size leads to a smaller approximation error. However, a small step size may result in insufficient model training. Could the authors further explain the trade-off?

### Soundness
3

### Presentation
3

### Contribution
3
