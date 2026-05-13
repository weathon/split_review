# Memory-Efficient Backpropagation through Large Linear Layers

- Decision: Reject
- Scores: 3, 6, 3, 3

## Abstract
In modern neural networks like Transformers, linear layers require significant memory to store activations during backward pass.
This study proposes a memory reduction approach to perform backpropagation through linear layers.
Since the gradients of linear layers are computed by matrix multiplications, we consider methods for randomized matrix multiplications and demonstrate that they require less memory with a moderate decrease of the test accuracy.
Also, we investigate the variance of the gradient estimate induced by the randomized matrix multiplication.
We compare this variance with the variance coming from gradient estimation based on the batch of samples.
We demonstrate the benefits of the proposed method on the fine-tuning of the pre-trained RoBERTa model on GLUE tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The presented paper proposes a stochastic estimator for the gradient of a linear transform. The proposed estimator is unbiased and relies on a randomized algorithm for matrix multiplication. In practice, this results in the introduction of a randomized linear layer where instead of storing the full batch of inputs during the forward pass, a random projection of the input tensor onto a lower dimensional space is stored for the backward pass. This results in memory savings together with a tradeoff on the variance of the resulting gradient estimate. The authors derive a theoretical analysis of the additional variance introduced by the randomized matrix multiplication and conduct experiments on fine-tuning tasks for NLP applications.

The presented method shares strong similarities with previous work on randomized matrix multiplication in the context of deep learning [1].

[1] EXACT: Scalable Graph Neural Networks Training via Extreme Activation Compression

### Strengths
1) The authors provide a theoretical analysis of the additional variance induced by the randomized matrix multiplication procedure.
2) The authors reports practical savings observed in the fine-tuning tasks with respect to their implementation.

### Weaknesses
1) The paper lacks comparison to other works aiming at reducing memory requirements during training. For example, both [2] and [3] compress activations with a quantization procedure. [1] jointly uses randomized matrix multiplications and quantization to compress the stored activations. The lack of comparison with these methods makes it difficult to evaluate the relevance of the contribution against these alternatives. These papers aren't mentioned in the related work section.
2) The EXACT method [1] stores a random projection of the input where the compression is applied to feature channels. In the presented work, the compression is applied to the batch dimension. More generally, it would be interesting to know the practical importance of the dimension chosen for compression in the presented method. Specifically, how does the performance and memory trade-off vary when compressing across different dimensions (batch vs. feature channels)?
3) In a fully-connected layer, the weights themselves have a substantial memory footprint, which explains why retaining only 10% of the input dimensionality only yields 25% memory savings. For convolutional architectures, however, the weight space is much smaller, meaning that the relative savings would be much higher. It would be interesting to know how the proposed method translates in this setting. Furthermore, the memory savings should be evaluated more precisely, accounting for the overhead of storing the random projection matrix and any intermediate computations.
4) Given that transformers are now widely adopted in both NLP and computer vision, it would also be interesting to know how the proposed methods perform for a ViT on CIFAR10 and ImageNet, which would enrich the experimental section with minimal coding efforts. The current experiments are limited to NLP tasks, which does not provide a comprehensive evaluation of the method's applicability across different domains.
5) [Minor comment] If the RMM forward block sends $W, b, S^{\top}X$ then the FC forward block should send $W, b, X$ instead of $W, b$.

### Questions
1) Could the author provides comparison with other works based on quantization of the activations?
2) Could the author provide experiments on convolutional architectures or on computer vision benchmarks with a transformer-based architecture?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work presents a memory-efficient method for computing the needed gradients in backpropagation training through large linear layers.
The method uses the randomized matrix multiplication approach to achieve this.
It randomly creates a matrix S that projects the signal X into a smaller dimension space.
The reduction is controlled by $\rho$, which takes up a value between 0 and 1.
The only required condition for S is that its autocorrelation equals the identity matrix I.

This work further analyzed the gradient variance induced by the randomized computation.
It also provides a detailed explanation of how the new approach reduces the memory requirement for backpropagation.
The work provides simulation results to support the main claim.

### Strengths
The paper is well organized and the literature review provides enough context needed to understand this work.
The topic is an interesting one that is worth pursuing, especially in the era of ever-growing large models that rely on transformer modules.

### Weaknesses
One of the suggested claims (under section 2.3) is not well-supported.
This work seems to suggest that the difference between the exact gradient and the randomized approximation is a form of noise injection.
It went on to state that it can play the role of a regularizer.
You will need to model the effect of the randomized error as such to make this claim. 
I do not think this paper contains such an explanation.

The paper states that the only requirement for the random matrix S is that its autocorrelation be equal to I.
But the definition of the random Gaussian random matrix suggests that the autocorrelation is  $\frac{1}{B_{proj}} I$.
I think you should align the two.
You can treat the constant as a scale on the learning rate.

### Questions
1). How will the sample size of $S$ affect the performance of this method?
I think the algorithm statement suggests that you only picked one sample of S.
If we compute the gradient over multiple samples of $S$ and take the average, will this improve the performance or not? 
This follows from equation (4), which relies on the expectation of the randomized gradients over $S$
It will be interesting to see the trade-off between the additional workload and the 
 
2). How does the depth of the network affect the variance and error induced by the randomized gradients?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This article proposes a way to reduce the memory cost of the backpropagation of linear layers, with Randomized Matrix Multiplication.

### Strengths
This article is relatively well-written and easy to follow.
The RMM algorithm is simple and well-motivated, lowering immediately the memory cost of backward operations on linear layers in DNN.
The authors bring a novel analysis of variance in both SGD and RMM.

### Weaknesses
 **Novelty** The novelty of the method is very limited. The main idea is already present in Adelman et al. (2021), even though their goal was not to save the memory during the stage. The authors do not bring many contributions over Adelman, the theoretical analysis of the variance being unclear in particular.

**Variance** $D_{SGD}$ and $D_{RMM}$  are not defined clearly (or in equations (10) and (11), is $D_{RMM}=D$?). In the Appendix, the equation (21) $D^2_{SGD}(X,Y)= \frac 1 {B−1} D^2 _Z(X,Y)$ is not clear. The core issue is that the notation is inconsistent and the relationship between $D_{SGD}$, $D_{RMM}$, and $D_Z$ is not rigorously established. It's unclear if $D_{RMM}$ is meant to represent the variance of the RMM gradient estimator or something else entirely. The connection between equation (21) and the variance of SGD is also not well-explained, and the factor of $\frac{1}{B-1}$ is not justified.

More generally, it is quite unclear what should be the conclusion of the analysis of the variances of SGD and RMM in Sections 2.3 and 3.3. The theoretical analysis gives an upper bound of the variance of RMM, but we observe that in practice the variance of RMM is much higher than the one of SGD, meaning that RMM brings a lot of noise to the training, which seems to hinder training. What is the conclusion of these sections? I also would at least have appreciated the theoretical upper bound on Figure 3. The practical implications of the variance analysis are not adequately discussed. The paper needs to clearly articulate how the theoretical bounds relate to the observed empirical behavior and what the trade-offs are between the variance of RMM and its memory savings.

**Computation cost** The computation requirements should be moved from the appendix to the main paper and discussed there, considering their importance. In particular, the comparison between the computation costs $O(BN^2)$ and $O(ρBN(B+ N))$ is important, as it showcases that the method may be slower, an important drawback that is confirmed in Table 3. For such a high computation time cost, other methods that compress the activation vector $X$ will be favored. The paper should also include a more detailed analysis of the computational overhead of the randomization process itself, including the cost of generating the random matrices and performing the matrix multiplications. This overhead could be significant, especially for large-scale models.

**Pretrained network** Experiments being done on a pre-trained network do not allow a clear measurement of the degradation due to RMM during training. The use of a pretrained network masks the true impact of RMM on the training dynamics. It is difficult to assess how RMM affects the convergence behavior and generalization performance when the network is already close to a local minimum. Ideally, the authors should include experiments where the network is trained from scratch using RMM.

Section 3.4 brings nothing new compared to Table 2.



### Questions
"In Adelman et al. (2021) the construction of S requires the knowledge of the norms of the rows of Y". I may be mistaken but I do not understand why this is the case. Bernoulli-CRS is unbiased whatever the values of $p_{j}$ are. Therefore it can be applied to RMM with no knowledge of $Y$ for any distribution $p_j$.

The results of Section 3.3 seem surprising. Why is the SGD variance increasing during training, while the network should converge?

Why say that "Subsampled Orthonormal with Random Signs (SORS)" is not considered if there is a Comparison of Randomized MatMuls in Section 3.5?
Considering the cost of computation of RMM, why should we choose Gaussian RMM rather than DCT or DFT, which the authors note have a much smaller computation cost?

"Moreover, we empirically found that our randomization is faster if ρ ≤ 0.1." Doesn't Table 3 show that even with $\rho=0.1$ the randomization is still longer than no RMM?

Various remarks and errors:
* Section 2.2: "this should be?", "target really accurate", "it may seem"
* Section 3 "We rewrite implementation". PRNG stage $G$ is only used here. " compression in 5–10 times" "study influence of randomized" "However, overfitting point"
*

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The proposed RMM utilizes random projection to reduce the memory required to store input activations of the linear layer while still achieving comparable accuracy.

### Strengths
This paper is 

1. well-written, 

2. provides justification for the RMM method through a comparison of gradient variance with SGD, and 

3. demonstrates the usefulness of the algorithm in RoBERTa.

### Weaknesses
1. Lack of experiemntal results

: The paper claims the efficacy of the method for large linear layers, but only presents experimental results from the GLUE benchmark of RoBERTa. A performance comparison with larger models, such as LLaMA-2-7B with over 7B parameters, seems necessary. The absence of results on models with significantly different scales and architectures raises concerns about the generalizability of the proposed method. Specifically, the behavior of random projection in extremely high-dimensional spaces, common in very large models, needs to be empirically validated.

2. Lack of comparison between previous works

: In fact, there have been many attempts in the past to save memory through activation compression. Notably, GACT (2022) is capable of compressing all input activations, including those of the linear layer, to an average of 4-bit in BERT-Large. A comparison between such existing methods and RMM seems necessary. The paper should include a quantitative comparison with state-of-the-art activation compression techniques, demonstrating the advantages and disadvantages of RMM in terms of both memory savings and accuracy. The current lack of comparison makes it difficult to assess the practical value of the proposed method.

3. Lack of novelty

: As the author pointed out, random projection has long been a widely used method, and applying it to activation compression doesn't necessarily mean it lacks novelty. However, there have already been cases using random projection under the same objective of activation compression. EXACT (2022) compresses activations using random projection, which seems strikingly similar to the proposed RMM. The paper needs to clearly articulate the novel aspects of RMM compared to existing methods like EXACT, especially given the shared use of random projection. Without a clear distinction, the contribution of the paper is significantly weakened.

### Questions
1. Lack of experiemntal results

: Please provide experimental results on larger models like LLaMA-2-7B. This is crucial in bolstering the claims made in the paper.

2. Comparision with previous works

: A quantitative experimental comparison with recently proposed activation compression algorithms like GACT (2022), EXACT (2022), AAL (2023), and DropIT (2023) seems necessary. If the review period is limited, please at least provide a comparison with GACT (2022), which is the-state-of-art activation compression technique,  in terms of 1) accuracy and 2) memory saving through experimental data. For the remaining algorithms, a qualitative analysis can be included in the related work section.

3. Lack of novelty

: A detailed comparison with EXACT, which also uses random projection, seems necessary. To offer some advice, 1) Unlike EXACT, RMM appears to compress the batch dimension. Demonstrating mathematically that this difference allows RMM to further reduce gradient variance, or 2) showing through actual experimental results that RMM offers a significant accuracy improvement over EXACT, would likely address concerns regarding novelty.

However, one concern is that, based on the comparison results in the Appendix for GCN2, EXACT seems to achieve higher accuracy than RMM. Given that both algorithms adopt very similar approaches, the accuracy of RMM must necessarily be higher than that of the existing EXACT.

* GACT: Activation Compressed Training for Generic Network Architectures (2022)
* EXACT: Scalable Graph Neural Networks Training via Extreme Activation Compression  (2022)
* DropIT: Dropping Intermediate Tensors for Memory-Efficient DNN Training (2023)
* Learning with Auxiliary Activation for Memory-Efficient Training  (2023)

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
