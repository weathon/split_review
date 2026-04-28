# LayerFusion: Harmonized Multi-Layer Text-to-Image Generation with Generative Priors

- Decision: Reject
- Avg Score: 4.80
- Scores: 5, 6, 5, 5, 3

## Abstract
Large-scale diffusion models have achieved remarkable success in generating high-quality images from textual descriptions, gaining popularity across various applications. However, the generation of layered content, such as transparent images with foreground and background layers, remains an under-explored area. Layered content generation is crucial for creative workflows in fields like graphic design, animation, and digital art, where layer-based approaches are fundamental for flexible editing and composition. In this paper, we propose a novel image generation pipeline based on Latent Diffusion Models (LDMs) that generates images with two layers: a foreground layer (RGBA) with transparency information and a background layer (RGB). Unlike existing methods that generate these layers sequentially, our approach introduces a harmonized generation mechanism that enables dynamic interactions between the layers for more coherent outputs. We demonstrate the effectiveness of our method through extensive qualitative and quantitative experiments, showing significant improvements in visual coherence, image quality, and layer consistency compared to baseline methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a novel image generation pipeline, which splits the generation of the whole image into foreground in RGBA format and background layers in RGB format, providing flexible editing and composition ability. Specifically, this paper proposes a harmonized generation mechanism framework that enables dynamic interactions between the foreground and background layers. The framework first extracts attention mask as the structure prior from the self-attention, and then extracts the content confidence map from the cross-attention in the foreground model. In the blending pipeline, the blended image and the foreground image are updated respectively based on the soft and hard mask. Overall, the proposed method result in more coherent outputs and more flexible editing pipelines compared to traditional sequential generation methods.

### Strengths
1. Splitting the image generation into foreground and background settings is more aligned with real-world application scenarios, facilitating easier editing for users.

2. The harmonized mechanism based on attention masks can effectively handle interactions between foreground and background, such as lighting and style.

3. The paper is well-written and clearly articulated.

### Weaknesses
1. Unstable interaction. In the Fig.8(b), the "glass" and "woman" sample repectively lack shadow and sufficiently strong Van Gogh style in the blending image. Does the threshold of the mask boundary affects the results? Please provide more details on how the mask boundary threshold is determined, and discuss the impact of boundary threshold on the blending quality across different types of objects and styles.

2. Multi-characters. The results in the paper are only contained one character. Do you test your method on prompts with multiple foreground objects? Please provide examples and discuss any challenges or limitations they encountered.

3. Further interaction. How does the pipeline perform on the physical interaction, such as "a man holding a glass of wine" or "a kid sitting on the chair"? Please provide examples of the performance on prompts involving physical interactions between foreground and background elements, and iscuss any specific challenges or adaptations needed for such cases.

### Questions
Please see the weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Layered content generation is crucial for creative workflows in various image fields. This paper proposes a layered content design method based on Latent Diffusion Models (LDMs) and employs a harmonized attention mechanism to enhance image generation quality.

### Strengths
1. Proposed a blending generation mechanism that enables dynamic interactions between different layers in layered content generation.

2. Utilized attention mechanisms to allow adjustments between different layer images, enhancing the realism of the generated images.

### Weaknesses
1. The foreground generation model relies on a pretrained model from existing work, which may conflict with the current mechanism.

2. There is a lack of quantitative metrics for evaluating the blending images.

### Questions
It is hoped that there will be quantitative metrics for evaluating the blending images.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel image generation pipeline based on Latent Diffusion Models (LDMs) that generates images with two layers: a foreground layer (RGBA) with transparency information and a background layer (RGB).

### Strengths
This paper proposes a novel image generation pipeline based on Latent Diffusion Models (LDMs) that generates images with two layers: a foreground layer (RGBA) with transparency information and a background layer (RGB).

### Weaknesses
I find the task setting somewhat confusing in terms of its purpose. If a foreground image is generated and then a blended image is produced, what additional flexibility does this provide compared to generating a complete image directly? Since both the foreground and background images are generated rather than provided by the user, unlike other blending tasks, the setup seems unusual and lacks clear practical applications or value.

The method’s contributions seem limited. As the model is training-free, operations such as extracting attention maps, generating masks, and performing attention blending are already widely used as general techniques in the AIGC field, and therefore cannot be considered significant contributions.

As this is a niche task defined by the authors, it feels quite specific, making it challenging to evaluate the effectiveness of the experiments and to perform meaningful comparisons.

### Questions
see weakness

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel image generation pipeline based on Latent Diffusion Models that focuses on generating layered content, specifically images with a foreground layer (RGBA) and a background layer (RGB). Unlike previous methods that generate these layers sequentially, the proposed approach introduces a harmonized generation mechanism that allows for dynamic interactions between the layers, resulting in more coherent outputs. The paper also presents a novel attention-level blending scheme that utilizes extracted masks to seamlessly blend the foreground and background layers, ensuring cohesive interaction and aesthetically pleasing compositions. Through extensive qualitative and quantitative experiments, the paper demonstrates the effectiveness of the proposed method in generating high-quality, harmonized layered images, outperforming baseline methods in terms of visual coherence, image quality, and layer consistency across various evaluation metrics.

### Strengths
The key advantages of this paper can be summarized as:

1. Innovative Layered Image Generation: The paper introduces a novel pipeline based on Latent Diffusion Models (LDMs) that generates layered content, including RGBA foreground and RGB background, addressing a gap in single-layer image generation.
2. Harmonized Generation Mechanism: The proposed approach enables dynamic interactions between layers, resulting in coherent and visually appealing outputs crucial for graphic design, animation, and digital art.
3. Attention-Level Blending Scheme: A unique blending scheme uses masks to seamlessly blend layers, ensuring cohesive interaction and natural compositions.
4. Extensive Experimental Validation: Qualitative and quantitative experiments show significant improvements in visual coherence, image quality, and layer consistency compared to baseline methods.

### Weaknesses
The Harmonized Generation Mechanism seemingly focuses more on the attention given to the foreground structure, but in terms of content understanding, there appear to be some issues based on the results shown in Figure 4. For instance, in the third column, the car and the tire tracks on the street look out of place. In the fourth and sixth columns, shadows are not properly reconstructed. The fifth column gives a more "sticker-like" appearance. The authors can show more additional experiments and analyses what could help identify the root cause of these problems, such as an ablation study on different components of the harmonization mechanism.

### Questions
1. Which Parameters in SD need Fine-Tuning? Have you ever investigated which layers or attention mechanisms in the SD model are most crucial for improving the layered generation process.
2. How the  approach in this paper to harmonization compares to PCT-Net's tone consistency techniques？Have you ever considered incorporating similar mechanisms?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a training-free solution for blending the content of foreground and background layers to generate harmonious images. The image generation pipeline employs Latent Diffusion Models (LDMs) that adeptly produce images with two layers: a transparent foreground (RGBA) and a background (RGB). The authors introduce a novel attention-level blending scheme that effectively merges these layers using extracted masks.

### Strengths
1.The framework introduced in this paper represents a training-free approach for simultaneously generating layered content. 

2.The paper introduces a novel attention-level blending scheme that uses extracted masks for seamless integration of foreground and background layers, resulting in cohesive and visually appealing compositions.

### Weaknesses
1.The writing requires polishing, as there are many errors in the article. For instance, in the section "Extracting Structure Prior" there are issues with the dimensions and the numerical domain of the attention probability map. Specifically, in Lines 195-196, the authors refer to the attention probability map with the notation $m \in \Re^{MxM}$. This appears to be a typographical error. It seems likely that the authors intended to write $m \in \mathbb{R}^{M \times M}$, which correctly denotes a matrix with dimensions M by M. Clarification and correction of such details are essential for maintaining the technical accuracy and clarity of the paper.

2.The evaluation presented in the paper appears to be insufficiently robust. The authors assert that their method enhances the "harmonization" of generated images, yet they rely on metrics such as the FID score, which primarily measures image quality, and the CLIP score, which assesses text-image alignment. Unfortunately, neither of these metrics directly evaluates the "harmonization" of images. A more direct measure of harmonization is needed. For instance, the authors could consider employing perceptual studies or user evaluations to assess the perceived quality of image blending. Furthermore, exploring metrics that quantify the coherence between foreground and background, such as those used in image composition tasks, could provide a more targeted evaluation. Based on my understanding, the authors could significantly strengthen their evaluation by leveraging existing image segmentation models to perform segmentation tasks on the generated images. By assessing the accuracy of these downstream tasks, they would be able to more effectively evaluate the quality of image harmonization, providing a more direct measure of how well the foreground integrates with the background in the generated images.

3.Benchmark is not clear; the benchmark dataset utilized for the evaluation is not explicitly specified. Could the authors please clarify which benchmark dataset was used? The lack of clarity regarding the benchmark dataset makes it difficult to assess the generalizability of the proposed method. Providing details about the dataset, including its size, diversity, and source, would allow for a better understanding of the experimental setup and facilitate comparisons with other methods.

4.I think the problem addressed in the paper is not suitable for this conference. The method proposed by the authors employs a manually designed blending technique to improve the integration of foreground and background elements in image blending. As such, it is more suitable for conferences in the multimedia domain. While the use of Latent Diffusion Models is relevant to the broader machine learning community, the core contribution of this work lies in the specific attention-level blending scheme, which is more aligned with research areas such as image processing and computer graphics.

### Questions
1.What is the definition of "harmonization" of generated image and why is important？

### Soundness
2

### Presentation
1

### Contribution
1
