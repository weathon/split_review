Now I have verified the paper thoroughly against each reviewer claim. Let me compose the final consolidated review.

## Summary

This paper proposes "informed meta-learning" — a paradigm for learning a mapping from human-interpretable knowledge representations (e.g., natural language) to inductive biases via conditional meta-learning. It formalizes the data-knowledge relationship, provides theoretical motivation (Theorem 1), instantiates the idea with the Informed Neural Process (INP), and presents illustrative experiments on synthetic and real-world data. The paper is positioned as a new viewpoint rather than a state-of-the-art method.

## Strengths

- **Clean formalization of the data-knowledge relationship.** Section 2 rigorously defines the generative process \(f\sim p(f), \mathcal{D}\sim p(\mathcal{D}|f), \kappa\sim p(\kappa|f)\) and establishes key distinctions (D1–D3) between knowledge and empirical data. This provides a clear conceptual framework that future work can build on.

- **Empirical demonstration of improved data efficiency and OOD robustness.** The synthetic experiments (Section 5.1) show that INPs achieve higher log-likelihood across all context sizes (Fig 4a) and maintain performance under distribution shift where the uninformed NP degrades sharply (Fig 5a, 5b). This directly validates the claim that knowledge-conditioned priors can mitigate task heterogeneity.

- **Practical use of LLMs for synthetic knowledge generation.** In the real-data experiments (Sections 5.2.1 and 5.2.2), the authors use GPT-4 to generate natural-language knowledge representations (weather forecasts, class descriptions), demonstrating a scalable approach to obtaining meta-training examples — a concrete solution to a key practical bottleneck discussed in Section 3.2.2.

- **Honest and circumscribed scope.** The paper explicitly states "The aim of our work is not to present a new method that surpasses existing baselines" and repeatedly frames experiments as "illustrative." This self-awareness about the paper's role as a vision piece is a strength, not a weakness.

## Weaknesses

### Fatal
None.

### Major

- **The generalization claim is overclaimed relative to what is actually tested.** Section 5.1.2 tests generalization from \(b\sim\mathcal{N}(2,1)\) (train) to \(b\sim\mathcal{N}(3,1)\) (test) — a distribution shift in the *value* of a scalar parameter. The knowledge \(\kappa\) is the exact numeric value of \(b\). The paper concludes "INPs successfully generalize to previously unseen knowledge representations." While the value \(b=6\) is technically "previously unseen," this tests robustness to distribution shift in the underlying function parameter, not generalization to *semantically novel* types of knowledge (e.g., "this function should be non-decreasing" when training only saw parametric descriptions). The paper itself identifies "generalization to previously unseen, and semantically novel knowledge representations" as a significant challenge in §3.2.2, but Q3 in the experiments explicitly asks whether conditional meta-learning can enable this, and the experiment does not actually address the "semantically novel" part. The claim goes beyond what the evidence supports.

### Minor

- **Theorem 1 is standard Bayesian conditioning dressed up.** The theorem states that conditioning on knowledge reduces expected KL divergence — this is a known property of Bayesian conditioning (more information cannot hurt the true posterior in expectation). The paper is transparent about the gap between true posteriors and learned approximations (§3.2.2: "While the inequality in equation (1) holds for the ground-truth marginals, it is no longer guaranteed to hold for \(p_\theta\)"). But this admission means the theorem does essentially no work toward the central claim. A finite-sample bound or PAC-Bayes analysis would have constituted a genuine theoretical contribution.

- **Missing comparison to conditional meta-learning baselines.** The paper cites Denevi et al. (2020, 2022) on conditional meta-learning but does not compare against any existing method that conditions on task descriptors (e.g., hypernetwork-based meta-learners, conditional neural processes). For a position paper this is not fatal, but it leaves unclear what the INP adds over simply feeding knowledge as an additional input to an existing conditional architecture.

- **No ablation isolating the knowledge encoder's contribution.** In the CUB experiments (Table 1), the paper does not report a "knowledge-only" baseline (predictions using \(\kappa\) alone, without images) or a "knowledge corruption" baseline (random/misleading knowledge). Without these, it is difficult to determine whether improvements come from meaningful knowledge integration or from the additional parameters acting as a learned prior that happens to correlate with class identity.

- **The knowledge-truthfulness assumption (D2) limits practical applicability and is not engaged with critically.** The paper assumes "knowledge should contain only true information." This is stated as a defining property rather than a limitation to be addressed. In real-world deployment, domain knowledge is often incomplete, ambiguous, or incorrect. The paper does not discuss what happens when knowledge contradicts data or when multiple sources conflict. The experiments avoid this issue entirely (all knowledge is derived from ground truth or dataset annotations). While the assumption is reasonable for a formalization, a vision paper should engage more with the practical consequences.

- **No characterization of when knowledge helps vs. hurts.** Section 3.2.2 acknowledges that with finite samples, informed predictions "could be worse" than uninformed ones, but no experiment varies the number of meta-training tasks to map this failure regime. This would directly address an important practical question and add depth.

- **Computational cost not reported.** The INP adds a knowledge encoder and more parameters vs. the NP, but no training time, model size, or inference cost is reported. For a paper proposing a framework for practical use, this is relevant information.

### Trivial

- The uncertainty decomposition in §5.1.3 uses the formula \(\mathbb{I}(y,f\mid x,I)\) for epistemic uncertainty, but the justification that this quantity can be reliably estimated from MC samples from the learned \(q_{\theta_e}\) is not provided in the main text.
- Fig 4a does not explicitly state whether error bars are shown (the paper uses bootstrap standard errors elsewhere).
- Parsing artifacts cause "\(\kappa=\kappa\)" in §5.1.1 where "\(\kappa=\emptyset\)" is intended, and some inline citations are garbled.

## Nice-to-Haves

- **LLM baseline for the weather NLP experiment.** Comparing INP(B) with a prompted LLM that receives the same text forecast and context points would clarify whether the informed meta-learning approach adds value over an off-the-shelf language model for this setting.
- **Test with genuinely loose, semantically expressed knowledge.** The paper would be significantly strengthened by an experiment where knowledge is a natural-language description that cannot be reduced to parametric form (e.g., "this function should be roughly bell-shaped" or "temperatures peak in the early afternoon"), and comparing to a manually encoded prior (e.g., a GP with a hand-specified mean function).
- **Failure cases / negative results.** Including examples where the INP misinterprets knowledge or where misleading knowledge degrades performance would help practitioners understand the method's limitations.
- **Robustness to knowledge corruption.** A simple experiment feeding random or intentionally wrong knowledge would test whether the model actually relies on the semantic content of \(\kappa\) or just treats it as an additional learnable signal.

## Removed Points

The following points from the harsh critic's review were removed or downgraded after verification against the paper:

- **"Weather experiment B does not demonstrate working with genuinely loose knowledge"** — The paper's claim is that the model learns to decode natural language, not that the knowledge is "loose" in the critic's sense. The experiment tests integration of NL-formatted information, which is a valid instantiation of the framework. The knowledge being derived from ground truth is an intentional design choice (to have a known ground truth for evaluation), not a flaw. The criticism was downgraded from Major to Minor/Nice-to-Have.
- **"No comparison to LLM prompting baseline"** — For a position paper that is not trying to beat baselines (as stated explicitly), this is a reasonable future direction but not a structural weakness. Moved to Nice-to-Haves.
- **"Reduction to meta-learning claim is only a design choice"** — The paper is transparent about this being a training procedure (random masking). This is not a flaw; it is implementation. Downgraded to Trivial.
- **"No error bars for κ=∅ comparison"** — The figure shows standard deviation bars (caption for Fig 5b confirms "Bars represent 1 standard deviation"), and the broader empirical methodology includes bootstrap standard errors for other results. Downgraded to Trivial.
- **"Manual methods provide guarantees whereas INP only approximates"** — The paper explicitly acknowledges this in §6 ("this approach lacks the guaranteed correctness that conventional methods enjoy"). This is a known trade-off, not an oversight. Downgraded to Trivial.
- **Theorem should be replaced** — The theorem is appropriate as motivation, not as a proof of the method's superiority. The paper's honest discussion of its limitations (§3.2.2) mitigates the concern. Retained as Minor (shallow) but not elevated to Major.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the tension between the paper's framing as a general framework for automated knowledge integration and the specificity of the experiments (numeric parameters, ground-truth-derived knowledge), but this is an observation about scope rather than a novel synthesis.

## Suggestions

1. **Tighten the generalization claim.** Replace "generalize to previously unseen and semantically novel knowledge representations" with language that accurately reflects what was tested: robustness to distribution shift in parameter values, with semantic novelty as an open challenge. This would make the paper more honest and prevent reader overinterpretation.

2. **Add a knowledge-only ablation for the CUB experiments.** Report zero-shot accuracy using \(\kappa\) alone (without images) and with corrupted/random knowledge. This would isolate the knowledge encoder's contribution and address one of the most natural questions readers will have.

3. **Add one experiment that varies the number of meta-training tasks** and measures the gap between INP and NP performance. This would directly address the finite-sample concern raised in §3.2.2 and provide practical guidance about when the approach is beneficial.

4. **Report computational cost** (training time, parameter count, inference speed) for INP vs. NP to enable practical deployability assessments.

5. **Discuss the knowledge-truthfulness assumption more critically**, including potential mitigations (e.g., confidence-weighting of knowledge, handling contradictions) as future work.

## Score and Decision

This paper introduces a well-formalized and appealing viewpoint on integrating human-interpretable knowledge into meta-learning. The formalization of the data-knowledge relationship is a genuine contribution that could influence future work. The INP implementation provides a reasonable proof of concept. However, the theoretical motivation (Theorem 1) is shallower than its presentation suggests, the empirical validation avoids the hard cases that would most convincingly validate the paradigm (semantically novel knowledge, loose non-parametric descriptions, untruthful knowledge), and the central claim about generalization to "semantically novel" knowledge representations is overclaimed relative to what the experiments test. The paper would benefit from focusing on one or two convincing demonstrations that directly address the paradigm's core promise rather than expanding breadth. For a vision paper the concept has merit, but in its current form the evidence is insufficiently probative.

**MY FINAL SCORE: <pineapple>5.0</pineapple>**
**MY FINAL DECISION: <orange>Reject</orange>**