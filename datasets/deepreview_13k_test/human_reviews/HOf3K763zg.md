# Beyond Differentiability: Neurosymbolic Learning with Black-Box Programs

- Decision: Reject
- Scores: 5, 5, 3, 6

## Abstract
Neurosymbolic learning has demonstrated promising potential as a paradigm to combine the worlds of classical algorithms and deep learning. However, existing general neurosymbolic frameworks require that programs be written in differentiable logic programming languages, restricting their applicability to a small fragment of algorithms. We introduce Infer-Sample-Estimate-Descend (ISED), a general algorithm for neurosymbolic learning with black-box programs. We evaluate ISED extensively on a set of 30 benchmark tasks that encompass rich data types and reasoning patterns. ISED achieves 30% higher accuracy than end-to-end neural baselines. Moreover, ISED's solutions often outperform those obtained using Scallop, a state-of-the-art neurosymbolic framework: the programs in 17 (61%) of the benchmarks cannot be specified using Scallop, and ISED on average achieves higher accuracy on those that can be specified using Scallop.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work presents a general framework for neurosymbolic learning with black-box programs (ISED). This framework does not need the differentiability of the program and uses a sampling-based method to approximate the gradient of the program execution. The evaluation results show that ISED is more accurate.

### Strengths
1. This paper uses lots of illustrations, which make the presentation clear.

### Weaknesses
1. Limited Benchmark: The evaluation compares with Scallop and CNN. However, this work did not compare with another differentiating neurosymbolic program work: DeepProbLog, which limits the significance of the performance.
2. Scalability. This work can only cover an input length of 7, concluding the multiplication and additional operation. However, a traditional neurosymbolic program’s statement may not limit two these two operations.

### Questions
1. How accurate the sampling-based method is? Is there any theoretical analysis about the gradient error from the estimation?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a general Neuro-Symbolic solver approach using fixed black-box programs with the premise this allows anyone to write the program in any language as it removes the need for the program to be differentiable. This changes the neurosymbolic problem from program inference, to focus on parameter sampling and gradient propagation around the black box. The authors show that on three tasks  calculation, sorting and disease detection their method is able to outperform the baseline.

### Strengths
- In principle, the approach is a general-purpose neuro-symbolic approach.
- Despite the removal of gradients during the execution step, the performance is equivalent to the baseline
- The idea of using user-defined programs in execution is interesting and novel.
- The author's multi-dataset evaluation provides a broad context in different settings.  However, the leaf disease setting does not need to be a neuro-symbolic approach as shown by the simple program. A spatial reasoning test would probably have been a better choice.

### Weaknesses
- The introduction of the black-box programs seems to constrain the problem largely. In the writing, it isn't clear if the programs are only used as supervision or explicitly used as the symbolic aspect. If it is the latter this greatly reduces the difficulty of the problem as the symbolic aspect is largely unneeded, as you could include an expert program to solve without needing symbolic, this is especially evident in the leaf disease test as there are a number of off the shelf expert models that could be applied without needing a threshold of % diseased. The approach would have been better argued by another approach, such as logical reasoning, ideally on Knowledge Graphs, which would be a compatible setting to prior methods, increasing the number of comparisons the authors could perform.
- It isn't clear how this would scale to larger, more complex problems where the black-box program actually is complex. All examples are relatively trivial.
- It isn't clear how they handle the gradients around the black box as they just state an optimizer solves this without any specificity.

### Questions
- Greater explanation of whether the programs are learnt or if they only the inputs are being estimated.
- Explanation of how gradients are propagated
- Any prediction of how this would scale to complex problems

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This article introduces a Neuro-Symbolic learning framework designed to utilize structured knowledge pertaining to the outputs of neural networks, expressed through black-box programs. The method proposed in this paper requires only that the reasoning part be capable of forward reasoning, without necessitating that the output of the reasoning part be differentiable with respect to the input. Authors validate the adaptability of the learning framework through extensive experimentation on a variety of synthetic and classic benchmarks.

### Strengths
1.	The paper is easy to read, with Figures 1 and 2 providing a clear and intuitive illustration of the proposed method.
2.	The paper conducts a comprehensive evaluation of the proposed method on synthetic and classic tasks such as MNIST Add, HWF and Sorting, demonstrating the method’s adaptability.

### Weaknesses
1.	In the abstract, the authors mention that ‘existing general neuro-symbolic frameworks require that programs be written in differentiable logic programming languages’. However, there already exist frameworks aiming at bridging machine learning and logic reasoning such as Semantic Loss [1], Abductive Learning [2] and NEUROLOG [3], which do not impose a requirement for differentiability and they use non-differentiable programs. The paper does not conduct comparisons with such methods.
2.	The novelty of the proposed work needs to improve to meet the desired standards. The method proposed in this paper involves employing the REINFORCE algorithm to eliminate the requirement for differentiability in neural-symbolic system. However, this idea has already been introduced in the previous work [4]. Another critical component of the method, 'Estimate', fundamentally constitutes a sampling estimation of the well-known semantic loss [1], yet the paper does not provide reference to this work.

[1] Jingyi Xu, Zilu Zhang, Tal Friedman, Yitao Liang, and Guy Van den Broeck. A Semantic Loss Function for Deep Learning with Symbolic Knowledge, ICML 2018.

[2] Zhi-Hua Zhou. Abductive learning: Towards bridging machine learning and logical reasoning. Science China Information Sciences, 2019. 

[3] Tsamoura, Efthymia, Timothy Hospedales, and Loizos Michael. Neural-Symbolic Integration: A Compositional Perspective, AAAI 2021.

[4] Cornelio Cristina, Jan Stuehmer, Shell Xu Hu, and Timothy Hospedales. Learning where and when to reason in neuro-symbolic inference, ICLR 2023.

3.	Inconsistent styles: some NeurIPS references include page numbers, while others do not; some conference names have abbreviations, while others do not.

### Questions
1.	Prolog is Turing-complete, possessing the same expressive capabilities as Python, and is also suitable for general-purpose use.
2.	The neural network's initial performance is nearly equivalent to a random output, and methods based on sampling may encounter difficulties in capturing certain symbols. How you address this cold start issue?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors of this paper introduce a new approach to neurosymbolic learning called Infer-Sample-Estimate-Descend (ISED). Neurosymbolic learning aims to combine classical algorithms and deep learning. Unlike existing neurosymbolic frameworks, ISED allows for the use of black-box programs written in general-purpose languages, expanding its applicability. ISED is designed for algorithmic supervision, where a black-box program is applied to the output of a neural model, and the goal is to optimize the model parameters using end-to-end labels. ISED consists of four phases: Infer, Sample, Estimate, and Descend, where neural models predict distributions for inputs, samples are generated, the program is executed, probabilities are estimated, and the loss function is computed. ISED is evaluated on 30 benchmark tasks with black-box programs written in Python and achieves higher accuracy than end-to-end neural approaches, often outperforming a state-of-the-art neurosymbolic framework called Scallop.

### Strengths
Good performance and quality experiences with clear text .

### Weaknesses
Poor quantitative aspects of training, including memory requirements, training time for each model, and for each dataset.

### Questions
What are the shortcomings related to the quantitative aspects of training, such as memory requirements, training time for each model, and for each dataset?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
