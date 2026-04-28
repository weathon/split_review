# LLM Spark: Critical Thinking Evaluation of Large Language Models

- Decision: Reject
- Avg Score: 5.25
- Scores: 3, 5, 8, 5

## Abstract
Large language models (LLMs) excel in complex tasks but often struggle with
inconsistencies in problem framing, a critical skill for real-world scenarios. This
paper introduces SPARK, a novel evaluation framework grounded in the Hierar-
chical Three-Space Theory, to assess LLMs’ ability to identify missing informa-
tion and challenge flawed problem setups. We propose a general framework to
create benchmarks by introducing inconsistencies and misleading cues in diverse
question-answering datasets, covering mathematics, science, and reading compre-
hension. To assist with robust measuring of critical thinking, we employ two key
metrics: problem-solving capability rate and challenge rate. Our experiments with
state-of-the-art LLMs reveal their limitations in critical thinking, particularly in
recognizing inconsistencies. We also explore mitigation strategies, such as modi-
fied prompting and targeted fine-tuning. Furthermore, we conduct comprehensive
experiments to investigate how model and problem properties influence critical
thinking capabilities in LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces SPARK, a framework intended to assess the capability of LLMs to identify inconsistencies in problem framings using modified existing datasets. The authors come up with two metrics "Correctness" and "Challenge Rate" for the evaluation. They use the idea of Three-space theory from the cognitive science to come up with this framework. The dataset consists of different domains  such as math, science, comprehension etc. They also introduce perturbation's to the data to see the changes in the output given by the LLM and evaluate those responses and try to analyze the behavior of LLMs. While the work is interesting but there are many issue with this, right from writing to selection of data and evaluation metrics.

### Strengths
The work uses inspiration from cognitive science to come up with framework 

They address an important aspect of LLMs which is critical thinking

Multiple models are considered for the work and comparison 

Multiple hypothesis are tested in this work.

### Weaknesses
-> First most of the figures are poorly inserted, there could have been other type of figures chosen as most of the figures have the data overlapping and it's hard to interpret them.

-> The writing is poor, there is too many things and little details

-> While the related work is good there are many more work that are missing one of them is "Tree of Thoughts" 

-> The datasets chosen for this work are diverse and contains many existing datasets, there is no mention of testing of data contamination given the models that are considered for this work have this data in their training data, also the dataset could have been better, I feel there are better datasets like Game24, or the one's mentioned in the related work are more relevant to this work.

-> It is mentioned that you create benchmarks in the abstract, I didn't clearly understand exactly what that meant.

-> A framework paper should be more detailed such that others can reproduce and compare their work to this, need more quantitative results.

-> Also there could have been more evaluations metrics rather than having just two of them and using them to test variety of hypothesis, this decreases the robustness of the results.

-> Most of the figures in the appendix were hard to interpret, more details on them is appreciated.

### Questions
None

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
This paper introduces a novel approach to evaluating LLMs' critical thinking in identifying flaws in problem formulation. Grounded in Three-Space Theory, the authors reformulate existing datasets as critical thinking evaluation ones by removing correct answer choices (for multiple-choice QA datasets) or removing necessary conditions (for free-form generation datasets). They assess the "challenge rate"—the frequency with which LLMs, prompted to detect flaws, correctly identify issues, using GPT-4 for automatic YES/NO judgments. To further evaluate the model's robustness to misleading information in the problem formulation, the authors also augment QA datasets with hints ("gaslighting") on correct/incorrect answers or both. 

Experiment results demonstrate that while some larger LLMs can achieve non-trivial challenge rates ($>50\\%$) on free-form generation tasks only, there remains substantial room for improvement. Notably, the challenge rate does not correlate with model accuracy, and chain-of-thought prompting yields inconsistent effects on both metrics across models and datasets. Although gaslighting increases challenge rates across models, it also reduces accuracy, highlighting LLMs' susceptibility to manipulation.

### Strengths
1. This paper investigates an interesting evaluation dimension on whether LLM can critique flaws in the prompted problem formulation, complementary to widely-used instruction-following and LLM reasoning benchmarks. 

2. The experiment results can support the major claims of the paper.

### Weaknesses
1. **Limited Insight into Findings.** As this is an evaluation-focused paper, deeper analysis and implications of the results are the most important contributions. Many findings are presented as direct observations, often summarized by broad statements like "experiment results are influenced by dataset properties, models, training ...", "[prompting methods]  achieves mixed results", or "[model names] are vulnerable to manipulation in prompts". While these findings may hold, they resemble insights from prior work (Section 2) and align with expectations under a well-constructed evaluation framework. Although the paper emphasizes a unique "critical thinking" evaluation, it’s unclear what additional insights this approach offers beyond previous evaluation works.

2. **Clarity and Rigor in Experiment Design.** This paper reformulates existing datasets to build a new benchmark that focuses on evaluating LLM critical thinking, but several important experiment details are missing, or not rigorous enough. For example, the implementation of "Missing Information" for non-Quail datasets is not clearly defined, and criteria for identifying and removing "necessary conditions" (to make questions unanswerable) are unspecified. 
The validity of the "LLM-as-judge" approach in this new critical thinking evaluation benchmark is not clearly explained, nor are the "held-out datasets" used in evaluations. 

    Additionally, the exclusive use of instruct-tuned models raises questions about claims regarding instruction training effects (e.g., Line 272), as non-instruct-tuned models are not assessed.  Including control prompts where no flaws should be detected is also important to investigate potential false positive problems and prevent simple flaw-reporting models from skewing the results. Also, it seems a random baseline (possibly achieving 50% challenge rates) can beat most models in identifying problem formulation flaws, but there is no related explanation and analysis. Further problems are listed in the "Questions" section. 

3. **Readability and Conciseness of Main Text.** Introducing the new "SPARK" framework and articulating hypotheses is understandably challenging. However, the overall paper organization, especially in Sections 3 and 4, could be improved for readability. The flow from Section 3.1 to Section 3.2 feels disjointed, and hypotheses are discussed in fragments across sections, which complicates their verification for readers. While the reviewer appreciates the efforts of putting an experiment summary in Section 3.4, it lacks grounding in detailed results, making the introduction feel verbose. Tightening the organization and streamlining explanations would improve the paper's clarity and coherence.

### Questions
Major problems are written in Weakness #2, and here are some less severe questions that need clarification or presentation advice:

1.  Why choose this particular set of questions? Why there is a focus on reasoning-focused datasets? 

2. What are the decoding parameters for most models used in the experiments? Some datasets and models are sensitive to these hyperparameter decisions, so it should be clarified in the paper. There is no need to seek for best hyperparameter combinations, but for reproduction purposes, it is needed to know these experiment details. 

3. How are checkpoints compared in Section 4.7 different? More importantly, what are they, and how they are related to the analysis in the main text?

4. Presentation Advice: The fonts and colors in many figures are hard to read or interpret, and some figures contain confusing legends and annotations (e.g., Figure 10).

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Based on the three-space theory, this paper presents the SPARK hypothesis and assessment framework on LLM critical thinking. Through the benchmark constructed in the paper, the authors explored the current critical thinking ability of LLM, with the influence of various factors on it, through a large number of experiments, contributing to the assessment and enhancement of LLM's critical thinking.

### Strengths
Focusing on LLM's critical thinking skills, this paper frames the Benchmark by designing inconsistencies in the problem and designing a large number of experiments to explore it. 

I personally like the idea of this work. In my opinion, the main strengths of this work include: 
1) This paper uses the three-space theory to model LLM's critical thinking ability and explores the reverse proof of the framework, which provides a theoretical basis for critical thinking related research.
2) This paper conducts a large number of experiments to explore LLM's critical thinking and its influencing factors from multiple perspectives, which provides a feasible direction for the subsequent research.

### Weaknesses
I do not find significant shortcomings of this work, but only a few minor points to be clarified:
1. The critical thinking assessment was designed without taking into account the impact of the model's capabilities. For example, if the model itself cannot understand or does not have knowledge of the question, it is difficult to "criticize" it. This is especially true for multiple-choice questions and smaller models, as shown in Figure 2, where multiple-choice questions have a low percentage of correct answers and most models have a low change rate. This may result in an underestimation of their critical thinking, i.e., it is not that they do not have the ability to think this way, but that the questions are beyond their knowledge and ability.
2. In terms of assessment metrics, it is best to minimize the use of LLM assessments, which can be costly. For example, for multiple-choice questions, can there be a simpler way of assessing correctness rate, making the benchmark easier to use?
3. Correctness rate is sometimes used in complete problems [line 278] and sometimes in incomplete problems, and is also expressed as "none of the options" in its definition (incomplete problem), which can be confusing when reading the experiments and results.
4. Why does the gaslight increase its challenge rate while decreasing its correctness rate? If it affects the correctness rate, i.e., LLM is misled by gaslight, shouldn't the reasoning not be challenged but follow the misguidance?
5. Some of the dots and text in Figures 2, 11, and 12 overlap, which is hard to read.

### Questions
See weaknesses.

P.S., I'm really curious how o1 would respond to such problems.

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
3

### Summary
This paper introduces SPARK, a framework for evaluating Large Language Models' (LLMs) critical thinking abilities, specifically their capacity to identify inconsistencies in problem framing. The framework is grounded in the Hierarchical Three-Space Theory and evaluates LLMs across multiple dimensions (problem framing space, strategy space and implementation space) through five key hypotheses proposed by the authors. The authors create benchmarks by modifying existing datasets like commonsense QA, math and science datasets to introduce inconsistencies (e.g. missing options or missing conditions in the questions). Multiple LLMs are tested, and the experimental results show their limitations in critical thinking abilities.

### Strengths
- The framework is grounded in a cognitive theory (the Hierarchical Three-Space Theory)
- Extensive experimental results covering multiple domains and tasks, demonstrate the limitations of current LLMs in identifying inherent inconsistencies in provided problems.

### Weaknesses
 - The findings that LLMs lack of ability to identify flaws and often agree with the hallucinations in the given queries are not surprising.
- It is unclear whether the modified question can truly capture the problem inconsistencies in the real world. It would be helpful to add a human baseline to see if this task is solvable and aligned.

### Questions
- How are the correctness rate and challenge rate calculated? Can a model that always rejects to answer questions obtain the highest challenge rate?

### Soundness
2

### Presentation
3

### Contribution
2
