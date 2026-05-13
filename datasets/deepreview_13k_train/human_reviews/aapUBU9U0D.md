# Evo-Step: Evolutionary Generation and Stepwise Validation for Optimizing LLMs in OR

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
Large Language Models (LLMs) have revolutionized various domains but face significant challenges in tackling optimization modeling tasks for Operations Research (OR) problems,  particularly when dealing with complex problem. In this work, we propose Evo-Step-Instruct, a framework that augments existing datasets and generates high-quality fine-tuning data tailored to OR modeling tasks.  Evo-Step-Instruct employs iterative problem generation to progressively increase problem complexity and stepwise validation to rigorously validate data, preventing error propagation and ensuring the quality of the generated dataset. Leveraging this framework, we fine-tune open-source LLMs, including LLaMA-3-8B and Mistral-7B, to develop Evo-Step—a model that achieves state-of-the-art performance on benchmarks such as NL4OPT, MAMO, and IndustryOR. Extensive experiments demonstrate the superior performance of Evo-Step, especially in addressing complex OR tasks, with a notable 17.01\% improvement in micro average accuracy on difficult problems. These findings highlight the effectiveness of combining structured validation with gradual problem refinement to advance the automation of decision-making processes using LLMs. The code and dataset are available at [https://anonymous.4open.science/r/Evo-Step-F5AB](https://anonymous.4open.science/r/Evo-Step-F5AB).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes an evolutionary framework for data generation for training LLMs for OR optimization modelling. The data generation consists of two parts, with the first evolutionary one, for instance, generation and the second one for solution assessment and refinement. The results are compared on three OR datasets of different difficulty. Promising results are generated when compared to existing LLMs with prompt engineering techniques and domain OR LLMs.

### Strengths
1.The framework automates the data generation process, enhancing efficiency and effectiveness.
2. The paper is well-structured and easy to follow, facilitating comprehension.

### Weaknesses
1. Although the results contribute to specific OR optimization problem modeling, the technique's contribution appears incremental, as the evolution process in data generation has been previously explored.
2. It is recommended to include more comparative studies with SOTA LLMs and provide additional explanations to further validate the results.

### Questions
1. How many queries are utilized during instance generation? What is the total cost? What percentage of samples are discarded during the data generation process?
2. The authors mention testing both COPT and GUROBI. It is unclear whether they use the same independent data generation pipeline and prompts for each. 
3. Are all experimental results based on COPT, GUROBI, or are they selecting the best outcomes from either? Additionally, if OMLR is only trained with COPT, is it appropriate to use the original checkpoint directly?
4. What would be the impact of directly applying the proposed "Stepwise Validation Mechanism" to SOTA LLMs, such as GPT-4, in modeling tasks? Would this significantly enhance accuracy and performance?

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
4

### Summary
This work aims to enhance large language models (LLMs) for complex optimization in Operations Research by evolving problem complexity and integrating real-time validation. Fine-tuned on generated data, the Evo-Step model significantly outperforms benchmarks, improving accuracy on challenging tasks, demonstrating the power of evolutionary problem generation for advanced decision-making automation.

### Strengths
1. This work considers different aspects such as problem generation, validation and LLMs fine-tune.
2. The proposed method achieves good performance on different operation problems.

### Weaknesses
 1. The presentation is poor especially the diagrams. Their captions are so short to understand what they intend to convey. The caption should be significantly expanded and improved.
2. There are some inaccurate expressions. For example, evolutionary strategy specifically refer to a branch algorithm in the evolutionary optimization instead of an arbitrary strategy related to evolution. 
3. The problem formulation needs further clarification. Normally, we propose a method/framework to solve a or several problems. However, you are trying to solve a large number of problems simultaneously. How to ensure its effectiveness would be a very serious issue. In addition, the problem to solve is also not clear to readers.
4. I suggest to use the proposed method to solve some OR problems and compare it with some traditional methods instead of LLM-based method, which can help demonstrate the effectiveness of your method.

### Questions
1. How do you fine-tune the LLMs? What technique do you use? Details  are lacking.
2. What is the contribution of this work in solving OR problems? It seems to focus on more how to generate problems and validation, which might be more trivival compared to solve problem itself.

### Soundness
2

### Presentation
2

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
This study proposes Evo-Step-Instruct, a new framework that incrementally escalates problem complexity using an evolutionary approach to strengthen LLMs' performance in optimization modeling. The framework employs progressive validation to enable immediate error identification and correction.

### Strengths
Evo-Step exhibits outstanding performance, particularly in managing complex OR tasks, with a significant 17.01% increase in micro-average accuracy on challenging problems.

### Weaknesses
The presentation requires substantial improvement, as the current version is difficult to comprehend and does not clearly convey the contributions. Here, I will first list some shortcomings:

(1) The caption of figures is not informed enough and it is difficult to understand the content of diagrams.

(2) Evolutionary Strategy (ES) typically refers to a type of evolutionary algorithm focused on optimizing complex problems by mimicking natural selection processes. However, I cannot see any element of Evolutionary Strategy in Figure 1, which is claimed as the example of evolutionary strategy.

(3) The citation format is not good and needs improvement.

### Questions
Due to the presentation, it it hard to fairly evaluate this work at the current stage. As such, I will reconsider this work after the following queries have been addressed:

(1) In this work, I cannot see any evolutionary components such as crossover and mutation. How do you evolve and what do you evolve?

(2) The contribution of this work is not clear or even a bit confused. This work states "increases the complexity of generated problems", why we need to generate problems on our own? A more convincible direction should be that we use LLMs to generate solution to the problems.

(3) How do you fine-tune the open-source LLMs? What technique do you use? 

(4) More experiments are required such the the comparison with tradition algorithms (non-LLM approach). LLMs are unnecessarily suited to every task, thus it is important to justify the strength of LLMs in this task.

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
Evo-Step-Instruct is a framework that uses evolutionary problem generation and stepwise validation to enhance LLMs in Operations Research (OR) tasks. Evo-Step incrementally builds datasets of increasing complexity, applying validation checks to prevent error propagation, and yields strong results on OR benchmarks like NL4OPT and IndustryOR.

### Strengths
The evolutionary strategies combined with real-time validation ensure high-quality data generation, reducing the need for post-processing, and the approach significantly outperforms baseline models on complex OR problems.

### Weaknesses
The computational demands of the approach could limit scalability, and Evo-Step’s OR-specific design may constrain its applicability to other domains.

### Questions
Question 1: Could the authors elaborate on Evo-Step’s computational requirements and its scalability for larger datasets or in different domains?

Question 2: How adaptable is Evo-Step’s framework for domains outside OR, and what modifications would be necessary?

### Soundness
3

### Presentation
3

### Contribution
3
