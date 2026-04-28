# ColPali: Efficient Document Retrieval with Vision Language Models

- Decision: Accept
- Avg Score: 5.25
- Scores: 5, 8, 5, 3

## Abstract
Documents are visually rich structures that convey information through text, as well as tables, figures, page layouts, or fonts. While modern document retrieval systems exhibit strong performance on query-to-text matching, they struggle to exploit visual cues efficiently, hindering their performance on practical document retrieval applications such as Retrieval Augmented Generation. 
To benchmark current systems on visually rich document retrieval, we introduce the Visual Document Retrieval Benchmark \textit{ViDoRe}, composed of various page-level retrieving tasks spanning multiple domains, languages, and settings. 
The inherent shortcomings of modern systems motivate the introduction of a new retrieval model architecture, \textit{ColPali}, which leverages the document understanding capabilities of recent Vision Language Models to produce high-quality contextualized embeddings solely from images of document pages. Combined with a late interaction matching mechanism, \textit{ColPali} largely outperforms modern document retrieval pipelines while being drastically faster and end-to-end trainable. 
We release all project artifacts at \url{https://huggingface.co/vidore}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents two contributions in the context of document retrieval: (1) it presents ViDoRe, a new benchmark used to evaluate document retrieval algorithms with an emphasis on documents containing visual information, which is not covered by most of the existing benchmarks; and (2) it introduces ColPali, a model architecture that uses Vision-Language Models to efficiently index the documents in an efficient manner, and performing retrieval at query time with a competitive cost.

ViDoRe is composed from different existing academic datasets (mainly Vision Question Answering benchmarks), plus topic-specific publicly-accessible PDFs collected by the authors. ColPali is built based on PaliGemma-3B and the ColBERT strategy to generate a set of vision-text tokens from PDFs (during indexing) and text queries (during retrieval).

The results reported in the paper show that standard methods of document retrieval are either very expensive for indexing (e.g. solutions based on the off-the-self "Unstructured" tool, augmented with image captioning or OCR) or provide lower quality (e.g. approaches based on contrastive Vision-Language encoders). The proposed

### Strengths
- The proposed benchmark, ViDoRe, covers an important gap for evaluating existing document retrieval systems.
- The method presented in the paper significantly improves existing approaches, even those that require some fine-tuning (see table 2).
- The paper includes a section with extensive ablation studies that justify some of the decisions made during the design of the ColPali method.
- Hyperparameter tuning was not directly done on the ViDoRe benchmark, but on a 2% split from their training set (however, this training set poses some problems, see the weaknesses bellow).

### Weaknesses
 - The paper builds ColPali iteratively starting from a SigLIP model, and using previously existing recipes. However, each of the steps is not very well detailed in the paper itself, which may make the paper hard to truly understand for readers not familiar with SigLIP, ColBERT, or PaliGemma. I would suggest expanding the details on section 5.1.
- For sytems that require any sort of tuning, the authors have used a dataset made of rouhgly 120k query-page pairs, 63% of which come from the same distribution used in the academic ViDoRe benchmark. The authors made sure that no query or page in the evaluation set is part of the training data, however the training data is very "in-distribution" of the evaluation data, which may bias both the hyperparameter tuning and the quality of the methods on ViDoRe. I would strongly suggest that the authors (also) present results, for the different methods that require some sort of tuning, using only the synthetic training data (including hyperparameter search). This way, we can measure if the gap between the proposed method and the Unstructured approaches is mainly due to the architecture or due to the (in-domain) fine-tuning  and hyperparameter selection.

### Questions
See questions / concerns implied in the weaknesses section.

### Soundness
3

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
2

### Summary
This paper introduces a novel document retrieval method called ColPali, which uses Vision Language Models (VLMs) to generate high-quality multi-vector embeddings directly from images of document pages. The method aims to address the performance bottlenecks of current text-centric retrieval systems when dealing with visually rich documents. The paper also introduces a new benchmarking framework, ViDoRe, to evaluate system performance in visually rich document retrieval.

### Strengths
1. The ViDoRe benchmark covers multiple domains and languages, providing a comprehensive framework to evaluate the capabilities of document retrieval systems.

2. ColPali presents an innovative concept that significantly improves performance through retrieval in the vision space. Experimental results demonstrate that ColPali significantly outperforms existing methods in several visually complex tasks and offers fast indexing and querying capabilities.

3. The paper mentions that all resources, including models, data, and code, are released under open licenses, which will promote further research and application within the community.

### Weaknesses
1. Although the ViDoRe benchmark covers multiple domains, the generality and adaptability of ColPali in broader application scenarios need further validation.

### Questions
No additional questions.

### Soundness
3

### Presentation
3

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
In this paper, the authors explore a different approach to visually-rich document retrieval. To better assess current systems for this task, they construct a benchmark, called ViDoRe, which consists of various page-level retrieval tasks spanning multiple domains, languages, and practical settings. Inspired by ColBERT, the authors propose to perform document retrieval by directly embedding the images of the document pages. The proposed model, termed ColPali, is a Vision Language Model with a late interaction matching mechanism. The proposed model is evaluated on the ViDoRe benchmark and compared with existing pipelines for document retrieval.

### Strengths
1. This work investigates a very important problem: retrieving information from visually-rich documents. Visually-rich documents are quite common in practice and usually with complex layouts as well as informative elements such as figures and tables, which cannot be well handled by existing pipelines for document retrieval.
2. Different from previous pipelines, the authors accomplish visually-rich document retrieval by directly embedding the images of the document pages with VLMs and late interaction mechanisms. Experiments demonstrate the effectiveness and efficiency of the proposed ColPali model.
3. The proposed ViDoRe benchmark is a good contribution to the community as it can be used to evaluate systems on page-level document retrieval with a wide range of domains and applications, in the setting of simultaneous textual and visual understanding.
4. Overall, the paper is well-written. The main idea and key technical details are clearly presented.

### Weaknesses
1. The proposed pipeline is mainly inspired by ColBERT and PaliGemma. The author should give more explanations and analyses to prove the novelty of it.
2. The authors specially emphasize the importance of retrieval efficiency in industrial applications. However, the quantitative results regarding the latencies of different document retrieval model/systems are not detailed in the paper.

### Questions
The authors are encouraged to further explain the novelty of the proposed ColPali and give more quantitative results regarding the latencies of different document retrieval model/systems.

### Soundness
3

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
The paper introduces ColPali, a document retrieval model that leverages LVLMs to create high-quality contextualized embeddings from images of document pages. This approach allows for efficient and fast query matching, leading to improved performance in document retrieval tasks. The paper's main contributions are: 1. The ViDoRe Benchmark: a comprehensive benchmark for evaluating document retrieval systems across various domains, visual elements, and languages. 2. The ColPali Model: a model that indexes documents based on their visual features and uses a late interaction mechanism for query matching, outperforming existing retrieval systems in terms of speed and accuracy.

### Strengths
**Performance Improvements**: ColPali demonstrates superior performance on the ViDoRe benchmark compared to modern document retrieval pipelines and is significantly faster, making it suitable for practical applications.

**End-to-End Trainability**: The ColPali model is end-to-end trainable, simplifying the optimization process for the retrieval task.

**Open-Source Release**: The authors release all project artifacts, including models and code, to encourage further development and research in the field.

**Multilingual Capabilities**: ColPali shows the ability to generalize to non-English languages, expanding its potential use cases globally.

### Weaknesses
 **Benchmark Samples**: The manuscript should include examples from the ViDoRe benchmark that showcase its diversity in modalities, thematic domains, and language types. This will provide a more comprehensive understanding of the benchmark's scope and applicability.

**Retrieval Candidate Space Clarification**: The manuscript does not clearly define the retrieval candidate space for the ViDoRe benchmark. Clarifying this aspect is essential for understanding the benchmark's parameters and the retrieval process.

**ColPali Model Details**: The manuscript lacks essential details about the ColPali model. For instance, the definitions of N_q and N_d
  are not provided, nor is it explained how the document representation is generated. It is unclear whether the representation is derived from features corresponding to the [BOS] or [EOS] tokens, or if it is an average of the entire sequence features. These details are vital for replicating the study and understanding the model's workings.

**Broader Evaluation**: The evaluation is currently limited to the ViDoRe benchmark, with no experiments conducted on publicly available datasets such as those used for the retrieval task in VLM2Vec [1] and page prediction in MPdocVQA [2]. Expanding the evaluation to include these datasets would strengthen the experimental results and increase their convincing.

### Questions
**Page-Level Retrieval Capability**: Does the ColPali support page-level retrieval within a PDF, such as those in DUDE and MPdocvqa? Both MPdocvqa and DUDE also provide the gold document of a PDF.

**Text Retrieval Functionality**: Is ColPali capable of performing conventional text-based retrieval, or is its functionality limited to document images and visual features?

### Soundness
3

### Presentation
2

### Contribution
2
