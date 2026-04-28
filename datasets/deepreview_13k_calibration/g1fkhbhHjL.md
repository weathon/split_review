# Black Sheep in the Herd: Playing with Spuriously Correlated Attributes for Vision-Language Recognition

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8

## Abstract
Few-shot adaptation for Vision-Language Models (VLMs) presents a dilemma: balancing in-distribution accuracy with out-of-distribution generalization. Recent research has utilized low-level concepts such as visual attributes to enhance generalization. However, this study reveals that VLMs overly rely on a small subset of attributes on decision-making, which co-occur with the category but are not inherently part of it, termed spuriously correlated attributes. This biased nature of VLMs results in poor generalization. To address this, 1) we first propose Spurious Attribute Probing (SAP), identifying and filtering out these problematic attributes to significantly enhance the generalization of existing attribute-based methods; 2) We introduce Spurious Attribute Shielding (SAS), a plug-and-play module that mitigates the influence of these attributes on prediction, seamlessly integrating into various Parameter-Efficient Fine-Tuning (PEFT) methods. In experiments, SAP and SAS significantly enhance accuracy on distribution shifts across 11 datasets and 3 generalization tasks without compromising downstream performance, establishing a new state-of-the-art benchmark.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
1. [Summary]
This paper focuses on Parameter-Efficient Fine-Tuning for vision language models. It discovers a group of black sheep, i.e., spurious attributes, on which VLMs inherently heavily rely, thereby leading to poor generalization and robustness. It introduces SPURIOUS ATTRIBUTE PROBING (SAP), aiming to identify and eliminate these problematic attributes, thereby improving the generalization of current attribute-based methods. Besides, it presents SPURIOUS ATTRIBUTE SHIELDING (SAS), a plug-and-play module seamlessly integrating into various PEFT methods to mitigate the influence of spurious attributes on predictions. Experiments show that the proposed method achieves good performances.
2. [Strengths]
- a. It proposes SPURIOUS ATTRIBUTE PROBING (SAP) and SPURIOUS ATTRIBUTE SHIELDING (SAS), which enhance the generalization of existing attribute-based methods is complementary to PEFT methods. 
- b. The experiments are extensive, and the performance of the proposed method is promising.
- c. The method is efficient, intuitive and effective.
3.1 [Reasons to Reject]
Although this paper is well written with comprehensive evaluation and good results, there are still some issues.
Several parts of this paper are not very clear and need further clarification. Please check the questions.
In addition, some key related VLM works are missed. Please check the questions.
3. [Weaknesses] 
1. Fair comparison issue. It is not clear whether the performance gains come from involving additional training data as illustrated in Figure 2 (a) and (b) or the designed methods. What if the compared methods also involve the additional data in training? And how about the performance then? It seems that the performance gains are largely attributed to the additional training data. It would be better to add some additional ablation studies to address this concern.
2. The core idea of this paper is to introduce attribute information (e.g., objects, parts and subparts) into vision-language model to enhance object recognition. The related works [A, B, C] are missed. Similarly, [A, B, C] enhance object recognition performance by introducing the additional information like multi-granularity object class information and hierarchical object class information. It would be better to discuss and highlight the similarity and difference between this paper and [A, B, C]. 
[A] Adversarial fine-grained composition learning for unseen attribute-object recognition
[B] Open-Vocabulary Object Detection via Language Hierarchy
[C] Multiple granularity descriptors for fine-grained categorization

3. The paper method relies on constructing pseudo categories via generating or retrieving, which shares similar idea with the concept of retrieval-augmented generation (RAG). It would be better to discuss and clarify the similarity and differences with RAG, for example, RAG for object recognition as in [D].
[D] Retrieval augmented classification for long-tail visual recognition.
4. As the objective of this paper is to enhance vision-language models, it would be better to test/verify the proposed method on multiple vision-language models in addition to CLIP. Besides, the Section 2 Related Work missing an important paragraph of “Vision-language model.”. It would be better to add a new paragraph in the Section 2 Related Work to introduce background and related papers of VLM and cite the survey [E] which could be a good reference for new readers that are not very familiar with recent progresses in VLM.
[E] Vision-language models for vision tasks: A survey


4. Conclusion
Overall, this work proposes to introduce attribute information into VLM to enhance object recognition performance with good performance gains. However, there are some details that need to be clarified, as listed in the questions. I would upgrade the score if the questions are well addressed.

### Strengths
as shown in Summary

### Weaknesses
1. Fair comparison issue. It is not clear whether the performance gains come from involving additional training data as illustrated in Figure 2 (a) and (b) or the designed methods. What if the compared methods also involve the additional data in training? And how about the performance then? It seems that the performance gains are largely attributed to the additional training data. It would be better to add some additional ablation studies to address this concern.
2. The core idea of this paper is to introduce attribute information (e.g., objects, parts and subparts) into vision-language model to enhance object recognition. The related works [A, B, C] are missed. Similarly, [A, B, C] enhance object recognition performance by introducing the additional information like multi-granularity object class information and hierarchical object class information. It would be better to discuss and highlight the similarity and difference between this paper and [A, B, C]. 
3. The paper method relies on constructing pseudo categories via generating or retrieving, which shares similar idea with the concept of retrieval-augmented generation (RAG). It would be better to discuss and clarify the similarity and differences with RAG, for example, RAG for object recognition as in [D].
4. As the objective of this paper is to enhance vision-language models, it would be better to test/verify the proposed method on multiple vision-language models in addition to CLIP. Besides, the Section 2 Related Work missing an important paragraph of “Vision-language model.”. It would be better to add a new paragraph in the Section 2 Related Work to introduce background and related papers of VLM and cite the survey [E] which could be a good reference for new readers that are not very familiar with recent progresses in VLM.

### Questions
as shown in Summary

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper aims to address the issue of VLMs overly relying on a small subset of attributes in decision-making due to spuriously correlated attributes. The paper proposes SAP to identify and filter out spurious attributes to enhance the generalization of existing attribute-based methods. In addition, a plug-and-play module SAS that integrates into various Parameter-Efficient Fine-Tuning (PEFT) methods is designed to reduce the influence of spurious attributes on predictions. The experiments demonstrate that SAP and SAS significantly improve accuracy on distribution shifts across 11 datasets and 3 generalization tasks without compromising downstream performance.

### Strengths
- Novelty: The paper reveals the impact of spuriously correlated attributes on the predictions of Vision-Language Models and proposes innovative methods (SAP and SAS) to tackle the problem of spurious correlations in VLMs

- Performance & Experiments: The proposed methods achieve state-of-the-art results across 11 datasets and 3 generalization tasks, enhancing the accuracy of VLMs on distribution shifts without sacrificing performance on downstream tasks. The figures of results effectively express the intended meaning and support the conclusions, as illustrated in Figure 3.

- Presentation: The writing is fluent and understandable.

### Weaknesses
 - Does the construction of pseudo categories using the synthetic method result in additional computational costs? And have any experiments been conducted to validate the computational efficiency of this method? Additionally, could you provide some analysis of the inference time based on GPT and diffusion-related methods?
- The paper primarily focuses on vision-language recognition. Could the proposed method generalize to other modalities (such as video) or tasks (such as language reasoning) outside of this specific task in this paper?

### Questions
- Will the code be made publicly available for community use?

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
5

### Summary
This paper investigates how spuriously correlated attributes can lead to poor generalization in Vision-Language Models (VLMs). To address this issue, the authors propose the SAP method for identifying and filtering out problematic attributes, thereby enhancing existing attribute-based methods. They also introduce a plug-and-play SAS module to mitigate these attributes' influence on prediction. Experiments are conducted on standard benchmark datasets.

### Strengths
1. Researching spuriously correlated attributes in VLMs is a less explored yet intriguing direction.
2. The method of identifying spuriously correlated attributes is both reasonable and effective.
3. The SAS module can be integrated with existing methods to validate its generalization capability.

### Weaknesses
1. Most existing attribute-based methods are zero-shot, whereas the attribute filtering in this paper appears to require a few labeled training images. This raises concerns about whether comparing it to zero-shot attribute-based methods is fair.
2. Some of the latest methods in VLM adaptation have not been discussed. For example, [1,2], which explore VLM adaptation tasks from new perspectives, should be included in the discussion. It would be beneficial to verify the complementarity of the proposed method with these new approaches.


### Questions
See weaknesses.

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
2

### Summary
This paper proposes a new adaptation strategy for improving the generalization of attribute-based VLM recognition methods. The authors assess the detrimental impact of spurious attribute on adapting to novel domains, and propose spurious attribute probing and shielding strategies to mitigate this influence. By learning a subsidiary task to discriminate target categories and spurious attribute categories, the adaptation performance on out-of-distribution data is notably improved.

### Strengths
1.The motivation of this paper appears interesting to me. The authors quantitively identify the influence of spurious attributes,  a key problem for out-of-distribution visual recognition.

2.The idea of learning pseudo category to mitigate the impact of spurious attribute is novel. The proposed SAS and SAP bring consistent improvement across 10 baselines, demonstrating the method’s effectiveness.

3.The paper is well-written, well-organized and easy to follow.

### Weaknesses
1.During fine-tuning, differentiating each category from the synthetic pseudo category is time-consuming and tedious. Although the authors apply selective optimization to maintain overall performance，they have not fundamentally addressed the prolonged optimization time for each category.

2.Only three visualization figs are presented in Figure 5, and the results can not effectively demonstrate the removal of attention to spurious attribute features, e.g., Figure 5 (b).

3.During training, an additional module generates negative samples to form a strong contrast from the target categories. There’s a possibility that the performance improvement is primarily attributed to data augmentation, as the authors also mentioned in the paper. However, the authors do not compare the performance when generating an equivalent number of positive samples for each target category.

### Questions
1.It is advisable to provide more visualization examples in Figure 5 or in supplementary materials.

2.Can you provide an ablation study of the performance when generating an equivalent number of positive samples for each category?

### Soundness
3

### Presentation
4

### Contribution
3
