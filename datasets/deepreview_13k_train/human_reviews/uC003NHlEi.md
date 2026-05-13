# Hyperparameter Optimization via Interacting with Probabilistic Circuits

- Decision: Reject
- Scores: 8, 3, 6, 5

## Abstract
Despite the growing interest in designing truly interactive hyperparameter optimization (HPO) methods, to date, only a few allow to include human feedback. However, these methods add friction to the interactive process, rigidly requiring to fully specify the user input as prior distribution ex ante and often imposing additional constraints on the optimization framework. This hinders the flexible incorporation of expertise and valuable knowledge of domain experts, which might provide partial feedback at any time during optimization. To overcome these limitations, we introduce a novel Bayesian optimization approach leveraging tractable probabilistic models named probabilistic circuits (PCs) as surrogate model. PCs encode a tractable joint distribution over the hybrid hyperparameter space and evaluation scores, and enable exact conditional inference and sampling, allowing users to provide valuable insights interactively and generate configurations adhering to their feedback. We demonstrate the benefits of the resulting interactive HPO through an extensive empirical evaluation of diverse benchmarks, including the challenging setting of neural architecture search.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a Bayesian Optimization (BIO) framework for interactive Hyperparameter Optimization (HPO).
This framework is termed Bayesian Optimization via Hyperparameter Probabilistic Circuits (IBO-HPC).
By interactive, they allow human experts to provide feedback during the HPO process through tractable Probabilistic Circuits (PCs).
Specifically, they use PCs, a tractable joint distribution over hyperparameters and evaluation scores, to allow exact conditional inference and sample.
They back up their method with extensive numerical experiments.

### Strengths
This paper presents a refreshing and  interesting idea with solid execution.
**Clarity.** The writing of this paper is good. This paper is easy to follow. I especially appreciate the line-by-line walkthrough of algo1 in page 5.

**Originality.**  This paper utilizes PCs to perform exact Bayesian inference, especially conditional inference to include human experts’ feedback. While it makes sense as it sounds, I haven’t seen other solid executions of similar ideas.


**Significance.** I find IBO-HPC significant. Beyond its empirical effectiveness, unlike many human-in-the-loop HPO methods, it does not add computational burden.

**Solid Experiments.** Numerical validations are solid and extensive, making this paper more convincing.

### Weaknesses
NA

### Questions
How does IBO-HPC handle multiple human experts’ feedback? For example, consider a distributed or federated setting.

Can IBO-HPC handle online or life-long learning models with human experts monitoring in real time? If yes, can you sketch the response time of the model?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces a hyperparameter optimization approach by incorporating user feedback directly into the optimization process through a Bayesian framework using probabilistic circuits (PCs). The proposed method, Interactive Bayesian Optimization via Hyperparameter Probabilistic Circuits (IBO-HPC), aims to overcome limitations in existing HPO by allowing dynamic incorporation of expert knowledge at any point during the optimization. The method leverages PCs for tractable inference and sampling, enabling users to provide valuable insights interactively and generate configurations adhering to their feedback.

### Strengths
- The paper addresses the important topic of interactive hyperparameter optimization.
- It presents a novel approach by using probabilistic circuits as a surrogate model.

### Weaknesses
1. In comparison to prior methods that incorporate static priors, this paper introduces flexibility in the timing of knowledge integration. However, the study of human knowledge remains restricted to optimal solutions or their distributions. It would be beneficial if the introduction provided some application scenarios to underscore the importance of addressing this limitation. Additionally, the primary distinction of this method from prior work lies in its approach to knowledge-based sampling, yet the proposed sampling technique does not seem to offer substantial theoretical advancements, such as analyzing the impact of the sampling method and prior integration on the convergence bounds of the algorithm.

2. Lines 277-283: The sampling method first draws a set of candidate points based on a prior distribution, then further samples from these points. The paper does not discuss how this approach ensures accuracy in approximating Equation 2. Additionally, it is unclear why the two product terms in the equation are approximated through separate sampling steps. Could you provide a theoretical justification evidence for the accuracy of their approximation method and give an explanation for why the two-step sampling process was chosen over alternatives.

3. The paper does not clearly explain how sampling is conducted in Algorithm 1, line 13, or how the value of 𝑠 is calculated in line 14.

4. The method for constructing the PC model using data and how to perform sampling with this model are not well-explained. What are the advantages of the PC model compared to other models? Is there any drawback of it?

5. Existing prior-based methods can be applied to the application scenario in this work. Could you provide a more explicit comparison of the method to existing prior chased method (for example, BOPrO and πB) highlight the key differences and advantages. The paper does not discuss related work in interactive hyperparameter optimization. Provide a discussion of related work in interactive hyperparameter optimization would help contextualize the contribution.

6. The rationale behind the time and quality of knowledge used in the experimental setup is unclear. What real-world applications might benefit from this approach?

7. The test problems presented are limited, making it difficult to verify the method’s applicability across a diverse range of problems. Furthermore, comparisons with more recent prior-based HPO methods, such as Priorband [1] and PFNs4BO [2], as well as HPO methods like DPL [3] and Hyper-tune [4], are lacking. For the problems tested, you could refer to the test cases used in these methods.
[1] Mallik N, Bergman E, Hvarfner C, et al. Priorband: Practical hyperparameter optimization in the age of deep learning[J]. Advances in Neural Information Processing Systems, 2024, 36.
[2] Müller S, Feurer M, Hollmann N, et al. Pfns4bo: In-context learning for bayesian optimization[C]//International Conference on Machine Learning. PMLR, 2023: 25444-25470.
[3] Kadra A, Janowski M, Wistuba M, et al. Scaling laws for hyperparameter optimization[J]. Advances in Neural Information Processing Systems, 2024, 36.
[4] Li Y, Shen Y, Jiang H, et al. Hyper-tune: towards efficient hyper-parameter tuning at scale[J]. Proceedings of the VLDB Endowment, 2022, 15(6): 1256-1265.

8. The paper could be improved with clearer explanations. For example：there are many equations $p(\boldsymbol{\Theta}, st, K) ̸= p(\boldsymbol{\Theta}, st, \phi)$, $\int_{\mathcal{H} \backslash \hat{\mathcal{H}}} p\left(\boldsymbol{\Theta}, s_t, \mathcal{K}\right)=q(\hat{\mathcal{H}})$. After defining these equations, it is essential to explain why satisfying these conditions supports the corresponding conclusions.

### Questions
1. The example in Figure 1 is confusing: "Users can guide the HPO algorithm with their knowledge (here, N = 16 and W = 3), thus considerably increasing convergence speed and the quality of the final solution by focusing the optimization on remaining hyperparameters." In what cases would users accurately know the precise value of certain hyperparameters during optimization? Why wouldn’t they fix these parameter values at the start of optimization? How does this work relate to preference-based optimization algorithms?

2. "Moreover, these approaches might not reflect user knowledge precisely as defined in the prior due to the non-linear integration of the priors in the acquisition function. For example, in Fig. 1 (Right), the configurations selected by both BOPrO (Souza et al., 2021) and πBO (Hvarfner et al., 2022) during the first 20 iterations of optimization remarkably deviate from the given user prior." How did the authors define "remarkably deviate"? If I understand correctly, these algorithms aim to move towards the region defined by the prior, rather than sampling exactly according to the prior distribution, since the user-provided prior might not be accurate. In this context, the example in Fig. 1 (Right) does not seem to support the authors’ claim.

3. What is the difference between "user knowledge" and "feedback" in Definitions 2 and 3?

4. There are several symbols in Definition 3, such as "an interactive policy $p$," "$p(\Theta, st, K)$," and "call $p$ feedback." I find these symbols confusing and difficult to interpret.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper leverages probabilistic circuits to enable user interaction in Bayesian optimization during hyperparameter optimization.

### Strengths
The paper is well-written and the methodology seems to be original.

### Weaknesses
Definition 3 would be clearer if it included an explanation of why the second condition is necessary and how it ensures the policy accurately represents the user's knowledge.

### Questions
Please provide more reasoning for the second condition on Definition 3.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents an algorithms for performing Bayesian optimization for hyperparameter tuning that is amenable to interaction with users. Users can indeed input their belief of promising hyperparameters at any iteration (compared to previously proposed approaches that only allow user to input at the beginning of the process) in the form of (possibly point mass) distributions. The method relies on previously proposed probability circuits and a sampling mechanism recalling Thompson sampling. 
The authors report various experiments showing how the proposed method IBO-HPC performs both without user inputs and with beneficial and detrimental user inputs, comparing to various baselines.

### Strengths
- The motivation of the work is well presented and clear
- the application of probability circuits to HPO is novel to the best of my knowledge
- PCs the integration of user knowledge seems natural and justified

### Weaknesses
 - some unclear notation and not properly introduced variables (see questions)
- to me, the overall novelty value of this work is not immediately clear. On the one hand, it does look like to me that the work is a direct application of the general framework of BO with a surrogate model given by PC. The integration of user knowledge in the form of prior distribution seems fairly straightforward, but not necessarily unique to the proposed framework (although this work focuses on this aspect). The user knowledge decay seems a reasonable heuristics. Perhaps I am missing some novelty aspect, I'd appreciate the authors comments on this.
- It is unclear to me why other HPO methods "cannot take user feedback" at any time, especially if this is given in the form of "fixing some hyperparameter value" (aka point mass distribution). Even thinking about random search, at any time (i.e. after any number of draws/trials), one can replace any previously given distribution with an updated guess by the user and continue the process. This sounds to me a reasonable simple baseline that is not included in the paper
- similarly (although I am not familiar with the methods) I would assume that both BOPrO and muBO could be modified in a straightforward way to allow for anytime user belief update by warm-restarting (i.e. using all previously evaluated configurations as starting points). Is there any fundamental limitation that prevents this integration?

For me these last aspects pared by the low level of novelty I see at the moment make me lean toward rejection.

### Questions
- notation:
  - what's the meaning of p(f|D) in 3.1? when I read this notation I think of a distribution over functions, but rather since f here is given, probably the authors mean a distribution over function values (given hyperparameters)? 
  - what is $\mathcal{S}$ and $\mathcal{K}$ (are they just generic collections)?
  - what's the measure of the integral in definition 3?
- if possible, I would like to see comparison with at least simple baselines such as RS with the same user belief integration used by IBO-HPC.

### Soundness
3

### Presentation
2

### Contribution
2
