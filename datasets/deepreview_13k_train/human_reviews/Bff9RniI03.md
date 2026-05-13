# Leveraging Skills from Unlabeled Prior Data for Efficient Online Exploration

- Decision: Reject
- Scores: 5, 8, 5, 6, 5

## Abstract
Unsupervised pretraining has been transformative in many supervised domains. However, applying such ideas to reinforcement learning (RL) presents a unique challenge in that fine-tuning does not involve mimicking task-specific data, but rather \textit{exploring} and locating the solution through iterative self-improvement. In this work, we study how unlabeled prior trajectory data can be leveraged to learn efficient exploration strategies. While prior data can be used to pretrain a set of low-level skills, or as additional off-policy data for online RL, it has been unclear how to combine these ideas effectively for online exploration. Our method \ours{} (\textbf{S}kills from \textbf{U}nlabeled \textbf{P}rior data for \textbf{E}xploration) demonstrates that a careful combination of these ideas compounds their benefits. Our method first extracts low-level skills using a variational autoencoder (VAE), and then \textit{pseudo-relabels} unlabeled trajectories using an optimistic reward model, transforming prior data into high-level, task-relevant examples. Finally, \ours{} uses these transformed examples as additional off-policy data for online RL to learn a high-level policy that composes pretrained low-level skills to explore efficiently.
We empirically show that \ours{} reliably outperforms prior strategies, successfully solving a suite of long-horizon, sparse-reward tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a hierarchical policy for leveraging unlabeled offline data for exploration. In the offline stage, low-level skills are extracted, and in the online stage, these skills are reused and a high-level policy is learned with optimistic rewards. The proposed method is tested on maze and manipulation tasks and shows good performance.

### Strengths
- The paper is well-written and easy to understand.
- The paper proposes a simple method for leveraging offline data and showing good performance on AntMaze, visual AntMaze, and Kitchen tasks. 
- The paper conducts thorough experiments and compares a set of different methods.

### Weaknesses
 - Dependence on offline data quality: The performance of the proposed method is influenced by the quality of the offline data and the specific features of the evaluation tasks. In particular, the approach relies on a high-level policy that is updated every 
𝐻 timesteps and keeps the pre-trained skill and trajectory encoder fixed during the online phase. This limitation constrains adaptability, especially in scenarios where task distribution varies from the offline data. The method's reliance on fixed-length trajectory segments for skill extraction may also limit its ability to capture more complex, variable-length skills, potentially hindering performance in tasks requiring intricate maneuvers or longer-term planning.
- Limited discussion on Hierarchical Reinforcement Learning (HRL): Although hierarchical policy structures have been extensively explored in the HRL literature [1-8] and are closely related to the paper, the paper does not sufficiently address relevant findings from HRL research. A more comprehensive discussion of how this work could provide valuable context. Specifically, the paper does not adequately discuss how its approach relates to established concepts such as options, which provide a formal framework for temporal abstraction and skill learning in HRL. The lack of discussion on how the proposed method compares to or differs from these established HRL techniques is a significant oversight.
- Novelty: The paper combines elements from ExPLORe and trajectory-segment VAE to leverage offline data for exploration, but adds limited new insights beyond prior work. HRL emphasizes hierarchical structures, and the benefits of skill extraction in offline settings have already been documented. This paper simply applies existing solutions to ExPLORe. The core idea of using a VAE to extract skills from trajectory segments and then using these skills in a hierarchical policy is not novel, and the paper does not provide sufficient justification for why this particular combination of existing techniques leads to a significant advancement.

### Questions
See weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper presents SUPE, a method for using offline data (without rewards) in the online reinforcement learning setting. SUPE first extracts a set of low level skills using the offline data, and then optimistically labels the offline trajectories. It then uses an off policy high level update to update on a mix of offline (pseudo labeled trajectories) and online real trajectories. The paper empirically validates the new algorithm on three environments and does ablations on amounts of offline data.

### Strengths
- This paper makes an insightful empirical benefit for using trajectories twice for both low level skill pretraining in addition to optimistic labelling.
- The paper thoroughly evaluates the proposed method.
- The paper does a good job explaining the proposed method and it's significance.

### Weaknesses
 - This paper could benefit from a bit deeper analysis of the contribution of the two uses of offline data. It's clear that both are necessary, but not necessarily why.

### Questions
- Where do the authors think their empirical benefit is coming from? Why can we use trajectories twice?
- Is the algorithm robust to different design choices?
- How important is the optimistic labelling (from Li et al.)?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces SUPE, a method that leverages unsupervised learning to extract skills from unlabeled prior data, subsequently using hierarchical methods to explore more efficiently. These unlabeled data can also contribute to high-level policy training. Experimental results show that SUPE outperforms previous methods on the D4RL benchmark.

### Strengths
- The approach of extracting latent “skills” from unlabeled data and employing hierarchical methods significantly enhances exploration.
- The approach of utilizing prior data twice ensures better use of the available data.
- The paper is well-structured and easy to follow.
- Extensive results demonstrate that this method outperforms previous approaches.

### Weaknesses
 - The concept of using a VAE to extract latent codes and employing a high-level policy for online exploration is not novel, and it shows limited progress compared to previous work [1].
- The ablation study lacks depth. I am interested in understanding the contribution of “reusing prior data twice” to the final performance. Additionally, I’d like clarification on the design choice for the latent variable $z$ in skill discovery: how do you ensure this latent $z$  is sufficient for effective skill discovery in the dataset? Is employing trajectory-segment VAEs truly necessary for efficient exploration?

### Questions
Please refer to the weakness part. I may consider increasing the score if my questions are addressed.

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
3

### Summary
This paper presents a pre-training method for reinforcement learning (RL) that can train on data sets that do not contain reward labels, i.e., the data sets are unlabeled. 
The problem setting resembles offline-to-online RL, except that there are no rewards in the data set.
In the pre-training stage, the authors propose to learn a set of skills from this unlabeled offline data.
Then, in the online fine-tuning state, the authors learn a high-level policy that selects which skill to use in a given state.
They utilize the unlabeled offline data during fine-tuning by learning an optimistic reward model and using it to add optimistic reward labels to the offline data.
They evaluate their method in the D4RL AntMaze and Kitchen benchmarks as well as the D4RL Visual AntMaze.

### Strengths
Overall, I found the paper easy to follow and I think it is addressing an important problem -- pre-training in RL -- which is of interest to the community.

The results demonstrate that learning skills from offline data is a promising approach to leverage reward-free offline data.
I think this is an interesting result.
I also like the idea of labelling the offline data using a learned reward function.

### Weaknesses
The authors consider the setting of having access to offline data but no reward labels. Whilst I see the value in this problem setting, it is not clear if practitioners should opt for this method over standard offline-to-online RL methods when
their data sets contain reward labels. Whilst I appreciate this is out-of-scope, ideally methods would leverage data sets both with and without reward labels. It would be insightful if the authors could compare to offline-to-online RL methods which do leverage reward labels. Whilst I do not expect their method to outperform these methods, I think it is an important baseline that we can gain insights from.

In my experience, optimistic-based exploration methods are very susceptible to the $\alpha$ parameter. How was this set in practice? Did it require a grid search to find the best value in each environment? Please can you provide details on any hyperparameter tuning process, including the range of values tested and how sensitivity varied across environments? This information would be valuable for reproducibility and understanding the robustness of the method.

Is there a reason the authors only considered the diverse data set for the AntMaze experiments? Does this method require a diverse offline data set collected by an unsupervised RL method, or can it leverage narrow offline data distributions? For example, data from solving a different task? How does the method perform when using the AntMaze "play" data set instead of the "diverse" data set? Even if the method performs poorly, I think it would be valuable to include these results.

I am not sure what to take from the coverage results. I can understand why we care about coverage in unsupervised RL where our sole purpose is to explore. However, during online training our goal is to balance exploration vs exploitation. Please can the authors provide a clearer justification for why coverage is an important metric in this context, or include additional plots that more directly show the relationship between exploration and task performance, such as the normalized return vs coverage?

In Table 1, what do the bold numbers represent? The authors should state what statistical test was used for the bolding or at least expla8in what the bolding represents.

### Questions
- How does your method compare to using offline-to-online RL methods which have access to reward labels?
- How was the $\alpha$ hyperparameter set?
- Why did you not compare to other types of offline data sets?
- What should I take from the coverage results?
- In Table 1, what do the bold numbers represent?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a two-phase framework, SUPE, which leverages data in two stages: first, extracting low-level skills during the offline pre-training phase, and then using these skills and unlabeled data in the online phase to train a high-level strategy for more efficient exploration. Building on prior works like SPiRL [1] and ExPLORe [2], the key contribution of this paper is to integrate unlabeled data with online data to accelerate exploration and training in off-policy reinforcement learning (RL) methods. In the offline pre-training stage, the authors train a set of low-level skills, while in the online phase, they develop a high-level policy by utilizing both online data and relabeled offline data. To assess the method’s effectiveness, the authors compare SUPE with several baselines using benchmarks such as D4RL, and also discuss its limitations and potential directions for future research.

[1] Pertsch, Karl, Youngwoon Lee, and Joseph Lim. "Accelerating reinforcement learning with learned skill priors." Conference on robot learning. PMLR, 2021.

[2] Li, Qiyang, et al. "Accelerating exploration with unlabeled prior data." Advances in Neural Information Processing Systems 36 (2024).

### Strengths
* The paper is highly detailed, well-written and provides detailed motivation. The complete code is also provided.
* The authors conduct numerous experiments to thoroughly validate their method and address in detail several key issues that I am particularly concerned about, including its scalability, robustness.

### Weaknesses
 * The overall novelty of this work is somewhat limited, as it builds heavily on existing methods and concepts (mentioned in summary).
* Although numerous experiments are conducted, the selected tasks are relatively monotonous and simplistic. The experiments test only two types of tasks: AntMaze and Kitchen.
* Given the similarities between SPiRL [1] and this work, apart from the online reinforcement learning stage, why isn’t SPiRL used as a baseline for comparison (despite the numerous experiments conducted) ?
* In the pre-training stage, it would also be valuable to discuss whether trajectory segment length $H$ significantly impacts the method's performance.
* I am curious whether using expert data would result in better low-level skills during the pre-training stage.

### Questions
* See weakness above. 
* Given the similarities between SPiRL [1] and this work, apart from the online reinforcement learning stage, why isn’t SPiRL used as a baseline for comparison (despite the numerous experiments conducted) ?
* In the pre-training stage, it would also be valuable to discuss whether trajectory segment length $H$ significantly impacts the method's performance.
* I am curious whether using expert data would result in better low-level skills during the pre-training stage.

[1] Pertsch, Karl, Youngwoon Lee, and Joseph Lim. "Accelerating reinforcement learning with learned skill priors." Conference on robot learning. PMLR, 2021.

### Soundness
2

### Presentation
3

### Contribution
2
