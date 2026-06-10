Now I have enough calibration data. Let me finalize the review.

**Round 1 bracket:** Between 4.0 (GISL, rejected) and 8.0 (CDIS, accepted). The paper's novel problem formulation and complete theoretical pipeline place it well above the rejected GISL paper, but the experimental concerns and unspecified intervention requirements prevent it from reaching the uniformly high-scoring CDIS paper.

**Round 2 narrowing:** Comparing against BZYIEw4mcY (6.0, accepted - causal discovery with latent variables, similar scope of theoretical contribution with limited experiments) and fGhr39bqZa (6.0, accepted - causal graph recovery with latent variables), the paper under review is comparable: a solid theoretical contribution with real but non-fatal experimental weaknesses.

The paper is clearly better than GISL (4.0) which had scalability and novelty issues, but falls below CDIS (8.0) which had a cleaner experimental evaluation and more general selection model. I place it at **6.0** — in line with other accepted theoretical causal discovery papers with moderate experimental evaluation.

---

## Summary
This paper introduces the problem of post-treatment selection in interventional causal discovery—where samples are selectively included after interventions (e.g., quality control in gene perturbation studies). The authors show existing frameworks cannot distinguish post-treatment selection from true causal relations since both produce identical distributional signatures (variant marginals, invariant conditionals). They propose a new augmented DAG formulation, define a finer FI-Markov equivalence class with a novel graphical representation (F-PAG), and develop a provably sound and complete algorithm (F-FCI) for recovering causal structure under these conditions.

## Strengths
- **Well-motivated, genuinely novel problem**: The paper provides concrete real-world examples (Norman et al. gene perturbation with quality control; clinical trial per-protocol analysis, §1) and formally demonstrates through Figures 1-2 how existing interventional frameworks fail under post-treatment selection, producing identical CI signatures for both causal and selection structures.
- **Complete theoretical pipeline**: The paper builds a coherent chain from Definition 1 (augmented DAG) through Theorem 1 and Lemmas 1-4 (Markov properties with CI pattern characterization in Figure 4(i)'s table), Definition 2 (FI-Markov equivalence), Theorem 2 (graphical criteria), to Theorems 3-4 (soundness and completeness of F-FCI).
- **Novel graphical representation (F-PAG)**: Definition 5 introduces new edge types (square □ mark, specialized ▸Δ and ▸▲ marks for inducing paths) and inducing node concepts (Definition 6, Type I and Type II). Figure 5 concretely demonstrates that structures indistinguishable under standard PAG are distinguished under F-PAG, providing a provably finer equivalence class.
- **Comprehensive baseline comparison**: F-FCI is compared against six baselines (GIES, IGSP, UT-IGSP, JCI-GSP, FCI-INTERVEN, CDIS) across multiple sample sizes (n=500, 1500, 2000), both hard and soft interventions, and variable counts (d=10-25), with F-FCI consistently achieving higher precision and lower SHD.

## Weaknesses
### Fatal
None

### Major
- **Intervention design requirements are not formally specified** — Step 2.3 requires interventions on Type I inducing nodes along paths between intervened variable pairs to disambiguate causal relations from selection (e.g., hard intervention on X₃ in Figure 4(b), testing ψ₃ ⊥̸ X₂). This requirement is acknowledged in §6 but never formally stated as a theorem or proposition specifying what class of intervention targets ℐ is necessary/sufficient. In practice, gene perturbation studies intervene on genes of interest, not on genes that happen to be internal nodes on unknown causal paths. Without a formal statement of intervention requirements, the reader cannot assess whether the method applies to any real experimental design. This gap between theoretical guarantees and practical applicability is the paper's most significant weakness.
- **Only 10 random graph instantiations per experimental configuration** — Figure 6 caption states "All values are averaged over 10 graphs." For constraint-based causal discovery with CI tests across complex graph structures, this produces unreliable estimates. Typical evaluations in this literature use 50-100+ graph instantiations. While error bars (95% CI) are shown, they are wide with only 10 repetitions.

### Minor
- **Non-standard noise distribution without justification** — The error terms are sampled from Uniform([0,2] ∪ [2,4]) (line 275), a bimodal distribution with a gap. No justification is given for this choice, and no results with standard distributions (Gaussian, uniform) are shown. This could interact with the selection mechanism in ways that affect generality of the empirical claims.
- **Algorithm Step 2.2 is unreadable in the extracted text** — All six conditional rules display the identical condition CIs == (⊥, ⊥, ⊥, ⊥) with different orientations (lines 216-226). This is almost certainly a PDF parsing artifact (the original likely has different CI patterns with ⊥ vs ⊥̸ for each rule, as indicated by Figure 4(i)'s table showing distinct patterns for each structure), but it prevents verification of the algorithm from the text.

### Trivial
None

## Nice-to-Haves
- An ablation varying the number of intervention targets and proportion of Type I inducing nodes covered would directly demonstrate the mechanism by which F-FCI outperforms baselines and show how improvement scales with intervention design richness.
- Clarification of what "DAG Precision" and "DAG SHD" measure—whether these are computed over the learned F-PAG mapped back to a DAG or over the equivalence class.
- Results with standard noise distributions (Gaussian) to establish generality of the experimental findings.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Algorithm Step 2.2 CI condition garbling**: This is a PDF extraction/parser artifact, not an author error. The original paper would have distinct CI patterns for each rule, as the Figure 4(i) table demonstrates different patterns for each structure. Removing this as it is not an author error.

## Novel Insights
The paper's core insight—that post-treatment selection produces the same distributional signature as true causal relations (variant p(effect), invariant p(effect|cause)) under existing interventional frameworks—is genuinely novel and practically important. The mechanism for breaking this symmetry via hard interventions on Type I inducing nodes (Figure 4(b)-(f)) combined with the Figure 4(i) table cataloging how eight different structural configurations yield distinguishable CI patterns provides a concrete analytical framework, not just an existence result. This complements the CDIS paper (which addressed pre-intervention selection with a twin graph framework) by tackling a distinct and practically relevant form of selection bias.

## Suggestions
- Add a formal theorem or proposition stating what intervention set ℐ is necessary and sufficient for F-FCI's identification guarantees. This is the single most important improvement.
- Increase simulation repetitions to at least 50 and report variance explicitly.
- Justify the noise distribution choice and add results with Gaussian noise to establish empirical generality.

## Calibration Anchors

**All retrieved papers:**

| Round | Paper | Avg Score | Comparison |
|-------|-------|-----------|------------|
| 1 | AvXrppAS2o (causal structure for prediction) | 3.0 | Much weaker - applied paper without theoretical novelty |
| 1 | 4u0ruVk749 (DFITE, treatment effect estimation) | 3.0 | Much weaker - different problem, no structural contribution |
| 1 | 5AJ8R4z5g0 (potential outcomes under hidden confounders) | 3.25 | Weaker - estimation focus, no graphical model contribution |
| 1 | MVpvyeVeyI (Causal BO with unknown graphs) | 3.4 | Weaker - different focus, less theoretical depth |
| 1 | G5KbDVAlI6 (GISL, GRN inference with selection + confounders) | 4.0 | Weaker - scalability issues, smaller evaluation; directly related topic |
| 1 | 0sO2euxhUQ (Latent SCM learning) | 4.0 | Weaker - less complete theoretical pipeline |
| 1 | ZXs3pkmrRG (TICL, test-time interventional causal learning) | 5.5 | Comparable novelty but rejected; different methodological approach |
| 1 | fGhr39bqZa (Causal graph recovery via homologous surrogates) | 6.0 | Similar level: solid theory, limited experiments, accepted |
| 1 | 3cuJwmPxXj (Intervention extrapolation) | 8.0 | Stronger - different problem, very polished |
| 1 | hrqNOxpItr (Cross-entropy inversion) | 8.0 | Stronger - different topic, more impactful |
| 1 | k38Th3x4d9 (AERCA root cause analysis) | 8.0 | Stronger - more complete experimental evaluation |
| 1 | xByvdb3DCm (CDIS, selection meets intervention) | 8.0 | Stronger - related but distinct problem (pre-intervention selection), uniformly high scores, similar theoretical scope |
| 2 | BZYIEw4mcY (latent variables + complex relations) | 6.0 | Similar: novel theory with limited experiments, accepted at 6.0 |
| 2 | nHkMm0ywWm (partially observed LiNGAM) | 6.5 | Slightly stronger: cleaner presentation, accepted |
| 2 | 8muemqlnG3 (DAG recovery via Bayesian Optimization) | 6.5 | Similar level: strong contribution, accepted |
| 2 | FhQSGhBlqv (RLCD, versatile causal discovery with hidden vars) | 7.5 | Stronger: very well-written, broader contribution |
| 2 | orD5t7blqV (PIT algorithm) | 4.25 | Weaker: limited novelty, rejected |
| 2 | 2pEqXce0um (Root cause analysis) | 4.5 | Weaker: different problem, less theoretical depth |
| 2 | mGmx41FTTy (two time-slices for DAG learning) | 6.33 | Similar level but rejected with mixed scores |

**Round 1 bracket:** 4.0–8.0. The paper is clearly above GISL (4.0, rejected for scalability/small experiments) but below CDIS (8.0, uniformly strong scores, more general selection model).

**Round 2 narrowing:** Comparing to BZYIEw4mcY (6.0, accepted) and fGhr39bqZa (6.0, accepted), the paper under review has a comparable level of theoretical contribution and similar experimental limitations. It's slightly below nHkMm0ywWm (6.5) which had cleaner presentation. The unspecified intervention design requirements (M1) and thin experiments (M2) prevent scoring higher, but the genuinely novel problem and complete theoretical pipeline keep it solidly in the accepted range.

**Final score: 6.0** — A solid theoretical contribution that introduces a novel, practically motivated problem with a complete pipeline from formulation to algorithm with formal guarantees. The contribution is accepted-range but tempered by unspecified intervention requirements and thin experimental validation.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>