# Multi-Session Budget Optimization for Forward Auction-based Federated Learning

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 5, 3, 3

## Abstract
Auction-based Federated Learning (AFL) has emerged as an important research field in recent years. The prevailing strategies for FL model users (MUs) assume that the entire team of the required data owners (DOs) for an FL task must be assembled before training can commence. In practice, an MU can trigger the FL training process multiple times. DOs can thus be gradually recruited over multiple FL model training sessions. Existing bidding strategies for AFL MUs are not designed to handle such scenarios. 
Therefore, the problem of multi-session AFL remains open. 
To address this problem, we propose the \underline{Multi}-session \underline{B}udget \underline{O}ptimization \underline{S}trategy for forward \underline{A}uction-based \underline{F}ederated \underline{L}earning (\methodname{}). Based on hierarchical reinforcement learning, \methodname{} jointly optimizes inter-session budget pacing and intra-session bidding for AFL MUs, with the objective of maximizing the total utility.
Extensive experiments on six benchmark datasets show that it significantly outperforms seven state-of-the-art approaches. On average, \methodname{} achieves 12.28\% higher utility, 14.52\% more data acquired through auctions for a given budget, and 1.23\% higher test accuracy achieved by the resulting FL model compared to the best baseline.
To the best of our knowledge, it is the first budget optimization decision support method with budget pacing capability designed for MUs in multi-session forward auction-based federated learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Auction-based federated learning consists of three types of participant: 1) data owners, who are willing to share their potentially sensitive data if they are appropriately compensated; 2) data consumers, who need data in order to train their federated learning models; and 3) a trusted third-party “auctioneer” who orchestrates the auction between data owners and data consumers. In scenarios where data consumers compete for data from the same pool of data owners, the key challenge for data consumers is to develop an optimal bidding strategy that maximizes certain key performance indicators subject to a budget. Previous work on optimizing this objective assumes that there is a single auctioning session, but in practice data consumers might recruit data owners over multiple training session. This paper proposes a budget optimization strategy for multi-session auction-based federated learning. The budget optimization strategy is based on hierarchical reinforcement learning with two types of budget allocation agents to handle the budget allocation both during a session and between sessions.

### Strengths
* The empirical evaluation is thorough, includes a decent number of datasets and also demonstrates good performance compared to previous methods.
* Extending budget optimization strategies to the multi-session AFL setting seems like an interesting and practical problem.

### Weaknesses
* The paper is dense with technical jargon. (One easy improvement could be to use acronyms less frequently, e.g. limit it to a max of one acronym per sentence).
* It is hard to get a sense of the novelty of the proposed method and how much of a jump it is from previous work. I would have also liked to see a more thorough discussion on the techincal challenges in extending budget optimization strategies to the multi-session AFL setting.

### Questions
Looking at footnote 2: “maximizing the total utiltiy is equivalent to optimizing the performance of the global FL model obtained by the target DC.” What is the distinction between “utility” and “test accuracy” as metrics?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper presents MultiBOS-AFL, a strategy for budget optimization in forward auction-based federated learning (AFL). This work extends data owner recruitment from single session to multi-session AFL, optimizing budget pacing over time. This approach features an inter-session budget pacing agent (InterBPA) and an intra-session bidding agent (IntraBMA), which jointly allocate and bid over multiple auction sessions.

### Strengths
- The paper tries to look into a new multi-session AFL scenario, expanding budget optimization strategies to cover temporal dimensions.

- paper is well written and easy to follow

### Weaknesses
- Applicability to real-world scenarios: The paper’s experimental settings use controlled noise and IID versus non-IID setups, but do not test more realistic settings with fluctuating budgets or DO availability patterns. In the real world, the DO availability is unknown, how does the proposed method handle that?

- How realistic is the proposed scenario of a multi-session auction? More motivation of why this scenario is valid would be helpful.  

- In the evaluation section, this work is not compared to other existing HRL algorithms. It is important to compare to existing HRL algorithms and show its performance benefit.

### Questions
- Adaptability in Dynamic Environments: How would MultiBOS-AFL perform if DOs arrived dynamically rather than being preset in each session? Could the HRL agents adapt if the number of sessions varied unexpectedly?

- Computational Efficiency: What is the computational overhead associated with HRL training, especially as the number of sessions and DOs increase?

- Can the proposed method scale to a larger dataset such as imagenet? Is there any limitation?

- Can the proposed method generalize when the demand or supply changes over time? It would be helpful to provide some analysis.

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
4

### Summary
This paper introduces an RL-based approach for auctions in federated learning. The goal is to maximize the total "reputation" of data owners that are won by the data consumer (who aims to train a model via FL) across multiple training sessions under a budget constraint. To this end, the RL approach consists of two RL agents, inter-session budget pacing agent (InterBPA) and intra-session budget management agent (IntraBMA). These two agents learn to allocate the budget across different sessions, and to determine the bid price for each data owner under the session budget in each session. The two agents are trained with DQN techniques.

### Strengths
S1. A well-motivated problem is studied.

S2. The AFL scenario considered in this work is practical.

S3. The approach is presented in a clear way.

### Weaknesses
W1. Some settings and assumptions of the task need to be explained (see questions below).

W2. In a competitive environment for DO auctions, it is unclear why DCs will follow the same approach (e.g., the one proposed in this paper). Any analysis about the incentives or truthfulness?

### Questions
Q1. Some settings and assumptions of the task need to be explained. I understand that some settings of this paper follow previous works. But more background about these settings is needed in Section 3. Also, it does not mean that all the settings are reasonable. Some of them need to be motivated better: for example,
- It is unclear how (2) and (3) can be evaluated efficiently across the FL training process to derive the reputation $v^i_s$ of each DO in each session. If they cannot be evaluated exactly, any approximation? How does the approximation affect the reward and in turn the quality of the learned model?
- What is the auction mechanism used in this work? This mechanism is supposed to affect the learned policies in different agents.

Q2. In a competitive environment for DO auctions, it is unclear why DCs will follow the same approach (e.g., the one proposed in this paper). Any analysis about the incentives or truthfulness?
- Are different DCs forced to use the same RL approach? In a competitive market, it is not realistic unless all DCs have sufficient incentive to do so (e.g., under a truthful mechanism).
- Following the second question in Q1, how do different auction mechanisms affect the learned policies? Experiments can be conducted for two or three such mechanism (e.g., first-price/second price)

Q3. The presentation is clear in general, some minor things to be fixed, e.g., $S$ appears twice in (1) and (2) - I know the fonts are different but it is still a bit confusing.

### Soundness
2

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
3

### Summary
The work propose MultiBOS-AFL, a budget optimization strategy for auction-based Federated Learning that enables data consumers (DCs) to strategically allocate budgets over multiple training sessions. Using hierarchical reinforcement learning, MultiBOS-AFL optimizes both session-level budget pacing and within-session bidding, allowing DCs to maximize data acquisition and model utility within budget limits.

### Strengths
- MultiBOS-AFL is the first of its kind to implement budget pacing in multi-session auction-based federated learning.

- Experimental results demonstrate consistent outperformance over state-of-the-art approaches, achieving higher data acquisition rates and improved FL model accuracy.

- Leveraging hierarchical reinforcement learning allows MultiBOS-AFL to adjust its bidding strategies dynamically, optimizing DC outcomes in real-time.

### Weaknesses
- The explanation of the DOs' Reputation Calculation is unclear. The paper lacks motivation for incorporating the Beta Reputation System to compute the reputation value $v_i$. It is unclear how the Shapley Value metric relates to the Beta Reputation System, and the references provided do not adequately support this rationale. Please clarify the rationale behind combining the Shapley Value and Beta Reputation System and explain why these methods complement each other in this context.


- The Shapley Value-based contribution metric depends on the post-trained model using DO $i$'s data, $f(W\_{S\cup\{i\}})$, which is unrealistic. Before deciding whether DO $i$ will be accepted for training, we cannot access or use its data to obtain a post-trained model and then evaluate the model's performance. The reviewer suggests clearly explain how  to estimate the Shapley Value without prior access to the DO's data.

- The proposed multiple auction-based strategy has a weak connection to the federated learning training process. It is unclear how the selection of DOs impacts the overall FL model performance in practice.

### Questions
- Typo in line 189: "It is important to highlight that, as depicted in Eq. equation  3."

- Why Beta Reputation System can be used to compute the reputation value of DO $i$? What is the rationale behind its use?

- Except for the total budget, what is the connection between independent multiple sessions?

- If there are any approximation methods or alternative metrics that could be used instead of the Shapley Value?

### Soundness
2

### Presentation
1

### Contribution
2
