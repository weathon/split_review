# OCN: Learning Object-centric Representations for Unsupervised Multi-object Segmentation

- Decision: Reject
- Avg Score: 6.25
- Scores: 6, 5, 8, 6

## Abstract
We study the challenging problem of unsupervised multi-object segmentation on single images. By relying on an image reconstruction objective to learn objectness or leveraging pretrained image features to group similar pixels as objects, most existing methods can either segment simple synthetic objects or discover a rather limited number of real-world objects. In this paper, we introduce OCN, a new two stage pipeline to discover many complex objects on real-world images. The key to our approach is to explicitly learn our carefully defined three level object-centric representations in the first stage. After that, our multi-object reasoning module directly leverages the learned object priors to discover multiple objects in the second stage. Notably, such a reasoning module is completely network-free and does not need any human labels to train. Extensive experiments show that our OCN clearly surpasses all existing unsupervised methods by a large margin on 7 real-world benchmark datasets including the particularly challenging COCO dataset, achieving the state-of-the-art object segmentation results. Most notably, our method demonstrates superior results on extremely crowded images where all baselines collapse.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a two-stage pipeline consisting of an object-centric representation learning stage followed by a multi-object reasoning stage for unsupervised multi-object segmentation. The proposed three levels of objectness: 1) a binary object existence score, 2) an object center field, and 3) an object boundary distance field are used to learn object-centric representations. Given experiments show that the suggested method achieves state-of-the-art object segmentation performance.

### Strengths
This paper is well-presented and provides sufficient detail, making it easy to follow.

The task of unsupervised multi-object segmentation that the authors have investigated is both interesting and challenging. 

Compared to the competing methods, the proposed approach demonstrates a significant performance improvement.

### Weaknesses
Could the authors provide more details on how the rough masks are generated from ImageNet without using human annotations? Specifically, what method is used to distinguish foreground from background, and how is this process unsupervised?

Have the authors considered how their method might be adapted for use in domains like medical or sonar imaging, where the nature of objects and backgrounds differs significantly from natural images? What modifications might be necessary to make the approach more generalizable across diverse image types?

### Questions
How are the rough masks obtained, and does the process require supervised training?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses unsupervised multi-object segmentation by learning an object-centric representation. The proposed method is composed of two stages. In the first stage, an object-centric representation of three levels is derived, encompassing object existence, center, and boundary levels. This representation is class-agnostic, enabling the segmentation of objects from unseen classes. In the subsequent stage, a multi-object reasoning module, built upon the derived representation, identifies object instances. The proposed method is evaluated on multiple datasets in different settings and achieves promising results.

### Strengths
1. The paper, in general, is well-written and easy to follow.

2. The proposed method is simple and reasonably designed.

3. Recognizing the limitations of the COCO validation set, the authors annotated object instances that were not originally labeled, significantly enhancing its value for unsupervised object discovery.

4. The proposed method demonstrates superior performance across various datasets and experimental settings. Additionally, ablation studies confirm the effectiveness of each component in the three-level, object-centric representation.

### Weaknesses
1. My primary concern regarding this paper is the limited novelty and technical contributions. The proposed method consists of two main components: a) an objectness network for extracting a three-level, object-centric representation and b) a multi-object reasoning module for unsupervised object discovery.

a. The three-level representation, encompassing object existence, center, and boundary information, has been widely explored in the literature. For example, techniques like the Hough transform and Chamfer distance have been extensively used to capture similar representations, where object centers and boundaries are encoded. Using these inherently class-agnostic representations for unsupervised object segmentation is a relatively straightforward extension, limiting the degree of novelty. Specifically, the object center field, which uses unit vectors pointing to the center, is conceptually similar to displacement fields used in other segmentation methods. Similarly, the object boundary distance field, representing the shortest distance to the boundary, is a common technique in distance transforms and has been used for shape representation and template matching. The application of these techniques in this context, while effective, does not introduce substantial novelty.

b. The multi-object reasoning module, composed of four sequential steps, is designed in a heuristic way. Each step processes the features from individual representation levels, potentially hindering the model's ability to fully exploit the interdependencies between these levels. The sequential processing of features from different levels may not be optimal for capturing complex relationships between object existence, center, and boundary information. A more integrated approach that allows for interaction between these levels could potentially improve performance.

2. In general, this paper is clearly written. However, to further enhance its clarity and impact, the following suggestions may be considered:

a. It may be better if Figures 3, 4, and 5 can be integrated into Figure 1. The three-level presentation is repeated several times on pages 1 and 2 with a reference to Figure 1. However, readers may clearly realize what the three-level representation is after seeing the example in Figures 3, 4, and 5 on pages 3 and 4. 

b. In Section 2, it would be better to discuss why the proposed method is superior to existing methods, especially those learning object-centric representations with pre-trained features, since the proposed method uses pre-trained features, too.

c. A deeper analysis of the experimental results is necessary. While the paper emphasizes the improved performance of the proposed method, a more in-depth exploration of the underlying reasons for this superiority would strengthen the overall argument.

d. The indexing of the four steps in the reasoning module should be consistent throughout the paper, either using #0 to #3 on page 5 or #1 to #4 on page 6.

3. The sensitivity analysis presented in Table 10 of the supplementary materials is limited in scope. The narrow value ranges of hyperparameter values and the lack of evaluation on multiple datasets hinder a comprehensive assessment of the method's sensitivity to hyperparameter variations across different datasets.

### Questions
1. The authors might address my comments given in Weaknesses.

2. Please check the correctness of the statement in Lines 255 ~ 258. Consider a proposal where two objects separated by a distance greater than five pixels are present. Can this proposal be correctly excluded by using the designed kernel in Figure 6? 

3. Why are different competing methods adopted in different experiments, namely those in Tables 1 ~ 4?

4. As the images in the COCO* dataset are newly annotated by the authors, did the authors tune the hyperparameters of the competing methods to report the performance of these methods?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper studies the challenging problem: unsupervised multi-object segmentation. Previous methods based on slot-attention usually fell short on complex scenarios such as COCO, while self-supervised feature distillation methods usually fail to discover multi-objects. This paper proposes a two-stage framework, including object-centric representation learning and multi-object reasoning. For the first stage, the authors first explicitly identify the object existence score, the object center field, and the object boundary distance field, as the representation, and then train an objectiveness network to learn this type of representation on ImageNet. For the second stage, an iterative algorithm is applied. Experiments under various evaluation protocols demonstrate the effectiveness of the proposed method.

### Strengths
- The topic is challenging and worth studying.
- This paper is well-written and easy to follow.
- The figures have vividly illustrated the proposed method.
- The proposed method is quite effective.
- The defined explicit object-centric representation is reasonable.

### Weaknesses
I only have one concern: the latency. The proposed method needs to iteratively leverage the objectiveness network, which is not that efficient. Could you compare the evaluation cost?

### Questions
I have no further questions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces an unsupervised object discovery framework for real-world images, called OCN (Object-Centric Representations via the Objectness Network), which operates without human annotations. To achieve this, this paper proposes Objectness Network, trained on ImageNet using masks generated by CuVLER [1], and it produces three outputs: i) an Object Existence Score, which determines if an object is present in the image; ii) an Object Center Field, which estimates pixel locations relative to the object center; and iii) an Object Boundary Field, which estimates pixel distance to the object’s boundary. Then, it adopts a Multi-Object Reasoning Module, where bounding boxes are iteratively updated based on the Objectness Network’s outputs. OCN achieves state-of-the-art performance on the object discovery task across several datasets, including COCO and COCO*, an extended version with additional object annotations.


---
[1] Shahaf Arica et al., CuVLER: Enhanced Unsupervised Object Discoveries through Exhaustive Self-Supervised Transformers, CVPR 2024

### Strengths
* This paper revisits the important concept of object discovery by decomposing objectness into three object-centric representations, followed by a network-free multi-object reasoning module.
* The use of boundary distance gradients for extending and shrinking bounding boxes is particularly effective, as it is parameter-free and potentially faster.
* The model successfully captures multiple objects of varying scales in the challenging COCO dataset.
* The paper is well-written, easy to follow, and supported by clear explanatory figures.

### Weaknesses
 * The model is more similar to MaskCut [1] supervised rather than unsupervised, as the objectness network is trained using masks from MaskCut. Therefore, the objectness network should be compared to CutLER [1] or CuVLER [2], but not to the pseudo-labeling mechanisms of them, ie MaskCut or VoteCut, as shown in Table 1. Since OCN includes an extra training step on ImageNet with pseudo-labels, whereas MaskCut and VoteCut do not involve training, this comparison is unfair. If we assume $g$ is the MaskCut operation and $I$ represents the data, Table 1 compares $g(I)$ to $f(g(I))$, where $f$ represents the OCN training.
* Similarly, Table 3 incorporates an additional level of training, giving OCN an advantage. The OCN results in this case are $p(f(g(I)))$, while the others are only $p(g(I))$, where $p$ is the detector training.
* The use of anchors and the existence network closely resembles the Region Proposal Network (RPN) in Faster R-CNN [3]. In this sense, the objectness network can be seen as a modified version of RPN (with additional outputs), which diminishes the novelty of the proposed network. The initial proposal generation, while not the core contribution, needs to be more clearly distinguished from RPN, especially given the similarity in architecture and function.
* The Objectness Network, particularly the center field module, is trained on images with single objects. However, it is used to detect multiple objects in an image, which is not represented during training. Is this possible due to the random cropping augmentation? The authors should provide more insights into this.

**Minor Comments**
* In the appendix, it states “MaskCut proposed in CuVLER,” but MaskCut was actually proposed in CutLER [1].
* The related work section on Object-Centric Learning with Pretrained Features is missing relevant references, such as SOLV [4] and VideoSAUR [5].
* There is no step #4 mentioned in the text, though it is referred to in line 306.
* Typos in Table 5: row 2 (“exsitence”) and row 6 (“filed”).

### Questions
* Why didn’t the authors utilize DINOv2 [1], which has been shown to exhibit greater object awareness, instead of DINO [2]?
* On average, how many iterations does it take to form the final bounding box?
---
[1] Maxime Oquab et al., DINOv2: Learning Robust Visual Features without Supervision, arXiv

[2] Mathilde Caron et al., Emerging Properties in Self-Supervised Vision Transformers, ICCV 2021

### Soundness
2

### Presentation
3

### Contribution
2
