Now I have all the information I need. Let me synthesize the final review.

## Summary
The paper proposes Pi-CCA, a replay-free continual learning method for vision-language models that preserves cross-modal alignment by storing a compact "certificate" of top-k canonical correlations and sketched subspaces, with spectral and subspace consistency losses plus a prompt-invariance term during adaptation.

## Strengths
1. **Principled geometry-first approach**: The paper explicitly recasts forgetting as alignment-geometry drift and directly preserves canonical spectrum and subspaces via losses L_spec and L_sub (Section 3.2–3.3), rather than regularizing proxy signals (similarities, logits, parameters) as in prior work. This is a clear conceptual contribution.

2. **Strong SOTA results across four benchmarks**: Tables 1 and 2 show PI-CCA achieves the best results among replay-free methods on MTIL, X-TAIL, VLCL, and ConStruct-VL, including surpassing the synthetic-replay method GIFT on VLCL without storing or generating data. Results include confidence intervals on VLCL/ConStruct-VL, supporting reproducibility.

3. **Replay-free, constant-memory consolidation**: The certificate stores only sketched h×k projectors (h ≪ d_v, d_t), updated via EMA without storing past data or using generative replay (Section 3.4). The Pareto analysis (Figure 2) shows a broad efficient frontier with peak memory <3 GB and step time <200 ms on A100.

4. **Thorough ablation and robustness analysis**: Table 3 systematically ablates each component, confirming both spectral and subspace terms are necessary. Figure 5 shows robustness across 20 random task orders (narrow IQRs). Figure 4 demonstrates prompt-invariance benefits under both ID and OOD templates.

## Weaknesses

### Fatal
None.

### Major
1. **Implausible correlation coefficients in Figure 3**: The figure caption reports Pearson r = 1.00 and Spearman ρ = 1.00 for two of four panels, and r = 0.99 / ρ = 1.00 for the other two. Perfect linear correlation (r = 1.00) across multiple hyperparameter sweeps (certificate size, EMAs, invariance strength, whitening, LoRA capacity/LR, sketch type — many degrees of freedom) is effectively impossible for real experimental data with measurement noise and stochastic optimization. The paper body text uses more measured language ("larger angle/spectral drifts generally imply larger drops"), but the figure values as reported are not credible. This does not invalidate the paper's core empirical claims (Tables 1–2, ablations), but it undermines the supporting causal analysis that geometry drift → performance drop and raises concerns about analysis rigor. The authors must provide raw data, multiple seeds, or an explanation for how r = 1.00 arises.

2. **Ambiguity in baseline comparison protocol**: The paper uses frozen backbones with LoRA adapters (line 64) but does not specify whether baselines (ZSCL, Mod-X, CTP, DKR, etc.) were re-implemented with the same LoRA configuration, use full fine-tuning, or use a different parameter-efficient setup. Methods like ZSCL and Mod-X were originally proposed with full fine-tuning. Uneven trainable parameter counts would affect forgetting dynamics and make the "state-of-the-art among replay-free methods" claim less precise. The paper also does not report per-method GPU memory and step time for the baselines used in the comparison, which would contextualize the efficiency claims. This is fixable but weakens the comparison as presented.

### Minor
1. **Inconsistent notation for text certificate**: The prompt-invariant text sketch is denoted as \(\bar{\mathbf{S}}_t^*\) in Eq. 4 but as \(\tilde{\mathbf{S}}_t^*\) in Eq. 13 (EMA update). This is a minor editing slip but suggests careless proofreading.

2. **Several method details deferred to appendix**: Differentiable SVD via block power iteration (number of iterations \(T_{\text{pow}}\), stability), perturbation types and strength definition for prompt invariance (Figure 4), and hyperparameter tables are all deferred to Appendix §A.1–§A.3. While acceptable for a 9-page paper, this limits in-line reproducibility for readers without immediate access to the appendix.

3. **Limited discussion of sketch dimension guarantees**: The sketch dimension \(h\) is introduced (Eq. 4) with mention of near-isometric embedding properties (Gaussian/SRHT), but no theoretical bound relating \(h\), \(k\), and the required embedding quality is provided in the main text. The empirical sweep (Figure 2) mitigates this, but a brief guarantee would strengthen the methodology.

### Trivial
- The notation \(\theta_v = (\theta_v, \phi_v)\) for the full parameter set (line 64) is confusing since the same symbol \(\theta_v\) is used for both the frozen parameters and the full set. This is a minor presentation issue.
- The caption for Figure 3 in the parsed text states all four panels have Spearman ρ = 1.00, but the top-right and bottom-right panels also show Spearman ρ = 1.00 despite Pearson being 0.99. If all data lies on a monotonic curve that is not perfectly linear, Spearman could be 1.00 while Pearson < 1.00, which is plausible — but this should be explained.

## Nice-to-Haves
- Adding standard deviations or confidence intervals to the MTIL/X-TAIL results in Table 1 (as is already done for VLCL/ConStruct-VL in Table 2) would strengthen the presentation.
- Including a controlled experiment where baselines are re-implemented with LoRA adapters of the same rank would remove any ambiguity about training protocol fairness.
- Reporting per-method trainable parameter counts and GPU memory footprint would substantiate the efficiency claims.

## Removed Points
These points are flagged to be removed, treat them with caution:
1. **Harsh critic's claim about "not truly invariant" / overclaim**: The critic notes the certificate is updated via EMA (Eq. 13) and says "prompt-invariant" is an overclaim. The paper explicitly uses "prompt-invariant" to describe the projector averaging mechanism (Section 3.2, Eq. 5–6) and the EMA update in Eq. 13 is clearly described. The term is justified by the averaging over perturbations, not by the EMA. This is a semantic nitpick removed because the paper's own framing is reasonable.
2. **Strength Finder's claimed "geometry → performance correlation evidence" as a strength**: Since the correlation coefficients are questionable (see Weakness Major #1), the correlation evidence cannot be uncritically listed as a strength. It is retained only as a methodological claim, not an established finding.
3. **Strength Finder's claim about "comprehensive ablation study"**: This is genuine and retained.
4. **Criticism about missing related work**: Removed per instructions.
5. **Nitpick about missing feature dimensionality**: The paper states \(d_v, d_t\) as general dimensions. This level of detail is adequate for the main text.
6. **Nitpick about hyperparameter settings not being in main paper**: These are standard to place in appendix; requesting them in the main text is scope creep.

## Novel Insights
None beyond the paper's own contributions — the reviews surface the Figure 3 correlation concern as the most critical issue but do not add conceptual novelty beyond what the paper itself presents.

## Suggestions
1. **Fix Figure 3**: Provide multiple seeds per configuration, show error bars, and report actual (non-rounded) Pearson/Spearman values. The trend itself (positive correlation between geometry drift and performance drop) is likely real and useful; the current presentation with r=1.00 undermines what would otherwise be clean supporting evidence.
2. **Clarify baseline implementation protocol**: Explicitly state whether each baseline uses full fine-tuning or LoRA, and ideally run a controlled comparison with uniform LoRA setup across methods.
3. **Fix the notation inconsistency** between \(\bar{\mathbf{S}}_t^*\) (Eq. 4) and \(\tilde{\mathbf{S}}_t^*\) (Eq. 13).

## Score and Decision

I bracket this paper as follows. Round 1 placed it between the weak anchors (avg 2.0–2.5) and strong anchors (8.0), with middle-band anchors at 3.8–6.5. Round 2 narrowed by reading C-CLIP (6.5, accepted), Proof (5.67, rejected), and the rehearsal-free CL paper (5.0, accepted). 

**Compared to C-CLIP (6.5)**: PI-CCA has a more principled and novel approach (geometry preservation vs. standard distillation/consolidation), stronger SOTA across more benchmarks, and more comprehensive analyses (Pareto, task-order, prompt invariance). However, C-CLIP does not have the Figure 3 credibility issue. PI-CCA is slightly weaker.

**Compared to Proof (5.67, rejected)**: PI-CCA has a clearer motivation, more thorough experiments, and stronger results. Proof's weaknesses (inference mismatch, representation drift) are more central to its method. PI-CCA is clearly stronger.

**Compared to rehearsal-free CL paper (5.0, accepted)**: PI-CCA has a more elegant approach and stronger evaluation. PI-CCA is clearly stronger.

The Figure 3 correlation issue is significant but not fatal — the paper's core empirical claims (SOTA results, component effectiveness via ablations) are independently established. The main effect is to reduce confidence in the causal analysis supporting the "why," not the "that." 

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>