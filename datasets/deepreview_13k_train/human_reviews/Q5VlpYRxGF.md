# Model Tells You Where to Merge: Adaptive KV Cache Merging for LLMs on Long-Context Tasks

- Decision: Reject
- Scores: 5, 5, 3

## Abstract
Large Language Models (LLMs) have attracted remarkable attention due to their unprecedented performance across a wide range of tasks. However, how to efficiently serve LLMs has become a pressing issue because of their huge computational cost in their autoregressive generation process. To mitigate computational costs, LLMs often employ the \emph{KV Cache} technique to improve the generation speed. While improving the computational efficiency, the storage requirements of the KV cache are substantial, particularly in long-context scenarios, leading to significant memory consumption. Existing KV cache eviction methods often degrade the performance of LLMs in long-context scenarios due to the information loss introduced by eviction. In this paper, we propose a novel KV cache merging approach, called \emph{KVMerger}, to achieve adaptive KV cache compression for long-context tasks without significant performance degradation under constrained memory budgets. Our approach is inspired by the intriguing observation that key states exhibit high similarity at the token level within a single sequence. To facilitate merging, we develop an effective yet straightforward merging set identification algorithm to identify suitable KV states for merging. Our merging set identification algorithm stimulates the second observation that KV cache sparsity, from similarity perspective, is independent of the dataset and remains persistent at the model level. Subsequently, we propose a Gaussian kernel weighted merging algorithm to selectively merge all states within each merging set. We conduct extensive experiments to demonstrate the effectiveness of \emph{KVMerger} for long-context tasks under constrained memory budgets, applying it to models including Llama2-7B/13B-chat and Mistral-7B-instruct. Using the LongBench and ZeroScroll benchmarks, we compare our method with other KV cache compression techniques, including H2O and CaM, showing that our method achieves superior performance across tasks with both $50\%$ and $35\%$ KV cache budgets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes KVMerger, an adaptive KV cache merging algorithm for large language models (LLMs) performing long-context tasks. By identifying and merging highly similar key-value (KV) cache states, the approach aims to reduce memory usage without compromising model performance. The authors use cosine similarity to cluster similar KV states and employ a Gaussian kernel-weighted merging technique. The effectiveness of KVMerger is demonstrated on various benchmarks and LLMs, with promising results compared to existing KV cache compression methods like H2O and CaM.

### Strengths
+ The paper introduces a unique perspective by formulating KV cache merging as a constrained clustering problem, presenting a fresh method to tackle memory efficiency challenges in long-context LLM tasks
+ KVMerger empirically appears to achieve notable memory savings, as evidenced by reduced GPU memory consumption during inference

### Weaknesses
 - The paper lacks a thorough discussion on the limitations or potential drawbacks of KVMerger, such as scenarios where high similarity assumptions in KV cache may fail or lead to degraded performance
- The merging algorithm’s reliance on cosine similarity computations and Gaussian kernel-weighted merging could be computationally expensive, especially for very large models, yet the paper provides limited insight into the computational overhead involved
- The paper assumes that highly similar key states contain redundant information, but it lacks a robust analysis of the potential impact of merging on nuanced context understanding, which is critical for certain tasks
- The study only compares KVMerger with H2O and CaM. Including more baselines or a hybrid method combining quantization with merging would better situate KVMerger’s relative effectiveness

### Questions
See weakness

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces KVMerger, a KV cache merging algorithm that adaptively compresses KV cache without significant performance loss. KVMerger uses a merging set identification algorithm and Gaussian kernel weighted merging to selectively merge similar KV states. Experiments on various LLMs show KVMerger outperforms baselines.

### Strengths
1. The writing is easy to follow.
2. The proposed method seems concise and effective.

### Weaknesses
1. The proof in Sec 4.1 makes the story confusing. In Sec 4.1, it is proven that the value states have low similarity due to the lack of RoPE representation, so why does your method still merge the value states and it is also effective?
2. Some experimental details are missing. Your Merging Set Identification likely requires calculating the similarity of states on a dataset. Which dataset do you use?
3. Some baselines are missing, such as PyramidInfer[1], PyramidKV[2] and SnapKV[3].
4. Is your merging only performed during the prefill stage? During generation, is merging also applied?
5. It would be best to compare the throughput during inference.
6. The equal sign '=' in Eq. (5) is used incorrectly. This is a formula, and '=' is not an assignment operator. You could represent the merged key state as something like $k_p^{*}$.

### Questions
1. Your objective function in Lines 311-314 appears to be NP-hard. How close is the solution found by your Algorithm 1 to this objective function?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Goal is to reduce the size of the KV-cache. The main approaches for this include quantization, cache eviction, and state merging. The core observation is that key states have high cosine similarity at the token level within a single sequence across different heads and model layers. The proposed approach cluster states, then uses Gaussian kernel weighted merging function to merge the elements within set. The method also retains anything with a top-k attention score (“sinks” style). The method is evaluated on a series of LongBench tasks, compared to CaM and H2O prior methods.

### Strengths
- The method is simple to implement, well-motivated, and is explained clearly 
- The paper compares to popular methods like H2O and CaM and offers strong improvements over them -- for this reason, the paper has the potential to be a significant step forwards
- The ablations around the choice of $\sigma$ and choice of merging algorithm are convincing

### Weaknesses
 The claim that RoPE is required to achieve high similarity is not well supported. It is not clear why RoPE is required to meet the stated conditions in Lemmas 4.1 and 4.2.
- The paper shows that key states exhibit similarity, but suggests that value states do not (Lines 203-205); it would be good to support this claim with experiments 

The method’s analysis could be improved
- It would be useful to further characterize when the method is expected to work well, as a function of the model and dataset – the analysis is incomplete. The current claim that the compression ratio remains the same independent of the dataset and model level seems incautious (Lines 267-283) – for instance, Mistral vs. Llama show very different trends in Table 1. 
- Most of the evaluated benchmarks are memorization oriented: rather than testing how well the model uses the context, models could use information stored in the MLP weights to succeed on most of these benchmarks (e.g., Wiki, QA, news tasks). It would be useful to consider a broader set of in-context learning tasks.
- Supporting this point that the chosen tasks are memorization-oriented, all the KV-cache compression methods work well on Llama models, and Llama is trained on many more tokens vs. Mistral.

The method is not compared to quantization and eviction methods; the paper suggests that all these categories methods tackle the same overarching objective, so it is important to compare to those methods’ quality as well.

The method does not explain how much of the gain is due to including the tokens with the top-k attention scores (Line 323). Do H2O and CaM do this as well? If not, then that could explain the improvement over those methods. I could not find this point clearly explained in the paper.

### Questions
There are several missing experiments and analyses -- see weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
