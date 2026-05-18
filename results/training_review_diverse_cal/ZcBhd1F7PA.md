Now I have a comprehensive understanding of the paper and the reviews. Let me produce the final consolidated review.

## Summary

This paper proposes Hierarchical Multi-Grained Reasoning (HGR) for Object Concept Learning (OCL), framing the recognition of object attributes and affordances as a many-to-many mapping problem. The method combines (1) a coarse-to-fine hierarchical reasoning module that uses multi-step learnable prompts to progressively localize concept-relevant information via global then instance-level cross-attention, and (2) a counterfactual relation-enhancing module with a concept connection graph network. Experiments on the OCL benchmark show 8.1% and 3.9% mAP improvements over the prior state-of-the-art (Li et al., 2023b) on attribute and affordance recognition, with additional results on NYUd2 and AGD20K.

## Strengths

1. **Well-motivated problem framing.** The paper correctly identifies that OCL is inherently a many-to-many mapping (multiple attributes/affordances per object, and a given attribute can apply across objects) and argues convincingly that standard discriminative representation learning alone is insufficient (Section 1, with concrete examples like cake/pizza/bowl sharing "round"). This framing provides clear motivation for a reasoning-based approach.

2. **Coarse-to-fine hierarchical prompting is a sound design.** The two-step prompt refinement — first aligning text prompts with global visual context via cross-attention (Section 3.1.1), then refining them with object-level instance features (Section 3.1.2) — is technically well-motivated. Table 5 confirms that both stages contribute and that skipping global context hurts performance (row 3 < row 4), a non-obvious result suggesting the method genuinely benefits from multi-granularity alignment.

3. **Consistent and substantial empirical gains across multiple benchmarks.** On the primary OCL benchmark, HGR outperforms the prior SOTA (Li et al., 2023b) by a meaningful margin (8.1% attribute mAP, 3.9% affordance mAP). Additional results on NYUd2 (multi-task scene understanding) and AGD20K (weakly supervised affordance grounding) demonstrate generalization beyond the primary setup. The ablation study (Table 4) isolates each component's contribution, showing that the gains are not driven by a single module.

4. **Ablation and analysis of design choices.** The paper systematically ablates the number of visual concepts (Figure 4, finding k=10 optimal) and prompt flow order (Table 5). These analyses provide practical guidance and strengthen the empirical credibility.

## Weaknesses

### Fatal

None.

### Major

1. **Incomplete specification of the counterfactual loss (Equation 7).** The counterfactual loss is presented as `L_cl = { max{0, γ - (ŷ_β - ŷ_β_mask)}, β_i=1,` with no corresponding case for β_i=0. The text says "We design two loss functions L_cl according to the different affordance label to promise the L_cl should be a positive value," but the second case is never shown. This omission prevents reproducibility of a core claimed contribution. This is the most serious technical flaw in the paper.

2. **Unclear what "causality annotation from the benchmark" refers to (Section 3.2.2).** The paper states it "utilize[s] the causality annotation from the benchmark to strengthen the connection" between attributes and affordances, and that the mask is "generated following (Li et al., 2023b)." The OCL dataset (Li et al., 2023b) provides independent binary labels for each attribute and affordance — it does not provide explicit causal annotations. Whether the "causality annotation" refers to statistical co-occurrence statistics, manually annotated causal pairs, or something else is never explained. Since the paper's claim about causal learning rests on this unspecified resource, the contribution is not fully verifiable.

### Minor

1. **Ambiguity about ground-truth bounding boxes at test time (Section 3.1.2).** The method uses "ground-truth bounding boxes to crop the objects" to compute instance visual features for the fine-grained prompt step. The paper does not clarify whether this requires ground-truth boxes at inference (which would give the method an information advantage over baselines that operate on full images) or only during training. The OCL dataset may object-level "instances" rather than full images, but this needs explicit statement. The NYUd2 experiment raises similar questions since it involves full scene images.

2. **Missing comparison against related prompt-tuning methods.** The related work discusses CoOp, CoCoOp, and Chain-of-Thought Prompting (Section 2), yet none are included as baselines. Since the method's core is multi-step prompt refinement with cross-attention, comparisons to these established prompt-tuning approaches would substantially strengthen the evaluation.

3. **No variance or statistical significance reported.** The experimental results lack error bars, standard deviations across runs, or any measure of statistical significance. Given the method's complexity (multiple learnable prompt stages, GRU iterations, graph network, multiple loss terms with λ₁=0.1, λ₂=1), the reported gains (e.g., 8.1%, 3.9%) could be seed-dependent. This is standard practice to report.

4. **The "reasoning" framing is overclaimed relative to what the method actually does.** The coarse-to-fine module performs sequential cross-attention feature alignment — first at the global image level, then at the instance level. While this is a legitimate and effective multi-stage design, the paper's repeated characterization as "imitating human reasoning" is unsupported by any cognitive grounding or analysis. The method is better described as a well-designed hierarchical feature refinement pipeline.

5. **Fully-connected graph structure conflicts with the causality narrative.** The adjacency matrix A = softmax_c(C_α C_β^T) + I_d creates dense connections between all attribute and affordance concept pairs. This contradicts the paper's own motivation that only specific causal attribute-affordance relations exist. A sparser or learnable graph structure would be more consistent with the claim of modeling causal relationships.

6. **Unsupported novelty claim about the many-to-many framing.** Contribution (1) states "We first summarize OCL as a many-to-many mapping problem." The OCL task definition inherently involves multiple attributes per object and multiple objects per attribute; this characterization is intrinsic to the task rather than a novel insight introduced by this paper.

### Trivial

- The term "two loss function" (line 137) contains a grammatical error but the meaning is clear.

## Nice-to-Haves

- An ablation on the number of GRU iterations (currently fixed at t=3) would help show convergence of the concept update process.
- The concept distinctiveness loss (Equation 9) penalizes all inter-concept similarity uniformly. This may interfere with learning related concepts (e.g., "edible" and "food-related"). A selective orthogonality constraint could be explored.
- Reporting training time and memory cost would be useful given the method's architectural complexity and the large OCL dataset.

## Removed Points

- **Criticism about tables being "rendered as images that were stripped by the parser"**: This is a parser artifact, not an author error. The tables exist in the original submission.
- **Criticism that "the claimed improvements could easily be within noise"**: The 8.1% and 3.9% margins are large enough that the reviewer's "within noise" characterization is overstated. The underlying concern about missing error bars is retained in Minor above.
- **Criticism that the paper does not "demonstrate that this constitutes reasoning in any sense beyond what any multi-stage cross-attention mechanism does" in an overly dismissive tone**: The underlying concern (overclaimed "reasoning" framing) is retained in Minor #4 above in a more measured form.

## Novel Insights

Beyond the paper's own contributions, the most interesting insight that emerges from the reviews is the tension between the paper's dense graph connectivity assumption and its causality narrative. The adjacency matrix forms a fully-connected bipartite structure where every attribute concept attends to every affordance concept with learnable weights. If the goal is genuinely to capture causal relationships (where only specific attribute-affordance pairs matter, e.g., "hard" → "ride"), then the fully-connected graph is architecturally at odds with this goal — it would be straightforward to learn a correlation-based solution that ignores the causality entirely. The fact that the CCC module still improves performance (Table 4) suggests that either (a) the dense connectivity is actually learning to selectively amplify certain paths despite the full connectivity, or (b) the counterfactual loss (even if only partly specified) is doing the causal work while the graph is mostly a featurizer. Disentangling these two alternatives would be a valuable follow-up.

## Suggestions

1. **Fix and fully specify the counterfactual loss equation.** Show both cases (β_i=1 and β_i=0). Clarify whether L_cl is a single piecewise function or two separate loss terms.

2. **Clarify the "causality annotation."** State explicitly what information it encodes, whether it is derived from the dataset labels or from an external resource, and how it differs from statistical co-occurrence.

3. **State test-time input format explicitly.** Clarify whether ground-truth bounding boxes are required at inference. If so, explain whether this is consistent with the OCL benchmark protocol and discuss any limitations. For the NYUd2 experiments, explain how object crops were obtained.

4. **Add prompt-tuning baselines (CoOp, CoCoOp).** Since the paper discusses these methods in related work and uses a prompt-tuning approach, comparing against them directly would strengthen the empirical positioning.

5. **Report results with standard deviation over multiple seeds** (at least 3) for all main experiments, especially given the method's complexity.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>