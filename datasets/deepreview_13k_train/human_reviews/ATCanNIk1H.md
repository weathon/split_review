# Initializing the Layer-wise Learning Rate

- Decision: Reject
- Scores: 3, 3, 5

## Abstract
Weight initialization schemes have been devised with heavy emphasis in the initial training dynamics, assuming the optimizer automatically handles appropriate step sizes in prolonged training. The optimizer typically calculates the step sizes using a single, global learning rate across all parameters, focusing exclusively on the (exponentially averaged) in-training time gradient. Motivated from hierarchical structure inherent in deep networks, this work explores assigning non-adaptive layer-wise learning rates based on the differences in gradient magnitude at initialization as a practical and effective optimization strategy. The gradient magnitude used to preset the layer-wise learning rates is measured at fan-in initialization, as stable activation variance is considered a desirable property during training, and so is assumed to largely hold true in prolonged training. Experiments on convolutional and transformer architectures show the proposed layer-wise learning rate can improve training stability and convergence in image classification and autoregressive language modeling

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper addresses a vital problem of learning rate assignment in the field of optimization. The authors propose a simple yet effective method for assigning layer-wise learning rates based on variations in gradient magnitude. Experiments conducted across various model architectures demonstrate that their proposed approach significantly enhances training stability.

### Strengths
The non-adaptive layer-wise learning rate assignment method proposed in this paper is straightforward to implement, and experimental results demonstrate its effectiveness in stabilizing the training process.

### Weaknesses
 - The novelty of the proposed method is somewhat limited. The authors in [1] have highlighted that layer heterogeneity impacts learning rate assignment and have introduced a similar approach in [2]. They validate their hypothesis by analyzing the block-wise Hessian spectra of the models. However, the evidence provided in this paper to support the effectiveness of the proposed methods is primarily intuitive.
- The paper lacks a theoretical justification for the presented method, particularly in terms of convergence analysis. Additionally, since the authors assert that the proposed methods can enhance model generalization, it would be beneficial for them to conduct a basic theoretical analysis to support this claim, such as deriving improved generalization error bounds.
- The experimental section is somewhat limited. The authors could enhance their evaluation by comparing their proposed method with more cutting-edge optimizers, such as Adam-Mini [2] and Sophia [3], to assess the performance benefits and overhead associated with their approach.

### Questions
- The Lion optimizer used in the experimental part addresses the impact of gradient magnitude through the use of the sign operation. Given this, what is the rationale behind the proposed method's effectiveness in conjunction with this optimizer? Could the authors offer some theoretical justification for this phenomena?
- What is the fundamental novelty and distinction of the proposed methods' underlying motivation or theoretical foundations in comparison to previous works, such as [1], which emphasizes block-wise heterogeneous Hessian spectra, and [4], which highlights the significance of gradient magnitude in the Adam optimization algorithm?

[1] Zhang, Y., Chen, C., Ding, T., Li, Z., Sun, R., & Luo, Z. Q. (2024). Why transformers need adam: A hessian perspective. arXiv preprint arXiv:2402.16788.

[2] Zhang, Y., Chen, C., Li, Z., Ding, T., Wu, C., Ye, Y., ... & Sun, R. (2024). Adam-mini: Use fewer learning rates to gain more. arXiv preprint arXiv:2406.16793.

[3] Liu, H., Li, Z., Hall, D., Liang, P., & Ma, T. (2023). Sophia: A scalable stochastic second-order optimizer for language model pre-training. arXiv preprint arXiv:2305.14342.

[4] Kunstner, F., Chen, J., Lavington, J. W., & Schmidt, M. (2023). Noise is not the main factor behind the gap between sgd and adam on transformers, but sign descent might be. arXiv preprint arXiv:2304.13960.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper focuses on setting the static layer-wise learning rate. By conducting empirical experiments on large-scale datasets among different tasks, the authors find out that there is a trend of parameter-wise gradient during the training procedure. From this insight, the authors propose a simple method based on inverting gradient magnitude to set static learning rates per layer.

### Strengths
- The authors identify key points in their empirical observations.
- The authors combine empirical and theoretical findings from other papers to propose a simple yet effective method.
- The authors evaluate the proposed method with different model architectures.

### Weaknesses
 - The main weakness of this paper comes from the empirical study. In detail, the empirical study is potentially sensitive to the weight initialization mechanism. Therefore the obtained results are not enough to conclude the main findings of the paper. 
- This method requires several prior training steps to approximate the gradient trajectory and then calculate the static learning rate, which may increase the total training time.
- Some statements are not theoretically or empirically proven. 
- There are some points that the empirical analysis is not aligned with the justification of the proposed method.

### Questions
1. Did the authors conduct empirical studies with different weight initialization? Or can the authors provide any theoretical study to prove the finding observation?
2. Did the authors conduct an ablation test on the combination of methods with different kinds of weight initialization mechanisms?
3. Can the authors explain why the layer-wise scheme is used while the previous weigh initialization technique was not considered?
4. Can the authors provide suggestions for the number of prior training steps needed for approximating gradient trajectory theoretically?
5. The author said that “For ResNet-50, using a T of 1 instead of 5004 results in a max 11.02%, average 2.66% deviation in the assigned layer-wise learning rates, which would not significantly impact the network performance compared to other random factors.”. However, in Figure 1, the empirical study for ResNet50 is conducted for 90 epochs, which is much longer than T = 1. Can the author provide more information on this unalignment? 
6. The author said, “A setting where a smaller subset of the dataset is repeatedly iterated over can be an efficient method to check if it can learn the characteristics implicitly shared across many minibatch, at the drawback of not explicitly verifying it on the large, diverse full dataset”. Did the author experiment with large batch size and with an optimizer for large batch training (Lars [R1], Lamb [R2], etc)?

References:
- [R1]: Boris Ginsburg, Igor Gitman, Yang You. Large Batch Training of Convolutional Networks with Layer-wise Adaptive Rate Scaling. ICLR 2018
- [R2]: Yang You, Jing Li, Sashank Reddi, Jonathan Hseu, Sanjiv Kumar, Srinadh Bhojanapalli, Xiaodan Song, James Demmel, Kurt Keutzer, Cho-Jui Hsieh. Large Batch Optimization for Deep Learning: Training BERT in 76 minutes. ICLR 2020.

### Soundness
2

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
5

### Summary
This paper proposes the use of a layerwise learning rate based on the gradient magnitude at initialization. The authors claim that this rescaling of learning rate at initialization takes into account the layerwise statistics at initialization without the network undergoing any training. Then they use the optimizer to test various setting of dataset and architectures to show the efficacy of the optimizer.

### Strengths
1) The optimizer is different from adaptive step size methods like ADAM which is per-parameter based and uses the curvature statistics at every update. Their method only requires computing the learning rate normalization at initialization. 
2) Optimizers like ADAM has an additional computational and storage overhead due to updating the second order moment information whereas this work uses a static learning rate throughout. 
3) Compared to SGD, their layer-wise learning rate method is easier to converge for complicated networks on large datasets.

### Weaknesses
The authors have tried to address the motivation clearly which I highlight in the strengths but I still think it may not be enough for the following reasons:

*1) Weak motivation*

Motivating the paper as simply mitigating ADAM's computation time is not enough. ADAM computes the preconditioner based on GGN (Gauss Newton) estimate of the Hessian at every iteration. Even ADAM is far from being a Newton-like update, it still calculates the curvature at the current iterate. The proposed method in this paper does not do that. The gradient information at initialization has no information of the curvature at any point in the loss landscape (except maybe at the initialization where curvature and gradient are correlated for eg in linear models). So, the fundamental motivation for the proposed algorithm seems to be missing. Furthermore, the authors do not provide any theoretical justification for why the gradient magnitude at initialization should be a good proxy for layer-wise learning rates during the entire training process. This lack of theoretical grounding makes it difficult to understand the underlying mechanism of the proposed method and its potential limitations.

*2) No substantial improvement*

The improvement on top of SGD or ADAM-W seems to be marginal and it is uncertain that whether it is solely because of the layerwise learning rate or the interaction of this layerwise lr with other tricks such as cosine scheudling or small batch size. It's hard to justify this algorithm unless studied in isolation without any other regularization tricks. Furthermore a 0.50% or 0.96% improvement is not considered substantial since there are various sharpness regularizers like SAM or even noise injection that outperforms their base optimizers (SGD or ADAM-W) by a siginficant margin. In this context the use of such layerwise learning rate is obsolete and unnecessary in the long run. The authors should have performed a more rigorous ablation study to isolate the effect of the proposed layer-wise learning rate from other training techniques. For example, they could have compared the performance of the proposed method with and without cosine scheduling, or with different batch sizes, to better understand the contribution of each component.

*3) Typos and unclear definitions*

Is there a typo in line 10 and 11 in Algorithm-1? seems like the sum cancels out? 
I am not sure what the index t stands for in the algorithm. The authors say they use the gradient magnitude at initilaization as informaiton to scale the learning rate. If the authors are trying to denote the index t as sampling of a new minibatch, then they should use a t-depdent notation for $L$ and not just L. The current terminology is confusing. The authors use the phrase
"low learning rates are assigned to low-level layers and high learning rates to deeper, high-level layers" where it is not defined what low or high level layers mean. The authors need to provide a more precise definition of what constitutes a "low-level" and "high-level" layer, especially in the context of different network architectures. For instance, in a convolutional network, are the initial convolutional layers considered low-level, and the fully connected layers high-level? Or is it based on the depth of the network? This ambiguity makes it difficult to interpret the results and understand the practical implications of the proposed method.

*4) Lack of intuitive justification for method*

Even if there is minor improvement in certain tasks, there is no justification as to why there is an improvement. Is it possible to plot some training metrics such as sharpness and perform a correlation analysis with respect to layer-size and learning rate? Also, is it possible that scaling the learning rate based on the dimension of each layer can be used to achieve the same result?

### Questions
The authors can address the four weakness points above.

### Soundness
2

### Presentation
2

### Contribution
1
