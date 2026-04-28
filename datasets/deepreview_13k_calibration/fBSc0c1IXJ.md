# Remote Reinforcement Learning with Communication Constraints

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3, 3

## Abstract
We introduce the novel problem of remote reinforcement learning (RRL) with a communication constraint, in which the actor that takes the actions in the environment lacks direct access to the reward signal. Instead, the rewards are observed by a controller, which communicates with the agent through a communication-constrained channel. This can model a remote control scenario over a wireless channel, where the communication link from the controller to the agent has limited capacity due to power, bandwidth, or delay constraints. In the proposed solution, rather than transmitting the reward values to the agent over the rate-limited channel, the controller learns the optimal policy, and at each round, signals the action that the agent should take over the channel. However, instead of sending the precise action--which can be prohibitive when the action set is large--we use an importance sampling approach to reduce the communication load, which allows the agent to sample an action from the current policy. The actor, sampling from the desired policy at each turn, can also learn the optimal policy, albeit at a slower pace, using supervised learning. We exploit the learned policy at the actor to further reduce the communication load. Our solution, called Guided Remote Action Sampling Policy (GRASP), exhibits a significant reduction in communication requirements, achieving an average of 12-fold decrease in data transmission across all experiments, and 50-fold reduction for environments with continuous action spaces. We also show the applicability of GRASP beyond single-agent scenarios, including parallel and multi-agent environments.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper addresses the problem of communication constraints when the actor cannot access the reward signal in a timely or direct manner. To reduce communication load, the authors propose a solution that, instead of sending the actual action over the controller, employs an importance sampling method. This method samples from the desired policy to effectively learn the optimal policy.

### Strengths
This paper considers a common challenge in real-world applications: an agent may not receive prompt feedback when taking action.

### Weaknesses
1. The reward signals in real-world settings are generally less complex than the states or observations, making it potentially unnecessary to use a controller solely for receiving reward signals. Additionally, how does this approach differ from centralized training with decentralized execution? The proposed setup seems too limited in scope.
2. The controller resembles a central critic, and I don't see a significant difference between the actor-critic framework and the proposed approach. Specifically, the controller learns a policy, and then the actor learns to mimic this policy, which is essentially what happens in an actor-critic setup where the critic guides the actor's learning.
3. Using imitation learning to train actors that mimic the controller's policies is not novel, and the proposed method lacks theoretical guarantees, relying primarily on heuristic design. The paper does not provide any analysis of the convergence properties of the proposed method, or any bound on the performance of the learned policy.
4. There is no comparison with other imitation learning algorithms such as VIPER (Verifiable Reinforcement Learning via Policy Extraction, NeurIPS 2018) or DAGGER (A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning, AISTATS 2011).
5. The paper claims to address challenges in MARL, yet there are no MARL settings presented.

### Questions
See the weakness section.

### Soundness
2

### Presentation
2

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
This paper addresses the novel challenge of Remote Reinforcement Learning (RRL) with communication constraints. In RRL, an actor takes actions based on state observations, while a separate controller receives the reward signals, and the two components communicate through a limited-bandwidth channel. To reduce the communication load, the authors propose the Guided Remote Action Sampling Policy (GRASP), which leverages importance sampling to select actions based on the controller’s optimal policy. By approximating the policy distribution through behavioral cloning, GRASP significantly reduces data transmission requirements. Experiments demonstrate that GRASP achieves up to a 50-fold reduction in communication for continuous action environments and shows comparable performance across single-agent, multi-agent, and parallel-agent environments.

### Strengths
1. The paper introduces the novel concept of remote reinforcement learning under communication constraints, a setting not extensively explored in the literature.
2. The paper is well-organized, clearly explaining the problem setting, methodology, and experimental design.
3. By addressing remote control scenarios in reinforcement learning, GRASP has practical applications in domains where agents operate under limited communication channels.

### Weaknesses
1. The originality of the GRASP solution is somewhat limited, as it primarily combines existing techniques without introducing significant new methods. The core idea of using behavioral cloning to approximate the controller's policy and then employing importance sampling for action selection, while practically useful, does not represent a substantial theoretical advancement in the field of reinforcement learning. The novelty is primarily in the application of these techniques to the remote RL setting, rather than in the techniques themselves.

2. The comparison between the Action Source Coding (ASC) benchmark and GRASP may be unfair, as ASC lacks access to alternative action choices, whereas GRASP employs importance sampling to transmit diverse actions. Specifically, ASC transmits a single action, while GRASP samples multiple actions from the approximated policy and uses importance sampling to select one. This gives GRASP an inherent advantage in exploring the action space, which is not a fair comparison given the communication constraints are supposed to be the primary focus. The method of action selection should be consistent across benchmarks to isolate the impact of communication constraints.

3. In Section 4 (Experiments), the paper mentions a second benchmark that transmits rewards directly to the actor, but results for this benchmark are missing from the tables and figures, leaving the comparison incomplete. The absence of this data makes it difficult to fully evaluate the performance of GRASP against all reasonable baselines. The paper should include a comprehensive comparison with all mentioned benchmarks to ensure the validity of the results.

### Questions
1. Does importance sampling introduce high variance during training, and if so, to what extent does it impact performance?
2. Does importance sampling enhance training by introducing diverse behaviors? An ablation study quantifying this impact would be helpful.
3. What is the performance of the benchmark that transmits rewards directly to the actor, and how does it compare with GRASP?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces the novel problem of Remote Reinforcement Learning (RRL) with communication constraints, where an actor, responsible for taking actions in an environment, does not have direct access to the reward signal. Instead, a controller, which observes the reward, communicates with the actor through a constrained channel.
The authors propose a solution called Guided Remote Action Sampling Policy (GRASP), a method they claim significantly reduces communication requirements while enabling the actor to learn an optimal policy via supervised learning.

### Strengths
The problem is interesting. The related work appears to be comprehensive.

### Weaknesses
However, I find that some of the problem setup and algorithmic assumptions lack clarity and coherence, which raises foundational questions about the validity and practicality of the approach.

1. The authors assume a remote setting where the communication bandwidth is limited, yet the remote controller have access to the full state and reward signal of the environment. This setup is ambiguous: how does the controller access those info without communication? If the the controller can observe both state and reward, why it cannot access the actions as well? I suggest the authors provide a clearer justification for this selective access and an real-world example for this setup.
    
2. The authors assume the actor has limited computation resources, making it unable to perform RL. However, they still require the actor to perform supervised learning as shown in algorithm 2. Supervised learning can still impose non-trivial computational demands. This contradiction needs further explanation.
    
3. The authors assume that sending “a real number reward“ is too demanding for the communication channel (line 075), but the same channel can be used to communicate the actions. Since both actions and rewards can be continuous, it’s unclear how one can be feasible while the other is not.

### Questions
Apart from these foundational concerns, the paper lacks sufficient detail in the algorithmic description, the implementation, and the experiment setup. Here I list a few questions:

1. There are two copies of the actor policies being learned, one within controller learning while the one in actor learning. Are these supposed to be the same, and if so, how is consistency maintained?
    
2. The objective function mentioned $\pi_A$ and $\pi_C$, what do they correspond to in the algorithms?
    
3. What is channel simulation encoding and channel simulation decoding?
    
4. The author conducted experiments on MARL setting, but it’s unclear how GRASP was adapted for them.
    

The proposed problem is interesting, but the assumptions need more justification, and key details are missing. Addressing these issues would make the claims stronger and the paper clearer.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a new scenario in reinforcement learning, termed "remote reinforcement learning," where an actor does not have direct access to the reward signal, but a controller does. Within this scenario, the authors propose a sampling approach that allows the controller to send an action with minimal communication load.

### Strengths
- The paper introduces a new paradigm of RL that considers practical constraints.
- Given this paradigm, the authors propose a concrete algorithm to reduce communication load while maintaining performance similar to conventional RL algorithms.

### Weaknesses
The main weakness of this paper lies in the motivation and rationale behind the proposed scenario. Although the authors provide detailed explanations and motivations in the introduction, I am uncertain about the practicality of the scenario.

- The limitations associated with sending reward signals might also apply to sending action signals. For instance, regarding one limitation—limited communication---while the authors differentiate between communicating actions and rewards, I question whether this distinction is significant. Rewards can be quantized, and there is extensive research on learning from noisy rewards. Quantized rewards could suffice; even in DQN for Atari games, clipped reward values perform effectively. Moreover, delayed communication could pose a problem. Communicating rewards might be feasible since rewards are mainly used for training (RL can generally handle delayed rewards), whereas delayed or noisy actions may degrade performance. Additionally, in most reinforcement learning, policies are trained in simulation and later deployed. Reward signals are typically only necessary during the training phase, while action signals are required in both simulation and deployment. I offer these examples because the practicality of this method is a central claim of the paper.
- If the primary advantage of this approach is reducing communication load, the authors should compare GRASP to a model with quantized reward signals under equivalent communication loads to strengthen their motivation.
- The first paragraph of the introduction could be improved. It states, "evaluating the reward may require solving optimization problems..." and "the challenges of lacking or costly reward acquisition in RL." However, the motivation for this scenario is related to communication, not reward acquisition challenges, as the proposed method still requires a reward signal (for the controller).

### Questions
See weakness

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies remote reinforcement learning (RL) where the controller communicates with the actor through a communication constrained channel to help the actor to train a RL policy. To minimize the communication cost, the paper aims to minimize the KL-divergence between the policies of the controller and the actor. A variety of environments are used to evaluate the algorithm.

### Strengths
1. The problem remote RL is interesting and has practical values.
2, Information theory seems a promising tool to solve the problem.
3. The experiments are solid.

### Weaknesses
1. The introduction lacks of the state-of-the-art on remote RL and discussions on how this paper advances the state-of-the-art.
2. The paper presentation is informal. First, the paper does not provide the formal problem statement (minimizing the KL divergence) until Page 6. Second, lots of important details are missing in the pseudocode, e.g., channel simulation encoding, channel simulation decoding, online RL and supervised learning. These details are essential to understand how the algorithm solves the problem.
3. The key idea of the algorithm is remote sampling from information theory. However, its discussion is isolated from the algorithm. It is difficult to understand how remote sampling solves the problem of minimizing the KL divergence.
4. The experiment results (Tables 1, 2 and Figures 2, 3) do not include any classic RL algorithm, which can access the reward. The paper needs to demonstrate that the remote RL algorithm can provide comparable performance as state-of-the-art RL algorithms with lower communication overhead.

### Questions
Please refer to the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
3
