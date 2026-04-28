# Pyramidal Flow Matching for Efficient Video Generative Modeling

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 5, 8

## Abstract
\vspace{-5pt}
Video generation requires modeling a vast spatiotemporal space, which demands significant computational resources and data usage. To reduce the complexity, the prevailing approaches employ a cascaded architecture to avoid direct training with full resolution. Despite reducing computational demands, the separate optimization of each sub-stage hinders knowledge sharing and sacrifices flexibility. This work introduces a unified pyramidal flow matching algorithm. It reinterprets the original denoising trajectory as a series of pyramid stages, where only the final stage operates at the full resolution, thereby enabling more efficient video generative modeling. Through our sophisticated design, the flows of different pyramid stages can be interlinked to maintain continuity. Moreover, we craft autoregressive video generation with a temporal pyramid to compress the full-resolution history. The entire framework can be optimized in an end-to-end manner and with a single unified Diffusion Transformer (DiT). Extensive experiments demonstrate that our method supports generating high-quality 5-second (up to 10-second) videos at 768p resolution and 24 FPS within 20.7k A100 GPU training hours.
All code and models will be open-sourced at~\web.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a novel pyramidal flow matching scheme for video generation, which significantly improves training efficiency while preserving generation quality. The authors also propose a unified flow-matching objective that enables joint training of the pyramid stages within a single DiT model, eliminating the need for separate optimization across multiple models seen in prior approaches. Comprehensive experimental analyses are conducted on the VBench and EvalCrafter benchmarks, with proofs and additional qualitative results included in the supplementary materials.

### Strengths
+ The proposed pyramidal flow matching scheme is novel in video generation modeling and greatly enhances training efficiency.
+ The unified training objective is intuitive and effective.
+ The quantitative and qualitative analyses in the paper are comprehensive.
+ The quality of the generated videos is excellent.

### Weaknesses
 * The writing in the paper could benefit from further improvement for clarity and readability.
    - The repeated use of the term "full-resolution" up to the experiment section suggests that generation is being done in pixel space rather than latent space. It would be helpful to clarify this in the paper, as it may be misleading.

    - The paper contains several grammatical errors and repeatedly uses unnecessary terms, such as "sophisticated," which affect readability. I encourage the authors to revise the manuscript to improve clarity and flow.

* Some of the derivations and assumptions in the paper are ambiguous and potentially flawed

    - In Equations 7 and 8, the notation should reflect the conditional distributions $\hat{x}{e_k}|x_1$ and $\hat{x}{s_k}|x_1$. While both endpoints are Gaussian-distributed conditionally, the endpoint distributions $\hat{x}{e_k} = \int p(\hat{x}{e_k}|x_1)p(x_1)dx_1$ are not Gaussian.

    - In line 213, while the objective $\hat{x}{e_k} - \hat{x}{s_k}$ is correct, since we consider flow matching with $K$ windows, the vector field should instead be conditioned on the endpoints, $u_t(x_t|\hat{x}{e_k})$. However, this is challenging because the distribution $p(x_t|\hat{x}{e_k})$ may not be Gaussian. This objective could be derived more straightforwardly from a rectified flow perspective [1], where velocities are matched with $\dot{X}_t$ (see section 2.3 in [1]).

    - For training, are $x_1$ and $n$ at the start and end the same? Since flow matching accommodates data points from arbitrary couplings, this should not impact training validity but would benefit from additional explanation for clarity.

    - Regarding the renoising procedure in Section 3.2.2, Equation 12 should ideally denote $Up(\hat{x}{e_{k+1}}|x_1)$ rather than $Up(\hat{x}{e_{k+1}})$, as the latter may be non-Gaussian. Consequently, the subsequent proof may be invalid if it relies on $Up(\hat{x}{e_{k+1}})$ being Gaussian.

         [1] Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow

* Some important details and experiments are missing from the paper.

    - In Sec 3.2.1, the authors claim to enforce the noise to be in the same direction to enhance the straightness of the flow trajectory (Lines 207-209). However, there is no ablation experiment to show the benefit of this design choice.

    - The proof in Section 3.2.2 and Appendix A primarily relies on Equation 8. However, the authors implement the scheme in Equation 10, with no discussion on how the derivations in Section 3.2.2 and Appendix A could be generalized for Equation 10.
    - What is the number of sampling steps in Algorithm 1?

    - (Minor) Have the authors considered using temporally compressed pyramidal flow as well?


* No experimental results are provided for the video autoencoding task
   - In Section 4.1, the authors claim to train a video VAE for spatial and temporal compression of videos; however, there are no experimental results provided to evaluate the performance of the video VAE.
    - Why train a new video VAE instead of utilizing existing open-source video VAEs, such as Open-Sora or Open-Sora-Plan? Wouldn't this approach have been more effective in ensuring a fair experimental comparison?

* The results on VBench and EvalCrafter are quite strong. However, since most of the competing approaches were published prior to the release of these benchmarks, it would be beneficial for the authors to include the FVD metric to compare their approach with the competing baselines. Additionally, could the authors provide a comparison of the generation and training speeds of their approach relative to previous works?

### Questions
Please refer to the questions (or issues) mentioned in the Weaknesses section.

### Soundness
2

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
5

### Summary
This work presents an effective flow matching approach for text-to-video generation via both spatial and temporal pyramidal designs. With such an architecture, the training efficiency has been significantly reduced. It has a good conversation that when noise is strong, flow matching is less critical and can be performed at a low resolution. It has a unified flow matching objective instead of having different models for generation and super-resolution. The paper has validated this effectiveness by controlled experiments compared to a baseline with full-resolution with the same computational costs. The source code of this paper is expected to be open-source, which is very helpful to video generation research and industrial communities.

### Strengths
The strength of this paper is multi-fold. 
+ It builds a flow matching model with multiple resolutions for text-to-video generation. The pyramidal flow matching allows the model to train with less computational costs and memory footprints.
+ The whole model has a unified objective instead of optimizing separate modules for video generation and super-resolution, using a single Diffusion Transformer.
+ The experimental results are competitive, with evaluation on two public benchmarks of VBench and EvalCrafter. The visual quality is comparable to other commercial text-to-video models.
+ The technical explanation for inference with renoising to solve jump points is clear with supplemental materials.
+ The model can be extended to image-to-video generation. 
+ The ablation studies are conducted to illustrate the contribution of different component in the model.

### Weaknesses
While this work has an interesting novel design for flow matching for video generation and competitive visual results, there are some unclear points and weaknesses as follows.
- Questions about [s_k, e_k]. The authors divide [0,1] into K time windows [s_k,e_k]. Why don't the authors set e_{k+1}=s_k? Instead, the authors use e_{k+1}=2s_k/(1+s_k) and we can that e_{k+1}>s_k. This means there are overlapping time windows. Given a time step t, t may fall on more than one time step, and how do authors handle such a scenario? Also, is s_K equal to zero? Could you show what the exact values of [s_k,e_k] are? The choice of $e_{k+1}=2s_k/(1+s_k)$ is not well-motivated and it is unclear why this specific formulation is used instead of a simpler non-overlapping scheme. The overlapping nature of these time windows raises concerns about the consistency and stability of the training process, as a single time step could potentially influence multiple levels of the pyramid, leading to unintended interactions.
- The Figure 1(b) and Figure 3 are not consistent. x^i_t takes x^{i-1}^t with the same spatial resolution as part of the history in Figure 3, but Figure 1(b) shows x^i_t takes x^{i-1}_t' with lower resolution as a temporal condition. This part confuses me. The inconsistency between these figures makes it difficult to understand the exact information flow within the model. Specifically, it is unclear how the temporal conditioning is applied across different pyramid levels, and how the model ensures that the temporal information is properly propagated while also being spatially downsampled.
- The model is autoregressive in the temporal domain, and does it mean that the model can generate videos with arbitrary lengths? Why the inference is limited to videos up to 10 seconds? The limitation to 10-second videos is not clearly justified given the autoregressive nature of the model. It is unclear if this is a fundamental limitation of the architecture or an implementation choice. The paper should clarify whether the model can be extended to longer videos, and if so, what modifications would be required.
- When performing the ablation study for the temporal pyramid, the baseline "full-seq" has only qualitative results. Can the authors provide quantitative results or something similar to the plot in Figure 7? The lack of quantitative results for the "full-seq" baseline makes it difficult to assess the true impact of the proposed pyramidal approach. A quantitative comparison, such as FVD scores, would provide a more objective evaluation of the model's performance.

### Questions
In the rebuttal, I hope the authors can address my questions and concerns in the weakness section.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposed a pyramid-based flow matching for efficient training of video diffusion models. Unlike traditional flow matching which operates on a single resolution, the proposed spatial pyramidal flow matching operates on a pyramid of resolutions. The denoising process starts from a small resolution, and the resolution will increase by 2 after several sampling steps. To address the discontinuity of the jumping point, the paper proposed a novel re-noising formula. For video generation, the paper proposed an autoregressive approach, where the generation of each frame is conditioned on the low-resolution of previous frames.

### Strengths
- The ideas of both spatial pyramids and temporal pyramids are novel and interesting.
- The training efficiency is largely improved due to the novel pyramid design.

### Weaknesses
 - The analysis of inference efficiency is lacking. How does the proposed method compare to previous full-attention methods for different numbers of frames, specifically considering the computational cost and latency for varying video lengths? A more detailed breakdown of FLOPs and memory usage would be beneficial.
- Compared to full-attention methods, the proposed autoregressive method may encounter the issue of error drifting when the number of frames increases. At how many frames, the proposed method will fail, and what is the nature of the failure? It would be helpful to see a quantitative analysis of the error accumulation over the generated sequence, perhaps by measuring the divergence from a ground truth video or by analyzing the consistency of generated features across frames.
- It will be good to include some video results from previous methods on the project page, especially to highlight the qualitative differences in motion and detail.
- Figure 7 and Figure 8 both show partial results before training convergence. It will be more convincing to show the training graph with more training iterations or converged training behavior, including loss curves and metrics that demonstrate the stability of the training process. The lack of converged results makes it difficult to assess the final performance of the proposed method.
- The text-video alignment is worse compared to previous methods. It is unclear if this is due to the model architecture or the training data. A more detailed analysis of the text-video alignment quality, perhaps using metrics like CLIP score or other text-video similarity metrics, would be beneficial.

### Questions
- During training (Equation-16), noisy condition is used. During testing (Equation-17), clean generated frames are used. Will there be a training-testing distribution mismatch?
- How is text condition added to the model?

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
This paper introduces pyramidal flow matching, a new video generative model that combines spatial and temporal pyramid representations, which can enhance the training efficiency and maintains high video generation quality.

### Strengths
This paper proposes a novel pyramidal flow matching algorithm based on the premise that the initial timesteps in diffusion models are quite noisy and uninformative. This approach builds upon the recent prevalent flow matching framework to address the shortcomings of existing methods, specifically the requirement of employing distinct models at different resolutions, which sacrifices flexibility and scalability.

### Weaknesses
1. The authors should clarify the specific implications of how the separate optimization of each sub-stage hinders knowledge sharing and sacrifices flexibility. This is crucial as it relates to the foundational aspects of the problem design presented in this paper.
2. The proposed method involves many parameters that require manual design. The authors should provide more explanations when designing these parameters, such as time windows and γ.
3. Figures 2 and 3 in the paper are overly simplistic, and the authors should provide a detailed explanation of their relationship to the equations.

### Questions
1. The authors should clarify whether their proposed method can be applied to text-to-image models, as the method appears to have limited relevance to video generation.
2. The authors should explain why they opted for flow matching over DDIM, as well as outline the advantages of flow matching.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a novel video generation method to address the problems of the current methods. The SOTA (state-of-the-art) methods mostly suffer from heavy computational burdens due to cascaded architectures or separate optimization for different resolutions of video generation training. The authors address this issue with a novel pyramid flow matching framework, both in the spatial and temporal domains. In the spatial domain, the method builds a pyramid of different resolution frames, where the early stages operate on compressed, low-resolution representations (latent representations) of the frames. As the stages go higher up, the resolution increases, and the full resolution is only used in the final stage for optimization. Temporal compression is achieved by using only a lower resolution history of previous frames (to understand motion and scene), further reducing computation for long videos. This pyramidal approach reduces redundant computation by focusing resources only on necessary parts, making training more efficient. The results are comprehensive and satisfactory. Overall, a good paper to be accepted.

### Strengths
The computational complexity of SOTA video generation methods is a real problem, and the pyramidal flow matching solution provided by the authors is interesting and effective.

The pyramidal flow matching framework is built on a single diffusion transformer model and can be optimized in a unified, end-to-end fashion. This saves time and enables better knowledge sharing. Better knowledge sharing can help achieve greater consistency in the generated videos, which is evident from the generated results.

Evaluated on benchmarks like VBench and EvalCrafter, the model demonstrated high performance, especially compared to methods trained with open-source data.

The model also achieved competitive performance during the user study, and I have personally checked their provided anonymous website for the videos, which looked good.

### Weaknesses
The mathematical notations are not clearly defined. For example, the authors start with s_k, e_k​, x_{s_k}​​, or x_{e_k}​​, etc., without properly defining them first. This hinders the flow of the paper. Please resolve all such issues.

Overall, the writing style of the paper is a bit convoluted (especially in the methods section); it should be revised for smoother understanding.

There is no ablation study on the number of pyramid stages, which is a crucial factor in their design choice.

There is no comparison between the number of parameters and FLOPs used by other open-source methods and the proposed method. This can reflect how effective the model is compared to other methods.

### Questions
What are the training data used by the other compared methods (especially the ones trained with open-source data)?

How much overlap is there between the training data used in the proposed method and the other methods?

Why did the authors keep the number of pyramid stages set to 3 in all the experiments? There should be an ablation study on the number of pyramid stages.

What are the number of parameters and/or FLOPs (operations) used by other (open-source) methods for video generation?

### Soundness
4

### Presentation
2

### Contribution
4
