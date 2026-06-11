Now I have sufficient calibration context. Let me write the final consolidated review.

## Summary

IRIS proposes using Negative Self-Certainty (NSC = KL(U ∥ πθ)) as an intrinsic reward for RL fine-tuning of autoregressive text-to-image models. The paper discovers that contrary to text reasoning (where maximizing self-certainty helps), minimizing self-certainty produces richer, more diverse images. Using only this intrinsic signal with GRPO, IRIS achieves results on GenEval, T2I-CompBench, and WISE that are within 3–4% of the external-reward baseline (T2I-R1) on all overall metrics, and outperforms it on several sub-metrics (Colors in GenEval, Color/Texture/Non-Spatial in T2I-CompBench, Biology in WISE).

## Strengths

- **Novel and counterintuitive finding about self-certainty direction for T2I**: The paper demonstrates through controlled ablations (Fig. 6 and 7) that minimizing self-certainty (maximizing uncertainty) consistently improves T2I generation, while maximizing self-certainty — which benefits text reasoning — causes rapid performance collapse. This reverses the finding in prior text-domain work (Zhao et al., Zhang et al.) and is a non-obvious contribution.

- **Comprehensive ablation study validating all design choices**: Sec. 4.3 systematically ablates each dimension — CoT vs. no CoT, minimize/maximize image SC, minimize/maximize text SC, forward vs. backward KL, and RL vs. direct optimization. Each ablation isolates a specific question. The direct-optimization collapse (Fig. 9) is a particularly informative sanity check showing why RL is necessary despite the reward being differentiable.

- **Competitive benchmark performance without any external supervision**: Table 1 shows IRIS (no external rewards, no human labels) achieves GenEval 0.72/0.77, T2I-CompBench Complex 0.3793/0.3916, and WISE 0.37/0.48 on Janus-Pro-1B/7B — within 3–4% of the external-reward baseline T2I-R1. On several sub-metrics, IRIS actually outperforms T2I-R1 (Colors in GenEval: 0.88 vs 0.86; Color/Texture in T2I-CompBench: 0.7946 vs 0.7924 and 0.6756 vs 0.6691; Position in GenEval: 0.66 vs 0.64).

- **Clean evaluation protocol**: The main evaluation uses independent benchmarks (GenEval, T2I-CompBench, WISE) separate from any training reward. The ablation study uses external reward models (HPSv2, DINO, GIT, ORM) only as evaluation metrics — they are never part of IRIS's training objective (line 211), avoiding evaluation circularity.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The Figure 2 evidence for "task-dependent behavior" is from a confounded comparison**: Figure 2 compares self-certainty trajectories of Qwen2.5-1.5B-Instruct on math reasoning (text tokens) vs. Janus-Pro-1B on T2I generation (image tokens). This confounds model architecture, task domain, and token modality simultaneously. The paper states that it "observes and confirms" task-dependent behavior of self-certainty (contribution 2), but the current evidence is suggestive rather than confirmatory — the observed difference could be driven by any of several confounded factors. A controlled experiment (same model on both tasks, or same task across modalities) would be needed for a stronger claim. The finding remains useful as motivation but should be framed as an observation, not a confirmation.

2. **No human evaluation despite claims about human preference alignment**: The introduction states that less confident models produce images "better aligned with human preferences" (p.1). However, all evaluation is conducted through automated benchmarks and reward models — no human preference study is conducted. While automated benchmarks are standard practice and the paper's core technical contribution (an intrinsic-reward method) does not depend on human evaluation, the framing that image quality is "inherently subjective and hard to evaluate automatically" (p.1) is in tension with evaluating entirely through automated proxies. A small-scale human preference study would strengthen the human-alignment claims.

3. **Training duration limited to 800 steps without convergence analysis**: All main experiments and ablations run for 800 training steps. While IRIS appears stable within this window, several ablation conditions (maximizing image SC, minimizing image SC only) degrade rapidly after ~200 steps. It is unclear whether IRIS would maintain or improve its performance with longer training, or whether the current best-checkpoint results reflect the method's asymptotic ceiling. Longer training runs (2000–5000 steps) would clarify this.

### Trivial
None.

## Nice-to-Haves

- A small human preference study (e.g., 100 prompts, pairwise between IRIS and T2I-R1) to directly support claims about human alignment.
- Analysis of the correlation between NSC scores and external reward model scores on a held-out set to directly test the paper's core assumption.
- Discussion of failure modes — when might NSC produce images that score well on the intrinsic metric but poorly by human judgment?
- Computational cost comparison between IRIS and the external-reward baseline.
- Longer training runs to assess convergence and stability.

## Removed Points

- **"Superior" claim in abstract not supported** — REMOVED. The abstract says "competitive with or superior to." Checking the data: IRIS outperforms T2I-R1 on several sub-metrics (Colors, Color attribution, Texture, Non-Spatial, Position, Biology). The overall metrics are within one standard deviation. "Competitive with or superior to" is a fair characterization.

- **Evaluation circularity** — REMOVED. The main evaluation uses independent benchmarks (GenEval, T2I-CompBench, WISE). The ablation study uses external reward models as evaluation metrics only, with explicit acknowledgment (line 211) that they are never used in training.

- **Semantic CoT finding not novel** — REMOVED. The paper explicitly cites T2I-R1 for this finding with external rewards and frames its contribution as showing intrinsic rewards also produce CoTs. This is appropriately scoped.

- **Insufficient comparison to generation-only models** — REMOVED. The paper includes these in Table 1 for completeness; the relevant comparison is between IRIS and T2I-R1 on the same autoregressive model.

- **Forward KL explanation not empirically connected** — REMOVED. The paper cites prior work and provides an ablation (Fig. 8) showing forward KL empirically outperforms backward KL. This is sufficient.

## Novel Insights

None beyond the paper's own contributions. The finding that self-certainty behaves oppositely for T2I vs. text reasoning, and that a simple token-level uncertainty signal can drive meaningful improvement without external supervision, is the paper's core novel insight.

## Suggestions

- Re-frame the Figure 2 claim more cautiously (e.g., "suggest" instead of "confirm") since the comparison confounds model architecture, task, and modality.
- Add a dedicated limitations paragraph addressing evaluation via automated benchmarks only and the limited training horizon.
- Run longer training (2000+ steps) to demonstrate convergence stability of IRIS.
- Consider a small human evaluation to directly support claims about human preference alignment.

## Score and Decision

**Bracketing (Round 1)**: The paper sits above the low band (<3.5, papers at 2.5–3.4 that are clearly weaker: GAN-based T2I, image captioning on small datasets) and below the high band (>7.5, papers at 7.6–8.0 that are major architectural contributions: Transfusion, Würstchen). Initial bracket: **5.0–7.0**.

**Narrowing (Round 2)**: Anchors read in full:

| Path | Score | Round | Comparison to IRIS |
|------|-------|-------|--------------------|
| bO31lfEdos (Human-Free RL for Hallucination) | 5.00 | R2 | Weaker — limited to one model/benchmark, less thorough ablations |
| Let8OMe20n (Confidence-aware Reward Opt.) | 6.00 | R2 | Comparable — IRIS has more novel contribution and better ablations |
| Ugs2W5XFFo (Info-Theoretic T2I Alignment) | 6.00 | R2 | Comparable — IRIS has more systematic ablations |
| 38E4yUbrgr (RL Contemplation for LLMs) | 6.00 | R2 | Weaker — limited novelty (similar to RLAIF) |
| 4w99NAikOE (IterComp) | 6.80 | R1/R2 | Stronger — more comprehensive, includes human eval |
| kNjrhD67LP (Cycle Consistency for Unpaired Data) | 7.00 | R3 | Stronger — broader scope and architecture contribution |

IRIS is clearly stronger than the 5.00–6.00 anchors (better ablations, more novel finding) but weaker than the 6.80–7.00 anchors (no human evaluation, shorter training, less comprehensive evaluation). Its novelty (first intrinsic-reward method for T2I, counterintuitive self-certainty finding) and thorough ablations make it stronger than the ~6.0 median of comparable papers.

**Final score**: 6.5 — a solid Accept with a clean, novel contribution and strong empirical support, held back from a higher tier by the absence of human evaluation and limited training horizon.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>