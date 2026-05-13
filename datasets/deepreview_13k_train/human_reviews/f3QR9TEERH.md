# Safety-Prioritizing Curricula for Constrained Reinforcement Learning

- Decision: Accept
- Scores: 3, 6, 6, 6

## Abstract
Curriculum learning aims to accelerate reinforcement learning (RL) by generating curricula, i.e., sequences of tasks of increasing difficulty. 
Although existing curriculum generation approaches provide benefits in sample efficiency, they overlook safety-critical settings where an RL agent must adhere to safety constraints.
Thus, these approaches may generate tasks that cause RL agents to violate safety constraints during training and behave suboptimally after. 
We develop a safe curriculum generation approach (SCG) that aligns the objectives of constrained RL and curriculum learning: improving safety during training and boosting sample efficiency.
SCG generates sequences of tasks where the RL agent can be safe and performant by initially generating tasks with minimum safety violations over high-reward ones.
We empirically show that compared to the state-of-the-art curriculum learning approaches and their naively modified safe versions, SCG achieves optimal performance and the lowest amount of constraint violations during training.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper tried to ensure the safety of curriculum learning.
Unlike previous curriculum learnings that tried to make the agent perform better, this paper prioritized safety but still cared about performance. 
The paper compared their results with CURROT(Klink 2022) on safety maze, safety-goal, and safety-push, which did not care about safety. 
The results showed that SCG can achieve a low CV regret and still achieve a high success rate.

### Strengths
The performance seems to be better.
It can achieve optimal policy.
Compared to CURROT,  it is safer.
Compared to DEFAULT, it is more sample efficiency.

### Weaknesses
1 The paper only compared simple environments. It does not compare to the environments in the previous work. For example, Point Mass and Bipedal Walker Stump Tracks. 

2 The method seems trivial to me. It is mostly based on CURROT.

3 There are many other curricular learning methods with different settings. This paper can show that it can be used in the same setting as CURROT.

### Questions
1 A proper baseline should be using a goal that cares about both safety and performance. The score can weighted sum of both scores. Using different weights will be interesting. 

2 Since the paper cares about cumulated regret, have you thought about the possibility of making more mistakes first and learn those mistakes can avoid future mistakes?

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
4

### Summary
This paper proposes modifying curriculum generation techniques to incorporate safety constraints. It does so by constraining the curriculum to not produce tasks which tend to result in constraint violations.

### Strengths
The clear exposition quickly brings the reader up to speed with the pragmatic approaches in the space of curriculum generation. It makes it clear how safety constraints are not incorporated in current techniques, providing a clear gap for this method to fill. The method appears to work approximately as advertised, resulting in similar performance to prior works with less violation of constraints.

### Weaknesses
The biggest weakness of this work is the lack of a demonstration of scalability. The 2-d navigation task with 2-d goals provides a very small space for curriculum design where all tasks can be approximately enumerated. It is unclear how this approach would scale to situations where the spaces of possible tasks is combinatorially large. However, as this is a concern that is shared with much of the prior work, I do not see this as a reason in itself to reject the paper.

The main limitation keeping me from raising my score is that it appears the impact of this work is currently somewhat limited. This is in-part because of the scale, in part because the gains on both safety and performance are not as dramatic as one would hope, and in part because it appears to be far from the point where it could be tested in concrete applications. My evaluation of this paper would be significantly higher if it were shown to be applicable to a robotics domain, where safety during training is a critical component. I am guessing this is not in the current draft because it is difficult to scale underlying methods like CURROT to those domains, but if that is the case, then it is not clear if this approach would still be applicable with whatever approach does eventually scale. These uncertainties make it less clear for the reader what to take away from this paper for their own future research.

The one point where the paper can be made significantly more clear is explaining the apparently constraint-violating tasks in Figure 5 c and Figure 3 (right). My sense is that these tasks are not as constraint-violating as they seem since they have a high-tolerance, but it cannot be confirmed from the diagram since there is no correspondence between color and radius of the tolerance. I think this could be resolved by adding a few circles to-scale to ones side of these figures which visually depicts what color would correspond to a given radius. This could then let me check that the tolerance of the radius is sufficient to let the agent avoid a constraint violation.

Minor point:
- 188 and 193 I think these sentences do not completely describe the objective, since they does not say what happens when "finding the optimal policy" and "minimising the constrained violation regret" are in tension.

### Questions
What is the main limitation to applying this approach to higher-dimensional environments like Brax?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents a safe curriculum generation (SCG) approach aimed at enhancing safety during training while improving sample efficiency. SCG generates task sequences as context distributions, prioritizing tasks with minimal safety violations over high-reward tasks in the early stages to safely converge on the target context distribution. Empirical studies indicate that SCG outperforms state-of-the-art curriculum learning methods and their naively adapted safe versions, achieving optimal performance with the fewest constraint violations during training.

### Strengths
- The paper effectively highlights the gap in current curriculum learning (CL) algorithms and the importance of developing safe CL approaches.
- Background and related work are thoroughly described, making the contribution and method easy to understand.
- The paper is well-organized, with clear explanations and logical flow.
- The algorithm demonstrates state-of-the-art performance across multiple benchmarks.

### Weaknesses
 - Limited Novelty: The approach’s novelty is modest, as it primarily adds an additional constraint to the existing CURROT algorithm.
- Empirical Limitations: 
    - The empirical evaluation lacks comparisons with other safe-RL baselines and is limited to three domains.
    - Sensitivity to newly introduced parameters (e.g., \apha_k) is not thoroughly analyzed.

### Questions
- Was the cost annealed in the Naive approach as well?
- How does the proposed approach compare to other safe-RL algorithms in these domains?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a safe curriculum generation (SCG) approach. Using safety constraints, SCG constraints the evolution of the curriculum to stay in the safe zone while annealing towards the maximization of the policy's performance. Based on the CURROT, SCG includes safety constraints to ensure that agent will not venture and make dangerous movements during training. Focusing on Safety-Push, Safety-Maze, and Safety-Goal environments, the authors explores how such design choices makes SCG outperform CURROT and other baselines.

### Strengths
This paper is generally well written and the structures are easy to follow, with the headers clearing marking out the points to be made across. The relative work is quite comprehensive, and extensive experiments conveys the main points well.

### Weaknesses
 - The algorithm is heavily inspired by CURROT and it feels like a somewhat of a safe RL implementation of CURROT. While some may consider this to be a incremental improvement of algorithm, I think the paper could be made stronger if the authors could share the design insights that led to SCG. For example, why did the authors decided to design an algorithm inspired by CURROT? The algorithmic features that differentiates SCG from CURROT, what were their motivations? If the authors could summarize their insight in a way that could help other researchers to make improvements to other existing algorithms in RL, the contribution of this paper would be much more significant.

- I think the paper does not convey well some of the underlying assumptions and motivations, especially towards the empirical analysis. I have included the details in the questions.

### Questions
* What is the motivation for choosing the safety-maze, safety-goal, and safety-push as benchmarks? Why would you consider that these baselines would demonstrate the pros and cons of SCG better than other benchmarks?
* Is the 'Default' mentioned in the empirical studies results of running RL without any curriculum generator?
* As this algorithm is inspired by CURROT, I understand why CURROT was chosen as baselines. But as for the rest, why were the other baselines selected for? What does comparing SCG with the selected baselines demonstrate?
* In figure 4, we see boxes and bars. Would it be correct to assume that boxes are standard deviations and bars are the maximum and minimum of the data distribution?

### Soundness
2

### Presentation
2

### Contribution
2
