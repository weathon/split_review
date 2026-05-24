Now I have everything needed. Let me write the final consolidated review.

**Calibration Report:**

**Round 1 Bracketing (3 queries, score bands):**
- Weak band (<3.5): Papers scoring 1.5–3.0 (e.g., NWvsm2VxAM, 12iSWNLDzj, kCnLHHtk1y). These are clearly weaker than WithAnyone — incomplete evaluations, unclear contributions.
- Mid band (3.5–7.5): Papers scoring 4.4–6.67 (DiffDeID at 4.40, Event-Customized at 5.00, UIFace at 6.00, MS-Diffusion at 6.00, InstantPortrait at 6.67). WithAnyone sits in this range.
- Strong band (>7.5): Papers scoring 7.6–10.0 (IC-Light at 10.0, RB-Modulation at 8.0, Representation Alignment at 9.0). These are theoretical breakthroughs or large-scale systems papers. WithAnyone is not at this level.

→ **Bracket: 5.5–7.0**

**Round 2 Narrowing (queries inside bracket):**
- MS-Diffusion (score 6.00): Multi-subject personalization paper. Comparable structure (dataset+model+benchmark). Received score 6. WithAnyone has clearer novelty (copy-paste formalization) and more dramatic quantitative improvements. Slightly stronger.
- InstantPortrait (score 6.67): One-step portrait editing. Very strong in its niche. WithAnyone has a broader scope but lacks the distillation novelty.
- UIFace (score 6.00): Face recognition synthetic data. Similar methodological depth. WithAnyone has more contributions (dataset, benchmark, metric, model).

→ Based on these, WithAnyone sits between MS-Diffusion (6.0) and InstantPortrait (6.67). The paper makes three solid contributions (dataset, benchmark, model) but has several minor but real weaknesses.

**Final score: 6.5**

---

## Summary

This paper introduces WithAnyone, a diffusion-based model for identity-consistent multi-person image generation. It makes three contributions: (1) **MultiID-2M**, a large-scale open-source dataset of ~500k group photos with paired identity references plus ~1.5M unpaired images; (2) **MultiID-Bench**, a benchmark with a formal Copy-Paste metric (Eq. 2) that quantifies the relative bias of a generated face toward the reference versus the ground truth; and (3) **WithAnyone**, a FLUX-based model trained with a four-phase pipeline, GT-aligned ID loss, and an ID contrastive loss with extended negatives, which demonstrably breaks the long-standing trade-off between identity fidelity and copy-paste artifacts.

## Strengths

- **Formal Copy-Paste metric (Eq. 2).** The paper correctly identifies that existing evaluation (Sim(Ref)) inadvertently rewards trivial copying. The proposed Copy-Paste metric \( \mathcal{M}_{\text{CP}} \) normalizes by the reference-GT angular distance, cleanly separating identity fidelity from copy-paste. This is a genuine contribution to evaluation methodology.

- **MultiID-2M paired dataset.** The four-stage construction pipeline produces ~500k group photos with paired references — a resource that enables contrastive training strategies impossible with existing unpaired datasets. The scale (~25k identities, 1M+ reference images) and the inclusion of both paired and unpaired subsets are well-motivated.

- **GT-aligned ID loss (Eq. 4).** Using ground-truth (rather than predicted) landmarks to align the generated face for ArcFace embedding is simple and effective. Figure 7 shows it produces lower and more informative ID loss across all noise levels compared to prediction-aligned alternatives, while avoiding the computational cost of full denoising.

- **Clear trade-off breaking.** Figure 5 and Tables 1–2 provide compelling evidence that WithAnyone occupies a previously empty region of the Sim(GT)-vs-Copy-Paste space. On the single-person subset, it achieves Sim(GT)=0.460 with Copy-Paste=0.144, while the nearest competitor at comparable similarity (InstantID, 0.464) has Copy-Paste=0.337 — more than double.

- **Comprehensive ablation.** Table 3 cleanly isolates the contribution of each component: removing Phase 3 (paired tuning) increases Copy-Paste from 0.161 to 0.239; removing extended negatives drops Sim(GT) from 0.405 to 0.368; training on FFHQ alone collapses to Sim(GT)=0.224. The ablation supports the claimed role of each design choice.

- **Large-scale evaluation.** Comparison against 15 baselines spanning both general customization models and face-specific methods, on both single- and multi-person subsets, provides a thorough assessment.

## Weaknesses

### Fatal
None.

### Major
None. The core claims — that WithAnyone reduces copy-paste while preserving identity fidelity — are supported by the evidence.

### Minor

1. **Test set shares the same data pipeline as training.** MultiID-Bench is sampled from the MultiID-2M corpus (same collection pipeline, different identities). While the paper filters out identity overlap, the test images share the same distribution of pose, lighting, viewpoint, and celebrity-photography conventions as training. The only external evaluation (OmniContext) is a single-person benchmark that does not measure copy-paste. This does not invalidate the results — many papers evaluate in-distribution — but it means the reported gains may partly reflect specialization to the pipeline's statistical structure rather than a fully general capability. The ablation showing FFHQ-only training yields poor results (Sim(GT)=0.224) confirms the dataset's importance but does not isolate whether the method or the data distribution drives the gap.

2. **User study lacks statistical rigor.** The study uses 10 participants ranking 230 groups across four criteria, but the main paper reports only a bubble chart of average rankings without error bars, confidence intervals, or significance tests. The paper defers details to Appendix H (stripped by the PDF parser), but based on what is visible in the main text, the reporting is insufficient to assess whether the observed advantage is reliable. This is a methodological gap, not a structural flaw — the results are suggestive but do not meet the standard of evidence for the claim that WithAnyone is preferred across all four criteria.

3. **Unresolved discrepancy between automatic aesthetics and human aesthetics.** In Table 1, WithAnyone's Aes score (4.783) is the second-lowest among face-specific models, far below GPT-4o (5.344) and InfU (5.389). Yet the user study ranks WithAnyone highest in aesthetics. The paper does not discuss or attempt to resolve this contradiction. If the automatic metric is unreliable for this type of generated content, that should be acknowledged; if it measures something orthogonal to human aesthetic judgment, that should be clarified.

4. **Marginal overclaim on identity similarity.** The paper states WithAnyone "achieves state-of-the-art identity similarity." In Table 1, WithAnyone's Sim(GT)=0.460 is technically second to InstantID's 0.464. The difference is negligible (0.004) and does not affect the paper's core claim — which is about breaking the trade-off, not maximizing Sim(GT) alone — but the phrasing should be more precise (e.g., "comparable identity similarity with substantially reduced copy-paste").

5. **Copy-Paste metric filtering may exclude harder cases.** The metric is only computed for cases where Sim(GT) > 0.40 (single) or > 0.35 (multi). This filtering is justified for numerical stability, but the paper does not report how many test cases are excluded by this filter or whether the exclusion pattern differs across methods. If WithAnyone systematically fails on the excluded harder cases (where no method achieves good identity fidelity), the reported Copy-Paste advantage could be biased.

### Trivial
- Figure 5's scatter plots include a regression line, but the paper does not specify whether this line is fitted on all models or excludes WithAnyone, or whether the deviation is statistically significant.

## Nice-to-Haves

- **Sensitivity analysis for the 50% paired-data ratio in Phase 3.** The paper uses 50% without justification. A sweep (e.g., 25%, 50%, 75%) would strengthen the empirical grounding of this design choice.
- **Out-of-distribution evaluation.** A small test set of non-celebrity faces from an independent source would address the in-distribution concern and provide stronger evidence of generalization.
- **Failure case analysis.** The paper would benefit from a discussion of what types of prompts or identities still cause copy-paste or identity degradation.
- **Computational cost comparison.** Training budget and inference time vs. baselines would help practitioners assess the method's practicality.
- **Missing related work comparisons** were not noted, as I cannot verify their existence; potential missing comparisons fall outside my knowledge.

## Removed Points

- Criticism about missing code/checkpoint availability: the paper states the project is fully open-sourced. Removed per Hard Rules (no reproducibility concerns about cited resources).
- Criticism about missing ablation for the 50% ratio in Phase 3: downgraded to Nice-to-Have. The existing ablation already validates Phase 3's importance; a ratio sweep is an incremental improvement.
- Criticism about no failure case analysis: typical nice-to-have, not a weakness.
- Criticism about missing analysis of computational cost: nice-to-have; not standard to require training cost comparisons.
- Formatting nitpicks and "missing appendix" complaints: removed per Hard Rules (parser strips appendices).

## Novel Insights

Both reviewers independently converged on a key insight that the paper itself does not fully articulate: the ablation in Table 3 shows that removing extended negatives (w/o Ext. Neg.) actually produces the *lowest* Copy-Paste score (0.074), but at a significant cost to Sim(GT) (0.368). This reveals an important nuance — the extended negatives primarily boost identity fidelity rather than directly suppressing copy-paste. The paper's ID contrastive loss and paired training (Phase 3) operate through complementary mechanisms: Phase 3 discourages copying by breaking the reference-target identity, while the contrastive loss strengthens identity representations. The finding suggests these two mechanisms could potentially be tuned independently (e.g., adjusting λ_CL and the paired-data ratio as separate knobs), which the current fixed configuration leaves unexplored.

## Suggestions

1. For the camera-ready version, add a brief discussion of the Aes discrepancy — even a sentence acknowledging that the automatic aesthetic predictor may not capture perceived quality in face-generation contexts would resolve the contradiction for readers.
2. Clarify the regression line in Figure 5 (whether it includes/excludes WithAnyone) and optionally report the correlation coefficient with and without the proposed method.
3. Report the number of test cases excluded by the Sim(GT) filtering threshold for the Copy-Paste metric, and verify that exclusion rates are balanced across methods.
4. Tone down "state-of-the-art identity similarity" to "comparable identity similarity" when describing the single-person results (Table 1), since InstantID achieves a marginally higher Sim(GT).
5. If the user study data permits, include a brief statistical summary (e.g., Fleiss' κ for inter-rater agreement, or at minimum the standard deviation of rankings) to give readers a sense of reliability.

## Score and Decision

**Calibration anchors used across rounds:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| NWvsm2VxAM (ID-Booth) | 3.00 | 1 | Much weaker — limited evaluation, unclear contributions |
| 12iSWNLDzj (Adversarial Face) | 3.00 | 1 | Much weaker — different problem scope, thin evaluation |
| kCnLHHtk1y (Ancient Buildings) | 3.00 | 1 | Much weaker — small-scale, niche topic |
| RFJGFrMvYj (TCIG) | 1.50 | 1 | Much weaker — unclear method, poor evaluation |
| 88Qm4fGWzX (Event-Customized) | 5.00 | 1 | Weaker — limited comparisons, task definition concerns |
| Bz9wjvToCS (DiffDeID) | 4.40 | 1 | Weaker — missing ablations, outdated baselines |
| riieAeQBJm (UIFace) | 6.00 | 1,2 | Comparable — similar methodological depth, weaker evaluation scope |
| WUibctXLT7 (DreamMakeup) | 4.75 | 1 | Weaker — limited task scope, weaker evaluation |
| PJqP0wyQek (MS-Diffusion) | 6.00 | 2 | Comparable — similar contribution structure (dataset+model+benchmark), slightly less novelty |
| ZkFMe3OPfw (InstantPortrait) | 6.67 | 2 | Slightly stronger — more impressive inference speed results, but narrower scope |
| GpdO9r73xT (Crystal Ball) | 6.25 | 2 | Comparable — different topic, similar quality |
| 9oMB6wnFYM (Deconstructing DDM) | 6.50 | 2 | Comparable — theoretical contribution vs. applied contribution, similar quality |
| aqlzXgXwWa (Multiple Character Animation) | 5.75 | 2 | Slightly weaker — narrower scope, more limited evaluation |

**Narrowing:** Round 1 bracketed at 5.5–7.0. Round 2 anchors consistently in the 5.75–6.67 range. The paper's three contributions (dataset, benchmark, model) are all solid, and the central claim (breaking the trade-off) is convincingly demonstrated. However, the test-set distribution concern, underpowered user study reporting, and unexplained Aes discrepancy prevent it from reaching the top of this range. The paper is stronger than MS-Diffusion (6.0) due to clearer problem formalization and more dramatic quantitative improvements, but not as strong as InstantPortrait (6.67) which had a more surprising technical result (one-step distillation). Final score: **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>