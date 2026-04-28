# Diffusion Guided Adversarial State Perturbations in Reinforcement Learning

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 5, 3, 6

## Abstract
Reinforcement learning (RL) systems, while achieving remarkable success across various domains, are vulnerable to adversarial attacks. This is especially a concern in vision-based environments where minor manipulations of high-dimensional image inputs can easily mislead the agent's behavior. To this end, various defenses have been proposed recently, with state-of-the-art approaches achieving robust performance even under large state perturbations. Upon closer investigation, however, we found that the effectiveness of the current defenses is due to a fundamental weakness of the existing $l_p$-norm constrained attacks, which can barely alter the semantics of the input even under a relatively large perturbation budget. In this work, we propose SHIFT, a novel diffusion-based state perturbation attack to go beyond this limitation. Specifically, we train a history-conditioned diffusion model, enhanced with policy guidance and realism detection to generate perturbed states that are semantically different from the true states while remaining realistic and history-aligned to avoid detection. Evaluations show that our attack effectively breaks existing defenses, including the most sophisticated ones, and significantly lowers the agent's cumulative reward in various Atari games by more than 50\%. The results highlight the vulnerability of RL agents to semantics-aware adversarial perturbations, indicating the importance of developing more robust policies for safety-critical domains.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper studies how to generate state perturbations for reinforcement learning, especially perturbation in an unconstrained way, instead of traditional L_p perturbations. The methods are based on diffusion models to generate states with different semantics. The experiments outperforms some existing baselines.

### Strengths
1. The paper studies an interesting question of non-L_p attacks, which is largely neglected by existing literature.
2. The methods can scale to image-input domain

### Weaknesses
1. One concern/question is that the goal of the paper is not very concrete. The paper said existing methods cannot change the semantics of the image input while this paper can. However, it is not very clear why the attacker has the motivation to change the semantics? In other words, isn't being stealthy beneficial for the attacker? 
2. Some newest/recent defense baselines to my best knowledge [1, 2] are not discussed or compared in experiments. These game-theoretical based defense methods are significantly different from the defense mechanisms discussed in the paper by nature, and more importantly agnostic to the attacker model (which means one only need to change the attacker model to non-L_p accordingly to extend the defense to non-L_p). Therefore, it will be important to evaluate how the attacks performs under such kind of defense strategies.

### Questions
see weakness

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces SHIFT, a diffusion-based adversarial attack that targets RL agents in vision-based environments by creating realistic, history-aligned state perturbations that go beyond traditional lp-norm attacks. Unlike existing methods, SHIFT generates semantic changes that significantly impair the agent's performance, bypassing even the most advanced defenses. Results demonstrate the attack's efficacy, reducing cumulative rewards by over 50% in Atari games, underscoring the need for more robust defenses in RL.

### Strengths
1. This work proposes semantic-level RL attacks using conditional diffusion models that balance semantic changes, realism, and historical consistency. The insight is novel.
2. Identifies a fundamental weakness in lp-norm attacks - their inability to meaningfully alter state semantics despite large perturbation budgets.
3. Employs EDM to enhance generation efficiency, making the approach more feasible

### Weaknesses
1. Despite using EDM and weighting joint, the paper lacks any systematic analysis of attack efficiency and computational costs. Specifically, there is no discussion on the time taken for generating a single adversarial example, nor is there any analysis of the computational resources required for training the diffusion model and the autoencoder. This makes it difficult to assess the practical feasibility of the proposed attack.
2. While reporting larger attack budgets, results are limited to PGD and MinBest baselines, missing broader comparative analysis. The paper should include more recent and stronger adversarial attack baselines, such as those that consider the temporal aspect of the environment, to better contextualize the performance of SHIFT. The lack of comparison against a wider range of attack methods limits the conclusions that can be drawn about the effectiveness of the proposed approach.
3. Experiments are restricted to only three Atari environments, providing insufficient evidence for the method's generalizability. The selected environments might not be representative of the broader spectrum of RL tasks, and the results might not hold for more complex or diverse environments. The paper needs to demonstrate the robustness of the attack across a wider range of environments to support its claims.
4. Overall Soundness: While the core idea is interesting, the paper falls short in rigor - lacking ablation studies, methodology analysis, and comprehensive experiments. The current evaluation scope is not convincing enough to support the claims. For example, there is no ablation study on the effect of different diffusion model parameters or the impact of the realism detector on the attack performance. The lack of such analysis makes it difficult to understand the contribution of each component of the proposed method.

### Questions
1. The Manipulation Rate and Deviation Rate metrics appear exclusive to SHIFT's diffusion-based approach, raising questions about fair comparison with non-diffusion methods. The necessity of diffusion models needs stronger justification.
2. The paper lacks crucial comparison between DDPM and EDM in terms of both effectiveness and efficiency. This missing analysis weakens the justification for the chosen architecture.
3. Overlooks recent related work [1] about temporally-coupled perturbations

[1]Game-Theoretic Robust Reinforcement Learning Handles Temporally-Coupled Perturbations, Liang et al, ICLR 2024

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The submission claims to find that the effectiveness of the current defenses is due to a fundamental weakness of the existing $\ell_p$-norm constrained attacks. Furthermore, the submission proposes a method to go beyond the $\ell_p$-norm bounded adversarial attacks in deep reinforcement learning. The submission evaluates its proposed attacks in Atari games and argues that the proposed attack method of the submission lowers the cumulative rewards of the agent by 50%.

### Strengths
AI safety and robustness is an important research area.

### Weaknesses
The major claimed contributions of the submission have been previously both mentioned and analyzed in previous work [1]. However, the submission does not refer to these studies, and furthermore, within the existing prior work the main claimed contributions of the submission are rather misplaced and inaccurate. The paper [1] already extensively studies and demonstrates that both deep reinforcement learning policies and current defenses, i.e. robust deep reinforcement learning, are not robust against semantically meaningful adversarial attacks and this study further reveals the need to have robustness beyond $\ell_p$-norm bounded attacks.

Not only has the necessity of considering beyond  $\ell_p$-norm bounded attacks already been discussed in previous work, furthermore the approach proposed in this paper [1] achieves higher degradation on the policy performance without even having access to the training details, the policy network (i.e. black-box adversarial attacks), and further without even training any additional network to produce such adversarial examples.

The submission substantially lacks appropriate references, and further positioning itself within the existing prior work and clarifying its main contributions within these studies. The claimed contributions of the submission are misplaced and incorrect.  

[1] Adversarial Robust Deep Reinforcement Learning Requires Redefining Robustness. AAAI Conference on Artificial Intelligence, AAAI 2023.

Furthermore, the submission lacks main technical details to interpret their experimental results. Not a single experimental detail is provided regarding deep reinforcement learning. These details are essential for reproducibility and further to interpret and analyze the experimental results provided in the submission. However, the submission does not provide any information on this. 

The submission only tests their algorithm in 3 games from Atari. However, in adversarial deep reinforcement learning it is usually tested in more games [1,2,3,4]. In particular, RoadRunner is missing from the baseline comparison.

[1] Robust deep reinforcement learning against adversarial perturbations on state observations, NeurIPS 2020.

[2] Robust Deep Reinforcement Learning through Adversarial Loss, NeurIPS 2021.

[3] Adversarial Robust Deep Reinforcement Learning Requires Redefining Robustness, AAAI 2023.

[4] Detecting Adversarial Directions in Deep Reinforcement Learning to Make Robust Decisions, ICML 2023.

The submission also refers to main concepts in the adversarial machine learning literature with inaccurate wording. For instance, in the introduction the submission writes: 

*“by poisoning its observation (Huang et al., 2017; Zhang et al., 2020a)”*

However, poisoning attacks in adversarial machine learning literature refer to completely something else and these papers are not poisoning attacks. These papers are test time attacks. Thus, it is misleading to use the word poisoning here. 

One thing I find ineffective is that the submission refers to a long list of papers such as these [1,2,3,4,5], however, somehow still misses the prior work that substantially coincides with the main claimed contributions of the submission and even further these prior studies already demonstrate the claimed contributions of this submission.

[1] Kangjie Chen, Shangwei Guo, Tianwei Zhang, Xiaofei Xie, and Yang Liu. Stealing deep reinforcement learning models for fun and profit. ACM Asia Conference on Computer and Communications Security, 2021.

[2] Mengdi Huai, Jianhui Sun, Renqin Cai, Liuyi Yao, and Aidong Zhang. Malicious attacks against deep reinforcement learning interpretations. ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, 2020.

[3] Yunhan Huang and Quanyan Zhu. Deceptive reinforcement learning under adversarial manipulations on cost signals. Decision and Game Theory for Security (GameSec), 2019.

[4] Zikang Xiong, Joe Eappen, He Zhu, and Suresh Jagannathan. Defending observation attacks in deep reinforcement learning via detection and denoising. Machine Learning and Knowledge Discovery in Databases: European Conference 2023.

[5] Inaam Ilahi, Muhammad Usama, Junaid Qadir, Muhammad Umar Janjua, Ala I. Al-Fuqaha, Dinh Thai Hoang, and Dusit Niyato. Challenges and countermeasures for adversarial attacks on deep reinforcement learning. ArXiv 2020.

### Questions
See above

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel non-$\ell_p$ attack algorihtm for image-observation reinforcement learning, based on a history-conditioned diffusion model. The generated attacks are semantically meaningful while misleading to the agent. Experiments show that the proposed SHIFT attack can significantly break existing robust RL learning algorithms that are mainly designed for $\ell_p$ attacks.

### Strengths
- The paper points out the limitation of mostly-studied $\ell_p$ attack model for image-observation reinforcement learning environments. By utilizing a denoising diffusion probabilities model (DDPM), the paper achieves stealthy and realistic attack by altering the semantic meaning of the original state. 
- The paper clearly defines the concept of valid and realistic states and adopts an autoencoder to enhance the realism of the generated attacks.
- Comparison with existing methods show that SHIFT can lower the reward of agent while having low state reconstruction error.
- The paper also proposes a possible defense method agains the new attack model.

### Weaknesses
 - Although the proposed attack uses methods such as autoencoder guidance to enhance the realism of the perturbed states, it is not guaranted or bounded like $\ell_p$ attacks, making it hard to compare and evaluate the stealthiness of the perturbations. It is not clear to me whether the reconstruction error can effectively represent the realism of the state perturbation. It would be better if the authors can provide a gif or video showing the full perturbed trajectory.
- The experiments are not very informative. It is not surprising that RL agents learned via $\ell_p$ attack assumptions will break under the proposed attack. But more empirical study can be done to verify the effectiveness of the proposed design. For example, how does the varying attack strengh influence the attack effects?

### Questions
As the author mentioned, the proposed method uses a myopic target action manipulation objective which can be sub-optimal. Is there a way to improve it? For example, how can it be combined with RL-based attack methods such as PA-AD?

### Soundness
3

### Presentation
3

### Contribution
3
