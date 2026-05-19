- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6
Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper introduces Monet, a Mixture-of-Experts architecture that uses product key composition (horizontal and vertical decomposition of expert weights) to scale to 262,144 experts per layer with O(√N) total parameter scaling relative to expert count. The authors train Monet models at 850M, 1.4B, and 4.1B total parameters, showing competitive performance with dense LLaMA baselines. They further demonstrate that Monet's experts exhibit domain/language-level specialization via masking experiments (removing experts for a domain/primarily hurts that domain), and show toxicity mitigation by purging correlated experts.

## Strengths

- **Genuine architectural innovation for many-expert MoE:** The horizontal and vertical decomposition schemes (Equations 6–15) reduce parameter scaling from O(N) (PEER) to O(√N). This is a clean, well-described contribution backed by the complexity analysis in Table 1 and the computation reorganization in Equations 10–12.

- **Strong evidence of domain-specialized experts via masking experiments:** Figure 3(a) shows that removing Monet's experts assigned to a single MMLU domain causes a sharp accuracy drop primarily in that domain (dark diagonal), while other domains remain largely unaffected—a pattern absent in OLMoE and dense LLaMA baselines (Figure 3c,d). The language masking experiment (Table 2) shows a -30.6% target drop vs. only -1.1% average collateral for other languages.

- **Toxicity mitigation with minimal general-performance impact:** Removing 4.1% of toxic-correlated experts reduces expected max toxicity from 0.795→0.657 (17% relative) on RealToxicityPrompts while average benchmark performance stays at 0.478 (unchanged). Table 4 (ToxiGen) shows a similar pattern.

- **Competitive with dense LLaMA at matched total parameter count:** Monet-VD 1.4B achieves 0.478 (vs. LLaMA 1.3B at 0.484) and Monet-VD 4.1B achieves 0.511 (vs. LLaMA 3.8B at 0.520) in 0-shot evaluation, demonstrating that the MoE overhead does not significantly hurt performance.

## Weaknesses

### Fatal
None.

### Major

1. **"Sparse dictionary learning" framing is not supported by the training objective.** The paper claims (abstract, lines 4, 53, 122, 487) to "incorporate sparse dictionary learning directly into end-to-end Mixture-of-Experts pretraining." However, the actual training objective (Equation 17, lines 199–202) is standard LM loss + uniformity loss + ambiguity loss — there is no reconstruction loss, no sparsity-inducing regularization on activations, and no overcomplete basis with explicit sparsity penalties as in Sparse Autoencoders. The model learns many experts through standard MoE pretraining, not dictionary learning. This inflates the claimed contribution and could mislead readers about the novelty of the approach. The architectural contribution (parameter-efficient scaling) is genuine and does not need this framing.

2. **Evidence for "monosemanticity" is indirect and coarser-grained than the term implies.** The paper's title and central claim center on monosemantic experts (experts responding to a single coherent concept). The evidence is: (a) qualitative examples of 6 selected experts (Figure 2), (b) domain masking showing domain-level specialization (Figure 3), and (c) language masking showing language-level specialization (Table 2). These experiments convincingly demonstrate **domain/language-level specialization**, but not the fine-grained, concept-level monosemanticity the term evokes in the mechanistic interpretability literature (e.g., a feature for "Golden Gate Bridge"). There is no quantitative measure of how many experts are truly monosemantic, no pairwise overlap analysis of expert-token activation maps, and no intervention faithfulness tests. The paper itself acknowledges the expert selection criteria as "basic and minimal" (line 494). Reframing the contribution as "domain-specialized experts enabling knowledge manipulation" would better match the evidence.

3. **The SAE comparison motivating the paper is confounded.** The paper uses Table 1 to compare Monet against Gemma 2 2B + Gemma Scope SAEs and argues that SAEs "fall short in maintaining model stability" (line 268). However, the comparison varies on multiple axes simultaneously: different base architectures (LLaMA-style vs. Gemma 2), different pretraining data scales (100B vs. 2000B tokens), and different total parameter counts (1.4B/4.1B vs. 2B). The observed performance gap between Monet and SAE-degraded Gemma 2 cannot be attributed to the SAE vs. end-to-end training dichotomy — it could reflect any of these confounds. A controlled comparison (e.g., applying SAEs to Monet's own hidden states vs. native Monet) is needed to support the paper's motivational framing. The primary comparison against dense LLaMA (same architecture, same data) is fair and should be foregrounded.

### Minor

4. **Active vs. total parameters are not reported.** The model sizes (850M, 1.4B, 4.1B) list only total parameters. Active parameters per token, which determine inference FLOPs, are not stated. This makes computational efficiency claims hard to evaluate.

5. **Adaptive Routing with Batch Normalization is underspecified.** Section 3 (lines 185–187) states that "Batch Normalization to estimate expert routing quantiles without performing top-k sorting" is used, but does not explain how this interacts with the routing mechanism, whether it fully replaces top-k, how training vs. inference differ, or how it relates to the dense routing formulation in Equations 10–12. This is a reproducibility gap.

6. **Key hyperparameters not reported in the main text.** The top-k value (if any), expert hidden dimension m, number of heads H, and the λ coefficient for load-balancing losses are not provided. The paper uses "dense routing" (line 147) which extends sparse scores to all experts — but it is unclear how the batch-normalization-based quantile estimation selects which experts are "active" and how many receive non-zero scores.

7. **No experimental comparison against PEER or other high-expert-count MoE approaches.** PEER is discussed extensively as related work and as the motivation for Monet's parameter efficiency, but no empirical comparison (performance, memory, speed) against PEER or MuMoE is provided. The experiments compare Monet against dense LLaMA and OLMoE, which are architecturally different.

8. **No analysis of expert utilization.** With 262K experts per layer and dense routing, the paper does not report histograms, utilization ratios, or the number of experts that receive meaningful routing mass across a dataset. The load-balancing losses encourage uniform routing, but no empirical verification is provided.

### Trivial
None.

## Nice-to-Haves

- FLOPs or wall-clock comparison against dense LLaMA and PEER to ground the practical efficiency claims.
- Ablation varying the number of experts to study the effect on interpretability and performance.
- Quantitative monosemanticity metrics (e.g., Jaccard overlap of top-activated tokens between experts, mutual information between expert activations and concept labels).

## Removed Points

These points were identified by the reviewers but are removed from the main review for the stated reasons:

- *"The SAE comparison is not a valid evaluation of the central claim"* — Retained as a major weakness; the central claim about SAE degradation is not fairly tested. However, the SAE limitation is a motivational framing, not the core contribution; the paper's main contribution (parameter-efficient MoE) stands independently.
- *"Evidence for monosemanticity is insufficient to support the core claim"* — Retained as major weakness, but reworded to acknowledge the valid domain-level specialization evidence while noting the claim goes beyond what is shown.
- *"No FLOPs or wall-clock comparison"* — Demoted to nice-to-have; parameter efficiency is claimed, but the paper does not claim runtime improvements.
- *"No ablation of expert count"* — Demoted to nice-to-have; the paper establishes the architecture's functionality but does not promise exhaustive ablations.
- *"Hyperparameters not reported"* — Retained as minor; these are needed for reproducibility.
- *"The domain masking heatmap is qualitative; bar chart with error bars would be more informative"* — Removed (style preference).
- *"The 2× skewness criterion is arbitrary"* — Retained implicitly in the acknowledgment that the paper calls its own criteria "basic and minimal" (limitations section).
- *"Self-Explained Experts subsection"* — This is a qualitative demonstration; the paper itself acknowledges quantitative evaluation is an open question (lines 495-496). Removed as a standalone criticism.
- *Strength about "Avoids post-hoc reconstruction loss of SAEs"* — The comparison showing SAE-degraded Gemma 2 is confounded (see Major weakness 3). Removed from strengths; replaced with the fair comparison against dense LLaMA (Strength 4).
- *"The method is standard MoE with a clever parameter-sharing trick, not dictionary learning"* — This is the same point as Major weakness 1, merged.

## Novel Insights

None beyond the paper's own contributions. The two reviews surface the gap between the paper's ambitious framing (sparse dictionary learning, monosemanticity) and the actual evidence (domain specialization, parameter-efficient routing) but do not offer a fundamentally new perspective on the method or results beyond what is already discernible from reading the paper.

## Suggestions

1. **Reframe the contribution honestly.** Drop the "sparse dictionary learning" framing and describe Monet as a parameter-efficient many-expert MoE architecture that yields domain-specialized experts useful for knowledge manipulation. This matches the evidence and is still a significant contribution.

2. **Add a controlled SAE experiment.** Apply standard SAEs to Monet's own hidden states and compare the performance of the SAE-reconstructed model vs. native Monet. This directly tests the claim about end-to-end training preserving knowledge better than post-hoc SAEs.

3. **Quantify monosemanticity.** Report pairwise Jaccard overlap of top-activated tokens between experts, or measure mutual information between expert activations and concept labels. Compare against expert specialization in OLMoE or a conventional MoE to substantiate the "more monosemantic" claim.

4. **Report active parameters per token and hyperparameters.** State the top-k (or effective active expert count), m, H, λ, and the number of experts removed per domain/language in masking experiments.

5. **Add expert utilization statistics.** Report histograms of expert activation frequencies or routing mass distribution across the 262K experts to verify that the uniformity loss is working.
