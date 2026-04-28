# Visibility-Uncertainty-guided 3D Gaussian Inpainting via Scene Conceptional Learning

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
3D Gaussian Splatting (3DGS) has emerged as a powerful and efficient 3D representation for novel view synthesis. This paper extends 3DGS capabilities to inpainting, where masked objects in a scene are replaced with new contents that blend seamlessly with the surroundings. Unlike 2D image inpainting, 3D Gaussian inpainting (3DGI) faces the challenge of effectively leveraging complementary visual and semantic cues from multiple input views, as occluded areas in one view may be visible in others. To address this, we propose a method that measures the visibility uncertainties of 3D points across different input views and uses them to guide 3DGI in utilizing complementary visual cues. We also employ the uncertainties to learn a semantic concept of the scene without the masked object and use a diffusion model to fill masked objects in the input images based on the learned concept. Finally, we build a novel 3DGI framework VISTA by integrating VISibility-uncerTainty-guided 3DGI with scene conceptuAl learning. VISTA generates high-quality 3DGS models capable of synthesizing artifact-free and naturally inpainted novel views. Furthermore, our approach extends to handling dynamic distractors arising from temporal object changes, enhancing its versatility in diverse scene reconstruction scenarios. We demonstrate the superior performance of our method over state-of-the-art techniques using two challenging datasets: the SPIn-NeRF dataset, featuring 10 diverse static 3D inpainting scenes, and an underwater 3D inpainting dataset derived from UTB180, which includes fast-moving fish as inpainting targets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents VISTA, a novel framework for 3D Gaussian inpainting that leverages visibility uncertainty and scene conceptual learning to address the challenges of inpainting in both static and dynamic scenes. The authors propose a method that integrates visibility uncertainty maps to guide the inpainting process, allowing for more coherent and contextually appropriate fills for masked regions. The framework is evaluated on two challenging datasets, demonstrating superior performance compared to existing state-of-the-art methods.

### Strengths
•	Originality: The integration of visibility uncertainty with scene conceptual learning is a fresh approach that addresses existing limitations in 3D inpainting. Although the idea is intuitively sample, but the performance is good under the complementary visual cues.

•	Quality: The experiments are robust, showcasing the effectiveness of the proposed method across diverse datasets. The paper also shows some ablation study in discussion and appendix section to support the results.

•	Clarity: The main ideas are presented clearly, and the paper provides a comprehensive overview of related work and the proposed contributions.

•	Significance: The results indicate potential applications in augmented and virtual reality, highlighting the practical implications of the research.

### Weaknesses
•	While the paper presents a robust methodology, certain experimental comparisons could be expanded. For instance, a more detailed analysis of the impact of diﬀerent hyperparameters on performance would provide deeper insights, particularly regarding the parameter v in equation (3) and the level of decrease initial noise during inference. Specifically, the paper lacks a systematic exploration of how varying the initial value and the incremental step size of \( \vartheta \) affects the convergence rate and the final inpainting quality. Similarly, the noise reduction strategy during the diffusion inference process needs more rigorous analysis. It is unclear how the choice of a fixed reduction ratio impacts the trade-off between convergence speed and the quality of the generated content. A more thorough ablation study is needed to justify the current selection of these parameters.

•	There are some writing issues to address: In section 4.1, you state that Figure 1 shows the initial representation’s failure to exclude dynamic objects; however, Figure 1 actually displays the results among diﬀerent approaches rather than the initial representation itself

### Questions
1.	Since the iterative process may slow down the pipeline, how does the computational eﬃciency of VISTA compare to other state‐of‐the‐art methods, particularly in real‐time applications? 

2.	In equation (3), Ui represents the visibility uncertainty map for a single frame, and the uncertainty for each pixel is calculated from equation (2). I would like to know if any normalization is applied to Ui between equations (2) and (3).

3.	Regarding the experimental setup illustrated in the appendix, you mention that the initial noise strength during inference decreases by 0.2 with each iteration. Was any ablation study conducted? I agree that reducing the initial noise over iterations is reasonable, as the rendered image quality becomes more conﬁdent with each iteration, but does this hyperparameter aﬀect the ﬁnal result?

4.	The results in Figure 7 show the reconstruction without a mask, which retains the fish in the top-left corner of the image while removing the other fish. I believe the visibility uncertainty used in Equation (3) to update the mask has favorable properties for removing dynamic distractors. However, why does only the top-left fish remain? Could you also provide some statistical evaluation for this ablation study?

5.	I would also like to inquire about the image resolution used for training and inference with stable‐diﬀusion‐v1.5, as the resolution may inﬂuence the inpainting quality in SD‐1.5

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces VISTA (Visibility-Uncertainty-Guided 3D Gaussian Inpainting via Scene Conceptual Learning), a framework specifically designed for 3D scene inpainting. VISTA combines visibility uncertainty maps with scene conceptual learning to improve inpainting quality across multiple viewpoints. The main contributions include VISTA-GI, which guides 3D Gaussian inpainting across views, and VISTA-CL, which uses scene conceptual learning to fill in areas lacking semantic information. Experimental evaluations demonstrate that VISTA outperforms existing methods on the SPIn-NeRF dataset for static scenes and an underwater dataset with dynamic objects.

### Strengths
1. VISTA introduces a novel multi-view 3D inpainting framework by combining visibility uncertainty maps with a diffusion model. This approach effectively uses complementary information across multiple views and includes scene conceptual learning to handle semantic filling, showing a certain level of originality.

2. The methodology clearly separates VISTA-GI and VISTA-CL, using an alternating iterative optimization to ensure consistency across views. This design handles both static and dynamic objects, broadening the framework’s flexibility for different application scenarios.

### Weaknesses
1. The main contribution of this paper is the introduction of visibility uncertainty to guide inpainting, but the uncertainty map considers only the visibility of 3D points across views without explicitly addressing texture consistency. This may lead to color or texture inconsistencies in the inpainted regions. Further analysis on how the model maintains texture consistency would strengthen this aspect.

2. VISTA-GI is designed to maintain consistency between neighboring views. However, as noted in the appendix, it struggles with scenes that have large viewpoint differences, which haven’t been quantitatively evaluated. Testing on larger viewpoint change would provide a clearer picture of the model's performance in maintaining consistency across wide angles.

3. The framework involves multiple components (visibility uncertainty maps, a diffusion model, and scene conceptual learning), which could increase computational demands. This may impact feasibility in large-scale or real-time applications. Providing more details on computational costs, such as training time, would support its applicability.

4. The paper does not include ablation studies for VISTA-GI and VISTA-CL, making it difficult to assess the individual contribution of each component. Adding these ablation studies would clarify each module’s role in the framework’s overall performance.

5. The paper includes few visual results on the SPIn-NeRF dataset, limiting readers’ understanding of the framework’s effectiveness in static scenes. Providing more visual results across different scenarios, as well as showing the impact of the visibility uncertainty map on static scenes, would help illustrate the method's inpainting capabilities.

6. There is a lack of visualizations of depth maps to verify the geometric accuracy of the inpainting results.

7. The paper does not compare VISTA with GScream[1], which is another 3D inpainting method operating in a similar setting. Including a comparison with GScream would help establish VISTA’s advantages.

### Questions
1. I still have concerns about texture consistency. Could you explain how the model ensures texture consistency in the inpainting results and provides visualizations of texture across different viewpoints in static scenes?

2. I am curious about the performance drop with large viewpoint differences. Could you quantify this to assess VISTA's robustness to viewpoint variations?

3. Could you conduct ablation studies on ***VISTA-GI*** and ***Scene Conceptual Learning*** to show their specific roles within the overall framework?

4. Could you visualize depth maps to demonstrate the geometric accuracy of the inpainting results?

### Soundness
2

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
3

### Summary
The paper introduces a general 3D Gaussian Splats (3DGS) inpainting framework called VISTA, which achieves 3D inpainting for both static and dynamic objects within 3DGS reconstruction, resulting in enhanced novel view synthesis performance.
By leveraging multiview information, the method extracts visibility uncertainty maps to guide the 3D reconstruction of inpainted scenes. Additionally, masked multiviews are employed to learn the scene concept through textual inversion techniques, which improves the accuracy of image inpainting priors. VISTA iteratively inpaints scenes and learns scene concepts from inter-view visibility information, enhancing scene consistency and preserving scene identity during the 3D inpainting process.

### Strengths
1. The work proposed a general 3D Gaussian inpainting framework applicable to both static or dynamic scenes.
2. The proposed VISTA leverages multiview visibility information for more detailed texture consistency, facilitating the inpaiting of unseen areas through conceptual learning.
3. The whole paper is well-written and easy to follow.

### Weaknesses
1. Although the comparison experiments are sufficient and the discussions are insightful, there is a lack of certain experiments, such as an ablation study on the effect of conceptual learning. Please see details in Question 1.
2. The paper does not discuss the multi-view inpainting consistency of this method, nor does it compare the results with or discuss differences from those obtained using video diffusion models. See details in Question 2.

### Questions
1. As a complex scene (e.g. with objects, backgrounds), the scene feature is not as distinct as ojects, is the concetual learning robust in scenes? How the conceptual learning improve inpainting performance?

2. It would be benefitial to discuss multi-view consitency during inpainting, as well as review and discuss video inpainting works which concerns about multi-view consitency.

3. Minor issues:

   3.1. Fig.1 InFusion's upper results with red boxes appears to be incorrectly cropped in misaligned areas?

    3.2. Fig.2 refers to wrong section numbers.

### Soundness
2

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
4

### Summary
This paper introduces a framework for 3D scene inpainting using 3D Gaussian Splatting that leverages multi-view information. The framework consists of two key components: VISTA-GI, which guides inpainting by measuring the visibility uncertainty of 3D points across multiple views, and VISTA-CL, which learns scene concepts without masked objects using a diffusion model. These components work iteratively to refine the 3D representation using geometric and semantic information progressively. The method extends to handling dynamic distractors in scenes, making it effective for challenging scenarios like underwater scenes with moving objects. Evaluated on the SPIn-NeRF dataset and a new underwater dataset derived from UTB180, VISTA demonstrates superior performance over state-of-the-art methods in quantitative metrics and visual quality, particularly in maintaining consistency across viewpoints.

### Strengths
- Novel use of visibility uncertainty to guide 3D inpainting
- Integration of 3D Gaussian Splatting with diffusion-based scene learning
- Iterative refinement combining geometric and semantic cues
- Strong quantitative results across metrics (PSNR, SSIM, LPIPS, etc.)

### Weaknesses
 - Missing analysis of how the visibility uncertainty threshold affects results. Specifically, the paper does not investigate the sensitivity of the method to the threshold $\vartheta$ in Equation (3). Different values of this threshold could lead to varying levels of uncertainty being incorporated, thus impacting the balance between geometric and semantic information used in the refinement process.
- The iterative process requires three iterations, potentially making it computationally expensive for real-time applications. And no clear ablation showing the impact of different numbers of iterations beyond Figure 5. The paper would benefit from a more detailed analysis of the trade-off between the number of iterations and the quality of the inpainting results. For instance, how does the performance degrade with fewer iterations, and is there a point of diminishing returns?
- No discussion of failure cases or limitations with large occlusions. It would be helpful to understand under what conditions the method struggles and what types of artifacts are introduced when it fails.
- Only tested on ten forward-facing scenes from the SPIn-NeRF dataset - a relatively small evaluation set and scenario. This limited evaluation raises concerns about the generalizability of the method to more diverse and complex scenes.
- Missing key hyperparameters like the size of the adjacent view window for uncertainty calculation. The number of adjacent views used to calculate the uncertainty in Equation (2) is a crucial parameter that can affect the accuracy of the uncertainty estimation. The paper should provide this information and discuss its impact on the results.
- No evaluation of common real-world scenarios like removing people from tourist photos. Dynamic object types are limited (mostly fish). While the underwater dataset presents a challenging scenario, testing on more common real-world scenes would strengthen the paper's claims of practical applicability.

### Questions
- What thresholds were used for the visibility uncertainty measure in Equation (2)? How sensitive is the method to these thresholds? Could you provide ablation studies showing how different thresholds affect the final results?
- Why exactly are three iterations optimal? The plot in Figure 5 shows diminishing returns, but could more iterations help in challenging cases? What is the runtime for each iteration? Is real-time performance possible with architectural optimizations?
- Could you provide examples of failure cases and discuss their causes?
- Could you evaluate more diverse scenarios, especially tourist photos with people?

### Soundness
2

### Presentation
2

### Contribution
2
