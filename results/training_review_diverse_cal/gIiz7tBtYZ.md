Here is my final consolidated review.

---

## Summary

This paper introduces a neural-network-based algorithm for solving continuous optimal transport (OT) with general cost functionals, going beyond standard Euclidean costs. The core theoretical contribution is a maximin (saddle-point) reformulation (Theorem 1) that allows implicit recovery of stochastic transport maps for any convex lower-semicontinuous cost functional, subsuming prior reformulations for classic and weak OT. The paper also provides an error analysis via duality gaps (Theorem 3) and constructs two concrete cost functionals: a class-guided functional \(\mathcal{F}_{\text{G}}\) for dataset transfer with class preservation, and a pair-guided functional \(\mathcal{F}_{\text{S}}\) for supervised image-to-image translation.

## Strengths

1. **Generic maximin reformulation that unifies prior work.** Theorem 1 provides a saddle-point formulation for general OT that automatically subsumes existing maximin formulations for classic OT (Rout et al., Fan et al.) and weak OT (Korotin et al.). This is a principled theoretical contribution that extends the continuous OT toolkit beyond standard Euclidean costs. (Lines 111–118, 133)

2. **Strong empirical results for class-guided dataset transfer.** On the FMNIST→MNIST task, the method achieves 83.22% accuracy using just 10 labeled target samples per class, massively outperforming label-using baselines (OTDD: 10.28%, SinkhornLpL1: 10.67%) and reducing FID to 5.26. This demonstrates that incorporating side information via general cost functionals solves a problem that standard Euclidean-cost OT and existing label-using methods cannot. (Table 1, Table 2, Lines 280–282)

3. **Error analysis that relaxes restrictive assumptions on the dual potential.** Theorem 3 provides an upper bound on plan approximation quality via duality gaps without requiring the learned dual potential \(\hat{v}\) to be convex — a requirement in prior work (Fan et al., Rout et al.). This is technically novel and relevant to weak OT, for which no prior error analysis existed. (Lines 139–153)

4. **Both theoretical and practical contributions in a single framework.** The paper connects the general OT theory (Paty et al.) to a practical neural algorithm with out-of-sample generalization, filling a gap between discrete general-OT solvers and continuous neural OT methods that previously only supported Euclidean/weak costs. (Lines 30, 88–95)

5. **Flexibility across stochastic and deterministic maps.** The framework supports both one-to-many (stochastic) and one-to-one (deterministic) transport maps, demonstrated in both the class-guided and pair-guided experiments. (Line 228)

## Weaknesses

### Fatal
None.

### Major
1. **Incomplete quantitative evaluation for the pair-guided functional.** The paper reports supervised image-to-image translation on three datasets (Comic-Faces-V1, Edges-to-Shoes, CelebAMask-HQ) but provides FID scores only for CelebAMask-HQ (21.1) and only for the proposed method — no FID numbers are given for any baseline (Pix2Pix, NOT, RMSE regression) on any dataset. For Comic-Faces-V1 and Edges-to-Shoes, only qualitative figures are shown. The claim of "competitive quality" (line 297) is not substantiated by quantitative evidence. Without baseline FIDs, the reader cannot assess whether the method is competitive with Pix2Pix (a well-established supervised baseline) on these standard benchmarks.

### Minor
2. **Error analysis (Theorem 3) is disconnected from the paper's own examples.** Theorem 3 requires \(\mathcal{F}\) to be \(\beta\)-strongly convex in a metric on \(\Pi(\mathbb{P})\). The pair-guided functional \(\mathcal{F}_S\) is linear in \(\pi\) (hence not strongly convex), and the class-guided functional \(\mathcal{F}_G\) (built from energy distances) is not argued to be strongly convex either. The paper acknowledges the strong convexity requirement (line 151) but does not discuss whether the examples satisfy it or why the analysis remains relevant. This does not invalidate Theorem 3 as a theoretical contribution, but it creates a gap between the presented theory and the practical demonstrations.

3. **The class-guided functional \(\mathcal{F}_G\) requires separate class-conditional sampling from both source and target.** The paper acknowledges this (line 212), but this requirement means the method needs more structured data access than standard OT — the learner must know and separately sample from each class of both \(\mathbb{P}\) and \(\mathbb{Q}\). This limits applicability in settings where target labels are unavailable or class boundaries are unknown.

### Trivial
None.

## Nice-to-Haves

- Reporting FID scores for Pix2Pix and other baselines on all three pair-guided datasets would substantially strengthen the empirical claims.
- A brief remark in the Discussion noting that the paper's pair-guided example does not satisfy the strong convexity required by Theorem 3, and that Theorem 3 applies to future functionals satisfying that condition, would help readers understand the scope.
- Showing a toy example where strong convexity holds and the duality gap bound can be validated empirically would connect the error analysis to practice.

## Removed Points

These points were identified by the reviewers but are removed or downgraded per the rules; they are included here for completeness:

1. **"Separably \(*\)-increasing" undefined in the main text** — Removed. The instructions state that the parser strips appendix sections from all papers; definitions and proofs that appear in the appendix exist in the original submission. While it is ideal for the central assumption of Theorem 1 to be stated in the main text, the paper likely contains the definition in the supplementary material. This is a presentational concern, not a structural flaw.

2. **Unfair comparison against unsupervised baselines** — Removed. The paper is transparent about which methods use labels (line 281: "Other baselines lack the capability to use label information") and compares against two label-using baselines (OTDD, SinkhornLpL1) which it dramatically outperforms. The comparison against unsupervised methods provides context — standard OT costs (W₂, W₂,γ) cannot solve the class-preserving task at all — and is not misleading. The accuracy improvement over label-using methods (83.22% vs. ~10%) is a genuine result.

3. **Formatting/style nitpicks** — Removed per rule about parser artifacts and style nitpicks.

## Novel Insights

The reviews reveal that the paper's core strength — the maximin reformulation for general OT — is its most solid contribution, while its main empirical weakness is the lack of quantitative comparison in the pair-guided experiment. The class-guided experiment is genuinely strong and well-evaluated (accuracy + FID + qualitative + multiple baselines including two label-using methods). The asymmetry between the rigorous evaluation of the class-guided functional and the nearly evaluation-free presentation of the pair-guided functional is striking and suggests the pair-guided experiment was included as a secondary demonstration rather than a primary validation. The error analysis, while technically sound, is effectively a standalone theoretical result that the paper does not operationalize — this is not uncommon in ML papers but the gap is wider here because neither example satisfies the required condition.

## Suggestions

1. **Complete the pair-guided quantitative evaluation.** Report FID (and ideally LPIPS or similar perceptual metrics) for Pix2Pix, NOT, and RMSE regression on all three pair-guided datasets. Without these numbers, the pair-guided results are not evaluable and the paper's claim of "competitive quality" is unsupported.

2. **Acknowledge the scope of Theorem 3 explicitly.** Add a sentence noting that neither \(\mathcal{F}_G\) nor \(\mathcal{F}_S\) satisfies strong convexity, so Theorem 3 does not directly apply to the paper's examples but is provided for future functionals constructed with regularization that does induce strong convexity.

3. **Improve the Introduction's framing.** Rephrase the class-guided results to emphasize the comparison against label-using baselines (OTDD, SinkhornLpL1) rather than unsupervised methods, which solve a fundamentally different problem (lines 37–38).

4. **Include a pointer to where "separably \(*\)-increasing" is defined** (e.g., "see Appendix A for the definition") in the main text, so the reader knows where to find it.

## Score and Decision

**Originality:** The maximin reformulation for general OT and the class-guided functional are both novel contributions that extend prior work in a non-trivial way.

**Importance:** The problem of continuous OT with general cost functionals is well-motivated and addresses a genuine gap. The dataset transfer application is practically relevant.

**Claims:** The central claim (that general OT can be solved via saddle-point optimization with neural networks) is well-supported. The claim of competitive quality on pair-guided translation is not supported.

**Soundness:** The theoretical results appear sound. The class-guided experiments are well-designed and thorough. The pair-guided experiments lack quantitative rigor.

**Clarity:** The paper is generally well-written but could benefit from clearer framing of the label-using vs. unsupervised comparison and explicit acknowledgment of the strong convexity gap.

**Value:** The paper's core contribution (the maximin framework) is valuable and likely to be built upon. The class-guided functional and its strong results on dataset transfer are practically useful.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>