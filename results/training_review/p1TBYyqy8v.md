Now I have all the evidence I need. Let me compose the final consolidated review.

>

## Summary

This paper introduces *spreading OOD detection*, a new benchmark for node-level OOD detection on graphs where OOD nodes propagate along edges via epidemic models (SI/SIS), replacing the static random-node-selection protocol used in prior work. The authors propose EDBD, an energy-based detector that controls neighborhood aggregation through an energy similarity matrix (edge-level) and an energy consistency matrix (node-level) to prevent the mixing of ID and OOD scores. A new Spreading COVID-19 dataset is also contributed. Extensive experiments on seven datasets show EDBD achieves best average metrics (FPR95-T, AUROC-T, AUPR-T) against eight baselines.

## Strengths

- **Novel and well-motivated problem formulation**: The paper correctly identifies that prior node-level OOD benchmarks with randomly selected OOD nodes ignore interactions among nodes. The epidemic-spreading formulation (Section 3) introduces realistic temporal and spatial structure absent from prior work—this is a genuine contribution likely to inspire follow-up research.

- **Effective method design with clear ablation support**: EDBD's two-component aggregation (energy similarity at edge level, energy consistency at node level) is intuitive and empirically justified. The ablation study (Table 4) confirms that both components contribute meaningfully and that their combination outperforms either alone, while removing both (reducing to GNNSAFE-style uniform aggregation) yields the worst results.

- **Strong empirical results, especially on Spreading COVID-19**: On the proposed COVID-19 dataset with SI model (Table 2), EDBD achieves 14.5% FPR95-T versus 28.4% for the second-best baseline GNNSAFE—a large relative improvement of 49%. Similar advantages appear across Cora and LastFM Asia (Table 3), with consistent gains under both SI and SIS models.

- **Real-world dataset contribution**: The Spreading COVID-19 dataset provides 23-dimensional symptom-grounded features (based on symptom frequencies for normal, allergies, cold, flu as ID; COVID-19 as OOD) on a human-network graph structure from LastFM Asia, along with careful justification for using online social network structure as a proxy for offline contact networks (Appendix A).

- **Comprehensive and fair evaluation**: Eight baselines spanning i.i.d. OOD detectors (MSP, ODIN, Mahalanobis, Energy) and graph-aware methods (GKDE, GPN, OODGAT, GNNSAFE) are compared using the same backbone encoder and tuned hyperparameters, with results averaged over 10 independent runs.

## Weaknesses

### Fatal

None.

### Major

- **Evaluation metrics do not support the claim of "performs well at any time stamp"** (the paper's central motivation, stated at lines 18 and 48). All reported metrics (FPR95-T, AUROC-T, AUPR-T) are **averages over time stamps within each episode** (Section 5.1, line 176). This averaging can mask catastrophic failure at early stages (where OOD nodes are sparse) or late stages. A detector could perform poorly when OOD is rare (e.g., t=1) and well when many nodes are infected, still producing a decent average. The paper never reports per-time-step curves or even per-stamp statistics. The authors explicitly define the goal as "discriminate OOD nodes well in every t" but then evaluate only with aggregate metrics. This is not a minor omission—it directly undermines the main evaluative claim for EDBD on the proposed benchmark. The gap is fixable (additional figures showing performance vs. t for key settings), but the evidence as presented is incomplete.

### Minor

- **The "realistic" benchmark claim is overstated for non-COVID datasets**. The paper criticizes prior work for using "unrealistic benchmarks" but then generates OOD features for Cora and LastFM Asia using a simple Bernoulli distribution (x ~ Ber(0.1)) entirely unrelated to any real OOD distribution. Only the Spreading COVID-19 dataset provides domain-relevant OOD features. The paper's core improvement over prior work is the *spatial/temporal structure* of OOD node placement (which is genuinely novel and valuable), not the realism of the OOD features themselves. The abstract's language ("unrealistic benchmarks" vs. "realistic benchmarks") creates an expectation the paper does not fully deliver on.

- **Missing hyperparameter sensitivity analysis and K ablation**: The method introduces three hyperparameters (α, β, ε) and an aggregation step count K, yet the ablation study (Table 4) only removes entire components (S or C) without varying α, β, ε, or K. The value of K is not even reported. Without understanding how performance depends on these choices, the method's robustness is unclear and reproducibility is harder.

- **No analysis of sensitivity to initial classifier quality**: EDBD constructs the similarity matrix S and consistency matrix C from the initial energies E^(0). If the initial classifier is unreliable (which is the very problem the method aims to address), these matrices could also be unreliable. The paper does not examine this dependency (e.g., by varying classifier capacity or training set size) to test whether EDBD remains beneficial when initial energies are noisy.

### Trivial

- On the label leave-out task (Table 1), EDBD's FPR95 improvement over GNNSAFE on Cora is marginal (~1%, within one standard deviation). The "state-of-the-art" claim is numerically correct but the margin on this specific dataset is small.

## Nice-to-Haves

- Time-resolved performance curves (FPR95 as a function of t) for at least one key setting (e.g., Cora SI) to substantiate the "any time stamp" claim.
- Multi-seed results on Cora/LastFM (Table 3 only shows single-seed for these; multi-seed appears only for COVID-19).
- Convergence analysis or empirical demonstration of stability for the iterative energy aggregation (Eq. 4).
- Discussion of the sensitivity of the "feature replacement upon infection" assumption—in some real spreading scenarios (e.g., computer viruses), infected nodes' observable features may not change.
- Comparison against a simple graph-smoothing baseline (e.g., Laplacian smoothing on energies with a fixed number of steps) to clarify whether EDBD's benefit comes from the specific similarity/consistency weighting or just from any form of controlled smoothing.

## Removed Points

*These points are flagged to be removed—treat them with caution.*

- The critic's concern about "stability of the similarity function under different energy scales" is addressed by the min-max normalization term ε·(max−min) in Equation (5), which explicitly handles scale variation. The function is designed to be scale-aware, not scale-sensitive.
- The suggestion to characterize the "fixed point" of the recurrence or provide "spectral analysis" is standard for theoretical papers but not standard practice for empirical method papers in this area. The method's behavior is sufficiently characterized by the ablation study and empirical validation across multiple datasets.
- The critic's claim that "the paper does not compare this pattern to any real-world node-level OOD scenario beyond the COVID analogy" ignores that the COVID-19 dataset IS the paper's real-world scenario, designed precisely for this purpose.

## Novel Insights

The reviews surface a tension between the paper's framing and its evaluation that is worth articulating explicitly. The paper introduces spreading OOD detection as a *temporally-aware* benchmark where performance matters at every step of the epidemic, yet evaluates with metrics that collapse over time. This is not merely a missing experiment—it reflects a deeper question about what "good" means for this task. Should an OOD detector be penalized equally for mistakes when OOD nodes are rare (early t) vs. common (late t)? The metric choice (simple averaging) implies yes, but the paper's framing ("well in every t") suggests the goal is uniform performance. The authors' own method, which uses fixed pre-computed weights (S and C) from initial energies, may actually perform differently across t as the energy distribution shifts—making the time-resolved question non-trivial even for EDBD. This gap between framing and evaluation is the single most actionable finding from the review process.

## Suggestions

1. **Add time-resolved evaluation**: For at least one key setting (e.g., Cora with SI model), provide a figure showing FPR95, AUROC as a function of the time stamp t, with error bands across episodes. This directly addresses the gap between the paper's central motivation and its evidence.
2. **Report and ablate K**: State the value of K used in experiments and add an ablation showing performance vs. K (e.g., K ∈ {1, 3, 5, 10, 20}) to demonstrate robustness.
3. **Add hyperparameter sensitivity analysis**: Vary α and β (and possibly ε) over a grid for one dataset and show that performance is not overly sensitive.
4. **Tone down the "realistic" language** for non-COVID datasets—describe the contribution as adding *spatial/temporal structure* (which is genuine) rather than claiming full "realism" when OOD features are still synthetic Bernoulli samples.
5. **Add multi-seed results** on Cora and LastFM Asia to match the multi-seed evaluation already provided for the COVID-19 dataset.

## Score and Decision

The paper introduces a genuinely novel and important problem formulation, a sensible method, and a useful dataset. However, the core evaluative claim—that EDBD "performs well at any time stamp"—is not supported by the evidence provided (only time-averaged metrics are reported). This gap weakens the paper's central argument and prevents acceptance in the current form. The remaining weaknesses (missing sensitivity analysis, overstatement of "realistic" benchmarks) are addressable but compound the concern. The paper's contributions are real and the path to a strong revision is clear.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>