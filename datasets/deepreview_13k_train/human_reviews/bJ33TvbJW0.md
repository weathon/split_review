# SinkQ: Accurate 2-bit KV Cache Quantization with Dynamic Sink Tracking

- Decision: Reject
- Scores: 5, 3, 3, 5, 6

## Abstract
The impressive capabilities of large language models (LLMs) come at the cost of substantial computational resources during deployment. While KV Cache can significantly reduce recomputation during inference, it also introduces additional memory overhead. KV Cache quantization presents a promising solution, striking a good balance between memory usage and accuracy.
Previous research has shown that the Keys are distributed by channel, while the Values are distributed by token. Consequently, the common practice is to apply channel-wise quantization to the Keys and token-wise quantization to the Values. However, our further investigation reveals that a small subset of unusual tokens exhibit unique characteristics that deviate from this pattern, which can substantially impact quantization accuracy. Furthermore, these tokens often have higher attention scores, exacerbating their quantization errors.
To address this, we develop a simple yet effective method to identify these tokens accurately during the decoding process and exclude them from quantization, significantly improving overall accuracy. Extensive experiments show that our method achieves significant accuracy improvements under 2-bit quantization and can deliver a 6.4× reduction in memory usage and a 2.3× increase in throughput. Our code will be released upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents SinkQ, a 2-bit quantization technique designed to improve the memory efficiency of KV cache in LLMs. This method dynamically identifies and tracks "sink tokens"—tokens with high attention scores that would otherwise suffer from quantization errors—and excludes them from quantization to retain accuracy. The SinkQ approach offers notable memory and throughput benefits, achieving a $6.4\times$ reduction in memory usage and a $2.3\times$ increase in throughput, while minimally impacting model accuracy. It is implemented in a hardware-friendly way, providing compatibility with common LLM frameworks.

### Strengths
- This work provides thorough ablation studies and insightful findings on KV cache compression, particularly the role of attention distribution and the characteristics of tokens that function as attention "sinks."
- By excluding high-attention tokens from quantization, SinkQ effectively preserves accuracy under 2-bit quantization, making it feasible for real-time applications that require efficient memory usage.
- SinkQ’s compatibility with methods like KIVI, which uses channel-wise and token-wise quantization, demonstrates flexibility and potential for integration with other compression frameworks.

### Weaknesses
 - The paper lacks an in-depth discussion of the computational overhead introduced by steps such as slicing, concatenation, and the calculation of outlier tokens. A profiling of these operations, detailing the time spent on each, would help to understand the real-world efficiency impact. The analysis should include a breakdown of the latency introduced by each stage of the SinkQ process, such as the threshold comparison, index selection, and quantization, to fully assess its practical applicability.
- The paper compares SinkQ with KIVI but does not include comparisons with other KV cache compression methods, such as KVQuant, [1], GEAR [2] and SKVQ [3]. This makes it difficult to assess the relative performance of SinkQ against state-of-the-art techniques in KV cache compression. A more comprehensive comparison would include a range of methods, including those that use different quantization strategies or token-dropping approaches.
- SinkQ could be considered an innovation that combines aspects of token-dropping approaches, such as those in StreamingLLM [4] and H2O [5], with quantization strategies. The novelty may be seen as limited, as it appears to be an incremental improvement rather than a fundamentally new approach. The paper should more clearly articulate the specific novel contributions beyond the combination of existing techniques.

### Questions
- What is the overall overhead incured by additional operations, a profiling will be good.
- What is the process if the sink pool reaches its maximum capacity? Could you elaborate on the overflow outlined in lines 294-298?
- What are the performance metrics for SinkQ on models like Qwen and LongChat?

### Soundness
3

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
This paper proposes SinkQ, a KV cache quantization method for reducing memory overhead and improving efficiency of LLM inference. The authors observe the existence of sink tokens, which are a small subset of tokens that exhibit outlier characteristics and can occur at any token position, which significantly impact model accuracy. Based on this observation, the authors propose to keep a fixed-size pool for storing these sink tokens in full precision, while quantizing all other tokens following the KIVI approach. Empirical evaluations show that SinkQ mostly outperforms KIVI in preserving model quality.

### Strengths
1. This paper studies an important problem.
2. The proposed approach is well-motivated by the authors' observation.

### Weaknesses
1. The authors' observation of sink tokens is not new or novel. Previous works have observed the existence of heavy-hitter tokens [1] or salient tokens [2] in LLMs, which may occur at any token position. Hence, the claim on line 211 is inaccurate: "Previous work suggesting that attention sinks occur only in the initial tokens..."
2. The proposed method lacks novelty. The proposed mixed-precision approach for KV cache quantization is similar to previous works [2,3], which also identify outlier tokens in the KV cache and preserve in higher precision or full precision. The specific mechanism of identifying these outlier tokens based on key magnitude is not sufficiently distinct from prior work that also uses magnitude-based metrics, even if applied to different data structures.
3. The "Method" section is incomplete, missing some important details. It is not clear how SinkQ identifies the sink tokens, which is a critical part of the proposed method. During inference, the tokens are ingested in a streaming manner, while the authors only describe how the outlier tokens can be identified after saving all keys in an offline manner on line 152. The description lacks details on the exact thresholding or selection criteria used to determine which tokens are considered sink tokens, and how this is adapted during the streaming inference process.
4. Baselines are missing from the experiments. Since the authors adopt a mixed-precision quantization approach, mixed-precision baselines, such as KVQuant and ZipCache, are more relevant than the KIVI baseline. Moreover, the comparison with KIVI feels like an unfair comparison; since SinkQ directly adopts the KIVI approach (per-channel for keys and per-token for values, with residual cache) and adds sink tokens, the model quality will certainly outperform KIVI, but with memory and latency overheads. These overheads are not made very clear in Table 1 and 2. The lack of a detailed analysis of the computational overhead associated with identifying and storing sink tokens makes it difficult to assess the practical benefits of the approach.

### Questions
Can the authors please clarify the concerns raised in Weaknesses?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents SINKQ, a KV Cache quantization designed for efficient deployment of large language models (LLMs) by balancing memory use and accuracy. SINKQ identifies unusual tokens with distinct distribution and higher attention scores, which often lead to quantization errors.

### Strengths
The paper introduces an approach to improve quantization accuracy by dynamically excluding high-error tokens.

### Weaknesses
1. The major claim of this paper lacks sufficient justification. The foundation of the work is based on the statement, "Previous work suggests that attention sinks occur only in the initial tokens; however, our observations reveal that they can appear at any position within a sentence." However, there is no concrete evidence or examples provided to support this strong claim. To strengthen the paper, it would be beneficial if the authors included specific evidence, such as visualizations or quantitative analysis, to demonstrate instances where attention sinks appear at various positions within a sentence.
2. In the experiments, Figure 3(b) and Figure 3(c) suggest that the proposed method may not be as memory-efficient as Kiwi, despite claims of improved efficiency. It would be helpful for the authors to directly address this observation and clarify the reasons behind this apparent discrepancy. A more detailed analysis of the trade-offs between the proposed method and Kiwi in terms of memory efficiency would strengthen the discussion.
3. There are other state-of-the-art KV cache methods, such as those referenced in [1] and [2], which should be considered as additional baselines. Including these baselines would provide a more comprehensive evaluation. It would also be beneficial for the authors to explain why these specific baselines were not included initially and how their method compares to the key innovations introduced in [1] and [2].

### Questions
1. Will the code be made publicly available for reproducibility?
2. Can SINKQ be extended for higher-bit quantization, or is its design specifically optimized for low-bit scenarios?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents SinkQ, a method of KV cache quantization that takes care of attention sinks, i.e., outlier tokens that exhibit significantly high attention scores. Different from methods that rely on uniform quantization or fixed attention sinks, SinkQ can dynamically track and store attention sinks that appear at any positions within a sentence. Evaluation results on normal context-length tasks and long-context tasks demonstrate that SinkQ can achieve better accuracy and a comparable level of throughput / memory usage as compared to KIVI (SoTA 2-bit quantization baseline).

### Strengths
`+` The design of the method mainly stems from insightful empirical observations (clearly presented and visualized). Thus, the motivation of the work is very clear. The design itself is also natural and many intuitions are aligned with observations from prior work.

`+` Eval results on normal context-length tasks are good (in terms of accuracy), indicating that the design of dynamic attention sinks is effective.

### Weaknesses
- The take-away from section 4.3 is unclear: When the choice of group size (G) / residual length (R) varies, would the throughput increase as compared to KIVI be consistent? The memory overhead also appears a bit concerning to me --- Would the additional memory overhead of SinkQ scale even more when sink_num goes up? The broader concern here is about scalability --- Please refer to "questions". Specifically, the paper lacks a clear analysis of how different G and R values impact the trade-off between throughput and memory usage for SinkQ, and how these trade-offs compare to KIVI. It's not clear if the performance gains observed are robust across a range of these hyperparameter settings, or if they are highly sensitive to specific choices. Furthermore, the memory overhead associated with storing attention sinks is not thoroughly investigated. It's unclear how this overhead scales with the number of sinks and how it compares to the memory footprint of KIVI under different configurations. This raises concerns about the practical applicability of SinkQ in resource-constrained environments.

- Minor issues: Please consider fixing the y-axis of figures 1b and 1e, and the citation on line 210.

### Questions
Thank you for submitting this paper for ICLR. I have one concern below and I greatly appreciate it if the authors can offer some insights or clarification. I don't think it would require new experiment results:

- Scalability: I understand that it would be difficult to run experiments on larger LLMs (like the 70B+ models), but one missing point in the paper is how SinkQ would succeed (or fail) when the number of model parameters or the context length continuously go up. One potential consequence I can think of could be that the number of outlier tokens (i.e. attention sinks) grow quickly as the scale of the model / the context increase. In this case, would a small size of sink_num work? From table 4, it seems to me that using sink_num=1 should be sufficient, but that seems a bit too good to be true in most cases. If not, to support a larger size of sink_num, how would the extra memory overhead look like? --- This is one concern I have when I take a closer look at figure 3b. And if the memory overhead is too large and you have to use a small, fixed number of sinks (which means that you cannot store all outlier tokens), would SinkQ still be superior to KIVI in this case?

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
This paper proposes SinkQ, a near 2-bit KV Cache quantization method that demonstrates quality improvement over previous SOTA while improving throughput and accuracy.

### Strengths
The target problem is clear and have both theoretical and empirical comparison with previous work. 
The paper also conducted a detailed analysis on the attention values as well as controlled experiment to explain how some operations could increase accuracy. 
It is a nice extension from previous method (KIVI) and handles some outlier token problem in that KIVI does not solve.

### Weaknesses
Writing: Authors did not explain enough of the baseline method of KIVI, especially the part of group and residual in KIVI. The method is partly based on KIVI but authors mainly explained how they improved upon KIVI. Adding background on how KIVI separates between grouping and residual will be nice.
Eval: Lacks comparison with other non-quantization works
Lacks throughput number for ablation studies
(minor) Lacks experiment to larger models (ex. 70B)

### Questions
Can you add some comparison with non-quantization based compression work? In the current paper the only baseline is KIVI and original.

### Soundness
3

### Presentation
3

### Contribution
3
