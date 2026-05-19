# RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches

- Decision: Accept
- Scores: 8, 8, 5

## Abstract
Generalization remains one of the most important desiderata for robust robot learning systems. While recently proposed approaches show promise in generalization to novel objects, semantic concepts, or visual distribution shifts, generalization to new tasks remains challenging. For example, a language-conditioned policy trained on pick-and-place tasks will not be able to generalize to a folding task, even if the arm trajectory of folding is similar to pick-and-place. Our key insight is that this kind of generalization becomes feasible if we represent the task through rough trajectory sketches. 
We propose a policy conditioning method using such rough trajectory sketches, which we call \methodname, that is practical, easy to specify, and allows the policy to effectively perform new tasks that would otherwise be challenging to perform. We find that trajectory sketches strike a balance between being detailed enough to express low-level motion-centric guidance while being coarse enough to allow the learned policy to interpret the trajectory sketch in the context of situational visual observations. In addition, we show how trajectory sketches can provide a useful interface to communicate with robotic policies -- they can be specified through simple human inputs like drawings or videos, or through automated methods such as modern image-generating or waypoint-generating methods. We evaluate \methodname at scale on a variety of real-world robotic tasks, and find that \methodname is able to perform a wider range of tasks compared to language-conditioned and goal-conditioned policies, when provided the same training data.
Evaluation videos can be found at \website.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes to abstract robot policies via rough sketches. The paper identify sketeches as a modality that is concise but yet expressive enough to represent a task, and allow for generalisation to novel tasks. The trajectory sketch in question in projected into the view of a calibrated camera. The paper explores when the trajectories are hand-drawn, derived from demonstration videos, prompted from LLMs, and generated from image generation models.

The paper is highly novel in using sketches as the abstraction for which tasks are conditioned on, and, by extensive experimental results, show the benefits of this representation for policy learning. The method appears sound, and the reviewer also appreciates the detailed evaluation on real world robot experiments and the discussion on emergent capabilities -- the retry behaviour was particularly interesting to observe. A question that might be interesting to ponder about is: does the smoothness or other property of the trajectory affect the quality of the task conditioning? Although abstracting the task as a sketch and conditioning on it is novel. The reviewer would like to point out that there have been previous attempts at leveraging human sketches to provide robot demonstrations in a paradigm known as "diagrammatic teaching" (https://arxiv.org/abs/2309.03835; https://openreview.net/forum?id=6cUysxHoL1), and should be viewed as related work.

Overall, this paper is novel, the method is sound and convincing with a solid amount of real robot experiments. The usage of trajectory sketches as a way of specifying tasks has the potential to produce many new oportunities in robot learning.

### Strengths
See above

### Weaknesses
See above

### Questions
See above

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes to use a rough trajectory of the end-effector in the image space as a way of task specification. This enables more flexible task specification during inference time, including a human drawing, with a human video demonstrating the task, or from LLM output. Experiments validate the effectiveness of the method and additionally demonstrate a small amount of motion generalization.

### Strengths
1. The paper is well-motivated, with a simple but effective modification to task specification. The paper makes a meaningful contribution to the literature and is well executed. 
2. The paper is well presented, with good writing and visuals.

### Weaknesses
1. Generating the trajectory itself might not be trivial. For example, in the case when a person draws the trajectory, the person needs to understand the trajectory of the end-effector (including any joint limits) and project it to a 2D space. This can become a bottleneck, especially for more difficult tasks (e.g. large-range motion, long-horizon tasks). More analysis of the robustness of the trajectory specification could strengthen the paper. 

2. As mentioned in the limitation section already, the method seems to be limited to a fixed-view camera with calibration, limiting the applicability of the method.

### Questions
Figure 8 is confusing to me. From the left visualization, the query trajectories are well captured by the training trajectories, suggesting no extrapolation and mostly interpolation. On the other hand, the right part is difficult to understand. Can the authors clarify or change the claim accordingly?

### Soundness
3 good

### Presentation
3 good

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
This paper proposes an approach to task specification based on providing, at test time, an approximate trajectory to accomplish the task. More specifically, the trajectory is provided as a 2D image, representing the projection on the camera of the end-effector position, the interaction points (where the gripper should be opened and closed), and possibly the height of the end effector. I see the approach as an instantiation of the general problem of trajectory tracking under constraints. The main contribution is adapting this idea to make it compatible with sensorimotor models and imitation learning. The approach is evaluated over multiple experiments in the real world, where it outperforms baselines without test-time goal conditioning and end-goal conditioning only.

### Strengths
The main strengths of the paper are:
1. The proposed approach, despite being a small extension of the well-known body of literature on trajectory tracking, is original. Using a trajectory to define the task at test time is the default for all control systems. The fact that the trajectory is not feasible is generally not a problem for feedback systems (See Borrelli et al., Predictive control for linear and hybrid systems). However, representing such a trajectory as an image and conditioning a model on it is an interesting idea.
2. While I don't agree with some of the experimental setup (more on this below), I found the analysis on trajectory conditioning (Sec 4.3) and measuring generalization (Sec. 4.4) to be quite interesting and well executed.
3. The paper writing is very good and easy to follow. The figures help in understanding the core concepts.

### Weaknesses
The main weaknesses I see are:
1. The paper does not make a strong enough connection between the traditional idea of trajectory tracking and the proposed approach. For example, there is no section in the related work covering the history of this technique and its recent applications to robot learning. As mentioned above, I still see some innovations in the proposed approach (sensorimotor controllers are generally conditioned on a low-dimensional trajectory, not an image of it)—however, this lack of perspective results in overclaiming the system's novelty.
2. The comparison against baselines in Sec 4.2 is not apples to apples: while the proposed approach gets an input a trajectory on __how__ to complete the task, the other methods only access a higher level instruction (e.g. language), or the final goal represented as an image. It is, therefore, not surprising that with more and cleaner information, the proposed approach outperforms the baselines. I find the experiments in Table I to be much more informative. They show that when the trajectory is very coarse, e.g. when drawn by a human, the proposed approach can track it better than the off-the-shelf IK. However, these results also show that the approach is, on average, worse than generating a trajectory with a VLM and tracking it with an IK, which somehow is against the main paper's contribution.
3. Each subsection seems to evaluate on different "tasks", and it is unclear how the task selection is done. For example, why change the task from 4.2 to 4.3? And why even change it in the comparisons of Table 1? Note that my point is not that the task were handpicked, but rather that this dynamics makes drawing insights from experiments challenging.
4. The paper has as its main claim generalization. Still, its main experiments on generalization over scenes and tasks only occupy a small part of the paper (Sec. 4.5). At the very least, this part should become quantitative since this is what would back up the claims on generalization.

Some rather minor limitations:
1. The ordering of Fig. 2 seems rather arbitrary. For example, in my subjective opinion, I see trajectory and code to be much closer than what is shown right now. Therefore, either more justification is needed, or the figure should be removed. 
2. The approach makes strong assumptions that contradict the claim on scalability. Specifically, the two main assumptions are: (1) the camera should be static at training and test time, as well as fully calibrated, and (2) the end effector should always be visible in the camera. This makes data collection and evaluation very challenging and limits the set of tasks that can be done.
3. In Fig. 8, I don't get what "unrelated semantic categories" mean for a low-level skill. At the level of trajectory, why is generalization over semantics a question? Isn't it obvious due to the abstraction of the skill? Or did I misunderstand the meaning?

### Questions
The main actions to improve the paper are in my opinion:

1. Better positioning of the work with respect to previous literature.
2. Motivation behind task selection
3. Quantitative experiments in the setup of Sec. 4.5

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
