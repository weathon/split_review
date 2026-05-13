# General OCR Theory:  Towards OCR-2.0 via a Unified End-to-end Model

- Decision: Reject
- Scores: 3, 5, 6, 5

## Abstract
Traditional OCR systems (OCR-1.0) are increasingly unable to meet people's usage due to the growing demand for intelligent processing of man-made optical characters. In this paper, we collectively refer to all artificial optical signals (e.g., plain texts, math/molecular formulas, tables, charts, sheet music, and even geometric shapes) as "characters" and propose the \textbf{G}eneral \textbf{O}CR \textbf{T}heory along with an excellent model, namely GOT, to promote the arrival of OCR-2.0. The GOT, with 580M parameters, is a unified, elegant, and end-to-end model, consisting of a high-compression encoder and a long-contexts decoder.  As an OCR-2.0 model, GOT can handle all the above "characters" under various OCR tasks. On the input side, the model supports commonly used scene- and document-style images in slice and whole-page styles. On the output side, GOT can generate plain or formatted results (markdown/tikz/smiles/kern) via an easy prompt. Besides, the model enjoys interactive OCR features, i.e., region-level recognition guided by coordinates or colors. Furthermore, we also adapt dynamic resolution and multi-page OCR technologies to GOT for better practicality.  In experiments, we provide sufficient results to prove the superiority of our model.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The manuscript proposes a unified end-to-end 2.0 model for OCR, called GOT (General OCR Theory) using LVLMs (Large Vision Language Models). The architecture contains 80M parameters in the encoder, and 500M parameters in the decoder tackling long-contexts. Region-based recognition, dynamic resolutions and multi-page OCR are few other properties of GOT. It supports English and Chinese and can produce structured formats like markdown, tikz, smiles and kern. 

GOT has a 3-stage training process: pre-training the vision encoder, joint-training of encoder and decoder, and finally the post-training of the language decoder. The performance is compared against SOTA methods on various scores like edit distance, F1, BLEU and METEOR, and seems to out-perform against majority of the SOTA methods. The results on markdown, sheet music, geometry and number-centric charts are also presented.

### Strengths
The paper presents a unified end-to-end model for a gamut of OCR documents, including sheet music, geometry and number-centric charts. It replaces the cascaded OCRs specialized in different document types.

The way the three stages of training are applied to unify a diverse set of OCR tasks (scene, document, chart, music sheets, etc.) within a single OCR is interesting. The task-oriented fine-tuning is limited to post-processing the language decoder. Freezing the vision encoder avoids increasing the computational demands and ensures foundational visual understanding is stable across the tasks. 

The results are compared against the SOTA methods on a variety of metrics including F1-scores, edit distances, BLEU and METEOR values, and seem to outperform majority of the methods. For box-guided and color-guided OCR, specific comparison to Fox Lie et al. seems to outperform against all the metrics.

### Weaknesses
The weakness of the paper lies in its novelty. The 3-stage training process is well known in the literature. For example, many existing frameworks in OCR, vision-language and LVLMs decouple encoder pre-training from the rest of the pipeline. The vision encoders are usually pre-trained on a wide variety of data to create a foundational understanding of text and scene. The joint training of vision and language pieces is again known in models in UniT, BLIP and LVLMs. Lastly, the fine-tuning of the language decoder piece is again seen in T5 etc. Perhaps, the prime novelty is the application of these methods to an OCR problem, smarts about synthetic data generation and OCR-specific fine-tuning.

The other weakness of the paper is in its presentation. The paper is overall hard to follow, as it continues to mix, architecture, training, data and task-specific details all together, and does not lay out in separate sub-sections. E.g. the section 3.2.1 starts with the architecture, dives into input sizes, parameter sizes, goes through data peculiarities (natural scenes, cropped slices) and training process all in one paragraph. A lot of architecture diagrams can be added to aid the reading.

Lastly, in experiments, ablation studies are missing to underscore the importance of each of the stages, data types. Latency studies, comparisons with SOTA methods, and failure cases are missing.

### Questions
1. Section 4.1 lists joint training and post-training for only 1 epoch. Usually multiple epochs are required to train a model. While post-training can be understood as vision encoder and much of language decoder may already be well-trained from prior stages, 1 epoch for joint training seems pretty small. Any reason why that worked? Is there a study on how more epochs affected the outcome? Is it possible that there isn't much data diversity between training and test set, and hence, 1 epoch is enough?

2. What are the training/inference latency gains by using a smaller size model like GOT compared to Qwen-VL-MAX or others?

### Soundness
3

### Presentation
1

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
This paper introduces an so-called OCR-2.0 model named GOT, designed for advanced Optical Character Recognition tasks. It proposes a new OCR model, emphasizing end-to-end architecture, low training costs, and versatility in recognizing a wide range of artificial optical characters. The model, with 580M parameters, incorporates a high-compression encoder and a long-context decoder for handling various OCR tasks.

GOT is evaluated on multiple OCR tasks, demonstrating superior performance in plain document OCR, scene text OCR, formatted document OCR, fine-grained OCR, and more general OCR tasks like sheet music, geometric shapes, and chart OCR.

### Strengths
- The paper introduces a unified OCR-2.0  model, emphasizing an end-to-end architecture whichl is designed to handle various OCR tasks efficiently.

- GOT demonstrates versatility by recognizing a wide range of artificial optical characters, including sheet music, geometric shapes, and charts. The model can adapt to different input styles and output formats, enhancing readability for formulas and tables.

- This paper is well written and well organized.

- The idea of OCR 2.0 is interesting and novel.

### Weaknesses
(1) The term "general OCR theory" is not appropriate as the paper does not present any rigorous theory. It is suggested to consider alternative terms such as General OCR Technology/Framework/Pipeline/Methodology.

(2) Dataset construction is a significant contribution of this work. The authors utilized data engineering methods to create a substantial amount of non-public training data. If these datasets are not made publicly accessible, it will make it challenging for other researchers to perform fair comparisons under the same settings as this paper.

(3). In section 4.2.2, the authors collected 400 natural scene text images for testing. Why did they not use publicly available datasets in this domain (such as CTW1500, ReCTS, etc.) to evaluate the performance of GOT on natural scene text?  I am wondering if the proposed method on these public datasets can achieve state-of-the-art (SOTA) performance.

### Questions
1. How does the performance of the proposed method fare on openly and widely used page-level datasets (such as CASIA-HWDB, HCCDoc, CTW1500, ReCTS, IAM, CROHME16/19, etc.)? Why was the effectiveness of the proposed method not tested on these commonly used datasets in the community?

2. Are the test datasets used in sections 4.2.2, 4.2.3, and 4.2.5 open-source?

3. In the references, proprietary acronyms should be capitalized, for example, CASIA, IAM, HDWB, BLIP, etc.

Additional comment:  I do not agree that low training and inference costs must be a characteristic of OCR 2.0. As a new technology framework or paradigm for OCR in the era of AGI, it should also possess scalability capabilities.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces the GOT model (General OCR Theory), to improve upon traditional OCR systems (OCR-1.0). With 580 million parameters, GOT processes various artificial optical signals and supports multiple output formats. It features interactive region-level recognition and incorporates dynamic resolution and multipage OCR, showing superior performance in experiments.

### Strengths
1. This article presents a unified approach to OCR recognition tasks, making it one of the most comprehensive OCR models to date with sufficient tasks.
2. The proposed GOT method employs a three-stage pre-training and fine-tuning process to achieve the experimental results outlined in the paper.
3. The GOT method addresses various OCR recognition problems across multiple scenarios (natural scenes, documents, etc.), as well as different levels of granularity, such as document-level and region-level recognition.
4. Multiple datasets are constructed to conduct these diverse settings of these OCR recognition tasks.

### Weaknesses
1. The writing of this article needs further improvement, as several key details are missing. For example, when discussing the method, it is unclear how to distinguish between different tasks. Does it involve using a question as input to the decoder, similar to existing MLLMs? Specifically, the paper lacks a clear explanation of the input format for different OCR tasks. It's not evident how the model is prompted to perform tasks such as document-level vs. region-level recognition, or how it handles different types of input signals (e.g., natural scene images vs. document scans). The absence of a detailed description of the task-specific input mechanisms makes it difficult to assess the model's versatility and the generalizability of the proposed approach.
2. In the experiment, the paper does not conduct the comparisons on the benchmarks of  OCRBench, InfoVQA, and DocVQA. Is this because the proposed method does not support QA? (You did not clarify how you distinguish between different tasks?) The lack of comparisons on standard benchmarks like OCRBench is a significant oversight. These benchmarks provide a standardized way to evaluate OCR performance across various tasks and datasets. Furthermore, the absence of results on InfoVQA and DocVQA raises concerns about the model's ability to handle tasks that require both OCR and question-answering capabilities. It is unclear whether the model is designed to be a pure OCR model or if it can be extended to handle downstream tasks that involve reasoning over the recognized text. The paper should clarify the model's scope and limitations in this regard.
3. This paper mainly focuses on recognition issues related to OCR tasks and does not address detection problems. One possible reason could be that both the current encoder-decoder and decoder-only architectures struggle with coordinate regression prediction, which may have prevented you from tackling detection tasks. The paper's focus solely on recognition, while understandable, limits its practical applicability. In real-world scenarios, OCR systems often need to perform both detection and recognition. The paper should acknowledge this limitation and discuss potential avenues for extending the model to handle detection tasks. The current lack of detection capabilities raises questions about the model's ability to handle complex documents with varying layouts and text orientations. The paper should address this limitation and discuss potential solutions.
4. Additionally, there is a lack of comparison with methods like Kosmos?

### Questions
Show in the part of Weakness.

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper describes a single unified framework to perform end-to-end OCR in different kinds of images (documents, scene images, handwritten text, charts, music sheets, math formula). The framework relies on collecting a large amount of data for every type of image, partially from public data sources, partially automatically rendered. Then, a curriculum strategy is employed to train the model based on standard encoder and decoder architectures. In a first stage, only a limited number of OCR tasks with limited variability are used to train the encoder using a simple decoder and, progressively more data, tasks and the final decoder architecture are included in subsequent training stages. Experimental results compare the proposed approach with other generic models based on multimodal LLMs

### Strengths
- Compared to other unified end-to-end frameworks for multi-task OCR based on multimodal LLMs, the proposed approach is efficient and the model is relatively smail. 
- The proposal of a new training strategy adding complexity increasingly to the model, either from the point of view of the model and the data used for training. 
- The generation of a large collection of data to train the model can be useful for advancing research in generic OCR (if the data is made public after publication)

### Weaknesses
 - The paper lacks contextualization and comparison with previous SoA OCR methods not based on LLMs, specialized on each of the individual OCR tasks. Related work lacks a much better discusion and reference to all existing specific methods for text recognition in different tasks (scene text, documents, handwritten text, ...). In the experimental results I also miss comparison with specific OCR methods in each task, even in some tasks comparison with existing commerical OCR tools. 
- Following the previous comment, I think that the papser should also use common standard benchmarks and datasets in some specific OCR tasks. In the past years there has been a huge effort in the text recognition community to create standard benchmarks for evaluation, that are ignored in the paper. Using these common benchmarks (for all the tasks where this is possible) would help to get a better understanding of the contribution of the proposed approach in comparison with existing OCR techniques. 
- As far as I understand, most of the images used to train and evaluate the proposed approach are very clean images, collected from clean pdf documents or automatically rendered, without the kind of noise, distortion, low resolution problems, ... that can be encountered when dealing with real images. 
- I miss some analysis of the contribution of each of the training stages in the final performance of the model.

### Questions
- Some more details would be necesary on how metrics are computed given the full recognized text and ground-truth . 
- Also some more details on how the OCR task on charts is defined

### Soundness
2

### Presentation
3

### Contribution
2
