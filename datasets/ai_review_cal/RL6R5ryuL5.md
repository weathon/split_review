- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper studies training stability of 830M-parameter language models by forcing divergence with high learning rates. It extends prior work (which focused on attention logit growth) by diagnosing that outputs of *QKV*, *Proj*, and *FC2* linear layers also grow during divergence. The paper proposes two architectural modifications — *QKV_norm* (moving layer norm after QKV and removing pre-norm) and *QK_norm_cap* (combining QK layer norm with softmax capping) — and shows they tolerate a 1.5× higher learning rate than the strongest prior method (*QK_norm*) and yield perplexity improvements at normal training settings.

## Strengths

- **Novel diagnosis extending beyond attention logits** (Table L2_NORM, §3): The paper demonstrates that during divergence the L2 norms of outputs from *QKV*, *Proj*, and *FC2* layers grow more than 2× compared to a converging model. Prior work (§1, citing VISION, SMALL, STABLE) focused primarily on attention logit magnitude; this paper broadens the diagnosis to all linear layers in the transformer block, providing a more complete empirical picture of where instabilities originate.

- **Two methods achieve 1.5× higher LR than the strongest prior method** (Table DIVERGE, §5): *QKV_norm* and *QK_norm_cap* converge at LR 60e-3 while *QK_norm* (the best prior approach in the same testbed) diverges. This is a clean, directly interpretable result: the proposed methods extend the stable training regime by a meaningful margin over a competitive baseline.

- **Perplexity improvements at normal training settings** (Table PPL, §5): *QKV_norm* (10.85), *QK_norm* (10.84), *QK_FC_norm* (10.87), and *QK_norm_cap* (11.00) all achieve lower perplexity than the bf16 baseline (11.19) and *soft_cap* (11.24) when trained at the standard LR of 3e-4. This shows the stability techniques do not degrade model quality and can improve it.

- **Systematic comparison across six baseline stability methods** (Table DIVERGE, §5): The paper evaluates σReparam, soft_temp, soft_cap, soft_clip, LayerScale, and QK_norm in the same training setup, allowing direct comparison of the proposed methods against a broad set of prior approaches. The resulting ranking of methods by LR tolerance is informative and internally consistent.

- **Gradient explosion analysis connects output growth to gradient pathology** (Table GRAD, §3): The paper documents that input gradient norms in *QKV* and *FC1* layers explode in the diverging model, linking the observed output L2-norm growth to the gradient instability that causes loss spikes. This provides mechanistic grounding for the divergence analysis.

## Weaknesses

### Fatal
None.

### Major

- **Single-seed evaluation for stability claims** (§5, line 209: "with the same initialization seed value"). The central claim — that *QKV_norm* and *QK_norm_cap* tolerate 1.5× higher LR — rests entirely on a single seed per learning rate. Training stability is inherently stochastic; a failure on one seed could be a random spike, and a single successful run does not demonstrate reliable stability. For a paper whose thesis is about *reliable* training stability, this is a significant evidential gap. The consistency of results across methods partially mitigates this concern (the ordering of methods by LR tolerance is clean and makes architectural sense), but it does not replace proper multi-seed evaluation. **Why it matters**: Without knowing whether the divergence boundaries are robust across random seeds, the paper cannot convincingly establish that its methods *reliably* increase LR tolerance.

### Minor

- **Dataset not fully specified for reproducibility** (§2, line 31): Training data is described only as "a mixture of diverse set of public and proprietary datasets" containing 53 human and 37 programming languages. No public components are named. Because training stability can be sensitive to data distribution, this limits independent reproducibility. (This is a common limitation in papers using proprietary data and does not invalidate results, but it is worth noting.)

- **Missing perplexity baselines for σReparam and LayerScale** (§5, Table PPL): The perplexity comparison omits σReparam and LayerScale — two stability methods tested in the divergence table. The paper's selection criterion ("which converge with LR 40e-3") excludes them, but including them at normal LR (3e-4) would strengthen the claim that the proposed methods' perplexity benefits are not simply artifacts of any normalization change.

- **Perplexity confidence interval is unexplained** (§5, Table PPL caption): The paper reports "confidence interval ±0.1 at 95% level" but does not describe how this is computed (token-level variance within one run, or across multiple runs?). Without clarification, the reader cannot assess whether the reported differences (e.g., 10.84 vs. 10.85) are statistically meaningful.

- **QK_FC_norm failure explanation is incomplete** (§5, line 245): The paper concludes that *QK_FC_norm*'s failure to improve over *QK_norm* implies "the main reason for divergence is in QK layers." An alternative hypothesis — that adding extra LayerNorms introduces gradient conflicts or optimization difficulties — is not explored. A brief gradient-norm analysis for *QK_FC_norm* would clarify this.

- **No ablation on softmax capping value** (§4, §5): *QK_norm_cap* uses a capping value of 50 (inherited from *soft_cap*). Whether this value is critical, or whether a range of values produces similar gains, is not examined. The paper would be strengthened by showing that the combined method is not brittle to this choice.

### Trivial

- **L2-norm plots are small embedded images** (Table L2_NORM, Table GRAD): The inline images (40mm × 30mm) are difficult to read quantitative values from. The claim of "more than 2× higher at training step 1000" (line 85) cannot be verified by the reader from the images alone. Including a tabulated numeric summary would improve clarity.

- **LR grid is coarse** (§5): The grid steps from 40e-3 to 60e-3 to 80e-3. The 1.5× claim uses the points 40 and 60, which is correct, but the grid resolution means the true maximum stable LR for each method is bracketed rather than precisely determined.

## Nice-to-Haves

- Run the full stability experiment with 3–5 random seeds, reporting the proportion of runs that diverge at each LR. This would transform the paper's central empirical claim from suggestive to robust.
- Include σReparam and LayerScale in the perplexity comparison at normal LR (3e-4) to complete the picture.
- Provide a brief ablation on the capping value in *QK_norm_cap* (e.g., try 25, 50, 100).
- Test the proposed methods on at least one larger model (e.g., 1.5B or 3B) to indicate scaling behavior.
- Include a short gradient-norm analysis for *QK_FC_norm* to rule out gradient-conflict explanations for its lack of improvement.

## Removed Points

These points were identified by reviewers but are removed (with brief justification):

- **"The synthetic softmax example (Fig 6) does not demonstrate that real attention logits reach 40× magnitude"** — The example is pedagogical (line 86: "For demonstration purposes"). The paper is not claiming real logits reach 40×; the synthetic example illustrates a phenomenon that the QK norm / capping methods are designed to prevent. This criticism reads the example too literally.
- **"The 1.5× factor is exaggerated by grid coarseness"** (harsh critic) — The factor is computed from the points where methods diverge (60/40 = 1.5), which is the standard way to report this. If anything, the true factor could be larger (between grid points). This criticism is incorrect.
- **"Pure formatting/style nitpicks"** and **"typos"** — These are parser artifacts, not author errors.
- **"Missing related works"** — I cannot verify the existence of missing references without external sources.
- **"Reproducibility concerns about undisclosed hyperparameters"** — The paper reports all key hyperparameters (batch size, LR schedule, optimizer params, weight decay, gradient clipping, warmup steps, etc.). The training setup is adequately specified.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Multi-seed evaluation** is the single highest-impact improvement. Re-run Table DIVERGE with at least 3 seeds; report the proportion of converged/diverged runs rather than a binary outcome from one seed. This directly addresses the most consequential weakness.
2. **Clarify the perplexity CI computation** in text or a footnote — specifically whether it reflects run-to-run variance or within-run token-level variance.
3. **Add σReparam and LayerScale to the perplexity table** (or explain why they are excluded beyond the convergence-at-40e-3 criterion). This would make the perplexity comparison more complete.
4. **Improve the L2-norm analysis** by including a small numeric table of L2 norms for representative layers at convergence/divergence steps, alongside the existing images.
