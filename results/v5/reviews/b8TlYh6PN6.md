Now I have a thorough understanding of the paper and the calibration landscape. Let me produce the final consolidated review.

## Summary

2-3 sentence summary of the paper's contribution.

The paper provides a complete graphical characterization of distributional equivalence for linear non-Gaussian causal models with arbitrary latent variables and cycles — the first such result in any parametric setting without structural assumptions. It introduces edge-rank constraints as a new tool and develops a transformational characterization (analogous to the Meek conjecture) that enables traversing the equivalence class. Building on this theory, it presents the glvLiNG algorithm for recovering models from data up to equivalence.

## Strengths

- **Novel and complete equivalence characterization (Theorems 2, 3, §3–4).** The paper delivers the first graphical criterion for when two linear non-Gaussian latent-variable models with cycles induce the same observed distribution set. The criterion is local (children bases of L and each X_i, Theorem 2) rather than requiring exhaustive path-rank checks, and the transformational characterization (Theorem 3) provides an operational way to traverse the entire equivalence class via admissible cycle reversals and edge additions/deletions. This genuinely advances the theoretical understanding of identifiability in a practically relevant model class.

- **Edge-rank constraints as a new tool (Definition 4, Theorem 1, §3.3).** The duality between path ranks and edge ranks (Theorem 1) fills a missing piece in the rank-based causal discovery toolbox. Edge ranks are more local and graph-manipulable than path ranks, enabling the clean derivations in the equivalence characterization. This contribution is likely to be useful beyond the paper's specific setting.

- **Clean handling of trivial unidentifiability via irreducibility (§2.2).** Propositions 1 and 2 give a simple graphical condition for irreducibility and an explicit reduction procedure, eliminating trivial cases (e.g., latent variables with no effect on observables) without imposing structural assumptions. This is a technically sound canonicalization that connects to prior work (Salehkaleybar et al., 2020) in the acyclic case.

- **Well-written and pedagogically effective.** The paper is clearly structured, with good examples (Figures 2, 3), helpful analogies to Markov equivalence (CPDAG, Meek conjecture), and a step-by-step development from path ranks through edge ranks to the final criterion. The exposition makes the technical material accessible.

## Weaknesses

### Fatal
None.

### Major

- **Mismatch between the "discovery method" claim and the evidence provided.** The title, abstract, and introduction present glvLiNG as a practical discovery method (e.g., "first structural-assumption-free discovery method"), but the evaluation does not adequately validate this claim. The algorithm's key step — recovering the mixing matrix via overcomplete ICA (OICA) — is treated as an oracle. In the target setting (more sources than observed variables, possible cycles), overcomplete ICA is a generically hard problem whose identifiability requires additional constraints that the paper does not discuss. The main-text evaluation either tests only the graph-construction subroutine (Table 4) or evaluates how baselines fail under misspecification (Table 5), which does not provide positive evidence that glvLiNG works end-to-end. The finite-sample pipeline results are relegated to Appendix D.4 and described as having mixed outcomes ("baselines perform better on sparser graphs," §5). The acknowledgment in the final remarks that the algorithm is a "proof of concept" is appropriate but comes too late, contradicting the strong claims in the earlier sections. The paper's genuine contribution is the theoretical characterization; the "discovery method" packaging overreaches relative to the evidence.

- **The OICA oracle assumption is not adequately scoped.** The paper relies on OICA to estimate the mixing matrix but does not specify which OICA procedure is assumed, what identifiability conditions are needed for it to succeed in the overcomplete regime, or how practical violations would affect results. While the paper cites Eriksson & Koivunen (2004) for identifiability, this reference addresses the number-of-sources problem rather than providing a practical estimation procedure for the general overcomplete setting with cycles. The gap between the oracle assumption and what can actually be computed from finite data is substantial and under-discussed. This limits the paper's contribution as a "method" paper.

### Minor

- **No procedure given for estimating ranks from finite data.** The algorithm reads rank constraints from the mixing matrix, but the paper provides no decision rule, threshold, or statistical test for rank estimation from finite samples. This makes it impossible to assess the practical robustness of the method without either reimplementing an external rank estimator or reading unspecified implementation details.

- **Main text omits critical algorithmic details.** Lemma 10 and the associated graph-construction procedure are central to the algorithm but are deferred entirely to the appendix (cited without explanation in the main text). A reader of the main text cannot assess how the algorithm works or why it is correct without the appendix.

- **The finite-sample evaluation is only in the appendix and has mixed results.** The full pipeline is tested only in Appendix D.4. The text summarizing these results (§5) notes that baselines perform better on sparser graphs, which is a significant qualification that undercuts the method's claimed advantage. The reader should not have to go to the appendix to learn this.

### Trivial
None.

## Removed Points

- **"Overcomplete ICA is not addressed at all"** — The paper does cite OICA results (Eriksson & Koivunen, 2004) and mentions OICA in the algorithm description and final remarks. The concern is valid but the paper does not completely ignore the issue; the criticism is too absolute. However, the substance (insufficient discussion of OICA's tractability) is retained in the Major weaknesses above.

- **"Comparison to Adams et al. (2021) is insufficient"** — The paper mentions Adams et al. (2021) as the closest theoretical result and explains what it covers (acyclic, unique identification conditions) and what it leaves open (describing the equivalence class when identifiability fails). This is an adequate comparison for the paper's scope. Removed.

- **"Missing appendix, missing proofs"** — The parser strips the appendix; the original submission has complete proofs and details. Removed per hard rules.

- **"Reproducibility concerns about undisclosed hyperparameters"** — The paper is a theoretical/algorithmic contribution with oracle experiments in the main text. The request for training details is not standard for this type of paper. Removed per hard rules.

- **"Missing related works"** — Cannot verify without external sources. Removed per hard rules.

## Nice-to-Haves

- The paper would be strengthened by honestly repositioning its contribution. The theoretical characterization (Sections 2–4) is the paper's core strength. A title such as "Distributional Equivalence in Linear Non-Gaussian Latent-Variable Cyclic Models: Characterization and Learning" (already reasonably close) with an abstract that foregrounds the theoretical result and presents the algorithm as a constructive corollary with explicit caveats about the OICA oracle would better match the evidence.

- A brief discussion of what class of OICA procedures could be used with glvLiNG, and under what conditions they succeed, would substantially increase the paper's practical value without requiring new experiments.

## Novel Insights

None beyond the paper's own contributions. The edge-rank / path-rank duality (Theorem 1) is the most transferable insight — it opens a new perspective on rank-based causal discovery that could simplify other problems currently formulated in terms of path ranks.

## Suggestions

1. Reframe the paper to foreground the theoretical characterization and present glvLiNG as a constructive demonstration (with clear oracle caveats) rather than a validated discovery method.
2. Add a discussion of the conditions under which OICA can recover the mixing matrix in the latent-variable cyclic setting, or at minimum state the problem's difficulty more prominently.
3. Include at least a sketch of the rank estimation procedure (if one is used) or clearly state that the evaluation assumes oracle rank access.
4. Move the finite-sample results to the main text and discuss the mixed performance on sparse graphs honestly.

## Score and Decision

**Calibration anchors consulted (all rounds):**

| Anchor | Avg Score | Round / Query | Comparison to Paper Under Review |
|--------|-----------|---------------|-----------------------------------|
| TRHyAnInUC | 3.25 | R1-topic-low | Much weaker paper (diffusion model for CD, no theory); paper is substantially stronger |
| AvXrppAS2o | 3.00 | R1-topic-low | Prediction-focused causal ML; not comparable |
| BZYIEw4mcY | 6.00 | R1-topic-mid / R1-weakness / R2 | Accept. Stronger evaluation but still requires structural assumptions; paper under review has stronger theory but weaker evaluation |
| nHkMm0ywWm | 6.50 | R1-topic-mid / R1-weakness | Accept. Pure-children assumption, strong theory + evaluation; paper under review has weaker evaluation |
| 7oT1X8xjIk | 5.80 | R1-topic-mid / R2 | Nonlinear representation learning; different subarea |
| fGhr39bqZa | 6.00 | R1-topic-mid / R1-weakness / R2 | Accept. Homologous surrogates relax pure children; paper under review has more general theory but weaker evaluation |
| vyQmKicyVw | 3.50 | R1-weakness | Different problem (multiple distributions); not comparable |
| q07DDpu8Xb | 5.25 | R2 | Reject. Theory with incremental contribution, weak experiments; paper under review has stronger theory |
| lQYi2zeDyh | 5.00 | R2 | Reject. Claim-evidence mismatch in amortized CD; similar pattern of overclaim vs. validation |

**Round-1 bracket:** [4.0, 6.0]. The paper is clearly above the low-band (3.0–3.5) and below high-band (8.0) anchors. Among mid-band anchors, it has stronger theory but weaker empirical validation than accepted 6.0–6.5 papers.

**Round 2 narrowing:** The paper's theoretical strength places it above the 5.0–5.25 rejection anchors (q07DDpu8Xb, lQYi2zeDyh). Its theoretical contribution is genuinely novel and well-executed. However, the claim-evidence mismatch keeps it below the accepted 6.0+ papers in the same subarea.

**What low-band anchors and weakness-anchored hits failed at:** The low-band papers either had weak theory (TRHyAnInUC at 3.25) or were in different subareas. The 5.0–5.25 papers (lQYi2zeDyh, q07DDpu8Xb) had claim-evidence mismatch or incremental theory — the paper under review shares the claim-evidence mismatch pattern. The accepted 6.0+ papers all had stronger empirical validation than the paper under review.

**Final score: 5.0.** The paper makes a genuine theoretical contribution that advances the state of knowledge. However, the mismatch between the ambitious "discovery method" framing and the actual evidence (oracle OICA, main-text evaluation of subroutines only, mixed finite-sample results in the appendix) prevents it from reaching the level of the accepted 6.0+ papers in this subarea. A revision that honestly reframes the contribution around the theory and tempers the algorithmic claims would merit a higher score.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>