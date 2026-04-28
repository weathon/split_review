# Stabilized E(n)-Equivariant Graph Neural Networks-assisted Generative Models

- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 3, 5

## Abstract
Due to its simplicity and computational efficiency, the E(n)-equivariant graph neural network (EGNN) [Satorras, et al., ICML, 2021] has been used as the backbone of equivariant normalizing flows (ENF), equivariant diffusion model (EDM), and beyond for Euclidean equivariant generative modeling. Nonetheless, it has been observed that ENF and EDM can be unstable; in this paper, we investigate the source of their instability by performing a sensitivity analysis of their backpropagation. Based on our theoretical analysis, we propose a regularization to stabilize and improve ENF and EDM. Experiments on benchmark datasets demonstrate that the regularized ENF outperforms the baseline model in terms of stability and computational efficiency by a remarkable margin. Furthermore, our results show that the proposed regularization can stabilize EDM and improve its performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper highlights that there exists instability in training E(n)-graph neural networks (EGNN), especially maps for positions. The authors aim to stabilize the training of EGNN, especially by regularizations. Note that positional mapping in the EGNN includes the distance multiplication term, which is the distance between the node's position and its neighbor's, and it is critical to the E(n)-equivariance of EGNN.

The authors first point out that the parameters' gradient is proportional to the gradient of the EGNN outputs wrt the pairwise distance (between a node and its neighbor), and thus, the gradient term is the source of the instability of the EGNN training.

Due to the gradient term, the authors claim that the previous attempt to stabilize the training, i.e., the normalized distance multiplication, is not sufficient, and thus, the authors propose to penalize the norm of the gradient (of EGNN) wrt the pairwise distance.

To test the hypothesis, the papers compare the three versions of EGNNs (vanilla, normalized distance, and the proposed method) over various benchmark datasets.

### Strengths
I consider that the paper and its results are essential for several reasons:

1. The paper provides a better understanding of a critical problem in training EGNN, i.e., the instability of its training, especially to the potential audience unfamiliar with EGNN and other similar models.
2. The paper well motivates the proposed method so that readers can understand how each step contributes to the merits of the regularization.
3. I found that the paper has a well-organized structure that makes it clear to understand the proposed method.

In addition, I found that the paper has a well-organized structure that makes it clear to understand the proposed method.

### Weaknesses
While the proposed method seems well-motivated and interesting, the importance of the proposed method needs further analysis.

For example, it is unclear why the gradient wrt the pairwise distance is the key source of the instability of the EGNN training, while the authors claim that the instability stems from the gradient. However, the claim is backed only by the sensitivity analysis explained in Section 3.2, which seems close to intuitions in my understanding. I believe that it would be much clearer if the authors were showing that the gradient wrt the pairwise distance is exploded when the training of vanilla EGNN failed.

### Questions
In my understanding, when the gradients are unstable during training, one common solution is gradient norm penalty or gradient clipping. How does the proposed method perform against such common techniques?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper builds upon E(n)-equivariant graph convolutional networks (EGNN) by normalizing the convolution layer with respect to the node’s positions, and by adding a regularization term to the loss that promotes small gradients during training. The goal is to stabilize the training of graph generative models: normalizing flows and diffusion models.

### Strengths
The paper is mostly well written and clear. The regularization and normalization methods are shown in experiments to improve performance.

### Weaknesses
The paper's contribution appears incremental, primarily involving a normalization factor applied to the well-known EGCL and a regularization term added to the training process. While these modifications are not entirely without merit, they represent relatively standard techniques in the field. The normalization approach, specifically the addition of the +1 term in the denominator, raises concerns about its stability and effectiveness across different coordinate scales. Furthermore, the analysis of the backpropagation stability is incomplete, neglecting crucial terms that contribute to the overall gradient magnitude.

Specifically, the sensitivity analysis in Section 3.2 seems to oversimplify the derivative of the coordinate update. The chain rule application appears to be missing intermediate steps, particularly the differentiation with respect to the intermediate message  `m_{i,j}`. This omission raises questions about the thoroughness of the analysis and the validity of the conclusions drawn from it.

Moreover, the analysis in Section 4 focuses solely on the derivative `\partial f^{l+1}/\partial f^l`  as the primary contributor to the gradient magnitude. However, this overlooks other significant components, such as `\partial f^l/\partial \theta^l`, which are likely influenced by `||x_i-x_j||^l`. This suggests that the proposed regularization, while potentially beneficial, might not be the sole or even the most effective way to address the instability issue. A more systematic analysis encompassing all contributing factors to the gradient is necessary to provide a complete picture.

The lack of a unified comparison between EDMs and ENF in the molecule generation experiments is another area that needs attention. Presenting these results separately obscures the relative performance of these methods and hinders a comprehensive evaluation of the proposed approach.

### Questions
Page 4: “In contrast, normalizing coordinates can avoid abnormal coordinate updates from large differences among coordinates of neighboring nodes” - but on the flip side, without the $+1$ regularization in the denominator, it is unstable to small coordinates. But with the $+1$ normalization, close-by nodes contribute a very small difference. How do you then choose the scale of the coordinates for the $+1$ to work well? Why do you use $+1$ and not $+b$ for some $b$ that depends on the characteristic target distance between modes?

Please explain how you construct a graph from the node locations and features.

Proposition 1: In all sums, shouldn’t you sum over the neighborhood, and not the whole graph? $m_{i,j}$ is only defined when $(i,j)$ is an edge.

Section 3.2 Sensitivity Analysis: The normalized EGCL is different from the unnormalized one. Why don’t you compute the derivatives of the normalized version if this is the method you propose? Also, it is strange to directly write the derivative of $\phi_x$ with respect to $\|x_i-x_j\|$. You need to use the chain rule, and first differentiate with respect to $m_{i,j}$.

Notations: you did not define $I_3$.

Section 4: I don’t think that the derivative $\partial f^{l+1}/\partial f^l$ is the only main contributor to the size of $\partial L (f^L)/\partial \theta$. To see this, note for example that when partitioning the parameters to the last layer parameters $\theta^L$ and the previous layers parameters $\theta^{L-1}$,  $\partial L (f^L)/\partial \theta$ has two components. First, $\partial L/\partial f^L \cdot  \partial f^L\partial \theta^L$, and then $\partial L/\partial f^L \cdot  \partial f^L\partial f^{L-1}\cdot \partial f^{L-1}\partial \theta^{L-1}$. Hence, $ \partial f^{l}/\partial \theta^{l}$ are also important, and these are roughly going to depend on $\|x_i-x_j\|^l$ by induction, as each later multiples by a factor of order $\|x_i-x_j\|$. I think that this is another main reason you would like to normalize $x_i-x_j$.

This example is to illustrate that the analysis presented in this paper is partial. There is no systematic analysis of all components that contribute to the gradient. 

One thing that is confusing in the analysis is that it analyzes only the unnormalized layer.  If you want to show that the normalized layer is more stable, you should write down a gradient analysis of it also. And write the full gradient with respect to the model parameters, as these are the gradients in training.


Experiments: why are EDMs and ENF not compared against each other and other models in molecule generation in one table? I only see a comparison between EDM and other methods.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a regularizer to alleviate the training instability issue of EGNN in generative modeling. It analyzes the gradient of coordinate updates with respect to input and figures out the sensitive term that results in numerical explosions. Experimental results show that the proposed regularizer can successfully stabilize the ENF and EDM training.

### Strengths
(1) This is the first time delving into the numerical instability issue of the ENF and EDM training. This is a very important challenge and fundamental research question that was overlooked in the previous research. This reviewer agrees with the significance of the proposed challenge;

(2) The writing is basically well-organized, containing both theoretical analysis and experimental analysis, which makes the paper technically solid;

### Weaknesses
 (1) This work analyzes the gradient update of a single-layer EGNN but this reviewer does not see an analysis of special reasons leading to unstable ENF and EDM training. Only a single sentence states that “In both ENF and EDM, the graph node coordinates keep changing during the generative process, and abnormal coordinate updates may occur.” However, the generative process is the inference process while this paper is dealing with the training instability. Therefore, the ENF and EDM training instability is not accurately summarized. Is EGNN on the given training data stable? Is ENF and EDM unstable on the given training data? If the answers to both questions are yes, then this might indicate that there are special reasons resulting in the instability of ENF and EDM training. If ENF and EDM training instability is caused by EGNN training only (no special stuff), then the discussions over the ENF and EDM are redundant and not necessary. In general, this reviewer thinks the preliminary discussions over the training instability are not sufficient. Specifically, the paper lacks a clear explanation of why the coordinate updates in ENF and EDM training are more prone to instability than standard EGNN training. The analysis should pinpoint the specific mechanisms within the ENF and EDM frameworks that exacerbate the gradient issues observed in EGNNs. For instance, are the specific loss functions used in ENF and EDM contributing to this instability, or is it related to the iterative nature of the generative process during training? Without a deeper dive into these aspects, the motivation for focusing on ENF and EDM remains unclear. 

(2) The proposed regularizer is a sum of gradient calculations, which is extremely hard to compute. The summations are computed over all atom pairs (i, j) and EGNN layers L with at least O(N**2*L) time complexity. Hence, although the proposed regularizer is a very effective approach to restricting the gradient norm, the calculation of the proposed regularizer could not be scalable to either larger particle systems or deep EGNN architectures.

### Questions
(1) What is the time complexity of the calculation of the proposed regularizer? How could the proposed approach scale to larger particle systems and deep EGNN architectures?

(2) What are the special reasons for numerical instabilities in ENF and EDM training? Or the instability of ENF and EDM is all caused by EGNN?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
