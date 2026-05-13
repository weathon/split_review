# Tree Search-Based Policy Optimization under Stochastic Execution Delay

- Decision: Accept
- Scores: 5, 6, 6, 6

## Abstract
The standard formulation of Markov decision processes (MDPs) assumes that the agent's decisions are executed immediately.
However, in numerous realistic applications such as robotics or healthcare, actions are performed with a delay whose value can even be stochastic. In this work, we introduce stochastic delayed execution MDPs, a new formalism addressing random delays without resorting to state augmentation. We show that given observed delay values, it is sufficient to perform a policy search in the class of Markov policies in order to reach optimal performance, thus extending the deterministic fixed delay case. Armed with this insight, we devise DEZ, a model-based algorithm that optimizes over the class of Markov policies. DEZ leverages Monte-Carlo tree search similar to its non-delayed variant EfficientZero to accurately infer future states from the action queue. Thus, it handles delayed execution while preserving the sample efficiency of EfficientZero. Through a series of experiments on the Atari suite, we demonstrate that although the previous baseline outperforms the naive method in scenarios with constant delay, it underperforms in the face of stochastic delays. In contrast, our approach significantly outperforms the baselines, for both constant and stochastic delays.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the delayed MDP problem, where stochastic delays are considered during the execution of actions. The authors introduce the concept of Stochastic Delayed Execution MDPs (SED-MDPs) as a solution to address random delays without relying on state augmentation. In particular, they show that optimizing within the set of Markov policies effectively reaches optimal performance.  Empirical validation across Atari games are performed under both constant and stochastic delay settings.

### Strengths
Standard RL assumes immediate availability of information for decision-making, overlooking delays prevalent in various real-world applications.  Existing approaches resort to state augmentation,  which is inefficient in handling exponential computational complexity and dependence on delay values, hindering its scalability to random delays. To address this issue, the authors propose Delayed EfficientZero, a delayed variant of EfficientZero, which is a model-based algorithm that optimizes over the class of Markov policies. The proposed method is able to accurately infer future states from the action queue, and thus handles delayed execution while preserving the sample efficiency of EfficientZero.

The authors establish the insight of optimizing within the set of Markov policies offers a more efficient and scalable solution compared to history-dependent policies. They introduce a model-based algorithm, namely, Delayed EfficientZero, that builds upon EfficientZero. The proposed algorithm yields non-stationary Markov policies, maintaining efficiency and scalability without making assumptions about the delay distribution.

Delayed feedback analysis is a rising topic in RL. Existing methods mainly focus on delays in states / trajectory / rewards. This work instead concerns delays in actions during policy execution, and this setting can be useful in practice.

### Weaknesses
1. This paper adopts the ED-MDP formulation of [1] that sidesteps state augmentation, and extends it to the random delay case. This extension appears to be a relatively direct application of the previous formulation. The authors are expected to explain the technical challenges compared to the constant delay formulation, and be clear about their technical contribution in terms of this formulation. Specifically, the paper should elaborate on how the randomness in delay values impacts the process distribution and how the proposed method addresses the potential variability introduced by this randomness. A more detailed discussion on the theoretical implications of transitioning from a constant to a stochastic delay model would strengthen the paper's contribution.

2. This paper mainly develops based on the ED-MDP formulation of [1], random delay formulation in [2], and EfficientZero [3]. The technical novelty in terms of the algorithm appears to be limited. While the integration of these existing works is acknowledged, the authors should highlight the specific technical challenges encountered when adapting these methods to the stochastic delay setting. For instance, how does the tree search in EfficientZero need to be modified to accommodate the uncertainty in delay? What are the specific modifications made to the action queue management compared to the original EfficientZero algorithm? Providing a more in-depth analysis of these adaptations would better showcase the paper's novelty.

3. While authors provide a thorough experimental study on 15 Atari benchmarks, they only consider small delays by setting $M = \{5, 15, 25\}$. It is desirable to see how the performance can be when delays are large. This is particularly important because the effectiveness of Markov policies might degrade as the delay increases, potentially leading to a more significant performance gap compared to history-dependent policies. Exploring the algorithm's performance under larger delay values, such as M = 50 or 100, would provide a more comprehensive understanding of its limitations and robustness.

### Questions
Under stochastic execution-delay MDPs (SED-MDPs), if at a specific time step (especially at the beginning of the game), there is no action available due to the delay, how does the proposed method execute the policy?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper focus on MDPs in which there is a stochastic delay in the execution of the action selected by an agent acting in the MDP. Stochastic exectuion delay can result in the agent executing actions in the wrong state as the environment changes in real-time. Prior work focuses in fixed-delay times. This work provides a framework for situations in which the delay time is stochastic.

### Strengths
**Orignality:"" The approach introduced in the paper is a novel algorithm for a problem framed in a more realistic way than before.

**Clarity:** The paper is relatively clear and easy to understand. Some minor tweaks could be useful (see later.)

**Significance:** The approach proposed would be of interest to others working MDPs with stochastic delays.

**Quality:** The algorithm designed seems reasonable. The theoretical analysis looks sound however I did not thoroughly go through the proofs. The experiments chosen made sense however there are weaknesses in the results (see later.)

### Weaknesses
 - I may be misunderstanding the graphs, but it looks as if SD-EZ scores worse than the other algorithms in most of the games in the plots in Fig 3a and 3b. Also, there are no confidence intervals or significance testing of any kind.

- The algorithmic description is slightly difficult to follow. Perhaps breaking down the data structures (lists, etc.) used into a list would help ease the process.

### Questions
No questions.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In the real world, state information may not instantly be observed, actions may not instantly be applied, and reward feedback may not be immediate for various environmental reasons. The authors tackle this problem, called stochastic execution delay in MDPs, through the introduction of a new formalism, SED-MDPs. They prove that during policy optimization it is sufficient to restrict the search to the set of Markov policies and present a novel algorithm called Delayed EfficientZero, which shows improved performance over EfficientZero and Delayed-Q on Atari benchmarks.

### Strengths
The authors motivate the problem well. It's easy to understand why stochastic execution delay is an important problem in RL. The contributions are also strong. The extension of ED-MDPs into SED-MDPs seems useful, and Theorem 4.2 is a nice theoretical result that shows Delayed EfficientZero is a well-principled algorithm for them. The results seem promising, given that Figure 5 is correctly labeled and not Figure 3.

### Weaknesses
There are some clarity issues with the experiments, particularly in Figure 3. It seems mislabeled. Figure 5 in the appendix suggests blue should be SD-EZ, red delayed DQN, and white Oblivious-EZ. It also looks like delays appear from "low to high" rather than from "high to low" as suggested in the caption. It would also be nice for comparison's sake to standardize the figure so that the same game appears on a single row in both columns.

Since SED-MDP is a new formalism, it may benefit the paper to include experiments in simpler domains. A central point of the paper seems to be constant vs. stochastic delays, but the experiments don't seem to show much of a difference between algorithms in the two environments for a given Atari game.

### Questions
My low score is down to the problems with Figure 3, which is central to supporting the claim about improved performance over Atari. If the authors can confirm my suspicions and commit to fixing the figure in the rebuttal, or at least clarify the situation, I will strongly consider raising my score (after considering other reviews as well).

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces(?) an MDP variant with stochastic execution delay. For the problem considered the authors show that  the optimal policy lays in a class of Markov policies. A variant of an MCTS algorithm, EfficientZero, is proposed that deals with the stochastic delay in the execution. Empirical evaluation are performed on a set of modified Atari benchmarks with superior results against some baselines.

### Strengths
The delayed MDP variant seems a relevant problem.

The theoretical insight for the considered variant is valuable, and the proposed algorithm extension seems reasonable.

### Weaknesses
It is not clear that this is a new MDP variant, or it is a particular version of the one with random delays considered in the Bouteiller article (cited in the paper) - with no observation delays. The core distinction from existing work on delayed MDPs, specifically the formulation in Bouteiller, needs to be rigorously established. The current presentation leaves ambiguity regarding the novelty of the proposed SED-MDP. Specifically, while the authors claim a difference in state space representation, the implications of this difference on the theoretical properties and practical performance are not fully elucidated. The absence of a clear comparison, highlighting the specific limitations of the Bouteiller formulation that the SED-MDP overcomes, weakens the contribution.

The algorithm is described only in terms of differences to EfficientZero, which makes it hard to understand. The description lacks sufficient detail to allow for independent implementation or verification. The modifications to EfficientZero are not clearly delineated, making it difficult to assess the complexity and practical feasibility of the proposed algorithm. A complete description of the algorithm, including the specific changes made to the search and learning processes, is required for a thorough evaluation.

While the experiments are fairly extensive, there is the issue of lack of clear baselines when a new problem is proposed. The absence of a direct comparison to existing methods for handling delayed actions, such as an adaptation of the Delay-Correcting Actor-Critic, makes it difficult to assess the relative performance of the proposed approach. The empirical evaluation would benefit from a more comprehensive set of baselines, including methods that explicitly address action delays, to provide a more robust assessment of the proposed algorithm's effectiveness. The current evaluation is limited by the lack of a clear benchmark for comparison.

Minor: the initial state distribution (\mu) in the MDP tuple is not present in the SED-MDP definition. Is this an intentional omission?

### Questions
The relation between the MDP variant considered here and the one discussed in the Bouteiller article should be made clear. I would prefer also some motivating discussion on the choice of dealing with the action delays. Personally, I would find more natural if the action delays would not be limited to discrete values, and being executed after the delay (in many physical systems, the evolution of the system is not restricted to discrete steps anyway, even if the decision are). This would avoid the drop and duplication of the actions. Also, we might not necessarily observe the realization of execution delay, unless we can reverse engineer it from a known transition model (when it is deterministic). 

I can see arguments for the considered variant as well. Since the `proper' way to incorporate stochastic action delays in the MDP is not well established, I would like to see some (more) motivating discussion on the choice, and not only how it is handled. 

While MuZero and (somewhat to lesser extent) EfficientZero are well known, it is still difficult to understand the new algorithm described only in terms of differences to EfficientZero. The algorithm should be described completely, while pointing out the relevant differences.

The experiments are fairly extensive, but there is the issue of lack of clear baselines when a new problem is proposed. Maybe adapting the Delay-Correcting Actor-Critic of Bouteiller (even if does not have an MCTS module)?

Minor: the initial state distribution (\mu) in the MDP tuple is not present in the SED-MDP definition. Is this an intentional omission? 

Overall, I feel that there is a valuable contribution in the paper, but the presentation issues are fairly significant, and make the evaluation of the contribution difficult.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
