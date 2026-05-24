Now I have sufficient calibration context. Let me write the final consolidated review.

## Summary

This paper addresses an important overlooked problem in interventional causal discovery: post-treatment selection bias, where samples are selectively included after interventions (e.g., quality control in biological studies). The authors show that post-treatment selection produces CI patterns indistinguishable from genuine causal relations under existing frameworks. They propose a new formulation (FI-Markov equivalence), a refined graphical representation (F-PAG), and a sound and complete algorithm (F-FCI) that can distinguish causal relations from selection-induced dependencies using interventional data. The paper makes genuine theoretical contributions, but the experimental validation has a significant gap in how evaluation metrics are defined.

## Strengths

- **Novel problem formulation.** Post-treatment selection is a real, overlooked challenge in interventional causal discovery. The paper compellingly demonstrates (Figures 1, 4) that existing PAG-based equivalence classes conflate causal relations with post-treatment selection, providing strong motivation for the work.

- **Theoretical characterization.** The FI-Markov equivalence class (Definition 2), F-PAG representation (Definition 5), and the graphical criteria (Theorem 2) form a coherent theoretical framework. The paper formally links CI patterns involving intervention indicators and selection variables to the distinguishability of causal vs. selection structures, going beyond standard PAGs.

- **Sound and complete algorithm.** F-FCI (Algorithm 1) is accompanied by soundness (Theorem 3) and completeness (Theorem 4) statements under oracle CI tests, providing formal guarantees. The algorithm's Step 2.3, which uses CI tests on intervention indicators of Type I inducing nodes to disambiguate inducing paths, is a clean conceptual innovation.

- **Comprehensive baseline comparison.** The synthetic experiments (Figure 6) compare F-FCI against six strong baselines (GIES, JCI-GSP, IGSP, UT-IGSP, FCI-INTERVEN, CDIS) across multiple sample sizes (500–2000), graph sizes (d=10–25), and intervention types (hard/soft), with consistent precision improvements and lower SHD.

## Weaknesses

### Fatal
None.

### Major
- **Evaluation metric mapping is not specified.** The paper reports "DAG Precision" and "DAG SHD" (Figure 6) comparing F-FCI against baselines, but F-FCI outputs an F-PAG containing edge marks (squares, special path types like Δ and ▲) that have no direct equivalent in a DAG. The paper never explains how the F-PAG output is mapped to a DAG for metric computation — which edges are counted as true causal relations, how partially oriented or selection-marked edges are treated, or how the special marks (square, Δ-path) factor into precision and SHD. Without this, the main experimental evidence (Figure 6) is not fully interpretable. This does not undermine the theoretical contributions, but it critically weakens the empirical validation as presented in the main text.

### Minor
- **Real-world experiment is qualitative only.** Section 5.2 states that F-FCI identified regulatory links in the Norman dataset, "evaluated using prior knowledge provided by Enrichr," but reports no quantitative results (precision/recall against known targets, comparison with baselines). The referenced Figure 13 is an output visualization. This makes the real-world section an illustration rather than evidence. (This is common for single-cell perturbation studies where ground truth is partial, but the paper should be transparent about the qualitative nature.)

- **Practical limitation of intervention requirements under-discussed.** The algorithm's key innovation (Step 2.3) relies on having interventions on Type I inducing nodes. While the conclusion states that identification "depends critically on the presence of Type I inducing nodes," the paper does not separately clarify that interventions must be available on those specific nodes. In many experimental settings, interventions may be conducted on only a subset of variables, which could limit the algorithm's ability to distinguish causal from selection paths in practice.

### Trivial
None (parser artifacts are excluded per instructions).

## Nice-to-Haves
- A breakdown of experimental results showing performance separately for edges resolvable via Type I inducing node interventions vs. edges resolvable from standard interventional CI patterns would help demonstrate that the novel algorithm component (Step 2.3) is actually used and effective.
- Quantitative results for the real-world experiment (even against a small set of known causal pairs) would significantly strengthen the paper.

## Removed Points
Points flagged to be removed — treat with caution:
1. "Intervention targets not specified in experiments" — The paper references Appendix D for additional experimental details (which the parser strips). The main text specifies the data-generating procedure and the "Hard"/"Soft" intervention subplots, and it is reasonable that detailed intervention specification appears in the appendix.
2. "Step 2.2 has formatting issues with identical CI conditions" — This is a parser artifact; the original PDF renders different CI patterns.
3. "Theorem 1 is standard/not novel" — This misreads the role of Theorem 1; it is a formal building block establishing the CI-to-invariance mapping, not claimed as a standalone novel result.
4. "The claim that PAG is too broad is too strong" — The paper's claim is verifiably correct: Figures 4(b) and 4(f) show that (a)/(b) and (e)/(f) share PAG representations but are distinguishable with interventional data. The criticism is factually wrong.
5. "CDIS is for pre-treatment selection, its poor performance is expected" — This is an informative negative control; showing that a method designed for a different problem fails on this problem validly demonstrates the distinction the paper aims to make.
6. "Missing discussion of Type II limitation beyond what's stated" — The paper explicitly acknowledges the Type II limitation in its conclusion. Expanding it is a nice-to-have, not a weakness.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface an observation about the work that the authors themselves missed.

## Suggestions
1. Add a paragraph (or a table in the appendix) explicitly describing the mapping from F-PAG edge types to DAG-level metrics. For example: "An edge X₁ → X₂ in the F-PAG is counted as a causal edge. Square marks and Δ/▲ paths are treated as non-causal. SHD counts edge-mark disagreements between the estimated F-PAG and the projection of the true DAG onto F-PAG marks." Without this, the reader cannot interpret the main experimental figure.
2. Move the practical limitation about intervention requirements on Type I inducing nodes from the conclusion into a dedicated "Limitations" subsection, and state it more explicitly: "The completeness result assumes that interventions are available on Type I inducing nodes, which may not hold in all experimental settings."
3. Consider softening the real-world claims or adding quantitative comparisons (even against a handful of known regulatory relationships from the literature).

## Score and Decision

**Calibration anchors (all rounds):**

*Round 1 (bracketing):*
- Weak anchors (<3.5): avg 2.50–3.33 — papers on confounding mitigation and treatment effect estimation, mostly withdrawn/rejected. Not directly comparable (different sub-problem).
- Middle anchors (3.5–7.5): avg 4.00–4.50 — causal discovery/treatment effect papers with identifiable flaws (e.g., "Identifying Partially Observed Causal Models" at 4.50/rejected; "Amortized Bayesian Causal Discovery" at 4.00/rejected; "Coupled Confounding and Collider Biases" at 4.50/rejected).
- Strong anchors (>7.5): avg 8.00 — papers on unrelated topics (protein generation, language models). Not relevant.

*Round 2 (narrowing):*
- Lower-middle (4.0–5.5): 
  - 4.50 "Theoretical Guarantees for Causal Discovery on Large Random Graphs" (accepted poster) — narrower scope (FNR bounds for one optimizer), synthetic-only experiments, but clean evaluation.
  - 5.00 "Influence without Confounding: Causal Discovery from Temporal Data" (accepted poster) — similar structure (theory + algorithm + experiments), limited real-world validation, clearer evaluation but linearity assumption.
  - 4.50 "Identifying Partially Observed Causal Models" (rejected) — flawed proofs and insufficient novelty.
- Upper-middle (5.5–7.0):
  - 6.00 "On the identifiability of causal graphs with multiple environments" (accepted poster) — strong theory, very restrictive assumptions (Gaussian noise), bivariate synthetic experiments only.
  - 6.00 "When Shift Happens - Confounding Is to Blame" (accepted poster) — theory for OOD generalization, different sub-problem.

**Round 1 bracket:** I identified the paper plausibly sits between 4.0 and 6.5 based on topically similar causal discovery papers.

**Round 2 narrowing:** The paper has stronger novelty and broader contributions than the 4.50 anchors (which had narrower/fixable flaws). It has a more developed algorithm and more comprehensive experiments than the 6.00 anchors (which had cleaner but more restrictive theory). However, the evaluation metric mapping gap is a real weakness that the cleaner anchor papers did not have—it prevents full assessment of the main experimental results. This places it between the 4.50–5.00 accepted papers (which had different but comparably serious weaknesses) and the 6.00 papers (which had cleaner evaluation despite more limited scope).

**Final score: 5.0** — The paper's theoretical contributions are genuine and the problem is important. The evaluation gap (unexplained F-PAG-to-DAG metric mapping) is significant but not fatal to the core contribution. A revision addressing this would make the paper substantially stronger.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>