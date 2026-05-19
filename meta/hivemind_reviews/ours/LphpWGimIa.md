## Summary
This paper trains Sparse Autoencoders (SAEs) on attention layer outputs (the pre-projection concatenated head vectors) across multiple transformer models up to 2B parameters, establishing that SAEs decompose attention outputs into sparse, interpretable features. The paper introduces weight-based head attribution to associate SAE features with specific heads, and demonstrates the tool's utility through two main case studies: discovering that apparently redundant induction heads in GPT-2 Small actually specialize in long-prefix vs. short-prefix induction, and resolving a long-standing mystery about the "positional signal" in the Indirect Object Identification circuit by showing it encodes whether a duplicate token follows "and." The paper also describes Recursive Direct Feature Attribution (RDFA) and releases trained SAEs and an interactive exploration tool.

---

## Strengths
**1. SAE-driven discovery of functionally distinct induction heads (long-prefix vs. short-prefix) that resolves a known puzzle about redundancy.**  
Section 4.2 uses weight-based attribution to hypothesize that heads 5.1 and 5.5 in GPT-2 Small specialize differently, then independently validates this with synthetic data and interventions. Figure 4a shows 5.1's induction score jumps from <0.3 to >0.7 as prefix length increases, while 5.5 starts at 0.7. Figure 4b shows that removing the second repeated prefix collapses 5.1's score to 0.05 while 5.5 remains at 0.43. This goes beyond prior work (Olsson et al. 2022, Nix & Path Patching) that did not identify specialization.

**2. Resolving the "positional signal" mystery in the IOI circuit with causally validated SAE features.**  
Section 4.3 localizes three causally relevant SAE features via zero-ablation (logit difference drop confirms causal relevance), interprets them as encoding "duplicate token that previously followed 'and'," and confirms this with a noising experiment. Perturbing names, absolute positions, and relative positions while preserving the "after-and" relation recovers ~93% of logit difference (Figure 6). Changing "and" to "alongside" drops recovery to ~43%. This directly addresses the unresolved "most interesting future direction" from Wang et al. (2023).

**3. First systematic demonstration that SAEs on attention layer outputs achieve sparse, faithful reconstructions comparable to prior MLP/residual-stream SAE work.**  
Table 1 reports L0 < 20 for most GPT-2 Small layers and >80% loss recovered, with the majority of features judged interpretable via dashboards. The evaluation spans GPT-2 Small (all 12 layers), Gemma-2B, and GELU-2L. The paper open-sources trained SAEs and feature dashboards, enabling reproduction and adoption by the community.

**4. Qualitative characterization of three attention-specific feature families (induction, local context, high-level context) with rigorous specificity/sensitivity analysis.**  
Section 3.3 provides a detailed case study (the "board induction" feature in GELU-2L) including specificity plots, sensitivity analysis with manual inspection of false negatives, and heuristic-driven automated detection of hundreds of induction features.

---

## Weaknesses
### Fatal
None.

### Major

**1. Weight-based head attribution is used pervasively but is never directly validated as a reliable measure of head contribution.**  
The method (Equation 4) computes the norm of each head's slice of the SAE decoder vector as a proxy for "how strongly each head writes this feature." Although the intuition is reasonable — the decoder direction's projection onto each head's subspace indicates how the reconstruction distributes across heads — the paper does not empirically verify whether these weight-based attributions correspond to actual head-level feature dependence. The paper could compare weight-based attributions to DFA (Equation 5, which is exact), or to causal head ablation experiments. This gap undermines the evidentiary strength of the systematic per-head analysis in Section 4.1 and the quantitative polysemanticity estimate that depends on it.

*Why this is Major rather than Fatal*: The long-prefix induction case study (Section 4.2) independently validates hypotheses generated via weight-based attribution with SAE-free synthetic data and interventions, demonstrating the method can generate correct hypotheses even if the attribution scores themselves are not validated. Similarly, the head 10.2 polysemanticity finding (Section 4.1, Figure 3) is validated with non-SAE ablation experiments. So the tool still generates useful insights. However, the systematic head-by-head taxonomy (Section 4.1) and the associated quantitative claims rest on unvalidated attribution.

**2. The quantitative estimate that "at least 90% of heads are polysemantic" is not adequately supported by the methodology.**  
The estimate derives from inspecting the top-10 features per head (by weight-based attribution) and judging whether they are "closely related." This suffers from several problems: (a) it depends on the unvalidated attribution method, (b) the sample of top-10 features per head is arbitrary and could miss features where the head participates outside the top-10, (c) human judgment of "relatedness" is subjective with no reported inter-annotator agreement, and (d) the abstraction level at which features are compared is not controlled. The paper's own text (Section 4.1.1) acknowledges some of these limitations (e.g., "the technique from Section 4.1 is not sufficient to prove that a head is monosemantic," "we missed some monosemantic heads due to missing patterns at certain levels of abstraction"). Nevertheless, the abstract states "at least 90% of the heads are polysemantic" as a headline finding, which over-interprets the data. A qualitative survey ("many heads appear polysemantic; we found only 14 monosemantic candidates") would be better supported than the specific 90% figure.

### Minor

**3. Recursive DFA (RDFA) is claimed as a contribution (item 4 in the introduction) but is not experimentally evaluated in the paper.**  
RDFA is described at a high level (Section 2) and a visualization tool is released. However, the paper presents no experiments showing that RDFA provides accurate or useful circuit traces, nor does it validate the linearity assumptions (frozen attention patterns, frozen LayerNorm) on which it depends. The paper would not be weakened by demoting RDFA from a claimed contribution to a description of a released tool-in-progress.

**4. The reconstruction quality metrics are insufficiently contextualized to calibrate how well the SAEs actually perform.**  
The loss-recovered metric (Equation 2) is the field standard, and the paper appropriately follows Bricken et al. (2023). However, reporting only the percentage of CE recovered (relative to zero-ablation) without absolute cross-entropy values makes it hard to judge absolute reconstruction fidelity. Additionally, the Gemma-2B SAE (L0=90, 75% CE recovered) performs notably worse than the GPT-2 Small SAEs — this discrepancy is not discussed in the main text. The paper claims SAEs are "faithful on the IOI distribution" for circuit analysis but defers those numbers to the appendix.

**5. The claim that "induction features are unique to attention" is slightly over-broad.**  
The paper states "as we are not aware of any induction features extracted by MLP SAEs in prior work, we hypothesize that induction features are unique to attention" (Section 3.2). This inference assumes that prior MLP-focused SAE work would have found induction features if they existed, which is not guaranteed given different training objectives and architectural components. The "hypothesize" wording is appropriate, but the surrounding context could more clearly note the limitations of this inference.

### Trivial
None.

---

## Suggestions
- **Validate or caveat weight-based head attribution.** Either (a) compare weight-based scores to DFA (Equation 5) or causal head ablation on a sample of heads, or (b) explicitly state that the attribution is a heuristic proxy whose reliability is untested, and present the per-head analysis and polysemanticity estimate as qualitative rather than quantitative.
- **Soft-pedal the 90% polysemanticity figure.** Either validate it more rigorously or present the finding as "we found only 14 heads whose top-10 attributed features appeared closely related" without converting to a percentage that implies precision.
- **Either demonstrate RDFA with a concrete example** (even a single circuit trace with validation) or remove it from the list of claimed contributions.
- **Provide absolute cross-entropy values** alongside the percentage recovered in Table 1.
- **Briefly discuss the Gemma-2B results** — the higher L0 and lower CE recovery relative to GPT-2 Small raise interesting questions about scaling that the paper should at least acknowledge.

---

## Score and Decision

**Originality:** 7/10. SAEs on attention outputs are a natural extension of prior work, but the weight-based attribution and the specific case study findings (long-prefix induction specialization, IOI "and" signal) are novel.

**Importance of research question:** 8/10. Decomposing attention outputs and understanding head polysemanticity are timely and important problems in mechanistic interpretability.

**Claims well-supported:** 6/10. The two main case studies are well-supported with independent validation. However, the per-head analysis and the 90% polysemanticity claim are weaker due to the unvalidated attribution method.

**Soundness of experiments:** 7/10. The validated case studies are rigorous (synthetic data, interventions, noising experiments with counterfactuals). The SAE evaluation follows field standards. The main experimental shortcoming is the lack of validation for the attribution method.

**Clarity of writing:** 8/10. The paper is well-organized, the methodology is clearly explained, and the contributions are honestly scoped (the paper explicitly states SAEs are not the main contribution).

**Value to the research community:** 8/10. Open-sourced SAEs, dashboards, and interactive tools, plus two independently-validated empirical findings (induction head specialization, IOI "and" signal) that advance understanding of transformer internals.

Overall, this is a solid tool-demonstration paper with two genuine, independently-validated discoveries. The main weaknesses — unvalidated weight-based attribution and overclaimed polysemanticity estimate — are fixable in revision and do not invalidate the core contributions.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept
