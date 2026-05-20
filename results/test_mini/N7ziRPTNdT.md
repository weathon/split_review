Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper argues that guaranteed compositional generalization requires a generative approach. Theoretically, it proves (Theorem 3.2) that when the observation space is high-dimensional ($d_x \ge d_z^3$), constraining an encoder to the function class $\mathcal{G}_{\text{int}}$ (inverses of compositional generators) is infeasible because the necessary constraints depend on the unknown OOD data manifold — whereas constraining a decoder to $\mathcal{F}_{\text{int}}$ is straightforward via architecture/regularization. Empirically, on photorealistic PUG datasets with controlled ID/OOD splits, non-generative methods fail at compositional generalization unless backed by large-scale pretraining, while generative methods (gradient-based search + generative replay) yield consistent OOD gains across all base encoders.

## Strengths

- **Theorem 3.2 provides a genuinely novel theoretical result.** It proves that when $d_x \ge d_z^3$, the first- and second-order derivatives of inverse generators in $\mathcal{G}_{\text{int}}$ can take arbitrary matrix values (up to measure zero), making encoder constraints data-dependent and ill‑posed — in contrast to decoder-side constraints which are global and architecture-friendly. This is a non-trivial and original theoretical contribution that cleanly formalizes an intuitive asymmetry.

- **Clean empirical validation on controlled photorealistic data.** The PUG datasets provide explicit ID/OOD splits for background, texture, and object combinations, enabling unambiguous measurement of compositional generalization. The three splits systematically vary concept interaction degree ($n=1$ for Background/Texture, $n=0$ for Object), directly matching the theoretical framing.

- **Generative search and replay consistently outperform non-generative baselines across all encoder conditions.** On PUG-Background (Fig. 6A), generative replay raises OOD accuracy from near 0% (from-scratch ViT-S/36) to ~60%, with search adding further gains. Even on the strongest baseline (SigLIP2), generative methods improve performance. On PUG-Texture (Fig. 6B), search provides clear gains across all models.

- **Identification and experimental validation of the $n=0$ special case (Fig. 5C, Sec. 3.1).** The paper shows that when concepts do not interact ($n=0$), $\mathcal{G}_{\text{int}}$ is more structured, and all non-generative methods achieve near-perfect OOD accuracy — a clean empirical consistency check for the theory.

- **Well-structured formalization linking compositional generalization to identifiability (Eqs. 2.5–2.6).** Building on Brady et al. (2025), the paper provides a precise, rigorous framework connecting OOD identifiability to function classes $\mathcal{F}_{\text{int}}$ and $\mathcal{G}_{\text{int}}$, which forms a solid foundation for the theoretical analysis.

## Weaknesses

### Fatal
None.

### Major
- **The title and central claim are overstated relative to the evidence.** The paper is titled "Generation Is Required for Data-Efficient Perception," implying a necessity result. Yet the empirical results show that non-generative methods with sufficient pretraining (SigLIP2) reach ~80% OOD accuracy on PUG-Background and ~85% on PUG-Texture (Fig. 5A–B). The theory itself (Sec. 3.1 takeaways) acknowledges that non-generative methods *can* succeed through optimization luck — so the empirical evidence is consistent with "generative methods help, especially when the encoder is weak" rather than "generation is required." The data-efficiency dimension of the claim is never directly tested: there is no experiment varying the size of the ID training set to measure whether generative methods close the gap with fewer examples (the paper compares "from scratch" vs. pretrained as a proxy, which is not the same). This mismatch between the headline claim and what is actually demonstrated is the paper's most significant weakness and would need to be addressed (either by tempering the language or adding a direct data-efficiency experiment).

### Minor
- **No error bars or statistical grounding for experimental results.** Figures 5 and 6 report single-bar heights with no error bars, confidence intervals, or indication of variance across multiple runs. For some comparisons (e.g., SigLIP2 with vs. without search on PUG-Texture), the reported differences are modest, and without variance estimates it is impossible to assess whether they are reliable. This is a standard expectation for experimental ML papers.
- **Data efficiency is asserted but not directly measured.** The paper's framing (abstract, introduction) connects compositional generalization to data efficiency, and the conclusion states that non-generative large-scale pretrained models improve OOD performance "at the cost of data efficiency." However, no experiment directly measures data efficiency by varying the amount of ID training data. The "from scratch" vs. pretrained comparison is a coarse proxy; a controlled data-efficiency study (e.g., OOD accuracy as a function of ID dataset size) would be needed to substantiate this dimension of the claim.
- **The decoder only approximately constrains to $\mathcal{F}_{\text{int}}$, with no verification of how well.** The paper acknowledges (Sec. 5.1) that the regularized cross-attention decoder is an *approximation* of $\mathcal{F}_{\text{int}}$, and in Appendix C reports results with unstructured decoders. However, it does not measure how well the decoder satisfies the theoretical conditions (e.g., Hessian block-diagonality). While this does not invalidate the empirical results, it loosens the link between the theoretical guarantees and the experimental mechanism.

### Trivial
None.

## Nice-to-Haves

- **Slot-alignment verification.** The evaluation trains slot-wise readouts and reports ~99% ID accuracy, but explicitly verifying that slots are consistently assigned (e.g., slot 1 always corresponds to animal 1) would strengthen confidence that OOD drops reflect compositional failure rather than slot-swapping.
- **Ablation of decoder inductive bias.** Replacing the regularized cross-attention decoder with an unstructured decoder while still using search/replay (beyond the Appendix C results) would help isolate how much of the generative advantage comes from the decoder architecture vs. the search/replay procedures.
- **Comparison to test-time adaptation baselines.** Non-generative methods could also be adapted at test time (e.g., fine-tuning the encoder on the OOD image with a self-supervised loss). Exploring such alternatives would make the comparison to generative approaches more comprehensive.

## Removed Points

- **"The theoretical results and empirical setup are only loosely connected"** — The paper explicitly states that non-generative methods can succeed through optimization luck (Sec. 3.1 takeaways), so the strong SigLIP2 results are *consistent* with the theory, not contradictory. The experiments are framed as a practical demonstration of the asymmetry, not a direct test of the causal mechanism. Removing because the criticism misunderstands how the paper positions the theory-experiment relationship.
- **"Generative methods rely on large-scale pretrained decoders"** — The paper includes a "from scratch (ViT-S/36)" condition (Sec. 5.1) where both encoder and decoder are trained from random initialization. Generative methods improve OOD accuracy even in this condition (Fig. 6). The claim that this is "not a truly from-scratch generative system" is factually incorrect given the paper's explicit description. Removing.
- **"The paper doesn't demonstrate that generation is necessary, only that it helps"** — This is correctly captured in the Major weakness about the overclaimed title, but the critic's framing conflates two separate issues: the overclaimed title (which is a real weakness) and the claim that the theory-experiment connection is loose (which is not a weakness, as explained above). The valid part is merged into the Major weakness above.
- Various pure speculation about confounds, formatting nitpicks, and demands for experiments outside the paper's stated scope — removed per filtering rules.

## Novel Insights

The harsh critic's analysis surfaces an important nuance that the paper itself does not fully engage with: the tension between the *theoretical infeasibility* result (Theorem 3.2) and the empirical finding that large-scale pretrained non-generative models (SigLIP2) achieve reasonable OOD accuracy. The paper treats this as "optimization luck" consistent with its theory, but never squarely addresses the magnitude of this phenomenon — i.e., whether there is a systematic reason why large-scale pretraining helps non-generative methods generalize compositionally (beyond mere luck), and whether this constitutes a meaningful practical alternative to the generative approach. The critic's observation that the strong SigLIP2 results would appear to "undermine the 'required' rhetoric" is not just a presentation nitpick; it points to an underexplored middle ground where the paper's absolute framing ("generation is required") forces a dichotomy that the evidence does not cleanly support. However, the paper's core theoretical contribution (the infeasibility of *guaranteeing* encoder-side constraints) remains valid regardless of whether some methods bypass the issue through optimization, and this nuance is worth preserving in how the contribution is described.

## Suggestions

1. **Temper the central claim.** Reframe the paper's contribution as "generative approaches are necessary to *guarantee* compositional generalization" or "generative methods are more reliable for compositional generalization than non-generative methods" rather than "generation is required." This would accurately reflect what the theory and experiments actually show.
2. **Add error bars to all experimental figures.** Report standard deviations over at least 3–5 random seeds for the main OOD accuracy results.
3. **Either add a direct data-efficiency experiment** (varying ID dataset size and measuring OOD accuracy) or remove "data-efficient" from the title and central framing.
4. **Measure decoder fidelity to $\mathcal{F}_{\text{int}}$.** Report how well the regularized cross-attention decoder satisfies the theoretical conditions (e.g., Hessian block-diagonality) on a held-out set of in-distribution latents.

## Score and Decision

### Calibration

**Round 1 bracket:** The paper sits between the weak anchors (< 3.5) and the strong anchors (> 7.5), most likely in the 3.5–7.5 range.

**Round 2 anchor comparisons:**

| Anchor Paper | Avg Score | Round | Comparison to Current Paper |
|---|---|---|---|
| Necessary Conditions for Comp. Gen. in Visual Models (yi06ZiVl2H) | 4.80 | R2 | Weaker. Current paper has more novel theoretical results (Thm. 3.2) and cleaner experimental setup (controlled PUG splits vs. post-hoc analysis of CLIP/SigLIP). |
| Why Transformers Succeed and Fail at Comp. Gen. (ADeeoMY4Dn) | 4.50 | R1/R2 | Weaker. More limited in scope (toy synthetic tasks) and the theoretical principles (composition equivalence) are less fundamental. |
| What Drives Comp. Gen. in Visual Generative Models? (oSUjUvs999) | 4.00 | R1/R2 | Weaker. Mostly empirical with less theoretical depth; conclusions found somewhat intuitive by reviewers. |
| Statistical and Structural Identifiability (Wa3cfE3Iay) | 6.00 | R2 | Comparable but stronger. Both have strong theoretical contributions about identifiability; the current paper's Thm. 3.2 is novel and non-trivial, but the identifiability paper has broader scope and cleaner presentation. |
| Characterizing Pattern Matching (VCjlm003WL) | 7.00 | R2 | Stronger. More thorough theoretical + empirical treatment with scaling laws, multiple architectures, and interpretability analyses. |

**Final score determination:** The paper is clearly stronger than the 4.0–4.8 anchors (which were rejected) due to its genuinely novel theoretical result and clean experimental design. It is somewhat weaker than the 6.0 anchor (accepted poster) due to the overclaimed central claim, missing error bars, and the data-efficiency claim not being directly tested. The comparison places the paper between 4.80 and 6.00, closer to 5.5 — acknowledging the real theoretical contribution while reflecting the significant framing mismatch.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>