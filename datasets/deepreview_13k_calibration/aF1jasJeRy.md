# Torque-Aware Momentum

- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 3, 5

## Abstract
Efficiently exploring complex loss landscapes is key to the performance of deep neural networks. While momentum-based optimizers are widely used in state-of-the-art setups, classical momentum can still struggle with large, misaligned gradients, leading to oscillations. To address this,  we propose Torque-Aware Momentum (TAM), which introduces a damping factor based on the angle between the new gradients and previous momentum, stabilizing the update direction during training. Empirical results show that TAM, which can be combined with both SGD and Adam, enhances exploration, handles distribution shifts more effectively,  and improves generalization performance across various tasks, including image classification and large language model fine-tuning, when compared to classical momentum-based optimizers.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes Torque-Aware Momentum (TAM), an improvement to traditional momentum-based optimizers, designed to handle large, misaligned gradients that may lead to oscillations and hinder convergence in DL. Through incorporating a damping factor adjusting the momentum update based on the alignment angle between current gradients and prior momentum, TAM aims to make the training stable, improve generalization ability, and increase exploration of the loss landscape. The proposed approach is evaluated over a range of tasks which include image classification, LLM fine-tuning, and online learning, indicating consistent improvements over standard momentum-based methods such as  SGDM.

### Strengths
1. The paper proposes an innovative concept via connecting damping mechanics to momentum updates, which adds an insightful dimension to the optimization community in ML.
2. The paper is equipped with detailed empirical analysis, which includes the comparisons over a variety of benchmarks and model types, highlighting the robustness and wide applicability of TAM proposed.
3. The concept of incorporating a damping factor contigent on gradient alignment is well-explained, and the pseudo-code presented contributes to clarifying implementation.

### Weaknesses
1. Despite the fact that TAM is computationally efficient, the requirement to compute the cosine similarity between gradients and momentum might introduce non-trivial implementation complexity in certain training frameworks. Specifically, while the dot product itself is efficient, the need to normalize both the gradient and momentum vectors before computing the cosine similarity could add overhead, especially when dealing with high-dimensional parameter spaces. This normalization step, involving square root and division operations, might not be negligible in resource-constrained environments or when using specialized hardware.
2. While comparisons with the standard optimizers and a few existing approachs are robust, additional benchmarks against more recent optimizers concentrating on gradient stability would strengthen the claims furthermore. For example, optimizers that explicitly address issues like exploding or vanishing gradients, or those that incorporate adaptive learning rates based on gradient statistics, would provide a more comprehensive comparison. Evaluating against methods designed for non-convex optimization landscapes would also be beneficial.
3. The paper illustrates TAM's effectiveness on various tasks, but its performance in more demanding and complex training scenarios, such as very large LLMs (e.g., 70B), could be further explored. The behavior of TAM in extremely high-dimensional parameter spaces and with the complex loss landscapes typical of very large models remains unclear. It is important to understand how the damping factor interacts with the intricate dynamics of these models, and whether it can consistently prevent oscillations and improve convergence in such scenarios.

### Questions
Would TAM still perform well in non-stationary environments, such as continual learning, where the gradient directions frequently change or shift?

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
4

### Summary
1. Summary	This paper is based on the idea that rapid changes in gradients (torque) negatively impact the performance of deep learning models. It attempts to improve the generalization performance of optimizers that utilize momentum (e.g., SGDM or Adam) by applying a damping effect during momentum updates, which is based on the angle between the gradient and momentum. The author devised a variation of SGDM called TAM and a variation of Adam(W), referred to as AdaTAM(W), and trained deep learning models on various datasets and tasks. Additionally, the author demonstrated the performance of the TAM approach in online learning. In the ResNet18 and CIFAR10 environments, the author showed that TAM exhibits less oscillation compared to SGDM.

### Strengths
1. A damping effect was applied based on the cosine similarity, which intuitively illustrates the relationship between gradients and momentum.
2. The experiments conducted on the Language Model (LM) side involved a diverse range of datasets.
3. The small change in gradient norm on the CIFAR10 dataset suggests that TAM has some effect in mitigating oscillations.

### Weaknesses
1. Throughout the paper, TAM and AdaTAM(W) are evaluated using a limited set of models, raising questions about whether the TAM approach works only with specific models. For instance, in the image domain, only ResNet-based models were used, while in the language model (LM) domain, only BERT-based models were employed. It is recommended to use other models in the image domain, such as MobileNet and ViT, and in the language domain, models like GPT, T5, and LLaMA.
2. In Table 1, the performance of TAM on the ImageNet dataset is quite marginal, with only a 0.1%-point difference when comparing SGDM and TAM (77.0 vs. 77.1). This is also the case when comparing Adam and AdaTAM (74.4 vs. 74.5. Since the aim of the method is to improve generalization performance, one would expect a more significant performance difference, especially on large datasets like ImageNet.
3. While it is impressive that TAM exhibits less oscillation compared to SGDM in Figure 6, the relationship between AdaTAM and Adam is not shown. To convincingly demonstrate that the proposed damping is indeed effective, it would be beneficial to include graphs obtained from AdaTAM as well.
4. In Figure 4, the threshold for similarity is set at 1%-point, which is a large value and could lead to the conclusion that they are not similar. It is recommended to lower the threshold for similarity to around 0.2%-point.
5. There is no convergence proof for TAM and AdaTAM. Since optimizers are techniques used in artificial intelligence training, it is essential to demonstrate that the models converge when these methods are applied. It is recommended to at least provide mathematical proof showing that the proposed optimizers converge in a convex environment. The convergence of Adam has already been proven, and several other optimizer papers have provided similar proofs (e.g., AMSGrad, AdaMax, SGDM).

### Questions
1. Why does TAM diverge at epoch 0 in the middle figure of Figure 6?
2. In the Methods section, gamma is fixed, but what is the effect of varying gamma on performance? An ablation study on this would be helpful. It would be useful to understand how performance changes with hyperparameters, as seen in Adam.
3. In the case of Adam, an exponential moving average is used to update momentum; why is this not done in AdaTAM?
4. Only the fine-tuning results for the Language Model (LM) are presented, but there are no results for training from scratch. I am curious about how performance would change if the TAM approach were used from the pre-training stage of the LM.
5. Figure 6 presents results for CIFAR10, but it is difficult to validate the performance of TAM using CIFAR10 alone. Are there graphs for more complex datasets, such as CIFAR100, which has a greater number of classes?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper identified the problem of momentum that large and misaligned gradients can lead to oscillations during training of DNNs. Thus, it proposed a novel momentum method called Torque-Aware Momentum (TAM), which introduces a damping factor based on the angle between the new gradients and previous momentum, stabilizing the update direction during training. The experiments demonstrate the effectiveness of TAM.

### Strengths
-As Momentum is a very important technique for optimization and deep learning, it is always interesting to see a novel and effective mometum method, such as TAM.

-The experiments cover both vision tasks and language tasks.   

-The idea of TAM is elegant and reasonable.

### Weaknesses
-This paper lacks convergence analysis. As a optimization method, the convergence guarantee is expected. And many previous studies on momentum provided convergence analysis.

-While large oscillations are bad, oscillations are sometimes good for searching minima intuitively. This paper also failed to formally explain the generalization advantage of TAM over standard momentum. Generalization bound analysis can be helpful.

-The empirical improvements are marginal, especially for vision tasks. The experiments of language modeling are also not compressive.

-The work missed a lot recent relevant works on analyzing or upgrading momentum. For example, [1,2] theoretically studied various momentum methods; [3, 4] designed momentum variants.

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
