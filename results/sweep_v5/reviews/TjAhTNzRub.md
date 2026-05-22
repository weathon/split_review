Now I have all the information I need. Let me compose the final consolidated review.

---

## Summary

MoRE introduces a training-free framework for class-wise machine unlearning that replaces naive subspace erasure (ESC) with a novel remapping strategy. The method has three components: (i) prototype-orthogonal (PO) projection that decorrelates forget and remain prototypes before any modification, solving the utility-degradation problem of ESC; (ii) a remapping operation that redirects forget prototypes into remain prototypes rather than simply erasing them; and (iii) a mixture-of-experts (MoRE) extension that scatters forget features across multiple remain prototypes using a stochastic router, breaking residual cohesive structure. Empirical results across CIFAR-10/100, Tiny-ImageNet, and diffusion model style erasure show strong unlearning performance with high efficiency.

## Strengths

1. **Prototype-orthogonal (PO) projection is a clean, principled solution to the utility-degradation problem.** Section 3.1 identifies that naive erasure of forget prototypes degrades remain prototypes due to correlation (Figure 3 shows remain prototype autocorrelation dropping to 0.52). The PO projection explicitly decorrelates prototypes before editing, and Table 3's ablation confirms this: without PO, Remap's remain accuracy (D_r) drops to 89.52%; with PO it stays at 99.94%. This is a direct improvement over ESC and is well-supported by the ablation study.

2. **Remapping + multi-expert routing demonstrably breaks feature-level separability.** Under the KR (linear probe) evaluation in Table 1, MoRE achieves forget accuracy near random (e.g., HM_f = 0.07 on CIFAR-100 with MoRE, versus 99.60 for ESC), far below even the retrain model (52.96). The t-SNE in Figure 1 provides complementary qualitative evidence. The multi-expert design is motivated by a concrete failure mode of single-prototype remapping (residual cohesion exploitable by tuned probes, Section 3.3) and the ablation confirms the benefit.

3. **Genuinely efficient: training-free and fast.** Figure 5 shows MoRE completes unlearning on CIFAR-10 in ~9.5 seconds with ~540 MB GPU memory, versus 88–100 seconds for training-based alternatives. The efficiency enables scaling to larger models.

4. **Out-of-the-box effectiveness on diffusion model concept unlearning.** Table 2 shows MoRE achieves competitive LPIPS tradeoff scores (LPIPS_d = 0.25 for Van Gogh, 0.26 for Kelly McKernan) without any architecture-specific adaptation, hyperparameter tuning, or additional training. This demonstrates generality beyond image classification.

5. **Thorough ablation isolating each component.** Table 3 systematically compares Erase vs. Remap with/without PO, then extends to MoRE. Table 6 compares stochastic vs. conditional routing. The ablations convincingly show that each innovation (PO, remapping, multiple experts) is necessary for the best performance.

## Weaknesses

### Fatal

None.

### Major

1. **"Irreversibility" claim is not supported by sufficient evidence.** The paper claims "irreversible feature-level unlearning" throughout (title, abstract, line 13, line 105, line 122, line 407) and states that remapping "impedes recovery via fine-tuning" (line 122). However, the evaluation only uses the KR metric, which trains a **linear probe on frozen features**. The paper does not test the most natural attack: fine-tuning the *entire* model (feature extractor + head) on the remain set and measuring whether forget accuracy recovers. Since MoRE leaves the feature extractor unchanged and only applies a fixed linear transformation at a specific layer, an adversary who fine-tunes the whole model could potentially learn features that circumvent the transformation. The paper's evidence supports "resistance to linear probing" but not "irreversibility" in any stronger sense. The claims should be calibrated to the evidence.

2. **Theoretical gap: full-rank assumption is not discussed for the k > d case.** Section 3.1 requires **P** to be full column rank to satisfy `DP = I_k` (line 185). However, on ImageNet (1000 classes) with ViT-B/16 (768-dim features), the prototype matrix **P** ∈ ℝ^{768×1000} is necessarily rank-deficient, so `DP = I_k` cannot hold. The paper reports ImageNet results in the appendix (line 286) and the method may still work approximately, but the theoretical foundation as presented breaks down in this critical scalability test. The paper should address this case explicitly.

3. **Factual error: the abstract's "constant memory" claim is contradicted by the paper's own method section.** The abstract (line 13) and bullet-point list (line 123) state "constant space complexity with respect to the number of concepts/classes and feature dimensions." But Section 3.4 (line 229) correctly states O(dk) memory complexity for storing prototypes, which is linear in both d (feature dimension) and k (number of classes). This internal contradiction undermines trust in the experimental reporting.

### Minor

4. **Figure 7 has a clear axis-labeling error.** The caption states the x-axis represents "number of experts" but shows values 0.2 to 0.8 (lines 391–393). The number of experts should be integer values (e.g., 1, 2, 4, 8). This makes the plot uninterpretable in its current form and raises concerns about experimental rigor.

5. **LPIPS_f evaluation contains a notation inconsistency.** Table 2's header shows LPIPS_f(↓), conventionally meaning lower is better, but the text (line 319) states "higher is better" for LPIPS_f. This needs to be resolved. (That said, the harsh critic's claim that UCE outperforms MoRE based on the table numbers is incorrect — under the text's interpretation of higher-is-better, MoRE's 0.33 > UCE's 0.25.)

6. **"Exact feature-level unlearning" is overstated.** The method uses class-mean activation vectors as prototypes and removes only the component along this single direction. The class mean does not necessarily capture the entire discriminative subspace of the forget class. Calling this "exact" is not justified; "prototype-direction erasure" would be more precise.

### Trivial

- Some standard deviation entries in Table 1 are reported as 0.00 (likely rounding), which makes the already-high HM values appear suspicious. Reporting to higher precision or clarifying the rounding convention would help.

## Nice-to-Haves

- **Fine-tuning attack experiment**: Fine-tune the entire unlearned model (feature extractor + classification head) on the remain set for a few epochs, then measure forget test accuracy. This directly tests the "irreversible" claim under the threat model the paper itself warns about (light fine-tuning recovery, line 93).
- **Nonlinear probe evaluation**: Train a small MLP on frozen unlearned features to classify forget vs. remain. If this recovers forget accuracy, the irreversibility claim weakens.
- **Discussion of rank-deficiency fallback**: For k > d scenarios, the paper could discuss using a low-rank approximation, regularization, or explain why the pseudoinverse still yields a useful projection.

## Removed Points

- **Criticism that MoRE's transformation is "trivially invertible"** — the operation includes a complement-space projection (I − PD)z that loses information; the harshest phrasing of this criticism is not backed by analysis of the actual transformation.
- **Criticism that the Van Gogh qualitative claim contradicts the numbers** — under the text's interpretation (higher LPIPS_f is better), MoRE (0.33) outperforms UCE (0.25). The actual issue is a notation inconsistency (see Minor 5), not a contradiction.
- **Several phrasing choices from the harsh critic about "strawman" or "speculative" flaws** — these are removed per the filtering rules.
- **Strength Finder claims about "correctly identifies three challenges" and "proper setup"** — these are generic and removed.
- **Criticism about missing ImageNet results in the main paper** — the paper states these are in the appendix (line 286), which is a standard practice.

## Novel Insights

The reviews collectively surface an interesting meta-point about the unlearning literature: the field's main evaluation protocol (KR/linear probing) may be insufficient to validate "irreversibility" claims. The harsh critic's demand for fine-tuning recovery tests is well-motivated and reflects a broader trend in the community (e.g., the "Do Unlearning Methods Remove Information from Weights?" anchor). The paper would benefit from acknowledging this as a limitation and suggesting it as future work rather than claiming irreversible unlearning on the basis of the KR metric alone. Additionally, the rank-deficiency issue (k > d) is a genuinely subtle theoretical gap that applies broadly to mean-subtraction and prototype-based unlearning methods, not just MoRE, and addressing it would strengthen the whole sub-area.

## Suggestions

1. **Calibrate the claims to the evidence.** Replace "irreversible feature-level unlearning" with "feature-level unlearning resistant to linear probing" or similar. Remove "exact" from the abstract. These changes would bring the language in line with what is actually demonstrated and would not diminish the paper's contribution.
2. **Fix the abstract's memory complexity claim** to match Section 3.4: O(dk) memory, not constant.
3. **Add a paragraph discussing the full-rank limitation** and explain how the method behaves when k > d (e.g., the pseudoinverse still exists but DP ≠ I_k; clarify whether the method still works and why).
4. **Fix Figure 7's x-axis labels** and ensure the plot can be interpreted.
5. **Resolve the LPIPS_f notation inconsistency** between the table header (↓) and the text description.
6. **Add a limitations section** that acknowledges the fine-tuning recovery threat and either provides preliminary experiments or clearly scopes it as future work.

## Score and Decision

**Calibration anchors** (all from the same dataset):

| Path | Avg Score | Comparison to MoRE |
|------|-----------|-------------------|
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/p7mgNvOD9Q.md (SUN) | 4.00 | Similar training-free subspace unlearning. MoRE has a more novel methodology (remapping vs. erasing) and stronger ablations, but shares overclaiming issues. MoRE is stronger. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/pUOesbrlw4.md (Deep Unlearning) | 5.25 | Very similar paper type (training-free class unlearning via SVD/projection). MoRE has a more creative core idea (remapping instead of erasing) and better evaluation. Comparable in scope and strengths. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/KvFk356RpR.md (Unlearning Mapping Attack) | 4.80 | Evaluates unlearning vulnerability rather than proposing a method. Less directly comparable. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/wAemQcyWqq.md (OUbL) | 5.67 | Privacy-preserving unlearning from a different angle. MoRE has stronger empirical results on standard benchmarks. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/OHOmpkGiYK.md (Decoupling Class Label) | 5.75 | Broadens unlearning problem scope. Comparable level of contribution. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/7erlRDoaV8.md (Can Sensitive Info Be Deleted) | 7.50 | Stronger evaluation framework with clear threat model and attack experiments. MoRE is weaker in evaluation rigor. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/Uv7bWrIucU.md (Auditing Privacy) | 4.20 | Auditing-focused paper with limited contribution. MoRE is stronger. |

MoRE is comparable to or slightly stronger than similar training-free class unlearning papers (SUN at 4.00, Deep Unlearning at 5.25) that were rejected. Its novel remapping idea, strong ablations, and diffusion model extension are genuine contributions, but the overclaiming of "irreversibility," the unaddressed rank-deficiency gap, and the internal contradiction in the memory claim prevent it from reaching acceptance level. The paper sits slightly below the typical acceptance threshold for a competitive venue.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>