# Select before Act: Spatially Decoupled Action Repetition for Continuous Control

- Decision: Accept
- Avg Score: 6.33
- Scores: 6, 8, 5

## Abstract
Reinforcement Learning (RL) has achieved remarkable success in various continuous control tasks, such as robot manipulation and locomotion.
Different to mainstream RL which makes decisions at individual steps, recent studies have incorporated action repetition into RL, achieving enhanced action persistence with improved sample efficiency and superior performance.
However, existing methods treat all action dimensions as a whole during repetition, ignoring variations among them.
This constraint leads to inflexibility in decisions, which reduces policy agility with inferior effectiveness. 
In this work, we propose a novel repetition framework called SDAR, which implements Spatially Decoupled Action Repetition through performing closed-loop act-or-repeat selection for each action dimension individually.
SDAR achieves more flexible repetition strategies, leading to an improved balance between action persistence and diversity.
Compared to existing repetition frameworks, SDAR is more sample efficient with higher policy performance and reduced action fluctuation.
Experiments are conducted on various continuous control scenarios, 
demonstrating the effectiveness of spatially decoupled repetition design proposed in this work.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Spatially Decoupled Action Repetition (SDAR), a framework that allows reinforcement learning (RL) agents to make separate act-or-repeat decisions for each action dimension. The method consists of a two-stage process: first, a selection policy determines if each dimension should repeat, followed by an action policy that generates new actions for those dimensions that chose not to repeat. Experiments across several continuous control tasks demonstrates the framework's performance and sample efficiency over baseline methods.

### Strengths
* The proposed method decouples the action dimensions and achieves more flexible and diverse repetition strategies, while maintaining high action persistence.
* The paper provides a thorough comparison with multiple baseline methods, including SAC, TAAC, and UTE. This context clarifies the advantages of SDAR over both open-loop and closed-loop action repetition approaches.

### Weaknesses
 * The method might be limited when the action dimension is high, which might cause computational overheads.
* The novelty of this paper appears limited, as TAAC has employed a similar two-stage act-or-repeat mechanism; the primary contribution here seems to be the separation of action dimensions.

### Questions
* Can TAAC be regarded as an ablation of the proposed method by treating all action dimensions as a whole for repetition? How about its switch policy?
* Would the proposed method be able to be applied to on-policy methods like PPO, where better sample efficiency would be more valuable?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
A version of state-conditioned action-repeat is proposed that also allows
for arbitrary subsets of the action dimensions to be repeated, while the rest are
directly controlled by the policy. The paper describes in detail how to learn the
action-repeat-selection policy to be learned.  To cope with the combinatorial complexity
issue that arises for high-D action spaces, an importance-based sampling approach is further proposed.
The method is evaluated on a reasonably-sized set of continuous action problems, 
ranging from low-D to high-D action spaces. The method is shown to be more sample efficient
than a reasonably-chosen set of model-free alternatives, including SAC and a variety
of other action-repeat-learning baselines.  Overall, the proposed method is shown to excel.
The learned patterns of action-subset-repeats are also visualized, to help provide
a qualitative understanding of their usage over time by the learned policies.

### Strengths
Strengths:
- clean idea, good execution, clearly written
- a "relatively simple" idea, entirely in the good sense, and so likely to have impact
- will inspire follow-up work;  learning structure in action representations remains
  very much an underexplored area, compared to learning structured or latent state representations

### Weaknesses
Weaknesses:
- I suspect that one could find an example where there is a price to be paid for using this approach, as opposed to it always being more sample efficient. For instance, in environments requiring rapid, uncorrelated changes across all action dimensions, the imposed temporal structure could hinder learning. The method's reliance on action repetition might not be beneficial in scenarios where fine-grained control and immediate responses are crucial, potentially leading to suboptimal performance compared to methods that allow for more dynamic action selection.
- it is always hard to see if equal time has been spent tuning all the comparison RL algos; with the right setup and high-replay ratios, some of the RL algos can possibly see further improved sample efficiencies. It's difficult to ascertain whether the reported gains are solely due to the proposed method or if they are partially attributable to suboptimal tuning of the baselines. The performance of RL algorithms is often highly sensitive to hyperparameter settings, and without a rigorous and systematic exploration of the hyperparameter space for each baseline, it's challenging to draw definitive conclusions about the superiority of the proposed approach.
- it's clear why we should care about learning rate / sample efficiency, but not so clear why we should actually care about action persistence of action fluctuation. While the paper introduces action persistence rate (APR) and action fluctuation rate (AFR) as metrics, the practical significance of these metrics beyond their use in analyzing repetition schemas remains unclear. It's not immediately obvious why an agent should necessarily strive for high action persistence or low fluctuation, especially if such behavior does not directly translate to improved task performance or other relevant metrics.

### Questions
Questions:
- how does experience replay sampling work when a- will be different?
  Or is a- explicitly stored with each tuple in the replay buffer?
- Could the learned "synergies" potentially be transferred when learning a new task?
- Perhaps I missed it, but are the exploration rates for the repetition schema policy, and the regular policy, being annealed?  Might that make sense?
- Ideally a method would also work when the "repetition" substructure could also be discovered even after the action-space was rotated, i.e., imagine all actions spanned all joints, to differing degrees, but the latent structure would still be there. Just a suggestion for something that would be fun (but arguably difficult) to pursue!

Minor feedback:
- At the end of the introduction, the second and third listed contributions probably belong together, as they
  describe the same thing. I like the visualization as another minor contribution.
- The notation might be easier to understand if the repetition schema is called a mask, m, rather than the current "b".
- Is it possible to collapse the two policies to a single deterministic policy pi, after training? 
  This would be of important practical importance.
- "This demonstrates the necessity and effectiveness":  necessity is perhaps too strong;
  it is effective in terms of speeding learning, but arguably not "necessary"
- Table 2: "Avearage"  (typo)
- lines 479-480: "rotors" --> "joints"?
- line 483:  "Besides,"  suggest to remove

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a novel reinforcement learning algorithm, "Spatially Decoupled Action Repetition", which decouples policy and repetition. This philosophy is achieved by learning two policies, selection and action policies. The selection policy outputs which action dimension should be masked and the action policy proposes a new action. The proposed algorithm was evaluated on several control domains, such as classical control, locomotion, manipulation.

### Strengths
* The paper demonstrates a novel algorithm that decouples repetition and control, which is an interesting idea.
* The proposed algorithm performs well on a wide range of control domains.

### Weaknesses
I don't think I am fully convinced by the paper.
1. Overall, I don't think I understand why the proposed decoupling is important. It is an interesting idea that extends the existing action dimension. But why? In continuous control, I believe many challenging problems mandate new actions at every single time step. Even many discrete action problems may require the same. 
2. In other words, what will be the problem class that must require decoupled action repetition? 
3. As a result, I currently think there can be other reasons that the proposed method outperforms the baselines, such as better hyperparameters or larger network sizes. Please note that I am not questioning the integrity of the proposed authors; there can be other reasons that we may not understand.

### Questions
* Would you be able to give us the intuition as to why the proposed method "should" work better than the baselines? Examples or toy-problems would be appreciated.
* The performance is only 10% better than SAC - many other ensemble-based approaches, such as RED-Q or Dro-Q, might perform much better than the proposed method.

### Soundness
2

### Presentation
3

### Contribution
2
