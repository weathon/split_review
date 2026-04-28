# Differentiable Learning of Generalized Structured Matrices for Efficient Deep Neural Networks

- Decision: Accept
- Avg Score: 5.67
- Scores: 6, 5, 6

## Abstract
This paper investigates efficient deep neural networks (DNNs) to replace dense unstructured weight matrices with structured ones that possess desired properties.
The challenge arises because the optimal weight matrix structure in popular neural network models is obscure in most cases and may vary from layer to layer even in the same network.
Prior structured matrices proposed for efficient DNNs were mostly hand-crafted without a generalized framework to systematically learn them. 
To address this issue, we propose a generalized and differentiable framework to learn efficient structures of weight matrices by gradient descent. 
We first define a new class of structured matrices that covers a wide range of structured matrices in the literature by adjusting the structural parameters.
Then, the frequency-domain differentiable parameterization scheme based on the Gaussian-Dirichlet kernel is adopted to learn the structural parameters by proximal gradient descent.
On the image and language tasks, our method learns efficient DNNs with structured matrices, achieving lower complexity and/or higher performance than prior approaches that employ low-rank, block-sparse, or block-low-rank matrices.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors introduce a Generalized Block-low-rank  (GBLR) matrix format to construct computationally efficient structures of weight matrices. They also introduce Gaussian-Dirichlet (Gaudi) function to make the structural parameters differentiable and provide an algorithm to learn neural networks with Gaudi-GBLR weight matrices.

### Strengths
The proposed GBLR format includes existing important matrix structures. Also, the authors provide a method to make the structural parameters of weight matrices learnable. The idea is interesting and relevant to the community.

### Weaknesses
Providing theoretical investigations of the neural networks learned by the proposed method can improve the quality of the paper. Since the weight matrices are forced to be sparse, I think we need a different analysis from existing analysis for the dense weight matrices. For example, do you have any explanation about the representation power and generalization property of the networks with GBLR weight matrices?

### Questions
As I also mentioned in the weakness part, how does the GBLR weight matrices affect the generalization property or the complexity of the neural network?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a generalized and differentiable method to learn efficient structures of weight matrices. Moreover, the authors present an effective initialization technique for the proposed method. Some experimental results show the performance of the proposed method.

### Strengths
1. This paper proposes a generalized and differentiable method to learn efficient structures of weight matrices. 
2. Moreover, the authors present an effective initialization technique for the proposed method. 
3. Some experimental results show the performance of the proposed method.

### Weaknesses
Although the paper is theoretically and experimental sound, there are still some questions need to be discussed in this paper:
1.	In Algorithm 1, what’s AdamW(.), as well as clip?
2.	In Eq. (8), what’s the variable, w or \theta?
3.	The advantage of the proposed method against existing methods is not clear. 
4.	The parameter initialization for the proposed method needs to perform SVD. Thus, the authors should analyze the computational complexity.  
5.	The experimental results are not convincing. The authors should compare the performance of the proposed algorithm and more methods on more models and datasets.
6.	The English language in this paper needs to be improved.

### Questions
Although the paper is theoretically and experimental sound, there are still some questions need to be discussed in this paper:
1.	In Algorithm 1, what’s AdamW(.), as well as clip?
2.	In Eq. (8), what’s the variable, w or \theta?
3.	The advantage of the proposed method against existing methods is not clear. 
4.	The parameter initialization for the proposed method needs to perform SVD. Thus, the authors should analyze the computational complexity.  
5.	The experimental results are not convincing. The authors should compare the performance of the proposed algorithm and more methods on more models and datasets.
6.	The English language in this paper needs to be improved.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents a new compressed matrix format (parametrization) called GBLR and an optimization method (involving proximal gradient descent, homotopy, and STE) to learn the parameters of the format to make NNs faster and smaller. The proposed parametrization can be understood as a juxtaposition of low-rank matrices of various shapes that needs to be appropriately padded. Such a parametrization is very flexible as contains regular low-rank matrices (if the shape of the blocks are same as the shape of the entire matrix), block low rank matrices, and block sparse. To be more specific, every low-rank submatrix  is represented as a sum of rank-1 matrices; thus, for a given subblock of rank $k$ parameters include shape of submatrix ($w$,$h$), location within orgininal matrix (i,j), and actual values that are $k$ rank-1 matrices of $w \times h$ stored as $w\times 1$ and $1 \times h$ updates.

Such a parametrization has many non-differentiable parameters, and to make it amenable to SGD based solvers the authors propose several modifications: instead of storing compact $w\times 1$ and $1\times h$ rank-1 matrices, the parametrization now involves the whole $n\times 1$ and $1\times n$ vectors that are appropirately masked with vector $m$. The mask presents a boxcar filter which is non-differentiable itself, but author approximate it via Gaudi mask in frequency domain with gaussian kernel (with variance $\sigma^2$); Gaudi mask converges to boxcar with $\sigma \to \infty$ which needs to be driven during training (hence a homotopy). Also, during the training the width $w$, height $h$, location $i,h$, are kept real-valued (for SGD) but apply straight-through estimation for actual matrix recreation. And finally, to drive matrix rank selection, authors propose a cost based selection via an $\ell_1$ penalty (controlled by $\lambda$) on certain structure parameters (since the exact equation is not given, I'm guessing on every rank-1 matrix?).

As for training of the compressed models, the authors plug in GBLR parametrized matrix instead of original weight matrices of nns (the initial values are obtained via an algorithm in A.2), choose appropriate $\lambda$ (to control for rank), and train or finetune end-to-end on a dataset. The results clearly show that such a scheme gets a better compression-accuracy tradeoff.

### Strengths
The paper proposed a new matrix parametrization that includes many other compressed forms (low rank, block low-rank, and block sparse) as a subset. The parametrization allows to get better error-compression tradeoffs.

The presentation of the method is very thorough and includes many small details (except for some, see questions) that is definitely a plus for reproducibility.

### Weaknesses
I find two minor weaknesses of the paper, literature review and comparison to other methods.

Although I understand that the focus of paper was compression of transformer based models, it seems many relevant low-rank and tensor-decomposition based methods that were used for compression of other networks (CNNs) were left out. Many of those left out papers share similar ideas (e.g., how to parametrize wrt rank) that need to be included. Some of the missed out works include:
- Factorized Higher-Order CNNs with an Application to Spatio-Temporal Emotion Estimation 
- Low-rank Compression of Neural Nets: Learning the Rank of Each Layer
- Coordinating filters for faster deep neural networks
- Constrained optimization based low-rank approximation of deep neural networks
- Compressing Neural Networks: Towards Determining the Optimal Layer-wise Decomposition

but there are many others (you can find others by looking within those)

Comparison to the relevant baselines. It seems the baselines authors choose are very simple (e.g., using a fixed rank for low-rank compression), and can be considerably strengthened if wanted. Thus I'm asking authors to include stronger baselines (low rank with rank selection, tensor decomposition methods) to compare.

### Questions
1. Can you please provide the exact from of $\ell_1$ penalty used in eq.8? How does FLOPs/parameter counts being represented as F$\ell_1$ penalty?
2. What is the value of $\lambda$ used in experiments? How to choose it properly?
3. What was the scheme used for $sigma$? The paper says that it was "gradually increased to 100", but having exact details is preferred.
4. Certain computations (Gaudi function) happens in frequency domain that involves DFT and IDFT; how expensive is this operations wrt single training step? No slowdown, 0.75x slowdown, etc..
5. Please included a more detailed literature review.
6. Please strengthen the baselines.
7. I am wondering why section 3.3 discusses the application on the basis of two layer MLP "for ease of understanding"? Wouldn't an example on a single layer be much simpler? BTW, there is a typo in this section, multi-layer perception => multi-layer perceptron

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
