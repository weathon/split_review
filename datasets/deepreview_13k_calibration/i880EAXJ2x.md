# Robust Training of Neural Networks at Arbitrary Precision and Sparsity

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3

## Abstract
The discontinuous operations inherent in quantization and sparsification introduce obstacles to backpropagation. This is particularly challenging when training deep neural networks in ultra-low precision and sparse regimes. We propose a novel, robust, and universal solution: a denoising affine transform that stabilizes training under these challenging conditions. By formulating quantization and sparsification as perturbations during training, we derive a perturbation-resilient approach based on ridge regression. Our solution employs a piecewise constant backbone model to ensure a performance lower bound and features an inherent noise reduction mechanism to mitigate perturbation-induced corruption. This formulation allows existing models to be trained at arbitrarily low precision and sparsity levels with off-the-shelf recipes. Furthermore, our method provides a novel perspective on training temporal binary neural networks, contributing to ongoing efforts to narrow the gap between artificial and biological neural networks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a universal framework for training neural networks at arbitrary precision and sparsity by treating quantization and sparsification as perturbations and applying a denoising affine transform to stabilize training. The method is compatible with standard architectures and recipes, achieving competitive results on ResNet-50 and Transformer models at low precision. It provides theoretical grounding through ridge regression and introduces efficient matrix multiplication for quantized models.

### Strengths
- A unified framework that applies to both quantization and sparsification.
- Denoising affine transform for training stability is novel. By framing quantization as a perturbation and introducing a controlled denoising mechanism, the authors provide a theoretically grounded way to mitigate the instability associated with ultra-low precision training.
- A solid mathematical foundation, especially in using ridge regression to stabilize training; analysis of the parameter sensitivity; shortcut for quantized matrix multiplication and the sub-channel quantization.
- Compatibility with standard architectures and training methods, which makes the approach practical.
- Competitive performance on ResNet-50 and Transformer, better results than the baselines (including the full precision training).

### Weaknesses
 - The proposed denoising technique is applied to both quantization and sparsification, but sparsity deserves special attention. Sparsity has unique challenges, such as gradient instability and poor convergence behavior in sparse regimes. By framing sparsification as a perturbation, the method simplifies the impact of sparsity on training. Sparse models typically exhibit unique instability issues, such as dead weights that don’t recover during training. The paper does not address how the proposed denoising affine transform could prevent or manage this issue. More dedicated experiments and ablations would be helpful to understand the unique contribution of the proposed solution to sparse training. The BLEU scores provided in Tab 6 are insufficient to validate the claim that the proposed approach robustly supports sparse training across different tasks and architectures. The method’s utility in extreme sparsity settings, such as >90%, is not tested.
- Certain layers, like the first and last layers or specific convolutional layers, may require lower sparsity levels / higher precision than intermediate layers due to their critical role in feature extraction and final prediction. The paper does not discuss how the proposed approach could be adapted to handle these layer-specific sparsity requirements, which are essential for maintaining performance.
- How does this approach work in the fine-tuning settings, where small shifts in weights might accumulate errors?
- The authors demonstrate results on ResNet-50 and Transformer models, without testing across a broader range of architectures, such as MobileNet and EfficientNet, which are widely used in low-power / mobile applications. Also consider providing performance results on architectures that have very different structural and computational properties, eg RNNs.

### Questions
See weaknesses above.

### Soundness
2

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
3

### Summary
The paper introduce an affine transform scheme for the quantization and sparsification of neural networks.

### Strengths
The paper proposes a novel affine transform to perform dequantization step of quantizer by solving a regularized least squares problem with respect to the scaling factor.

### Weaknesses
1. The authors appear to overstate their contributions. The primary challenge in training quantized neural networks is addressing the zero-gradient issue associated with discrete loss functions. However, if I understand correctly, the main contribution here is a de-quantization scheme used to compute the scaling factor for the quantizer, which does not directly address the zero gradient issue as what straight-through estimator does. The paper does not clearly articulate how the proposed affine transform addresses the fundamental challenge of non-differentiability in quantization, which is typically handled by techniques like the straight-through estimator or other gradient approximation methods. The paper's focus on a dequantization step seems orthogonal to the core problem of gradient propagation through discrete operations.

2. In the Abstract, it is stated that "Our solution employs a piecewise constant backbone model to ensure a performance lower bound and features an inherent noise reduction mechanism to mitigate perturbation-induced corruption." Could you clarify what the "piecewise constant backbone model" and the "performance lower bound" refer to specifically? I was unable to find details on these terms in the main text. The description of the piecewise constant backbone and its role in establishing a performance lower bound is vague. The paper lacks a clear mathematical definition or explanation of how this backbone is constructed and how it guarantees a performance floor. The connection between the piecewise constant structure and noise reduction is also not well-explained.

3. It is unclear whether the authors used quantization-aware training or post-training quantization in the experiments. Could you please clarify?

4. All experiments are conducted for group-wise quantization. To better demonstrate the advantages of the proposed method, I recommend including results for channel-wise quantization as well as testing on a broader range of neural architectures, such as vision transformers and MobileNet. The exclusive use of group-wise quantization limits the generalizability of the results. Channel-wise quantization is a common and often more effective approach, and the absence of results for this method raises questions about the versatility of the proposed technique. Furthermore, the lack of experiments on modern architectures like vision transformers and MobileNet makes it difficult to assess the method's performance in state-of-the-art scenarios.

5. It would be beneficial to provide more technical details on how this method is extend to sparsification. The paper lacks sufficient technical detail on how the proposed affine transform is adapted for sparsification. The connection between the dequantization approach and the process of setting weights to zero or other values is not clearly explained. The method's application to structured sparsity, in particular, needs further elaboration.

### Questions
1. What is the 'Flax framework'?

### Soundness
2

### Presentation
2

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
This paper proposes a denoising affine transformation that stabilizes training under these conditions. It introduces perturbation modeling and noise reduction strategies using a piecewise constant backbone model, which ensures performance stability across varying precisions and sparsities.

### Strengths
1. The approach achieves state-of-the-art results with models trained at very low precisions, demonstrating robustness and effectiveness.
2. Demonstrated effectiveness on both ResNet and Transformer architectures across multiple datasets, suggesting that the method is adaptable to a variety of deep learning tasks.

### Weaknesses
1. In Eq (1), $\epsilon$ is not defined. How do you choose it?
2. In line 162, why do you use $\delta_i$ instead of $\delta$? Is it a typo?
3. Run-time analysis is missing. This is important for low-precision networks.
4. Actual running memory consumption is missing. This is important for low-precision networks.
5. The added denoising transformation and affine operations might introduce computational overhead, especially in cases where ridge regression is used for reconstruction, possibly slowing down training on certain hardware.

### Questions
1. In Table 8, why there is a NaN when $\lambda=0$?
2. It is surprising that your A4W4 results are better than A32W32 results in tables 1/2/3. (Low-precision training is better than the conventional float32-precision training). Can you please make an explanation? Usually, low-precision computation reduces the accuracy during the inference.
3. How is your method's actual running memory consumption and run-time compared to other methods?

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
2

### Summary
This work proposes a denoising affine transform method for quantization and sparsification of deep learning. This is based on ridge regression between the original vector and its quantization, which reconstructs the original signal. The proposed method enables us to train deep nets with ultra-low precision and high sparsity levels. In particular, it provides training on temporal binary networks, which has been considered challenging in previous works.

### Strengths
- The proposed method is quite simple and implementation-friendly. It can potentially be combined with various other architectures and  algorithms.

- It empirically works even for high quantization cases such as A1W1.

### Weaknesses
 **Lack of Comparative Experimental Validation**  

The paper demonstrates the behavior of the proposed method through various experiments, but it barely shows how much better it is compared to existing methods. Starting from Table 2, the experiments only present results in terms of accuracy, with very little insight into the stability of the learning process, leaving only the final accuracy for comparison. In particular:  
- Tables 2 and 4 seem to compare results, but only for the A4W4 case, where the precision is not extremely low. Moreover, the difference in accuracy with existing methods seems negligible although there is no standard deviation provided and its significance is unclear.  As long as  the metric of performance is limited to the test accuracy, I must say that the contribution is minimal.  
- The comparison for ultra-low precision (A1W1) is limited to a single cell in Table 5.

Thus, while the method's functionality is evident, it is unclear in what aspects it excels.

As I am not an expert in quantization, I cannot make a definitive judgment, but it seems that there is little prior research on precision lower than A4W4. If this is true, then the main claim of the paper should not be the proposal of a method, but rather the experimental validation at precision levels lower than A4W4, which has rarely been tested before. The paper claims state-of-the-art performance in line 94, but if there are no previous studies, it would be more appropriate to describe the setup as novel.  

Furthermore, without a comprehensive evaluation of factors beyond accuracy, such as the stability against hyperparameters (e.g., learning rate), changes in training time, and memory efficiency, it seems difficult to demonstrate the advantages of the proposed method.

**Ambiguous and Inaccurate Mathematical Expressions**  
The readability is low, and I do not believe it is at a level suitable for acceptance.

Line 161:  
Although I understand the actual algorithm, I believe the mathematical formulation of the perturbation is inappropriate. Specifically, the author defines $\delta$ by $\delta = \text{round}(f(x)) - f(x)$, and substituting this into eq.(2) makes $q = \text{round}(f(x))$. So, as a mathematical operation, adding $\delta$ is meaningless for $q$. In other words, rather than adding a perturbation, it simply appears to be stating $q = \text{round}(f(x))$.

eqs.(3-8):  
Clarify the dimensionality of each variable, such as $x \in \mathcal{R}^N$. It is strange that $x$ is in bold font while $b$ is in regular font, implying it is a scalar, yet the authors use $\mathbf{x} - b$, subtracting a scalar from a vector. Additionally, there is no clear definition of $\text{Cov}_{xq}$. Is this a scalar?


**Memory efficiencty**  

Compared to existing methods, is the proposed method more memory efficient? Since it introduces continuous variables $a$ and $b$, it appears that training cannot be performed on low-precision hardware alone.

### Questions
**Ambiguous and Inaccurate Mathematical Expressions**  
The readability is low, and I do not believe it is at a level suitable for acceptance.

Line 161:  
Although I understand the actual algorithm, I believe the mathematical formulation of the perturbation is inappropriate. Specifically, the author defines $\delta$ by $\delta = \text{round}(f(x)) - f(x)$, and substituting this into eq.(2) makes $q = \text{round}(f(x))$. So, as a mathematical operation, adding $\delta$ is meaningless for $q$. In other words, rather than adding a perturbation, it simply appears to be stating $q = \text{round}(f(x))$.

eqs.(3-8):  
Clarify the dimensionality of each variable, such as $x \in \mathcal{R}^N$. It is strange that $x$ is in bold font while $b$ is in regular font, implying it is a scalar, yet the authors use $\mathbf{x} - b$, subtracting a scalar from a vector. Additionally, there is no clear definition of $\text{Cov}_{xq}$. Is this a scalar?


**Memory efficiencty**  

Compared to existing methods, is the proposed method more memory efficient? Since it introduces continuous variables $a$ and $b$, it appears that training cannot be performed on low-precision hardware alone.

### Soundness
2

### Presentation
2

### Contribution
2
