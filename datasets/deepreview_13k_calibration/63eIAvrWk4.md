# Leveraging One-To-Many Relationships in Multimodal Adversarial Defense for Robust Image-Text Retrieval

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5

## Abstract
Large pre-trained vision-language models (e.g., CLIP) are vulnerable to adversarial attacks in image-text retrieval (ITR). Existing works primarily focus on defense for image classification, overlooking two key aspects of ITR: multimodal manipulation by attackers, and the one-to-many relationship in ITR, where a single image can have multiple textual descriptions and vice versa (1:N and N:1). 
This is the first work that explores defense strategies for robust ITR. 
We demonstrate that our proposed multimodal adversarial training, which accounts for multimodal perturbations, significantly improves robustness against multimodal attacks; however, it suffers from overfitting to deterministic one-to-one (1:1) image-text pairs in the training data.
To address this, we conduct a conprehensive study on leveraging one-to-many relationships to enhances robustness, investigating diverse augmentation techniques.
Our findings reveal that diversity and alignment of image-text pairs are crucial for effective defense.
Specifically, text augmentations outperform image augmentations, which tend to create either insufficient diversity or excessive distribution shifts. 
Additionally, we find that cross-modal augmentations (e.g., $image \rightarrow text$) can outperform intra-modal augmentations (e.g., $text \rightarrow text$) due to generating well-aligned image-text pairs.
In summary, this work pioneers defense strategies for robust ITR, identifying critical aspects overlooked by prior research, and offers a promising direction for future studies.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This research introduces novel defense strategies for Image-Text Retrieval (ITR) by addressing the limitations of existing methods tailored for image classification. A pioneering approach is demonstrated, emphasizing the significance of multimodal adversarial training in enhancing the robustness of ITR systems against diverse attacks. Furthermore, a comprehensive analysis of leveraging one-to-many relationships is conducted, revealing the efficacy of diverse augmentations across image and text modalities for bolstering the resilience of ITR models.

### Strengths
1.This research pioneers a new direction in defense strategies for ITR, highlighting the inadequacies of conventional image classification defense methods.
2.The introduction of multimodal adversarial training significantly improves the robustness of ITR systems.
3.This study offers an in-depth analysis of leveraging one-to-many relationships
4.Well-written and easy to read.

### Weaknesses
1. Both the selection of datasets and the methodological exposition in this work are relatively weak and lack persuasiveness. It is suggested that the authors should not confine themselves to COCO and Flickr datasets but also test on more diverse datasets, such as remote sensing scenes, to thoroughly validate the generalizability of the proposed method. Furthermore, the introduced method lacks sufficient theoretical justification.
2. The ablation experiments are too simplistic; at the very least, different visual-language foundation models should be subjected to ablation analysis.

### Questions
1. Can the proposed method be extended to tasks at a finer granularity, such as VL segmentation and detection?
2. Since text augmentation is superior to image augmentation, is there a similar conclusion for the audio modality as well?
3. Since the author mentioned a one-to-many strategy, what about many-to-many strategies, such as [1]?

[1]. Leveraging Many-To-Many Relationships for Defending Against Visual-Language Adversarial Attacks, arXiv 2024

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper explored adversarial attack and defense for image-text retrieval (ITR) using vision-language models. It proposed Multimodal Augmented Adversarial Training (MA2T), using one-to-many relationships in image-text pairs to improve model robustness. The authors claimed improvements in adversarial robustness, especially when using text augmentations over image perturbations.

### Strengths
- An interesting problem of multimodal adversarial defense, particularly for ITR.
- The paper proposed a new defense strategy, MA2T, to improve robustness by incorporating multimodal adversarial training and augmentation.
- The paper conducted many experiments across multiple attack types, with detailed augmentation analysis.

### Weaknesses
 - It seems unclear why one-to-many augmentations should directly improve adversarial robustness in ITR, it would be good to add some theoretical explanations if possible. 
- Following the above, the selection choice, including the multimodal training setup, appears empirically driven without a theoretical basis.
- The paper used CLIP-ViT-B/16 as the base model and reported improvements in robustness metrics (e.g., 1.7%–8.7%). The authors should have realized that CLIP-ViT-B/16 is quite a small model, and the performance improvement on this may not be generalized to a larger model, which is said, the large model may already show much better adversarial robustness than the small model. So it is recommended to conduct a study on larger models to see the performance and the improvement gain compared with small models, 
- The paper only used a base model. Though many attacks have been studied, it seems unclear whether the proposed method only works on the models with architectures like CLIP or can be generalized to other model architectures. It is recommended that other model architectures be investigated as well. 
- Evaluations are limited to Flickr30k and COCO datasets. Existing studies have shown that Flickr is quite a simple dataset, so it is recommended that other, more complex datasets be explored.
- Some evaluations show selective use of augmented pairs, while others apply them inconsistently across attack types and scenarios. This inconsistency may lead to ambiguity around the robustness gains attributable to MA2T.

### Questions
Please see the comments above.

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
3

### Summary
This paper introduces Multimodal Augmented Adversarial Training (MA2T) to improve adversarial robustness in image-text retrieval (ITR). Extending beyond unimodal defenses, MA2T combines image and text perturbations and incorporates one-to-many and many-to-one augmentations to counteract overfitting and enhance multimodal resilience. Experiments on Flickr30k and COCO validate that MA2T improves robustness, especially with cross-modal augmentations.

### Strengths
The paper addresses adversarial robustness in image-text retrieval (ITR) by employing multimodal adversarial training alongside one-to-many and many-to-one augmentations. This approach leverages the multimodal characteristics of ITR data to enhance defenses against attacks. The experimental methodology is robust, featuring well-structured evaluations on Flickr30k and COCO, which illustrate the advantages of cross-modal augmentations. Overall, the work is clearly articulated, providing sufficient context and explanations, and is relevant for advancing robust vision-language models in the expanding field of multimodal research.

### Weaknesses
While the paper proposes a promising approach, several areas need improvement to strengthen claims of broader applicability and robustness. First, the experiments are limited to CLIP as the only vision-language model, which restricts conclusions about model generalizability. Evaluating the framework on additional models, such as BLIP or ALBEF, would provide a more thorough understanding of its robustness across various architectures. Additionally, the current augmentation strategy for image perturbations may introduce distribution shifts that could negatively affect performance. Specifically, the paper does not detail the types of image augmentations used, making it difficult to assess their potential impact on the feature space and how they might interact with adversarial perturbations. Finally, although the paper discusses the limitations of unimodal defenses in a multimodal context, a more comprehensive theoretical analysis of why cross-modal augmentations specifically enhance ITR robustness is warranted. The paper lacks a formal definition of what constitutes a 'good' cross-modal augmentation and how it relates to the underlying geometry of the multimodal embedding space.

### Questions
Since the framework is tested solely on CLIP, do the authors foresee challenges in adapting MA2T to other vision-language models, such as BLIP or ALBEF?

The paper notes that image augmentations may introduce distribution shifts that could affect performance. Have the authors investigated alternative augmentation techniques or constraints to mitigate this impact?

Minor issue:
Some Grammatical mistakes are there – like “conprehensive” instead of “comprehensive” [line 021]. “mutlimodal” instead of “multimodal” [line 225]. A thorough proofreading will be helpful.

### Soundness
3

### Presentation
2

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
This paper proposes a new defense framework, Multimodal Augmented Adversarial Training (MA2T), designed to enhance robustness in image-text retrieval tasks within vision-language models. MA2T is tailored for the CLIP model, leveraging one-to-many (1:N) image-text pairing and data augmentation to reduce the impact of multimodal adversarial attacks. This approach significantly improves model robustness on datasets such as Flickr30k and COCO.

### Strengths
1.	The authors are the first to propose a multimodal adversarial training method for ITR tasks, filling the research gap left by image-only defenses.
2.	Through an in-depth exploration of one-to-many relationships, the authors validate the effectiveness of various augmentation strategies, including text and image augmentation as well as cross-modal and unimodal augmentations.
3.	The experiments of the work show the operations make sense, and proposing data augmentation methods suitable for different tasks.
4.	The proposed framework can adapt to various real-world scenarios, providing a reference for AI security research.

### Weaknesses
1.	The experiments rely primarily on the Flickr30k and COCO datasets, lacking tests on other, more diverse real-world datasets. While these datasets are commonly used, their image and text content may not fully represent the complexity of real-world scenarios, potentially limiting the generalizability of the findings. The reliance on these datasets might not expose the model to the full range of adversarial attacks it could encounter in practical applications.
2.	The framework is only tested on the CLIP model, without validation on other vision-language models, such as BLIP, to assess generalizability. This narrow focus limits the understanding of how well the proposed defense would perform on different model architectures and pre-training strategies. The effectiveness of the approach might be highly dependent on the specific characteristics of CLIP, and it is unclear if the observed robustness gains would translate to other vision-language models.
3.	There is a typo in the tenth line of the abstract; it seems the authors likely meant to write “comprehensive” rather than “conprehensive.”
4.	The paper lacks a clear framework diagram or visual results that would make the contributions of this work immediately understandable. The absence of a visual representation of the proposed framework makes it difficult to grasp the overall architecture and the flow of information, hindering the reader's ability to quickly understand the method.

### Questions
1.	This paper lack a framework diagram, which limits its readability.
2.	In Table 3, the focus is mainly on comparing different augmentation strategies,  comparisons with other existing multimodal adversarial training methods are require.
3.	Why select Flickr30k and COCO datasets, it seems that the scenes in these two datasets are relatively limited?

### Soundness
2

### Presentation
2

### Contribution
2
