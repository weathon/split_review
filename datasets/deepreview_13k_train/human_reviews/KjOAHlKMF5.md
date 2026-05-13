# Cascading Reinforcement Learning

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
Cascading bandits have gained popularity in recent years due to their applicability to recommendation systems and online advertising. In the cascading bandit model, at each timestep, an agent recommends an ordered subset of items (called an item list) from a pool of items, each associated with an unknown attraction probability. Then, the user examines the list, and clicks the first attractive item (if any), and after that, the agent receives a reward. 
		The goal of the agent is to maximize the expected cumulative reward. However, the prior literature on cascading bandits ignores the influences of user states (e.g., historical behaviors) on recommendations and the change of states as the session proceeds. Motivated by this fact, we propose a generalized cascading RL framework, which considers the impact of user states and state transition into decisions. In cascading RL, we need to select items not only with  large attraction probabilities but also leading to good successor states. This imposes a huge computational challenge due to the combinatorial action space.
		To tackle this challenge, we delve into the properties of value functions, and design an oracle $\algbestperm$ to efficiently find the optimal item list. Equipped with $\algbestperm$, we develop two algorithms  $\algcascadingeuler$ and $\algcascadingbpi$, which are both computation-efficient and sample-efficient, and provide near-optimal regret and sample complexity guarantees. 
		Furthermore, we present experiments to show the improved computational and sample efficiencies of our algorithms compared to straightforward adaptations of existing RL algorithms in practice.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies cascading reinforcement learning, which is a natural extension of cascading bandits to the episodic reinforcement learning setting. In particular, this paper has

- proposed the cascading reinforcement learning framework;

- developed a computationally efficient algorithm to solve the "cascading MDPs" (i.e. the cascading reinforcement learning problems with known models). The key ideas are summarized in the BestPerm algorithm (Algorithm 1). 

- developed a learning algorithm for the cumulative regret minimization setting, which is referred to as CascadingVI (Algorithm 2). A regret bound is also established (Theorem 1). This paper has also discussed the tightness of this regret bound.

- also developed a learning algorithm for the best policy identification setting, which is referred to as CascadingBPI. A sample complexity bound is established (Theorem 2). This paper has also discussed the tightness of this regret bound.

- demonstrated preliminary experiment results (Section 7).

### Strengths
In general, I think this paper is a strong theoretical paper, for the following reasons:

- This paper studies a natural extension of a well-studied problem. Moreover, as summarized above, the contributions of this paper are clear.

- The main results of this paper, summarized in Section 4 (efficient oracle), Section 5 (regret minimization), and Section 6 (best policy identification), are interesting and non-trivial. In particular, the regret bound in Theorem 1 and the sample complexity bound in Theorem 2 are non-trivial. Moreover, this paper has also discussed the tightness of these two bounds by comparing with existing lower bounds. Both bounds are near-optimal.

- The paper is well-written in general, and is easy to read.

### Weaknesses
 - I am wondering if the developed algorithms are useful for practical recommendation problems. The reason is that, this paper considers a tabular setting, thus the developed regret bound and the sample complexity bound depend on the number of states $S$. However, my understanding is that for most practical recommendation problems, $S$ will be exponentially large. Might the authors identify a setting where $S$ is not too large and hence the proposed algorithms are practical?

- Currently the experiment results are very limited. In particular, this paper has only demonstrated experiment results in small-scale synthetic problems. I think experiment results on large-scale practical problems will further strengthen this paper.

### Questions
Please address the weaknesses above.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a new framework for reinforcement learning (RL) called cascading RL, which builds upon the concept of cascading bandits but incorporates state information into the decision-making process. This framework is aimed at applications such as personalized recommendation systems and online advertising, where cascading items are displayed to users one by one.

Key challenges addressed include computational difficulty due to the combinatorial nature of actions and ensuring sample efficiency without relying on the exponential number of potential actions. To overcome these, the authors developed an efficient oracle called BestPerm, which uses dynamic programming to optimize item selection. They also introduced two RL algorithms: CascadingVI for regret minimization and CascadingBPI for sample complexity, both of which utilize BestPerm to achieve polynomial regret and sample complexity.

CascadingVI achieves near-optimal regret matching a known lower bound. CascadingBPI offers efficient computation and sample complexity, reaching near-optimal performance.

In summary, the paper contributes a new cascading RL framework that efficiently handles the computational and sample complexity challenges of stateful item selection, supported by theoretical guarantees and demonstrated effectiveness through experiments.

### Strengths
- As far as I know, this would be the first theory RL work with cascading actions. The formulation is sound.
- The paper proposes an efficient optimization oracle for cascading RL, providing its correctness (it would be better to show it in the main text rather than the appendix).
- Although it is not groundbreaking, the paper provides both regret analysis and sample complexity analysis.

### Weaknesses
 - It seems that the techniques used for regret analysis and sample complexity are largely borrowed from the previous literature. I wonder if there are sufficient technical challenges once you know how to solve Problem (2).
- The readability of the algorithms can be improved. e.g., Update rule of $\bar{q}^k$ and $\underbar{q}^k$ in Line 6 of Algorithm 2, Line break in Line 8 of Algorithm 2, etc.

### Questions
Where does the gap $\sqrt{H}$ appear? Can you elaborate on this? Any possible direction to carve off this given that the tabular RL methods with a single action can achieve minimax optimality?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an extension of the cascading bandits framework to a more general reinforcement learning framework. The authors thereby attempt to model user sessions or historical user behavior and their impact on the click behavior and payoff.  While the action space (i.e., combination of items) is combinatorial, the feedback is item-wise so that attraction and transition probabilities can be estimated efficiently. This allows the authors to design algorithms with non-trivial regret and sample complexity guarantees. In particular, the authors rely on monotonicity properties to design an efficient oracle. Finally, the authors support their theoretical findings through experiments which support the efficiency of the proposed algorithms.

### Strengths
- Firstly, I think that the studied problem is interesting and the presentation of the paper clear. 
- The extension of the cascading bandit model to an RL formulation is highly non-trivial and the paper contains novel contributions including the RL formulation itself and an interesting algorithm design which relies on properties of the value function. 
- The authors do a good job explaining their algorithms and provide intuition for their results.  
- The necessity of adopting standard RL algorithms to the proposed cascading model is highlighted in the paper several times and the authors thereby provide proper justification for the proposed algorithms.

### Weaknesses
 - I am not fully convinced of the practicality of this model. Firstly, historical user behavior can be modeled as part of the context in contextual bandit frameworks. Moreover, "artificially" creating states appears fairly cumbersome compared to the contextual bandit structure and it is also not entirely clear how such states would be defined in practice. The paper does not sufficiently address the challenges of state definition, which is crucial for the applicability of the proposed RL framework. For instance, in a real-world recommendation system, how would one discretize the user's interaction history into a manageable set of states that are both meaningful and allow for effective learning? The paper also does not discuss the computational overhead of maintaining and updating these states, which could be a significant concern for large-scale applications. Furthermore, the assumption that state transitions are Markovian might not hold in many practical scenarios, where user behavior can be influenced by factors beyond the immediate previous state. This lack of discussion regarding the practical challenges of state definition and management undermines the claimed advantages of the RL formulation.


### Questions
- Could you further explain why contextual approaches are insufficient and what the merit of the RL formulation is in contrast to contextual bandits or recommendation approaches based on context trees? In the RL framework it is important what states the user transitions to, as some states may have the potential to yield higher rewards than others. Do you think that this is realistic in practice?  

- It would be great if you could go into a bit more detail in your related work section and more clearly highlight the differences to prior models. For example, in contrast to the classical cascading bandits, the order of items also matters in your case as you usually would like the item with largest reward in state s to be clicked. 

Minor things: 
- In the 4th contribution, I found the statement about "$\varepsilon$ sufficiently large" slightly confusing. It only becomes clearer later in Theorem 2 when the full bound is stated. Maybe there is a way to state this less conusingly in the introduction.  
- Typo in the 3rd paragraph of Section 7: "Regarding the best policy identification objective" instead of "Regarding the regret minimization objective".

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper tackles the Cascading Bandits problem over a Markov Decision Process, where time is divided into episode of fixed length $H$, and the attractiveness of items (which determined the expected state transitions and rewards) is dependent on a state at the current step in the episode. At each step in the episode, the system gets to observe the current state and proposed a ranked list of items and the environment provides a click on one of the items according to the cascading click model. For this problem, the paper provides a method for computing the optimal offline strategy when all distributions are known and an introduces the CascadingVI algorithm along with a regret bound of $O(H\sqrt{HSNK})$, where $H$ is the episode length, $S$ is the number of states, $K$ the number of episodes and $N$ is the number of individual items available to rank. The performance of the proposed algorithm is compared numerically with a baseline algorithm produced by adapting an existing algorithm to the combinatorial space, referred to here as AdaptRM.

### Strengths
- generalizes the cascading bandit problem to MDPs
- provides numerical experiments, even though, in my opinion the baseline is too weak
- provides theoretical guarantees and proofs of correctness
- generally well written, despite the convoluted algorithms I could navigate my way around the paper.

### Weaknesses
 - The significance of the contribution is not substantial enough to justify acceptance into the venue in my opinion. One of the main contributions is providing an algorithm that does not scale in complexity (both sample or computational) with the space of all possible rankings. I believe we have well-known recipes for how such algorithms can be formulated since the papers on Cascading Bandits from 2015 (Kveton et. al, Combes et al.). Providing a solution scaling with the number of items is expected in my opinion and not a surprising contribution (we know that estimating individual CTRs is enough to construct optimal rankings, we don't need to keep statistics on each individual ranking). This also leads me to believe the baseline used in the numerical experiments is weak.
- The contribution related to the generalization to MDPs is not opening a significant amount of new doors. In my opinion, this generalization does not provide further theoretical insights and has limited additional practical relevance.
- The experimental section use a setting that is too simplistic (very few items and states) and a weak baseline, in my opinion, thus not being representative enough of what we can expect from this algorithm in practice.

### Questions
On line 8 in Algorithm 2, what is the complexity of computing $E_{s'\sim p^k}[ .... ]$? 

Regarding BestPerm, to me it feels like the biggest hurdle is the computational complexity of computing the value functions $w$, which BestPerm assumes is an input. How does your proposed algorithm navigate this difficulty? 

I would also like to see more intuition regarding the exploration bonus $b^{k, pV}(s, a)$, in particular: how is the optimism of $\overline{V}^k_h(s)$ connected to the uncertainty in the estimates of state transition probabilities $p$? The algorithm is already fairly convoluted and it is hard to see how we can construct optimistic estimates of the value functions in light of estimation noise in the state transition probabilities. I believe it is very valuable to clearly articulate such insights in the main body of the paper.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
