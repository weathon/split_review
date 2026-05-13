# MRAG-Bench: Vision-Centric Evaluation for Retrieval-Augmented Multimodal Models

- Decision: Accept
- Scores: 5, 6, 5, 6, 6

## Abstract
Existing multimodal retrieval benchmarks primarily focus on evaluating whether models can retrieve and utilize external \textit{textual knowledge} for question answering. However, there are scenarios where retrieving visual information is either more beneficial or easier to access than textual data. %not only more beneficial but also easier than accessing textual data. 
In this paper, we introduce a \textbf{m}ultimodal \textbf{r}etrieval-\textbf{a}ugmented \textbf{g}eneration benchmark, \dataset, in which we systematically identify and categorize scenarios where visually augmented knowledge is better than textual knowledge, for instance, more images from varying viewpoints.
\dataset consists of 16,130 images and 1,353 human-annotated multiple-choice questions 
across 9 distinct scenarios. With \dataset, we conduct an evaluation of 10 open-source and 4 proprietary large vision-language models (LVLMs). Our results show that all LVLMs exhibit greater improvements when augmented with images compared to textual knowledge, confirming that \dataset is vision-centric. 
Additionally, we conduct extensive analysis with \dataset, which offers valuable insights into retrieval-augmented LVLMs. Notably, the top-performing model, GPT-4o, faces challenges in effectively leveraging retrieved knowledge, achieving only a 5.82\% improvement with ground-truth information, in contrast to a 33.16\% improvement observed in human participants. 
These findings highlight the importance of \dataset in encouraging the community to enhance LVLMs' ability to utilize retrieved visual knowledge more effectively.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a Multimodal Retrieval-Augmented Generation Benchmark (MRAG-Bench) to analyze and identify scenarios where visually augmented knowledge is better than textual one. MRAG-Bench comprises 16,130 images and 1,353 human-annotated multiple-choice questions, covering nine distinct scenarios. The authors analyze the performance of 10 open-source and 4 proprietary large vision-language models (LVLMs). Their results show that all the LVLMs exhibit performance improvement when augmented with visual data rather than textual. Moreover, the proprietary models can better leverage the retrieved visual information.

### Strengths
The paper is well-structured and accessible, presenting a benchmark for evaluating and analyzing the relevance of visually augmented samples across various scenarios. For example, it considers cases where the main object in an image is partially occluded or where the image depicts an outdated or modified version of the object. The authors conduct extensive experiments with both proprietary and open-source methods, demonstrating that visual augmentation offers greater utility than textual information for large vision-language models (LVLMs).

### Weaknesses
While the paper is easy to follow, the primary motivation behind the task remains unclear. In a real-world scenario, how would this pipeline function operationally? Given the findings that visually augmented samples offer significant value, an extensive repository of curated and labeled images for retrieval would be essential. However, this may be impractical due to legal and computational restrictions. Additionally, I would be interested in analyzing how the incorporation of augmented images affects response time and costs. Furthermore, the paper does not address the potential for the model to over-rely on retrieved visual information, potentially ignoring the original input image. This is particularly concerning when the question directly pertains to the input image. Finally, the evaluation using multiple-choice questions may not fully capture the performance of instructional models, as these models are typically used for open-ended question answering. The use of retrieved images could also inadvertently increase the hallucination rate of these models in open-ended scenarios.

### Questions
1. Could you elaborate on your motivation for creating this benchmark? Please include examples of real-world applications where this benchmark could offer substantial value.

2. Using this benchmark in real-world applications could be challenging, as it would require a comprehensive image repository encompassing a wide range of objects globally. This need introduces various limitations, such as legal and computational restrictions and the necessity for thorough curation to prevent biased or intrusive content. Could you discuss potential strategies for making this benchmark feasible in real-world scenarios, as well as approaches to mitigate these limitations?

3. Increasing context (whether visual or textual) means that large language models (LLMs) would need to process longer input sequences, which would raise inference times. Since images are typically represented as lengthy sequences, adding more images could substantially impact both inference time and associated costs, especially in the case of proprietary models, which gain the most from visual augmentation. Could you provide a detailed analysis of the trade-offs between performance gains, increased costs, and extended inference times?

### Soundness
2

### Presentation
2

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
This paper introduces a benchmark (MRAG-BENCH) designed to evaluate the performance of large vision-language models (LVLMs) in scenarios where visual information retrieval is more beneficial than textual data retrieval. First, this paper establishes the first benchmark focusing on visual information superiority over textual data. Second, this paper conducts an extensive analysis of LVLMs, and makes detailed analyses. Third, this paper points out a way that LVLMs could be evaluated and improved by emphasizing the importance of visual information in retrieval-augmented multimodal tasks.

### Strengths
1. The paper is well-written and easy to follow.
2. The paper offers a different visual-centric perspective and addresses a gap in the current text-centric benchmarks.
3. The comprehensive evaluation of multiple LVLMs provides valuable insights, such as how visual knowledge benefits LVLMs over textual knowledge, and the examination of retriever performance and its impact on LVLM accuracy.

### Weaknesses
1. The process of selecting ground-truth images and query images may introduce bias if not carefully controlled. The paper could be strengthened by discussing potential biases in the data collection process and how they were mitigated. Specifically, the manual selection of 5 ground truth images per question introduces a potential for selection bias, as different annotators might choose different sets of images. This could lead to inconsistencies in the benchmark's evaluation criteria.
2. The paper focuses on a specific set of scenarios, which may not scale well to other types of visual queries or more complex tasks. For example, what if there are many objects in the question? The current benchmark may not adequately address scenarios where multiple objects are present in the query image, potentially limiting its applicability to more complex real-world situations. The paper should discuss how the benchmark might be extended to handle such cases, including the challenges in retrieving relevant visual information when multiple objects are involved.
3. The paper could further discuss the implications of the findings, such as how they might influence the development of future LVLMs. The analysis lacks a deeper discussion on how the findings can be translated into actionable insights for improving LVLMs. For example, the paper could explore specific architectural changes or training strategies that could address the identified limitations in current models.

### Questions
1. How to conduct the process of human evaluation? For example, how many annotators were involved in evaluating each question, and what measures were taken to ensure consistency and accuracy in their assessments?
2. In Table 3, there are two human evaluation settings. How do you ensure that human annotators do not rely on their own knowledge when answering questions, and what steps have you taken to mitigate any potential biases in the human evaluation process
3. Whether retrieving additional visual information also enhance performance in text-intensive scenarios? 
4. The paper does not report the performance of GPT-o1 on MRAG-BENCH. How does GPT-o1 perform on this benchmark?
5. In Section 4.3, the paper shows that further increasing the number of retrieved images does not improve performance. Could the authors explain the reasons behind this effect, and what insights does this provide for future research on retrieval-augmented multimodal models?
6. Will you release this benchmark?

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
This paper introduces MRAG-BENCH, a multimodal retrieval-augmented generation benchmark comprising 16,130 images and 1,353 human-annotated multiple-choice questions across 9 distinct scenarios. The authors evaluate the performance of 10 open-source and 4 proprietary large vision-language models (LVLMs) on this benchmark.

### Strengths
- The authors conduct an investigation into the capability of models to retrieve and utilize external visual knowledge for question answering, which is a crucial and direct exploration within the LVLM field.

- The paper introduces a comprehensive multimodal retrieval-augmented generation benchmark that provides a foundation for the community to further explore and advance in this area.

- Figure 1 is well-designed, with well-chosen examples to illustrate the benchmark's scenarios and model evaluations effectively.

### Weaknesses
 - The data collection process is unclear. Adding a figure to illustrate the entire process could clarify the methodology, especially regarding the acquisition of ground truth (GT) text and the source of question-answer pairs.

- The experimental setup lacks sufficient detail. The authors should provide a complete subsection dedicated to describing the experimental setup, placed within Section 3, instead of scattering brief descriptions across various sections. This current layout diminishes the reliability of the experimental conclusions. For example, in Table 3 (Retrieved RAG), it’s unclear which model was used as the retriever, what the retriever’s input and output were, etc. Additional concerns regarding the experimental setup are outlined in the Questions section below.

- The analysis of the question, "How much does visual knowledge provide additional benefits over textual knowledge?" is insufficiently supported. Additional experimental analysis would strengthen the authors’ conclusions.

### Questions
- What is the meaning of "Unique number" in Table 2?

- How were the nine scenarios in MRAG-BENCH selected?

- Regarding the "Others" example in Figure 3, why is option A marked as the correct answer? This raises questions about the rule for obtaining question-answer pairs. How is the correct answer determined for each question?

- Could the authors clarify how CLIP is used for text retrieval? Is it a direct approach based on finding the sentence with the highest similarity to the current question, or does it involve a method similar to INFOSEEK [1], where visual entity recognition is performed first, followed by retrieval?

- Concerning Table 3:

  - If human performance on this task is low, how can the quality of GT images be assured during data collection?

  - How is "Human performance" in Table 3 measured?

  - Most open-source LVLMs exhibit performance declines when using Retrieved RAG, suggesting that retrieval effectiveness is crucial to answer quality. If retrieval consistently underperforms, is the entire process reasonable and valid?

- Concerning Table 4:

  - How were the five comparison methods implemented?

  - What is the meaning of GT Text RAG, and how is GT Text collected? Additionally, it seems counterintuitive that LLaVA-Next-Interleave performs worse with GT Text RAG. If adding GT Text RAG degrades model performance, does this suggest that the quality of GT Text might be low?

  - Why does the performance improvement for LLaVA-Next-Interleave, when provided with both GT images and textual knowledge, fall short compared to using GT images alone?

- There appears to be a minor error in Section 4.1, where it states, "LLaVA-Next-Interleave exhibited an 11.09% improvement with image knowledge over text knowledge." Shouldn't this be 11.90%?

### Soundness
2

### Presentation
2

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
- **Introduction of MRAG-BENCH**: The paper introduces **MRAG-BENCH**, a benchmark designed for evaluating retrieval-augmented multimodal models, focusing on scenarios where visual information is more beneficial than textual data. MRAG-BENCH consists of **16,130 images** and **1,353 human-annotated multiple-choice questions** across **9 distinct scenarios**.

- **Evaluation and Findings**: The paper evaluates **10 open-source** and **4 proprietary large vision-language models (LVLMs)**, showing that models exhibit greater improvements when augmented with images compared to textual knowledge.

- **Insights and Challenges**: The findings highlight the challenges LVLMs face in effectively leveraging retrieved visual knowledge, emphasizing the need for improved utilization of visually augmented information.

### Strengths
### Originality
- **New Benchmark**: The introduction of MRAG-BENCH is a significant contribution, focusing on vision-centric retrieval-augmented generation, which is less explored compared to text-centric benchmarks. The paper identifies and categorizes scenarios where visual knowledge is more beneficial than textual knowledge, such as perspective and transformative changes, which is a fresh approach in the field.

### Quality
- **Comprehensive Evaluation**: The paper evaluates 10 open-source and 4 proprietary LVLMs using a large dataset of 16,130 images and 1,353 questions, providing robust and extensive analysis.
- **Detailed Analysis**: The results include fine-grained performance metrics across different scenarios, highlighting the strengths and weaknesses of various models.

### Clarity
- **Well-Structured**: The paper is well-organized, with clear sections detailing the benchmark's design, data collection, and evaluation methodology.
- **Illustrative Examples**: Figures and tables, such as the scenario distributions and qualitative examples, effectively illustrate the concepts and findings, making the paper easy to follow.

Overall, the paper makes a substantial contribution to the field of multimodal models by introducing a novel benchmark that highlights the importance of visual knowledge, backed by thorough evaluation and clear presentation.

### Weaknesses
 - The motivation is unclear. In Figure 1, do the authors mean that retrieving from the image corpus is not difficult? While I agree that retrieving correct textual knowledge is challenging, why is retrieving from the image corpus considered easier? Additionally, I do not understand why retrieved correct textual knowledge is deemed not useful, which is confusing[^1^][1]. Please clearly state your motivation.

- How is the image knowledge database handled in the experiments? It is unclear how the authors retrieve the images.

- In my view, visual RAG is more difficult than text RAG. It would be valuable to explore CoT + Visual RAG. For example, in Figure 1, if VLLMs are unsure about the model of the car, they could consider some candidate answers and then use Visual RAG to validate and confirm the final answer. Directly retrieving images is not easy with a large image knowledge database and may sometimes hurt performance when incorrect images are selected.

- I cannot understand why GT Image RAG is better than GT Text RAG in Table 4. Can the authors provide more clarifications and illustrations?

I recommend that authors submit a link to the anonymous repo. It is very important for benchmark to release ASAP. After that, reviewers can check the data quality.

### Questions
Please see weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a new multimodal retrieval-augmented generation benchmark, MRAG-BENCH. In this benchmark the LVLMs are given the input of query image, textual question and retrieved relevant images, and required to answer the multiple choice questions. Evaluations on MRAG-BENCH show the gap between current leading LVLMs and human beings. The authors also have an interesting findings that current open-source LVLMs lack the ability to select useful information from the retrieved images while ignore the irrelevant or misleading retrieved images.

### Strengths
Multimodal RAG is surely an important problem, along the improvement of multi-image understanding ability in current LVLMs. Many cases in the benchmark are close to real world scenarios. The settings of noisy retrieved information is very meaningful and necessary, since in real world multimodal RAG, errors or failures in the retrieval process are inevitable.

### Weaknesses
Some cases in the benchmark might be too ideal for current retrieval systems, for example ,the Angle case and the Deformation case in Figure3. It is unlikely that a multimodal retrieval system (i.e., search engine, multimodal knowledge graph) can retrieve such accurate ground truth image given the query image. The reliance on near-perfect retrieval scenarios limits the benchmark's ability to assess the robustness of LVLMs in real-world conditions where retrieval errors are common. Specifically, the Angle and Deformation cases, which require very precise visual matches, are not representative of typical retrieval outputs, where results are often noisy and contain irrelevant or partially relevant information. This discrepancy between the benchmark's retrieval inputs and real-world retrieval outputs could lead to an overestimation of LVLM performance in practical applications.

### Questions
Suggestions: Maybe the authors can fix the ground truth images and add retrieved images from different retrieval systems (i.e. search engine, different multimodal knowledge graph), so that this benchmark can also be used to evaluate multimodal retrieval systems.

### Soundness
3

### Presentation
3

### Contribution
3
