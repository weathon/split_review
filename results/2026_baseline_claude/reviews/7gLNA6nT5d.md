## Summary

This paper integrates n-gram induction heads—previously studied in the in-context language learning literature—into transformer-based in-context reinforcement learning (ICRL), using Algorithm Distillation (AD) as the baseline. The core claim is that hardcoding n-gram attention patterns, rather than waiting for them to emerge during training, improves data efficiency (up to 27× less training data) and reduces hyperparameter sensitivity in ICRL models. The approach is further extended to pixel-based observations via a VQ bottleneck for state discretization, and is evaluated on Dark Room, Key-to-Door, and two Miniworld variants.

---

## Strengths

- **Well-motivated inductive bias.** The connection between n-gram induction heads and the simplicity bias of transformers (Edelman et al., Akyürek et al.) provides a principled hypothesis for why n-gram layers help in ICRL. Hardcoding what would otherwise require substantial data to learn organically is a logically coherent motivation, and the paper explicitly links this to the known instabilities of ICRL (transient in-context ability, hyperparameter sensitivity).

- **Principled evaluation protocol.** Using Expected Maximum Performance (EMP) over random hyperparameter search, with a fixed computational budget across all experiments, is a rigorous and reproducible way to simultaneously assess peak performance and hyperparameter sensitivity. This avoids the common pitfall of reporting cherry-picked best runs.

- **Consistent results across environments.** Improvements over the AD baseline are shown consistently across four environments (Dark Room, Key-to-Door, Miniworld-Dark Room, Miniworld-Key-to-Door), both for data efficiency and hyperparameter sensitivity, lending credibility to the central claims.

- **Extension to pixel-based observations via VQ.** Adapting n-gram matching to continuous/image observations through vector quantization is a practically meaningful contribution. The ablation in Table 1(c)—showing that a permuted (broken) n-gram mask degrades gracefully to baseline performance—is a useful safety check that the VQ approach is not introducing harmful noise.

- **Ablation study on n-gram hyperparameters.** Tables 1(a) and 1(b) demonstrate that the new hyperparameters introduced (n-gram length and layer position) show no significant sensitivity, which supports the paper's claim that the approach does not meaningfully expand the hyperparameter search space.

---

## Weaknesses

### Fatal
None.

### Major

1. **Narrow experimental scope limits generalizability.** All results are on small grid-world or toy 3D environments (Dark Room 9×9, Key-to-Door). These are the standard benchmarks for AD, but they are substantially simpler than environments where ICRL methods are now deployed (e.g., XLand-MiniGrid, Meta-World), which the authors themselves acknowledge only as future work. It is unclear whether the proposed benefits persist in environments with larger state spaces, richer dynamics, or longer episodes where n-gram patterns may not recur with the same regularity.

2. **The 27× data reduction claim is environment-specific and potentially misleading.** The comparison is made between the authors' Key-to-Door setup (100 training goals, 500–1000 learning histories) and the original AD paper's setting (2048 goals, 2048 learning histories). However, the two setups differ in environment, task diversity, data collection protocol, and the treatment of "tasks" vs. "learning histories" (the authors explicitly distinguish these differently from Laskin et al.). The claimed multiplier reflects a combination of these differences, not solely the effect of n-gram layers, making it difficult to isolate the method's contribution. A cleaner ablation—fixing all data parameters and only toggling the n-gram layer—within the same setup would more directly support the claim.

3. **Limited comparison to the broader ICRL landscape.** The only baseline throughout is vanilla AD. More recent ICRL approaches (e.g., Retrieval-Augmented Decision Transformer, noise-curriculum data augmentation methods cited in the related work) are not compared against, leaving open whether n-gram layers are competitive with alternative data-efficient strategies.

### Minor

1. **N-gram length ablation is inconclusive about mechanism.** Table 1(a) shows no significant difference between 1-gram, 2-gram, and 3-gram (all within overlapping confidence intervals). If a simple 1-gram (matching only the most recent token) is as effective as higher-order n-grams, this raises questions about the mechanism: does simply checking whether a state has been recently visited drive the benefit, rather than any richer n-gram structure?

2. **VQ pretraining costs are not quantified.** The ResNet + VQ bottleneck pretraining for Miniworld adds computational overhead that is not reported (training time, number of training steps, dataset size used for VQ pretraining). This omits a meaningful component of the overall resource budget.

3. **Figure 6 uses different training goal counts for n-gram and baseline (50 vs. 60 goals) in Miniworld-Dark**, which slightly conflates data efficiency with hyperparameter sensitivity. The caption justification is present but the setup adds noise to the sensitivity comparison.

### Trivial

- None worth noting.

---

## Nice-to-Haves

- A controlled experiment isolating the n-gram layer benefit while holding all data parameters identical (same number of goals, histories, and environment) would strengthen the 27× claim considerably.
- Reporting actual wall-clock or FLOPs comparisons (not just hyperparameter assignment counts) would make the computational efficiency story more complete.
- Even a preliminary result on a larger-scale environment (e.g., XLand-MiniGrid in a low-task regime) would greatly increase confidence in the generality of the findings.

---

## Novel Insights

The paper's most genuinely novel observation is that hardcoding n-gram induction heads—originally identified as an emergent structure in language transformers—can substitute for the slow and data-hungry emergence of this structure in ICRL settings. This reframes the data efficiency problem from a data collection challenge to an architectural one: by injecting the right inductive bias at initialization, the model bypasses an expensive self-organization phase. The VQ-based extension to visual observations is a pragmatic bridge between a fundamentally discrete mechanism and a continuous perception domain, and the finding that a broken n-gram mask gracefully degrades to baseline (rather than harming performance) is a useful property for practical deployment.

---

## Suggestions

- Clarify the 27× comparison by providing a controlled ablation table in the main text that holds environment and data structure fixed, toggling only the n-gram layer.
- Report VQ pretraining compute cost alongside the main experiment compute, so readers can assess total overhead.
- Consider including at least one larger or more diverse environment (e.g., a small XLand-MiniGrid split) to bound the scope of the claim.
- Investigate whether the 1-gram result being competitive with higher-order n-grams reveals something specific about the RL trajectory structure (e.g., revisitation patterns), as this could be an interesting mechanistic finding in its own right.

---

## Score and Decision

The paper addresses a real bottleneck in ICRL (data demands and hyperparameter instability), provides a principled and logically grounded solution, and demonstrates consistent empirical improvements across several environments. The evaluation protocol is notably rigorous. However, the method is a fairly direct application of an existing technique (Akyürek et al.'s n-gram attention) to a new domain, the experimental scale is limited to simple grid-world tasks, and the headline 27× claim involves a comparison that conflates multiple confounds. These factors make the contribution solid but incremental.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>