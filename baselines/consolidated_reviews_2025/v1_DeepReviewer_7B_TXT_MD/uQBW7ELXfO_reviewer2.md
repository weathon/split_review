### Summary

This paper proposes a novel approach to solve the Schrödinger Bridge problem by framing it as a sequence of conditional generation problems. The authors provide theoretical justification for their method and demonstrate its effectiveness through experiments on unpaired image-to-image translation tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a thorough theoretical analysis of the proposed method.
3. The experiments are comprehensive and demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that the proposed method is scalable and can be applied to large-scale image translation tasks. However, the experiments are conducted on relatively small datasets. It would be beneficial to see results on larger datasets to validate the scalability claim.
2. The authors claim that the proposed method can handle high-resolution images. However, the experiments are conducted on relatively low-resolution images. It would be beneficial to see results on high-resolution images to validate this claim.
3. The authors claim that the proposed method can handle unpaired image translation tasks. However, the experiments are conducted on paired datasets. It would be beneficial to see results on unpaired datasets to validate this claim.

### Suggestions

The paper would benefit from a more rigorous evaluation of the proposed method's scalability. While the authors claim the method is scalable, the experiments are limited to relatively small datasets. To strengthen this claim, the authors should consider evaluating their method on larger, more complex datasets commonly used in image translation tasks. For example, datasets with a greater number of images, higher diversity, or more complex image content could provide a more convincing demonstration of the method's scalability. Furthermore, the authors should provide a detailed analysis of the computational resources required by their method, such as memory usage and training time, as the dataset size increases. This would provide a more concrete understanding of the method's scalability and its practical applicability to large-scale problems.

To address the concerns regarding high-resolution image generation, the authors should conduct experiments on datasets with images of varying resolutions, including high-resolution images. This would provide a more comprehensive evaluation of the method's ability to handle high-resolution images. The authors should also provide a detailed analysis of the method's performance as the image resolution increases, including any potential limitations or challenges that arise. This analysis should include a discussion of the computational cost associated with high-resolution image generation and how the method addresses these challenges. Furthermore, the authors should compare their method's performance with existing state-of-the-art methods for high-resolution image translation, providing a more comprehensive evaluation of the method's strengths and weaknesses.

Finally, to validate the claim of handling unpaired image translation, the authors should conduct experiments on datasets where the source and target images are not paired. This would provide a more realistic evaluation of the method's performance in real-world scenarios. The authors should also compare their method's performance with existing methods designed for unpaired image translation, providing a more comprehensive evaluation of the method's strengths and weaknesses. This comparison should include a discussion of the method's ability to handle the challenges associated with unpaired image translation, such as domain shift and lack of paired data. Furthermore, the authors should provide a detailed analysis of the method's performance under different unpaired image translation settings, including varying degrees of domain shift and dataset sizes.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
