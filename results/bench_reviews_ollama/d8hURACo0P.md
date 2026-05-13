## Summary
The authors train LSTM policies with PPO to perform a delayed center-out reaching task with curl-field perturbations, replicating the experimental paradigm of Sun et al. (2022). They introduce two KL-based "zeroness" and "smoothness" regularizers to keep policy accelerations biophysically plausible, and report that the trained networks replicate several behavioral (overcompensated curved reaches, faster relearning) and neural (uniform preparatory shifts, stable force-predictive subspace) signatures from monkey M1. They further argue that pretraining on randomized curl fields produces near-orthogonal learning vs. washout shifts, matching the geometry observed in macaques.

## Strengths
- **Effective action-distribution regularization.** The zeroness/smoothness KL penalties (Eq. 3) are a clean fix for the unbounded-acceleration pathology in RL-trained motor policies; the ablation in Fig. 2a–b shows peak acceleration saturating near ~2 m/s² and qualitatively matches monkey hand profiles (Fig. 2c). This is a useful methodological contribution independent of the neural claims.
- **Behavioral phenomena emerge from sparse reward alone.** With no trajectory supervision, the model produces the "overcompensated" curved reach (Fig. 2e–f) that is physically optimal under the curl field, and shows faster relearning than initial learning (Fig. 2g) — these are non-trivial qualitative replications of human/monkey findings.
- **The CF-pretraining → orthogonality result is reported honestly with the baseline failure.** §3.3 explicitly notes that the baseline model does *not* produce orthogonal learning/washout shifts, and only after CF pretraining does the orthogonality emerge (Fig. 4b). Acknowledging the negative baseline is good scientific practice.

## Weaknesses

### Fatal
None. The contributions are real, but several inferential supports are weaker than the paper claims.

### Major
- **The "uniform shift" claim relies on failure-to-reject with n=4 seeds.** Fig. 3g reports p=0.08 (one-sided Wilcoxon, n=4 seeds) and Fig. 4c reports p=0.38, and the paper interprets these non-significant tests as positive evidence that near and far shifts are *equivalent*. The text even concedes "near shifts are consistently larger than far shifts." With four seeds the test is severely underpowered, so non-rejection cannot be evidence of uniformity. Replication of this Sun et al. finding — one of the headline neural results — is not actually established by the reported statistics. Either an equivalence test (TOST) with adequate seed count, or significantly more seeds with a two-sided test, would be required.
- **The orthogonality / "prior experience" intervention confounds three changes at once.** §3.3.1 describes the CF-pretrained variant as differing from baseline by (i) randomized curl fields during pretraining, (ii) the curl coefficient k provided as an input, and (iii) k zeroed at test time, which induces an input-distribution shift between pretraining and learning. The paper attributes the orthogonality gain (Fig. 4b) to "structured dynamical motifs," but the result is equally consistent with a coefficient-conditioning representation or an input-zeroing artifact pushing activity into a previously-unused subspace. Without ablations isolating these factors (random CF without k input; k input without random CF; or pretraining on a different rich task) the mechanistic interpretation is post-hoc and not separated from confounds.
- **No quantitative neural-similarity metric.** All neural comparisons (Fig. 3b vs 3c, Fig. 3e vs 3f) are visual matches in TDR projections that are themselves fit on the model to be force-predictive. The discussion already concedes "future work could…quantify the similarity," but this means the present claims of matching M1 geometry rest on eyeballed 2D projections rather than CKA, Procrustes, regression, or similar. Some quantitative similarity score against the Sun et al. data is needed to justify the strength of the abstract's claims.

### Minor
- **The "RL is the natural choice" framing is asserted but not tested.** The intro and discussion repeatedly motivate RL over supervised learning because the monkey lacks demonstrations, but no SL/imitation-learning baseline is run. The same emergent overcompensated trajectories (Fig. 2e–f) plausibly emerge from any objective optimizing time-to-target under the perturbation. This does not invalidate the paper, but the framing overstates what the experiments support.
- **"Motor memory" via faster relearning is not separated from optimizer/weight state.** The paper does not control for whether the speed-up after washout reflects encoded memory in weights or simply incomplete weight washout / Adam moment carryover. A reset of optimizer state at washout end would isolate this.
- **TDR fitting protocol is under-specified.** §3.3 does not state clearly which trials/phase the TDR axes are fit on (pre-learning only? pooled?). Stability of a "force-predictive subspace" defined on pre-learning data is partly mechanical if learning-related variance lies outside those axes — the analysis needs to clarify this and ideally show stability under alternative subspace definitions.
- **No biomechanical plant.** The agent outputs accelerations directly to a cursor, with no muscles or joints. Comparing LSTM hidden-state geometry to motor-cortex preparatory activity, which is tied to muscle-force readout, is a meaningful abstraction that should be explicitly listed as a limitation.
- **Regularizer coefficients chosen by inspection.** α_smoothness = α_zeroness = 0.001 is selected "for approximate behavioral match" with no sensitivity sweep; downstream neural-geometry results may depend on this choice.

### Trivial
- §3.2 cites a single monkey reference for "qualitative resemblance" of acceleration profiles (Fig. 2c) without a quantitative comparison.

## Nice-to-Haves
- A representational-similarity comparison between baseline-pretrained and CF-pretrained latent states *before* the learning phase begins, to test whether the orthogonality gain comes from a state-space displacement induced by input zeroing.
- Per-seed (rather than averaged) trajectories and neural geometry plots, to expose variability across the four seeds.
- A supervised / behavioral-cloning baseline with the same neural-geometry analyses to substantiate the RL-vs-SL framing.

## Removed Points
*These points are flagged to be removed; treat them with caution.*
- Harsh critic's framing of issues 1–2 as "structural" / unfixable: the underlying critiques (low n, confounded intervention) are valid and kept above, but they are addressable by additional experiments rather than being intrinsic to the framework, so the paper's contribution is not invalidated.
- Strength Finder's "faithful task-environment implementation" and "robust curriculum-learning scheme" — accurate but generic; not load-bearing for the scientific claims.
- Demand for "complete training logs" / very large seed counts as reproducibility issues — covered above as a statistical-power concern (the substantive part), not as a reproducibility nitpick.

## Novel Insights
None beyond the paper's own contributions. The work's novel observation — that pretraining with randomized curl-field experience induces more orthogonal learning/washout shifts in RL-trained RNNs — is interesting if confounds can be ruled out, but the reviews surface no insight beyond what the paper itself proposes.

## Suggestions
- Replace one-sided non-significance tests for "uniformity" with an equivalence test (TOST) and increase seed count substantially (≥10–20).
- Run the ablation grid for CF-pretraining: {random CF, fixed k=0} × {k input, no k input}, plus a "rich but non-CF" pretraining condition, to disentangle which component drives the orthogonality gain.
- Add at least one quantitative neural-similarity metric (CKA, linear regression to recorded neurons, or Procrustes) against the Sun et al. (2022) data.
- Reset optimizer/critic state at the end of washout to test whether the relearning speed-up is weight-encoded vs. optimizer-encoded.
- Sweep α_smoothness, α_zeroness over at least an order of magnitude to confirm the neural-geometry findings are not artifacts of one regularization setting.
- Specify exactly what data the TDR axes are fit on, and (ideally) show stability under multiple subspace-identification choices.

---

**Evaluation along the requested axes.** *Originality:* Moderate — extending RL-trained RNNs to a specific motor-adaptation paradigm and testing prior-experience effects is a reasonable new combination, though the regularizers are the most original methodological piece. *Importance:* The question (mechanisms of motor memory in M1) is well-motivated and well-scoped to a known empirical target. *Support for claims:* Mixed — behavioral replications are convincing; the neural claims are weakened by n=4, mis-applied non-significance tests, eyeballed similarity, and confounded pretraining intervention. *Soundness of experiments:* Adequate for behavior, under-powered and under-controlled for the neural-geometry conclusions. *Clarity:* Generally good; the methods and figures are readable. *Value to community:* The regularization trick and the demonstration that some M1 phenomena emerge from sparse-reward RL are useful starting points; the orthogonality/pretraining hypothesis is interesting but not yet conclusively supported.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>