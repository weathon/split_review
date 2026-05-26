Now I have a complete picture of the paper. Let me produce the consolidated review.

## Summary

This paper identifies and systematically addresses the problem of output length volatility in long-form LLM generation — the tendency for repeated runs to produce wildly different output lengths. The work unfolds in three stages: (1) **VOLTBench**, a multi-dimensional benchmark covering structured/unstructured tasks across languages, complexities, and scales up to ~100k words, with formal volatility metrics (LVC, LSD, MLA, FAD); (2) an **attention trace analysis** that identifies two internal patterns (Attention Collapse, Attention Instability) linked to volatility; and (3) **SELB** (Structural Enforcement via Logits Boosting), a training-free decoding-time intervention that boosts next-section tokens and suppresses known failure-mode tokens. Results show SELB substantially improves length adherence (MLA 78.25%) and reduces volatility (LVC 14.02%) compared to strong baselines.

## Strengths

- **VOLTBench is the first benchmark purpose-built for output volatility in long-form generation.** Table 1 directly contrasts VOLTBench against seven existing benchmarks (HelloBench, LongGenBench, LifeBench, etc.), showing it is the only one that jointly covers "Multiple Sampling" and "Stability Eval." The formal metrics (LSD, LVC, MLA, FAD) defined in §3.2 provide a reproducible, quantitative framework for an overlooked phenomenon. The benchmark's multi-dimensional design (language, complexity, structured/unstructured tasks, scaling from 5 to 500 chapters) goes beyond prior work.

- **SELB achieves concrete, large-magnitude improvements in length accuracy and stability.** On the 100-section task with a 20k-word target, SELB achieves 15,651 mean output words, 78.25% MLA, and 14.02% LVC (§6.3). These represent substantial gains in both reaching the target length and reducing cross-run variability compared to baselines (e.g., LongWriter-8B: 6,320 words, 31.6% MLA, 45.4% LVC). The generalization to free-form generation (§6.4) — where SELB-Hybrid achieves 97% MLA and 12.1% LVC on a 20k-word novel task — further demonstrates the method's practical reach beyond rigid structured outputs.

- **The attention trace methodology (§5) provides a well-defined formalism** for computing constraint-focused attention ($\bar{\alpha}^{(t)}$) averaged across layers and heads. This gives a concrete tool for probing the relationship between internal attention dynamics and output behavior, and the identified patterns (Attention Collapse, Attention Instability) are plausible mechanistic hypotheses that future work can build on.

- **The multi-dimensional evaluation design is thorough and includes automated quality metrics.** The use of Execution-based Verification for structured tasks (§3.2) and fine-grained constraint checking (§4.2, §4.3.1) enables objective quality evaluation that reduces reliance on subjective LLM-as-a-Judge scoring. The breadth of models tested (9+ architectures including reasoning models, various sizes, and training-free decoding baselines) provides a useful landscape of the volatility problem.

## Weaknesses

### Fatal
None.

### Major

- **The headline quantitative claims in the abstract and contributions (§1) are misleadingly framed.** The paper claims SELB "improves the mean output length of the base model by 148% and reduces the length volatility by 69%." The underlying numbers (§6.3: 15,651 words, 14.02% LVC) produce these percentages only when compared against **LongWriter-8B** (6,320 words, 45.4% LVC) — a different, specialized model, not the same model without SELB. "Base model" is undefined in context: SELB is a decoding strategy applied to models like Qwen2.5-7B, Qwen3-8B, and Llama3.1-8B (per Figure 5), and the paper never states which model produces the headline numbers nor provides a direct within-model comparison (same architecture with/without SELB). A reader naturally interprets "base model" as the model SELB operates on; the actual within-model comparison for Qwen2.5-7B would show ~3,418% length increase and ~17.5% LVC reduction — completely different figures. This framing ambiguity undermines the paper's central quantitative narrative and requires correction.

- **The attention analysis (§5) does not support the claim of "common internal patterns."** Only two model traces are shown (Qwen2.5-7B and Qwen2.5-3B) on a single task (diary, 40 sections). There is no systematic quantification of how often Attention Collapse or Attention Instability occurs across models, tasks, instruction complexities, or runs. No correlation is computed between any attention-derived metric and output volatility (e.g., LVC). The patterns are described through visual inspection of two plots, and the text's statement that "periodic attention spikes function as essential refocusing signals" goes beyond what the evidence supports. The contributions claim (§1) of "several common internal patterns of length volatility" is not commensurate with the evidence presented.

### Minor

- **The target length ($L_{\text{constraint}}$) for the main 100-section benchmark results is never explicitly stated.** The MLA metric definition (§3.2) requires this value, and Table 2 reports MLA for all models without specifying the target. The value can be back-calculated (20,000 words = 100 sections × 200 words/section, consistent with the observed MLA values), but the paper should state it directly. The task description says "M chapters, N words each" (§3.1) but M and N for the reported experiments are omitted from the main text.

- **The narrative connection between the attention analysis and the SELB mitigation is weak.** SELB (§6) enforces structure via logit boosting and bans conversational filler phrases — heuristics that address *symptoms* of the identified patterns (premature termination, section skipping) but do not directly target or demonstrably fix the underlying attention dynamics. The paper claims SELB "target[s] the identified internal patterns" (§1) but never shows that SELB restores periodic attention spikes or reduces attention instability. The two contributions remain largely decoupled.

- **SELB's evaluation lacks a direct within-model ablated comparison.** Section 6.3 reports results as "our model" without specifying which base architecture was used. While Figure 5 shows SELB applied to multiple models (Qwen2.5-7B, Qwen3-8B, Llama3.1-8B), the textual results (15,651 words, 78.25% MLA) are not mapped to a specific base model, and no table systematically compares each base model with and without SELB under identical conditions. Table 2 provides the without-SELB baselines, but a direct comparison table would clarify the gains.

- **The analysis of generation patterns (§4.3) states failure rates ("approximately half of the cases," "all models failed") without providing precise numerical support** or a formal definition of "failure" for those specific claims. While the qualitative patterns (incomplete generation, section skipping) are well-motivated, the paper would benefit from tabulating exact failure rates per model and per section count.

### Trivial

- The paper references "Figure 6" in §6.3 but the figure numbering in the parsed text runs only through Figure 5, suggesting a cross-reference issue.
- The instruction example (§3.1) uses placeholder variables *M* and *N* without example values, making the task format less immediately concrete.

## Nice-to-Haves

- **Provide confidence intervals or run-level statistics for the volatility metrics (N=5).** While 5 runs per instruction is acceptable for an initial study, reporting bootstrapped confidence intervals on LVC and MLA would strengthen the reliability assessment.
- **Ablation of SELB components.** Controlled experiments with structural enforcement alone, failure prevention alone, and both combined would clarify which design choices drive the gains. Sensitivity analysis on $\tau_{max}$ and $\beta$ would also strengthen the method's credibility.
- **More diverse free-form tasks for SELB-Hybrid.** The generalization results (§6.4) are impressive but limited to one task (20k-word novel) against two baselines. Additional free-form tasks would strengthen the generality claim.
- **Explicit hyperparameter disclosure for the decoding baselines** (repetition penalty value, entropy threshold, length constraint limit) in the main paper rather than deferred to the appendix.

## Removed Points

These points from the inputs were excluded or downgraded after cross-checking against the paper:

- **"The decision to exclude Claude-3.5-Sonnet from quality evaluation is odd"** (Harsh Critic) — Removed. The paper's rationale (176-word mean output is insufficient for long-text evaluation) is reasonable. Short output on a 20k-target task is itself evidence of failure, and excluding it from quality metrics avoids evaluating generation quality on near-empty outputs.
- **"SELB's novelty is limited"** (Harsh Critic, implied) — Removed. Training-free decoding interventions are a legitimate methodological contribution; evaluating novelty is outside the scope of this consolidation.
- **"The paper lacks an explicit limitations section"** — Removed. Many papers do not have one; this is not a substantive weakness.
- **Generic strengths from Strength Finder** (e.g., "the paper addressed an important problem") — Removed per instructions. Only strengths with concrete, paper-specific evidence are retained.

## Novel Insights

Beyond the paper's own contributions, an interesting observation emerges from the combination of the benchmark results and the mitigation: the finding that structured tasks naturally exhibit less volatility (§4.3, Figure 3) suggests that output format rigidity itself serves as a stabilizer — a point that reinforces the logic behind SELB's structural enforcement while also raising the question of whether volatility is primarily a *length-control* problem or an *attention-maintenance* problem. The paper's two attention patterns collapse these into related symptoms, but the interaction between task structure (code, math) and internal attention dynamics is not explored, leaving a natural direction for future work.

## Suggestions

1. **Rewrite the abstract and contributions to clarify what is being compared.** Replace "improves the mean output length of the base model by 148%" with precise language: e.g., "compared to the strong baseline LongWriter-8B, SELB improves mean output length by 148% (from 6,320 to 15,651 words)" — and also report a within-model comparison (SELB applied to Qwen2.5-7B vs. Qwen2.5-7B without SELB) in the same table so readers can see both improvements.
2. **State the target length $L_{\text{constraint}}$ explicitly** in Table 2's caption and in §3.2 when discussing MLA. Provide M and N values for the reported experiments.
3. **Systematize the attention analysis.** Compute an attention-derived metric (e.g., variance of $\bar{\alpha}^{(t)}$ over a sliding window; frequency of "attention summits") and correlate it with LVC across models and tasks. At minimum, acknowledge the anecdotal nature of the current evidence and soften the "common internal patterns" claim to be proportional to the data shown.
4. **Add a direct comparison table** for SELB vs. the same base model without SELB, with the same metrics as Table 2, clearly stating which base model is used.
5. **Provide exact failure rates** (with model-by-model breakdown) for the "approximately half the cases" and "all models failed" claims in §4.3.
6. **Acknowledge the decoupling** between the attention analysis and SELB explicitly, and either strengthen the connection (e.g., by showing SELB's effect on attention traces) or reframe the paper's narrative as two independent contributions rather than a causal chain.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>