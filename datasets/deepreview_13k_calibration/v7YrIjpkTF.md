# Multimodal Quantitative Language for Generative Recommendation

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Generative recommendation has emerged as a promising paradigm aiming at directly generating the identifiers of the target candidates.
Most existing methods attempt to leverage prior knowledge embedded in Pre-trained Language Models (PLMs) to improve the recommendation performance. However, they often fail to accommodate the differences between the general linguistic knowledge of PLMs and the specific needs of recommendation systems. Moreover, they rarely consider the complementary knowledge between the multimodal information of items, which represents the multi-faceted preferences of users.  To facilitate efficient recommendation knowledge transfer, we propose a novel approach called Multimodal Quantitative Language for Generative Recommendation (MQL4GRec). Our key idea is to transform items from different domains and modalities into a unified language, which can serve as a bridge for transferring recommendation knowledge. Specifically, we first introduce quantitative translators to convert the text and image content of items from various domains into a new and concise language, known as quantitative language, with all items sharing the same vocabulary. Then, we design a series of quantitative language generation tasks to enrich quantitative language with semantic information and prior knowledge.  Finally, we achieve the transfer of recommendation knowledge from different domains and modalities to the recommendation task through pre-training and fine-tuning. We evaluate the effectiveness of MQL4GRec through extensive experiments and comparisons with existing methods, achieving improvements over the baseline by 11.18\%, 14.82\%, and 7.95\% on the NDCG metric across three different datasets, respectively. Our implementation is available at: \href{https://anonymous.4open.science/r/QL4GRec-ED65/}{\textcolor{blue}{https://anonymous.4open.science/r/MQL4GRec-ED65/}.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper titled "Multimodal Quantitative Language for Generative Recommendation" introduces a novel approach to enhance generative recommendation systems by converting item content from multiple domains and modalities into a unified "quantitative language". This methodology seeks to bridge the gap between the generalized linguistic knowledge of pre-trained language models (PLMs) and the specialized needs of recommendation systems. The authors developed a new framework, MQL4GRec, which employs "quantitative translators" to convert textual and visual item data into a shared vocabulary. This shared language is then enriched with semantic information through various generation tasks to enable effective knowledge transfer from multimodal data to recommendation systems.

The paper's main contribution lies in its innovative method of integrating multimodal data to improve recommendation performance significantly, surpassing baseline methods by notable margins in terms of the NDCG metric across multiple datasets. Furthermore, the framework introduces a potential shift towards more universal recommendation systems that do not rely on traditional item IDs, thereby addressing common challenges like improving scalability and transferability across different domains.

### Strengths
1. The approach to transform diverse item content from different domains and modalities into a unified quantitative language is highly innovative. This integration allows for a more robust and versatile recommendation system that can handle varied inputs effectively.

2. The paper introduces a well-structured design of pre-training and fine-tuning tasks that includes not only generative prediction but also alignment tasks, enhancing the robustness of the method. This comprehensive approach allows the model to effectively leverage both generative capabilities and alignment strategies to improve overall recommendation accuracy.

3. The proposed framework significantly outperforms existing models on several benchmark datasets, particularly in terms of the NDCG metric. This suggests that the method is not only theoretically sound but also practically effective.

### Weaknesses
1. The paper does not discuss the impact of various training operations on the algorithm's time complexity, such as the handling of collisions. Specifically, the computational cost of the vector quantization process, including the number of layers and nodes in the MLP, is not analyzed in relation to the overall training time. Furthermore, the paper lacks a detailed discussion of how the collision resolution strategy affects the efficiency of the model, particularly in scenarios with a high density of collisions. This oversight might leave questions about the scalability and efficiency of the proposed method in practical applications, especially when dealing with large datasets.

2. The methodology section lacks a clear explanation of how the generated quantitative vectors are used to retrieve corresponding items during the next item generation task. It is unclear how the model maps the generated tokens back to the original items, and the paper does not provide sufficient detail on the data structures or algorithms used for this mapping. This omission could lead to ambiguity regarding the operational specifics of the model, making it difficult to reproduce or extend the work.

3. The model does not utilize multimodal information simultaneously to predict the next click item, which limits the paper's innovativeness and potential for expansion. The paper does not explore the potential benefits of fusing visual and textual information at the input level of the transformer model. This limitation restricts the model's ability to capture complex relationships between different modalities, which could lead to suboptimal performance in scenarios where multimodal context is crucial.

### Questions
1. How do different training operations, such as collision handling and quantization, impact the computational time and resource requirements of the model?

2. What methods or algorithms are employed to map these quantitative vectors back to specific items in the dataset?

3. Why does the model not use multimodal information simultaneously to predict the next click item? What are the challenges or limitations that prevent this integration?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
MQL4GRec introduces a novel approach for generative recommendation by transforming multimodal content from different domains into a unified "quantitative language," facilitating cross-domain knowledge transfer in recommendation tasks. The method uses quantitative translators for text and image content, building a shared vocabulary to encode semantic information across modalities. A series of language generation tasks further enriches this vocabulary, enhancing the model's capacity to represent multi-faceted user preferences. Experimental results demonstrate notable performance improvements over baseline models on key metrics across multiple datasets, showcasing MQL4GRec's scalability and potential in multimodal recommendation.



However, its innovation appears limited, closely resembling existing methods like GenRet and MMGRec in both tokenization approach and generative structure.

### Strengths
1. Innovation: The proposed MQL4GRec method translates content from different modalities into a unified “quantitative language,” enabling cross-domain and cross-modal recommendation knowledge transfer. This approach addresses limitations in handling multimodal data in existing generative recommendation models.


2. Superior Performance: Experimental results on multiple public datasets demonstrate that MQL4GRec outperforms baseline methods on key metrics such as NDCG.



3. Open-Source Availability: The paper provides a fully accessible code repository, facilitating reproducibility and further research within the community.

### Weaknesses
1. Similarity to Existing Tokenization Approaches
- The unified vocabulary for multimodal information closely resembles the generative retrieval tokenization approach found in "Learning to Tokenize for Generative Retrieval," [1]  particularly the "GenRet" model, which uses discrete auto-encoding for compact identifiers. This "multimodal codebook" seems to be an adaptation of single-modality tokenization, relying on established techniques like RQ-VAE and offering only incremental improvements without substantial architectural or performance innovation. Specifically, the method appears to directly apply RQ-VAE to each modality independently before concatenating the resulting codes, which lacks a mechanism for cross-modal interaction during the tokenization process. This approach may limit the model's ability to capture complex interdependencies between modalities.
- The motivational structure and initial figures in MQL4GRec are closely aligned with those in GenRet, which may diminish the perceived originality of the proposed approach.


2. Lack of Comparative Analysis
-  MQL4GRec’s generative approach appears heavily inspired by MMGRec [2], which also employs Graph RQ-VAE for multimodal representation through user-item interactions, raising concerns about the uniqueness of MQL4GRec’s contributions. The paper does not adequately address how MQL4GRec's tokenization method differs from MMGRec's Graph RQ-VAE, particularly in how it handles multimodal information and user-item interactions. Both methods use a form of vector quantization, but the specific differences in their application and impact on performance are not clearly delineated.
- The paper does not clearly distinguish MQL4GRec's advancements over MMGRec, especially in terms of multimodal token-based representations. A more thorough comparison is needed to establish any unique contributions beyond MMGRec’s existing framework.

The paper does not clearly distinguish MQL4GRec's advancements over MMGRec, especially in terms of multimodal token-based representations. A more thorough comparison is needed to establish any unique contributions beyond MMGRec’s existing framework.

### Questions
- User ID Collision: With only 2000 tokens representing a large user base, there is a potential for ID collisions, which may lead to inaccuracies in recommendation results in real-world applications.
   - Domain Adaptability: The model performs poorly on certain domain-specific datasets, such as the Games dataset, suggesting limitations in domain transferability.

### Soundness
3

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
4

### Summary
This paper presents a novel multimodal generative recommendation method, MQL4GRec, which facilitates the effective transfer of recommendation knowledge by converting item content from different domains and modalities into a unified quantitative language. Specifically, MQL4GRec introduces a unified quantitative language representation to handle multimodal content, including text and images. Additionally, a series of quantitative language generation tasks are designed to enrich the semantic representation. Extensive experiments across three datasets show that this method significantly outperforms baseline approaches.

### Strengths
* High Innovation: This work is the first to propose using a unified quantitative language to address knowledge transfer in multimodal recommendation, which is highly valuable for enhancing the generalization ability of recommendation systems.

* Thorough Experimental Validation: The paper conducts extensive experiments across three datasets, showcasing not only the overall performance of the method but also analyzing the role of individual components through ablation studies, indicating rigorous experimental design.

### Weaknesses
 * The model's high complexity poses significant computational and storage demands, which could lead to considerable costs in real-world deployment.


### Questions
* Figure 3 shows that the performance on the Games dataset slightly declines as the amount of pre-training data increases. Does this suggest that the pre-training strategy has limitations when applied to domains with substantial cross-domain differences?

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
This paper introduces a novel approach, MQL4GRec, designed to convert item content from diverse domains and modalities into a unified quantitative language.

### Strengths
1. The proposed concept of a multimodal quantitative language, together with the design of quantitative language generation tasks, represents a novel and innovative advancement in the field of generative recommendation

2.  The architecture design is elegant, presenting the idea in a straightforward way, yet experiments demonstrate its strong effectiveness. I personally appreciate this type of work and believe it can make a meaningful impact in the field of generative recommendation.

3. The availability of the code significantly enhances reproducibility.

### Weaknesses
1.The proposed framework is rooted in the generative recommendation paradigm and aligns with a preprint in a similar research direction [1]. However, it still represents a valuable contribution in my view, even if not groundbreaking.

2.The authors should consider testing the statistical significance of MQL4GRec results.

3.There remains a limitation in zero-shot capability, which is a known challenge in the field of recommendation.

4.To enhance the comprehensiveness of the "Multi-modal Recommendation" section in the related work, the authors could consider including more recent state-of-the-art multimodal recommender system papers, such as [2,3]. The field of multimodal codebooks from other communities should also be included in the related work section to clarify the distinctions between the proposed MQL approach and existing methods, such as those in [4, 5]

### Questions
1.As an efficient framework, I am interested in understanding the training costs of MQL4GRec compared to other baselines. Specifically, how does it perform in terms of training time, VRAM usage, and inference time?

2.In the field of recommender systems, there is a lack of widely recognized pre-trained models. Could MQL4GRec potentially serve as a foundation model for other downstream tasks?

My concerns are addressed by the authors, therefore, I will raise my scores from 6 to 8.

### Soundness
2

### Presentation
4

### Contribution
4
