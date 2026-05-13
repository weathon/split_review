# Is Cognition consistent with Perception? Assessing and Mitigating Multimodal Knowledge Conflicts in Document Understanding

- Decision: Reject
- Scores: 5, 5, 5, 3

## Abstract
Multimodal large language models (MLLMs) have shown impressive capabilities in document understanding, a rapidly growing research area with significant industrial demand in recent years.
    As a multimodal task, document understanding requires models to possess both perceptual and cognitive abilities.
    However, current MLLMs often face conflicts between perception and cognition.
    Taking a document VQA task (cognition) as an example, an MLLM might generate answers that do not match the corresponding visual content identified by its OCR (perception).
    This conflict suggests that the MLLM might struggle to establish an intrinsic connection between the information it ``sees'' and what it ``understands.''
    Such conflicts challenge the intuitive notion that cognition is consistent with perception, hindering the performance and explainability of MLLMs.
    In this paper, we define the conflicts between cognition and perception as \textit{Cognition and Perception (C\&P) knowledge conflicts}, a form of multimodal knowledge conflicts, and systematically assess them with a focus on document understanding.
    Our analysis reveals that even GPT-4o, a leading MLLM, achieves only 68.6\% C\&P consistency.
    To mitigate the C\&P knowledge conflicts, we propose a novel method called \textit{Multimodal Knowledge Consistency Fine-tuning}. 
    This method first ensures task-specific consistency and then connects the cognitive and perceptual knowledge. 
    Our method significantly reduces C\&P knowledge conflicts across all tested MLLMs and enhances their performance in both cognitive and perceptual tasks in most scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores the capability of large multimodal models in understanding document images. The authors highlight that current multimodal large models often provide conflicting extraction results in "perception" tasks (i.e., OCR) and "cognition" tasks (i.e., VQA based on document images). To address this issue, the authors introduce a metric to compute cognition-perception (C&P) consistency and construct a multi-task fine-tuning dataset based on OCR annotations. Experiments demonstrate that the proposed fine-tuning method significantly improves C&P consistency across three models with sizes ranging from 2B to 8B parameters.

### Strengths
1. This work highlights a noteworthy issue: an (M)LLM's factual understanding of identical content can vary depending on contextual differences.
2. The joint OCR-VQA dataset proposed in this paper may benefit future research in related topics.

### Weaknesses
1. Insufficient Experimental Results on C&P Conflict Causes and Impact: The paper does not provide extensive experimental results on the root causes of C&P conflicts or a detailed analysis of their impact on downstream tasks. While it demonstrates the existence of these conflicts and the effectiveness of the proposed method in reducing them, a deeper investigation into why these conflicts occur and how they specifically affect performance in various tasks could strengthen the paper's contributions. For example, the paper lacks a systematic analysis of whether these conflicts arise more frequently with certain types of document layouts, text complexities, or question types. Furthermore, the impact of these conflicts on specific downstream tasks, such as information extraction or document summarization, is not explored, leaving a gap in understanding the practical significance of the problem.

2. The applicability of the Multimodal Knowledge Consistency Fine-tuning method is discussed in the context of document understanding but may require further discussion for broader multimodal tasks. The paper could benefit from exploring how well these findings generalize to other domains beyond document understanding, such as scene understanding or visual reasoning. The current scope limits the impact of the work, as the proposed method's effectiveness in other domains remains unclear. For example, it is not clear if the same C&P conflicts would manifest in tasks involving natural images and complex visual scenes, or whether the proposed fine-tuning method would be as effective in those contexts.

3. The paper does not explore whether C&P conflicts can be mitigated through simple in-context learning strategies, such as performing VQA followed by OCR based on the previous context, or vice versa. This approach might provide insights into whether the conflicts are resolvable with less complex interventions. The lack of exploration of in-context learning leaves open the possibility that the observed conflicts are not fundamental limitations of the models but rather artifacts of the evaluation setup. A comparison with in-context learning approaches would provide a more comprehensive understanding of the problem.

4. The paper treats C&P conflict primarily as a consistency issue. However, it does not provide statistics on cases where the model's output consistency is low due to a failure to follow instructions correctly. Differentiating between consistency issues and instruction-following issues could offer a more nuanced understanding of the conflicts. It is crucial to determine whether the observed inconsistencies are due to genuine conflicts in the model's knowledge or simply due to the model's inability to adhere to the given instructions. Without this distinction, the analysis of C&P conflicts remains incomplete.

5. Ablation Study Metrics: The ablation study in Table 5 focuses on consistency metrics but does not include corresponding accuracy or F1 scores. Providing these metrics would offer a more comprehensive view of the method's performance, especially in terms of the trade-offs between consistency and accuracy. The absence of accuracy and F1 scores makes it difficult to assess whether the improvement in consistency comes at the cost of reduced performance on the individual tasks. A more complete evaluation would include both consistency and task-specific performance metrics.

### Questions
1. Can C&P conflicts be addressed or mitigated through simple in-context learning? For example, first performing VQA (OCR) and then conducting OCR (VQA) based on the previous context.
2. Is C&P conflict entirely a consistency issue? If the model does not follow the current instructions, the output consistency will naturally be lower. Could the authors provide statistics on the proportion of such cases?
3. The ablation study in Table 5 only presents the consistency metrics without corresponding accuracy or F1 scores. Could the authors provide these relevant metrics?
4. On tasks where the model already performs well, does C&P fine-tuning lead to a decline in performance?

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
Document understanding, as a multimodal task, requires models to accurately perceive visual content (perception) and then generate coherent responses (cognition) based on this perception. However, current multimodal large language models (MLLMs) often encounter conflicts between perception and cognition. For example, a model may use its OCR capabilities (perception) to recognize text within an image as "A" but then respond to a related question by providing a similar yet incorrect word, "B." In this paper, the authors define these intrinsic conflicts between cognitive knowledge and perceptual knowledge within MLLMs as *Cognition and Perception (C&P) knowledge conflicts*, leading to inconsistent responses involving cognition and perception. They conduct a systematic evaluation of current MLLMs to assess the prevalence of these conflicts in document understanding, demonstrating that such conflicts are indeed widespread. To address this issue, the authors propose a fine-tuning method called *Multimodal Knowledge Consistency Fine-tuning*, which aims to mitigate these conflicts.

### Strengths
1. **Clear Experimental Evidence:** The study provides a clear statistical presentation of answer inconsistencies in MLLM responses when different question formats are used, effectively highlighting the inconsistency issue in MLLMs.

2. **Definition of C&P Knowledge Conflicts:** The paper attempts to systematically define these inconsistencies as *Cognition and Perception (C&P) knowledge conflicts*, offering a detailed definition of the term.

3. **Systematic Evaluation of Existing Models:** It conducts a comprehensive assessment of existing MLLMs to evaluate the prevalence and nature of C&P knowledge conflicts, offering valuable insights into current model limitations.

4. **Proposed Fine-Tuning Method:** The authors propose a fine-tuning method incorporating three specific training tasks, aimed at enhancing consistency between cognition and perception in MLLMs.

### Weaknesses
1. **Lack of Robust Explanation for C&P Conflicts:** The attribution of answer inconsistencies across different questioning formats solely to Cognition and Perception (C&P) knowledge conflicts lacks a thorough explanation. The authors could strengthen this claim by including experiments that control for potential randomness in MLLM responses. For example, they could ask the same question multiple times with identical phrasing to observe whether inconsistencies persist under uniform questioning formats, which would help determine if the issue is rooted in C&P conflicts or random model behavior.

2. **Insufficient Consideration of OCR Limitations in Defining C&P Conflicts:** Given that high OCR accuracy is critical for intensive document understanding tasks, the definition of C&P knowledge conflicts should more carefully account for OCR limitations. The authors might include experiments to isolate and assess OCR capabilities, such as by using extracted OCR text as an auxiliary input (similar to the approach in TextVQA datasets) or by implementing other techniques to reduce OCR-related inconsistencies. This would help clarify whether observed C&P conflicts stem from limitations in OCR or from other aspects of the model's perception and cognition alignment.

3. **Limited Novelty in Fine-Tuning Approach:** While the proposed fine-tuning method appears effective in reducing inconsistencies, it essentially involves fine-tuning a general-purpose multimodal LLM on a document-understanding dataset, resulting in a specialized model for this particular task. Although this is a practical solution, it represents a relatively common approach in MLLM research and may lack innovation. Additionally, this specialization may come at the cost of the model's broader capabilities as a general-purpose MLLM. To enhance the study's impact, the authors could address these limitations by presenting results on more general benchmarks, which would demonstrate that their fine-tuning method improves consistency in document understanding without sacrificing the model's performance on other tasks, thereby reinforcing its relevance for broader MLLM applications.

### Questions
See weakness.

### Soundness
3

### Presentation
3

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
This submission discusses the concept of Cognition and Perception knowledge conflicts in MLLMs and proposes a method to mitigate these conflicts in document understanding tasks. ​ The proposed method includes three fine-tuning tasks aimed at improving consistency between cognitive and perceptual knowledge. ​ Experimental results demonstrate that this approach significantly enhances C&P consistency and overall performance in both cognitive and perceptual tasks.

### Strengths
There are several noticeable strengths in this paper:
* This paper sets eye on a new research area and presents a well-justified motivation for examining the conflicts between cognition and perception knowledge of MLLMs.
* This submission conducts extensive experiments to examine current open-source and closed-source MLLMs performance on the cognition and perception knowledge conflict problems, and to verify the effectiveness of the proposed finetuning method.
* The manuscript is commendable for its clarity and structured writing style, which greatly facilitates reader comprehension.
* Additionally, the inclusion of clear and illustrative figures and tables is a notable strength, as it significantly aids in conveying the main claims of the paper to the audience.

### Weaknesses
My main criticism for this submission is on its experimental design:

* **Limited Reproducibility**: Although the submission provides links to the model and weights, details about the hyperparameters used during inference are missing (e.g., values for top_p, top_k, temperature, beam search, etc). This lack of transparency makes it difficult to ensure fair comparisons across models and affects reproducibility. It is crucial to specify these parameters as they can significantly influence the output of MLLMs, leading to different performance results.
* **Lack of Repeated Experiments**: The authors did not report the mean and standard deviation of the experimental results, nor did they specify any settings for repeated runs, suggesting that results may have been obtained from a single inference run. However, LLMs and MLLMs often yield varying outputs across runs due to their inherent generation variability. How do the authors account for this potential source of instability when attributing results solely to conflicts in cognitive or perceptual knowledge, rather than to the natural output variability of the models? The absence of statistical measures makes it difficult to assess the robustness of the findings.

### Questions
Please refer to the Weaknesses above.

### Soundness
2

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
4

### Summary
This paper introduces the concept of Cognition and Perception Knowledge Conflicts to measure the discrepancy between perceptual and cognitive abilities in multimodal large language models (MLLMs). Through experiments focused on document understanding, it demonstrates a significant gap between these two abilities. Additionally, the paper proposes a tuning method, Multimodal Knowledge Consistency Fine-tuning, which effectively reduces this gap, mitigating the conflict between cognitive and perceptual knowledge.

### Strengths
- This paper introduces a new concept, Cognition and Perception Knowledge Conflicts, to investigate the behavioral discrepancy between the cognitive and perceptual abilities of MLLMs.

- This paper proposes a tuning method to mitigate the conflict by constructing a new dataset for training.

### Weaknesses
 - The concept of Cognition and Perception knowledge conflicts is not entirely convincing:
  - The task used to measure the model's cognitive abilities does not seem to require much cognitive processing. The VQA tasks, which primarily involve extracting text present in the image, do not necessitate complex reasoning or inference. This raises concerns about whether the observed discrepancies truly reflect a conflict between cognitive and perceptual knowledge, or simply a limitation in the model's ability to perform basic text extraction and matching.
  - The tasks used in these experiments are limited in scope. Focusing solely on document understanding, with tasks like OCR and VQA on document images, restricts the generalizability of the findings. It is unclear whether the observed C&P conflicts would manifest similarly in other multimodal scenarios, such as scene understanding or video analysis, which involve more diverse and complex perceptual and cognitive processes.

- It is unclear whether the low C&P consistencies arise from C&P knowledge conflicts or simply from poor model performance:
  - The varying consistency scores across different datasets in Table 2 suggest that the conflict may not be an inherent property of the model itself but rather linked to its performance on specific tasks. The fact that consistency varies significantly across datasets indicates that the observed inconsistencies might be task-specific artifacts rather than a fundamental conflict within the model's architecture.
  - Empirical results in Table 4 show that improvements in C&P performance appear related to increases in cognitive and perceptual abilities, supporting the idea that C&P knowledge conflicts might stem from the models' poor performance. This correlation suggests that the proposed conflict might be a consequence of the model's overall performance limitations, rather than a distinct phenomenon.

### Questions
Line 071 : What exactly does 'the intuitive notion that cognition is consistent with perception' mean?

### Soundness
2

### Presentation
2

### Contribution
2
