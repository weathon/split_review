# Deep Compression Autoencoder for Efficient High-Resolution Diffusion Models

- Decision: Accept
- Scores: 6, 8, 8, 6, 6

## Abstract
We present \modelfull (\modelshort), a new family of autoencoders for accelerating high-resolution diffusion models. Existing autoencoders have demonstrated impressive results at a moderate spatial compression ratio (e.g., 8$\times$), but fail to maintain satisfactory reconstruction accuracy for high spatial compression ratios (e.g., 64$\times$). We address this challenge by introducing two key techniques: (1) \textbf{Residual Autoencoding}, where we design our models to learn residuals based on the space-to-channel transformed features to alleviate the optimization difficulty of high spatial-compression autoencoders; (2) \textbf{Decoupled High-Resolution Adaptation}, an efficient decoupled three-phase training strategy for mitigating the generalization penalty of high spatial-compression autoencoders. With these designs, we improve the autoencoder's spatial compression ratio up to 128 while maintaining the reconstruction quality. Applying our \modelshort to latent diffusion models, we achieve significant speedup without accuracy drop. For example, on ImageNet $512 \times 512$, our \modelshort provides \textbf{19.1$\times$} inference speedup and \textbf{17.9$\times$} training speedup on H100 GPU for UViT-H while achieving a better FID, compared with the widely used SD-VAE-f8 autoencoder.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a family of autoencoders that achieve comparable or better reconstructions compared to the SD autoencoders while having a much stronger spatial compression rate, resulting in efficiency gains for downstream tasks such as latent diffusion training.
Using the techniques or residual autoencoding and decoupling high-resolution adaptation, the model is able to generalize well to higher resolutions while having a very large compression factor (x32, 64 vs 8 for SD-VAE).

### Strengths
* The paper is well written and easy to follow.
* The method allows to significantly reduce the computational requirements to train large scale diffusion models at high resolution, making it more accessible as a research topic.
* Evaluation of multiple metrics across 4 different datasets are reported.
* Evaluations on downstream diffusion training is also provided.
* Qualitative examples clearly showcase the improvements brought about by the proposed model.

### Weaknesses
 * What parameters were used for sampling the diffusion models (sampler, number of sampling steps, guidance scale) ? A more through investigation on the impact on sampling quality would be useful to get a better grasp of the limitations of this method.
* Missing ablations on the constituent parts of DC-AE.
* In tables 3 and 4, missing comparisons with more recent autoencoders such as the one from SD-XL, SD3, and Asymetric Autoencoder.
* In table 5. the PixArt model trained with DC-AE achieves a lower CLIP score than the one trained with SD-VAE while the text says otherwise (maybe a typo?). What if the memory usage is equalized with the SD-VAE by increasing the batch size, do the improvements get larger or do they stagnate ?
* While increasing the patch size is one method to reduce spatial resolution, one can also use a pixel shuffle operation in order to achieve a lower spatial dimension with a higher channel dimension. How does this simple operation, using SD-VAE compare with your method ?
* Training LDMs requires a shift and scale factor to be applied to the latents before the diffusion process, how are these values computed in your experiments ?

### Questions
* While increasing the patch size is one method to reduce spatial resolution, one can also use a pixel shuffle operation in order to achieve a lower spatial dimension with a higher channel dimension. How does this simple operation, using SD-VAE compare with your method ?
* Training LDMs requires a shift and scale factor to be applied to the latents before the diffusion process, how are these values computed in your experiments ?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper looks at the problem of scaling image autoencoders, used with generative models, to higher spatial compression rates without reducing visual quality. The authors identify a problem with existing AEs: visual quality degrades with higher spatial compression rates (Fig. 2) even when increasing the number of channels in the latent representation to maintain a fixed total size (see the "latent shape" column in Table 2). They also observe a quality degradation when generalizing from low resolutions (used for training) to higher-resolutions.

These observations imply that "high spatial-compression autoencoders are more difficult to optimize" so the paper introduces an architecture change ("residual autoencoding") and a training change ("decoupled high-resolution adaptation") to improve results with high spatial compression rates and to reduce generalization error across resolutions.

Residual autoencoding (Fig. 4) replaces strided conv blocks used for up/downscaling with residual blocks that learn a residual added to space-to-depth (for downscaling) or space-to-depth (for upscaling) blocks. The model uses channel averaging to adjust the number of channels when there is a mismatch, and authors also use channel averaging for a new kind of residual block even when there is no up/downscaling.

Decoupled high-resolution adaptation (DHRA) switched from a single-stage approach for training the AE to a three-stage appraoch (Fig. 6). In the standard approach, the AE is trained on low-res data using all reconstruction losses (typically mse + perceptual + adversarial). In DHRA, the stages are:
 1. low-res images optimized without the adversarial loss
 2. finetune with high-res images with only the "inner" layers (end of encoder, beginning of the decoder) trained. Other layers are frozen and, again, no adversarial loss is used.
 3. finetune again with reconstruction and adversarial losses. Only the final layers of the decoder are trained.

The authors argue that this multi-stage approach is more efficient than training the full model on high-res images, and it prevents the adversarial loss from affecting the encoder which helps with generalization.

The authors validate their claims by training models and evaluating reconstruction quality (Table 2) and generation quality (Tables 3 and 4). They also provide some example images for qualitative evaluation (Fig. 7 and in the supplementary material).

### Strengths
The primary strength of this paper is the development of an effective and relatively simple solution to a real-world deficiency that impacts all research and products using autoencoders. Specifically, the use of residual autoencoding and DHRA allow either better visual quality (e.g., in Table 3 look at rows witht he same number of tokens like SD-VAE-f16 with patch-size=2 or SD-VAE-f32 with patch-size=1 to DC-AE-f32) or similar visual quality with lower latency and higher throughput (e.g., Table 3 comparing SD-VAE-f32 to DC-AE-f64).

Another strength is that the authors evaluate their method on both reconstruction and generation problems. Improvements on just reconstruction still have some value, but many improvements to reconstruction quality do not translate to gains on the generation side.

### Weaknesses
A more detailed summary of the DC-AE architecture would help. Fig. 4 provides a high-level overview, but I'm not sure how literal or complete it is, and the details of the "Encoder/Decoder Stages" are not provided. To be fair, the authors do provide code, but architecture and training details should be in the paper (probably in the appendix).

The conjecture in Section 3.3 that DC-AE helps because otherwise the "diffusion model needs to simultaneously learn denoising and token compression when using a patch size > 1" is pretty hand-wavy. For example, I can always set patch_size=1 and add add a space-to-depth layer to the encoder and claim that now the encoder alone is responsible for token compression. That said, I don't have a better explanation, but I think it's ok for papers to accept that the contribution is a better architecture justified with empirical evaluation.

Regarding generalization across resolutions, I'm wondering how much changes to the training procedure can close the gap even with single-stage training. In particular, it makes sense that the statistics for a fixed-size patch (say 32x32 pixels) is very different between a 256x256 image and 1024x1024 pixel image of the same scene. You could train on 256x256 *crops* from a 1024x1024 dataset (rather than downscaling), but then you'd have a generalization gap in the other direction.

In other work, researchers try to avoid this problem by generating low-res training sets by randomly downscaling high-res sets. With enough training, this approach lets the model see the full range of statistics. Was this done for the experiments in the DC-AE paper? If not, do you think it's sufficient or perhaps complementary to DHRA? Either way, I still see potential benefits of DHRA, e.g., maybe it's good that the GAN doesn't influence the encoder (and thus the latent space), but this isn't investigated, in isolation, in the paper.

You can also frame higher spatial-compression rates as meaning that the model sees less training data (as measured by number of latents) per fixed-size image. This means that any negative affects from the boundary are exacerbated (e.g., if zero-padding is used for conv layers). In the extreme, imagine using f256 with 256x256 training data -- we certainly wouldn't expect this model to generalize to higher resolutions. Some discussion of these effects would help, and investigation of whether the generalization issue is mostly one of different pixel statistics or of boundary artifacts would strengthen the paper.

Did you experiment training different numbers of layers in Stage 2 and Stage 3? A graph showing the impact (training speed vs. evaluation metrics) as the number of layers increases would be interesting.

### Questions
Regarding generalization across resolutions, I'm wondering how much changes to the training procedure can close the gap even with single-stage training. In particular, it makes sense that the statistics for a fixed-size patch (say 32x32 pixels) is very different between a 256x256 image and 1024x1024 pixel image of the same scene. You could train on 256x256 *crops* from a 1024x1024 dataset (rather than downscaling), but then you'd have a generalization gap in the other direction.

In other work, researchers try to avoid this problem by generating low-res training sets by randomly downscaling high-res sets. With enough training, this approach lets the model see the full range of statistics. Was this done for the experiments in the DC-AE paper? If not, do you think it's sufficient or perhaps complementary to DHRA? Either way, I still see potential benefits of DHRA, e.g., maybe it's good that the GAN doesn't influence the encoder (and thus the latent space), but this isn't investigated, in isolation, in the paper.

You can also frame higher spatial-compression rates as meaning that the model sees less training data (as measured by number of latents) per fixed-size image. This means that any negative affects from the boundary are exacerbated (e.g., if zero-padding is used for conv layers). In the extreme, imagine using f256 with 256x256 training data -- we certainly wouldn't expect this model to generalize to higher resolutions. Some discussion of these effects would help, and investigation of whether the generalization issue is mostly one of different pixel statistics or of boundary artifacts would strengthen the paper.

Did you experiment training different numbers of layers in Stage 2 and Stage 3? A graph showing the impact (training speed vs. evaluation metrics) as the number of layers increases would be interesting.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a new type of autoencoder for high resolution generative diffusion models. Autoencoders are used in generative diffusion models primarily to reduce the computation necessary for training and evaluation. However, there is some loss of representation capacity in mapping the image to the latent domain. The loss of representation capacity becomes more severe with higher downsampling ratios, which limits compute gains beyond those provided by 8X downsampling, as well as high-resolution generation.

The present paper aims to expand the possible range of downsampling ratios to as high as 64X. The paper achieves this first by analyzing the challenges of higher downsampling ratios, finding that staged architectures actually have worse performance than architectures with simple space-to-channel operations. Following this, the paper proposes a new architecture with residual space-to-channel and channel-to-space connections that effectively skip the information across network blocks, improving optimization High-resolution performance after adopting the residual space-to-channel operations still left some to be desired, so the paper further proposes a decoupled high-resolution adaptation procedure that finetunes the head of the decoder while finetuning the rest of the model. A second stage tunes the middle layers.

In numerical experiments the trained autoencoders exhibit better reconstruction accuracy than their counterparts from stable diffusion, which are commonly used in the community. The full diffusion models show promising FID numbers vs. stable diffusion with more efficient training in both quantitative and qualitative examples.

### Strengths
1. The paper is well-written and easy to follow.
2. The baselines using stable diffusion are well-known and recognized by the community.
3. The qualitative examples seem compelling.
4. The advantages with using less compute could be of significant impact.

### Weaknesses
1. The authors mostly use stable diffusion for all experiments, although several datasets are considered.
2. A more detailed quantitative analysis of why standard staged training has difficulties with gradient propagation is not presented.
3. The proposed modifications are somewhat incremental - this seems close to simply removing some skip connection convolutions + a reshape operation in the standard stable diffusion autoencoder. The extra fine-tuning procedure is more detailed, but is only necessary due to the autoencoder changes.
4. Autoencoder comparisons in Table 2 are only done at high downsampling ratios - not sure how the proposed architecture performs with shallow downsamples.
5. Only the FID metric (presumably with the Inception V3 backbone) is used to evaluate the models.

### Questions
My overall rating is due to the somewhat limited set of modifications and the limited experiments, which should be a topic for rebuttal. In addition, I also have the following questions:

1. Did you adopt all the same loss functions and GAN architectures as in the stable diffusion paper?
2. How often does the proposed architecture output artifacts?
3. Are the images in all figures random-samples or selected? This should be made clear in the text.
4. Did you consider other operations for space-to-channel other than averaging? Same question for channel duplication in the upsampling process.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a new VAE architecture for latent diffusion generative modeling along with a multi-step training recipe. More specifically, the proposed design combines space-to-channels with averaging to build deep autoencoders with a high spatial subsampling factor (up to 64x). In order to train these models effectively at high resolution, they are first trained at low resolution without GAN loss, then partially tuned at higher resolution, and then refined with a GAN loss. The more aggressive subsampling leads to lower spatial resolution/sequence length in the latent space than VAEs from the literature and hence leads to substantial speed-ups of about 4x to 16x while maintaining generation quality, in combination with different latent diffusion models.

### Strengths
- The proposed architectural modifications are simple and sound, and the corresponding multi-step training recipe is relatively simple as well.
- The speed-ups are quite substantial.
- The method is tested on a broad range of data sets (including text-to-image modeling), and in combination with different latent diffusion models. So the results are quite comprehensive.

### Weaknesses
 - The role of the space-to-channels-based autoencoder design and the multi-step training recipe are entangled. How does the baseline autoencoder (with more aggressive subsampling) perform, when it is trained with the multi-step recipe? Specifically, a quantitative comparison of reconstruction metrics (e.g., rFID, PSNR, SSIM, LPIPS) between the baseline autoencoder and the proposed DC-AE, both trained with the multi-step recipe, would help disentangle the contributions of architecture and training.
- The paper seems to lack important experimental details, including optimizer, learning rate, schedule etc. These are important in particular given the multi-stage training with different losses (including a GAN loss). Also, what losses does the method use exactly? It looks like the low resolution stage uses a perceptual loss (Figure 5). A detailed description of the loss functions used at each stage, along with the specific hyperparameters and optimization settings, is crucial for reproducibility and understanding the training dynamics.


Minor:
- In the side-by-side comparisons it would be useful to have the original image as additional reference.
- Some prior works discuss the relevance of space-to-channel in image enhancement/generation methods, probably worth mentioning (see e.g. Shi et al. "Real-time single image and video super-resolution using an efficient sub-pixel convolutional neural network." CVPR 2016) [1]

### Questions
- What is the role of the averaging compared to simple space to channel? How would the model behave without the averaging? Would the channel dimension grow too fast?
- How does the use of EfficientViT blocks affect the quality (reconstruction/generation) of the method? Does it lead to better behavior when trained with large subsampling factors compared to the baseline?
- “..., we assume the number of sampling steps is 1.”: Does this also hold for inference throughput and latency? If so, I would suggest reporting the throughput/latency to sample a full image.
- What is the resolution of the images in Figure 7? It would generally be helpful to indicate the resolution for the visual examples in the caption.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The submission presents Deep Compression Autoencoder (DC-AE), a new series of autoencoders that enable highly efficient high-resolution image synthesis with latent diffusion models. The key architecture design is the adding residual connection with space-channel inter-play in both downsampling and upsampling layers, which alleviates the optimization difficulty significantly. They further propose decoupled high-resolution adaptation, a three-phase training strategy that mitigates the generalization penalty of high spatial-compression autoencoders. By improving the autoencoder's spatial compression ratio up to 128 while maintaining reconstruction quality, DC-AE provides significant speedups for both training and inference of latent diffusion models without sacrificing image generation accuracy. The authors demonstrate the effectiveness of DC-AE on various datasets and diffusion transformer architectures.

### Strengths
-	Novel autoencoder design for high compression ratios. The authors introduce additional non-parametric residual connections in the downsampling and upsampling layers, which facilitate the optimization of autoencoders in high spatial compression ratio scenarios.
-	The authors carefully design a three-stage training recipe to mitigate the high-resolution generalization gaps by fine-tuning the trained AE on high-resolution data with minimal additional costs.
-	The proposed DC-AEs show a substantial reduction in training and inference costs of latent diffusion models on various datasets.

### Weaknesses
-	Although the VAE shows little FID loss as it progresses to a higher spatial compression ratio (DC-AE-f32 to DC-AE-f64), it does not translate to similar results in the corresponding latent diffusion models as shown in Table 3. The underlying reason is probably that a diffusion model with higher capacity is required when dealing with high compression ratio latents.
-	The current submission lacks either theoretical analysis or illustrative toy examples on the proposed design choice of space-channel residual connection, e.g., comparisons on the loss landscapes. Specifically, the paper does not provide sufficient justification for why the proposed space-channel residual connections are superior to other possible residual connection strategies, such as purely spatial or purely channel-wise connections. The lack of ablation studies on different residual connection strategies makes it difficult to assess the true contribution of the proposed method.

### Questions
-	Could you please clarify the experimental settings and AE architectures in Section 3.1? By Line 161 ‘… convert the latent to higher spatial compression…’, do you mean that the f8 to f64 AEs have the same output latent size initially, yet f32 and f64 AEs further squeeze the space dimension into channel dimension?
-	In Table 5, the proposed method shows a lower CLIP score with the Pixart diffusion transformer, is it a typo?

### Soundness
3

### Presentation
2

### Contribution
3
