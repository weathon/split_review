## Summary
This paper proposes a parametric family of reverse-time stochastic differential equations (SDEs) for Lévy-Itô diffusion models (LIMs). The key theoretical contribution is a family of SDEs (Eq. 11) indexed by a noise-level parameter η_t that yields exact marginal densities matching the forward diffusion — unlike the existing approximate reverse SDE (SDE-A) which drops an intractable data-dependent term. The work also provides a finite-variation argument explaining why SDE-A degrades at low NFE and why the proposed SDE-E can outperform it. Empirically, on CIFAR10, SDE-E achieves substantially better FID than both the approximate SDE (SDE-A) and the probability flow ODE when using few solver steps (e.g., 20-50) while maintaining sample diversity. A secondary TTS experiment on imbalanced data shows that LIM-based models can achieve higher speaker similarity than Gaussian-diffusion baselines, though with noted limitations. The paper is technically sound in its core theoretical derivation, but several empirical weaknesses — missing variance reporting, marginal imbalanced-data gains, a single rare-speaker TTS setup, and potential test-set tuning of η_t — limit the strength of the experimental conclusions.

## Strengths
1. **Clean theoretical derivation**: Theorem 1 and its proof (Appendix A) provide a correct and self-contained derivation of a parametric family of reverse SDEs for LIMs that preserve exact marginal densities. The proof is concise, leveraging fractional Fokker-Planck equations and the composability of fractional Laplacians, and the result cleanly generalizes the analogous family from Song et al. (2021a) to the α-stable setting.

2. **Well-motivated practical problem**: The paper identifies a genuine practical issue — the existing LIM reverse SDE (SDE-A) drops an intractable term dZ_t, which can cause significant degradation at low NFE. The finite-variation argument using compensated Gamma processes (Figure 3) provides an intuitive explanation for why this degradation occurs.

3. **Strong empirical gains at low NFE**: The CIFAR10 results (Table 1) demonstrate dramatic FID improvements of SDE-E over SDE-A in the low-NFE regime, especially for Euler-Maruyama at N=20 (e.g., 8.79 vs 144.7 for α=1.8). This validates the core hypothesis that the proposed exact SDE family is beneficial when solver steps are limited.

4. **Diversity analysis**: The paper explicitly verifies that the improved FID from SDE-E does not come at the cost of sample diversity (Table 2), addressing a common concern with noise-reduced sampling in diffusion models.

5. **Open-science honesty**: The authors candidly discuss limitations (η_t tuning burden, open question of dZ_t estimation) and acknowledge challenges in the TTS experiments (pronunciation inaccuracies), which improves the paper's scientific credibility.

## Weaknesses
1. **Missing statistical significance reporting**: None of the experimental results include variance, confidence intervals, or significance tests. FID and coverage values are reported as point estimates. For the imbalanced CIFAR10 experiment where the gap is only 0.34 FID (18.10 vs 18.44), this makes it impossible to assess whether SDE-E is actually better than SDE-A. Even for the main CIFAR10 results where some gaps are large, standard deviations would strengthen reproducibility.

2. **η_t hyperparameter selection on test set**: The paper states η_t was chosen "as showing the best performance in terms of FID on CIFAR10 test set." This constitutes tuning on the test set, which can lead to over-optimistic FID estimates. A separate validation split should have been used.

3. **Modest imbalanced-data improvement**: On imbalanced CIFAR10, SDE-E's FID improvement over SDE-A is only 0.34 — marginal compared to the gains on balanced CIFAR10. The claim that SDE-E "still outperforms baseline methods" is technically correct but the practical significance of such a small gap is questionable, especially without variance.

4. **Single rare-speaker TTS evaluation**: The TTS experiment uses only one rare speaker (male, 10 minutes), and the authors acknowledge pronunciation inaccuracies across all models. The claimed "advantages over standard diffusion models" are based solely on speaker similarity scores, without quality/intelligibility metrics. This limits the generalizability of the TTS claims.

5. **No SDE-E evaluation on TTS**: Despite the paper's core contribution being the parametric SDE family (SDE-E), the TTS experiments only use the ODE solver. This is a missed opportunity to demonstrate the method's benefit in the speech domain.

6. **Storyline misalignment**: The introduction foregrounds "imbalanced datasets" as the core motivation, but the paper's main contribution is about exact sampling at low NFE for balanced data. The imbalanced-data narrative and sampling-improvement narrative compete rather than reinforce each other.

7. **Related work reads as a list**: The related work section catalogs prior methods chronologically rather than organizing them around comparison axes. Missing explicit differentiation from alternative noise distributions (Gamma, heavy-tailed Langevin) and from TTS diffusion models for speaker imbalance.

## Key Issues
**Key Issue 1: Missing variance/statistical reliability** (Severity: Major, Page 7 - Experiments)

The most critical experimental weakness is the complete absence of variance reporting. FID and coverage values are reported as single numbers without standard deviations, confidence intervals, or significance tests. The imbalanced CIFAR10 evaluation averages 5 runs but does not report per-run variation. Given that FID improvements in the balanced setting are often small (e.g., EI-20 for α=1.8: SDE-E 6.86 vs ODE 10.31 — a gap that could shift with one outlier seed), the reader cannot assess statistical reliability.

*Impact*: Without variance, the claimed improvements are not verifiable as statistically significant, weakening the paper's main empirical evidence.

*Required action*: Report mean ± std over at least 3 independent seeds (with different random seeds) for all experimental conditions in Tables 1-3.

---

**Key Issue 2: Test-set hyperparameter tuning of η_t** (Severity: Major, Page 7 - Experiments)

The η_t parameters are selected based on "showing the best performance in terms of FID on CIFAR10 test set." This is test-set leakage that can lead to over-optimistic performance estimates. Since η_t controls the noise schedule and is a key component of the proposed method, its selection procedure must be rigorous.

*Impact*: The reported FID values for SDE-E may be biased upward (i.e., better than would be achieved with an honestly held-out validation set).

*Required action*: Clarify whether a validation split of CIFAR10 (separate from the 10k test set) was used for η_t selection. If not, either re-run with proper validation-based selection or explicitly acknowledge this as a limitation and estimate the potential bias.

---

**Key Issue 3: Modest imbalanced-data gain and overclaiming** (Severity: Major, Pages 8-9 - Imbalanced CIFAR10 & TTS)

The imbalanced CIFAR10 improvement (0.34 FID) and the TTS results (single rare speaker, pronunciation issues) constitute the weakest empirical support in the paper. The claim in the abstract that LIMs "may have advantages over standard diffusion models on highly imbalanced datasets" is supported only by the TTS experiment with noted pronunciation problems and a marginal imbalanced CIFAR10 gain.

*Impact*: The TTS/application contribution (C3) is significantly weaker than C1-C2 and may mislead readers about the practical impact of the proposed method on imbalanced data.

*Required action*: Either (a) add statistically rigorous imbalanced-data experiments with multiple runs and multiple rare speakers in TTS, or (b) downgrade C3 from a core contribution to an exploratory study and adjust the abstract/conclusion accordingly.

---

**Key Issue 4: Storyline and motivation mismatch** (Severity: Moderate, Pages 1-2 - Introduction)

The introduction motivates the paper primarily through the problem of imbalanced data, but the paper's main contribution is about achieving exact reverse SDEs for LIMs at low NFE. These are largely independent contributions — the imbalanced-data benefit comes from using α-stable noise (inherited from Yoon et al., 2023), not from the proposed parametric SDE family.

*Impact*: Reader confusion about what the paper actually contributes. The first two paragraphs of the introduction create expectations that the experiments only partially address.

*Required action*: Restructure the introduction to lead with the exact-sampling problem (the paper's true focus), then mention imbalanced data as a secondary application domain.

---

**Key Issue 5: Incomplete related-work positioning** (Severity: Moderate, Page 3 - Related Work)

The related work section catalogs prior methods without organizing them into comparison axes. Missing is a clear statement of how the proposed η_t-controlled family differs from existing noise-reduction methods in Gaussian diffusion (e.g., DDIM, DPM-Solver, Analytic-DPM). Are these complementary or competing approaches?

*Impact*: The novelty claim is harder to evaluate because the precise technical differences from existing sampling efficiency methods are not articulated.

*Required action*: Add a comparison paragraph explicitly stating: (1) how the proposed SDE family generalizes to LIMs what Song et al. (2021a) did for Gaussian diffusion, and (2) why the η_t parameter is different from variance-reduction schedules in analytic DPM or exponential integrators.

## Actionable Suggestions
**S1 (Must): Add variance reporting for all experiments**
Report FID, coverage, and speaker similarity as mean ± standard deviation over at least 3 seeds with different random seeds. For the imbalanced CIFAR10 experiment (5 runs already done), report the per-run FID values and the standard deviation. This is a low-effort, high-impact fix that directly addresses the most critical weakness.

**S2 (Must): Clarify η_t selection protocol**
Add a sentence specifying whether η_t was tuned on a held-out validation subset or on the CIFAR10 test set. If tuned on the test set, either re-run experiments with a proper validation split (e.g., hold out 5k images from training set) or add a note estimating the potential over-optimism. Also report the η_t schedules actually used for each experimental condition in a more transparent format.

**S3 (Must): Restructure introduction narrative**
Move the imbalanced-data motivation to a secondary position. The introduction should lead with: (1) LIM reverse SDEs are inexact due to the dropped dZ_t term → (2) This causes degradation at low NFE → (3) We derive exact parametric reverse SDEs → (4) Experiments show gains on image generation at low NFE → (5) Secondary: LIMs are also applicable to TTS on imbalanced data.

**S4 (Nice-to-have): Strengthen imbalanced-data experiments**
For the imbalanced CIFAR10 experiment, replace the single-run-setup with at least 5 independent training runs from different initializations, each evaluated with the same η_t schedule. Report per-class FID in addition to coverage. For the TTS experiment, either (a) add at least 2-3 additional rare speakers, or (b) explicitly reframe as a preliminary case study and remove from core contributions.

**S5 (Nice-to-have): Add SDE-E evaluation for TTS**
Run the TTS experiments with SDE-E sampling (the proposed method) in addition to the ODE. This would demonstrate the paper's core contribution in a second domain. Use the best η_t schedule found from CIFAR10 (tuned to a small TTS validation set) as a starting point.

**S6 (Nice-to-have): Add explicit a_t and γ_t formulas**
Provide the analytical forms of a_t and γ_t for the specific VP-type forward SDE used in experiments. This improves reproducibility and helps readers connect the theoretical score-matching objective (Eq. 6-8) to actual implementation.

**S7 (Nice-to-have): Acknowledge finite-variation argument limitations**
Add a sentence acknowledging that the compensated Gamma process analogy is heuristic, and that a rigorous bound on the dZ_t omission error is future work, as suggested in the annotation on Page 6.

**S8 (Nice-to-have): Restructure related-work section**
Organize related work by three thematic axes: (1) Non-Gaussian noise in generative models (with explicit comparisons to Nachmani et al. 2021 and Deasy et al. 2022), (2) Sampling efficiency for diffusion models (positioning this paper's contribution as a generalization of Song et al. 2021a to LIMs), (3) TTS with diffusion models for speaker-conditional generation.

## Storyline Options + Writing Outlines
## Storyline Analysis

The current introduction has a misalignment: it emphasizes "imbalanced datasets" as the primary motivation, but the paper's core theoretical contribution is about exact reverse SDE sampling. This creates reader expectation that the main experiments will focus on imbalanced data, when in fact the strongest results are on balanced CIFAR10.

### Proposed Storyline: "Sampling-First" (Recommended)

This storyline leads with the exact-sampling problem and positions imbalanced-data applications as a secondary validation.

**Abstract Outline (S1-S5):**
- **S1 (Problem)**: LIMs extend diffusion models to α-stable noise and improve performance on imbalanced data, but their sampling algorithm uses an approximate reverse SDE.
- **S2 (Gap)**: The approximation error from dropping the intractable dZ_t term can be significant when solver steps are limited, unlike Gaussian diffusion where both SDE and ODE solvers are exact.
- **S3 (Solution)**: We derive a parametric family of reverse SDEs for LIMs that preserve exact marginal densities, controlled by a noise-level parameter η_t.
- **S4 (Key Result)**: On CIFAR10, the proposed SDEs improve FID by up to 3.5 points at 20 solver steps without sacrificing diversity.
- **S5 (Secondary Result)**: We also demonstrate that LIMs extend to text-to-speech on imbalanced data, achieving higher speaker similarity than Gaussian-diffusion baselines.

**Introduction Outline (P1-P5):**

**P1 — Domain and Efficiency Challenge** (revised):
"Denoising diffusion models are powerful but require many steps. A large body of work addresses this through better solvers and distillation. However, a distinct challenge arises in Lévy-Itô diffusion models (LIMs), which replace Gaussian noise with α-stable noise to improve performance on imbalanced data."

**P2 — The Exactness Gap in LIMs** (new emphasis):
"Unlike Gaussian diffusion where both the reverse SDE and probability flow ODE are exact, the reverse SDE used for LIMs in practice (Yoon et al., 2023) drops an intractable data-dependent term dZ_t. This yields an approximation that can significantly degrade sample quality when the number of function evaluations is small."

**P3 — Proposed Solution** (current P2 restructured):
"We bridge this gap by deriving a parametric family of reverse SDEs (Theorem 1) whose solutions have the same marginal densities as the forward process, analogous to Song et al. (2021a) for Gaussian diffusion. The family is indexed by a noise parameter η_t that controls the amount of α-stable noise added at each reverse step."

**P4 — Application to Speech** (current P3, condensed):
"As a secondary investigation, we apply LIMs to text-to-speech on highly imbalanced speaker data, evaluating whether the heavy-tailed noise properties that benefit imbalanced image generation transfer to the speech domain."

**P5 — Contributions** (unchanged, but reorder C3 to last and qualify):
"1) A parametric family of exact reverse SDEs for LIMs. 2) Empirical demonstration of improved image generation at low NFE without diversity loss. 3) A preliminary study of LIM-based TTS on imbalanced data, warranting further investigation."

### Alternative Storyline 2: "Unified Framework"
If the paper wants to keep imbalanced data as co-primary, the title and contributions should be restructured to emphasize the dual contribution equally: "Exact Sampling and Imbalanced-Data Applications of Lévy-Itô Diffusion Models." This would require stronger imbalanced-data experiments to match the claim level.

### Alternative Storyline 3: "TTS-Focused"
Reframe the paper around a problem statement about speaker imbalance in TTS, introduce LIMs as the solution, then present the parametric SDE as an enabling technology for efficient TTS sampling. This would require major rewriting of the introduction, method, and experiments to center on TTS.

**Recommendation:** Use Storyline 1 ("Sampling-First") as it aligns best with the paper's strongest evidence (CIFAR10 image generation) and correctly positions the TTS contribution as preliminary.

## Priority Revision Plan
### P0 — Publication-Critical (Must fix before acceptance)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P0 | Missing variance/statistics (Key Issue 1) | Add std dev over ≥3 seeds to all tables | Establishes statistical credibility of FID/diversity claims | Low (re-run inference) |
| P0 | η_t selection on test set (Key Issue 2) | Clarify protocol or re-run with validation split | Prevents over-optimistic FID estimates | Low-Medium |
| P0 | Introduction narrative mismatch (Key Issue 4) | Restructure intro per Storyline 1 (Sampling-First) | Aligns reader expectations with actual contributions | Low (text revision) |

### P1 — High Impact (Significantly strengthens paper)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P1 | Imbalanced CIFAR10 uncertainty (Key Issue 3) | Add run-level variance and discuss practical significance | Clarifies whether 0.34 FID gain is meaningful | Low (already have 5 runs) |
| P1 | Related-work structure (Weakness 7) | Reorganize by thematic axes with explicit differentiation | Improves novelty positioning | Medium |
| P1 | Missing a_t, γ_t formulas (from annotation on Page 5) | Provide analytical forms for VP-type schedule | Enables reproducibility | Low |

### P2 — Quality Improvement (Nice-to-have)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P2 | SDE-E evaluation on TTS | Run TTS with SDE-E sampler | Demonstrates core method in second domain | Medium |
| P2 | Multiple rare speakers in TTS | Add 2-3 additional rare speakers | Strengthens C3 generalizability | High |
| P2 | Finite-variation argument caveat (annotation Page 6) | Add heuristic acknowledgement sentence | Improves theoretical honesty | Low |

### Revision Workflow

1. **Week 1**: Fix P0 items — add variance (re-run inference with 3 seeds), clarify η_t selection protocol in text, restructure introduction.
2. **Week 2**: Fix P1 items — compute and report imbalanced CIFAR10 variance, restructure related work, add a_t/γ_t formulas to appendix.
3. **Week 3** (optional): P2 items — TTS SDE-E evaluation, additional rare speakers if resources permit.

## Experiment Inventory & Research Experiment Plan
| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|---------------------------------------|---------|--------------|-----------------|-------------------|
| E1 | Evaluate SDE-E vs SDE-A vs ODE on balanced CIFAR10 | CIFAR10, NCSN++(deep), 3 α values (1.8/1.5/1.2), EM and EI solvers, N ∈ {20,50,500} | FID (Table 1), Coverage (Table 2) | SDE-E best FID at low NFE; diversity maintained | C1, C2 | No variance reported; η_t tuned on test set |
| E2 | Evaluate SDE-E on imbalanced CIFAR10 | Imbalanced CIFAR10 (5000→50 per class), α=1.8, EI-20, 5 runs averaged | FID, Coverage (Tables 3, 4) | SDE-E marginally better (0.34 FID gain) | C2 (partial) | Very small gain; no variance from 5 runs; single α value |
| E3 | LIM-based TTS on imbalanced speaker data | Grad-TTS-like model, 2 speakers (1000 min female, 10 min male), Gaussian vs α=1.8 vs α=1.5, ODE solver only | Speaker similarity (CAM++, Table 5) | α-stable models outperform Gaussian; α=1.5 best | C3 (preliminary) | Single rare speaker; pronunciation issues; no SDE-E tested; no quality/intelligibility metrics |

### Research-Theme Gap Diagnosis

- **New knowledge (Sampling)**: The parametric SDE family is a meaningful theoretical contribution. The proof is sound and the extension of Song et al. (2021a) to LIMs is novel. **Supported** by E1.
- **New knowledge (Imbalanced data)**: The paper adds marginal evidence (0.34 FID gain) but does not convincingly show that the proposed SDE-E improves imbalanced-data generation more than SDE-A or ODE. **Weakly supported**.
- **Reproducibility**: Several experimental details (a_t, γ_t schedules explicit formulas, full η_t schedules per condition) are deferred to appendices but some are implicit. The missing variance reporting reduces reproducibility of claimed improvements. **Partially supported**.
- **Impact on practice**: The TTS results are too preliminary to change practice. The image generation results are stronger but limited to CIFAR10. **Partially supported**.

### Proposed Research Experiments (P0/P1/P2)

**Exp-R1 (P0): Variance quantification for balanced CIFAR10**
- Target Claim: C2 — SDE-E outperforms SDE-A/ODE at low NFE
- Hypothesis: The FID improvements are statistically significant
- Minimal Design: Re-run Table 1 configurations with 3 seeds each (different random seeds, same hyperparameters). Compute mean ± std FID and coverage.
- Controls/Baselines: Same as Table 1 (SDE-A, ODE, SDE-E)
- Metrics: FID, Coverage
- Success Criterion: SDE-E improvement over SDE-A/ODE > 2× the pooled standard deviation for each condition
- Estimated Cost: ~3× current inference cost (low)
- Expected Gain: Converts all main FID claims from point estimates to statistically grounded results

**Exp-R2 (P1): Imbalanced CIFAR10 with proper η_t selection**
- Target Claim: C2 (imbalanced setting) — SDE-E outperforms SDE-A on imbalanced data
- Hypothesis: With properly tuned η_t on a validation set, SDE-E shows a meaningful FID improvement
- Minimal Design: Split the 50k imbalanced training set into 45k train + 5k validation. Tune η_t on validation. Train 3 independent models with different seeds.
- Controls/Baselines: SDE-A, ODE with same training
- Metrics: FID, per-class coverage, per-class FID
- Success Criterion: Statistically significant FID improvement (p<0.05 via paired bootstrap) over SDE-A
- Estimated Cost: ~1-2 GPU-days per seed
- Expected Gain: Stronger evidence for imbalanced-data claims OR honest acknowledgement if gain is not significant

**Exp-R3 (P2): SDE-E on TTS**
- Target Claim: C1 (method generality) — the parametric SDE family is beneficial across domains
- Hypothesis: SDE-E improves TTS quality at low NFE compared to ODE
- Minimal Design: Generate speech with SDE-E at N=10,20,30 using η_t schedules adapted from CIFAR10 (tuned on a small TTS validation set). Compare to ODE at same NFE.
- Controls/Baselines: ODE (current results in Table 5)
- Metrics: Speaker similarity (CAM++), Mel-Cepstral Distortion (MCD), or WER from ASR
- Success Criterion: SDE-E achieves comparable or better speaker similarity than ODE at lower NFE
- Estimated Cost: ~1-2 GPU-days
- Expected Gain: Demonstrates method generality; strengthens C1; may make C3 more impactful

**Exp-R4 (P2): Additional rare speakers in TTS**
- Target Claim: C3 — LIMs benefit rare speakers in TTS
- Hypothesis: The speaker similarity advantage of α-stable noise holds across multiple rare speakers
- Minimal Design: Add 2-3 additional rare speakers (5-15 min each) from a multi-speaker dataset. Train with same protocol.
- Controls/Baselines: Gaussian noise baseline
- Metrics: Speaker similarity, pronunciation accuracy (WER)
- Success Criterion: Consistent speaker similarity improvement across all rare speakers
- Estimated Cost: ~3-5 GPU-days (new training runs)
- Expected Gain: Transforms C3 from a single-case study to a generalizable finding

```text
ASCII Diagram — Experiment Upgrade Plan
Stage 1 (P0 — week 1):
  [E1: add variance] -> [statistically grounded FID claims]
Stage 2 (P1 — week 2):
  [E2: proper η_t tuning] -> [solid or honestly bounded imbalanced-data claims]
  [Exp-R2: 3-seed training] -> [imbalanced data significance test]
Stage 3 (P2 — week 3+):
  [Exp-R3: SDE-E on TTS] -> [method generality demonstrated]
  [Exp-R4: more rare speakers] -> [C3 generalizability]
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

*Justification:*
The paper makes a solid theoretical contribution (parametric family of exact reverse SDEs for LIMs, with a clean proof) and shows convincing empirical gains on balanced CIFAR10 at low NFE. However, the score is constrained by:
- **Missing statistical rigor** (no variance reporting, test-set η_t tuning) weakens confidence in quantitative claims.
- **The imbalanced-data and TTS contributions (C3)** are exploratory rather than definitive, with marginal gains and a single-speaker setup.
- **Storyline misalignment** between the imbalanced-data motivation and the sampling-improvement core contribution.
- **Novelty cannot be fully adjudicated** without external literature verification (Retrieval-Disabled Mode active for this run).

The theoretical contribution (C1) is the strongest aspect; the empirical methodology (C2) has good signal but needs statistical grounding; the application extension (C3) is the weakest contribution.

**Post-Revision Target: [7.5, 8.0] / 10**

*Justification:*
If the authors fully address the P0 and P1 items (add variance reporting, clarify η_t selection protocol, restructure introduction narrative, add a_t/γ_t formulas), the paper would achieve a score of approximately 7.5-8.0. The upper bound assumes that the variance reporting confirms the claimed FID improvements and that the imbalanced-data experiments are either strengthened or honestly bounded. The theoretical contribution remains the strongest pillar regardless of experimental improvements.

| Scoring Dimension | Current Score (out of 10) | Post-Revision Target |
|-------------------|--------------------------|---------------------|
| Research Value / Significance | 6.5 | 7.5 |
| Novelty | 6.5 (provisional — external verification deferred) | 7.0 |
| Validity / Soundness | 6.0 | 7.5 |
| Reproducibility | 6.0 | 8.0 |
| Overall | 6.5 | 7.5-8.0 |