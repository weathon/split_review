# Generalized Principal-Agent Problem with a Learning Agent

- Decision: Accept
- Scores: 8, 5, 8, 8

## Abstract
Classic principal-agent problems such as Stackelberg games, contract design, and Bayesian persuasion, often assume that the agent is able to best respond to the principal's committed strategy. 
We study repeated generalized principal-agent problems under the assumption that the principal does not have commitment power and the agent uses algorithms to learn to respond to the principal. We reduce this problem to a one-shot generalized principal-agent problem where the agent approximately best responds. Using this reduction, we show that: (1) If the agent uses contextual no-regret learning algorithms with regret $\mathrm{Reg}(T)$, then the principal can guarantee utility at least $U^* - \Theta\big(\sqrt{\tfrac{\mathrm{Reg}(T)}{T}}\big)$, where $U^*$ is the principal's optimal utility in the classic model with a best-responding agent.
(2) If the agent uses contextual no-swap-regret learning algorithms with swap-regret $\mathrm{SReg}(T)$, then the principal cannot obtain utility more than $U^* + O(\frac{\mathrm{SReg(T)}}{T})$. 
But (3) if the agent uses mean-based learning algorithms (which can be no-regret but not no-swap-regret), then the principal can sometimes do significantly better than $U^*$.
These results not only refine previous results in Stackelberg games and contract design, but also lead to new results for Bayesian persuasion with a learning agent and all generalized principal-agent problems where the agent does not have private information.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper considers the principal's adaptive strategy design problem against a non-regret learning agent. The paper shows that the problem can be reduced from against an approximated best response agent.  The key technique is the perturbation argument.

### Strengths
- The paper introduces a novel problem along with a generic solution framework. I like its results derived from a clean reductions approach.
- The paper provides the reader's sufficient knowledge about the general principal-agent problem from Gan et al. (2024).
- The paper provides many well-sketched intuitions to help us understand its proofs.

### Weaknesses
 - The writing of the paper can be improved. For example, the paper could use a table to summarize all results and a table for all notations in this paper. While the paper is framed under the general principal-agent problem, it only discusses the Bayesian persuasion problem as its special case. 
- The major drawback of this paper is that the problem itself is not well-motivated. A no-regret learning agent would assume a stationary environment, but the principal here can adaptively adjust its strategy and make the environment non-stationary. I think there is a valid problem to study in theory, but it would be much better if we can derive some practical implication from this paper's results.
- While I find the result of this paper interesting, the technical depth of this paper is relatively shallow and thus I would not recommend higher level of acceptance for this paper.

### Questions
Why is it necessary in this paper to drop the private information in the generalized principal-agent problem from  Myerson (1982) and Gan et al. (2024)?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies "generalized principal-agent problem" in which a learning agent interacts with a principal who lacks commitment power. This setting can be used to describe several economic scenarios, like Stackelberg games and Bayesian persuasion. The paper focuses on the utility that the principal can achieve depending on the learning algorithm adopted by the agent—specifically, whether the agent uses a no-regret or no-swap-regret learning algorithm. The authors provide upper and lower bounds on the principal's achievable utility based on the algorithm played by the agent. To accomplish this, they establish a connection with the $\delta$-robust principal-agent problem, developing results that are of independent interest.

### Strengths
- The problem studied in the paper represents an interesting contribution to principal-agent problems that mainly focus on models in which the agent does not learn
- The results on the achievable utility when the agent plays a $\delta$-suboptimal best response according to a randomized strategy are interesting and novel

### Weaknesses
 - If my understanding is correct, the assumption that there exists a $p_0 \ge \min \mu_0(\omega)$ limits the applicability of the results in large state instances (since ${1}/{|\Omega|} \ge p_0$), which are well studied in Bayesian persuasion problems. I believe the authors should address this limitation explicitly in the paper and discuss potential extensions.
  
- Similarly, in Stackelberg games with a small inducibility gap, the proposed analysis does not hold.

- The approach to proving Theorem 4.1 (first point) appears somewhat incremental with respect to Gan et al. (2023). Both consider a convex combination (depending on the inducibility gap) of two strategies, where in one strategy the principal’s utility is larger than $G$ when they play specific action compared to all the remaining actions. This is not necessarily a drawback, but it raises questions about the technical novelty of this approach—perhaps related to the shape of the domain?

- The authors show that their model can be generalized to contract design settings. However, they should more clearly specify that they consider a model without costs, particularly in comparison with prior works. Furthermore, the model assumes that the agent chooses an action without knowledge of the contract the principal committed to, which is not realistic in contract design settings. The agent's action is based on a signal, i.e., the action recommended by the principal, without knowing the actual contract the principal committed to. This is problematic, as it implies that an agent performs an action on behalf of the principal without knowing how much the principal will pay it.

- Typo: Line 981 “Sectin”

### Questions
- In the statement of Theorem 5, the authors claim: "the sender can obtain a utility significantly larger than $U^*$ ..." Can the authors quantify what "significantly larger" means in the context of this theorem? Is it something proportional to the time horizon $T$? Furthermore, why does the lemma hold only in Bayesian persuasion settings?

- How can the fixed policy $\pi_t$ in the statement of Theorem 3.1 be computed?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper studies a generalized principal-agent problem where the agent learns to make decisions. The goal is to design the principal's strategy against such an agent. A sequential setting is considered, where the principal and the agent interact over time. The agent uses a no-regret algorithm to determine actions to perform in each time step, based on the past reward yielded by his actions. The paper considers different types of no-regret algorithms, including no-swap-regret and mean-based no-regret algorithms. Utilities the principal can achieve against these algorithms are analyzed, in comparison with the principal's optimal utility in the standard one-shot principal-agent model.

### Strengths
The paper is well-writen and very clear. I enjoy reading it. The topic of playing against a learning agent is very relevant to the theme of ICLR. Extending this line of research from standard normal-form games to generalized principal-agent problems is well motivated and interesting. The paper analyzed different types of no-regret algorithms and the results presented look quite complete. Technically, the results also look solid and are presented rigorously. The authors did a good job in explaining the intuitions behind the results, too.

### Weaknesses
I don't have any major concerns with the paper. One weakness is that Results 1 and 4 seem to largely follow by previous work and looks somewhat incremental. But the other results look sufficiently new and to extend normal-form games studied in previous work to generalized principal-agent problem seems to require a good amount of effort. It would be helpful if the authors can stress a bit more the differences between normal-form games and generalized principal-agent problem, and highlight the additional difficulties for addressing the latter.

### Questions
- I assume that the whole paper assumes the principal knows the agent's payoffs? If so it would be helpful to point that out more explicitly.

- There's also recent work on similar sequential principal-agent problems, which look relevant: Gan et al. (2023), Sequential principal-agent problems with communication: efficient computation and learning. What do you see any implications between your work and theirs?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a general method to reduce the repeated principal-agent games to one-shot approximate best-response on principal-agent games.

The setup is very close from the Bayesian Persuasion  one [Kamenica and Gentzkow, 2011].
The principal does not have commitment power but as in the Bayesian Persuasion setup, they can disclose information so to influence the agent’s behavior.
Then, the problem on a repeated game is reduced to a one-step game with approximately optimal action played by the agent. The reduction is achieved through the fact that a no-regret learning agent is behaving approximately optimally - which can be seen with the following equation:
$$V(\pi, d) - V(\pi, \rho) \leq CReg(T)/T,$$
which makes the agent’s actions a $\delta$-approximate best-response. After this reduction is done, the paper shows that an agent’s appropriate best response makes the principal's utility close from optimality. The proofs are achieved through a nice perturbation argument. The paper finally gives some applications to Bayesian Persuasion, Stackelberg games and Contract design.

I appreciate the fact that extending an online Bayesian Persuasion model, the paper recovers several interesting games and results. Also, the assumptions used are reasonable, which can be a lack in some papers from this kind of literature. As an example, for Theorem 3.1, the principal knows the agent’s regret bound but not the learning algorithm itself, which is a reasonable assumption and could be recovered in real-world scenarios.

### Strengths
I really enjoy the fact that the paper formulates interesting results about a fully abstract game theoretic setup. I think that great applications could be built relying on that.

One might wonder about the relevance of a theoretical paper on principal-agent issues for ICLR. However, the paper’s focus on signaling states and Bayesian perspectives effectively bridges representational learning with economic concepts, making it a strong fit for the conference.

The paper is well written and clear, which makes it pleasant to read.

### Weaknesses
 **First point:** My main concern is about the relation between the paper and existing results in the computational game-theoretic literature, especially in the link between no-regret and equilibrium.

I enjoy how the paper relates online learning problem between a principal and an agent to one-step games. However, I wonder if the results that are obtained (e.g., a principal's utility arbitrary close from the optimal one, etc) can be described in terms of coarse-approximate or coarse-correlated equilibrium. More discussion on this would be interesting since the paper does not mention any form of equilibrium at all.

Regret minimization of the agents alone is sufficient to ensure convergence to coarse correlated equilibrium in general-sum multiplayer games. This kind of results are given in these lecture notes for instance (https://www.mit.edu/~gfarina/2024/6S890f24_L04_regret/L04.pdf). Is it possible to formulate your setup as a game (for instance by saying that players commit to a strategy that will be more complex and will depend on a revelation of a state of nature) and then apply the equilibrium results to obtain your convergence/approximation rates?

**Second point:** I have a few comments on the setup. According to the authors, it is a general principal-agent game with a learning agent that recovers Bayesian Persuasion among other types of games. To me, this setup is exactly an online version of Bayesian Persuasion canonical setup, adding the fact that the principal also take an action $x_t$ alongside choosing a signal. It is not a huge issue but I think that the authors should not phrase their problem as such a general setup.

Below, I copied the model of the paper « Online Bayesian Persuasion », that is part of the references:

« We consider the following online setting. The sender plays a repeated game in which, at each round $t \in [T]$, she/he commits to a signaling scheme $\phi_t$, observes a state of nature $\theta_t \sim \mu$, and she/he sends signal $s_t\sim \phi^t_{\theta_t}$ to the receiver. Then, a receiver of unknown type updates her/his prior distribution and selects an action $a_t$ maximizing her/his expected reward (in the one-shot interaction at round t). We focus on the problem in which the sequence of receiver’s types ${k_t:t \in [T]}$ is selected beforehand by an adversary. After the receiver plays $a_t$, the sender receives a feedback on her/his choice at round t. In the full information feedback setting, the sender observes the receiver’s type $k_t$. Therefore, the sender can compute the expected payoff for any signaling scheme she/he could have chosen other than $\phi_t$. Instead, in the partial information setting, the sender only observes the action $a_t$ played by the receiver at round t. », Castigioni et al., 2020

I agree that it is different from what is proposed in the Generalized Principal-Agent Problem with a Learning Agent setup (page 4 in the paper) but it seems quite close though. The type of the agent in Castiglioni et al. could be represented as the strategy picked by the agent at round $t$ in this model. I think that this work desserves a more thorough discussion, due to its similarity with your framework. I think that good ideas are brought to the setup but the differences should be highlighted.


I put in the weakness section my main concerns but they should be seen more as questions and I am confident in a satisfying answer to them by the authors.

### Questions
I would say that the paper could be defined as an attempt towards information design with a learning agent and how to manipulate/persuade this agent. To my knowledge, the same kind of issues are becoming explored recently for mechanism design or Markov Decision Processes setups with a learning agent (as Guruganesh et al., 2024 with Contract theory, that you mention):

	- Learning to Mitigate Externalities: the Coase Theorem with Hindsight Rationality, that studies mechanism design bet-ween a learning principal and a learning agent on a bandit game and how the principal can align the agent’s actions on her preferences.

	- Principal-Agent Reward Shaping in MDPs, that studies principal-agent interactions on a MDP and formulates it as an  optimization problem.

	- Bayesian Incentive-Compatible Bandit Exploration, that studies how a principal could reveal information to incentivize the agent to take some specific actions - they also provide a black-box reduction of the problem to incentive-compatible bandits..

One could say that information design is about trading information while mechanism design is about trading utility. I believe that these references are close from your work and that it could be interesting to discuss them. How could they be related it?

Finally, it is mentioned that « the sender commits to a signaling scheme » and then follows $\pi(s|\omega)$ - it is always the case in Bayesian Persuasion. However, if we consider the setup of a game, I do not see why the principal would not deviate from it if this was in their interest. I think that this part of the model should be discussed with regards to real scenarios or motivations.

### Soundness
3

### Presentation
3

### Contribution
4
