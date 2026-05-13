# DynaMath: A Dynamic Visual Benchmark for Evaluating Mathematical Reasoning Robustness of Vision Language Models

- Decision: Accept
- Scores: 6, 6, 8, 8

## Abstract
The rapid advancements in Vision-Language Models (VLMs) have shown great potential in tackling mathematical reasoning tasks that involve visual context. 
Unlike humans who can reliably apply solution steps to similar problems with minor modifications, we found that state-of-the-art VLMs like GPT-4o can consistently fail in these scenarios, revealing limitations in their mathematical reasoning capabilities. 
In this paper, we investigate the \textbf{mathematical reasoning robustness} in VLMs and evaluate how well these models perform under different variants of the same question, such as changes in visual numerical values or function graphs.
While several vision-based math benchmarks have been developed to assess VLMs' problem-solving capabilities, these benchmarks contain only static sets of problems and cannot easily evaluate mathematical reasoning robustness.
To fill this gap, we introduce \textsc{DynaMath}, a dynamic visual math benchmark designed for in-depth assessment of VLMs. \textsc{DynaMath} includes 501 high-quality, multi-topic \emph{seed} questions, \emph{each represented as a Python program}. Those programs are carefully designed and annotated to enable the automatic generation of a much larger set of \emph{concrete} questions, including many different types of visual and textual variations. 
\textsc{DynaMath} allows us to evaluate the generalization ability of VLMs, by assessing their performance under varying input conditions of a seed question. We evaluated 14 state-of-the-art VLMs with 5,010 generated concrete questions (10 per seed question). Our results show that the worst-case model accuracy, defined as the percentage of correctly answered seed questions in all 10 variants, is significantly lower than the average-case accuracy.
In addition, many models show high consistency in answering these questions -- the incorrectness of a certain variant of a seed question is not due to inherent randomness. Our analysis emphasizes the need to study the robustness of VLMs' reasoning abilities, and \textsc{DynaMath} provides valuable insights to guide the development of more reliable models for mathematical reasoning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces DYNAMATH, a dynamic visual benchmark designed to evaluate the mathematical reasoning robustness of Vision-Language Models (VLMs). DYNAMATH contains 501 seed questions implemented as Python programs that can generate diverse variants by altering visual conditions while maintaining the same underlying mathematical concepts. The benchmark spans multiple mathematical topics and difficulty levels. The authors evaluated 14 state-of-the-art VLMs (both closed and open-source) and found significant gaps between average-case and worst-case performance, indicating limitations in VLMs' mathematical reasoning robustness.

### Strengths
1. The dynamic nature of the benchmark is innovative and addresses a critical gap in existing evaluation methods for VLMs' mathematical reasoning capabilities.
2. The evaluation is comprehensive. The author tests multiple aspects of mathematical reasoning across 9 different topics and they evaluate both closed and open-source models. The detailed performance includes various types of variations (numerical, geometric, functional, etc.).
3. The ablation analysis is strong: (a) detailed performance breakdown by topic and difficulty level;(b) Introduction of meaningful metrics (worst-case accuracy, reasoning robustness);(3)Thorough error analysis with clear categorization
4. The methodology is well-documented. The author provides a clear explanation of benchmark creation process.

### Weaknesses
1. The authors acknowledge that the difficulty level is relatively limited compared to some existing benchmarks like MATH-V. The requirement for programmatic generation may restrict the inclusion of more complex problems
2. The selection of seed questions and their variants might introduce unintended biases. The paper doesn't deeply discuss potential limitations in the variation generation process.
3. The human evaluation seems limited (only 10 participants). It is unclear if the human evaluators' backgrounds are representative, which may limit the validation of human performance.
4. Generalization of the conclusion on realistic questions. The questions (especially the vision content) are created by the program, which is quite different from the figures in the application (like the exam paper; hand-written question, or photo of the book). If the model fits well on these tasks, does it mean the model performs well on the realistic scenario?
5.Missing in-depth analysis of the performance gap between the worst-case and the standard accuracy. If we use a large amount of synthetic data in a similar manner, can the model work well also on these problems? If the performance gap can be resolved by introducing more synthetic data, the conclusion will be trivial and have no interesting news.

### Questions
In addition to the problems in weaknesses. There are some extra questions and suggestions.
1. Can we convert the existing problem into a dynamic/programmatic version?
2. Including analysis of the correlation between different types of variations and model performance will be better.
3. Investigate potential relationships between training data/training techniques and performance on different variation types if possible.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a dynamic visual benchmark designed to evaluate the mathematical reasoning robustness of VLMs. Unlike static benchmarks, DynaMath generates question variations programmatically to test models under diverse conditions. This allows for a nuanced assessment of VLMs’ robustness and generalization across mathematical tasks.

### Strengths
- The proposed dynamic benchmark for evaluating the mathematical reasoning robustness of VLMs are complementary to existing benchmarks, and it aligns well with the challenges in real-world mathematical applications, where variations in problem conditions often arise.
- Extensive evaluations on reasoning robustness are conducted and some observations are beneficial to the community.

### Weaknesses
 - Although the paper presents some error analysis, the model robustness is still underexplored. Quite a few factors are not investigated, such as the difficulty level and type of questions and variants.
- Besides the question itself, the prompt template can also result in different responses. The robustness regarding to prompt variants is neither studied nor excluded from the research scope with clear explanation.
- Deeper insights into the failure modes and interpretability would be great.

### Questions
1. It is uncertain if the benchmark could be easily hacked by just adopting the same program-based question generation to produce training data and then finetune the models.
2. Is the reasoning robustness relevant to the difficulty level and type of questions and variants?
3. Is there any preliminary study on how to scale the dynamic generation approach for more comprehensive and difficult benchmarks?
4. It would be insightful to know if the authors have tested any interventions (e.g., prompt adjustments) to increase the robustness and reduce the memorization phenomenon.
5. Is there any interpretability of the observations on the mathematical reasoning robustness?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
DynaMATH, a new benchmark for evaluating visual reasoning in vision language models, offers greater controllability than previous tools like MathVistas. Using 501 programmable seed questions with multiple variants, it tests both closed and open-source VLMs, revealing insights about worst-case accuracy and memorization patterns.

### Strengths
1. The paper effectively presents comprehensive and interesting findings.
2. The benchmark's controllability should be highlighted as a key strength.

### Weaknesses
1. The paper effectively presents comprehensive and interesting findings.
2. The benchmark's controllability should be highlighted as a key strength.

1. Move Figure 7 to the main paper to better illustrate the benchmark's appearance.
2. The paper lacks details about the seed question curation process and should address the benchmark's scalability limitations.

### Questions
Can the authors provide a rough time estimate for designing/redesigning seed questions? This is important for future benchmark design. Also, how can we scale up the design flow for a larger dynamic math benchmark?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces DYNAMATH, a dynamic visual math benchmark aimed at evaluating the mathematical reasoning robustness of Vision-Language Models (VLMs). 
The benchmark reveals that state-of-the-art VLMs, like GPT-4o, struggle with mathematical reasoning when visual numerical values or function graphs change, despite these tasks being simple for humans. 
DYNAMATH includes 501 seed questions, each represented as a Python program, capable of generating varied concrete questions with different visual and textual alterations. 
The benchmark was used to assess 14 VLMs (including proprietary ones and open-source ones) with 5,010 generated questions, showing a significant gap between average-case and worst-case model accuracy. 
The paper's contributions include identifying the weakness in VLMs' reasoning abilities, introducing DYNAMATH for robustness evaluation, and providing insights to guide the development of more reliable VLMs for mathematical reasoning.

### Strengths
1. DYNAMATH is the first dynamic visual math benchmark designed to evaluate the robustness of mathematical reasoning in VLMs. 
The dynamic generation of varied problem sets more accurately simulates real-world problem-solving, providing a more genuine assessment of model capabilities.
2. With 501 high-quality seed questions that can generate a multitude of variant problems across various mathematical topics and difficulty levels, DYNAMATH allows for an in-depth evaluation of VLMs' generalization abilities under different input conditions, revealing the limitations of current models when dealing with problem variations.

### Weaknesses
1. Lacks analysis of open-source VLMs performance under the zero-shot / few-shot setting.
2. Lacks analysis of the reproducibility of evaluation results (since temperature is not 0).
3. The paper does not provide a detailed breakdown of the problem types within DYNAMATH, specifically the distribution of multiple-choice, numerical answer, and free-form text questions.
4. While the paper introduces repetition consistency, it does not explore the circular consistency metric as defined in MMBench [1], which could reveal further insights into the models' robustness to input variations, particularly for multiple-choice questions.

### Questions
1. What about the zero-shot / few-shot COT results for open-source VLMs? It would be beneficial to present those results and do some analysis. 
2. Evaluating VLMs with temperature not set to 0 will make the results less reproducible. Will the evaluation result vary much when you run the evaluation multiple times? Can you provide an error bar for it? 
3. Would you please provide the detailed distribution of problems in DYNAMATH (multiple choice, answer is float, answer is text)? 
4. In MMBench [1], the authors have defined another consistency named circular consistency? Will the Repetition Consistency still be that high (>80%) when circular shift is applied to choices for MCQ problems in DYNAMATH?

[1] MMBench: Is Your Multi-modal Model an All-around Player?

### Soundness
3

### Presentation
3

### Contribution
3
