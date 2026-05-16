Now I have a thorough understanding of the paper. Let me synthesize the final review.

---

## Summary

This paper proposes **informed meta-learning**, a framework that learns a mapping from human-interpretable knowledge representations (e.g., natural language) to inductive biases of a model via conditional meta-learning. Instead of learning a fixed prior, the model learns a knowledge-conditioned prior $p_\theta(f|\mathcal{K})$ that can be adjusted per task. The paper formalizes the data-knowledge relationship (Section 2), provides theoretical motivation (Theorem 1), instantiates the framework as an Informed Neural Process (INP, Section 4), and demonstrates feasibility on synthetic and real-world experiments (weather prediction, CUB few-shot classification). The contribution is primarily conceptual—introducing a paradigm for automated, steerable inductive bias specification—rather than a state-of-the-art method.

## Strengths

1. **Novel and well-motivated conceptual contribution.** The idea of learning a mapping from human-interpretable knowledge to inductive biases is genuinely novel and timely given the growing use of LLMs for generating knowledge. The paper clearly distinguishes this from manual knowledge integration and standard meta-learning (Section 1, Section 3). The formalization in Section 2 (distinctions D1–D3) provides a clean problem setting.

2. **Theoretical motivation for knowledge conditioning.** Theorem 1 (Section 3.2.1) formally shows that conditioning on knowledge reduces the expected KL divergence to the true predictive distribution compared to using data alone, under the conditional independence assumption. This provides a principled foundation for why informed meta-learning should improve data efficiency.

3. **Demonstrated generalization under distribution shift.** The synthetic experiment (Section 5.1.2, Fig. 5a) directly shows that when the parameter responsible for the domain shift ($b$) is provided as knowledge, the INP maintains predictive log-likelihood on out-of-distribution tasks while the uninformed NP degrades sharply. This concretely supports the claim that informed meta-learning can mitigate task distribution shift.

4. **Improved data efficiency in low-data regimes.** The synthetic experiments (Section 5.1.1, Fig. 4a) show that the performance gap between INP and NP widens as the number of context points decreases, confirming that knowledge integration improves data efficiency.

5. **Real-world demonstration with loosely formatted knowledge.** The CUB image classification experiment (Section 5.2.2, Table 1) shows meaningful improvements over the uninformed NP baseline across all shot settings using genuine knowledge sources (class attributes, human captions, GPT-4 generated descriptions). This demonstrates that the framework works beyond structured synthetic setups.

6. **Honest discussion of limitations and practical considerations.** Section 3.2.2 provides a candid discussion of finite-sample approximation, the need for meta-training sets, and distribution shift challenges. Section 6 acknowledges the lack of guaranteed correctness compared to model-based methods. This transparency strengthens the paper's credibility.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Knowledge source in the weather experiment (Section 5.2.1) requires clarification.** The paper states: "For each task, knowledge κ is a vector encoding two values: the minimum temperature and the maximum temperature on the day" but does not specify whether these are computed from the ground-truth temperature record of that day or obtained from a genuinely separate forecast source. Condition B is explicit about using GPT-4 "based on values from the ground truth temperature measurements," but Condition A is ambiguous. Even if the min/max are derived from the same day's ground-truth data, they are truthful properties of the underlying function $f$ (consistent with the paper's framework), so the concern is not "cheating." Nevertheless, the source should be clarified to match the paper's framing of knowledge as externally-provided information. If the values are computed from the ground truth, the authors should note that this mirrors the synthetic setup where knowledge is a known property of $f$.

2. **Uncertainty decomposition lacks quantitative summary.** The epistemic uncertainty analysis in Section 5.1.3 (Fig. 6, last column) is visually suggestive but only reported qualitatively. Reporting average epistemic uncertainty reduction across tasks (e.g., mean and standard deviation) would make the analysis more informative and support the claim that knowledge reduces model uncertainty.

3. **No discussion of computational overhead.** Encoding knowledge at test time (especially via LLMs for natural language) adds computational cost. The paper should at least acknowledge this trade-off, even if a full cost analysis is beyond the paper's scope.

4. **Baseline NP for classification is not contextualized.** The CUB results (Table 1) show large gains (e.g., 5-way 1-shot: 30.9% vs. 16.7%), but the paper does not discuss whether the baseline NP implementation is well-tuned. A brief comment on how the baseline compares to typical CUB results (even if the goal is not SOTA) would help readers calibrate the improvements.

### Trivial
None.

## Nice-to-Haves

- **Provide a brief proof sketch or intuition for Theorem 1 in the main text.** Even a one-paragraph explanation (e.g., "conditioning on K reduces posterior variance, tightening the KL") would help readers who do not consult the appendix. This would strengthen the theoretical framing without changing the paper's claims.

- **Add a simple experiment on robustness to inaccurate knowledge.** Since D2 assumes knowledge is truthful, a natural extension would be to corrupt the knowledge in the synthetic setup (e.g., adding noise to the revealed parameters) and measure the INP's ability to discount unreliable information. This would deepen the practical narrative without broadening the paper's scope.

- **Comparison to a simple Bayesian baseline in the synthetic experiment.** For the sinusoidal regression with known parameters, a Bayesian linear regression with informative priors would serve as a gold-standard. Showing that INP approaches this baseline would strengthen the claim that automated integration is competitive with hand-crafted priors.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Criticism that Theorem 1 is "stated without a proof sketch, making its exact meaning ambiguous."** The paper states the theorem clearly and references Ashman et al. and the appendix for details. The parser likely stripped the appendix content that contains the proof. The theorem's statement is unambiguous as written. This is moved to Nice-to-Haves (as a suggestion to add a sketch).

2. **Criticism that D2's assumption ("knowledge should contain only true information") is "strong and not tested."** The paper explicitly acknowledges this limitation in Section 6 ("this approach lacks the guaranteed correctness that conventional methods enjoy"). The paper's scope is to propose a framework, not to test every assumption's violation.

3. **"No comparison to manual knowledge integration methods."** The paper explicitly states in the intro (line 33): "The aim of our work is not to present a new method that surpasses existing baselines on a benchmark dataset; rather, we propose a new viewpoint on meta-learning." Demanding this comparison would judge the paper against expectations that do not match its stated goals.

## Novel Insights

The primary insight from the reviews is that the paper's core conceptual contribution — learning a mapping from knowledge representations to inductive biases via conditional meta-learning — is well-received and considered timely. The harsh critic correctly notes that the weather experiment's knowledge source needs clarification, but this is a presentation issue rather than a structural flaw. The reviewer's framing of this as "structural" overstates the severity: even in the worst-case interpretation (min/max from ground truth), the knowledge is a truthful summary statistic of the underlying function $f$, consistent with the paper's own generative model (Section 2). The real strength of the empirical section is the CUB classification experiment, where the knowledge sources are genuinely separate from the labels, and the distribution-shift synthetic experiment, which cleanly demonstrates the framework's potential. The most useful suggestion across both reviews is the call for a robustness-to-inaccurate-knowledge experiment, which would address the paper's acknowledged limitation (D2's truthfulness assumption) and strengthen the practical narrative.

## Suggestions

1. **Clarify the weather experiment's knowledge source in Condition A.** State explicitly whether the min/max values are computed from the ground-truth temperature measurements of the same day, obtained from a separate forecast source, or synthetically generated. If from ground truth, note that these are summary statistics of $f$ (consistent with the synthetic setup) and acknowledge the limitation that this is not a genuinely external knowledge source.

2. **Add a quantitative summary to the uncertainty decomposition analysis** (Section 5.1.3). Report the mean and standard deviation of epistemic uncertainty reduction across tasks, rather than only showing one example in a figure.

3. **Briefly acknowledge the computational overhead** of using LLMs for knowledge encoding at test time, even if only in the Limitations section.

## Score and Decision

This is a well-written, well-motivated conceptual paper that introduces a novel framework for automated knowledge integration. The theoretical motivation is sound, the experiments (while illustrative rather than exhaustive) support the claims, and the authors are transparent about limitations. The weather experiment clarification is a minor issue that can be resolved without changing the paper's conclusions. The contribution — a new paradigm for steerable inductive bias specification via conditional meta-learning — is timely and clearly articulated.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>