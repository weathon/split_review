Now I have all the evidence I need. Let me write the final consolidated review.

## Summary

The paper proposes CONTROL, a framework that adds three contrastive losses (supervised for seen classes, nearest-neighbor for all classes, and unsupervised for consistency) on top of existing BCE-based open-world semi-supervised learning methods (ORCA, NACH). The paper claims a theoretical proof that contrastive loss is robust to misaligned nearest-neighbor pairs while BCE loss is not, and that uniformity in contrastive features prevents unseen-class collapse. Empirically, the method yields meaningful improvements (e.g., +6.4% unseen-class accuracy on CIFAR-100 over NACH).

## Strengths

- **Meaningful empirical improvements on standard benchmarks.** On CIFAR-100, CONTROL + NACH achieves a 6.4% absolute gain on unseen-class accuracy and a 2.1% gain on all-class accuracy over NACH alone (Table 1). Consistent gains are shown on ImageNet-100 (Table 2). These are practically relevant improvements on an important problem.

- **Ablation study validates the contribution of each loss component.** Table 3 shows that adding ℒ_SupSeen + ℒ_SimAll yields +2.7% unseen-class accuracy, and further adding ℒ_SupNN provides an additional boost. This supports the design rationale.

- **Diagnostic analysis links feature-level alignment to reduced seen–unseen confusion.** Table 4 shows that CONTROL increases the ratio of unseen-class predictions (+2.77%) and the ratio of unseen–unseen nearest-neighbor pairs (+2.35%), providing evidence that the contrastive framework reduces misclassification between seen and unseen classes.

## Weaknesses

### Fatal

None. The empirical contributions stand on their own, and the framework design is reasonable even if the theoretical justification is flawed. The paper can be rescued by correcting or re-scoping the theory.

### Major

- **The theoretical derivation in Section 4.1 claiming contrastive loss is robust to misaligned nearest-neighbor pairs is mathematically unjustified.** The paper claims that under the noisy joint distribution P^η_XV, the contrastive loss risk simplifies to (1-η)E[L_φ] + η·log(|𝒩(x)|), where log(|𝒩(x)|) is a constant, so the optimal classifier is unchanged. The last equality is justified only by saying "φ(x), φ(v^+), and φ(v^-) are independent." This does not suffice:
  - E_{x,v^+}[-φ(x)^⊤·φ(v^+)/τ] = -(1/τ)·E[φ(x)]^⊤·E[φ(v^+)], which depends on the model parameters and is not generally constant, let alone equal to log(|𝒩(x)|).
  - E_{x,v^-}[log Σ exp(φ(x)^⊤·φ(v^-)/τ)] is also not generally constant or equal to log(|𝒩(x)|); it depends on the feature geometry.
  
  Independence alone does not make these expectations vanish or collapse to log(|𝒩(x)|). Without additional assumptions (e.g., that feature vectors are zero-mean on the hypersphere and that the log-sum-exp simplifies), the derivation is unsupported. Since the paper explicitly lists "theoretically demonstrating" as a core contribution (Contributions list, point 2), this flaw undermines one of its claimed contributions.

- **The uniformity argument in Section 4.2 connecting feature uniformity to logit-level unseen-class collapse is hand-wavy.** The paper invokes the Wang & Isola (2020) asymptotic decomposition and claims that "g(·) maintains the spatial structure between feature representations and logits." No argument or evidence is provided for why g(·) preserves spatial structure, nor is it explained how this prevents unseen-class logit collapse specifically. The argument is at best an analogy, not a demonstration. Separately, the decomposition equation (line 167) uses an undefined constant "log K" and its alignment term (-E[exp(z^⊤·z^+/τ)]) differs from the standard form in the cited work, which uses -E[z^⊤·z^+]/τ.

- **Key hyperparameters and experimental details are missing.** The paper does not report values for λ₁, λ₂, λ₃, temperature τ, batch size, optimizer, learning rate, or training epochs. These are essential for reproducibility. The paper states results are "the average of three runs" but never reports any measure of variance (standard deviations, confidence intervals), making it impossible to assess the statistical significance of the reported gains (especially the modest ones in Table 4).

### Minor

- **Limited demonstration of "broad compatibility."** The paper claims CONTROL is "compatible with a broad range of existing open-world SSL algorithms" but tests it with only two baseline methods (ORCA and NACH), both from the same BCE-based family. The paper itself categorizes methods into "BCE-based" and "other methods" (OpenLDN, TRSSL), but compatibility with the latter is not tested.

- **No discussion of computational overhead.** Adding three contrastive losses on top of the base method incurs additional computational cost. The paper does not report training time, memory usage, or batch size requirements—a practical concern for practitioners.

- **No qualitative analysis.** The claimed mechanism (feature uniformity preventing logit collapse) could be made more concrete with t-SNE/UMAP visualizations of features or logits with and without CONTROL, but none are provided.

### Trivial

- The "log K" term in the uniformity decomposition equation (line 167) is not defined anywhere in the paper.
- The paper states at line 127 that g(φ(x))^⊤g(φ(v)) = 0 for independent x and v, which leads to M→−∞. This is a strong simplifying assumption (logits being exactly orthogonal) that is not realistic for softmax outputs. The general intuition (unrelated samples produce small dot products) is reasonable, but the "= 0" claim is an overstatement.

## Nice-to-Haves

- Hyperparameter sensitivity analysis for λ₁, λ₂, λ₃, and τ would strengthen the practical utility of the paper.
- Testing CONTROL with at least one non-BCE-based open-world SSL method (e.g., OpenLDN, TRSSL) would better support the "broad compatibility" claim.
- Qualitative visualizations of learned feature distributions (with/without CONTROL) would make the mechanism more concrete.

## Removed Points

These points were flagged but are removed for the following reasons:

- **"Table not readable in the submitted manuscript" (OpenCON comparison):** Removed. The table images are extraction artifacts from the PDF parsing process, not errors in the original submission. The numeric comparisons are stated in the text (lines 222–223).
- **"Results limited to ImageNet-100, doesn't demonstrate scalability":** Removed. ImageNet-100 is a standard benchmark in the open-world SSL literature, matching the evaluation protocol of the baselines (ORCA, NACH). Demanding larger-scale evaluation beyond what the community uses is scope creep.
- **Criticism of missing appendix/proofs:** Removed per instructions — the parser strips appendix content; it exists in the original submission.
- **Reproducibility concern framed as "cannot be independently verified":** Removed per hard rule — all cited models/tools/datasets are assumed to exist as of the current date.
- **Generic statements about "the paper should also cover Y domain":** Removed — these amount to demands for a different paper rather than critiques of the present one.

## Novel Insights

The empirical finding that feature-level contrastive alignment (via ℒ_SupNN) directly reduces the ratio of seen–unseen nearest-neighbor pairs is interesting and novel within the open-world SSL literature. Prior work (ORCA, NACH) operated primarily at the logit level; this paper provides evidence that feature-level intervention changes the nearest-neighbor graph structure itself, creating a beneficial feedback loop where better features lead to better pair selection, which in turn improves BCE loss. This mechanism insight is valuable, even if the formal theoretical framing is flawed. The ablation study further shows that the unsupervised contrastive loss (ℒ_SimAll) contributes primarily to unseen-class accuracy (+2.7%), suggesting it functions as more than just a consistency regularizer — it may actively shape the feature space in ways that reduce collapse. These observations could guide future method design in this area.

## Suggestions

1. **Fix or rescope the theoretical contribution.** Either provide a rigorous proof for the contrastive robustness claim (with properly stated assumptions) or reframe Section 4.1 and 4.2 as intuitive motivation / heuristic justification rather than "theoretical demonstration." The empirical results are strong enough to carry the paper without overclaimed theory.
2. **Report all hyperparameter values and standard deviations.** Provide λ₁, λ₂, λ₃, τ, batch size, optimizer, learning rate, and epoch count. Add standard deviations or confidence intervals to all main results.
3. **Add at least one non-BCE baseline (e.g., OpenLDN, TRSSL)** to substantiate the "broad compatibility" claim.
4. **Add qualitative visualizations** (t-SNE/UMAP of features) comparing NACH vs. NACH+CONTROL to directly illustrate the alignment and uniformity effects.
5. **Clarify the "log K" term** in the decomposition equation and correct any discrepancies with the cited Wang & Isola (2020) formulation.

## Score and Decision

The paper addresses an important problem and reports real, practically meaningful improvements over strong baselines. The framework design is sensible and the ablation studies provide solid empirical validation. **However, the paper overclaims a theoretical contribution that is mathematically unsupported.** The derivation in Section 4.1 contains an unjustified simplification, and the uniformity argument in Section 4.2 is superficial. Since the paper frames these theoretical claims as a core contribution, this is a significant weakness that cannot be ignored. Combined with missing reproducibility details (hyperparameters, variance estimates) and limited baseline coverage, the paper in its current form does not meet the bar for acceptance at a top venue. The underlying empirical contributions are real, and the paper could become a solid contribution with major revisions (fixing the theory or re-scoping it, adding experimental details, and broadening baseline testing).

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>