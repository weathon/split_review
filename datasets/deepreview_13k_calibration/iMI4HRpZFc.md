# Identifying and Addressing Delusions for Target-Directed Decision Making

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
\vspace*{-2mm}
Target-directed agents utilize self-generated targets, to guide their behaviors for better generalization. These agents are prone to blindly chasing problematic targets, resulting in worse generalization and safety catastrophes. We show that these behaviors can be results of delusions, stemming from improper designs around training: the agent may naturally come to hold false beliefs about certain targets. We identify delusions via intuitive examples in controlled environments, and investigate their causes and mitigations. With the insights, we demonstrate how we can make agents address delusions preemptively and autonomously. We validate empirically the effectiveness of the proposed strategies in correcting delusional behaviors and improving out-of-distribution generalization.
\vspace*{-3mm}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the problem of “delusions” in target-directed (goal-conditioned) RL by establishing a taxonomy of delusions that are possible for the Generator (proposer of the targets) and the Estimator (that measures the goodness of the target). Then, they propose two new HER relabeling strategies (and mixed strategies) to mitigate the effects of different types of delusions.
Finally, they evaluate their proposed strategies in a controlled gridworld that allows them to quantify the different kinds of delusional targets they consider.

### Strengths
1. The systematic approach to studying delusions in target-oriented RL is relevant to the community. The authors' approach allows us to understand the potentially problematic behavior that can arise from naively training agents within this paradigm.
2. The empirical evaluation shows an organized approach to verifying the effect of the types of delusions and the effects of potential mitigation strategies. 
3. The knowledge provided in the paper is of general interest to practitioners and researchers.

### Weaknesses
1. I can see that the authors studied the problem with empirical rigor, however, the experimental section, which goes a long way to showcase the problems, looks a bit crammed and it’s hard to follow. I would suggest sacrificing part of the previous discussion to treat the empirical section with more care.

2. Figure 3, it’s hard to follow because of the number of overlapping curves, colors, and legend positioning. This overall makes the curves hard to interpret.

3. Though I understand that scaling these ideas to more complex environments can be the subject of future research, perhaps showcasing the effect on the learning performance these mitigation strategies can have in a different environment (beyond the controlled gridworld proposed) would also be informative and relevant to this paper.

### Questions
1.  I see much of the mitigation strategies are based on making the estimator better and recognizing delusions from the generator. What kind of mitigation strategies (beyond "generate") would be useful to generate less delusional targets?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses failure modes in target-directed Reinforcement Learning (RL) agents induced by delusions, where the agent holds false beliefs about their targets, leading to poor OOD generalization and/or undesired behaviours.
The authors first identify and characterize delusions that either come from the generator or the estimator of the targets. The empirical experiments are based in the case of HER-based training. 
In this case, they propose 2 new strategies: 'generate', 'pertask' in addition to 2 ones  coming from the literature ('future', 'episode'). 
The authors combine in an hybrid fashion this 4 HER strategies, showing that this approach can help mitigate the issues coming from delusions.

### Strengths
- OOD generalization is an important topic in RL, and further work on this is beneficial for the community. 
- The characterization of different type of delusions (coming either from the generator or estimator) is valuable both in the context of the paper, but also for future work possibly building on this. 
- The approach presented in Section 4 is sounds, Table 1 is particularly useful to understand the motivation behind their design choices.

### Weaknesses
In general, I am particularly unsure about both the relevance and the soundness of the claim. The paper in fact argues very strongly about their approach, which I however think is limited in some ways. In fact, the authors investigate only HER-based training, specifically the case where both the estimator and the generator are trained in this way. It is okay if the paper focuses only on this, but the authors claims that all of their approaches can be extended beyond HER, which is not easily validated in my opinion.

The paper is an empirical paper, although it does not seem the Experiment section to be sufficiently strong. The paper does not explain the results extensively and/or in enough detail everywhere. I'm also skeptical about the results being as strong as they claimed they are.  In general I find the figures hard to follow.

Please see below for more details for my criticisms about the paper.

- "For aggregated OOD performance [...] we sample 20 tasks [...], which have a mean difficulty matching the training tasks.". Could you clarify why you call this OOD performance? For this to be the case, I would both expect the gradient of difficulties to be wider. My intuition is that you want to keep the average the same to distinguish capability generalization vs delusion generalization, is that correct? I would however not call this OOD performance if I understand it correctly...  In general, I am curious how you see the difference between capability vs goal misgeneralization [1], and argue which of the two your work addresses. This would help me better clarify how valid the claims made are

- "To maximize difficulty, the initial state is fixed in each novel evaluation task instance: the agents are not only spawned to be at the furthest side of the monster": this is not always true, especially if the agent did not see often particular combination of start positions/state. This is true in the case only in terms of capability generalization, but I guess your answer to the above can also address this one.

- I suggest for the experiments to include actual OOD scenarios as I intend them. For example, try to test a scenario where the agent spawns with already one shield in hand, but another is present in the environment ( without training in such a situation). It would then be interesting to see if the targets generated still suggest to pick up the other shield even if it is in fact not necessary...

- I'm unsure the characterization of delusions proposed is comprehensive - could you argue why this is the case? It seems that this applies only to the environments proposed, and may not be general. It is okay if this is the case, but that should be specified better.

- I would like to see an experiment where the proposed approaches are validated beyond HER. If that is not possible, I argue to be appropriate to weaken the claims regarding such of a possible extension. If you do not agree, could you please explain why we expect these results to hold further?

- Figure 3 is too condensed, and very hard too look at. In some cases the error bars are extremely large, which makes difficult to even consider some of the results statistically valid. I suggest this work [2] to improve how metrics are reported such that to have a better sense if this empirical results do in fact hold...

- The best performing algorithm in Figure 3h seem to reach accuracy ~0.4. If I understand correctly, the maximum achievable in that case is 1, correct? If you have discounting, what is the baseline given by the optimal policy? Are all levels proposed solvable? It is important to report a baseline also for the other figures somehow, since the results presented in this way make it difficult for their significance to be judged.

- I suggest moving the related work section either after the introduction, or before the conclusion. Now it breaks the flow of the paper since it is placed just before the experiments

- The authors say in line 371 "Due to page limit, 3 out of 4 sets of experiments are only presented in the Appendix". While I do not expect all of the experiments to fit in the main paper, being able to condense and critically decide what goes in the main text is an important task authors should dedicate time to. This is mainly an empirical paper, and it is thus important for the most relevant experiments to be in the main text such that the claims can be supported by those experiments.

- ' generators are a major source of risk related to delusion' should at least backed up by some previous work.

There are also many parts with grammatical errors, e.g.
- line 186
-line 251
-line 257 etc..

### Questions
- "For aggregated OOD performance [...] we sample 20 tasks [...], which have a mean difficulty matching the training tasks.". Could you clarify why you call this OOD performance? For this to be the case, I would both expect the gradient of difficulties to be wider. My intuition is that you want to keep the average the same to distinguish capability generalization vs delusion generalization, is that correct? I would however not call this OOD performance if I understand it correctly...  In general, I am curious how you see the difference between capability vs goal misgeneralization [1], and argue which of the two your work addresses. This would help me better clarify how valid the claims made are

- "To maximize difficulty, the initial state is fixed in each novel evaluation task instance: the agents are not only spawned to be at the furthest side of the monster": this is not always true, especially if the agent did not see often particular combination of start positions/state. This is true in the case only in terms of capability generalization, but I guess your answer to the above can also address this one.

- I suggest for the experiments to include actual OOD scenarios as I intend them. For example, try to test a scenario where the agent spawns with already one shield in hand, but another is present in the environment ( without training in such a situation). It would then be interesting to see if the targets generated still suggest to pick up the other shield even if it is in fact not necessary...

- I'm unsure the characterization of delusions proposed is comprehensive - could you argue why this is the case? It seems that this applies only to the environments proposed, and may not be general. It is okay if this is the case, but that should be specified better. 

- I would like to see an experiment where the proposed approaches are validated beyond HER. If that is not possible, I argue to be appropriate to weaken the claims regarding such of a possible extension. If you do not agree, could you please explain why we expect these results to hold further?

- Figure 3 is too condensed, and very hard too look at. In some cases the error bars are extremely large, which makes difficult to even consider some of the results statistically valid. I suggest this work [2] to improve how metrics are reported such that to have a better sense if this empirical results do in fact hold...

- The best performing algorithm in Figure 3h seem to reach accuracy ~0.4. If I understand correctly, the maximum achievable in that case is 1, correct? If you have discounting, what is the baseline given by the optimal policy? Are all levels proposed solvable? It is important to report a baseline also for the other figures somehow, since the results presented in this way make it difficult for their significance to be judged. 

- I suggest moving the related work section either after the introduction, or before the conclusion. Now it breaks the flow of the paper since it is placed just before the experiments

- The authors say in line 371 "Due to page limit, 3 out of 4 sets of experiments are only presented in the Appendix". While I do not expect all of the experiments to fit in the main paper, being able to condense and critically decide what goes in the main text is an important task authors should dedicate time to. This is mainly an empirical paper, and it is thus important for the most relevant experiments to be in the main text such that the claims can be supported by those experiments. 

- ' generators are a major source of risk related to delusion' should at least backed up by some previous work. 

There are also many parts with grammatical errors, e.g. 
- line 186
-line 251
-line 257 etc..




[1] Di Langosco, Lauro Langosco, et al. "Goal misgeneralization in deep reinforcement learning." International Conference on Machine Learning. PMLR, 2022.

[2] Agarwal, Rishabh, et al. "Deep reinforcement learning at the edge of the statistical precipice." Advances in neural information processing systems 34 (2021): 29304-29320.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
1

### Summary
The paper addresses delusional behaviors in reinforcement learning (RL) agents that set their own sub-goals (targets). These agents sometimes form "delusions"—incorrect beliefs about which targets are achievable or safe. The study identifies two types of target-related delusions: G.1 (nonexistent or invalid) and G.2 (temporarily unreachable). It also categorizes types of estimator errors that arise from delusional target evaluations: E.0 (non-delusional target errors), E.1 (errors related to G.1 targets), and E.2 (errors related to G.2 targets). To combat these, the paper introduces modifications to Hindsight Experience Replay (HER) to train agents to recognize problematic targets more effectively. This approach demonstrates some improvement in out-of-distribution (OOD) generalization, though specific results vary.

### Strengths
Novelty of the Problem: The paper tackles a unique issue in reinforcement learning—delusions in target-directed decision-making, which hasn't been addressed explicitly in previous literature.

Detailed Taxonomy of Delusions: The categorization into G.1 and G.2 target types, along with E.0, E.1, and E.2 estimator delusions, is well-structured and provides clear, actionable insights into RL challenges.

### Weaknesses
Complexity and Clarity: The paper introduces complex terminology and presents dense explanations that may be challenging to follow. This affects readability and accessibility, as it requires a high level of familiarity with RL and HER. The definitions of G.1 and G.2 delusions, while conceptually clear, are not always easy to distinguish in practice, particularly when an agent is in a novel state space. The paper would benefit from more concrete examples illustrating how these delusions manifest in the specific environments used.

Limited Generalization Evidence: Although the study introduces methods to handle delusional targets, the empirical validation is largely confined to specific, controlled environments (SSM and RDS). It is unclear if these strategies would generalize well to more complex or real-world scenarios. The environments, while useful for isolating the problem, are relatively simple grid-world setups. The paper lacks a clear discussion of the limitations of these environments and how they might impact the generalizability of the findings. For instance, the state spaces are discrete and low-dimensional, which may not reflect the challenges of high-dimensional continuous control problems.

High Computational Cost: The proposed strategies, particularly the "generate" strategy, rely on additional computational resources. This limitation may hinder real-world application due to high resource requirements. The paper does not provide a detailed analysis of the computational overhead of the "generate" strategy, making it difficult to assess its practical feasibility. Furthermore, it's not clear how the computational cost scales with the complexity of the environment or the size of the state space.

### Questions
I am not an expert in this domain, and I found this paper relatively difficult to follow. It seems to be more of a conceptual paper rather than a traditional ML paper with detailed formulas and technical explanations. Given this, I don’t have any further questions.

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
3

### Summary
This paper tackles the challenge of delusions in target-directed reinforcement learning agents - a problem where agents develop false beliefs leading to unwanted behaviors and poor generalization. The authors identify and categorize different types of delusions (G.1, G.2, E.0, E.1, E.2), propose two new strategies ("generate" and "pertask") for addressing these delusions through hindsight relabeling, and introduce a hybrid approach that separates generator and estimator training. The work is validated through experiments on two environments (SSM and RDS) using two different methods (Skipper and LEAP), with detailed ablation studies and performance metrics.

### Strengths
* The paper's primary strengths lie in its clear problem identification, technical depth, and thorough empirical validation. The categorization of delusions is well-structured and the proposed solutions are practically implementable. 
* The experimental work is comprehensive, with clear visualizations and detailed analysis. The writing is clear and well-organized, effectively using diagrams and examples to illustrate complex concepts. 
* The hybrid approach of separating generator and estimator training demonstrates good understanding of the underlying challenges.

### Weaknesses
 * The theoretical framework lacks formal analysis and guarantees about why the proposed strategies work. The experimental scope is confined to grid-world type of environments, missing opportunities to demonstrate effectiveness in more complex or real-world scenarios. 
* The paper also lacks sufficient discussion of scalability challenges. How would these approaches scale to more complex environments with continuous action spaces? What theoretical guarantees can be provided about the reduction of delusions? How do these methods compare to other state-of-the-art approaches addressing similar issues in target-directed RL?

### Questions
Please address my questions in Weakness

### Soundness
2

### Presentation
3

### Contribution
3
