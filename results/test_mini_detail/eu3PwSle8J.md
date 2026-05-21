Now I have sufficient calibration data. Let me write the final consolidated review.

## Summary

This paper introduces Augmented Intermediate Representations (AIR), a defense against indirect prompt injection attacks in LLMs. The core insight is that existing instruction hierarchy (IH) defenses inject privilege signals only at the input layer, where they degrade through deeper layers. AIR addresses this by adding layer-specific trainable privilege embeddings to the intermediate representations in every decoder block. Across three model families (3B–8B), two training methods (SFT and DPO), and two gradient-based attacks (GCG and Astra), AIR achieves 1.6× to 9.2× reduction in attack success rate compared to prior IH methods, with negligible utility degradation.

## Strengths

1. **Clear, well-motivated architectural contribution.** The paper identifies a genuine limitation of existing IH-based defenses (signal injection only at the input layer) and proposes a simple fix: inject privilege embeddings at every decoder layer (Eq. 1, Fig. 4). The analogy to RoPE distributing positional information across layers provides independent grounding for the design principle. The overhead is minimal — 0.005% parameter increase for Llama-3.1-8B.

2. **Consistent and substantial robustness gains across diverse settings.** Table 1 shows AIR achieves lower ASR than both Delim and ISE on nearly every (model × training × attack) combination. For GCG, improvements range from 1.6× (Llama-3.1-8B, DPO) to 9.2× (Llama-3.2-3B, SFT). For Astra, the gains are even larger in many settings (e.g., Qwen-2.5-7B SFT: 69.0→2.4 vs Delim). These results are the paper's strongest asset.

3. **Broad and systematic evaluation.** The paper tests 3 model sizes (3B, 7B, 8B), 2 adversarial training paradigms (SFT, DPO), 2 gradient-based attacks (GCG, Astra), 4 static attacks, and 2 evaluation benchmarks (AlpacaFarm, SEP). This breadth convincingly demonstrates that the improvement is not an artifact of a specific configuration.

4. **Negligible utility impact.** Figure 6 shows AIR's win rate on AlpacaFarm remains competitive with or exceeds the non-adversarial baseline across all models and both training methods. The SEP evaluation (Fig. 8) further shows AIR-DPO achieves the best utility–separation trade-off on all three models, providing independent evidence of robustness without sacrificing task performance.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The causal narrative around signal degradation is suggestive but not proven.** Figure 3 shows that per-token cosine similarity between different privilege levels increases through layers for Delim and ISE, while AIR maintains lower similarity. The paper interprets this as evidence that input-layer IH signals "degrade," but this conflates observation with mechanism: for Delim, privilege is signaled by delimiter tokens between segments, not by content-token embeddings, so high content-token similarity is expected by design. For ISE, the increasing similarity through layers is what one would expect in a residual network. The paper's hedged language ("may fail to adequately preserve") partially mitigates this, but the causal claim that degradation → lower robustness is not isolated. Importantly, the main empirical result (AIR outperforms baselines) does not depend on this causal story — it stands on its own.

2. **The headline "up to 145× lower" Astra ASR is driven by a single cell on the smallest model.** The 145× figure comes from Llama-3.2-3B SFT (Delim ASR 14.5 → AIR ASR 0.1). On the largest model (Llama-3.1-8B), Astra ASR for AIR is 0.1 (SFT) vs ISE's 0.2 — a 2× reduction, not 145×. The paper does qualify with "up to" and discusses the full results, but this caveat is easy to miss.

3. **No variance or confidence reporting for ASR.** Table 1 reports ASR as point estimates. For gradient-based attacks sensitive to initialization and optimization path, reporting means and standard deviations over multiple runs (or at least multiple random seeds for the GCG prefix) would strengthen the conclusions.

4. **No discussion of adaptive attacks.** An attacker aware of AIR's mechanism could attempt to optimize an adversarial prefix that suppresses or overrides the privilege embedding. While this is a challenging attack (and the paper already evaluates against strong gradient-based attacks), a discussion of potential adaptive countermeasures and why they would be difficult would strengthen the paper's analysis.

### Trivial
None.

## Nice-to-Haves

- **Ablation controlling for model capacity.** Training a variant of AIR where per-layer embeddings are randomly initialized and frozen (or replaced with a fixed scalar) would help distinguish whether the improvement comes from privilege awareness per se or from added noise/regularization from extra parameters.
- **Per-layer analysis of the learned embeddings.** Are early-layer embeddings qualitatively different from late-layer ones? Do they converge to a common direction? This would give insight into how the model uses the privilege signal across depth.
- **Attack loss curves for Astra** (similar to Fig. 7 for GCG) would help compare optimization difficulty across defenses.

## Removed Points

- **Missing comparison against non-IH defenses (perplexity filtering, input sanitization, etc.):** The paper explicitly scopes itself within the IH-based defense family. It does not claim to survey all defenses. The appendix (stripped by parser) likely discusses broader context. Scope creep.
- **Question about baseline implementation fidelity ("Are these exactly the implementations from the original works?"):** Speculative; the paper describes implementations clearly.
- **Missing training dataset details (referenced to Appendix B.1):** The appendix was stripped by the parser; it exists in the original submission.
- **The claim that "adaptive attacks" are needed:** This is speculative and not tied to a concrete failing in the paper. The paper already evaluates against the strongest known gradient-based attacks.
- **Formatting/style nitpicks from reviews:** Parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The key insight — that distributing privilege signals across all layers, rather than injecting them only at the input — is well-articulated by the authors and directly yields the empirical results.

## Suggestions

- Report ASR with variance (e.g., over 3 random seeds for the GCG prefix) for the main gradient-based attack results.
- Add a brief discussion of adaptive attack vectors and why they are challenging in the AIR framework.
- Include the per-layer ablation (frozen vs trained embeddings) to strengthen the mechanistic understanding of why AIR works.
- Clarify in the abstract/intro that the "up to 145×" figure is model/setting-dependent and characterize the typical improvement range more precisely.

## Score and Decision

**Calibration summary:**

**Round 1 (Bracketing):** Papers in the low band (<3.5) — "Inverse Prompt Engineering" (3.0), "Safeguarding System Prompts" (3.0), "KDA" (2.5) — are clearly weaker: narrower evaluations, less convincing results, or flawed methodology. Our paper is substantially stronger than these.

Papers in the middle band (3.5–7.5) — "Baseline Defenses" (5.25), "AutoHijacker" (4.25), "Nested Gloss" (4.0), "Backdooring" (4.75) — have significant limitations (single attack evaluation, unclear motivation, narrow threat model). Our paper's evaluation breadth, clean results, and simple yet effective contribution place it well above this cluster.

Papers in the high band (>7.5) — "Safety Alignment Should be Made More Than Just a Few Tokens Deep" (9.5), "Backtracking Improves Generation Safety" (8.0), "Context-Parametric Inversion" (8.0) — are oral/spotlight-level papers with deeper analysis, theoretical insight, or broader implications. Our paper does not reach this tier.

**Initial bracket: 5.5–7.5**

**Round 2 (Narrowing):** Compared to accepted poster papers:
- "Safety Layers in Aligned LLMs" (6.0): Narrower applicability (fine-tuning defense only), weaker evaluation. Our paper is stronger.
- "Hypergraph Metric Space" (6.5): Complex method with unclear motivation and missing baselines. Our paper's simpler, cleaner contribution is at least comparable.
- "Catastrophic Jailbreak" (7.0): Strong attack paper with high scores but a different category. Our paper is slightly weaker in terms of headline impact.

Our paper is stronger than the 6.0 anchor and comparable to the 6.5 anchor, but not as strong as the 7.0 anchor. The weaknesses (unproven causal mechanism, no variance reporting, limited adaptive attack analysis) prevent it from reaching the top of the bracket.

**Final score: 6.5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>