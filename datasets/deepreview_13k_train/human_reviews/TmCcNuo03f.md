# Measuring And Improving Engagement of Text-to-Image Generation Models

- Decision: Accept
- Scores: 8, 5, 8, 6

## Abstract
Recent advances in text-to-image generation have achieved impressive aesthetic quality, making these models usable for both personal and commercial purposes. However, in the fields of marketing and advertising, images are often created to be more engaging, as reflected in user behaviors such as increasing clicks, likes, and purchases, in addition to being aesthetically pleasing. Further, we find that existing image generation metrics like aesthetics, CLIPScore, PickScore, ImageReward, etc. fail to capture viewer engagement. To this end, we introduce the challenge of optimizing the image generation process for improved viewer engagement. In order to study image engagement and utility in real-world marketing scenarios, we collect EngagingImageNet, the first large-scale dataset of images, along with associated user engagement metrics. To address the lack of reliable metrics for assessing image utility, we use the EngagingImageNet dataset to train EngageNet, an engagement-aware Vision Language Model (VLM) that predicts viewer engagement of images by leveraging contextual information about the tweet content, enterprise details, and posting time. We then explore methods to enhance the engagement of text-to-image models, making initial strides in this direction. These include conditioning image generation on improved prompts, supervised fine-tuning of stable diffusion on high-performing images, and reinforcement learning to align stable diffusion with EngageNet-based reward signals, all of which lead to the generation of images with higher viewer engagement. Finally, we propose the Engagement Arena, to benchmark text-to-image models based on their ability to generate engaging images, using EngageNet as the evaluator, thereby encouraging the research community to measure further advances in the engagement of text-to-image modeling. These contributions provide a new pathway for advancing utility-driven image generation, with significant implications for the commercial application of image generation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces EngageNet, a text-to-image generation model optimization method to improve the audience engagement of the generated images, rather than merely the aesthetic quality and realism. Based on this, the first automated arena, i.e., EngageNet Arena, is proposed to benchmark the engagement of text-to-image models.

### Strengths
- The idea of the engagement-optimized image generation is novel, as images are often created to drive user engagement beyond just aesthetic appeal.
- The paper introduces a large dataset of 168 million tweets with images and associated user engagement metrics like likes, paving the way for such research direction.
- Multiple methods are explored to enhance the engagement of text-to-image models, including prompt conditioning, supervised fine-tuning, and reinforcement learning.

### Weaknesses
Null

### Questions
What are the further direction in this research topic? Given the situation that many labs may lack computational resources, how to make it possible for these researchers to follow your work? Will the EngageNet also be appliable to other research domains, such as multimodal item recommendation?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates how current text-to-image generation models fall short of predicting viewer engagement. To address this gap, the authors propose several contributions including (1) EngagingImageNet: A dataset of high-quality enterprise images alongside engagement metrics like user likes, which serve as real-world indicators of viewer engagement, (2) EngageNet: A Vision Language Model (VLM) trained on EngagingImageNet to predict engagement by analyzing contextual factors around each image, such as tweet content, enterprise details, and posting time, and (3) Engagement Arena: A benchmarking platform where EngageNet scores various image generation models based on their capacity to generate engaging images. The paper explores approaches to enhance engagement in generated images, including prompt-based conditioning, fine-tuning, and reinforcement learning with EngageNet-generated reward signals.

### Strengths
- The paper presents an interesting application to optimize image generation for viewer engagement, a metric commonly aligned with recommendation and commercial objectives. 
- The dataset curation and model development appear thorough. EngagingImageNet is large, high-quality, and potentially valuable for further research on engagement in visual content. The paper includes rigorous validation of EngageNet’s correlation with actual engagement metrics, offering a credible alternative to existing models.

### Weaknesses
 - As EngagingImageNet is sourced from enterprise accounts on Twitter, the dataset may have an inherent bias toward corporate content. For a model aiming to set a standard for engagement-optimized image generation, more diverse data sources would provide a broader foundation and improve applicability across various domains. Specifically, the model's performance on non-corporate content, such as artistic or personal images, is unclear, potentially limiting its generalizability.
- The effectiveness of engagement-enhancing techniques is primarily measured using EngageNet scores and correlations. Incorporating additional real-world engagement experiments, for example, a small-scale human evaluation study, would strengthen the claims regarding the improvements in viewer engagement and provide additional validation. The reliance on EngageNet scores alone might not fully capture the nuances of human perception and engagement, as these scores are ultimately a proxy for real user behavior.
- The negative sampling method for training EngageNet is vaguely described. The paper mentions that negative samples are randomly generated by pairing tweets with unrelated images, yet does not explain how the random sampling affects EngageNet's robustness or alignment with true engagement. The lack of detail regarding the selection criteria for these unrelated images raises concerns about the quality and representativeness of the negative samples, which could impact the model's ability to accurately discern between engaging and non-engaging content.

### Questions
-  Can you provide further detail on how negative samples were generated and their effects on training EngageNet? How does the negative sampling impact model robustness and alignment with actual user engagement?
- Can EngageNet be adapted to predict other engagement metrics (e.g., CTR, shares) in addition to likes?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This study constructs a large-scale dataset of images paired with user engagement metrics to investigate image engagement and utility in real-world marketing contexts. An engagement-aware visual language model (VLM) is developed to predict viewer engagement. Contemporary techniques are explored to enhance engagement in text-to-image models, including conditioning image generation on optimized prompts, supervised fine-tuning of Stable Diffusion on high-performing images, and reinforcement learning to align Stable Diffusion outputs. The authors also introduce a benchmarking method for text-to-image engagement models, offering the research community a standard framework for evaluating advancements in engagement modelling.

### Strengths
1.	The proposed method is robust, producing a large-scale, high-quality dataset that addresses the gap in image engagement and utility analysis.
2.	The paper is clearly written and well-structured.
3.	The authors evaluate various models, offering valuable insights into the dataset’s application and benchmark characteristics.

### Weaknesses
1.	A more precise definition and scope of viewer engagement would be helpful, as the current metrics appear to include clicks, likes, and shares. It is unclear how these metrics are weighted or normalized, and whether they are equally indicative of engagement. Additionally, detailed statistics of the dataset should be provided, including the distribution of engagement scores, the number of unique users, and the types of content included, to help the community better understand this dataset.
2.	Given the dataset spans over a decade, how is the temporal information being utilized? It's not clear if the model accounts for shifts in user preferences or platform algorithms over time, which could significantly impact engagement metrics. The paper should clarify if the temporal information is used as a feature, and if so, how it is incorporated into the model.
3.	While the introduction of the engagement dataset and benchmarking metrics is a valuable contribution, the proposed methods—conditioning image generation, supervised fine-tuning, and reinforcement learning for diffusion alignment—are relatively straightforward adaptations of existing techniques. The paper lacks a novel approach to these tasks, such as a new loss function or a unique architecture modification tailored to engagement prediction. A more innovative approach to these tasks could elevate the paper’s impact.
4.	The paper could discuss a broader range of use cases and scenarios, such as recommender systems or advertising, beyond standard text-to-image applications, especially given the marketing focus of this work. It would be beneficial to see how the engagement model could be integrated into different systems, and what practical benefits it could offer in these contexts.
5.	An in-depth discussion on potential use cases would be beneficial. The paper should explore how the model could be used in real-world scenarios, and what challenges might arise during implementation.
6.	The paper does not clarify whether any collected data contain identifiable information. If they do, obtaining informed consent from individuals would be essential. The paper should explicitly address data privacy concerns and describe any measures taken to anonymize the data.

### Questions
1.	A more precise definition and scope of viewer engagement would be helpful, as the current metrics appear to include clicks, likes, and shares. Additionally, detailed statistics of the dataset should be provided to help the community better understand this dataset.
2.	Given the dataset spans over a decade, how is the temporal information being utilized?
3.	While the introduction of the engagement dataset and benchmarking metrics is a valuable contribution, the proposed methods—conditioning image generation, supervised fine-tuning, and reinforcement learning for diffusion alignment—are relatively straightforward adaptations of existing techniques. A more innovative approach to these tasks could elevate the paper’s impact.
4.	The paper could discuss a broader range of use cases and scenarios, such as recommender systems or advertising, beyond standard text-to-image applications, especially given the marketing focus of this work.
5.	An in-depth discussion on potential use cases would be beneficial.
6.	The paper does not clarify whether any collected data contain identifiable information. If they do, obtaining informed consent from individuals would be essential.

### Soundness
3

### Presentation
3

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
This paper introduces a novel consideration in the text-to-image generation task: human engagement. The authors first collect a large dataset, EngagingImageNet, from an online platform. They then train EngageNet to assess the engagement level of generated images based on auxiliary information embedded in the prompts. Additionally, they propose methods to leverage EngageNet to enhance the performance of text-to-image models. Finally, the authors introduce Engagement Arena to assess the engagement levels of different text-to-image models. This work presents a comprehensive framework for evaluating and improving engagement of text-to-image models.

### Strengths
1. The collected dataset EngagingImageNet is a strong foundation, as authors provide the detailed introduction of obtaining and filtering this datasets. This dataset encompasses multimodal information for each image, supporting not only engagement assessment but also various other applications.
2. The author trained the EngageNet with several tricks, obtaining a superior performance. The release of such model would offer both academia and industry a new perspective for evaluating generated images.
3. This paper introduces multiple strategies for enhancing the engagement of generated images, during run-time and train-time. They achieve notable improvement using these approaches.

### Weaknesses
1. The paper would benefit from a more detailed explanation of the DDPO method utilized, including the hyper-parameters and loss terms. Specifically, the paper lacks a clear description of how the state, action, and reward are defined within the Markov Decision Process framework. The transition function and how it relates to the denoising steps of the diffusion model should also be elaborated upon. Furthermore, the specific loss function used to optimize the policy and how it incorporates the reward signal from EngageNet requires more detailed explanation. The paper should also include a discussion of the specific hyperparameter choices, such as learning rate, batch size, and the number of training epochs, and how these were determined.

2. The paper lacks a user study or online experiment to evaluate the engagement of images generated by the fine-tuned models. It is unclear whether the fine-tuned models genuinely improve engagement or merely optimize to satisfy the reward model. Without a user study, it is difficult to ascertain if the improvements in the EngageNet scores translate to actual human engagement. The paper should include a discussion of the potential biases in the EngageNet model and how these biases might affect the results. For example, the model might be biased towards certain visual styles or content, which may not align with the preferences of all users.

3. The paper lacks discussion of some relevant works:

[1] Rich Human Feedback for Text-to-Image Generation, CVPR 2024.
[2] Towards Reliable Advertising Image Generation Using Human Feedback, ECCV 2024.
[3] Directly Fine-Tuning Diffusion Models on Differentiable Rewards, ICLR 2024.

Moreover, other works on using human feedback to improve image generation models should be considered.

### Questions
1. Why did the authors not consider including retweets as part of the engagement indicator?

2. Why was SD 1.4 chosen for train-time optimization, as it is one of the weakest models?

3. Does KPI refer to the normalized likes of an image? So the regression value of KPI is just used in training phase?

4. I would like to see an analysis of the complexity or latency of the proposed components, such as the Retrieval module, since an excessively long generation process would be impractical for real-world applications.

5. All concerns in Weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3
