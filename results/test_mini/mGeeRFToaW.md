Now I have verified all reviewer claims against the paper. Let me write the final consolidated review.

## Summary
This paper proposes QZO, a method that enables zeroth-order (ZO) fine-tuning of quantized LLMs by perturbing the continuous quantization scale parameters Δ rather than the discrete quantized weights. QZO combines two components: Q-SPSA (extending SPSA gradient estimation to quantized weights via scale perturbation) and Directional Derivative Clipping (DDC, clipping the estimated directional derivative to stabilize training). Empirically, QZO achieves 18× memory reduction vs 16-bit fine-tuning (e.g., 5.0 GB vs 26 GB for Llama-2-7B) while performing competitively with MeZO, and extends to 2-bit quantization via AQLM.

## Strengths
1. **Clever and well-motivated core idea**. Perturbing continuous quantization scales (Δ) rather than discrete weights to enable ZO on quantized models is elegant and non-obvious. The method cleanly sidesteps the discrete-weight perturbation problem that prior ZO-quantized approaches (e.g., ZO-signSGD variants) struggle with, eliminating the need for de-quantization/re-quantization at each step.

2. **Extreme and clearly-documented memory reduction**. Figure 1 and Table 1 provide compelling memory profiling: QZO (4-bit) achieves 18.3–18.4× GPU memory reduction vs 16-bit full fine-tuning (e.g., OPT-6.7B: 4.8 GB vs 26.8 GB; Llama-2-7B: 5.0 GB vs 26.0 GB). The profiling uses batch size 1 and covers the first 100 steps, providing an apples-to-apples comparison.

3. **Convincing DDC ablation**. Figure 2 shows unambiguously that without DDC, training collapses to NaN within 22 steps, while with DDC it remains stable over 1,000 steps. Figure 3 further demonstrates robustness to the clipping threshold C across a wide range (75–150). This is the strongest empirical evidence in the paper.

4. **Comprehensive evaluation across model families and tasks**. Results span OPT-6.7B, Llama-2-7B, Llama-3.1-8B, and Llama-2-13B across 5 datasets (SST-2, RTE, CB, BoolQ, SQuAD) covering both classification and generation. The 2-bit AQLM results (Table 3) demonstrate feasibility under extreme quantization.

5. **Computational efficiency**. Table 2 shows QZO uses only ~1% of the trainable parameters and a fraction of the FLOPs of MeZO (e.g., OPT-6.7B: 8.19×10¹³ vs 9.91×10¹⁷), since only the quantization scales are updated.

## Weaknesses

### Fatal
None.

### Major
None. No verified weakness is severe enough to invalidate the paper's core claims.

### Minor
1. **DDC variance proof in Eq (8) is technically sloppy.** The step replacing $\mathbb{E}[\|\hat{\nabla}\mathcal{L}\|]^2$ with $(\nabla\mathcal{L})^2$ is not justified: by Jensen's inequality $\mathbb{E}[\|\hat{\nabla}\mathcal{L}\|]^2 \geq \|\mathbb{E}[\hat{\nabla}\mathcal{L}]\|^2 = \|\nabla\mathcal{L}\|^2$, so the equality is incorrect as written. However, the variance reduction claim *is* correct via a cleaner argument: since $d'^2 \leq d^2$ pointwise implies $\|\hat{\nabla}'\mathcal{L}\|^2 \leq \|\hat{\nabla}\mathcal{L}\|^2$, and both estimates are unbiased (Theorem 1), we have $\text{Var}[g'] = \mathbb{E}[\|g'\|^2] - \|\nabla\mathcal{L}\|^2 \leq \mathbb{E}[\|g\|^2] - \|\nabla\mathcal{L}\|^2 = \text{Var}[g]$. The paper should either simplify the proof or fix the erroneous step. This is a presentation/rigor issue, not a fundamental flaw.

2. **No error bars or multiple-seed reporting.** ZO methods are inherently stochastic; single-run results (Table 1) make it impossible to assess whether the reported numbers are a lucky draw or typical. Even 3 seeds with standard deviations would substantially strengthen the evaluation.

3. **No experimental comparison with prior ZO-quantized works.** The related work section (p. 3) cites Feng et al. (2024), Zhou et al. (2025), and Bar & Giryes (2025) as sharing "a similar spirit in minimizing the memory footprint, namely combining zeroth-order optimization with quantization." The paper claims QZO is "inherently more efficient and flexible" but does not provide any experimental comparison. Adding at least a memory/accuracy comparison would substantiate this claim.

4. **Scale-only expressivity not discussed as a limitation.** QZO updates only the quantization scales Δ (~1% of parameters), leaving the discrete integer codes fixed. The paper presents this as a strength (memory/FLOPs savings) but does not analyze or discuss the resulting constraint that individual weights cannot be independently adjusted — only uniformly scaled per quantization group. This could limit performance on tasks requiring fine-grained weight changes (e.g., the gaps on BoolQ and RTE in Table 1 may partly stem from this). An ablation comparing scale-only updates against a variant that also adjusts the integer codes (even occasionally) would clarify the method's scope.

### Trivial
- The clamp to non-negative in Algorithm 1 (`Δ_i ← max(Δ_i - η·d'·z, 0)`) is sensible but not discussed in the main text; it could affect gradient-estimation unbiasedness in practice and deserves brief commentary.

## Nice-to-Haves
- **Comparison with QLoRA** would be useful context, though QLoRA operates in a different paradigm (backprop + LoRA adapters vs ZO + scale updates). A brief head-to-head on memory and accuracy, even if imperfect, would help practitioners situate QZO among the broader landscape of memory-efficient fine-tuning.
- Reporting MeZO hyperparameters (steps, learning rate) used in the experiments would improve reproducibility beyond "adopt the official code."
- The diffusion model results are mentioned (Appendix F) but stripped by the parser; the LLM results stand alone, so this does not affect the core claims.

## Removed Points
These points are flagged to be removed; treat them with caution:
- **"Missing QLoRA comparison" (from Harsh Critic's Critical Issues #2)**: QLoRA uses backpropagation with LoRA adapters, which requires storing gradients and optimizer states — a fundamentally different memory regime from QZO's goal of eliminating all three (weights, gradients, optimizer states). The paper's evaluation focuses on ZO-based methods (MeZO) and full fine-tuning. QLoRA is not a "direct competitor in the same regime" because it does not eliminate gradients/optimizer states. Demoted to Nice-to-Have.
- **"DDC proof is unsupported and likely flawed" (Critical Issues #1)**: The conclusion is correct via a simpler argument (see Minor Weakness 1). The proof is sloppy, not invalid. Demoted from "fatal" to Minor.
- **"Fine-tuning uses SGD not AdamW"**: The paper explicitly notes this as a budget limitation (footnote 2). It is transparent and not a weakness.
- **"Missing appendix content" / "diffusion results not shown"**: Parser artifacts; the original submission contains these sections.
- **"Missing hyperparameters for MeZO"**: The paper states "For MeZO, we adopt the official code," which is standard practice.
- **Strength Finder's claim about "DDC provably stabilizes training through rigorous proof"**: The proof is sloppy as noted in Minor Weakness 1. This strength is retained only for the strong *empirical* evidence (Figure 2), not the theoretical proof.
- **Strength Finder's generic phrasing about the problem being important**: Removed as generic; the concrete strengths above are sufficient.

## Novel Insights
None beyond the paper's own contributions. The two reviews largely agree on the paper's strengths and weaknesses, with the Harsh Critic overstating the severity of the DDC proof issue and the QLoRA omission, both of which the paper handles either adequately or with minor fixes.

## Suggestions
1. **Fix the DDC variance proof.** Replace the muddy derivation in Eq (8) with the simple pointwise argument: $d'^2 \leq d^2 \implies \|g'\|^2 \leq \|g\|^2$, and since both estimates are unbiased, $\text{Var}[g'] = \mathbb{E}[\|g'\|^2] - \|\nabla\mathcal{L}\|^2 \leq \mathbb{E}[\|g\|^2] - \|\nabla\mathcal{L}\|^2 = \text{Var}[g]$. If Theorem 1's unbiasedness requires the appendix proof, include a brief sketch.
2. **Add error bars.** Re-run experiments with at least 3 random seeds and report mean ± std in Table 1.
3. **Compare experimentally with Feng et al., Zhou et al., and Bar & Giryes.** Even a single-dataset memory/accuracy comparison would substantiate the claim that QZO is "more efficient and flexible."
4. **Discuss the expressivity of scale-only updates.** Add a paragraph to the limitations section acknowledging that fine-tuning only the quantization scales constrains the model's ability to make fine-grained weight adjustments.

## Score and Decision

**Bracket summary:**
- **Round 1 bracket** (initial): Plausible range **4.0–6.5**, based on topically similar anchors: ZeroQAT (2.50, weak), SparQ (4.00, middle), FZOO (5.00, middle), CoA-LoRA (5.50, middle), JAGUAR (4.50, middle).
- **Round 2 narrowing**: Examined in full: FZOO (5.00, accepted poster — missing ablation studies, some proof issues), CoA-LoRA (5.50, accepted poster — limited model scale, some reproducibility gaps), JAGUAR (4.50, rejected — sparse experiments, missing baselines). QZO has stronger empirical breadth than JAGUAR and comparable breadth to FZOO, with a cleaner core contribution than CoA-LoRA (whose contribution is primarily in meta-learning for quantization configurations). QZO is closest in quality to FZOO (5.00) and CoA-LoRA (5.50), but sits slightly higher than FZOO due to more comprehensive experiments across model families and slightly lower than CoA-LoRA due to the DDC proof issue and missing error bars.

**Final score: 5.5** — The paper has a genuinely clever core contribution, strong empirical evidence for the main claims, and clear presentation. The weaknesses are addressable (sloppy proof, missing error bars, missing comparison with cited prior works) and do not undermine the core contribution. The paper is above the acceptance threshold for this venue conditional on addressing these issues.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>