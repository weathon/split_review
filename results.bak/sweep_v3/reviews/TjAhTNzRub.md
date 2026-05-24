Now I have all the context I need. Let me write the consolidated review.

## Summary

The paper proposes MoRE (Mixture of Remapping Experts), a training-free framework for class-wise machine unlearning that operates at the feature level. MoRE introduces three innovations: (1) prototype-orthogonal (PO) projection to decorrelate forget and remain prototypes before erasure, preserving utility; (2) remapping forget prototypes onto multiple remain prototypes via mixture-of-experts to scatter forget features and block recovery through probing; (3) efficient activation-mean prototypes for O(Nd) prototype collection and O(dk) memory. Experiments on CIFAR-10/100, Tiny-ImageNet, and ImageNet show that MoRE achieves near-random forget accuracy under the Knowledge Retention (KR) probing metric while maintaining remain-set accuracy, all in under 10 seconds of compute, outperforming training-based baselines including retrain-from-scratch in the KR setting.

## Strengths

1. **Prototype-orthogonal projection demonstrably solves the utility-degradation problem.** Section 3.1 identifies that forget and remain prototypes are highly correlated (cosine similarities ~0.5, up to 0.77, Fig. 3) and that naive erasure (ESC) drops remain prototype autocorrelation from 1.0 to 0.52. The PO projection via pseudoinverse (Eq. 2) decorrelates prototypes so that erasing a forget prototype does not distort remain prototypes. Table 3 shows the ablation: without PO, Remap achieves remain accuracy D_r=89.52; with PO, D_r=99.87. This cleanly addresses a known limitation of prior work.

2. **Remapping with mixture experts achieves state-of-the-art resistance to linear probing.** In the KR evaluation (Table 1), MoRE drives forget accuracy to near random-guess levels across all datasets (CIFAR-10: 9.01% vs 10% random; CIFAR-100: 0.07% vs 1% random; Tiny-ImageNet: 0.50% vs 0.5% random). This decisively outperforms all baselines, including retrain-from-scratch (which achieves 72.62%/57.20%/78.57% forget accuracy under KR). The t-SNE visualization (Fig. 1) provides qualitative evidence that MoRE scatters forget features across the latent space rather than leaving a separable cluster.

3. **Exceptional efficiency without sacrificing effectiveness.** Fig. 5 shows MoRE completes unlearning in 9.5 seconds using 540 MB GPU memory on CIFAR-10/100, whereas training-based methods (Prototype, PO, PE) take ≥88 seconds. Despite this efficiency, MoRE outperforms all training-based baselines in HM across all datasets (Table 1), establishing a new Pareto frontier in the unlearning efficiency-effectiveness trade-off.

4. **Robustness to design choices.** Fig. 7 shows HM stability over a wide range of expert counts for all three datasets. Table 5 shows that different target remapping classes yield nearly identical HM (95.38–95.16 on CIFAR-10 standard), indicating the framework is not brittle to this design choice.

## Weaknesses

### Fatal

None.

### Major

1. **The central claim of "irreversible" unlearning is overstated relative to the evidence provided.** The paper uses "irreversible" in its title, abstract, and throughout (e.g., "irreversible feature-level unlearning," "ensuring irreversibility at the feature level"). However, the evidence for irreversibility comes entirely from the KR metric — a *linear probe* trained at a *single* learning rate (lr=0.1). While the results at this configuration are impressive (near-random forget accuracy), a linear probe is a weak adversary: non-linear probes, deeper fine-tuning with more epochs, or feature-reconstruction attacks might still recover forget information. The paper's own remapping operation (Eq. 6) is a *linear* transformation on features, meaning that the information is remapped rather than destroyed. The authors should either (a) add experiments with stronger recovery methods (non-linear probes, full-model fine-tuning, feature inversion) or (b) adopt more measured language such as "resistant to linear probing" or "effectively blocks recovery via light fine-tuning." The current terminology promises a guarantee that the experiments do not fully support.

2. **The diffusion-model adaptation is presented with insufficient methodological detail.** Section 4.1 states that MoRE is applied "out of the box" to cross-attention layers of Stable Diffusion v1.4, "using tokenized input prompts to construct prototypes." The paper does not specify: how prototypes are derived from tokenized prompts, which cross-attention layers are modified, how the forget/remain split is defined for artistic styles, or how the linear projection (Eq. 6) operates on cross-attention keys/values. Since the appendix is stripped, these details may exist there, but the main text lacks a self-contained description adequate for reproducibility. Given that the diffusion results (Table 2, Fig. 4) are presented as evidence of generalizability, the methodological gap is significant.

### Minor

1. **"Constant space" claim in the abstract is inconsistent with the methods section.** The abstract states "constant space complexity with respect to the number of concepts/classes and feature dimensions," but Section 3.4 correctly states O(dk) memory complexity for storing prototypes. The abstract is wrong; O(dk) scales linearly with both dimensions and number of classes. This does not undermine the method's efficiency (which is still excellent) but should be corrected.

2. **Statistical significance is inconsistently reported.** Standard deviations are reported in some tables (e.g., Table 6 for router variants, Table 7 for layer ablation) but not in the main results (Table 1). While the results are so strong that significance is unlikely to change the conclusions, the inconsistency is a presentation issue.

### Trivial

None.

## Nice-to-Haves

- Adding non-linear probing or stronger recovery attacks would strengthen the irreversibility claim.
- A brief limitations paragraph discussing scenarios where MoRE might struggle (e.g., when class prototypes are not well-separated, or very small k) would improve completeness.
- Reporting standard deviations in Table 1 would improve consistency.

## Removed Points

- **Harsh critic's claim that SVD of P is "not O(Nd)" and should be O(dk²).** The paper's O(Nd) claim is about prototype collection (computing activation means), not about SVD computation. The methods section (Sec. 3.4) separately states O(Nd) for prototype collection and O(dk) for memory — it never claims SVD is O(Nd). The reviewer conflated different operations.

- **Harsh critic's claim that storing P requires O(dk) memory contradicts "constant space."** This is true (see Weakness Minor #1 above), but the reviewer's framing as a "methodological gap" is too severe — it is a minor wording inconsistency in the abstract, and the methods section correctly reports O(dk).

- **Strength Finder's claim about "ensuring irreversibility at the feature level."** While the evidence is strong, the word "ensuring" overstates what a linear-probe-only evaluation can guarantee. Absorbed into the Major weakness above.

- **Strength Finder's generic praise** (e.g., "the paper addresses an important problem"). These are superficial and lack specific evidentiary anchors.

- **Harsh critic's comment about missing hyperparameters for ESC and KR metric details.** The paper states these are in the appendix (which is stripped). This is a known parser artifact, not an author error.

- **Strength Finder's claim that "MoRE achieves the best LPIPS_d among all training-free methods, exceeding specialized diffusion unlearning approaches."** This is factually correct per Table 2 (MoRE LPIPS_d=0.25 for Van Gogh vs. next best RECE 0.23), so it's retained in strengths.

- **Harsh critic's point about SVD pseudoinverse via normal equations being fine.** The paper's choice to use SVD for numerical stability (avoiding condition-number squaring) is a standard and reasonable practice. This is a nitpick.

## Novel Insights

Beyond the paper's own contributions, the reviews surface an interesting tension: the paper's key technical strength (remapping forget features into the remain distribution via a *linear* operation) is the same reason that "irreversibility" is hard to guarantee — a linear remapping is mathematically invertible if the exact transformation is known, so the protection comes from the difficulty of inferring the mapping, not from information destruction. This suggests that the paper's true contribution is best understood as *practical irreversibility* (make recovery harder than it is worth) rather than *theoretical irreversibility*, and future work could explore whether adding non-linear components to the remapping could strengthen the guarantee.

## Suggestions

1. **Soften the "irreversible" language** throughout to something like "effectively irreversible under linear probing and light fine-tuning" or add stronger recovery experiments (non-linear probes, full fine-tuning, feature reconstruction). This is the single change that would most improve the paper.
2. **Expand the diffusion-model description** in the main text, even briefly: specify which cross-attention layers are modified, how prototypes are derived from tokenized prompts, and how forget/remain splits are defined for artistic styles.
3. **Correct the abstract's "constant space" claim** to match Section 3.4's correct O(dk) characterization.
4. **Add standard deviations to Table 1** for consistency with other tables.

## Score and Decision

### Calibration Anchors

| Anchor Path | Avg Score | Comparison |
|---|---|---|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/PBjCTeDL6o.md` | 8.00 | Stronger theoretical foundation and broader applicability, but MoRE's empirical results (outperforming retrain) are more striking for its subfield |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/OHOmpkGiYK.md` | 5.75 | Both address class-wise unlearning; MoRE has stronger results and addresses a more fundamental problem (residual feature-level knowledge), making it a stronger paper |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/wAemQcyWqq.md` | 5.67 | OUbL tackles a different unlearning problem (privacy-preserving oblivious unlearning); MoRE is empirically stronger and better validated |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/pUOesbrlw4.md` | 5.25 | Similar SVD-based class unlearning approach, but MoRE addresses real limitations (utility, residual cohesion) with novel techniques and achieves much stronger results |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/p7mgNvOD9Q.md` | 4.00 | SUN is also a training-free subspace unlearning method; MoRE's results and methodological novelty are substantially stronger |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/KvFk356RpR.md` | 4.80 | Addresses unlearning vulnerabilities rather than proposing a new unlearning method; different contribution type |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Xagys9QD3T.md` | 3.00 | PPU has a weaker method and limited evaluation; MoRE is significantly stronger on all fronts |

The paper makes a clear, well-supported contribution to class-wise unlearning with novel technical ideas (PO projection, prototype remapping via MoE) and state-of-the-art results that surpass even retrain-from-scratch under the KR metric. The core weakness is the overclaimed "irreversibility" label — a real issue but fixable. Relative to the mid-range unlearning papers (scoring 5–6), MoRE is clearly stronger in terms of both novelty and empirical results. Relative to top papers (scoring 7.5+), it falls short in presentation rigor and breadth of evidence for its strongest claim. A score of 6.5 reflects a solid, above-threshold contribution with clear issues to address.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>