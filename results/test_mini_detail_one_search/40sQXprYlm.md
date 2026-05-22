Now I have everything I need. Let me write the consolidated review.

## Summary

This paper introduces Distributed Neural Architectures (DNAs), a new paradigm for neural network design where each token follows a learned, data-dependent path through a collection of modules (transformer blocks, MLPs, attention layers, etc.) rather than a fixed feed-forward structure. The authors train DNA models in both vision (ImageNet classification) and language (autoregressive language modeling) domains, demonstrating that these models are trainable with standard optimization, achieve performance competitive with dense baselines, and exhibit emergent structure including power-law path distributions, interpretable data-dependent compute allocation, and qualitative module specialization.

## Strengths

1. **Genuinely novel conceptual contribution.** The idea of non-feedforward architectures where connectivity emerges from end-to-end training of token routing through an unordered collection of modules is a fresh perspective that extends beyond existing conditional computation paradigms (MoE, MoD, early exit). This opens up a new design space that the community could fruitfully explore.

2. **Cross-domain feasibility demonstration.** Training DNA models in two very different domains (vision classification and language modeling) with different modalities, objectives, and data scales provides credible evidence that the architecture is broadly trainable, not a one-trick pony. The models converge smoothly with AdamW and standard schedules (Figures 2, 6).

3. **Rich qualitative analysis of emergent structure.** The paper goes well beyond just reporting accuracies. It analyzes path distributions (power-law with exponent −1.2 for trained vs. −1 for random), visualizes routing decisions (Figures 3, 4, 8), shows that compute allocation correlates with visual/textual content (Figure 5), and documents emergent parameter sharing. This level of analysis is unusual for a first architecture paper and provides genuine insight.

4. **Competitive results in vision with matched active parameters.** In Table 1, the top-1 DNA (22M active params) achieves 79.1% vs. ViT-small (22M) at 79.8% — within 0.7 points with identical active parameter count. This is a clean comparison that supports the feasibility claim.

## Weaknesses

### Major

1. **Unfair parameter comparison undermines the best language result.** The top-2 DNA (433M active params) outperforms GPT-2 (406M) in Table 3, but this is a 6.6% parameter advantage (27M extra parameters). The fair comparison — top-1 DNA (406M active) vs. GPT-2 (406M) — shows the DNA is slightly *worse* (loss 2.754 vs. 2.720; worse on 6 of 7 benchmarks). The paper's headline claim "competitive with dense baselines" rests heavily on the top-2 result, but the correct matched-parameter comparison tells a weaker story. The paper reports the numbers transparently but does not discuss this caveat.

2. **No comparison to existing conditional computation methods (MoE, MoD, early exit).** The paper repeatedly frames DNAs as "a natural generalization of the sparse methods such as Mixture-of-Experts, Mixture-of-Depths, parameter sharing" and states the construction "includes feed-forward, MoE, MoD, weight sharing, early exit as particular cases." Yet the paper benchmarks against none of these. Without an ablation showing whether the distributed routing structure provides any advantage over a simpler MoE-ViT or depth-wise MoD with the same total modules and training budget, it is impossible to assess whether the added complexity of DNAs is warranted. This is the most consequential experimental gap.

3. **No statistical significance or multiple seeds.** All experiments report single runs. The vision gap between ViT (79.8%) and top-1 DNA (79.1%) is only 0.7 points, and the language comparisons involve small differences. Without confidence intervals or standard deviations over multiple seeds, it is impossible to determine whether these gaps are meaningful or within noise — especially given the inherent stochasticity of routing training.

### Minor

4. **No FLOPs measurement.** The paper reports compute only as "number of modules used," which conflates expensive modules (full transformer blocks with attention) with cheaper ones (MLP-only, identity). For any claim about compute savings, FLOPs are the standard currency. This is a notable omission.

5. **Language models are severely undertrained.** Training 400M+ parameter models on only 21B tokens (roughly 50 tokens per parameter) puts results in a pre-convergence regime. The paper acknowledges this ("our models are way too small to truly absorb it"), but still draws conclusions about relative competitiveness. Better-resourced pre-training or smaller models trained to convergence would strengthen the claims.

6. **Missing ablations of key design choices.** Several non-trivial hyperparameters are not ablated: (a) the number of backbone layers \(N_b\) (first N_b layers are dense and non-routed — this could do much of the work); (b) top-k value (k=1 vs. k=2); (c) the bias trick for skip encouragement vs. a fixed skip rate or no skip pressure. Without these, it is unclear which components are essential.

7. **Interpretability findings are entirely qualitative.** The claims about path specialization (Figures 3, 8) and routing encoding semantic meaning (Figure 4, deep-dream reconstruction) are visually striking but not supported by any quantitative metric. The paper acknowledges that random models also cluster images but does not quantify the difference. These results are suggestive but do not constitute rigorous scientific evidence.

### Trivial

None.

## Nice-to-Haves

- A compute-normalized comparison: a dense model whose FLOPs match the DNA's average per-token FLOPs.
- Quantitative interpretability metric: intra-path vs. inter-path patch similarity (e.g., using activation distances), compared to a random model baseline.
- A comparison of the power-law exponent change (−1 to −1.2) against a null model controlling for dataset statistics.

## Removed Points

- **"The compute efficiency claim is not supported by proper baselines (equal FLOPs dense model)."** The paper's primary claim about compute is "compute efficiency/parameter sharing can be learnt from data" (feasibility), not "our models are more compute-efficient than baselines." The paper does show the model learns to skip modules. Demanding a full FLOPs-matched baseline for a feasibility paper is too stringent given the stated scope. However, the lack of FLOPs reporting is retained as Minor weakness #4.
- **"The paper conflates active, non-shared active, and total parameters across model variants."** The paper clearly defines these categories in Tables 1–2 and uses different columns. This is not conflation; it is transparent reporting. The parenthetical "(non-shared active)" is explained and referenced to the efficiency sections.
- **"The parameter sharing analysis in language shows no correlation... undermines the claim that DNAs learn meaningful parameter sharing."** The paper reports this finding honestly and suggests it as a direction for improvement. Reporting a null result does not undermine the paper; it adds credibility.
- **"The bias update rule... no ablation shows this is better than fixed skip rates."** Valid in spirit but too granular for a feasibility paper. Retained as a minor note about missing ablations (#6).
- **"The backbone layers (Nb) are a non-trivial design choice that is not ablated."** Retained in aggregated form in weakness #6.
- **"The deep-dream images... do not constitute rigorous evidence."** Retained in aggregated form in weakness #7.
- **"The comparison of GPT-2 (30% shallover) provides no details on construction."** This is a minor reproducibility concern, too fine-grained for the main weaknesses. The appendix reference is noted.
- Various formatting/style nitpicks about figures, captions, and grammar — these are parser artifacts.

## Novel Insights

The harsh critic correctly identifies the parameter fairness issue in the language experiments — this is the single most concrete threat to the paper's central claim. What is more interesting is the unresolved tension between the paper's two framings: if DNAs are presented as a feasibility study (as stated), then the missing MoE/MoD comparisons and FLOPs accounting are tolerable gaps that future work can fill. But the paper also claims DNAs "generalize" these methods, which implicitly invites comparison. The paper's strongest contribution may not be performance at all, but rather the empirical finding that distributed routing produces power-law path distributions, emergent specialization, and data-dependent compute allocation — phenomena that do not depend on beating baselines. The qualitative evidence for these phenomena is genuinely suggestive even though unquantified, and the paper's honest reporting of null results (e.g., random parameter sharing in language) is a methodological virtue worth noting. The core weakness is that the experimental design treats the paper as a preliminary exploration while the rhetoric (abstract, conclusion) treats it as a demonstrated method, and these two framings are not well reconciled.

## Suggestions

1. **Fix the parameter fairness issue directly:** Either train a top-2 DNA variant with matched active params (~406M) or present the top-1 DNA (matched) comparison as the primary result and clearly discuss the top-2 advantage as a caveat. The abstract should reflect the matched-parameter comparison.

2. **Add at least one conditional computation baseline:** A MoE-ViT with comparable total modules and a layer-skip/MoD baseline trained under the same recipe would be the single most informative experiment to evaluate whether the distributed routing structure provides value.

3. **Report results with 3–5 seeds** for the main comparisons, especially the vision ViT vs. DNA gap (0.7%).

4. **Report FLOPs** alongside module counts, since different modules have different costs.

5. **Quantify the interpretability claims** with a simple metric: e.g., measure intra-path vs. inter-path patch-feature similarity and report the gap between trained and random models.

## Score and Decision

### Calibration Anchors

I compared the paper under review to the following anchors retrieved from the human-review corpus:

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `T26f9z2rEe.md` (DynMoE) | 7.00 | Accepted paper with solid MoE experiments and ablations but incremental novelty. The DNA paper is more novel but much weaker experimentally. |
| `Pu3c0209cx.md` (Tight Clusters) | 7.00 | Accepted paper with strong theory + experiments. The DNA paper lacks comparable theoretical/empirical rigor. |
| `GM7cmQfk2F.md` (Neat Weight Embedding) | 7.00 | Accepted paper with clean experiments and strong baselines. The DNA paper is more novel conceptually but less rigorous. |
| `QHzzAU7Qf9.md` (Soft Merging) | 6.00 | Rejected paper with good baselines but scale limitations. The DNA paper has comparable experimental breadth but more novel concept. |
| `gWHQQagPbN.md` (Beyond 2:4) | 5.80 | Rejected empirical/engineering paper. The DNA paper has more conceptual novelty but similar experimental gaps. |
| `ar9tcnD4e9.md` (Neural Modules) | 4.75 | Rejected paper with similar theme (rethinking NN structure) but weaker experiments. The DNA paper is stronger in both concept and evaluation. |
| `IA3wm5vwUl.md` (Routing Problems) | 3.67 | Rejected paper with weak novelty. The DNA paper is substantially stronger. |

The DNA paper is more novel conceptually than any of these anchors, but its experimental validation has real gaps (unfair parameter comparison in language, no MoE/MoD baselines, no statistics, no FLOPs) that place it below the 6+ accept-worthy papers. It is stronger than the 3–4 range papers. I position it at 5.0.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>