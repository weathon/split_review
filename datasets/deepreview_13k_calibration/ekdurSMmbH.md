# Universal Off-Policy Selection for Human-Centric Systems via Participant Sub-grouping

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Human-centric tasks like healthcare and education are characterized by heterogeneity among patients and students, resulting in different disease trajectories and learning styles that require personalized treatments or instructional interventions for specific subgroups. When deploying reinforcement learning (RL) for such tasks, off-policy selection (OPS) is essential, since it it closes the loop by selecting and
evaluating RL-induced policies offline, without the need for any online interaction with the participants. Many pre-existing OPS methods, however, do not consider the heterogeneity among the participants. In this work, we introduce a universal off-policy selection (UOPS) approach to address the issue of participant heterogeneity by taking a multi-step approach. Initially, it divides the participants into sub-groups, grouping together those who exhibit similar behaviors. Subsequently, it acquires OPS criteria tailored to each of these sub-groups. Consequently, when new participants come, they will receive policy recommendations based on the sub-groups
they align with. This methodology enhances the adaptability and personalization of the RL system, ensuring that policy selections align more closely with the unique characteristics of each participant or group of participants. We evaluate UOPS’ effectiveness through two applications: an intelligent tutor system that has been used in classrooms for over eight years, as well as a healthcare application for
sepsis treatment and intervention. In both applications, UOPS shows significant improvements in students’ learning and patient outcomes.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a framework for accounting for heterogeneity in people when evaluating and selecting RL policies offline. They call their method universal off-policy selection (UOPS). Broadly, the method consists of categorizing each human participant into a certain class, and then finding a policy that suits each participant class the best. In this way, the RL method accounts for heterogeneity among multiple types of participants. The authors demonstrate the empirical performance of their approach on an educational task and a healthcare task.

### Strengths
- The authors clearly communicate their objective and the backbone of their approach. They are well-motivated, especially with the education application.
- The educational dataset is novel and is impressive in its breadth.
- The proposed methodology behind UOPS is quite straightforward and intuitive. No extra frills added where not needed, which I appreciate.

### Weaknesses
 - While the paper is quite convincing in its results on the education dataset, I'm not sure that ICLR is the best venue for these results. The methodology presented is less novel/interesting than the education dataset and results. This leads me to think that this work could be better suited for an education-based venue.
- Consider a simple approach to the same problem: Cluster the students using some basic technique, then run any out-of-the-box RL method on each group independently. How would this compare to your results? It seems that there is a decently large sample size and not a crazy high number of subgroups.

### Questions
See the second bullet in the Weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a policy selection algorithm to produce more optimal behavior policies for human centered systems (HCS). The algorithm uses previously collected offline data with a partitioning function to select optimal policies for each partition of the offline data. New users of the HCS are then assigned to the most similar partition and given the previously selected policy for the partition. The author's primary contribution is their UOPS framework which bridges the gap between online policy deployment and offline policy selection. To support their contribution the authors provide two empirical experiments.

### Strengths
* The authors provide two substantial experiments (one real world and one simulated) where their proposed method outperforms 18 alternative methods selected by the authors
* The authors provide extensive connections to existing literature and bring together many ideas from disparate fields such as unsupervised learning (i.e. clustering), off-policy evaluation, and human centered systems.

### Weaknesses
 * The motivation for the method seems weak. For example, one proposed problem is the time and cost to collect data, however the proposed method still requires trajectories to be collected a priori thus the time and cost of data collection is not removed.
* Sometimes the paper says clustering is done based on the initial state but it does not seem obvious that optimizing (1) requires similarity in the initial state.

* It is not clear to me how the clustering method suggested optimizes (1). The TICC clustering method maximizes the likelihood that an example belongs to a group correct?
* The terminology of "policy selection" instead of what the more common "policy evaluation" is a little confusing. There does not seem to be any reason why this method couldn't be referred to as an improved policy evaluation technique.
* How does this work relate to Konyushova, Ksenia, et al. "Active offline policy selection." Advances in Neural Information Processing Systems 34 (2021): 24631-24644.
* Why do the authors believe clustering improves performance? If the initial state is unique to participants wouldn't it be possible to learn a single policy that performs well across all states? Why do they think this doesn't happen? Is the policy class being trained on offline data not rich enough?

### Questions
* It is not clear to me how the clustering method suggested optimizes (1). The TICC clustering method maximizes the likelihood that an example belongs to a group correct?
* The terminology of "policy selection" instead of what the more common "policy evaluation" is a little confusing. There does not seem to be any reason why this method couldn't be referred to as an improved policy evaluation technique.
* How does this work relate to Konyushova, Ksenia, et al. "Active offline policy selection." Advances in Neural Information Processing Systems 34 (2021): 24631-24644.
* Why do the authors believe clustering improves performance? If the initial state is unique to participants wouldn't it be possible to learn a single policy that performs well across all states? Why do they think this doesn't happen? Is the policy class being trained on offline data not rich enough?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents an off-policy selection (OPS) method, which aims to determine the best policy from a set of predefined policies. In contrast to the conventional approach of selecting a universal policy, this paper suggests an initial step of clustering trajectories (or, equivalently, participants) and subsequently selecting the most suitable policy for each sub-group. Additionally, the paper introduces a data augmentation technique to address situations where the number of participants within each group is insufficient to accurately estimate policy value. The evaluation is performed in two settings: an offline setting for intelligent tutoring and an off-policy setting for simulated sepsis treatment.

### Strengths
- The general idea of not treating everyone with a single policy sounds reasonable and may protect underrepresented groups.
- Evaluations are conducted on both real and simulated data.
- An observation that a fixed policy for everyone may not work well for some sub-groups is interesting.

### Weaknesses
 - The clarity of the paper could be improved. It was hard for me to follow the details of the paper both the methodology and experiments at some points.
- At the outset, the idea of selecting a policy out of many for each sub-group sounds like designing a new policy. I have difficulty understanding whether, during the partitioning step, any information unavailable to the policy is being used or not. In fact, if there is some information, like patient characteristics, which are used to cluster participants but were not used in training the policy, why not incorporate them in the first place to train the policy? This raises concerns about the practical utility of the proposed approach, as it seems to introduce an unnecessary layer of complexity by first training policies without subgroup information and then using that information for policy selection.
- There are some inconsistencies in the problem formulation and explanations. Please refer to my questions.
- The choice objective to choose partitioning requires further motivation. Please refer to my questions. The objective function (1) seems to be summing the value of the behavioral policy across different subgroups, which should simply be the value of the behavioral policy itself, making the optimization problem trivial. This raises questions about the validity and purpose of the proposed objective.
- On the evaluation side, some values need further clarification. For instance, true reward, or AE of OPE.
- The writing could be improved as there are many typos in the text. For example: "it it" in the abstract, "a initial" in Assumption 2, "an classic" on page 6

### Questions
1. Please clarify what information may be available at the time of partitioning and if any why they cannot be used during training.
2. In Problem 1, you say the initial state is given but in calculating $V^\pi$ take the expected value wrt $s_0$. What does it mean?
3. I thought Assumptions 1 and 2 imply a one-to-one correspondence between participants and the distribution of initial state. However, a stronger assumption seems to be made on page 3 last paragraph.
4. I'm having a hard time understanding the notation of $V^\pi_{K_m}$ in Definition 1. What distribution $s_0$ is drawn from? 
5. Regarding objective (1), isn't the sum over the second term just the value for behavioral policy?
6. Regarding evaluations, please elaborate what are the values reported on the y-axis of Figure 1 in complete detail. Also, what is a true reward mentioned on page 7 for the IE experiment and how AE is defined on page 8?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
