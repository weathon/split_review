Now I have thoroughly verified the paper against the reviewer claims. Here is my synthesized review:

---

## Summary

The paper proposes FedPMVR, a federated learning algorithm that applies momentum-based variance reduction selectively to the final classification layers of neural networks (as opposed to all layers) to mitigate client drift from non-IID data. The method trains initial layers with standard SGD while maintaining a per-client momentum term for the last two layers. Experiments on CIFAR10, MNIST, and FMNIST with two heterogeneity levels show that FedPMVR consistently achieves the highest top-1 accuracy across most settings and reduces the number of communication rounds needed to reach FedAvg's best accuracy.

## Strengths

1. **Consistent empirical gains across multiple settings.** Table 1 shows FedPMVR achieves the highest top-1 accuracy in 7 out of 8 experimental configurations (three datasets × two heterogeneity levels × two architectures). While margins are sometimes small (e.g., 51.86% vs 51.84% on CIFAR10 β=0.1), the pattern is consistent across diverse conditions.

2. **Substantial communication round reduction.** Table 2 reports 1.42× to 3.0× speedups over FedAvg in reaching FedAvg's own best accuracy. This is a practically meaningful result if it holds with statistical rigor.

3. **Ablation study validates selective targeting of classification layers.** Figure 8 shows that applying the proposed momentum correction to the final classification layers yields the best accuracy and convergence, while applying it to all layers harms performance. This directly supports the paper's core design rationale.

4. **Broad baseline comparison.** The paper compares against eight FL algorithms (FedAvg, FedProx, FedNova, FedBN, FedDyn, MOON, SCAFFOLD, FedPVR) across three datasets, plus partial client participation (Fig. 6) and IID data (Fig. 7) experiments.

## Weaknesses

### Major

1. **Flawed drift analysis (Section 2.3.1).** Equation (15) claims that the drift for the last two layers under FedPMVR is δ_c^i = (1−α)(∇f_c(w_t^i) − ∇f(w_t^i)). This does **not** follow from the stated momentum update rule (m_{t+1} = α·m_t + (1−α)∇f_c) without assuming m_t^{c,i} = ∇f(w_t^i)—i.e., that the local momentum term equals the *global* gradient. The momentum term is a local quantity that accumulates past local gradients; equating it to the global gradient is unjustified. Since this drift reduction is presented as the paper's central theoretical justification for the method, the analysis as written is mathematically unsupported. The paper would be stronger either providing a correct derivation or removing the claimed factor and presenting the method on empirical grounds alone.

2. **Missing critical baseline: FedAvgM (or standard client-level momentum).** The paper's core contribution is introducing momentum into local updates. The most natural baseline is the same algorithm with momentum applied **globally or to all layers** (e.g., FedAvgM). The ablation study (Fig. 8) shows that applying the paper's *own non-standard momentum formulation* to all layers hurts performance, but this does not rule out that standard momentum SGD (FedAvgM) would outperform both. Without this baseline, it is impossible to attribute observed improvements to the "partial" aspect rather than to momentum itself. This is the most significant empirical gap.

3. **Results lack statistical rigor.** All main accuracy results (Table 1) are reported as single numbers with no error bars, standard deviations, confidence intervals, or indication of the number of random seeds or runs. Given the inherent randomness in FL (client sampling, data partitioning, initialization), single-run results are not trustworthy—especially when the claimed improvements over the second-best method are as small as 0.02 percentage points (FedPMVR 51.86% vs FedBN 51.84% on CIFAR10 β=0.1). Without error bars, the claim of "outperforming" state-of-the-art methods is not statistically substantiated. The communication round reduction metric (Table 2) suffers from the same issue.

### Minor

4. **Conformal prediction section (Section 3.4) is poorly motivated and mischaracterized.** The paper states that conformal prediction is used "to improve model performance," which mischaracterizes the technique—conformal prediction produces prediction sets with coverage guarantees, not improved top-1 accuracy. The connection to the paper's main contribution is unclear, the experimental setup (what "individual models" are, how predictive sets are constructed) is not described, and the section reads as an unrelated add-on. It should either be removed or given a proper justification and exposition.

5. **"No extra parameters" claim is misleading.** The paper states "FedPMVR does not necessitate any extra parameters, unlike SCAFFOLD and FedPVR." While momentum terms are not communicated to the server (so communication cost is unchanged), they are stored and maintained per client, adding local memory and computational overhead. The claim is accurate only in the narrow sense of communication parameters; it should be qualified.

6. **Inconsistency in method description between Sections 2.2.1 and 2.3.1.** Section 2.2.1 describes a two-phase procedure: train with SGD for several epochs, compute gradients relative to initialization, update momentum once, then correct weights. Section 2.3.1 describes per-step momentum integration (m_{t+1} = α·m_t + (1−α)∇f_c; w ← w − η·m). These are different procedures, and it is unclear which one is actually implemented. This ambiguity harms reproducibility.

7. **Typo in server aggregation formula (Eq. 7).** The formula writes `W_{t+1} = (n_c/n) Σ w_t^i`, where `n_c/n` is a scalar from a single client placed outside the summation. The intended form is presumably `Σ (n_i/n) w_t^i`. This appears to be a transcription error but the current form is mathematically incoherent.

### Trivial

8. **"First" novelty claim is overstated.** The paper claims to be "the first work to leverage such a selective momentum-based regularization." Given prior work on selective correction in FL (FedPVR uses selective control variates) and the widespread use of momentum in FL (FedAvgM, server-side momentum), this claim should be moderated.

## Nice-to-Haves

- Report main results with error bars over at least 3–5 seeds, ideally with statistical significance tests.
- Include FedAvgM (standard momentum FL) as a baseline.
- Correct or remove the mathematically unsupported drift reduction factor in Eq. (15).
- Remove the conformal prediction section or integrate it properly with a clear motivation and experimental setup.
- Clarify the inconsistency between the two-phase description (Section 2.2.1) and the per-step description (Section 2.3.1).
- The main text should at minimum state the convergence rate and key assumptions from the theoretical analysis (currently relegated to the stripped appendix) so readers can assess the claim of "limited reliance on data heterogeneity."

## Removed Points

These points from the reviews are flagged for removal; treat them with caution:

- **Criticism that the convergence analysis (Section 2.4) is an empty placeholder.** The parser strips appendix content from all papers; the theoretical analysis exists in the original submission. This is a parser artifact, not an author error.
- **Claim that "the illustrative example does not demonstrate that momentum would fix this."** The paper does not claim the toy example demonstrates momentum efficacy; it illustrates the client drift problem that motivates the method. This is a generic criticism that misreads the paper's pedagogical intent.
- **Strength from Strength Finder about conformal prediction adding "practical insight."** This conflicts with the verified weakness (Major #4) that the CP section is poorly motivated and mischaracterized. Per the rules, when strength and weakness disagree, the weakness wins. Dropping this strength.

## Novel Insights

The most insightful observation from the reviews is that the paper's method description is internally inconsistent: Section 2.2.1 describes a two-phase procedure (train, then correct) while Section 2.3.1 describes per-step momentum integration. If the method is actually the two-phase version, then the drift analysis in Section 2.3.1 (which assumes per-step momentum) is disconnected from the actual algorithm, compounding the theoretical issues flagged above. This inconsistency, rather than either issue in isolation, is the most actionable finding for the authors.

## Suggestions

1. Clarify the actual implementation: is it per-step momentum (as in Section 2.3.1) or post-hoc correction (as in Section 2.2.1)? Fix the inconsistency and align the theoretical analysis with the implemented method.
2. Add FedAvgM as a baseline and report all main results with error bars over multiple seeds.
3. Either remove the flawed drift factor derivation in Eq. (15) or provide a correct derivation that accounts for the accumulation of local momentum.
4. Remove the conformal prediction section or rewrite it with proper framing (it provides calibrated prediction sets, not improved top-1 accuracy) and a clear connection to the method.

## Score and Decision

The paper's core direction—selective momentum on classification layers to combat client drift—is sensible and the ablation study provides meaningful support for the design choice. The consistent (though often marginal) empirical improvements across many settings suggest the idea has merit.

However, the paper has three major problems: (1) the theoretical drift analysis that purports to show a (1−α) reduction factor is mathematically unsupported; (2) the most important baseline (FedAvgM, standard momentum FL) is absent, so the "partial" aspect cannot be evaluated; and (3) the main results lack any statistical rigor, which is especially problematic given the tiny margins in several comparisons. These issues collectively prevent acceptance in the current form. The contribution is incremental but potentially useful; a substantially revised version with corrected theory (or honest removal of the unsupported claim), the missing baseline, and proper error bars could be a moderate contribution to the FL literature.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>