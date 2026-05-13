# CFG++: Manifold-constrained Classifier Free Guidance for Diffusion Models

- Decision: Accept
- Scores: 6, 6, 8, 1

## Abstract
Classifier-free guidance (CFG) is a fundamental tool in modern diffusion models for text-guided generation. Although effective, CFG has notable drawbacks. For instance, DDIM with CFG lacks invertibility, complicating image editing; furthermore, high guidance scales, essential for high-quality outputs, frequently result in issues like mode collapse. Contrary to the widespread belief that these are inherent limitations of diffusion models,
this paper reveals that the problems actually stem from the off-manifold phenomenon associated with CFG, rather than the diffusion models themselves.
 More specifically, inspired by the recent advancements of diffusion model-based inverse problem solvers (DIS),  we reformulate text-guidance as an inverse problem with a text-conditioned score matching loss and
develop CFG++, a novel approach that tackles the off-manifold challenges inherent in traditional CFG. CFG++ features a surprisingly simple fix to CFG, yet it offers significant improvements, including 
better sample quality for text-to-image generation, invertibility, smaller guidance scales,  reduced mode collapse, etc. Furthermore, CFG++ enables seamless interpolation between unconditional and conditional sampling at lower guidance scales, consistently outperforming traditional CFG at all scales. 
Moreover, CFG++ can be easily integrated into the high-order diffusion solvers  and naturally extends to distilled diffusion models.
Experimental results confirm that our method significantly enhances performance in 
text-to-image generation, DDIM inversion, editing, and solving inverse problems, suggesting a wide-ranging impact and potential applications in various fields that utilize text guidance. Project Page: \url{https://cfgpp-diffusion.io/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes to tackle Classifier Free Guidance's (CFG) limitations, particularly its lack of invertibility and mode collapse. The authors formulate the hypothesis that these limitations come from the off-manifold phenomenon. The proposed method leverages recent approaches developed for inverse problem-solving through diffusion models. The proposed method named CFG++ is compared with CFG for text-to-image generation, image edition or image restoration.

### Strengths
The paper is generally well-written with a useful high-level preliminary section. One of the strengths of the method is its simplicity while being well justified. The paper proposes many experiments showing relative gains compared to CFG.

### Weaknesses
 * The CFG method formulation seems different than in the original paper see eq (6) from (Ho and Salimans, 2021). Moreover, the $w=0$ setting in the experiments should be equivalent to no guidance at all when using CFG according to the eq (6) (from the CFG++ method). In Fig. 6, however, the images appear edited with $w=0$ indicating some contradiction.
* The ImageReward metric is not defined. The FID and CLIP metrics are very similar between CFG and CFG++ especially when using SD v1.5. In Tab. 1 the FID and CLIP are also very close for both methods. This tends to indicate that the gains are relatively marginal even in a low NFE setting.   
* The statement that the proposed CFG++ is invertible and brings more diversity in the generation is not evaluated.

**Typos**

* The variable $x_c$ is not introduced in line 228
* Table 1., column 2, Clip score arrow does not show the correct direction
* line 238 ``a crucial difference in the **renoising** process'' shoulnd't it be denoising?

### Questions
* Having the average performance across the different corruption in Tab. 3 would help. Here, the proposed method seems more efficient than CFG to retrieve the clean image according to the FID metric but not so much according to the LPIPS one. Do the authors have some justifications?
* It is unclear why the performances of CFG drop while augmenting the NFE in Fig. 6 (b).

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces CFG++, a novel approach to fixing the off-manifold issues that can occur in CFG (classifier-free guidance) during sampling. They reformulate CFG as a manifold-constrained problem, transforming the conditional guidance from extrapolation to interpolation between unconditionally sampled trajectories and conditionally sampled trajectories, thus making the guidance more interpretable. Experimental results show that the method can reduce the artifact, solve the DDIM inversion problem, and be integrated into the high-order diffusion solvers.

### Strengths
1. CFG++ introduces a novel approach by redefining classifier-free guidance as a constrained manifold problem, which effectively improves the generation quality by staying within the data manifold.
2. This paper validates the effectiveness of the proposed method on standard benchmarks and different tasks (e.g., text-to-image generation, inversion, editing).
3. The paper is well-written and easy to follow.

### Weaknesses
1. There are a few minor issues in the tables, such as the direction of the arrow in the fourth column of CLIP in Table 1 (which should be as high as possible) and the missing ImageReward metric for SD v1.5 in Table 2.

2. This paper focuses on addressing the inability to perform successful DDIM inversion with classifier-free guidance, so it should include a comparison of the results with this class of methods like [1]. Specifically, the paper should benchmark against methods that explicitly address the inversion problem in diffusion models, demonstrating how CFG++ compares in terms of reconstruction quality and editability. Without such a comparison, it's difficult to assess the true advancement of CFG++ in this specific context.

3. I'm a little suspicious of ''Contrary to the widespread belief that these are inherent limitations of diffusion models, this paper reveals that these problems actually stem from outrageous phenomena associated with CFGs...'' in the Abstract. As far as I know, current work has generally recognized and worked for the CFG problem.  Perhaps rewording would better reflect the originality of the paper.

### Questions
1. SDXL-Turbo does not make use of guidance_scale or negative_prompt. Instead, they disable it with guidance_scale=0.0. I would like to know how to verify the validity of CFG/CFG++ in this case.

2.  Does this method also work for negative prompts?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work introduces an enhanced version of the widely used classifier-free guidance (CFG) technique, CFG++. By formulating conditional generation as an inverse problem and utilizing score distillation sampling (SDS) loss, CFG++ improves various tasks, including text-to-image generation, DDIM inversion-based editing and text-conditioned inverse problems.

### Strengths
Overall, this manuscript is excellent, and I hope it gets accepted. Below, I outline some strengths that support this view:

1. **Well-written**: The paper is well-written with coherent logic and clear notation, making it easy to understand and follow.

2. **Thorough Experiments**: The work studies many downstream tasks, including text-to-image generation for SDv1.5, SDXL, and their distilled versions, as well as DDIM inversion and editing, PF-ODE trajectories, and text-conditioned inverse problems. The authors provide extensive quantitative and qualitative results to show the superiority of the proposed method.

3. **Intriguing Derivation and Analysis**: The derivation of CFG++ is intriguing by treating text-conditioned generation as an inverse problem and utilizing SDS as the loss function. Moreover, the authors present various perspectives to analyze CFG++, including manifold geometry, score matching loss throughout the denoising process, and the evolution of the posterior mean. These analyses are insightful and helpful in understanding the underlying mechanisms of CFG++.

4. **Simple Yet Widely Applicable Method**: The proposed method essentially modifies the re-noising process of the original CFG, but it achieves improvements across various downstream tasks and could be potentially effective for other tasks relevant to the ICLR community. Additionally, the DDIM solver, as well as other popular diffusion solvers like EDM and DPM-Solver, are derived, establishing CFG++ as a general method.

### Weaknesses
Generally, I think there are no obvious weaknesses in this work. However, there are some questions and please refer to the Questions part.

### Questions
1. Only diffusion-/score matching-based generative models are discussed in this work. Could you please **provide some similar derivations for the recent flow matching-based generative models, such as SD3 and FLUX**? I believe similar conclusions stand for flow-based methods, and it will make this work more comprehensive.

2. Is it possible to **disentangle two noises used in the denoising and renoising process**? For example, we can set different hyperparameters $\lambda_1$ and $\lambda_2$ for $(\epsilon_c-\epsilon)$, and use this term in different weights for denoising and renoising respectively. Setting $\lambda_1=\lambda_2$ is the same as CFG and setting $\lambda_2=0$ is the same as CFG++.

3. Is it possible to **provide derivations of CFG++ for other diffusion solvers**, except DDIM? Extensions of CFG++ to other solvers in Appendix A are more like intuitive understanding, rather than derivations from inverse problems and SDS loss, as done for DDIM.

4. Essentially, **CFG++ can be written as reweighted CFG whose $\omega$ varies along the sampling process** (let $s\coloneqq t-1$ and $\epsilon\coloneqq \epsilon_\emptyset$ for easier LaTeX rendering in OpenReview):

- For DDIM CFG: $$\mathbf{x}_s=\frac{\sqrt{\bar{\alpha}_s}}{\sqrt{\bar{\alpha}_t}}\mathbf{x}_t-\frac{\sqrt{(1-\bar{\alpha}_t)\bar{\alpha}_s}-\sqrt{(1-\bar{\alpha}_s)\bar{\alpha}_t}}{\sqrt{\bar{\alpha}_t}}(\omega\epsilon_c-(\omega-1)\epsilon)$$

- For DDIM CFG++: $$\mathbf{x}_s=\frac{\sqrt{\bar{\alpha}_s}}{\sqrt{\bar{\alpha}_t}}\mathbf{x}_t-\frac{\sqrt{(1-\bar{\alpha}_t)\bar{\alpha}_s}}{\sqrt{\bar{\alpha}_t}}(\lambda\epsilon_c-(\lambda-1)\epsilon)+\sqrt{1-\bar{\alpha}_s}\epsilon$$
$$=\frac{\sqrt{\bar{\alpha}_s}}{\sqrt{\bar{\alpha}_t}}\mathbf{x}_t-\frac{\sqrt{(1-\bar{\alpha}_t)\bar{\alpha}_s}-\sqrt{(1-\bar{\alpha}_s)\bar{\alpha}_t}}{\sqrt{\bar{\alpha}_t}}(\frac{\lambda\sqrt{(1-\bar{\alpha}_t)\bar{\alpha}_s}}{\sqrt{(1-\bar{\alpha}_t)\bar{\alpha}_s}-\sqrt{(1-\bar{\alpha}_s)\bar{\alpha}_t}}\epsilon_c-\frac{(\lambda-1)\sqrt{(1-\bar{\alpha}_t)\bar{\alpha}_s}+\sqrt{(1-\bar{\alpha}_s)\bar{\alpha}_t}}{\sqrt{(1-\bar{\alpha}_t)\bar{\alpha}_s}-\sqrt{(1-\bar{\alpha}_s)\bar{\alpha}_t}}\epsilon)$$

So, $$\omega=\frac{\lambda\sqrt{(1-\bar{\alpha}_t)\bar{\alpha}_s}}{\sqrt{(1-\bar{\alpha}_t)\bar{\alpha}_s}-\sqrt{(1-\bar{\alpha}_s)\bar{\alpha}_t}}.$$

As discussed in Sec. 5, previous studies also propose adjusting the guidance scale across timesteps. However, it may be incorrect to claim that "these findings are orthogonal to ours and keep the sampling trajectory the same ... CFG++ is designing a different trajectory".

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper presents CFG++, an innovative approach designed to enhance the performance of diffusion models by addressing limitations associated with traditional Classifier-Free Guidance (CFG). The authors argue that several drawbacks of CFG, such as the lack of invertibility in DDIM (Denoising Diffusion Implicit Models) and the issues of mode collapse when high guidance scales are used, arise from the off-manifold phenomena related to CFG rather than the inherent characteristics of diffusion models themselves.

### Strengths
The paper exhibits a high degree of originality by introducing the CFG++ framework, which fundamentally reinterprets the limitations of traditional Classifier-Free Guidance (CFG). Instead of merely enhancing existing methodologies, the authors propose that many issues attributed to diffusion models arise from off-manifold behavior. This shift in perspective not only challenges established assumptions but also provides a fresh lens through which to analyze and improve guidance mechanisms in generative models. By integrating recent advancements in inverse problem-solving within diffusion contexts, the authors demonstrate a creative synthesis of ideas that broadens the scope of CFG applications.


The quality of the research is evident in both its theoretical foundations and empirical validation. The authors articulate their arguments clearly, supported by robust mathematical formulations and well-structured experiments. The comparative analysis illustrates the advantages of CFG++ over prior methods, effectively showcasing the model’s performance improvements in terms of reduced artifacts and enhanced image quality. Additionally, the use of rigorous benchmarks for evaluation strengthens the credibility of the findings. The paper’s methodology is sound, making it a valuable contribution to the field.


The clarity of the writing is commendable, as the authors navigate complex concepts with precision. The introduction provides a succinct overview of the issues addressed and the motivations behind the proposed solution. Throughout the paper, technical jargon is well-defined, ensuring accessibility for readers with varying levels of expertise. Figures and diagrams are effectively utilized to illustrate key points, facilitating a better understanding of the model's mechanics and results. Overall, the paper is well-organized, which enhances its readability and facilitates comprehension.

### Weaknesses
One notable weakness is the limited scope of experiments presented. While the authors provide comparative results demonstrating the efficacy of CFG++, the evaluation primarily focuses on specific datasets or tasks. To enhance the robustness of their claims, the authors could include a broader range of benchmarks across diverse domains. For instance, incorporating tasks from different image generation contexts (e.g., artistic style transfer, super-resolution) would provide a more comprehensive assessment of CFG++’s performance and generalizability. The authors should extend their experimental framework to include varied datasets and tasks, thereby demonstrating the versatility and applicability of CFG++ in different settings.

Although the paper claims improvements over prior methods, it lacks a detailed comparison with a broader array of state-of-the-art techniques in diffusion models. For example, a comparison with models like **Stable Diffusion** or recent advancements in **Guided Diffusion** could contextualize the advantages of CFG++ more clearly.  The authors should include direct comparisons with a wider selection of contemporary approaches, utilizing standardized metrics (such as FID scores) to provide a clearer understanding of CFG++’s standing in the current landscape.

While the paper introduces the concept of manifold constraints and off-manifold behavior, the theoretical underpinnings could be further strengthened. The authors briefly mention these concepts but do not provide a rigorous mathematical framework that details how CFG++ operates under these constraints or why these adjustments yield better results. A more thorough theoretical analysis, including mathematical proofs or derivations that illustrate the benefits of operating within manifold constraints, would bolster the paper's credibility and understanding.

The paper does not address how CFG++ scales with increasing model size or complexity. As generative models continue to grow, understanding how CFG++ performs under these conditions is crucial. There is a lack of discussion regarding potential computational overhead or challenges in real-world applications. Including analyses or experiments that assess the scalability of CFG++ with larger models or datasets, along with a discussion on computational efficiency, would provide valuable insights for practitioners considering its application.

The paper primarily focuses on quantitative metrics, such as image quality, but does not incorporate user-centric evaluations. Assessments based on human judgment, such as user studies to evaluate the perceived quality or usefulness of generated images, could provide a more holistic view of CFG++’s effectiveness.  The authors should consider conducting qualitative studies where human evaluators assess the output of CFG++ compared to other methods. This could provide insights into the model's real-world applicability and user satisfaction.

### Questions
**Question**: Could you elaborate on the specific mechanisms through which off-manifold behavior impacts the performance of traditional Classifier-Free Guidance (CFG)?  A detailed explanation of how off-manifold behavior is identified and measured within the context of your experiments would enhance understanding. Including visualizations or theoretical examples could further clarify this concept.

**Question**: What are the reasons behind selecting the specific datasets used in your experiments? Are there plans to test CFG++ on a wider array of datasets or tasks?  Expanding the experimental framework to include diverse datasets and applications would strengthen the validity of your findings. Consider including datasets from different domains (e.g., text-to-image generation, video synthesis) to demonstrate the versatility of CFG++.

**Question**: Why were certain state-of-the-art methods, such as Stable Diffusion and other recent advances in guided diffusion, excluded from your comparative analysis?  Including a more comprehensive set of comparisons with these methods would provide a clearer context for evaluating the performance of CFG++. Detailed performance metrics and qualitative results could enrich the discussion.

**Question**: Can you provide more in-depth mathematical justifications or derivations that support the effectiveness of CFG++ in addressing the limitations of traditional CFG?  A rigorous theoretical framework would enhance the paper's credibility. Detailed mathematical formulations explaining how CFG++ operates under manifold constraints could help bridge the gap between theory and practice.

 **Question**: How does CFG++ perform in terms of computational efficiency and scalability with larger models or datasets?  Including a discussion on scalability, including any computational overhead observed during experiments, would be valuable. Experiments assessing performance on larger models could illustrate the practical applicability of CFG++ in real-world scenarios.

 **Question**: Have you considered conducting user studies to evaluate the perceived quality and usefulness of the outputs generated by CFG++?  Incorporating qualitative assessments from human evaluators could provide insights into the model's effectiveness from a user perspective. Such studies could help highlight the practical implications of using CFG++ in various applications.


**Question**: What future research directions do you foresee emerging from your findings regarding CFG++ and manifold constraints in diffusion models?  A discussion on potential extensions or related areas of research would help contextualize your contributions within the broader landscape of machine learning, inviting collaboration and further inquiry.

### Soundness
2

### Presentation
2

### Contribution
1
