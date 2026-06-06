## Summary
CaPT introduces an asymmetric-modalities co-training framework that integrates CLIP as a "prior teacher" into semi-supervised learning (SSL). The core insight is that SSL methods under extreme label scarcity suffer from degraded pseudo-label quality and fail to leverage unlabeled data—a limitation the paper formalizes with Theorem 1.1 and motivates empirically. CaPT addresses this by jointly training a fully fine-tuned unimodal ViT and an adapter-tuned CLIP model via entropy-weighted co-pseudo labels and feature-augmented consistency regularization. It achieves state-of-the-art results across multiple SSL benchmarks, with particularly pronounced gains in the one-label-per-class regime (21.38% over the next-best method on CIFAR-100).

---

## Strengths

- **Dramatic gains in low-label regimes**: Table 3 confirms a +21.38% improvement on CIFAR-100 (1-label/class) and +4.05% on EuroSAT over the previous best SSL method, directly supporting the paper's central claim that CLIP's prior can unlock unlabeled data where standard SSL collapses.

- **Compelling motivating evidence**: Figure 1c demonstrates that FreeMatch's accuracy gain from unlabeled data on CIFAR-100 under the 1-label setting approaches zero, which precisely and directly motivates the paper's entire approach. Figure 1b (pseudo-label accuracy degrading with label prototypicality) is equally sharp. These two figures make the problem concrete without relying on the theorem.

- **Strong ablation design**: Table 6 systematically ablates every component — adapter-tuning (CaPT-Deb, −12.73% EuroSAT), bidirectional flow (CaPT-Uni, −0.88%/−1.49%), feature-augmented consistency (−0.57%/−1.81%), and entropy-based weighting (−0.87%/−1.57%). Each component's necessity is empirically justified, and the magnitude of the ablation drops is credibly large for critical components.

- **Computational efficiency**: Table 4 shows CaPT adds only 8% memory and 11% training time over FreeMatch, while delivering a 6.23% accuracy improvement on CIFAR-100 with 2 labels/class. This makes the approach practically viable.

- **Cross-modal complementarity evidence**: Figure 3 provides direct visual evidence that CLIP's ViT attends to qualitatively different image features (rooster comb vs. eye/beak) compared to two unimodally-pretrained ViTs, grounding the argument that asymmetric modalities break the pattern-homogeneity bottleneck.

- **Bias mitigation via adapter-tuning**: Figure 5 shows that zero-shot CLIP's highly skewed class distribution on EuroSAT (peak ~0.25 on one class) becomes balanced after adapter-tuning, and the CaPT-Deb row in Table 6 (−12.73% EuroSAT when adapter-tuning is removed) quantifies the importance of this correction.

---

## Weaknesses

### Fatal
None.

### Major

- **DebiasPL and CLS are absent from all main result tables**: DebiasPL is the closest prior work (integrating CLIP into SSL via a unidirectional prior) and CLS (Yao et al., 2022) is the direct methodological predecessor for co-training in SSL. Both are discussed at length in Section 2 and depicted in Figure 2, yet neither appears in Tables 1–5. The CaPT-Deb ablation in Table 6 partially substitutes for a DebiasPL comparison but is not equivalent: per Section 4.5, CaPT-Deb simultaneously disables adapter-tuning *and* the vision-model→CLIP feedback flow, conflating two distinct design choices. This means the paper cannot cleanly isolate the contribution of adapter-tuning alone (i.e., what CLIP with adapter tuning but without bidirectional feedback would achieve) relative to DebiasPL's actual behavior. Including DebiasPL as a baseline and CLS in at least one result table is necessary to fully close the argument that CaPT's improvements stem specifically from the asymmetric-modalities co-training design rather than from CLIP integration or co-training in isolation.

### Minor

- **Theorem 1.1 framing overstates the theoretical contribution**: The theorem assumes a Gaussian mixture generative model and a nearest-prototype classifier, both far from the actual training setup with deep networks. The paper's contribution list states "we theoretically establish the label dependency that constrains SSL," but the theorem's conclusion — that larger prototype bias *B* or smaller labeled set size increases pseudo-label error — is intuitive and would be accepted without proof. The theorem is not wrong and provides useful vocabulary, but the gap between its assumptions and the actual CaPT setting is not acknowledged. The stronger case for label dependency rests on Figure 1b and Figure 1c rather than on Equation 1.

- **SVHN result is the paper's most surprising finding yet receives the least analysis**: Table 5 shows CLIP zero-shot accuracy on SVHN is only 34.36% — far below the SSL baselines — yet CaPT achieves 81.20% vs. FreeMatch's 67.35% (a 13.85-point gain). This is an important empirical result precisely because it involves a badly biased CLIP prior that the framework successfully salvages. The paper notes FGVCAircraft (a failure case) and defers it to Appendix N, but the SVHN case receives no analogous treatment in the main text. Understanding whether this gain comes from the adapter alone or from the UPM feedback loop would considerably strengthen the "reliable prior through co-training" argument.

- **Hard vs. soft pseudo-label weighting (Eq. 13) is unmotivated and unablated**: The co-pseudo label is computed as $\tilde{q}^c = \Gamma^a \hat{q}^a + \Gamma^b \hat{q}^b$ where $\hat{q}^a, \hat{q}^b$ are argmax one-hot vectors (Eq. 10), not the soft distributions $q^{w,a}, q^{w,b}$. Weighting hard one-hot vectors discards all second-order uncertainty when the two models agree on the top class but have different confidence levels. The choice is not motivated, and no ablation compares hard vs. soft pseudo-label weighting in Table 6. Given that this is a load-bearing design choice in PFM, the omission is notable.

### Trivial

- **Memory efficiency explanation is implicit**: The claim that CaPT uses only 8% more memory than FreeMatch despite running a second transformer (Table 4) is plausible (CLIP's encoder is frozen, so no gradient memory is needed for its parameters beyond the small adapters), but this explanation does not appear in the main text. A single sentence in Section 4.3 would make the result more readable.

---

## Nice-to-Haves

- An ablation that replaces the CLIP branch with a second ViT initialized from CLIP's visual encoder weights but without text-alignment would isolate whether the gains stem from CLIP's vision-language pre-training specifically or from any two models with different inductive biases. Figure 3 is suggestive but not conclusive without this control.
- The ImageNet section (Section 4.2) reports 10 and 100 labels per class (10,000 and 100,000 total labeled samples in a 1000-class setting). A brief note on whether labeled samples are class-balanced and how threshold filtering operates at 1000-class scale would help readers interpret the scalability claims.
- Expanding the SVHN analysis (at least briefly) in the main text would transform it from an unexplained outlier into strong confirmatory evidence for the "co-training refines biased priors" narrative.

---

## Removed Points

*These points are flagged for removal; treat them with caution.*

- **"Feature-augmented regularization framed as purely principled"** (Harsh Critic, Section 3.2.2): Section 3.2.2 explicitly states "Feature-augmented consistency regularization not only improves the generalization of CLIP but also *avoids the need to construct another high-resolution version*..." — the paper does acknowledge the efficiency motivation alongside the regularization benefit. The framing criticism is factually incorrect.

- **"ImageNet 10-label setting is not trivially low supervision"** (Harsh Critic, Section 4.2): The paper frames it as lower supervision relative to standard supervised training, not as an extreme scarcity setting comparable to the 1-label-per-class experiments. The criticism misreads the scope of the experiment.

- **Theorem 1.1 as "structural flaw"**: The harsh critic labels the theoretical mismatch "fatal" at points. After review, the theory's assumptions are standard in the analysis-of-SSL literature and the empirical evidence independently supports all theoretical claims. The limitation is real but amounts to a framing issue, not a structural flaw.

- **"STL10 shows adapter-tuned CLIP outperforms full CaPT"** (implicit in Table 1 numbers): Adapter-tuned CLIP alone achieves 96.86%/97.15% on STL10 vs. CaPT's 96.07%/96.34%. This potentially embarrassing result is not discussed in the paper; however, because STL10 is visually similar to ImageNet (on which CLIP was trained), the high standalone CLIP performance is expected and does not undermine the framework's purpose, which is most valuable when CLIP's prior is imperfect.

---

## Novel Insights

The paper's most genuinely novel empirical finding is that a badly biased CLIP prior (34.36% zero-shot on SVHN) can be recalibrated through asymmetric co-training to substantially outperform SSL baselines that start from a much stronger supervised signal. This goes beyond the expected result that "good CLIP prior + SSL = better performance" and suggests that the bidirectional co-training loop itself is doing calibration work rather than merely providing pseudo-labels. This finding is currently buried and underanalyzed, but it points toward a potentially broader principle: co-training with a complementary-modality model can rescue weak or biased priors in ways that unidirectional integration cannot.

---

## Suggestions

1. Add DebiasPL as a direct baseline in at least Tables 1 and 3 (the USB and 1-label benchmarks). Additionally, add a separate ablation row that disables only the adapter-tuning (keeping bidirectional flow) to cleanly isolate the adapter's contribution from the co-training design relative to DebiasPL.
2. Include CLS (Yao et al., 2022) in Tables 1 or 3 with one or two benchmark settings to directly quantify the benefit of asymmetric-modalities co-training over symmetric co-training.
3. Add a brief (2–3 sentence) analysis of the SVHN result in Section 4.4: does the gain emerge primarily after adapter tuning stabilizes, or does the UPM feedback drive early improvement? Training curves would suffice.
4. Ablate hard vs. soft pseudo-label weighting in Table 6 to justify the argmax design in Eq. 13.
5. Revise Contribution 1 in the Introduction to be explicit that the theoretical result holds under Gaussian mixture / nearest-prototype assumptions and that the empirical evidence (Figure 1b–c) provides the primary support.

---

## Assessment on Key Axes

- **Originality**: The asymmetric-modalities co-training design with entropy-weighted co-pseudo labels is a clean, non-obvious synthesis of adapter-tuning and co-training. The observation that CLIP's prior can be used *against* label dependency rather than simply as a stronger supervised signal is the paper's key conceptual move. Solid originality.
- **Importance of research question**: Label scarcity is a central challenge in practical ML deployment, and the 1-label-per-class regime is highly realistic. The question is well-motivated.
- **Claims well supported**: The main quantitative claims are strongly supported by experiments. The theoretical claim is supported but slightly overstated given the gap between theorem assumptions and practice.
- **Soundness of experiments**: Broadly sound. Multiple benchmarks, multiple label scales, ablations for all components, efficiency measurements. The main gap is the missing DebiasPL/CLS comparison.
- **Clarity of writing**: Clear and well-organized. The modular UPM/MPM/PFM decomposition makes the method easy to follow.
- **Value to the research community**: High. The framework is portable (the paper explicitly claims this in Section 5), the gains are large and consistent, and the insight about using VLMs as label-independent priors is immediately applicable.

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>4</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>