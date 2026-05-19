- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper proposes AutoModel, a multi-agent LLM framework that autonomously develops image classification models through iterative refinement by five specialized agents (Project Architect, Data Engineer, Model Engineer, Training Engineer, Performance Analyst). The system requires only a dataset as input, generates and executes code, and iteratively improves performance across data augmentation, architecture selection, and hyperparameter tuning in a unified loop.

## Strengths

- **Multi-agent framework that jointly optimizes the full pipeline.** Unlike prior AutoML work that isolates individual components (data augmentation, architecture search, hyperparameter tuning), AutoModel has five specialized agents that collaborate on all components in a single iterative loop, described in Section 3.2 and visualized in Figure 1. This is a clear architectural contribution over prior isolated AutoML methods.

- **Consistent, substantial gains over zero-shot LLM prompting.** Across all 10 datasets in Tables 1–3, AutoModel outperforms the zero-shot baseline. The most striking case is TinyImageNet, where AutoModel achieves 78.75% vs. 48.15% for zero-shot — a +30.6 point improvement. This demonstrates that the iterative multi-agent process produces meaningful gains beyond a single LLM prompt.

- **Zero-shot initialization technique is empirically validated.** The ablation study (Table 4) shows that generating a single coherent pipeline in one call and then splitting it into components yields substantially higher final accuracy than sequential generation of components. This is a concrete methodological insight with controlled experimental support.

- **Adaptive data augmentation based on dataset semantics.** Section 4.4 provides specific evidence: AutoModel selects ColorJitter for SVHN (lighting variation in real-world house numbers) and deliberately avoids horizontal flips for the dSprites Orientation dataset because flipping would corrupt the orientation label. This demonstrates the LLM's ability to apply semantic reasoning beyond what standard AutoML augmentation search provides.

- **Demonstrated generalization across diverse domains.** The framework is evaluated on standard benchmarks (CIFAR-10, TinyImageNet), robustness datasets (CIFAR-10-C), VTAB tasks (SVHN, dSprites Orientation), and four Kaggle datasets spanning agriculture, kitchenware, Arabic letters, and animal classification — varying in size, image quality, and domain.

## Weaknesses

### Fatal
None.

### Major

1. **The main baseline (zero-shot LLM prompting) is too weak to validate the core claim.** The paper states that zero-shot prompting simulates what a "non-ML expert" would do by asking an LLM to "generate code for training a model on a dataset with x classes." However, the paper's central contribution is the *multi-agent iterative design*, not merely "being better than a single LLM call." Without comparing to a *single-agent iterative baseline* — where one LLM agent receives the same training logs and performance feedback and refines its own code over 20 iterations — the experiments cannot isolate whether the gains come from the multi-agent specialization or simply from having multiple attempts with performance feedback. The 31% gap on TinyImageNet could largely reflect the difference between one-shot generation and iterative refinement with feedback, rather than role specialization. Section 4.3 (ablation) only tests zero-shot initialization and a smaller LLM; the most important ablation — single-agent vs. multi-agent — is absent.

2. **The claim of "human practitioner-level performance" (Abstract, Conclusion) is overstated relative to the evidence.** On the four Kaggle datasets, AutoModel's *average* accuracy lags behind the *best* human submission on the leaderboard by margins of 0.64 to 6.16 percentage points (e.g., Kitchenware: 90.23% vs. 96.39%; Arabic Letters: 94.62% vs. 99.42%). The paper compares its average (across 3 trials) to the best single human submission and argues the ~50% code failure rate makes the comparison fair because humans also make many attempts. But this argument conflates failure rate with actual refinement: a failed iteration provides zero improvement, whereas human "attempts" typically produce valid submissions. The claim in the abstract ("human practitioner-level performance") and the final contribution list ("matches the performance of expert human practitioners") go beyond what the data supports, especially without reporting best-of-3 alongside averages for a more apples-to-apples comparison.

3. **No comparison to standard, non-LLM AutoML methods.** The paper compares only to zero-shot LLM prompting and (on VTAB) Visual Prompt Tuning. It does not compare against standard AutoML techniques on the same datasets — not even simple hyperparameter optimization (random search, Bayesian optimization), data augmentation search (AutoAugment, RandAugment), or standard baselines like a well-tuned ResNet. The selective evaluation makes it impossible to assess whether the costly multi-agent LLM approach offers a practical advantage over much simpler and cheaper alternatives. Even a single such comparison on CIFAR-10 or TinyImageNet would contextualize the results.

### Minor

4. **CIFAR-10-C evaluation uses a non-standard protocol.** The paper creates subsets by uniformly sampling one image per corruption at each severity level, rather than the standard practice of evaluating on all corrupted test images. This means the reported numbers (85.65% on CIFAR-10-C-5) cannot be compared to any published CIFAR-10-C results. While this is acceptable for internal comparisons, it limits the generalizability of the robustness claims.

5. **The 50% code error rate is a significant practical limitation that is under-discussed.** Approximately half of the 20 iterations encounter runtime errors, yielding only ~10 useful iterations. The paper acknowledges this but does not analyze it: what types of errors occur (syntax, shape mismatches, import errors)? Does the error rate decrease over iterations as the system learns? How does the system avoid repeating the same bug? These questions matter for any claim that the system is truly "autonomous" for non-ML experts — a user with no ML background would be unable to debug failed runs.

6. **Missing critical ablations.** Section 4.3 only tests (1) with vs. without zero-shot initialization, and (2) using GPT-4o-mini. The paper does not ablate the multi-agent design itself (e.g., combining all roles into a single agent, removing the Performance Analyst, or removing history summarization), making it impossible to attribute the gains to the specific multi-agent collaboration architecture.

7. **The zero-shot baseline on VTAB datasets may not use the same architecture as AutoModel.** The paper states that for VTAB datasets, the AutoModel Model Engineer "was specifically instructed to use the Vision Transformer (ViT), specifically the ViT-B/16 model, to ensure a fair comparison with the VPT paper." However, it does not state whether the zero-shot LLM baseline was also instructed to use ViT-B/16. If the zero-shot baseline used a different architecture, the comparison is confounded.

### Trivial
- Line 141: "weres" → "were" (typo).
- Line 199-200: The final paragraph appears garbled (likely a PDF extraction artifact, not the original text).

## Nice-to-Haves
- Reporting best-of-3 accuracy alongside averages for Kaggle comparisons would enable a fairer comparison to leaderboard toplines.
- A cost analysis (approximate USD per dataset, number of LLM calls per run) would help readers assess practicality.
- Showing the trajectory of accuracy across the 20 iterations for representative datasets, with indications of which iterations had code failures, would demonstrate the refinement process in action.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Specific prompts not provided (not even in the appendix)"** — Removed per Hard Rules: the parser strips appendix/supplementary sections from all papers; these exist in the original submission.
- **"TinyImageNet zero-shot baseline is suspiciously low (48.15%); standard CNN can exceed 60%"** — Removed: this is the reviewer's speculation about what a different baseline would achieve. The paper's baseline is what the zero-shot LLM actually generated, not a hand-crafted baseline. The paper is transparent about the baseline being a zero-shot LLM prompt.
- **"Robust to code-generation errors" (from Strength Finder)** — Removed: framing a ~50% code error rate as a "strength" is not appropriate. It is a practical limitation that the paper acknowledges but does not solve.
- **"Error handling and recovery not explained"** — Removed as standalone point (merged into weakness #5 above which covers the same ground more precisely).
- **"Missing comparison to GENIUS and Zhang et al. (2023)"** — Removed per Hard Rules and the instruction to not mention missing related works.
- **"Comparison to VPT is selective"** — Merged into weakness #7 with more precise anchor.

## Novel Insights

The harsh critic's most useful observation is that the paper's evaluation cannot isolate the effect of multi-agent role specialization from the simpler confound of "iterative refinement with performance feedback." A single-agent iterative baseline is the minimal experiment needed to attribute the gains to the multi-agent design, and its absence is a structural gap in the evaluation. The strength finder correctly identifies that the zero-shot initialization ablation and the semantic augmentation examples (SVHN vs. dSprites) are the strongest concrete evidence for specific design choices. The tension between these two perspectives reveals that the paper's core claim (multi-agent collaboration drives performance) is plausible but unproven by the current experiments.

## Suggestions

1. **Add a single-agent iterative baseline.** This is the single most impactful addition: let one LLM agent receive the same training logs and performance feedback and refine its own code across 20 iterations. If the multi-agent system outperforms this baseline, the role specialization claim is directly supported.
2. **Tone down the "human practitioner-level" claim** or provide best-of-N performance and a clearer comparison (e.g., reporting whether AutoModel would place in the top X% of Kaggle competitors, not just comparing to the #1 submission).
3. **Add at least one standard AutoML comparison** (e.g., random search over learning rate, weight decay, and architecture) on CIFAR-10 to contextualize the approach's cost-benefit profile.
4. **Report and analyze the code error types and rates** across iterations — is the system learning to avoid common errors?
5. **Use the standard CIFAR-10-C evaluation protocol** (all corrupted test images) to enable comparison with the literature.
