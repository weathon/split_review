# InfoCon: Concept Discovery with Generative and Discriminative Informativeness

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
We focus on the self-supervised discovery of manipulation concepts that can be adapted and reassembled to address various robotic tasks. 
We propose that the decision to conceptualize a physical procedure should not depend on how we name it (semantics) but rather on the {\it significance} of the informativeness in its representation regarding the low-level physical state and state changes.
We model manipulation concepts -- discrete symbols -- as generative and discriminative goals and derive metrics that can autonomously link them to meaningful sub-trajectories from noisy, unlabeled demonstrations.
Specifically, we employ a trainable codebook containing encodings (concepts) capable of synthesizing the end-state of a sub-trajectory given the current state -- {\it generative informativeness}.
Moreover, the encoding corresponding to a particular sub-trajectory should differentiate the state within and outside it and confidently predict the subsequent action based on the gradient of its discriminative score -- {\it discriminative informativeness}.
These metrics, which do not rely on human annotation, can be seamlessly integrated into a VQ-VAE framework, enabling the partitioning of demonstrations into semantically consistent sub-trajectories, 
fulfilling the purpose of discovering manipulation concepts and the corresponding sub-goal (key) states. 
We evaluate the effectiveness of the learned concepts by training policies that utilize them as guidance, demonstrating superior performance compared to other baselines. 
Additionally, our discovered manipulation concepts compare favorably to human-annotated ones while saving much manual effort. 
{\color{brilliantrose} Our code is available at:
\href{https://zrllrz.io/InfoCon\_/}{\texttt{https://zrllrz.io/InfoCon\_/}}}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This manuscript proposed InfoCon, a framework that can discover concepts in manipulation tasks automatically based on information reuseness. Specifically, the authors designed an analysis system that outputting discretized concepts from an offline manipulation dataset using a few different losses: generative goal loss, discriminative goal loss. Also, the side product from the architecture is the derivative of the discriminative loss, which represents the action to perform in order to complete the task.

### Strengths
1. The manuscript is nicely written. I can follow most of the parts.
2. The evaluation covers a medium size of tasks and dataset, which is not perfect (not large-scale) but I believe is enough for showcasing in robot learning area.
3. The results look impressive that beat previous method marginally, achieving either the first or second best result in the whole table.

### Weaknesses
See question.

### Questions
1. I am a little bit confused about the motivation of discriminative goal loss. How is it trained and why it is useful for extracting information from the input states?
2. I am not fully confident about the fairness of the comparison. It seems to me that methods including LLM+CLIP are zero-shot learning process that does not require the training data to be seen. Am I correct or it's actually not the case? If so, I would suggest to separating them in the comparison. However, I still think the proposed method has technical contributions that is worth to present.
3. Is there any real-world example to indicate the effectiveness?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose using vector quantization to discretize robot manipulation trajectories into sets of discrete sub-trajectory encodings that maximize proposed metrics on discriminative and generative informativeness.

### Strengths
The paper is well written and the motivations and technical details are clear.  There are detailed evaluations and the proposed method is compared to multiple SOTA approaches.  The authors also include an ablation study and highlight a comparison of of human interpretability in addition to policy performance.

### Weaknesses
How do the authors feel about the interpretability of manipulation concepts for human robot interaction?  Learned concepts may not be as understandable in an interaction.  I am curious about an opinion on being able to map the learned concept back to a semantic concept or how that can be integrated into the objective.  I know human intuition is covered in Table 2, and the authors state there is a weak correlation with policy performance, but there may be cases where the goal is to optimize for both.

In section 2, "partition each trajectory into semantically meaningful segments" should this be clarified on what "semantically meaningful" means?  This goes with the earlier stated motivation of moving away from human semantic discretization into self-discovered discretization that optimizes discriminative and generative informativeness.

For eq 1, how does the observed state sequence factor into the generative goal?

### Questions
See weaknesses

### Soundness
3 good

### Presentation
4 excellent

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
This work, InfoCon, uses self-supervised learning method to discover the manipulation concepts in robotic tasks. The concepts are verified with semantic meaning in terms of human linguistics while saving much manual annotation efforts. This can be used as auxiliary task to support the encoding in the policy optimization. Experiements demonstrate that the policy trained based on these learned concepts can achieve the state-of-the-art results.

### Strengths
1. InfoCon can be self-supervised given state-action trajectory without human annotation, guided by network architecture VQ-VAE and informativeness objectives. Surprisingly, the self-supervised key states even performs better than the human GT in the COTPC for policy generation.

2. The robot with InfoCon can discover abstract concepts themselves other than struggling with the grounding of concepts that are manually defined.

3, The concepts of generative goal and discriminative goal are novel and beneficial to the trajectory encoding, which serves as the auxiliary task for self-supervision.

4. Strong results in simulation comparing to extensive baselines.

### Weaknesses
1, The proposed approach and concept of self-supervised manipulation concepts and key states seems closely related to the COTPC, as COTPC needs the key states. However, in the method description, there is no mention of COTPC. It may be possible to achieve co-optimization between policy generation and self-supervised manipulation concept. Moreover, can the proposed approach be general beneficial to policy optimization beside COTPC?

2. The experience portion is a bit weak where only few tasks are evaluated. For the baseline, it should also include COTPC + other manipulation concept discovery for fair comparison.

3. Lack of real robotic experiments. It is hard to judge if the proposed self-supervised approach works for the real-world complex tasks and videos.

### Questions
1. As generative models, there are many VAE variants. Can you explain why you choose VQ-VAE architecture or include ablation study?

2. As mentioned in the paper: the manipulation concept, key state, and state are random variables depending on the trajectory. Does the initialization of these variables affect the experimental results? Or other prototype network approaches help?

3. How about the generalization capability of InfoCon? In the paper, the training and testing tasks are same: P&P Cube, Stack Cube, Turn Faucet and Peg Insertion.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method for extracting different manipulation concepts (i.e. grasp, align, insert) from expert trajectories of robot manipulation tasks. In essence, the algorithm unsupervisedly learns relevant subgoals to accomplish a task, and in addition, also provides a gradient signal for actions to achieve these (sub)goals. This is done by training two components: predicting the next subgoal given the current state, and training a compatibility function that indicates how "compatible" a state is with the desired subgoal, using contrastive learning. The gradient of the compatibility function can then be used to select actions, i.e. which action increases the goal compatibility given the current state. The method is evaluated on 4 tasks of the ManiSkill2 benchmark, and some qualitative examples are provided of the discovered subgoals.

### Strengths
- Interesting ideas and approach to go from expert trajectories to subgoals, and in addition obtain policies to accomplish those subgoals.

### Weaknesses
- The experimental results don't provide standard deviations, which makes it difficult to assess if there is any significant improvement compared to the presented baselines.

### Questions
- What are the standard deviations on the results in Table 1. To what extent is InfoCon actually significantly better than the other baselines?

- For some tasks (i.e. P&P Cube) the GT key states underperform the other approaches. Any insight on why the ground truth key states are insufficient to efficiently execute the task, and which are the "extra" subgoals identified by InfoCon that might explain this gap?

- The model is trained on only 500 trajectories. To what extent is this overfitting to the train set, and does this explain the large gap between seen and unseen scenarios? Would this gap be closed by just adding more trajectories?

- The VQ-VAE is pretrained on the trajectories without any task-related signal. Hence, the learned subsequences are merely clustered by visual appearance, rather than semantic relevance of being a valid "subgoal" for a task?  Wouldn't it make sense to also adjust the codes in the codebook based on e.g. how good one can predict a particular goal and/or how well-behaved a compatibility function is?

- The policy is conditioned on the current state and the gradient of the compatibility function. Wouldn't it make sense to also condition the policy on the goal state, i.e. similar to e.g. https://arxiv.org/abs/2211.13350

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
