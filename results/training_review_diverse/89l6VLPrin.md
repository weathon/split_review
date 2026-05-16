Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper introduces two graph representation learning methods — graph t-SNE (for 2D layouts) and graph CNE (for high-dimensional contrastive embeddings) — and unifies them under a neighbor-embedding framework. Graph t‑SNE applies standard t‑SNE optimization directly to the graph adjacency matrix and convincingly outperforms existing layout algorithms on local structure preservation. Graph CNE uses an MLP with the InfoNCE loss and graph edges as positive pairs, achieving competitive node representations without a GCN architecture and outperforming all existing MLP-based GCL methods.

## Strengths

- **Graph t‑SNE yields large, consistent improvements over strong layout baselines.** Across all six benchmark datasets and both metrics (kNN recall, kNN accuracy), graph t‑SNE outperforms FDP, DRGraph, and t‑FDP by substantial margins — 18.2 percentage points average improvement in recall and 6.7 in accuracy over the best competitor (Figure 3). The improvement is especially pronounced on the largest graph (ogbn-arxiv), where competitor performance degrades steeply. This evidence directly supports the claim of state-of-the-art local structure preservation.

- **Remarkable simplicity contrasts favorably with existing methods.** Graph t‑SNE uses openTSNE with default parameters; graph CNE uses a standard MLP with off-the-shelf Adam and InfoNCE loss. This contrasts sharply with the custom approximations, hand-crafted forces, and complex heuristics of competing layout algorithms (DRGraph, t‑FDP, tsNET) and GCL methods. The results are therefore easy to reproduce and deploy.

- **Conceptual unification of graph layouts and GCL under neighbor embeddings is novel and valuable.** The paper shows that both 2D non-parametric layouts (graph t‑SNE) and high-dimensional parametric contrastive embeddings (graph CNE) can be implemented by applying the same neighbor-embedding machinery to the graph adjacency matrix. The introduction of parametric 2D embeddings as a "missing link" (Figure 1) is a nice bridging idea that connects the visualization and representation learning literatures.

- **Graph CNE consistently outperforms all existing MLP-based GCL methods.** On every dataset where MLP-based comparisons exist (Local-GCL MLP, GRACE MLP), graph CNE achieves higher linear accuracy (Table 2). This is a meaningful result because it controls for architecture: the advantage comes from the CNE/InfoNCE framework, not from using a GCN.

## Weaknesses

### Fatal

None.

### Major

- **Uncontrolled comparison for graph CNE vs. GCN-based GCL methods (Table 2).** The paper borrows baseline numbers from external papers without matching train/test splits, evaluation procedures, or potentially even dataset versions. The paper uses a 2/3–1/3 random split, while most GCL benchmarks use fixed per-class splits (e.g., 20/30 per class for Cora/Citeseer/Pubmed). This methodological gap means the claimed "state-of-the-art" performance cannot be reliably assessed. The abstract states "state-of-the-art linear classification accuracy" for graph CNE, which overstates what the uncontrolled comparison can support. The more measured language in Section 6 ("comparably to the state-of-the-art") and the Discussion ("comparable performance") is appropriate, but the abstract should be revised to match.

### Minor

- **Default-parameter comparison for layout baselines is acknowledged but its limitation is under-discussed.** The paper transparently states that FDP, DRGraph, and t‑FDP are run with default parameters, while graph t‑SNE also uses default parameters. However, it does not discuss whether tuning the baselines (e.g., adjusting repulsive/attractive force parameters in DRGraph) could partially close the gap. The gains are large (18 pp recall) so this is unlikely to change the conclusion, but the paper would be stronger with a brief sensitivity note or a small hyperparameter sweep for one baseline.

- **No ablation or sensitivity analysis for graph CNE hyperparameters.** The number of negative samples (set to 100 from a default of 5) and the batch size formula (min{1024, |V|/10}) are stated but their effect on final accuracy is not shown. A brief sensitivity study on one or two datasets would strengthen the robustness claim, especially since these parameters directly affect training cost and could interact with dataset size.

- **Missing layout baselines.** ForceAtlas2 and LinLog are mentioned in the related work but not benchmarked. While the choice of FDP, DRGraph, and t‑FDP (two recent SOTA methods plus a classic baseline) is defensible, including at least ForceAtlas2 — a widely used practical standard — would have made the evaluation more comprehensive.

- **MLP-based GCL numbers come from non-standard sources.** The MLP baselines (Local-GCL MLP, GRACE MLP) are cited from an OpenReview discussion thread and a single paper, making it difficult to verify how those numbers were obtained under exactly what conditions.

### Trivial

- **Inconsistency between abstract and body claims.** The abstract claims "state-of-the-art linear classification accuracy," while Section 6 says "comparably to the state-of-the-art" and the Discussion says "comparable performance." The abstract language should be aligned with the more measured body text.

- **Graph t‑SNE variability not reported.** Graph CNE reports mean ± std over five runs (Figure 4), but graph t‑SNE results (Figure 3) are shown as single values. While the deterministic initialization makes variation unlikely, a brief note on stability would be helpful.

## Nice-to-Haves

- A controlled comparison with at least one GCN-based GCL method (e.g., DGI or GRACE) under matching train/test splits for a subset of datasets would significantly strengthen the graph CNE evaluation.
- Tuning layout baselines over a small grid (or reporting the range of performance across parameter choices) would remove the "tuning advantage" concern for graph t‑SNE.
- Including common GCL datasets such as WikiCS or Coauthor CS/Physics would broaden the empirical scope.
- A brief paragraph explaining in a more principled way when the neighbor-embedding perspective on graphs might fail (beyond planar graphs) would sharpen the conceptual contribution.

## Removed Points

These points were flagged by reviewers but are removed or downgraded after verification against the paper:

- **"Overclaimed conceptual contribution"**: The reviewer faults the paper for not providing deep theoretical analysis beyond the observation that both paradigms can be cast as neighbor embeddings. However, the paper claims a *practical unification* — it shows that both tasks can be *implemented* via the same neighbor-embedding machinery — and delivers exactly that. The critic demands a different kind of contribution (theoretical) that the paper never promises. This is a strawman.

- **"MLP over GCN defense is unconvincing"**: The paper's argument for MLP (ability to process held-out nodes one at a time) is a legitimate design philosophy stated in the Discussion and acknowledged as a design choice, not a tested empirical claim. Criticizing it as unsupported confuses a design rationale with an empirical result. The paper does not claim to have tested this advantage; it merely offers it as motivation. This is scope-creep criticism.

- **"Code availability not stated"**: The paper does not claim to release code, so noting its absence as a weakness is questioning the release status of something the paper doesn't promise. Not a valid weakness.

- **"Missing WikiCS/Coauthor datasets"**: Demanding additional datasets is a wishlist item, not a weakness — the current set of six is standard and sufficient to demonstrate the method.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one genuinely novel observation: the contrast between the two halves of the paper is instructive. Graph t‑SNE's evaluation is well-controlled (same datasets, same preprocessing, same metrics for all methods) and shows decisive improvements — this half of the paper is empirically solid. Graph CNE's evaluation, by contrast, relies on borrowing numbers from external papers under different evaluation protocols, revealing an asymmetry in how the two contributions are validated. This suggests that the paper's core strength (graph t‑SNE) could stand on its own, while graph CNE needs either more rigorous empirical support or more modest claims. The fact that graph CNE beats all MLP-based GCL methods (a more controlled comparison) is under-emphasized relative to the GCN comparison and could be promoted as the primary evidence.

## Suggestions

- **Tighten the abstract** to match the measured language of Sections 6–7. Replace "state-of-the-art linear classification accuracy" with "competitive linear classification accuracy" or "comparable to state-of-the-art GCL methods."
- **For graph CNE**, either (a) re-run at least one GCN-based GCL method (e.g., GRACE or DGI) under the paper's own 2/3–1/3 split so the comparison is controlled, or (b) explicitly demote the GCN comparison to an informal reference and promote the MLP-based comparison (where graph CNE is unambiguously best) as the primary evidence.
- **For graph t‑SNE**, add a brief paragraph acknowledging the default-parameter limitation and, if possible, show that a small hyperparameter sweep on one dataset does not qualitatively change the ranking.
- Add a brief sensitivity analysis for graph CNE's negative-sample count and batch size on one or two datasets (e.g., Cora and ogbn-arxiv).

## Score and Decision

**Evaluation axes**:
- *Originality*: Moderate-high. The core idea (applying neighbor embeddings to graphs) is not entirely novel, but the specific demonstration that off-the-shelf t-SNE/CNE outperforms task-specific methods is original and practically significant.
- *Importance of research question*: High. Both graph drawing and GCL are active areas where simpler alternatives to increasingly complex methods would be valuable.
- *Claims supported*: Partially. Graph t‑SNE claims are well-supported; graph CNE's strongest claims (SOTA) are not fully supported due to uncontrolled comparison.
- *Soundness of experiments*: Adequate for graph t‑SNE; weaker for graph CNE due to the uncontrolled comparison.
- *Clarity of writing*: Good. The paper is well-structured and readable.
- *Value to community*: Moderate. The graph t‑SNE result alone is a useful practical finding. The unification perspective offers conceptual clarity.

The graph t‑SNE contribution alone is a solid, reproducible result with convincing evidence. The graph CNE evaluation is weaker — the uncontrolled comparison undermines the strongest claims — but the method is clearly described, beats all MLP-based alternatives, and the conceptual value of the paper does not rest on graph CNE being SOTA. The paper's core flaws are addressable through claim moderation and (ideally) one controlled experiment, not structural. The paper should **not** be rejected; it requires revisions to match its claims to its evidence.

**Score**: 6.0 — A solid paper with a strong graph t‑SNE contribution and a weaker but still interesting graph CNE component. The overclaim in the abstract and the uncontrolled GCL comparison need to be addressed, but the overall contribution is clearly positive.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>