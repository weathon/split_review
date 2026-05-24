Now I have all the information I need. Let me compile the final review.

---

## Summary

This paper proposes **Steady Thought (ST)**, a thought-level preference optimization framework to mitigate "under-thinking" in Large Reasoning Models (LRMs) — the tendency to prematurely abandon promising reasoning paths for wasteful thought switching. ST operates in three stages: (1) entropy-based segmentation of reasoning traces into individual thoughts, (2) forced thought completion via trigger-token suppression to generate self-supervised preferred continuations, and (3) a SimPO-inspired length-normalized preference optimization loss (STPO) applied at thought boundaries. Experiments across three model scales (1.5B, 8B, 14B) and four benchmarks show consistent accuracy improvements (up to 5.3%) alongside token reductions (17.3–25.5%), with generalization to out-of-distribution code tasks.

## Strengths

- **Clear formalization of under-thinking as a preference problem**: The paper models under-thinking through a Bradley-Terry framework with a latent "steadiness score" (Section 2.1, Eq. 2), instantiated via the model's own conditional log-probabilities. This provides a principled foundation for the subsequent method.

- **Well-designed three-stage pipeline**: The integration of entropy-based thought segmentation, forced completion via trigger-token suppression, and fine-grained preference optimization is coherent and each stage has a clear purpose. The approach is more selective than prior global-suppression methods (NOWAIT, SEAL), preserving the model's ability to explore when needed while encouraging commitment when a thought shows promise.

- **Strong empirical results across diverse settings**: ST improves accuracy while simultaneously reducing token counts across three model sizes (DeepSeek-R1-Distill-Qwen-1.5B, Qwen3-8B, DeepSeek-R1-Distill-Qwen-14B) and four benchmarks (MATH-500, AIME 2024, GSM8K, LiveCode). The LiveCode results are particularly notable as an out-of-distribution test — models were trained only on math data, yet ST improved Qwen3-8B's code accuracy by 5.3% with 19% token reduction, suggesting genuine behavioral change rather than dataset memorization.

- **Convincing ablations**: The training method comparison (Table 4) shows STPO outperforms SFT and DPO. The entropy threshold ablation (Table 3) demonstrates a U-shaped trade-off and justifies the chosen value. The thought-level behavioral analysis (Table 2, Figure 2) provides evidence that ST reduces unnecessary switching and deepens exploration of promising thoughts.

## Weaknesses

### Fatal

None.

### Major

- **Unvalidated thought segmentation**: The entire framework depends on segmenting responses into meaningful "thoughts" via a combination of `".\n\n"` pre-segmentation and entropy-threshold-based switch detection. No human validation, oracle comparison, or qualitative examples are provided to assess whether the resulting segments correspond to coherent reasoning units. Different reasoning models have different output formats, and it is unclear how reliably the heuristic generalizes. If segmentation is noisy, the subsequent thought completion and preference pairs may encode spuriously broken or merged reasoning steps. The paper provides indirect validation through downstream performance and the threshold ablation (Table 3), but this does not directly verify segmentation quality. A small-scale annotation study or qualitative analysis would substantially strengthen the claim of operating at a true "thought level."

- **Under-specified data construction**: The creation of preference pairs is described only in high-level terms. Specifically: (a) the rule for selecting which thought \(T_i\) to complete ("When we identify a promising thought \(T_i\)") is never made precise — are all correctable thoughts used, only the first one, or some heuristic? (b) no statistics are reported on the training set (number of pairs, fraction of completions that yield correct answers, distribution of thought positions selected). (c) the trigger-word suppression mechanism's implementation details (magnitude of logit reduction, whether applied throughout completion or only at the start) are absent. These gaps make the method difficult to reproduce and obscure possible biases in the training data construction.

### Minor

- **Lack of statistical rigor in main results**: The paper reports averages of 8 runs for AIME 2024 and 2 runs for LiveCode, but does not specify the number of runs or report variance for MATH-500 and GSM8K. No standard deviations or confidence intervals are reported anywhere. The decoding protocol (temperature, sampling vs. greedy) is never specified for evaluation. While single-run evaluation on large fixed test sets is not unusual in this subfield, the inconsistency across benchmarks and absence of any variance estimates weakens confidence in the modest accuracy gains (e.g., +1.1% on GSM8K for Qwen3-8B, +2.0% on MATH-500 for the 1.5B model).

- **PCT metric circularity**: The "percentage of correct thoughts" metric (Table 2, Section 4.4.2) uses the same segmentation and completion pipeline (Sections 3.1 and 3.2) that ST was trained with. The metric is therefore confounded with the method itself — it is not an independent measure of thought-switching behavior. The paper should acknowledge this circularity; the observed decrease in PCT (e.g., 73.18% → 67.74% for Qwen3-8B) may partly reflect that ST-trained models produce outputs that are easier for ST's own segmentation to classify as having fewer switches, rather than genuinely switching less.

- **Per-model entropy threshold tuning**: The segmentation threshold is tuned separately per model (shown for the 1.5B model in Table 3; appendix results for others). The need for per-model threshold search, chosen based on downstream test performance, raises overfitting concerns and limits practical applicability. The U-shaped pattern in Table 3 suggests the optimal threshold is performance-metric-dependent, and the paper lacks a principled criterion for setting it without test-set access.

- **Decoding protocol unspecified**: The paper never states whether evaluation uses greedy decoding, temperature sampling, or another strategy. This matters for reproducibility and for interpreting the token-count reductions.

### Trivial

- The choice of `".\n\n"` as the pre-segmentation delimiter is not justified; its generality across model output formats is undiscussed.
- The SFT baseline's underperformance relative to vanilla (22.9% vs. 27.5% on AIME for the 1.5B model, Table 4) is attributed to "memorization" without analysis — a speculative explanation.

## Nice-to-Haves

- A comparison against a training-based length-control method (e.g., L1 from Aggarwal & Welleck, 2025, which the paper cites) would strengthen the claim that ST's gains are not merely due to any length-penalty training.
- The main text should summarize the computational overhead of the thought completion stage (currently deferred to Appendix E, which is unavailable to the reviewer).
- A discussion of why NOWAIT catastrophically fails on Qwen3-8B (61% accuracy on MATH-500, +84.6% tokens) while ST succeeds, given that both suppress similar trigger words at some stage, would be informative.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic: "The table's formatting is garbled in the PDF"** — this is a parser artifact, not an author error. The original submission does not have this issue. REMOVED.

- **Harsh Critic: "The paper defers [computational cost] discussion to an appendix that is unavailable to the reviewer"** — the appendix exists in the original submission; the parser strips it. Cannot fault the paper for missing appendix sections the parser removed. Moved to Nice-to-Haves as a suggestion to summarize in main text.

- **Harsh Critic: "The authors must run each experiment with a sufficient number of seeds (e.g., at least 3–5) on all datasets"** — this is a reasonable suggestion but framed too strongly. Single-run evaluation on fixed test sets like MATH-500 and GSM8K is standard in the field. Kept as Minor but softened from the harsh critic's "fundamental evidential weakness."

- **Harsh Critic: The NOWAIT catastrophic failure is presented as a weakness of ST** — this is not a weakness of ST; it's a baseline behavior that actually supports the paper's motivation (global suppression is harmful). REMOVED from weaknesses; moved to Nice-to-Haves as a discussion suggestion.

- **Harsh Critic: Missing related work, missing limitations section, missing parts** — the parser strips the appendix and some sections. Cannot verify. REMOVED.

- **Strength Finder: "The problem is important" type generic strengths** — REMOVED as generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The core insight — that under-thinking can be modeled as a preference problem and addressed through thought-level rather than global intervention — is the paper's novel contribution.

## Suggestions

- Provide a small-scale human evaluation of thought segmentation quality (e.g., inter-annotator agreement on 50–100 traces), or at minimum qualitative examples comparing entropy-based segmentation against a fixed-rule baseline, with discussion of failure modes.
- Specify the thought-selection rule precisely, report training set statistics (number of pairs, fraction of correct completions, position distribution of selected thoughts), and include an algorithmic description of the data construction loop.
- Add variance estimates for all main results and specify the decoding protocol used for evaluation.
- Discuss the circularity in the PCT metric and, ideally, provide an alternative measure of switching behavior that does not rely on the ST pipeline.

## Score and Decision

### Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Supervised CoT | pXIbcRPxWR | 2.50 | R1 (weak) | Much weaker — descriptive study, no method |
| Planning in Strawberry Fields | jOuHjFw71C | 3.00 | R1 (weak) | Weaker — evaluation-only paper |
| Reward Learning with Ties | fTdhM7q1o2 | 3.00 | R1 (weak) | Different domain, narrower scope |
| MCTS Planning | sdpVfWOUQA | 3.00 | R1 (weak) | Weaker — limited evaluation, less novelty |
| Mind Your Step | rpbzBXdo4x | 5.00 | R1 (mid) | Weaker — significant experimental design issues |
| LD-DPO | CuwjD3cazX | 5.00 | R1 (mid) | Weaker — heuristic solution, hyperparameter sensitivity |
| PrefOpt for Combinatorial | 8QkpCRio53 | 5.75 | R1 (mid) | Different domain, less relevant |
| SCDPO | ZRDa2IT1sQ | 6.00 | R2 (narrow) | Weaker — narrower eval, known-similar to prior work |
| 3D-Properties | 9Hxdixed7p | 6.25 | R2 (narrow) | Comparable but narrower scope |
| TPO | O0sQ9CPzai | 6.33 | R1+R2 | Closest anchor — similar scope; ST has broader eval and OOD results |
| A Little Goes a Long Way | TrKRpaOk8y | 6.40 | R2 (narrow) | Different domain, but similar quality tier |
| TokenFormer | oQ4igHyh3N | 7.50 | R2 (wide) | Stronger — more novel architecture contribution |
| Transformers Provably Solve Parity | n2NidsYDop | 8.67 | R1 (strong) | Much stronger — theoretical work with formal guarantees |
| Safety Alignment | 6Mxhg9PtDE | 9.50 | R1 (strong) | Much stronger — deep analysis with broad impact |

**Round 1 Bracket**: 5.5–7.0. The paper is clearly above the weak band (2.5–3.0) and the lower-middle band (LD-DPO at 5.0, Mind Your Step at 5.0) but below the strong theoretical/impact papers (7.5+).

**Round 2 Narrowing**: Compared against SCDPO (6.00), 3D-Properties (6.25), and TPO (6.33). SteadyThought is stronger than SCDPO (broader evaluation, more complete method) and comparable to or slightly better than TPO (which also does preference optimization for reasoning but tests on fewer model types and lacks OOD evaluation). The dual improvement (accuracy + length reduction) and the OOD generalization to code are distinguishing positives, while the unvalidated segmentation and under-specified data construction are real but addressable concerns.

**Final Score**: 6.5. The paper makes a clear, well-motivated contribution with strong empirical results across diverse settings. The methodological gaps (unvalidated segmentation, under-specified data construction, missing variance estimates) prevent a higher score but do not invalidate the core claims. The paper is stronger than TPO (6.33) due to broader evaluation and OOD generalization but falls short of the 7.5+ tier due to the segmentation validation gap and statistical rigor issues.

Overall assessment: The paper is original in framing under-thinking as a preference optimization problem and designing a thought-level intervention rather than global suppression. The research question is important for the efficient deployment of reasoning models. The claims are well-supported by experiments across multiple model scales and benchmarks, though statistical rigor could be improved. The writing is clear and well-structured. The method offers practical value to the community working on reasoning model efficiency.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>