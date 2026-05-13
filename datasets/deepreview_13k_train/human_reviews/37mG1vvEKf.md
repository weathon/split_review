# ChuLo: Chunk-Level Key Information Representation for Efficient Long Document Processing

- Decision: Reject
- Scores: 3, 5, 3, 5

## Abstract
Transformer-based models have achieved remarkable success in various Natural Language Processing (NLP) tasks, yet their ability to handle long documents is constrained by computational limitations. Traditional approaches, such as truncating inputs, sparse self-attention, and chunking, attempt to mitigate these issues, but they often lead to information loss and hinder the model's ability to capture long-range dependencies. In this paper, we introduce ChuLo, a novel chunk representation method for long document classification that addresses these limitations. Our ChuLo groups input tokens using unsupervised keyphrase extraction, emphasizing semantically important keyphrase based chunk to retain core document content while reducing input length. This approach minimizes information loss and improves the efficiency of Transformer-based models. Preserving all tokens in long document understanding, especially token classification tasks, is especially important to ensure that fine-grained annotations, which depend on the entire sequence context, are not lost. We evaluate our method on multiple long document classification tasks and long document token classification tasks, demonstrating its effectiveness through comprehensive qualitative and quantitative analyses.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces ChuLo, a chunk-level key information representation method aimed at enhancing the efficiency and effectiveness of Transformer-based models for long document processing. ChuLo employs unsupervised keyphrase extraction to create semantically meaningful chunks, prioritizing important tokens while reducing input length. The authors argue that this approach better preserves semantic and contextual information compared to existing techniques such as truncation or sparse self-attention. The method is validated on multiple document classification and token classification tasks, showing competitive performance improvements over baselines.

### Strengths
1. The proposed method introduces a novel combination of unsupervised keyphrase extraction and chunk-based representation, which benefits encoder models for text classification.
2. The paper presents a thorough empirical evaluation across several datasets, demonstrating clear performance improvements compared to traditional baselines and SoTA API-based models.
3. The performance analysis across different document lengths provides useful information for similar research in the future.

### Weaknesses
1. From the writing perspective, the structure of certain sections is repetitive and confusing. For example, in Section 3.2, the idea that extracting keyphrases is important is repeated multiple times throughout the paragraph. The same idea is repeated in Section 3.4 as well.
2. The proposed keyphrase extraction method has some strong inductive bias without explanation, like the position penalty, which is neither explained nor verified through ablation studies. I suppose this design assumes that the noun phrases appear earlier in the text are more likely key phrases. The effect of such a design is not discussed and might limit the use case for the proposed method.
3. There are some doubts regarding the evaluation process. More details in the Questions part.

### Questions
1. Some questions regarding the evaluation process:
(1) The results in Table 3's "All" setting do not match those in Table 1. Can you explain the reason behind this gap?
(2) In Table 3, why not compare ChuLo with other baselines used in Table 1?
(3) Why do GPT4o and Gemini1.5pro only have results on the "2048" setting?
(4) The NER task prompt used in Figure 8 might not be optimal. Please refer to some related research in this area, such as [1].
2. Although Algorithm 1 provides some details about the keyphrase extraction process, it would be better if more explanations could be added. For example, the meaning of the regex used (for extracting noun phrases), and the effect for the position penalty. Certain notations are unexplained, like $h$ in line 8.
3. The proposed method has a lot of hyperparameters: $a, b, n, \alpha, \gamma$, to name a few. How did you decide the value for them, and what are the values you used?
4. Do you have any explanations for why RoBERTa underperforms BERT in Table 8?
5. Why only emphasize the noun phrases instead of emphasizing key sentences that contain facts about the key phrases?
6. Some minor mistakes: In Algorithm 1's Line 8, $l_k$ should be $l_{k_i}$. In line 216, add a space within "key phrases".

[1] Dhananjay Ashok and Zachary Lipton. PromptNER: Prompting For Named Entity Recognition. arXiv preprint arXiv: 2305.15444.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces Chulo, a model that enhances transformer-based approaches for long document-level and token-level classification tasks by effectively integrating chunk-level information. The method of dividing long documents into manageable chunks is reasonable, resulting in good performance especially in token-level classification tasks.

### Strengths
1. The method of dividing long documents into manageable chunks is reasonable.
2. The performance is good particularly in token-level classification.

### Weaknesses
1. The motivation of this work—"… can handle long documents efficiently while retaining all key information from the input…" (lines 55-56)—appears unaddressed. As I understand, the proposed model maintains the same sequence length as other BERT-like models and integrates additional information, such as chunk-level details with key phrases, which in fact increases computational load. The paper would benefit from a dedicated section thoroughly discussing the motivation of the work, or detailing the method’s potential cost savings (e.g., in terms of FLOPs, model size, etc.).

2. The comparison with LLMs appears unfair, as Chulo is fine-tuned on the downstream dataset. To make the comparison more balanced, it would be beneficial to fine-tune some open-source LLMs, such as LLaMA or Qwen, on the same dataset.

3. The design is not novel; similar to hierarchical-BERT [1], it organizes sentences into chunks.

[1] Lu, J., Henchion, M., Bacher, I. and Namee, B.M., 2021. A sentence-level hierarchical bert model for document classification with limited labelled data. In Discovery Science: 24th International Conference, DS 2021, Halifax, NS, Canada, October 11–13, 2021, Proceedings 24 (pp. 231-241). Springer International Publishing.

### Questions
See weakness

### Soundness
3

### Presentation
2

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
The paper introduces "ChuLo," a chunk-level key information representation method designed to improve long document processing in Transformer-based models. Traditional models face limitations handling extensive texts due to high computational demands, often resulting in information loss from truncation, sparse attention, or simple chunking methods. ChuLo uses unsupervised keyphrase extraction to identify and emphasize core content within each chunk, enhancing document and token classification accuracy without losing critical details. Experimental results demonstrate ChuLo's superior performance across various datasets, especially for lengthy documents, making it a scalable solution for tasks requiring comprehensive text analysis.

### Strengths
1. ChuLo outperforms GPT-4o on certain tasks.

### Weaknesses
1. The novelty of the method is limited, as keyphrase extraction is already widely used.
2. The title and experiments do not align, as "Long Document Processing" has a broader scope than classification.
3. The baselines used for comparison are somewhat outdated, with most being from 2022 or earlier.

### Questions
1. I would not recommend using the "long document" concept here, as many LLMs like LLaMA have already extended the context length to 131k, whereas this paper handles only up to 10k.
2. The comparison with GPT-4o is commendable; however, how would LLaMA perform on this task if fine-tuned directly? I don't believe this experiment can be avoided.
3. If comparing with fine-tuned LLMs or GPT models, I would expect the authors to include inference speed comparisons, which might be one of the method's advantages.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a method named ChuLo, designed to address the computational limitations encountered by Transformer-based models when processing long documents. ChuLo extracts key phrases through an improved PromptRank to preserve the core content of the document while reducing the input length. The model is trained using enhanced chunk representations of key information, enabling it to effectively integrate the core semantic content of the document. The paper supports its claims through multiple document-level and token-level classification tasks, providing both qualitative and quantitative analyses. Experimental results demonstrate that ChuLo achieves competitive results across multiple datasets.

### Strengths
Originality: The combination of unsupervised key phrase extraction with chunk representation to improve long document understanding is uncommon in previous research.

Quality: The paper aims to address the practical and significant issue of computational limitations faced by Transformer models when processing long documents. Experimental evaluations conducted on multiple document-level and token-level classification tasks demonstrate the feasibility of the proposed method.

Clarity: The paper is structured clearly, with a logical progression from problem statement to methodology, experiments, and conclusions. The detailed description of the SKP algorithm in the paper aids readers in understanding its working principles.

Importance: The proposed ChuLo method enhances the efficiency and performance of long document processing, holding potential for application in long document classification tasks.

### Weaknesses
1. The ChuLo method proposed in the paper focuses on long document processing, particularly in document classification tasks. It is stated on line 72 that the contributions of this method include its applicability to various NLP applications, but you have not experimentally confirmed the generalization ability of your method. Therefore, we cannot determine its performance on other types of NLP tasks, such as long document question answering and summarization.
2. The description of the model training process in the paper is not detailed enough, lacking specific steps of the training. In Section 3.4 of the paper, only the selected model for training is introduced, with no mention of data sources, data processing, optimization algorithms, parameter configurations, or other relevant details.
3. In Sections 5.4 and 5.5, ChuLo demonstrates significant performance differences compared to existing methods. Therefore, providing scientific explanations for these differences is very important. The lack of analysis of such significant differences in the paper is confusing.

### Questions
1. According to line 72, how does the paper determine the performance of the ChuLo method on other types of NLP tasks?
2. What are the specific details of the model training process described in the paper?
3. What are the scientific explanations for the significant performance differences demonstrated by ChuLo in Sections 5.4 and 5.5?

### Soundness
3

### Presentation
2

### Contribution
3
