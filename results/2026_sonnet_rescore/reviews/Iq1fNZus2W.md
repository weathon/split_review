## Summary
The paper proposes Patch-wise and Keyword-Aware Attention (PKA), an efficient attention framework for multi-condition control in Diffusion Transformers (DiTs). It introduces two specialized modules — Position-Aligned Attention (PAA) for spatial conditions and Keyword-Scoped Attention (KSA) for subject-driven conditions — that exploit observed structural sparsity in attention patterns to reduce the quadratic cost of the "concatenate-and-attend" paradigm. Complemented by an early-timestep sampling strategy and a condition caching mechanism, PKA achieves up to a 10× inference speedup and 5.12× VRAM reduction at 16 conditions compared to full-attention baselines, with quantitative results on three 2-condition tasks suggesting competitive or better generative quality.

---

## Strengths

- **Empirically grounded motivation for sparse attention.** Figure 2 demonstrates that spatial-condition attention matrices are nearly diagonal (strong activation only along aligned positions), and Figure 3 shows subject-driven cross-attention activates only on keyword-relevant image regions. These figures directly quantify the computational waste that PAA and KSA eliminate, providing principled justification rather than heuristic motivation.

- **PAA reduces spatial-condition attention from O(N²) to O(N) via a principled one-to-one correspondence.** Equation 2 and Figure 4(c) formalize the per-position independent attention, and Figure 9 confirms the efficiency gain: PAA reduces latency from 15.38s to 13.63s and VRAM from 308MB to 237MB vs. full attention, outperforming even the most efficient Sliding Window Attention variant (14.00s / 276MB), with visually indistinguishable output quality.

- **KSA provides a tunable efficiency–quality tradeoff backed by ablation.** Figure 10 shows that raising threshold ε from 0 to 0.4 reduces latency from 16.99s to 15.26s and VRAM from 368MB to 242MB, while fine subject details remain highly faithful; only subtle rendering differences appear at aggressive thresholds.

- **Early-timestep sampling insight is well-supported and novel.** Figure 5's perturbation analysis cleanly shows that visual condition influence is front-loaded: the "High-to-Low" SSIM curve drops steeply within the first few perturbation steps while "Low-to-High" remains flat until later steps. This directly motivates using Logit-N(μ>0, δ>1) sampling, and Figure 11 confirms accelerated convergence and better control fidelity compared to standard (μ=0) and late-biased (μ<0) baselines.

- **Strong scalability evidence for the core efficiency claim.** Figures 7 and 8 demonstrate that PKA's latency and VRAM remain near-flat as conditions scale from 1 to 16, whereas UniCombine grows steeply (reaching >175s and >2000MB at 16 conditions). The speedup factors (3.90×–10× latency, 2.46×–5.12× VRAM) are clearly presented and independently compelling.

---

## Weaknesses

### Fatal
None.

### Major

- **Quality comparison conflates attention mechanism with training regime.** Table 1 compares PKA (LoRA fine-tuned on a curated Subject200K subset) against OminiControl2 and UniCombine, which were trained on different data with different regimes. The test set is drawn from the same curated Subject200K subset used to train PKA. There is no within-system ablation — i.e., training the identical model with full attention vs. PKA on the same data — that would isolate whether quality differences in Table 1 stem from the attention mechanism, the training data curation, or the LoRA optimization choice. As submitted, it is impossible to determine whether the FID/SSIM/CLIP-I/DINOv2 improvements are attributable to PKA or to favorable distributional alignment. This is the central evidential gap for the quality half of the joint claim.

- **Headline efficiency numbers apply to a setting not used in any quality evaluation.** The abstract and introduction lead with "up to 10× speedup and 5.12× VRAM reduction," measured at 16 conditions. All quality experiments in Table 1 use exactly 2 conditions. From Figure 7, at 2 conditions the PKA line and the baselines appear very close (speedup is not labeled for that point). The paper never reports the efficiency gain in the 2-condition setting where quality was actually measured, preventing readers from evaluating the efficiency–quality tradeoff in a unified picture. The current presentation implies the efficiency and quality results belong to the same setting, which they do not.

- **Substantial Canny controllability gap is minimized without explanation.** Table 1 (Subject-Canny row) reports PKA F1 = 0.414 versus UniCombine F1 = 0.551 — a ~25% relative gap on the primary controllability metric for that task. Section 4.2.3 characterizes this as "a minor exception of a narrow margin." This characterization is factually incorrect; a 25% relative controllability gap is not narrow. The paper never investigates whether PAA, KSA, their interaction, or training data characteristics are responsible for this deficit. Given that KSA is explicitly motivated by improving subject-driven control fidelity, a corresponding spatial controllability loss deserves a mechanistic explanation rather than a euphemistic dismissal.

### Minor

- **Ablation studies report only efficiency metrics, not quantitative quality metrics.** Figures 9 (PAA ablation) and 10 (KSA ablation) report latency and VRAM side-by-side with visual examples but include no quantitative quality scores (FID, SSIM, F1, etc.). The visual examples are helpful but insufficient to confirm that PAA and KSA individually preserve quality. A single quantitative quality row in each ablation table would substantially strengthen the per-module analysis.

- **Condition Cache's independent contribution to the speedup is not decomposed.** Figure 4(a) and Section 3.2 introduce the KV caching of condition tokens as part of the PKA framework. However, the latency/VRAM numbers in Figures 7 and 8 reflect the combined effect of caching, PAA, and KSA together. Whether the headline speedup is primarily from the structural attention change or from caching alone is not reported, making it difficult to assess the marginal value of PAA and KSA's algorithmic innovations.

- **Early-timestep sampling ablation is qualitative only.** Figure 11 demonstrates μ=0.5, δ=1.5 vs. μ=−0.5 alternatives qualitatively, but there is no quantitative ablation of this component in Table 1, and the chosen (μ, δ) values are not optimized or compared to intermediate settings. The perturbation analysis in Figure 5 tests single-condition influence; generalization to multi-condition training is assumed rather than verified.

### Trivial
None beyond what is noted above.

---

## Nice-to-Haves

- **Report efficiency numbers at 2 conditions.** Adding a "for our 2-condition evaluation setting, PKA reduces latency from X to Y seconds relative to UniCombine" would let readers directly compare the efficiency-quality tradeoff rather than extrapolating from Figure 7.
- **Characterize PAA's failure boundary.** A brief discussion or a few examples of conditions where the diagonal-alignment assumption may break down (e.g., at resolution mismatch, or for conditions with non-local structure) would better scope PAA's applicability.
- **Discuss KSA's limitation with free-form prompts.** The paper acknowledges that dataset curation ensures prompts contain keywords, but does not discuss what happens when KSA is applied to arbitrary prompts lacking clear keyword tokens. Even a brief limitation note would be valuable.

---

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: "PAA O(N) claim requires exact spatial alignment — unaddressed resolution mismatch."** The paper explicitly states PAA operates at the same spatial coordinates between patchified noisy image and condition tokens (Eq. 2, Figure 4(c)). For standard equal-resolution inputs (the normal case for edge/depth maps of matching resolution), this is fully valid. The concern about resolution mismatch is a speculative edge case not evidenced in the experiments, and the formulation is mathematically correct for the described setting. Demoted to a nice-to-have at most; removed from weaknesses.

- **Harsh critic: "Attention sparsity observations are not surprising."** While the diagonal structure of spatial attention follows intuitively, the paper's value is providing empirical quantification that justifies an O(N) redesign — not claiming the insight is novel. This is a qualitative critique with no bearing on correctness; removed.

- **Harsh critic: "KSA efficiency gains are modest (10% latency reduction)."** Figure 10 shows a real ~10% latency and ~34% VRAM reduction at ε=0.2. These are genuine gains; characterizing them as too small without a threshold criterion is a generic complaint. Removed.

- **Strength finder: "Table 1 comprehensively confirms state-of-the-art quality."** This is partially contested by the major weakness regarding training regime confounding and the Canny controllability gap. Retained in modified form in the strengths above, with qualification.

- **Strength finder: "Addressing an important problem" (generic statement).** Removed per filtering rules for non-specific strengths.

---

## Novel Insights

The perturbation analysis in Figure 5 is the most genuinely novel insight beyond the method itself: by separately measuring "high-to-low" vs. "low-to-high" progressive perturbation of a visual condition over the denoising trajectory, the authors provide a clean empirical proof that visual conditioning influence is concentrated in early (high-noise) timesteps. This observation — distinct from prior timestep analysis focused on image quality — directly motivates a principled change to the training sampling distribution and has implications beyond this paper: any fine-tuning of DiTs for visual conditional control could benefit from this bias. The PAA design (one-to-one spatial correspondence reducing O(N²) → O(N)) is a principled, clean reformulation that, while conceptually straightforward, makes explicit an approximation that was implicitly valid and previously unexploited.

---

## Suggestions

1. **Add a within-system quality ablation.** Train a single FLUX.1 LoRA on the same curated Subject200K subset with identical hyperparameters, varying only whether attention uses full attention or PKA. Even a partial subset (1K iterations) would provide the missing evidence that quality differences in Table 1 stem from the mechanism rather than training factors.
2. **Report 2-condition efficiency numbers.** Add a table or sentence quantifying latency and VRAM for the 2-condition case that matches the quality evaluation setup.
3. **Honestly address the Subject-Canny F1 gap.** Section 4.2.3 should quantify the gap (0.414 vs. 0.551) and discuss which module(s) may be responsible. A focused ablation — e.g., Subject-Canny with and without KSA — could localize the issue.
4. **Add quantitative quality rows to ablation figures.** Even a single metric (F1 for PAA, CLIP-I for KSA) in Figures 9 and 10 would replace visual-only evidence with quantitative confirmation of quality preservation per module.
5. **Decompose caching vs. attention structure in the efficiency results.** A version of Figure 7 that isolates the contribution of KV caching from PAA+KSA would clarify the value of each component.

---

## Score and Decision

**Originality:** The PAA and KSA designs are clean and principled; the early-timestep sampling insight is genuinely novel. The overall approach is incremental relative to attention sparsity literature but applies it distinctively to the multi-condition DiT setting. Solid but not transformative. (3/5)

**Importance of research question:** Multi-condition DiT control is practically important and the quadratic attention bottleneck is a real barrier to scalability. (4/5)

**Claims well supported:** Efficiency claims at high condition counts are well-supported. Quality claims are weakly supported due to training-regime confounding and the unexplained Canny controllability gap. (2/5)

**Soundness of experiments:** Ablation studies are present but incomplete (no quantitative quality metrics per module). The main comparison lacks a within-system ablation. The perturbation analysis is clean. (3/5)

**Clarity of writing:** Generally clear; the method is well-described with good figures. The dismissal of the Canny gap as "narrow" is the one notable presentation problem. (3/5)

**Value to the research community:** The efficiency results (especially the scalability to 16 conditions) and the early-timestep sampling insight are genuinely useful. The method is practical and the framework is extensible. (3/5)

The paper has real, principled contributions — especially PAA's O(N) spatial attention and the early-timestep sampling strategy — and the scalability results are compelling. However, the quality claims rest on a comparison that conflates training regime with attention design, the headline efficiency numbers are not paired with quality numbers in the same setting, and a substantial controllability gap is dismissed rather than analyzed. These issues together make the quality side of the paper's joint claim "efficiency without quality loss" untrustworthy as submitted.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>