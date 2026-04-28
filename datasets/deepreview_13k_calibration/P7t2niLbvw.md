# Swift Hydra:  Self-Reinforcing Generative Framework for Anomaly Detection with Multiple Mamba Models

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Despite a plethora of anomaly detection models developed over the years, their ability to generalize to unseen anomalies remains an issue, particularly in critical systems. This paper aims to address this challenge by introducing Swift Hydra, a new framework for training an anomaly detection method based on generative AI and reinforcement learning (RL). Through featuring an RL policy that operates on the latent variables of a generative model, the framework synthesizes novel and diverse anomaly samples that are capable of bypassing a detection model. These generated synthetic samples are, in turn, used to augment the detection model, further improving its ability to handle challenging anomalies. Swift Hydra also incorporates Mamba models structured as a Mixture of Experts (MoE) to enable scalable adaptation of the number of Mamba experts based on data complexity, effectively capturing diverse feature distributions without increasing the model’s inference time. Empirical evaluations on ADBench benchmark demonstrate that Swift Hydra  outperforms other state-of-the-art anomaly detection models while maintaining a relatively short inference time. From these results, our research highlights a new and auspicious paradigm of integrating RL and generative AI for advancing anomaly detection.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel framework, Swift Hydra, for training an anomaly detection method that leverages generative AI and reinforcement learning. It introduces Mamba models structured as a Mixture of Experts (MoE), allowing for scalable adaptation of the number of Mamba experts based on data complexity. Experiments conducted on the ADBench benchmark demonstrate that Swift Hydra outperforms other state-of-the-art anomaly detection models while maintaining a relatively short inference time.

### Strengths
1.The writing in this paper is clear and well-structured.

2.The incorporation of reinforcement learning, conditional VAE, and Mixture of Experts (MoE) is novel and well-justified.

3.The paper conducts thorough experiments on ADBench and demonstrates strong performance.

### Weaknesses
1.Typically, experiments relying on only one dataset are insufficient. It would be beneficial to include additional analysis and comparisons using other popular datasets.

2.It appears that Swift Hydra is not specifically designed for tabular anomaly detection. Have you explored the generalizability of this method to other domains, such as image data or time-series data?

3.The paper introduces several complex components, such as reinforcement learning, which may complicate implementation. Additionally, could you provide an analysis of the computational cost associated with training, including metrics such as the number of parameters and training time per batch?

4.How does the performance of Swift Hydra fare in multi-class or cross-dataset scenarios?

### Questions
See weakness above. I will consider raising my score if my concerns are addressed well.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel tabular anomaly detection method by designing a RL-based anomaly data augmentation technique and a Mixture of Experts (MOE) based anomaly detection module. The authors verified the effectiveness of their proposed method with 3 baselines on ADBench and also provided visualized proofs of the effectiveness of their reward function and anomalous data augmentation technique.

### Strengths
1. Overall well written. The paper is easy to follow and organized in a clear orchestration. 
2. Novel idea. This paper proposes a novel idea that using RL to make anomalous data augmentation. Besides, the authors also prove the effectiveness of their proposed reward function by showing the consistency between AUC-ROC and the reward.
3. It is proved that the RL-based anomaly data generation method can generate anomalies of high diversities, as show in Fig 2.

### Weaknesses
1. Weak soundness of experiment. The experiments are not persuasive enough. The baselines do not cover enough SOTA tabular anomaly detection methods. The authors only compares the proposed methods with 3 baselines. Besides, there is no ablation study to verify the effectiveness of RL-based anomaly data generation technique and the MOE anomaly detection module separately.
2. Unrealistic assumption in mathematical proof. In the mathematical proof of theorem 2 and theorem 3, it is actually assumed that single anomaly detector can not distinguish anomalies and normality in overlap region. However, this assumption is only available for linear classification methods (e.g. support vector machine). The deep neural networks are non-linear classification methods and can deal with interlaced anomalies and normality in  overlap region well. In this situation, theorem 2 and 3 can not be deduced.
3. The illustration of the process of "gating network" and "Tackling winner-take-all" is somewhat ambiguous. What confused me is that given both of these two mechanism actually are used to assign input to different expert, how could we use them together?

### Questions
1. In theorem 1, do you mean $\hat{x}_i=\mathcal{M}_\phi(\hat{z}_i,y_i=1)$?
2. Could you please add more SOTA tabular anomaly detection methods?
3. Could you please add ablation experiments?
4. In Table 1, why Swift Hydra (MOME) has less inference time than Swift Hydra (Single)?
5. Could you please further explain how to use "gating network" and "Tackling winner-take-all" together?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This method focus on generalization to unseen anomalies. To do that, this method generates new anomaly samples using reinforcement learning and conditional VAE. The conditional VAE generate samples conditioned on the class anomaly. The reinforcement learning enforces the generated samples to be diverse and difficult to detect by the detection model. For the detection model, in order to keep the complexity low while can capture diverse feature distribution, Mixture of Experts consisting of multiple Mamba experts are utilized.

### Strengths
Adding new anomalous synthetic data during training to increase generalization using reinforcement learning seems to be novel.

### Weaknesses
See questions.

1. Which part of the experiments that prove the generalization to unseen anomalies?

2. It is unclear whether this work use both real and fake data or only real data. I can't find the information in Line 94-105. My guess from other part of the paper is using both real and fake, but I am not 100\% sure. 

3. Why is this method called reinforcement learning method if the action is (afaik) backpropagatable directly from the reward/loss? 

4. How is the balanced dataset updated? I can't find any information in Algorithm 1 in the appendix.

5. Why not also generating normal data?

### Questions
1. Which part of the experiments that prove the generalization to unseen anomalies?

2. It is unclear whether this work use both real and fake data or only real data. I can't find the information in Line 94-105. My guess from other part of the paper is using both real and fake, but I am not 100\% sure. 

3. Why is this method called reinforcement learning method if the action is (afaik) backpropagatable directly from the reward/loss? 

4. How is the balanced dataset updated? I can't find any information in Algorithm 1 in the appendix.

5. Why not also generating normal data?

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes Swift Hydra, a novel anomaly detection framework based on the conditional variational autoencoder (CVAE) and reinforcement learning.
The proposed method generates high-quality anomalies using CVAE and reinforcement learning, and performs anomaly detection using a mixture of expert models based on Mamba (MoME). 
Experiments on various datasets demonstrated improved anomaly detection performance and reduced inference time compared to existing methods.

### Strengths
- This paper introduces several strategies to achieve high-accuracy anomaly detection. For example, the reward function in reinforcement learning incorporates the entropy of the union of the training data and the generated data, which encourages the generation of diverse anomalies. Additionally, in the MMoE model, experts are selected probabilistically to avoid the winner-take-all problem.
- The visualization of the generated anomalies is interesting. It clearly shows a clean separation between normal data and anomalies, and we can also observe the generation of a wide variety of anomalies.

### Weaknesses
 - Although the proposed method works well, there are a few parts that are unclear to me. I will write more details in the Questions section, so please refer to it.


### Questions
1. Why does the proposed method use CVAE? Since VAE generally has lower data generation quality compared to other generative models, I don't think it's very suitable for data augmentation purposes in this case. For example, would the proposed method work well with a diffusion model, which can be considered a special case of VAE?
2. The proposed method performs anomaly detection in the data space, but wouldn’t it be more beneficial to take advantage of CVAE’s strengths by performing anomaly detection in the lower-dimensional latent space? What is the reason for performing anomaly detection in the data space?
3. I understand that MMoE performs binary classification between normal and anomaly data. In binary classification, a decision boundary is set between the normal and anomaly data included in the training set, which makes it difficult to handle unseen anomalies that are far from the known anomalies in the training data. Can the proposed method address this issue?
4. If the proposed method can handle unseen anomalies, I believe it is because CVAE can generate such unseen anomalies. Why is the proposed method able to generate unseen anomalies? Even though the entropy is incorporated into the reward of the reinforcement learning, I think generative models can only generate data similar to the training data.
5. Is it possible to visualize the generated samples and decision boundaries of the proposed method using two-dimensional toy data? For example, if there is normal data shaped like a sine curve, and the generated anomalies are arranged surrounding that curve, I believe the method would be able to handle both seen and unseen anomalies.

### Soundness
3

### Presentation
2

### Contribution
2
