# CIRCUIT: A Benchmark for Circuit Interpretation and Reasoning Capabilities of LLMs

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
The role of Large Language Models (LLMs) has not been extensively explored in analog circuit design, which could benefit from a reasoning-based approach that transcends traditional optimization techniques. In particular, despite their growing relevance, there are no benchmarks to assess LLMs’ reasoning capability about circuits. Therefore, we created the CIRCUIT dataset consisting of 510 question-answer pairs spanning various levels of analog-circuit-related subjects. The best-performing model on our dataset, GPT-4o, achieves 48.04\% accuracy when evaluated on the final numerical answer. To evaluate the robustness of LLMs on our dataset, we introduced a unique feature that enables unit-test-like evaluation by grouping questions into unit tests. In this case, GPT-4o can only pass 27.45\% of the unit tests, highlighting that the most advanced LLMs still struggle with understanding circuits, which requires multi-level reasoning, particularly when involving circuit topologies. This circuit-specific benchmark highlights LLMs' limitations, offering valuable insights for advancing their application in analog integrated circuit design.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper introduces a CIRCUIT dataset. The dataset contains 510 questions and is evaluated via three LLM based models.

### Strengths
* Evaluation results looks extensive, with results analysed in detail to have a comprehensive understanding of their performane on the dataset introduced.

### Weaknesses
 * The dataset size may not be sufficient enough to fully evaliate the capabilities of LLMs in analogue circuit design.
* While the evaluation results do show there is imrovements in terms of accuracies on analogue circuit related questions, it is unclear how well does this translate in designing analogue circuits.
* The paper only tests on solutions using LLM only, it is not clear how circuit design using combination of different models could utilize this as a benchmark. This seems more like how to train a LLM using questions on how analogue circuits operate.

### Questions
please see weakness

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a Circuit Interpretation and Reasoning Capabilities (CIRCUIT) dataset to evaluate LLMs in understanding and reasoning about analog circuits. The authors conduct a series of experiments to assess the performance of various LLMs in understanding analog circuits and their topologies from diagrams and netlists.

### Strengths
1. This paper is the first to evaluate the ability of LLMs in circuit design domain and summarizes the limitations of existing LLMs according to the results. The authors summarize the limitations of existing models based on the experimental results. The qualitative analysis of errors offers valuable insights for improving LLMs.
2. This paper is well organized and clear.

### Weaknesses
1. The sources of problems are limited. Most of problems are collected from textbooks published more than 10 years ago, which primarily assess general knowledge of analog circuits. It should be beneficial to construct more challenging problems about complex analog IC designs from various sources, such as handmade questions according to modern IC datasheets. 
2. The categories in this dataset are imbalance. In Figure 3, most of Basic questions are in level 1, while RF questions are more challenging. Besides, there is a lack of detailed analysis regarding LLM performance across different levels and categories.

### Questions
1. How to differentiate between errors where LLMs have insufficient background knowledge about circuits and those where incorrect reasoning occurs? Do errors caused by insufficient knowledge fall under Direction Errors? 
2. A minor question about Table 4: how is the error rate calculated? I saw that the sum of each column or raw do not equal 1.

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
This paper focuses on the application of large language models (LLMs) in analog circuit design. Given that analog circuit design highly depends on human expertise and faces a labor shortage problem, the authors aim to evaluate the capabilities of LLMs in this field by creating the CIRCUIT dataset. The paper details the construction of the dataset, evaluation metrics and methods, and conducts experiments to evaluate multiple LLMs. Finally, it discusses the significance, limitations, and future directions of the research results.

### Strengths
1. The article constructs a dataset for analog circuits to evaluate the capabilities of LLM in analog circuits, promoting the exploration and research of LLM in analog circuits.
2. The construction of the dataset is relatively comprehensive, covering different difficulties, and considering diagrams and netlists.
3. The experiment is relatively detailed, testing and validating the current mainstream models and conducting analysis and summary.

### Weaknesses
1. The dataset focuses more on evaluating the LLM's answers to analog circuit questions, similar to math problems. However, it cannot verify the LLM's ability to assist in analog circuit design. For example, use a LLM to evaluate the quality of circuit design in terms of power, performance, and area (PPA). The current evaluation primarily tests the LLM's ability to perform symbolic analysis and solve for circuit parameters, which is a limited view of the overall design process. It does not assess the LLM's capacity to make design trade-offs or optimize for specific performance targets.
2. The dataset lacks diversity in design and does not cover the entire analog circuit design process. For example, circuit structure design, device selection, test verification and physical design, etc. The dataset appears to be limited to relatively simple circuit topologies and does not include more complex or specialized circuits commonly encountered in real-world analog design. There is a lack of representation of different design styles, such as current-mode circuits, switched-capacitor circuits, or RF circuits. Furthermore, the dataset does not include any information on device parameters, process variations, or layout considerations, which are crucial aspects of practical analog design.
3. The benchmark lacks an evaluation of the overall performance of the circuit. The evaluation metrics focus on the correctness of the answers to specific questions, but do not assess the overall performance of the designed circuit in terms of metrics such as gain, bandwidth, noise, linearity, or power consumption. These performance metrics are essential for evaluating the quality of an analog circuit design and should be considered in a comprehensive benchmark.

### Questions
1. How does the benchmark results help to improve LLM for EDA-aided design?
2. The current dataset focuses more on formula derivation and mathematical calculations, but may lack an understanding of how to evaluate LLM's understanding of the quality of analog circuit design. For example, evaluate the ability of large language models in predicting circuit PPA, ultra-parameter tuning of circuits, and test verification.

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
5

### Summary
This paper introduces a benchmark designed to evaluate the circuit interpretation and reasoning capabilities of large language models (LLMs). 
The benchmark comprises 510 question-answer pairs covering various areas of analog circuit design. 
Evaluations conducted on three representative LLMs provide some insights into the reasoning abilities of state-of-the-art models.

### Strengths
The paper presents an intriguing study on the capabilities of large language models (LLMs) in circuit interpretation and reasoning and offers some insights to advance research in leveraging LLMs for analog design automation. 

The dataset, comprising over 500 question-answer pairs sourced from a variety of courses and textbooks, appears substantial and non-trivial, providing a solid foundation for evaluating LLM performance in this domain.

### Weaknesses
The paper’s technical contributions appear limited, focusing primarily on prompt engineering.

Additionally, the benchmark used raises concerns: although it consists of 500 question-answer pairs, these questions are sourced from textbooks, which overly simplify the real-world challenges of analog circuit design. Analog circuit design involves multiple critical stages, such as topology generation, device sizing, and layout design, and it is unclear how the current benchmark addresses these complexities.

Furthermore, the results seem unreasonable. Instead of reporting only the overall accuracy, a more detailed breakdown of circuit performance across varying complexities should be presented. Understanding how the model handles complex analog circuit problems, as opposed to simpler ones, would provide far more meaningful insights into its effectiveness.

The insights are limited. It does not show how to improve the capabilities of LLM in addressing analog design automation.

### Questions
How does the benchmark address the different design stages of analog circuits? 
What is the success ratio of each level circuit (e.g., 1, 3, 5) based on the benchmark?

### Soundness
2

### Presentation
2

### Contribution
2
