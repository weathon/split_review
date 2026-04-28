# Image2Sentence based Asymmetrical Zero-shot Composed Image Retrieval

- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 8, 8, 8

## Abstract
The task of composed image retrieval (CIR) aims to retrieve images based on the query image and the text describing the users' intent. 
Existing methods have made great progress with the advanced large vision-language (VL) model in CIR task, however, they generally suffer from two main issues: lack of labeled triplets for model training and difficulty of deployment on resource-restricted environments when deploying the large vision-language model.
To tackle the above problems, we propose Image2Sentence based Asymmetric zero-shot composed image retrieval (ISA), which takes advantage of the VL model and only relies on unlabeled images for composition learning.
In the framework, we propose a new adaptive token learner that maps an image to a sentence in the word embedding space of VL model. 
The sentence adaptively captures discriminative visual information and is further integrated with the text modifier.
An asymmetric structure is devised for flexible deployment, in which the lightweight model is adopted for the query side while the large VL model is deployed on the gallery side.
The global contrastive distillation and the local alignment regularization are adopted for the alignment between the light model and the VL model for CIR task. 
Our experiments demonstrate that the proposed ISA could better cope with the real retrieval scenarios and further improve retrieval accuracy and efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an image2sentence based asymmetric framework for zero-shot composed image retrieval tasks. In particular, a lightweight visual encoder and a consequent adaptive token learner are designed to effectively extract the visual features from query images for the mobile side. By doing so, the learned features could be generated as a good visual prompt as with the text intent for conventional LLM to deal with image retrieval tasks. In addition, a local alignment regularization term is added to further improve the training. The experiments conducted on several benchmark datasets verify the effectiveness of the proposed method compared with existing SOTA ones.

### Strengths
1. This paper is of good written quality that makes the readers easy to follow. The logic, the notion expression, and the experiments are all very clear.

2. The asymmetric design is interesting and this design has been proven an efficient way to deal with resource-limited circumstances.

3. The experiments conducted are very convincing to support the contribution claimed by the authors. The properties of the proposed method are well demonstrated in the ablation study.

### Weaknesses
1. It could be better to discuss more about the number of token selections in detail. According to Fig 3, it seems the performance is a bit sensitive to the number of tokens used in the proposed method. Then, a more detailed discussion of this observation with a visual example of the same query but a different number of tokens could help to better demonstrate the impact brought by the tokens. Specifically, it is unclear how the token selection process balances the need for comprehensive visual information with the risk of introducing noise or redundancy. A more thorough analysis of the trade-offs involved in selecting different numbers of tokens, including the impact on attention maps and feature representations, would strengthen the paper.

2. It could be good to add a discussion of the relationship between the proposed adaptive token learner and the similar approach used in the following papers [1,2]. They have a similar structure, a discussion would help to better locate the position of the token learned in this work. While the paper mentions the token learner's role in extracting visual features, it does not adequately differentiate its specific function and contribution from existing token-based methods. A more detailed comparison of the architectural differences, training objectives, and the specific types of representations learned by the proposed token learner versus those in [1,2] is needed to clarify the novelty and unique aspects of this work.

### Questions
Please check the weaknesses above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a novel approach to composed image retrieval (CIR), emphasizing on the challenges associated with composed image retrieval that needs understanding of both visual and textual data. To address data scarcity in CIR, the authors introduce a new task paradigm named "zero-shot composed image retrieval" (ZSCIR) that transforms image retrieval to a text-to-image format, allowing for a more intuitive mapping between images and descriptive text. However, the methods presented face challenges with large-scale models which are not suitable for deployment on resource-constrained platforms, such as mobile devices. To mitigate this, the authors propose an asymmetric approach, termed Image2Sentence based Asymmetric ZSCIR, that uses different models for query and database extraction. This method utilizes a lightweight model for the user's device and a heavier model for cloud processing. The core of this approach is an adaptive token learner which converts visual features into textual tokens, thus enhancing the representation. The proposed framework was tested on various benchmarks, demonstrating its efficiency and effectiveness compared to existing state-of-the-art methods.

### Strengths
1. The paper addresses the challenges in Composed Image Retrieval by introducing the zero-shot composed image retrieval (ZSCIR). This method offers a fresh perspective on image retrieval by transforming it to a text-to-image format, thereby providing a more direct linkage between descriptive text and its corresponding image.

2. The introduction of an adaptive token learner, which effectively translates visual features into textual tokens, stands out as a major strength. This conversion mechanism is pivotal in enhancing the representation of images and ensuring that the retrieval process is both accurate and efficient. The adaptive nature of the learner means that it can adjust and improve over time, potentially leading to even better retrieval results in the future.

### Weaknesses
1. While the adaptive token learner is a strength in terms of converting visual features to textual tokens, there's a risk that the system could become overly reliant on this component. If the learner fails or encounters unanticipated scenarios, it might compromise the effectiveness of the entire retrieval process. Specifically, the paper does not discuss the sensitivity of the token learner to variations in image quality, such as blur, noise, or changes in lighting conditions. It is unclear how the system would perform if the visual features extracted are not representative of the image's content due to these factors.

2. Introducing an asymmetric text-to-image retrieval approach, while innovative, adds an extra layer of complexity to the system. This might present challenges in terms of maintainability, debugging, and further development of the system. The paper does not provide a detailed analysis of the computational overhead associated with maintaining two separate models (one lightweight for the query and one heavier for the database). It also lacks a discussion on the potential for increased latency or synchronization issues between these models.

3. The transformation of the retrieval problem from image-to-image to text-to-image inherently assumes that the descriptive texts are of high quality and detailed. Any inaccuracies or vagueness in the text could lead to inefficient or incorrect image retrievals. The paper does not address how the system handles ambiguous or poorly worded text descriptions. For example, if a user provides a very general description, it is unclear how the system would prioritize relevant images or if it would return a large set of potentially irrelevant results.

4. The paper presentation is not very attractive. It is difficult to understand the novelties / contributions after reading the introduction of the paper.

### Questions
1.  How does the ZSCIR approach compare in performance and efficiency with state-of-the-art image retrieval methods that don't employ a text-to-image asymmetry? Are there scenarios where a traditional symmetric approach might outperform ZSCIR?

2. In terms of training data apart from the image augmentation, did you employ any data augmentation techniques to enhance the performance and robustness of the ZSCIR model? Furthermore, how did you ensure the diversity and representativeness of the descriptive texts used in the system?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces an asymmetric zero-shot composed image retrieval framework. The asymmetric retrieval pipeline is established using a lightweight model for query images and a large foundation model for gallery images, enabling feature extraction. Composed image retrieval is achieved by concatenating the sentence representation mapped from the image with a text modifier. To align the features extracted by the lightweight model and the large foundation model, two techniques, namely global contrastive distillation and local alignment regularization, are proposed. Extensive experiments and an ablation study conducted on benchmark datasets have demonstrated the effectiveness of the proposed method.

### Strengths
1. An asymmetric zero-shot composed image retrieval framework is proposed. 
2. Global contrastive distillation and local alignment regularization techniques are proposed to align features from different models.
3. Extensive experiments are conducted.

### Weaknesses
1. The clarity of the writing, particularly in the methods section, requires improvement.

2. For image-only retrieval, could you provide results using the DINO-V2 and MoCo-V3 pretrained models? The CLIP model is typically used for content matching between image and text features.

### Questions
t-SNE visualizations could be shown to illustrate the differences between the different methods. This would provide a more intuitive understanding of the feature distributions and separability.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper aims at the task of composed image retrieval (CIR) which retrieves images by providing a multimodal query such as a query image and additional text which describes the user's further query intention. Usually, such task is resolved by aligning the multimodal query and gallery features with vision-and-language pretraining and finetuning techniques. The authors argue that existing methods are not feasible to mobile applications due to expensive computational costs by forwarding large multimodal foundation models on mobile devices. The proposed solution is adopting a lightweight model to process the query while still maintaining the large foundation model for the gallery side. In order to bridge the representation gap between the lightweight and large model, the adaptive token learner is proposed to map an image to a sentence in the language model space. Finally, the authors verify their contributions on three evaluation benchmarks.

### Strengths
[1] Overall, this paper is well written and easy to follow. 

[2] I like the motivation of this work since deploying original large foundation model is almost impossible in mobile applications. Different from pruning or distilling such heavy models, the authors proposed the lightweight encoder with a tunable adaptive token learner. The idea behind is borrowed from the LLM-Adapters. 

[3] The proposed modules are technically sound and the experimental resutls are sufficient. The training resources are extremly friendly with 4 RTX 3090 GPUs.

### Weaknesses
[1] Since this work is a retrieval task, it is important to report how the retrieval performance varies as the gallery size scales up. I understand that the three evalutation datasets are standard benchmarks. However, it would make the contribution more solid if millions distractors could be involved in the gallery, although most existing SOTAs didn't report such results. Specifically, the impact of gallery size on both retrieval accuracy and computational cost should be analyzed. The paper should include experiments with varying gallery sizes, perhaps from the original dataset size up to a million distractors, to demonstrate the scalability of the proposed method. This is crucial for real-world applications where the gallery size can be substantial.

[2] The inference time should be reported including in the query side and in the cloud side. It's critical to understand the latency introduced by both the lightweight query model and the large gallery model. The paper should provide a breakdown of the inference time for each component, including the time taken for feature extraction on the query side and the time for similarity calculations on the server side. This will help assess the practical feasibility of the proposed approach in real-time applications.

[3] Some minor issues are listed in the next part.

### Questions
[1] Figure 1 could be further improved. Specifically, the pink rectangle and trapezoid could be shrunk and the blue trapezoids could be enlarged. As a result, it is much easier to quickly grasp the idea at first glance for readers. 

[2] Table 5 provides a viriant mapping network which is actually a MLP. Are there other options?

[3] Figure 3 reveals a fact that larger token lengths could degrade the retrieval performance. The authors attribute such fact to the background noise or the trivial patterns. Are there any deeper insights or visualization analysis?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
