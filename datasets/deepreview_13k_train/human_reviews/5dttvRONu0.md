# Federated Learning Nodes Can Reconstruct Peers' Image Data

- Decision: Reject
- Scores: 3, 5, 3

## Abstract
Federated learning (FL) is a privacy-preserving machine learning framework that enables multiple nodes to train models on their local data and periodically average weight updates to benefit from other nodes' training. Each node's goal is to collaborate with other nodes to improve the model's performance while keeping its training data private. However, this framework does not guarantee data privacy. Prior work has shown that the gradient-sharing steps in FL can be vulnerable to data reconstruction attacks from an honest-but-curious central server. In this work, we show that an honest-but-curious node/client can also launch attacks to reconstruct peers' image data in a centralized system, presenting a severe privacy risk. We demonstrate that a single client can silently reconstruct other clients' private images using diluted information available within consecutive updates. We leverage state-of-the-art diffusion models to enhance the perceptual quality and recognizability of the reconstructed images, further demonstrating the risk of information leakage at a semantic level. This highlights the need for more robust privacy-preserving mechanisms that protect against silent client-side attacks during federated training.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an attack approach within the federated learning (FL) framework to reconstruct image data from participating peers in a centralized system. The study demonstrates that consecutive updates in the FL setting can inadvertently reveal information about other clients. Experiments are conducted to validate the effectiveness of this attack method.

### Strengths
The strength of this paper lies in its successful implementation of an attack capable of reconstructing images from other participating users. The experiments effectively demonstrate the effectiveness of the proposed method.

### Weaknesses
I have several concerns regarding the experimental setup and the novelty of this paper, which I outline below:

The method relies on several assumptions, including that each client has ample computational resources, employs a consistent learning rate, and trains with an equal number of images locally. Additionally, the approach presumes that the attacker is either aware of or can accurately estimate the number of clients participating in each training round. Further assumptions, such as the use of full-batch gradient descent for local training and other idealized conditions, may not be realistic for federated learning (FL) environments. The assumption of a consistent learning rate across clients is particularly concerning, as practical FL deployments often involve adaptive learning rate strategies tailored to individual client data distributions and computational capabilities. This assumption significantly limits the applicability of the attack in more realistic scenarios where clients might employ different optimizers or learning rate schedules.

These restrictive assumptions may limit the method's practical applicability in typical FL settings. Federated learning is generally designed to support users with limited resources, accommodate non-iid (non-independent and identically distributed) data, and handle asynchronous updates among clients. The paper does not address these critical FL challenges, potentially reducing the relevance of the proposed approach in real-world scenarios. The lack of consideration for non-IID data, which is a common characteristic of federated datasets, is a major oversight. The performance of the attack under such conditions is unclear, and the paper does not provide any analysis or discussion on how the attack would be affected by varying degrees of data heterogeneity.

The optimization framework introduced here does not appear to be novel, and the paper lacks citations to previous work on similar frameworks. There is also no comparison provided to demonstrate why or how the proposed optimization function is more effective or advantageous over existing methods. The paper does not adequately justify the choice of the specific optimization method used for the attack, nor does it explore alternative optimization strategies that might be more effective or robust. A more thorough analysis of the optimization landscape and a comparison with other relevant techniques would be beneficial.

In the experiments, the maximum number of clients is set at 8, which limits the insights into how the framework performs at larger scales. Additionally, there are insufficient ablation studies to illustrate the robustness of the proposed framework under varying conditions. The absence of ablation studies exploring the impact of different hyperparameters, such as the number of local iterations or the inversion learning rate, makes it difficult to assess the robustness and generalizability of the proposed attack. Furthermore, the limited scale of the experiments raises concerns about the scalability of the attack to more realistic federated learning scenarios with a larger number of participants.

### Questions
How does the proposed approach perform with a larger number of clients?
How robust is the proposed approach if any of its underlying assumptions are violated?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper investigates the privacy issues in federated learning (FL), a framework allowing nodes to train models locally while sharing updates. Despite its privacy goals, FL is vulnerable to data reconstruction attacks. The paper reveals that not only central servers but also semi-honest clients can reconstruct peers' image data, posing significant risks. Using advanced diffusion models, the authors show how a single client can enhance image quality, underscoring the need for stronger privacy measures to prevent client-side attacks in FL.

### Strengths
1. **Stealth and Undetectability**: The attack method does not disrupt the training process or introduce corrupted data, making it challenging for detection by servers or other clients, which underscores its potential impact.

2. **Relevance to Cross-Silo FL**: The findings are particularly concerning for cross-silo FL, where data scarcity is addressed through collaboration, emphasizing the need for enhanced privacy measures in such settings.

3. **Extensive Experiments**: The paper conducts thorough experiments to validate the effectiveness of the attack, providing strong empirical evidence of the vulnerability in FL systems.

### Weaknesses
1. This paper attacks from the perspective of any node/client and reconstruct all training data of all other participants. However, this is no different from a conventional inversion attack launched from the server. When the secure aggregation protocol is applied, the server can obtain the model parameters at time $t$ and the corresponding aggregated gradients; while any client can receive the model parameters at time $t$ and time $t+1$. Obviously, the information obtained in these two cases is exactly the same, and the updated gradient is the difference between these two rounds. It is good that the authors start from the node/client perspective, but the current analysis is the same as the typical gradient inversion attacks, and there is no special or new inspiration.

2. The core contribution of the paper is to propose a post-processing method for reconstructing images (based on the diffusion models). However, this is based on a premise that the original restored image already contains enough information. If the results after the attack are like the results of Figure 5(b) and Figure 15 of ROG or the last three rows of Figure 4 of GradInversion (See through Gradients, Yin et al.), the reconstructed images are similar to noise, then your proposed method obviously does not work. How do you solve this situation? This is not mentioned in the paper.

### Questions
1. Figures 2, 3, 5, and 8 demonstrate the effect of data reconstruction. What hyperparameters such as the training model structure, batch size, and epoch of FedAvg local training are used corresponding to these results?

2. You selected LPIPS as the main evaluation metric. Do the results or trends of MSE, PSNR, SSIM and LPIPS are consistent in these experiments? Because sometimes the LPIPS values ​​of two sets of images may be close, but the visual effects are very different.

3. In the left figure of Figure 6, when there are 8 clients and the batch size is 64, the attacker has to restore a total of (amazing) 512 images. What is the specific visualizatioin results of these images? Does the LPIPS value reflect the actual reconstruction effect?

4. In Equation (3), why do you choose L2 norm instead of cosine similarity? In your method, which one do you think has a greater impact on the final restoration result, raw reconstruction or post-processing?

5. Figure 2 shows the results of different epochs. How do you choose the best epoch? For all the images to be processed, do they use the same optimal number of epochs?

6. After adding two diffusion models (MDT and DDPMs) to optimize the reconstruction results, how much will the efficiency of the attack and the computational cost increase compared to before?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a high-quality privacy data reconstruction method in the federated learning scenario, which achieves excellent results especially when the number of participating training nodes and the amount of data are limited. Unlike traditional methods, this paper considers attacks from peer nodes, making the scenario more versatile.

### Strengths
This paper integrates gradient inversion attacks with generative models to achieve higher quality privacy attacks. Additionally, it takes into account attacks from peer nodes, making the scenario more versatile compared to traditional ones.

### Weaknesses
The authors claim that the advantage of this paper lies in the achievement of node-level privacy attacks in the federated learning scenario. However, there are several significant limitations:
1. Unreasonable assumptions. In the aggregation of global gradients, updates from different nodes are weighted based on the amount of training data used by each party. However, the authors simplistically assume that the parties aggregate with equal weights. Additionally, the authors mention that an attacker can directly initialize N (line 161), but we do not think that a peer node can have this information. In summary, these assumptions make the paper fundamentally similar to traditional privacy attacks conducted by a central server, with only an additional simple subtraction operation. This also makes the paper’s main contribution less solid.

2. Lack of novelty and originality. The work presented in this paper is a simple combination of gradient inversion attacks with super-resolution and denoising techniques, without proposing a new method or solving an unsolved problem (although the authors claim to have achieved peer node attacks, we have already shown in point 1 that this assumption is not fundamentally different from existing center-based studies). Therefore, the academic value of this paper is not sufficient for publication in a top-tier conference like ICLR.

3. The introduction of the experimental setup is very rough. In the optimization objective Eq. (3) of this paper, there is no variable related to labels, and the setup does not explain how the attacker obtains the labels. Although the paper mentions the method of Yin et al., their method cannot handle scenarios with duplicate labels. Moreover, I do not think that the paper can be replicated based on the setup provided, as almost all configurations related to optimization are missing.

### Questions
My concerns are detailed in the WEAKNESS part, specifically in relation to these limitations. If the authors provide convincing responses to these limitations, I would be happy to raise my score.

### Soundness
2

### Presentation
2

### Contribution
1
