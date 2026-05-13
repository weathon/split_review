# On the Positive Definiteness of the Neural Tangent Kernel

- Decision: Reject
- Scores: 3, 6, 5, 3

## Abstract
The Neural Tangent Kernel (NTK) has emerged as a fundamental concept in the study of wide Neural Networks. In particular, it is known that the positivity of the NTK is directly related to the memorization capacity of sufficiently wide networks, i.e., to the possibility of reaching zero loss in training, via gradient descent.  
Here we will improve on previous works and obtain a sharp result concerning the positivity of the NTK of feedforward networks of any depth. More precisely, we will show that, for any non-polynomial activation function, the NTK is strictly positive definite.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper analyzes the positive definiteness of the neural tangent kernel, which is the inner product of the gradient of the network function w.r.t. the weights in the infinite limit of the width. Compared to the previous work (Du et al. 2019), this paper shows that the activation function does not need to be analytic but being continuous and differentiable a.e. is sufficient to prove the result.

### Strengths
This paper gives a nice introduction to the background of the neural tangent kernel and its importance. The proof is well presented and is easy to follow.

### Weaknesses
1. The contribution made in this paper appears incremental. Compared to previous work, it relaxes the condition on the activation function from analytic to continuous and differentiable almost everywhere. While proving the positive definiteness of the NTK is an interesting theoretical question, the practical implications of this relaxation are not thoroughly discussed, and its significance to the broader ICLR community might be limited.

2. Theorem 1 seems to have an oversight. The NTK is not positive definite if two data samples are identical. The authors need to explicitly state the condition that data samples must be distinct.

3. Section 2.1 is unclear in its purpose. It dedicates considerable space to discussing results that do not satisfy the conditions of Theorem 1, where the activation function is assumed to be  $C^{N-1}$. The relevance of this section to the main result is not well established. Furthermore, a similar discussion is repeated at the end of page 5, which adds redundancy.

4. In the proof of Theorem 4, the statement "with the $z_i$ pairwise distinct and $\beta \neq 0$, in the view of Theorem 3..." is not entirely accurate. Theorem 3 requires the data to be totally non-aligned, and being pairwise distinct is not a sufficient condition to satisfy this requirement. This needs further clarification.

5. The discussion on the presence or absence of bias seems to be a minor point. The authors correctly point out that with bias, x can be viewed as $[x,1]$. Therefore, the condition of x being pairwise non-proportional can be reframed as [x,1] being pairwise distinct. This observation could be integrated more concisely into the main arguments.

### Questions
I didn't follow the proof of Proposition 1. ''under the previous circumstances, $\sigma$ must be a constant. I am unclear about the mentioned circumstances and how to see that $\sigma$ is a constant.

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper is dedicated to sufficient conditions for the positive definiteness of NTK. It is proved that the architecture with a bias term and a non-polynomial activation function automatically leads to positive-definite NTK. The proof is based on Theorem 3, which states that functions sigma(a[i]x+b[i]y), i=1,...,n are linearly independent if [a[i],b[i]] is not a multiple of [a[j],b[j]] for all i,j and sigma is not polynomial. An easy proof of Theorem 3 is given for the case when sigma is many times differentiable. In the appendix, a more elaborate proof is given for a general case. To avoid differentiability finite differences are analyzed instead. Then a case of an architecture with only one hidden layer becomes quite straightforward. A general case is treated in Proposition 1, in which it is proved that positive definiteness of NTK for lower layers inductively guarantees positive definiteness of NTK for the next layer. 

Major claims seem correct, proofs are convincing. The paper is purely theoretical. A major weakness is a lack of deeper discussions about what these results give us for a better understanding of NNs.

Minor correction on page 1: as emerged -> has emerged

### Strengths
Mathematically clean, at least from the first site I could not find any issues.

### Weaknesses
There is no any discussion of proved results in the context of NTL theory. The fact that positive definiteness is somehow related to memorization is only mentioned. Also, experimental part is absent.



### Questions
Non-polynomiality of activation function also plays a key role in Universal approximation theorem as was probed by Moshe Leshno et al in 1993 and later Allan Pinkus in 1999. So a natural question is how it is related to the proved property that non-polynomiality leads to positive definiteness of NTK?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper analyzes the neural tangent kernel at the infinite width limit. It shows that NTK is strictly positive definite, as long as the activation function is not a polynomial and data is non-degenerate (pairwise non-proportional, if no bias). The major technique it uses is Theorem 3, about a characterization of polynomial functions.

### Strengths
The main results of this paper require milder assumptions than prior works. Particularly, it does not require the unit sphere data assumption. Compared to Du et. al. 2019, it also does not require the activation function to be analytic.

The paper is clearly written. Main techniques are highlighted, so that intuitions can be easily seen.

### Weaknesses
My concern is on the significance of the results and the technical novelty. 
Similar results/claims already exist with a little bit stronger assumptions. For example, Du et. al. 2019 showed the same thing, just additionally required unit sphere data, and analytic activation functions. I am afraid this improvement in this paper is not enough to meet the ICLR acceptance standard.

In addition, most parts of the proofs (except the application of Theorem 3) in the main content are common treatments which can be found easily in literature. It seems a bit tedious for those who are familiar with the topic. Theorem 3 seems a bit novel (at least to my knowledge), but not technically hard to prove. Hence, I also have concern on the significance of technical novelty.

### Questions
no further questions

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the minimum eigenvalue of the neural tangent kernel (NTK), which is an essential problem for analyzing the convergence and generalization of over-parameterized neural networks. They have two main results. First, for a multi-layer network with activated biases and a continuous, differentiable, and non-polynomial activation function, the NTK is positive definite. Second, for a multi-layer network without bias and a continuous, differentiable, and non-polynomial activation function, if the training data points are pairwise non-proportional, then the NTK is positive definite.

### Strengths
The paper's results improve on previous results in two ways: first, they apply to more general activation functions; second, they do not require strong assumptions on the training data. The paper is well-written, with clear statements of the theorems and rigorous proofs.

### Weaknesses
My main concern with this paper is the usefulness of its results. First, the two results only show that the minimum eigenvalue of the kernel is non-zero. However, to analyze the convergence rate of over-parameterized neural networks, we need an explicit bound on the minimum eigenvalue in terms of the network parameters. Therefore, by combining the results with convergence theory, we can only deduce that gradient descent on those neural networks will minimize the training loss to zero. However, we still do not know the training costs. Second, in recent years, many works have pointed out the limitations of NTK and infinite-width neural networks. To apply the NTK theory, we may assume that the width should be $m=\Omega(n^4)$, which is too impractical. Therefore, this paper may only have a limited broader impact on the deep learning theory community.

### Questions
Some typos:

P3: “As mentioned above We generalize”: “We”->”we”

P7, $K_X^{(2)}$: an extra “)”

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
