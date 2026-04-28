# Value from Observations: Towards Large-Scale Imitation Learning via Self-Improvement

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 6, 5, 6, 5, 8

## Abstract
Imitation Learning from Observation (IfO) offers a powerful way to learn behaviors from large-scale, mixed-quality data. Unlike behavior cloning or offline reinforcement learning, IfO leverages action-free demonstrations and circumvents the need for costly action-labeled demonstrations or carefully crafted reward functions. However, current research focuses on idealized scenarios with tailored data distributions. This paper introduces a novel algorithm to learn from datasets with varying quality, moving closer to a paradigm in which imitation learning can be performed iteratively via self-improvement. Our method extends RL-based imitation learning to action-free demonstrations, using a value function to transfer information between expert and non-expert data. Through comprehensive evaluation, we delineate the relation between different data distributions and the applicability of algorithms and highlight the limitations of established methods. Our findings provide valuable insights for developing more robust and practical IfO techniques on a path to scalable behaviour learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a method for learning policies from two types of demonstration data: sub-optimal demonstrations with state-action pairs and expert demonstrations containing only states without action labels. The proposed approach involves learning a value function for the states from both datasets and fitting a policy to maximize this learned value. The value function is supervised in two ways: by assigning a reward of 1 to states in the expert demonstration set and 0 to other states, or by using predictions from a discriminator that determines whether a state is from the expert demonstration set. The method further incorporates iterative self-improvement by generating new sub-optimal demonstrations using the learned policy. The approach is evaluated in various simulation environments from MuJoCo and Robomimic, leveraging open datasets collected in these settings.

### Strengths
*Addresses an Important Problem*: The paper tackles the practical challenge of learning from heterogeneous demonstration data, which is valuable in scenarios where expert action labels are unavailable but expert state observations are accessible.

*Novel Methodology*: Extend existing methods that combine value function learning and policy fitting, supervised through either binary rewards or discriminator predictions, which is a creative approach to leveraging available data.

*Application to Diverse Environments*: Applies the method to various simulation environments using open datasets, demonstrating the method's applicability across different tasks and specifically showing good results in self-improvement.

### Weaknesses
 - *Insufficient Practical Motivation*: The paper lacks clear examples of real-world scenarios where the specific data setting (expert demonstrations without actions and sub-optimal demonstrations with actions) is prevalent.
Providing practical applications, such as the use of shared-embodiment devices like the UMI gripper (https://umi-gripper.github.io/), would strengthen the motivation and highlight the method's relevance to practitioners.
- *Absence of Real-World Experiments*: The lack of real-robot experiments limits the demonstration of the method's effectiveness in practical settings. Including real-world applications would greatly enhance the paper's impact and validate the approach beyond simulated environments.
- *Clarity and Writing Quality*: Several sentences are difficult to read due to approximative language, which affects the overall readability.
For example, the last sentence before the related work section (line 85) and the use of terms like "decade of experience" without scientific backing (line 128) or "struggle to achieve improvement" instead of underperform.
- *Weakness in Related Work Section*: Some citations are not well justified, and the connections to the proposed method are unclear.
This makes it difficult to assess the novelty and positioning of the work within existing literature.
- *Unclear Experimental Results*: It is specified that the reported results are from the training set (line 305). This is concerning, results should be reported from simulated rollouts. The experiments lack clear takeaways, making it challenging to interpret the effectiveness of the method. In Figure 2, the large difference between the discriminator and binary results in the walker experiment is not explained, leaving readers uncertain about the underlying reasons.
- *Lack of Baseline Comparisons in Self-Improvement Experiments*: The second set of experiments demonstrates iterative self-improvement but contains only one relevant baseline and an oracle approach. It makes it difficult to evaluate the advantages of the proposed approach over existing methods.
- *Unsupported Practical Relevance in Conclusion*: The conclusion mentions "practical evaluation settings" and "practically relevant" applications without providing supporting evidence or examples within the paper. These supporting evidence do exist and should be mentionned.

### Questions
- *Practical Applications*: Can you provide concrete examples of practical scenarios where expert demonstrations without action labels and sub-optimal demonstrations with actions are available? How would your method be applied in such settings? Is the UMI gripper (https://umi-gripper.github.io/) a good fit?
- *Evaluation Methodology*: How did you evaluate your method? Did you use simulated rollouts? Clarifying this is crucial for assessing the validity of your results. Line 305 mentions success rates, did you mean the policy success difference? 
- *Discriminator Performance*: In Figure 2, what accounts for the large difference between the discriminator and binary results in the walker experiment? Does this indicate issues with the discriminator's ability to discern state provenance?
- *Experimental Conclusions*: What are the key takeaways from your experiments? Could you summarize the main findings and how they support the effectiveness of your method? My understanding is that in the simplest settings and data distribution your methods outperform your baselines and approaches the method using oracle reward. While for more complex tasks and data distributions your method underperforms or is similar to the baseline. Is that the conclusion of your first set of experiments?

Additional Feedback:
- *Enhance Motivation with Practical Examples*: Incorporate real-world applications or potential applications where your method would be particularly beneficial. Discuss devices like the UMI gripper or other expert demonstration systems to illustrate practical relevance.
- *Improve Writing and Clarity*: 
Revise the manuscript for language and structural clarity.
Ensure that all sentences are clear, concise, and scientifically precise.
- *Strengthen Related Work Discussion*:
Include a section about self-improvement. It seems to be one of the strongest experimental results of the paper but it is not situated in the literature.
- *Clarify Experimental Procedures*: Provide detailed information about the evaluation methodology.
Include an appendix with comprehensive results, such as comparable absolute returns or success rates, to facilitate comparison with other works.
- *Explicitly State Conclusions*:
Draw clear conclusions from your experimental results.
Summarize the main contributions and how they are validated through your experiments.

I would happily raise my score if my concerns about the evaluation methodology are answered.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors expand on previous soft reinforcement learning methods, to facilitate learning from observations (IfO) without considering actions. In this setting, it is assumed that a reasonable demonstration set exists that does not exhaustively capture the occupancy measure of the target task.

They present their method: Value from Observation (VfO) and evaluate against several baselines on a crafted synthetic dataset, comprised of varying quality rollouts collected from Behavior Cloning policies (BC). The authors’ contribution lies in adapting the SQIL and ORIL in the action-less domain, relaxing the assumptions of the demonstration set needed and showcasing that learning can still be facilitated via an extensive set of experiments.

### Strengths
Generally well written paper, with easy to follow structure and well laid out motivations and claims.
The authors make reasonable claims and specifically state their effort to contribute to the significant and challenging problem of learning from Observations, in the offline setting, which can be a prerequisite for large scale learning.

Their experiments are reasonably displayed. The authors compare their method against the baselines in both their own dataset for the popular task in the D4RL and Robomimic benchmarks.

The ablations, especially for figures 6 and 7 are very interesting. They showcase that self-improvent is possible from self collected data, even from a very underperforming starting policy.

### Weaknesses
I) Novelty. This author’s contribution lies in showcasing that SQIL type methods can potentially learn even if not considering actions, as long as the demonstration set is reasonably perfomant and in providing a new dataset that could be of use to the community. While the adaptation of SQIL to the action-less domain is a non-trivial modification, the core idea of regularizing behavior cloning by penalizing deviations from the demonstrated state distribution remains conceptually similar. The paper's contribution would be strengthened by a more in-depth analysis of the specific challenges and nuances introduced by the absence of action data, beyond simply removing the action component from the SQIL objective. The empirical results, while demonstrating the method's effectiveness, do not fully explore the boundaries of this approach, particularly in scenarios with highly diverse or suboptimal demonstration data. The claim of a novel offline evaluation recipe also needs further justification, as it is not clear how it differs fundamentally from existing methods of evaluating offline RL algorithms, other than the specific dataset used.

II) Minor

a) The expert’s returns should be displayed in the plots along the background data. This would give a better understanding to the reader of the impact of the differing quality between the presumed expert data and background data. The current plots make it difficult to assess the absolute performance of the method and its proximity to the expert's performance.

b) The choice of  plotting  return differences vs background data returns, can be confusing. While the intention might be to highlight the improvement over the background data, it obscures the actual performance of the trained policy and makes comparisons across different background datasets challenging.

### Questions
1) Why does simple BC seem to improve on the background data? Was it not trained to true convergence?

2)What happens when a significant part of the demonstrated data is of very low returns? Is there a point where the method could irrecoverably suffer from trying to imitate these potentially harmful examples?

3) In figures 6 and 7 it can be hard to discern what is happening especially in the later parts of Hopper and Walker. What does this box-tooth behavior mean?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper deals with the problem of learning from a mixture of expert collected data without action annotations(expert data) and another dataset with actions but is not expert collected(background data). The authors pose the Imitation Learning Problem in this setting as an RL problem to learn a Value function over the mixture dataset and then use the value function to learn a policy, adapting two variants of prior methods in RL - SQIL ( VfO - bin) and ORIL (VfO - disc) to compute the pseudo rewards for Value function learning based on the source of the dataset.  The authors also propose a self-improvement benchmark ( SIBench), an offline dataset proxy to online policy improvement compiled from policies learnt at various stages of training starting from a random policy and learnt with behavior cloning.

### Strengths
Significance: 

Finding edge cases and distribution imbalance in the benchmarks followed in the literature and proving an alternative benchmark. Based on the findings in the paper - the prior benchmarks are biased to be bimodal. Also finding cases where the prior work doesn't perform as well - DILO[1] and SMODICE[2]. 

Originality:

 It is a mix of ideas from previous work. The algorithm is similar to the one proposed in DILO[1] - learning a value function and using it to learn a policy. Using SQIL to compute the pseudo-reward is new. ORIL[3] style models where a discriminator is learnt to compute the good states has been proposed before in the prior work. 

Quality and Clarity: 

The presentation is easy to read, the figures are simple but can be improved significantly. There are a few typos which can be addressed in a revised print.



[1] Harshit Sikchi, Caleb Chuck, Amy Zhang, and Scott Niekum. A dual approach to imitation learn- ing from observations with offline datasets, 2024.

[2] Yecheng Ma, Andrew Shen, Dinesh Jayaraman, and Osbert Bastani. Versatile offline imita- tion from observations and examples via regularized state-occupancy matching. In Kamalika Chaudhuri, Stefanie Jegelka, Le Song, Csaba Szepesvari, Gang Niu, and Sivan Sabato (eds.), Proceedings of the 39th International Conference on Machine Learning, volume 162 of Proceedings of Machine Learning Research, pp. 14639–14663. PMLR, 17–23 Jul 2022.

[3] Konrad Zolna, Alexander Novikov, Ksenia Konyushkova, Caglar Gulcehre, Ziyu Wang, Yusuf Ay- tar, Misha Denil, Nando de Freitas, and Scott Reed. Offline learning from demonstrations and unlabeled experience, 2020.

### Weaknesses
1. The paper is an empirical experiment on using value functions for a mixture of expertly annotated datasets and background datasets. It would be nice to see rigorous study grounded in theory regarding policy improvement ? What are the bounds of improvement on the policy - the maximum performance that can be achieved by the policy ? Can the policy do better than the expert demonstrations, if yes, in what settings ?

2. There has been a mention of Advantage Weighted Regression(AWR) in Section 3 and AWR is used as the oracle in Section 4, it would be nice to see some equations and proofs on cases where this method meets the performance of Advantage Weighted Regression, instead of just a claim ?

3. Rigorous study and Ablations for the mixture of datasets is missing. Some ideas to explore - What is the maximum performance that can be achieved from just the background data? Methods like learning from Hindsight([2],[3]) can be used to learn without rewards. What is the performance increase with the expert datasets? And if the expert dataset is out of distribution from the background data? 

4. Explanations on why SMODICE[4], DILO[5] perform worse ( Other than the overlap of demonstrations) and why the proposed Vfo-bin and Vfo-disc perform better are missing in the experiments analysis ?

### Questions
Some questions on the clarity on equations and figures: 

In equation 2, it is not clear how do you have access to the expert policy, pi_E(a|s). Is that the learnt policy on expert observations ?

Plots with lines in Figure 6 and 7 are confusing? Could the same idea be conveyed with different style of plots? 

Here are some suggestions for stronger results, addressing which I am happy to revise my score: 

1. In the algorithm, is it necessary to learn value function and policy in a single iteration ? Since in the binary case, the rewards are always 1 for expert datasets and 0 for the background datasets. Have any experiments been conducted where the value function is learnt just on the expert data and then it is used to learn a policy on background datasets?

2. It could also be possible that if a similar set of states are encountered by the background datasets, it could confuse the value function since all the background states are given a reward of zero ? It would be good to see some results in the extreme case, where all the expert observations are a subset of the background data?

3. Although the Value function is appropriate for a setting without demonstrations, it would also be nice to see how well the algorithm performs when action annotations are available with SQIL. The setting would be SQIL uses the action annotation information, VfO learns just from observations. This would also be a stronger result if VfO can learn comparatively to SQIL like methods without any actions. 

4. With reference to the title and the mentions regarding scaling in Section I and - there are already many large pre-trained models available and harder problems like the robotics manipulation problems in the real used in DILO ? It would be nice to see any practical problems being tackled by the proposed methods?(Performance on Carla Leaderboard[1], or using Offline Autonomous Driving Datasets, or learning robotics policies in the real world ) Studies on the number of episodes versus the policy performance and proposing any scaling laws ? 


[1] CARLA Leaderboard (https://leaderboard.carla.org/)

### Soundness
2

### Presentation
3

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
The paper contributes an algorithm for learning from a dataset in which the agent has access to expert demonstrations without action labels, and background datasets with action labels but not actions for the same desired task. In this case, expert refers to being on-task with respect to the desired task for the given embodiment. The paper also contributes a dataset with a variety of policies of different quality on background tasks.

The method uses a value function to transfer information between expert and non-expert data. 
Given that the expert dataset doesn’t include actions, the agent must learn the dynamics between actions and states from the background dataset. The state-value function transfers knowledge from the expert data to the background data. The authors note that a state-action value function offline RL approach cannot be applied because we cannot assume any of the background has action annotations that are “good” with respect to the desired task. One variant of VfO assigns binary 0-1 reward to if a state came from background or expert, respectively. Another variant learns a discriminator that performs a soft assignment. Policy evaluation based on the state-value function is performed by computing the loss via temporal difference error of a virtual policy that mixes expert and background data (mixing is controlled by alpha). Then, AWR is used to update the policy. The key different to the offline RL setting is the (soft) binary reward for sourcing a state from the expert versus the background data. The learned policy is incentivized to visit expert states.

### Strengths
The results are promising in that they show VfO is competitive with RL from ground truth reward when using a few action free trajectories.

### Weaknesses
The assumption that background actions have zero reward may overlook potentially valuable information. For instance, if the background dataset contains partial executions of the desired task (like pouring water for a coffee-making task), discarding these actions might lose important insights that could improve the agent’s performance. I’m curious about the results of a sensitivity analysis of algorithm parameters to better guide practitioners on how they should utilize VfO. For example, how does the ratio of expert to background affect performance, and the alpha parameter? I’m unsure about how compelling the paradigm of VfO is in practice, see question below.



### Questions
I’m unsure about how compelling the paradigm of VfO is in practice. Let’s say I have a robot that I’d like to teach a specific desired task: I’d have the capacity to give only a limited amount of expert, on-task demonstrations, but these would contain action labels, and lots of background internet-scale data (likely without action labels, e.g. youtube videos) to train the robot policy. Given that this is leveraging of large-scale datasets is a motivation in the paper, it would be great to discuss why it would be more likely we’d have action-labels for background tasks? It would be helpful to provide concrete examples of real-world scenarios where one would have action-labeled background data but unlabeled expert data, and discuss how common these scenarios are in practice.

How similar does the background data need to be to the desired task? How sufficiently covering of the transitions needed in the expert dataset does the background data need to be? Further analyses to characterize how the similarity between background and expert data affects performance, such as systematically varying the overlap between the datasets, would help readers better understand the generalizability of the approach. 

Does the assumption that the background contains actions that should receive a reward of 0 risk losing potentially informative action sequences? It possible that the background data contains trajectories that contain partial executions of desired tasks? For example, if my desired task is preparing coffee, but the background dataset contains pouring water, might we want to learn a positive value for those transitions? It would be helpful to discuss potential ways to extend the method to better handle partially relevant background data, or to analyze how this limitation affects performance in practice.

How does the value of mixing parameter alpha affect the training of the policies? It would be helpful to include an ablation study or sensitivity analysis for key parameters like the expert/background ratio and alpha. 

In the bimodal task, why did VfO fail to achieve improvement beyond simple BC? Would an alternative generative policy architecture improve these results? It would be great to further discuss potential hypotheses and suggestions for modifications that might improve its performance on bimodal data.

I am not well-versed in offline RL, and I hope the other reviewers can speak more to the technical appropriateness of the evaluation.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a simple method for imitation learning with a mixed dataset. The proposed method first labels the dataset with either learned reward or binary reward and then use an offline RL procedure to extract optimal policy. In experiments, the authors compare their method to several offline imitation learning method and achieved superior performance.

### Strengths
1. The method is clean and straightforward.
2. The method can outperform selected baselines in both state-based and image-based setups.

### Weaknesses
I am concerned about the novelty of the approach:
1. Existing studies (e.g., [1, 2]) already label background datasets using certain imitation learning-based reward functions, then apply offline RL to derive the optimal policy. The proposed method appears to be a variation within this established framework, merely adopting a different implementation. It is unclear what new insights or discoveries are presented here. A more detailed comparison to these works would help clarify the unique contributions.

2. The authors rely on existing reward functions to label the dataset, which further raises questions about the novelty.

### Questions
Suggestions and Questions for Improvement:
1. Consider experimenting with a wider variety of reward functions (as baselines) and discussing best practices for selecting effective reward functions in this context. For example, the use of Optimal Transport (OT) Based Reward used by recent applications [1] and the binary goal completion reward in the goal conditioned setups. 

2. Since the author claims that the method targets large-scale imitation learning, it would be valuable to see evaluations on more challenging problems, such as those with longer time horizons or real-world applications. For example, the D3IL benchmark [2]. 

[1] Haldar et al. Watch and match: Supercharging imitation with regularized optimal transport. In CoRL 2022.
[2] Jia et al. Towards Diverse Behaviors: A Benchmark for Imitation Learning with Human Demonstrations. In ICLR 2024.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper suggests a novel method for imitation learning from observation (IfO), a setting where only demonstrations without reward and action labels are available. However, more non-expert experience with action labels may be obtained. The proposed algorithm Value learning from Observations (VfO), extracts information from the expert demonstrations by learning a value function using one of two simple rewards: (i) assign a reward of 1 to expert transitions and 0 to all others (VfO-bin), or (ii) learn a discriminator distinguish expert states and use its output as a reward (VfO-disc). This value function is then used with the offline RL algorithm Advantage Weighted Regression to train a policy. Both versions of VfO are evaluated on datasets obtained from a range of simulated continuous control tasks both in a fully offline and a self-improvement setting. Additionally, benchmark datasets (SIBench) mimicking iterative self improvement are proposed to simplify the evaluation of VfO methods. The experimental results indicate that VfO can improve on the behavior policy used to collect the labeled data. In particular, it can outperform strong baselines like SMODICE and DILO on the SIBench data, sometimes close to AWR with access to the ground-truth reward. In contrast to this, VfO is less successful on bimodal data.

### Strengths
The IfO setting (also with iterative self improvement) is highly relevant for scaling up imitation learning, in particular in robotics. The proposed algorithm VfO is quite simple, and easy to implement. An analysis of the VfO-bin variant furthermore shows that the objective tries to maximize visitation of states that occur in the expert demonstrations, which helps with building intuition. 

Apart from the VfO algorithm, the paper also proposes a suite of datasets (SIBench) for benchmarking IfO algorithm in a purely offline fashion. Results on SIBench are shown to correlate with the iterative self-improvement setting. 

The fact that VfO outperforms more complex baselines like SMODICE on the SIBench data is quite remarkable. Yet, the paper is quite honest in presenting the experimental results, and clearly states that on bimodal data, VfO performs less well.

Overall, the paper is well written and the figures do a good job in conveying the results.

### Weaknesses
While the text mentions that the learned value function is essentially the discounted probability of being in an expert state, there is no discussion about why (or when) maximizing this is sufficient as an imitation learning objective. During iterative self improvement, could it not happen that the agent learns to stay stationary in a region of the state space which was visited by the expert even though the expert was not stationary and covered a bigger region of the state-action space? This problem seems to be more severe than in SQIL as SQIL learns a Q-function from expert demonstrations with actions and therefore would not learn to be stationary. I would encourage the authors to discuss the implications of the VfO objective and explain when it can be expected to work well. Specifically, the paper should address how the VfO objective prevents the agent from exploiting the reward signal by simply remaining in a small subset of the expert's state space, rather than learning the full range of expert behaviors. This is particularly relevant in the iterative self-improvement setting where the agent might overfit to the initial expert state distribution.

In line 325 the choice of the hyperparameter lambda is mentioned (which is different on D4RL and Robomimic). As lambda controls the amount of behavioral cloning, it would be interesting to see its impact on performance, and discuss its role in VfO. I would appreciate a hyperparameter study for lambda. Furthermore, the paper should clarify how the temperature parameter in AWR affects the learning process and how it interacts with the VfO-derived value function. A sensitivity analysis of this parameter is also needed to understand its impact on the final policy.

The labels in figures are too small. This is particularly evident in figure 1 but also true for the other figures to a lesser extent. It would be better to adjust the plots to look good when printed out. I would furthermore encourage the authors to provide additional plots with the absolute performance of the algorithms as it would make it easier to judge how significant the improvements are. The confidence intervals in the plots are not clearly explained, making it difficult to interpret the statistical significance of the results. The paper should provide a more detailed explanation of how these intervals are calculated and what they represent in the context of the experiments.

### Questions
* In line 334, the bootstrap value is introduced a bit ad hoc. Why is this construction necessary as opposed to not bootstrapping when terminating?
* It would be interesting to discuss if there are qualitative differences between the behaviors learned by the VfO and baseline agents. If such differences exist, can they be related to the training objective?
* It is not clear to me what exactly the subplots with the confidence intervals show (in figures 2, 3, 4, 5). It would be great to explain this in the caption.
* ‘demonstration’ in line 085 does not seem to fit into the sentence.
* The last sentence of the abstract seems to be broken/unfinished.
* ‘VfO-dist’ seems to be a typo in line 341.
* The order of the data points (to which iteration they belong) is a bit hard to make out in figure 6. Maybe encoding the iteration with saturation or some other property could help.

### Soundness
3

### Presentation
3

### Contribution
3
