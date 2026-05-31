## Human Reviewer 1

### Summary
This paper presents **SWiReasoning**, a training-free framework that dynamically switches between **explicit (token-based)** and **latent (hidden-space)** reasoning based on entropy-derived confidence trends. A switch-count control prevents overthinking, improving both accuracy and token efficiency. Across multiple math and STEM reasoning benchmarks (GSM8K, Math500, AIME24/25, GPQA) and three reasoning LLMs (Qwen3-8B, Qwen3-1.7B, DeepSeek-R1), the method yields +1.5–2.8% Pass@1 improvement and up to +80% token efficiency gains without retraining.

### Strengths
- **Practical and training-free**: Improves reasoning efficiency entirely at inference time.  
- **Comprehensive experiments**: Consistent gains across models and reasoning benchmarks.  
- **Well-analyzed switching mechanism**: Includes ablations on window size, confidence, and signal mixing.  
- **Clear motivation**: Tackles overthinking and token inefficiency in CoT reasoning.

### Weaknesses
- **Moderate novelty**: Combines existing ideas (latent reasoning + token control) with minor algorithmic extensions.  
- **Pipeline complexity**: The overall system involves multiple heuristic components (entropy tracking, switching windows, signal mixing), making the pipeline heavy and less theoretically elegant.  
- **System-oriented nature**: The contribution is more of a practical inference-time system design than a fundamentally new reasoning principle.  
- **Marginal improvement**: Accuracy gains are modest given the added complexity.

### Questions
1. How robust is the entropy-based switching to unseen data or noisy prompts?  
2. Could the switching mechanism be learned rather than manually tuned?  
3. How does this compare to dynamic decoding methods such as COCONUT or Long⊗Short?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
3

---

## Human Reviewer 2

### Summary
The paper proposes SWIREASONING, a training-free framework that dynamically switches between explicit and latent reasoning based on entropy-driven confidence signals in the next-token distribution. The key idea is that staying purely in latent space can diffuse probability mass and cause slow or noisy convergence, so the model alternates modes to balance exploration and exploitation. A second mechanism caps the number of thinking-block switches to reduce “overthinking” and save tokens. The authors conduct some experiments and show the performance.

### Strengths
1.	The paper proposes a method that flexibly combines latent reasoning with explicit reasoning, effectively reusing intermediate embeddings as inputs to enable denser thinking steps.
2.	The authors provide experiments on several standard reasoning benchmarks to demonstrate the applicability of the approach.

### Weaknesses
1.	The overall performance gains are relatively small, and the efficiency story is not fully convincing — a clearer, more direct metric is needed, and Appendix Table 8 suggests that long generations are still required to reach good accuracy.
2.	The paper should further explain why switching between latent and explicit modes improves performance, and clarify whether (and how) the latent trajectories can be decoded or inspected in text for interpretability.
3.	The experimental scope is limited; results on larger models and on other task types (e.g., coding), where latent reasoning may be less naturally applicable, would make the empirical claims more convincing.

### Questions
Please chek the weakness

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
5

---

## Human Reviewer 3

### Summary
This paper introduces SwiReasoning, a training-free framework for improving reasoning in large language models by dynamically switching between explicit chain-of-thought (CoT) and latent reasoning modes. The core innovation lies in using entropy trends from next-token distributions as block-wise confidence signals to guide mode transitions: when confidence increases (entropy drops), the system switches to explicit reasoning to consolidate progress; when uncertainty persists (entropy rises), it switches to latent reasoning for exploration. Additionally, a switch count control mechanism limits the maximum number of mode transitions and enables early answer generation at natural checkpoints, suppressing overthinking and improving token efficiency.

### Strengths
1. The insight that reasoning should adaptively switch based on confidence is intuitive yet underexplored in training-free settings, thereby making the idea and approach of the paper novel. 

2. The evaluation is comprehensive and spans multiple model families, scales (1.7B–8B parameters), training paradigms, and five diverse benchmarks. The consistency of improvements across all settings (13 out of 15 evaluations achieve highest token efficiency) provides strong empirical support.

3. The methodology is well-structured with intuitive explanations, formal algorithmic descriptions (Algorithm 1), and effective visualizations (Figures 1–5). The paper is well written.

### Weaknesses
Enumerating a few weaknesses here

1. While the convergence and termination triggers are intuitive, the specific thresholds (½Cmax for convergence, Cmax for termination) appear arbitrary. Why these specific fractions? How sensitive is performance to these choices? The paper doesn't ablate these design decisions.

2. Limited failure case analysis and the modes of failure. It would be good to add the cases or categories of questions where the proposed approach fails. 

3. The results reported for soft thinking approach appear to be lower than standard CoT, which is contrary to the claims in the original Soft-thinking paper. This raises concerns about implementation correctness and whether comparisons are on equal footing.

### Questions
1. How is entropy computed during latent steps when no explicit token is selected? Is it from the softmax over the last hidden state projected through the LM head?

2. In ablation Table 3, window size 512 is optimal. Given typical generation lengths (e.g., ~2000 tokens for GSM8K), does this mean most problems only switch 2–4 times? If so, is this really "dynamic" switching, or just a staged approach (latent -> explicit -> latent -> explicit) Can you show histograms of actual switch counts across problem difficulties?

3. The paper claims "Pareto-superior" results. However, in some cases (e.g., AIME24 in Fig. 4), CoT appears to match or exceed SwiReasoning's accuracy at similar token budgets. Can you clarify where strict Pareto dominance holds vs. where there are trade-offs?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper proposes SwiReasoning, a training-free framework for LLM reasoning that dynamically switches between explicit chain-of-thought and latent reasoning modes. The switching is guided by block-wise confidence estimated from entropy trends in next-token distributions. The method also includes a switch count controller to suppress overthinking and improve token efficiency. Experiments on mathematical and STEM benchmarks show consistent accuracy improvements and token efficiency gains across different model families and sizes.

### Strengths
- The idea of dynamically switching between explicit and latent reasoning based on confidence signals is intuitive and addresses limitations of pure latent reasoning approaches.
- The experimental evaluation is comprehensive across multiple models and benchmarks, including various token budget settings and Pass@k analysis that shows the method overall improves the performance with better efficiency.
- The ablation studies analyze key design choices and provide insights into how different components contribute to performance.

### Weaknesses
- The method introduces many heuristic design choices and hyperparameters (window sizes W_E→L and W_L→E, signal mixing coefficients α₀ and β₀, switch count limits C_max, convergence/termination triggers), and it appears from the ablations that these are tuned on the test sets, which raises concerns about generalization and fair comparison.

- It seems unclear whether the latent reasoning mode genuinely enables the claimed "exploration" of multiple reasoning paths, since Soft-Thinking simply weights tokens by probability, and the pretrained LLM likely still concentrates probability mass on similar natural language tokens. It would be beneficial to provide some analysis of the probability distributions within the latent tokens or other evidence that meaningful exploration is occurring beyond what explicit sampling would achieve.

- There are quite a few citations that are wrong and appear to be LLM-hallucinated, even including the most important "Soft-Thinking" paper that this work is primarily built on top of - the citation in the draft is ```Bowen Zhang, Yanzhuo Li, Shuohang Wang, Yu Tu, Jason Wei, Ashish Vaswani, Shikun Liu, Chenlu Yu, Deli Chen, Hongyi Li, Zhihua Zhang, and Chen Liang. Soft thinking: Training-free
latent reasoning for large language models.``` while the actual one should be ```Zhen Zhang, Xuehai He, Weixiang Yan, Ao Shen, Chenyang Zhao, Shuohang Wang, Yelong Shen, Xin Eric Wang. Soft Thinking: Unlocking the Reasoning Potential of LLMs in Continuous Concept Space```.

### Questions
See weaknesses.

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

## Human Reviewer 5

### Summary
Summary
This paper introduces SWIREASONING, a training-free reasoning approach that integrates latent and explicit chain-of-thought (CoT) modes. Instead of committing to token-level reasoning at every step, the method forms latent reasoning states via weighted token embeddings, allowing the model to retain uncertainty and explore multiple hidden trajectories.
A block-wise entropy reference is used as a switching criterion: when the entropy decreases (confidence rises), the model switches from latent to explicit reasoning immediately; when entropy increases, switching from explicit back to latent requires a dwell window to prevent oscillation. To signal mode transitions more explicitly, the method injects fused embeddings of  < think > / </ think > tokens during switch steps.
Additionally, switch counters and termination triggers are employed to avoid unbounded “over-thinking” and encourage timely final answer production.
Experiments show that, particularly for smaller models (≤8B) and token-budget-constrained settings, SWIREASONING delivers higher reasoning accuracy and efficiency compared to standard CoT and soft-thinking baselines. Ablation studies on signal mixing and dwell window length further support the design choices.

### Strengths
1. The approach does not require model updates and can be applied directly at inference time, making it practical for deployment on existing models.
2.The entropy based switching between latent and explicit reasoning, combined with a dwell window to avoid oscillation, is conceptually simple and computationally lightweight.
3. The method shows consistent gains over standard CoT on math reasoning benchmarks, particularly for ≤8B models under constrained token budgets, with ablation studies supporting key design choices.

### Weaknesses
1. Latent reasoning contribution unclear at small budgets
In short-budget settings, the method typically switches to explicit mode immediately and does not enter latent reasoning due to the dwell window. Yet it still outperforms CoT, suggesting the improvements largely come from early confidence-based stopping and < think >/< /think > embedding conditioning rather than latent reasoning itself. Ablation isolating these effects would clarify the true source of gains.
2. Scope limited to math-focused tasks
Experiments are concentrated on math reasoning, and it remains unclear whether the method benefits broader domains (e.g., multi-hop QA, code, commonsense reasoning). Reasoning dynamics can differ significantly across tasks.
3. Large-model scaling and SoftThinking baseline discrepancy
The original SoftThinking results indicate improvements over CoT primarily for ≥32B models. Here, the reproduced SoftThink baseline is weaker than CoT on ≤8B models. Given that SwiReasoning is training-free, extending evaluation to ≥32B models would help verify baseline fidelity and clarify whether the proposed method scales beyond the small-model setting.
Heuristic hyperparameters + no runtime reporting
4.Heuristic switching and lack of runtime analysis
The switching logic, dwell window, and mixing schedule are manually designed. While intuitive, their tuning behavior across models and tasks remains unclear, and no wall-clock or FLOP analysis is provided, making deployment efficiency uncertain.

### Questions
1 In small budget settings, the model often does not actually enter latent mode due to the dwell window, yet achieves strong gains. Can you provide ablations where latent reasoning is disabled but the early-exit and <think> conditioning remain, to isolate the effect of latent reasoning itself?

2 Token efficiency does not necessarily imply inference-time efficiency. Can you report wall-clock latency or FLOPs vs CoT and SoftThinking to demonstrate practical gains?

3 The SoftThinking baseline underperforms CoT in your ≤8B experiments, whereas the original paper shows gains mainly at ≥32B scale. Can you confirm your implementation matches the original, and provide results on a ≥32B model to ensure fairness?

4 Could you clarify whether your latent update uses the full vocabulary distribution or a top-k truncation (as in SoftThinking)?

5 Could you provide a systematic component-wise ablation (turning each mechanism on/off) to quantify the marginal contribution of:  (i) dwell window (incl. 0) and asymmetry, (ii) < think >/< /think > mixing, (iii) switch-count cap/termination triggers。

### Soundness
3

### Presentation
4

### Contribution
2

### Rating
2

### Confidence
4