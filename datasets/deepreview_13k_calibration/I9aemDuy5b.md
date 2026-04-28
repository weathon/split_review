# Stochastic Steepest Descent with Acceleration for $\ell_p$-Smooth Non-Convex Optimization

- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3

## Abstract
In this work, we analyze stochastic $\ell_p$ steepest descent for non-convex problems. Specifically, for $p > 2$, we establish $\epsilon$-approximate stationarity (in expectation) with respect to the dual norm $\Vert\cdot\Vert_{p^*}^{p^*}$ at a rate of $O(\epsilon^{-4})$, thereby generalizing the previous guarantees for signSGD ($p=\infty$). In addition, inspired by techniques for the convex setting, we present a new accelerated $\ell_p$ descent method, called Stacey, based on interpolated primal-dual iterate sequences that are designed for non-Euclidean smooth optimization settings. We compare our algorithm against popular methods such as SGD, Adam, AdamW, and Lion on image classification and pretraining language modeling tasks, and our results demonstrate the potential for both faster convergence and achieving higher accuracy. We further evaluate our algorithm for different values of $p$ across various models and datasets, highlighting the importance and efficiency of non-Euclidean methods as compared to standard Euclidean-based approaches.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies $\ell_p$ steepest descent methods for convex and non-convex problems. The authors are motivated by two key observations: first, while sign-based methods like signSGD have been studied, theoretical understanding of general $\ell_p$ descent methods (beyond $p = 2$ or $p = \infty$) remains limited. Second, they recognize that different optimization problems may have inherently different geometric structures that are better captured by different choices of p-norm.  
The authors are particularly interested in the trade-off between acceleration rates and the choice of norm - for instance, the value of $p = 4$ could potentially gain up to a $d^{1/2}$ factor compared to the Euclidean case, while the acceleration rate would degrade from $T^{-2}$ to $T^{-3/2}$. This is why the authors design methods called $Stacey_{(2,p)}$ and $Stacey_{(p,p)}$ based on the linear coupling framework for acceleration. The resulting methods are similar to other methods that combine momentum with sign updates such as Lion and are shown to perform well in preliminary experiments.

I found the paper to be a bit handwavy in the sense that the theory is only provided for SGD while the more practical methods are more like heuristics.

### Strengths
1. The $\ell_p$ geometry has attracted a lot of attention in recent years due to the similarity of Adam to signSGD. The theory, however, is still quite limited and is usually restricted to the case $p=\infty$, while the authors make an interesting observation that a different value of $p$ might turn out to be better.
2. The numerical experiments are on several benchmarks and the authors don't just compare their method to others, they also study how different hyperparameter choices affect convergence.
3. The performance of the proposed methods is promising and even if the methods themselves are not immediately useful, the ideas presented in this work could inspire an efficient algorithm for deep learning.

### Weaknesses
1. The results in Theorem 1, while new, are clearly inspired by the proof of Bernstein et al. (2018) for signSGD. They do require a lot more work since the update is not exactly the sign of stochastic gradient, but unlike the result of Bernstein et al. (2018), the new one also requires the gradients to be bounded. Thus, $\ell_p$ approach seems to come at the price of having more complicated proofs and requiring more properties from the objective. It remains unclear if this bounded gradient assumption is a fundamental requirement of the method or an artifact of the proof technique. If the rescaling of the gradient introduces pathological changes that necessitate bounded gradients for convergence, it would significantly limit the applicability of the method. This aspect warrants further investigation, as it is crucial to understand the class of problems for which the method is suitable.
2. There is no convergence theory for the two accelerated methods presented in the paper. Even though the authors note that we shouldn't expect acceleration when the variance dominates the convergence rates, it would still be useful to know what convergence properties the methods have. Especially if we could get a faster convergence to a neighborhood of the solution, that would have been already insightful.
3. What we are left with in terms of contributions is the empirical comparisons, but they are too limited to be the main contribution. In some experiments, the authors do not compare to standard baselines, and the LLM experiment is done only for the first 5000 iterations. The absence of comparisons to established optimizers like Lion and Adam, particularly in the ImageNet experiment, is a significant oversight. The authors' justification that their batch size is smaller than that used in the Lion paper does not negate the need for a comparison. Furthermore, the limited number of iterations in the LLM experiment makes it difficult to assess the long-term behavior of the proposed methods.
4. Some experimental details appear to be missing, for instance, I didn't find a description of the scheduler used in the LLM experiment. I also wish the experiments were done and reported with multiple random seeds. I think it would be great if the authors added a section in the appendix with a full list of hyperparameters used in the experiments.
5. The 2D example and plots in Figure 1 do not seem very insightful to me. I think in small dimensions, all geometries should be roughly equivalent since the dimension is just a constant factor. I suggest the authors put the figure in the appendix and use the space to add more numerical comparisons (Lion and Adam).

### Questions
1. Why is there no comparison to Lion and Adam in the ImageNet experiment?
2. Can convergence be established for Stacey? Does it follow immediately from the existing theory for linear coupling?
3. Was cosine annealing or other schedulers used in the LLM experiment? If not, why?

### Soundness
3

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
3

### Summary
This paper studies the problem of accelerating steepest $\ell_p$ descent for minimizing non-convex functions. The authors use signSGD as the motivation for studying steepest descent in the setting of more general norms other than $\ell_2$. They present a theorem for (unaccelerated) stochastic $\ell_p$ descent. They also present an algorithm which they call STACEY, based on coupling $\ell_p$ steepest descent with mirror descent. They compare their algorithm with other optimizers experimentally.

### Strengths
The literature review is well written and mostly does a good job of placing the work in the context of prior works. The authors provide good justifications for why it is useful to study $\ell_p$ descent for values of $p$ other than $2$ and $\infty$. Theorem 1 extends the result for convergence of $\ell_p$ descent to approximate stationary points of the objective function to the stochastic setting.

### Weaknesses
The authors propose two variants of their algorithm Stacey, but do not provide any theoretical analysis of the algorithm even for any simplified/toy examples. The algorithm is primarily motivated by the idea of accelerating $\ell_p$ descent but since there are no convergence or stability results, it is difficult to say whether it actually achieves that goal. The authors try to provide some intuition for how Stacey is different from a previous algorithm, Lion-K, there is not much evidence or analysis to show these differences help the algorithm.

The experiments presented to claim the superior empirical performance of Stacey do not look convincing either. We need to consider the hyperparameter choices (presented in Tables 5, 6, and 7 in Appendix D) to judge whether the comparisons presented are fair. I made the following observations about the experiments:

1.For the ImageNet experiment, Stacey has been compared only with SGD *without momentum*. Without momentum, SGD is known to converge extremely slow, so it is no surprise that it performs as badly as it does, and there is no other baseline in that experiment. 

2. For the LLM experiment, SGD is used without momentum again, so it is expected to perform badly. The learning rate used for Adam and AdamW ($10^{-4}$) is 100 and 500 times smaller than the learning rate used for the different versions of Stacey ($10^{-2}$ and $5\times 10^{-4}$). 

3. For the CIFAR-10 experiment, some versions of Stacey are used with learning rate 0.1 whereas Adam and AdamW used with learning rates 0.001 and 0.01 respectively. Again, it does not appear to be a fair comparison. Moreover, the value of $\lambda$ (presumably, weight decay parameter) for Adam and AdamW is set to $2\times 10^{-4}$, for Stacey it is 0.01.

Different values of $p$ have been chosen for Stacey for different experiments, the reason for which is also not clear. The hyperparameters vary widely within each experiment as well as across different experiments. There are no justifications provided for these hyperparameter choices. If there was a particular rationale for these choices, the authors should describe that and provide more details of the experiment design in the paper. In the absence of that, it is not possible to conclude that Stacey really outperforms the baseline algorithms.


### Questions
1. In Theorem 1, what is the justification for choosing the batch size same as the number of iterations (T)? Typically, the batch size would be constant. In practice, the number of iterations might even be much larger than the total number of training samples available. What would a batch size of T mean in such situations? 

2. For the CIFAR-10 experiment, Stacey(p,p) has been used with p=2, which means that both of the descent steps reduce to just the usual gradient descent. In this case, in what ways is Stacey(2,2) different from the existing momentum-based gradient descent algorithms? 

3. The authors state in lines 316-317 that "In convex settings, SGD cannot improve upon the standard $O(1/\sqrt T)$ rate when the noise parameter $\sigma$ is large enough" and suggest that practical implementations of SGD with momentum introduce acceleration despite the theoretical difficulties. While this is true assuming that the stochastic gradients have bounded variance, there have been multiple works that argue that a different noise assumption is more appropriate for deep learning ("strong growth condition" or "multiplicative noise") and provide accelerated convergence guarantees for stochastic variants of Nesterov's accelerated gradient descent in convex optimization. The authors should consider including them in their discussion of stochastic convex optimization in the context of machine learning:

    [1] Vaswani et al. "Fast and Faster Convergence of SGD for Over-Parameterized Models and an Accelerated Perceptron" https://arxiv.org/abs/1810.07288

    [2] Wojtowytsch, "Stochastic gradient descent with noise of machine learning type. Part I: Discrete time analysis" https://arxiv.org/abs/2105.01650

    [3] Liu & Belkin, "Accelerating SGD with momentum for over-parameterized learning" https://arxiv.org/abs/1810.13395

    [4] Gupta et al. "Nesterov acceleration despite very noisy gradients" https://arxiv.org/abs/2302.05515

4. In the footnote on page 6 as well lines 370-371, the authors make a distinction between "Nesterov's acceleration" and "momentum" but it is not entirely clear what exactly the distinction is. Can the authors clarify how they define these terms and what do they mean when they say they coincide in the deterministic convex setting?

5. Can the authors clarify how the hyperparameters for various algorithms were chosen, in particular for baseline algorithms like SGD, Adam, and AdamW? Was a grid search performed for these or were they chosen based on some default values suggested in prior work? How were the values of $p$ determined for Stacey in various experiments?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The work considers stochastic $\ell_p$ steepest descent for non-convex optimization in case when $p>2$ and establishes its convergence rates. The work introduces an accelerated $\ell_p$ method and compares it to SGD, Adam, AdamW, and Lion.

### Strengths
The paper contains many insights, references, theorems and assumptions are clearly written. Plots, tables and diagrams are well-done and help to understand the contribution.

### Weaknesses
The analysis in Theorem 1 is done under a restrictive bounded gradients assumption. Usually it significantly simplifies the analysis. There are many convergence results for gradient methods without it, e.g., see [1, 2] and references therein. 

It appears to me that the main contribution of the paper is therefore mostly experimental, yet a very large part of the introduction is devoted to the discussion about the theory for $\ell_p$-spaces. I just find it inconsistent, yet insightful. I do not see many explanations to the experiments, though.

I am ready to discuss the paper with the authors and find the work interesting. But I believe it can be improved a lot.

### Questions
Can the theory be improved by removing the bounded gradients assumption? What is the challenge?

Why the authors analyze only the stochastic descent but not STACEY?

How can one choose an appropriate $p$ for the deep learning problem at hand? Do practitioners need to follow your recommendation of $p=3$ or they need to set it themselves for each particular problem?

Could you explain, what is written in Appendix? You provide tables for different methods, but you test only STACEY.

Can you explain, how do you choose parameters for the baselines? Why do you choose a smaller lr for Adam against Stacey? Why can not we use the fact that $\ell_p$ norms are equivalent, choose $p$ for the problem based on STACEY experiments (e.g., $p=3$), adjust the parameters for Adam using the relations between $\ell_2$ and $\ell_3$ norms.

### Soundness
3

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
4

### Summary
This paper presents stochastic $\ell_p$ steepest descent (Algorithm 1) for non-convex optimization and its convergence analysis (Theorem 1). It also presents STACEY optimizers (Algorithms 2 and 3) that are accelerated descent methods. Moreover, it provides numerical results to support the theoretical analyses.

### Strengths
The strengths of this paper are
- to present stochastic $\ell_p$ steepest descent (Algorithm 1) for non-convex optimization. 
- to present STACEY optimizer (Algorithms 2 and 3) based on convex optimization. 
- to provide numerical results to support the theoretical analyses.

### Weaknesses
 I am interested in the proposed methods (Algorithms 1, 2, and 3) and numerical results (Section 4). However, I have some theoretical concerns that are Weaknesses of the paper. Please see the following Questions.
- Theorem 1: The result is based on the standard assumptions (Assumptions 1-4). However, I do not think that the theorem leads to convergence of Algorithm 1. This is because, for all $T \geq 1$ an upper bound of $\mathbb{E}[T^{-1} \sum_{t=0}^{T-1} \Vert \nabla f (\theta_t) \Vert_{p^*}^{p^*}]$ is
\begin{align*}
\frac{f(\theta_0) - f(\theta^*)}{\eta T} + \frac{1}{T} \sum_{t=0}^{T-1} \frac{\frac{2p - 1}{p-1} G^{\frac{1}{p-1}} \Vert \sigma \Vert_1}{\sqrt{n_t}} + \frac{L \eta G^{\frac{2}{p-1}}}{2},
\end{align*}
which, together with $T \to \infty$,  implies that the upper bound becomes
\begin{align*}
\frac{f(\theta_0) - f(\theta^*)}{\eta T} + \frac{1}{T} \sum_{t=0}^{T-1} \frac{\frac{2p - 1}{p-1} G^{\frac{1}{p-1}} \Vert \sigma \Vert_1}{\sqrt{n_t}} + \frac{L \eta G^{\frac{2}{p-1}}}{2} \to \frac{L \eta G^{\frac{2}{p-1}}}{2} > 0,
\end{align*}
where we assume that the second term $\frac{1}{T} \sum_{t=0}^{T-1} \frac{\frac{2p - 1}{p-1} G^{\frac{1}{p-1}} \Vert \sigma \Vert_1}{\sqrt{n_t}}$ converges to $0$. 
Since the learning rate $\eta$ is a positive constant, the upper bound never converges to $0$.
- Theorem 1 (Cont.): Although Theorem 1 does not guarantee convergence of Algorithm 1, there is a possibility such that Algorithm 1 is an $\epsilon$-approximation, i.e., there exist sufficient conditions such that the upper bound is less than or equal to a small $\epsilon > 0$:
\begin{align*}
\underbrace{\frac{f(\theta_0) - f(\theta^*)}{\eta T}}_{\leq \epsilon/3} + \underbrace{\frac{1}{T} \sum_{t=0}^{T-1} \frac{\frac{2p - 1}{p-1} G^{\frac{1}{p-1}} \Vert \sigma \Vert_1}{\sqrt{n_t}}}_{\leq \epsilon/3} + \underbrace{\frac{L \eta G^{\frac{2}{p-1}}}{2}}_{\leq \epsilon/3} \leq \epsilon.
\end{align*}
Here, let us consider the case where the batch size $n_t$ is a constant ($n_t = n$). Then, sufficient conditions to satisfy that Algorithm 1 is an $\epsilon$-approximation are as follows:
\begin{align*}
\eta \leq \frac{2 \epsilon}{3 L G^{\frac{2}{p-1}}} \land T \geq \frac{3 (f(\theta_0) - f(\theta^*))}{\epsilon \eta} \land \sqrt{n} \geq \frac{3 \frac{2p - 1}{p-1} G^{\frac{1}{p-1}} \Vert \sigma \Vert_1}{\epsilon}.
\end{align*}
The conditions would be appropriate in theory. However, it would not be good in practice, since the setting of $\eta$, $n$, and $T$ satisfying the above conditions would be unrealistic. For example, let $\epsilon = 10^{-3}$. Then, $\eta$ satisfying $\eta \leq \frac{2 \epsilon}{3 L G^{\frac{2}{p-1}}}$ would be sufficiently small, since $L$ and $G$ would be large. Even if we assume that $p= 2$, $L = 10^2$, and $G = 10$, we have that $\eta \leq 2 \cdot 10^{-3}/(3 \cdot 10^4) = (2/3) 10^{-7}$. This implies that Algorithm 1 using $\eta$ satisfying $\eta \leq \frac{2 \epsilon}{3 L G^{\frac{2}{p-1}}}$ would not work. Therefore, I would like to suggest that the authors could show that the sufficient conditions to achieve an $\epsilon$-approximation of Algorithm 1 hold in practical cases such as DNN training.
- Theorem 1 (Cont.): Although Theorem 1 does not guarantee convergence of Algorithm 1, the authors fixed the number of steps $T$ and proposed the setting of the batch size $n_t = T$, the number of gradient call $N = T^2$, and the learning rate $\eta = \frac{1}{L^{1/2} G^{1/(p-1)} T^{1/2}}$. Then, the authors claimed that the upper bound is $O(N^{- 1/4})$. The setting and the upper bound $O(N^{- 1/4})$ seem to be useful in theory. However, we must verify whether or not the real upper bound 
\begin{align*}
U := \frac{1}{N^{1/4}} \left(  L^{1/2} G^{1/(p-1)} ( f(\theta_0) - f(\theta^*) + 1/2)  + \frac{2p -1}{p-1} G^{\frac{1}{p-1}} \Vert \sigma \Vert_1 \right)
\end{align*}
becomes sufficiently small (e.g., $U < 10^{-4}$). I think that there is a possibility such that $U$ becomes large  (e.g., $U > 10^{2}$). Therefore, I would also like to suggest that the authors could provide sufficient conditions (e.g., practical setting of $\eta$, $n_t$, and $T$) such that $U$ can be small in practical cases such as DNN training. 
- Theorem 1 (Cont.): The above major concerns for Theorem 1 are based on unknown parameters $f(\theta^*)$, $G$, $\Vert \sigma \Vert_1$, and $L$. It would be grateful if the authors could estimate their parameters before implementing Algorithm 1. However, I think that such estimations are difficult. Also, using constant learning rates would not decrease the upper bound (from the above discussion). Here, I would like to suggest that using diminishing learning rate $\eta_t$ (e.g., $\eta_t = 1/\sqrt{t}$) could be useful to show that an upper bound converges to $0$. Even if the upper bound includes unknown parameters, there is a possibility such that the upper bound can be represented by using Landou's symbol $O$ (such as $\mathbb{E}[T^{-1} \sum_{t=0}^{T-1} \Vert \nabla f (\theta_t) \Vert_{p^*}^{p^*}] = O(\log T/\sqrt{T})$). If the authors use diminishing learning rate $\eta_t$, then Section 5 should use the diminishing learning rate $\eta_t$ not constant learning rates in Tables 5, 6, and 7 (see also the final question).
- The proof of Theorem 1: The proof is well-written. However, I have one concern for the proof of Lemma 3 (Appendix A.1 and L269-L284). Given $t$, the authors consider two cases: (1) $\forall i (| \nabla f(\theta_t)^{(i)} | \leq |\zeta^{(i)}| \leq |g(\theta_t)^{(i)}| )$ and (2) $\forall i (| \nabla f(\theta_t)^{(i)} | \geq |\zeta^{(i)}| \geq |g(\theta_t)^{(i)}| )$. The cases seem to be incorrect. If (1) is assumed, then (2) should be $\lnot (1)$, i.e.,
\begin{align*}
\exists i_0 \text{ } (| \nabla f(\theta_t)^{(i_0)} | > |\zeta^{(i_0)}|) \lor (|\zeta^{(i_0)}| > |g(\theta_t)^{(i_0)}|),
\end{align*}
which is not equal to the current (2): $\forall i (| \nabla f(\theta_t)^{(i)} | \geq |\zeta^{(i)}| \geq |g(\theta_t)^{(i)}| )$.
Hence, I think that the proof of Lemma 3 should be improved. For example, I would like to suggest the authors could prove Lemma 3 for the following two divided cases:
 (1) $\forall i (| \nabla f(\theta_t)^{(i)} | \leq |\zeta^{(i)}| \leq |g(\theta_t)^{(i)}| )$ and (2) $\exists i_0 \text{ } (| \nabla f(\theta_t)^{(i_0)} | > |\zeta^{(i_0)}|) \lor (|\zeta^{(i_0)}| > |g(\theta_t)^{(i_0)}|)$.
- I do not think that the parameters (Tables 5, 6, and 7) used in the numerical results are based on the theoretical result (Theorem 1). For example, STACEY in Table 5 uses $n_t = n = 128$ and $\eta = 0.02, 0.1$. Could you show that the parameters such as $n_t = n = 128$ and $\eta = 0.02, 0.1$ satisfy the sufficient conditions to achieve an $\epsilon$-approximation of STACEY? Showing it is important to justify the theoretical result in the paper. If the parameters do not satisfy the conditions, then I think that parameters based on the theoretical result (Theorem 1) should be used in the numerical results. For example, given $\epsilon = 10^{-3}$, we set $\eta = O(\epsilon)$, $n = \Omega (1/\epsilon)$, and $T = \Omega (1/(\epsilon \eta))$ (However, I do not know how to set $L$, $G$, $\Vert \sigma \Vert_1$). Then, we should plot the minimum $\min_{t = 0, \cdots, T-1}\Vert \nabla f (\theta_t) \Vert_{p^*}^{p^*}$ of the full gradient norms (or the mean $(1/T) \sum_{t=0}^{T-1} \Vert \nabla f (\theta_t) \Vert_{p^*}^{p^*}$ of the full gradient norms) versus the number of steps $t$ and check whether or not the minimum (or the mean) is less than or equal to $\epsilon$ $(=10^{-3})$.

### Questions
- Theorem 1: The result is based on the standard assumptions (Assumptions 1-4). However, I do not think that the theorem leads to convergence of Algorithm 1. This is because, for all $T \geq 1$ an upper bound of $\mathbb{E}[T^{-1} \sum\_{t=0}^{T-1} \Vert \nabla f (\theta_t) \Vert\_{p^*}^{p^*}]$ is 
\begin{align*}
\frac{f(\theta_0) - f(\theta^*)}{\eta T} + \frac{1}{T} \sum\_{t=0}^{T-1} \frac{\frac{2p - 1}{p-1} G^{\frac{1}{p-1}} \Vert \sigma \Vert\_1}{\sqrt{n_t}} + \frac{L \eta G^{\frac{2}{p-1}}}{2},
\end{align*}
which, together with $T \to \infty$,  implies that the upper bound becomes 
\begin{align*}
\frac{f(\theta_0) - f(\theta^*)}{\eta T} + \frac{1}{T} \sum\_{t=0}^{T-1} \frac{\frac{2p - 1}{p-1} G^{\frac{1}{p-1}} \Vert \sigma \Vert\_1}{\sqrt{n_t}} + \frac{L \eta G^{\frac{2}{p-1}}}{2} \to \frac{L \eta G^{\frac{2}{p-1}}}{2} > 0,
\end{align*}
where we assume that the second term $\frac{1}{T} \sum\_{t=0}^{T-1} \frac{\frac{2p - 1}{p-1} G^{\frac{1}{p-1}} \Vert \sigma \Vert\_1}{\sqrt{n_t}}$ converges to $0$. 
Since the learning rate $\eta$ is a positive constant, the upper bound never converges to $0$.
- Theorem 1 (Cont.): Although Theorem 1 does not guarantee convergence of Algorithm 1, there is a possibility such that Algorithm 1 is an $\epsilon$-approximation, i.e., there exist sufficient conditions such that the upper bound is less than or equal to a small $\epsilon > 0$:
\begin{align*}
\underbrace{\frac{f(\theta_0) - f(\theta^*)}{\eta T}}\_{\leq \epsilon/3} + \underbrace{\frac{1}{T} \sum\_{t=0}^{T-1} \frac{\frac{2p - 1}{p-1} G^{\frac{1}{p-1}} \Vert \sigma \Vert\_1}{\sqrt{n_t}}}\_{\leq \epsilon/3} + \underbrace{\frac{L \eta G^{\frac{2}{p-1}}}{2}}\_{\leq \epsilon/3} \leq \epsilon.
\end{align*}
Here, let us consider the case where the batch size $n_t$ is a constant ($n_t = n$). Then, sufficient conditions to satisfy that Algorithm 1 is an $\epsilon$-approximation are as follows:
\begin{align*}
\eta \leq \frac{2 \epsilon}{3 L G^{\frac{2}{p-1}}} \land T \geq \frac{3 (f(\theta_0) - f(\theta^*))}{\epsilon \eta} \land \sqrt{n} \geq \frac{3 \frac{2p - 1}{p-1} G^{\frac{1}{p-1}} \Vert \sigma \Vert\_1}{\epsilon}.
\end{align*}
The conditions would be appropriate in theory. However, it would not be good in practice, since the setting of $\eta$, $n$, and $T$ satisfying the above conditions would be unrealistic. For example, let $\epsilon = 10^{-3}$. Then, $\eta$ satisfying $\eta \leq \frac{2 \epsilon}{3 L G^{\frac{2}{p-1}}}$ would be sufficiently small, since $L$ and $G$ would be large. Even if we assume that $p= 2$, $L = 10^2$, and $G = 10$, we have that $\eta \leq 2 \cdot 10^{-3}/(3 \cdot 10^4) = (2/3) 10^{-7}$. This implies that Algorithm 1 using $\eta$ satisfying $\eta \leq \frac{2 \epsilon}{3 L G^{\frac{2}{p-1}}}$ would not work. Therefore, I would like to suggest that the authors could show that the sufficient conditions to achieve an $\epsilon$-approximation of Algorithm 1 hold in practical cases such as DNN training.
- Theorem 1 (Cont.): Although Theorem 1 does not guarantee convergence of Algorithm 1, the authors fixed the number of steps $T$ and proposed the setting of the batch size $n_t = T$, the number of gradient call $N = T^2$, and the learning rate $\eta = \frac{1}{L^{1/2} G^{1/(p-1)} T^{1/2}}$. Then, the authors claimed that the upper bound is $O(N^{- 1/4})$. The setting and the upper bound $O(N^{- 1/4})$ seem to be useful in theory. However, we must verify whether or not the real upper bound 
\begin{align*}
U := \frac{1}{N^{1/4}} \left(  L^{1/2} G^{1/(p-1)} ( f(\theta_0) - f(\theta^*) + 1/2)  + \frac{2p -1}{p-1} G^{\frac{1}{p-1}} \Vert \sigma \Vert\_1 \right)
\end{align*}
becomes sufficiently small (e.g., $U < 10^{-4}$). I think that there is a possibility such that $U$ becomes large  (e.g., $U > 10^{2}$). Therefore, I would also like to suggest that the authors could provide sufficient conditions (e.g., practical setting of $\eta$, $n_t$, and $T$) such that $U$ can be small in practical cases such as DNN training. 
- Theorem 1 (Cont.): The above major concerns for Theorem 1 are based on unknown parameters $f(\theta^*)$, $G$, $\Vert \sigma \Vert\_1$, and $L$. It would be grateful if the authors could estimate their parameters before implementing Algorithm 1. However, I think that such estimations are difficult. Also, using constant learning rates would not decrease the upper bound (from the above discussion). Here, I would like to suggest that using diminishing learning rate $\eta_t$ (e.g., $\eta_t = 1/\sqrt{t}$) could be useful to show that an upper bound converges to $0$. Even if the upper bound includes unknown parameters, there is a possibility such that the upper bound can be represented by using Landou's symbol $O$ (such as $\mathbb{E}[T^{-1} \sum\_{t=0}^{T-1} \Vert \nabla f (\theta_t) \Vert\_{p^*}^{p^*}] = O(\log T/\sqrt{T})$). If the authors use diminishing learning rate $\eta_t$, then Section 5 should use the diminishing learning rate $\eta_t$ not constant learning rates in Tables 5, 6, and 7 (see also the final question).
- The proof of Theorem 1: The proof is well-written. However, I have one concern for the proof of Lemma 3 (Appendix A.1 and L269-L284). Given $t$, the authors consider two cases: (1) $\forall i (| \nabla f(\theta_t)^{(i)} | \leq |\zeta^{(i)}| \leq |g(\theta_t)^{(i)}| )$ and (2) $\forall i (| \nabla f(\theta_t)^{(i)} | \geq |\zeta^{(i)}| \geq |g(\theta_t)^{(i)}| )$. The cases seem to be incorrect. If (1) is assumed, then (2) should be $\lnot (1)$, i.e.,
\begin{align*}
\exists i_0 \text{ } (| \nabla f(\theta_t)^{(i_0)} | > |\zeta^{(i_0)}|) \lor (|\zeta^{(i_0)}| > |g(\theta_t)^{(i_0)}|),
\end{align*}
which is not equal to the current (2): $\forall i (| \nabla f(\theta_t)^{(i)} | \geq |\zeta^{(i)}| \geq |g(\theta_t)^{(i)}| )$.
Hence, I think that the proof of Lemma 3 should be improved. For example, I would like to suggest the authors could prove Lemma 3 for the following two divided cases:
 (1) $\forall i (| \nabla f(\theta_t)^{(i)} | \leq |\zeta^{(i)}| \leq |g(\theta_t)^{(i)}| )$ and (2) $\exists i_0 \text{ } (| \nabla f(\theta_t)^{(i_0)} | > |\zeta^{(i_0)}|) \lor (|\zeta^{(i_0)}| > |g(\theta_t)^{(i_0)}|)$.
- I do not think that the parameters (Tables 5, 6, and 7) used in the numerical results are based on the theoretical result (Theorem 1). For example, STACEY in Table 5 uses $n_t = n = 128$ and $\eta = 0.02, 0.1$. Could you show that the parameters such as $n_t = n = 128$ and $\eta = 0.02, 0.1$ satisfy the sufficient conditions to achieve an $\epsilon$-approximation of STACEY? Showing it is important to justify the theoretical result in the paper. If the parameters do not satisfy the conditions, then I think that parameters based on the theoretical result (Theorem 1) should be used in the numerical results. For example, given $\epsilon = 10^{-3}$, we set $\eta = O(\epsilon)$, $n = \Omega (1/\epsilon)$, and $T = \Omega (1/(\epsilon \eta))$ (However, I do not know how to set $L$, $G$, $\Vert \sigma \Vert\_1$). Then, we should plot the minimum $\min\_{t = 0, \cdots, T-1}\Vert \nabla f (\theta_t) \Vert\_{p^*}^{p^*}$ of the full gradient norms (or the mean $(1/T) \sum\_{t=0}^{T-1} \Vert \nabla f (\theta_t) \Vert\_{p^*}^{p^*}$ of the full gradient norms) versus the number of steps $t$ and check whether or not the minimum (or the mean) is less than or equal to $\epsilon$ $(=10^{-3})$.

### Soundness
2

### Presentation
2

### Contribution
2
