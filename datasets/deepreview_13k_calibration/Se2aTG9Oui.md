# CoNNect: A Swiss-Army-Knife Regularizer for Pruning of Neural Networks

- Decision: Reject
- Avg Score: 4.80
- Scores: 3, 6, 6, 6, 3

## Abstract
Pruning encompasses a range of techniques aimed at increasing the sparsity of neural networks (NNs). These techniques can generally be framed as minimizing a loss function subject to an $L_0$-norm constraint. In this paper, we introduce CoNNect, a novel differentiable regularizer for sparse NN training that quantifies connectivity in weighted graphs. Our theoretical and numerical analyses show that CoNNect integrates seamlessly with many established pruning strategies and is applicable to both unstructured and structured pruning. By including CoNNect as a regularizer during training, we ensure neural networks maintain connectivity between input and output layers, addressing limitations of $L_1$-regularization, a common surrogate for $L_0$-norm regularization. We prove that CoNNect effectively approximates $L_0$-regularization, guaranteeing maximally connected network structures as stable stationary points and avoiding issues like layer collapse. Through numerical experiments, we demonstrate that classical pruning strategies benefit from CoNNect regularization compared to $L_1$- and $L_2$-norm regularization. Additionally, we show that integrating CoNNect into LLM-pruner, a one-shot pruning method for large language models, yields improved results.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The focus of the paper is to develop a pruning strategy for a sparse network. This has been
achieved by the differentiable regularizer. The approach maintains connectivity and prevents
layer collapse. This is an important and topical area of research. The results from the approach 
in the paper, named CoNNect has been compared with L1 norm regularizer and used for one-shot
pruning in LLMs.

### Strengths
1. A proof that the approach approximated the L0 regularizer  and guarantees maximally connected
structures as a stationary points.

### Weaknesses
1. Several research work on pruning has aimed at and succeeded in accomplishing 
even more successfully what has been achieved here.
2. A comparison with the existing body of literature is needed as maximal connectivity, 
avoiding layer collapse and zero shot pruning have also been addressed previously. 
So the contribution of this work in the correct context is not emphasized.
3. The CoNNect is only compared with magnitude pruning and Synflow. Other pruning
approaches have not been considered for comparison.
4. The experimental results in Table 2 doesn't show any significant difference
with CoNNect as compared to others. The performance also falls significantly 
with pruning.

### Questions
1. How are the theoretical results reflected in the experimental results?
A more through analysis perhaps can give more insight about the impact of 
the regularizer.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the problem of neural network pruning. The authors propose two axioms for pruning: reducing the NNs' size by removing unnecessary weights and preserving their connectivity to ensure stable information flow. To address these two axioms, the authors propose a novel regularizer called CoNNect, which computes a connectivity matrix based on Katz centrality, providing a measure that prefers direct paths over parallel ones. The method demonstrates higher performance in various pruning scenarios, including VGG-11 for CIFAR-10 and large language models (LLMs) like LLaMA-7B for various NLP tasks.

### Strengths
1. It is a novel use of Katz centrality to enhance pruning by maintaining connectivity, which is an overlooked factor in neural network pruning. This approach ensures that information can effectively flow from input to output layers, addressing the common issue of layer collapse in sparse networks.

2. The authors develop a strong theoretical foundation, proving that CoNNect approximates L0 regularization while preventing collapse, which strengthens the validity of their approach.

3. Through comprehensive experiments, the authors provide evidence of CoNNect’s superiority over standard L1- and L2-based regularization techniques. The approach's effectiveness in CV and NLP benchmarks demonstrates the practical impact of this research.

4. The writing is clear and well-structured, making it easy to follow the authors’ arguments and contributions.

### Weaknesses
1. The authors should discuss more about the second axiom (Preserve Neural Network Connectivity). Why is preserving connectivity important for pruning? How could keeping the flow of information benefit the performance of the pruned model? More insights on this point would make the paper more convincing.

2. The convergence analysis for regularizer loss in lines 243-280 seems impractical and unnecessary, since the parameters not only receive gradients from the regularizer but also from the main task loss. Then these two gradients will added together. With this different gradient, will it still converge to minimal point of regularizer loss?

3. This work does not apply to some important architectures like resnet with residual connections. The authors could provide some discussions on possible solutions for these architectures.

4. The experiments are not extensive. If the authors could provide more results on some modern CV models and datasets, it would be more convincing.

### Questions
My main concerns and suggestions are already mentioned in the weaknesses section. I would like to mention some minor points here.

1. Time/space complexity analysis could be provided.

2. The presentation could be improved. I think Figure 2 could serve as a perfect illustration of intuition, thus I suggest drawing a similar one in the introduction part.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
The paper introduces a new neural network pruner CoNNect that focuses on maintaining connectivity between network layers. CoNNect achieves this by leveraging Katz centrality to ensure sparse yet fully connected networks. The CoNNect regularizer is a differentiable and effective surrogate for the L0 norm, promoting sparse architectures while preserving crucial connections. CoNNect avoids issues like layer collapse by maintaining a stable structure, beneficial for both unstructured and structured pruning. Experiments demonstrate that Connect performs well on the LLMs.

### Strengths
1. The paper is overall well-written and logically well-organized.
2. The CoNNect is proven to approximate the L0-norm regularization, and the pruned neural network architecture guarantees the maximal connected network structure, which seems solid.
3. The CoNNect is differentiable and can be optimized by gradient descent.

### Weaknesses
1. In the introduction, the author highlights that neural network connectivity is important for good running. However, the benefits of maintaining such connectivity for pruning are unclear to readers. It would be better if the authors could illustrate this further. Specifically, what are the failure modes of pruning methods that do not explicitly maintain connectivity, and how does maintaining connectivity mitigate these issues? For instance, do such methods lead to fragmented networks that hinder information flow, or do they result in unstable training dynamics?

2. In Section 3.3.1, the motivation to use Katz centrality for neural network pruning can be illustrated better. Specifically, while there are many centrality measures in network analysis, it is unclear why Katz centrality stands out. The authors should elaborate on the specific properties of Katz centrality that make it suitable for this task, compared to other measures like betweenness centrality or eigenvector centrality. What advantages does it offer in terms of identifying and preserving crucial connections for network functionality?

3. In Section 4.1, is it necessary to prune a small MLP model for evaluation? While the authors claim it illustrates the working of CoNNect, it is not clear why this small-scale experiment is needed, given the more extensive evaluations on larger models. What specific insights does the MLP experiment provide that cannot be gleaned from the other experiments? Does it offer a unique perspective on the behavior of CoNNect, or is it redundant?

4. Some typos, e.g. caries -> carries in Line 348.

### Questions
Please refer to weaknesses. Because the reviewer is not an expert, the novelty and the correctness of the proofs cannot be evaluated.

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
This work proposed CoNNect, a regularization-based neuron connectiviy-preseving neural network pruning algorithm. Specifically, the authors consider the computation graph of neural network as a directed weighted graph, where the each node represents a neuron, each weight parameter represents a weighted-edge. The CoNNect regularizer penalizes the the negative logarithm of the connectivity between the input layer and the output layer. The authors proved that 1) Theorem 1: CoNNect does incur sparsity, 2) Theorem 2: the stationary points of CoNNect regularizer are its global minimizers. The authors validate the effectiveness of CoNNect on MLP on synthesis regression data, VGG-11 on CIFAR-10, and LLaMA-7B on multiple datasets.

### Strengths
1. The authors introduce a principled algorithm (CoNNect regularizer) to preserve the output-input layer connectivity during pruning.
2. The authors provide theoretical guarantee on the sparsity of CoNNect minizer, and characterize its stationary points.
3. The authors validate the effectiveness of CoNNect on MLP, VGG, and LLaMA-transformer.

### Weaknesses
1. The connectivity analysis did not explicitly consider the residual connection structure, which is ubiquitous in mainstream machine learning models, e.g. ResNet, UNet, and Transformers. When the residual connection is involved, the input and output features are ensured to be connected. In this case, it seems that existing pruning methods can still enjoy a satisfactory connectivity between the input and output layer. I wonder to what extend does the residual connection structure overshadow the necessity and benefit of the proposed CoNNect regularizer (which may hinder the training process). Specifically, the current formulation of the connectivity regularizer appears to treat the residual connection as a constant, effectively ignoring its contribution to the overall connectivity graph. This simplification could lead to inaccurate connectivity measurements, particularly in networks with extensive residual connections. The analysis should explicitly model how the skip connections influence the connectivity metric and how the proposed regularizer interacts with these structures. Furthermore, it's unclear whether the theoretical guarantees on sparsity and stationary points still hold when these connections are properly accounted for in the connectivity graph.

2. Beside the standard gradient-based $L_1$ regularization, the authors are recommended to compare their method with improved $L_1$ optimization methods, e.g. Lasso shrinkage operator-based optimization [1] and Spred-$L_1$ [2]. It's important to evaluate the method's performance against more recent and sophisticated $L_1$ regularization techniques, which often incorporate adaptive learning rates or other optimization strategies. A direct comparison with these methods would provide a clearer understanding of the advantages and limitations of the proposed approach. Specifically, the Lasso shrinkage operator and Spred-$L_1$ methods offer potentially more efficient ways to achieve sparsity, and it is crucial to assess if the proposed method can offer comparable or better performance in terms of both sparsity and model accuracy.

3. According to Figure 4, it seems that the CoNNect regularizer hinders the train from scratch process of the model, as the `No Reg. w/ Tun` consistently outperforms the `CoNNect Reg. w/ Tun.` until a pruning ration below $0.8$. This observation raises concerns about the practical applicability of the proposed regularizer in scenarios where training from scratch is required. The regularization seems to impede the learning process, leading to lower performance compared to the non-regularized model, especially at lower pruning ratios. This suggests that the regularization might be overly aggressive or not well-tuned for the initial training phase, and further investigation is needed to understand the trade-offs between connectivity preservation and model performance.

4. Minor Typo:

   a) In Page 4, lines 207-210, should $V_k$ be captalized as $V_K$?

   b) Page 6, lines 311-312, magnetude-based.

### Questions
1. Can the authors provide the detailed implementation of the calculation of the total conectivity regularizer Eq. (3) for mainstream architectures (e.g. VGG, ResNet, Transformer, UNet)? Do we need to parse the network into an adjacency matrix representation, or there is a more efficient and practicable implementaion?

2. Can the authors compare the FLOPs and inference acceleration of the pruned models against the baseline methods? Can the authors provide a complexity analysis of the proposed algorithm?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces a novel differentiable regularizer, CoNNect, for training sparse neural networks. Inspired by Katz centrality from graph theory, CoNNect is designed to enhance neural network pruning techniques while maintaining key connectivity between the input and output layers throughout training. Traditional pruning methods often rely on L1-regularization as a surrogate for L0-norm, but these methods may lead to issues like layer collapse and loss of network structure. CoNNect addresses these limitations by ensuring the network retains essential paths, thereby preserving the model’s performance during pruning.

The paper demonstrates CoNNect's ability to approximate L0-regularization more effectively than L1-regularization, leading to improved sparsity without sacrificing connectivity. It is suitable for both unstructured and structured pruning techniques. The authors validate CoNNect's performance across several experiments, including channel-level pruning in CNNs and one-shot pruning for large language models, demonstrating improved performance compared to existing pruning techniques.

### Strengths
1. **Originality**: 
   The paper introduces an original approach by leveraging Katz centrality, a concept from graph theory, to measure and preserve neural network connectivity during pruning. 

2. **Quality**: 
The authors establish the stability and effectiveness of CoNNect in approximating L0 regularization while avoiding layer collapse. 

3. **Clarity**: 
   The paper is fairly well-written and structured.

4. **Significance**: 
The CoNNect regularizer directly tackles the limitations of L1 regularization and other sparsity-inducing methods, which often lead to disconnected or underperforming models. By maintaining network connectivity, CoNNect ensures that pruned models retain their predictive power and functional integrity.

### Weaknesses
1. **Complexity of Implementation**:
   The complexity of implementing the CoNNect regularizer in practice remains a concern. The reliance on Katz centrality, while novel, introduces additional computational overhead, particularly when calculating the inverse of the matrix $(I - \theta(W))$. This operation's cost scales with the size of the weight matrix, which can be substantial for large neural networks. The paper lacks a detailed analysis of the computational cost of this operation and how it scales with different network architectures and sizes. Furthermore, the paper does not provide sufficient guidelines or discussion about how CoNNect scales with larger and more complex neural network architectures, particularly in real-world environments.

2. **Lack of Comprehensive Comparisons**:
   While the paper demonstrates that CoNNect outperforms traditional L1 and L2 regularization and some pruning methods like SynFlow, it lacks a comparison with other contemporary pruning techniques. For instance, techniques like Lottery Ticket Hypothesis-based pruning (Frankle & Carbin, 2019), DLTH  (Bai et al. 2022),  or other structured pruning methods using adaptive sparsity (e.g., Movement Pruning by Sanh et al., 2020) are notably absent. To strengthen the empirical validation, the authors should include experiments that compare CoNNect with these other pruning frameworks. The absence of these comparisons makes it difficult to assess the true performance of CoNNect relative to the current state of the art.

3. **Limited Architectural Diversity in Experiments**:
   The paper focuses mainly on feedforward networks, convolutional neural networks (CNNs), and large language models (LLMs), but does not include experiments on other widely-used architectures such as recurrent neural networks (RNNs), transformers, or graph neural networks (GNNs). The authors claim that CoNNect can be applied across various neural network architectures, but the lack of empirical evidence on a broader range of models weakens this claim. For example, the application of CoNNect to RNNs, which have different connectivity patterns and temporal dependencies, is not explored. Similarly, while the method is applied to LLMs, there is no exploration of its effects on other transformer-based architectures.

4. **Insufficient Exploration of Hyperparameters**:
   The paper uses fixed hyperparameter values for CoNNect across different experiments, but there is limited discussion on how sensitive CoNNect is to these hyperparameters or how they should be tuned for different models or datasets. Given that regularization methods can be highly sensitive to parameter tuning, especially in complex neural networks, it would be beneficial for the authors to conduct an ablation study or sensitivity analysis on the regularization coefficients used in CoNNect. The lack of such analysis makes it difficult to determine the robustness of the method and its generalizability to different settings.

### Questions
I would like to see more comprehensive comparisons with other recent pruning techniques for large language models (LLMs). For instance, the following two papers report higher accuracies at more aggressive levels of pruning, as evidenced by Table 23 in the *Wanda* paper (the second in the list):

1. **SparseGPT: Massive language models can be accurately pruned in one-shot** (Elias Frantar and Dan Alistarh, ICML 2023)
2. **A simple and effective pruning approach for large language models** (Sun et al., ICLR 2024)

Incorporating these methods into the experimental results would provide a clearer picture of how **CoNNect** performs relative to state-of-the-art pruning techniques for LLMs, particularly when it comes to accuracy and the extent of pruning.

Additionally, the experiments in the current paper are not sufficiently comprehensive. The results are reported for only one LLM architecture and one model size. However, in empirical studies of this nature, it is common practice to evaluate multiple model sizes across different architectures to ensure generalizability. Expanding the range of experiments would help substantiate the claims made about CoNNect’s effectiveness and scalability.

### Soundness
2

### Presentation
2

### Contribution
2
