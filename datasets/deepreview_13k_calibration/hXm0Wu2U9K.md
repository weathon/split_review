# Correcting the Mythos of KL-Regularization: Direct Alignment without Overoptimization via Chi-Squared Preference Optimization

- Decision: Accept
- Avg Score: 6.40
- Scores: 6, 8, 6, 6, 6

## Abstract
Language model alignment methods, such as reinforcement learning from human feedback (RLHF), have
led to
impressive advances in language model capabilities, but existing
techniques are limited by a widely observed phenomenon known as
\emph{overoptimization}, where the quality of the language model
plateaus or degrades over the course of the alignment process. Overoptimization is often
attributed to overfitting to an inaccurate reward model, and while it
can be mitigated through online data collection, this is infeasible in
many settings. This raises a fundamental question: Do existing
\emph{offline} alignment algorithms make the most of the data they have, or
can their \emph{sample-efficiency} be improved further?
\loose

We address this question with a new algorithm for offline
alignment, \emph{\alglong} (\algshort).

\noindent \algshort is a one-line change to Direct Preference
Optimization (\dpo; \citet{rafailov2024direct}), which only involves
modifying the logarithmic link function in the \dpo{} objective.
Despite this minimal change, \algshort implicitly implements the
principle of \emph{pessimism in the face of uncertainty} via
regularization with the \chis-divergence---which quantifies uncertainty
more effectively than KL-regularization---and provably alleviates
overoptimization, achieving sample-complexity guarantees based on
\emph{single-policy concentrability}---the gold standard in offline
reinforcement learning. \algshort's simplicity and strong
  guarantees make it the first practical and general-purpose offline
  alignment algorithm that is provably robust to overoptimization.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work focuses on the issue of over-optimization in RLHF, where over-optimization refers to the issue of overfitting of language model to an imperfect offline reward model. Authors use the principle of pessimism in reinforcement learning to tackle the over-optimization, and they propose to replace the KL divergence-based regularization in RLHF with the more conservative $\chi^2$ divergence. A single policy concentration convergence result is derived to show the sample-efficiency of the proposed algorithm and a summarization task is used for numerical validation.

### Strengths
1. Over-optimization to offline reward model has drawn a lot of attention recently and deserves more research attention.
2. The proposed algorithm is simple to implement with a one-line change compared to the classical RLHF/DPO
3. Convergence results in terms of single policy concentration are provided and detailed comparison with DPO in terms of bias/over-optimization trade-off is provided.

### Weaknesses
Empirical evaluation is the main weakness of the paper. Authors only compare with one task (the summarization task) and one baseline method (DPO). Considering the recent large body of work studying the topic, it is desirable to compare with more baseline methods such as the 'DPO+SFT' approach. Furthermore,  the improvement of XPO compared to DPO is not significant (roughly one point when comparing the best results of the two) and XPO still suffers from over-optimization when the training epochs are increased. Finally, can you show the plots of win-logps vs epochs? Does it increase or decrease as training goes.

### Questions
Can you elaborate more in terms why the mix $\chi^2$ regularization obtains single-policy concentration while the KL regularization not? What roles the pessimism plays in the proof?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Existing offline alignment algorithms based on KL regularization, such as direct preference optimization (DPO) and DPO+SFT, suffer from reward overoptimization in experiments.
This work aims to address this issue.
The authors first observed that reward overoptimization is related to the dependence of the regret bound on the coverage coefficient.
To address this, they proposed $\chi$PO, a variant of DPO based on $\chi^2$ regularization.
This algorithm is the first general method with a sample complexity bound of $O(\sqrt{C^{\pi^\star}/n})$, where $C^{\pi^\star}$ is the coverage coefficient, $n$ is the sample size, and $\pi^\star$ is the policy to which we wish to compare.
This bound can be significantly smaller than existing bounds that depend on $\max_{\pi}C^{\pi}$.
Numerical experiments demonstrate the robustness of $\chi$PO against overoptimization.

### Strengths
I have read the main paper, Appendix A, B, C, E, F, and have skimmed through Appendix G and H.

This work is solid and generally well-written.
Related works are adequately cited.
Theoretical results are sound.
It is surprising to me that a small tweak to DPO can significantly improve the theoretical guarantee and the empirical results.
I appreciate this work.

### Weaknesses
I did not spot any major weaknesses. Below are some minor issues related to clarity.

1. In Appendix E.2, it is mentioned that $\chi$PO was not used in the experiments because it may be unstable during training. Therefore, another link function was used. I suggest mentioning this in the captions (Table 1, Figure 4, Table 2) to avoid misunderstanding and, if possible, presenting the experimental results of $\chi$PO.
2. In line 131, it should be $x \in \mathcal{X}$.
3. In line 138, it should be $y \sim \mathbb{P}(a \succ b | x)$.

### Questions
1. The explanation of the non-triviality in Section 4.3 is a bit confusing to me. My understanding is that we can use the all-policy concentrability and Assumption 3.2 to obtain a sample complexity guarantee for $\chi$PO. Nevertheless, this does not yield a guarantee based on the single-policy concentrability, so the sample complexity guarantee of $\chi$PO (Theorem 3.1) is non-trivial. Is my understanding correct?
2. The sample complexity guarantee of $\chi$PO (Theorem 3.1) has an exponential dependence on the maximal reward $R_\max$. The algorithm of Xie et al. (2024) also has this exponential dependence. Is this exponential dependence unavoidable, or can it be improved? Also, is this exponential dependence observed in experiments? 
3. The $\chi$PO algorithm uses a regularizer that combines the $\chi^2$ divergence and the KL divergence. In Theorem H.1 (a general version of Theorem 3.1), it is mentioned that we can make the weight of the KL divergence arbitrarily close to $0$ while still maintaining the sample complexity guarantee. As the weight of the KL divergence decreases to $0$, does the empirical performance of $\chi$PO improve?
4. Following question 3, I wonder if the algorithm and the proof would still hold if we removed the KL divergence. Furthermore, does this suggest that the technical assumption $0 \notin \text{dom}(f')$ in Wang et al. (2023) might be removable?

References:
- T. Xie et al. Exploratory preference optimization: Harnessing implicit Q*-approximation for sample-efficient RLHF. *arXiv*, 2024.
- C. Wang et al. Beyond reverse KL: Generalizing direct preference optimization with diverse divergence constraints. *arXiv*, 2023.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies overoptimization problem in RLHF where language models trend to overfit to the learned reward model which often results in degraded performance. The authors analyze the weaknesses of commonly used KL regularization from RL theoretic perspectives and claim its insufficiency to prevent overoptimization. 
They propose to replace KL regularization with $\chi^2$-regularization to achieve theoretical guarantees on single-policy concentrability. Finally, the authors derive a variant of offline alignment objective function using $\chi^2$-regularization with minimal change to DPO.

### Strengths
- The proposed $\chi$PO algorithm and its theoretical analysis are novel contributions to alleviate overoptimization issue for offline alignment. 
- $\chi$PO has better provable robustness to overoptimization and well-supported by empirical experiments.
- The theoretical analysis of $\chi$PO and its properties is sound and comprehensive.

### Weaknesses
 - In addition to the comprehensive and rigorous analysis, it could be great to support the claim with more empirical experiments. For example, it would be nice to add additional benchmarks (e.g., MMLU, GSM8K) against common baselines (e.g. DPO, KPO) for empirical validations.
- As offline alignment has recently been rapidly growing, the empirical experiments could include a few more latest baselines (e.g. DPO, KPO, IPO, ...) with ablations over key hyperparameters such as $\beta$.
- As a comment: I think it would be nice to have experiments in Appendix E.2 included in main text more extensively for broader audience.

### Questions
- Although the paper explains the necessity from theoretical perspective to include KL term in mixed regularization, what would be the practical implications to have only $\chi^2$ regularization? How about a comparison among PPO-Mix (paper), PPO-KL (standard RLHF), and PPO-Chi for online setting to validate how well the theory and practice are matching. 
- What would be training dynamics between two divergence regularizers? How separate coefficient would affect the interaction between KL and $\chi^2$ regularizers?
- More broadly, in standard RL policy optimization, PPO-Clip objective also does not have log-term. Could there be a meaningful link between $\chi^2$ regularization in general policy optimization? e.g. utilize $\chi^2$-divergence to constraint trust region during policy optimization.

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
3

### Summary
This paper introduces Chi-Squared Preference Optimization ($\chi$PO) as an alternative to KL-based regularization in preference alignment. $\chi$PO replaces the KL divergence with Chi-Squared divergence, leveraging its ability to better quantify uncertainty and provide stronger, more reliable regularization against overoptimization. The authors demonstrate that $\chi$PO aligns language models more effectively by enhancing sample efficiency and robustness, grounded in single-policy concentrability—a key offline reinforcement learning standard. This theoretical shift offers a novel perspective on controlling overoptimization, simplifying the DPO framework with a mathematically sound alternative that generalizes well across alignment tasks.

### Strengths
1. $\chi$PO provides stronger regularization than KL-divergence by better accounting for uncertainty, thus significantly reducing the risk of overoptimization when aligning language models with human preferences. 

2. $\chi$PO achieves sample-complexity guarantees through single-policy concentrability, meaning it requires fewer samples to achieve reliable performance, making it particularly effective in offline alignment tasks.

3. The approach requires minimal modifications to the DPO framework, making it both practical and easy to implement in existing systems.

4. By grounding $\chi$PO in well-established principles from offline reinforcement learning, the authors provide a robust theoretical foundation that enhances the credibility and potential generalizability of the method.

### Weaknesses
1. Limited empirical validation: The paper only provide theoretical insights, not sure about the gap between the analysis and the real practice.

2. The gap between theoretical/implementable algorithm: the additional KL term for KKT.

### Questions
1. In order to obtain the practical algorithm, the authors added the KL term, do you have more explanation about the gap and more intuitions to deliver the implementable algorithm?

2. Have you tried to perform empirical experiments?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes a simple variant of DPO called $\chi$PO, by adding $\chi^2$-divergence regularizer to DPO to encourage pessimism, and proves that $\chi$PO has improved generalization error bound of DPO with all-policy concentrability replaced by single-policy concentrability.

### Strengths
Adding $\chi^2$ divergence is novel in DPO. Theorem 3.1 well supports the good generalization ability of $\chi$PO, and it also does not require convex set assumption in existing pessimistic approach called DPO+SFT. The presentation before Section 4 is clear.

### Weaknesses
Some points could be clarified as listed in the questions below. The experiments only demonstrate the advantage of $\chi$PO over DPO but not DPO+SFT.

(1) $\widehat{\pi}$ is defined by different objective functions (7) and (9). However, it seems that only (9) is used for algorithm, Theorem 3.1 and analysis in Section 4. Is it more clear to only introduce (9) not (7), and state your novelty as adding $\chi^2$-divergence to the original DPO objective, not replacing the KL divergence?

(2) You could give the full name of "SFT" at its first appearance.

(3) At the end of Section 2.1, I think (4) is $-\infty$ if $\pi(a_+|x)\ll\pi _ {\rm ref}(a_+|x)$ for some data point $x,a_+$.

(4) In Eq. (5), is $n$ the size of $\mathcal{D}_{\rm off}$?

(5) Theorem H.1 (General version of Theorem 3.1) and Corollary 3.1 seem to use the same choice of $\beta$ relying on $\pi^*$. In this case, I am not sure why do we need Corollary 3.1?

(6) You could define $\mathcal{C}_{\infty}^{\pi}$ at its first appearance.

(7) At the beginning of Section 4.3, why can Assumption 3.2 about two-point difference imply single-point bound $\big\|\frac{\pi}{\pi _ {\rm ref}}\big\| _ {\infty} \lesssim \frac{V _ {\max}}{\beta}$ for all $\pi\in\Pi$?

(8) In line 507, should it be $\frac{\pi_{\beta;{\rm KL}}^{\star}(a \mid x)}{\pi_{\rm ref}(a \mid x)} \gtrsim \exp\big(-\frac{R_{\max }}{\beta}\big)$ (as you said in line 449)? If so, the optimal mixed $\chi^2$-regularized policy also has this lower bound and thus also cannot simultaneously satisfy the two properties you said in line 509 (change the second to $\exp\big(-\frac{R_{\max }}{\beta}\big)$).

(9) Is Section 4.3 necessary, as it seems to only give a looser bound than Theorem 3.1 which already shows the better generalization ability of $\chi$-PO over DPO by replacing $\max_{\pi\in\Pi}\mathcal{C}^{\pi}$ with $\mathcal{C}^{\pi^*}$? Also, I feel it will be more clear to conclude the benefits of $\chi$-PO over DPO, for example, at the beginning or end of Section 4 or its subsections.

(10) About experiments: The link function $\tilde{\phi}(z):=\exp \big(\operatorname{clip} _ {[-88,20]}(\alpha \cdot z)\big)+\gamma\log z$ looks far away from $\phi$ since $\exp \big(\operatorname{clip} _ {[-88,20]}(\alpha \cdot z)\big)$ is exponential in a large range $[-88,20]$ which is far away from $z$. Since you said $\tilde{\phi}(z)$ is has better stability and performance in practice, do you think we can obtain its generalization bound? It is also better to compare with existing pessimistic approaches such as DPO+SFT. Also, in Section E.2, we could use $\alpha\in${$\frac{1}{4},1$} and $\gamma\in${$0.1,1$}.

### Questions
(1) $\widehat{\pi}$ is defined by different objective functions (7) and (9). However, it seems that only (9) is used for algorithm, Theorem 3.1 and analysis in Section 4. Is it more clear to only introduce (9) not (7), and state your novelty as adding $\chi^2$-divergence to the original DPO objective, not replacing the KL divergence? 

(2) You could give the full name of "SFT" at its first appearance. 

(3) At the end of Section 2.1, I think (4) is $-\infty$ if $\pi(a_+|x)\ll\pi _ {\rm ref}(a_+|x)$ for some data point $x,a_+$. 

(4) In Eq. (5), is $n$ the size of $\mathcal{D}_{\rm off}$? 

(5) Theorem H.1 (General version of Theorem 3.1) and Corollary 3.1 seem to use the same choice of $\beta$ relying on $\pi^*$. In this case, I am not sure why do we need Corollary 3.1? 

(6) You could define $\mathcal{C}_{\infty}^{\pi}$ at its first appearance. 

(7) At the beginning of Section 4.3, why can Assumption 3.2 about two-point difference imply single-point bound $\big\|\frac{\pi}{\pi _ {\rm ref}}\big\| _ {\infty} \lesssim \frac{V _ {\max}}{\beta}$ for all $\pi\in\Pi$? 

(8) In line 507, should it be $\frac{\pi_{\beta;{\rm KL}}^{\star}(a \mid x)}{\pi_{\rm ref}(a \mid x)} \gtrsim \exp\big(-\frac{R_{\max }}{\beta}\big)$ (as you said in line 449)? If so, the optimal mixed $\chi^2$-regularized policy also has this lower bound and thus also cannot simultaneously satisfy the two properties you said in line 509 (change the second to $\exp\big(-\frac{R_{\max }}{\beta}\big)$). 

(9) Is Section 4.3 necessary, as it seems to only give a looser bound than Theorem 3.1 which already shows the better generalization ability of $\chi$-PO over DPO by replacing $\max_{\pi\in\Pi}\mathcal{C}^{\pi}$ with $\mathcal{C}^{\pi^*}$? Also, I feel it will be more clear to conclude the benefits of $\chi$-PO over DPO, for example, at the beginning or end of Section 4 or its subsections. 

(10) About experiments: The link function $\tilde{\phi}(z):=\exp \big(\operatorname{clip} _ {[-88,20]}(\alpha \cdot z)\big)+\gamma\log z$ looks far away from $\phi$ since $\exp \big(\operatorname{clip} _ {[-88,20]}(\alpha \cdot z)\big)$ is exponential in a large range $[-88,20]$ which is far away from $z$. Since you said $\tilde{\phi}(z)$ is has better stability and performance in practice, do you think we can obtain its generalization bound? It is also better to compare with existing pessimistic approaches such as DPO+SFT. Also, in Section E.2, we could use $\alpha\in${$\frac{1}{4},1$} and $\gamma\in${$0.1,1$}.

### Soundness
2

### Presentation
2

### Contribution
3
