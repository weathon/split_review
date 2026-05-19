Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper analyzes the MLP-Mixer architecture from the perspective of sparse MLPs. It shows that when vectorized, the Mixer's mixing layers are equivalent to an extremely wide MLP with Kronecker-product weights (effective width \(m = SC\)). Through this lens, the paper: (1) derives an implicit L1 regularization bias of linear mixing layers, (2) reveals a hidden connection to Monarch matrices, (3) provides spectral analysis showing Mixers avoid the singular-value explosion that plagues unstructured sparse-weight MLPs at large widths, and (4) derives and empirically validates that maximizing width under a fixed connection budget occurs when \(C = S\). The paper introduces the RP-Mixer (random-permuted mixing) as a controlled baseline and shows it exhibits similar trends, supporting the claim that sparsity matters beyond the specific block structure.

## Strengths

1. **Explicit mathematical formulation connecting Mixer to wide sparse MLP (Proposition 1).** The vectorization identity \( \operatorname{vec}(WXV) = (V^\top \otimes W)\operatorname{vec}(X) \) plus the commutation-matrix derivation yields a clean characterization: the S-Mixer is equivalent to a shallow MLP of width \(m=SC\) with Kronecker-product weight matrices whose sparsity ratios are \(1/S\) and \(1/C\). This identity was missing from prior work and provides the foundation for the entire paper's analysis.

2. **Derivation of the optimal width condition \(C=S\) with extensive empirical validation across four datasets.** Equation (8) gives \(C^* = S^* = (\Omega/\gamma)^{1/3}\) as the configuration maximizing width (hence sparsity) under fixed connections. Figure 5 then shows test error is minimized around \(C \approx S\) on CIFAR-10, CIFAR-100, STL-10, and ImageNet-1k, for both normal and RP Mixers. This directly links the theoretical sparsity principle to quantifiable performance gains.

3. **Spectral analysis identifying a structural advantage of Mixers over unstructured sparse MLPs.** Section 4.3 shows that the maximal singular value of an unstructured sparse-weight MLP grows with width (via Marchenko–Pastur, scaling as \(O(m)\)), while the Mixer's Kronecker-product weight maintains a stable maximal value \(1+\sqrt{\gamma}\). This explains why Mixers can exploit much larger effective widths without the trainability collapse observed in SW-MLPs (Figure 3), and is a genuine architectural insight.

4. **Introduction of the RP-Mixer as a controlled ablation that preserves sparsity and spectrum while destroying block structure.** Section 5.2 defines the PK family and shows that random-permuted variants exhibit the same test-error-vs-width trends (Figure 6) and can match or beat normal Mixers at sufficient depth (Figure 7). This strengthens the case that the sparsity level—not the specific permutation pattern—is the operative factor.

5. **Connection to Monarch matrices and implicit L1 regularization.** Proposition 2 shows that Frobenius-norm regularization on Kronecker factors implies an L1 penalty on the full effective weight, linking two facets of sparsity (zero entries vs. limited independent parameters). The Corollary revealing that the linear S-Mixer is an MLP with a weight-shared Monarch matrix bridges two previously disconnected sparse-parameterization frameworks.

## Weaknesses

### Fatal

None.

### Major

1. **The claim that "sparsity is the key mechanism" is partially supported but not fully established.** The paper asserts (abstract, introduction, conclusion) that sparsity is *the* key mechanism underlying Mixer performance. The evidence shows compelling correlation but falls short of establishing causation isolated from other architectural factors. The RP-Mixer experiments are the strongest causal evidence, yet they still retain structured (Kronecker) sparsity — every row of the effective weight matrix has exactly \(n_1\) non-zero entries, just scattered by permutation. This is not unstructured random sparsity, so the gap between Mixer sparsity and the SW-MLP sparsity the paper analogizes to remains. The paper's central insight — that Mixer behavior can be *characterized* through the lens of sparsity — is well-supported, but the claim that sparsity *explains* Mixer performance is stronger than the evidence warrants. The authors should tone down the causal language (e.g., "verifying that sparsity is the key mechanics underlying the MLP-Mixer" in the conclusion) to "sparsity is a key characterization" or "a central explanatory factor."

### Minor

2. **The CKA evidence for feature similarity is modest in strength.** The maximum average CKA reported (~0.6 on a 0–1 scale) indicates moderate similarity, not strong alignment. The paper compares this favorably against a lower CKA with dense MLPs, which provides a relative sanity check, but the absolute value weakens the claim that "the sparse Mixer was similar to sparser MLP in hidden features." Additionally, no error bars or variance estimates are provided for the CKA values, making it unclear how stable this similarity is across random seeds.

3. **The implicit regularization result (Proposition 2) has limited connection to actual Mixer training.** The inequality is mathematically correct — it lower-bounds a Frobenius-norm penalty on Kronecker factors by an L1 norm on the full matrix. However: (i) it is a bound on *regularized* objectives, not a statement about optimization dynamics; (ii) the Mixer trains factors via backprop through the Kronecker product, not the effective weight matrix directly; (iii) the result is for linear layers only, with no evidence it operates in the non-linear Mixer used in practice. The paper would benefit from stating more candidly that this is a bound relating two regularization forms, not evidence of implicit sparse regularization during actual Mixer training.

4. **The ImageNet improvement (Mixer-B-W vs. Mixer-B/16) is small relative to variance.** The reported gain is approximately 0.3% top-1 accuracy (23.26 vs. 23.56) with a standard deviation of ±0.19 from 3 seeds. Given the small absolute improvement and limited number of seeds, it is unclear whether this difference is statistically significant. A significance test or more seeds would strengthen this result.

5. **The \(\beta\)-LASSO comparison (Table 1, upper) compares a static-sparsity Mixer variant with a dynamic-sparsity method** that starts dense and prunes during training. These are different training regimes; the comparison is informative but the setting is not directly comparable. The Mixer-B/16 vs. Mixer-B-W comparison (lower table) is cleaner and more relevant to the paper's central thesis.

### Trivial

6. **The paper lacks a dedicated limitations section.** Several limitations are scattered through the text but are not synthesized: the per-layer \(\Omega\) analysis assumes the same connectivity budget for every layer, but in practice \(S\) is determined by patch size; the theoretical bound (Proposition 2) is for linear activations and does not extend to the non-linear case; the CKA and spectral analyses are on small models. Consolidating these into one place would improve clarity.

7. **Minor inconsistency in claim strength:** the abstract says "a key mechanism" while the introduction and conclusion say "the key mechanism" — the stronger claim is not better supported.

## Nice-to-Haves

- A direct comparison between a Mixer variant whose structured sparsity is replaced by truly unstructured sparsity at the same effective width (e.g., using a library that supports sparse linear layers without materializing the full \(m \times m\) matrix) would substantially strengthen the causal claim about sparsity.
- Testing whether the linear S-Mixer trained with weight decay yields a smaller L1 norm of the effective weight than a dense linear MLP with the same weight decay would directly connect Proposition 2 to training behavior.
- Adding error bars to the CKA figure and reporting the sample size used for mini-batch CKA computation would improve reproducibility and strength of evidence.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Similar tendency contradicts visual evidence at large widths"** (Harsh Critic §4.2) — REMOVED. The paper explicitly acknowledges the divergence at large widths ("However, we observed for too-wide cases…the test error of SW-MLP is higher") and provides spectral analysis explaining why. The claim of "similar tendency" refers to the range where both models are trainable, which is accurate.

2. **"RP-Mixer 'much closer to random sparse weights' is misleading"** (Harsh Critic §5.2) — REMOVED. The paper uses "seemingly much closer" (qualified language) and explains that non-zero entries are scattered throughout the matrix. It does not claim RP-Mixer has unstructured random sparsity.

3. **"CKA methodology is too vague (mini-batch size, number of samples)"** (Harsh Critic §3.4) — REMOVED. The paper states "Detailed settings of all experiments are summarized in \cref{sec:experimental_setting}" which is an appendix section stripped by the parser. These details exist in the original submission.

4. **"Improvement could come from architecture change rather than width alone"** (Harsh Critic, Table 1) — REMOVED. Changing \(S\) and \(C\) under fixed \(\Omega\) IS the width manipulation the paper studies; the "architecture change" and the "width change" are the same intervention.

5. **"Missing related works"** — REMOVED per policy (cannot verify existence of works not cited).

6. **"Reproducibility nitpicks about undisclosed hyperparameters"** — REMOVED per policy; experimental details are in the appendix.

## Novel Insights

**From the reviews, the most notable observation not present in the paper itself** is that the RP-Mixer experiments, while clever, still operate within a structured-sparsity regime (Kronecker product + permutations). A truly decisive test of the "sparsity is key" hypothesis would require a model that maintains the Mixer's exact sparsity ratio but with completely unstructured nonzero locations, implemented memory-efficiently. The paper's current strongest evidence for sparsity over structure is the RP-Mixer's comparable performance at sufficient depth — which is suggestive but not definitive, since RP-Mixer weight matrices still have exactly \(n_1\) non-zeros per row (deterministic row-degree), unlike the Poisson row-degree of a Bernoulli random sparse matrix. This gap between "Kronecker with random permutation" and "fully unstructured sparse" remains an open question that the reviews collectively surfaced but the paper did not address.

## Suggestions

1. **Tone down the causal claim** from "the key mechanism" to "a key characterization" or "a central explanatory factor." The paper's contributions stand on their own as a characterization framework without overclaiming causation.

2. **Add error bars to the CKA results** and specify the sample size and layer-pairing methodology used.

3. **Add a brief discussion** of the statistical significance of the ImageNet result, or run additional seeds to increase confidence.

4. **Consolidate limitations into one place** (e.g., a short paragraph before the conclusion) covering: per-layer \(\Omega\) assumption, linear-only theoretical result, small-model evidence for CKA/spectral analysis, and the gap between RP-Mixer sparsity and fully unstructured sparsity.

5. **Clarify in the implicit regularization section** that Proposition 2 is a bound relating two regularized objectives, not a statement about training dynamics or implicit bias in the standard sense.

## Score and Decision

**Originality:** 7/10 — The vectorization identity is simple but was missing from prior work; the connection to Monarch matrices and the spectral analysis are novel.

**Importance of research question:** 8/10 — Understanding why the MLP-Mixer works is a timely and relevant question.

**Claims supported:** 6/10 — The central claim is somewhat overstated relative to the evidence; the supporting experiments are well-designed but the causal link is not fully isolated.

**Soundness of experiments:** 7/10 — Good breadth across datasets, reasonable controls (S-Mixer, RP-Mixer), but some statistical rigor missing (CKA error bars, ImageNet significance).

**Clarity of writing:** 7/10 — The mathematical derivations are clear; some claims could be better qualified.

**Value to the community:** 7/10 — The optimal-width principle (\(C=S\)) is simple and actionable; the analytical framework will be useful for future MLP-based architecture design.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>