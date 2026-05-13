# ICL-TSVD: Bridging Theory and Practice in Continual Learning with Pre-trained Models

- Decision: Accept
- Scores: 5, 6, 5, 6

## Abstract
The goal of continual learning (CL) is to train a model that can solve multiple tasks presented sequentially. Recent CL approaches have achieved strong performance by leveraging large pre-trained models that generalize well to downstream tasks. However, such methods lack theoretical guarantees, making them prone to unexpected failures. 
Conversely, principled CL approaches often fail to achieve competitive performance. In this work, we bridge this gap between theory and practice by integrating an empirically strong approach (RanPAC) into a principled framework, Ideal Continual Learner (ICL), \textit{designed} to prevent forgetting. Specifically, we lift pre-trained features into a higher dimensional space and formulate an over-parametrized minimum-norm least-squares problem. We find that the lifted features are highly ill-conditioned, potentially leading to large training errors (numerical instability) and increased generalization errors (\textit{double descent}). We address these challenges by continually truncating the singular value decomposition (SVD) of the lifted features. Our approach, termed ICL-TSVD, is stable with respect to the choice of hyperparameters, can handle hundreds of tasks, and outperforms state-of-the-art CL methods on multiple datasets. Importantly, our method satisfies a recurrence relation throughout its continual learning process, which allows us to prove it maintains small training and generalization errors by appropriately truncating a fraction of SVD factors. This results in a stable continual learning method with strong empirical performance and theoretical guarantees.



\iffalse
In continual learning (CL), the goal is to train a model capable of solving multiple tasks presented sequentially. Recently, leveraging large pre-trained  models for CL has gained popularity due to their generalizability to various downstream tasks. However, many current CL methods that utilize pre-trained models exhibit instability, with their performance highly sensitive to specific hyperparameters. Moreover, these methods often lack theoretical guarantees. In this paper, we introduce a simple yet stable CL method that effectively utilizes pre-trained models. Our approach is robust to hyperparameter choices, offers theoretical guarantees on both training and generalization errors, and is capable of handling hundreds of tasks. Inspired by classical numerical linear algebra techniques and the "ideal continual learner" framework \citep{Peng-ICML2023}, our method also draws on recent theoretical insights from benign overfitting and double descent. Extensive experiments on standard datasets demonstrate that our approach outperforms several state-of-the-art CL methods.

In continual learning (CL), one aims to train a model that can solve multiple tasks presented sequentially, and it has recently been popular to design CL methods assuming the availability of some powerful, large deep network models pre-trained on big data and generalizable to downstream tasks. However,  many existing CL methods leveraging pre-trained models are not stable: Their performance is at the mercy of well-tuned hyperparameters for certain problem settings. On the other hand, many such methods do not have theoretical guarantees. In this paper, we make use of pre-trained models and introduce a simple stable CL method that is insensitive to the choice of hyperparameters, theoretically guaranteed to have small training and generalization errors, can handle hundreds of tasks, and outperforms multiple state-of-the-art methods on an array of standard datasets. Our method is inspired by classic numerical linear algebra techniques and a recent CL framework called ``ideal continual learner'', and our generalization guarantees are inspired by recent theoretical advances in benign overfitting and double descent.
\fi

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
1

### Summary
This paper proposes a method for continual learning. In this method, the singular values are continuously truncated. The authors claim that their method has theoretical guarantees as well as good practical performance.

### Strengths
The authors provided comprehensive theoretical and empirical results.

### Weaknesses
A simple baseline in continual learning is experience replay. But I did not see the authors providing the results for experience-replay-based method.

### Questions
Did the authors compare with experience replay method?

### Soundness
3

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
2

### Summary
This paper proposes a new method to address instability issues of RanPAC. Part of the contribution is a diagnosis of the cause of the instability which is attributed to the condition number of the features exploding as the number of tasks increases. The proposed method truncates the smaller singular values of the features in an online or continual way, so that it doesn't have to store all of the previous tasks samples. Effectiveness of the new method is validated empirically.

### Strengths
The problem and setup is well motivated. The results are natural and the writing is clear. The experimental results are extensive and seem significant.

### Weaknesses
It seems to me that the main contribution of this work is an algorithm for continual principal component regression, with an application to training with random features. Specially, the properties of the features that arise from pretraining, random projections and nonlinearity don't seem to matter much to the derivations theoretically. On the other hand, if I view the work mainly as an algorithm for continual principal component regression, then the guarantees given in theorems 1 and 2 are a black box, since the quantities $\gamma_t$ and $a_t$ which have an unpacked recursive form. It is not clear to me how they behave in general.

In the ICL framework of Peng et al. (2023), they are maintaining a minimum norm solution based on proof of Proposition 5 in that work where they are using the pseudoinverse. So I think the statements on top of page 3 might not be quite accurate. 


In lines 202-208 the cause of instability of RanPAC is attributed to the double descent phenomenon. I think it would be helpful to explain this more to the reader.


New notation that is used in lines 242-243 has not been introduced yet.

To judge the significance of the experimental results, it would be helpful if the reported numbers included also a measure of uncertainty.

### Questions
In the ICL framework of Peng et al. (2023), they are maintaining a minimum norm solution based on proof of Proposition 5 in that work where they are using the pseudoinverse. So I think the statements on top of page 3 might not be quite accurate. 


In lines 202-208 the cause of instability of RanPAC is attributed to the double descent phenomenon. I think it would be helpful to explain this more to the reader.


New notation that is used in lines 242-243 has not been introduced yet.

To judge the significance of the experimental results, it would be helpful if the reported numbers included also a measure of uncertainty.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a new algorithm, ICL-TSVD, designed to bridge the gap between theory and practice in continual learning (CL) with pre-trained models. It integrates an empirically strong approach RanPAC within the Ideal Continual Learner (ICL) framework. Specifically, ICL-TSVD lifts pre-trained features into a higher dimensional space, then addresses the ill-conditioning of these lifted features through continually SVD truncation, and solves the truncated form of an over-parameterized minimum-norm least-squares problem. Theoretically, it is shown that the method achieves small training and generalization error under certain conditions. Empirically, ICL-TSVD demonstrates stability across various hyperparameter settings and outperforms other CL baselines across multiple datasets.

### Strengths
1. The paper clearly demonstrates the contribution of the proposed approach and is easy to follow.

2. Extensive experiments across multiple datasets show that ICL-TSVD remains stable regarding hyperparameter selection (including regularization parameter $\lambda$ and truncation percentage $\zeta$) and consistently outperforms previous CL baselines, particularly RanPAC.

3. It provides theoretical guarantees for the proposed method ICL-TSVD by revealing a recurrence relation throughout the CL process, showing that it has small estimation and generalization errors when a suitable fraction of SVD factors are truncated.

### Weaknesses
 1. The continual Implementation of $\overline{\bf{W}}_t$ involves the computation of $\widetilde{\bf{B}}_t$, which has the form of $\widetilde{\bf{B}}_t = [\widetilde{\bf{U}}_{1:t-1}\widetilde{\bf{\Sigma}}_{1:t-1}, \widetilde{\bf{H}}_t]$ when $t\geq 2$ according to Eq. (3). Appendix C.1 briefly mentions that it is empirically found continually updating all SVD factors $\widetilde{\bf{U}}_{1:t}, \widetilde{\bf{\Sigma}}_{1:t}$ and $\widetilde{\bf{V}}_{1:t}$ lead to large test errors. However, it remains unclear why authors use $\widetilde{\bf{B}}_t = [\widetilde{\bf{U}}_{1:t-1}\widetilde{\bf{\Sigma}}_{1:t-1}, \widetilde{\bf{H}}_t]$ instead of $\widetilde{\bf{B}}_t = [\widetilde{\bf{U}}_{1:t-1}\widetilde{\bf{\Sigma}}_{1:t-1}\widetilde{\bf{V}}_{1:t-1}, \widetilde{\bf{H}}_t]$ from a theoretical perspective. What are the difference and connection between these two implementations? Why just maintaining $\widetilde{\bf{U}}_{1:t-1}$ and $\widetilde{\bf{\Sigma}}_{1:t-1}$ can serve as a substitution for all SVD factors, what is the motivation for that?

2. In Section 6.2,  ICL-TSVD chooses embedding dimension $E = 10^5$ while RanPAC uses the default choice $E=10^4$. It is not so convincing that this is a fair comparison although the authors claim that ICL-TSVD’s implementation is more scalable and more efficient than RanPAC’s. Figure 8 and Table 13 in Appendix K indeed show that ICL-TSVD does not outperform RanPAC on about half of the datasets.

3. 
  - For Theorem 1, take Figures 3 and 4 for example, the truncation percentage is set to 25%. Then based on eigenvalues vs. eigenvalue index shown in Figure 1, $a_t$ should be at least in the order of $10^5 \sim 10^6$, and $\gamma_t$ is around or slightly larger than 1. In this case, the bound for the estimation error can be very large even if the unknown ground-truth $\|\mathbf{W}_t^*\|_F^2$ and noise $\|\mathcal{E}_{1:t}\|^2$ are reasonably small, which means that the theoretical guarantee does not match with empirical results. And similar issue exists in Theorem 2 as well. 
  - Furthermore, without independent i.i.d. Gaussian vectors assumption on $\bf{h}$ and the columns of $\bf{H}_{1:t}$ (which is unrealistic for practice), we may not guarantee that $\|\Lambda - \frac{1}{M_t}\bf{H}_{1:t}\bf{H}_{1:t}^{\top}\|$ converges to 0 as $M_t\rightarrow\infty$. 

4. Figure 5 shows the comparison of training times for varying embedding dimensions $E$ between ICL-TSVD and RanPAC. How about comparison with other CL baselines in terms of training time? Typically, the computational cost of SVD-type algorithms is large, is ICL-TSVD still faster than other CL methods under the current experimental settings?

### Questions
1. In Table 2, why the final accuracy of RanPAC on StanfordCars dataset is only 1.19%? Could you provide an explanation for it?

2. Figure 5 does not plot the training time for RanPAC when embedding dimension $E = 50\mathrm{K}, 100\mathrm{K}$, is this because the training process is too slow?

3. How about the running time of ICL-TSVD compared to other CL baselines, especially those that do not utilize SVD in their implementation?

4. For original definition of $\overline{\bf{W}}_t$ in Eq. (2) and practical implementation of $\widetilde{\bf{W}}_t$ in Eq. (4), do they close to each other? In other words, is there any theoretically guarantee showing that $\\|\overline{\bf{W}}_t - \widetilde{\bf{W}}_t\\|_F$ is small in general?

**Minor issues and typos**

- In Eq. (5) of Section 5, the denominator of $\gamma_t$ should be $\max\_{1\leq i\leq t-1}\mu\_{k_{i+1}}(\widetilde{\bf{B}}_i\widetilde{\bf{B}}_i^{\top})$ instead of $\max\_{1\leq i\leq t-1}\mu\_{k\_{i}+1}(\widetilde{\bf{B}}_i\widetilde{\bf{B}}_i^{\top})$.

### Soundness
3

### Presentation
3

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
The paper tackles the problem of class-incremental learning (CIL).
To this end, the paper improves RanPAC (McDonnell et al., 2023), making it more numerically stable as a least-squares problem, by truncating small singular values from the SVD of the (pretrained) embeddings of the samples from *all* previous tasks. The truncation might also positively impact the generalization itself.
The authors link their method to a theoretical framework (ICL by Peng et al., ICML 2023) which derived sufficient conditions to preventing forgetting in linear models, and use this connection to derive some bounds on the training and generalization error of the proposed algorithm.

### Strengths
1. The proposed method seems to empirically improve upon the existing RanPAC method (McDonnell et al., NeurIPS 2023).
1. The proposed method is easy to implement.

### Weaknesses
# Major concerns

1. **Proposed analysis feels contrived.**
    To me, the analytical connection between ICL (Peng et al., ICML 2023) and the proposed method feels overly strained.
    1. To begin with, the ICL formulations presented in Line 111 and 116, are purely theoretical (formalizing a sufficient condition to prevent forgetting), and *cannot* be considered continual learning approaches, since they require storing the data from all previous tasks.
    1. In Line 105 (Eq. 1), the raw feature matrices $X_t$ are randomly mapped to the "effective" matrices $H_t=\text{relu}(PX_t)$ using a random matrix $P\in\mathbb{R}^{E\times d}$ where $E\gg d$.
To facilitate the comparison to the ICL framework, in Line 113, the authors assume that $E$ is so large that it makes the *entire* task sequence feasible (jointly!). However, for most datasets, this would practically make the time and space requirements of the proposed method infeasible. This assumption, while simplifying the analysis, does not reflect the practical constraints of continual learning.
    1. Theorem 1 also implicitly requires such extreme overparameterization or that the data can already be explained linearly almost perfectly. Otherwise, $\Vert\mathcal{E}_{1:t}\Vert$ would be large, making the bound uninformative ($\frac{M_t-k_t}{M_t}$ is not small).  
However, if the data is linearly explained by some model $W^{*}_t$, then ICL trivially obtains 0 loss (since all previous data is stored and optimized simultaneously) and all that is left to analyze is the error stemming from the truncation (which implicitly assumes that the smaller singular values are very small, which might not be the case for arbitrary data).   
In my opinion, this is **not** a significant theoretical contribution. The analysis essentially reduces to showing that truncating small singular values incurs a small loss, which is a well-known property of low-rank approximations, and the connection to ICL does not provide any additional insight.

1. **Unclear if accuracy improvements are significant.**
 It seems like the results in the main Table 1 are of a single run per model-dataset combination. No standard deviation is reported. Given that most of the improvements upon RanPAC are somewhat small, it is unclear if these are indeed statistically significant.

---

## Summary of weaknesses

 Considering all of the above, I believe the paper constitutes a nice incremental improvement over RanPAC (using truncation instead of regularization), but I am not convinced that the analysis makes the paper valuable enough for ICLR.

-----

# Minor concerns

I do not expect any response on the following concerns but I recommend addressing them in any future revised version.

1. Many times (e.g., Line 160), the authors specify constant values like $\lambda = 10^{4}$ and $\lambda = 10^{-5}$  and refer to them as being very small or very large. However, I find these references problematic since the regularization strength in least-squares problems is meaningless without taking into account the scale of the data and the fitting error. Similarly, I would even go further and say that the main benefit from the proposed method is not that it gets rid of the smallest singular values, but that it remedies the *condition number* of the matrices. The smallest singular values can only be considered "small" when comparing to the largest singular values. An alternative method could have limit the condition number instead of using a fixed percentage $\zeta$.

1. I think Figure 1c would be better if it showed the training accuracy, since this is the origin of the problem there.

1. The time complexity analysis should appear immediately after the algorithm, rather than as a side note on page 9. Space complexity should also be specified. Moreover, at some point, given enough tasks, $M_t = k_{t-1} + m_t$ can become larger than $E$, which then makes the time complexity $E^3$ (notice that the $M_t - $E$ smallest singular values are zeros), just like in RanPAC.

1. In Line 130, the authors say "the theoretical justification for the strong empirical performance of RanPAC remains limited". I kindly disagree and claim that it is trivially justified, since according to the formula in Line 124, it just minimizes *all* the losses simultaneously.

1. To be slightly more precise, step 3 in Algorithm 1 should use the floor operator $\lfloor(1-\zeta)M_t\rfloor$.

1. The paper would be more readable if the dimensions are specified when matrices are first presented, e.g., the authors should specify the dimensions of ${\widetilde{U,\Sigma,B}_{1:t}}$ in Eq. (3).

1. The sentence in Line 319 (about the values of $\delta$) is unclear.

1. The message of Figure 6 is unclear.

1. In Theorem 1, I believe $\frac{M_t-k_t}{M_t}$ is simply $(1-\zeta)$.

1. In Theorem 1, specify the subscript for the norm used for $\mathcal{E}_{1:t}$.

1. The presentation is often overcomplicated and inconsistent. For instance, in line 105 (Eq. 1), a projection matrix $P$ is introduced, while most of the analysis throughout the paper, especially in Section 5, completely ignores that matrix and deals with arbitrary deterministic feature matrices $H_t$. Moreover, I would consider presenting the ICL details only after the algorithm itself, as a retrospect.

### Questions
Other than what I wrote above,

1. I could not immediately understand why both RanPAC and the proposed method outperform the $LC(H_{1:T})$ benchmark (trained with the original cross entropy loss like explained in Appendix J). Even if the data matrices are ill-conditioned, early stopping (e.g., when performing a fixed number of steps) should create a remedying effect and help generalization. Is it possible that a better hyperparameter tuning is needed here? Did the authors check the training *and* test curves throughout the training of this competitor?

1. In Figure 4a, what is going on with the scaling of the x-axis? What was the maximal truncation percentage that you examined? I would expect seeing a sharp decrease at the for high values, but it is not apparent. Moreover, why can we truncate so much without losing performance even though the eigenvalues do not decrease so quickly (as seen from Figure 1a)?

### Soundness
2

### Presentation
3

### Contribution
2
