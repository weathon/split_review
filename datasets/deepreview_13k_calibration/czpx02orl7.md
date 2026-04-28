# Learning Abstract World Models for Value-preserving Planning with Options

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 8, 3

## Abstract
General-purpose agents require fine-grained controls and rich sensory inputs to perform a wide range of tasks. However, this complexity often leads to intractable decision-making. Traditionally, agents are provided with task-specific action  and observation spaces to mitigate this challenge, but this reduces autonomy. 
Instead, agents must be capable of building state-action spaces at the correct abstraction level from their sensorimotor experiences. We leverage the structure of a given set of temporally-extended actions to learn abstract Markov decision processes (MDPs) that operate at a higher level of temporal and state granularity. We characterize state abstractions necessary to ensure that planning with these skills, by simulating trajectories in the abstract MDP, results in policies with bounded value loss in the original MDP.
We evaluate our approach in goal-based navigation environments that require continuous abstract states to plan successfully and show that abstract model learning improves the sample efficiency of planning and learning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a grounded abstract model formulation with a dynamic preserving abstraction. This abstract state representation (and model) guarantees not only accurate future predictions but also the bounded values in the abstracted rollouts. This paper then provides its implementation using contrastive learning to maximize mutual information between the future state, and the current abstract state and option. The results show that training DDQN in imagination using the abstract model improves the sample efficiency.

### Strengths
* The paper proposes a solid foundation of the abstract model that preserves dynamics and values.

* The paper is well written.

* The visualization in Figure 3 clearly shows that the abstract state representations focus on important features in the original observation space.

### Weaknesses
 * The main focus of the paper is to show the efficiency of planning and learning when using the proposed abstract MDP. The experiments in the paper are a bit simple to showcase the benefits of the abstract model for planning. It would be stronger if the experiment was done in more complex environments with much longer-horizon tasks, such as AntMaze experiments (Hafner 2022) or robotic manipulation tasks [a]. Specifically, the current environments, while demonstrating the core idea, do not fully capture the potential of the method in scenarios requiring intricate planning over extended time horizons. The AntMaze environment, for instance, would necessitate the model to learn and utilize a more complex understanding of spatial relationships and long-term dependencies, which would be a more compelling demonstration of the abstract model's capabilities.

* Similarly, the comparisons in Figure 5 are essentially between model-free RL (ground) and model-based RL (abstract), which does not seem fair. It might be fair to compare the proposed method with other model-based RL approaches, such as Dreamer and TD-MPC. The current comparison setup does not isolate the benefits of the proposed abstraction technique from the general advantages of model-based RL. A more rigorous evaluation would involve comparing against state-of-the-art model-based methods that also learn dynamics models and use them for planning. This would provide a clearer picture of the unique contributions of the proposed approach.

* Exhaustive comparisons to the alternatives to the dynamics preserving abstraction would be interesting, such as bisimulation. The paper could benefit from a more detailed discussion and empirical comparison with bisimulation-based abstractions. This would help to clarify the specific advantages and disadvantages of the proposed dynamics-preserving approach compared to existing methods. For example, it would be insightful to see how the two methods perform in scenarios with varying levels of stochasticity or partial observability.

* Some highly relevant works on temporally-extended models [a,b] are missing in the paper. Proper comparisons to these approaches are necessary. The absence of comparisons with temporally-extended models limits the paper's ability to contextualize its contribution within the broader landscape of hierarchical reinforcement learning. These methods often use options or skills to achieve temporally extended actions, and a comparison would highlight the unique aspects of the proposed approach.

### Questions
Please address the weaknesses mentioned above.


### Minor questions and suggestions

* Figure 1 may want to explain why abstract state representations and options are helpful for planning and learning. However, Figure 1 does not seem to help understand the paper. To understand this figure, we first need to know about options and abstract state representations, and how they simplify planning.

* In Section 4.2, it is unclear whether $\mathcal{L}^T_{\theta, \phi}$ is used to update $f_\phi$ or not.

* For multi-goal experiments in the paper, using the same amount of environment steps for the abstract planning and the ground baseline would make it easier to understand how better or worse a method is.

* The appendix could be included in the main paper for easier navigation.

* What is the difference between Figure 7 and 8?

* Training the abstract planning method longer in Figure 7 and 8 would be helpful to see how it learns. Using different x-scales for two methods is okay but it would be better to have the same scale.

* Many minor typos in the paper.


---

Thank you for author responses. I would love to see comparisons to Dreamer-like baselines, but couldn't find the results by the end of the rebuttal period. Thus, I keep my rating, borderline reject.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a method for enabling general-purpose agents to efficiently handle complex tasks by constructing abstract models based on temporally-extended actions. These models facilitate more efficient planning and learning and are characterized using principled conditions. The approach provides empirical evidence of improved sample efficiency in goal-based navigation tasks and offers theoretical support for information maximization strategies in abstract state representation learning.
The authors claim that they introduced a method for creating abstract world models that empower agents to plan effectively for goal-oriented tasks. The key idea is to allow agents to construct reusable abstract models for planning with specific skills. This is achieved by characterizing the state abstraction that ensures planning without any loss in simulation, meaning that planning with the learned abstract model can generate policies for the real world. The paper also provides theoretical support for the use of information maximization as a reliable strategy for learning abstract state representations.

### Strengths
- Good overview of the related work.
- Good description of motivations and intuitions. 
- proper choice of environment settings.

### Weaknesses
Major:
- Some measures are used without definition,
- It seems that there exists a lot of inaccuracies and impreciseness in the theories and definitions. See all questions!

minor:
- typos: 
last paragraph of the introduction "the *agents* needs", definition 3.5 "$s_{o}$" must be "$s_0$"
- writing: 
Define the abbreviations before using them, e.g. "PDDL", "VAE"

There is a chance that I have not fully understood what this paper is trying to present.

### Questions
1- What is $P(s'|s,o)$ used in the paragraph right after definition 3.1?

2- An option $o$ is defined, and then you mention $T(s'|s,o)$ to define the transition probability of taking option $o$ in $s$? $T$ earlier was defined on action space $A$. How is it applied on options without showing the relationship of $I_o$ and $\beta_o$ with $s$ and $s'$ under option policy $\pi_o$?

3-the paper has defined "$\bar {\gamma} = \gamma ^{\tau (s,o)}$ is the abstract discount factor, $\tau: Z \times O \rightarrow [0,\infty)$, which consists of contradictory phrases. How is ${\tau (s,o)}$ but defined as a function of abstract variables $Z$ instead of $S$? Not clear what $\tau$ is. If based on definition 3.1, it is the option's execution time starting from $s$ taking option $o$, it is not clear how in definition 3.2 it becomes a map from $Z$ and $O$ to a non-negative real.

4- What does definition 3.4 mean? $ \Pi = {\pi \in \Pi : \pi(·|s) = \pi (·|z) \forall s \in z}$ says the probability of taking actions/options in $s$ should be equivalent to the probability of taking actions/options in abstract states. Transitions of taking actions in states might take you to another state $s'$ inside the similar abstract state $z$. How can the policies used for both abstract states and states be equivalent? Unless you are just discretizing the continuous state spaces based on the optimal policies that are already given. Lots of interchangeable usage of symbols here. Not precise and is hard to follow.

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents an approach for learning dynamics preventing abstractions for sensorimotor observation space. Given a set of high-level skills and the learned dynamics preserving abstractions, the paper claims to develop an approach for planning for a solution. 

The approach is evaluated in two test domains where the paper shows the visualization of the learned abstractions.

### Strengths
- For the most part of the paper, it is extremely well written. Given the wide use of embodied AI systems and robots, an approach that generates plannable abstractions for high-dimensional sensor input is extremely important. 

- The paper nicely motivates the problem.

### Weaknesses
While the paper in general is nicely written, it has a few limitations: 

- The paper advocates learning a continuous abstract  representation instead of a symbolic abstractions. However, it does not provide any reasons to that. Why are continuous abstractions more desirable than symbolic abstractions? 

- Sec 4.1 is unclear. The notation for MI is a bit unclear. It needs to be made more clear. Sec 4.1 requires a re-writing including more explanation for the equation.

### Questions
I have two important questions: 

- How is the dynamics preserving abstraction defined in Def. 3.6 different from the Markovian abstractions defined in [Srivastava et al. 2016]? 

- Can you discuss the differences between the presented approach and [Allen et al. 2021] 

Reference 

Allen, Cameron, et al. "Learning markov state abstractions for deep reinforcement learning." Advances in Neural Information Processing Systems 34 (2021): 8229-8241.

Srivastava, Siddharth, Stuart Russell, and Alessandro Pinto. "Metaphysics of planning domain descriptions." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 30. No. 1. 2016.

### Soundness
3 good

### Presentation
3 good

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
This paper proposes an algorithm for learning MDP state abstractions that preserve information needed for planning (namely, the values of states). A major differentiator from symbolic approaches is the idea that these state abstractions should be continuous rather than discrete. The key assumption is that you are given a set of options and a dataset obtained by rolling them out. Experiments are conducted in a few simple domains: pinball and antmaze, and demonstrate that the learned abstractions are sensible.

### Strengths
The paper addresses an important topic (abstraction learning) and I appreciate the theoretically motivated algorithms. This line of work is of great interest to many attendees of ICLR. I also appreciate that the authors were clear about wanting continuous representations right off-the-bat. The math is also correct as far as I was able to tell, though I didn't check the proofs in the appendix in careful detail.

### Weaknesses
Unfortunately, I recommend rejection for this paper due to 4 major reasons: 1) unconvincing experiments, 2) missing key citations to related work, 3) issues in technical details, and 4) unclear motivation.

1) unconvincing experiments

The experiments in this paper are very basic and only serve as a simple proof-of-concept that the learned abstractions are somewhat useful. To really scale up the experiments to the level expected for a conference paper, I would expect to see evidence that the learned abstractions are useful in more hierarchical domains (e.g., classic domains from the options literature like keys and doors). In such domains, we could test whether the value-preserving property holds empirically, by comparing the values from planning under the abstract model to the (ground truth) values from planning under the true model. The current experiments do not demonstrate this, and it's unclear how the learned abstractions would perform in more complex scenarios with longer planning horizons.

Additionally, I would like to see comparisons to many more RL algorithms, especially hierarchical ones like HIRO (https://arxiv.org/abs/1805.08296), HVF (https://arxiv.org/abs/1909.05829), and Director (https://arxiv.org/abs/2206.04114). This is because at the end of the day, the authors are proposing to learn a state encoder $\phi$, and despite all the theory that has gone into their algorithm, the question that must be answered is whether this $\phi$ outperforms the encoders learned by all these other SOTA hierarchical RL algorithms. The paper lacks a clear benchmark against these methods, making it difficult to assess the practical significance of the proposed approach.

2) missing key citations to related work

The authors are missing several key citations, the most important of which is the line of work by David Abel, such as "Near optimal behavior via approximate state abstraction" (https://proceedings.mlr.press/v48/abel16.html) and "Value preserving state-action abstractions" (https://proceedings.mlr.press/v108/abel20a/abel20a.pdf). Those papers have very similar theory to what appears in this one, and so the novelty of the proposed approach is unclear. There are also less-famous but still important-to-cite papers from other authors, like "Abstract value iteration for hierarchical reinforcement learning" (https://proceedings.mlr.press/v130/jothimurugan21a/jothimurugan21a.pdf) and "Deciding what to model: Value-equivalent sampling for reinforcement learning" (https://proceedings.neurips.cc/paper_files/paper/2022/hash/3b18d368150474ac6fc9bb665d3eb3da-Abstract-Conference.html). It is important for the authors to contextualize the contributions of this paper against all these related works. The absence of these citations makes it difficult to understand the paper's place within the existing literature and raises concerns about the authors' awareness of relevant prior work.

3) issues in technical details

The authors say in Section 3.2 that when B = \bar{B}, "then simulating a trajectory in the abstract model is the same as in the ground model". But I don't think this is true, because we need the rewards to match between the two trajectories too, and $B_t$ says nothing about rewards, only dynamics. The authors go on to say: "Therefore, planning in the abstract model is accurate, in the sense, that the value of an abstract state z computed in the abstract model is the same as the one would get from trajectories from the ground MDP for the abstraction operator G." Again, I think this is wrong because it ignores the abstract reward function, which could be arbitrarily different from the ground one. In fact, in the proof of corollary 3.8, the authors assume $E_{s \sim G(\cdot \mid z)}[R(s, o)] = \bar{R}(z, o)$, and it's only _under this assumption_ that the claims hold. But combining this assumption on reward function with Definition 3.6 ends us back up at the bisimulation conditions, and then it's not clear what the contributions of this paper are. The paper does not adequately address the critical role of the reward function in preserving value equivalence between the ground and abstract models.
 
As a separate point, the second term in the mutual information expression of Section 4.2, $MI(S'; Z, A)$, seems very extreme! It is saying that you have to be able to predict the entire ground next state from the current abstract state and action. Doesn't this means the abstraction can't lose any information? This seems like an important technical limitation of the approach. This constraint appears overly restrictive and may limit the ability of the method to learn meaningful abstractions in complex environments.

4) unclear motivation

The authors often state that a discrete abstract state space is bad, when pointing to work on symbolic abstraction learning (e.g., PDDL). But it's not clear why this is really bad. The authors say discrete abstract states are "not applicable when planning with the available high-level actions requires a continuous state representation", but this doesn't make sense to me, as the options have to act in the ground environment states, not in the abstract state space, and so the options could be defined with respect to either a discrete or a continuous abstract state space. Furthermore, it can be much easier to plan in a discrete abstraction (e.g., using powerful symbolic planners). The paper does not provide a compelling argument for why a continuous abstraction is inherently superior to a discrete one, especially given the potential advantages of discrete abstractions for planning. The motivation for focusing solely on continuous abstractions remains unclear and unconvincing.

I believe a fruitful research direction would be to compare the abstractions learned by a symbolic approach against the abstractions learned by a continuous approach (like the authors').

### Questions
Questions:
* Not much is said about the dataset $\mathcal{D}$, but intuitively, it has to be "good" in order for the learned state abstraction to be reasonable. In particular, the agent must see all the options being executed in a variety of settings, and obtain good coverage over the state-action space. Are there any concrete statements we can make about what properties we need this dataset to have?
* "we must build a model of its effect" Do you mean to say "of the effect of each option"?
* "with mean value equal to that by planning with the original MDP" What is the mean over?
* Why did we switch from using O (denoting the option set) everywhere to using A throughout Section 4? Shouldn't we continue to use O, unless I am misunderstanding something?
* Section 4.3: Why should there be any cost/reward associated with executing skills? Shouldn't a sparse reward for reaching the goal be enough?
* Eq 2: What are the "I" random variables inside the mutual information expression referring to?

Minor edits:
* "make the same decision" To clarify, we just need that the policy maps all states in z to the same action distribution. A stochastic policy isn't really committing to a "decision" about what action to take.
* "Abstractions alleviate this tension: action abstractions enable agents to plan at larger temporal scales and state abstractions reduce the complexity of learning and planning" I would say that both of them do both of these. Action abstractions certainly reduce the complexity of planning, which is typically exponential in the branching factor.
* "learns a further abstraction" --> "learn a further abstraction"
* "otherwise it is referred as learning" I would say "policy learning" to distinguish from other things you might learn
* "when it is the given position" --> "when it is in the given position"
* "referred as learning" --> "referred to as learning"
* "results a bounded value loss" --> "results in a bounded value loss"
* In definition 3.5, the authors use $s_o$ in a few places where they mean $s_0$.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
