Now let me write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal

### Major
...

### Minor
...

### Trivial
...

## Nice-to-Haves
- suggestion that would improve but is not a core flaw

## Removed Points
...

## Novel Insights
One paragraph synthesizing genuinely novel observations.

## Suggestions
- specific actionable suggestion

## Score and Decision

**Calibration Anchors (All Rounds)**

**Round 1 (Bracketing):**
- iSSM (FwW3jqchtY) — avg 5.00 — Very similar paper on interventional state space models for causal neural dynamics; also had weak baselines and strong assumptions, but had real perturbation data. Our paper is comparable.
- BRAID (3usdM1AuI3) — avg 6.25 — Stronger paper with comprehensive baselines, ablation studies, and clean evaluation. Our paper is weaker.
- MRINE (eR1119aUlL) — avg 4.25 — Similar in being a combination of techniques with limited experiments. Our paper is slightly stronger.
- MR-SDS (WQwV7Y8qwa) — avg 5.80 — Stronger validation with real multi-region neural data and baselines. Our paper is weaker.
- Spectral Learning (wCUw8t63vH) — avg 6.80 — Clean analytical method paper with strong theoretical contribution. Our paper is weaker.

**Round 2 (Narrowing within bracket 4.0–6.5):**
- Closed-loop EEG (4ltiMYgJo9) — avg 5.75 — Another closed-loop stimulation framework tested offline; similar weaknesses but slightly better reception. Our paper is slightly weaker.
- Nonparametric Covariance Regression (PdZkfSttGK) — avg 5.25 — Nonparametric method for neural data; similar scope of contribution. Our paper is comparable.
- Neural Manifold Regularization (TVnkjz4MqV) — avg 5.50 — Neural latent dynamics method with moderate validation. Our paper is slightly weaker.
- Time-Dependent VAE (N83O2FcqzN) — avg 5.00 — Neural latent variable model. Our paper is comparable.

**Round 1 bracket:** (4.0, 6.0). Based on comparison with these anchors, particularly the strong similarity to iSSM (5.00) and the weaker validation compared to papers that scored 5.5+, the paper falls at the lower end of this bracket.

**Final score: 5.0** — The paper presents a well-motivated framework with several novel components (sjPCA, temporal kernel discounting, constrained optimization) and demonstrates real-time feasibility. However, the central claims are undermined by: (1) the "real data" experiments using simulated (AR(1)-modeled) rather than real stimulation effects, (2) trivial baselines that do not establish competitiveness against existing methods, and (3) the absence of ablation studies isolating component contributions. The contributions are real but the validation does not match the strength of the claims.