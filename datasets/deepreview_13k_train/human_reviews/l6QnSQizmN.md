# Online Reinforcement Learning in Non-Stationary Context-Driven Environments

- Decision: Accept
- Scores: 8, 8, 8, 5

## Abstract
We study online reinforcement learning (RL) in non-stationary environments, where a time-varying exogenous context process affects the environment dynamics. Online RL is challenging in such environments due to ``catastrophic forgetting'' (CF). The agent tends to forget prior knowledge as it trains on new experiences. Prior approaches to mitigate this issue assume task labels (which are often not available in practice) or use off-policy methods that suffer from instability and poor performance. 

We present \bigsys (\sys), an online RL approach that combats CF by anchoring policy outputs on old experiences while optimizing the return on current experiences. To perform this anchoring, \sys locally constrains policy optimization using samples from experiences that lie outside of the current context distribution. We evaluate \sys in Mujoco, classic control and computer systems environments with a variety of synthetic and real context traces, and find that it outperforms state-of-the-art on-policy and off-policy RL methods in the non-stationary setting, while achieving results on-par with an ``oracle'' agent trained offline across all context traces.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes Locally Constrained Policy Optimization (LCPO), a policy gradient algorithm for non-stationary reinforcement learning where the context changes are observed and exogenous. LCPO’s updates are constrained to preserve the policy trained on the past contexts while it maximizes returns on newer samples. Two replay buffers are maintained in order to store the samples belonging to the past contexts and the current context. Whenever the distribution of samples is different in these two buffers, which is detected using an OOD threshold-based detector, then a “regularization” update is performed to preserve past learnings. The proposed approach is tested on a range of environments with a whole suite of baselines to demonstrate its benefits.

### Strengths
* The paper is well-written and easy to read: the introduction is thorough, the related works section is exhaustive, preliminary and the LCPO sections provide adequate details, and the methodology section is well-presented.
* The specific kind of non-stationary problem that the paper considers is well-described. And, the proposed solution fits like a glove to this problem. The approach is also intuitive and parallels the TRPO algorithm.
* The authors evaluate their approach against numerous baselines on several tasks, which provides substantial confidence in the presented results and conclusions. The ablation studies are also welcome, as they offer more insights into the proposed approach.
* The illustrative examples discussed throughout the paper offer an intuitive understanding of various complex ideas – the authors have done a great job of including them.

### Weaknesses
 * The biggest weakness is that the paper considers a specific kind of non-stationarity in the study. Although exogenous processes could be common in real-world scenarios, many other kinds of non-stationarities exist, such as those arising from changes in the agent's embodiment or the reward function itself, and it is unclear whether the proposed approach works well in those cases. Besides, the OOD detector is an important piece in the algorithm and its effectiveness depends on the threshold value – a hyperparameter that is environment-dependent and unknown beforehand. The paper does not discuss how sensitive the performance is to this threshold, and what strategies could be used to choose it in practice.
* The approach also assumes that the context is observed, although it is not used as a task detector or task boundary detector. In many practical cases, the context information is unavailable, and it is unclear how one could use the proposed approach in that case. The paper should discuss potential ways to extend the approach to scenarios with latent context, perhaps by combining it with methods for inferring the context from the agent's history.
* The proposed constrained optimization problem is approximately solved, which in itself is fine, but when paired with the fact that the approach doesn’t use TRPO-style local constraint, the training procedure could be unstable. While the line search procedure attempts to enforce the constraint, it is not clear how this approximation affects the convergence properties of the algorithm, and whether it could lead to oscillations or divergence in some cases.

### Questions
**Decision:**

Although the paper has some weaknesses, the positives outweigh them. The paper is well-executed and it is a good contribution to continual reinforcement learning. Therefore, I recommend an **acceptance.**

**Areas of improvement:**

* The paper should discuss how [1] and [2] are related to the proposed approach. [1] uses a KL constraint on the current policy to be closer to the global policy, and [2] learns a global value function as a baseline estimate for all contexts on top of which the learning happens. It seems like the global policy and the global value functions induce the regularization effect on the past that the paper proposes.
* In Sec 4, the episodic returns are -4 and -6 and not -3 and -5 as mentioned in the paper.
The ablation experiments and the results presented in the appendix can be summarized as one-line bullet points in the main paper.

**Questions:**

* Deep neural networks are known to overfit to the early samples [3], wouldn’t regularizing with respect to the past data exacerbate this process?
* How is the context information different from a task ID?
* In Sec 4, does the A2C use both context and state information to learn the policy?
* Is it possible to approximate the proposed objective in the PPO style as opposed to the TRPO style to avoid using second-order information?
* What happens if the reverse KL is used in the constraint proposed in Eq. 1?
* What is a warm-up period and why is it needed in the experiments?

**References:**

[1] Teh, Yee, et al. "Distral: Robust multitask reinforcement learning." Advances in neural information processing systems 30 (2017).

[2] Anand, Nishanth, and Doina Precup. "Prediction and control in continual reinforcement learning." Advances in Neural Information Processing Systems 36 (2024).

[3] Nikishin, Evgenii, et al. "The primacy bias in deep reinforcement learning." International conference on machine learning. PMLR, 2022.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper addresses "catastrophic forgetting" in continual reinforcement learning with non-stationary dynamics. The dynamics depends on the current context which is observable but can change arbitrarily. A problem in these kind of settings is that the agent over time forgets how to behave in prior contexts. To address this problem the paper proposes a new on-policy algorithm that aims to keep policy updates such that the policy for prior contexts does not change. The proposed approach does not need task labels but only an out-of-distribution detector.

### Strengths
Well written paper. Clear definitions and derivations. The paper explains well all the design decisions in the proposed approach.

The main algorithmic idea of sampling states from the history buffer that differ from the samples currently collected from the environment, and, then using these samples to constrain the policy update is simple and based on the experimental results appears very effective.

I like that the resulting algorithm is an almost straight forward modification of TRPO but for a completely different problem. Note that while being simple the main idea is only obvious in hindsight.

### Weaknesses
I could not find major weaknesses in the paper.

This is not a weakness but just a comment:
Choosing of the out of distribution (OOD) detector is one obvious design decision when running the method in a specific environment. Section 6.2 discusses different thresholds for the OOD detector. Although OOD detection has been discussed in the supervised learning literature, the paper could provide a more thorough discussion on which kind of OOD detectors could be beneficial in which kind of RL environments.

The proposed algorithm places a constraint that aims to keep the new policy relevant for old samples. This constraint replaces the TRPO policy update constraint. The original TRPO formulation results in an approximate natural gradient due to which in TRPO the gradient update does not in principle depend on the parameterization of the (neural network) policy. This property is lost here? Do we get other properties?

### Questions
The proposed algorithm places a constraint that aims to keep the new policy relevant for old samples. This constraint replaces the TRPO policy update constraint. The original TRPO formulation results in an approximate natural gradient due to which in TRPO the gradient update does not in principle depend on the parameterization of the (neural network) policy. This property is lost here? Do we get other properties?

### Soundness
4

### Presentation
4

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
The paper introduces an online RL method for environments with non-stationary (but observable) context, which affects the dynamics/reward. The main difficulty in such settings is catastrophic forgetting; while training the agent on an unobserved context, it forgets the optimal behavior in past contexts. The authors aim to solve this issue by constraining the agent to maintain current behavior for previously-observed contexts, which is possible due to an OOD detector -- basically a distance measure over contexts. To test the proposed method, the authors use a single toy problem and a large amount of benchmarks, the results show that the method indeed surpasses other baselines.

### Strengths
I think the paper is well-written, easy to understand and comprehensive. Notably, the empirical sections present the advantages of the proposed algorithm. For my opinion, with a few minor changes, it passes the acceptance threshold.

### Experiments
The experiments are extensive in terms of both benchmarks and baselines, and show good performance for the proposed method.

### Illustrative Example:
I think this empirical analysis helps to understand what's happening, and shows the value of the method.

### Weaknesses
 **Paper exceeds the 10-page limit**

### Presentation
1. The references within the paper seem to have improper notation (using § instead of Sec.) 

2. I am not sure about the contribution of the opening sentence in the introduction, as this is not the first paper introducing CF, and I do not see any specific relation to the proposed method.

3. Since the method uses a few components, adding a block diagram could help, but is not mandatory in the main body. Such block diagram should show the interconnections at each time step between the buffer, new sampled data, OOD detector, and the agent (policy).

### Related Work:
While not exactly the same, maybe contextual MDPs could be related.

### Minor comments:

1. line 66: "These assumptions are rarely met and lead to poor performance in practice." -- is there any reference to support this claim? If it cannot be backed, you can alter the sentence to be more soft: "...and would likely lead to...".

2. line 268: "proof in §B in the Appendix." -- rephrase.

### Questions
1. Have you tried learning the OOD proxy? e.g., using weighted norm with tunable parameters?

2. You do discuss the differences between your proposed OOD detector and CPD, but have you tried comparing the "whole package"? i.e. using LCPO with CPD.

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
This paper investigates online reinforcement learning (RL) in non-stationary environments, 
where the non-stationarity arises from a time-varying exogenous context process affecting the dynamics.
In particular, they study the catastrophic forgetting (CF) problem.
They propose a new method named locally constrained policy optimization (LCPO),
which combats CF by constraining policy updates for a particular context on prior data from other contexts.
They evaluate their method in the classic control tasks from MuJoCo and computer systems environments.

### Strengths
Whilst this paper is slightly out of my expertise, I think the authors are addressing an important problem as
handling non-stationarity in online RL is important.
To the best of my knowledge, the method presented in this paper seems original.

I particularly liked Figure 1. I would suggest the authors move it earlier in the paper.

### Weaknesses
Overall, I found the paper quite hard to follow. 
The method seems fairly straightforward but the paper lacks a clear and easy-to-follow structure I would expect from an ICLR paper.
I am confused as to why Section 4 "Locally-Constrained Policy Optimization" and Section 4 "Methodology" are different sections.
I would recommend the authors combine these sections as they both explain the method. 
If needed, use sub-sections to structure the content.

Further to this, the figures are not explained thoroughly enough in the text. What does the y-axis in Figures 3 and 4 represent? I assume it is the cumulative distribution function but this should be stated in the paper. 
Further to this, how should the reader interpret the results?
The authors should explain how to interpret the plots, including what the steepness of curves represents, what does it mean
when curves are intersecting, etc?
I suggest the authors check out [rliable](https://github.com/google-research/rliable/tree/master) and use this to create figures.
I am also not sure at what environment step these figures were created for.
Again, this should be clear from the text.

Why are there confidence intervals for Figure 3a but not for Figures 3b or 4?
In Section 6.3, the authors claim that buffer sizes less than $n_b=500$ results in a drop in performance.
I am not sure you can make this claim without showing confidence intervals in Figure 4.

The authors have incorrectly cited throughout the paper. 
The authors should take time to become familiar with when to use textual citations and when to use parenthetical citations.
If using the `natbib` package, the authors can use `\citet` for textual citations and `\citep` for parenthetical citations.
The authors almost always cite such that they should be using parenthetical citations but they use textual citations throughout.

What does the bolding in the table represent?
Does it represent statistical significance under a t-test?
This should be clear from the caption.

# Minor comments
- "Mujoco" should be "MuJoCo"
- Line 191 - the policy is stochastic but on line 112 it's a deterministic mapping.

### Questions
- How can you improve the clarity of the writing?
- How am I supposed to read Figure 3. What does the y-axis represent?
- Why have you used textual citations everywhere?
- What does the bolding in tables represent?

### Soundness
2

### Presentation
2

### Contribution
2
