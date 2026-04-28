# A Competition Winning Deep Reinforcement Learning Agent in microRTS

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 5, 3

## Abstract
Scripted agents have predominantly won the five
previous iterations of the IEEE microRTS ($\mu$RTS) competitions hosted at CIG and
CoG. Despite Deep Reinforcement Learning (DRL) algorithms making significant strides
in real-time strategy (RTS) games, their adoption in this primarily academic
competition has been limited  due to the considerable training resources required and the complexity
inherent in creating and debugging such agents. \agentName\ is the first DRL agent
to win the IEEE microRTS competition. In a benchmark without performance
constraints, \agentName\ regularly defeated the two
prior competition winners. This first competition-winning DRL submission can be
a benchmark for future microRTS competitions and a starting point for future DRL
research. Iteratively fine-tuning the base policy and transfer learning to specific maps were 
critical to \agentName's winning performance. These strategies can be used to
economically train future DRL agents. Further work in Imitation Learning using Behavior Cloning and
fine-tuning these models with DRL has proven promising as an efficient way
to bootstrap models with demonstrated, competitive behaviors.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents AnonymizedAI, a Deep Reinforcement Learning (DRL) agent, which is the first of its kind to secure a win in the IEEE microRTS competition. AnonymizedAI exploits a combination of carefully fine-tuned base policies and map-specific transfer learning to outperform previous competition winners. The paper describes the implementation of AnonymizedAI, including its 7 trained neural networks and the significant effort required to train and debug the agent, emphasizing the role of iterative fine-tuning and transfer learning in the agent's success. Furthermore, the authors discuss potential improvements in inference time and explore behavior cloning and its potential to bootstrap models with novel behaviors.

### Strengths
1. The major novelty of this work is the application of iterative fine-tuning and transfer learning to a DRL agent in the microRTS competition. The victory of AnonymizedAI in the competition demonstrates the effectiveness of the DRL approach in complex strategy games.

2. The paper is well-structured and clear in its explanations, making the complex mechanisms behind AnonymizedAI accessible to readers.

### Weaknesses
1. Although the developed agent provides an innovative solution in the realm of the µRTS competition, the novelty of the techniques employed—transfer learning and iterative fine-tuning—within the broader context of DRL is somewhat limited as these techniques are already widely adopted.
2. The authors didn't delve into an analysis of diverse self-play strategies that could potentially improve the agent's performance. Considerations for strategies beyond basic self-play, such as fictitious self-play[1] or more complex schemes[2], would have enriched this study.


### Questions
1. It would be interesting to know whether the authors plan to explore the inclusion of more advanced self-play strategies, and how they believe these could potentially impact AnonymizedAI's performance.

2. The authors have mentioned the possibility of using the imitation learning approach for bootstrapping models with novel behaviors. Could they provide more insights into potential novel behaviors they are considering and how these could improve the agent's performance?

3. I did not find a description of the hardware information for training the agents in the paper, such as the CPU model and number of cores, GPU model and number of cores, the size of training memory usage, etc. I wonder if the author could provide this information.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a DRL model named AnonymizedAI, which is the first DRL method to win the IEEE microRTS competition. It defeated two prior competition winners in the IEEE microRTS (μRTS) competitions hosted at CIG and CoG. Its success largely benefits from iteratively fine-tuning the base policy and transfer learning to specific maps, which can be an economic method for training low-cost and efficient DRL agents.

### Strengths
**Originality:**

This paper presents a novel DRL training paradigm, which fine-tunes the base policy and transfers the policy to new scenarios. The proposed method won the IEEE microRTS competitions.

**Quality:**

To demonstrate the priority of the proposed method, this paper conducted massive experiments and presents detailed implementation of the novel method. The experimental results in the microRTS scenarios are convincing.

**Clarity:**

Overall, this paper is easy to follow. This article dedicates a considerable amount of text to elaborating on various technical details.

**Significance:**

This paper investigates an important research problem, i.e., training RTS AI efficiently with DRL. The proposed training method brings insights to the DRL community

### Weaknesses
Despite the fact that this paper presents a paper with convincing experimental results, I list some weaknesses:

1. This paper covers a considerable amount of text on technical details, such as policy networks and speeding up inference. However, it is hard to gain insights for training DRL agents on other complex scenarios, such as Mahjong and Stratego. [See the questions below]
2. The proposed method is a combination of prior methods. Contribution on DRL algorithm is limited.
3. Discussions on some related works are missing, such as SCC [1], it achieves top human performance defeating GrandMaster players in test matches and top professional players in a live StarCraft II event with order of magnitude less computation.

### Questions
1. In Sec. 2.1, why self-play failed in UAS and GridNet?
2. Why did not you use supervised learning?
3. Why does AnonymizedAI load 7 different policy networks?
4. What is Squnet?
5. What is the key takeaway for readers who want to use this proposed pipeline to train DRL agents on other complex scenarios, such as Stratego, Mahjong, PUBG and Honour of Kings?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors describe their entry to the IEEE-CoG2023 microRTS competition, where their entry won, thus 
becoming the first deep RL agent to win the competition. This is a competition to produce the best agent on the microRTS environment. RTS environments are difficult for RL agents because of their complex game structure with varying unit types and strategies, large action space, long episodes and sparse rewards.

The authors apply a number of implementation tricks to improve on existing methods, including using a value function that predicts three different rewards that vary throughout training and training 7 different networks and selecting based on the map. They then train an agent using behaviour cloning and then fine-tune it with deep RL.

### Strengths
The paper has a few notable strengths:
- The technical details of their implementation are very clearly described. 
- Winning the IEEE MicroRTS competition while being the first deep RL agent to do so is clearly a notable achievement.

### Weaknesses
However, the paper has a few notable weaknesses. In particular, although an impressive feat of engineering, I gained little insight about which parts of their design were particularly important, how exploitable their method was, how to improve the performance on larger maps and the required deeper strategy and other important research questions surrounding designing a good RTS agent. The submission could be significantly improved by focussing more on understanding why and how the system itself works. For example, the paper could include ablations of the different design decisions, or attempt to train a deep RL agent on the largest map. Instead the paper is mostly a grab-bag of previously-known techniques that combine to produce a very good agent.

### Questions
- You mention that scaling the behaviour cloning loss by the number of units that could take an action was critical to get it to train. Have you investigated why this is?

### Soundness
4 excellent

### Presentation
3 good

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
This paper presents AnonymizedAI, the first Deep Reinforcement Learning (DRL) agent to win the IEEE microRTS competition. AnonymizedAI's training process involved transfer learning to specific maps, which was critical to its winning performance. The paper also discusses the challenges of debugging and fine-tuning a DRL implementation, as well as the potential benefits of combining Imitation Learning and DRL. The contributions of this paper are:
1. Introducing AnonymizedAI, the first DRL agent to win the IEEE microRTS competition.
2. Demonstrating the importance of transfer learning to specific maps in achieving competitive performance.
3. Providing insights into the challenges and potential benefits of using DRL in real-time strategy games.

### Strengths
Quality: The paper provides detailed information on AnonymizedAI's architecture, training process, and performance, as well as insights into the challenges and potential benefits of using DRL in real-time strategy games.
Clarity: The paper is well-organized and clearly written, with sections on Introduction, Related Work, Methodology, Results, and Conclusion.

### Weaknesses
the contribution lacks novelty, the network architecture mainly references existing algorithm networks. At the same time, a method that can well solve the performance under multiple different maps is not proposed.

### Questions
Q1: how to ensure the high performance of the model in the new hidden map or an untrained map?
Q2: the masking significantly reduces the action space per turn and makes training more efficient, and how to determine and obtain the action needs to be masked?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
