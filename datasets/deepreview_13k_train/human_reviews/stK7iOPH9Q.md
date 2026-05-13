# Lotus: Diffusion-based Visual Foundation Model for High-quality Dense Prediction

- Decision: Accept
- Scores: 6, 6, 6, 8, 6

## Abstract
Leveraging the visual priors of pre-trained text-to-image diffusion models offers a promising solution to enhance zero-shot generalization in dense prediction tasks.
\haodong{However, existing methods often uncritically use the original diffusion formulation, which may not be optimal due to the fundamental differences between dense prediction and image generation.}
In this paper, we provide a systemic analysis of the diffusion formulation for the dense prediction, focusing on both quality and efficiency. And we find that the original parameterization type for image generation, which learns to predict noise, is harmful for dense prediction; the multi-step noising/denoising diffusion process is also unnecessary and challenging to optimize.
Based on these insights, we introduce \textbf{Lotus}, a diffusion-based visual foundation model with a simple yet effective adaptation protocol for dense prediction.
\haodong{Specifically, Lotus is trained to directly predict annotations instead of noise, thereby avoiding harmful variance. We also reformulate the diffusion process into a single-step procedure, simplifying optimization and significantly boosting inference speed.
Additionally, we introduce a novel tuning strategy called detail preserver, which achieves more accurate and fine-grained predictions.}
\haodong{Without scaling up the training data or model capacity, Lotus achieves SoTA performance in zero-shot depth and normal estimation across various datasets. 
It also enhances efficiency, being significantly faster than most existing diffusion-based methods.}
\haodong{Lotus' superior quality and efficiency also enable a wide range of practical applications, such as joint estimation, single/multi-view 3D reconstruction, etc.}
Project page: \href{https://lotus3d.io/}{\textcolor{blue}{\fontfamily{cmtt}\selectfont{lotus3d.io}}}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors simply told us diffusion-based method is not suitable, not necessary, and even harm dense prediction quality. They form a story that they reduce the diffusion step to 1, while adding a regularization of detail preserver, and finetune from a large-scale UNet pretrained on T2I task, to achieve good dense prediction performance.

### Strengths
- The authors presented an interesting story of removing 'diffusion' from dense prediction to make things less complicated. 
- If the proposed method and claims are proved to be effective, it shows using a diffusion-based dense prediction method is overkill compared to the efficiency of a 1-step direct prediction. It can be a nice finding.

### Weaknesses
 - What is the fundamental difference between the proposed method with a model trained with UNet using latent-space? If there is no diffusion process and the model is doing x0 prediction, why it is still called diffusion method, especially when the authors proposed a discriminator version, does it just fall back to a simple UNet-based method? The authors need to clarify the necessity of the noise input, given that the discriminator version performs well without it, and other methods like Lotus-D also achieve good results using paired data and reconstruction loss. The claim that the performance gain comes from diffusion priors is vague and needs further investigation. It's unclear if the noise channels are truly necessary or if the performance is primarily due to the pre-trained model's strong feature representation.
- If the authors claim the powerful prediction quality can come from the strong prior of the pretrained model, but the currently proposed detail preserver, is just learning the reconstruction, and can be lazily learned via the skip connection within the UNet structure, it does not seem to preserve the original generator capability. The reviewer believe after longer training or large batch size training, the performance will degrade more. It is interesting that the detail preserver can enhance the detail by a large margin, given the reconstruction can be easily learned by the residual connection in each layer. The detail preserver seems to be a form of regularization, but it is not clear why it is needed if the skip connections in the UNet architecture should already be capable of preserving details. The authors need to provide more analysis on the necessity of this module.
- If the authors claim it can be served as a visual foundation model, it needs to show more capability of generalization or potentials of other tasks, either through finetuning or adaptation. The current results are limited to depth and normal estimation, and more diverse tasks should be explored to support this claim. The authors should provide more evidence of the model's generalization capabilities beyond the tasks presented.
- The qualitative results seem still not strong enough compared with other baselines, and are very close to Marigold.

### Questions
- Do we need to finetune the VAE or decoder for dense representation given the original VAE can be only trained on image data?
- How did the author evaluate the generative methods given the randomness?
- Does the conclusions from this paper also apply to other simpler vision tasks? How do the author feel about segmentation task? Also whether diffusion is just not suitable for any tasks requiring pixel-level preservation?

Overall I feel the authors proposed a good observation for dense prediction, but a couple of statements are over-claimed, like foundation model, 1-step 'diffusion' is enough, or detail preserver is necessary.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a novel method for dense prediction tasks by fine-tuning a pre-trained diffusion model. To achieve stable and consistent predictions, the method shifts the model’s prediction from epsilon to x0 (clean image) prediction, significantly reducing the variance in outputs. This transition allows for accurate single-step inference, which simplifies the process while maintaining high-quality results.

To avoid generating excessively smoothed outputs—a common issue in dense prediction with diffusion models—the approach incorporates input frame reconstruction into the training process. This addition serves to preserve finer details and structure in the output predictions, balancing accuracy with realistic visual representation.

The proposed method is evaluated in a challenging zero-shot scenario, where its performance is benchmarked against both discriminative and generative approaches. Despite being fine-tuned on limited data, the model demonstrates competitive, promising performance, highlighting its robustness and adaptability for dense prediction tasks.

### Strengths
The paper presents its motivation clearly, leading readers through a coherent explanation of the research objectives and the rationale behind the proposed method. Supported by carefully crafted figures, the narrative flows in a way that helps readers follow the progression of ideas and understand the purpose of each methodological contribution. Each figure complements the text by visually illustrating the transition from epsilon prediction to x0 prediction, the integration of input frame reconstruction, and the steps involved in single-step inference. This combination of clear motivation and visual aids effectively demonstrates how the approach stabilizes predictions and reduces variance, helping readers grasp the value and impact of the proposed method for dense prediction tasks, even in zero-shot settings with limited data.

### Weaknesses
The proposed method, while effective in its application, appears relatively simplistic and may lack substantial innovation. Both the use of  \mathbf{x}_0  prediction and few-step inference have been previously explored in the diffusion model literature, which limits the originality of these aspects. The  \mathbf{x}_0  prediction has been extensively discussed in seminal works such as “Denoising Diffusion Probabilistic Models” and Stable Diffusion. Similarly, few-step inference has been considered in studies like “UFOGen: You Forward Once Large Scale Text-to-Image Generation via Diffusion GANs” and “One-step Diffusion with Distribution Matching Distillation.” Consequently, these elements alone may not constitute a significant contribution to the field.

Furthermore, the paper’s evaluation and analysis are narrowly focused on the zero-shot scenario, which, while valuable, provides a limited perspective on the method’s potential. To fully illustrate the strengths of this approach for generative dense prediction, a broader evaluation across diverse scenarios beyond zero-shot would enhance the analysis. Expanding the experiments to include intra-dataset inference, or testing in varying contexts, such as semantic segmentation or optical flow, could highlight the model’s generalization abilities and its versatility in handling different levels of supervision.

I also acknowledge the authors’ claims regarding the model’s performance in minimal-data contexts. Exploring the scalability of the model could offer significant insights, especially given the inherent scalability of diffusion-based methods. Demonstrating the model’s performance with larger, more complex training datasets, similar to “DepthAnything,” would facilitate a deeper understanding of its robustness and computational efficiency. This could be achieved by training the model with datasets of varying sizes and evaluating the performance gains of such a diffusion-based approach. An expanded evaluation would provide a more balanced perspective, showcasing the model’s adaptability beyond minimal-data contexts and emphasizing its potential applicability in real-world, data-rich environments.

### Questions
I’m curious about the mention of “removing noise” on line 430. In the figure, the noise appears to be concatenated with the input frame—how exactly is this term removed? What value, if any, is set in its place? Does this modification affect any underlying assumptions of diffusion models?

### Soundness
2

### Presentation
4

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
This paper introduces a novel approach to dense prediction tasks in computer vision. The authors analyze existing diffusion formulations and identify that traditional noise prediction methods are suboptimal for dense prediction, leading to significant prediction errors. They propose Lotus, a diffusion-based model that directly predicts annotations instead of noise, simplifying the optimization process and enhancing inference speed. The model employs a single-step diffusion process and introduces a detail preserver mechanism to improve accuracy in detail-rich areas. Experimental results demonstrate that Lotus achieves state-of-the-art performance in zero-shot depth and normal estimation tasks, significantly outperforming existing methods while requiring minimal training data.

### Strengths
+ This paper introduces a dense prediction method that directly predicts annotations rather than using traditional noise prediction, enhancing prediction stability and enabling one-step inference.
+ The paper provides an in-depth analysis of existing diffusion models, highlighting instability issues in dense prediction and examining the relationship between prediction variance and time steps.
+ The proposed method achieves competitive performance across multiple benchmarks, rivaling state-of-the-art approaches.

### Weaknesses
- In this work, the diffusion model functions more like a single-step restoration network, employing a one-step strategy for both training and inference. It may be beneficial to explore training the diffusion model with a variable approach to the time step *t*, rather than fixing it, for example, by sampling *t* from a range during training. This could potentially lead to a more robust model that is less sensitive to the specific choice of *t*.
- For the detail-preserving component, a task switcher s is selected during each training iteration. Since predicting annotations and reconstructing images are mutually exclusive tasks, the loss function should be adjusted to reflect this "either-or" relationship more explicitly. The current approach might not fully capture the inherent competition or trade-off between these two objectives.

### Questions
What is the relationship between the proposed network and existing conditional restoration methods? Could this design be extended to other dense prediction tasks, such as segmentation?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper follows a recent trend to formulate dense per-pixel regression tasks (in particular, monocular depth and normal estimation) as conditional image generation, so as to benefit from the strong prior of (latent) denoising diffusion models. Building on Marigold [Ke et al., 2024] and its derivative GeoWizard [Fu et al., 2024], the paper proposes the following technical improvements.
1) Training the diffusion process to predict the denoised image, rather than the noise, as commonly done for image generation; Arguing that the increased variability when predicting the noise is undesirable for regression tasks.
2) Faster and less variable one-step inference, including a deterministic variant without initial random noise.
3) Additional regularisation with the image generation task to enhance the preservation of details.

### Strengths
The analysis of predicting the clean image vs. predicting the noise in conditional regression tasks is interesting. It is a relevant observation that, empirically, predicting the clean output directly may perform better in terms of mean prediction error. This could contribute to a better understanding of the mechanisms in diffusion models, and may potentially be interesting also for other conditional uses of those models.

The regularisation, by switching between predicting the regression target and reconstructing the input image, is plausible. While it is really a simple implementation trick with a fairly hand-wavy explanation, it might be useful for a whole range of applications that repurpose generative models for image analysis tasks.

The paper provides further evidence for the confluence of conditional generation and discriminative prediction - the evidence is thickening in the last few months that one can move to one-step prediction and even drop the random initialisation (or replace it with a constant zero-input), effectively using a pre-trained multi-step generative model as a “training scheme” or “teacher model” for a discriminative one.

### Weaknesses
The paper does not go very deep in its analysis of the difference between predicting the clean target or the noise. It is a plausible and important message that clean image prediction yields lower errors for certain conditional regression tasks. But the slightly higher mean error of noise prediction could, to some degree, also be an inevitable price to pay for the benefit of proper probabilistic modelling. Is the larger variability really just an algorithmic artefact, or is it perhaps a correct rendition of the underlying predictive uncertainty in the ill-posed task? The findings in the paper are an interesting starting point, but a deeper and more neutral analysis would be helpful.

The findings regarding one-step inference, as well as deterministic prediction without initial noise, are credible and important for the further development of the field. That being said, they should be discussed in the context of other recent literature, in particular [Garcia et al., 2024]. Yes, that paper only came out as a preprint 2 weeks before the ICLR deadline. I am aware that it does not qualify as "prior art", and I am not suggesting that there would be any novelty issue. But I would opine that, in this specific case, the work of Garcia et al. should be discussed and not ignored altogether. The findings - one-step training and inference, zero-noise initialisation - are very similar to one of the present paper's main messages. To maximally benefit the research community it will be important to paint a complete picture. Importantly, Garcia et al. show that these improvements are equally possible with the standard formulation (with noise prediction), after fixing a small but impactful bug in the DDIM scheduler of the most popular implementation (HuggingFace Diffusers). Again: I applaud the authors of the present paper for independently confirming that 1-step and deterministic inference are possible based on a pre-trained diffusion model. Still, since [Garcia et al.] is in some sense a bugfix and shows that these improvements apply to pretty much all of the conditional diffusion schemes of the past year if it were not for an incorrect implementation of the scheduler, I really think the authors should relate, compare and discuss that work in the final version of the paper.
- [Garcia et al., 2024] Garcia, GM, Abou Zeid, K, Schmidt, C, de Geus, D, Hermans, A, Leibe, B (2024). Fine-tuning image-conditional diffusion models is easier than you think. arXiv:2409.11355
(for the record: I am not an author of it)

My main technical criticism, where I really hope the authors could provide some insight during the discussion, comes from the ablation study in Table 3. According to that table, the “direct adaptation” of the diffusion model works a lot worse (2-3 times higher AbsRel), and both x0-prediction and single-timestep inference are needed to reach good performance. But the baselines Marigold and GeoWizard both reach comparable performance (NYU ~5.5, KITTI ~11, ETH3D ~6.5, ScanNet ~6.5) without those modifications, just doing “direct adaptation”. Why is the Lotus version of “direct adaptation” so much worse than prior art, and would the modifications have the same impact if one started from one of the competitors that already achieves low errors with direct adaptation?

I also find the "league table mentality" in the experiments (which the paper shares with many recent ones) really irritating. I would urge the authors to take a more objective, scientific stance and interpret the experimental results in a sensible and candid manner instead of desperately looking for a “win”. My interpretation of the bottom 4 lines in Table 1 is not “Lotus-G is the best”, but rather “all methods based on Stable Diffusion have comparable performance”. And it is totally ok to say that - your method is still fast, elegant and efficient in terms of training data and brings interesting insights, there is no need to over-interpret differences of mostly <0.5 percent points (mischievously, one could say that the only significant differences are on KITTI, where Lotus does not win - but then again that dataset is problematic anyway and should not be taken too serious).

The language and formulations are sometimes slightly imprecise or awkward, perhaps this can still be improved. Nothing serious that would seriously impair understanding, but still. Random examples:
- “first, their is a pair of autoencoders E(.), D(.)”. I would argue that there is only a single auto-encoder: encoder and decoder parts together form one auto-encoder, not a pair.
- “the type of parameterization is a vital configuration”. What exactly does this mean? The type of parametrisation may be important, or the configuration of the diffusion loop may be important, but something seems to be redundant in this sentence.

(there are more such small language and style issues, please check)

### Questions
Most important for the rebuttal: please clarify the performance gap of "direct adaptation" in Table 3 compared to other recent conditional diffusion approaches. Why do they almost match your best performance despite not using x0-prediction and single-step inference? Or, conversely, why does Lotus not perform decently without those extensions? The answer to this question is likely to significantly influence my final rating (either way).

Why did you drop DIODE from the test datasets? I am aware that it has certain issues, but since many papers (e.g., Marigold, GeoWizard, BetterDepth, etc.) show DIODE results in addition to exactly the datasets used in the paper, it would be better to also include it, for completeness. Once more, it is not a problem if, for once, you wouldn't get the bold numbers.

Similarly, why not also include DIODE and OASIS for normals, given that it does not require any training effort and makes the comparisons more complete? Also, some numbers in Table 2 differ from those I have seen floating around (although for some methods, e.g. Marigold, there do not seem to be author-approved or peer-reviewed numbers available at the time of writing). I would recommend to double-check the literature and available code bases for the rebuttal, and again for a possible final submission, to avoid swamping the literature with preliminary and potentially contradictory numbers.

### Soundness
2

### Presentation
2

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
This paper introduces a new way of using pre-trained text-to-image diffusion model for dense prediction tasks, including monocular depth estimation and surface normal estimation. Different from existing methods that use the pre-trained diffusion model without considering the dense prediction tasks, authors present several meaningful modifications. First, the parameterization type is changed in a way of predicting original image or annotation ($x_o$) instead of estimating noise. Second, the number of time-steps is reduced (even to one). Third, to enhance the capability of dealing with image details, authors utilize a task switcher that enables the proposed denoiser to generate annotation or reconstruct an input image.

### Strengths
1) The paper was written clearly and is easy to understand.
2) The three modifications tailored to dense prediction tasks seem to be effective.

### Weaknesses
1) The two tasks (depth and surface normal estimation) presented in this paper are rather insufficient. It would be better to show the possibility of using this framework in other tasks such as segmentation and detection. The current evaluation limits the generalizability of the proposed method, as it is unclear whether the observed performance gains are specific to these two tasks or if they can be extended to other dense prediction problems. For example, tasks like semantic or instance segmentation, which involve more complex reasoning about object boundaries and categories, would provide a more comprehensive evaluation of the method's capabilities.

2) More explanations are necessary for the detail preserver, as it is hard to understand why the image reconstruction task improves the details of estimated annotations. The image reconstruction and dense prediction tasks share the U-net denoiser, so it would be harmful to perform the two heterogeneous tasks within the single network due to some unexpected interferences. Specifically, the gradients from the image reconstruction task might interfere with the learning of the dense prediction task, potentially leading to suboptimal performance. This interference could manifest as a blurring of fine details or a reduction in the accuracy of the predicted annotations. This part needs to be clarified with more experiments and detailed analysis, including ablations on the contribution of the image reconstruction loss.

3) It was shown experimentally that decreasing the number of denoising steps is more effective in the dense prediction tasks, but no theoretic analysis is given. For instance, what attributes of dense prediction tasks make it possible to reduce the number of denoising steps, unlike the image generation task? Also, does it work for other prediction tasks such as segmentation and detection? The paper lacks a discussion on why a single-step approach is sufficient for dense prediction, while image generation typically requires multiple steps. It is crucial to understand the underlying reasons for this difference, such as the nature of the information being processed or the complexity of the task itself. Furthermore, it is not clear if this single-step approach would generalize to other dense prediction tasks, or if it is specific to the tasks presented in the paper.

### Questions
Refer to the comments in the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
