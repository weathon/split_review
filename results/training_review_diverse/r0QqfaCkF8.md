Now I have all the evidence I need. Let me construct the final review.

## Summary

The paper proposes Fragment-Augmented Diffusion (FADiff), which uses molecular fragmentation as a data augmentation strategy within torsional diffusion models for conformer generation. By decomposing molecules into chemically meaningful fragments (via BRICS/RECAP rules) and treating them as independent training examples, FADiff increases data diversity and captures local structural variations. The paper presents empirical results on GEOM-DRUGS and GEOM-XL showing consistent improvements over TorDiff and other baselines, with particularly large gains under data scarcity (e.g., 42% relative improvement in COV-R with 1,000 training samples).

## Strengths

- **Substantial gains in data-scarce regimes.** Table 3 shows that with only 1,000 training samples, FADiff achieves COV-R of 49.39% versus TorDiff's 34.70% (a 42% relative improvement), and this advantage persists across all tested sample sizes (5,000 and 10,000). This directly supports the paper's central claim of improving data efficiency via fragment augmentation.

- **Consistent improvements over strong baselines on standard benchmarks.** On GEOM-DRUGS (Table 1), FADiff achieves the best mean COV-R (70.07%), COV-P (52.87%), AMR-R (0.609 Å), and AMR-P (0.588 Å). On the large-molecule GEOM-XL set (Table 2), FADiff achieves the lowest mean AMR-R (1.80 Å) and AMR-P (2.60 Å), demonstrating generalization to molecules far larger than training examples.

- **Chemically informative ablation study.** Table 4 shows that removing BRICS edges primarily degrades precision (COV-P falls from 50.10% to 33.93%), while removing RECAP edges primarily degrades recall (COV-R drops from 51.17% to 49.38%). This provides actionable insight into how different chemical fragmentation rules contribute to generation quality.

- **Higher sampling efficiency for practical deployment.** Figure 3 shows FADiff achieves strong performance with as few as 10 reverse steps, maintaining an advantage over TorDiff across all step counts, which reduces computational cost.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Conformer matching attribution is ambiguous.** The paper states "we use conformer matching as a additional data augmentation technique" (Section 4.1) and cites Jing et al. (2022) as having shown its benefit. However, it does not explicitly state whether the TorDiff baseline numbers in Tables 1–3 were obtained under the same conformer-matching protocol or are taken from the original TorDiff paper (which also used conformer matching). Since both methods likely use conformer matching (TorDiff's original paper already did), this is not likely to be a fatal flaw, but the lack of explicit statement prevents full verification. The authors should clarify: "all torsional diffusion baselines, including TorDiff, use conformer matching, and the reported TorDiff numbers are [reproduced under the same protocol / from the original paper]."

- **Fragment-size threshold z is not specified.** Section 4.1 states "only fragments larger than z atoms are selected for augmentation" but never provides the numerical value of z. This is a simple omission that harms reproducibility and should be trivial to correct.

- **Results on GEOM-QM9 are listed as a dataset but never reported.** The experimental setup (Section 4.1) states the paper uses "GEOM-QM9, GEOM-DRUGS, and GEOM-XL," and the δ threshold for QM9 (0.5 Å) is specified, but no results table for QM9 appears in the paper. While the paper's focus is on larger molecules where fragment augmentation is most motivated, the omission is noticeable given QM9 is listed as part of the evaluation.

- **No ablation on κ (maximum fragmentation edges).** The method uses κ=5 exclusively. An ablation sweeping over different values of κ (e.g., 2, 5, 10) would help readers understand sensitivity to this hyperparameter and how fragment granularity affects performance.

- **Theoretical analysis is loosely connected to experiments.** Lemma 1 and the error analysis in Section 3.4 provide a conceptual framing (mutual information maximization, error variance bounds) but are never empirically tested—e.g., by estimating mutual information for different fragmentation strategies or connecting the derived bounds to observed performance. The ablation in Table 4 is presented without reference to the theoretical framework. The theory does not hurt the paper but does not carry weight in supporting the claims.

### Trivial

None.

## Nice-to-Haves

- **Confidence intervals or multi-seed results.** The paper reports all performance numbers as single values. While single-run evaluation is standard practice in this benchmark line (Jing et al., 2022; Xu et al., 2022), adding mean±std over 3 random seeds for the main DRUGS results (Table 1) and Table 3 would increase confidence, especially for the data-scarce results where the relative gains are large but sample sizes are small.

- **Ablation on z (minimum fragment size) and κ** as a natural extension of the BRICS/RECAP ablation (Table 4).

## Removed Points

These points were raised by reviewers but are either factually incorrect, style nitpicks, parser artifacts, or demands outside the paper's scope. Treat them with caution.

1. **"No measure of variance is a methodological gap that weakens every claim"** — Moved to Nice-to-Haves. Reporting confidence intervals for large-scale conformer generation benchmarks is not standard practice in this field (TorDiff, GeoDiff, ConfGF all report single values). This is a nice improvement, not a methodological gap that weakens evidence.

2. **OCR/formatting artifacts** (e.g., "geun,verate", "denuo,tves", bracket imbalance in loss formula) — These are parser errors from PDF extraction, not author errors. Removed per hard rules.

3. **"The 'randomly selected fragmentation edges' specification is vague"** — The paper actually specifies this clearly in Section 4.1: "For a given molecule, we identify all fragmentation-edges and randomly select B = min(b, κ) edges." Every-epoch random selection is standard for data augmentation; the description is sufficient for reproducibility.

4. **"Missing appendix content / proofs"** — The parser strips appendix sections from all papers; these exist in the original submission. Removed per hard rules.

5. **"Weaknesses about whether cited models/tools exist"** — None raised directly, but any such concerns would be removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviews surface useful clarification requests but no angle or framing that the paper itself does not already present.

## Suggestions

1. **Clarify the conformer-matching protocol used for TorDiff.** A single sentence stating whether TorDiff numbers are from the original paper (which used conformer matching) or re-implemented under identical conditions would resolve the central ambiguity.

2. **Report the numerical value of z** (minimum fragment atom count) in Section 4.1. This is a trivial fix that improves reproducibility.

3. **Consider including GEOM-QM9 results or explicitly scoping them out** with a brief justification (e.g., "fragment augmentation is less impactful for small molecules; results are deferred to Appendix B").

4. **Add an ablation for κ** (e.g., 2, 5, 10) on the DRUGS-5000 subset to demonstrate sensitivity to fragment granularity.

5. **(Optional, nice-to-have)** Report mean±std over 3 seeds for the main tables to rule out the possibility that improvements are within run-to-run variation.

## Score and Decision

This paper proposes a simple, chemically intuitive augmentation strategy that delivers consistent empirical gains, particularly in the practically important data-scarce setting. The core claim is well-supported by the experimental evidence, the ablations are informative, and the method is presented with sufficient clarity (modulo the minor omissions above). The weaknesses are addressable and do not undermine the contribution. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>