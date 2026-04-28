# MeteoRA: Multiple-tasks Embedded LoRA for Large Language Models

- Decision: Accept
- Avg Score: 6.20
- Scores: 8, 5, 6, 6, 6

## Abstract
The \textit{pretrain+fine-tune} paradigm is foundational for deploying large language models (LLMs) across various downstream applications. Within this framework, Low-Rank Adaptation (LoRA) stands out for its parameter-efficient fine-tuning (PEFT), producing numerous reusable task-specific LoRA adapters. However, this approach requires explicit task intention selection, posing challenges for autonomous task sensing and switching during inference with multiple existing LoRA adapters embedded in a single LLM.
In this work, we introduce \textbf{\method} (\textbf{M}ultipl\textbf{e}-\textbf{t}asks \textbf{e}mbedded L\textbf{oRA}), a scalable and efficient framework that reuses multiple task-specific LoRA adapters into the base LLM via a full-mode Mixture-of-Experts (MoE) architecture.
This framework also includes novel MoE forward acceleration strategies to address the efficiency challenges of traditional MoE implementations.
Our evaluation, using the LlaMA2-13B and LlaMA3-8B base models equipped with 28 existing LoRA adapters through \method, demonstrates equivalent performance with the traditional PEFT method. Moreover, the LLM equipped with \method\ achieves superior performance in handling composite tasks, effectively solving ten sequential problems in a single inference pass, thereby demonstrating the framework's enhanced capability for timely adapter switching.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces MeteoRA, which automatically applies the appropriate LoRA adapters to a pre-trained LLM based on the current task.
MeteoRA is an MoE-inspired approach in which a gating function selects the top-k LoRA adapters for each token in each input sequence.
The authors demonstrate that MeteoRA performs similarly to an LLM with a handpicked, in-domain LoRA adapter, and provide an efficient
kernel implementation that addresses runtime concerns and memory overhead.

### Strengths
1. MeteoRA is a general approach to incorporate domain-specific knowledge from multiple LoRAs in a single model.
2. Extensive evaluation which demonstrates that MeteoRA performs similarly to the PEFT reference implementation, which provides a reasonable upper-bound reference.
3. The authors explain concerns about runtime and memory-efficiency. Based on this, the authors design, implement, and evaluate a CUDA kernel which addresses the concerns.

### Weaknesses
1. All LoRAs are stored in GPU memory, which limits the scalability of the approach. In contrast, S-LoRA (a LoRA serving system) scales to thousands of LoRA adapters by swapping LoRA weights to host memory. Proposing a target range for the # of LoRA adapters or a method to swap adapters to host memory could help address this concern. The current implementation requires all LoRA parameters to reside in GPU memory, which becomes a significant bottleneck as the number of adapters increases. This limits the practical application of MeteoRA in scenarios requiring a large number of specialized adapters. A more detailed analysis of the memory footprint with respect to the number of LoRAs and the base model size would be beneficial. 
2. MeteoRA model is fine-tuned on a set of LoRAs and their target domains. Consequently, the approach does not efficiently integrate new LoRA adapters. The fine-tuning process for MeteoRA requires a predefined set of LoRA adapters and their corresponding tasks. This makes it difficult to incorporate new adapters without retraining the entire model, limiting its adaptability to evolving task requirements. A discussion of the computational cost associated with adding new LoRA adapters would be valuable.
3. Capability regression with $k=2$ indicates that LoRA adapters likely interfere with one another. Some discussion of how to mitigate interference or exploit $k=1$ for further speedups could address this weakness. The observed performance degradation when using $k=2$ suggests that the selected LoRA adapters may not always be complementary, leading to interference. Further investigation into the mechanisms causing this interference and potential mitigation strategies, such as regularization techniques or more sophisticated gating mechanisms, is needed. Exploring the trade-offs between performance and speed when using $k=1$ could also be beneficial.
4. On a few tasks, MeteoRA performs worse than the baselines (e.g., NewsIT, CNNDM, and TrackObj). An explanation of why this might be the case could help contextualize these results. The fact that MeteoRA underperforms compared to baselines on certain tasks raises concerns about its robustness across diverse tasks. A more detailed analysis of these specific tasks, including the characteristics of the datasets and the nature of the tasks themselves, could help identify the reasons for the performance drop. It would also be useful to explore whether these tasks have specific requirements that are not well-addressed by the current approach.
5. No evaluation on how MeteoRA scales to larger batch sizes. It would be interesting to see the relationship between batch size and runtime/memory because larger batch sizes would access more adapters which could impact these metrics. The lack of evaluation on the impact of batch size on runtime and memory usage is a significant limitation. As batch size increases, the number of LoRA adapters accessed simultaneously may also increase, potentially leading to performance bottlenecks. A detailed analysis of the relationship between batch size, runtime, and memory consumption is necessary to assess the scalability of MeteoRA in practical scenarios.

### Questions
**Questions**
1. How does MeteoRA perform on out-of-distribution tasks (e.g., compared to baselines such as the base LLM, LoRA-F, and LoRA-B)?
2. In section 3.3, what is $p_i$?
3. For measuring forward-pass speed, what is the batch size?

**Suggestions**
1. Introduction should quantify benefit of MeteoRA beyond speedup (e.g., average accuracy increase).
2. Fig 1: unclear where the MoE is located, and how experts are selected.
3. Background: should cite other MoE-based LLMs, such as GLaM (preceded Mixtral), DBRX, and Grok.
4. Section 3.3 needs more revisions for clarity. While I appreciate the explanation to motivate the kernel design, it took several reads to fully understand the problem with the `loop-original` method, why it is 10x slower, and how `bmm-torch` works.
5. Figure 8 is hard to interpret. The font size is small and the colors/lines are difficult to distinguish due to small line width and shading. Such a key figure should be better-presented (i.e., bigger, clearer lines, easier to read).
6. Figure 5: root-of-runtime is a strange (and potentially misnamed) evaluation metric. It would be better to report runtime directly.

### Soundness
4

### Presentation
2

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
This paper presents MeteoRA, a framework combining MoE and LoRA to enhance inference efficiency via forward acceleration. It analyzes PEFT methods related to user tasks, integrating multiple LoRA adapters for new tokens and identifying the top-k experts for processing. The authors introduce a batched matrix multiplication (bmm-torch) strategy to enable parallel processing of LoRAs, improving speed and efficiency over sequential methods. In summary, by merging MoE and bmm-torch, MeteoRA significantly accelerates token processing and enhances operational efficiency.

### Strengths
MeteoRA effectively implements a scalable integration of LoRA while adopting forward acceleration techniques during the inference phase, thereby enhancing the efficiency of the inference process.

### Weaknesses
 - The paper is not very novel, given that using MoE for LoRA is an idea that has already been extensively explored [1,2,3]. It would be beneficial to clearly delineate how MeteoRA compares to and differs from the referenced LoRAMoE works.

- The term "reuse existing LoRA" is misleading and unclear; it implies the need for offline training and does not introduce any innovation compared to other MoE methods.

- While the bmm-torch method for parallel processing of LoRA adapters improves forward training, it may increase memory consumption. This approach requires larger memory allocations for concurrent processing, potentially offsetting time savings from reduced sequential processing. Please provide quantitative comparisons of memory usage and speed gains across different batch sizes or sequence lengths to clarify this trade-off.


- MeteoRA is presented as an advancement over existing LoRA techniques, a direct comparison with LoRA MoE methods is missing. Such a comparison could underscore the performance superiority of the proposed method. Could the authors conduct and present a detailed comparative analysis with LoRA MoE [1,2,3] methods?

Minior: 

-The font size in Figure 3 is too small to read.

### Questions
The b$\times$s tokens are treated as independent. However, there is concern about potential correlations among tokens. Knowledge across domains can be interrelated, and sentence meaning may depend on context. How do the authors address this issue? Could the assumption of independence negatively affect performance by ignoring relevant interdependencies?

### Soundness
2

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
3

### Summary
The paper introduces MeteoRA, a framework designed to enhance the deployment of multiple LoRA adapters in LLM through a Mixture-of-Experts (MoE) architecture. This approach aims to facilitate autonomous task sensing and dynamic adapter switching, improving efficiency in handling composite tasks.

### Strengths
- The use of a full-mode MoE architecture to integrate multiple LoRA adapters is a novel contribution, potentially addressing limitations in existing methods like Huggingface PEFT and S-LoRA.
- The proposed forward acceleration strategies address efficiency challenges in traditional MoE implementations, achieving significant speedups.

### Weaknesses
 - It will be better to also compare with a model trained with MoE upcycling and discuss the benefit of the proposed method.
- It should be a more detailed analysis of the triton operator, how it differ from methods like S-LoRA.
- The legend in Figure 3 is too small

### Questions
See weakness

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
2

### Summary
This paper proposes MeteoRA to enable scalable multi-task LoRA embedding within LLMs. The key of MeteoRA is using gated MoE to automatically select the most pertinent LoRA adapters to generate appropriate responses. It also employs efficient GPU kernel operators for forward acceleration. Evaluation results show the effectiveness of MeteoRA.

### Strengths
+ Using gated MoE for automatic selection of LoRA adapters
+ Employing efficient GPU kernel operators for forward acceleration

### Weaknesses
 - Re-training is required when some LoRA adapters are updated, making it hard to use in practice

### Questions
How to reduce the re-training costs when some LoRA adapters are updated? How many LoRA adapters can be supported by MeteoRA?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose an automatic selection model for multi-task LoRA using a MoE arch, supporting both top-1 and top-k selection methods. In addition to constructing an automatic selection process using Gate Logits, they also utilize PyTorch's bmm operator for forward acceleration. The authors demonstrate the effectiveness of their proposed algorithm across multiple tasks by comparing it with existing multi-task LoRA methods as well as their own baselines, LoRA-F and LoRA-B.

### Strengths
### Originality
Since the gate logits approach is primarily inspired by methods from Mixtral of Experts, the main novelty lies in the design of the loss function and the implementation of forward acceleration. This method can solve up to ten sequential problems in a single inference pass automatically, which demonstrates both the scalability and utility of the proposed solution.

### Quality
The technical details appear correct, as the paper does not involve extensive mathematical derivations. The authors also introduce efficient acceleration strategies for MoE, which contribute meaningfully to improving the computational feasibility of such models.

### Clarity
The paper is generally clear in presenting the proposed methodology and results.

### Significance
The work addresses a significant challenge in the field of parameter-efficient fine-tuning (PEFT) by proposing a novel approach to autonomously manage and switch between multiple LoRA adapters embedded within a single LLM. The proposed framework is of considerable practical value for large-scale language models and downstream applications. The emphasis on practical deployment of the framework and the specific use of LoRA in a multi-task setting distinguishes this work from previous studies.

### Weaknesses
### Originality
The gate logits approach is primarily inspired by methods from Mixtral of Experts, and the paper could more clearly emphasize its origin and what it is (just a linear layer with softmax). The novelty is primarily in the loss function design and forward acceleration, which, while valuable, might not be substantial enough to warrant a high originality score. The paper should explicitly acknowledge the use of a standard softmax gating mechanism and focus on highlighting the specific modifications and contributions made on top of this established technique.

### Clarity
The description of the gating network is insufficient. The paper lacks details on the specific architecture of the gating network, such as the number of layers, hidden dimensions, and activation functions used. More details on the construction of composite-3/5/10 tasks should also be provided in the main text, including the specific criteria used for selecting tasks and how the questions are concatenated. The motivation behind using a composite task is not clearly explained, and the paper should include a more detailed justification for this design choice. The paper would benefit from a more thorough explanation of why this particular approach is advantageous compared to other multi-task learning strategies.

### Writing Quality
The LaTeX formatting should be unified, such as using consistent notation for $o_{base}$ and $W_\mathrm{base}$ in Equation (2). Additionally, consistent notation should be used in the formulas (e.g., whether the vectors are row or column vectors, and whether matrices operate on vectors from the left or the right). For instance, in Equation (2), the expression $o = xW_\mathrm{base} + x\Delta W_{I(x)}$ is used, while in Appendix A, $h = W_\mathrm{base}x + B_iA_ix$ is used. This inconsistency makes it difficult to follow the mathematical formulations and understand the exact implementation details.

### Questions
1. In the appendix, the authors mention, "However, given the limited capability of the instruction following in the zero-shot setting, neither the MeteoRA models nor the models fine-tuned by LoRA achieve satisfactory results." Is there any supporting evidence for this statement? Also, why did the authors ultimately choose a 2-shot setting?
2. According to Figure 3, MeteoRA's performance on the ParaSeg task is noticeably poor when using LlaMA2, but it shows significant improvement with LlaMA3. Could the authors provide an explanation for this?

### Soundness
3

### Presentation
3

### Contribution
2
