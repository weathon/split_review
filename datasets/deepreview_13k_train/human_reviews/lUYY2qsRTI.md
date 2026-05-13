# Delphic Offline Reinforcement Learning under Nonidentifiable Hidden Confounding

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
A prominent challenge of offline reinforcement learning (RL) is the issue of hidden confounding: unobserved variables may influence both the actions taken by the agent and the observed outcomes. Hidden confounding can compromise the validity of any causal conclusion drawn from data and presents a major obstacle to effective offline RL. In the present paper, we tackle the problem of hidden confounding in the nonidentifiable setting. We propose a definition of uncertainty due to hidden confounding bias, termed delphic uncertainty, which uses variation over world models compatible with the observations, and differentiate it from the well-known epistemic and aleatoric uncertainties. We derive a practical method for estimating the three types of uncertainties, and construct a pessimistic offline RL algorithm to account for them. Our method does not assume identifiability of the unobserved confounders, and attempts to reduce the amount of confounding bias. We demonstrate through extensive experiments and ablations the efficacy of our approach on a sepsis management benchmark, as well as on electronic health records. Our results suggest that nonidentifiable hidden confounding bias can be mitigated to improve offline RL solutions in practice.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
* The authors address the unobserved confounding problem in offline reinforcement learning with pessimism over possible "worlds" (confounder values) compatible with the observation (distribution of trajectory).
* They define a new type of uncertainty "Delphic uncertainty" as the variance of Q value over the compatible (thus unidentifiable) worlds with theoretical decomposition with other types of uncertainties.
* Simulated evaluation and evaluation by experts clearly indicated that their method outperformed existing methods that do not address the Delphic uncertainty such as CQL and BC when strongly confounded.

### Strengths
* The unobserved confounding is a major issue in offline reinforcement learning.
* They investigate a minimal problem setting (contextual MDP) to reproduce it and propose a simple and intuitive method that models the uncertainty related to the confounding.
* The theory that decomposes the variance into several types of uncertainties motivates the approach well.
* Empirical evidence including evaluation by experts clearly supports their claim.

### Weaknesses
1. Baselines and environments tested are relatively limited (see also Question 1 and 2).
1. Not being a major concern, it would be more intuitively superior if an end-to-end formulation was possible, as in the CQL. The proposed method is divided into a step of learning multiple possible worlds and a step of pessimism using them.

### Questions
1. Intuitively, it seems that estimating $z$ from the trajectory and using it as $\pi(a|s,z)$ as in POMDP methods would improve performance for later steps $t$, but is such an extension possible? Also, is the proposed method still superior when such a POMDP method is used as a baseline? I'm wondering if the online identification of the world is possible within an episode through such a formulation.
1. The existing approaches for a similar setting are discussed (e.g. using partial identification) but not compared. Isn't it possible to compare them?
1. Is the $\max$ taken w.r.t. not only $z,z'$ but also $s,a$? If not, how $\Gamma(s,a)$ is summarized for an environment?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of offline learning an optimal independent policy. To achieve this goal, the authors propose the Delphic Offline RL algorithm that:
1. identifies the compatible world model for confounded MDP and learn the world-dependent value function $Q_w^\pi$;
2. incorporates pessimistic policy optimization using the estimated delphic uncertainty;
The experimental results show that Delphic ORL method achieves better performance under large confounding strength.

### Strengths
The paper is well motivated and the author proposed an interesting idea to incorporate the delphic uncertainty in pessimistic offline policy optimization. The writing is generally clear and easy to follow.

### Weaknesses
1. It seems that the estimator $\mathbb{Var}_w (Q^\pi_w (s, a))$ is not an unbiased estimator for the delphic uncertainty as the other two forms of uncertainty can still enter the estimation (noting that $Q_w^\pi$ is not the conditional expectation given by Theorem 4.2). I didn't see the author making effort to justify this point. Specifically, the practical computation of $Q_w^\pi(s,a)$ involves an expectation over $\theta_w$, which is approximated by a sample mean using an ensemble of particles. While this sample mean is an unbiased estimator of the expectation given a fixed $w$, it does not account for the fact that the individual particle estimates $Q_{\theta_w}^\pi(s,a)$ are themselves subject to epistemic and aleatoric uncertainty. These uncertainties propagate into the estimation of $Q_w^\pi(s,a)$, and consequently into the delphic uncertainty estimate, making it potentially biased.

2. Is it necessary to evaluate the delphic uncertainty on a state-action level rather than evaluating the same thing for the total reward of the whole trajectory under  policy $\pi$? I'm not convinced of the soundness of the method here, as there might be some correlations between different state-action pairs in the Q function.  Furthermore, if the goal is to optimize for the total return, assessing uncertainty at the trajectory level would seem more directly aligned with the objective. Evaluating at the state-action level might not fully capture the cumulative effect of delphic uncertainty over a sequence of decisions, and could lead to suboptimal policies if these correlations are not properly accounted for.

### Questions
It is assumed that the offline policy is known. What if $\pi_b$ is unavailable so that the importance sampling method has biased in estimating the value function? Is it possible to incorporate other unbiased estimation method in confounded POMDP setting like (Shi. et al, 2022)?


### Reference:

Shi, Chengchun, et al. "A minimax learning approach to off-policy evaluation in confounded partially observable markov decision processes." International Conference on Machine Learning. PMLR, 2022.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper uses the contextual Markov Decision Process to model unobserved confounders in offline reinforcement learning. First, the authors define the class of contextual MDP that are compatible with the dataset. Then, based on a variance decomposition formula, the authors introduce the delphic uncertainty. Delphic uncertainty means the variance of policy performance across all compatible worlds. Then based on the delphic uncertainty term, the authors propose a penalty term for offline RL.

### Strengths
The method is applied to two real/semi-real-world medical datasets, which is very nice.

### Weaknesses
The probability setup of the paper is a bit unclear to me.

Specifically, the notation $P_w \mapsto \Delta W$ on page 4 is not standard and its meaning is not immediately obvious. It's unclear if this notation is intended to mean that $P_w$ is an element of $\Delta W$ or if it represents some kind of mapping. This lack of clarity makes it difficult to follow the subsequent definitions and theorems.

Furthermore, the introduction of a stochastic value model $Q_{\theta w}$ immediately after Definition 4.1 is confusing. The value function of a policy is typically a deterministic quantity, and it is not clear where the randomness in this model is supposed to come from. This is especially concerning since the paper is about offline RL, where the environment is fixed and the randomness should only come from the policy. The authors should clarify the source of this stochasticity and its implications.

Finally, the meaning of Theorem 4.2 is unclear due to the ambiguous probability setup. The theorem seems to involve expectations with respect to two different measures: one over the space of compatible worlds (denoted by $E_w$) and another over Q-value functions (denoted by $E_{\theta_w}$). The relationship between these measures and how they are derived from the underlying probability model is not clearly explained. This makes it difficult to understand the significance of the variance decomposition presented in the theorem.

### Questions
1. On page 4, what does the notation $P_w \mapsto \Delta W$ mean? Do you mean $ P_w \in \Delta W$?

2. Right after Def 4.1, the author proposes to model the Q function as a random element "value model $Q_{\theta w}$ is defined by some stochastic model". Where is this randomness coming from? Isn't the value function of a policy just a deterministic function?

3. Related to the previous remark, the meaning of Theorem 4.2 is unclear to me. Could the authors detail the probability setup for this theorem? From my understanding, there is a measure over the space of compatible worlds (by the notation $E_w$), and then there is a measure over Q-value functions (by the notation $E_{\theta_w}$). What is the relationship between these measures?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the problem of nonidentifiable confounding in RL. In this regard, a new notion of so-called delphic uncertainty is introduced in addition to aleatoric and epistemic uncertainties. An offline RL algorithm is proposed that penalizes taking actions with high delphic uncertainty. The performance is reported on both synthetic and real data.

### Strengths
- The presentation is excellent with adequate illustrations that helped my understanding.
- The new notion of uncertainty is insightful and important in the real application of RL.
- The algorithm and employed strategies sound reasonable to me.

### Weaknesses
I generally enjoyed reading this paper, but there are a few things that I wish were discussed in more depth or clarified:
1. I'm a little confused about how should I decide whether a world is compatible or not. Apparently, I can start with any confounder space dimensionality, prior $p(z)$ and model architectures and then estimate the parameters using ELBO, and then I have a compatible world? How far I can go here or what should I see to say a world is not compatible here? Specifically, what are the criteria for determining the validity of the learned confounder model? It seems that any model that maximizes the ELBO would be considered a 'compatible world,' which raises concerns about the identifiability of the confounder space and the robustness of the approach to different modeling choices. How sensitive is the performance to the choice of prior $p(z)$ and the architecture of the model used to approximate the posterior $q(z|\tau)$?
2. The behavior policy is in general a context-aware policy. So, I'd expect enforcing similarity to the behavior policy might result in some sort of context awareness. Is this the case? For instance, in the illustrative bandit example, an optimal context-independent policy only explores $a_0$ and $a_2$, which in World 2 is very different from the behavioral policy and seems to be suboptimal compared to a uniform policy. So, if I get it right, the similarity to behavioral policy is encouraged in this setting with unobserved confounders. It's unclear how the method distinguishes between beneficial context awareness and simply mimicking a potentially suboptimal behavior policy, especially when the confounders are unobserved and the behavior policy itself might be flawed.
3. As a similar question to the previous question, don't we expect avoiding actions $(s,a)$ with high delphic similarity to result in a policy more similar to the behavioral policy? It seems to be the opposite: page 8 "... we also studied the discrepancy of our trained policy with that in the data. Particularly, we compared the actions taken by our policy and the policy in the data and found that ... our policy was significantly different." This seems counterintuitive, as one would expect that penalizing actions with high delphic uncertainty should lead to a more conservative policy that resembles the behavior policy. The discrepancy between this expectation and the reported results needs further explanation.
4. Could you elaborate on how counterfactual $Q_w^\pi$ is estimated using importance sampling in Section 5.1? Also, I'm not sure where in appendix C is referred to. The exact implementation details of the importance sampling estimator are unclear, and the connection to Appendix C needs to be explicitly clarified. What is the specific form of the importance weights used, and how are they computed given the estimated confounder distributions? It would be beneficial to see the exact equations and a more detailed explanation of the process.
5. I'm not sure how to think about a reasonable $\Gamma$. Isn't Figure 7 concerning? The choice of $\Gamma$ as a measure of confounding strength is not well justified, and it would be helpful to understand how its magnitude relates to the severity of confounding in practice. Figure 7 shows that the preference between BC and offline RL policies remains close to 50%, which raises questions about the practical significance of the proposed approach. It would be useful to see a more detailed analysis of the sensitivity of the results to different values of $\Gamma$ and to understand the implications of this measure.

### Questions
Please refer to the Weaknesses. I'm happy to update my scores after hearing your thoughts.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
