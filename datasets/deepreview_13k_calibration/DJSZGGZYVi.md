# Representation Alignment for Generation: Training Diffusion Transformers Is Easier Than You Think

- Decision: Accept
- Avg Score: 9.00
- Scores: 10, 8, 10, 8, 8, 10

## Abstract
Recent studies have shown that the denoising process in (generative) diffusion models can induce meaningful (discriminative) representations inside the model, though the quality of these representations still lags behind those learned through recent self-supervised learning methods. We argue that one main bottleneck in training large-scale diffusion models \emph{for generation} lies in effectively learning these representations. Moreover, training can be made easier by incorporating high-quality external visual representations, rather than relying solely on the diffusion models to learn them independently. We study this by introducing a straightforward regularization called \emph{REPresentation Alignment (\sname)}, which aligns the projections of noisy input hidden states in denoising networks with clean image representations obtained from external, pretrained visual encoders. The results are striking: our simple strategy yields significant improvements in both training efficiency and generation quality when applied to popular diffusion and flow-based transformers, such as DiTs and SiTs.
For instance, our method can speed up SiT training by over 17.5$\times$, matching the performance (without classifier-free guidance) of a SiT-XL model trained for 7M steps in less than 400K steps. In terms of final generation quality, our approach achieves state-of-the-art results of FID=\bestfidinterval using classifier-free guidance with the guidance interval.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The paper presents a novel argument that a primary bottleneck in training large-scale diffusion models for generation lies in learning effective representations. The authors suggest that training can be significantly simplified when the model is supported by strong external visual representations. To address this, they introduce a straightforward regularization technique called REPresentation Alignment (REPA), which aligns the projections of noisy input hidden states in denoising networks with clean image representations obtained from pretrained external visual encoders, such as DINOv2. Comprehensive experiments validate this perspective, reinforcing the paper’s innovative viewpoint.

### Strengths
1. The paper’s key finding—that self-supervised representations, like those from DINOv2, can serve as a teacher to distill base features in a diffusion model—is both novel and insightful. By using these high-quality representations, the diffusion model can more quickly learn a robust semantic foundation, allowing deeper layers to focus on higher-frequency details. This approach is innovative and inspiring.
2. The experimental setup is thorough, covering various aspects such as types of self-supervised encoders, encoder scalability, the number and location of layers used for regularization, and different alignment objectives. These comprehensive experiments add credibility to the proposed method.

### Weaknesses
1. High-resolution results (e.g., 512x512) are needed to support and further validate findings.
2. FID may be unreliable here, as it relies on the Inception network, which tends to lose significant spatial information and focusing on class information. I recommend re-evaluating using DINO-FID to obtain a more accurate measure. I would consider raising the score to 10 if state-of-the-art fid is demonstrated at resolution 512x512 and DINO-FID at 256x256. For DINO-FID, it’s necessary to pass the ImageNet training set through DINOv2 to store features for dino-FID calculation, which might be challenging to implement. If resources are limited, DINO-FID can be computed at 256x256 resolution, while 512x512 results can use the Inception FID npz provided by ADM.
3. It would be beneficial to include visualizations of the features before and after alignment. Although differences can already be observed in the generated images, since the core concept is feature alignment, visualizing the impact directly at the feature level would strengthen the argument and provide deeper insights.
4. I recommend exploring the effects of different diffusion objectives. For example, the intermediate features of an epsilon-prediction diffusion model might differ from those of a v-prediction or x0-prediction model. An analysis of these variations could provide valuable insights into the interaction between diffusion objectives and feature alignment.
5. The use of class conditions may not fully represent the entire generative domain, particularly in areas like text-to-image and text-to-video generation. This raises concerns about the generalization of the claim that feature alignment is universally important for generative tasks. It would be beneficial to clarify or qualify this claim in light of these broader application areas. In scenarios that already include rich semantic prompts, such as text-to-video generation, would the proposed method still be effective? DINO’s semantic extraction during training may differ from the semantics derived by an LLM when captioning or re-captioning. It would be helpful to include experiments that use detailed textual descriptions as conditions to evaluate the method’s performance under these circumstances.

### Questions
1. I recommend releasing the training and evaluation codes to support future research efforts, as feature representation plays a crucial role in diffusion models.
2. You mention that directly fine-tuning a DINOv2 model within a diffusion framework fails due to the noisy input. This raises some questions, as fine-tuning is generally quite robust and should be capable of handling noise. Additionally, have you considered training a diffusion model from scratch while incorporating a partial DINOv2-based loss (similar to a LPIPS loss) alongside the denoising loss? This approach might aid in feature preservation during denoising.
3. How do you handle cases where the spatial dimensions (height × width) differ between DINOv2 and DIT? Would using cross-attention mechanisms be a feasible method for aligning features in such cases? This might offer a flexible solution to manage discrepancies in spatial resolution between the models.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents REPresentation Alignment (REPA), a regularization technique designed to enhance the efficiency and quality of training in diffusion models. By aligning the noisy input states within denoising networks with clean image representations taken from pretrained visual encoders, REPA helps diffusion models learn better internal representations. The approach significantly improves training efficiency—such as a 17.5× speed-up for SiT models—and boosts generation quality, achieving a FID score of 1.80 on ImageNet with guidance. The authors emphasize the importance of aligning diffusion model representations with powerful self-supervised representations to make training easier and more effective.

### Strengths
- I like the idea of combining diffusion model training and representation learning. The authors highlight the importance of aligning diffusion model representations with powerful self-supervised representations to make training easier and more effective.

- The writing in the paper is clean and easy to follow. The authors start with their observations from the empirical study on pretrained diffusion models, which provides the audience with enough background to understand the problem.

- The experimental section of this paper is solid. They conduct extensive ablation studies on the proposed method, including aspects such as encoder type, encoder size, alignment depth, and more.

### Weaknesses
 - My main concern with this work is that the authors focus on class-conditioned diffusion models rather than text-conditioned diffusion models. The success of diffusion heavily depends on text prompts, as better prompts lead to improved performance and faster training of the diffusion model. I am worried that representation learning may not be necessary for text-conditioned diffusion models, as the text itself already acts as a regularizer to guide the training. Additionally, the improvement in FID with classifier-free guidance (CFG) in this paper is not significant, which partially validates my concern that additional representation learning may not be needed when there is strong guidance.

- The empirical study presented in Figure 2 is based on linear probing, which is unfair to the diffusion model as it is trained with reconstruction objective. In this context, I suspect that the performance gap for the diffusion model would be smaller on tasks like semantic segmentation.

### Questions
I believe this is a solid piece of work and an important first step toward combining representation learning and diffusion model training. My main concern is whether this approach is generalizable to text-conditioned diffusion models. Additionally, I would suggest that the authors add [a] and [b] to the literature review:

[a] Learning Disentangled Representation by Exploiting Pretrained Generative Models: A Contrastive Learning View. ICLR 2022.

[b] DisDiff: Unsupervised Disentanglement of Diffusion Probabilistic Models. NeurIPS 2023.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The paper introduces representation alignment for diffusion models, a new technique that aligns diffusion features with those of a pretrained foundation model during training. The method is motivated by the observation that the features of pretrained diffusion models inherently align with the features of pretrained, diffusion-based transformer models. Inspired by this, the authors conducted a thorough analysis of the correlation between features at different layers of a foundation model and a diffusion model, finding that certain layers exhibited higher feature correlation. To enhance this alignment, the authors introduced a representation alignment loss, which results in a performance boost. An extensive study was conducted with various foundation models and across different diffusion model layers to identify the most suitable model and layer for enforcing similarity. The authors achieved 17.5x faster convergence on DiT when trained with RePA.

### Strengths
1. The paper is well-motivated. The introduction section clearly states the logic and reasoning behind why and how the features of foundation models can be leveraged to improve the convergence of a diffusion model.
2. The authors analyze different visual foundation models for representation learning and demonstrate that RePA is invariant to the choice of foundation model, with almost all visual foundation models enhancing generation performance and convergence.
3. The authors also study the correlation between generation performance and discriminative classification performance using validation accuracy on ImageNet, showing that both exhibit a linear correlation. A model trained to provide better representation capabilities automatically achieves better generation quality as well.
4. These insights are extremely valuable and novel, representing a significant step forward in the field.

### Weaknesses
1. The main claims of the paper is valid in the cases where classifier free guidance is not applied. Could the authors provide an analysis of the benefit of RePA in the presence of classifier free guidance. Specifically it would be great to see the results in Figure 1 with classifier free guidance included
2. How well does RePA work when there is already an alignment with text like cross attention in text-to-image models. Will RePA cause a conflict in representation alignment between CLIP/T5 and Dinov2 representations and reduce performance? If time permits I would request the authors to add an analysis in this aspect. This could be a simple experiment like finetuning the existing model an small text to image datasets like CUB-200[3]. If not a detailed explanation of why/why not this may work would suffice.
3. Diffusion features are generally noisy in the encoder layers and tends to become clearer in the decoder[1,2]. However in REPA we find that the best suited layer is indeed in the encoder which suggests cleaner representations in the encoder itself. Could the authors comment on why although the correlations seems better in the decoder features, the encoder layer 8 is best suited for representation alignment? An answer to Q1 in the questions section would suffice for this query.
4. There are no limitations section or future works section in the manuscript. I would advise the authors to please include these as well in an updated version. The request for these sections is for enabling the research community to further tackle problems that the authors might not have time to tackle.

### Questions
1. In Figure 3, was the analysis performed by training different networks with RePA applied at different layers or was the training process for a single layer and evaluation was performed at different layer? This aspect is not clear from the paper. Could the authors please include this clarification in the figure caption or the related section. 
2. In cross attention layers, the main learning process happens through alignment of the image space and text space . Diffusion models leveraging cross attention functions better if the  cross attention is applied at different layers. Considering a contrast of REPA for diffusion alignment. Would doing representation alignment based training leveraging different levels of features from the foundation model and the diffusion model lead to an improve in performance? Could the authors comment on this.
3. Diffusion features are generally noisy towards the start of the sampling process and becomes clearer towards the end. In Figure 2a, the authors showed that the semantic gap for cleaner features tends to be lower. However does this also suggest that a time varying repa might lead to a even better boost in performance
4. In Figure 5, the authors have shown the benefit of different visual foundation models for represenation alignment. However, there is also a correlation that the linear probing performance also follows the same trend i.e 
Dinov2> CLIP>MoCov3>DINO>MAE
Hence I'm curious if repa using a pre-trained SOTA VIT based classifier may further boost the performance. An experiment for a limited number of training iterations or a detailed explanation would suffice for this issue

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a technique called REPA, which speeds up the process of training diffusion transformers. The high-level idea of REPA is to align the diffusion model representation with the visual representation of pretrained models. Experimental results show that after using REPA, the training process of diffusion transformers can be much faster, and also achieve better performance when training for the same number of steps.

### Strengths
++ The idea flow of this paper is very clear. First, the paper presents the semantic gap between diffusion transformer features and discriminative features. Then, the paper shows that the quality of the feature representations from diffusion transformers are correlated with the generation quality. Finally, the proposed method REPA is an intuitive solution based the previous observations and arguments. Therefore, the proposed technique has clear and reasonable motivations.

++ The benefit of applying REPA in training diffusion transformers seem to be significant to me. Experimental results like the quantitative ones from Tables 2-4 show that REPA helps the models reach the same performance with fewer iterations, and further achieve better generation results when trained for the same number of steps. Therefore, this technique can be useful in training diffusion models.

++ The proposed solution is simple but effective, just to align the features from diffusion models with pretrained visual foundation models. Therefore, it is a neat yet efficient solution for speeding up diffusion models.

### Weaknesses
-- The quantitative evaluations of REPA on DiT/SiT are only conducted on $256\times 256$ images, which is kind of low-resolution with respect to the capability of state-of-the-art diffusion models. I am wondering how REPA performs in higher-resolution cases, like $512\times 512$ which is also be supported by DiT/SiT. Is it still useful in training higher-resolution diffusion transformers? I think this evaluation is crucial, otherwise the application scenario of this technique will be relatively restricted to lower-resolution.


### Questions
-- I understand that this paper mainly focuses on speeding up diffusion transformers, as mentioned in the title. However, I am curious about why the application scenario is only limited in diffusion transformers instead of more general diffusion models. Is it because pretrained visual encoders like DINOv2 are mainly in vision transformer architecture, so enforcing the alignment of the features make more sense? Or the authors think diffusion transformers are the future trend for developing diffusion models, so studying the training dynamics of diffusion transformers is more meaningful?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a simple method to improve the diffusion-based generative model’s training efficiency. It discovers the semantic difference in self-supervised vision encoders and diffusion generative models, and the motivation is to use pre-trained vision encoder representation to regularize the diffusion transformer’s feature representation. The paper is well-written, the motivation, metrics, and methods are easy to understand, and the experiments conducted on various pre-trained vision encoders under different settings demonstrate the effectiveness of the proposed method in both generation quality measured in FID and representation ability measured in linear-probing accuracy.

### Strengths
--the proposed method is simple and very easy to implement, also the idea is well-motivated by the semantic measurement metrics

--the experiments are strong and complete, and examine various vision encoders under various setups (model size, depth) and with different DiT model sizes, all show promising improvement in terms of FID

### Weaknesses
-- the paper only shows results under resolution 256x256, which is the scale most of the vision encoders are pretrained on, it raises the concern if the pre-trained low-res representation can transfer to the generative models when train on higher resolution 512, 1024, 2048 etc

-- missing dataset analysis on the pre-trained vision encoder, i.e. is the performance of the encoder pre-trained on ImageNet the same as on in-the-wild dataset?

### Questions
--The pretrained vision encoder usually also finetunes on the ImageNet dataset, how do you separate the dataset leakage effect when measuring generative models trained on the ImageNet?

-- The same techniques can be applied to the video generative model, where training cost/efficiency is more important, do you think the proposed method can be transferred to the video domain?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 6

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This paper finds that learning a good representation in diffusion transformers will speed up the training process and achieve better performance. By simply aligning diffusion transformer representations with recent self-supervised representations (DINOv2), the DDPM-based models (DiT) and flow-based models (SiT) show significant FID metric drops in early training.

### Strengths
This paper astutely captures the feature representation gap between generative and discriminative models, providing a feasible approach to enhance model representation and accelerate the training process of DiT models. The extensive analysis and observations regarding representation clarify the underlying motivation. Additionally, the experiments are detailed and validate the effectiveness of the proposed method across different settings. The presentation of Table 2 and the experiment section is very clear.

### Weaknesses
1. All the experiments in this paper are conducted under the setting of ImageNet 256x256. Although this work shows good results in this setting, it is still far from being applied to the currently popular high-resolution transformer-based text-to-image generation models, such as Flux. I would be more excited to see results and observations at higher resolutions or in text-to-image generation. If the generation is limited to the DiT/SiT class condition, its applications will be severely restricted.
2. Metrics for ImageNet generation often confuse me; the FID, sFID, IS, and other metrics frequently show differing trends. And FID does not effectively reflect actual quality differences at low values. How do you consider these metrics comprehensively to make a reasonable judgment about performance? For instance, in the last two rows of Table 2, NT-Xent outperforms in sFID, while Cos. sim. outperforms in FID and IS. And it would be beneficial to provide some experimental results to explain why you chose NT-Xent, rather than simply stating "Empirically, ..." in line 421. I would be glad to discuss this further with you in the Questions section.

### Questions
1. The experimental results indicate that the speedup for SiT training is quite significant. However, can it achieve state-of-the-art performance in the final results? MDT (ICCV'23) [1] seems to have achieved an FID of 1.79.
2. Let's discuss the gap between FID metrics and actual image performance, in Figure 6, your visualization are under classifier-free guidance with $w = 4.0$, but SiT-XL/2 with REPA achieves best FID of 1.80 under classifier-free guidance scale of $w = 1.35$. What do you think of the difference w between best visualization and best metrics, and whether this measure is unreasonable?
3. I agree with "the diffusion transformer model needs some capacity for capturing high-frequency details after learning a meaningful representation that contains good semantics.", but minimum semantic gap are at layer 20 before alignment with REPA, which is different between layer 8 after alignment with REPA  (I note this because layer 8 yields the best metrics). Could you further explain this difference?
4. To more clearly represent the process of alignment in the representation, I recommend including the definition of layers in formula (8). I suggest using $h^{[n,m]}$ to represent diffusion transformer encoder output, where $n$ is a patch index and $m$ is layer index. There is a small parenthesis error in formula (8).

[1] Gao, Shanghua, et al. "Masked diffusion transformer is a strong image synthesizer." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023.

### Soundness
4

### Presentation
3

### Contribution
3
