# Regularization by Texts for Latent Diffusion Inverse Solvers

- Decision: Accept
- Scores: 8, 8, 6

## Abstract
The recent advent of diffusion models has led to significant progress in solving inverse problems, leveraging these models as effective generative priors. Nonetheless, there remain challenges related to the ill-posed nature of such problems, often due to inherent ambiguities in measurements or intrinsic system symmetries. To address this, drawing inspiration from the human ability to resolve visual ambiguities through perceptual biases, here we introduce a novel latent diffusion inverse solver by {\em regularization by texts} (TReg). Specifically, TReg applies the textual description of the preconception of the solution during the reverse diffusion sampling, of which the description is dynamically reinforced through null-text optimization for adaptive negation. Our comprehensive experimental results demonstrate that TReg successfully mitigates ambiguity in the inverse problems, enhancing their effectiveness and accuracy.
  \keywords{Inverse problems \and Text regularization \and Latent diffusion model}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a novel method for solving inverse problems using diffusion models, with a focus on reducing ambiguity in the solutions.
The authors propose a latent diffusion inverse solver that incorporates regularization by texts (TReg), which applies textual descriptions of the expected solution during the reverse sampling phase. 
During training, this text guidance is dynamically adjusted through null-text optimization for adaptive negation.

Overall, I think this is a good paper.

### Strengths
* this paper introduces an explicit regularization term during training via text-driven regularization (TReg)
* the proposed TReg effectively addresses the challenge of ambiguity in inverse problems
* this paper further introduces an adaptive negation to dynamically adjust the influence of textual guidance
* the paper is well written and easy to follow, extensive in main text and supplementary demonstrate the effectiveness of the proposed method for diffusion inverse solvers

### Weaknesses
1. lack of overall results over whole dataset. all the experiments results are shown in visualizations or subset results of specific classes.
2. i notice in both table 1 and table 2, PSNR scores are higher without adaptive negation, do authors have any analysis or intuition about this results?
3. (this might not be a weakness, just naturally curious) in the experiments, the text regularization is only tested with class name, how about the results using some natural captions (such as generated with BLIP or GPT)?

### Questions
please refer to weakness part.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces TReg (Regularization by Text), a method for solving inverse problems in image processing using latent diffusion models by conditioning on text.  TReg leverages user provided textual descriptions to guide the image reconstruction process.

Prior diffusion-based inverse solvers often struggle with ambiguity, as multiple different images can produce the same degraded output. TReg addresses this by incorporating textual prompts as a form of regularization. The authors frame the problem as a text-conditioned latent optimization, where the goal is to find a solution that is both consistent with the measurements and aligned with the provided text description.

The authors introduce the following:
* A text based regularization term that encourages the reconstructed image's latent representation to be close to a text-conditioned denoised estimate. This helps guide the sampling trajectory towards solutions that are semantically aligned with the text.
* To further refine the textual alignment, this method uses a novel "null-text optimization" technique. This dynamically adjusts the influence of the textual guidance during the reverse diffusion sampling process, suppressing unintended signal components.


The authors also discuss limitations, particularly the challenge of finding suitable text prompts for some challenging inverse problems where the problem is extremely ill posed.

### Strengths
Overall the paper is well written, provides clear motivation, and the authors perform reasonably comprehensive experiments. The authors do a good job in their logical flow and provide pretty clear explanations of the proposed method and experimental setup. Figures look nice.

In terms of novelty, they authors introduce a reasonably novel approach to solving inverse problems by incorporating text-based regularization into latent diffusion models.  This addresses a significant limitation of existing solvers, mostly their struggle with ambiguity, and mitigates the need for task specific training. 

The proposed method is technically sound, with a clear mathematical formulation and well-defined optimization procedures.  The integration of LDPS further enhances the method's capabilities.

### Weaknesses
 * `Line 071` In my view the connection to the human brain is quite weak, not sure why the authors put this in the paper...
* I would like to see additional, none cherry picked outputs. In my experience using diffusion models to recover images can often fail in very strange ways. I am specifically interested in image inpainting results, which nearly always result in boundary artifacts.
* I would like to see experiments in the presence of measurement noise, for example with JPEG compression artifacts after gaussian blurring.

### Questions
See above

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
This work uses diffusion models with text guidance in order to solve inverse problems. Inverse problems (e.g., in-painting or deblurring) have been recently tackled using diffusion models, however, their ill posedness nature makes resolving some ambiguities still challenging. The authors propose to leverage a user bias via a text prompt in order to guide the diffusion process towards a solution that is aligned with the description provided. The proposed framework uses a latent diffusion model with classifier-free guidance as a core framework with two innovations compared to previous works: (1) a term that induces alignment between the latent being optimized and that conditioned through the text prompt, and (2) a dynamic null-text adaptation. (1) is the distance between the latent embeddings that are being optimized and those obtained with the text used as guidance (in a classifier free guidance algorithm). (2) The null-text (which usually is the representation provided without any guidance) is updated dynamically in order to be aligned with the CLIP embeddings of the text provided by the user, incentivizing in this way the embeddings to continue to learn new concepts by moving the null-text closer and closer to the text description. 

The authors show results on super resolution, deblurring and Fourier Phase Retrieval problems and compares with some baselines such as DDRM, PGDM, PSLD, and PnP.

### Strengths
The paper tackles an interesting problems with many potential applications. 

While the individual ingredients are not completely new, even in the context of inverse problems (the use of prompts and the idea of solving the problem using alternate direction method have been explored by Chung et al in “PROMPT-TUNING LATENT DIFFUSION MODELS FOR INVERSE PROBLEMS”; the optimization of the null-text has been explored by Mokady et all in “Null-text Inversion for Editing Real Images using Guided Diffusion Models”) the overall framework and the way these ingredients are used is novel and seems to lead to compelling results.

### Weaknesses
 The main weaknesses of this work are in the lack of quantitative evaluations on full datasets, lack of some important baselines and the clarity of the writing could be improved. See below for more detailed comments.

Evaluation: all tasks presented are obtained on specific classes rather than being averaged across full datasets as it is done in other the state of the art works (e.g., P2L). Specifically:
- Ambiguity reduction: it is unclear if the quantitative evaluation in Figure 3 is an average over a dataset or simply the results of the image shown (bear). It is also unclear from which source this image comes from. Maybe it is ok since this is an interesting experiment but not the core? In any case more clarity is needed.
- Accuracy of obtained solution: use true class as c. Results in  Table 1 and Table 2 show quantitative measurements (great) for two tasks (super resolution and de-blurring) but only on two classes “Ice-cream” and “fired rice” rather than averaging across full datasets.
- Accuracy of obtained solution: use different class as c. Results shown in Table 3 are for only two classes using two different C labels (fried rice to spaghetti, and Ice Cream to Macaroons). It is understandable to show selected classes in Figures but the quantitative evaluation should be reported on a larger datasets (with mean and standard deviations).
- Results on non-linear inverse problems. These results are only qualitative shown on 4 different images (Figure 6).

This work shares a lot of similarities with P2L (Chung et al.) so I was expecting P2L to be among the baselines. In the intro when talking about P2L the authors say “However, this method primarily focuses on data consistency and lacks robust alignment with textual prompts.” It would be great to support this statement with quantitative results.

For the alternate directions method there should be some additional information about convergence. Being an iterative method one would expect to see some analysis about it but I did not find any information.

The work of Mokady et al also shares the idea of adaptive negation (but with different application and implementation) so for Inpainint experiments (which are suitable for Mokady) this would also be a useful baseline.

Writing: The paper is not alway easy to follow. The readability of the manuscript would benefit from some re-writing. For example 
- Background session could be summarized and moved to the appendix since these are all known concepts.
- The additional space gained should be used to provide more details about the proposed method. Here are some examples of things that could be clarified but there are more throughout the text:
    - Probably the most important: authors should mention that the proposed update is scheduled to be performed every so many iterations  end not always. This is somewhat hidden in the “range” argument of algorithm 1 but it becomes clear only reading the appendix. I strongly encourage the authors to bring this discussion into the main paper.
    - Consider moving the inpaiting results (with comparison with Mokady) in the main paper.
    - In Eq (13) and (14) there is the term A(x). Given that A is an “imaging system” but it is not clear the role it plays in practice when solving a specific problem. I would recommend the authors to provide some information about the role of the forward operator when discussing section 3.1.
    - “Here, ζ,γ are empirically chosen to satisfy¯αt−1 = ζ/(ζ+ γ).” Please provide an explanation why satisfying this equation is important.
    - …
- Since Figure 1 is even before the abstract the reader should be able to understand it without reading anything but the caption and looking at the figure itself. Consider increasing the details in the caption or moving the figure in a place where the reader has sufficient information to understand all of the examples.
- I find the abstract lacking important details. It should encourage a reader to continue the reading but in order to do so the more details  need to be presented. Here some potential improvements:
    - ``ambiguities in measurements or intrinsic system symmetries.’’ consider adding a concrete example of these problems.
    - define what adaptive negation is  or avoid adding a non-defined term.
    - ``Our comprehensive experimental results’’ consider telling the reader which are the most important quantitive results so that it encourages the reader to continue.
- In the experimental section consider breaking down the baselines for each experimental task. Currently they are presented all at once at the beginning irrespective of the tasks and I find this to be too much information to process and too far from where it is useful.
- The authors used the prompt “A photography of a ….”. This might not be grammatically correct. Photography is the art of creating photos or the process of creating photos. A better prompt would  be “A photo of a…” or “A photograph of a …”. I would be curious to know if this changes the results.
- Tweedie’s formula should be cited.
- From (10) to (13) the terms are swapped. Please consider maintaining consistent order.
- While the fact that the work uses a pre-trained VAE is mentioned in the main paper, I think the fact that also the diffusion model is pre-trained is not explicitly mentioned before the appendix. Consider clarifying this aspect in the main paper.
- The following sentences are unclear, consider rephrasing them: 
    - “We also prepare a situation that different class label is given as a text description. Here, we should carefully set proper text prompt for measurement to avoid ignoring the provided guidance”. 
    - “For the case that given text description is differnet from the original classes, we use “spaghetti" and “macarons", respectively.”. There is a typo (differnet) but beyond that it is unclear what this sentence means.
    - “For data consistency methods, we utilize the measurement itself “. What is the measurement?
    - “TReg leads to a unique solution corresponding to the given text description”. Maybe “TReg leads to similar solutions.”? Possibly one could say “semantically unique and aligned with the text”?
    - “ This discrepancy is clearly observed in pixel-level uncertainty in Figure 3(c). “ I suppose this is the variance computed across the 10 reconstruction? Consider mentioning explicitly how uncertainty is computed.

### Questions
Main questions (answering these questions could affect the recommendation)

- Could the authors provide information about convergence of the alternate direction method? 
- Could the authors provide quantitive evaluation averaged across full datasets (as done in state of art works, e.g., P2L) and include relevant baselines, as mentioned above P2L should be included. Mokady would also be a good comparison for inpainting results. 

Other questions (this are more curiosity driven questions, it is unlucky the answers here will change the recommendation)
- In figure 2 authors show that thanks to the adaptive negation strategy the generated image is less noisy. It is unclear however why this would be the case. Could it be that without adaptive negation one could reach a similar results with more iterations?
- Due to (18) does it mean that the VAE needs to have the same dimensionality of CLIP embeddings?
- “The proposed solver without adaptive negation tends to achieve higher PSNR than with adaptive negation, since it obtains blurry images”. Could the Structural similarity index measure (SSIM) be a better metric in this case?
- For the phase retrieval experiments: the error in the LDPS reconstruction seem to go beyond the ambiguity of symmetries… Do the authors have any intuition about why the quality of LDPS reconstruction is so low compared to TReg?
- How sensitive is this frameworks to slight variation of the text? This would be an interesting discussion of the paper. The authors use “A photography of …” how much do results change if instead they used “A photo of xxx” or simply “xxx”?

### Soundness
3

### Presentation
2

### Contribution
3
