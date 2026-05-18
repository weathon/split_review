Now I have all the information needed to produce the consolidated review.

## Summary

This paper proposes MeCo, a method that uses representation probing (RepE) on LLM hidden states to decide when to invoke external tools vs. relying on internal knowledge. It introduces the MeCa benchmark for evaluating tool-use timing decisions. The core idea is to train a probe via contrastive instruction pairs, extract a score from the model's internal representations, and use a dual-threshold strategy to override the model's default Yes/No output about tool necessity. Experiments on Llama-3-8b/70b and Mistral-7b show consistent accuracy improvements over two baselines (first-token and probability-ratio).

## Strengths

1. **Consistent and substantial accuracy gains across models and settings.** Tables 1–3 show MeCo outperforming both Naive and P_Yes baselines on every configuration — multiple backbone models (Llama-3-8b, Llama-3-70b, Mistral-7b), with/without context, pre- and post-fine-tuning, and on both Metatool and MeCa benchmarks. Gains range from +4.5% to +16.8%, supporting the claim that representation-level information improves tool-use timing decisions.

2. **Fine-tuning-free design with demonstrated orthogonality to fine-tuning.** Section 6.1 explicitly shows that MeCo improves fine-tuned models as well (e.g., Llama-3-8b-sft gains +8.5% with context), and the paper observes that fine-tuning degrades on OOD tasks while MeCo's improvements remain robust. This is a practical advantage — the method can be layered on existing pipelines.

3. **MeCa benchmark addresses a gap in evaluation.** Metatool only covers individual-tool queries without context. MeCa expands coverage to six tasks including provided-tool evaluation and multi-turn interaction, plus an adaptive RAG component, all with human verification. This provides a more challenging and ecologically valid test bed for the understudied "when to use tools" problem.

4. **Threshold transferability across benchmarks.** Section 6.1 shows that thresholds fitted on Metatool transfer to MeCa-Tool Tasks 1 and 4 with only minor accuracy drops, suggesting the signal is model-dependent and generalizes across query distributions — a practically useful property.

## Weaknesses

### Fatal
None.

### Major

1. **"Meta-cognition" framing inflates the actual contribution.** The paper defines meta-cognition as "the model's ability to self-assess its own capabilities and limitations" (line 14) and claims MeCo detects this self-awareness. In reality, MeCo trains a probe via contrastive instruction pairs (following RepE) to distinguish whether the model is in a "high meta-cognition" or "low meta-cognition" prompt condition, then uses dual thresholds to override tool-use outputs. The probe does not measure the model's own self-assessment — it measures whether the model's hidden states correlate with an externally imposed distinction (tool-needed vs. not-needed) after being primed with meta-cognitive vs. non-meta-cognitive instructions. This is a learned representation-based trigger policy, not a detection of the model's internal self-awareness. The conceptual framing is misleading: what the paper actually contributes is a representation-based override mechanism for tool-use timing decisions, which is a legitimate contribution on its own terms and does not require the "meta-cognition" scaffolding. Reframing honestly would strengthen the paper.

### Minor

2. **The decision rule is not specified precisely enough.** Sections 3.2 and the caption of Figure 1 describe a dual-threshold strategy (l_yes for "Yes" tokens, l_no for "No" tokens) but never state the exact override logic. Is it: if the model says "Yes" and the probe score < l_yes, override to "No"; if the model says "No" and the probe score > l_no, override to "Yes"? This is the natural reading but the paper should state it explicitly with pseudocode. Without this, reproducibility is unnecessarily difficult.

3. **Limited baseline comparisons.** Only two baselines are compared: Naive (first token) and P_Yes (probability ratio). P_Yes does serve as a de facto confidence-based baseline (it's P(Yes)/(P(Yes)+P(No))), mitigating the reviewer's suggestion to compare against entropy/logit-difference methods. However, comparisons against a simple classifier trained on query embeddings, or against alternative trigger approaches from prior work, would more convincingly establish that the representation-level probe provides unique value beyond simpler alternatives.

4. **No measures of variability.** All accuracy results in Tables 1–3 are reported as single numbers without confidence intervals, standard errors, or any measure of variability. Given that thresholds are fit on subsets (e.g., 100 queries for some MeCa-Tool tasks), the results could be sensitive to the particular train/test split. Bootstrapped confidence intervals would strengthen confidence in the reported improvements.

5. **Computational cost is asserted but not measured.** The paper claims MeCo "incurs minimal cost" (abstract, line 180) but provides no measurement of latency increase, memory overhead, or throughput impact. Since MeCo requires computing probe scores from hidden states at inference time, a quantitative analysis would be important for practical adoption.

6. **Probe training data details are incomplete.** Section 3.1 says "only a small number of queries and responses are enough" but never specifies how many. The exact contrastive prompt templates used for the meta-cognition probe (the experimental T_f^+ and reference T_f^- prompts) are not provided. The pipeline description — proprietary LLM generates queries/responses, then representations are collected from the **target** model (as Rep(M, ...) in Eq. 1 makes clear) — is technically correct but could be much clearer to prevent confusion.

7. **Figure 3 validates the probe on contrastive-pair classification, not on the downstream decision task.** Figure 3 shows that the meta-cognition probe can distinguish held-out contrastive examples (high vs. low meta-cognition prompts), which is a standard RepE sanity check. The actual tool-use decision accuracy is in Tables 1–3, so the paper does have the right end-to-end evaluation — but the presentation of Figure 3 as the primary probe evaluation without linking it explicitly to downstream performance is somewhat disjointed.

### Trivial
None.

## Nice-to-Haves
- Ablation showing sensitivity to the layer selection range (-5 to -2) and whether averaging across multiple layers works comparably.
- Analysis of probe score distributions on failure cases (where MeCo disagrees with the model's default output).
- More detailed characterization of MeCa's domain coverage and difficulty calibration.

## Removed Points
- **Reviewer Point 4 (probe trained on proprietary LLM's representations):** The paper's Eq. 1 clearly shows representations are collected from the target model M (Rep(M, ...)). The proprietary LLM only generates queries and responses; the probe operates on the target model's own hidden states. The specific concern about cross-model transfer of probes is based on a misreading. Kept only the clarity issue as Minor #6.
- **Reviewer claim about missing confidence-based baseline:** P_Yes is P(Yes)/(P(Yes)+P(No)), which is exactly a confidence-based method using token logit ratios. The suggested "logit difference" baseline is essentially what P_Yes captures.
- **Criticism that Figure 3 "does not assess what matters for the paper's claims":** Figure 3 validates probe detection capability on contrastive pairs; the downstream decision accuracy is evaluated in Tables 1–3. The paper has both evaluations; they are just presented in different sections.

## Novel Insights
None beyond the paper's own contributions. The observation that representation-level probes can improve tool-use timing decisions beyond the model's own output is the paper's core finding, and the reviewers' perspectives do not add a fundamentally different lens. The main insight from the review process is that the paper's technical core (representation probe + dual-threshold override) is stronger than its conceptual packaging (meta-cognition) would suggest, and a reframed submission would be more convincingly positioned.

## Suggestions
1. **Drop or carefully operationalize the "meta-cognition" framing.** Describe MeCo as a "representation-based trigger for tool-use timing" or a "learned override policy from hidden-state signals." This does not change any experiment but would make the contribution more defensible.
2. **Add pseudocode for the dual-threshold decision rule.** Explicitly state how l_yes and l_no are fit on validation data and applied at test time.
3. **Add error bars or bootstrapped confidence intervals** to all main accuracy tables.
4. **Add at least one stronger baseline** — a simple binary classifier on the last-layer query embedding would be straightforward and would strengthen the claim that the probe's signal is uniquely useful.
5. **Report latency and memory overhead** of the probe computation to substantiate the "minimal cost" claim.
6. **Provide the exact prompt templates** for the contrastive pairs (T_f^+ and T_f^-) and specify the dataset size for probe training.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>