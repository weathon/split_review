Now I have all the data I need. Let me compile my final review.

Key observations:

**Length confound analysis:**
- GPT-4-turbo LC Win Rate (the only LC metric available):
  - SPPO 2B iter 3: BT=38.86, GPM=35.30 → BT wins
  - GPO 2B iter 3: BT=38.79, GPM=38.51 → basically tied
  - SPPO 8B iter 3: BT=40.55, GPM=39.72 → BT slightly wins
  - GPO 8B iter 3: BT=42.16, GPM=41.19 → BT slightly wins
- The raw win rate improvements in Table 3 (GPT-4o-mini) and Table 5 (DeepSeek-V2) show large margins but GPM consistently produces longer outputs. The paper explicitly notes LC Win Rate is only available for GPT-4-turbo.
- The abstract claims "margins up to 9.3%": this comes from GPO 2B iter 3 (77.11 vs 67.81 raw win rate with GPT-4o-mini), yet the LC win rate (the length-controlled metric) shows no consistent advantage.

**Parameter capacity confound:**
- BT RM has embedding dim=1 (essentially a scalar), while GPM uses dims 2,4,6,8. The best GPM (dim 8 at 2B) has significantly more parameters in the preference head. This is a legitimate concern, though the paper does ablate across dimensions.

**GPO log Z=0:**
- Line 305 shows the footnote justification: "In late stages of the iterative training, π_θ_t is close to equilibrium so the preference model can not distinguish between policy π_θ and the opponent policy π_θ_t (meaning ŝ(y ≻ π_θ_t | x) ≈ 0). Therefore, log Z ≈ 0." This is indeed a heuristic approximation applied at all iterations 1-3, not just late stages.

**E[s] vs E[P]:**
- The paper acknowledges this difference in line 287-288: "we would like to point out that this formulation is different from... as they consider maximizing the win rate P(y≻y'|x), while our formulation is to maximize s(y≻y'|x) = log[P/(1-P)]" and notes "The flexibility in its value range might benefit fine-tuning."

Now let me write the final review.

## Summary

The paper introduces General Preference representation Modeling (GPM), which embeds responses into a latent space and models pairwise preferences via a skew-symmetric operator, achieving O(K) query complexity while expressing intransitive preferences. It also proposes General Preference Optimization (GPO), a policy optimization method using preference scores instead of probabilities. Experiments show GPM outperforms BT reward models on RewardBench (+5.6%), models cyclic preferences perfectly, and yields downstream improvements on AlpacaEval 2.0 (up to 9.3% raw win rate) and MT-Bench.

## Strengths

- **Principled theoretical framework**: The skew-symmetric preference operator construction (Section 4) is clean, with BT correctly derived as a special case (k=1) and Theorem 1 establishing full expressiveness for any skew-symmetric preference matrix. The guaranteed skew-symmetry (s(yi≻yj) = −s(yj≻yi)) eliminates the positional asymmetry problem of PairPM approaches without data augmentation.
- **Genuine O(K) efficiency advantage**: Unlike PairPM methods requiring O(K²) forward passes, GPM computes one embedding per response and evaluates all pairs via inner products. This is a real, architecturally meaningful efficiency gain for test-time scaling with large response sets.

## Weaknesses

### Fatal
None.

### Major

- **Length confound undermines headline downstream claims** — The abstract claims "margins up to 9.3%" on AlpacaEval 2.0, drawn from raw win rates (e.g., Table 3: GPO 2B iter 3, GPM 77.11% vs BT 67.81%). However, GPM models consistently produce longer outputs (e.g., iter 3: 2613 vs 2245 tokens for 2B GPO), and AlpacaEval is well-known for length bias. The paper itself provides length-controlled (LC) win rates for the GPT-4-turbo evaluator (Table 4), where the picture reverses: for SPPO 2B iter 3, BT RM achieves LC WR 38.86 vs GPM's 35.16; for SPPO 8B iter 3, BT gets 40.55 vs GPM's 39.72; for GPO 8B iter 3, BT achieves 42.16 vs GPM's 41.19. On the sole length-controlled metric available, GPM does not consistently outperform BT, and the large raw win-rate gains may be largely explained by output length. The paper does not discuss this discrepancy and continues to claim "substantial improvements" in the abstract and conclusion without qualification. This significantly weakens the empirical case for downstream alignment quality.

- **GPO formulation sets log Z = 0 as a practical approximation without validation** — The partition function log Z_{π_θ_t}(x) (Eq. 12) is set to zero in practice (footnote, line 305) with the justification that in "late stages" preferences approach equilibrium so ŝ≈0 and Z≈1. However, results are reported from iterations 1–3, and no analysis or ablation verifies that this approximation is benign at these early iterations. Additionally, the GPO objective maximizes E[s] (preference score) rather than E[P] (preference probability), and the paper acknowledges this is different from prior work (line 287) but does not formally establish that this objective converges to the von Neumann winner or any specific equilibrium. These two unverified approximations together mean the theoretical-to-practical bridge in Section 5 is incomplete.

### Minor

- **RewardBench comparison confounds preference representation with parameter capacity** — BT RM uses embedding dim 1 while the best GPM uses dim 8, meaning the preference head has roughly 8× more learnable parameters. The RewardBench improvements (+5.6% at 2B) may partly reflect increased model capacity rather than the intransitive expressiveness of the representation. A parameter-matched BT baseline (e.g., a wider MLP head) would strengthen this comparison, though the ablation across dims 2/4/6/8 provides partial evidence.

- **Cyclic preference experiment validates theoretical capability on synthetic data only** — The 100% accuracy on cyclic preferences (Section 6.1) confirms Theorem 1's expressiveness claim, but the cycles are artificially imposed via different evaluation metrics. That BT fails on data designed to be intransitive is expected. The paper does not measure whether real training data (Skywork) exhibits intransitive structure that GPM exploits, limiting practical significance of this result. The paper's own limitation section acknowledges this partially (line 543–545).

- **Non-monotonic RewardBench performance with embedding dimension** — Table 2 shows that increasing dim does not consistently improve performance (e.g., 2B Chat: dim 8→71.5, but.dim 4→63.1; Reasoning: dim 4→81.0, but dim 6→76.7). The paper's ablation discussion states "increasing the embedding dimension generally improves performance" (line 403), which oversimplifies the actual pattern. Higher dim can hurt, possibly due to overfitting on 80K training samples, which the paper does not analyze.

- **MT-Bench improvements are marginal** — Across configurations, MT-Bench improvements are typically 0.1–0.4 points. For 8B GPO iter 3, GPM scores 7.93 vs BT's 7.94 (Table 6)—effectively identical. The paper does not claim large MT-Bench gains, but the inconsistency with the AlpacaEval narrative is notable.

## Trivial
None.

## Nice-to-Haves

- Measure intransitivity rates in the Skywork training data or RewardBench to quantify how much GPM's expressiveness is actually utilized on real data.
- Ablation of the log Z = 0 approximation in GPO (even log Z estimated via sampling) to assess its impact.
- Comparison against a PairPM-style model on RewardBench despite its O(K²) cost, to provide an expressiveness-efficiency tradeoff benchmark.
- Visualization of learned preference representations (e.g., projecting dim-2 embeddings) to show whether interpretable cyclic or intransitive structure emerges.

## Removed Points

- **Critic's claim that PairPM's asymmetry is stated "without evidence"** — The paper provides specific reasoning (line 141) about position encoding and causal attention causing asymmetry. This is a known architectural property, not an unsupported claim.

- **Critic's demand for comparison against ArmoRM, Eurus-RM, or other strong reward models** — These are different model families trained on different data. The paper's comparison is against BT RM trained on identical data with the same base model, which is the right controlled comparison for isolating the effect of the preference representation.

- **Critic's claim that "BT RM actually outperforms GPM at every iteration for 2B models"** — This is true for SPPO 2B on LC WR, but not for GPO 2B iter 3 (BT=38.79 vs GPM=38.51, nearly tied). The broader point about LC WR advantage disappearing is valid (kept above), but the sweeping "every iteration" claim is inaccurate for some cells.

- **Strength Finder's claim about "substantial improvements on AlpacaEval"** — Conflicts with the verified length confound weakness. Moved to removed points.

- **Demand for DPO/IPO experiments** — The paper's claim of integration with other methods (Remark, line 312) is speculative without experiments, but this is a nice-to-have rather than a core flaw since the paper's main experiments (SPPO and GPO) are sufficient to demonstrate the approach works.

## Novel Insights

The paper identifies an important design point in the preference modeling literature: can we achieve PairPM-level expressiveness at BT-level efficiency? The skew-symmetric operator construction is a genuine structural contribution here. However, the empirical narrative is weakened by the tension between raw win rates (which favor GPM due to length) and length-controlled win rates (which show parity or slight BT advantage). This suggests that GPM's primary demonstrated benefit may be efficiency (O(K) vs O(K²)) and theoretical expressiveness guarantees rather than raw alignment quality gains—still a valuable contribution, but one the paper does not position honestly.

## Suggestions

- Report LC win rates for all evaluators, not just GPT-4-turbo, or at minimum discuss why length-controlled metrics tell a different story than raw win rates and temper the "9.3%" claim accordingly.
- Add a parameter-matched BT baseline on RewardBench to disentangle representation expressiveness from model capacity.
- Provide an ablation of log Z = 0 in GPO, even just comparing GPO with a sampled estimate of Z.

## Score and Decision

The theoretical framework is sound and the O(K) efficiency is a real contribution. However, the headline empirical claim of "up to 9.3% improvement" is misleading because it relies on length-biased raw win rates while the length-controlled metric shows no consistent advantage. The GPO formulation has two unvalidated approximations (log Z = 0; maximizing E[s] vs E[P]). The RewardBench gains have a parameter capacity confound. These are significant but not fatal—the O(K) efficiency advantage, the skew-symmetric construction, and the theoretical expressiveness guarantee stand on their own. The paper needs its claims tempered and additional ablations, not a fundamental redesign.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>