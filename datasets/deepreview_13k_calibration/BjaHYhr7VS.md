# Not all parameters are equal: a Hessian informed differential learning rate for deep learning

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 3, 5

## Abstract
Differential learning rate (DLR), a technique that applies different learning rates (instead of a single one) to different model parameters, has been widely used in deep learning and achieved empirical success via its various forms. For example, parameter-efficient training (PET) applies zero learning rates to most parameters so as to significantly saves the computational cost; adaptive optimizers such as Adam apply the coordinate-wise learning rate to accelerate the convergence.

At the core, DLR leverages the observation that different parameters can have different loss curvature, which is hard to characterize in general. We propose the Hessian-informed differential learning rate (Hi-DLR), an efficient approach that captures the loss curvature of parameters for any model and optimizer adaptively. Given a proper grouping of parameters, we empirically demonstrate that Hi-DLR can improve the convergence by dynamically determining the learning rates during the training. Furthermore, we can quantify the influence of different parameters and freeze the less-contributing parameters, which leads to a new PET that automatically adapts to various tasks and models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The main idea of this paper is to use different learning rates for different parameter groups. This is a common knowledge among optimizer designs that for different part of the model, e.g., the weight, bias, head, norm, etc., need different learning rates, however, how to search for the best learning rates remains open. This paper proposes to use the second-order approximate of the loss function to solve for the adaptive learning rates. In addition, the second-order approximation are done by regression on random sampled directions. The proposed algorithm significantly enhances training efficiency. Moreover, the paper introduces a per-parameter influence index, which identifies the most influential parameters, facilitating more efficient parameter-specific training.

### Strengths
Well-written, the intuition of this paper is clear, if the shape of a convex optimization surface is given, we can obtain the optimal learning rates for each directions directly. This can be done on top of any gradient momentum, and preconditioning regularizations. 

Although the dimension of the parameters are large, the authors pick a few directions in the space (K directions) to get a low dimensional second-order approximation for learning rate searches.

The idea is simple but effective.

The authors also designed a per-parameter influence, that can differentiate the most influencial parameters for training. By freezing all other parameters under a PPI threshold, the authors can largely reduce the training cost of models, while preserving most of the testing accuracies.

### Weaknesses
Although everything diagonalized, the computational cost of the search is relatively high when fitting the second-order model, especially when $K$ is large. Specifically, the need to sample and evaluate the loss function along $K$ directions introduces a computational overhead that scales with the number of parameter groups. This could become a bottleneck in large-scale models or when a fine-grained grouping strategy is employed. The paper would benefit from a more rigorous analysis of the computational complexity of this step, perhaps with a theoretical bound on the number of operations as a function of $K$ and the model's dimensionality.

It seems to me that the algorithm in principle is partly based on search, that you first move towards K directions defined by the split of K parameter groups, and than decides the curvature of each direction (fit a second order function) to get a learning rate on the parameter groups. I wonder if the algorithm can actually be designed more directly, for example instead of randomly sampled $\eta$s, fix several points on K lines, and than estimate curvature, make the learning rate on a line the negative curvature, etc. A more direct approach might involve pre-computing or approximating the curvature information, potentially reducing the reliance on iterative sampling. This could be particularly beneficial in scenarios where the loss landscape exhibits certain regularities that can be exploited.

The authors discussed the empirical comparison with other adaptive learning rate algorithms like prodigy and adaptation, etc. however, they did not discuss the relationship of their adaptation with previous adaptive algorithms in principle. A more thorough theoretical comparison with existing methods, such as Adam, would strengthen the paper. This could involve analyzing the convergence properties of the proposed method in relation to these established optimizers, or highlighting the specific scenarios where the proposed approach offers a distinct advantage. It would also be valuable to clarify how the proposed method interacts with the momentum and adaptive learning rate schedules commonly used in optimizers like Adam. Specifically, understanding whether these components are orthogonal or if there are potential synergies or conflicts would be crucial for practitioners.

$d_k$ is used both as an update direction, and as a notation of dimensionality in your paper.

In Equation (3.1), and when fitting the quadratic function, are you using the gradient calculations, or the corrected gradients like the momentum gradients in Adam? Does that mean second order Taylor expansion on any direction? It would be better if the authors could discuss how does their adaptive gradient interact with Adam's momentum, and adaptive schedule. Are they completely orthogonal, or how they influence each other?

For LoRA, the optimal learning rates ratios for matrix A and B can be fixed [1]. How does your schedule interact with this ratio? If $\lambda$ is fixed, then your algorithm cannot work further on Lora+?

### Questions
$d_k$ is used both as an update direction, and as a notation of dimensionality in your paper.

In Equation (3.1), and when fitting the quadratic function, are you using the gradient calculations, or the corrected gradients like the momentum gradients in Adam? Does that mean second order Taylor expansion on any direction? It would be better if the authors could discuss how does their adaptive gradient interact with Adam's momentum, and adaptive schedule. Are they completely orthogonal, or how they influence each other?

For LoRA, the optimal learning rates ratios for matrix A and B can be fixed (Hayou et al., 2024) . How does your schedule interact with this ratio? If $\lambda$ is fixed, then your algorithm cannot work further on Lora+?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a novel method called Hessian-informed Differential Learning Rate (Hi-DLR) to optimize the training of neural networks by adapting learning rates based on the curvature of the loss function, which enhances convergence across various tasks. It highlights the limitations of existing Parameter-Efficient Tuning (PET) methods, demonstrating that no single PET method is universally effective, as performance varies significantly with different datasets and model architectures. The authors propose a flexible, model-agnostic meta-framework that adaptively selects the most effective PET methods and parameter groups based on their Per-Parameter Influence (PPI) during training.

### Strengths
The paper presents the Hessian-informed Differential Learning Rate (Hi-DLR) method, which enriches the approximation of Hessian information to leverage the varying loss curvature of different parameters through adaptive learning rates, enhancing the training efficiency of deep learning models .

The authors propose an efficient algorithm for computing Hi-DLR, incorporating a novel diagonalization technique that significantly reduces computational costs while effectively separating the contributions of different parameter groups, thus facilitating faster training without sacrificing performance .

The paper introduces a flexible, model-agnostic meta-framework for Parameter-Efficient Tuning (PET) that utilizes per-parameter influence to dynamically select trainable parameters. This adaptive approach allows for improved performance across various tasks and models, addressing the limitations of existing PET methods

### Weaknesses
1. This method includes other time-consuming steps and is incomplete without measurement. Under the same conditions, would a standard AdamW approach achieve a similar result?


2.The effectiveness of Hi-DLR depends on appropriate parameter grouping; suboptimal groupings can lead to less effective learning rate adjustments, potentially hindering performance. In the paper, parameter groups are adjusted manually, which requires explanation. Additionally, for large models, the hyperparameter K warrants further discussion.

3.When group number K is a large number, the update period will increase as its learning rate update every \phi iterations, which might influence the convergence.

### Questions
Could the authors provide the source code for reproduction?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes Hessian informed differential learning rates for deep learning, which is derived based on the second-order Taylor approximation of the loss function. Experiments on synthetic data and real data are conducted to demonstrate the effectiveness of the proposed learning rates.

### Strengths
1. The authors conducted extensive experiments covering multiple different settings, from synthetic data and toy objective functions to various advanced practical learning tasks.

### Weaknesses
### weaknesses:
 1. The novelty of the proposed method is questionable. The idea bears a strong resemblance to the derivation of Newton's method, particularly in its use of a second-order Taylor approximation. Furthermore, approximating the Hessian with a diagonal matrix is not a new concept. For instance, a similar approach is taken in [1]. This raises concerns about the originality and potential impact of the proposed learning rates.

2. The logic behind integrating the proposed learning rates with AdamW is unclear. The derivation of the learning rates is based on equations (2.1) and (2.3), where the vector $\mathbf{d}$ in (2.1) is substituted with $ \boldsymbol{\eta}\_\{[K]} \mathbf{g}\_\{[K]}^{\mathrm{optim}} $. However, if these learning rates are intended for use with AdamW, it would be more logical to set $\mathbf{d}$ in (2.1) to the actual difference between iterates in AdamW, thereby incorporating the entry-wise adaptive learning rates inherent to AdamW. The notation $ \mathbf{g}\_\{[K]}^{\mathrm{optim}} $ also lacks a clear explanation. A more detailed explanation of how the proposed method integrates with AdamW is needed.

3. The paper lacks sufficient experimental details to ensure reproducibility. While some details are provided in the appendix, they are insufficient. For example, there is no information regarding the training of the ViT. Crucial details such as whether data augmentation was used, the batch size for training ViT, the specific version of ViT used across different datasets (e.g., classifier type, dimensions of heads, use of dropout, number of patches per image), are missing. The absence of code further hinders reproducibility.

4. The paper primarily focuses on applying the proposed learning rates to fine-tuning for relatively large models. It is important to evaluate the performance of the proposed method during pre-training as well. Including experiments on pre-training models like ViTs would provide a more comprehensive understanding of the method's effectiveness.

5. The paper's presentation requires significant improvement. Several notations and experimental setups are not clearly explained. Moreover, the paper lacks a well-structured introduction section that provides context and motivation for the proposed method.

### Questions
I suggest that the authors should respond to the weaknesses pointed out above.

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
3

### Summary
This paper proposes a differential learning rate strategy called Hi-DLR. The algorithmic novelty of Hi-DLR lies in diagonalizing the Hessian matrix $H$ and extending the first-order approximation of $\mathbf{G}_t^{\top} \mathbf{g}_t^{\text{optim}} / \left(\mathbf{g}_t^{\text{optim}}\right)^{\top} \mathbf{H}_t \mathbf{g}_t^{\text{optim}}$ from [1] from ULR to Differential Learning Rate (DLR). The authors also adopt a per-parameter influence derived from Hi-ULR to select influential parameters for parameter-efficient training. From the reviewer's perspective, this definition of parameter influence is novel, although it is the optimal solution of equation 3.1 with a diagonalized version of the Hessian matrix. The reviewers welcome discussions with other reviewers and the Area Chair to determine if this definition of influence demonstrates conceptual novelty.

[1] Automatic gradient descent with generalized Newton’s method. arXiv, 2024.

### Strengths
- The paper is well-motivated and designed to create suitable learning rates for different parameters.
- The authors also provide applications of the proposed Hi-DLR to NAM and LoRA.
- The per-parameter influence metric is interesting.

### Weaknesses
 **Evaluation of Hi-DLR**: All training loss figures in this paper are plotted with respect to iterations (e.g., Figures 4 and 5). Could the authors provide wall-clock time comparisons between Hi-DLR and baseline methods, in addition to the iteration-based plots. This would help demonstrate whether Hi-DLR provides real-world speedups. The current iteration-based plots do not fully capture the practical trade-offs, especially given the computational overhead of diagonalizing the Hessian. A more thorough analysis should include a breakdown of the time spent on different parts of the algorithm, such as the Hessian computation and the parameter updates, to better understand the bottlenecks and potential for optimization. Without this, it's difficult to assess the practical applicability of Hi-DLR in resource-constrained environments.



### Questions
The authors state that they consistently observe existing PET methods selecting highly influential parameters, which have approximately ($10^4 \times$ ) higher PPI than the majority of model parameters. Why is this the case? The PPI metric is an estimation of parameter influence, so what is the corresponding ground truth for parameter influence? Without ground truth, how can we be certain that PET methods have indeed selected the highly influential parameters?

### Soundness
2

### Presentation
3

### Contribution
2
