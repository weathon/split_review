# Diving Segmentation Model into Pixels

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
More distinguishable and consistent pixel features for each category will benefit the semantic segmentation under various settings.
Existing efforts to mine better pixel-level features attempt to explicitly model the categorical distribution, which fails to achieve optimal due to the significant pixel feature variance.
Moreover, prior research endeavors have scarcely delved into the thorough analysis and meticulous handling of pixel-level variance, leaving semantic segmentation at a coarse granularity.
In this work, we analyze the causes of pixel-level variance and introduce the concept of $\textbf{pixel learning}$ to concentrate on the tailored learning process of pixels to handle the pixel-level variance, enhancing the per-pixel recognition capability of segmentation models.
Under the context of the pixel learning scheme, each image is viewed as a distribution of pixels, and pixel learning aims to pursue consistent pixel representation inside an image, continuously align pixels from different images (distributions), and eventually achieve consistent pixel representation for each category, even cross-domains.
We proposed a pure pixel-level learning framework, namely PiXL, which consists of a pixel partition module to divide pixels into sub-domains, a prototype generation, a selection module to prepare targets for subsequent alignment, and a pixel alignment module to guarantee pixel feature consistency intra-/inter-images, and inter-domains.
Extensive evaluations of multiple learning paradigms, including unsupervised domain adaptation and semi-/fully-supervised segmentation, show that PiXL outperforms state-of-the-art performances, especially when annotated images are scarce.
Visualization of the embedding space further demonstrates that pixel learning attains a superior representation of pixel features.
The code is available at https://github.com/ChenGan-JS/PiXL.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes  a pixel-level learning framework, PiXL, for semantic segmentation. The framework consists of a pixel partition module,  a prototype generation and selection module, and a pixel alignment module. The pixel partition module separate pixels features into joint and   drift pixels based on their entropy. The prototype generation module is to select the most meaningful pixels. The pixel aligment module adopts contrastive learning to align pixel features intra and inter-distribution. The effectiveness of proposed framework and components are experimentally validated on three public datasets: GTA5, SYNTHIA, and Cityscapes.

### Strengths
1. The idea of investigating semantic segmentation from pixel feature distribution perspective is novel.
2. The proposed pixel learning framework and its components are technically solid and innovative.
3. The motivation and the underlying principles of designing the framework and each components are clearly presented and explained, so that it is easy to follow the work.
4. The experiments are extensive and solid.

### Weaknesses
The experiment results of the proposed results are not much better than previous works.

### Questions
no

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper takes pixel-level distribution (local distribution) into consideration, and proposed Pixel Level Sub-Domain Partition Module (PSP), Adaptive Prototype Generation Module (APG); Drift Pixels Alignment Module(DPA) modules, the effectiveness of which is proved in ablation study.
First, the PSP module divides all features (with multiscale feature extraction) into Joint pixel features and Drift Pixel features based on the entropy of each segmentation pixels corresponding to each pixel feature. For Joint ones, they use APG to generate local feature prototypes based on their semantic classes, while the Drift ones would be pulled by the prototypes extracted from APG using info NCE loss. 
The prototypes from APG is the mean value of pixel features which belongs to Joint pixel features in two samples. From which, the paper argues that can get intra-image and inner-image information.
Finally, the effectiveness of these module is proved in unsupervised domain adaptation, semi-supervised semantic segmentation together with fully-supervised semantic segmentation.

### Strengths
1. This paper is well-written and nicely organized.
2. Extensive experiments have been conducted and a number of quantitative and qualitative results are shown, demonstrating the effectiveness of the proposed method.

### Weaknesses
1. The method seems incremental. The paper generates class prototype from two image features and push or pull image features based on these prototypes. Their novelty lies in the partition of joint features and drifted features, the selection of high resolution feature prototypes and low resolution prototypes, which seems to be triky.


### Questions
see weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors introduce the pixel learning scheme by treating each image as a local distribution of pixels. The PiXL framework, which segregates pixels within a given local distribution into sub-domains: joint pixels and drift pixels, is proposed. Then, the PiXL employs an asymmetric alignment approach to align drift pixels with the joint pixels, effectively addressing pixel-level variance in a
divide-and-conquer manner. Extensive experiments confirm PiXL’s performance, especially demonstrating promising results in
label-scarce settings.

### Strengths
This paper  proposes a novel pixel learning scheme to dive semantic segmentation models into the pixel level by treating an image as a distribution of pixels. This advocates addressing pixel-level variance to enhance the segmentation model’s per-pixel recognition capability.
The strengths are as follows:
1. This paper proposed PiXL, a pure pixel-level learning framework that executes pixel-level intra- and inter-distribution (image) alignment within the context of pixel learning. 
2. Extensive quantitative and qualitative experiments in various settings of semantic segmentation confirm the effectiveness of PiXL, demonstrating the feasibility and superiority of the pixel learning scheme, which deserves further exploration.
3. The writing is clear and well-reading.

### Weaknesses
The weakness are as follows:
1. Some description is not very clear. For example, in equation 4, "PiXL determines the threshold ...", how to determine the threshold is not presented. Furthermore, the rationale behind "that pixel partitioning is performed separately...considering the entropy gap across images" is not adequately explained. It's unclear why a separate thresholding is needed for each image versus a global threshold across all images, especially considering the goal is to align distributions.
2. "PiXL employs entropy as the criteria to segregate the pixel features in g into joint pixels and drift pixels." how to compute the entropy? The paper does not specify the probability distribution used to calculate entropy, nor does it specify how the pixel features are converted into a probability distribution suitable for entropy calculation. This lack of detail makes it difficult to reproduce the results.
3. The paper validates the effectiveness on the HRDA model, but whether the proposed methods can be applied to general semantic segmentation methods is not verified. The experiments are limited to one specific architecture, and it's not clear if the pixel learning scheme is generalizable to other architectures, or if it requires specific architectural modifications or hyperparameter tuning. The claim that it is a plug-and-play method needs more extensive validation.
4. In table 3, the proposed method cannot show state-of-the-art performance compared with other methods. The authors should prove its effectiveness. The results in Table 3 do not clearly demonstrate the superiority of the proposed method over existing approaches. The paper should provide a more thorough analysis of the results, including a discussion of the limitations and potential areas for improvement.

### Questions
The questions are summarised with weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a  pixel learning framework for semantic segmentation. Intra-image, inter-image, inter-domain pixels variances are considered in this framework. The framework is elaborate, which consists of four components, i.e., Multiple Resolution Feature Extraction, Pixel Level Sub-Domain Partition, Adaptive Prototype Generation, and Drift Pixels Alignment. The motivation of this paper is interesting. The experimental results demonstrate the effectiveness of the proposed method.

### Strengths
(1) Pixel variance is important in semantic segmentation. This paper proposed a new solution. 

(2) This framework is flexible, it is quite easily to perform different semantic segmentation tasks.

(3) The performance is good.

### Weaknesses
(1) The authors did not report the results on higher resolution images, is that because too many pixels should be considered?

(2) In semantic segmentation, contextual information is quite important to assign a class label to a pixel.  But this paper discards the context in some extent. Is this reasonable?

(3) Pixel-level contrastive learning is widely used in unsupervised semantic segmentation, both local and global relations are considered. In these methods, global pixel features are usually store in a memory bank.  The differences with these method should be given in detail.

(4) In Table 1, the proposed method performs worse with 1/8 and 1/4 than 1/30. The authors should explain this.

(5) In addition of intra-image, inter-image pixel relations, this method also considers the inter-domain one, but this is not presented in abstract.

### Questions
see the weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
