# Decoupling Layout from Glyph in Online Chinese Handwriting Generation

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 6, 5, 8

## Abstract
Text plays a crucial role in the transmission of human civilization, and teaching machines to generate online handwritten text in various styles presents an interesting and significant challenge. However, most prior work has concentrated on generating individual Chinese fonts, leaving \textit{complete text line generation largely unexplored}. In this paper, we identify that text lines can naturally be divided into two components: layout and glyphs. Based on this division, we designed a text line layout generator coupled with a diffusion-based stylized font synthesizer to address this challenge hierarchically. More concretely, the layout generator performs in-context-like learning based on the text content and the provided style references to generate positions for each glyph autoregressively. Meanwhile, the font synthesizer which consists of a character embedding dictionary, a multi-scale calligraphy style encoder and a 1D U-Net based diffusion denoiser will generate each font on its position while imitating the calligraphy style extracted from the given style references. Qualitative and quantitative experiments on the CASIA-OLHWDB demonstrate that our method is capable of generating structurally correct and indistinguishable imitation samples.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a novel approach for generating online handwritten Chinese text with specific styles. The authors naturally divide a text line into two components: layout and glyphs, and design a text line layout generator coupled with a diffusion-based stylized font synthesizer to address this challenge hierarchically. The layout generator autoregressively generates the positions for each glyph based on text content and provided style references, while the font synthesizer generates each font at its position while imitating the calligraphy style extracted from the given style references. Experiments on the CASIAOLHWDB demonstrate the method's capability to generate structurally correct and indistinguishable imitation samples.

### Strengths
1. The study proposes a hierarchical method to address the under-explored task of online handwritten Chinese text line generation.
2. By decoupling layout generation from glyph generation, the method offers more flexibility in handling the generation of text lines, which is particularly useful when dealing with complex Chinese characters.
3.  The experiments conducted on the CASIA-OLHWDB database indicate high performance in imitation sample generation, demonstrating the effectiveness of the method.

### Weaknesses
1. While decoupling layout and glyph generation increases flexibility, it may also add to the model's complexity, potentially affecting training and inference efficiency. Specifically, the independent training of the layout generator and the diffusion-based font synthesizer could lead to a more complex optimization landscape, requiring careful tuning of each component and potentially leading to slower convergence. Furthermore, the sequential nature of the two-stage generation process, even with parallelization within each stage, might still introduce latency compared to a single-stage model.
2. Are there any application scenarios for this task? The author could analyze its practicality. It is unclear how this method would be used in real-world applications beyond generating synthetic data. The paper lacks a discussion on the potential use cases, such as personalized handwriting generation, educational tools, or data augmentation for text recognition, and how the proposed method would be beneficial compared to existing approaches in these scenarios.
3. The paper mentions difficulties in imitating styles with extensive cursive connections between characters due to the independent generation of each character, indicating potential limitations in handling certain calligraphic styles. This limitation is significant, as many styles of Chinese calligraphy involve strong ligatures and stroke connections between characters, which are not captured by the current method. The independent generation of glyphs could result in unnatural breaks and discontinuities in the generated text lines, especially for styles with high levels of inter-character connectivity.

### Questions
Please see Weaknesses

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on the generation of online Chinese handwriting text lines. It proposes a hierarchical approach that decouples layout generation from glyph generation. The text line layout generator arranges character positions based on text content and writing style references, while the font synthesizer generates characters with specific styles. The contributions include a novel layout generator, a 1D U-Net network for font generation, and a multi-scale style encoder. Experiments demonstrate the effectiveness of the method in generating structurally correct and stylistically similar samples.

### Strengths
(1) The hierarchical decomposition into layout and glyph generation is an innovative approach, particularly suited for complex scripts like Chinese. This framework successfully addresses challenges specific to the language, such as the diversity of character structures.

(2) The model is thoroughly tested on both character and line generation, with metrics tailored to layout and stylistic fidelity. The model's success across multiple metrics shows a well-rounded, effective design.

(3) Despite the technical depth, the paper provides a good level of explanation for each module, with helpful visualizations that demonstrate layout and glyph generation separately.

(4) The method has potential applications in handwriting synthesis, digital personalization, and document augmentation, contributing a valuable approach for future research in multilingual handwriting generation.

### Weaknesses
 (1) Missing qualitative comparisons with prior methods, limiting insights into this model’s advantages in style fidelity and layout accuracy. Specifically, the paper lacks a visual comparison showing how the generated text lines compare to those produced by existing methods, making it difficult to assess the practical improvements in both the stylistic quality and the spatial arrangement of characters. The absence of such comparisons makes it hard to judge whether the proposed method truly advances the state-of-the-art.

(2) The contributions over previous approaches could be articulated more clearly, especially regarding the effectiveness of the layout-glyph separation. The paper does not sufficiently explain why decoupling layout generation from glyph generation is a significant advancement over existing approaches. It needs to clarify how this separation addresses specific limitations of prior methods and why it is crucial for the task of generating Chinese handwriting text lines. The novelty and impact of this design choice are not adequately justified.

(3) The organization could be refined for readability, as the methods section contains complex explanations that could benefit from clearer structuring. The current structure makes it difficult to follow the technical details of the proposed method. The explanations of the layout generator, font synthesizer, and style encoder are intertwined, making it hard to understand each component in isolation and how they interact. A more modular presentation would greatly enhance the clarity and accessibility of the paper.

### Questions
(1) Could more details be provided on how the layout-glyph separation specifically enhances performance in comparison to prior models?

(2) Would additional experiments on style consistency across diverse text lines clarify the benefits of this approach?

(3) Could this method can be adapted to non-Chinese scripts or connected handwriting styles?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper focuses on the generation of online Chinese handwritten text lines. The core of this method lies in decomposing text line generation into layout generation and character generation, and fill characters into the generated layouts to form complete text lines. Experiments evaluate the proposed method.

### Strengths
1) This paper proposes a hierarchical online Chinese handwritten text line generation method. The proposed method utilizes a layout generator and a font synthesizer to produce the layouts and characters independently, then arranges the characters within the layouts to create complete text lines.

2) The proposed method achieves the best performance in purely data-driven font generation task.

### Weaknesses
1) The multi-scale style encoder is not a novel design in handwriting generation area, as a similar idea has been proposed in [a]. Besides, the proposed style contrastive learning loss is somewhat similar to the style learning loss in [b]. Specifically, the multi-scale style encoder uses a 1D CNN, while [a] employs a 2D CNN. This difference is a minor implementation detail. The contrastive loss applies the multi-scale concept of [a] to [b], using contrastive learning across multi-scale features, which is not a novel combination.

2) The method description is not clear: (1) In lines 233-237, it is mentioned that style reference samples are used as context prefixes, but how they guide the subsequent layout generation is unclear. (2) The paper does not specify the modality of the style references used, online data, or offline images. (3) The paper does not specify the number of style reference samples used, one-shot or few-shot.

3) Section 4.3.2 lacks quantitative experiments in terms of calligraphy styles, raising doubts about whether the proposed Multi-Scale Style Encoder can accurately extract calligraphy styles from entire text lines.

4) In the 'Conditional' row of Figure 7, the generated layouts (red boxes) show significant absences at the beginning of the text line, which raises concerns about the effectiveness of the layout generator.

5) It is recommended to compare the proposed method with style transfer-based approaches, as it can be relatively straightforward to extend this method to a style transfer setting by replacing character embedding with a CNN-based content encoder.

6) The layout generator requires real layouts of style references, which is not directly available in the application, does this limitation affect its applicability? If some simple layout extraction methods are used to extract the pseudo-layouts of style references, what impact would this have on generation performance?

7) The paper provides very few generated visual results and lacks visual comparisons with the baseline.

### Questions
My main concerns are the novelty of the proposed multi-scale style encoder and style contrastive learning loss, and the effectiveness of the proposed layout generator. For details, please refer to the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper addresses the task of generating online handwritten Chinese text lines condition on the content and style. It identifies that text lines can be divided into two components: layout and characters. The authors propose a hierarchical approach that includes a text line layout generator and a stylized font synthesizer. The layout generator uses in-context-like learning to determine the positions of each character, while the font synthesizer generates characters that imitate the calligraphic style of the provided references. The method is evaluated using the CASIA-OLHWDB dataset, demonstrating its effectiveness in producing structurally correct and indistinguishable imitation samples.

### Strengths
1.While some work on English handwritten text line generation exists, as far as I know, no such work has been published for online Chinese text lines. Compared to English characters, Chinese characters have more complex structures and a larger number of categories, making English generation methods unsuitable for direct application to Chinese. This work proposes a method to address this task, representing a noticable contribution.

2.The method decouples text line generation into two steps—layout generation and character generation—under a unified probabilistic framework, providing a good theoretical foundation and considerable novelty.

3.The experimental section includes comprehensive comparative and visualization experiments for both layout generation and character generation, yielding convincing results.

4.The paper is well-organized and clearly written.

### Weaknesses
1. The assumption that character generation is independent given their positions seems too strong. Does text line style only manifest in the relative positions and sizes of individual characters? I hope the authors can give discussion on the reasonableness of this assumption and explain whether it might limit the method's ability in style learning.

2. It is better to add sub-figure index for figure 8 and 9. It seems each of figure 8 and 9 has three sub-figures, but now their boundaries are not clear. In Figure 7, it is also suggested to identify which one is the proposed method in the paper. Of course, this is not a big issue.



### Questions
1. If the bounding box generated by the layout model and the bounding box generated by the character model have different shapes, how should this be handled?

2. Since the method can be described as a unified probability distribution according to Equation 1, why not jointly train the two models end-to-end instead of training them separately?

3. The paper does not discuss whether the method can be applied to handwriting generation of other languages.

4. in Line 285, what does L represent? Although the authors write this is the length of the feature sequence, it is not clear what does this sequence represent? 

5. In Line 230, is the ground truth the same as the reference input in Figure 3？

### Soundness
4

### Presentation
3

### Contribution
4
