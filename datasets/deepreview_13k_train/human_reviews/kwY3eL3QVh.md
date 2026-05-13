# Feature-guided score diffusion for sampling conditional densities

- Decision: Reject
- Scores: 6, 8, 5, 3

## Abstract
Score diffusion methods can learn probability densities from samples. The score of the noise-corrupted density is estimated using a deep neural network, which is then used to iteratively transport a Gaussian white noise density to a target density. Variants for conditional densities have been developed, but correct estimation of the corresponding scores is difficult.
We avoid these difficulties by introducing an algorithm that guides the diffusion with a projected score. The projection pushes the image feature vector towards the feature vector centroid of the target class. 
The projected score and the feature vectors are learned by the same network. Specifically, the image feature vector is defined as the spatial averages of the channels activations in select layers of the network. 
Optimizing the projected score for denoising loss encourages image feature vectors of each class to cluster around their centroids. It also leads to the separations of the centroids. We show that these centroids
provide a low-dimensional Euclidean embedding of the class conditional densities. 
We demonstrate that
the algorithm can generate high quality and diverse samples from the conditioning class.
Conditional generation can be performed using feature vectors interpolated between those of the training set, demonstrating out-of-distribution generalization.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel guided score-based diffusion model that does not require any additional structural modifications. Instead, it extracts features from key layers of its own score estimation model (i.e. Unet) and applies spatial averaging, enabling guidance control in the feature space. Unlike methods such as classifier-free guidance, this feature-guided diffusion does not rely on likelihood estimation, allowing for a more accurate estimation of conditional density.

### Strengths
1. The paper is well-structured, easy to read, and highly innovative, introducing a projected score embedded in feature space. This embedding is not only straightforward to obtain (directly extracted from the score estimation model) but also adheres to Euclidean interpolation properties.

2. The model successfully achieves conditional generation in a mixture of Gaussian distributions, demonstrating that the feature-guided score diffusion model can accurately capture conditional density—an ability lacking in many other approaches.

3. Compared to mixture models, the feature-guided score diffusion model shows stronger concentration and separation across different classes within the embedding space.

### Weaknesses
The dataset used in experiments is overly simple. The training dataset is derived by cropping 1700 images into 234k patches. Although the patches are non-overlapping, the data distribution for each class lacks sufficient diversity. Experiments on a more complex dataset, like ImageNet, would strengthen the paper’s validity. The use of cropped patches, even if non-overlapping, introduces artificial correlations within the training data, potentially leading to an overestimation of the model's generalization capabilities. Specifically, the model might learn to exploit the local context within these patches rather than capturing the global structure of the underlying classes. This is further exacerbated by the relatively small number of original images (1700), which limits the overall variability in the training set, making it difficult to assess the true robustness of the proposed method. The lack of diversity in the training data makes it challenging to determine if the model's performance is due to genuine feature learning or simply overfitting to the limited variations present in the cropped patches. This raises concerns about the practical applicability of the method to real-world scenarios with more complex and diverse data distributions.

### Questions
1. What is the difference between feature space and latent space in stable diffusion? While the latter requires an additional encoder, how does the former feed $x$ and $x'$ into the U-Net?

2. In Fig. 3 (left), the feature-guided model shows strong performance across all noise levels. Does this suggest that fewer NFE (Number of Function Evaluations) could be used during conditional generation? Designing experiments to verify this could strengthen the paper.

3. In Fig. 4 (middle), were the two metrics normalized? Otherwise, this comparison might not be on the same scale. Additionally, the variance in image feature vectors appears large—is this due to insufficient training? Please clarify further.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a guided score diffusion method that samples from class conditional distributions by calculating a projected score based on feature vectors, avoiding the need to directly estimate the scores of those densities. The method employs a neural network trained to minimize a single denoising loss, with the feature vector defined as spatial averages from selected layers, leading to a Euclidean embedding of class conditional probabilities. It effectively clusters learned features around their centroids, allowing for accurate sampling from target conditional distributions and facilitating smooth transitions between classes through linear combinations of mean feature vectors.

### Strengths
This is a well-written paper. Both score and feature vectors are represented with the same network. The learned feature vectors cluster around their centroids, which enhances the accuracy of sampling rom the conditional probability density. The method enables gradual transitions of the images between classes through linear interpolation of mean feature vectors. The experimental results show that a diffusion algoriothm based on the projected score provides an accurate sampling of conditional probabilities.

### Weaknesses
The authors provided a way to build the feature vectors that share the same network weights as the score function. It is not clear how to determine the feature vector dimension.

### Questions
How does the feature dimension affects the learning and generation?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The most common approach to guide diffusion models is by using score guidance, whether in the form of classifier guidance or in the form of classifier free guidance. The paper claims that this approach relies on an approximation and is thus inaccurate. As an alternative, it proposes a simple method for training a conditional diffusion model. The approach is motivated intuitively and tested empirically.

### Strengths
- Classifier free guidance (CFG) is the most dominant approach for guiding diffusion models today, even though it is known to lead to biased densities. Several recent papers analyzed the drawbacks of the approach from a theoretical standpoint. However the topic of designing good practical alternatives to CFG is still under-explored. This paper attempts to fill this gap, which is undoubtedly an important goal.
- The paper presents clear intuition and empirically validates that the assumptions underlying the proposed construction hold.

### Weaknesses
 - The whole motivation of the paper is to propose an alternative to existing guidance methods. However, it does not provide theoretical guarantees that the approach samples from the conditional distribution. And it also does not provide any empirical evidence that the proposed approach outperforms the standard way of conditioning diffusion models. Specifically, it does not compare the sampling quality to that obtained with a conditional denoiser (with the common conditioning mechanism for U-Nets), neither without nor with CFG. It also does not present any quantitative measure of sample quality (e.g. FID) on natural images, and does not present results on popular datasets like CIFAR or ImageNet, which prevents from evaluating whether the proposed method leads to SOTA results. As such, it is impossible to evaluate the effectiveness of the proposed method.
- I believe that the motivation presented in the paper is inaccurate and somewhat misleading. Using score guidance (as in Eq. (4)) should theoretically lead to accurate results. What is inaccurate in CFG is that when taking the guidance parameter w to be greater than 1, it does not sample from the titled distribution p(x)p(y|x)^(1+w) from which it attempts to sample, but rather from a different distribution. See for instance the closed form expressions for the Gaussian setting in [1] (Eqs. (11),(12)), where the distributions of samples obtained with CFG-DDPM and CFG-DDIM are incorrect only when the CFG parameter (gamma) is greater than 1, but are correct when it equals 1. In particular, the statement in L147-148 that Chidambaram et al. (2024) proved the inaccuracy of guidance on Gaussian mixtures is incorrect. They proved the inaccuracy of CFG only when the guidance parameter w is sufficiently large. When w=1 the process is theoretically accurate.

### Questions
- Can the authors comment on how the method compares to regular guidance on common datasets, like CIFAR-10, in terms of FID?
- Can the authors comment on the motivation for suggesting an alternative to regular guidance (second weakness stated above)?
- L216: Why are the activation layer averages close to the first principal components of the network channels? Can the authors provide a proof or a reference to a paper showing this?

Typos:
- L216: principle -> principal
- L360: "some some"
- L429: missing parentheses around (m2-m1)
- L517: remove "And most"
- L518: mixeed -> mixed

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper focuses on the problem of conditional generation with diffusion models, and specifically class-conditional generation. The authors claim that commonly used class-conditional sampling methods are inexact, and thus propose a new method for class-conditional sampling with diffusion models. Their method, taking inspiration from a GMM distribution, attempts to train a diffusion model that is biased to a certain class based on the features of some given conditioning image. The authors demonstrate several examples of their method.

### Strengths
- Conditional sampling is a key problem, where improvements may have a high impact.
- The proposed solution is novel, to the best of my knowledge.

### Weaknesses
 - The paper's motivation is not sufficiently clear. While adding noise and conditioning may not commute in the general case, I believe the operation do commute in the case where each sample image has only one corresponding class, which is the common case in class-conditional sampling.
- Many conditional diffusion models in the literature are trained with the condition as an input to the network, alleviating the concern regarding the inexactness of using Eq. (4) for sampling. While such method require training a conditional model, but so does the method proposed in the paper, making the advantage here unclear. The authors need to clarify how their method offers a distinct advantage over these existing conditional diffusion models, especially since both require training a model with conditional information. The paper should explicitly address why training a conditional diffusion model directly is insufficient for the task at hand.
- The experiment section is missing a meaningful comparison with alternative conditional generation methods, despite those methods being well established and mentioned in the text. Could the authors to compare their method to existing conditional diffusion models, and highlighting specific advantages or differences? Specifically, a comparison with classifier-free guidance methods, which are widely used, is necessary to understand the benefits of the proposed approach. The absence of such a comparison makes it difficult to assess the practical value of the proposed method.
- The proposed method relies on access to an example image from a given class for sampling, making generation more cumbersome. this concern is not addressed in the paper. Perhaps this could be meaningfully discussed in a limitations section.
- Please address several typos in the discussion section.

### Questions
Please see concerns under Weaknesses.
- Why have the authors chosen not to use an established class conditional dataset, such as CIFAR10 or ImageNet for the experiments in the paper?
- Can the authors elaborate why adding noise and conditioning do not commute? I believe such a claim requires proof.

### Soundness
1

### Presentation
1

### Contribution
1
