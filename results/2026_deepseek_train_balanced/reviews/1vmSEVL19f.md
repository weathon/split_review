## Summary

This paper introduces Direct Reward Fine-Tuning (DRaFT), a family of methods that fine-tune diffusion models by backpropagating differentiable reward gradients through the sampling process. DRaFT-K truncates backpropagation to the last K steps, and DRaFT-LV uses a low-variance gradient estimator by averaging over multiple noise samples at the final step. The paper provides a unified algorithmic framework connecting DRaFT variants with prior work (ReFL) and demonstrates results on aesthetic quality, human preference scores (HPSv2, PickScore), and diverse unconventional rewards (compressibility, object detection, adversarial examples).

## Strengths

1. **>200× sample efficiency vs. RL on aesthetic optimization, directly measured**: Figure 2 (Left) shows DRaFT reaching LAION Aesthetic scores of ~7.5 in roughly 200 reward queries, while DDPO requires ~50k queries to reach 7.4 on the same 45 animal prompts. This is a concrete, quantitative comparison on an identical setup that cleanly demonstrates the advantage of using reward gradients over policy-gradient methods.

2. **Non-obvious finding that truncated backprop (K=1) outperforms full backprop, with gradient-norm evidence**: The paper demonstrates empirically (Figure 8) that small K yields better reward per training step than full backpropagation (DRaFT-50), and provides an explanatory mechanism — gradient norms explode as K increases (Figure 7). This is counterintuitive (more gradient information should be better) and practically significant.

3. **DRaFT-LV's low-variance estimator yields ~2× faster learning with ~10% overhead**: DRaFT-LV achieves higher HPSv2 reward at 5k training steps than DRaFT-1 at 10k steps (Figure 4, line 299), while adding only ~10% compute overhead (line 206). This is a clean, measurable improvement over both DRaFT-1 and ReFL.

4. **Unified algorithmic framework subsuming prior work**: Algorithm 1 presents a single framework where DRaFT, DRaFT-K, DRaFT-LV, and ReFL differ only in the position of a `stop_gradient` operation. This abstraction clarifies the design space and correctly identifies that ReFL with m=1 is equivalent to DRaFT-1 (line 213).

5. **Practical LoRA compositionality across reward functions**: The paper demonstrates that LoRA weights trained independently for different rewards (PickScore, HPSv2, aesthetic) can be linearly interpolated to combine their effects without additional training (Figure 6, Right), a practical advantage over score-function composition that increases inference cost linearly with the number of models.

## Weaknesses

### Fatal
None.

### Major

1. **Overclaiming reinforcement learning outperformance relative to the evidence presented**: The abstract (line 6: "outperforming reinforcement learning-based approaches") and introduction (line 43) make a broad claim of superiority over RL methods. However, the only direct RL comparison is the aesthetic experiment on 45 animal prompts (Figure 2, Left), where the DDPO baseline result was obtained "from correspondence with the authors, as the results in the original paper use a buggy implementation" (line 244). RL methods (DDPO, DPOK) are entirely absent from the paper's main HPSv2 benchmark evaluation (Section 5.2, Figure 4), which compares against supervised methods, DOODL, best-of-16, and ReFL. The claim's breadth exceeds what the experiments support. This is not a fatal flaw — the method's efficiency advantage is convincingly shown on the aesthetic task — but the paper should either add controlled RL comparisons or qualify the claim.

2. **Evaluation relies almost entirely on the reward metrics being directly optimized, with no diversity or human evaluation**: Across all experiments, the primary quantitative metric is the reward score itself (LAION aesthetic predictor, HPSv2, PickScore) — precisely the functions DRaFT maximizes via gradient ascent. The paper explicitly acknowledges reward hacking: "the methods initially produced improved images, but eventually collapsed to producing very similar high-reward images" (line 255). Without diversity metrics (FID, LPIPS diversity, CLIP score) or even a small human preference study, it is unclear whether the reported score gains reflect genuine image quality improvement or better reward overfitting. This gap matters because the paper's central conclusion is that DRaFT "substantially improves" image quality (abstract, line 8).

### Minor

3. **DRaFT-LV's possible bias not discussed**: DRaFT-LV noises the final generated image and re-denoises it (lines 203–204). This means the reward gradient is evaluated on a noise-perturbed-and-reconstructed image rather than the clean generated image. The paper does not discuss whether this creates a systematic bias toward images robust to noise corruption — a subtly different objective from maximizing the reward on the actual generated output.

4. **Gradient norm analysis is only qualitative**: The explanation for why truncated backprop outperforms full backprop — gradient explosion as K increases — is supported only by a visual figure (Figure 7, caption "Gradient norms") with no quantitative summary (e.g., mean/max gradient norms per K value in a table). This limits reproducibility and makes it harder for others to build on this finding.

### Trivial
None.

## Nice-to-Haves

- A controlled RL comparison on the HPSv2 benchmark (matched prompts, LoRA, and training budget for DDPO/DPOK) would substantiate or temper the central comparative claim. This is the single highest-leverage addition.
- A small-scale human preference evaluation (e.g., 100 pairwise comparisons between DRaFT and baseline SD outputs) would convert the evidential gap about reward overfitting into a demonstrated strength.
- Wall-clock time comparisons for DRaFT variants (not just training steps) would clarify whether the efficiency claims hold end-to-end.

## Removed Points

*These points were flagged by reviewers but excluded from the main weaknesses after verification against the paper.*

1. **"Best-of-16 comparison is misleading because it does not train"** — Removed. The paper lists best-of-16 as a baseline on final HPSv2 reward values (Figure 4 caption, line 269), which is standard practice. The paper does not compare methods on training steps or make a compute-controlled claim against best-of-16. The criticism misreads the evaluation.

2. **"Paper does not state how many reward queries DRaFT used"** — Removed. The DRaFT curves in Figure 2 are plotted on the "Reward Queries" x-axis; the information is presented visually, which is standard.

3. **"ReFL comparison is not decisive"** — Removed in this framing. The paper transparently acknowledges ReFL with m=1 is equivalent to DRaFT-1 (line 213) and correctly compares against ReFL as originally proposed (m=20). DRaFT-LV is the substantive improvement, and this is clearly stated (line 299). The comparison is fair.

4. **Missing appendix/hyperparameter details** — Removed per instructions. The parser strips appendices; these exist in the original submission.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Remove or substantially qualify the broad claim of "outperforming reinforcement learning-based approaches" from the abstract, or add a controlled RL comparison on the HPSv2 benchmark to support it.
2. Add diversity metrics (LPIPS diversity, FID, or per-prompt CLIP score variance) to the HPSv2 evaluation to demonstrate that reward gains are not at the expense of generation diversity.
3. Add a small quantitative table of mean/max gradient norms across K values to make the gradient explosion analysis reproducible.
4. Discuss the potential bias from DRaFT-LV's noise-then-denoise procedure.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>