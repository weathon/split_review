# Exploring Multi-Grained Concept Annotations for Multimodal Large Language Models

- Decision: Reject
- Scores: 3, 5, 5, 5

## Abstract
\label{sec:abstract}
   \setcounter{footnote}{0}
   Multimodal Large Language Models (MLLMs) excel in vision--language tasks by pre-training solely on coarse-grained concept annotations (\eg{} image captions).
   We hypothesize that integrating fine-grained concept annotations (\eg{} object labels and object regions) will further improve performance, as both data granularities complement each other in terms of breadth and depth in concept representation.
   
   We introduce a new dataset featuring \textbf{M}ultimodal \textbf{M}ulti-\textbf{G}ra\textbf{i}ned \textbf{C}oncept annotations (\textbf{\datasetname{}}) for MLLMs.
   In constructing \datasetname{}, we explore the impact of different data recipes on multimodal comprehension and generation.
   Our analyses reveal that multi-grained concept annotations integrate and complement each other, under our structured template and a general MLLM framework.
   
   We clearly explore and demonstrate the potential of \datasetname{} to help MLLMs better locate and learn concepts, aligning vision and language at multiple granularities.
   We further validate our hypothesis by investigating the fair comparison and effective collaboration between \datasetname{} and image--caption data on $12$ multimodal comprehension and generation benchmarks, \eg{} their appropriate combination achieve $3.95\%$ and $2.34\%$ absolute improvements over image--caption data alone on POPE and SEED-Bench.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces a new dataset, Multimodal Multi-Grained Concept Annotations (MMGIC), aimed at enhancing Multimodal Large Language Models (MLLMs) in vision-language tasks by integrating both coarse-grained and fine-grained concept annotations. MMGIC is designed to address this limitation by including fine-grained annotations, such as object labels and object regions, alongside traditional captions, to better align vision and language across multiple granularities. The proposed approach leverages MMGIC within a general MLLM framework and evaluates its effectiveness on 12 multimodal comprehension and generation benchmarks.

### Strengths
The paper introduces MMGIC, a multimodal dataset with multi-grained concept annotations that integrates both coarse-grained (e.g., captions) and fine-grained (e.g., object labels, regions) annotations. This is a novel approach to enrich MLLMs, allowing them to achieve more nuanced vision-language alignment across different granularities.

### Weaknesses
 **Writing and Clarity:** While I appreciate the authors’ efforts in extensively detailing the effectiveness of the proposed dataset, the writing is difficult to follow. There are too many unnecessary explanations, making the core claim of the paper unclear. The main focus seems to be on the dataset, yet the structure and writing style do not align well with a typical dataset paper, leading to a somewhat disorganized presentation.

**Dataset Quality:** As this is a dataset paper, it would be helpful to include a thorough evaluation of the dataset’s quality. Although large models like GPT are powerful to generate captions for local areas in the proposed dataset, they are known to suffer from hallucination issues. Could this dataset potentially exacerbate such problems, and how do you mitigate this risk?

**Untenable argument:** The importance of fine-grained understanding is well recognized. However, I question the point made in line 63 regarding the use of next-token prediction as a means to facilitate image understanding. Given the scale of the proposed dataset, a more effective loss function tailored to enhance comprehension might be a better choice than a simple autoregressive objective, which may not fully leverage the dataset’s potential.

### Questions
See weaknesses.

### Soundness
2

### Presentation
1

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
To integrate fine-grained concept annotations into Multimodal Large Language models (MLLMs) learning, this paper proposes a new dataset to explore the impact of different data recipes on multimodal comprehension and generation.  Extensive experiments demonstrate that multi-grained concepts do facilitate MLLMs to better locate and learn concepts, aligning vision and language at multiple granularities.

### Strengths
1. The proposed dataset with fine-grained annotations can be beneficial to the multimodal community. 
2. Authors provided extensive ablation studies to compare different types of fine-grained annotations.
3. The proposed dataset demonstrates reasonably good results on image captioning, retrieval, and image generation tasks.

### Weaknesses
1. Considering the rich information of the fine-grained annotations, there seems to be marginal improvements comparing row 3 and row 0 in Table 1.

2. In Table 4, MLLM-MMGIC performs slightly better or even worse compared to the baseline model LaViT-v2-7B. It is a little bit unclear about the effectiveness of the proposed dataset.

3. Considering the large amount of images in IC dataset (i.e., 52M), the improvement of row 1 over row 2 is marginal.

### Questions
See the above weakness. The main concern is related to the performance on various tasks. The authors provide a large scale image-text dataset with fine-grained annotations. As this dataset is mainly collected from public object detection datasets, it should be naturally beneficial to VQA /GQA tasks. However, such improvements seem to be marginal on several tasks. For image captioning tasks, the model trained with the proposed dataset perform even worse compared to the baseline. It is difficult to evaluate the quality and effectiveness of the proposed dataset given such results.

### Soundness
2

### Presentation
2

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
This research examines how MLLMs perform better when given two types of image information: broad descriptions (like overall image captions) and specific details (such as labeled objects and their locations). By using both levels of information together, MLLMs can better connect visual and linguistic elements, leading to improved performance on tasks that combine vision and language—whether that's describing images, answering questions about them, or creating images from text descriptions.

### Strengths
1- The researchers developed MMGIC, a new dataset that provides image annotations at multiple levels of detail. This fills an important need in the field of multimodal learning, where existing datasets often lack such comprehensive labeling.

2- The study's findings are backed by concrete test results, particularly on established benchmarks like POPE and SEED-Bench. By analyzing different combinations of annotation types, the researchers showed that using multiple levels of image descriptions significantly boosts how well MLLMs handle complex tasks that combine visual and language understanding.

### Weaknesses
1- Creating large datasets with detailed object-level annotations poses a major challenge, as it demands either extensive manual labor or sophisticated automated systems. While MMGIC makes valuable contributions, its reliance on existing public datasets creates two key limitations: it's difficult to expand the dataset size, and there's less room for automated data collection.

2- The study tests how different combinations of image annotations affect model performance. However, it falls short in explaining why certain combinations are more effective than others. This gap in analysis means we can see which approaches produced better results, but we don't fully understand the underlying reasons for their success.

### Questions
Address each of the weaknesses mentioned.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces the MMGIC dataset with multi-grained concept annotations, significantly improving model understanding and generation abilities, and demonstrates its effectiveness in zero-shot image captioning and generation tasks. It details the data filtering and synthesis process to enhance data quality.

### Strengths
1. The introduction of the MMGIC dataset with multi-grained concept annotations is a novel approach that significantly enhances model understanding and generation capabilities, providing richer and more detailed annotation information compared to traditional datasets.
2. The paper details an effective data filtering and synthesis process from multiple public datasets, ensuring high data quality and diversity, which in turn improves model training efficiency and effectiveness.

### Weaknesses
1. This paper emphasizes the introduction of a novel dataset. However, the process of image collection and dataset creation is relatively straightforward and lacks significant innovation, primarily involving the aggregation of existing datasets and the application of standard annotation techniques. The novelty of the dataset is further diminished by the fact that the multi-grained annotations are largely derived from existing resources and LLM-generated descriptions, rather than through a novel annotation process.
2. The paper mentions several new features of the dataset, but these have not been thoroughly validated or discussed in either theoretical or subsequent practical experiments. Specifically, the proposed label description, which involves designing prompts to generate detailed descriptions via LLMs, is general in nature and unrelated to the images. This could potentially lead to hallucinations during model training, as the descriptions are not grounded in the visual content. The lack of analysis on the impact of these potentially noisy descriptions is a significant oversight.
3. Although this paper is focused on the dataset, a significant portion is dedicated to describing the model architecture. Additionally, the experimental results lack comparative references from other studies, making it difficult to verify the dataset's effectiveness. The absence of comparisons with existing datasets and models that utilize similar multi-grained annotation strategies makes it challenging to assess the true contribution of the proposed dataset.

### Questions
1. Shouldn't you compare your method with others to demonstrate the superiority of your dataset?

2. Compared to others' methods of creating datasets, what are the advantages of your approach?

[1] Chen, Lin, Jinsong Li, Xiaoyi Dong, Pan Zhang, Conghui He, Jiaqi Wang, Feng Zhao, and Dahua Lin. "Sharegpt4v: Improving large multi-modal models with better captions." In: ECCV (2024).  

[2] Urbanek, Jack, Florian Bordes, Pietro Astolfi, Mary Williamson, Vasu Sharma, and Adriana Romero-Soriano. "A picture is worth more than 77 text tokens: Evaluating clip-style models on dense captions."  In: CVPR (2024).

### Soundness
3

### Presentation
3

### Contribution
2
