# SPAM: Spike-Aware Adam with Momentum Reset for Stable LLM Training

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Large Language Models (LLMs) have demonstrated exceptional performance across diverse tasks, yet their training remains highly resource intensive and susceptible to critical challenges such as training instability. A predominant source of this instability stems from gradient and loss spikes, which disrupt the learning process, often leading to costly interventions like checkpoint recovery and experiment restarts, further amplifying inefficiencies. This paper presents a comprehensive investigation into gradient spikes observed during LLM training, revealing their prevalence across multiple architectures and datasets. Our analysis shows that these spikes can be up to 1000× larger than typical gradients, substantially deteriorating model performance. To address this issue, we propose Spike-Aware Adam with Momentum Reset (SPAM), a novel optimizer designed to counteract gradient spikes through momentum reset and spike-aware gradient clipping. Extensive experiments, including both pre-training and fine-tuning, demonstrate that SPAM consistently surpasses Adam and its variants across a range of model scales. Additionally, SPAM facilitates memory-efficient training by enabling sparse momentum, where only a subset of momentum terms are maintained and updated. When operating under memory constraints, SPAM outperforms state-of-the-art memory-efficient optimizers such as GaLore and Adam-Mini. Our work underscores the importance
of mitigating gradient spikes in LLM training and introduces an effective optimization strategy that enhances both training stability and resource efficiency at scale. Code is submitted.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a novel optimization method designed to mitigate training instabilities, specifically gradient and loss spikes in large language models (LLMs). The method, SPAM, introduces momentum reset and spike-aware gradient clipping to counteract the effects of significant gradient spikes that can disrupt the learning process. Extensive experiments suggest that SPAM outperforms traditional Adam and its memory-efficient variants, offering better stability and performance across different model scales and training setups.

### Strengths
- The paper’s analysis highlighting the prevalence and impact of gradient spikes in LLM training is insightful and demonstrates an important issue.
- The experiments show consistent improvements across different LLM sizes and benchmarks, suggesting the method’s robustness within these settings.
- The introduction of sparse momentum is a useful addition for reducing the memory overhead of training large models.

### Weaknesses
 - Although SPAM is compared to Adam and a few memory-efficient optimizers, it lacks comprehensive analysis against more recent memory-efficient methods. Furthermore, additional experiments, as outlined below, are necessary to strengthen the evaluation.



### Questions
1. **Detrimental effects of gradient spikes**. It would be valuable to observe the middle and right plots of Figure 5 during actual training.
2. **Moment reset.** Does the benefit of momentum reset lie in isolating the effects of gradient spikes, even at the cost of training intervals affected by these spikes?
3. **Statistical significance**. Were the fine-tuning experiments conducted using multiple random seeds?
4. **Baselines**. How does this method compare with other memory-efficient approaches such as MeZO [1], SparseMeZO [2], and Extremely Sparse MeZO [3]?
5. **Ablation studies**.
    1. There is no comparison between Spike-Aware Clipping and simply nullifying gradient spikes.
    2. It would be interesting to see if the parameter for sparse momentum could be selected in a structured manner, as described in  [4].
    3. What happens in the case $\triangle T < N$?
6. **Loss and Gradient plots of SPAM**. How do the loss and gradient plots of SPAM compare with those of other methods shown in Figures 2-4?
7. **Computational analysis**. Can the authors report the computational overhead of SPAM compared to other methods?

[1] Malladi, Sadhika, et al. "Fine-tuning language models with just forward passes." *Advances in Neural Information Processing Systems* 36 (2023): 53038-53075.

[2] Liu, Yong, et al. "Sparse mezo: Less parameters for better performance in zeroth-order llm fine-tuning." *arXiv preprint arXiv:2402.15751* (2024).

[3] Guo, Wentao, et al. "Zeroth-Order Fine-Tuning of LLMs with Extreme Sparsity." *arXiv preprint arXiv:2406.02913* (2024).

[4] He, Yang, and Lingao Xiao. "Structured pruning for deep convolutional neural networks: A survey." IEEE transactions on pattern analysis and machine intelligence (2023).

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces SPAM (Spike-Aware Adam with Momentum Reset), an innovative optimization approach aimed at stabilizing the training of LLMs. SPAM addresses the challenges of gradient and loss spikes that result in training instability, which can require costly interventions such as checkpoint recovery. The proposed method improves the ADAM optimizer via integrating two key mechanisms:  spike-aware gradient clipping and momentum reset. These novelties contribute to mitigating the accumulation of gradient spikes, therefore enhancing the training stability and efficiency. Extensive experiments show that SPAM outperforms ADAM and other memory-efficient optimizers like GaLore and Adam-Mini over various LLM sizes and tasks, supporting its potential to improve training under memory constraints.

### Strengths
1. The integration of momentum reset and spike-aware gradient clipping into Adam is noval and addresses the persistent issue of gradient spikes in Large Language Model training.
2. The experiments are thorough and extensive, with evaluations spanning multiple LLM architectures and scales. The results clearly manifest SPAM's superior performance over the standard and memory-efficient baselines.
3. The approach is highly relevant, especially for large-scale training where stability and efficiency are paramount.
4. SPAM's sparse momentum feature is especially useful for resource-constrained training, making it an important contribution to memory-efficient optimization approaches.

### Weaknesses
1. The paper mentions the efficient implementation of momentum reset and spike detection, but a moredetailed practical guidance or pseudo code might improve reproducibility.
2. While SPAM performs excellently across various Large Language Model sizes, additional experiments on tasks beyond LLM training, such as CV models or multi-task learning, should illustrate broader applicability.
3. The choice of the gradient spike threshold might affect performance to a great extent. More discussion on how to tune this parameter across different model architectures would be of benefits.

### Questions
Could the spike-aware clipping method proposed be extended to handle other types of optimization tasks and scenarios, like adversarial training?

### Soundness
3

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
This paper analyzes the phenomenon of loss spikes observed in large language models (LLMs) and reveals that loss spikes are not restricted to specific layers or architectures, but occur in a wide range of environments. The authors experimentally demonstrate that loss spikes affect the performance of AI systems and mathematically show that loss spikes are influenced by momentum-based optimizers, such as Adam. The proposed method, SPAM (Stochastic Gradient Projection with Adaptive Momentum), effectively addresses this issue by using a threshold-based approach to manage the average gradient. The paper compares the performance of SPAM in both pre-training and fine-tuning stages with various other methods, showing its effectiveness.

### Strengths
This paper addresses the loss spike problem from the perspective of gradient clipping and demonstrates the algorithm's validity through an ablation study on the hyper-parameters used in the algorithm, along with various performance improvements. Additionally, the paper proposes a memory-efficient algorithm using sparse momentum, aiming to solve both the loss spike issue and the out-of-memory problem simultaneously.

### Weaknesses
1. Clipping gradients based on a threshold seems to lack novelty. It might be worthwhile to consider methods that prevent gradient spikes altogether.
2. In sparse momentum, a random mask is applied, setting certain gradients to zero. It would be helpful to explain in detail how this actually reduces memory usage. From an algorithmic perspective, it appears as though the entire matrix, including the zero elements, is still being stored.

### Questions
1. The use of theta in GSS seems heuristic. How about selecting outliers based on the known distribution (such as Gaussian) of gradients instead? [Umut Simsekli, Levent Sagun, & Mert Gurbuzbalaban. (2019). A Tail-Index Analysis of Stochastic Gradient Noise in Deep Neural Networks.]
2. If the method used in the experiments is SPAM with the sparse momentum approach, according to Algorithm 1, when m and v are set to zero, some weights are not updated, similar to dropout. It’s unclear whether the performance improvement is due to this or the actual spike gradient clipping.

### Soundness
3

### Presentation
3

### Contribution
3
