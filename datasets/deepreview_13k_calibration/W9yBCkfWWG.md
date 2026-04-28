# Federated Coordination: Private and Distributed Strategy Alignment

- Decision: Reject
- Avg Score: 5.60
- Scores: 5, 6, 5, 6, 6

## Abstract
Coordination in multi-agent systems is critical for optimizing collective outcomes and is applicable in diverse fields such as drone swarms, emergency response, and more. Despite extensive research, the distributed coordination strategy alignment problem---where all agents follow the same strategy and execute the prescribed actions without a global coordinator---remains largely unexplored, posing challenges in scalability and privacy preservation. We introduce a new research problem termed ``federated coordination", which seeks to achieve decentralized strategy alignment across distributed agents while maintaining the privacy of strategy choices. To address this problem, we propose a framework that employs an energy-based model. It facilitates decentralized strategy alignment by associating agent states with coordination strategies through local minimum energy values. We address privacy concerns through a simple yet effective communication protocol that protects strategy selections from eavesdropping and information leakage. Our extensive experimental results validate these contributions, demonstrating scalability and reduced computational demands. This enhances the practicality of coordination systems in multi-agent settings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper addresses a new problem named “federated coordination”, where the goal is for distributed agents to align their strategies, while maintaining their privacy and decentralized computations/communication. The proposed methodology for tackling this problem relies on an energy-based optimization problem formulation. In particular, the core idea is to associate predefined strategies with predetermined local minima in this problem and arrive to random strategies alignments based on the random local minima this optimization will converge to. Privacy requirements are met through a simple communication protocol that can address three types of threats. The presented experiments results suggest that the proposed methodology is effective for the problem that is studied.

### Strengths
The strengths of this submission are listed as follows:

1. An interesting problem/methodology of associating predefined multi-agent strategies with prescribed local minima in an energy-based model minimization is presented.  

2. A distributed algorithm for solving this energy-based optimization problem is provided. 

3. Privacy requirements are considered by showing how the proposed algorithm can handle three different types of privacy threats. 

4. The experiments suggest that the proposed algorithm is indeed effective for addressing the problem introduced in this paper. In particular, its performance, scalability, computational efficiency and robustness to lost connections are validated.

### Weaknesses
The weaknesses of this submission are outlined as follows: 

1. Although this is an interesting problem to study, the authors should better justify its meaningfulness and importance. For example, a motivating application for multi-drone systems is provided in the beginning of Section 3, stating that “To optimize their performance, the drones must randomly switch between these strategies for each operation, ensuring unpredictability in their tactics”. The authors should provide references where arriving to completely random and environment/opponent independent - yet predefined - tactics is indeed useful. 

2. The claim in lines 191-192, i.e., “Given $\mathbf{W}$ and $\mathbf{b}$, the size of local minimum collection $L$ and the value of each $\mathbf{v}^l$ are uniquely determined” requires further clarification/justification. The problem presented in Eq. (1) is highly non-convex and as (correctly) explained in the first paragraph of Section 4.1, “determining all local minima of the corresponding energy-based model is very difficult, if not impossible”. As a result, these two parts of the paper appear to contradict each other. The authors should either better explain/rephrase their claim in lines 191-192 or provide a theoretical justification.  

3. The authors claim in Section 4.1 that their algorithm “ensures that all local minima are known”. To my best understanding, solving Eq. (4) will indeed give a pair ($\mathbf{W},\mathbf{b}$) that sets the prescribed local minima $\mathbf{v}^l$ as local minima of the optimization in Eq. (1). Nevertheless, how does this guarantee that there are no other local minima in this problem in addition to the prescribed ones? The presence of additional, unprescribed local minima could lead to unpredictable behavior and undermine the intended strategy alignment.

4. For the proposed approach to make sense, the authors assume that the system in Eq. (4) has a unique solution (see claim “This ensures that $\mathbf{W}$ and $\mathbf{b}$ are uniquely determined by the constraints”). Nevertheless, is there a guarantee that this system is solvable? If the constraints are more than the d.o.f., can’t it be the case that there is no solution for this system? My expectation is that this also has to do with the linear independence of the equations in system (4). The authors should discuss the conditions under which the system is guaranteed to have a solution, and how the algorithm handles cases where the system is over-constrained or inconsistent.

5. It is not clear why the authors opt to solve the least-squares minimization in Eq. (6) instead of directly solving the system in Eq. (4). Note that if the optimal value of the problem in Eq. (6) is other than $J^* = 0$, then (4) is not satisfied, and as a result the prescribed local minima $\mathbf{v}^l$ are not going to be actual local minima of the problem in Eq. (1). Now, whether the optimal cost can be 0 or not is directly related to whether system (4) is solvable – see previous point. As a result, the motivation for employing the minimization presented in Eq. (6) is unclear. The authors should clarify why a least-squares approach is preferred, especially given that it does not guarantee the exact satisfaction of the constraints in Eq. (4).

6. At the end of Section 4.1, an algorithm for setting $L$ and $M$ is motivated and then fully described in the Appendix. The motivation for this algorithm appears to be that “setting $L$ and $M$ can result in an unsolvable Eq. (6)”. However, it is unclear how this algorithm indeed guarantees the solvability of the system. To my best understanding, the algorithm presented in appendix A.3 computes the optimal *user-defined number of local minima* $L$ and state size $M$, under the constraints in lines 781-783 and the cost that $M$ and $L$ should be as small as possible. Nevertheless, this approach does not take into account important aspects such as the fact that i) the number of local minima is actually related to the form of $\mathbf{W}, \mathbf{b}$ - which are going to emerge later after solving Eq. (4) and ii) the linear independency of the resulting equations in Eq. (4) is a major factor of whether the system is solvable. The authors should explain how the algorithm ensures that the resulting system of equations is solvable and that the chosen $L$ and $M$ are appropriate for the problem.

7. Given the importance of arriving to a (prescribed) local minimum using the distributed algorithm presented in Section 4.2, it is crucial to provide a guarantee that the proposed algorithm indeed converges to such a point. If this is not the case, then converging to a point other than the prescribed minima could be dangerous – especially for applications such as the coordination of multi-drone teams which is the motivation for this paper. Despite its expected importance, such a theoretical guarantee is not provided in this submission. The authors should provide a convergence analysis for their distributed algorithm, demonstrating that it will reliably converge to one of the prescribed local minima.

8. This paper's motivation is to achieve randomness on selecting between the predefined strategies. Nevertheless, whether this is in fact achieved is not clearly explored either theoretically or empirically.  

    a. From a theory perspective, it would be interesting if the authors can establish a guarantee on this “randomness”. My expectation is that this would depend on the initializations, the underlying local optimizers and of course $\mathbf{W}, \mathbf{b}$. For example, assuming the initializations are coming from uniform distributions, can any conclusion be drawn on perhaps some bounds on the probabilities of each strategy to emerge?

    b. If such a theoretical result is too mathematically demanding to prove, then the authors should at least provide an empirical validation of their claim. An easy way to verify this could be testing whether "scanning" the space of initial conditions for $\mathbf{u}$ provides solutions that do not disproportionately favor the selection of specific strategies over others, or that do not make specific strategies to never appear.

### Questions
The authors are encouraged to address the following questions: 

1. Pointing to weakness (1), can the authors better justify why this is a meaningful problem to address by providing specific references, for example on the motivation application, i.e., multi-drone systems, where their problem setup would be directly applicable? 

2. Pointing to weakness (2), can the authors provide a clarification on the point made in lines 191-192 and especially what they mean with all local minima being “uniquely determined”?  

3. Can the authors address the concern raised in weakness (3)? Is there a guarantee that the pair $(\mathbf{W}, \mathbf{b})$ we get from solving Eq. (4) will not lead to an optimization problem in Eq. (1) that has extra local minima in addition to the prescribed ones $\mathbf{v}^l$? 

4. Pointing to weakness (4), why is it guaranteed that the system in Eq. (4) is solvable? How can it be avoided that this system might have no solution? Shouldn’t this also be related to the linear independence of these equations? 

5. Pointing to weakness (5), can the authors elaborate on opting to solve the minimization in Eq. (6) instead of the system in Eq. (4)? If the optimal value of $J$ in Eq. (6) is other than 0 wouldn’t this mean that  system (4) is not satisfied and as a result the prescribed local minima are not actual local minima?  

6. Can the authors address the comments raised in weakness (6), regarding whether the algorithm in appendix A.3 actually guarantees the solvability of the system? 

7. Pointing to weakness (7), can it be proven that the algorithm proposed in Section 4.2 is guaranteed to converge to one of the prescribed local minima?  

8. Pointing to weakness (8), would it be possible that the authors elaborate on whether this desired “randomness” of strategy selection is indeed achieved. If providing a theoretical result that guarantees that is too mathematically tedious, would it be possible that it is at least shown empirically in the experiments section? 

9. In the beginning of Section 5, it is mentioned that the Adam optimizer is used for solving the optimization in Eq. (6) as well as the local optimizations of the agents using the gradients in Eq. (8). 

    a. Regarding using Adam to optimize Eq. (6), why is there a need to employ stochastic optimization to solve this problem? How is stochasticity incorporated here? Does it refer to a notion of evaluating at random subsamples (minibatches) of the “data” provided in Eq. (5)? The authors should elaborate on that and why Adam is preferred over standard or accelerated (non-stochastic) gradient descent, especially since this is also a convex minimization. 

     b. It would be useful if the authors could also provide details on how Eq. (8) is used with Adam as the local optimizer of each node and whether again stochasticity is incorporated through evaluating at random subsamples. 

10. In Section 5.2, to my best understanding, the authors refer with number of steps $Z$ to the rounds of the distributed optimization in Algorithm 1? Nevertheless, the amount of performed local Adam iterations is not stated. Isn’t the number of local Adam iterations affecting the number of rounds/steps $Z$ needed to achieve convergence? 

11. Similarly, in the computational efficiency analysis in Section 5.3, how many local Adam iterations are performed per step?

### Soundness
3

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
This paper proposes a new problem formulation called "federated coordination" which is geared towards decentralized strategy alignment with privacy preservation in multi-agent systems. Strategy alignment among agents is posed as an optimization problem using energy based models (EBMs), where an undirected graph is used to represent the interaction among neighboring or communicating agents. Different strategies correspond to different local minima for the EBM and the communication protocol among the agents is designed to be privacy-preserving against eavesdropping and information leakage without depending on more computationally demanding cryptography techniques. In an adversarial game setting between strategic agents, this paper proposes an algorithm for distributed strategy alignment against an adversary and demonstrates the scalability of the algorithm with different team sizes, different graph connectivity and robustness to communication loss.

### Strengths
1. The problem setting proposed in this paper is novel and interesting with possible applications to multi-agent systems in robotics, security games, etc. 

2. The paper is generally well-written. 
- The authors have pointed out the differences in their proposed problem setting compared to prior work in multi-agent reinforcement learning, game theory and differential privacy. 
- The two parts of the proposed algorithm: strategy alignment and privacy preservation against adversarial opponents, is clearly explained with discussion of the implications of the design choices under different settings (eg. in sec 4.3).

3.  Framing strategy alignment as equivalent to finding the local minima in an EBM for a particular inter-agent interaction layout is a principled and flexible approach. The iterative communication based gradient computation to minimize the agent's energy function naturally leads to a decentralized alignment procedure without a central coordinating agent.

### Weaknesses
While I appreciate the experiments outlined in support of the proposed problem formulation and the algorithm, the authors do not sufficiently highlight the potential weaknesses of the proposed approach and the scope for improvement. 
1. The proposed algorithm requires a pre-determined mapping between an agent's energy at a possible local minima to the corresponding action as part of the joint strategy. This reduces the difficulty of the setup by only focusing on achieving the local minimum starting from a random initialization of the agent's energy. For the algorithm to be actually practical, perhaps the mapping should be dynamic and learned from inter-agent interaction. Specifically, the current approach assumes a direct correspondence between a local minimum and a pre-defined action, which bypasses the challenge of learning optimal actions within the defined energy landscape. The algorithm does not address how these minima are associated with effective strategies in the first place, which is a critical step in real-world applications. The current setup simplifies the problem by assuming that reaching a local minimum is sufficient for achieving a desired outcome, neglecting the need for agents to learn which minima lead to beneficial joint strategies.
2. In this paper, the authors assume a pre-defined set of strategies and alignment means each agent looking up from the dictionary exactly which strategy they are meant to follow, which is different from the multi-agent reinforcement learning setting where the focus is primarily on learning a joint strategy for the team. By jointly optimizing both the energy landscape and learning high-reward strategies for the team, it might improve robustness against strategic adversary and unreliable communication. The current approach treats strategy selection as a lookup problem rather than a learning problem. This is a significant departure from multi-agent reinforcement learning where agents must learn to coordinate and adapt their strategies through interaction with the environment and other agents. The paper does not address how the pre-defined strategies are obtained or how they might be adapted to changing conditions or adversarial behavior. This limitation restricts the applicability of the proposed method in dynamic and uncertain environments.
3.  Instead of binary values for the local minima in the energy landscape, allowing continuous values would make the experimental setup more practical and flexible. The experiments also do not follow an adversarial team game setting which was used to motivate the federated coordination framework. The use of binary values for local minima restricts the expressiveness of the energy landscape. Continuous values could allow for a more nuanced representation of agent states and strategies. Furthermore, the experiments do not fully explore the adversarial team game setting, which was a key motivation for the framework. The experiments focus on demonstrating alignment but do not fully evaluate the system's performance against strategic adversaries, which limits the practical relevance of the results.

### Questions
1. Can you explain what is meant in line 527-528, especially what does inability to reach alignment mean in terms of outcome from an adversarial team game?

2.  How was $\rho(\cdot)$ selected?

3. Please add a notation table to clearly define all the variables used in the paper.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Authors present an approach to ensure multi-agent decentralized coordination using only local (neighbors) information and preventing information leakage, based on defining a joint strategy energy equation of which any desired coordination strategy is a local minimum. An algorithm for designing appropriate local minima is presented, and the effectiveness is demonstrated in coordination experiments.

### Strengths
- The solution of achieving decentralized coordination through a common potential function and carefully designed local minima is interesting, and relatively novel to the best of my knowledge.
- The paper is very clear and ideas are well presented.

### Weaknesses
 - My main concern is that the paper may fall slightly on the edge of suitable topics for ICLR. While multi-agent learning is clearly relevant, in this case the work feels more suitable for a multi-agent or robotics venue, where much of the current literature on multi-agent coordination is presented. The core contribution seems to be in the design of the potential function and local minima, which is more aligned with control theory and distributed systems than machine learning.
- Although I believe the method is novel, there are many existing works on decentralized coordination for multi-agent systems, as well as decentralized consensus control for distributed systems. Additionally I do not see such a clear distinction between decentralized coordination and federated coordination as the authors seem to argue for. The paper lacks a detailed discussion on how the proposed method differs from existing decentralized coordination algorithms, particularly in terms of the underlying assumptions, guarantees, and limitations. A more thorough positioning of the paper with respect to existing literature would help. This affects the relevance and contribution. The paper needs to clarify the specific advantages of the proposed approach over existing methods, especially in terms of scalability, robustness to noise, and convergence properties. The current discussion is too high-level and does not provide enough technical detail to justify the claims of novelty and superiority.

### Questions
- Would be interesting to see how this method applies to dynamic games or more general multi agent planning problems, both theoretically and experimentally.

I do not have any other major questions. I believe the paper is good and the ideas are interesting. My assessment scores are entirely based on a combination of contribution weight and appropriateness of the venue.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed a new problem - federated coordination, where decentralized agents such as drones choose their strategies to minimize energy values. Each agent only needs to gather information from their immediate neighbors, which contributes to the privacy protection and efficiency of the coordination. Besides, the scenario where cooperative agents face an opponent is modeled by a one-shot adversarial team game, which is a zero-sum game. Specifically, strategies are stored first before the coordination. In the proposed algorithm, agents will update their energy values based on the neighbor's information until reaching the minimum by gradient descent. Furthermore, they developed an encryption-free yet privacy-preserving communication protocol, to further maintain the confidentiality of agents' strategies. Last, experiments were conducted to show the validation and efficiency of the methods and algorithms.

### Strengths
1. The problem setting is novel, which addresses both privacy and coordination without a centralized agent. 
2. The algorithm is computationally efficient as it converges at sub-linear speed. 
3. The example of drones is good for illustration purposes.
4. The figures for the experiment results are great for visualizing the outcomes of this work.

### Weaknesses
As mentioned in this work, "with random W and b, determining all local minima of the corresponding energy-based model is very difficult". Therefore, the work uses a preset collection of local minima and then determines the value of W and b. However, these local minima may not be readily accessible in practice, which could limit the approach's effectiveness. Specifically, the method relies on a pre-defined set of local minima, which are then used to derive the parameters W and b of the energy function. This approach raises concerns about the generalizability of the method, as the selection of these minima is not clearly defined and may not be applicable to different scenarios or environments. The paper does not provide a clear methodology for how these local minima are chosen or how their selection affects the performance of the algorithm. This lack of clarity makes it difficult to assess the practical applicability of the proposed method, especially in real-world scenarios where the energy landscape may be complex and unknown.

### Questions
In reality such as the drones, how could you decide or find the preset collection of local minima?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper addresses the problem of coordination of agents without a central coordinator, addressing specifically the issues of scalability and privacy. It proposes a framework that uses energy as the base to accomplish federated coordination.  The basic idea is that each agent needs to minimize its energy use.  Each agent needs to know the energy state of its neighbors to be able to compute the gradient of its own energy.  Communication is limited to communication with neighbors., which is needed to compute the energy gradient.  For privacy, reasons, each agent knows only its own actions, not the collective strategy. To guarantee privacy, the paper considers the ability of the other agents to (1) predict the coordination strategy using past history, (2) eavesdrop om communication, and (3) access information stored by other agents. The approach proposed uses a non-stationary strategy distribution which is hard to predict, a privacy-preserving communication protocol that guarantees the confidentiality of data of agents not directly connected to compromised agents, so they stay protected. The experimental results include experiments to measure the effectiveness of the method, scalability, computational efficiency, and robustness against lost connections.

### Strengths
The approach proposed is a novel way of dealing with the important problem of distributed decision making with guarantees on privacy and scalability.  

Since the strategy distribution depends on the distribution of the initial energy states and the optimizer, each agent can make its strategy distribution non stationary so the opponents cannot make accurate predictions.  

The set of experiments included in the paper is extensive, and shows strong scalability, computational efficiency, and robustness against dropped connections.

### Weaknesses
The writing is clear but dense, so it is hard to follow the mathematical details.  For instance, the explanations for Tables 1, 2, 3, are not clear.  The explanation says "From the third row, we observe that the distributions of black and white grids are the same across agents for each obtained equilibrium (i.e., the converged energy states), which means the equilibrium is a preset local minimum." If I look at the table, for each number of agents there are three different equilibria. Are you saying that all the agents for that network have the same equilibria? The figures do not show that the equilibria shown are for all the agents.
Please provide a more detailed explanation of Tables 1, 2, and 3, perhaps with a step-by-step breakdown of how to interpret the data. Additionally, please clarify whether the equilibria shown are indeed for all agents in each network.

What happens if there are no neighbors within the communication range?  Please discuss the implications of this scenario on your framework's performance or explain how your method handles such edge cases

Since all the agents share the same random number generator, doesn't this provide a potential path for breaking privacy? Please discuss the security implications of using a shared random number generator and whether you have considered alternative approaches to address this potential issue. 

The paper says that opponents cannot infer the strategy from the messages exchanged, because noise is added to avoid cases where the opponent  has seen the converged energy states before. I am wondering if can comment on how robust this noise addition is to a tenacious set of opponents. Please provide more details on the noise addition process and discuss any theoretical or empirical guarantees you can offer regarding its robustness against persistent adversaries.

What is the time unit in Table 4? Please clarify the time unit used in Table 4 and explain how this unit relates to real-world performance

Is there a reason for Figure 3 to get up to 40 agents, while the other go up to 80 or 180?  How sharp is the decline in the success rate? Please explain the rationale behind the different agent numbers used in various experiments. Please also provide a more detailed analysis of the success rate decline, and, if possible, include quantitative measures of the decline rate or additional data points to better illustrate the trend.

### Questions
What happens if there are no neighbors within the communication range?  Please discuss the implications of this scenario on your framework's performance or explain how your method handles such edge cases

Since all the agents share the same random number generator, doesn't this provide a potential path for breaking privacy? Please discuss the security implications of using a shared random number generator and whether you have considered alternative approaches to address this potential issue. 

The paper says that opponents cannot infer the strategy from the messages exchanged, because noise is added to avoid cases where the opponent  has seen the converged energy states before. I am wondering if can comment on how robust this noise addition is to a tenacious set of opponents. Please provide more details on the noise addition process and discuss any theoretical or empirical guarantees you can offer regarding its robustness against persistent adversaries.

What is the time unit in Table 4? Please clarify the time unit used in Table 4 and explain how this unit relates to real-world performance

Is there a reason for Figure 3 to get up to 40 agents, while the other go up to 80 or 180?  How sharp is the decline in the success rate? Please explain the rationale behind the different agent numbers used in various experiments. Please also provide a more detailed analysis of the success rate decline, and, if possible, include quantitative measures of the decline rate or additional data points to better illustrate the trend.

### Soundness
3

### Presentation
3

### Contribution
3
