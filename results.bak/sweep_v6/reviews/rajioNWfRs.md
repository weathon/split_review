Now I have all the information needed to write the consolidated review.

---

## Summary

This paper introduces TNT, a two-stage training framework for deep memory modules (specifically Titans). Stage 1 uses a hierarchical memory architecture—a global module processing large chunks for long-range context, and parallel local modules with periodic state resets for fine-grained details—to enable massive context parallelism during pre-training. Stage 2 fine-tunes only the local modules at smaller chunk sizes for high-resolution inference. Evaluated on 150M-parameter Titans models, TNT reports up to 17.37× training speedup to a target loss while simultaneously improving perplexity and commonsense reasoning accuracy over the strongest Titans baseline.

## Strengths

- **Periodic reset of local memory states is a simple yet effective mechanism for enabling context parallelism in non-linear RNNs.** This breaks a long-standing sequential dependency that previously prevented efficient parallelization of non-linear recurrent modules (e.g., those with normalization between chunks). The idea is clean, well-motivated by the problem analysis, and demonstrably effective (nearly flat runtime across sequence lengths while Titans' runtime grows 10×).

- **Q-K Projection elegantly addresses a genuine domain mismatch.** The observation that memory is trained on keys but queried with queries is insightful, and the projection fix is computationally cheap (running-sum implementation). The ablation (Table 3) confirms its importance: removing it hurts perplexity from 21.04 to 22.01.

- **Training speedups are substantial and credible.** Even accounting for comparisons against the strongest Titans configuration (C=8), TNT achieves meaningful wall-clock speedups (7.68× with matching chunk size C_L=8, up to 17.37× with C_L=64). The pattern is consistent across all configurations in Table 1.

- **Accuracy improvements are real and not just efficiency-for-performance trade-offs.** TNT Stage 1 achieves C4 perplexity 20.15 with C_L={4,8,16,32} vs. the best Titans C=8 at 22.25—a genuine quality improvement alongside the speed gains. Commonsense reasoning accuracy also improves (41.0% vs. 39.0% for Titans C=8).

- **The paper correctly identifies three concrete challenges** (training inefficiency, compression-retrieval mismatch, chunk-size sensitivity) that constrain deep memory modules, providing a clear problem statement that frames the contributions.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Ablation baseline inflates apparent improvement.** Table 3 uses Titans C=256 (C4 PPL 23.53) as its "Base Model," not the strongest Titans configuration C=8 (PPL 22.25). Adding one local memory to TNT brings PPL to 21.04, which the paper presents as a 2.49-point improvement (23.53→21.04), but the improvement over the strongest baseline is 1.21 points (22.25→21.04). The main comparisons in Table 2 are fair and include both C=256 and C=8 baselines, so this doesn't invalidate the paper's claims, but the ablation's framing is misleading and should be corrected or explicitly justified.

- **No control or clarification for parameter count across architectures.** The paper states "150M parameter models" but does not explain how the parameter count is maintained when TNT adds a global memory module plus multiple local memory modules on top of a single-memory Titans backbone. If total parameters are held constant, the per-component capacity differs; if they are not, TNT has more capacity. This is important for attributing the source of accuracy gains.

- **The "linear runtime scaling" claim for TNT contradicts the data shown.** Figure 4 reports TNT's runtime as ~400–550 ms across sequence lengths 2K–32K (roughly constant), not growing linearly. The experimental design fixes total tokens per batch (0.5M), so a flat runtime is expected from a well-parallelized model. The comparison against Titans (which does grow) is valid and informative—it demonstrates TNT's superior parallelization—but the specific claim of "linear scaling" for TNT is incorrect as stated.

- **Stage 2 fine-tuning yields marginal improvements.** Average perplexity improves from 23.13 (Stage 1, best) to 23.09 (Stage 2). While the paper correctly notes it is inexpensive (~5% additional compute), the magnitude of improvement is very small and in some configurations (Table 3, +4 local memories) Stage 2 actually increases perplexity (20.15→20.86). The paper's claim that Stage 2 "often surpasses" should be tempered.

- **The 17.37× speedup and best accuracy come from different configurations.** The best speedup (Table 1) uses C_L={64} with one local module, while the best perplexity (Table 2) uses C_L={4,8,16,32} with four local modules. The paper's phrasing "improving accuracy" is true in an overall sense (TNT configurations outperform Titans), but it does not show a single configuration simultaneously achieving the full 17× speedup *and* the best accuracy.

### Trivial

- Figure 4 caption states "TNT's runtime grows linearly with sequence length" but the plotted data shows approximately constant runtime. This is a factual error in the description.

## Nice-to-Haves

- A controlled comparison where the Titans baseline is scaled to have comparable total FLOPs or memory module capacity as TNT would strengthen the attribution of accuracy gains to the training paradigm rather than to additional capacity.
- An ablation of the periodic reset itself (TNT with hierarchical memory but *without* the reset, i.e., local memory carries state across the full sequence) would directly validate the central mechanism.
- Reporting tokens-per-second or wall-clock time for the best-quality TNT configuration (C_L={4,8,16,32}) alongside its accuracy would complete the time-to-quality picture (this may already be in the stripped Table 4).

## Removed Points

- **"Figure 4 cannot support the paper's scaling claims"** (Harsh Critic #3 second half): The comparison between TNT and Titans under identical experimental conditions is valid. TNT's flat runtime vs. Titans' growing runtime *does* demonstrate superior parallelization, even if the "linear scaling" label is wrong. Kept as a minor presentation issue instead.
- **"Target loss of 3.20 is arbitrary"** (Harsh Critic): Time-to-target-loss is a standard comparison method. Removed as a generic nitpick.
- **"Stage 2 fine-tuning shows negligible improvement"** framed as a fatal flaw: The small improvement is acknowledged (minor weakness above) but the paper is transparent about it being inexpensive. Not a fatal issue.
- **"No training time reported for best TNT configuration"** (Harsh Critic #4): The paper references Table 4 for detailed training time. The parser strips appendices; this information exists in the original submission. Removed per hard rules.
- **Generic strengths from Strength Finder**: Removed vague praise about "important problem" and "well-motivated." Only kept concrete, evidence-grounded strengths.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the ablation baseline**: Either justify why Titans C=256 is the appropriate comparison point (e.g., it matches the global memory's large-chunk setting), or re-run the ablation with C=8 as the base to present an honest delta.
2. **Clarify parameter accounting**: State explicitly whether the 150M parameter count includes the memory modules, and if TNT's global + N local memories have the same total memory-parameter budget as Titans' single memory.
3. **Correct the runtime description**: Replace "linear runtime scaling" with "near-constant runtime across sequence lengths due to context parallelism, with a wall-clock advantage over Titans that grows with sequence length."
4. **Temper Stage 2 claims**: Acknowledge that fine-tuning gains are small (or negative in some configs) and explain when it helps vs. when it doesn't.
5. **Add the periodic-reset ablation**: The reset mechanism is the paper's central innovation; ablating it (hierarchical memory without reset) would substantiate the core claim.

## Score and Decision

**Calibration anchors** (from `/home/wg25r/split_review/datasets/deepreview_13k_calibration/`):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `AL1fq05o7H.md` (Mamba) | 6.25 | A landmark efficient architecture paper with broader impact but similarly questioned on missing baselines and weak ablations. The current paper is narrower in scope and less ambitious. |
| `dDpB23VbVa.md` (Patch-Level Training) | 7.50 | Cleaner experimental design and clearer presentation of a training efficiency idea. The current paper has comparable contribution size but weaker experimental framing. |
| `IIVYiJ1ggK.md` (Rodimus) | 6.00 | Similar scope (efficiency-accuracy trade-off), comparable experimental depth. Current paper's weaknesses (ablation baseline, parameter matching) are more pronounced. |
| `HEcbGXzIHK.md` (Episodic Memory for RNNs) | 4.25 | Overclaimed, confusing presentation. Current paper is more clearly motivated and has more concrete contributions. |
| `4ymHtDAlBv.md` (FSFC RNN) | 2.33 | Very weak paper. Current paper is substantially stronger in both ideas and evidence. |
| `FBkpCyujtS.md` (Min-p Sampling) | 8.50 | Clean, narrowly-scoped contribution with clear evidence and community adoption. Current paper is less polished and less definitive. |

The paper's core ideas (periodic reset for context parallelism, Q-K projection) are genuine contributions with clear empirical support. The training speedups are real and the accuracy improvements are meaningful. However, the experimental presentation has multiple flaws—a misleading ablation baseline, imprecise runtime claims, and unclear parameter accounting—that collectively weaken the paper's credential. The paper is not fatally flawed; these issues are fixable. Relative to the anchors, it sits between the weaker RNN papers (~4.25) and the cleaner efficiency papers (~6.0–6.25), closer to the former due to the presentation issues.

**Score**: 5.0

**Decision**: Reject

The paper has real ideas and the evidence broadly supports its claims, but the presentation—particularly the choice of ablation baseline and the mischaracterization of the runtime results—obscures the true magnitude of the contributions and undermines reader trust. A revised version with honest ablation comparisons, corrected runtime descriptions, and parameter accounting would merit reconsideration.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>