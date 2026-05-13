# Improving Discrete Optimisation Via Decoupled Straight-Through Gumbel-Softmax

- Decision: Reject
- Scores: 3, 5, 6, 3

## Abstract
Discrete representations play a crucial role in many deep learning architectures, yet their non-differentiable nature poses significant challenges for gradient-based optimization. To address this issue, various gradient estimators have been developed, including the Straight-Through Gumbel-Softmax (ST-GS) estimator, which combines the Straight-Through Estimator (STE) and the Gumbel-based reparameterization trick. However, the performance of ST-GS is highly sensitive to temperature, with its selection often compromising gradient fidelity. In this work, we propose a simple yet effective extension to ST-GS by employing decoupled temperatures for forward and backward passes, which we refer to as \textit{Decoupled ST-GS}. We show that our approach significantly enhances the original ST-GS through extensive experiments across multiple tasks and datasets. We further investigate the impact of our method on gradient fidelity from multiple perspectives, including the gradient gap and the bias-variance trade-off of estimated gradients. Our findings contribute to the ongoing effort to improve discrete optimization in deep learning, offering a practical solution that balances simplicity and effectiveness.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper present a simple method, called decoupled stgs,for dealing with discrete representation. Through the employing the decoupled temperatures for forward and backward passes, the gradient estimators could be less sensitive to the temperature. The experimental results demonstrate the practical advantage.

### Strengths
The proposed approach makes use of the advantage of st-gs and ste and avoid the disadvantage of these two methods. The paper provides the simple approach that provide the two temperatures for both forward and backward passes.

### Weaknesses
However, the proposed approach lack newly estimator, even though the performance improved. The result relies on the selected parameters, which prevent the practical usages

### Questions
1 how to determine the forward and backward temperatures
2 for the modified Gumbel-SoftMax sample \hat{z}^b, its partial gradient is still approximated to one?
3 the results is sensitive to the choice of the forward and backward temperatures

### Soundness
1

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
3

### Summary
This paper strives to focus on studying the limitations of the Straight-Through Gumbel-Softmax (ST-GS) estimator, which is sensitive to temperature settings. The authors propose the Decoupled ST-GS estimator, which uses distinct temperatures for the forward and backward passes, claiming to enhance both performance and gradient fidelity. Through extensive experiments on various tasks and datasets, they demonstrate that this approach significantly improves upon the original ST-GS, offering better control over the trade-off between relaxation smoothness during inference and gradient accuracy during training.

### Strengths
1. The paper is clearly written and easy to follow.
2. The authors provide some interesting results. The experimental demonstration are in detail.

### Weaknesses
It is unfortunate that the simplicity of the proposed idea is not supported by any theoretical guarantees to validate its effectiveness. Additionally, the paper suffers from redundancy and lacks sufficient depth.

### Questions
See Weakness.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces $Decoupled ST-GS$, an extension of the Straight-Through Gumbel-Softmax (ST-GS) estimator that utilizes separate temperature parameters for forward and backward passes. This decoupling enhances control over relaxation smoothness during inference and gradient fidelity during training, addressing the limitations of the traditional ST-GS method. Through extensive experiments, the authors demonstrate that Decoupled ST-GS significantly outperforms the standard ST-GS across various tasks and datasets. Additionally, the paper analyzes its impact on gradient fidelity, providing insights into how the new approach improves optimization in discrete latent models.

### Strengths
1. The paper introduces Decoupled ST-GS, a novel extension of the Straight-Through Gumbel-Softmax estimator that allows independent control of temperature parameters for forward and backward passes, enhancing relaxation smoothness and gradient fidelity.
2. The authors demonstrate significant performance improvements over the traditional ST-GS.
3. Additionally, the paper thoroughly analyses gradient fidelity, exploring the gradient gap and bias-variance trade-off, which offers valuable insights into optimizing discrete latent models in deep learning.

### Weaknesses
Most experiments are performed on toy experiments in three small datasets: CIFAR10, SVHN, and MNIST for binary autoencoder and VAE.

### Questions
Can the author provide a comparison of MAE settings for ImageNet1k experiments? To show the methods works on more practical settings.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes an extension of the straight-through Gumbel-Softmax estimator by decoupling the temperatures for the forward and backward passes. The authors present an empirical evaluation across multiple tasks and datasets to demonstrate the advantages of the proposed method.

### Strengths
The proposed approach is simple, straightforward to implement, and the paper is clearly written.

### Weaknesses
It is unfortunate that the simplicity of the proposed idea is not supported by any theoretical guarantees to validate its effectiveness. Additionally, the paper suffers from redundancy and lacks sufficient depth.

### Questions
- It seems that the temperature should affect the smoothness of the training objective. Could you comment? If so, why was the same step size used for all temperature settings?
- How many random seeds were used for each experiment? Could you provide error bars to quantify variability?
- Your grid search suggests that the minimum validation errors occur at the boundary of the search space. Do you believe extending the grid might lead to further improvements?

### Soundness
2

### Presentation
3

### Contribution
1
