Now I have all the information needed. Let me compose the final consolidated review.

## Summary

MotionDreamer proposes a localized generative masked transformer for one-to-many motion synthesis from a single reference motion. It introduces two technical contributions: (1) a codebook distribution regularization loss (L_token) that mitigates codebook collapse when training a VQ-VAE on a single sequence, and (2) a sliding window local attention mechanism (SlidAttn) with overlap fusion that captures local token dependencies and prevents the overfitting that global self-attention suffers on single sequences. The method is evaluated against GAN, diffusion, and non-parametric baselines on the new SinMotion dataset (60 sequences), with additional demonstrations on temporal editing, crowd animation, and beat-aligned dance synthesis.

## Strengths

- **Novel localized attention mechanism specifically designed for single-instance generation.** The SlidAttn layer with overlap fusion (AttnFuse) is a principled architectural choice: standard global self-attention overfits on a single sequence (Table 3 shows Global Diversity of only 0.09 for the standard transformer baseline), while SlidAttn dramatically improves diversity to 0.52 while maintaining coverage. AttnFuse further improves the harmonic mean from 0.370 (average pooling) to 0.447. The mechanism is well motivated for this problem setting.

- **Codebook distribution regularization that addresses a genuine problem with single-sequence VQ training.** The KL-divergence loss L_token encourages uniform codebook utilization, directly attacking the under-utilization issue that persists even when EMA and codebook reset are used. Table 2 shows VQ perplexity increases from 7.95 to 16.65 with L_token, and coverage improves from 0.79 to 0.84. Figure 5 provides qualitative confirmation that local motion patterns (e.g., "house dancing" window) are better preserved.

- **Thorough ablation studies that isolate each component's contribution.** The paper systematically ablates codebook regularization (Table 2, Figure 5), Local-M architecture (Table 3), and overlap attention fusion (Figure 6). Each ablation cleanly demonstrates that the proposed designs (SlidAttn, AttnFuse, differentiable dequantization, L_token) individually improve performance and are not redundant. This is a significant strength given how many papers present entangled ablations.

- **User study provides independent perceptual validation.** The 20-participant study (Figure 4) scores MotionDreamer highest on perceptual coverage and diversity, with naturalness comparable to the non-parametric GenMM baseline. This is arguably stronger evidence than the composite metric because it avoids aggregation issues and directly measures what practitioners care about.

- **Demonstrated applicability to downstream tasks.** The framework successfully performs temporal motion editing, crowd animation, and beat-aligned dance synthesis from a single reference (Figure 7), showing that the learned tokenization and generation framework generalizes beyond the basic unconditional synthesis setup.

## Weaknesses

### Fatal

None.

### Major

- **Ambiguous composite evaluation metric undermines the headline quantitative claim.** The paper's central quantitative claim—"improving the harmonic means by 19%" and "state-of-the-art comprehensive performance"—rests on a weighted harmonic mean that is not properly specified. The formula given (Section 4.1) is the standard *unweighted* harmonic mean (HE = H / Σ 1/x_i). The prose then states "we give the highest weight to metric (1) and lower weights to (2)–(5)," but no weighted formula is provided, and it is not explained how weights enter the computation (e.g., whether they affect the standardization step, the harmonic mean itself, or both). Without a reproducible procedure, the reported harmonic means in Tables 1 and 3 cannot be independently verified. This is especially problematic because individual metrics tell a more nuanced story: the paper acknowledges that GenMM achieves "higher coverage" (line 158), and other baselines may lead on certain diversity dimensions. The composite alone determines the overall ranking, and its construction is insufficiently transparent. The paper should either (a) provide a clear weighted formula, (b) use a standard aggregation (e.g., unweighted harmonic mean of ranks), or (c) rely on per-metric reporting with a transparent average.

- **Overclaiming on individual metrics.** The paper states "Our method achieves state-of-the-art results on individual metrices (1)–(5)" (line 158) while simultaneously acknowledging that GenMM "reaches higher coverage" (same paragraph). These statements are contradictory—if a baseline exceeds the proposed method on metric (1), the method is not SOTA on that metric. This overclaiming inflates the paper's achievements and should be corrected.

### Minor

- **Baseline hyperparameter tuning on SinMotion is not discussed.** The paper compares against Ganimator, SinMDM, and GenMM without indicating whether these baselines were re-tuned for the SinMotion dataset or if published default settings were used. Since SinMotion includes non-human skeletons (TrueboneZOO), some baselines may not have been designed for arbitrary topologies. This is a methodological gap that weakens the fairness of the comparison, though it is unlikely to reverse the overall conclusions given the user study support.

- **No reported reconstruction quality for the VQ tokenization.** Table 2 reports VQ perplexity and generation coverage, but never reports actual reconstruction error (e.g., L1 distance or MPJPE between the reference and the VQ reconstruction). Since codebook regularization trades off reconstruction fidelity for uniform usage, the absence of reconstruction numbers makes it impossible to judge whether L_token harms tokenization accuracy. This is a basic sanity check that should be reported.

- **No statistical significance or confidence intervals.** The quantitative comparisons (Tables 1–3) report point estimates without standard deviations, confidence intervals, or significance tests. Given that the SinMotion dataset contains only 60 sequences (30 long, 30 short), variance may be non-negligible. Reporting variability would substantially strengthen the quantitative claims.

- **Downstream applications are purely qualitative.** The temporal editing, crowd animation, and beat-aligned dance synthesis demonstrations (Section 4.5, Figure 7) lack any quantitative metrics (e.g., beat hit rate for dance, coverage/diversity for crowd). While these are framed as demonstrations rather than core experiments, quantitative evaluation for at least one downstream task (e.g., beat alignment on AIST++) would better substantiate the claim of practical applicability.

### Trivial

- **The user study uses only 3 reference motions and 20 participants.** This limits the generalizability of the perceptual findings, though the protocol itself is standard and the results are directionally clear.
- **Selection bias / documentation for SinMotion.** The paper does not discuss how the 30 Mixamo and 30 TrueboneZOO sequences were chosen, raising the possibility of selection bias. The dataset construction should be documented more transparently.

## Nice-to-Haves

- A Pareto-style plot of Coverage vs. Global Diversity (or a similar 2D visualization of the fidelity-diversity trade-off) would directly support the paper's narrative without needing a composite metric.
- Reporting reconstruction quality (L1/MPJPE) for the VQ-VAE with and without L_token would clarify whether the regularization comes at a fidelity cost.
- A simple control experiment showing that each baseline achieves comparable reconstruction quality on SinMotion as on its original test set would strengthen the SOTA claim.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Missing hyperparameters in the main text (window size W, stride S, number of layers, codebook size K, etc.).** The paper's main text defines the architecture conceptually (Section 3.2.1), and these numerical details are standard for the appendix, which the parser strips. This is not a genuine weakness in the original submission. (Rule: REMOVE weaknesses about missing appendix content.)
- **Criticism that the paper should clarify whether EMA/codebook reset are used in the ablation.** The paper states in Section 4.3 that L_token is "in addition to the commonly used strategies (EMA and codebook reset)" and compares "with vs. without L_token"—making it clear that EMA/reset are used in both conditions. The critic's concern is addressed.
- **Complaint that "prior methods 'fail to achieve diverse and natural synthesis' is a bit sweeping."** This is a generic stylistic critique of the introduction's framing, not a substantive weakness.
- **Strength Finder's claim that MotionDreamer achieves "the highest coverage (0.84)."** The paper itself acknowledges GenMM achieves higher quantitative coverage (line 158), so this strength is factually inaccurate. The method does achieve the best *harmonic mean* and best perceptual coverage in the user study, which should be stated instead.

## Novel Insights

The reviews surface an important tension: the paper's strongest quantitative evidence (the harmonic mean) is also its weakest link methodologically, yet the user study independently confirms the perceptual advantages. This suggests a more fundamental insight—evaluation of single-instance generation may be better served by perceptual studies and per-metric reporting than by composite aggregation formulas, especially when different methods lead on different individual metrics. The paper's ablation methodology (isolating each component across Tables 2 and 3) sets a good standard for this subfield and could be adopted more broadly.

## Suggestions

1. **Replace the ambiguous weighted harmonic mean** with a transparent aggregation: either an unweighted harmonic mean of metric ranks (which avoids scaling issues and weights naturally), or a simple average of standardized scores with clearly pre-specified weights. Better yet, present a 2D scatter plot of a fidelity metric vs. a diversity metric and let readers assess the trade-off visually.

2. **Correct the overclaim about SOTA on individual metrics** (line 158). The paper should report that it achieves the best *comprehensive* performance (harmonic mean) and competitive results on individual metrics, noting honestly where baselines lead.

3. **Report VQ reconstruction error** (L1/MPJPE) for the tokenizer with and without L_token, to demonstrate that codebook regularization does not degrade reconstruction fidelity.

4. **Add standard deviations or confidence intervals** to the quantitative results in Tables 1–3, and ideally report significance tests for the most important comparisons.

5. **Provide basic quantitative evaluation for at least one downstream application** (e.g., beat hit rate for beat-aligned dance synthesis on AIST++).

## Score and Decision

The paper makes a genuine contribution: the SlidAttn mechanism and codebook regularization are well-motivated, the ablations are thorough, and the user study provides independent perceptual validation. However, the evaluation protocol is marred by an ambiguously defined composite metric and a contradictory claim about individual metric SOTA. These issues are fixable—they do not invalidate the core technical contribution or the qualitative findings—but they prevent acceptance in the current form. The paper would be suitable after major revision that clarifies the evaluation protocol, corrects the overclaiming, and adds basic missing controls (reconstruction quality, variability estimates).

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>