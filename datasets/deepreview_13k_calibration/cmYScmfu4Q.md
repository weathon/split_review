# Zeroth-Order Policy Gradient for Reinforcement Learning from Human Feedback without Reward Inference

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 3, 8, 8

## Abstract
Reward inference (learning a reward model from human preferences) is a critical intermediate step in Reinforcement Learning from Human Feedback (RLHF) for fine-tuning Large Language Models (LLMs) such as ChatGPT. In practice, reward inference faces several fundamental challenges, including double problem misspecification, reward model evaluation without ground truth, distribution shift, and overfitting in joint reward model and policy training. 
An alternative approach that avoids these pitfalls is direct policy optimization without reward inference, such as Direct Preference Optimization (DPO), which provides a much simpler pipeline and has shown empirical success in LLMs. However, DPO utilizes the closed-form expression between the optimal policy and the reward function, which only works under the bandit setting or deterministic MDPs. This paper develops two RLHF algorithms without reward inference, which work for {\em general} RL problems beyond bandits and deterministic MDPs, and {\em general} preference models beyond the Bradely-Terry model. The key idea is to estimate the local value function difference from human preferences and then approximate the policy gradient with a zeroth-order gradient approximator. For both algorithms, we establish rates of convergence in terms of the number of policy gradient iterations, as well as the number of trajectory samples and human preference queries per iteration. Our results show there exist provably efficient methods to solve general RLHF problems without reward inference.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This is a novel result that establishes local convergence for an RLHF setup utilizing a novel method to estimate the difference in value functions. However, given the current literature which has established global convergence with a better sample complexity. I do not think this work has sufficient novelty for acceptance.

### Strengths
The paper utilizes a novel method for estimation of the difference in the value functions using the inverse of the preference functions. It is able to prove local convergence for a non-deterministic MDP. The paper is well laid out and easy to read.

### Weaknesses
The paper establishes local convergence for an RLHF setup using a novel method to estimate the difference in value functions. However, the established local convergence with a sample complexity of $\epsilon^{-5}$ is a significant limitation.  The current literature, specifically Xie et al. (2024), has already demonstrated global convergence with a better sample complexity of $\epsilon^{-2}$. The key issue is the lack of a clear justification for why this work is an improvement, given that the existing results provide stronger guarantees and better sample complexity, even if it is in a more restricted setting. The practical implications of local convergence, especially in high-dimensional policy spaces common in RLHF, are unclear, as the convergence region could be very small and difficult to reach in practice. Furthermore, the $\epsilon^{-5}$ sample complexity is quite high, raising concerns about the practical applicability of the method, especially when compared to methods with better sample complexities. 

Even though the paper's method for estimating the difference in value functions is novel, the lack of global convergence and the higher sample complexity make the contribution questionable. The paper needs to provide a compelling argument as to why local convergence is a sufficiently strong result in the context of current literature, and why the novel method justifies the weaker convergence guarantees and higher sample complexity. The novelty of the method alone is not sufficient to overcome the limitations in convergence guarantees and sample complexity.

### Questions
Is there a way to go from local to global convergence? Perhaps is global convergence can be achieved, the work may be accepted for publication.

### Soundness
4

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
4

### Summary
The paper proposes a zero-order optimization algorithm for RLHF. The idea is to carry out random perturbation in the space of parameters directly and construct gradient updates based on the random samples. The paper presents some theoretical results that characterize the bias and convergence property of the algorithm.

### Strengths
The paper presents theoretical guarantees for zero-order optimization algorithm for RLHF.

### Weaknesses
The idea of applying zero-order optimization is not novel. Similar ideas have been extensively studied in the deep RL literature. Much literature reference is missing from discussion. A theoretical paper like this is not very valuable to the RLHF or deep RL community.

It's not clear if the discussion here is specific to RLHF at all. Do RLHF allow us to assume additional structure on the rewards or the parameter space? No such discussion is furthered in the paper - in regular RL or deep RL setups, the same algorithmic discussions apply. And as a result, the paper is not really a RLHF specific algorithm, the algorithm itself has been extensively studied in the RL literature as well.

There is no empirical backup of the results at all, not even tabular experiments. I think a theoretical paper in its current form like this would not offer too much additional value to the field of RLHF or deep RL. Certain amount of experimentation is warranted, and in the case of RLHF, it is also interesting to see if the algorithm can work at all and how it compares with REINFORCE / PPO.

### Questions
### === Zero-order method in deep RL ===

The idea of applying random perturbation to model parameters and construct gradient accordingly, has been studied extensively in the deep RL literature as replacement for REINFORCE or PPO like algorithms. It seems that much discussion is missing from the paper such as [1] which basically started the trend of zero-order based method for deep RL.

[1] Salisman et al, 2017, Evolution Strategies as a Scalable Alternative to Reinforcement Learning

### === Relevance to RLHF ===

It's not clear if the discussion here is specific to RLHF at all. Do RLHF allow us to assume additional structure on the rewards or the parameter space? No such discussion is furthered in the paper - in regular RL or deep RL setups, the same algorithmic discussions apply. And as a result, the paper is not really a RLHF specific algorithm, the algorithm itself has been extensively studied in the RL literature as well.

### === Empirical ===

There is no empirical backup of the results at all, not even tabular experiments. I think a theoretical paper in its current form like this would not offer too much additional value to the field of RLHF or deep RL. Certain amount of experimentation is warranted, and in the case of RLHF, it is also interesting to see if the algorithm can work at all and how it compares with REINFORCE / PPO.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes the use of zero-th order algorithms to align a policy to preference data. They propose ZPG, based on random spherical perturbations, and ZBCPG, based on subblockwise perturbations, and prove sample complexity and convergence rates. These algorithms generalize from a Bradley-Terry preference model to general preference model with a specified link function, as well as generalize from deterministic to stochastic domains.

### Strengths
- The methods ZPG and ZBCPG work for a general class of link functions (beyond the BT-model) and stochastic dynamics as well.
- Theoretical sample complexity and convergence rates that give an idea of the dependence on the number of human preferences needed, and prove convergence exists. I have not checked the proofs in detail.

### Weaknesses
 - ZPG and ZBCPG do not work directly from an offline dataset like DPO can; they require online human preferences for the current samples. - Furthermore, even comparing ZPG to online DPO, it seems that ZPG requires more trajectory samples (i.e. more forward passes) because you need multiple perturbations, which is multiple times more costly than online DPO.
- Zero-th order methods may be slower than gradient-based methods, especially for very large models like LLMs.
- No toy experiments. While LLM experiments would seem daunting in addition to the theoretical contribution, toy experiments in simple, stochastic domains to illustrate how DPO would fail but ZPG would work, would be a great addition to further motivate the need for a DPO alternative. I would be willing to increase my score if toy experiments are added to the paper.

### Questions
- You mention that classic RLHF and DPO use human preferences to construct a global model, while your method uses the preferences only to locally estimate the policy gradient. While that’s true in theory, however in the actual DPO algorithm in practice, it is also using the expected difference in preference between two generations to construct a policy gradient. Like you mention, because of function approximation, the global BT model assumed by DPO no longer holds, so the empirical DPO also ends up only using local information to estimate the policy gradient. Especially if DPO is used online instead of from a fixed offline dataset. So in practice, both DPO and ZPG are using local information to estimate a policy gradient, and the global-local divide isn’t really clearly there anymore. Could you update the discussion to reflect this?
- You mention the link function generalizes the BT-model. Could you give one or  more motivating examples of non-BT models and link functions that could be applicable (no need for experiments or deep analysis, just give some intuition on when non-BT models could be useful)? I think this would strengthen the contribution of the more general link function.

-- After Author Response --
Thank you for adding the additional numerical experiments and non-BT explanations. I have increased my score.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces two new algorithms for RLHF that do not require learning a reward function. The core algorithm is a variation of reinforce, using a zero-order gradient approximator (the two proposed algorithms differing in the choice of the perturbation direction). To avoid learning a reward function, the authors assume that the preference model is Bradley-Terry-like (considering a more general sigmoid link function, instead of just the logistic function), that $M$ human raters (with $M$ large enough) are available for ranking $N$ pairs of completions (current policy - perturbation), and then use the  inverse of the link function to estimate the reward difference from the empirical preference probability, this reward difference being used for the zero-order gradient estimate. The authors show a convergence result for each algorithm, with rate of convergence (the same), for reaching a stationary policy (not necessarily the optimal one, but one with zero gradient). They also provide some explanations about the technical difficulties of their proof (full proofs being provided in the appendix). There is no empirical study.

### Strengths
* The proposed algorithms are interesting, at least from a theoretical viewpoint
* The paper is overall clearly and well written
* There is a nice discussion of the technical difficulties for proving their results, which is quite helpful
* The provided theoretical results sound plausible (some questions about the proofs of Thm1 though, and Thm 2 has not been double-checked)

### Weaknesses
 * There are overclaims and/or lack of discussion of the limitations of the proposed approach. Drawbacks of DPO or classic RLHF are discussed at length, suggesting that the proposed approach alleviate them (which is only very partly true), but not the limitations of the proposed approach. The strongest issue is that it is assumed that $M$ humans are available for rating $N$ pairs of trajectories for each gradient step (and this must be done online, because the proposed approach is purely on-policy). So, it is hard to see any setting where this could be applicable or reasonable, and it is a strong drawback compared to more practical RLHF approaches. It may be fine to have an algorithm with theoretical guarantees that is not fully applicable, but this should be discussed.
*  The proposed algorithms seem to be new, and they are explicitly positioned as addressing shortcomings of classic RLHF or DPO, which would call for some empirical results, at least on bandits or toy MDPs (possibly comparing with classic RLHF, DPO, but also things like online DPO, eg see « Direct language model alignment from online ai feedback » by Guo et al). There is no such empirical study, and it would really strengthen the paper by providing some empirical evidences on some claims done in the paper.
* There are parts of the paper and of the proofs that are not totally clear, see questions.

## Lack of discussion 
* Can you please discuss more thoroughly the limitations of the proposed approach (like the need to have on-policy online human raters), and in more details what are the pros and cons compared to DPO and classic RLHF?
* One advantage claimed compared to DPO is the ability to handle stochastic transitions. However, the focus is also mostly done on LLMS. Can you explain in which case we would have stochastic transitions in this context (and how it is handled by your framework)?
* There is no KL regularization, compared to all other works for doing RLHF (and not without reason). Can you expand on this, is it no longer required (from a practical perspective)?
* The paper claims going « beyond the BT model », but the generalization is rather weak, could it handle more general preference models such as those considered for example in « Nash learning from human feedback » by Munos et al?

## No empirical study
* Given that the analyzed algorithm is not representative of practical approaches, and that the second proposed algorithm is motivated by computational aspects (memory, distributed aspect), would it make sense to at least provide some minimal empirical study (with the proposed algorithms, but also DPO, classic RLHF, online DPO)? Or to provide a clear discussion about why it would not bring interesting evidences?

## Aspects to clarify and/or correct 
* It is claimed (l.163) that the considered setting encompasses things like convex MDP. Can the authors expend on this (from the setting, they do not make the assumption that the return is sum-decomposable, but why would this tell that it can be framed as a convex function of the occupancy measure)?
* Would it be possible to group or recall the properties and assumptions of the link function, as it is a quite central object? For example, should we not assume also that $\sigma(x) = 1 - \sigma(-x)$, or is it a consequence of what is already written? Could you also give some examples of the Lipschitz constants $L$ (Assm 2), for example for the logistic function used in Bradley-Terry?
* There is a typo l. 305 (as written, the gradient is always zero, issue in the second value index)
* Assm 2 and 3, the same notation $L$ is used for the Lipschitz constant of $\sigma^{-1}$ and for $L$-smoothness of $V$. There is not reason for these two values to be the same. They are also confused in the proofs. Would it be possible to restate the results by making them distinct (or at least by stating that it’s for some upper-bound of both terms, if that's enough to make proofs work)?
* In Thm 1 and 2, $M$ is a function of $D$, quantity which has never been defined. Even checking the proofs it is not clear what $D$ is. Please clarify (and this is especially important as it is the number of human raters).
* Corollary 1 doesn’t seem to be proven, even in the appendix, can you provide a proof?
* l. 435, how does $\theta^*$ appear with a telescoping argument (plus, the corresponding equation in the appendix involves $\theta_T$, which seems more logical)?
* Lemma 2, would be helpful to explain why the trim operator is introduced (as the result would hold without the trim according to the proof)
* l. 977, typo (parenthesis)
* l. 1014, is it the same $L$ as in Assm 3?
* the end of proof of Thm 1 is pretty unclear (line 1104 to the end of the proof), which is a pitty, as it is the clever part of the proof discussed l.455-465. Why do we have Eq 1106, and why does it lead (and how) to the equation line 1110? It is claimed to be for the case of large gradient, but line 1119 it is again for the case of large gradient. How is the Eq line 1122 obtained, and how does it relates to the one in line 1107? Do these both equations covers all possible gradient cases, and why? L. 1134, how are combined the bounds (max of them, summing them, something else)? Overall, could you reexplain this overall important part?
* l. 1214, there is a missing term (or the line should be removed)
* l. 1230-1241, why the 3 factor? (not wrong, but why)

### Questions
## Lack of discussion 
* Can you please discuss more thoroughly the limitations of the proposed approach (like the need to have on-policy online human raters), and in more details what are the pros and cons compared to DPO and classic RLHF?
* One advantage claimed compared to DPO is the ability to handle stochastic transitions. However, the focus is also mostly done on LLMS. Can you explain in which case we would have stochastic transitions in this context (and how it is handled by your framework)?
* There is no KL regularization, compared to all other works for doing RLHF (and not without reason). Can you expand on this, is it no longer required (from a practical perspective)?
* The paper claims going « beyond the BT model », but the generalization is rather weak, could it handle more general preference models such as those considered for example in « Nash learning from human feedback » by Munos et al?

## No empirical study
* Given that the analyzed algorithm is not representative of practical approaches, and that the second proposed algorithm is motivated by computational aspects (memory, distributed aspect), would it make sense to at least provide some minimal empirical study (with the proposed algorithms, but also DPO, classic RLHF, online DPO)? Or to provide a clear discussion about why it would not bring interesting evidences?

## Aspects to clarify and/or correct 
* It is claimed (l.163) that the considered setting encompasses things like convex MDP. Can the authors expend on this (from the setting, they do not make the assumption that the return is sum-decomposable, but why would this tell that it can be framed as a convex function of the occupancy measure)?
* Would it be possible to group or recall the properties and assumptions of the link function, as it is a quite central object? For example, should we not assume also that $\sigma(x) = 1 - \sigma(-x)$, or is it a consequence of what is already written? Could you also give some examples of the Lipschitz constants $L$ (Assm 2), for example for the logistic function used in Bradley-Terry?
* There is a typo l. 305 (as written, the gradient is always zero, issue in the second value index)
* Assm 2 and 3, the same notation $L$ is used for the Lipschitz constant of $\sigma^{-1}$ and for $L$-smoothness of $V$. There is not reason for these two values to be the same. They are also confused in the proofs. Would it be possible to restate the results by making them distinct (or at least by stating that it’s for some upper-bound of both terms, if that's enough to make proofs work)?
* In Thm 1 and 2, $M$ is a function of $D$, quantity which has never been defined. Even checking the proofs it is not clear what $D$ is. Please clarify (and this is especially important as it is the number of human raters).
* Corollary 1 doesn’t seem to be proven, even in the appendix, can you provide a proof?
* l. 435, how does $\theta^*$ appear with a telescoping argument (plus, the corresponding equation in the appendix involves $\theta_T$, which seems more logical)?
* Lemma 2, would be helpful to explain why the trim operator is introduced (as the result would hold without the trim according to the proof)
* l. 977, typo (parenthesis)
* l. 1014, is it the same $L$ as in Assm 3?
* the end of proof of Thm 1 is pretty unclear (line 1104 to the end of the proof), which is a pitty, as it is the clever part of the proof discussed l.455-465. Why do we have Eq 1106, and why does it lead (and how) to the equation line 1110? It is claimed to be for the case of large gradient, but line 1119 it is again for the case of large gradient. How is the Eq line 1122 obtained, and how does it relates to the one in line 1107? Do these both equations covers all possible gradient cases, and why? L. 1134, how are combined the bounds (max of them, summing them, something else)? Overall, could you reexplain this overall important part?
* l. 1214, there is a missing term (or the line should be removed) * l. 1230-1241, why the 3 factor? (not wrong, but why)

### Soundness
3

### Presentation
3

### Contribution
3
