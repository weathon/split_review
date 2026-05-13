# Markov Persuasion Processes: Learning to Persuade From Scratch

- Decision: Reject
- Scores: 3, 5, 5, 5, 3

## Abstract
In \emph{Bayesian persuasion}, an informed sender strategically discloses information to a receiver so as to persuade them to undertake desirable actions.
	Recently, \emph{Markov persuasion processes} (MPPs) have been introduced to capture \emph{sequential} scenarios where a sender faces a {stream of myopic receivers} in a Markovian environment.
	The MPPs studied so far in the literature suffer from issues that prevent them from being fully operational in practice, \emph{e.g.}, they assume that the \emph{sender knows receivers' rewards}.
	We fix such issues by addressing MPPs where the sender has no knowledge about the environment.
	We design a learning algorithm for the sender, working with partial feedback.
	We prove that its regret with respect to an optimal information-disclosure policy grows sublinearly in the number of episodes, as it is the case for the loss in persuasiveness cumulated while learning.
	Moreover, we provide a lower bound for our setting matching the guarantees of our algorithm.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper considers learning in a Markov persuasion process (MPP) where the learner cannot take actions directly, and must persuade a receiver to take the intended action. The focus is on the setting where the learner is not aware of the receiver's reward function and must guarantee that both the regret in total reward and violation of persuasion constraints is sublinear in $T$. The authors consider two settings -- (a) full feedback setting where the learner observes the rewards for all the actions at a time-step, and (b) partial feedback setting where the learner observes rewards only for the chosen action.

The authors propose an optimistic planning based algorithm which finds persuasive policy by being optimistic according to sender's rewards and receiver's persuasion constraints. For the full feedback setting the reward regret and violation of constraints is $O(\sqrt{T})$, whereas for the partial feedback setting there is a trade-off between regret in reward and violation of constraints.

### Strengths
The authors consider an interesting extension of MPP when the sender is unware of the receiver's rewards and must learn them over time. The algorithms and the main ideas are explained clearly in the paper. It's also interesting to see that the authors provide a trade-off between the reward regret and the violation of persuasion constraints.

### Weaknesses
1. The authors claim that it is impossible to satisfy persuasive constraints at all rounds. However, the negative result is provided only for the partial feedback setting, and I wonder if one can avoid the negative result for the full feedback setting. If so, it makes more sense to study a version of MPP where the constraints are satisfied with high probability. In general, I favour the guarantee of high probability persuasion compared to providing only upper bound on the total amount of violation. Since we cannot make any assumption about receiver's preferences, it is not clear whether the receivers will still follow the sender's recommendation.

2. The proposed algorithms and the proof techniques are very similar to prior work (in particular Bernasconi et. al. 2022 or Gan et. al. 2024). All these works propose explore then exploit (based on optimistic planning) algorithm for persuasion problems. So the authors need to clarify what are the technical difficulties in the analysis in this paper.

3. It is not clear that the optimistic planning problem can be solved efficiently i.e. poly(|X|, |A|, L) time.

4. Finally, the authors consider only tabular MDPs. The original paper on MPP did consider more general MDPs and without such extensions, it is not clear whether the result generalizes.

### Questions
1. What is the trade-off between reward regret and constraint violation for the full feedback setting?

2. What is the time-complexity of Opt-Opt problem (2)?

3. Can you generalize your results beyond tabular MDP?

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
2

### Summary
This paper studies the Markovian Persuasion Processes (MPPs), a repeated version of Bayesian persuasion, by relaxing the common assumption that the sender knows receivers’ rewards. Unlike previous works, the authors use the setting in which the senders have no knowledge about transitions, prior distributions over outcomes, sender’s stochastic rewards, and receivers’ ones. Removing this requirement allows for capturing real-world problems, for e.g.,  online streaming platforms recommending movies to its users. The authors propose a learning algorithm, Optimistic Persuasive Policy Search (OPPS) for the sender with partial feedback and prove that its regret with respect to an optimal information-disclosure policy grows sublinearly in the number of episodes.

### Strengths
The paper considers a natural extension of the existing MPP studies by relaxing the assumption of full knowledge about the environment and the players. The problem formulation as well as the objectives of the learning problem are clearly described. Mathematical proofs are also provided that highlight the effectiveness of the proposed algorithm.

### Weaknesses
I think the major weakness of this paper is the missing case study. While the authors highlight “practical/real-world application” as the key motivation behind studying this variation of MPP, they fail to provide an example (or a simple toy case). I think the paper would benefit from a case study as it would also help readers to understand the problem better.

I am not an expert in this topic, but from what I gathered, the setup in the paper resembles a general-sum game, is that correct? If so, could it be also extended to model a zero-sum game in which it may not be in the receivers' best interest to follow the sender?

In line 383:
> ...the sender does not observe sufficient feedback about the persuasiveness of $\phi_t$.
  * Could the authors comment on what are the necessary feedback to infer about the persuasiveness and why the information about only the agents' rewards for the visited triplets are not enough?

### Questions
* I am not an expert in this topic, but from what I gathered, the setup in the paper resembles a general-sum game, is that correct? If so, could it be also extended to model a zero-sum game in which it may not be in the receivers' best interest to follow the sender? 

* In line 383:
> ...the sender does not observe sufficient feedback about the persuasiveness of $\phi_t$.
  * Could the authors comment on what are the necessary feedback to infer about the persuasiveness and why the information about only the agents' rewards for the visited triplets are not enough?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the online learning version of Markov Persuasion Process (MPP). An MPP involves a sender and a receiver interacting for $L$ time steps, where at each time step with state $x_k$ commonly observed by both players, the sender sees an additional outcome $\omega_k \sim \mu(x_k)$ (only observed by the sender) and sends a signal (action recommendation) to the receiver according to some signaling scheme, then the receiver takes an action that affects the rewards of both players and the state transition. The authors assume that the sender does not know any information about the environment (the prior $\mu$, the transition matrix, the receiver's reward, and their own reward).  Repeating this MPP $T$ times, the sender aims to learn the environment and the optimal signaling scheme over time.  The main results include:
- With full feedback (which includes the realized rewards of all actions at each round), the authors design a learning algorithm that achieves $O(L^2|X| \sqrt{T |A||\Omega| \ln(1/\delta)})$ regret for the sender, and $O(L^2 |X| \sqrt{T |A| |\Omega| \ln(1/\delta)})$ violation of the persuasiveness constraint (i.e., the regret for the receiver if the receiver follows the action recommendation.)
- With partial feedback (which includes the reward of the taken action only), the authors design a learning algorithm with $O(T^\alpha)$ regret for the sender and $O(T^{1-\alpha/2})$ violation for the receiver, where $\alpha\in[1/2, 1]$. 
- A lower bound showing that no learning algorithm can achieve regret $o(T^{\alpha})$ and violation $o(T^{1-\alpha/2})$.

### Strengths
(S1) This paper provides a relatively complete picture for the online MPP problem, providing upper and lower bounds on the sender's regret and the receiver's violation that are tight in terms of $T$. 

(S2) Compared to previous works in online MPP that all assume that sender has some type of knowledge of the environment, this work makes no such assumption.  This is a significant conceptual contribution.

### Weaknesses
(W1) Although this paper provides a relatively complete picture for the online MPP problem, most of the techniques are standard and directly come from previous works. The upper bound techniques come from the constrained Markov Decision Process (MDP) literature, e.g., [Germano et al, 2023](https://arxiv.org/pdf/2304.14326), as the authors mentioned. The MPP problem is basically a constrained MDP with linear objective and linear constraint (maximizing the sender's expected reward subject to persuasiveness constraint), for which the constrained MDP literature already provides satisfactory solutions. Specifically, the paper adapts techniques like Lagrangian relaxation and online gradient descent, which are standard in constrained MDPs. The novelty in adapting these techniques to the MPP setting is not clearly articulated, and it appears that the core challenges of the problem are addressed by directly applying existing machinery. Furthermore, the specific handling of the persuasiveness constraint, while necessary, does not introduce fundamentally new algorithmic ideas beyond what is already present in the constrained MDP literature. The lower bound is basically the same as previous paper [Bernasconi et al (2022)](https://proceedings.neurips.cc/paper_files/paper/2022/file/6604fbf7548524576c9ee2e30b0d5122-Paper-Conference.pdf), except that previous bound only works for $\alpha \in[1/2, 2/3]$ while this paper improves to $\alpha \in [1/2, 1]$. This extension, while technically non-trivial, does not represent a major conceptual leap. 

(W2) Although the regret bounds in this work are tight in $T$, there is still a large gap between the upper and lower bounds in terms of other parameters $L, |X|, |\Omega|, |A|$. The lower bound does not contain those parameters, while the upper bound have polynomial dependency on them. In the full information setting for example, an upper bound in the form of $O(parameter * \sqrt{T})$ is typical in the online learning literature (in particular, it can be easily derived from the previous constrained MDP techniques), and a lower bound like $\Omega(\sqrt{T})$ is also expected. Since this work aims to give a complete picture for the online MPP problem, I think it is important to characterize the tight dependency of the regret on parameters other than $T$ as well. Moreover, given that there are already several previous works on online Bayesian persuasion and MPP (like Wu et al (2022)), only characterizing the regret dependency on $T$ does not seem to be a large enough contribution to the existing literature. The lack of tight bounds with respect to these parameters limits the practical applicability of the results, as it is unclear how the algorithm would scale with increasing state space, action space, or length of interaction.

### Questions
**Question:**

(Q1) How is your work different from the constrained MDP works you cited?  What's the additional contribution? 

(Q2) Can you provide a lower bound that includes the parameters of the environment? 


**Suggestions:**

- Typo: Line 428: "si" -> "is".

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the Markov persuasion process (MPP) in which the sender does not know the environment, i.e., the transition, prior, and reward functions. They consider two types of feedback: full feedback and partial feedback. Full feedback means that the sender can observe all agents' rewards for the realized state and outcome in every round, but partial feedback means that the sender can only observe agents' rewards for the realized state, outcome, and action in every round.

The authors design algorithms for both kinds of feedback that achieve sublinear regret and violation of persuasiveness. Furthermore, the algorithm for the partial feedback has a matching lower bound.

### Strengths
1. The paper removes the assumption in the previous related paper that the sender knows everything about the environment. Given their result that it is impossible to achieve sublinear regret while being persuasive at every episode with high probability, it's reasonable to turn to the goal that the violation of persuasiveness is sublinear in T. Overall, the question studied by this paper is well motivated and their desiderata are reasonable.

2. The paper provides a solid theoretical analysis. The authors achieve tight results for the partial feedback setting.

### Weaknesses
1. The setting of this paper is similar to the setting of [1]. To be specific, in this paper, the authors consider MDP with persuasiveness as the stochastic long-term constraint because the receiver's reward function is drawn from some distribution. In [1], the authors consider MDP with constraint matrices, which can be stochastic or adversarial. As a consequence, these two papers share a similar upper-bound technique that maintains estimators and confidence bounds of the environment and uses them to update the occupancy measure. The similarity makes me cast doubt on the novelty and technical contribution of this paper. I think the authors should clarify the difference between these two papers. The core issue is that both approaches rely on maintaining confidence bounds on the environment parameters and using these to construct a feasible set for optimization. While the specific constraints differ (persuasiveness vs. general constraints), the high-level approach seems very similar, raising questions about the incremental contribution of the proposed method. The paper should more clearly articulate how the specific structure of the persuasiveness constraint necessitates a novel technical approach beyond the existing techniques for constrained MDPs.

2. While the result is tight in the partial feedback setting, it is not shown in the paper whether the result is tight in the full feedback setting. I think the lower bound in the full feedback setting should be included for the completeness of this paper. Without a corresponding lower bound, it is difficult to assess the optimality of the proposed algorithm in the full feedback scenario. The absence of this result leaves a gap in the theoretical analysis and makes it unclear whether further improvements are possible.

3. For the proposed algorithm: (1)the computational complexity can be another issue that may prevent MPPs from being used in practice because large linear programming needs to be solved at every round; (2) the intuition of the algorithms should be explained more for better understanding. The paper should provide a more detailed discussion of the computational cost of solving the linear programs, especially in relation to the size of the state and action spaces. Furthermore, the algorithms are presented with limited explanation of the underlying intuition. A more detailed explanation of the design choices and the rationale behind the specific update rules would greatly enhance the accessibility and understanding of the proposed approach. For instance, a step-by-step walkthrough of how the confidence bounds are used to update the occupancy measure would be beneficial.

4. There is a typo on page 8:  "every triple \si" not "si".

### Questions
Is the regret bound of the algorithm in the full feedback setting tight?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In Bayesian persuasion, a sender sends information to a receiver with the goal of persuading them to take particular actions, while the receiver is aware of the sender’s incentive and has their own goals, and thus may deviate from the recommended action. Typically one designs a “persuasive” communication scheme, meaning it is always in the receiver’s best interest to follow the recommendation. Usually, this occurs in a single-round setting.

The present submission studies Markov Persuasion Processes (MPPs), which essentially combine MDPs with Bayesian persuasion. Specifically, the sender instead interacts with T different receivers sequentially, and actions on previous time steps affect the current state. This paper assumes the sender starts with no information and must learn everything on the fly (transition function, sender reward function, receiver reward function). The goal is then regret which is sublinear in T. This paper also requires the cumulative violation of the persuasiveness constraint to be sublinear in T.

The authors provide algorithms which achieve both of those goals (regret sublinear in T and persuasiveness violation sublinear in T), in both a “full feedback” setting and a “partial feedback” setting. They also provide a matching lower bound.

### Strengths
I think this is a nice paper. It’s well-written, the model seems mostly reasonable, the results are satisfying, and there are some interesting technical ideas. Without considering prior work, I would probably lean towards acceptance.

### Weaknesses
Unfortunately, I have some serious concerns about the lack of novelty when compared to [1], which previously studied no-regret learning in MPPs. From my reading, the authors articulate four differences between the present submission and [1]:

A. [1] assumed that the receiver’s reward function is known to the sender, while the present submission does not. This is the primary difference emphasized by the authors.

B. [1] assumed rewards are deterministic, while the present submission allows rewards to be stochastic

C. [1] assumed the reward function is fixed, while the reward function to vary across episodes, but assumes that the reward function for each episode is sampled iid

D. [1] assumed that receivers know everything about the environment in order to compute a best-response, while the present submission does not.

I commend the authors for providing a clear discussion of the technical differences between their work and [1]; this made my job as a reviewer much easier. Unfortunately, none of (A) - (D) seem especially significant to me. I discuss each in turn.

_(A) and (B)_. I argue that typically in RL theory, most of the technical difficulty comes from learning the transition function, and knowing the reward function doesn’t help much. The distinction between stochastic and deterministic rewards is also typically not significant. To semi-formalize this, I argue below that for {0,1} rewards, any no-regret algorithm for MDPs with known deterministic rewards can also solve MDPs with unknown stochastic rewards. This reduction breaks down for more general rewards than {0,1}, but I think the conceptual takeaway still holds: that most of the difficulty comes from learning the transition function. Also note that {0,1} rewards are sufficient for most RL lower bounds [2]. Beyond the technical connections, [1] also provide a conceptual justification for known rewards: “The receiver’s utility is known to the sender because the pricing rules are usually transparent, some are even set by the platform. For example, a rider-sharing platform usually sets per hour or mile payment rules for the drivers.” I think this is a reasonable argument, although it certainly doesn’t apply to all applications.

_(C)_. I would guess that since the reward function for each episode is iid, their average quickly converges to the mean, such that this does not add much difficulty. However, I may be wrong, and I could imagine this component adding some novelty to the paper.

_(D)_. If I understand correctly, the present submission instead assumes that the receiver always plays the action recommended by the sender and does not play a best response at all. The authors then show that the cumulative violation of the persuasiveness constraint is sublinear in T. I think this approach is reasonable: as the authors note, it is impossible to be immediately persuasive when the sender starts out with no information about the receiver. However, I don’t think this is a strength over [1]: this model seems easier in some ways and harder in some ways than [1]’s assumption of perfect best response.

Beyond the comparison with [1], I also have some concerns about the model. I’m unsure whether there exist natural applications which both involve Bayesian persuasion and MDP-style dynamics. The authors cite movie recommender systems as a motivating example, but what do the states represent? Receivers would be users, right? If I understand correctly, the sender interacts with a new receiver on every time step, so how does one user affect the state of a different user? It also seems like users’ incentives are pretty aligned with the recommendation system (they want to watch movies that they like), so it seems unlikely for users to engage in reasoning like “the system is recommending me movie A which isn’t what I want to watch but it does give me information about which movie I should actually watch”. Even if the authors agree with everything above (and I am open to disagreement), I don’t think the paper has zero novelty, but I think the novelty is too low for ICLR.

### Questions
Do you agree with my comparison with [1]? For (A) and (B), do you agree with my reduction? For (C), could you elaborate on whether you believe this difference is significant? Is my understanding of (D) correct?

I would also be curious to hear if the authors have any response to my concerns about the model.

### Soundness
3

### Presentation
3

### Contribution
1
