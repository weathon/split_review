# QCircuitNet: A Large-Scale Hierarchical Dataset for Quantum Algorithm Design

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 5, 3

## Abstract
Quantum computing is an emerging field recognized for the significant speedup it offers over classical computing through quantum algorithms. However, designing and implementing quantum algorithms pose challenges due to the complex nature of quantum mechanics and the necessity for precise control over quantum states. 
Despite the significant advancements in AI, there has been a lack of datasets specifically tailored for this purpose. 
In this work, we introduce QCircuitNet, the first benchmark and test dataset designed to evaluate AI's capability in designing and implementing quantum algorithms in the form of quantum circuit codes. Unlike using AI for writing traditional codes, this task is fundamentally different and significantly more complicated due to highly flexible design space and intricate manipulation of qubits. 
Our key contributions include: 
\begin{enumerate}
\item A general framework which formulates the key features of quantum algorithm design task for Large Language Models.
\item Implementation for a wide range of quantum algorithms from basic primitives to advanced applications, with easy extension to more quantum algorithms.
\item Automatic validation and verification functions, allowing for iterative evaluation and interactive reasoning without human inspection.
\item Promising potential as a training dataset through primitive fine-tuning results.
\end{enumerate}
We observed several interesting experimental phenomena: fine-tuning does not always outperform few-shot learning, and LLMs tend to exhibit consistent error patterns. QCircuitNet provides a comprehensive benchmark for AI-driven quantum algorithm design, offering advantages in model evaluation and improvement, while also revealing some limitations of LLMs in this domain.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces QCircuitNet, a novel dataset aimed at facilitating AI-driven quantum algorithm design. This dataset provides benchmarks and tools to evaluate the ability of LLMs to generate and validate quantum algorithms in quantum circuit code. QCircuitNet provides an automatic verification framework that ensures circuit validity.

### Strengths
The paper introduces QCircuitNet, and it provides a comprehensive structure, including benchmarks, automatic validation, and compatibility with various algorithms. Additionally, it offers a unique framework for large language models by formulating quantum algorithms as programming tasks.

### Weaknesses
See Questions.


1. In QcircuitNet, what is the specific number of circuits, and what is the range of qubits? As a benchmark, the description of the dataset is unclear.

2. Directly using LLMs to design quantum algorithms remains challenging. For workflows like Figure 2, can LLMs only learn specific quantum algorithms? However, with the limited algorithms/circuit types in the current benchmark, it seems insufficient to evaluate LLMs’ ability to design arbitrary quantum algorithms.

3. The current setup relies on classical simulations for verification, which limits scalability and slows down processes, especially for higher qubit counts. If real quantum computers are used, significant noise will be present. In such cases, how can effective verification be ensured?

### Questions
1. In QcircuitNet, what is the specific number of circuits, and what is the range of qubits? As a benchmark, the description of the dataset is unclear.

2. Directly using LLMs to design quantum algorithms remains challenging. For workflows like Figure 2, can LLMs only learn specific quantum algorithms? However, with the limited algorithms/circuit types in the current benchmark, it seems insufficient to evaluate LLMs’ ability to design arbitrary quantum algorithms.

3. The current setup relies on classical simulations for verification, which limits scalability and slows down processes, especially for higher qubit counts. If real quantum computers are used, significant noise will be present. In such cases, how can effective verification be ensured?

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
4

### Summary
The authors present a new dataset, QCircuitNet, for Quantum Algorithm Design, aimed at enhancing the design and implementation of quantum algorithms using LLMs. The authors a structured framework that allow the LLMs to apply to the quantum algorithm discovery. QCircuitNet features built-in functions for automatic validation and verification of algorithms, supporting iterative evaluation without human intervention. Experiments results highlight the evaluation of LLMs for quantum algorithm discovery with dataset, showcasing its potential as a valuable resource in the field.

### Strengths
1. QCircuitNet is the first dataset specifically designed for evaluating LLMs in quantum algorithm design.

2. The authors provide a structured framework that encapsulates key features of quantum algorithm design, allowing LLMs to work effectively with complex quantum tasks.

3. The paper presents valuable experimental findings regarding the performance of LLMs in quantum algorithm discovery.

### Weaknesses
1. The paper primarily addresses quantum circuit design as a language modeling task, which may limit the scope of quantum algorithm generation and overlook other important methodologies. Specifically, framing quantum algorithm design as a code generation problem may not fully capture the nuances of quantum computation. The discrete nature of code generation might struggle to represent continuous parameters inherent in many quantum algorithms, such as the rotational angles in parameterized quantum circuits. This approach risks overlooking methodologies that rely on continuous optimization or mathematical formulations.

2. The authors do not address Variational Quantum Algorithms, which are significant in near term quantum computing, indicating a gap in the dataset's comprehensiveness. The exclusion of VQAs is a significant limitation, as these algorithms represent a major area of research and application in the field. VQAs often involve iterative optimization of circuit parameters, a process that is not well-represented by the current dataset's focus on discrete circuit design. This omission limits the dataset's applicability to a substantial portion of contemporary quantum algorithm research.

3. Given the limited research on LLMs for quantum circuits, the necessity of creating this dataset at this stage may be questioned. While the idea of using LLMs for quantum algorithm design is interesting, the current state of research in this area is not mature enough to justify the creation of a specialized dataset. The lack of established methodologies and benchmarks for LLMs in quantum computing raises concerns about the dataset's immediate utility and impact.

4. The evaluation metrics used are heavily influenced by natural language processing. It raises the question of whether there might be a more intrinsic approach to integrating quantum into these metrics. The reliance on NLP metrics like BLEU may not accurately reflect the performance of quantum algorithms. These metrics often focus on syntactic similarity rather than the functional correctness or quantum mechanical properties of the generated circuits. A more intrinsic approach would involve metrics that directly assess the quantum mechanical behavior of the generated circuits, such as fidelity or entanglement measures.

### Questions
1. Why did you choose to focus primarily on quantum circuit design as a language modelling task? 

2. Are there alternative methodologies or frameworks that could also be explored for quantum algorithm discovery with your dataset?

2. What is your rationale for excluding VQAs from QCircuitNet? How do you see their importance in the context of quantum algorithm design?

3. Have you considered developing metrics that are more aligned with quantum computing?

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper introduces QCircuitNet, a benchmark dataset specifically designed to evaluate AI's capability in designing and implementing quantum algorithms as quantum circuit codes.

### Strengths
1. A proposed method effectively captures quantum algorithms, situated between pure mathematical formulas and natural language.

### Weaknesses
1. The dataset contains only classic algorithms and lacks generalizability.
2. Lacks tests for code completion.

### Questions
1. Why call "QCircuitNet"? I mean it is more like a neural network rather than a dataset or benchmark. This name is confusing.
2. How many algorithms are currently included in the dataset? Does each algorithm contain test data with different number of qbits?
3. "The total computation cost is approximately equivalent to two days on an A100 GPU." you mean to test one model or all the experiments add up cost 2days? 
4. Can you incorporate "chain of thought" in this benchmark?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents QCircuitNet, the benchmark and test dataset for evaluating AI’s ability to design and implement quantum algorithms in quantum circuit codes.

### Strengths
+ Interesting direction of using AI/LLM for developing quantum circuits for a particular quantum algorithm
+ Dataset can be useful to some extent

### Weaknesses
 + Not clear what exactly are the new contributions in addition to the “run_and_analyze” function.

 This paper claims that existing application benchmarks fail as a dataset for AI because they did not capture the design patterns of each algorithm, ignore post-processing and construction of different oracles. However, after reading the paper, I could not find what exactly are the “design patterns” of a quantum algorithm. The paper did not clarify any circuit features, or algorithm features, or device features. 

 Meanwhile, It seems this work only focuses on oracle-based quantum algorithms, which represents a very small group of quantum algorithms that were well-known and developed many years ago (and is also not the main focus of the quantum computing/algorithm community).

 It seems to me this claimed ‘dataset contribution’ is only a different way of selling the application benchmarks by (i) collecting the standard descriptions of particular quantum algorithms from text or existing paper; (ii) running in Qiskit-Aer to obtain standard output as the reference; (iii) adding metric measurement functions for the feedback/reward/gradient, which can be easily achieved using the MQTBench templates online. With that, I don’t think the technical contribution is sufficient for an ICLR publication. 

 Last but not least, the word ‘post-processing’ is confusing, as in quantum computing, post-processing usually refers to error-mitigation.

### Questions
This paper claims that existing application benchmarks fail as a dataset for AI because they did not capture the design patterns of each algorithm, ignore post-processing and construction of different oracles. However, after reading the paper, I could not find what exactly are the “design patterns” of a quantum algorithm. The paper did not clarify any circuit features, or algorithm features, or device features. 

Meanwhile, It seems this work only focuses on oracle-based quantum algorithms, which represents a very small group of quantum algorithms that were well-known and developed many years ago (and is also not the main focus of the quantum computing/algorithm community).

It seems to me this claimed ‘dataset contribution’ is only a different way of selling the application benchmarks by (i) collecting the standard descriptions of particular quantum algorithms from text or existing paper; (ii) running in Qiskit-Aer to obtain standard output as the reference; (iii) adding metric measurement functions for the feedback/reward/gradient, which can be easily achieved using the MQTBench templates online. With that, I don’t think the technical contribution is sufficient for an ICLR publication. 

Last but not least, the word ‘post-processing’ is confusing, as in quantum computing, post-processing usually refers to error-mitigation.

### Soundness
2

### Presentation
2

### Contribution
2
