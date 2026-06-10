## Summary

This paper presents "persona vectors" — automatically extracted linear directions in LLM activation space corresponding to personality traits (evil, sycophancy, hallucination) — and demonstrates their utility across four applications: deployment-time monitoring, post-hoc mitigation via steering, training-time preventative steering, and pre-finetuning data screening. The extraction pipeline is fully automated given only a natural-language trait description, and results are validated on both Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct.

## Strengths

- **Strong predictive correlations for finetuning-induced shifts.** Figure 4 shows very strong correlations (r = 0.76–0.97, all p < 0.001) between finetuning shift along persona vectors and post-finetuning trait expression scores across all three traits and both models. Cross-trait baselines (r = 0.34–0.86, Appendix I.2) are lower, indicating trait-specific signal. The authors honestly acknowledge cross-trait correlations in footnote 6.

- **Preventative steering preserves capabilities where inference-time steering fails.** Figure 6 (fact-acquisition case study) shows that inference-time steering against hallucination destructively degrades both MMLU accuracy and new-fact recall, while preventative steering suppresses hallucination to baseline levels with only slight reduction in new-fact accuracy and stable MMLU. This is a clear, practically important advantage and a genuinely novel contribution.

- **Pre-finetuning data screening is highly predictive.** Figure 7 shows correlations of r = 0.88–0.95 (all p < 0.001) between projection difference on training data and post-finetuning trait expression, enabling proactive identification of problematic datasets before any finetuning occurs.

- **Automated, general-purpose pipeline validated across models and traits.** The pipeline requires only a trait name and description, works across seven traits (three main text, four additional in Appendix I), and is validated on two distinct model families (Qwen, Llama), demonstrating generality and cross-architecture robustness.

- **Honest characterization of monitoring limitations.** Section 3.3 explicitly states that monitoring correlations (r = 0.75–0.83) "arise primarily from distinguishing between different prompt types, with more modest correlations when controlling for prompt type." This transparency about the method's scope is commendable.

## Weaknesses

### Fatal

None.

### Major

- **No variance or error bars reported for any experiment.** The paper reports no confidence intervals, variance across random seeds, or any measure of statistical uncertainty — not for steering effectiveness (Figures 2, 5, 6), not for the correlation analyses (Figures 4, 7), not for capability preservation claims (Figures 5, 6). Each finetuning experiment appears to be run once. For a paper whose central claims rest on quantitative correlations and steering coefficient comparisons, this is a meaningful omission. While confidence intervals can be derived for correlations given sample sizes, the steering and capability preservation results have no uncertainty quantification.

- **Layer selection procedure is optimized for the primary evaluation metric (steering).** Line 70 states: "we select the most informative layer by testing steering effectiveness across layers (Appendix D.4)." Since steering effectiveness (Figure 2) is a primary validation metric, selecting the layer to maximize this metric creates circularity. The finetuning shift and data screening evaluations use separate evaluation questions, partially mitigating the concern for those results, but the steering demonstrations specifically benefit from this optimization.

- **MMLU is the sole general capability metric.** The "preserves general capabilities" claim is central to the preventative steering contribution (Figures 5 and 6), but MMLU is the only general benchmark used. The fact-acquisition case study (Section 5.2) also measures new-fact accuracy, but this is task-specific. One benchmark is insufficient to support the broad capability-preservation claim.

### Minor

- **Experiments limited to 7–8B models.** The motivating real-world incidents involve frontier models (GPT-4o, Grok, Claude), but all experiments use Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct. Cross-model consistency is valuable, but practical relevance would be stronger with even one experiment on a larger model.

- **Near-duplicate paragraph at lines 194–196.** Two consecutive paragraphs in Section 5.1 make nearly identical comparisons of preventative steering to regularization penalties and CAFT, with slightly different wording. This appears to be an editing oversight.

- **Sample-level analysis (Figure 8) only shows a subset of comparisons.** The paper notes that EM-like datasets induce persona shifts (e.g., "training on flawed math reasoning increases expression of evil," Section 4.1), but Figure 8 shows only Evil/Sycophancy/Hallucination projections for explicit trait-eliciting datasets and one EM-like dataset (Opinion Mistake II). Showing more cross-domain effects at the sample level would strengthen the data screening contribution.

## Nice-to-Haves

- A mechanistic analysis of why preventative steering works (even a simple gradient-level argument) would help practitioners predict when it will generalize and is especially important given that simple regularization penalties fail (Appendix L.5) while this approach succeeds.
- Expanding capability evaluation beyond MMLU to 2–3 additional benchmarks (e.g., HellaSwag, ARC, a coding benchmark).
- Sensitivity analysis for extraction parameters (number of contrastive pairs, rollouts, evaluation questions).
- Promoting real-world dataset screening results from Appendix N to the main text.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Circularity in the full evaluation pipeline.** The harsh critic raised a broader circularity concern (persona vectors extracted to separate trait-positive from trait-negative activations → finetuning shift measured by projecting onto same vectors → trait expression scored by LLM judge). This is partially valid but overstated: the paper uses separate extraction and evaluation question sets (20 each), validates the LLM judge against human evaluators (Appendix D), and presents cross-trait baselines. The concern is captured in the narrower layer selection weakness above.
- **Existence/availability concerns about cited tools/models.** The harsh critic did not raise these; the strength finder did not either. No such concerns to filter.
- **"Strengthening the Paper on Its Own Terms" section from harsh critic.** These are essentially the same as the nice-to-haves and minor weaknesses already captured.

## Novel Insights

The most novel observation is that preventative steering (adding α·v during training to prevent the model from learning that direction) works empirically even though the mechanism is not understood. The fact that simple regularization penalties fail while this activation-intervention approach succeeds suggests something mechanistically interesting: the gradient updates from the loss function must be learning to compensate for the shifted activations rather than amplifying them. Understanding why (a) dominates (b) is a genuine open question that could enable a new class of training-time alignment methods.

## Suggestions

- Rerun each finetuning experiment with 3–5 random seeds and report mean ± std for all key quantitative claims.
- Expand capability evaluation beyond MMLU to include at least 2–3 additional benchmarks.
- Clarify whether the layer selection criterion uses the same data/metric as downstream evaluation; if so, report results for a fixed (non-optimized) layer as well.
- Deduplicate the two similar paragraphs in Section 5.1 (lines 194–196).

## Calibration Report

**Anchors retrieved:**

| Round | Path | Avg Score | Comparison |
|-------|------|-----------|------------|
| 1 | DXaUC7lBq1.md (Low-empathy LLMs) | 3.0 | Weaker: poorly understood mechanisms, limited experiments |
| 1 | z1yI8uoVU3.md (Measuring Steered Representations) | 3.0 | Weaker: evaluation framework only, no novel applications |
| 1 | LQdaXixB0g.md (pSAE-chiatry) | 2.5 | Weaker: narrow domain, limited validation |
| 1 | M7CblLwJB8.md (AutoCustomization) | 2.6 | Weaker: less rigorous, less novel |
| 1 | 2XBPdPIcFK.md (ActAdd/Activation Engineering) | 5.0 | Weaker: basic method, limited experiments, small benchmarks |
| 1 | wozhdnRCtw.md (Instruction-Following Steering) | 7.0 | Similar but weaker: narrower scope, fewer applications |
| 1 | 9wjGUN65tY.md (Conceptors for Steering) | 5.0 | Different focus: theoretical framework, less practical |
| 1 | ZPkNrs6aNO.md (Confident Directions) | 5.5 | Weaker: limited experiments, narrower contribution |
| 1 | I4e82CIDxv.md (Sparse Feature Circuits) | 8.0 | Stronger: more thorough methodology, stronger mechanistic analysis |
| 1 | NN6QHwgRrQ.md (MAP Alignment) | 8.0 | Stronger: novel theoretical framework with strong validation |
| 1 | aWXnKanInf.md (TopoLM) | 8.0 | Different domain, strong neuroscience contribution |
| 1 | EytBpUGB1Z.md (Retrieval Heads) | 8.0 | Stronger: very thorough interpretability work |
| 2 | 0DZEs8NpUH.md (Personality Alignment) | 6.0 | Weaker: less technically novel, focused on personalization |
| 2 | TqwTzLjzGS.md (BIG5-CHAT) | 5.25 | Weaker: dataset contribution, limited method novelty |
| 2 | cxt2Auexc3.md (Editing Personality) | 5.75 | Weaker: benchmark-focused, limited method depth |
| 2 | kGteeZ18Ir.md (Bias in Personas) | 5.75 | Different focus: analysis, not control method |
| 2 | GjfIZan5jN.md (Interpretability & Classifiability) | 7.33 | Different domain but comparable quality |
| 2 | DzGe40glxs.md (Emergent Planning) | 8.0 | Stronger: thorough mechanistic analysis |
| 2 | Njx1NjHIx4.md (Formation of Representations) | 7.5 | Comparable: strong theoretical contribution |
| 2 | Oi47wc10sm.md (CAST/Conditional Steering) | 7.33 | Comparable but narrower: refusal only, less broad impact |

**Round 1 bracket:** 6.5–8.0 (clearly above 5.0–6.0 anchors, somewhat below 8.0 anchors).
**Round 2 narrowing:** The paper is clearly stronger than the 6.0 Personality Alignment paper (more novel, broader applications, stronger empirical validation) and comparable to or slightly better than the 7.0 instruction-following steering paper. It is somewhat below the 7.33 CAST paper in methodology rigor (CAST has more focused evaluation), but has broader scope and more novel contributions (preventative steering). It sits below the 7.5–8.0 range due to methodological gaps (no variance, limited capability evaluation).

**Final score: 7.0** — a solid contribution with novel preventative steering and multiple practical applications, tempered by missing variance reporting, single capability metric, and layer selection circularity.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>