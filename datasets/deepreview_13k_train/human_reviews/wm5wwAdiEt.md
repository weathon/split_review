# Learning to Construct Implicit Communication Channel

- Decision: Accept
- Scores: 8, 3, 6, 8

## Abstract
Effective communication is an essential component in collaborative multi-agent systems. Situations where explicit messaging is not feasible have been common in human society throughout history, which motivate the study of implicit communication. Previous works on learning implicit communication mostly rely on theory of mind (ToM), where agents infer the mental states and intentions of others by interpreting their actions. However, ToM-based methods become less effective in making accurate inferences in complex tasks. In this work, we propose the Implicit Channel Protocol (ICP) framework, which allows agents to construct implicit communication channels similar to the explicit ones. ICP leverages a subset of actions, denoted as the scouting actions, and a mapping between information and these scouting actions that encodes and decodes the messages. We propose training algorithms for agents to message and act, including learning with a randomly initialized information map and with a delayed information map. The efficacy of ICP has been tested on the tasks of Guessing Number, Revealing Goals, and Hanabi, where ICP significantly outperforms baseline methods through more efficient information transmission.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents the **Implicit Channel Protocol (ICP)** framework, an approach for enabling implicit communication in collaborative multi-agent reinforcement learning (MARL) environments where explicit communication is unavailable or costly. ICP introduces a subset of actions termed "scouting actions" that allow agents to communicate indirectly by encoding and decoding messages through their choice of these actions. By leveraging these actions, ICP builds an implicit channel similar to explicit communication protocols. The framework is evaluated on tasks such as Guessing Number, Revealing Goals, and the Hanabi card game, where it demonstrates effective information transmission and improved performance over baseline methods.

### Strengths
The paper is well-structured and easy to follow. The algorithm is clearly-explained, with clear definitions of necessary notations. The experiments are well-designed and comprehensive, with sufficient implementation details.

### Weaknesses
1. The ICP framework requires pre-identified scouting actions that can serve as indirect communication channels. This dependency limits its applicability in environments where such actions are not readily available or are difficult to define. The paper does not discuss how to systematically identify or design these scouting actions, which is a critical limitation for practical implementation. For instance, in a complex robotic manipulation task, it might not be obvious what actions could serve as effective communication signals without significantly disrupting the primary task.

2. It can help the readers to better understand the method if the authors can include a diagram of the algorithm pipeline. The current description, while detailed, lacks a visual representation of the information flow and decision-making process within the ICP framework. A diagram would clarify how the agents select scouting actions, encode messages, and how the receiving agents decode these messages, making the overall process more intuitive.

### Questions
1. In experiments, for agents trained with VDN, is the action space the combination of “regular actions” and “scouting actions“?  
2. In figure 3b, why are those methods not trained to the same length?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a communication framework for a multi-agent reinforcement learning system. Efficient and targeted communication in the form of query-key pairs have been explored under previous works. Moreover, in order to address the challenges of a non-stationary environment, prior works have used Theory of Mind (ToM) methods to infer the intentions/states of the other agents in the environment to make more informed decisions. Developing models of other agents, add complexity to the training of multi-agent systems. This paper proposes an Implicit Communication Protocol, where each agents actions are supplemented with a *communication/scouting* action, that controls whether an agents sends a scouting action/query. Unlike the attention mechanism, where all agents receive 'N' messages from all 'N' agents, this paper proposes a common channel that aggregates all the information into one message vector. This paper additionally uses a gating mechanism similar to IC3Net, but with a Gumbel-Softmax relaxation that allows it to encode it as a binary classifier that functions as ATOC's (Jiang et al, 2018) "initiator" gating mechanism. 

The paper utilizes the non-differentiable communication aggregator mechanism RGMComm. Additionally, standard end-to-end differentiable communication networks can instead be used. A lookup table of the local observation of each agent with the respected broadcasted messages are then constructed for all agents to discretize the communication channel. Moreover, they use the hat-mapping technique where agents can infer their own targeted messages from the common message. The messages are then passed along with the hidden states of the agents to get the updated action.

### Strengths
The proposed method is interesting, particularly toward the foundational problem of efficient multi agent communication by generating a information table with respect to the observation and message. Additionally, research into reducing computational complexity for intention inference techniques of agents will be highly valuable to the large-scale multi-agent systems.

### Weaknesses
1. The paper does not discuss the impact of scalability or impact of heterogeneous agents to the proposed framework for multi agent systems, as you increase the number of agents to say up to 10, 20, 50 agents.

2. The paper does not compare results for common communication architectures such as CommNet, TarMAC, SARNet etc for their environments but only with value decomposition networks (VDN), that do not perform communication as part of their actions. 

3. The paper does not discuss limitations on the size of the action spaces or performance with respect to more dynamic environments such as predatory-prey, cooperative navigation.

I believe more comprehensive experimental results are needed for the proposed framework.

### Questions
The results for Hanabi are quite remarkable, however,  game rules indicate, the hints are only constrained towards revealing either the color or the number. Since ICP implicitly encodes the local observation of each agent (both for DIAL and RGMComm) into message vectors, I believe each agent observes in essence have access to the complete global state, which inherently breaks the rule of Hanabi, unless I am mistaken. I would like more clarification on this.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper looks into communication in collaborative multi-agent system under the formalism of multi-agent reinforcement learning. Specifically, the focus is on implicit communication for situations where explicit messaging is not possible. The paper proposes the Implicit Channel Protocol (ICP) framework. Unlike common implicit communication approaches like theory of mind which requires belief modeling of other agents, ICP uses a subset of actions (scouting actions) to broadcast in formation. It uses a mapping between the scouting actions and information that is learned either with a randomly initialized map or a delayed information map. The latter first learned with explicit communication before fixing the mapping. ICP is evaluated against baseline methods on 3 environments, including Guessing Number and Revealing Goals which are designed by the authors. Experimental results show ICP’s effectiveness in transmitting information more efficiently.

### Strengths
- The effectiveness of the method is evaluated against two newly designed benchmarks and results show ICP being superior to baselines

### Weaknesses
 - I still find the line between explicit and implicit communication a bit unclear here. Both of the newly designed environments have actions given specifically for communication and I find the definition of scouting actions to be quite narrow for implicit communication. Using the Revealing Goals as an example, agents can communicate with just directional movement actions if they could learn that certain direction corresponds to certain information. Hence, I don't see why implicit communication action has to be limited to those in which the state does not change.
- I sympathize with the issue with compute. But the difference between SAD (green dash line) and the proposed method is simply too close to support the conclusion.

### Questions
- Isn’t broadcasting an assumption rather than a benefit? This is not possible in many practical scenarios 
- What do you mean by ‘efficient embedding techniques’ in line 268?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work presents techniques for communicating through implicit channels (i.e. using environment actions instead of a dedicated communication channel). Specifically, by distinguishing between "regular" actions and "scouting" actions, agents can send messages through scouting actions. The first proposed technique uses the Gumbel-Softmax trick to have a fully differentiable communication pipeline through discrete actions, allowing a communication map between messages and scouting actions. The second proposed techniques adds a direct communication channel for pre-training and then uses a "hat mapping" strategy to encode and decode messages within scouting actions. These implicit communication techniques are effective at outperforming baselines in environments that require implicit communication, like Hanabi.

### Strengths
- The problem setting of constructing implicit communication channels is very important to multi-agent RL, and this paper takes important steps to tackling this challenge.
- The hat mapping strategy is a quite smart application of the classic logic problem to a broader space of communication challenges.
- The techniques and environments are easy to understand.

### Weaknesses
 - All of the environments studied in this work have the same quirk as Hanabi, namely that agents cannot view the information they need but they can view the information for all other agents and have to communicate that information to other agents. This work would be more convincing if the key communication challenge between settings were more unique.
- The task of learning an implicit communication channel in this paper does not seem too different from learning an explicit discrete communication channel, with the only major difference being that the "scouting" actions actually have some information prior whereas discrete channels are typically arbitrary. I would've liked to see how algorithms for explicit discrete communication channels compare to the proposed techniques in this paper as baselines. Furthermore, DIAL should be added as an explicit baseline instead of just comparing with VDN baselines. 
- Although two techniques are presented (random initial map and delayed map), the two techniques are only compared in the Hanabi game. Readers should be able to see the performance of both techniques across all environments due to the significant differences between the two.


Minor note:
- There are many grammatical errors throughout the paper, especially mixing up the use of singular and plural nouns and incorrect exclusions of definite articles ("the").

### Questions
- How does the delayed map approach perform in Guessing Number and Revealing Goals?
- Can the proposed technique be used in situations where there is no clear delineation between "scouting" and "regular" actions?

### Soundness
2

### Presentation
2

### Contribution
2
