# Ensembling Diffusion Models via Adaptive Feature Aggregation

- Decision: Accept
- Scores: 8, 5, 6, 6, 5, 8, 6

## Abstract
The success of the text-guided diffusion model has inspired the development and release of numerous powerful diffusion models within the open-source community.
    These models are typically fine-tuned on various expert datasets, showcasing diverse denoising capabilities. 
    Leveraging multiple high-quality models to produce stronger generation ability is valuable, but has not been extensively studied.
    Existing methods primarily adopt parameter merging strategies to produce a new static model. 
    However, they overlook the fact that the divergent denoising capabilities of the models may dynamically change across different states, such as when experiencing different prompts, initial noises, denoising steps, and spatial locations. 
    In this paper, we propose a novel ensembling method, Adaptive Feature Aggregation (AFA), which dynamically adjusts the contributions of multiple models at the feature level according to various states (i.e., prompts, initial noises, denoising steps, and spatial locations), thereby keeping the advantages of multiple diffusion models, while suppressing their disadvantages.
    Specifically, we design a lightweight Spatial-Aware Block-Wise (SABW) feature aggregator that adaptive aggregates the block-wise intermediate features from multiple U-Net denoisers into a unified one.
    The core idea lies in dynamically producing an individual attention map for each model's features by comprehensively considering various states.
    It is worth noting that only SABW is trainable with about 50 million parameters, while other models are frozen. 
    Both the quantitative and qualitative experiments demonstrate the effectiveness of our proposed Adaptive Feature Aggregation method.
  \keywords{Image Generation \and Diffusion Models \and Model Ensembling}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Adaptive Feature Aggregation (AFA), a novel ensembling method for text-to-image diffusion models. Unlike conventional static parameter merging approaches, AFA dynamically aggregates features from multiple diffusion models using a lightweight Spatial-Aware Block-Wise (SABW) feature aggregator. The method adaptively adjusts model contributions based on various states including prompts, initial noise, denoising steps, and spatial locations. The key technical innovations lie in block-wise feature aggregation and spatial attention mechanisms, enabling effective ensemble that maximizes strengths while minimizing weaknesses of individual models.

### Strengths
- Novel perspective on model ensembling that goes beyond both conventional parameter merging and timestep-specific expert selection strategies
- Comprehensive consideration of multiple states (prompts, noise levels, timesteps, spatial locations) for adaptive feature aggregation, offering more fine-grained control than existing expert-based approaches
- Well-designed empirical validation with thorough ablation studies and clear visualization of spatial attention patterns
- Practical advantages in terms of implementation, requiring only the training of SABW while keeping base models frozen
- Demonstrates robust performance with fewer inference steps, suggesting potential for real-world applications
Strong quantitative improvements across multiple metrics (FID, IS, CLIP scores) compared to both single models and existing ensemble methods

### Weaknesses
 - While the paper introduces a novel method, it lacks direct comparison with recent mixture-of-expert diffusion approaches such as ERNIE-ViLG 2.0 [a], eDiff-I [b], and MEME [c], which also address the dynamic nature of the denoising process with multiple models. Basically, I think that the reader should be informed about the ideas that can be thought of in the direction of improving DPMs using multiple models, such as using different expert models along the time axis, and how this study proposes a different concept from those studies. Specifically, comparing performance metrics (e.g., FID, IS, CLIP scores), computational efficiency (inference times, resource utilization), and qualitative differences in generated images would provide a clearer understanding of how AFA stands relative to these methods. Including such comparisons or ablation studies would strengthen the claim that spatial-aware aggregation offers advantages over or complements timestep-specific expert selection. In the process of improving DPMs by utilizing multiple models, I believe that research directions along two axes, spatial and temporal, should be compared.
- Missing theoretical analysis on when and why spatial-aware feature aggregation outperforms timestep-specific expert selection. Incorporating theoretical insights—such as analyzing the information flow, gradient propagation, or the capacity of spatial attention mechanisms within the diffusion process—could help elucidate the conditions under which AFA is most effective. A comparative theoretical framework would enhance the understanding of the benefits and limitations of spatial versus temporal adaptation strategies.
- Computational overhead during inference could be problematic for practical applications, yet alternatives or optimizations are not thoroughly explored. I think the limitations associated with these computational costs should be clearly explained and guidelines for practical application should be provided.
- Experiments limited to SDv1.5-based models, raising questions about generalizability across different model architectures
- Lack of analysis on the trade-off between the granularity of adaptation (spatial/temporal) and computational cost

### Questions
- Given that recent work in diffusion models increasingly focuses on efficiency, have you explored knowledge distillation or other compression techniques to reduce the inference overhead of AFA?
- How does the spatial attention mechanism in SABW interact with different types of prompts? Are there certain prompt patterns where timestep-specific expert selection might be more appropriate than spatial aggregation?

### Soundness
3

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
3

### Summary
This paper introduces a novel ensembling method called Adaptive Feature Aggregation (AFA) for leveraging multiple high-quality diffusion models to enhance text-to-image generation capabilities. The key innovation of AFA is its ability to dynamically adjust the contributions of multiple models at the feature level based on various states, such as prompts, initial noises, denoising steps, and spatial locations. This is achieved through a lightweight Spatial-Aware Block-Wise (SABW) feature aggregator that adaptively aggregates block-wise intermediate features from multiple U-Net denoisers into a unified one.

The paper's main contributions are:
1. The proposal of an ensembling-based AFA method that dynamically adjusts the contributions of multiple models at the feature level.
2. The design of the SABW feature aggregator, which can produce attention maps according to various states to adaptively aggregate the block-level intermediate features from multiple U-Net denoisers.
3. The demonstration, through both quantitative and qualitative experiments, that the proposed AFA outperforms the base models and the baseline methods in terms of superior image quality and context alignment.

### Strengths
The paper presents a novel Adaptive Feature Aggregation (AFA) method for ensembling multiple diffusion models in text-guided image generation. 

1. The paper introduces a new approach to ensembling diffusion models by dynamically adjusting the contributions of multiple models at the feature level based on various states such as prompts, initial noises, denoising steps, and spatial locations. This is a departure from existing methods that primarily adopt parameter merging strategies to produce a new static model.

2. The proposed AFA method is evaluated quantitatively and qualitatively, demonstrating improvements in image quality and context alignment. The method outperforms base models and baseline methods.

3. The paper is well-structured, with clear explanations of the proposed method, including the Spatial-Aware Block-Wise (SABW) feature aggregator. The authors provide a detailed description of the AFA framework, its components, and the training and inference processes.

4. The paper addresses an important research direction in leveraging multiple high-quality diffusion models to improve text-to-image generation. The proposed AFA method has the potential to significantly enhance the generation capabilities of diffusion models, making it a valuable contribution to the field.

### Weaknesses
1. AFA's computational efficiency is lower for individual inference steps compared to merging-based methods, primarily due to the additional parameters introduced by the Spatial-Aware Block-Wise (SABW) feature aggregator. However, the paper notes that AFA's tolerance for fewer inference steps can offset this initial inefficiency, making the overall computational cost comparable to that of base models or merging methods.

2. The performance of AFA is contingent on the quality of the base models. If the base models have inherent limitations in their generative capabilities, increasing the number of training samples for AFA does not necessarily lead to improved performance.

3. While the paper proposes a dynamic feature-level ensembling method, it does not extensively explore alternative ensemble strategies that could potentially offer further improvements.

4. The paper does not address the scalability of the AFA method when ensembling a larger number of models, which could become computationally prohibitive.

### Questions
Has any research optimizing the SABW module to reduce its computational overhead been done? potentially through model pruning, quantization, or more efficient network architectures.

Other ensemble strategies can be compared, such as model distillation or more sophisticated attention mechanisms.

Could the authors extend their evaluations to diverse datasets to testify its generality?

### Soundness
2

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
3

### Summary
This work introduces a novel method called Adaptive Feature Aggregation (AFA) to enhance the performance of text-guided diffusion models by dynamically adjusting the contributions of multiple models at the feature level. Different from the existing static model which utilizes merging strategies, AFA can recognize the performance of diffusion models depending on different states including text prompts, initial noises, denoising steps, and spatial locations. The method employs a lightweight Spatial-Aware Block-Wise (SABW) feature aggregator, which produces attention maps to realize adaptively aggregation of block-level intermediate features from multiple U-Net denoisers.

### Strengths
1. the method can adjust the contributions of multiple diffusion models based on various states.
2. the generated attention maps can give a straightforward view of the context and timestamps in the ensembled diffusion model.
3. AFA demonstrates its tolerance to reductions in inference steps.

### Weaknesses
1. the method integrates intermediate features from U-Net denoisers with the same architecture, posing doubts on its ability to ensemble a wider range of model types or architectures. The method's reliance on consistent feature maps across models limits its applicability to scenarios where models have different internal structures or feature representations. This is a significant constraint, as many advanced diffusion models employ diverse architectures beyond the standard U-Net. For example, transformer-based diffusion models or those with different attention mechanisms might not be directly compatible with the proposed feature aggregation approach.
2. As the number of base models increases, the method's reliance on multiple base models may result in overfitting if, say, the base models have correlated features. The adaptive feature aggregation might not effectively differentiate between redundant information provided by highly correlated models, potentially leading to a model that overfits to the training data and generalizes poorly to unseen examples. This is especially concerning when the base models are trained on similar datasets or have similar inductive biases, which can lead to highly correlated feature spaces.

### Questions
1. How does the method handle the situation that base models have correlated features or that base model bias is generated by imbalanced data? 
2. How is the method’s performance when facing particularly noisy input data?
3. What modifications should be considered when applying AFA to integrate models with different architectures?
4. Are there any potential optimization strategies to reduce the extra computational complexity brought by AFA to every single inference?
5. What if the contributions of different models have conflict impacts on the result significantly?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper investigates an ensemble of multiple diffusion models with identical architectures. Rather than simply blending the network parameters of multiple diffusion models through weighted averaging, it introduces a trainable "glue" module, referred to as the AFA method, to integrate them into a cohesive system. This module dynamically adjusts each model's contribution at the feature level, adapting to various conditions such as prompts, initial noise, denoising steps, and spatial locations. Specifically, the paper proposes a U-Net-specific "glue" module, called SABW. Through extensive experiments and ablation studies, the effectiveness of SABW in integrating three diffusion models with U-Net architectures is thoroughly demonstrated.

### Strengths
1. The paper is well-written and well-structured, with clear and informative figures and tables that effectively support the content.
2. The motivation is interesting and novel: using a trainable "glue" module to integrate multiple pre-trained diffusion model experts at the feature level, aiming to improve generation quality. This approach is instructive and easy to follow.
3. The experimental design is comprehensive and thorough. The paper conducts extensive experiments on two datasets, COCO 2017 and Draw Bench Prompts, utilizing four evaluation metrics for each. These experiments provide robust evidence of SABW's effectiveness in integrating three diffusion models with U-Net architectures, demonstrating the model's enhanced performance across diverse scenarios.

### Weaknesses
1. This paper aims to effectively integrate multiple diffusion models to achieve improved generation quality. However, based on the framework and experimental setup of SABW, it appears that SABW is only suitable for integrating diffusion models with identical U-Net architectures, which may limit its flexibility and applicability. Specifically, the method relies on aggregating feature maps at corresponding layers of the U-Net, making it difficult to apply to models with differing architectures or even those with the same architecture but different numbers of layers or feature map dimensions. This limits the potential for combining diverse expert models.
2. According to the training algorithm presented, SABW can theoretically be used to combine any N diffusion models. However, the experiments seem to only consider the integration of three diffusion models, without sufficient discussion or explanation of this choice. A study on the impact of the number of integrated diffusion models, including a detailed analysis of performance trends and computational costs, would better validate the effectiveness of SABW. It is unclear if the performance gains observed with three models would scale to a larger number of models, or if there would be diminishing returns.
3. During inference, AFA essentially combines all base models with the glue module SABW, which results in relatively low inference efficiency. The authors provided results for AFA with a reduced number of inference steps compared to the base models. However, comparing AFA's results to those of the baselines under the same reduced-step inference would better validate AFA's practical time efficiency. The current comparison does not isolate the effect of the reduced steps from the effect of the AFA method itself.

### Questions
1. Could the authors provide further explanation as to why you chose to randomly split the six diffusion models into two groups of three, rather than integrating all six models directly? Additionally, could you provide more insights into the rationale behind selecting three diffusion models for integration?
2. During the training process of AFA, it appears that intermediate inference features of all base diffusion models at different timesteps are required. Wouldn’t this process be quite time-consuming? Could the authors provide more information on the training time efficiency of AFA compared to other baselines?

### Soundness
2

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
This study focuses on dynamically ensembling multiple diffusion models with the same architecture for stronger general generation capability, previously done mostly by static merging. The authors propose to train a plug-in module to generate spatial attention maps for each U-Net block to aggregate the intermediate features. Experiments demonstrate consistent performance improvement.

### Strengths
1.	The studied task is very useful in practice. The technical contribution of this study should be acknowledged.
2.	The proposed method is intuitive and reasonable, with inner workings and results that match the motivation.
3.	Experiments show consistent performance improvement.

### Weaknesses
1.	The presentation really needs polishing. For example, “various states” are repeatedly mentioned in both line 80 and line 85. There is a missing reference in line 352. Some of the fonts in Figure 2 are also too small. The following two weaknesses are also related to presentation.
2.	SABW implements spatial attention using the composition of several modules, instead of a variant of typical multi-head self-attention in diffusion models. This makes the presentation quite confusing for readers who are familiar with diffusion model architecture. I think the authors should clearly remind readers of this difference, as well as explain why such a special architecture is necessary in comparison to some variant of self-attention.
3.	While this study aims to enhance the general generation capability, it is also a common goal of ensembling/merging to combine the styles/concepts of multiple models, which is not the interest of this study. The authors should help readers notice this difference.

### Questions
1.	More recent diffusion models, such as Stable Diffusion XL and DiT-based models, have different architectures from Stable Diffusion v1.5. For example, if we view DiT models in the same way as used in this study, the entire model will be a single block. SDXL models also have significantly larger inner structures within each block. How may the proposed method generalize to these new models?
2.	As far as I know, some diffusion models also fine-tune the text encoder alongside U-Net. How may the proposed method apply to such scenarios?
3.	In line 346, it is stated that all the methods generate 4 images. This means 4 images per what? Only 4 images per dataset will cause serious insufficiency in evaluation, so the authors should clarify if this is another presentation issue.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 6

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces Adaptive Feature Aggregation (AFA), a new feature layer ensemble method for generating high-quality images from text. In particular, the paper proposes a Spatial-Aware Block-Wise (SABW) aggregator, which seeks to aggregate intermediate features of various pre-trained models dynamically at the block level. Furthermore, the paper includes a wide range of quantitative & qualitative validations showing strong empirical evidence of AFA's improvements in a range of image generation tasks.

### Strengths
The strengths of the paper are as follows:
- The paper is well-written and provides a clear outline of the underlying motivation for AFA.
- The paper provides a timely analysis of an underexplored field of feature layer ensemble methods for diffusion models.
- SABW component addresses a novel spatial attention variation in denoising capabilities across states.
- The resulting AFA shows strong empirical results across a wide range of tasks.

### Weaknesses
Some weaknesses of the paper are as follows:
- From the reviewer's perspective, the AFA method, especially the SABW component, introduces a large degree of additional complexity.
- The review would also like to see some empirical comparisons with other methods when evaluating the computational efficiency of AFA.

### Questions
Where there any cases or prompts where the authors find that AFA underperforms expectations?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 7

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel method called Adaptive Feature Aggregation (AFA) for ensembling multiple diffusion models to improve the quality of text-guided image generation. By adding a spatial-aware block-wise feature aggregator in every unet block of two aggregated models, this work ensembles multiple diffusion models into a united one.

### Strengths
This work is novel to aggregate multiple diffusion models with a light weighted structure, showing an evident improvement on inference quality especially in small inference steps. The structure of Spatial-aware block-wise feature aggregator is well-designed, which has some enlightening reference value on latent map feature learning.

### Weaknesses
1. Considering the model version, the paper lacks comparisons with newer models like SD 3.0 or Flux. Considering the model architecture, the paper doesn’t use diffusion with different frameworks like DiT, but only ensembles multiple SDv1.5 with the same unet structure, which is not convincing. Besides, the application of this work is limited. The method fails when considering ensembling different diffusion model architectures.

2. The experimental details are incomplete, with no information on the hardware used, detailed memory consumption or quantitative analysis on time consumption.

3. The experiment is not rigorous enough. Aggregators are trained on JourneyDB which is a high-quality dataset, but baselines are not finetuned on the same dataset. The comparison between baselines and your ensembled model is not fair. Besides, in the paper it’s claimed that SDv1.5 failed to understand the number in the prompt, but this phenomenon is hard to reproduce.

### Questions
1. The contribution you mentioned in this paper is the sampling efficiency, but in the limitation phase you’re aware that “A significant limitation of our AFA is that a single inference step may necessitate a proportional increase in inference time, resulting in lower computational efficiency for that step”. As for comparison experiment Figure 4, I don’t think it fair and meaningful to only compare inference steps without detailed time consumption.

2. Some of the results are not reproducible. For instance, in Figure 5(b), the paper claims ”in Fig. 5 (b), all the base models and the baseline methods generate images containing more than one clock, despite the textual prompt specifying a single clock”, but my tests with SD 1.5 produced correct results.

### Soundness
3

### Presentation
3

### Contribution
3
