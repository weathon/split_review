# Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
Self-improvement is a mechanism in Large Language Model (LLM) pre-training, post-training and test-time inference. We explore a framework where the model verifies its own outputs, filters or reweights data based on this verification, and distills the filtered data.  Despite several empirical successes, a fundamental understanding is still lacking. In this work, we initiate a comprehensive, modular and controlled study on LLM self-improvement. We provide a mathematical formulation for self-improvement, which is largely governed by a quantity which we formalize as the *generation-verification gap*. Through experiments with various model families and tasks, we discover a scaling phenomenon of self-improvement -- a variant of the generation-verification gap scales monotonically with the model pre-training flops. We also examine when self-improvement is possible, an iterative self-improvement procedure, and ways to improve its performance. We believe our results have several empirical implications, and our study leaves many exciting future directions for understanding the potential and limits of LLM self-improvement.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper investigates the concept of self-improvement in Large Language Models (LLMs) during pre-training, post-training, and test-time inference. The authors present a framework where the model verifies its own outputs, refines or reweights data based on this verification, and distills the filtered data. Despite empirical successes, there is a lack of fundamental understanding of this process. The study offers a comprehensive, modular, and controlled exploration of LLM self-improvement, introducing a mathematical formulation governed by the "generation-verification gap." Through experiments across different model families and tasks, the authors identify a scaling phenomenon linked to this gap that scales with model pre-training computational efforts. Additionally, the paper examines conditions under which self-improvement is feasible, proposes an iterative procedure for self-improvement, and suggests methods to enhance its performance. The findings not only deepen the understanding of LLM self-improvement but also open new research possibilities regarding its capabilities and limitations.

### Strengths
1. The research focus of this paper is commendable, as the GV-Gap aids in determining whether a model possesses self-improvement capabilities at any stage (Pre-/Post-training).

2. The overall layout are well-organized.

3. The experiments appear to be extensive and comprehensive. (Respect to Your Hard working)

### Weaknesses
### Deficiencies in Expression

1. The paper lacks a clear definition of the Generation-Verification Gap, with no illustrative diagram and only complex, confusing formulas cluttered with symbols. The core concept of the generation-verification gap (GV-Gap) is not intuitively explained, making it difficult to grasp its significance. The mathematical formulation, while potentially rigorous, is presented in a way that obscures its practical meaning, hindering understanding of how it relates to the model's self-improvement process. A clear, visual representation of the GV-Gap, such as a diagram illustrating the flow of information between the generator and verifier, would greatly enhance the paper's clarity.

2. The authors fail to clearly outline the overall methodological framework or how the experimental process operates. The description of the experimental setup lacks sufficient detail, making it challenging to reproduce the results or understand the underlying mechanisms. It is unclear how the generator and verifier models interact, how the data is filtered, and how the performance is evaluated. The paper needs a more explicit description of the experimental pipeline, including the specific steps involved in generating, verifying, and filtering data. The lack of clarity in the experimental process makes it difficult to assess the validity of the findings.

### Limitations in Contribution

The contributions to the community are relatively weak, as most of the conclusions are already known, such as the "verification gap scales monotonically with the model pre-training flops" and the "Saturation Limit and Cause of Saturation." The observation that the verification gap scales with model size, while empirically supported, does not offer substantial new insights into the underlying mechanisms of self-improvement. Similarly, the saturation limit, where iterative self-improvement plateaus, has been observed in previous studies, and the paper does not provide a novel explanation for this phenomenon. As a purely experimental analysis paper, it does not offer new insights, which is regrettably disappointing.

### Experimental Deficiencies
1. The experiments are primarily based on GSMK8k, which consists only of elementary-level math problems, making the results less convincing. The use of a single, relatively simple dataset limits the generalizability of the findings. The GSM8K dataset, while useful for initial testing, does not represent the full range of challenges that LLMs face in real-world applications. The lack of experiments on more complex and diverse datasets raises concerns about the robustness of the conclusions.
2. In Section 3, the experimental setup has predetermined parameters for lm-evaluation-harness tasks. However, it is unclear why so many hyperparameters would affect the GV-Gap instead of being solely determined by differences between the verifier and the generator. The choice of hyperparameters in the experimental setup is not well-justified, and it is unclear how these parameters affect the observed GV-Gap. The paper does not adequately explain why the GV-Gap is influenced by these parameters rather than solely by the inherent differences between the generator and verifier models. This lack of clarity raises questions about the validity of the experimental results.

### Questions
Please Check Weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work performs an extensive and exhaustive analysis on self-improvement abilities of large language models. First, authors present related work under which the self-improvements capabilities has been studied and formulate a high-level, unified way of representing such framework. Then they propose a novel way of measuring the self-improvement capability using the so called generation-verification gap (GV-gap). Further, they design an experimental setup and provide multiple takeaways that helps to bring the light onto the cases where self-improvement is likely very limited and hypothesize why this might be happening. Finally, authors provided multiple future directions based on their takeaways and findings.

### Strengths
* The proposed measure (gv-gap) is clearly defined with real world examples when it comes to different cases of generators and verifiers. This brings good clarify into the overall presentation.
* The view on self-improvements via the proposed gap brings a new way to quantify the limits of self-improvements, that is a contribution into this research direction and can be used by the research community in future work.

### Weaknesses
 * While the definition of the gv-gap is pretty strict, the real world choice of the utility function making the practical measurements very noisy as authors pointed out in the text (which is great!). They have proposed some ways on improving the verification signal, however, that is a weak point in the entire framework that does not present itself when we just measure the model performance before and after self-improvement steps.
* While I agree that studying base models makes things much easier to handle in paper-size experimental setup, the absence of any signal about the gap changes with instruct based model weakens the provided takeaways. For instance, recent work showed that smaller (8B) instruct models are self-improving very well while in this work there is an opposite signal from the base smaller models that are seemingly lacking reasoning capabilities even under few shot settings.

### Questions
* adding more about the limitations coming from only using the base models would make overall takeaways not weaker, but clearer w.r.t. other recent research in this area.
* overall I think this will be a very useful analysis work for future self-improvement research direction.

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
3

### Summary
The paper provides a mathematical formulation of LLM self-improvement and defines generation-verification gap to measure the potential of self-improvement. Based on the metric, the work conducts extensive experiments in terms of scaling laws, tasks suitable for self-improvement, iterative procedure and better verification attempts.

### Strengths
1. The paper presents a math formulation and a new metric for studying self-improvement, which I believe will be beneficial for current studies related to LLM self-improvement.
2. The experiments are comprehensive, analyzing self-improvement from various perspective.
3. The experimental findings are generally insightful.
4. The paper is well-written and easy to follow.

### Weaknesses
1. My main concern is about the experiment setup. The main experiments are limited to one benchmark, GSM8k, in the math task. Despite GSM8k is a classical benchmark for mathematics, it is relatively easy for current cutting-edge LLMs and its benchmarking function may decrease due to potential data contamination. Additionally, the self-improvement performance as well as the findings may differ across different datasets or scenarios. Therefore, I think it would be beneficial for the authors to complement experiments on more datasets and scenarios, especially those that are more challenging and less likely to have been seen during pre-training. The lack of diversity in the task domain limits the generalizability of the conclusions drawn from the experiments.
2. The defined metric reveals the capability gap between generation and verification. Empirically the metric is useful in predicting potential self-improvement. But it would be more solid if the authors could analyze the correlations between the metric and the actual performance changes after iterations of self-improvement. Specifically, a more rigorous analysis of how the gap correlates with the *magnitude* of performance improvement, not just the presence of improvement, would be valuable. This would provide a more nuanced understanding of the metric's predictive power and its limitations. Experimental evidences and analyses would provide more understanding of the metric and its potential use.

### Questions
1. The findings on "effective diversity of generations" are interesting. Have you conducted further experiments to clarify the underlying causes? For instance, could it be attributed to the training process itself? (Perhaps an experiment involving training on golden labels could provide insights.) Alternatively, could it stem from noise introduced by self-verification? (An experiment to filter out incorrect samples using golden labels or employing stronger evaluators might help determine if this mitigates the issue.)
2. From the main results on scaling law (Figure 1), the scaling laws seem to be severely influenced by the verification methods. Why do some methods (like MC, To) not exhibit such scaling laws? And whether the other methods share similar findings (like CoT-B in the paper and some others)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the self-improvement phenomenon of LLMs. The authors have proposed a mathematical framework to formally discuss the LLM self-improving process, and introduced a well-motivated metric called generation-verification gap (GV-gap) for observation. Linear scaling properties between the GV-gap and pretraining FLOPs are illustrated. The authors have adopted three types of distinct tasks for a comprehensive study of the LLM self-improvement process.

### Strengths
- The authors conducted a timely study on self-improvement of LLMs.

- The proposed mathematical framework about LLM self-improvement is insightful, especially the design of the generation-verification gap (and its relative variant).

- The designed experiments (GSM-8K, NQ, and Sudoku) are representative, as they correspond with the settings of the improvable, the unimprovable, and the "theoretically improvable, but empirical findings show unimprovable".

- The scaling property of GV-gap ~ pretraining FLOPs is a nice read.

### Weaknesses
Please see the Questions below.

### questions:
 - Is the RL update illustrated in Example 2.1 adopted in experiments? 

- Does the **High-fidelity model update** condition mentioned in Section 2.1 examined / verified in experiments？What's the practical benefit for having this condition (principle)?

- Will different decoding algorithms (e.g., search algorithms) for generation help LLMs to (self-)improve? And will the choices of different generation methods alter the conclusions drawn in this paper?

- I like the experiments with Sudoku (Section 4.4), as this is a setting with answer generation strictly harder than verification (NP-hard > P; assuming NP!=P). However, according to the experimental results, non-trivial gaps are observed only with models of > 70B parameters. I wonder if the authors could conduct additional experiments by sweeping the settings of the Sudoku problems: currently it's of 4x4 matrices; how about 3x3, or even 2x2 sized matrices, where the problems should be much easier? With these experiments, can we have the observation that LLMs with different sizes can self-improve?

- Can the authors **use the mathematical framework proposed in Section 2** to provide insights about why the diversity deteriorates with iterative rejection fine-tuning?

- Further thoughts: if diversity deteriorates, do the authors mean that the self-improving process is in fact harmful in some aspect to LLMs, and eventually the self-improvement is just about some kind of tradeoff? What's the authors' opinion on this?

### Questions
- Is the RL update illustrated in Example 2.1 adopted in experiments? 

- Does the **High-fidelity model update** condition mentioned in Section 2.1 examined / verified in experiments？What's the practical benefit for having this condition (principle)?

- Will different decoding algorithms (e.g., search algorithms) for generation help LLMs to (self-)improve? And will the choices of different generation methods alter the conclusions drawn in this paper?

- I like the experiments with Sudoku (Section 4.4), as this is a setting with answer generation strictly harder than verification (NP-hard > P; assuming NP!=P). However, according to the experimental results, non-trivial gaps are observed only with models of > 70B parameters. I wonder if the authors could conduct additional experiments by sweeping the settings of the Sudoku problems: currently it's of 4x4 matrices; how about 3x3, or even 2x2 sized matrices, where the problems should be much easier? With these experiments, can we have the observation that LLMs with different sizes can self-improve?

- Can the authors **use the mathematical framework proposed in Section 2** to provide insights about why the diversity deteriorates with iterative rejection fine-tuning?

- Further thoughts: if diversity deteriorates, do the authors mean that the self-improving process is in fact harmful in some aspect to LLMs, and eventually the self-improvement is just about some kind of tradeoff? What's the authors' opinion on this?

### Soundness
3

### Presentation
3

### Contribution
3
