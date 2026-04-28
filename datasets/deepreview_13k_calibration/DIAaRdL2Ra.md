# Convergence of Adafactor under Non-Convex Smooth Stochastic Optimization

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Adafactor, a memory-efficient variant of Adam, has emerged as one of the popular choices for training deep learning tasks, particularly large language models.
However, despite its practical success, there is limited theoretical analysis of Adafactor's convergence. In this paper, we present a comprehensive analysis of Adafactor in a non-convex smooth setting. We show that full-batch Adafactor finds a stationary point at a rate of $\tilde{O}(1/\sqrt{T})$ with the default setup, which could be accelerated to $\tilde{O}(1/T)$ with a constant step-size parameter. For stochastic Adafactor without update clipping, we prove a convergence rate of $\tilde{O}(1/\sqrt{T})$ with the right parameters covering the default setup. We also prove that Adafactor with a time-varying clipping threshold could also find a stationary point with the rate of $\tilde{\mathcal{O}}(1/\sqrt{T})$. Our theoretical results are further complemented by some experimental results.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper studies the theoretical convergence of Adafactor without momentum for smooth non-convex optimization. That is, under the assumption of Lipschitzness of the gradient, lower boundedness of the objective, and uniform boundedness of the (stochastic) gradients, the authors derive new convergence guarantees for Adafactor with and without update clipping.

In particular, for the deterministic version of Adafactor, the authors derive $O(\log(T) / T)$ rate for the constant relative stepsize parameter $\rho_k$ and $O(\log(T) / \sqrt{T})$ rate for $\rho_k \sim k^{-1/2}$. Both results hold for $\beta_{2,1} = 1/2$ and arbitrary $\beta_{2,k} \in (0,1)$ for $k \geq 2$

Next, for the stochastic version of Adafactor without update clipping, the authors prove $O(\log(T/\delta) T^{-c + 1/2})$ high-probability convergence rate, where $\delta \in (0,1)$ is the failure probability and parameter $c \in [1/2,1]$ defines the rate of the increase of $\beta_{2,k}$ as $\beta_{2,k} = 1 - k^{-c}$ for $k\geq 2$. In particular, when $c = 1$, the derived rate matches the one known for Adam. 

Finally, for the stochastic version of Adafactor with update clipping, the authors show similar results when the clipping parameter $d_k$ is chosen as $d_k = k^{\frac{c}{2(\alpha - 1)}}$ for some $\alpha > 1$.

The authors also provide several experimental results where they test the performance of Adagrad for different increase rates for $\beta_{2,k}$ parameter and the sensitivity of the method to the choices of $\epsilon_1$ and $\alpha$ parameters.

### Strengths
S1. To the best of my knowledge, this paper provides the first theoretical convergence analysis of Adafactor. Given the popularity of the method and the relevance of memory-efficient optimizers to modern problems such as the training of LLMs, obtaining rigorous theoretical convergence guarantees for Adafactor is important for the community.

S2. The authors provide a sketch of the proof that helps to understand the key steps of the analysis.

### Weaknesses
### weaknesses:
W1. The analysis relies on the assumption that the $\ell_\infty$-norms of **the iterates are bounded from below and from above by $\Theta_{\min}$ and $\Theta_{\max}$ respectively**. This is a restrictive assumption, and it should be included in the list of assumptions provided in Section 3. In lines 302-304, the authors briefly mention that they assume $\|\| X_k\|\| \leq \Theta_{{\max}}$ and that the rate depends on $\Theta_{\max}$, but they do not mention in the main text that all the results of the paper rely on the additional assumption that $\|\|X_k \|\| \geq \Theta_{\min}$ for some $\Theta_{\min} > 0$. Both conditions are restrictive, particularly the lower bound, and it is not obvious why the norms of the iterates are bounded with probability $1$. The best-known convergence results for Adam do not require such assumptions. It is unclear how \(\Theta_{\max}\) could be bounded in practice, and how \(\Theta_{\min}\) could be guaranteed to be greater than zero.

W2. The analysis relies on the boundedness of the gradients and the boundedness of the gradient noise. Although the boundedness of the gradients is a common assumption in the literature, assuming boundedness of the noise is quite restrictive: this assumption seems to be unrealistic (e.g., even for Gaussian noise, it doesn't hold), and, in addition, even if the noise is bounded for a particular run of the method, the bound can be huge, especially for training LLMs [1].

W3. The derived bounds are proportional at least to $\epsilon_1^{-1/2}$ (e.g., the first bound from (13)), some bounds are proportional to $\epsilon_1^{-5/2}$ (e.g., the second bound from (13)). Since $\epsilon_1$ is typically small, this extra factor is noticeable. Moreover, the best-known results for Adam do not have such a dependency on an analogous parameter, e.g., in [2], the dependency is only logarithmical.

W4. The rate in the deterministic case is $O(mn\log(T)/T)$ (for constant $\rho_k$) or to $O(mn\log(T)/\sqrt{T})$ (if we assume that $A_0$ and $A_1$ are $O(1)$ in the first bound in (13)) or to $O(\epsilon_1^{-2}\log(T)/\sqrt{T})$ (if we assume that $A_0$ and $A_1'$ are $O(1)$ in the second bound in (13)). That is, the rate is either proportional to $mn$, i.e., the dimension dependence is similar to Adam, or to $\epsilon_1^{-2}$, which is of the order $10^{60}$ - much larger than the dimensionality of the largest existing model - for the default value $\epsilon_1$. This raises concerns about the practical applicability of the derived bounds.

W5. Experiments do not clearly illustrate the dependence on parameters $\epsilon_1, c, \alpha$. In particular, in the experiment for BERT-base model, the authors report only training loss. Next, in the experiments with ResNet, the authors show that the accuracy, in fact, largely depends on $c$, but from the training loss, it is not that clear. Finally, in the experiments from sections D.2 and D.3 the authors do not report the accuracy and the test loss, thus, the real influence of $\epsilon_1$ and $\alpha$ remains unclear. Moreover, in Figures 4, 5, and 6, the difference between the lines is not visible. I recommend to zoom in the plots and show the area where the loss is small, especially for the final stages of training.

W6. The paper requires a thorough proofreading. I noticed several inaccuracies in English and flaws in the structure. Here are some of them:
- title: under --> for
- line 48: on non-convex smooth setup --> for non-convex smooth setup
- line 54: under --> for
- lines 92-94: this part should be rephrased because it could be misunderstood by the readers, i.e., one can interpret that the authors mention only a part of closely related works
- line 145: dependent by the random sample --> dependent on the random sample
- page 4: missing periods after "Matrix factorization", "Increasing decay rate", and so on
- line 182: maintain --> maintains
- section 6.1: the first and the second paragraphs in the discussion of $c$ and optimal rate are redundant
- section 6.1: the whole paragraph about $\epsilon_1$ and $\epsilon_2$ gives a technical discussion of the results that are given in the appendix. This discussion is not self-contained: to understand what the authors mean, one needs to read the result in the appendix. I suggest adding the details to the main text.

### Questions
Q1. Can the authors remove the assumption from (14), i.e., boundedness of the iterates, and derive the results without it?

Q2. Is it possible to generalize the results to the case of unbounded noise?

Q3. Is it possible to remove the assumption of boundedness of the gradients at least for the deterministic case?

Q4. Is it possible to show similar bounds to the ones derived in the paper but with logarithmic dependence on $\epsilon_1$?

Q5. Is it possible to prove $O((m+n)\log(T)/T)$ convergence rate for Adafactor?

Q6. Why is a time-varying threshold considered in Section 7? Is it crucial? Is it possible to prove a similar result for constant $d_k$?

**Other comments.**

C1. Reference to PaLM in line 41 is a bit misleading since, in that work, the authors use Adafactor without factorization, which is essentially Adam with re-scaling.

C2. In the discussion of the choice of $\beta_2$, it is worth to add that with constant $\beta_2$ (stochastic) Adam is not guaranteed to converge [1].

C3. It is worth mentioning that update clipping in Adafactor is not a standard gradient clipping.

C4. In formula (10), $\bar{G}_k$ is not defined (it is defined in the appendix).

C5. Line 378: (18) --> (10)

C6. Line 399: $V_k \to R_k$

---
References

[1] Reddi et al. On the convergence of Adam and beyond. ICLR 2018

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper provides a theoretical analysis of the convergence of AdaFactor in the non-convex smooth setting. The analysis is given both for the deterministic case (full-batch) and for the stochastic case. Moreover, the authors obtain theoretical guarantees of convergence when clipping is added to AdaFactor.

### Strengths
1) These results look novel, as authors demonstrate the analysis of AdaFactor for the non-convex smooth case with various considerations of oracle (with and without stochasticity).
2) The proofs look correct.
3) The paper is easy to follow except some shortcomings (see section Weaknesses).

### Weaknesses
1)  The paper is positioned as theoretical, so it is expected to see some more advanced theoretical results, especially they already exist in the literature.

a) Assumption A.4 (almost surely bounded stochastic gradient) is quite strong and noticeably reduces the class of possible stochastic oracles (as a consequence, possible distributions of stochasticity). Indeed, there exist some analyses for adaptive methods (AdaGrad) which provide theoretical guarantees of convergence under weaker assumption on stochastic oracle (e.g. see [1]), more specifically, with sub-Gaussian noise. Is it possible, in the authors' opinion, to obtain similar convergence rates as in the provided analysis by relaxing Assumption A.4? For example bounded not stochastic gradient but variance or other moment.

b) It would also be interesting to know what the authors were guided by when they integrated the clipping technique into AdaFactor. Based on convergence bounds (see Theorems 6.1 and 7.1), the addition of clipping is not really justified since the theoretical guarantees for AdaFactor with and without clipping are the same. What is the authors' main idea to add clipping? Typically clipping is needed when the stochastic gradient has heavy tails [2]. But again the authors have a simple assumption of boundedness. Moreover, the current analysis does not demonstrate any benefit from clipping, and it is not clear if the clipping used is the standard one that is used to handle heavy-tailed noise.

[1] Liu, Zijian, et al. "High probability convergence of stochastic gradient methods." International Conference on Machine Learning. PMLR, 2023.

[2] Gorbunov, Eduard, Marina Danilova, and Alexander Gasnikov. "Stochastic optimization with heavy-tailed noise via accelerated gradient clipping." Advances in Neural Information Processing Systems 33 (2020): 15042-15053.

2) The experimental section is pretty weak. As I said the paper is positioned as theoretical, so weak experiments are not a big disadvantage. But it is nice to add at least one experiment comparing with other methods (Adam, RMSProp, Lion and other SOTA) except AdaFactor. Just to understand which method we talk about in terms of its practical feasibility.

3) Some shortcomings in terms of the writing of the paper:

    a) In the part with contribution, there must be $\mathcal{O}\left(\frac{1}{T}\right)$ instead of $\mathcal{O}\left(\frac{1}{\sqrt{T}}\right)$ (for the full-batch setting), see Theorem 5.1. Right?

    b) Superfluous numbering of formulas: did not found any references on $(4), (5), (11), (19), (21), (23), (37), (39), (41), (64), (69), (76), (86), (101), (102)$. It is worth noting that, possibly, they should be removed. It can increase the readability of the paper.

========================

The article is not bad, but the theoretical analysis is rather rough for me, there are more delicate results in the literature. And theory is the main contribution.

### Questions
See Weaknesses

### Soundness
3

### Presentation
2

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
This paper investigated the first convergence behavior of Adafactor on non-convex smooth case. The results show that Adafactor could achieve comparable convergence performance to Adam. The authors also designed a new proxy step-size to decouple the stochastic gradients from the unique adaptive step-size and update clipping.

### Strengths
1.The authors list all major differences of Adafactor from Adam, which benefits readers’ understanding.

2.Some discussions are given to emphasize the advantages of the results in this paper.

3.The challenges and techniques of proof are presented in detail.

### Weaknesses
1.Although the quality of paper doesn’t depend on the word count of Abstract, readers may have a bad impression towards this paper. I think this abstract doesn’t fully present all contributions of this paper.

2.Abstract (line 16) shows the convergence rate of full-batch Adafactor is $\tilde{\mathcal{O}}(1/T)$. However, the first contribution (lines 67-70) is that the convergence rate of full-batch Adafactor is $\tilde{\mathcal{O}}(1/\sqrt{T})$. The discrepancy between these two statements is confusing and needs to be addressed. It is crucial to maintain consistency in the presentation of results.

3.In Equation (13), the second result should not have $\triangle_0^2$ rather than $\tilde{\triangle}_0^2$. The use of $\triangle_0^2$ seems inconsistent with the notation established earlier in the paper, and this needs to be corrected for clarity and mathematical rigor.

4.In line 1430, the first $C_0$ should be $C_0^\prime$. This is a minor but important typographical error that needs to be fixed to avoid confusion.

5.The word “estimation” is just mentioned once in the main text. Some explanations of this word are necessary for readers’ understanding. The lack of context around this term makes it difficult to understand its significance within the broader framework of the paper. A more detailed explanation of how this estimation is performed and its role in the analysis is needed.

### Questions
1.The third contribution (lines 75-77) states that Adafactor a time-varying clipping threshold could also achieve the best convergence rate of  $\tilde{\mathcal{O}}(1/\sqrt{T})$. Why do the authors think the rate $\tilde{\mathcal{O}}(1/\sqrt{T})$ is best? Isn't the rate $\tilde{\mathcal{O}}(1/\sqrt{T})$ better than $\tilde{\mathcal{O}}(1/\sqrt{T})$?

2.How do the equations (26) and (38) hold since we don’t know whether $\frac{d\sqrt{mn}}{\|\bar{\mathbf{U}}_k\|_F} > 1$ holds, which is the key point to derive a free-dimension numerator bound (the second result in Equation (13))? 

3.In Theorem B.1, I don’t find any dependency on the dimension $d$ like Theorem A.1. So, why do the authors regard the results (Equations (43), (45)) of Theorem B.1 as free dimension bounds?

### Soundness
3

### Presentation
2

### Contribution
2
