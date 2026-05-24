Now I have sufficient context for calibration. Let me synthesize the review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
// List only reasonable points. Rank by severity.

### Fatal

### Major

### Minor

### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me now compose the full review.

---

**Bracket determination:** Round 1 placed the paper somewhere between the weak anchors (~3.0) and strong anchors (8.0). The most directly comparable anchor is the CDIS paper (8.0, "When Selection meets Intervention"), which addresses the related but distinct problem of pre-intervention selection bias. The current paper addresses post-treatment selection, provides both soundness AND completeness (stronger than CDIS's only-soundness), but has thinner real-world validation and some algorithm clarity issues. Round 2 anchors at 6.0 and 7.0 confirm the paper sits between those points. Comparing against the 7.0 anchor ("Deriving Causal Order..."), this paper has stronger theoretical novelty but weaker real-world validation. I place it at 7.0.

---

## Summary

This paper identifies and formalizes the problem of **post-treatment selection** in interventional causal discovery — a scenario where samples are selectively included after interventions (e.g., quality control in single-cell experiments), creating spurious dependencies that existing frameworks mistake for true causal relations. The authors introduce a causal formulation that models post-treatment selection jointly with latent confounders, define a finer-grained equivalence class (ℱℐ-Markov equivalence) and its graphical representation (ℱ-PAG), and develop the ℱ-FCI algorithm, which is proven sound and complete for recovering this class. Synthetic experiments against six baselines show consistent improvements, and a real-world gene perturbation analysis demonstrates practical applicability.

## Strengths

1. **Identifies a genuinely overlooked problem.** Post-treatment selection is common in practice (gene perturbation quality control, clinical trial per-protocol analysis) but no existing interventional causal discovery framework addresses it. The paper's motivating examples (Figure 1) clearly demonstrate why the standard invariance/variance pattern fails to distinguish causation from selection, making the problem easy to grasp.

2. **Sound and complete algorithm with formal guarantees.** The ℱ-FCI algorithm is proven sound (Theorem 3) and complete (Theorem 4) for recovering the ℱℐ-Markov equivalence class. This is a meaningful theoretical contribution — notably, the closely related CDIS paper (Dai et al., 2025) on pre-intervention selection only proved soundness, not completeness. The paper also provides Lemmas 2–4 and Theorem 2 that establish graphical criteria connecting CI patterns to edge marks, forming a principled foundation.

3. **ℱ-PAG representation extends the expressive power of PAGs.** The introduction of square marks (□), ▲, and →△ edge types captures structural distinctions that standard PAGs collapse. Figure 5 convincingly shows that a single PAG edge (e.g., ○→○) corresponds to multiple structures that ℱ-PAG can differentiate (direct causation, inducing path via latent, selection via inducing path). This is not merely cosmetic — it is necessitated by the richer CI patterns available from interventional data.

4. **Comprehensive synthetic evaluation against strong baselines.** The experiments compare ℱ-FCI against six methods (GIES, IGSP, UT-IGSP, JCI-GSP, FCI-interven, CDIS) across hard and soft interventions, varying sample sizes (500–2000) and variable counts (10–25), with 95% confidence intervals averaged over 10 random graphs. ℱ-FCI achieves consistently higher DAG Precision and lower SHD, with the gap widening as the number of variables increases. F1-score and recall are also reported (Appendix Figure 10), and scalability (Figure 11) and noise robustness (Figure 12) are assessed.

## Weaknesses

### Major

1. **Real-world validation in the main paper is too thin to be convincing.** Section 5.2 devotes only three sentences to the Norman et al. (2019) single-cell perturbation experiment. The paper states that results are "evaluated using prior knowledge provided by Enrichr" and references Appendix D.3 for "detailed analysis," but the main text provides no quantitative metrics (precision/recall against a known regulatory network, overlap with curated pathway databases, or baseline comparison on the same data). Even a comparison against FCI-interven or CDIS on the same gene expression data would substantially strengthen the claim that the method recovers biologically meaningful structure. This is the single weakest link in the empirical story.

2. **Reliance on Type I inducing nodes is acknowledged but not analyzed.** The paper states in the Conclusion that identification "depends critically on the presence of Type I inducing nodes" and mentions Type II inducing nodes as a future direction. However, there is no analysis of how often Type I nodes exist in the synthetic experimental setup or in realistic biological graphs. The reader cannot gauge how much of the reported precision advantage over baselines comes from cases where Type I nodes happen to be present vs. how often ℱ-FCI cannot apply its core disambiguation step. An empirical analysis of Type I node frequency in the synthetic graphs would directly address this.

3. **No computational complexity analysis.** The algorithm inherits FCI's exponential skeleton discovery and adds interventional CI tests parameterized by `AllPaths` between intervened node pairs. The paper mentions scalability results (Figure 11) but provides no explicit complexity analysis. For a constraint-based method that may need to enumerate all paths between pairs of intervened nodes, the worst-case cost matters. An analysis of the number of CI tests required, or at least a discussion of how the algorithm scales with the number of interventions, would help practitioners assess feasibility.

### Minor

4. **Algorithm pseudocode clarity (Step 2.2).** The CI condition tuples in Step 2.2 are all rendered as `(⊥, ⊥, ⊥, ⊥)` (a parser artifact). More substantively, the mapping from specific CI pattern tuples to specific edge orientations is not given in the pseudocode itself — the paper refers to "the orientation rules summarized in Figure 4," but the figure caption and table do not enumerate six distinct patterns that map to the six orientation cases. A reader trying to implement the algorithm would need to reconstruct these mappings from the textual description. The available GitHub repository mitigates this, but the paper should be self-contained.

5. **No ablation study for Step 2.3 (refinement using Type I inducing nodes).** Step 2.3 is the key innovation that distinguishes causal relations from post-treatment selection. An ablation comparing ℱ-FCI with and without this refinement step would isolate its contribution and quantify how much of the observed improvement over baselines comes from this mechanism vs. from other aspects of the algorithm.

### Trivial

6. **Definition 5 (ℱ-PAG) lists eight edge types but the types are garbled in the parsed text** (e.g., "○---○" repeated). The original figure presumably had the correct edge typology, but the main text should be explicit and unambiguous.

## Nice-to-Haves

- A worked example walking through Steps 2.1–2.3 for a concrete graph (e.g., distinguishing Figure 4(b) from 4(e)) would significantly improve accessibility.
- Clarify how hard vs. soft interventions are handled by the theoretical lemmas (Lemmas 3–4 use "intervention" without specifying type; the distinction matters because hard interventions change the graph structure and can alter which inducing paths exist).
- Report F1 on the subset of edges between intervened node pairs (where the algorithm focuses) rather than only on the full DAG.

## Removed Points

The following points from the input reviews were removed with justification:

- **"Algorithm description is insufficiently clear to be reproducible — repeated CI patterns."** The Step 2.2 pseudocode showing `(⊥, ⊥, ⊥, ⊥)` repeated six times is a parser artifact; the original submission had distinct CI patterns. Also, the code is available on GitHub. → Parser artifact, removed per hard rules.
- **"Step 2.1's AllPaths subroutine is computationally explosive if done naively."** `AllPaths` is a standard subroutine for constraint-based methods; the skeleton from Step 1 limits the search space, and the paper mentions scalability evaluation (Figure 11). This is a generic concern applicable to most FCI-family algorithms. → Weakened and now reflected in the complexity analysis point.
- **"Theorems 3 and 4 lack proof sketch."** The appendix (stripped by parser) contains the proofs. → Removed per hard rules about appendix content.
- **"Missing related works."** → Removed per hard rules: I cannot confirm existence of missing references.
- **"Pure formatting/style nitpicks."** → Removed per hard rules.

## Novel Insights

The paper's key insight — that post-treatment selection creates invariant/variant CI patterns identical to causal relations but can be disambiguated through interventions on Type I inducing nodes along intermediate paths — is genuinely novel and extends the theory of interventional causal discovery. The ℱ-PAG representation with square marks fills a gap left by standard PAGs, which cannot distinguish between a direct causal edge and an inducing path through a post-treatment selection mechanism. An interesting observation is that the asymmetry of selection (Figure 4(e) vs. 4(a)) provides a detectable signal when interventions are available on multiple variables, which existing frameworks missed because they only look at endpoint CI patterns. This suggests that the "Y-structure" at intermediate nodes (non-endpoints on inducing paths) carries information that previous equivalence classes discarded but that is recoverable with interventional data.

## Suggestions

1. **Strengthen the real-world evaluation.** At minimum, apply FCI-interven and CDIS to the same Norman et al. (2019) dataset and report overlap of discovered edges with known regulatory pathways, using a quantitative enrichment score (e.g., Enrichr combined score) rather than only a qualitative listing. Even better: report precision/recall against a curated gold-standard network.
2. **Provide a Type I node frequency analysis.** In the synthetic experimental setup, report the proportion of inducing paths that contain at least one Type I inducing node, stratified by graph density and number of interventions. This lets readers assess the practical scope of the core disambiguation mechanism.
3. **Include an ablation of Step 2.3.** Report precision and SHD for ℱ-FCI with and without the Type I inducing node refinement, to isolate its contribution.
4. **Add a complexity analysis section.** Provide the worst-case number of CI tests as a function of |V|, |ℐ|, and max path length, and show empirical runtime alongside the scalability figure.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):**
- Weak band (avg < 3.5): AvXrppAS2o (3.0), 4u0ruVk749 (3.0), fSxiromxAq (3.0), 5AJ8R4z5g0 (3.25) — all papers with significant flaws or limited novelty, clearly below the current paper.
- Middle band (3.5–7.5): x2rZGCbRRd (5.5), cbFqqtJGtA (4.25), ZXs3pkmrRG (5.5), G5KbDVAlI6 (4.0) — mixed-quality papers addressing relevant topics.
- Strong band (avg > 7.5): xByvdb3DCm (8.0 — "When Selection meets Intervention", CDIS paper), Nx4PMtJ1ER (8.0), 3cuJwmPxXj (8.0), k38Th3x4d9 (8.0).

**Initial bracket:** The paper sits between 5.5 and 8.0. The CDIS paper at 8.0 is the most directly comparable — both address selection bias in interventional CD, but the current paper tackles post-treatment selection (complementary problem) and provides completeness guarantees that CDIS lacks. However, CDIS had more polished real-world validation.

**Round 2 (Narrowing within 5.5–8.0):**
- BZYIEw4mcY (6.0 — "Efficient and Trustworthy Causal Discovery") — accepted with 4×6.0; similar theoretical depth but less novel problem. Current paper is stronger in novelty and completeness.
- u63OVngeSp (7.0 — "Deriving Causal Order from Single-Variable Interventions") — accepted, mixed scores (5,8,8,6,8); strong theory but restrictive assumptions. Current paper has comparable theory quality but broader applicability.
- SKulT2VX9p (6.67 — fairness, less relevant).
- nHkMm0ywWm (6.5 — structural estimation).

**Final score:** 7.0. The paper is stronger than the 6.0 anchor (novel problem, complete theory, broader experiments) and comparable in quality to the 7.0 anchor. It falls slightly below the 8.0 CDIS paper due to thinner real-world validation and some presentation clarity issues, though it offers completeness guarantees that CDIS did not.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>