# Learning In-Distribution Representations for Anomaly Detection

- Decision: Reject
- Avg Score: 3.80
- Scores: 5, 3, 5, 1, 5

## Abstract
Anomaly detection involves identifying data patterns that deviate from the anticipated norm. Traditional methods struggle in high-dimensional spaces due to the curse of dimensionality. In recent years, self-supervised learning, particularly through contrastive objectives, has driven advances in anomaly detection by generating compact and discriminative feature spaces. However, vanilla contrastive learning faces challenges like class collision, especially when the In-Distribution (ID) consists primarily of normal, homogeneous data, where the lack of semantic diversity leads to increased overlap between positive and negative pairs. Existing methods attempt to address these issues by introducing hard negatives through synthetic outliers, Outlier Exposure (OE), or supervised objectives, though these approaches can introduce additional challenges. In this work, we propose the Focused In-distribution Representation Modeling (FIRM) loss, a novel multi-positive contrastive objective for anomaly detection. FIRM addresses class-collision by explicitly encouraging ID representations to be compact while promoting separation among synthetic outliers. We show that FIRM surpasses other contrastive methods in standard benchmarks, significantly enhancing anomaly detection compared to both traditional and supervised contrastive learning objectives. Our ablation studies confirm that FIRM consistently improves the quality of representations and shows robustness across a range of scoring methods. It performs particularly well in ensemble settings and benefits substantially from using OE. The code is available at \url{https://anonymous.4open.science/r/firm-8472/}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This study introduces FIRM (Focused In-distribution Representation Modeling), a novel contrastive approach for anomaly detection. Traditional methods struggle with high-dimensional data and class collision, especially with homogeneous datasets. FIRM addresses these issues by compacting in-distribution representations and separating them from synthetic outliers. It outperforms existing methods in anomaly detection benchmarks, improving robustness and representation quality, especially in ensemble settings and with Outlier Exposure (OE).

### Strengths
* This paper addresses an important problem of learning representation for anomaly detection, which is challenging due to the lack of rich training signals in typical in-distribution datasets.
* The proposed method is straightforward and shows promising results on many benchmarks.

### Weaknesses
While the experimental results are promising, the technical novelty of the proposed algorithm is somewhat limited, as it essentially represents a minor modification of class labels in the conventional contrastive learning objective.

The paper provides limited theoretical discussion.

Most experiments are conducted with relatively small images (32x32 pixels), and it is unclear whether the cats-vs-dogs dataset is also resized to this dimension. Practical anomaly detection scenarios often involve larger images, which may lead to qualitatively different outcomes and trends when experimented with. It would be beneficial if the paper included experiments with industrial anomaly detection tasks or images larger than 128x128 pixels.

### Questions
* Could you provide the details on how the images are preprocessed in the experiments?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposed a novel contrastive loss for the anomaly detection, which favors representation invariance for the inliers, but not for the (synthetic) outliers (Eq. 2). This is expected to make the inliers or normal samples compact in the learned feature space, while allowing the outliers be diverse in that space. The proposed method is tested in multiple datasets, such as CIFAR-10, 100, Fashion-MNIST, Cats-vs-Dogs in the anomaly detection setting where one class is considered as normal and the others as anomaly. They also considered testing the proposed method in the OOD detection, where an entirely different dataset is considered as OOD, e.g. CIFAR-10 vs SVHN. The results showed minor improvements over the baselines.

### Strengths
The idea to highlight the ID in the positive pairs in contrastive learning for anomaly detection sounds interesting and novel. The results are complemented by several ablations against vanilla NT-Xent, and SupCon contrastive losses.

### Weaknesses
 - The improvement margin is very narrow compared to the competitors such as CSI. For instance in table 1, the AUROC is improved by only 1.1% points compared to the CSI (s_ens). The other variant of the method that relies on OE, is not fair when experimenting CIFAR-10 or 100, as the OE has shown to perform well when its distribution is close to the ID (e.g. see "RODEO: Robust Outlier Detection via Exposing Adaptive Out-of-Distribution Samples" by H. Mirzaei et al ICML 2024).
- Comparison against standard anomaly detection datasets, such as MVTec AD, and VisA, or medical datasets are missing. This makes validation of the claims universality difficult.
- If the author claims are true, we expect the false positive, i.e. wrongly detecting a normal sample as anomaly, should be high. Because if the normal samples lack representational invariance, it would be more likely for the model to make mistakes on those cases. However, no evidence is provided along this direction.
- In the OOD detection application, the proposed method (without OE) fails to outperform CSI in harder cases of distinguishing CIFAR-10 from the near-distribution datasets such as CIFAR-100 and ImageNet. The improvement only happens when a huge OE is used, which is unfair as mentioned in the first point earlier.

### Questions
- How does your method perform when tested against MVTec AD, or medical datasets?
- Why the improvement margin is so small compared to the CSI? 
- How does the FPR @ TPR = 95% looks like for your model compared to the other contrastive learning based models?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces the "Focused In-distribution Representation Modeling (FIRM)" loss, built on contrastive learning using multi-positive aiming to improve representation quality to prevent class collision and tackling intraclass variance problem, using synthetic outliers (by augmenting normal data) and outlier exposure method to achieve higher performance.

### Strengths
- Introducing a multi-positive contrastive for anomaly detection, addressing class collision and intraclass variance.
- The paper provides extensive experiments on benchmark datasets, and it employs multiple scoring functions and ablation studies, which add rigor to the evaluation, and I appreciate the hard works. 
- The paper’s use of ablation studies to dissect the performance impact of each component, like scoring functions, effectively supports the design choices.

### Weaknesses
 - In Figure 1 authors depicting loss landscapes, but these visualizations are not sufficiently clear regarding class collision and representation compactness. Additionally, a t-SNE visualization comparing FIRM and baseline representations (like CSI method) would provide concrete evidence of FIRM’s impact on clustering and separation in the representation space.
- The experiments are conducted on typical anomaly detection benchmarks like CIFAR-10, SVHN and etc., which are well-studied but may not adequately represent the complexities of real-world anomaly detection tasks because of: First the resolution of these datasets is very low and models like ResNet-18 could easily be overfitted on them (as you have a train model with 2000 epochs!). It is recommended apply your method on datasets like MvTech-AD and VisA for anomaly detection and ImageNet-30 for OOD.
- While the paper introduces the multi-positive objective, it lacks a rigorous theoretical analysis to justify why this approach is optimal for anomaly detection.
- The paper does not explore the impact of different types of augmentations, particularly those that might introduce more semantically meaningful variations rather than just rotations. The use of rotations as the primary method for generating synthetic outliers may not be sufficient to capture the full spectrum of potential anomalies, especially for object classes where rotations do not significantly alter the object's appearance or context.
- The ensemble scoring method, which uses rotations and random crops, could introduce artifacts. Rotating an image of a car, for example, might not create a semantically meaningful anomaly, and random cropping could remove critical anomaly features, thus hindering the detection process. The paper does not adequately address how these transformations impact the overall anomaly detection performance, especially for specific object classes.

### Questions
1- Does the author test the generalization of the provided method on augmentations and noises?

2- In provided "Ensemble score" you use data and 3 rotations of it as an input and then add random crop to it. Wouldn't blindly rotating an image like a car made it anomaly and it will affect your score? Then randomly cropping and image also could hurt detection of anomaly by removing anomaly part of the object.

3- In your experiment for creating synthetic outliers is again above argument will apply by creating an anomaly data using its rotation (like a rotated ship). I know that CSI with also used this type of rotation as their main contribution for achieving a good representation, but their works lacks the generality, and the accuracy will drop over some augmentation. Did you even test your method for generality?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper introduces a novel contrastive loss function for representation learning in anomaly detection. The approach incorporates multiple positive samples from the in-distribution into the contrastive objective, enabling the model to learn a more compact representation space. At the same time, it differentiates these in-distribution samples from a synthetic outlier distribution, which is created by augmenting in-distribution data with rotations.

### Strengths
- The paper presents a clear intuition behind the proposed approach, making it easy to follow.
- Extensive experiments and figures support the main claims.

### Weaknesses
The objective in this paper is identical to $L_{UniCLR}$ from UniCON [1], and the anomaly score function matches that proposed in CSI [2]. Moreover, UniCON has already extended this approach to incorporate outlier exposure. Consequently, the contribution of this paper remains unclear. Specifically, the contrastive loss function, which uses multiple positive samples and a synthetic outlier distribution created by rotations, is directly adopted from UniCON. The anomaly score, which measures the distance of a test sample from the learned in-distribution representation, is a standard approach previously introduced in CSI. The paper does not introduce any novel components in either the objective function or the anomaly scoring mechanism. The extension to outlier exposure, which is a key aspect of practical anomaly detection, is also not a novel contribution, as UniCON already addresses this. Therefore, the paper's novelty is significantly limited by its reliance on existing methods without any substantial modifications or improvements.

### Questions
- Given that the proposed method is nearly identical to the previously published UniCON approach, could the authors clarify what distinguishes their work? Are there specific improvements, modifications, or novel insights that were not covered in UniCON?
- Could the authors further explain how their method advances beyond the techniques presented in UniCON and CSI, especially regarding the objective function and anomaly score?
- Since UniCON already extended this objective to incorporate outlier exposure, in what ways does this paper expand on or improve that application?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper indeed combines virtual OOD (out-of-distribution) samples and contrastive learning. From the main contributions and technical details, we can observe the following:

Virtual OOD and Anomaly Detection: The paper utilizes synthetic outliers, which are virtual samples generated through transformations like rotations applied to the original distribution (ID data). Alternatively, the outliers can be obtained from external datasets using Outlier Exposure (OE). These virtual samples serve as "hard negatives" to enhance the model’s ability to distinguish between normal and anomalous data​.

Contrastive Learning and the FIRM Method: The paper introduces a novel multi-positive contrastive loss called FIRM (Focused In-distribution Representation Modeling). This is an extension of traditional contrastive learning, designed to address the class collision problem. FIRM aligns multiple positive samples with the same ID anchor and leverages virtual outliers to improve the model’s ability to differentiate between normal and abnormal data​.

Advantages of the Method: The core of the FIRM loss function is to promote tight clustering of ID samples while maintaining diversity among synthetic outliers. This design effectively enhances anomaly detection performance and mitigates the class collision issue often encountered with standard contrastive learning objectives​.

Thus, this paper indeed employs virtual OOD and contrastive learning methods, with innovative improvements over traditional contrastive approaches. FIRM aims to enhance representation learning by tightly clustering ID samples and leveraging synthetic outliers to improve OOD detection.

Cons
1. I concern the novelty of this work.
2. The baselines are old. Could you intoduce resent baselines (2023-2024) related to OE? such as
Learning to Augment Distributions for Out-of-distribution Detection. NeurIPS 2022
3. DreamOOD (Dream the impossible: Outlier imagination with diffusion models) also considers to generate fake OOD data. Do you have considered this case?

### Strengths
Virtual OOD and Anomaly Detection: The paper utilizes synthetic outliers, which are virtual samples generated through transformations like rotations applied to the original distribution (ID data). Alternatively, the outliers can be obtained from external datasets using Outlier Exposure (OE). These virtual samples serve as "hard negatives" to enhance the model’s ability to distinguish between normal and anomalous data​.

Contrastive Learning and the FIRM Method: The paper introduces a novel multi-positive contrastive loss called FIRM (Focused In-distribution Representation Modeling). This is an extension of traditional contrastive learning, designed to address the class collision problem. FIRM aligns multiple positive samples with the same ID anchor and leverages virtual outliers to improve the model’s ability to differentiate between normal and abnormal data​.

Advantages of the Method: The core of the FIRM loss function is to promote tight clustering of ID samples while maintaining diversity among synthetic outliers. This design effectively enhances anomaly detection performance and mitigates the class collision issue often encountered with standard contrastive learning objectives​.

Thus, this paper indeed employs virtual OOD and contrastive learning methods, with innovative improvements over traditional contrastive approaches. FIRM aims to enhance representation learning by tightly clustering ID samples and leveraging synthetic outliers to improve OOD detection.

### Weaknesses
Cons
1. I concern the novelty of this work.
2. The baselines are old. Could you intoduce resent baselines (2023-2024) related to OE? such as
Learning to Augment Distributions for Out-of-distribution Detection. NeurIPS 2022
3. Please consider more recent OOD methods as baselines.
4. DreamOOD (Dream the impossible: Outlier imagination with diffusion models. NeurIPS 2023) also considers to generate fake OOD data. Do you have considered this case?

### Questions
See Weakness

### Soundness
2

### Presentation
3

### Contribution
2
