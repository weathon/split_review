Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

---

## Summary

This paper introduces Online Continual Graph Learning (OCGL), a formal framework that bridges Online Continual Learning (OCL) and Continual Graph Learning (CGL) in a node-streaming, task-free setting. The authors construct benchmark datasets by adapting four standard graph datasets to a class-incremental node stream, evaluate six CL methods (adapted for the online setting), and identify the neighborhood expansion problem in multi-hop GNNs — proposing fixed-size neighborhood sampling as a preliminary mitigation. The experiments show replay-based methods (especially A-GEM) generally outperform regularization methods.

## Strengths

- **Principled formalization of OCGL (Section 3).** The paper provides a clear problem definition with an evolving graph, bounded mini-batch constraints, a Past Information Store, and task-free streaming. This bridges a genuine gap between OCL and CGL and provides useful vocabulary for standardizing future work. The definition is general enough to accommodate various stream constructions.

- **Comprehensive benchmarking with proper online hyperparameter selection.** The paper adapts four datasets of varying scale and density (CoraFull, Arxiv, Reddit, Amazon Computer), evaluates six CL methods (ER, EWC, A-GEM, LwF, MAS, TWP) with two batch sizes, uses three metrics (AA, AF, AAA), and follows the online-valid hyperparameter protocol of Chaudhry et al. (2018b) using only the first 20% of tasks. The results consistently show replay methods outperforming regularization methods, providing a solid reference for future work.

- **Identification of the neighborhood expansion problem as a unique challenge for OCGL.** The paper correctly isolates this issue (Section 3.2, Figure 2) as specific to graph-structured data and orthogonal to forgetting — growing neighborhoods can make per-batch computation unbounded even if the model architecture is otherwise efficient. This framing is valuable for the community.

- **Anytime evaluation and per-task breakdown (Figure 1).** The AAA metric and per-task accuracy plots provide insights beyond final accuracy, revealing that regularization methods (EWC, MAS) offer more stable but lower performance while replay methods show higher variance with occasional backward transfer — a useful characterization of the stability-plasticity trade-off.

## Weaknesses

### Fatal
None.

### Major

- **Transductive message passing in experiments does not fully align with the OCGL framework.** The paper states (line 72): *"A transductive setting is used: validation and test nodes are not used for loss computation, but they are still used for message passing."* This means that during training, the GNN aggregates information from nodes (val/test nodes, and potentially future nodes in the stream) that would not yet have arrived in a strictly online deployment. The OCGL definition (Section 3) specifies that at time *t*, the graph snapshot G<sup>t</sup> contains only nodes up to *t*, and the Past Information Store should reflect this temporally constrained view. Because the experiments use the full static graph for message passing instead of a temporally growing graph, the reported accuracy numbers do not strictly represent a realistic online setting where future nodes are unknown. This is a meaningful limitation; while the core comparative findings (replay > regularization) are likely robust, the absolute accuracy numbers and anytime plots are affected by structural information the model would not have in practice. The paper acknowledges the transductive choice but does not discuss it as a limitation.

### Minor

- **Neighborhood sampling experiments are preliminary.** Section 7 tests only a single fixed-size uniform sampling budget per dataset (5, 10, or 15 neighbors) with no comparison to other sampling strategies (e.g., importance sampling, layer sampling, or GraphSAGE-style variable-size sampling). No runtime or memory measurements are reported to substantiate the claimed efficiency benefit. The observed performance degradation is noted but not analyzed in terms of forgetting dynamics, and the paper defers deeper investigation to future work. While this is acceptable as a first exploration (the paper is transparent that "more research is required"), the contribution here is limited.

- **No sensitivity analysis for the class-incremental stream construction.** The streams are built by grouping nodes into fixed 2-class tasks with a single class ordering. The paper does not assess how results vary with different class orderings, task sizes, or numbers of classes per task. Since the findings could be sensitive to these choices, the generalizability of the conclusions is somewhat unclear.

- **The single GCN layer on Reddit (vs. 2 layers elsewhere) introduces an uncontrolled architectural variable.** The paper justifies this choice by citing the high average degree (984) and neighborhood expansion (Section 5, line 75). This is reasonable, but it means cross-dataset comparisons of absolute accuracy are confounded by differing model capacity. The sampling experiments in Section 7 use 2 layers on all datasets, which partially addresses this — but the full-neighborhood results (Section 6) remain affected.

### Trivial
None.

## Nice-to-Haves

- Report runtime and peak GPU memory for full-neighborhood vs. sampling settings to empirically support the efficiency motivation.
- Include at least one comparison sampling strategy (e.g., GraphSAGE-style sampling) to establish whether degradation is sensitive to the sampling approach.
- For one dataset (e.g., CoraFull), repeat experiments with 3–5 random class orderings to quantify variance due to task ordering.
- Provide per-task accuracy plots (analogous to Figure 1) for the sampling experiments to examine whether sampling amplifies forgetting.
- Discuss the transductive choice explicitly as a limitation and, if feasible, include an experiment on a small dataset using a strictly inductive setting to bound the effect.

## Removed Points

- **Criticism about tables being images (Tables 1–4).** The original PDF contains proper tables; the parsed text renders them as images. This is a parser artifact, not an author error. *Removed per rule about formatting artifacts.*
- **Criticism about missing appendix content.** The parser strips appendix sections from all papers. *Removed per rule.*
- **Criticism about the results not supporting any conclusions.** The experiments still provide valid comparative insights between methods; the transductive issue is a real limitation but does not invalidate all conclusions. *Removed the overstatement; kept the underlying concern as a Major weakness.*
- **Strong claim that experiments must be completely redesigned with inductive evaluation.** This is a suggestion, not a requirement for a first benchmark paper. Keeping the limitation noted but not demanding full redesign. *Moved to Nice-to-Haves.*
- **Criticism about the paper not analyzing why some methods are more robust to sampling.** The paper is a benchmark paper presenting initial results; such analysis would be a deeper investigation beyond the stated scope. *Removed; the paper is transparent about preliminary nature.*

## Novel Insights

None beyond the paper's own contributions. A genuinely novel angle would be the observation that the neighborhood expansion problem interacts with forgetting in unexpected ways — for instance, ER performing better on Arxiv under sampling than without (Table 5–6) — but the paper does not develop this. The reviews do not surface an insight the paper itself missed.

## Suggestions

1. **Add an explicit "Limitations" paragraph** discussing the transductive message-passing choice, quantifying how it differs from a strictly online temporal constraint, and (if possible) including a small-scale inductive experiment to bound the effect.
2. **Expand the neighborhood sampling analysis** with runtime/memory figures, a second sampling strategy, and per-task forgetting breakdowns to substantiate the efficiency and robustness claims.
3. **Acknowledge the lack of sensitivity analysis** for class ordering and task size as a limitation, and consider adding one such analysis for the smallest dataset (CoraFull) to establish bounds on result variability.
4. **Clarify in the problem definition** whether the graph snapshot at time *t* should be strictly restricted to the nodes observed up to *t*, or whether the authors intend the transductive setting as the standard for OCGL benchmarks.

## Score and Decision

The paper makes a clear contribution by formalizing OCGL and providing a comprehensive initial benchmark. The transductive experimental setup is a real limitation that prevents the results from fully representing a strict online setting, but the paper is transparent about the choice, and the core comparative findings retain value. The neighborhood sampling experiments are appropriately scoped as preliminary. Overall, the paper provides a solid foundation for future work in this area.

**MY FINAL SCORE:** <pineapple>7.0</pineapple>
**MY FINAL DECISION:** <orange>Accept</orange>