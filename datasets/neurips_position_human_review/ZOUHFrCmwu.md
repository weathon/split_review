# The Road to Generalizable Neuro-Symbolic Learning Should be Paved with Foundation Models

- Decision: Reject
- Scores: 3, 5, 8

## Abstract
Neuro-symbolic learning was proposed to address challenges with training neural networks for complex reasoning tasks with the added benefits of interpretability, reliability, and efficiency.
Neuro-symbolic learning methods traditionally train neural models in conjunction with symbolic programs but they face significant challenges that limit them to simplistic problems.
On the other hand, purely-neural foundation models now reach state-of-the-art performance through prompting rather than training, but they are often unreliable and lack interpretability.
Supplementing foundation models with symbolic programs, which we call neuro-symbolic prompting, provides a way to use these models for complex reasoning tasks.
Doing so raises the question: What role does specialized model training as part of neuro-symbolic have in the age of foundation models?
To explore this question, we highlight three pitfalls of traditional neuro-symbolic learning with respect to the compute, data, and programs leading to generalization problems.
This position paper argues that
foundation models enable generalizable neuro-symbolic solutions,
offering a path towards achieving the original goals of neuro-symbolic learning without the downsides of training from scratch.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper argues that with the advent of foundation models neuro-symbolic training should be substituted by neuro-symbolic prompting.
The argument is supported by two main observations
- Computation level: it is not necessary to train from scratch as current foundation models are already good at extracting good symbolic representations when properly prompted on traditional neuro-symbolic benchmarks.
- Representation level: neuro-symbolic training is based merely on a top-down approach resulting in the symbol grounding problem (e.g. the neural network learns the wrong input-output mapping)
Both observations are backed up by experimental analysis.

### Strengths
- The paper is very clearly written and I enjoyed the reading **Clarity**
- The hypothesis questions and the experimental analysis are very original and compelling to support the proposed approach **Originality**.
- The work may be of interest to the neuro-symbolic community **Scope**.


**Weaknesses**
- The paper seems to propose a solution rather than a position **Significance**. As a matter of fact, clear challenges and a roadmap are currently missing and should be explicitly provided for a position paper.
- It is not clear what is the difference between the proposed solution and constrained decoding used in LLMs for constrained generation **Significance**
- There is an important misconception, which is an artifact of the naming conventions. Note that neuro-symbolic training differs from the problem of neuro-symbolic integration. One can achieve the former through a simple top-down approach, whereas the latter requires a two-way communication between the neural and symbolic components. The paper focuses on the former and therefore has limited potential impact **Significance**

### Weaknesses
- see above *Strengths*
- Imprecise related work. The symbol grounding problem was first introduced by [1] in [2]. The work in [3] first revived the simple grounding problem in the machine learning community through a simple instantiation using a sequence of MNIST images. Later Marconato et al. [4] extended this idea to a larger set of tasks, giving a different name to the same problem. Again reasoning shortcuts is a misnomer as the problem arises simply from the fact that learning occurs in a top down fashion, where the neural network is informed only by the supervisory information of the program, thus not necessarily capturing information of the input (indeed symbols should be grounded on perceptual information, hence the name symbol grounding problem). The recent work in [5] demonstrates that a joint combination of bottom up and top down training is sufficient to mitigate this issue.
- continued in *Questions*

### Questions
- The discussion about program and data pitfalls seems to be an effect of the symbol grounding problem **Discussion**. 
    - Program pitfalls “using programs as a component in neuro-symbolic training can lead to the neural component hallucinating symbols” -> this is the problem of symbol grounding as neuro-symbolic training is typically performed in a top down fashion
    - Data pitfalls “neuro-symbolic training with specialized datasets, as opposed to large-scale foundation model pretraining, encourages overfitting to dataset particularities.” -> This is again a problem of top-down training

**References** \
[1] The symbol grounding problem. Physica D: Nonlinear Phenomena 1990 \
[2] Perceptual symbol systems. Behavioral and Brain Sciences 1999 \
[3] Learning Symbolic Representations Through Joint GEnerative and DIscriminative Training. ICLR Workshop 2023 \
[4] Neuro-symbolic continual learning: Knowledge, reasoning shortcuts and concept rehearsal. ICML 2023 \
[5] Unifying Self-Supervised Clustering and Energy-Based Models. To appear in TMLR 2025

### Presentation
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper claims that the traditional neuro-symbolic training introduced scalability and training issues which limited its effectiveness to overly simplistic domains. The authors believe that prompting along is often enough to solve many tasks without training in the age of foundational models. They highlight three pitfalls of neuro-symbolic training with respect to compute, data and programs, and encourage future research on neuro-symbolic prompting systems which infer the necessary symbols and program for solving a problem.

### Strengths
1. The paper provides clear arguments with empirical evidence on various datasets for its position. 
2. The proposal of the paper may be interested to the neuro-symbolic learning community.

### Weaknesses
1. The paper doesn't address the pitfalls of traditional neuro-symbolic learning by leveraging data augmentation or synthetic data generation.

### Questions
Can you answer the questions in the weaknesses?

### Presentation
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This position paper argues that neuro-symbolic prompting, a paradigm in which foundation models (FMs) are used for perception tasks like symbol extraction, while symbolic programs handle reasoning, offers a more scalable and generalizable alternative to traditional neuro-symbolic systems. In contrast, the traditional approach relies on end-to-end training of neural and symbolic components, which the authors argue is less effective in the era of foundation models. The authors identify three major pitfalls in the traditional approach: the compute pitfall (inefficient and costly training), the data pitfall (overfitting and lack of robustness), and the program pitfall (symbol hallucination due to weak supervision). Through empirical evaluations across five benchmarks, the paper demonstrates that prompting-based systems can match or outperform training-based ones, while offering improved interpretability and reducing the need for annotated data. The authors introduce the symbol hallucination rate as a novel metric to assess the reliability of intermediate representations and highlight autonomous program and symbol inference as a key direction for future research.

### Strengths
1. The paper presents a clear, well-structured argument for shifting from neuro-symbolic training to prompting, with well-defined pitfalls supported by both quantitative and qualitative evidence.
2. It is well-written and accessible to both neuro-symbolic and foundation model researchers, with strong diagrams, terminology, and a helpful taxonomy that guides critique and future work.
3. The topic is timely and relevant, addressing core concerns like interpretability, reliability, and efficiency in the context of evolving ML paradigms.
4. Extensive experiments across diverse benchmarks (Sum5, HWF5, CLUTRR, CLEVR, Leaf) compare traditional systems (Scallop, ISED) with prompting-based approaches using state-of-the-art FMs (e.g., Gemini, GPT-4o, LLaMA 3.2), grounding the argument in empirical evidence.
5. The paper introduces the novel symbol hallucination rate metric, offering a thoughtful way to assess the reliability of intermediate representations—validated through human evaluation.
6. It encourages a shift in research focus toward program synthesis and symbol inference, rather than training perception models from scratch.
7. Code is promised and experiments are replicable, enhancing the paper’s practical value.

### Weaknesses
1. The paper briefly mentions finetuning but largely dismisses it in favor of prompting. A more balanced discussion of its advantages especially in low-resource or domain-specific contexts would strengthen the argument.
2. The paper argues prompting is preferable because it avoids training. However, it overlooks the high inference costs of foundation models. Quantitative comparisons (e.g., compute time, energy, API costs) are missing and would be valuable for practitioners.
3. The proposed metrics, like symbol hallucination, rely on ground-truth intermediate symbols, limiting applicability to real-world, unannotated data. Practical evaluation strategies or proxy metrics are not provided.
4. Reliance on external, often closed-source foundation models raises productization concerns where model behavior may change across time which can break deterministic programs relying on specific FM outputs. The paper lacks discussion on versioning, regression testing, and safeguards against model drift.

### Questions
1. How well would neuro-symbolic prompting generalize to domains with limited or noisy data, such as medical imaging or legal reasoning?
2. How does the cost and latency of prompting large foundation models compare to training smaller, task-specific models in real-world deployment scenarios?
3. What evaluation protocols or proxy metrics would you propose when annotated symbols aren’t available?
4. In which regimes would training specialized neural components remain necessary, and how might hybrid fine-tuning + prompting approaches fit?

### Presentation
4
