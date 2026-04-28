# Hierarchy-Aided Sparse Attention For Fast LLMs Prefilling Inference

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Pre-filling Large Language Models (LLMs) with long-context inputs is computationally expensive due to the quadratic complexity of full attention. While global attention is essential during decoding, its importance diminishes during pre-filling, where the focus is on contextualizing tokens rather than predicting the next one. Building on prior work, we apply diagonal block sparse attention during the pre-filling phase, reducing attention-related FLOPs by over 90\% without significant degradation in language modeling performance. To address the remaining performance gap, we propose \textbf{H}ierarchy-\textbf{A}ided \textbf{S}parse \textbf{A}ttention (HASA), which incorporates a specialized transformer branch. This branch extracts global embeddings from each chunk and aligns local attention with full-attention, facilitating cross-chunk interaction. HASA stabilizes sparse attention computations, making the pre-filling phase highly efficient, particularly in long-sequence scenarios. While HASA significantly accelerates the pre-filling phase, we ensure robust language modeling performance by enabling interaction between global embeddings across chunks, which prevents the performance degradation typically observed in sparse attention mechanisms. Given that there are limited methods specifically accelerating pre-filling, our baselines include various open-source long-context models. Across multiple benchmarks, HASA not only maintains performance but also outperforms baseline models in certain scenarios. We will release the models upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes using block sparse attention to reduce prefilling time and an additional branch of global attention to compensate for the loss of global information. For global attention, they pool each block to get the representative token for each block and pass it to a new branch of the transformer.  This paper further parameter efficient fine-tuning LLMs with this method. This method improves over full attention on long context benchmarks and reduces latency.

### Strengths
1. This paper proposes a novel way to bridge sparse attention methods and hierarchical attention.

2. The prefilling phase is time-consuming, and this paper reduces time while maintaining most of the performance.

### Weaknesses
1. The novelty of this paper is limited. This paper is a mix of existing methods.

2. This method's speedup is not significant, and the additional branch takes twice the time to pass transformed layers.

### Questions
1. In Figure 2, it seems you are trying to express information with color; please add descriptions of each color.

### Soundness
3

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
This paper introduces HASA, hierarchy-aided sparse attention, to reduce the quadratic computation complexity. HASA incorporates a specialized transformer branch that combines sparse attention with hierarchical embeddings. Specifically, HASA first separate long texts into a series of chunks and compute local attention for each chunk during prefilling. To setup the connection between different chunks, the tokens inside each chunk also attend to a special embedding, which is an average pooling of token embeddings inside the chunk and attends to other previous special embeddings via the specialized branch with shift mask attention. Experiments conducted on various benchmarks demonstrate that HASA not only maintains performance but also outperforms baseline methods in certain scenarios.

### Strengths
- The key idea of leveraging a special embedding to capture dependency among different chunks is interesting in the context of efficient pre-filling.
- HASA achieves lower end-to-end latency compared to baseline methods.
- Table 4 shows that HASA achieves superior performance on several tasks from LongBench such as SQA and MQA.

### Weaknesses
1. HASA introduces a specialized branch to model inter-chunk attention, which, while ensuring efficiency, increases GPU memory consumption.
2. The performance comparison experiments with prior methods are not fully convincing. For example, YaRN-7B was trained on the PG19 dataset, whereas HASA was trained on the SlimPajama dataset in stage 1, followed by stage 2 instruction tuning on a mixed dataset. It is recommended to reimplement YaRN using the datasets utilized in this paper for a fairer comparison.
3. Compared to training-free methods for efficient long-context inference, such as Streaming LLM and MInference, HASA's adaptability to various LLMs and scenarios may be limited.

### Questions
Please see Weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces Hierarchy-Aided Sparse Attention (HASA), a simple and effective approach to enhance the efficiency of the pre-filling phase in large language models (LLMs) when processing long-context inputs. By employing diagonal block sparse attention with specifically designed global attention tokens, they significantly reduce attention-related floating-point operations (FLOPs) without largely compromising language modeling performance.

### Strengths
1. This paper is well-written, with a clear analysis and step-by-step presentation of the improvement from the original diagonal block sparse attention to the Hierarchy-Aided Sparse Attention. Hierarchy-Aided Sparse Attention is technically sound, and the experiments demonstrate its efficiency in the pre-filling phase with a long-context input.
2. The experiments are thoroughly conducted on LM, few-shot tasks, and long-context tasks, showing the effectiveness of Hierarchy-Aided Sparse Attention.

### Weaknesses
1. Introducing another transformer branch to distill the global information seems computationally heavy. It's better to include the original diagonal block sparse attention and HASA w.o. another transformer branch as baselines for ablating the influence of each proposed component for efficiency.
2. A strong baseline is sliding window attention plus some global attention at the end. In this way, information flows between overlapped blocks, compared to the independent block sparse attention. I would like to see the efficiency and performance compared to HASA.
3. Why does HASA not include the sink attention? As many papers suggest, the LLMs tend to contribute most of the attention score to the first token (i.e., the sink token). It seems that more efforts will be needed (e.g., training cost and network design) to convert full attention to sparse attention when dropping the sink token.

### Questions
Please address the concerns and questions in the Weaknesses part.

### Soundness
3

### Presentation
4

### Contribution
3
