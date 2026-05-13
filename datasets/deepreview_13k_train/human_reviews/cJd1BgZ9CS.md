# DSI: Faster Inference of Large Language Models via Speculation Parallelism

- Decision: Accept
- Scores: 6, 3, 6, 5

## Abstract
Accelerating the inference of large language models (LLMs) is an important challenge in artificial intelligence. This paper introduces Distributed Speculative Inference (DSI), a novel distributed inference algorithm that is provably faster than speculative inference (SI) [leviathan2023fast, chen2023accelerating, miao2023specinfer] and traditional autoregressive inference (non-SI). Like other SI algorithms, DSI works on frozen LLMs, requiring no training or architectural modifications, and it preserves the target distribution. Prior studies on SI have demonstrated empirical speedups (compared to non-SI) but require fast and accurate drafters, which are often unavailable in practice. We identify a gap where SI can be slower than non-SI given slower or less accurate drafters. We close this gap by proving that DSI is faster than both SI and non-SI—given any drafters. DSI introduces a novel type of task parallelism called Speculation Parallelism (SP), which orchestrates target and drafter instances to overlap in time, creating a new foundational tradeoff between computational resources and latency. DSI is not only faster than SI but also supports LLMs that cannot be accelerated with SI. Our simulations show speedups of off-the-shelf LLMs in realistic single-node settings where DSI is 1.29-1.92x faster than SI.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a novel approach called Distributed Speculative Inference (DSI) for accelerating LLM inference. The algorithm is inspired by Speculative Inference (SI) but uses multiple drafters (small) and overlaps their execution with verifications from the verifier (large) to obtain greater speedup than SI. The authors show theoretically that DSI is faster than SI and standard LLM inference in expectation and 
 also show empirical speedups.

### Strengths
1. DSI appears to be a novel approach and effectively leverages the strengths of SI but also seeks to address its weaknesses like the drafter being blocked by verifier until the generated tokens are verified and also generalizes SI to work with multiple drafters in parallel.

2. The paper provides empirical evidence demonstrating that DSI outperforms both traditional speculative inference (SI) and non-SI methods

### Weaknesses
1. The approach requires more compute and memory (multiple KV cache) than SI with the amount of extra compute and memory required increasing with increase in number and size of the drafters, and with increase in input context length. Therefore, I believe that the increase in cost/resources also needs to also be considered in addition to the reduction in latency to make a fair assessment.

2. Evaluation is performed using simulations and not real implementations due to which it is not entirely clear if the gains will hold up in real settings. However, I understand that it is challenging to procure the amount of compute for inference with multiple LLMs and so I am willing to let this pass if my questions below on the evaluation are adequately answered.



### Questions
1. I do not understand the rationale behind the formula for acceptance rate on Page 8, line 410. Please clarify.

2. Why are you using an estimate of the acceptance rate instead of independently simulating acceptance/rejection for each drafter, target pair? For e.g. you could generate 'lookahead' tokens, verify them, go back to the drafter, and so on until the entire sequence is generated and then use the estimates of TTFT and TPOT to estimate the total latency. 

3. Please report the value of lookahead used for each row of Table 2, and clarify why that value was chosen.

4. Why are real world latencies of multithreading and context switching ignored (Page 10, lines 487-488)? These contribute to the overhead of DSI, and I feel that they should be reported and studied for a fair comparison of with SI and non-SI.

5. Will it be possible to show any simulation results with multiple drafters? I feel that one of the strengths of DSI is that it can work with multiple drafters and I would like to see how using multiple drafters compares with using a single drafter.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces Distributed Speculative Inference (DSI), an inference algorithm that accelerates large language model (LLM) inference more effectively than traditional Speculative Inference (SI) methods or standard autoregressive techniques. Unlike SI, DSI achieves speed improvements even when these drafters are slow or less precise. Speculation Parallelism (SP) enables target and drafter models to overlap in execution, reducing latency and introducing a new balance between computational resources and response time

### Strengths
* Paper is well written upto method. 
* Proposed Speculation parallelism effectively solves the blocking operation of speculative inference into non-blocking. 
* Method is backed by proof.

### Weaknesses
 * Evaluations are very weak. Can we get the experimental result by varying lookahead values on different machines?
* Actual improvement measurement seems missing. 
* Evaluating distributed evaluation on a single machine doesn’t make sense.. Authors really need to find way to run the evaluation on multi-GPU machines. Distribution involves communication latency as well, so in practice there are many things involved but these practical concerns are not discussed in the paper. 
* Evaluation writing is also very confusing..

### Questions
* What kind of communications are involved in distributed speculative parallelism and how does that affect the latency?

### Soundness
2

### Presentation
2

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
The paper introduces the parallel verification for accelerating speculative decoding. Experiments show speedups compared to the original speculative decoding.

### Strengths
- The paper is well-written and easy to follow.

- The idea is clear and seems to work well through evaluation.

### Weaknesses
 - The largest target model is capped at 13B.

  - How does the model work on larger models?

- The method need multiple GPUs to host several target model. This can cause deployment issues and energy issues.

  - How does the data communication defect the approach? The KV-cache also seems to move between GPUs. How about synchronization issues?
  - The analysis of the energy consumption compared to the original speculative decoding method seems to missing. More justification may be needed given the energy inefficiency of the method.

### Questions
See above.

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
This work proposes distributed speculative inference (DSI), or speculation parallelism in particular,
which accelerates speculative inference (SI) by leveraging more hardware resources (e.g. GPUs) to hide the latency of the verification steps in SI via parallelism and careful synchronization across multiple threads.
Through rigorous analysis,
it is shown that, while SI can be slower than standard autoregressive inference (non-SI) in certain scenarios, 
DSI is provably faster in expectation than both of them.
With a proof-of-concept implementation of DSI and careful design of numerical simulations,
empirical results suggest that DSI achieves 1.29-1.92x speedup over SI in various settings.

### Strengths
- The proposed speculation parallelism is novel and interesting, and might inspire future work on speculative inference or more general LLM inference acceleration.

- The rigor in both theoretical analysis and numerical validation (via careful design of simulations) is appreciated.

- The source code for the experiments is provided.

### Weaknesses
My main concern is that the practical value of this work is not yet evident enough.
If I understand correctly, the implementation of DSI in the current work is more or less a proof-of-concept, rather than one that is ready for application.
More specifically, only the outline of the multi-thread system is implemented, while the LLM part (e.g. forward passes of the drafter or target model) is not actually implemented but rather replaced by `WAIT` commands with delays that mimic the actual latencies of real LLM forward passes, for the purpose of simulations.
One might argue that, for a full implementation of DSI, we simply need to plug the LLM forward passes into the multi-thread system.
But this does not seem straightforward to me, since LLM inference is a complicated process by itself; 
combining it with the implemented multi-thread system can be challenging, as these two might not be completely decoupled.



One particular aspect I can think of is the compatibility with KV caches, which have been supported by both non-SI and SI, and enabled by default in most cases (e.g. when huggingface transformers is used for profiling the latency of standard LLM inference in the `ExperimentLatency` class within the source code of this work).
With multiple target LLMs (or verifiers) on different GPUs, each at its own pace, 
managing and synchronizing their KV caches seems like a non-trivial task and requires quite some engineering work,
which has not been implemented in this work.

### Questions
- Do you think DSI with a batch size larger than 1 is possible, at least in theory?
Batch inference is already quite a challenge for SI, and things seem to get much more complicated with the proposed speculation parallelism.


- Some minor issues about writing:
  - The paragraph between Lines 422 - 487 is a bit long; might be better to divide it into several paragraphs
  - Line 128 mentions "implementing (3) above", while Eq. (3) is actually located in the appendix 
  - Line 303, $f_1$ and $f_2$: should they be $f_j$ and $f_m$ instead?
  - Line 931, "upper bound": should it be "lower bound", since some components of latency in reality are neglected in the estimate?

### Soundness
2

### Presentation
3

### Contribution
2
