# SEAL: Scaling to Emphasize Attention for Long-Context Retrieval

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
In this work, we introduce a novel approach called Scaling to Emphasize Attention for Long-context retrieval (SEAL), which enhances the retrieval performance of large language models (LLMs) over extended contexts. Previous studies have shown that each attention head in LLMs has a unique functionality and collectively contributes to the overall behavior of the model. Similarly, we observe that specific heads are closely tied to long-context retrieval, showing positive or negative correlation with retrieval scores. Built on this insight, we propose a learning-based mechanism using zero-shot generated data to emphasize these heads, improving the model's performance in long-context retrieval tasks. 
By applying SEAL, we can achieve significant improvements in in-domain retrieval performance, including document QA tasks from LongBench, and considerable improvements in out-of-domain cases.
Additionally, when combined with existing training-free context extension techniques, SEAL extends the context limits of LLMs while maintaining highly reliable outputs, opening new avenues for research in this field.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work focuses on scaling to emphasize attention to long-context retrieval, designed to enhance the retrieval performance of LLMs in handling extended contexts. A cost-effective, learning-based mechanism is proposed to improve the model's performance in long-context retrieval tasks, which emphasizes specific attention heads tailored to retrieval tasks. Experimental results demonstrate superior performance over the compared baselines.

### Strengths
1. This paper is well-organized and easy to read. 
2. The proposed method presents a reasonable approach for long-context retrieval by identifying the key components of Transformer architecture to boost retrieval performance. 
3. The approach is practical and has the potential for broad application in various RAG settings.

### Weaknesses
1. The term "cost-efficient" is not clearly defined, resulting in ambiguity when assessing the cost-effectiveness of the approach. The strategy of identifying key components initially and subsequently fine-tuning these components may prove to be computationally intensive. It would be beneficial to provide details regarding the computational time involved in this process, including the time required for both the initial component identification and the subsequent fine-tuning stages. Furthermore, a more detailed breakdown of the computational resources used, such as the specific GPU model and memory usage, would be valuable.
2. A more thorough evaluation would benefit from comparisons with a broader range of advanced baseline models. Currently, the proposed method is compared against only one simple. Including more sophisticated long-context modeling methods, such as those employing attention mechanisms with sparse or hierarchical structures, and state-of-the-art techniques like retrieval-augmented generation with more complex indexing methods, would better validate the effectiveness of the proposed method. The current comparison does not sufficiently demonstrate the advantages of the proposed method over existing advanced techniques.
3. To confirm the versatility of the proposed method, it would be beneficial to conduct experiments on different LLMs of varying sizes, including both smaller and significantly larger models. This would help assess the scalability of the approach and its applicability across a wider range of model architectures and parameter counts. The current experiments do not provide sufficient evidence to generalize the method's effectiveness across diverse LLM scales.

### Questions
Please refer to the weaknesses.

### Soundness
2

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
The paper introduces SEAL (Scaling to Emphasize Attention for Long-context retrieval), a novel attention scaling approach that improves retrieval performance for long-context tasks in Large Language Models (LLMs). It addresses the challenge of performance degradation over extended contexts, particularly in retrieval tasks. SEAL fine-tunes specific attention heads or channels using a minimal amount of training data, leading to significant improvements in long-context retrieval across various benchmarks. The paper focuses on cost-efficient enhancement of long-context capabilities without altering the model’s learned behavior.

### Strengths
1. SEAL presents an innovative approach by leveraging attention head/channel scaling to enhance long-context retrieval.
2. The method uses very few trainable parameters and requires minimal training data, making it highly efficient.

### Weaknesses
1. The term “long-context retrieval” is ambiguous. It would be clearer to refer to “retrieval tasks that have long contexts,” which directly emphasizes tasks like passage retrieval or number retrieval. The current phrasing lacks the necessary specificity to clearly define the scope of the problem being addressed. It is unclear whether the focus is on the length of the context itself or the nature of the retrieval task when dealing with long contexts. For example, does long-context retrieval refer to retrieving a single fact from a long document or retrieving multiple facts scattered throughout the document? This ambiguity makes it difficult to assess the novelty and relevance of the proposed method.
2. The paper lacks explicit detail about which context extension techniques are used. For example, Figure 6 mentions the use of Self-Extend, but no experiments isolating its performance are provided. The paper does not clearly delineate the contributions of the proposed method from the effects of context extension techniques. Without isolating the performance of Self-Extend, it is difficult to determine whether the observed improvements are due to the proposed method or the context extension technique. This lack of clarity undermines the validity of the experimental results.
3. Logical Flow in Writing: Certain parts of the paper are difficult to follow due to writing issues such as ambiguous expressions, inconsistent time tense, and occasional typographical errors (e.g., “biases” instead of “bias”). The paper suffers from a lack of clarity and precision in its writing, making it difficult to understand the proposed method and its contributions. The use of ambiguous expressions and inconsistent terminology creates confusion and hinders the reader's ability to follow the logical flow of the arguments. These issues detract from the overall quality of the paper and make it difficult to assess its technical merits.
4. The distinction between “in-domain” and “out-of-domain” in the experiments is confusing. Specifically, if “in-domain” refers to training on retrieval tasks, why are the same datasets used for both “in-domain” and “out-of-domain” experiments? The use of the same datasets for both in-domain and out-of-domain experiments raises questions about the validity of the experimental design. It is unclear how the authors define the domain and what criteria are used to differentiate between in-domain and out-of-domain scenarios. This lack of clarity makes it difficult to interpret the experimental results and assess the generalization capabilities of the proposed method.

### Questions
1. What specifically constitutes “long-context retrieval”? Could the authors clarify this definition and provide more precise terminology?
2. Why are different LLMs used in Figures 5 and 6? Is there a specific reason for the model changes, and how do these variations impact the comparability of the results?
3. Can the authors provide experiments isolating the effect of Self-Extend in Figure 5 to verify its individual impact on performance?
4. What is the rationale behind using the same datasets for “in-domain” and “out-of-domain” experiments in Table 3? How is “out-of-domain” defined in this context, and what criteria differentiate the two?

### Soundness
2

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
This paper proposes an approach called Scaling to Emphasize Attention for Long-context retrieval (SEAL), which emphasizes specific heads or channels (attention outputs) particularly related to long-context retrieval by efficiently adjusting the strength of each attention component. The authors claimed that SEAL achieves significant improvements in in-domain retrieval performance and cross-domain document QA tasks, also extends the context limits of LLMs while maintaining highly reliable outputs.

### Strengths
1. This paper proposes SEAL to efficiently adjusting the strength of each attention component, and achieves superior performance to various LLM baselines in long-context retrieval.
2. The content, figures, and tables of the paper provide a detailed explanation and analysis of the motivation, methods, and experiments, facilitating the readers' understanding.

### Weaknesses
1. The experimental results in Table 1 show that SEAL-H and SEAL-C require fewer parameters than Baseline and SEAL-L. However, their performance does not consistently surpass SEAL-L in long-context scenarios, failing to demonstrate the authors' claims.
2. The experiments only select SEAL-L as the baseline, it should include other PEFT methods for comparison.

### Questions
1. Except fewer parameters, what other advantages does SEAL have over LoRA or other PEFT methods? Since the parameters of SEAL-L is also small compared to LLMs, what are the unique application scenarios for SEAL?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel and practical method, SEAL, to improve the long-context retrieval ability of LLMs. 

First, through perturbation experiments, it finds a certain attention head or a certain channel in it can cause a positive or negative effect on long-context retrieval accuracy.

Second, it demonstrates directly scaling the hidden states of these heads or channels can indeed improve the retrieval accuracy of LLMs. 

Third, it adds trainable scale factors into the model and use a small amount of samples of retrieval tasks to fine-tune the model. The results show SEAL can remarkably improve the long-context retrieval ability of LLMs.

### Strengths
1. This paper discovers that a certain attention head can cast a remarkable positive or negative effect on long-context retrieval accuracy, even as well as a certain channel. This is interesting and helpful for us to further understand the role of the internal modules of LLMs.

2. The proposed method, SEAL, is very cost-effective, which only needs very few training samples and tuned parameters.

3. There are enough evaluation results of various models to demonstrate the method’s effect.

### Weaknesses
1. Narrow scope

The method seems to only be applicable for classic retrieval tasks such as NIAH, and the training data is also the same types of tasks. It will not be surprising that this leads to an improvement, since this task has been too simple, fixed and formulaic, which may represent a narrow application scope for this method. It would be better to train and test on more tasks such as Knowledge-QA.

2. No unique advantages

The author should empirically test whether the time or space required by SEAL is significantly less than that of LoRA. Otherwise it cannot show significant superiority of SEAL compared to LoRA. Because the parameters tuned by LoRA are already very few. Though SEAL can theoretically tune much less parameters, it may not significantly save much time. 

3. There is little detailed description about the procedures of the method in the abstract or introduction. This will make it hard for readers hard to grasp the method quickly. There usually should be a paragraph included in the introduction to describe the specific operation of the method.

4. The curve of data points in Figure 4 (a) may be too small, making it hard to clearly see the changes.

### Questions
1. Can you demonstrate the unique advantages of your method compared to LoRA through more experiments?
2. Can you train and test on more various task types to demonstrate the generalization of your method?

### Soundness
3

### Presentation
3

### Contribution
3
