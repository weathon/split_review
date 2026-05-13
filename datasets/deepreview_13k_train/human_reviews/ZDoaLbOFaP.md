# Sparse Covariance Neural Networks

- Decision: Reject
- Scores: 1, 3, 3, 5

## Abstract
Covariance Neural Networks (VNNs) perform graph convolutions on the covariance matrix of tabular data and achieve success in a variety of applications. However, the empirical covariance matrix on which the VNNs operate may contain many spurious correlations, making VNNs' performance inconsistent due to these noisy estimates 
and decreasing their computational efficiency.
To tackle this issue, we put forth Sparse coVariance Neural Networks (S-VNNs), a framework %pipeline 
that applies sparsification techniques on the sample covariance matrix before convolution. When the true covariance matrix is sparse, we propose hard and soft thresholding to improve covariance estimation and reduce computational cost. Instead, when the true covariance is %also 
dense, we propose stochastic sparsification where data correlations are dropped in probability according to principled strategies. We show that S-VNNs are more stable than nominal VNNs %their nominal dense counterparts 
as well as sparse principal component analysis. By analyzing %, and we analyze %model 
the impact of sparsification on their behavior, we provide %providing 
novel connections between S-VNN stability and data distribution.
We support our theoretical findings with experimental results on various application scenarios, ranging from brain data to human action recognition, and 
show an improved task performance, stability, and computational efficiency of S-VNNs %our approach 
compared with nominal VNNs.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
This paper builds upon covariance neural networks, which are constructed to process covariance matrices. The authors study the impact of sparsifying the covariance matrix with hard or soft thresholding before feeding it to the network. They demonstrate that this improves the estimation when the true covariance matrix is sparse, and explain how to drop coefficients at random when it is not the case. The authors demonstrate some improvements compared to no thresholding in several experiments.

### Strengths
- The idea of sparsifying the covariance before feeding it to the network is sound.

### Weaknesses
 - This paper is very hard to follow. Several variables are not defined ($V$, $u$, $u_g$, $h_{klfg}$, etc...). Several concepts must be guessed from the text (what are the covariance filters? how does $u$ relate to the $u_g$ in eq. 1? what are the per covariance filters in theorem 1?). Overall, it is hard to understand this paper alone without reading the original paper on covariance neural networks. This paper needs a major rewriting before being ready for publication, which explains my note.
- The novelty is minor. This paper builds upon covariance networks, which are seldom used in practice, and incrementally improves on them by pre-processing the covariances.


### Questions
- How can we know in practice if the covariance of the dataset is sparse?
- How does $\nu$ in thm.1 depends on the data distribution? I only see one data distribution, which depends only on $C$, so $\nu$ is only a function of $C$?
- In def. 1, is it for a fixed matrix? In which set do the eigenvalue pairs $\lambda_i, \lambda_j$ belong? This is unclear.
- Is lemma 1 an original result? If not then a citation is needed here.
- Should $F_{in} = F_{out}$ in (1)? since it seems like $u^l$ is both of size $F_{out}$ and $F_{in}$.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
**Summary:**
Graph convolutions on the covariance matrix of tabular data are performed by a architecture called Covariance Neural Networks (VNNs). These rely an empirical estimates of the covariance matrix, which is notoriously difficult. The authors propose Sparse VNNs, which sparsifies the covariance matrix before convolution is applied. This is advantageous when the true covariance is sparse, and also when the true covariance is dense, and different techniques are investigated. S-VNNs are compared against VNNs and PCA. Experiments are provided on brain data and human action reconition, showing performance, sensitivity and efficiency benefits over VNNs.

### Strengths
**Strengths:**
- The proposed architectures come with apparent theoretical guarantees on the closeness of hidden representations or predictions when applied to the approximate versus true covariance matrices. These distances become smaller as the number of samples increase, at a rate of $\mathcal{O}(t^{-1/2})$, ignoring some parameter-dpendent constants.
- Experiments are provided showing the predictive performance and stability of the proposed methods. This experiments agree with the theory, and nicely demonstrate the approach. 
- A very large amount of related literature is cited, and this seems appropriate.
- The theory appears to be mostly sound, roughly based on a Lipschitz assumption. (although there are some isolated places where precision could be improved, see weaknesses below).

### Weaknesses
 **Weaknesses:**
- Comparing Lemma 1 and Thoerem 1. I am guessing (please correct me if I am wrong!) that somehow hidden inside $\mathcal{O}$ in Theorem 1 are the parameters $\mathcal{H}$. Intuitively, these should learn something similar to PCA, and if the eigenvalues of PCA are close, this constant term in $\mathcal{O}$ will be bad but in terms of $\mathcal{H}$. In Lemma 1, the constant term in terms of the small gap eigenvalues is explicitly given, and it is obvious how this causes instability. Whether my guess about Theorem 1 is correct or not, the authors should state either way about the possibility of dependent of $\mathcal{H}$ on the factors in $\mathcal{O}$. Right now the claim that " VNNs do not suffer from this as the covariance filter can exhibit a stable response to close eigenvalues at the expense of lower discriminability" is not clear, as are similar repeated claims throughout the paper. It seems as though this is also an important consideration for later derived theoretical results (Theorem 2, Proposition 1, ...). **This is my most major important concern.**
- Theorem 1 explicitly writes the probability of the event. The later results only state with high probability. What does with high probability mean?
- In definition 3, how does one ensure that the resulting soft-thresholded matrix is PSD? 
- In definition 4, how does one ensure that the matrix is PSD after dropout? 
- What happens when the true data distribution is heavy tailed, and does not have a (finite) covariance matrix? I guess there should be some condition in the theoretical results, which is currently absent, on the distribution of $x$. In Theorem 1 a Gaussian distribution is used (which has finite variance), and it is not clear in the presentation of later results if a Gausssian is also being used. 
- It is claimed that "For sparse covariance, ... the hard thresholding improves stability." According to my understanding, the authors are able to derive bounds which are tighter for sparse covariances than for dense covariances with hard thresholding. This does not necessarily show that hard thresholding definitively improves stability, only the bound is tighter. If I have understood correctly, perhaps the authors should rephrase their claim (otherwise, am happy to be corrected).


**Minor:**
- I don't understand one sentence in Theorem 1. "Consider a generic data sample $x \sim \mathcal{N} (0, C)$ such that $\Vert x \Vert \leq 1$". Does this mean $x$ is drawn from the conditional distribution obtained by conditioning a Gaussian random vector on the event that the norm is less than or equal to 1? I believe this should be phrased better, in terms of the distribution x is actually drawn from. (I understand this is from another paper, but still it would be nice to improve clarity here).
- Incorrect grammar for paragraph starting line 167/168.
- Limitations of PCA in terms of unstable or poor estimation of eigenvalues is discussed. Do the authors know where does this fit into more robust variants of PCA, exponential family PCA, kernel PCA, etc.? Do such advanced variants of PCA overcome these issues? Either way, it would be nice to mention in the discussion in a sentence around line 39/40.

### Questions
Please address each of the weaknesses above. In particular:
- In Theorem 1 and related results, is it true that $\mathcal{O}$ hides dependence on $\mathcal{H}$, which as in the case of PCA, could be arbitrarily bad?
- What does with high probability mean exactly?
- How are matrices ensured to be PSD?
- What happens in the case of undefined / infinite variance? How should this be reflected in the theorems? Is a Gaussian assumption on x used throughout, or only in the first result?
- Does the theoretical result really show a guaranteed improvement in stability? Or does it only fail to show a decrease in stability?
- Please clarify whether $x$ is drawn from an (unconditional) Gaussian or from a "truncated" Gaussian conditioned on its norm.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a sparse version of covariance neural networks (VNNs), showing that the sparse-VNNs are more stable than nomial VNNs and sparse component analysis.

### Strengths
The presentation of the paper is clear.

### Weaknesses
1. It is well known that the covariance matrix is not invariant to the scale of the data, making it impractical to set a common threshold for different elements of c_{ij}. Specifically, the magnitude of covariance values is directly influenced by the variance of the input features. Features with larger variances will naturally exhibit larger covariance values, regardless of their true underlying relationship. Therefore, applying a single threshold across all elements, as proposed in Definition 2, is problematic because it does not account for these inherent differences in scale. This could lead to the incorrect removal of meaningful connections between features with high variance, while retaining spurious connections between features with low variance. The rationale behind Definition 2 is therefore difficult to justify without a clear explanation of how the data is preprocessed to address this issue.

2. From a sparsity perspective, the elements c_{ij}'s should be classified into two categories: zero and nonzero. However, this key point is obscured in Theorem 2, making the results difficult to interpret. The theorem's focus on bounding the number of non-zero elements per row, while relevant to sparsity, does not directly address the fundamental question of whether the thresholding process effectively distinguishes between true signal (non-zero covariances) and noise (zero covariances). In other words, it is challenging to justify that the proposed method effectively denoises the data, as the thresholding criteria may not accurately identify and remove spurious correlations.

3. The contribution of the paper appears incremental in light of the existing work by Sihag et al. (2022).

### Questions
1. See weakness. 

2. Additionally, using t to represent the sample size is somewhat unusual to me, though this is merely a notation issue.

### Soundness
2

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
4

### Summary
This paper studies the sparsification strategy upon the spurious correlation and computation efficiency issues for the covariance matrix used in the coVariance Neural Networks (VNN), which is more stable than the Principal component analysis (PCA) methods in the previous studies. This paper proposes hard and soft thresholding strategies if the true covariance matrix is sparse, and two stochastic sparsification techniques, including Absulute covariance values (ACV) and Ranked covariance values (RCV) when the covariance matrix is dense, and theoretically analyze the sparsification error and covariance uncertainty for the stability of VNN. The effectiveness of sparsity techniques is validated through synthetic and real datasets in contrast to the dense-VNN and sparse-PCA on the performance and computational time.

### Strengths
Quality: The paper is well-written, the motivation sounds reasonable, and the proposed sparsification strategies seem good with a theoretical analysis of the stability.
Originality: The paper proposes several sparsification strategies to tackle the spurious correlation and computation cost issues for the VNN. Although the theoretical analysis of the stability of VNN is good, the originality of the proposed solutions is limited. 
Significance: Spurious correlation and sparsity techniques are important.

### Weaknesses
The novelty of the proposed strategies is limited, similar strategies have been used in the study of neural networks like dropout or pruning, and the current results are not enough strong. The core contribution seems to stem from the increased number of zero terms in the covariance matrix, leading to computational speedup, rather than a fundamentally novel approach to covariance estimation or VNN training. The stability analysis, while present, feels like a necessary justification for the random sparsification rather than a core contribution in itself. The empirical results, while validating the effectiveness of the proposed strategies, lack a more rigorous comparison with alternative methods that directly enforce sparsity during covariance matrix estimation.

Although current results can validate the effectiveness of the proposed strategies, the results should be compared with the covariance with sparsity regularizer, not just dense-VNN and robust-PCA. Specifically, the comparison should include methods that obtain a sparse covariance matrix through L1 regularization or similar techniques during the covariance estimation process, rather than relying solely on post-hoc thresholding or random selection.

### Questions
Although current results can validate the effectiveness of the proposed strategies, the results should be compared with the covariance with sparsity regularizer, not just dense-VNN and robust-PCA.

### Soundness
3

### Presentation
3

### Contribution
2
