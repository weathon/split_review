Now I have a solid set of anchors for calibration. Let me synthesize everything into the final review.

**Calibration Summary:**

| Anchor Paper | Score | Decision | Comparison to Current Paper |
|---|---|---|---|
| `7VPTUWkiDQ` — Brady et al. 2025 "Provable Compositional Generalization for Object-Centric Learning" | 7.33 | Accept | Current paper builds on this; weaker (more incremental, overclaims more, sloppier empirics) |
| `cCl10IU836` — "Interaction Asymmetry" (Brady et al. 2023) | 7.00 | Accept | Current paper extends this framework; weaker (less self-contained, overclaims) |
| `hKMPz3wkPV` — "Towards a formal theory of compositionality" | 6.75 | Reject | Had fundamental technical flaw (definition degeneracy); current paper's theory is sounder |
| `s1zO0YBEF8` — "Dynamics of Concept Learning and Compositional Generalization" | 6.50 | Accept | Both have theory+experiments with overclaiming; current paper's theory-empirics link is more direct |
| `dggRphAcCj` — "GeoCon" | 6.33 | Reject | Current paper has stronger theory, comparable empirics |
| `UVSKuh9eK5` — "CLIP Exhibits Improved Compositional Generalization" | 5.67 | Reject | Current paper is clearly stronger (novel theory + controlled experiments) |

**Bracket from Round 1:** 5.5–7.0.  
**Round 2 narrowing:** The relevant anchors cluster around 6.33–7.33. The current paper is clearly below the 7.0+ cluster (Brady papers) and clearly above the ~5.5 cluster (CLIP-CG, transfer papers). It lands closest to GeoCon (6.33) and Dynamics (6.50).

**Final score: 6.0.** The paper makes a genuine theoretical contribution (Theorem 3.2) with a clever empirical control (PUG-Object), but overclaims relative to what the theory establishes, lacks basic empirical rigor (no error bars), and has model selection concerns. It is weaker than the Brady et al. papers it builds upon but stronger than rejected CG papers in the anchor set.

---

## Summary

This paper argues that generative (decoder-based) approaches to visual perception have a structural advantage over non-generative (encoder-only) approaches for compositional generalization. The core theoretical contribution is an asymmetry result: constraining a decoder to the function class \(\mathcal{F}_{\text{int}}\) that guarantees OOD identifiability is straightforward via architecture or regularization, whereas constraining an encoder to the corresponding inverse class \(\mathcal{G}_{\text{int}}\) is infeasible because the necessary structure (Eq. 3.4) depends on the tangent-space geometry of the data manifold, which is unknown for OOD regions. Empirically, the paper evaluates on PUG datasets, finding that non-generative methods struggle at OOD compositional generalization without large-scale pretraining, while generative methods (VAE + replay/search) improve OOD performance substantially using the same underlying autoencoders.

## Strengths

- **Theorem 3.2 is a concrete, non-obvious theoretical result.** When \(d_x \geq d_z^3\) (the realistic image setting), the Jacobian and Hessian of inverse generators \(g \in \mathcal{G}_{\text{int}}\) can be essentially arbitrary matrices at a point, erasing the diagonal structure present in the \(d_x = d_z\) case (Lemma 3.1). The only surviving structure (Eq. 3.4) depends on the tangent space of the data manifold, which is unknown for OOD regions. This directly supports the paper's central claim about an asymmetry between encoder and decoder constraint feasibility, and is a genuinely novel insight beyond the Brady et al. framework the paper builds upon.

- **The PUG-Object split (Figure 5C) serves as an elegant natural control experiment.** When \(n=0\), concepts do not interact (animals never occlude), and the theory predicts \(\mathcal{G}_{\text{int}}\) is more structured. All non-generative models achieve near-perfect OOD accuracy on this split, whereas they struggle on PUG-Background and PUG-Texture where \(n > 0\). This pattern across three splits — predicted by the theory without model-specific tuning — provides strong evidence that the structure of the inverse function class drives generalization difficulty.

- **Within-model comparison isolates generative inversion as the active ingredient.** The replay and search results (Figure 6) use the same autoencoders as the non-generative baselines from Figure 5. Replay alone yields substantial gains (e.g., DINOv2 ViT-S/36 goes from ~40% to ~65% on PUG-Background), and search adds further improvement. This rules out confounds from architecture or training differences.

- **Clean formalization in Section 2.** Both generative and non-generative approaches are unified under a single identifiability framework (Eq. 2.2–2.6), making the subsequent theoretical comparison precise rather than metaphorical. The mapping of compositional generalization to OOD identifiability via Eq. 2.5–2.6 is well-executed and provides a solid foundation for the analysis.

## Weaknesses

### Fatal

None.

### Major

- **The paper's rhetoric overclaims relative to what the theory actually establishes.** The theory shows that *guaranteeing* compositional generalization via explicit encoder constraints (architecture/regularization) is infeasible because the needed structure (Eq. 3.4) depends on unobserved OOD manifold geometry. But infeasibility of *guarantees* does not imply that encoders *cannot succeed in practice* — optimization, implicit biases of SGD, pretraining, and data augmentation can all produce OOD generalization without formal guarantees. The paper's title ("Generation Is Required"), abstract ("generation is required for machines to achieve human-level visual perception"), and key framing statements (e.g., "guaranteeing compositional generalization requires a generative approach," Sec. 4 opening) slide from "cannot be guaranteed via explicit constraints" to "is required," and the theory does not license that slide. The paper's own results confirm that non-generative methods can perform well — SigLIP2 achieves ~80% OOD on PUG-Background (Fig. 5A, supervised) — which the framing does not adequately reconcile.

### Minor

- **No error bars or variance reporting.** All experimental results are presented as bare bar charts (Figures 5, 6). For a dataset of ~20K images with many model variants, variance across seeds and data splits is needed to assess whether the reported differences are statistically meaningful. Some bars differ by modest margins (e.g., ~5–10 percentage points in parts of Fig. 6B), making uncertainty information important for interpreting the results.

- **Model selection procedure may inflate reported performance.** The paper reports "the best-performing combination of slot encoder and fine-tuning choice" for each base encoder (line 213). This is a form of post-hoc selection that can inflate apparent performance relative to a fixed-protocol evaluation. It is unclear whether the same selection protocol was applied to the generative results in Figure 6, which complicates cross-figure comparison.

- **The search method uses asymmetric test-time computation.** Gradient-based search (Sec. 4.1) performs per-sample optimization at test time, while the non-generative baselines in Figure 5 are purely feedforward. The replay method (Sec. 4.2) does not have this issue — it uses the same feedforward encoder at test time — but the search gains are not contextualized relative to this additional computational budget.

### Trivial

- The theoretical analysis is presented for \(n=1, m=1\) in Lemma 3.1, with the paper noting that "similar statements can in principle be derived for higher order derivatives." The generality claim for \(n>1\) is not fully demonstrated in the main text.

## Nice-to-Haves

- Running a non-generative baseline with equivalent test-time computation (e.g., an ensemble or test-time adaptation) would strengthen the comparison and help isolate whether gains come from generation specifically or from extra computation.
- A direct comparison consolidating the best non-generative method, the VAE encoder (no search/replay), and the VAE encoder + search/replay into a single figure with error bars would make the comparison cleaner than cross-referencing Figures 5 and 6.
- Soften the title to better match the claims — e.g., "Guaranteeing Compositional Generalization Requires Generation" or "Why Generative Approaches Have a Structural Advantage for Compositional Generalization."

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic Point 3 (definition mismatch between theory and experiments):** The critic claims the VAE encoder is "already a generative approach on \(\mathcal{X}_{\text{ID}}\) by the paper's own definition." The paper explicitly addresses this in Section 5.1: "This case is nevertheless non-generative since the encoder is only constructed to invert the decoder on \(\mathcal{X}_{\text{ID}}\), and not on \(\mathcal{X}_{\text{OOD}}\)." The distinction between "non-generative" (Fig 5, VAE bars) and "generative" (Fig 6) is about whether OOD inversion is attempted — the operationalization is consistent with the paper's definitions. This criticism misunderstands the paper.

- **Harsh Critic section-by-section note about \(\mathcal{F}_{\text{int}}\) being sufficient but not necessary:** The paper explicitly states \(\mathcal{F}_{\text{int}}\) is "the largest function class shown to enable OOD identifiability" and does not claim it is the only path. This is a limitation of scope acknowledged by the paper, not a logical error.

- **Strength Finder claim about "causal effect":** While the within-model comparison is strong, the term "causal effect" overstates what a comparison between conditions with no randomization or intervention can demonstrate. The within-model comparison is correlational, not causal, but still informative.

## Novel Insights

The core insight — that the structure of inverse generator classes depends on data-manifold geometry while forward generator classes are coordinate-aligned and data-independent — is genuinely novel and provides a principled theoretical lens for understanding why generative approaches might be advantageous for compositional generalization. The PUG-Object control experiment operationalizing the \(n=0\) vs. \(n>0\) distinction is a clever empirical test of this theoretical asymmetry that goes beyond standard benchmark comparisons and is the kind of controlled experiment that makes theory-empirics feedback loops convincing.

## Suggestions

- Tighten the rhetorical framing to match what the theory actually supports: the claim should be that encoder constraints cannot *guarantee* compositional generalization (because OOD manifold geometry is unknown), not that generation is categorically *required*. The title in particular should be softened — the current title claims a universality the theory doesn't support.
- Add error bars across at least 3 seeds for all experimental results. This is a basic requirement at top venues.
- Clarify the model selection protocol for Figure 6 and ensure it matches the one used for Figure 5, or justify any differences.
- Discuss the SigLIP2 result (~80% OOD on PUG-Background as a non-generative method) more prominently — it is an important counterexample to the strong "required" framing and warrants explicit discussion of what it means for the theory's practical implications.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>