# Optimal Transport for Reducing Bias in Causal Inference without Data Splitting

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
Causal inference seeks to estimate the causal effect given a treatment such as a kind of medicine or the dosage of a medication. To address the issue of confounding bias caused by the non-randomized treatment assignment on samples, most existing methods reduce the covariate shift between subpopulations receiving different values of treatment. However, these methods split training samples into smaller groups, which cuts down the number of samples in each group, while precise distribution estimation and alignment highly rely on a sufficient number of training data. In this paper, we propose a distribution alignment paradigm that involves all the training samples without data splitting, which can be naturally applied in the settings of binary and continuous treatments. To this end, we characterize the distribution shift by considering different probability measures of the same set including all the training samples, and reduce the shift between the marginal covariate distribution and the conditional covariate distribution given a treatment value. By doing this, data reduction caused by splitting is avoided, and the outcome prediction model trained on samples receiving one treatment value can be generalized to the entire population. In specific, we exploit the optimal transport theory built on probability measures to analyze the confounding bias and the outcome estimation error, which motivates us to propose a balanced representation learning method for causal inference of binary and continuous treatments. The experimental results on both binary and continuous treatment settings demonstrate the effectiveness of the proposed method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper suggests the use of a novel estimator of conditional average treatment effects and related causal objects when there is confounding explained by observable covariates. The method can be adjusted to allow for continuous treatments as well as discrete treatments. The proposed methods employ a particular adjustment for covariate imbalance that is based on an optimal transport. The authors also propose a related measure of covariate imbalance which they suggest may be used to assess the threat of confounding bias. The authors benchmark their methods against alternative approaches on established synthetic datasets.

### Strengths
The use of optimal transport methods to adjust for covariate imbalance seems to me a promising area of research. The performance of the proposed methods on synthetic data is very encouraging.

### Weaknesses
I found the motivation for the methods unclear. The authors point out that the difference between the feasible loss function $\int\varepsilon_{q_{t}}(h_{t})p(t)dt$ and the infeasible loss function $\int\varepsilon_{q}(h_{t})p(t)dt$ can be bounded by the Wasserstein distance between $q_{t}$ and $q$. It does not follow immediately that minimizing the sum of the feasible loss and this distance metric should lead to superior estimation performance. Indeed, the objective in equation (20) is minimized over three parameters $\phi$, $\psi$, and $\theta$, but only $\phi$ is shared between the feasible loss estimate $\hat{\mathcal{L}}$ and the Wasserstein metric. The estimate of $\tau_{t}(x)$ depends only on $\phi$ and $\psi$. Thus the benefits of including this Wasserstein distance in the optimization problem must result only from improved feature learning (i.e., an improved choice for $\phi$). In fact, I was rather perplexed that the loss $\hat{\mathcal{L}}$ did not incorporate the generalized propensity score $\theta$. It seemed to me from earlier parts of the paper that calculating the generalized propensity score by optimal transport, and using this to recover covariate balance, was likely to be the main point of the paper. But unless there is an error in the description of the methods, then $\theta$ is not directly used in learning $\tau_{t}(x)$, only impacting that problem through its impact on the choice of $\phi$. Incidentally, this in itself is rather complicated because the cost function $c_\phi(\cdot,\cdot)$ in the optimal transport is based on $\phi$, and setting $\phi$ to be identically zero would trivially make the Wassersteuin metric equal to zero.

Perhaps I am missing something here, particularly given that the very good performance on the benchmarking data, but I spent rather a long time trying to understand this and so, at the very least, I do not think it is well-explained.

I also found the description of the algorithm confusing. The algorithm contains a loop whose final step is to minimize the objective in (20) and the loop is iterated until convergence. But if we minimize this objective, then what changes in each iteration of the loop?

Finally, I find the description of the existing literature to be somewhat narrow. Causal inference methods have been developed over many decades and ML methods that incorporate data-splitting represent only a very recent and thin stratum of this much broader literature. In my opinion the authors ought to clarify when they are talking about causal inference methods as a whole, and when they are referring specifically to only recent causal inference methods from the ML literature.

### Questions
Why does the loss $\hat{\mathcal{L}}$ not incorporate the generalized propensity score? Give that it does not, what is the purpose of the Wasserstein part of the loss? Does it play a role other than improving the choice of $\phi$? If its only purpose is indeed to improve $\phi$ why should it achieve this? I am very curious to better understand the methods, particularly given the apparent superior performance in Section 5, but until I am able to grasp how/why the proposed methods  might work I do not feel I can recommend accepting the paper.

I wondered how GPS (without MLP) might perform on the data, and likewise for some other classical or non neural-network-based methods?

### Soundness
3

### Presentation
2

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
This work mainly studies the optimal transport method to reduce bias in causal inference. The authors propose a distribution alignment paradigm that leverages all training samples, avoiding the need for data splitting, which is a common limitation of existing methods. The theoretical contributions and empirical results demonstrate the effectiveness of the proposed method in both binary and continuous treatment settings.

### Strengths
1. The paper is well-structured and flows naturally.

2. This paper proposes a balanced  algorithm is designed that can effectively reduce confounding bias without data splitting.

3. The experimental studies are well done. A sufficient amount of empirical evidence for the proposed method is provided.

### Weaknesses
1. Theorem 2 holds under the assumption that $\mathcal{H}$ is an RKHS. Given this, it’s unclear why the author didn't opt to use kernel methods for learning representations, as they seem more aligned with the conditions of the theorem. Furthermore, the practical implementation uses neural networks, which do not inherently satisfy the RKHS property, raising questions about the direct applicability of the theoretical results.

2. While the experimental results show notable improvements, it's not entirely clear why the method performs so well. The theoretical bounds appear loose, so it would be valuable to explore why the method is still effective in practice. Specifically, the bounds in Theorem 3 involve terms that may not be tight, and it is not clear how these bounds relate to the observed performance gains. Gaining a deeper understanding would make the approach more reliable.

3. It would be beneficial to conduct ablation studies on the loss function involving Wasserstein distances. This could help identify which components contribute most to the performance gains and provide further insight into the tightness of the theoretical bounds. For example, it would be useful to see how performance changes when the Wasserstein distance is replaced with other metrics or when specific terms within the Wasserstein loss are removed.

4. What are the key advantages and differences between the author's debiasing method and other re-weighting approaches? Clarifying this comparison would be helpful. In particular, how does the proposed method address the limitations of traditional re-weighting methods, such as sensitivity to extreme weights or instability in high-dimensional settings?

### Questions
1. The algorithm relies on the ignorability assumption for its validity. I'm curious about its robustness in the presence of unobserved confounders. Could it still perform well under such circumstances?

2. If $X$ is a high-dimensional variable, how to estimate the probability mass $q(x_i)$? I worry about the curse of dimensionality


I will raise the score if these items are addressed.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a novel approach for measuring the causal effect given a treatment. The model, called ORIC, is designed to directly predict outcomes rather than causal effects and is based on the formulation of optimal transport to reduce confounding bias in observational data. Unlike typical causal inference models that often split the data according to treatments and train separate models (e.g., T-learner), ORIC is designed to be effectively trained without data splitting, which is the most significant contribution of this paper.

### Strengths
While there have been a few instances in the literature over the past few years where the formulation of optimal transport has been borrowed to solve the problem of measuring causal effects, this paper presents yet another new perspective, which I find intriguing. The formulation that naturally combines representation learning through the $\phi$ function with it could be widely utilized in other related research in the future.

### Weaknesses
The paper lacks a convincing explanation or example of how avoiding data splitting is practically beneficial in certain cases. In the case of binary treatment, splitting into just two sub-populations means the sample size is halved. Still, it is hard to see how this significantly worsens the estimation of the conditional covariate distribution. It is unclear whether the assumption is that one population is extremely smaller than the other or if the issue is that both populations are too small, making splitting problematic. This paper aims to apply to observational data rather than RCTs, but in real-world data, while there may be confounding bias, the sample size is not too small and often large. Therefore, it needs to be more clearly explained in which scenarios this methodology is more beneficial.

The approach in this paper that avoids data splitting starts from equations (3) and (4), where AMSE is defined. It is necessary to explain the validity of why minimizing AMSE should be the goal and to provide more details on the mathematical properties of the results produced by minimizing AMSE. AMSE can be also expressed as follows: $AMSE=\int_T[\int_Xl(h_t,\tau_t)p(x|t)dx]p(t)^2 dt$. This includes the term $p(t)$ twice. Since $\epsilon_{q_t}(h_t) \equiv \int_X l(h_t,\tau_t)p(x|t)dx$ is biased, the inclusion of the $p(t)$ term is necessary. However, including it twice is not immediately convincing. For example, when defining PEHE, the $p(t)$ term is included only once: $PEHE=\int_T [\int_X ((h_1-\tau_1) – (h_0-\tau_0))^2  p(x|t)dx] p(t) dt$. Because AMSE includes $p(t)$ twice, through Theorem 3, the integral in equation (16) is calculated over the joint distribution $p(x,t)$ rather than $p(x|t)$, which enables to avoid data splitting. If the integral in equation (16) were calculated over $p(x|t)$, data splitting would still be required. This paper intentionally designed AMSE to avoid data splitting and aimed to reduce it through its upper bound. Therefore, it is necessary to explain why minimizing AMSE guarantees unbiased and accurate causal inference. As it stands, minimizing AMSE might lead to excessive bias depending on the data. For instance, does it sufficiently minimize $\epsilon_q(h_0)$ when $p(t=1) >> p(t=0)$? Additional proofs or demonstrations seem necessary.

### Questions
[1] Please provide a rebuttal or explanation for the points raised in the weaknesses section.

[2] Since the computational complexity of the Sinkhorn algorithm used to calculate optimal transport increases quadratically with the number of data points, the algorithm in this paper would have a significant computational load for large datasets. How does it compare to other algorithms?

[3] In Figure 1, the $\theta$ neural network is not depicted. How is the $\theta$ neural network implemented? The explanation of the $\theta$ model is insufficient, making the understanding of lines 360 to 364 somewhat ambiguous. How does the $\theta$ model depend on $t$?

[4] Can this paper be understood in the context of S-learner vs. T-learner? In other words, is this paper proposing an S-learner framework?

### Soundness
3

### Presentation
2

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
The paper proposes a novel method for addressing covariate shift in observational data when estimating treatment effects, based on optimal transport. The benefit of the method is that data does not need to be split into groups and that the method can easily be applied to both binary and continuous treatments. Extensive theoretical and empirical results are provided to validate the efficacy of the method.

### Strengths
- The method addresses a clear problem and provides a natural solution.
- The paper provides extensive theoretical and empirical results.
- Despite the complex topic, the paper is generally easy to follow.

### Weaknesses
1. I found it hard to judge the novelty and contribution of the work with respect to existing work:
  - There is earlier work on applying optimal transport for treatment effect estimation, which is not discussed [1, 2]. How does this work compare to your own? Is there any reason why these methods were not included as benchmarks?
  - Apart from the data splitting, how exactly is your method different from CFR_Wass in Shalit et al. (2017)? Understanding this would make your own contribution more clear. Did you use CFR's version with Wasserstein distance in your experiments? 

2. The method introduces significant complexity and I would like to see more discussion of technical details:
  - Tuning of hyperparameters ($\lambda$, $\gamma$), as well as tuning in general, is not discussed. As this is a difficult problem in CATE estimation generally, I would like to see how the authors addressed this. Additionally, a sensitivity analysis of $\lambda$ is provided, but not for $\gamma$. Is there any reason why no such analysis is presented for $\gamma$?
  - The efficiency of the method is not discussed. Does the Sinkhorn algorithm make your training procedure much slower?

3. The conclusion summarizes the work, but does not include limitations of the proposed method or suggestions for future work.

### Questions
- See weaknesses points 1, 2, and 3

- Calling the potential outcome $\tau$ instead of $\mu$ is a bit confusing, as $\tau$ is typically reserved for the treatment effect. I would suggest calling it $\mu$. Related to this, previous work is mostly focused on estimating the treatment effect, instead of the potential outcome; or PEHE instead of AMSE. Could your theoretical results be applied to PEHE as well? 

- Any reason why evaluation for continuous treatments was not done with the Mean Integrated Squared Error (MISE)?

**Minor points:**
- Missing space in line 
- Missing space in line 845

### Soundness
2

### Presentation
3

### Contribution
2
