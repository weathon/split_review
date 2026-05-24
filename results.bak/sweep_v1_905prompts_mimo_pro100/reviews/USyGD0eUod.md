Now I have enough calibration data. Let me synthesize the review.

**Round 1 bracket**: The paper falls between the weak anchors (~3.5, rejected SAE papers with clarity issues) and the strong anchors (~8+, major contributions like Gao et al.'s scaling paper). My initial bracket is 6.0–7.5.

**Round 2 narrowing**: 
- "Towards Best Practices of Activation Patching" (6.67, accepted): similar methodology evaluation paper for MI. Our paper is more focused and has stronger experimental design, so it should be above this.
- "A is for Absorption" (7.5, rejected despite high scores): SAE failure mode analysis, similar scope but more narrow. Our paper is broader but slightly less deep mechanistically.
- "Towards Principled Evaluations of SAEs" (7.0, accepted): very similar topic — SAE evaluation methodology. Our paper covers broader model scale and proposes actionable diagnostics.

I position this paper at **7.0** — on par with the "Principled Evaluations" paper and slightly above the "Activation Patching Best Practices" paper.

---

## Summary

This paper demonstrates that commonly used SAE evaluation metrics — particularly aggregate auto-interpretability AUROC scores — fail to reliably distinguish SAEs trained on fully trained Pythia transformers from those trained on randomly initialized ones across model sizes from 70M to 6.9B parameters. The paper introduces token distribution entropy as a supplementary diagnostic and presents toy model analyses suggesting that random networks may preserve or amplify superposition in input data.

## Strengths

- **Rigorous multi-variant experimental design with a proper negative control**: The paper compares five model variants (Trained, Re-randomized incl./excl. embeddings, Step-0, and Control) across multiple Pythia model sizes. The Control — where token embeddings are replaced with i.i.d. Gaussian noise at inference time — consistently falls to chance-level AUROC (0.50), cleanly validating the experimental setup while trained and randomized variants overlap at 0.79–0.88 for Pythia-6.9B (Figures 1–2).

- **Systematic scaling analysis across model sizes**: Figure 2 presents results across Pythia-70M through Pythia-6.9B and multiple layers, revealing that the gap between trained and randomized variants narrows as model size increases — a concrete finding that smaller-model results (Bricken et al., 2023) do not hold at scale.

- **Token distribution entropy as an actionable diagnostic**: The entropy metric (last row of Figure 2) reveals that trained-model features become more abstract (higher entropy) in later layers while randomized-variant features remain token-specific (lower entropy), despite similar AUROC scores. This is a concrete, interpretable measure that goes beyond identifying the problem.

- **Honest limitation section and nuanced internal framing**: The paper explicitly acknowledges ambiguity: "one could argue that a randomly initialized network still performs a basic form of computation" (Section 1) and "we leave the question of which predominates... to future work" (Section 4). The conclusion states "This result does not imply that SAEs trained on real models fail to learn meaningful computational features." This internal honesty is commendable.

- **Robustness across SAE hyperparameters**: The paper confirms results hold across expansion factors 16–128 and sparsities 16–32 (Figure 18, Section 3), and shows consistency when scaling training data from 100M to 1B tokens (Appendix C).

## Weaknesses

### Fatal

None.

### Major

- **The title and abstract overstate the finding relative to the nuanced evidence**: The title asserts metrics "do not distinguish" trained and random transformers, and the abstract frames this as a failure of metrics. However, Figure 2 shows that token distribution entropy *does* distinguish them, and the paper internally acknowledges that random transformers perform "a basic form of computation." A more precise framing would be that *aggregate auto-interpretability AUROC* is insufficient — not that the metrics categorically fail. This matters because a reader could conclude SAEs are fundamentally broken, when the more accurate conclusion is that a specific class of aggregate metrics needs supplementing. The paper's own conclusion and limitations sections are more nuanced than the headline claims, creating a mismatch.

- **The mechanistic explanation is left unresolved, limiting actionability**: Section 4 presents two hypotheses — random networks preserve superposition, or amplify it — and provides toy model evidence for both. The GloVe experiment (Section 4.3) is directly relevant but the paper explicitly defers "the question of which predominates" to future work. Without understanding *why* random models score similarly to trained ones, it is difficult to assess whether this is a fundamental limitation of current metrics or a fixable artifact. The Pareto frontier analysis (Figure 5b) shows the gap between GloVe embeddings and Gaussian controls is small to begin with, making interpretation difficult.

### Minor

- **Fuzzing/simulation correlation not verified for random models**: The paper cites Paulo et al. (2024) to justify using fuzzing AUROC throughout ("this measure has been demonstrated to correlate with simulation scoring"), but never checks whether this correlation holds in the random-model regime where features are simpler and more token-specific. If the correlation breaks down for simple features, the choice of fuzzing as the primary metric could be confounding the results.

- **Token distribution entropy analysis is underdeveloped as a contribution**: The entropy metric is identified as the paper's most actionable finding — it successfully separates trained from random models where AUROC fails — but is treated as a minor observation ("preliminary" per the conclusion). Formalizing it as a metric with a concrete threshold, statistical test, or workflow for practitioners would substantially strengthen the paper from a critique into a critique with a partial solution.

- **CE loss score plotted alongside other metrics without clear visual distinction**: The CE loss score (row 5 of Figure 2) is shown only for the trained variant, which the paper notes verbally, but the figure layout presents it alongside metrics computed for all variants, potentially misleading quick readers.

### Trivial

None.

## Nice-to-Haves

- Develop the entropy metric into a concrete diagnostic workflow: e.g., train SAE → compare to randomized baseline on AUROC and entropy → flag if the AUROC gap is below threshold.
- Test whether fuzzing AUROC correlation with simulation scoring holds for random-model features.
- Include even a small number of illustrative qualitative examples in the main text (referenced in Appendix J/L) showing trained-model latents capture different concepts than random-model latents, since the paper's own argument is that aggregate metrics miss qualitative differences.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **SAE hyperparameters not discussed** — The harsh critic claims the paper doesn't discuss whether expansion factor 64 or sparsity 32 contributes to the result. This is factually wrong: the paper explicitly tests expansion factors 16–128 and sparsities 16–32 (Section 3, Figure 18) and reports the results are robust.

- **"The linear algebra argument is trivial"** — While true that the linear case is straightforward, the paper acknowledges this is a "simplified model" (Section 4.1) and proceeds to nonlinear MLP experiments and GloVe embedding analysis. This is appropriate scaffolding, not a weakness.

- **"The control is not the right null model"** — The harsh critic argues that high AUROC for random models may be "legitimate rather than spurious." This is precisely the nuanced interpretation the paper itself offers in Section 1 and Section 4 — the paper's point is that even if legitimate, these features don't reflect *learned computation*, which is what the community needs to evaluate. The paper's recommendation (use randomized baselines) is appropriate regardless of interpretation.

## Novel Insights

The most novel insight from this review synthesis is the observation that the paper's most actionable contribution — token distribution entropy — is simultaneously its most underdeveloped. The paper identifies a metric that *does* solve the very problem it reports (aggregate metrics failing to distinguish trained from random), yet treats this finding as supplementary rather than central. Reframing the paper around this positive finding alongside the negative result would make the contribution both more impactful and more balanced.

## Suggestions

1. Reframe the title/abstract to distinguish between "aggregate AUROC fails" and "metrics categorically fail," since entropy does succeed.
2. Formalize the token distribution entropy metric with a threshold or statistical test and present it as a primary contribution, not an afterthought.
3. Verify that fuzzing/simulation scoring correlation holds for random-model features, or caveat the fuzzing-only evaluation more prominently.

## Score and Decision

**Calibration anchors retrieved:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Decomposing The Dark Matter of SAEs | 3.50 | 1 | Weaker — rejected, severe clarity issues, single model |
| Measuring Feature Sparsity in Language Models | 3.50 | 1 | Weaker — rejected, less systematic |
| Sparse Autoencoders Find Highly Interpretable Features | 4.80 | 1 | Weaker — foundational but narrower scope |
| Benchmarking XAI Explanations | 5.50 | 2 | Weaker — different domain, less impactful finding |
| Towards Best Practices of Activation Patching | 6.67 | 2 | Similar — methodology paper for MI, less focused |
| Unpacking SDXL Turbo with SAEs | 4.40 | 1 | Weaker — domain-specific application |
| Towards Principled Evaluations of SAEs | 7.00 | 1 | Similar — SAE evaluation framework, narrower model scope |
| A is for Absorption (SAE feature splitting) | 7.50 | 2 | Similar — identifies SAE failure mode, narrower but deeper |
| Scaling and Evaluating Sparse Autoencoders | 8.20 | 1 | Stronger — major architectural + scaling contribution |
| Sparse Feature Circuits | 8.00 | 1 | Stronger — novel method with broad applications |

**Round 1 bracket**: 6.0–7.5 (above activation patching best practices at 6.67, below scaling SAEs at 8.2).

**Round 2 narrowing**: The paper is comparable to "Towards Principled Evaluations of SAEs" (7.0) — both are SAE evaluation methodology papers. Our paper covers broader model scale and provides a cleaner negative result, but has a less developed constructive contribution. It is slightly below "A is for Absorption" (7.5) in technical depth. Final score: **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>