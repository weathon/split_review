## Final Review

## Summary
DelRec introduces a method to learn per-neuron transmission delays in the recurrent connections of spiking neural networks using surrogate gradient learning. The key technique relaxes integer delays to real values during training via a differentiable triangular spread function whose width is annealed to zero, then rounds to integers for inference. A scheduling-matrix buffer efficiently handles future spike scheduling. The paper demonstrates new SOTA on SSC (82.58%) and PS-MNIST (96.21%) using only simple LIF neurons, and provides a controlled three-phase ablation study on SHD showing learned recurrent delays causally improve performance over baselines, particularly under low-parameter budgets.

## Strengths
- **Genuinely strong empirical results on SSC (Table 1)**: DelRec achieves 82.58% ± 0.08% on SSC using only LIF neurons with 0.37M parameters, outperforming all prior LIF-based models including ASRC-SNN (81.54%). This is achieved without data augmentation or normalization layers, making the contribution of the recurrent delay mechanism clear rather than confounded by auxiliary tricks.
- **Well-designed three-phase ablation study on SHD (Section 3.2, Figure 3)**: The systematic comparison of six configurations (vanilla SNN, vanilla RSNN, fixed random recurrent delays, learned FF delays, learned recurrent delays, both) under matched parameter budgets provides convincing causal evidence. The finding that even fixed random recurrent delays (~78%) dramatically outperform a vanilla RSNN (~40%) in Fig. 3B provides direct support for the gradient-propagation motivation.
- **Rigorous benchmarking practices**: The paper separates LIF-based models from complex-neuron architectures in the main comparison table while transparently disclosing higher results in a footnote (line 162). On SHD, it correctly identifies the historical flaw of test-only evaluation, adopts a proper validation split, reports 10 seeds, and acknowledges that differences above ~93% are not statistically significant given the small test set.
- **Clean and practical method design**: The triangular spread function with annealed sigma (Eq. 9-13) provides a principled way to make discrete delay optimization differentiable, converging to integer delays at inference for direct neuromorphic deployment. The scheduling-matrix buffer and \(\tilde{E}\) approximation avoid predefining a maximum delay range.

## Weaknesses

### Fatal
None.

### Major
- **SSC result where adding feedforward delays reduces performance is unexplained (Table 1)**: DelRec with only recurrent delays achieves 82.58% ± 0.08%, while DelRec with both recurrent and feedforward delays achieves 82.19% ± 0.16% — lower by 0.39 percentage points. The paper lists combining feedforward and recurrent delay optimization as a contribution (line 36), yet on SSC, the largest and most important dataset, this combination hurts performance. No explanation is offered. This directly challenges the value of that particular contribution claim and needs to be addressed.

### Minor
- **Abstract claims are stronger than the evidence supports**: The abstract states that "trainable recurrent delays outperform feedforward ones" without qualification (line 9). While this holds on SSC and in the small-model SHD regime (Fig. 3C), on large-model SHD (Table 2), DCLS (ff-only, 93.77% ± 0.68%) marginally outperforms DelRec rec-only (93.39% ± 0.45%), and SE-adLIF with no delays (93.79% ± 0.76%) also beats it. Since the paper acknowledges SHD differences are not statistically significant (lines 176-177), the unqualified "outperform" claim is not supported.
- **The "first SGL-based method" claim needs sharpening**: The paper claims to be "the first SGL-based method to train axonal or synaptic delays in recurrent spiking layers" (abstract, line 9; line 36). However, ASRC-SNN (Xu et al.), which the paper cites and compares against, also learns recurrent delays via SGL/backpropagation — albeit one delay per layer selected from a fixed set via softmax. DelRec's genuine advances are per-neuron granularity and no predefined delay range, not the category of SGL-based recurrent delay learning itself.
- **PS-MNIST result rests on a single seed with a 0.44% margin**: The 96.21% vs. ASRC-SNN's 95.77% is a narrow margin from one seed. The paper transparently notes this follows prior convention (line 132), but at this level of saturation, run-to-run variance could plausibly account for the difference.
- **Confounding factors in the SHD simplification-to-comparative transition**: Architectures after simplification differ in more than just delays — batch norm is removed, bias is removed, τ is changed, learning rates differ (Table 3). While transparently disclosed, this makes it harder to attribute comparative-phase results purely to delays.

### Trivial
- **Equation reference error**: Line 98 references "Eq.15" which does not exist — likely a numbering error (should be Eq. 9 or Eq. 11).

## Nice-to-Haves
- **Computational cost analysis**: The scheduling-matrix approach adds overhead relative to standard RSNN training. A brief discussion of wall-clock time or memory usage would help practitioners assess practicality.
- **Analysis of learned delay values**: The paper never examines the distribution of learned delays (do they cluster? do different neurons learn systematically different delays?). This would connect the empirical results back to the motivating theory about expressivity and gradient propagation.
- **Per-neuron vs. per-layer delay ablation**: Since the primary advance over ASRC-SNN is per-neuron delay granularity, isolating this factor would directly quantify how much the granularity matters.
- **Discussion of the axonal vs. synaptic delay asymmetry**: The paper uses axonal delays (one per neuron) for recurrent connections while comparing against DCLS which uses synaptic delays (one per synapse) for feedforward connections. The asymmetry in delay granularity deserves a brief discussion.
- **Neuromorphic hardware constraints**: The paper motivates deployment on neuromorphic hardware but doesn't discuss constraints real hardware imposes (maximum delay values, delay resolution, per-neuron delay support).

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"Core differentiable mechanism is directly adopted from DCLS, limiting methodological novelty"**: The paper explicitly acknowledges this on line 122 ("A similar strategy was used in Hammouamri et al., 2024"). The contribution is the application to recurrent connections and the scheduling-matrix infrastructure. The method description does not re-derive the interpolation as if new — the borrowing is properly cited.
- **"Sigma annealing schedule is never specified — critical for reproducibility"**: The paper references Appendix A.2.5 for hyperparameters. The appendix was stripped in parsing; this is a parser artifact, not an author omission.
- **"Algorithm 1 is referenced but not visible"**: Same — likely in the stripped appendix.
- **"No direct experimental comparison with Mészáros et al. (2025) EventProp-based method"**: The paper explains why (EventProp's scalability issues, lines 30-34) and includes the EventProp result on SSC (76.1%) in Table 1. A direct comparison on a small-scale task would be nice but is not a weakness — the paper makes its case with SGL-based comparisons.
- **"Section-by-section notes" about minimum-delay convention and neuron model exposition**: These are presentation preferences, not substantive weaknesses. The minimum-delay convention (d=0 → effective delay of 1) is clearly stated in line 74.

## Novel Insights
None beyond the paper's own contributions. The empirical finding that even fixed random recurrent delays dramatically improve RSNN training (Fig. 3B: ~40% → ~78%) is a striking piece of evidence for the gradient-propagation hypothesis that the paper could elevate more prominently.

## Suggestions
- Explain the SSC rec-only vs. rec+ff performance gap. Even a hypothesis (overfitting, mechanism interaction, hyperparameter issue) would substantially improve the paper.
- Recalibrate the abstract's claims: qualify "recurrent delays outperform feedforward ones" to reflect where this holds, and sharpen the "first SGL-based method" claim to specify per-neuron granularity and no predefined delay range as the novelties.
- Add multi-seed results for PS-MNIST to strengthen the SOTA claim.
- Fix the "Eq.15" reference on line 98.

## Calibration Anchors

**Round 1 — Bracketing:**

| Anchor | Score | Band | Comparison |
|--------|-------|------|------------|
| pIJR9uPjy3 (DeNN) | 4.50 | Mid | Delay-based neural network; related topic but different approach (no weights, feedforward, single-spike). DelRec has substantially stronger empirical results, better-controlled ablation, and clearer writing. |
| vq75kRCYuY (SOLO) | 4.00 | Mid | SNN online training; limited novelty, significant performance drops. DelRec is clearly stronger. |
| 6iM7mmVhXh (Layer Sync) | 5.75 | Mid | Asynchronous SNN processing; interesting idea but mixed clarity and results. DelRec has clearer results and more rigorous benchmarking. |

**Round 1 bracket:** DelRec sits above the mid-band (4.00–5.75), plausibly in the 6.0–7.5 range.

**Round 2 — Narrowing:**

| Anchor | Score | Band | Comparison |
|--------|-------|------|------------|
| rDe9yQQYKt (TS-LIF) | 6.00 | Narrow | Dual-compartment LIF for time series; novel but biological plausibility concerns, missing controls. DelRec has stronger empirical validation and more thorough ablation. |
| 9HsfTgflT7 (Temporal Flexibility) | 6.20 | Narrow | Mixed time-step training; disconnect between problem framing and solution, marginal improvements in some cases. DelRec has clearer problem framing and stronger results. |
| drPDukdY3t (DeepTAGE) | 6.25 | Narrow | Gradient enhancement for SNNs; good results but energy concerns from increased firing rates. DelRec is comparable or slightly stronger — similar level of methodological novelty with more rigorous benchmarking. |

**Final score: 6.5.** DelRec is slightly stronger than the 6.25 DeepTAGE anchor (stronger empirical validation, more thorough ablation study) and clearly above the 6.00–6.20 anchors. The paper has genuine contributions with fixable weaknesses (overclaimed abstract, unexplained SSC rec+ff result), but the core method and empirical demonstration are solid.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>