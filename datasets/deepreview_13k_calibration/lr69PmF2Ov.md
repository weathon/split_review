# Discriminatively Matched Part Tokens for Pointly Supervised Instance Segmentation

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
The self-attention mechanism of vision transformer has demonstrated potential for instance segmentation even using a single point as supervision. However, when it comes to objects with significant deformation and variations in appearance, this attention mechanism encounters a challenge of semantic variation among object parts. In this study, we propose discriminatively matched part tokens (DMPT), to extend the capacity of self-attention for pointly supervised instance segmentation. DMPT first allocates a token for each object part by finding a semantic extreme point, and then introduces part classifiers with deformable constraint to re-estimate part tokens which are utilized to guide and enhance the fine-grained localization capability of the self-attention mechanism. Through iterative optimization, DMPT matches the most discriminative part tokens which facilitate capturing fine-grained semantics and activating full object extent. Extensive experiments on PASCAL VOC and MS-COCO segmentation datasets show that DMPT respectively improves the state-of-the-art method by 2.0% mAP50 and 1.6% AP, achieving the best performance under point supervision. DMPT is combination with the Segment Anything Model (SAM), demonstrating the great potential to reform point prompt learning. Code is enclosed in the supplementary material.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a method called discriminatively matched part tokens (DMPT) for pointly supervised instance segmentation. The DMPT method allocates tokens for parts by using the attention maps from the vision transformer and matches the part tokens with part classifiers. In addition, DMPT can generate part points and be combined with SAM for better performance.

### Strengths
+ The proposed part token allocation and token classification with deformation constraint are reasonable and effective. They help to recognize more stable object deformation parts.
+ The proposed method is well illustrated with the visualization figures.
+ The corresponding source code is attached to this submission, which reflects good reproducibility.

### Weaknesses
- The paper shares the same idea of using self-attention maps with prior works [a], but the differences are not well elaborated. Specifically, the paper does not clearly articulate how the proposed method's use of attention maps for part token allocation differs from existing approaches that also leverage attention for similar purposes. The novelty of the token allocation strategy needs further clarification, especially regarding the specific mechanisms that enable the method to achieve superior performance compared to existing methods.
- The limitation of the part deformation constraint is not considered. For example, will it work properly if the target is a snake with a long and thin shape? The paper does not discuss the potential failure modes of the deformation constraint, particularly when dealing with objects that exhibit extreme aspect ratios or highly articulated structures. It is unclear how the method would handle situations where the assumed deformation model does not align with the actual object's geometry.

### Questions
Please refer the Weaknesses.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents discriminatively matched part tokens to improve pointly supervised instance segmentation. The part tokens are initialized by clustering and refined by part classifiers. The part tokens are utilized with self-attention maps to generate better pseudo masks for training instance segmentation models. The proposed method is validated on PASCAL 2012 and COCO datasets. The experimental results show that the proposed method achieves state-of-the-art performance for pointly-supervised instance segmentation.

### Strengths
The proposed methods utilizes part tokens to generate pseudo masks of higher quality for training instance segmentation masks. Part-classifier matching, spatial constraints and part-based guidance are proposed to generate better part tokens. The design of the components of the proposed method is well motivated. 

The proposed method achieves state-of-the-art performance for pointly-supervised instance segmentation. Extensive experiments are conducted to validate the effectiveness of the components of the proposed method. Visualization results show that the proposed method can generate better attention maps for pseudo mask generation. 

The proposed method is well written. The idea is clearly presented.

### Weaknesses
The training process seems complex. How much computational cost is inctroduced by the newly introduced modules?

It is not clear how much performance improvment is brought by the introduction of spatial constrains (eq. (5)). One more experiment is needed to verify this.

### Questions
See Weakness section.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces Discriminatively Matched Part Tokens (DMPT) to extend the capabilities of self-attention in point-based supervised instance segmentation. The main working logic of DMPT is as follows: 1) perform mean-shift to find part tokens, 2) update the part tokens based on part deformation constraint, and 3) match the part tokens with the part classifiers. Through iterative optimization, DMPT identifies the most discriminative part tokens, enabling the capture of fine-grained semantics and activation of the complete object extent. Extensive ablation studies and comparisons with the other methods are conducted on the PASCAL VOC and MS-COCO datasets. Notably, DMPT also can be integrated with the Segment Anything Model (SAM).

### Strengths
1. The idea is intuitive. It can be a simple yet effective approach.
2. The performance seems pretty good for both with and without using SAM.
3. Extensive ablation studies are conducted.

### Weaknesses
[Major]

1. The authors present the result for an image of a person. It would be advantageous to include more image samples in the main paper. I am particularly interested in the extent to which the part-classifiers effectively learn semantically meaningful parts and consistently activate similar parts in diverse images. Interestingly, the person sample in Figure 2 in the supplementary material does not seem to achieve this. Could the authors explain this?

2. I have reservations about the validity of the token-classifier matching, especially in the following two scenarios. In the rebuttal, visual results for these cases would be appreciated:

* When some parts are missing in the input image due to occlusion or other factors. In such situations, do the part-classifiers corresponding to the missing parts get correctly excluded in the matching matrix?

* Additionally, does the matching mechanism adequately handle cases of over-segmentation? It seems possible that sometimes K can significantly exceed N, especially as there is no constraint on K. In such cases, a single part-classifier should ideally be matched with multiple tokens. 

3. It would be valuable for the authors to explain their criteria for determining N, the number of part-classifiers. The optimal number of parts may vary across different classes and datasets. Complex classes like bicycles might require more parts, while classes with simple shapes (e.g., a ball) may need fewer. Can the authors elaborate on their approach to determining the number of part classifiers in various scenarios?

4. I think SAM itself can handle this task to some extent. Using the given point annotations serve as prompts for SAM, we can obtain pseudo-labels simply. Can you check this setting and compare it with your DMPT-SAM?

[Minor]

The notations are somewhat distracting, but honestly, I haven't come up with a better alternative. The core concept of this paper appears to be pretty intuitive to me. However, its mathematical formulation makes the understanding rather complex. It would greatly enhance the paper's clarity if the authors could improve its presentation.

### Questions
Please refer to the weaknesses.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to achieve pointly supervised instance segmentation based on self-attention and propose discriminatively matched part tokens (DMPT) method to address the deformation and variations in appearance of object.  This method first allocates a token for each object part by finding a semantic extreme point, and then prensents part classifiers with deformable constraint to re-estimate part tokens which are utilized to guide and enhance the fine-grained localization capability.  The extensive experiments are conducted and show the effectiveness of the method.
Besides, this method can enhance SAM model to achieve the better performance.

### Strengths
1. The proposed DMPT sounds reasonable based on self-attention.

2. The performance  on PSIS is state-of-the-art compared with the current methods. And the method can benefit the performance of SAM model for object-level segementation.

3. This paper is well-conducted, including the presentation  and figures, tables.

4. The experimental section is well-presented to demonstrate the effectivenss.

### Weaknesses
1. The section of related work is inadequate in weakly supervised instance segmentation.  Some weakly image-level supervised methods[1] and box-supervised methods[2][3]  not listed. 
2.  The inference speed of whole method could be reported and it can better demonstrate the superiority of the proposed method.
3.  Some typos  exist, like "Combed with ..." in  section 3.5 should be "Combined with ..."

### Questions
1. If some parts of an object are directly filtered as background due to low activation values in the self-attention map, how could this be further optimized in subsequent steps?
2. It would be beneficial to include comparsions with more weakly supervised methods as the performance reference for the readers.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
