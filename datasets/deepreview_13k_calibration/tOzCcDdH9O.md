# Matryoshka Diffusion Models

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 8, 6, 5

## Abstract
Diffusion models are the \emph{de-facto} approach for generating high-quality images and videos but learning high-dimensional models remains a formidable task due to computational and optimization challenges. Existing methods often resort to training cascaded models in pixel space, or using a downsampled latent space of a separately trained auto-encoder. In this paper, we introduce {\Model} ({\model}), an end-to-end framework for high-resolution image and video synthesis. We propose a diffusion process that denoises inputs at multiple resolutions jointly and uses a NestedUNet architecture where features and parameters for small scale inputs are nested within those of the large scales. In addition, {\model} enables a progressive training schedule from lower to higher resolutions which leads to significant improvements in optimization for high-resolution generation. We demonstrate the effectiveness of our approach on various benchmarks, including class-conditioned image generation, high-resolution text-to-image, and text-to-video applications. Remarkably, we can train a \emph{single pixel-space model} at resolutions of up to $1024\times1024$ pixels, demonstrating strong zero shot generalization using the CC12M dataset, which contains only 12 million images.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a diffusion model capable of denoising multiple resolutions simultaneously. To enhance computational efficiency, they use a nested UNet structure. While it is possible to train the model all at once, the results show that progressively training it led to better convergence.

### Strengths
The proposed model converges faster compared to traditional cascaded diffusion models. In the case of MS-COCO, the model demonstrates superior performance.

### Weaknesses
It is anticipated that there will be an increase in computational load. And the performance does not seem to surpass that of LDM, which employs classifier-free guidance. Also, since multi-ratio and resolution training is already being conducted in stable-diffusion XL, the proposed method with multi-resolution training is not much novel.

### Questions
It is curious about the computational load increases. Also, it would be nice if the performance difference with usual UNet and NestedUNet is provided.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a new framework for high-resolution image synthesis using diffusion models. Due to computational limitations, diffusion models are often limited to cascaded approaches in pixel-space or operating in latent space. The proposed framework, Matryoshka Diffusion Models (MDMs), denoises images at various resolutions simultaneously. MDM is trained using the standard diffusion objective jointly at multiple resolutions with a progressive schedule where the higher resolutions are added into the objective later in training. The authors demonstrate that MDM has greater efficiency with comparable performance on image and video generation.

### Strengths
- The proposed framework is straightforward and easy to understand, drawing inspiration from existing GAN literature to address limitations of current diffusion models for high-resolution synthesis.
- The authors evaluate MDM on multiple synthesis tasks and demonstrate comparable results. The qualitative results look impressive especially given the relatively small scale of training data.
- Ablation studies quantify the effects of progressive training and the number of nested levels on the quality and alignment of the outputs.

### Weaknesses
 - The variables in the provided pseudocode for the NestedUNet architecture are not clear. A quick description to clarify the inputs to the function would be beneficial.
- In Table 1 we see that there is a noticeable gap between MDM and the baselines. It would be helpful if the authors provided insight as to why they think this may be the case. Specifically, the FID score for MDM is significantly worse, suggesting a potential issue with either the training procedure or the model's ability to capture the data distribution effectively. It would be beneficial to see a more in-depth analysis of this discrepancy.
- The authors highlight video generation as a contribution of MDM, but there is no discussion of the experiments or results (aside from implementation details and a few subsampled frames). It is difficult to get a sense of MDM's performance for this task. The lack of quantitative metrics and comparisons to existing video generation models makes it hard to assess the true value of this contribution.
- There are several typos (especially with spacing before citation parentheses on page 8).

### Questions
- Generally the experiments section would benefit from including more insights on the results, especially for the scenarios where MDM is outperformed by the baselines.
- While there is some differentiation already denoted through the colors, it would be helpful to explicitly label the novel pathways introduced by the NestedUNet architecture in Figure 3 to clearly distinguish from skip connections from the original UNet.
- It is helpful to understand how the proposed multi-resolution prediction affects sampling speed.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a multi-stage image/video generation model based on f-DM. The model is structured as a NestedUNet: a UNet with multiple inputs/outputs of increasing/decreasing resolutions. Compared to f-DM, it incorporates progressive growing and benchmarks the approach on multiple large-scale text-to-image and text-to-video datasets. The works positions itself as a new paradigm for high-resolution diffusion models and rivals latent DMs and cascaded DMs. It features faster training convergence in terms of the amount of iterations compared to the existing paradigms. The obtained results visually look quite good to me.

### Strengths
- Visually, the results look very good. And it is especially remarkable given the little compute used to train the models.
- A good advantage of the given method is that, compared to CDMs, it does not need require the previous stage to be well-trained to have meaningful training of the current stage with reliable scores. For CDMs, while it's possible to train all the stages simultaneously, one cannot generate images from scratch in the middle since the base stage has not been fully trained yet. Somehow, this does not happen for the given model.
- The ablations and evaluation in general is quite solid.
- The exposition is good, and the paper is written well.

### Weaknesses
 - The method is not end-to-end (or at least does not perform well when trained in the end-to-end manner), despite what the paper claims. If I am not mistaken, at the end it still trains stage-by-stage similarly to CDMs — and without such stage-by-stage training it produces considerably worse results.
- The paper does not report training costs rigorously for all the experiments, and it's impossible to compare between methods without knowing their training cost.
- The comparison to CDMs does not seem fair, since the paper compares to under-trained CDMs. If one trains CDMs withing a limited computational budget, then more focus should be put on the base stage, since the final stages converge much faster. It is unclear if the reported results for CDMs are the best achievable within the given budget.
- FID scores on ImageNet are ~3x times higher than the current SotA (e.g., MDT). It is unclear whether this is due to insufficient training or an inherent limitation of the method. It would be beneficial to see a comparison of fine-tuning MDM and CDM from a well-performing pixel-space diffusion model, such as EDM, to better understand the method's potential.
- The paper makes a claim about good results on a small text-to-image dataset (CC12M), but does not compare to existing large-scale text-to-image generators. This makes it impossible to evaluate this claim — e.g., Figure 8c should contain the results of existing text-to-image generators to make the existing model comparable. Otherwise, such a claim is not grounded. Judging by the maximum CLIPScore on a CLIP/FID trade-off chart is wrong since in the Imagen's paper, one can notice that even their bad models can attain very high CLIP scores under a strong enough guidance.

- "crtical" => "criticial" (page 2)
- "under performs" => "underperforms" (page 6)
- "eg" => "e.g." (page 7)
- page 8 — no space before the bracket "(" in multiple places.

### Questions
- What are the computational budgets of all the experiments? (I can only see the amount of GPUs being used for the experiments — without a notice on for how long). I believe that the smaller amount of training could also justify inferior FID results on ImageNet compared to SotA.
- Are there any other differences compared to f-DM [1] apart from the progressive training idea and larger-scale experiments? It seems that f-DM uses the same NestedUNet idea, but the f-DM authors just do not call it a "NestedUNet". Do you use the same noise schedule as f-DM?
- To be honest, I do not quite understand why the FID on ImageNet is so high. Samples in Figure 5 looks very good to me (given that they are random samples). What CFG weight was used generate them?
- Please, include the comparison with existing text-to-image generators. Judging by the maximum attainable CLIP score is misleading.
- I find the results on video generation to be quite good. For how long has the model been trained and was there joint image/video training (or image pretraining) used?
- Why do you think your model does not suffer from the "train/test gap" problem of CDMs and its late stages can generate meaningful images even when the low-resolution stage has not been trained yet?
- I have a suspicion that the video generator can struggle in generating videos with moving scenes because the base low-resolution generator produces just a single frame. Could you please provide the video results for moving scenes? And in general include some mp4/gif videos in the submission (i have not found any in the supplementary).

Some typos:
- "crtical" => "criticial" (page 2)
- "under performs" => "underperforms" (page 6)
- "eg" => "e.g." (page 7)
- page 8 — no space before the bracket "(" in multiple places.

[1] Gu et al "f-DM: A Multi-stage Diffusion Model via Progressive Signal Transformation"

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Matryoshka Diffusion Models for high-resolution image and video synthesis. Unlike conventional approaches that use either cascade models or latent diffusion models with an additional autoencoder, Matryoshka Diffusion Models uses a diffusion process that denoises the multi-resolution input jointly, where such a process can be trained progressively and improves the optimization efficiency significantly. The paper shows the effectiveness of the method on popular image generation and video generation tasks and verifies the training efficiency of the method compared with existing diffusion model variants.

### Strengths
- The paper is generally well-written and easy to follow. 
- The paper is well-motivated.
- The paper conducts experiments with various datasets, including ImageNet, MSCOCO, and WebVid-10M.
- The high-resolution image generation results are quite impressive.

### Weaknesses
 - The paper lacks an analysis on "comparison with literature". The paper simply states the result is comparable to other baselines, but the results show a clear gap (e.g., FID 3.60 (LDM) while 6.62 (MDM) on ImageNet 256x256). In this respect, the authors should provide an extensive analysis and reasons why the performance is worse than the baselines, not just saying the proposed method shows comparable performance. 
- To verify the "faster convergence", I think x-axis in Figure 4 should be wall-clock time rather than training iterations. Otherwise, I think the authors should provide time/iteration for each baseline used for the evaluation. 
- Some important implementation details are missing: learning rate, batch size, model configurations, etc. 
- Missing quantitative evaluation on text-to-video generation compared with existing baselines.
- No video files included for illustrating text-to-video generation results.
- Why some points in Figure 4 (e.g., after 200K of Latent DM in Figure 4(a)) are missing?

### Questions
- Why some points in Figure 4 (e.g., after 200K of Latent DM in Figure 4(a)) are missing?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
