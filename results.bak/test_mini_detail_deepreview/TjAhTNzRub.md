Now I have all the information I need. Let me synthesize the final review.

**Round 1 bracket:** 3.5–7.5. The paper is clearly stronger than the weak band (SUN at 4.00, weak unlearning papers at 2.5–3.0) and clearly weaker than the strong band (8+ papers about interpretability/continual learning).

**Round 2 narrowing:** I read Deep Unlearning (5.25), SUN (4.00), Decoupling Class Label (5.75), Low Compute Unlearning (5.75), and Label-Agnostic Forgetting (6.00). MoRE is stronger than SUN and Deep Unlearning, comparable to Decoupling Class Label and Low Compute Unlearning, but below Label-Agnostic Forgetting. The internal contradictions (memory claims) push it down slightly.

**Final score: 5.5**

---

## Summary

This paper proposes MoRE (Mixture of Remapping Experts), a training-free framework for feature-level machine unlearning. The key idea is to: (1) project features into a prototype-orthogonal (PO) space via pseudoinverse to decorrelate forget and remain prototypes, (2) erase and remap forget prototypes into remain prototype distributions to prevent recovery, and (3) use multiple remapping experts to scatter forget features across the latent space. The method is evaluated on CIFAR-10/100, Tiny-ImageNet, and ImageNet for classification unlearning, and extended to diffusion model concept erasure.

## Strengths

- **Prototype-orthogonal (PO) projection is a well-motivated and empirically validated innovation.** The paper clearly demonstrates (Section 3.1, Figure 3, Figure 6) that forget and remain prototypes are highly correlated (cosine similarities ~0.5–0.77) and that naively erasing forget prototypes degrades remain prototypes from 1.0 to 0.52 autocorrelation. The PO projection via pseudoinverse is a clean mathematical fix that preserves remain-prototype autocorrelation near 1.0 after unlearning, directly addressing ESC's utility degradation. This is the paper's strongest technical contribution.

- **Remapping achieves demonstrably stronger irreversibility than prior feature-level methods.** Under the KR evaluation (linear probing after unlearning), MoRE keeps forget-set accuracy near random-guess levels (CIFAR-100: 0.07% HM_f; Tiny-ImageNet: 0.50% HM_f) while ESC-T exhibits much higher forget accuracy (CIFAR-100: 96.07% HM_f; Tiny-ImageNet: 95.47% HM_f). The t-SNE visualization (Figure 1) corroborates that remapping scatters forget features into remain distributions, breaking the separable-cohesive structure that ESC leaves behind.

- **Training-free efficiency is genuinely achieved.** MoRE completes unlearning in under 10 seconds using only activation means and linear algebra operations, with no gradient-based optimization required. The complexity analysis in Section 3.4 (O(Nd) time, O(dk) memory) is sound, and the empirical efficiency comparisons (Figure 5) show MoRE is orders of magnitude faster than training-based baselines like NG and RL.

- **Solid ablation study isolating each component.** Table 3 systematically decomposes the contributions of PO projection, erasing, remapping, and multi-expert extension. On CIFAR-10 (KR setting), HM improves from 15.94% (Remap without PO) to 69.78% (Remap with PO) to 89.61% (MoRE with multiple experts), making each component's contribution empirically verifiable.

## Weaknesses

### Major

- **Internal contradiction in memory and efficiency claims.** This is the most concerning issue. The text (Section 4, line 298) claims "MoRE performs complete unlearning in under 10 seconds while consuming less than 200 MB of GPU memory (see Fig. 5)." However, Figure 5 reports MoRE consuming **540 MB** of GPU memory, not <200 MB. Additionally, the abstract and introduction claim "constant memory" / "constant space complexity with respect to the number of concepts/classes and feature dimensions," but Section 3.4 explicitly states O(dk) memory complexity, which depends on both d (feature dimensions) and k (number of concepts). These are not minor presentation issues — they are factual inconsistencies that undermine trust in the reported results and claims. The authors must resolve which numbers are correct and correct the overclaims.

- **"Exact feature-level unlearning" and "irreversibility" claims are overstated relative to evidence.** The abstract claims "exact feature-level unlearning," but the method is fundamentally approximate — it applies a linear transformation (projection + remapping) to features, not an exact removal guarantee. The claim of "irreversibility" is supported by the KR metric evaluated at only a single learning rate (lr=0.1). A single linear probe with fixed LR is a weak test of irreversibility; a more thorough evaluation would include multiple probing strategies (varying LR, number of epochs, fine-tuning of the full model, stronger adversarial recovery attempts). Without such evidence, the scope of the irreversibility claim exceeds what is demonstrated.

- **The MoE (mixture-of-experts) framing does not match its measured contribution.** In the standard accuracy setting (Table 1, non-KR columns), Remap (single expert) and MoRE (multiple experts) are essentially identical across all datasets (e.g., CIFAR-100: both 99.98–99.99 HM). MoRE's advantage over Remap is only visible under the KR probing setting, and even there the gains are inconsistent (CIFAR-10: 10.79 vs 33.20 HM_f; CIFAR-100: 0.07 vs 51.88 HM_f). The paper's title and framing emphasize the "Mixture of Experts" component, but the evidence suggests that the core mechanism is the remapping strategy, not the mixture per se. A single-expert Remap is already highly effective, and the MoE extension adds complexity whose benefit is confined to one specific evaluation mode.

### Minor

- **Metric notation D_R is undefined in the main text.** The paper defines D_f, D_r, D_ft, D_rt in Section 3 (line 159), but Table 1 uses D_R without explanation. Readers must guess that D_R corresponds to D_ft (forget test accuracy). The KR metric itself is also only referenced to the appendix (Section B.3) without a definition in the main body. While deferring details to the appendix is acceptable, the main text should at least define the column abbreviations used in its primary results table.

- **Diffusion model extension is under-specified and under-evaluated.** The paper states MoRE is applied "out of the box" to cross-attention layers with tokenized prompts, but provides no details on how the projection dimension, prototype construction from text embeddings, or transformation insertion work in the diffusion architecture. Quantitatively (Table 2), MoRE does not achieve the best LPIPS_f (forget score) — ESD and SAFEE achieve higher values — and the claimed qualitative superiority rests on a single cherry-picked example. This extension does not constitute rigorous evidence of generalizability.

- **Router mechanism for the MoE component is underspecified.** The stochastic router is described as "input-independent and routes each input randomly" (Section 3.3), but the probability distribution over experts is not stated. Is it uniform? Per-sample? Per-batch? This matters because the entire claim of "scattering" forget features depends on how routing works. The conditional router initialization is mentioned but not described in sufficient detail for replication.

- **Number of experts used in main results is not stated.** The sensitivity analysis (Figure 7) tests varying expert counts, but the paper never states the default number of experts used for the MoRE results in Table 1. This is a basic experimental detail that should be reported.

### Trivial

- The Morgan (?) notation: Table 7 and some ablations use "MoUE" which appears to be a typo for "MoRE."

## Nice-to-Haves

- The paper would benefit from a limitations section acknowledging that the method requires access to the original model's feature extractor and the remain set, and that the irreversibility guarantee is only empirical, not theoretical.
- A clearer presentation of Table 1 (separating the standard and KR settings into distinct tables or using clearer column grouping) would improve readability.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Tables are nearly unreadable"** — The table is dense but interpretable; column headers are clear and the arrow notation (↑/↓) indicates direction. The parser mangling of column alignment is a known artifact, not an author error. The critic's claim of "13 numerical values without definition" reflects parser-induced confusion; the actual table structure is standard for the field.
- **"ESC-T is faster"** — The paper claims efficiency relative to *training-based* methods (NG, RL), not absolute superiority over ESC-T. The comparison with ESC-T is for reference, not as a claim of being uniformly faster.
- **"Single cherry-picked example" in diffusion** — While the diffusion experiment is light, single qualitative examples are standard in generative unlearning papers (c.f. ESD, UCE). This is a valid limitation of scope but not evidence of cherry-picking.
- **"Missing appendix, missing proofs"** — Parser strips appendix content; these exist in the original submission.
- **"Statistical significance concerns with 3 trials"** — Three trials with standard deviation reporting is standard practice in unlearning literature.
- **"Missing related works"** — Cannot verify this without external sources.
- **Formatting/style nitpicks** — Parser artifacts, not author errors.
- **Generic speculation** ("could the metric be measuring a proxy?", "are confounders controlled?") lacks concrete anchors in the paper.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that meaningfully reframes or deepens understanding of the paper's content beyond what the authors already state.

## Suggestions

1. **Fix the internal contradictions.** Resolve the discrepancy between the text claim of "<200 MB" and Figure 5's value of 540 MB. Replace "constant memory" / "constant space complexity" claims with accurate descriptions (e.g., "O(dk) memory, linear in feature dimension and concept count"). Correct or remove "exact feature-level unlearning" — the method is approximate.
2. **Strengthen the irreversibility evaluation.** Test the KR metric with multiple learning rates (e.g., 0.01, 0.05, 0.1, 0.5) and probing strategies (full fine-tuning of the classification head, or several epochs of SGD). Report results across these settings to demonstrate that forget knowledge truly cannot be recovered.
3. **Reframe the contribution around remapping, not MoRE.** The single-expert Remap is simpler and nearly as effective for standard metrics. Acknowledge that the MoE component provides marginal benefit limited to the KR setting, or present it as an optional extension rather than the central framing.
4. **Define all metrics in the main text.** At minimum, define D_R (= D_ft) and HM_f in the body alongside the primary results table.
5. **State the number of experts used** for the main MoRE results, clarifying whether it was tuned per dataset or held constant.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>