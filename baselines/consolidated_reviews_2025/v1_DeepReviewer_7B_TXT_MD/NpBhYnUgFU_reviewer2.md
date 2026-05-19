### Summary

This paper proposes a zero-shot remote sensing scene classification method, which combines super-resolution and zero-shot learning. The proposed method consists of a super-resolution module, a CAT module, and a feature refinement module. The super-resolution module enhances the resolution of remote sensing images, and the CAT module and feature refinement module are designed to improve the visual features of remote sensing images. The proposed method is evaluated on three benchmark datasets, and the experimental results show that the proposed method outperforms the baseline methods.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. This paper proposes a zero-shot remote sensing scene classification method that combines super-resolution and zero-shot learning.
2. The proposed method is evaluated on three benchmark datasets, and the experimental results show that the proposed method outperforms the baseline methods.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is not novel. The super-resolution module is not a novel method, and the CAT module and feature refinement module are similar to existing methods. The novelty of the proposed method is limited.
2. The proposed method is not well-motivated. The authors do not explain why the super-resolution module is used in the proposed method. The authors should explain the motivation of the proposed method.
3. The proposed method is not well-written. The authors should improve the writing of the paper.

### Suggestions

The paper would benefit from a more thorough justification of the super-resolution module's inclusion within the zero-shot remote sensing scene classification framework. While super-resolution can enhance image quality, its direct relevance to the core task of scene classification is not immediately clear. The authors should elaborate on the specific mechanisms by which super-resolution contributes to improved classification performance. For instance, do the enhanced high-frequency details provide additional discriminative information that is not present in the original low-resolution images? Or does the super-resolution act as a form of data augmentation, effectively increasing the diversity of the training data? A detailed explanation of these aspects would significantly strengthen the motivation for incorporating this module. Furthermore, the authors should consider comparing their approach with methods that directly operate on low-resolution images, highlighting the advantages of their super-resolution strategy.

Regarding the novelty of the proposed method, the authors need to more clearly differentiate their approach from existing techniques, particularly in the CAT and feature refinement modules. While the paper mentions that these modules are inspired by existing methods, it does not sufficiently articulate the specific modifications or improvements that make their approach unique. A more detailed comparison with related works, highlighting the differences in architecture, training procedures, and the specific problem they address, would be beneficial. For example, if the CAT module is similar to a cross-attention mechanism, the authors should clearly state this and then emphasize the novel aspects of their implementation, such as the specific attention mechanism used, the way it is integrated with the feature refinement module, or any unique training strategies employed. Similarly, for the feature refinement module, the authors should provide a more detailed explanation of how it differs from existing feature refinement techniques, focusing on the specific operations and parameters used.

Finally, the paper's writing needs to be improved to enhance clarity and readability. The authors should ensure that all technical terms are clearly defined, and that the overall structure of the paper is logical and easy to follow. The motivation for each module should be clearly stated, and the experimental results should be presented in a way that is easy to understand. The authors should also consider adding more visualizations to illustrate the effects of each module, which would help readers to better understand the proposed method. For example, visualizing the feature maps before and after the feature refinement module could provide valuable insights into how this module enhances the visual features. Additionally, the authors should carefully proofread the paper to eliminate any grammatical errors or typos.

### Questions

1. The authors should explain the motivation of the proposed method.
2. The authors should improve the writing of the paper.

### Rating

5

### Confidence

3

**********
