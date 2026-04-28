# Learn from Interactions: General-Sum Interactive Inverse Reinforcement Learning

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 3, 3, 6

## Abstract
This paper studies the problem that a learner aims to learn the reward function of the expert from the interaction with the expert and how to interact with the expert. We formulate the problem as a stochastic bi-level optimization problem and develop a double-loop algorithm "general-sum interactive inverse reinforcement learning" (GSIIRL). In the GSIIRL, the learner first learns the reward function of the expert in the inner loop and then learns how to interact with the expert in the outer loop. We theoretically prove the convergence of our algorithm and validate our algorithm through simulations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces the General-Sum Interactive Inverse Reinforcement Learning (GSIIRL) framework, which uses inverse reinforcement learning to enhance the learner´s policy optimization process in a multi-agent setting. In GSIIRL, a learner agent interacts with an expert to infer the expert´s reward function, using this insight to adapt its policy within a general-sum environment without assuming equilibrium conditions.

### Strengths
1. **Structured Learner-Expert Framework:** GSIIRL´s learner-expert setup, where the learner infers the expert´s reward and adjusts its own policy, provides a unique structure within multi-agent IRL. This interaction-focused approach enables the learner to balance its intrinsic rewards with its understanding of the expert´s objectives in a general-sum setting, which is an important extension to IRL in interactive environments.
2. **Flexibility in Non-Equilibrium Scenarios:** Unlike methods like MA-AIRL, which often rely on equilibrium assumptions, GSIIRL operates without this requirement, making it well-suited to dynamic, real-world environments where equilibrium conditions may not be guaranteed.
3. **Theoretical Analysis:** The paper provides theoretical convergence guarantees and error-bound analysis, strengthening the reliability of the GSIIRL framework.

### Weaknesses
1. **Simplistic Expert Reward Structure:** GSIIRL currently assumes a single, static reward function for the expert, which may limit its flexibility in more complex environments where the expert´s objectives could adapt dynamically in response to the learner´s actions. This static assumption places GSIIRL closer to frameworks like MA-AIRL, which also assume fixed rewards, potentially reducing the depth of interactions in dynamic multi-agent scenarios. Specifically, the use of a single, unchanging reward function prevents the expert from exhibiting more nuanced behaviors, such as shifting priorities or adapting strategies based on the learner's observed policy. For instance, in a competitive game, an expert might initially prioritize exploration but later switch to exploitation; GSIIRL, as currently formulated, cannot capture such dynamic shifts.
2. **Assumption of Observability:** As recognized by the authors, the assumption of full access to state-action pairs limits GSIIRL´s practicality, especially when compared to frameworks like MA-AIRL, which are designed to operate under partial observability. This limitation is significant because many real-world multi-agent systems involve scenarios where agents have only limited or noisy observations of the environment. The requirement for full observability restricts the applicability of GSIIRL in such settings, making it less versatile than methods that can handle partial information.

### Questions
1. Could the authors elaborate at a high level on whether the GSIIRL framework could be extended to operate under partial observability? Additionally, how would such an extension theoretically impact the framework´s reward inference and policy optimization, especially regarding convergence guarantees and error bounds?
2. Could the authors discuss the rationale behind using a single, static reward function for the expert, rather than a structure with both intrinsic and learner-responsive components? How might incorporating a more flexible, adaptive reward structure for the expert impact the framework´s effectiveness in dynamic multi-agent environments?

### Soundness
3

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
3

### Summary
This paper proposes a novel framework for general-sum interactive inverse reinforcement learning (IRL) where a learner aims to infer the reward function of an expert through interaction rather than passive observation. The authors introduce a stochastic bi-level optimization approach, embodied in their General-Sum Interactive Inverse Reinforcement Learning (GSIIRL) algorithm, which features a double-loop structure: the inner loop learns the expert’s reward function, while the outer loop refines the learner’s policy. Unlike traditional IRL methods focused on fully cooperative or competitive setups, this approach allows for complex interaction dynamics, where the learner’s reward can be decomposed into expert-dependent and expert-independent parts.

### Strengths
I am afraid it is difficult to find a strength in its current state.

### Weaknesses
Please see comments for details on weaknesses and what must be improved.
# The Writing

The writing is in bad shape and must be improved drastically.

- There are language errors such as "Until now, IRL has been applied to
different areas." where the use of "until" is wrong. Also, there are many vague statements such as "Current state-of-the-arts (Ziebart
et al., 2008; Abbeel & Ng, 2004; Ziebart et al., 2010; Bagnell et al., 2006; Finn et al., 2016) solve this problem with different approaches." that does not describe any of these approaches and do not add any content to the paper. These kinds of vague and generic statements must be immediately concretised afterwards, or not be made at all.

- "The aforementioned works are only focused on a single expert and a single learner. In the real world,
many scenarios have multiple experts interacting with each other in the environment." -- Here it s not clear whether you are talking about a dataset of demonstrations for a single-agent task performed by different experts, or a multi-agent task. Also, what are these real-world scenarios? You should give an example immediately after this statement, otherwise again it is hand-wavy and vague.

- The whole of Introduction is extremely convoluted, filled with vague statements, and difficult to read. This needs to be re-written entirely with a good flow and with proper scientific writing. Right now, it reads like the draft of a draft. By the time I reach line 74, I still have no idea what the paper is about. It is also extremely difficult to assess the paper's relation to previous work because of how convoluted the introduction is. Is this multi-agent IRL? Is this single-agent multi-expert IRL?

- The Related Works should be a section, not a \paragraph inside the Introduction. In the Related Works, you do not need to include all the different things bi-level optimization is used for. Those are not related works to your paper. Your related works should contain related inverse RL papers and how your work differs from them. Right now, this paragraph is a long and unnecessary background on bilevel optimization.

# The Novelty and Problem Setting

I believe the paper's problem statement is wrong, in the sense that, it does not require the use of inverse RL, and IRL is not justified in any other way either.

- In the motivating example, the robot's goal is to compute an optimal policy with respect to a reward function that depends on the human. So this seems like it is a two-agent setting where there is a robot and a human. In Section 2, it is unclear where the inverse RL is needed. Any model-free multi-agent RL algorithm that can solve a Markov Game can be used to compute a good policy for robot here, because the robot gets to observe its rewards even if it does not know the function. This is standard model-free RL.

- The paper must cite the "Efficient Inverse Multiagent Learning" work (https://openreview.net/forum?id=JzvIWvC9MG) and make similar comparisons to their work and works mentioned in Table b. Specifically, the bilevel optimization method presented here looks extremely similar to the minmax formulation presented there, and also presented in other inverse MARL works. However, I reiterate that it is incredibly difficult to assess the paper's novelty due to the writing.

- I also do not understand what the empirical results tell us. In your setting, both the robot (i.e. learner) and the human (i.e. expert) actually can observe their rewards when a joint action is executed. Then, for the robot, there is no reason to do inverse RL. Standard MARL is enough.

- The point above makes me think that there is a crucial misunderstanding here. Inverse RL is not applied to settings where simply the reward function is not _known_ by the agent. As long as the rewards can be observed by the agent, standard RL (i.e. model-free) is enough. We use IRL for settings where the agent cannot even observe rewards, as in, once robot takes an action it does not receive any reward feedback, thus even the feedback itself must be learned. This is not the case in your work.

### Questions
Please feel free to address any points mentioned under the Weaknesses.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a stochastic bilevel method to tackle the problem of multi agent inverse reinforcement learning.
The authors manage to prove some convergence guarantees and conclude the paper with some experiments in simple settings.

### Strengths
Multi Agent IRL is an important open problem.

The author ran some experiments motivating their method.

### Weaknesses
 The setting does not seem the standard inverse reinforcement learning setting where the learner does not access any reward.
In addition, the fact that the reward $r^{ld}$ can be evaluated along the learned trajectory makes not true the sttaement that the single agent case can be recovered if the learner does not affect the transitions and the reward of the expert. Therefore, overall I do not think that this method can be labeled as inverse reinforcement learning.

The theory is rather week in my view. In particular, how does a guarantee on the gradient norm transfer on the guarantees of the learner policy. It would be interesting to have a result saying that the learner policy converges to the best response to the expert but this is not shown in the paper.

In addition, in RL it is important to quantify not only the convergence rate but also the dependence on the number of states and actions. This is not evident in the theorem statement provided by this work.

Finally, the experiments are in my opinion carried out in only toy environment.

### Questions
How does the result in Theorem 2 translate in terms of guarantees for the suboptimality of the recovered policy measure against the expert policy with respect to the true reward function ?

How does the bound in Theorem 2 depend on the number of states/actions in tabular MDPs or on the complexity of the reward class in the function approximation case ?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper considers inverse reinforcement learning (IRL) under the multi-agent setting, which aims to extend beyond the fully cooperative and fully competitive rewards in prior work. The authors propose a bi-level optimization problem and an IRL algorithm. Numerical results confirm the effectiveness of the proposed methodology.

### Strengths
1. The paper has a clear motivation and provides examples to show the commonality of the proposed setting.
2. The proposed algorithm attains comparable performance to the baseline without assessing demonstrations generated by ground truth rewards.

### Weaknesses
As multiple NEs may exist for a general-sum game, the proposed algorithm requires the expert and the learner to agree on the same NE (lines 4 and 10). This is a significant limitation because the algorithm does not explicitly address how this agreement is achieved or guaranteed. The assumption that both expert and learner converge to the same NE is not trivial, especially in complex multi-agent scenarios where multiple NEs with varying characteristics might exist. Furthermore, the paper lacks a discussion on the potential impact of converging to different NEs, which could lead to suboptimal learning or even divergence. The practical implications of this assumption on the algorithm's performance in real-world scenarios are not clearly addressed.

### Questions
1. Is it possible to also learn the expert's reward $r_e$ using $D_{r_{ld}^{\theta_l},r_e}$?
2. Does Theorem 2 guarantee the convergence to an NE?

### Soundness
3

### Presentation
2

### Contribution
3
