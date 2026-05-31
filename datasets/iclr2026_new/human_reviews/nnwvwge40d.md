## Human Reviewer 1

### Summary
This paper introduces VeriFree, a method that extends R1-Zero-style reinforcement learning to general-domain, non-mathematical reasoning by using the model's own probability of the ground-truth answer as the reward signal, thereby eliminating the need for explicit verifiers. The authors evaluate VeriFree on broad reasoning benchmarks akin to GeneralReasoner and show that it outperforms a strong LM-based verifier baseline.

### Strengths
- The method is simple yet effective, offering a clear mathematical derivation and concise comparisons with existing algorithms.
- By tackling general-domain reasoning rather than confining itself to mathematics, this work addresses a pressing gap and distinguishes itself from the current wave of math-only RL studies.

### Weaknesses
- The VeriFree method uses implicit reward induced by model confidence, which is unavoidably an imperfect measure. Where budget is unconstrained, practitioners will still prefer a heavyweight but higher-fidelity verifier; the method therefore does not raise the performance ceiling of RL reasoning, it merely lowers the cost floor to some extent.
- All reported experiments rely on single-word or short-phrase ground-truth answers; leaving open the critical question of whether the method can be applied to problems with long answers and coding tasks.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper proposes VeriFree, a verifier-free methodology for general reasoning tasks beyond rule-based verification. The authors explicitly test VeriFree on a variety of domains such as economics, chemistry, and health (among others) to examine performance on multi-task understanding, and `graduate student level reasoning'. In addition, for the case when there is exactly one correct answer to questions, the authors provide theoretical analysis demonstrating that the approach of VeriFree has lower variance than methods which use a verifier, including reinforcement learning with verified rewards (RLVR).

### Strengths
(+) The paper presents an interesting approach to bypass the need for verification for more general reasoning tasks that might not be rule-based. 

(+) The claims are supported by analysis (for one specific setting- also see Weaknesses, below) and experimental evaluations. 

(+) The performance of VeriFree is comparable to verifier-based methods on a large variety of tasks, providing a promise of improved computational efficiency resulting from eliminating reliance on a strong verifier. 

(+) Sec. 2.3 comparing the gradient estimator in VeriFree to estimators from alternate approaches offers particularly helpful and revealing insight into the working of VeriFree (for the single correct answer setting).

### Weaknesses
(-) The authors claim that VeriFree is the first verifier-free methodology for this class of problems. It is not clear if benchmarking against verifier-based methods only adequate. 

(-) What does `rule-based answer verification’ exactly mean? It is reasonable to conjecture that some of the domains mentioned might support rule-based answer verification (e.g., based on statutes of laws). This question becomes even more relevant since the authors state in the Limitations (in the Appendix) that VeriFree is constrained by its dependency on question-answer pairs for supervision. 

(-) It is not clear if the single answer assumption is a reasonable one to make for domains beyond rule-based verification. Specifically, one would assume the potential ambiguities in answers to questions in these domains is a characteristic that has necessitated use of a verifier. 

(-) From Fig. 1, the claim of VeriFree surpassing instruct models and models tuned with a specialized LLM verifier are somewhat strong, given that the accuracy numbers in the bar graphs for VeriFree are only very marginally higher in 5 out of 6 graphs and comes in second best in one graph. At best, one can conclude that VeriFree matches the accuracy performance of these models. 

(-) In Line 107, the paper claims that VeriFree is simpler, faster, less memory-intensive, and more robust than verifier-based alternatives. It is not clear which experiments in the paper correspond to evaluations of memory intensiveness and robustness. 

(-) In Tables 1 and 2, it is not clear to me how the quantity in the Avg column is computed. Checking the numbers, it does not appear to be equal to the mean (average) of the numbers in the same row in the columns on the right. For example, in Table 1, for Qwen3-8B Base-VeriFree, the Avg reported is **67.2**, while **mean(71.5,85.3,73.5,…,45.6) = 66.3**. If it is indeed the case that the Avg should correspond to the mean of the entries in the same row, then this discrepancy extends to many of the other numbers in both tables. 

(-) While VeriFree performs better when looking at the average accuracy, for the 4B experiments in Table 1, VeriFree obtains a higher accuracy than Verifier in only 8 out of 14 domains. Similarly, for the 8B experiments in Table 2, VeriFree obtains higher accuracy that Verifier in only 7 out of 13 domains. 

(-) Minor typo: Line 183 - marginalizes —> marginalize.

### Questions
The authors' comments on the points raised in the Weaknesses section, above, will be helpful.

### Soundness
2

### Presentation
3

### Contribution
3

### Rating
2

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper propose a novel VeriFree framework that bypass answer verification and assign rewards according to the probability of generating reference answer.

Unique answer assumption might not hold generally.

### Strengths
1. The proposed VeriFree framework is simple to implement and bypass the need of verifiers.
2. Experimental results demonstrate that VeriFree achieves comparable results to the verifier-based baseline and shows good transferable reasoning skill gains.

### Weaknesses
1. Evaluation reliability: Single run pass@1 results are too noisy for small benchmarks like MATH-500, Minverva etc. The author might have to report Avg@k and other statistics for robust demonstration.
2. Missing baselines: many existing probability- or frequency-based baselines are missing, such as TTRL.
3. The assumption that only single accurate answer exists might be problematic due to the flexibility of language (e.g., 'A is larger than B' and 'B is the smaller one'). The author might need to conduct more analysis on this assumption.

### Questions
1. Does VeriFree performs better than existing methods that rely on verifiers such as DAPO and ORZ. As RLVR exhibits good generalization capability, could it be possible that training on mathematical problems can yields better results?
2. How does VeriFree works on other model families, considering the data contamination risk of Qwen3 model family.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
3

---

## Human Reviewer 4

### Summary
The paper proposes an RL framework called VeriFree, which extends the R1-Zero paradigm (DeepSeek-R1-Zero) to general reasoning tasks without requiring explicit verifiers. Existing methods like RL with verifiable rewards (RLVR) rely on rule-based or model-based verifiers (often another LLM), which are infeasible for open-ended domains such as law, medicine, or economics. VeriFree addresses this by eliminating the verifier entirely while preserving the core benefits of RL-based fine-tuning. In R1-Zero-style training, a model generates a reasoning trace (z) and a final answer (y). A verifier gives a reward = 1 if y matches the reference answer y*, else 0. VeriFree reformulates this process: instead of relying on a verifier, it directly maximizes the model’s probability of generating the reference answer. The resulting gradient estimator combines: (a) a reasoning term weighted by the model’s likelihood of producing the correct answer, and (b) a supervised term weighted by the same likelihood.

This makes it equivalent in expectation to RLVR under single-correct-answer cases but with lower gradient variance (proved via Rao-Blackwellization). The approach integrates variance reduction (RLOO) and tokenization-aware patching to ensure stable optimization.

For experimental evaluation, Qwen3 (1.7B, 4B, 8B) base models are fine-tuned with VeriFree using the Oat framework. Benchmarks used are MMLU-Pro, GPQA, SuperGPQA (for general reasoning) and MATH-500, OlympiadBench, Minerva Math, GSM8K, AMC, AIME24 (for mathematical reasoning). On MMLU-Pro and SuperGPQA, VeriFree matches or surpasses verifier-based RL baselines while being simpler and more compute-efficient. The accuracy gains are +12-40% over base models, and it achieves faster convergence and higher final accuracy than verifier-based RL.

### Strengths
- The paper is very well-written and structured well. 

- The concept of verifier-free RL eliminates reliance on rule-based or LLM verifiers, making RL training scalable to open-ended reasoning domains. Further, it is derived directly from the RL objective; proven equivalence to RLVR under certain assumptions with formal variance reduction.

- Strong empirical results: Matches or surpasses verifier-based methods across multiple benchmarks while being simpler, faster, and less memory-intensive. The proposed method demonstrates reasoning transfer to unseen domains and improved convergence behavior.

### Weaknesses
- In Tables 1 and 2, it is unclear why the accuracy of Qwen3-4B-Base-Verifier is lower than that of Qwen3-4B-Base-VeriFree. In VeriFree, the LLM output is first parsed into reasoning tokens and a generated final answer (y). Then, the generated answer is replaced with the gold-standard final answer (y⁎). If only one answer (y⁎) is correct and receives a reward of 1 (while all others receive 0), then the expected reward for a reasoning trace z can be computed directly as the probability assigned to y⁎, effectively marginalizing out y. In contrast, when using a verifier, y⁎ will receive a reward of 1 from the verifier, but all other correct answers (for questions with multiple valid answers) will also receive a reward of 1. Conceptually, this should make the verifier-based approach perform better than VeriFree, as it trains the model to obtain a reward of 1 for all correct answers rather than a single reference answer.

- The paper mentions that "when multiple valid answers exist, we show empirically that using just one as a reference provides a sufficient learning signal to elicit strong reasoning behavior."" However, it is not clear why this should be the case. In the VeriFree framework, the model is trained to maximize the reward only for a single correct answer.

- The theoretical equivalence holds only when there is a unique correct answer, limiting its applicability to open-ended or multi-valid-response tasks. In such cases, the model may overfit to the reference answers instead of exploring diverse reasoning paths, thereby reducing interpretability.

- For the baseline, it is unclear why a model-based (i.e., LLM-judge) reward model was used. For math and code tasks, rule-based or test-case-based evaluation is feasible and far more reliable than an LLM judge. The paper claims that VeriFree demonstrates strong transfer to math benchmarks; therefore, for math- or code-specific benchmarks, a stronger rule-based verifier should have been used as a baseline.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4