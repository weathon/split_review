# A Trust Region Approach for Few-Shot Sim-to-Real Reinforcement Learning

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3

## Abstract
Simulation-to-Reality Reinforcement Learning (Sim-to-Real RL) seeks to use simulations to minimize the need for extensive real-world interactions. Specifically, in the few-shot off-dynamics setting, the goal is to acquire a simulator-based policy despite a dynamics mismatch that can be effectively transferred to the real-world using only a handful of real-world transitions. In this context, conventional RL agents tend to exploit simulation inaccuracies resulting in policies that excel in the simulator but underperform in the real environment. To address this challenge, we introduce a novel approach that incorporates a penalty to constrain the trajectories induced by the simulator-trained policy inspired by recent advances in Imitation Learning and Trust Region based RL algorithms. We evaluate our method across various environments representing diverse Sim-to-Real conditions, where access to the real environment is extremely limited. These experiments include high-dimensional systems relevant to real-world applications. Across most tested scenarios, our proposed method demonstrates performance improvements compared to existing baselines.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper tackles the problem of few-shot sim-to-real. To mimic this, the experimental setting is consider the setting where a source and target simulator is available. The proposed approach is a penalized variant of a trust region approach, where the reward is maximized with an additional term to minimize a divergence between state (action) marginal in the source vs target simulator. As a result, the method resembles GAIL where the critic is trained to distinguish source vs target simulator + the original MDP reward,  rather than generator vs expert as in the original formulation. The approach outperforms DARC, ANE, and CQL baselines on a suite of environments.

### Strengths
* The approach is novel to my knowledge.
* The approach is relatively simple and makes sense intuitively in my opinion. 
* The approach does not make as many assumptions as related works (e.g. DualDICE's assumption as discussed in section 4.1) and thus can be applied in more settings
* The suite of environments used for evaluation look extensive to me.

### Weaknesses
 * Using state action of the current policy in the target environment as regularization can harm learning, since a suboptimal policy would result in suboptimal state action distribution used for regularization.
* I am confused as to how this approach can work well in the limited data regime. Doesn't the limited quantity of real data limit the ability for GAIL to learn a good discriminator?
* I'm not so convinced by the baselines. First about CQL. From the text, the authors state "it does not leverage the simulator in its learning process". The text also mentions that "FOOD, DARC, and ANE are trained for 5000 epochs in the simulated environment" but does not mention CQL. This leads me to believe that CQL is only trained on the limited real data, but not on simulated data. In that case, I am not clear on what regularization is used. I would think the most obvious way to implement a CQL baseline is to train on simulated data primarily, and use the real data to reguarlize the Q value. This can be done with online Q learning in the simulated enviornment. I apologize if I am misunderstanding here.
* In a similar vein, simple baselines like TD3+BC can be used, where TD3 is done in simulated environment with BC regularization from real data.

### Questions
Could the authors address the points above?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a new sim-to-real transfer algorithm named FOOD for maximizing policy performance in simulation as well as minimizing the state visitation discrepancy between simulation and real environment, so as to achieve high performance considering the dynamics shift. Although the experiments in different simulation environments show the improvement over the DARC algorithm and several other baseline, the proposed trust region method is not novel enough for me as a straightforward combination of RL and IL. The theoretical justification is not directly supporting the proposed algorithm, also the writing is very confusing in several paragraphs, which I think needs further clarification.

### Strengths
The paper proposes an effective method for improving sim-to-real (not truly real-world) domain adaptation performances over DARC baseline. The language is good but the description of methods is not clear.

### Weaknesses
The paper introduces a new sim-to-real transfer algorithm named FOOD for maximizing policy performance in simulation as well as minimizing the state visitation discrepancy between simulation and real environment, so as to achieve high performance considering the dynamics shift. Although the experiments in different simulation environments show the improvement over the DARC algorithm and several other baseline, the proposed trust region method is not novel enough for me as a straightforward combination of RL and IL. The theoretical justification is not directly supporting the proposed algorithm, also the writing is very confusing in several paragraphs, which I think needs further clarification.

 The novelty of the proposed method is not sufficient. It is a straightforward usage of the trust region method for minimizing the policy state visitation divergence from simulation to real environments.

The definition of $V_{imit}^\pi$ in Eq.5 is not provided and this equation is also not justified with proof.

The Alg.1 is confusing for me without additional details. What does it mean by "select best trajectories’’, and what’s the criteria for the "best’’? What are the objectives for updating the value function and imitation value functions? Where does $\mathcal{D}_t$ and $\mathcal{M}_s$ appear in Eq.4? Please clearly indicate these in papers.

I’m also confused by the CQL baseline, which is an offline-RL algorithm. What does it mean by real-world data and simulator in the paper? CQL is just trained on offline data collected by a behavior policy in simulation, with the objective of maximizing its performance for online evaluation in simulation with the same dynamics. Why does it become a baseline method for sim-to-real setting?

### Questions
How is proposition 4.1 related to the practical FOOD algorithms, given that proposition 4.1 shows the bound by state-action-state visitation while in FOOD the imitation learning minimizes the state-action (or state) visitation discrepancy?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on the Sim2Real problem in reinforcement learning. Due to the Sim2Real gap, the well-trained policy from the simulator might perform poorly in real-world scenarios. This paper proposes to constrain the state-action visitation distribution in the real world to be close to that distribution in simulator. Therefore, the policy is optimized for higher returns in the simulator while keeping trajectories that are feasible in the real world. The authors explain the method with theoretical justification, related to trust region approaches (TRPO) and imitation learning approaches (GAIL).

The experiments are conducted on locomotion tasks in OpenAI Gym and Minitaur environment. The proposed method mostly outperforms baselines, including SOTA off-dynamics RL algorithm, SOTA offline RL algorithm and action noise envelope algorithm.

### Strengths
The method is well-motivated with simple intuition. 

The method is solid and supported by theoretical justification.

The experiments are conducted on many classical RL benchmarks with great performance in comparison with baselines.

### Weaknesses
Overall, the technical contribution is not strong enough.

The theoretical part mainly follows derivations from previous paper, such as TRPO. So there is no novel contribution to theory in RL.

The experiments are not extensive enough to fully support the proposed method. See my questions below for more details.

### Questions
1. As for the baseline DARC, why is it necessary to re-implement it in the same RL algorithm as the proposed method? It will be great to see how the original DARC (not the modified one) performs in the benchmarks used in this paper.

2. To fix the Sim2Real problem in robotics, domain randomization is an important approach and generally helps improve the robustness of policy trained from the simulator. Is it possible to add this baseline? Logically speaking, if the domain randomization is strong enough to cover the dynamics in the real world, this baseline can perform really well in the evaluation.  I noticed this paper assumes the simulator is a black box. Is this the reason that domain randomization should not be used as a baseline? Why do we need to be constrained by this assumption?

3. The Sim2Real problem is a critical problem in robotics. This paper will be much more impressive if the proposed method can be evaluated in the real world with the real robot.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a trust-region-inspired scheme for incorporating real-world data into simulation-based (online) RL. Results and comparisons to relevant baselines illustrate that it can perform well, and a sensitivity analysis provides some insight into the key hyperparameter of the method.

### Strengths
- Problem is well-motivated and of great interest to the community
- Literature review is clear and appears to be complete, and in particular points out key ideas which distinguish classes of approaches for this problem and how they relate to the proposed approach
- Experimental construction is clear and well-justified. Experimental analysis is, for the most part, very clear

### Weaknesses
 - First, a general comment about so-called “trust region” methods in RL: upon reading a standard text on nonlinear programming (e.g., Nocedal and Wright, or Bertsekas), I am increasingly dissatisfied with how the RL community seems to neglect some of the key ideas and defining characteristics of trust region methods. I am not trying to pin blame anywhere, but rather suggest that the authors might do well to try and exploit some of these classical ideas in RL. A few examples:
    - Trust region methods sequentially optimize a model of the true objective built around a nominal point, and at every step, constrain the feasible set to a ball centered at that point. In this paper, the objective in (2) does not appear to be a local approximation to the true objective at current iterate $\theta_k$. Perhaps there is room for improvement here?
    - Likewise, a key idea in the design of good trust region methods is that the size of the feasible set changes at each iteration to reflect how closely the previous “model” matched the true objective. How is $\epsilon_k$ varied across iterations? Does it try to capture this kind of model-mismatch? Perhaps this could be a good direction for improvement.
- nit: this kind of work really reminds me of [1]. While I understand the methods are quite different, the basic problem is the same. I encourage the authors to investigate this literature and discuss connections. (I am not an author of this paper, by the way)
- In 3.1 (first paragraph), the subscript notation on $\mathbb{E}$ could be explained more carefully. This leads to ambiguities later on, e.g., in (1) where my best guess is that s and aanare drawn from distributions d, $\pi$ respectively. But clearly these variables are dependent upon one another, and that dependence is not really very clearly expressed in the notation. One could, for example, imagine that (1) is trying to say that we should sample independent copies of the state and action from their marginal distributions. What is really going on here could be easily clarified by being more precise with notation earlier on.
- Similarly, the role of $b_P^\pi$ is not really made clear when it is first introduced or used in (1), and the reader is left to infer what it is from context and use.
- It seems like a key problem the method will have is the estimation of $d_{P_t}^{\pi_\theta}$ from only a few target domain trajectories. Kernel density estimation is known to be data inefficient, and I am quite skeptical about how the IL methods are going to scale here while remaining accurate. Some discussion here would be good, ideally accompanied by experimental results which highlight performance as a function of the amount of target domain data. The authors should also consider the implications of using a fixed bandwidth for the kernel density estimation, especially in high-dimensional state spaces, and discuss how this might affect the accuracy of the estimated distribution and the overall performance of the algorithm.
- nit: it is a bit odd that the Nachum 2019 paper is mentioned as coming chronologically after (“then used…”) Touati 2020.
- I do not follow the brief discussion in the sentences above section 4.2.
- Proposition 4.1 does not make much sense to me, although the proof steps are indeed straightforward. What I mean is this:
    - First off, so far as I see, the variable J is never defined anywhere.
    - Relatedly, it is unclear if this result is intended to apply at each iteration of the proposed approach, or to its final result, or even if it has any relationship to the proposed approach (i.e., is it just a general result about sim-to-real?). Relatedly, I suspect (but could not point to a specific paper) that this result is known in the literature since it does not clearly pertain to the proposed algorithm. Perhaps I am just confused. Help me to understand.
    - There is no mention of $\epsilon$ anywhere in the result. Surely the size of the feasible set should influence performance of the proposed algorithm.
- nit: in the caption for table 1, I do not see how one can “minimize the state(-action) visitation distribution” itself. One can minimize a metric of that distribution, but not the distribution itself, right?
- In the experimental protocol paragraph, the bit about removing trajectories that perform poorly in the real environment confuses me. Isn’t that phenomenon exactly what the proposed method is trying to fix? Wouldn’t seeing state transitions that result in poor performance be essential?
    - OR, as I suspect, what is going on here is really that the “trust-region” constraint/regularizer is effectively saying that the simulation has to visit the same states/actions as the real environment (regardless of how much reward they accrued). Something seems strange about this. Comment would be appreciated.
- Dividing the stddev by two in plots is a good indication that results are insignificant… It is also totally statistically useless when computed from 4 random seeds. Why not just show the min and max of all runs? These kinds of statistics are misleading at best -  this kind of thing is common in the literature, and I think it is high time that the community fix such mistakes. The use of standard error bars with such a small sample size is not statistically sound and does not provide a reliable measure of the variability in the results. The authors should acknowledge the limitations of this approach and consider alternative ways of presenting the data, such as showing individual runs or using non-parametric methods.
- The discussion below Fig. 1 is confusing to me, and not particularly convincing. For example, how could “a high value induce the agent to replicate real environment trajectories” result in “behavior close to RL_sim?” What am I missing here? More generally, I really don’t see much of a pattern in the figures - it seems like everything is very environment dependent, and as above, I would not draw statistical conclusions from such little data. The interpretation of the hyperparameter \alpha and its impact on the agent's behavior needs further clarification. The authors should provide a more detailed explanation of how \alpha influences the trade-off between replicating real-world trajectories and optimizing for reward in the simulation environment. Additionally, the lack of clear patterns in the figures and the high environment dependency suggest that the method's robustness and generalization capabilities need to be further investigated.
- Last, I feel it is a bit unfortunate that a paper on “sim-to-real” did not actually test anything in the real “real world.” Why not try something on a real robot or other setup and put things to the test? I certainly understand that such a test means a lot of work, but it would also go a long way to illustrating the practicality of the proposed method. For instance, there is precious little discussion of the real-world data complexity of the method!

### Questions
see above

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
