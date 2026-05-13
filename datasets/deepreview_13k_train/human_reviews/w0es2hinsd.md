# RD2Bench: Toward Data-Centric Automatic R&D

- Decision: Reject
- Scores: 3, 8, 5, 5

## Abstract
The progress of humanity is driven by those successful discoveries accompanied by countless failed experiments. Researchers often seek the potential research directions by reading and then verifying them through experiments. The process imposes a significant burden on researchers. In the past decade, the data-driven black-box deep learning method has demonstrated its effectiveness in a wide range of real-world scenarios, which exacerbates the experimental burden of researchers and thus renders the potential successful discoveries veiled. Therefore, automating such a research and development (R\&D) process is an urgent need. In this paper, we serve as the first effort to formalize the goal by proposing a \textbf{R}eal-world \textbf{D}ata-centric automatic \textbf{R}\&\textbf{D} \textbf{Bench}mark, namely $\text{RD}^2$Bench. $\text{RD}^2$Bench benchmarks all the operations in data-centric automatic R\&D (D-CARD) as a whole to navigate future work toward our goal directly. We focus on evaluating the interaction and synergistic effects of various model capabilities and aiding in selecting well-performing trustworthy models.
    Although $\text{RD}^2$Bench is very challenging to the state-of-the-art (SOTA) large language model (LLM) named GPT-4, indicating ample research opportunities and more research efforts, LLMs possess promising potential to bring more significant development to D-CARD: They are able to implement some simple methods without adopting any additional techniques. We appeal to future work to take developing techniques for tackling automatic R\&D into consideration, thus bringing the opportunities of the potential revolutionary upgrade to human productivity.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes a benchmark named RD2Bench for evaluating data-centric automatic Research & Development (R&D) using Large Language Models (LLMs). The benchmark aims to assess and improve the efficiency of the R&D process by evaluating a model’s ability to understand, extract, and implement methods described in raw research materials. The focus is on leveraging LLMs to perform data-centric R&D in a real-world context, with an emphasis on minimizing manual labor for researchers. The authors also present an evaluation of current state-of-the-art LLMs, like GPT-4, in different stages of data-centric R&D.

### Strengths
1. This paper propose an interesting task. The concept of automating the R&D process to minimize human intervention is innovative and highly valuable.
2. The proposed RD2Bench appears well-conceived, focusing not only on a model’s understanding ability but also on the complex interaction between multiple abilities, such as data extraction, method selection, and implementation.

### Weaknesses
This paper presents an interesting and novel task for large language models, contributing valuable insights to the field. However, despite its strengths, there are still some weaknesses that prevent me from assigning a higher score and lead me to believe that the work, in its current form, is not yet sufficiently developed or complete.
1. While the goal of RD2Bench is to evaluate models across a broad spectrum of R&D tasks, the current focus on only financial reports and stock trading data is a significant limitation. The models' performance on financial data may not be indicative of how well they would perform in fields with different data characteristics or domain-specific challenges. For instance, the structured nature of financial data, often presented in tables and reports, contrasts sharply with the unstructured text and complex relationships found in scientific research papers or medical records. This narrow domain focus limits the generalizability of the benchmark and raises questions about its applicability to other R&D areas.
2. The paper mentions that RD2Bench includes human-annotated ground-truth results, but it provides insufficient detail about the annotation guidelines and mechanisms used. Given that human annotation quality is vital for evaluating automated systems, a more comprehensive explanation of how annotation challenges were overcome would be valuable. For example, the paper does not specify the level of expertise required of the annotators, the inter-annotator agreement scores, or the process used to resolve disagreements. Without this information, the reliability and validity of the ground truth data are questionable.
3. The performance metrics reported in Tables 1, 2, and 4 show values that are frequently close to 0.9 or even nearly 1.0, which raises concerns about the benchmark's effectiveness in distinguishing the capabilities of different models. Such high scores across various models suggest that the benchmark may lack the complexity or sensitivity needed to reveal meaningful performance differences, potentially limiting its utility for assessing model strengths and weaknesses comprehensively. The lack of variability in the scores indicates that the benchmark may not be challenging enough to expose the nuances in model performance, making it difficult to identify which models are truly superior for the task.

### Questions
1. The paper evaluates the performance of GPT-4 and Llama but does not extend the analysis to other state-of-the-art models such as GPT-4o, Claude, or a broader selection of open-source alternatives. Including these models could provide a more comprehensive assessment of current capabilities in automatic R&D.
2. The study's focus on financial domain data raises concerns about the generalizability of the benchmark. Without empirical evaluation across diverse domains, it remains unclear whether the models would exhibit comparable performance in other research areas, which limits the applicability of the findings.

### Soundness
2

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
This paper introduces RD2Bench, a benchmark designed to evaluate and advance data-driven automated R&D processes. RD2Bench assesses large language models on their performance in automated R&D tasks, focusing on two core abilities: (1) language understanding to accurately extract implementable methods from research materials, and (2) technical implementation skills to develop reliable and trustworthy solutions. Unlike existing benchmarks, RD2Bench evaluates not just individual capabilities but also the synergistic effects of multiple abilities in real-world R&D tasks. The contributions of the paper include providing a structured framework to assess model performance in automated R&D workflows and establishing metrics to measure task success, accuracy, and stability. Experimental results reveal the potential of advanced models like GPT-4 in these tasks, while also identifying areas needing further improvement to achieve full automation in scientific and data-driven fields.

### Strengths
1. Innovative and Practical Benchmark: RD2Bench introduces a unique data-centric benchmark specifically designed for automating R&D tasks, moving beyond traditional evaluations by assessing multiple model capabilities in real-world applications.

2. Focus on Synergistic Model Abilities: Unlike other benchmarks that assess isolated abilities, RD2Bench emphasizes the interaction and synergy between language understanding and technical implementation, providing a comprehensive evaluation framework for large language models.

3. Detailed and Insightful Experimental Findings: The paper provides experimental results that reveal specific strengths and weaknesses of state-of-the-art models like GPT-4, offering actionable insights for future research on improving automated R&D capabilities.

4. Robust Metric Design: The benchmark incorporates multiple detailed metrics, such as running success rate, format success rate, correlation, and accuracy, allowing nuanced assessments of model performance across diverse R&D tasks.

5. Structured Literature Review: The paper contextualizes its contributions within existing research on language models and automated R&D, effectively highlighting gaps and motivating the need for a new benchmark like RD2Bench.

6. Practical Applications for Productivity Enhancement: RD2Bench has clear practical implications, as it is designed to improve the efficiency and productivity of scientific research processes, making it highly relevant for both academic and industrial applications.

### Weaknesses
1. Lack of Analysis on Model Error Sources: While performance metrics like accuracy and correlation are well-covered, the paper could strengthen its impact by analyzing common sources of model errors, such as misunderstanding prompts or misinterpreting data. A deeper error analysis could highlight specific improvement areas in LLMs for R&D.

2. Limited Detail on Human Annotation Quality Control: Although human annotation plays a significant role in RD2Bench, the paper could provide more information on quality control mechanisms for annotators beyond training and double-checking. Expanding on inter-annotator agreement or including validation checks would reinforce the reliability of the benchmark.

3.Insufficient Discussion on Computational Efficiency: RD2Bench implies the need for repeated trials and extensive processing, especially for large models. An analysis of the benchmark’s computational requirements and possible optimizations could make it more practical for widespread research use, especially in settings with limited resources.

### Questions
1. How do the authors envision RD2Bench being adapted or extended for domain-specific applications, such as finance or biotech, where specialized knowledge is often critical? Are there plans to incorporate domain-specific adaptations in future work?

2. Could the authors elaborate on the complexity of the R&D tasks included in RD2Bench? Introducing more advanced, iterative R&D tasks could better reflect real-world challenges. Would the authors consider integrating more complex task workflows?

3. What are the most common sources of errors encountered in the benchmark tasks, and how could they inform improvements for language models? An in-depth error analysis might reveal valuable insights into model limitations and areas for enhancement.

4. The paper mentions quality control for human annotations but provides limited details. Could the authors clarify the mechanisms used to ensure annotation consistency, such as inter-annotator agreement metrics or other quality checks?

5. Given the computational demands of RD2Bench, have the authors considered optimizations to reduce resource requirements? An analysis of potential optimizations would be beneficial for research environments with constrained computational resources.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a benchmark called "RD2Bench" designed to evaluate the process of Data-Centric Automatic R&D (D-CARD). RD2Bench focuses on the interaction and synergy between the abilities of large language models (LLMs) in areas such as language understanding, code implementation, and data selection during the R&D process. The benchmark simulates real-world data-centric R&D scenarios to study the performance and challenges of these models in handling automated R&D tasks. Experimental results indicate that while current state-of-the-art LLMs perform well on some simple R&D tasks, more complex tasks still pose significant challenges.

### Strengths
1. The paper is the first to formalize the task of automating research and development (R&D), which is an important and impactful endeavor.
2. The motivation of the paper is well-grounded and clearly articulated.

### Weaknesses
1. The dataset size and scope are quite limited, containing only 27 formulas and 6 models. The formulas are solely from the financial domain, and the models are only graph neural networks, representing a very small part of "Data-Centric Research and Development.
2. The authors claim RD2Bench evaluates the interaction and synergy of various model capabilities, but the results only assess "information extraction" and "method implementation" separately. Existing benchmarks, like [1], already combine these capabilities, and RD2Bench's unique contribution in this regard is not clearly demonstrated.
3. The evaluation metrics, task descriptions, and several experimental details remain unclear, particularly with the absence of Appendix A.

[1] Mialon, G., Fourrier, C., Swift, C., Wolf, T., LeCun, Y., & Scialom, T. (2023). Gaia: a benchmark for general ai assistants. arXiv preprint arXiv:2311.12983.

### Questions
1.	Is there a more detailed explanation of the task difficulty levels?
2.	Regarding method extraction in Section 3.3: Figures 1 and 2 only show the formula extraction results. Are the model extraction results also in a key-value format? What exactly do the evaluation metrics measure? Is it the matching degree between expected keys and extracted keys?
3.	In the Implementation Step, are the method extraction ground truths used as inputs, or are the actual extracted results (even if potentially incorrect) used as inputs?

### Soundness
2

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
3

### Summary
This paper introduces RD2Bench, a benchmark designed to enhance real-world data-centric automatic R&D (D-CARD) by evaluating the synergistic effects of various model capabilities. The authors aim to improve research efficiency and foster the automation of data-centric R&D processes. The study highlights the strengths of state-of-the-art models like GPT-4 while identifying areas for further improvement.

### Strengths
1. Innovative approach to automating data-centric R&D with a comprehensive benchmark.
2. Thorough methodology encompassing data collection, human annotation, and robust evaluation metrics.
3. Insightful experimental results demonstrating the capabilities and limitations of current models.

### Weaknesses
1. Data is limited to the financial domain; a broader variety of datasets would enhance the benchmark's applicability.
2. The paper would benefit from providing related implementation codes and datasets to facilitate reproducibility.
3. There is a lack of comparison with model combinations, which could provide insights into potential performance improvements.
4. Insufficient discussion on the limitations and potential biases in the data collection process.
5. Need for more clarity on how the benchmark could be adapted for various domains beyond the current focus.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
3
