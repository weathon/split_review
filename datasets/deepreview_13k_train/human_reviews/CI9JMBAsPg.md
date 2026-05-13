# DocGenome: A Large Benchmark for Multi-Modal Language Models in Real-World Academic Document Understanding

- Decision: Reject
- Scores: 6, 5, 6, 8

## Abstract
Scientific documents record research findings and valuable human knowledge, comprising a vast corpus of high-quality data. Thus, leveraging multi-modality data extracted from these documents and assessing large models' abilities to handle scientific document-oriented tasks is meaningful. Despite promising advancements, large models still perform poorly on multi-page scientific document extraction and understanding tasks, and their capacity to process within-document data formats such as charts and equations remains under-explored. To address these issues, we present DocGenome, a structured document dataset constructed by annotating 500K scientific documents from 153 disciplines in the arXiv open-access community, using our custom auto-labeling pipeline. DocGenome features four characteristics: 1) Completeness: It is the first dataset to structure data from all modalities including 13 layout attributes along with their LaTeX source codes. 2) Logicality: It provides 6 logical relationships between different entities within each scientific document. 3) Diversity: It covers various document-oriented tasks, including document classification, visual grounding, document layout detection, document transformation, open-ended single-page QA and multi-page QA. 4) Correctness: It undergoes rigorous quality control checks conducted by a specialized team. We conduct extensive experiments to demonstrate the advantages of DocGenome and objectively evaluate the performance of current large models on our benchmark.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposed a new dataset for academic document understanding. By processing 500k documents from arXiv (using their source LaTeX files) the authors create a new large dataset which covers diverse disciplines, preserves data in all modalities from papers, and covers 7 document-oriented tasks. 
The paper describes its automatic processing and labeling pipeline, along with the two metrics used for quality assurance. The authors then describe how the dataset is split into train and test subsets; where the data is divided into tiers based on the previously mentioned metrics and 1004 papers are sampled from the top tier. 
The sampled papers are them used to create QA pairs about their content (both single-page and multi-page questions) using GPT-4V, which are them validated by professional faculty members.
The paper also present the benchmarking of different LLMs on its test set, along with the usage of its training data to effectively create new models that outperform selected baselines.

### Strengths
The paper presents a new large dataset of multi-modality academic documents for document-understanding tasks. This is a welcome and useful target as most existing datasets are limited in scope, diversity, and especially do not preserve all modalities of data in the source papers, losing important information.

The process to create the dataset is well presented and pragmatic and both the toolset and processed data can be valuable in themselves or for further collections and annotations for new tasks. 

While somewhat small when compared to the overall collected data, the annotated test set with questions is shown to be already a useful benchmark for recent large multi-modality models.

### Weaknesses
1. While datasets and benchmarking are important to drive research, the paper does not contain research contributions.
2. The documents are based on latex formatted documents which is a subclass of all documents.

### Questions
With so many different disciplines covered in the data, how exactly were the faculty members selected to review the annotated dataset?

Will the data and codebase be released under a permissive license? With the lack of explicit table-QA or image-QA/chart-QA annotations, for example, it would be critical that the data can be used for re-annotation and extensions.

In line 161 you say \ref commands are removed, but these seem essential in relationship extraction. Also, Table 2 implies they are indeed used.

If GPT-4V was used to create all questions, is there a reason its performance in Table 3 is not so high and even worse than GPT-4o?

How many QA pairs were actually created and used? My understanding is that 4 QA pairs are created per sample, but only 3k total QA pairs were kept? Did I miss some details on how this was filtered?

Please provide more details on the sampled data for the OOD experiments. This data should also be released for reproducibility.

### Soundness
3

### Presentation
3

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
Long  document understanding is an interesting and complex problem. The paper provides a document processing pipeline and a large and diverse collection of documents for academic document understanding. The paper also evaluates the performance of large models on multiple tasks using the benchmark dataset.

### Strengths
As shown in Table 1 of the paper, the document collection is superior to existing collections on multiple aspects.

### Weaknesses
1.  Overall this paper feels like a resubmission from venues like the
    NeurIPS dataset and benchmark track. The methodology contribution is
    relatively weak: the method of creating the dataset (i.e., parsing
    latex sources) is not novel (e.g., a lot of earlier work like GROTOAP, PubLayNet, DocBank, all use similar approaches ),
    neither is the framing of the tasks (all these tasks have been
    studied before to some extent). I am inclined to a borderline reject
    unless the authors can give a strong statement in terms of the
    novelty of the dataset or the methodology.

2.  While I find there could be one potentially novel aspect of the
    dataset---the "13 categories of component units and 6 types of
    logical relationships between them", it is not clear how the authors
    actively use this component in the experiments. (The empirical
    studies mostly focus on using individual components but not the
    relationships.) I'd encourage the authors to provide more
    insights/experiments on this.

3.  There's another limitation of the datasets: since it is curated via
    automatically parsing latex sources, the variance and the structure
    could be limited, and the trained models might not be able to
    transfer to other types of papers (which is also mentioned by the
    authors in line 458.)

### Questions
1. Is the collection representative of scientific documents? In other words, does latex formatting constrain documents in some way? For example, latex denotes non-existing references by ??. If a document is created using other formatting software, such mistakes are not flagged.

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
The main contribution of this paper is a dataset called DocGenome that
is curated mostly automatically.

1.  The main component of paper is a dataset 500k samples of structured
    representation of academic papers. The author developed a pipeline
    to automatically parse the latex source.

2.  The authors also curate a test set of 7 tasks (vision-only,
    language-only, and multi-modal) to evaluate the performance of
    models on the dataset.

3.  The author also verified that the training data could be helpful and
    lead to better performance on downstream tasks via training on
    DocGenome data.

### Strengths
1.  The paper is nicely written, and there authors have conducted a lot
    of experiments evaluating different aspects of this dataset.

2.  The dataset, as well as the document conversion pipeline, could be a
    helpful resource for the community.

### Weaknesses
1. The QA data creation process depends heavily on GPT-4. As the QA pairs are generated by GPT-4, it can introduce biases regarding the type and difficulty of the questions. Further examinations into the potential biases would therefore be beneficial. Specifically, the reliance on a single model for question generation may lead to a lack of diversity in question types, potentially favoring questions that are easily answered by the model itself, while neglecting more challenging or nuanced questions that require deeper understanding of the document content. This could skew the evaluation results and limit the generalizability of the dataset.

2. The evaluation metrics used for different tasks could be improved. Specifically, edit distance or BLEU may not accurately evaluate Equation-to-LaTeX and Table-to-LaTeX tasks, as these metrics do not account for the semantic equivalence of different LaTeX expressions. For instance, two LaTeX expressions might have different syntax but represent the same mathematical equation or table structure. Additional evaluation could also be performed to verify the grammatical correctness of generated LaTeX expressions. Moreover, Open-ended QA tasks are evaluated using GPT-4 to compare reference and generated answers. While this is likely a reasonable approach, human evaluation to verify the reliability of GPT-4’s judgment would be beneficial. The use of a single model for evaluation introduces a potential bias, as the evaluation may favor responses that align with the model's own understanding, rather than reflecting true accuracy or human-like comprehension.

### Questions
1.  The author mentioned that "Each QA pair is reviewed by three
    reviewers for cross-verification." (line 310) It would be great if
    the authors can provide more details in terms of the inter-annotator
    agreement or additional details. "Finally, the two
    manually-evaluated results, along with the automatically-evaluated
    result are cross-verified with the original text to ensure accuracy
    and consistency" (line 317) I am not sure how this process works,
    can you provide more details?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work presents a large-scale multimodal academic document understanding dataset. It includes training and high-quality test sets, along with 7 benchmarking tasks proposed. The manuscript provides a clear description of the data collection and quality control processes. A series of large multi-modal models are benchmarked on the proposed test set, and training experiments are conducted to verify the effectiveness of the proposed training set.

### Strengths
1. The proposed large-scale multimodal academic document understanding dataset makes a solid contribution to the related research community, especially given the scarcity of such datasets.

2. The dataset collection and quality control are carefully designed, executed, and documented. The provided anonymous GitHub repository includes detailed documentation and links for downloading the dataset, supporting reproducibility and accessibility.

3. A training set is provided along with the test set, and training experiments are conducted to verify the effectiveness of the training set.

### Weaknesses
1. The QA data creation process depends heavily on GPT-4. As the QA pairs are generated by GPT-4, it can introduce biases regarding the type and difficulty of the questions. Further examinations into the potential biases would therefore be beneficial.

2. The evaluation metrics used for different tasks could be improved. Specifically, edit distance or BLEU may not accurately evaluate Equation-to-LaTeX and Table-to-LaTeX tasks, as these metrics do not account for the semantic equivalence of different LaTeX expressions. Additional evaluation could also be performed to verify the grammatical correctness of generated LaTeX expressions. Moreover, Open-ended QA tasks are evaluated using GPT-4 to compare reference and generated answers. While this is likely a reasonable approach, human evaluation to verify the reliability of GPT-4’s judgment would be beneficial.

### Questions
1. The manuscript discusses that the GPT-4-generated QA pairs are verified and updated by human annotators. What is the acceptance rate of the original QA pairs, or alternatively, what is the editing rate? Given that GPT-4 achieves around 60%-70% accuracy on QA tasks in Table 3, this suggests that a substantial portion of the QA pairs were likely updated.

2. Why are large multimodal models (e.g., GPT-4V, QWen-VL) not benchmarked on the Equation-to-LaTeX and Table-to-LaTeX tasks?

### Soundness
3

### Presentation
3

### Contribution
3
