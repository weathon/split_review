Now I have all the information needed. Let me write the final consolidated review.

---

## Summary

This paper introduces Sparling, a technique for learning intermediate representations with extremely sparse activations (>99.9% sparsity) from only end-to-end supervision. The method combines a spatial sparsity layer (thresholded ReLU with quantile-based threshold tracking) with an adaptive annealing algorithm that gradually reduces the target density based on validation accuracy. The paper demonstrates on three synthetic domains (DigitCircle, LaTeXOCR, AudioMNIST) that Sparling recovers ground-truth motifs with high accuracy despite never seeing motif labels during training, achieving density levels (0.005%) that L1 and KL-regularization baselines cannot match without catastrophic accuracy loss.

## Strengths

1. **Novel method that demonstrably works.** Sparling's spatial sparsity layer + adaptive annealing is a well-designed approach to a hard optimization problem. The results convincingly show it achieves extreme sparsity (99.995% on DigitCircle) while recovering motifs with CE ≈ 1% — a substantial advance over L1 and KL baselines which either cannot reach comparable sparsity or suffer >70% end-to-end error (Table 1). The ablation study (Section 5.2) cleanly validates that both batch normalization and the annealing schedule are essential design choices.

2. **Results replicate across three domains with different characteristics.** The method works on computer vision (DigitCircle, LaTeXOCR) and audio (AudioMNIST), with the AudioMNIST experiment including generalization to unseen speakers (Speakers 52-60). The LaTeXOCR case is particularly informative: the method correctly fails to recognize fraction bars and parentheses when they are not needed for the end task (line 240), which provides indirect evidence that the method genuinely identifies *necessary* structure rather than memorizing spurious patterns.

3. **Retraining analysis demonstrates the accuracy-sparsity tradeoff is manageable.** The paper shows that freezing the learned motif layer and retraining only the downstream model recovers most of the end-to-end accuracy gap relative to a non-sparse baseline (Figure 7). This is an important practical contribution: it shows that the extreme sparsity constraint does not fundamentally compromise task performance.

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparison with hard sparsity baselines.** The paper compares only against L1 and KL-divergence penalties — both of which are *soft* sparsity methods known to struggle at high sparsity. The most natural competitor to Sparling's spatial sparsity layer would be a hard sparsity mechanism such as top-k activation (retaining only the top k values per channel) or a hard concrete relaxation. The paper itself cites Bizopoulos & Paschalis (2020) as using "a quantile-based activation limit equivalent to both of our ablations combined" (line 65), but never directly compares against this or any other hard sparsity approach. Without this comparison, the paper cannot fully substantiate the claim that Sparling's specific combination of spatial sparsity + annealing is uniquely effective — it is possible that a simpler hard sparsity baseline (e.g., top-k with a similarly annealed k) would achieve comparable results. This is the most significant gap in the evaluation.

2. **The "necessity of extreme sparsity" claim is supported by a single training trajectory.** Figure 6 plots error metrics vs. density for what appears to be one run. The paper states that "CE is often substantially higher for even a 2–3× increase in δ" (line 250), but provides no information about variance across seeds or multiple trajectories at fixed density values. Moreover, the x-axis is reversed to simulate training progression, which conflates changes in density with other training dynamics (e.g., model capacity, optimization state). The L1 baselines provide indirect support (at 0.023% density, motif recovery fails), but those models also have >70% end-to-end error, making it hard to isolate the effect of sparsity from general model collapse. Multiple trajectories tracking density-idle training or seed-level variance would strengthen this central claim considerably.

### Minor

3. **"Unachievable" claim is slightly overstated.** The abstract says Sparling "enforces levels of activation sparsity unachievable using other techniques" (line 6). In fact, L1 with λ=2 reaches 0.023% density — within the same order of magnitude as Sparling's 0.005% — and the paper's later text (line 33-34) correctly clarifies that other methods "either do not produce extreme sparsity or have accuracy below 50%." The abstract and conclusion (line 290) should be sharpened to reflect that the advantage is the *joint* optimization of extreme sparsity *and* accuracy, not sparsity per se.

4. **Motif identifiability claim is purely empirical with no theoretical foundation.** The paper explicitly acknowledges this ("This is an empirical claim, which we validate in our experiments," line 86), which is honest but limits depth. The central thesis — that sparsity + locality + necessity implies that ĝ recovers g* up to permutation — would be substantially strengthened by even a simple formal result (e.g., for linear g*, binary motifs, noiseless setting). The information bound derivation (Section 3.3) is too generic to serve this purpose, and it has a technical gap: the term η in the bound "$H(\mathcal M[i,c]) ≤ H(B(δ_{i,c})) + ηδ_{i,c}$" (line 132) is never defined, making this section incomplete.

5. **No hyperparameter sensitivity analysis for the adaptive sparsity algorithm.** The algorithm (Algorithm 1) requires setting M=2×10^5, B=10, d_T=10^{-7}, and δ_update=0.75. For a method whose core claim is that it "automatically tunes" sparsity (line 185-187), the brittleness of these choices matters. A single sentence acknowledging stability across seeds or showing results with perturbed values would suffice.

6. **Abstract's 98.84% accuracy claim lacks clear metric mapping in the results section.** The intro states "98.84% of the time on average (up to permutation)" (line 33), and the results report CE=1.16% for DigitCircle (Figure 4). The mapping is traceable (100% − CE) but should be explicitly stated — the abstract claim reads as an accuracy metric while CE is a confusion error metric with a specific definition. Similarly, the ">90% accuracy" headline claim in the abstract should be qualified with the observed seed-level variance visible in Figure 4's dot plots.

7. **Retrained vs. non-sparse comparison relies on visual inspection.** The paper asserts the retrained model "tends to perform similarly to or only slightly worse than the Non-Sparse setting" (line 283) based on Figure 7, which shows error bars but no numerical comparison. For LaTeXOCR and AudioMNIST, the difference in mean E2EE appears non-trivial. Explicit numbers or a statistical test would be cleaner.

### Trivial
- The batch normalization ablation (Section 5.2) reports end-to-end error but not motif metrics; if the model fails the end task (71% E2EE), motif metrics are likely meaningless — this should be stated explicitly.
- The confusion matrix merging of channels for LaTeXOCR (32 channels for ~13 symbols) raises a question about whether channels are reliably one-to-one with symbols or whether multiple channels per symbol are common; a figure showing raw channel assignments before merging would be informative.

## Nice-to-Haves
- A limitations section discussing when the assumptions (sparsity, locality, necessity) break down, and potential failure modes (e.g., overlapping motifs, non-sparse g*, noise distributions).
- A stress test on the synthetic domains: varying motif density, adding overlapping motifs, or introducing non-local dependencies in h* to probe where the method breaks.
- A formal argument (even for a simplified linear/binary case) that sparsity + locality + necessity implies identifiability up to permutation.
- Reporting a single "motif accuracy" number (e.g., percentage of test samples where all motifs are correctly localized and classified) alongside the decomposed error metrics.

## Removed Points

- **Criticism about domain generality (Critic Issue #5):** The critic asks for "real handwritten equations with unknown character positions" and "real multi-speaker audio without forced alignment." The paper explicitly describes these as synthetic domains with known ground truth — this is the correct methodology for a proof-of-concept paper establishing a technique. Demanding real-world deployment validation is scope creep and inappropriate for the paper's stated aims.

- **Request for VIB baseline comparison:** The critic asks for a variational information bottleneck comparison. VIB penalizes mutual information directly via a KL term, which is a fundamentally different mechanism from the sparsity-enforcing approach used here. The paper frames sparsity as an *information bottleneck* (connecting to mutual information bounds) but does not claim to implement a VIB. This comparison would be a different paper direction, not a missing baseline.

- **Generic requests for larger-scale evaluation / more models:** These are one-size-fits-all criticisms that do not engage with the paper's actual scope.

- **"Not yet released" / reproducibility concerns about cited references:** Removed per hard rules — the paper cites entities that exist.

## Novel Insights

The reviews surface an interesting tension that the paper does not fully address: the "necessity of extreme sparsity" claim (Figure 6) relies on a single training trajectory where density decreases over time alongside other optimization dynamics, making it hard to disentangle the causal effect of sparsity from the effect of continued training with a well-tuned annealing schedule. The L1 baselines at comparable density fail catastrophically (70%+ E2EE), but this failure could stem from L1's gradient dynamics rather than the density level itself. A clean experiment holding density fixed across multiple runs while varying only the mechanism (Sparling vs. top-k vs. L1) would be the most direct way to isolate whether Sparling's advantage is the *sparsity level achieved* or the *way it achieves and optimizes at that sparsity level*. The paper's current design conflates these two questions.

## Suggestions

1. **Add a hard sparsity baseline** — top-k activation with annealed k (or a fixed target density) is the most important missing comparison. This would isolate the contribution of Sparling's specific spatial sparsity + quantile tracking mechanism from the general concept of hard sparsity.

2. **Strengthen the "necessity of extreme sparsity" claim** by including multiple training trajectories at fixed density values (or seed-level variance for Figure 6), and by showing that the relationship between density and CE is not an artifact of the annealing schedule.

3. **Define η in the information bound** (Section 3.3) or remove the incomplete derivation. As written, the bound is not self-contained.

4. **Sharpen the abstract's phrasing** from "unachievable using other techniques" to something like "at levels of sparsity that existing techniques cannot reach while maintaining accuracy" to accurately reflect the paper's actual results.

5. **Report explicit numbers** for the retrained vs. non-sparse comparison (Figure 7) rather than relying on visual inspection.

6. **Add a limitations section** discussing the assumptions (sparsity, locality, necessity) and when they are expected to hold or fail.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>