# Data-Efficient Training by Evolved Sampling

- Decision: Reject
- Scores: 5, 5, 5, 8

## Abstract
Data selection is designed to accelerate learning with preserved performance. To achieve this, a fundamental thought is to identify informative data samples with significant contributions to the training. In this work, we propose **Evolved Sampling** (**ES**), a simple yet effective framework for *dynamic* sampling performed along the training process. This method conducts *batch* level data selection based on *differences* of historical and current losses, significantly reducing the back propagation time with modest additional overheads while maintaining the model performance. Due to its conciseness, ES is readily extensible to incorporate *set* level data selection for further training accelerations. As a plug-and-play framework, ES consistently achieves lossless training accelerations across various models (ResNet, ViT, ALBERT), datasets (CIFAR, ImageNet, GLUE), and optimizers (SGD, Adam), saving up to 40\% wall-clock time. Particularly, the improvement is more significant under the *noisy supervision* setting. When there are severe corruptions in labels, ES can obtain accuracy improvements of approximately 20\% relative to the standard batched sampling. Our results motivate further investigations on the data efficiency aspect of modern large-scale machine learning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes "Evolved Sampling" (ES), a dynamic sampling method aimed at improving data efficiency during training. The method selects informative samples based on the loss values during training using a decoupled Exponential Moving Average (EMA) scheme. This reduces the number of samples needed for backpropagation, saving up to 40% in wall-clock time while maintaining model performance. The method was tested on a thorough evaluation across many different models (ResNet, ViT, ALBERT) and datasets (CIFAR, ImageNet, GLUE).

### Strengths
- ES shows a reduction in training time without loss in performance, which is promising for computationally expensive tasks.
- The use of loss evolution for sampling is an interesting approach that addresses the shortcomings of previous static and simple dynamic sampling methods.
- The results on datasets with noisy labels are interesting.
- Evaluation is sufficiently complete.

### Weaknesses
 - Limited novelty: the paper largely builds on existing sampling concepts with incremental improvements.
- The description of the method can be simplified considerably.

- While the method helps reducing the number of backpropagation steps performed during training, it still requires feedforward running of all samples through the network, which is still computationally expensive. Indeed, while the results are positive, the measured gains are not particularly game-changing.

- Minor: I am not sure "evolved" is the right term here;  "evolved" and "ES" remind strongly of evolutionary optimization and "Evolution Strategies", which can introduce confusion.

- It would be interesting to read more about the increased robustness to label noise; I might have expected the proposed method to perform worse, since samples with wrong labels would yield higher losses (unless/until the network memorizes the whole training set).

### Questions
See Weaknesses.

### Soundness
3

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
4

### Summary
The paper introduces a method called Evolved Sampling (ES) for efficient data selection in training machine learning models. The core contribution is a dynamic sampling framework that identifies informative data samples based on the evolution of loss values throughout the training process. By adjusting the selection of data at the batch level according to changes in loss values, ES significantly reduces the required training time while maintaining model accuracy.

### Strengths
1. Novelty - The paper introduces decoupled exponential moving averages, which leverage first-order loss differences for more stable and robust sampling, effectively combining ideas from loss and gradient-based sampling with robust optimization principles.

2. Quality - The paper provides theoretical proofs and experiments across models and datasets, demonstrating consistent gains in efficiency and robustness, especially under noisy labels.

3. Writing - The paper is clearly structured, with well-organized sections and visual aids that clarify ES’s advantages over traditional methods, though some theoretical sections may be dense for general readers.

4. Relevance -  ES offers practical relevance for reducing computational costs without accuracy loss, making it impactful for both research and industry applications in large-scale ML.

### Weaknesses
1. Significance - Much of the computation cost of foundation models occurs during pre-training, which is mostly self-supervised (auto-regressive, contrastive learning, auto-encoders). All the experiments in the paper are for labeled datasets, which represent fine-tuning use cases where the computation cost is not a major concern. Thus, the significance of the method is not clearly demonstrated. The experiments do not address the core computational bottleneck in modern machine learning.

2. Scalability - The paper claims that ES has only modest overheads, but lacks an in-depth analysis of computational and memory costs associated with the decoupled EMA calculations, especially in large-scale tasks or datasets. The analysis should include a breakdown of the forward pass overhead, memory usage for storing per-sample scores, and the impact on communication costs in distributed settings.

3. Assumptions - Some assumptions in theoretical analysis may not hold in practice, e.g., smoothness of loss functions, especially for complex architectures and non-convex losses. A discussion of how the method performs when assumptions deviate from theory, or empirical analysis on non-smooth tasks, would help clarify the applicability. The paper should include experiments on tasks with highly non-convex loss landscapes, such as those found in GAN training or reinforcement learning.

4. Hyperparameter Sensitivity - Introducing 2 hyperparameters could be a major concern for the proposed method. The current analysis (Figure 5) is too limited, e.g., what's the impact of hyperparameters on efficiency? Besides, it does seem that hyperparameters introduce a large variance in performance. For fair comparisons, the cost of searching hyperparameters should also be considered in the overall task (e.g., on a smaller dataset to test hyperparameters and then apply to a large dataset.) The paper needs a more thorough hyperparameter study, including the impact of different hyperparameter values on training time and convergence speed, not just final accuracy.

5. Lack of Baselines for Noise - In the experiments on label noise, ES performs well, but the comparison is limited mainly to non-specialized sampling methods. The paper should compare against methods specifically designed for handling noisy labels, such as those using robust loss functions or label correction techniques.

nit - ES in this literature often refers to 'Evolution Strategy', so would be nice to have a different abbreviation for the proposed method.

### Questions
1. Could the authors provide more insight into the sensitivity of the hyperparameters $(\beta_1, \beta_2)$ across different datasets and architectures?

2. ES appears computationally feasible for single-machine training, but would its performance gains hold up in distributed training settings?

3. ES with Pruning (ESWP) combines batch and set-level selection, but it is not entirely clear how this combination impacts overall performance in practice.

4. How can ES be used for self-supervised training?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a novel framework called Evolved Sampling (ES) (and with Pruning ES-WP) aimed at enhancing data efficiency in machine learning. The authors propose a dynamic sampling method that selects informative data samples based on the evolution of losses during training. This approach aims to reduce backpropagation time while maintaining model performance across various architectures (ResNet, ViT, ALBERT) and datasets (CIFAR, ImageNet, GLUE). Key contributions include: (i) Dynamic Sampling: ES utilizes historical and current loss differences to inform data selection, allowing for batch-level sampling without the need for pre-trained models. (ii)Efficiency Gains: The method achieves up to 40% reduction in wall-clock time during training and shows improved accuracy (approximately 20%) in scenarios with noisy labels; and (iii) Theoretical Justifications: The authors provide theoretical insights into how their method alleviates loss oscillations and can be viewed through the lens of distributionally robust optimization.

### Strengths
### Originality:

The main proposition lies in the recursive definition of an Exponentially Moving Average over the losses of individual examples to deselect them from the training process to gain speedups and improved; i.e. stable, learning dynamics. The single-level EMA itself is a well-known approach that is applied to this setting with a recursive definition. The other techniques, i.e. annealing and pruning, are mere adaptations from prior work and are only a minor contribution to the originality. The bridge between batch and set-level data selection, which their method allows them to do is a nice feature, but not the main contribution. The theoretic analysis is interesting overall. But insights like decoupled EMA is in fact a convolution over hyperparameters’ powers of historical losses – so their results are not really surprising.

### Quality: 

Quite a few experimental issues are present, which I will detail in the weaknesses section.

### Clarity:

Overall the paper is clearly and concisely written. With the main exception of when exactly we are collecting the loss values of pruned examples; which might bias the calculation of their weight.

### Significance: 

The efficiency of modern machine learning algorithms and neural networks is a great issue, as it results in huge energy demand. Reducing the footprint is a critical point. One angle of attack pursued in this paper is being selective about the order and the subset of consumed examples. This is indeed an important and interesting avenue.

### Weaknesses
Besides the weak overall originality, my main criticism is connected to the empirical evaluation:

The necessity for a burn-in period, where standard training must occur to initialize the loss adequately before applying the Exponential Moving Average (EMA) scheme, points to a limitation in the approach. This dependency on a specific loss initialization suggests that the method might not be entirely robust across various starting conditions. It would benefit the study to explore a more systematic ablation of this burn-in period as a hyperparameter. Additionally, understanding whether variations in the burn-in length affect performance could provide insight into the model's dependency on initialization stability and might even reveal opportunities to shorten or eliminate this requirement.

Another area where clarity is needed is the reporting of statistical measures. The number of seeds used for evaluation and averaging remains unspecified, and no standard deviations are provided. This omission raises questions about whether noise rather than true performance gains might influence observed differences in performance between the proposed method and baseline competitors. Including standard deviations would allow readers to assess the consistency of the results, providing a clearer understanding of the variability in performance.

The use of wall-clock time as a measure of speedup also presents challenges. Since wall-clock time is influenced by multiple factors, including the specific point of reference and the extent to which reference performance is met or exceeded, this metric is not straightforward. No details are provided on the variability of wall-clock measurements, which could make these results more challenging to interpret. An additional, complementary metric—such as the number of examples seen (similar to token counts in LLM training)—could yield a more direct and comparable measurement of processing efficiency, especially since the baseline approach involves higher computational requirements.

Regarding robustness to label noise, Figure 3a indicates that while the method outperforms the baseline, the speedup advantage is lost under noisy conditions. This finding implies that the method may benefit from integrating the baseline up to its peak performance before switching to the proposed scheme. Such a hybrid approach could potentially leverage the best of both methods, maintaining efficiency without sacrificing performance under challenging conditions.

In Figure 3b, the gradients under comparison lack clarity. It is uncertain whether the gradients displayed encompass all examples (both corrupted and uncorrupted), necessitating additional forward passes and potentially affecting wall-clock measurements, or if the results only include corrupted examples selected by the method. The latter case would introduce a selection bias, affecting the integrity of the reported results. A more informative and balanced approach would be to calculate the proportion of non-informative examples selected per epoch, providing a relative measure of their influence on learning. This would give a clearer picture of how these less useful samples affect training efficiency and could allow for more balanced comparisons.

In Table 5, the ground-truth results are presented without a corresponding baseline for corruption-free performance. Including such a baseline would clarify the upper bound achievable in the absence of noise, providing a benchmark against which the "superior" performance in noisy conditions could be assessed.

Further minor Issues:

* Ablations:
  * choices of \beta. The presented heatmap tables are way too broad. I suggest using some Sobol or Latin Hypercube design and then reporting the heat surfaces. This way, we get a far more fine-grained perspective on the hyperparameters’ behavior.
  * Pruning is not ablated
* The notation 0^+ and 1^- should probably be introduced or replaced by intervals (0, 1) instead of [0, 1]
* The notation is at times slightly overburdened (e.g. the additional vector notation in 320), instead of just writing the actual values in there directly.

### Questions
I would like to get a clarification regarding Eq. 3.8. We have access to the current loss of an example to decide whether or not we want to sample it for that epoch. I interpret this as doing the forward pass on an example that we later deselect to be part of the backward pass calculation. This means that we still maintain the gradient of that example until we deselect it. The main cost saved then is the amount of bwd passes. In Algorithm 1, the necessity for forward passes seems to be mitigated in Line 284 at least during the pruning by taking the historically weighed score s instead of the weight function. This seemingly implies that to select examples, only historic losses are considered. But this poses yet another question: How do we adjust an example’s loss if the example is no longer selected? Because then we yet again will need a fwd pass and we could have calculated the full weight. This seems to be what is done in 289; i.e. only the loss over the batch examples is calculated. The only thing to mitigate the issue of disregarding bad losses (almost) completely is in Remark 1 and discounting the existing values. Either way, this introduces non-trivial and dead-lock-ish dynamics I would like to see investigated.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper functions as a well-thought-out "momentum optimizer" in the data space. Instead of considering the presentation of data as fixed as in SGD, we take a more expansive view and think of the data space as another component of the model to optimize.

The work is somewhat novel in the large model training space.

### Strengths
The paper builds upon good theoretical foundations.

The paper well cites related work and the literature that leads to this contribution.

The paper creates an efficient heuristic based approach to solve a practical problem which rests on the previous theoretical contributions.

The paper well considers ablation studies and robustness studies.

The paper's theoretical arguments are well constructed.

### Weaknesses
This should be better justified: This can be inefficient since different samples may have varied importance. Can you look at the influence functions or coresets literature?

This statement needs to be better motivated and explained, why is evolved sampling "natural?" In general machine learning tasks, the typical behaviors of loss curves often appear decent trends
overall, but can oscillate meanwhile due to certain noises. This introduces the sensitivity or instability
issue of the sampling scheme (3.6). A natural smoothing operation is to use the exponential moving
average (EMA) of losses

The proof presentations are somewhat lacking. It's difficult for me to quickly match up concepts from the optimization literature to some of the theoretical arguments made, for example, the EMA to the minimax problem.

It may be worthwhile in explaining this better with regards to the control theory literature, specifically, control theory also deals with oscillations and rectifies them in similar manners:

Decoupled EMA. To sufficiently leverage the loss dynamics in a more robust sense, we propose to
calculate the sampling probability as
pi(t) ∝ wi(t) = β1si(t − 1) + (1 − β1)ℓi(θ(t)),
si(t) = β2si(t − 1) + (1 − β2)ℓi(θ(t)), si(0) = 1/n (3.8)
with β1, β2 ∈ [0, 1] as two hyper-parameters. Here, the intermediate series {si(t)}t∈N, updated in
the EMA scheme, is also referred as the score (for the i-th sample). The scheme (3.8) is the so-called
decoupled EMA,
2 which reduces to (3.7) when β1 = β2 = β. In Figure 1, it is shown by the red curve
and appears an “interpolation” between the original loss and single EMA: When losses oscillate,
the decoupled EMA reacts moderately by not only capturing detailed dynamics of losses, but also
remaining necessary robustness , exhibiting the flexibility to trade-off (by tuning two betas).
Intuitively, by setting (β1, β2) → (0+, 1
−), we are able to exploit the long-term historical information
along the training (via β2), while focusing on the importance of current losses (via β1) and thus can
get the best of both world. This simple and elegant design turns out to be surprisingly beneficial in
practice, which is further verified in numerous experiments in Section 4.


This should really be better explained. Again, this paper is moving into the "total optimization landscape" where both data and model parameters are considered components of the system to be optimized. It's not immediately clear whether this is a consequence of the problem the authors were solving, or the key insight that led to the approach.

(ii) ES to solve a DRO problem. From another perspective, ES can be also reformulated as a
solution to the minimax problem...

### Questions
Can the key idea of the paper: optimization of the data space, be more cohesively or clearly presented? Currently, it's still difficult to understand the key idea of the paper without significant theoretical and literature knowledge.

### Soundness
3

### Presentation
4

### Contribution
2
