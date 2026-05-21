I have all the information needed. Let me now write the consolidated final review.

## Summary

This paper systematically investigates benchmark contamination detection in Large Reasoning Models (LRMs) across two realistic scenarios: (I) contamination introduced during SFT before RL-based reasoning training, and (II) contamination with chain-of-thought (CoT) reasoning applied as a final SFT step to already-advanced LRMs. The paper finds that in Stage I, SFT contamination is initially detectable but a brief GRPO training on clean data systematically conceals contamination signals across 10 detection methods. Controlled ablations and theoretical analysis identify PPO-style importance sampling and clipping as the driving mechanism. In Stage II, even extensive SFT contamination with CoT on advanced LRMs leaves near-random detection performance, challenging the memorization-based assumptions underlying most existing detection methods.

## Strengths

- **Systematic empirical demonstration that RL training conceals SFT contamination across diverse detection methods (Stage I).** The paper evaluates 10 detection methods spanning generation-based, perturbation-based, reference-based, and reference-free approaches across 6 benchmarks and 2 base models (Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct). Tables 1-2 and Figure 2 consistently show that GRPO training (even on clean data) reduces AUROC across all methods, with reference-free methods dropping to near-random (AUROC ≈ 50%) after only 156 steps. This breadth makes the result robust rather than method-specific.

- **Controlled experiments cleanly rule out forgetting as an alternative explanation.** The paper shows that further SFT on clean data (4 additional epochs) does not reduce detection AUROC, while GRPO does — even though performance inflation from contamination persists. This experimentally isolates the RL optimization objective as the cause, not simply additional training or memory decay. This is a clean controlled result.

- **Stage II findings are striking and carry significant implications.** Table 5 shows that after extensive SFT contamination with CoT on 4 different advanced LRMs (DeepSeek-R1-Distill variants and OpenThink-3-7B), all 10 detection methods perform at or near random across 6 benchmarks (most AUROCs between 48% and 62%). The log-prob density plots (Figure 4) visually confirm that contaminated LRMs generalize confidence to non-members, undermining the core memorization assumption of prior detection work.

- **Ablation study (Table 3) pinpoints the mechanism.** By comparing RAFT (no clipping), RAFT++ (with clipping), GRPO (with clipping), and versions with clipping removed, the paper empirically demonstrates that the PPO-style clipping term is the key driver: without clipping, RAFT++ and GRPO show no detection degradation (Δ ≈ -1 to -2%), while with clipping, degradation is severe (Δ ≈ -14 to -18%).

## Weaknesses

### Fatal
None.

### Major

- **Misalignment between the theoretical assumptions and the main experimental setting.** The theoretical analysis (Section 3.2) explicitly assumes "RL training is performed on the benchmark data (i.e., training data is the combination of members M and non-members N)" (line 195). However, the main Stage I experiments (Table 2, Figure 2, Section 3.1) use GRPO on *clean* data (10K questions from DeepMath-103K), not benchmark data. The theory elegantly explains why importance sampling/clipping contracts the NLL gap when RL is on the benchmark itself, but it does *not* directly explain the paper's central experimental observation: why GRPO on clean (non-benchmark) data contracts the gap for previously seen SFT-contaminated samples. While the underlying mechanism (clipping disproportionately affects higher-variance trajectories from non-members) is a plausible intuitive explanation that could extend to this setting, the formal derivation as presented does not cover it. The ablation in Table 3 partially addresses this, but the training data used in those ablations is not explicitly stated in the available text (it presumably appears in the stripped appendix). This disconnect weakens the paper's claim to have "isolated the core reasons" for concealment via formal theory. **Resolution**: Either (a) extend the theoretical analysis to cover clean-data RL, (b) add an experiment where RL is performed on benchmark data itself, matching the theory's assumptions, or (c) clearly acknowledge this limitation and reframe the theoretical contribution as illustrative rather than directly explanatory.

### Minor

- **The "broad class of RL methods" claim is somewhat overextended.** The paper concludes that "a broad class of RL methods may inherently exhibit similar concealment capability" based on experiments with two algorithms (GRPO, RAFT++) and theoretical reasoning about PPO-style objectives. While the argument is plausible — many RL algorithms do use importance sampling and clipping — the empirical basis is narrow. The paper would benefit from testing at least one additional algorithm (e.g., PPO, RLOO) or explicitly qualifying the scope.

- **Stage II CoT data source is underspecified.** The paper states "extensive SFT contamination with CoT" on advanced LRMs but does not specify how the CoT responses are generated — whether by the same model, a stronger model, or ground-truth reasoning. This matters because the detection methods operate on model-generated responses during evaluation; different CoT distributions could affect memorization signals. The Stage I setup is clearer ("responses distilled from an advanced LRM"), but Stage II needs the same precision.

- **No uncertainty estimates for main detection results.** All AUROC values in Tables 2, 3, and 5 are reported as single numbers without variance, confidence intervals, or multiple-seed averaging. Given that detection scores involve stochastic rollouts (8 responses per question) and training variability, reporting some measure of uncertainty would strengthen the evidence.

- **The scope is limited to ~7B-scale models.** The paper tests Qwen2.5-7B, Llama-3.1-8B, and ~7-14B LRMs. While this is a reasonable starting point, the paper should explicitly acknowledge that the results may not generalize to much larger models (e.g., 70B+) rather than leaving the reader to infer generality.

### Trivial
- The theoretical section (3.2) would benefit from a brief plain-language intuitive summary after Theorem 3.1 to improve accessibility for readers less familiar with RL theory.
- Figure 3 and 4 captions could be more informative (they currently repeat figure text verbatim).
- Typo in "Miresghallahi et al." in Tables 2 and 5 (should be "Mireshghallah").

## Nice-to-Haves
- A brief discussion of computational costs or practical limitations of the evaluated detection methods (e.g., LiRA requires training many shadow models) would help practitioners contextualize the findings.
- Controlling for whether post-contamination response quality differences (e.g., longer CoT) independently affect detection scores beyond memorization signals would strengthen the Stage II analysis.
- Multi-seed experiments or confidence intervals would improve statistical rigor, but single-run reporting is common in this benchmark style, so this is not a weakness per se.

## Removed Points

These points were flagged by reviewers but are removed or demoted for the following reasons:

- *"Missing related works"* — Removed per policy: I cannot verify the existence of missing references without external sources.
- *"The paper does not consider computational cost of detection methods"* — Moved to Nice-to-Haves; this is a practical consideration, not a weakness of the scientific contribution.
- *"Potential confound in Stage II: different CoT response quality could affect detection"* — Removed as speculative; the paper's discussion (Section 4, paragraph starting "Despite Feng et al.") already addresses this point by explaining that LRMs generalize rather than memorize.
- *"Mismatch between theoretical analysis and experiments" as a fatal flaw* — Demoted from Fatal to Major. The empirical findings stand independently, and Table 3 validates the mechanism. The theory-experiment misalignment is a real issue in the *framing* of the contribution, not an invalidation of the core results.
- *"Weakness about CoT data ambiguity" as major* — Demoted to Minor as this is a clarity issue that can be resolved with a sentence or two.
- *"Paper does not discuss statistical significance"* — Demoted from the reviewer's implied severity; this is a common practice gap in this area and is not a fatal omission. Kept as Minor.
- *"Strength: addresses an important problem"* — Removed as generic. Kept only strengths with specific evidence anchors.
- *"Strength: theoretical analysis connects algorithmic choice to detection evasion"* — Modified to note the caveat about theory-experiment alignment, and reframed as a strength of the ablation study (Table 3) rather than the formal theorem.

## Novel Insights

The most interesting observation across the reviews is that the paper's two stages reveal qualitatively *different* failure modes of contamination detection — Stage I shows active *concealment* via RL optimization dynamics, while Stage II shows that LRMs *generalize* to non-member questions, precluding detection from the start. This is a deeper duality than simply "detection fails": one failure is algorithmic (driven by the training objective), the other is architectural/capacity-driven (driven by the model's reasoning ability). The paper's discussion of the Stage II mechanism (that LRMs internalize knowledge rather than memorizing sequences, Section 4) is underdeveloped relative to its importance and could be the basis for a follow-up study. The combination of these two distinct failure modes strengthens the overall argument that contamination detection for LRMs requires fundamentally new approaches, not incremental improvements to existing methods.

## Suggestions

1. **Resolve the theory-experiment alignment.** The paper's strongest selling point is the empirical demonstration. Either reframe the theoretical analysis as providing *intuition* for why clipping matters (supported by Table 3) rather than a direct formal explanation of the main experiments, or add an experimental condition where RL is performed on the benchmark data itself (matching the theory's assumptions) to close the gap.
2. **Specify the training data for all ablation experiments** (Table 3) — the paper should explicitly state whether the RL data in these ablations is clean, benchmark, or mixed.
3. **Clarify the CoT source for Stage II contamination** — specify whether responses are generated by the same LRM, a stronger model, or are templated reasoning traces.
4. **Tone down the "broad class of RL methods" generalization** or support it with at least one additional algorithm beyond GRPO and RAFT++.
5. **Add uncertainty estimates** (e.g., variance across seeds or bootstrap confidence intervals) for at least the key AUROC results.

## Score and Decision

**Round 1 bracket**: After comparing against calibration anchors — weak (avg 2-3), middle (avg 4.25-6.75), and strong (avg 7.5-8) — the paper clearly sits in the upper-middle range. It is substantially more systematic than "Evading Data Contamination Detection" (4.25, Reject), comparable in breadth and execution quality to "Language Model Detectors Are Easily Optimized Against" (6.00, Accept) and "Detecting Pretraining Data from LLMs" (6.25, Accept), but below the clean theoretical+empirical integration of "Proving Test Set Contamination" (7.50, Accept). **Initial bracket: 5.0 – 7.0**.

**Round 2 narrowing**: Comparing against "Language Model Detectors Are Easily Optimized Against" (6.00) — the paper under review has broader scope (10 detection methods, 2 stages, theory) but a more significant flaw (theory-experiment mismatch). Against "How much can we Forget about Data Contamination" (6.75) — the paper under review has a cleaner causal identification (clipping ablation) but weaker theory alignment. Against "Detecting Pretraining Data from LLMs" (6.25) — our paper has more ambitious breadth but less polished execution of its core claim. **Final score: 6.0**.

The paper makes a strong empirical contribution to an important and timely problem. The main weakness — misalignment between the theoretical framing and experimental setting — is addressable through revision and does not invalidate the core empirical findings. The breadth of evaluation (10 methods, 6 benchmarks, 2 stages, multiple models) and the clean causal identification in the ablation study are genuine strengths that merit acceptance.

### Calibration Anchors

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| Evading Data Contamination Detection (Nk1MegaPuG) | 4.25 | 1 | Weaker — tests only one attack, poor presentation. Our paper is stronger. |
| Language Model Detectors Are Easily Optimized Against (4eJDMjYZZG) | 6.00 | 1,2 | Comparable — both show RL-based detection evasion. Our paper has broader scope but a clearer weakness. |
| Detecting Pretraining Data from LLMs (zWqr3MQuNs) | 6.25 | 1,2 | Comparable — both solid empirical contributions. Our paper has more methods but a theory-experiment gap. |
| How much can we Forget about Data Contamination (Nsms7NeU2x) | 6.75 | 1,2 | Slightly stronger — cleaner theory even though bounds are loose. |
| To the Cutoff... and Beyond? (m2NVG4Htxs) | 6.75 | 2 | Slightly stronger — clever longitudinal approach. Our paper is more actionable for practitioners. |
| Proving Test Set Contamination (KS8mIvetg2) | 7.50 | 2 | Stronger — novel method, clean execution, provable guarantees. |
| Training on the Test Task Confounds Evaluation (jOmk0uS1hl) | 8.00 | 1 | Stronger — cleaner framing with unambiguous causal identification. |

**MY FINAL SCORE: 6.0**
**MY FINAL DECISION: Accept**