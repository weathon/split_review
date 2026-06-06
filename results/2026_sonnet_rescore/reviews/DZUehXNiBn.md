## Summary

VISTA (Voting-based Integration of Subgraph Topologies for Acyclicity) is a modular meta-framework for causal structure learning that decomposes the global DAG learning problem into local Markov Blanket (MB) subgraphs, aggregates local predictions via a weighted voting mechanism that penalizes low-support edges with exponential decay, and enforces acyclicity via a GreedyFAS heuristic. The framework is model-agnostic, supports parallelization, and is accompanied by finite-sample error bounds and an asymptotic consistency guarantee. Experiments across multiple base learners, graph types, and sizes show consistent improvements in FDR and SHD, with notable runtime reductions.

---

## Strengths

- **Consistent model-agnostic empirical improvements.** Tables 1 and 2 show that VISTA-WV reduces FDR by 50–80% relative to standalone baselines across six base learners (NOTEARS, GOLEM, DAG-GNN, GraN-DAG, SCORE) and both ER and scale-free graph families, with F1 improvements ranging from marginal (NOTEARS: 0.76→0.79 on ERS) to substantial (GOLEM: 0.35→0.60 on ERS). The gains persist across both normalized and unnormalized data, supporting the model-agnostic claim.

- **Meaningful runtime efficiency.** Table 3 documents large speedups: NOTEARS at n=300 goes from 12,515s to 2,137s; GraN-DAG from 25,206s to 2,336s. These gains are mechanically grounded in the divide-and-conquer design, not algorithmic tricks specific to any one base learner.

- **Honest and transparent theoretical treatment.** The paper provides Theorem 3.4 (feasible λ interval), Corollary 3.3 (minimum subgraph count), and Theorem 3.5 (O(log n) consistency). Crucially, the paper explicitly acknowledges the independence assumption underlying Theorem 3.2 as idealized ("the bound should be interpreted as a qualitative guide"), and commits to extending the theory as future work. This transparency is preferable to overstating guarantees.

- **Well-motivated sensitivity analysis.** Figure 4 empirically validates the monotonic precision–recall trade-off predicted by Theorem 3.4 — as λ increases, recall rises and precision falls, then curves plateau once λ exceeds the upper bound of Eq. (5). This alignment between theory and experiment bolsters confidence in the theoretical framework's directional correctness.

- **Plug-and-play design with no solver overhead.** VISTA requires only one pass of edge counting and O(n²) aggregation, with no retraining or iterative optimization. The pseudocode (Figure 2) and modular pipeline (Figure 3) are clear and directly reproducible.

---

## Weaknesses

### Fatal
None.

### Major

- **Theoretical guarantees apply to an idealized surrogate, not the actual algorithm.** Theorems 3.2 and 3.5 assume that votes from different MB subgraphs are statistically independent. However, subgraphs derived from overlapping MB neighborhoods of the same dataset produce correlated votes, particularly for edges shared by multiple MBs. The paper acknowledges this gap ("the bound should be interpreted as a qualitative guide"), which is honest — but it means the consistency proof in Theorem 3.5 formally applies to an oracle ensemble of independent classifiers, not to VISTA as implemented. The O(log n) coverage argument in Theorem 3.5 is particularly undermined in sparse graphs where true edges may be covered by few, highly correlated MBs. The theory's directional claims are plausible and the empirics support them, but the paper cannot currently claim a proven consistency guarantee for its actual algorithm.

- **No comparison to a purpose-built scalable competitor in the main text.** Every main-body table pairs a base learner against its VISTA-wrapped version, measuring relative improvement only. The paper's central motivation is scalability in high-dimensional settings — yet Tables 1–3 never benchmark VISTA+base against, say, constraint-based methods designed for large graphs, nor do they show whether VISTA+weak-learner is competitive with a well-tuned standalone scalable method at n=300. The DCILP comparison is deferred to Appendix F.2 (which is stripped from reviewer access), leaving readers unable to assess the absolute performance claim. Given that the paper's stated motivation is improving over existing distributed/fusion strategies, this comparison belongs in the main body.

- **CAM is listed as a baseline in Section 4.1 but absent from all result tables, with no explanation.** The paper explicitly names "CAM Bühlmann & Peters (2016)" in the baselines description, yet Tables 1, 2, and 4 contain no CAM rows. Selective omission of a named baseline — without any explanation such as computational intractability or out-of-scope data settings — warrants justification.

### Minor

- **Real-data evaluation is too small to substantiate scalability claims.** The only real dataset is Sachs (11 nodes, 17 edges, 853 samples), which is far too small to validate the framework's main claim of large-scale causal discovery. Table 4 results are also reported without standard deviations (single-run estimates), making them unreliable for statistical inference. The GraN-DAG result in particular (FDR: 0.82→0.00, SHD: 16→12) is striking and unexplained — a single unreplicated run on an 11-node graph is insufficient to trust this number. A real-data benchmark at n≥100 is needed.

- **Inconsistency between λ=0.5 in tables and the theoretical range in Eq. (5).** The paper claims λ=0.5 "lies within (5)," but at typical subgraph coverages (m≈10, t=0.7, ε=0.05), the upper bound of Eq. (5) is approximately −ln(0.05)/10 ≈ 0.30, placing λ=0.5 outside the guaranteed interval. The plateau argument implicitly handles this (once above the upper bound, the score approximates A/m), but the paper's explicit claim that λ=0.5 lies within (5) should be qualified or supported with the relevant m values from the experiments.

- **Table 3 runtime does not separate MB identification time from local learning time.** The paper says VISTA includes "total computing time," but MB identification (using IAMB or HITON-MB) is itself non-trivial and grows with graph size. Without knowing what fraction of the VISTA runtime is MB identification vs. local learning, it is unclear how much of the speedup is attributable to the divide-and-conquer strategy per se vs. the subgraph sizes being small. This breakdown would strengthen the efficiency claim.

- **Latent confounding from subgraph restriction is a theory gap, not only a practical limitation.** The paper correctly notes in the conclusion that restricting the learner to MB-induced subgraphs introduces unobserved confounders relative to the full graph. This affects orientation accuracy in local learners and is currently treated as a "future work" limitation. It should at least be acknowledged in the theory section, since Proposition 3.1 guarantees coverage but says nothing about correct orientation under induced confounding.

### Trivial
- VISTA-NV is framed as a positive result ("NV lifts recall") despite exploding SHD (208→3171 for NOTEARS on ERS). The paper eventually explains that WV filters NV's false positives, but the presentation of NV as a feature rather than an intermediate artifact could mislead a casual reader. A brief note clarifying NV's role as diagnostic rather than deployable would improve clarity.

---

## Nice-to-Haves

- A partial analysis bounding the correlation among MB-subgraph votes under standard sparsity assumptions (e.g., bounded degree d) would substantially strengthen the theory. Even an approximate independence result under low-degree settings would transform the current "qualitative guide" into a genuine convergence argument for the actual algorithm.
- Adding a larger real-data benchmark (e.g., a gene regulatory network with ≥100 nodes) would considerably bolster the paper's scalability claims, which currently rest entirely on synthetic experiments.
- Moving the DCILP comparison to the main body (or at minimum summarizing it in a table footnote) would let readers assess absolute performance without relying on a stripped appendix.
- Reporting Figure 4's sensitivity curves at t=0.7 (the main-table operating threshold) rather than t=0.5 would make the sensitivity analysis directly comparable to the reported results.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "Proposition 3.1 is a tautology."** While it is simple, formalizing foundational coverage as a proposition is standard practice in framework papers and provides a verifiable precondition for subsequent results. Removed as a nitpick.

- **Harsh Critic: "GOLEM SHD 567→306 for WV — the gains are moderate."** For GOLEM specifically, the F1 improvement (0.35→0.60 on ERS) and FDR reduction (0.61→0.23) are substantial by any standard. The critic's framing that gains are uniformly "moderate" does not match the data for weaker base learners. Removed as factually incorrect.

- **Harsh Critic: "VISTA-NV SHD inflation is presented misleadingly."** The paper clearly presents NV as a straw-man variant whose recall gain comes at the cost of precision, and explicitly introduces WV as the principled fix. The pipeline structure is not hidden. Removed as misreading the framing.

- **Strength Finder: "Theoretical justification converts heuristic aggregation into principled procedure with finite-sample bounds."** This overstates the guarantee; the bounds apply to an idealized independent-vote model. Retained as a partial strength with the caveat applied in the review above.

- **Strength Finder: "Proposition 3.1 provides non-trivial coverage guarantee."** The result follows directly from the definition of Markov Blanket in one line. It is a useful formalization but not a novel or non-trivial result. Removed as overstated.

---

## Novel Insights

The most genuinely novel architectural insight is that edge-level voting weight can be made *retraining-free*: because λ appears only in the aggregation step and not in the local learning step, the full precision–recall frontier can be swept by recomputing scores over cached edge counts. This decoupling — costly learning once, cheap aggregation many times — is the practical heart of the framework and is not foregrounded enough by the authors. The theoretical insight that O(log n) independent subgraph samples per edge suffice for consistency is clean, even if the independence assumption is idealized. The empirical finding that VISTA stabilizes performance as graph size grows (Figure 1), even for learners that collapse at n=300, is a concrete and reproducible contribution that validates the divide-and-conquer intuition.

---

## Suggestions

1. **Close the independence gap in the theory.** Derive, even approximately, the covariance between votes on the same edge from two overlapping MBs under max-degree-d sparsity. Alternatively, prove a weaker "weakly dependent" consistency result using, e.g., Azuma's or McDiarmid's inequality on a dependency graph of subgraphs. This would transform Theorem 3.5 into a genuine guarantee for the actual algorithm.

2. **Add a real-data benchmark with ≥100 variables.** Use a standard gene regulatory network (e.g., a DREAM challenge network or similar publicly available biological network) with known ground truth. Report multiple runs with standard deviations.

3. **Bring the DCILP comparison into the main body.** Even a single summary row in Table 3 or a small ablation table showing VISTA vs. DCILP on representative settings would address the "absolute utility" question and appropriately position VISTA relative to its closest competitor.

4. **Explain or restore CAM results.** If CAM was excluded because it is too slow for the node sizes tested, say so explicitly. If it was excluded because results were unfavorable to VISTA, include them with explanation — selective omission of named baselines weakens credibility.

5. **Clarify runtime accounting.** In Table 3, explicitly state whether MB identification time is included in the VISTA timing. If it is not, provide a supplementary breakdown.

---

## Evaluation on Key Axes

- **Originality:** Moderate. The divide-and-conquer with MB decomposition is not new; the specific weighted voting aggregation with exponential decay and the associated error bounds are novel, as is the decoupled retraining-free sweep of the aggregation parameter.
- **Importance of research question:** High. Scalable causal discovery is a central open problem; practical plug-and-play wrappers that reliably improve base learners would be widely useful.
- **Claims well supported:** Partially. The model-agnostic improvement claim is well-supported by diverse experiments. The theoretical consistency claim is supported only for an idealized surrogate, honestly acknowledged. The "large-scale" claim rests on synthetic experiments up to n=300; the only real dataset is 11 nodes.
- **Soundness of experiments:** Moderate. Synthetic experiments are thorough (multiple graph types, sizes, base learners, multiple runs). Real-data evaluation is thin (single small network, no standard deviations). Missing CAM results and absent main-body competitor comparison are gaps.
- **Clarity of writing:** Good. The exposition is clear, the pseudocode is readable, and the framework stages are well-described. The framing of VISTA-NV as a feature is slightly misleading.
- **Value to research community:** Moderate-to-high. The code is provided, the framework is truly plug-and-play, and consistent empirical gains across diverse learners and settings are the kind of result practitioners can use immediately.

---

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>