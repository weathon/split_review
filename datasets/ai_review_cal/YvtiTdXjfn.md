- Decision: Reject
- Avg Score: 5.33
- Scores: 6, 5, 5
Now I have all the information I need to write the final consolidated review.

---

## Summary

This paper presents SED (Scalable Ensemble Diversification), a method that scales disagreement-based ensemble diversification to ImageNet-scale without requiring external OOD data. SED introduces three innovations: (1) dynamic hard-sample selection from the training set using an ensemble-loss-based weight, (2) stochastic pair selection (random single pair per batch) to reduce computational cost from O(M²) to O(1), and (3) last-layer-only training on a frozen backbone. The paper also proposes a Predictive Diversity Score (PDS) for OOD detection. Experiments show that SED produces dramatically more diverse ensembles (#unique scores of 5.00 vs ~1.0 for baselines), improves OOD generalization (e.g., 48.7% vs 46.5% on ImageNet-R for M=5 prediction ensemble), and achieves state-of-the-art OOD detection AUROC on four benchmarks when combined with PDS.

## Strengths

- **Dramatic diversity increase (Table 1):** SED-A2D achieves a #unique score of 5.00 (the maximum possible for M=5) on IN-Val, IN-C-1, and IN-C-5, compared to at most 1.11 for deep ensemble, A2D, and DivDis baselines. This is a clear and substantial verification that SED produces genuinely diverse ensembles at ImageNet scale — a regime where prior disagreement-based methods failed to create meaningful diversity.

- **Consistent OOD generalization gains (Table 2):** Under the prediction ensemble aggregation (the most practical setting), SED-A2D achieves 48.7% on ImageNet-R (M=5), outperforming the best baseline (deep ensemble + diverse HPs at 46.5%). For M=50, the gap widens to 53.8% vs. 48.5%. Improvements are also seen on ImageNet-A and competitive results on ImageNet-C, demonstrating that increased diversity translates into better OOD generalization across multiple test distributions.

- **State-of-the-art OOD detection with PDS (Table 3):** SED-A2D with PDS achieves the highest AUROC on all four OOD test sets (IN-C-1: 0.681, IN-C-5: 0.894, iNaturalist: 0.977, OpenImages: 0.941), outperforming every baseline including BMA variants of deep ensembles and A2D. The PDS score's effectiveness is clearly tied to ensemble diversity, as shown by the jump from deep ensemble (0.589 on OpenImages) to SED-A2D (0.941).

- **Computational scaling (Section 3.2):** The stochastic pair selection and last-layer-only training jointly reduce the per-iteration cost of the diversity term from O(M²) to O(1), enabling ensemble sizes up to M=50 at ImageNet scale — a regime previously inaccessible to disagreement-based methods.

- **Elimination of separate OOD data (Section 3.1):** The dynamic hard-sample weighting based on ensemble loss gradient (Eq. 4, with the batch-normalization property that α_B = 1/avg_loss) provides a principled way to identify disagreement candidates from the training data itself, removing the requirement for an external OOD dataset that prior A2D/DivDis methods depend on.

- **Qualitative validation (Figure 2):** The paper shows ImageNet-R samples with high vs. low PDS; high-PDS images are visually ambiguous (e.g., "cowboy hat" also eliciting "comic book" predictions), confirming that the diversity measure captures meaningful ambiguity rather than noise.

- **λ-Diversity-Detection correspondence (Figure 1):** Both PDS and AUROC rise sharply in the same λ interval (10⁻¹ to 10¹), providing evidence that the increased diversity directly drives OOD detection gains rather than being a spurious correlation.

## Weaknesses

### Fatal

None.

### Major

- **No ablation isolating the three proposed innovations.** The paper claims three technical contributions (dynamic hard-sample selection, stochastic pair selection, last-layer-only training) but provides no ablation study that isolates the effect of any single component. Figures 1 ablates λ (diversification strength) but not the mechanisms themselves. It is therefore impossible to determine whether the observed gains come from dynamic weighting, stochastic pairing, the last-layer trick, or simply their combination. The paper also notes (Section 3.2) that "stochastic sum sometimes induces diversity by itself" without supporting evidence — further underscoring the need for an ablation. Without this, the contributions remain poorly characterized and the method appears as a bundle of heuristics whose individual necessity is unverified.

- **The A2D/DivDis baselines are given access to test-distribution-like data.** A2D and DivDis use ImageNet-R as their OOD disagreement data during training (line 225, Table 2 caption), while ImageNet-R is also a primary OOD test set on which OOD generalization is evaluated (Table 2). This means these baselines receive training signal from examples drawn from a distribution that overlaps with the test set, while SED does not use any external OOD data. The paper claims this choice "has little influence on the results" (citing Table 5 in the appendix, which is not available in the main text for verification). However, this concern is partially mitigated by the fact that SED still outperforms A2D on ImageNet-R (48.7% vs. 45.2% for prediction ensemble, M=5) despite this asymmetry — meaning SED's advantage holds even when the baseline has an information advantage. The comparison should be re-run with A2D/DivDis using a truly held-out OOD dataset (e.g., a random subset of Places) to remove any ambiguity.

### Minor

- **No variance or error bars reported.** All results in Tables 2 and 3 are single numbers with no error bars, confidence intervals, or multiple-seed reporting. The training involves randomness from stochastic pair selection and random seeds. While the margins in Table 2 are substantial enough (2–3% on ImageNet-R, 3% on ImageNet-A) that they are unlikely to be noise, the lack of variance estimates is a weakness in presentation rigor.

- **The "oracle selection" evaluation is misleadingly named and conflates test-set-dependent selection with true ensemble improvement.** The oracle selection (choosing the best single model per OOD test set) does not represent a usable method — it is standard in the diversification literature as a diagnostic, but the paper's description ("the best-performing individual model is chosen from an ensemble," line 302) could mislead readers into interpreting it as a practical result.

- **The reported results for OOD detection in Table 3 use different λ values per detector type (covariate vs. semantic shift), meaning the results for different OOD datasets come from different ensemble checkpoints.** While the paper is transparent about this (Table 1 caption, line 259), it means the reader cannot compare a single trained ensemble across all OOD detection tasks simultaneously. The paper would be strengthened by reporting results from a single unified λ.

- **Unsupported claim about stochastic pair selection.** The paper states "we noticed empirically that this stochastic sum sometimes induces diversity by itself (without a diversification term) and leads to better performance" (line 176) without presenting any evidence. If true, this could partially undermine the necessity of the diversification loss itself.

### Trivial

- Line 136 contains a typographical issue: "such OOD that that clearly differs."

## Nice-to-Haves

- Report wall-clock training time and memory usage per epoch for different ensemble sizes, to substantiate the O(1) vs. O(M²) complexity claim with concrete measurements.
- Ablate the number of stochastic pairs |ℐ| (the paper references Table stoch_sum_abl in the appendix).
- Compare PDS against established OOD detection scores (MSP, Energy, Mahalanobis distance) on the same backbone to better support the claim that it "surpasses a large number of OOD detection baselines."

## Removed Points

These points were flagged during review synthesis but removed as invalid, non-substantive, or not verifiable from the paper as written.

- **"PDS conflates aleatoric and epistemic uncertainty" (Harsh Critic Point 3):** REMOVED because the critic's analysis is mathematically incorrect. PDS = (1/C)Σ_c max_m p_c^m(x). For ImageNet (C=1000), even if all 5 ensemble members each predict a different class with probability 1, PDS = 5/1000 = 0.005 (low, not high). If all members output uniform probabilities, PDS ≈ 1/C ≈ 0.001. The critic forgot the 1/C normalization factor. The paper's derivation and claims about PDS are sound.

- **"Missing appendix materials / missing Table 5 / missing ablation tables":** REMOVED per review guidelines. The parser strips appendix content from all papers; these materials exist in the original submission.

- **"Section 3.1 α_n formula uses an unjustified square":** REMOVED because the paper explicitly justifies this design choice: the square in the denominator ensures that α_B (batch-wise average weight) equals 1/avg_batch_CE, which gives the desired property that the overall weighting level is inversely proportional to average ensemble loss (low trust early, high trust late).

- **"A2D reimplementation may not be competitive under shallow-ensemble setting":** REMOVED because this concern applies symmetrically to all methods (SED and A2D both use the same frozen backbone + last-2-layer training). The comparison is fair; the question is whether the baselines are well-tuned, not whether the comparison is asymmetric.

- **"The paper should cite additional related work":** REMOVED per guidelines (reviewer does not have external sources to verify missing citations).

- **Various formatting/style nitpicks and requests for content in the stripped appendix:** REMOVED per guidelines.

## Novel Insights

None beyond the paper's own contributions. The two reviewers' analyses did not surface any insight about the paper that goes beyond what the authors themselves articulate. The core finding — that disagreement-based diversification can be scaled to ImageNet by substituting hard training samples for OOD data and using stochastic pair selection — is the paper's own contribution, and neither reviewer identified an unanticipated implication or connection.

## Suggestions

1. **Add an ablation study isolating the three components**: The most impactful revision would be a table showing (a) full SED, (b) SED without dynamic weighting (uniform α_n), (c) SED with exhaustive pairs (no stochastic selection), (d) SED with full fine-tuning instead of last-layer-only. This would validate the individual necessity of each design choice.

2. **Run A2D/DivDis with a held-out OOD dataset** (e.g., a random subset of Places or a corruption-augmented version of the training data) instead of ImageNet-R, to directly settle the concern about test-set leakage. Even if the results are similar (as the paper claims), showing them explicitly would eliminate ambiguity.

3. **Report results over 3 random seeds** with mean and standard deviation for the key entries in Tables 2 and 3, particularly for the prediction ensemble results where the margins are 2–3%.

4. **Provide results for a single unified λ** alongside the per-detector-type results, to give readers a sense of the practical performance of a single trained ensemble across all OOD detection tasks.
