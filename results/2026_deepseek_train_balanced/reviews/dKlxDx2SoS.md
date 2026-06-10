Now let me produce the final review.

## Summary

The paper proposes QNet, a quaternion-based multimodal fusion approach for prompt learning with CLIP. Image and text features are combined via element-wise addition and processed through a quaternion encoder layer, whose orthogonal imaginary axes are claimed to disentangle complex multimodal distributions. The resulting quaternion-valued features are used to construct prompts for both vision and language branches. Experiments across 11 datasets show modest but consistent improvements over MaPLe with ~17.7% fewer parameters (2.93M vs 3.56M).

## Strengths

- **Parameter efficiency with consistent gains**: QNet achieves a higher harmonic mean (79.30% vs. 78.55%) than MaPLe with substantially fewer learnable parameters across 11 datasets (Section 4.2). This is a concrete and measurable efficiency improvement.

- **Single-layer ablation isolates fusion quality from depth advantages**: When all methods are restricted to one prompt layer (Table 4), QNet significantly outperforms both Co-CoOp and MaPLe, while MaPLe's base accuracy drops below Co-CoOp's. The paper correctly interprets this (Section 4.5, line 223): MaPLe's gains are largely driven by deep prompting, not inherently better fusion. This provides evidence that QNet's fusion mechanism itself drives improvement.

- **Systematic ablation of quaternion axis design choices**: Tables 5 and 6 empirically validate the architectural intuition by showing that (a) adding the real axis degrades performance, (b) more imaginary axes improve novel-class accuracy, and (c) using the k-axis as a modulation axis is more effective than as a parameter axis. These controlled experiments support the claimed role of the imaginary axes.

## Weaknesses

### Fatal
None.

### Major

1. **Method underspecification prevents reproduction (most important issue).** The quaternion encoder `Q_ua(·)` is described as a "quaternion dense layer" (line 69), but the paper omits critical architectural details: the number of layers, hidden dimensions, and activation functions. The "Meta-Proj" module (line 82) is named but never defined — yet it transforms image features before fusion. While the quaternion algebra implementation is attributed to Gaudet & Maida (2018), the specific architecture choices for QNet are absent. A reader cannot reproduce the method from the paper as written. This must be resolved.

2. **Comparison asymmetry in cross-dataset evaluation.** In the cross-dataset setting (Section 4.3, line 193), MaPLe uses a prompt depth of 3 while QNet uses only 2 layers. This makes the comparison non-apples-to-apples — the advantage could arise from architectural differences rather than quaternion fusion itself. Controlled comparisons at matched prompt depths are needed.

3. **Conceptual claims about quaternion algebra are metaphorical, not mathematically grounded.** The paper repeatedly claims that orthogonal imaginary axes "disentangle complex feature distributions" and "capture complementary information." However, the actual computation produces Q = x_i + y_j (line 72) — a quaternion with only two nonzero components — with the real axis serving as a vaguely defined "energy axis" and the k-axis receiving no input assignment. How this specific structure provides disentanglement beyond a comparably-sized real-valued dense layer is asserted through metaphor, not derived or analyzed. The claimed benefit lacks mathematical justification.

4. **Strong claims disproportionate to evidence.** The paper describes results as "exceptional" (line 17), "significant margin" (line 19), and "fundamentally addresses" (line 186). Actual improvements over MaPLe are ~1.04% (base), ~0.51% (novel), and ~0.75% (HM) averaged across 11 datasets (Section 4.2). Domain generalization gains are 0.2–1 percentage points (Section 4.4). The language should be calibrated to match the effect size.

### Minor

1. **Ablation studies on only one dataset (Caltech).** The ablations on axis design (Tables 5–6), prompt depth (Figure 3), and single-layer restrictions are all performed only on Caltech. Generalizability of these findings to other datasets (especially fine-grained ones) is uncertain.

2. **k_m/k_p distinction introduced post-hoc without definition.** The ablation discussion (line 225) introduces k_m (modulation axis) and k_p (parameter axis) subscripts, but these are not defined in the methodology section. They appear to be ad-hoc labels created to describe ablation results.

3. **Fusion mechanism framing is overstated.** The paper claims QNet "circumvents the necessity of crafting explicit interaction architectures" (line 14, Section 3.2.5). Yet the fusion pipeline begins with F_multi = F_image + F_text (element-wise addition), which is itself a simple interaction structure. The paper replaces complex interactions (cross-attention) with a simpler one, not eliminate interaction structures entirely. This framing should be corrected.

### Trivial

- The paper cites "ChatGPT (Radford et al., 2019)" (line 10), but Radford et al., 2019 describes GPT-2, not ChatGPT. Minor citation inaccuracy.
- Equation (97) uses notation that is difficult to parse (e.g., `w = |w|e^{q_multi^q} = φ q_multi^q`). The mathematical content of the weight initialization needs clarification.

## Nice-to-Haves

- Per-dataset breakdowns from the embedded tables could be reproduced in the main text for easier reading.
- Confidence intervals or error bars on main results would help assess variability in the 3-run setup.

## Removed Points

- "No code is released for verification": The paper explicitly provides a repository URL (line 4). Per hard rules, questioning the availability of cited resources is disallowed.
- "No statistical significance testing": Not standard practice in this prompt learning literature; demoted to nice-to-have.
- The critic's characterization of the underspecification as "fatal" and rendering the paper "not a valid contribution": The underspecification is a real and significant problem, but it is addressable in revision (adding architectural details) and does not invalidate the core contribution or empirical results.
- "Hierarchical feature mechanism is unexplained": The paper describes using QNet at multiple CLIP layers, which is a reasonable interpretation of utilizing hierarchical features across layers. This criticism was removed.
- "Theoretical proofs missing": Soft rule applied — demanding theoretical proofs for an empirical systems paper is scope creep.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Provide complete architectural specifications for Q_ua(·) (number of layers, hidden dimensions, activation functions) and Meta-Proj.
2. Run the cross-dataset comparison with matched prompt depths to eliminate the confound.
3. Calibrate the claims to match the effect size — "modest but consistent improvement" rather than "exceptional" or "fundamentally addresses."
4. Clarify the mathematical relationship between the specific quaternion computation (Q = x_i + y_j with learned k-axis weights) and the claimed disentanglement benefit.
5. Extend ablation studies to at least one additional dataset beyond Caltech.
6. Provide per-dataset tabular results in the main text rather than only in embedded images.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>