### Summary

This paper addresses the challenge of generating images with the correct number of objects as specified in text prompts, a known limitation of current text-to-image diffusion models. The authors propose REMASKER, a method that enhances count accuracy by identifying object-instance features within the model's self-attention layers and using these to detect and correct over- or under-generation of objects. REMASKER includes a layout-correction component that adjusts the number of objects while preserving the scene's composition and a layout-guided generation phase that ensures the final image adheres to the corrected layout. The method is evaluated on benchmark datasets and shows significant improvements in count accuracy over existing methods, including commercial models.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper introduces a novel approach to a significant problem in text-to-image generation—ensuring the accurate number of objects as specified in text prompts. The REMASKER method is innovative in its use of self-attention features to identify and correct object counts directly within the diffusion model, without needing external layout inputs. This approach is both creative and technically sound, addressing a gap in current generative models.

The paper is well-structured and clearly written, making complex concepts accessible. The authors provide thorough explanations of the technical components, such as the layout-correction mechanism and the cross-attention loss function, which enhance the reader's understanding.

The empirical evaluation is comprehensive, with experiments on benchmark datasets and comparisons to multiple baselines, including state-of-the-art models. The results demonstrate substantial improvements in count accuracy, which are convincing.

This work has significant implications for improving the reliability and usability of text-to-image models in applications where accurate object representation is essential, such as technical documentation, children's books, and recipe illustrations. The method's ability to generate count-accurate images could also benefit areas like e-commerce and educational content creation.

### Weaknesses

#### Some Related Works


#### comment

While REMASKER improves count accuracy, the paper does not extensively explore potential trade-offs in other aspects of image quality, such as object realism or overall scene coherence. Further analysis of these trade-offs would provide a more balanced view of the method's effectiveness.

The method currently supports generating images with up to 10 object instances. Its scalability to scenes with a higher number of objects is unclear, which may limit its applicability in more complex scenarios. Addressing this limitation would enhance the method's robustness.

### Suggestions

The paper would benefit from a more detailed analysis of the potential trade-offs between count accuracy and other aspects of image quality. While the method demonstrates improved accuracy in the number of objects, it is crucial to understand how this improvement affects the realism and coherence of the generated images. For example, does enforcing a specific number of objects lead to artifacts or distortions in object shapes or textures? A quantitative analysis using metrics beyond object count, such as FID or CLIP score, would provide a more comprehensive view of the method's overall performance. Furthermore, a qualitative analysis with examples of where the method succeeds and fails in terms of image quality would be beneficial. This would help to identify specific scenarios where the method might be less effective and guide future improvements.

To address the scalability limitation, the authors should investigate the method's performance with a larger number of object instances. The current limit of 10 objects is a significant constraint, as many real-world scenarios involve more complex scenes. The paper should include experiments that systematically increase the number of objects to determine the method's breaking point. This analysis should not only focus on count accuracy but also on the computational cost and memory requirements. It would be valuable to understand how the method's performance degrades as the number of objects increases and to identify potential bottlenecks. Furthermore, the authors should explore techniques to improve the method's scalability, such as using more efficient attention mechanisms or hierarchical generation strategies. This would make the method more practical for a wider range of applications.

Finally, the paper should include a more thorough analysis of the method's sensitivity to prompt variations. While the authors mention that the method works with different prompts, a systematic evaluation of how different prompt structures or vocabularies affect the method's performance is needed. For example, how does the method perform with prompts that are more ambiguous or that specify complex spatial relationships between objects? It would be beneficial to test the method with a diverse set of prompts, including those that are more challenging or that require a higher level of reasoning. This would help to identify the method's limitations and to ensure that it is robust to a wide range of input conditions.

### Questions

How does REMASKER handle overlapping or visually similar objects, and could this affect count accuracy in such cases?

The method currently supports generating images with up to 10 object instances. Is there potential to scale REMASKER to handle more complex scenes with a higher number of objects?

How sensitive is REMASKER to variations in prompts, and could this affect its performance in generating the correct number of objects?

### Rating

6

### Confidence

3

**********
