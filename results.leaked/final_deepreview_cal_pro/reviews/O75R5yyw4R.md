Now I have a thorough understanding of the paper and the calibration anchors. Let me write the final consolidated review.

---

## Summary

This paper proposes IterRef, a test-time scaling method for discrete diffusion models that uses a Multiple-Try Metropolis (MTM) framework to iteratively refine intermediate states during the denoising process. At each selected timestep, the method generates candidate states via a noising-denoising transition kernel and selects proposals according to reward-weighted importance sampling, with theoretical guarantees that the Markov chain converges to the reward-aligned target distribution. IterRef is evaluated across three discrete diffusion backbones (MDLM, LLaDA-8B, MaskGIT) on five reward-guided tasks spanning language and image generation, demonstrating consistent improvements over baselines under equal compute budgets.

## Strengths

- **Strong methodological contribution with theoretical grounding.** The MTM framework with a tailored noising-denoising transition kernel and a carefully chosen balancing function (Eq. 2) provides a principled mechanism for reward-guided refinement in discrete diffusion. Proposition 1 establishes convergence to the optimal intermediate distribution under mild reversibility assumptions — a property absent from prior single-pass guidance methods. The practical design choices (balancing function eliminating resampling, pool reuse on rejection) demonstrably reduce per-iteration cost while preserving the theoretical guarantee (Section 3.3).

- **Broad and consistent empirical validation.** IterRef is evaluated across three discrete diffusion backbones (MDLM, LLaDA-8B, MaskGIT), two modalities (text and image), and five different reward types (toxicity, sentiment, CoLA, perplexity, CLIPScore). The method consistently outperforms FK Steering, SVDD, Search-over-Path, and Best-of-N across nearly all compute budgets and tasks (Figure 2, Table 1). On MDLM, IterRef achieves with 2T NFEs what baselines require 32T NFEs to reach on Sentiment, CoLA, and Perplexity — a 16× compute efficiency gain on those tasks.

- **Insightful analysis of discrete diffusion dynamics.** Controlled experiments isolate the value of iterative refinement: fixing the same compute budget, increasing refinement iterations k while decreasing candidate count N consistently improves reward (Table 3, e.g., k=8/N=4 yields 54.0% toxicity reduction vs. 3.3% for k=1/N=32). The timestep analysis (Table 2) reveals that, unlike continuous diffusion where early steps dominate, later denoising steps are far more influential in discrete diffusion — a practically useful finding for compute allocation.

- **Practical algorithmic design.** The method applies refinement only at selected timesteps (effective set U), allowing flexible cost allocation. The balancing function choice and pool-reuse strategy cut per-iteration cost roughly in half. The method is training-free and can be dropped onto any pretrained discrete diffusion model.

## Weaknesses

### Major

- **Evaluation uses the same reward signal as guidance, with no independent validation.** In every task (toxicity, sentiment, CoLA, perplexity, CLIPScore), the metric reported for evaluation is the output of the same classifier or reward model that was optimized during sampling. This is well known to invite reward overfitting: a method that aggressively exploits proxy weaknesses can achieve high scores without genuinely improving the underlying property. The paper provides no held-out classifier evaluation, no human study, and no fluency/diversity metrics (beyond the circular perplexity task) to rule out this concern. While this limitation affects all compared baselines equally — so the relative comparison remains meaningful — it means the absolute claims about generation quality improvement are not well supported by the evidence presented. The paper references ImageReward scores in Appendix C.1 for MaskGIT, but this is insufficient to address the concern across all tasks. This is the single issue that most weakens the paper and should be addressed through external validation.

### Minor

- **No statistical uncertainty reported.** All figures and tables lack error bars, confidence intervals, or significance tests. With 3 seeds, 15 prompts, and 20 samples per prompt (300 total per condition), the data exists to compute them. The reader cannot judge whether observed gaps between methods are meaningful or noise, particularly for the smaller gaps in the LLaDA-8B results.

- **NFE metric does not fully capture real cost asymmetry.** The paper treats generative model calls and reward model calls as equal under NFE. As the authors acknowledge (line 178), for large models like LLaDA-8B, denoising steps dominate cost, while for MDLM the two are comparable. The paper references wall-clock analysis in Appendix C.4, but the main evaluation (Figure 2, Table 1) relies exclusively on NFE. A brief summary of wall-clock findings in the main body would strengthen the fairness claim.

- **Limited evaluation set size.** Language tasks use only 15 prompts, and the detoxification case study similarly uses 15 high-toxicity prompts. While 300 total samples per condition provides some statistical power, the small prompt set limits confidence that results generalize beyond these specific inputs.

- **No explicit limitations section.** Key caveats — the reward-overfitting concern, dependence on the reversibility assumption, and the NFE vs. wall-clock discrepancy — should be explicitly discussed rather than left implicit or deferred to the appendix.

### Trivial

- **Algorithm 2 vs. Section 3.3 discrepancy.** Algorithm 2 includes the backward resampling step (lines 8–9) that Section 3.3 states is eliminated in the practical implementation. The algorithm should reflect what was actually run, or at minimum include a note that lines 8–9 are skipped in practice.

- **Intermediate reward approximation is described vaguely.** Section 3.3 states intermediate rewards r(x_t) "can approximate by evaluating the reward function on the diffusion model's prediction of x_0" without specifying how the prediction is obtained (single-step prediction, full denoising, etc.). Reproducibility would benefit from a concrete sentence.

## Nice-to-Haves

- Reporting the trade-off between reward optimization and output naturalness (e.g., perplexity under an unrelated reference LM as guidance strength increases) would help readers assess whether gains come at the expense of output quality.
- Discussing how realistic the reversibility assumption (required for Proposition 1) is for modern discrete diffusion backbones, and whether the method is empirically sensitive to its violation.
- Expanding the prompt set beyond 15 examples, particularly for the detoxification case study, to strengthen generality claims.
- Connecting the late-timestep finding (Table 2) back to the noising-denoising kernel design more explicitly.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **"The detoxification examples show the model switching to quoting song lyrics, which could easily fool the toxicity classifier; this possibility is not discussed."** → REMOVED. The paper explicitly discusses this on line 353: "We observe a tendency to reduce toxicity by completing sentences as if they were quoted speech from someone else." The paper acknowledges exactly the behavior the harsh critic claims is undiscussed.

- **"The timestep analysis is presented in isolation; connecting it back to the noising–denoising kernel design would add depth."** → REMOVED. This is a suggestion for additional analysis, not a weakness of the paper as written. Moved to Nice-to-Haves.

- **Strength: "Strong safety-detoxification results"** → KEPT but with the caveat that evaluation uses the same toxicity classifier as guidance, limiting confidence. The qualitative examples are helpful but do not independently validate the detoxification.

## Novel Insights

The finding that late denoising steps (near t=0.1T) dominate reward-guided refinement in discrete diffusion — in direct contrast to continuous diffusion where early steps are most influential — is a genuinely novel and practically useful insight. It suggests that the discrete diffusion sampling dynamics are fundamentally different from their continuous counterparts in ways that affect how one should allocate refinement compute. The paper provides clear evidence for this across four separate tasks (Table 2), making it the most compelling insight beyond the method itself.

## Suggestions

- **High priority:** Add at minimum one independent evaluation metric per task — e.g., a different toxicity classifier for detoxification, perplexity under a held-out LM for fluency, a separate sentiment model. Even a small-scale human evaluation (e.g., 50 comparisons) on one task would dramatically increase trust in the results. This would address the paper's most significant weakness.
- Include error bars or confidence intervals on all figures and tables. The data already exists (3 seeds × 15 prompts × 20 samples); the computation is straightforward.
- Add a brief summary of wall-clock timing results in the main body, since NFE can be misleading for large models.
- Note in Algorithm 2 that the resampling step (lines 8–9) is eliminated in the practical implementation per Section 3.3.
- Add an explicit limitations paragraph that discusses reward overfitting, the reversibility assumption, and the NFE vs. real-cost gap.

## Score and Decision

**Calibration anchors used:**

| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| XsgHl54yO7 (Discrete Guidance for Discrete Diffusion) | 6.50 | R1 | Similar topic; our paper has broader empirical scope but weaker evaluation validation |
| Ombm8S40zN (DDPP — Steering MDMs) | 6.25 | R1 | Very similar topic; DDPP has wet-lab validation compensating for evaluation concerns; our paper has cleaner theory and broader model coverage |
| vi3DjUhFVm (DAS — Alignment without Over-optimization) | 7.25 | R2 | Better paper; explicitly addresses reward over-optimization with cross-reward experiments; our paper is clearly below |
| tfemquulED (Sampling Demons) | 6.20 | R2 | Training-free alignment; our paper has broader empirical coverage (3 models, 2 modalities vs. primarily image generation) and stronger theory |
| MJNywBdSDy (Planned Denoising) | 5.75 | R2 | Discrete diffusion with planning; our paper is stronger in empirical breadth and theoretical grounding |

**Round 1 bracket:** 6.0–7.0, based on the most relevant anchors (XsgHl54yO7 at 6.50, Ombm8S40zN at 6.25 in the middle band; stronger anchors at 7.25+ are clearly above; weaker anchors below 4.0 are clearly below).

**Round 2 narrowing:** The paper sits below vi3DjUhFVm (7.25) and XsgHl54yO7 (6.50) primarily due to the evaluation concern (same reward used for guidance and evaluation without independent validation). It is comparable to Ombm8S40zN (6.25) in theoretical depth but lacks the independent wet-lab validation that partially mitigates DDPP's evaluation concerns. It is above tfemquulED (6.20) due to broader empirical scope and stronger theoretical grounding. **Final score: 6.0.**

The method is genuinely novel, theoretically well-founded, and empirically thorough in its breadth. The single factor preventing a higher score is the significant evaluation weakness — using the same reward signal for both guidance and evaluation across all tasks without independent validation. This is addressable and does not invalidate the core contribution, but it limits confidence in the claimed generation quality improvements.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>