# Reverse Forward Curriculum Learning for Extreme Sample and Demo Efficiency

- Decision: Accept
- Scores: 3, 8, 6

## Abstract
Reinforcement learning (RL) presents a promising framework to learn policies through environment interaction, but often requires an infeasible amount of interaction data to solve complex tasks from sparse rewards. One direction includes augmenting RL with offline data demonstrating desired tasks, but past work often require a lot of high-quality demonstration data that is difficult to obtain, especially for domains such as robotics. Our approach consists of a reverse curriculum followed by a forward curriculum. Unique to our approach compared to past work is the ability to efficiently leverage more than one demonstration via a per-demonstration reverse curriculum generated via state resets. The result of our reverse curriculum is an initial policy that performs well on a narrow initial state distribution and helps overcome difficult exploration problems. A forward curriculum is then used to accelerate the training of the initial policy to perform well on the full initial state distribution of the task and improve demonstration and sample efficiency. We show how the combination of a reverse curriculum and forward curriculum in our method, RFCL, enables significant improvements in demonstration and sample efficiency compared against various state-of-the-art learning-from-demonstration baselines, even solving previously unsolvable tasks that require high precision and control. Website with code and visualizations are here: https://reverseforward-cl.github.io/

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper deals with curriculum learning in cases where there are only a small number of demonstrations available. The proposed method specifically design the curriculum generation as two stages: one along the demonstration paths, another explore around demonstration and eventually cover the entire space. The experiments are performed on several learning from demonstration (LfD) benchmarks.

### Strengths
- The presentation of this paper is good. 
- The experiment results are strong compared to multiple related baselines.

### Weaknesses
There are several issues/concerns on the method and experiments:

Method:

- The most important issue is the design of curriculum. Basically, the author tried to separate the curriculum of reset states into two stages: in the first one the reset states are along the demonstrated states, and in the second one the reset states gradually move away from the demonstrated states. This does not make sense. Why not just combine the two stages into one, i.e. a curriculum that includes explorations of reset/initial states along the demonstration and also away from demonstrated states? The reset states need to cover the entire space in the end anyway. I don't see any reason for a two-stage design to make sense. Conceptually, reverse curriculum and "forward curriculum" are almost the same thing, with the latter has a difference of weighting on the exploration area.

- What if there is no demonstration? Or intentionally forget about demonstration but just design curriculum that directly moves the reset/initial states away from goal? If this paper's assumption is that in the end, the initial/reset states should be able to cover the entire space anyway, then whether there is demonstrations provided should not matter: all starting states has to be explored sooner or later. I didn't see an ablation experiment to compare against the setting where no demonstration is available.

Experiment:

- As mentioned, it would be great to show the results under the setting where no demonstration is available, or the "forward curriculum"-only case. I understand the Maze task in Figure 6 tries to show this. But the experiment in Figure 6 is wrong: it does not show forward-curriculum-only is worse than reverse+forward curriculum. The reason it is worse is because forward-curriculum-only experiment mistakenly messed up with exploration (it should only explore in unexplored area, not around already explored demonstration area on blue lines). The explanation in the last two sentences of Section 5.2 is wrong too imo.

- In Figure 5, do all experiments have the same reset/initial state distribution (cover all possible states) at the end of their curricula? If so, it's so hard to understand why the more demonstration there is, the faster it can be trained.

- It seems that RFCL without "forward curriculum" works almost the same as RFCL with "forward curriculum" in most tasks (Fig 5). This again questions the necessity of having a second stage, as mentioned earlier. Without the two-stage setting, the novelty of this work is negatively impacted.

- I'm not sure if the tasks selected in this paper are suitable for the proposed method:
   - If the robot arms are moved by a positional controller, then the initial/reset position/states of the robot arm does not matter, because the positional controller should guide the robot arm/end effector converge to the goal position anyway regardless of initial states. Not much exploration is needed. So if this is the case, then the selected task cannot fully evaluate the potential of the proposed method.
   - If the robot arms are not moved by a positional controller, then why not do so?

### Questions
My questions are written in previous "Weakness" section. The authors can respond to the concerns/question written there.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper the authors show the benefits of first using a reverse curriculum on demonstrations (of simulated RL tasks with sparse rewards) followed by a forward curriculum that expands the set of initial states (from which the agent can achieve the task). In many different simulated RL tasks, it is shown that the method can achieve quite significant boosts in sample efficiency, and can sometimes succeed in tasks which other methods completely fail. Ablation studies show that the method is robust to the number of demonstrations and that the reverse-forward curriculum seems to be the best among various other choices.

### Strengths
* The paper convincingly shows that their method and their particular choice of curriculum leads to significantly better performance in many different RL tasks with sparse reward structure. 

* Ablation studies are well done and cover significantly the possible variations.

* Figures captions and plots are well done, as well as the visualizations in the website.

### Weaknesses
* The paper could benefit from an algorithmic summary. Algorithmic decisions not summarized succinctly by equations or in algorithmic form, but by verbose descriptions make the method look more 'alchemical' than it need be. e.q. 

"Define q to be the fraction
of episodes out of the last k episodes that receive nonzero return starting from a sampled initial state
si,init. If q is 0, then assign a score of 2 to si,init. If 0 < q < ω for a threshold 0 < ω < 1, assign
a score of 3. If q ≥ ω, assign a score of 1." 

The actual numbers chosen detract from the concept of rejecting samples based on e.g. the expected return of exploration.

### Questions
* Please do not use the word 'extreme', you used it several places throughout the paper.

* "In practice, the observations used by the policy πθ may be different from the actual environment state but for simplicity in this
paper state also refers to observation."
> So you don't consider noisy feedback or POMDPs? This should be mentioned clearly in the introduction. As the method shows significant improvement in learning curves, it is vital to indicate when/where we expect them to hold and where they would fail.

* "In both stages, we use the off-policy algorithm Soft Actor Critic (Haarnoja et al., 2018) with a Q-ensemble (Chen et al., 2021b), "
> What happens if you use another RL algorithm? Does it make a big difference? Which other methods, competitive to SAC, could you use?

* Minor comment: " As a result, a curriculum for each demonstration is necessary as opposed
to a curriculum constructed from all demonstrations as done in prior work in order to ensure noisy
information arising from the multi-modality of demonstrations do not impact the reverse curriculum
of each demonstration as much." -> Too long sentence.

* You use \phi before you introduce it, and I didn't get what it's supposed to mean?

* "In this manner, initial states that sometimes receive
return are prioritized the most, then initial states that receive no return, then initial states that are
consistently receiving return." -> Not a very clear sentence, do you want to use 'than' instead?

* Would be nice to discuss why the methods compared against were chosen out of all the possible RL algorithms out there (maybe in an appendix?) Would the others be unsuitable for the task (e.g. on-policy, not suitable for demonstrations etc.)

==== POST-REBUTTAL ====
* My score remains the same, I think this paper should be accepted, as it has good results and detailed ablations. 
* Assumptions/limitations of the method (e.g. full observability, restricted to simulations, requires demonstrations) are mentioned throughout the paper and is not a deal-breaker. As mentioned in the rebuttal, just improving simulation efficiency is also a contribution.

### Soundness
3 good

### Presentation
2 fair

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
In this study, a novel methodology is proposed, combining reverse and forward curricula. The authors suggest resetting from demonstrations to effectively perform exploration when access to a limited number of demonstrations is available. The reverse curriculum starts from positions backward from the goal point using demonstrations, while the forward curriculum is executed through score-based prioritizing, allowing the starting point to have an appropriate level of difficulty. As a result, it shows improved performance compared to baseline methods that leverage demonstrations.

### Strengths
- The proposed method, combining reverse-forward curriculum approach is novel.

- The learning curves presented in figures 3 and 4 demonstrate improved performance compared to the baselines, and the figure in 5 suggests that using both the reverse and forward curriculum with a limited number of demonstrations is beneficial.

### Weaknesses
- The assumption of resetting from demonstrations is a strong one and only applicable in simulation environments. While this study proposes an efficient way to leverage one or more demonstrations through the reverse curriculum, I still consider it to be a strong assumption.

- The study may appear to be not significantly different from consecutively performing Jump-Start RL and PLR.

- While it compares to various baselines, many of them seem to be algorithms that do not assume state resets or use curricula.

### Questions
- In Figure 6, it seems that 'reverse' and 'forward' are only applicable to 'reverse-forward,' and not to 'none' and 'forward only,' which might be confusing.
- Which algorithms among the compared baselines require the State Reset assumption?
- If possible, could you please explain the reason for the initial high performance of RLPD in the stick pull task in Figure 4, followed by a drop?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
