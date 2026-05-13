# Efficient Scaling of Diffusion Transformers for Text-to-Image Generation

- Decision: Reject
- Scores: 6, 6, 3

## Abstract
We empirically study the scaling properties of various Diffusion Transformers (DiTs) for text-to-image generation by performing extensive and rigorous ablations, including training scaled DiTs ranging from 0.3B upto 8B parameters on datasets up to 600M images.  We find that U-ViT, a pure self-attention based DiT model provides a simpler design and scales more effectively in comparison with cross-attention based DiT variants, which allows straightforward expansion for extra conditions and other modalities. We identify a 2.3B U-ViT model can get better performance than SDXL UNet and other DiT variants in controlled setting. On the data scaling side, we investigate how increasing dataset size and enhanced long caption improve the text-image alignment performance and the learning efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper conducts extensive experiments to analyze properties of different diffusion transformer variants, providing some valuable practical findings.

### Strengths
Extensive experiments of models with different architectures, different numbers of parameters and different dataset settings are conducted.
Given the fact that transformer-based diffusion models are important and popular in both image and video generations. 
Practical findings from this paper could contribute to the community and help other researchers in future model architecture design and model training.

### Weaknesses
Although the paper provides some valuable experience and findings, it lacks in-depth analysis. 
I appreciate the author's efforts in conducting comprehensive experiments and offering the practical findings, but only performing ablation studies based on existing model designs might be a weakness of a research paper.

In experiments, some models are not trained with the same number of steps. As a result, we can compare their performance at the early stages of training, but whether the comparison will remain the same after fully convergence is actually uncertain.

Evaluating inpainting task with TIFA and ImageReward may not be appropriate.

Only some simple qualitative results are presented for edge-to-image generation in section 5.2. More quantitive comparison with existing, related methods are suggested.

### Questions
Is it possible that the performance gap between fine-tuning/freezing text encoders is partially because of the incapability of the chosen text encoder? In other words, if one use a much stronger text encoder, will the performance gap become smaller?

What is the reason of many models in some figures are trained with different steps, even when they have the same architecture design?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper conducted extensive experiments on the scaling properties of various diffusion transformers for text-to-image generation. From model scaling perspective, it discovered that a pure self-attention based variant called U-ViT scales more effectively than other variants including PixArt-$\alpha$ and LargeDiT. It also observed that the self-attention nature allows U-ViT models to take extra conditions and other modalities in a straightforward manner. From data scaling perspective, it observed that U-ViT models have better scalability given a larger training data size.

### Strengths
- This paper conducted extensive experiments to examine the model scaling properties of different kinds of models, including UNet based ones like SD2 and SDXL, and transformer based ones like UViT, LargeDiT, and PixArt-$\alpha$.
- This paper investigated many scaling perspectives, including model size scaling, data size scaling, caption scaling, token number scaling, and so on.
- This paper delivered a message that UViT models have better scaling properties, which can provide a reference for future research.

### Weaknesses
 - Despite the extensive study, there seem no novel technical contributions within this paper.
- The analysis regarding why long caption enhancement and dataset scaling help to improve the text-image alignment performance seems not thorough enough.
- In Figure 4 left, why does U-ViT-h2560-d42-n16 perform worse than U-ViT-h2048-d42-n16? The performance degradation with increased model size is concerning and requires further investigation into potential overfitting or optimization issues.
- In section 4.2, the experiments on fine-tuning text encoders are carried to SDXL, PixArt-$α$, and LargeDiT. Why not also study U-ViT models? Although there might not be significant improvement since transformer blocks in U-ViT **may** be implicitly considered as part of the text encoder which is being fine-tuned, conducting the study of U-ViT models does no harm, and can further validate the correctness of the previous reason. The lack of this experiment leaves a gap in the analysis of text encoder fine-tuning across all model architectures.
- In section 6.1 about caption scaling, which model was used to compare LensArt and LensArt-Long-50%? Why not conduct a more thorough ablation with all variants of UNet based models and transformer based models, like in section 6.2? The absence of a consistent experimental setup across different scaling experiments makes it difficult to draw definitive conclusions about the impact of caption length.
- Since the models studied in sections 6.1 and 6.2 are not the same, the analysis in section 6.3 about “information density” seems not that convincing. For example, since in figure 13, the LensArt Long Caption consistently outperforms SSTK in terms of “the percentage of captions with matched TIFA element phrases in each TIFA element type”, can we expect that using the same model, training with LensArt Long Caption can lead to better performance improvement than SSTK? The analysis lacks a direct comparison using the same model architecture, which makes the conclusions about information density less robust.

### Questions
- In Figure 4 left, why does U-ViT-h2560-d42-n16 perform worse than U-ViT-h2048-d42-n16?
- In section 4.2, the experiments on fine-tuning text encoders are carried to SDXL, PixArt-$\alpha$, and LargeDiT. Why not also study U-ViT models? Although there might not be significant improvement since transformer blocks in U-ViT **may** be implicitly considered as part of the text encoder which is being fine-tuned, conducting the study of U-ViT models does no harm, and can further validate the correctness of the previous reason.
- In section 6.1 about caption scaling, which model was used to compare LensArt and LensArt-Long-50%? Why not conduct a more thorough ablation with all variants of UNet based models and transformer based models, like in section 6.2?
- Since the models studied in sections 6.1 and 6.2 are not the same, the analysis in section 6.3 about “information density” seems not that convincing. For example, since in figure 13, the LensArt Long Caption consistently outperforms SSTK in terms of “the percentage of captions with matched TIFA element phrases in each TIFA element type”, can we expect that using the same model, training with LensArt Long Caption can lead to better performance improvement than SSTK?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper study the scaling properties of various Diffusion Transformers (DiTs) for text-to-image generation, including training scaled DiTs ranging from 0.3B upto 8B parameters on datasets up to 600M images.

### Strengths
The research toppic is popular

The paper is well-written

### Weaknesses
There is not much to take in this paper.  The paper seems to be incomplet:
1) important metrics like FID and IS are not used in the paper
2) although the authors study the scalling of DITs, they didn't privide a stonger version of DIT. Hence, they didn't demenstrate the reliablity of their paper.
3) Conclusions from the paper  like:'Finetuning text encoder improves the convergence speed for UNet' are not important. Because finetuning usually improves the performance..
4) what's more, contribution from the paper:'We examined why long caption enhancement and dataset scaling help to improve the
text-image alignment performance.' seems not straitforward.  Then the authors claim that 'Thus, we conclude that captions with higher information density (i.e., not necessarily long caption length) is key to improve text-image alignment'. Similar to 3), the authors again provide useless points.

### Questions
What's the contribution of this paper?
Could the authors provide stronger models enhanced by conclusions from the paper?
Could the authors provide FID results?

### Soundness
1

### Presentation
2

### Contribution
1
