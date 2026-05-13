The paper does not describe how OpenVLA and Octo were fine-tuned or adapted. This is a real gap. However, the baselines are not completely zero — OpenVLA gets 84% on "Grab Remote" in Robot Dog and 50% on "Pick Up Bottle" in Pour Water-L-1/3, suggesting they are functioning but struggling. The concern about baseline adaptation details is valid, but describing it as "fatally unfair" may be overstated.

Now, let me synthesize my review.

## Summary

RDT-1B is a 1.2B-parameter diffusion-based foundation model for bimanual manipulation that addresses two key challenges: (1) designing a powerful architecture (using Diffusion Transformers with QKNorm/RMSNorm, MLP decoding, and Alternating Condition Injection) to capture multimodal action distributions, and (2) enabling training on heterogeneous multi-robot data via a Physically Interpretable Unified Action Space. The model is pre-trained on 1M+ multi-robot trajectories across 46 datasets and fine-tuned on a 6K+ trajectory bimanual dataset, then evaluated on 7 real-robot tasks testing generalization along object, scene, instruction, and skill dimensions.

## Strengths

- **Comprehensive real-robot evaluation across multiple generalization axes.** The 7-task suite genuinely tests distinct capabilities — unseen objects/scenes (Q1), compositional instruction following with novel descriptors like "one-third" (Q2), few-shot skill acquisition (Q3), and dexterity (Q4). This evaluates more dimensions of generalization than is typical in robotics papers. Table 1 demonstrates that RDT outperforms all baselines across every task.

- **Architectural modifications are well-motivated with empirical evidence of necessity.** Fig. 3(a) shows training instability/collapse without QKNorm & RMSNorm, which is a clear indicator that these modifications address a real training issue. The ACI design (alternating cross-attention injection of image and text tokens) addresses a specific identified problem (text being overshadowed by image tokens).

- **Clear problem formulation and scope.** The paper explicitly frames the goal as using multi-robot data to enhance bimanual manipulation "rather than developing a cross-embodiment model" (line 84), which is an honest and useful scoping of claims. The unified action space concept is a reasonable and well-justified approach to cross-robot data integration.

- **Strong ablations for core model design choices.** Table 1 shows that removing diffusion (regression model), reducing model size (from 1.2B to 166M), or removing pre-training all cause substantial performance drops, with particularly dramatic effects on generalization (RDT-scratch achieves 0% on unseen objects). These ablations support the necessity of all three components.

## Weaknesses

### Fatal
None.

### Major

- **Insufficient description of baseline adaptation and fine-tuning details.** OpenVLA (7B) and Octo (93M) are foundation models designed for different robots with different action spaces. The paper provides no description of how these baselines were adapted to the 14-DOF ALOHA bimanual robot — what data they received during fine-tuning, how their action spaces were mapped, or what training procedures were used. While OpenVLA and Octo are not completely broken (OpenVLA achieves 84% on "Grab Remote" and 50% on "Pick Up Bottle" in some tasks; Octo achieves 100% on "Grab Remote"), their near-0% performance on most tasks raises concerns about whether they received comparable adaptation. This gap makes the headline "56% improvement" claim difficult to interpret, since it's unclear whether RDT's advantage comes from the architecture, the pre-training methodology, or from baselines being suboptimally configured. This is addressable in a revision by providing these implementation details.

- **Architectural ablations (QKNorm/RMSNorm, MLP Decoder, ACI) are conducted without pre-training** (line 190: "All the models are without pre-training in this experiment due to resource constraints"). The claimed purpose of ACI is to prevent text information from being overshadowed by image tokens during large-scale pre-training — yet this effect is validated only in the non-pre-trained setting. Whether these architectural choices remain beneficial (or necessary) after pre-training is unknown, which weakens the empirical validation of these contributions for the 1.2B model that is the paper's main claim.

### Minor

- **Small trial counts with no variance reporting.** Most conditions use only 8 trials per setting (each trial shifts the result by 12.5 percentage points); two tasks use 25 trials. No confidence intervals, standard deviations, or repeated runs are reported. This makes fine-grained comparisons (e.g., RDT-small vs. RDT on Unseen Scene at 62.5% each in Table 1) unreliable, though the large gap between RDT and most baselines is sufficiently large to be robust to this noise.

- **The "few-shot learning" framing is somewhat misleading.** The abstract claims the model "learns new skills with just 1~5 demonstrations," but these demonstrations are included in the fine-tuning dataset and the model is gradient-trained on them for 130K steps. While this usage is consistent with robotics conventions where "few-shot" refers to few demonstration trajectories, it diverges from the NLP/in-context-learning convention and may overstate the claim for readers from other fields. The paper would benefit from clarifying that this is fine-tuning with limited data rather than in-context adaptation.

- **The unified action space design lacks empirical ablation.** The paper's second key contribution is the "Physically Interpretable Unified Action Space," but the physical-interpretability property is claimed without being tested against simpler alternatives (e.g., normalization to a standard range). Whether preserving physical meaning actually helps cross-robot transfer compared to simpler unification schemes remains unvalidated, though the overall pre-training pipeline clearly works.

- **Sub-task success rates conflate sequential dependencies.** The sub-task decomposition in Table 3 means failing an early sub-task (e.g., "Pick Up Cup") automatically makes all subsequent sub-tasks fail. The "total" success rate thus conflates sequential failure propagation with independent capability. While this is common in robotics evaluation, a per-sub-task analysis of conditional success rates could better reveal where models fail.

### Trivial
None.

## Nice-to-Haves

- Bootstrap confidence intervals for the 8-trial conditions, or at minimum report number of successes alongside success rates.
- Ablation of ACI, MLP Decoder, and QKNorm on the full pre-trained model, even for a subset of tasks.
- Qualitative failure analysis showing where RDT fails and whether failures stem from perception, language understanding, or motor execution.
- Comparison with an RDT variant using a simpler action space unification scheme to validate the "physically interpretable" claim.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Fatally unfair baseline comparisons"**: While the lack of baseline adaptation details is a real concern (kept as a Major weakness), the characterization as "fatally unfair" overstates the case. OpenVLA and Octo achieve non-trivial scores on several subtasks (OpenVLA: 84% on Grab Remote, 50% on Pick Up Bottle in Pour Water; Octo: 100% on Grab Remote, 50% on Pick Up Bottle in Pour Water), indicating they are operational baselines, not completely broken ones. The concern about insufficient detail is real but not "fatal."

- **"56% improvement claim is meaningless"**: The claim is partially supported by the data — RDT does substantially outperform ACT, which is a well-established bimanual baseline. The 56% figure may be an aggregate that inflates the metric due to near-zero baselines, which is a valid concern, but the improvement over ACT (the strongest non-foundation-model baseline) is still clear.

- **"Request for missing related works"**: Removed per hard rules — cannot verify existence of uncited works.

- **"Missing appendix proofs/details"**: The unified action space definition is deferred to an appendix, but this is standard and the parser strips appendices. Removed per hard rules.

- **"Reproducibility concerns about undisclosed hyperparameters"**: Removed per hard rules — these are standard implementation details impractical to include in a submission.

- **"Formatting/style nitpicks"**: Removed per hard rules.

## Novel Insights

The paper reveals an interesting tension in its evaluation: its strongest baselines (OpenVLA and Octo) are foundation models that were originally designed for different robot embodiments and action spaces. While RDT is specifically adapted to the bimanual domain both architecturally and through a bimanual-focused fine-tuning dataset, whether these baselines received comparable domain adaptation is unclear. This raises a broader question for the robotics foundation model community: how should one benchmark cross-embodiment foundation models on novel target embodiments? A fair comparison requires that all models receive comparable access to the target domain's data and action space representation, and the community would benefit from standardized benchmarking protocols for such settings.

## Suggestions

- Provide explicit details on how OpenVLA and Octo were fine-tuned or adapted to the 14-DOF ALOHA robot, including data, action space mapping, and training procedures. Even a brief appendix description would significantly strengthen the interpretability of the comparisons.
- If possible, validate at least one of the architectural modifications (especially ACI, which is theoretically motivated by scale) on the pre-trained model, even on a limited task subset.
- Reframe "few-shot learning" as "fine-tuning with limited demonstrations" to avoid confusion with the in-context learning convention, or explicitly note the distinction early in the paper.
- Consider adding conditional success rates for sub-tasks (probability of success given previous sub-task success) to separate sequential failure propagation from independent capability assessments.

## Score and Decision

The paper makes a substantial contribution — a 1.2B diffusion foundation model for bimanual manipulation with real-robot evaluation across multiple generalization axes. The core technical approach (diffusion modeling + unified action space + architectural modifications for stability) is sound, and the results are impressive on multiple challenging tasks. The main concerns are: (1) insufficient detail on baseline adaptation, which makes the head-to-head comparison hard to interpret, and (2) architectural ablations conducted without pre-training, which limits validation of those contributions. However, these are addressable concerns — baselines do show some non-trivial performance, and the model's advantages are large enough that they're unlikely to be purely artifact of poor baseline configuration. The ablation for pre-training vs. scratch is convincing. The paper's contributions are real and significant.

Originality: Moderate — unified action space and ACI are novel contributions; diffusion for manipulation is established but scaling to 1.2B for bimanual is new.
Importance of research question: High — bimanual manipulation with generalization is an important and understudied problem.
Claims well-supported: Partially — main claims are supported, but baseline comparison details and pre-trained ablations are gaps.
Experiments: Good real-robot evaluation across multiple generalization dimensions, but trial counts are small and variance is unreported.
Clarity: Good — well-structured with clear problem formulation.
Value to community: High — large-scale bimanual diffusion model with public code/videos.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>