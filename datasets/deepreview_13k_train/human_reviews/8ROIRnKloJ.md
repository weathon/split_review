# $\epsilon$-VAE: Denoising as Visual Decoding

- Decision: Reject
- Scores: 8, 5, 8, 5, 5, 3

## Abstract
In generative modeling, tokenization simplifies complex data into compact, structured representations, creating a more efficient, learnable space. For high-dimensional visual data, it reduces redundancy and emphasizes key features for high-quality generation. 
Current visual tokenization methods rely on a traditional autoencoder framework, where the encoder compresses data into latent representations, and the decoder reconstructs the original input. 
In this work, we offer a new perspective by proposing \textit{denoising as decoding}, shifting from single-step reconstruction to iterative refinement.
Specifically, we replace the decoder with a diffusion process that iteratively refines noise to recover the original image, guided by the latents provided by the encoder.
We evaluate our approach by assessing both reconstruction (rFID) and generation quality (FID), comparing it to state-of-the-art autoencoding approach.
We hope this work offers new insights into integrating iterative generation and autoencoding for improved compression and generation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes an autoencoder trained with diffusion loss, together with LPIPS loss and GAN loss applied on the estimated sample from the diffusion decoder. The authors show improved reconstruction and generation quality comparing to the prior GAN-based autoencoders, which demonstrates the effectiveness of the diffusion loss in joint training.

### Strengths
**Update after rebuttal:**

```
The authors have well addressed my questions and I will keep my rating.

I also looked on the remaining concerns from other reviewers, and do not feel they are major weaknesses:

1. Novelty: To the best of my knowledge, and according to the papers other reviewers listed, I did not find any published paper shows the same results that joint training AE with diffusion loss helps rFID and visual quality, which is an important result to understand the strength of diffusion autoencoders.

2. Inference time: To me this is not the key focus. Any method with diffusion models uses iterative sampling. As long as all reviewers agree on the improvement of evaluation metric and visual quality, this is not a major weakness. Especially given the recent advancements of faster samplers and one-step diffusion distillation.

```

---

1. Diffusion loss for autoencoder training is an important direction to explore. This work is one of the first works that show promising results.
2. The proposed method outperforms prior GAN-based autoencoder on ImageNet with the common metric FID. The trend of compression ratio also shows the advantage of the diffusion loss.
3. The evaluation is comprehensive and well-organized. The number of trainable parameters are also listed for better comparison.

### Weaknesses
1. The LPIPS and GAN loss are applied on the estimated sample, which seems to be not accurate that may cause objective bias in theory. Specifically, the diffusion process is a stochastic process, and applying a deterministic loss like LPIPS on a single estimated sample might not accurately reflect the overall quality of the learned distribution. This could lead to the model optimizing for a specific realization of the diffusion process rather than the underlying data distribution.
2. It is not very easy to note the difference between the baseline VAE and the proposed eps-VAE in Figure 4 (images are compressed in the paper?), especially for 8x downsampling. A higher quality / higher resolution demonstration, zoom-in crops, or even selection on samples, could be helpful as visual comparison. The lack of detail makes it difficult to assess the practical advantages of the proposed method, particularly in scenarios with high compression rates.
3. The generation FIDs are a bit high in Table 2 (though it could be due to the computation budget and could be a fair comparison with the same number of iterations). The high FID scores suggest that the generated samples may not fully capture the diversity and complexity of the training data distribution, which could limit the practical applicability of the method for high-fidelity image generation tasks.
4. A few related works [1, 2] that might be missing in the paper.

### Questions
How is the baseline VAE (GAN-based autoencoder) designed and scaled up in the paper? Are they all re-trained to match the setting of eps-VAE? Is the number of channels 8 for Figure 4 and 5?

In particular, is there any quantitative results / visual samples correspond to downsampling-factor-8 and 4-channels setting for the baseline VAE, which is the default setting used in LDM / Stable Diffusion (for images at resolution 256 or 512)?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes ε-VAE as a new tokenizer to replace traditional VAE, specifically implementing a diffusion model as the decoder process instead of the original VAE decoder.

Advantages:
1. The idea is straightforward and appears promising
2. The paper is well-written and easy to understand, I can follow all equations in the paper. There is no innovation in the mathematical aspect.

Disadvantages:
1. The novelty is limited
2. The quantitative metrics are subpar
3. The reconstruction visual quality is inadequate

According to LLamaGen [1], on the 256×256 ImageNet 50k validation set, SD-VAE achieves rFID 0.820 and SDXL-VAE obtains an rFID of 0.68. Similar results can be found in [5]. However, this paper's performance is significantly lower than the original VAE results.

Based on my reconstruction experience, after carefully examining the figures presented in the paper, the visual quality of the reconstructions is not satisfactory.
Please show some results that can reconstruct face details and text details.

I have some suggestions,
1. Test the method on COCO dataset
2. Further improve current results, as there is still a considerable gap to SOTA performance on ImageNet
3. Evaluate reconstruction performance on video data

References:
[1] LLamaGen
[2] VAR
[3] MAR
[4] SDXL
[5] https://github.com/LTH14/mar/issues/3
[6] MagVit2

### Strengths
Advantages:
1. The idea is straightforward and appears promising
2. The paper is well-written and easy to understand, I can follow all equations in the paper. There is no innovation in the mathematical aspect.

### Weaknesses
Disadvantages:
1. The novelty is limited
2. The quantitative metrics are subpar
3. The reconstruction visual quality is inadequate

According to LLamaGen [1], on the 256×256 ImageNet 50k validation set, SD-VAE achieves rFID 0.820 and SDXL-VAE obtains an rFID of 0.68. Similar results can be found in [5]. However, this paper's performance is significantly lower than the original VAE results.

Based on my reconstruction experience, after carefully examining the figures presented in the paper, the visual quality of the reconstructions is not satisfactory.
Please show some results that can reconstruct face details and text details.

### Questions
see above

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a new generative model, named $\epsilon$-VAE, combining together techniques from Variational Autoencoders (VAEs), Generative Adversarial Networks (GANs) and Diffusion Models (DM), to accomplish both image reconstruction tasks (super-resolution), and generation. In particular, the architecture of $\epsilon$-VAE consists of a decoder in the style of a Variational Encoder, mapping the input image to its latent representation, and a conditional DM-based decoder, which maps the latent representation back to the image domain. The experimental section is mostly well-done, and it clearly shows that -VAE beats modern VAE model in basically every analyzed setup.

### Strengths
- **Originality**: The idea presented in the paper is original and, in my opinion, non trivial.
- **Quality**: Despite a few observations, the overall quality of the paper is great.
- **Clarity**: The paper is well-written and the results clearly presented. 
- **Significance**: The results from the presented experiments prove that the idea is appealing to the scientific community. While being relatively simple, the idea presented in this work is worth to be published.

### Weaknesses
There are a few points that needs to be clarified for the paper to be accepted.

- First of all, the notation is confusing. The authors use the terms “tokenization” and “pre-processing” to indicate what is simply a CNN-based encoder, in the style of any image autoencoder network. While this is in general not a big issue, I suggest to clarify this aspect more clearly at the beginning of the paper, since the term “tokenization” is usually associated with language models, while “encoder” is more common in image processing field.
- Secondly, I do not understand why the name “$\epsilon$-VAE” contains a clear reference to Variational Autoencoders, while after the modifications provided by the authors the resulting model is far from being a VAE. For example, the primary difference between VAE and any other Autoencoder is the training loss (i.e. the ELBO objective) and the presence of an approximate probability distribution of the latent space, in the form of q(z | x). None of these two properties appear to be present in the proposed model, which looks closer to a Diffusion Model conditioned on latent representation obtain through a convolutional encoder, than to a VAE. I understand that this is close to what happens in VQ-VAE and VQ-GAN [1], but in this case the absence of an explicit fit of the prior distribution during training is justified by the assumption of a discrete latent space, which avoids the gradient to be backpropagated through the network, while in your setup the latent variable is continuous.
- A consequence of the previous point is that in the experimental section you compared your result with a moden VAE model (from Esser et al, 2021) [1]. While the compared model is close to be state-of-the-art in the field of Variational Autoencoder, its performance as a generative model are easily surpassed by state-of-the-art Diffusion Models. Since I believe $\epsilon$-VAE is a Diffusion Model, it would be interesting to see results compared against a Diffusion Model, instead of against a Variational Autoencoder. This observation is also supported by Figure 2 (left), where ADM by itself clearly reaches lower rFID than the VAE model to which you compared with. Thus, I suggest the authors to compare $\epsilon$-VAE with ADM in the experiments.
- Lastly, for the big part of the paper, the authors did not declare the number of diffusion steps employed by $\epsilon$-VAE. Based on the Iterative and Stochastic Decoding paragraph at the end of the paper, I infer that you maybe used either 1 or 3 diffusion steps. While a low number of steps is of common use in Diffusion Models applied to solve Image Reconstruction tasks, one could argue that a single-step Diffusion Model is not really a Diffusion Model, but a simple application to a conditional UNet denoiser.

**Minor Comments.**

1. In line 32, “Tokenization is a essential in both”. Remove the “a”.
2. In line 105, I believe that in the definition of sigma_t, it should be an “alpha” instead of an “a”.
3. In the “Impact of proposal” section, the notation (1), (2), … is confusing because it looks like it refers to equations. I suggest to instead use some variants such as (P1), (P2), …, to indicate “Proposal 1”, “Proposal 2”, ….

### Questions
I included a few questions on the "Weakness" section.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces $\epsilon$-VAE, which replaces the decoder with a UNet diffusion model. This work focuses on tokenization for latent diffusion models and substitutes the deterministic decoder with a diffusion process, aiming to achieve higher compression rates and improved reconstruction quality, thereby enhancing the generation quality of downstream generative models. Experiments are conducted on ImageNet using evaluation metrics such as FID, rFID, IS, Precision, and Recall.

### Strengths
The proposed $\textit{denoising as decoding}$ is interesting

Performance significantly exceeds the VAE

### Weaknesses
1. The approach involves using a diffusion model instead of a decoder. However, vanilla diffusion operates in latent space, resulting in generated latent code that do not match the image size. Without an additional decoder, how can images of the correct size be generated?

2. A major limitation of the vanilla diffusion model is its multi-step iteration, which results in longer inference times. Many existing methods have addressed this issue by reducing the number of inference steps (e.g., LCM, SD-Turbo, SwiftBrush). The decoder of the $\epsilon$-VAE also requires multiple inference steps, limiting its scalability to more general tasks (such as text-to-image tasks and downstream applications) and increasing inference time. Therefore, a comparison between a one-step $\epsilon$-VAE and a traditional VAE should be provided.

SwiftBrush: One-Step Text-to-Image Diffusion Model with Variational Score Distillation (CVPR'24)

SD-Turbo: Adversarial Diffusion Distillation

LCM: Latent Consistency Models: Synthesizing High-Resolution Images with Few-Step Inference

### Questions
The $\epsilon$-VAE transforms the standard decoding process of a VAE into an iterative denoising task. However, this iterative process introduces additional inference time, which is not reported in the paper.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes using a diffusion-based decoder for visual tokenization, replacing traditional single-step decoding with iterative refinement. The authors compare U-Net and DiT diffusion architectures, finding U-Net to be superior. Compared to VQGAN, this approach also achieves better reconstruction (rFID) across all scales. Finally, the authors assess image generation quality and perform an ablation study.

### Strengths
- Uses a flow-based model, which could serve as a major upgrade over the previous diffusion-based decoder.
- Adds adversarial training to the pipeline, potentially retaining the benefits of GANs compared to VQGAN, and allowing for a reduction in sampling steps.
- Includes both U-Net and DiT architectures with comparisons across multiple model sizes, making this an extensive experiment.
- It’s beneficial to include image generation quality, though this aspect might not be the paper’s main focus; it’s expected that image generation quality should align with image reconstruction quality.

### Weaknesses
 - The authors did not use DiT with a patch size of 2, which is considered optimal in the DiT paper and is the most widely used; however, the computational limitations are understandable.
- Image reconstruction evaluation relies heavily on a single metric, rFID (across both Tables 1 and 2). While it’s reasonable for authors to report preferred metrics, it would strengthen the paper to include additional commonly used metrics, such as PSNR, SSIM, and LPIPS, to provide a more comprehensive assessment. The exclusive use of rFID makes it difficult to assess the pixel-level reconstruction quality and compare with other methods that report these standard metrics.
- The paper lacks mention and discussion of previous diffusion-based autoencoders like DiffusionAE (https://diff-ae.github.io/) or DiVAE (https://arxiv.org/abs/2206.00386).
- Despite testing a new flow-based model and architecture, the conclusions on diffusion-based decoding do not significantly expand on those from previous studies. The paper does not clearly articulate how the proposed method advances the understanding of diffusion-based decoders beyond what is already known.
- Diffusion-based decoders have been shown to improve upon standard VQGAN-based decoders (since 2022) and have seen applications like in 4M-21  (https://4m.epfl.ch). However, the reason that it not become popular, i believe, is time-intensive both training and inference, a challenge that this paper does not seem to overcome yet.

### Questions
- What are the "new insights" you mention in the abstract? 
- "by" in line 216

### Soundness
4

### Presentation
3

### Contribution
1

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper focuses on improving the VAE and demonstrates its effectiveness using a generation task. The authors optimize the decoder part, and the diffusion model iteratively denoises the data to recover the original. They compare two metrics, rFID and FID.

### Strengths
1. Provides some insight by exploring a new VAE decoding method.
2. Theoretical derivation makes sense and enhances the interpretability of the approach.

### Weaknesses
1. A minor point: In the abstract, you mention, "We evaluate our approach by assessing both reconstruction (rFID) and generation quality (FID)," but why is FID used to validate generation quality? I see you used IS in the experiment section instead.

2. The novelty is limited. The core innovation is only improving the VAE decoder, which offers minimal technical contribution.

3. The Introduction mentions various tokenizers, but the actual comparison seems to focus solely on VAE. What about discrete tokenizers like VQVAE and VQGAN?

4. You mention that the proposed model’s inference time is better than VAE, but also admit that "it requires more compute costs than VAE due to its U-Net design." In Section 5’s Discussion, you briefly touch on potential future optimizations. Does this imply that this limitation in your model is unsolvable?

5. You discuss VAE optimization in the context of Diffusion Models, but the inference time you’re referring to compares VAE’s reconstruction speed. In practice, the major time consumption in generation models isn’t in the VAE part. The faster inference time you mention is insignificant because the time it saves is negligible within 50 DDIM steps.

### Questions
See the weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
2
