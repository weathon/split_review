# Optimizing Activations Beyond Entropy Minimization for Test-Time Adaptation of Graph Neural Networks

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 3, 6

## Abstract
Test-time adaptation for classification models involves optimizing classifiers through self-supervised learning without labeled training samples. Existing methods often rely on entropy minimization as the optimization objective, which indeed addresses the model performance connections with prediction confidence or representations amenable to cluster structure. However, due to the lack of ground truth in training samples, test-time adaptation, as an effective way to deal with the shifting dataset distributions or domains, can sometimes lead to model collapse. In this paper, we focus on optimizing activations in batch normalization (BN) layers for test-time adaptation of graph neural networks (GNNs). Unlike many entropy minimization methods prone to catastrophic model collapse, our approach leverages pseudo-labels of test samples to mitigate the potential forgetting of training data. 
We optimize activations in BN by a two-step process. First, we identify weights and masks for the empirical batch mean and variance of both training and test samples. Subsequently, we refine BN's scale and shift parameters using a reformulated loss function with an energy-based model for improved generalization. Empirical evaluation across seven challenging datasets demonstrates the superior performance of our method compared to state-of-the-art test-time adaptation approaches.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a novel two-step optimization method for test-time adaptation (TTA) in graph neural networks (GNNs), focusing on fine-tuning batch normalization (BN) activations. This approach effectively tackles distribution shifts, which is an important issue in GNNs, especially for practical applications involving non-stationary environments

### Strengths
1.	The paper proposed method is sound.
2.	Writing is good to follow.
3.	Comprehensive experiments on seven diverse datasets with different types of distribution shifts demonstrate the effectiveness of the proposed method. 
4.	Large scale graphs like OGB-Products are included in the experiments.

### Weaknesses
1.	Only evaluate the performance on shallow GNNs. Some deep GNN should also be evaluated (e.g., GCNII).
2.	The improvement is marginal on some datasets (e.g., Twitch-E)
3.	The paper could benefit from deeper theoretical insights or a more thorough justification

### Questions
See the above weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work proposes a two-step batch normalization optimization method for test-time adaption in graph neural networks for better generalization performance. First, they determine weights and masks for the empirical batch mean and variance, considering training and test data statistics. Subsequently, they refine the scale and shift parameters of the BN layers using a reformulated loss function incorporating an energy-based model, aiming to enhance the model’s generalization capabilities. The experiment results show its good performance.

### Strengths
The method is clear, easy to understand.

### Weaknesses
For method: Tuning the parameter of batch normalization layer is a common idea in test-time adaption area, including optimizing parameter and statistic values. Although this paper proposes new idea of masking and model calibration, it lacks explanation/empirical results to explain the reason for their designs. It is more like an ensemble of several tricks instead of a complete algorithm. Therefore, the method is less attractive to me.

For experiment: The baseline accuracy in Table 1 is much lower than results shown in other papers[1][2], such as test accuracy on OGB-Arxiv and OGB-Products.

### Questions
see Weaknesses

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
This paper presents a new approach for test-time adaptation (TTA) in classification models, specifically targeting graph neural networks (GNNs). This work optimizes the activations in batch normalization (BN) layers to improve TTA performance. To prevent forgetting of training data, the method uses pseudo-labels derived from test samples.

### Strengths
1. This work addresses test-time adaptation for graph neural networks (GNNs), which is an important research direction.

2. The authors have provided code that enables reviewers to validate the proposed method.

### Weaknesses
1. The proposed method appears complex and lacks elegance (particularly Sec 3.1), making it difficult to understand. Providing pseudocode for the whole method might help clarify the approach and improve reader comprehension.

2. The performance improvement achieved by this method is marginal (Table 1), making it challenging to demonstrate the superiority of the approach compared to existing methods.

3. The reliance on pseudo-labels could be problematic if the pseudo-labels are inaccurate, especially in scenarios with complex distribution shifts, such as in dynamic or mixed domain shifts found in real-world or online settings like SAR. Please validate the method’s effectiveness in these challenging settings. Additionally, if optimization becomes unstable, are there any solutions to address this issue?

4. Please include an ablation study on the impact of test batch size on model performance to understand how sensitive the method is to this parameter.

### Questions
Please refer to the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
The paper offers a method to optimize different batch normalization parameters when performing test-time adaptations for GNNs. The paper focuses on optimizing all the BN parameters rather than just the mean and variance, and shows empirically that the proposed method outperform the previous such method in a significant margin across several datasets using number of architectures.

### Strengths
Originality: the paper suggests learning other parameters of BN layers, which makes sense given the methods suggested in previous works. As far as I can tell, this method is original and novel, and well places in the current literature.

Clarity: The paper is written in a clear way, and it was easy to follow the suggested ideas and the motivations behind them.

Quality: The suggested method is tested across several benchmarks using different architectures. I'm fairly convinced that the method work, and improves the upon the previous methods. The papers presents a good ablation study which checks the different parts of the method.

Significance: The results presented show notable improvements over previous works, suggesting that the approach could positively impact the field.

### Weaknesses
Originality: While the method is novel, it may be perceived as somewhat incremental, as it only modifies BN layers, similar to several previous studies.

Quality: The paper could be strengthened with additional results, particularly a comparison of computation times with baseline methods. Since the approach calculates second-order statistics, this might incur computational costs, which would be useful to discuss. Additionally, as the baseline methods also approximate the mean and variance of the BN layers, it would be helpful to see if using the suggested method to calculate only the scale and shift of the BN layers, but then using the mean and variance calculated by the baseline methods is also beneficial.

Significance: The scalability of this method to larger networks and datasets is unclear. Without the computational cost analysis and baseline comparisons, it’s challenging to fully assess the impact of the results.

----

Summary:

The paper could be significantly improved by including the suggested additional experiments. Nonetheless, I believe it has merit for publication, which is why I recommend a weak accept.

Disclaimer: This paper is outside my primary area of expertise. My review provides only a general assessment, and there may be aspects regarding related work or specific methodological details that I have missed.

### Questions
Can the method be implemented when the data is significantly larger? How fast it is to implement it?

What happens if you use the mean and variance calculated by other methods, and calculate the scale and shift using your method?

### Soundness
3

### Presentation
3

### Contribution
3
