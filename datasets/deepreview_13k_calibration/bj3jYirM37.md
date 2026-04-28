# Can Agent Learn Robust Locomotion Skills without Modeling Environmental Observation Noise?

- Decision: Reject
- Avg Score: 5.67
- Scores: 8, 3, 6

## Abstract
Deep Reinforcement Learning (DRL) has been widely attempted for solving locomotion control problems recently. Under the circumstances, DRL agents observe environmental measurements via multi-sensor signals, which are usually accompanied by unpredictable noise or errors. Therefore, well-trained policies in simulation are prone to collapse in reality. Existing solutions typically model environmental noise explicitly and perform optimal state estimation based on this. However, there exists non-stationary noise which is intractable to be modeled in real-world tasks. Moreover, these extra noise modeling procedures often induce observable learning efficiency decreases. Since these multi-sensor observation signals are universally correlated in nature, we may use this correlation to recover optimal state estimation from environmental observation noise, and without modeling them explicitly. Inspired by multi-sensory integration mechanism in mammalian brain, a novel Self-supervised randomIzed Masked Augmentation (SIMA) algorithm is proposed. SIMA adopts a self-supervised learning approach to discover the correlation of multivariate time series and reconstruct optimal state representation from disturbed observations latently with a theoretical guarantee. Empirical study reveals that SIMA performs robust locomotion skills under environmental observation noise, and outperforms state-of-the-art baselines by 15.7% in learning performance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
For DRL-based locomotor control tasks, the ability to adjust to environmental observation noise is essential. Due to the existence of non-stationary noise, modeling is difficult or impossible. Previous works lack effective solutions for the above problems. In this paper, the authors present a method for learning robust locomotion skills without explicitly modeling noise from environmental observations. Inspired by multi-sensory integration mechanism, the authors first formulate the MDP with an environmental de-noising process as a DRPOP problem. Based on this, the authors propose a Self-supervised randomIzed Masked Argumentation (SIMA) algorithm to learn the internal correlation of multivariate time series and reconstruct latent state representation from noisy observations. The experiments on locomotion control tasks demonstrate that the proposed algorithm performs robust locomotion skills under environmental observation noise, and outperforms state-of-the-art baselines by 15.7% in learning performance.

### Strengths
I would like to appreciate the authors for the submission of such high-quality manuscripts.

From a high-level point of perspective, this appears to be a very well-structured work. Related work covers deep reinforcement learning, observation de-noising, and masked multivariate time series modeling completely. The authors are really good storytellers and the topic is novel. This paper is well written and each section is well detailed, especially the introduction section and the methodology section, which is precisely to the point. I truly enjoy every figure. The authors put a great deal of effort into refining the figures.

### Weaknesses
1. In section 5.1 LEARNING PERFORMANCE UNDER ENVIRONMENTAL OBSERVATION NOISE (RQ1), the performance of the proposed algorithm shows sharp declines in all locomotion control tasks. I suggest the authors to add more contents to analyze the causes in the manuscript. What's more, more training steps should be visualized since the performance of some baselines is still increasing such as RL-DR and RL-vanilla in the Walker2D environment.

2. There are so many abbreviations throughout the paper, e.g., DRPOP, SIMA, VICOR, RMA, and MASOR, making them difficult to understand. In my humble opinion, one or two abbreviations are good.

### Questions
1. I suggest the authors to attempt BetaVAE and Beta-TC-VAE as the generative model to encode masked state observation into the the latent state representation and reconstruct state observation from latent state representation.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a reinforcement learning framework under correlated observational noise. The paper assumes that the ground-truth state observation can be recovered from different sensor modalities and proposes a denoising method by using a masked reconstruction technique. Once the training trajectories are denoised, the paper then trains a student policy using the denoised trajectories through imitation learning. Experiments are done for a set of locomotion tasks built on top of pybullet.

### Strengths
The paper deals with an important problem of learning robust policies for sim2real transfer and is well motivated by the multi-sensory integration observation. The approach is overall sound.

### Weaknesses
1. The main experiment shows marginal improvements over the baseline. Figure 4 is quite suspicious: SIMA mostly performs the same as the baselines but will have sudden drops in performance, after which the performance will rise again. This suggests a mistake in the experimental setting or visualization.

2. The idea of masked modeling for reinforcement learning is not new. See [1], [2]. Masked modeling itself could help improve the sample efficiency and robustness to noises. The paper does not make comparisons with these methods.

3. The writing of the paper could be further improved, by reducing the use of long abbreviations, e.g. VICOR, RMA (the name is also used in a different sim2real transfer for locomotion paper), MASOR

### Questions
See weakness.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a self-supervised method, self-supervised randomized masked augmentation, to discover the correlation of multi-variable time series data to reconstruct the optimal state representation. The authors give theoretical guarantees and verify the method's empirical improvement on locomotion tasks for RL algorithms.

### Strengths
- The paper proves the effectiveness of the method from both theoretical and experimental perspectives.

- The paper is well written. The authers present the whole framework clearly, and the experimental part explains the advantages of the method with several questions.

- The paper has the case studies to demonstrate the effect of state reconstruction, and the policy distribution unorder the reconstructed states.

### Weaknesses
 - The paper shows the algorithm boosts the stability of the training process. However, it does not consider whether the method is robust when the test environment has random noises with different distributions. The auothers should consider if the policy is robust in unseen noise distribution, which is much more essential for using RL in the real-world.

- The paper mainly compares whether the training curves of various RL algorithms is better than SIMA when combined with some relatively simple encoders (filters, lstm). However, I think this is slightly unfair for state representation learning. The process of SIMA is obviously more complicated and uses more training objectives. The author should compare it with more solid works on state representation learning for locomotion are, such as [1][2].

### Questions
- Why do we have to use RL algorithms to get a teacher policy? Can we consider using classic control algorithms to generate teacher behaviors?
- Can the SIMA still perform better on a totally unseen noise distribution (after the student policy learning stage)? Is it still robust when noise distribution is shifted?
- In Appendix E, how are the scores calculated? Why can scores above 99 be achieved under clean experimental settings?
- How did the authors draw policy distribution? Is it t-SNE visualization of action? How the actions are sampled?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
