# Predictive Differential Training Guided by Training Dynamics

- Decision: Reject
- Scores: 6, 6, 5, 5

## Abstract
This paper centers around a novel concept proposed recently by researchers from the control community where the training process of a deep neural network can be considered a nonlinear dynamical system acting upon the high-dimensional weight space. Koopman operator theory, a data-driven dynamical system analysis framework, can then be deployed to discover the otherwise non-intuitive training dynamics. Taking advantage of the predictive power of the Koopman operator theory, the time-consuming Stochastic Gradient Descent ( SGD) iterations can be bypassed by directly predicting network weights a few epochs later. This novel predictive training framework, however, often suffers from gradient explosion especially for more extensive and complex models. In this paper, we incorporate the idea of differential learning, where different parts of the network can undergo different learning rates during training, into the predictive training framework and propose the so-called "predictive differential training'' (PDT) to sustain robust performance for accelerated learning even for complex network structures. The key contribution is the design of an effective masking strategy based on Koopman analysis of training dynamics of each parameter in order to select the subset of parameters that exhibits "good'' prediction performance. PDT also includes the design of an acceleration scheduler to keep track of the prediction error so that the training process can roll back to the traditional GD-based approaches to "correct'' deviations  from off-predictions. We demonstrate that PDT can be seamlessly integrated as a plug-in with existing optimizers, including, for example, SGD, momentum, and Adam. The experimental results have shown consistent performance improvement in terms of faster convergence, lower training/testing loss, and fewer number of epochs to achieve the best loss of Baseline.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a Koopman operator based method to predict intermediate weight updates in SGD training runs. The authors present empirical evidence showing faster convergence with their proposed method. The main contributions compared to prior work are I) in adding a masking step that updates only parameters with good predictions from the Koopman operator and ii) a schedule to switch between Koopman based prediction and regular SGD updates.

### Strengths
The method descriptions are very clear and the paper is well written.

### Weaknesses
Two main concerns:

1. The main concern for the proposed method is the computational complexity of the method and the per FLOP gain. Since  $h$ has to be considerably small to minimize costs of approximating the Koopman operator, the per FLOP gain is not completely clear in the experimental results. Would the authors be able to provide Fig 5 with x-axis as the training FLOPs? What is the per FLOP generalization performance gain?

2. What is the difference between the proposed method and the DMD based method in [https://arxiv.org/pdf/2006.14371]? How would they compare?

Additional:
What is the variance between the Koopman and SGD training runs? E.g., Figure 5(d), the difference between AdamW and PDT looks considerably minimal, I wonder whether they are within the randomness between different SGD runs.

### Questions
From Fig 9, it is observable that PDT is sensitive to the scheduling hyperparameters. What is the variance in these runs? Also from Fig 9 c it seems that for most of the prediction starting points, the difference between SGD and PDT is negligible. Does that mean that the benefit of PDT is mostly in the starting epochs (around epoch 7 when the red line diverges)? This also indicates that the optimal pred starting epoch needs to be exhaustively searched to obtain benefits through PDT.

It might also be worth studying the training dynamics effect not only on the loss but properties of the learned function, e.g., sharpness/smoothness or grokking? [https://arxiv.org/pdf/2402.15555], [https://arxiv.org/pdf/2010.01412]

Can fig 2 be combined in one plot with solid and dashed line for SGD and PDT? Also what is the effect of the width of the network? How do different optimizers compare for the same network width-depth. How sensitive is it to the learning rates?

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
4

### Summary
- This paper introduces a Koopman operator-based method, called Predictive Differential Training (PDT), which uses an adaptive mask to enhance and accelerate training dynamics. The authors empirically demonstrate that PDT can achieve performance improvements and faster convergence.

### Strengths
- This paper is well-written and presents a compelling approach to addressing the gradient explosion issue in Koopman-based methods.
- The authors empirically validate their method across various network architectures on CIFAR-10 and ImageNet, providing support for its effectiveness.

### Weaknesses
- The accuracy of recovering an approximated Koopman operator, as I understand, is influenced by (i) the noise amplitude (stochasticity) in the learning dynamics and (ii) the dataset's complexity. High stochasticity can obscure deterministic trends, and greater dataset complexity can impede adequate state space coverage within a few steps. These factors seem essential to comprehending the dynamics of PDT and determining the valid scope of the method. However, the paper does not fully address or justify these aspects

### Questions
### Major
- The accuracy of estimating the Koopman operator may depend on the batch size and learning rate, as these primarily influence the stochasticity of learning dynamics. I am curious whether the proposed method maintains effectiveness when using smaller batch sizes or higher learning rates

- It would be insightful to observe how the mask elements evolve during training. I expect that the number of active elements (i.e., those set to 1) might decrease over time, potentially making the "prediction" block redundant. Please clarify the scope and limitations of this method as they relate to this aspect.

- Please provide more detailed experimental information, including the hyper-parameters used in Figs. 2 and 5–8, batch size, the number of runs conducted to obtain the averaged results, and the criteria or process used for selecting these hyper-parameters. 

- I am curious about the decision to end training before loss convergence in Fig. 5. For example, in Fig. 5(b), the test accuracy on CIFAR-10 appears substantially lower than widely reported values (≥ 95%). Further clarification on this would be helpful.

### Minor
- In Eq. (2), $x_0$ should be $x_i$.
- Please correct typos in Algorithm 1.

### Soundness
2

### Presentation
2

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
This paper presents a new approach that treats deep neural network training as a nonlinear dynamical system, using Koopman operator theory to predict network weights several epochs ahead and bypass costly SGD iterations. To address issues like gradient explosion in large models, it introduces *predictive differential training* (PDT), where parts of the network learn at different rates. PDT includes a masking strategy to focus on parameters with reliable predictions and an acceleration scheduler to revert to traditional methods if needed. Compatible with optimizers like SGD and Adam, PDT demonstrates faster convergence, lower loss, and fewer epochs in experiments.

### Strengths
1. The paper's introduction is clear, and the effectiveness of the proposed algorithm is well illustrated in Figure 1. The integration of Koopman Operator Theory is smooth and accessible.

2. The understanding of the optimization method is accurate, and the motivating example in section 3.2 is clearly presented.

3. Table 1, showing runtime, is well-organized and effective for comparison.

### Weaknesses
1. The statement in section 3.3 may be inaccurate. $\mathcal{O}(N h^2)$ is indeed large, especially given the size of current deep learning models. Otherwise, methods like L-BFGS would be suitable for neural networks.

2. The experiments are limited to CIFAR-10, making it challenging to assess scalability to larger datasets. A drawback of these algorithms is that they often underperform compared to plain SGD on larger datasets.

3. What is the space complexity of the algorithm? Additionally, an ablation study on hyperparameters like batch size is missing, which is crucial for deep learning methods.

Minor Typo: Line 628 - there is "???"

### Questions
What motivates the use of the first principle? Is there any theoretical proof to support its validity? Traditional methods, such as line search, do not depend on this assumption.

Although the paper is well-written, the proposed algorithm is less convincing than expected (see previous comments). Specifically, two issues are concerning: (1) space complexity appears to be a significant problem, and (2) the experimental results are not sufficiently compelling.

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes predictive differential training (PDT) of deep neural networks based on Koopman operator theory for accelerated training. The key contribution of the paper involves designing a masking strategy that can stabilize predictive training and enable PDT to reach good network performance. PDT can be integrated within the standard stochastic gradient descent-based (SGD) iterative training where an acceleration scheduler was added to revert to SGD training based on an error in weight prediction. Experiments were presented to investigate the generalizability of PDT, and the effectiveness of the proposed masking strategy.

### Strengths
The presentation of the paper is clear. The authors provided the key background needed to understand their method. The authors presented an intuitive understanding of the method which is easy to understand. The authors provided experiments demonstrating the effectiveness of their method and ablation studies to understand the key aspects.

### Weaknesses
1.	The main weakness of the paper is the weak empirical performance of PDT. The generalizability study (Fig 5) seems to show similar performance vs SGD or Adam on the test loss and accuracy for the first three rows. The only observable gain seems to be on ImageNet-1k with VIT where it shows better accuracy over AdamW after epoch 200. Probably a table with the final accuracy by running each method should be presented.
2.	The test loss in the first two rows of Fig 5 seems to be indicating overfitting for both approaches hence the effectiveness of the method is unclear. 
3.	There are substantial details missing about how the authors have selected the hyperparameters for the baseline optimizers. In my view, the methods should be compared after running an extensive hyperparameter optimization, especially w.r.t the learning rate. The authors also did not provide ablation studies regarding changing learning rate and batch size which is directly correlated with the time taken by SGD or Adam to converge.
4.	In my view, the experimental section needs a lot of updating. I am unclear about the necessity of section 4.3 in the main paper.

### Questions
1. In Fig 5, what is the last column is it train or test accuracy? 

2. It is unclear if replication studies were performed. If yes, please include the sds.

### Soundness
2

### Presentation
2

### Contribution
2
