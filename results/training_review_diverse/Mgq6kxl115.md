Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper proposes Diffusion Bridge Networks (DBN), a method to approximate Deep Ensemble predictions at reduced inference cost. DBN trains a diffusion Schrödinger bridge (based on I2SB) that transports a single model's logit distribution directly to the ensemble-averaged logit distribution, then distills the multi-step diffusion into a single sampling step. On CIFAR-10, CIFAR-100, and TinyImageNet, DBN approaches or matches DE-3 performance with modest FLOPs overhead (1.166×), outperforming Bridge Network and standard ensemble distillation baselines.

## Strengths

- **Novel formulation.** DBN replaces BN's pairwise low-loss subspace curves with a single stochastic transport from one member's logit distribution to the full ensemble's logit distribution, avoiding quadratic growth in bridges. This is a principled re-framing of ensemble approximation as a conditional diffusion bridge problem (Section 3.2).

- **Empirically strong efficiency vs. quality trade-off.** DBN with a single bridge achieves near-DE-3 accuracy and NLL at 1.166× relative FLOPs, whereas BN at higher cost (1.411×) struggles to reach DE-2 (Table 1, Fig. 3). On TinyImageNet, DBN even surpasses DE-3 at less than half the computation.

- **Effective single-step distillation.** The paper adapts progressive distillation (Salimans & Ho) to reduce the multi-step diffusion bridge to a single function evaluation, making inference cost essentially one forward pass of the source model plus one lightweight score network evaluation (Section 3.3). This directly addresses the paper's core goal.

- **Thorough multi-metric evaluation.** Beyond accuracy, the paper reports NLL, Brier Score, ECE, and DEE, giving a more complete picture of uncertainty quality than many prior works in this area.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Constrained BN comparison in the main table.** The paper states "we assume the situation where both BN and DBN can utilize only a single source model to make the problem difficult" (Section 4.1). This constrains BN to a configuration it was not designed for (BN typically connects pairs of models via pairwise subspaces), giving DBN a structural advantage in this comparison. The paper is transparent about the constraint, and the trade-off analysis (Fig. 3) provides a fairer multi-bridge comparison where DBN still wins — so the claim is not invalidated. However, because the abstract and introduction draw on the main table results, the headline comparison is stronger than what a fully neutral setup would show. The authors should explicitly acknowledge this asymmetry when citing the main table results, or present a version of the main table where BN uses its natural multi-bridge configuration alongside the constrained one.

- **Missing distillation ablation.** The paper distills the 5-step diffusion bridge down to 1 step but provides no comparison with the non-distilled version (e.g., 5-step DBN). Without this ablation, the reader cannot assess how much approximation quality is sacrificed for speed, nor whether the diffusion process itself contributes meaningfully beyond the distillation trick (Section 3.3). A simple table or curve showing accuracy/NLL/ECE for non-distilled vs. distilled DBN would resolve this.

- **Poor ECE noted but not analyzed.** The paper reports that "interestingly DBN also shows poor ECE scores even with high performance in the other uncertainty metrics" (Section 4.1). For a method that claims to preserve ensemble uncertainty benefits, systematically poor calibration is a significant limitation. The paper offers no analysis (overconfidence vs. underconfidence, reliability diagrams, or even post-hoc temperature scaling experiments) to explain or mitigate this. This gap weakens the uncertainty quantification claims.

- **Unspecified $p_\text{temp}$ distribution.** The temperature-sampling distribution $p_\text{temp}$ is introduced as a critical design choice that makes the source stochastic and avoids trivial solutions (Section 3.2, Eq. 5). However, its exact form (e.g., uniform over which interval?) is never specified in the main text. This harms reproducibility and the paper would benefit from stating the distribution and showing sensitivity.

- **Underspecified "more refined version of END2."** The paper states it uses "a more refined version of END2" but provides no citation or description distinguishing this version from the original END2 (Section 4.1, Baseline methods). This makes the baseline comparison unreproducible.

### Trivial

- The capacity analysis (Fig. 2, right) shows DEE saturates at ~2.5 for a single DBN, meaning it never perfectly replicates DE-3. The paper honestly reports this ("slightly less than three ensembles"), but this honest limitation should also appear in the conclusion abstract discussion, not just the capacity section.

## Nice-to-Haves

- A comparison of total training overhead (GPU-hours or FLOPs) for DBN vs. BN, since the paper focuses entirely on inference cost but DBN requires training a score network and distillation for each bridge.
- Statistical significance measures (e.g., multiple random seeds with confidence intervals) for the main metrics, especially ECE and NLL where single-run results can be noisy.
- A limitations section that explicitly discusses the poor ECE and the need to know the exact ensemble composition at train time (the bridge is trained for a specific set of members).

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Insufficient justification of diffusion bridge formulation / I2SB assumptions not satisfied"** — REMOVED as factually incorrect. The reviewer claimed the I2SB Gaussian posterior (Eq. 4) might not hold for the paper's choice of boundary distributions. However, I2SB's tractability requires $p_0 = \delta_a$ (a Dirac delta), which holds in the paper because the target $Z_0$ is deterministic given the input and ensemble. The Gaussian posterior $q(Z_t|Z_0, Z_1)$ is a standard Brownian bridge property independent of the marginal distribution of $Z_1$ (which can be any distribution). The paper correctly explains why temperature sampling is needed to make $Z_1$ distributional (avoiding trivial solutions and satisfying the conditional distribution requirement).

2. **"I2SB section is dense and assumes prior knowledge"** — REMOVED as a generic presentation nitpick. The section provides a self-contained derivation with equations; background knowledge commensurate with the venue is reasonable.

3. **"Method never perfectly replicates DE-3"** — MOVED to Trivial. This is true but the paper is transparent about it. The reviewer even calls this "honesty."

4. **Various formatting/style nitpicks** from the section-by-section notes — REMOVED per hard rules.

## Novel Insights

The harsh critic identifies a genuinely important structural point: the paper's central comparison in Table 1 constrains BN to a single-source-model configuration that BN was never designed for. This is a real presentation weakness — the paper's headline claim is based on a comparison that advantages DBN by design. However, the critic overstates the severity: the paper is transparent about the constraint, and the trade-off analysis (Fig. 3) allows BN its natural multi-bridge configuration and still shows DBN winning. The critic's specific demand — "run BN in its standard multi-bridge configuration for 3 ensembles" — would be a constructive addition but does not invalidate the paper's contribution, since the trade-off analysis already shows DBN's advantage holds under fair comparison. The critic's other major claim (the I2SB theoretical grounding is insufficient) is simply wrong about what I2SB's tractability requires. The strength finder correctly identifies the paper's core innovations but is too generous in treating the I2SB foundation as "principled" without noting the gap in specifying $p_\text{temp}$.

## Suggestions

1. Add a distillation ablation table showing non-distilled (5-step) vs. distilled (1-step) DBN on at least one dataset.
2. Specify $p_\text{temp}$ explicitly and include a sensitivity analysis.
3. Add a brief analysis of the poor ECE: produce a reliability diagram, test post-hoc temperature scaling, and discuss whether the issue is inherent to the diffusion process or fixable.
4. Either add a version of the main table with BN in its multi-bridge configuration or explicitly caveat the single-source comparison when citing these results in the abstract/intro.
5. Provide a citation or description for the "more refined version of END2" used.

## Score and Decision

The paper proposes a genuinely novel application of diffusion bridges to ensemble approximation, with solid empirical results and efficient distillation. The core claims are supported. The main weaknesses — incomplete specification of $p_\text{temp}$, missing distillation ablation, unanalyzed poor ECE, and the constrained BN comparison — are all addressable in a revision and do not undermine the paper's overall contribution. Minor weaknesses outweigh the strengths only if one considers the constrained BN comparison fatal, which it is not (the paper is transparent, and the trade-off analysis validates the result under fairer conditions).

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>