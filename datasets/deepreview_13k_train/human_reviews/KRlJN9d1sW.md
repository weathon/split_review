# Reinforcement Learning via Lazy-Agent for Environments with Random Delays

- Decision: Reject
- Scores: 5, 6, 5

## Abstract
Real-world reinforcement learning applications are often hampered by delayed feedback from environments, which violates the fundamental assumption of the Markovian property and introduces significant challenges. While numerous methods have been proposed for handling environments with constant delays, those with random delays remain largely unexplored owing to their inherent complexity and variability. In this study, we explored environments with random delays and proposed a novel strategy to transform them into their equivalent constant-delay counterparts by introducing a simple agent called the *lazy-agent*. This approach naturally overcomes the challenges posed by the variability of random delays, enabling the application of state-of-the-art methods, originally designed for handling constant delays, to random-delay environments without any modification. Empirical results demonstrate that our lazy-agent significantly outperformed other baseline algorithms in terms of asymptotic performance and sample efficiency in random-delay environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a derivation and a small-scale empirical analysis that shows random-delay MDPs can be transformed to nearly equivalent constant-delay MDPs by employing a lazy-agent that assumes that all states are (constantly) delayed by the maximum delayed times.

### Strengths
Soundness
======
 The approach is sound, and, albeit a small increment over existing approaches, well demonstrated empirically. The paper lacks an in-depth discussion of the benefits and limitations of the approach. 
	
Significance & Related work
=========
There is no related work section in the paper and thus the significance of the work is not clarified.  

Experimentation
=========
The experimental analysis shows the equivalence of RDMDPs to CDMDPs in BPQL in the MuJoCo environments. 


Presentation
=========
The paper is well written.

### Weaknesses
Soundness
======
The paper lacks an in-depth discussion of the benefits and limitations of the approach. Specifically, the paper does not address the potential for sub-optimal policies arising from the assumption that all states are delayed by the maximum delay. This could lead to an overly conservative agent that does not fully exploit the environment's dynamics when delays are shorter. A more thorough analysis of the trade-offs between the simplicity of the approach and potential performance degradation is needed.

Significance & Related work
=========
There is no related work section in the paper and thus the significance of the work is not clarified. The paper does not situate itself within the existing literature on delayed reinforcement learning. It is unclear how this approach compares to other methods for handling delayed rewards or observations, such as those that use recurrent neural networks or temporal difference learning with eligibility traces. A discussion of how this method advances the state-of-the-art is missing.

Experimentation
=========
There is a need, however, for more in-depth ablation experiments that evaluate the impact of assuming states are processed in order, and of highly varied random delays. The experiments are limited to a few MuJoCo environments and do not explore the performance of the approach in more complex or diverse settings. Furthermore, the paper does not analyze the sensitivity of the approach to the maximum delay parameter, $o_{max}$. It is unclear how the performance would be affected by different values of $o_{max}$ and whether there is an optimal range for this parameter.

### Questions
* What is the performance of the approach in the other MuJoCo environments?

### Soundness
2

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
This paper proposes a way to transform random delay environments into constant delay environments, by imposing the specified maximum delay onto all observed states, regardless of their actual delay. Experiments show that agents trained under this transformation achieve similar results to agents trained in constant delay environments.

### Strengths
1. Nice visual representations e.g. Figure 1 help with understanding
2. The paper proposes a straightforward way to apply an algorithm for constant-delay environments to environments with random delays
3. Convincing number of environments and comparison algorithms used in experiments

### Weaknesses
1. Still requires a maximum number of delay time steps to be specified, which may be unrealistic in some environments (e.g. if observations must be sent over a high-latency network, if the observations require lengthy processing). This would admittedly be a challenging setting to address.
2. Only addresses the issue of large augmented state dimensions if the specified max delay is small.
3. I found the explanation of BPQL a bit confusing, as I don’t see how it avoids state space explosion if you are still training a policy on the augmented state.

### Questions
1. Unsure why you need to wait for $t>2_{o_{max}}$ in line 19 of Algorithm 1, instead of just $t>o_{max+2}$, if the purpose is just to wait until you have the next state/augmented state?
2. In section 3.2 it is stated that the state dimension could become infinite in infinite-horizon MDPs, wouldn’t this only occur if $O_{max}$ was infinite? 
3. Could you provide more details on how BPQL mitigates the state space explosion problem, particularly given that the policy is still trained on the augmented state?

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
The paper introduces Lazy-Agent for handling reinforcement learning in environments with random delays.
Traditionally, state-of-the-art RL techniques assume constant delays, simplifying the learning process but failing to reflect real-world scenarios' complexity.
A Lazy-Agent operates under the assumption that all feedback, such as states or rewards, is delayed by the maximum possible time, even though the actual delay is random.
This method allows the transformation of random-delay environments into constant-delay ones, making it possible to apply conventional RL techniques designed for constant delays.
Rather than reacting immediately, the Lazy-Agent waits for the maximum delay before making decisions.
This simplifies the management of random and unpredictable delays by treating them as constant delays, thereby facilitating the use of existing reinforcement learning methods for delayed feedback.
The paper extends the belief projection-based Q-learning (BPQL) framework, introducing Lazy-BPQL.

### Strengths
- The authors demonstrate that using Lazy-Agent can convert random-delay Markov decision processes (RDMDPs) into constant-delay MDPs (CDMDPs). This transformation allows established constant-delay solutions to be applied to random-delay environments.
- The proposed method is simple and easy to implement.

### Weaknesses
 - For certain tasks (such as Ant, Hopper, Humanoid, and Pendulum), the performance gains from using Lazy-BPQL are minimal.
The reported improvements in performance, when considering standard deviation, are negligible.
 - There is no significant advantage of Lazy Agents over traditional methods in all benchmarks, which raises concerns about the broader applicability of the Lazy Agent model.

### Questions
See weaknesses

### Soundness
3

### Presentation
3

### Contribution
2
