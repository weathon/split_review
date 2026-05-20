Now I have enough information. Let me write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper proposes statistical tests based on permutation equivariance of training dynamics to determine whether two language models were independently trained, using only their weights. The core framework (PERMTEST) produces exact p-values by permuting hidden units to generate identically-distributed copies of a model, and the authors develop test statistics based on matching hidden units via the Hungarian algorithm. The robust GLU-based variant resists adversarial transformations, and experiments on 21 open-weight models (210 pairs) demonstrate the tests reliably identify all 69 dependent pairs while controlling false positives.

## Strengths

- **Exact p-values with formal guarantees (Theorem 1)**: The PERMTEST framework is sound — under the null hypothesis (independent models), the p-value from Algorithm 1 is provably uniformly distributed on {i/(T+1)}. This is a genuine theoretical contribution and contrasts with prior heuristic approaches (Zeng et al., 2024; Xu et al., 2024). The proof is clear and follows from the definitions of Π-equivariance and Π-invariance.

- **Strong empirical separation across 210 model pairs**: Table 1 and the broader evaluation (69 dependent pairs, 141 independent pairs) show clean separation: all dependent pairs yield p-values at numerical underflow (ε ≈ 2.2e-308) for φ_U and φ_H, while independent pairs yield valid, non-significant p-values. Detection persists even after 750B additional fine-tuning tokens (Llama 2 → Llemma).

- **Robustness to adversarial MLP retraining**: The robust statistic φ_MATCH remains effective even after each MLP layer is retrained from scratch with doubled width (Section 4.2.1). The statistic for dependent pairs stays at numerical underflow, demonstrating resilience to a strong adversarial manipulation that prior work cannot withstand.

- **Fine-grained layer-level forensics**: By computing φ_MATCH on all pairs of MLP blocks across two models, the method identifies which specific blocks of Llama 3.1-8B were used to initialize Llama 3.2-3B (Figure 4). This goes beyond binary testing to provide architectural provenance information.

- **Cross-architecture and cross-dimension applicability**: The robust test works across models with different hidden dimensions (e.g., Llama-7B vs. ShearedLlama 1.3B) and different architectures (Mistral, StripedHyena, BERT, Phi-3), as shown in Section 4.3.

## Weaknesses

### Fatal
None.

### Major

- **Unjustified claim about matching uniformity under the null**: The paper states (Section 3.2, line 113) that "if θ_1 ⟂ θ_2 then letting π = LAP(C) in MATCH is equivalent in distribution to sampling π ∼ Unif(Π)" and uses this to justify converting the Spearman correlation to a p-value via `scipy.stats` rather than running PERMTEST. This claim is stated without proof or even a sketch of the argument. While a symmetry-based proof exists (the Π-invariance of each model's distribution implies the matching distribution is uniform over the permutation group — see below for the argument), the paper provides no such reasoning. Given that this shortcut is central to how the main test statistics (φ_U, φ_H) produce their p-values, the absence of justification is a significant gap that must be addressed (either by providing the proof or by characterizing the procedure as approximate and adding calibration evidence).

  *Why this is major, not fatal*: The claim is mathematically defensible. Let π(U₂) denote permuting the rows of U₂ by π. Under H₀, U₁ and U₂ are independent, and the distribution of U₂ is Π-invariant (rows exchangeable). Thus (U₁, U₂) and (U₁, π(U₂)) have the same joint distribution. Since LAP(C_π) = π^{-1}∘LAP(C) and C_π has the same distribution as C, the distribution of LAP(C) is invariant under left-multiplication by any group element, which forces it to be uniform. The paper should make this argument explicit.

- **Missing calibration plots for φ_U and φ_H**: The paper provides a calibration plot (Figure 3) for the robust statistic φ_MATCH, demonstrating near-uniformity under the null for independent model pairs. However, no analogous calibration plot is shown for φ_U and φ_H. While the independent-pair p-values in Table 1 (0.60, 0.16, 0.25, 0.36, 0.36, 0.64, 0.71, 0.88) look reasonable, a systematic calibration curve on all 141 independent pairs would be the expected standard for a test claiming exactness. This should be added.

### Minor

- **φ_ℓ₂ comparison with FISHER aggregation not shown in main table**: Footnote 3 notes that aggregating φ_ℓ₂ over blocks with FISHER yields p-values < 1e-30 for dependent pairs, but this is not reported in Table 1, which shows only the PERMTEST-with-T=99 result (p=0.01). Since FISHER aggregation substantially boosts power, the main comparison would be fairer with the aggregated results included.

- **Limited MLP retraining evaluation**: The adversarial MLP retraining experiment (Section 4.2.1) tests only one model pair (vicuna-7b-v1.5 vs. Llama-2-7b-hf). While the results are impressive (φ_MATCH still at ε for all 32 retrained layers), testing additional pairs would increase confidence in the robustness claim.

- **Adversarial transformation details somewhat underspecified**: The paper states models are "randomly permute[d] and rotate[d]" to simulate an adversary, but does not explicitly state how the rotation is applied or whether it exactly preserves the model output. The description should be more precise (presumably a random orthogonal matrix applied to the concatenated rows?).

### Trivial
None.

## Nice-to-Haves
- Adding a direct empirical comparison with Zeng et al. (2024) on the same model pairs (not just the adversarial construction in Appendix D.1) would help calibrate the relative strengths of the approaches.
- A brief discussion of computational cost for the Hungarian algorithm on large hidden dimensions (e.g., Llama-70B with h=8192) would be useful for practitioners.

## Removed Points

These points are flagged to be removed, treat them with caution:
- **Critic's claim that "LAP(C) ∼ Unif(Π) is false in general"**: My analysis shows this claim IS mathematically correct under the paper's assumptions (Π-invariance of the underlying distributions). The symmetry argument above demonstrates it. Thus this is not a "fatal flaw," just a missing justification.
- **Critic's claim that "this cannot be fixed by adding small experiments; the methodology must be revised"**: Overstated. The paper can address this by either (a) providing the symmetry proof, or (b) adding calibration plots and characterizing the shortcut as approximate. Neither requires a complete methodology revision.
- **Missing related work complaint**: Removed per instruction — I cannot verify whether specific works are missing.
- **Reproducibility nitpicks (runtime, hyperparameters in appendix)**: Standard for conference submissions; the appendix exists in the original submission.
- *Strength Finder's generic strength about "addressing an important problem"*: This is generic and applies to many papers; removed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine gap in theoretical presentation (the uniformity claim for LAP is stated without proof) but do not identify any novel connection to other fields or analytical frameworks that the paper itself missed.

## Suggestions

1. **Provide the symmetry proof** for the claim that LAP(C) ∼ Unif(Π) under H₀. This is straightforward (as sketched above) and would resolve the main theoretical concern.

2. **Add calibration plots** for φ_U and φ_H across all 141 independent model pairs (analogous to Figure 3 for φ_MATCH). This would empirically validate the behavior under the null and address the reviewer's concern about Type I error control.

3. **Include φ_ℓ₂ results with FISHER aggregation** in the main table (not just a footnote) for fair comparison.

4. **Clarify the adversarial transformation** (rotation) in more detail, and ideally test MLP retraining on at least one additional model pair.

5. **Replace or supplement** the Spearman-based p-value with PERMTEST for the main statistics, at least as an ablation, to remove any theoretical doubt about exactness.

---

## Score and Decision

### Round 1 (Bracketing)

| Anchor Path | Avg Score | Round | Comparison |
|---|---|---|---|
| ZNMZdEQQga.md | 3.00 | R1 | Weak paper with unclear contribution; current paper is substantially stronger |
| 9L9j5bQPIY.md | 2.50 | R1 | Weak paper about neural network autoencoding; much less coherent than current paper |
| gInIbukM0R.md | 2.50 | R1 | Weak paper on emergence metrics; little in common |
| vvROJOMYP8.md | 2.50 | R1 | About style transfer; unrelated |
| QCDdI7X3f9.md | 6.50 | R1 | Model equality testing via MMD; similar application. Current paper is more ambitious theoretically and has stronger empirical breadth but a notable justification gap in one component. Comparable quality. |
| NvRVYVN106.md | 5.25 | R1 | Privacy breach detection; shares two-sample testing framing but less related. Current paper is stronger. |
| fwHVclv0ij.md | 5.25 | R1 | Black-box LLM change detection; different methodology. Current paper is stronger theoretically. |
| l18hiEXRJS.md | 4.50 | R1 | Data shift detection via activation graphs; solid but less ambitious. |
| EUSkm2sVJ6.md | 7.60 | R1 | High-quality oracle paper about data usage inference; stronger empirical methodology |
| UHPnqSTBPO.md | 8.00 | R1 | Strong oral paper; different topic |
| uHLgDEgiS5.md | 8.00 | R1 | Strong oral paper; different topic |
| A3YUPeJTNR.md | 8.00 | R1 | Strong oral paper; different topic |

**Round 1 bracket: [5.0, 7.0]** – clearly above the weak papers (2.5–3.0) and below the orals (7.5+). Comparable to the poster-level papers in the 5.25–6.5 range.

### Round 2 (Narrowing)

| Anchor Path | Avg Score | Round | Comparison |
|---|---|---|---|
| KS8mIvetg2.md | 7.50 | R2 | Test set contamination detection with exact guarantees; oral-level. Current paper is slightly weaker because of the justification gap. |
| KRMSH1GxUK.md | 5.80 | R2 | Watermarking for IP detection; poster. Current paper has stronger theoretical foundations and broader evaluation. |
| f8S3aLm0Vp.md | 6.50 | R2 | Unauthorized data usage detection in diffusion models; poster. Comparable quality but different domain. |
| z9j7wctoGV.md | 6.00 | R2 | MGT detection via kernel relative test; poster. Current paper has stronger theory and more comprehensive evaluation. |

**Final bracket narrowing: [5.5, 6.5]** → Score = **6.0**

The paper is stronger than the 5.8 watermarking anchor (greater novelty, broader scope, stronger theory) and comparable to the 6.0 and 6.5 anchors. It is weaker than the 7.5 oral anchor (which has a cleaner theoretical story). The score of 6.0 reflects that the paper makes a genuine contribution (clever framework, strong empirical validation) but has a significant presentation gap (the LAP uniformity claim is asserted without proof) that prevents it from being higher.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>