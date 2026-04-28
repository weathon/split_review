# Exponential Topology-enabled Scalable Communication in Multi-agent Reinforcement Learning

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 8, 5, 6

## Abstract
In cooperative multi-agent reinforcement learning (MARL), well-designed communication protocols can effectively facilitate consensus among agents, thereby enhancing task performance. Moreover, in large-scale multi-agent systems commonly found in real-world applications, effective communication plays an even more critical role due to the escalated challenge of partial observability compared to smaller-scale setups. In this work, we endeavor to develop a scalable communication protocol for MARL. Unlike previous methods that focus on selecting optimal pairwise communication links—a task that becomes increasingly complex as the number of agents grows—we adopt a global perspective on communication topology design. Specifically, we propose to utilize the exponential topology to enable rapid information dissemination among agents by leveraging its small-diameter and small-size properties. This approach leads to a scalable communication protocol, named ExpoComm. To fully unlock the potential of exponential graphs as communication topologies, we employ memory-based message processors and auxiliary tasks to ground messages, ensuring that they reflect global information and benefit decision-making. Extensive experiments on large-scale cooperative benchmarks, including MAgent and Infrastructure Management Planning, demonstrate the superior performance and robust zero-shot transferability of ExpoComm compared to existing communication strategies.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes to utilize the exponential topology to enable rapid information dissemination among agents, which leads to scalable communication protocol ExpoComm. A memory-based message processors are employed and auxiliary loss is introduced to ground message. Experiments are conducted to validate their algorithm.

### Strengths
- Extensive experiments
- Superior performance against other baselines

### Weaknesses
 - The presentation of section 3.3 is not ideal, e.g. line 323, can you elaborate more on the prediction function f? Specifically, what is the input and output space of this function, and what is the motivation behind choosing a two-layer MLP? line 354 to line 355, what is t'? Is it a fixed time step or a variable one, and how is it sampled or determined during training? The lack of clarity makes it difficult to understand the message grounding process.

- In figure 4(f), the test win rate of ExpoComm starts to drop from 4*1e6 steps, which is concerning. While some fluctuation is expected, a consistent drop at this stage of training suggests a potential issue with the learning dynamics or hyperparameter settings. It would be beneficial to investigate this behavior further and provide some analysis on why this might be happening.

- The claim that this algorithm should excel in large-scale multi-agent environments is not fully supported by the results in Figure 4. While the algorithm shows good performance, the performance gap between the proposed method and other baselines does not consistently increase with the number of agents. It is important to provide a more thorough analysis of the scalability of the proposed method and discuss the factors that might limit its performance in very large-scale settings.

### Questions
- In figure 4(f), why does the test win rate of ExpoComm start to drop from 4*1e6 step? 
- This algorithm should excel in large-scale multi-agent environment, so can we suppose the performance gap between the algorithm proposed and other baselines should increase when the number of agents increase? If so, why can't we see such trend in figure 4?

### Soundness
2

### Presentation
2

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
The paper introduces ExpoComm, a scalable communication protocol for multi-agent reinforcement learning that uses exponential graph topologies to efficiently manage information flow among numerous agents in large-scale environments. Exponential graphs offer a small-diameter structure enabling ExpoComm to have rapid and cost-effective communication across agents. The method overcomes the need to finding task specific pairwise communication. The authors utilize a memory based message network for processing messages over time and to allow agents to accumulate and utilize past information. In addition, auxiliary tasks are used to align messages with global information, either through direct access to the global state (when available) or through contrastive learning techniques. The method is evaluated on MAgent gridworld benchmarks and compared with baselines having varying communication protocols.  The one-peer verison of the exponential graph performed the best despite only requiring a linear scaling communication cost.

### Strengths
The use of exponential graphs as a communication topology in MARL is an innovative approach.  Combining memory-based message processing and auxiliary tasks to enhance message relevance is also a strong contribution. The authors have performed extensive experiments with multiple baselines. The zero-shot transferability demonstrates a level of generalization. The method’s scalability and efficiency in managing communication in large agent populations without sacrificing performance have implications for large-scale MARL applications. Overall, the manuscript is well-organized and clearly presents both the motivation and implementation details of the proposed approach.

### Weaknesses
The paper would benefit from a more explicit discussion of the limitations of ExpoComm. Specifically, scenarios where the proposed exponential topology may not be ideal---such as tasks requiring task-specific pairwise communication links or settings where agents are non-cooperative or adversarial---are not fully addressed. The paper does not delve into the potential for message saturation or interference as the number of agents and communication hops increases, which could impact performance. Furthermore, the auxiliary tasks, while beneficial, may not be universally applicable or effective across all types of MARL problems, and the paper lacks a detailed analysis of their sensitivity to different task characteristics. The evaluation could also be strengthened by including a more diverse set of environments, particularly those with more complex spatial structures or agent dynamics.

### Questions
The proposed exponential topology works well for cooperative tasks. However, could the authors clarify how this approach might be adapted for tasks where agents require specific pairwise connectivity? For instance, if a task necessitates more targeted information sharing between certain agents due to task-specific roles, would ExpoComm accommodate such requirements?

How would the proposed protocol perform in scenarios where some agents are adversarial or non-cooperative?

Could the authors provide more details about the experimental setups? Including environment visualizations or schematic diagrams would be extremely helpful for understanding the experimental conditions. Such visual aids could illustrate the setup, agent interactions, and communication patterns in more detail.

In Figures 4 and 6, the x-axis is labeled as "test return," although it appears to show plots related to training return. Could the authors clarify this discrepancy?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The work focuses on the improving communication in large scale multi-agent reinforcement learning. The authors propose using exponential topology as a communication pattern among agents. The authors show that this method can improve the multi-agent performance in a large scale environment using the MAgent and Infrastructure Management Planning environments.

### Strengths
- The author studies the problem of improving large scale MARL communication, which can be helpful for MARL research and deployment.
- The paper is well written and easy to follow. The toy example and figures presented is helpful for understanding.
- The proposed method seems to show improved performance for the AdversarialPursuit case.

### Weaknesses
 - It is unclear how the proposed exponential graph can be helpful for improving agent communication under target scenario. Providing some theoretically analysis or motivating example would be helpful. The toy example is helpful, but random global communication is not considered there.
- Beside the exponential graph, the contribution of this work seems limited. Highlighting and clarifying the contributions of this work would be helpful for better understanding.
- Evaluation seems incomplete. Comparing the proposed method to the traditional broadcast communication methods can help make the claim more persuasive.

### Questions
- How does the proposed method performs compared to traditional mulitcast type of multi-agent communication method such as CommNet, as it seems more global communication is beneficial for the target scenarios?
- How does the proposed exponential graph compared with random selection of communication peers? (keeping the number of communication peers the same)?
- What are the limitation of this method? Based on the results in Figure 4, the benefit of the method is more obvious for AdversarialPursuit than for Battle. It seems it's only learning after for the Battle environments. Is it learning faster for Battle because there is less communication peers for each node?

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
This work focuses on the problem of learning scalable communication in many-agent systems through multi-agent reinforcement learning. To tackle this problem, this work uses exponential graphs to model the communication topology, and memory-based message processors and message grounding for information representation. Through examples and baseline comparisons, the authors demonstrate that exponential graphs can balance the trade-off between dissemination speed and redundancy; thereby allowing agents to receive messages from other connected members in the graph without additional communication overhead.

### Strengths
The problem this paper seeks to address is an interesting and important issue in multi-agent reinforcement learning regarding scalable communication. The idea of using exponential graphs in this application is novel to me, and I appreciated the way that the authors helped the reader build intuition for the benefits ofgraph design in section 3.1; an exponential  I thought this was clear and very well-written. The experiments on the transferability of the method were very thorough, and I appreciated the comparisons for both K cases. The ablation studies served to reiterate the author's point and useful aspects of their architecture.

### Weaknesses
Overall, my concerns with this paper lie in the framing regarding communication overhead.
- The definition of communication overhead in this paper is rather ambiguous. It would probably be best to add a formalized definition, as communication overhead has very field-specific connotations beyond computer science. While addressed by the authors in the introduction, it is possible to reduce communication overhead by only communicating with a subset of peers. If ExpoComm does produce lower communication overhead, I think this paper could be strengthened significantly by adding additional metrics where the number of messages (or unique messages) ExpoComm has sent is directly compared against another method that only communicates with a subset of agents (eg DGN). From my understanding, Table 1 lacks these comparisons now. If ExpoComm does not result in lower numbers of messages passed between agents against comparable baselines (eg. MAGIC, DGN), then I would recommend clarifying the wording throughout the paper, to be in line with your definition of communication overhead.

### Questions
-  Do you have any theories why CommFormer performs so terribly in the Adversarial Pursuit 25 agent case? It performs similarly to ExpoComm in the Battle Environment 20 agent case; I would be interested to hear your theories on why it doesn’t generalize well or performs similarly to ExpoComm in that one case. 

- The performance of ER and ExpoComm are very smilar in the filled bar transferability cases (i.e. K=log2N). Do you have theories about why this is? 

- Did you experiment with more K values beyond log2N and 1? If so, what did you observe and why did you believe these two values in the paper would be representative examples?

- Does communication overhead in this paper refer to number of messages passed? Can you provide a definition in-text? Are there additional communciation savings that can be achieved by your method beyond its exponential graph structure? (i.e. savings due to pruning or shorter timesteps or less redundant agents communicated with to compared to other techniques)

### Soundness
2

### Presentation
3

### Contribution
3
