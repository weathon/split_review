Now I have a thorough understanding of the paper and its calibration context. Let me compile the final review.

---

## Summary

CausalNovo introduces a model-agnostic framework that adds a Causality Extraction Module (CEM) to existing de novo peptide sequencing models. Grounded in a structural causal model, it uses contrastive learning with spectrum perturbations and information-theoretic objectives to disentangle causal signal peaks from spurious noise peaks in latent representations. Applied to three diverse baseline architectures (CasaNovo, AdaNovo, π-HelixNovo) across three benchmark datasets, it yields consistent improvements in amino acid, peptide, and PTM-level metrics, with particularly strong gains under noisy conditions and perturbation stress tests.

---

## Strengths

- **Compelling vulnerability motivation with clear mitigation**: The paper systematically demonstrates that baseline models degrade sharply when non-causal (noise) peaks are perturbed (Figures 1, 3), and CausalNovo substantially reduces this degradation — relative improvements reach up to 28.5% under strict perturbation thresholds (Table 6). This directly supports the core claim that the framework reduces reliance on spurious correlations.

- **Consistent and substantial gains across diverse architectures and datasets**: CausalNovo improves amino acid precision by up to +14.2% (AdaNovo on HC-PT, Table 1) and yields peptide and PTM-level gains across all three baselines and three benchmark datasets (Tables 1–2). The gains are not isolated to one model or dataset, strengthening the model-agnostic claim.

- **Thorough ablation and component analysis**: Ablation studies (Table 4) validate each loss component (independence, purification, symmetric contrastive), and Table 5 isolates the contribution of replace-based perturbation and causality enhancement. These confirm that design choices are individually beneficial, not just bundled into an opaque package.

- **Robustness across noise levels and cross-species transfer**: CausalNovo maintains superior amino acid precision across the full NSR range (0–10) on HC-PT for all three baselines (Figure 4), and leave-one-out cross-species validation shows consistent peptide precision gains for every species in the Nine-species dataset (Table 3).

- **Mechanistic evidence via attention analysis**: Table 7 shows a clear shift — the fraction of predictions where all top-3 attended peaks are causal rises from 19.26% (baseline) to 32.87% (CausalNovo), while the rate of predictions completely ignoring causal peaks drops. This provides direct evidence that the framework changes what the model attends to in the intended direction.

---

## Weaknesses

### Fatal

None.

### Major

- **The purification objective lacks a clear causal justification**: Section 3.3 introduces maximizing \(I(z_s; Y)\) as an auxiliary objective that "can indirectly lead to the purification of \(z_c\)." But the mechanism is never explained: why would *maximizing* predictive information in the non-causal branch help remove non-causal information from the causal branch? The text argues that optimizing \(I(z_c; Y)\) "can reduce \(I(z_s; Y)\)," then introduces maximizing \(I(z_s; Y)\) to "address this issue" — but this reads as contradictory (moving predictive signal into \(z_s\) would seem to put it back where it was). The ablation (Table 4) shows this term adds ~0.8% amino acid precision, so it empirically helps, but the paper does not explain *why* in terms that follow from its own causal principles. This weakens the conceptual coherence of the causal narrative. The loss could be honestly reframed as a regularizer that prevents the mask from collapsing all predictive information into \(z_c\), which would align the description with what the loss empirically achieves.

### Minor

- **The independence objective's conditioning on \(Y\) is only implicit**: Equation 5 targets \(I(z_c; z_c' \mid Y)\) but the implemented contrastive loss (InfoNCE) does not explicitly condition on \(Y\). The paper argues that using same-peptide positive pairs implicitly conditions on \(Y\) (since \(Y\) serves as a proxy for \(C\)), which is a reasonable approximation, but the text states "\(I(z_c; z_c' \mid Y) \approx \log(\dots)\)" and then presents the standard unconditioned InfoNCE. An explicit explanation of how the conditioning is achieved through pair selection would connect the derivation to the implementation.

- **Causality enhancement may introduce a training-time vs. test-time mismatch**: The intervened spectrum \(x_{\text{intervene}}\) includes all theoretical peaks from the ground-truth peptide (\(x_{\text{theory}}\)). This enriched spectrum is used as the positive view in the contrastive loss. While the decoder operates only on \(z_c\) from the *original* spectrum at both training and test time (so no direct leakage into predictions), the contrastive objective encourages the encoder to match representations between the noisy original and the theoretically-enriched view. Whether this teaches robust feature extraction or creates a shortcut that overfits to the augmentation is not analyzed. The ablation (Table 5) shows the enhancement helps, but a discussion of this risk and ideally a robustness check (e.g., removing enhancement and measuring the gap) would strengthen confidence.

- **Baseline retraining discrepancies are not explained**: In Table 1, retrained CasaNovo jumps from 0.697 to 0.741 amino acid precision on Nine-species, while AdaNovo drops from 0.698 to 0.681, and π-HelixNovo stays at 0.765. The mixed pattern (one up, one down, one flat) does not suggest systematic unfair tuning, but the paper does not discuss why these differences exist. A brief note on whether the same training recipe, optimizer, and preprocessing were used for all models would clarify that the CEM — not better hyperparameter tuning — drives the reported gains. The gains of CausalNovo over the retrained baselines are still clear and substantial, so this does not threaten the core claims.

- **The \(C \perp S\) independence assumption is strong and undiscussed**: The SCM (Figure 2A, Eq. 2) assumes causal and non-causal factors are independent. In real mass spectra, noise patterns can correlate with peptide properties (e.g., co-eluting peptides sharing chemical features). The paper does not discuss how violations of this assumption might affect the method's behavior. A brief acknowledgment would suffice.

- **The tolerance threshold \(\gamma\) (Eq. 4) for identifying non-causal ions is never specified**: The paper mentions \(\gamma\) as a tolerance for matching peaks to theoretical spectra but gives no value and no sensitivity analysis. Since the entire intervention pipeline depends on correctly classifying peaks as causal vs. non-causal, the method's sensitivity to this threshold matters for reproducibility.

### Trivial

- The contrastive loss uses mean-pooled aggregated representations with \(\tau=0.1\), but the impact of the pooling strategy is not discussed.

---

## Nice-to-Haves

- Reinterpreting the purification loss as a regularizer that prevents \(z_c\) from hoarding all predictive information, rather than forcing a strained causal "purification" argument, would make the paper more intellectually honest and easier to follow.
- A sensitivity analysis for \(\gamma\) (the peak-matching tolerance) would improve reproducibility and practical adoption.
- Evaluating CausalNovo under the out-of-distribution benchmarking protocol used by ContraNovo and RankNovo (training on large external corpora) is acknowledged as future work; doing so would further validate real-world robustness.
- The ~2.3× training time increase is noted but could benefit from a brief discussion of whether mixed-precision or gradient accumulation could mitigate it.

---

## Removed Points

*These points were flagged by reviewers but are removed from the final review. Treat them with caution.*

- **"The purification objective could simply be an extra supervised signal"**: While the causal justification is shaky (retained as Major above), the ablation shows the term contributes beyond the supervised CE loss already present in the baseline. The claim that it's "just extra supervision" was not grounded in a specific flaw in the ablation design. Removed as speculative.

- **"Similar large improvements appear for other baselines" (re: retraining discrepancies)**: Factually incorrect — AdaNovo retrained *worse* on Nine-species and π-HelixNovo stayed the same. The pattern is not "all baselines jumped." Retained only the legitimate concern about explaining the discrepancies (as Minor).

- **Decoder usage in purification**: The Harsh Critic asked whether the purification CE loss uses the same decoder as the sufficiency loss. Actually, the paper specifies that both use cross-entropy losses (Eq. 6), which implies the same decoder architecture. This concern is based on speculation, not evidence of a problem.

- **"Tightening the threshold could be misinterpreted" (Introduction)**: This is a reader-comprehension concern about Figure 1, not a paper flaw. The figure is clear enough.

- **Impact of pooling and temperature**: These are implementation details that fall below the threshold for meaningful criticism. The temperature is stated (\(\tau=0.1\)) and pooling is standard practice.

- **Training time overhead**: Already acknowledged by the authors in the Conclusion. Not a weakness to flag.

- **Missing appendix content / references**: The parser strips appendix sections; these exist in the original submission. Cannot be flagged.

---

## Novel Insights

The vulnerability analysis methodology — systematically replacing noise peaks at varying \(m/z\) tolerance thresholds and measuring degradation — is a genuinely useful diagnostic that could become standard for evaluating de novo sequencing models. The attention-shift analysis (Table 7), which counts causal peaks among top-attended positions per prediction, provides a simple but effective mechanistic probe that goes beyond aggregate metrics. These evaluation practices are transferable to other mass spectrometry models.

---

## Suggestions

- Reframe the purification loss honestly: instead of claiming it "purifies \(z_c\)" through an unexplained mechanism, present it as preventing the importance mask from collapsing — by ensuring \(z_s\) retains some predictive capacity, the mask \(M\) cannot simply assign all peaks to \(z_c\). This is consistent with the empirical behavior and removes the weakest link in the causal argument.
- Specify \(\gamma\) and provide a brief sensitivity sweep (e.g., \(\gamma \in \{0.01, 0.02, 0.05\}\) Da) in a small table. This is a low-effort, high-value addition.
- Add a sentence confirming that the same training recipe (optimizer, LR schedule, preprocessing) was used for both retrained baselines and CausalNovo-augmented models, to preempt concerns about hyperparameter confounding.

---

## Score and Decision

**Calibration anchors used:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| ReNovo (uQnvYP7yX9) | 6.50 | R1 | Retrieval-based de novo sequencing — similar empirical strength, accepted. CausalNovo has stronger conceptual contribution. |
| RankNovo (87B3zDRMjv) | 5.50 | R1/R2 | Reranking approach — modest improvements, limited novelty. CausalNovo is clearly stronger. |
| CFD (CsOIYMOZaV) | 6.50 | R2 | Causal disentanglement for molecular representation — most comparable in structure (disentanglement framework, biological domain, OOD robustness). Similar empirical thoroughness; both have some conceptual gaps in disentanglement justification. |
| Celcomen (Tqdsruwyac) | 6.67 | R2 | Causal disentanglement for spatial transcriptomics — stronger theory but weaker empirical validation. CausalNovo has more comprehensive experiments. |
| MolSpectra (xJDxVDG3x2) | 6.33 | R2 | Pre-training with spectra — different domain but similar empirical rigor. CausalNovo is slightly stronger. |

**Bracket**: Round 1 placed the paper between 5.5 and 8.0. Round 2 narrowed this to approximately 6.0–7.0. The paper is most comparable to CFD (6.50) and Celcomen (6.67): it has stronger empirical validation than Celcomen but a less polished theoretical story. It is clearly above RankNovo (5.50) — the contribution is more substantial and the evaluation more thorough. It is comparable to ReNovo (6.50) in overall quality, with a more ambitious conceptual framework but some execution gaps in the causal narrative.

**Score rationale**: The paper's core idea (contrastive learning with causal interventions on mass spectra) is sound and well-executed. The empirical evidence is thorough and convincing across multiple baselines, datasets, and stress tests. The main weakness is that the causal narrative is not fully coherent — particularly the purification objective — which prevents the paper from achieving the theoretical clarity of a top-tier contribution. I score this at **6.5**, comparable to CFD (6.50) and slightly below Celcomen (6.67), reflecting a solid contribution with meaningful empirical results but conceptual presentation that needs revision.

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>