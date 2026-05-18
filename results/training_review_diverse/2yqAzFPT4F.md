Now I have a thorough understanding of the paper and all claims. Let me verify each criticism against the actual text.

Key verification results:
- The paper acknowledges logit requirement in Discussion (lines 354-356) but uses "black-box" unqualified in title/abstract/contributions
- WB baseline is indeed the authors' own trivial construction (Section 3.2)
- No full-image SPSA baseline exists anywhere in the paper
- "55 iterations" is reported without defining what an iteration is or reporting total queries
- λ and α are named but specific numeric values are not in the main text
- The target phrase shifts from "Sure, here is" (GCG, lines 83/100) to "Sure, here it is" (their method, line 106) without explanation
- Only one GPT-4o showcase example

---

## Summary

This paper proposes Zer0-Jack, a zeroth-order optimization method for directly jailbreaking black-box Multi-modal Large Language Models (MLLMs). The key idea is to use Simultaneous Perturbation Stochastic Approximation (SPSA) with a patch coordinate descent variant (SPSA-P) to generate adversarial images without backpropagation, enabling attacks on models where only output logits (not parameters) are accessible. Experiments on MiniGPT-4, LLaVA1.5, and INF-MLLM1 show high attack success rates (e.g., 95% on MiniGPT-4, Harmful Behaviors dataset) that substantially exceed transfer-based baselines while requiring significantly less GPU memory than white-box alternatives.

## Strengths

1. **First direct (non-transfer) black-box jailbreak for MLLMs using zeroth-order optimization.** The paper provides the first demonstration that a gradient-estimation approach can directly optimize image inputs for jailbreaking MLLMs without white-box access. Evidence: Tables 2-3 show Zer0-Jack achieves 95% ASR on MiniGPT-4 (Harmful Behaviors) versus just 16% for the best transfer method (AutoDAN), a gap of ~80 points that clearly establishes the advantage of direct optimization.

2. **Substantial and well-documented memory reduction.** Table 1 shows concrete numbers: Zer0-Jack uses 10GB vs. 15GB (MiniGPT-4 7B), 22GB vs. 39GB (MiniGPT-4 13B), and the method enables attacking a 70B model on a single A100 (63GB) where the white-box baseline OOMs. This is a practical contribution that enables scaling to larger models.

3. **High ASR across diverse models and datasets.** The method achieves 90-95% on Harmful Behaviors and 95-98% on MM-SafetyBench-T across three different 7B MLLMs and one 70B model, with consistent margins over transfer baselines. This breadth supports robustness of the approach.

4. **Transferability demonstrated.** Table 4 shows that images optimized on MiniGPT-4 transfer to GPT-4o (51.8%), LLaVA1.5 (54.2%), and INF-MLLM1 (54.8%), substantially above the P-Image baselines. This shows cross-model utility beyond the source model.

## Weaknesses

### Major

1. **The core novelty (patch coordinate descent) is unvalidated against the obvious simpler alternative: full-image SPSA.** The paper motivates patch-wise optimization as a way to reduce gradient estimation error in high dimensions (Section 3.3, lines 141-149), and SPSA-P is the main algorithmic contribution. However, there is no experiment comparing SPSA-P against vanilla SPSA applied to the whole image. Without this ablation, we cannot tell whether the patch strategy helps, hurts, or is neutral. The memory advantage comes from zeroth-order optimization itself (no backprop), not from patching. The iteration efficiency comparison is against white-box methods and transfer baselines, not against full-image SPSA. This is the single largest methodological gap — it leaves the central design choice untested.

2. **Query complexity is not reported, making it impossible to assess the practical cost of the attack.** The paper reports "55 iterations on average" (Section 4.4, line 328) but never defines what constitutes an "iteration." From Algorithm 1, each outer loop iterates over all patches, and each patch update performs two forward passes. If "55 iterations" means 55 outer loops, total forward passes ≈ 55 × 49 patches × 2 = 5,390. If it means 55 total patch updates, the cost is much lower but only part of the image is updated. Either way, total forward passes per successful attack — the primary efficiency metric for any black-box method — is never stated. Mean, variance, or max query counts are absent. This prevents comparison with other black-box methods on a common resource axis and undermines the claim of "reasonable queries" (line 30).

### Minor

3. **"Black-box" framing is overstated; the method requires logit access, not just response access.** The paper consistently uses "black-box" in the title, abstract, and contributions without qualification. In practice, the method requires output logits or token probabilities (line 140), which many commercial MLLMs (including Claude, as acknowledged in Section 6) do not expose. The logit_bias trick for GPT-4o is clever but API-specific and possibly patchable. The paper acknowledges these limitations in the Discussion (lines 354-356) but should qualify "black-box" upfront (e.g., "logit-level black-box") so the scope is clear from the start. The contribution remains significant with this qualification, but the current framing is imprecise.

4. **Claim of being "comparable with existing white-box jailbreak techniques" is unsupported.** The only white-box comparison (WB baseline, Section 3.2) is the authors' own trivial construction: full-image gradient descent on the same loss function. This is not representative of state-of-the-art white-box methods such as those combining image and text perturbations (Qi et al. 2024, Shayegani et al. 2023, cited in the paper). The claim in the abstract and contributions (line 35) conflates matching this one trivial baseline with matching "existing white-box techniques." The ASR numbers against this baseline are still meaningful (showing ZO can match direct gradient), but the claim should be tempered to "comparable with a gradient-based white-box baseline" or similar.

5. **Commercial model evaluation is limited to a single showcase example.** Section 4.6 (lines 334-342) demonstrates a successful jailbreak of GPT-4o with one example costing $0.7. While the logit_bias trick is interesting, a single example does not constitute an evaluation. Even 10-20 prompts from the Harmful Behaviors dataset (the paper's own benchmark) with a reported ASR would substantiate the claim of "directly attack commercial MLLMs." The cost is low enough that this expansion seems feasible.

### Trivial

6. **Target phrase mismatch between GCG and the proposed method is not explained.** The paper describes GCG's target as "Sure, here is" (lines 83, 100) but adopts "Sure, here it is" (line 106) for the MLLM version. The reason for this change is not discussed, and no ablation over target prefixes is provided.

7. **No patch size sensitivity analysis.** The patch size is fixed at 32×32 for 224×224 images (line 149). Different patch granularities could affect both ASR and convergence, but no sensitivity analysis is provided.

## Nice-to-Haves

- A comparison of SPSA-P against full-image SPSA on ASR, query count, and convergence (this is actually a Major gap per weakness #1, but listed here as a concrete suggestion).
- Reporting mean, variance, and max query counts (total forward passes) per attack across the test set.
- Patch size ablation (e.g., 16×16, 32×32, 64×64) and its effect on ASR.
- Robustness to simple defenses (JPEG compression, blurring, pixel clipping) to strengthen the threat model.
- An ablation over the target prefix choice ("Sure, here is" vs. "Sure, here it is").

## Removed Points

- **"Hyperparameters λ and α not given numeric values"** — Removed per hard rule on undisclosed hyperparameter nitpicks. These may also be in the appendix (which was stripped by the parser).
- **"The paper should report results for every scenario in MM-SafetyBench-T"** — Not present in the original reviewer's text; the paper already references detailed results in an appendix section.
- **"The patch-only optimization evaluation"** (e.g., reporting ASR when only k patches are optimized) — This is a reasonable ask but belongs in Nice-to-Haves or as part of the SPSA-vs-SPSA-P ablation. The reviewer's framing of it as a "missing part" is too strong; it is an interesting diagnostic, not a requirement.
- **"Reviewer questions novelty claims about being first direct black-box method"** — The paper properly qualifies with "To the best of our knowledge" (line 33), which is standard. Concerns about undiscovered prior work are speculative and cannot be verified.

## Novel Insights

The most interesting observation that emerges across the reviews is the tension between the paper's framing and its actual threat model. The method is presented as a "black-box" attack, but its reliance on logit access places it in a gray area between white-box and response-only black-box. The GPT-4o attack using logit_bias is simultaneously the most impressive practical demonstration and the most fragile component — it exploits a specific API affordance (the ability to bias arbitrary tokens and read their log probabilities) that could be closed at any time. This suggests that the paper's lasting contribution may not be the specific attack on commercial APIs, but rather the general insight that zeroth-order optimization with dimension reduction (patch decomposition) can effectively substitute for backpropagation in the MLLM jailbreaking setting, dramatically reducing memory requirements. The real value is less about "attacking commercial models" and more about "matching gradient-based attack quality without gradients," which the paper demonstrates convincingly for open-source models.

## Suggestions

1. **Add the missing full-image SPSA baseline.** This is the most important addition. Compare SPSA-P against vanilla SPSA on the whole image for ASR, query count, and convergence. This directly validates or refutes the core design choice.

2. **Report total forward passes per attack** (mean, variance, max across the dataset). Define clearly whether "55 iterations" refers to outer loops, total patch updates, or something else. This is essential for any black-box evaluation.

3. **Qualify "black-box" in the title or abstract** as "logit-level black-box" or clarify that the method requires access to output logits/probabilities. This is honest about the scope and does not diminish the contribution.

4. **Temper the white-box comparability claim.** Change "performing comparably with existing white-box jailbreak techniques" to something like "matching a gradient-based white-box baseline" unless additional SOTA white-box comparisons are added.

5. **Expand the GPT-4o evaluation** to at least 20-30 prompts with reported ASR and average cost, to substantiate the commercial model attack claim.

## Score and Decision

The paper presents a genuinely novel approach (zeroth-order optimization + patch coordinate descent for MLLM jailbreaking) with strong empirical results across multiple models. The main contributions — demonstrating that direct black-box optimization can vastly outperform transfer methods while reducing memory — are real and valuable. However, two significant gaps prevent full confidence in the claims: (1) the core algorithmic novelty (patch-wise optimization) is not validated against vanilla full-image SPSA, and (2) query complexity, a primary efficiency metric for black-box methods, is not reported. The "comparable with white-box" claim is also overstated relative to the evidence. These issues are fixable in a revision (adding one ablation and reporting query counts). The paper would benefit from a short rebuttal period to address them, but in its current form the evidence falls short of fully substantiating the claims.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>