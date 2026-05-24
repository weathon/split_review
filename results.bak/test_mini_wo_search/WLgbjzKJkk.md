Now I have all the information needed to produce the final consolidated review. Let me write it.

## Summary

CO-MOT proposes two lightweight plugins for end-to-end Transformer-based multi-object tracking: (1) **COLA** (Coopetition Label Assignment), which allows tracked objects to be assigned to detection queries in intermediate decoders while keeping the final decoder competitive to avoid trajectory redundancy, enabling detection queries to augment tracking queries through self-attention; and (2) **Shadow Sets**, which replace each query with a set of perturbed copies so all shadows in a set jointly predict the same target, providing robustness to noise and discriminative training via hardest-sample selection. On DanceTrack, CO-MOT achieves 69.4% HOTA without an external detector (comparable to MOTRv2's 69.9% which uses YOLOX), while requiring only 38% of MOTRv2's FLOPs and running 1.4× faster.

## Strengths

1. **Well-diagnosed problem with quantitative evidence.** Table 1 cleanly shows that vanilla MOTR's detection mAP drops from 66.1% (detection-only) to 42.5% (tracking+detection), and that removing tracking queries at inference recovers +18.1%. This concrete measurement establishes that tracking-query interference during inference is a genuine bottleneck, going beyond anecdotal examples.

2. **State-of-the-art end-to-end results on DanceTrack and BDD100K without an external detector.** CO-MOT achieves 69.4% HOTA on DanceTrack (Table 2a), outperforming all prior end-to-end methods (MOTR: 58.3%, MeMOTR: 67.5%) and matching MOTRv2 (69.9%) which uses an extra YOLOX detector. On BDD100K (Table 2b), CO-MOT achieves 52.8% TETA with strong association accuracy (56.2% AssocA vs MOTRv2's 51.9%).

3. **Meaningful efficiency advantage.** As shown in Figure 4, CO-MOT requires 173G FLOPs (38% of MOTRv2's 460G) and runs 1.4× faster than MOTRv2 at comparable HOTA, since it avoids an external detector. The parameter count (40M) stays similar to MOTR's baseline.

4. **Thorough component-level ablation.** Table 3a cleanly attributes gains: COLA alone adds +3.8% HOTA, Shadow Sets alone add +2.6%, combining both gives +5.4% over the 56.4% baseline. The hyperparameter sweeps (Tables 3b, 3c) explore initialization methods, shadow counts, and representative sampling strategies, providing practical design guidance.

5. **Attention weight analysis supporting the COLA mechanism.** Figure 3 shows that detection queries contribute >15% of the normalized self-attention weight to their corresponding tracking queries in decoders 4–6 (often exceeding tracking-query self-contribution), providing quantitative evidence that the proposed "coopetition" indeed yields feature augmentation between query types.

## Weaknesses

### Major

1. **Causal mechanism not directly validated.** The paper convincingly shows that tracking queries interfere with detection during inference (Table 1: removing tracking queries recovers +18.1% mAP). COLA is then proposed as a training-time mitigation. However, the paper never runs the same diagnostic on CO-MOT itself — i.e., comparing CO-MOT's mAP with and without tracking queries at inference to see whether the gap shrinks relative to MOTR. The ablation (Table 3a) and attention analysis (Figure 3) show that COLA *improves performance*, but they do not establish that it specifically *reduces the inference-time interference* that was the stated motivation. The improvement could stem from other mechanisms (e.g., additional training supervision via extra matched targets). This is a significant evidential gap in the paper's causal narrative, though it does not invalidate the method's empirical success. **Why it matters:** The paper sells COLA as addressing a specific problem (inference-time interference), but doesn't verify this causal link. Adding the diagnostic would make the story airtight; without it, the link between motivation and solution remains plausible but unvalidated.

### Minor

1. **Imprecise framing of Shadow Sets' benefit.** The abstract and contribution list claim Shadow Sets "address the hungry for positive training samples." However, the one-to-set matching strategy (Section 3.5) still assigns exactly **one** ground-truth object per set (the representative is selected via Hungarian, and other shadows share that match; line 87). The total number of positive assignments per ground-truth is 1 per set, not increased — unlike true one-to-many methods (Group-DETR, H-DETR) where the same GT is independently assigned to multiple queries. The actual benefits of Shadow Sets (which the paper does correctly describe) are: (a) robustness to prediction noise via shared supervision across perturbed copies, and (b) hardest-sample training via max-cost selection. The paper should reframe the claim to match what the design actually does.

2. **Shadow Set hyperparameter ablation uses short training.** The Shadow Set hyperparameter sweep (Table 3b, λ and φ) is conducted with only 5 training epochs and without COLA (line 171). It is possible that longer training or the presence of COLA would shift the optimal hyperparameters. The reviewer who raised this notes it is unlikely to affect the main conclusions, but it weakens the precision of the reported design choices.

### Trivial

None.

## Nice-to-Haves

- The paper could briefly justify why the noise initialization for Shadow Sets uses σ=1e-6 (e.g., "near-identity initialization allows divergence through training while avoiding convergence issues of fully random initialization").
- The paper could note that the total query count is multiplied by N_S, which may increase memory usage even if FLOPs remain similar, for completeness.

## Removed Points

1. **"Paper should report actual FLOPs/params increase for N_S=3 relative to baseline"** — The paper already reports this: Figure 4 and Section 4.5 state CO-MOT has 173G FLOPs and 40M parameters, similar to MOTR's baseline. Removed as factually incorrect.

2. **"Mention shadow-set query increase as a potential drawback"** — The paper already explicitly states in Section 3.3: "queries contain (N_T+N_D)*N_S position and embedding" and that the total number of queries is N×N_S. Already acknowledged. Removed.

3. **Various formatting/style nitpicks and speculation about missing appendix content** — Removed per hard rules (parser artifacts, not author errors). The submission is complete and formatted correctly for the venue.

## Novel Insights

The two reviewers' perspectives, when read together, surface an interesting tension: the paper's strongest diagnostic evidence (Table 1) identifies a *test-time* problem (interference between query types during inference), but the primary solution (COLA) operates *only during training*. The attention analysis partially bridges this gap by showing that training-time cooperation changes self-attention patterns, but neither reviewer fully resolves whether the benefit comes from reduced interference at test time versus simply providing richer training supervision. This tension suggests that the paper's contribution might be more accurately described as "improving detection-query representations during training so they become more useful auxiliaries to tracking queries" rather than "mitigating test-time interference" — a subtle but potentially important distinction for future work.

## Suggestions

1. **(Required for rebuttal)** Run the Table 1 diagnostic on CO-MOT: measure CO-MOT's mAP with and without tracking queries at inference, and as a detection-only model. Report whether the gap shrinks compared to MOTR. This is the single experiment that would most strengthen the paper's narrative.

2. **(Required for rebuttal)** Reframe the Shadow Sets contribution to accurately describe the mechanism: "addresses sensitivity to prediction noise and provides discriminative training via hardest-sample selection" rather than "addresses hunger for positive training samples." The design is sound; the framing just needs correction.

3. If the hyperparameter sweeps in Table 3b can be re-run with longer training (or the current limitation noted in the text), this would increase confidence in the chosen settings.

## Score and Decision

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>