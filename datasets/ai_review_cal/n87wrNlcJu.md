- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3
Now I have a thorough understanding of the paper and the reviews. Let me produce the consolidated review.

---

## Summary

This paper proposes ART (and its convolutional variant ARC), an autoregressive generative model for knowledge graph completion that learns the joint distribution p(S,R,D) over source entities, relations, and destination entities from positive triples only, thereby avoiding negative sampling entirely. By modeling a single joint distribution rather than per-query scoring functions, the method produces globally consistent scores across the KG. The paper introduces a global ranking evaluation protocol and demonstrates strong performance on FB15k-237 global MAP, while remaining competitive on standard local link prediction.

## Strengths

- **Avoids negative sampling while achieving meaningful scores.** The model learns p(S,R,D) from observed triples only, eliminating the need for artificially generated negative samples — a significant practical advantage under the Open World Assumption (Section 4, Figure 2). The kernel density plots (Figure 2c) empirically show that ART does not concentrate unknown-triple scores near zero the way negative-sampling-based methods do (Figures 2a, 2b), supporting the claim that the model is more open to unknown triples potentially being true.

- **Strong global ranking performance on key benchmarks.** On FB15k-237, ART achieves a global MAP of 0.122 and F1* of 0.434, substantially outperforming ComplEx (MAP 0.048, F1* 0.153) and NBF (MAP 0.026, F1* 0.131) — the best baselines by a wide margin (Table 2). This directly demonstrates the value of globally consistent scoring.

- **Flexible prior modeling with informative ablation.** The ablation study (Table 4) explores uniform, frequency-based, and learned priors across three datasets, revealing that the best choice is dataset-dependent and that a learned prior improves MAP on WN18RR and OGBLBioKG. This provides a clear direction for further improvement.

- **Competitive local link prediction while being fully generative.** On standard local MRR (Table 5), ART achieves 0.314–0.355 on the three benchmarks, outperforming the only other probabilistic generative baseline (ComplEx²) on two of three datasets, showing that global consistency does not come at catastrophic cost to local ranking.

## Weaknesses

### Fatal
None.

### Major

- **Baselines constrained to suboptimal rank = 150.** The paper fixes the embedding rank to 150 for all methods "for fairness" (Section 5.1), but this is far below the ranks at which strong baselines are typically deployed (e.g., ComplEx commonly uses rank 2000). The paper itself acknowledges in Section 6 that "future work can increase the rank to 2000 as Complex in this study." Because the headline global MAP improvements (Table 2) are compared against deliberately constrained baselines, the claimed state-of-the-art on global consistency is premature. The margin on FB15k-237 is very large (0.122 vs. 0.048), which suggests the finding is likely robust, but without experiments at standard ranks the reader cannot evaluate this.

### Minor

- **No variance or significance reporting.** All results are single numbers without confidence intervals, multiple seeds, or any discussion of training randomness (Section 5). This makes it impossible to assess the stability of the reported improvements. While single-run evaluation is common in this subfield, it is a limitation when a new evaluation protocol (global ranking) is being introduced.

- **Limited clarity on what p(S,R,D) represents and whether calibration is needed.** The paper states p(S,R,D) is "the probability that a link is sampled from the KG" (abstract) — this is precise. However, claims about "probabilistic semantics for complex reasoning" and "truth value" (Section 6) blur the line between density over observed triples and truth probability. The paper does not include calibration experiments (e.g., reliability diagrams or ECE on a held-out set with known negatives), which would substantiate the interpretive claims. The discussion in Section 6 about min-max normalization for PDB compatibility implicitly acknowledges the gap, but this is not connected back to the main claims.

- **Inverse triples and their effect on the joint distribution are not discussed.** As described in Section 4.3, inverse triples are added to the training set to enable efficient head prediction. This doubles the training data and changes what the joint distribution p(S,R,D) covers (now including both (s,r,d) and (d,r⁻¹,s) as independent observations). The paper neither quantifies how this affects the learned distribution nor discusses the implied assumption that both directions are equally informative.

### Trivial
- "the the" typo on line 108 ("We fix the the batch size").

## Nice-to-Haves

- **Calibration experiment.** Adding a reliability diagram or expected calibration error against known true/false triples (e.g., from a dataset where negatives are known) would substantially strengthen the probabilistic semantics claim.
- **Complex query answering evaluation.** The paper repeatedly motivates global consistency for complex query answering but never evaluates on that task. Even a small experiment using the query decomposition framework of Arakelyan et al. (2021) would significantly strengthen the motivation.
- **Computational cost comparison.** A brief comparison of training/inference time against baselines would help readers assess practical trade-offs, since autoregressive generation is typically slower.
- **Hyperparameter details.** The main text mentions "randomly searched" learning rates and configurations (Section 5.1) without reporting ranges or final values, making reproduction harder than necessary.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"Probabilistic semantics claim is unsupported"** (harsh critic, Critical Issue #1) — The paper *does* clearly state that p(S,R,D) models the probability a triple is sampled from the observed KG (abstract: "probability that a link is sampled from the KG"). The critic conflates this with a claim about calibrated truth probabilities, which the paper does not explicitly make. This criticism as framed is a misreading; the calibration concern is retained above as a Minor weakness, not a structural fatal flaw.

2. **Section 4.1 decomposition trade-off tension** — The critic notes tension between the design logic and ablation results, but the paper presents its ablation (Table 4) transparently and discusses the findings. This is an observed phenomenon, not a weakness.

3. **Global ranking analysis on OGBLBioKG (Table 3) being insufficiently justified** — The paper provides a clear optimistic/pessimistic/realistic breakdown and discusses the results honestly. The averaging scheme is explained. This is thorough evaluation, not a flaw.

4. **Figure 2 qualitative interpretation being insufficient** — The paper's interpretation of Figure 2c ("more open to the possibility that some unknown triples are true") is supported by the visible density shift away from zero. This is a reasonable qualitative reading of empirical data, not a weakness.

5. **Local ranking gaps in Table 5** — The paper explicitly disclaims SOTA on local rankings ("we do not aim to achieve state-of-the-art performance on this task," line 156). The critic's concern is acknowledged by the authors themselves.

6. **Missing appendix/references/reproducibility details** — The parser strips these from all papers; they exist in the original submission. The instructions explicitly forbid marking these as weaknesses.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a genuinely novel perspective that the paper itself does not articulate.

## Suggestions

1. **Re-run the main baselines (ComplEx, NBF) at their standard ranks (e.g., 2000 for ComplEx) and report global MAP.** This is the single most impactful fix; if the large margins in Table 2 persist, the main claim is strongly supported. If they shrink substantially, the paper should discuss what the residual improvement says about the method's value.

2. **Add a small calibration experiment** — a reliability diagram or ECE on a dataset where negatives can be assumed (or use the optimistic/pessimistic setup already in the paper). Even a simple analysis on OGBLBioKG would greatly strengthen the probabilistic semantics discussion.

3. **Report results from at least 3 random seeds with mean and std** for the main global ranking metrics, so readers can assess the stability of the improvements.

4. **Discuss how adding inverse triples affects the interpretation of p(S,R,D)** — does the model learn one joint distribution over an extended triple set, or two coupled distributions? This would address a subtle but fair conceptual question.
