# Interpretable Unsupervised Joint Denoising and Enhancement for Real-World low-light Scenarios

- Decision: Accept
- Scores: 6, 6, 6, 8, 6

## Abstract
Real-world low-light images often suffer from complex degradations such as local overexposure, low brightness, noise, and uneven illumination. Supervised methods tend to overfit to specific scenarios, while unsupervised methods, though better at generalization, struggle to model these degradations due to the lack of reference images. To address this issue, we propose an interpretable, zero-reference joint denoising and low-light enhancement framework tailored for real-world scenarios. Our method derives a training strategy based on paired sub-images with varying illumination and noise levels, grounded in physical imaging principles and retinex theory. Additionally, we leverage the Discrete Cosine Transform (DCT) to perform frequency domain decomposition in the sRGB space, and introduce an implicit-guided hybrid representation strategy that effectively separates intricate compounded degradations. In the backbone network design, we develop retinal decomposition network guided by implicit degradation representation mechanisms. Extensive experiments demonstrate the superiority of our method. The code will be released soon.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces an interpretable, unsupervised framework for joint denoising and low-light enhancement of images, focusing on real-world scenarios. 

The method employs physical imaging principles and Retinex theory for decomposing images into illumination and reflection components.

### Strengths
1. The paper combined the Retinex model and data-driven methods since the first effort of RetinexNet. 
2. Experiments are sufficient.
3. Frequency domain decomposition is well-used. 
4. The unsupervised low-light enhancement method is a promising direction. 
5.  The self-supervised denoising method based on neighboring pixel masking is well-aligned with the challenges of handling zero-reference images.

### Weaknesses
1. For low-light enhancement task, I want to see more results on LIME, NPE, MEF, DICM and VV. Since these datasets do not have ground truth, then is more fair to justify the effectiveness.

2. Missing citations of real-world low-light enhancement methods,
[1] Enhancing Visibility in Nighttime Haze Images Using Guided APSF and Gradient Adaptive Convolution

3. The paper lacks a discussion on the computational complexity and runtime efficiency of the proposed model.

### Questions
1. How does the proposed method handle edge cases such as extreme noise or heavy color distortions, which may not follow typical low-light degradation patterns?

2. Given the success of the DCT-based frequency decomposition, have the authors considered combining this with other frequency-domain transforms (e.g., wavelets) to enhance robustness across diverse types of degradation?

### Soundness
3

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
This paper proposes an interpretable unsupervised joint denoising and enhancement method suitable for real-world low-light scenes. Based on the physical imaging principles and Retinex theory, discrete cosine transform (DCT) is used for frequency domain decomposition, and an implicitly guided hybrid representation strategy is introduced to effectively separate complex compound degradations, thereby realizing the detection and optimization of complex degradation problems caused by low-light conditions. The authors conduct experiments to verify the effectiveness of the proposed method.

### Strengths
1. The authors explore the difficulties traditional methods face in dealing with complex degradation issues such as noise, brightness, and contrast, and propose solutions that significantly outperform existing technologies.
2. Technically, the authors introduce a spatial frequency domain filtering module that uses discrete cosine transformfor explicit multi-band separation, which facilitates the decomposition of enhanced images into illumination and reflectance maps.
3. Experiments depict the effectiveness of the proposed method on multiple datasets.

### Weaknesses
1. Some of the latest methods are not compared, such as RetinexFormer， and Rerinex-Diffusion. Besides, the experiments do not provide statistical indicators such as standard deviation or confidence interval in Table 1 and Table 2, which makes the reliability and stability of the results unclear. Moreover, the generalization ability of the proposed method is not explored, for example, when training the method in low-light environment and testing it one other exposure scenes.

2.  Although authors claim the proposed method is new, quantities of methods have explored introducing frequency-based techniques into image enhancement including some components-decomposition-based methods (such as [1])， what are the special characteristics of the proposed method that introducing the techniques that used above into retinex-based mechanism?

[1] Unveiling Advanced Frequency Disentanglement Paradigm for Low-Light Image Enhancement, ECCV 2024.

3.  There are too few visual results, for example, the visualization results of more real-world scenes (other low-light datasets or other exposure scenes) can be provided. Moreover, the detailed mechanism of why the proposed method works is not presented. How it has better performance than previous methods?

### Questions
Please see the Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this article, to address the complex degradation issues of images in low-light scenarios, the author proposes a training strategy based on physical imaging principles and retinal theory. Specifically, first, the author derives a novel training strategy from paired images under varying lighting conditions and noise levels; second, the author introduces an implicit guidance hybrid representation strategy through DCT transformation, effectively separating complex composite degradation; finally, the author develops a retinal decomposition network based on the implicit degradation representation mechanism. The article demonstrates the effectiveness and reliability of the proposed method through extensive experiments.

### Strengths
1. The author proposes a novel retinal decomposition network based on an implicit degradation representation mechanism in the article, which shows certain effectiveness in image enhancement for low-light scenarios;
2. The language of the article adheres to English writing standards and is fluent;
3. The article provides mathematical proofs for each module of the network, making the logic of the article strong;

### Weaknesses
1. On page 4, lines 175-180, the author proposes the use of Discrete Cosine Transform (DCT) to separate different frequencies of images (including chromatic, semantic information, edge contours, and noise intensity). What is the theoretical basis for this approach? Or is it more of an empirical practice? If so, would the performance of the model be affected if different methods were used to decompose the feature maps after Discrete Cosine Transform? Specifically, while DCT is known for its energy compaction properties, the claim that it directly separates semantic information, edge contours, and noise into distinct frequency bands requires more rigorous justification. The typical application of DCT in image processing involves separating low-frequency components (representing smooth regions) from high-frequency components (representing edges and textures), but the direct mapping to semantic information is not a standard interpretation. The authors should clarify whether they are observing a correlation or a causal relationship, and provide evidence that this separation is consistent across different image types and degradation levels.

2. On page 6, lines 322-333, the author presents the loss function of the model. However, during the experiments, the author seems to have not conducted an in-depth exploration between the loss function and the performance of the model. If such research were included, it would make the argument of the paper more complete. The loss function appears to be a weighted combination of several terms, but the rationale behind the specific weights and the impact of each term on the final performance are not thoroughly discussed. For example, how sensitive is the model to changes in the weights of the individual loss components? Are there any specific scenarios where one loss term dominates the others, and what are the implications for the model's behavior? A more detailed analysis of the loss function's landscape and its effect on the optimization process is needed to fully understand the model's training dynamics.

### Questions
1. On page 4, lines 175-180, the author proposes the use of Discrete Cosine Transform (DCT) to separate different frequencies of images (including chromatic, semantic information, edge contours, and noise intensity). What is the theoretical basis for this approach? Or is it more of an empirical practice? If so, would the performance of the model be affected if different methods were used to decompose the feature maps after Discrete Cosine Transform?
2. On page 6, lines 322-333, the author presents the loss function of the model. However, during the experiments, the author seems to have not conducted an in-depth exploration between the loss function and the performance of the model. If such research were included, it would make the argument of the paper more complete.

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
This manuscript introduces an interpretable, unsupervised framework designed to enhance and denoise real-world low-light images without the need for paired training data. The proposed method leverages physical imaging principles and retinex theory to derive a training strategy based on paired sub-images with varying illumination and noise levels. The framework employs the Discrete Cosine Transform (DCT) to perform frequency domain decomposition in the sRGB space.

### Strengths
1. It is technically sound to incorporate the neighbor2neighbor denoiser with the task of unsupervised LLIE 
2. The authors provided code in the supplementary materials.

### Weaknesses
1. In Equation (8), the term P1 is introduced without prior explanation, and it appears that the FIcoder is omitted in the process. Additionally, while the authors describe P1 in Equation (15), the description is still quite vague. Could the authors please clarify the shape of P1, how it is learned, what constraints are used, and whether it can be visualized?

2. If Equations (9) and (13) are identical to the standard DCT/IDCT transformations, there is no need to present them in the paper.

3. In Equation (14), the L_{reg} term is not explained. Could the authors please provide an explanation for this term?

4. In Equation (15), what is the difference between the first and third terms? Additionally, the authors are requested to show several decomposed illumination and reflection maps to demonstrate that the constraints in this equation are sufficient to learn reasonable Retinex decomposition results.

5. On Line 150, the reference year for noise2noise is incorrect; the paper was published in 2018, not 1803.

6. Figures 1, 2, 3, and 5 are not explained in the main text (at least I could not find them), while Figure 4 is explained but not correctly referenced.

7. In Figure 6, I do not see the advantage of the author's method over the SCI method, and the authors avoid explaining this point in the paper.

8. In Figure 7, the author's method still leaves noticeable noise, which I did not see in the Neighbor2Neighbor comparative experiment. Is there an issue with the author's training process?

9. The authors should introduce qualitative comparisons on an independent test set to demonstrate the superiority of their generalization performance. I personally believe this is a key experiment to distinguish whether a low-light enhancement model is valuable, and it should also be an advantage of unsupervised methods. Recommended datasets include LIME, NPE, MEF, DICM, and VV, as used in the Retinexformer.

### Questions
See the weakness.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper develops a zero-reference joint denoising and low-light enhancement framework designed for real-world applications. 
The framework incorporates a self-supervised optimization strategy and physical priors to effectively capture complex degradations. 
Grounded in Retinex theory, the optimization process generates paired low-light and enhanced images by dynamically adjusting brightness, thereby establishing mutual self-supervision. 
A Discrete Cosine Transform (DCT) is employed to extract degradation representations across varying levels, facilitating degradation decomposition and removal within the frequency domain.

### Strengths
1. This paper presents a zero-reference joint denoising and low-light enhancement framework that operates without the need for paired or unpaired images, a crucial feature for real-world applications.

2. The framework introduces a novel neighboring pixel masking strategy and creates paired images with varying brightness levels to enable self-supervised image denoising and decomposition.

3. Experiments on real-world datasets show that the proposed framework outperforms existing zero-reference low-light image enhancement methods.

### Weaknesses
1. The reviewer notes that the proposed neighboring pixel masking strategy appears to draw from methods like Neighbor2Neighbor [1] and MAE [2], which are known to sometimes produce over-smoothed results. The authors are encouraged to clarify the differences between their approach and these methods, highlighting any improvements that address over-smoothing issues. Specifically, the paper should detail how the masking strategy avoids averaging out high-frequency details, which is a common problem with methods that rely on pixel neighborhood information.

2. Conducting ablation studies on the size of the neighboring mask would be beneficial to assess its impact on preserving texture details. Such analysis should include a range of mask sizes and shapes, and quantify the trade-off between noise reduction and detail preservation using appropriate metrics. The analysis should also investigate how different mask sizes affect the model's ability to capture fine-grained image structures.

3. The exposure loss function relies on a pre-defined exposure level, similar to the approach in Zero-DCE. However, in scenarios with non-uniform or overexposure, the results may tend toward overexposure and color distortion. The authors are encouraged to consider integrating an adaptive exposure adjustment strategy in future work to address these limitations. The paper should discuss how the fixed exposure target might lead to artifacts in regions with varying illumination and propose a mechanism to dynamically adjust the target exposure based on local image statistics.

4. While the authors claim that the proposed framework can both denoise and enhance images, the LOL dataset—characterized by slight noise degradation—may not fully validate its denoising capabilities. It would be beneficial to conduct experiments on low-light image enhancement datasets with significant noise levels, such as LSRW or other image denoising datasets, to substantiate the framework's performance in more challenging conditions. The paper needs to demonstrate the effectiveness of the denoising component by evaluating on datasets with varying noise levels and types, and provide a comparative analysis with state-of-the-art denoising methods.

### Questions
Please refer to Weaknesses

### Soundness
2

### Presentation
3

### Contribution
2
