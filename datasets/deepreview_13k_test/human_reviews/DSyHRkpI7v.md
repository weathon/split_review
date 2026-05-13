# Leveraging Sub-Optimal Data for Human-in-the-Loop Reinforcement Learning

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
To create useful reinforcement learning (RL) agents, step zero is to design a suitable reward function that captures the nuances of the task. However, reward engineering can be a difficult and time-consuming process.  
Instead, human-in-the-loop (HitL) RL allows agents to learn reward functions from human feedback. Despite recent successes, many of the HitL RL methods still require numerous human interactions to learn successful reward functions. 
To improve the feedback efficiency of HitL RL methods (i.e., require less feedback), this paper introduces Sub-optimal Data Pre-training, SDP, an approach that leverages reward-free, sub-optimal data to improve scalar- and preference-based HitL RL algorithms. In SDP, we start by pseudo-labeling all low-quality data with rewards of zero. Through this process, we obtain ``free'' reward labels to pre-train our reward model. 
This pre-training phase provides the reward model a head start in learning, whereby it can identify that low-quality transitions should 
have a low reward, all without any \emph{actual} feedback. 
Through extensive experiments with a simulated teacher, we demonstrate that SDP can significantly improve or achieve competitive performance with state-of-the-art (SOTA) HitL RL algorithms across nine robotic manipulation and locomotion tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The submission proposed a simple framework, namely Sub-optimal Data Pre-training (SDP), that leverages reward-free, suboptimal data to warm-start the reward model as well as the RL agent replay buffer. Through simulation experiments with both simulated teacher policy and real human subjects, the authors claim that the proposed SDP can significantly improves the efficiency of human feedbacks under Human-in-the-loop (HitL) reinforcement learning setting.

### Strengths
- The main idea of this submission is straightforward and intuitive. Utilizing sub-optimal data is a popular way to improve sample efficiency.
- The submission is well-written and easy to follow. Visualizations are clear and helpful.
- The demonstrated experiments are reasonably comprehensive, invluding robotic locomotion and manipulation tasks.
- The submission includes a 16-people human subject study.
- The result analysis is well-formulated with multiple seeds and significant tests.

### Weaknesses
- My main concern about the submission is that the contribution is incremental without significant advance. Leveraging a set of sub-optimal data generated with randomly initialized policy as a warm-start for the reward model is straight forward, and seems to me the only major contribution. The authors follow the standard RLHF framework such as Bradley-Terry model, etc. This work failed to address any of the existing challenges, such as the assumption of linear reward feature combinations, the assumption of Boltzmann rationality of the human demonstrator, etc.

- I remain somewhat unconvinced in the claim made in line 205 - line 210. Pseudo-labeling all low-quality transitions with the same minimum environmental rewards indeed introduces bias into the reward model, and will further lead to reward ambiguity. The empirical results in the DMControl suite is not sufficient to claim that the bias for using an incorrect reward is low. In fact, I doubt the effectiveness in pseudo-labeling low-quality samples in more complex real-world robotic tasks with higher dimensions. It would be helpful if the authors can include additional experiments on higher-dimensional simulation or real-world experiments to showcase the effectiveness.

- The authors took a great effort to include a well-formulated human subject study. I don't think it deserves any extra credits as the human subjects are only asked to compare two clips and provide preference labels, instead of provide direct interventions (learning from human intervention). I think the user study with diverse human subjects will be mostly useful if they can provide direct intervention and correction trajectories. A single preference label over two trajectory pairs might not fully reflect human's intention.

### Questions
- Can authors provide more thorough explanation on why introduced bias into the reward model will not affect the performance?
- Can authors explain why Deep Tamer is not learning at all in Figure 3?
- In Figure 6 Phase Ablation, what is the difference between SDP Agent Update Only and R-PEBBLE? Why SDP Reward Pre-train Only has better performance over SDP Agent Update Only? A more detailed explanation on the difference between these baselines will be helpful.

### Soundness
3

### Presentation
4

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Use reward-free sub-optimal data for pretraining human in the loop RL by adding a reward. The reward is trained by assigning the minimum environment reward to all states in the reward free suboptimal data, and iteratively adding interactions. The online interactions can be labeled either with preference-based RL or with scalar rewards. This suboptimal-data aware method is then evaluated over several experiments against other human in the loop algorithms.

### Strengths
The algorithm is straighforward.

The method is well explained and clear.

The empirical analysis is good.

Running human in the loop with human participants is admirable.

### Weaknesses
The assumption made in Equation 4 is quite restritive, since this states that the per-state reward must be low for every state in a suboptimal trajectory. There are many tasks for which a sub-optimal trajectory may receive significant non-trivial reward, suhc as achieving an intermediate goal, while still being significantly suboptimal. In addition, knowledge of the minimum environment reward can also be a limiting assumption, though less so.

The method may be a little bit too straightforward, as the concept of applying a small, fixed, low reward given to unlabeled interaction data has been explored in the offline/off-policy RL literature, which has a lot of overlap with human in the loop RL. Since the method proposes very little to convert this interaction data into the context of human in the loop, this makes the algorithm itself of low novelty. It seems like knowledge about the scale or type of human in the loop data (preference or scalar) would provide some insight into a better method for assigning the suboptimal data.

How does relabeling the suboptimal data with the preference learned rewards through training compare? This seems like a logical experiment that could provide insight into how much the suboptimality assumption can be relaxed.

While the baseline evaluation is extensive, it seems like a missing area are methods that utilize suboptimal data. As a comparison, pretraining with an offline RL method that can leverage suboptimal data smoothly would be preferred, at least as an upper bound on performance.

While user load is a serious concern, a participant study that investigated more complex domains, and experiments in more complex domains such as Franka Kitchen or 2D minecraft would illustrate the efficacy of this method. In these control tasks it is not particularly realistic to have a large amount of entirely reward-free data, whereas in a robotic kitchen this is more plasible. Since this method is fundamental, an experiment along this line would make sense.

### Questions
See Weaknesses

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
4

### Summary
The paper introduces Sub-optimal Data Pre-training (SDP), a method for improving human-in-the-loop reinforcement learning by pre-training reward models with sub-optimal, reward-free data to enhance feedback efficiency and performance.

### Strengths
1. This SDP approch is novel
2. This paper has some real world validation (human study)

### Weaknesses
1. The performance of the SDP method is highly dependent on the quality and representativeness of the sub-optimal data used for pre-training. Limited data availability or random policies generated from the same initial seeds can negatively impact SDP performance.
2. The human study in this paper did not account for human variance. For instance, would differences in education levels affect the quality of the labels?

### Questions
1. Is learning with the SDP method more effective than learning with sparse rewards?
2. Does SDP require more data for more complex environment?
3. How well does the SDP approach perform when applied to high-dimensional action or state spaces, such as humanoid?
4. Does the human teacher need to undergo training?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a method to initialize a reward network for RL with human feedback. Their method centers around using random exploration to then label sub-optimal trajectories with low rewards and therefore filter those state action pairs from exploration once the human preference phase begins. Their results show that this method is able to improve results in baselines and is agnostic to which human preference algorithm used.

### Strengths
Research Problem. The research problem is at a high level “how to use unlabeled data to warm start RL with human preferences”. Since human preferences (or even AI preferences) are a reasonable and increasingly common method for learning reward models as opposed to hand coding them improving such algorithms with cheap data is a good research problem.

Novelty. The novelty seems reasonable from the related work section.

Significance/Contribution. The significance of this paper is solid. It has a high practicality in many empirical applications and I am of the opinion that works that improve data efficiency are critical in RL research.

Algorithm Details. The algorithm itself isn’t extremely complex but the authors do a good job explaining it.

Experimental Selection. The experiments ran emphasize the point of the paper well. 

Presentation of Results. All figures are very well done and very clear.

Ablation Studies. Sensitivity study is done with hyperparams and shows relative robustness. 

Empirical Results. Good, results indicate this is a successful method and general strategy for improving preferences.

Failure Analysis. There is no failure analysis in this paper. I wish for the Rune + SDP baseline you would talk about why it doesn’t help in this case. Is there a particular part of rune that makes it work worse? In what future algorithms would this strategy not work.

Clarity is generally good. See weakness for improvements.

### Weaknesses
I think the related work section could be improved. I understand that this work is human in the loop RL but I feel the human in the loop RL section is lacking. None of this section is actually compared to this work and doesn’t emphasize what makes this work novel. I understand that it isn’t directly related to most of these, but then I believe you should choose papers that this work relates more directly to (improving reward models for RL). I would recommend you shorten the Human in the loop section and add a section based on improving reward models.

I have a few issues with the experimental section. You say over 5 seeds. Does that mean each bar is only the average/CI of 5 runs? If I just missed the number let me know, if I didn’t miss it and that is correct, I’d recommend running these many more times (I realize it might take a while but 5 isn’t enough). You say the that the addition of SDP never huts performance. Your plots in Figure 2 suggests otherwise. It generally improves performance but for rune SDP hurts performance in a few of the tasks. If you mean never hurts performance by a statistically significant margin this is fine but I would prefer you say this explicitly as this is slightly misleading in my opinion. 

Is it possible to hypothesize why not only does this improve sample efficiency but from Figure 4 seems to also improve finals results? 

Clarity: I wish the authors would more explicitly/intuitively define some of the terms. I was able to figure it out eventually but helping the reader would be great. Specifically:
-	“Low quality transitions”
-	“Minimum environment reward”
-	“Feedback efficiency” 
I wish the authors didn’t use the term “RQ”. Instead, if it possible, redefine them in the paragraph where you discuss them. No reason to make the reader jump around.

### Questions
There are no baseline comparison here. Is this the only work that you could augment the reward function with? I know there are other methods which do data augmentation possibly for the reward function, is there no such reasonable comparisons? If no that is fine but I would imagine there is (maybe not limit yourself to only pre-trained options if needed?). 

How do we determine r_min?

What future work is there?

### Soundness
3

### Presentation
4

### Contribution
3
