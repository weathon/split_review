## Human Reviewer 1

### Summary
The model introduces a binary persuasion problem of a long-lived designer interacting with a sequence of short-lived agents that learn from the prior action sequence. This problem is related to social learning among LLM agents as well as human societies. They prove tractability of the model with Bayesian agents and investigate non-Bayesian LLM agents in simulations.

### Strengths
The paper thoroughly sets up its problem, and is very well-written. I found the integration of experiments alongside a (mostly) theory paper convincing, as the authors stated departures from their Bayesian assumption in the beginning of their experiments section.

### Weaknesses
The paper considers and names several restrictions in particular on the information structure and short-livedness of agents, but does not say something on how these affect outcomes. While I understand that for the tractability of the theoretical model all of them are essential, the fact that the authors run experiments would allow for an investigation of what other dynamics are possible with variations on, e.g., the stringent public information assumptions.

### Questions
- Does your setting admit a revelation principle?
- (LLM-)Experimentally, which assumptions lead to significantly different dynamics compared to your current simulation exercise?

### Soundness
4

### Presentation
4

### Contribution
4

### Rating
8

### Confidence
3

---

## Human Reviewer 2

### Summary
This paper introduces a formal framework for controlled social learning where a centralized planner (e.g., an LLM-based mediator) chooses the precision of private signals sent to sequential agents. The planner can be altruistic (maximizing social welfare) or biased (steering agents toward a preferred action), and faces costs for altering signal precision. The authors characterize optimal planner policies as functions of evolving public belief, prove structural properties (e.g., convexity of the altruistic value function), and show how informational externalities shape long-run outcomes. LLM-based simulations validate the theory, revealing that adaptive planners can substantially influence collective beliefs and welfare and that modern LLMs can exhibit emergent strategic behaviors—highlighting both opportunities and risks of algorithmic information mediation.

### Strengths
- The understanding and introduction of Bayesian persuasion (information design) are accurate.
- The entire article is presented well, with a clear structure and easy to understand.

### Weaknesses
**1**

Currently, this manuscript appears to lack sufficient literature review, which makes the position and contribution problematic.

Contribution 1 is not as claimed. The authors claim:
> We introduce the first formal model that integrates a dynamic control problem for a centralized information planner with the mechanism of sequential social learning.

There is a series of articles that the authors have not considered: the combination of Bayesian persuasion (information design) and RL. In fact, in the past 5 years, there have been a large number of variants such as online persuasion and multi-receiver variants, etc. (while the authors' citations on information design are the latest only up to 2000).

Talking about RL is not off-topic—considering that the authors position their article as a control problem (dynamic programming). Then this series of articles must at least be discussed.

Farsighted agents is also a rapidly developing topic in the persuasion community. The social learning mentioned in this manuscript is indeed a novel point, but it is also a common problem in the multi-agent RL field. Therefore, the claim of contribution 1 is incorrect.

In addition, the citations on LLM on information design / Bayesian persuasion are not comprehensive enough (only focusing on the work of two or three labs), and the discussion is too limited.

**2**

This manuscript is submitted to the Primary Area: alignment, fairness, safety, privacy, and societal considerations.

However, this manuscript is about a stylized dynamic programming problem with a lot of assumptions. According to the authors' position, it seems that the entire related part should be in Section 6: EVALUATION VIA LLM-BASED SIMULATION.

The steps in section 6 by the authors are: “analyze the behavior of LLM agents to identify key deviations from Bayesian rationality”. The remaining logic seems to be: LLM is non-Bayesian, but LLM can still exhibit results that do not deviate much from the theoretical analysis results of Bayesian-rational agents.

Regarding the player setting, there are 2 gaps:

- non-Bayesian players vs human; non-Bayesian is a very rough concept, as long as it does not perfectly conform to Bayesian rationality, it counts. This is just one trait of humans. Not satisfying Bayesian rationality is not sufficient to conclude that it is close to humans. Humans have many other traits, and from an agent-based perspective, they can also be endowed with different personalities.
- LLM vs human; this point is currently very controversial in the literature.

Therefore, the authors' experiments may only illustrate that this algorithm has a certain robustness and can have good effects even when agents do not satisfy Bayesian-rationality. But this cannot indicate that this algorithm is more realistic, nor can it be said to be an effect brought by LLM.

In addition, the main text does not provide the LLM's role-play settings, and the experiments do not involve human participation or human data. Therefore, I believe the experiments and their claims are mismatched.

**3**

The abstract must be changed to a single paragraph.

### Questions
N/A

### Soundness
2

### Presentation
3

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper studies how a social planner can intervene on signal strength in the information cascade model to induce both altruistic and biased outcomes. The authors derive optimal policies for the planner in both cases, in both the setting where the social learning aspect is ignored and when the social learning aspect is taken into account. They then study these dynamics with LLMs posing as the agents, the social planner, and a belief oracle.

### Strengths
The main contributions of this work are theoretical results for intervening on signal strength and an interesting experimental setup to evaluate the theoretical results. I am not aware of this particular style of intervention, and I am excited to see clear and insightful theoretical work in this vein. The paper is also clearly written and laid-out.

### Weaknesses
Some small recommendations:
1. include more of the experimental setup in the main body. It would just help to clarify how exactly you set this up with prompting etc.
2. the theorems may benefit from diagrams to show what the policies are in the different regimes. 
3. worth having one extra line about computation about $\tilde{b}_i$ in the main body as otherwise it is quite mysterious to the reader since it is a crucial point.

### Questions
-

### Soundness
4

### Presentation
4

### Contribution
4

### Rating
8

### Confidence
2

---

## Human Reviewer 4

### Summary
This paper revisits sequential social learning (Bikhchandani et al.) and adds a centralized planner who, at each step, chooses the precision of the next agent’s private signal. Agents best respond given the public belief and the stated precision. The planner’s problem (altruistic vs. biased objective) is cast as an infinite‑horizon discounted MDP in the public belief state. A key theoretical contribution is proving that the altruistic optimal value function $V^*_A$ is convex in belief, which underpins a threshold‑type policy structure; the paper also reports LLM‑based simulations.

### Strengths
The convexity proof of $V^*_A$ is neat.  It gives a clear policy structure and may be useful for other related problems, e.g., dynamic information acquisition, and sequential contract design.

### Weaknesses
- The model is a little too restrictive.  It is not clear if their result can go beyond symmetric binary signal setting.
- The LLM experiment require more cares.  Figure 1 is misleading, as the value of prior and posterior are self-reported by LLMs.  Similarly, they should validate the strength of the signal from the oracle agent, e.g., asking another LLM to guess q_i.  I do not feel comfortable comparing those values with Bayesian models.


### Miner issue
- The theorem statement can be clearer.  For instance, though Theorem 1 only works for $\delta = 1$, Theorem 2 should hold for all discount factors $\delta<1$. 
- Equation (28) should depend on prefix of the trajectory but $P^*_\lambda$ seems to the probability of whole trajectory.
- You may try to simplify the proof by using dynamic programming (Bellman operator) or coupling.

### Questions
Instead of a symmetric binary signal and 01 loss, how is the result generalized to a general signal and a loss function?

### Soundness
3

### Presentation
2

### Contribution
4

### Rating
8

### Confidence
3