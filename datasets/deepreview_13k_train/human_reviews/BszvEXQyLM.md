# Phase-Aware KANGaussian : Phase-Regularized 3D Gaussian Splatting with Kolmogorov-Arnold Network

- Decision: Reject
- Scores: 3, 6, 5, 3

## Abstract
Vanilla 3D Gaussian Splatting struggles with modelling high frequency details, especially in unbounded scenes. Recent works such as Scaffold-GS and Spec-Gaussian have made tremendous improvements to the reconstruction quality of these high frequency details, specifically in synthetic and bounded scenes, but still struggle with unbounded real world scenes. Therefore, we propose Phase-Aware KANGaussian, a model building on these earlier contributions to produce state-of-the-art reconstruction quality for unbounded real world scenes with greatly improved high frequency details. Phase-Aware KANGaussian introduces a novel phase regularization method that optimizes models from low-to-high frequency, dramatically improving the quality of high frequency details. Phase-Aware KANGaussian is also one of the first few papers to integrate a Kolmogorov-Arnold Network (KAN) into the Gaussian Splatting rendering pipeline to verify its performance against the Multilayer Perceptron (MLP). All in all, Phase-Aware KANGaussian has three main contributions: (1) Introduce a Gaussian Splatting model with state-of-the-art performance in modelling real-world unbounded scenes with high frequency details, (2) a novel phase regularization technique to encode spatial representation and lastly, (3) first few to introduce a KAN into the Gaussian Splatting rendering pipeline.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a 3DGS method Phase-Aware KANGaussian method, which aims to enhance 3D reconstruction quality, particularly for capturing high-frequency details in unbounded real-world scenes. The authors propose a novel phase regularization technique that progressively optimizes model training across frequencies from low to high. Additionally, they integrate the Kolmogorov-Arnold Network (KAN) into anisotropic color modeling.

### Strengths
The introduction of KAN for modeling anisotropic color is novel. It might be theoretically better than MLP, as KAN exhibits a locality property due to its B-Splines as claimed in Line 245-246 and Figure 4.

### Weaknesses
## Major Concerns:
1. The novelty of phase regularization is questionable. FreGS [R1] has already provided frequency regularization on both amplitudes and phase parts. Equation 7 in this paper is similar to Equation 6 in FreGS. Besides, this paper introduces frequency filtering by expanding the frequency band, which is similar to the frequency annealing proposed in FreGS. For example, Equation 17 in this paper is similar to Equation 13 in FreGS. The core difference, if any, between the proposed method and FreGS is not clearly articulated. Specifically, the claim that only the phase term is regularized is not sufficiently justified, as the amplitude also carries spatial information, and the impact of excluding it requires more rigorous analysis. A comprehensive experimental comparison to validate the superior advantage of the proposed method, including a direct comparison with FreGS, is necessary to demonstrate the effectiveness of the proposed phase-only regularization.

2. The lack of evaluation on synthetic datasets is a significant oversight. The authors claim SOTA performance on real unbounded scenes, but they should also validate the proposed method on synthetic shiny scenes, as used in Spec-Gaussian [R2] and [R3]. These datasets are crucial for evaluating the method's ability to handle complex reflections and specularities, which are often present in real-world scenarios. Without these evaluations, the generalizability of the proposed method remains questionable.

3. The experimental results presented in Table 1 for comparisons with Scaffold-GS [R4] raise serious concerns. Specifically, the performance of Scaffold-GS on Mip-NeRF 360 is notably lower than the values reported in the original paper, whereas results on the other two datasets are the same. The authors do not clarify whether these results are based on retrained models or reporting values from the original work. This discrepancy undermines the validity of the comparisons and the conclusions drawn from them. A detailed description of the experimental setup, including whether models were retrained, is crucial, and an explanation for the observed discrepancies in these results is necessary.

4. The presented experimental results are not fully convincing. For instance, in the overall comparison of real datasets (Table 1), the proposed method ranks second in PSNR, underperforming compared to Spec-Gaussian [R2]. Additionally, in the ablation studies, the “No KAN” variant surprisingly outperforms the proposed method on Mip-NeRF 360 and Tanks&Temples in SSIM and LPIPS. Given SSIM and LPIPS’ importance in assessing texture detail, these results suggest that the proposed method may not be effectively capturing high-frequency details. More thorough explanations and additional experiments are needed to validate the effectiveness of each module, particularly the KAN-based color modeling and the phase regularization.

5. A direct comparison between the Kolmogorov-Arnold Network (KAN) and the MLP used in Spec-Gaussian [R2] is missing. The authors claim that KANs have a locality property due to their B-Splines, but this advantage is not clearly demonstrated in the experiments, as the results do not consistently surpass Spec-Gaussian on PSNR (Table 1). Further evidence, including a direct comparison with a similarly sized MLP, is needed to substantiate the choice of KAN over MLP. The computational cost and memory usage of KAN should also be compared to MLP.

6. The hyperparameters are not provided, e.g., the scalar terms of production of scale and phase regularization (Equation 19) used in experiments. The lack of hyperparameter details makes it difficult to reproduce the results and assess the robustness of the method. An analysis or explanation of hyperparameter choice is essential to understand the sensitivity of the method to different parameter settings.

7. Certain aspects of the writing lack clarity and structural coherence, hindering readability and comprehension of the paper’s innovations. Here are some examples:
* Lines 253-254: Potential confusion between “spherical Gaussians” and “spherical harmonics.”
* Lines 259-260: Grammar issues in explaining the smooth and exponential terms.
* Line 402: Mislabeling “\lambda_{prod}” as “\lambda_{}”.

### Questions
see above

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This study investigates integrating KAN into the 3DGS framework to enhance rendering quality. By replacing MLP with KAN in Neural-Appearance GS techniques like Scaffold-GS, the authors achieve improved visual outcomes. Phase regularization is applied to further refine the visuals, leading to satisfactory results. However, the approach is somewhat limited, as it combines KAN and GS directly on color prediction, serving as a continuation of Scaffold-GS and Spec-GS.

### Strengths
1. The paper excels in presenting a novel integration of KAN within the 3DGS framework, leading to significant improvements in rendering quality. The authors effectively demonstrate how replacing MLP with KAN in established methods like Spec-Gaussian and Fre-GS enhances visual outcomes. This innovative approach not only improves the clarity and detail of rendered images but also introduces phase regularization to refine the results further.

2. The paper is well-organized and clearly written, making complex concepts accessible to readers. The authors provide comprehensive ablation studies and figure illustrations that thoroughly support their claims, showcasing the superiority of KANGaussian over traditional methods in real-world scenarios. The method's potential to handle high-frequency details and improve visual fidelity is well-articulated, backed by detailed experimental results that highlight its practical applicability and robustness.

### Weaknesses
1. There is no comparison of training time and rendering speed. One of Gaussian's greatest advantages is its fast rendering and minimal training time. Including quantitative measurements of training and inference time would clarify KAN's impact on GS.

2. As mentioned in the summary, I find the direct combination of KAN and GS in the well-explored area of neural GS appearance to be somewhat trivial. However, I believe that experimenting with novel technique combinations and sharing results benefits the community. I encourage such efforts, especially when the technique is straightforward. The results, though, are not significantly superior to other methods.

### Questions
I hope the author reports the training and inference speeds, as these are two of GS's greatest advantages and are of significant interest to readers.

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
5

### Summary
This paper aims to apply KAN within the 3DGS framework to achieve higher-quality rendering. The authors primarily build upon Spec-Gaussian, Scaffold-GS, and Fre-GS, replacing the MLP with KAN, which results in improved rendering quality. Additionally, phase regularization is introduced to further enhance visual results. The experimental results show that KANGaussian achieves impressive results in real-world scenarios.

### Strengths
- This paper is well-written and easy to understand.
- The use of KAN in Gaussian splatting is novel.
- The impressive visual results and ablation studies are appreciated.

### Weaknesses
1. This paper lacks sufficiently novel methods. For example, Sections 3.2.1 and 3.2.2 are largely based on Spec-Gaussian (with the exception of differences in KAN and MLP). Section 3.2.3, on the other hand, is based on Fre-GS. The paper seems to be a KAN version that combines Spec-Gaussian with Fre-GS. I recommend that the authors move parts of these sections to the Preliminary section.
2. The authors dedicated a significant portion of the paper to explaining how KANGaussian theoretically offers a higher capacity for modeling high-frequency information. However, in the Experiments section, there are no examples that demonstrate improvements in modeling specular components; instead, the focus is on floater removal, as seen in Figure 7. It could be much better if the authors used scenes with specular highlights, such as the example shown in Figure 5, to substantiate their claims and prove the effectiveness of their method in improving specular modeling.
3. Missing comparison of training time and rendering efficiency (FPS). There is still a computational speed difference between KAN and MLP. Although KANGaussian may not have an advantage in rendering speed, it could be much better to provide these details to give readers a clearer understanding of the strengths and weaknesses of the KAN-based approach. 
4. Missing comparison of the number of Gaussians. The quantity of Gaussians has a significant impact on rendering metrics, and the authors need to provide a comparison of the actual number of Gaussians used in each method to ensure a fair comparison.

### Questions
I'm very curious about the resolution the authors used for Mip-NeRF 360. Did they follow the Mip-360 setup with downsampling factors of 4 for outdoor scenes and 2 for indoor scenes, or did they adopt the 3DGS setting where the images are uniformly cropped to a width of 1600 pixels?

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
The paper presents "Phase-Aware KANGaussian," a 3D reconstruction model that enhances the detail and quality of unbounded real-world scenes, particularly in high-frequency details. Its contributions can be summarised as:
1. Integrated 3D Gaussian Splatting with a Kolmogorov-Arnold Network (KAN) in the rendering procedure for improving rendering quality.
2. A phase regularization technique aimed at optimizing models from low to high frequency to dramatically enhance high-frequency detail rendering, which involves filtering before computing a regularization term in the Fourier domain.

### Strengths
1. The use of Kolmogorov-Arnold Networks in the 3DGS rendering pipeline is innovative, and the authors are the first few who are doing this.
2. The phase regularization approach for controlling frequency details during training could lead to more precise control over detail rendering in complex scenes.
3. The derivation of the formulas and the figures in the front part are used appropriately and clearly.
4. The problem is well stated.

### Weaknesses
1. The motivation for integrating KAN into 3DGS is not clear. How is the locality property of KANs expected to benefit the modeling of specular highlights and other high-frequency details? The paper does not provide a clear justification for why KANs, with their inherent locality, are suitable for capturing global scene properties or view-dependent effects, which are often crucial for high-frequency details like specularities. A more detailed explanation of how KAN's architecture aligns with the specific challenges of 3DGS rendering is needed.
2. The author put too much content in PRELIMINARIES and it feels like this article was cobbled together. Can you reorganize the preliminaries section to focus more tightly on the concepts most crucial to understanding the novel contributions? The current preliminaries section includes a lot of background information that is not directly relevant to the core contributions of the paper, making it difficult to follow the main ideas. The section needs to be streamlined to focus on the specific aspects of 3DGS and frequency analysis that are directly relevant to the proposed method.
3. There is a potential risk of overfitting to high-frequency details at the expense of overall scene fidelity, as indicated by the slightly lower PSNR scores compared to Spec-Gaussians. The paper needs to provide a more thorough analysis of the trade-off between high-frequency detail and overall reconstruction quality. The lower PSNR scores suggest that the model might be prioritizing high-frequency details at the cost of lower-frequency components, which can lead to artifacts and a less faithful reconstruction of the overall scene structure.
4. The baseline (Spec-Gaussian (Yang, 2024)) of this article is not a peer-reviewed article, if there are peer-reviewed alternatives that could serve as additional comparisons? It is important to compare against established, peer-reviewed methods to properly evaluate the performance of the proposed approach. The lack of comparison with peer-reviewed baselines makes it difficult to assess the true novelty and effectiveness of the proposed method.
5. The ablation study is confusing. e.g. Does "Phase Regularization (Ours)" contain Kan or does it only contain Phase Regularization? If does not, then which one is “No Kan” supposed to be compared to? Please provide a clear description of each ablation condition, including which components are present or absent in each case. The ablation study lacks clarity in defining the different configurations being tested. It is unclear which components are included or excluded in each ablation, making it difficult to understand the impact of each component on the overall performance.

### Questions
1. The figure on Page 9 is too small. I have to zoom in "300%" to see it.
2. Please check whether the citation format is suitable for ICLR 2025. Sometimes the names of people are mixed with the sentences of the article, making it confusing. For example, "we employ Kolmogorov Arnold Networks (KANs) in the rendering pipeline in contrast to earlier works Lu et al. (2023)" -> "we employ Kolmogorov Arnold Networks (KANs) in the rendering pipeline in contrast to earlier works (Lu & Yu, 2023)"
3. Could you have some visual results for the ablation study? For example, some of your model's visual results remove some of your components.
4. Could you provide insights into the computational demands of your model, particularly regarding the use of KAN? (how much slower?)
5. How does the model perform under varied lighting conditions and metal areas, especially given its focus on high-frequency details which can be highly sensitive to such changes?
6. Could you elaborate on the potential causes for the observed decrease in PSNR?
7. There is an error in 3.2.4. "and λ□ are scalar values to adjust..."
8. What are the differences and advantages of your model over Mip-Splatting[1], which also focuses on high frequency?

[1] Yu, Z., Chen, A., Huang, B., Sattler, T. and Geiger, A., 2024. Mip-splatting: Alias-free 3d gaussian splatting. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 19447-19456).

### Soundness
3

### Presentation
3

### Contribution
2
