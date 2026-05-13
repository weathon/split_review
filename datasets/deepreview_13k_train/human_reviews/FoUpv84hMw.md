# Federated $Q$-Learning with Reference-Advantage Decomposition: Almost Optimal Regret and Logarithmic Communication Cost

- Decision: Accept
- Scores: 8, 6, 8, 3, 6, 6

## Abstract
In this paper, we consider model-free federated reinforcement learning for tabular episodic Markov decision processes. Under the coordination of a central server, multiple agents collaboratively explore the environment and learn an optimal policy without sharing their raw data. Despite recent advances in federated Q-learning algorithms achieving near-linear regret speedup with low communication cost, existing algorithms only attain suboptimal regrets compared to the information bound. We propose a novel model-free federated Q-learning algorithm, termed FedQ-Advantage. Our algorithm leverages reference-advantage decomposition for variance reduction and operates under two distinct mechanisms: synchronization between the agents and the server, and policy update, both triggered by events. We prove that our algorithm not only requires a lower logarithmic communication cost but also achieves an almost optimal regret, reaching the information bound up to a logarithmic factor and near-linear regret speedup compared to its single-agent counterpart when the time horizon is sufficiently large.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper addresses the problem of federated reinforcement learning (RL) in a model-free, tabular episodic Markov Decision Process setting.  The FedQ-Advantage algorithm  proposed allows multiple agents to collaboratively learn an optimal policy through a central server without sharing raw data. Variance reduction is achieved through a reference adaptive decomposition. Novel contributions include event triggered communication and policy switching. The result is an an algorithm with almost optimal cost and communication that scales logarithmically with $T$ and a constant that scales better than previous algorithms reported in the literature.

### Strengths
The paper seems technically sound, I only skimmed most of the material in the appendix but the structure of the proofs and flow makes sense. I believe the paper will be of interest to the ICLR community. I believe the combination of the reduced communication burden and the near optimal regret together make this a significant result.

### Weaknesses
The main weakness of the paper is that it is extremely notationally heavy and very little intuition is provided in any of the steps - a representative example of this is the section "Updates of estimated value functions and policies". It's 90% equation. I appreciate that it is difficult to keep this under control, but I believe this needs to be improved in order for it to have any value. The lack of narrative makes it difficult to understand the motivation behind specific design choices, such as the particular form of the reference-advantage decomposition or the event-triggered communication mechanism. The paper dives directly into mathematical formalisms without first establishing a clear conceptual framework, making it hard to grasp the significance of the proposed approach. Furthermore, the connection between the theoretical results and practical implications is not well-articulated, leaving the reader wondering about the real-world applicability of the algorithm.

### Questions
Can the authors find a way to describe their work and provide some intuition behind the various steps. While I believe the validity of the results, I don't understand where the insights and intuition come from.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces FedQ-Advantage, a federated Q-learning algorithm for tabular episodic Markov Decision Processes. The algorithm utilizes reference-advantage decomposition to reduce variance and incorporates innovations like event-triggered communication, policy switching, and heterogeneous communication conditions. The paper proves that FedQ-Advantage achieves near-optimal regret with logarithmic communication cost.

### Strengths
1. The paper presents a well-structured and coherent methodology, detailing the innovations introduced in FedQ-Advantage, such as reference-advantage decomposition and communication mechanisms.
   
2. The proof of the algorithm’s near-optimal regret and logarithmic communication cost is rigorous and well-supported. The mathematical treatment is thorough, providing strong theoretical guarantees for the algorithm’s performance.

3. The algorithm's design, especially the heterogeneous communication triggering conditions and forced synchronization, shows creativity in addressing the challenges of federated learning.

### Weaknesses
1. The paper assumes a specific structure for communication conditions (e.g., event-triggered communication), which may not be universally applicable. The impact of these assumptions on algorithm performance in heterogeneous environments could be better analyzed. Specifically, the paper does not sufficiently explore how the event-triggered communication strategy interacts with varying agent learning speeds, potentially leading to inefficiencies if some agents consistently lag behind others in exploration. A more detailed analysis of the algorithm's robustness to diverse agent behaviors is needed.

2. The description of forced synchronization and its impact on performance, while novel, lacks a detailed explanation of how it interacts with other parts of the algorithm. A clearer explanation would help in understanding its necessity and effectiveness in the overall approach. For instance, it's unclear how forced synchronization affects the trade-off between exploration and exploitation, and how it might influence the convergence rate of the algorithm under different levels of agent heterogeneity. The paper should provide a more rigorous analysis of the conditions under which forced synchronization is beneficial or detrimental.

### Questions
1. How does the event-triggered communication strategy affect the algorithm’s performance when applied to environments with highly variable agent performance?
   
2. What are the trade-offs between forced synchronization and the other two mechanisms (communication triggering and policy switching)?

3. How would the FedQ-Advantage algorithm perform when applied to non-tabular environments or environments with larger state-action spaces, where Q-learning is typically more challenging?

4. In figure 1, what do $k_{12}$ and $k_{22}$ mean? Are these typos? Moreover, can you explain again about the condition and process when communication occurs?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a model-free federated reinforcement learning method called FedQ-Advantage. It focuses on  improving regret bounds and communication efficiency in multi-agent learning scenarios. This method leverages reference-advantage decomposition to reduce variance, designs an event-triggered communication method, and allows heterogeneous conditions. FedQ-Advantage achieves almost optimal regret, low communication cost, and near-linear regret speedup compared to the single-agent setting. It is especially efficient for distributed reinforcement learning tasks.

### Strengths
1. SOTA Results. The proposed model-free FedRL method achieves a logarithmic communication cost.
2. Novel techniques. The heterogeneous event-triggered communication in FedRL is new and effective.
3. The guarantees are given with solid theoretical proof.

### Weaknesses
1. The tabular setting is studied without function approximation. The action and state space are discrete and finite.
2. Literature Review. Is it possible to list federated value-based, and federated policy gradient-based methods separately and clearly? It would be better to have some pros and cons of federated Q-learning (value-based) methods compared to policy gradient-based methods.

### Questions
1. Comparison with model-based approaches. How does FedQ-Advantage compare to model-based FedRL methods in terms of convergence speed and communication complexity, given that model-based methods often have lower complexity?
2. Is there a trade-off between regret and communication complexity?

### Soundness
3

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
This paper studies online federated Q-learning, which seeks to develop an optimal Q-function by utilizing collaborative exploration of multiple agents in a federated manner. The authors introduce a federated Q-learning algorithm that incorporates reference-advantage decomposition to reduce variance, which leads to the improved regret bound. Additionally, they propose event-triggered communication and policy switching, which save communication costs.

### Strengths
1. The paper incorporated the variance reduction technique to federated Q-learning and demonstrated improved sample efficiency through regret analysis.
2. They empirically demonstrated the performance of the proposed algorithm in a synthetic environment, comparing it with baseline algorithms.

### Weaknesses
1. Considering the existing literature on federated Q-learning [1,2,3], Q-learning with variance reduction (reference-advantage decomposition) [4,5], and Q-learning with unaligned stage design [5], the integration of these existing techniques into federated Q-learning seems incremental.
2. The communication cost provided in this paper (O(SAH^2) or O(MSAH^2)) does not seem particularly low or noteworthy, given that other federated Q-learning algorithms [2,3] have demonstrated that O(H) communication rounds are sufficient. 
3. The presentation of the paper seems to need further refinement. Due to excessive notation and the use of vaguely defined terms, the descriptions of the algorithm and the equations are somewhat confusing, making them difficult to follow.
4. In federated settings, privacy is very crucial; however, the algorithm seems to require the agents to send too many estimates to the server alongside value estimates, which could potentially expose too much information about the datasets.

### Questions
See weaknesses.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes the first model-free federated tabular RL algorithm that achieves almost optimal regret with logarithmic communication cost. The authors adopt a reference-advantage decomposition when updating the $Q$ function via UCB for variance reduction. In addition, several designs surrounding communication and synchronization ensure a lower communication cost. Numerical experiments also support the benefit of FedQ-Advantage.

### Strengths
* The authors effectively highlight the contributions, including technical novelty.
* FedQ-Advantage is the first design for an almost optimal federated model-free RL algorithm that enjoys a logarithmic communication cost in a federated tabular setting.
* Theoretical analysis is provided and it can match the performance of the state-of-the-art results in tabular RL.

### Weaknesses
 * The related work is not comprehensive. The authors mentioned *most existing model-free federated algorithms do not actively update the exploration policies for local agents and fail to provide low regret*, which is not precise. Please also consider including [1, 2, 3] for full comparison. Although they are more based on functional approximation instead of pure tabular setting, they definitely incorporate active exploration strategies in federated learning. Specifically, while the cited works [1, 2, 3] focus on function approximation, they also tackle the challenge of balancing exploration and communication in federated settings, which is a core aspect of this paper. The current related work section does not adequately address how the proposed approach compares to these methods in terms of exploration strategies and communication efficiency, even if the settings are different. 
* The writing can be improved, especially the algorithm design section. The description of the algorithm is difficult to follow, and the notation is not always clear. Specifically, the use of $k^t_h(s,a)$ to denote the index of the first round belonging to stage t is confusing, especially given that Figure 1 seems to indicate that $k_2^1$ belongs to stage 2. The relationship between the stage index 't' and the round indices $k_h^t$ and $k_h^{t+1}$ needs further clarification. The logic of how stage $t$ is composed of rounds $k_h^t, k_h^t +1, ..., k_h^{t+1}-1$ is not clearly explained, making it hard to understand the temporal structure of the algorithm. The presentation of the algorithm lacks clear explanations of the steps, making it difficult to grasp the overall flow and logic.



### Questions
* The setting requires more description. I am not sure if I misunderstood the algorithm design, but it seems that the notation and Figure 1 is not clear to me. Specifically, $k^t_h(s,a)$ is denoted as the index of the first round that belongs to stage t, so I thought "t" refers to the index of stage while the first row in Figure indicates $k_2^1$ belongs to stage 2. In addition, the second row in Figure 1 shows $k_{12}$ and $k_{22}$ also confuses me. Please also explain more about the logic of stage $t$ how it is composed of rounds $k_h^t, k_h^t +1, ..., k_h^{t+1}-1$.

* Can you mainly compare your threshold/ event-triggered communication strategy with [1, 2]? Again, I know that your work is in a tabular setting, but since I am not fully clear with Figure 1. A comparison can make your design more readable. 

* I was wondering how your method can be extended to function approximation out of a tabular setting with the curse of dimensionality, especially for those main components in your algorithm, such as separate event-triggered communication and policy switching, heterogeneous communication triggering conditions, optional forced synchronization, and reference-advantage decomposition. Any challenge or limitation for your designs to convert to linear functional approximation setting?

* In Figure 3, it shows that the empirical regret from Concurrent UCB-Advantage is larger than FedQ-Advantage while Concurrent UCB-Advantage has the same regret as FedQ-Advantage from a theoretical standpoint. Could you please elaborate more on where the gap comes from? I am also interested in the rounds of communication as the comparison for Figure 3 (FedQ-Advantage vs. Concurrent UCB-Advantage), which you can ignore UCB-A: $10^6$.

#### [1] Dubey, Abhimanyu, and Alex Pentland. "Provably efficient cooperative multi-agent reinforcement learning with function approximation." arXiv preprint arXiv:2103.04972 (2021).

#### [2] Min, Yifei, et al. "Cooperative multi-agent reinforcement learning: Asynchronous communication and linear function approximation." ICML, 2023

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents FedQ-Advantage, a novel model-free federated reinforcement learning (FRL) algorithm designed for tabular episodic Markov decision processes (MDPs). This algorithm addresses the challenges of achieving optimal learning performance with minimal communication costs in a distributed setting where multiple agents collaborate under the coordination of a central server.
The proposed FedQ-Advantage enhances existing federated Q-learning methods by introducing mechanisms for variance reduction through reference-advantage decomposition and active policy updates coordinated by the central server.
The algorithm employs event-triggered communication, aligning communication rounds with specific conditions while allowing unaligned updates across state-action-step tuples. This approach reduces communication overhead significantly.
The introduction of heterogeneous triggering conditions allows agents to optimize exploration early in the learning process, further enhancing efficiency by limiting unnecessary communication later on.
An optional forced synchronization mechanism improves robustness and reduces waiting times for agents, streamlining the overall learning process.
The paper demonstrates that FedQ-Advantage achieves an almost optimal regret that approaches the information theoretical bound, scaling logarithmically with the number of communication rounds, and provides near-linear regret speedup compared to single-agent algorithms.
The authors propose heterogeneous triggering conditions that decrease the synchronization frequency, ultimately improving communication costs.
Overall, the paper makes significant strides in federated reinforcement learning by successfully developing an algorithm that balances optimal learning performance with low communication costs. Statistical theory demonstrates that FedQ-Advantage is the first model-free federated RL algorithm to achieve both almost optimal regret and logarithmic communication efficiency. These contributions position this paper as a valuable contribution to the field.

### Strengths
This paper is theoretically solid and well structured. 

Novelty: This paper develops the first near-optimal model-free RL algorithm under the setting of a tabular MDP and a communication graph with a central server. 

Significance: The communication cost matches with the best policy switching cost in Q-learning. 

Quality: The paper has good quality. The theoretical results look solid. It is good to see the synthetic experimental results match the theory. .  

Overall, I think this is a good theoretical paper.

### Weaknesses
There is no major flaw in this paper. However, the following can be addressed.

1. The paper is not easy to read and can be improved. For examples:

a) At the end of page 5, the paper mentioned that the visitation number $y_{t+1}$ is similar to the exponential rate in related works due to the first case and ‘Equation 4’. However, equation 4 is in page 7 and thus it is very hard to really understand what it means when reading the sentence Page 5. To improve, I think the authors could (i) either not to add such kind of details in section 3.1. Just presenting some intuition would be enough, or (ii) provide a brief preview of the key idea from Equation 4 when it's first mentioned on page 5. These might help readers follow the logic more easily without having to jump ahead in the paper.

b) Page 7, Item 4 can be improved. It is very hard to read. I understand that it is inevitable for this paper to be notationally heavy. But in the main text one might still want to avoid in-line equations of such lengths. If indeed one wish to insert these in the main text, then I think an explanation after each chunk of equations is necessary. The explanation can be as short as one sentence like “the central server finds the tuples whose visitation number exceeds… ”.

2. The claimed technical novelty of “non-martingale concentration” is a bit misleading. If my understanding is correct, the paper is simply approximating a non-martingale sequence with a martingale. In order to achieve this, the algorithm is specifically designed with a heterogeneous trigger condition that forces communication with the server when the number of visitations exceeds a threshold. This will ensure the ‘distance’ between the non-martingale sequence and the implicit martingale sequence to be small enough. After that, the entire error bound is a standard martingale convergence argument. If my understanding is not wrong, then this seems to me a quite straightforward approach to handle concentration under an asynchronous communication setting. I wouldn't expect the paper to give a real non-martingale concentration inequality. After all, if the communication is truly arbitrary and random, then I imagine it is impossible to get any valid concentration result.
To resolve this issue, I would suggest not to call this a ‘non-martingale’ concentration to avoid misunderstanding from people doing literature search for real non-martingale concentration.

Overall, I do not detect major technical issues in this theoretical paper. The above issues should be easily fixable.

### Questions
Please see the **Weaknesses** section.

### Soundness
3

### Presentation
2

### Contribution
3
