# Towards Robust Offline Reinforcement Learning under Diverse Data Corruption

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
Offline reinforcement learning (RL) presents a promising approach for learning reinforced policies from offline datasets without the need for costly or unsafe interactions with the environment. However, datasets collected by humans in real-world environments are often noisy and may even be maliciously corrupted, which can significantly degrade the performance of offline RL. In this work, we first investigate the performance of current offline RL algorithms under comprehensive data corruption, including states, actions, rewards, and dynamics. Our extensive experiments reveal that implicit Q-learning (IQL) demonstrates remarkable resilience to data corruption among various offline RL algorithms. Furthermore, we conduct both empirical and theoretical analyses to understand IQL's robust performance, identifying its supervised policy learning scheme as the key factor. Despite its relative robustness, IQL still suffers from heavy-tail targets of Q functions under dynamics corruption. To tackle this challenge, we draw inspiration from robust statistics to employ the Huber loss to handle the heavy-tailedness and utilize quantile estimators to balance penalization for corrupted data and learning stability. By incorporating these simple yet effective modifications into IQL, we propose a more robust offline RL approach named Robust IQL (RIQL). Extensive experiments demonstrate that RIQL exhibits highly robust performance when subjected to diverse data corruption scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper concerns the robustness of different offline reinforcement learning methods to comprehensive data corruption, including states, actions, rewards, and dynamics. Their empirical results show that IQL method has better robustness to all types of data corruptions except noisy dynamic. The authors first give a theoretical explanation about IQL's robust performance, and according to empirical evidence, attribute this exceptional phenomenon to the heavy-tailed Q-targets. To verify this assumption and address this issue, this paper adopts observation normalization and Huber loss function for robust value function learning. Besides, this paper finds the potential negative value exploding issue of the clipped double Q-learning technique used in the original IQL and adopts quantile Q estimators instead of the LCB estimation. All the above modifications are verified to improve the performence of IQL under the data corruption of enviorment dynamic.

### Strengths
1. This paper provides comprehensive analysis and interesting findings on different types of data corruption in the offline RL;
2. Sufficient empirical evidence on the possible reason of the failure setting, and efficient solutions to address these issues.

### Weaknesses
1. Lack theoretical evidence on heavy-tailed Q-target issue;
2. Heavy work on parameter finetuning;

### Questions
In Fig.1 only two scales are illustrated, would you please make it more clear about the underlying mechanism that generates the corrupted data in each cases,  and how to ensure that the generated noisy data is realistic and representative in the sense that they do represent typical noisy data we encountered in practice? Intuitively, different level of noise would lead to different robustness outcomes of various algorithms - in this sense, how do you ensure that the empirical evidence is conclusive?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work concentrates on dealing with diverse types of data corruption associated with state, action, reward, and transition kernel in offline RL history datasets. In particular, it first did data corruption test on some existing offline RL algorithms to show their vulnerable behaviors against data corruption. A theoretical result for the robustness of IQL has been shown w.r.t. the data corruption ratio. Then a robust variant of IQL has been proposed and outperform offline RL baselines, which consist of three key parts: state normalization, Huber loss, and $\alpha$-quantile Q ensemble.

### Strengths
1. It shows interesting testing of the effect of data corruption for current offline RL algorithms.
2. Some theoretical relationship between the data corruption ratio and the performance of IQL is presented.
3. A new robust IQL algorithm has been proposed and outperforms conducted baselines when data corruption appears.

### Weaknesses
1. Except for the traditional offline RL algorithms based on TD learning or the Bellman operator, there exists some other new baselines using a transformer or a diffusion model. It is helpful to involve the discussion about such algorithms at least.
2. Since the new algorithm (RIQL) involves in ensemble, which is a very powerful trick in RL algorithms, it is better to add some baselines that also use ensemble Q, while not appearing in the experiments if I didn't miss something.
3. There does not exist comparisons between the proposed algorithm RIQL to other existing robust RL algorithms, but only to non-robust counterparts.

### Questions
1. Is there any study on ablation study for the proposed RIQL that is similar to Figure 1. It will be helpful to see how can RIQL handle different types of data corruption.

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
This paper proposes Robust IQL (RIQL), an offline RL algorithm that works decently even when the dataset is corrupted. It first experimentally and theoretically shows that IQL is robust to dataset noise. Adding upon the discovery, it presents three heuristics that can further improve IQL's performance on the corrupted dataset: (1) observation normalization, (2) Huber loss for value function learning, (3) using the $\alpha$-quantile of an ensemble of Q functions as the target value. The authors conducted experiments on varying the degree and type of corruption and showed that RIQL outperforms other baselines in most of the settings.

### Strengths
The paper tackles a novel problem where the offline dataset is corrupted. It provides an exact error bound of IQL under the data contamination setting supported by a mathematically sound argument. The paper also presents an interesting discovery that the Q target distribution has heavy tails and suggests a simple but clever solution, which is to use the Huber loss instead of an MSE loss. To prove the effectiveness of RIQL, multiple experiments were conducted, together with a thorough ablation study. Finally, the paper is overall well-written and easy to understand.

### Weaknesses
1. The paper provides no plausible scenarios where a malicious attack on the offline dataset would occur.

2. The definition of $\pi_{\mathcal{D}}(a\mid s)$ is unclear.

3. The paper assumes that IQL can learn the optimal value function $V^*$ from the corrupted dataset without justification.

4. The random corruption setting used in the experiments is a bit unrealistic.

    * If environmental noise exists, the entire dataset would be corrupted, not just a tiny portion as assumed in the experiments.

    * Most offline RL datasets are collections of trajectories not $(s, a, r, s')$ 4-tuples. Adding random noise just to $s$ or $s'$ does not seem to make much sense.

5. The adversarial corruption setting is not really "adversarial" towards algorithms other than EDAC since the adversarial noise was computed via projected gradient descent with respect to the Q functions learned by EDAC. To see whether RIQL is robust to malicious attacks, the adversarial noise should be computed with respect to $Q_\alpha$ learned by RIQL.

6. The paper does not contain experiments for sequence-modeling-based algorithms such as Decision Transformer (Chen et al., 2021) or Diffuser (Janner et al., 2022). As the sequence modeling approach is one of the main branches of offline RL, I believe they should be included.

### Questions
1. The main theorem holds for any algorithm that uses AWR to learn the optimal policy. Is it possible to add experimental results of other algorithms based on AWR?

2. Does observation normalization also improve the performance of other algorithms?

3. The sentence "This is likely because normalization can help to ensure that the algorithm's performance is not unduly influenced by larger-scale features." from §4.1 is difficult to understand.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the authors investigate the robustness of offline RL algorithms when dealing with data corruption, including states, actions, rewards, and dynamics. 
They then introduce Robust IQL (RIQL), an offline RL algorithm that enhances robustness through observation normalization, Huber loss, and quantile Q estimators. 
Empirical evaluations demonstrate RIQL's exceptional resistance to various data corruption types, both random and adversarial. 
This research sheds light on the vulnerability of current offline RL algorithms and provides a promising solution to enhance their robustness in real-world scenarios.

### Strengths
+ This study illuminates the susceptibility of existing offline RL algorithms while offering a promising approach to bolster their resilience in real-world environments. The proposed analysis is unquestionably relevant to the offline RL community. While there have been previous works (e.g., Zhang et al. (2022)) that offer theoretical analyses regarding the impact of using contaminated data in offline RL algorithms, this work appears to take it a step further by examining the impact of various forms of contamination (actions, states, etc.) and providing a highly detailed analysis for the offline IQL model. As a conclusion, it suggests a robust alternative for IQL, addressing how to mitigate its identified weaknesses.


+ The theoretical and experimental analysis presented in Section 3 is elegantly and clearly articulated. The authors' discovery about the robustness of using a weighted imitation learning strategy is intriguing, but for the specific case of dynamics corruption, this doesn't seem to hold true. This observation leads them to propose up to three modifications to the IQL model to enhance its robustness. Each of these modifications (observation normalization, Huber loss, and quantile Q estimators) is well-founded and justified.

+ The experimental evaluation is comprehensive and very detailed. First, all state-of-the-art models in offline-RL are assessed to see how they perform in perturbation scenarios. Once the analysis is completed, the article focuses on improvements for the IQL model. The environments used for the experiments are well-known within the community (Halfcheetah, Halfcheetah, Halfcheetah). The results presented are conclusive. I also appreciate the ablation study in section 5.3, which allows the reader to understand the impact of the modifications applied to IQL until achieving the robust version (RIQL).

### Weaknesses
 - Some particularly interesting, and I would say more challenging, environments have been left out of the experimental analysis, especially in terms of the potential impact of perturbations, and in which the original IQL model was tested. It would be interesting to hear the authors' opinion on this. I'm referring to the following environments: locomotion-v2, antmaze-xx, kitchen, adroit.

- Somewhat, the theoretical analysis and the experimental evidence detailed in the section appear contradictory. The paper explicitly states this as follows: "Our theoretical analysis suggests that the adoption of weighted imitation learning inherently offers robustness under data corruption. However, empirical results indicate that IQL still remains susceptible to dynamics attacks".  This contradiction is not further examined in the manuscript. On the contrary, what is proposed is to address IQL's issue with dynamic attacks.

- Previous works on certification protocols for offline RL against attacks has not been considered for the novel RIQL model proposed. This is an important weaknesses that should be addressed in the rebuttal. Specifically, the authors should discuss why the proposed method was not tested against the COPA protocol, which provides a framework for certifying robustness in offline RL against adversarial attacks. The lack of such an analysis makes it difficult to assess the true robustness of RIQL in a certified manner.

- Minor comments:
(Wu, 2022) Update the reference as it is not anymore an ArXiv manuscript but an ICLR22 paper.

### Questions
- As I pointed above, Have the authors evaluated how RIQL performs in any of the environments I mentioned above?
- Why hasn't the new model RIQL been tested on the COPA protocol in (Wu, 2022)?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
