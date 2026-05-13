# Anomaly Detection through Conditional Diffusion Probability Modeling on Graphs

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
Existing Graph Neural Network-based anomaly detection methods suffer from over-smoothing issues during feature aggregation. Moreover, most existing methods are discriminative models that learn the boundaries between anomalous and normal data points, allowing malicious nodes in a dynamic adversarial environment to bypass detection boundaries. To address these issues, existing methods primarily focus on enhancing the discriminative boundary for each individual node, rather than considering the interdependencies of node anomalies from a holistic graph perspective. We propose an advanced Conditional Graph Anomaly Diffusion Model (CGADM) to model and capture the joint distribution of anomalies on the whole graph, thereby enabling generative graph anomaly detection. To avoid starting the diffusion process from a random state, CGADM introduces a prior-guided denoising diffusion probability model. To circumvent the need for iterative denoising samplings for each node on large-scale graphs, we adopt a prior confidence-aware mechanism to dynamically adjust the reverse sampling steps for each node, significantly reducing the computational burden on large-scale graphs. We conducted experiments on CGADM using standard benchmarks, and the results demonstrated excellent performance in graph anomaly detection tasks. Additional ablation studies confirmed our framework's computational advantages.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a Conditional Graph Anomaly Diffusion Model (CGADM) for generative graph anomaly detection, aiming at considering the interdependencies of node anomalies from a holistic graph perspective.

### Strengths
1. The performance of CGADM outperforms the SOTA methods on most of the datasets on most of the metrics.

2. Malicious nodes in a dynamic adversarial environment are very hard to detect since they are normal in the moment but can be anomalous in the next second. It is a worth studying problem, and pattern recognition may be a plausible approach.

3. The method is efficient due to the reduction of the reverse steps, time and space scalability is always important in graph algorithms.

### Weaknesses
1. The performance gap on Quest and Reddit are somehow marginal. Diffusion model need large amount of data to capture the distribution, and according to Table 3, Quest and Reddit have the least anomaly ratio. This raises the question that: In real world, anomaly ratio may be less than 1%, will CGADM still work in imbalanced scenarios?

2. The distribution definition is not clear. What indeed is the distribution that the authors expect DM to capture? TSNE visualizations or some insights about this are appreciated. Figure 1 doesn't provide enough information in such an important place.

3. Some of the related work [1~4] (especially new works in the field) are missing.

### Questions
Will CGADM still work in imbalanced scenarios?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed an advanced conditional graph diffusion model that can capture the joint distribution of anomalies in the whole graph. It introduces the prior-guided denoising diffusion probability model to replace the random state. The experiments demonstrate the CGADM achieves the best performance when compared with state-of-the-art methods.

### Strengths
1. A  prior-guided denoising diffusion probabilistic model is designed to capture the distribution of anomalies in the whole graph thereby enabling the generative graph anomaly detection. 
2. The experiments demonstrate the CGADM achieves the best performance when compared with state-of-the-art methods.
3. A  prior confidence-aware mechanism allocating disparate sampling time steps is proposed to mitigate the computational burden in processing the large-scale graph.

### Weaknesses
1. The motivation for leveraging the diffusion model is not very clear since the challenges proposed in the introduction are not unique to the GAD task. How does the prior guided diffusion process mitigate the over-smoothing problem at the topology level?

2. This paper does not include a baseline involving diffusion models for GAD [1]. The methods from [1] should be incorporated into both the related work and experimental comparison sections to emphasize the differences [2].

3. The paper claims the efficiency of CGADM.  While I agree that the confidence-aware mechanism can enhance inference efficiency, to support the overall efficiency claims of CGADM, the authors should include a comparison of running times with other baseline methods as well as an analysis of time complexity. The main challenge lies in modeling large-scale graphs, which require substantial memory. In contrast, running time is not a significant bottleneck.

### Questions
1. What is the advantage of CGADM when compared with other generative models like GAN and VAE in dealing with the challenges existing in GAD tasks?

2. For the parameterized network $g_\phi(\mathcal{E}, \mathbf{X})$ which serves as the prior, it is pre-trained on the training set to estimate the mean. Could you elaborate on the pre-training process for this network?  Are there any traditional methods involved, since the priors are implemented using Random Forest (RF) and XGBoost (XGBT) in the ablation study,

3. The diffusion model with the random state should be added to the ablation studies to demonstrate the effectiveness of CGADM where the random state is replaced with the prior.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The existing Graph anomaly detection models (GAD) tend to obtain a discriminative boundary for each individual node. This paper introduces a novel method, CGADM, which leverages a conditional diffusion model to account for the interdependencies among node anomalies and constructs the decision boundary for anomaly detection from the perspective of the whole graph.  To address both the effectiveness and efficiency challenges of diffusion models, the authors employ a prior estimator to integrate node anomaly priors into the forward and backward processes. This ensures that the forward process converges to the anomaly prior rather than a standard Gaussian distribution, and also allows for early termination of the backward process. Experimental results demonstrate the efficacy of the proposed approach.


I think direct use of the diffusion model as the primary framework for anomaly detection to be somewhat novel, as most existing methods still use it as an auxiliary model, such as for data augmentation. The paper’s motivation convincingly supports the rationale for employing the diffusion model, with targeted modifications to enhance both effectiveness and efficiency. However, some technical details are lacking, which makes it difficult to fully comprehend the method, as noted in the weaknesses section. Therefore, my score is a positive borderline.

### Strengths
1. Novely of this paper, rather than utilize diffusion model as auxiliary model, CGADM directly generate the prediction and the otivation of this paper supports this idea.
2.The proposed technique is reliable. CGADM  inject the learned anomaly prior into the diffusion model, which improves the efficiency and performance compared with the direct use of vanilla diffusion model, and better fits the anomaly detection task.
3.The modification to the diffusion model seems mathematically reliable, as the authors provide a detailed proof procedure in appendix.
4. The experimental results are significantly improved on some datasets.

### Weaknesses
1. There is no need to cliam that GNNs are suffer from over-smoothing problem in the first paragraph of the abstract, as this is weakly related to the problem the authors are addressing in the GAD domain. I suggest that the author reconsider the necessity of this paragraph to avoid misunderstanding.
2. Some technical details are lacking, see questions.
3. Algorithm I does not embody the improvement about sampling efficiency mentioned by the authors in the paper, and will cause misleading. I think the author should describe the sampling procedure described in Section 4.4 in pseudocode.

### Questions
1. How is the anomaly prior model trained? The explanation on line 256 confused me, how can a  meachine learning model trained to be used to estimate the mean of a distribution? I'm sorry I can't understand how to do that.

2. How efficient is CGADM compared to other GAD models that are not based on diffusion models? The authors only mention the number of samples in section 5.4, but do not report numerical metrics such as execution time, memory footprint, etc. This is unconvincing. I suggest that authors can introduce a table or figure comparing execution times and memory usage across all evaluated models

3. Why does line 311 mention the need to simplify $L_{recon}$ and $L_{con}$ to get to the final optimization objective? Although I think Eq 12 is reasonable as an optimization objective, why can Eq 3 be theoretically simplified to Eq 12?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a framework for graph anomaly detection using a conditional graph diffusion model, called CGADM, aiming to solve the issue of over-smoothing and poor generalization boundaries between normal and anomalous nodes. Experimental results show that CGADM outperforms baselines on datasets included in this paper.

### Strengths
S1. This paper proposes a framework for graph anomaly detection using a conditional graph diffusion model. 

S2. Experimental results show that CGADM outperforms baselines on datasets included in this paper.

### Weaknesses
W1. The contribution is limited. The main equations in this paper are almost the same as in previous works, so this paper is more of an implementation, with almost no components changed. To be specific, in Section 4 of this paper, equation (2), (3), (4), (5), (6), (7), (8), and (12) are the same as equation (1), (2), (6), (7), (8), (9), and loss function in Algorithm 1 in CARD[1], equation (9) is the same as equation (11) in DDPM[2], and equation (14) is the same as equation (12) in DDIM [3]. The authors need further explanations to show their contributions other than an implementation from the image model to the graph model.

W2. The experiments are not comprehensive enough. There are several novel supervised GAD works in recent years, such as XGBGraph[4] and CONSISGAD[5]. The authors need to conduct a comparison between their framework and these novel SOTA models.

W3. Some parts of the design need further explanation. For example, in Section 4.2, the authors claim "For the parameterization, we may select equation (9)". Such a choice is a lack of explanation. Besides, the heuristic strategy in equation (16) is also not convincing. To address these concerns, they need to provide further explanations of their design.

### Questions
Q1. Previous works in this field, such as GHRN and CONSISGAD, usually use AUC and F1 scores as the evaluation metric. Why do the authors use AUPRC instead of F1 score? Can the authors provide the results of the F1 score of these models on the datasets? 

Q2. What is the explanation of equation (10)? Typical aggregation functions utilize addition instead of subtraction, so the authors need to further illustrate the idea. Is it from a previous work? 

Reference: 
1. Xizewen Han, Huangjie Zheng, Mingyuan Zhou. CARD: Classification and Regression Diffusion Models. NeurIPS 2022. 
2. Jonathan Ho, Ajay Jain, Pieter Abbeel. Denoising Diffusion Probabilistic Models. NeurIPS 2020. 
3. Jiaming Song, Chenlin Meng, Stefano Ermon. Denoising Diffusion Implicit Models. ICLR 2021. 
4. Jianheng Tang, Fengrui Hua, Ziqi Gao, Peilin Zhao, Jia Li. GADBench: Revisiting and Benchmarking Supervised Graph Anomaly Detection. NeurIPS 2023. 
5. Nan Chen, Zemin Liu, Bryan Hooi, Bingsheng He, Rizal Fathony, Jun Hu, Jia Chen. Consistency Training with Learnable Data Augmentation for Graph Anomaly Detection with Limited Supervision. ICLR 2024.

### Soundness
2

### Presentation
2

### Contribution
2
