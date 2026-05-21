## Summary

This paper proposes EDPA (Embedding Disruption Patch Attack), a model-agnostic adversarial patch attack for VLA (Vision-Language-Action) models that requires only encoder parameters — unlike prior attacks (UADA/UPA) that demand full model access and action-space knowledge. EDPA uses two losses: a patch contrastive loss and an image-instruction alignment loss. The paper also proposes an adversarial fine-tuning defense for the visual encoder. Experiments on LIBERO across three VLA models (OpenVLA, OpenVLA-OFT, π₀) show that EDPA drives failure rates to near 100% on OpenVLA and substantially degrades the others.

## Strengths

1. **Practical, model-agnostic attack with reduced access requirements.** EDPA requires only encoder parameters, no knowledge of the action space or robotic manipulator, and no LVLM backbone access. Table 1 systematically contrasts this with UADA and UPA, and Section 3.2's loss functions operate purely on latent representations to achieve this agnosticism. This is a clear advance over prior work for real-world threat modeling.

2. **Consistent attack effectiveness across diverse VLA architectures.** Table 2 shows EDPA drives OpenVLA's failure rate to 100% on all four LIBERO suites. Table 3 extends this to OpenVLA-OFT (e.g., 2.8% clean → 80.8% on Goal) and π₀ (12.0% → 44.3% on Goal), demonstrating that the attack transfers as a method (not just a patch) to models with different architectures and camera configurations without modification.

3. **Reproducible methodology with clear pseudocode.** Algorithm 1 provides explicit pseudocode for the adversarial fine-tuning procedure. Hyperparameters for both attack and defense are specified in Section 4.1 (α₁=0.8, α₂=0.5, φ=1000, K=1, η_δ=2/255), enabling direct replication.

4. **Insightful visual analysis of learned patches.** Figure 2 reveals that all generated adversarial patches exhibit structural patterns resembling a robotic arm. Section 5 builds on this to propose a well-reasoned hypothesis about visual encoders overfitting to the constrained viewpoints in robotic datasets, which explains the differential robustness across models.

## Weaknesses

### Fatal
None.

### Major

1. **Overstated defense claims.** The paper describes the defense as "effectively mitigat[ing]" the degradation (Abstract, Conclusion), but Table 2 tells a different story: after adversarial fine-tuning, EDPA's failure rate on the Long suite only drops from 100% to 91.2%, and from 100% to 73.9% on Goal. A model that still fails 91.2% of the time is not meaningfully robust. The defense provides partial improvement — reducing the attack's impact from total to merely severe — but this is not "effective mitigation." The language should be replaced with a candid acknowledgment that the defense is a step in the right direction, not a solution. The same issue applies to UADA (97.4% on Long) and UPA (86.7% on Long) after defense.

2. **Defense evaluation limited to a single model.** The attack is demonstrated on three architectures (OpenVLA, OpenVLA-OFT, π₀), supporting its claimed generality. However, the defense is only evaluated on OpenVLA (Section 4.2). Section 3 notes "OpenVLA exhibited the weakest robustness against EDPA" as justification, but this does not establish that the defense is model-agnostic or even effective on other architectures. Without evidence on at least one additional VLA, the defense claims remain unsubstantiated for architectures beyond OpenVLA. The paper should either test the defense on another model, or clearly state this as a limitation and temper the claims.

### Minor

3. **No ablation of the two attack loss components.** The attack combines a patch contrastive loss (Eq. 2) and an image-instruction alignment loss (Eq. 3) via a weighted sum with α₁=0.8, but the paper does not ablate their individual contributions. An ablation showing the failure rate of each loss in isolation on at least one task suite would provide evidence that both are needed and justify the two-loss formulation.

4. **No analysis of attack transferability.** Since EDPA is claimed to be model-agnostic, a relevant practical question is whether a patch optimized on OpenVLA's encoder transfers to OpenVLA-OFT or π₀. The paper evaluates the attack as a procedure (generate patches per model) but does not test cross-model patch transfer. If patches do not transfer, the attack still requires some model-specific access (the specific encoder), which weakens the "agnostic" framing.

5. **The patch contrastive loss (Eq. 2) uses an InfoNCE-style formulation over spatial positions within a single image.** Treating the same-index patch pair as positive and other indices as negatives is an unusual application of InfoNCE, which is typically applied across images/samples. While the attack works empirically, the paper's justification is limited to "inspired by InfoNCE" without explaining why this formulation is appropriate for disrupting visual understanding. A clearer rationale or a simpler alternative (e.g., directly maximizing cosine distance between corresponding patches) should be discussed.

### Trivial
None.

## Nice-to-Haves
- A sensitivity analysis for hyperparameter α₁ in the main text (currently deferred to the appendix).
- An analysis of how the defense generalizes to different patch sizes, shapes, or adversarial patterns beyond the fixed 50×50 configuration.
- Confidence intervals or statistical significance tests for the key comparisons across task suites.

## Removed Points
- **"Patch visualization hypothesis is speculative"**: The paper (Section 5) explicitly says "we propose a hypothesis" and "this hypothesis also helps explain." The hypothesis is clearly labeled as such. This criticism misreads the paper.
- **"No statistical significance assessment"**: Standard deviations over three runs are reported, which is standard practice for this type of benchmark. Asking for formal significance tests beyond this is not a weakness.
- **"Patch reset frequency φ=1000 seems arbitrary"**: The paper explains it prevents overfitting to a specific patch. This is a reasonable justification sufficient for the systems paper context.
- **"Defense results show non-monotonic behavior"**: On Goal suite, clean performance improves from 26.9% to 22.8%. This is a small fluctuation within variance, not a meaningful non-monotonicity requiring special explanation.
- **"Missing limitation about patch size/shape generalization"**: This is a reasonable suggestion but belongs in nice-to-have, not as a weakness.
- **"Formatting/style nitpicks"**: Parser-related artifacts, not author errors.
- **"Sensitivity analysis should be in main text"**: Acceptable to defer to appendix for a new-method paper.
- **"Section 4.2 defense results against random noise not discussed"**: The paper does note this indirectly through the reported numbers, and the primary focus is adversarial robustness.

## Novel Insights
None beyond the paper's own contributions. The calibration process did not surface a novel perspective that the paper itself fails to articulate.

## Suggestions
1. Replace "effectively mitigates" and similar language with more measured phrasing that acknowledges the defense reduces but does not eliminate the threat (e.g., "partially mitigates" or "reduces the impact").
2. Test the adversarial fine-tuning defense on at least one additional VLA model (e.g., OpenVLA-OFT on a single task suite) to support the claim of generality.
3. Add an ablation study of the two attack loss components (patch contrastive vs. alignment loss in isolation) on at least one LIBERO suite to demonstrate that both are necessary.
4. Test cross-model transfer of EDPA patches (e.g., patch optimized on OpenVLA evaluated on OpenVLA-OFT) to clarify the practical threat model.

## Score and Decision

**Calibration Anchors (retrieved across all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| KBSHR4h8XV.md | 3.33 | R1 | Significantly weaker — reject on VLA paper with limited experiments |
| I05Z6KjQ9K.md | 2.50 | R1 | Withdrawn; substantially less developed than current paper |
| ywgwArtbDq.md | 3.00 | R1 | CAPTCHA adversarial examples; different domain, lower quality |
| oyXoGJQlUf.md | 3.00 | R1 | GRAIL robotic planning; weaker empirical evaluation |
| **wvFnqVVUhN.md** | **6.25** | R1,R2 | VLM transferability study with 40+ models; more comprehensive evaluation but different contribution type. Current paper has stronger methodological novelty but narrower evaluation → comparable |
| **b1CVu9l5GO.md** | **7.00** | R1 | TraceVLA — VLA model improvement paper with strong real-robot results; stronger empirical demonstration → current paper weaker |
| **PdA9HAxO4w.md** | **5.00** | R1,R2 | Universal adversarial perturbations for VLP; rejected for poor loss motivation and weak comparison. Current paper is clearly stronger in evaluation and practical motivation |
| **iR5qF9N1Ge.md** | **5.80** | R1,R2 | MAA attack on VLP models; rejected despite comprehensive experiments. Current paper's contribution is more cleanly novel → current paper slightly above |
| **1XxNbecjXe.md** | **5.50** | R2 | Soft prompts for VLMs; rejected primarily on novelty. Current paper has stronger methodological novelty → above |
| **BteuUysuXX.md** | **6.67** | R2 | Energy-latency attack on VLMs; accepted despite loss-motivation concerns. Current paper faces similar issues but defense is weaker → slightly below |
| **nZP10evtkV.md** | **6.20** | R2 | Optimal transport patch attack; accepted poster. Similar structure (new attack method + solid evaluation). Current paper comparable |
| WyEdX2R4er.md | 8.00 | R1 | Clearly stronger — broader, more rigorous VLM study |
| 7gUrYE50Rb.md | 8.00 | R1 | Significantly stronger — EQA with large-scale dataset |
| TPZRq4FALB.md | 8.00 | R1 | Stronger — multi-modal test-time adaptation |
| kxnoqaisCT.md | 7.75 | R1 | Stronger — GUI agent grounding |

**Round 1 bracket**: 5–7
**Round 2 narrowing**: The paper sits above the rejected anchors (5.0, 5.5, 5.8) and is comparable to nZP10evtkV (6.20) and slightly below BteuUysuXX (6.67). The main contribution — the EDPA attack — is solid and practically motivated, but the defense overclaim and limited defense evaluation prevent it from reaching the 6.5+ tier.
**Final score**: 6.0

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>