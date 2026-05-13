# K-HALU: Multiple Answer Korean Hallucination Benchmark for Large Language Models

- Decision: Accept
- Scores: 6, 6, 8

## Abstract
Recent researchers and companies have been developing large language models (LLMs) specifically designed for particular purposes and have achieved significant advancements in various natural language processing tasks. However, LLMs are still prone to generating hallucinations—results that are unfaithful or inconsistent with the given input. As a result, the need for datasets to evaluate and demonstrate the hallucination detection capabilities of LLMs is increasingly recognized. Nonetheless, the Korean NLP community lacks publicly available benchmark datasets demonstrating the faithfulness of knowledge-based information. Furthermore, the few existing datasets that evaluate hallucination are limited in their access to the entire dataset, restricting detailed analysis beyond simple scoring, and are based on translated English knowledge. To address these challenges, we introduce K-HALU, a Korean benchmark designed to evaluate LLMs' hallucination detection in Korean. This benchmark contains seven domains, considering the faithfulness of statements based on knowledge documents compiled from Korean news, magazines, and books. For more strict evaluation, 40% of the dataset is structured as multiple-answer questions, requiring models to select all possible correct answers from the given options. Our empirical results show that open-source LLMs still struggle with hallucination detection in Korean knowledge, emphasizing the need for a more detailed analysis of their limitations. The K-HALU benchmark will be made publicly available after the anonymous review period.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work introduced a Korean benchmark namely K-HALU designed to evaluate LLM's hallucination detection in Korean. Specifically, K-HALU consists of more than 2,000 challenging test samples from Korean news, magazines and books, covering seven domains. The evaluated LLMs involve open-source models: Llama 2, Llama3, Mistral and Korean models such as KULLM3 and ExaOne, and API models: GPT-3.5 and GPT-4 series. Results show that the open-source LLMs exhibit low accuracy less than 35% and 15% on harder tasks, compared with the API LLMs show better accuracy by 27%.

### Strengths
1. This paper introduces a Korean benchmark to evaluate LLM's ability for hallucination detection. The benchmark consists of more than 2,000 examples and is labeled by both human annotators and top-performing models.

2. The writing is clear and easy to follow.

3. The analyses are extensive for different LLMs and different scenarios such as domain, instruction type and few-shot.

### Weaknesses
1. The comparisons and discussion with the English are missing. Given the fact that there exist benchmarks for hallucination detection in English, the difficulty of Korean hallucination detection by LLMs and the corresponding novelty is unclear to me. This will hurt the contribution of this work. 

2. The evaluation measure is a bit simple to some extent. The measurement used in the benchmark is selecting the hallucinated statements from the given statements. However, it is more useful for LLMs to directly give judgments or reasons on whether an input has a hallucination. The problem setting in such two cases is different in the existence of reference selections. 

3. The metrics on how different human annotators consensus with each other is unclear. Besides, the linguistic background of human experts can be essential to the correctness of data labeling. 

4. (Minor) I notice from Table 7 that The CoT approach can hardly improve the accuracy, it is peculiar from the literature of CoT. More discussion on this can be helpful. 

5. (Minor) The question in the benchmark can have multiple selections, thus other measurements such as precision, recall or F1 can be more comprehensive to evaluate hallucination detection than accuracy.

### Questions
I hope the authors can clarify my concerns about the above weakness. But if I missed some important thing, please correct me in the rebuttal.

### Soundness
2

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
This paper presents a benchmark for evaluating the performance of LLMs on determining whether a statement (short sentence) written in Korean is hallucination or not with respect to a given document also written in Korean and its publication date. Concretely, there is a set of statements for each document and the LLM is tasked to either pinpoint all hallucination ones or all correct ones (i.e., two types of multiple-choice questions). The motivation to create this benchmark is due to the lack of evaluation resources in Korean. The benchmark creation pipeline is described together with its statistics. The performance of several open- and closed-source, multi-lingual and Korean-tuned, LLMs is evaluated.

First, the authors should revise the terminology (i.e., hallucination, factual, faithful) which seems confusing as used in the paper. As the benchmark and task is stated, it seems that the actual task is to distinguish between faithful (i.e., supported by the input document) or unfaithful (not supported by the input document) statements. A statement can be not supported by the given document but still be factual (see definition in Maynez et al. 2020).

Second, it is not clear why the format of the benchmark is multiple-choice and why the strict evaluation on sets of statements (select n hallucination/non-hallucination statements from given N). It is not clear why this task setup, it seems adding extra complexity that is not needed to see whether an LLM can distinguish whether a statement is faithful (or not). Cannot it just evaluate the LLM on each individual statements?
 
As for the LLM execution of the task, why the selection between hallucination or not is based on probabilities? Why not prompting the model to generate/select the options (i.e., to generate "1, 2")? The authors should explain why they chose this method and may be also add results with the prompt approach. Previous evaluation methods based on prompt ask the model to choose among plausible responses. Also, how was this probability approach implemented for closed-source LLMs (i.e., GPT variants)?

More details about the Chain-of-Thought implementation should be provided. The prompts and partition into reasoning sub-steps?

The authors should avoid using the term "uncertain" throughout the paper. It is confusing and under-specified, do the authors mean that the statement is not supported by the document? Then should be said 'unsupported'.

Related work should discuss other work on creating evaluation resources for less represented languages. eg., [1].
[1] https://arxiv.org/abs/2403.20266

Section qualitative analysis, Appendix A and Figure 4 should go into the main paper.

Minor comments:

- the source dataset should be better described (Knowledge Graph-to-Text dataset from AI-Hub) what is this graph?
- Lens Observation section. At this point in the paper, it is not clear what the used frameworks are nor why suddenly we are looking at these frameworks.
- Line 360, "handling hallucinations" should be called "detecting hallucinations" as the task is to detect whether the sentence is hallucination or not rather than doing something to mitigate hallucinations.

### Strengths
- The collected evaluation suit from Korean sources is valuable for the evaluation of Korean language models.
- Experiments show that LLMs struggle to reason about content in Korean (though see comments above about the experimental setup).

### Weaknesses
First, the authors should revise the terminology (i.e., hallucination, factual, faithful) which seems confusing as used in the paper. As the benchmark and task is stated, it seems that the actual task is to distinguish between faithful (i.e., supported by the input document) or unfaithful (not supported by the input document) statements. A statement can be not supported by the given document but still be factual (see definition in Maynez et al. 2020).

Second, it is not clear why the format of the benchmark is multiple-choice and why the strict evaluation on sets of statements (select n hallucination/non-hallucination statements from given N). It is not clear why this task setup, it seems adding extra complexity that is not needed to see whether an LLM can distinguish whether a statement is faithful (or not). Cannot it just evaluate the LLM on each individual statements?
 
As for the LLM execution of the task, why the selection between hallucination or not is based on probabilities? Why not prompting the model to generate/select the options (i.e., to generate "1, 2")? The authors should explain why they chose this method and may be also add results with the prompt approach. Previous evaluation methods based on prompt ask the model to choose among plausible responses. Also, how was this probability approach implemented for closed-source LLMs (i.e., GPT variants)?

More details about the Chain-of-Thought implementation should be provided. The prompts and partition into reasoning sub-steps?

The authors should avoid using the term "uncertain" throughout the paper. It is confusing and under-specified, do the authors mean that the statement is not supported by the document? Then should be said 'unsupported'.

Related work should discuss other work on creating evaluation resources for less represented languages. eg., [1].

Section qualitative analysis, Appendix A and Figure 4 should go into the main paper.

Minor comments:

- the source dataset should be better described (Knowledge Graph-to-Text dataset from AI-Hub) what is this graph?
- Lens Observation section. At this point in the paper, it is not clear what the used frameworks are nor why suddenly we are looking at these frameworks.
- Line 360, "handling hallucinations" should be called "detecting hallucinations" as the task is to detect whether the sentence is hallucination or not rather than doing something to mitigate hallucinations.

### Questions
- why the format of the benchmark?
- why only the implementation using probabilities?

### Soundness
2

### Presentation
2

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
This paper introduces K-HALU, a multiple-answer Korean hallucination benchmark for evaluating LLMs on their ability to detect factual inaccuracies or hallucinations within Korean-specific contexts. Unlike previous Korean benchmarks, which often rely on translations of English datasets or offer limited dataset access, K-HALU provides a culturally and linguistically relevant resource. It consists of 2,170 test samples. By requiring models to select all possible correct answers in a multiple-choice format, K-HALU presents a stricter evaluation standard than traditional benchmarks, especially for open-source models, which often struggle with hallucination detection.

### Strengths
The main strength of this paper lies in the originality and cultural relevance of K-HALU, as it fills a significant gap in the Korean NLP community by using carefully selected and annotated content rather than translations from existing benchmarks. K-HALU’s focus on Korean linguistic and socio-cultural contexts ensures that factuality assessments and hallucination detection are appropriately designed, making it particularly valuable for future NLP research in non-English settings. The multiple-answer format provides a more rigorous evaluation by requiring the selection of all correct answers, offering a strict measure of model robustness and enhancing the benchmark's reliability in assessing hallucination vulnerabilities in real-world applications. Additionally, figures in the paper reveal that open-source models still struggle with hallucinations in Korean, highlighting opportunities for further development and application in multilingual hallucination research.

### Weaknesses
A weakness of the paper is the lack of clarity regarding the human-annotated statements. The paper does not provide details about the annotators' backgrounds, such as their expertise in relevant domains (e.g., whether they hold advanced degrees or come from diverse educational backgrounds). This information is critical for understanding the quality and reliability of the annotations, especially in fields that require specialised knowledge. Secondly, the evaluation section appears unclear and lacks specificity. It is unclear whether exact match is used as the primary metric for assessing correctness in multiple-answer questions or if external models are used in evaluation.  A more detailed breakdown of the evaluation methods would improve clarity and provide stronger support for the paper’s conclusions.

### Questions
1. For common benchmarks like MMLU, the majority of samples can be sourced online to verify the correctness of extractions. Can K-HALU samples similarly be sourced online for users to verify correctness?

2. In evaluating multiple-choice answers (as mentioned in the weaknesses section), is exact match used as the criterion for correctness, or are alternative evaluation methods applied?

3. What would the model accuracy be if strict exact match criteria were applied, where an incorrect answer is not picked and the entire question being marked as incorrect? A breakdown of accuracy under these conditions for each model would provide valuable insights into model performance.

4. What would the feasibility of extending K-HALU to other non-English or low-resource languages be? Is the framework adaptable beyond Korean, or are there limitations specific to the Korean language context?

### Soundness
4

### Presentation
4

### Contribution
3
