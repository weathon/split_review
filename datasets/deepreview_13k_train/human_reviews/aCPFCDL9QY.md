# Self-Updatable Large Language Models with Parameter Integration

- Decision: Accept
- Scores: 6, 6, 6, 5

## Abstract
Despite significant advancements in large language models (LLMs), the rapid and frequent integration of small-scale experiences, such as interactions with surrounding objects, remains a substantial challenge. Two critical factors in assimilating these experiences are (1) \textbf{Efficacy}: the ability to accurately remember recent events; (2) \textbf{Retention}: the capacity to recall long-past experiences. Current methods either embed experiences within model parameters using continual learning, model editing, or knowledge distillation techniques, which often struggle with rapid updates and complex interactions, or rely on external storage to achieve long-term retention, thereby increasing storage requirements.
In this paper, we propose \textbf{\ours} (Self-Updatable Large Language Models with Parameter Integration). \ours requires no extra parameters while ensuring near-optimal efficacy and long-term retention.
Our method employs a training objective that minimizes the Kullback-Leibler (KL) divergence between the predictions of an original model (with access to contextual information) and a target model (without such access). By generating diverse question-answer pairs related to the knowledge and minimizing the KL divergence across this dataset, we update the target model to internalize the knowledge seamlessly within its parameters.
Evaluations on question-answering and conversational recommendation tasks demonstrate that \ours significantly outperforms existing methods, even when accounting for non-zero storage requirements. This advancement paves the way for more efficient and scalable integration of experiences in large language models by embedding knowledge directly into model parameters.
\vspace{-5pt}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces SELF-PARAM, a novel method for updating LLMs with new knowledge without requiring additional storage parameters. The key insight is using KL divergence minimization between models with and without context access to embed knowledge directly into model parameters. Through comprehensive experiments across various injection scenarios and a practical demonstration on conversational recommendation tasks, the authors show SELF-PARAM outperforms existing methods while maintaining zero storage overhead - effectively solving the challenge of efficient knowledge integration in LLMs.

### Strengths
1. The writing of the paper is clear and easy to follow and understand.
2. The paper proposes a novel and elegant solution to knowledge injection in LLMs by using KL divergence minimization - it's technically sound while being simple. The zero additional storage requirement is a plus compared to existing methods that need external memory or retrieval modules.
3. The empirical evaluation is overall comprehensive and convincing. The authors tested their method across multiple dimensions (single/batch/sequential injection) and backed up their claims with solid results.

### Weaknesses
1. The computing cost is significantly larger for the proposed method compared to next-token-prediction fine-tuning. For one query, it has to run the base model twice to get the two corresponding probability distributions. This paper only discusses the space complexity. The comparison of time complexity is also worth discussing. Specifically, the paper should detail the exact computational overhead, including the number of forward and backward passes required for both the proposed method and standard fine-tuning. Furthermore, a breakdown of the time spent on each step (e.g., KL divergence calculation, gradient computation) would be beneficial to understand the bottlenecks of the proposed method.
2. In the experiment setting, this method utilizes two popular dense retrieval (DPR) and spare retrieval (BM25) methods as baselines. However, these two methods are a little bit too old to be considered as the baselines. Using a stronger retrieval model, such as [1][2], will better demonstrate the superiority of the proposed method. It would be more convincing to compare against state-of-the-art retrieval methods that incorporate more recent advancements in areas like contrastive learning and weakly-supervised pre-training. The current baselines might not fully capture the potential of retrieval-augmented methods, making it difficult to assess the true advantage of the proposed approach.

### Questions
1. I found the term self-updating very confusing here. This up-updating method requires (1) an extra training process to update the parameters and (2) an extra instruct model (GPT-4o-mini) to construct the training data. I think the authors could provide more insight into how to understand self-updating.
2. Retention is discussed in the introduction but not mentioned in the experiments. I wonder how the authors evaluate the aspects of retention performance. 
3. An ablation study is missing from this paper; there are multiple techniques (KL-div, diverse instructions construction...) introduced in this method, and how each one contributes to the final result should be investigated and compared. At least, some discussion should be included.

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
3

### Summary
The authors propose a method to inject context information into LLMs on-the-fly, with two criteria: being able to effectively use the injected the context (efficacy), and retain context information for a long time, as more additional information is added (retention).
The method involves two key steps:

1. An external LLM is used to augment the given context information by generating relevant question-answer pairs.
2. The base LLM is fine-tuned on the question-answer pairs, using KL-divergence.
Notably, the base LLM is fine-tuned such that $P(A_{i} | Q, A_{0, ..., i-1})$ follows $P(A_{i} | C, Q, A_{0, ..., i-1})$. I.e., the LLM is trained to answer the plain question (where the context had *not been* given), as if the context *had been* given.

The authors evaluate the method under three settings:

1. Single context injection: inject a single piece of context information and evaluate on a held-out question.
2. Batch context injection: inject a batch (100 to 500 pieces) of context information and evaluate on held-out questions.
3. Sequential injection: inject contexts 0 to i and evaluate on question for context i (for i in 0 ... 20).

The authors compare with the following baselines:

1. prompting with the relevant context (upper-bound)
2. fine-tuning on the context itself
3. LLMs with external memory
4. infinite-context methods (InfLLM)
5. RAG methods

The proposed method outperforms all previous methods (2–5), often by a wide margin.

### Strengths
1. The method substantially outperforms previous methods.
1. The method is empirically validated on three evaluation settings, across three base LLMs, comparing with many baseline methods.
1. The writing is easy to follow and the experiment results are presented clearly.

### Weaknesses
1. **The requirement of an external teacher LLM is heavily underemphasized**: Throughout the paper, the authors emphasize that the main component of the proposed method is the *KL divergence objective* applied to the base model. However, the augmented context information (QA pairs) generated by the *external model* appear to play a significant role and come with non-trivial costs. This highlights several points of potential improvement:

    1. **Cost implications of using an external teacher LLM**: The external LLM used to augment context information (gpt-4o-mini) is considerably more advanced than the base models considered in this study (OpenLLaMA 3B, Mistral 7B, Llama 3 8B), effectively positioning it as a "teacher" model. This substantial cost factor is neither discussed nor mentioned in the paper and could benefit from additional clarity. The cost is not only in terms of monetary expense but also in terms of computational resources and time required for inference using the external model to generate question-answer pairs for each context. This overhead is incurred *before* any fine-tuning of the base model even begins, and is a significant factor that should be acknowledged.

    1. **Unclear role of KL divergence in observed performance gains**: Given the role of augmented context information (QA pairs) generated by the external LLM, it remains uncertain how much of the observed performance gains stem directly from the KL divergence objective. A useful ablation study might involve comparing the proposed method with a fine-tuning baseline that employs next-word prediction (NWP) on the generated QA samples, rather than KL divergence with the context-prompted base LLM. This could clarify the unique contribution of the KL divergence. Note that the fine-tuning baseline experiment in the paper only uses the context information itself, rather than the augmented QA pairs.

    1. **Potentially misleading title**: Given the dependency on an external LLM, it may be misleading to describe the method as enabling "self-updatable LLMs". Additionally, describing fine-tuning (using KL divergence) as “updatable LLMs with parameter integration” may over-exaggerate the scope of the work.

2. **The novelty of the proposed context injection method may be overstated**: As described in Lines 124-128, previous works have also introduced the approach of distilling a given prompt into the model by replicating the output distribution when the prompt has been prepended (e.g., Choi et al. 2022), extending to distilling factual knowledge (context information) as well (Padmanabhan et al. 2024). Claims such as “This paper introduces the concept of Context Injection in LMs” (Line 154) might be reconsidered for a more balanced presentation.

3. **Lack of discussion on the costs associated with fine-tuning**: The computational cost of fine-tuning LLMs is substantially higher than that of inference, typically requiring roughly triple the computation due to backward passes, and significantly more memory to store intermediate activations. This additional cost is unique to fine-tuning approaches and does not apply to non-fine-tuning alternatives (e.g., MemoryLLM, InfLLM, RAG methods). However, the paper only contrasts storage requirements, which might downplay the runtime costs associated with fine-tuning in the proposed method.
    1. **Insufficient clarification of storage requirements across methods**: Providing more details on the storage requirements of the baseline methods—specifically by showing the constant factor (e.g., number of bytes) relative to the full model size—could be beneficial to readers, alongside asymptotic complexity.
    1. **Limited applicability of the method for "rapid integration"**: While the paper discusses the need for “rapid and frequent integration of small-scale experiences” (Lines 11-12), it is unclear how the fine-tuning-based approach proposed here supports rapid integration. A clarification might help strengthen this point.
        - To achieve rapid integration in a ChatGPT-like setting, one could use the context window to retain current session information and employ the proposed method (or baseline methods) to store and retrieve context from prior sessions. Fine-tuning could occur between sessions to support this integration. This may represent a more realistic evaluation setting. This may also achieve higher overall efficacy, as evidenced by the results in the single-context injection scenario, where the base model with the context provided directly in the prompt outperforms all other methods.

4. **Potential risk of encouraging hallucination**: Standard LLM pretraining typically encourages the model to respond accurately to the given context. Under the proposed method, however, the model is fine-tuned to respond to a question \( Q \) as though a specific context \( C \) were provided, even when it is not. This could introduce a risk of hallucination (and other undesirable behavior) by training the model to produce responses that might not be contextually relevant. For example, if the model is trained with QA pairs based on the context “Assume the current year is 1985,” it might answer a question like “Who is the current president?” with “Ronald Reagan,” disregarding the actual context. *(This is an illustrative example to convey the potential issue.)*

### Questions
Please refer to weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents SELF-PARAM, a framework for enabling self-updatable large language models that integrate new knowledge directly into model parameters without additional storage modules. By minimizing the Kullback-Leibler (KL) divergence between an original model (with context access) and a target model (without context), SELF-PARAM effectively embeds context within the model’s parameters. The framework addresses the challenges of rapid experience integration and long-term retention by incorporating diverse question-answer pairs related to the injected knowledge. Experimental results show SELF-PARAM’s effectiveness across single and batch context injections, sequential knowledge injections, and conversational recommendations, outperforming baseline methods in knowledge retention and response accuracy without extra parameters or external storage.

### Strengths
Originality: The approach of embedding knowledge directly in model parameters through KL divergence minimization of the source & target model while excluding the context information from the target model is a creative solution to self-updateability without extra storage.
Quality: Experimental results validate the approach across multiple tasks, showing improvements over existing methods in terms of efficacy and retention.
Clarity: The methodology and experiments are largely well-explained, making the paper accessible to researchers familiar with LLMs.
Significance: Addressing rapid knowledge integration and long-term retention in LLMs is a critical step forward, particularly for applications requiring frequent updates in dynamic environments.

### Weaknesses
Limited Baseline Analysis: While the paper compares extensively against memory-based methods, it does not do any comparison with other methods that are similar to the proposed methods, such as regularization approaches or other distillation based approaches that are commonly used in the continual learning literature. Specifically, the paper lacks a comparison against methods that also aim to modify model parameters directly for knowledge integration without relying on external memory or additional modules. This is a significant oversight, as the core claim of the paper is that it achieves self-updatability without extra storage, and thus, it should be benchmarked against other parameter-efficient methods that achieve similar goals. For example, regularization techniques that penalize changes to important weights or knowledge distillation approaches that transfer knowledge from a teacher model to a student model could serve as relevant baselines. The absence of these comparisons makes it difficult to assess the true novelty and effectiveness of the proposed SELF-PARAM framework.

### Questions
Questions
- Could the authors elaborate on potential limitations when scaling SELF-PARAM to even larger LLMs or highly complex contexts?
- How sensitive is the model’s performance to variations in the diversity of the question-answer pairs generated for context injection?
Suggestions
- I would suggest that the authors add other baselines that do not add additional modules or parameters; they are mentioned in the introduction section, but no explicit comparisons were made in the experimental section. Since this paper highlights the component that no additional parameters are needed, such comparisons should be made with those methods as well.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a context injection method SELF-PARAM.
Given a context, SELM-PARAM (i) employs an instruct model to generate a set of contextually relevant question-answering pairs (ii) trains the model by minimizing the KL divergence with the distribution where the context is provided.
Empirical evaluation is conducted to inject the contexts in PwC dataset into OpenLlama-3B-v2, Mistral-7B, and Llama-3-8B and INSPIRED and REDIAL into Mistral-7B, where the proposed method achieves consistently superior performance than the baselines in various settings.

### Strengths
* The proposed method requires no additional parameter and storage, which is computationally and memory efficient and compatible with the standard serving engine.
* In the empirical evaluation, the proposed method achieves superior performance in various settings, which seems inspiring.

### Weaknesses
 * My primary concern lies in the novelty.
Prompting highly capable language models have been a common method to collect training data and KL divergence is a common loss in knowledge distillation.
* Eq. (2) is ill-posed.
The summation is over any sentence $s$, making the term infinite and cannot be minimized.
It is also unclear to me what is the KL divergence between two scalar rather than distributions.
* Unrelated sentences are randomly sampled from SlimPajama to maintain the linguistic capabilities, but relevant ablation and evaluation are missing.

### Questions
* Why the fine-tuning is not compared in the sequential injection setting?

### Soundness
2

### Presentation
3

### Contribution
2
