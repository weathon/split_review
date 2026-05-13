# Pareto Low-Rank Adapters: Efficient Multi-Task Learning with Preferences

- Decision: Accept
- Scores: 5, 6, 5, 6

## Abstract
Dealing with multi-task trade-offs during inference can be addressed via Pareto Front Learning (PFL) methods that parameterize the Pareto Front with a single model, contrary to traditional Multi-Task Learning (MTL) approaches that optimize for a single trade-off which has to be decided prior to training. However, recent PFL methodologies suffer from limited scalability, slow convergence and excessive memory requirements compared to MTL approaches while exhibiting inconsistent mappings from preference space to objective space. In this paper, we introduce PaLoRA, a novel parameter-efficient method that augments the original model with task-specific low-rank adapters and continuously parameterizes the Pareto Front in their convex hull. Our approach dedicates the original model and the adapters towards learning general and task-specific features, respectively. Additionally, we propose a deterministic sampling schedule of preference vectors that reinforces this division of labor, enabling faster convergence and scalability to real world networks. Our experimental results show that PaLoRA outperforms MTL and PFL baselines across various datasets, scales to large networks and provides a continuous parameterization of the Pareto Front, reducing the memory overhead $\cityscapesPamalPaloraRatio-\nyuPamalPaloraRatio$ times compared with competing PFL baselines in scene understanding benchmarks.
\looseness=-1

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a new method called PaLoRA (Pareto Low-Rank Adapters) to address efficiency issues in multi-task learning. PaLoRA enhances any neural network architecture by adding task-specific low-rank adapters and continuously parameterizing the Pareto frontier within their convex hull. This approach encourages the original model and adapters to learn general features and task-specific features, respectively, thereby improving the model's flexibility and efficiency.
Additionally, the paper proposes a deterministic sampling schedule. This schedule reinforces the division of labor between tasks, accelerates convergence, and strengthens the validity of the mapping from preference vectors to the objective space. Specifically, the sampling schedule evolves over training time, gradually shifting the focus from learning general features to learning task-specific features, ensuring the effectiveness and stability of the training process.

### Strengths
1. This paper is well-organized and clearly written.
2. The idea of decouple a neural network into a general feature extrator and several task-specific low-rank adapters is reasonable.

### Weaknesses
1. The key equation (2) is quite similar to LoRA (Low-Rank Adaptation). And there are many multi-LoRA methods proposed for multi-task learning. However, the authors have missed. Please tell us the benefits of the proposed method compared with the multi-LoRA methods (e.g., [1-4]). Specifically, the paper needs to clarify how PaLoRA's approach to parameterizing the Pareto frontier differs fundamentally from simply applying multiple LoRA adapters, and if the proposed method offers any advantages in terms of training stability or convergence speed compared to these alternatives.
2. Fig.2 is difficult to understand. First, how is $\lambda$ changed over time? Second, how to judge the quality of the mappings from preference to objective space? The visualization of the sampling schedule is unclear; it needs to explicitly show how the preference vector $\lambda$ evolves during training and how this evolution leads to the desired exploration of the Pareto front. Furthermore, the paper should provide a metric or method to evaluate the quality of the mapping from preference vectors to the objective space, going beyond visual inspection.
3. For Fig.3, why are there fewer or even no compared methods in (b) and (c)? The absence of comparison methods in subplots (b) and (c) makes it difficult to assess the relative performance of PaLoRA. The paper should either include more baselines in these subplots or justify why such comparisons are not feasible or relevant. The choice of baselines should also be consistent across all subplots to ensure a fair evaluation.
4. In Table 1 and Table 2, the proposed PaLoRA performs similarly to the other MTL methods. If the main purpose is accelerating convergence and reducing the memory requirements, then, I think it should be compared with the multi-LoRA methods [1-4]. The experimental results do not clearly demonstrate the advantages of PaLoRA over existing multi-task learning methods, particularly in terms of convergence speed and memory efficiency. The paper should include a comparison with multi-LoRA methods to validate its claims, especially if the method is designed to be more efficient.
5. The effects of the hyper-parameters (e.g., $\alpha$, $r$, and $Q$) on the results are not well studied in the experiments. The paper lacks a thorough analysis of the impact of key hyperparameters on the performance of PaLoRA. A sensitivity analysis should be conducted to determine how the performance of the method varies with different values of $\alpha$, $r$, and $Q$. This analysis is crucial for understanding the robustness and generalizability of the proposed approach.

### Questions
Please see the weaknesses.

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
The paper presented a multi-task learning method using low-rank adaptors. The paper formulates the multi-task learning problem as Pareto Front Learning, where points on the Pareto Front are sampled and optimised in training. Different from previous work which uses random sampling for such point, the paper proposed to use fixed interval, sampled either evenly or using a pre-defined schedule. Across different benchmarks, the method outperforms other Pareto Front Learning methods, while sometimes underperforms conventional multi-task learning methods.

### Strengths
1. The proposed method uses low-rank adaptors to encode weight updates in multi-task learning, and is more efficient compared to previous work. Specifically, it achieves over $\times 20$ reduction of memory usage. This is particularly impactful in real-world applications, where large neural networks are typically memory-intensive and costly to scale.

2. The proposed deterministic sampling of preference, i.e., $\lambda$, seems like a notable improvement over the existing random sampling strategy. The annealing strategy is fairly well motivated. By gradually moving $\lambda$ from the centre of the simplex to the faces, the sampled point transition from general models to more task-specific ones. This was shown to increase the convergence speed and stability.

3. The paper presented fairly comprehensive experiments across multiple benchmarks and demonstrates the superior performance of the proposed method over existing PFL methods, despite the occasional lower performance compared to MTL methods. The paper also includes rich visualisations that very well illustrates the ideas behind the method and the experimental results.

### Weaknesses
1. Being able to construct a Pareto Front of models is in itself an interesting result. But what is the practical value of this? The objective of multi-task learning is to produce one model that performs well on two or more tasks. By this definition, it seems sufficient to just have one model, or rather one point on the Pareto Front. I think it will make the paper much stronger if some practicality can be demonstrated, besides the nice theoretical result. Perhaps the Pareto Front can help in OOD scenarios. For instance, after a model is trained on cityscapes for segmentation and depth estimation, when it is tested on MS COCO for segmentation, I imagine MTL methods might be less effective due to the distribution shift, but the proposed method can still adjust the coefficients/preference to the new dataset.

2. The contribution of the fixed schedule is not the most convincing. The disadvantage of random sampling according to the paper seems to be that it produces a tight cluster of sampled points. This may be related to the distribution used rather than the random sampling process. In addition, there doesn't seem to be any experiments showing the improvement of the annealed schedule compared against the even-sampling strategy.

3. The motivation of the annealed strategy seems to be mimicking the training dynamics, where the network learn generic features in early stages while specialise in later stages. I don't think this is a homogeneous behaviour across the entire model. Usually the shallow layers of model extract generic, low-level features while the deeper layers extract task-specific features. Perhaps it makes more sense to apply this annealed schedule layer wise, instead of chronologically. There is in fact an increasing body of work on multi-task learning/model merging using learned layer-wise coefficients, such as Zhang et al. (2024) and Yang et al. (2024). I think the annealed schedule will make more sense in this context.

### Questions
1. Why does PaLoRA has a memory overhead compared against the MTL baseline? If I understand this correctly, only the LoRAs are trained, albeit one for each task. But training a LoRA only costs a fraction of the memory required for fine-tuning the whole model, which is needed for MTL if I didn't misunderstand the settings.

2. For M>1, is it essentially doing gradient accumulation? Otherwise what does multiple forward passes refer to?

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
This paper proposes Pareto Low-Rank Adaptors (PaLoRA), which are claimed to address the problem of limited scalability, slow convergence, excessive memory requirements, and inconsistent mappings from preference to objective space that existed in previous methods. The goal is achieved by adding multiple task-specific low-rank adapters and optimizing the weights with Pareto Front. Experiments on multiple tasks and variant datasets show the effectiveness of the proposed method.

### Strengths
1. This paper proposes to address multi-task learning with multiple low-rank adapters equipped with Pareto Front Learning.

### Weaknesses
1. It lacks discussions between PaLoRA and MoE-like methods.
2. It lacks discussions between PaLoRA and general adaptive weight learning methods. How is PaLoRA better and why?
3. It seems that this work applies PFL on multiple Lora, any significant differences between general PFL applications?
4. Comparisons between GFLOPS/Memory/Speed with other methods at the inference stage?
5. What is "Functional Diversity" in Sec 4.2? Any definitions or quantitative evaluations?
6. Any comparisons between PaLoRA and other LoRA-using methods on multi-task learning?
7. It points out the problem of " inconsistent mappings from preference to objective space", but no experiments and explanations validate the improvements or the relationship between mapping consistency and good performance/generalization on multiple tasks.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
PaLoRA presents a method for Pareto Front Learning (PFL) with two main contributions. First, the paper adds a low-rank adapter for each task, significantly reducing the overhead of the additional parameters added to the network. Second, they perform a deterministic (either fixed or annealing) preference sampling, leading to more stable learning and faster convergence.

### Strengths
- The proposed method is more efficient regarding number of parameters, i.e., memory complexity, compared to PaMaL and outperforms it as well and they also scale up to larger number of tasks (as shown with the SARCOS).
- Interesting discussion sections that shows the efficiency of their method in converging faster and also the multiple adapters learning different tasks.

### Weaknesses
 - What happens if you train longer for the SARCOS dataset? I.e., Figure 3 (c) goes for more than 100 epochs (until convergence of each model)? How does PaLoRA compare to PaMaL?
- Have you done a ablation over different ranks for the LoRA modules? It would be great if you could report the numbers for different ranks.
- Please provide the standard deviation for the runs in Table 1 and also for the numbers for MultiMNIST (given the variance among the performances of PaLoRA on MultiMNIST and MultiMNIST-3).
- Would be great to have another dataset added to the experiments, such as  UCI Census-Income.
- Figure 3 (b) could improve and have the legends in the image.

### Questions
Please refer to the "weaknesses".

### Soundness
2

### Presentation
3

### Contribution
2
