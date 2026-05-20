Now I have enough to write the review. Let me verify a couple final details.## Summary
The paper proposes HOMIL, an MIL framework for whole-slide image classification that augments ABMIL's attention-weighted mean (first-order moment) with a covariance-based "second-order moment" branch, while using DBSCAN clustering of patch features for adaptive granularity and efficiency. On CAMELYON16 and TCGA-NSCLC (CONCH features, 5-fold CV), HOMIL reports the best ACC/AUC/F1 against nine baselines, with an ablation showing each component contributes ~1 ACC point.

## Strengths
- **Top-line metrics across both datasets**: Tables 1–2 show HOMIL achieves the best ACC, AUC and F1 against nine baselines on both CAMELYON16 (96.98 / 99.23 / 96.54) and TCGA-NSCLC (93.24 / 97.41 / 92.93), and the per-fold runtime is the smallest of all attention-style baselines (310s vs ABMIL's 455s on CAMELYON16).
- **Self-consistent ablation isolating both components**: Table 3 cleanly shows that removing CM drops ACC 1.26 points and AUC 1.09, removing SOM drops ACC 1.00 / F1 1.60, and removing both reduces the model to ABMIL — confirming the two pieces are not redundant.
- **Clean statistical framing of ABMIL as first-order moment estimation**: §3.1 derives μ = Σ aᵢ hᵢ = 𝔼_{aᵢ}[hᵢ] explicitly, motivating the second-order extension via a familiar probabilistic interpretation rather than handwaving.

## Weaknesses

### Fatal
None — no single flaw definitively invalidates the headline result.

### Major
- **The "moment" framing in the motivation does not match the math the method actually computes.** §3.1 defines aᵢ as a probability distribution over instances, under which the second-order moment is the *attention-weighted* covariance Σ aᵢ(hᵢ − μ)(hᵢ − μ)ᵀ. However Eq. (3) in §3.2 drops the weighting, and §4.3.3 step 2 — explicitly titled "Weighted Covariance Matrix" on line 154 — also drops the weighting: it writes **C = Σ_{k=1}^K g̃_k g̃_kᵀ** with no a_k factor. The framing the paper sells (ABMIL = first moment, HOMIL = first + second moment of the same distribution) is therefore inconsistent with the implementation; the actual second branch is an unweighted scatter matrix of cluster means with the same label "weighted." The conceptual contribution is meaningfully weaker than advertised, and the paper should either correct the equation, justify the asymmetry, or rewrite the motivation.
- **The CAMELYON16 protocol deviates from the community standard in a way that affects comparability.** CAMELYON16 has an official 270/129 train/test split that the cited baselines (ABMIL, CLAM, TransMIL, etc.) report against. §5.1 / §5.2 instead do 5-fold CV over all 399 slides, collapsing the official test set into training for 4/5 folds. This is a real deviation that is not justified in the paper, makes the headline 99.23% AUC not directly comparable to numbers in the literature, and means all baselines are re-implementations under a non-standard protocol (e.g., HMIL at 94.44% AUC on CAMELYON16, well below ABMIL's 98.88%, suggests the baselines are not uniformly tuned). The paper should at minimum report the official-split results alongside CV.
- **Headline performance gaps are within fold-to-fold noise.** Tables 1–2 report mean_SE over 5 folds. For HOMIL on CAMELYON16 ACC, SE 2.43 corresponds to a fold-to-fold SD ≈ 5.4 points; the margin over the nearest baseline (MambaMIL 96.48 vs 96.98) is 0.5 points. On TCGA-NSCLC ACC, HOMIL 93.24 vs HMIL 92.89 is 0.35 points against SEs of 2.47 and 1.45 respectively. No paired statistical test across folds is reported. The abstract claim that the method "significantly improves the state-of-the-art" is not supported by the spread of the reported numbers, regardless of whether the underlying method is in fact better.
- **The runtime comparison is not apples-to-apples.** §5.3 attributes HOMIL's 310s vs ABMIL's 455s to "adaptive clustering," but DBSCAN+mean-pooling is an orthogonal preprocessing step. The right counterfactual ("ABMIL + same DBSCAN clusters") is not provided. The "w/o CM" row in Table 3 removes clustering from HOMIL but does not add it to any baseline. As reported, the speed claim rewards the proposed method for a preprocessing trick that no baseline was given.

### Minor
- **Covariance compression is heavily lossy and unvalidated.** §4.3.3 collapses the d×d matrix C to a d-vector via row-wise 1-D conv (m=64, T=4) followed by two max-pools (Eqs. 6–7), producing one scalar per row. There is no comparison to obvious alternatives (vectorized upper triangle, bilinear/compact bilinear pooling, log-Euclidean SPD features) and no reconstruction or sensitivity check. Combined with the SOM ablation gap of only ~1 ACC point, it is unclear how much of the gain is from "covariance structure" specifically vs. simply a second learned nonlinear branch.
- **DBSCAN+mean-pooling within clusters is in tension with the second-order motivation.** §3.2 argues the covariance is needed to capture *patch-level* variability, but §4.3.3 computes C over at most K cluster means after mean-pooling each cluster (§4.1 step 2.c), discarding within-cluster variability before the covariance is taken.
- **Fusion weights in Figure 2(b) do not sum to 1.** Eq. (8) is a softmax over two entries, so α⁽¹⁾ + α⁽²⁾ = 1 by construction. The curve description in §5.5 has α⁽¹⁾ stabilising near 0.6 and α⁽²⁾ near 0.45, which sum to ≈1.05. The figure and Eq. (8) need to be reconciled.
- **Unmotivated heuristics.** §4.2 sets ε to the 65th percentile of nearest-neighbour distances, d′ = 32, minPts = 4, m = 64, T = 4 — none of these choices are motivated or accompanied by sensitivity ablations in the main text (a brief Appendix sensitivity is referenced but not substantiated in the visible body).
- **Ablation missing the most informative cell.** "ABMIL + clustering" is not reported. This is the natural way to isolate how much of the gain comes from CM independently of SOM, and would also be the cleanest version of the apples-to-apples efficiency argument.

### Trivial
- The discussion in §5.5 that "the model increasingly relies on first-order information while retaining second-order statistics for complementary cues" is a post-hoc reading of the fusion weights; α⁽²⁾ ≈ 0.45 < α⁽¹⁾ ≈ 0.6 reflects gate output (and depends on branch norms), not branch informativeness.

## Nice-to-Haves
- Overlay DBSCAN cluster assignments on CAMELYON16 tumor annotations and report mean cluster size for tumor- vs. non-tumor-annotated patches, to back the §1/§4.2 claim that DBSCAN produces "small clusters for rare pathological regions, large clusters for abundant normal tissues."
- Add paired statistical tests across folds for the headline comparisons.
- Run at least one strong baseline (e.g., CLAM-MB or MambaMIL) on the same DBSCAN-clustered inputs to disentangle clustering speedup from the model contribution.
- Justify or rederive Eq. (4) as a properly attention-weighted second moment if that is the intended object.

## Removed Points
These points are flagged to be removed, treat them with caution.

- *Harsh critic's "w/o CM at 530s is slower than ABMIL at 455s, what is the model?"* — The paper's structure makes the model clear (HOMIL minus clustering = ABMIL backbone + SOM branch on raw patches), and the gap is plausibly the cost of the SOM branch on n≈3000 patches rather than K clusters. Demoted to a trivial-tier presentation note, not a substantive flaw.
- *Strength Finder's "Adaptive clustering achieves meaningful computational savings"* as listed — the underlying number is real but the comparison is not apples-to-apples (covered in the Major weakness on runtime), so it cannot stand as an unqualified strength.
- *Strength Finder's "Attention-based fusion is learnable and stable" with α⁽¹⁾ ≈ 0.6, α⁽²⁾ ≈ 0.45* — conflicts with the verified inconsistency that these do not sum to 1 under Eq. (8); kept as a minor weakness instead.

## Novel Insights
None beyond the paper's own contributions. The most interesting framing — MIL aggregation as moment estimation under the attention distribution — is one the paper introduces but does not actually implement consistently.

## Suggestions
- Replace Eq. (4) with a genuinely attention-weighted second moment $C = \sum_k a_k \tilde g_k \tilde g_k^\top$ (and analogously for the patch-level Σ in §3.2), or explicitly retitle the section and argue why the unweighted scatter is preferable.
- Report CAMELYON16 results on the official 270/129 split alongside the 5-fold CV results.
- Add paired statistical tests (e.g., paired t-test or Wilcoxon across folds) for the headline comparisons against the strongest two baselines on each dataset.
- Add a baseline-with-clustering row in Table 3 (e.g., ABMIL + DBSCAN, CLAM-MB + DBSCAN) so the runtime claim is interpretable.
- Provide a small validation that DBSCAN's clusters align with annotated tumor regions on CAMELYON16 (overlay figure plus mean cluster size by annotation).
- Compare the Conv1D + double max-pool covariance compression against vectorized upper triangle and bilinear pooling baselines, even on a single dataset.

---

### Calibration

**Anchors retrieved across rounds**

| Path | Avg score | Round | Comparison vs. paper |
|---|---|---|---|
| 0yVP49SDg0.md (Mamba-HMIL) | 3.25 | R1 | Same task family; rejected for unclear motivation/justification. HOMIL is cleaner in motivation/ablation but shares the "stack components, unclear theoretical grounding" flavor. |
| MOCEoNsjEx.md (Pg-GAT) | 3.00 | R1 | WSI MIL with graph approach; rejected for incremental contribution. |
| i4ouG6Kc8M.md (Dual-Metric histopath) | 2.50 | R1 | Tangentially related histopathology paper; not used. |
| jHdsZCOouv.md (SHAP-CAT) | 3.40 | R1 | Multimodal WSI; rejected. |
| 6xrDPHhwD3.md (MFC) | 6.00 | R1/R2 | Accepted WSI MIL paper with a clearer novel contribution (frequency-domain causal framing); HOMIL has weaker conceptual coherence. |
| T7ZVzuObcj.md (PointMIL) | 5.50 | R1 | MIL with clear interpretability story; rejected at the margin. |
| lo9HMoGNwQ.md (SMIL) | 4.50 | R1 | MIL framework with sound but incremental contribution; rejected. |
| AZW3qlCGTe.md (Set-Level Labels) | 5.67 | R1 | Accepted, theoretical grounding stronger than HOMIL. |
| xriGRsoAza.md (Interpretable TS MIL) | 8.00 | R1 | Far stronger, broad evaluation; not in HOMIL's range. |
| anek0q7QPL.md (Covariance + Hessian) | 5.00 | R2 | Uses covariance for classification with formal proofs; rejected despite theory — HOMIL's covariance story is weaker (no theory, inconsistent definition). |
| KiK4MNkuiQ.md (Geometric Modularity) | 5.00 | R2 | DBSCAN-based clustering paper; unrelated domain. |
| SPu6k4OZkj.md (Thetan Berserker) | 5.25 | R2 | Distance-based clustering; unrelated domain. |
| jqff3wzkLT.md (VCReg) | 4.33 | R2 | Variance/covariance regularization; rejected. |
| OPpqmSp0wK.md (MLCD) | 5.00 | R2 | Cluster discrimination representation learning; rejected. |

**Round-1 bracket**: between Mamba-HMIL (3.25) and MFC (6.00). HOMIL is clearer than Mamba-HMIL but has a substantive structural inconsistency MFC does not, so 3.5–5.0 is the plausible range.

**Round-2 narrowing**: anchors in the 4–6 range converge on a picture of incremental MIL/covariance-pooling papers that get rejected with mixed reviews. HOMIL has comparable empirical strength to SMIL (4.50) but a more serious conceptual mismatch (Eq. (4) labeled but not implemented as weighted), and weaker theoretical grounding than anek0q7QPL (5.00). I place HOMIL slightly below SMIL: real contribution, but the structural motivation problem plus non-standard evaluation pull it down.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>