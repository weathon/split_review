## Human Reviewer 1

### Summary
The paper introduces ASPD, a method that uncovers and exploits intrinsic parallelism in AR LLM outputs by identifying semantically independent segments that can be decoded in parallel. 
A dataset processing pipeline is also proposed. 
Evaluation results show that ASPD can speed up inference with under a 1% drop in output quality across tasks.

### Strengths
1. The paper proposes a new direction for test time scaling, where the LLM can generate texts using its intrinsic ability. 
2. The speedup comes with no additional compute cost. 
3. The parallel data generation pipeline seems interesting. 
4. It effectively overcomes the autoregressive bottleneck at the segment level.

### Weaknesses
1. The methodology for the dataset generation (Section 3.1) is not very clear to me. How do you rewrite the data into parallel and serial data? How is the verification done in detail? I feel Section 3.1 could be elaborated further with more clarity. 
2. There are not much details on the inference engine, like how it handles batching and so on. 
3. The evaluation does not compare with SOTA verifier-guided beam search methods.


Minor:
1. Figure 1 and 2 font sizes are too small to read.

### Questions
In addition to the weaknesses mentioned above, there are a few more questions:

1. What is the major difference between ASPD and Multiverse?
2. How does the inference engine maximize the inference efficiency?
3. What is the batch size used for inference in experiments?
4. What is the training cost?

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
4

### Confidence
4

---

## Human Reviewer 2

### Summary
The paper addresses the inference‑latency bottleneck in current LLMs due to strictly sequential autoregressive decoding. The authors observe that many generated responses contain intrinsic parallelism — segments that can be produced independently without breaking coherence. Motivated by this, they propose Adaptive Serial‑Parallel Decoding (ASPD), which addresses two core
challenges: automated construction of parallelizable data and an efficient parallel decoding mechanism. Experiments show that this method provides significant improvements in both effectiveness and efficiency compared to existing approaches.

### Strengths
Parallel decoding is a promising technique for inference acceleration. While previous works mainly focus on token-level parallel decoding (i.e., decode multiple tokens simultaneously), this paper leverages the intrinsic parallelism in LLMs. This is a good motivation.

Speed gains across diverse domains and models, with minimal trade‑off in output quality.

### Weaknesses
see questions

### Questions
The paper says: Tokens in the main branch maintain absolute positions in the flattened sequence, while parallel branches synchronize their position encodings at each timestamp. (line 269). Does this mean that tokens in parallel branches have two position ids: one for the main branch and the other for the parallel branches? If so, parallel tokens will recompute KVs when they are flattened and merged into the main branch, which introduces extra cost. If not, the position ids in the main branch are problematic.

What is the average and variance of parallel branch lengths? If branches have very different lengths, the decoding will be blocked by the longest branch.

### Soundness
2

### Presentation
2

### Contribution
3

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
The paper presents ASPD, a methodology for enabling parallel decoding. The method enables reusable KV cache and maintains ground truth position IDs during parallel decoding, with the capability to resume sequential generation mode after parallel generation mode. The work evaluates ASPD, showing it achieves increase in tokens/sec while maintaining the quality of sequential generation.

### Strengths
- ASPD enables parallel decoding while addressing the weaknesses of previous work (no sequential decoding after parallelizing in APAR; approximated position IDs disrupting position continuity in Pasta)
- The paper is generally well written and easy to understand, which the figures giving a very clear overview of the methodology and of differences with previous works.
- The experiments show that ASPD achieves the greatest tokens/sec and highest quality compared to APAR, SOT, and sequential across three benchmarks, demonstrating that ASPD does enable more tokens generated at time.

### Weaknesses
- The paper does not present the wall clock latency speedup of the different methods, but only tokens/sec and other efficiency metrics which do not account for actual system overheads to the methodology. As a speed-oriented parallelization method, wall clock speedup is an important evaluation metric. 
- It seems that the main difference between ASPD and Pasta is that in ASPD the position ID is maintained as if the tokens generated in parallel were actually sequential (i.e. ground truth position IDs) while Pasta uses model predictions to compute the position IDs, which makes Pasta an important baseline. However, the evaluation doesn't compare against PASTA as a parallel decoding baseline in Figure 4, but only ablate the data pipeline methodology used in Pasta.

Minor comment:
- The colored grid lines on Figure 4 makes it difficult to read.

### Questions
Please address the above concerns.

### Soundness
2

### Presentation
4

### Contribution
3

### Rating
4

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper introduces ASPD (Adaptive Serial-Parallel Decoding) to accelerate LLM inference by exploiting "intrinsic parallelism" in responses. Instead of pure autoregressive decoding, it identifies parallelizable structures via an automated, non-invasive data pipeline. A hybrid decoding engine then adaptively switches between serial and parallel generation, crucially maintaining and reusing the KV cache across modes. This approach achieved significant speedup up to 3.10x (1.82x avg) on Vicuna Bench while preserving generation quality with less than 1% degradation.

### Strengths
- The paper tackles an interesting aspect of the LLM parallelism. And the found intrinsic parallelism such as lists are interesting.

- The experiments are comprehensive and thorough, covering different reasoning tasks such as STEM, roleplay, reasoning, and extraction tasks.

### Weaknesses
- Speedups for certain tasks such as mathematics reasoning are limited. For example, the speedup on MATH500 is 1.17x, much lower than the 1.82x achieved on Vicuna Bench.

- The method is dependent on task structure. Mathematical reasoning, for instance, involves "strong inter-step dependencies" and "step-by-step deductions," which naturally reduces the opportunities for parallelization.

- The training overhead seems to be missing. What are the training overhead and how long does it take? Consider a quantitative analysis.

Miscellaneous
- Line 277 end: should be ``<branch>T_i:"

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
2