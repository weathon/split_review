## Summary

This paper integrates n-gram induction heads (from Akyürek et al.) into the Algorithm Distillation (AD) framework for in-context reinforcement learning (ICRL). It proposes two matching strategies for RL sequences (state-only and full-transition matching) and a vector quantization pipeline to extend n-gram matching to pixel observations. The work aims to improve data efficiency and reduce hyperparameter sensitivity in ICRL. Results on Dark Room, Key-to-Door, and Miniworld environments show that the n-gram modification can outperform standard AD, particularly in low-data regimes.

## Strengths

1. **Quantified reduction in hyperparameter search cost.** Section 4.1 (line 171) reports that with 1K learning histories, the n-gram model finds optimal hyperparameters in ≈20 random assignments versus the baseline requiring >400 — a ≈20× measured improvement. This is a specific, directly measured comparison against the re-implemented baseline under identical conditions.

2. **Controlled ablation confirms n-gram layers do not harm baseline performance.** Section 4.5 (Table 1(c)) shows that a permuted n-gram mask achieves EMP 0.51±0.03 vs. baseline 0.52±0.02 — essentially identical. This control rules out the concern that the extra parameters from the n-gram layer degrade performance when the matching mechanism is ineffective.

3. **Extension of n-gram matching to pixel observations via VQ.** Sections 2.3 and 4.3 describe a non-trivial adaptation: using a pretrained VQ-VAE to quantize images into discrete codebook indices for n-gram matching. Results in Miniworld (Figure 5) show the n-gram model achieving near-optimal return (0.96) where the baseline saturates substantially lower. This goes beyond the discrete-state setting for which n-gram heads were originally designed.

4. **Systematic evaluation protocol.** The paper uses random hyperparameter search with the Expected Maximum Performance (EMP) metric (Section 3.2), avoiding cherry-picking and fixing batch size and gradient steps to ensure equal data usage across methods.

## Weaknesses

### Fatal
None.

### Major

1. **The headline 27× data efficiency claim rests on a cross-paper comparison, not a controlled experiment.** The paper asserts (lines 45, 129, 179) that the method needs 27× less data than AD, comparing their configuration (100 goals, 500–1000 learning histories) against the performance *reported* by Laskin et al. for AD at 2048 goals and 2048 learning histories. This is not a controlled re-implementation: the authors' own re-implemented baseline in Figure 4 plateaus at ≈1.3 return at this scale, while AD's original paper reported near-optimal performance at 2048 goals. The claimed factor therefore conflates the actual improvement of n-gram over the re-implemented baseline with a cross-paper comparison at vastly different data scales. The 27× figure as stated is uninterpretable without a direct, controlled comparison at multiple data scales. (The paper defers justification to Appendix B, which the parser strips; however, the core concern is the experimental design, not a missing appendix.)

2. **Unequal training conditions in the Figure 6 hyperparameter sensitivity experiment.** In the Miniworld-Dark panel (Figure 6, left), the n-gram model is trained on **50 goals** while the baseline is trained on **60 goals** (line 195). The caption states this asymmetry without any justification. If the goal is to compare hyperparameter sensitivity, both methods should be trained on identical conditions. Using fewer goals for the proposed method introduces an uncontrolled advantage that undermines the comparison.

### Minor

1. **Only a single baseline (Algorithm Distillation) is compared against.** The paper cites Lee et al. [18] (another ICRL approach), data augmentation [14], and retrieval-augmented methods [26] in the related work, but includes none as baselines. With only one baseline — which the authors re-implement and which shows notably weaker performance than reported in the original AD paper — the evidence cannot distinguish whether n-gram heads specifically drive improvement, or whether any architectural modification adding parameters or inductive bias would produce similar gains at this scale.

2. **The "states" vs. "[s, a, r]" matching disparity is not analyzed.** Figure 4 shows that matching only states dramatically outperforms matching full (s, a, r) triples (by ≈0.3 return), a gap nearly as large as the gap between n-gram and baseline. This suggests the benefit may come largely from simple state-matching (a 1-gram memory: "has this state been visited before?") rather than from higher-order n-gram patterns. The paper does not analyze why state-matching works so much better, nor test whether a simpler form of hardcoded state-memory (e.g., a recurrent state cache) would achieve similar gains.

3. **EMP values in ablation tables are inconsistent with main results and unexplained.** Table 1(a) and 1(b) report EMP values of 0.67–0.76 for the n-gram model in Miniworld-Dark, while Figure 5 shows the same method reaching ≈0.96 near-optimal performance in the same environment. The paper does not specify the data conditions (number of goals, learning histories) for the ablation experiments or explain why performance is so much lower.

4. **VQ pretraining resource cost is not accounted for.** The paper states that a ResNet encoder-decoder with VQ bottleneck is "pretrained to reconstruct the input image" (line 97) but does not specify the pretraining dataset size, whether it overlaps with the ICRL training data, or the additional compute cost incurred. Since the paper's headline claim is about data efficiency, the resources consumed by VQ pretraining should be factored in.

5. **Figure 2 curves lack confidence intervals.** The paper reports striking differences in HP search efficiency (≈20 vs. >400 assignments) without uncertainty quantification, making it difficult to assess variance in the EMP estimates.

### Trivial
None.

## Nice-to-Haves

- Add at least one additional baseline — a simple recurrent model (e.g., LSTM trained on the same data) or another ICRL method (Lee et al. 2023 or a retrieval-augmented approach) — to strengthen the claim that n-gram heads specifically are what help.
- Run a fully controlled data-efficiency comparison with both methods trained on identical datasets at multiple scales (e.g., 100, 250, 500, 1000, 2000 goals) to directly quantify the data efficiency gain without cross-paper reliance.
- Analyze why state-matching outperforms full-transition matching, and test whether a simpler hardcoded state-cache baseline replicates the n-gram advantage.
- Report confidence intervals on all main EMP figures.
- Disclose VQ pretraining dataset details and account for its resource cost.

## Removed Points

These points were flagged for removal; treat with caution if examining raw reviewers.

- **Appendix availability issue** (from Harsh Critic Weakness 1): The critic noted that the 27× justification is in Appendix B which was "not available." Removed per the rule that the parser strips appendix sections; they exist in the original submission. The core concern about cross-paper comparison design is retained in Major weakness 1.
- **"Transitivity" typo**, **"Minigrid" vs. "Miniworld" naming**: Removed as formatting/text issues.
- **Connection between motivation and evidence being loose** (Harsh Critic "Section-by-Section Notes"): Removed as too general without a specific anchor.
- **Differential sensitivity to data collection structure** (Experiment Setup note): Removed as scope creep — the paper is not required to analyze this for its core claims.
- **"Section 4.3 is the weakest contribution claim"**: Removed as an opinion without a specific evidentiary anchor.
- **Strength Finder generic strengths**: No generic strengths were present in the Strength Finder output; all four listed strengths were specific and anchored in the paper.

## Novel Insights

None beyond the paper's own contributions. The reviews usefully pressure-test the paper's empirical claims but do not contribute novel observations about the methodology or results.

## Suggestions

1. **Run a fully controlled data-efficiency experiment** where both n-gram and AD are trained on identical datasets at multiple scales (e.g., 100, 250, 500, 1000, 2000 goals) in the same environment, using the same data generation pipeline. This would directly quantify the data efficiency gain.
2. **Equalize training conditions in Figure 6** — train both methods on the same number of goals.
3. **Add at least one additional baseline** — a simple recurrent model (LSTM) or another ICRL approach (Lee et al. 2023, retrieval-augmented methods).
4. **Analyze why state-matching outperforms full-transition matching**, and test whether a simpler state-cache baseline achieves similar gains.
5. **Report confidence intervals on all main EMP figures** (Figures 2, 4, 5).
6. **Disclose VQ pretraining dataset details** (size, overlap with ICRL data, compute cost).

## Score and Decision

### Calibration

**Round 1 — Bracketing (all queries run in parallel):**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| Demonstration Distillation for ICL (Y8DClN5ODu) | 3.40 | R1 | Weaker — had more fundamental framing issues |
| Continual RL with Language Inference (zEhTnQZB3D) | 2.33 | R1 | Weaker — poor clarity, limited contribution |
| EReLELA (7ienVkNf83) | 3.00 | R1 | Weaker — limited evaluation |
| Inductive Transformers (NSBP7HzA5Z) | 3.00 | R1 | Weaker — speculative, small-scale |
| ICL and Occam's Razor (2PKLRmU7ne) | 5.60 | R1 | Comparable — interesting theory but theory-experiment gaps; rejected |
| Functional Gradients for ICL (uqLQjtSdFN) | 3.57 | R1 | Weaker — narrow analysis |
| Mechanistic Basis of Data Dependence (aN4Jf6Cx69) | 4.50 | R1 | Comparable — very split reviews (1,1,8,8) |
| In-context vs. In-weight Learning (aKJr5NnN8U) | 6.50 | R1 | Stronger — cleaner theoretical and experimental framing; accepted |
| Context-Parametric Inversion (SPS6HzVzyt) | 8.00 | R1 | Stronger — rigorous analysis, clean experiments |
| Abstract Reasoning with Transformers (STUGfUz8ob) | 7.60 | R1 | Stronger — theoretical proofs, clean experiments |
| Training Instabilities (d8w0pmvXbZ) | 8.00 | R1 | Stronger — rigorous empirical study |
| Never Train from Scratch (PdaPky8MUn) | 8.00 | R1 | Stronger — clean empirical methodology |

**Round 1 bracket: 4.5–6.5**

**Round 2 — Narrowing within bracket:**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| Memory-Efficient AD for ICRL (5iWim8KqBR) | 5.50 | R2 | **Most directly comparable** — same problem domain, similar methodological approach. Our paper has stronger novelty (n-gram adaptation vs. using existing efficient transformers) but more evidentiary gaps (27× claim, unequal conditions). Slightly weaker overall. |
| Recurrent Linear Transformers (dALYqPm9gW) | 4.75 | R2 | Weaker — limited novelty, narrow evaluation |
| Dynamic Layer Tying (d4uL2MSe0z) | 4.50 | R2 | Comparable but very split (6,6,1,5) |
| Study of Linear Transformations (PWtx9fJqM5) | 5.00 | R2 | Weaker — modest novelty |
| Actions Speak Louder Than States (b5MCteb3w7) | 4.75 | R2 | Weaker — fundamental design issues (task conditioning confound) |
| LLMs Are In-Context RL Learners (YW79lAHBUF) | 3.75 | R2 | Weaker — limited scope |
| ReLIC (sMWkTWh2JF) | 4.67 | R2 | Weaker — strong empirically but novelty concerns |
| Is ICL Sufficient for Instruction Following? (STEEDDv3zI) | 5.67 | R2 | Stronger — cleaner experimental design |

The paper sits below the In-context vs. In-weight Learning anchor (6.50) and above the Memory-Efficient AD anchor (5.50), approximately at 5.5. The Memory-Efficient AD paper (5.50, rejected) is the closest comparison: both modify AD, both use a single baseline, both have limitations in their comparison protocols. Our paper has marginally stronger novelty (n-gram heads are a more interesting architectural adaptation than simply adopting existing memory-efficient transformers), but the 27× claim and unequal training conditions are more serious evidentiary problems than the Memory-Efficient AD paper had. The balance places the paper at the same level.

**Final score: 5.5** — The core idea (n-gram induction heads for ICRL) is promising and some results are well-supported (HP search reduction, permuted mask ablation), but the headline data-efficiency claim is not properly supported and the hyperparameter sensitivity comparison has an uncontrolled experimental asymmetry. These issues are fixable, but in the current form the evidence does not meet the bar for acceptance.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>