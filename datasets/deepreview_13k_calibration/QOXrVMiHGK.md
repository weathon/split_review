# PEARL: Parallel Speculative Decoding with Adaptive Draft Length

- Decision: Accept
- Avg Score: 5.75
- Scores: 8, 6, 6, 3

## Abstract
Speculative decoding (SD), where an extra draft model is employed to provide multiple \textit{draft} tokens first and then the original target model verifies these tokens in parallel, has shown great power for LLM inference acceleration.
However, existing SD methods suffer from the mutual waiting problem, i.e., the target model gets stuck when the draft model is \textit{guessing} tokens, and vice versa. This problem is directly incurred by the asynchronous execution of the draft model and the target model, and is exacerbated due to the fixed draft length in speculative decoding.
To address these challenges, we propose a conceptually simple, flexible, and general framework to boost speculative decoding, namely 
\textbf{P}arallel sp\textbf{E}culative decoding with \textbf{A}daptive d\textbf{R}aft \textbf{L}ength (PEARL). 
Specifically, PEARL proposes \textit{pre-verify} to verify the first draft token in advance during the drafting phase, and \textit{post-verify} to generate more draft tokens during the verification phase.
PEARL parallels the drafting phase and the verification phase via applying the two strategies, and achieves adaptive draft length for different scenarios, which effectively alleviates the mutual waiting problem.
Moreover, we theoretically demonstrate that the mean accepted tokens of PEARL is more than existing \textit{draft-then-verify} works.
Experiments on various text generation benchmarks demonstrate the effectiveness of our \name, leading to a superior speedup performance up to \textbf{3.79$\times$} and \textbf{1.52$\times$}, compared to auto-regressive decoding and vanilla speculative decoding, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper aims to accelerate LLM decoding by building on top of the popular Speculative Decoding (SD) algorithm. It addresses a key bottleneck in SD, the mutual waiting problem: the draft model and target model often get stuck waiting for each other because of sequential execution of the two logic with fixed draft lengths.

Unlike traditional SD, the proposed algorithm PEARL (Parallel spEculative decoding with Adaptive dRaft Length) generates variable draft lengths and supports asynchronous execution through two new operations: pre-verify and post-verify. The authors evaluated PEARL across various tasks (e.g., HumanEval, GSM8k), observing significant speedups in performance.

### Strengths
* The motivation is clear, with strong supporting evidence, such as in Figure 2.
* Effective visualization of the PEARL algorithm, as shown in Figure 3.
* Reduction in manual parameter tuning for gamma, which previously required significant effort in SD (Section 4.1), even if the estimation remains somewhat approximate.
* Extensive evaluation across various tasks, including code generation, reasoning, and multi-round dialogue.

### Weaknesses
 * The window size for each chunk (gamma) appears to remain fixed, which means the draft length will still be determined by the multiplication of gamma. While this may be unavoidable in the current algorithm, the abstract and introduction suggest that the authors intend to eliminate the need for gamma entirely.
* Pre-verify with only a single token might not be the most reliable method. See below for a question.
* While Section 5 presents a study on various datasets, the paper does not include a detailed analysis, such as step-by-step profiling or the failure rate in pre-verification. Furthermore, the analysis lacks specifics regarding the frequency of pre-verify vs. post-verify strategy changes, which would be crucial for understanding the adaptive behavior of the algorithm.



### Questions
* The range of 1.50x to 4.43x represents a significant gap. Is there any analysis explaining the reasons for such large differences?
* Considering that pre-verifying a single token may not be the most accurate method for estimating difficulty, can the authors provide empirical evidence or analysis on how effectively the pre-verification of the first token compares to that of other tokens? For example, could there be potential pitfalls when using a very large gamma?
* Could the authors illustrate a few examples of profiling PEARL on real data, similar to Figure 3, but using actual data?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents an interesting speculative decoding (SPD) paradigm, PEARL, that attempts to overlap the drafting and verification stages in the standard SPD framework, thereby mitigating the so-called mutual waiting issues. As a training-free SPD method, PERAL achieves a state-of-the-art acceleration ratio with different pairs of LLMs on different domains by switching between pre-verify and post-verify stages to adjust the draft length dynamically.

### Strengths
1. The idea is novel to some extent: while the community has noticed that the drafting stage is the bottleneck of the current SPD system and has proposed works to either dynamically adjust the draft length or decode draft tokens in parallel, attempts to pre-verify and post-verity are innovative to lower the proportion of drafting latency in the SPD process.
2. The illustrations are self-explanatory in Figure 3. 
3. PERAL eliminates the need to tune the drafting window size according to Section 4.1, a desirable property for other SPD frameworks.

### Weaknesses
1. Missing baselines: while comparison with SPD methods that require training (Medusa, EAGLE, etc.) is not expected, there is still a line of works that focus on training-free SPD, such as Self-Speculative [1], Parallel Decoding [2] and REST [3]. Adding these should be able to strengthen this submission, but please do not focus on this during the discussion stage.

Other than these, I don’t find obvious weaknesses in this submission. Please refer to the question section regarding my main concern.

### Questions
I find the following concerns and would like further clarification from the authors. 

The core idea behind SPD is to utilize hardware computation redundancy; therefore, running forward passes on drafter and target models simultaneously has to bring additional latencies for both the drafting and verification stages. I am glad to see the paper presents theoretical and empirical analysis, but none of them discussed this. Profiling the latency overhead brought by overlapping two stages could strengthen this paper. (I noticed Appendix E, an engineering technique to get around the resource competition issues, but still, some analysis is expected; let’s say we don’t have a multi-GPU environment to implement the PP solution.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper describes and addresses the problem of "mutual waiting" in Speculative decoding (SD) for LLM inference acceleration, where typically, the target model and draft model are mutually blocked by each other since verification can only occur after drafting is completed and vice-versa (draft-then-verify). The authors propose a novel framework to address this mutual waiting problem called "Parallel Speculative Decoding with Adaptive Draft Length" (PEARL) that coordinates the drafting and verification steps partially in parallel by using “pre-verify” and “post-verify” strategies for verifying the first draft token in advance during drafting and generating more drafts during verification, respectively. This can be thought of as a shift from the “draft-then-verify” sequential paradigm into a more parallelized “draft-and-verify” paradigm. In addition to the “pre-verify” and “post-verify” strategies, the authors explore the use of an adaptive draft length to further reduce the mutual-waiting scenario where suboptimal draft lengths are used, whether too short or too long. Using these proposed strategies, the authors are able to showcase relative speedups on top of vanilla SD on a variety of text generation tasks.

### Strengths
- Authors clearly present their ideas and propose their PEARL framework with solid working examples and motivations. In particular, the analysis into the mutually blocked asynchronous execution of drafting and verification as well as optimal draft length per decode step were helpful in understanding the potential headroom for a parallelized framework of SD.
- Experiments with PEARL yield a solid speed up of 1.5x over vanilla speculative decoding on common text generation tasks as well as in comparison to other baselines for the HumanEval code generation task
- The paper examined each of the component strategies of PEARL, pre-verify, post-verify, and adaptive length, independently via ablation studies and analysis to isolate and highlight the relative impacts and relationships between each strategy
- Authors provide code implementation for reproducibility

### Weaknesses
 - The main paper assumes execution scenarios where there are enough resources to run drafting and verification in parallel (e.g. multiple GPUs). However, in many instances, drafting and verification happen in co-located settings (e.g. single GPU) where it is more resource constrained. While the authors do make brief mentions in the main paper about these resource constrained scenarios, their discussion and strategies to address this are limited to a relatively short section in the appendix with not much details on their experimental results. It would be much more fitting to have this section filled with more detail and part of the main paper. For example, the strategy mentioned in the appendix involved copying the drafter model across multiple chips which incurs greater memory cost as well as potential communication cost in having to transport and sync intermediate attention KV caches.
- Additionally, given the fact that drafting and verification is assumed to occur on separate devices in parallel, it would be good to see a mention into the communication overhead of data transfer (i.e. logits for adjusted sampling during verification rejection) as well as a breakdown into the additional computational and power consumption in practice from added drafting and verification calls that PEARL conducts in comparison to SD. Specifically, the cost of transferring logits for the adjusted sampling during the verification rejection phase should be quantified, as this could become a bottleneck in distributed settings. Furthermore, a detailed analysis of the computational overhead, including FLOPs and energy consumption, associated with the increased number of drafting and verification calls in PEARL compared to standard SD is needed to fully assess the practical implications of the proposed method.
- While a variety of tasks (HumanEval, GSM8K & MGM, MT-bench) and baselines (SD, Ouroboros, Lookahead Decoding, Distillspec, Assisted Generation) were mentioned in the experiments, the variety of baselines were only used for the HumanEval code generation task while the remaining GSM8K & MGM and MT-bench tasks only used auto-regressive (AR) and SD baselines. The lack of comprehensive comparisons across all tasks limits the generalizability of the findings. For instance, it is unclear how PEARL compares to methods like Ouroboros and Lookahead Decoding on tasks beyond code generation, making it difficult to assess its overall effectiveness.

### Questions
- Is additional communication overhead costs incurred when running drafting and verification on separate accelerators? (e.g. logits transport from 2 devices for rejection sampling/verification)
- There are 5 baselines listed but Table 2 and Table 3 only report Auto-regressive and SPEED?
- What is the assisted generation baseline exactly? Does it adjust draft length depending on the number of tokens accepted in the previous iteration?
- What value of gamma was used for the baselines on each task? Was it fixed according to the optimal gamma values determined for PEARL?
- Why do Table 5 and Table 6 differ for HumanEval with gamma=5 for Llama2 7B&70B (40.72 in Table 5 and 30.34 in Table 6)?
- Is there a cap on draft length given the fixed optimal verification window size? Something like 2x? Large gamma values aren’t only detrimental to drafting phase but also incur additional computational cost in verification (verifying 4 tokens vs. 32 can be a significant difference) even for vanilla SD
- Table 9 should clarify that it’s not inference speed time but is the number of model runs? Perhaps good to report the ratio on the side (PEARL has ?x more model runs than SD)
- Line 034: remove “the” in “the natural language”
- Line 046-047: rewrite to “draft tokens that the original large model (referred as the target model) then verifies in parallel…”
- Line 161: “generating” not “generation”
- Line 199: “that stucks the target model” ? Do you mean “blocks”?
- Line 240 remove “have”
- Line 331 “being” not “been”
- Line 352: speed up ratio relative to baseline auto-regressive?
- Line 410: Pearl without post-verify as Pearl w/o “pre-verify”
- Line 412: “exhibits a more pronounced”
- Line 691: “reject some” not “someone”

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors aim to address two challenges: 1. The mutual waiting problem, which arises when the target model becomes idle while waiting for the draft model to generate tokens, and vice versa. The asynchronous execution of the draft and verification phases leads to inefficiencies. 2. Fixed draft model length.

The authors introduced two strategies to solve this issue: 1. Pre-verification: This strategy involves using the target model to verify the first draft token during the drafting phase. By doing this, PEARL can determine whether the drafted token will likely be accepted or rejected.
If the first draft token is verified and accepted, the draft model can generate additional tokens more confidently. Conversely, if the first token is likely rejected, the draft model can generate fewer tokens, thus saving computational resources and time. 

2. Post-verification: In this phase, the draft model generates additional draft tokens while the target model verifies the previously drafted tokens. This allows for a more continuous flow of token generation and verification. By enabling the draft model to produce more tokens during the verification phase, PEARL capitalizes on situations where the target model is actively processing the earlier drafts. This strategy ensures that the draft model is not idle while waiting for the target model to complete its verification, thus maximizing throughput.

### Strengths
The paper is clearly written and provides several contributions: 

1. PEARL allows the drafting and verification phases to occur simultaneously

2. Instead of using a fixed draft length, PEARL adapts the number of draft tokens generated based on the context and complexity of the task. This flexibility ensures that the draft model generates an appropriate number of tokens, reducing unnecessary computations and improving the acceptance rate of tokens by the target model. This adaptability helps to optimize the inference process for different scenarios.

3. PEARL theoretically demonstrates that it can achieve a higher mean number of accepted tokens compared to existing draft-then-verify methods. This means that more of the generated tokens are useful, leading to better performance overall

### Weaknesses
The author claims that they can continue doing draft generation while doing the verification. This raises many questions:

1. The latency of verifying a 70B model is about generating 2.5 tokens on the 8B model. Based on the speedup that the authors provided, this parallel approach would not work beyond a lookahead length of 3, which is shown to be suboptimal empirically. Therefore it is not clear how much this post-verify step improves the performance. Specifically, the authors do not address the fundamental constraint that the verification latency of the target model limits the potential gains from parallel draft generation. The draft model will inevitably stall if it generates tokens faster than the target model can verify them, making the post-verification strategy's effectiveness questionable beyond very short lookahead lengths.

2. Some parameters are underspecified in the tokens accepted per second table (Table). It is not clear under what lookahead length are the baseline numbers achieved, or if they are optimal. The lack of clarity regarding the baseline parameters makes it difficult to assess the true performance gains of the proposed method. Without knowing the specific lookahead lengths used for the baseline, it's impossible to determine if the comparison is fair or if the baseline results are themselves sub-optimal.

3. The authors picked pipeline parallelism for their implementation. However, while this is a convenient setup for solving the "resource contention" challenge, this is an unreasonable setting and introduces much higher latency in the first place. In deploying a 70B target model with a 7B draft model, using tensor parallelism (TP) can reduce the latency of the target model by leveraging more parallelism in each layer. Therefore, this casts doubt on all the speedup that the authors reported as this causes both the baseline and their reported results to be slower than in a TP setup. Also, with TP, the proposed solution to resource contention in Appendix E would not apply and it is not clear whether the authors can show a similar speedup with their algorithm. The choice of pipeline parallelism (PP) over tensor parallelism (TP) is a significant limitation. PP introduces substantial overhead due to the need to transfer activations between devices, which is not an issue with TP. This overhead would artificially inflate the reported speedups, as the baseline is also affected by PP's inefficiency. The authors' method may not be effective in a more realistic TP setting.

4. Furthermore, using PP instead of TP causes a higher activation memory footprint, reducing the effective batchsize the model can accommodate during decoding, effectively reducing the overall throughput. The increased memory footprint of PP compared to TP is a critical concern. The larger activation memory requirements of PP limit the batch size that can be used during decoding, which directly impacts the overall throughput. This limitation is not adequately addressed and further undermines the practical applicability of the proposed method.

### Questions
My concerns are raised above.

### Soundness
3

### Presentation
3

### Contribution
3
