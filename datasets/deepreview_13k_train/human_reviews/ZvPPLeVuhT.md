# ReGRAF: Training free Prompt Refinement via Gradient Flow for Segmentation

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
Visual Foundation Models (VFMs) such as the Segment Anything Model (SAM) have significantly advanced segmentation, object detection, and image classification tasks. 
However, SAM and its fine-tuned variants necessitate substantial manual effort for prompt generation and additional training for specific applications. 
Recent methods have addressed these limitations by integrating SAM into one-shot and few-shot segmentation, enabling auto-prompting through semantic alignment between query and support images. 
Despite these advancements, they still generate inadequate prompts that degrade segmentation quality. 
To tackle this limitation, we introduce ReGRAF (Refinement via GRAdient Flow), a training-free method that refines prompts through gradient flow derived from SAM's mask decoder. ReGRAF seamlessly integrates into SAM-based auto-prompting frameworks and is theoretically proven to refine segmentation masks with high efficiency and precision. Extensive evaluations demonstrate that ReGRAF consistently improves segmentation quality across various benchmarks, effectively mitigating false positives without requiring additional training or architectural modifications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes  ReGRAF (Refinement via Gradient Flow), which is a training free module that can be added to auto-prompting methods (such as PerSAM or Matcher) for promotable segmentation models (such as SAM). ReGRAF relies on using gradient flow, logits from mask decoder and query embeddings to update embeddings of the query, to best match that of support image. ReGRAF is an iterative method that iteratively updates embeddings with no need to learnable parameters. 

Authors tested the proposed method on 2 tasks of semantic segmentation and part segmentation on total of 5 different datasets and a combination of 7 baselines stemmed from variations on 2 major baseline methods (PerSAM or Matcher)

### Strengths
- Although iterative, the method's running time is marginal compares to baselines (Table 3)
- That paper is easy to follow and formulations clearly explain the proposed method.

### Weaknesses
 - Although the proposed method provides consistent improvement on top of baselines, the improvements are mostly very marginal (less than 0.5% in majority of times and less than 1% in almost every experiment except for 2 on a specific dataset (Tables 1 and 2).
- The visual results in the paper mostly focused on cases where the proposed method improved baselines and there is a lack of showing failure cases. This causes a lack of clarity on weaknesses of the method and a fair understanding of performance.
- The proposed method seem to rely on a number of hyper parameters (Iterations T, entropy regularization factor, and step size). The paper does not provide any experiments to show sensitivity of the method to these parameters and their impact on performance.
- The paper mentions that the gradient estimation becomes inaccurate with a large number of iterations due to an approximation in the density ratio calculation. However, the explanation of how and why this approximation leads to inaccuracy is not sufficiently detailed, making it hard to assess the practical implications of this limitation.

### Questions
- Given the marginal improvements this begs the question of how much time should one spend tuning these parameters for new cases and how sensitive the method will be to them?
- Authors mentioned "s equation (6) implies that the gradient estimation in equation (12) becomes inaccurate with a large number of iterations." (on page 7 section Hyperparameter setting of ReGRAF). This was not clear to me. How in accurate and why?
- Table 1 shows a wide range of performance improvements depending on the baseline and dataset. Would be great is authors can share some insight for when their method could have more significant improvements vs marginal. Was there any trends in the results?
- What are some cases that the method will fail and provide worse results than baseline?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Though SAM has achieved impressive generalization ability. It is not directly tailored to be specific to different tasks. Recently, one-shot and few-shot methods such as PerSAM and Matcher have been proposed to generate the auto prompting via query and supporting set. However, the auto-prompt generation process is far from perfect, missing prompts or error prompts can appear. As a result, the resulting mask is not aligned with the support set well. This paper proposed to leveraging additional cues to iteratively sample prompts for improving one/few-shot segmentation performance. As the ground truth masks are not available for correcting the prompts, the author proposed to leverage gradient flow from the decoder to improve the prompt sampling, and therefore, the final segmentation results.

### Strengths
Leveraging the guidance from the decoder to guide the prompt sampling for interactive segmentation is novel from my perspective. It alleviates the need for external human supervision and makes use of the interactive correction ability of the interactive segmentation foundation model. Specifically, the author computes the gradient flow from the decoder to align the distribution of the query and support embeddings. Afterward, the updated query embedding is used to compute the similarity map for a new round of interactive segmentation. 

The proposed method has been validated on both the part segmentation dataset and semantic segmentation, which demonstrates its broad applicability. 

A theoretical analysis has been provided to show the proposed method's convergence and convergence rate. 

The presentation of the paper is well-structured and the equations are clearly displayed.

### Weaknesses
The performance improvement is somehow marginal for both the semantic segmentation and part segmentation, across dataset and base method. From the qualitative examples, it seems that the refinement process is quite effective in aligning different semantic hieratical levels of the target and support mask. For example, in figure 5, some object-level base predictions are correctly adjusted to part masks with the proposed methods. In figure 4, some missing components are correctly saved back. Does the proposed method aim to resolve the semantic hieratical ambiguity or mainly the details correction? If it is the first part, then it is unclear to me how is this achieved. As it is not well explained in the method part or the motivation part. 

Besides, the examples displayed achieve significant improvement. However, quantitative evaluation shows the opposite. Are there some examples becoming worse after refinement? It would be nice to show some scatter plots of the sample-wise IoU before and after refinement so that we have a better idea of the advantages and the limitations of the proposed method. 

I miss the ablation on the number of refinement times.

### Questions
See the weakness. I am willing to raise the score if the author can solve my concerns

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
4

### Summary
This paper delves into the domain of prompt segmentation, which is pertinent to the foundational model, SAM. The authors propose a training-free method to refine segmentation results by updating the visual embeddings of query images. They provide a rigorous theoretical analysis to elucidate why the gradient flow through the mask decoder can optimize segmentation results and demonstrate the convergence of their approach. They assert that this design can be readily integrated with other baseline methods for prompt segmentation, which is exemplified in the experimental section.

### Strengths
1.This paper provides a substantial theoretical justification for the method, which possesses favorable interpretability.
2.The method can be integrated flexibly with multiple baseline segmentation prompts without the need for training, while incurring minimal additional inference costs.
3.The paper includes a wealth of visualized results.

### Weaknesses
The analysis of the experimental results in the article is insufficient, and the improvement achieved is limited. Firstly, the paper only compares their method with  PerSAM-F， Matcher and their HQ_SAM variants, without benchmarking against other methods in the field. The analysis in the related work section is similarly inadequate. Secondly, apart from the comparisons with baseline methods in Tables 1 and 2, there is a lack of analytical experiments and an examination of hyper-parameters. Thirdly, the improvements shown in Tables 1 and 2 are overall modest, with many of the increments less than 0.5%. Given that segmentation task results typically exhibit significant variability, these results provide insufficient evidence of the method's efficacy.

### Questions
1、Why does the performance of ReGRAF, when integrated with HQ-Matcher on the COCO-20i dataset, fall short of the results achieved with the standard Matcher?
2. Please explain line 359, "gradient estimation in equation (12) becomes inaccurate with a large number of iterations." Why does an increase in the number of iterations lead to inaccuracies in the results? Theoretically, shouldn't the process gradually converge to a value near the optimal one?
3.In section 4.2.2, the author states that the numerical improvement is not significant, explaining that the segmentation effect is better, but these individual examples are not very persuasive. Perhaps some better evaluation criteria could more comprehensively demonstrate the enhancement brought by the method.

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
3

### Summary
Despite the integration of SAM into one-shot and few-shot segmentation, which enables auto-prompting through semantic alignment between query and support images, there are limitations in the generated prompts that can degrade the quality of segmentation. This is primarily due to visual inconsistencies between the support and query images.
To address this issue, the authors propose a training-free method called ReGRAF (Refinement via Gradient Flow). ReGRAF refines the prompts by utilizing gradient flow derived from SAM's mask decoder. This approach aims to improve the quality of prompts without the need for additional training.

### Strengths
The proposed method serves as a simple and effective training-free refinement technique, offering broad applicability to Auto-Prompting Segmentation Frameworks. Additionally, the authors provide a theoretical guarantee of convergence, further strengthening the credibility and reliability of their approach.

### Weaknesses
1.	In table 1 and 2, the incremental improvement resulting from the addition of ReGRAF is not readily apparent. This raises concerns about whether the implementation of ReGRAF will yield a satisfactory increase in performance, considering the trade-off in terms of time and cost.
2.	When considering the accuracy of SAM segmentation, it is often observed that the mask fails to accurately calibrate complex edges. This issue becomes particularly challenging when dealing with cases involving complex edges or thin objects. What happen for this hards cases with complex edges or thin objects by your ReGRAF. It is happy to add more high-accurate segmentation wokrs:
[1]. Transparent Image Layer Diffusion using Latent Transparency
[2]. DiffuMatting: Synthesizing Arbitrary Objects with Matting-level Annotation
[3]. Highly Accurate Dichotomous Image Segmentation

### Questions
see in weakness

### Soundness
3

### Presentation
3

### Contribution
3
