Now I have sufficient information to produce the consolidated review. Let me write it.

## Summary

This paper proposes **informed meta-learning**, a framework for automatically integrating human-interpretable knowledge (e.g., natural language) into machine learning models by learning a mapping from knowledge representations to task-specific priors via conditional meta-learning. The authors formalize the data-knowledge generating process, provide theoretical motivation (Theorem 1), instantiate the framework as Informed Neural Processes (INPs), and present experiments on synthetic sinusoidal regression, weather prediction (with GPT-4 generated text forecasts), and few-shot image classification on CUB-200. The synthetic distribution-shift experiment is the strongest result; the real-world language-based experiments are illustrative but lack the baselines needed to fully substantiate the central claim.

## Strengths

1. **Well-formulated conceptual framework**: Sections 2–3 provide a clean, principled probabilistic formalization of the relationship between data, knowledge, and the learning task. The distinctions D1–D3 (human-interpretable domain, truthful knowledge, a priori understood relevance) clarify the intended setting and help position the contribution relative to prior work. The generative model in Fig. 2 is precise and useful.

2. **Strong synthetic experiment establishing proof-of-concept**: The sinusoidal regression experiments (Section 5.1) convincingly demonstrate that INPs improve data efficiency when knowledge (even simple numeric parameter values) is available, and that performance degrades gracefully to NP levels when knowledge is absent. The distribution-shift experiment (Section 5.1.2, Fig. 5) is the paper's most compelling result: INP maintains performance when the task parameter *b* shifts out of the training range, while uninformed NP degrades sharply. This cleanly isolates the mechanism and supports the claim that knowledge can mitigate heterogeneous task distributions.

3. **Epistemic uncertainty decomposition**: The analysis in Section 5.1.3 (Fig. 6, last column) provides a concrete, quantitative illustration of how knowledge reduces epistemic uncertainty globally (e.g., knowledge of oscillation frequency reduces uncertainty across all *x*), while a single data point reduces it only locally. This insight is genuinely informative and distinguishes knowledge from data qualitatively.

4. **Concrete model instantiation with practical training procedure**: INP (Section 4) is a fully specified model. The masking of knowledge during training (setting *k* = 0) to handle missing knowledge at test time is a sensible practical design choice. The paper releases code and data for the main experiments.

## Weaknesses

### Fatal

None.

### Major

1. **Real-world experiments lack critical baselines, making the central claim about human-interpretable knowledge under-supported**: The paper's headline claim is enabling automated knowledge integration from *human-interpretable* representations (particularly natural language). The synthetic experiments use numeric parameters — the weather text (knowledge B) and CUB-200 experiments are the only tests with loosely formatted language. For CUB-200 (Table 1), the only baseline is NP — a method that is not competitive with standard few-shot approaches (ProtoNet, MAML, or even direct CLIP zero-shot). Without these baselines, it is impossible to tell whether INP's improvements over NP translate to meaningful gains relative to reasonable alternatives, or whether the approach is competitive at all. For weather, there is no ablation comparing text-based knowledge (INP B) against simply using the numeric min/max values directly as input features, so it is unclear whether the text embedding adds value beyond the numeric information it describes. Even acknowledging the paper's stated goal ("not to present a new method that surpasses existing baselines on a benchmark dataset"), the experiments need to establish that the *approach works for language* in a way that would not be achieved by simpler alternatives — and the current design does not rule this out.

2. **No ablation of core architectural choices**: The aggregation operator *a* is stated to be a simple sum that "works well in practice" with no supporting comparison. The knowledge encoder *h<sub>θ<sub>e</sub>,K</sub>* is not analyzed for sensitivity to embedding quality or format. The zero-mask for missing knowledge is not ablated (is training with masking essential, or would a separate "unknown knowledge" embedding work as well?). Since the paper's conceptual contribution is about the framework rather than the specific INP architecture, ablations are important to understand which design decisions matter and to guide future implementations.

### Minor

3. **Theoretical contribution is standard and disconnected from practice**: Theorem 1 is a known information-theoretic inequality (data-processing/Blackwell dominance), as the paper acknowledges ("drawing from the results of Ashman et al."). The paper is transparent about this. The more significant issue is that the theorem holds for the optimal predictor under an idealized conditional-independence assumption, but the paper provides no analysis of *when* the finite-sample approximation (Section 3.2.2) fails or succeeds. There is no experiment varying meta-training set size, model capacity, or knowledge complexity to characterize the gap between theory and practice. The only check — that INP with *κ* = ∅ matches NP — is necessary but insufficient.

4. **No evaluation of robustness to incorrect or noisy knowledge**: Assumption D2 states that knowledge contains only true information. The paper acknowledges this is an assumption but does not test robustness when it is violated. In real-world deployment, expert knowledge may be noisy, incomplete, or outright wrong. Without even a synthetic experiment corrupting knowledge (e.g., providing incorrect parameter values), it is unclear how brittle the approach is — a critical limitation for any practical system.

5. **Informed MAML example raises scalability concerns that are not discussed**: The example in Section 3.2 of conditioning MAML's initialization on knowledge via a mapping *g<sub>θ</sub>* from knowledge to weight initializations would require mapping a low-dimensional (text) input to potentially billions of parameters. The paper does not discuss the feasibility or practical challenges of this mapping, which undermines the claimed generality of the framework.

### Trivial

6. The zero-shot performance for knowledge C (GPT-4 generated descriptions) is near random for 5-way classification, suggesting the generated descriptions may be poorly aligned — this is mentioned but not analyzed.
7. The weather forecast experiment (Section 5.2.1) does not control for GPT-4 generation randomness (no multiple seeds or quality analysis), though bootstrap standard errors are reported.

## Nice-to-Haves

- Comparison to an NP baseline that uses class names as text input (without attribute/caption descriptions) on CUB-200, to isolate the effect of richer knowledge.
- Comparison to a non-meta-learning baseline on weather (e.g., a simple regressor using min/max as features) to contextualize the improvements.
- Direct comparison to an LLM-based in-context learner on the weather data, given the paper's discussion of LLMs as an alternative (Section 6).
- Analysis of how meta-training set size affects the gap between INP and NP performance, to characterize the finite-sample approximation failure mentioned in Section 3.2.2.

## Removed Points

These points are flagged to be removed, treat them with caution:

- The critic's claim that "the paper does not engage with advances since 2019 that address [meta-learning struggles with OOD tasks]" — this is a vague complaint about a single citation choice and does not materially affect the paper's framing.
- The critic's concern about image classification code being "promised upon acceptance" — the paper is transparent about this, and it is standard practice for venue review processes.
- The critic's claim that conditioned task-conditioned meta-learning "is not new" — the paper explicitly discusses Denevi et al. (2020, 2022) and frames its contribution as a *perspective* on meta-learning for human-interpretable knowledge, not as a claim to have invented knowledge-conditioned learning itself. This is a misreading of the positioning.
- The strength finder's claim about "73.5% vs 48.8% for 10-way 1-shot on CUB-200" is presented without acknowledging that these comparisons lack standard few-shot baselines that would contextualize the numbers. This strength is weakened by the verified weakness about missing baselines.

## Novel Insights

The most interesting tension across the reviews is between the paper's self-described role as a "new perspective" (position paper / proof-of-concept) and the reviewer's expectation that claims about automated knowledge integration from natural language must be rigorously validated against strong baselines. The synthetic experiments cleanly demonstrate the *mechanism* (knowledge conditions the prior), but the step from "this mechanism works for clean numeric parameters" to "this mechanism works for noisy natural language" requires much stronger bridging evidence than is provided. The paper would benefit from intermediate experiments — e.g., using structured text templates with controlled variation — to isolate what the knowledge encoder learns from language and where it fails. The epistemic uncertainty decomposition is a genuinely useful diagnostic tool that future work in this direction should adopt.

## Suggestions

1. **Add missing baselines to the CUB-200 experiment**: At minimum, compare against ProtoNet, MAML (with comparable backbones), and direct CLIP zero-shot / few-shot on the same splits. This will contextualize whether INP's improvements over NP translate to meaningful absolute performance.
2. **Add a controlled experiment on the weather text condition**: Compare INP with text knowledge (B) against an INP that receives the *same* numeric information (min/max) that GPT-4 was given. If text does not match numeric performance, analyze why (e.g., measure how well the knowledge encoder extracts the relevant features from text).
3. **Add robustness experiments**: Test INP when knowledge is systematically corrupted (wrong parameter values, irrelevant text, misleading descriptions) to characterize the assumption D2 violation.
4. **Ablate the aggregation operator and knowledge encoder**: Compare sum vs. concatenation vs. cross-attention for fusion, and analyze sensitivity to knowledge embedding quality.
5. **Characterize the finite-sample gap**: Vary the number of meta-training tasks and show the INP vs. NP performance crossover, providing practical guidance on when the approach is safe to use.
6. **Add an analysis of GPT-4 text quality**: Show examples where the generated forecasts are accurate vs. misleading, and measure the correlation between text quality and prediction quality.

## Score and Decision

The paper identifies an important problem and provides a clear conceptual framework. The synthetic experiments are well-designed and support the core mechanism. However, the real-world experiments with natural language — which are essential to the paper's central claim — lack the baselines and ablations needed to demonstrate that the approach works for loosely formatted, human-interpretable knowledge in a meaningful way. The theoretical contribution is acknowledged as standard. The paper reads as a promising research proposal rather than a completed empirical contribution. Substantial additional experiments (proper baselines, ablations, robustness analysis) would be needed to make the case.

**Score: 5.5**

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>