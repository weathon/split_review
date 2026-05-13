# Feature-Based Online Bilateral Trade

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
Bilateral trade models the problem of facilitating trades between a seller and a buyer having private valuations for the item being sold.
    In the online version of the problem, the learner faces a new seller and buyer at each time step, and has to post a price for each of the two parties without any knowledge of their valuations. 
    We consider a scenario where, at each time step, before posting prices the learner observes a context vector containing information about the features of the item for sale. The valuations of both the seller and the buyer follow an unknown linear function of the context. In this setting, the learner could leverage previous transactions in an attempt to estimate private valuations. 
    We characterize the regret regimes of different settings, taking as a baseline the best context-dependent prices in hindsight. First, in the setting in which the learner has two-bit feedback and strong budget balance constraints, we propose an algorithm with $O(\log T)$ regret. Then, we study the same set-up with noisy valuations, providing a tight $\widetilde O(T^{\nicefrac23})$ regret upper bound.
    Finally, we show that loosening budget balance constraints allows the learner to operate under more restrictive feedback. Specifically, we show how to address the one-bit, global budget balance setting through a reduction from the two-bit, strong budget balance setup.
    This established a fundamental trade-off between the quality of the feedback and the strictness of the budget constraints.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper tackles the bilateral trade problem in an online setting where there is an additional context present. At each time step $t$, a buyer and a seller arrive with private values $b_t$ and costs $s_t$. The algorithm must provide a pair of prices $(p,q)$ such that a sale happens if the buyer's value $b_t$ is less than $q$ and the seller's value is above $p$. The Gain from this trade assuming a sale happens is $(b_t - s_t)$.  The authors consider the problem of maximizing the gains from trade assuming either two bit feedback where we find out if $\mathbb{1}[b_t \leq q] $ and if $\mathbb{1}[s_t \geq p]$. They also consider the model where we have only one bit feedback where we know the product of these two bits of feedback. The original problem was already studied by Cesa-bianchi et al. This problem considers the setting where the buyer and seller have a hidden vector of preferences $\theta_b, \theta_s$ and their private values are generated from a shared context $b_t = x_t^T \theta_b$ and $s_t = x_t^T \theta_s$ . They consider where there may be some noise that is added as well as the budget balanced setting where the prices offered to both parties must be the same ($p=q$). 


The main results:

1) In the two feedback setting with strong budget balance $p=q$ at each time step when there is no noise in the setting. Here the authors use a natural modification of the feature based toolification.
2) In the two bit feedback model with noise, where the noise is i.i.d coming from distributions with bounded support and densities. Finally they devise an algorithm following the explore-or-commit framework where the authors decompose the gain in terms 
3) They also study the one bit feedback problem where you only find out if a sale happens or not. To get good bounds for this model they assume they have a good regret for the strongly-balanced two bit feedback and then use that in a black box manner. However the new bounds only have a global budget balanced guarantee.

### Strengths
The authors propose a very reasonable contextual model of online bilateral trade. I find the new model to be well motivated and combines two natural areas of study namely bilateral trade and online contextual regret minimization. The algorithms themselves seem interesting and are fairly natural. 

The reduction from the two bit strong budget balanced case to the one bit global budget balanced case is perhaps the most interesting to me. Essentially it is a general recipe where by one can exploit explore-or-commit algorithms and perform the explorations in such a way that we can always get feedback about either the buyer or seller. However, we may lose regret compared to other party, and thus we need to ensure that there is sufficient budget to do this. This is done by measuring the average profit the 2 bit algorithm can learn and then appropriately setting the parameters to balance out the findings.

### Weaknesses
Although the algorithms are natural and interesting, I am unable to distinguish where the new ideas are and how much of the paper is using known tools to a new setting. I would appreciate more explanation on what the new ideas are in both the two bit setting and the one-bit setting. 

Specifically, in the two-bit setting, the adaptation of feature-based pricing is mentioned, but it is not clear how the challenges of bilateral trade, such as the interdependence of buyer and seller valuations, are addressed. For example, how does the algorithm handle scenarios where the uncertainty sets for the buyer's and seller's valuations overlap? How does it determine the optimal price within this intersection, given that any price within the range between the buyer's and seller's valuations theoretically yields the same reward? 

In the one-bit setting, the reduction from the two-bit strong budget-balanced case is mentioned as a general recipe. However, the details of this reduction are not sufficiently elaborated. It is stated that explorations are performed in a way that feedback is obtained about either the buyer or the seller, but how is this achieved in practice? What specific mechanisms ensure that sufficient information is gathered about both parties, especially when only one bit of feedback is available? Furthermore, the paper mentions a potential loss of regret compared to the other party. A more detailed explanation of how this loss is quantified and mitigated would be beneficial.

### Questions
1) I am wondering why the stronger bounds from Contextual Search (Liu et al) were not used in place of the Feature Based Pricing. It seems many of the ideas would carry over and you would achieve improved regret guarantees.

2) It would be useful to know what new ideas are introduced for noisy setting  and how much was already known in other settings.

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors investigate online contextual bilateral trade problem, where the valuations of two traders are modeled by different (unknown) linear functions. The authors focus on two different feedback models: (1) two-bit feedback model, where the learner can observe the binary feedback of both traders (2) one-bit feedback model, where the learner can only learns the binary information of whether the trade happens or not. For (1), the authors propose an online learning algorithm to set trading price at each round (that satisfies the strong budget balance constraint), which achieves $O(T^{2/3})$ regret. The authors also show a matching lower bound. For (2), the authors provide a reduction from one-bit feedback model to two-bit feedback model by sacrificing per-round budget balance to global budget balance and show the algorithm used in (1) can be applied to (2) and still achieves sublinear regret guarantee.

### Strengths
The paper is well-written and analyzes a very interesting theoretical problem. The authors did a good job to describe the problem and how the algorithm handles the challenges. 

The theoretical guarantee of the paper is sound. The authors provide a complete story for the setting with two-bit feedback model. In addition, the reduction from one-bit to two-bit by sacrificing budget balance constraint is very interesting and elegant.

### Weaknesses
There is no matching lower bound for the one-bit feedback setting. I also have some questions regarding this setting.

### Questions
1. Can you elaborate a bit more about the comparison with the related work, "A contextual online learning
theory of brokerage. arXiv preprint arXiv:2407.01566, 2024"? The setting is very similar, however, it seems the valuations of two traders in their paper share the same expected value.

2. For the one-bit feedback model, if we want to maintain per-round budget balance, is it still learnable?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the bilateral trade model which involves the challenge of enabling transactions between a seller and a buyer who both hold private valuations for the item. This paper considers specifically the online scenario, where at each step there is a fresh seller and buyer entering the system and the pricing decisions for both parties must be made immediately without prior knowledge of their valuations. The paper further restricts to the contextual setting where the private valuations for the seller and buyer are linearly featured by a context. A two-bid feedback is considered where for both the seller and the buyer, it can be observed whether the posed price has exceeded its value or not. By further assuming a strong budget balance between the buyer and the seller, the paper is able to derive a $O(\log T)$ regret. Without the budget balance conditions, the paper achieves a $O(T^{2/3})$ regret, which is minimax optimal. The paper further discusses the one-bit feedback and shows the potential to obtain a sub-linear regret.

### Strengths
1. The paper derives strong $O(\log T)$ regret, though under stronger conditions.

2. The paper derives $O(T^{2/3})$ regret upper bound for their algorithm and shows that there exists a matching lower bound.

### Weaknesses
1. The main results of the paper rely on the two-bid feedback setting, where both the seller and the buyer reveal to the decision maker whether they want to sell the product or buy the product. This is quite a strong condition, and the paper would benefit from a more detailed discussion on whether this condition happens or not in reality. Specifically, while the paper assumes that both the seller and buyer provide feedback on whether the posted price exceeds their private valuation, it is unclear how this information is obtained in practice, especially in scenarios where agents are strategic and may not truthfully reveal their preferences. The paper should discuss the practical limitations of this assumption and potential mechanisms to elicit truthful feedback.

2. Though the theoretical guarantee is provided, there are not numerical experiments in the paper showing the empirical performances. Also, the computation complexity of the proposed algorithms has not been discussed. The lack of numerical experiments makes it difficult to assess the practical relevance of the proposed algorithms. Furthermore, a detailed analysis of the computational complexity, including the per-iteration running time and memory requirements, is essential for understanding the scalability of the proposed approach.

3. The algorithmic idea and the proof technique mainly build upon the previous work Cohen et al. (2020) and it has not been discussed which part of the proof is novel. While the paper acknowledges the connection to previous work, it does not clearly delineate the novel contributions in terms of algorithmic design and proof techniques. A more detailed explanation of the specific innovations is needed to justify the contribution of this work.

4. The $O(\log T)$ regret depends on some strong conditions that are hard to justify in practice. The strong budget balance condition, requiring the prices posted to the seller and buyer to be identical, is a significant constraint that may not hold in many real-world scenarios. The paper should discuss the limitations of this assumption and the potential impact on the applicability of the results.

5. The paper is overall theoretical and it is not clear how to apply their algorithm in practice. The paper lacks a clear discussion of how the proposed algorithms can be implemented in practice. The paper should provide more concrete guidance on how to translate the theoretical framework into a practical system, including details on parameter tuning and implementation considerations.

### Questions
1. How do you check whether the strong budget balance condition holds or not?

2. Could you please conduct numerical experiments to show the real performance? Also, what is the computation complexity of your algorithms.

### Soundness
2

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
The authors study the feature based online bilateral trade problem. Here,  the buyer's valuations are given by a linear function. The seller's valuation is similar. In each round, the buyer and seller see a new context that along with their private parameter vector determines the parameterized part of the reward. The noisy version of the problem adds a i.i.d. random variable (not necessarily zero mean) with the parameterized reward.  The authors study the problem in both 2-bit and 1-bit feedback under strong and global budget balance constraints, respectively. For the deterministic version they adopt existing  EllipsoidPricing policy and show a log(T) regret bound. For the noisy, version they propose an Explore-or-Commit algorithm that achieves a $O(T^{3/4})$ regret, which is further improved to $O(T^{2/3})$ (which matches the lower bound). Some tradeoff between budget and regret is established for 1-bit feedback case.

### Strengths
- This work initiates the feature based online bilateral trade problem
- With budget balance and two-bit feedback they establish a tight $O(T^{2/3})$ regret bound with by combining Scouting and Explore-or-Commit strategies. 
- They extend the results to the one-bit feedback setup while maintaining the regret guarantees under the budget balance constraint.

### Weaknesses
 - See questions for more discussions around improving the paper, and my own curiosity.

### questions:
 Two bit feedback:
- Do we gain anything by removing the budget balance constraint in the two-bit feedback case (simplifying the algorithm maybe)?
- Can the authors provide more intuition of how combining the ETC, and Scouting strategy works? (maybe along the line -> with $O(T^\beta)$  exploration regret we reduce the 'Range of Delta_t' = $O(T^{-\alpha})$ and then the Scouting results in $O(T^{2/3})$ regret)
- As we do not rely on the exact reward feedback, will approximately linear reward functions work? 


One bit feedback:
- In the one-bit feedback case, is the knowledge of $\alpha$ essential? 
- Can the authors discuss if the $\alpha$ dependency a side effect of selecting the specific strategy of collecting the profit in the first phase? Can we improve/remove such dependency by adaptively collecting the budget or by leveraging improved exploration strategy?

### Questions
Two bit feedback:
- Do we gain anything by removing the budget balance constraint in the two-bit feedback case (simplifying the algorithm maybe)?
- Can the authors provide more intuition of how combining the ETC, and Scouting strategy works? (maybe along the line -> with $O(T^\beta)$  exploration regret we reduce the 'Range of Delta_t' = $O(T^{-\alpha})$ and then the Scouting results in $O(T^{2/3})$ regret)
- As we do not rely on the exact reward feedback, will approximately linear reward functions work? 


One bit feedback:
- In the one-bit feedback case, is the knowledge of $\alpha$ essential? 
- Can the authors discuss if the $\alpha$ dependency a side effect of selecting the specific strategy of collecting the profit in the first phase? Can we improve/remove such dependency by adaptively collecting the budget or by leveraging improved exploration strategy?

### Soundness
4

### Presentation
3

### Contribution
3
