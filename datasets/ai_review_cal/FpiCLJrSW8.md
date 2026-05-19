- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6
Now I have a thorough understanding of the paper and all the reviewer claims. Let me produce the consolidated final review.

---

## Summary

This paper systematically evaluates how RLHF (PPO and DPO) affects five trustworthiness dimensions—toxicity, stereotypical bias, machine ethics, truthfulness, and privacy—across multiple open-source models (Pythia 1.4B–6.9B, Llama-7B). It provides stage-wise comparisons (pre-RLHF → post-SFT → post-RLHF) and demonstrates that general-purpose RLHF improves machine ethics (31%) but degrades bias (+150%), truthfulness (−25%), and privacy (+12% leakage). The paper also proposes an adaptation of influence-function-based data attribution (DataInf) to the RLHF setting to explain observed trustworthiness changes from a data perspective.

## Strengths

1. **First systematic stage-wise evaluation of RLHF's impact across five trustworthiness aspects.** The paper provides quantitative results at three stages (Figures 2–4) for four models using standard benchmarks. The net-effect summary table (Figure 4, right panel) cleanly shows which aspects improve (machine ethics: ✓), worsen (bias, truthfulness, privacy: ✗), or are unclear (toxicity: ?), directly supporting the central claim that RLHF on generic preferences does not automatically guarantee trustworthiness (Section 4.5).

2. **Novel adaptation of influence-function-based data attribution to the RLHF setting.** The paper adapts DataInf (Kwon et al., 2023) by substituting task-specific loss terms for SFT (Equation 10), the reward model's Bradley-Terry loss (Equation 11), and the DPO policy loss (Equation 12). The approach is technically grounded and represents a genuine methodological extension to a new setting (Section 5).

3. **Mechanistic explanations for each observed trustworthiness trend.** The paper offers concrete, testable explanations: sycophancy for bias increase (Section 4.2), toxicity of chosen vs. rejected responses in the HH dataset for toxicity dynamics (Section 4.1), and helpfulness-driven compliance for privacy leakage (Section 4.5). These add interpretability beyond mere measurement.

## Weaknesses

### Fatal
None.

### Major

1. **The PPO attribution is an unvalidated proxy with unquantified error.** The paper acknowledges it "cannot directly perform attribution on the language model" for PPO and instead computes influence scores on the *reward model* using the Bradley-Terry loss (Section 5, lines 196–202). The reasoning—that trustworthiness changes are "induced by reward maximization" and the reward model provides "the guiding signal for PPO"—is a plausible but unverified proxy. The actual PPO policy update combines the reward signal, KL regularization, and a pretraining term (Equation 3); the reward model alone does not determine the policy's final behavior. The error introduced by this proxy is unquantified. This weakens the claim (contribution 3) that the attribution "explain[s] the misalignment from a data-driven perspective" for PPO specifically. (The SFT and DPO attributions, which operate directly on the language model, do not share this problem.)

2. **The attribution analysis lacks causal validation.** The paper shows that overall contribution scores "align with observed changes in trustworthiness benchmarks" (Figure 5) and that human-selected harmful examples receive high scores (Figure 6), but it never performs a causal test—e.g., removing high-influence data points and verifying that trustworthiness changes in the predicted direction, or comparing attribution-predicted rankings against ground-truth from retraining experiments. Without such validation, the claim that the method "enables practical applications such as influential data identification and dataset pruning" (contribution 3, line 22) remains unsupported. The "cross-validation" asserted in the text (line 220) refers to correlation with aggregate trends, not a rigorous test of the attribution scores.

### Minor

3. **Incorrect claim about loss convexity.** The paper states (line 210): "We note that the loss functions above are all convex, so it's theoretically sound to apply DataInf or similar approximation methods for data attribution." As functions of neural network parameters, these losses (negative log-likelihood, Bradley-Terry, DPO policy loss) are *not* convex. DataInf's theoretical guarantees (Kwon et al., 2023) rely on convexity in parameters. While this is a common simplification in the influence-function literature and does not invalidate the heuristic use of the method, the claim of theoretical soundness is technically inaccurate and should be corrected.

4. **No statistical significance tests for main trends.** The paper reports standard deviations from five independent runs (line 88) but performs no statistical tests (e.g., paired t-test across models or bootstrapped confidence intervals) to support claims about the significance of pre-RLHF vs. post-RLHF differences. Given the consistent direction of trends across all models and both algorithms, the conclusions are likely robust, but formal tests would strengthen the presentation.

5. **The construction of the evaluation set for attribution is underspecified.** For the attribution analysis, the paper defines the evaluation set as pairwise samples `(x_j, y'_j^w, y'_j^l)` where `y'_j^w` and `y'_j^l` are "model generations before and after the fine-tuning step we want to analyze" (Section 5, line 188). However, it is not explicitly stated how these generations are produced (e.g., greedy decoding? temperature sampling? which checkpoint exactly?). This detail matters because it determines the direction of the influence computation.

### Trivial
None.

## Nice-to-Haves

- A per-model correlation analysis examining whether models that become more biased also become less truthful, which would strengthen the understanding of whether these effects are coupled.
- Including a model ≥13B parameters to confirm that the observed trends hold at larger scales (the paper acknowledges this limitation).
- Reporting the computational budget for the attribution experiments to help assess practicality.
- Reporting hyperparameter choices for DataInf (rank of Hessian approximation, λ_l values) for reproducibility.
- Noting explicitly that TruthfulQA multiple-choice measures factual recall under constrained settings, not open-ended generation truthfulness.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The PPO attribution attributes to the *wrong* model"** — The harsh critic calls this a "structural flaw" that "fundamentally does not measure what it claims to measure." However, the paper *explicitly acknowledges* the limitation ("we cannot directly perform attribution on the language model") and clearly describes what the attribution measures ("contribution to reward model's prediction... which is the guiding signal for PPO"). The paper does not claim to be measuring direct policy attribution for PPO. The criticism overstates the issue. The concern is retained (as Major weakness #1) but reframed as an unvalidated proxy with unquantified error, not as a "structural flaw."

- **"The paper does not discuss whether the same models see correlated changes across aspects"** — This is a suggestion for additional analysis, not a genuine weakness.

- **"Model selection only up to 7B"** — The paper explicitly discusses this limitation and cites prior work suggesting trends generalize. This is a scope limitation, not a flaw.

- **"Limitations of the privacy benchmark"** — The privacy benchmark is cited from prior work (Wang et al., 2024) and is a standard evaluation. The critic's concern about the prompting template is speculative.

- **Strength Finder's claims about "demonstration of practical data-attribution use case"** — Weakened by the lack of causal validation; the paper shows feasibility examples, not a demonstrated tool. The strength is still partially valid but is appropriately caveated in the remaining strengths.

- **Generic strengths from Strength Finder** (e.g., "this paper addressed an important problem") — Dropped as generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a synthetic observation that the paper itself does not already articulate.

## Suggestions

1. For the attribution analysis, either (a) restrict PPO attribution to the reward model and clearly label it as an indirect proxy, or (b) derive a proper influence formulation for the PPO policy loss. In either case, add a small-scale validation experiment (e.g., remove the top 10% highest-influence training samples and measure whether trustworthiness shifts in the expected direction) to support the claimed applicability for dataset pruning.

2. Correct the convexity claim in Section 5. Acknowledge that the loss functions are not convex in neural network parameters and that DataInf is applied as an approximation, consistent with common practice in the influence-function literature.

3. Add brief statistical significance statements (e.g., paired tests across independent runs or models) for the key pre-RLHF vs. post-RLHF comparisons in Section 4.

4. Clarify the evaluation set construction for the attribution analysis: how are `y'_j^w` and `y'_j^l` generated, and from which checkpoints?
