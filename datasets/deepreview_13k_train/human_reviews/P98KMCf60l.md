# Theoretical Insights into Fine-Tuning Attention Mechanism: Generalization and Optimization

- Decision: Reject
- Scores: 5, 6, 5, 3

## Abstract
Large Language Models (LLMs), built on Transformer architectures, exhibit remarkable generalization across a wide range of tasks. However, fine-tuning these models for specific tasks remains resource-intensive due to their extensive parameterization. In this paper, we investigate two remarkable phenomena observed during the fine-tuning of LLMs, particularly focusing on the attention mechanism: (1) Different Impact, optimizing the $\mathbf{W}_v$ matrix significantly improves performance over optimizing the $\mathbf{W}_k$ matrix. Fine-tuning only the $\mathbf{W}_q$ and $\mathbf{W}_v$ matrices is computationally efficient, delivering results that are comparable to, or even better than, fine-tuning all three matrices $\mathbf{W}_q$, $\mathbf{W}_k$, and $\mathbf{W}_v$. (2) Efficient Convergence, employing distinct learning rates for these matrices is crucial for optimal performance, with a higher learning rate for the $\mathbf{W}_v$ matrix expediting convergence. However, theoretical analyses of these phenomena are still relatively limited. We present a theoretical analysis of these phenomena from two perspectives: (i) Generalization, where we demonstrate that fine-tuning only $\mathbf{W}_q$ and $\mathbf{W}_v$ improves generalization bounds, enhances memory efficiency, and (ii) Optimization, where we emphasize that the feature learning of the attention mechanism is efficient, particularly when using distinct learning rates for the matrices, which leads to more effective fine-tuning. Building on these insights, we propose a new strategy that improves fine-tuning efficiency in terms of both storage and time. Experimental results on benchmark datasets validate the effectiveness of this approach, supporting our theoretical findings. Our analysis lays the theoretical groundwork for configuring and improving lightweight algorithms in LLMs fine-tuning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates and addresses the resource-intensive nature of fine-tuning Large Language Models (LLMs) on transformer architectures, focusing specifically on the attention mechanism. The study identifies two key phenomena:

1. **Different Impact**: The research demonstrates that optimizing the value matrix (Wv) in the attention mechanism leads to better performance improvements than optimizing the key matrix (Wk). Moreover, fine-tuning just the query (Wq) and value (Wv) matrices—not only reduces computational demands but also yields results that are on par with or surpass full matrix optimization (including Wq, Wk, Wv).

2. **Efficient Convergence**: The paper highlights the importance of employing distinct learning rates for different matrices, particularly using a higher learning rate for Wv to speed up the convergence process.

The contributions of the paper are both theoretical and practical. Theoretically, it offers a new analysis on how selective fine-tuning of the attention matrices can enhance generalization bounds and improve memory efficiency. Practically, it proposes a fine-tuning strategy that optimizes model training time and resource use. The effectiveness of this approach is supported by experimental results on benchmark datasets, which validate the proposed methods and lay the groundwork for developing more efficient algorithms for fine-tuning LLMs.

### Strengths
- **Importance of Understanding Attention Mechanisms During Fine-Tuning**: The challenge of gaining a deeper understanding of the attention mechanism during fine-tuning is a critical one. The approach developed in this paper has the potential to serve as a plug-and-play solution for achieving improved accuracy-efficiency trade-offs in LLM fine-tuning.

- **Empirical and Theoretical Contributions**: This paper offers both empirical and theoretical analyses to elucidate the behavior of the attention mechanism during fine-tuning. The insights provided here could make a valuable contribution to the field, supporting the development of enhanced fine-tuning techniques that optimize the accuracy-efficiency trade-off.

### Weaknesses
 - **Generalizability of the Proposed Approach**: The primary concern is the generalizability of the proposed approach. Specifically, the authors could enhance the analysis by demonstrating that the proposed method consistently improves LLM performance across diverse scenarios. To this end, it would be beneficial to include performance results under more complex, open-ended generation tasks, such as MT-Bench or comparable challenging benchmarks. Additionally, considering variations in model behavior, evaluating the approach on a broader range of LLMs, such as Mistral, would further strengthen the claim of general applicability.

- **Visualization for Better Insight**: To deepen the analysis and understanding of the findings, visualizing the learned attention distributions across different settings could be valuable. By examining how attention distributions vary under different configurations, the authors could offer a more nuanced understanding of the observed effects, shedding light on the underlying phenomenon.

### Questions
- How will the proposed method perform on other PEFT techniques, such as DoRA [1]?

[1] Liu, Shih-Yang, et al. "Dora: Weight-decomposed low-rank adaptation." arXiv preprint arXiv:2402.09353 (2024).

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
3

### Summary
This paper presents theoretical and empirical insights into improving the efficiency of fine-tuning large language models. The key contributions are as follows:

1. Different Impact in Fine-Tuning: The paper demonstrates that fine-tuning only the value (`Wv`) and query (`Wq`) matrices of the attention mechanism is computationally efficient and can yield results comparable to or better than fine-tuning all three matrices (`Wq`, `Wk`, `Wv`). It suggests that `Wv` has a significantly greater impact on performance compared to `Wk`.

2. Efficient Convergence: The authors show that using distinct learning rates for different matrices, particularly a higher rate for `Wv`, expedites convergence and optimizes the fine-tuning process. This insight provides a practical approach to achieving better fine-tuning results with fewer computational resources.

3. Theoretical Analysis: The paper provides a theoretical analysis from the perspectives of generalization and optimization. It establishes that fine-tuning `Wq` and `Wv` enhances memory efficiency and generalization bounds while optimizing convergence dynamics by accelerating learning for specific matrices.

4. Proposed Strategy: Building on these insights, the authors propose a strategy to improve fine-tuning efficiency, both in terms of storage and time. Experimental results on benchmark datasets validate the effectiveness of this approach.

### Strengths
- Originality: The originality of this paper lies in its focused approach to fine-tuning the attention mechanism of large language models. By exploring the selective fine-tuning of `Wv` and `Wq` matrices, the authors introduce a novel method that challenges the conventional approach of fine-tuning all attention matrices (`Wq`, `Wk`, `Wv`). The theoretical insights into the distinct roles of these matrices, combined with empirical validation, provide a fresh perspective on optimizing the attention mechanism. Additionally, the proposed use of differentiated learning rates for convergence further demonstrates creativity in enhancing the fine-tuning process.

- Quality: The quality of the paper is reflected in its theoretical analysis and empirical validation. The authors employ both information-theoretic methods and optimization theory to support their claims, which significantly strengthens the credibility of their contributions.

- Clarity: The paper is generally well-written, making the complex ideas accessible to a broad audience. 

- Significance: The significance of the paper lies in its potential to influence future research and practical implementations of fine-tuning large language models. This contribution is highly relevant for both academia and industry, as it provides a more resource-efficient approach to adapting pre-trained models for downstream tasks.

### Weaknesses
1. **Lack of Base Model Performance for Each Task**: The paper does not provide the performance of the base model before fine-tuning for each task, making it challenging to evaluate the true effectiveness of the fine-tuning methods. Including these baseline results would help contextualize the improvements made through fine-tuning. Without these baselines, it's impossible to determine if the reported gains are significant or merely reflect the model's inherent capabilities on the tasks.

2. **GLUE Evaluation Is Too Simple for LLaMA3.1-8B**: The use of the GLUE benchmark to evaluate the LLaMA3.1-8B model is insufficient, as GLUE tasks are relatively simple compared to the capabilities of such a large model. Evaluating on more challenging tasks, such as coding or mathematical problem, could make the results more convincing and demonstrate the robustness of the proposed approach. The GLUE benchmark may not fully capture the nuances of the model's performance, especially for a model of this scale.

3. **Lack of Ablation Studies**: The paper could benefit from more extensive ablation studies to isolate the effects of different components of the proposed method, such as the impact of learning rate scaling and the specific contribution of each matrix (`Wq`, `Wv`). This would provide a clearer understanding of the factors contributing to the observed performance gains. For example, it is unclear if the performance improvement is primarily due to the higher learning rate for `Wv` or the selective fine-tuning of `Wq` and `Wv`.

4. **Lack of Guidance on Hyperparameter `λ`**: The paper does not provide sufficient guidance on how to choose the hyperparameter `λ`, which controls the relative learning rates of different matrices. Without explicit guidelines or a heuristic for selecting `λ`, practitioners may find it difficult to replicate the reported results or apply the method effectively in different contexts. The lack of a clear strategy for setting `λ` limits the practical applicability of the proposed method.

### Questions
1. **Baseline Performance**: Could you provide the performance metrics of the base model before fine-tuning for each of the tasks? This would help in better understanding the relative improvements brought by your fine-tuning strategy.

2. **More Challenging Evaluations**: Have you considered evaluating the LLaMA3.1-8B model on more complex benchmarks, such as tasks involving coding or mathematical problem? Including such challenging tasks would make your results more comprehensive and convincing.

3. **Ablation Studies**: It would be helpful if you could add more ablation studies to isolate the effects of different components of the proposed method, such as the specific impact of `Wq` vs. `Wv` fine-tuning or the effect of learning rate scaling. This would provide a clearer picture of what drives the observed improvements.

4. **Hyperparamete `λ`**: Could you provide more guidance on how to choose the hyperparameter `λ`?

### Soundness
3

### Presentation
2

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
This paper explores fine-tuning strategies for the attention mechanism from a theoretical perspective, focusing on generalization and optimization issues, and claims to provide theoretical insights to guide algorithm design. It has two major propositions, one is fine-tuning WqWv matrix is more efficient and can achieve comparable results as fine-tuning WqWkWv matrix. Another is fine-tuning Wq and Wv should use different learning rates for more efficient convergence.

### Strengths
The idea of using different local learning rates for Wq and Wv is interesting. As V is timed with attention logits, q and v should have more different gradient distributions than q and k. Using different local learning rates for these two types of matrices is reasonable and worth exploring.

### Weaknesses
1. The writing and presentation are rather poor. Both sentence level and logical level polishment are suggested for this work. 
    E.g. In line 16~22, "In this paper, we investigate two remarkable phenomena ... with a higher learning rate for the Wv matrix expediting convergence." The ordering of the sentences and the way of structuring the arguments add unnecessary difficulty to reading. This kind of problem happens across the whole manuscript.
    A suggestion is, use multiple statement sentences instead of clauses. A rewritten version of these sentences is " In this paper, we investigate two remarkable phenomena associated with attention mechanism, during the fine-tuning of LLMs. One is 'Different Impact' and another is 'Efficient Convergence'. ......". Another point is that the naming of "Different Impact" and "Efficient Convergence" doesn't help with understanding. Consider other ways to name them.

2. For the "Different Impact", the authors claimed that fine-tuning Wq&Wv is favored over Wq,Wk,Wv together. However, this argument is not supported by their experimental results in Table 1. It can be seen from the table that fine-tuning Wq,Wk,Wv together still gets the best performance for most of the cases. I wonder if the authors are writing the arguments and conducting experiments separately without any discussion. The authors should summarize their findings according to the experiment results.

### Questions
1.  In line 160~193, the author writes "As seen in the table, we can see a clear trend where solely updating the Wv matrix outperforms just learning the Wq,Wk matrix. Interestingly, the combination of fine-tuning both Wq and Wv often leads to performance that matches or even exceeds that achieved by fine-tuning all three matrices Wq,Wk, and Wv". This statement is not supported by the results in Table 1, as solely updating the Wv is inferior to updating Wq,Wk together, and fine-tuning all three matrices Wq,Wk, and Wv achieves the best result in most cases. The authors should first rewrite the whole section of "Different Impact" to have a consistent argument with the experiment results, and investigate more tasks to see whether there are certain types of tasks in which "different impact" is true.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper investigates two phenomena observed during the fine-tuning of Transformer LLMs, focusing on the attention mechanism. The first phenomenon is the "Different Impact," where optimizing the Wv (value) matrix significantly improves performance more than optimizing the Wk (key) matrix. The second is "Efficient Convergence," where using distinct learning rates for different matrices is crucial for optimal performance, with a higher learning rate for Wv being beneficial for faster convergence. The paper provides theoretical analysis on these phenomena from the perspectives of generalization and optimization. Based on this, this paper proposes only finetuning Wq and Wv, and with a larger learning rate for Wv.

### Strengths
The observation that fine-tuning only Wq and Wv​ matrices yields performance gains comparable to finetuning of Wq, Wk and Wv is interesting. Trying to analyze and uncover the reason can benefit the research commnity.

### Weaknesses
My biggest concern with this paper is that the key observation seems to originate from the LoRA paper: *"Adapting both \( W_q \) and \( W_v \) gives the best performance overall"* (this sentence is quoted from the LoRA paper), and even the experiment setup is similar to Table 5 in the LoRA paper. Deriving key observations from other works isn’t an issue (or saying we share the same observation/insights), but I believe it should be directly and explicitly pointed out, rather than presented as your own observation, concerning the lora paper is very famous for several years and you do cite it. Or could you clarify what differences there are between your work and the LoRA paper? Please provide a detailed comparison between their findings and those in the LoRA paper, highlighting any novel contributions or deeper insights their work provides. This would help clarify the paper's originality and contribution to the field.

As you pointed out on line 205, \( W_q \) and \( W_k \) can be treated as a single unit. In linear algebra, two matrices multiplied without an intermediate activation can be equivalent to a single matrix. This could explain why fine-tuning only \( W_q \) and \( W_v \) achieves comparable accuracy to tuning all matrices. If this is the case, have you tried fine-tuning only \( W_k \) and \( W_v \)? It seems that neither the LoRA paper nor your work has conducted this experiment. Could you please include this experiment in your study or explain why not to perform it. This could provide valuable insights and strengthen the paper's analysis.

What are the main conclusions of the theoretical analyses in Sections 3 and 4? I found it difficult to follow your proofs. Please include a clear summary of the main conclusions from their theoretical analyses at the end of Sections 3 and 4. I would suggest to provide more intuitive explanations to help readers better understand the theoretical analyses and proofs.

Section 5 appears to be simply fine-tuning \( W_q \) and \( W_v \) with a search for \lambda. Do you have any insights on how to determine \lambda? could you provide guidelines or heuristics for determining an appropriate \lambda value based on your theoretical and empirical results?

### Questions
1. My biggest concern with this paper is that the key observation seems to originate from the LoRA paper: *"Adapting both \( W_q \) and \( W_v \) gives the best performance overall"* (this sentence is quoted from the LoRA paper), and even the experiment setup is similar to Table 5 in the LoRA paper. Deriving key observations from other works isn’t an issue (or saying we share the same observation/insights), but I believe it should be directly and explicitly pointed out, rather than presented as your own observation, concerning the lora paper is very famous for several years and you do cite it. Or could you clarify what differences there are between your work and the LoRA paper? Please provide a detailed comparison between their findings and those in the LoRA paper, highlighting any novel contributions or deeper insights their work provides. This would help clarify the paper's originality and contribution to the field.

2. As you pointed out on line 205, \( W_q \) and \( W_k \) can be treated as a single unit. In linear algebra, two matrices multiplied without an intermediate activation can be equivalent to a single matrix. This could explain why fine-tuning only \( W_q \) and \( W_v \) achieves comparable accuracy to tuning all matrices. If this is the case, have you tried fine-tuning only \( W_k \) and \( W_v \)? It seems that neither the LoRA paper nor your work has conducted this experiment. Could you please include this experiment in your study or explain why not to perform it. This could provide valuable insights and strengthen the paper's analysis.

3. What are the main conclusions of the theoretical analyses in Sections 3 and 4? I found it difficult to follow your proofs. Please include a clear summary of the main conclusions from their theoretical analyses at the end of Sections 3 and 4. I would suggest to provide more intuitive explanations to help readers better understand the theoretical analyses and proofs.

4. Section 5 appears to be simply fine-tuning \( W_q \) and \( W_v \) with a search for \lambda. Do you have any insights on how to determine \lambda? could you provide guidelines or heuristics for determining an appropriate \lambda value based on your theoretical and empirical results?

### Soundness
1

### Presentation
2

### Contribution
2
