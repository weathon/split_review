Now let me run calibration searches to bracket the paper's quality.Now let me run narrowing searches within the bracket of 4.5–5.5:Now I have enough information to write the full review. Let me synthesize all findings.

---

## Summary

LS-Merge is a model-merging framework that encodes pretrained LLM weights into a transformer-based VAE latent space, performs interpolation or averaging there, and decodes back to parameters. Its three claimed contributions are: (1) an analysis of LLM weight statistics showing heavy-tailed, leptokurtic distributions that motivate the VAE design; (2) a two-stage curriculum-trained VAE for weight encoding that outperforms PCA; and (3) a heterogeneous merging protocol using proportional layer alignment and Gaussian OT for cross-architecture model fusion.

---

## Strengths

- **Heavy-tailed weight distribution empirically documented (Table 1).** Excess kurtosis up to 15.05 in Gemma-3 self-attention layers is directly measured and motivates the two-stage curriculum (KL-off then KL-on) to avoid mode collapse — a concrete, grounded technical choice, not a generic claim.

- **Expert merging in latent space consistently outperforms weight-space baselines (Table 3).** LS-Merge (soup) achieves 56.0 MMLU, 60.1 HellaSwag, and 56.1 NLQGraph versus Greedy Soup at 50.8, 54.6, and 52.9 respectively — substantial margins across 8 benchmarks. This is the paper's strongest, most reproducible evidence.

- **Non-linear manifold demonstrated by VAE vs. PCA ablation (Table 8).** PCA collapses to near-random MMLU (25.50%) even at the mildest compression ratio r=1.6, while the VAE retains 39.89% (vs. base 41.44%). The failure is not capacity-related (performance equally poor at r=4.0), confirming the failure is structural, not dimensional. This is a meaningful, well-executed ablation.

- **Zero-shot weight-encoding generalization (Table 7).** A VAE trained only on Gemma-3-4B-it maintains near-base accuracy on unseen Gemma-3-1B-it (MMLU 39.98 vs. base 40.76) and LLaMA-3.2-1B-it (WinoGrande 61.25 vs. 61.56) at r=1.6 — strong evidence that the VAE has learned transferable weight structure.

- **Competitive with activation-based methods without data access (Table 4).** LS-Merge achieves 55.07 MMLU and 36.41 IFEval on Llama-2-13B vs. AIM's 54.18 and 32.00, showing that weight-space latent merging can match methods that require model activations.

---

## Weaknesses

### Fatal
*None.*

### Major

- **Self-merging mechanism lacks mechanistic explanation, undermining the headline Table 2 claim.** The paper describes encoding a model, "sampling multiple latent codes from its posterior distribution, merging these codes into a single representation," and decoding. The attributed mechanism is "exploring the learned parameter distribution," but this is not mechanistically accounted for. If the VAE posterior is tight (as expected for a well-trained model), averaging samples simply recovers the posterior mean — equivalent to a MAP estimate with noise reduction. If the posterior is loose, the effect is weight regularization/smoothing, not exploration. The gain of 35.13% vs. 32.20% MMLU on Gemma-3-1B-it could reflect that the VAE slightly regularizes toward a better generalization point — a much more limited claim. No posterior variance analysis or sample-count ablation is provided to distinguish these regimes. This matters because self-merging is one of two headline contributions.

- **Task Arithmetic baseline in Table 4 shows suspicious catastrophic failure.** Task Arithmetic achieves 4.20% on GSM8k — identical to the base model — while the individually fine-tuned code and instruct models score 24.10% and 43.40% respectively. A correctly configured Task Arithmetic merge of two task-specialized models should not regress all the way to base-model performance. This result indicates likely misconfiguration (e.g., coefficient tuning not performed), which would inflate LS-Merge's apparent advantage over Task Arithmetic substantially. The paper presents this as a straightforward comparison without acknowledging the anomaly.

- **VAE training data insufficiently specified, creating an internal consistency concern between Tables 7 and 8.** Section 4 states only: "Training data consist of pretrained weight snapshots for Gemma-3-1B-it and Gemma-3-4B-it." Section 5.2 trains a VAE *only* on Gemma-3-4B-it and evaluates generalization (Table 7), where Gemma-3-1B-it at r=4 reaches only 25.02% MMLU. But Table 8 shows the "LS-Merge VAE" on Gemma-3-1B-it at r=4 reaching 39.83%. The most natural explanation is that Table 8's VAE was trained on Gemma-3-1B-it weights, while Table 7's was not — but the paper never states this explicitly. Without clarification of which VAE variant applies to each table, readers cannot determine whether the strong Table 8 results reflect genuine reconstruction capability or near-memorization of the evaluation model's weights.

### Minor

- **Gaussian OT assumption is internally inconsistent with the paper's own heavy-tail motivation.** Section 3.1 establishes that LLM weights are heavy-tailed and non-Gaussian, motivating the VAE design. Section 3.3 then applies Gaussian OT alignment (approximating per-layer latent distributions as Gaussians to obtain a closed-form affine map). These two positions are in tension: the paper argues the weight distribution violates Gaussianity as a key observation, then assumes Gaussianity in the alignment step without any empirical validation that the latent distributions are approximately Gaussian. Figure 9b in the appendix (showing heterogeneous latent distributions) is referenced but not analyzed for Gaussianity.

- **Cross-family merging gains are modest and heavily dependent on a small λ (Table 5).** At λ=0.1 (90% target, 10% source), WinoGrande improves from 56.83 to 57.75, ARC-C from 42.78 to 43.34, HellaSwag from 49.07 to 50.10. Notably, OT-only (without interpolation) degrades WinoGrande to 51.13, suggesting alignment alone introduces distributional distortion. The benefit may arise from the small interpolation weight acting as a gentle regularizer rather than from meaningful cross-family knowledge transfer. Results across broader λ values are not reported, so it is unclear whether λ=0.1 is cherry-picked.

- **Inconsistent evaluation protocols between Table 3 and Table 4.** Table 3 (expert merging) uses the authors' custom evaluation code, while Table 4 uses lm-eval "for fair comparison with baselines." If lm-eval ensures fairness with external baselines, the same rationale applies to Table 3, where the gains over weight-space methods could be sensitive to evaluation tooling differences. The asymmetry is noted in the paper but not fully justified.

### Trivial

- **Section 3.3 self-merging description conflates "self-merging" and "homogeneous merging."** The text states "self-merging encodes a single model and draws multiple latent codes … which is equivalent to merging homogeneous models." This conflation is confusing — drawing multiple posterior samples from one model is conceptually different from interpolating between two separate checkpoints.

---

## Nice-to-Haves

- Show the latent-space trajectory (MMLU vs. λ) for homogeneous merging to verify that the latent space is smoother than weight space — this would be the clearest mechanistic demonstration of *why* latent merging works better than direct weight interpolation.
- Provide a sample-count ablation for self-merging (how performance varies as a function of the number of posterior samples) to clarify whether the effect is real posterior exploration or simply variance reduction.
- Validate the Gaussian approximation used in the OT step empirically (e.g., QQ-plots or normality tests on per-layer latent codes from heterogeneous models).
- Computational cost characterization (encoding/decoding time, GPU memory) for practical adoption at scale.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **"Theoretical motivation overstates the math" (Harsh Critic, Section 3.1).** Removed because the paper does not claim the Eckart-Young theorem proves the VAE will work — it uses it to show a compressive map *exists*, which is standard motivation. The inferential gap between "manifold exists" and "VAE approximates it well" is explicitly addressed by citing manifold embedding results (Bengio et al., 2012; Lahiri et al., 2016). The criticism is a scope-creep misread.

- **"Single VAE handling two architectures is unexplained" (Harsh Critic, Section 4.1).** Removed as a strawman. The paper explicitly explains the chunking mechanism in Section 3.2 that normalizes different weight shapes into fixed-size sequences; the shared encoder/decoder then operates on these standardized chunks. This is addressed directly in the paper.

- **PCA comparison is "only weakly" valid because VAE was specifically trained to reconstruct these weights (Harsh Critic, Section 5.3).** Removed. The comparison's purpose is to show whether a linear method can preserve the functional manifold — and PCA catastrophically fails, which is a valid empirical finding regardless of whether the VAE was trained on the same data. The critic's concern about a "fairer" comparison (MLP autoencoder) is a nice-to-have, not a flaw.

- **LoRA expert merging results in Table 3 may not be comparable to published results (Harsh Critic).** Removed because the paper states it uses its own evaluation code *in that section* and explicitly switches to lm-eval when comparing to external baselines in Section 4.3. The paper acknowledges the difference; there are no external published results for this specific experimental setup being claimed to be reproduced.

- **Strength: "MLP and attention layers encode complementary knowledge" (Table 6).** Retained at minor level — the ablation is real but the conclusion ("complementary functional knowledge") slightly overstates what the data shows. Table 6 shows that combined merging is best, but doesn't isolate why. Kept as a valid supporting finding, not a primary strength.

---

## Novel Insights

The most novel technical observation in this work is that LLM weights lie on a non-linear manifold that is functionally opaque to linear methods — demonstrated by the complete collapse of PCA reconstruction even at mild compression (Table 8) while the VAE remains stable. This is a direct empirical refutation of the implicit linear-subspace assumption in much prior low-rank analysis of LLM weights, and goes beyond what the paper's PCA-variance plots (Figure 2) alone would suggest: the weights being *low-rank in variance* does not mean they are *linear in function-preserving structure*.

---

## Suggestions

1. **Resolve the Table 7/Table 8 discrepancy explicitly.** State clearly which VAE (trained on which data) is used in each experiment. If Table 8 uses a VAE trained on Gemma-3-1B-it, say so and explain what that tells us (and doesn't tell us) about generalization.
2. **Investigate the Task Arithmetic baseline.** Re-run with explicit coefficient tuning and report results; if Task Arithmetic genuinely fails on this configuration, provide a brief analysis of why (e.g., conflicting task vectors for these two domains).
3. **Add a posterior-variance characterization and sample-count ablation for self-merging** to establish whether the gain comes from exploration or regularization.
4. **Report heterogeneous merging results across a range of λ values** (0.0, 0.05, 0.1, 0.2, 0.5) to assess whether λ=0.1 is optimal or cherry-picked.

---

## Score and Decision

**Calibration anchors:**

**Round 1 (bracketing):**
- `/deepreview_13k_calibration/yx8bU8T5ZN.md` — avg 2.33, Reject — delta-parameter editing paper; much simpler contribution than LS-Merge.
- `/deepreview_13k_calibration/lNtio1tdbL.md` — avg 3.00, Reject — task arithmetic gradient equivalence; technically narrower, less novel.
- `/deepreview_13k_calibration/XVHXVdoV11.md` — avg 3.40, Reject — compatible specialization via CKA; identifies a problem but proposes limited solution.
- `/deepreview_13k_calibration/lIdc5DUplq.md` — avg 4.33, Reject — SUPERMERGE gradient-based merging; incremental over task arithmetic.
- `/deepreview_13k_calibration/fvUVe2gJh0.md` — avg 5.33, Reject — what matters for model merging at scale; systematic evaluation, no new method.
- `/deepreview_13k_calibration/Bq3fEAGXUL.md` — avg 5.33, Reject — realistic evaluation of model merging; evaluation paper.
- `/deepreview_13k_calibration/2pvMZKGYDR.md` — avg 5.67, Reject — WIDEN weight disentanglement for PT+FT merging; novel method, similar scope.
- `/deepreview_13k_calibration/gU58d5QeGv.md` — avg 8.00, Accept — Würstchen text-to-image diffusion; unrelated, strong anchor only.

**Round 1 bracket: 4.0 – 5.5**

**Round 2 (narrowing):**
- `/deepreview_13k_calibration/LJGY2GVcit.md` — avg 5.50, Reject — Foldable SuperNets for merging transformers from different initializations; directly comparable problem, similar methodological limitations (empirical, limited explanation of mechanism, narrow experimental scope).
- `/deepreview_13k_calibration/t73rC2GJQJ.md` — avg 4.50, Reject — DMM distillation-based model merging for image generation; narrower problem, results dependent on specific domain.
- `/deepreview_13k_calibration/4wuvmJRAU4.md` — avg 5.00, Reject — layer shuffling and task vector superposition for multi-model compression; zero-optimization method with cleaner results.
- `/deepreview_13k_calibration/W2Wkp9MQsF.md` — avg 5.75, Accept — model folding data-free compression; cleaner contribution with stronger theoretical grounding.

**Comparison to round-2 anchors:**

LS-Merge is *comparable to or slightly weaker than* Foldable SuperNets (5.50): both are novel methods targeting harder merging problems than standard fine-tuned merging, both are empirical with limited mechanistic explanation, but LS-Merge's additional issues (suspicious Task Arithmetic baseline, under-specified training data, very small cross-family gains at λ=0.1) tilt it below FS-Merge's level. LS-Merge is *stronger than* DMM (4.50) by covering LLMs and a more principled method (OT + VAE), but weaker than WIDEN (5.67) in experimental rigor. The paper is below the model-folding accepted paper (5.75) in contribution clarity and experimental soundness.

**Final score: 4.5 — Reject.** The core expert-merging contribution is genuine and Table 3 is strong evidence, but the paper's two other headline claims (self-merging and heterogeneous merging) are either inadequately explained or produce results too small to establish the claim independently. The suspicious Task Arithmetic baseline and training data ambiguity further erode confidence. The paper is closer to the DMM (4.50) / lower-FS-Merge range than to WIDEN (5.67) or model folding (5.75).

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>