Now I have a clear picture. Let me write the final review.

**Round 1 Bracket:** [4.5, 6.5] — CaPT sits clearly above SelfPrompt (3.50) and WSL-PT (4.75), comparable to or slightly below SemiCLIP (5.80), and below PASLE (6.40).

**Round 2 Narrowing:** Within the bracket, CaPT is stronger than WSL Pre-Trained (4.75, rejected for writing/clarity issues) and slightly weaker than SemiCLIP (5.80, accepted but with novelty concerns). CaPT's framing overstatement and missing baseline are more structural concerns than SemiCLIP's incremental-novelty complaints. This places CaPT at approximately **5.0**.

---

## Summary
This paper identifies that SSL methods remain label-dependent — their ability to exploit unlabeled data collapses under extreme label scarcity — and proposes CaPT, an asymmetric-modalities co-training framework that jointly trains a fully fine-tuned unimodal network with an adapter-tuned CLIP model using entropy-weighted co-pseudo labels. CaPT achieves strong empirical results across multiple benchmarks, with particularly large gains in extremely low-label regimes.

## Strengths
- **Well-motivated problem with clear empirical evidence**: Figure 1 provides multi-faceted evidence (label quantity, quality, and unlabeled-data utility) that SSL methods degrade sharply when labeled data becomes scarce or non-prototypical — a genuinely underappreciated phenomenon that is carefully demonstrated.
- **Technically sound and well-ablated method design**: The three-module architecture (UPM, MPM, PFM) is clearly described. Table 6 systematically isolates each component: removing bidirectional flow, adapter-tuning, entropy weighting, and feature-augmented regularization all degrade performance, validating each design choice.
- **Broad and rigorous evaluation**: The paper evaluates across USB (3 datasets × 2 label settings, 12 baselines), ImageNet, extreme scarcity (1 label/class), and six fine-grained datasets with CaPT leading in the majority of settings. The resource comparison (Table 4) validates efficiency claims.
- **Honest acknowledgment of limitations**: The paper explicitly discusses where CaPT underperforms (FGVCAircraft, where CLIP's prior is weak) and frames this as a boundary condition rather than hiding it.

## Weaknesses

### Fatal
None.

### Major
- **Headline results overstate CaPT's architectural contribution**: The abstract highlights a 21.38% gain on CIFAR-100 at 1 label/class over the second-best method (FreeMatch). But FreeMatch does not use CLIP at all, so this gain largely reflects CLIP's pretraining rather than CaPT's co-training architecture. The paper's own ablation (Table 6) reveals more modest deltas: CaPT beats "only UPM" (FreeMatch, no CLIP) by 6.23 points, and the bidirectional co-training flow (CaPT vs. CaPT-Uni) accounts for only 0.88 points. The framing systematically conflates "having CLIP" with "having CaPT's architecture," inflating the perceived contribution. The abstract and introduction should lead with the architectural contribution rather than the CLIP-vs-no-CLIP gap.
- **Missing baseline: CLIP predictions used directly as pseudo-labels**: The most natural benchmark for CLIP integration is to generate pseudo-labels from an adapter-tuned CLIP and use them to train the unimodal network — without joint training, bidirectional flow, or entropy-weighted fusion. This would cleanly isolate whether the co-training mechanism adds value beyond simply having access to CLIP's predictions. The existing ablations (CaPT-Deb, CaPT-Uni, "only MPM") do not test this. This is a gap in the evidence for the paper's central claim that the full co-training framework is necessary.
- **Theorem 1.1 is disconnected from the proposed method**: The theorem bounds pseudo-label error under a Gaussian mixture model with a nearest-prototype classifier, showing that fewer/worse labeled samples increase error. While this formalizes the motivation, it provides no theoretical insight into CaPT — it does not involve CLIP, co-training, adapter-tuning, or any mechanism of the proposed framework. Since the paper lists "theoretically establish the label dependency" as its first contribution, this disconnect weakens the paper's intellectual coherence. The theorem supports the problem statement but not the solution.

### Minor
- **Cross-modal complementarity claim is underevidenced**: The paper argues that asymmetric modalities mitigate pattern-homogeneity (Figure 3), but severing the backward flow (CaPT-Uni) costs only 0.88% on CIFAR-100 (Table 6). There is no comparison against co-training two differently-pretrained unimodal networks, which would test whether the benefit comes from cross-modal complementarity or simply from having two diverse models.
- **STL-10 results complicate the narrative**: On STL-10, adapter-tuned CLIP standalone achieves 96.86–97.15% while CaPT's unimodal network achieves 96.07–96.34% (Table 1). The final unimodal network underperforms the standalone CLIP it was co-trained with, which goes undiscussed.
- **Standard deviations missing from Tables 2, 3, and 5**: Table 1 reports standard deviations across three seeds, but Tables 2 (ImageNet), 3 (1 label/class), and 5 (fine-grained) omit them. Given that label sampling variance matters greatly in low-label regimes, this is a notable omission.
- **No experimental comparison to CLS**: CLS (Yao et al., 2022) is the most directly comparable co-training method and is discussed in related work, but no numerical comparison is provided. Including CLS would ground the asymmetric-modalities claim.

### Trivial
- The confidence threshold for pseudo-label filtering (line 196) is described qualitatively; the exact threshold value is not stated in the main text.
- The CaPT-Ada ablation (Table 6) changes two design choices simultaneously (replaces UPM with CLIP-Adapter and removes MPM), making it hard to isolate which change drives the 16-point performance drop.

## Nice-to-Haves
- A decomposition analysis separating "CLIP pretraining gain" from "co-training architecture gain."
- An experiment co-training two differently-pretrained unimodal networks to test whether cross-modal complementarity drives the benefit.
- A clearer characterization of when CLIP's prior is too weak for CaPT to help (beyond FGVCAircraft).

## Removed Points
These points are flagged to be removed, treat them with caution:
- (From Harsh Critic) "No comparison to CLS is reported numerically" — kept as minor weakness since CLS is discussed in related work and is directly comparable.
- (From Harsh Critic) "The 'paradoxically and unexpectedly' language is rhetorical overreach" — removed as a stylistic nitpick; the paper is entitled to characterize its findings.
- (From Harsh Critic) "The paper does not discuss prior work on using pretrained models beyond CLIP as teachers in SSL" — removed per the rule against flagging missing related works.
- (From Harsh Critic) "FreeMatch already achieves near-saturation on EuroSAT (90.12%), a 6.21% improvement is also substantial" — the paper already explicitly notes this in footnote 3, so this is not a weakness.
- (From Harsh Critic) "Scaling behavior of resource costs is not discussed" — removed as generic; efficiency analysis demands scaling behavior in almost any paper.
- (From Strength Finder) "Principled theoretical motivation" — kept in spirit but acknowledged that the theorem is disconnected from the method; the theoretical contribution is motivation-only, not a contribution to the method's analysis.
- (From Strength Finder) Several strengths about the problem importance and targeting an interesting question — removed as generic/superficial.

## Novel Insights
None beyond the paper's own contributions. The empirical demonstration that SSL's gain from unlabeled data shrinks as labeled data quality/quantity degrades (Figure 1c) is genuinely interesting and well-executed, but it is the paper's own central observation rather than a meta-insight emerging from the review process.

## Suggestions
- **Add the CLIP-as-pseudo-labeler baseline**: Train the unimodal network using adapter-tuned CLIP's predictions as fixed pseudo-labels. This is the single highest-leverage experiment for validating the co-training claim.
- **Recalibrate the framing**: Lead with what CaPT's architecture contributes over simpler CLIP integration strategies (the 3–6 point co-training delta), not the CLIP-vs-no-CLIP gap. Revisit the abstract and introduction accordingly.
- **Either connect Theorem 1.1 to CaPT or demote it**: The theorem currently stands as motivation only. Either extend it to show how an external prior changes the bound, or reposition it as problem motivation rather than contribution #1.
- **Add CLS to the experimental comparison** and report standard deviations consistently across all result tables.
- **Discuss the STL-10 anomaly**: Why does CaPT's unimodal network underperform standalone adapter-tuned CLIP on STL-10? This is an important boundary case.

## Anchor Comparisons
- **SelfPrompt (3.50, Reject)**: Semi-supervised VLM prompt-tuning. CaPT is clearly stronger — cleaner method, more comprehensive evaluation, better ablation.
- **WSL Pre-Trained (4.75, Reject)**: CLIP for weakly supervised learning. CaPT is stronger — clearer method, broader evaluation, more significant results.
- **SemiCLIP (5.80, Accept)**: Semi-supervised CLIP training. CaPT is slightly weaker — SemiCLIP's weaknesses were about incremental novelty and evaluation scope, while CaPT's framing overstatement and missing baseline are more structural concerns about evidence for core claims.
- **PASLE (6.40, Accept)**: Test-time adaptation with pseudo-labels. CaPT is weaker — PASLE has stronger framing and more complete evidence.
- **Image Clustering (5.80, Accept)**: CLIP-based image clustering. Different problem but similar CLIP-leveraging theme. CaPT is slightly weaker due to framing issues.
- **VLM Selection (6.33, Reject)**: VLM selection and reuse. CaPT is weaker in framing coherence.
- **Label Noise Pre-training (6.25, Accept)**: CaPT is weaker — cleaner theoretical connection.
- **Black Sheep (7.00, Accept)**: CaPT is clearly weaker — stronger framing and theoretical grounding.

## Score and Decision
The paper addresses a genuine problem with a practical method and delivers strong empirical results. However, the framing systematically overstates the architectural contribution by conflating CLIP's pretraining gains with CaPT's co-training design, a critical baseline is missing, and the theoretical contribution is disconnected from the method. These are addressable but significant concerns that prevent acceptance in current form.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>