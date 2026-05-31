## Human Reviewer 1

### Summary
The paper investigated flow-matching models for vector-quantized image generation. It pointed out the strengths and weaknesses of existing approaches: continuous flow models preserved geometric information but could not exploit categorical learning signals, while discrete models aligned with the quantized structure and allowed temperature-scaling control but failed to understand geometry. It then proposed Purrception, a variational flow-matching technique for vector-quantized image generation that combined the advantages of continuous and discrete flow models. Purrception learned categorical posteriors over codebook indices, which could be used for computing velocity fields in the continuous embedding space. Experiments showed that Purrception outperformed both continuous and discrete flow-matching baselines in both convergence speed and image generation quality on the ImageNet-1k 256 x 256 dataset.

### Strengths
- The paper discussed the strengths and weaknesses of existing flow-matching approaches for vector-quantized image generation. It then proposed to employ a variational flow-matching technique to combine the advantages of mentioned approaches.
- The paper is technically sound.
- Experiments showed that Purrception outperformed both continuous and discrete flow-matching baselines in both convergence speed and image generation quality on the ImageNet-1k 256 x 256 dataset.

### Weaknesses
- The middle side of Equation (13) seems to be incorrect. 
- Section 4.1: Missing information on the averge NFE and the used temperature (I guess it is 0.9 based on Table 1).
- Section 4.2: From my understanding, this experiment only varies the temperature at inference while keeping the training temperature (possibly 0.9) unchanged.
  + As expected, using the inference temperature similar to the training one (the straight-forward configuration) provides the best performance. Deviating the inference temperature from the training one causes performance degradation, particularly in color saturation. Hence, the experiment cannot prove the benefits of the temperature-scaling control
  + A more reasonable experiment is to use the same temperature for training & inference, and compare models trained w/ different temperatures
  + There is no evidence showing that the temperature affects image diversity
- The results reported in Table 1 are far from state-of-the-art for Class-conditional generation on ImageNet-1k 256 x 256. The state-of-the-art ones, e.g., REPA, have FID less than 2. The reported result is only strong for vector-quantized image generation using standard DiT backbones. The authors should correct their claim.
- Writting issues:
  + Equation 12: $\pi$ was used before being defined
  + L265: The text should be in the same paragraph with the previous one
  + Figure 5: Should add the temperature lable for each column

### Questions
- The middle side of Equation (13) seems to be incorrect. 
- Section 4.1: Missing information on the averge NFE and the used temperature (I guess it is 0.9 based on Table 1).
- Section 4.2: From my understanding, this experiment only varies the temperature at inference while keeping the training temperature (possibly 0.9) unchanged.
  + As expected, using the inference temperature similar to the training one (the straight-forward configuration) provides the best performance. Deviating the inference temperature from the training one causes performance degradation, particularly in color saturation. Hence, the experiment cannot prove the benefits of the temperature-scaling control
  + A more reasonable experiment is to use the same temperature for training & inference, and compare models trained w/ different temperatures
  + There is no evidence showing that the temperature affects image diversity

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
4

### Confidence
2

---

## Human Reviewer 2

### Summary
This paper proposes variational flow matching to train flow matching with discrete code from vq-vae. By jointly combining discrete and continuous, it shows that flow matching achieves better convergence than purely continuous or discrete.

### Strengths
1. The paper shows that under same discrete VQ-VAE, it outperforms the discrete flow matching training or the continuous flow matching training. The idea of uncertainty in sampling is quite interesting.

2. The paper writing is easy to follow and clear.

### Weaknesses
1. The motivation is not well-convincing to me. It is not clear why receiving categorical signal is better for continuous flow matching. What is the geometry structure in continuous here ?

2. The theory about VFM seems to be out of place for me. To my understanding, this method is based on VFM framework but instead of inputing the codebook index and let the flow matching learn internal codebook embedding, they utilize the codebook embedding from vq-vae to create soft embedding $z_1$ and input continuous signal. This leads to limited novelty.

3. The model underperforms with DiT using continuous VAE. Furthermore, this technique heavily depends on a good VQ-VAE which is limited the model performance. It would be better to choose other discrete VQ-VAE, which has better rFID and some generative model training on that achieves very good FID like [1,2] to see how good the proposed technique can reached given different VQ-VAE. 

[1]: An Image is Worth 32 Tokens for Reconstruction and Generation
[2]: Autoregressive Model Beats Diffusion: Llama for Scalable Image Generation

### Questions
Please see the weakness above

### Soundness
1

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
5

---

## Human Reviewer 3

### Summary
This paper introduces Purrception to address a dual nature of VQ-latents, which the authors argue that existing flow-based models make a poor trade-off: Continuous Flow Matching (CFM) respects the continuous geometry but ignores the discrete categorical structure, while Discrete Flow Matching (DFM) models the indices but discards the geometry.

Purrception proposes a hybrid solution by adapting Variational Flow Matching (VFM). The model learns a categorical variational posterior over the discrete codebook indices, while the actual transport velocity is computed in the continuous embedding space.

Experimental results on ImageNet-1k $256\times256$ showing that Purrception converges significantly faster (1.7x-3.5x) and achieves a better final FID score than both CFM and DFM baselines when using the same DiT backbone88.

### Strengths
1. The motivation "discrete-continuous tradeoff" is a real problem for VQ-latents, and the paper's solution directly addresses it without compromise.
1. The proposed solution is simple and elegant.
1. Exprimental results show faster convergence than other DFM and CFM baselines.

### Weaknesses
1. Purrception failed to beat LlamaGen-XL, which has similar number of parameters, with respect to FID (Purrception 4.72 vs LlamaGen-XL 3.39), as well as other baselines.
1. Purrception's encoder, decoder, and codebook are kept frozen during training, thus the entire method is fundamentally capped by the quality of the frozen vq-f8 tokenizer.
1. Missing comparision with CDCD mentioned in related work, which also "preserves the continuous-time formulation by operating on noisy embeddings while training with cross-entropy".
1. Table 1 does not include a CFM baseline. The paper only argues the converge curve "strongly suggests" Purrception would surpass CFM, but this is not convicing enough.
1. Missing visual comparison with baselines.

### Questions
1. As shown in Figure 5, the temperature does not affect the generated image too much. How is temperature useful in real application? And any tests on DFM baseline?
1. Is z-loss just a specific patch that masks a deeper problem with scaling Purrception?
1. Any reason why adapting VFM to a fixed, pretrained codebook is novel compared to the CDCD framework?
1. Any evident that the final FID of 4.72 is not a property of Purrception, but just an inherent limitation of the vq-f8 latent space itself?
1. Did you test how Purrception performs with any other VQ-VAE tokenizers?

### Soundness
2

### Presentation
3

### Contribution
3

### Rating
2

### Confidence
2

---

## Human Reviewer 4

### Summary
The authors propose a latent variational flow matching approach, Purrception, for vector quantized generative models. The motivation for the approach is to propose a hybrid between discrete and continuous latent flows for the latent generative models. They exploit the variational formulation of the marginal vector field and propose to model the discrete latent tokens as a categorical distribution (probabilities) from the continuous latent embeddings. With the experiments on the ImageNet-256 dataset, they show training efficiency over discrete and continuous latent generative models and improved final accuracy over discrete latent generative models.

### Strengths
The idea of a continuous flow path and categorical token prediction combined under the variational flow matching framework is interesting. The application to VQ-VAEs does show improvement in generative performance compared to latent discrete flow-based approaches.

### Weaknesses
Major:

Important baseline missing - The main improvement compared to baselines is shown in the training efficiency. However, a comparison to the key baseline latent generative model SiT (Ma et al. 2024) is missing. I would request the authors to add this to their training efficiency analysis to improve thoroughness.

Other:

The model doesn't reach competitive FID vs continuous models. This is not a major weakness, as it is known (empirically) that continuous latent models tend to perform better than the discrete ones in image generation. However, I would request the authors to add a discussion of why a 750M Purrception (discrete) will be more useful than a 675M DiT (continuous) model.

### Questions
In line 294, what is e^{x_i}?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
3