# Invariance to Planning in Goal-Conditioned RL

- Decision: Accept
- Avg Score: 4.25
- Scores: 3, 3, 5, 6

## Abstract
We study goal-conditioned RL through the lens of generalization, but not in the traditional sense of random augmentations and domain randomization. Rather, we aim to learn goal-directed policies that generalize with respect to the horizon: after training to reach nearby goals (which are easy to learn), these policies should succeed in reaching distant goals (which are quite challenging to learn). In the same way that invariance is closely linked with generalization is other areas of machine learning (e.g., normalization layers make a network invariant to scale, and therefore generalize to inputs of varying scales), we show that this notion of horizon generalization is closely linked with invariance to planning: a policy navigating towards a goal will select the same actions as if it were navigating to a waypoint en route to that goal. Horizon generalization and invariance to planning are appealing because of their potential reach: they imply that a policy trained to reach nearby goals would succeed at reaching goals that are arbitrarily more distant.Our theoretical analysis proves that both horizon generalization and planning invariance are possible, under some assumptions. We present new experimental results, as well as recalling results from prior work, in support of our theoretical results. Taken together, our results open the door to studying how techniques for invariance and generalization developed in other areas of machine learning might be adapted to achieve this alluring property.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the generalization of RL from the perspective of horizon invariance. An RL agent that has been trained to reach nearby goals should succeed on distant goals and hence generalize to different horizon lengths. The paper intends to study how the techniques on invariance and generalization from other machine learning domains can be adapted to make goal-directed policies generalize to different horizons.

### Strengths
1. The paper aims to study an important question of generalization and planning under different horizon lengths for a goal-conditioned RL agent.
2. Connections between existing methods and the new proposed methods are provided.

### Weaknesses
1. The writing of the paper needs some work to strengthen the motivation and claims. The related works section can also benefit from further elaboration and coverage of the related literature.
2. The paper mentions that horizon generalization means that a policy that can achieve a goal n steps away should also be able to reach any new goal for which that original goal is a waypoint. This is a bit far-fetched of a statement as in a longer horizon, a lot of different things could happen over this longer timeframe and not all en-route waypoints would be relevant. Moreover, things could demand a completely different set of actions or approach after these n steps. Defining horizon generalization in this scenario needs a more thorough definition.
3. The example of dominoes considered in the paper is a very simple bandit setting, while the paper focuses on more general RL settings with different horizon lengths. Providing relevant working examples will be beneficial to the understanding.
4. Experiments are over simpler environments / task settings.

### Questions
1. Generalization in RL and in goal-conditioned setting can come in different forms. While generalizing over different horizons is important, why do you think invariance will help here? As the horizon changes and the trajectories get longer, it is possible that any of the waypoints relevant over shorter horizons are not that relevant anymore if better paths are discovered for example.
2. How does the method relate to when we are no longer looking at smaller horizons as being sub-goals of the longer horizons? Or even when we are not considering the goal as a condition. Do you think this work can include those cases?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper explores the problem of horizon generalization in goal-conditioned reinforcement learning. It presents clear definitions of planning invariance and demonstrates how this concept can facilitate horizon generalization.

### Strengths
The problem studied in the paper is novel and very interesting to me. The motivation of the paper is clear and the writing of the paper is generally clear and easy to fllow.

The paper presents clear definition of planning invariance and horizon generalization, which make sense to me.

### Weaknesses
The paper contains some symbols that are not well defined, some of which even affect the readability of the paper.

- I got lost from Line 245 with $d(s,a,g)$. I don't understand the meaning of this symbol and why it contains an action. The paper didn't clearly define it. This is critical as I failed to fully understand the proof of Lemma 1 and Lemma 2, which are the major results of the paper. I hope I didn't miss anything.

Some undefined symbols that do not affect reading:

- Eq. (2): $p_\gamma^\pi$, $Geom$ is never defined
- Line 117: $\delta$, $r_g$

The paper also uses different terminology from the common terminology, making it seem less professional.

Usually, the distance (metric) function should satisfy the three rules: Non-negativity, Triangle Inequality, and Symmetry; while a quasimetric relaxes one or more of the metric's defining properties.

Minor Comments:

- It seems Lemma 1 and 2 are some important results of the paper. Then please use "Theorem" rather than "Lemma".
- "Markove process" should be "Markov Decision Process". You didn't include the definition of the reward function.



Another weakness is the paper's lack of clarity on how its discoveries could inspire future algorithm development. I hope future revisions of the paper will devote more effort to exploring this aspect.

### Questions
I was unable to assess the correctness of the theorems due to some undefined symbols mentioned earlier. Please respond to my previous queries in weakness. I will reassess them in case I missed anything.

### Soundness
1

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies horizon generalization in goal-conditioned RL. The main contributions of the paper are a definition of horizon generalization and planning invariance, and proofs of existence for both, as well as some small-scale experimental studies. I admit I am unclear what the takeaways for the reader are - it seems like the main contributions, i.e. the definition of horizon and planning invariance, are quite obvious, as well as the existence of these kinds of invariances. I do agree that the goal of inducing invariances that facilitate generalization in RL is important. It may be that I misunderstood parts of the paper, hence I am putting my confidence at 3 and recommendation at borderline.

### Strengths
- Conceptual investigations are welcome
- The paper's figures are well drawn

### Weaknesses
 - As mentioned above, the takeaways for the reader are not clear - this does not propose a new method, or (to my understanding) clearly shed light on existing methods, highlight a previously unknown weakness,...
- The relationship of this work to other areas of work is unclear in some cases.

- It seems obvious that if the series of waypoints produced by a planner is optimal, then we should have planning invariance according to the definition given here (i.e., the optimal action to reach the next waypoint is the same at the optimal action to reach the final goal), so my guess is that this is not the main message of the paper. The other way around, where the agent trains on easy goals and generalizes to hard ones, seems much more useful, so that this is what the paper is getting at. The paper refers to this as the “forward perspective”. However, there doesn't seem to be any suggestions on how to induce this kind of invariance. Also, this seems related to compositional generalization in language-conditioned RL, where the agent is trained on language commands and asked to generalize to novel combinations. How does this relate to planning invariance/generalization?

- The paper claims that most prior work on generalization in RL relates to invariance to perceptual changes or simulation parameters. But there is a rich literature on state abstractions which induce invariances to criteria other than perceptual differences, for example: optimal actions (known as policy irrelevance), rewards/Q-values (utile distinctions) [1] bisimulation [2]  belonging to a common latent state (however defined) [3]. It seems like the proposed planning invariance could be seen as a special case of one of these other abstractions (such as policy irrelevance). It would be helpful to include a discussion of other types of state abstraction/generalization in the paper. If the proposed invariance cannot be subsumed in any of the prior ones, it would be helpful to describe in what ways. 

- It would help to give more examples of non-trivial cases where planning invariance is or is not met, in order to build intuitions. There is one example in Section 4.1, but it didn’t really help my understanding because in that example, there was a single action that was optimal for all goals (and the problem is in a sense trivial for that reason). Also, the example of knocking over dominoes with levers felt fairly contrived. Would it be possible to add one or more examples that 1) have different actions that are optimal for different goals, 2) one can construct some policies that do have planning invariance and others not, in order to illustrate their differences, and 3) are more closely related to common sequential decision-making problems? I know there is also the example in Figure 6, but there the goal-conditioned policy on the left is not optimal.

### Questions
- It seems obvious that if the series of waypoints produced by a planner is optimal, then we should have planning invariance according to the definition given here (i.e., the optimal action to reach the next waypoint is the same at the optimal action to reach the final goal), so my guess is that this is not the main message of the paper. The other way around, where the agent trains on easy goals and generalizes to hard ones, seems much more useful, so that this is what the paper is getting at. The paper refers to this as the “forward perspective”. However, there doesn't seem to be any suggestions on how to induce this kind of invariance. Also, this seems related to compositional generalization in language-conditioned RL, where the agent is trained on language commands and asked to generalize to novel combinations. How does this relate to planning invariance/generalization?

- The paper claims that most prior work on generalization in RL relates to invariance to perceptual changes or simulation parameters. But there is a rich literature on state abstractions which induce invariances to criteria other than perceptual differences, for example: optimal actions (known as policy irrelevance), rewards/Q-values (utile distinctions) [1] bisimulation [2]  belonging to a common latent state (however defined) [3]. It seems like the proposed planning invariance could be seen as a special case of one of these other abstractions (such as policy irrelevance). It would be helpful to include a discussion of other types of state abstraction/generalization in the paper. If the proposed invariance cannot be subsumed in any of the prior ones, it would be helpful to describe in what ways. 

- It would help to give more examples of non-trivial cases where planning invariance is or is not met, in order to build intuitions. There is one example in Section 4.1, but it didn’t really help my understanding because in that example, there was a single action that was optimal for all goals (and the problem is in a sense trivial for that reason). Also, the example of knocking over dominoes with levers felt fairly contrived. Would it be possible to add one or more examples that 1) have different actions that are optimal for different goals, 2) one can construct some policies that do have planning invariance and others not, in order to illustrate their differences, and 3) are more closely related to common sequential decision-making problems? I know there is also the example in Figure 6, but there the goal-conditioned policy on the left is not optimal. 

[1] https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=ca9a2d326b9de48c095a6cb5912e1990d2c5ab46

[2] https://www.auai.org/uai2014/proceedings/individuals/67.pdf

[3] https://arxiv.org/pdf/1901.09018

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The motivation and insight presented in this paper are interesting and straightforward. This paper presents the abundant theoretical contribution to Planning Invariance and Horizon Generalization. Experimental results of existing methods support the theoretical results.

### Strengths
1. Good writing and structure.
2. The authors illustrate their research problem via the good toy example (Figrue 3).
3. Theoretical results are clear and sound.

### Weaknesses
I have no concern with the main contribution of the theoretical part of this paper. The main concern is related to the application and limitations.

1. One of the main concerns of the reviewer is the limitations of the planning invariance and horizon generalization, as mentioned by the authors (Section 4.5).
2. I am also concerned about real-world applications (e.g., more complicated tasks). In real-world settings, the planning invariance and horizon generalization seem to be limited in their application to general cases, although they indeed exist as mentioned by the authors. In the high-dimensional settings (Section 6.2), it is hard to derive insightful results.
3. The authors provide some interesting future directions in Appendix C, but it would be better to present some experimental results or practical implementations.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3
