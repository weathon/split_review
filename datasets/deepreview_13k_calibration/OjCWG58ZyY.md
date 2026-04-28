# Goal-Conditioned Reinforcement Learning with Virtual Experiences

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6

## Abstract
Goal-conditioned reinforcement learning often employs a technique known as Hindsight Experience Replay (HER) for data augmentation by relabeling goals. However, HER limits goal relabeling to a single trajectory, which hinders the utilization of experiences from diverse trajectories. To address this issue, we present a curriculum learning method to construct virtual experiences, incorporating actual state transitions and virtual goals selected from the replay buffer. Considering that virtual experiences may contain a lot of noise, we also propose a self-supervised subgoal planning method that guides the learning of virtual experiences by imitating the subgoal-conditioned policy. Our intuition is that achieving a virtual goal may be challenging for the goal-conditioned policy, whereas simplified subgoals can provide effective guidance. We empirically show that the virtual experiences from diverse historical trajectories significantly boost the sample-efficiency compared to the existing goal-conditioned reinforcement learning and hierarchical reinforcement learning methods, even enabling the agent to learn tasks it has never experienced.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposes a variant to hindsight experience replay (HER) methods for GCRL that improves the quality of hindsight-relabeled goals using a high-level subgoal proposal policy, and additionally uses a task density model to produce better curricula of goals to reach. On a few RL benchmarks (AntMaze, Reacher, Sawyer), this method shows substantial improvements over existing GCRL methods.

### Strengths
- Lots of interesting ideas presented: hierarchical policy for proposing subgoals for the hindsight experience relabeling; density model for designing good subgoal curricula; imitation regularization objective using subgoal-policy; p-norm for generating subgoal sequences
- The method outperforms prior online GCRL methods on several tasks (AntMaze, Sawyer, Reacher), showing strong performance

### Weaknesses
 - There are many moving parts to this method which aren't ablated (the "three key ways" mentioned at the start of Sec. 4 seem to be relatively distinct algorithmic decisions that should be ablated). Specifically, the impact of the high-level subgoal proposal policy, the task density model for curriculum learning, and the imitation regularization objective are not independently evaluated. It's unclear how much each contributes to the overall performance gain. For example, the benefit of using the p-norm for generating subgoal sequences is not isolated from the other components.
- I found the method presentation to be confusing, in particular how the various components (like "task-probability-density-based curriculum learning" and "subgoal planning" relate). The paper lacks a clear, step-by-step explanation of how these components interact during training. The description of the task density model's role in curriculum learning is particularly vague, and it's not clear how it influences the selection of goals for relabeling.
- Minor formatting issues: use \citep{} for parenthetical citations, the green citecolor is a bit hard to read

### Questions
- Can $1<p<2$ be used in the p-norm for subgoals? When might $p=\infty$ be suboptimal?
- In Fig. 12, most of the proposed subgoals appear very close to the goals
- Is there a theoretical justification for why imitating the subgoal-generating policy in eq. (9) is beneficial?
- Likewise, is there any mathematical statement that can be made for why this goal relabeling approach is superior to HER?
- How exactly is the task density model used for curriculum learning? This seems to be an important component to the method (Fig. 10), but I didn't understand how it fits into, e.g., Eqs. (5) and (7).
- What is the justification for the direction of the KL divergence in Eq. (9)? What is $\pi^{\text{prior}}$?

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper studies goal-conditioned reinforcement learning, and proposes an approach that 1) learns with a curriculum of relabelled goals, and 2) distills learned behavior for reaching s-> subgoal to learn a model that can reach s -> goal. Across a number of state-based environments, the authors find that the proposed approach significantly outperforms past hierarchical approaches and other GC methods.

### Strengths
The goal-conditioned learning problem setting is an important one in reinforcement learning, and this paper offers a nice way of reducing its complexity. I particularly found the idea of distilling policies from a subgoal to a further goal to be a nice one, especially that it helps propagate information that can cleanly be learned at small scales to help shape the noisier long-horizon learning problem.


The results are very thorough: the benefit seems relatively compelling on the studied domains, and the different components of the algorithm are very well ablated. the two different components of the algorithm are well-ablated.

I found the use of visualizations throughout the paper to be useful to help understand the proposed method in the paper -- the visualizations in Figure 5 were particularly useful.

### Weaknesses
The importance of the curriculum is not clear to me: for one, it introduces much additional complexity (e.g. the need to train a Flow or RealNVP model, whose details are not well discussed in the paper), it provides seemingly little benefit (in Figure 7, middle), and requires special hyperparameters (e.g. (0.8, 1.2) for state density clipping).

The paper only studies relatively simple state-based domains with intrinsic 2d structure, and most of the analysis is on Antmaze (which has a clear 2d structure, even if this is not the axis being measured) -- this is particularly worrisome, since the high-level policy learning problem gets more complicated in higher dimensional state spaces, and it is unclear how this method generalizes. The paper would be stronger if it had a more complex state-based environment  (e.g. one may consider Franka Kitchen or CALVIN)

Section 4.2 is difficult to follow: it introduces additional notation for the sub-goal sequence that is not explained clearly, and it is not clear whether the mechanism being used is an A2C-like (A2C updates using policy gradient estimates) or if it is AWR-like (which seems to be the form of Equation 8).

Nit: The paper begins the methods section (Section 4) describing how the framework differs from Kim et al, 2023 -- the paper to this point has no description of Kim et al, nor is it made clear prior to this point that the method is building on top of Kim et al, 2023. Especially for readers who are unfamiliar with this work, it would be useful to describe the paper in greater detail in related work, or perhaps softly introduce the ideas in Kim et al otherwise in the paper.


Minor:

Would be good to have non-abbreviated captions in the Figures (e.g. in Figure 7)
The paper has several typos throughout:

Misuse of \cite or \citet instead of \citep throughout the paper
Figure 4 -> Enveronment -> Environment
L893: Swayer -> Sawyer

### Questions
1. Why does selecting all virtual goals cause the method to fail? (in Fig 7)
2. It is common in hindsight GC implementations to (with some proportion) sample a goal at random from the replay buffer. This alleviates a lot of the challenges with otherwise only choosing goals on the same trajectory. Is this being done for the baselines (specifically for SAC+HER?) 
3. In Equation 9, it seems that $k$ is being overloaded both as an iteration index (e.g. theta_{k+1}), and also as the subgoal index?

### Soundness
3

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
Goal-conditioned environments are MDPs where the policy reward aligns with reaching a given end goal. The sample complexity of such problems can be significantly reduced with augmentation techniques such as hindsight experience replay (HER), where visited states in a trajectory are relabeled as goals and used to augment the policy training procedure. This work suggests an expanded augmentation, that broadly aims to break the goal-based task to several sub-goals using a higher level policy, and learn reaching the sub-goals using a lower level policy. The high-level policy can be trained directly with the value function of the lower level policy.

### Strengths
* The idea of a high-level policy learning the sub-goals directly is elegant.
* The evaluations show a wide gap between the proposed approach and baselines.

### Weaknesses
I'm fond of this work, but there are several things I found concerning. An explanation by the authors could potentially be helpful.

* While §4.2 and §4.3 were well-written, I found §4.1 very hard to grasp.

    What is $j$, and why is it that if $i=j$, Eq. 5 is equivalent to Eq. 4? What is the "task probability density" trying to learn? What does the condition (e.g., the range filter) mean from a high-level perspective? Why would there be a "lack of connection between state transitions", as described in line 238? It doesn't seem like state transitions are being tinkered with in Eq. 5.

    Overall, I would suggest a major rewrite of this section.
* How was VE tuned for the experiments in §5.2? It seems like VE was tuned per each environment separately, but how was this done without tuning on the "test" problem (the goal conditioned environment that you evaluate on)?

Some minor nitpicks:
* Several "Swayer" typos: Figure 3, F.2, etc.
* There is no $j$ in Eq. 5.

### Questions
* How was VE tuned? This is related to the weaknesses comment I made.
* What is the main difference between this work and other works that employ sub-goals? Is it that other works attain sub-goals without learning (e.g. the midpoint, bisection or graph-based methods)?
* Are there any ablation experiments that show the effectiveness of Eq. 9 in §4.3? If I understood correctly, Eq. 9 played the role of a soft regularization over the policy. It would be interesting to show how important it is, but I could not find it in §5.3.
* I found it difficult to get a final takeaway from Figure 5. Did I miss something? Is there any information we can deduce from it?
* In line 317, it is stated that "we use a entire 31-dimensional state space as the goal space". Why? Without justification, this comes off as an arbitrary decision. Even if the reason is trivial, it would be helpful to mention it somewhere, or link to an explanation in the appendix.
* What is the concrete definition of "Uniform smoothing" in line 357? Either a citation is needed, or a reasonable technical explanation. Otherwise it is difficult to know what artifacts might have been caused by the smoothing.

### Soundness
3

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
This paper proposes a novel framework called Virtual Experience (VE) that leverages curriculum learning and subgoal planning to improve sample efficiency and tackle long-horizon tasks. It uses task-probability-density-based curriculum learning and self-supervised subgoal planning. VE integrates low-level skills from diverse experiences to improve exploration efficiency, especially for long-horizon tasks with sparse rewards. The experiments demonstrate VE's superior performance in navigation and robotic control tasks, significantly boosting sample efficiency and handling complex tasks that require multiple goals. The paper also explores the balance between actual and virtual experiences in optimizing learning.

### Strengths
* This paper provides extensive experimental validation in a variety of environments.
* The authors offer comprehensive visualizations and a detailed experimental setup.
* This paper extends the HER method with virtual experience from the whole replay buffer, offering a more flexible approach to goal relabeling.

### Weaknesses
 * Several formula symbols are not clearly presented, which significantly hinders readability and comprehension.
* The paper assumes that virtual goals can be useful without fully addressing the potential for introducing noise or unrealistic transitions. The framework’s reliance on implicit curriculum learning to mitigate this issue may not be effective in more complex, real-world settings where noise cannot be easily filtered out. Specifically, the method does not explicitly account for the discrepancy between the distribution of real transitions and the distribution of virtual transitions, which could lead to instability or suboptimal performance. The paper also lacks a clear discussion on how the task probability density is estimated and how sensitive the performance is to the accuracy of this estimation. This is a critical point because if the density estimation is poor, the subgoals selected might not be meaningful, and the virtual experience could be detrimental.

### Questions
* I do not fully understand how subgoals are selected based on task probability density $e$ for curriculum learning.
* I am confused why introducing only a single subgoal (i.e. $k=1$) in AntMaze yields the best results.
* Can the entire framework be adapted to integrate different lower-level off-policy algorithms, such as HER?

### Soundness
3

### Presentation
2

### Contribution
2
