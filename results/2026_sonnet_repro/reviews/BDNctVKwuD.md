Now let me do calibration search to properly score this paper.Now let me read two key anchors in full to calibrate precisely.Now I have enough information to write the comprehensive final review.

---

## Summary

This paper addresses two intertwined problems: (1) a theoretical limitation of HiResCAM explanations arising from softmax's shift invariance—whereby HiResCAM maps are not uniquely determined and admit an arbitrary common spatial shift M without altering predicted probabilities—and (2) a training loss, Core-Focused Cross-Entropy (CFCE), that leverages ContrastiveCAMs to penalize model reliance on non-core image regions. ContrastiveCAMs (class-versus-class differences of HiResCAMs) are proven M-invariant and are used both as improved explanations and as a structural device to decompose the cross-entropy loss into core and non-core contributions. Experiments on Hard-ImageNet, Oxford-IIIT Pets, and PASCAL VOC show that CFCE-trained models dramatically concentrate attention on core regions, with large improvements in alignment metrics at some cost to raw classification accuracy.

---

## Strengths

- **Theorem 3.2 identifies a concrete, non-trivial failure mode of HiResCAM**: The theorem proves that for any trained network, the full HiResCAM tensor can be perturbed by an arbitrary matrix M shared across all classes without changing the softmax prediction. Figure 1 illustrates this with a concrete numerical example where a 4×4 matrix M changes the logit vector from [4, 0] to [16, 12] while preserving the identical probability output [0.98, 0.02], making the severity tangible.

- **Theorem 4.6 establishes classification-calibration of CFCE**: The proof that minimizing RCFCE risk implies convergence to the Bayes-optimal predictor under the Core-Constrained Risk Minimization framework (Eq. 16) gives CFCE a principled theoretical foundation beyond heuristic motivation.

- **Hard-ImageNet results are large and consistent across ablation types**: Table 2 shows CFCE drops accuracy under gray-mask ablation from 75.94% (CE) to 41.78%, under gray-bbox from 69.39% to 31.66%, and under tiling from 67.38% to 34.31%, while achieving ContrastiveCAM IoU of 89.22% vs. 30.27% for CE w/ Arch. These are large, consistent differences that strongly support the central alignment claim.

- **Practical applicability with weak supervision**: Table 3 demonstrates that CFCE with SAM auto-generated masks achieves binary validation IoU of 83.54% and multiclass 85.16%, competitive with ground-truth mask results (82.92% / 88.16%), confirming the method is usable when precise annotations are unavailable.

- **Downstream segmentation benefit**: Figure 4 shows CFCE+KL-pretrained backbones yield higher per-class segmentation IoU on PASCAL VOC than CE-pretrained backbones across most of the 20 classes, in both fine-tuned and end-to-end settings—evidence that learned alignment transfers to related tasks.

---

## Weaknesses

### Fatal
None.

### Major

- **Accuracy-alignment trade-off is underanalyzed**: On Hard-ImageNet (Table 2), CFCE drops accuracy from 94.25% to 90.53% (~3.7 pp). The paper's caption acknowledges "some un-ablated performance" cost but provides no analysis: there is no discussion of whether the drop is acceptable in context, whether it closes with more data or longer training, or whether CFCE-trained models actually generalize better OOD (where alignment is supposed to help). On Oxford-IIIT Pets (Table 3), multiclass accuracy also falls consistently: CE baseline is 94.41%, CE w/ Arch is 95.5%, CFCE is 92.96%, CFCE+KL is 90.08%. The cost is real and present across all datasets; leaving it unanalyzed weakens the argument that CFCE is a practical replacement for cross-entropy rather than a niche alignment tool.

- **Inaccurate "pareto improvement" claim for PASCAL VOC** (Section 5.3): The paper states "We report a pareto improvement with increased Average Precision (AP) and Intersection-over-Union (IoU) scores when using core-focused loss formulations." Table 4 contradicts this for CFBCE+KL: it achieves 87.19% validation AP versus CE w/ Arch's 88.85% AP—*lower* AP despite higher IoU. The pareto improvement holds only for CFBCE (88.39% AP vs. 87.32% CE baseline), not for the regularized variant. This is a verifiable factual overclaim that should be corrected.

### Minor

- **ContrastiveCAMs as an explanation tool lack independent quantitative validation**: The paper claims ContrastiveCAMs provide "more faithful attention maps" (Abstract), but faithfulness of the explanation method itself is only evaluated through proxy metrics (γ ratio in Table 1, qualitative Figure 2). No pointing-game accuracy, insertion/deletion, or ROAR-style perturbation test is applied to a frozen CE-trained model comparing HiResCAM vs. ContrastiveCAM. As a result, the claim that ContrastiveCAMs are *better explanations* (independent of training objective) is asserted more than demonstrated. Crucially, in Table 2, ContrastiveCAM IoU is only reported for CFCE-trained models (baseline rows show "—"), making it impossible to isolate the explanation method's quality from the training objective's quality.

- **Anomalous CE w/ Arch IoU in binary Pets setting (Table 3)**: CE w/ Arch achieves binary validation IoU of 39.07% (with a massive 16.98% standard deviation) compared to 78.37% for standard CE. This counterintuitive result—adding interpretability-motivated architectural modifications *hurts* alignment substantially—is never explained. The reader cannot assess this without understanding what "Arch" modifications entail for binary vs. multiclass performance.

- **Proposition 4.2 requires zeroing the bias vector b**: The paper states "b := 0 for h only" to exactly dissociate core/non-core contributions. This is a non-trivial architectural constraint enabling the theoretical decomposition in Eq. (12)–(13). No ablation is presented showing what happens when the bias is retained, leaving unclear whether the method degrades gracefully if this constraint is violated in practice.

### Trivial

- The regularized CFCE (Definition 4.7, Eq. 18) introduces three hyperparameters (λ₁, λ₂, λ₃) with no sensitivity analysis reported.

---

## Nice-to-Haves

- An out-of-distribution generalization experiment (e.g., background-swapped test sets, ImageNet-C corruptions) would directly demonstrate whether CFCE's alignment improvement translates to better robustness, which is the core motivation from the shortcut-learning literature.
- A direct ContrastiveCAM faithfulness experiment on CE-trained models (e.g., pointing game on Hard-ImageNet held-out set) would cleanly decouple the explanation method's quality from the CFCE training objective.
- A brief ablation over λ₁, λ₂, λ₃ in the KL regularization term would establish that the performance gains are not fragile to hyperparameter choice.
- An analysis of the γ redundancy metric's practical implications: does higher γ correlate with more misleading explanations, or does it not matter at typical γ values (0.2–0.37)?

---

## Removed Points

*These points were flagged for removal — treat with caution.*

- **"M-shift is overstated as a practical threat" (Harsh Critic)**: The critic argues that for a fixed trained network there is a single deterministic HiResCAM, so M only corrupts when comparing across networks or when reading absolute magnitudes. This is technically correct, but the paper's actual claim is about reading absolute spatial contributions as meaningful quantities (the standard use case for HiResCAMs). Figure 1 demonstrates this concretely. The limitation is not overstated as much as the critic claims; the framing is defensible. *Removed as a standalone weakness.*

- **"ContrastiveCAM M-invariance is trivial once Theorem 3.2 is accepted"** (Harsh Critic): While the mathematical step (subtraction cancels the common M) is indeed simple, establishing the formal invariance result (Theorem 3.5) and connecting it to Proposition 4.1 (Correctness of ContrastiveCAMs, Eq. 11) are necessary to ground CFCE. Triviality of a proof step does not invalidate the contribution. *Removed.*

- **"Comparison with CORM and DFR is unfair"** (Harsh Critic): The hard rule removes unfair-comparison criticisms when the asymmetry favors the baseline. CORM and DFR have better accuracy but worse alignment; CFCE has better alignment at worse accuracy. This is an accuracy-alignment trade-off, not an unfair comparison—and the paper correctly notes "models trained using our proposed core-focused loss functions show significant improvement across all evaluations, at the cost of some un-ablated performance." *Removed as an unfairness criticism; the accuracy cost is captured in the Major weakness above.*

- **Strength: "Class-versus-class granularity reveals model behavior hidden by single-class explanations"** (Strength Finder): The evidence is qualitative only (Figure 2). Without a quantitative evaluation of the richer information, this is a plausible but unverified claim for the explanation method specifically. *Removed as a standalone strength; merged into the ContrastiveCAM validation weakness.*

---

## Novel Insights

The paper's most genuinely novel observation is the connection from softmax shift-invariance (Proposition 3.1, a known property) to the non-uniqueness of spatially-resolved HiResCAM maps (Theorem 3.2), and then the direct use of this non-uniqueness as a *design opportunity*: the same algebraic cancellation that removes the spurious M also yields class-contrastive maps that separate core from non-core region contributions within the cross-entropy loss (Proposition 4.2). This chain—from a known softmax property, through a formal interpretability limitation, to a principled training correction—is a clean and underexplored path in the feature-alignment literature. The practical demonstration that this chain works even with automatically generated (SAM) or coarse (bounding box) masks, and that it transfers to downstream segmentation, substantially extends the scope of the observation beyond the theoretical result.

---

## Suggestions

1. **Add OOD evaluation**: Test CFCE-trained models on synthetically corrupted or background-swapped test sets to show alignment improvements translate to actual robustness gains — this is the strongest argument for CFCE as a practical alternative to CE.
2. **Correct the pareto improvement claim**: Restrict the claim to CFBCE (without KL) vs. CE baseline on PASCAL VOC, or acknowledge that CFBCE+KL trades AP for IoU.
3. **Report ContrastiveCAM IoU for CE-trained baseline models**: Computing this for CE and CE w/ Arch rows in Table 2 would directly test whether ContrastiveCAMs better expose alignment for any model, independent of training objective.
4. **Analyze the CE w/ Arch binary IoU anomaly**: Explain why adding the architectural modifications reduces binary alignment from 78.37% to 39.07% on Oxford Pets.
5. **Brief hyperparameter sensitivity table**: Report CFCE+KL results under a few λ configurations to establish robustness of the best result.

---

## Score and Decision

**Calibration anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| WYsLU5TEEo.md | 2.50 | R1 (weak) | Much weaker — GAN-based counterfactual classifier, thin theory, rejected |
| HXwrppoSPc.md | 3.25 | R1 (weak) | Weaker — prototype explanations, less rigorous, rejected |
| 6u6GjS0vKZ.md | 4.25 | R1 (mid) | Weaker — activation hue regularization, modest gains, rejected |
| T7q5LBGISH.md | 5.25 | R1 (mid) | Comparable-to-slightly-weaker — saliency smoothing, narrower contribution, rejected |
| x9rtYetTsA.md | 4.60 | R2 | Weaker — spurious bias mitigation via last-layer retraining, weaker theory, rejected |
| rJKlmCpOQ7.md | 5.20 | R2 | Slightly weaker — shortcut learning via MTL, comparable scope, rejected |
| W0zgCR6FIE.md | 5.75 | R2 | Comparable — spurious correlation benchmark, less theory, rejected |
| bkdWThqE6q.md | 6.00 | R2 | Slightly stronger — interpretable transformer, accepted; cleaner contribution, less accuracy trade-off |
| OZWHYyfPwY.md | 7.00 | R1 (strong) | Clearly stronger — critiques feature visualization with adversarial circuits, broader impact |
| S5yOuNfSA0.md | 6.50 | R2 | Stronger — CLIP theory paper, more complete |
| kbjJ9ZOakb.md | 8.00 | R1 (strong) | Much stronger — neuroscience + ML alignment paper, high-quality theory and experiments |

**Round 1 bracket:** 4.5–6.5

**Round 2 narrowing:** The paper is clearly above 4.60 (LaSAR) and 5.20 (multi-shortcut MTL) — it has broader theoretical coverage and more convincing empirical evidence. It sits close to the 5.75 (Spawrious benchmark) range, being comparably novel but more theoretically grounded. It is somewhat weaker than the 6.00 accepted "Simple Interpretable Transformer" because that paper is cleaner in scope and avoids the accuracy degradation and overclaiming present here. The inaccurate pareto improvement claim, the underanalyzed accuracy cost (~3.7 pp on Hard-ImageNet, consistent drops on Pets/VOC), and the absence of a standalone ContrastiveCAM faithfulness benchmark keep it below the 6.0 threshold.

**Final score: 5.5** — The paper makes a real theoretical contribution and has strong empirical evidence for its core alignment claim on Hard-ImageNet, but the systematic accuracy cost is insufficiently analyzed, one claim is verifiably inaccurate, and the paper's secondary claim (ContrastiveCAMs are better explanations) is not independently validated. The work is interesting and largely sound, but requires targeted revisions before it reaches the quality of accepted papers in this range.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>