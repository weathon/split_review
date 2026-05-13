# I-Max: Maximize the Resolution Potential of Pre-trained Rectified Flow Transformers with Projected Flow

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
Rectified Flow Transformers (RFTs) offer superior training and inference efficiency, making them likely the most viable direction for scaling up diffusion models. However, progress in generation resolution has been relatively slow due to data quality and training costs. Tuning-free resolution extrapolation presents an alternative, but current methods often reduce generative stability, limiting practical application. In this paper, we review existing resolution extrapolation methods and introduce the I-Max framework to maximize the resolution potential of Text-to-Image RFTs. I-Max features: (i) a novel Projected Flow strategy for stable extrapolation and (ii) an advanced inference toolkit for generalizing model knowledge to higher resolutions. Experiments with Lumina-Next-2K and Flux.1-dev demonstrate I-Max's ability to enhance stability in resolution extrapolation and show that it can bring image detail emergence and artifact correction, confirming the practical value of tuning-free resolution extrapolation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces the I-Max framework, designed to address resolution extrapolation in text-to-image models using Rectified Flow Transformers. This paper incorporates a Projected Flow for fidelity and an inference toolkit to enhance model generalization at extrapolated resolutions. Experiments on the Lumina-Next-2K and Flux.1-dev models demonstrate that I-Max effectively improves the stability and detail of extrapolated high-resolution images, showing its potential for practical applications where tuning-free resolution extrapolation is needed.

### Strengths
- The paper is well-structured, making the methodology and findings easy to understand.
- The paper provides thorough experimental evaluations, including ablation studies on key components of the I-Max framework.

### Weaknesses
 - The evaluation relies heavily on a single metric (GPT-4 preference) to assess the quality of generated images, limiting the objectivity of the results. This reliance may affect the demonstration of the proposed method’s effectiveness.
If evaluating high-resolution images with widely used metrics (e.g., FID) is challenging, as noted in the manuscript, a toy experiment using a pretrained model on a lower-resolution dataset, such as CIFAR or ImageNet, could offer a feasible benchmark and enable standardized metric comparisons. Specifically, the lack of established metrics for high-resolution image quality makes it difficult to validate the improvements claimed by the authors. The subjective nature of preference-based evaluation introduces potential bias, and it is unclear how well these preferences correlate with actual image fidelity and text alignment. A more robust evaluation would incorporate metrics that are less susceptible to subjective interpretation, such as FID scores calculated on image crops, which can capture local image quality, and CLIP scores to assess text-image consistency.
- In line 254, the paper mentions the use of a low-pass filter for projection but does not specify the type. Additionally, exploring the impact of different low-pass filters could offer insights into how they affect stability and quality during resolution extrapolation. The choice of low-pass filter can significantly impact the frequency content of the projected image, which in turn affects the stability and detail of the extrapolated high-resolution image. Without specifying the filter type (e.g., Gaussian, Butterworth, or a specific wavelet), it is difficult to assess the generality of the results. Furthermore, an analysis of how different filter parameters (e.g., cutoff frequency) affect the final image quality would be beneficial.

### Questions
Please refer to the Weaknesses section.

### Soundness
2

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
The paper addresses the task of tuning-free resolution extrapolation for text-to-image Rectified Flow Transformers (RFTs) from which one can obtain samples at a much higher resolution than the resolution at which the model was originally trained. While directly training high-resolution generative models is practically difficult, this paper aims to adapt trained RFTs to generate images of high resolutions (such as 4096X4096) without the need for fine tuning.

The proposed scheme named I-Max involves low-resolution guidance named projected flow. Here, the low-resolution
space is treated as a low-dimensional projection of the high-resolution space, and thereby the low-resolution
flow can be regarded as the projection of the ideal high-resolution flow. Considering the linear
interpolation characteristic of rectified flow, I-Max incorporates guidance in the projected space at each timestep.
Additionally I-max incorporates inference techniques tailored for RFT to enhance the model’s ability to generalize to extrapolated resolution.

### Strengths
Attempting to extrapolate resolution of trained models is interesting and practically useful given the issues of data quality and fine tuning costs. This paper addresses the task of resolution extrapolation for trained Rectified Flow Transformers for the first time.

Relevant prior works have been discussed appropriately.

### Weaknesses
The guidance mechanism in eq 7 does not exactly correspond to the Classifier Free Guidance. It is indeed some sort of a guidance function. Could the authors explain the relationship between their guidance mechanism and Classifier Free Guidance?

Additionally, it is not clear how the first term in the RHS of eqns 6 and 7 (v_{theta} at the extra resolution) is obtained. Is the same model trained at the native resolution used for this?

The steps followed to generate the high resolution image could have been summarized in the form of an algorithm.

Evaluation is based only on GPT-4o. More qualitative examples wherein one can see improvements as shown in Fig 2 could have been shown in the supplementary material. Since GPT-4o is not necessarily trained for image quality assessment, other measures should have been used for comparison. Time aware scaled ROPE (Fig 7) also has good performance according to this measure.

Typo 'for butter efficiency' line 419.

Some of the ideas incorporated are based on existing works. Specifically, the inference techniques in section 2.3 are based on prior works. 
Could the authors clarify their novel contributions in the techniques used in section 2.3?

### Questions
Why is the proposed method not shown on only Lumina-Next instead of the self-trained Lumina-Next-2K? Does the method require native resolution also to be high? Can the proposed I-Max work for low native resolutions?

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
This paper presents a method to extrapolate the resolution of the generated images at inference time. The authors focus on rectified flow transformers. The key ideas are a projected flow strategy that is designed to ensure more stability at inference, and a number of implementation techniques to enhance the quality of the extrapolation, such as NTK-aware scaled RoPE, SNR resolution adjustment, attention re-scaling, and text duplication.

### Strengths
I-Max integrates a number of simple but important components to make a rectified flow model generalise to higher resolutions at inference. In particular, the projected flow strategy makes sense as a method to ensure more stability. As far as I know this is original and the specific implementation in the style of a classifier-free guidance seems original too. 
The results achieved in the experimental section show also that the proposed projection with the other inference techniques are quite effective in the resolution extrapolation task.

### Weaknesses
The presentation is at times not optimal.
For example, the split in the introduction into How to guide and How to infer does not seem very clear to me. At lines 93-95 the explanations do not seem to match the names of the two perspectives.
Overall, the use of the English language could be better. I would suggest to have the paper revised but a native English speaker to correct typos.
Could you check the following?
Line 220: Eq. 2 illustrates the equivariance of the flow wrt the projection rather than its invariance.

The other concern is regarding the method (see also the Questions below). It would be useful to the reader to better explain the technical choices by providing the motivation/rationale behind each of them.

### Questions
I would like the authors to clarify the following points:
1) Provide visual examples of failures at very high resolution (as pointed out in sec 3.3 for Figure 6);
2) Why is the projected flow implemented via the classifier-free guidance? Is this the only way?
3) Could you show how you would explain the transition to eq. (5) with more technical details?

### Soundness
3

### Presentation
2

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
This paper proposes the I-Max, designed to maximize the resolution potential of Text-to-Image Rectified Flow Transformers (RFTs). I-Max includes a novel Projected Flow strategy and an advanced inference toolkit, enhancing generative stability, improving image detail, and correcting artifacts during resolution extrapolation.

### Strengths
- The paper is well-structured.
- The proposed method achieves excellent visual results.

### Weaknesses
1.  **Lack of Quantitative Comparisons:**
   The paper lacks any quantitative comparisons, making it difficult to demonstrate the superiority of the proposed method. Metrics such as FID (Fréchet Inception Distance) and IS (Inception Score) could be used to provide concrete quantitative comparisons. It is crucial to compare the performance of I-Max against existing state-of-the-art methods for high-resolution image generation, not just show results at different resolutions. The absence of such comparisons makes it impossible to assess the true contribution of the proposed method relative to the current landscape.

2.  **Need for User Study:**
   A user study is necessary to validate the visual effectiveness of the method. This study should focus on aspects such as detail preservation, artifact reduction, and overall image quality of the generated images, which would further enhance the quality of the paper. While GPT-4o can provide some insights, it is not a substitute for human evaluation, which is essential for assessing the subjective quality of generated images.

3.  **Comparison of Model Parameters and Runtime:**
   The paper should include comparisons of model parameters and runtime to provide a comprehensive picture of the method’s efficiency. Reporting the generation time at different resolutions, such as 1K and 2K, is crucial for understanding the practical applicability and efficiency of the proposed framework. It is also important to compare the computational cost of I-Max with other high-resolution generation techniques, including both training-free and tuning-based approaches, to determine its relative efficiency.

### Questions
As shown in Weaknesses

### Soundness
2

### Presentation
2

### Contribution
3
