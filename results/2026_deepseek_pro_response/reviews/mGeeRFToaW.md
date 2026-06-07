Now I have all the anchors I need. Let me compose the final review with the score.

**Calibration summary across all rounds:**

| Anchor | Score | Round | Comparison to QZO |
|--------|-------|-------|-------------------|
| SensZOQ (myYzr50xBh) | 5.80 | R1,R2 | Most similar — ZO + quantization. QZO has more novel core idea (perturbing scales vs. Fisher-based mask selection). Both have evaluation gaps. QZO slightly better. |
| LOZO (9BiVepgmWW) | 7.00 | R1 | ZO + low-rank. Stronger theory, weaker practical memory savings. QZO is below this. |
| SubZero (FK6T0U4Mg1) | 4.25 | R1 | ZO + random subspace. QZO is clearly stronger. |
| Simultaneous ZO (vqJZb9SX1T) | 4.00 | R1 | ZO + layer-wise sparse. QZO is clearly stronger. |
| Sparse MeZO (4Kw4KAoVnx) | 5.50 | R2 | ZO + sparse parameter selection. QZO has more novel idea, similar evaluation rigor. QZO comparable or slightly better. |
| HiZOO (bEqI61iBue) | 5.67 | R2 | Hessian-informed ZO. Both have theory issues and limited tasks. QZO has more novel idea and stronger practical results. QZO comparable. |
| Addax (QhxjQOMdDF) | 6.00 | R2 | ZO + FO hybrid. Stronger theory and larger-scale experiments. QZO slightly below. |
| LQ-LoRA (xw29VvOMmU) | 6.75 | R2 | FO method, different paradigm. QZO below. |

**Bracket:** 5.5–6.0 after Round 1, confirmed by Round 2. QZO's core idea is more novel than SensZOQ (5.80) and HiZOO (5.67), but the two major weaknesses (flawed DDC proof, missing ZO-signSGD baselines) pull it down. It lands between Sparse MeZO (5.50, Reject) and HiZOO (5.67, Accept). I place it at **5.5** — the core idea merits acceptance after revision, but the current evaluation gaps (especially claiming advantages over ZO-signSGD methods without testing them, and presenting a flawed proof as theoretical evidence) prevent acceptance as-is.

---

## Summary
QZO enables fine-tuning of quantized LLMs using zeroth-order optimization by perturbing continuous quantization scales instead of discrete weights, combined with directional derivative clipping (DDC) for stability. The method achieves ~18× memory reduction vs. AdamW full fine-tuning and ~3× vs. MeZO, while maintaining competitive task performance across classification and QA benchmarks on three model families.

## Strengths
- **Q-SPSA solves a genuine technical barrier**: The core idea — perturbing continuous quantization scales Δ instead of discrete quantized weights θ̄ to enable ZO gradient estimation — is elegant and well-motivated. The decomposition θ → Δ ⊙ θ̄ (Section 3.2.1, Eqs. 3–5) cleanly separates continuous and discrete components, avoiding the precision-gap problem that prior ZO-for-quantized work (Feng et al., 2024; Zhou et al., 2025; Bar & Giryes, 2025) faces.
- **Substantial and well-measured memory reduction**: Table 1 and Figure 1 show QZO (4-bit) uses 4.8–6.3GB VRAM on 7B models vs. 14.8–20.4GB for MeZO (16-bit) and 26–32GB for fine-tuning. The method further enables 2-bit Llama-2-13B fine-tuning within a single 24GB RTX 4090 (5.78GB, Table 3).
- **DDC is empirically necessary and effective**: Figure 2 shows that without DDC, training collapses to NaN at step 22; with DDC, it remains stable across 1,000 steps. Figure 3 demonstrates robustness to clipping threshold C ≥ 75.
- **Competitive performance against 16-bit MeZO at 4× lower precision**: Across OPT-6.7B, Llama-2-7B, and Llama-3.1-8B on five NLP benchmarks (Table 1), 4-bit QZO performs on par with 16-bit MeZO, and on several settings outperforms it (e.g., Llama-2-7B on SST-2: QZO 90.0 vs MeZO 83.5; on SQuAD: QZO 85.5 vs MeZO 80.7).
- **Cross-paradigm quantization compatibility**: Works with both scalar-based GPTQ (4-bit, Table 1) and codebook-based AQLM (2-bit, Table 3). QZO lifts Llama-2-13B from 57.6% zero-shot to 80.5% on SST-2 under 2-bit compression.
- **Computational efficiency**: Table 2 shows QZO trains only ~5×10^7 parameters (~0.7% of full model) and uses substantially fewer FLOPs than MeZO.

## Weaknesses

### Fatal
None.

### Major
- **Missing ZO-signSGD baselines**: The paper explicitly positions QZO against ZO-signSGD methods (Feng et al., 2024; Zhou et al., 2025; Bar & Giryes, 2025) in Related Work (Section 2), claiming QZO is "inherently more efficient and flexible, as it does not require quantization of perturbation noises or re-quantization of model weights at each optimization iteration." These are the most directly comparable prior methods — they also combine ZO with quantized models — yet they are never included as experimental baselines. Without this comparison, the paper cannot substantiate its claimed advantages over the closest prior art.

- **Flawed theoretical justification for DDC's variance reduction**: The derivation in Eq. 8 attempting to prove Var[∇̂'] ≤ Var[∇̂] has genuine mathematical issues: (1) the variance definition used (E[||∇̂'||²] − E[||∇̂'||]²) is nonstandard and differs from the conventional definition (E[||∇̂'||²] − ||E[∇̂']||²); (2) the final step substitutes E[||∇̂||]² with (∇_Δ L)², which implicitly assumes equality in Jensen's inequality (E[||∇̂||] = ||E[∇̂]||) — this is unjustified and only holds in degenerate cases; (3) there is dimensional confusion in writing (∇_Δ L)² (a vector cannot be directly squared to a scalar). The paper claims "theoretical evidence" for variance reduction but the proof as presented does not hold. The empirical evidence (Figures 2–3) independently demonstrates DDC's effectiveness, but the paper overstates its theoretical contribution.

### Minor
- **Parameter-count confound in MeZO comparison**: QZO trains only ~5×10^7 scale parameters while MeZO trains ~6.7×10^9 full parameters. The FLOPs and part of the memory advantage therefore reflect training fewer parameters, not purely the scale-perturbation mechanism. The paper reports parameter counts transparently in Table 2, but a controlled ablation (MeZO applied to scale parameters only) would isolate the contribution of Q-SPSA's specific design.

- **Fine-tuning "upper bound" weakened by using SGD**: The full fine-tuning baseline uses SGD rather than AdamW (acknowledged in footnote 2 due to computational budget). AdamW is the standard for LLM fine-tuning and typically outperforms SGD. Furthermore, QZO occasionally exceeds this baseline (e.g., Llama-3.1-8B on SQuAD: QZO 88.3 vs. Fine-tuning 83.7), which undermines its reliability as a reference point.

- **No statistical significance reporting**: Test sets have only 1,000 examples (some SuperGLUE subsets are even smaller). Performance differences in Table 1 (often within a few points) could be explained by variance across seeds or data splits. Standard deviations are not reported.

- **Narrow task evaluation**: Experiments cover classification (SST-2, RTE, CB, BoolQ) and extractive QA (SQuAD), but no open-ended generation tasks. For LLM fine-tuning, generation quality is a critical dimension not assessed.

- **Fine-tuning step count unspecified**: The paper does not report how many steps or epochs the SGD fine-tuning baseline used, making computation budget comparisons impossible.

- **2-bit AQLM results are thin**: Table 3 reports only one model (Llama-2-13B) with no comparison beyond zero-shot. The Triton kernel modification for AQLM is mentioned but its correctness and overhead are not discussed.

### Trivial
- The 2-bit AQLM case falls back to standard SPSA for unquantized weights (line 98), partially weakening the purity of the scale-only approach for codebook-based methods. This is noted transparently and is a minor design observation.

## Nice-to-Haves
- An ablation where MeZO is applied to only the quantization scale parameters, to isolate whether Q-SPSA's perturbation mechanism provides benefits beyond simply training fewer parameters.
- Qualitative analysis of how learned scale parameters differ from original PTQ scales (e.g., do they grow, shrink, redistribute?).
- Extension to open-ended generation tasks to demonstrate broader applicability.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **QLoRA baseline missing**: The harsh critic argued QLoRA should be included as a baseline. REMOVED because: (a) QLoRA uses backpropagation through LoRA adapters, which is a fundamentally different paradigm from QZO's zeroth-order approach; (b) the asymmetry would favor QLoRA (backprop > ZO for accuracy), and per hard rules, criticisms about unfair comparisons where the asymmetry favors the baseline should be removed; (c) the paper's contribution is about enabling ZO for quantized models, not competing with all quantized fine-tuning methods. QLoRA comparison would be scope creep.
- **18× claim needs contextualization**: The harsh critic noted that 18× compares QZO (4-bit, ZO) against AdamW (16-bit, FSDP), stacking quantization + ZO + optimizer elimination savings. REMOVED — the paper explicitly states "compared to full-parameter fine-tuning in 16 bits" (abstract, line 9; Section 1, line 36), so the comparison basis is clear.
- **AQLM mechanism only sketched**: REMOVED — the paper clearly states "both the channel-wise scales and un-quantized weights are updated" (line 98), which is sufficient detail for the main text.
- **Missing DDC sensitivity analysis beyond C=150**: REMOVED — the paper addresses this: "When C is set to a value bigger than 150, the training becomes unstable and sometimes collapse" (lines 279-280). The studied range 0–150 is adequate.
- **Strength Finder — "DDC is theoretically motivated"**: The theoretical justification is flawed (see Major weakness). Retained the empirical necessity claim but dropped the theoretical motivation claim.
- **Generic strength claims removed**: "The paper addressed an important problem" and similar generic framing statements from the Strength Finder — these lack concrete, verifiable anchors in the paper.

## Novel Insights
The paper's decomposition of model parameters into θ = Δ ⊙ θ̄ and the insight that perturbing only Δ enables ZO on quantized models is genuinely novel. Prior ZO-for-quantized work required quantizing perturbation noise and re-quantizing weights at each step; QZO avoids both by exploiting the continuous/discrete separation inherent in the quantization formulation. The DDC method — clipping the estimated directional derivative before applying ZO-SGD — is a simple but practically effective stabilizer for ZO training on quantized models, with strong empirical evidence even though the theoretical proof needs revision.

## Suggestions
- Add experimental comparison against at least one ZO-signSGD baseline (e.g., Bar & Giryes, 2025) to substantiate the claimed advantages. This is the single highest-impact addition the paper needs.
- Either fix the DDC variance-reduction proof (correct the variance definition and justify the substitution properly) or reposition DDC as an empirically-motivated heuristic. The empirical evidence already makes a strong case independently.
- Report standard deviations across at least 3 random seeds for the main results in Table 1.
- Include a MeZO-on-scales-only ablation to disentangle parameter-count reduction from the Q-SPSA perturbation mechanism.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>