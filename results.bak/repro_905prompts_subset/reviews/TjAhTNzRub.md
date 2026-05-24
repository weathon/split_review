Now I have all the information needed to write the consolidated review. Let me synthesize it carefully.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me now produce the final review.

---

Anchor papers used for calibration:

**Round 1 (bracketing):**
- Weak band (avg < 3.5): Xagys9QD3T (PPU, 3.00), hwXUmwJAq5 (UGradSL, 3.00), BJfIDS5LsS (MASIMU, 2.50), 85X9awoVtv (Auditing, 2.50) — all rejected, simpler methods
- Mid band (3.5-7.5): p7mgNvOD9Q (SUN, 4.00, rejected), pUOesbrlw4 (Deep Unlearning, 5.25, rejected), 7tpMhoPXrL (Forget Vectors, 4.80, rejected), okRSNTMdFg (Meta-Unlearning, 4.00)
- Strong band (avg > 7.5): PBjCTeDL6o (UNI, 8.00, accepted), 51WraMid8K (Probabilistic LLM Unlearning, 8.00, accepted), gc8QAQfXv6 (Function Vectors, 9.00, accepted), j7b4mm7Ec9 (Watermarking, 7.60, rejected)

**Round 1 bracket determination:** The paper clearly falls between the weak anchors (2.5-3.0) and strong anchors (8.0-9.0). The most topically similar anchors are SUN (4.0) and Deep Unlearning (5.25), both training-free subspace methods. MoRE is technically stronger than both. Bracket: 4.5–6.5.

**Round 2 (narrowing):**
- Lower-mid (4.5-6.0): pUOesbrlw4 (Deep Unlearning, 5.25), OHOmpkGiYK (TARF, 5.75), TLBPjECC5D (Sparse Representations, 5.25), 7tpMhoPXrL (Forget Vectors, 4.80)
- Upper-mid (6.0-7.5): fMNRYBvcQN (Jogging Memory, 6.75, accepted), UstOpZCESc (Privacy-Aware Lifelong, 6.25, accepted), gjwhDHeAsz (SFD, 6.50, accepted)

MoRE is clearly stronger than SUN (4.0) and Forget Vectors (4.80) — more sophisticated methodology, better evaluation breadth. It is comparable to Deep Unlearning (5.25) and TARF (5.75) in terms of contribution density, but stronger in technical novelty (PO projection + remapping is more than SVD subspace removal). However, the SFD paper (6.50, accepted) has a cleaner evaluation story and is accepted. MoRE has a similar issue to Deep Unlearning: interesting method with incomplete evaluation of the central claim (irreversibility). Given these comparisons, I place MoRE at **5.5** — stronger than 5.25 methods but with unresolved evaluation gaps that keep it below the accepted 6.5 range.

---

## Final Review

## Summary

MoRE proposes a training-free framework for feature-level machine unlearning that combines (i) prototype-orthogonal (PO) projection to decorrelate forget and remain prototypes before editing, (ii) erasure-then-remapping of forget prototypes into remain-class distributions, and (iii) a mixture-of-experts mechanism that scatters forget features across multiple remain prototypes to break residual cohesive structure. Experiments on CIFAR-10/100, Tiny-ImageNet, ImageNet, and Stable Diffusion v1.4 show that MoRE achieves near-zero forget accuracy while preserving remain accuracy, with orders-of-magnitude less compute than training-based methods.

## Strengths

- **Prototype-orthogonal projection is a principled and effective solution to utility preservation.** The paper identifies that forget and remain prototypes are highly correlated (cosine similarity up to 0.77 in CIFAR-10), and shows that naive erasure damages remain prototypes (autocorrelation drops from 1.0→0.52). The pseudoinverse-based PO projection mathematically guarantees that erasing one prototype does not distort others. The ablation in Table 3 convincingly demonstrates this: without PO, Remap drops remain HM from 95.38→88.67 on CIFAR-10; with PO, both erasure and remapping preserve near-perfect remain performance.

- **Remapping with multiple experts provides a clean, novel mechanism for disrupting feature-level separability.** The t-SNE visualization (Figure 1) shows that ESC leaves a distinct forget cluster, single-expert remapping absorbs it into one remain cluster (reducing separability but leaving cohesion), and MoRE with multiple experts scatters forget features across the latent space. This progressive degradation of recoverable structure is well-motivated and directly addresses the residual cluster problem of ESC.

- **Exceptional efficiency and scalability.** MoRE completes unlearning in under 10 seconds with <200 MB GPU memory on CIFAR-10/100 (Figure 5), while ESC requires O(N_f d) memory for SVD. The O(Nd) time / O(dk) memory complexity (Section 3.4) is clearly stated and represents genuine improvement over ESC's O(N_f d) memory bottleneck.

- **Broad applicability demonstrated across both discriminative and generative models.** MoRE achieves the best LPIPS_d tradeoff (0.25 for Van Gogh, 0.26 for Kelly McKernan) among all training-free diffusion unlearning methods (Table 2), while being applied out-of-the-box with no architecture-specific adaptation.

## Weaknesses

### Major

1. **The central claim of "irreversibility" is tested only via linear probing, not against fine-tuning attacks.** The paper repeatedly states that MoRE "impedes recovery via fine-tuning" (Abstract, Section 3, Section 1), yet the entire KR evaluation uses linear probes only. A determined adversary could fine-tune the full model (not just a linear head) on a small forget subset — the paper's own shallower-layer analysis (Table 7) shows MoRE weakens at earlier layers, suggesting the effect may be partially reversible with deeper re-training. Without a fine-tuning attack experiment (e.g., fine-tuning on 1%, 5%, 10% of forget data and measuring forget accuracy), the irreversibility claim remains insufficiently supported. This is the most significant gap in the evaluation.

2. **The KR metric — the primary evidence for irreversibility — is defined entirely in the appendix (B.3), leaving the main-text evaluation incomplete.** The paper states that KR measures "feature-level unlearning performance" and gives the brief note "lr=0.1" in the table headers, but the reader cannot independently verify what the KR protocol entails: Is the linear probe trained on the forget subset, remain subset, or full dataset? What is the probe architecture, training budget, and evaluation procedure? The retrain baseline achieves 72.62% forget accuracy under KR on CIFAR-10 (vs. 10% random), which needs explanation in the main text — without it, the KR results invite confusion rather than confidence. While the appendix presumably contains this information (and was stripped by the parser), the paper should provide enough protocol detail in the main text for the reader to interpret the central evaluation metric.

### Minor

3. **The "constant memory" claim in the abstract is imprecise.** The abstract claims "linear computational complexity and constant memory," but Section 3.4 correctly states O(dk) memory for storing prototypes — this grows linearly in the feature dimension d and number of concepts k, not constant. The intended meaning is "constant with respect to the number of data samples N" (in contrast to ESC's O(N_f d)), but the phrasing in the abstract could mislead.

4. **Stochastic routing "ensures an even workload among the experts" only in expectation.** For a finite forget set, random assignment does not guarantee balanced usage — some experts may receive few or no samples. The paper acknowledges this implicitly by noting the stochastic router is the default, but the claim of guaranteed even workload is overstated.

5. **The diffusion model results are competitive but not uniformly superior.** While MoRE achieves the best LPIPS_d tradeoff (Table 2), its LPIPS_f (0.33) is lower than SAFEE (0.42) and ESD (0.40), meaning the style change detection is weaker. The paper's claim of "outperforming SOTA diffusion model unlearning methods" should be qualified to reflect that MoRE wins primarily on the tradeoff metric rather than all dimensions.

### Trivial

6. **Main results table (Table 1) reports means without visible standard deviations.** The caption states "mean ± std across three trials" but the table values show only means. Standard deviations are shown for some ablation tables but not the main results, making variance assessment difficult.

## Nice-to-Haves

- **Fine-tuning attack experiment** (as discussed in weakness #1 above) would substantially strengthen the irreversibility claim.
- **A brief intuitive explanation of the retrain baseline's KR performance** (e.g., "the retrain model's features capture visual concepts shared with the forget class, so a probe trained on all classes achieves 72.62%") would preempt confusion.
- **The "complement-space projection" term in Eq. 4** could be discussed more: does the complement space (I - PD)z contain residual forget-relevant information that a stronger attack could exploit?

## Removed Points

The following points from the inputs were removed with justification:

- **KR metric "not properly defined" / "appears nowhere in the main text":** The paper explicitly names the KR metric, cites its origin in Lee et al. (2025), states it measures "feature-level unlearning performance," and directs to Appendix B.3 for implementation details. This is proper referencing practice, and the appendix was stripped by the parser.
- **Retrain baseline KR performance (72.62%) is "implausible":** Not implausible — a model trained on 9/10 CIFAR-10 classes still produces features that correlate with the held-out class (shared visual concepts). A linear probe trained on the full 10-class feature set can achieve well-above-chance accuracy on the forgotten class. This is a known property, not an error.
- **ESC has D_rt=88.81 in KR setting:** This is a misreading of Table 1. ESC in the KR setting has D_R=88.81 and D_rt=0.74. The critic confused D_R with D_rt.
- **"MoRE and Remap show no std" in Table 1:** No method in Table 1 shows visible std values — this is a presentation issue affecting all methods equally, not unique to MoRE.
- **"training-free" contradiction with trained conditional router:** The paper clearly states the stochastic router is the default and is training-free, while the conditional router (MoRE-P-T-B) is a separate trained variant explored in Table 6. No contradiction.
- **Missing appendix/proofs/references:** Stripped by the parser; not author errors.
- **Pure speculation about KR protocol contamination:** The critic suggests the KR protocol "uses the full dataset to train the probe" as one possible explanation — this is speculation, not a verified flaw.
- **Generic scope-creep demands** (e.g., "larger dataset", "more models"): The evaluation already spans CIFAR-10/100, Tiny-ImageNet, ImageNet, and Stable Diffusion with multiple architectures.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a fine-tuning attack experiment where the unlearned model is fine-tuned on small subsets of forget data (1%, 5%, 10%) and forget accuracy is measured — this directly tests the irreversibility claim against the most natural adversary.
2. Move a brief description of the KR evaluation protocol into the main text: what probe is trained, on which data split, with what hyperparameters, and why the retrain baseline achieves 72.62% on CIFAR-10.
3. Qualify the "constant memory" claim to "constant with respect to the number of data samples" for precision.
4. Add standard deviations to the main results table for all methods.

## Score and Decision

**Score:** 5.5  
**Decision:** Reject

The paper presents a technically sound and well-motivated framework with genuine contributions (PO projection, remapping-based irreversibility, training-free efficiency). The ablation study is strong, and the method is clearly superior to ESC in both utility preservation and feature-level dispersion. However, the evaluation of the paper's central claim — *irreversible* feature-level unlearning — relies entirely on linear-probe recovery (the KR metric) and lacks any fine-tuning attack experiment. Given that the paper itself motivates its design as "impeding recovery via fine-tuning," the absence of this experiment is a significant gap. The KR metric details are deferred to the appendix, and the main text does not provide enough protocol information for independent interpretation of the central results. These issues keep the paper below the acceptance threshold for a top venue, but the method is promising and the gaps are addressable with targeted additional experiments.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>