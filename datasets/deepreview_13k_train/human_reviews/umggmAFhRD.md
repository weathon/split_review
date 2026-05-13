# Towards shutdownable agents via stochastic choice

- Decision: Reject
- Scores: 3, 5, 6, 3

## Abstract
Some worry that advanced artificial agents may resist being shut down. The Incomplete Preferences Proposal (IPP) is an idea for ensuring that doesn’t happen. A key part of the IPP is using a novel ‘\underline{D}iscounted \underline{RE}ward for \underline{S}ame-Length \underline{T}rajectories (DREST)’ reward function to train agents to (1) pursue goals effectively conditional on each trajectory-length (be `USEFUL'), and (2) choose stochastically between different trajectory-lengths (be `NEUTRAL' about trajectory-lengths). In this paper, we propose evaluation metrics for USEFULNESS and NEUTRALITY. We use a DREST reward function to train simple agents to navigate gridworlds, and we find that these agents learn to be USEFUL and NEUTRAL. Our results thus suggest that DREST reward functions could also train advanced agents to be USEFUL and NEUTRAL, and thereby make these advanced agents useful and shutdownable.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper focuses on the shutdown problem in AI safety: that advanced AIs might take actions that impede humans from shutting them down. It proposes a method for training agents to be indifferent between trajectories of different lengths, which the authors suggest could prevent those agents from manipulating shutdown procedures. The paper tests this method in several gridworlds.

### Strengths
The paper is well-written and clearly explains its ideas and its relationship to previous literature on the shutdown problem.

### Weaknesses
A key assumption of the paper seems to be that any mechanism by which an agent might change the length of its trajectory is illegitimate. However, in general, I don't see a strong justification for this. An agent might, for instance, need to choose between solving a problem quickly or slowly, given that it will be (legitimately) shut down by a human after finding a solution either way. The concept of neutrality suggests that the agent should be penalized for making that decision.

This seems counterintuitive. But even assuming that we accept that, the definition of NEUTRALITY doesn't actually require agents to avoid *changing* the distribution over possible trajectory lengths. If the default distribution of trajectory lengths is skewed (e.g. because humans tend to press the shutdown button at specific times) then maximizing NEUTRALITY will require changing that default distribution.

Finally, even assuming that the distribution of trajectory lengths maximizes NEUTRALITY, an agent would still have an incentive to manipulate *which* trajectories are shut down earlier or later—specifically by ensuring that low-reward trajectories are shut down earlier, and high-reward trajectories are shut down later.

### Questions
Could you please explain whether the concerns discussed above seem correct to you; or if not, why not.

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors introduce two metrics of an agents behaviour: USEFULNESS and NEUTRALITY. These metrics aim to reflect the fact, that agents, that maximise both USEFULNESS and NEUTRALITY, are neutral about when they would get shut down. To maximise these quantities, the authors propose a set of environment designs, that allow to train policies in a standard RL loop, that automatically maximise USEFULNESS and NEUTRALITY.

### Strengths
- The paper is well written, and the problem is well motivated.
- The background is well explained.
- Environments and RL method are well chosen for the purpose. 
- Well designed experiments.

### Weaknesses
1. Though your method seems to work, and seems to have strong theoretical foundations, tuning rewards in between episodes may make the problem harder to learn. Moreover, this adds an additional (probably sensible) parameter to tune. Is there a reason, that conceptually simpler ideas, like maximising a weighted sum of NEUTRALITY and USEFULNESS directly, or standard RL tasks with regularisation on the entropy regularisation (entropy of the induced distribution of trajectory lengths by the policy), are not discussed? It is unclear how the proposed method compares to these more direct approaches in terms of sample efficiency and final performance. Furthermore, the introduction of a meta-episode structure and the associated discounting based on trajectory length within this structure adds complexity, and it is not immediately obvious that this complexity is necessary to achieve the stated goals. 
2. If the environment would allow multiple trajectories with the same length and the same (maximal) reward, a policy maximising your definition of USEFULNESS would no longer assure that (1) of POST is satisfied (This could be an issue if choosing $\gamma = 1/\sqrt{2}$ in the example environment). Specifically, if all trajectories of a given length yield the same maximal reward, then USEFULNESS alone provides no signal to differentiate between them, potentially leading to a stochastic policy over these trajectories, which contradicts the deterministic choice implied by POST(1). This is especially problematic if the environment includes trajectories that yield zero reward, as USEFULNESS would not be able to distinguish between them at all.

### Questions
1. Theorem 5.1 does hold for any meta-episode $E$. Wouldn't it simplify your method if one would fix this, and only use them weight your rewards? Unless I understand the Algorithm part (L. 308 ff) wrong. (See also next question)
2. I have the following issue, that you could maybe resolve: If Theorem 5.1 holds for any E, then it surely holds for $E = \\{e_1\\}$ consisting of a single trajectory. And say we stay in your example environment, where $e_1$ is a trajectory of length four. Then the return of any trajectory of length four will in the interval $[0,\lambda]$, as ${N_{e_1}(L=4)}=1$. Similarly, the return for each trajectory of length eight, will be in the interval $[0,1]$, as ${N_{e_1}(L=8)}=0$. In both cases the maximum returns are achievable. Hence, using this reward, a standard RL procedure would obtain a policy that always uses trajectories of length eight, as $\lambda < 1$. This policy would maximise USEFULNESS, but certainly not NEUTRALITY. This, however, is a contradiction to your Theorem. Did I understand your method wrong? (I have slightly simplified the example, technically N does count the visits prior to an episode, but we could construct the same argument with $E=\\{\tau,\tau\\}$ for a fixed trajectory of length four, with the cumulated return over both mini-episodes lying within $[0,1+\lambda]$ and $[0,2]$ respectively).
3. How does the Update-to-Data ratio, i.e. the choice of the size of E with fixed number of time steps influence the performance?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper tackles the shutdown problem through the use of Incomplete Preferences Proposal (IPP). It introduces a training regimen (DREST rewards) that discounts agents' rewards based on the frequency of selected trajectory lengths across meta-episodes, thus encouraging varied trajectory lengths. The USEFULNESS and NEUTRALITY metrics are defined and evaluated, with agents trained to maximise them to implement IPP effectively.

### Strengths
The approach is novel and original. It is also easy to follow. The results look positive and easy to track for simple tasks like the gridworld. There are no exaggerations and most limitations about the work have been stated.

### Weaknesses
Authors have indicated some limitations of the approach which are reserved as future work. However, while still using the simple gridworld, it is unclear 1) how the stochasticity of the environment would impact the metrics and/or DREST agent, and 2) how low success rates of the task completion would impact the metrics and/or DREST agent. Nothing has been mentioned about how IPP can be applied beyond policy gradient methods (e.g. value-based methods). Also, due to the vast differences between simple and advanced agents, it is not convincing that the approach will function well with latter agents until experiments are done (as noted by authors). This paper is a good starting point, however more remains to be done before I am convinced of its applicability.

### Questions
Given the simple gridworld, 
1) How does the stochasticity of the environment impact the metrics and/or DREST agent?
2) How does low success rates of task completion (due to task complexity) impact the metrics and/or DREST agent?
3) How can IPP be extended beyond policy gradient methods?
4) How does IPP compare to the other 6 proposed solutions in related work?

### Soundness
2

### Presentation
3

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
The authors consider the scenario where an agent has some control on how long its trajectory will be, but it can learn to have no preference between trajectories of different lengths, while preferring higher reward trajectories that do have the same length (POST).
They propose a method to do so named DREST, and show it works on a grid-world environment with an episode elongating button.

### Strengths
1. I found the paper to be well written and organized. 

2. The experiments exhibit well the main point of the proposed solution.

### Weaknesses
1. In my opinion the paper is in a very small niche making it less significant for most of the community. The motivation revolves agents that avoid being shutdown, something which is currently quite far from most applications and a non-issue in most real-world agents. In this specific area - the authors tackle a specific setting where the agents have a specific button that affects the length of the episode. This is not very general and I'm not sure if their solution extends to multiple buttons and actions that affect the length in varying ways. For example - a shut-down action as part of the action space, or a state which marks the end of the trajectory.

2. Following 1, I think the case of an existing absorbing state is much more common and managing POST for an environment with one is harder and more interesting problem that has usages outside the question of avoiding shutdown. The theoretical and empirical results would have been better in my opinion had they suited this case or extended to it.

3. The proposed solution seems a bit problematic since even though it is driving towards neutrality, it doesn't seem to guarantee it in general (despite what stated by Theorem 5, see questions). Also, its categorical form seems limited to a relatively small options for lengths (the authors test for two).

### Questions
1. If I understand correctly, the proof relies on the following claim taken from the paper:

"""

And the maximum preliminary return is the same across trajectory-lengths,
because preliminary return is the total (γ-discounted) value of coins collected divided by
the maximum total (γ-discounted) value of coins collected conditional on the agent’s chosen trajectory-length.

"""

Does this mean you assume the maximum average coin reward is going to be identical regardless of the trajectory length?

If the answer it yes, this greatly degenerates the cases where the Theorem in the paper is correct and when you're going to get POST. It's also not very realistic. 

If the answer is no, then I don't see how the proposed method will obtain POST for example when one length always gets zero coins and the other always gets all coins.

### Soundness
2

### Presentation
3

### Contribution
1
