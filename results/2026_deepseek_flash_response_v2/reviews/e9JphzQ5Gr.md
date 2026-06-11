Here is the final consolidated review:

---

## Summary

This paper proposes CaPT, an asymmetric-modalities co-training framework that integrates CLIP into semi-supervised learning (SSL). CaPT jointly trains a fully fine-tuned unimodal vision network and an adapter-tuned multimodal CLIP model, fusing their predictions via co-pseudo labels with entropy-based weighting. The paper also provides a theoretical bound on pseudo-label error under a prototype-based generative model. CaPT achieves state-of-the-art results across multiple SSL benchmarks, notably +21.38% on CIFAR-100 and +4.05% on EuroSAT under one-label-per-class.

## Strengths

1. **Novel asymmetric-modalities co-training design**: The paper identifies and empirically demonstrates (Figure 3) that co-training two pure-vision ViTs yields similar attention patterns regardless of initialization, whereas the CLIP + ViT asymmetric setup produces genuinely complementary attention (e.g., CLIP attends to the rooster's comb while pure-vision ViTs focus on eye/beak). This addresses the pattern-homogeneity bottleneck in prior co-training methods like CLS and is a concrete, well-motivated architectural insight.

2. **Dramatic empirical gains under extreme label scarcity**: Table 3 shows CaPT outperforms the second-best method by **21.38%** on CIFAR-100 (82.51% vs. 60.49%) and **4.05%** on EuroSAT (96.33% vs. 92.28%) under one-label-per-class. Table 1 shows consistent leadership across all 6 USB evaluation settings with low standard deviations across 3 seeds. These margins are large enough to clearly indicate a substantive improvement.

3. **Favorable efficiency profile**: Table 4 quantifies that CaPT adds only 8.00% memory (4676→5050 MiB) and 11.18% training time (0.0939→0.1044 sec/iter) over FreeMatch while improving accuracy by 6.23%, and uses *less* memory and time than RegMixMatch (6578 MiB, 0.1484 sec/iter) while outperforming it. This makes the practical adoption argument credible.

4. **Well-structured ablation study**: Table 6 systematically decomposes CaPT into five ablated variants (CaPT-Ada, CaPT-Deb, CaPT-Uni, only UPM, only MPM) plus two design choices (w/o feat aug., equal weights) on two datasets, quantifying each component's contribution. The ablation confirms that co-training (CaPT-Uni: -0.88% on CIFAR-100), adapter-tuning (CaPT-Ada: -16.40%), and backward information flow all matter.

5. **Validation on fine-grained datasets**: Table 5 tests on 6 fine-grained benchmarks where CLIP's zero-shot accuracy is low (e.g., 18.97% on FGVCAircraft), showing CaPT outperforms baselines on 5 of 6 datasets. This mitigates concerns that CaPT merely inherits CLIP's existing strengths on standard benchmarks.

## Weaknesses

### Major

1. **STL-10 anomaly unaddressed**: In Table 1, adapter-tuned CLIP alone achieves **96.86%** (4 labels/class) and **97.15%** (10 labels/class) on STL-10, while the full CaPT framework evaluated on the UPM network achieves only **96.07%** and **96.34%**. CLIP zero-shot is even higher at **97.18%**. The co-training framework produces a final output that *underperforms* a component that was trained alongside it. The paper does not comment on this discrepancy. If the adapter-tuned CLIP is the better model, the claim that "CaPT achieves X%" is incomplete — a practitioner could simply deploy the CLIP adapter. This needs explanation, and the evaluation protocol (always reporting UPM) needs justification.

2. **Missing error bars on headline results**: Tables 2 (ImageNet), 3 (one-label-per-class), and 5 (fine-grained datasets) report only point estimates with no variance information. The paper's most striking result — the 21.38% gap on CIFAR-100 in Table 3 — has no error bars, making it impossible to assess whether this margin is robust across random seeds. Since the paper runs 3 seeds for Table 1, the same should be done for these experiments.

### Minor

3. **No direct head-to-head comparison against DebiasPL**: The paper discusses DebiasPL conceptually and includes a CaPT-Deb ablation, but does not run DebiasPL's actual algorithm as a standalone baseline with reported numbers. The CaPT-Deb ablation disables *both* adapter-tuning AND the vision-model-to-CLIP backward flow, which goes beyond DebiasPL's setup. A direct comparison would clarify whether CaPT's gains come from the co-training framework itself or primarily from adding CLIP in any reasonable configuration.

4. **Theoretical result disconnected from the SSL method used**: Theorem 1.1 bounds the pseudo-label error of a *nearest-prototype classifier* under a prototype-based Gaussian-mixture model. Modern SSL methods (including CaPT's own UPM) use deep neural networks with consistency regularization, softmax-based pseudo-labeling, confidence thresholding, and strong data augmentation — none of which are captured by the nearest-prototype model. The bound provides useful intuition about label dependency, but it is not connected to the experimental setting and does not inform CaPT's design. The paper should explicitly acknowledge this gap rather than presenting the theorem as directly supporting the empirical claims.

5. **CLIP branch never sees strongly-augmented images**: The MPM module performs Mixup at the feature level (Eq. 9) rather than feeding strongly-augmented images through CLIP's encoder. This means the CLIP branch only processes weakly-augmented inputs and convex combinations of weak features, never actual strongly-augmented images. This is a meaningful departure from typical SSL consistency regularization and should be discussed as a design limitation.

6. **Thresholding strategy inherited without ablation**: CaPT uses FreeMatch's adaptive threshold to filter pseudo labels (stated in Section 4.1). The ablation does not test whether CaPT's improvements are additive to this specific choice; a simpler fixed-threshold baseline would clarify this.

### Trivial

None.

## Nice-to-Haves

- Report the better of the two branches (UPM or MPM) as an additional evaluation metric, or justify the exclusive choice of UPM.
- Demonstrate portability with a different VLM (e.g., SigLIP, EVA-CLIP) to support the framework-level generality claim made in the conclusion.
- Evaluate CaPT under more abundant label regimes (e.g., 400 labels/class on CIFAR-10) to show the framework does not hurt when labels are plentiful.

## Removed Points

The following points from the inputs were removed with justification:

1. **"Comparison is structurally unfair because CLIP brings 400M image-text pairs"** — This criticism mistakes the paper's contribution. The paper's core claim is about *integrating CLIP into SSL*. Comparing against pure SSL methods is the correct experiment to test whether CLIP helps. This comparison would be inappropriate only if the paper claimed to improve pure SSL without external data, which it does not.

2. **"No demonstration of portability"** — The paper states portability as a design goal and references Appendix L. Testing another VLM would strengthen the claim but is not a required weakness; filed as a nice-to-have.

3. **"Missing evaluation under abundant-label regimes"** — The paper's scope is explicitly low-label regimes (the title and abstract emphasize "breaking the label dependency"). Evaluating under abundant labels is outside the stated scope.

4. **"Theoretical result over-claimed/fatal"** — The disconnect is real and kept as Minor #4. However, the critic's characterization as "fatal" is excessive; the theorem is presented as motivational intuition, not as a design driver for CaPT, which is standard practice in ML papers.

5. **"CaPT-Deb is not equivalent to DebiasPL"** — This sub-point is absorbed into Minor #3 (missing direct DebiasPL baseline). The CaPT-Deb ablation remains informative even if not a perfect DebiasPL replication.

## Novel Insights

The most genuinely novel observation from the reviews is the STL-10 anomaly: the UPM output underperforms the adapter-tuned CLIP trained alongside it, revealing a tension in the evaluation protocol. If CaPT's final output is consistently worse than one of its components on a specific dataset, the paper should either explain why or offer the option of deploying the better branch. Beyond this, the asymmetric-modalities insight (Figure 3) is the paper's own genuine contribution and is well-supported by the attention map analysis.

None beyond the paper's own contributions.

## Suggestions

1. **Explain the STL-10 result** — On STL-10, CLIP zero-shot is already 97.18%, so the domain is near-solved by CLIP alone. This may explain why co-training adds little or even hurts (the UPM may learn noise from near-perfect CLIP predictions). Report the best of UPM/MPM or justify the UPM-only protocol.

2. **Add standard deviations** to Tables 2, 3, and 5 (3 seeds, as done for Table 1) so the 21.38% gap on CIFAR-100 can be assessed for robustness.

3. **Run a direct DebiasPL baseline** following its published algorithm, or at minimum clarify how CaPT-Deb differs from DebiasPL and why the comparison is valid.

4. **Acknowledge the theory–method gap** in Section 1 or 5: the theorem analyzes nearest-prototype classifiers under a Gaussian mixture, while CaPT uses deep networks with consistency regularization.

5. **Discuss the feature-level Mixup limitation** — that the CLIP branch never processes strongly-augmented images, only convex combinations of weak features.

6. **Ablate the thresholding choice** by comparing FreeMatch's adaptive threshold against a simple fixed threshold.


MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>