Now I have all the calibration data I need. Let me synthesize the final review.

---

## Summary

This paper identifies and studies a practical problem in multi-modal entity alignment (MMEA) called Dual-level Noisy Correspondence (DNC), where both intra-entity (entity-attribute) and inter-graph (entity-entity, attribute-attribute) correspondences contain annotation errors. The authors propose RULE, which estimates the reliability of each correspondence via a two-fold principle combining Dirichlet-based uncertainty and similarity-based consensus, uses these reliability scores to down-weight noisy pairs during training and robust attribute fusion, and incorporates a test-time correspondence reasoning (TTR) module using a large vision-language model to uncover implicit attribute connections. The method is evaluated on five benchmarks across seven baselines under inherent, 20%, and 50% noise settings, showing consistent and often substantial improvements.

## Strengths

- **Strong empirical validation of the DNC problem and solution.** Figure 1(b), Figure 3(b) (reliability distributions cleanly separating clean from noisy pairs), and Figure 4 (uncertainty × consensus scatter plots partitioning pairs into the intended 𝒮_U, 𝒮_I, 𝒮_C subsets) provide concrete, well-visualized evidence that the proposed reliability framework effectively identifies noisy correspondences. The bar charts in Fig. 1(b) directly demonstrate that both inter-graph and intra-entity noise degrade standard fusion approaches while RULE maintains high performance.

- **Comprehensive and decisive experimental results.** Tables 1–2 cover five datasets (ICEWS-WIKI, ICEWS-YAGO, DBP15K in three language pairs) across three noise regimes (inherent, 20%, 50%), against seven state-of-the-art baselines. RULE consistently ranks first across all settings, with average H@1 gains of e.g., 6.8 points over the second-best in the inherent Non-name setting. Figure 3(a) further demonstrates that RULE's performance degrades markedly more slowly than all baselines as noise increases, directly supporting the robustness claim.

- **Well-executed ablation study clearly attributing gains.** Table 3 isolates each module: removing DRL collapses Non-name H@1 from 58.2 to 31.6 under 50% DNC; removing DRF drops it to 50.4; removing TTR reduces it to 56.5 (still well above the best baseline at 42.4). This cleanly demonstrates that the training-time robustness components carry the bulk of the improvement, with TTR providing a complementary boost. The "Only Unc." and "Only Cons." variants further validate that both principles are needed. Figure 5 qualitatively confirms that reliability weights correctly suppress noisy attributes during fusion.

- **Genuinely novel test-time reasoning component.** The TTR module, which uses chain-of-thought prompting of an MLLM to uncover latent cross-graph attribute connections during inference, addresses a practical test-time challenge (Fig. 1(c)) that prior MMEA work has not tackled. This is a creative extension beyond standard training-time robustness.

## Weaknesses

### Fatal
None.

### Major

- **Incomplete specification of intra-entity fusion weights w_i^m (Section 2.4).** The paper states that "the inter-graph reliability w_i^m could be employed to identify unreliable intra-entity attributes" and uses these weights in the fusion (Eq. 14), but never provides an explicit formula for computing w_i^m for each modality m. Section 2.2 details reliability estimation only for entity-level correspondences (w_i), noting it is "a showcase." While a reader can infer that the same uncertainty-and-consensus procedure extends to attribute-level correspondences using s_ij^m similarity scores and y_ij^m labels, the paper should provide this extension explicitly — or at minimum state it clearly. The core fusion mechanism depends on these weights, so their computation is not a minor implementation detail. This gap makes the method not fully reproducible as described and should be addressed in a revision.

### Minor

- **Main results conflate training-time and test-time contributions.** All results in Tables 1–2 include the TTR module, which uses Qwen2.5-VL-72B-Instruct (a 72B-parameter model). While Table 3's ablation shows that training-time components alone (w/o TTR) already substantially outperform all baselines (H@1 = 56.5 vs. best baseline 42.4 at 50% DNC Non-name), the main tables do not report results without TTR across all benchmarks. This makes it difficult to cleanly assess the contribution of the core reliability framework independently from the large MLLM. The paper would benefit from presenting primary results both with and without TTR.

- **Novelty framing is slightly overclaimed.** The paper claims to "reveal a new problem" (DNC), but acknowledges prior work that "tackles uncertain correspondences for multi-modal entity alignment" (Chen et al., 2024). DNC's novelty is in the joint formulation and dedicated treatment of dual-level noise, not in the discovery that correspondence noise exists. Reframing the contribution as the first explicit dual-level formulation with a unified solution would be more precise and no less impactful.

- **Unsupported claim about vanilla prompts.** Section 2.5 asserts that "vanilla prompts fail to fully activate the deep reasoning capabilities of MLLM" without any qualitative or quantitative evidence comparing vanilla vs. CoT prompts. This claim should either be supported with evidence or removed.

### Trivial

- The tanh mapping in Eq. 2 (e_ij = exp(tanh(s_ij/τ))) lacks a brief motivation for why similarity is squashed through tanh before exponentiation. A sentence of justification would suffice.
- The paper does not discuss whether the TP-based threshold identification (Eq. 8, relying on argmax(s_i) matching argmax(y_i)) is stable early in training, or whether any warm-up is used.

## Nice-to-Haves

- Report primary results without TTR on all five benchmarks (not just in ablation on ICEWS-WIKI), so readers can assess the pure training-time contribution independently.
- Extend the analytic studies (Figures 3–5, Table 3) to at least one additional dataset beyond ICEWS-WIKI to demonstrate generality of the reliability behaviors.
- Provide a sensitivity analysis for the pair-division threshold β and discuss how performance varies with it.
- Discuss the computational cost and hardware requirements of the TTR module for practitioner guidance.

## Removed Points

*These points were flagged by the harsh critic but are removed from the main review. Treat them with caution.*

- **"50% DNC claim not substantiated in main text."** The paper references Appendix B for the statistic ("over 50% in ICEWS benchmarks"). Since the appendix was stripped by the parser, this cannot be verified from the provided text, but it exists in the original submission. Per review policy, we do not flag appendix-referenced content as missing.

- **"tanh mapping has no motivation — fatal gap."** The tanh in Eq. 2 is a minor design choice (squashing similarity before exponentiation to control evidence magnitude). It does not threaten any core claim. Demoted from the harsh critic's "missing justification" framing.

- **"Pair division thresholds may be unreliable early in training — structural weakness."** The harsh critic speculates that early-training TP identification could be unstable. This is a reasonable point for the nice-to-have section but is speculative without evidence that it actually causes problems. No experiments indicate instability.

- **"Experiments only on ICEWS-WIKI for analysis" — kept as nice-to-have only.** The harsh critic's framing as a significant weakness is disproportionate; the main results cover five datasets, and analytic depth on one is standard.

- **"Method should be evaluated without MLLM on all benchmarks" — downgraded.** The harsh critic framed this as a fatal fairness issue. But Table 3's ablation already shows training-time components alone beat all baselines by a wide margin (56.5 vs. 42.4 at 50% DNC), so the gains are not "partially attributable to the MLLM's external knowledge" in a way that undermines the core claims. The concern is legitimate but minor.

- **Strength Finder: "novel test-time correspondence reasoning"** — kept but noted that the TTR integration is one of the first for MMEA, which is a reasonable claim.

## Novel Insights

The paper's most interesting conceptual contribution is the two-fold principle itself — the observation that uncertainty alone is insufficient to identify noisy correspondences (Theorem 1), because a model can be uncertain about the correct match without being wrong about the annotated one, or conversely, certain about an incorrect annotation. The consensus term elegantly closes this gap by directly measuring whether the similarity signal agrees with the annotation, and the marginal-contribution-based greedy strategy for estimating consensus at test time (when annotations are unavailable) is a creative solution. This decomposition of correspondence reliability into (epistemic uncertainty × annotation agreement) may generalize beyond MMEA to other multi-modal alignment tasks with noisy pairings.

## Suggestions

- Add an explicit subsection or paragraph in Section 2.4 that defines w_i^m as the attribute-level reliability computed via the same two-fold principle as w_i, using s_ij^m similarity scores and y_ij^m labels to derive u_i^m and c_i^m analogously, then computing w_i^m analogously to Eq. 1. This would close the main reproducibility gap.
- Add a column to Tables 1–2 (or a separate table) showing RULE performance without TTR, so readers can cleanly separate the training-time and test-time contributions.
- Tone down the "new problem" language to "first explicit dual-level formulation" — more accurate and still a strong contribution claim.

## Score and Decision

**Calibration anchors used:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| a4O528mek9 (Mul2vec) | 3.00 | R1 | Much weaker — vague method, weak evaluation |
| YrxhSkfHh0 (UniFast HGR) | 3.33 | R1 | Much weaker — limited scope, unclear claims |
| 4qRCiEZGKd (Neural DL Reasoning) | 3.40 | R1 | Much weaker — different problem, less mature |
| jy6Lj3JaOf (MM-GRAPH) | 4.50 | R1 | Weaker — benchmark paper, less methodological depth |
| NNUiUwQWx6 (NeuSymEA) | 5.75 | R1/R2 | Weaker — entity alignment but less comprehensive, rougher execution |
| 5BXWhVbHAK | 6.33 | R2 | Weaker — less comprehensive experiments, narrower scope |
| QQYpgReSRk (MOFI) | 6.25 | R2 | Weaker — different task, less methodological novelty |
| z3dfuRcGAK (GEEA) | 6.67 | R1/R2 | RULE is stronger — more comprehensive experiments, clearer motivation, stronger results |
| uSz2K30RRd | 7.33 | R2 | Comparable — good theory and experiments; RULE has more comprehensive empirical validation but a methodological gap (w_i^m) |
| 9bMZ29SPVx | 7.50 | R2 | Comparable — strong motivation, clean execution; RULE is similar in quality |
| TPZRq4FALB (READ) | 8.00 | R1/R2 | RULE is slightly weaker — READ has cleaner methodology, no missing formula gap, similarly strong experiments |
| 9Cu8MRmhq2 (Norton) | 8.00 | R1/R2 | RULE is slightly weaker — Norton has a fully specified method without gaps, comparably strong empirical validation |

**Round-1 bracket:** The paper clearly sits above the 3.0–3.4 weak band and above the 5.75 rejected entity-alignment paper (NeuSymEA). The GEEA paper at 6.67 (accepted) provides a lower bound — RULE is stronger. The READ/Norton papers at 8.0 provide an upper bound — RULE is slightly weaker due to the missing w_i^m derivation and MLLM entanglement.

**Round-2 narrowing:** RULE lands between GEEA (6.67, accepted with some rough edges) and READ (8.0, well-executed with minor gaps). RULE has stronger empirical results and clearer motivation than GEEA, but a more significant methodological gap than READ. It is comparable to the 7.33–7.50 papers in overall polish and contribution.

**Final score: 7.0.** This reflects a solid, well-motivated contribution with comprehensive experiments and clear practical value, held back from the 8.0 range by the incomplete specification of w_i^m and the somewhat entangled presentation of training-time vs. test-time contributions. The paper is clearly above the accept threshold for a venue like ICLR.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>