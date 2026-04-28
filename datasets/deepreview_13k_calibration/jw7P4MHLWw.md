# Personalized Representation from Personalized Generation

- Decision: Accept
- Avg Score: 5.60
- Scores: 6, 6, 5, 5, 6

## Abstract
Modern vision models excel at general purpose downstream tasks. It is unclear, however, how they may be used for personalized vision tasks, which are both fine-grained and data-scarce. Recent work has successfully applied synthetic data to general-purpose representation learning, while advances in T2I diffusion models have enabled the generation of personalized images from just a few real examples. Here, we explore a potential connection between these ideas, and formalize the challenge of using personalized synthetic data to learn personalized representations, which encode knowledge about an object of interest and may be flexibly applied to any downstream task relating to the target object. We introduce an evaluation suite for this challenge, including reformulations of two existing datasets and a novel dataset explicitly constructed for this purpose, and propose a contrastive learning approach that makes creative use of image generators. We show that our method improves personalized representation learning for diverse downstream tasks, from recognition to segmentation, and analyze characteristics of image generation approaches that are key to this gain.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper aims to learn personalized representations given a small number of images of an object. This involves using T2I models to generate additional data followed by contrastive learning. A new dataset, PODS, was also introduced to allow for evaluations of these personalized representations under distribution shifts. Supportive results were shown for several tasks and datasets.

### Strengths
- The paper was well written and easy to follow.
- The overall idea of having a personalized vision backbone that can work well on several downstream tasks is interesting.
- The additional experiments on useful synthetic data was insightful.

### Weaknesses
 - Additional baselines or comparisons.
    - For example, generating additional data with augmentations instead of using T2I models is a cheap baseline. If this is done in real-aug (Tab. 2) and it is comparable to the results of Tab. 1, why does it seem to perform worse than no personalization?
    - It may also be useful to compare against using real data only to get an upper bound of the method.
    - It would be interesting to see if, with more real images, cut/paste would outperform Masked DB. I.e., if we can tradeoff sampling more images for a faster runtime.
- The method seems to be computationally expensive as it involves several stages of finetuning and generation. It may be useful to include the runtimes of each method beside the results in e.g., Tab 2.
- The method learns a personalized representation for a single instance, a more realistic scenario probably involves several personalized instances e.g., one in each object category in PODS.

### Questions
- What is the runtime for the methods in Tab. 2? And what is the breakdown e.g., how much time take for each stage?
- Methods for synthetic data generation e.g., for supervised training, tend to include a filtering step to ensure that the generations are faithful to the prompt. Was any filtering needed and how was it done?
- What are some of the potential complications from extending the method to multiple instances?

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
4

### Summary
This paper investigates using personalized synthetic images, alongside a few real images, to develop personalized visual representations that enhance performance across multiple downstream tasks, including classification, retrieval, detection, and segmentation. 

The authors propose a novel contrastive learning framework where a personalized representation is trained using only three real positive samples without any real negatives. To support the evaluation of this approach, they introduce the Personal Object Discrimination Suite (PODS) dataset, specifically crafted for testing under conditions such as pose variation and background distractors, along with reformulations of DeepFashion2 and DogFaceNet datasets for the same purpose. By leveraging generative models, particularly DreamBooth with masked training, they demonstrate the effectiveness of synthetic data for learning representations of specific instances. This personalized approach shows promising improvements over general-purpose pretrained representations.

### Strengths
The paper presents a creative combination of generative models and contrastive learning to address the challenge of instance-specific visual representation with minimal real data. 

The experimental framework is thorough, covering classification, retrieval, detection, and segmentation tasks across three datasets (DeepFashion2, DogFaceNet, and the newly introduced PODS). The results consistently highlight the advantage of personalized representations over pre-trained ones, demonstrating the robustness of the approach. The author also shows that the method could be integrated into existing pipelines.

The paper is well-organized and has clear explanations. Multiple figures, including pipelines and qualitative results, aid in understanding. Writing is accessible without unnecessary complexity, making the proposed approach and findings straightforward.

### Weaknesses
1. It looks unnecessary to exclude real negatives in the proposed setting of personalized representation learning. Unlike real positives, real negatives might be easily obtained directly from open-source data. The paper relies on generated negatives produced by the generative model, which can be computationally costly. Alternatively, obtaining real negatives from readily available online sources might be a more efficient solution. Could the authors provide additional insights into why they excluded real negatives and whether this impacts performance? Are there any existing works exploring the setting of including real negatives?

2. Figure 1 is somewhat unclear and could be improved to more explicitly illustrate the flow and connection between real and synthetic data in the proposed framework. Additionally, it is not mentioned in the main texts. More explanation may also help.

3. The term "real-augmentation" is mentioned but not clearly defined in the context of this paper, which could lead to confusion regarding its role and implementation. By line 473, it seems that the real-aug is just using the real images without any augmentation to train the backbone models. If so, "real images" might be a better name than "real-aug."

4. The method of real augmentation on the PODS dataset shows degraded performance compared to pre-trained representations in retrieval, detection, and segmentation tasks, especially in retrieval (combining information from Table 1 and Table 2). However, this phenomenon does not appear in the other two datasets. This anomaly is not fully explored, and further insight into the underlying cause would help readers understand any limitations in generalizing the approach across different datasets.

### Questions
In addition to the questions in the "weaknesses" section:

1. In Table 1, are the results obtained with or without access to segmentation masks? This point is somewhat unclear—could the authors clarify if this information is noted elsewhere in the paper?

2. For tasks such as detection and segmentation, where the performance improvement was less pronounced, do the authors have plans to refine the pipeline for further gains in these areas? If so, could they share any specific strategies or potential modifications they are considering?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the challenge of learning personalized representations. The authors utilize a generative model to augment the dataset for the target personalized object, followed by fine-tuning a pretrained model using contrastive learning. This approach aims to develop a model capable of handling downstream tasks related to the specific object. Several downstream tasks were evaluated, and the proposed method demonstrated an average improvement across these tasks.

### Strengths
1. The paper explores a novel and intriguing problem: learning personalized representations, which could be valuable for downstream tasks related to target objects. The setting is innovative and promising. 

2. The proposed method is both simple and effective, as the authors employ an image customization technique to augment the dataset and address the challenge of limited training data. 

3. Overall, the paper is well-structured and easy to read.

### Weaknesses
1. While the problem being studied is intriguing, the overall approach is relatively basic. The concepts of using image generation to augment the dataset and contrastive learning are not novel. The paper does not sufficiently explore the limitations of this combination, particularly in scenarios where the generated images might introduce biases or artifacts that negatively impact the learned representations. For example, if the generative model struggles with certain poses or lighting conditions, the augmented dataset might over-represent these flawed examples, leading to a skewed representation space.

2. Additionally, incorporating image generation could significantly increase the cost of the method. The paper lacks a detailed analysis of the computational overhead associated with the image generation step, including both training and inference costs. This omission makes it difficult to assess the practical feasibility of the proposed approach, especially when compared to alternative methods that might not require such a computationally expensive data augmentation process. The paper should also consider the energy consumption and carbon footprint implications of using generative models.

3. Moreover, in certain tasks, the method results in a decline in performance. The paper does not provide a thorough analysis of why the proposed method fails in these specific cases. It is crucial to understand the underlying reasons for these performance drops, such as potential overfitting to the augmented data or the introduction of noise that interferes with the learning process. Without a detailed investigation, it is hard to determine the reliability and robustness of the proposed method.

### Questions
1. Are there any real-world scenarios where the benefits of personalized representation outweigh the high training costs? 

2. In certain challenging tasks, like distinguishing between dog faces of the same breed, it might be helpful to present more difficult or even failure cases to showcase the capabilities of the proposed method. 

3. Why does the proposed method sometimes lead to a decline in final performance for certain tasks?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper explores the use of synthetic data to train personalized visual representations, addressing data scarcity challenges in fine-grained, instance-specific vision tasks. The authors propose a three-stage pipeline involving synthetic image generation, contrastive learning, and fine-tuning of a general-purpose pretrained model using only three real examples of an object. They introduce an evaluation suite, including two reformulated datasets (DeepFashion2 and DogFaceNet) and a novel PODS dataset, to evaluate the effectiveness of their approach across tasks such as classification, retrieval, detection, and segmentation. Results suggest that the proposed method outperforms pretrained models on these tasks and provides an analysis of the impact of generative models (e.g., DreamBooth) on representation quality. However, this work lacks certain methodological and experimental rigor, as discussed in the critique below.

### Strengths
The paper presents an interesting approach to personalized visual representation learning using synthetic data, offering a novel perspective on addressing data scarcity in fine-grained instance-specific tasks. 
The study showcases the potential of synthetic data in personalized representation learning, especially for data-limited tasks, indicating that personalized generative models could contribute to a broader field of personalized AI applications.
The PODS dataset is a valuable addition to the field, providing a benchmark for evaluating the performance of personalized visual models across multiple tasks. Although limited, it may be useful in future research for controlled comparisons in low-data personalized settings.

### Weaknesses
High Computational Cost: The approach’s dependency on DreamBooth and other costly generative models for fine-tuning makes it impractical for widespread use. By not considering more computationally feasible alternatives, such as GAN-based models, the method lacks the flexibility needed for real-world adoption. Lack of Baseline Comparisons and Systematic Experimentation: The paper does not provide enough rigorous comparisons against simpler, cheaper baselines that could yield similar or competitive results, such as training with real, small datasets or using augmentation strategies on a limited set of real images. This gap leaves the reader questioning the unique benefit of using complex synthetic data pipelines, particularly in relation to common data-efficient techniques in computer vision.
Limited Task Scope and Lack of Real-World Validation: Although the paper claims improvements across multiple tasks, the experimental setup is relatively narrow, focusing on a limited range of controlled settings. Given that the proposed approach aims for personalization, testing its robustness in diverse and complex real-world scenarios is essential. Additionally, the observed performance gains in detection and segmentation tasks are relatively small, raising concerns about the method's robustness. Ethical and Privacy Considerations: While the authors briefly address these considerations, they do not offer practical guidelines or safeguards to mitigate potential misuse. Expanding on ethical implications and providing specific measures for responsible deployment would improve the paper’s comprehensiveness. Inadequate Analysis of Data Diversity: Although the authors highlight the role of data diversity in improving representation quality, they fail to conduct a thorough, quantitative analysis of the impact of diversity on representation learning. The paper lacks a clear quantification of diversity’s effect on model performance, and only discusses a few configuration parameters, which does not sufficiently explore the potential of synthetic data augmentation.

### Questions
Given the reliance on DreamBooth, which is computationally intensive, have the authors considered alternative  generative models  to achieve similar outcomes? 
How does the computational cost compare to simpler data augmentation methods, and what trade-offs are involved in model performance?
Has the study examined the potential biases and limitations introduced by synthetic data in the personalized learning setting, especially in comparison to real data? Could the authors provide any quantitative result to show how the synthetic data representations compare with those learned from real data, particularly in terms of generalization?
The proposed approach has clear applications in sensitive areas, such as surveillance or individual tracking, raising potential privacy concerns. How do the authors propose to mitigate these risks,?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the challenge of using modern vision models for personalized vision tasks, which are often fine-grained and limited in data availability. The authors propose a method that combines insights from synthetic data in general representation learning and advances in T2I (text-to-image) diffusion models, leveraging personalized synthetic data to learn representations specific to an object of interest. To support this goal, they introduce an evaluation suite consisting of reformulated datasets and a novel dataset designed for personalized learning. The proposed contrastive learning approach uses image generators to enhance representation learning for diverse downstream tasks, such as recognition and segmentation.

### Strengths
- Clarity and Structure: The paper is well-organized and clearly written, making it accessible and easy to follow, even for readers who may be less familiar with the technical aspects of personalized representation learning in vision models.
- Visualization Quality: The visualizations of generated images are well-designed and effectively demonstrate the model’s representation capabilities, enhancing the clarity and impact of the experimental results.
- Meaningful Personalized Representation: The concept of learning personalized representations for specific objects is a valuable contribution, offering potential applications across various fine-grained and data-scarce tasks where general-purpose representations may fall short.

### Weaknesses
 - Effectiveness of contrastive learning: It is unclear if the observed performance gains stem from the proposed method or from the inherent knowledge in Stable Diffusion 1.5. In the appendix, “Table 4: Ablation on the Number of Anchor-Positive Pairs” indicates poor performance when the “# Synthetic Imgs” and “# Anchor-Pos Pairs” are small. Could the authors provide evidence that the improvement in representation learning is not primarily due to the knowledge embedded in Stable Diffusion? A comparison between the proposed contrastive approach and straightforward fine-tuning with the same number of synthetic positives (maybe I2T+LLM+Stable Diffusion) would help clarify this point. Specifically, it is not clear if the contrastive loss is truly necessary, or if the gains are simply due to the increased diversity of the training data generated by Stable Diffusion.
- Contrastive Learning Setup and Objectives: The purpose and setting of the contrastive learning approach remain ambiguous. If the objective is solely to improve personalized representation at inference, it would be useful to include more baselines to demonstrate the effectiveness of your contrastive learning, such as using simple LORA/finetuning on positives obtained from I2T+LLM+Stable Diffusion. Conversely, if the goal includes a defensive aspect, ensuring that performance declines for objects other than the target, results showing the performance on unrelated objects would provide valuable context. The current setup does not clearly define the intended use case for the contrastive learning, making it difficult to assess its true value. It is also unclear how the negative samples are selected, and whether this selection process impacts the final performance.
- Typos and Formatting:
  - Line 53: "e.g. a model" should be "e.g., a model".
  - Line 59: "e.g. recognizing" should be "e.g, recognizing".
  - Line 78: "i.e. no" should be "i.e., no".
  - Line 153: "e.g. segmentation" should be "e.g., segmentation".
  - Line 162: "e.g. one" should be "e.g., one".
  - Line 348: ”query” and ”retrieval” should be formatted as ``query``” and “``retrieval``.
  - Figure 2: Missing period. "Pipeline Our" should be "Pipeline. Our".
  - Figure 5: "following 4. " should be "following Figure 4. ".

### Questions
- Distillation vs. Personalized Fine-Tuning: Could the authors clarify whether the observed performance gains primarily result from their proposed contrastive method or from pre-existing knowledge in Stable Diffusion 1.5? Would a comparison with a straightforward fine-tuning approach on a large set of synthetic positives help isolate the benefits of the proposed method?
- Contrastive Learning Setup and Objectives: Regarding the contrastive learning approach, could the authors elaborate on its intended objectives? If the primary aim is to enhance personalized representation capabilities at inference, would adding a baseline using simple LORA or finetuning with I2T+LLM+Stable Diffusion positives be beneficial? Alternatively, if there is a defensive objective to reduce performance for non-target objects, would the authors consider providing results on unrelated objects?
- Clarification of Typos and Formatting: There are minor typos and formatting inconsistencies throughout the text (e.g., “e.g.” should be formatted as “e.g.,”). Would the authors consider a thorough review to address these to improve readability?

### Soundness
2

### Presentation
2

### Contribution
3
