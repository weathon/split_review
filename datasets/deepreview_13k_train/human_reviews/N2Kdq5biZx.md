# Planning to Go Out-of-Distribution in Offline-to-Online Reinforcement Learning

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
Offline pretraining with a static dataset followed by online fine-tuning (offline-to-online, or OtO) is a paradigm well matched to a real-world RL deployment process. In this scenario, we aim to find the best-performing policy within a limited budget of online interactions. Previous work in the OtO setting has focused on correcting for bias introduced by the policy-constraint mechanisms of offline RL algorithms. Such constraints keep the learned policy close to the behavior policy that collected the dataset, but we show this can unnecessarily limit policy performance if the behavior policy is far from optimal. Instead, we forgo constraints and frame OtO RL as an exploration problem that aims to maximize the benefit of online data-collection. We first study the major online RL exploration methods based on intrinsic rewards and UCB in the OtO setting, showing that intrinsic rewards add training instability through reward-function modification, and UCB methods are myopic and it is unclear which learned-component's ensemble to use for action selection. We then introduce an algorithm for \textbf{p}lanning \textbf{t}o \textbf{g}o \textbf{o}ut-\textbf{o}f-\textbf{d}istribution (PTGOOD) that avoids these issues. PTGOOD uses a non-myopic planning procedure that targets exploration in relatively high-reward regions of the state-action space unlikely to be visited by the behavior policy. By leveraging concepts from the Conditional Entropy Bottleneck, PTGOOD encourages data collected online to provide new information relevant to improving the final deployment policy without altering rewards. We show empirically in several continuous control tasks that PTGOOD significantly improves agent returns during online fine-tuning and avoids the suboptimal policy convergence that many of our baselines exhibit in several environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work focuses on offline-to-online (OtO) setting with limited budget online interactions. In particular, the proposed planning to go out of distribution (PTGOOD) treats this problem as an exploration problem and encourages the exploration on the dataset that is unlikely to be visited by the behavior policy. The experiments show that the proposed method can improve the learning performance comparing with previous methods.

### Strengths
1. This paper aims to solve an important problem in the OtO setting and the derived algorithm show the promising results in the DMC tasks 
2. The exploration perspective is novel, which is in contrast with previous with regularization on the policy when exploring the out of distribution data.

### Weaknesses
1. The writing can be really hard to follow. The exploration approach is supposed to be used to motivate the proposed PTGOOD as in introduction. In section 4, many details of PTGOOD are referred to the following sections. The authors need to organize the paper in a different way
2. The core of the proposed method is to "target online exploration in relatively high-reward regions of the state-action space unlikely to be visited by the behavior policy". However, it is unclear what is "relatively high-reward regions", e.g., what is the criterial for choosing those regions. This lack of clarity significantly weakens the novelty and practical impact of the method. The paper does not provide a concrete definition or a quantifiable measure for identifying these regions, making it difficult to understand how the algorithm effectively targets them. Without a precise characterization, the claim of targeted exploration remains unsubstantiated.


### Questions
1. How does the learnt dynamics model $\hat{T}$ have impact on the PTGOOD planning procedure, e.g., the accuracy of the model vs. the performance of the PTGOOD
2. What is the explanation of the low variance in Figure 1 when choose small $\lambda$

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper targets on the offline-to-online setting. Different with prior works, this paper frame offline-to-online setting as an exploration problem. For this reason, the authors study major online RL exploration paradigms and adpat them to work in this setting. This paper proposes an new method, named PTGOOD, which targets online exploration in relatively high-reward regions to encourage collect informative data. The authors show its performance in several tasks.

### Strengths
1. This paper is written well and easy to follow. The writing of the article is very clear. 
2. The author gives a different perspective from previous work in offline-to-online setting, that is, using an exploratory approach to handle the switch from offline to online environments.

### Weaknesses
1. Although the authors tried to approach the offline-to-online problem from an exploratory perspective, they did not prove their claims through extensive experiments. For example, the experiments in Table 2 are too limited and only include 6 tasks. I suggest the authors provide additional experimental results in complete D4RL tasks to verify their claims. The selection of tasks seems arbitrary, and a more rigorous justification for the chosen environments is needed. Furthermore, the performance differences between PTGOOD and other methods, while present, are not overwhelmingly large in some cases, raising questions about the practical significance of the proposed approach.
2. In recent years, there has been rapid development in the field of offline-to-online RL, with numerous relevant works published. It is crucial for the authors to include and discuss these more recent works in the related works section, like AWAC[1], E2O[2], PROTO[3], SUNG[4] and PEX[5]. The absence of a thorough comparison with these methods makes it difficult to assess the novelty and contribution of the proposed approach within the broader context of the field. Specifically, the related works section should discuss the specific mechanisms employed by these methods and how they differ from the proposed PTGOOD approach.
3. I have serious doubts about the reproduction of Cal-QL. Cal-QL does not seem to work at all in picture 11. This is very different from the results in the original paper. Why is this? The authors should provide a detailed explanation of the implementation and hyperparameter settings used for Cal-QL to ensure a fair comparison. The discrepancy between the reported results and the original paper raises concerns about the validity of the experimental setup.

### Questions
1. The author claims that traditional exploration methods do not work, such as internal rewards and UCB. What will happen if naive exploration methods are used, such as epsilon exploration?
2. In the online stage, does the author use standard online RL algorithms, such as SAC and TD3, or does he use the online version of the offline learning algorithm?

-------

Thanks for the authors' explanation. I maintain my score since I believe this paper has a lot of room for improvement.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a new method for offline-to-online RL (oto RL), where the paper proposes that during the online fine-tuning stage, the policy perform exploration in a controlled manner and the exploration is determined by the visitation distribution of the current policy (or how out-of-distribution the state-action is). The paper proposes a way to measure the out-of-distribution-ness using conditional entropy bottleneck. Finally the paper compares the proposed algorithm with other baselines on a rage of offline-to-online benchmarks.

### Strengths
1. The paper proposes a natural way to address the oto RL problem: during the online fine-tuning stage, performing exploration to cover the unexplored region (thus out-of-distribution) seems a very reasonable strategy, and the paper suggests that one should also perform the exploration in a more careful manner (taking the return into account), which is a reasonable heuristic in practice. 

2. The proposed algorithm is easy to understand and extensible (for a wide range of offline RL methods). 

3. The empirical performance seems strong.

### Weaknesses
1. Although there seems no issue with the technical part of the paper, I do want to bring the attention to a recent paper: Reward-agnostic Fine-tuning: Provable Statistical Benefits of Hybrid Reinforcement Learning (https://arxiv.org/abs/2305.10282). I believe this paper, from the theory perspective, proposes the same intuition as the current paper: after running model-based offline RL on the offline dataset, one could use the model to estimate the occupancy measure of the offline policy, and thus have the knowledge of the uncovered directions from the offline data, and during online fine-tuning, one could use exploration to collect the data in the remaining directions. To me the current paper shares a lot of intuition with this earlier paper, minus many empirical considerations, which are also good contributions. 

2. Other than CEB, there might be many other methods for measuring the out-of-distributioness. It would improve the paper if there are more ablations. Specifically, the paper could explore other representation learning techniques, such as contrastive learning or autoencoders, to see if they offer different or improved performance in identifying out-of-distribution state-action pairs. The justification for using CEB is somewhat weak, and a more thorough investigation is needed.

3. The experiment section seems to miss of of the benchmarks that are tested in cal-QL. The absence of these benchmarks makes it difficult to compare the proposed method with a recent and relevant baseline. The paper should either include these benchmarks or provide a strong justification for their exclusion.

4. Minor point: in the related work section, two cited paper (Nair et al., 2020 and Song et al., 2023) seem to be more general than just using expert demonstration. I believe they also use the more general offline data (the same as the ot2 setting).

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
