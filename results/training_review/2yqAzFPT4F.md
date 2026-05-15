Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes Zer0-Jack, a method for jailbreaking black-box Multi-modal Large Language Models (MLLMs) by optimizing image inputs using zeroth-order optimization (SPSA with patch coordinate descent, SPSA-P). The method estimates gradients using only output logits, avoiding backpropagation and thus significantly reducing memory. Experiments on MiniGPT-4, LLaVA1.5, and INF-MLLM1 show high attack success rates (88–98%) that match or exceed white-box methods while using far less GPU memory. The paper also demonstrates a proof-of-concept attack on GPT-4o via a logit-bias trick.

## Strengths

- **First direct black-box gradient-based jailbreak for MLLMs via zeroth-order optimization (SPSA-P).** The method estimates gradients using only output logits, eliminating the need for white-box access or transfer attacks. Evidence: Section 3.3 and Tables 2–3 show 88–98% ASR across four models, while the best transfer-based baseline (AutoDAN) reaches at most 22% on Harmful Behaviors and 52.4% on MM-SafetyBench-T.

- **Dramatic memory reduction without performance loss.** By avoiding backpropagation and optimizing only 32×32 patches, Zer0-Jack reduces memory to near-inference levels, enabling attacks on 13B models with a single 4090 and 70B models with a single A100. Evidence: Table 1 shows white-box requires 39 GB for MiniGPT-4 13B vs. 22 GB for Zer0-Jack, and OOM for 70B vs. 63 GB.

- **Attack success rate matches or exceeds white-box methods across both datasets.** Evidence: Table 2 – MiniGPT-4: WB 93% vs. Zer0-Jack 95%; LLaVA1.5: WB 91% vs. 90%; INF-MLLM1: WB 86% vs. 88%. Table 3 – similar parity (MiniGPT-4: WB 96.4% vs. Zer0-Jack 98.2%).

- **Transferability of optimized images is demonstrated.** Images optimized with Zer0-Jack on MiniGPT-4 transfer to GPT-4o with 51.8% ASR, well above random baselines (P-Text 33.3%, P-Image 40.5%). Evidence: Table 4.

## Weaknesses

### Fatal
None.

### Major

1. **Query efficiency is reported only as "iteration" counts that are not comparable across methods, undermining the efficiency claim.** The paper reports that Zer0-Jack needs ~55 "iterations" on average and claims this is comparable to white-box (40–50). However, each of Zer0-Jack's outer iterations (Algorithm 1) processes all patches sequentially: for a 224×224 image with 32×32 patches (n=49), each iteration requires 98 forward passes (2 per patch × 49 patches). Thus 55 iterations ≈ 5,390 forward passes. For white-box (WB), one iteration is one gradient descent step (one forward + one backward pass ≈ 2 forward-equivalent passes), so 50 iterations ≈ 100 forward-equivalent passes. The paper uses the same term "iteration" for fundamentally different operations without reporting the actual query cost, making the efficiency comparison invalid. This does not undermine the memory-efficiency contribution, but it does leave the computational efficiency claim unsupported.

2. **The attack on commercial MLLMs (GPT-4o) is supported only by a single showcase.** The abstract and introduction claim Zer0-Jack "can directly attack commercial MLLMs such as GPT-4o," but Section 4.6 provides only one example costing $0.70. No systematic ASR across multiple harmful queries, no cost analysis, no discussion of failure modes or rate limits. While the logit-bias trick is clever, a single anecdote does not constitute evidence for the claim made in the contribution list.

### Minor

1. **Missing ablation on the core design choice: patch size.** The paper uses 32×32 patches for 224×224 images but provides no justification or ablation for this choice (e.g., 16×16 vs. 64×64). Similarly, no sensitivity analysis is provided for the smoothing parameter λ or learning rate α. Adding SPSA on the full image (without patching) as a baseline would clearly isolate the benefit of the patch coordinate descent.

2. **The text-based baselines (GCG, AutoDAN, PAIR) are transferred from LLaMA2, a text-only LLM.** Their poor ASR (0–22% on Harmful Behaviors) in a multi-modal setting is expected and does not constitute a strong comparison. The paper's claim of "surpassing transfer-based methods" is accurate but would carry more weight with direct black-box baselines that also optimize images (e.g., plain SPSA on the full image, random search, or CMA-ES). This would better isolate the contribution of the patch decomposition.

3. **The "first method" claim is imprecisely scoped.** The abstract claims "the first method that aims at jailbreaking black-box MLLMs directly." Prior black-box methods like FigStep (gong2023figstep), while not gradient-based, are direct (non-transfer) approaches. The novelty is better captured as "first zeroth-order gradient-based direct black-box jailbreak for MLLMs."

### Trivial

1. No variance or confidence intervals are reported for ASR values. The Harmful Behaviors evaluation uses 100 samples with a single run, making it unclear whether the small gaps between Zer0-Jack and WB (e.g., 90% vs. 91% on LLaVA1.5) are statistically significant.

2. The method requires output logits (score-based black-box), which is a stronger assumption than output-only black-box (text-only). The paper acknowledges this but buries it in the experimental setup ("We only use the logits from models to simulate a black-box situation"); this limitation should be stated earlier and more prominently.

## Nice-to-Haves

- A systematic GPT-4o evaluation with ≥20 harmful queries reporting ASR, average cost, and failure cases would substantially strengthen the commercial MLLM claim.
- Ablation on patch size and hyperparameters (λ, α) to validate the design choices.
- Analysis of image perceptibility (e.g., L2 distortion, human evaluation) to characterize the visibility of perturbations.
- Convergence curves plotting ASR vs. number of forward passes rather than iterations.
- Discussion of how the logit-bias trick interacts with OpenAI's terms of service.

## Removed Points

These points are flagged to be removed, treat them with caution:

- *"The line plot for iterations misses a y-axis label"* — Removed as a formatting/style nitpick per hard rules.
- *"The use of \cref{eq:path_zero_order} appears twice with the same label"* — Removed as a parser artifact issue.
- *"Misses discussion of zeroth-order adversarial attacks on vision-language models"* — Removed per hard rules against requesting missing related works.
- *"The method requires output logits, which is not the standard black-box assumption"* — Moved from major criticism to trivial, as the paper explicitly states this in Section 4.1 ("We only use the logits from models to simulate a black-box situation"), though it could be foregrounded earlier.
- *"The 70B row for WB is '-' because of OOM, making the comparison incomplete"* — Removed because this is actually a strength of the proposed method (the baseline cannot run, while Zer0-Jack can), not a weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews surface useful experimental gaps (forward-pass reporting, ablation studies, systematic GPT-4o evaluation) but do not contribute a new perspective on the method itself.

## Suggestions

1. **Report forward passes, not just iterations, for all methods** (Table 3 or a separate figure). Without this, the efficiency claim cannot be evaluated. Also clarify the definition of "iteration" for each baseline.

2. **Add an ablation baseline**: apply SPSA directly to the full image (without patching) under the same budget. This would isolate the benefit of the patch coordinate descent and demonstrate that the dimensionality reduction is what makes zeroth-order optimization work.

3. **Conduct a systematic GPT-4o evaluation** on at least 20–50 harmful queries, reporting ASR, average dollar cost, and representative failure cases. If API limitations prevent this, explicitly state the constraints and temper the claim accordingly.

4. **Ablate the patch size** (e.g., 16×16, 32×32, 64×64) and report ASR and forward-pass cost for each. This would validate the 32×32 choice and characterize the trade-off.

5. **Rephrase the novelty claim** from "first method that aims at jailbreaking black-box MLLMs directly" to "first zeroth-order gradient-based direct black-box jailbreak for MLLMs" to accurately reflect the gap relative to prior handcrafted-prompt methods like FigStep.

## Score and Decision

The paper introduces a genuinely useful technique — patch-wise zeroth-order optimization for black-box MLLM jailbreaking — and provides strong evidence for memory efficiency and high ASR. However, two major weaknesses undermine important secondary claims: (1) the efficiency comparison is invalid because "iterations" mean different things across methods and forward-pass counts are not reported, and (2) the GPT-4o attack is supported by a single anecdote rather than systematic evaluation. These are addressable in revision but leave the current version with overstated claims relative to the evidence.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>