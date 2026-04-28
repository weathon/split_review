# Scaling Offline Model-Based RL via Jointly-Optimized World-Action Model Pretraining

- Decision: Accept
- Avg Score: 6.60
- Scores: 5, 8, 6, 6, 8

## Abstract
A significant aspiration of offline reinforcement learning (RL) is to develop a generalist agent with high capabilities from large and heterogeneous datasets. However, prior approaches that scale offline RL either rely heavily on expert trajectories or struggle to generalize to diverse unseen tasks. Inspired by the excellent generalization of world model in conditional video generation, we explore the potential of image observation-based world model for scaling offline RL and enhancing generalization on novel tasks. In this paper, we introduce JOWA: \textbf{J}ointly-\textbf{O}ptimized \textbf{W}orld-\textbf{A}ction model, an offline model-based RL agent pretrained on multiple Atari games with 6 billion tokens data to learn general-purpose representation and decision-making ability. Our method jointly optimizes a world-action model through a shared transformer backbone, which stabilize temporal difference learning with large models during pretraining. Moreover, we propose a provably efficient and parallelizable planning algorithm to compensate for the Q-value estimation error and thus search out better policies. Experimental results indicate that our largest agent, with 150 million parameters, achieves 78.9\% human-level performance on pretrained games using only 10\% subsampled offline data, outperforming existing state-of-the-art large-scale offline RL baselines by 31.6\% on averange. Furthermore, JOWA scales favorably with model capacity and can sample-efficiently transfer to novel games using only 5k offline fine-tuning data (approximately 4 trajectories) per game, demonstrating superior generalization.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents JOWA, an offline model-based reinforcement learning method aimed at scaling and generalizing multi-task RL through a shared transformer-based architecture. JOWA is designed to stabilize temporal difference learning for large models by integrating world modeling with Q-value criticism, thus leveraging a shared transformer backbone for both tasks. The paper introduces a novel parallelizable planning algorithm to counter Q-value estimation errors, achieving more consistent policy identification during inference. The model is pre-trained on Atari games with minimal data and reportedly outperforms existing baselines, demonstrating some generalization capacity to new tasks.

### Strengths
1. Scalability: JOWA’s design showcases robust scaling potential, as performance improves with model size without the usual TD-learning instability issues.

2. Detailed Ablation Studies: The authors conducted extensive ablations, examining the impact of core design elements such as task embeddings, training losses, and synthetic data usage.

### Weaknesses
1. Missing related work and explanations for the architecture of the world-action modeling. The work proposes to use VQ-VAE for the representation learning in Atari games, while there is a work named Forward-Inverse Cycle Consistency (FICC), which uses VQ-VAE for the offline Atari dataset to learn representations and action embeddings. It seems this pipeline is so similar to the FICC, however, the author didn't mention the difference between JOWA and FICC. (Both use offline Atari datasets for model-based RL and learning universal policy under VQ-VAE loss terms)

Ye, W., Zhang, Y., Abbeel, P., & Gao, Y. (2022). Become a proficient player with limited data through watching pure videos. In The Eleventh International Conference on Learning Representations.

2. Overclaim of the generalization ability. The experiments are based on Atari games, while using offline atari dataset for pre-training. Extending this approach to more complex control task scenarios (e.g., robotics or high-dimensional continuous control tasks) remains unproven. I'm not sure about the effectiveness of the scaling results.

### Questions
1. How might JOWA perform in a single-task setting compared to standard model-based methods? Would the shared architecture yield efficiency or performance gains? If it is worse than training from scratch with model-based RL, why the Atari games are good benchmarks for evaluating the scaling laws?

2. The author mentioned the beam search, so why not use MCTS, which is proven effective in MuZero and EfficientZero. And the author didn't compare with other model-based RL algorithms, such as Dreamer.

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
4

### Summary
This paper introduces a model-based RL agent, JOWA, which employs a transformer architecture and jointly optimizes world dynamics and Q-values across different environments. To compensate for inaccurate Q-values, the learned world model enables JOWA to search out the optimal policy via planning during inference time. Empirically, JOWA demonstrates impressive performance in a low-data regime by training on 15 Atari games. Moreover, JOWA's performance scales up with model sizes.

### Strengths
- The proposed JOWA outperforms existing SOTA methods by a large margin. The perform scales up with model sizes

- The joint optimization of world and action models stabilizes large-scale multi-task offline RL training.

- The ablation studies comprehensively study the key design choices of the proposed methods.

### Weaknesses
 - The proposed method combines the best offline RL training techniques, leveraging the world modeling loss to stabilize Q-value learning. The empirical performance is impressive. However, the technical novelty is thus limited.

- By taking a closer look at Table 2, we can see that the 150M variant does not consistently outperform the 40M and 70M variants on all tasks. For example, the 40M variant achieves the highest score on Centipede, while the 70M variant excels on NameThisGame, SpaceInvaders, and StarGunner. Can you explain the phenomenon a bit more? Is it because of the training instability? Can further increase the model size and training iterations solve the issue?

- It would be insightful to examine the emergent behaviors that arise when scaling up model size. For example, the 150M JOWA achieves a significantly higher score than the 70M JOWA and the other baseline methods on *Zaxxon*. Does the 150M JOWA agent exhibit any distinct emergent behaviors that could explain this performance improvement?

- This work misses the citation for [1,2]

### Questions
How's the model performance when you further scale up the model size, e.g., to 1B?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces JOWA, a Jointly-Optimized World-Action model for offline RL. By optimizing a shared transformer backbone for world-action modeling and employing an efficient planning algorithm to improve policy search, JOWA achieves good performance on pretrained games with limited data and demonstrates superior generalization to new games with minimal fine-tuning trajectories.

### Strengths
1. This paper is clearly written and easy to follow.
2. This paper presents sufficient experimental results to demonstrate the validity of its proposed method.

### Weaknesses
1. A large generalist TD-MPC2 agent is capable of performing a variety of tasks across multiple domains. I wonder if the proposed method is better than TD-MPC2 in the offline setup.
2. Extending the experiments beyond Atari to more complex environments like Kitchen or Meta-World would offer stronger validation of the proposed method's effectiveness.

### Questions
Please see the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces JOWA (Jointly-Optimized World-Action model), a novel offline model-based reinforcement learning (RL) agent designed for generalization across multiple tasks, specifically focusing on scaling RL with image-based observations. JOWA is pretrained on multiple Atari games using a shared transformer backbone that jointly optimizes a world model and action model. This setup allows the model to learn both general-purpose representations and decision-making skills.

JOWA stabilizes temporal difference learning by incorporating world modeling as a regularizer, enabling large models to scale effectively. The proposed framework also features a parallelizable planning algorithm to improve Q-value estimation and policy search at inference time. Experiments show that JOWA outperforms state-of-the-art offline RL methods, achieving 78.9% human-level performance on pretrained games and demonstrating strong sample-efficient transfer to novel games with minimal fine-tuning.

### Strengths
- Extension from Sequential Modeling: JOWA effectively adapts transformer-based architectures from NLP to reinforcement learning, leveraging tokenization for image observations and combining offline RL with online planning to scale across tasks.
- Strong Baseline Performance: It outperforms state-of-the-art methods, showing significant improvements on Atari benchmarks while requiring only 10% of the dataset.
- Adaptability: JOWA demonstrates efficient transfer to new tasks with minimal fine-tuning, highlighting its robustness and generalization capabilities.

### Weaknesses
 - Limited Originality: While JOWA effectively combines existing state-of-the-art techniques, it lacks substantial novelty in introducing new ideas. The core contributions largely build upon well-established methods, such as transformers, tokenization, and offline RL. The planning algorithm, while effective, is not fundamentally different from existing lookahead methods, and the joint optimization of world and action models is an incremental step rather than a significant breakthrough.
- Reliance on Expert Data for New Games: While JOWA demonstrates strong performance in fine-tuning to new tasks, it heavily relies on expert-level data for unseen games. This dependence on high-quality data might limit its applicability in scenarios where such data is not readily available or costly to obtain. The paper does not explore the model's performance when fine-tuned with suboptimal data, which is a more realistic scenario in many practical applications.
- Excessive Discretization: The paper discretizes the reward into the set {-1, 0, 1}, which may lead to a loss of important nuance and granularity in reward signals. This overly simplified reward structure might not capture the full complexity of more sophisticated environments, limiting the model’s performance in tasks requiring finer reward distinctions. This approach also makes it difficult to evaluate the model's ability to learn subtle differences in reward magnitude, which is crucial for many real-world tasks.

### Questions
- Why was the sequence length relative low (8)?
- Could JOWA learn useful policy on new games using non-expert transitions?
- It seems the number for MGDT are very different from the original paper (MGDT achieved 93% IQM HNS on 40M model). Why is this?
- Is the action-part module (CQL) hard to tune in this method?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper focuses on the important research question: "Can image observation-based world model scale offline RL across multiple tasks while enhancing generalization to diverse unseen tasks?". The paper presents JOWA, which 1) jointly trains a Transformer model that includes world model, policy, critic using the offline data, 2) planning with beam-search in inference-time using the trained world model. Experimental results in Atari tasks shows that JOWA trained with 10% of subsampled 15 tasks significantly outperforms previous multi-task offline RL approaches not only in in-distribution tasks, but also in fine-tuning with 5k expert demonstrations. Moreover, JOWA shows favorable scaling property respect to the number of parameters. Exhaustive ablation studies show the importance of individal components of JOWA.

### Strengths
S1. JOWA significantly outperforms previous multi-task offline RL approaches.
* Experimental results of Table 2 shows that JOWA gives state-of-the art result in multi-task offline RL with 10% subsampled Atari (Mean 0.456, IQM 0.789)
* Experimental results of Table 3 shows that JOWA significantly outperforms prior works in fine-tuning (Mean 0.647, IQM 0.647)

S2. JOWA shows favorable scaling property.
* Increase in the number of parameters leads to better performance.
* Compared to other methods, the performance increase is significant.

S3. Ablation studies shows useful insights on JOWA's performance.
* Planning with world model largely contributes the performance.
* Training policy jointly with the world model is important for multi-task agents.

S4. Open-source codes & checkpoints.
* Those resources will be helpful for the community.

### Weaknesses
W1. Evaluated only in Atari
* For example, continous tasks like DMControl are relatively simple but challenging.
* It will be exciting to see if JOWA can be also applied in continuous tasks.

W2. Discrepancy between Theorem 1 and planning of JOWA
* Although the planning emprically improves the performance, it seems that the theory slightly differs with the planning of JOWA. Specifcally, Theorem 1 assumes critic is the estimate of the optimal Q-function, but JOWA uses a conservative estimate (CQL). Thus, $Q(s, a) - Q*(s, a)$ will not be bounded by the term mentioned in Theorem 1; Q(s, a) will be much smaller than Q*(s, a) in reality.
* Please correct me in the point if I'm wrong.

### Questions
Q1. Can Theorem 1 be applied for planning of JOWA?
* Theorem 1 shows that error caused by model-based planning can be bounded. However, it assumes that the critic $Q(s,a)$ is the estimate of the optimal Q-function (i.e. $\mathbb{E}[\sum_t \gamma^t r_t]$). However, the critic is learned via CQL, which tends to underestimate the Q-values, as discussed in [1]. Thus, $Q(s, a) - Q*(s, a)$ will not be bounded by the term mentioned in Theorem 1; Q(s, a) will be much smaller than $Q^{*}(s, a) = \mathbb{E}[\sum_t \gamma^t r_t]$ in reality.
* Can you share your thoughts on this? Please correct me in the point if I'm wrong.

Q2. Scaling property in fine-tuning tasks
* Can you provide the fine-tuning results for JOWA-40M, JOWA-70M?
* I think it will be helpful on investigating scaling effects in fine-tuning.

Q3. Extending JOWA to continuous environments
* It would be exciting if JOWA can be also extended to continuous tasks. For example, continous tasks like DMControl are relatively simple but challenging.
* However, I understand that the training process is time-consuming and authors should put a lot of effort on this. Thus, I'm not strongly suggesting (but welcome) the authors to answer this question via additional experiments; if then, telling your thoughts or ideas on how to extend this work to continuous environments will be helpful for potential users of JOWA and future works.

[1] Mitsuhiko Nakamoto et al., Cal-QL: Calibrated Offline RL Pre-Training for Efficient Online Fine-Tuning, NeurIPS 2023.

### Soundness
4

### Presentation
3

### Contribution
3
