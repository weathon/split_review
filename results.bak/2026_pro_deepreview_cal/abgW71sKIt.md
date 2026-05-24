Now I have enough information to produce the consolidated review. Let me compose it.

---

## Summary

This paper investigates why naive output alignment fails in 1-bit post-training quantization (PTQ) of LLMs through a preliminary analysis revealing three failure modes: layer-wise output matching does not guarantee block-level improvement, activation errors accumulate across layers, and output alignment can distort attention token-similarity patterns. Based on these insights, the authors propose (a) an output-error objective using full-precision targets, (b) an Attention Matrix Preservation (AMP) mechanism that gates parameter updates to preserve token-similarity, and (c) selective application of output alignment to the last fully-connected layer of each transformer block. Experiments on OPT (1.3B–30B) and LLaMA-2/3 models show consistent perplexity and zero-shot QA improvements over several 1-bit PTQ baselines.

## Strengths

- **Insightful preliminary analysis.** Section 3 provides genuine, non-obvious findings: Figure 1 demonstrates that layer-wise output matching (ARB-X) does not reliably reduce block-level loss compared to weight alignment (ARB), and Figure 2 quantifies how activation-conditioned error accumulates across blocks while token-similarity matrices progressively degrade. These observations directly and convincingly motivate the method's design decisions.

- **Consistent empirical improvements over strong baselines.** Tables 1 and 2 show the proposed method outperforms ARB-RC, ARB-X, BiLLM, and PB-LLM across OPT (1.3B–30B) and LLaMA-2/3 models on C4, WikiText2, PTB, and seven zero-shot QA tasks. Improvements are often substantial (e.g., 4.85 PPL reduction over ARB-RC on OPT-1.3B WikiText2, 0.78% accuracy gain on average QA). The breadth of evaluation — five OPT scales, three LLaMA variants, four language modeling datasets, seven QA benchmarks — provides strong evidence of general effectiveness.

- **Well-designed ablation studies.** Table 3 isolates AMP's contribution (removing AMP raises LLaMA-2-7B C4 perplexity from 19.25 to 29.12) and Table 4 isolates the output-error objective (switching to activation-conditioned error degrades perplexity by 0.7). Both components are shown to be necessary, and the ablation also reveals an architecture-dependent sensitivity (AMP matters far more for LLaMA than OPT), which the authors connect to RMSNorm vs. LayerNorm differences — a plausible and interesting hypothesis.

## Weaknesses

### Fatal

None.

### Major

- **AMP mask formulation is mathematically imprecise.** Equation (10) defines AMP masks as the `sign()` of the gradient of the AMP objective, yielding values in {−1, 0, +1}. The update rule in Equation (11) — e.g., α_r = α_r · (1 − M^r) + α_r* · M^r — is designed for a {0,1} mask. When M = −1, the update becomes α_r = 2α_r − α_r*, which extrapolates *away* from the closed-form solution. The intended behavior (use the closed-form solution when the AMP gradient indicates attention will be preserved; otherwise keep the current parameter) requires a binary mask such as M = 𝟙[∇ℒ_AMP > 0], not a sign function. Since AMP is the largest single contributor to the method's gains (Table 3), this imprecision undermines the paper's technical rigor. The fix is straightforward, but as written the procedure is ill-defined.

- **PTB collapse on LLaMA-2-7B is dismissed rather than investigated.** On PTB, the proposed method yields 3166 perplexity for LLaMA-2-7B (full-precision: 37.91), which is worse than ARB-RC (763) and ARB-X (681). The paper states "the large perplexity indicates that the metric cannot provide a meaningful evaluation" (line 237). This is hand-waving: while all 1-bit methods degrade severely on this benchmark (BiLLM reaches 5243), the proposed method is notably worse than several baselines on this specific model-dataset pair, and no analysis is offered to explain why. A method claiming robustness should confront failure cases, not dismiss them.

### Minor

- **Output-error objective provides only modest gains for LLaMA.** Table 4 shows that switching from activation-conditioned error to output error improves C4 perplexity by 0.72 for LLaMA-2-7B and 0.69 for OPT-6.7B, while AMP provides gains of ~10 PPL on LLaMA and ~0.15 on OPT. The paper's narrative weights the output-error reformulation as a core contribution, but the empirical evidence shows it is secondary to AMP, especially for LLaMA models. The paper would benefit from acknowledging this asymmetry more candidly.

- **Selective layer-wise application is asserted without supporting analysis.** Section 4.2 restricts output alignment to "only the last fully connected layer of each block, since it has the most direct impact on the block loss" (line 165). No experiments or analysis justify why this particular layer is chosen over alternatives (e.g., attention projection layers, all layers with learned weighting). The preliminary analysis in Section 3.1 only establishes that naive layer-wise alignment can be counterproductive; it does not identify *which* layers should receive output alignment.

- **Missing STB-LLM baseline.** STB-LLM (Dong et al., 2024) achieves sub-1-bit average precision and is cited in Related Works (line 42) but not included as a baseline. While STB-LLM is a pruning-quantization hybrid and not a pure 1-bit method, its inclusion would strengthen the comparative picture, particularly since it targets the same extreme-compression regime.

### Trivial

- Equation (2) contains a typo: the LHS reads \|\widehat{X}\widehat{W} - \widehat{X}\widehat{W}\|_F^2 (both terms are Ŵ) but should read \|\widehat{X}W - \widehat{X}\widehat{W}\|_F^2. The RHS expansion is correct.
- The paper states "We following a similar strategy" (line 104); should be "We follow."
- Convergence of the alternating minimization (Eqs. 5–8) is not discussed, though this is a minor omission for an empirical paper.

## Nice-to-Haves

- The AMP mechanism could be reformulated as a proper Lagrangian regularization term (λ · ℒ_AMP added to the main loss) rather than a heuristic gradient-gated mask. This would eliminate the sign-function issue and provide a clearer trade-off between output error and attention preservation.
- A systematic layer-sensitivity analysis (e.g., measuring block-loss impact when output alignment is applied at different layers) would substantiate the choice of the last FC layer.
- Reporting standard deviations across multiple calibration seeds would strengthen confidence in the reported perplexity improvements, though single-run evaluation is standard practice in LLM PTQ benchmarking.
- Adding STB-LLM as a baseline would complete the comparative evaluation.

## Removed Points

These points were flagged for removal. Treat them with caution.

- **"AMP is a principled attention-preserving regularizer" (from Strength Finder):** Removed. Equation (10)'s sign function and the resulting {-1,0,1} mask do not constitute a principled derivation. The core idea (gating parameter updates based on attention-gradient direction) is sensible, but calling it "principled" overstates the case given the mathematical imprecision.

- **"The derivation of the AMP mask and its application are problematic... makes the AMP procedure ill-defined and raises doubts about whether the reported results can be reproduced" (Harsh Critic, framed as fatal):** Demoted from Fatal to Major. The mathematical imprecision is real and important, but the core idea is clear enough to be fixable, and the empirical results demonstrate the approach works. The issue is a presentation/formulation problem, not a fundamental invalidation — replacing `sign()` with a binary threshold `𝟙[· > 0]` resolves it.

- **"No runtime or memory overhead measurements are provided in the main paper" (Harsh Critic):** Removed. The paper states "Please refer to Appendix D" (line 269). The appendix is stripped in the review copy; this is a parsing artifact, not an author omission.

- **"No statistical variability (standard deviations, confidence intervals) is reported" (Harsh Critic):** Moved to Nice-to-Haves. Single-run evaluation is the norm for large-scale LLM PTQ benchmarks (GPTQ, AWQ, OmniQuant, BiLLM all report single-run numbers). While reporting variance would be ideal, its absence does not constitute a weakness by the field's standards.

- **"The baseline set omits STB-LLM" (Harsh Critic):** Kept as Minor because STB-LLM is a relevant method in the extreme-compression space, but it targets sub-1-bit through pruning+quantization, making it not strictly a 1-bit PTQ method. Inclusion would improve the paper but is not critical.

- **"The core claimed contribution—accounting for accumulated output error—provides only a minor benefit" (Harsh Critic, framed as major):** Demoted to Minor. The ~0.7 PPL improvement is real and consistent across settings, and the paper does not claim it is the *largest* contribution — the paper presents both output error and AMP as complementary. However, the narrative tension between the stated motivation and where the gains actually come from is worth noting.

- **"Direct comparison with a simple baseline that augments ARB-RC with a token-similarity regularizer" (Harsh Critic):** Removed. This is a speculative suggestion for a new experiment, not an identified weakness of the paper as written.

- **"The analysis in Figure 1 uses full-precision other layers, which is not how PTQ operates in practice" (Harsh Critic):** Removed. This is a standard diagnostic methodology for isolating per-layer effects, not a flaw. The paper explicitly describes this as a controlled experiment to assess the relationship between layer-wise and block-wise loss.

- **"The AMP objective... maximizing this quantity does not necessarily preserve relative token relationships; a high inner product could be achieved by scaling" (Harsh Critic):** Removed. The paper states that token similarity matrices are computed "after row-normalizing" (line 80), which controls for scaling effects. The concern does not apply given this normalization.

- **"No theoretical justification is offered for why a sign-based mask would preserve attention" (Harsh Critic):** Merged into the Major weakness about the sign-function issue. The lack of theoretical justification is part of the same imprecision concern.

## Novel Insights

The preliminary analysis (Section 3) contributes a genuinely novel empirical finding: even when layer-wise output alignment succeeds at reducing per-layer error, it can *increase* block-level reconstruction loss relative to simple weight alignment (Figure 1). This is a subtle but important observation that challenges the intuitive appeal of output-matching objectives and has implications beyond 1-bit quantization — it suggests that block-level objectives should be preferred in any PTQ method that operates layer-by-layer. The finding that token-similarity matrices degrade under naive output alignment (Section 3.3) is also interesting, though the specific mechanism (RMSNorm vs. LayerNorm sensitivity) is only hypothesized rather than tested.

## Suggestions

- Replace `sign()` in Equation (10) with a binary threshold `𝟙[· > 0]` (or a sigmoid-based soft gate) to make the AMP mask well-defined. This is a one-line change that resolves the major mathematical imprecision.
- Investigate and report the cause of the LLaMA-2-7B PTB collapse. Even a brief diagnostic (e.g., checking whether specific outlier tokens or sequences cause the degradation) would strengthen the paper significantly.
- Add a brief discussion of why the last FC layer is chosen for output alignment — even a simple ablation comparing different layer choices within a block would provide empirical support.
- Fix the Equation (2) typo and minor language issues.

## Score and Decision

**Round 1 bracket:** Based on calibration anchors for 1-bit/PTQ quantization of LLMs, the paper falls between ~5.0 and ~7.5.
- Low band (<3.5): EfficientQAT (3.00), PrefixQuant (3.00), CVXQ (3.00) — all clearly weaker.
- Middle band (3.5–7.5): PB-LLM (6.75), OmniQuant (6.40), STB-LLM (6.00), FPTQ (4.00) — these are the relevant comparators.
- High band (>7.5): CBQ (7.60), Scaling Laws for Precision (8.00) — these are stronger papers.

**Round 2 narrowing within [5.0, 7.5]:**
- STB-LLM (6.00): sub-1-bit structured binarization. Our paper is stronger — clearer motivation, better-organized contribution, more consistent evaluation, and does not suffer from the motivation-methodology mismatch that STB-LLM reviewers flagged.
- PB-LLM (6.75): partially binarized LLMs. Our paper has broader evaluation (5 model sizes vs. 1, 4 datasets vs. primarily CSQA) and more insightful preliminary analysis. However, PB-LLM has a cleaner methodology without mathematical imprecision. Our paper is comparable but slightly lower due to the AMP sign-function issue.
- CBQ (7.60): cross-block quantization. Our paper falls below this — CBQ has a cleaner framework and addresses error accumulation more systematically.

**Anchor summary:**
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| EfficientQAT | 3.00 | 1 | Clearly weaker — different topic, QAT not PTQ |
| PB-LLM | 6.75 | 1,2 | Closest comparator; our paper has better evaluation but sloppier methodology |
| STB-LLM | 6.00 | 2 | Our paper is stronger — better motivation and evaluation |
| CBQ | 7.60 | 1,2 | Our paper is weaker — CBQ has cleaner methodology |
| OmniQuant | 6.40 | 1,2 | Our paper has more novel insights but less polished method |

The paper sits between STB-LLM (6.00) and PB-LLM (6.75). Given the AMP formulation issue (fixable but significant), the PTB dismissal, and the modest output-error contribution relative to the narrative, but offset by the genuinely insightful preliminary analysis and thorough evaluation, I place it at **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>