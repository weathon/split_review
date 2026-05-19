Now I have all the information needed. Let me synthesize the final review.

## Summary
The paper proposes LoRA-FA, a parameter-efficient fine-tuning method that freezes the down-projection matrix A in LoRA adapters and only updates B, thereby eliminating the need to store full-rank input activations for gradient computation. Experiments on RoBERTa, T5, and LLaMA models show LoRA-FA matches or nearly matches the accuracy of full fine-tuning and LoRA while reducing peak GPU memory by modest but consistent margins. The core idea is clearly presented and the memory complexity analysis is sound.

## Strengths

1. **Clear activation-memory reduction with formal analysis**: The paper provides a precise memory complexity derivation (Section 3.1) showing that LoRA-FA stores only the low-rank activation \(XA\) (size \(bsr\)) instead of the full input \(X\) (size \(bsd\)). This translates to measurable savings in Table 4 — e.g., RoBERTa-large drops from 22.5GB (LoRA) to 15.7GB, T5-base from 32.1GB to 25.3GB.

2. **Competitive accuracy across model families and scales**: Tables 1–3 show LoRA-FA achieves accuracy within 0.1–0.3 points of full fine-tuning and LoRA on GLUE (RoBERTa-large average 88.5% vs 88.5% LoRA and 88.4% FT), matches LoRA on WMT16 translation (T5-large BLEU 37.0), and outperforms LoRA on LLaMA-7B instruction tuning (MMLU 37.4 vs 37.2 on Alpaca) while using only 1.3% of full parameters.

3. **Theoretical grounding via low-rank subspace constraint**: Section 3.1 uses QR decomposition to show that weight updates \(\Delta W\) are constrained to the column space of the initialized \(A\) (Equation 2), and Section 3.3 derives an equivalence to low-rank gradient compression — placing the method on a principled foundation rather than a pure heuristic.

4. **Robustness to hyper-parameters**: Figure 4 systematically compares LoRA and LoRA-FA across ranks (1–128) and learning rates on MRPC, showing similar sensitivity patterns (negative correlation between rank and learning rate), indicating LoRA-FA does not require more careful tuning than standard LoRA.

## Weaknesses

### Fatal
None.

### Major

1. **Headline memory claim is not verifiable from the reported experiments**. The introduction (line 30) states LoRA-FA "reduced the memory footprint from 56GB to 27.5GB for fine-tuning a LLaMA-7B model" — a roughly 2× reduction over full fine-tuning. However, in Table 4, full fine-tuning of LLaMA-7B reports **OOM** (out of memory) under the stated batch-size-1 setup on a single A100 40GB. The 56GB baseline is not anchored to any described experimental condition, and no presented experiment achieves a 2× reduction over full fine-tuning (the closest is ~1.47× for RoBERTa-large). This inconsistency between a headline claim and the paper's own experimental data undermines confidence in the reported numbers. The authors should either present the specific configuration that yields the 56GB measurement or remove the unverifiable claim.

2. **No variance or statistical significance reported for any performance result**. All accuracy numbers in Tables 1–3 are single point estimates with no standard deviations, confidence intervals, or indication of multiple runs. This is especially problematic for the LLaMA experiments (Table 3), where differences between methods are as small as 0.2–0.4% absolute (Alpaca: FT 37.6, LoRA-FA 37.4, LoRA 37.2). Without error bars, these differences are within likely noise ranges, and the claim that LoRA-FA "performs better than LoRA" cannot be evaluated as statistically meaningful.

### Minor

3. **No analysis of sensitivity to A's random initialization**. The method freezes a randomly initialized A that defines the expressible low-rank subspace. The paper does not ablate the effect of different random seeds or initialization distributions on final accuracy. Since the method's representational capacity is entirely constrained to the column space of one specific random draw, the paper should at minimum report variance across multiple initializations or discuss why this concern is moot.

4. **No discussion of when the method might underperform**. The frozen subspace of A may be insufficient for tasks requiring high-rank weight updates (where the optimal \(\Delta W\) lies far from the column space of the initial A). The paper does not acknowledge this limitation or characterize the types of tasks/adaptations where LoRA-FA might degrade relative to full LoRA.

5. **Layer-selection baseline is discussed but not tested**. Section 2 discusses selecting a subset of layers for LoRA as an alternative memory-saving strategy but claims it "could affect the fine-tuning performance." The paper does not experimentally compare LoRA-FA against this approach, which would be a natural ablation to justify why freezing A is preferable to reducing the number of adapted layers.

### Trivial

None.

## Nice-to-Haves

- A wall-clock training time comparison would strengthen the "no computational overhead" claim, which is currently argued from FLOPs alone.
- The gradient-compression connection (Section 3.3) is insightful but could be expanded: the equivalence holds for SGD but the paper uses AdamW in all experiments, so the practical connection to the actual optimizer is less direct.
- A breakdown of peak memory into parameters, activations, and optimizer states would help readers see exactly where the savings come from.

## Removed Points

- **"1.4× over LoRA appears in only one model"** — Removed. The abstract says "up to 1.4×", which is accurate: RoBERTa-large achieves 22.5/15.7 ≈ 1.43×, and the "up to" qualifier honestly captures the maximum across experiments. This is standard practice and not a weakness.
- **"Convergence curves show no trade-off, which should be contextualized"** — Removed. Near-identical convergence is a strength (no degradation), not a weakness. The paper is not claiming a trade-off exists.
- **"Related work lists PEFT methods without comparing to them"** — Removed. The paper explicitly scopes itself as a LoRA variant and states "We will compare to more PEFT approaches in our future work" (line 250). Criticizing a LoRA variant for not comparing to IA3, Prompt Tuning, etc., is scope creep.
- **"FLAN v2 50k sample could be chosen to favor the method"** — Removed as speculative. Line 161 states the split was randomly sampled following prior work (QLoRA).
- **"No comparison to gradient compression methods"** — Removed. Section 3.3 explicitly discusses the relationship and explains why gradient compression is not advantageous in the fine-tuning context.
- **"Gradient compression equivalence glosses over scaling factor and only holds for SGD"** — Removed. The paper acknowledges (line 96–98) that the two methods differ when applying adaptive optimizers like AdamW. The discussion is appropriately caveated.

## Novel Insights
None beyond the paper's own contributions. The reviews did not surface any perspective that fundamentally reframes or deepens the understanding of LoRA-FA beyond what the paper already states.

## Suggestions
1. **Reconcile the memory numbers**: Either present the experimental conditions (batch size, sequence length, GPU count) that produce the 56GB baseline for LLaMA-7B full fine-tuning, or remove the 2× / 56GB claim from the introduction. Clearly state the batch size and settings for every memory figure.
2. **Add error bars** by running key experiments (especially LLaMA/MNLU/MMLU) with 3–5 seeds and reporting mean ± std. Without this, small differences between methods cannot be interpreted.
3. **Ablate A's initialization**: Run LoRA-FA with 3–5 random seeds for A and report the variance in final accuracy. This directly addresses whether the frozen subspace is reliably expressive.
4. **Acknowledge the limitation** that LoRA-FA's expressiveness is restricted to the column space of one random draw of A, and discuss conditions under which this might be insufficient.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>