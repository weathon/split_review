Now I have all the information needed. Let me write the consolidated review.

---

## Summary

This paper introduces Distributed Neural Architectures (DNAs) — a novel paradigm where tokens dynamically select their own computation paths through an unstructured collection of modules (transformers, MLPs, attention), with routing learned end-to-end. Unlike feed-forward networks, DNAs have no predefined depth or topology; each token's trajectory through the model is determined by content-dependent router decisions. The authors demonstrate feasibility by training DNA models on ImageNet (ViT scale) and FineWeb-Edu (GPT-2 medium scale), showing competitive performance with dense baselines. They also analyze emergent properties: path distributions follow power laws, individual paths/modules exhibit semantic specialization, and models learn interpretable, content-dependent compute allocation when incentivized via identity-module skipping.

## Strengths

- **Genuinely novel architecture concept.** The idea of a fully distributed neural architecture where any token can traverse any sequence of modules — encompassing MoE, MoD, weight sharing, and early exit as special cases — is conceptually ambitious and opens a new design space beyond incremental modifications to feed-forward networks. The paper convincingly shows that such architectures can be trained end-to-end, which is non-trivial.
- **Cross-domain demonstration.** The same DNA construction is successfully applied to both discriminative vision (ImageNet, ViT scale) and generative language (FineWeb-Edu, GPT-2 scale) tasks. This two-domain validation strengthens the claim that DNAs are a broadly applicable framework rather than a vision-specific or language-specific trick.
- **Competitive performance with dense baselines.** In vision, top-1 DNA reaches 79.1% ImageNet accuracy vs. 79.8% for ViT-small (a 0.7% gap). In language, top-2 DNA achieves 2.674 validation loss vs. 2.720 for GPT-2 medium, while also outperforming on most downstream benchmarks (ARC-E, BoolQ, HellaSwag, LAMBADA, PIQA, WikiText). The paper explicitly positions itself as demonstrating *feasibility*, not SOTA, and the results support that claim.
- **Honest and informative negative findings.** The paper reports that random DNA models also exhibit power-law path distributions, and that language model parameter reuse appears random (unlike vision), providing useful baselines and identifying domain-specific challenges for future work.
- **Emergent parameter reuse.** Vision DNA models spontaneously reuse modules, yielding ~25% non-shared active parameters, and this reuse correlates with image content (low-reuse images lack clear objects). The differential behavior between vision (structured reuse) and language (random reuse) is an interesting finding.

## Weaknesses

### Fatal

None. The paper's core claims — that DNAs are trainable and competitive with dense baselines — are supported by the reported experiments.

### Major

- **"Emergent compute efficiency" is partially pre-determined, not fully learned.** The skip mechanism (Eq. 2–3) uses a bias-based scheme with a target skip ratio $r$ set as a hyperparameter. While the model learns *which* tokens to skip, the overall skip rate is imposed rather than emerging from the optimization objective alone. The paper's framing (Abstract: "compute efficiency/parameter sharing can be learnt from data") overstates the degree of emergence. Furthermore, the 30% skip DNA model underperforms a static 30% shallower GPT-2 baseline on all downstream benchmarks (Table 3), which weakens the claim that dynamic, learned skipping provides an advantage over static depth reduction. A compute-aware loss that lets the router freely discover when to skip would more directly test the "learned from data" claim.

- **Interpretability evidence is entirely qualitative.** Sections 3.2 and 4.2 present selected path groupings, deep-dream reconstructions, and two-paragraph token routing examples to argue for "emergent specialization." However, no quantitative metrics are provided — no clustering purity, no statistical tests comparing trained vs. random routing patterns, and no controlled comparisons against baseline models. The power-law path distribution (Fig. 1c,d) is observed in both trained and random models, which the paper acknowledges but does not quantify how trained distributions differ beyond the exponent. Without systematic metrics, the interpretability analysis remains suggestive rather than persuasive.

### Minor

- **Parameter count comparisons are not fully controlled.** In the language domain, the best DNA model (top-2, 603M total / 433M active params) has more total parameters than the GPT-2 baseline (406M). The paper uses active parameter counts for comparison, which is standard in conditional computation literature, but the total parameter disparity means some of the observed gains could stem from additional capacity rather than the distributed architecture itself. A matched-total-parameter baseline would strengthen the competitiveness claim. (Note: the vision top-2 DNA with skip actually has *fewer* total params than ViT-small, so this concern is domain-specific.)

- **Limited scale of investigation.** The vision models are at ViT-small scale (22M active params) and the language models at GPT-2 medium scale (406M active params), trained on 21B tokens. The authors acknowledge this limitation and state that scaling is future work. While appropriate for an exploratory paper, it means the findings (particularly the emergent specialization and power-law patterns) may not generalize to larger regimes where MoE and related methods are typically deployed.

### Trivial

- The paper would benefit from clearer specification of router initialization and how the bias mechanism (Eq. 3) interacts with top-k sampling in practice. These details are not central to the contribution but would aid reproducibility.

## Nice-to-Haves

- A compute-aware training objective (e.g., FLOPs penalty in the loss) that lets the router freely learn skipping behavior, rather than imposing a target skip rate via bias hyperparameters, would more cleanly test the "emergent efficiency" claim.
- Quantitative evaluation of routing specialization (e.g., normalized mutual information between path identity and class labels, compared against a random-routing baseline) would substantially strengthen the interpretability claims.
- Scaling experiments to larger models/training budgets would help establish whether the observed emergent properties persist at scale.

## Removed Points

These points are flagged as removed from the main review; treat with caution.

- **"Unfair baseline comparison invalidates the core claim of competitiveness" (Harsh Critic #1):** The critic argues the comparison is structurally unfair because DNA models have more total parameters. This is partially addressed above as a minor weakness, but the critic's framing as "invalidating the core claim" is too strong. The paper explicitly states it is not trying to beat SOTA but to demonstrate feasibility. The 0.7% accuracy gap in vision and the competitive language results support the "competitive" claim adequately. The vision top-2 DNA with skip (18M total) actually has fewer total parameters than ViT-small (22M), directly contradicting the critic's implication that all DNA models enjoy a parameter advantage.

- **Claim that "the mechanism is imposed, not learned" invalidates the efficiency narrative (Harsh Critic #2):** Retained above in softened form as a major weakness. The critic's claim that this "directly contradicts" the paper's contribution is overstated — the paper does show learned allocation of *which* tokens to skip, just not the overall rate.

- **"Interpretability analyses are anecdotal and lack quantitative support" (Harsh Critic #3):** Retained as a major weakness. The critic's additional claim that path-distribution power-law similarity between trained and random models "undercuts the claim of emergent structure" is noted; the paper itself acknowledges this observation and discusses differences in similarity measures used by trained vs. random models (Sec. 3.2, footnote 5, Appendix G.2), so this is not a failure to address but rather a limitation of the qualitative analysis.

- **Reproducibility concerns about router initialization and bias interaction (Harsh Critic, Section 2 notes):** These are legitimate implementation details but fall under the "trivial reproducibility nitpicks" category per the hard rules. Moved to Trivial.

- **"Missing appendix, missing proofs" (Harsh Critic, general):** Per hard rules, the parser strips appendix sections. Not a valid criticism of the paper.

- **Pure formatting/style criticisms from the Harsh Critic:** Removed per hard rules.

## Novel Insights

The paper's most genuinely novel observation is that path distributions in DNA models follow power laws even at random initialization, and that training shifts the *qualitative nature* of path specialization (from superficial feature clustering to semantic clustering) rather than fundamentally changing the distribution shape. This suggests that the architecture's combinatorial path space itself induces a power-law structure, and that training primarily reorganizes the *meaning* of paths rather than their frequency distribution. If verified quantitatively at scale, this could have implications for understanding how routing-based architectures organize computation.

## Suggestions

- Add a quantitative metric for routing specialization (e.g., adjusted mutual information between path clusters and class labels, compared against a random-routing baseline) to convert the qualitative interpretability analysis into a testable claim.
- Consider replacing the hyperparameter-controlled skip bias with a compute-aware loss term (e.g., FLOPs penalty) to more directly demonstrate that compute efficiency can be learned from data alone.
- A matched-total-parameter dense baseline for the language experiments would help isolate the effect of the distributed architecture from raw capacity differences.
- The finding that language model parameter reuse is random while vision model reuse is structured is under-explored. A hypothesis about why this occurs (e.g., discrete vs. continuous input spaces, dataset complexity, training objective differences) would add depth.

## Anchor Comparison

| Anchor Paper | Avg Score | How DNA Compares |
|---|---|---|
| S7o8zBYw4V (DARE, dynamic MoE routing) | 4.50 | DNA is more novel architecturally (fully distributed vs. just dynamic expert count) and demonstrates across two domains vs. one. Similar experimental rigor. DNA is stronger. |
| exMMxIakjl (Subjective Depth Transformers) | 3.00 | DNA clearly stronger: DNA achieves competitive results with baselines while Subjective Depth models consistently underperform dense baselines. |
| wPemGNb66V (Informed Routing / LFF) | 4.50 | DNA is more novel in architecture design. Informed Routing has more systematic experiments. DNA's cross-domain validation is a differentiator. Comparable overall. |
| ANKQqRicBM (DiffMoE) | 5.33 | DNA is more architecturally novel (fully distributed routing vs. MoE for diffusion). DiffMoE has stronger quantitative results (SOTA on its benchmark). Comparable quality. |
| BqyPLOkxFY (Cross-layer MoE interpretability) | 5.00 | DNA has the dual contribution of novel architecture + interpretability analysis. BqyPLOkxFY has more rigorous interpretability methodology but less architectural novelty. DNA comparable. |
| XGODWn7HeJ (FleS activation) | 6.67 | FleS has stronger empirical validation across many benchmarks and clearer problem identification. DNA is more ambitious in scope but less rigorous. DNA is weaker. |
| koKWoKaMrE (Tversky Neural Networks) | 7.00 | Tversky has a clear novel concept with demonstrated quantitative benefits. DNA is similarly novel but lacks comparable experimental rigor. DNA is weaker. |

**Calibration:** The paper sits above the 4.5 band (DARE, Informed Routing) due to higher conceptual novelty and cross-domain demonstration. It sits below the 6.67–7.0 band (FleS, Tversky) due to weaker experimental validation and qualitative-only interpretability. It is most comparable to DiffMoE (5.33) and the MoE interpretability paper (5.0) — novel concepts with solid but not outstanding experimental support.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>