Now I have sufficient calibration. Let me write the final review.

---

## Summary

This paper addresses a genuine and underexplored problem: post-treatment selection bias in interventional causal discovery with latent confounders. The core contribution is a new formulation that explicitly models post-treatment selection within the augmented DAG framework, defines a finer equivalence class (FI-Markov equivalence) with a new graphical representation (F-PAG), and proposes a sound and complete algorithm (F-FCI) to recover causal structure up to this equivalence class. The method is validated on synthetic data across multiple configurations and on a real-world single-cell gene perturbation dataset (Norman et al.).

## Strengths

- **Novel problem formulation with clear motivation**: The paper identifies a concrete gap — existing interventional causal discovery frameworks cannot distinguish post-treatment selection from genuine causation because both produce the same invariance/variance pattern (variant marginal, invariant conditional). The synthetic and real-world motivation (gene perturbation quality control) is compelling. This is formalized in Section 3.1-3.2 with Lemmas 3-4 linking distributional changes to graphical marks.

- **FI-Markov equivalence provides a strictly finer equivalence class**: Theorem 2 proves that two augmented DAGs are FI-Markov equivalent iff they share the same skeleton, v-structure, and edge marks among intervened nodes. The paper demonstrates concretely (Figure 1) that structures indistinguishable under standard MAG-based equivalence classes become separable under FI-Markov equivalence.

- **Soundness proof is reasonably constructed**: The proof of Theorem 3 (Appendix B) walks through each mark type (tail, arrowhead, square) and the special edge types, showing that the CI patterns uniquely identify them under the augmented DAG model. The acknowledgment of the square-mark limitation (Y-structures with latent confounders) and the proposal to use hard interventions to address it is honest and constructive.

- **Strong synthetic experimental validation**: Figure 6 shows F-FCI consistently outperforming six baselines (GIES, IGSP, UT-IGSP, JCI-GSP, FCI-INTERVEN, CDIS) on both DAG Precision and SHD across 10-25 variable graphs. Table 2 shows >15% precision gains over FCI-INTERVEN, the closest constraint-based baseline. The paper includes extensive robustness checks: varying noise levels (Figure 12), Laplace/Gumbel noise families (Tables 4-5), and complex nonlinearities (Table 3). F-FCI remains stable across all these conditions.

- **Expressive graphical representation (F-PAG)**: Definition 5 introduces novel edge types (e.g., `→`, `-`) that distinguish inducing paths without direct causal links from genuine causation. This is a genuinely useful extension of the standard PAG for the post-treatment selection setting.

- **Code availability**: The paper provides a GitHub repository with a Python implementation, partially mitigating concerns about algorithmic reproducibility.

## Weaknesses

### Fatal
None.

### Major
None. The core claims are supported by the theory and experiments. The issues below are addressable.

### Minor

- **Completeness proof is thin and relies heavily on prior work**: The proof of Theorem 4 (Appendix B, lines 1364-1372) asserts that node marks are identifiable from Lemmas 2-4, then claims the `→` and `-` edges follow from Type I node detection, and finally defers to prior work (Ali et al. 2012, Zhang 2008b, Kocaoglu et al. 2019) for marks involving unintervened nodes. It does not provide a self-contained argument that the six CI pattern signatures in Step 2.2 of the algorithm exhaust all possible graph structures, nor does it prove that the orientation rules produce a maximally informative F-PAG. This weakens the "provably complete" claim. The paper would be stronger if it either (a) provided a more rigorous completeness argument, or (b) explicitly qualified the completeness as conditional on available interventions and Type I nodes (which the authors partially acknowledge in the Conclusion).

- **Real-world evaluation lacks systematic quantitative metrics**: The Norman dataset analysis (Section 5.2, Appendix D.3) lists specific edges with supporting biological evidence from Enrichr, ARCHS4, GEO, and ChEA2022, and provides a plausible narrative linking detected selection-affected genes (CDKN1A, CDKN1C, RREB1, ZNF318) to QC filtering mechanisms. However, there is no systematic quantification — no precision/recall against a curated gold-standard network (e.g., TRRUST, ChEA3 consensus), no F1-score, and no comparison with any baseline on this dataset. The edge-level validation, while biologically informed, remains qualitative.

### Trivial

- **Algorithm pseudocode has ambiguous definitions**: Step 2.1 references `AllPaths(Gp(0), XI(i), XI(j))` without defining what `AllPaths` returns (all simple paths? all nodes on any path?). The break condition "If no more paths can be blocked then break" is vague. The code repository mitigates this, but the pseudocode should be self-contained.

## Nice-to-Haves

- A worked-through toy example walking from raw CI tests through each orientation rule to the final F-PAG would substantially improve clarity, especially for the Type I node refinement in Step 2.3.
- Relaxing the dependence on Type I inducing nodes — as the authors acknowledge in the Conclusion — would broaden practical applicability. Even a discussion of sufficient conditions under which Type II-only paths might be partially resolved would be valuable.
- A systematic quantitative evaluation on the Norman dataset (e.g., precision/recall against a transcription factor target database) would strengthen the real-world claims.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **"Theoretical claims are not substantiated by the proofs provided" (Harsh Critic)**: The harsh critic claims the soundness proof "concedes ambiguity" regarding square marks. This is a misreading: the proof honestly acknowledges a limitation (Y-structures with latent confounders can cause non-identifiability for square marks) and proposes a solution (hard interventions). Acknowledging scope limitations is good scientific practice, not a proof failure. The soundness proof is reasonable and covers each mark type. Only the completeness proof is thin (see Minor weakness above).

- **"Experiments compare against baselines not designed to handle post-treatment selection" (Harsh Critic)**: This comparison is the entire point — the paper demonstrates that existing methods fail when post-treatment selection is present, which is exactly the motivation. The comparison against FCI-INTERVEN (Table 2), the closest method structurally, is a valid ablation. Demanding that the authors adapt competitors' methods to their setting is unreasonable.

- **"Claim of 'going beyond traditional equivalence classes' is misleading" (Harsh Critic)**: The abstract explicitly qualifies this as "up to FI-Markov equivalence." The paper demonstrates (Figure 1, Theorem 2) that FI-Markov equivalence is strictly finer than standard MAG-based equivalence. The claim is accurate.

- **"Theorem 2 is stated without proof" (Harsh Critic)**: The proof is in Appendix B (lines 1254-1282), walking through arrowhead, tail, and both-marks cases with reference to MAG construction rules. It is brief but present.

- **"Link between Type I nodes and CI patterns is described only informally" (Harsh Critic)**: Definition 6 formally defines Type I nodes. Step 2.3 of Algorithm 1 and Theorem 3 explicitly connect them to CI tests for refining orientations. The connection is formal.

- **Strength Finder's claim about "empirical advantage over baselines"**: Kept in strengths, but note that the ~5% precision margin in Figure 6 has overlapping error bars with some baselines (notably CDIS) in certain configurations. This is a modest but consistent advantage, not a dominant one.

## Novel Insights

None beyond the paper's own contributions. The paper's core observation — that post-treatment selection and causation produce the same marginal/conditional invariance pattern and thus require additional structural information (Type I nodes, hard-hard intervention contrasts) to disentangle — is the key novel insight, and it is already stated in the paper.

## Suggestions

- Strengthen the completeness proof with an explicit argument that the six CI patterns in Step 2.2 are exhaustive for the augmented DAG structure, rather than relying primarily on citations to prior work.
- Add systematic quantitative evaluation on the Norman dataset: compute precision/recall/F1 against at least one curated transcription factor target database (e.g., TRRUST or ChEA3 consensus), and report these metrics alongside any baseline applicable to this setting.
- Define `AllPaths` precisely in the algorithm pseudocode and clarify the break condition.
- Consider including a small worked example (e.g., Figure 4(b) walked through step by step) to make the algorithm mechanics transparent to readers.

## Score and Decision

**Anchor comparison:**

| Anchor | Avg Score | Decision | Comparison |
|--------|-----------|----------|------------|
| `mA78uXqcnl.md` (Hawkes processes + latent confounders) | 7.00 | Oral | Stronger: more novel theoretical bridge (continuous→discrete), rigorous identifiability conditions. Current paper's theory is more incremental. |
| `ta8BKRa1bl.md` (Identifiability with multiple environments) | 6.00 | Poster | Somewhat stronger: more surprising theoretical result (constant envs suffice). Current paper has broader experiments. |
| `BNHplerBYE.md` (Score-based greedy search, latent vars) | 5.33 | Poster | Comparable: solid theory with some proof gaps, strong synthetic experiments, limited real-world validation. |
| `V7pT2ZRoTB.md` (Theoretical guarantees on random graphs) | 4.50 | Poster | Current paper has more practical relevance and broader experimental validation. |
| `r4TvgVFo9L.md` (InvarGC) | 3.50 | Reject | Current paper has stronger theory (soundness) and more thorough experiments. |
| `YvMkU4BYOA.md` (XBIC) | 2.00 | Reject | Current paper is far stronger: real theoretical framework vs. heuristic. |

The paper under review sits at the level of a solid poster: it addresses a genuine gap, provides a principled theoretical framework, and validates it with thorough synthetic experiments. The completeness proof is thin and the real-world evaluation is qualitative, but neither issue invalidates the core contribution. The paper's strengths in problem formulation, theoretical characterization (FI-Markov equivalence, F-PAG), and synthetic validation place it clearly above the reject threshold and in the range of accepted posters.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>