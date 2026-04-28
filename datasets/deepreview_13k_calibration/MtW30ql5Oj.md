# BP-Modified Local Loss for Efficient Training of Deep Neural Networks

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 6, 5, 8

## Abstract
The training of large models is memory-constrained, one direction to relieve
    this is training using local loss, like GIM, LoCo, and Forward-Forward
    algorithms. However, the local loss methods often face the issue of slow or
    non-convergence. In this paper, we propose a novel BP-modified local loss
    method that uses the true Backward Propagation (BP) gradient to modify the
    local loss gradient to improve the performance of local loss training. We
    use the stochastic modified equation to analyze our method and show that
    modified offset decreases the bias between the BP gradient and local loss
    gradient, but introduces additional variance, which results in a
    bias-variance balance. Numerical experiments on full-tuning and LoKr tuning
    on the ResNet-50 model and LoRA tuning on the ViT-b16 model on CIFAR-100
    datasets show 20.5\% test top-1 accuracy improvement for the Forward-Forward
    algorithm, 18.6\% improvement for LoCo algorithm and achieve only on average
    7.7\% of test accuracy loss compared to the BP algorithm, with up to 75\%
    memory savings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a method to compute local loss based on BP which significantly improves performance of local loss based training methods with negligible memory overhead.

### Strengths
Significantly improved performance compared to SoTA local loss based learning methods

Results in negligible additional memory usage

Strong theocratical foundations for proposed method

### Weaknesses
Compare throughput with SoTA local loss-based learning methods

Misc:
Paraphrase line 31, 32, and 33 for better readibility

### Questions
Is there any overhead in latency or throughput for BP-modified loss compared to other local loss-based training methods?

Is the bias-variance trade-off analysis generalizable across various model architectures and tasks, or are there conditions under which it may not apply?

Can you further explain how using true gradient information doesn’t increase memory usage?

The lazy update and mini-batch splitting techniques are introduced to manage memory and computational costs. How sensitive is the method to the choice of period K and mini-batch size B'?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new BP modified local loss method, which aims to adjust the local gradient by introducing an additional offset to reduce the deviation between the local gradient and the true gradient and introduce additional variance. This approach improves the performance of local loss training while maintaining memory efficiency. The theoretical analysis and experimental results of the paper show that this method can effectively improve performance on different models and tasks, while significantly reducing memory usage. This is an interesting and promising research direction with important implications for the deep learning community.

### Strengths
Innovation: The proposed BP modification of local loss method improves training efficiency while reducing memory usage, which is a valuable contribution.
Theoretical analysis: The paper provides a theoretical analysis based on the random modification equation, deeply explores the bias-variance trade-off, and derives the optimal scaling factor.

### Weaknesses
Impact of delayed gradient adjustment: The paper discusses the noise accumulation and bias adjustment problems that may be caused by delayed gradient adjustment, but does not provide a detailed analysis. Specifically, the paper lacks a discussion on how the delay in applying the offset gradient affects the convergence rate and stability of the training process. It is unclear how the accumulated noise interacts with the momentum of the optimizer, potentially leading to oscillations or divergence. A more rigorous analysis, possibly including a study of the eigenvalue spectrum of the Hessian with the delayed gradient, would be beneficial. It is recommended that the authors further study the impact of these factors on training dynamics and explore possible solutions.
More extensive experimental validation: Although the paper conducts experiments on multiple models and tasks, it is still recommended to conduct further experimental validation on larger models and datasets to demonstrate the universality and scalability of the method. The current experiments, while promising, do not fully explore the method's behavior on very deep networks or datasets with significantly more complex data distributions. For instance, the performance on datasets like ImageNet with full resolution images and deeper architectures should be investigated to ascertain the method's robustness.

### Questions
The paper mentions hyperparameters such as offset batch size B' and sampling period K, but does not discuss the selection of these parameters in detail. It is recommended that the authors provide more analysis on how these hyperparameters affect model performance and memory usage.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, authors proposed a novel training algorithm called BP-modified local loss, which aims to address non-convergence issues and poorer performance in the previous local loss methods, e.g., GIM, LoCo, and Forward-Forward algorithm. It combines backward propagation (BP) with local loss methods by modifying the local gradient using the BP gradient to balance bias and variance.

### Strengths
1. Strong empirical results: The BP-modified local loss shows significant improvement, e.g., up to 36% improvement in the test accuracy for Forward-Forward algorithm, 20% for LoCo and 11% for MPC.

2. The use of scaling factors $\alpha_{h}$ and $\lambda_{h}$ to manage the bias-variance balance is well motivated. The use of stochastic differential equations to model the modified training dynamic helps in understanding the benefits, as well as the limitations of the method.

### Weaknesses
1. Generalisability is one of the major concerns, as the scope of the experiments is a bit limited. The results are primarily conducted on CIFAR-100, a relatively small dataset. While the improvements are evident, a more robust evaluation that includes larger datasets like ImageNet, as well as tasks other than image classification, would make the proposed method more convincingly. Specifically, the current evaluation lacks diversity in both dataset scale and task complexity, making it difficult to ascertain the method's effectiveness in more realistic and challenging scenarios. The absence of experiments on larger-scale datasets such as ImageNet, which is a standard benchmark for image classification, raises concerns about the method's scalability. Furthermore, the method's applicability to other tasks beyond image classification, such as object detection or natural language processing, remains unexplored, which limits the understanding of its general applicability.

2. The authors leveraged the Ornstein-Uhlenbck process to model the bias-variance dynamic, however, the OU process is a simplified linear model, and deep neural network training is inherently non-linear and non-convex. The validity of the approximation that discussed in the paper would require some empirical evidence to support, as well as some discussions in more depth. For example, deep neural networks exhibit different training dynamics across layers, with shallow and deep layers experiencing different gradient behaviours. Can authors provide how gradients evolve for different layers and test if the OU process holds similarly for both shallow and deep layers. The use of a linear model to represent a complex non-linear process like neural network training raises questions about the accuracy and relevance of the theoretical analysis. The analysis does not account for the non-convexity of the loss landscape, which can significantly affect the training dynamics. Additionally, the assumption that the training dynamics are similar across all layers of the network is questionable, as different layers may exhibit vastly different behaviors in terms of gradient magnitudes and noise characteristics. This lack of granularity in the analysis limits its ability to provide a comprehensive understanding of the proposed method's behavior.

### Questions
1. The method introduced several new hyper-parameters, such as batch size $B^{'}$ for the BP gradient, scaling factors $\lambda_{h}$ and $\alpha_{h}$, as well as the lazy update period $K$. I wonder how sensitive is the performance to these hyper-parameters, can authors report sensitivity analyses for these hyper-parameters? And what guidance or insight can authors provide on how to tune them for different models and datasets? Specifically, the optimal scaling factors, $\lambda_{h}$ and $\alpha_{h}$, are derived theoretically, but their practical implementation seems challenging. 

2. Although the authors adopted some strategies like lazy update and split mini-batch, computing the offset $Δg_{h,t}$ involves additional operations. I wonder what’s the overhead in terms of runtime and memory usage as the depth of the network increases? Can authors quantify the impact of these additional operations on the overall training efficiency? Such as total training time, per-epoch time as well as GPU memory usage as the depth of the network increases?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a novel BP-modified local loss to improve the performance of local loss training, which decreases the bias between the BP gradient and local loss gradient but introduces additional variance. Then authors provide a theoretical analysis using the stochastic modified equation, illustrating the bias-variance trade-off and deriving optimal scaling factors. Experiment results show that the proposed method can effectively improve the performance of local loss algorithm while increase little GPU memory.

### Strengths
- The theoretical derivation of the proposed BP-Modified Local Loss algorithm is convincing.
- Experimental results indicate that the proposed method significantly improves the performance of local loss training algorithm.
- The paper is highly readable and describes the implementation details of BP-Modified Local Loss algorithm in detail.

### Weaknesses
 - The main motivation of local training algorithms is to train large datasets or large models in resource-constrained environments. So I think authors could scale to some datasets larger than CIFAR-100, such as the ImageNet, to better illustrate the applicability of the proposed method and meet the design motivation.
- The optimization of the Loss function tends to significantly affect the training convergence performance. So I think it is necessary to provide model training time comparison results between the BP-Modified Local Loss method and other Local Loss baseline methods, such as total epochs needed for convergence.

### Questions
Overall, I think this is a good paper and I would raise rating if authors could address my concerns above. In addition, I suggest adding some figure descriptions if possible so that the readers could more clearly understand the authors’ intention.

### Soundness
3

### Presentation
4

### Contribution
3
