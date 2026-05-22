Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper identifies that 3D molecular distributions exhibit a "dense-concentrated structure" (DC-structure) — narrow, densely packed probability peaks separated by low-density voids — which causes diffusion-model reverse steps to overshoot valid regions and accumulate irreparable errors. The authors propose DIST, a plug-in corrective sampling method that filters and rescales intermediate model distributions at a chosen timestep, steering trajectories back toward valid peaks. The paper provides a formal definition of DC-structure, theoretical analysis, and experiments on QM9 and GEOM-Drugs showing consistent improvements across three backbone models (EDM, GeoLDM, RADM).

## Strengths

1. **Strong and consistent empirical improvement across diverse backbones.** Table 2 shows that DIST improves atom stability, molecule stability, validity, and validity×uniqueness for EDM, GeoLDM, and RADM on both QM9 and GEOM-Drugs. The gains are substantial (e.g., EDM molecule stability on QM9: 82.0% → 89.9%; validity: 91.9% → 96.9%) and hold across GNN-based equivariant, Transformer-based, and latent-space models. This demonstrates the issue is architecture-agnostic and the fix is general.

2. **Meaningful efficiency gains are demonstrated.** Table 3 reports that DIST reduces the average number of inference timesteps from 1000 to between ~414 and ~637 across backbones and datasets while simultaneously improving quality. Even with the smallest pilot subset (size 30) in Table 4, DIST outperforms the original EDM on all metrics while using fewer timesteps (428.3 vs. 1000).

3. **Well-motivated problem framing.** The paper articulates a genuine challenge for molecular diffusion: that the narrow validity regions cause overshoot errors during reverse inference which then propagate and compound. The formalization of DC-structure (Definition 3.1) provides a quantitative vocabulary for this phenomenon that goes purely qualitative observations.

4. **Plug-in design validated fairly.** The paper uses officially released model weights for all backbones without altering hyperparameters, demonstrating that DIST works as a model-agnostic add-on rather than requiring retraining.

## Weaknesses

### Fatal

None.

### Major

1. **The precise implementation of the pilot score is unspecified in the main text.** The paper describes the pilot score s_j only via examples ("round-trip residual, self-consistency, ensemble variance, or chemistry-based penalty," line 154) without stating which one was actually used in experiments or how it is computed. This is not a missing appendix detail — the main text itself does not commit to a concrete scoring function. Since the scoring mechanism is central to how DIST selects valid batches, the reader cannot determine what the method actually does from the main paper. The authors reference Appendix F for "detailed settings," but the core algorithmic choice should be explicit in the main text.

2. **The efficiency accounting in Section 4.3 appears incomplete by the paper's own formula.** The claimed cost of (T-t)/|B| + t steps (e.g., 307 for t=300, |B|=100) counts the main trajectory steps from T to t (parallelized) and from t to 0, but does not explicitly account for the cost of running "full reverse inference" on the pilot subset from each batch. If the pilot inference runs a complete reverse process from T to 0 (or from the correction timestep to 0) on even a small number of samples per batch — say, 30 pilot samples per batch of 100 — the total model evaluations per accepted sample could be substantially higher than 307. The paper references Appendix G.1 for a "detailed quantification," but the main text's simplified framing of "nearly half the cost" could be misleading if the pilot overhead is significant.

3. **Corollary 3.1 is a standard data-processing inequality that does not rely on the DC-structure or provide molecular-specific insight.** The corollary states that steering q_t closer to p_t reduces the final TV distance — this holds for any distributions and any Markov kernel. Its inclusion as a theoretical contribution specific to molecular generation or DIST is overstated. The paper would benefit from either removing it or explicitly acknowledging that it is a general property being leveraged rather than claimed as novel theory.

### Minor

1. **No direct comparison against alternative corrective/sampling methods in the main text.** The paper states that a comparison with corrective methods is provided in Appendix B, but the main experimental section (Table 2) only compares DIST-augmented models against their original counterparts and non-diffusion baselines. Including a main-text comparison against, e.g., simply using fewer DDIM steps or a rejection-sampling baseline would strengthen the empirical case that DIST's specific corrective mechanism — not just any step-count reduction — drives the improvement.

2. **The claim of being "the first to highlight" the dense-concentrated nature of molecular distributions (line 31) is too strong.** Prior work on molecular diffusion (Hoogeboom et al., 2022; Xu et al., 2023) already discusses that valid molecular configurations occupy narrow regions and that chemical constraints make generation challenging. The formalization of DC-structure is a contribution, but claiming "first to highlight" overstates novelty.

3. **Proposition 3.1 is stated abstractly with the exact form deferred to the appendix.** The bound depends on quantities (α(τ), β(τ), TV(q_{t,j}, p_{t,j})) that are not computable in practice, and no instantiation is given for concrete choices of pilot score or threshold. As presented in the main text, the proposition does not provide actionable guidance or verifiable guarantees for the actual DIST algorithm.

4. **The definition of DC-structure (Definition 3.1) is a Gaussian mixture with bounded covariance and separation, which is not specific to molecules.** The definition could apply to any multimodal distribution with narrow peaks. The paper would benefit from connecting the parameters (σ_*, Δ) to estimable or observable quantities from molecular data to make the definition more than a conceptual illustration.

### Trivial

None.

## Nice-to-Haves

- A controlled experiment comparing DIST against the backbone models using the same reduced number of steps (e.g., via DDIM) without any correction, to separate the effect of fewer steps from the effect of the corrective mechanism.
- An ablation comparing DIST against random rejection of the same fraction of batches, to show that the pilot score is providing non-trivial information.
- Wall-clock time or total model evaluation count (including pilot inference) to complement the timestep-based efficiency report.

## Removed Points

These points are removed from the main review for the reasons stated below. Treat them with caution if they surface in discussion.

1. **"The DIST method is specified at such a high level that it cannot be implemented or evaluated" (Harsh Critic #1).** Removed as a fatal-level criticism because the paper explicitly defers implementation details to Appendix F ("For detailed settings of DIST, please refer to Appendix F"). The main text provides a conceptual description of the algorithm (Section 3.2 "Corrective Sampling" paragraph) which is standard practice for conference papers. The reviewer's objection primarily concerns content that exists in the appendix (which the parser strips). The core concern about the pilot score not being committed to in the main text is preserved as a Major weakness #1 above.

2. **"The improvements could be an artifact of using fewer steps rather than the corrective mechanism" (Harsh Critic #3a).** Removed because it is factually backward: using fewer standard diffusion steps generally *increases* discretization error, not decreases it. The paper's baselines use 1000 steps; DIST achieves better quality with fewer steps, which is the opposite of what would happen if the effect were simply due to reduced step count. This criticism reflects a misunderstanding of diffusion discretization.

3. **"No comparison to existing sampling improvements such as classifier guidance, DDIM, DPM-solver, consistency models, particle filtering" (Harsh Critic, Missing Experiments #3).** Removed because the paper states that "a detailed discussion on the comparison of our work with corrective method is provided in Appendix B." The reviewer presumes this comparison is absent from the paper, but it exists in the appendix (stripped by parser). Additionally, several of the named methods (classifier guidance, DDIM) address different problems (conditional generation, deterministic sampling) than DIST's trajectory correction, so their absence as baselines is not a fundamental flaw.

4. **Strength Finder strength about "theoretical guarantees for DIST" (Corollary 3.1 and Proposition 3.1).** Demoted/removed because, as noted in Major weakness #3, Corollary 3.1 is a standard data-processing inequality, and Proposition 3.1 is stated abstractly without a concrete instantiation. While the theoretical ambition is commendable, the strength as stated overclaims the value of these results.

5. **Strength Finder strength about "the problem is important."** Removed as generic and lacking specific evidence. Strengths must be concrete and specific to the paper's execution, not about the importance of the problem domain.

6. **Strength Finder strength about "ablation on pilot subset size" as a key strength.** Retained as part of the efficiency strength (Strength #2), but downgraded from a standalone strength because the ablation varies only pilot size and does not include a "no-pilot" random-filtering control.

## Novel Insights

None beyond the paper's own contributions. The primary novelty — that the DC-structure of molecular distributions causes reverse inference to overshoot valid regions, and that selective correction at intermediate timesteps can mitigate this — is already stated by the authors. The reviews add perspective on the method's presentation gaps and the need for stronger controlled comparisons, but do not reveal fundamentally new observations about the work.

## Suggestions

1. **Commit to a concrete pilot score in the main text.** State explicitly which scoring mechanism was used in all experiments (e.g., "we compute s_j as the RDKit validity check after running full reverse inference on the pilot sample"). This is essential for reproducibility and algorithmic clarity.

2. **Report total model evaluations including pilot inference overhead.** Either in the main text or a clearly referenced appendix table, provide a complete accounting of model evaluations per accepted sample, showing how the pilot cost scales with pilot size and batch configuration. This will resolve ambiguity about the efficiency claim.

3. **Add a simple controlled baseline:** run the backbone models with an equivalent reduced step count using a standard deterministic sampler (e.g., DDIM) without DIST correction. This would cleanly separate the effect of fewer steps from the effect of the corrective mechanism.

4. **Acknowledge the generality of Corollary 3.1** and reframe it as a known property being leveraged rather than a novel theoretical contribution. This avoids overclaiming.

5. **Tone down the "first to highlight" claim** (line 31) or support it with a brief discussion of why prior discussions of molecular distribution narrowness (e.g., Hoogeboom et al. 2022) are qualitatively different from the DC-structure formalization.

## Score and Decision

The paper makes a genuine contribution: identifying and formalizing the DC-structure issue in molecular diffusion, and proposing an effective corrective method (DIST) that consistently improves quality across diverse backbones while also reducing computational cost. The empirical results in Table 2 are strong and credible. However, the paper has notable presentation issues: the main text does not specify the concrete pilot scoring mechanism used, the efficiency claim may undercount the pilot overhead, and some theoretical claims (Corollary 3.1, "first to highlight") are overstated. These issues are addressable in a revision and do not undermine the core empirical contribution. The paper is above the acceptance threshold but not exceptionally strong.

**Originality:** 7 — The DC-structure formalization and DIST approach are novel, though the broad observation about molecular distribution narrowness has precedent.

**Importance of question:** 8 — Improving molecular generation quality and efficiency is an important research problem.

**Claims supported:** 6 — The main empirical claims are well-supported by Table 2, but the efficiency claim needs clarification and the theoretical framing is partially disconnected.

**Soundness of experiments:** 7 — Fair evaluation using official weights and standard benchmarks. Missing controlled comparisons against alternative sampling methods in the main text.

**Clarity:** 6 — The method description is clear at a conceptual level but lacks concrete algorithmic specification of the pilot score in the main text.

**Value to community:** 7 — The plug-in nature of DIST makes it practically useful, and the DC-structure analysis provides useful framing.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>