# IterComp: Iterative Composition-Aware Feedback Learning from Model Gallery for Text-to-Image Generation

- Decision: Accept
- Avg Score: 6.80
- Scores: 6, 6, 6, 8, 8

## Abstract
Advanced diffusion models like RPG, Stable Diffusion 3 and FLUX have made notable strides in compositional text-to-image generation. However, these methods typically exhibit distinct strengths for compositional generation, with some excelling in handling attribute binding and others in spatial relationships. This disparity highlights the need for an approach that can leverage the complementary strengths of various models to comprehensively improve the composition capability.
To this end, we introduce \textbf{IterComp}, a novel framework that aggregates composition-aware model preferences from multiple models and employs an iterative feedback learning approach to enhance compositional generation. Specifically, we curate a gallery of six powerful open-source diffusion models and evaluate their three key compositional metrics: attribute binding, spatial relationships, and non-spatial relationships. Based on these metrics, we develop a composition-aware model preference dataset comprising numerous image-rank pairs to train composition-aware reward models.
Then, we propose an iterative feedback learning method to enhance compositionality in a closed-loop manner, enabling the progressive self-refinement of both the base diffusion model and reward models over multiple iterations. Theoretical proof demonstrates the effectiveness and extensive experiments show our significant superiority over previous SOTA methods (e.g., Omost and FLUX), particularly in multi-category object composition and complex semantic alignment. IterComp opens new research avenues in reward feedback learning for diffusion models and compositional generation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes IterComp, an iterative composition-aware reward-controlled framework. It introduces a model gallery and constructs a high-quality composition-aware model preference dataset. Utilizing a new iterative feedback learning framework, IterComp progressively enhances both the reward models and the base diffusion model.

### Strengths
1. This work claims to be the first work to introduce a reward-controlled framework in the concept composition generation, which is somehow novel in this field.
2. This work is presented well with complete theoretical details and proof.
3. The quantitative experimental results show better performance compared to SOTAs.

### Weaknesses
1. The qualitative comparison in Fig. 4 is confused. There seems to be a marginal improvement in Line 3 and Line 4. The authors should make the difference between the qualitative examples clear to be recognized.
2. The qualitative examples are not enough to evaluate the model performance since the cases in the paper are somehow complex. The authors can provide more examples for a single case. Also, there is a need to evaluate the stability of the proposed model.
3. The comparison with InstanceDiffusion is confusing. As a layout-guided method, InstanceDiffusion needs detailed layout inputs. It is not fair to provide only one box if the case includes two or more instances, as indicated in the third line of Fig. 4. As the authors attempt to compare with layout-to-image methods, a SOTA method named MIGC [1] is also not included.

### Questions
Please see the weakness.

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
3

### Summary
This paper introduces IterComp, a novel framework that enhances compositional text-to-image generation by aggregating preferences from multiple diffusion models through iterative feedback learning. The approach demonstrates superior performance in both compositional accuracy and image quality, while maintaining efficient inference speed. The main strength lies in its ability to combine different models' advantages without adding computational overhead, though the long-term stability of the iterative learning process could be further explored.

### Strengths
Novel and practical approach: The paper presents a simple yet effective way to combine multiple models' strengths for compositional generation without increasing computational complexity.

Strong empirical results: The method shows clear improvements over existing approaches, with comprehensive evaluations on both compositional accuracy and image quality metrics.

Well-structured technical contribution: The paper provides clear theoretical analysis with detailed proofs, and the iterative feedback learning framework is well-designed and easy to implement.

### Weaknesses
The paper mentioned that RPG is challenging to achieve precise generation, but Tab2 did not compare with RPG, and I checked that RPG's performance on T2I-Compbench is better than that of the paper.

It is necessary to test the results of FLUX-dev directly on the t2i compbench to see how much improvement the method proposed in this paper has. I currently suspect that the improvement may not be very significant.

### Questions
See weakness

### Soundness
2

### Presentation
3

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
This paper propose a framework that aggregates composition-aware model preferences from multiple models and employs an iterative feedback learning approach to enhance T2I compositionality and general performance. The qualitative and quantitative results show their SOTA compositional generation capabilities compared to previous works.

### Strengths
1. This paper presents a novel framework combining preferences from multiple diffusion models to enhance compositional text-to-image generation and address the relationship understanding in diffusion models.
2. The qualitative/quantitative results show comparable improvements in compositionality.
3. A composition-aware dataset is collected which provide diverse preferences that inform the reward models. (will it be released in the future?)

### Weaknesses
1. There is limited discussion of the computation resources required to manage multiple reward models, which may affect the scalability in large-scale applications. Although the authors claim that their model has fast inference speed, the cost of model training and data collection is not clear. This makes me feel less likely than DPO to be widely used in practice.
2. The user study only demonstrates the user preferences lacking the deep analysis of attribute binding and object relationship, which are critical to model performance. 16 samples is also too small to evaluate such a complex task.

### Questions
1. As mentioned in W.1, how long does the training loop take (including the iterative feedback learning)?
2. Could I use this method to improve a specific concept generation (e.g., a human-object interaction)? How much time does it take from collecting synthetic data to finalizing the model training?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This study addresses improving the compositional text-to-image generation capability of less powerful diffusion models. The authors contribute in two main areas. First, they decompose the capabilities of various diffusion models into three domains—attribute binding, spatial relationships, and non-spatial relationships—and rank model outputs accordingly to guide reinforcement learning with reward models specific to each domain. Second, they introduce an iterative training process that utilizes the fine-tuned diffusion model outputs to progressively enhance the reward models.

Through multiple experiments, the study demonstrates the proposed method’s effectiveness, enabling early-stage models to achieve comparable generative abilities with reduced inference time. The authors also verify the effectiveness and general applicability of each design component across different models.

### Strengths
1. The paper is well-structured, making it accessible and easy for readers to follow.
2. Clear formulas are provided for each component, effectively removing any ambiguity.
3. Mathematical proofs substantiate the validity of the proposed method.
4. The authors conduct detailed, extensive experiments to support their approach.
5. Illustrative images are included, enhancing clarity and understanding.

### Weaknesses
1. About the number of texts used for attribute binding, "500 prompts" in Line 185 is inconsistent with "1500" in Table 1. Which is correct?
2. Although the experiments are detailed, some comparisons appear incomplete. The reinforcement learning from human feedback (RLHF) approach leverages outputs from advanced models like FLUX and SD3 for training, yet direct comparisons with these models are not provided. Including these comparisons would better highlight the method's effectiveness. Specifically, the paper should include a comparison of the proposed method against these models using the same compositional metrics, as well as metrics for image quality and inference time. Without these direct comparisons, it is difficult to fully assess the practical advantages of the proposed method.
3. An additional experiment focusing on the first-round fine-tuned model—trained solely with human-annotated data—would be valuable. This would clarify the necessity and impact of the iterative training approach. It is unclear if the iterative training is truly necessary or if a single round of fine-tuning with sufficient human-annotated data would achieve similar results. The paper should include a comparison of the first-round fine-tuned model against the final model, using the same evaluation metrics.

### Questions
In addition to the weakness mentioned above, I have a question regarding stability. 

Based on my experience, RLHF in diffusion models can often be unstable. I’m curious whether your method consistently produces stable results or if there’s a risk of occasionally poorer outcomes. I’m concerned that the iterative training process might lead to overfitting on biases present in the reward models, potentially reducing overall robustness.

I hope the authors can make up for the weaknesses mentioned and address these questions.

### Soundness
3

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
The paper presents a new dataset for compositional generation where experts evaluate the outputs of multiple pre-trained models. The dataset consists of three aspects of compositionality: attribute binding, spatial relationships, and non-spatial relationships, along with 52.5K image-rank pairs, which can be used for training feedback, ranking, or reward models.

The second contribution of the paper is using the collected dataset to train reward models for each of the three key aspects. A multimodal model (BLIP) is used as a feature extractor for both the prompts and the generated images, and the extracted features are projected by MLPs to output the reward. The goal is to predict how good the given image-prompt pairs are by training the model similar to contrastive learning (moving toward winning examples and away from losing examples).

The third contribution is improving the compositional ability of a base model (SDXL is selected but it should not be limited to that) by optimizing it using the trained reward models. The base model is trained to maximize the reward model's output so that its outputs are better aligned with the reward models, which are trying to enforce compositionality. Furthermore, the paper proposes an iterative update mechanism for both reward models and the base model. Reward models are updated to predict the rankings generated by experts while the base model is updated to maximize the outputs of reward models. Through this process, both the base model and reward models are improved for their specific tasks.

**Important note:** This review's technical content and analysis are my original work. Large Language Models were used solely to improve grammar and writing style, without altering any meanings or substantive feedback.

### Strengths
* The collected dataset can lead to better models and new research directions. Furthermore, researchers can follow a similar approach to collect their own data. The data can also be used for other RLHF methods, such as diffusion-DPO.
* The iterative feedback mechanism seems to be a novel way to optimize both reward models and the base model.
* The code is shared, which allows reviewers to follow the details of the proposed method.
* The performance gain from IterComp appears significant, as evaluated through user studies, quantitative analysis, and qualitative assessment.

### Weaknesses
 * Table 5 should be in the main part instead of the Appendix, as it simply demonstrates that the proposed method outperforms previous methods.
* Several experiments are missing:
   - The paper combines all reward models simultaneously, likely leading to improved compositional performance. However, reviewers would benefit from seeing the individual effect of each reward model. Specifically, it is unclear if all three reward models contribute equally, or if one or two dominate the performance gains. An ablation study is needed to isolate the contribution of each reward model (attribute, spatial, and non-spatial) by training the base model with each reward individually and in combinations.
   - While SDXL is chosen as the base model, testing other models would help reviewers understand how reward models affect different base architectures. The effectiveness of the reward models may be dependent on the base model's architecture, and it is important to evaluate this dependency. For example, it is unclear if the same level of improvement can be achieved with models that have weaker or stronger compositional abilities than SDXL. Testing on models such as SD1.5 and SD2.1 would provide a more comprehensive understanding of the method's generalizability.
   - It would be valuable to examine Diffusion-DPO's performance when trained on the collected dataset. Currently, Diffusion-DPO is trained on the pick-a-pic dataset, which is larger but lacks compositional details. These results would be necessary to evaluate the proposed method's effectiveness using consistent standards. A direct comparison on the same dataset would provide a more robust evaluation of the proposed method's advantages over existing approaches.
* Expert ranking may inadvertently include aesthetic information [This observation is meant to prompt discussion rather than highlight a weakness, as the underlying cause remains unclear]:
   - When IterComp is applied, the aesthetic score improves, suggesting that reward models can interpret image aesthetics, since reward maximization leads to better aesthetic scores. This could be because either expert rankings are influenced by image aesthetics (beyond compositional attributes) or because models with better composition naturally generate more aesthetic images (for instance, FLUX, being the best compositional model, likely produces more aesthetically pleasing outputs). It is important to investigate whether the reward models are truly capturing compositional aspects or if they are also influenced by aesthetics, which could lead to unintended biases.
* Some experimental conditions may be misleading:
   - The paper uses 40 inference steps for all models to ensure fairness. However, some models can generate samples with fewer steps; for example, FLUX-dev uses 28 steps by default. This raises questions about the optimality of the chosen inference steps for each model and whether this choice is truly representative of each model's capabilities.

### Questions
* Training time considerations:
   - Diffusion-DPO operates in the latent space without requiring image decoding. In contrast, IterComp requires image decoding for the reward models (though this could be avoided by training the reward model with latent space inputs), likely resulting in slower training. Additional commentary on the training scheme would be valuable.
* Potential code and paper discrepancy:
   - The paper describes an iterative feedback mechanism that optimizes both reward models and the base model. However, examination of `feedback_train.py` reveals that only unet parameters (base model) are passed to the optimizer. This suggests that only the base model is being optimized, while reward models remain static. This difference requires clarification.
* Question regarding test-time adaptation:
   - Could the iterative feedback mechanism be applied as test-time adaptation of the base model? Similar to Slot-TTA [1], the base model could be optimized using reward models to improve compositional quality. The process would work as follows: for a given prompt, the base model generates an image, which is then evaluated by reward models. The base model's parameters would be updated to maximize these rewards. This process could be repeated for several iterations. This approach would eliminate the need for training the base model, allowing it to adapt to any prompt at test time through multiple iterations. Comments on this possibility would be valuable.

[1] Test-time Adaptation with Slot-Centric Models, Prabhudesai et al., ICML 2023

EDIT: After the rebuttal and discussion with the authors, I raise my score to 8 from 6.

### Soundness
3

### Presentation
3

### Contribution
3
