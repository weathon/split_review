## Summary

This paper proposes OML, a brain-inspired hierarchical neural network for online multimodal learning with three claimed capabilities: (1) continuous learning without catastrophic forgetting, (2) reference extraction to autonomously identify which feature dimensions a word refers to, and (3) conflict detection with human-in-the-loop question-asking. While the reference extraction idea is genuinely novel, the evaluation has two structural problems that undermine the core claims.

## Strengths

- **Reference extraction via coefficient of variation (Section 3.4).** The idea of using variance/mean ratios across sample presentations to identify which feature dimensions a word consistently refers to is genuinely novel and well-motivated. The intuition that referring dimensions' variance shrinks while non-referring dimensions' variance grows is conceptually sound.

- **Continuous learning demonstrated against online baselines (Table 1).** In the open environment, OML achieves 89.8 (Fruits V→A) and 89.0 (A→V), outperforming the online methods ART (84.2, 83.0) and AEN (86.2, 84.9) with 3–5 point margins, while demonstrating stability against catastrophic forgetting.

- **Modal extension (Table 3).** OML consistently outperforms AEN across all 12 task/modality combinations in the VAT experiments, and the use of frequency parameter λ for routing signals to modality-specific pathways is architecturally interesting.

## Weaknesses

### Major

1. **Inconsistent evaluation criteria across methods in Tables 2 and 3.** The paper explicitly states that when ART/AEN return supersets of features (all shape+color features when queried with "hóng sè" instead of only color), these are counted as correct: *"we count this as a correct result for them in Table 2"* (line 248). Similarly for Table 3, AEN returning concepts in both visual and taste channels is counted as correct. This means baselines are evaluated under a different correctness criterion than OML, which returns precise referring features. Because the scoring rule differs between methods, Tables 2 and 3 do not provide an apples-to-apples comparison. A table where one method's outputs count as correct while another's are scored on a stricter criterion does not establish superiority on the claimed capability. The paper either needs a uniform metric applied to all methods, or must acknowledge that the tables measure different constructs.

2. **Human-in-the-loop interaction was not tested with real users.** The paper states: *"In the experiment, if the question posed to the user by OLM remains unanswered for a certain period of time, we set the answer to be positive"* (line 240). Attribute (2) in Section 1 — *"detect conflict… ask the user appropriate questions and conduct learning based on user's answer"* — is presented as a core contribution. Conflict detection was tested via 10% mismatched pairs, but the interactive learning loop itself (asking questions, receiving answers, updating based on them) was simulated with default positive responses. A central claimed capability was never actually evaluated with real human interaction.

### Minor

1. **No ablation studies.** The paper claims three component capabilities jointly contribute to performance but never removes any component to measure its individual contribution.

2. **Open-environment protocol for offline methods is underspecified.** The paper does not describe how offline methods (DAE, DBM, DJSRH, NRCH, FUME) are adapted to the sequential-parts protocol. Whether they are retrained from scratch on accumulated data or fine-tuned on each new part would drastically affect results. This gap makes the magnitude of the open-environment comparison uninterpretable.

3. **No variance or statistical significance reported.** All results are single numbers without standard deviations, confidence intervals, or significance tests. Given the small 3–5 point margins against online baselines, reliability cannot be assessed.

4. **No sensitivity analysis for key hyperparameters.** The reference extraction threshold r=0.5 and probability density threshold ϑ=0.8 are set without analysis of how performance varies with these choices.

5. **No per-part accuracy in the open environment.** The paper reports aggregate accuracy but never shows whether earlier classes are retained after later ones are learned — the core definition of catastrophic forgetting resistance.

6. **Eq. (1) cosine summation purpose is unexplained.** The paper states T=150 and *"its value does not affect the algorithm"* (line 71), yet includes it in the computation. Why this Fourier-series-like formulation is used instead of a simpler similarity metric is never explained. The Fourier transform in Eq. (6) is similarly underspecified in terms of how amplitude/frequency outputs are transmitted and decoded.

### Trivial

None.

## Nice-to-Haves

- A small user study (even 5–10 participants) to validate the human-in-the-loop interaction claim.
- Ablation experiments removing the reference extraction mechanism to show its specific contribution.

## Removed Points

These points were flagged by reviewers but are either factually incorrect, overblown, or violate the filtering rules:

1. **"Offline methods are straw men / staged comparison inflates OML's position"** — The paper includes online methods (ART, AEN) as fair comparators, and OML beats them. Offline methods are included to demonstrate known consequences of catastrophic forgetting, which is informative. The underspecified adaptation protocol (kept as Minor #2 above) is the real issue, not the inclusion itself.
2. **"Method cannot be reproduced"** — While some details are unclear (Eq. 1 cosine term, Fourier transform), Section 3.5 provides four concrete learning cases with specific procedural rules. Individual unclear aspects are kept as minor points above.
3. **"Neuroscience framing is decorative"** — A presentation/style issue, not a substantive weakness. The paper would be clearer describing the architecture in its own terms.
4. **"Missing code/pseudocode"** — Removed per hard rule on reproducibility nitpicks.
5. **"Datasets are tiny"** — The paper uses established benchmarks from prior work (Xing et al. 2019, Lai et al. 2011). Scale is noted but not a fatal issue for a methods paper.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Re-run Tables 2 and 3 with a uniform evaluation criterion applied to all methods, or restructure the claims to honestly reflect what each comparison actually measures.
2. Conduct a human evaluation (or at minimum a synthetic evaluation with varying answer types — both positive and negative) to validate the interaction capability.
3. Add ablation studies removing the reference extraction mechanism to show its specific contribution.
4. Report results over multiple runs with variance, and show per-part accuracy in the open environment.
5. Add sensitivity analysis for the reference extraction threshold r and activation threshold ϑ.

## Score and Decision

**Score: 3.5 / Decision: Reject**

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| gNoqEdT2wO.md | 2.33 | R1 | Lower contribution (benchmark only, no novel method). OML has stronger conceptual novelty. |
| JIlIYIHMuv.md | 2.50 | R1 | Lower contribution (adapts existing CL to LVLMs). OML has stronger conceptual novelty. |
| 0CtIt485ew.md | 4.00 | R1/R2 | Similar bio-inspired approach and similar evaluation gaps (no std dev, missing baselines). |
| jYyste2HLP.md | 4.33 | R1/R2 | Similar bio-inspired incremental learning, unsupported claim about multimodal generalization — analogous to OML's untested human interaction. OML's evaluation problems are more severe. |
| G9Ea7mlqGO.md | 3.80 | R1/R2 | Similar evaluation concerns (missing baselines, unclear claims). OML has stronger conceptual novelty but more severe evaluation flaws. |
| IhOeYKqnfp.md | 4.25 | R2 | More rigorous evaluation and stronger empirical results than OML. |
| Ur4LqAOXIF.md | 3.50 | R2 | Comparable-level paper: novel idea but evaluation on synthetic data only with missing details. |
| 0dELcFHig2.md | 6.67 | R1 | Significantly stronger evaluation methodology (Accepted). OML far below this. |

**Round 1 bracket**: 3.5 – 6.67 (narrowed from initial broad search). The paper clearly sits below the 5+ band.

**Round 2 narrowing**: Placed the paper at 3.5 — comparable to SODA (3.50) and below Artsy (4.00) and FlyOrien (4.33), because the asymmetric scoring issue is a structural evaluation flaw rather than a missing detail. The paper has genuine conceptual novelty but the evaluation does not support the core claims as presented.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>