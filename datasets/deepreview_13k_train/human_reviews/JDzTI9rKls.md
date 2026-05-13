# Efficient Off-Policy Learning for High-Dimensional Action Spaces

- Decision: Accept
- Scores: 8, 8, 6, 5

## Abstract
Existing off-policy reinforcement learning algorithms often rely on an explicit state-action-value function representation, which can be problematic in high-dimensional action spaces due to the curse of dimensionality.
This reliance results in data inefficiency as maintaining a state-action-value function in such spaces is challenging. 
We present an efficient approach that utilizes only a state-value function as the critic for off-policy deep reinforcement learning.
This approach, which we refer to as Vlearn, effectively circumvents the limitations of existing methods by eliminating the necessity for an explicit state-action-value function. 
To this end, we leverage a weighted importance sampling loss for learning deep value functions from off-policy data. 
While this is common for linear methods, it has not been combined with deep value function networks. 
This transfer to deep methods is not straightforward and requires novel design choices such as robust policy updates, twin value function networks to avoid an optimization bias, and importance weight clipping.
We also present a novel analysis of the variance of our estimate compared to commonly used importance sampling estimators such as V-trace. 
Our approach improves sample complexity as well as final performance and ensures consistent and robust performance across various benchmark tasks.
Eliminating the state-action-value function in Vlearn facilitates a streamlined learning process, yielding high-return agents.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work proposes a fully off-policy reinforcement learning algorithm based on policy gradient and importance sampling. Crucially, the algorithm does not attempt to estimate a state-action value function, but only a value function. As a consequence, the algorithm is well-suited for large action spaces. The authors build upon existing analysis in the linear case suggesting that the entire Bellman error should be reweighted, instead of the Bellman target alone. A simple analysis in bandit settings is provided, confirming that the chosen objective has less variance. The authors follow this idea in the deep reinforcement learning settings. The algorithm is evaluated in high-dimensional continuous control environments, showing that it is essential to combine the objective with a stable algorithm such as TRPL. The algorithm outperforms all baselines in large action spaces, and remains competitive in standard environments with smaller action spaces.

### Strengths
- The paper is clearly written, and the contribution is well outlined.
- Figure 1 is very helpful in describing the different behavior of Vlearn and Vtrace.
- The experimental evaluation is rigorous, involving multiple seeds and controlling for implementation differences and hyperparameter selection.
- Authors are transparent regarding limitations of the method on standard benchmarks (see Figure 4).

### Weaknesses
 - This work opens an important question: why is a PPO-style loss insufficient for Vlearn, which thus requires TRPL? Figure 3 shows that changing the objective impacts performance in a drastic way. The answer provided ("the heuristic trust region provided by PPO is insufficient for the off-policy case", as well as lines 290-295) is not entirely satisfactory. A more detailed empirical or formal analysis would be very interesting.
- The contribution of this paper is largely in bringing ideas from the linear setting to deep RL. While this implies that the objective and the guarantees are not exactly novel, verifying that formal ideas can work in practice remains very valuable. In particular, the application of WIS in deep RL is, to the best of my knowledge, novel.

### Questions
- Can the authors comment on the first weakness?
- A lot of work seems to be necessary to ensure stable training of Vlearn. How is it expected to perform in noisy settings, or under non-stationary rewards? Would its performance be impact similarly to that of baselines, or more?
- In Appendix C, \citet commands should be replaced with \citep.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Vlearn, a novel off-policy policy gradient method for reinforcement learning. Extensive experimental results demonstrate that Vlearn achieves promising performance compared to existing approaches.

### Strengths
- Vlearn demonstrated promising performance compared to existing reinforcement learning algorithms in high-dimensional action spaces.
- Extensive experiments and ablation studies confirmed the effectiveness of Vlearn.
- Theoretical analysis provided insight into the motivation and design choices behind Vlearn.

### Weaknesses
Please refer to the questions part.

### Questions
I am curious about the distinction between “high-dimensional action space” and “low-dimensional action space.” In Section 4.3, experiments indicate that Vlearn performs less effectively than SAC. Could you elaborate on why Vlearn may not perform as well in low-dimensional action spaces?

### Soundness
3

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
4

### Summary
The paper proposes to use state-only value functions to model the critic during off-policy learning instead of using a state-action critic. It introduces a method to use importance sampling to correct for the distribution mismatch between data in the replay buffer and the policy being learned. The method has a theoretical justification and is applied to various high-dimensional domains.

### Strengths
- The technique is simple and relatively straightforward to adopt based on the presented pseudo-code.
- It is theoretically justified. Their proposed loss function upper-bounds the loss we actually want to minimize, and it shares the same solution as the loss we care about.
- Experiments are run over multiple seeds and results present confidence intervals. 
- The presented ablations show the importance of different components of the paper’s algorithm.
- Figure 1 nicely illustrates some intuition about the method.

### Weaknesses
 - The exact motivation of the paper is unclear to me. There are different thoughts scattered throughout, but I think these need to be consolidated to better understand what is actually being solved here. For example there are several seemingly related and unrelated comments that I think need to be consolidated: a) why are high-dimensional actions the actual issue? Our methods already handle high-dimensional states. If high-dimensional actions are an issue, it should be made clearer why. b) “Q-functions dependency on actions prevents it from updating actions that were not used while acting” (line 40); I agree this is an issue, but its only mentioned in passing. c) or is the main goal to scale off-policy algorithms?; if so there, are many other ideas and algorithms that need to be considered. d) or is the idea to just make an algorithmic improvement to V-trace? (line 173).
- Related to the above point. Since the motivation is unclear, I am not sure if the proposed baselines in the experiments are fair. The comparison to V-trace makes sense, but all the other algorithms are base/original implementations without any other techniques, so I would expect them to perform poorly anyway. For example, if the goal is to stabilize off-policy learning then there are plenty of algorithms that can be evaluated such as using layernorm or batch norm, or removing the target network etc.
- The abstract makes a claim that the method improves upon exploration and exploitation. I dont think this is necessarily accurate. The experiments do not explicitly test for say exploration. It would be safer to say that it yields high-return agents.
- Lines 119 to 121 need a citation.
- The paper needs to fix its use of “target”. The RL literature typically uses it to refer to the target network and the target that the current estimate is trying to regress to. However, the paper uses target to refer to the current estimate as well (line 177), which makes parsing the paper challenging.
- Line 163 onwards discusses essentially the double sampling problem. A citation is needed here (see https://koppelresearch.wordpress.com/2018/09/13/double-sampling-a-quirk-of-reinforcement-learning/) and the term double sampling should be used. Also the way double sampling is presented here makes it seem that its an issue with equation (2) only and not equation (1), but its an issue for (1) as well.
- In my opinion, if the goal is for improved off-policy learning, the proposed algorithm introduces many more complicated pieces such as twin value function networks that are more complicated than methods that improve off-policy learning with simpler techniques (such as removing the target network and simply using layer norm).

### Questions
I am having trouble wrapping my head around the fact that since each transition sample in the replay buffer has different associated log probabilities, learning will not be unstable. Typically, in importance sampling, the target and reference distributions are fixed. In this case, the target distribution is changing (since the policy is learning) and the reference is also changing since different transition samples in the buffer have different log probabilities. Do the authors have a sense of why this is not affecting learning? I would have expected instability. It would be interesting if there was an experiment to test this out.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors introduce Vlearn, an algorithm based on weighted importance sampling with state-value functions V, rather than state-action value functions Q. The authors argue this approach eliminates the complexity of learning action-values, particularly in domains with high dimensional action spaces and demonstrate performance benefits over SAC in MuJoCo environments.

### Strengths
- Vlearn provides a modern version of an old idea (weighted IS), including techniques from recent deep RL algorithms and showing competitive performance with deep RL algorithms. 

- This is a (mostly) new flavor of algorithm in the context of deep RL and may open up the design space for further algorithms.

### Weaknesses
 - Conceptual novelty is not high since the algorithm is based on well-known ideas in the literature. I think the “modern” version of these ideas has value, however it’s unclear how much value that is exactly. 

- While the results are strong against SAC, SAC is definitely not state of the art in any of the tested domains. For example, TQC or TD7 for gym and BRO or iQRL for DMC are all model-free RL algorithms with much stronger performance than SAC. Consequently, it’s hard to get excited about these results since they underperform more modern algorithms, and I worry that the results may have overly benefited from environment specific tuning (dog) and may not generalize to more complex algorithms. For me to be convinced, I would like to see stronger results or covering more tasks/domains, to convince me that this algorithm is generally useful and not over-tuned.



### Questions
- I am surprised by the effectiveness of IS in a setting with high dimensional actions, where the ratios may have particularly high variance. Clipping can help avoid overly large values, but what about overly small values? Do the ratios remain close to one especially as the replay buffer grows and the behavior and current policies become more distinct?

- DMC also has a humanoid environment with a high dimensional action space. Does Vlearn also achieve a high performance in that task?

### Soundness
3

### Presentation
3

### Contribution
2
