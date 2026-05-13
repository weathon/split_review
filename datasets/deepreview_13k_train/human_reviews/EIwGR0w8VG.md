# Scalable Approximate Message Passing for Bayesian Neural Networks

- Decision: Reject
- Scores: 3, 6, 6

## Abstract
Bayesian neural networks (BNNs) offer the potential for reliable uncertainty quantification and interpretability, which are critical for trustworthy AI in high-stakes domains. However, existing methods often struggle with issues such as overconfidence, hyperparameter sensitivity, and posterior collapse, leaving room for alternative approaches. In this work, we advance message passing (MP) for BNNs and present a novel framework that models the predictive posterior as a factor graph. To the best of our knowledge, our framework is the first MP method that handles convolutional neural networks and avoids double-counting training data, a limitation of previous MP methods that causes overconfidence. We evaluate our approach on CIFAR-10 with a convolutional neural network of roughly 890k parameters and find that it can compete with the SOTA baselines AdamW and IVON, even having an edge in terms of calibration. On synthetic data, we validate the uncertainty estimates and observe a strong correlation (0.9) between posterior credible intervals and its probability of covering the true data-generating function outside the training range. While our method scales to an MLP with 5.6 million parameters, further improvements are necessary to match the scale and performance of state-of-the-art variational inference methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
They propose a scalable message-passing framework for Bayesian neural networks and derive message equations for various factors, which can benefit factor graph modeling across domains. The method is applied for both CNNs and FCNs on MNIST.

### Strengths
- Good contribution for the message passing community and especially the experiments on CNNs.

### Weaknesses
 - The writeup in overall is difficult to follow and the motivation of the work is not clear.
- Poor experimental evaluation, especially since the method is tested only against synthetic data and MNIST. It should be tested on bigger models than LeNet (which is quite outdated), and it should also be tested against CIFAR-10 which is a common benchmark on BNNs. The lack of evaluation on a more complex dataset makes it difficult to assess the practical applicability of the proposed method. The experiments also lack a comparison with other established Bayesian neural network training methods, making it hard to determine the relative advantages and disadvantages of the proposed approach.
- All of the proofs are in the Appendix. I would suggest to squeeze something in the main text since there is still space in page 10. Probably the main proof of global minimization objective?

### Questions
My main question is why have you not evaluated the proposed approach on CIFAR10 and you evaluated only against MNIST? MNIST is considered as a toy dataset so we do not know if your method generalizes in bigger models even though you scaled the MLP model on MNIST. In the current state the paper is not strongly either theoretically or experimental and therefore it needs more revisions.


Misc: line 178 "predictionsfor" -> "predictions for"

### Soundness
3

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
2

### Summary
This paper introduces a scalable message-passing (MP) framework for Bayesian neural networks (BNNs), aiming to improve uncertainty quantification in deep learning models. BNNs are known for their potential in high-stakes domains due to their ability to capture predictive uncertainty. Traditional methods, like variational inference (VI), struggle with overconfidence and hyperparameter sensitivity, prompting the development of this MP framework. The authors’ approach utilizes factor graphs to model the predictive posterior, demonstrating that this avoids common issues like double-counting training data, which leads to overconfidence in other MP methods. Their implementation shows better calibration and out-of-distribution detection than standard SGD, particularly in data-constrained settings.

### Strengths
* The MP approach achieves superior calibration and out-of-distribution detection, crucial for applications in high-stakes domains where understanding model uncertainty is vital.
* The method shows competitive accuracy, especially in scenarios with limited data, outperforming standard approaches like SGD on tasks with restricted data availability.
* This framework is the first to apply message passing effectively to convolutional neural networks, marking a significant advancement over previous MP implementations. It opens up a relatively unexplored branch which is very important for the advancement of the field.

### Weaknesses
 * The MP method is computationally demanding, resulting in slower training times compared to standard approaches such as SGD and VI. The method needs substantial memory, especially during training, making it challenging to apply to memory-intensive tasks or very large networks without further optimization. Specifically, the message passing requires storing and updating messages for each edge in the factor graph, which can become prohibitive for large networks with many connections. This is further exacerbated by the need to compute gradients through the message passing steps, adding to the computational overhead.
* Although it scales better than prior MP methods, the approach still lags behind VI in handling large, complex models and datasets. The computational complexity of the message passing algorithm, even with optimizations, scales poorly with the number of parameters and data points, limiting its applicability to very large-scale problems. The authors should provide a more detailed analysis of the scaling behavior with respect to network size and dataset size.
* The method is based on some assumptions and oversimplification, such as the latent variables have a Gaussian distribution. This might not hold in complex scenarios with multimodal patterns. The assumption of Gaussianity might not be appropriate for all types of uncertainties, and the method's performance could degrade in situations where the true posterior is highly non-Gaussian. The authors should explore the sensitivity of the method to this assumption and consider alternative distributions.
* There is no proper time measurement of the method to have a crisp understanding of the computation complexity. The lack of detailed timing measurements makes it difficult to assess the practical applicability of the method. The authors should provide a breakdown of the computational cost of different parts of the algorithm, including message passing, gradient computation, and parameter updates, to better understand the bottlenecks and potential areas for optimization.

### Questions
* Would it be feasible to apply this approach to a larger network or a more challenging dataset?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper advances message passing (MP) methods for Bayesian neural networks by introducing a novel framework that models the predictive posterior as a factor graph. The key technical contribution is being the first MP method to handle convolutional neural networks while avoiding double-counting of training data, which was a key limitation of previous approaches that led to overconfidence. Their method shows particularly strong performance in data-constrained settings, achieving 94.62% accuracy on MNIST with LeNet-5 using only 640 samples (compared to 22.15% for SGD), while also demonstrating better calibration and out-of-distribution detection than standard approaches. While the method scales to networks with 5.6 million parameters and requires minimal hyperparameter tuning, it currently has higher computational overhead compared to standard training methods and has not yet matched the scale of state-of-the-art variational inference approaches. Nevertheless, the work represents an important step forward in providing more balanced uncertainty estimates, especially in scenarios with limited training data.

### Strengths
- First message passing method to handle convolutional neural networks while solving the data double-counting problem
- Exceptional performance with limited data (94.62% MNIST accuracy with 640 samples vs 22.15% for SGD)
- Better calibration and out-of-distribution detection than standard approaches
- Scales to practical network sizes (5.6M parameters) with minimal hyperparameter tuning
- Clear theoretical framework with thorough derivations and implementation details, making it reproducible

### Weaknesses
 - Significantly slower than standard training methods (96.4s vs 2.3s on GPU for LeNet-5 training)
- Does not yet match the scale of state-of-the-art variational inference methods
- Limited empirical evaluation - only tested on MNIST and synthetic data, lacking results on more complex datasets
- Memory intensive during training, and requiring approximately twice the memory of standard approaches during inference.
- No comparison against other Bayesian methods like variational inference or MCMC in terms of uncertainty quality
- Limited discussion of how the approach handles different neural network architectures beyond MLPs and basic CNNs
- Does not scale to large neural networks beyond 5.6M parameters.

### Questions
- Can you provide empirical results on more complex datasets beyond MNIST (e.g., CIFAR-10, ImageNet) to better demonstrate practical applicability and scalability?
- How does your method compare to modern variational inference approaches (like VOGN or IVON) in terms of uncertainty quality, calibration, and computational costs?
- What are the key bottlenecks causing the 40x slower training time compared to SGD, and are there potential optimizations to reduce this gap?
- How does your method handle modern neural network architectures with skip connections, batch normalization, or attention mechanisms - is the factor graph framework adaptable to these components?

### Soundness
3

### Presentation
3

### Contribution
3
