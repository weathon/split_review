Now I have thoroughly verified the paper content against each reviewer claim. Let me produce the consolidated review.

---

## Summary

This paper proposes Dynamic Prompt Corruption (DPC), a two-stage instance-level method for improving complex reasoning with soft prompts. DPC first uses saliency-based analysis to detect when a soft prompt is harming reasoning (Dynamic Trigger), then selectively masks the most problematic prompt token(s) to mitigate the negative effect (Dynamic Corruption). Experiments on GSM8K, MATH, and AQuA with LLaMA2-13B, LLaMA3-8B, and Mistral-0.2-7B are reported.

## Strengths

- **Well-designed ablation that validates the mechanism**: The ablation study (Table 2) is the paper's strongest empirical contribution. Random corruption *hurts* performance (GSM8K drops from 65.5% to 51.3%), corruption without the trigger yields only marginal gains (+0.3% GSM8K, +0.5% MATH), while the full DPC combining both components achieves substantially better results (GSM8K 67.6%, MATH 36.3%, AQuA 42.5%). This provides causal evidence that the synergy of targeted detection and precise corruption is what drives the improvement, not the corruption operation alone.

- **Novel analysis framing**: The core observation — that soft prompts can be beneficial during early reasoning steps but harmful when later steps continue to attend to them — is well-motivated and plausible. Using saliency scores to quantify information flow between soft prompts and rationale tokens is a reasonable diagnostic approach that grounds the method in an interpretability lens rather than pure heuristics.

- **Principled instance-level adaptation**: Unlike static prompt tuning, DPC decides *whether* to intervene and *where* to corrupt on a per-instance basis. The Dynamic Trigger (ratio of "affected tokens" in the latter half of the rationale) and the corruption targeting the single most information-heavy soft prompt position represent a sensible design that goes beyond one-size-fits-all approaches.

## Weaknesses

### Major

- **Baseline selection is too narrow to support the claimed contribution**: The paper compares DPC only against vanilla prompt tuning and ACT (an attention-sink calibration method). The related work section itself discusses several directly relevant methods — DePT (decomposes soft prompts), Dynamic Prompting (selects different prompts per instance), Nemesis (exploits Low-norm Effect) — yet none are included as baselines. Without comparison to at least one other adaptive or optimization-based prompt tuning method, the reader cannot determine whether DPC is genuinely superior or merely better than the weakest baseline. This limits the significance of the claimed 4–8% gains.

- **Internal inconsistency in the results text**: The GSM8K results paragraph (Section 4.2) states that for LLaMA3-8B, accuracy *improved* from 65.5% to 36.3%. This is clearly a factual error: the 36.3% belongs to MATH (confirmed by the MATH paragraph), and the ablation section reports DPC achieving 67.6% on GSM8K. While this is likely a copy-editing mistake, it undermines confidence in the reporting and must be corrected. Moreover, all results are reported as single accuracy numbers with no variance, confidence intervals, or multiple seeds — concerning for a method where the trigger may flip decisions on a small number of instances.

- **The Dynamic Trigger threshold selection is underspecified**: The threshold β is described as "the average intensity of information flow from the soft prompt to the former part of the reasoning tokens by default" (Section 3.2). The paper then states that the authors "summarize different thresholds to delimit the incorrect reasoning" after analyzing instances across tasks and models. It is not specified (a) how the "average" is computed, (b) whether thresholds are derived from a held-out validation set or from the test instances themselves, (c) what the actual threshold values are, or (d) how sensitive results are to the threshold. This gap raises a legitimate concern about whether thresholds could have been post-hoc tuned to maximize reported gains.

- **Information-flow analysis central to the method is incompletely reported**: Section 2.1 ("Layer Analysis") contains essentially no content — it states that "we define two metrics to measure the strength of information flow layer-wise" but does not define them, show results, or provide quantitative evidence. The paper's foundation (that soft prompts harm later reasoning steps) is therefore asserted rather than demonstrated with data in the main text. While the appendix may contain the full analysis, the main paper should at minimum summarize key quantitative findings.

### Minor

- **No explanation of how saliency is computed at inference time**: The saliency score (Equation 1) uses cross-entropy loss, and the trigger computes saliency from the soft prompt to rationale tokens. At inference time, ground-truth labels are unavailable. The paper does not clarify how the saliency computation is performed during test-time evaluation — e.g., whether it uses the model's own generated answer as the target. This is a practical gap in the method description.

- **No ablation on the corruption hyperparameter Γ**: The corruption step eliminates the smallest Γ% of embedding values (excluding the masked token), with Γ=10 by default. No sensitivity analysis or ablation is provided for this hyperparameter, making it unclear how robust the method is to this choice.

- **ACT baseline adaptation unclear**: ACT was originally designed for classification tasks to mitigate attention sinks. The paper does not describe how it was adapted to generative reasoning tasks, making the comparison difficult to interpret.

- **Evaluation limited to math reasoning**: All three datasets (GSM8K, MATH, AQuA) are math reasoning tasks. If DPC is claimed as a general technique for complex reasoning, at least one non-math reasoning task (e.g., StrategyQA, HotpotQA) would strengthen the claims of generality.

### Trivial

- The reference to "Equation 6" (Section 3.3) appears to point to an equation that was either an image stripped during parsing or missing; this should be clarified or the equation should be displayed inline.

## Nice-to-Haves

- A precision/recall analysis of the Dynamic Trigger: what fraction of instances flagged as "harmful" actually benefit from corruption, and what fraction of beneficial instances are missed?
- Wall-clock time or FLOPs comparison between DPC and vanilla PT, since DPC requires a forward pass with gradient computation before deciding whether to re-run inference.
- A breakdown of test-set instances into four categories (trigger on/off × corruption helps/hurts) to directly test the method's logic.

## Removed Points

These points are flagged for removal — treat them with caution.

- **"Equation 6 not presented" / missing method details**: Reference to Equation 6 may be a parser artifact (equation rendered as image that was stripped). The corruption strategy is described textually (mask the j-th vector, zero out smallest Γ% of remaining values), so the missing equation does not materially affect understanding. *Justification: Potential parser artifact; the method is still described.*

- **"Motivating example not quantified"**: Figure 1 provides an illustrative example. A single example is standard for motivation; demanding a prevalence statistic for every motivating example is excessive. *Justification: Generic expectation misaligned with standard practice.*

- **"Section 2.1 has no visible text" as a standalone critique**: While the content gap in Section 2.1 is real (kept as a Minor weakness above), the harsh critic's framing as a "methodological gap" that "weakens the paper's foundation" overstates the issue — the core saliency analysis tool and key findings are described in Section 2 itself. *Justification: Downgraded to Minor — the analysis tool is introduced, but the layer-specific findings are missing.*

- **"Large differences across models (Llama2-13B worse than Llama3-8B on GSM8K)"**: This is not unusual. Llama3 is a newer architecture and can outperform an older, larger model. *Justification: Factually correct behavior, not a paper flaw.*

- **Complaints about ACT baseline being from classification tasks**: This is a valid concern about adaptation, but the reviewer's framing as a fatal flaw is overstated — many methods transfer between task types. *Justification: Kept as Minor above (appropriately weakened).*

## Novel Insights

None beyond the paper's own contributions. The reviews surface the paper's core tension well: the method is intuitively appealing and the ablation provides mechanistic evidence, but the evaluation is too thin and the reporting too sloppy to trust the claimed gains without further validation.

## Suggestions

1. **Fix the internal inconsistency** in Section 4.2 (LLaMA3 GSM8K: 36.3% → should be the correct value, likely 67.6% as in the ablation). Report all numbers with verification against the table.
2. **Add at least one directly comparable baseline** — Nemesis (low-norm effect for PT) or Dynamic Prompting (instance-level prompt selection) would directly test whether DPC's approach is competitive with other adaptive strategies.
3. **Specify how β thresholds are selected**: report the actual threshold values per task/model, state whether they were chosen on a held-out validation set, and add a sensitivity analysis (e.g., accuracy as β varies ±20%).
4. **Report variance**: run experiments with at least 3 random prompt initializations and report mean and standard deviation. The trigger may affect only a small fraction of instances, making single-run estimates noisy.
5. **Clarify test-time saliency computation**: explain how the loss is defined during inference when ground-truth labels are unavailable (e.g., using the model's own generated token as target).

## Score and Decision

The paper proposes an interesting and well-motivated idea with a clean ablation study that provides mechanistic support. However, the evaluation is critically weakened by (a) a too-narrow baseline set that does not justify the claimed superiority, (b) a factual error in the reported numbers that undermines confidence, (c) underspecified threshold selection that raises reproducibility concerns, and (d) missing variance reporting. These are not fatal to the core idea, but they prevent the paper from making a convincing case in its current form. The paper would benefit from a major revision addressing these gaps.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>