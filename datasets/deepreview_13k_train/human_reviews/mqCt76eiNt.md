# Advantage-Aware Policy Optimization for Offline Reinforcement Learning

- Decision: Reject
- Scores: 6, 6, 5, 5, 3

## Abstract
Offline Reinforcement Learning (RL)  endeavors to leverage offline datasets to craft effective agent policy without online interaction, which imposes proper conservative constraints to tackle the Out-Of-Distribution (OOD) problem. However, existing works often suffer from the constraint conflict issue when offline datasets are collected from multiple sources with distinct returns. To remedy this issue, previous Advantage-Weighted (AW) methods prioritize samples with high advantage values to perform agent training while inevitably leading to overfitting on these samples. In this paper, we introduce a novel Advantage-Aware Policy Optimization (A2PO) method to explicitly construct the advantage-aware policy constraint from the multi-source dataset for agent learning. Specifically, A2PO employs a Conditional Variational Auto-Encoder (CVAE) to  disentangle the action distributions of different behavior policies by modeling the advantage values of all training data as conditional variables. Then we can optimize the advantage-aware agent policy  towards high advantage values while adhering to such disentangled distribution constraint of the multi-source dataset. Extensive experiments conducted on both the single-source and multi-source datasets of the D4RL benchmark demonstrate that A2PO yields results superior to state-of-the-art counterparts. Our code will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce A2PO, which aims to learn an advantage-aware policy from offline RL datasets containing mixed-quality data. The proposed method first trains a CVAE over the actions and optimizes the advantage-aware policy towards high advantage values over the learned action embeddings. The experiments show that their method can outperform baselines such as CQL and LAPO.

### Strengths
1. The paper is easy to understand.
2. The experiments in the paper demonstrate the effectiveness of A2PO. The agent can learn to sample different actions based on the given advantages and can achieve good performance when given large advantages.

### Weaknesses
1. A comparison with diffusion-based methods is lacking. Figure 2 shows that one feature of the proposed method is its ability to model multi-modal actions conditioned on the given state. Recently, diffusion models have become a popular approach for this purpose. How does your method compare to diffusion-based methods? Here are some related papers:
  - Diffusion Policies as an Expressive Policy Class for Offline Reinforcement Learning
  - Planning with Diffusion for Flexible Behavior Synthesis
  - IDQL: Implicit Q-Learning as an Actor-Critic Method with Diffusion Policies
2. As shown in Figure 45, the CVAE over the action space is sensitive to the number of training steps. How can we determine the optimal number of training steps before training an offline RL agent? Is this stage time-consuming?

### Questions
Is it possible to use this algorithm in various robot manipulation environments, such as Meta-World and ManiSkill? Additionally, is this stage time-consuming?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper develops an offline RL method for mixed-quality datasets. Their algorithm alternates between (1) performing actor-critic-style policy optimization and (2) disentangling policy quality within the latent space of the actor. (2) is accomplished by CVAE training in which prediction is conditioned on both the state and the current advantage value. The novelty of this paper is the choice to condition on the current advantage value. They show that their method (A2PO) outperforms baselines such as CQL, IDL, MOPO, LAPO, etc on D4RL navigation and locomotion tasks.

### Strengths
This is a sound and well-presented paper. I would place the readability and cleanliness of presentation in the top 5% of papers. A2PO outperforms baselines on most D4RL navigation and locomotion tasks. The ablation analysis in Figure 4 shows that the resulting policy is very responsive to advantage conditioning. I think this is a powerful and elegant way of handling the underestimation issue that has been recurrent in work on off-line RL. I think the experimental results and algorithmic contribution will be useful to the offline RL community.

### Weaknesses
The main weakness of this paper is lack of empirical depth. Many of the baselines also show strong performance on sparse-reward/manipulation tasks within D4RL and it's not clear why these tasks have been omitted here. It would be helpful for the authors to clarify if this approach is specific to navigation and locomotion or to show results on a manipulation tasks such as FrankaKitchen or Adroit. For a concrete reference, please see Table 2 of the CQL paper.

The idea of conditioning on a proxy for policy return (i.e., the advantage) itself is not novel. It would be helpful for the authors to include a reference to reward-conditioned supervised learning [Brandfonbrener et. al., 2023].

### Questions
Why do the authors ablate discrete vs continuous advantage variables within the CVAE? For a distribution that is inherently categorical, I could understand why this ablation would be useful, but because the space of advantages is continuous anyways I don't understand what the reader should takeaway from this experiment.

The margins for improvement between A2PO and the baselines is quite narrow in some cases. It's possible that the ordering of the results could change with more or less tuning. Can the authors clarify what hyper parameters were tuned within A2PO vs the baselines?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents an offline advantage-aware policy optimization method, which uses a generative model to describe the action distribution conditioned on states and advantage values, then samples from this model for high-advantage actions to conduct offline policy optimization. The method is motivated by the argument that mixed-quality dataset may have conflicting constraints if each sample is treated equally, hence some differentiation is needed. The proposed advantage-aware differentiation is verified on datasets of single- and mixed-quality. The empirical results show their method outperforms baselines and especially works well on a dataset with mixed-quality. Ablations are also provided to analyze the method design choices.

### Strengths
1. The empirical results are strong compared to baselines.
2. The paper presents a detailed ablation analysis for the proposed method.

### Weaknesses
1. The contribution is a bit incremental, by mainly moving the advantage values from weight coefficient of the loss function (as in LAPO equation [7]) to condition variables (as in this paper equation [5]). This shift, while present, does not seem to introduce a fundamentally new approach to offline policy optimization. The core idea of leveraging advantage for better policy learning is already explored, and the current method appears to be a minor variation.
2. It looks to me that the policy optimization part is not the same as LAPO, which uses TD3. The differences make the performance comparison between A2PO and LAPO not fair, and make it hard to justify the benefits of conditioning the generative model using advantage values. Specifically, the use of a behavior cloning (BC) term in A2PO's policy optimization loss, which is absent in the LAPO implementation, introduces a confounding factor. This makes it unclear whether the performance gains are due to the advantage-aware conditioning or the additional BC regularization. The lack of a direct comparison with LAPO using the same policy optimization framework makes the advantage of the proposed method questionable.

### Questions
1. A minor typo on Page 8: “The performance comparison of different discrete advantage conditions for test is given in Figure **4**”.
2. I wonder how A2PO compares to LAPO if the policy optimization steps are made the same.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This manuscript proposes an Advantage-Aware Policy Optimization (A2PO) method for offline RL problem. The authors first disentangled behavior policies with CVAE, then combine the  advantage-aware method for policy improvement and optimization.  The superiority of the A2PO method is validated from single-quality and mixed-quality datasets of the D4RL.

### Strengths
1. The problem of mixed behavior policy data is very interesting, and the main idea of this manuscript is easy to follow. 
2. The empirical studies shows that the A2PO method significantly outperforms the competitors in most cases.

### Weaknesses
1. Some details in methodologies are not clear.  How to select the $\xi^*$ in equation (7) and the optimal selected action $\alpha^*_\xi$. As the $\xi$ is transformed by the tanh function, what if there are no (s,a) pairs with $\xi^*=1$? This is an very important step for understanding the main idea of this paper. 
2. Follow the last point, if the $\xi$ is normalized to [0,1], the largest value of $\xi=1$ only corresponds to single data point in the mixed dataset, how do you learn the action distribution from CVAE with this single data point?
3. The information in pseudocode in Algorithm 1 is limited, it is suggested to add some important details in Algorithm.

### Questions
1. Some offline-RL baselines, such as BEAR/AWAC are missed in experiment, and the recent popular SPOT [1] method is not considered in experiments as well.  It is suggested to consider the baselines in offline-RL methods. 
2. The author suggested CVAE to disentangle policies from mixed data. However, the CVAE may not be a good choice for distinguish data from different sources from [1] and [2]. So I wonder why A2PO could achieve significant results in empirical experiments. 
3. In the experiment, the authors manually combines the single-quality datasets to setup the mixed datasets. The details of mixed data combination should be provided, and some ablation studies about the amount of each single-quality data are also suggested. 

[1] Supported Policy Optimization for Offline Reinforcement Learning. https://arxiv.org/abs/2202.06239

[2] A Behavior Regularized Implicit Policy for Offline Reinforcement Learning. https://arxiv.org/pdf/2202.09673.pdf

[3] EMaQ: Expected-Max Q-Learning Operator for Simple Yet Effective Offline and Online RL. https://arxiv.org/pdf/2007.11091.pdf

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an offline RL algorithm which uses CVAE to map the actions into the latent space and then perform latent space TD3+BC for policy optimization. The key design as claimed by the authors is to introduce the projected advantage values as an additional conditional input in CVAE, which can help better distinguish data quality. The proposed method lacks concrete theoretical backing on why it will work, and seems to require careful hyperparameter tuning to maintain stability and achieve good performance. See the following strengths and weaknesses for detailed comments.

### Strengths
- The paper is easy to read.
- Relatively comprehensive evaluations on MuJoCo and antmaze tasks. Reasonable performance. Though I find some antmaze task scores seem to be problematic.

### Weaknesses
 - The design of adding advantage values into a jointly trained CVAE can lead to extra training instability. As the value functions are gradually learned, the advantage value can keep changing during the CVAE training. This means that the conditioning information in CVAE is not stationary, causing the learning of CVAE to also fluctuate. It can become worse when using the latent representation from a non-stationary CVAE, which can further cause instability in the value and policy learning. This is evident as the authors have admitted that the training step $K$ of CVAE needs to be carefully tuned, and as shown in Fig. 5, the proposed method can fail miserably if using an improper $K$ value.
- The references on offline RL algorithms are mostly restricted to those before 2022. As this field is rapidly developing, there are many strong offline RL algorithms have been proposed in 2023 but lack acknowledgment or comparison. The reported scores are only comparable to some of the newer but more lightweight in-sample learning algorithms like XQL[1] and SQL[2], and less performant than some recent methods that use diffusion policies [3, 4]. Given the proposed method is somewhat heavy (needs to learn an additional, potentially unstable CVAE), I don't think the proposed method offers impressive performance.
- The value and policy learning procedure is essentially TD3+BC[5], but conducted in the latent space. However, TD3+BC is never mentioned in Section 4.2. Even in the codes provided by the author, the corresponding method names are "TD3BC_critic_loss" and "TD3BC_actor_loss". Same as TD3+BC, the actual implementation needs to use a $\lambda$ hyperparameter to trade off max Q and minimize the BC penalty. However, this is not mentioned in Eq.(8). This extra hyperparameter is intentionally omitted and corresponding hyperparameter tuning is not discussed. If this hyperparameter is carefully tuned for each task, even the original TD3+BC is likely to have strong performance.
- I feel the proposed method is essentially doing some kind of representation learning over TD3+BC, but unlike other representation learning methods, it could be more unstable. It is suggested that the proposed method should also be compared with existing offline RL baselines with representation learning.
- In the experiments, adding additional experiments on datasets mixed with random data is not very meaningful for practical settings. As nobody will use bad random data to train their offline RL policy in practice. Moreover, BPPO is a flawed offline RL algorithm and is not worth comparison. In its code implementation, it hides online evaluation during offline training, which is a kind of cheating in the offline RL setting. It is a shame that such a paper even gets accepted in ICLR 2023. On the other hand, some recent strong and rigorous offline RL algorithms should be compared.

### Questions
- The scores for antmaze-m-d and antmze-l-d look strange, CQL and IQL are reported to have reasonable scores in the IQL paper as well as in previous references [1-2,4], however, their scores are all zero in this paper. Moreover, the proposed A2PO's performance looks very bad, inferior to scores of baselines as reported in other papers. Why is that?
- Please report the max-Q and BC trade-off hyperparameter values in the TD3+BC style policy improvement step (Eq.(8)). Has it been tuned for different tasks?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
