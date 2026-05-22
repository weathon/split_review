Now I have enough calibration data. Let me write the final consolidated review.

## Summary

This paper identifies and theoretically characterizes the label-dependency problem in SSL—showing that pseudo label utility degrades with scarce/poor labeled data—and proposes CaPT, an asymmetric-modalities co-training framework that integrates CLIP into SSL via three modules: a unimodal prediction network (UPM), an adapter-tuned CLIP module (MPM), and a prediction fusion module (PFM) that uses entropy-based weighting to combine their pseudo labels. The method achieves state-of-the-art results across multiple SSL benchmarks, with particularly striking gains in the one-label-per-class regime (e.g., +21.38% on CIFAR-100, +9.33% top-1 on ImageNet with 10 labels/class), at only 8% additional memory and 11% additional time over FreeMatch.

## Strengths

- **Large and consistent empirical gains, especially under extreme label scarcity.** On CIFAR-100 with 1 label/class, CaPT achieves 82.51% vs. 61.13% for FreeMatch (Table 3). On ImageNet with 10 labels/class, CaPT outperforms RegMixMatch by 9.33% top-1 (Table 2). These margins are far larger than typical SSL improvements and directly demonstrate that the framework unlocks unlabeled data under near-absence of supervision.

- **Well-designed asymmetric-modalities co-training with clear motivation.** Figure 3 shows that CLIP's attention patterns (e.g., attending to the rooster's comb) diverge from those of pure-vision ViTs (which focus on eye/beak), while symmetric co-training of two ViTs yields homogeneous representations. This cross-modal complementarity is concretely visualized and grounds the claim that co-training CLIP with a unimodal network is more informative than prior symmetric approaches (CLS).

- **Thorough ablation study validates every design choice.** Table 6 shows measurable degradation when removing bidirectional flow (CaPT-Uni: -0.88% to -1.49%), feature-augmented consistency (-0.57% to -1.81%), and entropy-based weighting (-0.87% to -1.57%). The modular contribution of each component is established, not asserted.

- **Efficient integration with practical overhead.** CaPT adds only 8.00% memory and 11.18% training time over FreeMatch while improving accuracy by 6.23% (Table 4). The feature-level Mixup for CLIP avoids expensive high-resolution re-feeding, making the framework practical despite using two models.

- **Strong performance under domain shift on fine-grained benchmarks.** CaPT leads on 5/6 fine-grained datasets (Table 5), including Flowers102 (+14.48% over RegMixMatch with 1 label/class) and StanfordCars (+11.61% with 5 labels/class), demonstrating that the gains are not limited to standard benchmarks or datasets potentially seen in CLIP's training.

- **Theoretical diagnosis of SSL's label-dependency problem.** Theorem 1.1 formally bounds pseudo label error in terms of prototype bias B and sample size n_min, providing a clean analytic model for why SSL fails under extreme label scarcity.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Theorem 1.1 diagnoses the problem but does not explain why CaPT addresses it.** The theorem bounds pseudo label error in a prototype-based Gaussian-mixture model as a function of labeled data quality/quantity. The paper uses this to motivate *why* SSL fails, but derives no new bound for CaPT and provides no analytic argument that CLIP reduces B or increases the effective margin g/2 − r. The title's "Breaking the Label Dependency" implies a theoretical guarantee that is not formally delivered. The contribution stands on empirical grounds, but the theoretical framing over-promises relative to what is proven.

2. **No numerical comparison against the most directly related methods (DebiasPL, CLS).** The paper discusses DebiasPL (which also integrates CLIP into SSL) and CLS (co-training) conceptually in Section 2, but provides no direct experimental comparison on the same benchmarks. Given these are the closest prior works in spirit, a numerical comparison would clarify CaPT's incremental advantage beyond the conceptual discussion provided.

3. **Limited ImageNet evaluation at extreme low-label settings.** Despite strong claims about reducing label dependency, ImageNet experiments use 10 and 100 labels/class—settings that are not "extreme" by the paper's own standards (the most dramatic gains occur at 1–2 labels/class). Adding a 1- or 2-label-per-class experiment on a subsample of ImageNet would strengthen the scalability argument.

### Trivial
None.

## Nice-to-Haves

- **Analyze why CaPT fails on FGVCAircraft more concretely.** The paper notes CLIP's prior is weak on aircraft subtypes but does not analyze *why* (e.g., CLIP's text encoder may not distinguish fine-grained aircraft models). A brief analysis, perhaps using class descriptions rather than single class names, could suggest a concrete fix.
- **ImageNet with 1–2 labels/class** (as noted in Weakness 3 above) would further strengthen the extreme low-label claims.

## Removed Points

- *"No discussion of the prompt template used for CLIP class weights"* — The paper explicitly states "more details in Appendix H" (line 127). The appendix was stripped by the parser; this is not an author omission. **Reason: parser artifact.**
- *"CLIP dependency is an inherent weakness"* — The harsh critic's own text says this is "not a weakness" and the paper is "transparent about this." The strength finder also correctly treats this as a property, not a flaw. **Reason: mischaracterization of the reviewer's own assessment.**
- *Strength: "Importance of the problem"* type generic praise — Removed per filtering rules. Only concrete, evidence-backed strengths are kept above.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a short analysis connecting Theorem 1.1 to CaPT: even an informal argument that CLIP's zero-shot prior reduces effective prototype bias B would strengthen the theoretical framing.
2. Include a direct experimental comparison with DebiasPL (and ideally CLS) on the USB benchmark to quantify the advantage of CaPT's co-training approach.
3. Add extreme low-label ImageNet results (1 or 2 labels/class on ImageNet-100 or similar) to match the paper's strongest claims.

## Score and Decision

**Calibration summary:**

- **Round 1 bracket (5.5–7.0):** Weak anchors (avg 2.50–3.40) were clearly below CaPT. Middle anchors included SemiCLIP (5.80, Accept), cleaning label noise with CLIP (4.50, Reject), semi-supervised CLIP methods. Strong anchors (8.00) were pure-theory or top-venue papers measuring a different kind of contribution.
- **Round 2 narrowing:** SemiCLIP (avg 5.80) — similar domain (CLIP + SSL) but smaller gains (1.72–6.58%) and more incremental novelty. Image Clustering via rate reduction (avg 5.80) — strong empirical results but novelty questioned. Synergy/Diversity in CLIP (avg 6.25) — ensemble method with practical concerns. Understanding CLIP Transfer (avg 6.50) — theory paper. CaPT is empirically stronger than SemiCLIP and comparable to or slightly above the 6.25–6.50 anchors.
- **Final position:** The paper's empirical contributions (21.38% gains, comprehensive benchmarks, thorough ablations, practical efficiency) are stronger than the 5.80 anchors, and its method is more novel than the 6.25 ensembling paper. The main limitations (the theorem not explaining CaPT, missing DebiasPL comparison) are real but bounded. Score anchored at **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>