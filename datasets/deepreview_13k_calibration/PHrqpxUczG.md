# LogQuant: Log-Distributed 2-Bit Quantization of KV Cache with Superior Accuracy Preservation

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 5, 3, 6

## Abstract
We introduce LogQuant, a groundbreaking 2-bit quantization technique for KV Cache in large language model (LLM) inference, delivering substantial memory savings while preserving superior performance. Previous methods either assume that later tokens are more important or attempt to predict important tokens based on earlier attention patterns. Both approaches, however, can result in performance bottlenecks or frequent mispredictions.

LogQuant takes a different approach. By applying a log-based filtering mechanism, it selectively compresses the KV Cache across the entire context, achieving better performance with the same or even reduced memory footprint compared to existing methods. In benchmark tests, it enhances throughput by 25\% and boosts batch size by 60\% without increasing memory consumption. For challenging tasks such as Math and Code Completion, LogQuant improves accuracy by 40\% to 200\% at the same compression ratio, outperforming comparable techniques. LogQuant integrates effortlessly with popular inference frameworks like Python’s \texttt{transformers} library and will be made open-source upon publication.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes LogQuant, a KV cache quantization method for improving the memory efficiency and throughput of LLM inference.  Previous methods, such as KIVI and StreamingLLM, assume the most recent tokens and the first few sink tokens are more important for model performance. This work observes using log-distributed recent tokens are better for preserving model accuracy. Hence, the authors propose LogQuant, which stores a set of tokens at log-distributed positions in full precision, while keeping all other tokens quantized to achieve KV cache compression. Empirical evaluations show that LogQuant outperforms KIVI at 2-bit quantization.

### Strengths
1. This paper studies an important problem.
2. The presentation, including the figures and tables, are overall good.

### Weaknesses
1. The proposed method lacks novelty. The proposed LogQuant is highly similar to KIVI: they both use integer quantization with a fixed-sized full-precision cache, and the only difference is the selection method for the full-precision tokens. This work is also similar to mixed-precision approach for KV cache quantization such as [1,2], which identify outlier tokens in the KV cache and preserve in higher precision or full precision.
2. The token selection process of the full-precision cache in LogQuant is fixed and non-adaptive. The token selection is determined only by token position, and not dependent on attention score or token importance. As the authors illustrate in Figure 2, the outliers in attention score do not follow a fixed pattern. Hence, it is questionable whether using a fixed pattern of full-precision cache improves the accuracy of  KV cache quantization universally for all downstream tasks. Furthermore, the method does not account for the varying importance of tokens across different layers of the model. Some layers might benefit more from full-precision storage of recent tokens, while others might prioritize different token positions or attention-based importance metrics.
3. The experiments are not comprehensive. 4-bit quantization offers better quality than 2-bit quantization, and it is missing from the experiments. The baseline KIVI is also missing in the memory usage and throughput comparison in Figure 7.

### Questions
1. How does LogQuant compare with KIVI for 4-bit quantization? And how do they compare in terms of inference latency and memory usage?
2. In Table 2, is LogQuant achieving better accuracy than KIVI using equal or less memory budget?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents LogQuant, a new 2-bit quantization approach for compressing the KV cache in LLM inference. This approach applies a log-based filtering mechanism that enables significant memory savings while preserving performance. Unlike traditional methods that prioritize recent tokens or rely on predicted attention patterns, LogQuant uses a log-distributed approach to selectively compress tokens. LogQuant shows improvements in throughput (by 25%) and batch size (by 60%), and reportedly improves task accuracy for complex tasks like math and code completion by 40-200% at similar compression ratios.

### Strengths
- This work is based on interesting findings of attention score distribution among token positions.
- Leveraging a log distribution for token selection is innovative and addresses a core limitation in existing KV cache compression methods, improving the balance between memory use and performance.
- The method’s compatibility with popular inference frameworks makes it easily adaptable.

### Weaknesses
 - The evaluation only compares with KIVI [1] on task performance, which lacks a broad comparison with other compression methods. A more comprehensive range of baseline methods—like KVQuant [2], SKVQ [3], etc. Other types of compression methods [4, 5] under similar compression rates can be included. Also compression settings like 4-bit quantization—would provide a fuller view of its strengths and trade-offs.
- For many tasks, LogQuant results in a substantial accuracy drop (10+ points in some cases), which raises concerns about its reliability in sensitive tasks.
- This work does not sufficiently discuss the overhead from operations like slicing and concatenating.
- In many cases, the model experiences unexpectedly large accuracy drops, compared to numbers in other KV cache compression methods [1,2,3].

### Questions
- Could you expand the comparisons to include other compression strategies, especially those operating at similar compression rates? And what are the performance results for LogQuant under 4-bit quantization?
- Could you provide discussion and profiling of the overhead from additional operations, such as slicing and concatenating, to quantify their impact on throughput?
- What are the results on models like LLaMA3-8B (3.0), Mistral, and Lonchat? Refer to settings of https://github.com/henryzhongsc/longctx_bench [1].

[1] Kv cache compression, but what must we give in return? a comprehensive benchmark of long context capable approaches

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
3

### Summary
This paper proposes a new KV-cache quantization algorithm called LogQuant.

The design of LogQuant relies on the empirical observation that the position of high-attention spikes follows a log distribution—namely, it becomes sparser as tokens move further from the current position. Accordingly, LogQuant keeps non-quantized cache entries with respect to the observed distribution and quantizes the rest to INT2.

The paper also proposes an interesting throughput optimization by observing that $Softmax(Q · K^T)$ and $V$ positions can be reordered without changing the computation's outcome.

Evaluation results over several LLMs and benchmarks show that LogQuant is more accurate than KiVi.

### Strengths
- The paper makes the interesting observation that high-attention positions follow a log-like distribution. This observation can help guide the design of future approaches.
-	The reordering observation is interesting and can help improve future approaches' inference speed.
-	The empirical results seem to set the new SOTA for 2-bit KV-cache quantization

### Weaknesses
 - Some design choices are not compelling:

    o	The quantization scheme of using INT2 is arbitrary and should be elaborated on.  Specifically, the choice of INT2 over other low-bit quantization schemes such as INT3 or INT4, or even ternary quantization, is not justified. A detailed analysis of the trade-offs between different bit-widths and their impact on accuracy and memory footprint is missing.

    o	The design choice of which token to keep accurate is somewhat arbitrary. One can achieve a sparse pattern according to the desired distribution in different ways. For instance, instead of keeping the most recent tokens, the authors could explore a method that prioritizes tokens based on their attention scores or some other importance metric, which might lead to better performance.

- The evaluation leaves more to be desired:

    o	The prompt and generation lengths appear to be very small. Testing with larger context windows and generated sequences (e.g., 128K) would improve the paper. The current evaluation does not provide enough evidence that the proposed method can handle long sequences effectively, which is a crucial aspect for modern LLMs.

    o	There is no evaluation of the quantization error of the tokens that are not quantized. It is important to understand how the quantization impacts the accuracy of the retained tokens, as any error introduced in the quantized tokens could propagate to the retained tokens and affect performance.

- The degradation compared to the baseline is significant, and it is unclear where such a compromise can be acceptable. The paper should provide a more in-depth analysis of the scenarios where LogQuant is most suitable, considering the trade-off between accuracy and memory savings. Without this analysis, it is difficult to assess the practical value of the proposed method.

### Questions
- What would the performance of LogQuant be if the quantized tokens were discarded completely? 
- What group size is used in INT2? Is this overhead taken into account when comparing to other schemes?

- What about picking the retained accurate tokens in a way that preserves the distribution but non-deterministically? 

- Will the accuracy of a model with LogQuant be better than that of a smaller baseline model?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents LogQuant, a KV-cache quantization technique based on the observation that the positions of high-attention spikes follow a log distribution.

### Strengths
- The paper points out an interesting observation regarding the distribution of the positions of high-attention spikes. 
- The paper targets the KV-cache quantization of LLM, which has a high importance in deploying LLM.

### Weaknesses
 - The paper is mostly based on observation and proposes a heuristical solution. 
- The presentation of LogQuant (mostly section 3) requires revision to clarify the solution better.
- The authors use the terms “quantization” and “compression” alternatively, however, these terms have different meanings.
- I couldn’t find which quantization/compression technique is used in LogQuant. Furthermore, I found Figure 5 (and its caption) unclear.

### Questions
- The authors use the terms “quantization” and “compression” alternatively, however, these terms have different meanings.
- I couldn’t find which quantization/compression technique is used in LogQuant. Furthermore, I found Figure 5 (and its caption) unclear.

### Soundness
2

### Presentation
2

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
This paper 1) observes the log-distribution patterns of attention score magnitudes and attention spike locations, 2) introduces LogQuant to exploit these properties, and 3) shows that their approach can achieve higher accuracy and competitive throughput at the same compression ratio. LogQuant achieves this by applying a log-based filtering mechanism in the 2-bit quantization of the KV cache.

### Strengths
1. This paper observes an interesting phenomenon in the attention score pattern and designs a simple but effective KV cache quantization framework around it.
2. The paper is well-written.

### Weaknesses
1. Latency is the most important metric of efficiency, but it was not compared in the experiments.
2. The efficiency comparison does not use real-world inference traces and only includes a naive BF16 baseline.
3. The accuracy comparison only includes quantization baseline KiVi but no eviction-based baseline.

### Questions
Given that LogQuant and PartialLogQuant excel at different tasks, how do you decide when to use LogQuant or PartialLogQuant?

### Soundness
3

### Presentation
4

### Contribution
3
