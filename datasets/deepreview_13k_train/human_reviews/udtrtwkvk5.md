# Subspace Optimiztion for Large Language Models with Convergence Guarantees

- Decision: Reject
- Scores: 6, 6, 3, 6

## Abstract
Subspace optimization algorithms, with GaLore (Zhao et al., 2024) as a representative method, have gained popularity for pre-training or fine-tuning large language models (LLMs) due to their memory efficiency. However, their convergence guarantees remain unclear, particularly in stochastic settings. In this paper, we unexpectedly discover that GaLore does not always converge to the optimal solution and substantiate this finding with an explicit counterexample. We then investigate the conditions under which GaLore can achieve convergence, demonstrating that it does so either in deterministic scenarios or when using a sufficiently large mini-batch size. More significantly, we introduce **GoLore** (**G**radient rand**o**m **Lo**w-**r**ank proj**e**ction), a novel variant of GaLore that provably converges in stochastic settings, even with standard batch sizes. Our convergence analysis can be readily extended to other sparse subspace optimization algorithms. Finally, we conduct numerical experiments to validate our theoretical results and empirically explore the proposed mechanisms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates subspace optimization approaches for LLM pre-training and fine-tuning. The authors demonstrate that GaLore fails to converge to the desired solution under regular assumptions, as the SVD-based projection often generates noise-dominated subspaces when the true gradient is relatively small. Furthermore, the authors introduce a variant of GaLore - GoLore, and establish its convergence rate even with small-batch stochastic gradients. A limitation of this paper is that convergence guarantees for GoLore are currently provided only when using MSGD as the subspace optimizer.

### Strengths
1. The paper is logically structured and written in clear, accessible language.
2. The theorems presented are robust and well-supported.

### Weaknesses
1. The empirical advantages of GoLore appear marginal. Is the inability of GaLore to converge common in real-world scenarios?
2. The experiments only compare GoLore with GaLore. Do other memory-efficient fine-tuning algorithms also struggle with convergence? If not, what advantages does GoLore offer over these alternatives?
3. It is surprising that selecting components of the gradient matrix randomly provides better convergence guarantees than selecting the most informative components using SVD. A more intuitive explanation of this phenomenon would be beneficial. Additionally, since GoLore does not require SVD decomposition, does it run faster than GaLore?

### Questions
Please refer to the Weaknesses.

### Soundness
2

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
4

### Summary
The paper investigates into the convergence behaviour of GaLore and finds that GaLore only converges when their is no gradient noise or the batch size is large enough such that the gradient noise is small. For the stochastic setting without large batch, the paper provides one counter example where GaLore fails to converge. To address the issue of non-convergence, the paper proposes to use GoLore that replaces the projection matrix in GaLore with random matrices. Convergence analysis as well as experiments on language models are provided to support the effectiveness of the proposed GoLore algorithm.

### Strengths
Training language model requires large amount of resources. The research on efficient and cheaper algorithms for pretraining and fine-tuning language models is thus important and valuable to the entire community. Previous works that propose efficient methods like LoRA and GaLore focus on empirical performance, while this work aims at building theoretical foundations on the convergence analysis of GaLore. The theoretical results then guide the design of a new algorithm, GoLare. This paper is well written and clear, providing novel and important insights on a trendy and significant area on memory efficient methods for training language models.

### Weaknesses
1. There is a typo in the title. It should be optimization instead of optimiztion. At first impression, I feel the paper lacks careful proofreading and attention to detail. Given that most results are theoretical, I also have reasonable questions towards the overall quality and rigor of the work. Therefore, I recommend the authors to carefully reviewing the paper. Other typos: line 198 effiicent, line 347 large-batch is the same as stochastic. Other minor suggestions: (1) pre-training and pretraining are used interchangeably. It is better to be consistent. (2) I was very confused when first reading Figure 1. It might be good to at least explain what is the loss, MSGD, L.B., @50%, etc., in Figure 1's title. (3) line 335-338 and line 344-347 in Algorithm 1 are exactly the same. There is no need to repeat twice. It saves space to move these three lines outside the if-else block, e.g., $G\leftarrow$..., if ... then SVD ... else $P^t\leftarrow P^{t-1}$... end if. (4) I guess that the second moments $V$ in Algorithm 1 can also be implemented with projection in the same way as MP. Why not also consider it?

2. The theoretical results suggest that GaLore converges with large batch size while fails for the stochastic case. It is not clear how large this batch size should be. Theorem 3 only provides one case where batch size $B\sim\sqrt{T}$. What happens for other batch size? Would anything smaller lead to non-convergence? Theorem 1 is also not clear in this sense. The non-convergence happens when $B=1$. What happens for other choice of batch size? The specific question is that is there any condition, threshold, or phase transition for $B$ such that anything smaller leads to divergence and anything larger leads to convergence. The current large batch v.s. stochastic setting is not super clear.

3. I assume GoLore@100%'s performance is not comparable with GaLore based on the intuition the authors provide for using GaLore at the beginning and GoLore at the end. If the performance of GoLore@100% is comparable, the authors should also report it in the experiments. Otherwise, this seems to be contradictory to the theoretical results that GaLore diverges while GoLore converges.

4. Besides ReLoRA, FLoRA, and SIFT, there are also some similarity between GoLore and zeroth-order methods with directional derivatives, and GoLore and gradient sketching, e.g., [arXiv: 1809.03054] and [Can Gaussian Sketching Converge Faster on a Preconditioned Landscape? ICML 2024]. It is better to also include such comparisons. Paticularly, zeroth-order methods are also popular for LLMs fine-tuning because of its memory-efficiency, see [arXiv: 2305.17333], [arXiv: 2310.09639], and [arXiv: 2410.07698].

5. The language models used in the experiments are not "large" language models, as Figure 3 is only 60M and Table 2 is 125M. Figure 4 is the curve for fine-tuning LLaMA2-7B, but no test performance like Table 2 is given. Also, the improvement of GoLore in Table 2 is only marginal.

### Questions
1. In Theorem 1, what does it mean for any subspace optimizer $\rho$? What if $\rho$ just maps $P^\top G$ to the stochastic gradient $G$? In this case, the algorithm should still converge.

2. In Theorem 2, $\beta_1=1$ just reduces to SGD without momentum. What happens for other $\beta_1$? Also, in Theorem 3 and 4, what happens for other choice of $\beta_1$? I think $\eta\leq...$ should work instead of being the exact value. Is it the same for $\beta_1$ or the results only hold for only one specific choice?

3. The loss in LLMs training is usually very noisy. Are the curves in Figures 3 and 4 already smoothed?

4. What are the batch sizes used in Figure 1 for all four different algorithms?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper analyzes the convergence properties of GaLore, an existing method for memory-efficient training of large language models (LLMs), where parameters are updated within the dominant subspace of the gradient from a previous iteration rather than the ambient space. For non-convex functions under standard assumptions, the authors establish that GaLore, with a noiseless gradient oracle, converges to a first-order stationary point at a rate of $1/T$. In the stochastic gradient setting, they demonstrate the existence of a loss function and noisy gradient oracle where GaLore fails to converge with probability 1. However, they show that with a sufficiently large and increasing batch size, GaLore provably converges to a first-order stationary point in a mean-square sense at a rate of $1/\sqrt{T}$. Finally, they propose GoLore, a variant of GaLore in which parameters are updated in a random subspace, and prove that it converges to a first-order stationary point in a mean-square sense at a rate of $1/\sqrt{T}$ with a noisy gradient oracle. Brief experiments indicate slight improvements when using GoLore for the final 20% of training iterations on GLUE tasks with LLMs.

### Strengths
The paper provides theoretical results on the convergence of GaLore in both deterministic and specific stochastic settings, circumventing previous assumptions in the literature that required gradient projections to be unbiased and/or contractive. Interestingly, the projection matrices do not necessarily need to be updated at each iteration and can instead be reused across iterations, which may be applicable to other contexts that work with lossy gradient estimates. The counterexample demonstrating when GaLore fails to converge is clear, and the paper is well-motivated.

### Weaknesses
Overall, the discussion of GaLore’s shortcomings is unconvincing both theoretically and experimentally. While the authors present a clear example of when GaLore fails to converge—where gradient noise can be adversarially chosen to occur in a space orthogonal to the gradient of the function—their reasoning for this result is problematic. They claim that near first-order stationary points, the function gradient is dominated by the gradient noise, making it difficult for GaLore to find an informative direction. However, this intuition seems flawed, as in general, for any form of SGD, the gradient noise will dominate the function gradient near a first-order stationary point. The authors show that with a sufficient condition on batch sizes, GaLore will converge in the stochastic setting, effectively bypassing their own negative result. However, there is a lack of discussion on other conditions that could ensure the convergence of GaLore. 

The experimental results show minor improvements when using GaLore followed by GoLore, with an average performance increase of 0.3% on GLUE relative to running GaLore alone. This setup does not align with the theoretical analysis or previous claims regarding GoLore’s superiority, as GaLore is still used for the majority of the training process.

Secondly, the language and presentation of the paper could be improved. The term “stationary solutions” is frequently used and appears to refer to first-order stationary points. Figure 1 is shown on page 2 but isn’t introduced until the end of page 5, and the y-axis label seems intended to represent log(f) in Equation (1) but is labeled simply as “Loss.” At the top of page 4, GaLore is described as a “subspace learning algorithm,” which is inaccurate. In the statement of Theorem 2, the use of the term MSGD and the expected value is confusing, as the source of stochasticity is unclear when the gradients are deterministic. Lastly, there are numerous typos that need correction, especially the spelling of “Optimization” in the title.

### Questions
**Questions**

Are there other mild conditions sufficient to prove the convergence of GaLore in the stochastic setting? Specifically, does a sufficiently small gradient norm suffice, or must the gradient noise tend to zero when computing the subspace? Additionally, what if the gradient noise is isotropic? The presented counterexample relies on the gradient noise occurring in a space orthogonal to the function gradient.

Regarding the GoLore analysis, is the GoLore projection contractive according to the definition in Section 2 of (Fatkhullin et al., 2024)? It seems a random projection should satisfy the contraction property. Also, how does the empirical performance of running only GaLore compare to running only GoLore? The theoretical claims suggest GoLore could replace GaLore entirely, so does GoLore outperform GaLore when used for all training iterations, or does it encounter issues when used independently?


**Comments**

While the paper’s motivation is intriguing, the narrative feels somewhat misguided. The claim that GaLore is unsatisfactory lacks strong support from both theoretical and experimental perspectives. The most compelling results are the positive convergence findings for GaLore in the deterministic and large-batch settings. The paper would be significantly improved by focusing on analyzing conditions under which GaLore converges with mild assumptions, rather than asserting that GaLore has fundamental flaws. Investigating the computational interplay between subspace update frequency, gradient noise, and step size would add valuable insights.

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
4

### Summary
This paper studies the non-convergence of GaLore in stochastic optimization, and addresses this issue using simple approaches. Some numerical experiments are provided to support the proposed GoLore.

### Strengths
(+) The convergence of GaLore is characterized under common assumptions for smooth stochastic nonconvex optimization. The results show that GaLore's projection (via SVD) cannot cope with gradient noise in some cases.

(+) The authors then address the non-convergence of GaLore by substituting its projection with random projection. The proposed GoLore is proved to converge.

### Weaknesses
(-) The non-convergence of GaLore is studied and addressed within the smooth optimization, which is not the major application of GaLore. While non-smooth might be challenging, there are still some analyzable problems, e.g., those in GaLore paper. Specifically, the analysis focuses on smooth functions with bounded gradients, whereas GaLore is primarily used in non-smooth settings such as training large language models with ReLU activations. The paper does not provide sufficient justification for why the smooth analysis is relevant to the practical use cases of GaLore, nor does it demonstrate that the proposed GoLore addresses the limitations of GaLore in the non-smooth settings, which is the main focus of the original GaLore paper.

(-) While the choice of random projection in GoLore is not necessary the best choice in practice. The paper does not discuss on this point. There can be several natural choices, and one example is to use random r singular vectors instead of top-r singular vectors. The authors' methodology of mixing GoLore and GaLore is a supporting evidence on the possible inefficiency of GoLore. The paper lacks a thorough investigation into the properties of different random projection strategies, particularly how they affect convergence and performance compared to SVD-based projection. The theoretical justification for choosing the current random projection method is not fully explored, and it is not clear why other alternatives, such as using random singular vectors, are not considered. The performance difference between different random projection strategies should be explored both theoretically and empirically.

(-) The numerical benefit of GoLore is not very obvious compared to GaLore in both pretraining and finetuning tasks. Note that the improvement of GoLore also needs to apply GaLore at initial training. The numerical comparison with FLoRA is missing. This is very important given the similarity between GoLore and FLoRA. The experimental results do not convincingly demonstrate the practical advantages of GoLore over GaLore. Specifically, the reported improvements are marginal, and the need to use GaLore in the initial training phase raises questions about the practical utility of GoLore. The absence of a comparison with FLoRA, which is a relevant baseline due to its similar approach, further weakens the empirical evaluation.

(-) Typo in the title: optimiztion --> optimization

### Questions
Q1. I would like to know the authors' point of view on the following question. GaLore is a practice-oriented approach for memory efficiency of LLM training. The major application of GaLore is clearly a non-smooth optimization problem. That being said, both GoLore and GaLore do not have theoretical guarantees. How would the benefits of random projection proposed in this paper extend to non-smooth settings? As indicated in Figure 3, GoLore and GaLore share similar performance.

### Soundness
3

### Presentation
3

### Contribution
2
