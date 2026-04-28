# Steering No-Regret Learners to Optimal Equilibria

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 6, 5, 8

## Abstract
We consider the problem of steering no-regret-learning agents to play desirable equilibria via nonnegative payments. We show that steering is impossible if the total budget (across iterations) is finite, both in normal- and extensive-form games. However, vanishing average payments are compatible with steering. When players' full strategies are observed at each timestep, constant per-iteration payments permit steering. When only trajectories through the game tree are observable, steering is impossible with constant per-iteration payments in general extensive-form games, but possible in normal-form games or if the maximum per-iteration payment may grow with time, maintaining vanishing average payments. We supplement our theoretical positive results with experiments highlighting the efficacy of steering in large games, and show how our framework relates to optimal mechanism design and information design.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explores the problem of steering no-regret-learning agents to play desirable equilibria in games, using nonnegative payments. The authors present a framework for achieving this goal, and provide theoretical and experimental evidence to support its effectiveness. They also discuss the relationship between this framework and other areas of game theory, such as mechanism design and information design.

### Strengths
The authors study an interesting question that might have interesting potential applications in mechanism design (and in my opinion) in federated learning.

### Weaknesses
I find the paper to be inaccessible and lack precision at times (for instance, a central notion to the paper such as optimal equilibrium is not well-defined—is it one that is Pareto-optimal or that maximizes some notion of welfare?). The experiments seem also unrelated to the theoretical results (Pure Nash vs. Correlated). The definition of the steering problem in terms of pure Nash equilibria is also odd, since pure Nash equilibria are not guaranteed to exist.

Comments and questions:

Page 2: full feedback is not defined

Is this problem solved 

Section 3, regarding regret definition and repeated play. Are the time iterations, the time iterations of some online learning algorithm or is this the steps of an episode? I think as is standard in the literature, the author are considering repeated-play settings but (although this can be understood clearly in the learning literature, I do not think this is clear in this setting). A description of the learning setting would be appreciated.

What is the meaning of the directness gap? I cannot read the math as the description given, an explanation would be appreciated.

The steering problem is defined pure strategy Nash equilibria, when are pure strategy Nash equilibria guaranteed to exist in extensive form and normal-form games? How much of the theory provided by the authors apply to mixed Nash equilibria?

### Questions
Comments and questions:

Page 2: full feedback is not defined

Is this problem solved 

Section 3, regarding regret definition and repeated play. Are the time iterations, the time iterations of some online learning algorithm or is this the steps of an episode? I think as is standard in the literature, the author are considering repeated-play settings but (although this can be understood clearly in the learning literature, I do not think this is clear in this setting). A description of the learning setting would be appreciated.


What is the meaning of the directness gap? I cannot read the math as the description given, an explanation would be appreciated.

The steering problem is defined pure strategy Nash equilibria, when are pure strategy Nash equilibria guaranteed to exist in extensive form and normal-form games? How much of the theory provided by the authors apply to mixed Nash equilibria?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper targets the following problem can we steer no-regret dynamics towards optimal equilibria. The paper considers both settings of normal form and extensive form games as well as full feedback versus bandit feedback. The results can be roughly organized into two categories. Firstly, there are results targeting pure Nash equilibria. In this case the paper provides a number of results showing that such targeting is possible given sublinear total of payments. They also provide an example where finite amount of payments do not suffice for a specific sequence of no-regret play in a 2x2 game. Secondly, there are results targeting mixed NE, and different notions of CE. There is a significant departure in what the paper interprets as steering equilibria. Instead of considering standard no-regret algorithms playing e.g. Follow-the-Regularized-Leader playing the original game, they expand the setting to add a new "action" to each algorithm. The new  actions is not an action in the original game but effectively implements the policy "I will play what my mediator tells me to do" which mediator can e.g. solve for an optimal correlated equilibrium. This technique effectively allows the paper to leverages recent computational  reductions by (Zhang et al. (2023) and reduce the mixed equilibrium problem to a pure equilibrium problem.

### Strengths
The paper targets a rather interesting problem of how to steer no-regret learning algorithms to implement equilibria. It connects interesting areas in game theory, online learning and mechanism design. It presents a plethora of theoretical results in a wide range of different settings and solution concepts. The mathematical parts of the paper are generally well articulated. The authors show good technical grasp of the area and leverage expertly recent results. The paper has also shows some experiments to complement the theory.

### Weaknesses
I have two different criticisms for the paper. One for the pure Nash results and one for the rest of the mixed solution concepts.

1. For the case of non-pure Nash equilibria, if I am not mistaken, the paper does not solve the problem that is advertised in the title/abstract/intro. Specifically, from the first paragraph of the intro: 

Any student of game theory learns that games can have multiple equilibria of different quality—for
example, in terms of social welfare (Figure 1). How can a mediator—a benevolent third party—steer
players toward an optimal one? In this paper, we consider the problem of using a mediator, who
can dispense nonnegative payments to players, to guide players to a better collective outcome.

That is *not* what the paper is doing. The mediator in the case of mixed eq is a much more powerful entity that can actually broadcast advice to all players. Furthermore, the players are not playing any recoginzable no-regret algorithm but learning with advice algorithms,  which have a special option (ignore the actual algorithm and follow centralized advice according to a pre-configured scheme that allows for global instantaneous broadcast of signals that are unambiguously interpreted by all users and acted upon). This is not steering no-regret algorithms but a different class of algorithms altogether where agents learn in the presence of a broadcasting device. The current paper mentions in passing in the introduction some of these papers by Balcan et al (see also [1] for a more recent paper) but they fail to mention that these settings work with a more realistic broadcasting device, which only reaches a small random fraction of all agents (e.g. 1%) instead of all. More importantly, I would have expected that words such as public service advertising, learning with centralized advice, global information, etc. would play central role in the description of the approach. This is a critical part of the model and important difference between the case of pure and mixed eq. 
To be clear, what is being done is still interesting but it is significantly easier to achieve than merely using payoffs to steer the dynamics.

2. For the case of pure Nash equilibria, it is not clear to me that the problem is hard to begin with. The paper provides a lower bound where a simple game along with a specific type of very unnatural no-regret behavior can be hard to steer. Following results from e.g. [2-4], pure/strict Nash (e.g. like in Stag Hunt games explored in the paper) are locally asymptotically stable for effectively all no-regret algorithms and in fact arguably for all reasonable game dynamics. So here is how to informally stabilize all of them with a finite amount of money. Pad the target strategies with enough money at an initial phase of the algorithm. With a finite excess payoff any reasonable aggregate payoff based dynamics (not even no-regret) after some finite amount of investment will be in the attractor. This is a stronger convergence result since it is actually even guarantees last-iterate convergence (and it does so with a finite amount of money).

My question is the following: Why should we care enough for totally non-meaningful no-regret behaviors that do not capture any realistic algorithm either from an optimization or a behavioral point of view to be willing to accept paying an infinite amount of money when finite amount should suffice for all reasonable dynamics? 

You also have an experiment with Exp3 where clearly a finite amount of money suffices to select the optimal equilibrium. Can you create a negative example where you would need unbounded money for Exp3? If not, then doesn't this show that the $T^{alpha}$  unbounded payoffs are too loose in comparison to real world lower bounds?

### Questions
Please see my questions above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the problem of guiding no-regret-learning agents toward desirable equilibria using nonnegative payments. The authors first show that achieving vanishing average payments allows for steering in scenarios where complete player strategies are observable. However, steering is impossible with a finite budget across all iterations. In cases where only game tree trajectories are observable, the feasibility of steering varies, being possible in normal-form games or with growing per-iteration payments, but generally impossible in extensive-form games with constant per-iteration payments. The paper supplements its theoretical findings with experimental validation, demonstrating the efficacy of steering in large games.

### Strengths
On the positive side, I found the paper to be well-written, and if you take the model as given, the paper gives a fairly satisfying and complete first investigation – the questions asked are exactly the ones I would hope are answered first.

### Weaknesses
I have a major concern regarding the motivation behind this paper, particularly with respect to the assumption that agents willingly accept being directed. A key question arises when these agents are required to continue their interactions for extended rounds after being steered towards equilibrium – should compensation be provided once they reach this equilibrium? While the paper mentions that a small constant, P (P <= 8), is sufficient to guide them to the exact equilibrium within a finite number of iterations, it overlooks the potential utility loss (because of being steered into a different equilibrium) experienced by agents after this steering process. Intuitively, it seems reasonable that they should also receive compensation to offset this particular loss. Moreover, an alternative approach could be to simplify the model into a single step, instructing agents to directly adopt the ideal equilibrium. In this case, the mediator could provide one-time compensation equal to the total utility difference experienced under an alternative equilibrium.

Specifically, regarding the assumption that followers will consistently play a no-regret strategy in response to the leader's queries, especially when they are aware of the steering process towards equilibrium. Steering mechanisms have the potential to influence agents' decisions and behaviors, raising questions about the potential introduction of bias or preferential treatment for certain groups of agents. For instance, in the design of payment schemes, concerns about fairness may emerge. It is crucial for the paper to elaborate on the validity of this behavior model and provide justifications into the application domains where such assumptions hold.

From a technical perspective, I found it challenging to understand how the algorithms can be effectively applied to mixed-strategy equilibria through a mediator-augmented game. Specifically, when dealing with pure strategies, solving equation (2) seems feasible. However, when considering mixed strategies, X_i transforms into an infinite set, and solving equation (2) would necessitate the optimization of a non-convex problem.

### Questions
The concept of a mediator-augmented game reminds me of a paper by Deng, Yuan, Jon Schneider, and Balasubramanian Sivan titled "Strategizing against no-regret learners." This paper, which addresses similar problems involving strategies against no-regret learners, was cited in your work but not extensively discussed. In a mediator-augmented game, the mediator essentially takes on the role of the leader who strategizes against the no-regret learner. I am curious whether you can provide a detailed explanation of the difference between your models and results.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers a setting where there is a mediator whose goal is to direct (i.e. steer) the learning agents to desirable equilibria by paying the agents, thus affecting the learning agents' payoff. The authors show that if the total payment is upper bounded by a constant then it is not possible to steer the agents. However, it is possible when the per-iteration payments are o(1). In particular, in the setting where the agents use an algorithm that has sqrt{T} regret, they show that in the full information setting or normal setting, the per-iteration payment is O(T^{-1/4}) and, in the bandit setting for extensive-form games, the per-iteration payment is O(T^{-1/8}). The authors study both the full-information setting and the bandit setting.

To prove their results, one idea is to pay the agents so that playing a Nash equilibrium is a dominant strategy. However, the technical difficulty here is that we want to ensure that the per-iteration payment goes to 0 as t tends to infinity. The authors show how to do this by designing a payment function with essentially three components. The first component is to subsidize the agents when the other agents are not bidding the equilibrium. An important aspect of this is that when the agents are in equilibrium, this component should vanish. The second is a reward which incentives the agents to bid the equilibrium. And the last component is just to ensure the payments are non-negative.

### Strengths
The problem is quite original and is very interesting. The results are interesting and I believe will be of interest to researchers working in the intersection of AGT and learning. In particular, there is a large body of work on understanding dynamics of games and this paper should fit right in.

In addition, the writing is clear and the techniques seem quite sophisticated. I enjoyed reading the paper and appreciate that it is a novel problem.

### Weaknesses
No weaknesses to discuss from my end.

### Questions
p. 1: Maybe clarify what is meant by bounded regret. Is it constant regret per-iteration? Vanishing regret?
Algorithm 5.1: Do the sandboxing payments have the same property in the normal form case where having those payments ensures that d_i is a dominant strategy?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
