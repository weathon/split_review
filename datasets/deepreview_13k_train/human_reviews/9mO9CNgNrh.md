# TableTextGrad: A Reflexive Framework for Tabuar Understanding

- Decision: Reject
- Scores: 5, 3, 6, 3

## Abstract
Table understanding is a complex task that requires not only grasping the semantics of free-form questions but also accurately reasoning over semi-structured tables. Recently, promising approaches designed sophisticated prompts that leverage large language models (LLMs) by combining Chain-of-Thought strategies with function calls, consequently demonstrating competitive results without requiring fine-tuning. 
However, creating sufficiently effective prompts remains a challenge. Without fine-tuning, all necessary priors must be incorporated directly into the initial prompt, making prompt design even more critical.
Motivated by the recent advancements in the ''textual gradient'' space, we introduce TableTextGrad, a novel framework that enables automatic prompt optimization by leveraging the ``differentiation'' of prompting pipelines through textual gradients. Concretely, according to the feedback of LLMs, TableTextGrad iteratively refines each function within the Chain-of-Thought steps and function calls, resulting in more accurate and reliable table reasoning outcomes. Experiments on table question-answering datasets demonstrate that our integrated approach achieves significant improvements, setting new state-of-the-art results on the WikiTableQA benchmark. Our TableTextGrad not only enhances the reasoning capabilities of LLMs in the table reasoning task but also lays a groundwork for more robust and generalizable prompting pipelines due to its simplicity and effectiveness.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents TableTextGrad, a framework for table understanding. Motivated by the recent advancements in the “textual gradient” space, this paper introduces TableTextGrad, a novel framework that enables automatic prompt optimization by leveraging the
“differentiation” of prompting pipelines through textual gradients. In the process, an initial LLM (Agent 1) generates table operations iteratively for table understanding. After each step, the table is updated based on the generated function calls and arguments. Then, in the validation phase, a second LLM agent (Agent 2) evaluates the predicted answers. If the answers are incorrect, natural language feedback on how to improve the prompt is backpropagated as textual gradients. These gradients are backpropagated to every prompting step used in generating the answer, including those for function selection, argument generation, and the final table query.  The framework is tested on datasets like WikiTableQA and TabFact and compared with various baseline methods.

### Strengths
This paper adapts the TextGrad technique to the table understanding field, which leverages the Automatic Prompt Updating pipeline, which refines prompts through natural language feedback and gradient updates on training data. The contribution of this paper is simple and easy to understand.

From the experimental results, we observe that this paper demonstrates its ability to significantly improve performance in table question-answering tasks. Leveraging the “differentiation” of prompting pipelines refines each function within the Chain-of-Thought steps and function calls, leading to more accurate and reliable table reasoning outcomes. The results show that it achieves new state-of-the-art performance on benchmarks like WikiTableQA and TabFact, outperforming many existing methods.

### Weaknesses
Although this paper shows its merits in Dynamic Prompt Optimization and Soft Selection of Table Elements, it has some weaknesses that need improvement.

1. The novelty of borrowing the idea of TextGrad to the table understanding domain is limited since the contribution lies in the domain adaptation of the methodology, not belonging to the original contribution from scratch.

2. The performance of TableTextGrad decreases significantly when dealing with large tables. The increased complexity and token context required for large tables seem to lead to issues with memory and attention span within the model. If the authors have considered techniques like table chunking or hierarchical attention mechanisms to address the limitations with large tables.

3. The core reasoning capabilities of TableTextGrad rely on large language models like GPT - 4o and LLaMA 3.1, which are resource-intensive. Also, the improvements over these large models are slight and have not been evaluated with significant tests.

### Questions
Are there any plans to address the limitations of TableTextGrad in future work? For example, how to deal with large tables?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces TableTextGrad, a framework that enhances large language models' ability to reason over tables by automatically optimizing prompts through textual gradients. It combines the flexibility of inference-only techniques with data-driven learning, achieving state-of-the-art results on WikiTableQA and TabFact benchmarks. The approach refines prompts iteratively based on LLM feedback, improving accuracy in table reasoning tasks.

### Strengths
1. The writing is relatively clear. 
2. The model has achieved good performance on two datasets.

### Weaknesses
1. The evaluation datasets are relatively small, with tests conducted on only two datasets, and the evaluation tasks are quite limited. 

2. The authors claim to utilize the textgrad method.  It appears that tab textgrad is merely an application of textgrad.

### Questions
1. Can this method be extended to more table tasks, such as text-to-SQL hybrid table question answering?
2. Can they explain the significant innovations that this method introduces based on textgrad?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a prompt optimisation technique, named TableTextGrad, for the table QA understanding task. Specifically, TableTextGrad uses the *Chain of Table* method as the basis and applies the TextGrad idea to it to automatically optimises the chain of prompts used. 

Evaluation is done on two benchmark datasets: WikiTQ and TabFact, and TableTextGrad achieves the best performance, compared against a number of fine-tuning and inference-only methods.

### Strengths
* Training-free methods are a useful approach to improving LLM performance without having to access their parameters. 

* Table understanding is an interesting and practical task. 

* The proposed technique makes intuitive sense, and shows strong performance.

### Weaknesses
 * The proposed technique is incremental, and the novelty is a bit limited. It essentially applies TextGrad to the *Chain of Table* backbone. While effective, this is not exactly surprising that it works nor groundbreaking.



### Questions
* In Figure 1, what is the right small rectangle in the "Gradient Update Example" part of the figure? What is its relationship with the left rectangle?

* In Sec. 4.2, you mention "the results" in line 396-397. However, I don't see it being referred to in the paper. Thus, in which table/figure are the results shown?

* You discussed training efficiency in Sec. 4.5. However, the discussion is abstract without empirical evidence. I'd like to see a comparison of running time & token consumption/cost against the baselines.

### Soundness
3

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
4

### Summary
This paper introduces *TableTextGrad*, a framework for enhancing table reasoning in LLMs through automated prompt optimization. It refines prompts iteratively using "textual gradients" based on model feedback, improving multi-step reasoning without extensive manual prompt engineering. Key innovations include extending Chain-of-Thought prompting with adaptive prompt adjustments and employing soft selection to retain broader table context, enabling more accurate comprehension in complex table tasks with minimal computational overhead.

### Strengths
1. **Good Motivation for Automated Prompt Optimization**: The paper is well-motivated, highlighting the challenges of manual prompt engineering in table reasoning tasks and effectively positioning automated prompt optimization as a practical solution. The use of "textual gradients" for iterative refinement addresses the need for adaptive prompt tuning in large language models, making the approach both relevant and impactful.

2. **Comprehensive Ablation Study and Analysis**: The paper includes a thorough ablation study, providing valuable insights into the contributions of different components, such as soft versus hard selection and tuning all prompts versus only the final prompt. This detailed analysis strengthens the understanding of TableTextGrad’s performance and demonstrates the robustness and versatility of the proposed method across various model configurations and datasets.

### Weaknesses
1. **Questionable SOTA Claim**: The paper asserts achieving state-of-the-art performance; however, this claim is **not entirely accurate**. According to results in the E5 paper (Table 3) [1], E5 with GPT-4 achieves a score of 88.77 on TabFact, surpassing the 88.75 reported here. This discrepancy **raises concerns about the rigor of this paper's experimental claims** and the reliability of its benchmarking methodology.

2. **Limited Dataset Evaluation**: The evaluation is restricted to only two Table QA datasets (WikiTableQA and TabFact), which may not sufficiently demonstrate the generalization of the approach. Including a more complex and realistic dataset, such as HiTab [2], would provide a more robust assessment of the framework's applicability to diverse, real-world tabular data.

### Questions
See weakness

### Soundness
2

### Presentation
3

### Contribution
2
