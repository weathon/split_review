## Summary
# Final Review Report

## Summary
This paper introduces PATTERN-MARK, a novel watermarking framework designed specifically for order-agnostic language models (LMs), such as those used in protein generation (ProteinMPNN) and machine translation (CMLM). Unlike sequential LMs, order-agnostic models generate tokens without a fixed left-to-right order, breaking the n-gram context dependency of existing watermarking schemes. To address this, the authors propose a Markov-chain-based key sequence generator that induces high-frequency local patterns, paired with a statistical pattern-based detector that recovers the key structure and performs hypothesis testing on pattern counts. Extensive experiments demonstrate that PATTERN-MARK achieves a superior trade-off between detection efficiency (TPR@FPR), generation quality (pLDDT, BLEU), and robustness against token modification and paraphrasing attacks compared to adapted sequential baselines (Soft watermark, Unigram, Multikey).

## Strengths
1. **Clear Problem Formulation:** The paper identifies a well-defined and practically significant gap: the incompatibility of existing sequential watermarking schemes with order-agnostic LMs due to n-gram context dependency. The motivation is logically sound and clearly articulated.
2. **Novel Methodological Design:** The use of a Markov chain to generate key sequences with high-frequency local patterns is a creative and effective solution. It elegantly bypasses the need for sequential history while enabling reliable statistical detection through pattern counting.
3. **Comprehensive Empirical Evaluation:** The experiments cover two distinct order-agnostic domains (protein generation and machine translation) and evaluate multiple dimensions: detection efficiency, generation quality, robustness against attacks, and hyperparameter sensitivity. The Pareto frontier analysis (Figure 3) provides a rigorous comparison of the quality-detectability trade-off.
4. **Theoretical Grounding:** The inclusion of a dynamic programming algorithm (Alg. 3) to compute the exact pattern occurrence probability under the null hypothesis strengthens the statistical rigor of the detector and ensures controlled false positive rates.

## Weaknesses
1. **Unbounded Novelty and Superiority Claims:** The abstract and introduction claim PATTERN-MARK as the "first work" and "superior technique" without sufficiently scoping these statements to the evaluated benchmarks. Without broader cross-domain validation (e.g., speech, time series mentioned in the intro), these claims risk overstatement.
2. **Fixed-$\delta$ Comparison Limitations:** While Tables 1 and 2 compare methods at matched $\delta$ values, the impact of $\delta$ on distribution distortion may vary across watermarking schemes. Relying primarily on fixed-$\delta$ comparisons can be misleading; the Pareto trade-off analysis is more rigorous but is currently underemphasized in the text.
3. **Deterministic Key Sequence Vulnerability:** The ablation study selects $a_{11}=0$ for the transition matrix, resulting in a fully deterministic alternating key sequence. While this maximizes signal strength, it may introduce vulnerability to adversarial pattern-breaking attacks. The paper does not discuss this robustness trade-off.
4. **Missing Variance and Significance Reporting:** The experimental results report mean TPR and quality metrics but lack variance (standard deviation over multiple seeds) and statistical significance tests. This limits the ability to assess the stability and reliability of the reported gains, especially for small margins.

## Key Issues
1. **Claim-Evidence Alignment in Abstract and Introduction:** The abstract states prior techniques "cannot be directly applied" but omits the core technical reason (n-gram context dependency). This weakens the immediate motivation. Additionally, the "first work" and "superior" claims are not bounded to the evaluated settings, risking overreach.
2. **Methodological Intuition Clarity:** The explanation of why a Markov chain solves the order-agnostic key recovery problem is convoluted in the introduction. The link between local Markovian dependencies, pattern frequency induction, and order-independent detection needs sharper articulation to establish the method's novelty.
3. **Experimental Rigor and Fairness:** Comparing watermarks at fixed $\delta$ values assumes equivalent distortion impact across schemes, which may not hold. Furthermore, the absence of multi-seed variance reporting prevents readers from assessing the statistical reliability of the TPR and quality gains.
4. **Robustness Trade-off Oversight:** The selection of a deterministic transition matrix ($a_{11}=0$) maximizes detection signal but ignores potential adversarial vulnerabilities. The ablation study lacks discussion on how slight stochasticity might improve robustness against targeted pattern-breaking attacks.

## Actionable Suggestions
1. **Refine Abstract and Introduction Gap Statement:** Explicitly state that prior watermarks fail in order-agnostic settings due to their reliance on sequential n-gram context for key derivation. Bound the "first work" and "superior" claims to the evaluated benchmarks (ProteinMPNN, CMLM) and tasks.
2. **Clarify Markov Chain Intuition:** Rewrite the introduction's method intuition paragraph to clearly separate the problem (key recovery without sequential order) from the solution (Markovian pattern generation). Explain how low self-transition probabilities induce alternating patterns that serve as detectable statistical signals.
3. **Reframe Experimental Comparison:** Shift the primary results discussion from fixed-$\delta$ comparisons to the quality-detectability Pareto frontier (Figure 3). Use fixed-$\delta$ results as supplementary evidence. Add multi-seed variance reporting (mean ± std) for all TPR and quality metrics to establish statistical reliability.
4. **Discuss Robustness Trade-offs:** In the ablation study, acknowledge that the deterministic choice ($a_{11}=0$) maximizes signal but may be vulnerable to adversarial pattern-breaking. Suggest that future work or a minor ablation could explore slightly stochastic matrices (e.g., $a_{11}=0.1$) for robustness.
5. **Expand Conclusion with Limitations:** Add a concise paragraph to the conclusion outlining current limitations (e.g., evaluation scope, deterministic key vulnerability) and future directions (e.g., extension to speech/time-series, adaptive pattern lengths).

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** Statistical watermarking is well-established for sequentially decoded LMs but fails for order-agnostic models due to missing sequential context.
- **S2 (Significance/Challenge):** Order-agnostic LMs are critical for protein design, machine translation, and other non-sequential tasks, creating an urgent need for compatible watermarking.
- **S3 (Prior Gap):** Existing schemes rely on n-gram history for key derivation, which is inconsistent or unavailable in non-sequential decoding, leading to key mismatches during detection.
- **S4 (Proposed Method):** We introduce PATTERN-MARK, a framework using Markov-chain-based key generation to induce high-frequency local patterns, enabling order-independent statistical detection.
- **S5 (Key Result & Bounded Implication):** Evaluations on ProteinMPNN and CMLM show PATTERN-MARK achieves superior quality-detectability trade-offs and robustness, positioning it as a strong solution for non-sequential watermarking.

### Introduction Outline (Complete)
- **P1 (Big Picture & Stakes):** AI generation expands into non-sequential domains (proteins, translation), raising security concerns. Watermarking is essential but currently limited to sequential LLMs.
- **P2 (Concrete Gap):** Order-agnostic LMs lack fixed generation order, breaking the n-gram context dependency of prior watermarks. Adapted baselines suffer from key mismatches or quality degradation.
- **P3 (Proposed Idea & Intuition):** PATTERN-MARK solves this by generating keys via a Markov chain, creating predictable local patterns that can be recovered and tested without knowing the global generation order.
- **P4 (Evidence Preview):** Experiments on ProteinMPNN and CMLM demonstrate superior detection efficiency, generation quality, and robustness compared to adapted sequential baselines.
- **P5 (Contribution Summary):** (1) First dedicated watermarking framework for order-agnostic LMs. (2) Rigorous statistical pattern-based detector with controlled FPR. (3) Comprehensive empirical validation of quality-detectability trade-offs.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Refine abstract/intro gap statement to explicitly mention n-gram dependency failure. | Clarifies core motivation and strengthens novelty positioning. | Low |
| **P0** | Bound "first work" and "superior" claims to evaluated benchmarks (ProteinMPNN, CMLM). | Prevents overreach and improves scientific defensibility. | Low |
| **P1** | Reframe results discussion around Pareto-optimal quality-detectability trade-offs (Figure 3). | Provides fairer, more rigorous comparison than fixed-$\delta$ metrics. | Medium |
| **P1** | Add multi-seed variance reporting (mean ± std) for TPR and quality metrics. | Establishes statistical reliability of reported gains. | Medium |
| **P2** | Discuss robustness trade-offs of deterministic key sequence ($a_{11}=0$) in ablation study. | Demonstrates awareness of adversarial vulnerabilities and guides future work. | Low |
| **P2** | Expand conclusion with limitations and future directions (e.g., speech/time-series extension). | Improves scientific maturity and scope awareness. | Low |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Detection efficiency vs baselines | ProteinMPNN, CMLM; Soft, Unigram, Multikey | TPR@FPR, pLDDT, BLEU | PATTERN-MARK outperforms at matched $\delta$ | Superior detection/quality | Fixed-$\delta$ comparison may be unfair |
| E2 | Quality-detectability trade-off | Varying $\delta$ across methods | TPR@FPR=0.1% vs Quality | Superior Pareto frontier | Efficient watermarking | Lacks variance reporting |
| E3 | Robustness to attacks | Random token mod (protein), ChatGPT paraphrase (MT) | TPR@FPR=0.1% under $\epsilon$ | Consistently outperforms baselines | Robustness | No adversarial pattern-breaking tests |
| E4 | Ablation: pattern length $m$ | Varying $m \in [2, 10]$ | TPR@FPR=0.1% | Optimal at $m=4/5$ | Hyperparameter sensitivity | None |
| E5 | Ablation: transition matrix $a_{11}$ | Varying $a_{11} \in [0, 0.5]$ | Quality metrics | Quality stable; $a_{11}=0$ chosen | Signal strength justification | Ignores robustness trade-off |

### Research-Theme Gap Diagnosis
The core claim of superior order-agnostic watermarking is well-supported, but the lack of multi-seed variance limits statistical confidence. Additionally, the deterministic key choice ($a_{11}=0$) leaves a gap in adversarial robustness evaluation.

### Proposed Research Experiments (P0/P1/P2)
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Statistical Reliability | Gains are stable across random seeds. | Run E1/E2 over 3-5 seeds. | Same baselines | Mean ± std TPR/Quality | Non-overlapping CIs | Medium | Validates significance |
| Adversarial Robustness | Deterministic keys are vulnerable to pattern-breaking. | Apply targeted pattern-disruption attacks. | Unigram, Soft | TPR drop under attack | Quantify vulnerability | High | Guides robust design |
| Cross-Domain Generalization | Method extends to other order-agnostic tasks. | Evaluate on speech/time-series models. | Adapted baselines | TPR, Quality | Comparable trade-off | High | Broadens impact |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10
**Post-Revision Target:** [7.5, 8.5]/10

**Rationale:** The paper addresses a clear and practically significant gap in watermarking for order-agnostic LMs, proposing a creative and theoretically grounded Markov-chain-based solution. The empirical evaluation is comprehensive and demonstrates strong performance. However, the score is moderated by unbounded novelty/superiority claims, the lack of multi-seed variance reporting, and the oversight of robustness trade-offs regarding deterministic key sequences. Addressing these issues through claim bounding, variance reporting, and refined experimental discussion would significantly strengthen the paper's scientific rigor and defensibility, justifying the higher post-revision target.