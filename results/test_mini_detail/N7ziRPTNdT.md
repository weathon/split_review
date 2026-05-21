Now I have all the information I need to write the consolidated review. Let me synthesize everything.

**Round 1 Bracket**: I initially placed this paper between 5 and 7.5 based on three calibration anchors: weak (<3.5), middle (3.5–7.5), and strong (>7.5).

**Round 2 Narrowing**: I examined anchors in the 4–8 range. The most relevant anchors are:
- **Provable Compositional Generalization for Object-Centric Learning** (7.33, oral) — closely related, cleaner claims, synthetic data. The current paper has stronger experiments (photorealistic PUG data) but weaker claim framing.
- **Learning to Compose** (6.50, poster) — similar experimental scope, but the current paper has stronger theory.
- **Compositional Risk Minimization** (6.00, reject) — similar theory+experiments balance, rejected for experimental limitations.
- **Feature Accompaniment** (5.67, reject) — similar claim/evidence mismatch issue.
- **No Free Lunch: Fundamental Limits...** (6.00, poster) — similar "impossibility" framing, purely theoretical. The current paper has experiments, which is stronger.

The paper sits below the Provable Compositional Generalization anchor (7.33) primarily because of the claim-evidence mismatch. It's comparable to Learning to Compose (6.50) but the claim overreach pulls it down. I place it at **5.5** — below the acceptance threshold, but with genuine contributions.

---

## Summary

This paper investigates whether generative (decoder-based) or non-generative (encoder-based) methods are better suited for data-efficient compositional generalization. The authors formalize perception as inverting a ground-truth generator belonging to a structured function class ℱ_int, and show theoretically (Theorem 3.2) that constraining an encoder to the corresponding inverse class 𝒢_int is infeasible when the image dimension exceeds the squared latent dimension, because the required constraints depend on the unknown geometry of out-of-domain regions of the data manifold. In contrast, constraining a decoder to ℱ_int is straightforward via architecture or regularization. The paper proposes search (gradient-based optimization) and generative replay (training on synthetic OOD images) as practical methods for inverting a decoder OOD, and evaluates on PUG datasets. Non-generative methods fail on compositional splits unless scaled to large pretraining, while generative methods using search/replay substantially improve OOD accuracy.

## Strengths

- **Theorem 3.2 provides a formal obstruction for non-generative methods.** The proof that when $d_x \geq d_z^3$, the derivatives of inverse generators in $\mathcal{G}_{\text{int}}$ can be arbitrary (up to measure zero) is a genuine theoretical contribution. It shows that enforcing the constraints needed to guarantee compositional generalization on an encoder requires knowledge of unobserved OOD manifold geometry — a principled difficulty that goes beyond empirical observations.

- **Clear experimental demonstration of the practical gap.** The controlled evaluation on PUG datasets (Figure 5) shows that non-generative methods achieve near-perfect in-domain accuracy but fail OOD unless backed by massive pretraining (e.g., SigLIP2). Figure 6 then shows that generative methods (replay + search) consistently improve OOD accuracy across all base encoders without additional real data. The contrast is clean and well-presented.

- **Validation of the $n=0$ special case.** The PUG-Object split (where concepts do not interact) confirms the theoretical prediction from Section 3.1: when $\mathcal{G}_{\text{int}}$ is more structured, non-generative methods achieve near-perfect OOD accuracy (Figure 5C). This strengthens the overall argument by showing that the difficulty is diagnostic of concept interaction, not a blanket failure.

- **Principled connection to causal/anti-causal learning.** Section 6 explicitly links the theoretical results to the long-standing heuristic that generalization is easier in the causal (generator) direction than the anti-causal (inverse) direction, providing formal justification for conjectures in prior work (Kilbertus et al., 2018).

## Weaknesses

### Major

- **Central claim is overstated relative to the evidence.** The title "Generation is Required for Data-Efficient Perception" and the abstract assert necessity, but the paper only shows that (a) under a specific formalization of perception as inversion of a known generator in $\mathcal{F}_{\text{int}}$, non-generative methods face a theoretical obstacle, and (b) generative methods help on one dataset (PUG). The paper does not rule out that non-generative methods could achieve compositional generalization through alternative mechanisms (e.g., learning invariant features, structured readouts, or task-specific inductive biases) under different definitions of perception. The claim conflates "generation provides a principled path" with "generation is required." The limitations section (Sec. 7) acknowledges the $\mathcal{F}_{\text{int}}$ assumption, but the title and abstract do not reflect this qualification. The paper's own results — that SigLIP2, a non-generative method, reaches ~80% OOD accuracy on PUG-Background — suggest that data scale (rather than generation per se) may be a viable alternative, which the paper dismisses as "at the cost of data efficiency" without considering whether the cost is acceptable in practice.

### Minor

- **Missing baseline: isolating generation from data augmentation.** The replay method (Eq. 4.4) trains an encoder on synthetic OOD images generated by the decoder. This is effectively data augmentation with a generator. The paper does not include a baseline that trains a non-generative encoder on the same synthetic images but without the decoder's $\mathcal{F}_{\text{int}}$ constraint (or with an unstructured decoder). This would isolate whether the benefit comes from the generative *inversion* (search) or simply from having more structured training data. The PUG-Texture results partially mitigate this concern — replay cannot be applied there, yet search alone improves OOD accuracy — but the missing baseline on PUG-Background weakens the clean causal claim.

- **Limited experimental scope.** The evaluation is on a single dataset (PUG) with a small number of concepts (10 backgrounds, 32 animals), simple slot-based compositions, and no occlusions or complex interactions. While the paper acknowledges this limitation, it is a significant gap between the broad claim ("data-efficient perception") and the evidence. Human perception operates in far richer, multimodal, interactive environments.

- **Definition-dependent framing.** The paper defines perception as inverting a known ground-truth generator (Eq. 2.1). This is a legitimate modeling choice, but the central claim depends on accepting this definition. The paper notes that task-based views can be framed as a special case (line 47), but does not explore whether task-based generalization may require weaker inductive biases than inversion-based generalization. A reader unconvinced by the inversion framing could reasonably argue that the paper's theory does not apply to standard vision benchmarks.

### Trivial

- None that survive filtering.

## Nice-to-Haves

- Report standard deviations or confidence intervals for the OOD accuracy results. While the differences are substantial, error bars would strengthen reproducibility.
- Include a brief analysis of decoder reconstruction quality (e.g., examples of synthetic OOD images used for replay) to allow readers to assess the validity of the replay data.
- Report computational cost of search (gradient steps per image) and replay generation, as these matter for practical adoption.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that non-generative methods with large-scale pretraining achieve good OOD performance, undermining the "required" claim.** The paper's framing is explicitly about *data-efficient* perception. Large-scale pretraining achieving good OOD performance is acknowledged as a costly alternative, not a counterexample to the paper's thesis. The paper's title includes "data-efficient," so this is internally consistent. **Removed** because it misreads the paper's scope.

- **Criticism that the paper does not discuss computational cost of search/replay.** This is a nice-to-have, not a structural weakness. **Moved to Nice-to-Haves.**

- **Criticism about statistical significance and variance.** The differences in Figure 6 are large enough that error bars are unlikely to change conclusions. **Moved to Nice-to-Haves.**

- **Criticism that the paper should demonstrate that practical attempts to constrain encoders to $\mathcal{G}_{\text{int}}$ fail.** The paper's theoretical claim (Theorem 3.2) is that such constraints are *infeasible* because they depend on unknown OOD manifold geometry, not merely that the authors didn't try. This is a formal result, not an empirical gap. **Removed** as it misunderstands the nature of the theoretical claim.

- **Generic "related work missing" points.** The instructions forbid mentioning missing related works without external sources. **Removed.**

- **Formatting/style nitpicks and typos.** These are parser artifacts, not author errors. **Removed.**

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Calibrate the title and central claim.** Replace "Generation is Required for Data-Efficient Perception" with something like "Generation Provides Principled Guarantees for Data-Efficient Compositional Generalization" or "The Case for Generative Approaches to Compositional Generalization." The abstract should explicitly state that the claim holds under the inversion-based definition of perception for generators in $\mathcal{F}_{\text{int}}$.

2. **Add a baseline that trains a non-generative encoder on synthetic OOD images from an unstructured decoder.** This would isolate whether the replay benefit comes from the decoder's $\mathcal{F}_{\text{int}}$ constraint or simply from having more training data.

3. **Expand the experimental scope** to at least one additional dataset with more complex compositions (e.g., CLEVR with controlled OOD splits, or a real-world dataset with annotated compositional structure). This would directly address the concern that the results are dataset-specific.

## Score and Decision

**Calibration anchors used (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 7VPTUWkiDQ (Provable Comp. Gen. for OCL) | 7.33 | R1, R2 | Oral. Closely related theory; cleaner claims, synthetic data. Current paper has stronger experiments but weaker claim framing. |
| rmg0qMKYRQ (Intriguing Properties of Generative Classifiers) | 8.00 | R1 | Spotlight. Broader empirical study of generative classifiers. Less theoretical, more comprehensive. |
| zyBJodMrn5 (On the generalization capacity...) | 5.67 | R1, R2 | Poster. Studies multimodal generalization. Methodological, less direct comparison. |
| hKMPz3wkPV (Towards a formal theory of compositionality) | 6.75 | R1, R2 | Reject. Definitional paper. Cleaner framing but less empirical grounding. |
| HT2dAhh4uV (Learning to Compose) | 6.50 | R1, R2 | Poster. Similar experimental scope on synthetic data. Current paper has stronger theory. |
| oKglS1cFdb (Feature Accompaniment) | 5.67 | R2 | Reject. Similar claim/evidence mismatch issue. Current paper's theory is stronger. |
| YtAhOVCy2t (Compositional Risk Minimization) | 6.00 | R2 | Reject. Studies compositional shifts. Solid theory+experiments but rejected for limitations. |
| OwNoTs2r8e (No Free Lunch: Fundamental Limits...) | 6.00 | R2 | Poster. Similar "impossibility" framing, purely theoretical. Current paper has experiments. |
| RIaIpdUCPb (Brain-inspired Geometry...) | 3.00 | R1 | Withdrawn. Weak, unrelated. |
| OcaKeyGb0K (A unified theory of scene representation...) | 3.00 | R1 | Reject. Unrelated. |

**Round 1 bracket:** 5.0–7.5  
**Round 2 narrowing:** Compared to Provable Comp. Gen. (7.33, oral): the current paper has weaker claim framing but stronger experiments. Compared to Learning to Compose (6.50, poster): stronger theory. Compared to Feature Accompaniment (5.67, reject): stronger theory, similar claim-evidence gap. The claim-evidence mismatch is the primary factor that keeps this paper below the 6.5+ range.

**Final score:** 5.5 — The paper has genuine theoretical and empirical contributions, but the central claim is overstated relative to the evidence. The definition-dependent framing, missing baseline isolating generation from data augmentation, and limited experimental scope prevent the paper from supporting its title. The paper would benefit from toning down its claims and adding the suggested baselines.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>