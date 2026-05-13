# The Crucial Role of Samplers in Online Direct Preference Optimization

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Direct Preference Optimization (DPO) has emerged as a stable, scalable, and efficient solution for language model alignment.
Despite its empirical success, the \emph{optimization} properties, particularly the impact of samplers on its convergence rates, remain underexplored.
In this paper, we provide a rigorous analysis of DPO's \emph{convergence rates} with different sampling strategies under the exact gradient setting, revealing a surprising separation: uniform sampling achieves \emph{linear} convergence, while our proposed online sampler achieves \emph{quadratic} convergence.
We further adapt the sampler to practical settings by incorporating 
posterior distributions and \emph{logit mixing}, demonstrating significant improvements over previous approaches.
On Safe-RLHF dataset, our method exhibits a $4.5\%$ improvement over vanilla DPO and a $3.0\%$ improvement over on-policy DPO;  on Iterative-Prompt, our approach outperforms vanilla DPO, on-policy DPO, and Hybrid GSHF by over $4.2\%$.
Our results not only offer insights into the theoretical standing of DPO but also pave the way for potential algorithm designs in the future.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper titled "The Crucial Role of Samplers in Online Direct Preference Optimization" explores Direct Preference Optimization (DPO) for aligning language models (LMs) with human preferences. While DPO is recognized for stability and efficiency, the authors focus on its convergence properties under different sampling methods. The study reveals that standard uniform sampling achieves only linear convergence, while their proposed samplers (DPO-Mix-R and DPO-Mix-P) attain faster, quadratic convergence. These findings are validated through experiments on the Safe-RLHF and Iterative-Prompt datasets, where the proposed methods outperform traditional DPO and on-policy sampling, showing improvements in model alignment with human preferences.

### Strengths
1. Theoretical Rigor: The authors provide a comprehensive theoretical analysis of DPO convergence with various samplers, adding clarity to an underexplored aspect of preference optimization.

2. Practical Enhancements: The proposed samplers improve DPO's performance, demonstrating notable advantages over baseline approaches on empirical datasets.

3. Insightful Implications: The work not only proposes new samplers but also reinterprets existing DPO methods within their framework, offering a broader understanding of optimization in language model alignment.

### Weaknesses
1. The experiments are not valid enough to test the performance of their method. First, in Table 2, the model is scored by the same reward function used for the training set. In this way, the improvement is likely to come from overfitting. Hence, I suggest the authors to test their performance by using gpt-4o.

2. The analysis lacks the intuition of the specific choice of the mixed sampler, such as why in Line 226, $\pi^s1$ and $\pi^s2$ should have the form of $\exp(r)$ and $\exp(-r)$. Is the way of mixed sampler optimal? The authors should provide more intuitions and interpretation.

3. The contribution of this work to RLHF may not be significant enough since the improvement is not so obvious based on the weakness point 1.

### Questions
1. For empirical DPO, how to compare the efficiency with the uniform DPO since the empirical DPO is the practical one.The paper titled "The Crucial Role of Samplers in Online Direct Preference Optimization" explores Direct Preference Optimization (DPO) for aligning language models (LMs) with human preferences. While DPO is recognized for stability and efficiency, the authors focus on its convergence properties under different sampling methods. The study reveals that standard uniform sampling achieves only linear convergence, while their proposed samplers (DPO-Mix-R and DPO-Mix-P) attain faster, quadratic convergence. These findings are validated through experiments on the Safe-RLHF and Iterative-Prompt datasets, where the proposed methods outperform traditional DPO and on-policy sampling, showing improvements in model alignment with human preferences.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies online DPO where the sampling schemes for the two completions on the same prompt are different, from an optimization perspective. The theoretical conclusion is that a class of mixed samplers can achieve quadratic convergence, as compared with standard sampling methods with linear convergence. The authors then develop a new mixed sampling scheme for practice and demonstrate empirically that it improves the previous methods.

### Strengths
1. By developing a general framework of mixtures of heterogeneous sampling strategies, the paper can unify some existing methods.
2. The theoretical results show a separation in convergence rates that is quite unexplored in this area.
3. Empirical evaluations seem to align with theoretical results, showing that the analysis in this paper is promising in improving RLHF.,

### Weaknesses
1. The mixed samplers in definition 4&5 differ from standard samplers in two aspects: first they consider a heterogenous sampling scheme (enhancer) that increases the difference between the positive completion and the negative completion, second they mix the heterogenous sampling scheme with the standard (homogenous) sampling scheme using some nontrivial  mixing coefficient. In the theoretical study, it is shown that the two aspects combined have certain benefits. However, overall there is a lack of analysis of the contributions from each individual aspect. In a certain sense, this weakness diminishes the convincingness of the theory and limits its usage in practice. Certain ablation studies or analyses that isolate the effects of the heterogeneous sampling scheme and the mixing strategy separately would resolve this concern.
2. While I largely agree with table 2, there are still some gaps between the theoretical samplers in definition 4&5 and the practical ones. In particular, the first sampler in definition 4&5 are uniform over Y, but in practice no-one would use uniform distributions. Moreover, the mixing coefficients $\alpha_2,\alpha_2$ are set somewhat ad hoc but without explanation. The practical samplers use $\pi_\theta^{2\beta}$ as a posterior distribution, which is not explicitly justified by the theory. This discrepancy between the theoretical setup and the practical implementation raises concerns about the direct applicability of the theoretical results.
3. The main theoretical result is in the exact setting, which is a bit far from practice. The analysis assumes access to the exact gradient, which is not available in practical scenarios where stochastic gradients are used. This limits the direct applicability of the theoretical convergence rates to real-world DPO training.
4. There is a lack of explanation/justification of the results of the LLM experiments. In table 2 & 3, the improvements in rewards and win-rate appear to be modest. Combining figure 2, it can be observed that the benefit of the proposed method mostly occurs in later iterations, or equivalently, in the large KL-divergence regime. It then brings the question of whether the model overfits to the reward model and whether the comparison is fair. See the question section for more comments.

### Questions
1. What are the individual contributions of (1) choosing a heterogenous sampling scheme (enhancer), and (2) mixing the heterogenous sampling scheme with the standard (homogenous) sampling scheme?
2. Any insights of the choice of mixing coefficients $\alpha_2,\alpha_2$?
3. What would the convergence rates be when replacing the uniform distributions in definition 3,4,5 with $\pi^\theta$?
4. Could you explain what do you mean by 'concentrate on responses with high probabilities ...' in line 392-395? 
5. Is win-rate evaluated on human, gpt or reward model?
6. In Figure 2: the proposed method outperforms baselines only in large KL divergence. Why? Is this a fair comparison, given that vanilla DPO doesn't reach such high KL in figure 2?

### Soundness
2

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
4

### Summary
This is a theoretical paper concerned with the performance of the Online DPO algorithm for alignment/RLHF. Online DPO iteratively alternates between (i) fitting a new language model/policy with DPO on the current dataset, and (ii) gathering new feedback and expanding the dataset by sampling response pairs from the trained model/policy. In its original form, online DPO samples both responses in the pair directly from the trained policy. The main point of this paper is to investigate the impact of different sampling strategies on the convergence of the algorithm. The authors show the following results for a simplified "bandit" setting where there are no contexts and the response space is small/finite.

- In the absence of statistical errors ("exact DPO"), uniform sampling converages at a linear rate (which the authors prove is tight), whereas two non-trivial sampling strategies the authors propose ("DPO-Mix-R" and "DPO-Mix-P"), which involve mixing the learned policy based on a reward model or reference policy, achieve faster quadratic convergence.
- With statistical errors, DPO-Mix-R and DPO-Mix-P still converge to the noise level at a linear rate.

The authors also support these theoretical findings with empirical results.

### Strengths
The problem the authors study in this paper is an important and timely one. The setting in the paper (essentially finite-armed bandits) is admittedly very stylized, but I found the theoretical results to be interesting and non-trivial, and I can imagine that they might serve as a useful starting point to study tradeoffs around sampling in online alignment for more complex/challenging settings. I generally found the paper to be well-written and easy to follow.

### Weaknesses
The main limitations of the paper concern the simple/stylized nature of the bandit setting the authors study.

- The authors restrict their attention to the setting where the response space is small/finite, which allows for uniform sampling, and neglects the problem of *exploration*, which is critical for large response spaces. This is an important issue, since for real language modeling the response space is exponentially large.

- The authors, by focusing on the bandit setting, do not consider issues around generalization and function approximation---whether across contexts/prompts or across responses.

Due to the simplifications above, it is unclear whether any of the conclusions in the paper extend to more realistic settings. While I agree that studying the stylized setting in the paper is a useful starting point, it would be useful to at least include some more discussion around the question of whether the insights in the paper extend.  

Regarding the experiments: It would be useful to see some errors bars/confidence bounds to get a sense for whether the improvement the authors find is significant.

### Questions
See comments above:
1) Can the authors comment on whether the theoretical findings can extend to settings with large action spaces or settings with function approximation
2) Can the authors comment on confidence intervals for tables 2 and 3?

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
2

### Summary
This paper provides DPO's convergence rates with different sampling strategies under the exact gradient setting, and proves that uniform sampling achieves linear convergence while the proposed online sampler achieves quadratic convergence. Then this paper adapts the sampler to practical settings by incorporating posterior distributions and demonstrates significant improvements over previous approaches.

### Strengths
DPO is a very popular and important topic. The perspective of sampling strategy looks novel. The claimed quadratic convergence looks significant and impressive.

### Weaknesses
The presentation is very unclear. The unclear points are listed below.

(1) At the end of Section 3.1, should $\theta$ and $\pi_{\theta}$ also depend on $x$? In that case, we have $\theta\in\mathbb{R}^{\mathcal{X}\times\mathcal{Y}}$ with entries $\theta_{x,y}$.

(2) In Definition (1), what is the expression of the stopping-gradient operator $sg$? Could you provide an intuitive explanation about why we use $\pi^s(y,y')$? "The sampling coefficient $\alpha$ is for the purpose of comparing different sampling regimes", do you mean to compare $\pi^{\rm s1}$ and $\pi^{\rm s2}$? Does Eq. (4) implicitly include expectation over prompt $x$?

(3) In Definition (2), does $G^{(t)}\in\mathbb{R}^{|\mathcal{Y}|}$ and is $G_y^{(t)}$ the $y$-th entry of $G^{(t)}$? It is better to explain the distribution of $G_y^{(t)}$. For example, is $G_y^{(t)}$ the true gradient plus sub-Gaussian noise scaled by $\beta A$? Why do you use sub-Gaussian noise instead of Gaussian noise?

(4) Could you provide an intuitive explanation why we select $\pi^{s1}$ and $\pi^{s2}$ in Definitions 4 and 5?  

(5) The derivation of (6) looks non-trivial and thus could be proved in the main text or the appendix. 

(6) What does parameter difference (y-axis) mean in Figure 1?

(7) What is the range of $\xi_R$ in the Taylor expansion right below Theorem 2? You could indicate in the paper.

(8) What are the choices of $\alpha_1,\alpha_2,\eta$ in your experiments? You could add to your paper. 

(9) In the paragraph "Setting the posterior", what do posterior and its corresponding prior and likelihood mean? Do you intend to use $\pi_{\theta}^{2\beta}$ to approximate $\pi^*$. The derivation looks vague to me. Also, does Eq. (8) provide $\alpha_1:\alpha_2$?

You said $h(\theta)=sg\big[f(\theta)\big]\cdot g(\theta)$ means $\nabla_{\theta}h(\theta)=f(\theta)\cdot \nabla_{\theta} g(\theta)$.

Based on that, the definition of $\pi^s(y,y')={\rm sg}\big[\pi^{\rm s1}(y)\pi^{\rm s2}(y')+\pi^{\rm s1}(y')\pi^{\rm s2}(y)\big]$ in Definition (1) still looks vague.

I cannot find stopping gradient operator by both Google and AI search. They all refer to the criterion of when to stop (stochastic) gradient descent algorithm, which seems far from your definition.

**Could you write down explicitly the definition of $\pi^s(y,y')={\rm sg}\big[\pi^{\rm s1}(y)\pi^{\rm s2}(y')+\pi^{\rm s1}(y')\pi^{\rm s2}(y)\big]$ in both comment and edited paper (can be uploaded now)? The most reasonable guess I can think of is $\pi^s(y,y')=\big[\pi^{\rm s1}(y)\pi^{\rm s2}(y')+\pi^{\rm s1}(y')\pi^{\rm s2}(y)\big]/2$ as the integral of each policy is 1, right? This is important as Definition 1 is the basis of this paper.**

### Questions
(1) At the end of Section 3.1, should $\theta$ and $\pi_{\theta}$ also depend on $x$? In that case, we have $\theta\in\mathbb{R}^{\mathcal{X}\times\mathcal{Y}}$ with entries $\theta_{x,y}$. 

(2) In Definition (1), what is the expression of the stopping-gradient operator $sg$? Could you provide an intuitive explanation about why we use $\pi^s(y,y')$? "The sampling coefficient $\alpha$ is for the purpose of comparing different sampling regimes", do you mean to compare $\pi^{\rm s1}$ and $\pi^{\rm s2}$? Does Eq. (4) implicitly include expectation over prompt $x$? 

(3) In Definition (2), does $G^{(t)}\in\mathbb{R}^{|\mathcal{Y}|}$ and is $G_y^{(t)}$ the $y$-th entry of $G^{(t)}$? It is better to explain the distribution of $G_y^{(t)}$. For example, is $G_y^{(t)}$ the true gradient plus sub-Gaussian noise scaled by $\beta A$? Why do you use sub-Gaussian noise instead of Gaussian noise? 

(4) Could you provide an intuitive explanation why we select $\pi^{s1}$ and $\pi^{s2}$ in Definitions 4 and 5?  

(5) The derivation of (6) looks non-trivial and thus could be proved in the main text or the appendix. 

(6) What does parameter difference (y-axis) mean in Figure 1?

### Soundness
3

### Presentation
2

### Contribution
2
