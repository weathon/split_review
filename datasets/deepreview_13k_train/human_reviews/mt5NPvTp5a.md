# Improved Operator Learning by Orthogonal Attention

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
This work presents orthogonal attention for constructing neural operators to serve as surrogates to model the solutions of a family of Partial Differential Equations (PDEs). 
The motivation is that the kernel integral operator, which is usually at the core of neural operators, can be reformulated with orthonormal eigenfunctions. 
Inspired by the success of the neural approximation of eigenfunctions~\cite{deng2022neuralef}, we opt to directly parameterize the involved eigenfunctions with flexible neural networks (NNs), based on which the input function is then transformed by the rule of kernel integral. 
Surprisingly, the resulting NN module bears a striking resemblance to regular attention mechanisms, albeit without softmax. 
Instead, it incorporates an orthogonalization operation that provides regularization during model training and helps mitigate overfitting, particularly in scenarios with limited data availability. 
In practice, the orthogonalization operation can be implemented with minimal additional overheads.
Experiments on six standard neural operator benchmark datasets comprising both regular and irregular geometries show that our method can outperform competing baselines with decent margins.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
the paper proposed a novel network architecture for neural operators that solve PDEs. The proposed architecture incorporates an orthogonal attention mechanism to alleviate the potential overfitting issues, and improve the generalization of the operator for solving PDEs. The demonstration of the effectiveness in the experimental section is clear, and the ablation study highlights the positive contribution of the proposed orthogonal attention mechanism.

### Strengths
1. a novel attention mechanism is proposed to address the issue of overfitting, and the experimental sections show improvement over the existing attention mechanisms.

2. the ablation study compares the proposed orthogonal attention mechanism to other normalization schemes, and shows the advantages of the proposed mechanism.

3. scaling up the neural network with the proposed orthogonal attention mechanism brings in performance improvement, which shows that the proposed mechanism improves generalization of neural networks with various sizes.

### Weaknesses
1. I understand the motivation that the top line in figure 1 updates the PDE solution so that strong regularization is needed, and that is why the proposed orthogonal attention is incorporated, along with linear attention. However, technically, both the top line and the bottom line are simply nonlinear functions, so have the authors tried to incorporate the proposed attention into both lines to see if it further improves the generalization?

2. the current parametrization requires solving a Cholesky decomposition for each batch of the data during training, and I wonder whether there could be ways to simplify the process. For example, could we fix the orthonormal matrix before training, and learn mu as a function of the input data? in that way, we could avoid taking the inverse of a whole matrix each iteration but rather taking the inverse of individual values in mu.

### Questions
n/a

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel neural operator architecture called Orthogonal Neural Operator (ONO) for solving partial differential equations (PDEs).
The key idea is to introduce an orthogonal attention mechanism that provides inherent regularization to combat overfitting when training on limited PDE data from classical numerical solvers.
The orthogonal attention is motivated by representing the kernel integral operator for PDE solutions using orthonormal eigenfunctions based on Mercer's theorem.
This eigendecomposition perspective allows defining a parameterized attention-like module with orthogonal regularization on the features.
Specifically, ONO consists of two pathways - one pathway uses neural networks to extract expressive features that approximate eigenfunctions, while the other pathway updates the PDE solution states based on the orthogonal attention.
The orthogonal attention first projects the eigenfunction-like features to an orthonormal space and then performs linear attention weighted by eigenvalues to update the solution states.
The orthogonalization acts as regularization and is implemented efficiently using the covariance matrix and its Cholesky decomposition.
The experiments are conducted on 6 benchmark datasets with regular and irregular geometries.
The empirical evaluations validate the effectiveness of the proposed technique over competitive baselines.

### Strengths
- This work proposes a novel orthogonal attention mechanism for neural operators that provides inherent regularization. The connection to eigendecomposition of the kernel operator is an original perspective. The authors introduces a two-pathway architecture with eigenfunction approximation and orthogonal attention-based solution update. The disentangled design is innovative.
- Orthogonal regularization through orthogonalization of features is an interesting way to mitigate overfitting in neural operators.
- The results demonstrate ONO achieves competitive performance by reducing the prediction error substantially compared to prior neural operator methods like FNO, Geo-FNO, LSM, etc. Further analysis shows ONO generalizes remarkably better than baselines for zero-shot super-resolution and predicting unseen time intervals. Ablation studies verify that the orthogonal attention is crucial to the performance gains.
- Broad applicability to diverse PDEs with different geometries highlights the potential of the idea.

### Weaknesses
 - The motivation of avoiding overfitting with regularization is reasonable, but the paper lacks experiments that directly demonstrate overfitting issues in baseline models to substantiate the need for orthogonal regularization. Adding such empirical analysis could strengthen the motivation.
- While the eigendecomposition perspective provides insights, the connection to eigenfunctions is mainly conceptual. More theoretical analysis that formally relates the orthogonal attention to spectral properties could enhance the rigor.
- The ablation study verifies the usefulness of the orthogonalization component. However, it does not isolate the impact of the two-pathway architecture itself. Additional experiments are needed to demonstrate the benefits of the disentangled design.
- The long-term impact could be boosted by testing on real-world datasets and problems beyond standard benchmarks to showcase effectiveness in complex practical settings. The paper could also provide a more comprehensive evaluation of the model's performance across a broader spectrum of PDEs, including those with more complex boundary conditions and non-linearities. This would not only demonstrate the robustness of the model but also identify potential limitations in its current form.

### Questions
Please see above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper has proposed a new attention method to improve the generalization ability of neural operators for PDE.

### Strengths
1. The method is easy to understand with some theory backup.
2. The method has shown improved performance across many datasets.

### Weaknesses
1. It is unclear how to justify that the method mitigates the overfitting problem, which is one of the central claims of the paper. Specifically, the paper does not provide a clear definition of what constitutes overfitting in the context of neural operators for PDEs. The paper should clarify whether overfitting refers to poor generalization to unseen initial conditions, or to a specific type of error in the solution space. Furthermore, the paper should include a quantitative measure of overfitting, such as the gap between training and validation error, to support the claim that the proposed method reduces overfitting.
2. The impact of the method versus the models' size should be studied more rigorously. The paper should include experiments that systematically vary the model size (both width and depth) and demonstrate how the proposed method's performance changes relative to baseline models. It is not sufficient to simply show that the model improves with size; the key is to understand if the proposed method provides a benefit at different model sizes, and if this benefit saturates or diminishes with increased capacity. The paper needs to provide more evidence that the method's performance gains are not merely a result of increased model capacity.

### Questions
1. what are the performance versus model sizes?
2. how do you measure the overfitting?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes an attention based operator learning method, where the features are orthonormalized at each layer. The orthonormalized features imply a trainable kernel and also act as a built-in regularization mechanism that aims to improve the generalization and prevent overfitting.

### Strengths
The paper is overall well-written and focuses on the important problem of generalization and overfitting in operator learning. The theoretical build-up is insightful and the experiments show promising results, although some details are lacking.

### Weaknesses
- The model complexity is not completely clear. As pointed out by the authors, the Cholesky decomposition and also inverting the matrix $L$ are computationally expensive. While this complexity depends on the dimension $k$ of $\hat{g}_i$, the choice of $k$ is not clear in the experiments. The paper mentions that the *width* in the experiments refers to the size of $d$ in $h_i^l$s, but it does not specify how $k$ relates to $d$ or the overall model width. A more precise explanation of the relationship between $k$, $d$, and the width parameter would be beneficial. Furthermore, the computational cost of the orthonormalization process should be analyzed in more detail, particularly in comparison to the baseline methods.
- While the paper tries to address the overfitting with limited data, the experimental results concerning the dataset size are limited to only one dataset and one baseline method. A similar comparison with other methods, and if possible, with DeepONet, would help understanding the data efficiency and generalization power of these methods better. The current analysis lacks sufficient breadth to fully support the claims about improved generalization and data efficiency. Expanding the experiments to include more datasets and baselines would strengthen the paper's conclusions.

### Questions
1. I would like to see more details and clarifications regarding the choices made for hyperparameters in the experiments, such as the size of $k$ and $d'$. 
2. A per-epoch runtime comparison with other methods would also help clarify the model complexity.
3. I am wondering whether multi-head attention can be naturally applied in the Orthogonal Attention blocks and if the authors have considered or tried that.
4. Right before Equation 6, the non-linearity is said to come after the residual connections and FFN. However, Equation 6 doesn't explicitly apply $\sigma$. Does that mean that $\sigma$ is built into the last layer of the FFN? If so, since the FFN is said to serve as the projection $\mathcal{P}$ to the solutions in the last layer, are the last layer's outputs also passed to $\sigma$? Wouldn't that be troublesome for the predictions?
5. Figure 2 is a bit confusing and misleading when compared with Equation 5. A more detailed caption might help clarify the process.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
