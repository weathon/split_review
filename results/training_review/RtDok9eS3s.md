Here is the consolidated final review.

## Summary

This paper systematically investigates whether standard transformer blocks can be simplified by removing components (skip connections, value/projection matrices, sequential sub-blocks, normalization). Combining signal propagation theory with empirical insights, the authors show that fixing value and projection matrices to the identity, using Shaped Attention, and adopting parallel sub-blocks removes most "non-essential" components while matching standard Pre-LN convergence speed. Their SAS and SAS-P blocks achieve 16% parameter reduction and up to 16% throughput increase on BERT-scale models, with GLUE scores within noise of the baseline.

## Strengths

- **Systematic, well-motivated research question**: The paper decomposes the transformer block into individual components and tests each one's necessity. This clarity makes negative results (e.g., normalization removal harming fine-tuning) as informative as the positive ones.

- **Recovery of training speed in skipless attention sub-blocks**: Figures 3-4 (vary_vp_resid_gain) demonstrate that restricting V/P updates or fixing them to identity eliminates the severe per-step training speed loss previously reported by He et al. (2023), directly supporting the paper's central claim that the attention skip can be removed without sacrificing convergence speed.

- **Convincing demonstration that V/P converge to identity during training**: Figure 5 (skip-resid_gain_ratios) shows that when V/P are reparameterized as identity + learnable deviations, the residual-skip ratios converge to zero for most layers. This provides a compelling empirical explanation for why these parameters are unnecessary.

- **Depth scaling results are strong**: Figure 6 shows SAS and SAS-P benefit from increased depth (18 to 72 layers), unlike prior skipless work (Value-SkipInit) which degrades. This is arguably the strongest evidence that the simplifications do not harm the model's ability to leverage depth.

- **Practical efficiency gains are real and quantified**: The 16% parameter reduction and 16% throughput increase (Table 1) are demonstrated on both decoder-only and encoder-only architectures, with matching wall-clock convergence (Figure 7: loss vs. runtime for BERT).

- **Transparent discussion of limitations**: The paper explicitly acknowledges the modest scale (100-300M parameters), the normalization removal instability during fine-tuning, and the puzzling underperformance of trainable V/P vs. fixed identity V/P.

## Weaknesses

### Fatal
None.

### Major

- **Limited scale relative to modern deployment**: The core experiments use 100-300M parameter models trained on ≤2B tokens, which is modest by current standards. While depth scaling to 72 layers is shown, these are loss curves only — no downstream task evaluation at larger scales. The paper acknowledges this limitation, but it means practitioners may hesitate to adopt the proposed block for large-scale training without evidence that the simplifications hold at 1B+ parameters.

- **Normalization removal is fragile and under-analyzed**: The paper's own experiments show: (a) a slight per-step convergence degradation (Figure 9/loss_vs_step), (b) NaN instabilities during fine-tuning ("a small minority of sequences"), and (c) the paper retreats to recommending SAS/SAS-P *with* normalization as its main approach. The root cause of the NaN issue is not explained, and the Conclusion's statement that normalization has "beneficial properties for training speed beyond what is captured by signal propagation theory" is unsatisfyingly vague. A reader interested in practical simplification needs to know *when* and *why* normalization can be safely removed.

- **Missing ablation isolating each simplification**: The paper removes multiple components at once (skip, V/P, sequential sub-blocks, normalization). An ablation that adds back one component at a time would clarify which changes are responsible for the performance recovery. In particular: does fixing V/P to identity work *without* Shaped Attention? Does Shaped Attention work *without* V/P removal? Without this, the contribution of each individual modification is unclear.

### Minor

- **GLUE scores show a small but consistent gap**: SAS (78.4±0.8) and SAS-P (78.3±0.4) vs. Pre-LN (78.9±0.7). The error bars overlap and the paper accurately says "up to statistical significance over 3 seeds," but the trend is consistently ~0.5 points lower in the same direction across variants. With only 3 seeds, the paper's claim of "no loss of performance" is slightly overconfident — "matching within noise" would be more precise.

- **The trainable V/P underperformance is unexplained**: The reparameterized model with trainable V/P achieved *worse* loss than the fixed-identity model (1.194 vs. 1.178, Section 4.2). The paper notes this and mentions the trend reverses when the attention skip is re-added, but offers no explanation. This raises unanswered questions about whether the reparameterization itself induces optimization biases, making the fixed-identity success less cleanly interpretable.

- **"No loss of training speed" language is slightly overbroad**: The abstract and introduction claim components can be removed "with no loss of training speed," but (a) normalization removal shows per-step degradation, (b) GLUE scores show a small gap, and (c) the decoder-only experiments report "essentially match" rather than exact match. The paper's own data supports "matching or slightly underperforming in some settings" more than "no loss."

- **Per-step convergence gap for normalization removal**: While wall-clock speed matches, Figure 9 (loss_vs_step) shows SAS-P no-norm has a visible per-step convergence gap, which the paper acknowledges but does not analyze. If one were to train for a fixed number of steps (rather than fixed wall time), the simplified block would underperform.

### Trivial
None.

## Nice-to-Haves

- **Ablation study isolating each simplification**: Testing identity V/P without Shaped Attention, and vice versa, would help attribute the recovery to specific mechanisms.
- **Test with randomly initialized frozen V/P (not identity)**: This would separate the *initialization choice* from the *act of removing parameters*. If random orthogonal frozen V/P work as well, the claim is about parameter removal; if not, it is about identity initialization.
- **Investigate the fine-tuning NaN issue**: What causes it — exploding activations? Can gradient clipping or a different initialization fix it? Without this, normalization removal cannot be recommended for deployment.
- **Single larger-scale experiment** (e.g., 1B parameters) would significantly strengthen confidence that the simplifications hold at scale.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The direct comparison in Figure 4 is confounded by the reparameterization trick"**: When β_V=β_P=0 with identity initialization, W^V=W^P=I (fixed) — there is no "trick" or active reparameterization during training. The matrices are simply identity and not updated. The comparison (Pre-LN vs. skipless block with identity V/P and appropriate MLP downweighting) is apples-to-apples for the question being asked. This criticism reflects a misunderstanding of the paper's setup.

- **"The correct comparison would be standard Pre-LN vs. a skipless block with identity V/P and standard Adam updates on the remaining parameters"**: This is exactly what the experiment does — Adam updates on Q, K, and MLP parameters. The MLP downweighting (β_FF=0.1) is a separate, transparently documented mechanism needed for signal propagation reasons when removing skips, not a confound.

- **"The experiment uses a special initialization scheme that itself contributes to training speed"**: Identity initialization for V/P is the simplest possible — it is equivalent to removing them. This does not "contribute to training speed" in any special way beyond the fact of removing the parameters.

## Novel Insights

The most interesting finding to emerge from the reviews is the tension between the paper's empirical success and the incomplete theoretical understanding of *why* V/P can be removed. The paper shows that (a) V/P converge to identity during training even when left trainable, and (b) the fixed-identity model *outperforms* the trainable one in the skipless setting, but this reverses when the skip is re-added. This asymmetry suggests an optimization-dynamic explanation rather than a purely expressive one: identity V/P create a better-conditioned optimization landscape for the remaining parameters when no skip is present. The community would benefit from understanding this interaction — it points toward a deeper principle about when linear projections in attention are actually harmful rather than helpful. The depth scaling result (Figure 6) that previous skipless methods actually degrade with depth while SAS improves is also noteworthy and suggests the Shaped Attention + identity V/P combination fundamentally resolves a scaling pathology that prior approaches could not.

## Suggestions

1. **Tone down the "no loss" language** to "matching within statistical noise" or "matching in wall-clock convergence" to better reflect the evidence, especially given the consistent ~0.5-point GLUE gap and the normalization removal's per-step degradation.

2. **Add a clean ablation study** isolating the effect of identity V/P from Shaped Attention and from MLP downweighting, so readers can attribute the recovery to specific mechanisms.

3. **Investigate the fine-tuning NaN issue** for normalization removal: is it an activation explosion in specific layers? Can it be mitigated with gradient clipping, a warm-up schedule change, or LayerNorm on queries/keys? Even a negative result would be informative.

4. **Report GLUE per-task results in the main paper** (they are currently in an appendix that was stripped by the parser) to allow readers to judge whether the gap is concentrated on specific tasks.

5. **Explain or investigate the trainable V/P underperformance** — this is the most puzzling result in the paper and undermines the clean interpretation that "V/P are simply unnecessary."

## Score and Decision

This paper makes a genuine contribution: it systematically simplifies the transformer block with well-designed experiments, achieves real efficiency gains, and provides depth scaling evidence that prior work lacked. The central claims are supported by multiple lines of evidence (convergence curves, GLUE evaluation, depth scaling, longer training). However, the "no loss" claim is slightly overstated for normalization removal and the GLUE results, and the experiments are at a modest scale. The paper's core value — demonstrating that V/P can be removed and combined with parallel blocks — stands even with these caveats.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>