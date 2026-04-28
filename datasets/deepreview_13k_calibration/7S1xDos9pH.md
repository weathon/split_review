# Generalized Gaussian Temporal Difference Error for Uncertainty-aware Reinforcement Learning

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 8, 3

## Abstract
Conventional uncertainty-aware temporal difference (TD) learning methods often rely on simplistic assumptions, typically including a zero-mean Gaussian distribution for TD errors. Such oversimplification can lead to inaccurate error representations and compromised uncertainty estimation. In this paper, we introduce a novel framework for generalized Gaussian error modeling in deep reinforcement learning, applicable to both discrete and continuous control settings. Our framework enhances the flexibility of error distribution modeling by incorporating additional higher-order moment, particularly kurtosis, thereby improving the estimation and mitigation of data-dependent noise, i.e., aleatoric uncertainty. We examine the influence of the shape parameter of the generalized Gaussian distribution (GGD) on aleatoric uncertainty and provide a closed-form expression that demonstrates an inverse relationship between uncertainty and the shape parameter. Additionally, we propose a theoretically grounded weighting scheme to fully leverage the GGD. To address epistemic uncertainty, we enhance the batch inverse variance weighting by incorporating bias reduction and kurtosis considerations, resulting in improved robustness. Extensive experimental evaluations using policy gradient algorithms demonstrate the consistent efficacy of our method, showcasing significant performance improvements.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors consider uncertainty estimation in TD learning and seek to generalize the conceptually simple and implicit Gaussian assumption behind the MSE loss. To do so, they consider  the generalized gaussian distribution, which has an additional shape parameter that can modulate heavy/light tailedness for the errors. The authors extend a previous approach to estimating uncertainty in TD learning to include an additional network to predict the kurtosis/shape parameter.

Edit: updated my score after reviewing the author replies.

### Strengths
- Effective uncertainty estimation is an important problem for RL and the authors study a valid relaxation of commonly held simplifying assumptions around Gaussianity.
- The authors conduct an experimental study that shows plausible benefits of the proposed generalizations in simple environments

### Weaknesses
 - There appear to be several ways to generalize the Normal distribution to have different tail behaviors, for example see q-Gaussian for yet another alternative. In the tradeoff between simplicity and more expressive modeling, it is unclear what is the right axis to explore. Even more generally, all of these are unimodal, symmetric (i.e. zero skew) distributions and arguably one could consider a full return distribution as well. In fact, prior work on distributional RL has explored this (https://arxiv.org/abs/1707.06887).

 - In terms of the learning algorithm, the paper modifies the loss function proposed in [Mai et al 2022] to the GGD case aided with an additional predictor for the kurtosis (the beta term).

 - The empirical results are mostly within error bars of the baselines. This seems especially so, when considering the marginal benefits in going from a basic uncertainty modeling with the gaussian assumption to the extra parameter estimation. Considering that this involves a whole extra network (not just an extra hyper-parameter) to predict the beta, this seems like a much more complex method for relatively little gain.

 - The tailedness of the distribution seems like a very sensitive parameter to estimate, and sensitive to simple reward transformations and/or clipping so I would be surprised if these observations are robust to such changes.

### Questions
- It seems like the distribution associated with environment transition stochasticity could easily lead to multi modal distributions of the cumulative return, which might be a much more interesting/important aspect than estimating the shape of a unimodal distribution better. Please address whether you observed any evidence of multimodality in your empirical results, and if so, how your method handles or could be extended to handle such cases.

- Rewards are typically bounded, so I would expect any estimation of the tail behavior to be quite sensitive to various practical assumptions. Please describe any preprocessing steps applied to the rewards, and how the performance varies with different reward scales or bounds.

- Given that your method requires predicting an extra head for the beta/kurtosis parameter, and training this (see Equation (4)) requires gradient descent through the gamma function of the output, how stable is the learning and/or optimization?  Please consider providing empirical evidence of the optimization stability, such as plots of the beta parameter estimates over time, or  discuss any specific techniques used to ensure stable training.

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
3

### Summary
The paper presents a novel framework for generalized Gaussian error modeling in uncertainty-aware temporal difference (TD) learning. It critiques conventional methods that assume a zero-mean Gaussian distribution for TD errors, leading to inaccurate uncertainty estimations. The proposed framework incorporates higher-order moments, specifically kurtosis, to enhance error modeling in reinforcement learning.

### Strengths
1. The paper offers a closed-form expression demonstrating the relationship between uncertainty and the generalized Gaussian distribution's shape parameter, adding depth to the theoretical framework.
2. The framework's applicability to both discrete and continuous control settings makes it relevant across various reinforcement learning contexts.
3. The emphasis on data-dependent noise and aleatoric uncertainty is timely and important for improving the robustness of reinforcement learning algorithms.

### Weaknesses
1. The introduction of higher-order moments may complicate the implementation in practical scenarios, which could deter application by practitioners.
2. In Figure 5, the return curves of Ant, HalfCheetah, and Humanoid are still increasing at the end of training step. The training steps can be increased to compare the final performances when all algorithms are converged.

### Questions
What specific tasks or environments in the real world do the authors envision as most beneficial for applying their method?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this work, the authors present a method to estimate uncertainty based on the Generalized Gaussian Distribution (GGD) to better characterize temporal difference error (TD-error) distributions. Unlike previous work, which assumes Gaussianity, the GGD captures additional parameters, specifically kurtosis, to account for higher-order moments, thus enhancing the description of the TD-error distribution. The authors then modify an existing algorithm to operate under GGD assumptions, demonstrating improved performance across various settings. They also provide theoretical guarantees for well-behaved probability density function optimization under GGD assumptions and offer insights into why their proposed method is effective.

### Strengths
- (S1): The authors provide strong motivation for improving uncertainty-aware reinforcement learning (RL), it is an active area with relevance in applications like risk-averse decision-making, managing the exploration-exploitation trade-off, and enhancing sample efficiency.

- (S2): They conduct extensive experimentation, including ablation studies and parameter sweeps, to demonstrate that their proposed method outperforms the baseline (the original uncertainty-aware method).

- (S3): The proposed method is supported by theoretical validations and guarantees. Additionally, the proofs and mathematical analyses are well-documented in the appendix, making them relatively straightforward to follow.

### Weaknesses
 - (W1): The writing of the paper could be significantly improved. Many concepts and terms are used in the main text without proper definitions, making it difficult to follow.

- (W2): Some important aspects of the proposed method are not well-developed and are instead left to references from the baseline method. While this approach is generally acceptable, in this case, understanding key elements like the inclusion of GGD and the consideration of uncertainty during training requires substantial familiarity with the referenced material. As a result, the text is not self-contained, and combined with the clarity issues, makes the main content challenging to understand.

- (W3): Although extensive experimentation demonstrates the effectiveness of the proposal, some results are counterintuitive. There is also insufficient exposition of the proposed method’s inner workings and its differences from the baseline, for which performance plots alone are insufficient.

### Questions
- Q1: Related to W1 and W2, what is the intuition behind Equation 3? In the original paper (Mai et al., 2022), this is Equation (10), which is preceded by a detailed explanation of many complex terms in the equation. As it stands, I do not think the main text is self-contained, as it requires substantial prior knowledge of that specific reference.

- Q2: How are ensembles used in this method? Ensembles are mentioned, but there is no explanation of how they are applied. Is this related to the variance in epistemic uncertainty estimation in the regularization term?

- Q3: How does the regularization term capture epistemic uncertainty (as the uncertainty that can be reduced through learning)?

- Q4: In Equation 4, how are risk-averse weights introduced? Was this derived from the inclusion of GGD in Mai et al. (2022), or was it manually designed to incorporate risk sensitivity?

- Q5: Why is estimating only beta sufficient to account for uncertainty compared to variance? Since the GGD has three parameters, with the first two set to 0 and 1 respectively, how can variance and kurtosis be represented simultaneously by a single number, beta? If I understand correctly, variance and kurtosis can be derived from beta (and alpha, in the case of variance). How do both quantities vary for a fixed alpha and a changing beta? There may be a range of TD-error distributions that cannot be fully described by just beta, which could potentially decrease the agent's performance.

- Q6: If Equation 4 holds, why does optimizing for both alpha and beta jointly decrease the agent’s performance, as shown in Figure 15?

- Q7: If considering higher moments of the TD-error distribution improves performance, does this mean that greater improvements are seen in tasks where TD-error tails are larger or smaller? How does performance compare to the evolution of the moments in the observed TD-errors? Does this method show a greater improvement over the baseline when higher-order moments are more or less pronounced?

- Q8: Typo in lines 198 and 987, and the font size of labels and ticks in figures could be increased significantly to facilitate reading.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Instead of Gaussian distribution, this paper applies generalized Gaussian distribution (GGD) to model temporal difference (TD) error, and proposes an uncertainty-aware objective function to minimize the TD error. It discussed several properties of the GGD distributions and empirically the proposed objective can work better than some baselines on common benchmark RL problems.

### Strengths
- Discussion on some advantageous properties of GGD modelling
- Empirical success with the proposed objective

### Weaknesses
The main problem with the current paper is its presentation, especially the lack of motivation for the objective function.

1. Fig.2 requires further clarification. It is surprising to see that, for example, the Gaussian fitted PDF is so different from the empirical histogram for Ant-v4 (see also the MountainCar-v0 in Fig.7(d) for a more obvious mismatch). For Hopper-v4, the standard deviations of the two Gaussians are very close to each other despite the empirical histograms having very different shapes. More importantly, this figure is about the distribution of ALL TD errors across state-action pairs, while the NLL objective is about the underlying distribution of ONE single state-action pair. For this figure to make sense, one needs to assume that all TD errors come from the same underlying distribution, which doesn’t seem to be the case as Eq.(4) uses different betas for different step t. The mismatch between the fitted Gaussian and empirical distributions, particularly the underestimation of the tails, suggests that the Gaussian assumption is fundamentally flawed for modeling TD errors, and the justification for using GGD is not sufficiently supported by this figure.

2. L273 offers a hypothesis, which is unverified. How do we define “unexpected states and rewards” and could you provide empirical support for this? Similarly, the explanation of interplay is unsatisfactory for the paragraph in L278. No evidence to support claims like “As training advances, aleatoric errors tend to become more influential while epistemic uncertainty diminishes, potentially resulting in non-normally distributed errors with heavier tails.” The paper needs to provide a more rigorous definition of 'unexpected states and rewards' and provide concrete evidence, such as plots of the TD error distribution over training, to support the claim that these errors become more heavy-tailed as training progresses. The current explanation lacks the necessary depth to be convincing.

3. It remains unclear how Thm.2 can lead to the specific weighting in Eq.(4). A detailed derivation would be helpful. Similarly, it is unclear why Eq.(8) can address the bias issue mentioned in L332. The current paper has too many hand-wavy arguments without sufficient rigorous discussions. The connection between the stochastic dominance property in Thm.2 and the weighting scheme in Eq.(4) is not clear. The paper needs to provide a step-by-step derivation that shows how the risk-averse weighting is derived from the theorem. The justification for Eq.(8) is also weak, and the paper should provide a more detailed explanation of how the proposed weighting addresses the bias issue.

4. Finally, it seems that all theoretical properties in the current paper are stemmed from prior work, as shown by the reference in every theorem/proposition. If this is indeed the case, then what would be the main theoretical contribution of the current paper, other than an application of an existing tool (GGD) to TD learning?

### Questions
1. Please explain further why the Gaussian fits in Fig.2 are very off, and why looking at the TD errors of all examples can justify the underlying GGD assumption as discussed above.

2. How can Thm.2 lead to the specific weighting in (4)?

3. What is the main theoretical contribution of this work?

### Soundness
3

### Presentation
1

### Contribution
2
