# Det-CGD: Compressed Gradient Descent with Matrix Stepsizes for Non-Convex Optimization

- Decision: Accept
- Scores: 6, 6, 3

## Abstract
This paper introduces a new method for minimizing matrix-smooth non-convex objectives through the use of novel Compressed Gradient Descent (CGD) algorithms enhanced with a matrix-valued stepsize. 
The proposed algorithms are theoretically analyzed first in the single-node and subsequently in the distributed settings. 
Our theoretical results reveal that the matrix stepsize in CGD can capture the objective's structure and lead to faster convergence compared to a scalar stepsize. 
As a byproduct of our general results, we emphasize the importance of selecting the compression mechanism and the matrix stepsize in a layer-wise manner, taking advantage of model structure. 
Moreover, we provide theoretical guarantees for free compression, by designing specific layer-wise compressors for the non-convex matrix smooth objectives. Our findings are supported with empirical evidence.\footnote{This work was supported by the KAUST Baseline Research Funding Scheme.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors present two novel matrix stepsize sketch type compression GD algorithms which are optimization algorithms based on sketch based compression gradient calculation. The authors utilize the layered structure of the sketches while designing the sketches.

### Strengths
- Matrix smoothness is leveraged to reduce distribution communication complexity. 

- layer layer-wise structure of the neural nets is utilized while designing the sketches and block diagonal smoothness is used.

-The number of bits broadcasted at each iteration are reduced without losing in the total communication complexity. (free compression)

### Weaknesses
 - Determinant normalization is not too common approach. Hence, I would appreciate some further reference, and supporting statement into why to use the normalized determinant.



### Questions
- Why did the authors first present the stochastic gradient and presented the compressed gradient as a  replacement for the stochastic gradient? Is it stochastic?
- Did the authors try some further algebraic tricks on equation 15? What is the complexity of those operations?
- What is the take home message in Figure 1, for comparison of CGD 1 and CGD2. Did the authors experiment a scenario where these two methods are performing different?

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces two new matrix stepsize sketch Compressed Gradient Descent (CGD) algorithms for minimizing matrix-smooth non-convex functions. The theoretical analysis of these algorithms extends to both single-node and distributed settings.The newly introduced matrix stepsize strategy captures the underlying structure of the objective function, and lead to faster convergence. Leveraging the block-diagonal structure within neural networks, the proposed Det-CGD algorithm outperforms classical methods.

### Strengths
S1. The authors introduce two novel matrix stepsize sketch CGD algorithms, and offer convergence guarantees for these algorithms in both single-node and distributed scenarios.

S2. Taking into account the layer-wise structure of neural networks, the authors devise efficient compression mechanisms.

S3. The author derives the expression for the optimal step size for the CGD algorithms, offering an important guideline for achieving rapid convergence.

### Weaknesses
W1. Assumption 2 is stringent and may not align well with the characteristics of neural network problems. Note that Inequality (4) in Assumption 2 is assumed to apply to the entire dataset rather than just a mini-batch.

-- Neural network problems can be viewed as high-order polynomial fitting problems that are inherently nonconvex. Inequality (4) should include not only second-order terms but also third-order and higher-order terms. Utilizing a varying matrix D^t is more effective than using a constant stepsize D to capture the curvature information of the nonconvex objective function.

-- Even though Assumption 2 holds, the authors employ a global convex majorization function in Inequality (4), which may lead to slow convergence due to its potential looseness.

W2. The authors claim that their proposed methods take advantage of the layer-wise structure of neural networks, but in the experiments, they only focus on the logistic regression problem with a non-convex regularizer. Additionally, the neural network architecture is not defined.

W3. This stepsize is the minimizer of the right-hand side of the normalization upper bound in (10) under certain conditions. It is not clear why this results in the "optimal stepsize".

W4. Solving the log-det minimization problem under the constraints specified in (21) can be challenging and impractical, particularly when the dimension $d$ is large.

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper investigates matrix step sizes of the compressed gradient descent method and provides convergence analysis.

### Strengths
The paper investigates matrix step sizes of compressed gradient descent and provides convergence analysis.

### Weaknesses
The paper claims that the matrix step size improves performance but introduces problems. The presence of the neighboring term in Theorem 3 creates a significant neighborhood when $\Delta^{inf}$ is large. This is particularly concerning as a large $\Delta^{inf}$ implies a significant deviation in the compressed gradient from the true gradient, which could lead to instability or slow convergence, especially in highly heterogeneous distributed settings. Furthermore, the analysis does not provide clear guidance on how to select $\lambda_D$ to effectively balance the convergence rate and the neighborhood size. 

This paper uses the compressed gradient as shown in (3), which is a direct compression on the full gradient. Given the prevalence of error feedback techniques in handling compression errors, it is pertinent to consider whether the proposed matrix step size can be extended to incorporate error feedback methods. The current approach, without error feedback, is susceptible to accumulating compression errors, potentially leading to a significant performance gap compared to methods that do incorporate error feedback. The lack of consideration for error feedback is a major limitation in the current formulation.

The paper does not consider the use of SGD, local update, and partial participation techniques in distributed settings. These techniques are widely used to improve scalability and reduce communication costs in distributed optimization. The absence of these considerations limits the applicability of the proposed method in practical distributed learning scenarios. 

The paper introduces det-CGD1, but it is unclear why this algorithm, specifically in a distributed setting, can obtain Algorithm 1. The connection between the single-client algorithm and its distributed counterpart is not clearly established, making it difficult to understand the theoretical basis of the proposed distributed algorithm.

### Questions
1) The paper claims that the matrix step size improves performance but introduces problems. The presence of the neighboring term in Theorem 3 creates a significant neighborhood when $\Delta^{inf}$ is large.
2) This paper uses the compressed gradient as shown in (3), which is a direct compression on the full gradient. Given the prevalence of error feedback techniques in handling compression errors, it is pertinent to consider whether the proposed matrix step size can be extended to incorporate error feedback methods. 
3) The paper does not consider the use of SGD, local update, and partial participation techniques in distributed settings. 
4) The paper introduces det-CGD1, but it is unclear why this algorithm, specifically in a distributed setting, can obtain Algorithm 1.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
