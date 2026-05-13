# Early Neuron Alignment in Two-layer ReLU Networks with Small Initialization

- Decision: Accept
- Scores: 8, 5, 8, 5

## Abstract
This paper studies the problem of training a two-layer ReLU network for binary classification using gradient flow with small initialization. We consider a training dataset with well-separated input vectors: Any pair of input data with the same label are positively correlated, and any pair with different labels are negatively correlated. Our analysis shows that, during the early phase of training, neurons in the first layer try to align with either the positive data or the negative data, depending on its corresponding weight on the second layer. A careful analysis of the neurons' directional dynamics allows us to provide an $\mathcal{O}(\frac{\log n}{\sqrt{\mu}})$ upper bound on the time it takes for all neurons to achieve good alignment with the input data, where $n$ is the number of data points and $\mu$ measures how well the data are separated. After the early alignment phase, the loss converges to zero at a $\mathcal{O}(\frac{1}{t})$ rate, and the weight matrix on the first layer is approximately low-rank. Numerical experiments on the MNIST dataset illustrate our theoretical findings.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the problem of training a two-layer ReLU network classifier via gradient flow under small initialization. Training dataset assumes well-separated input vectors. Analysis of the neurons’ directional dynamics establishes an upper bound on the time it takes for all neurons to achieve good alignment with the input data. Numerical experiment on the MNIST dataset validate the theoretical findings.

### Strengths
+ Interesting alignment behavior of the gradient flow for training two-layer ReLU networks under small initialization and separable data
+ Rate analysis for the after-alignment-phase convergence

### Weaknesses
 - The results only hold for correlated data.
- Only ReLU activation functions are analyzed.
- Some of the results have been previously known or observed, e.g., the solution of (stochastic) gradient flow finds in training two-layer ReLU networks on separable data is (almost) low-rank.
- How small the initialization shall be to ensure the two-phase convergence is not qualitiatively discussed?

### Questions
1) Do the results/analysis extend to other activation functions? 
2) How small the initialization shall be to ensure the two-phase convergence? In general, since the training is nonconvex even with correlated/separable data due to the nonlinear relu activation function in the los. SGD/GD converges to a local minimum and indeed, this has been observed and numerically validated in the literature; see also [R1] Brutzkus et al. 2018. SGD learns over-parameterized networks that provably generalize on linearly separable data. ICLR. [R2] Wang et al. 2019. Learning ReLU networks on linearly separable data: Algorithm, optimality, and generalization. IEEE TSP. In [R1], SDG for two-layer ReLU networks under separable data converges to local minimum; yet for leaky ReLU networks, it finds global minimum. In [R2], it also shows that plain SGD on ReLU networks using separable data converges to local minimum numerically. Yet, a bit modification on the SGD helps SGD converge to a global minimum but with random initialization. It would be great if a comparison can be made between the approach in [R2] and the small-initialization SGD for training two-layer ReLU networks on e.g., MINIST. Moreover, is there any transition for such initialization value to go from the two-phase to single-phase gradient flow convergence to local minimum?
3) It would be great if more numerical tests are provided to demonstrate the two-phase convergence and provide the plots. 
4) If the second-layer weights are initialized not in a balanced manner (although not initialized according to (3)), I understand it would also work and guess that the imbalance between positive v_j and negative v_j values only influences the time it takes for the two-phases. More balanced initalization, faster convergence. It would be interesting to numerically validate if this is the case. 
5) There are some grammar issues and typos. Please correct.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the problem of training a two-layer ReLU network for binary
classification using gradient flow with small initialization on well-separated input datasets, i.e. datasets $(x_i, y_i)_{i \in [n]}$ with $ \min \frac{\langle x_iy_i, x_jy_j  \rangle}{\Vert x_i \Vert_2 \Vert x_j \Vert_2 } \geq \mu$.
They show that in time $O(\frac{\log(n)}{\sqrt{\mu}})$ all neurons are well aligned with the input data, which means that positive neurons show in the same direction as the positively labeled points (or have a negative scalar prouct with all vectors of the dataset) (and an equivalent result for negative neurons).
Furhter they show that after the early alignment phase, the loss converges to zero at a $O(1/t)$ rate, and the weight
matrix on the first layer is approximately low-rank. Numerical experiments are provided.

### Strengths
All claims are proven and illustrations are supporting the explanations.

### Weaknesses
The assumption that the dataset is well seperated is very strong. I don't see why one would use a neural network on such a dataset rather than linear regression. The core issue is that the theoretical analysis relies on a strong separability condition, which limits the practical relevance of the results. While the paper provides a detailed analysis of the training dynamics under this assumption, it does not address the more common scenario where data is only approximately separable or has more complex decision boundaries. The analysis does not provide insights into how the network would behave when the data is not perfectly separable, which is a crucial aspect for understanding the practical applicability of the results. Furthermore, the paper does not explore the behavior of the network when the data is noisy or contains outliers, which are common in real-world datasets.

### Questions
-

### Soundness
3 good

### Presentation
4 excellent

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper improves on previous theoretical analysis of the early alignement phase of the neurons of a shllow neural network initialized with small weights. This allows them to prove quantitative bounds in terms of the initialization scale, time, number of neurons and number of datapoints required to guarantee convergence.

### Strengths
The paper is easy to follow and explains well the previous issues and how they are solved. It is nice that the results apply to deterministic initialization of the weights, and do not require a random initialization (though they can of course be applied to this case).

### Weaknesses
The assumption of positively correlated labels and balancedness are very strong, and usually are not true in practice. The requirement for positively correlated labels is particularly limiting, as it implies that the classes are not only separable but also that the feature representations of different classes tend to point in similar directions in the feature space. This is a very strong constraint that is unlikely to hold in real-world datasets, where classes are often designed to be as discriminative as possible, leading to feature representations that are orthogonal or even anti-correlated. The balancedness assumption, while less restrictive, still poses a challenge as real-world datasets often exhibit significant class imbalance, which can affect the dynamics of the early alignment phase. Furthermore, the paper does not provide a clear explanation of how these assumptions interact with the derived bounds, making it difficult to assess the practical relevance of the theoretical results.

### Questions
The description of Assumption 2 before the statement of the assumption does not match the statement of the assumption.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the learning dynamics in the special case of two-layer ReLU neural network with small initialization.

### Strengths
The results of this paper extend prior results from infinitesimal initialization to finitely small initialization.

The relation and difference with prior results are clearly presented. The paper is clearly written and easy to follow. The figures are helpful for understanding the argument.

### Weaknesses
 The setting of the neural network is unconventional. It requires the second layer weights to depend on the first layer weights in a way as shown in Eq.(3), instead of independently initialized.  This setting is used neither in practice nor in most theoretical analysis. According to the analysis,  I doubt that the results of this paper hold without this restriction on the second layer weights.

> The paper has some discussion on this setting. However, it does not justify the validity of this setting. That it is commonly assumed in other papers does not directly justify. I would like to see some analysis, or at least some intuition, on why the results would hold on the natural setting.

The assumption on the data (Assumption 1) is strong, as it is not met by almost all real data. 

The significance of the results is limited, as it is an extension of similar results from $\epsilon \to 0$ to the finite but small $\epsilon$.

 In Eq.(5), why the R.H.S. is independent of the network output $f(x_i)$? Or, why there is no such term $y_i-f(x_i)$ which usually appears in the expression of gradients.

### Questions
In Eq.(5), why the R.H.S. is independent of the network output $f(x_i)$? Or, why there is no such term $y_i-f(x_i)$ which usually appears in the expression of gradients.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
