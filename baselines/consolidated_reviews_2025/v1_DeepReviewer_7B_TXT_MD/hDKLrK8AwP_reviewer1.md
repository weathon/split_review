### Summary

This paper proposes a new method to generate readable SVG code. The authors introduce three desiderata for readable SVG code and three metrics to evaluate the readability of SVG code. Differentiable objectives are designed to optimize SVG generation models to produce readable SVG code. Experiments are conducted to demonstrate the effectiveness of the proposed method.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed metrics and objectives are reasonable and well-motivated.
3. Experiments are conducted to demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the proposed method is limited. The proposed method is a combination of existing techniques, including VAE, differentiable proxy loss, and existing SVG generation methods. The core idea of using a VAE to generate SVGs, while effective, is not new, and the application of differentiable losses to guide the generation process is also a common approach in generative modeling. The specific combination of these techniques, while potentially effective, does not represent a significant conceptual leap.
2. The proposed metrics are not well-motivated. The authors claim that the proposed metrics are based on "desiderata" for readable SVG code, but the connection between these desiderata and the specific mathematical formulations of the metrics is not clearly established. For example, the "Structural Proximity Index" (SPI) is based on the assumption that elements should be generated in the correct order, but this assumption is not rigorously justified. The metrics also lack a clear connection to actual human readability, making it difficult to assess their practical relevance.
3. The evaluation of the proposed method is not comprehensive. The experiments are limited to a small number of examples, and the evaluation is primarily qualitative, relying on GPT-3.5 to assess the readability of the generated SVG code. This approach is not robust and does not provide a clear picture of the method's performance on more complex or diverse datasets. The lack of quantitative metrics beyond the proposed ones makes it difficult to compare the method against existing approaches.

### Suggestions

To address the limited novelty, the authors should focus on highlighting the specific challenges in generating readable SVGs that are not addressed by existing methods. For example, they could explore the unique difficulties in balancing structural correctness, element simplicity, and redundancy reduction in SVG generation. A more detailed analysis of how the proposed method overcomes these specific challenges would significantly strengthen the novelty claim. Furthermore, the authors should consider exploring more advanced techniques for differentiable loss optimization, such as adversarial training or reinforcement learning, to potentially achieve better results. This would demonstrate a more substantial contribution to the field.

To improve the motivation of the proposed metrics, the authors should provide a more rigorous justification for each metric, connecting it to established principles of readability and cognitive load. For example, the SPI metric could be linked to the concept of cognitive load by measuring the number of changes in the rendered image as elements are added to the SVG. Similarly, the Element Simplicity Score (ESS) could be linked to the principle of parsimony by penalizing the use of complex elements. The authors should also consider incorporating metrics that directly measure the cognitive effort required to understand the generated SVG code, such as human subject studies. This would provide a more direct link between the proposed metrics and human readability.

To enhance the evaluation, the authors should conduct experiments on more diverse and challenging datasets, including real-world images with complex structures and patterns. The evaluation should also include quantitative metrics that are widely used in the field of image generation, such as structural similarity index (SSIM) and peak signal-to-noise ratio (PSNR). This would allow for a more objective comparison of the proposed method against existing approaches. Additionally, the authors should consider using human subject studies to evaluate the readability of the generated SVG code, providing a more direct measure of user perception. The evaluation should also include a detailed analysis of the failure cases of the proposed method, identifying the specific scenarios where it struggles to generate readable SVGs.

### Questions

1. What is the motivation for proposing the metrics in Section 2.2.1 and 2.2.2?
2. What is the motivation for proposing the losses in Section 3.2.1, 3.2.2, and 3.2.3?
3. What is the performance of the proposed method on real-world images?
4. What is the performance of the proposed method on the SVG-Fonts dataset?

### Rating

3

### Confidence

4

**********
