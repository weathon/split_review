# VideoAlchemy: Open-set Personalization in Video Generation

- Decision: Reject
- Scores: 5, 5, 6, 3

## Abstract
Video personalization methods allow us to synthesize videos with specific concepts such as people, pets, and places. However, existing methods often focus on limited domains, require time-consuming optimization per subject, or support only a single subject. We present $VideoAlchemy~-$ a video model equipped with built-in multi-subject, open-set personalization capabilities for both foreground objects and backgrounds, eliminating the need for time-consuming test-time optimization. Our model is built on a new Diffusion Transformer module that fuses each reference image conditioning and its corresponding subject-level text prompt with cross-attention layers. Developing such a large model presents two main challenges: $dataset$ and $evaluation$. First, as paired datasets of reference images and videos are extremely hard to collect, we opt to sample video frames as reference images and synthesize entire videos. This approach, however, introduces data biases issue, where models can easily denoise training videos but fail to generalize to new contexts during inference. To mitigate these issue, we carefully design a new automatic data construction pipeline with extensive image augmentation and sampling techniques. Second, evaluating open-set video personalization is a challenge in itself. To address this, we introduce a new personalization benchmark with evaluation protocols focusing on accurate subject fidelity assessment and accommodating different types of personalization conditioning. Finally, our extensive experiments show that our method significantly outperforms existing personalization methods, regarding quantitative and qualitative evaluations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
his paper proposes VideoAlchemy, synthesizing personalized videos with multiple subjects and open-set capabilities without time-consuming optimization. It integrates multiple conditions like reference images and text prompts. It proposes a an automatic data construction pipeline and a new personalization benchmark, in which the model outperforms existing methods.

### Strengths
1. The task of multi-subject open-set video customization is promising.
2. The paper is clearly written
3. This paper constructs a large-scale dataset and introduces a new personalization benchmark, which may promote future work.

### Weaknesses
1. The pipeline for dataset construction doesn't impress me much. Using Grounding DINO and SAM is quite common, as seen in [1,2]. Similar operations for face cropping are also demonstrated in [3].
2. The differences between the proposed method and IP-Adapter are minimal, and further discussion would be beneficial.
3. It seems that the paper does not mention plans to open-source the constructed large-scale dataset.
4. Temporal metrics were not used in the experiments, even though temporal consistency is another crucial factor in video alongside quality.
5. The experiments lack comparison with multi-subject video customization methods.

### Questions
N/A

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
5

### Summary
The paper presents VideoAlchemy, a novel model for open-set video personalization that enables multi-subject, optimization-free video generation. It utilizes a Diffusion Transformer to integrate text prompts with reference images, addressing challenges in data collection and model evaluation. The paper introduces a unique benchmark, MSRVTT-Personalization, for evaluating video personalization performance on both foreground and background elements, showing that VideoAlchemy outperforms existing methods.

### Strengths
- **A Strong Video Personalization Model**: The paper introduces an open-set video personalization model that supports robust multi-subject capabilities. By leveraging large-scale pre-training, the model enhances efficiency by eliminating the need for test-time fine-tuning, which is a notable advancement.
- **Comprehensive Dataset Curation and Augmentation**: The paper develops an extensive dataset curation and augmentation pipeline aimed at reducing biases in training data, which strengthens the quality and generalizability of the model's outputs.
- **Introduction of MSRVTT-Personalization Benchmark**: The MSRVTT-Personalization benchmark provides a nuanced and valuable framework for evaluating personalized video generation, contributing a useful tool for future research in this area.

### Weaknesses
 - **Unclear Methodological Contribution of the Model**: While the dataset curation, augmentation pipeline, and benchmark are well-developed, the model itself primarily utilizes off-the-shelf techniques. It would be beneficial for the authors to clarify any specific methodological contributions of the model component. The paper lacks a detailed explanation of how the Diffusion Transformer is adapted for multi-subject personalization, particularly how it handles multiple reference images and corresponding text prompts simultaneously. The novelty of the approach is not clearly articulated beyond the integration of existing components.
- **Limited Baseline Comparisons**: The paper does not exhaustively compare its method against relevant video customization approaches, which could provide important context for the performance claims. Furthermore, differences in data, models, and training configurations across the compared baselines complicate a fair evaluation. The selection of baselines seems somewhat arbitrary, and a more systematic comparison against state-of-the-art methods in video personalization is needed to validate the claimed superiority. Specifically, the paper should compare against methods that also leverage diffusion models for video generation and personalization.
- **Lack of Ablation Studies**: The paper provides limited methodological ablation studies, particularly concerning the proposed training augmentation techniques and data. A more thorough exploration of these components would help clarify their individual contributions and effectiveness. For instance, it is unclear how the specific choices of image augmentations impact the model's performance, and whether these augmentations are crucial for achieving the reported results. The paper should also investigate the impact of different data augmentation strategies on the model's ability to generalize to unseen subjects and scenarios.

### Questions
Please refer to the weaknesses.

### Soundness
3

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
3

### Summary
The paper presents VideoAlchemy, a new video generation model capable of multi-subject, open-set personalization for both foreground and background elements. Built on a DiT architecture, it aims to handle personalization tasks across diverse subjects and settings. Different from those tuning-based methods, this paper direct trains the generation network from a large-scale dataset, eliminating the need for test-time optimization. To address the lack of paired video and image datasets, the authors introduce an automated data construction pipeline, alongside a new benchmark called MSRVTT-Personalization for evaluating subject fidelity in video synthesis.

### Strengths
● The model's design leverages separate cross-attention layers for text and image conditioning. It conceptually allows for effective handling of different modalities for more accurate conditioning. This design makes sense.

● This paper makes great efforts in building large-scale training datasets as well as the evaluation benchmark. If these can be publicly available, it will benefit research community.

● The paper proposes an effective data construction pipeline with extensive augmentations to counteract biases in training data.

● The model shows strong performance improvements in the proposed new task, particularly in preserving subject fidelity and achieving better video quality than previous methods.

### Weaknesses
1. One of the important contributions of this paper is the curated dataset. However, I have concerns about:
    - The quality and diversity of the training and evaluation datasets. From Fig. 8's word cloud, humans and static objects/scenes (laptop, branch, house, sunset, building, etc.) make up a larger proportion of the dataset. Videos with static objects may have minimal motion. Also, based on my experience, the videos in MSRVTT primarily feature humans and scenes, with fewer animals and objects, potentially limiting test set diversity.
    - Availability of training dataset. While the paper promises to release the test dataset, it does not confirm making the training dataset publicly available. I believe releasing the training dataset is of great significance to the open-source community, especially since this paper uses the curated dataset as one of its main contributions.
2. The method's innovation is relatively limited. Although the differences from the IP-Adapter are mentioned in the method part, the similar idea of using separate cross-attention layers for text and image embeddings has been explored in previous work [1]. It would be better to discuss the differences. Specifically, the paper should clarify how the proposed method addresses the challenge of binding multiple image conditions with corresponding text prompts, which is crucial for multi-subject customization. The current description lacks sufficient detail on this aspect.
3. The introduced evaluation benchmark mostly uses existing metrics and lacks comprehensiveness. It would be better to introduce new metrics, like temporal consistency or subject motion intensity as in VBench [2], to enhance the benchmark. The current metrics, such as text and video similarity, do not fully capture the temporal dynamics and subject-specific motion characteristics, which are important for evaluating video generation quality.
4. Another concern I have is about experiments:
    - Comparison Fairness. The method uses a DiT architecture, while comparison methods are mostly based on UNet, raising concerns that improvements might stem from a more robust video base model rather than the method itself. This makes it difficult to isolate the contribution of the proposed approach.
    - Baseline Selection. It would be better to apply and reproduce image customization methods to video generative models, as in VideoBooth [3], rather than animation. On the other hand, there are some face customization works for video generation, such as Magic-Me[4] and ID-Animator [5]. It is best to compare with these methods to verify the effectiveness of the proposed method. The current comparisons do not adequately cover relevant baselines in both general and face-specific video customization.
    - Lack of comparisons with multi-subject video customization methods. Since the paper studies the multi-subject customization task, existing methods like VideoDreamer [6], CustomVideo [7], and DisenStudio [8] should be discussed and chosen two or more for comparison. The absence of comparisons with these methods makes it difficult to assess the novelty and effectiveness of the proposed approach in the context of multi-subject customization.
    - Ablation Study. It would be better to conduct an ablation study on excluding text embeddings from image embeddings in image encoder. The current ablation study does not fully explore the impact of different design choices on the final performance.
5. I carefully viewed each video provided in the supplementary material. The video examples provided are not diverse enough for multi-subject video customization. There are only two categories, human and dog, and only one motion prompt "a ... is petting a dog on ...". It would be better to provide examples with different categories and prompts to demonstrate the effectiveness of the method on multi-subject customization.

### Questions
See the Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces VideoAlchemy, a video customization method that generates personalized videos with multiple subjects and specified backgrounds, eliminating the need for test-time fine-tuning. The approach leverages a DiT architecture with an additional cross-attention layer and linear projection. Furthermore, this paper curates a large-scale training dataset, while employing data augmentation and conditional subject sampling strategy for training. For evaluation, this work develops a multi-subject video customization benchmark with four metrics. Experimental results demonstrate that VideoAlchemy surpasses existing methods both quantitatively and qualitatively.

### Strengths
1. This paper studies the multi-subject open-set video customization task, which is interesting and meaningful for practical video generation.
2. The paper is well-written and easy to understand.
3. This work curates a large multi-subject video dataset, containing 37.8M videos with subjects, objects, and backgrounds. It also introduces a multi-subject video customization evaluation benchmark.
4. The generated videos exhibit relatively high quality by using the DiT model and abundant data.

### Weaknesses
1. One of the important contributions of this paper is the curated dataset. However, I have concerns about:
    - The quality and diversity of the training and evaluation datasets. From Fig. 8's word cloud, humans and static objects/scenes (laptop, branch, house, sunset, building, etc.) make up a larger proportion of the dataset. Videos with static objects may have minimal motion. Also, based on my experience, the videos in MSRVTT primarily feature humans and scenes, with fewer animals and objects, potentially limiting test set diversity.
    - Availability of training dataset. While the paper promises to release the test dataset, it does not confirm making the training dataset publicly available. I believe releasing the training dataset is of great significance to the open-source community, especially since this paper uses the curated dataset as one of its main contributions.
2. The method's innovation is relatively limited. Although the differences from the IP-Adapter are mentioned in the method part, the similar idea of using separate cross-attention layers for text and image embeddings has been explored in previous work [1]. It would be better to discuss the differences.
3. The introduced evaluation benchmark mostly uses existing metrics and lacks comprehensiveness. It would be better to introduce new metrics, like temporal consistency or subject motion intensity as in VBench [2], to enhance the benchmark.
4. Another concern I have is about experiments:
    - Comparison Fairness. The method uses a DiT architecture, while comparison methods are mostly based on UNet, raising concerns that improvements might stem from a more robust video base model rather than the method itself.
    - Baseline Selection. It would be better to apply and reproduce image customization methods to video generative models, as in VideoBooth [3], rather than animation. On the other hand, there are some face customization works for video generation, such as Magic-Me[4] and ID-Animator [5]. It is best to compare with these methods to verify the effectiveness of the proposed method.
    - Lack of comparisons with multi-subject video customization methods. Since the paper studies the multi-subject customization task, existing methods like VideoDreamer [6], CustomVideo [7], and DisenStudio [8] should be discussed and chosen two or more for comparison.
    - Ablation Study. It would be better to conduct an ablation study on excluding text embeddings from image embeddings in image encoder.
5. I carefully viewed each video provided in the supplementary material. The video examples provided are not diverse enough for multi-subject video customization. There are only two categories, human and dog, and only one motion prompt "a ... is petting a dog on ...". It would be better to provide examples with different categories and prompts to demonstrate the effectiveness of the method on multi-subject customization.

[1] Li X, Hou X, Loy C C. When stylegan meets stable diffusion: a w+ adapter for personalized image generation.

[2] Huang Z, He Y, Yu J, et al. Vbench: Comprehensive benchmark suite for video generative models.

[3] Jiang Y, Wu T, Yang S, et al. VideoBooth: Diffusion-based video generation with image prompts.

[4] Ma Z, Zhou D, Yeh C H, et al. Magic-me: Identity-specific video customized diffusion.

[5] He X, Liu Q, Qian S, et al. ID-Animator: Zero-Shot Identity-Preserving Human Video Generation.

[6] Chen H, Wang X, Zeng G, et al. Videodreamer: Customized multi-subject text-to-video generation with disen-mix finetuning.

[7] Wang Z, Li A, Xie E, et al. Customvideo: Customizing text-to-video generation with multiple subjects.

[8] Chen H, Wang X, Zhang Y, et al. DisenStudio: Customized Multi-subject Text-to-Video Generation with Disentangled Spatial Control.

### Questions
1. Please refer to the weaknesses section. If my concerns are well addressed, I am willing to modify my score.
2. Typo: "issue" in line 60.
3. Typo: line 176 has two periods.
4. In line 339, the paper mentions using six metrics but only introduces four metrics.

### Soundness
3

### Presentation
3

### Contribution
3
