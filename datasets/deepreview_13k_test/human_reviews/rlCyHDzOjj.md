# A New Tensor Network: Tubal Tensor Train Network and its Applications

- Decision: Reject
- Scores: 6, 5, 3, 5

## Abstract
This paper introduces the Tubal Tensor Train (TTT) decomposition, a novel tensor decomposition model that effectively mitigates the curse of dimensionality inherent in the Tensor Singular Value Decomposition (T-SVD). The TTT decomposition represents an $N$-order tensor as the Tubal product (T-product) of a series of two third-order and $(N-3)$ fourth-order core tensors, contracted. Similar to the Tensor-Train (TT) decomposition, our approach addresses the curse of dimensionality problem. In order to decompose a given tensor into the TTT format, we propose two high-performing algorithms. Numerical simulations are conducted on diverse tasks to demonstrate the efficiency and accuracy of these algorithms compared to the State-of-the-Art methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel tensor decomposition model called the Tubal Tensor Train (TTT) and shows that it successfully mitigates the curse of dimensionality exhibited in the Tensor Singular Value Decomposition (T-SVD) model. The paper proposes two efficient algorithms to compute the TTT of an input higher-order tensor and conducts extensive simulations to show the efficiency of the approach on diverse tasks.

### Strengths
1. This paper introduces a new tensor decomposition model called the TTT, which mitigates the curse of dimensionality exhibited in the T-SVD model.

2. This paper proposes two efficient algorithms to compute the TTT of an input higher-order tensor, one is a fixed-rank version, the other is a fixed-precision version.

3. The proposed TTT model is shown to outperform TT-based model in terms of efficiency and accuracy on diverse tasks.

### Weaknesses
1. It is better to show an intuition behind TTT decomposition for better understanding.

2. In theory, why can TTT decomposition surpass TT decomposition? The theoretical analysis is insufficient.

3. It is better to report the error bar for the experimental results.

4. It is better to provide more SOTA baseline methods, rather than just TT decomposition.

5. The notation $\ast$ in Section 2 Definition 3 does not specify.

6. $I_N$ lost $I$ in the last few lines of Section 3.2.

### Questions
1. Why the compression ratio of the proposed method is lower than that of TT-based model in “News qcif” dataset?

2. You claim that “The key difference between the TT-SVD and the TTT-SVD is the first works on unfolded matrices, while the latter deals with reshaped form of the underlying tensors, which are of order three”. Thus, can a decomposition deals with reshaped form of the underlying tensors with order greater than three achieve even better performance?

### Soundness
2 fair

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The article presents a new tensor decomposition method called Tubal Tensor Train (TTT) decomposition. The method is an extension of the Tensor Train (TT) decomposition approach, where the Tensor Singular Value Decomposition (T-SVD) and T-product methods are used to decompose N-order tensors into two third-order and (N − 3) fourth-order core tensors. The approach is claimed to  mitigate the curse of dimensionality the T-SVD method suffers. Two algorithms are discussed for the computation of the TTT decomposition.  Several numerical results are presented on different datasets and applications  to illustrate the performance of the proposed method.

### Strengths
Strengths:
1. A novel tensor decomposition approach is presented for higher order tensors.
2. The proposed method used the T-product and T-SVD, and a decomposition of higher order tensor with approximation guarantees.
3. The pair presents various numerical results from different applications.

### Weaknesses
Weakness:
1. The presentation can be improved. The paper might be hard to follow for non experts.
2. The computational cost and scalability of the proposed method, and few other details are not clear.

### Questions
The paper presents an interesting new tensor decomposition approach, that extends the Tensor Train (TT) method. This might be interesting in applications where there are natural multi-dimensional correlations such as videos, genetics and others.

I have the following comments about the paper:

1. The presentation is difficult to follow and certain details about the method are not clear.

i.  Firstly, the main section 4 will be difficult to follow for readers unfamiliar with tensor methods, particularly the T-product. Currently, it is not clear how the factor tensors interact with each other to form the full N-order tensor. The T-product between 4th-order tensor and how to multiply a third tensor with a fourth order tensor contracted using T-product is not obvious.

ii. t is claimed that applying T-SVD to higher order tensors suffers from the curse of dimensionality problem . But this is not clear or obvious to readers and should be explained why this is the case, and how does TTT over come this issue.

iii. how to choose the TTT-rank vector for a given N-order tensor? Are these ranks unique for given tensor? Are they related to tubal rank corresponding to T-SVD?

iv. How do we show that the space of all tensors of TTT-rank no higher than a given r_k is closed?

v. What does best low TTT rank mean and how to compute this for a given tensor?

vi. Algorithm 1 output says,  an approximation with error tolerance \epsilon is returned. But this \epsilon is not an input parameter. How do we control the error? Perhaps this is a typo.

2. The computational cost and scalability of the proposed method is not clear.

3. In the numerical experiments, we things are not clear.

i. Why is the runtime of TTT less than the TT method? Shouldn't T-SVD computation be more expensive than SVD?

ii. The advantage of TTT in the applications considered is not really clear and seems a bit forced. Reshaping the images into 10th ordertensor seems strange, and the choice of the rank values in TTT-rank vector seems arbitrary. Wouldn't considering the images (in all 4 examples) as 3rd order tensors and just using T-SVD be good enough? Comparison with this approach of just treating the images and videos in the natural 3rd order form and using T-SVD would be interesting to show that TTT actives something different/better. 

iii. Why a 10-order tensor is considered and what happens to the performance if a lower order is chosen? 

Minor Comment:

i. Section 3.2, middle tensor if -->  middle tensor is

ii. Recently, \star_M product, a generalization of the T-product, where FFT is replaced by a general invertible matrix M has been proposed. Perhaps, TTT can be extended using this general version of the tensor product. For image applications, it has been shown that DCT matrix as M performs better than FFT.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies a new tensor decomposition model by combining tensor train (TT) decomposition and tensor SVD (T-SVD). Specifically, the authors replace tensor contractions in traditional TT with T-products defined in T-SVD. To compute the proposed TTT, the authors proposed two algorithms, which are analogous to TT-SVD and ATCU in previous literature of TT.

### Strengths
A new tensor decomposition is proposed with two algorithms for guaranteed low-rank approximation.

### Weaknesses
1. The motivation of the proposed model is not well presented. The authors stated TTT addresses the curse of dimensionality issue of T-SVD. But what is the advantage compared to TT and other tensor network structures?
2. The overall presentation is not clear enough. The preliminaries might be vague for readers not familiar with tensor decompositions. Moreover, the definition of the proposed model is not explicitly expressed. Besides, the review of related work is missing. 
3. The definition of the proposed TTT is not well presented and the example in Figure 2 is not clear. I hope the authors could give a general equation of the proposed TTT, including the dimension of each factor and the meaning of each dimension.
4. For empirical evaluations, the authors only compare with TT and T-SVD, both of which are very old and classical models. It should be encouraged to choose more recent baselines.
5. The authors proposed two algorithms, TTT-SVD and TACTU, but they did not claim which one was used for experiments. Moreover, they did not mention which algorithm was used for TT.

### Questions
1. What is the complexity of the proposed algorithm and comparison with previous algorithms?
2. In Figure 4, it seems that TTT discards color information for Kodim 15, Barbara and Airplane images. Can the authors give some insights on this?

**Minor:**
1. The notations or preliminaries are not adequately introduced, especially for readers who are not familiar with tensors. I suppose the authors use $\ast$ to denote the T-product. However, they did not introduce this notation explicitly.
2. The authors do not clearly define the modulo-T circular convolution in Definition 1.
3. The definition of frontal slices are not introduced in Definition 5.
4. In the first Equation of Section 3.1, the middle index of $X_{N-1}$ might be $i_{N-1}$.
5. In Figure 2 bottom subfigure, is the shape of the last factor $2 \times 1 \times 10$?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work proposed a new tensor network model called TTT, where the algebra is re-defined using vectors with t-product and element-wise sum. The effectiveness of the new model is numerically verified in the task of image restoration.

### Strengths
The TTT model is relatively new (although I find a similar idea from https://arxiv.org/pdf/2204.10229.pdf), and introduced clearly.

### Weaknesses
1. Although the performance is evaluated with experiments like image compression or completion, the superior performance of TTT is not convincing. More SOTA methods should be implemented.
2. Apart from the TTT model, nothing is new compared with the original TT. It would be good if the author could highlight the uniqueness from the existing models.
3. The writing should be carefully improved. For example, Definitions 3 and 4 define the identity and orthogonal tensors in the t-product context. But it should be clarified the ambiguity from the conventionally defined identity and orthogonal tensors.

### Questions
No more questions for this work.

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor
