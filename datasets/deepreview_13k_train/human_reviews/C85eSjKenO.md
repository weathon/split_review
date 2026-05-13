# Tensor-GaLore: Memory-Efficient Training via Gradient Tensor Decomposition

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
We present Tensor-GaLore, a novel method for efficient training of neural networks with higher-order tensor weights. Many models, particularly those used in scientific computing, employ tensor-parameterized layers to capture complex, multidimensional relationships. When scaling these methods to high-resolution problems makes memory usage grow intractably, and matrix based optimization methods lead to suboptimal performance and compression. We propose to work directly in the high-order space of the complex tensor parameter space using a tensor factorization of the gradients during optimization. We showcase its effectiveness on Fourier Neural Operators (FNOs), a class of models crucial for solving partial differential equations (PDE) and prove the theory of it. Across various PDE tasks like the Navier Stokes and Darcy Flow equations, Tensor-GaLore achieves substantial memory savings, reducing optimizer memory usage by up to 75\%. These substantial memory savings across AI for science demonstrate Tensor-GaLore's potential.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper extends GaLore [Zhao 2024] to neural networks with tensor weights by adding Tucker Decomposition and performing low-rank projection directly on tensor gradients. The experiment compares the proposed method to vanilla GaLora (with reshaping) on Fourier Neural Operators (FNOs), a class of tensor-weight models for solving partial differential equations.

### Strengths
This paper appears to tackle a gap that has received little attention by the literature, the efficient training of tensor-weight models, with the only prior works being [Kossaifi 2024] and [George 2024]. 

The paper is generally well-written and easy to follow, with a clear story.

### Weaknesses
Despite the novel application, the approach is a somewhat straight-forward extension of GaLore to tensor-weight models, replacing SVD decomposition with Tucker. 

There is a lack of discussion on the slowdown in training given the overhead.

### Questions
See weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work presents Tensor-GaLore, an algorithm that leverages low-rank tensor decomposition on the gradients of tensorized weights. This work is built on top of the previous work (GaLore), which applies low-rank factorization (SVD) on the gradients. Experimental results show that applying it Fourier Neural Operators yield better memory usage and accuracy for numerical PDE problems.

### Strengths
1. The quality of the presentation is good. The work is clear and easy to follow.
2. The idea of using Tucker decomposition to perform low-rank approximation makes sense for numerical PDE problems, and experimental results verify that.

### Weaknesses
Despite being clear and effective, I believe the work has limited novelty. The tensor-GaLore approach has limited difference compared to GaLore. In particular, the core idea of applying low-rank approximations to gradients is already present in GaLore, and this work simply extends it to tensor decompositions. The application of Tucker decomposition, while sensible for tensorized weights, feels like a direct application of existing tensor decomposition techniques rather than a novel algorithmic contribution. In addition, only empirical rather than theoretical results is provided to show the efficacy of the algorithm. The paper lacks a theoretical analysis of why and when the proposed method should be expected to work, and how it compares to other low-rank approximation methods in terms of convergence and stability.

### Questions
please see above

### Soundness
3

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
3

### Summary
This paper presents a modification of the GaLora method that allows to update the weights not directly, but in a low-parameter space. The authors present a modification of this method that uses a low rank tensor decomposition, namely the Tucker decomposition, instead of a low rank matrix decomposition. This approach is applied to neural operators for solving PDEs, where 4-way tensors arise naturally.

### Strengths
- The paper uses a low-rank tensor decomposition, which preserves the original multidimensional structure
- Some experiments show the effectiveness of this technique
- Clearly presented paper

### Weaknesses
 - No code provided to reproduce the results
- No theoretical analysis (in the original GaLora paper there are theoretical justification of low-rank structure, convergence, etc.)
- The only significant change (other than technical changes) from the original GaLora method is the use of Tucker Decomposition for 4-way tensor instead of low-rank matrix decomposition
- The presented method shows good results only on the Darcy flow equation, in the other experiments the improvement is not strong
- Since this paper describes improvements to the GaLora method (which has been published previously), it would be fair to compare against it rather than baseline. For example, in Table 2 for the Darcy equation the presented method is 48.8% better than baseline, while the regular GaLora is 19% better than baseline. Thus, the improvement presented in this paper is a 25% improvement.

Overall, this paper is incremental to the original GaLora paper, without theoretical evaluations (which were in the original paper) and with inconclusive numerical results.

Minor 

- L458-459 "On Darcy flow (as shown in Table 6)" should be "Table 2"
- L397 word "Table" is missing

### Questions
- Can one pick the efficient rank ratio in advance?
 - How is it that for Burgers Equation in Table 2 test loss is much (by an order of magnitude) less than train loss?
 - Have you tried using other low-rank tensor decompositions (CANDECOMP/PARAFAC, Tensor-train, etc.)?

In Algorithm 1

- is $r$ is rank of rank ratio?
- tensor $\mathcal{M}_0$ (with $\mathcal V_0$) has the same shape as $\mathcal W\in\mathbb{C}^{N_1\times N_2\times N_3\times N_4}$. Should it be $\mathcal M_0\in\mathbb{C}^{R_1\times R_2\times R_3\times R_4}$?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors present Tensor-GaLore as a method for compressing the weights using tensor compression. They show the use of their approach on Fourier Neural Operators (FNOs) used for solving PDEs.

### Strengths
The focus on efficient learning techniques for PDEs is very timely and requires constant improvement to outperform traditional methods in terms of accuracy and computing time.

### Weaknesses
 - the authors discuss that TensorGalore is superior to Galore as it avoids SVDs. Nevertheless, the computation of tensor formats (Tucker, Tensor Train, etc.) relies on matricizations of the tensor and then typically singular value decomposition of those. So the SVD is still at the heart of TensorGalore.
- I think the idea of the manuscript is based on taking an FNO example and then using the tensor compression of the weights. I believe this to work well but it also seems a straightforward extension of previous work. There have been many applications of tensors for compression within neural networks.

### Questions
- How do the authors implement their tensor format as they argue that the disadvantage of Galore is the need for the SVD, which typically used for efficient computations of popular tensor formats?

### Soundness
3

### Presentation
3

### Contribution
2
