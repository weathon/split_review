## Summary

TabDiff proposes a joint continuous-time diffusion framework for tabular data generation that handles numerical and categorical features in their native types. The core technical contribution is feature-wise learnable noise schedules (power-mean for numerical, log-linear for categorical) designed to address the high heterogeneity of column-wise distributions. The model also introduces a restart-based stochastic sampler and classifier-free guidance for conditional imputation. Experiments across seven datasets and eight metrics show consistent improvements over prior methods, with notably strong gains on column-pair correlation (Trend, +22.6% over TabSyn).

## Strengths

- **Feature-wise learnable noise schedules that explicitly address column heterogeneity**: Unlike prior tabular diffusion models that use a single shared noise schedule across all columns, TabDiff introduces per-feature learnable schedules via power-mean parameters ρ_i for numerical features (Eq. 7, Section 2.3) and log-linear parameters k_j for categorical features (Eq. 8, Section 2.3). The ablation (Table 6) validates this design: the learnable variant consistently beats the fixed variant under both deterministic and stochastic samplers (e.g., 1.17 vs. 1.24 on Shape), and Figure 6 shows learnable schedules reduce both numerical and categorical training losses.

- **Continuous-time joint diffusion operating directly on native data types without encoding overhead**: Prior work either used discrete-time diffusion (TabDDPM, CoDi), yielding a looser ELBO, or transformed features into a latent continuous space via autoencoders (TabSyn), incurring encoding overhead. TabDiff defines a continuous-time hybrid diffusion process—Gaussian SDE for numerical features (Eqs. 3–4) and masked diffusion for categorical features (Eqs. 5–6)—and optimizes the continuous-time ELBO (Eq. 9) directly in the original data space. This is a principled architectural improvement over both approaches.

- **Consistent empirical gains across 7 datasets and 8 metrics**: TabDiff achieves the best or second-best performance on nearly every dataset-metric combination, with particularly strong margins on Trend (+22.6% over TabSyn, Table 2) and on the categorical-heavy Diabetes dataset (+46.39% on Shape, +37.3% on Trend, Tables 1–2). The method also achieves the best average MLE gap (5.76%, Table 3), outperforming TabSyn (6.78%).

- **Stochastic sampler with demonstrated error-correction benefit**: The restart-based backward stochastic sampler (Algorithm 2, Section 2.4), adapted from EDM/restart sampling to the multi-modal tabular setting, consistently improves both Shape and Trend over the deterministic sampler under both fixed and learnable schedules in the ablation (Table 6), confirming its effectiveness in reducing accumulated decoding errors.

## Weaknesses

### Major

- **Uneven baseline evaluation weakens confidence in comparative claims**: The vast majority of baseline results are not re-run by the authors. The table notes state the following explicitly: *"TabSyn's performance is obtained via our reproduction. The results of other baselines except on Diabetes, are taken from Zhang et al. (2024)"* — meaning CTGAN, TVAE, GOGGLE, GReaT, STaSy, CoDi, and TabDDPM results across six of seven datasets are copied from the TabSyn paper's tables, not generated in the same environment. This pits TabDiff (run in the authors' pipeline, with their hyperparameter choices and compute budget) against baselines run in someone else's experimental pipeline, where preprocessing, evaluation code, random seeds, and tuning protocols can differ systematically. The most concerning case is TabDDPM's extreme Shape outliers on News (78.75) and Diabetes (31.44) — these are taken as-is without commentary on whether they reflect a genuine failure or a configuration mismatch. This does **not** invalidate the contribution (TabSyn, the strongest prior competitor, was reproduced and TabDiff beats it), but it weakens the headline claim of *"superior average performance over existing competitive baselines across all eight metrics."* A proper head-to-head re-run of at least the top-3 competing methods in a unified codebase would resolve this.

### Minor

- **Transformer architecture is critically underspecified**: The paper states the model is "parameterized by a transformer handling different input types" (Sections 1 and 2.1) but provides zero architectural details — no depth, width, attention mechanism, how numerical and categorical embeddings are fused, or positional encoding scheme. For a method whose main novelty relies on a joint denoising network, this is a meaningful reproducibility gap.

- **Ablation study lacks granularity**: The ablation (Table 6) reports only global averages across 7 datasets with no per-dataset breakdown, uses only Shape/Trend (omitting other metrics), and does not isolate the two schedule families (e.g., learnable numerical only vs. learnable categorical only) to determine which modality drives the gain.

- **Paper undermines its own MLE metric**: Section 4.3 states: *"methods with varying performance on data fidelity metrics might have very close MLE scores. This suggests that the MLE score evaluated under the current setting may not be a reliable indicator of data quality."* Yet MLE is one of the eight metrics across which the paper claims superiority. If the metric is unreliable, it should not be counted as evidence. This is a minor self-contradiction.

- **CFG imputation uses asymmetric model capacity**: For the unconditional path within TabDiff's CFG imputation (Section 4.4), the paper states it uses *"a significantly smaller denoising network."* Since TabSyn's model size is not described, it is unclear whether the CFG improvement (ω=0.6 vs. ω=0.0) comes from the guidance mechanism or from capacity differences between the conditional and unconditional networks.

- **"Unified CFG framework" overstates novelty**: The CFG derivation (Eqs. 11–12) follows the standard Ho & Salimans (2022) classifier-free guidance. The categorical extension (Eq. 13) is a straightforward application of log-probability interpolation to the discrete categorical posterior. This is a useful adaptation but not a new framework.

### Trivial

- **Dataset listing error**: The paper states *"seven real-world tabular datasets"* but lists eight names: Adult, Default, Shoppers, Magic, Faults, Beijing, News, and Diabetes (line 251). "Faults" never appears in any experiment table.

## Nice-to-Haves

- Run a clean head-to-head with at least the top-3 baselines (TabSyn, TabDDPM, STaSy) in the same codebase to eliminate pipeline-confounding concerns.
- Provide per-dataset ablations for the learnable schedules and show the learned parameter values (ρ_i, k_j) for a concrete dataset to make the mechanism interpretable.
- Report the unconditional model size used in CFG imputation to clarify the capacity asymmetry.

## Removed Points

The following points raised in reviewer inputs are removed after verification against the paper:

- **OOM entries distorting aggregate comparisons** (removed: factually incorrect). The harsh critic claimed OOM entries are "included in the average computation" and methods are "scored as if they had infinite error." Inspection of the tables shows the opposite: GReaT Shape average (14.20) is computed over 5 datasets excluding OOM entries on News and Diabetes; STaSy Shape average (7.72) is over 6 datasets excluding OOM on Diabetes. OOM entries are excluded from averages, not included. TabDDPM's outlier values of 78.75 and 31.44 are real results, not OOM artifacts, and the concern about these belongs under the evaluation-asymmetry issue (whether they are genuine or configuration artifacts), not as a separate OOM-distortion claim.

## Novel Insights

None beyond the paper's own contributions. The reviews surface well-known tensions in ML benchmarking (copied baselines, underspecified architectures, metric reliability) without producing a novel observation about the method or the problem.

## Suggestions

1. Re-run the top competitive baselines (TabSyn, TabDDPM, STaSy) in a unified codebase on a subset of datasets to validate the main comparison.
2. Provide transformer architecture details in the main text or a public code release — at minimum depth, width, embedding dimension, and the fusion mechanism for numerical/categorical features.
3. Add per-dataset ablation results and an ablation isolating numerical-only and categorical-only learnable schedules.
4. Fix the dataset listing error (line 251) and clarify which datasets appear in which tables.
5. Frame the CFG contribution as an adaptation rather than a "unified CFG framework" and report the unconditional model size used in imputation.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>