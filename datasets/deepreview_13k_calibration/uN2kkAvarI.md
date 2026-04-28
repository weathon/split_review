# ViVa: Video-Trained Value Functions for Guiding Online RL from Diverse Data

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 5, 3

## Abstract
Online reinforcement learning (RL) with sparse rewards poses a challenge partly because of the lack of feedback on states leading to the goal. Furthermore, expert offline data with reward signal is rarely available to provide this feedback and bootstrap online learning. How can we guide online agents to the right solution without this on-task data? Reward shaping offers a solution by providing fine-grained signal to nudge the policy towards the optimal solution. However, reward shaping often requires domain knowledge to hand-engineer heuristics for a specific goal. To enable more general and inexpensive guidance, we propose and analyze a data-driven methodology that automatically guides RL by learning from widely available video data such as Internet recordings, off-task demonstrations, task failures, and undirected environment interaction. By learning a model of optimal goal-conditioned value from diverse passive data, we open the floor to scaling up and using a wide variety of data sources to model general goal-reaching behaviors relevant to guiding online RL. Specifically, we use intent-conditioned value functions to learn from diverse video and incorporate these goal-conditioned values into the reward. Our experiments show that video-trained value functions work well with a variety of data sources, exhibit positive transfer from human video pre-training, can generalize to unseen goals, and scale with dataset size.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This submission proposes ViVa (Video-trained Value Functions), a method that learns goal-conditioned value functions from diverse video data (from Ego4D + environment-specific data) to develop an intent-conditioned value function (Ghosh et al., 2023) to guide the agent during online RL in sparse-reward settings.

### Strengths
- The paper is well-motivated and easy to understand.
- I appreciate that the authors used multiple seeds for their experiments and clearly stated the hyperparameters for all experiments to ensure reproducibility.

### Weaknesses
The paper, in its current form, lacks in certain areas outlined below:

1. While the authors report results over multiple seeds, the plots do not show standard deviation or error bars. This makes it difficult to assess the algorithm’s sensitivity to underlying hyperparameters and to compare the approach fairly with other algorithms like JSRL in Fig. 4 or RLPD in Fig. 5. I urge the authors to also show standard dev. / error for a fair comparison. The presentation of the results makes it difficult to ascertain the statistical significance of the reported gains. The absence of error bars or shaded regions representing standard deviation obscures the degree of overlap between the performance of ViVa and the baselines, making it hard to judge the robustness of the method.
2. The presentation of all plots and figures could be improved by increasing the font size of the x- and y-axis ticks, as well as by enlarging the images in Figure 7. Currently, these are not readable in printed form or even when zoomed in on a laptop screen.
3. When reporting rewards in Figures 4 and 5, do the authors run the agent for multiple trials in the evaluation environment (e.g. 100 trials) and then report the mean or median? Or is the agent run only once? These details are necessary to support the SOTA performance claims. The evaluation protocol needs to be clearly defined, including the number of evaluation episodes and whether the mean or median is reported. Without this information, it is impossible to assess the reliability of the reported performance.
4. Equation 4 combines the equations for loss to be minimized with the advantage function being estimated. Separating these two components would improve readability. The current form of Equation 4 makes it difficult to understand the individual components of the loss function and the advantage estimation. Separating these would improve clarity and facilitate a better understanding of the method.
5. No training curves are provided for the Ego4D video pre-training or the online RL fine-tuning phases. Additionally, the exact pre-processing steps for Ego4D videos should be specified to enhance the reproducibility of the approach. The lack of training curves for both pre-training and fine-tuning stages makes it difficult to assess the convergence and stability of the learning process. Furthermore, the absence of detailed pre-processing steps for Ego4D videos hinders the reproducibility of the experiments.
6. Minor: There is no discussion of computational costs or training times.


Overall, while the approach (ViVA with Ego4D) appears slightly more sample-efficient than other baselines, the results do not seem particularly promising. I would like to see details on the amount of effort (in terms of time and computational resources) required for pretraining on Ego4D, followed by fine-tuning, and finally training the agent for ViVA as well as the training time for RLPD and JSRL. If the effort is substantial, then the gains do not seem meaningful enough, as it appears that using Ego4D makes only a slight difference in the downstream task.

Therefore, I recommend a rejection but would be willing to reconsider my score based on the authors' rebuttal.

### Questions
1. On page 4, lines 201–205, the authors mention using a monolithic function instead of a multilinear formulation to learn the ICVF network. Are there any empirical results that the authors could share for this choice on at least one of the environments?
2. On page 5, in the *Guided Online RL* section, the authors state that they use 50% of online data from the replay buffer and 50% sampled from the prior dataset. Is there an ablation where the authors sampled only from the replay buffer (i.e., 100%) without any prior data?
3. Since the Ego4D dataset can include videos from multiple viewpoints, do the authors apply any pre-processing to make the ICVF agnostic to camera angle?
4. On page 7, line 348, it says "Appendix 2," but it should be corrected to "Appendix 8.2."
5. Typo:
    - Page 4, Line 206: “we working” → “we **are** working”

### Soundness
2

### Presentation
2

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
This paper introduces a method called “ViVa” for pre-training intent-conditioned value functions (ICVF) on video datasets and then using the resulting value function to guide online RL in sparse reward settings. To do so, the authors define a goal-conditioned reward function that is -1 for all states except the goal state, where it is 0. Based on this, they then define an ICVF which models the unnormalized likelihood of reaching some outcome state from some starting state while following an optimal goal-reaching policy for a goal (intent) state. By setting the outcome state equal to the goal state they obtain a value function corresponding to the (negative) temporal distance to the goal state.

The authors pretrain this model on 3000 hours of internet video data, finetune it on environment-specific (but not task-specific) data, and then use the final value function to augment the environment’s reward function in online RL. They show that their approach performs favorably compared to several baselines (RLPD, SAC, JSRL).

### Strengths
- The paper makes a significant contribution to the approach of using internet-scale video data for pre-training RL models in order to improve the performance/data-efficiency of downstream RL. The comparison to baselines is fair and the experiments convincingly demonstrate the effectiveness of ViVa. I appreciate that the authors specifically included experiments to evaluate generalization and scaling properties of ViVa, in addition to evaluating performance.
- The related work section is generally comprehensive (with one caveat discussed below).
- The discussion section was very interesting, I particularly liked:
  - the comparison between ViVa and imitation policies w.r.t. generalization
  - and the proposed method for resolving value errors by collecting counterfactual examples with an exploratory policy
- The paper is well written and the presentation is good.

### Weaknesses
I would be happy to raise the score pending clarification/discussion of some of the concerns below.

**1. Discussion of imitation learning methods:**

The chosen baselines as well as the related work section focus on methods for learning value functions from videos. One closely related line of work that is omitted (both as a baseline as well as in the RW) is the approach of learning policies directly from video data, e.g. with latent policy imitation methods such as ILPO (Edwards et al. 2019), LAPO (Schmidt et al., 2023), Genie (Bruce et al., 2024), LAPA (Ye et al., 2024).

Relatedly, the authors claim
> Our analysis of ViVa illustrates the importance of using value function pre-training on video data as
opposed to other methods of utilizing prior data.

> Comparisons with JSRL further depict the superiority of value functions as a representation of prior
data as opposed to imitative policies.

I don't believe these claims are sufficiently supported by their results since (1.) they are based on a single method for imitative policies, JSRL, and (2.) crucially this method does not actually use the prior video data (Ego4D). The authors also state: 
> Furthermore, imitative policies prevent support from action-free data sources such as Ego4D.

However, this limitation only applies to classical imitation learning methods (and JSRL), but not to methods for latent imitation from video.

Overall, based on the results shown, I believe the authors could argue for the importance of leveraging prior action-free video data, but would not be able to conclude that value function learning methods are generally superior to policy imitation methods.

**2. Other environments:**

The paper includes experiments on several robotics control environments (from RoboVerse, FrankaKitchen, AntMaze). I would be very interested in results from non-robotics environments, although I understand if that is beyond the scope of this paper.

**3. Minor issues:**

- Figure 1 is unclear: this is the first point where `s`, `s'`, `s+`, and `g` are used in the paper, but they haven't been defined yet.
- In the Figure 1 caption and also Section 4 it's a bit unclear what the difference between "future outcome", "intent", and "goal" is, plus it wasn't immediately obvious that all of those are states.
  - If intent and goal is the same thing (as is suggested in Sec 4.1), it might be better to stick to one of the two terms
  - To standardize the terms, I'd suggest using `current state` (`s`), `next state` (`s'`), `outcome state` (`s+`), `goal state` (`g+`)

### Questions
1. Could you clarify how exactly you performed environment finetuning? From Section 4.3, it is not entirely clear whether finetuning works exactly the same as ICVF pre-training (just on a different dataset), or whether this uses some ground-truth environment rewards to update the VF?

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
This paper proposed a novel intrinsic reward method for sparse reward RL tasks. The intrinsic reward is derived from a goal-conditioned value function that is trained on Internet-based task-unrelated videos. The authors proved that the proposed ICVF could empirically help task training and performance. The method could promote RL's application in real-world tasks.

### Strengths
1. Although leveraging knowledge in internet large-scale videos and intrinsic reward are not fresh ideas, the authors design a framework that combines them and benefits sparse-reward RL.

### Weaknesses
1. This paper lacks theoretical analysis, especially the convergence of policy improvement and policy optimality after adding the intrinsic reward term.
2. What's the performance if removing all the sparse environment rewards?
3. Could you provide more comparisons with related baselines like FAC(Foundation Actor-Critic)?

### Questions
See above.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work proposes ViVa to learn prior knowledge from large-scale video datasets and then fine-tune on in-domain data. It encodes the video to representations first and then uses shallow MLP layers to output the value function.

### Strengths
* An ablation study is conducted.
* Deep studies help investigate the succeed of the method on tasks (Fig. 2 and 7).

### Weaknesses
 * The experiments are all in simulators, not in the real-world. It is unclear how the ViVa works on real-image tasks.
* Mathematical formulation is unclear (see questions).
* In corrupted AntMaze, JSRL is better than ViVa. Why is that, and what is the point of conducting the experiment then?
* In the setting of demonstrations with rewards, the author should compare it with more baselines, such as Adril. In the setting of demonstrations without rewards, the author should compare against methods that learn a world model like Dreamer.

# Minor:
* incorrect use of ” ”,  use “” (line 43)
* no space before whereas (line 129)
* when COG first appears, it is not defined.
* “Figure” 5 in line 397.
* start appendix with section A.

### Questions
* See weakenss1
* How do we intuitively understand why V-PTR is less performant than ViVa?
* What is f in line 207?
* Is equation 4 minimizing over V theta? And the second line is st.t?
* What is the difference between RLPD and ViVa in Antmaze? They all only learn from the demonstrations.
* isn’t the marginal increase in performance in Figure 6 indicating that there is no need for heavy pre-training? As stated in the limitation, “RoboVerse is significantly different than Ego4D”, so the pre-training phase only makes sense for relevant tasks to Ego4D. I believe further investigation is needed to look into this relevance, which again might be relevant to the gap between simulators and the real world.
* Following the previous, this work motivates the use of Internet-scale datasets to accelerate learning in the abstract, but some experimental results support the opposite view. If not using the Internet-scale datasets, I do not see how this work separates from other works on imitation learning.

### Soundness
2

### Presentation
2

### Contribution
2
