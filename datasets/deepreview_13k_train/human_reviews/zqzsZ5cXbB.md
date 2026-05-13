# Let the Code LLM Edit Itself When You Edit the Code

- Decision: Accept
- Scores: 3, 6, 8, 5

## Abstract
In this work, we investigate a typical scenario in code generation where a developer edits existing code in real time and requests a code assistant, e.g., a large language model, to re-predict the next token or next line on the fly. Naively, the LLM needs to re-encode the entire KV cache to provide an accurate prediction. However, this process is computationally expensive, especially when the sequence length is long. Simply encoding the edited subsequence and integrating it to the original KV cache meets the temporal confusion problem, leading to significantly worse performance. We address this efficiency and accuracy trade-off by introducing \underline{\textbf{P}ositional \textbf{I}ntegrity \textbf{E}ncoding} (PIE). Building upon the rotary positional encoding, PIE first removes the rotary matrices in the Key cache that introduce temporal confusion and then reapplies the correct rotary matrices. This process ensures that positional relationships between tokens are correct and requires only a single round of matrix multiplication. We validate the effectiveness of PIE through extensive experiments on the RepoBench-C-8k dataset, utilizing DeepSeek-Coder models with 1.3B, 6.7B, and 33B parameters. Our evaluation includes three real-world coding tasks: code insertion, code deletion, and multi-place code editing. Results demonstrate that PIE reduces computational overhead by over 85\%  compared to the standard full recomputation approach across all model sizes and tasks while well approximating the model performance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a technique to update the rotary positional encoding when a small part of the context tokens are updated. It aims to optimize computational efficiency in real-time editing scenarios. The authors show that by fixing the positional encoding alone, they were able to retain a performance that is almost as good as fully re-encoding the context on a left-to-right code generation task, but with considerably less computational cost.

### Strengths
The paper effectively outlines the real-time editing problem and clearly describes the mathematical foundation for PIE based on rotary positional encoding.

### Weaknesses
 **Limited Technical Novelty**: The mathematical derivation is relatively straightforward, stemming directly from rotary positional encoding's relative nature, without additional innovation or complexity.

**Unrealistic Setting for Interactive Editing**:
 * Random Edits Only: The experimental setup evaluates PIE on random edits, which does not align with realistic real-time editing workflows, where temporally or contextually related edits are more common (e.g., editing a function signature and then updating its call sites). PIE’s simplifications may therefore be less applicable to typical usage patterns.
 * Single-Edit Evaluation: The paper evaluates PIE in a single-edit scenario, overlooking the potential for accumulated errors in multi-edit settings. In practical applications, users often make multiple edits, which could introduce drift in the positional encoding without full recomputation.
 * Left-to-Right Only: Evaluations are limited to left-to-right generation, omitting fill-in-the-middle (FIM) generation, a task relevant in code editing where users may modify code segments in the middle of sequences. Without this, it is unclear how PIE would perform in varied editing tasks.

**Unconvincing Conclusions Due to Limited Evaluation Scope**: Given the unrealistic evaluation settings, the claim that PIE can retain performance by adjusting positional encoding alone is unconvincing. By testing only on random edits, the experiments fail to address cases where contextual dependencies (e.g., edits that affect other tokens' relevance) might demand full recomputation. This risks overstating PIE’s applicability to real-world editing scenarios. To build a more compelling case, I recommend:
 * Evaluating PIE on real user edit sequences rather than synthetic random edits.
 * Restricting comparisons with full recomputation to cases where edited tokens impact final target tokens meaningfully (e.g., by verifying that removing or masking these edited tokens affects the target token prediction likelihood).
 * Including a special baseline where the pre-edit context is reused without modification, establishing a zero-cost apporach for comparison.

**Lack of Multi-Edit and Accumulated Error Analysis**: With each edit, additional errors will enter the encoding under the proposed technique, but the paper provides no analysis of error accumulation across multiple edits. Without such discussion, it’s unclear when a full recomputation might be needed to reset the encoding.

**Lack of Fill-in-the-Middle Evaluation**: Evaluations are limited to left-to-right generation, omitting fill-in-the-middle (FIM) generation, which is more relevant to the interactive coding assistant scenarios mentioned by the paper.

### Questions
Could you provide performance results for a baseline that reuses the pre-edit context without modification for making suggestions? This zero-cost approach would be helpful to compare against Full-recomputation in your benchmark.

### Soundness
1

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
The paper presents Positional Integrity Encoding (PIE) as an inexpensive alternative to re-encode the entire KV cache during LLM decoding specifically for code related tasks. PIE solves the temporal confusion task efficiently using a single round of matrix-multiplicaton. The authors provide results on RepoBench dataset using 3 different sizes of DeepSeek-Coder model for 3 tasks- code insertion, deletion and multi-place editing. The results show that PIE reduces computational overhead by 85% compared to full-recomputation without significant loss of performance.

### Strengths
1. The paper is well-written and easy to understand.
2. The authors solve an important task of efficiency in updating KV cache in a real-time code editing setting. This is crucial for interactive coding assistant scenario where the developers make frequent and incremental changes to the exisiting code and require copilot to correctly predict the next line on the fly.
3. The authors perform experiments on 1 dataset for 3 tasks and show 85% reduction in computational overhead compared to brute-force approach.

### Weaknesses
1. The results are limited to 1 dataset and 1 model. Including more than 1 dataset and model would make the claim more strong.
2. The authors solve an important task of efficiency of real-time code editing but do not discuss the limitations of this approach for other tasks where semantic impact is large or in case of large code edits.
3.The approach has a dependency on RoPE and might not be suitable for other models without RoPE

### Questions
1. Can you please add evaluations for 1 more dataset and 1 more model?
2. How does the approach do for other non-code related tasks where semantic relationship is important?
3. How does the approach do for longer edits?
4. Is there any memory overhead of the proposed approach?
5. Does this approach lead to any cumulative errors if you continue to update KV cache based on PIE?
6. The average scores of 3 experiments are reported, could you also report the standard deviation?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper describes a new approach called Positional Integrity Encoding (PIE) that aims to improve the efficiency of Large Language Models in real-time code editing scenarios.

PIE improves the accuracy and efficiency of predictions by solving the problem of the computational overhead associated with recoding the entire context when editing existing code.

### Strengths
I really enjoy this paper!

The Positional Integrity Encoding (PIE) introduced by the authors capitalizes on RoPE, adeptly addressing temporal disorientation by initially stripping away the rotary matrices responsible for confusion and subsequently reinstating the appropriate matrices through straightforward matrix multiplication.

This capability to enhance computational efficiency without compromising accuracy is precisely the straightforward yet potent approach we value in the realm of language model optimization.

The PIE not only paves the way for future research in optimizing Large Language Models (LLMs), particularly focusing on efficiency, but also excels in real-time dynamic scenarios. Its compatibility with existing acceleration techniques positions PIE as a catalyst for further advancing the practical deployment of LLMs.

### Weaknesses
My current concerns are regarding the selection of downstream tasks and evaluation metrics considered by the authors.

(1) The tasks of code insertion, code deletion, and multi-place code editing that the authors have considered seem less critical and common in actual development scenarios compared to code generation.

(2) The chosen evaluation metrics, EM (Exact Match) and ES (Edit Similarity), may not accurately assess the semantic correctness of the generated code.

(3) The selection of models is limited to the DeepSeek-Coder series.

### Questions
1. Can the PIE be effective on code generation tasks?

2. Why not consider the Pass@1 metric?

3. Is PIE equally valid on other models (Qwen-2.5-Coder; Llama-3.1; Yi-Coder)?

I am more concerned about the third of the above issues. If the supplemental results do show the validity of PIE, I will raise my score.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes Positional Integrity Encoding, an algorithm to correct rotary positional encoding in the KV cache of displaced tokens due to edits. It shows significant speed-up compared to full recomputation.

### Strengths
- The proposed algorithm significantly reduces the latency of generation with edited prefixes.
- A straightforward solution to adjust the rotary matrices to correct temporal confusion.

### Weaknesses
 - The algorithm looks somewhat trivial to me. It simply corrects the position embedding by transforming the rotary matrix in RoPE.
- Limited experiments. All performance experiments were conducted on RepoBench-C-8k and DeepseekCoder. It is unclear if this algorithm generalizes to other settings and models.

### Questions
- Have you conducted more experiments on more settings and models?
- Is it possible to provide an in-depth *theoretical* analysis (in 4.3) of the cause of performance drop between PIE and the recomputation?

### Soundness
2

### Presentation
3

### Contribution
2
