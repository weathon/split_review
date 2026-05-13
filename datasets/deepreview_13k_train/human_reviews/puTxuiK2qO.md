# AdaFisher: Adaptive Second Order Optimization via Fisher Information

- Decision: Accept
- Scores: 6, 5, 6, 8

## Abstract
First-order optimization methods are currently the mainstream in training deep neural networks (DNNs). Optimizers like Adam incorporate limited curvature information by employing the diagonal matrix preconditioning of the stochastic gradient during the training. Despite their widespread, second-order optimization algorithms exhibit superior convergence properties compared to their first-order counterparts e.g. Adam and SGD. However, their practicality in training DNNs are still limited due to increased per-iteration computations and suboptimal accuracy compared to the first order methods. We present AdaFisher--an adaptive second-order optimizer that leverages a block-diagonal approximation to the Fisher information matrix for adaptive gradient preconditioning. AdaFisher aims to bridge the gap between enhanced convergence capabilities and computational efficiency in second-order optimization framework for training DNNs. Despite the slow pace of second-order optimizers, we showcase that AdaFisher can be reliably adopted for image classification, language modelling and stand out for its stability and robustness in hyperparameter tuning. We demonstrate that AdaFisher outperforms the SOTA optimizers in terms of both accuracy and convergence speed.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a new idea: using Kronecker factored preconditioners, with diagonal factors. The Kronecker product approximates empirical Fisher information matrix. The method demonstrates better performance compared to diagonal approaches such as Adam.

### Strengths
1. Kronecker factored preconditioner with diagonal factors hasn't been used with empirical Fisher matrix before. 
2. Thorough experimentation.

### Weaknesses
1. The preconditioner still requires layer inputs and gradients backpropaged through the layer, which is not always feasible for large training systems. 
2. The Adafactor already uses Kronecker factored preconditioner with diagonal factors. There is no comparison against Adafactor. 
3. sub-optimal regret bound $O(\log(T)\sqrt{T})$, compared to Shampoo - which is optimal $O(\sqrt{T})$.
4. There are low rank approaches with similar complexity as proposed methods  such as EVA [1]. There should be comparison against EVA.

### Questions
Does your shampoo baseline use grafting? 
CASPR is another paper which uses Kronecker sum based approach, what are your thoughts on Kronecker sum based combination to approximate empirical Fisher information matrix.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The authors use the Fisher information matrix as a precondition matrix to obtain a second order optimizer. They also provided some analysis and numerical results for the method. 

My concern is that this method is too similar to a previous method "Kronecker-Factored Second-Order Optimizers Perform First-Order Descent on Neurons" by Frederik Benzing.

### Strengths
Using the Fisher imformation matrix as a precondition is really a good point.

### Weaknesses
It seems that the author didn't realize a previous work "Kronecker-Factored Second-Order Optimizers Perform First-Order Descent on Neurons" by Frederik Benzing, which is very similar to this work. The core idea of using the Fisher information matrix (FIM) for preconditioning is not novel, and the specific approximation used here, while computationally efficient, needs more justification regarding its impact on the quality of the preconditioning. The empirical results focus heavily on generalization, but the computational cost of the proposed method is not clearly addressed. The authors should provide a more detailed analysis of the trade-off between computational overhead and performance gains, especially in comparison to first-order methods like SGD and Adam.

### Questions
1. The authors should specify the difference of the current work to the previous work "Kronecker-Factored Second-Order Optimizers Perform First-Order Descent on Neurons" by Frederik Benzing.

2. Empirically, the high-order optimizers are computationally more expensive than first order optimizers for each step and also have poorer generalizability. It is somehow strange that the numerical results in this work didn't show how the method accelerate the training process clearly but mainly about the strength of the method in generalization. The authors should explain why the method can help in enhance the generalization significantly. They should also include results obtained with SGD, since usually the generalization ability  of SGD is better than ADAM.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This  paper  proposes  a new  second-order  optimizer,  AdaFisher,  which  ensures  better  convergence  while  maintaining  computational  efficiency.  Based  on  the  K-FAC optimizer,  AdaFisher  discovers  that  the  Kronecker  factor  is  diagonally  dominant  and  the  Fisher  information  matrix can be approximated  by  using  a diagonal block Kronecker approximation.  On image  classification  and  language  modeling  tasks,  AdaFisher  achieves  better  results  than  other  second-order  optimization  methods when applying Wall-Clock-Time method (training  for  the  same  amount  of  time).

### Strengths
The  paper  innovatively  discovers  that  the  Kronecker  factor  is  diagonally  dominant  and  proposes  a diagonal  block-Kronecker  approximation  for  the  FIM. The  resulting  AdaFisher  optimizer  shows  good  performance.  And the  paper  is  well-organized  and  easy to follow.

### Weaknesses
Please  refer  to  Questions.

- In Section  2,  it  is  stated  that  $F_i = \cal{H_{i-1}} \otimes \cal{S_{i}}$, but  in  the  algorithm  implementation,  it  becomes  $F_i = \cal{H_{i}} \otimes \cal{S_{i}}$. Why  is  this  the  case?
- Why are two parameters, $\gamma_1$ and $\gamma_2$, introduced for calculating the exponential moving averages of $\cal{H}$ and $\cal{S}$ in the AdaFisher optimizer? Would it not suffice to introduce only one parameter?
- It is known that the SGD optimizer performs better than the Adam optimizer in image classification tasks. Why is there no comparison with SGD?
- The experimental section compares performance under the same computation time. Could you provide a performance comparison under the same number of epochs? I suspect that second-order optimizers like AdaHessian may not have converged yet. When all optimizers have converged, does AdaFisher still outperform other second-order optimizers?
- The AdaFisher optimizer introduces two parameters, $\gamma_1$ and $\gamma_2$. I see that the authors conducted extensive searches for these parameters. Could you provide the values of $\gamma_1$ and $\gamma_2$ used in different tasks for the AdaFisher optimizer? If these parameters also require extensive searching to achieve good performance, then the AdaFisher optimizer might be very limited.

### Questions
- In Section  2,  it  is  stated  that  $F_i = \cal{H_{i-1}} \otimes \cal{S_{i}}$, but  in  the  algorithm  implementation,  it  becomes  $F_i = \cal{H_{i}} \otimes \cal{S_{i}}$. Why  is  this  the  case?
- Why are two parameters, $\gamma_1$ and $\gamma_2$, introduced for calculating the exponential moving averages of $\cal{H}$ and $\cal{S}$ in the AdaFisher optimizer? Would it not suffice to introduce only one parameter?
- It is known that the SGD optimizer performs better than the Adam optimizer in image classification tasks. Why is there no comparison with SGD?
- The experimental section compares performance under the same computation time. Could you provide a performance comparison under the same number of epochs? I suspect that second-order optimizers like AdaHessian may not have converged yet. When all optimizers have converged, does AdaFisher still outperform other second-order optimizers?
- The AdaFisher optimizer introduces two parameters, $\gamma_1$ and $\gamma_2$. I see that the authors conducted extensive searches for these parameters. Could you provide the values of $\gamma_1$ and $\gamma_2$ used in different tasks for the AdaFisher optimizer? If these parameters also require extensive searching to achieve good performance, then the AdaFisher optimizer might be very limited.

I'm willing to improve my score if you address my concerns.

### Soundness
3

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
3

### Summary
The authors introduce **AdaFisher**, a novel adaptive second-order optimizer that uses a block-diagonal approximation of the Fisher Information Matrix (FIM) to improve both convergence speed and computational efficiency in second-order optimization. The paper aims to address the limitations of current second-order methods, such as high computational costs and poor generalization, by proposing a diagonal block-Kronecker approximation of the FIM. The authors demonstrate that AdaFisher outperforms several SOTA optimizers on tasks such as image classification and language modeling.

### Strengths
1. **Novel methodology:** The introduction of a diagonal block-Kronecker approximation applicable to various layers offers an interesting balance between computational efficiency and the use of curvature information typically employed in second-order optimization. 

2. **Empirical results:** The paper provides comprehensive experimental evidence showing that AdaFisher outperforms baseline methods (Adam, K-FAC, AdaHessian, etc.) on benchmark datasets such as CIFAR-10, CIFAR-100, ImageNet, and WikiText-2 across different network architectures.

3. **Stability:** AdaFisher shows strong stability across varying learning rates and batch sizes, reducing the need for extensive hyperparameter tuning, which is a common challenge when training deep models.

4. **Theoretical contribution:** The paper presents a rigorous theoretical convergence analysis for both convex and non-convex cases, asserting a convergence rate of  $O(\log T / \sqrt{T})$ , similar to Adam-type methods. The derivation of the update rules using the diagonal approximation of the FIM is clearly explained.

### Weaknesses
 1. The paper considers nonconvex optimization, but in reality DNNs are **nonsmooth**, due to operations such as ReLU and max-pooling. It would be valuable to discuss this limitation in Section 3.4. 

 2. **Hyperparameter tuning:** It is unclear how many epochs were used for hyperparameter tuning, especially in grid search experiments (Appendix D). Providing more details on the tuning process would enhance the reproducibility of the results.

 3. **Comparision with AdamW:** AdamW has become the most widely used optimizer due to its improved handling of weight decay. It would have been interesting to compare AdamW directly with AdaFisherW. (in particular, for image classification).

### Questions
1.	**Figure 1:**  I try reproducing Figure 1 using your code. In my experiments, AdaFisher did not consistently converge to similar local minima across multiple runs. Could you discuss the sensitivity to initialization or provide further insights?

2.	**Algorithm 1:** How did you choose the values for $\gamma_1$ and $\gamma_2$? You mentioned that “the decay factors $\gamma_1$ and $\gamma_2$ for AdaFisher were tuned within $\(\{0.1, 0.2, \dots, 0.9, 0.99\}\)$, but you did not specify which values were  used. Providing these details would help practitioners apply AdaFisher effectively.

3.	**Related work:** The paper does not mention some other recent second-order optimizers (e.g., Sophia, INNA, etc.), which could be relevant in the context of adaptive second-order methods. Including these in the discussion would provide a more comprehensive overview of related work. 

4.	**Table 3:** I was surprised by the Top-1 accuracy of Adam for ResNet50 on ImageNet. Could you clarify which hyperparameters were used for Adam in this experiment?

### Soundness
3

### Presentation
3

### Contribution
3
