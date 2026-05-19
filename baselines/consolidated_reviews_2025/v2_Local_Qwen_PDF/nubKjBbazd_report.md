## Summary
# Final Review Report

## Summary
This paper proposes Adversarial Perturbation Dropout (APD), a method to enhance the transferability of black-box adversarial attacks. The core hypothesis is that existing methods create strong synergistic dependencies between perturbations in different image regions, which limits transferability when target models attend to different semantic blocks. APD addresses this by dynamically dropping perturbation blocks during optimization, guided by Class Activation Maps (CAM) to target attention hotspots. By forcing the optimization to generate robust gradients across diverse regions, APD reduces regional co-adaptation. Experiments on ImageNet demonstrate that APD consistently improves attack success rates when integrated with strong baselines (e.g., MI-FGSM, AA-TI-DIM), achieving up to 19.6% relative gains. The method is modular, computationally manageable, and shows particular effectiveness against models with sparse, multi-block attention patterns.

## Strengths
1. **Novel Conceptual Insight:** The identification of "perturbation synergy" as a bottleneck for transferability is a fresh perspective. Framing the problem as regional co-adaptation during gradient optimization provides a clear mechanistic explanation for why extending perturbations (e.g., TI-FGSM) does not always yield proportional transferability gains.
2. **Effective and Modular Method:** APD is simple to implement and seamlessly integrates with existing iterative attack methods. The CAM-guided dropping strategy is well-motivated and empirically validated against random dropping, demonstrating that targeting attention hotspots is crucial for breaking synergy.
3. **Comprehensive Empirical Validation:** The paper provides extensive experiments across multiple source/target models, ensemble settings, defense mechanisms, and diverse architectures (CNNs, ViTs, LSTMs). The ablation studies on hyperparameters (scale factor, number of centers) and the computational cost comparison (Appendix A.3) strengthen the credibility of the results.
4. **Clear Visualizations:** Figure 1 effectively illustrates the attention region mismatch and the impact of selective noise removal, providing intuitive support for the core hypothesis.

## Weaknesses
1. **Logical Contradiction in Synergy Argument:** The introduction states that extending strategies are limited due to a "lack of assistance with other region’s perturbations," but then claims that "without the synergy from neglected perturbations, attacks may fail." This phrasing is contradictory. The intended meaning is that current methods *over-rely* on synergy, so when a target model ignores certain regions, the attack collapses because the remaining perturbations were not optimized to be independently effective. This confusion undermines the motivation.
2. **Incomplete Methodological Specification:** The optimization formula in the main text presents the update rule "without momentum," but the experiments primarily use momentum-based baselines (MI-FGSM). It is unclear how the averaged gradient from the `nm` dropped images is integrated with the momentum accumulator. Additionally, the computational overhead of `nm` forward/backward passes per iteration is not discussed in the main method section.
3. **Factual Overclaims and Dataset Inaccuracy:** Contribution 3 claims experiments on "various datasets," but the manuscript only reports results on a 1000-image subset of ImageNet. This is a factual inaccuracy. Furthermore, claiming to "reach the state-of-the-art" is risky without comparing against the most recent transferability methods beyond the selected baselines.
4. **Superficial Results Analysis:** The analysis of Table 1 lists percentage improvements but does not discuss why the relative gain diminishes on stronger baselines (e.g., 6.8% for AA-TI-DIM vs. 12.7% for MI). Similarly, the low gain on MnasNet (1.8%) in Table 3 is unexplained, missing an opportunity to discuss architectural limitations.
5. **Critical Reproducibility Defect in Appendix:** Algorithm 1 contains an unfilled placeholder ("Update xadv_{t+1} by ??;") and a naming typo ("ADP" instead of "APD"). This prevents direct implementation without cross-referencing the main text.

## Key Issues
1. **Causal Logic in Motivation (Major):** The synergy argument is currently contradictory. The paper must clarify that the goal is to *reduce dependency* on synergy by forcing each region to contribute independently to the loss, rather than implying that synergy itself is beneficial for the target model.
2. **Reproducibility of Algorithm (Critical):** The pseudocode in Appendix A.4 contains an unfilled update rule placeholder. This is a severe defect that blocks direct implementation. The momentum integration mechanism is also missing from the main formula.
3. **Factual Accuracy of Contributions (Major):** Claiming experiments on "various datasets" when only ImageNet is used damages credibility. Contribution statements should focus on conceptual insights and modularity rather than experimental execution.
4. **Lack of Mechanistic Analysis in Results (Minor):** The diminishing returns on stronger baselines and the low gain on MnasNet are not analyzed. Understanding these boundaries is crucial for validating the synergy-breaking hypothesis.
5. **Grammatical and Stylistic Errors (Minor):** Multiple grammatical errors (e.g., "although... but", "outperform", "are demonstrate") and typos ("behide", "ADP") reduce professionalism and readability.

## Actionable Suggestions
1. **Clarify Synergy Mechanism:** Rewrite the motivation paragraph to explicitly state that current methods *over-rely* on regional synergy, causing attacks to fail when target models attend to different blocks. Frame APD as a mechanism to force independent gradient robustness, analogous to neuron dropout preventing co-adaptation.
2. **Complete Algorithm Specification:** Replace the placeholder in Algorithm 1 with the explicit update rule: `x_{t+1}^{adv} = \Pi_{x, \epsilon}(x_t^{adv} + \alpha \cdot \text{sign}(g))`. Add the momentum integration formula to the main text and acknowledge the `nm` computational overhead.
3. **Correct Factual Claims:** Change "various datasets" to "ImageNet benchmark" in Contribution 3. Reframe the contribution to emphasize modularity and compatibility with diverse baselines. Bound SOTA claims to the evaluated setting.
4. **Deepen Results Analysis:** Add a paragraph discussing why gains diminish on stronger baselines (e.g., AA-TI-DIM already incorporates diversity mechanisms) and why MnasNet shows lower gains (e.g., compact architecture, different attention sparsity). This validates the synergy hypothesis.
5. **Polish Language and Structure:** Fix grammatical errors ("although... but", "outperform", "are demonstrate"). Reorganize the related work into thematic categories (Input Transformations, Ensemble Strategies, Attention-Guided Attacks) to sharply contrast with APD.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem):** Adversarial transferability relies on perturbations crafted on a source model misleading unseen target models, but regional attention mismatches often limit success.
- **S2 (Gap):** Prior methods extend perturbations across the entire image, inadvertently creating strong synergistic dependencies that make attacks brittle when target models attend to different semantic blocks.
- **S3 (Method):** We propose Adversarial Perturbation Dropout (APD), which dynamically drops perturbation blocks during optimization to decouple regional dependencies and force independent gradient robustness.
- **S4 (Mechanism):** By leveraging Class Activation Maps (CAM) to target attention hotspots, APD effectively breaks synergy while maintaining high attack success on the source model.
- **S5 (Result):** Extensive experiments on ImageNet demonstrate that APD consistently improves transferability across diverse baselines and architectures, achieving up to 19.6% relative gains.

### Introduction Outline (Complete)
- **P1 (Big Picture):** DNNs are vulnerable to adversarial attacks; black-box transferability is critical for practical threats but remains limited by model diversity.
- **P2 (Gap):** Existing transferability methods (input transformations, ensembles) treat perturbations as a monolithic whole, creating regional synergy that fails when target attention patterns differ.
- **P3 (Insight):** We identify that perturbations in different attention blocks co-adapt during optimization, reducing independence. Breaking this synergy is key to robust transferability.
- **P4 (Solution):** APD introduces a dropout mechanism on perturbation regions, guided by CAM hotspots, to force the generation of independently effective gradients.
- **P5 (Evidence Preview):** Experiments show APD seamlessly integrates with strong baselines, consistently boosting attack success rates against normally trained, adversarially trained, and defended models.
- **P6 (Contributions):** (1) Synergy bottleneck identification & APD proposal, (2) CAM-guided dropping strategy, (3) Comprehensive validation & modularity demonstration.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0 (Critical)** | Fix Algorithm 1 placeholder and title typo; add momentum integration formula to main text. | Resolves severe reproducibility blocker; ensures method can be implemented directly. | Low |
| **P0 (Critical)** | Correct factual dataset claim ("various datasets" -> "ImageNet"); bound SOTA claims. | Restores credibility; prevents rejection for overclaiming. | Low |
| **P1 (Major)** | Rewrite synergy motivation to clarify causal logic (over-reliance on synergy vs. lack of assistance). | Strengthens core hypothesis; improves narrative coherence. | Medium |
| **P1 (Major)** | Add analysis of diminishing gains on strong baselines and low gain on MnasNet. | Validates synergy hypothesis; demonstrates scientific depth. | Medium |
| **P2 (Minor)** | Reorganize Related Work into thematic categories; fix grammatical errors throughout. | Improves readability and positioning; enhances professionalism. | Low |

**Page Coverage Audit:**
- Page 1: 2 annotations (Abstract, Intro P1-P3) - Covered
- Page 2: 1 annotation (Intro P4-P6, Synergy argument) - Covered
- Page 3: 1 annotation (Contributions, Related Work start) - Covered
- Page 4: 1 annotation (Method Notation, Baselines, Transition) - Covered
- Page 5-6: 1 annotation (APD Method details, Formula) - Covered
- Page 7: 1 annotation (Table 1 results analysis) - Covered
- Page 8: 1 annotation (Defense models, Diverse architectures) - Covered
- Page 9: 1 annotation (Conclusion) - Covered
- Page 13: 1 annotation (Appendix Algorithm/Pseudocode) - Covered

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | APD improves transferability over baselines | ImageNet 1k, 4 source/7 target models, single model setting | ASR (%) | Consistent gains (up to 12.7% avg over MI) | C1, C3 | No variance/seeds reported |
| E2 | APD works with ensemble attacks | 4-model ensemble source, same targets | ASR (%) | Clear margin over baselines | C3 | Limited to one ensemble config |
| E3 | APD bypasses defenses & attacks diverse archs | FD, NRP defenses; Seq2dl, ViT, MnasNet | ASR (%) | Gains on ViT/Seq2dl; low gain on MnasNet | C3 | MnasNet gain unexplained |
| E4 | CAM-guided dropping > Random dropping | Same setup as E1 | ASR (%) | CAM significantly outperforms random | C2 | No ablation on CAM type (Grad-CAM vs others) |
| E5 | Hyperparameter sensitivity (β, centers, scales) | Inc-v3, Res-101 sources | ASR (%) | Optimal at β=27, 4 centers, 7 scales | C2 | Fixed hyperparams used in main results |
| E6 | Compute cost vs transferability gain | MI(1x), MI(15x) vs APD-MI | ASR (%) | APD-MI >> MI(15x) despite similar compute | C1 | Only compared to MI baseline |

### Research-Theme Gap Diagnosis
The core claim of "breaking synergy" is well-supported by E1-E3, but the lack of multi-seed variance reporting weakens statistical reliability. The low gain on MnasNet suggests architectural boundaries that are not fully explored. Additionally, the computational overhead of `nm` passes per iteration is acknowledged but not optimized.

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| C1 (Synergy) | APD gains correlate with attention sparsity | Evaluate on models with varying attention entropy (e.g., ResNet vs. ViT vs. EfficientNet) | Standard baselines | ASR, Attention Entropy | Strong correlation | Medium | Validates mechanism |
| C3 (Robustness) | APD is stable across random seeds | Run E1 with 3-5 seeds | Same baselines | Mean ± Std ASR | Std < 1% | Low | Statistical reliability |
| C2 (Efficiency) | Adaptive dropping reduces cost without losing gains | Dynamic `n` or `m` based on gradient variance | Fixed APD | ASR, FLOPs | Similar ASR, lower FLOPs | Medium | Practical deployment |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6/10

**Rationale:** The paper presents a novel and well-motivated concept (perturbation synergy) with a simple, effective method (APD) that demonstrates consistent empirical gains. The modular design and comprehensive evaluation are strong points. However, the score is reduced due to critical reproducibility defects in the pseudocode (unfilled placeholder), factual overclaims regarding datasets, and logical contradictions in the motivation that undermine the core hypothesis. The lack of statistical variance reporting and superficial results analysis further limit confidence in the conclusions.

**Post-Revision Target:** [7, 8]/10

**Path to Target:** Fixing the algorithm placeholder and momentum integration will resolve the critical reproducibility blocker. Correcting factual claims and clarifying the synergy argument will restore credibility and narrative coherence. Adding multi-seed variance and deeper analysis of architectural boundaries (e.g., MnasNet) will significantly strengthen the scientific rigor and impact.