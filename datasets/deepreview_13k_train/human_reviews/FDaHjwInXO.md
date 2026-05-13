# LoRA-Contextualizing Adaptation of Large Multimodal Models for Multi-page Document Understanding

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Large multimodal models (LMMs) have recently shown great progress in text-rich image understanding, yet they still struggle with complex, multi-page visually-rich documents. Traditional methods using document parsers for retrieval-augmented generation suffer from performance and efficiency limitations, while directly presenting all pages to LMMs leads to inefficiencies, especially with lengthy ones. We demonstrate that LMMs themselves can be an effective multimodal retriever to fetch relevant pages and then answer user questions based on these pages. LoCAL is implemented with two specific LMM adapters, one for evidence page retrieval and the other for question answering. Empirical results show state-of-the-art performance on public benchmarks, demonstrating the effectiveness of LoCAL.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
It presents a framework named LoRA-Contextualizing Adaptation of Large multimodal models (LoCAL) to broaden the horizons of LMM for multi-page document understanding. 
LoCAL is implemented with two specific LMM adapters, one for evidence page retrieval and the other for question answering. 
Empirical results show state-of-the-art performance on public benchmarks, demonstrating the effectiveness of LoCAL.

### Strengths
1. A novel framework named LoCAL to broaden the horizons of LMMs, where it uses intermediate LMMs hidden embedding for efficient question-based evidence page retrieval. 
2. It finetunes LMMs through dual LoRA adapters for evidence page retrieval and question answering.
3. It collects a visually-rich document QA dataset, LoCAL-bench.
4. It empirically demonstrates its effectiveness.

### Weaknesses
1. This article needs to be compared with more methods, such as bge-large, NV-Embed-v2, SigLIP, ColPali.
2. Two LoRA with one model, actually there are still two models, not a real unified model.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces LoCAL (LoRA-Contextualizing Adaptation of Large multimodal models), a framework for extending LMMs to handle long, multi-page document understanding. The key insight is using LMMs themselves as efficient retrievers for relevant pages before performing question answering, rather than relying on traditional document parsers or trying to process entire documents at once. It implements efficient parameter sharing through dual LoRA adapters to build a dual-module architecture where a single LMM serves both as a retriever and question answerer.

### Strengths
- The paper introduces an approach to multipage document understanding by combining LLMs with a retrieval mechanism tailored for multi-page, visually-rich documents. The use of dual LoRA adapters for separate retrieval and question-answering tasks is a creative adaptation that enhances the efficiency and modularity of the model.
- The paper provides an extensive set of experiments across multiple datasets, including SlideVQA, MMLongBench-Doc, DocVQA, and the newly proposed LoCAL-bench.

### Weaknesses
The idea of using LMM for evidence page retrieval is interesting but not entirely novel. Previous work like ColBERT (Khattab & Zaharia, 2020) has already employed contextualized late interaction in document retrieval tasks. Moreover, using LORA to efficiently adapt LLMs for different tasks is also widely used in many scenarios. Therefore, the paper could better position its contribution by clearly delineating how LoCAL surpasses existing methods in LMM retrieval and adaptation for long documents. Specifically, the paper does not sufficiently address the limitations of using a single LMM for both retrieval and question answering, particularly in scenarios where the optimal representations for these two tasks may diverge. The use of dual LoRA adapters attempts to mitigate this, but the extent to which this approach truly decouples the tasks and avoids interference needs further analysis. Additionally, while the paper mentions the use of web-crawled documents, it lacks a thorough discussion on the potential biases introduced by this data, and how these biases might affect the model's generalization capabilities.

### Questions
- Based on the fine-tuning dataset, you trained the retrieval module using the original ColPali training data, supplemented with DocMatix-IR and PFLDocVQA. Have you noticed any performance improvements compared to the retrieval module trained only on the original ColPali training data on Table 1 benchmarks and also ViDoRe benchmark from ColPali?
- According to the ColPali paper, the authors use the BGE-M3 embedding model as the text-based baseline. Do you believe this model could significantly outperform the SBERT baseline, given that BGE-M3 is more advanced on existing benchmarks?

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
4

### Summary
This paper introduces the LoCAL framework, which aims to enhance the understanding of multi-page, visually-rich documents by large multimodal models (LMMs). The framework employs dual LMM adapters for evidence page retrieval and question answering, demonstrating state-of-the-art performance on public benchmarks. The proposed method involves using LMMs as multimodal retrievers to fetch relevant pages and answer user questions based on these pages, utilizing hidden states for efficient retrieval. The paper also introduces a new dataset, LoCAL-bench, comprising 226 documents and 471 question-answer pairs across nine domains. The results highlight the effectiveness of LoCAL.

### Strengths
1.The paper introduces the LoCAL framework, which effectively broadens the capabilities of large multimodal models (LMMs) for understanding multi-page, visually-rich documents. This is a significant advancement in the field.

2. The implementation of dual LMM adapters for evidence page retrieval and question answering is a novel approach that enhances the efficiency and performance of the models.

3. The introduction of the LoCAL-bench dataset, which includes a diverse range of documents and question-answer pairs, provides a valuable resource for further research and development in this area.

### Weaknesses
While the paper does mention the limitations of traditional methods using document parsers for retrieval-augmented generation, it focuses on introducing and evaluating the LoCAL framework without a direct comparison to RAG methods.

### Questions
How to evaluate the quality of the LoCAL-bench dataset? Because the data is purely genereted from the GPT-4o model, although with human verificaition I still doubt its quality compared with other human-labeld datasets.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper aims to solve the problem of long document understanding. It proposes a method based on the LoRA technique that uses latent embeddings from LLMs to perform evidence retrieval and question answering at same time. To demonstrate the effectiveness of the method, the paper introduces a new dataset, LoCAL-Bench, and conducts experiments using multiple benchmarks.

### Strengths
1.	The paper is well-motivated, and the experiments demonstrate that the proposed method effectively addresses the challenge of long document understanding. 
2.	The structure of the LoCAL method is well-designed and compatible with multiple existing LLM models. Furthermore, sharing LLM parameters fully leverages their linguistic capabilities and enhances memory efficiency, thereby extending applicability. The proposed solution in the article is simple, effective, and insightful.
3.	The experiments are well-organized, and comparisons with multiple baselines, including LLM-based and non-LLM-based methods, are sound and the results convincing. 
4.	The paper is well-written, fluent, and highly readable.

### Weaknesses
1.	The LoCAL method primarily aims to solve the problem of multi-page long document understanding. However, the LoCAL-Bench dataset does not appear to feature the characteristics of long document length, which makes it hard to examine the real performance of the method. An ideal dataset should include a greater number of document pages than existing benchmarks. The authors should clarify whether the LoCAL-Bench dataset is necessary to demonstrate the effectiveness of the proposed method.
2.	Although the method achieves comparable performance to proprietary models such as Claude-3 Opus and Gemini-1.5-Pro, these proprietary models still exhibit strong abilities in other downstream tasks. However, the generalization ability of the method remains untested, which is crucial for LLM-based methods. Additionally, some work such as Textmonkey (Yuliang Liu, Biao Yang, Qiang Liu, Zhang Li, Zhiyin Ma, Shuo Zhang, and Xiang Bai. Textmonkey: An ocr-free large multimodal model for understanding document. arXiv preprint arXiv:2403.04473, 2024d.) also test their performance on multiple downstream tasks. Therefore, the author should conduct the experiments on the generalization ability or explain why such experiments are unnecessary for the paper.  
3.	The evidence pages supported by the proposed method seem to be limited to five pages. When the relevant evidence pages for a question exceed five, performance may decrease. This characteristic may reduce the method's general performance.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
3
