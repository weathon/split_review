Now let me search for calibration anchors.Initial bracket: 4.5 - 6.5. Let me narrow.## Summary
The paper proposes QZO, a zeroth-order optimization method that perturbs the *continuous quantization scales* of a frozen, post-training-quantized LLM rather than the discrete weights, plus a Directional Derivative Clipping (DDC) heuristic to stabilize training. Empirically, QZO fine-tunes 4-bit 7B-class models with ~3× lower memory than MeZO and enables 2-bit Llama-2-13B fine-tuning on a single 24 GB GPU, while remaining compatible with both scalar (GPTQ) and codebook (AQLM) PTQ.

## Strengths
- **Clean technical idea**: Perturbing the continuous quantization scale Δ while freezing discrete weights $\bar{\theta}$ (Eq. 5, Def. 3.3) is a genuinely simple resolution of the precision mismatch between ZO and quantized weights, and it works for both scalar (GPTQ) and codebook (AQLM) PTQ methods.
- **Real memory reduction vs the closest competitor (MeZO)**: Table 1 shows ~3× less peak VRAM than MeZO across OPT-6.7B, Llama-2-7B, and Llama-3-8B (e.g., 14.8 → 5.0 GB on Llama-2-7B), and Table 3 fits 2-bit Llama-2-13B fine-tuning in 5.78 GB — a genuinely useful operating point.
- **Computation efficiency**: Table 2 shows QZO uses ~1% of the trainable parameters and orders of magnitude fewer FLOPs than MeZO on SST-2, which is a non-trivial side effect of restricting updates to scales.
- **DDC is empirically supported**: Figure 2 shows training collapses to NaN at step 22 without DDC and remains stable with it; Figure 3 shows the method is reasonably robust to C across roughly 75–125. The empirical claim that clipping stabilizes ZO over scales is well-supported.

## Weaknesses

### Fatal
None — no single issue verifiably invalidates the core empirical contribution as stated.

### Major
- **Theorem 1's unbiasedness claim is dubious, and Eq. 8 leans on it.** Theorem 1 (Sec. 3.2.2) states that the *clipped* estimator $\hat\nabla'_\Delta\mathcal{L}=d'\cdot z$ with $d'=\mathrm{clip}(d,-C,C)$ is an unbiased estimate of $\nabla_\Delta\mathcal{L}$. For small $\epsilon$, $d\approx z^\top\nabla_\Delta\mathcal{L}$, and clipping a non-linear scalar function of $z$ generically biases $\mathbb{E}[d'z]$ relative to $\nabla\mathcal{L}$ whenever the threshold ever fires; the claim can only be tight in the degenerate case $C\to\infty$. The variance derivation in Eq. 8 then substitutes $\mathbb{E}[\|\hat\nabla'\|]=\nabla\mathcal{L}$ via Theorem 1 to obtain $\mathrm{Var}[\hat\nabla']\le\mathrm{Var}[\hat\nabla]$. Without that substitution the inequality does not directly follow. An honest "DDC trades a small bias for a larger second-moment reduction" framing would match what is actually happening; the unbiasedness claim, which is doing real work in the analysis, is on shaky ground. Why it matters: the paper's "theoretical evidence" for DDC is the only formal scaffolding around the method's stability claim.
- **The paper names the most relevant baselines and then does not run them.** The Related Work explicitly cites ZO-signSGD (Liu et al., 2019), ZOQO (Bar & Giryes, 2025), Feng et al. (2024), and Zhou et al. (2025) as prior work combining ZO with quantized models, and claims QZO is "inherently more efficient and flexible." None of these appear in Tables 1–3. Similarly, QLoRA — the dominant approach for memory-efficient fine-tuning of quantized LLMs — is cited but never compared. Without head-to-head comparisons in the same memory/data regime, the paper's specific claim of superiority over these methods is unsupported by the evidence presented.
- **Framing of the contribution and the "18× memory reduction" headline conflate distinct savings.** Table 2 makes clear QZO trains ~$5\times10^7$ parameters — about 0.7% of a 7B model — i.e., the quantization scales only. The title/abstract read as "fine-tuning quantized neural networks," but the actual method is *zeroth-order tuning of per-group scale parameters of a frozen quantized model*, which is a particular form of PEFT. Relatedly, the 18× headline comparison (Fig. 1) folds together AdamW→SGD (optimizer-state elimination), all→1% params (PEFT), backprop→ZO (no activation cache), and bf16→int4 (quantization), and only the last two are this paper's contribution. The contribution that isolates QZO's method — the comparison to MeZO — is ~3× (still meaningful), not 18×. Why it matters: this affects both the natural comparison class (PEFT methods, not full FT) and the strength of the claim.

### Minor
- **The "on par with MeZO" claim glosses over real gaps on some datasets.** On Llama-3-8B, MeZO substantially beats QZO on CB (91.1 vs 69.6) and BoolQ (83.4 vs 78.2). These are sizable margins on small test sets that the discussion does not engage with directly.
- **Fine-tuning upper bound uses SGD instead of AdamW** (footnote 2). This weakens the "upper bound" against which gap-to-FT is reported.
- **The 2-bit setup is not pure scale-tuning.** Sec. 4.1 states that for AQLM the "un-quantized parts are jointly fine-tuned using the regular SPSA and ZO-SGD." So the 2-bit result is QZO + standard ZO over un-quantized components — worth flagging since the section is presented as evidence that QZO works under extreme quantization.
- **Algorithm 1 clamps $\Delta_i\leftarrow\max(\Delta_i-\eta_t d'z,0)$** to keep scales non-negative — an additional non-linearity ignored by the variance analysis. Likely small effect, but it compounds the Theorem 1 concern.
- **Robustness to $C$ is narrower than implied.** Fig. 3 shows accuracy collapses to zero-shot at $C=0$ and degrades by $C\ge150$; the "robust" plateau is roughly 75–125. The paper itself reports this honestly, but the take-home in the text overstates it slightly.
- **No standard deviations** in Tables 1 and 3 despite small (1k) test sets and sensitive datasets like RTE/CB; even one extra seed would harden the comparisons.

### Trivial
- The motivation for *why* tuning only scales should be sufficient is not analyzed — the paper has the setup to answer this (scale-only first-order baseline would isolate "scale-only" from "ZO"), but does not.

## Nice-to-Haves
- A scale-only first-order (backprop) control to disentangle the "scale-only" restriction from the "ZO" estimator.
- Even one apples-to-apples comparison against QLoRA (matching memory budget) and against one of the named prior ZO+quantization methods.
- Replace Theorem 1's unbiasedness claim with a truncated-mean style result that explicitly characterizes bias as a function of $\Pr(|d|>C)$ and variance reduction via the truncated second moment.
- Multi-seed numbers with standard deviations on RTE/CB.
- Reframe the headline number as ~3× over MeZO with the 18× decomposed.

## Removed Points
These points are flagged to be removed; treat them with caution.
- "QZO is best understood as just PEFT and shouldn't be called 'fine-tuning quantized neural networks'" — kept as a Major framing issue but the harsher framing ("not even a fine-tuning paper") is too strong; the paper is transparent in Sec. 3.2.1 and Table 2 that scales are what is updated.
- Reproducibility/availability concerns about cited entities (none were raised, but per rules they would be removed regardless).
- Generic "evaluation lacks rigor" sweeps without a specific anchor.
- Strength: "QZO has a variance-reduction *guarantee* via Theorem 1" — removed because it conflicts with the verified Major weakness about Theorem 1; the empirical Figure 2 evidence is retained as a strength, the theoretical "guarantee" framing is not.

## Novel Insights
None beyond the paper's own contributions. The core observation — that quantization scales are continuous and therefore ZO-friendly, while the integer codes can stay frozen — is the paper's own insight and is genuinely the clean part of the work.

## Suggestions
- Run at least one comparison to QLoRA at matched memory and one to a representative prior ZO+quantization method (e.g., ZOQO) on the same five datasets and the same models.
- Rewrite Theorem 1 as a bias-variance trade-off statement; report empirically the truncation probability $\Pr(|d|>C)$ at chosen $C$.
- Add a first-order, scale-only baseline (backprop into scales only) to isolate the contribution of restricting to scales from the contribution of using ZO.
- Re-anchor the memory comparison around MeZO (~3×) and present the 18× as a decomposed bar with each source of savings attributed.
- Add at least 2-seed results with standard deviations on RTE and CB, and discuss the Llama-3-8B CB/BoolQ gaps with MeZO directly.

## Axis-by-axis evaluation
- **Originality**: Moderate. The core "perturb scales not weights" trick is clean and, as far as the paper's own related work shows, not done in this exact form by prior ZO+quantization methods.
- **Importance**: Real. Fitting 2-bit 13B fine-tuning into 24 GB is practically useful; on-device personalization is a credible application.
- **Claim support**: Partial. Memory and feasibility claims are well supported; the unbiasedness/variance-reduction theoretical claim is not; the headline 18× framing oversells what is isolated to QZO; "on par with MeZO" elides real gaps.
- **Soundness of experiments**: Adequate but uneven. Tables are clean but lack seed variance, omit the most directly cited competitors, and the FT upper bound uses SGD.
- **Clarity**: Generally clear. The method section is readable; the framing of what is trained could be more upfront.
- **Value**: Worth publishing in some form once the theorem is fixed and the named baselines are run; not yet acceptable as is.

## Score and Decision

### Calibration anchors retrieved
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/6Mdvq0bPyG.md` (avg 3.00, R1) — EfficientQAT, weaker bracketing anchor for the low band; QZO is clearly stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/vw0NurJ7UX.md` (avg 3.00, R1) — PrefixQuant; QZO is stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/0T8vCKa7yu.md` (avg 3.00, R1) — CVXQ; QZO is stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/1MHgMGoqsH.md` (avg 3.00, R1) — MPC paper; less topical.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/myYzr50xBh.md` (avg 5.80, R1, read in full) — **SensZOQ**, the closest topical match (ZO + quantization for on-device LLM FT). Comparable in quality: similar "combine existing pieces" critique, similar memory-comparison concerns. Accept at 5.80.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/vqJZb9SX1T.md` (avg 4.00, R1) — layer-wise sparse ZO; QZO has stronger empirical demonstration.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/9BiVepgmWW.md` (avg 7.00, R1) — LOZO; cleaner theoretical contribution than QZO and no analogous theorem error; QZO is weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/FK6T0U4Mg1.md` (avg 4.25, R1) — SubZero; QZO arguably stronger empirically (broader compatibility).
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/zcx6rIMbbR.md` (avg 5.40, R1, read in full) — Three-Stage quantized LLM FT; QZO is comparable, perhaps slightly cleaner narrative but worse theoretical scaffolding.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/eW4yh6HKz4.md` (avg 7.60, R1) — CBQ; substantially more thorough work; QZO is weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/wg1PCg3CUP.md` (avg 8.00, R1) — Scaling Laws for Precision; different scope, QZO much weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/E4Fk3YuG56.md` (avg 8.50, R1) — Cut Cross-Entropy; QZO far weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/TJo6aQb7mK.md` (avg 7.60, R1) — Spectra ternary LMs; different scope.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/WvFoJccpo8.md` (avg 6.33, R2, read in full) — QA-LoRA; cleaner contribution, cleaner ablations, no broken theorem; QZO is weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/rBzvEEbrF7.md` (avg 5.00, R2) — Q-GaLore; similar magnitude of contribution; comparable.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/aJnKjvTtPq.md` (avg 5.00, R2) — LoQA; comparable magnitude.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/AfhNyr73Ma.md` (avg 7.00, R2) — General Stability for ZO; theoretical work, less directly comparable.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/N8tJmhCw25.md` (avg 6.00, R2) — STP convergence; less directly comparable.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/BV1PHbTJzd.md` (avg 7.00, R2) — distributed stochastic optimization; less directly comparable.

### Round-1 bracket
Initial bracket: **4.5 – 6.5**, anchored by SensZOQ (5.80 Accept) above and SubZero/Three-Stage (4.25–5.40 Reject) below.

### Round-2 narrowing
Within that bracket, QZO is closer in spirit to SensZOQ (similar topic, similar combine-existing-pieces critique) than to the more polished QA-LoRA at 6.33. However, QZO carries the additional substantive concerns of (a) a theorem that does real work in the analysis but is mathematically dubious, (b) explicit prior baselines named in its own related work that are not run, and (c) headline framing that conflates contributions. These pull it below the 5.80 SensZOQ anchor and roughly even with Q-GaLore (5.00) and LoQA (5.00), but above Three-Stage (5.40 Reject — note: Reject despite 5.40 here) is a closer call. On balance the paper sits slightly below the SensZOQ accept anchor and slightly above the SubZero reject anchor.

Final placement: **5.0**, just below the accept threshold of this corpus. The contribution is real and the empirical work is competent, but the structural issues (theorem, missing comparisons to the paper's own named prior work, conflated headline) make it not yet ready in current form.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>