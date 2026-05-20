Now I have a clear picture from the calibration. Let me write the consolidated review. The paper sits in the 3.5–5.0 range — weaker than Nova (5.60, well-specified hierarchical attention for code) and comparable to or slightly below Coarse-Tuning (4.75, clear method but evaluation gaps). The critical differentiator is that the current paper's method is too underspecified to fully evaluate.

---

## Summary

This paper proposes a hierarchical architecture for encoding program code as RL state representations, combining token-level transformer attention, function-level GAT over ASTs, module-level attention, and graph attention over a Code Dependency Graph (CDG). The representation is trained end-to-end with PPO and evaluated on three code-related tasks cast as RL problems: code completion, program repair, and algorithmic problem solving. The ablation study and task-comparative results suggest the hierarchical design contributes positively to performance.

## Strengths

- **Hierarchical design with ablation validation.** Table 2 confirms each component contributes to program repair performance: removing token-level attention drops success rate by 6.2%, function-level by 3.6%, module-level by 2.4%, and CDG edges by 1.9%. This directly supports the claim that multi-level processing is beneficial.

- **Task-adaptive attention patterns.** Section 6.3 reports that module-level attention distance varies by task — mean 2.1 edges for code completion (local focus) versus 3.8 edges for program repair (broader context). This provides evidence that the hierarchical mechanism adapts its representations to different RL objectives.

- **Consistent improvements across three diverse tasks.** Table 1 shows the proposed model outperforms all five baselines on code completion (+4.5 BLEU over CodeBERT), program repair (+5.7% success rate), and algorithmic problem solving (+6.2% pass rate). The pattern of gains across all tasks and all baselines is stronger evidence than a single-task result would be.

- **Scalability advantage over baselines.** Figure 3 shows the model maintains lower prediction error as code complexity grows (18% at 175 functions) while baselines hit 20% error at 100–125 functions. The module-level attention and CDG appear to help with larger codebases.

## Weaknesses

### Major

- **Incomplete method specification — the forward pass cannot be reconstructed from the paper.** Section 4 states that function-level attention "aggregat[es] token's representation into function embeddings" (line 93) but never defines the mapping from token-level transformer outputs to AST node features $\mathbf{h}_u$ used in Equation (2). The CDG is mentioned as a key architectural component (lines 107, 119, 139) but its construction — what nodes and edges it contains, how it is extracted from code — is never defined. Equation (5) concatenates $\mathbf{f}_{\text{main}}$ and $\mathbf{m}_{\text{root}}$ without explaining how these specific embeddings are selected from function- and module-level outputs. A reader cannot sketch a forward pass from the paper alone, which makes the evaluation results ungrounded and reproducibility impossible.

- **RL experimental design is insufficiently specified.** The paper casts code completion, program repair, and algorithmic problem solving as MDPs (line 169) but provides almost no concrete MDP details. Reward functions are described only as "based on prediction accuracy and semantic correctness" (completion, line 165) and "receiving rewards for successful repairs" (repair, line 166). The action space is given as "token-level edits (insert/replace/delete) and (complexity raising functions, name changes of variables) depending on the task" (line 229), which is too vague to assess whether the RL setup meaningfully tests representation quality. Episode termination conditions are not stated. Without these details, it is impossible to determine whether the reported performance differences arise from representation quality or from ad-hoc environment design choices.

- **Statistical evidence is claimed but absent.** The paper states that "statistical significance tested via paired t-tests (p < 0.01)" (line 219), yet no standard deviations, confidence intervals, error bars, or p-values appear anywhere. Table 1 reports single scalar values. Figure 2 learning curves show no error bands. Table 2 ablation results have no variance estimates. The quantitative claims cannot be distinguished from noise based on the presented evidence.

### Minor

- **t-SNE and nearest-neighbor analyses are described but not shown.** Section 6.4 describes t-SNE visualizations and nearest-neighbor analysis results in prose only ("as you can clearly see clustering based on semantic categories," "better maintain functional similarity"), with no actual figures or quantitative metrics. This leaves the representation-quality claims in Section 6.4 entirely unsupported.

- **Scalability analysis uses unnamed baselines with missing data.** Figure 3 and its accompanying table label baselines as "Baseline 1" and "Baseline 2" without identifying which methods these are. The table has empty cells at higher function counts (e.g., only the proposed model reports values at 150 and 175 functions), making the comparison at those points one-sided.

- **Relationship between CDG attention formulations is unclear.** Equation (4) computes CDG attention with LeakyReLU, while Equation (7) introduces multi-head CDG attention with separate edge-type heads. The paper does not clarify whether these are alternative formulations, sequential, or one supersedes the other.

- **Dynamic edge feature learning (Eq. 8) is disconnected from the architecture.** The edge update rule is presented but its role in the overall forward pass — which components use these updated edge features and when — is never connected to the rest of the method.

### Trivial

- The metrics list includes "CodeBLEU score (?)" (line 210) with a question mark, suggesting unresolved uncertainty about the metric definition.
- The Chandak et al. (2019) citation (line 21) is about action representations for continuous control, making its relevance to code embedding limitations unclear.

## Nice-to-Haves

- A step-by-step example tracing a small code snippet through each attention layer would substantially improve clarity and make the architecture concrete.
- Reporting results over multiple training seeds with error bars would transform the evidence from suggestive to substantive.
- Identifying the baselines in the scalability analysis and completing the missing data points would make that comparison fair and interpretable.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic: "Traditional approaches regularly address code embeddings as flat sequences" overstates the gap.** This is introductory framing rhetoric. The paper does cite relevant hierarchical prior work (Gao et al., 2023; Zhou et al., 2022) and differentiates its RL-focused approach. Not a substantive weakness.
- **Harsh critic: "Related work coverage is scattered; several references appear mis-cited."** Beyond the Chandak et al. point (kept as Trivial), this criticism is too vague and lacks concrete anchors. The paper does position itself relative to code representation learning, attention mechanisms, and RL embedding work.
- **Harsh critic: "The limitations section is underdeveloped" and "future applications are speculative."** The paper's limitations section is brief, but criticizing the length of a discussion section is not a methodological weakness. Future work speculation is standard in discussion sections.
- **Strength Finder: "Rigorous, fair experimental protocol."** The shared warm-up phase and equal embedding dimensionality are standard practice, not evidence of particular rigor — and the experimental design is significantly underspecified (see Major weaknesses).
- **Strength Finder: "Interpretability analyses support representation quality claims."** The t-SNE and nearest-neighbor analyses are described only in prose without actual visualizations or metrics (see Minor weakness). This claimed strength is not supported by evidence on the page.

## Novel Insights

None beyond the paper's own contributions. The task-dependent attention distance finding (2.1 vs. 3.8 edges for different tasks) is interesting but would need more systematic analysis — across more tasks, with uncertainty estimates — to qualify as a genuinely novel insight rather than a suggestive observation.

## Suggestions

- The single most impactful revision would be to fully specify the data flow: define how the AST is extracted, how token embeddings are pooled per AST node, how the CDG is constructed from a concrete program analysis pipeline, and how $\mathbf{f}_{\text{main}}$ / $\mathbf{m}_{\text{root}}$ are selected. Until this exists, nothing else in the paper can be properly evaluated.
- Define the MDP for each task concretely: state space, action space with exact enumeration, reward function with equations, termination conditions. These are table-stakes for any paper claiming an RL contribution.
- Add error bars to all tables and figures, report actual p-values, and either show or remove the t-SNE / nearest-neighbor claims. Unsupported claims weaken rather than strengthen the paper.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| FALCON (N18Z2MkMEa) | 3.00 | R1 | Significantly weaker — unclear contribution, limited evidence |
| EReLELA (7ienVkNf83) | 3.00 | R1 | Weaker — narrower scope, less evidence |
| GEPCode (DgGdQo3iIR) | 4.33 | R2 | Comparable — reasonable idea but underspecified contribution; current paper has broader scope but worse specification |
| Coarse-Tuning (vLqkCvjHRD) | 4.75 | R2 | Slightly stronger — clearer method, better-specified experiments; current paper has more ambitious architecture but key details missing |
| Structured Pred Reps (sEv6vHIUnu) | 4.80 | R2 | Similar tier — representation learning for RL with evaluation gaps |
| Nova (4ytRL3HJrq) | 5.60 | R1 | Clearly stronger — well-specified hierarchical attention, rigorous evaluation, clear contribution |
| Code Rep Learning at Scale (vfzRRjumpX) | 5.75 | R2 | Stronger — large-scale, well-evaluated code representation work |
| RepoGraph (dw9VUsSHGB) | 6.20 | R2 | Stronger — clear graph-based method with strong SWE-bench results |
| RECODE (OwtMhMSybu) | 7.33 | R1 | Much stronger — SOTA exploration with rigorous evaluation |

**Round-1 bracket:** 3.5–6.0. The paper is clearly above the ~3.0 anchors (which have fundamental flaws or trivial contributions) and clearly below Nova (5.60, well-specified hierarchical attention with strong evidence).

**Round-2 narrowing:** The paper sits near GEPCode (4.33) and below Coarse-Tuning (4.75). Like GEPCode, the paper has an interesting architectural idea but the evaluation does not fully support the claims. Unlike Coarse-Tuning, which has a clear MDP specification, this paper's experimental design is too vague. The hierarchical attention idea is more ambitious than GEPCode's GNN approach, but the underspecification prevents proper assessment. Score: **4.0**.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>