## Summary
The paper introduces Distributed Neural Architectures (DNA), a framework in which tokens (or image patches) are routed through an arbitrary sequence of computational modules, with both routing and module parameters learned end-to-end. DNA is presented as a strict generalization of existing sparse methods (MoE, MoD, weight-sharing, early exit). The authors train DNA models at ViT-Small and GPT-2-Medium scales in vision and language domains, demonstrate competitive performance with dense baselines, and analyze emergent connectivity patterns including a power-law distribution of token paths, module specialization, and input-dependent compute allocation.

---

## Strengths

- **Clean conceptual unification.** DNA is a well-formulated superset of MoE, MoD, parameter sharing, and early exit. The update rule (Eq. 1) is carefully derived to avoid double-counting residual connections and is backed by prior signal-propagation work. The framework motivates natural future directions for co-designed hardware.

- **Competitive empirical results in two domains.** Top-2 DNA (433 M active params) achieves 2.674 validation loss vs. 2.720 for GPT-2-Medium (406 M) while matching or exceeding it on five of seven zero-shot benchmarks (Table 3). On ImageNet, top-1 DNA is within 0.7 pp of ViT-Small. Results are obtained with reasonable hyperparameter sweeps and the paper honestly quantifies the gap rather than cherry-picking.

- **Power-law path distribution.** The empirical finding that path frequencies follow a power-law (exponent ≈ −1.2 for language, −1 for vision) in trained models is novel and provocative. The comparison with randomly initialized models (exponent −1) sharpens the finding, showing that training shifts but preserves the functional form.

- **Interpretable emergent specialization.** The visualization in Fig. 3 and the deep-dream routing visualization in Fig. 4 clearly show that low-rank (frequent) paths aggregate semantically general features while high-rank (rare) paths capture specific visual or linguistic concepts. The finding that object boundaries attract the most compute (Fig. 5) is independently interpretable and connects to prior work on critical patches.

- **Honest framing.** The paper explicitly disclaims SOTA competition and frames the goal as feasibility and emergent structure analysis — a framing that is appropriate and enables a more thorough mechanistic investigation than a pure performance paper would allow.

---

## Weaknesses

### Fatal
None.

### Major

1. **No FLOPs or latency comparison.** Every efficiency claim is made in terms of "active parameters" or "skipped modules," but no wall-clock time, hardware FLOPs, or inference latency is reported. Router overhead (a softmax + top-k per step per token, repeated 11–24 times) is non-negligible and can dwarf module savings at small model sizes. Without this comparison the efficiency claims—a primary motivation of the work—are unsubstantiated.

2. **Compute-skipping in language is significantly worse.** The 30%-skip DNA language model degrades substantially: LAMBADA accuracy falls from 33.8 to 23.8, Wikitext perplexity rises from 33.7 to 52.6 (Table 3). While the paper compares against a 30%-shallower GPT-2 (also worse), the magnitude of degradation for the skip model is large enough to challenge the claim that "compute efficiency can be learnt from data" with "minor effects on performance." The vision case fares better, but the language result needs more analysis.

3. **Parameter comparison is not iso-FLOPs.** The DNA "top-2" language model has 433 M active parameters vs. 406 M for GPT-2-Medium, while the total parameter count is 603 M vs. 406 M. The slight downstream wins (e.g., +1.3 pp on HellaSwag) could plausibly be explained by access to more parameters rather than superior architecture. An iso-FLOPs and iso-parameter ablation is needed to isolate the architectural contribution.

4. **Emergent parameter sharing in language is self-admittedly random.** Section 4.3 concludes "module reuse is most likely random in the language case." This contradicts the parameter-sharing story presented for vision and weakens the generality of the efficiency narrative. The authors suggest discouraging module reuse as future work, but this implies the current language DNA design may be sub-optimal in a systematic way.

### Minor

1. The attention within DNA tokens is described as sparse because only co-routed tokens attend to each other. This has important implications for information flow across the sequence, yet the paper does not analyze whether critical long-range dependencies are broken, even qualitatively.

2. The deep-dream reconstructions (Fig. 4) produce images that the model does not classify correctly (e.g., "spotlight" instead of "bell pepper"). While the paper acknowledges this, no quantitative measure of routing alignment is provided, making it hard to assess how much the routing captures semantics vs. texture statistics.

3. The maximum processing depth $s_{\max}$ is a hyperparameter that caps compute per token; no sensitivity analysis is reported, making it unclear how much the results depend on this choice.

### Trivial
The caption for Fig. 2 top-right refers to "effective number of compute nodes" but the axis label says "effective task" in Fig. 6—a minor inconsistency across figures.

---

## Nice-to-Haves

- Reporting GPU-hours or FLOPs per training run and inference latency benchmarks would make the efficiency claims concrete and actionable.
- An ablation fixing total FLOPs (not just active parameters) between DNA and dense baselines would clarify how much of the gain is architectural.
- A controlled experiment discouraging parameter sharing in the language model to test whether it improves performance would directly address the observation in Section 4.3.
- Scaling the analysis to a larger model (e.g., 1B parameters) would help assess whether the power-law and specialization findings are scale-invariant.

---

## Novel Insights

Beyond the paper's own framing, the observation that trained and randomly initialized DNA models both exhibit power-law path distributions (with similar exponents) is genuinely surprising. It suggests the power-law structure is a property of the combinatorial space of routing decisions rather than an emergent consequence of gradient-driven specialization. The shift in exponent from −1 (random) to −1.2 (trained, language) or retention at −1 (trained, vision) then becomes a measurable signature of how much training concentrates routing mass onto fewer paths. This raises the interesting hypothesis that the exponent of the path distribution could serve as a measure of routing collapse or routing diversity—distinct from existing load-balancing metrics—and could be used as a diagnostic or regularization signal in future MoE/DNA training.

---

## Suggestions

- Add a latency or FLOPs table (even approximate, e.g., FLOPs per token for DNA vs. dense, accounting for routing) so the efficiency argument can stand on its own.
- Report a DNA ablation with the same total parameter budget as the dense baseline (not just active parameters) to give a cleaner architectural comparison.
- Quantify routing stability: report the fraction of tokens whose routing decision changes across different runs of the same input (to assess stochasticity from top-k sampling).
- For the language efficiency model, try separating "skip all modules" from "attend globally at the identity step" to distinguish compute savings from information-flow changes.

---

## Score and Decision

The paper introduces a genuinely interesting and well-formulated generalization of conditional computing, demonstrates training feasibility in two domains, and uncovers interpretable emergent behaviors (power-law path distributions, semantic specialization, compute-content correlation). The main limitations are the absence of FLOPs/latency analysis, the substantial degradation in the compute-efficient language variant, and the lack of iso-FLOPs comparisons. These are significant gaps but do not invalidate the core contribution, which is conceptual and analytical rather than claiming a new efficiency SOTA.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>