# Towards Understanding Robustness and Generalization in World Models

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3

## Abstract
World model has recently emerged as a promising approach to reinforcement learning (RL), as evidenced by the recent successes that world model based agents achieve state-of-the-art performance on a wide range of visual control tasks. This work aims to obtain a deep understanding of the robustness and generalization capabilities of world models. Thus motivated, we develop a stochastic differential
equation formulation by treating the world model learning as a stochastic dynamical system in the latent state space, and characterize the impact of latent representation errors on robustness and generalization, for both cases with zero-drift representation errors and with non-zero-drift representation errors. Our somewhat surprising findings, based on both theoretic and experimental studies, reveal that for the case with zero drift, modest latent representation errors can in fact function as implicit regularization and hence result in improved robustness. We further propose a Jacobian regularization scheme to mitigate the compounding error propagation effects of non-zero drift, thereby enhancing training stability and robustness. Our extensive experimental studies corroborate that this regularization approach not only stabilizes training but also accelerates convergence and improves accuracy of long-horizon prediction.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates the robustness and generalization of World Models by framing the learning process as a stochastic dynamical system within the latent state space. The authors present theoretical results to analyze the impact of latent representation errors on robustness and generalization in both zero-drift and non-zero-drift scenarios. Specifically, they demonstrate that, under certain assumptions, there exist CNN architectures for the world model’s encoder and decoder that achieve a small $W_1$ approximation error. Furthermore, they derive the relationship between the expected loss of the system in scenarios with no latent representation error and those with zero-drift and non-zero-drift errors. Based on their theoretical findings, the authors propose using Jacobian regularization to reduce representation error and improve the quality of rollouts during inference. Experiments were conducted on two environments, Walker and Quadruped, demonstrating that a world model trained with Jacobian regularization achieves faster convergence and greater robustness against unseen noisy observations, perturbed dynamics, and encoder errors.

### Strengths
- Overall, the paper is well-written and clear.

- This work enhances our understanding of the generalization and robustness of world models by leveraging less commonly used tools, specifically stochastic dynamical systems and differential geometry.

- The paper addresses a popular class of world models that have demonstrated practical effectiveness, adapting them to a theoretical framework with certain simplifying assumptions.

### Weaknesses
 - The theorems are weakly interpreted in the discussion sections. Specifically, the primary variables and parameters within the theorems are not sufficiently explained, making it challenging for readers to fully understand the implications of the results. For instance, in Theorem 3.6, the authors suggest that $\varepsilon $ can be assumed to be small, but they do not provide details on the relevant parameters or the conditions under which this assumption is valid. Further interpretation and clarification of these variables and assumptions would significantly enhance the accessibility and impact of the theoretical results.

- The primary weakness of the paper lies in the experimental evaluation. The authors use DreamerV2 as the world model and compare results with and without Jacobian regularization. However, comparing only with the non-regularized version may be insufficient, as it lacks the same inductive bias present in the regularized model. I recommend that the authors include baselines that incorporate similar inductive biases to their technique—specifically, methods explicitly designed to be robust against perturbations at inference time.


- The experiments are limited to only two environments, Walker and Quadruped, making it difficult to fully assess the effectiveness and generalizability of the proposed method. I suggest that the authors expand their experiments to include additional environments.



### Questions
- Could the authors elaborate on how the results in table (1) connects with their theoretical findings?

- In (4), is the decoder intentionally conditioned on $\tilde{z}_t$? Dreamer and PlaNet typically condition the decoder on $z_t$ directly.

- Could the authors clarify what $\mathcal{X}$ represents in the CNN configuration? Is it intended to denote the state space or submanifold $\mathcal{M}$?

- Does Theorem 3.6 apply exclusively when the hidden representation is one-dimensional, given that the codomain of $f_{\text{CNN}}$ is $\mathbb{R}$?

- Could the authors elaborate on how "Theorem 4.1 correlates with the empirical findings in Hafner et al. (2019) regarding the diminished
predictive accuracy of latent states $\tilde{z}_t$ over the extended horizons"?

- Does "masked image percentage" refer to the portion of an image that has had noise applied?

- How did author select Jacobian regularization coefficient $\lambda$ in their experiments?

- In appendix D.6, what is the rationale behind using a different noise distribution for augmentation approach?

**Typos**

- Citations in the Related Work section are missing parentheses.

- Line 247: "choice choice" appears to be duplicated.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies robustness and generalisation in model-based RL agents with world models (e.g. DreamerV2/V3) by analysing the effects of latent representation errors. The authors develop a stochastic differential equation (SDE) formulation as continuous generalisation of discrete-time latent transitions in world models, and characterise two types of latent representation errors: zero-drift and non-zero-drift. Their key findings suggest that modest zero-drift errors can actually act as implicit regularization and improve robustness, while non-zero-drift errors can be harmful. They propose using Jacobian regularisation to mitigate negative effects from non-zero-drift errors. The authors empirically evaluate the performance of the proposed regularisation methods on selected MuJoCo tasks.

### Strengths
- Novel theoretical perspective on applying the continuous-time formulation of discrete transition dynamics to latent transitions in world models.
- The proposed Jacobian regualrisation is simple and seems to lead to performance increase empirically.

### Weaknesses
 - The presentation is quite dense and difficult to follow, with repetitive statements and inadequate motivation for why this analysis approach is needed.
- The assumption of requiring C3 functions with bounded Lipschitz derivatives for theoretical analysis can be very strong and potentially unrealistic in practice.
- Empirical evaluation is limited to only Walker and Quadruped environments, leading to imcomprehensive evaluations.
- The hyperparameter sensitivity for the regularization weight, $\lambda$, is expected to significantly affect the resulting model performance, but its sensitivity is not discussed (either theoretically or empirically) in the manuscript.
- There is a lack of comparison with existing approaches on addressing robustness and generalisability in world models.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
1

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
This paper theoretically analyzes the robustness and generalization of world models, particularly by formulating latent dynamics models as stochastic differential equations with latent representation errors. The authors first demonstrate that these errors can be made sufficiently small using appropriate CNN encoders and decoders. They then show that these errors introduce additional terms in the loss function, which act as implicit regularization in the zero-drift case but introduce unstable bias in non-zero-drift scenarios. To enhance robustness and generalization, the authors propose an explicit regularization on the Jacobian, which is empirically validated in Mujoco environments.

### Strengths
1. To my knowledge, there is currently no substantial theoretical analysis of latent dynamics models, despite the significant empirical success of models like Dreamer.
2. The theoretical analysis leads to the derivation of a regularization term that improves empirical performance.

### Weaknesses
I must preface my comments by stating that I am not an expert in theoretical analysis. As a researcher focused on empirical methods (such as Dreamer), my main concern is that the theoretical formulation presented in this paper may not align well with the empirical implementation of Dreamer. I have outlined my questions below. The Area Chair is free to disregard my review if they deem these points inappropriate, but I believe my perspective could be valuable in assessing this paper.

 1. What are the experimental settings in Table 1? I could not find any explanation or references in the Introduction.
2. There are various types of errors in latent dynamics models. In my opinion, the most crucial is the error in the transition models. However, this error is not addressed in equations (5-6). Could the authors provide insights into why they focus solely on representation errors?
3. What is the ground truth probability measure $P$ introduced in Line 232? In Dreamer, latent representations are learned using a per-sample reconstruction loss of states and a prediction loss. How do these implementation losses relate to the two minimizations of distribution distance mentioned in Line 238? Additionally, how does the $W_1$ distance relate to the scale of errors $\varepsilon$?
4. How is Corollary 4.2 regarding Q functions in Section 4 defined and derived? There do not appear to be any reward variables in the SDE formulation.
5. How is the Jacobian regularization term in equation (20) implemented in the experiments? I could not find implementation details in the Appendix.

### Questions
1. What are the experimental settings in Table 1? I could not find any explanation or references in the Introduction.
2. There are various types of errors in latent dynamics models. In my opinion, the most crucial is the error in the transition models. However, this error is not addressed in equations (5-6). Could the authors provide insights into why they focus solely on representation errors?
3. What is the ground truth probability measure $P$ introduced in Line 232? In Dreamer, latent representations are learned using a per-sample reconstruction loss of states and a prediction loss. How do these implementation losses relate to the two minimizations of distribution distance mentioned in Line 238? Additionally, how does the $W_1$ distance relate to the scale of errors $\varepsilon$?
4. How is Corollary 4.2 regarding Q functions in Section 4 defined and derived? There do not appear to be any reward variables in the SDE formulation.
5. How is the Jacobian regularization term in equation (20) implemented in the experiments? I could not find implementation details in the Appendix.

I am open to discussing these questions with the authors and am willing to increase my rating if my questions are well responsed.

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
3

### Summary
This paper investigates how regularization can give rise to better generalization in world models, particularly how Latent Representation Errors can be an important source for robustness in Dreamer-style world models. Theoretical results are derived and authors propose a Jacobian regularization scheme for improving robustness. Their approach is tested on two Mujoco environments with noise perturbations and augmented versions of image observations.

### Strengths
* Interesting research question: can world model inaccuracies improve generalization.
* Jacobian regularization of Dreamer-style models is, to my knowledge, novel.
* Proposed method improves robustness.

### Weaknesses
While I appreciate that the paper's main contribution is theoretical, I think the paper is written in a way that makes it unnecessarily difficult to understand. The mathematical treatment is very thorough, but the readability of the paper suffers a lot as a consequence. Moreover, while a lot of attention is put into describing mathematical details that I don’t believe need to be in the main text, some very important concepts like Latent Representation Errors (LRE) and zero/non-zero drift and Jacobian regularization are discussed very briefly, and very late in the paper. In fact, LRE is mentioned many times in the introduction without ever being explained. The authors need to explain precisely what LREs are, how they differ from noise injection, and why LREs are an interesting source of robustness early on in the paper, and in a way that is accessible to most ML practitioners working on World Models. The same holds for drift and Jacobian regularization. A paragraph summarizing in natural language what these things are, and how they relate to each other would improve readability immensely. The subsequent mathematical treatment will be a lot easier to understand as a consequence.

Secondly, while the results look promising, they are not very extensive. Does the regularization give performance gains in other mujoco environments too? How does the performance compare to other ways of regularizing the dynamics model, like Repo [1] or RPC [2], or just L2 regularization on dynamics weights?

Due to the inadequate exposition of the paper, and the limited experimental evaluation, I cannot recommend it for acceptance in the current form. If the readability of the paper is significantly improved, and experiments in more DMC environments are added, and more baselines (like Repo and RPC) comparisons are made, I am willing to increase my score.

### Questions
* Did you evaluate your method on other Mujoco environments?
* Did you compare your method to other regularization methods?

### Soundness
3

### Presentation
1

### Contribution
2
