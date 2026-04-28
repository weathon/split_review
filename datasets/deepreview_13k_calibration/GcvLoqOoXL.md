# Rethinking Diffusion Posterior Sampling: From Conditional Score Estimator to Maximizing a Posterior

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
Recent advancements in diffusion models have been leveraged to address inverse problems without additional training, and Diffusion Posterior Sampling (DPS) (Chung et al., 2022a) is among the most popular approaches. Previous analyses suggest that DPS accomplishes posterior sampling by approximating the conditional score. While in this paper, we demonstrate that the conditional score approximation employed by DPS is not as effective as previously assumed, but rather aligns more closely with the principle of maximizing a posterior (MAP). This assertion is substantiated through an examination of DPS on 512$\times$512 ImageNet images, revealing that: 1) DPS’s conditional score estimation significantly diverges from the score of a well-trained conditional diffusion model and is even inferior to the unconditional score; 2) The mean of DPS’s conditional score estimation deviates significantly from zero, rendering it an invalid score estimation; 3) DPS generates high-quality samples with significantly lower diversity. In light of the above findings, we posit that DPS more closely resembles MAP than a conditional score estimator, and accordingly propose the following enhancements to DPS: 1) we explicitly maximize the posterior through multi-step gradient ascent and projection; 2) we utilize a light-weighted conditional score estimator trained with only 100 images and 8 GPU hours. Extensive experimental results indicate that these proposed improvements significantly enhance DPS’s performance. The source code for these improvements is provided in the supplementary material.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper points out the ineffectiveness of Diffusion Posterior Sampling(DPS), revealing that DPS aligns more closely with maximum a posteriori(MAP) estimation rather than conditional score estimation. This paper demonstrates that DPS’s score estimation diverges from an accurate conditional model and produces low-diversity samples. The authors enhance DPS by explicitly maximizing the posterior with gradient ascent and incorporating a lightweight conditional score estimator.

### Strengths
- This paper is well organized. I enjoy reading this paper. 
- This work suggests MAP hypothesis that can explain the recent mysterious observations regarding DPS. I think this is clear and novel contribution.
- Significant performance gain by being more faithful to MAP estimate well supports their hypothesis.
-

### Weaknesses
 - Although I think insights from this paper is beneficial, this paper heavily relies on the empirical observations to develop and support their claims. It is okay, but theoretical insights will be strengthen their claim and more naturally lead to their MAP hypothesis.
- This work is limited to show that MAP hypothesis can explain the weird part of DPS rather than clarifying the reason why it works in MAP estimate.

### Questions
When distribution is multi-modal, is it possible to say that working as MAP estimate is the main reason for low-diversity generation?

### Soundness
3

### Presentation
3

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
This paper challenges the prevailing view that Diffusion Posterior Sampling (DPS) works by approximating conditional score, hypothesizing that DPS is closer to maximizing a posterior (MAP) and proposes two improvements for DPS based on the new hypothesis.

### Strengths
* The paper presents compelling evidence through empirical analysis on 512x512 ImageNet images that DPS does not effectively approximate conditional score, contradicting prior understanding.
* The proposed improvements, explicit MAP implementation (DMAP) and a light-weighted conditional score estimator, are shown to significantly enhance the performance of DPS.
* The paper is well-organized and provides clear explanations of the technical details, including the mathematical formulations and algorithms.

### Weaknesses
 * The paper mainly focuses on image restoration tasks and the generalizability of the MAP hypothesis to other inverse problems is not explored. Specifically, the paper lacks analysis on how the proposed methods perform on tasks with different noise models or measurement operators, such as those encountered in medical imaging (e.g., CT or MRI reconstruction) or other computer vision tasks like depth estimation. The performance of DPS and its variants may vary significantly depending on the specific characteristics of the inverse problem, and the paper should include experiments that cover a wider range of scenarios to validate the MAP hypothesis more thoroughly.
* While the light-weighted conditional score estimator is efficient, its performance still lags behind well-trained conditional diffusion models like StableSR. The paper does not provide a detailed analysis of the trade-offs between computational efficiency and performance. It would be beneficial to explore the limitations of the light-weighted estimator, such as its sensitivity to the number of training samples or the complexity of the conditional distribution. Furthermore, the paper should investigate whether the performance gap can be reduced by incorporating more sophisticated training techniques or network architectures for the conditional score estimator.
* The authors claim that the MAP hypothesis can explain why Adam helps DPS, but this claim is not sufficiently substantiated. The argument relies on the idea that Adam's adaptive learning rates do not harm MAP estimation, but it does not provide a rigorous analysis of how Adam's specific update rules interact with the objective function of DPS. A more detailed investigation is needed, potentially including an analysis of the convergence properties of Adam in the context of DPS or a comparison with other optimization algorithms.

### Questions
* To further investigate the hypothesis that DPS is closer to MAP than conditional score estimation, one suggestion is to experiment with toy distributions where the ground truth posterior is known. This approach would allow for a direct numerical comparison between the results of DPS and the true posterior.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors challenge the traditional view that DPS functions as a conditional score estimator, arguing instead that it aligns more closely with MAP. Through empirical analysis, they find that DPS exhibits significant score estimation errors, a high score mean, and low sample diversity, supporting this reinterpretation. To improve DPS, they propose explicitly maximizing the posterior using gradient ascent and introduce a lightweight conditional score estimator. These methods demonstrate improved results in terms of image quality, particularly for deblurring tasks.

### Strengths
1. The paper has the potential for significant impact as this is a popular field at the moment.
2. It introduces new ideas and reinterprets existing arguments, supported by data that validates this new perspective.
3. Building on their reinterpretation, the authors develop a new method that outperforms traditional DPS.

### Weaknesses
1. The paper has several grammatical flaws:
   - Captions for tables should be placed on top, as I believe this is required formatting by ICLR.
   - Add an arrow to indicate that lower FID is better, and do the same for other metrics.
   - There are many undefined acronyms, such as FID, KID, and LPIPS.
   - The captions for figures and tables could be improved for clarity, adding the takeaway from each table and image as in the text would benefit the reader.
   - In line 196, the notation for different math symbols is redundant with what is already explained on line 153.
   - The claim "With Observation I & II, one can conclude that DPS is far away from a reasonable conditional score estimator in practical scenarios" is quite extreme, especially since it is shown on just one problem.
   - In line 255, "we hypothesis" should be corrected to "we hypothesize."
   - In line 273, "(See Appendix C.1)" should not be placed after a sentence.
   - The first quotation marks throughout the paper are incorrect; in LaTeX, use `` for the opening quotation mark.
   - Citations like "Chung et al. (2022a); Song et al. (2023c)" are not grammatically correct and appear throughout the paper. Correct the citation style to improve readability.

2. There are no results for inpainting, unlike the original DPS paper.

### Questions
Is DPS not used for in painting as well? You seem to only provide results for deblurring.

### Soundness
3

### Presentation
2

### Contribution
3
