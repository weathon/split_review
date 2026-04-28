# ADOPD: A Large-Scale Document Page Decomposition Dataset

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Research in document image understanding is hindered by limited high-quality document data. To address this, we introduce ADOPD, a comprehensive dataset for document page decomposition. ADOPD stands out with its data-driven approach for document taxonomy discovery during data collection, complemented by dense annotations. Our approach integrates large-scale pretrained models with a human-in-the-loop process to guarantee diversity and balance in the resulting data collection. Leveraging our data-driven document taxonomy, we collect and densely annotate document images, addressing four document image understanding tasks: Doc2Mask, Doc2Box, Doc2Tag, and Doc2Seq. Specifically, for each image, the annotations include human-labeled entity masks, text bounding boxes, as well as automatically generated tags and captions that have been manually cleaned. We conduct comprehensive experimental analyses to validate our data and assess the four tasks using various models. We envision ADOPD as a foundational dataset with the potential to drive future research in document understanding.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
To help the community develop techniques that process documents (like letters, forms, emails, news articles, resumes, and research papers), this work introduces a large dataset for several document understanding tasks. They annotate this data for document classification and for a few "page-decomposition" tasks, namely, Doc2Mask, Doc2Box, and Doc2Seq.

The underlying data is labeled and derived from Laion. However, the authors seem to have some concern about the diversity/balance of the types of data in there and/or the quality of the labels. Annotating this data is hard because of its scale. The authors introduce a rich pipeline to discover document taxonomies. The taxonomy developed in this way helps ensure that the final dataset is diverse and balanced. This pipeline is based on a human in the loop with information derived from several foundation models, namely, an LLM that orchestrates information from an image feature extractor, an OCR model, an image captioning model, an image tagging model, and a vision-language model. 

The authors analyze the document taxonomy and find that it contributes "to a more comprehensive and balanced dataset". Then, they evaluate several models on their page-decomposition tasks, namely, Doc2Mask, Doc2Box, and Doc2Seq.

### Strengths
1. This is clearly a very large and well-managed effort that contributes a resource that the community will benefit from. The authors are thoughtful and thorough in working to ensure the quality of the data.

2. The proposed algorithm for hybrid data annotation is very rich and interesting. I'm not aware of any other successful orchestration of this number of models of various modalities, within a powerful human-in-the-loop iterative k-means clustering. There may be much of independent value in this process, beyond the benchmark itself.

### Weaknesses
1. The paper is particularly hard to follow! I cannot overstate this: it affects every section of the paper, from the abstract to the evaluation, so I'm not even 100% sure I understand the work. All sections contain a lot of unnecessary commentary (like comments on novelty or general motivations) that do not contribute a lot of value. At the same time, the background and organization are lacking. Please spend that space on background setup or technical details. For instance, half-way through the introduction, it was not really clear what Document Page Decomposition Dataset means (that's a lot of nouns in a sequence).

2. What is the exact contribution in the paper, compared to the data source in Laion? Were the labels of Doc2Mask, Doc2Box, and Doc2Seq just used as-is from existing data or labeled in this work? It's a significant weakness in my opinion that I'm not sure how to answer this.

3. The evaluation repeatedly claims that the authors "carry out experiments using various baseline models and parameter configurations, confirming the effectiveness of ADOPD for document domain". How does evaluating the models confirm the effectiveness of the dataset? It's very plausible in some ways, but could you be more explicit? How much of the data was confirmed to be of high quality and what kind of error analysis was conducted, etc., particularly for any labels (other than taxonomy, which is well-analyzed) generated automatically.

### Questions
See weakness 2.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a new document page decomposition dataset called ADoPD, mainly focusing on document tagging, segmentation, text detection and caption. Combining automatic procedure like machine/deep learning models and human annotator, this paper creates a much large and high-quality document dataset and still maintains low cost. Additionally, this paper conduct analysis of proposed dataset.

### Strengths
1.	This paper collects a large amount of data (120k), which has high resolution, wide source, and diverse appearance, the high quality data is beneficial for area. It offers segment, caption annotations which are rare in other document datasets.
2.	The “hybrid data annotation” is novel and it helps to ensure the dataset is balanced and diverse. This proposed method alleviates the demand for human annotators and still maintains the high tagging quality for this dataset.
3.	This paper offers quantitative evaluation for the diversity of data distribution, further confirmed the effectiveness of the “hybrid data annotation”.

### Weaknesses
1.	The detection and segmentation annotation quality are not well studied, they all come from pretrained model and corrected by human annotators. It’s better to give more detail about the procedure to correct the annotation. Especially there are some other document datasets like DocBank -- the box annotation is extracted from PDF by automatic tools and it should be much more precise than detection model.
2.	Although the proposed dataset is claimed to be suitable for caption, but the caption annotation is generated by BLIP-2 and there is no human correction. BLIP-2 is mainly trained for universal visual-language task and it might not suitable for document caption.

### Questions
1.	The caption annotation is just generated by BLIP-2 and there are not further correction or filter. I think this model-annotation might be meaningless for the area.
2.	The section 4.2.3 Doc2Seq claims that 5000 samples are manually annotated, but after that, the paper says “utilized 80,000 samples for training, 20,000 for testing, and another 20,000 for validation“. It’s confusing how the manually annotation are collected and used, and why it has 20,000 validation and test samples – not consistent with 5,000 manual annotation.
3.	Will the dataset be open-source?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a new annotated database to enhance automatic document comprehension and, more specifically, document page decomposition. The dataset was annotated multimodally to support 4 tasks: document entity segmentation, text detection, tagging, and captioning. The annotation was done in such a way as to combine the use of large pre-trained models and human expertise. Finally, a great effort has been made to maximize the diversity of document images.

### Strengths
* This paper presents a very significant and interesting work on data collection, showing a great diversity. Moreover, the use of numerous pre-trained models such as ViT, CLIP, or BLIP and the fusion of all the information predicted by these models within a single prompt is very interesting and rarely presented (and even used?) in research papers.
* Even if this is not really shown in the results tables, it is clear that this dataset will certainly help research on documents, particularly thanks to the diversity of the images and the multiple annotations.

### Weaknesses
 * While the use of 5 pre-trained models to pre-label images is quite innovative, it would also be interesting to indicate the cost of applying these different models to an image (and even to millions of images). Specifically, the computational cost, in terms of GPU hours and memory usage, should be quantified for each model, as well as the time required for inference on a single image and on the entire dataset. This would help assess the feasibility of the approach for researchers with limited resources.
* I found section 4.1 a little unclear. Although efforts have been made to explain the image selection process as fully as possible, I'm not sure that this methodology can be easily reproduced from these explanations. The description lacks specific details regarding the thresholds used for filtering images based on the outputs of the various pre-trained models, and the exact criteria used to determine the final set of images. A more detailed, step-by-step explanation of the process, including the specific parameters used for each model, would be necessary for reproducibility.
* In the results tables, the authors show how the different models compare once they've been trained on ADOPD. It would have been interesting to compare these models with and without fine-tuning on ADOPD to see the real impact of this dataset. The comparison should include a clear indication of the performance gain achieved by fine-tuning on ADOPD, rather than just showing the performance of models trained on it. This would help in understanding the dataset's contribution to the models' performance.
* It would have been interesting to see results on other document datasets, starting from models pre-trained on ADOPD vs. on ImageNet for example. This would have shown the real gain of pre-training on a wide variety of document images compared to a large quantity of natural scene images. The comparison should include a variety of document datasets, representing different document types and complexities, to provide a comprehensive evaluation of the dataset's generalization capabilities.
* The metrics used to evaluate the caption performance should probably be a bit more explained in the text. Specifically, the rationale behind choosing these metrics, their strengths and weaknesses, and how they relate to the task of document captioning should be discussed. This would provide a better understanding of the evaluation process and the results obtained.

### Questions
* This dataset would be very interesting to explore and obviously to use for pre-training. I think it would also be great to see what generalization capabilities a model trained on this dataset would have, once applied to another use case. This is not described in the paper, but do you plan to make this dataset public? If so, how do you plan to distribute it?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
### Summary:
The paper introduces "ADoPD," a large-scale document page decomposition dataset designed for document understanding. This encompasses tasks such as document entity segmentation, text detection, tagging, and captioning. ADoPD is distinct with its novel document taxonomy, meticulously crafted through a data-driven approach that incorporates both large-scale pretrained models and human expertise. By merging outlier detection with a human-in-the-loop method, the dataset achieves a notable diversity. ADoPD offers deeper insights into document structures and significantly elevates techniques in document processing and analysis.

### Major Contributions:
1. **Systematic Exploration of Document Taxonomy**: The work presents the first systematic exploration of document taxonomy using a blend of machine learning models and a human-in-the-loop approach.
  
2. **Largest and Most Comprehensive Database**: The paper has developed the most extensive and comprehensive database for document image segmentation and object detection.

3. **Thorough Dataset Analysis**: A profound analysis of the proposed dataset is conducted, accompanied by detailed experimental comparisons for entity segmentation and text detection tasks.

4. **Quantitative and Qualitative Results**: The value of the dataset is highlighted through both quantitative and qualitative outcomes.

5. **Advancement in Document Analysis**: The authors express the aspiration for ADoPD to serve as a catalyst in propelling research within the domain of document analysis.

### Strengths
### 1. Originality:

- **Novel Dataset**: The introduction of "ADoPD" represents a fresh addition to the domain of document processing. Few datasets offer the same breadth in terms of document page decomposition.
  
- **Unique Taxonomy Approach**: The blend of data-driven approaches with human expertise in crafting a document taxonomy is a distinctive contribution. This combination brings together the best of automated and manual categorization.

- **Human-in-the-loop Integration**: Incorporating human feedback in outlier detection for dataset diversity is an inventive methodology. This ensures that the dataset remains robust and versatile.

### 2. Quality:

- **Comprehensive Analysis**: The authors have delved deeply into the analysis of their proposed dataset, providing both qualitative and quantitative evaluations. Such rigorous examination is indicative of the dataset's quality and its potential applicability.

- **Comparison with Existing Datasets**: While the main content delves deeper, the authors seem to be aware of the limitations of existing datasets, positioning ADoPD as a superior alternative. This indicates meticulous research and understanding of the current landscape.

### 3. Clarity:

- **Well-Structured Presentation**: The paper appears to be organized in a logical flow, starting from the introduction of the problem, moving to methodology, followed by results and conclusions.

- **Illustrative Figures**: Based on the portions reviewed, figures like the overview of ADoPD annotations aid in visual comprehension, making the content more digestible.

- **Explicit Problem Statements**: The authors have clearly laid out the challenges and questions they aim to address with their dataset, providing clarity of purpose.

### 4. Significance:

- **Filling a Gap**: With the increasing demand for automated document processing techniques, ADoPD addresses a significant gap in the domain, especially with its emphasis on diversity and comprehensive taxonomy.

- **Potential for Future Research**: The introduction of such a dataset can catalyze further research in document understanding, segmentation, and object detection. It can serve as a foundational resource for subsequent works in the field.

- **Broader Application**: Beyond academic research, the advancements proposed in the paper have potential real-world applications in areas like digital archiving, automated content extraction, and more.

### Weaknesses
 ### 1. **Depth of Comparative Analysis**:
- **Weakness**: From the segments reviewed, while the paper introduces a new dataset, there seems to be a limited in-depth comparison with existing datasets.
- **Recommendation**: A deeper comparative analysis highlighting the specific advantages of ADoPD over existing datasets would solidify its significance. Quantitative benchmarks against datasets like DocBank, if not already included in the deeper sections, would be beneficial. Specifically, the paper should include a more rigorous comparison using metrics relevant to the tasks the dataset is designed for, such as mAP for object detection or F1-score for segmentation tasks. The comparison should not only focus on overall performance but also on performance across different document categories and complexities to highlight the dataset's robustness and generalizability.

### 2. **Methodological Justifications**:
- **Weakness**: The choice of the "human-in-the-loop" approach for outlier detection is novel, but the paper might not sufficiently justify why this method was chosen over others.
- **Recommendation**: Delve deeper into the advantages and potential limitations of this method, comparing it with purely automated outlier detection techniques. The paper should discuss the trade-offs between the cost and potential biases introduced by human annotation and the efficiency and potential errors of automated methods. A more detailed explanation of the criteria used by human annotators to identify outliers, and how these criteria were standardized across different annotators, would also be beneficial. Furthermore, the paper should explore the potential for incorporating more sophisticated outlier detection algorithms, such as those based on density estimation or anomaly detection, to complement the human-in-the-loop approach.

### Questions
**Dataset Composition**:
   Could you provide a more detailed breakdown of the types and sources of documents included in the ADoPD dataset? Understanding the diversity in terms of document genres, geographical origins, and linguistic variations would offer more insight into its applicability and robustness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
