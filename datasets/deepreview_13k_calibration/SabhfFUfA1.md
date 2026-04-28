# Inference, Fast and Slow: Reinterpreting VAEs for OOD Detection

- Decision: Reject
- Avg Score: 4.67
- Scores: 5, 3, 6

## Abstract
lthough likelihood-based methods are theoretically appealing, deep generative models (DGMs) often produce unreliable likelihood estimates in practice, particu larly for out-of-distribution (OOD) detection. We reinterpret variational autoen coders (VAEs) through the lens of fast and slow weights. Our approach is guided by the proposed Likelihood Path (LPath) Principle, which extends the classical likelihood principle. A critical decision in our method is the selection of statistics for classical density estimation algorithms. The sweet spot should contain just enough information that’s sufficient for OOD detection but not too much to suffer from the curse of dimensionality. Our LPath principle achieves this by selecting the sufficient statistics that form the "path" toward the likelihood. We demonstrate that this likelihood path leads to SOTA OOD detection performance, even when the likelihood itself is unreliable.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper introduces the LPath algorithm for OOD detection. LPath operates in two stages: first, it trains a VAE on in-distribution data and extracts key statistics from the fast weights related to the reconstruction error and latent variables; second, it applies classical density estimation methods to these statistics for OOD detection. The key idea is that the computational path to the likelihood function contains more informative details than the likelihood alone. The method is demonstrated on some simple datasets.

### Strengths
- The paper addresses a crucial problem in machine learning: the need for reliable OOD detection, particularly in safety-critical applications. The proposed “LPath Principle” and its application to VAEs offer a promising direction for improving OOD detection performance.

- The paper presents a new perspective on OOD detection by reinterpreting VAEs through the lens of fast and slow weights in an interesting manner. The authors also demonstrate originality by pairing two VAEs with different latent dimensions to address the trade-off between encoder and decoder performance for OOD detection.

- The paper provides a thorough analysis of the LPath Principle, examining it from different perspectives. The authors ground their approach in well-established statistical principles. The combinatorial analysis, while the explanation is lacking a bit of clarity, seems to be well motivated.

### Weaknesses
### Communication
* The paper is not an easy read as it quickly gets rather convoluted. For example, some efforts are spent on talking about "slow and fast weights", but it is unclear how this concept is related to the actual work. The actual work seems to be about sufficient statistics, so it seems like a detour to talk about "fast and slow weights". I may have missed an important insight here, but I do not see what the fast-and-slow-analogy brings to the table (beyond confusion for this reader).
* Another example of convoluted writing is that the method is motivated by the proposed "likelihood path" principle in Sec 3, but this principle is only discussed in Sec 4. It feels to me like the order of presentation is unconstructive. (I understand that such comments are fundamentally subjective, but I, at least, found the presentation confusing).
* The phrased likelihood path principle is imprecise: the first sentence say that there is "more information", but it does not say relative to what. It does not help that the principle is repeated three times throughout the paper.

### Conceptual
* The paper presents a fairly broad principle and argues based on the idea that $T$ is a sufficient statistic for the marginal likelihood. This, however, appears incorrect. $T$ is, as far as I can tell, a sufficient statistics for the one-sample-estimate of the marginal likelihood, but this is a notoriously different quantity than the marginal likelihood. Pragmatically, I understand why the one-sample-estimate is considered, but I find it troublesome that this is not more elaborately discussed, and instead the paper largely talks about the one-sample-estimate as being the marginal likelihood.
* Following the point above, then equations 23 and 24 appear incorrect. They would be correct for the ELBO or the one-sample-estimate of the marginal likelihood, but they are incorrect for the marginal likelihood (which is what the equations state).

### Questions
N/A

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper considered out-of-distribution (OOD) detection using variational autoencoders (VAEs). The idea is essentially to represent each data point with $T(x) = [\mu_z(x), \sigma_z(x), \mu_x(z), \sigma_x(z)]$, i.e. with the mean-variance pairs of both encoder and decoder. A density estimate is then formed on the training data $T$, and OOD detection is done with respect to this density estimate. Empirical results appear promising.

The approach is justified through a newly phrased "Likelihood Path" principle, which is linked to both the likelihood principle and information theory.

### Strengths
* I think the key idea of extracting sufficient statistics per data point and doing OOD detection in a density of these is neat.
* Empirical performance suggests that the approach has some merit.

### Weaknesses
As illustrated in Table 1, the performance improvement of the proposed algorithm is not substantial when compared to other competitors. In some instances, its performance is even inferior to other state-of-the-art (SOTA) methods. Specifically, while the proposed LPath method achieves competitive results, it does not consistently outperform existing methods across all datasets and OOD scenarios. The gains are marginal in many cases, and in some instances, such as the comparison with DDPM on certain datasets, the performance is noticeably lower. Furthermore, the datasets used in the experiments are all small in size. Consequently, the benefits of the proposed likelihood path principle and the associated algorithms have not been fully demonstrated. It remains uncertain whether the proposed concept and algorithm would be effective in more complex real-life scenarios. The limited scale of the datasets raises concerns about the generalizability of the findings to more challenging, high-dimensional data.

### Questions
* I like that the approach works well with small models. Have you tried using your approach on larger models?
* Is the approach applicable to hierarchical VAEs? Since these have many latent variables, I assume $T$ becomes rather large, which may render the approach impractical. Do you have any experiences with this?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a novel VAE-based approach for unsupervised OOD detection. The core idea is to utilize the sufficient statistics generated during the encoding and decoding processes of a VAE as features for classical OOD detection algorithms, such as COPOD (Li et al., 2020) or MD (Lee et al., 2018; Maciejewski et al., 2022). The authors also propose a method to address the trade-off in selecting the latent dimension. This involves using two VAEs, one with a high latent dimension and the other with a lower one. The performance of the proposed method is empirically evaluated on benchmark datasets. The results demonstrate that the proposed method can achieve performance comparable to existing state-of-the-art approaches while maintaining a smaller model size.

### Strengths
1. This paper is well written in presenting the proposed idea and algorithm, and is very easy to follow. 

2. The performance of the proposed algorithm is empirically demonstrated by comparing to existing SOTA approaches. It's shown that this method performs on par with others using smaller models.

### Weaknesses
As illustrated in Table 1, the performance improvement of the proposed algorithm is not substantial when compared to other competitors. In some instances, its performance is even inferior to other state-of-the-art (SOTA) methods. Furthermore, the datasets used in the experiments are all small in size. Consequently, the benefits of the proposed likelihood path principle and the associated algorithms have not been fully demonstrated. It remains uncertain whether the proposed concept and algorithm would be effective in more complex real-life scenarios.

### Questions
1. The proposed LPath principle and algorithm are presented in a context of Gaussian VAE. Is it possible to extend them to Gaussian mixture VAE or hierachical VAE? By doing so, likely it can improve the OOD detection performance, while at a cost of increasing the model size.  

2. As shown in Table 1, for some cases, DDPM performs much better than the proposed methods. Why? Is it because the model capacity of proposed algorithm is too small compared to DDPM? How about enlarging its model size, then compare it again with DDPM? 

Some minor issues: 

pp.122-123,  the equation needs to be revised

pp.226,  "While VAE optimization should already be driving Eqs. 17–19 to a small value", why?

pp.893, Theorem ??

### Soundness
3

### Presentation
3

### Contribution
3
