Now I have everything I need. Let me write the consolidated review.

## Summary

This paper proposes the Language Confusion Gate (LCG), a lightweight two-layer MLP that operates at decoding time to filter tokens from inappropriate language families. The gate is trained via norm-adjusted self-distillation: the model's own debiased logits (divided by token embedding norms) are used to create multi-label pseudo-targets indicating which language families are permissible. At inference, the gate dynamically masks disallowed tokens, guided by simple intervention rules. Evaluated on Qwen3, Llama3.1, Gemma3, and GPT-OSS across FLORES+, INCLUDE, and Humaneval-XL, LCG reduces script-level language confusion by an order of magnitude (e.g., Qwen3-8B CJ confusion from 4.5%→0.1%, Latin from 12.1%→2.0%) with only 0.4% overhead, while largely preserving legitimate code-switching.

## Strengths

1. **Well-motivated method grounded in mechanistic analysis.** Section 3.2's analysis of token embedding norm imbalance (Table 1) directly motivates the norm-adjusted self-distillation training. The paper shows that high-resource language tokens have systematically larger embedding norms, biasing sampling. The ablation in Table 3 (LCG-unadjusted vs. LCG-adjusted) validates that norm adjustment is essential — e.g., Llama3.1-8B Latin% drops from 5.7% to 2.9% when norm adjustment is added.

2. **Order-of-magnitude confusion reduction without task degradation.** Tables 3 and 4 show consistent, large reductions across four standard models and three thinking models. On no-think models: Qwen3-30B CJ% from 1.0%→0.0%, Latin% from 4.4%→0.4%, BLEU stable (13.2→13.4). On thinking models (Humaneval-XL): Qwen3-30B CJ% from 0.12%→0.00% with Pass@1 unchanged (91.25→90.50). This directly and convincingly supports the central claim.

3. **Extremely lightweight and practical.** Section 6 reports only 0.4% per-step overhead (15.95ms vs 15.99ms) and Section 5.3 shows the gate fires at only 0.33%–0.38% of tokens. This is measured in a production setting, not a synthetic benchmark. The plug-in design requires no model modification or retraining, making it directly deployable.

4. **Comprehensive evaluation across diverse models.** The paper tests LCG on 5 model families (Qwen3-8B/30B, Llama3.1-8B, Gemma3-12B, GPT-OSS), covering both standard and thinking/reasoning modes, across translation (FLORES+), knowledge/reasoning (INCLUDE), and code generation (Humaneval-XL) tasks. This breadth supports generalizability claims.

5. **Direct comparison with multiple baselines and systematic ablation.** Figure 3 compares LCG with ICL, greedy decoding, and ORPO, showing LCG achieves the lowest confusion rates while maintaining task performance (ORPO degrades accuracy). The "No Rule" ablation demonstrates that the learned gate contributes beyond the heuristic rules, and the LCG-adjusted vs. unadjusted comparison validates the norm-adjustment contribution.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Pseudo-target quality is not directly validated.** The training signal is the norm-adjusted candidate set — the paper determines which language families appear in the top-k/p tokens after dividing logits by embedding norms. However, there is no systematic analysis of how often these pseudo-targets match the ground-truth intended language. While the downstream results (Tables 3, 4) provide indirect validation that the training signal is useful, the paper would be stronger with a direct recall/precision evaluation on a held-out set. This is an evidential gap in the training procedure, though not a fatal one since the overall method demonstrably works.

2. **Missing comparison with the most directly comparable inference-time baseline.** The related work discusses Nie et al. (2025), who suppress specific neurons during inference to reduce language confusion. This is the same operational paradigm (inference-time intervention without model retraining) and several of the tested models (Llama3.1, Qwen) are compatible. Including this baseline would clarify whether LCG offers advantages over neuron suppression.

3. **Train/eval data overlap for FLORES+ not explicitly clarified.** The LCG training data includes the FLORES+ dataset (used to generate translation pairs), and evaluation is on FLORES-NO-LATIN and FLORES-WITH-LATIN, which are subsets of FLORES+. The paper does not state whether evaluation examples were excluded from training. This should be clarified. If there is no overlap, stating this explicitly would resolve the concern.

4. **Training hyperparameters for the gate are not reported.** The hidden dimension of the two-layer MLP, optimizer, learning rate, number of epochs, and computational cost are not specified. This limits reproducibility.

5. **Code-switching preservation is partially evaluated but could be stronger.** The 86.7% allow rate on human-validated examples is reasonable evidence that LCG preserves natural code-switches. However, the FLORES-WITH-LATIN experiment shows a large reduction in code-switch rate (e.g., Qwen3-8B from 46.34% to 25.90%, vs. the reference answer rate of 38.36%). While the paper correctly notes this is closer to the reference (the baseline over-generated Latin), there is no token-level analysis confirming that the removed tokens were actually erroneous rather than legitimate. Adding such an analysis would strengthen the claim.

6. **Within-script confusion is scoped out without quantification.** The paper acknowledges that LCG operates at the script level and cannot handle within-script confusion (e.g., English vs. Spanish). However, it does not quantify what fraction of real-world language confusion is cross-script vs. within-script, making it difficult to assess the practical coverage of the method.

### Trivial

- Statistical significance / confidence intervals are not reported for any result. Given the large token counts (e.g., 139k tokens for one condition), small differences could be significant, but the reader cannot assess this.

## Nice-to-Haves

- **Within-script confusion analysis:** A distribution analysis of confusion errors across the tested models would clarify the practical significance of LCG's script-level scope.
- **"Rules only" ablation:** The paper includes "No Rule" (gate without rules) but not "rules without gate," which would isolate the contribution of the gate vs. the heuristics.
- **Statistical reporting:** Confidence intervals or significance tests for the main results.
- **Pseudo-target recall/precision:** A direct validation of the norm-adjusted candidate set's accuracy on a held-out annotated set.

## Removed Points

These points were considered and excluded from the main weakness section with justification:

- **"The code-switching evaluation is circular"** (Harsh Critic): The human-validated experiment tests whether LCG would *block* already-validated natural code-switches. This is a valid and direct evaluation of LCG's harmlessness to legitimate mixing, not circular reasoning. However, the weaker related point (that natural switches that *could have happened* but didn't are not tested) is reasonable, and the code-switching analysis remains a minor weakness (see #5 above).

- **"Rule (2) could negate the gate's effect"** (Harsh Critic): This is speculative — the overall results show LCG works effectively. Without data on how often this rule fires, this is not a verifiable weakness.

- **"Rule (3) persistence bias may account for much of the reduction"** (Harsh Critic): The "No Rule" ablation already shows LCG works without rules. The missing "rules only" ablation is noted in Nice-to-Haves.

- **"Figure 2 only shows a single example"** (Harsh Critic): Figure 2 is illustrative; the main results validate the approach statistically. This is not a weakness.

- **"Token classification details in Appendix A are not in the main text"** (Harsh Critic): Appendix content is stripped by the parser — this is not a weakness of the paper as submitted.

- **"ORPO baseline may not be optimized"** (Harsh Critic): Speculative. The paper describes the ORPO setup (multilingual dataset, synthesized confusion samples). Without evidence of suboptimal configuration, this is not a valid criticism.

- **"Overhead only reported for one model"** (Harsh Critic): A reasonable single-data-point measurement given that this is a production-system benchmark. Not a weakness.

- **Strength Finder strengths about "comprehensive comparison" and "generalizability"** are valid and retained; strength about "preservation of legitimate code-switching" is retained but nuanced in the weakness section.

## Novel Insights

None beyond the paper's own contributions. The key insight — that token embedding norm imbalance creates a systematic bias favoring high-resource language tokens, and that this can be exploited via norm-adjusted self-distillation to train a lightweight confusion gate — is the paper's own contribution, not a meta-insight from the reviews.

## Suggestions

1. Clarify the train/eval split for FLORES+ to address the potential data leakage concern.
2. Include the Nie et al. (2025) neuron suppression baseline in the comparison.
3. Report training hyperparameters (MLP hidden size, optimizer, learning rate, epochs) for reproducibility.
4. Add a token-level analysis for the FLORES-WITH-LATIN experiment to confirm that LCG's reduced code-switch rate comes from removing erroneous, not legitimate, Latin tokens.
5. Add a direct validation of the pseudo-target quality (recall/precision against ground-truth language on a held-out set).
6. Report confidence intervals or significance tests for the main results.

## Score and Decision

**Calibration Anchors (all rounds):**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| Polybasic Speculative Decoding | 3.00 | R1 (weak) | Much weaker — lacks empirical grounding, theoretical-only |
| FTP Token-wise Pruner | 3.00 | R1 (weak) | Weaker — narrow contribution, unclear improvements |
| BMLM Bidirectional LLM | 3.00 | R1 (weak) | Weaker — domain-specific, limited impact |
| MrT5 (Poster) | 4.25 | R1 (mid) | Weaker — only tested on moderate model sizes, performance tradeoffs, missing baselines |
| Fast and Slow Generating (Reject) | 5.25 | R1 (mid) | Weaker — lacks concrete results, System 1/2 analogy forced |
| TA-ITI (Reject) | 6.00 | R2 (narrow) | Comparable approach but considered incremental, LCG has cleaner motivation/evaluation |
| SASA Self-Detoxifier (Poster) | 6.00 | R2 (narrow) | Similar lightweight decoding-time intervention; LCG has better task preservation and overhead measurement |
| RAIN (Poster) | 6.00 | R2 (narrow) | Similar self-distillation concept but for alignment; LCG has more comprehensive evaluation |
| VocADT (Poster) | 6.25 | R2 (narrow) | Comparable accepted paper but only one base model tested, more incremental; LCG stronger in breadth and mechanistic motivation |
| Decoding as Direct Metrics (Poster) | 6.25 | R2 (narrow) | Comparable accepted paper with different focus; LCG lighter weight and more targeted |
| Chunk-Distilled LM (Poster) | 6.50 | R2 (narrow) | Comparable quality; both have clear contributions and solid evaluations |
| Judge Decoding (Oral) | 8.00 | R1 (strong) | Breakthrough-level contribution — LCG is not at this level |

**Scoring rationale:** The paper sits above the 6.0-level papers (TA-ITI, SASA, RAIN) because it has a well-motivated mechanistic analysis, cleaner evaluations across more models, and practical overhead measurements. It is comparable to the 6.25–6.5 papers (VocADT, DAEMON, Chunk-Distilled) but has some fixable gaps (training details not reported, pseudo-targets not validated, data overlap not clarified). The weaknesses are real but addressable and do not threaten the core claims. The contribution is genuine and practical.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>