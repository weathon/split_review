# LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
With the rapid development of AI-generated content, the future internet may be inundated with synthetic data, making the discrimination of authentic and credible multimodal data increasingly challenging. Synthetic data detection has thus garnered widespread attention, and the performance of large multimodal models (LMMs) in this task has attracted significant interest. LMMs can provide natural language explanations for their authenticity judgments, enhancing the explainability of synthetic content detection. Simultaneously, the task of distinguishing between real and synthetic data effectively tests the perception, knowledge, and reasoning capabilities of LMMs. In response, we introduce LOKI, a novel benchmark designed to evaluate the ability of LMMs to detect synthetic data across multiple modalities. LOKI encompasses video, image, 3D, text, and audio modalities, comprising 18K carefully curated questions across 26 subcategories with clear difficulty levels. The benchmark includes coarse-grained judgment and multiple-choice questions, as well as fine-grained anomaly selection and explanation tasks, allowing for a comprehensive analysis of LMMs. We evaluated 22 open-source LMMs and 6 closed-source models on LOKI, highlighting their potential as synthetic data detectors and also revealing some limitations in the development of LMM capabilities. More information about LOKI can be found at \url{https://opendatalab.io/LOKI/}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces a novel benchmark designed to evaluate the capability of LMMs in detecting synthetic data across multiple modalities, including video, image, 3D, text, and audio. LOKI is structured to provide diverse modalities, cover 26 detailed categories, and offer multi-level annotations, enabling tasks that range from basic authenticity judgments to fine-grained anomaly selection and explanation. The benchmark consists of 18,000 questions across various levels of difficulty, allowing for a comprehensive analysis of LMMs in detecting synthetic content. Additionally, the paper includes evaluations of 22 open-source and 6 closed-source LMMs, revealing both the potential and current limitations of these models in terms of detection accuracy and interpretability.

### Strengths
+ LOKI is a novel, multimodal dataset.

+ The paper is easy to read and well-organised.

+ Comprehensive Evaluation and Validation.

+ Curates a diverse dataset with 18,000 questions across five modalities and 26 categories, providing a solid foundation for synthetic data detection evaluation.

+ Detailed Annotations.

+ Directly addresses the challenges of synthetic data proliferation, impacting security, misinformation, and content authenticity.

+ LOKI’s findings on LMM strengths and weaknesses have the potential to drive advancements in synthetic data detection and multimodal model development.

### Weaknesses
-  The benchmark lacks a robustness test against common real-world conditions like compression artifacts. To enhance real-world applicability, the authors could include performance evaluations on compressed data.

### Questions
No follow-up questions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors introduce  LOKI, a novel benchmark designed to evaluate the ability of LMMs to detect synthetic data across multiple modalities. With the concurrent preponderance of synthetic data and the rise of powerful LLMs, the authors aim to address the emerging research topic of LMM evaluation for synthetic data detection. LLMs can provide reasoning behind authenticity judgments, benefitting explainability. The focus of LOKI is to evaluate the performance of LLMs on synthetic data detection tasks. 

In particular, LOKI is aimed at addressing several shortcomings present in extant synthetic data evaluation datasets, including emphasizing human interpretability and multimodality. Overall, LOKI provides key improvements to synthetic data detection, including: diverse modalities, heterogenous categories, multi-level annotations and multimodal synthetic evaluation. framework.

### Strengths
The paper is well-written and easy to follow.

This work addresses a glaring and emergent need in a topic field: synthetic data detection for LLMs; I agree with the authors that there doesn't currently exist a comprehensive, multi-modal, nuanced dataset including explainability assessment for this domain area. 

Extensive examples and case studies provided in appendices. 

Many data domains are covered in this benchmark, including several categories and characteristics that are often underrepresented in synthetic data detection (e.g., satellite images, "abnormal details").

### Weaknesses
While the differentiated modalities, categories and annotation levels are beneficial, the overall size of the dataset actually seems relatively small vis-a-vis related datasets (Table 1).

It is unclear to me, how a user can methodically compare scores for different models across tasks/categories (e.g., in Table 2); perhaps the authors can address this, given the heterogenous and imbalanced nature of the data modalities and tasks, as well as the problem/domain "difficulty".

As deepfake detection is one of the most prominent synthetic data detection categories today, I believe the benchmark would benefit from its inclusion.

### Questions
Do you have a sense as to why the prompting strategies (FS, CoT) in general had a poor/neutral impact for most of the model/data pairs (Table 5)?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces LOKI, a novel benchmark for evaluating large multimodal models (LMMs) in detecting synthetic data across multiple modalities, such as video, image, text, and audio.This benchmark features broad-level assessments, including judgment and multiple-choice tasks, alongside detailed anomaly selection and explanation exercises, providing an in-depth evaluation of large multimodal models (LMMs).

### Strengths
1.	The paper is well written and easy to follow. The authors provide sufficient technical details for readers to understand their work.
2.	The benchmark designed by the authors encompasses a rich variety of modalities and diverse question types, enabling a comprehensive evaluation of LMM performance.
3.	The authors introduce a metric called the Normalized Bias Index (NBI) to quantify the performance differences of the model on natural and AI-generated data across different modalities, which is an innovative way to assess model bias.

### Weaknesses
1.	The current evaluation mainly relies on accuracy and NBI; however, at low recall rates, NBI may not adequately reflect model bias. Additionally, the design of NBI may be insufficient to comprehensively capture various types of bias exhibited by the model. Specifically, the NBI metric, while useful for summarizing overall bias, may not capture nuanced biases that manifest differently across various types of synthetic data or at different levels of model confidence. For instance, a model might perform well on average but exhibit significant bias towards specific types of synthetic images, which the NBI could mask.
2.	The paper mentions that the model exhibits "bias" across different modalities. However, the specific causes of this bias are not thoroughly explored through experiments or comparative analysis. This conclusion may be based on surface-level observations without further investigation into whether the bias arises from data, model architecture, or task design. The paper should include a more detailed investigation into the source of the bias, such as analyzing the model's performance on different subsets of the data or comparing models with different architectures.
3.	The paper mentions that the Chain-of-Thought (CoT) approach can impact model performance in image and 3D reasoning tasks.  However, it does not provide sufficient experimental details to clarify whether CoT significantly enhances performance across all types of tasks or if it is only effective for the specific tasks currently evaluated. It is unclear if the observed improvements are consistent across different question types (e.g., multiple-choice, anomaly selection) or if CoT is only beneficial for specific reasoning tasks. The paper should include a more thorough analysis of the impact of CoT across different task types and modalities.
4.	It is suggested to discuss and compare more related works such as [1,2] in this paper.

### Questions
1.	In the fine-grained anomaly selection task, all samples were manually reviewed to ensure question quality. However, how can the robustness of the task design be ensured in future large-scale applications?
2.	Could you provide additional insights into why Claude-3.5-Sonnet tends to misclassify synthetic images as real? For instance, does this result from limitations in the model's ability to recognize fine-grained abnormalities, or are there certain types of synthetic image features that are particularly challenging for the model?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces LOKI, a comprehensive benchmark designed to evaluate the capabilities of Large Multimodal Models in detecting synthetic data across multiple modalities. Recognizing the rapid advancement of AI-generated content and the associated risks of synthetic media proliferation, the authors aim to assess how well LMMs can discern real data from AI-generated counterparts.

LOKI encompasses a diverse set of data modalities, including video, image, 3D models, text, and audio, covering 26 detailed subcategories such as satellite images, medical images, philosophical texts, and various audio types like music and environmental sounds. The benchmark includes over 18,000 carefully curated questions with varying levels of difficulty.

The tasks within LOKI are multi-faceted:

Judgment Tasks: Binary classification to determine if a piece of data is real or AI-generated.
Multiple-Choice Questions: Selecting the AI-generated item from a set of options.
Abnormal Detail Selection: Identifying specific anomalies in synthetic data.
Abnormal Explanation Tasks: Providing explanations for why data is identified as synthetic.
The authors evaluated 22 open-source LMMs and 6 closed-source models (including GPT-4 and Gemini) using LOKI. Their findings highlight that while LMMs show promise in synthetic data detection and offer interpretability advantages over traditional expert models, they also exhibit significant limitations. Models tend to have biases, lack domain-specific knowledge, and display unbalanced performance across different modalities.

### Strengths
- Comprehensive Multimodal Benchmark: LOKI covers an extensive range of data modalities and subcategories.
- Inclusion of specialized domains like satellite imagery, medical images, and philosophical texts pushes the boundaries of traditional datasets and tests models in less-explored areas.
- Multi-Level Task Design: The benchmark doesn't just focus on binary classification but also includes tasks that assess models' abilities to explain their reasoning, promoting the development of interpretable AI systems.
- Highlighting the Importance of Explainability
- By testing perception, knowledge, and reasoning across modalities, LOKI contributes to the broader goal of advancing towards AGI.

### Weaknesses
 - Limited Performance in Certain Modalities: The benchmark reveals that LMMs perform poorly in modalities like 3D and audio, which may be due to the lack of available models or training data in these areas.
- Insufficient Details on Data Generation Methods: The paper could provide more in-depth information on how synthetic data was generated for each modality, which is crucial for reproducibility and understanding potential biases in the dataset.
- Evaluation of Few-Shot and Chain-of-Thought Prompting: The analysis of prompting strategies is somewhat limited.

### Questions
- Quality and Realism of Synthetic Data: How does the synthetic data in LOKI reflect the latest advancements in generative models? Are there measures taken to ensure that the synthetic data poses a realistic challenge for detection models?
- Prompting Strategies Implementation: Could you elaborate on how chain-of-thought and few-shot prompting were implemented across different models? Specifically, how did these strategies impact models that are less capable of handling long contexts or reasoning tasks?

### Soundness
3

### Presentation
3

### Contribution
4
