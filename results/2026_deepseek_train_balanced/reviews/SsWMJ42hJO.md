## Summary

This paper studies neural collapse in contrastive learning and proposes CLOP, a loss term that pulls labeled embeddings toward fixed orthonormal prototypes to prevent both complete collapse (all embeddings identical) and dimensional collapse (embeddings confined to a low-rank subspace). The paper contributes (1) a theoretical bound of \(2+O(1/k)\) on the learning rate to prevent complete collapse, derived on a simplified cosine-similarity loss, (2) a geometric analysis showing why cosine-similarity optimization drives dimensional collapse, and (3) the CLOP method with experiments on CIFAR-100 and Tiny-ImageNet.

## Strengths

- **Tight numerical validation of the learning-rate bound (Theorem 1, Figure 2/fig:collapse).** The theoretical bound of \(2+O(1/k)\) is not presented as a loose inequality — it is empirically verified: gradient descent on \(\mathcal{L}_{\text{class}}\) succeeds at LR=2.0 (bound=2.03) and collapses at LR=2.1, and the bound tracks the empirically measured maximum safe learning rate across varying numbers of class embeddings. The alignment between theory and controlled experiment is unusually tight and lends credibility to the analysis *of the simplified loss*.

- **Lemma 2 (theory-subspace) provides a clean geometric diagnosis of dimensional collapse.** The lemma shows that when a \(k\)th class embedding is added to \(k-1\) linearly independent ones, the optimal move to minimize total cosine similarity is to make the new embedding linearly dependent. Figure 4 (fig:svd100) confirms that gradient descent on \(\mathcal{L}_{\text{class}}\) consistently converges to rank \(k-1\) without maintaining equal distances. This gives a clear, first-principles explanation for why dimensional collapse is endemic to cosine-similarity-based contrastive methods.

- **Practical improvement in small-batch training (Figure 3/fig:exp-batchsize).** The paper reports that CLOP achieves accuracy with batch size 32 comparable to baseline SupCon with batch size 2048 on CIFAR-100 — a 64× reduction in memory footprint. If this claim stands, it is a practically significant result with direct relevance for edge-device deployment.

- **Hyperparameter robustness across a wide range.** The λ ablation (Table 1/ablation-lambda) shows Top-1 accuracy on CIFAR-100 varies only between 0.740 and 0.760 as λ ranges from 0.1 to 1.5, demonstrating that CLOP is not brittle to its tuning parameter.

## Weaknesses

### Fatal

None.

### Major

1. **The theoretical analysis is conducted on a surrogate loss (\(\mathcal{L}_{\text{class}}\)), not on InfoNCE, and the gap is not bridged.**  
   At line 134, the paper states that "the InfoNCE loss can be simplified to" \(\mathcal{L}_{\text{class}}(\mathbf{X}) = -\sum_{i\neq j} [\mathbf{X}^\top \mathbf{X}]_{ij}\). This is not a simplification — it discards the log-sum-exp structure, the temperature \(\tau\), and the normalization term, replacing them with a sum of pairwise cosine similarities that has fundamentally different gradient dynamics. Theorem 1's bound of \(2+O(1/k)\) is derived and numerically validated on this surrogate loss in a toy setting (random vectors, no neural network, no data, no augmentations). The paper then claims the bound "can be applied to both self-supervised and supervised contrastive learning" (line 27) without any argument that it carries over to actual InfoNCE or SupCon training. This disconnect does not invalidate the CLOP method's empirical results, but it means the paper's headline theoretical result is not connected to the real losses used in practice.

2. **Missing comparisons to relevant neural-collapse-prevention methods.**  
   The paper claims CLOP prevents neural collapse, yet the main experiments compare only against plain InfoNCE and plain SupCon (line 214). Multiple methods specifically designed to address neural collapse in contrastive learning are cited in the related work but completely absent from the experiments: DirectCLR (Jing et al. 2021, line 68), the ETF-prototype method (Gill et al. 2024, line 70), whitening-based approaches (Tao et al. 2024; Hassanpour et al. 2024, line 70), and class-conditional InfoNCE (Fu et al. 2022, line 69). Without comparisons to these existing approaches, the claim that CLOP provides a superior or even complementary solution to neural collapse is unsupported.

3. **No statistical significance reported for any experimental result.**  
   The main experimental results (Figures 3, 4; Table 1) are reported as single numbers or single-line plots without standard deviations, confidence intervals, or trial counts. The paper mentions "5 consecutive trials" only for the toy numerical experiment (Figure 2). For a paper making comparative claims about accuracy and stability, the absence of any error quantification undermines the ability to assess whether observed improvements are meaningful.

### Minor

1. **Synthetic experiment (Table 1) conflates CLOP's mechanism with the effect of using labels during pretraining.**  
   In the synthetic experiment, CLOP uses the 10% labeled samples *during pretraining* via the prototype loss, while the baselines (InfoNCE, DCL, BarlowTwins, VICReg) are trained purely self-supervised — the same 10% labels are used only for the post-hoc KNN classifier. The 70.01% vs. 100% gap therefore conflates two variables: the orthonormal prototype mechanism, and whether any labeled information is available during representation learning. The synthetic experiment should have given the baselines an equivalent supervised auxiliary loss (e.g., cross-entropy or supervised contrastive loss on the same 10%) to isolate the effect of orthonormality specifically.

2. **Internal inconsistency about the nature of co-linear optima.**  
   Figure 1's caption (line 18) describes co-linear class arrangements as "global optima" of the InfoNCE loss, while Lemma 1 (line 88) and the surrounding text (line 86) describe them as "local minima." Line 86 further adds "This includes non-unique global optima," creating confusion about whether co-linear configurations are global or local optima. This is a relatively minor inconsistency but detracts from the paper's clarity, especially since the distinction matters for the paper's core argument about why collapse is problematic.

3. **Numerical validation of Theorem 1 (Figure 2) is a toy experiment.**  
   The tight bound is validated using randomly initialized vectors with no neural network, no data, and no augmentations. As the paper itself notes (line 139), "adjusting the learning rate alone cannot prevent dimensional collapse" in this setting. While this toy validation is not a flaw per se, the paper's framing (line 141: "the theoretical upper bound closely aligns with the highest successful learning rate recorded") does not emphasize that this alignment is only demonstrated for gradient descent on the surrogate loss in a highly idealized setting, not for real neural network training.

4. **No ImageNet experiment.**  
   ImageNet is the standard benchmark for contrastive learning methods. Its absence limits the empirical weight of the paper's claims, especially given that the datasets used (CIFAR-100, Tiny-ImageNet) are relatively low-resolution and low in diversity.

### Trivial

None.

## Nice-to-Haves

- **Directly measure embedding rank on real datasets.** The paper qualitatively shows CLOP prevents collapse in the synthetic 3D visualization and reports downstream accuracy on CIFAR-100/Tiny-ImageNet, but never directly measures whether CLOP's embeddings actually occupy a higher-rank space on real data (e.g., effective rank or singular value spectrum analysis). This would directly connect CLOP's mechanism to its claimed effect.
- **Ablation to isolate orthonormality vs. any supervised pull.** Replacing the orthonormal prototypes with randomly initialized non-orthogonal prototypes (or trainable class-mean vectors) would clarify whether orthonormality is the crucial property or whether any class-specific supervisory signal during pretraining suffices.
- **Pseudo-labeling experiments.** The paper correctly identifies this as future work (line 268), but even a preliminary experiment would strengthen the case for CLOP in settings with very limited labels.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The paper does not explain how the number of prototypes is chosen for datasets where the number of classes is unknown."* — The paper clearly states \(k\) equals the number of classes in the dataset (line 180). The unknown-class scenario is acknowledged as future work (line 268).
- *"CLOP cannot adapt to class structure that differs from the initial random basis"* and *"no analysis of whether the prototypes remain targetable"* — These are speculations about potential limitations, not verified weaknesses from the paper as written.
- *"Lemma 1 is a restatement of a well-understood property"* — The paper cites relevant prior work (Jing et al. 2021, Fu et al. 2022, etc.) in the related work section; whether this property was previously understood is a matter of judgment and not a concrete flaw.
- *"No training curves shown"* — Not standard for a paper of this length; curves are not required for the claims made.
- *"Missing hyperparameter and implementation details"* — The paper provides optimizer, architecture, batch size, learning rate schedule reference, and key hyperparameters. A complete training log is impractical to include.
- *"Weakness" about the λ ablation table showing small differences that "could fall within variance"* — Without error bars, this is speculation either way; the small range (0.740–0.760 across a 15× λ range) is itself evidence of robustness, even if precise statistical significance cannot be assessed.
- *Strength about synthetic experiment providing "direct visual evidence"* — The strength finder overstated this. The visualization is useful, but the comparison is unfair (as noted in Minor weakness 1), so citing it as a clean strength is misleading.

## Novel Insights

None beyond the paper's own contributions. The reviewers' analyses surface real gaps (theory–practice disconnect in the learning-rate bound, missing baselines, unfair synthetic comparison) but do not contribute novel insights about the problem beyond what the paper itself provides.

## Suggestions

1. **Rebuild the experimental evaluation.** Add comparisons to DirectCLR, Gill et al. (ETF prototypes), whitening approaches (Tao et al., Hassanpour et al.), and Fu et al. (class-conditional InfoNCE). Report all results with standard deviations over at least 3–5 trials.

2. **Fix the theory–practice gap.** Either (a) provide a rigorous argument that the learning-rate bound for \(\mathcal{L}_{\text{class}}\) carries over to InfoNCE (e.g., via a Lipschitz property or gradient dominance), or (b) reframe the theoretical contribution as applying specifically to the simplified loss and use it as motivation rather than proof.

3. **Correct the synthetic experiment.** Give the baseline methods access to the same 10% labels during pretraining (e.g., via a supervised contrastive or cross-entropy auxiliary loss) so the comparison isolates the orthonormal prototype mechanism.

4. **Resolve the internal inconsistency** between Figure 1's caption ("global optima" for co-linear arrangements) and Lemma 1 ("local minima" for the same). Also, line 86's "non-unique global optima" phrasing needs clarification.

5. **Run an ImageNet experiment** at a 100-epoch schedule to demonstrate scalability, or explicitly justify why the current datasets suffice for the paper's claims.

6. **Add an effective-rank analysis** of the learned embeddings on CIFAR-100/Tiny-ImageNet to directly connect CLOP's orthonormal-prototype mechanism to the claimed collapse-prevention effect.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>