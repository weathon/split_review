Now I have a comprehensive picture from both rounds. Let me synthesize everything and write the final review.

---

## Summary

This paper proposes integrating n-gram induction heads (originally from language modeling) into transformer-based in-context reinforcement learning, specifically into the Algorithm Distillation (AD) framework. The n-gram attention layer explicitly computes n-gram matching patterns rather than relying on the transformer to learn them, which the authors argue reduces data requirements and hyperparameter sensitivity. Experiments on Dark Room, Key-to-Door, and Miniworld environments (both discrete and pixel-based) show the n-gram method consistently outperforming the AD baseline, particularly in low-data regimes.

## Strengths

- **Novel, well-motivated architectural contribution**: The idea of hardcoding n-gram induction heads into ICRL transformers is a sensible cross-domain transfer from language modeling. The motivation — that transformers struggle to discover these patterns on their own due to simplicity bias — is clearly articulated and grounded in prior work (Edelman et al., Akyürek et al.).

- **Consistent empirical gains across environments**: The n-gram method reliably outperforms the AD baseline in Dark Room (Figure 1), Key-to-Door (Figure 4), and both Miniworld variants (Figures 5–6), spanning discrete and pixel-based observation spaces. The improvements are large in low-data conditions (e.g., baseline plateaus at ~1.3 while n-gram reaches ~1.9 in Key-to-Door with only 100 training goals).

- **Useful ablation studies**: Section 4.4 demonstrates that the added n-gram hyperparameters (n-gram length, layer position) do not introduce fragile dependencies — varying these parameters across reasonable ranges yields similar performance (Tables 1a, 1b). Section 4.5 shows that a deliberately broken n-gram mask (permuted) reduces performance to baseline levels, providing evidence that the n-gram mechanism itself, not extra parameters, drives the gains.

- **Sensible evaluation protocol**: The use of Expected Maximum Performance (EMP) over random hyperparameter searches is appropriate for studying hyperparameter sensitivity and avoids cherry-picking.

- **Clear, accessible writing**: The paper is well-structured and the method description (Section 2) is easy to follow, including the handling of discrete vs. image observations.

## Weaknesses

### Fatal

None.

### Major

- **The 27× data efficiency claim relies on an indirect comparison and lacks direct experimental support.** The paper states that the n-gram method requires "27× less data" than the original AD, computed by comparing the authors' setup (100 goals, 500–1000 histories in Key-to-Door) against Laskin et al.'s original numbers (2048 goals, 2048 histories). The justification is deferred to Appendix B (not available in this review copy). No direct scaling experiment is performed where AD and the n-gram method are both trained on progressively smaller datasets to determine the exact data regime where AD fails while the n-gram method succeeds. The paper's own Figure 1 does show a roughly 8× improvement in Dark Room (n-gram at 128 goals ≈ baseline at 1024 goals), which is a cleaner self-contained comparison, but the headline 27× claim is not supported by any within-paper experiment. This weakens the paper's strongest quantitative assertion.

- **No error bars or confidence intervals on any EMP curves (Figures 2, 4, 5, 6).** The EMP metric averages over hyperparameter assignments, but there is inherent variability from the random ordering of those assignments and from different random seeds. Without bootstrapped confidence bands or seed-based error bars, the reader cannot assess whether the observed gaps between methods are statistically reliable. This is particularly important given that some curves show non-monotonic behavior (e.g., Figure 1 baseline drops from 1.8 to 1.7 going from 1024 to 2048 goals, suggesting substantial noise). For a paper whose central claims are about comparative performance improvements, this omission is significant.

### Minor

- **The hyperparameter search fairness concern has partial but incomplete addressal.** The paper's main EMP experiments random-search over core transformer hyperparameters, but it is not stated whether the n-gram-specific parameters (n-gram length, layer position) are included in that search or fixed a priori. Section 4.4 shows these parameters have low impact individually, which mitigates the concern, but the paper does not demonstrate a joint random search where n-gram parameters are sampled alongside core parameters. If n-gram parameters were pre-selected, the n-gram model had a modest head start.

- **The AD baseline is not validated against the original published results.** The paper uses a re-implementation of AD. While the baseline does reach reasonable performance in data-rich Dark Room conditions (~1.8 at 1024 goals, Figure 1), the paper never demonstrates that this re-implementation can match Laskin et al.'s reported performance when given similar data. This leaves a small residual doubt about whether baseline underperformance in low-data regimes reflects a genuine limitation of AD or a suboptimal re-implementation.

- **The VQ-based n-gram matching for images lacks fidelity analysis.** Section 2.3 describes using VQ to map images to 4×4 index matrices with exact-match n-gram comparison. The paper does not evaluate how often semantically identical states map to different VQ indices (causing false negatives) or how often distinct states collide to the same indices. Section 4.5's permuted-mask experiment shows the matching mechanism matters, but does not quantify its accuracy.

- **Environments are limited in scope.** The paper evaluates on two grid-worlds (Dark Room, Key-to-Door) and their Miniworld 3D analogues. While reasonable for a proof-of-concept, the paper's conclusions would be stronger with experiments on at least one more diverse or challenging environment. The authors acknowledge this limitation in the conclusion.

- **Architectural and hyperparameter details are in the stripped appendices.** The main text defers model architecture (layers, hidden size, heads, parameter counts), hyperparameter search spaces, and the 27× computation to Appendix B, C, and D, which are not available in this review copy. This makes independent verification of key experimental claims impossible from the main text alone.

### Trivial

- The abstract claims the method "matches, and in some cases surpasses, the performance of AD" — this is somewhat sweeping given the narrow set of environments.

- The computational overhead of the n-gram matching step (both at training and inference) is not discussed.

## Nice-to-Haves

- **Direct data-scaling experiment**: Train both AD and the n-gram method on the same suite of progressively smaller datasets (varying number of tasks and histories) and determine the data regime where AD fails but n-gram still succeeds. This would provide a clean, self-contained quantification of data efficiency without relying on external numbers from Laskin et al.

- **Joint hyperparameter search**: Include n-gram-specific parameters (length, position) in the main random search to fully rule out fairness concerns.

- **VQ fidelity evaluation**: Measure within-state vs. across-state code consistency to assess whether the VQ-based matching captures semantically meaningful n-grams.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The baseline AD implementation is not validated to match published performance" (Harsh Critic, Critical Issue 3)**: The paper's baseline does work — it reaches ~1.8 return in Dark Room at 1024 goals (Figure 1), which is reasonable performance. The failure in Key-to-Door at 100 goals is the actual finding of interest. I've kept a softened version as a Minor weakness rather than the original framing which implied the baseline might be fundamentally broken.

- **"The paper lacks essential architectural details"**: These are in the appendices (Appendix C), which were stripped by the parser. This is not an author error.

- **"No comparison to more recent ICRL approaches"**: The paper's scope is to improve AD with n-gram heads. Comparing to every recent ICRL method is scope creep. The AD baseline is the appropriate comparison.

- **"The hyperparameter search spaces are not described anywhere in the main text"**: They are in Appendix C, which was stripped.

- **Harsh Critic's framing of the 27× claim as "unsubstantiated" and "misleading"**: I've kept a softened version as Major — the issue is real (indirect comparison) but the paper does show clear data-efficiency gains in its own experiments (Figure 1, Figure 4), so the core direction is supported even if the specific multiplier is not rigorously tested.

- **Harsh Critic's suggestion that "the authors' own baseline fails at 100 tasks, but it is unclear whether that baseline was itself trained to saturation"**: The paper uses EMP over random hyperparameter search, which is designed to measure what's achievable within a budget. The baseline curve saturates in Figure 4 — more hyperparameter search wouldn't help. This concern is addressed by the experimental protocol.

- **Strength Finder's claim of "27× reduction" as a core strength**: This is contradicted by the Major weakness above. I've kept the data efficiency finding as a strength but without the 27× multiplier.

- **"The abstract's statement is too sweeping given the narrow set of environments"**: Moved to Trivial — this is a phrasing issue, not a substantive problem. The abstract does say "in both grid-world and pixel-based environments," which accurately reflects the scope.

## Novel Insights

The paper's most valuable insight is that n-gram induction heads — originally studied in language modeling — transfer naturally to the ICRL setting because RL trajectories contain recurring patterns (states, state-action pairs) that n-gram matching can exploit. The finding that this transfer works without modification for discrete states and with only a simple VQ wrapper for pixel observations suggests that the n-gram inductive bias is broadly useful for sequential decision-making, not just language. The ablation showing that deliberately breaking the n-gram mechanism (permuted mask) drops performance to baseline levels (Table 1c) provides clean evidence that the mechanism itself, not added parameters, drives the improvement — a crisp experimental design worth emulating.

## Suggestions

- Replace the indirect 27× comparison with a direct scaling experiment. Even a modest scaling study (e.g., train both methods on 25, 50, 100, 200, 500 goals in Key-to-Door) would provide a far stronger data-efficiency claim than the current cross-paper comparison.

- Add bootstrapped confidence bands to all EMP curves. This is standard practice and would substantially strengthen the reliability of the results.

- Clarify in the main text which hyperparameters are included in the random search for each method, and ideally run one joint search that includes n-gram-specific parameters.

- Move key architectural parameters (layers, hidden size, attention heads) and the hyperparameter search space definition into the main paper rather than only in appendices, for self-contained readability.

## Score and Decision

**Anchor comparison summary:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| 5iWim8KqBR | 5.50 | R1-topic-mid | Most similar: AD + DarkRoom/Door, Reject. Our paper has more novel contribution (n-gram heads vs. evaluating existing architectures) but shares narrow-benchmark concern. Comparable. |
| p9OsTj0nMP | 7.00 | R1-topic-mid | XLand-100B dataset, Accept. Much larger-scale contribution (50K GPU hrs). Our paper is clearly below this. |
| b5MCteb3w7 | 4.75 | R2 | ICRL benchmark paper, Reject. Our paper has clearer contribution and better empirical grounding. Our paper is better. |
| 0spR7wDwBh | 6.00 | R1-weakness / R2 | Grid-world agent with inductive biases, Reject. Both introduce inductive biases for data efficiency. Our paper has broader scope (pixel-based), better ICRL framing, but similar contribution level. Our paper is comparable. |
| J5s6EG6ual | 3.00 | R1-topic-low | Self-attention in DRL, Reject. Flawed evaluation, arbitrary attention choices. Our paper is substantially better. |
| WM5G2NWSYC | 2.00 | R1-weakness | Weak empirical validation. Our paper does not share these failures. |
| E2RyjrBMVZ | 4.17 | R1-weakness | Variance in benchmarks. Our paper shares the missing-error-bars issue. |
| aN4Jf6Cx69 | 4.50 | R2 | Induction head mechanistic analysis, Accept (controversial). Very different paper type — theoretical vs. applied. Not directly comparable. |

**Round-1 bracket**: 4.5–6.5. The paper clearly outperforms the low-band anchors (J5s6EG6ual at 3.00, WM5G2NWSYC at 2.00) which had fundamental evaluation flaws. It sits below p9OsTj0nMP (7.00), the large-scale dataset paper with clear community value. Within the bracket, it is most comparable to 5iWim8KqBR (5.50) and 0spR7wDwBh (6.00).

**What did the low-band anchors fail at?** They had fundamental experimental flaws: J5s6EG6ual used an arbitrarily shallow architecture and compared attention variants nobody uses; WM5G2NWSYC had extremely weak empirical validation. The paper under review does not share these failure modes — its experiments are systematic, its baselines are relevant, and its core finding (n-gram heads help ICRL) is supported across environments.

**Round-2 narrowing**: The round-2 anchors confirmed the bracket. The paper is comparable to 5iWim8KqBR (5.50) but has a somewhat more novel contribution and broader scope (pixel-based environments). However, the missing error bars and the indirect 27× comparison drag it down relative to the 6.00 anchor (0spR7wDwBh).

**Final placement**: The paper has a genuinely novel and well-motivated idea, consistent empirical gains, and a clean evaluation protocol. But the headline quantitative claim (27×) is not directly substantiated, all EMP curves lack uncertainty quantification, and the hyperparameter search fairness concern is only partially addressed. These are evidential gaps that prevent the paper from reaching the acceptance threshold, but they are addressable with additional experiments. The paper's contribution is real but the evidence is not yet tight enough.

**Score: 5.0**

The paper makes a solid contribution that would benefit from a round of strengthening experiments and presentation cleanup, but in its current form the evidential support for its strongest claims is insufficient for acceptance at ICLR.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>