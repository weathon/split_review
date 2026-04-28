# Sparsely multimodal data fusion

- Decision: Reject
- Avg Score: 4.80
- Scores: 5, 3, 5, 6, 5

## Abstract
Multimodal data fusion is essential for applications requiring the integration of diverse data sources, especially in the presence of incomplete or sparsely available modalities. This paper presents a comparative study of three multimodal embedding techniques, Modal Channel Attention (MCA), Zorro, and Everything at Once (EAO), to evaluate their performance on sparsely multimodal data. MCA introduces fusion embeddings for all combinations of input modalities and uses attention masking to create distinct attention channels, enabling flexible and efficient data fusion. Experiments on two datasets with four modalities each, CMU-MOSEI and TCGA, demonstrate that MCA outperforms Zorro across ranking, recall, regression, and classification tasks and outperforms EAO across regression and classification tasks. MCA achieves superior performance by maintaining robust uniformity across unimodal and fusion embeddings. While EAO performs best in ranking metrics due to its approach of forming fusion embeddings post-inference, it underperforms in downstream tasks requiring multimodal interactions. These results highlight the importance of contrasting all modality combinations in constructing embedding spaces and offers insights into the design of multimodal architectures for real-world applications with incomplete data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a method called Modal Channel Attention (MCA) to enhance masked multimodal transformer models for learning from multimodal data, even in the presence of missing modalities. The approach extends existing masked multimodal attention (MMA) by incorporating channels for incomplete modalities, which significantly improves the quality of learned embeddings.

### Strengths
1. It addresses the challenge of missing modalities.

2. It extends the masked multimodal attention (MMA), improving its capability to handle incomplete data.

3. Improves the quality of learned embeddings.

### Weaknesses
1. The contributions primarily emphasize performance improvements and extensions to the existing MMA. More detailed explanations of the specific contributions and the importance of the novelty would be beneficial. 

2. The technical section is quite brief (half a page), and it would be helpful if the figure showing the architecture and self-attention provided more detail. Moreover, part of the technical section is devoted to describing the architecture by listing details like activations, hidden size, and the number of attention heads. However, no explicit motivations are provided for these choices. Additionally, the figures should have been more curated to avoid text pixelation. Given the current shape of the paper, the novelties seem to be present, but the paper fails to properly highlight them, relying mostly on an empirical evaluation.

### Questions
The paper suggests novel contributions, but they are not sufficiently highlighted. Can you expand on how MCA distinguishes itself from existing methods in terms of theoretical innovations or novel mechanisms, beyond empirical performance? Providing explicit motivations for architectural choices would also make the contributions clearer and more impactful.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper is not ready for publication in ICLR

### Strengths
The topic is very interesting and important.

### Weaknesses
The presentation is poor. The manuscript lacks clear explanations of the core methodology, making it difficult to assess the novelty and significance of the proposed approach. The figures are low-resolution and do not effectively illustrate the key concepts or experimental results. The writing is often vague and lacks the necessary detail to reproduce the experiments. The overall structure of the paper is disorganized, making it hard to follow the logical flow of the arguments.

### Questions
No

### Soundness
1

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
**Summary of this paper:**

This work proposes an extension to the masked multimodal transformer model which incorporates modal-incomplete channels in the multihead attention mechanism called modal channel attention (MCA).

**Strengths:**

1.	This paper addresses an interesting problem by extending the masked multimodal attention model architecture to work with modality-incomplete datasets, a common scenario in real-world applications.

2.	The paper is straightforward.
 
3.	Experimental results demonstrate the effectiveness of the proposed method.

**Weakness:**

There is no visual comparison between the proposed architecture and previous structures, which would help clarify the improvements and differences.

**Comments, Suggestions And Typos:**

1.	It is recommended to add a figure in the introduction to briefly introduce the task of this paper, or to add a figure somewhere to compare the proposed model architecture with previous MMA architecture.

2.	Figure 1 is not good-looking, the authors are encouraged to improve the quality of the figure.

3.	For clarity and rigor, it is recommended to express important definitions or functions (i.e., modal sparsity) by formulas.

4.	The citation formats for figures differ in this paper.

### Strengths
Refer to the summary

### Weaknesses
There is no visual comparison between the proposed architecture and previous structures, which would help clarify the improvements and differences.



### Questions
Refer to the summary

### Soundness
3

### Presentation
2

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
Traditional multimodal learning methods often assume that all modes are uniformly present in training and reasoning, which may be impractical in practical applications. To solve this problem, the authors propose a modal channel attention (MCA) model, which is an extension of the masked multimodal attention (MMA) approach. By integrating a dedicated attention mechanism, MCA achieves efficient fusion and embedding of multimodal data, even in the case of sparse modes. We evaluate MCA on the CMU-MOSEI and TCGA datasets, and the results show that MCA outperforms MMA in creating aligned, uniform embeddings with different modal sparsity. In downstream tasks such as multimodal sentiment analysis and tumor type prediction, MCA also shows higher recall rates and classification/regression performance, making it a versatile tool for real-world multimodal data fusion.

### Strengths
1. MCA provides a novel method for dealing with modal sparsity in multimodal transformers, addressing a common limitation in multimodal learning. The approach enhances the MMA model by adding a modality-aware attention channel, innovatively allowing robust embedding creation from incomplete datasets.
2. The study is rigorous, using two datasets (CMU-MOSEI and TCGA) to evaluate the model's effectiveness across varied tasks, including sentiment analysis and cancer classification. The experiments are thorough, with evaluations under multiple levels of modal sparsity and comparisons with established models.
3. This model has important implications for real-world applications where complete multimodal data is often unavailable, such as in medical data analysis and surveillance systems. MCA enables more resilient model applications by tolerating missing modalities without significant loss of performance, thus broadening the scope of multimodal transformers.

### Weaknesses
1. This paper does not explore in depth the interactions between modes to further explore the specific impact of different combinations of modes on MCA model performance. You may wish to consider exploring whether particular combinations are more conducive to improving model performance in order to gain a fuller understanding of the relative importance of each mode. Specifically, the paper lacks an analysis of how the model performs when certain modalities are consistently present or absent, which could reveal underlying dependencies or biases in the fusion process. For example, does the model rely more heavily on certain modalities when others are missing, and how does this affect the quality of the final embedding?
2. Although MCA is described as an efficient solution, this paper does not further quantify its computational efficiency and resource consumption on larger or more complex datasets to effectively assess the feasibility of its practical application. The paper should include a detailed analysis of the computational cost of MCA, including training time, memory usage, and inference speed, especially when compared to the baseline MMA model. This analysis should also consider how these metrics scale with increasing dataset size and modality complexity.
3. The attention mechanism of the MCA model in dealing with missing modalities is still complex and not easy to understand intuitively. I would like to see the interpretability of the model in applications, which would help build user trust in the model's decisions. The paper should provide a more detailed explanation of how the attention mechanism handles missing modalities, perhaps through visualizations of attention weights or feature maps. It would also be beneficial to analyze the model's behavior when specific modalities are masked, to understand how the model compensates for the missing information.
4. The comparison experiments in this paper are limited to comparisons with the MMA model, which makes it difficult to fully demonstrate the relative strengths of the MCA model in multimodal approaches. You can evaluate the advantages and limitations of the MCA model more comprehensively by increasing the number of comparison experiments with multimodal methods other than MMA. The paper should include comparisons with other state-of-the-art multimodal fusion techniques, such as those based on graph neural networks or other attention mechanisms, to provide a more comprehensive evaluation of the MCA model's performance.

### Questions
1.	In the MCA model, are important modalities treated differently from minor modalities? Or are different modalities given different weights in the attention mechanism?
2.	At which critical point does the performance of MCA significantly degrade as modal sparsity increases? Are there optimisation methods to maintain embedding quality at higher sparsity?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a sparse multimodal fusion method in the presence of modal incompleteness. An extension to the masked multimodal transformer model is proposed which incorporates modal-incomplete channels in the multi-head attention mechanism called modal channel attention (MCA). The validity and usefulness of the method is verified by experiments on two multimodal datasets with different metrics and scenarios.

### Strengths
* This paper demonstrates the importance of how to cope with representation learning in the case of incomplete modalities in real applications.

* The authors provide extensive implementation details and interesting experiments to demonstrate the need for the proposed structure.

* The authors' review of the relevant literature is well organized.

### Weaknesses
This paper is clearly not ready for publication, including confusing typography, inadequate page counts for major sections, and formatting errors. For example, Fig and Figure are mixed up and line 221 is missing punctuation.

The experimental section focuses on the comparative analysis of different metrics. However, the authors lacked an effective comparison with previous work to highlight the advantages of the proposed methodology.

In addition, this study does not have enough qualitative analysis and ablation studies to explore the effect of different combinations of modal deletions in the proposed structure on performance.

### Questions
* As far as I know, CMU-MOSEI primarily provides information in three modalities, including audio, video, and text. I am not sure what exactly the four modalities the authors are referring to when they use them.

* The core structure presented in this paper is very similar to previous work [1], leading to limited improvements and contributions. I suggest that the authors clarify the differences between them in detail to highlight their contribution.

[1] Shvetsova, N., Chen, B., Rouditchenko, A., Thomas, S., Kingsbury, B., Feris, R. S., ... & Kuehne, H. (2022). Everything at once-multi-modal fusion transformer for video retrieval. In Proceedings of the ieee/cvf conference on computer vision and pattern recognition (pp. 20020-20029).

### Soundness
2

### Presentation
2

### Contribution
1
