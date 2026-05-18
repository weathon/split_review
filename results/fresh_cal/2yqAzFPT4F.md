Now I have verified all claims. Let me produce the final consolidated review.

## Summary

This paper proposes Zer0-Jack, a method for directly jailbreaking black-box Multi-modal Large Language Models (MLLMs) using zeroth-order optimization (SPSA) with patch coordinate descent. By avoiding backpropagation and optimizing individual image patches sequentially, the method achieves high attack success rates (e.g., 95% on MiniGPT-4 with Harmful Behaviors dataset, 98.2% on MM-SafetyBench-T) while substantially reducing memory usage compared to white-box gradient-based approaches. The paper also demonstrates a proof-of-concept attack on GPT-4o and shows that the method's adversarial images transfer across models.

## Strengths

1. **Direct black-box jailbreak with strong empirical results**: Tables 2 and 3 show that Zer0-Jack achieves 95% ASR on MiniGPT-4 (HB dataset) and 98.2% on MM-SafetyBench-T, far outperforming transfer-based baselines (best text-based: AutoDAN at 16% and 39.9%, respectively) and matching white-box performance (93% and 96.4%). This directly supports the claim that a zeroth-order approach can rival white-box attacks in a black-box setting.

2. **Clear memory efficiency advantage**: Table 1 documents concrete memory reductions (e.g., from 39G to 22G for 13B MiniGPT-4, from 46G to 25G for 13B LLaVA1.5). Critically, it enables attacking a 70B model with 63GB (single A100) where white-box runs out of memory (OOM). This is a genuine practical advantage derived from avoiding backpropagation.

3. **Patch coordinate descent (SPSA-P) as a principled approach to high-dimensional zeroth-order optimization**: The paper identifies that zeroth-order gradient estimation suffers in high dimensions and proposes optimizing one 32×32 patch at a time. Algorithm 1 and the formal description (Eq. 7–8) are clearly presented. While the numerical claim about dimension reduction is off (see Weaknesses), the conceptual direction is sound.

4. **Competitive iteration efficiency**: Figure 3 shows Zer0-Jack requires ~55 iterations per successful attack, comparable to white-box (40–50) and notably fewer than GCG (~100) or AutoDAN (100–120). This efficiency stems from updating patches immediately rather than waiting for a full-image gradient.

5. **Demonstrated transferability**: Table 4 shows adversarial images optimized on MiniGPT-4 achieve 54.2% ASR when transferred to LLaVA1.5 and 51.8% to GPT-4o, significantly higher than P-Image baselines (14.3% and 40.5%). This supports the claim that zeroth-order optimization produces structured adversarial examples.

## Weaknesses

### Fatal
None.

### Major

1. **No statistical grounding for reported ASR values**: The method involves stochastic elements (random sampling of u per patch per iteration) and GPT-4-based evaluation (non-deterministic), yet all ASR numbers are reported as single point estimates with no error bars, standard deviations, or multiple-seed repetitions. Several comparisons show 1–2% differences between Zer0-Jack and the white-box baseline (e.g., 95% vs. 93% on MiniGPT-4 HB; 98.2% vs. 96.4% on MM-SafetyBench-T). Without variance estimates, these margins cannot be distinguished from noise, and the paper's central quantitative claims are not established with statistical rigor. This is the most significant weakness.

2. **Missing query-cost analysis despite claiming reduction in "query complexity"**: Contribution 2 claims Zer0-Jack "reduces ... query complexity," and the abstract mentions "reasonable queries," yet the paper never reports actual query counts. It reports only iteration counts (~55). For a 224×224 image with 32×32 patches (49 patches), each iteration requires 2 forward passes per patch (98 forward passes per full cycle), totaling ~5,390 forward passes per attack. For a black-box attack, query cost is the primary practical constraint, and this analysis is entirely absent. The claim of reduced "query complexity" is unsubstantiated.

3. **Missing ablation of patch coordinate descent**: The paper does not compare SPSA-P (patchwise) against plain full-image SPSA under equivalent total query budgets. Without this ablation, the reader cannot attribute the method's success to the patch decomposition strategy versus the zeroth-order optimization approach itself. The claimed benefit of mitigating high-dimensional estimation error is not empirically validated.

### Minor

1. **Inconsistent memory comparison in Figure 3**: The bar chart compares memory for GCG and AutoDAN evaluated on LLaMA2-7B (an LLM) against image methods (A-Image, WB, Zer0-Jack) evaluated on MiniGPT-4 (an MLLM), yet the caption says "optimizing a sample on MiniGPT-4." This apples-to-oranges comparison weakens the figure's informativeness.

2. **Mathematical error in dimension reduction claim**: Section 3.3 states that updating one 32×32 patch instead of the full 224×224 image reduces dimensions to "0.02%". The correct figure is approximately 2% (1,024/50,176 ≈ 2.04%). The paper is off by a factor of 100. While this does not affect the method's substance, it is a factual error that should be corrected.

3. **Commercial MLLM attack is a single example**: Section 5.5 demonstrates one successful attack on GPT-4o with one image and one question, costing $0.70. This is an anecdote, not systematic evidence. The claim that Zer0-Jack "can directly attack commercial MLLMs" is not supported by a single qualitative example.

4. **Underspecified image pairing for text-based baselines**: Section 4.1 states that GCG, AutoDAN, and PAIR text prompts are "paired with corresponding images," but it is not explicitly stated whether these are black images (like P-Text), the original dataset images, or something else. This ambiguity affects reproducibility and interpretation of baseline results.

### Trivial
None.

## Nice-to-Haves

- Run the full 500-question Harmful Behaviors dataset (or provide confidence intervals showing the 100-sample estimate is stable).
- Conduct a small-scale GPT-4o evaluation (10–20 diverse harmful questions) with reported ASR and average cost to turn the anecdote into a pilot study.
- Visualize the optimized patches and discuss whether perturbations are structured or noise-like.
- Compare against full-image SPSA to isolate the benefit of patch decomposition.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"P-Text and P-Image are trivial baselines"** (Harsh Critic) — These are intentionally trivial baselines serving as lower bounds; this is standard practice and not a weakness.
- **"No comparison to existing query-based black-box attacks on vision-language models"** (Harsh Critic) — The cited prior works target adversarial classification attacks on vision-language models, not jailbreaking; they operate under a different objective and threat model.
- **"No white-box MLLM baselines (Qi et al., Niu et al.)"** (Harsh Critic) — The paper already includes a WB (white-box) baseline that optimizes images using gradients, which is functionally equivalent to these cited methods for the jailbreaking task.
- **"Call for defense strategy is vague"** (Harsh Critic) — This is a discussion/future-work section; vagueness about defense is not a weakness of the proposed attack method.
- **Several generic strengths from Strength Finder** (e.g., "this paper addressed an important problem") — Removed as superficial.
- **"The 2-point gain above white-box is treated as fact"** (Harsh Critic) — The paper uses the language "comparable" and "on par with," not "surpasses"; this specific criticism overstates the paper's claims. However, the underlying concern about missing error bars is captured in Major Weakness #1.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder are largely convergent on the paper's strengths and weaknesses; the key novel observation from the review process is that the paper's 0.02% dimension-reduction claim is a mathematical error (should be ~2%), and that the query-cost gap (claimed but unmeasured) is a more central weakness than either reviewer independently emphasized. Neither reviewer fully connected the "reduces query complexity" contribution claim with the complete absence of query-count reporting in the experiments.

## Suggestions

1. **Add statistical grounding**: Report mean ASR with standard deviation across at least 3–5 independent runs (different random seeds for patch perturbation ordering and SPSA sampling). This is the single most important improvement.
2. **Report query counts**: For each method, report median and IQR of forward-pass queries required per successful attack. This is essential for substantiating the "query complexity" claim and for practical deployment considerations.
3. **Add the missing ablation**: Compare SPSA-P against full-image SPSA with matched total query budget to empirically validate that patch decomposition reduces estimation error.
4. **Fix the 0.02% error**: Correct to ~2% (or provide the exact calculation).
5. **Strengthen the GPT-4o experiment**: Run 10–20 diverse harmful questions, report ASR and average cost.
6. **Clarify image pairing for text-based baselines**: State explicitly what images are used for GCG, AutoDAN, and PAIR in Section 4.1.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>