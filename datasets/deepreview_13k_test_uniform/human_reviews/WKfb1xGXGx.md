# Perm: A Parametric Representation for Multi-Style 3D Hair Modeling

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
We present \textsc{Perm}, a learned parametric model of human 3D hair designed to facilitate various hair-related applications. Unlike previous work that jointly models the global hair shape and local strand details, we propose to disentangle them using a PCA-based strand representation in the frequency domain, thereby allowing more precise editing and output control. Specifically, we leverage our strand representation to fit and decompose hair geometry textures into low- to high-frequency hair structures. These decomposed textures are later parameterized with different generative models, emulating common stages in the hair modeling process. We conduct extensive experiments to validate the architecture design of \textsc{Perm}, and finally deploy the trained model as a generic prior to solve task-agnostic problems, further showcasing its flexibility and superiority in tasks such as 3D hair parameterization, hairstyle interpolation, single-view hair reconstruction, and hair-conditioned image generation. Our code, data, and supplemental can be found at our project page: \url{https://cs.yale.edu/homes/che/projects/perm/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents PERM, a parametric model for representing 3D hair, designed to efficiently handle hair synthesis, editing, and reconstruction. PERM disentangles global hair structure and local curl patterns using a PCA-based strand representation in the frequency domain, enabling intuitive editing and precise control. The model architecture combines StyleGAN2 and VAE networks to generate guide and residual textures, capturing both broad and detailed features of hair. PERM performs well across tasks like single-view hair reconstruction and hairstyle editing, often surpassing task-specific methods. The approach is lightweight, computationally efficient, and achieves high fidelity, providing a robust framework for diverse hair modeling applications.

### Strengths
The strengths of the paper include its use of a PCA-based strand representation for 3D hair that efficiently disentangles global and local hair details, enabling precise control and intuitive editing. The PERM model’s architecture is computationally lightweight and achieves high fidelity with reduced memory and training requirements. It showcases versatility by performing well across various applications like single-view reconstruction and hairstyle editing, often matching or surpassing specialized, task-specific methods. Additionally, the framework’s modularity makes it adaptable for different hair modeling tasks, enhancing its practical value in digital human applications.

### Weaknesses
While the motivation of this paper is clear and the introduction is enjoyable to read, I am extremely frustrated with the forward-referencing (or no-referencing) writing style in Section 3. I often have to hold many questions until much later in the text, making it so easy to lose track of the mathematical flow. For example, Figure 4 starts with StyleGAN, but it is not properly introduced until Section 3.2. The same issue occurs with guide textures, residual textures, and many other components. The strand parameterization function S() , which is the last step in the diagram of Figure 4, is introduced first in the subsections, while preceding steps are explained in a recursive manner. The PCA coefficients, \gamma, are not explicitly present on the RHS of Eq 1. I understand that they are outputs of the guide textures, but I was so clueless when first looking at it until very late in Section 3. Additionally, the function  M()  on the LHS of Equation 1 was never properly introduced. I am concerned that this paper requires a major revision.

The paper presents the method as a parametric model, but unlike deterministic models such as SMPL or FLAME, it lacks a clear deterministic nature as it involves stochastic elements (e.g., generative processes or randomness in texture synthesis). This ambiguity raises questions about the consistency and reproducibility of the model’s outputs. You won’t be able to encode hair geometry into a fixed set of parameters and then decode it back accurately.

### Questions
Is  S = {p1 , p2 , . . . , pL }   the output of Equation 2? The way it is drafted in line 212 makes it seem like it should be an input to the subsequent equation.

Line 230 states that “Our analysis reveals that the first 10 PCA coefficients are enough to effectively capture the global structure of each strand, and the remaining 54 coefficients encode high-frequency details, such as curl patterns”. Where is this analysis? This is another place where I am frustrated by no-referencing.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposed perm, a learning-based parametric representation for hair modeling. A PCA-based strand representation in the frequency domain is proposed to jointly model the global hair structure and local curl patterns, enabling hair editing and other downstream tasks. The authors have conductive comprehensive experiments, including comparisons to other representations, ablation studies, and demonstrations on downstream tasks, showing the great potential of the proposed hair parameterization model.

### Strengths
- The frequency domain PCA for hair strands is neat. Also, 10 coeffs for coarse strands and 54 coeffs for detailed curls is reasonable and straightforward.

- The proposed framework is meticulously designed. The model can be applied to differentiable optimization/rendering. I did not find an obvious fallback of the proposed framework.

- The evaluation of the paper is comprehensive, including comparisons with other methods, ablation studies on different key components, and exemplar downstream tasks. From my perspective, the authors successfully demonstrate the effectiveness/SOTA performance of the proposed representation.

### Weaknesses
I am not an expert in hair modeling and I did not find obvious fallbacks of the proposed framework. Below I listed the questions raised after reading the manuscript:

- From single view reconstruction results in Fig. 10, I find that the current SOTA is a good fit for the hair in the input image. However, the hair details are still misaligned. Is this restricted by model capacity given the current parameterization? (I understand hair modeling is very difficult). Are there any suggestions to improve the parameterization (e.g., modeling the random strands in the input image)?

- Is it possible (or how) to combine the proposed method with NeRF/3DGS for realistic full-head/full-body reconstruction?

### Questions
The two questions are listed above.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes PERM, a lightweight and generic parametric representation of 3D human hair.  The proposed PERM method contributes to the field of 3D hair modeling by providing a lightweight, generic, and editable parametric representation that addresses the limitations of existing methods and enables versatile applications in various hair-related tasks.

Specifically, a novel parametric representation of 3D human hair, PERM, is introduced.   To independently control the global structure and curl pattern, a strand representation based on principal component analysis (PCA) in the frequency domain is proposed.  The learned principal components form an interpretable space for hair decomposition, where initial components capture low-frequency information, and subsequent components encode high-frequency details.  The paper follows previous literature to compute the UV of the scalp and map the geometry features of each strand onto a 2D texture based on its root position.  With the strand PCA representation, dominant coefficients fit and are stored in guide textures, and higher-order coefficients are stored in residual textures for detailed strand patterns.

### Strengths
The paper focuses on the hot topic of 3D hair parametric modeling and innovatively proposes a strand representation method based on Principal Component Analysis (PCA) in the frequency domain.  The paper is clearly articulated, with a rigorous technical approach and strong innovation.  The rendering results presented in the experimental stage effectively demonstrate the effectiveness of the method.

The authors have conducted extensive and in-depth experimental validations.  At the strand representation level, they have fully demonstrated the superiority of the PCA-based strand representation method compared to other representation approaches through comparative experiments.  In terms of full hair representation, the authors have compared the effectiveness with the Groom-Gen method.  Furthermore, the authors have showcased the broad application effects of the proposed parametric model in multiple tasks, including single-view hair reconstruction, perm parameter editing, and hair-conditioned image generation, fully proving the method's promising application prospects.

### Weaknesses
The paper only compared Groom-Gen and presented a limited number of samples, making it difficult to analyze the strengths and weaknesses of the two approaches comprehensively. To more accurately evaluate the methods, it is suggested that the number of samples in the comparison experiments be increased.

Furthermore, the paper did not discuss any failure cases of the proposed method. I am particularly interested in the failure cases of the method in random synthesis and single-view reconstruction tasks. Presenting these failure cases would help to elucidate the limitations of the proposed approach more clearly.

### Questions
As explained in the "weaknesses", my primary concerns lie in the experiments section.      I hope that the authors can provide detailed responses and explanations to the following specific issues:

* In the comparison with GroomGen, it is evident that all random sampling results generated by GroomGen exhibit markedly unrealistic strand structures.      How can this phenomenon be explained?

* In Figure 5, the rendering results of the PCA method and the authors' proposed Freq. PCA (Ours) methods are similar, to the extent that they are almost indistinguishable by visual inspection.      Could the authors further elaborate on the differences and merits of these two methods in terms of specific rendering details?

* What is the extent of the impact of Guide Texture Upsampling on the final rendering results?  Incorporating an ablation study on the upsampling module is crucial for comprehensively evaluating its significance and contribution.

* I suggest that the authors showcase failure cases encountered in random generated and single-view reconstruction tasks, and provide a thorough analysis and discussion of such cases.      This not only helps to uncover potential limitations of the current method but also offers valuable insights and references for future research endeavors.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces **PERM**, a parametric representation for 3D human hair designed to improve a variety of hair-related applications. Unlike previous models that combine global hair structure and local curl patterns, PERM separates these elements using a **PCA-based strand representation** in the frequency domain. This allows for more precise control and editing by decomposing hair textures into different frequency levels, from low to high. Each frequency level is then parameterized with distinct generative models to mimic typical hair grooming stages. Experiments validate PERM's architecture, and the trained model is applied as a flexible prior for various tasks, including single-view hair reconstruction, hairstyle editing, and hair-conditioned image generation.

### Strengths
1. The proposed pipeline, as illustrated in Fig. 4, looks reasonable and straightforward.
2. The paper is well polished, and the experiments are sound.

### Weaknesses
N/A since I am not an expert in this area. A potential improvement direction, from my perspective, is to demonstrate the proposed representation on 3D generation tasks / other amortized pipelines, such as X-conditioned 3D avatar (with controllable hair) generation. E.g., as in Gaussian3Diff (ECCV 24'), the UV space can be used for 3D diffusion training for full head synthesis, and I think that pipeline is applicable to this proposed method.

### Questions
Regarding the overview pipeline, is the residual branch necessary, since the StyleGAN model with U-Net SR module can already generate pretty fine-grained results (intuitively). If this branch is removable, I believe the proposed pipeline will be more neat.

### Soundness
3

### Presentation
3

### Contribution
3
