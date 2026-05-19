## Summary
# Final Review Report

## Summary
This paper addresses the challenge of providing faithful, model-agnostic explanations for black-box NLP models by estimating the causal effect of high-level concepts on predictions. The authors propose a theoretical framework linking faithfulness to "order-faithfulness," proving that approximated counterfactual (CF) methods satisfy this property under unbiasedness assumptions, unlike non-causal methods. Practically, they introduce two approaches: (1) LLM-generated CFs for high-quality but costly explanations, and (2) a causal representation learning method for efficient matching-based explanations. Empirical results on the CEBaB benchmark and a new LLM-constructed stance detection benchmark demonstrate that CF generation achieves strong performance, while the causal matching method outperforms existing baselines with significantly lower latency. The paper also highlights that Top-K aggregation universally improves explanation accuracy.

## Strengths
1. **Theoretical Contribution:** The paper introduces a clear and intuitive criterion for explanation faithfulness ("order-faithfulness") and provides a rigorous theoretical proof showing that approximated CF methods satisfy this property under unbiasedness assumptions, while non-causal methods do not. This strengthens the theoretical foundation for using counterfactuals in model explanation.
2. **Dual-Approach Practicality:** By proposing both an LLM-based generative approach and an efficient causal matching method, the paper addresses the trade-off between explanation quality and computational cost. The matching approach's claim of being up to 1000x faster is highly valuable for real-time or large-scale deployment scenarios.
3. **Comprehensive Empirical Validation:** The evaluation covers multiple explained models (including large LLMs like Llama-2), various baselines, and a new stance detection benchmark. The ablation study in the appendix thoroughly validates the design choices of the causal representation learning objective.
4. **Benchmark Construction:** The demonstration of using LLMs to construct a new interventional benchmark for stance detection is a valuable contribution, addressing the scarcity of high-quality causal explanation datasets and enabling out-of-distribution evaluation.

## Weaknesses
1. **Contradiction in Loss Function Rationale:** In Section 3.3, the text states that the method "favors" misspecified matches over misspecified CFs due to shared traits, but the formal ranking order ($x_{\neg M} \preceq x_{\neg CF} \preceq x_M \preceq x_{CF}$) indicates that misspecified matches have the lowest similarity. This contradiction confuses the intended behavior of the contrastive loss and undermines the method's design rationale.
2. **Unbounded SOTA Claims:** The introduction and results section claim that LLM-generated CFs are "the SOTA explanations" and that the causal model with GT CFs is "potentially the SOTA explainer." These claims lack necessary qualifiers (e.g., scope, benchmark, comparison set) and appear speculative when relying on impractical assumptions (access to GT CFs).
3. **Missing Theoretical Assumptions in Main Text:** The theorem proving order-faithfulness critically depends on the unbiasedness of the CF approximation error ($E[\epsilon] = 0$). This assumption is defined only in Appendix A, making the main text theorem statement appear universally true without its necessary conditions.
4. **LLM-as-Ground-Truth Limitation:** The new stance detection benchmark relies on GPT-4 to generate "golden CFs." Using the same family of models (LLMs) to generate both the evaluation target and the explanations introduces potential circularity and alignment bias, which is not explicitly acknowledged in the main text.
5. **Reproducibility Gaps:** The reproducibility statement omits crucial details regarding the computational budget (e.g., GPU hours, specific hardware), which are essential for contextualizing the efficiency claims and ensuring fair comparison with baselines.

## Key Issues
1. **Loss Function Ranking Contradiction (Major):** The textual description in Section 3.3 claims the model favors misspecified matches over misspecified CFs, but the formal ranking order places misspecified matches as the least similar. This must be resolved to ensure the method's design is logically sound and clearly communicated.
2. **Theorem Self-Containment (Minor):** The order-faithfulness theorem relies on an unbiasedness assumption ($E[\epsilon]=0$) that is only defined in the appendix. Explicitly stating this assumption in the main text theorem statement is necessary for theoretical rigor.
3. **Hypothetical SOTA Claims (Minor):** Claims about being "potentially the SOTA explainer" based on access to ground-truth CFs are speculative. Reframing these as demonstrating the "upper bound of matching-based explanations" improves defensibility.
4. **Benchmark Ground-Truth Validity (Minor):** The reliance on GPT-4 for generating golden CFs in the new benchmark introduces potential bias. Acknowledging this limitation is crucial for accurate interpretation of the results.

## Actionable Suggestions
1. **Resolve Loss Function Contradiction:** Clarify the intended similarity ranking in Section 3.3. If the goal is to push misspecified matches furthest away, update the text to state that the model "discriminates against misspecified matches more strongly than misspecified CFs." If the ranking is incorrect, update the formal order to match the intuition.
2. **Bound Theoretical and SOTA Claims:** Add the unbiasedness assumption ($E[\epsilon]=0$) explicitly to the theorem statement in Section 3.1. Reframe the "potentially the SOTA explainer" claim in the results section to emphasize that it demonstrates the "upper bound performance of matching-based explanations when ideal CFs are available."
3. **Acknowledge Benchmark Limitations:** In Section 6, add a sentence acknowledging that while GPT-4 provides a scalable proxy for ground-truth CFs, its inherent biases and potential alignment with evaluated LLMs should be considered when interpreting results.
4. **Enhance Reproducibility Details:** In the Reproducibility section, specify the hardware used (e.g., GPU type) and the approximate training/inference time for the causal representation model and baselines to contextualize the efficiency claims.
5. **Improve Abstract Quantification:** Insert 1-2 key metrics (e.g., average error reduction on CEBaB, speedup factor for matching) into the abstract to provide concrete evidence of the method's effectiveness.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** Causal explanations of NLP system predictions are essential for safety and trust, yet existing methods often lack efficiency or are model-specific.
- **S2 (Significance/Challenge):** Faithful explanations require estimating the causal effect of high-level concepts, which traditionally relies on exact counterfactuals that are impractical to acquire.
- **S3 (Prior Gap):** Prior counterfactual approximation methods are limited to simple local manipulations or costly manual annotation, hindering scalable causal effect estimation.
- **S4 (Proposed Method):** We propose two model-agnostic approaches: (1) LLM-generated counterfactuals for high-quality explanations, and (2) a causal representation learning method for efficient matching-based approximations.
- **S5 (Key Result & Implication):** Theoretically, we prove approximated CF methods guarantee order-faithfulness. Empirically, our CF generation achieves state-of-the-art performance on CEBaB, while our causal matching method outperforms baselines with up to 1000× lower latency.

### Introduction Outline (Complete)
- **P1 (Big Picture & Motivation):** Establish the imperative for faithful, causal explanations in NLP to ensure safe deployment and trust. Highlight the opacity of black-box models and the limitations of correlational explainers.
- **P2 (Gap & Solution Preview):** Identify the gap in acquiring exact counterfactuals and the limitations of prior approximation methods (simple manipulations, manual cost). Introduce the proposed theoretical framework (order-faithfulness) and the two practical approaches (LLM generation, causal matching).
- **P3 (Theoretical Contribution):** Briefly explain order-faithfulness and state the theorem that approximated CF methods satisfy this property under unbiasedness, unlike non-causal methods.
- **P4 (Method 1: LLM Generation):** Describe the CF generation approach, its effectiveness, and its computational/latency limitations.
- **P5 (Method 2: Causal Matching):** Introduce the efficient matching alternative, explaining how causal representation learning enables fast CF identification within a candidate set.
- **P6 (Empirical Evidence & Contributions):** Summarize the key findings: CF generation is SOTA among model-agnostic methods, causal matching outperforms baselines efficiently, Top-K universally improves accuracy, and LLMs can construct new explanation benchmarks.

## Priority Revision Plan
| Priority | Issue | Action | Expected Impact |
|---|---|---|---|
| **P0** | Loss Function Contradiction (Sec 3.3) | Clarify the intended similarity ranking between misspecified matches and misspecified CFs; update text or formal order to resolve contradiction. | Ensures logical soundness of the method's design rationale. |
| **P0** | Theorem Assumption (Sec 3.1) | Explicitly state the unbiasedness assumption ($E[\epsilon]=0$) in the main text theorem statement. | Improves theoretical rigor and self-containment. |
| **P1** | SOTA Claim Bounding (Intro/Results) | Qualify SOTA claims to "model-agnostic methods on CEBaB"; reframe hypothetical GT-CF claim as "upper bound demonstration." | Increases defensibility against reviewer scrutiny. |
| **P1** | Benchmark Limitation (Sec 6) | Acknowledge potential bias/circularity of using GPT-4 for golden CFs. | Enhances transparency and accurate result interpretation. |
| **P2** | Reproducibility Details (Sec 10) | Add hardware specs and training/inference time to the reproducibility statement. | Contextualizes efficiency claims and aids reproducibility. |
| **P2** | Abstract Quantification (Abstract) | Insert 1-2 key metrics (error reduction, speedup factor) into the abstract. | Provides concrete evidence of effectiveness upfront. |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | CF generation vs matching baselines on CEBaB | CEBaB test set, 5 explained models (DistilBERT, BERT, RoBERTa, Llama-2-7b/13b) | L2, Cosine, Norm Diff Error | Generative models achieve lower error; Causal Model outperforms matching baselines | CF generation is strong; Causal matching is best among matching methods | No variance/seeds reported in main text |
| E2 | Top-K impact on explanation accuracy | CEBaB, K=1 vs K=10 | L2 Error | Top-K universally lowers error for all methods | Top-K should be a standard | Optimal K selection per example not explored |
| E3 | Causal Model with GT CFs | CEBaB, candidate set includes human-written CFs | L2, Cosine, Norm Diff Error | Outperforms generative models | Demonstrates upper bound of matching | Impractical assumption (access to GT CFs) |
| E4 | New Stance Detection Benchmark | SemEval 2016 tweets, GPT-4 generated CFs, OOD setting | L2, Cosine, Norm Diff Error | Replicates main findings in OOD setting | Validates robustness and benchmark utility | LLM-as-ground-truth bias not fully addressed |
| E5 | Ablation Study (Appendix C) | Variations of candidate sets and loss components | L2, Cosine, Norm Diff Error | All 6 loss components contribute to robustness | Validates design choices | Limited to CEBaB |

### Research-Theme Gap Diagnosis
- **Statistical Reliability:** Main results lack variance reporting (multiple seeds), making it difficult to assess the stability of small error differences.
- **Optimal K Tuning:** The paper arbitrarily selects K=10. A method for adaptive K selection per example is missing.
- **LLM Ground-Truth Validation:** The new benchmark relies on GPT-4 CFs. Human validation of a subset of these CFs would strengthen the benchmark's credibility.

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Statistical Stability | Results are stable across random seeds | Run E1 and E4 over 3-5 seeds | Same baselines | Mean ± Std Error | Std < 5% of mean | Low | Increases confidence in rankings |
| Adaptive K Selection | Optimal K varies by example complexity | Train a small predictor to select K based on query features | Fixed K=10, K=20 | L2 Error | Error reduction vs fixed K | Medium | Improves practical utility |
| Human Validation of CFs | GPT-4 CFs align with human judgments | Sample 100 CFs from new benchmark, have annotators rate quality | Human-written CEBaB CFs | Agreement score | Agreement > 80% | Medium | Validates benchmark ground truth |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
Final Score: 6.5/10
Post-Revision Target: [7.5, 8.5]/10

**Rationale:** The paper makes a solid theoretical contribution by linking faithfulness to order-faithfulness and proposes two practical, model-agnostic explanation methods with strong empirical results. The dual approach (high-quality generative vs. efficient matching) addresses a real-world trade-off. However, the score is moderated by a major contradiction in the loss function rationale, unbounded SOTA claims, and missing statistical details (seeds, compute budget). Addressing the P0/P1 revision items will significantly improve the paper's rigor and defensibility.