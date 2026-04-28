# Beyond Fine-Tuning: A Systematic Study of Sampling Techniques in Personalized Image Generation

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 3, 5

## Abstract
Personalized text-to-image generation focuses on creating customized images based on user-defined concepts and text descriptions. A good balance between learned concept fidelity and its ability to be generated in different contexts is a major challenge in this task. Modern personalization techniques often strive to find this balance through diverse fine-tuning parameterizations and enhanced sampling methods that integrate superclass trajectories into the backward diffusion process.  Improved sampling methods present a cost-effective, training-free way to enhance already fine-tuned models. However, outside of fine-tuning approaches, there is no systematic analysis of sampling methods in the personalised generation literature. Most sampling techniques are introduced alongside fixed fine-tuning parameterizations, which makes it difficult to identify the impact of sampling on the generation outcomes and whether it can be applied with other fine-tuning strategies. Moreover, they don't compare with the naive sampling approaches, so the intuition of how the superclass trajectory affects the sampling process remains underexplored. In this work, we propose a systematic and comprehensive analysis of personalized generation sampling strategies beyond the fine-tuning methods. We explore various combinations of concept and superclass trajectories, developing a deep understanding of how superclass influence generation outputs. Based on these results, we demonstrate that even a weighted mix of the concept and superclass trajectory can establish a strong baseline that enhances the adaptability of concepts across different contexts and can be effectively transferred to any training strategy, including various fine-tuning parameterizations, text embedding optimization, and hypernetworks. We analyze all methods through the lens of the trade-off between concept fidelity, editability, and computational efficiency, ultimately providing a framework to determine which sampling method is most suitable for specific scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This manuscript systematically studies the sampling techniques for personalized text-to-image diffusion models. Various combinations of concept and superclass trajectories are explored. A comprehensive analysis of existing techniques is presented that covers fidelity, edit ability, and computational efficiency. A framework is provided to determine which sampling method to use for different scenarios.

### Strengths
1. A comprehensive study covering various sampling techniques and different aspects of quality evaluation is presented. 
2. A finetuning-independent evaluation is presented to demonstrate the effectiveness of different sampling strategies. 
3. A guideline on how to choose sampling strategies is provided that can balance between image similarity, text similarity, and computation overhead.

### Weaknesses
1. The main weakness is in the contributions. Although this manuscript presents a comprehensive study of various sampling strategies, they are all based on existing techniques. There are not many new ideas presented in the manuscript. The work lacks a novel methodological contribution, primarily focusing on empirical analysis of existing methods. While a systematic study is valuable, the absence of new techniques or modifications to existing ones limits the overall impact.
2. The results shown in the paper are all easy cases with common objects. It is not sure if the conclusion will stay the same for more challenging cases involving unique objects. The evaluation is limited to relatively simple object categories, and it's unclear whether the observed trends in sampling strategy effectiveness would generalize to more complex or unusual concepts. For example, the study could benefit from including abstract concepts or very specific object instances that are not well represented in the training data.
3. All experiments are based on a single diffusion model backbone (Stable diffusion 2) and fine-tuning method SVDiff. It is not sure if the conclusion will still hold for other backbones and finetuning methods. The conclusions drawn from the experiments might be specific to the chosen model architecture and fine-tuning approach. The paper should include an analysis of how the sampling strategies perform with other diffusion model architectures such as Latent Diffusion Models or different fine-tuning techniques like LoRA or textual inversion to ensure the generalizability of the findings.

### Questions
would these sampling strategies also be helpful for non-finetuning personalized text-to-image diffusion models, for example ELITE?

### Soundness
3

### Presentation
3

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
Personalizing text-to-image models involves fine tuning a generative model on a small set of images that depict a new concept that wasn’t part of the training data of the text-to-image model. There are two objectives for every personalization method, (1) to be able to generate images that faithfully resemble the source subject and (2) to maintain the ability to generate images from novel prompts. The authors study the effectiveness of test-time sampling strategies for improving personalization methods. While there have been papers that developed or used various sampling techniques for aligning the personalized models in test-time, this paper studies different sampling techniques and compares them in terms of running time, subject fidelity and prompt alignment.  

Test-time sampling strategies usually run the denoising prediction of the model on the super-class concept, or on the new personal concept (and sometimes both) and make use of this to steer the generation process to either be more prompt-aligned or subject aligned. The ultimate good is to balance the trade-off of text- and subject fidelity.

The paper considers three simple-strategies, mixed-, switching- and masked- strategies. They also consider two strategies developed in the ProFusion method and Photoswap. For evaluation, the CLIP score and image-similarity metrics were used. The paper shows mixed-sampling consistently improving base personalization methods, while switching harms subject-fidelity. Masked-Sampling on the other hand induces unstable behavior for different hyperparameters.

### Strengths
[1] The paper is well written and the experimental setup follows existing evaluation protocols

[2] The authors use the common metrics in their evaluation (CLIP Score and Image Similarity), and use publicly available dataset. 

[3] The authors run their evaluation on multiple baseline personalization methods including DreamBooth, TI and SVDiff.

### Weaknesses
[1] The main concern I have about this paper is that it doesn’t convince the reader that test-time sampling strategies are effective and necessary for optimal personalization results. In particular, altering the sampling strategy at test-time indicates the personalization method used is not optimal, otherwise, the model should retain its capabilities in generating images from novel prompts. The gain using different sampling strategies is not significant, at least from the qualitative and quantitative results. 

[2] While the experimental section is well carried - it lacks deeper analysis beyond CLIP and Image similarity report. What would be the result if you change the sampling with superclass to something else,  how would that change the findings of the results ? For example instead of sampling “A dog wearing a police outfit”-> “Wearing a police outfit”. Another interesting thing to check is to measure how different the “super-class” trajectories are from the personalized trajectory, and whether it indicates something regarding the personalized model. 

[3] The authors should consider new state-of-the-art personalization methods and compare the effectiveness of using test-time sampling strategies on newer methods. 

[4] The qualitative samples don’t show enough evidence that test-time sampling strategies are sufficient for ultimate personalization results. It is necessary to assess the performance on long prompt and complicated prompts.

### Questions
As appears in the paper, the authors use the fine-tuned model prediction on the super-class rather than taking the base-model prediction. Is this the case ? and if so, why not use the base-model prediction as it has better text-alignment.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper performs a detailed ablation study around different sampling approaches for personalized text-to-image diffusion models. The different sampling approaches are built around sampling with the concept (e.g., "photo of a V*") and sampling with the superclass of the given concept (e.g., "photo of a dog") and compared various approaches of combining those two during sampling (e.g., by combining them via classifier-free guidance or by doing some sampling steps with the concept prompt and some sampling steps with the superclass prompt). The ablations show that, given a personalized model, the sampling strategy will affect how much the resulting image will follow the overall prompt and how much it preservest the identity.

### Strengths
This paper performs a detailed ablation study of various sampling strategies combining the personalized prompt (e.g., photo of a V*) and the superclass prompt (e.g., photo of a dog). Many different sampling approaches are evaluated across many different hyperparameters across different personalized models and the results are presented in graphs, showing the pareto front of the different sampling approaches and hyperparameters.

The ablations show that the sampling strategy and sampling parameters clearly have an impact on the quality of the output. As such, the paper highlights that choosing a good sampling strategy and sampling hyperparameters is crucial for personalized text-to-image models and that related works should disentangle the impact of improved sampling strategies from the impact of potential other changes to the personalization approach (e.g., architecture or finetuning changes).

### Weaknesses
While the ablation is comprehensive the results are not necessarily surprising and it is also not clear to me what to do with the results. Different sampling approaches have different advantages and trade-offs (both in quality and sampling cost) and there is no winner. Rather, the best sampling approach is dependent on the model, desired outcome, and available inference compute. But I feel like that was clear before this and is also evidenced by the large related literation on sampling approaches for diffusion models, all of which have different trade-offs and advantages.
So it's not clear what novel knowledge this ablation concretely contributes or how it would change the approach to current personalization approaches.

### Questions
What is the concrete outcome of the ablations? Do you suggest to use a default sampling approach or specific hyperparameters? Will that recommendation translate to other models besides SVDDiff?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a new perspective on sampling strategies in personalized image generation. The authors conduct a systematic and comprehensive analysis of the pure sampling process, which is orthogonal to pseudo-token optimization, U-Net fine-tuning, and encoder training stages typically used for learning specific concepts. They explore various methods for combining concept and superclass trajectories, including switching, mixing, and masked sampling techniques, as well as their hybrid variants. Experimental results demonstrate that integrating these strategies into existing personalized generation methods can effectively enhance both concept fidelity and context alignment.

### Strengths
- The paper offers a comprehensive overview and detailed analysis of various personalized generation methods, including discussions of related approaches such as ProFusion and Photoswap.
- The authors provide insights into customized generation. They propose several simple and concise sampling baselines based on the backward sampling process, which are cost-effective, require no additional training, and can be seamlessly integrated into off-the-shelf methods, independent of fine-tuning approaches.

### Weaknesses
 - While mixed sampling, stage sampling, multi-stage sampling, and mask sampling are generally straightforward to understand, Equation (11) appears to be merely a combination of the previous methods, making it somewhat complex and less engaging. The introduction of excessive hyperparameters may reduce its practical applicability. Incorporating a complementary adaptive hyperparameter selection strategy could significantly enhance its effectiveness.
- Some of the experimental settings require more detailed explanations. Specifically, please clarify what 'TS' and 'IS' represent, and elaborate on the necessity of using the Pareto Frontier in your analysis.
- The purple dog in Fig. 1(b) is too similar to the concept dog. It is recommended to replace it with a dog that better represents the superclass to more effectively illustrate the distinctions between concept and superclass trajectories.
- Typos: Page 5 line 259 "speciall" should be "special",  Page 13, line 674: "Textual Inveersion" should be "Textual Inversion"; Page 2, line 078: "...by fine-tuning strategies; ;" should be "...by fine-tuning strategies;".

### Questions
- Fig. 2 shows the results of "a purple V*" and "A purple dog". Are there any changes in generating samples with "a purple V* dog"?
- In Figure 9, most of the qualitative results compare SVDiff combined with the proposed sampling methods against other state-of-the-art personalized generation methods. It would be beneficial to also compare the proposed sampling methods applied to other state-of-the-art methods. For example, comparing DreamBooth+ Mixed versus DreamBooth+ProFusion.
- In the evaluation of DreamBooth, it is mentioned using Image Similarity (IS) to assess concept identity preservation. However, DreamBooth typically employs both CLIP-I and DINO metrics to calculate the similarity between real and generated images. Please clarify which specific metric is used for IS.
- It is recommended to display the masks used in the masked sampling method to intuitively demonstrate their ability to extract concept regions and to illustrate the influence of the quantile $q$ on the mask. Additionally, please explain why you chose to use a binary mask instead of a soft mask.
- On page 4, line 199, the phrase "Up to 10 steps" requires clarification. The hyperparameter corresponding to the value 10 is not indicated as $t_{sw}$ in Figure 2. Please provide more details on this parameter.

### Soundness
2

### Presentation
2

### Contribution
2
