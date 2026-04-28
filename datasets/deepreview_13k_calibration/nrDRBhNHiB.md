# A multiobjective continuation method to compute the regularization path of deep neural networks

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 3, 6, 3

## Abstract
Sparsity is a highly desired feature in deep neural networks (DNNs) since it ensures numerical efficiency, improves the interpretability of models (due to the smaller number of relevant features), and robustness. For linear models, it is well known that there exists a \emph{regularization path} connecting the sparsest solution in terms of the $\ell^1$ norm, i.e., zero weights and the non-regularized solution. Very recently, there was a first attempt to extend the concept of regularization paths to DNNs by means of treating the empirical loss and sparsity ($\ell^1$ norm) as two conflicting criteria and solving the resulting multiobjective optimization problem for low-dimensional DNN. However, due to the non-smoothness of the $\ell^1$ norm and the high number of parameters, this approach is not very efficient from a computational perspective for high-dimensional DNNs. To overcome this limitation, we present an algorithm that allows for the approximation of the entire Pareto front for the above-mentioned objectives in a very efficient manner for high-dimensional DNNs with millions of parameters. We present numerical examples using both deterministic and stochastic gradients. We furthermore demonstrate that knowledge of the regularization path allows for a well-generalizing network parametrization.
To the best of our knowledge, this is the first algorithm to compute the regularization path for non-convex multiobjective optimization problems (MOPs) with millions of degrees of freedom.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a multiobjective optimization method for non-smooth problem with efficient predictor and corrector step by approximation of Pareto front. It can extend the regularization paths from linear models to nonlinear high-dimensional deep learning models. The method is used to train neural network starting sparse, which can help avoid overfitting by early stop.

This is the comments from the fast reviewer.

### Strengths
Strength:
1. The idea using approximation of Pareto front to improve multiobjective optimization on non-smooth problem to extend regularization path to high-dimensional nonlinear deep learning model is interesting and effective.

2. The results shows the method can help avoid the overfitting problem and obtain models with low loss and sparsity.

3: The paper provides thorough related background information in Section 3, making it easy to follow.

4: The predictor-corrector scheme is innovative, avoiding clustering around the unregularized and very sparse solutions, in comparison with weighted sum approach.

### Weaknesses
1: You highlight the efficiency of your method in several aspects, such as reducing the computational expense by avoiding the computation of the full gradient in Section 4, and also provide your experimental settings. While your experimental settings are detailed, the inclusion of metrics on computational time, such as wall-clock time per epoch, or time to convergence, would significantly enhance the evaluation of your method's efficiency. Furthermore, a comparison of computational cost with alternative methods would be beneficial. The current analysis lacks concrete evidence to support the claim of efficiency.

2: You claim that the algorithm shows a performance that is suitable for high-dimensional learning problems, may should be supported by more results extended to deeper DNNs including non-linear layers, and more complex datasets just as you mention in Section 5. The current experiments are limited to relatively shallow networks and simple datasets. The generalization of the proposed method to more complex architectures and datasets remains unclear. It would be beneficial to see results on a more challenging benchmark, such as ImageNet or a comparable dataset with a deeper network.

3: Have you compared the performance of your method with existing regularization path generation methods? It is crucial to position your method within the existing literature by comparing it to state-of-the-art techniques for regularization path generation. A thorough comparison is needed to demonstrate the novelty and advantages of your approach.

4: One of your key merits is avoiding overfitting, and it would strengthen the claim to conduct additional experiments, such as varying the amount of training data or using different regularization techniques, to show the robustness of the method in diverse scenarios. Currently, the experimental results are insufficient to fully support this claim.

### Questions
1: You highlight the efficiency of your method in several aspects, such as reducing the computational expense by avoiding the computation of the full gradient in Section 4, and also provide your experimental settings. While your experimental settings are detailed, the inclusion of metrics on computational time would significantly enhance the evaluation of your method's efficiency.

2: You claim that the algorithm shows a performance that is suitable for high-dimensional learning problems, may should be supported by more results extended to deeper DNNs including non-linear layers, and more complex datasets just as you mention in Section 5.

3: Have you compared the performance of your method with existing regularization path generation methods?

4: One of your key merits is avoiding overfitting, and it would strengthen the claim to conduct additional experiments.

5. It seems that finding the initial point and using randomly multi-start to find components of Pareto front cost a lot. With more complex network structure, it is possible that finding the initial point be a bottleneck which is hard to accelerate.

6. With stochastic gradient, it is possible that the initial points are different between experiments. Will different initial points affect the performance or the iteration times of the algorithm?

7. What is the method to decide when should the training stop before when the slope of the Pareto front becomes too steep. In practical settings, it seems to complex and tricky to achieve the early stopping.
8. One missing related reference: DessiLBI: Exploring Structural Sparsity on Deep Network via Differential Inclusion Paths. ICML2020

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to extend the concept of regularization path from linear model to deep neural networks. In detail, the authors formulate the problem as a multi-objective composed of empirical loss as well as sparsity regularization. The authors propose an efficient approximation algorithm to recover the entire Pareto front as the regularization path. The proposed method is composed of two parts, the first part is a stochastic gradient descent combined with a proximal mapping. The other step is a multi-objective update step, which maps the solution after the gradient step back to the required Pareto set. To validate the proposed method, several experiments are conducted to validate the efficacy. In specific, the authors conduct experiments on MNIST a widely used dataset and validate the empirical Pareto front.

### Strengths
This paper proposes a novel view to solve the sparsity constrained problem in deep learning. The idea of using multi-objective to formulate the problem is novel. Additionally, an efficient predictor and corrector algorithms is proposed to find the Pareto front of the training process. The authors also put emphasis on the regularization path which can give a deeper understanding of the training process. The method is also validated with a widely used dataset.

### Weaknesses
For the topic of extending regularization path from linear model to deep learning, several references[1][2][3] are missed.For [1], it utilizes Bregman Iteration to explore sparsity when training deep neural network where regularization can be generated during the iteration.  For [2], it proposed an efficient way to generate the reguarlization path from simple to complex via exploring inverse scale space.  For [3], it extends lasso from linear model to deep neural networks, regularization path is also discussed in this paper.

In addition, could the authors further explain the benefit of finding such Pareto front during training neural networks. 

For the Multiobjective Proximal Gradient algorithm, for the setting training with only cross entropy loss, it seems that the formulation is similar to the Bregman Iteration as discussed in [4], could the authors give a further discussion?

For the experiment parts, the current experiments are not sufficient. Only showing the performance on MNIST is not persuasive. It would be better for the authors to add experiments on more datasets.

Furthermore, could the authors illustrate whether the proposed method could be used to find the Pareto front of a series of Lottery Ticket Subnetworks[5].

### Questions
Please refer to weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents a method to travel on the Pareto front for a two-objective optimization problem and shows how to apply it to compute the regularization path for deep NNs using the L1 penalty.

### Strengths
An interesting approach that seems to work well in traveling on the Pareto front.

### Weaknesses
 - The title and the paper over-claims to work on multi-objective problems, but actually the method is only for two objective problems. For more than two objectives, it seems to me that the method will not explore the entire Pareto front.
- A comparison is missing with the standard approach to obtain the regularization path that starts with no penalty and gradually increases the L1 penalty lambda and optimize the penalized loss for each value of lambda.
- The L1 penalty is known to bias the weights and prevent the model from fitting the data well. In that respect non-convex penalties such as SCAD/MSC or the L0 penalty are preferred.

### Questions
- Can the proposed method work on more than two objective functions?
- How does the method compare din computation time and accuracy with the standard approach for obtaining the regularization path described above?
- Can the proposed method work with the SCAD/MCP penalties?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies multi-objective optimization problem with $\ell_1$ regularization. The paper claims that they extend the target problem from linear to high-dimensional non-linear problems. Numerical experiments on MNIST demonstrate the efficacy of the proposed optimization schema.

### Strengths
- The paper is written well and easy to follow. 
- The target problem is important to the community.

### Weaknesses
 - Missing references.
The authors claim in introduction that `Very recently, there was a first attempt to extend the concept of regularization paths
to DNNs by means of treating the empirical loss and sparsity.`
However, dating back to 2020, the problem has been studied in OBProxSG where the multi-objective could be considered as a weighted sum of each individual target objective.

   [1] Orthant Based Proximal Stochastic Gradient Method for $\ell_1$-Regularized Optimization, 2020. 

- Experiments are not sufficient. I am concerned about the experiments. In particular, the paper studies multi-objective problems. However, in the experiment, only cross-entropy is considered as loss function. Where are other losses to form a real multi-objective problem? Meanwhile, the network and dataset are too simple to validate the efficacy. The use of a simple fully connected network on MNIST is not sufficient to demonstrate the method's applicability to high-dimensional non-linear problems, as claimed. The method's performance should be evaluated on more complex architectures and datasets to validate the claims made in the paper.

### Questions
See the weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
