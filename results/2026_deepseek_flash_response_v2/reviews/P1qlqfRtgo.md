Now let me write the final consolidated review.

## Summary

This paper compares three neural architectures (MLP, a "U-Net-like" residual network, and a DeepONet-style model) for surrogate modeling of thermal explosion kinetics in hydrogen-oxygen-air mixtures. Using a dataset of 70,000 samples spanning extreme combustion regimes (T ∈ [250,5000]K, p ∈ [10⁴,2×10⁷]Pa, Δt ∈ [10⁻¹⁰,10⁻⁵]s), the authors find that the U-Net-like model achieves substantially lower MSE (1.374×10⁻³) with non-overlapping 95% CIs than the MLP (2.029×10⁻²) and DeepONet (1.808×10⁻²). The paper's core claim is that architectural choice significantly affects performance for stiff chemical kinetics.

## Strengths

- **Multi-step recursive loss with decaying weights (Eq. 4):** Training on a 30-step recursive prediction loss with 1/k weighting is a principled design for stiff chemical kinetics. This goes beyond prior work (e.g., Goswami et al., 2024) that trained on a fixed set of future instants. The decaying weights prioritize near-term accuracy while still penalizing long-term drift.

- **Statistical reporting via non-overlapping 95% CIs (Table 1):** The paper reports means, standard deviations, and 95% confidence intervals for all three architectures. The U-Net CI [7.692×10⁻⁴, 1.980×10⁻³] does not overlap with the MLP or DeepONet intervals, establishing statistical significance. This level of statistical reporting is above average for this literature.

- **Physically motivated invariant enforcement:** All three models explicitly copy dt, N₂, and Ar from input to output (Sec. 4.1–4.3), ensuring that physically non-reacting quantities remain exact by construction. This is a simple but effective domain-knowledge inductive bias.

- **Dataset covering extreme combustion regimes (Sec. 3):** The training data spans 5 orders of magnitude in timestep, a 20× range in temperature, and 3 orders of magnitude in pressure, deliberately including sudden autoignition alongside slow induction. This is more extensive than many prior studies on operator learning for combustion.

## Weaknesses

### Major

- **Misleading architectural framing: the "U-Net" is an MLP with residual connections, and two of the three "architectures" are near-identical.** The architecture labeled "U-Net-like residual network" (Sec. 4.2) consists of: 13×100 expansion → 100×120 → 120×120 → 120×100 dense blocks → 100×13 compression, with two skip connections (a local skip adding expansion output to block output, and a global skip adding input to final output). There are no convolutional layers, no downsampling/upsampling, and no encoder-decoder structure — the defining characteristics of a U-Net. This is an MLP with residual connections. The plain MLP (Sec. 4.1) shares exactly the same layer structure (13×100 → 100×120 → 120×120 → 120×100 → 100×13), differing only in the absence of the skip connections. So the headline result that "U-Net outperforms MLP" is effectively "an MLP with residual connections outperforms the same MLP without them" — a modest and well-known finding (He et al., 2016). The paper repeatedly invokes "hierarchical feature extraction" and "multi-scale representation" (Sec. 5) to describe what is simply an MLP with skip connections, inflating the apparent contribution. The paper never acknowledges that two of its three "architectures" share the same structure.

- **Non-standard DeepONet implementation and unmeasured capacity confound.** The DeepONet-style model (Sec. 4.3) does not follow the standard formulation (Lu et al., 2021), where a branch network encodes input functions at sensor points and a trunk encodes query coordinates, combined via dot product. Instead, the branch processes 12 state variables through 12×120→120×120→120×120 layers reshaped to 12×10, and the trunk maps dt through 1×32→32×32→32×10, with the combination described as a "matrix product" whose exact form is ambiguous. More importantly, model sizes are not reported anywhere. Computing from the described layer dimensions: the MLP and U-Net each have ~41,000 parameters, while the DeepONet-style model has ~32,000 (branch ~30,600 + trunk ~1,450). Without controlling for parameter count or reporting FLOPs/training time, performance differences cannot be cleanly attributed to architecture rather than capacity. This weakens the paper's central claim that "network architecture is an important factor" separable from model size.

- **CO and NO appear in figures but are not in the described chemical mechanism.** The figure captions (Figs. 3 and 4) list CO and NO among the plotted species. However, the reduced mechanism in Section 2 lists only 9 hydrogen-oxygen reactive species (H₂, O₂, H₂O, OH, H, O, HO₂, H₂O₂, OH*) plus inert N₂ and Ar — CO and NO are not among them. This is a factual inconsistency in the paper's own system description.

### Minor

- **Dataset structure is ambiguous.** The paper states 70,000 samples split 50k/15k/5k (Sec. 3), but it is unclear whether these are independent time points or full trajectories. If they are consecutive time steps from trajectories, the independence assumption underlying the reported confidence intervals may be violated due to temporal autocorrelation.

- **Only one random seed per architecture.** The reported standard deviations are across test samples, not across training initializations. Without multiple seeds, we cannot assess whether the observed performance gaps are robust to different weight initializations.

- **Normalization scheme not described.** The paper states that trajectories are plotted in "normalized space" (Sec. 5) but never specifies the normalization method (min-max, z-score, etc.), which is necessary for reproducibility.

- **No rollout-horizon analysis.** The multi-step loss (Eq. 4) weights 30-step rollouts, but results are only reported as aggregate per-sample MSE. Plots of how error accumulates over the rollout horizon for each model would be far more informative for a surrogate-modeling application.

### Trivial

None.

## Nice-to-Haves

- Reporting computational cost (training time, inference speed, parameter counts) would strengthen practical claims about suitability for combustion simulations.
- Testing with multiple hyperparameter configurations would strengthen the claim that architecture — not tuning — drives results.
- Rebranding the "U-Net" honestly as "MLP with residual connections" and acknowledging that the comparison reduces to an ablation of skip connections would make the paper more credible.

## Removed Points

These points from the harsh reviewer were removed after cross-checking against the paper:

- **"Contradictory abstract/conclusions"** — Removed. The abstract says "the problem remains unresolved" and the conclusions say "architecture is critical." These are not contradictory; a problem can be unsolved while design choices still matter. This is a misreading.
- **"DeepONet capacity is underpowered (~1,300 params)"** — Demoted. The critic focused only on the trunk network (~1,450 params) while ignoring the branch network (~30,600 params). Total DeepONet-style model has ~32,000 params vs ~41,000 for MLP — a ~25% difference, not the order-of-magnitude gap implied. The capacity concern remains valid but is weaker than framed.
- **"Question never genuinely addressed"** — Removed. The paper does compare the models and arrives at a finding. The comparison is flawed, but the question was addressed on its own terms.
- **"Code and data availability"** — Removed per hard rules (cannot flag cited entities as nonexistent).
- **"Missing related works"** — Removed per hard rules.
- **Formatting/style nitpicks** — Removed per hard rules.
- **"Hyperparameter selection may favor one model"** — Weakened to nice-to-have; using identical training setups for all models is standard practice and not inherently unfair.

## Novel Insights

The harsh reviewer's central observation — that two of the three "architectures" are nearly identical MLPs differing only in residual connections — is valid but is a critique of framing rather than a novel synthesis. The paper's own contributions are accurately described in the strengths above; no additional novel insights emerged from the review process beyond a clear-eyed assessment of the methodological gap between the paper's claims and its experimental design.

## Suggestions

1. **Rebrand honestly.** Drop the "U-Net" label throughout. Call the architecture "MLP with residual connections" and explicitly frame the comparison as an ablation study of skip connections for chemical kinetics. This would align the paper's language with its content.
2. **Report and match capacity.** Provide parameter counts for all models, and either match them (e.g., widen the DeepONet branch/trunk) or report FLOPs so readers can assess whether capacity differences drive results.
3. **Implement a standard DeepONet** following Lu et al. (2021): branch encodes the initial condition as a function evaluated at sensor points, trunk encodes the query time, output is the dot product. If the authors intend to compare against DeepONet, the implementation should be canonical.
4. **Add multiple random seeds** (at least 5) and report variance across training runs, not just test samples.
5. **Clarify dataset structure** — are the 70,000 samples independent time points or trajectory segments? Describe the normalization scheme.
6. **Resolve the CO/NO discrepancy** in figures — either explain the presence of these species or correct the captions.
7. **Show per-step error accumulation** over the 30-step rollout horizon to demonstrate how each model behaves as prediction horizon increases.

---

## Calibration Report

**Round 1 (Bracketing):** Searched for "neural network architecture comparison surrogate model combustion kinetics" across three score bands: (−1, 3.5), (3.5, 7.5), (7.5, 11). Weak-band anchors (avg 2.33–3.00): papers with fundamental flaws or trivial contributions (Atmospheric Radiation Parameterization at 3.00, Residual F-FNO at 3.00, EPINN at 2.50). Middle-band anchors (avg 4.50–7.33): Hottel Zone at 4.50 (reject), Open-CK at 6.25 (accept), HyResPINNs at 5.00, KinFormer at 6.00. Strong-band anchors (avg 7.60–8.00): substantially more sophisticated papers. Initial bracket: 3.0–5.0.

**Round 2 (Narrowing):** Searched for "neural network architecture comparison surrogate modeling chemical kinetics combustion" (2.5, 5.0) and "MLP DeepONet comparison physics simulation surrogate model" (3.0, 6.0). Key comparisons:
- *Residual F-FNO* (avg 3.00, reject): Adding residual connections to FNO for turbulence. Similar core contribution (skip connections improve a baseline), similarly limited evaluation. Our paper has better statistical rigor and a more challenging dataset, making it slightly stronger.
- *Atmospheric Radiation Parameterization* (avg 3.00, reject): Compared many architectures for weather emulation, had code+real-world coupling. Our paper's dataset is more purpose-built and the loss design is more principled, but our architectural comparison is weaker.
- *Hottel Zone* (avg 4.50, reject): Physics-constrained NNs for furnaces. Methodologically cleaner comparison, comparable applied-combustion focus. Our paper is weaker due to architectural mislabeling and capacity confound.

**Final score:** 3.5. The paper sits between the 3.0 anchors (which have weaker methodology but are honest about what they compare) and the 4.0–4.5 anchors (which have cleaner comparisons). The core methodological issues — architectures not genuinely distinct, non-standard DeepONet, unmeasured capacity — prevent a higher score despite the paper's genuine strengths in statistical reporting and dataset design.

**Anchors consulted:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| otXB6odSG8.md | 3.00 | 1,2 | Comparable; our paper has better stats/dataset but weaker architecture framing |
| yGdoTL9g18.md | 3.00 | 1,2 | Similar incremental contribution (skip connections); our paper slightly stronger on evaluation rigor |
| hz3NtNpDNv.md | 4.50 | 1,2 | Cleaner comparison methodology; our paper weaker due to architectural confounds |
| A23C57icJt.md | 6.25 | 1 | Substantially stronger (large benchmark, comprehensive eval) |
| fH9eqpCcR3.md | 5.20 | 2 | Substantially stronger (novel pretraining methodology, extensive experiments) |
| sSWiZr8QU7.md | 4.00 | 2 | Comparable quality; different task domain |
| HDmmwwTIlf.md | 2.50 | 1 | Weaker; our paper has better data and evaluation |
| aAI92OHA4t.md | 2.33 | 1 | Weaker; different contribution type |
| SYiOxXWlKU.md | 2.50 | 1 | Weaker; addressing stiff ODEs with simpler method |

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>