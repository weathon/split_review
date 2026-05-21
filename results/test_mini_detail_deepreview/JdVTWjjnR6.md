Now I have a clear calibration picture. Let me write the consolidated review.

**Round 1 bracket**: 4.5–6.5 (clearly above weak anchors at 3.0–3.33, clearly below top anchors at 8.0)

**Round 2 narrowing**: Comparing to anchors at 5.0–6.33 (SURE at 5.0, MoE-Retriever at 5.5, MiDl at 6.0, Synergize at 6.33):
- HiTNet is slightly stronger than MoE-Retriever (5.5) in experimental scope and ablation depth
- Weaker than MiDl (6.0) in clarity and integrity of claims
- The overclaimed improvement range, unsupported headline claim, and numerical inconsistency are real presentation issues that prevent it from reaching the 6.0 tier

---

## Summary

This paper proposes HiTNet, a dual-stream architecture for multimodal sentiment analysis under random frame-level missingness. The hippocampal-inspired intra-modal stream uses a semantic memory module with dynamic retrieval and sparse activation to recover modality-specific information. The thalamic-inspired inter-modal stream estimates confidence scores to guide cross-modal completion and suppress redundancy. Experiments on MOSI, MOSEI, and SIMS show consistent improvements over several strong baselines, with notable gains on MOSI (1.31% Acc-2 improvement) and SIMS (4.53% Acc-3 improvement).

## Strengths

- **Novel dual-stream architecture with demonstrated component independence**: The ablation study (Table 3) provides concrete evidence that both streams contribute independently — removing the inter-modal stream drops MOSI Corr from 0.539 to 0.499 and removing the intra-modal stream also degrades across multiple metrics. This directly supports the paper's core thesis that both intra-modal self-completion and inter-modal confidence-gated completion are beneficial.

- **Consistent improvements across three datasets**: Tables 1 and 2 show HiTNet achieves SOTA on MOSI (74.12% Acc-2 vs 72.81% for P-RMF) and competitive results on MOSEI and SIMS across most metrics. The gains on SIMS Acc-3 (59.28% vs 57.14% for LNLN, a 2.14pp improvement) are particularly notable.

- **Completion quality directly measured**: Figure 4 provides quantitative evidence that the Euclidean distance between completed features and complete features is markedly smaller than the distance from raw missing features, confirming the modules actually recover information rather than merely reweighting features.

- **Demonstrated generalization to modality-level missingness**: Table 4 shows HiTNet achieves 59.33% Acc-2 with only visual modality present on MOSI, a >4% absolute improvement over TETFN (55.25%), showing effectiveness beyond the frame-level setting.

- **Robustness visualized at extreme missingness**: Figure 5 shows confusion matrices at 90% missing rate where the baseline LNLN collapses to the neutral class while HiTNet maintains predictions across multiple sentiment categories.

## Weaknesses

### Major

- **Unsupported headline claim in the abstract**: The abstract claims "72.20% accuracy under extreme 90% missing conditions on MOSEI" and "1.5%–2.0% average accuracy improvements over state-of-the-art methods across all missing rates." The per-missing-rate breakdown supporting the 72.20% claim is deferred to Appendix B.3, which is not available in the main paper (line 219). This is a significant evidential gap — a headline result should be directly verifiable from the main paper's tables and figures. The claimed improvement range also does not match several key results: on MOSEI, Acc-2 improves by only 0.15pp (78.29 vs 78.14), and Acc-7 improves by 0.01pp (47.19 vs 47.18). The paper should present per-missing-rate results in the main body and calibrate the abstract claims to the actual reported gains.

- **Potential information leakage through the Semantic Memory Module**: The SMM stores key-value pairs derived from training-sample features and retrieves them at test time via cosine similarity (Eq. 2–3), then adds the retrieved value to the test feature through a gated mechanism. Because the memory values are computed from the same encoder that processes training samples, they may carry sentiment-correlated information. While this is not "label leakage" in the traditional sense (the values are feature projections, not labels), the mechanism could provide an advantage through nearest-neighbor-style transfer of label-correlated representations. The paper does not control for this — e.g., by comparing against a version where retrieved values are replaced with random features or zero vectors, or by ablating the retrieval entirely (not just removing the SMM module, but also verifying that the encoder+fusion backbone without retrieval is weaker). This concern is amplified in the modality-level missingness results (Table 4), where {V} or {A} alone show large gains with no cross-modal signal available to constrain retrieval.

- **Numerical inconsistency in reported gains**: Line 193 states "a substantial 2.56% gain in Acc-7 on MOSEI," but this figure does not match any comparison in Table 1. The closest competitor (CENET, 47.18) yields a 0.01pp difference. The best comparison (Self-MM, 44.70) yields a 2.49pp difference, close to 2.56 but not exact, and the paper does not specify the reference baseline. Similarly, the reported 1.41% F1 improvement on MOSI (74.53 vs best competitor P-RMF at 72.93 = 1.60pp) is inconsistent. These mismatches, while small, indicate imprecision in reporting that undermines trust.

### Minor

- **Missing backbone baseline in ablations**: The ablations in Table 3 remove individual components (w/o SMM, w/o CPM, w/o Intra, w/o Inter) but never remove *both* streams entirely, leaving only the unimodal encoders + vanilla fusion. Without this baseline, it is impossible to attribute how much of the gain comes from the proposed modules versus from the choice of encoder architecture or training procedure.

- **Figure 3 only shows missing rates up to 0.5**: The caption and axes in Figure 3 show performance up to 50% missing rate, but the test setup goes to 90%. Since the paper's headline claims concern extreme missingness (90%), the main figure should show the full range or include a separate figure for high missing rates.

- **Mixed results on SIMS not acknowledged**: On SIMS (Table 2), HiTNet has worse F1 (77.33 vs LNLN 79.43), worse Corr (0.389 vs P-RMF 0.414), and marginally worse MAE (0.504 vs P-RMF 0.500). The paper highlights the 4.53% Acc-3 gain but does not discuss these declines, which weakens the claim of consistent superiority.

- **Hyperparameter sensitivity without analysis**: The loss weights vary dramatically across datasets (γ=9.0 on MOSEI vs 0.1 on MOSI, α=1.5 on MOSEI vs 10 on MOSI/SIMS). The paper notes this but provides no analysis of how sensitive the results are within a reasonable range. This suggests potential brittleness in the objective.

### Trivial

- Numerical inconsistency in line 193 (2.56% gain) as discussed above.
- Figure 3 appears to label "LNLT" instead of "LNLN" in the legend (though this may be a parsing artifact).

## Nice-to-Haves

- Move per-missing-rate breakdown (currently Appendix B.3) into the main paper, or at minimum show the 90% missing rate results in a table or figure in the main body.
- Add an ablation where memory retrieval values are replaced with random or zero vectors to isolate the effect of the semantic content.
- Show that confidence scores (s_m) correlate with actual reconstruction quality or prediction uncertainty, rather than just with the missing ratio.
- Report standard deviations across seeds for key metrics to establish statistical significance.
- Add a "backbone-only" baseline (both streams removed) to Table 3.

## Removed Points

The following points from the inputs are removed with justification:

1. *"Brain inspiration is superficial / neuroscience framing is decorative"* — The paper explicitly grounds its design in SDM and Hopfield networks (Section 1, lines 27–28), which are established computational models of associative memory. The actual implementation (cosine similarity retrieval + gated addition + MoE) is a practical instantiation of content-based addressing and pattern completion — a faithful engineering translation rather than a literal biological simulation. This is standard practice for brain-inspired ML.

2. *"Existing methods LNLN and P-RMF also exploit intra-modal cues"* — The paper's claim is not that these methods completely ignore intra-modal information, but that they "fail to exploit the residual semantic cues within each modality and overlook modality-specific characteristics" (lines 19–20). LNLN focuses on text integrity; P-RMF uses latent Gaussians. Neither systematically retrieves modality-specific memory for self-completion. This is a reasonable characterization.

3. *"Reconstruction module could learn identity mapping"* — The reconstruction target is u_m = Enc_m(U_m), which is the encoded version of the *complete* input. Since the input x_m is the encoded version of the *missing* input, the reconstruction must map from missing to complete features — this is not an identity mapping. The concern is unfounded.

4. *Generic criticisms about standard deviations and reproducibility* — The paper reports results averaged over 3 seeds (line 189) and provides code in an anonymous repository. This meets the standard for this domain.

5. *"Missing related works"* — Cannot be verified without full knowledge of the literature.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine tension: the paper has a solid technical architecture with component-wise validation, but the presentation over-reaches with imprecise numerical claims (the 1.5–2.0% range, the unsupported 72.20% headline, the miscalibrated 2.56% gain). This is a case where the experimental substance is stronger than the paper's own narration of it, and the key improvement needed is honest calibration of claims to data.

## Suggestions

1. Move per-missing-rate results (including the 90% rate) from the appendix into the main paper so the headline claim is directly verifiable.
2. Calibrate the abstract's improvement range to match the actual reported numbers — distinguish percentage-point gains from relative improvements and acknowledge metrics where gains are marginal (MOSEI Acc-7, Acc-2).
3. Add a backbone-only ablation (both streams removed, just encoders + fusion) to isolate the contribution of the proposed modules versus the encoder architecture.
4. Add an ablation where SMM retrieved values are replaced with random noise or zero vectors to rule out label-correlated information transfer.
5. Correct the numerical inconsistency for the "2.56% gain in Acc-7 on MOSEI" claim in line 193.
6. Discuss the SIMS F1 and Corr declines explicitly to present a balanced picture.

## Score and Decision

**Round 1 bracket**: 4.5–6.5 (between the 3.0 weak anchor and the 8.0 strong anchor)

**Round 2 narrowing**: Compared against anchors at 5.0 (SURE), 5.5 (MoE-Retriever), 6.0 (MiDl), and 6.33 (Synergize):
- HiTNet is **stronger** than MoE-Retriever (5.5) in experimental scope (3 datasets, more comprehensive metrics, better ablation design) and clarity of writing.
- HiTNet is **weaker** than MiDl (6.0) in integrity of claims and freedom from overclaiming — MiDl's 6.0 is supported by precise reporting and a clear scope, while HiTNet's abstract makes claims that the tables do not fully substantiate.
- HiTNet is comparable to SURE (5.0) in technical contribution but with stronger empirical results on MOSI/MOSEI/SIMS.

The paper sits near the upper end of the 5.0–6.0 band. It proposes a well-motivated architecture with validated components and credible results on three datasets. However, the overclaimed improvement range, unsupported headline result (72.20%), and numerical inconsistency prevent it from reaching the 6.0 tier. A revision that fixes these presentation issues and adds the missing ablations would merit a higher score.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>