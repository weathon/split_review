# Hypercone Assisted Contour Generation for Out-of-Distribution Detection

- Decision: Reject
- Scores: 5, 6, 6, 3

## Abstract
Recent advances in the field of out-of-distribution (OOD) detection have placed great emphasis on learning better representations suited to this task. While there have been distance-based approaches, distributional awareness has seldom been exploited for better performance. We present HACk-OOD, a novel OOD detection method that makes no distributional assumption about the data, but automatically adapts to its distribution. Specifically, HACk-OOD constructs a set of hypercones by maximizing the angular distance to neighbors in a given data-point's vicinity, to approximate the contour within which in-distribution (ID) data-points lie. Experimental results show state-of-the-art FPR@95 and AUROC performance on Near-OOD detection and on Far-OOD detection on the challenging CIFAR-100 benchmark without explicitly training for OOD performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
HACk-OOD is a post-training OOD detection method using hypercone projections to construct class-specific contours in embedding space. The approach achieves SOTA performance on CIFAR-100 and improves with larger networks. Including Imagenet experiments could further demonstrate scalability on large datasets.

### Strengths
HACk-OOD introduces a unique method using hypercone projections to delineate class contours, avoiding traditional Gaussian distribution assumptions and offering greater flexibility in complex feature spaces. The method achieves competitive, often superior, results on challenging datasets like CIFAR-100, demonstrating strong performance in both near and far OOD detection scenarios.

### Weaknesses
1. Experiments are limited to CIFAR-based datasets, testing on a large-scale dataset like Imagenet would better validate the method’s scalability. Also evaluating HACk-OOD on the OpenOOD benchmark would provide a clearer comparison to recent methods. I would consider rating this paper higher if Imagenet results were provided.

2. Missing comparisons with some of the latest post-hoc OOD methods, such as ASH and SCALE. Including these would offer a more comprehensive assessment of its relative performance.

Djurisic, Andrija, et al. "Extremely simple activation shaping for out-of-distribution detection." ICLR 2022
Xu, Kai, et al. "Scaling for training time and post-hoc out-of-distribution detection enhancement." ICLR 2023

### Questions
See Weakness.

### Soundness
3

### Presentation
3

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
The paper introduces a post-training out-of-distribution (OOD) detection method, HAC_k-OOD, which models the training data distribution through a set of hypercones and assesses OOD status based on whether a test sample falls within any hypercone. Specifically, for each class, the method first computes the class centroid and defines an angular boundary using the k-th nearest neighbors for each training point. Additionally, a radial boundary is set based on the mean and variance of the sample norms within the angular boundaries. During inference, a sample is classified as OOD if it lies outside either the angular or radial boundaries. Experiments were conducted using ResNet-18, ResNet-34, and ResNet-50, with both supervised contrastive learning and cross-entropy loss. The method was evaluated on CIFAR-10/100 as the in-distribution dataset and tested on various OOD datasets, covering both near and far OOD scenarios.

### Strengths
1. The method takes an interesting approach to distance-based OOD detection by relaxing the distributional assumptions and, unlike naive KNN, still leveraging nearby training data statistics to construct class contours. To the best of my knowledge, the use of hypercones for this purpose is novel and appears well-motivated.

2. The authors present their method clearly, making the paper easy to follow and understand.

3. Although the method involves hyperparameter k, the authors provide a practical approach to estimating it without requiring additional OOD data.

4. The experiments investigate various model sizes and training losses, demonstrating their impact on distance-based methods. Overall, the method benefits more from larger models trained with contrastive loss, as these models produce more distinguishable features.

### Weaknesses
1. The computational complexity is a concern for this method. Since the computation appears to increase with the size of the training dataset, it’s unclear if this approach would be feasible for large-scale, real-world applications. Although the authors state that the method is computationally efficient and support this with inference time per sample, I encourage them to provide a more detailed discussion on this aspect. For instance, what is the time required to construct the hypercones? A comparison of inference times with other methods would also be valuable. Specifically, the method requires calculating k-nearest neighbors for each training point, which can be computationally expensive, especially with high-dimensional feature spaces and large datasets. The construction of hypercones, involving angular and radial boundary calculations, also adds to the computational overhead. A more thorough analysis of these steps is needed to understand the scalability of the method.

2. How would the method perform on a large-scale, real-world dataset like ImageNet? Many recent OOD detection methods use ImageNet-1k as the in-distribution (ID) dataset. I encourage the authors to consider experiments on this dataset to evaluate the general applicability of the method in more realistic scenarios. The current evaluation on CIFAR-10/100, while useful, does not fully demonstrate the method's ability to handle the complexities of real-world data, such as the higher resolution and greater diversity of ImageNet. The performance of distance-based methods can be significantly affected by the increased dimensionality and complexity of feature spaces in larger datasets, and it is crucial to assess how the proposed method scales in such scenarios.

3. Recent work has explored OOD detection using CLIP as a backbone model (eg. [a1]), as CLIP may offer a more robust feature space. It would be interesting to see how this method performs when applied to a CLIP-based model. The use of vision-language models like CLIP has shown promise in OOD detection due to their ability to learn more semantically meaningful representations. It is important to investigate whether the proposed method can leverage these robust features or if it is limited to the feature spaces learned by traditional image classification models. Exploring this would provide a better understanding of the method's generalizability and potential for improvement.

4. Could the authors elaborate on why this method outperforms a naive KNN approach? One advantage seems to be that the method leverages the nearest neighbors within the training set (as opposed to KNN’s i.i.d. approach) to construct hypercones, which may capture more robust information about class boundaries. Additionally, an ablation study using either angular or radial boundaries separately for OOD detection could provide valuable insights into the method’s effectiveness and support future research. The current explanation of the method's advantage over KNN is somewhat high-level. A more detailed analysis of how the hypercone construction specifically addresses the limitations of standard KNN would be beneficial. For example, how does the angular boundary adapt to varying densities of training data, and how does the radial boundary contribute to the overall performance? An ablation study would help isolate the impact of each component.

5. While the paper is generally well-written, a few sections could be clearer. For example, in lines 80-81, P_in is referenced without being introduced in a previous formula. Additionally, in Section 5.2, only ResNet-34 is mentioned as the backbone model, though ResNet-18 and ResNet-50 are also used.

### Questions
Please see the weaknesses part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a post-training method for out-of-distribution (OOD) detection. The method approximates the contour of each class with a set of hypercones and defines per-hypercone decision boundaries. 
More specifically, the hypercones are drawn as follows: 
1. compute per-class centroids, which will be the apex of the class hypercones 
2. take a class sample and set the hypercone axis to be the vector that points its (penultimate) representation 
3. set the opening angle to be the angle between the hypercone axis and the k-th nearest neighbor from the sample representation
4. set the decision boundary using the distribution of representations within the hypercone's angular boundary

The method is an extension of another technique, SSD+, which assumes the decision boundary could be modeled with a unique hypersphere (or multidimensional ellipsoid) per class. It's training does not require OOD data. 

Experimentally, the authors follow common practice and evaluate the OOD performance with the CIFAR-100 dataset as an in-distribution dataset and many different datasets as out-of-distribution datasets. Two types of pre-trained classification models are tested: models trained with a softmax cross-entropy loss and with a supervised contrastive loss. 
The method achieves SOTA results in the supervised contrastive learning setup and is competitive in the cross-entropy setting.

### Strengths
1. The paper is well-written and easy to follow. The authors provide a good summary of the different approaches to OOD, a background section on hypercones, and a clear and precise method description. 
2. Relevance and novelty of the method: the algorithm doesn't require assumptions about the data distribution and can model complex embedding spaces since it draws multiple hypercones per class and since it defines per-hypercone decision boundaries. 
3. The authors discuss some limitations of the method (e.g., it works less well with smaller models ).

### Weaknesses
1. Limited evaluation: the method is only evaluated on models pre-trained on the *quite simple* CIFAR datasets and not on more complex datasets such as the ImageNet-200 or ImageNet-1k OOD benchmarks. This is a significant limitation as the CIFAR datasets, with their low resolution (32x32 pixels) and relatively small number of classes, do not adequately represent the complexity of real-world image data. The method's performance on these datasets might not translate to more challenging scenarios involving higher resolution images, more diverse object categories, and more complex background variations, which are common in ImageNet-scale datasets.



### Questions
- (see Weakness 1): how does the method perform on the ImageNet (200 or 1k) OOD benchmarks? Its evaluation on benchmarks beyond *quite simple* datasets (i.e., CIFAR-10/CIFAR-100) would strengthen the claims. 
- What is the intuition behind the use of hypercones? Isn't the embedding space of a class more "dense" close to its centroid?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a post-training strategy for Out-Of-Distribution (OOD) detection for image classification. The proposed method assumes no access to the OOD samples and employs a set of hypercones with varying cutoff distances in feature space to define the class boundaries of in-distribution data. The work evaluates this method and a combination with a previous OOD technique on the Far-OOD and near-OOD detection benchmarks, with comparisons to a set of baselines.

### Strengths
1. The paper addresses an important problem and proposes a new distance-based model based on hypercones. 
2. The evaluation of the method seems comprehensive and it achieves strong results in some cases.

### Weaknesses
1. The paper is not clearly motivated. The discussion on training-based and distance-based post-training methods are insufficient. While the introduction section listed many previous methods, it is unclear what OOD modeling challenges this method aims to address, in particular for the distance-based approach. Specifically, the paper does not articulate why existing distance-based methods, such as those using hyperspheres or k-nearest neighbors, are inadequate for the problem, and what specific limitations the proposed hypercone approach overcomes. The lack of a clear problem statement makes it difficult to assess the significance of the contribution.
2. The assumption of this method is very restrictive. As stated in Line 064, it requires "that ID and OOD data are separable in the space", which is unrealistic for real-world data. This assumption is particularly problematic as many OOD detection scenarios involve subtle shifts in the data distribution, where clear separation is not guaranteed. The paper does not discuss the implications of this assumption or provide any analysis of the method's robustness when this assumption is violated. The performance on near-OOD data is not sufficient to justify this assumption.
3. The novelty of this method is limited. The proposed hypercone representation is similar to a mixture of Gaussian kernels for the ID data distribution. While the authors claim that their method is geometric, it still relies on the same underlying principle of capturing the distribution of the ID data in feature space. The paper does not provide a rigorous comparison to methods that explicitly use Gaussian mixtures, making it difficult to ascertain the true novelty of the approach.
4. The presentation of this work lacks clarity and the technical details are difficult to follow. Several parts of Sec 4.3 are confusing: 1) Line 260: Why do the hypercone representations rely on the test data feature Z_{test}, which should not be used during model construction? The use of test data during the construction of the hypercones is a major flaw and needs to be clarified. 2) Line 299: How is the score function defined and what threshold is used during the inference (in Sec 4.4)? The description of the score function and the thresholding mechanism is vague and lacks sufficient detail for reproducibility. The paper should provide a clear mathematical definition of the score function and explain how the threshold is determined.
5. The experimental evaluation is lacking in three aspects: 1) The experimental setup is limited, which only considers three ResNet-based backbones. More modern architectures, such as ViT, should be included to validate its generalization. The lack of experiments on ViT architectures limits the generalizability of the findings. 2) The ablative study is lacking. What contributions are from the hypercones? What if it is replaced by Gaussians? The paper does not provide sufficient ablation studies to isolate the contribution of the hypercone representation. A comparison with simpler methods, such as using Gaussian kernels, is needed to justify the complexity of the proposed approach. 3) The performance of the original version HAC_k-OOD is mixed in both Table 1 and 2, and in most of cases, it is worse than the SOTA methods. It is unclear whether the proposed representation is truly effective.

### Questions
Please address the questions in the weaknesses part as above.

### Soundness
2

### Presentation
1

### Contribution
2
