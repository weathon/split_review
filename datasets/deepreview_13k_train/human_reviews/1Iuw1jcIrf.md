# MathCoder2: Better Math Reasoning from Continued Pretraining on Model-translated Mathematical Code

- Decision: Accept
- Scores: 8, 6, 8

## Abstract
Code has been shown to be effective in enhancing the mathematical reasoning abilities of large language models due to its precision and accuracy. Previous works involving continued mathematical pretraining  often include code that utilizes math-related packages, which are primarily designed for fields such as engineering, machine learning, signal processing, or module testing, rather than being directly focused on mathematical reasoning. In this paper, we introduce a novel method for generating mathematical code accompanied with corresponding reasoning steps for continued pretraining. Our approach begins with the construction of a high-quality mathematical continued pretraining dataset by incorporating math-related web data, code using mathematical packages, math textbooks, and synthetic data. Next, we construct reasoning steps by extracting LaTeX expressions, the conditions needed for the expressions, and the results of the expressions from the previously collected dataset. Based on this extracted information, we generate corresponding code to accurately capture the mathematical reasoning process. Appending the generated code to each reasoning step results in data consisting of paired natural language reasoning steps and their corresponding code. Combining this data with the original dataset results in a 19.2B-token high-performing mathematical pretraining corpus, which we name MathCode-Pile. Training several popular base models with this corpus significantly improves their mathematical abilities, leading to the creation of the MathCoder2 family of models. All of our data processing and training code is open-sourced, ensuring full transparency and easy reproducibility of the entire data collection and training pipeline.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a novel approach for enhancing mathematical reasoning in large language models (LLMs). Unlike previous models that used math-related code without detailed explanations, MathCoder2 generates mathematical code paired with natural language reasoning. This process involves filtering a large math-related dataset from web pages, synthetic sources, code, and textbooks to build a high-quality corpus called MathCode-Pile.

This dataset consists of 19.2 billion tokens and includes LaTeX-extracted mathematical expressions, conditions, results, and Python code to capture the underlying reasoning. MathCoder2 uses this corpus to significantly improve performance on various mathematical benchmarks, achieving results competitive with state-of-the-art models. Moreover, the MathCoder2 framework is fully open-source, which supports reproducibility and transparency in model training and data processing. This work sets a foundation for future research by focusing on reasoning capabilities through detailed code integration.

### Strengths
MathCoder2’s MathCode-Pile corpus is rigorously curated and filtered from diverse math-related sources, including web data, synthetic data, specialized code, and textbooks. This ensures relevance, reduces noise, and provides a comprehensive dataset tailored specifically for mathematical reasoning, which is essential for pretraining LLMs in this area.

MathCoder2 demonstrates significant gains on multiple mathematical reasoning benchmarks, outperforming comparable models across different tasks. The improvement underscores the effectiveness of continued pretraining on the structured MathCode-Pile corpus and shows MathCoder2's potential for real-world applications in math-intensive fields.

### Weaknesses
There are no major weaknesses.

### Questions
Python was chosen for code snippets; it it possible to use specialized math software language instead (e.g., Mathematica)? This is not a direct limitation of this paper, but a possible future direction.

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
4

### Summary
The paper "MathCoder2: Better Math Reasoning from Continued Pretraining on Model-translated Mathematical Code" explores enhancing the mathematical reasoning capabilities of LLMs through continued pretraining on a novel dataset called MathCode-Pile. This dataset is constructed from various sources, including math-related web data, textbooks, and synthetic data. A key contribution is the generation of paired natural language reasoning steps and Python code, aimed at improving the alignment between mathematical reasoning and executable code. The authors demonstrate significant improvements in mathematical reasoning benchmarks such as MATH and GSM8K, using models fine-tuned with MathCode-Pile. The paper also emphasizes the open-source nature of their data processing and training pipeline.

### Strengths
* Originality: The paper introduces a novel method of generating and pairing Python code with natural language reasoning steps, enhancing the mathematical reasoning capabilities of large language models.
* Quality of Dataset: The MathCode-Pile dataset, comprising 19.2B tokens, is a significant contribution, demonstrating meticulous curation from diverse sources like web data, math textbooks, and synthetic examples.
* Significant Performance Gains: The use of this dataset leads to notable improvements across various models, including Llama-3-8B, DeepSeekMath-7B, and Code-Llama-7B, especially on benchmarks like MATH and GSM8K.
* Detailed Methodology: The process of extracting LaTeX expressions, conditions, and results to generate corresponding Python code is well-documented, offering transparency and reproducibility.
* Open-Source Commitment: The release of data processing and training code enhances the research community's ability to validate and build upon this work.

### Weaknesses
 * Generalizability of Code Generation: The method’s applicability to more abstract or advanced mathematical domains is unclear, particularly beyond high-school-level math. The reliance on Python code generation, while effective for problems with clear computational solutions, may not extend well to areas requiring symbolic manipulation or formal proof construction. For example, the approach might struggle with problems involving abstract algebra or advanced calculus, where the reasoning steps are not easily translated into executable code.
* Evaluation Uncertainty: It is ambiguous whether the generated Python code is executed during benchmark evaluations or merely used for pretraining, leaving questions about its practical impact. The paper does not clearly specify if the reported performance gains are due to the model's improved reasoning capabilities or its ability to leverage the generated code during inference. This distinction is crucial for understanding the true contribution of the method. If code execution is not part of the evaluation, the practical utility of the code generation aspect is diminished.
* Scope Limitation: The focus on grade-school-level mathematics is not explicitly emphasized, potentially misleading readers about the dataset’s broader applicability. While the paper mentions benchmarks like MATH and GSM8K, it does not clearly state that the dataset and method are primarily designed for problems within this range. This lack of clarity could lead to misinterpretations regarding the method's suitability for more advanced mathematical reasoning tasks.
* Ablation Study Depth: While the ablation studies show the value of the synthesized code, further exploration into the necessity of aligning reasoning steps with code versus treating them as independent could provide deeper insights. The current ablation study does not fully explore the impact of the alignment between the natural language reasoning steps and the generated code. It remains unclear whether the performance gains are primarily due to the paired nature of the data or if the code and reasoning steps could be treated as independent training signals.

### Questions
* Code Execution in Evaluation: Is the Python code generated and executed during benchmark evaluations? Clarifying this would help to understand the role of Tool-Integrated Reasoning in the observed performance improvements.
* Generalization to Formal Proofs: Can the method be extended to generate formal proofs in languages like Lean or Coq? Specifically, how well does the approach handle abstract reasoning steps that require formal verification, which might be better suited to proof assistants rather than executable Python code?
* Independent Reasoning Steps: Would separating reasoning steps and corresponding code into independent examples still yield significant improvements? Such an ablation could help assess the criticality of their alignment in the dataset.

### Soundness
3

### Presentation
3

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
This paper proposes MathCode-Pile, a 19.2B-token dataset of math text and Python code. The dataset includes high-quality math-related web content, code with mathematical packages, math textbooks, and synthetic data. In addition, they present MathCoder2, a family of large language models with enhanced mathematical reasoning capabilities over MathCode-Pile.

### Strengths
1. The author combining symbolic math reasoning with executable code in the dataset, MathCode-Pile, which is noval. This innovative methodology extends prior research, making MathCode-Pile a significant resource for advanced math reasoning tasks.

2. The paper is clearly organized, with a well-structured explanation of each step in the MathCode-Pile creation and model evaluation process. Figures and tables also effectively illustrate the overall data pipeline.

3. This work has great significance in advancing mathematical reasoning within language models. MathCoder2, using MathCode-Pile, achieves superior results on math benchmarks, demonstrating the potential of code-paired reasoning data.

### Weaknesses
1. The paper lacks a analysis of potential data leakage between MathCode-Pile and evaluation benchmarks, which could artificially inflate model performance.

### Questions
I have interested about whether the MathCode-Pile’s strong focus on mathematical reasoning might impact the model’s performance in non-mathematical domains. For example, whether this dataset would enhance the model’s general coding abilities beyond math-focused tasks.

### Soundness
4

### Presentation
4

### Contribution
4
