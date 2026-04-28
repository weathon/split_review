# Weakly-Supervised Affordance Grounding Guided by Part-Level Semantic Priors

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 8, 6, 5

## Abstract
In this work, we focus on the task of weakly supervised affordance grounding, where a model is trained to identify affordance regions on objects using human-object interaction images and egocentric object images without dense labels. 
Previous works are mostly built upon class activation maps, which are effective for semantic segmentation but may not be suitable for locating actions and functions. Leveraging recent advanced foundation models, we develop a supervised training pipeline based on pseudo labels. The pseudo labels are generated from an off-the-shelf part segmentation model, guided by a mapping from affordance to part names.
Furthermore, we introduce three key enhancements to the baseline model: a label refining stage, a fine-grained feature alignment process, and a lightweight reasoning module. These techniques harness the semantic knowledge of static objects embedded in off-the-shelf foundation models to improve affordance learning, effectively bridging the gap between objects and actions.
Extensive experiments demonstrate that the performance of the proposed model has achieved a breakthrough improvement over existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The proposed framework for weakly supervised affordance grounding (WSAG) uses pseudo-supervised learning to link affordance actions to object parts via part segmentation models and semantic cues. It generates and refines pseudo-labels by focusing on affordance-relevant regions with exocentric images, improving label accuracy and feature alignment. To enhance generalization, a lightweight reasoning module maps affordances to latent object part representations, enabling the model to handle unseen categories. By integrating semantic knowledge from foundation models, the framework transitions from weakly to pseudo-supervised learning, achieving a breakthrough in performance over prior methods

### Strengths
1) The paper is clearly written and easy to follow.
2) The method is well-motivated, and the VFM-assisted pseudo-labeling should effectively address the challenges of the weakly-supervised setting.
3) The overall improvements over existing methods are quite significant.

### Weaknesses
My biggest concern lies in the experimental section. In Table 2, the reasoning model appears to negatively impact the baseline, and the other two design components only provide marginal improvements.

### Questions
Could the authors clarify why the baseline method in Table 2 outperforms existing state-of-the-art methods by such a significant margin? Based on the numbers in Tables 1 and 2, it seems the improvement over existing methods might primarily stem from a strong baseline, while the additional modules contribute only marginal benefits

### Soundness
3

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
4

### Summary
This paper tackles weakly supervised affordance grounding (WSAG) by leveraging foundation models to generate pseudo labels, departing from previous CAM-based approaches. The authors propose a three-stage pipeline: (1) using VLpart and SAM to generate initial pseudo labels by mapping affordance-object pairs to part names, (2) refining these labels using human-object interaction cues from exocentric images, and (3) training an affordance grounding model with the refined pseudo labels. The method also includes cross-view feature alignment and a reasoning module to handle unseen objects. The approach shows significant improvements over existing WSAG methods

### Strengths
- The problem is important and well-motivated, as affordance grounding is crucial for robotic manipulation and human-object interaction understanding
- The proposed pseudo-labeling approach effectively leverages existing foundation models (VLpart, SAM) to provide supervision, addressing limitations of previous CAM-based methods
- The label refinement process using exocentric images is novel and well-designed, providing a clever way to improve initial pseudo labels
- The reasoning module helps generalize to unseen objects, which is crucial for practical applications
- The writing is clear and the method is well-explained with appropriate visualizations

### Weaknesses
The choice of CLIP as the vision encoder could be better justified given previous work suggesting limitations (vs DINO, OWLViT, SAM). For example, the paper will be stronger with an ablation study of different visual encoders.

### Questions
See weaknesses.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the task of weakly supervised affordance grounding (WSAG), where the goal is to identify affordance regions on objects using only image-level labels and human-object interaction images. 
The key contributions include:
- A novel pseudo-supervised training framework and pipeline that leverages visual foundation models to generate affordance heatmaps, mapping affordance classes to object parts.
- Three key enhancements to improve performance:
    - Label refinement using interaction cues
    - Fine-grained object feature alignment with exocentric images
    - Reasoning module for better generalization
- Extensive experiments demonstrating significant performance improvements over existing methods

### Strengths
- Clear writing and organization.
- Well-motivated technical approach with clear problem formulation.
- This paper propose a novel approach that uses visual foundation models and part-level semantic priors for WSAG, unleashing the power of these models for affordance learning.
- Using human occlusion cues for label refinement, which is an innovative insight.
- Comprehensive experimental validation and thoughtful analysis of limitations in existing methods.

### Weaknesses
 - Could benefit from more analysis of failure cases.
- The label refinement stage using human occlusion cues may be problematic when interactions are ambiguous or when multiple affordances exist.
- The mapping from affordance to part names is ad-hoc and manually crafted, which limits the scalability to new affordance types and more complex objects.

### Questions
1. Could you provide more details about failure cases and limitations of the proposed approach?
2. How sensitive is the method to the results of VFM? How well can the refine state correct possible errors by VLpart and SAM?
3.  How does the computational cost (training & inference) compare to existing CAM-based methods?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper propose a weakly supervised affordance grounding framework. It uses off-the-shelf foundation models to generate pseudo labels of object parts. To further improve the performance, a label refining strategy, a fine-grained feature alignment process, and a lightweight reasoning module are introduced. Experiments show promising results.

### Strengths
1. Training affordance grounding models with object labels is an interesting question.
2. Using off-the-shelf foundation models to generate affordance label is an interesting idea.
3. Experiments show promising results.

### Weaknesses
1. As shown in the ablation study table 2, the improvements of using all these three modules look marginal over using one module. It seems that the effectiveness of the three components are not significant. Specifically, the performance gains from adding each module individually are relatively small, and the combined improvement is not substantially larger than the best single module. This raises concerns about the necessity and individual contribution of each component.
2. In section 3.4, the authors propose to align the features of exo- and egocentric images after SAM segmentation while the existing methods directly align the features of the two images. However, there is no solid experiments to show the effectiveness of this design. It is unclear whether the added complexity of SAM segmentation and masked feature alignment provides a significant advantage over direct feature alignment, and the lack of a direct comparison makes it difficult to assess the true benefit of this approach.
3. The framework refines the affordance labels with the need of the corresponding exocentric image which may not be available sometimes. This reliance on paired exocentric images limits the applicability of the method in scenarios where such data is not readily accessible, potentially restricting its practical use.

### Questions
1. Aligning the features of an object from different views is a commonly used strategy for feature learning. How is this strategy related to pseudo label generation and refinement.
2. Some designs need more detailed ablation studies. E.g., how does the proposed fine-grained feature alignment process with SAM perform when compared with the previous work aligning the features directly. Is there any significant performance difference?

### Soundness
3

### Presentation
3

### Contribution
3
