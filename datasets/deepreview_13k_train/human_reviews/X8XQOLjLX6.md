# Autoencoders for Anomaly Detection are Unreliable

- Decision: Reject
- Scores: 6, 3, 3, 6

## Abstract
Autoencoders are frequently used for anomaly detection, both in the unsupervised and semi-supervised settings. They rely on the assumption that when trained using the reconstruction loss, they will be able to reconstruct normal data more accurately than anomalous data. Some recent works have posited that this assumption may not always hold, but little has been done to study the validity of the assumption in theory. In this work we show that this assumption indeed does not hold, and illustrate that anomalies, lying far away from normal data, can be perfectly reconstructed in practice. We extend the understanding of autoencoders for anomaly detection by showing how they can perfectly reconstruct out of bounds, or extrapolate undesirably, and note how this can be dangerous in safety critical applications. We connect theory to practice by showing that the proven behavior in linear autoencoders also occurs when applying non-linear autoencoders on both tabular data and real-world image data, the two primary application areas of autoencoders for anomaly detection.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper examines the limitations of Autoencoders for anomaly detection from a theoretical perspective. It explores approaches including PCA, linear Autoencoders, non-linear Autoencoders, and Convolutional Autoencoders, using synthetic tabular data and the MNIST dataset. The study demonstrates that under certain conditions, anomalies can yield zero or low reconstruction errors in autoencoders, leading to the conclusion that reconstruction loss may not reliably indicate anomalies.

### Strengths
- The paper presents a novel and intriguing perspective by questioning the use of autoencoders for anomaly detection theoretically.
- Analysis is conducted through both theoretical exploration and practical examples using synthetic data and MNIST.
- Figure 1 results are well-illustrated and offer interesting findings.

### Weaknesses
 - Although this work highlights the limitations of autoencoders for anomaly detection, it may not fully address practical cases where anomalies come from out-of-class data or shifts in distribution, which differ from the conditions presented. For instance, in Figure 2, some examples show failure cases in convolutional autoencoders, but in many regions, reconstruction errors appropriately increase as the distribution shift grows. Specifically, in Figure 2(a), the presence of low reconstruction errors might be reasonable, as these cases are close to the normal training data and could be considered examples of generalization. The analysis does not sufficiently explore the boundary between acceptable generalization and problematic low reconstruction errors for true anomalies. The paper would benefit from a more detailed discussion on how the observed phenomena scale with more complex datasets and higher dimensional input spaces, as the current analysis is limited to relatively simple synthetic data and MNIST.


### Questions
* Could the authors provide more discussion about how the conclusion can be generalized in the out-of-class anomalies or other potential realistic distribution shifts or anomaly cases?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper demonstrates that using auto-encoder reconstruction loss is an ineffective metric for anomaly detection. It argues that it is possible to generate instances that lie on the PCA hyperplane yet are still anomalous.

This argument is valid and straightforward to illustrate. Intuitively, the PCA hyperplane has an infinite volume, whereas the volume occupied by normal examples is finite. Therefore, there must exist points on the PCA hyperplane that are anomalous. The same reasoning applies to non-linear auto-encoders as well.

The authors then extend their conclusion to state that "Auto-encoders are unreliable for anomaly detection." However, this generalization is incorrect because the unreliability stems from the authors' application of PCA rather than the PCA methodology itself.

The core assumption of PCA is that there is an underlying multivariate Gaussian distribution. Consequently, PCA provides variance estimates along the principal components (the eigenvalues). These variance estimates can be utilized to calculate likelihoods, which are valuable for anomaly detection.

Other autoencoders either output variance directly (such as VAEs) or allow for the estimation of variance and covariance through multiple examples.

The unreliability of reconstruction error for anomaly detection, as discussed by the authors, arises from disregarding the variance information provided by PCA, not from the PCA process itself.

Many anomaly detection studies employ autoencoders and model the latent space with Gaussian assumptions without encountering the issues highlighted in this paper. Examples include:

Tipping, M. E., & Bishop, C. M. (1999). "Probabilistic Principal Component Analysis."
Archambeau, C., et al. (2007). "Anomaly Detection with Robust Deep Autoencoders."
Xie, J., Girshick, R., & Farhadi, A. (2016). "Unsupervised Deep Embedding for Clustering Analysis."

Although I find the mathematical foundations and arguments presented in the paper to be sound. However, the arguments whereby auto-encoders are unreliable, are not sound.

### Strengths
+ Mathematical notations and flow are sound.

### Weaknesses
The core argument of this paper is that auto-encoder reconstruction loss is an ineffective metric for anomaly detection, which is demonstrated by showing that points can lie on the PCA hyperplane yet still be anomalous. This argument is valid, as the PCA hyperplane has an infinite volume while the normal data occupies a finite volume. The same logic applies to non-linear autoencoders. However, the authors incorrectly generalize this to state that "Auto-encoders are unreliable for anomaly detection." This conclusion is too broad, as the unreliability stems from the specific use of reconstruction error, not from the autoencoder methodology itself. The fundamental assumption of PCA is that the data can be represented by a lower dimensional linear subspace, which can be used to estimate variance along the principal components. These variance estimates can then be used to calculate likelihoods, which are valuable for anomaly detection. The authors' argument fails to acknowledge that other autoencoders, such as VAEs, either output variance directly or allow for the estimation of variance and covariance through multiple examples. The unreliability of reconstruction error for anomaly detection arises from disregarding the variance information provided by PCA, not from the PCA process itself. Many anomaly detection studies successfully employ autoencoders and model the latent space with Gaussian assumptions without encountering the issues highlighted in this paper. Examples include:

Tipping, M. E., & Bishop, C. M. (1999). "Probabilistic Principal Component Analysis."
Archambeau, C., et al. (2007). "Anomaly Detection with Robust Deep Autoencoders."
Xie, J., Girshick, R., & Farhadi, A. (2016). "Unsupervised Deep Embedding for Clustering Analysis."

While the mathematical foundations and arguments presented in the paper are sound, the generalization that auto-encoders are unreliable is not.

### Questions
.

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper discusses that an autoencoder may reconstruct anomalies even though the anomaly resides very far from the training data. Their analysis starts with the linear case, i.e., PCA, and then is extended to neural networks, showing that an autoencoder can give a very small reconstruction error for outliers. However, the paper does not provide a solution to remedy this phenomenon.

### Strengths
* The paper discusses the under-appreciated problem of the autoencoder being capable of generating anomalies when applied to anomaly detection.
* The overall exposition of the paper is clear and easy to follow.

### Weaknesses
 * The paper only reports the problem but not a solution. The contribution of the paper is questionable, as the unexpected reconstruction of anomalies by an autoencoder was mentioned and studied several times in previous works. According to line 427 of the manuscript, this work is not the first to report the reconstruction of anomalies.
* There are missing references that reported and discussed the anomaly reconstruction phenomenon.
    * https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial9/AE_CIFAR10.html#Out-of-distribution-images
    * Autoencoding under normalization constraints https://arxiv.org/abs/2105.05735 and references therein. Their appendix contains analyses similar to those provided by the manuscript.
    * Outlier reconstruction web demo https://swyoon.github.io/outlier-reconstruction/
* The value of the analyses provided by the paper is not clear. Most sections are dedicated to simply showing the existence of reconstructed anomalies, which is somewhat trivial. The analyses do not lead to deeper insight, which can be used to build better anomaly detection algorithms.

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explains that when autoencoders (AEs) are used for anomaly detection, their reliability can be compromised because they may reconstruct data outside of the training dataset. First, this paper proves that PCA and linear AE can reconstruct data not included in the training dataset. Then, it demonstrates that this issue also occurs in nonlinear cases and when using convolutional layers.

### Strengths
- This paper theoretically and visually demonstrates that autoencoders can reconstruct data that is not included in the training dataset.

### Weaknesses
 - I am unclear about the novelty of this paper. Please refer to the Questions section.



### Questions
- Could you tell me the contributions of this paper? The paper theoretically proves that PCA and linear autoencoders (AEs) can reconstruct anomalies, but does this qualify as novelty? This issue is widely known, and for example, [1] demonstrates that variational autoencoders (VAEs) cause this problem. Although there may be probabilistic or deterministic differences, I believe that AEs are a special case of VAEs, so this should be mentioned in the paper. From the perspective of probabilistic models like VAEs, for instance, [2] provides a theoretical explanation of this problem. Could you explain the relationship between these previous studies and this paper?

- For example, in the case of VAEs, this issue can be mitigated by using hierarchical models as in [3] or by employing ensembles as in [4]. For autoencoders, this problem can be mitigated by restricting latent variables as in [5] or by normalizing the latent space by considering it as an Energy-Based Model (EBM), as in [6]. In this paper, specific anomalies that can potentially be reconstructed are identified. Based on these insights, could you propose any ideas on how to mitigate this issue?

[1] Nalisnick, Eric, et al. "Do deep generative models know what they don't know?." arXiv preprint arXiv:1810.09136 (2018).

[2] Fang, Zhen, et al. "Is out-of-distribution detection learnable?." Advances in Neural Information Processing Systems 35 (2022): 37199-37213.

[3] Havtorn, Jakob D., et al. "Hierarchical vaes know what they don’t know." International Conference on Machine Learning. PMLR, 2021.

[4] Choi, Hyunsun, Eric Jang, and Alexander A. Alemi. "Waic, but why? generative ensembles for robust anomaly detection." arXiv preprint arXiv:1810.01392 (2018).

[5] Zhou, Yibo. "Rethinking reconstruction autoencoder-based out-of-distribution detection." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022.

[6] Yoon, Sangwoong, Yung-Kyun Noh, and Frank Park. "Autoencoding under normalization constraints." International Conference on Machine Learning. PMLR, 2021.

### Soundness
2

### Presentation
3

### Contribution
2
