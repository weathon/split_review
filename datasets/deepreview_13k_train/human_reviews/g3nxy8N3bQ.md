# STEER-ME: Assessing the Microeconomic Reasoning of Large Language Models

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
Large language models (LLMs) are increasingly being applied to economic tasks like stock picking and financial analysis. Existing LLM benchmarks tend to focus on specific applications and often fail to describe a rich variety of economic tasks. Raman et al. (2024) offer a blueprint for comprehensively benchmarking strategic decision-making. However, their work failed to address the non-strategic settings prevalent in micro-economics. We address this gap by taxonomizing micro-economic reasoning into $58$ distinct elements, each grounded in up to $10$ distinct domains, $5$ perspectives, and $3$ types. The generation of benchmark data across this combinatorial space is powered by a novel LLM-assisted data generation protocol that we dub auto-STEER which generates a set of questions by adapting handwritten templates to target new domains and perspectives. By generating fresh questions for each element, auto-STEER  helps reduce the risk of data contamination, ensuring that \model evaluations remain valuable over time. We leveraged our benchmark to evaluate $15$ LLMs over each of the instantiated elements, examined their ability to reason through and solve microeconomic problems and compared LLM performance across a suite of adaptations and metrics. Our work provides insights into the current capabilities and limitations of LLMs in non-strategic economic decision-making and a tool for fine-tuning these models to improve performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a new benchmark specifically tailored to evaluate LLMs' performance in non-strategic microeconomic reasoning. This benchmark, STEER-ME, addresses limitations in existing economic benchmarks by categorizing microeconomic reasoning tasks into 57 distinct elements, covering various domains and perspectives. The authors also propose an LLM-assisted data generation protocol that dynamically generates questions to prevent data contamination. The study evaluates 15 LLMs across these elements to identify both strengths and limitations in their reasoning capabilities, providing insights into current LLM performance on fundamental economic tasks.

### Strengths
1. The paper offers a highly comprehensive benchmark, breaking down microeconomic reasoning into 57 distinct elements that span a wide range of domains and perspectives.
2. Significant resources and computational effort were invested in the study, with $5,896.33 spent on API requests to OpenAI and Anthropic, and 6.81 GPU years of compute used to evaluate open-source models.
3. All model outputs are made publicly available, promoting reproducibility and enabling further research and contributions to evaluation practices.
4. The study employs a wide range of evaluation metrics, including calibration-related metrics like Expected Calibration Error (ECE).
5. The paper highlights the critical issue of data contamination in LLM benchmarks

### Weaknesses
1. The primary contribution—expanding benchmarks to cover non-strategic microeconomic settings—leans more toward an economic contribution than a machine learning one, which may affect the paper's resonance with ICLR’s core audience.
2. The paper asserts that auto-STEER addresses data contamination but lacks empirical evidence or a detailed explanation of how it mitigates this problem effectively.
3. The benchmark is limited to multiple-choice questions, whereas real-world financial assistant LLMs are often required to handle open-ended generation tasks relevant to economic analysis. I would recommend expanding more experiments with more types of datasets, such as the free-text generation QA datasets.
4. The extensive number of elements and perspectives, while thorough, could complicate the task of providing a clear, overall model recommendation.
5. A substantial portion of the paper focuses on introducing economic rationality elements, which might not align well with the technical expectations of ICLR’s machine-learning audience. But overall, the idea is pretty interesting.

### Questions
Please refer to the weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a new benchmark specifically designed to evaluate large language models (LLMs) in non-strategic microeconomic tasks, addressing a gap in existing benchmarks that focus more on strategic decision-making. The authors create a taxonomy of 57 microeconomic reasoning elements across multiple domains, perspectives, and types, and introduce a data generation protocol called auto-STEER to produce fresh, contamination-resistant questions for each element. By evaluating 15 LLMs using this benchmark, the study reveals strengths and weaknesses in the models' ability to handle microeconomic concepts such as optimization and marginal analysis.

### Strengths
1. The creation of a taxonomy with 57 elements specifically for non-strategic economics provides a strong theoretical basis for the benchmark. This comprehensive taxonomy ensures that the benchmark is grounded in a thorough understanding of microeconomic reasoning, enabling a detailed and structured evaluation of LLMs in this domain.
2. The benchmark is solid, due to its broad variation in testing angles and use of multiple testing metrics.

### Weaknesses
1. The paper fails to discuss the correlation between the results of the proposed benchmark and those of related benchmarks, highlighting the significance of this research. Specifically, the absence of a comparative analysis with existing benchmarks leaves a gap in understanding the unique value proposition of this new benchmark. Without such a comparison, it's difficult to ascertain whether the benchmark offers novel insights or merely replicates existing findings. A discussion of how this benchmark differs from, and potentially complements, other benchmarks in the field is crucial for establishing its importance.
2. There are still some issues that need to be addressed in the writing of the paper, such as:
- The paper lacks hyperlinks for tables, figures, and sections, making it difficult for readers to locate referenced content.
- The title of Figure 2 contains misleading positional descriptors for the two images, referring to them as ‘on top’ and ‘on the right.’

### Questions
1. The analysis in the results section appears incomplete. Why is there only a separate section on "Domain Robustness" without any mention of "type robustness" or "perspective robustness"?
2. Although the paper generates a large number of questions for testing purposes, is this amount really necessary? For instance, the paper creates 100 templates by rephrasing, only modifying exact words or objects in the questions. Will these modifications lead to significant differences in results?

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
3

### Summary
This study fills a gap in the assessment of existing Large Language Models (LLMs) for non-strategic microeconomic reasoning tasks. To achieve this goal, the authors propose a new STEER-ME benchmark that categorizes microeconomic reasoning into 57 elements, generates a large number of multiple-choice questions and dynamically generates test data using the LLM-assisted data generation protocol (auto-STEER) to reduce the risk of data contamination. The experimental results show that the performance of different LLMs in the microeconomic reasoning task varies significantly, with even the larger models falling short; the only model that consistently performs well is o1-preview.

### Strengths
1. This work identifies a gap in the evaluation of current LLMs for non-strategic microeconomic reasoning tasks with high practical needs and research value.

2. A structured STEER-ME benchmark and a dynamic data generation protocol auto-STEER are proposed to ensure test diversity and data cleanliness.

3. The experiments cover a wide range of models and adaptation strategies, revealing differences in the performance of different LLMs in non-strategic microeconomic reasoning.

### Weaknesses
1. In the AUTO-STEER section, the authors may need to clarify which type of LLM was used for data generation. Additionally, it is important to discuss the impacts of the benchmark results by different LLMs for data generation.

2. The authors note that LLMs struggle with basic mathematical problems, like calculating the deadweight loss of a monopoly[Line 445-450], and suggests that this may be attributed to the use of incorrect formulas. To strengthen this claim, the authors should present specific evidence, such as analyses of error cases.

3. The authors need to provide more information on which open-source LLMs were tested (they did not list the LLMs), particularly whether they included models from the fields of mathematics and economics. It would also be important to discuss any differences in results between these specialized LLMs and general LLMs.

### Questions
1. It would be better to explore the effects of LLMs under in-context learning conditions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a novel benchmark, STEER-ME, to assess LLM's microeconomic reasoning in non-strategic settings. Using an LLM-assisted data generation method, Auto-STEER, the benchmark includes 57 distinct microeconomic elements across multiple domains and perspectives, minimizing data contamination. The authors evaluated 15 LLMs on these benchmarks, highlighting strengths and limitations in handling non-strategic economic decision-making.

contributions:
1. Novel benchmark development: The STEER-ME benchmark assesses LLM performance in non-strategic microeconomics, a domain not extensively covered by previous benchmarks that focused mainly on game theory or strategic decision-making.

2. Comprehensive taxonomy: The paper categorizes microeconomic reasoning into 57 elements, each tested across diverse contexts, such as finance and public policy, to evaluate broad economic reasoning capabilities.

### Strengths
1. proposed a benchmark on economics reasoning, which is relatively novel compared to classical benchmarks.

2. evaluated quite a few LLMs on the benchmark and have achieved some results.

### Weaknesses
Section 2: There are numerous economic concepts that may be challenging for machine learning researchers to follow, particularly the rationale behind constructing the taxonomy shown in Figure 1.

Section 3.1: Details about the dataset are lacking. Key statistics, such as the distribution of questions and question lengths, are not provided. Additionally, there is no discussion on how the dataset’s quality is ensured.

Section 5: The analysis of experimental results is limited. There is no case study or error analysis presented to offer deeper insights into model performance.

Code / Data:  i have not seen it uploaded.

### Questions
See weakness. In addition, i have questions below

1. Why is it necessary to develop these benchmarks for LLMs? Existing finance-related benchmarks, such as FinQA, FinEval, FinBench, FinanceBench, and FAMMA, already appear to cover similar topics to those in STEER. Additionally, general reasoning datasets in common scenarios may address some overlapping subjects.

2. What specific insights does this benchmark provide for LLM researchers?



--------------------------------------------------
I raise to 5 for the clarification about the motivation and dataset.

### Soundness
1

### Presentation
2

### Contribution
1
