# CAPGen: An Environment-Adaptive Generator of Adversarial Patches

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3

## Abstract
Adversarial patches, often used to provide physical stealth protection for critical assets and assess perception algorithm robustness, usually neglect the need for visual harmony with the background environment, making them easily noticeable. Moreover, existing methods primarily concentrate on improving attack performance, disregarding the intricate dynamics of adversarial patch elements. In this work, we introduce the \textbf{C}amouflaged \textbf{A}dversarial \textbf{P}attern \textbf{Gen}erator (CAPGen), a novel approach that leverages specific base colors from the surrounding environment to produce patches that seamlessly blend with their background for superior visual stealthiness while maintaining robust adversarial performance. We delve into the influence of both patterns (i.e., color-agnostic texture information) and colors on the effectiveness of attacks facilitated by patches, discovering that patterns exert a more pronounced effect on performance than colors. Based on these findings, we propose a rapid generation strategy for adversarial patches. This involves updating the colors of high-performance adversarial patches to align with those of the new environment, ensuring visual stealthiness without compromising adversarial impact. This paper is the first to comprehensively examine the roles played by patterns and colors in the context of adversarial patches.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a method that can produce patches that blend with their background to fool the person detector. Moreover, this paper proposes to update the base colors instead of the patterns to improve the attack efficient and to ensure visual stealthiness without compromising adversarial impact.

### Strengths
1. This paper shows clear writing and is easy to follow.
2. This paper compared both white-box and black-box performance on different detectors.

### Weaknesses
1. The motivation of this paper is in question. For person detection, the person may be placed in many different places with various backgrounds. The adversarial patch should be assumed to be able to fool the person detector under different backgrounds. For example, Hu et al. [1] use many different backgrounds to compute the expectation loss.
2. It did not compare with some of the latest work, such as [1]. Moreover, it is shown that the attack success rate is lower than AdvPatch.
3. In a real-world attack, there may be some nonlinear distortions because of the clothes. This paper did not consider this, compared with some previous work., such as [1][2].

### Questions
1. What is the attack performance on some of the latest person detectors?
2. What is the potential scenario of your attack? Could you give a more realistic reason for producing an adversarial patch that needs to be concealed in the background?
3. There is already some work to produce "natural" adversarial patches", such as [1][2]. In Table 8, you only compared with AdvPatch, which is an early work. Could you compare the naturalness with these latest works that can produce natural adversarial patches, such as [1][2]?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces CAPGen, a method for creating camouflaged adversarial patches that seamlessly blend into their environment to deceive both deep learning-based object detection systems and human observers. CAPGen achieves this by optimizing a color probability matrix that adapts patch colors to match the background, enhancing visual stealth without compromising adversarial effectiveness.

### Strengths
- The writing and presentation are good and easy to follow.
- The evaluation on the YOLO-family detectors is comprehensive.
- The experimental results performed in the digital and physical scenarios also demonstrate some effectiveness of the proposed method.

### Weaknesses
 - Limited technical contributions: While CAPGen proposes an approach to camouflage adversarial patches, the task of attacking object/person detection systems has been widely studied, limiting the novelty of the technical contributions.
- Limited color adaptability in complex environments: CAPGen relies on a restricted set of base colors to match the background, which works well in simpler scenes but may fail in urban or high-color-variability environments. This limited color adaptability could make patches visually conspicuous in complex scenes, potentially reducing their stealth and effectiveness. 
- Challenges in maintaining stealth across varied environments: In environments dominated by specific colors (e.g.,indoors with monochromatic walls or in environments with limited textures), CAPGen’s pattern-based approach may stand out if color matching is not precise, compromising its stealth.
- Over-reliance on transferability: The approach shows promising transferability with a single substitute detector (YOLOv4), but the lack of extensive testing across multiple models and datasets raises questions about its general applicability. Limited testing may reduce confidence in its universal effectiveness across diverse detection architectures.
- Inconsistent benchmarking with state-of-the-art results: The performance metrics reported for state-of-the-art adversarial patches differ from those in their original papers, which may undermine the reliability of CAPGen’s comparative analysis. These discrepancies could be due to differences in setup or configurations, making it difficult to accurately assess CAPGen’s performance relative to established methods.
- Insufficient robustness testing across diverse scenarios: CAPGen’s robustness evaluation lacks indoor testing and does not examine varying distances from the camera or different viewing angles. Such scenarios are important for understanding real-world applicability, especially in surveillance settings. Without testing across diverse conditions, it is difficult to determine CAPGen’s effectiveness in dynamic environments.
- Ambiguity in regularization parameters: The regularization terms and parameters, such as the λ values, lack justification and sensitivity analysis. This ambiguity may make it challenging for others to replicate or adapt CAPGen without clear guidelines on parameter selection.
- Limited evaluation of color probability matrix Eficiency: While the color probability matrix is central to CAPGen, there is little analysis on its computational complexity or scalability in diverse environments with high color variation. This could impact CAPGen’s efficiency and adaptability in real-world scenarios.

### Questions
I suggest the following actions:
- Evaluating CAPGen in diverse environments, such as cityscapes, would also clarify the model’s scalability and adaptability.
- Evaluating CAPGen on a wider range of detection models, including those with different architectures and training datasets, to validate its transferability and effectiveness across diverse settings.
- Ensuring alignment with the evaluation protocols of prior works to provide consistent benchmarking. Alternatively, clearly documenting any deviations in methodology to clarify CAPGen’s comparative advantages.
- Expanding robustness tests to include varied indoor and outdoor settings, as well as different perspectives and distances. This would provide a more comprehensive assessment of CAPGen’s real-world applicability.
- Conducting a sensitivity analysis on regularization parameters and provide guidance on optimal parameter selection, improving reproducibility and adaptability for different environments.
- Including a computational efficiency analysis of the color probability matrix, especially in high-color-diversity scenarios. This would help determine CAPGen’s scalability and suitability for real-time applications in complex scenes.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces CAPGen, a method for generating context-adaptive adversarial patches that can seamlessly blend with different visual backgrounds to enhance attack effectiveness and stealth. Traditional adversarial patches are often visually conspicuous, limiting their applicability in the real world. CAPGen addresses this limitation by introducing an adaptive patch design that considers the background context, allowing the patches to visually blend into various environments while maintaining strong adversarial properties.

### Strengths
1. The paper proposes the Environment Adaptive Adversarial Patch Generator (CAPGen), an innovative method for generating camouflaged adversarial patches by extracting the base color of the background environment. Through this method, the generated patches can better blend with the background, not only improving the adversarial effect at the algorithm level, but also achieving concealment at the visual level, greatly increasing the possibility of its practical application. This design is of great significance in adversarial attacks in the physical world. 
2. The paper optimizes the color probability matrix to ensure that each pixel of the patch matches only one base color, thereby achieving color control and consistency. This strategy effectively solves the problem that traditional adversarial patches are not coordinated with the background in terms of color and texture, making the patches more concealed in the physical environment and not easily detected by the human eye.
3. CAPGen uses the analysis of the impact of color and texture components to propose a fast generation strategy that only replaces the patch color in the new background. By replacing the color of existing high-performance adversarial patches, rapid adaptability in dynamic environments is achieved, reducing the time for re-optimization and generation. This efficient generation method makes it more suitable for adversarial applications in real scenes, especially in scenes that require rapid response.

### Weaknesses
1. This paper achieves environmental adaptability and concealment of adversarial patches by optimizing the color probability matrix, but there is a lack of more effective optimization methods to balance adversarial and concealment, especially in dynamic or complex scenes. It is recommended that the authors provide more detailed technical details to show how to improve concealment without affecting adversarial resistance, and clearly indicate in which scenarios adversarial effect and concealment may conflict. It is recommended to further quantify these trade-offs, such as by evaluating attack success rates and visual detection scores (such as visual perception scores) in different scenarios. For complex scenarios in practical applications, the authors can provide specific experiments or feasibility verification in scenarios where patches significantly affect the balance of adversarial resistance or concealment.

2. This paper proposes a fast generation strategy by comparing the impact of color and texture on adversarial performance, but does not deeply analyze the adaptability of color selection under diverse backgrounds, especially in scenarios with dynamic lighting, complex backgrounds, or even multi-object interference. It is recommended that the authors provide multi-scenario experiments to specifically analyze the performance of color selection in different environments (such as daytime and nighttime, different weather, indoors and outdoors, etc.), and test the adaptability of color selection through multiple lighting and background complexity settings. Consider introducing quantitative indicators, such as background consistency scores for color and texture, and combining dynamic scene changes in practical applications (such as weather changes, shadow effects, etc.) to evaluate the concealment and attack effectiveness of the method under different backgrounds.

3. During the optimization process, the author used regularization to ensure that each pixel value corresponds to the main color, but did not clearly describe the specific implementation details of the regularization, especially the gradient calculation method, loss function construction, and parameter selection. It is recommended to supplement the detailed mathematical formula and gradient update rules of the regularization process in the method section, especially how to select the loss term and related weights, so that other researchers can reproduce it. The author can consider showing experimental results for different regularization parameters, analyzing the impact of parameter changes on patch concealment and adversarial resistance, and enhancing the generalization of the method. In addition, it is recommended to add experiments for different complex scenes to verify the robustness of CAPGen, such as testing its robustness under different occlusions or nonlinear backgrounds.

4. This paper compares with methods such as AdvPatch, but lacks comparison with the latest adversarial patch generation techniques (such as patches based on generative adversarial networks or Transformer models) in more challenging environments, which may affect the comprehensive evaluation of CAPGen's innovation. It is recommended that authors include specific state-of-the-art methods (such as adversarial patches generated by GAN or Transformer models proposed in recent years) and add performance comparisons with these methods in the experimental section. Authors can introduce more evaluation metrics (such as Fooling Rate, Perceptual Quality Score) and combine multi-scenario comparative tests (such as in complex natural scenes or dynamic crowd environments) for comprehensive evaluation. Key literature can be cited, such as the latest research on multimodal patch generation based on generative adversarial networks, to more clearly demonstrate the innovation and wide applicability of CAPGen in the field of adversarial patch generation.

### Questions
Please see the weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces an algorithm called CAPGen, which generates adversarial patches by extracting base colors from the environment to enhance stealthiness in physical-world settings. The paper also explores the impact of patterns and colors on the effectiveness of the attack. The adversarial patches generated using CAPGen demonstrate improved stealthiness compared to the original AdvPatch method.

### Strengths
1, This paper addresses a critical issue: the stealthiness of adversarial patches in the physical world.
2, The paper is well-structured and easy to follow, with discussions effectively supported by relevant illustrations.

### Weaknesses
1, The approach is quite simple and lacks significant technical novelty.
2, The impact of adversarial patch components and the color transfer method has already been demonstrated in [1].
3, Several alternative approaches for improving adversarial patch stealthiness are not discussed in the paper [2].
4, While the paper focuses on physical-world stealthiness, it lacks a human perception study and a quantified comparison with other methods in real-world scenarios.

### Questions
1, Does CAPGen perform reliably in physical-world environments, given the limited color range? A physical-world experiment is necessary to demonstrate its effectiveness in such settings.
2, The demonstration figures predominantly feature complex textures, which make it easier to hide adversarial patches. A more general environmental setup, along with a human perception study, is needed to better evaluate the proposed method’s impact on stealthiness.

### Soundness
3

### Presentation
3

### Contribution
1
