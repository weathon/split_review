# M-Longdoc: A Benchmark For Multimodal Super-Long Document Understanding And A Retrieval-Aware Tuning Framework

- Decision: Reject
- Scores: 5, 8, 5

## Abstract
The ability to understand and answer questions over documents can be useful in many business and practical applications. However, documents often contain lengthy and diverse multimodal contents such as texts, figures, and tables, which are very time-consuming for humans to read thoroughly. Hence, there is an urgent need to develop effective and automated methods to aid humans in this task. In this work, we introduce \datasetname{}, a benchmark of \datasize{} samples, and an automated framework to evaluate the performance of large multimodal models.
We further propose a retrieval-aware tuning approach for efficient and effective multimodal document reading. Compared to existing works, our benchmark consists of more recent and lengthy documents with hundreds of pages, while also requiring open-ended solutions and not just extractive answers. To our knowledge, our training framework is the first to directly address the retrieval setting for multimodal long documents. To enable tuning open-source models, we construct a training corpus in a fully automatic manner for the question-answering task over such documents. 
Experiments show that our tuning approach achieves a relative improvement of \performanceincrease{} for the correctness of model responses, compared to the baseline open-source models. Our data, code, and models are available at \url{https://multimodal-documents.io}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a dataset for long document understanding challenges with an automatic evaluation approach. The authors also propose a retrieval-aware tuning framework to mitigate the limitations of current LLMs dealing with multimodal long documents.

### Strengths
- Research problem is challenging and necessary for this direction and various domain applications.
- A new dataset is proposed for multimodal long document understanding.
- A LLM-based auto-evaluating framework is introduced.

### Weaknesses
 - The scope of this paper limited the question only focusing on specific pages ignoring the more natural cases of answers distributed spanning pages. And the author mentioned the in-depth but there is no supporting analysis and results to show why the dataset shows more in-depth. 
- The dataset generation workflow uses off-the-shelf tools and models to extract the document structure which should be verified as the accumulated errors may occur when moving to the automatic QA generation stage. 
- More dataset analyses are expected including question length and focusing topics. Simple statistics can not show more insight of your datasets. 
- The proposed evaluation metrics may need more detailed analysis to show robustness. Current average weighting looks too simple ignoring the difference between specific models dealing with specific types of questions. Some penalty or reward terms may need to be considered.
- As the metrics are unexplored the results may not be comprehensive and reliable. Lack of quantitative analysis show different domain, question types performance.

### Questions
- Does your dataset consider the spanning-page answer setting?
- Is there a dataset structure parsing quality checking procedure?
- Is there any analysis or comparison before and after human checking automatically generated QA pairs?
- Why does the number of document pages per document look wired, especially for academic papers? It might be too long for an academic paper.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents M-LongDoc, a new benchmark for evaluating the ability of large multimodal models to understand and answer open-ended questions over lengthy and diverse documents containing text, figures, and tables. M-LongDoc comprises 851 samples across academic, financial, and product domains, featuring documents significantly longer and more structurally complex than those in existing benchmarks. The authors also proposes a novel retrieval-aware tuning approach that specifically trains models to handle potentially irrelevant retrieved content, leading to a 4.6% relative improvement in answer correctness compared to baseline open-source models. Lastly, the authors contribute a large-scale training corpus of 10,070 samples and an automated evaluation framework based on a committee of multimodal judges to assess the correctness of open-ended solutions.

### Strengths
Useful new eval dataset, training dataset, eval framework and interesting model for multimodal RAG-QA on long docs.

### Weaknesses
This paper doesn't really have any major weaknesses. In particular, the paper presents its contribution as being primarily a dataset paper, so there's understandably not much novelty with the models.

### Questions
All clear to me

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
The paper introduces M-LongDoc. M-LongDoc is a novel benchmark dataset to evaluating multimodal long document (210 pages in average) understanding. M-LongDoc features 851 samples that challenge existing multimodal models / systems to answer open-ended questions requiring in-depth understanding of complex documents (including financial reports and academic papers). 

Besides the benchmark datasets, the paper offers a retrieval-aware tuning framework to explore the solutions to solve the problem. The retrieval-augmented tuning approach improves model performance by guiding attention to relevant content while ignoring distractions.

### Strengths
1. M-LongDoc provides a new benchmark. It is different from existing multimodal document visual question answering benchmarks, such as MP-DocVQA and DUDE, which is much longer (210 pages in average), and they are all open-ended questions (not extractive QA or short answer QA). 

2.  The paper proposes a retrieval-aware tuning to improve multimodal model performance on M-LongDoc benchmarks, a strategy that could benefit applications requiring nuanced document comprehension.

### Weaknesses
1. All questions in the benchmark are synthetically generated by multimodal LLMs, which may limit the benchmark's reflection of real-world scenarios. Human annotations are not involved in the benchmark creation process.

2. The dataset's scale is relatively modest (only 852 samples), potentially insufficient for capturing a wide range of perspectives and real-world scenarios.

3. Evaluation relies on proprietary LLMs, introducing potential variability due to different checkpoints or versions. 

4. Some related works are missing [1], the differences are not discussed.

[1] DocBench: A Benchmark for Evaluating LLM-based Document Reading Systems

### Questions
1. How would direct text extraction and retrieval perform as an alternative to solve the problem? What are the performance on text-only questions? What are the performance on multimodal questions?

2.  Retrieval tuning appears to yield only marginal performance gains. What specific challenges in retrieval are contributing to this limited improvement, and how do they align with the unique requirements of M-LongDoc?

### Soundness
3

### Presentation
3

### Contribution
2
