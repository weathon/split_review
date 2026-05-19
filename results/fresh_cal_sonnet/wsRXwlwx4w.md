Now let me do the calibration search to anchor the score.**Round 1 bracket: 5.0–6.5.** CoPrompt is clearly above the weak-rejected anchors (score 2–3) and below the truly novel CLIP papers (score 8). The DeKg paper (5.75, accepted) is the most topically similar. Now narrowing within [5, 6.5].Now I have enough calibration data. Let me write the full review.

**Round 1 bracket:** 5.0–6.5  
**Round 2 anchors:** DeKg (5.75, accepted) is most topically similar; DeMul (6.40, accepted) has cleaner LLM contributions; OGEN (6.00, accepted) has more novel regularization; Patch-Level Prompting (5.20, rejected) has similar consistency-combo design. CoPrompt sits slightly below DeKg (5.75) due to a verifiable equation error, no variance reporting on sub-1% SOTA gains, and domain-gen underperformance inconsistent with headline claims.

---

## Summary

CoPrompt proposes a consistency-guided fine-tuning method for CLIP that enforces cosine similarity between a trainable model (multi-modal prompts + adapters) and the frozen pre-trained CLIP backbone, augmented by LLM-generated text perturbations and image augmentations. The method combines two established PEFT paradigms (MaPLe-style coupled prompting and CLIP-Adapter) under a consistency regularizer. Experiments across base-to-novel generalization (11 datasets), cross-dataset transfer, and domain generalization are reported, with the primary headline improvement being +0.51% HM and +1.13% novel accuracy over PromptSRC on the base-to-novel benchmark.

---

## Strengths

- **State-of-the-art base-to-novel generalization:** CoPrompt achieves 77.23% novel accuracy and 80.48% HM across 11 datasets (Table 1), surpassing PromptSRC (76.10%, 79.97%) on 8 of 11 individual datasets. The improvement is real and consistent across diverse domains.

- **Cross-dataset transfer leadership:** CoPrompt achieves 67.00% average on 10 target datasets (Table 2), outperforming MaPLe (66.30%) and PromptSRC (65.81%), with wins on 8 of 10 individual target datasets. The 1.19% margin over PromptSRC on this benchmark is more substantial than the base-to-novel margin.

- **Compelling ablation demonstrating the role of consistency for adapter integration:** The ablation (Table 4) shows that adding adapters *without* the consistency constraint actually hurts performance (78.45% vs. 78.55% baseline with neither), while adding adapters *with* the constraint reaches 80.48%. This is a genuine empirical insight — the consistency regularizer is what makes multi-modal adapters viable, contradicting CLIP-Adapter's finding that dual-branch adapters cause degradation.

- **Enables training more prompt layers without overfitting:** CoPrompt achieves best performance at all 12 encoder layers (80.48%, Table 7a), whereas MaPLe plateaued at 9 layers. This directly demonstrates the practical benefit of the consistency constraint in expanding the effective parameter budget.

---

## Weaknesses

### Fatal
None.

### Major

- **CE loss equation (Eq. 6) appears to use frozen CLIP embeddings, providing no gradient to learned parameters.** As written, Eq. 6 is: $\mathcal{L}_{ce} = -\log \frac{\exp(sim(z, w_y)/\tau)}{\sum_k \exp(sim(z,w_k)/\tau)}$, where the paper defines $z = \theta(x)$ (frozen image encoder) and $w_k = \phi(\text{template})$ (frozen text embeddings). Under this definition, neither the learned prompts nor the adapters receive any gradient from the classification loss — they would be trained solely by the consistency constraint. The actual implementation almost certainly uses $\theta(i)$ and $\phi^a(\phi(t_k))$ (the tunable model embeddings, as in Eq. 2/5), but as written this is a substantial error in the core training objective. A reader cannot verify what is actually being optimized from the paper as written.

- **Sub-1% improvements over PromptSRC with no statistical validation.** The primary SOTA claim rests on +0.51% HM and +1.13% novel accuracy over PromptSRC. The ablation components individually contribute 0.46% (adapters), 0.46–0.92% (input perturbation). In 16-shot few-shot settings, run-to-run variance can easily span 0.5–1%, yet no standard deviations, confidence intervals, or multi-seed results are reported. Without this, the evidential weight of sub-1% comparisons to PromptSRC cannot be established.

### Minor

- **Domain generalization underperforms PromptSRC, inconsistent with stated scope.** In Table 3, CoPrompt scores 60.42% vs. PromptSRC's 60.65%, trailing on all four individual ImageNet variants (ImNetV2: 64.25 vs. 64.35; ImNetS: 49.43 vs. 49.55; ImNetA: 50.50 vs. 50.90; ImNetR: 77.51 vs. 77.80). The paper correctly describes this as "comparable" in Section 4.3, but the Conclusion (Section 5) claims "surpassing the existing state-of-the-art by a significant margin" without qualification — an overclaim given this benchmark loss. The Conclusion should be narrowed to the two evaluation suites where CoPrompt genuinely leads.

- **EuroSAT λ sensitivity reveals a 7-point regression at the globally selected λ.** Table 4 (sensitivity study) shows EuroSAT achieves 85.84% at λ=0.1 but drops to 78.63% at λ=8 — the value used in all main experiments. The paper notes EuroSAT behaves differently but offers no mechanistic explanation, and does not discuss whether other datasets are also evaluated at their individual optima. This large per-dataset variability (vs. <1% elsewhere) warrants deeper treatment: it suggests the consistency constraint may be actively harmful on datasets far from ImageNet's pre-training distribution, which directly touches the paper's core generalization thesis.

### Trivial

- **Cosine vs. L1 differ by 0.08%** (80.48 vs. 80.40, Table 5b), yet the paper presents cosine distance as a meaningful design differentiator from PromptSRC in Section 3.2. The difference is negligible; the framing should be softened.

- **GPT-2 vs. GPT-3 differ by 0.02%** (80.46 vs. 80.48, Table 5c). These should not be reported as distinct experimental results — the difference is clearly within measurement noise and implies a precision the single-run experiment cannot support.

---

## Nice-to-Haves

- A 3-seed multi-run variance report on the main ablation table (Table 4) and the average HM comparison to PromptSRC would substantially increase the paper's credibility at minimal cost.
- A mechanistic analysis of why EuroSAT behaves oppositely to other datasets (distribution distance from ImageNet, texture-vs-semantics sensitivity) would sharpen the paper's understanding of *when* consistency regularization helps vs. hurts.
- Clarifying how training epochs compare across methods (PromptSRC vs. CoPrompt) in the main tables, given that CoPrompt at equal FLOPs achieves 80.01% vs. 80.48% at full training — this gap should be acknowledged in the main comparison discussion.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Conclusion's claim of surpassing by a significant margin invalidates the cross-dataset narrative."** Kept as a Minor weakness (domain gen) and Trivial (conclusion phrasing), but not elevated to Major because the body text correctly qualifies domain gen performance.
- **LLM text perturbation as "non-trivial external dependency."** The 0.39% gain from GPT-based text (vs. same template) is small, and the GPT-2 vs. GPT-3 gap is 0.02%. The harsh critic's framing as a "meaningful cost deserving honest discussion" is valid as a minor concern but has been merged into the Trivial section on GPT-2 vs. GPT-3 precision, and the 0.39% gain appears in the ablation and is not claimed as a headline contribution.
- **Reviewer request for CI/significance testing framed as a "missing part."** This is valid and retained as a Major weakness about evidential strength, but the demand for CI on *every* result is moved to Nice-to-Haves — the Major weakness focuses specifically on the headline PromptSRC comparison.
- **Computational budget comparison not fully disclosed.** The paper explicitly reports 2× FLOPs (Section 4.5) and includes an equal-budget comparison showing 80.01% vs. 80.48%. This is sufficient disclosure; the harsh reviewer's "concern" is therefore removed.
- **Cosine vs. L1 undermines the "key differentiator" framing.** Verified and kept as Trivial.
- **Criticism that "improvements are below noise floor without variance reporting"** — applicable as a Major (kept), but the specific claim that "some or all" ablation gains may wash out is speculative without evidence they don't hold. The Major weakness correctly flags the *evidential* gap without asserting the results are wrong.

---

## Novel Insights

The most interesting empirical finding—largely underdiscussed in the paper itself—is that adding adapters *without* consistency regularization hurts performance relative to the no-adapter baseline (78.45% vs. 78.55%), while adding adapters *with* the constraint improves performance by 1.93% over that same baseline. This is not merely "consistency helps"; it specifically implies that the consistency constraint changes the optimization landscape in a way that permits more tunable parameters to be beneficial rather than harmful in few-shot settings. The λ sensitivity table also contains a structurally important but underexplored counterexample: EuroSAT's 7-point degradation from λ=0.1 to λ=8 is an order of magnitude larger than any other variation, suggesting domain shift magnitude relative to CLIP's pre-training data governs whether consistency regularization is beneficial or harmful — a hypothesis the paper does not state.

---

## Suggestions

1. **Fix Equation 6** to use the tunable model embeddings $\theta(i)$ and $\phi^a(\phi(t_k))$ rather than the frozen CLIP embeddings $\theta(x)$ and $\phi(\text{template})$, and verify the full training pipeline is correctly described.
2. **Report mean ± std over 3 seeds** for the average HM comparison against PromptSRC and for each ablation row — this is the single change that would most credibly establish the contribution.
3. **Narrow the Conclusion** to avoid claiming "by a significant margin" across all three evaluation suites; domain generalization should be described as "comparable to" or "slightly below" PromptSRC.
4. **Analyze EuroSAT separately** in the sensitivity section: why does it peak at λ=0.1 while all others peak at λ=8? Connecting this to distribution distance from CLIP's ImageNet pre-training would strengthen the paper's theory of why consistency helps.
5. **Remove the GPT-2 vs. GPT-3 row** from Table 5c or reframe it explicitly as showing insensitivity to LLM quality (not a fine-grained performance comparison).

---

## Score and Decision

**Axis evaluation:**
- *Originality*: Moderate. Combining MaPLe-style coupled prompting, adapters, and cosine consistency regularization is a principled combination but not fundamentally new. The insight that consistency enables dual-branch adapters to work is the strongest novel finding.
- *Importance*: Reasonable. Few-shot PEFT for VLMs is an active and important problem.
- *Claims vs. support*: Partially weak. The primary headline numbers (+0.51% HM over PromptSRC) are credible but lack statistical validation, and domain generalization underperformance contradicts the broader claim.
- *Soundness*: Mostly sound, but the CE loss equation error (Eq. 6) is a real technical deficiency.
- *Clarity*: Generally clear and well-organized, with comprehensive ablations.
- *Value to community*: Moderate — the ablation insights are useful, but the incremental margin over PromptSRC limits impact.

**Anchor comparison:**
- Round 1 anchors: weak anchors at 2.5 (much weaker), strong anchors at 8.0 (much stronger). Bracket: 5–6.5.
- Round 2 anchors: DeKg (5.75, accepted) — most topically similar, slightly more novel HSIC constraint; DeMul (6.40, accepted) — cleaner LLM contribution; OGEN (6.00, accepted) — more novel but older baselines; Patch-Level Prompting (5.20, rejected) — similar consistency combo, rejected for complexity/novelty concerns.

CoPrompt is comparable to the DeKg anchor (5.75) but sits slightly below it: DeKg has a more theoretically-grounded contribution (HSIC, plug-and-play) while CoPrompt has a verified equation error and lacks statistical validation for its core SOTA comparisons. The domain generalization loss and overstated conclusion further pull it down. Compared to Patch-Level Prompting (5.20, rejected), CoPrompt is better organized and has cleaner contributions, warranting a higher score. Final score: **5.5**.

| Anchor | Score | Round | Comparison |
|---|---|---|---|
| j1FLTvgyAh (MVMP) | 2.50 | R1 | Much weaker — no consistent framework, simpler contributions |
| ZaudLwn0Hm (Prototypical evolution) | 2.50 | R1 | Much weaker — limited novelty, poor execution |
| dGMJ93qpfq (Patch-Level Prompting) | 5.20 | R1 | Somewhat weaker — rejected, more complex system, comparable consistency motivation |
| 6wOmHdwCC4 (DeKg) | 5.75 | R1 | Most similar; slightly better — more novel constraint (HSIC), plug-and-play, accepted |
| Rc3RP9OoEJ (InCPL) | 5.00 | R1 | Slightly weaker — different setting but similar tier |
| 4lqo5Jwfnq (CIL prompts) | 4.67 | R1 | Weaker and different domain |
| 1aF2D2CPHi (DFKD CLIP) | 8.00 | R1 | Much stronger — novel problem, data-free KD |
| 74vnDs1R97 (Visual Concepts) | 5.80 | R2 | Slightly better — broader analysis, accepted |
| SYnIf4LxAG (Cross-Modality Transfer) | 6.50 | R2 | Better — more novel cross-modality insight, accepted |
| 1L9vdc7BB5 (ADAPT) | 5.50 | R2 | Comparable tier — heterogeneous prompt lengths, rejected |
| dsiwLm8yjz (Prompt Reverse) | 5.00 | R2 | Slightly weaker |
| PKICZXVY9M (OGEN) | 6.00 | R2 | Slightly better — more novel contributions despite older baselines |
| 2JF8mJRJ7M (Lipsum-FT) | 5.75 | R2 | Comparable |
| NDLmZZWATc (DeMul) | 6.40 | R2 | Better — cleaner LLM contribution, stronger novelty |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>