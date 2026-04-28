# Maximizing Benefits under Harm Constraints: A Generalized Linear Contextual Bandit Approach

- Decision: Reject
- Scores: 3, 5, 6, 3

## Abstract
In many contextual sequential decision-making scenarios, such as dose-finding clinical trials for new drugs or personalized news article recommendation systems in social media, each action can simultaneously carry both benefits and potential harm. This could manifest as efficacy versus side effects in clinical trials, or increased user engagement versus the risk of radicalization and psychological distress in news recommendation.
These multifaceted situations can be modeled using the multi-armed bandit (MAB) framework. Given the intricate balance of positive and negative outcomes in these contexts, there is a compelling need to develop methods which can maximize benefits while limiting harm within the MAB framework. This paper aims to address this gap. The primary contributions of this paper are two-fold:
(i) We propose a novel contextual MAB model with the objective of optimizing reward potential while maintaining certain harm constraints. In this model both rewards and harm are governed by a generalized linear model with coefficients that vary based on the contextual variables. This flexibility allows the model to be broadly applicable for a wide range of scenarios.
(ii) Building on our proposed generalized linear contextual MAB model, we develop an $\epsilon$-greedy-based policy. This policy is designed to strike an effective balance between the dual objectives of exploration-exploitation to achieve the desired trade-off between benefit and harm. We demonstrate that this policy achieves a sublinear $\mathcal{O}(\sqrt{T\log T})$ regret.
Extensive experimental results are presented to support our theoretical analyses and validate the effectiveness of our proposed model and policy.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper tackles the problem of multi-armed bandit(MAB) when the bandit's arms provide feedback as *reward* (positive effect) and *harm* (negative effect). The work uses a generalized linear model with contextual variables to model the rewards and harm and proposes a novel $\epsilon$-greedy algorithm to tackle the proposed MAB setup. The algorithm enjoys sublinear regret and is supplemented with extensive experimental evidence to support the claim.

### Strengths
The problem tackled in the paper is **very** significant as most of the applications witnessed in multi-armed bandits have an arm model where harm is witnessed but often neglected. This is an important direction for a sustainable future (for e.g. overconsumption is often associated with adverse effects)

The paper provides a novel method for modeling reward and harm in multi-armed bandits as well as a sublinear regret algorithm that can tackle the problem. The authors provide simulation evidence for the prowess of their method. They provide an explanation for the assumptions taken while proving the theorem.

### Weaknesses
I will split this answer into parts : 

1) **Modelling choices**:  There is an opaqueness in the modeling choices at various places in the paper. 

For e.g. 
* The choice of $u_{i}$ for arms -- why are they scalar values, what is the physical interpretation, and why are they increasing across arms? Does that mean that arm $1$ and arm $K$ are best and worst or vice versa?

* choice of optimization problem taken in equation (1). Is there a motivation as to why equation (1) is chosen over other forms? Does the following work?
$$ \min \{\arg\max_k\{q_{k, t}^2 -\lambda(p_{k, t} -\theta)^2_+\}\} $$

* why is equation (5) linear in $u_k$ but equation (8) quadratic? Is it coming from some existing models?

These are some examples, I am not listing all of them

2) **Missing definitions**: Certain places seem to have missing definitions. For e.g.
* equation (4), (5), (7), (8) -- what are the functions p, q,g,h,$\zeta, \xi$? why are these equations the way they are?

3) **Missing lower bound**: There is no explanation or intuition as to why the upper bounds obtained in the paper could be tight. Would be good to have a quantification as to the suboptimality of the upper bounds in terms of the dimensional dependence. 

4) **Algorithm ambiguity**: There are some points not covered when discussion of the algorithm happens:

* The algorithm is not really $\epsilon$-greedy. Maybe change the name or reference to $\epsilon_t$-greedy? Since $\epsilon$-greedy would give the impression of permanent forced exploration based on static $\epsilon$ which is not the case here. 

* Why is forced exploration (through $\epsilon$-greedy methodology) required? Is it because of the lack of closed-form expression for confidence width?

* The choice of forced exploration parameter $\epsilon_t$ is taken to be $\propto \frac{\log T}{T}$ which is typically for the case of vanilla bandits as the confidence width there is also proportional to a similar function in $T$. Why is it the choice here when the confidence width is not discussed?

* There seems to be some mistake in the pseudocode line 3-5 (initialization phase). 

* What is the complexity of each inner loop of the $\epsilon$-greedy algorithm?

5) **Limited experiments**: The experiments seem to be on a much smaller scale with no reasoning on issues taking it to a larger scale or to real-world datasets.

A suggestion would be to rename the algorithm to "
$\epsilon$-greedy" rather than "variable coefficient" (assuming they are the same)

It is completely possible that I might have missed some context while reading and I am open to changing my opinion on the issues listed

### Questions
1) I am a bit confused about the connection with Multiobjective MAB. Can the framework not tackle the setup of reward and harm? What are the exact challenges in extending the MOMAB framework to encompass the current problem?

2) There are a fair number of works on safety-constrained MABs, but I see limited mentions of them (E.g. some works focus on a safety budget). Are they very different from the current work and hence not mentioned?

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the problem of contextual-based online decision making with harmful effects. After parameterizing both the benefit and the harm effect, the authors propose an epsilon-Greedy algorithm that achieves regret of $\tilde{O}(\sqrt{T})$.

### Strengths
According to Table 1, this paper is the first work to consider feedback involving context features, action features, and underlying parameters in bandit problems. The authors have designed an algorithm that is provably achieving near-optimal regret in this setting.

### Weaknesses
1. The comparison to related work in this paper is not sufficiently clear. In the section comparing this work to previous MOMAB papers, the authors claim that "this paper is the first to consider MOMAB in a contextual setting." However, it seems that this paper revolves around a single-objective problem, as in equation (1) of the paper. This approach doesn't involve the optimization of Pareto regret, which as far as I know is the central topic in prior MOMAB works. Thus I think it is not so fair to make direct comparsion to previous MOMAB works.

2. The assumptions made in this paper is implicitly strong but not sufficiently clear: Theorem 1's results rely on the existence of a positive lower bound for $\lambda_{min}(\Sigma_1)$ and $\lambda_{min}(\Sigma_2)$. Implicitly, these bounds necessitate a diversity assumption concerning the distribution of context and action features. Such a strong assumption significantly simplifies the algorithm design of online decision-making. However, I was unable to locate this assumption clearly spelled out in Assumptions A1 to A3. It would be helpful if the authors could present such strong assumption in a more easily identifiable way.

### Questions
I have no further questions.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors address the setting of Multi-Objective Contextual Multi Armed Bandits.
The motivation for the work is the necessity, in many practical scenarios, to execute actions considering the positive as well as the negative outcome that such actions entail. The main motivating example cited in the paper is that of clinical trials.
The setting addressed by the authors contains information on the context $X_t$, common to all arms and varying at each round, as well as features for each arm, constant across the rounds.
The authors propose a method to tackle such a problem by modelling the mean reward and harm of every arm via two varying coefficient GLMs.
The parameters for such models are to be estimated through MLE.
Finally, after an initial uniform exploration of the arms, an $\epsilon$-greedy algorithm is employed to address the exploration-expolitation trade-off.

### Strengths
The paper, as the authors also acknowledge, places itself in a field where many results have been proposed. Some of the existing results have many aspects in common with the authors' results, although there are some differences.
The paper is well written, the setting is clear and introduced clearly, the notation is clear, as are the results.
In my opinon, the biggest contribution made by the authors is the parametrization of the harm effect on the regret. To the best of my knowledge, no other works have proposed this.
The penalization $\lambda$, together with the threshold $\theta$ could allow practitioners to have more control on how much harm can be "risked" by taking an action.
This, I find to be a good original contribution.
Finally, the authors have provided the code used to generate the experiments. As such, the paper's results should be easily replicable.

### Weaknesses
From my understanding of the work, in a practical situation in which the value of $\lambda$ is high (i.e., the practitioners want to avoid harm at the cost of having a lower benefit) the initialization rounds of the algorithm would still cause some rounds to cause a high harm. As the authors also acknowledge in the conclusions, it would probably be possible to exploit independent samples collected during the execution of the algorithm to obtain a similar result in terms of convergence of the algorithm, while lowering the need for a long initialization phase.
As also noted by the authors, the expensive computation of $\eta$ could become impractical in a real use.
Finally, a minor observation, the graphs representing the average regret and average count of $p > \theta$ could benefit from representing also confidence intervals along with the mean.

### Questions
1) As the authors acknowledge in the conclusions, the balance between benefit and harm could be tackled through Pareto optimality. Turğay et. al. (2018) (https://doi.org/10.48550/arXiv.1803.04015) have proposed a method that exploits Pareto optimality. Although with some differences (Turğay et. al. allow for both conflicting and non-conflicting multiple objectives, but do not use penalizations and thresholds for harm), the two works share some commonalities. If the work of Turğay et. al. were to focus only on conflicting objectives, how would the authors compare the results obtained by the two works?

2) Can prior knowledge of $u_k$ be used to give a prior on reward and harm of the arms? Would it be possible to reduce the number of pulls in the initialization phase for ams which are known as "worse" with respect to $u_k$ while maintaining theorethical guarantees?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies a sequential decision-making problem where the goal is to maximize the reward while containing a harm measure. They propose to model the reward and harm responses as a GLM and use a simple $\epsilon$-greedy algorithm to solve the problem.

### Strengths
1. The paper reads smoothly and is clear in all aspects.

### Weaknesses
1. Significance: the paper considers just an instance of constrained bandits. There are several related works similar to this setting (see Section 2). Even the modeling is a special case of algorithms 9,18 in Table 1 (consider concat$(x_i, u_k) \equiv x_{t,k}$). The $\epsilon$-greedy algorithm is a very basic algorithm for any bandit algorithm. Why not use more optimal algorithms like Thompson sampling or UCB?
2. The experimental results only include synthetic studies and very minimal. Experimenting with real-world public datasets could be insightful for instance for the model misspecification accounts.

### Questions
1. How can a practitioner come up with $\theta$ and $\lambda$? these are hyperparameters of your algorithm and do not directly translate into their goals.
2. Depending on the problem instance, $\kappa$ could be arbitrarily small. Then the regret bounds in Thm. 1 are meaningless. How can you address this issue?

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor
