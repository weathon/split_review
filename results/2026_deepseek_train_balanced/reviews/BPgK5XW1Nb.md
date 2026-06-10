## Summary

SPA proposes an iterative framework for LLM alignment that dramatically reduces the need for human-annotated preference data. The key idea is to derive preference labels directly from the training LLM's own logits using the DPO reward formulation (avoiding distribution mismatch from external RMs), and then refine noisy labels via a computationally free de-coupled noise detection mechanism using linear extrapolation of logits. The core result is strong: with only 3.3% of UltraFeedback's ground-truth labels, SPA achieves a 21.13% AlpacaEval 2.0 win rate, more than doubling the 10.03% of Zephyr-7B-β trained on the full 100% of the same data.

## Strengths

- **Direct logit-based preference judgment avoids distribution mismatch (Section 4.1, Eq. 7; Table 2, Figure 3)**. Instead of using a fixed external reward model that degrades as the training distribution shifts, SPA derives preference labels from the training LLM's own logits via the DPO reward. Table 2 shows SPA achieves 21.13% vs 9.46% for PairRM under identical iterative training. Figure 3 confirms the gap widens across iterations, consistent with the distribution-mismatch rationale.

- **De-coupled noise detection provides meaningful gains with zero extra computation (Section 4.2, Eq. 11; Table 6)**. The DND method linearly extrapolates between current and reference model logits to approximate a stronger model's preference confidence, requiring no additional forward passes. The ablation shows DND raises the win rate from 19.91% to 21.13% (+1.22pp) and the LC win rate from 14.41% to 15.39% (+0.98pp).

- **Achieves superior results with only 3.3% of labels compared to a model trained on 100% (Table 1)**. SPA (21.13% WR, 15.39% LC WR) clearly outperforms Zephyr-7B-β (10.03% WR, 11.75% LC WR) which uses the same base model and SFT dataset but 100% of UltraFeedback labels.

- **Generalizes across model families and seed sizes (Tables 3, 4, 5)**. SPA improves alignment on Phi-2 (2.7B), LLaMA-3 (8B), and Phi-3 (14B) with consistent gains. The method also works robustly across different random seeds and varying amounts of seed data (0.8%–10%).

- **Operates even without any seed preference data (Figure 4)**. SPA applied to Mistral-7B-instruct-v0.1 without any human-labeled preference data raises AlpacaEval 2.0 WR from 6.31% to 9.79%, demonstrating the method can extract preference signal from the model's pre-existing knowledge.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The "confidence-based self-refinement" (SR) component contributes negligibly on its own, which contradicts the paper's characterization of it as a core contribution.** The ablation (Table 6) shows that adding SR alone to the "DE only" baseline improves win rate from 19.91% to 19.94% (a 0.03pp gain) and LC win rate from 14.41% to 14.70%. These improvements are within noise range for AlpacaEval. The paper states that "the self-refinement component is a crucial factor in enhancing performance" — this overstates the evidence. The actual gains come from DND (+1.22pp WR, +0.98pp LC WR), not from SR. The paper lists SR as a separate technical contribution (Section 1), but its standalone effect is negligible.

- **The PairRM (Iterative DPO) baseline advances only from 7.68% to 9.46% across three iterations — a remarkably small gain of 1.78pp.** While the paper plausibly attributes this to distribution shift (and provides Figure 3 as supporting evidence), the magnitude is striking enough that a stronger baseline incorporating periodic reward model retraining (a common practice in iterative RLHF pipelines, e.g., Dong et al., 2024) would be a natural and informative comparison. Without it, readers cannot assess how much of the advantage over PairRM comes from SPA's intrinsic logit-based judgment versus PairRM being used in a configuration that is known to degrade under distribution shift. This does not invalidate the paper's results, but it limits the conclusiveness of the PairRM comparison.

### Trivial
- The paper states in Section 5.2 that "the length-control win rate is also improved (9.03% → 15.39%)" for DPO → SPA, but in Table 1, DPO with 3.3% gold labels achieves a 9.03% LC win rate, consistent with this. Good — no formatting issues of substance.

## Nice-to-Haves
- Include a baseline where the reward model (PairRM) is periodically retrained during iterative DPO, which is standard in industrial iterative RLHF pipelines. This would strengthen the claim that SPA's advantage is inherent, not an artifact of a suboptimal baseline configuration.
- Study behavior beyond 3 iterations: does the method plateau, continue improving, or risk collapse?
- Provide a direct analysis of DND's accuracy in identifying noisy labels (e.g., compare its noise detection against ground-truth noise labels in a synthetic noise setup).

## Removed Points

1. **Harsh critic's claim that the SPA–PairRM gap is "suspiciously large" and may be due to suboptimal PairRM setup** — REMOVED. The paper provides a clear, well-reasoned explanation (distribution shift) and supporting evidence (Figure 3 shows the gap is small at iteration 1 and widens at iteration 2). The speculation that PairRM was "run in a suboptimal way" is not grounded in any specific error identified in the paper. The critic's request for "reward model retraining" goes beyond the standard setup for this baseline class. This concern was demoted to a Minor weakness above, reframed as a missing baseline rather than a criticism of the existing experiment.

2. **Harsh critic's truncation of the ablation analysis** — The critic's text cuts off mid-sentence showing only partial data. The complete Table 6 data was verified and used correctly.

## Novel Insights

None beyond the paper's own contributions. A useful observation that emerges from cross-referencing the reviews and the paper: the primary technical novelty is really the direct logit-based judgment (Contribution 1) plus DND (Contribution 3), while the standalone confidence-based refinement (Contribution 2) adds essentially nothing. The paper would be strengthened by reframing contributions around the two-component pipeline (direct judgment + DND-enhanced refinement) rather than presenting three co-equal components.

## Suggestions

- Reframe the contributions to accurately reflect the ablation evidence: DND is the effective denoising mechanism, while standalone confidence-based SR provides negligible benefit. Distinguish the two more clearly in the contribution list.
- Include an Iterative DPO + PairRM baseline with periodic RM retraining (the standard RLHF pipeline) to strengthen the comparison.
- Add error bars or confidence intervals to key results (Tables 1, 2, 6) to contextualize the magnitude of improvements, especially for small deltas like the SR-only gain.

## Score and Decision

MY FINAL SCORE: <score>8</score>
MY FINAL DECISION: <decision>Accept</decision>