# Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 6, 5

## Abstract
Exceptional mathematical reasoning ability is one of the key features that demonstrate the power of large language models (LLMs). How to comprehensively define and evaluate the mathematical abilities of LLMs, and even reflect the user experience in real-world scenarios, has emerged as a critical issue. Current benchmarks predominantly concentrate on problem-solving capabilities, presenting a substantial risk of model overfitting and fails to accurately measure the genuine mathematical reasoning abilities. In this paper, we argue that if a model really understands a problem, it should be robustly and readily applied across a diverse array of tasks.
To this end, we introduce \textbf{\textsc{MathCheck}}, a well-designed checklist for testing task generalization and reasoning robustness, as well as an automatic tool to generate checklists efficiently. \textsc{MathCheck} includes multiple mathematical reasoning tasks and robustness tests to facilitate a comprehensive evaluation of both mathematical reasoning ability and behavior testing. Utilizing \textsc{MathCheck}, we develop \textbf{\textsc{MathCheck-GSM}} and \textbf{\textsc{MathCheck-GEO}} to assess mathematical textual reasoning and multi-modal reasoning capabilities, respectively, serving as upgraded versions of benchmarks including GSM8k, GeoQA, UniGeo, and Geometry3K.
We adopt \textsc{MathCheck-GSM} and \textsc{MathCheck-GEO} to evaluate over 26 LLMs and 17 multi-modal LLMs, assessing their comprehensive mathematical reasoning abilities. 
  Our results demonstrate that while frontier LLMs like GPT-4o continue to excel in various abilities on the checklist, many other model families exhibit a significant decline.
  Further experiments indicate that, compared to traditional math benchmarks, \textsc{MathCheck} better reflects true mathematical abilities and represents mathematical intelligence more linearly, thereby supporting our design. Using \textsc{MathCheck}, we can also efficiently conduct informative behavior analysis to deeply investigate models. Finally, we show that our proposed checklist paradigm can easily extend to other reasoning tasks for their comprehensive evaluation.\footnote{Data and code can be found here: \url{https://mathcheck.io/}}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents MathCheck, a benchmark/checklist for testing (M)LLMs' task generalization and reasoning robustness in mathematical problems. It utilizes GSM8k and GeoQA to create new math problems that are of different styles (e.g., irrelevant disturbance) and different types (e.g., process judging). By evaluating 26 LLMs and 17 MLLMs on this benchmark, the authors find that some models show generally robust performance (e.g., strong close models like GPT-4o), while other models (e.g., Qwen1.5-72B-Chat) show performance drop in alternative problem settings (e.g., OJ and ID). Overall for MLLMs there is large room for improvement on the multi-modal subset (GEO) of the benchmark. They include several analyses to support the reliability of the benchmark and show how the main ideas in the paper can be applied to other evaluation domains such as commonsense reasoning.

### Strengths
- The paper is clearly written. The examples and figures are illustrative. For example, I can easily understand what the benchmark is about by looking at Figure 1. The sections are structured well.

- The task setup is innovative (i.e., the 4 x 4 matrix). It is valuable to have these different styles and formats of problems in one place for evaluation and comparison. The argument that the 4 x 4 setup is relevant to measuring generalization and robustness (at least to some degree) is sound.

- The benchmark has text only and multi-modal parts, which are of interest to multiple sub-communities in the field.

- The authors studied a comprehensive set of LLMs, covering models that are open and closed, big and small, generalist and specialized. And they studied several different prompting strategies, which we know matter for mathematical reasoning.

- The authors do a good job attempting to ensure data quality and establish benchmark reliability. For example, they show human pass rates w.r.t. LLM-based problem generation, and they show that the accuracy of MathCheck-GSM is highly correlated to that of GSM1k, a putative high-quality private dataset. 

- The authors not only discuss how the evaluation method introduced in this paper can be general (applied to other domains), but they also have already done work in that direction by creating variants of "data understanding" and code generation tasks. This would prompt other researchers to consider how this method may be relevant to their own domains of interest.

Overall, I believe that this paper and dataset are a valuable contribution to the AI for math research community.

### Weaknesses
 - One weakness of the benchmark is about the difficulty of the problems. MathCheck-GSM is based on GSM8k, which is a grade-school-level benchmark that the SoTA models perform very well on. And correspondingly they tend to perform well on MathCheck-GSM. It would have been a stronger benchmark if MathCheck also included high-school and beyond problems, so that we could have a better understanding of where and how models like GPT-4o and O1-preview fail. But this is not a major weakness and can be left for future work. MathCheck already has promise for measuring progress in smaller/weaker models and multi-modal models.

- A similar weakness to the above is about the diversity of problems. The seed data only contain two types of problems: simple word problems and geometry problems.

- The related work section needs to be improved/expanded. Only talking about other math benchmarks is not enough. I encourage the authors to add at least two paragraphs. One can be on what people have done to improve mathematical reasoning with LLMs (training, inference, prompting, LLMs + formal tools, etc.)—the broad landscape of AI for math. Another can be similarly spirited benchmarks in other domains. For example, the use of counterfactual tasks in [1] is also for evaluating how robust and general LLMs' problem understanding and reason abilities are.

### Questions
Who are the human annotators that evaluated the quality of GPT-4T rewriting? Are they (a subset of) the authors? (That is implied from C.3, but I think it should be explicitly stated.) How did one determine whether a problem "passed"? I just encourage the authors to add a few sentences to better clarify the human evaluation process.

### Soundness
3

### Presentation
4

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
This paper introduces MathCheck, a new mathematical reasoning benchmark for large language models (LLMs). It aims to address the limitations of existing benchmarks, which often focus on evaluating individual tasks rather than LLM models' understanding of the problems. MathCheck incorporates carefully augmented math problems in different dimensions, including generalization and reasoning robustness.

### Strengths
The paper provides a novel approach to evaluating math problems by considering whether the models understand the problems, not just solve them. The dimension of task generalization is innovative, offering various methods to judge problem answers and providing insights into evaluating reasoning ability. The linearity and performance on different complexity levels demonstrate the potential of the new benchmark for comprehensive evaluation of models' math reasoning abilities.

### Weaknesses
The data generation pipeline with an 86% pass rate, although good, doesn’t sound ideal given the scale of samples. The paper could benefit from briefly discussing in the main text when showing the pass rate how low-quality generated questions are handled when detected.

Nitpicks: Line 431: It would be helpful to include references to the alleged works. Line 463: quote left mark is incorrect.

### Questions
In Figure 6, could the accuracy drop be attributed to the increasing difficulty LLMs faced in generating or reconstructing task generation entries for more complex problems?

Appendix C2 presents pass rates for different rewriting types. Would it be practical to also show the pass rates for different complexity levels? (This may not be necessary if the such questions are omitted in evaluation.)

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
This paper introduces MATHCHECK, a new evaluation framework for assessing mathematical reasoning capabilities in LLMs. The framework's key innovation is its comprehensive evaluation approach that tests both task generalization and reasoning robustness. The authors develop two datasets using this framework: MATHCHECK-GSM for text based mathematical reasoning and MATHCHECK-GEO for multimodal geometric reasoning. They demonstrate that while some frontier models like GPT-4o maintain strong performance across their checklist, many other models show significant performance degradation compared to their standard problem solving abilties. The authors also provide evidence that MATHCHECK correlates better with true mathematical reasoning abilities compared to other benchmarks. Finally, the authors show that the current paradiem of finetuning models for math probalem solving capabilities leads to stagnation or even degredation in other areas of math reasoning.

### Strengths
In terms of originality and quality, it introduces a novel evaluation paradigm that goes beyond traditional problem-solving assessments to comprehensively evaluate mathematical reasoning through multiple tasks and robustness tests. While there have been some previous work on creating function variations, this paper goes beyond simply rewritting the question.
The methodology is rigorous, with extensive empirical validation involving 43 models and a careful data generation process that achieves an 84.61% pass rate with manual validation. The authors validate their framework's effectiveness through correlation with private data and compression efficiency metrics, imlying performance on this benchmark is more robustly capturing llm math abilities.
The paper is reasonably clear in its presentation, with well-structured explanations of the framework and comprehensive documentation of methodology.
The paper is moderately siginificant. The paper provides a more reliable way to evaluate true mathematical reasoning capabilities of LLMs and is exstensible to other domains as well. In particular, the ability to evauate llms on areas other than problem solving is very useful to MCTS and LLM-as-a-judge methods.

### Weaknesses
Would recommend citing 1+ papers on functional variations benchmarks which programatically generate question variations.

MATHCHECK-GSM seems to be saturated by frontier models, making it hard to get an accurate measure of their relative abilities. Constructing a MATHCHECK benchmark from MATH or another harder benchmark would be ideal.

In Appendix C, it is unclear what is meant by "data statistic". I assume in tables 3 and 4 it is the total count of questions for that variation type, but I'm not sure what table 5 is trying to show.

Recommended:
- Evaluate models on MATHCHECK adapted to other reasoning tasks (i.e. commonsense reasonin and code)

Minor:
- Use (M)LLM and MLLM inconsistently/unclear what the term means
- It would be nice to have tables 1 and 2 in a plot somehow so we can better see how performance compared across evaluation categories.
- The text in Figure 5 is a bit small and in general hard to interpret
   - I would recommend using a bar chart or similar where it is easier to see the performance deltas (this might require aggregating over the rows)
- Figure 6 should have an x-axis label
- In figure 7, the pink and red are hard to differenciate (perhaps remove the color fills and only include the outlines)

### Questions
- What is the pass rate for GPT-4o rewritting for the MATHCHECK-GEO benchmark?
- The data generation pipeline has a pass rate of ~85%. It is not explicit in the paper whether the released banchmark has filtered out the questions that don't pass or left them in.

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
This paper explores the question that how to comprehensively evaluate LLMs’ mathematical abilities. Considering that if a model understands a problem, it should be applied across different tasks and problem varieties, they introduce MATHCHECK. MATHCHECK is a checklist for testing task generalization and reasoning robustness. For textual and multimodal language models, they develop MATHCHECK-GSM and MATHCHECK-GEO separately utilizing MATHCHECK.

### Strengths
1.	The paper studies an important research question from a fresh perspective, evaluating the models’ reasoning abilities across various tasks and problem varieties.
2.	Abundant experiments: A total of 43 models are evaluated on the proposed benchmarks, which serve as comprehensive baselines for further studies.
3.	The paper is well-written and easy to follow.

### Weaknesses
1.	Although the paper attempts to analyze the mathematical reasoning capabilities of existing models from multiple aspects (including PS: Problem Solving, AJ: Answerable Judging, OJ: Outcome Judging, PJ: Process Judging, OP: Original Problem, PU: Problem Understanding, ID: Irrelevant Disturbance, SU: Scenario Understanding), there are the following shortcomings. On one hand, some models (such as O1-preview) have already achieved very good performance (>90%) on these datasets and have shown extremely strong robustness, indicating that the evaluation methods proposed in the paper may not be challenging enough for the most advanced models currently available. Moreover, the reviewer did not find any new insights proposed by the evaluation method for the improvement of existing models. On the other hand, the goal of the paper is to explore whether models truly possess mathematical reasoning abilities, and the multiple aspects proposed seem insufficient: if one model performs well in all the proposed aspects, does it truly have reasoning abilities?
2.	Given that these benchmarks are generated by LLMs and only verified by humans, how to ensure the diversity across different question groups? For example, with different seed questions, LLMs may tend to include similar irrelevant information when generating the “irrelevant disturbance” variety, leading to a less comprehensive evaluation.

### Questions
1.	A seed problem is expanded to include 4 math tasks and 4 problem varieties (as shown in Fig.1), resulting in a total of 4\*4=16 problems. Therefore, for the 129 style groups in MATHCHECK-GSM, the total number of samples should be 129\*16=2064. However, in Sec. 3.1, the number of samples in MATHCHECK-GSM is reported as 3096. Could you clarify this discrepancy?

### Soundness
3

### Presentation
4

### Contribution
2
