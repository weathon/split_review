Now I have all the evidence needed. Let me write the final consolidated review.

---

## Summary

This paper identifies that existing SSL methods are inherently label-dependent: their ability to exploit unlabeled data degrades when labeled data is too scarce or of low quality. To address this, the authors propose CaPT, an asymmetric-modalities co-training framework that integrates CLIP (adapter-tuned) as a prior teacher alongside a fully fine-tuned unimodal network. The two models exchange supervision through entropy-weighted co-pseudo labels, and feature-augmented consistency regularization maintains efficiency. CaPT demonstrates strong empirical results, notably a 21.38% absolute improvement on CIFAR-100 with one label per class.

## Strengths

- **Well-motivated problem identification.** The paper provides clear empirical evidence (Figure 1a–c) that SSL performance collapses under extreme label scarcity and that pseudo-label quality degrades with less prototypical labeled samples. Theorem 1.1, while operating in a simplified generative setting, usefully formalizes the intuition that label quality bounds pseudo-label quality. This problem diagnosis is the paper's strongest conceptual contribution.

- **Efficient and sensible architecture design.** CaPT's three-module design (UPM, MPM, PFM) cleanly decouples learning capacity (fully fine-tuned unimodal network) from prior knowledge (adapter-tuned CLIP). Feature-level Mixup (Section 3.2.2) avoids re-encoding high-resolution images through the frozen CLIP encoder. The entropy-based weighting scheme (Eq. 11–13) adaptively shifts supervision from CLIP (dominant early) to the unimodal network (dominant later) as training progresses. Table 4 confirms modest overhead: +8% memory, +11% time over FreeMatch.

- **Informative internal ablation.** Table 6 validates core design choices: CaPT outperforms its unidirectional variant (CaPT-Uni), the DebiasPL-style variant (CaPT-Deb), the adapter-only variant (CaPT-Ada), and single-module baselines. Removing feature augmentation or replacing entropy weighting with equal weights both degrade performance, confirming those mechanisms matter.

- **Strong empirical performance under label scarcity.** The 21.38% gain over RegMixMatch on CIFAR-100 with one label/class (Table 3) and consistent improvements across USB benchmarks (Table 1), ImageNet (Table 2), and most fine-grained datasets (Table 5) demonstrate that the CLIP-integrated approach substantially improves over SSL-only methods in low-label regimes.

## Weaknesses

### Fatal

None.

### Major

- **Comparison against non-CLIP baselines conflates CLIP's pretraining with the co-training framework's contribution.** The main experimental comparisons (Tables 1–3, 5) pit CaPT — which benefits from CLIP's 400M image-text pair pretraining — against SSL methods whose only external knowledge is ImageNet-pretrained ViT weights. The large gains in extreme low-label settings (e.g., +21.38% on CIFAR-100, 1 label/class) are therefore at least partially attributable to CLIP's prior rather than the co-training mechanism per se. While using CLIP as a prior is explicitly the paper's goal, the headline comparisons do not disentangle "CLIP is helpful" from "the CaPT co-training framework is uniquely effective at integrating CLIP." The paper would be strengthened if the main tables included a row where baselines also receive CLIP-generated pseudo-labels or use CLIP's visual encoder as a common backbone, isolating the co-training framework's added value.

- **Missing "static CLIP teacher" baseline in the ablation study.** Table 6 compares CaPT against CaPT-Deb (disables adapter tuning and vision→CLIP flow), CaPT-Uni (unidirectional CLIP→vision), and single-module variants. What is absent is a straightforward baseline where CLIP generates pseudo-labels (without fine-tuning or co-training) that directly supervise the unimodal network. This is the most natural way to assess whether the bidirectional co-training loop and adapter-tuning offer gains beyond simply distilling CLIP's predictions. CaPT-Deb approximates this but also alters the training procedure (adding CLIP-predicted samples to the labeled set), making it an imprecise control.

### Minor

- **Theorem 1.1 is loosely connected to the method.** The theorem bounds pseudo-label error under a Gaussian-mixture model with a nearest-prototype classifier — a setting that shares little with modern SSL (neural networks, consistency regularization, adaptive thresholding, self-training). It serves as conceptual motivation for why label dependency exists but provides no direct insight into why CaPT works or how to design it. The paper does not claim the theorem as a theoretical foundation for CaPT, so this is not fatal, but the disconnect between the theory and the method is noticeable.

- **No quantitative head-to-head comparison with CLS.** CLS (Yao et al., 2022) is the most directly comparable co-training method and is discussed qualitatively in the related work. A quantitative comparison — even if CLS does not use CLIP — would help readers assess whether the asymmetric-modalities design (CLIP + unimodal) yields gains beyond what symmetric co-training (two unimodal networks) provides under the same total parameter budget. The CLS co-training baseline with CLIP features could serve as an interesting intermediate point.

- **Pattern-homogeneity claim relies entirely on qualitative attention maps.** The argument that asymmetric modalities mitigate a "pattern-homogeneity bottleneck" (Section 3, Figure 3) is supported only by a handful of attention map visualizations showing different ViTs attending to similar regions while CLIP attends elsewhere. A quantitative metric (e.g., CKA similarity, mutual information, or pseudo-label agreement between co-trained unimodal ViTs vs. between UPM and MPM) would make this claim more persuasive. The paper acknowledges further experiments in Appendix B, but the main-text evidence is thin.

### Trivial

- **SVHN is listed among fine-grained benchmarks** (Table 5). SVHN (Street View House Numbers) is not a fine-grained dataset; its inclusion dilutes the fine-grained evaluation claim. The results remain valid since CaPT outperforms on all other datasets regardless, but the framing is imprecise.

- **Figure 1a includes CaPT in the motivating plot.** Showing the proposed method already solving the problem in the figure that motivates the problem's existence is a minor presentational circularity.

## Nice-to-Haves

- Replacing or supplementing Theorem 1.1 with an empirical analysis measuring how pseudo-label quality degrades under varying label quantity/quality across multiple SSL algorithms would connect more directly to the method.
- An analysis decomposing how much of CaPT's gain comes from CLIP's visual representations versus its textual knowledge (e.g., replacing the textual classifier with a learned linear classifier on frozen CLIP visual features).
- A quantitative metric for the pattern-homogeneity bottleneck (e.g., CKA between co-trained models' representations).

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Beta distribution parameters are not specified"* — This is a trivial implementation detail presumably in the appendix; does not affect the contribution.
- *"Backbone details for USB are not specified"* — The paper states (Section 4.1): "USB adopts the pre-trained ViTs as the training backbone. For fair comparison, our unimodal network uses the same training configuration and backbone as USB." This is sufficient.
- *"The one-label setting is where CLIP's zero-shot capability is most dominant, further highlighting the unfairness"* — This is subsumed by the Major weakness about comparison fairness and should not be double-counted as a separate concern.
- *"No comparison with DebiasPL"* — The paper includes CaPT-Deb in Table 6, which is a DebiasPL-style variant. The claim that "no quantitative head-to-head experiments are provided" is incorrect regarding DebiasPL.
- *"The theorem should not be presented as a theoretical foundation for the work"* — The paper presents Theorem 1.1 as motivation ("To complement these empirical observations, we present an analytic model and a supporting theorem"), not as a theoretical foundation for CaPT. This criticism overstates the paper's claims.
- *"Theoretical motivation is not relevant"* — While the connection is loose, using simplified models to illustrate a problem phenomenon is standard practice. The harsh critic's framing that this "should not be presented" is too strong.
- *"Entropy-based weighting stability with small batch sizes is not discussed"* — This is a speculative concern without evidence from the paper that stability is actually an issue. The critic is guessing at a potential problem.

## Novel Insights

The paper's identification that SSL's label dependency creates a paradoxical dynamic — as labeled supervision degrades, SSL paradoxically becomes *more* dependent on that failing supervision, and can cease to benefit from unlabeled data entirely — is a genuinely insightful reframing of why SSL fails in low-label regimes. The heatmap visualization in Figure 1c, showing accuracy gain from unlabeled data diminishing to near-zero as labeled data shrinks, makes this point crisply. This insight, rather than the specific co-training architecture, may be the paper's most lasting contribution.

## Suggestions

- Add a baseline where CLIP-generated pseudo-labels (from frozen CLIP, no adapter tuning) directly supervise the unimodal network. This is the most direct way to isolate the co-training mechanism's contribution.
- Consider including a row in the main comparison tables where at least one strong baseline (e.g., FreeMatch or RegMixMatch) is given access to CLIP features or CLIP pseudo-labels, to provide a fair resource-matched comparison.
- Replace or supplement the qualitative attention-map evidence for pattern homogeneity with a quantitative metric (e.g., CKA or pseudo-label agreement between co-trained unimodal ViTs vs. between UPM and MPM).

## Score and Decision

**Round 1 Bracketing:** Retrieved anchors in three bands — weak (2.33–3.33: multimodal CLIP papers with fundamental flaws), middle (4.25–5.80: CLIP-integration papers with mixed novelty/execution), and strong (8.00: polished, highly novel analysis contributions). Initial bracket: **4.5–6.5**.

**Round 2 Narrowing:** Retrieved anchors within the bracket: SemiCLIP (5.80, Accept — semi-supervised CLIP training), VLM Selection (6.33, Reject — novel VLM reuse framework), VL Dataset Distillation (5.50, Reject — first work on a new problem), BLG (4.67, Reject — CLIP for long-tail recognition), Clean Label Noise (4.50, Reject — CLIP for sample selection).

**Anchor comparison:**
- SemiCLIP (5.80): Most comparable. Both integrate CLIP into a training framework with strong results. SemiCLIP's evaluation was cleaner (isolated contribution better) but CaPT's empirical gains are more dramatic. CaPT's evaluation fairness concern pushes it below SemiCLIP.
- VL Dataset Distillation (5.50): First work on a new problem with solid experiments but questions about generalization of distilled data. CaPT is in a similar tier of contribution quality.
- BLG (4.67): Weaker novelty, high computational cost, performance tradeoffs. CaPT is clearly stronger.
- VLM Selection (6.33): More rigorous evaluation framing and novel problem. CaPT's evaluation weakness places it below this.

**Final score: 5.5.** The paper makes a genuine contribution — identifying SSL's label dependency and proposing a sensible CLIP-integration framework — but the evaluation does not adequately isolate the co-training mechanism's contribution from CLIP's pretraining advantage. The ablation study partially addresses this but the missing static-CLIP-teacher baseline and the headline comparisons against non-CLIP methods weaken the evidence for the paper's central claim about the co-training framework's unique value.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>