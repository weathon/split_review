Now I have all the verification I need. Let me write the consolidated review.

## Summary

The paper proposes a hierarchical attention architecture for code embeddings that combines token-level (transformer), function-level (AST-based GAT), and module-level (GAT with code dependency graph) attention mechanisms, and uses the resulting state representations in reinforcement learning for code-related tasks (code completion on PY150, program repair on ManySStuBs4J, algorithmic problem solving on APPS). The architecture is specified through equations (Eqs. 1–8) and evaluated against five baselines.

## Strengths

1. **Clear architectural specification through equations.** The paper defines token-level relative-position attention (Eq. 1), function-level AST-based GAT (Eq. 2), module-level additive attention (Eq. 3), inter-module CDG attention (Eqs. 4, 7), and dynamic edge feature learning (Eq. 8). These equations provide a concrete, reconstructable description of how the hierarchical attention operates at each level, which is the paper's primary architectural contribution.

2. **Consistent empirical improvements over five baselines across three tasks.** Table 1 shows the proposed model outperforming all baselines on code completion (BLEU 72.9 vs. 68.4 for CodeBERT), program repair success rate (54.3% vs. 48.6%), and algorithmic problem solving pass rate (67.5% vs. 61.3%). The improvement is consistent across all three tasks, suggesting the hierarchical architecture provides genuine benefit beyond any single baseline design.

3. **Ablation study validates each architectural component.** Table 2 shows that removing any level of attention degrades program repair performance: token-level (−6.2%), function-level (−3.6%), module-level (−2.4%), CDG edges (−1.9%), and replacing with uniform attention (−4.5%). This decomposition confirms that each component of the hierarchy contributes positively, not just the overall model size.

4. **CDG integration beyond AST is validated.** The ablation includes removing CDG edges (−1.9%), providing concrete evidence that the semantic dependency graph beyond pure syntactic structure contributes to performance. This goes beyond standard AST-only code representations.

## Weaknesses

### Major

1. **RL framing is superficial and the claimed contribution of end-to-end RL optimization is untested.** The paper claims novelty in "optimizing the embeddings end to end on the purpose of policy learning objective" (Section 1), but the RL setup is critically underspecified: reward functions are described in single phrases ("rewards based on prediction accuracy and semantic correctness," Section 5.1), action spaces are handwaved ("token-level edits (insert/replace/delete) and (complexity raising functions, name changes of variables)," Section 5.5), and the policy and value network architectures that take the hierarchical state **s** as input are never described. The three evaluation tasks (code completion, program repair, algorithmic problem solving) are standard supervised/autoregressive generation problems, and the paper provides no justification for why they need to be formulated as MDPs, nor any experiment showing that RL-based training produces better embeddings than supervised pretraining of the same architecture. Without this, the reader cannot tell whether the reported improvements come from the hierarchical architecture, the RL training protocol, or the specific task framing. This undercuts the paper's core framing as an RL state representation contribution.

2. **The computational efficiency claim in Section 6.6 is unsubstantiated and appears inconsistent with the architecture.** The paper states: *"Memory consumption is linearly proportional to program size with our model, compared to quadratic growth for sequence transformers"* but provides zero memory or runtime measurements. The figure that accompanies this claim (Figure 3) only shows prediction error vs. code complexity, not efficiency. Furthermore, the model includes a 6-layer transformer at the token level (Section 5.3), which inherently has quadratic self-attention in the token sequence length. The paper does not discuss any mechanism (sliding windows, sparse attention, bounded function-level token sequences) that would achieve linear scaling. The claim appears to conflate complexity in number of functions (linear) with complexity in total tokens (quadratic), but the model contains a transformer at the token level, so this comparison is uninformative without clarification.

3. **Critical experimental details are missing, undermining reproducibility and evidential value.** (a) Tables 1 and 2 report only point estimates; Section 5.4 mentions *"statistical significance tested via paired t-tests (p < 0.01)"* but no test statistics, confidence intervals, or standard deviations are reported anywhere. The number of independent runs is not stated. (b) Figure 3, a core result on scalability, labels its baselines as "Baseline 1" and "Baseline 2" without identifying them in the caption, legend, or text. (c) The Code Dependency Graph (CDG) is central to the method (Section 4.4), yet the paper never describes how it is constructed from source code—what program analysis framework, what edge types, how nodes align with AST structures. (d) CodeBERT is described as "fine-tuned for RL" (Section 5.2) but no architectural details are given for how the masked language model was adapted to produce state representations for policy learning. These omissions collectively mean the experiments cannot be independently reproduced or fully evaluated.

4. **No comparison to contemporary code models.** The only language-model baseline is CodeBERT (2020), which is six years old. The reported improvements over CodeBERT are modest (4.5 BLEU, 5.7% repair success rate, 6.2% algorithmic pass rate). Without comparisons to more recent code models (e.g., CodeT5, CodeLlama, StarCoder), it is unclear whether the proposed architecture is competitive with current approaches or merely improves over a dated baseline.

### Minor

1. **Ablation conditions are underspecified.** The "w/o Token-Level Attention" ablation (Table 2) removes token-level attention but does not specify what replaces it—does the model skip token processing entirely, fall back to a different mechanism, or use uniform weights? Without specifying the replacement, the ablation tests "whether a transformer at the token level helps" rather than testing the specific role of hierarchical attention.

2. **Attention pattern analysis lacks rigor.** Section 6.3 claims task-dependent specialization (code completion has "attention distance 2.1 edges," program repair has "mean distance 3.8 edges") but provides no standard deviations, no statistical significance, and no description of what the distances are measured on. This is a single-sentence qualitative claim masquerading as analysis.

3. **Method description is difficult to parse in places.** While the equations are clear, the surrounding prose has substantial clarity issues (e.g., *"The transformer part processes token GAT sequences while the one longer the GAT depends on AST AND code dependency graph (CDG) structures"* — Section 4.2). Some of this may be parser artifacts, but the textual description between equations systematically impedes reconstruction of architectural details, including how tokens are aggregated into function-level representations and how "main function" is identified for code without a clear entry point (Eq. 5).

### Trivial

- Section 7.3 ("Ethical Considerations") lists generic AI safety concerns with no specific connection to the proposed architecture; it does not add information.
- The disclosure in Section 9 ("We use LLM polish writing") is non-standard for a disclosure statement.

## Nice-to-Haves

- Disentangle the architecture contribution from the RL framing: show whether the hierarchical encoder produces better representations under supervised training before adding RL fine-tuning. This would directly test whether "end-to-end RL optimization" (the claimed novelty) provides additional benefit beyond the architecture itself.
- Add memory and runtime measurements to support or retract the efficiency claim.
- Provide full MDP specification (state space, action space with vocabulary and constraints, reward functions, policy network architecture) for reproducibility.
- Report means and standard deviations over multiple seeds, and identify the baselines in Figure 3 by name.

## Removed Points

- Criticism about the paper lacking visualizations of attention patterns: The extracted text mentions t-SNE visualizations (Section 6.4) and attention analysis; figures may have been stripped by the parser. Not verifiable.
- Criticism about the ethical considerations section being generic: True but trivial; does not affect the scientific contribution.
- Criticism about missing related works (Gao et al. 2023, Wang et al. 2020b differentiation): The paper does differentiate from these works (Section 2), albeit briefly. The point lacks specific textual anchor for a weakness.
- Criticism about "what does main function mean for code without a clear entry point (libraries)": A reasonable implementation question but a minor detail; the paper could clarify in camera-ready.
- Criticism about Section 9 being an "unusual inclusion": The section is a disclosure statement; this is neither a weakness nor a strength.
- Strength about end-to-end RL optimization: The paper claims this but provides no experiment demonstrating its benefit vs. supervised learning of the same architecture. Not a verified strength.
- Strength about task-adaptive attention patterns: The evidence (two numbers without variance or context) is too thin to qualify as a strength.
- "No comparison to recent code models" kept above as Minor, but note the instruction about not questioning model existence: This is about missing baselines, not questioning whether models exist. However, reframed as a minor limitation rather than major, since CodeBERT is a reasonable baseline and the paper still compares against five diverse methods.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Restructure the paper as a general-purpose hierarchical code encoder contribution and either substantially strengthen the RL framing (with full MDP specification and an experiment isolating the effect of RL vs. supervised training) or remove the claim of RL-specific novelty.
2. Provide memory/runtime measurements across program sizes, or remove the efficiency claim in Section 6.6.
3. Identify Baseline 1 and Baseline 2 in Figure 3 by name. Report means and standard deviations over multiple seeds for all main results.
4. Describe CDG construction in detail (program analysis tools, edge types, node alignment), as the graph structures are integral to the method.
5. Improve the clarity of the prose between equations, particularly the descriptions of how representations flow between hierarchy levels.

## Score and Decision

**Anchors used for calibration:**

| Anchor | Avg Score | Round / Source | Comparison |
|--------|-----------|----------------|-----------|
| FALCON (N18Z2MkMEa) | 3.00 | R1-topic-low | Similar failure modes (poor writing, missing RL details, no variance) but worse; our paper has clearer equations and more empirical tasks |
| EReLELA (7ienVkNf83) | 3.00 | R1-topic-low | Not directly comparable (emergent language for RL); similar score band |
| Compositional World Models (EHmjRIA4l2) | 3.00 | R1-topic-low | Not directly comparable |
| HRL + LLMs (6y00rooi7i) | 4.75 | R1-topic-mid | Better presented with clearer contribution; our paper is noticeably weaker |
| PcLast (NlBuWEJCug) | 4.50 | R1-topic-mid | Not directly comparable (planning latent states) |
| Reconciling Spatial/Temporal (odY3PkI5VB) | 6.33 | R1-topic-mid | Accepted; much stronger theoretical and empirical contribution |
| Nova (4ytRL3HJrq) | 5.60 | R1-topic-mid | Accepted; hierarchical attention for assembly code with thorough evaluation; much stronger paper |
| CodeSage (vfzRRjumpX) | 5.75 | R1-topic-mid | Accepted; code representation learning with thorough experiments and clear writing; much stronger paper |
| Coarse-Tuning Code with RL (vLqkCvjHRD) | 4.75 | R2 | Similar domain (RL for code); clearer writing and better-specified method; our paper is weaker |
| RLEF (zPPy79qKWe) | 4.50 | R2 | Similar domain; stronger empirical grounding |
| Weak Bisimulation (x7Q0uFTH2a) | 3.75 | R1-weakness-MDP | Similar issues with RL setup underspecification; comparable quality |
| Solving Robust MDPs (Zi1QNJKXAD) | 3.20 | R1-weakness-MDP | Similar underspecification issues; comparable |
| Interchangeable Token Embeddings (iflKXk8oeg) | 3.75 | R2 | Similar presentation issues, less empirical contribution; our paper slightly stronger |
| Unmasking Version-Switching (7rxn2wnx88) | 3.50 | R2 | Different domain but similar presentation issues |
| Codev-Bench (c2C2NQKjZw) | 4.25 | R1-weakness-ablation | Better presented benchmark paper |

**Round 1 bracket:** Based on topic-anchored queries, the paper sits between the low band (avg ~3.0, papers with unclear writing and missing details) and the mid band (avg 4.5–6.3, papers with clearer contributions and stronger evaluation). Weakness-anchored queries confirm that papers sharing this paper's specific failure modes (underspecified RL setup, missing variance, unsubstantiated claims) cluster in the 3.0–4.25 range.

**Round 2 narrowing:** The most directly comparable anchor is Coarse-Tuning (4.75), which addresses a similar topic (RL for code generation) with clearer writing and better-specified methodology. Our paper is noticeably weaker on presentation and evidential rigor. The closest match in overall quality and failure profile is the 3.5–3.75 range, where papers share similar presentation issues and missing experimental details. The paper's clear architectural equations and consistent (if incompletely reported) empirical results lift it above the 3.00 FALCON baseline but not to the 4.75 Coarse-Tuning level.

**What the low-band anchors failed at:** Poor writing quality obscuring the method, missing implementation details that prevent reproducibility, insufficient evaluation rigor (no variance, missing baselines), and claims that outpace the evidence. The paper under review shares these failures to a degree that places it in the low band, though its architectural equations and multi-task evaluation are better than the lowest anchors.

**Score rationale:** The paper has a clear architectural contribution (hierarchical attention with equations) and consistent empirical gains across three tasks with ablation support. However, it is seriously undermined by: (1) a superficial RL framing that does not deliver on the claimed contribution of end-to-end RL-specific optimization, (2) an unsubstantiated and likely inconsistent efficiency claim, (3) missing experimental rigor (no variance, unidentified baselines in Figure 3, absent CDG construction details), and (4) prose that systematically impedes understanding. The combination of these weaknesses means the paper in its current form does not meet the bar for acceptance. A major revision addressing the RL framing, efficiency claim, experimental rigor, and writing could make this a solid contribution.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>