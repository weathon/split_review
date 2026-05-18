I have all the information needed. Let me now produce the final consolidated review.

---

## Summary

The paper introduces Spectral Contrastive Regression, a method for improving generalization in regression tasks through two novel losses: (1) L_std, which models the feature-label distance proportion as a variable mapping function (rather than a constant as in prior work) and minimizes its standard deviation, and (2) L_svd, which aligns the largest singular value of feature representations across real and C-Mixup-synthesized domains to reduce distribution discrepancy. The method is evaluated on eight regression benchmarks across both in-distribution and out-of-distribution settings.

## Strengths

1. **Novel formulation of the feature-label proportion as a variable mapping.** Prior work (RML) treats the proportion between feature distance and label distance as a constant. The paper argues this should be a variable mapping function and proposes L_std to reduce its variance. This is a conceptually interesting departure from existing approaches and is supported by t-SNE visualizations showing more discriminative embedding patterns (Figure 1).

2. **Spectral norm alignment for OOD regression is an underexplored idea.** The insight that aligning only the top singular value (rather than the full Frobenius or nuclear norm) may be more effective for domain alignment in regression is well-motivated. On the MPI3D benchmark (Tables 3–4), where no fine-tuning confound exists, spectral norm alignment consistently outperforms alignment with nuclear and Frobenius norms across three domain shifts, providing clean empirical evidence for this component.

3. **Evaluation across eight diverse regression benchmarks covering tabular, time-series, and image data.** The method is tested on 3 in-distribution and 5 out-of-distribution datasets. The MPI3D experiments (3 domain shifts × 2 metrics × comparison against multiple norm choices) are a reasonably thorough evaluation of the spectral alignment approach.

4. **Ablation of the two components on MPI3D (no fine-tuning confound).** On MPI3D, the paper compares L_std alone, L_svd with various norms, and the full method — all without the FT strategy. These results provide evidence that both losses contribute beyond the baseline (C-Mixup) and beyond each other.

## Weaknesses

### Major

1. **Theorem 1 assumes an invertible weight matrix without justification (theoretical flaw).** The derivation of the upper bound for the proportional distance d_r uses W_p*^{-1}. In standard regression, the optimal weight W_p* has shape (output_dim × feature_dim). When output_dim < feature_dim (e.g., scalar regression with high-dimensional features), W_p* is non-square and has no inverse. Even when output_dim = feature_dim, invertibility is a strong assumption not justified in the paper. Consequently, the mathematical grounding for the boundedness of d_r, the link to Remarks 1 and 2, and the motivation for L_std as a consequence of Theorem 1 are built on an unsupported premise. The authors should reframe the proportional distance as a heuristic or provide a corrected derivation (e.g., using pseudoinverses under additional rank assumptions).

2. **Confounded experimental comparisons in the main results (Tables 1 and 2).** The proposed method uses a freeze-fine-tuning strategy (FT: freezing top layers except the last block) that is not applied to the baseline methods. In Table 1, the baselines (C-Mixup*, RML†, RankSim†) do not appear to use FT, while "Ours(FT+L_std)" and "Ours(FT+L_std+L_svd)" do. The improvements attributed to L_std and L_svd could plausibly come partly or entirely from the changed training procedure (FT itself). The paper states "we also provide the result of RML combined with our fine-tuning method" (line 218) but RML† is marked as results from Yao et al. (2022) — this inconsistency is unexplained. Without a controlled comparison (e.g., running all baselines with the same FT strategy, or at minimum adding an "FT only" column), the core empirical claims are not cleanly supported for Tables 1 and 2. **Mitigation**: On MPI3D (Tables 3,4), the paper explicitly states no FT is used (line 247), and these comparisons are clean. The MPI3D results provide partial support for the method, but the main claims rest substantially on Tables 1 and 2.

3. **The connection between Theorem 2 and the L_svd loss is theoretically coarse.** Even though Theorem 2 itself is mathematically valid (see Removed Points), the bound involves ||Y^h||_F (Frobenius norm of the output), while L_svd minimizes |||F_real||_2 - ||F_syn||_2| (difference of spectral norms of features). The link is via the inequality ||Y^h||_F ≤ ||F||_2||W||_2 + |b| (line 170), which is a loose bound that introduces dependence on the regression weights W and bias b. Minimizing the difference in feature spectral norms does not directly minimize the claimed bound on distribution discrepancy — it only loosely constrains an upper bound on an upper bound. This gap should be acknowledged explicitly rather than presented as a tight theoretical motivation.

### Minor

1. **Missing standard deviations/confidence intervals.** All results are reported as averages over 3 seeds without variance. For a paper making SOTA claims, readers cannot assess the reliability of the improvements.

2. **L_svd aligns only the largest singular value, which is a necessary but far-from-sufficient condition for distribution alignment.** Two feature matrices can share the same largest singular value while differing arbitrarily in other spectral dimensions or singular subspaces. This is a known limitation of spectral norm alignment; the paper does not discuss it. The MPI3D empirical results partially mitigate this concern, but the theoretical gap remains.

3. **Hyperparameters α, β not reported per dataset.** The sensitivity analysis (Figure 2) shows L_std is quite sensitive to α, yet the chosen values for each benchmark are not stated. This harms reproducibility.

4. **Inconsistency about RML+FT results.** The paper claims to provide RML+FT results (line 218), but the table description (line 221) lists RML† as from Yao et al. (2022), not re-run with FT. This discrepancy needs resolution.

5. **t-SNE visualization (Figure 1) is purely qualitative.** It supports the narrative but does not quantify what "clearer pattern" means. Not a fatal issue, but it limits the evidentiary weight of this figure.

### Trivial

- None beyond what is listed in Removed Points.

## Nice-to-Haves

- Adding an "FT only" baseline column to Tables 1 and 2 would immediately clarify the confound concern.
- Reporting α and β values per dataset in a small table would improve reproducibility.
- A discussion of the computational cost of computing SVD per batch for L_svd would be useful.
- Running baselines (C-Mixup, RML, RankSim) with the same FT procedure and reporting the results would fully resolve the controlled-comparison issue.

## Removed Points

- **Theorem 2 bound is invalid (from Harsh Critic).** *Removed as factually wrong.* The proof is mathematically correct: for MSE loss, L(h',h) = L(h-h',0). Since H is a subspace, h'' = h-h' ranges over all of H. Thus max_{h,h'} |L_P(h',h) - L_Q(h',h)| = max_{h''∈H} |L_P(h'',0) - L_Q(h'',0)| = (1/N) max_{h''} |||Y_P^{h''}||_F^2 - ||Y_Q^{h''}||_F^2|. The bound is valid (the ≤ direction is trivially true as equality). The critic's reading that "setting h'=0 loses generality" overlooks that H being a subspace ensures the zero hypothesis is in H and h'' covers all pairs.
- **C-Mixup comparison not controlling for augmentation (on MPI3D).** *Partially removed.* The reviewer claims the MPI3D baseline doesn't control for C-Mixup augmentation, but the MPI3D tables explicitly compare C-Mixup as a separate baseline, and L_std/L_svd are additive on top. The comparison of Ours vs C-Mixup on MPI3D tests whether adding L_std+L_svd improves over C-Mixup alone. This is a controlled comparison.
- **Missing appendix / proofs / references.** *Removed per parser artifact rule.* These exist in the original submission.
- **Pure formatting nitpicks.** *Removed per rules.*

## Novel Insights

None beyond the paper's own contributions. The reviewer analyses largely trace known methodological concerns (controlled comparisons, theoretical rigor) rather than producing novel observations about the work.

## Suggestions

1. **Resolve Theorem 1.** Either justify invertibility (e.g., by assuming output_dim = feature_dim and full rank of W_p*), replace the inverse with a pseudoinverse and an additional rank assumption, or reframe the proportional distance as a heuristic without claiming a theorem-grounded upper bound.

2. **Add controlled baselines.** Rerun C-Mixup, RML, and RankSim under the same FT strategy (freeze top, unfreeze last block) and report alongside the current numbers. Add an "FT only" column (freeze strategy with only MSE loss). If FT is the same across all methods, the improvement from L_std and L_svd becomes interpretable.

3. **Clarify the theoretical link for L_svd.** Acknowledge that the connection between Theorem 2 and L_svd is inductive rather than tight: the spectral norm of features loosely upper-bounds the output norm, which in turn bounds the discrepancy. Frame L_svd as a heuristic regularizer motivated by this intuition, not as a direct corollary of Theorem 2.

4. **Report variance and hyperparameter values.** Add standard deviations or confidence intervals for all tables. Report chosen α, β values per dataset.

5. **Clarify the RML+FT status.** Either show the RML+FT column in Table 1 or remove the claim that it is provided.

## Score and Decision

The paper tackles an important underexplored problem (generalization in regression) with interesting ideas. However, the two major issues — a flawed theoretical theorem (invertibility assumption in Theorem 1) and confounded experimental comparisons in the main tables — substantially weaken the submission. The theoretical grounding for L_std needs correction, and without controlled baselines the empirical contributions for Tables 1 and 2 are uninterpretable. The MPI3D results are clean and provide partial support, but they alone do not fully substantiate the paper's SOTA claims across eight benchmarks. The paper requires major revisions before its contributions can be assessed.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>