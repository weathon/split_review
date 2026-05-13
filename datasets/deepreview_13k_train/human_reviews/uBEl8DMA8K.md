# Addressing Data Heterogeneity In Federated Learning With Adaptive Normalization-Free Feature Recalibration

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
Federated learning is a decentralized collaborative training paradigm that preserves stakeholders’ data ownership while improving performance and generalization. However, statistical heterogeneity among client datasets poses a fundamental challenge by degrading system performance. To address this issue, we propose Adaptive Normalization-free Feature Recalibration (ANFR), an architecture-level approach that combines weight standardization and channel attention. Weight standardization normalizes the weights of layers instead of activations. This is less susceptible to mismatched client statistics and inconsistent averaging, thereby more robust under heterogeneity. Channel attention produces learnable scaling factors for feature maps, suppressing those that are inconsistent between clients due to heterogeneity. We demonstrate that combining these techniques boosts model performance beyond their individual contributions, by enhancing class selectivity and optimizing channel attention weight distribution. ANFR operates independently of the aggregation method and is effective in both global and personalized federated learning settings, with minimal computational overhead. Furthermore, when training with differential privacy, ANFR achieves an appealing balance between privacy and utility, enabling strong privacy guarantees without sacrificing performance. By integrating weight standardization and channel attention in the backbone model, ANFR offers a novel and versatile approach to the challenge of statistical heterogeneity. We demonstrate through extensive experiments that ANFR consistently outperforms established baselines across various aggregation methods, datasets, and heterogeneity conditions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents an approach for improving collaboration across different clients in FL when the clients are heterogeneous in terms of their data distributions. The contribution of this paper is the method ANFR that combines weight standardization and channel attention to reduce the affect of the data heterogeneity in collaboration. The weight standardization makes the local models' training independent of the batch statistics and channel attention can focus or suppress important and irrelevant features respectively. The usage of CA and its beenfit seems intuitive.

### Strengths
1. The authors mention that this approach can be used for existing global and personalized FL algorithms with different aggregation mechanisms.
2. Experiments and ablations - The authors conduct extensive evaluation along with ablations demonstrating the effect of different components.

### Weaknesses
1. Adding an extra attention module on channels might not be practical for FL when the devices do not have sufficient compute.


### Questions
1. The impact of CA is clear with ablations, can you please provide more insights on how SWS helps the learning? Is it required for CA to work?

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
The paper addresses the challenge of data heterogeneity in federated learning by introducing feature recalibration through two main strategies: weight standardization (which normalizes the weights of layers rather than the activations) and channel attention (which suppresses feature maps inconsistent across clients due to heterogeneity). This approach is agnostic to aggregation methods and performs effectively in standard and personalized federated learning settings.

### Strengths
- This paper focuses on an important challenge: statistical heterogeneity in federated learning. Introduces weight standardization and channel attention. 
- The experimental evaluation in the paper seems exhaustive, covering a wide range of baseline methods and datasets.

### Weaknesses
 **Unrealistically high results:** Table 1 illustrates very high and seemingly unrealistic results, which appear to outperform even centralized training outcomes (not directly provided in the paper but evident from the literature). 

**Lack of sufficient evidence:** 
- The primary concern is with the CIFAR-10 experiments. Achieving 97.42% accuracy is challenging even in the centralized settings, let alone in federated settings. This makes the results highly questionable. 
- The reported increase in Fed-ISIC experiment is unusually significant and better than what was presented in the original paper [1]. In the original work, the accuracy achieved using FedAvg, FedProx, and SCAFFOLD does not surpass 60%, and centralized training does not exceed 70%, where [1] uses the EfficientNet architecture with a similar fine-tuning approach. 
- The performance of the SCAFFOLD method on the ResNet-50 architecture appears unusually high. In nature, SCAFFOLD is designed to work well in convex settings but is generally expected to struggle in highly non-convex and non-smooth scenarios.

### Questions
See weaknesses and provide the following details: 

- Include a performance plot for the experiments conducted, showing results for both **Centralized** and **Individual** accuracies. 
- Conduct and include an experiment that demonstrates how your method performs when you train from scratch (i.e., without pre-training weights), starting with random weights, and provide those results for comparison.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Statistical heterogeneity among multiple client datasets in federated learning can diminish the system's effectiveness. To address this, this paper introduces Adaptive Normalization-free Feature Recalibration (ANFR), an architecture-level solution combining weight standardization and channel attention. Weight standardization normalizes layer weights, making the system more resilient to client data inconsistencies and irregular averaging. Channel attention produces learnable scaling factors for feature maps, helping suppress those that vary significantly between clients. 

By applying weight standardization and channel attention, ANFR can enhance model performance by boosting class selectivity and optimizing channel attention weight distribution, delivering benefits that surpass their individual effects. To improve the privacy guarantee, ANFR with differential privacy achieves the balance between privacy and utility.

### Strengths
This paper gives some interesting experimental results, such as performance comparison, pFL aggregation method comparison, and differential privacy training.

### Weaknesses
- The proposed approach appears to integrate weight standardization and channel attention in a relatively straightforward manner, with few technical complexities or novel mechanisms to address the combination. Moreover, the experimental results are not very exciting (e.g., the improved performance over FedChest is less than 1%.)
- In Section 4.3, ANFR combines differential privacy to enhance the protection of the model. However, the work does not include a formal analysis or theoretical proof to rigorously substantiate the differential privacy guarantees, causing a lack of clarity on the degree of privacy achieved from the theoretical perspective.
- The experimental results look incremental on CIFAR-10 and FedChest for performance comparison. For example, the improved performance is mostly less than 1%.
- Writing: Regarding the writing style, Section 3 delves directly into technical details without offering an introductory overview. This sudden shift into specifics could benefit from a preliminary summary that provides context and a roadmap for the technical content, enhancing the logical flow of the section.

### Questions
1. Why is the improved performance in pFL aggregation not impressive? For example, compared with NF-ResNet, the improvements are from 84.2 to 84.9 and 83.7 to 83.8.

2. Although the authors introduced "... train with strict sample-level privacy guarantees, employing a privacy budget of $\epsilon=1$, followed by training without privacy constraints to illustrate the privacy/utility trade-off of each model...", it remains unclear what the configurations are for $\delta,\sigma$ and other common parameters used in differentially private learning.

3. The paper lacks a formal analysis of differential privacy and an insightful explanation of "enabling strong privacy guarantees without sacrificing performance." Given my understanding, the authors should theoretically prove the improved privacy-utility trade-off.

4. The authors stated the contribution "offers a robust and flexible solution to the challenge of statistical heterogeneity". However, I can not find any theoretical analysis of robustness and privacy relevant to statistical heterogeneity.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents ANFR, a method designed to address the challenge of statistical heterogeneity in federated learning environments, with a particular focus on the limitations of batch normalization across heterogeneous client datasets. The authors propose a combination of weight standardization and channel attention mechanisms to normalize layer weights and adaptively scale feature maps, aiming to emphasize shared, informative features across clients. The approach is evaluated across various domains, including medical and common computer vision tasks.

### Strengths
1. Simple and straightforward approach that can be easily integrated into existing FL frameworks

2. Comprehensive empirical evaluation across multiple datasets

3. Clear experimental setup and ablation studies

### Weaknesses
1. The proposed method combines two existing techniques—weight standardization and channel attention—without substantial modifications specific to the federated learning context. The theoretical justification primarily draws from existing literature, lacking novel analysis within the federated learning framework.

2. In Section 3, the connection between feature consistency in different layers and the proposed weight assignment mechanism (A_C_R, A_C_NR) is unclear, undermining the theoretical foundation.

3. The analysis of Figure 2, which aims to demonstrate the method's advantages regarding class selectivity, requires revision. The current presentation shows minimal difference between ANFR and NF-ResNet, contradicting the authors' explanation of significant improvements.

4. In Table 1, the performance result of FedChest + FedProx + BN-ResNet is identical to that of FedChest + FedProx + ANFR. The authors state that "we employ a large batch size of 128 to maximize the probability that all classes are represented in each batch, following best practices. This choice incidentally biases the setting in favor of BN models since larger batches reduce inconsistent averaging of mini-batch statistics and BN parameters" (lines 427–429). To gain a more detailed understanding, could the authors provide additional results using smaller or larger batch sizes? Additionally, is there further analysis to explain why this result is observed only under the FedProx setting?

### Questions
1. Improved organizational structure in Section 3, with clearer problem definition and methodology subsections, would enhance readability. Including detailed pseudo-code would also aid reproducibility.

2. The experiments in Section 4.4 seem disconnected from the core claims. It would be advisable to include content related to this experiment in Section 3.

3. In Table 1, the performance result of FedChest + FedProx + BN-ResNet is identical to that of FedChest + FedProx + ANFR. The authors state that "we employ a large batch size of 128 to maximize the probability that all classes are represented in each batch, following best practices. This choice incidentally biases the setting in favor of BN models since larger batches reduce inconsistent averaging of mini-batch statistics and BN parameters" (lines 427–429). To gain a more detailed understanding, could the authors provide additional results using smaller or larger batch sizes? Additionally, is there further analysis to explain why this result is observed only under the FedProx setting?

### Soundness
2

### Presentation
2

### Contribution
2
