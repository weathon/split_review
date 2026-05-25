Now I have all the information needed. Let me compile the final authoritative review.

## Summary

The paper proposes CausalNovo, a model-agnostic framework that adds a causality-informed module to existing de novo peptide sequencing models. It identifies noise peaks using the theoretical spectrum from the ground-truth peptide, performs a replace-based perturbation to simulate causal intervention, and uses contrastive learning (independence principle) together with a masked representation (sufficiency/purification) to enforce independence from noise and sufficiency for prediction. Evaluations on three public datasets with three base models (CasaNovo, AdaNovo, π-HelixNovo) show consistent improvements in amino-acid, peptide, and PTM-level metrics, and the method is shown to be more robust when noise peaks are perturbed.

## Strengths

1. **Consistent and substantial gains across multiple models and datasets.** Tables 1–2 show that CausalNovo improves all three base models on all three datasets. Improvements include up to +14.2% in amino acid precision (AdaNovo on HC-PT) and up to +10.3% in peptide precision (CasaNovo on Nine-species, threshold 1), often surpassing recent methods like SearchNovo.

2. **Mechanistic evidence from attention analysis.** Table 7 directly confirms that CausalNovo shifts attention toward causal fragment ions: the fraction of predictions attending to three causal peaks rises from 19.26% to 32.87%, while those attending to zero causal peaks drop from 12.73% to 10.76%. This provides evidence that the framework achieves its stated goal of focusing on signal peaks.

3. **Robustness to noise demonstrated across multiple analyses.** Figures 1, 3, and 4 show that CausalNovo-enhanced models degrade less than baselines when noise peaks are perturbed, with relative improvements averaging 14.9%–15.7% on HC-PT, and maintain higher amino acid precision across varying Noise-Signal Ratios (gains of +10.2% to +12.0%).

4. **Comprehensive ablation studies.** Table 4 isolates the contribution of each learning objective (independence, purification, symmetric training), and Table 5 ablates components of the causal intervention (replace, enhance, drop), showing each contributes positively.

## Weaknesses

### Fatal
None.

### Major

1. **Missing controlled baseline to attribute gains to the causal mechanism vs. data augmentation.** The method uses a replace-based perturbation (intervention) that generates additional training examples. The paper does not include a control where the *base model* (without the Causality Extraction Module, without contrastive/independence loss, and without purification loss) is trained on the same set of perturbed spectra. Table 5 ablates components *within the full CausalNovo framework*, but it does not answer: does the base model itself improve when simply given the same augmented data as extra training examples?

   Since the perturbation already uses the ground-truth label to identify noise peaks (theoretical spectrum), it provides a strong inductive bias. Without this control, a skeptic can argue that all observed gains come from the data augmentation, not from the causal representation learning objectives. The reported improvements from the independence and purification components (+1.2% and +0.8% in Table 4) are measured *on top of a framework that already includes the augmentation*; we do not know what fraction of the total +2.4% over baseline would be achieved by augmentation alone.

2. **The theoretical justification of the purification (auxiliary) objective is unclear and internally under-explained.** Section 3.3 writes: "However, it can reduce I(z_s; Y). To address this issue, we introduce an auxiliary objective that maximizes I(z_s; Y) which can indirectly lead to the purification of z_c." The paper does not explain the *mechanism* by which maximizing I(z_s;Y) purifies z_c. If the decoder can use both z_c and z_s during training (both are supervised with cross-entropy loss, Eq. 6), then putting predictive information into z_s could reduce the incentive for z_c to contain all necessary information, working *against* purification rather than toward it. The reference to Chen et al. (2022) is cited but not unpacked. This is not a minor clarity issue—it concerns the coherence of a central component of the claimed theoretical contribution. The causal framing is weakened when a core loss is not properly motivated.

### Minor

3. **No variance or statistical significance information.** Reported improvements are often 1–3% absolute in amino acid precision (Tables 1–2). No confidence intervals, standard deviations, or multiple-run statistics are provided. While single-run evaluation on held-out test sets is common in this field, the modest margins and baseline retraining discrepancies (e.g., CasaNovo 0.697→0.741) make variance information important for assessing stability. Some comparisons (e.g., π-HelixNovo 0.765† vs. +CausalNovo 0.787 on Nine-species) could benefit from error bars.

4. **Hyperparameters α and γ not specified in the main text.** The fraction of replaced noise peaks (α) and the m/z tolerance threshold (γ) are introduced in Section 3.4.1 but their numeric values are not given. The appendix (stripped) may contain them, but the main paper should at least reference an appendix section clearly.

5. **Cross-species validation only with CasaNovo.** Table 3 provides leave-one-out cross-species results only for CasaNovo. The claim of model-agnostic generalization across biological conditions would be strengthened by analogous results with AdaNovo and π-HelixNovo. (The paper mentions Appendix Table 8 for Seven-species, but again with CasaNovo only.)

### Trivial
None.

## Nice-to-Haves

- A comparison with simple robustness baselines (random noise injection, peak dropout, adversarial perturbations on the spectrum) would help contextualize the benefits of the causal approach.
- Demonstrating the framework on a non-Transformer model (e.g., DeepNovo or a convolutional architecture) would strengthen the model-agnosticism claim, though the three Transformer-based models already show breadth.
- Reporting parameter count of the CEM and the latency increase (beyond the stated "<1% inference overhead") would be informative.

## Removed Points

The following points were raised by reviewers but moved here after verification against the paper:

- **"Retrained baselines differ considerably from original publications"** — The paper marks retrained baselines with † and uses them as direct comparators. This is standard practice; the discrepancy is acknowledged by the notation. The comparison with CausalNovo is against these retrained baselines, which is fair.
- **"Table labels ambiguous"** — Table 5's caption ("Ablation study on the causal intervention") and the surrounding text (Section 4.4, "Ablating the Causal Intervention") clearly indicate these are components of the intervention within the full framework. The rows show different intervention configurations.
- **"Missing comparison with other robust training techniques"** — Moved to Nice-to-Haves. Not a core weakness; the paper already compares against many SOTA methods.
- **"Model agnosticism requires non-Transformer test"** — Moved to Nice-to-Haves. Three Transformer-based models provide reasonable breadth.
- **"Inference cost analysis insufficient"** — The paper reports <1% inference overhead. This is adequate for the stated claims.
- **Strength Finder's generic strengths** (e.g., "addresses an important problem", "clear writing") — These are filtered per the filtering rules as they are not tied to specific evidence in the paper, or are baseline expectations.

## Novel Insights

Beyond the paper's own contributions, the key tension that emerges from the review is this: the paper's strongest evidence is its *mechanistic* analysis (attention shifts toward causal peaks, differential robustness to perturbation), not its aggregate performance numbers. If the authors reframed their contribution around the mechanistic finding ("we can demonstrably shift model attention toward causal fragment ions, and this yields robustness benefits"), the missing augmentation control becomes less critical. Currently, the paper pitches itself as a causal framework with a theoretically motivated objective, but the theory is shaky and the attribution is confounded. The most compelling takeaway—that causal attention shift is measurable and beneficial—is buried in Section 4.4.

## Suggestions

1. **Add the missing augmentation control.** Train the base model (CasaNovo) on the same set of replace+enhance perturbed spectra, *without* the CEM and without the contrastive/independence and purification losses. Report whether the gains of the full CausalNovo are additive beyond this baseline. This single experiment would either strongly validate the framework (if the causal module adds significant value) or reveal that augmentation explains most of the gains.

2. **Clarify or reframe the purification objective.** Either provide (a) a rigorous derivation or intuitive explanation of why maximizing I(z_s;Y) purifies z_c, citing the specific mechanism from Chen et al. 2022, or (b) reframe this component as an empirical regularization technique and de-emphasize the causal narrative around it.

3. **Add variance information.** Report means and standard deviations over at least 3 independent runs for the main results (Tables 1, 2), especially for comparisons where margins are small.

4. **Specify α and γ in the main paper** (or provide explicit cross-references to the appendix section containing them).

## Score and Decision

**Calibration anchors used** (all retrieved across rounds 1 and 2):

| Anchor | Avg Score | Round/Query | Comparison |
|--------|-----------|-------------|------------|
| uQnvYP7yX9 (ReNovo) | 6.50 | R1-topic-mid | Retrieval-augmented de novo sequencing, accepted. Cleaner methodology but missing comparisons. CausalNovo has broader evaluation but more fundamental issues. |
| 87B3zDRMjv (RankNovo) | 5.50 | R1-topic-mid, R2 | Reranking framework, rejected. Clear methodology, modest gains. CausalNovo has larger gains but less clear theoretical foundations. |
| I2ZYngkRW6 (Distilling NAT) | 4.25 | R1-topic-mid, R2 | Knowledge distillation, rejected. Criticized as limited novelty. CausalNovo has more novel framing and broader evaluation. |
| 78tc3EiUrN (MADGEN) | 6.00 | R1-topic-mid | Mass spec molecular generation. Less directly comparable (molecules, not peptides). |
| IZiKBis0AA | 3.00 | R1-topic-low | Antibiotic drug design. Fundamentally different task and evaluation. |
| 1S8ndwxMts | 3.00 | R1-topic-low | Protein generative model evaluation. Different scope. |

**Round-1 bracket:** 4.0–6.0, based on comparison to ReNovo (6.5) at the top and Distilling NAT (4.25) at the bottom.

**Round-2 narrowing:** Queried inside (4.0, 6.5) and (4.5, 7.0). No new anchors changed the bracket; the most informative comparators remain ReNovo, RankNovo, and Distilling NAT.

**What the low-band anchors failed at:** Papers scoring 2.6–3.0 had fundamental unsoundness (evaluation doesn't support claims, methods don't work as stated). CausalNovo does *not* share these failures—the method consistently improves results and the evaluation is thorough in breadth. It is clearly above this band.

**Why the score is 5.0, not higher:** ReNovo (6.5) had missing comparisons but a clean, well-motivated method. CausalNovo's two Major weaknesses—missing attribution control and unclear theoretical justification—are more central to the paper's contribution. RankNovo (5.5) was rejected despite clear methodology; CausalNovo has stronger empirical breadth but weaker theoretical grounding. The missing control prevents full confidence in the causal attribution claim.

**Score: 5.0 — Below the acceptance threshold for top venues. The paper has clear empirical merit and a genuinely interesting approach, but two Major weaknesses (uncontrolled confound in the experimental attribution, unclear theoretical justification of a core component) must be resolved before the contribution can be assessed as solid.**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>