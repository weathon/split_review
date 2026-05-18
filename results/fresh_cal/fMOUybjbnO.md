I've thoroughly verified the paper content against all reviewer claims. Here is my consolidated review.

---

## Summary

This paper introduces BAdd, a bias mitigation method that adds features capturing protected attributes to the model's penultimate-layer representation during training and then fine-tunes the classification head without those features at inference. The core insight — that adding bias features stabilizes training by preventing the loss spikes that otherwise trap vanilla models in a vicious cycle of biased representations — is well-motivated through gradient analysis and empirically validated. BAdd is evaluated across seven benchmarks covering both single-attribute and multi-attribute bias scenarios, achieving particularly strong results on the challenging multi-attribute benchmarks FB-Biased-MNIST (+27.5% absolute accuracy at q=0.99) and CelebA (+5.5% absolute accuracy on the HeavyMakeup bias-conflicting group).

## Strengths

1. **Large, well-documented gains on multi-attribute bias benchmarks where existing methods collapse.** On FB-Biased-MNIST (Table 5), BAdd achieves 69.5% accuracy at q=0.99 versus 42.0% for the best competitor (FairKL) — a margin far exceeding typical single-attribute improvements. On real-world CelebA (Table 7), BAdd achieves 92.7% on HeavyMakeup bias-conflicting samples versus 87.2% for the next-best method (FLAC). These results directly support the paper's central claim that BAdd is effective precisely where prior art struggles.

2. **Causal analysis of the bias mitigation mechanism.** Section 3.2 provides a formal derivation (Eq. 4) showing how vanilla training produces loss spikes that trap the model in biased solutions, and Figure 1 empirically demonstrates that BAdd eliminates those spikes. This goes beyond comparing numbers to explain *why* adding bias features works.

3. **Quantitative evidence of representation invariance.** Table 2 shows BAdd maintains mean pairwise cosine similarity above 0.97 across all background-color variations of Biased-MNIST test samples at q=0.999, versus 0.416 for vanilla. This directly measures the fairness property BAdd claims to achieve.

4. **Ablations that validate specific design choices.** Addition of bias features (98.1%) strongly outperforms concatenation (91.5%) at q=0.99 (Table 8), and the penultimate layer yields best results (Table 9). These experiments distinguish BAdd from naive alternatives and justify the architecture.

5. **Consistent strong performance across all seven benchmarks with a single method.** BAdd ranks first or tied for first on Biased-MNIST (all q), Biased-UTKFace (both protected attributes), Corrupted-CIFAR10 (all q), Waterbirds (WG accuracy tied), and both multi-attribute benchmarks, using the same approach without per-dataset tuning of the core mechanism.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **UrbanCars gap metrics reported without absolute subgroup accuracies, complicating interpretation when I.D. Acc differs across methods.** The UrbanCars results (Table 7) report gaps relative to each method's In-Distribution Accuracy. Because BAdd has a lower I.D. Acc (91.0%) than LLE (96.7%), its gap values (-4.3 BG Gap, -1.6 CoObj Gap) are not directly comparable to LLE's (-2.1, -2.7) in terms of absolute performance. For example, LLE's absolute accuracy on the background-conflicting group (96.7 - 2.1 = 94.6%) is *higher* than BAdd's (91.0 - 4.3 = 86.7%), even though BAdd's BG Gap looks competitive. Importantly, the paper's own text is quite measured — it explicitly notes that LLE is the exception and requires heavy preprocessing — so the textual claims are not overblown. However, reporting only gaps without absolute subgroup accuracies makes the table less informative.

2. **The method's requirement to know *which* specific attributes are the biasing ones (not just to have labels) is under-discussed.** On CelebA, the authors run a vanilla classifier to identify WearingLipstick and HeavyMakeup as the top-two biasing attributes (Table 1). This is a sensible diagnostic, but the paper does not clarify whether this is an integral part of the BAdd pipeline or a separable preprocessing step. The conclusion lists only "access to protected attribute labels" as the limitation, but in practice, the user also needs to know *which* of the available attributes cause bias. This is a modest gap — the CelebA setup demonstrates a reasonable workaround — but the paper would benefit from explicitly discussing this nuance.

### Trivial
None.

## Nice-to-Haves

- Report absolute subgroup accuracies (or at least I.D. Acc alongside gaps) for UrbanCars to make the table self-contained.
- Clarify the attribute-selection diagnostic (Table 1) as either a recommended part of the pipeline or an optional one-time analysis.
- Include a brief discussion of computational overhead: the extra forward pass through the bias-capturing model is negligible for a regressor but could be nontrivial for a full classifier.
- If feasible, compare against multi-attribute–aware methods (OccamNets, LLE) on at least one additional multi-attribute benchmark beyond UrbanCars, given LLE's segmentation preprocessing requirement makes broad comparisons difficult.

## Removed Points

- **"BAdd effectively addresses both background and co-occurring object biases" overstatement claim (Harsh Critic Critical Issue 1).** This exact phrase does not appear in the paper. The paper's actual text (Section 5.2) states "most compared methods struggle to address both... the only exception is LLE" — an appropriately qualified claim that acknowledges LLE's better BG Gap. Removed because the criticism is directed at a claim the paper does not make. (The underlying metric concern is retained as Minor Weakness 1 with corrected framing.)
- **Missing comparison with OccamNets/LLE on more multi-attribute benchmarks.** The paper already includes LLE on UrbanCars, the most natural benchmark. The critic acknowledges that LLE requires object-segmentation preprocessing, making it impractical for CelebA. Moved to Nice-to-Have.
- **Fine-tuning procedure could hurt baselines.** The paper states (Section 4.3) that the classification head of *all* models is fine-tuned for 20 additional epochs. Since this is applied uniformly, it is a fair comparison condition, not a confound. Removed.
- **Missing appendix content, missing proofs, missing supplementary experiments.** These are artifacts of the PDF extraction pipeline; the original submission contains these sections. Removed per policy.

## Novel Insights

The two reviews largely converge on the same picture: BAdd is a simple, well-motivated method with strong empirical results, particularly on multi-attribute benchmarks, and the main points of critique revolve around presentation nuance on a single dataset (UrbanCars) and scope clarification. The harsh critic's framing of the UrbanCars gap metrics as potentially "misleading" overstates the problem — the paper's actual claims about UrbanCars are already qualified by acknowledging LLE as the exception. A more precise reading is that the paper would be strengthened by adding absolute subgroup accuracies to the table, but the current presentation does not constitute an evidential flaw. The strength finder's identification of the +27.5% and +5.5% absolute improvements as the most compelling evidence is well-supported and reflects the genuine novelty: existing methods collapse under multi-attribute bias, while BAdd handles it with a straightforward architectural modification.

## Suggestions

1. In the UrbanCars table, add columns for the absolute accuracy on each conflicting subgroup (computed as I.D. Acc + Gap), so readers can directly compare subgroup performance across methods without mental arithmetic.
2. Add a brief paragraph in or after Section 3.2 acknowledging that the method requires not just protected-attribute labels but also knowledge of which attributes are the dominant sources of bias, and note that Table 1 illustrates one practical way to identify these (running a vanilla classifier and measuring accuracy disparities).
3. Consider a short sentence on computational cost: the extra forward pass through b(·) is negligible when using a regressor from label embeddings, but could double the forward pass when using a full bias-classifier network.

## Score and Decision

This is a solid paper with a clear, well-motivated method, strong theoretical grounding (loss spike analysis), and impressive empirical results — particularly the large gains on multi-attribute benchmarks where existing methods struggle. The weaknesses are minor and easily addressable: the UrbanCars metric presentation can be clarified, and the scope assumptions can be more precisely stated. There are no fatal or major flaws.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>