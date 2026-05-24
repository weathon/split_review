Now I have sufficient calibration data. Let me synthesize the final review.

## Summary

This paper identifies the "copy-paste artifact" in identity-consistent image generation — where models replicate the reference face rather than preserving identity across natural variations — and makes three substantial contributions: **MultiID-2M** (a large-scale paired dataset of 500k group photos with multiple references per identity), **MultiID-Bench** (a benchmark with a novel copy-paste metric M_CP that quantifies bias toward the reference vs. ground truth), and **WithAnyone** (a diffusion-based model with a GT-aligned ID loss, a contrastive ID loss with extended negatives, and a four-phase training pipeline that leverages paired data). On multi-person scenes, WithAnyone achieves the best identity fidelity among ID-specific models with the lowest copy-paste, demonstrably breaking the trade-off curve that all other methods follow. The paper is well-written, the technical components are cleanly motivated and ablated, and the project is fully open-sourced.

## Strengths

- **Formal definition and metric for the copy-paste artifact.** Section 4 introduces M_CP (Eq. 2), which captures a generated image's relative bias toward the reference vs. ground truth — moving beyond Sim_Ref, which inadvertently rewards direct copying. Figure 2 provides both a conceptual illustration and empirical density plots showing how existing models (e.g., InstantID) peak at near-perfect similarity to the reference while real image pairs have a broad distribution. This is a genuine conceptual contribution.

- **MultiID-2M dataset and MultiID-Bench benchmark.** The four-stage data pipeline (Section 3) produces 500k paired group photos with ~400 references per identity for ~3k identities, plus 1.5M unlabeled images. MultiID-Bench (Section 4) provides a standardized evaluation protocol with Sim_GT as the primary metric and M_CP as a novel diagnostic. Table 1 reports results across 12 baselines, enabling systematic comparison. This fills a real data gap in multi-ID generation research.

- **Breaking the identity-fidelity vs. copy-paste trade-off.** Table 1 shows WithAnyone achieves the lowest copy-paste score (0.144) among all methods on the single-person subset while maintaining the second-highest Sim_GT (0.460, within 1% of the best). Figure 5 shows WithAnyone deviating substantially from the regression curve that all other methods follow — it attains high similarity without the usual copy-paste penalty.

- **Well-ablated technical contributions.** The GT-aligned ID loss (Eq. 4) avoids noisy landmark extraction from generated images and enables ID supervision across all noise levels. The ID contrastive loss (Eq. 5) leverages the large reference bank for 4096 negatives per sample. The four-phase training pipeline (Section 5.2) is a sensible progression from reconstruction to controllable generation. Table 3 confirms each component's contribution: removing Phase 3 increases copy-paste from 0.161→0.239, removing extended negatives drops Sim_GT from 0.405→0.368, and removing GT-alignment drops Sim_GT to 0.385.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Abstract marginally overstates single-person results.** The abstract claims WithAnyone "maintains state-of-the-art identity similarity" without qualification. On the single-person subset (Table 1), WithAnyone achieves Sim_GT=0.460 vs. InstantID's 0.464 — second place, not first. The claim is accurate for multi-person subsets (Table 2), where WithAnyone achieves the highest Sim_GT, and the gap on single-person is only ~1%, but the abstract should either qualify the scope or use more precise language.

- **User study has a labeling error and is undersized for strong claims.** Figure 8 labels the method as "Cure" instead of "WithAnyone," a copy-paste artifact that undermines confidence in careful execution. With only 10 participants, no confidence intervals or inter-rater agreement metrics are reported. While the study directionally supports the automated metrics, these issues weaken its evidentiary weight.

- **No confidence intervals on main quantitative results.** Tables 1 and 2 report only point estimates for Sim_GT, CP, etc. Without confidence intervals, it is unclear whether the small gaps (e.g., 0.460 vs. 0.464 on single-person Sim_GT) are statistically meaningful. This is standard practice to address.

### Trivial

- The method name "Cure" appearing in Figure 8 is a clear labeling error that should be corrected to "WithAnyone."

## Nice-to-Haves

- **Evaluate with a different face recognition backbone** (e.g., FaceNet, MagFace) to test whether the gains and the M_CP metric are robust beyond ArcFace's embedding space.
- **Show failure cases** where WithAnyone still exhibits subtle copy-paste or loses identity, providing a balanced picture of remaining limitations.
- **Include statistical significance tests** (bootstrapped confidence intervals or paired tests) for the main quantitative comparisons.
- **Report the correlation coefficient** between M_CP and human judgments rather than stating only "moderate positive correlation."

## Removed Points

These points were raised by reviewers but are removed after cross-checking against the paper:

1. **Criticism that the trade-off "not fully broken" on single-person (CP not lowest, Sim_GT not highest).** WithAnyone achieves CP=0.144 vs. FLUX.1 Kontext's 0.099 and OmniGen2's 0.142, but these low-CP methods have far lower Sim_GT (0.324 and 0.365, respectively). The paper's claim is about the *combination* of high Sim_GT and low CP — shown by the outlier position above the regression curve in Figure 5 — not that it is strictly best on every individual axis. The paper's narrative is well-supported by the data.

2. **Reproducibility concern about web-scraped dataset.** The paper explicitly states "explicit Creative Commons (CC) filters" were used, a 500k paired subset is being released, and the project is fully open-sourced (line 20). Per hard rules, questioning the existence/release status of cited resources is removed.

3. **Missing DynamicID comparison.** The paper explicitly acknowledges DynamicID was excluded "due to unavailability of code and pretrained models" (footnote 1, line 64). This is a reasonable and transparent exclusion.

4. **Criticism about dataset not being redistributable.** The ethics section addresses licensing, and the paper states it is released for non-commercial academic research. This is a scope limitation, not a flaw in the paper itself.

5. **Strength: User study confirming perceptual superiority.** Removed because the verified weakness (labeling error, small sample) undermines confidence in this evidence. The user study results are directionally consistent but not strong enough to serve as a pillar of support.

6. **Strength "comprehensive evaluation across multiple settings."** While the paper evaluates on many baselines, this is a generic descriptor that adds little beyond what is already covered in other strengths.

## Novel Insights

The most interesting observation emerging from the reviews is the following tension: the harsh critic's strongest criticism (abstract overstatement on single-person) actually reveals an important nuance about the paper's framing. The paper's core contribution is the *joint* optimization of identity fidelity and copy-paste suppression, yet it occasionally describes this as "state-of-the-art identity similarity" which invites comparison on a single dimension. The real novelty — and the data fully supports this — is that WithAnyone achieves the best *combination* of high Sim_GT and low copy-paste, occupying a previously empty region in the trade-off space (Figure 5). The reviews also surface that the dataset construction pipeline (combining single-ID clustering with multi-ID group photo retrieval via name-aware queries) is a pragmatic engineering contribution that may prove more influential than the method itself, since paired multi-ID data remains the primary bottleneck for progress in this area.

## Suggestions

1. **Tone down the "state-of-the-art identity similarity" claim** in the abstract and introduction to more precisely match the evidence: e.g., "WithAnyone achieves competitive identity similarity (within 1% of the best single-person method) while substantially reducing copy-paste artifacts, breaking the trade-off observed in prior work."
2. **Fix the "Cure" labeling error** in Figure 8 and either scale up the user study or report it more transparently with confidence intervals and inter-rater agreement.
3. **Add bootstrapped confidence intervals** to Tables 1 and 2 for the main metrics (Sim_GT, CP) to clarify statistical significance.
4. **Report the correlation coefficient** between M_CP and human judgments (currently only described as "moderate positive correlation").
5. **Add a brief discussion of failure cases** to the qualitative section for balance.

## Score and Decision

**Anchor papers for calibration** (all from the deepreview_13k_calibration corpus):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| u1cQYxRI1H (IC-Light) | 10.0 | Substantially stronger — physically grounded method with exceptional results and clearer demonstration of scalability. WithAnyone is good but not at this level. |
| 6O3Q6AFUTu (NoiseDiffusion) | 8.0 | Comparable in terms of solid technical contribution, but WithAnyone has broader scope (dataset + benchmark + method). |
| KZgo2YQbhc (PaRa) | 7.5 | Very similar profile: clear technical idea, good ablation, minor overclaiming in the abstract. WithAnyone arguably has more contributions (dataset + benchmark). |
| PJqP0wyQek (MS-Diffusion) | 6.0 | Similar multi-subject personalization task, but WithAnyone has stronger evidence of a real problem (copy-paste metric) and more thorough evaluation. |
| 4GSOESJrk6 (DreamBench++) | 6.0 | Benchmark-only paper with limited novelty. WithAnyone has more substantive contributions. |
| Bz9wjvToCS (DiffDeID) | 4.4 | Weaker face-generation paper with missing ablations. WithAnyone is substantially stronger. |
| NWvsm2VxAM (ID-Booth) | 3.0 | Poor results and limited novelty. WithAnyone is far stronger in both technical contribution and empirical validation. |

Position relative to anchors: WithAnyone is clearly above the ~6.0 papers (DreamBench++, MS-Diffusion, DiffDeID) which have notable weaknesses in contribution density or evidence quality. It is comparable to PaRa (7.5) — both have a well-executed technical contribution with minor overclaiming issues. It does not reach the exceptional level of the 9-10 papers (IC-Light) which demonstrate a more transformative advance. The paper's main strengths are its combined dataset+benchmark+method contribution, clear problem identification, thorough ablation, and strong results on multi-person scenarios. Its main weaknesses are limited to presentation-level issues (abstract wording, labeling error, missing confidence intervals) that do not threaten the core claims.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>