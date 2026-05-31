## Human Reviewer 1

### Summary
ATF is a system that turns natural-language math problems into formal Lean 4 statements using feedback tools. It combines **syntax checks** from the Lean compiler and **semantic checks** from multiple LLM judges to iteratively refine results. Trained in three stages, ATF greatly improves both accuracy and consistency over previous models and releases a 750K-sample dataset (**Numina-ATF**) to support further research.

### Strengths
- The proposed framework, ATF, is clearly structured and the experimental results are reported in a generally comprehensible way.  
- The topic itself is timely, and the authors make an effort to connect their work to recent trends in LLM-based reasoning and formal verification.

### Weaknesses
- I want to know what other tool calls, besides the **Syntax Check Tool**, can enhance autoformalization.
I doubt that there are many tools capable of surpassing **Lean** in terms of checking ability, so the paper should explore **Lean’s potential as a tool** more deeply.

- Lean is not good at performing numerical calculations, but I didn’t see you invoke any **calculator-related tools** in your framework.

- Please provide experiments on **benchmarks that require extensive numerical computation**.

### Questions
Please refer to Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
2

### Confidence
5

---

## Human Reviewer 2

### Summary
The paper proposes a model called ATF (Autoformalizer with Tool Feedback), which is designed to translate mathematical problems from natural language into formal statements. To this end, the authors design two types of tool feedback mechanisms: the first uses the Lean 4 compiler to check and correct the syntax of the generated formal statements, ensuring syntactic validity; the second adopts a multi-model voting approach to evaluate the semantic consistency of the generated results. When errors occur in the formalization results, the model can iteratively revise its outputs based on the tool feedback. To train ATF, the authors propose a three-stage training process: first, a “cold start” phase on synthetic data to teach the model how to use tools for correction; then an “expert iteration” phase to further improve the model’s capability through simulated expert feedback; and finally, a Direct Preference Optimization (DPO) phase to reduce ineffective modifications. In the experiments, ATF is evaluated on three mainstream benchmark datasets (FormalMath-Lite, ProverBench, and CombiBench), and the results show that ATF significantly outperforms the current best baseline, Goedel-V2-Formalizer-32B, in both syntactic validity and semantic consistency. The authors also release a synthetic dataset containing 750,000 formal statements (Numina-ATF) and conduct detailed human evaluations and ablation studies to verify the effectiveness of each component. Overall, this work demonstrates a new approach to significantly improve automatic mathematical formalization through tool feedback and provides new data resources.

### Strengths
- High innovation: For the first time, the paper introduces the use of Lean compiler outputs as a syntax verification tool and multi-model collective judgment as a semantic verification tool in the automatic formalization task, effectively combining the strengths of formal systems and large model reasoning.
- Significant experimental results: The proposed method substantially surpasses the current best approach (Goedel-V2-Formalizer-32B) on multiple popular benchmarks, including FormalMath-Lite, ProverBench, and CombiBench, with particularly notable improvements in semantic consistency metrics, demonstrating the effectiveness of the approach.
- Well-designed training process: The proposed three-stage training strategy—cold start, expert iteration, and DPO—progressively optimizes the model for different needs, enabling it to learn how to invoke tools and make reasonable corrections based on feedback, showing a thoughtful and well-structured design.
- Resource contribution: The authors release the Numina-ATF synthetic formalization dataset with 750,000 samples, providing the community with valuable resources for training and evaluation, which holds high practical value.
- Detailed analysis: The paper includes human evaluations and ablation studies, offering in-depth analysis of the roles of each component and the model’s scalability (such as extension effects in the inference stage), enhancing the credibility of the work. The writing is clear, and the figures are easy to read, making the contributions easy to grasp.

### Weaknesses
- Concerns about the reliability of the multi-model consistency tool: The paper relies on multiple large language models as “judges” to determine whether the generated statements are semantically consistent with the problems. However, the judgments made by LLMs may be unstable or biased, especially when it comes to subtle logical errors. Although the authors conducted human evaluations, the error rate and potential blind spots of the consistency checking tool remain unclear. It is recommended to further quantify or add verification mechanisms to ensure the accuracy of consistency feedback.
- Limited generalization ability and scope: The current tool feedback is based on the Lean 4 compiler. If mathematical problems need to be formalized in other languages (such as Isabelle or Coq) or in different versions of Lean, the current approach may not be directly applicable. The authors mention the differences between Lean versions, but there is insufficient study on the adaptability of the method. Future work could explore the method’s transferability across different formal systems or introduce language-agnostic tool interfaces.
- Training and inference overhead: The three-stage training and multi-round feedback mechanisms of ATF increase computational complexity. In particular, during inference, the repeated invocation of the compiler and multi-model judgments may lead to slower inference speed and higher resource consumption. The paper does not discuss efficiency in detail. In practical applications, fast response is also important, and it would be helpful for the authors to specify the model’s inference cost and latency, as well as its performance under limited computational resources.
- Interpretability and failure analysis: Although the paper provides overall performance improvement data, it lacks an in-depth analysis of failure cases. For example, it remains unclear what types of problems ATF still struggles to formalize, or when tool feedback fails to correct the output. A detailed analysis of failure cases would help reveal the limitations of the approach and potential directions for improvement.

### Questions
- The paper mentions using multiple large language models (LLMs) as “judges” for semantic consistency verification. However, I only observed the use of **QWQ-32B** and **Qwen3-32B** in the main text. Could the authors clarify whether these are the only LLMs employed in the consistency check, or if other models were also used but not explicitly mentioned in the paper?
- In Table 1, the results do not appear to show a clear advantage of the *Ensemble Vote* method compared to using a single LLM as the judge. I would recommend adding a new evaluation metric — **Accuracy** — to the table, which would provide a more intuitive comparison and make it easier to quantify the improvement brought by the ensemble voting method.
- Since ATF requires multiple rounds of tool calls for iterative correction during inference, does this lead to a significant computational overhead? How does the actual inference speed compare to conventional one-shot formalization models? Moreover, have the authors considered strategies such as reducing the number of iterations or parallelizing the process to enhance scalability for large-scale mathematical libraries?
- In Section 5.2 (“Tool Analysis”), the paper states: “As shown in Figure 5, the number of tool calls varies by dataset; CombiBench requires the highest average number of tool invocations (8.35) due to its combinatorial complexity, while FormalMath-Lite requires fewer attempts (3.19).”However, I was unable to locate the corresponding values (8.35 and 3.19) in Figure 5. Similarly, the sentence *“ProverBench is an exception where consistency checking (66.34%) outperforms syntax checking (61.65%)”* cites values that also do not appear in the figure. Could the authors verify whether these numbers are accurate or possibly correspond to an earlier version of the figure?
- In Table 4 (ablation study), the improvement brought by adding the DPO training stage over the *Expert Iteration* stage alone appears rather marginal (around 1% increase). Could the authors elaborate on whether the DPO stage provides additional benefits beyond accuracy improvement, such as better stability, generalization, or robustness in handling ambiguous formalization cases?
- The experiments report strong results on **FormalMath-Lite**, **ProverBench**, and **CombiBench**. However, other widely used benchmarks for formalization tasks include **MiniF2F** and **ProofNet**. Could the authors share any results or observations on these datasets, or discuss potential challenges in applying ATF to them?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper presents Autoformalizer with Tool Feedback (ATF), a framework that integrates Lean 4 compiler feedback and multi-LLM semantic evaluation to improve mathematical autoformalization. Through three-stage training—cold start, expert iteration, and DPO—ATF learns effective tool usage and revision strategies. Experiments on FormalMath-Lite, ProverBench, and CombiBench show significant gains over prior systems like Goedel-V2 and StepFun-Formalizer, particularly in semantic consistency.

### Strengths
1. The paper clearly identifies two key bottlenecks in current autoformalization models—syntactic errors and semantic drift—and systematically addresses both through tool feedback.
2. The experiments show substantial improvements in syntactic validity and semantic consistency, further validated by human evaluation, demonstrating a strong correlation with human judgment.
3. The system is thoughtfully designed, featuring grouped execution and expert iteration mechanisms that enable efficient syntax checking and progressive tool learning.
4. The paper is well-written and comprehensive, with detailed appendices and clear figures that effectively illustrate the model’s iterative reasoning and tool interaction process.

### Weaknesses
1. The paper introduces a meaningful but moderately novel approach by systematizing tool feedback specifically for autoformalization
2. Training and evaluation datasets are all derived from the Numina ecosystem; although similarity-based decontamination (cosine < 0.8) is performed, stronger guarantees against overlap would make the results more convincing. Include one external dataset (e.g., MiniF2F or PutnamBench) or a stricter decontamination threshold.

### Questions
Please refer to the Weakness section.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
2