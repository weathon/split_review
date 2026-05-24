Now let me compile my analysis and write the review.

## Final Analysis Before Writing

**Verified claims from the paper:**

**TVC algorithm (Section 3.1):** The paper describes the method at a high level: produces optimized SAE decomposition weights θ ∈ ℝ^{d_SAE}, reconstructs vθ from θ, steers, computes NLL loss, applies L1 regularization (sweeps reported for coefficient l), and references Figure 10 (appendix) for the overview. Results across multiple model sizes and SAE widths show 50-80% feature reduction.

**SFC modifications (Section 4.1):** Token position categorization (4.1.1) and loss function modification (4.1.2) are described with stated rationales. Two tasks excluded from Figure 6 with explanation (lines 206-207).

**Detection-execution causal experiment (Section 4.2):** "We then ablated detection directions while fixing attention patterns and measured the decrease in execution activations" (line 221). Results in Figure 8. Two tasks show weak connections (line 227).

**Unification claim:** Abstract states "well approximated by a sparse sum of SAE latents"; conclusion says "unifying the task vectors view with SAEs." The paper shows TVC decomposes task vectors into SAE features, establishing a connection between the two views.

**Ruling on each criticism (applying filtering discipline):**

1. **TVC underspecified** → KEEP as Minor (weakened). The main text is brief, though Figure 10 (appendix) exists. The paper does specify L1 regularization and NLL loss. The criticism about missing optimizer/hyperparameter details is valid for main-text self-containedness.

2. **Causal connection weak** → KEEP as Major. The experimental protocol ("ablated detection directions while fixing attention patterns") is genuinely vague. Two tasks show weak connections as acknowledged.

3. **SFC modifications lack validation** → KEEP as Minor (weakened). The paper explains the rationale. The missing control is a valid suggestion but not a fatal flaw.

4. **Unification not demonstrated** → REMOVE. The paper demonstrates that task vectors can be decomposed into SAE features via TVC. This constitutes a connection between the two views. The harsh critic's demand for a stronger demonstration is scope creep.

5. **Figure 3b caption confusion** → KEEP as Trivial. The caption is potentially confusing.

6. **No quantitative failure metrics for baselines** → KEEP as Minor. The paper says "more than 10 nonzero features" and "noticeably reduced" without precise numbers.

7. **No error bars** → KEEP as Minor. Valid point for steering results.

8. **Two excluded tasks** → KEEP as Minor (weakened). The paper does address this but doesn't investigate the root cause.

**Score: 6.0** — The paper makes genuine, multiple contributions (TVC algorithm, SFC scaling, discovery of task-detection features) with reasonable empirical support, but has notable presentation gaps in the causal experiment and algorithm specification that prevent it from being as strong as the 6.5-7.0 anchors.

Now writing the review.

---

## Summary

(2-3 sentence summary of the paper's contribution.)

## Strengths

- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal
None.

### Major
- weakness 1 — why it matters
- ...

### Minor
- ...

### Trivial
- ...

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me write it now.Now I have all the information I need. Let me compose the final review.

---

## Summary

This paper applies Sparse Autoencoders (SAEs) to understand in-context learning (ICL) in LLMs, making three contributions: (1) a **Task Vector Cleaning (TVC)** algorithm that decomposes task vectors into a sparse set (~4) of SAE features while preserving steering performance; (2) an **adaptation of Sparse Feature Circuits (SFC)** to Gemma-1 2B (30× larger than prior SFC work) and the ICL setting; (3) the **discovery of task-detection features** — SAE latents that activate on output tokens of completed task pairs and are causally linked to task-execution features through attention and MLP layers. The paper also releases SAE training infrastructure and dashboards.

---

## Strengths

1. **Novel TVC algorithm with quantitative validation across model scales.** Section 3.1 introduces a gradient-based method that decomposes task vectors into ~4 SAE features on average (Figure 3b), whereas naive SAE reconstruction yields >10 noisy features. The paper reports consistent 50–80% reduction in active features across multiple model sizes (Gemma 1 2B, Gemma 2 2B/9B) and SAE widths, and the sweeps for the L1 regularization coefficient are documented.

2. **First scaling of Sparse Feature Circuits to a 2B-parameter model and the ICL task.** Section 4 demonstrates non-trivial adaptations (token position categorization in §4.1.1, loss function modification in §4.1.2) that enable SFC on a model 30× larger than Marks et al. (2024). Figure 6 shows that ablating ~few hundred nodes reduces faithfulness by 0.5 for specific tasks while leaving unrelated tasks largely unaffected, validating that the circuits are task-specific.

3. **Discovery of task-detection features with causal evidence linking them to task-execution features.** Section 4.2 identifies features that activate almost exclusively on output tokens of completed task pairs (Table 2: 97.3% of activation mass on output tokens), earlier in the prompt than executor features. Figure 8 provides a causal connection experiment: ablating detection features reduces executor feature activations, with strongest effects for paired tasks and expected sharing among translation tasks.

4. **Comprehensive steering heatmaps demonstrating task specificity.** Figures 5 and 7 show that steering with a single identified feature boosts exactly one task for most tasks, with the interpretable exception of translation tasks sharing a generic English-to-foreign feature — providing fine-grained causal evidence beyond correlational analysis.

---

## Weaknesses

### Fatal
None.

### Major

- **The causal experiment linking detection and execution features is underspecified, weakening the paper's central circuit claim.** Section 4.2 states that the authors "ablated detection directions while fixing attention patterns and measured the decrease in execution activations" (line 221), but neither operation is defined: what does "ablating detection directions" entail (zeroing, mean-centering, resampling)? How are attention patterns "fixed" (cached from the clean run, frozen via gradient blocking)? The paper shows results in Figure 8 but the protocol is insufficiently described for a reader to assess whether the intervention is well-controlled or whether "fixing attention" blocks the very mechanism under study. Two tasks (person profession, present simple gerund) show weak connections, acknowledged as "warranting further investigation" (line 227), which further limits the generality of the claim. This is the paper's most important mechanistic result, and the current presentation does not provide enough detail to evaluate it.

### Minor

- **TVC algorithm description in the main text lacks sufficient detail for independent understanding.** The paper describes the method in roughly half a paragraph (lines 110–120): it produces optimized decomposition weights θ, reconstructs vθ, steers, and computes NLL loss with L1 regularization. While Figure 10 (appendix) provides an overview, the main text does not state the full optimization objective, optimizer choice, learning rate, initialization, or how sparsity is enforced beyond mentioning L1 coefficient sweeps. The method is a core contribution, and the main text should make its operation self-contained enough for an expert reader to understand what is being optimized and how.

- **No error bars, confidence intervals, or variance estimates are reported for any steering or faithfulness results.** The steering heatmaps (Figures 5, 7, 8) and the faithfulness analysis (Figure 6) present point estimates without any measure of variance across prompts, tasks, or runs. Given the modest number of tasks (~10–15), per-task variance could be meaningful. The two unstable tasks excluded from Figure 6 further underscore that variability exists but is not quantified.

- **The SFC modifications (token categorization, multi-pair loss) are not validated against the original SFC method.** The paper justifies the loss modification as amplifying task-solving relative to "copying circuits" (Section 4.1.2), but does not provide a control comparison — e.g., computing faithfulness with the original SFC loss on the last pair only, on the same tasks — to verify that the modification actually improves task-specific circuit discovery. The modifications are plausible, but their necessity is asserted rather than demonstrated.

- **Two tasks excluded from the faithfulness analysis (Figure 6) without root-cause investigation.** The paper states that person profession and football player were excluded due to "very small difference between their fully ablated and non-ablated losses" (line 206). The paper partially attributes this to the modified loss function, but does not investigate whether these tasks are genuinely unsuitable for ICL analysis in this model, or whether the SFC method itself fails for these inputs. A negative result (SFC does not work for tasks with small loss margins) would be a meaningful finding worth discussing.

### Trivial

- **Figure 3b caption is ambiguous.** The caption reads "Average L0 for cleaned task vectors vs. original task vectors at layer 12." It is unclear what L0 means for "original" (non-decomposed) task vectors, which are activation-space vectors, not SAE feature decompositions. The intended comparison (cleaned vs. naive SAE reconstruction?) should be clarified.

---

## Nice-to-Haves

- Compare steering with the top TVC feature vs. steering with a random SAE feature of similar L0 norm to strengthen the claim that the identified features causally matter and the heatmap specificity is not an artifact of using any large-magnitude direction.
- For the two excluded tasks, investigate whether the model actually performs them in the ICL setting; if not, remove them from the dataset; if yes, report the negative finding as a meaningful limitation of the SFC method.
- Show the full optimization objective, hyperparameters, and pseudocode for TVC in the main paper (or ensure Figure 10 is present).

---

## Removed Points

These points from the inputs were removed after cross-checking against the paper:

- **"Unification of task vectors and SAEs is not demonstrated"** — The paper shows that task vectors can be decomposed into sparse SAE features via TVC and that these features causally matter for steering. This constitutes a connection between the two views. The demand that the paper additionally prove that task vectors *are* the SFC circuit, or that the task vector's effect can be fully reconstructed from SFC features, extends beyond the paper's stated scope and what a single paper can reasonably establish.
- **"SFC modifications are ad-hoc"** — The modifications are clearly motivated (token structure of ICL prompts, balancing task vs. copying circuits) and the rationale is stated. The missing control comparison (retained as a Minor weakness) is the substantive concern, not the framing.
- **Criticism about missing appendix content (Figure 10)** — The parser strips appendix sections from all papers. Figure 10 exists in the original submission.
- **Request for comparison to non-SAE circuit discovery methods (ACDC, activation patching)** — This is outside the paper's stated scope (demonstrating SAEs as a tool for ICL analysis), not a required baseline.
- **Formatting/style nitpicks** (grammar, capitalization, equation labeling) — These are parser artifacts or presentation preferences, not substantive weaknesses.
- **"SAE architecture not clearly cited when introducing Equations 1 and 2"** — The paper explicitly states in line 53 that all SAEs use "the improved Gated SAE architecture (Rajamanoharan et al., 2024a)." The equations are generic SAE formulations followed by the architecture citation.
- **"Absolute activation values would be more informative than percentages" (Table 1)** — Percentages of total mass are a standard way to report feature activation patterns; this is a presentation preference, not a weakness.

---

## Novel Insights

The review process surfaces a tension between the paper's two main analyses (TVC decomposition of task vectors and SFC circuit discovery) that the paper itself does not fully resolve. The TVC analysis identifies task-execution features at layer 12; the SFC analysis identifies task-detection features at layer 11. These are presented as a two-stage circuit, but the paper never directly tests whether the TVC-discovered executive features are the *same* features that receive the highest Indirect Effect in the SFC analysis. A cross-method comparison — do the top-IE SFC nodes at layer 12 correspond to the TVC-decomposed executor features? — would either validate that both methods converge on the same mechanism or reveal that they capture different aspects of ICL. This cross-validation is a natural next step that the paper does not take, and it would substantially strengthen the claim that SAEs provide a unified view of ICL.

---

## Suggestions

1. **Provide a detailed, replicable protocol for the detection→execution causal experiment** in a revision: specify how detection directions are ablated (zero ablation? mean ablation? resampling?), how attention patterns are fixed (cached activations? gradient freezing?), and include a control intervention (e.g., random direction ablation) to establish specificity.

2. **Report the full TVC optimization objective, hyperparameters, and pseudocode** in the main paper (or ensure Figure 10 from the appendix is accessible), so that the core methodological contribution is self-contained.

3. **Add error bars or report per-task variance** for the steering and faithfulness results, even if only as a range across the task set, to give readers a sense of result stability.

4. **Add a control comparison** for the SFC loss modification: compare faithfulness obtained with the modified loss vs. the original SFC loss (last-pair only) on a subset of tasks, to validate that the modification is necessary and effective.

---

## Score and Decision

**Calibration summary:**

| Anchor | Path | Avg Score | Round | Comparison to this paper |
|--------|------|-----------|-------|------------------------|
| SAE super. dict. skyline | 1Njl73JKjB | 7.00 | R1, R2 | Stronger — cleaner evaluation framework and more rigorous controls |
| Cross-arch SAE comparison | 2J18i8T0oI | 6.50 | R1, R2 | Similar strength — clear contribution but metric validation concerns |
| SAE Match (data-free) | MDvecs7EvO | 6.50 | R1, R2 | Similar — novel method, some evaluation gaps |
| Inherent Interpret. Score | GjfIZan5jN | 7.33 | R2 | Stronger — more systematic experiments and rigorous analysis |
| ICL uncertainty | Jwtpbhheoy | 5.00 | R2 | Weaker — narrower scope, less empirical support |
| TCMRL meta-RL | 5GauLpaNGC | 5.67 | R2 | Weaker — mixed evaluation quality |
| Histogram counting | UatDdAlr2x | 5.75 | R2 | Weaker — more limited in scope |
| Biology dict. learning | uDIiL89ViX | 5.60 | R1, R2 | Weaker — ambiguous comparisons, underspecified method |
| Mental health SAEs | LQdaXixB0g | 2.50 | R1 | Much weaker — narrow, small-scale |
| EfficientSkip | 7DY2DFDT0T | 2.50 | R1 | Much weaker |

**Round 1 bracket:** I determined this paper sits between 3.5 and 7.5 — well above the weak 2.5 anchors but below the strong 8.0 anchors.

**Round 2 narrowing:** Comparing within the bracket, the paper is stronger than the 5.0–5.75 cluster (those papers have narrower contributions or more significant evaluation gaps) and comparable to but slightly weaker than the 6.5–7.0 anchors (the 6.5 anchors have clearer method specification and fewer underspecified experimental protocols). The underspecified causal experiment and the missing TVC algorithmic details in the main text are the primary gaps.

**Final score:** This paper makes multiple genuine contributions (TVC, SFC scaling, detection features) with reasonable empirical breadth, but the underspecified causal protocol and lack of variance reporting prevent it from reaching the 6.5–7.0 level of its strongest peers. Score of **6.0** reflects a solid paper with interesting findings that would benefit from a major revision addressing the presentation gaps in the main claims.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>