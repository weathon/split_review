# Schur's Positive-Definite Network: Deep Learning in the SPD cone with structure

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
Estimating matrices in the symmetric positive-definite (SPD) cone is of interest for many applications ranging from computer vision to graph learning.
  While there exist various convex optimization-based estimators, they remain limited in expressivity due to their model-based approach.
  The success of deep learning motivates the use of \emph{learning-based} approaches to estimate SPD matrices with neural networks in a data-driven fashion.
  However, designing effective neural architectures for SPD learning is challenging, particularly when the task requires additional structural constraints, such as element-wise sparsity.
  Current approaches either do not ensure that the output meets all desired properties or lack expressivity.
  In this paper, we introduce SpodNet, a novel and generic learning module that guarantees SPD outputs and supports additional structural constraints.
  Notably, it solves the challenging task of learning jointly SPD and sparse matrices.
  Our experiments illustrate the versatility and relevance of SpodNet layers for such applications.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a new method SPODNET for learning SPD matrices by elements, supported by the classical Shur’s condition, where the matrix elements (u and v) to update are learned using neural networks. The work demonstrates the use of SPODNET for the sparse precision matrix learning task, and proposes three new model architectures to perform the learning, including UBG, PNP and E2E. Two sets of experiments were conducted for evaluation, using a synthetic data and a real-world data. The results show the effectiveness of the proposed methods, and their advantages over the compared ones.

### Strengths
•	To my knowledge, the proposed method is original. I like the proposed SPODNET, building on classical theory, simple but elegant.
•	The paper is well written and well structured.
•	Experiment design is appropriate for demonstrating the effectiveness of the proposed method. I particularly like the result of UBG in Figure 6, highlighting more distinct structure that is interesting  for this real-world data.

### Weaknesses
•	The paper would be stronger if they could include another real-world learning problem over SPD manifold.  But I don’t see this as a major issue.
•	Lack of discussion on the limitation of the proposed work.
•	There are a couple of things that could be explained better, see my questions.
•	Figures 4 and 5 are too small, hard to read.

### Questions
•	Although the proof is straightforward, it would be useful for the reader and for completeness to explain how Eq. (3) is derived in proof.
•	For clarify, the role/design rationale behind each term in Eq. (5) can be explained briefly, although it is an existing method.
•	In line 364, it is mentioned that the MSE reconstruction loss is used. How is this implemented together with the GLasso loss in Eq. (5)?
•	How does the proposed method perform in terms of training time/cost?
•	What do different colours mean in Figure 1?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a deep learning-based approach to solving SPD problems such as covariance selection. The authors start with the block coordinate descent (BCD) algorithm and then unroll the optimization using neural networks. This follows with three different unrollings, where each preserves different levels of the problem structures (or inductive bias in the deep learning words). The authors evaluate the proposed SpodNet on synthetic data and the animal dataset against GLAD, GLasso, and other traditional approaches.

### Strengths
The paper is well-written and easy to follow. The idea of unrolling the column-row BCD algorithm to ensure SPD seems novel.

### Weaknesses
I think this is a borderline paper in its current form. I value the novelty of the paper, but its numerical performance is not the most convincing. I think solving the following points will make the paper stand more firmly at my rating.

1. GLAD-Z: SpodNet's NMSE performance on synthetic data seems to be consistently worse than GLAD-Z's. I understand the authors' argument that GLAD-Z is not SPD, but what if Z is projected onto the SPD cone? Will the projected Zs remain the lower NMSE scores? Because GLAD uses an ADMM-like algorithm, the learned $\Theta$ matrices are not projections if I understand correctly.
2. Large sample regime: The NMSE performance of SpodNet is no better or only marginally better than the baselines when $n>p$.
3. Real-world datasets: The results of GLAD on the animal dataset are missing. Also, the paper will benefit from adding at least another real-world dataset.
4. Figures: Some figures can be hard to read, especially Fig. 4-5. I suggest the authors use thinner lines and/or redesign their layout to make line plots larger.

### Questions
1. Training details: What are the exact steps of the unrolling algorithm? How many unrollings are needed? From line 363, does the training posit an MSE loss on the intermediate $\Theta$s or only the last one?
2. GLasso: In Fig. 5, the F-1 performance of GLasso decreases when $n$ gets larger. This is weird because I expect it to recover the graph perfectly when $n\gg p$. What are the authors' explanations about this?

### Soundness
2

### Presentation
3

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
The paper presents a method for jointly learning Symmetric Positive Definite (SPD) and sparse matrices using a learning based approach. The proposed method SpodNet is an iterative method which learns column-row pairs stepwise where each step is parametrized by a neural network. The SPD constraint is then ensured via Schur’s condition.

### Strengths
1. SpodNet enables increased expressivity for estimating SPD matrices with a neural network based parametrization, at the same time maintaining constraints like sparsity unlike other model based approaches, as verified by experiments on synthetic data.
2. In order to make the method tractable the authors leverage the block structure of SPD matrices to restrict the complexity of each update step to $O(p^2)$.
3. Experiments on synthetic data and graph topology estimation using SpodNet are presented, highlighting the effectiveness of the method. On the synthetic data, the proposed method is similar to model based approaches while achieving both SPD and sparsity at the same time.

### Weaknesses
1. The proposed SpodNet provides a novel approach to leverage neural networks and increase expressivity on constrained manifolds. However, the design of the neural networks itself is not discussed in detail. It is not clear to me why the authors choose the input features for  $g$ as $\theta_{22}$, $s_{22}$ and $\theta_{12} \theta_{11}^{-1} \theta_{12}$. Similar for each of the three described approaches the explanation for choosing the input features is missing. I assume the features are chosen to best suit the model based approach and that performs well with gradient descent but the paper would benefit from a detailed explanation of the same.
2. The method still seems relatively expensive in spite of the improved update rule. The overall cost as the authors mentioned is of the order of $O(p^3)$, how does this compare with the other model based approaches?
3. Can the SpodNet framework maintain other structure constraints for example structural sparsity. In general what conditions would the constraints need to satisfy in order to be optimized with a SpodNet layer.

Since the general literature of SPD matrix estimation points towards applications in computer vision, it would be informative to see an experiment for a vision task with SpodNet to verify the comparison with baselines and its scalability given its computational requirements.

### Questions
See above

### Soundness
3

### Presentation
3

### Contribution
3
