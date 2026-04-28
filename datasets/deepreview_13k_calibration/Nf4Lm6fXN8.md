# Replay across Experiments: A Natural Extension of Off-Policy RL

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Replaying data is a principal mechanism underlying the stability and data efficiency of off-policy reinforcement learning (RL).
We present an effective yet simple framework to extend the use of replays across multiple experiments, minimally adapting the RL workflow for sizeable improvements in controller performance and research iteration times.
At its core, \method~(\met) involves reusing experience from previous experiments to improve exploration and bootstrap learning while reducing required changes to a minimum in comparison to prior work. %
We empirically show benefits across a number of RL algorithms and challenging control domains spanning both locomotion and manipulation, including hard exploration tasks from egocentric vision. 
Through comprehensive ablations, we demonstrate  robustness to the quality and amount of data available and various hyperparameter choices. Finally, we discuss how our approach can be applied more broadly across research life cycles and can increase resilience by reloading data across random seeds or hyperparameter variations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper discusses a new setting, where data is shared across experimental runs to improve the performance of the policy. A simple strategy, adding data from previous experiments to the initial replay buffer, is explored and shown to be an effective approach. Various factors are investigated including the quality of the data used and the amount of data kept. These experiments are done with a variety of policy optimizatino algorithms and robotics benchmarks.

### Strengths
- The approach of keeping data from previous experiments seems to be very relevant in practical scenarios where our main goal is to train an agent with strong performance. In that case, given the cheap cost of memory, it would be sensible to keep data from previous runs for the benefit of future experiments. 
This seems like an understudied topic and it's great that this paper discusses it.

- There's a nice variety of environments that are used, including some more complex ones with a good mix of algorithms too.

- The writing and organization is clear, making the paper easy to read. The paper has a distinct focus which helps gets the message across too.

### Weaknesses
 - In the current paper, most of the experiments run the same learning agent on the same environment with the RaE algorithm but the method is pitched as being helpful for boosting learning between different experiments with potential differences in experimental conditions.
See Questions.

- There are other simple algorithms for this across-experiment setting that would be interesting to investigate. See Questions.

### Questions
- Aside from RaE, another natural baseline for this across-experiment setting would be to use behaviour cloning (or distillation) on the previously trained agents. Have you considered doing so? 

- RaE only incorporates the previous data at the beginning of optimization. What about training on the data throughout the optimization process? For example, keeping the buffer of previous data and sampling from it occasionally or mixing in samples into minibatches. 

- As I mentioned in strengths section, I think training across-experiments could be relevant for practical purposes. How do you see it being used in a scientific context? It could be difficult to fairly assess algorithms if the data they have access to depends on the sequence of previous experiments done. i.e. an advantage of discarding previous data is that algorithms start on equal ground in different papers, allowing fair comparisons. 

- I'm a bit surprised that doing some offline learning first is so detrimental to the policy (Fig. 4, finetuning and AWAC). Intuitively, I would guess that there should be a jumpstart in the performance due to the additional offline training. Could you clarify this?
Do you have any hypotheses why these methods don't perform very well here?

- Currently, the experiments that use RaE are quite similar to simply using resets but at the end of each experimental run. It would be interesting to see some experiments where the same algorithm was not used in consecutive experiments or, at least, changing hyperparameters. This could better simulate the development process of an RL algorithm. 
As a suggestion, I would be curious to see if hyperparameter optimization could be made easier. Since RL agents can be sometimes hard to run initially on a new problem, we might be able to more easily identify which hyperparameter settings are promising by giving the agent additional data.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose Replay across Experiments (RaE), in which all past experiment data is stored in the replay memory for training. In essence, data is never discarded. Data from all past experiment trials is stored and reused, not just the trajectories left in the buffer at the end of the previous experiment. The authors recommend a default mixture of 50-50 offline/online data (where “online” data is from the current experiment) to obtain good performance without tuning this hyperparameter. The authors compare RaE against other common strategies (fine-tuning, AWAC, and parameter resetting) combined with algorithms such as DMPO and D4PG in control benchmarks including Locomotion Soccer, Manipulation RGB Stacking, and RL Unplugged.

***Rebuttal: score raised from 5 to 6**

### Strengths
- The method is simple to implement compared to many existing data-reuse RL methods.
- The experiments in the paper are comprehensive, testing a multitude of diverse methods in a number of high-dimensional control environments. Several strong baselines from the literature are compared against. In spite of this simplicity, RaE can achieve strong performance in these tasks. The breadth of the results demonstrate the generality of RaE.
- The paper is well organized and includes nice discussions for related work and practical use cases.

### Weaknesses
 - The main insight of the work, while interesting, is a small contribution. As the authors note in the background section, other methods already use data stored from previous experiments, so the only novelty here is that *data is not discarded*. There is no theoretical analysis in the paper. Without significant novelty or theory, the paper depends solely on its empirical results.
- Storing all previous data is memory intensive, which is why offline RL generally uses more complicated techniques to learn from limited data. The authors do not discuss this drawback of their method, but I could see it being a bottleneck in long experiments with high-dimensional observations.
- It is unclear that replaying offline data from a long time ago is as beneficial as the authors claim. Table 1 seems to indicate that performance improves almost monotonically as the proportion of online data increases to 90%. The authors claim that “as more data becomes available, a lower ratio [of 70-80%] works better,” but this only happens occasionally, and the performance improvement is small (about 2-5%). Without any measure of significance provided, it does not seem that more than 10% offline data actually helps much.
- The results are rather noisy and would benefit from increasing the number of trials (which is currently only 5). I would recommend that the authors use a 95% confidence interval instead of standard deviation and apply a 100-episode moving average (if they are not already doing so already) to make the results easier to read. Currently, some of the standard deviations are overlapping, but I think the results would be significant if confidence intervals are used instead.

### Questions
1. What is meant by “Accumulated Reward” in the y-axes of Figures 3, 4? Is this the undiscounted episode return?
1. What is meant by “from scratch to convergence” in Table 1’s caption? Does that mean that exactly 100% refers to the final performance obtained by a pure online-data agent?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a method to reuse experience from prior RL experiments and shows benefits across a variety of RL algorithms and experiments.

### Strengths
- The authors present a very simple idea that leads to improved performance across a variety of environments.
- The proposed method works well even with a small amount of prior data.
- The proposed method works well even with low return offline data, which makes the method much more useful in practice.

### Weaknesses
 - It is not clear to me if "Total online steps" in the figures includes the steps from prior experiments or not, so I'm concerned about the fairness of the comparison between RaE and baselines. If the authors can clarify this point then I may be willing to raise my score.

 - I'm a bit confused about the difference between Random Weight Resetting and RaE. The authors write that "Reloading data for an experiment restart implicitly involves resetting network weights", which makes me think that RaE and Random Weight Resetting are very similar. However, this clearly isn't the case since RaE performs better. Can the authors clarify the difference?
- Across all figures does "Total online steps" include the steps from prior experiments for RaE? If not, I'm concerned that it may not be a fair comparison.
- The authors write, "At the beginning of each training run, policy and value-function are re-initialized in line with stand-alone experiments". I'm curious if re-initializing vs not re-initializing at the start of each training run makes a difference in performance?
- Under "Potential Limitations and Strategies for Mitigation" the authors write that "changes in dynamics or experimental settings might invalidate previously collected data." Have the authors actually tried experimenting with changing dynamics across training runs. I'd be curious to see how much of a negative effect this would actually have in practice.

### Questions
- I'm a bit confused about the difference between Random Weight Resetting and RaE. The authors write that "Reloading data for an experiment restart implicitly involves resetting network weights", which makes me think that RaE and Random Weight Resetting are very similar. However, this clearly isn't the case since RaE performs better. Can the authors clarify the difference?
- Across all figures does "Total online steps" include the steps from prior experiments for RaE? If not, I'm concerned that it may not be a fair comparison.
- The authors write, "At the beginning of each training run, policy and value-function are re-initialized in line with stand-alone experiments". I'm curious if re-initializing vs not re-initializing at the start of each training run makes a difference in performance?
- Under "Potential Limitations and Strategies for Mitigation" the authors write that "changes in dynamics or experimental settings might invalidate previously collected data." Have the authors actually tried experimenting with changing dynamics across training runs. I'd be curious to see how much of a negative effect this would actually have in practice.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes Replay across Experiments (RaE) which is based on the simple concept of reusing experience from previous experiments to improve exploration and bootstrap learning. The proposed approach is employed with a number of existing algorithms in locomotion and manipulation tasks and shown to improve the learning efficiency.

### Strengths
The described approach is simple. It could be impactful as it is mostly algorithm-agnostic.

### Weaknesses
The main drawback is the lack of explicit explanations for the improvements observed. The limitations, perhaps such as increased storage memory could also be emphasized. Furthermore, the paper does not explore the impact of trajectory recency on performance. It is unclear if older trajectories are as beneficial as newer ones, or if there is a decay in their utility over time. This aspect is crucial for practical implementation, especially when storage is limited. The paper also lacks experiments on Atari environments, which are fundamentally different from the continuous control tasks presented. The results in Table 1 are interesting, but the reasons for the observed trends are not clearly explained, particularly regarding the performance differences between high, mixed, and low return data. Finally, in Fig 1, the size of the ‘Data’ blocks is increasing, but is not immediately noticeable. It would be better to exaggerate the increase in block size to bring a reader’s attention to the data accumulation mechanism.

### Questions
1.	What motivated the reuse of previous experimental data? There is no explicit explanation for this.

2.	Do the age of trajectories matter? Eg: Suppose there is a limit on the data storage, would it be more valuable to add older trajectories to the data buffer or relatively newer ones?

3.	In the interest of comprehensiveness, I would have liked to see the benefits of this approach in Atari games as well. Does the approach improve the performance of say, DQN in Atari environments? Performance with methods like prioritized experience replay would also be interesting.

4.	The results in Table 1 are interesting. However, the reasons for the observed trends are not clearly explained.

5.	In Fig 1, the size of the ‘Data’ blocks is increasing, but is not immediately noticeable. It would be better to exaggerate the increase in block size to bring a reader’s attention to the data accumulation mechanism.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
