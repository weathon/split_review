# Easing Training Process of Rectified Flow Models Via Lengthening Inter-Path Distance

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 8, 6

## Abstract
Recent research pinpoints that different diffusion methods and architectures 
trained on the same dataset produce similar results for the same input noise. 
This property suggests that they have some preferable noises for a given sample. 
By visualizing the noise-sample pairs of rectified flow models and stable diffusion models in two-dimensional spaces, 
we observe that the preferable paths, connecting preferable noises to the corresponding samples, 
are much well organized with significant fewer crossings comparing with 
the random paths, connecting random noises to training samples. 
In high-dimensional space, paths rarely intersect. 
The path crossings in two-dimensional spaces indicate the shorter inter-path distance 
in the corresponding high-dimensional spaces. 
Inspired by this observation, we propose the Distance-Aware Noise-Sample Matching (DANSM) method 
to lengthen the inter-path distance for speeding up the model training. 
DANSM is derived from rectified flow models, which allow using a closed-form formula to calculate the inter-path distance. 
To further simplify the optimization, we derive the relationship between inter-path distance and path length, 
and use the latter in the optimization surrogate. 
DANSM is evaluated on both image and latent spaces by rectified flow models and diffusion models. 
The experimental results show that DANSM can significantly improve the training speed by 30\% $\sim$ 40\%
without sacrificing the generation quality.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This work proposes Distance-AwareNoise-Sample Matching (DANSM) to increase training speed in generative models without any loss (in fact gain) in performance. The proposed method is inspired by "the difference between random paths used in training and preferable paths from well-trained models".
The work is theoretically motivated and sound.
The work offers limited evaluations, however, they seem to be sufficient to make the case.

### Strengths
The work is well written except for a few typos (for example, in line 198/199 "To **analysis**" is written instead of "To **analyse**", and in line 309/310 "have not been **evaluation** on RFM" is written instead of **evaluated**).

The idea is sound and is theoretically motivated, the results are in line with the hypothesis.
The implementation seems simple and straightforward. 

The claims made in the paper seem to be backed by empirical evaluations.

### Weaknesses
I have 2 major points in this regard:
1. The plots are not well made, some of the lines in the plots, for example, Figure 6(b), Figure 7(b), and Figure (b) seem to be starting from arbitrary locations. It would help to invest more time and make better-looking plots without these artifacts, or if they are not artifacts then an explanation for the same would be very helpful.

2. The work lacks comparisons to "Immiscible Diffusion", while the paper does point out the key differences in lines 307-315, it would be interesting to see empirical evaluations in comparison to "Immiscible Diffusion" since the methods are closely related.

### Questions
Q1- I would appreciate a better explanation for Figure 6 (b), the plot looks a bit unclear to me. Additionally, there are lines behind the legend curbing my ability to understand the plot completely. My essential question is that unlike Figure 7, in Figure 6 (b) I do not see any gains in training times when using the proposed method. Is this understanding of mine correct?

### Soundness
4

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
2

### Summary
This paper explores how different diffusion methods yield similar results with the same dataset, identifying "preferable noises" for samples. It introduces the Distance-Aware Noise-Sample Matching (DANSM) method to optimize training by increasing inter-path distances. DANSM significantly speeds up training by 30%–40% without losing quality, offering insights into enhancing diffusion model efficiency.

### Strengths
1. The diagram is very clear, making it easy to understand how different diffusion methods yield similar results with the same dataset, identifying "preferable noises" for samples.

2. The proposed method significantly speeds up training by 30%–40% without losing quality, offering new insights into enhancing diffusion model efficiency.

### Weaknesses
1. The FID calculations are measured with very few sampling steps, making it difficult to ensure the quality of the generated results. It would be beneficial to provide a comparison of different methods while maintaining image quality, ideally with visualizations, such as images decoded using stable diffusion. Specifically, the use of only a small number of sampling steps may not accurately reflect the true performance of the models, as diffusion models often require a larger number of steps to converge to high-quality samples. A more thorough evaluation would involve assessing FID scores across a range of sampling steps, including those closer to convergence, to provide a more complete picture of the method's capabilities.

2. The experiments were only validated on CIFAR and LSUN-BEDROOM datasets. Validation on a broader range of datasets, such as ImageNet and FFHQ, would provide more comprehensive insights. Additionally, including some actual generated images for visual comparison would be advantageous. The limited dataset scope restricts the generalizability of the findings. Expanding the evaluation to include datasets with varying complexities and characteristics, such as ImageNet with its diverse object categories and FFHQ with its high-resolution facial images, is crucial to demonstrate the robustness of the proposed method. Furthermore, visual comparisons are essential to complement the quantitative metrics, offering a qualitative assessment of the generated samples.

### Questions
1. Include a comparison using longer sampling steps.

2. Conduct more extensive experiments on complex datasets.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper reveals that different diffusion models trained on the same dataset tend to produce similar outputs when given the same input noise. This suggests the existence of "preferable noise-sample pairs" in the training process. The authors propose the Distance-Aware Noise-Sample Matching method to lengthen the inter-path distance for speeding up the training of diffusion-based models. The experiments show that the proposed method improves the training speed by about 30%~40%.

### Strengths
The paper presents a framework that simplifies the optimization of inter-path distances to path length optimization, based on the observations of noise-sample pair relationships in diffusion models.

The approach leverages closed-form formulas derived from rectified flow models to enable efficient optimization without requiring architectural modifications, making it easy to integrate with existing methods.

### Weaknesses
The authors heavily emphasize "consistent model reproducibility," which seems interesting but abruptly transitions to proposing a method for improving training speed. This makes the main idea of the paper quite unclear.

The presentation of the proposed method is vague, and Algorithm 1 cannot be effectively reproduced with the provided steps. I suggest adding mathematical formulations in Sections 3.3 and 4.2 to rigorously explain how the proposed model is optimized. Specifically, the connection between the proposed distance-aware noise-sample matching and the actual optimization process is not clearly established. The paper lacks a detailed explanation of how the permutation \(\sigma\) is optimized in practice, and how this optimization relates to the overall training objective. Furthermore, the algorithm's complexity and computational cost are not discussed, which is crucial for assessing its practical applicability.

Regarding experiments, the paper lacks visual comparison results, which are crucial for method evaluation, especially when the FID quantitative metrics show minimal differences at the tiny scale discussed. I also recommend comparing with more methods and incorporating the proposed training speed improvement approach across more SD models. I believe the paper should present higher-resolution and larger-scale generation results. Given the computational benefits brought by this work's methodology, these tasks should be more computationally feasible. The current experiments are limited to relatively small datasets and low-resolution images, which makes it difficult to assess the method's effectiveness on more complex and realistic scenarios. The absence of ablation studies to analyze the impact of different components of the proposed method further limits the understanding of its behavior.

### Questions
Why is it necessary to learn latent-noise pairs that are well-aligned in the t-SNE space? This might suggest that straight flow matching is preferable, but the underlying reasoning is not clearly explained in the paper. Furthermore, I am confused about whether "consistent model reproducibility" is beneficial or detrimental for diffusion-based models. The fact that different model architectures can generate similar images from the same noise might indicate limited generation patterns due to the isotropic nature of the Gaussian noise.

### Soundness
3

### Presentation
3

### Contribution
2
