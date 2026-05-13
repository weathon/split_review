# Efficient Backpropagation with Variance Controlled Adaptive Sampling

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Sampling-based algorithms, which eliminate ``unimportant'' computations during forward and/or back propagation (BP), offer potential solutions to accelerate neural network training. However, since sampling introduces approximations to training, such algorithms may not consistently maintain accuracy across various tasks. In this work, we introduce a variance-controlled adaptive sampling (VCAS) method designed to accelerate BP. VCAS computes an unbiased stochastic gradient with fine-grained layerwise importance sampling in data dimension for activation gradient calculation and leverage score sampling in token dimension for weight gradient calculation. To preserve accuracy, we control the additional variance  by  learning the sample ratio jointly with model parameters during training. We assessed VCAS on multiple fine-tuning and pre-training tasks in both vision and natural language domains. On all the tasks, VCAS can preserve the original training loss trajectory and validation accuracy with an up to 73.87\% FLOPs reduction of BP and 49.58\% FLOPs reduction of the whole training process.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a sampling method for back propagation with controlled variance and self-adaptive sample ratios, named VCAS. It computes an approximate stochastic gradient by applying finegrained sampling to gradually remove samples and tokens during backpropagation. VCAS have similar variance as well accuracy with exact back propagation, while seems to reduce the training cost significantly.

### Strengths
1. I like it very much that the authors test the proposed algorithm on multiple fine-tuning and pre-training tasks in both vision and
natural language domains. Typically, papers in this domain would use small scale datasets such as MNIST or CIFAR 10/100.

2. The ablation studies on a few hyperparameters are very important. I see only very few of the papers in this domain have done this before.

### Weaknesses
I think the authors can improve the paper in the following ways:

1. I believe adding an algorithm table with detailed steps would make the paper more clear. 

2. The authors report the Final Train Loss / Final Eval Acc.(%) / FLOPs reduction ratio(%). However, I'd like to know the actual reduction in training time as these sampling methods might introduce overhead in computation. It would be helpful if the authors can report a time table for training on these datasets.

To be frank, I feel not many papers actually do this but it can be interesting to see that the actual training time might not be reduced at all, or at least not much as expected given a certain sampling ratio.

3. The paper lacks discussions of related paper. For example, https://arxiv.org/pdf/2104.13114.pdf also considers the importance sampling problem by sampling data points proportionally to the loss, instead of norm of gradient.

For another example, https://arxiv.org/pdf/2306.10728.pdf also proposes adaptively sampling methods for dynamically selecting data points for mini-batch. I'd love to see the authors discussed more about these papers.

4. Can the authors be more specific in terms of the notations? Adding a table of notation would be very helpful. For example, what is $h^{(l)}$ below:

$$\nabla_{Z^{(l-1)}}=h^{(l)}\left(\nabla_{Z^{(l)}} ; Z^{(l-1)}, \theta^{(l)}\right)$$


### Questions
1. Although the proposed VCAS algorithm seems promising compared with SB and UB, I'd like to know the actual reduction in training time as these sampling methods might introduce overhead in computation. It would be helpful if the authors can report a time table for training on these datasets.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes Variance-Controlled Adaptive Sampling (VCAS), which performs an approximated stochastic gradient with an adaptive sampling rate. Based on the insight that gradients are sparse after learning has progressed to some extent, the authors improve the efficiency of learning by computing only a few selected gradients through adaptive sampling. The proposed method approximates the exact backpropagation values well in BERT and ViT training.

### Strengths
VCAS performs backpropagation 20-50% faster, while following the loss curve of true full backpropagation with low variance. VCAS has an adaptive sampling rate, which allows for efficient sample selection based on learning loss and per layer. The idea is simple and highly applicable.

### Weaknesses
Comparing accuracy under the same amount of FLOPs reduction makes it difficult to understand its effectiveness compared to a metric like time to reach target accuracy[1]. As a result, it is unknown how VCAS will perform under a 50% or greater reduction. The paper does not provide sufficient detail on the relationship between the variance threshold and the resulting FLOPs reduction, making it hard to understand the trade-offs. The experimental results do not explore the sensitivity of the method to different variance thresholds, which is a critical parameter for the adaptive sampling. Furthermore, the paper lacks a clear explanation of how the adaptive sampling rate is determined per layer, and how this affects the overall performance and convergence of the model. It is also unclear how the method handles the variance introduced by the sampling process, and whether this variance is consistent across different layers and training stages.

### Questions
I would like to see more detail in Table 2 or 3. What is the relationship between Final Eval Accuracy and FLOPs reduction? For example, is the recommending FLOPs reduction ratio for VCAS around 40%?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces a variance-controlled adaptive sampling (VCAS) method for accelerating the back-propagation of deep neural network training. VCAS computes unbiased, variance controlled gradients for both activations and network weights. By sampling both data samples and tokens in each datum in a layer-wise, fine-grained manner, VCAS can drastically reduce the computation in the back-propagation process without introducing too much variance overhead. With the similar FLOPs reduction, VCAS better optimizes the target model compared with prior loss-based and gradient-based sampling methods.

### Strengths
- This work introduces a fine-grained strategy that 1) increasingly removes data samples when back-propagating to the input layer, and 2) samples tokens in each data sample when computing gradients for network weights. This fine-grained strategy allows high FLOPs reduction with controlled variance.

- The sampling ratios are adaptively adjusted according to the estimated variance. As training progresses, the network may require changing sampling ratios, and the adaptive sampling ratios can better satisfy this need.

- Compared with prior methods, the proposed method, VCAS, can better simulate exact back-propagation, leading to better optimized loss and better evaluation performance.

### Weaknesses
 - Training time reduction: When comparing with baselines, this work uses FLOPs as the efficiency indicator. However, FLOP reduction may not directly translate into wall-clock time reduction due to various factors like parallel computation efficiency, memory access patterns, and overhead from the sampling process itself. It is crucial to demonstrate that the proposed method's FLOPs reduction effectively translates to a tangible reduction in training time. The paper should include a comparison of wall-clock training time, especially for larger models and datasets, to validate the practical efficiency gains.

- Insights on sampling ratio updates: In Section 7 this work has discussed the design choices that determine the sampling ratio updates. For better comprehension, it may be useful to include a figure that shows how $s$ and $\nu_l$ changes as training progresses. The current discussion lacks a clear visualization of how these ratios evolve, making it difficult to understand the adaptive nature of the sampling process and how it responds to different training stages. A figure illustrating the dynamics of these ratios would greatly enhance the interpretability of the method.

- Figure/Table clarity: Figure 2 seems to lack some more detailed explanation, particularly regarding the specific operations and data flow within the sampling process. In Table 1, it is not clear which numbers should be bolded. For example, for ViT-base fine-tuning on CIFAR-100, UB seems to be highlighted for the highest eval accuracy, but for ViT-large fine-tuning on CIFAR-100, UB seems to be highlighted for the lowest train loss? Also for Table 1, how significant is the relative improvement over baselines? The current presentation makes it difficult to discern the key performance differences and the rationale behind the highlighting.

- Limitations: It is suggested to include some detailed discussion on the limitations (e.g., applicable model architectures, base optimizer, dataset) of the proposed method. In this paper, only Transformer-based architectures and Adam-like optimization algorithms are tested. It is not clear whether we can extrapolate the conclusion to other settings. The paper should explicitly address the potential limitations of the method, such as its applicability to different network architectures (e.g., CNNs, RNNs), optimizers (e.g., SGD, Momentum), and datasets with varying characteristics. This discussion should include an analysis of why the method might not be effective in certain scenarios.

### Questions
- It is not directly clear to me whether the weight gradient sampling of VCAS is applicable to convolution neural networks (CNN). In principle, convolution is yet another linear operator, but I’m not sure how to perform this sampling in a convolutional layer. Similarly, can VCAS be applied when optimizing a recurrent neural network (RNN)?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This manuscript proposes a sampling algorithm to eliminate computation during forward and/or BP. More specifically, a variance-controlled adaptive sampling (VCAS) method is designed to accelerate BP by computing unbiased stochastic gradients.

The effectiveness of the VCAS is justified by pre-training and fine-tuning tasks in both vision and NLP domains. Some ablation studies are also included to discuss the effects of hyper-parameters.

### Strengths
* This manuscript is well-structured, with a clearly explained methodology section.
* The manuscript evaluates the effectiveness of the VCAS on pre-training and fine-tuning tasks in both vision and NLP domains.
* An ablation study is also included.

### Weaknesses
1. Limited literature review. This manuscript did not carefully examine the relevant papers, and some closely related papers were omitted from the discussion, e.g., [1, 2, 3] and the related work in [1]. The manuscript fails to adequately position itself within the broader context of sparse training methods, particularly those focusing on reducing computations during backpropagation. The discussion should include methods that explore structured sparsity, which can be more hardware-friendly than unstructured approaches.
2. Limited baseline evaluations. Close baseline methods e.g., [2, 3] should be considered. The evaluation lacks a comprehensive comparison against state-of-the-art sparse backpropagation techniques. The absence of comparisons with methods that achieve structured sparsity makes it difficult to assess the practical advantages of the proposed method, especially in terms of real-world speedup on various hardware.
3. Additional hyper-parameters and insufficient ablation studies. The ablation study on one task, i.e., fine-tuning BERT-base on MNLI, is insufficient to justify the insensitivity of these hyper-parameters. The study should include a wider range of tasks and datasets to demonstrate the robustness of the method across different scenarios. The impact of hyperparameter choices on both the convergence rate and final performance should be more thoroughly investigated.
4. Clarity. Some design choices in Section 5 are just given and have no explanation. For example, how to derive the provided equation from the mentioned zeroth-order algorithm? The description of the variance control mechanism is unclear, and the connection between the zeroth-order algorithm and the update rule is not well-explained. The manuscript should provide a more detailed derivation and intuitive explanation of the update process.
5. The claim on the unbiased stochastic gradient needs to be more careful and some theoretical justifications should be provided. While the method aims to compute unbiased stochastic gradients, the manuscript lacks a rigorous mathematical proof demonstrating this property. The theoretical analysis should include a formal proof of unbiasedness, addressing potential sources of bias in the sampling and backpropagation process.

### Questions
NA

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
