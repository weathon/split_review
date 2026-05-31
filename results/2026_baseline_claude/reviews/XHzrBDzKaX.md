## Summary

The paper introduces **VisFACTOR**, a benchmark that adapts 20 vision-centric subtests from the Factor-Referenced Cognitive Test (FRCT) — a well-established psychometric battery — into an automated multimodal evaluation framework for MLLMs. Spanning four cognitive domains (Visualization/Spatial Processing, Perceptual/Closure, Memory, Reasoning), the benchmark covers 10 distinct psychometric factors. The authors evaluate 23 frontier models, find a maximum accuracy of 30.17% (GPT-5.1) against a human baseline of 78.8%, and implement parametric generation for 12 subtests to produce difficulty-controlled items that resist benchmark saturation.

---

## Strengths

- **Psychometric grounding is principled and novel.** Anchoring MLLM evaluation to the FRCT battery — which is built on factor analysis of latent cognitive abilities rather than post-hoc task design — is genuinely new in this community. This provides scientific legitimacy: each subtest isolates a specific, theoretically motivated visual competency, making failures interpretable rather than merely observed.

- **Comprehensive multi-model evaluation with a meaningful human baseline.** Testing 23 models from all major families (GPT, Gemini, Claude, Qwen, Llama, Seed) under a unified zero-shot protocol, alongside 31 undergraduates using the identical digital protocol, yields a robust performance gap (30.17% vs. 78.8%). The within-family findings are particularly striking — Qwen-2.5-32B outperforms Qwen-2.5-72B, Claude-3.7 outperforms Claude-4 — indicating that model recency/scale does not track foundational visual cognition, which is a novel and practically significant observation.

- **Rigorous reduction of chance-level accuracy.** The authors carefully engineer five distinct item-modification strategies (decomposed multiple-choice, grouped-consistency, symmetry variants, specialized rewrites) that reduce average random accuracy from 22.47% to 2.89%, with no single test exceeding 6.25%. This distinguishes VisFACTOR from benchmarks that effectively allow 25–50% chance baselines.

- **Insightful failure analysis distinguishing concept recognition from visual perception.** The MA1 experiment — swapping semantically rich images for abstract CF2 line patterns while keeping everything else fixed — is an elegant probe. The sharp accuracy drop (e.g., Qwen-VL-Max: 97.62% → 2.38% at 40 pairs) provides direct causal evidence that models rely on concept-level recognition rather than raw visual memory. The CF3 text-vs.-image ablation (100% with text coordinates vs. ≤18.8% from images) similarly isolates the visual perception bottleneck cleanly.

- **Parametric generation for benchmark longevity.** The difficulty-controlled generator for 12 subtests (e.g., varying fold count for VZ2, pair count for MA1, noise level for CS1-CS3) demonstrates that the benchmark can be refreshed as models improve and provides direct training signal for future RL-based approaches.

---

## Weaknesses

### Fatal
None.

### Major

- **Data contamination is unaddressed.** The FRCT battery has been published since 1976 and its specific test items are likely present in pretraining corpora. The paper does not include any contamination analysis (e.g., canary-string probing, checking whether models recall specific item wordings, or comparing performance on FRCT original vs. generated items across models). This is a significant omission for a benchmark paper because it undermines the claim that low performance reflects genuine visual deficiencies rather than absence of memorized test keys. The fact that the best model scores only 30.17% is circumstantially reassuring but not a substitute for an explicit analysis.

- **Generated-subset evaluation is confined to a single model.** Table 3 evaluates only GPT-4.1 across Easy/Normal/Hard levels. Extending this to the full set of 23 models (or at minimum a representative subset) would substantially strengthen the conclusion that difficulty modulation is effective and general. As it stands, the generator — which is positioned as a key contribution — is validated only for one model family.

- **Grouped-consistency scoring creates incommensurable scales.** Requiring all constituent items in a group to be simultaneously correct (§2.3) conflates subtest accuracy with product probability. A model with 60% per-item accuracy on CF2 (Hidden Patterns) will score only ~(0.6)^5 ≈ 7.8% on a group, while a model scoring 90% per-item scores ~59% on the same group — a nonlinear mapping that is very different from the arithmetic average used for other subtests. The paper does not discuss this scoring asymmetry, and it complicates cross-subtest comparisons.

### Minor

- **Human evaluation population is narrow.** The 31 participants are all university students; the FRCT was normed on a broader adult sample. Some subtests (RL2 — Diagramming Relationships) show humans at 51.7%, barely above chance on a task MLLMs apparently handle better, which the paper attributes to MLLM language strength but does not investigate further. A brief error analysis of human failures on RL2 would clarify whether the task is testing language comprehension rather than vision in this digital format.

- **Instruction adaptation circularity.** Using GPT-4o and Gemini-2.5-Flash to summarize FRCT instructions (§2.2) introduces a mild circular dependency — those two model families may be implicitly advantaged by instructions partially authored by their own output. The human reconciliation step partially mitigates this but the design choice is not discussed.

### Trivial

- Table 1 column headers appear garbled by the PDF parser (duplicate RL2/P3 columns, misaligned entries) — likely a parser artifact.

---

## Nice-to-Haves

- Extend Table 3 (generated-subset evaluation) to at least five or six models spanning different model families, so that the difficulty-modulation claims generalize beyond GPT-4.1.
- Include a contamination probe: ask models to reproduce a FRCT item verbatim, or compare verbatim-FRCT vs. parametrically generated performance across all 23 models.
- Discuss the scoring incommensurability from product-accuracy in grouped tasks explicitly, and consider reporting per-item accuracy alongside group accuracy as a diagnostic.
- Expand the human evaluation to a broader age/education range to more faithfully match the FRCT normative population.

---

## Novel Insights

The most genuinely novel insight beyond the benchmark itself is the concept-recognition hypothesis demonstrated in §4.1. The controlled experiment substituting semantically rich MA1 stimuli with abstract CF2-generated line patterns — while holding all other task parameters constant — provides clean causal evidence that current MLLMs function as concept-level recognizers rather than general visual processors. This connects naturally to the "Middle Score Anomaly" observed on P3 (30–50% accuracy on a trivially binary human task), where partial success is better explained by partial conceptual coverage than by partial visual ability. The structural mismatch identified in §4.2 — that verbalization through chain-of-thought is inherently lossy for spatial configurations that lack stable linguistic representations (VZ2 hole positions, CF2 grid patterns) — offers a principled mechanistic explanation for why CoT harms perceptual tasks while helping reasoning tasks, reinforcing and extending the hypothesis from Liu et al. (2025a).

---

## Suggestions

1. **Add a contamination analysis** comparing verbatim FRCT items vs. parametrically generated Normal items for the same models; if scores are similar, contamination is unlikely.
2. **Report per-item accuracy alongside group accuracy** for all grouped-consistency subtests to facilitate fair cross-task comparisons.
3. **Extend generated-difficulty evaluation** (Table 3 style) to at least five representative models from different families.
4. **Deeper investigation of RL2 human underperformance** — clarify whether this reflects genuine MLLM advantage on logical/linguistic reasoning or an artifact of the digital adaptation of a task that requires drawing relationships.
5. **Discuss practical impact on data scaling** — given the parametric generator produces unlimited training items, even a preliminary RL fine-tuning experiment on one or two subtests would demonstrate the benchmark's practical utility for model improvement.

---

## Score and Decision

VisFACTOR is a well-motivated benchmark paper with a genuinely novel psychometric grounding, a comprehensive 23-model evaluation, a human baseline, and meaningful failure analysis. The core finding — that the best frontier model scores 30.17% against human 78.8% on standardized cognitive vision tasks — is both surprising and actionable. The major unresolved issues (contamination, single-model generated-subset evaluation, scoring incommensurability) are real but correctable; none invalidates the central contribution. The paper sits clearly above the venue mean in originality and relevance.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>