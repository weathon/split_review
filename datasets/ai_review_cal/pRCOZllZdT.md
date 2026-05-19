- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8
Here is my consolidated review.

---

## Summary

BoPITO introduces a principled framework that integrates pre-trained Boltzmann Generators (BGs) into Implicit Transfer Operator (ITO) learning for molecular dynamics. The key idea is to decompose the score function of a conditional diffusion model into an equilibrium component (fixed by a pre-trained BG) and a learnable dynamic component weighted by a decay factor \(\hat{\lambda}^N\), so the model asymptotically samples the unbiased Boltzmann distribution at long time lags. The paper further proposes an interpolation scheme to combine off-equilibrium simulation data with experimental observables, enabling approximate recovery of unbiased dynamics from biased data.

## Strengths

- **Principled spectral score decomposition.** The core design (Eq. 10) cleanly separates the score into an equilibrium term from a Boltzmann Generator and a decaying dynamic term, grounded in the spectral decomposition of the transfer operator (\(\lambda_1=1\), \(\phi_1=\mu\)). This directly guarantees asymptotically unbiased equilibrium statistics as \(N\to\infty\) — a theoretically sound inductive bias.

- **Consistent improvement across two systems.** BoPITO outperforms standard ITO on both the low-dimensional Prinz potential and the 22-atom Alanine Dipeptide across multiple data budgets (Figure 3). The improvement is systematic: BoPITO achieves lower correlation error than ITO given the same amount of training data, particularly on long time-scales, and the gap narrows as data increases (as expected).

- **BG-based data generation is clearly beneficial.** Section 4.2 (Figure 2) cleanly demonstrates that initializing short MD trajectories from a pre-trained BG yields significantly lower correlation errors than starting from a single crystal structure, across lag times and trajectory counts. This validates a concrete, practical benefit that is cleanly isolated from the score decomposition.

- **Novel interpolation concept for biased data.** The BoPITO interpolator (Eqs. 11–12) provides a tunable protocol to bridge between models trained on off-equilibrium data and an unbiased equilibrium prior, using experimental observables to select the interpolation parameter. This is, to the authors' knowledge, the first deep generative transition density surrogate that can integrate multiple data sources (biased simulations + equilibrium prior + experimental observables).

## Weaknesses

### Fatal
None. The method is sound, the reasoning is coherent, and no experimental result is contradicted by the paper's own data.

### Major

- **The "one order of magnitude" claim is stated but not explicitly quantified.** The paper claims in the abstract, introduction, Section 4.3, and conclusion that BoPITO reduces required data by an order of magnitude. The supporting evidence is visual: Figure 3c–d shows that on Alanine Dipeptide, ITO with ~200 trajectories performs similarly to BoPITO with ~20 trajectories on long time-scales. No table reports the minimal number of trajectories needed for each method to reach a given error threshold (e.g., correlation error < 0.05), no explicit ratio is computed, and no statistical test confirms the factor. The split into "short, medium, and long" time-scales (Figure 3 caption) is not defined — the \(N\) ranges are never stated, so the reader cannot independently assess which time-scales drive the claim. This is the paper's headline quantitative result; it needs proper numerical support.

- **The interpolation experiment (Section 4.4) is validated only qualitatively.** The BoPITO interpolator recovers marginal distributions of \(\phi\) and \(\psi\) that visually match the unbiased ground truth (Figure 5), and the correlation function is fitted to one observable (Figure 4). However: (i) no quantitative metric is reported for the recovered densities (KL divergence, Wasserstein distance, histogram error); (ii) only one observable is used for fitting and no independent held-out observable is checked; (iii) the method is not compared against any alternative for incorporating the same bias and equilibrium prior (e.g., reweighting of the biased ITO output, or using the BG as a Metropolis-corrected kernel). The claim that BoPITO interpolators "recover approximate dynamics from models trained on biased simulations" is therefore supported by promising but incomplete evidence.

### Minor

- **No ablation separates the two components of BoPITO's improvement.** BoPITO combines (a) better initial-condition sampling via a BG and (b) the score decomposition inductive bias. Section 4.2 isolates (a), and Section 4.3 tests the full system. But there is no experiment training a standard ITO on BG-initialized trajectories (isolating the data-generation benefit without the score decomposition) or training BoPITO on the same initialization as baseline ITO (isolating the score decomposition without BG data). This makes it difficult to attribute how much of the improvement in Section 4.3 comes from better data coverage versus the spectral inductive bias.

- **The global decay hyper-parameter \(\hat{\lambda}\) is neither reported nor explored.** The paper defines \(0<\hat{\lambda}<1\) as a hyper-parameter (Eq. 10) and acknowledges sensitivity as a limitation (Limitations section), but the value used in experiments is never stated, and no sensitivity analysis (e.g., 2–3 values on one system) is provided. This affects reproducibility and robustness assessment.

### Trivial
- The split thresholds for "short, medium, and long" time-scales in Figure 3 are not defined in the text or caption. These should be stated explicitly (e.g., \(N\) ranges in simulation steps or physical time).

## Nice-to-Haves
- A brief discussion of the computational cost of pre-training the BG, and how to account for that cost when comparing sample efficiency (is the BG trained on the same data that would otherwise go to ITO?).
- Reporting the number of metastable modes visited by BG-initialized vs. single-start trajectories in the data generation experiment (Section 4.2).
- A comparison to alternative bias-correction methods for the interpolation setting (e.g., MSM-based TRAM), though this is scope-expanding and not required.

## Removed Points

*These points were flagged by reviewers but removed after verification against the paper. They should be treated with caution if encountered elsewhere.*

- **"The paper should compare to alternative bias-correction methods (TRAM, Metropolis correction)."** — Removed. The paper introduces a *new* framework for deep generative transition surrogates; requiring comparison to every existing MSM-based approach is scope creep. The paper correctly notes that "such estimators are so far unavailable for deep generative surrogates of the transition density."
- **"The paper should acknowledge the computational cost of training a BG."** — Removed; this is a reasonable discussion point but not a weakness. Moved to Nice-to-Haves.
- **"Show number of modes visited by each strategy."** — Removed as a weakness; this is a strengthening suggestion, moved to Nice-to-Haves.
- **Strength Finder's claim of "one-order-of-magnitude sample efficiency improvement"** — This strength is retained but qualified in the Weaknesses section. The paper does show a consistent improvement that *appears* to be roughly an order of magnitude; the weakness is that this is not rigorously quantified, not that the claim is false.
- **"The training procedure for \(s_{\mathrm{dyn}}\) is underspecified regarding gradient signal for large \(N\)."** — Removed. The paper follows standard ITO training (Section 2.5), and the factor \(\hat{\lambda}^N\) applies to the score, not to the loss. The effect is no different from training a standard diffusion model with variable \(N\), which is the standard ITO procedure. This is a natural property of the model, not a flaw.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an observation about the paper that the authors themselves do not make. The synthesis confirms that the method is principled, the evidence is directionally supportive but insufficiently rigorous on two fronts (quantification of the central efficiency claim, validation of the interpolator), and the missing hyperparameter and ablation details are addressable in revision.

## Suggestions

1. **Quantify the data efficiency factor explicitly.** For each system and time-scale bucket, report the minimum number of trajectories needed for BoPITO and ITO to reach a fixed error threshold (e.g., correlation error < 0.05) as a table. Compute and state the ratio explicitly. Define the short/medium/long split thresholds in physical time or \(N\).
2. **Validate the interpolator quantitatively.** Report KL divergence or Wasserstein distance between interpolated and ground-truth marginal distributions. Check at least one independent observable not used in fitting \(N_{\mathrm{int}}\).
3. **Add a two-component ablation.** Compare: (i) ITO on standard data, (ii) ITO on BG-initialized data, (iii) BoPITO on standard data, (iv) BoPITO on BG-initialized data for at least one system.
4. **State the value of \(\hat{\lambda}\) used and show sensitivity** (e.g., 2–3 values on Prinz or Alanine Dipeptide).
