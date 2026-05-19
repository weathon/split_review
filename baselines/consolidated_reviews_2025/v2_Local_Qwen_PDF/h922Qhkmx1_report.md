## Summary
This paper introduces Multi-Source Diffusion Models (MSDM), a unified framework that learns the joint prior distribution of musical sources to enable simultaneous music generation and source separation. By leveraging denoising score-matching, the model performs total generation, partial generation (source imputation), and separation from a single trained network. The authors propose a novel Dirac likelihood inference method for separation, demonstrating competitive quantitative results on Slakh2100 and qualitative improvements in generation tasks. While the conceptual unification of generation and separation is compelling, the manuscript requires tighter claim bounding, explicit discussion of computational trade-offs, and stronger theoretical justification for the Dirac approximation to meet publication standards.

## Strengths
1. **Conceptual Unification:** The proposal to learn the joint prior $p(x_1, \dots, x_N)$ elegantly bridges the gap between generative modeling and source separation, offering a theoretically grounded path toward multi-task audio models.
2. **Novel Inference Mechanism:** The Dirac likelihood formulation provides a principled alternative to Gaussian likelihoods, enforcing the exact additive mixing constraint and yielding measurable improvements in separation quality.
3. **Comprehensive Evaluation:** The paper provides both subjective listening tests and objective metrics (FAD, SI-SDRI) across generation and separation tasks, including a data efficiency study on MUSDB18-HQ.
4. **Reproducibility Effort:** The authors provide a public repository and detailed hyperparameter ablations (Appendix D), facilitating independent verification and future research.

## Weaknesses
1. **Overstated Novelty and Performance Claims:** The abstract and conclusion claim the method is the "first example" of a single model handling both tasks and state separation results are "comparable to state-of-the-art regressor models." Table 3 shows a ~1.25 dB gap behind Demucs + Gibbs. These claims require scoping to avoid misleading readers about practical readiness.
2. **Algorithmic Symmetry Bias:** Algorithm 1 constrains the $N$-th source as $x_N = y - \sum_{n=1}^{N-1} x_n$, breaking symmetry among stems. Without permutation averaging or explicit bias analysis, separation quality may depend on source ordering, threatening fairness and reproducibility.
3. **Missing Efficiency Trade-off Discussion:** The limitations section omits the critical inference latency gap. Table 4 shows MSDM is significantly slower than deterministic baselines. Ignoring this undermines deployability claims and scientific honesty.
4. **Theoretical Justification for Dirac Approximation:** The derivation in Appendix A relies on a Monte Carlo approximation (Eq. 16 to 18) without bounding the error or justifying the high-noise concentration assumption. This leaves the posterior gradient estimation partially heuristic.

## Key Issues
1. **Claim-Evidence Mismatch in Separation Performance:** The manuscript claims parity with SOTA regressors, but empirical results show a consistent deficit. This mismatch risks reviewer rejection for overclaiming.
2. **Source Ordering Bias in Dirac Sampler:** The hard constraint on the $N$-th source introduces an uncontrolled variable. If performance varies by instrument position, the method's reliability is compromised.
3. **Unbounded Novelty Assertion:** The "first example" claim lacks precise scoping (e.g., "first diffusion-based joint prior model"). Without boundaries, it is vulnerable to counterexamples from autoregressive or GAN-based multi-task models.
4. **Incomplete Limitation Analysis:** Omitting inference latency and computational cost prevents readers from assessing the method's practical trade-offs, reducing the paper's impact on deployment-oriented research.

## Actionable Suggestions
1. **Scope Novelty and Performance Claims:** Revise the abstract and conclusion to state "first diffusion-based joint prior model" and explicitly acknowledge the ~1.25 dB gap behind Demucs + Gibbs, framing the contribution as a trade-off between separation accuracy and generative flexibility.
2. **Mitigate Source Ordering Bias:** Implement permutation averaging in Algorithm 1 (run inference $N$ times with different constrained sources and average results) or report variance across source orderings to demonstrate robustness.
3. **Add Efficiency Trade-off Discussion:** Insert a paragraph in Section 6.1 explicitly discussing inference latency (citing Table 4) and proposing mitigation strategies like knowledge distillation or reduced-step sampling for real-time applications.
4. **Justify Dirac Approximation:** In Appendix A, add a theoretical remark justifying the Monte Carlo approximation (Eq. 16 to 18) under the high-noise regime, or provide an empirical sensitivity analysis showing stability across noise schedules.
5. **Enhance Architecture Self-Containment:** Summarize key U-Net hyperparameters (depth, channels, attention heads) in the main text or Appendix C to ensure reproducibility without relying solely on external repository links.

## Storyline Options + Writing Outlines
**Abstract Outline (S1-S5):**
- S1 (Problem): Musical mixtures are additive sums of interdependent sources, making joint modeling essential for both composition and analysis.
- S2 (Gap): Existing models specialize in either generation (collapsing source info) or separation (lacking generative flexibility), preventing unified control.
- S3 (Method): We propose MSDM, a diffusion model learning the joint prior $p(x_1, \dots, x_N)$ to enable simultaneous generation and separation.
- S4 (Innovation): We introduce a Dirac likelihood inference method that enforces exact mixing constraints, outperforming Gaussian baselines.
- S5 (Result): Experiments on Slakh2100 show competitive separation and high-quality partial generation, positioning MSDM as a step toward multi-task audio models.

**Introduction Outline (P1-P4):**
- P1 (Big Picture): Audio generation and separation are dual processes; humans naturally compose and decompose sound simultaneously.
- P2 (Gap): Deep learning models remain siloed. Generative models learn $p(y)$, losing source structure; separators learn $p(x|y)$, lacking unconditional generation.
- P3 (Solution): MSDM bridges this by modeling the joint prior, enabling total generation, partial imputation, and separation from one network.
- P4 (Evidence & Contributions): We validate MSDM on Slakh2100, introduce Dirac likelihood for tighter conditioning, and discuss trade-offs in efficiency vs. flexibility.

## Priority Revision Plan
**P0 (Critical - Claim & Validity):**
- Scope novelty claims in Abstract/Intro/Conclusion to "first diffusion-based joint prior model."
- Bound separation performance claims by explicitly acknowledging the gap vs. Demucs + Gibbs.
- Add permutation averaging or bias analysis for Algorithm 1 to resolve symmetry breaking.

**P1 (Major - Theoretical & Practical Rigor):**
- Justify the Monte Carlo approximation in Appendix A (Eq. 16 to 18) with theoretical or empirical bounds.
- Insert efficiency trade-off discussion in Section 6.1, citing Table 4 inference times.
- Summarize key U-Net hyperparameters in Appendix C for self-containment.

**P2 (Minor - Writing & Presentation):**
- Clarify paradigm differences in Related Work (e.g., SingSong autoregressive vs. MSDM diffusion).
- Quantify filtered chunk percentages in Section 5.2 to prevent cherry-picking concerns.
- Improve figure captions to explicitly state main conclusions and baselines.

## Experiment Inventory & Research Experiment Plan
**Completed Experiment Inventory:**
| Exp ID | Objective | Setup | Metrics | Outcome | Limitation |
|---|---|---|---|---|---|
| E1 | Total Generation | Slakh2100, MSDM vs Mixture Model | FAD, Listening Tests | Comparable quality/coherence | No text conditioning |
| E2 | Partial Generation | Slakh2100, various stem combos | sub-FAD, Listening Tests | Non-trivial accompaniment quality | No baseline for comparison |
| E3 | Source Separation | Slakh2100, MSDM/ISDM vs Demucs | SI-SDRI | Competitive, Dirac > Gaussian | Trails Demucs+Gibbs by ~1.25 dB |
| E4 | Data Efficiency | MUSDB18-HQ, zero-shot/fine-tune | SI-SDRI | Poor zero-shot, improves with fine-tune | Limited stems overlap |

**Research-Theme Gap Diagnosis:**
The core claim of unified generation/separation is validated, but robustness evidence is thin. Missing: multi-seed variance, OOD generalization, and explicit source-ordering bias tests.

**Proposed Research Experiments:**
1. **Source Permutation Robustness (P0):** Run Algorithm 1 with all $N!$ source orderings. Report mean/std SI-SDRI per instrument. *Gain:* Validates symmetry bias claim.
2. **Multi-Seed Variance (P1):** Report separation results over $\ge 3$ random seeds. *Gain:* Establishes statistical reliability of Dirac gains.
3. **OOD Generalization (P1):** Test Slakh-trained MSDM on real-world mixtures (e.g., MUSDB18-HQ without fine-tuning). *Gain:* Bounds external validity claims.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10

**Rationale:** The paper presents a conceptually strong unification of generation and separation via joint prior learning, supported by a novel Dirac likelihood inference method. However, the score is reduced due to overstated novelty/performance claims, unaddressed algorithmic symmetry bias, and missing efficiency trade-off discussion. The mathematical derivation also requires tighter justification. With targeted revisions to bound claims and validate robustness, the paper would be highly competitive.

**Post-Revision Target:** [7.5, 8.5]/10