Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper proposes CaPT (CLIP as a Prior Teacher), a framework that integrates a frozen, adapter-tuned CLIP model into semi-supervised learning via asymmetric-modalities co-training with a standard unimodal network. The method uses co-pseudo labels with entropy-based weighting, feature-level Mixup for CLIP side efficiency, and adapter-tuning to mitigate CLIP's biased predictions. CaPT achieves strong performance across the USB benchmark, ImageNet, fine-grained datasets, and extreme low-label regimes, with especially large gains on CIFAR-100 (+21.38% over the second-best method in the one-label-per-class setting) while adding modest computational overhead.

## Strengths

- **Consistent and large-margin empirical improvements across diverse benchmarks.** CaPT leads in all 6 USB settings (Table 1), often by several points (e.g., +4.09% over RegMixMatch on CIFAR-100 with 2 labels/class, +6.18% on STL-10 with 4 labels/class). The gains are most pronounced in the most challenging low-label regimes (Table 3), which directly supports the paper's central claim.

- **Well-motivated asymmetric-modalities co-training design.** The paper identifies (Figure 3) that two pure-vision ViTs trained with different seeds still produce similar attention patterns ("pattern-homogeneity bottleneck"), while CLIP's multimodal representations provide genuinely complementary attention (e.g., attending to the comb vs. eye/beak of a rooster). This is a principled advance over prior co-training methods like CLS.

- **Comprehensive and honest ablation study.** Table 6 systematically ablates each design choice (adapter-tuning, debiasing, unidirectional flow, only-UPM, only-MPM, feature augmentation, entropy weighting), and the paper also acknowledges its failure case on FGVCAircraft. The transparency of this evaluation is a strength.

- **Practical efficiency.** Table 4 shows CaPT adds only 8.00% memory overhead and 11.18% extra training time over FreeMatch, while achieving +6.23% accuracy — a favorable trade-off that supports practical deployment.

- **Adapter-tuning mitigates CLIP's biased prior.** Figure 5 quantitatively shows that adapter-tuned CLIP produces nearly uniform class predictions, whereas vanilla CLIP concentrates ~25% of predictions on a single class, providing concrete evidence that PEFT addresses the bias problem identified in prior work (DebiasPL).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The co-training (bidirectional) gain is modest compared to simply adding CLIP as a one-way teacher.** The ablation (Table 6) reveals that on CIFAR-100, the one-way CLIP teacher (CaPT-Uni) already improves over the unimodal baseline (only UPM) by **5.35%** (78.60→83.95), while the additional bidirectional co-training (CaPT vs. CaPT-Uni) adds only **0.88%** (83.95→84.83). Similarly on EuroSAT: 1.61% one-way gain vs. 1.49% bidirectional gain. The paper's emphasis on co-training and cross-modal complementarity as the central novelty is thus somewhat disproportionate to the evidence. The method works very well, but the dominant source of gain is incorporating CLIP in any form, not the specific bidirectional mechanism.

2. **Theorem 1.1 is only loosely connected to the actual deep SSL setting.** The theorem bounds pseudo-label error for a nearest-prototype classifier under a Gaussian mixture model with prototype bias \(B\). The paper's method and baselines all use deep neural networks with consistency regularization, confidence-based filtering, and learned representations that shift during training — none of which are captured by this analytic model. While it is common to use simplified theory for motivation, presenting this as a "fundamental limitation" of modern SSL methods overstates its scope. The paper would benefit from either removing the theorem or explicitly clarifying that it provides intuition for a simplified setting rather than a formal characterization of deep SSL.

3. **"Breaking label dependency" framing is inflated.** The title and abstract claim that CaPT "breaks the label dependency" in SSL, but what the method actually does is *augment* SSL with a powerful external prior from CLIP. The label dependency of the unimodal network is still present; it is circumvented by injecting external multimodal knowledge rather than truly eliminated. This overclaiming is amplified by the fact that the largest gains occur on datasets where CLIP already has strong zero-shot performance (CIFAR-100: 65.1% zero-shot). The paper's contribution is better described as leveraging CLIP priors to *mitigate* label dependency.

4. **Suspiciously low standard deviations.** CaPT's standard deviations (e.g., 0.05–0.13 on STL-10) are substantially lower than baselines (e.g., 1.89–3.22 for baselines on STL-10 with 4 labels). The paper attributes this to reduced label dependency, but an alternative explanation is that the frozen CLIP dominates training dynamics to the point of suppressing seed variability. A brief discussion or analysis would be helpful.

5. **Failure on FGVCAircraft.** CaPT underperforms FreeMatch on FGVCAircraft (50.12% vs. 51.43%). The authors acknowledge this and attribute it to CLIP's weak zero-shot performance (18.97%) on that dataset. While honest, this reveals a brittleness that limits the generality claim — the framework's success is contingent on the strength of the VLM prior, which is not always available.

### Trivial

- The paper could mention that the co-training ablation (CaPT-Uni vs. CaPT) shows a modest gain and comment on why the bidirectional mechanism nonetheless matters conceptually despite its small numerical contribution (e.g., as a future-proofing feature for stronger VLMs).

## Nice-to-Haves

- **Compare against a simpler CLIP-utilization baseline**: Using CLIP's zero-shot predictions as fixed soft pseudo labels (with temperature scaling or confidence thresholding) added to the existing SSL loss. This would directly test whether the adapter-tuning and co-training framework is needed, or whether simply adding CLIP's output is sufficient for most of the gain.
- **Quantify the complementarity over training**: The paper claims asymmetric modalities mitigate pattern-homogeneity (Figure 3) but provides no quantitative metric (e.g., prediction agreement rate, CKA similarity) over the course of training. Showing that the two models' predictions diverge meaningfully and that divergence correlates with co-training improvement would strengthen the claim.
- **Plot the entropy-based weights \(\Gamma^a\) and \(\Gamma^b\) over training iterations** to support the claim that CLIP dominates early and the unimodal network takes over later.
- **Test on datasets where CLIP zero-shot is very weak** (e.g., medical imaging, specialized satellite domains) to stress-test the framework's robustness, beyond the one FGVCAircraft case.

## Removed Points

These points are flagged to be removed, treat them with caution:

- The harsh critic's point about "incomplete control for the strength of the CLIP backbone" is partially misaligned: the paper compares against methods that use the *same* pre-trained ViT backbone (as per USB standard). The critic's request for a baseline using CLIP zero-shot as fixed targets is moved to Nice-to-Haves, not a core weakness — the paper already compares against DebiasPL and adapter-tuned variants, which are the relevant CLIP-based SSL baselines.
- The harsh critic's claim that "absent comparisons against other CLIP-based SSL methods" is a weakness: the paper compares against DebiasPL, the only method the authors identify as related. Since I cannot independently verify whether other CLIP+SSL methods exist, this criticism is removed per instructions.
- Some of the Strength Finder's claimed strengths (e.g., the theorem being a "core strength") are weakened by the verified disconnection between the theory and deep SSL practice. The theorem is kept as a motivational framework but downgraded.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the contribution**: Shift from "breaking label dependency" to "mitigating label dependency via external VLM priors." Be explicit that the largest gains come from injecting CLIP knowledge, with co-training playing a supporting role. The current framing invites unnecessary scrutiny.

2. **Either drop Theorem 1.1 or bridge it**: Either remove the theorem entirely and rely on the strong empirical motivation (Figure 1), or add a paragraph explaining how the simplified model connects to deep SSL (e.g., treating learned representations as prototype-based, or noting that consistency regularization can be seen as implicitly enforcing prototype structure).

3. **Add the simple CLIP-as-fixed-teacher baseline** to Table 6 or an appendix. This would cleanly separate the question of "is CLIP helpful?" from "is the CaPT framework the best way to use CLIP in SSL?" and would significantly strengthen the paper.

4. **Discuss the suspiciously low variance** in a sentence or two in Section 4.1. Even a brief acknowledgement would address what some readers will perceive as a red flag.

5. **Soften the title**: "Breaking the Label Dependency" is too strong. Something like "Mitigating Label Dependency in Semi-Supervised Learning with a CLIP Prior Teacher" would be more accurate and less likely to draw criticism.

## Score and Decision

**Calibration anchors** (all from /home/wg25r/review_agent/human_reviews_2026/):

| Anchor | Avg Score | Comparison to CaPT |
|--------|-----------|-------------------|
| fwMEqaKgTd.md (Rethinking SSL in the Era of Large Models) | 4.67 (Reject) | Much weaker — it is purely an empirical comparison without a new method. CaPT proposes a real method with strong results. |
| 4PxRhcO8fz.md (DHO for VLM distillation in SSL) | 4.67 (Reject, scores 4/2/8) | Similar problem setting and also uses VLMs in SSL, but CaPT has more thorough experiments, broader evaluation, and better ablation. |
| H4RVXhicSj.md (CLOP: Contrastive SSL with orthonormal prototypes) | 5.00 (Reject) | CLOP has theory + experiments but narrower scope. CaPT covers more benchmarks, settings, and has a clearer practical contribution. |
| lqrpmqrTnH.md (In-Context SSL) | 4.50 (Accept Poster) | IC-SSL is more theoretical and niche. CaPT has broader empirical impact and clearer applicability. |
| SXR1bpHHCg.md (LapBoost) | 2.50 (Reject) | Much weaker — poor presentation, incremental, limited experiments. CaPT is substantially stronger across all dimensions. |
| oN55r8iJJW.md (SAM-Veteran) | 7.00 (Accept Poster) | Stronger paper with a more novel methodological contribution (RL-based reasoning segmentation). CaPT is more of an engineering contribution but still solid. |

CaPT sits above the 4-5 range papers (it has a real method, thorough experiments, and clear results) but below the 7+ tier (the novelty is more architectural/application-level than foundational, the theory is loose, and the central claim is somewhat overstated). Relative to the anchors, I assess CaPT at **6.0** — a solid paper with strong empirical validation, a well-designed framework, and clear practical value, but with some overclaiming and a few evidential gaps that prevent it from reaching the top tier.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>