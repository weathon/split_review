## Summary

This paper introduces MobileLLM-R1, a family of sub-billion-parameter reasoning models (140M–950M) trained using a benchmark-free, influence-based data curation framework. The core contributions are: (1) leave-one-out ablations to identify which data sources drive which reasoning capabilities, (2) cross-capability influence scoring to optimize data mixing ratios, and (3) iterative data-model co-evolution for mid-training knowledge compression. The resulting models, trained on 4.2T tokens (~2T unique), achieve strong reasoning performance — matching Qwen3-0.6B despite far fewer training tokens, and substantially outperforming fully-open baselines (OLMo, SmolLM) in controlled comparisons.

## Strengths

- **Controlled ablation isolates pre-training from post-training (Table 2):** Fine-tuning all models on the identical reasoning SFT corpus cleanly disentangles the effect of pre-training/mid-training data curation from post-training differences. MobileLLM-R1-950M* (949M params) achieves 57.8 MATH vs. 53.0 for OLMo-2-1.48B (56% larger), directly demonstrating that the data curation recipe instills stronger latent reasoning before post-training even begins. This is the single strongest piece of evidence supporting the paper's core claims.

- **Leave-one-out analysis yields non-obvious findings (Section 2.1, Figure 3):** Systematic removal of individual datasets with NLL measurement on capability-probing datasets reveals that StarCoder benefits math more than OpenWebMath benefits code — a reversal of conventional wisdom — and that FineWeb-Edu acts as a cross-domain "glue." This goes beyond generic "data quality matters" claims by providing causal, quantitative evidence of which specific data sources matter for which capabilities.

- **Influence-based data mixing improves all three capability axes without benchmark exposure (Section 2.2, Figure 4):** The datamix strategy, derived entirely from capability-probing datasets (not held-out benchmarks), consistently lowers perplexity on Code, Math, and Knowledge benchmarks compared to uniform sampling — evidence that the learned mixture generalizes rather than overfitting to specific evaluation sets.

- **Commitment to full reproducibility:** The paper releases all datasets, model weights, and training code (a structural advantage over partially-open baselines like Qwen, Gemma, LLaMA), enabling community replication and extension.

## Weaknesses

### Major
- **The "~2T unique data is sufficient" claim is not directly supported by experiments (Abstract, Section 2):** The paper states "only ~2T tokens of high-quality data are sufficient" but the actual training pipeline uses 4.2T tokens (2T Phase 1 + 2T Phase 2 + 0.2T mid-training), achieved by resampling the ~2T unique tokens. The model is never trained on just 2T tokens, so the claim that 2T is "sufficient" is an extrapolation without direct evidence. An experiment training on exactly 2T unique tokens without resampling would be needed to support this claim. This is a meaningful overstatement of what the paper demonstrates.

### Minor
- **Token-only framing of the Qwen3 comparison collapses the parameter dimension (Abstract, Section 1, Section 6):** The paper repeatedly states MobileLLM-R1-950M is trained on "only 11.7% of the tokens compared to Qwen3's 36T" while matching Qwen3-0.6B. This omits that MobileLLM-R1-950M (949M params) is 58% larger than Qwen3-0.6B (~600M params). Under FLOPs (size × tokens × 6), the advantage is roughly 18% of Qwen's compute — still impressive but less dramatic. The paper does include Figure 1 with a FLOPs-based comparison, partially mitigating this, but the token-only framing in prominent positions inflates the apparent efficiency advantage.

- **Anomalous pattern in the mid-training MMLU comparison (Figure 6):** The "original" (uncompressed) mid-training curve shows an unusual spike at 30K steps (28.5 → 38.0) followed by a drop to 31.0 at 40K, while the subsampled curve climbs steadily. This pattern is atypical of normal training dynamics and could reflect an evaluation artifact, training instability, or a run-specific issue rather than a systematic benefit of subsampling. The paper acknowledges "a pronounced performance dip" but offers no explanation for the underlying cause.

- **Computational cost of the data curation pipeline is opaque (Section 2.1–2.2):** The proposed pipeline requires training multiple models from scratch under leave-one-out configurations, training separate domain-specialized models to convergence, computing Hessian-based influence scores at 10 checkpoints each, and iterating data-model co-evolution. The total compute invested in deciding how to train is not reported, making it difficult to assess net efficiency. This is a notable omission given the paper's emphasis on token efficiency.

- **Influence score reliability is not internally validated (Section 2.2):** The paper does not provide correlation analysis between influence scores and downstream performance, comparison with random subsets, or error bars on influence estimates. Given known instability of Hessian-based influence functions at this scale, some validation would strengthen confidence in the method.

### Trivial
- None beyond parser-extraction artifacts that do not reflect on the paper.

## Nice-to-Haves
- Comparison against simpler data-pruning baselines (e.g., DSIR, D4, or perplexity filtering) would help contextualize whether the complex influence-based approach adds value over simpler alternatives.
- Discussion of data repetition effects (the model trains on ~4.2T tokens from ~2T unique data, meaning ~2× repetition).
- Reporting of training variance / multiple seeds for key results.

## Removed Points

The following points from the inputs were removed with justification:

- **"Benchmark-free" overstatement:** REMOVED. The paper's claim is that benchmark test sets are not accessed during training or mixture construction — which is literally true from the description. The critic argued capability-probing datasets encode benchmark preferences indirectly, but the paper uses general quality/relevance filtering (FineWeb-Edu classifier, Ask-LLM scoring for reasoning relevance), not benchmark-specific information.
- **AIME comparison conflating pre- and post-training:** REMOVED. The critic claimed the abstract's AIME comparison (15.5 vs. 0.6 vs. 0.3) is unfair because it compares post-trained vs. base models. The paper describes these as "prior models trained on fully open-sourced data" — all fully trained versions.
- **Mid-training MMLU curve "dips from 38.0 to 29.0":** REMOVED as factually wrong. The critic confused original and subsampled values. The original goes 38.0 → 31.0 (not to 29.0, which is the subsampled value at step 30K). The corrected concern about unusual training dynamics is retained in Weaknesses (Minor).
- **Missing related works:** REMOVED per hard rules (cannot confirm existence of unmentioned works without external sources).
- **Missing baselines (DCLM, Phi):** REMOVED. The paper's scope is comparison with fully-open-source models (OLMo, SmolLM), which is a clearly stated scope choice.
- **Strength Finder generic praise:** REMOVED ("addresses an important problem," generic platitudes).

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any observation about the paper's methodology or results that the paper itself does not articulate.

## Suggestions

1. Reframe the Qwen3 comparison to prominently include FLOPs alongside token counts, or make the FLOPs plot (Figure 1) the primary comparison.
2. Either directly test the "2T tokens are sufficient" claim with an experiment training on exactly 2T unique tokens without resampling, or rephrase it to "we curated ~2T unique tokens, which when resampled to 4.2T yields strong performance."
3. Investigate and explain the anomalous MMLU training pattern in Figure 6 — is the spike at 30K reproducible, and what causes the subsequent drop?
4. Report the total compute cost of the data curation pipeline (LOO runs, domain models, influence computation) alongside the final training FLOPs.
5. Add internal validation of influence scores (e.g., correlation analysis, comparison against random subsets).

**Calibration Report:**

Round 1 bracket: 5.5–7.5. Round 2 narrowed with these anchors:

| Anchor Paper | Avg Score | Round | Comparison to this paper |
|---|---|---|---|
| phi-1 (avg 6.00, Reject) | 6.00 | 1 | Our paper is clearly stronger: open data/recipes vs proprietary data generation, controlled ablation (Table 2), principled influence-based pipeline vs simple filtering. |
| NanoLM (avg 5.50, Reject) | 5.50 | 1 | Our paper is stronger: broader scope, concrete model release, more rigorous methodology. |
| RegMix (avg 7.20, Accept) | 7.20 | 2 | Our paper is slightly below: RegMix is cleaner methodologically with tighter validation. Our paper has broader scope but some overclaims and opaque compute costs. |
| What Kind of Pretraining Data (avg 6.75, Accept) | 6.75 | 2 | Comparable quality but different scope. Their narrow focus (80 queries) is offset by our overclaims. |
| Smaller, Weaker, Yet Better (avg 7.00, Accept) | 7.00 | 2 | Our paper is below: that paper has clearer hypothesis testing and cleaner execution. |

Final score: 6.5 — positioned between phi-1 (6.00) and RegMix (7.20), closest to the "What Kind of Pretraining Data" anchor (6.75). The paper's open release, clean Table 2 ablation, and principled LOO+influence pipeline are genuine strengths, but the unsupported "2T sufficient" claim and opaque compute costs prevent a higher score.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>