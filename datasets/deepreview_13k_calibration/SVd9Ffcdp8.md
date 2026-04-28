# Deep Reinforcement Learning for Sequential Combinatorial Auctions

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Revenue-optimal auction design is a challenging problem with significant theoretical and practical implications. Sequential auction mechanisms, known for their simplicity and strong strategyproofness guarantees, are often limited by theoretical results that are largely existential, except for certain restrictive settings. Although traditional reinforcement learning methods such as Proximal Policy Optimization (PPO) and Soft Actor-Critic (SAC) are applicable in this domain, they struggle with computational demands and convergence issues when dealing with large and continuous action spaces. In light of this and recognizing that we can model transitions differentiable for our settings, we propose using a new reinforcement learning framework tailored for sequential combinatorial auctions that leverages first-order gradients.  Our extensive evaluations show that our approach achieves significant improvement in revenue over both analytical baselines and standard reinforcement learning algorithms. Furthermore, we scale our approach to scenarios involving up to 50 agents and 50 items, demonstrating its applicability in complex, real-world auction settings. As such, this work advances the computational tools available for auction design and contributes to bridging the gap between theoretical results and practical implementations in sequential auction design.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work investigates sequential combinatorial auctions, an instance of auction where the bidders arrive in a sequence and place bids on bundles (combinations) of items. Sequential combinatorial auctions is relevant due to its simplicity, its strategyproofness, and its generality. This work aims on numerically finding the optimal solution. Previously, this was achieved by formulating the problem into an MDP, and then running PPO on it. But the previous work was under the additive assumption so it did not really tackle the combinatorial nature of the problem. This obviously skipped the exponential action space brought by the bundles.

This work leverages the particular structure of auction, and proposes a gradient that uses the knowledge of the world model. This allows a first-order gradient feedback of the update. The work is inspired by fitted policy iteration (which I'm not sure why the manuscript did not cite any previous work) and the policy improvement step of which could benefit from the gradient derived.

With some additional techniques and tricks, the work is capable of hosting a decent size (at most 50 items) problem. Experiments are conducted on both additive and combinatorial settings against baselines including mechanism design methods and the previous RL approach. The proposed method seems to work well on the experiments.

### Strengths
1. This work numerically solves sequential auctions with combinatorial action space. The solution is through an organic synergy between policy gradient and the auction process.
2. It scales to an action space with as many as 50 items.
3. Experiments show that it outperforms previous baselines.

### Weaknesses
1. The topic (sequential auction + combinatorial + numerical solution) is a bit limited to the specific sub-community. I'm not seeing the method/techniques to be of a general interest.
2. The experiments are conducted only on toy examples. Given the numerical nature of the work, I was expecting some real data, or even real system, experiments.

### Questions
Isn't FTI an existing algorithm? I don't see a citation on that.

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
2

### Summary
This paper proposed a method on designing revenue-optimal mechanisms for sequential combinatorial auctions to allocate items to multiple agents in stages where the agents place bids on bundles of items based on their preferences using DRL with designs like analytical gradients.

### Strengths
- The paper is generally well-written and easy to follow, the motivation on solving limitations from RL on sample inefficiency and issues with convergence in large, continuous action spaces is valid
- Use of Analytical Gradients seems to be effective in enhancing sample efficiency and convergence.
- The approach demonstrates scalability to scenarios with empirical results.

### Weaknesses
 -  Despite improvements, the method may still face computational challenges in extremely large-scale auctions, similar to issues noted in Pieroth et al. (2023).
- The reliance on known valuation distributions may limit applicability in settings where such information is unavailable which limits the use cases of this method, more explanation on this would be good
- The baseline selection needs to be justified, why not also compare with more state-of-the-art algorithms?
- This approach uses a fixed order of agent visits, which can limit its optimality in situations where the order of bidding impacts the auction’s overall revenue.
- Whether and how much this work is sensitive to hyperparameters is not explained.

### Questions
Please see weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper explores designing revenue-maximizing mechanisms in sequential combinatorial auctions (SCAs) using deep reinforcement learning (DRL). SCAs present auction items sequentially, allowing bidders to make strategic choices at each stage. Although traditional sequential auctions have theoretical guarantees, they lack mechanisms to maximize revenue in complex environments. This paper addresses these limitations by proposing a deep reinforcement learning framework that leverages analytical gradients to optimize auctions involving multiple agents and items efficiently.

### Strengths
1. The paper provides theoretical foundations for its policy optimization approach and demonstrates its effectiveness through extensive experiments. 
2. The paper introduces a new way to handle DRL in SCAs, particularly in combinatorial and high-dimensional settings.

### Weaknesses
 * The method involves fitted policy iterations and analytical gradients. The complexity can be increased and needs to be measured.
* The framework assumes knowledge of agents' valuation distributions, which may not always be accessible or accurate in practice.

### Questions
1. What is the complexity of the new proposed method?
2. How to reduce the reliance on agents' valuation distributions?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a new approach that uses fitted policy iteration and analytical gradients for learning revenue-maximizing sequential combinatorial auctions. Using twofold manner: initially refining the value function to align with the policy function and subsequently adjusting the policy function to maximize rewards. This method also can used in continuous action spaces via gradient descent.

### Strengths
This paper introduces a new approach that uses fitted policy iteration and analytical gradients for learning revenue-maximizing sequential combinatorial auctions. Using twofold manner: initially refining the value function to align with the policy function and subsequently adjusting the policy function to maximize rewards. This method also can used in continuous action spaces via gradient descent.

### Weaknesses
No

### Questions
No

### Soundness
3

### Presentation
3

### Contribution
3
