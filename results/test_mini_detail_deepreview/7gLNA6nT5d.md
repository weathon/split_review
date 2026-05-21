Now I have all the information needed to write the consolidated review. Let me compose it.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
// List only reasonable points. Rank by severity.
// Not every paper has weaknesses at every tier. Leave a tier empty (or write "None") if nothing qualifies.

### Fatal

### Major

### Minor

### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

Score and Decision.

---

Let me consolidate my analysis.

**Round 1 bracket:** The paper sits between 4 and 7.

**Round 2 narrowing:** Comparison with anchors:
- Memory-Efficient AD (5.50, Reject): This paper has stronger novelty and better experiments → current paper is stronger
- DICP (6.67, Accept): Similar quality, slightly cleaner experimental design → current paper is slightly weaker
- Actions Speak Louder (4.75, Reject): Had major conceptual flaws → current paper is much stronger

**Final score: 6.0, Accept**

Now writing the full review.## Summary

This paper integrates n-gram induction heads (from Akyürek et al., 2024) into transformers trained via Algorithm Distillation (AD) for in-context reinforcement learning. The core idea is to hardcode n-gram matching attention patterns to provide an inductive bias that reduces data requirements and hyperparameter sensitivity. Experiments across Dark Room, Key-to-Door, and Miniworld (image-based) environments show that the n-gram method matches or outperforms AD, particularly in low-data regimes, and extends to visual observations via vector quantization.

## Strengths

- **Novel adaptation of n-gram induction heads to ICRL.** While n-gram induction heads were previously studied in language modeling (Akyürek et al., 2024; Edelman et al., 2024), this paper is the first to apply them in a decision-making / ICRL setting. The connection — that transformers in ICRL suffer from the same simplicity bias as in language modeling, and that hardcoding n-gram patterns can mitigate this — is well-motivated and non-trivial. The method is clearly described (Section 2.2, Equations 1–3).

- **Data efficiency is convincingly demonstrated within the paper's own framework.** Figure 4 shows that with 100 training goals in Key-to-Door, the n-gram method reaches near-optimal return (~1.9) while the baseline AD plateaus at ~1.3 under identical conditions (same 100 goals, same 500/750/1000 histories). This is a controlled within-experiment comparison that directly supports the claim that n-gram heads improve data efficiency.

- **Reduced hyperparameter sensitivity is well-supported.** Figure 2 shows that in Dark Room with 1K histories, the n-gram method reaches optimal performance in ~20 hyperparameter assignments versus >400 for the baseline. The use of Expected Maximum Performance (EMP) following Dodge et al. (2019) is a principled evaluation protocol that avoids cherry-picking and provides a fair comparison of training difficulty.

- **Extension to visual observations is a genuine technical contribution.** Section 2.3 describes how vector quantization enables n-gram matching on pixel observations (Miniworld), and Figures 5–6 show significant improvements over the baseline in this setting. This goes beyond prior n-gram work restricted to discrete/text domains.

- **Ablation studies provide useful sanity checks.** Table 1(c) shows that a permuted (random) n-gram attention mask yields EMP 0.51 ± 0.03, statistically indistinguishable from the baseline without n-gram layers (0.52 ± 0.02). This demonstrates that inserting the layer does not harm performance when the matching mechanism is unreliable, and strongly suggests the benefit comes from the inductive bias rather than added parameters alone. Table 1(a,b) further shows low sensitivity to n-gram length and layer position.

## Weaknesses

### Major

- **Model capacity is not explicitly controlled.** The paper states it "include[s] an n-gram attention layer as one of the transformer layers" (Section 2.2) and ablates positions [1], [2], [1,2] (Section 4.4), but never clarifies whether this *replaces* an existing layer or is *added* as an extra layer. The N-Gram Layer (NGL) defined in Equation 3 includes both an attention mechanism and an MLP, constituting a full transformer layer. If inserted rather than swapped, the n-gram model would have greater depth and parameter count than the baseline. **However**, the permuted-mask experiment (Table 1c) mitigates this concern — if extra capacity alone were responsible, the permuted NGL (same added parameters) should also outperform the baseline, but it does not (0.51 vs. 0.52). The authors should clearly state whether the NGL replaces or augments existing layers, and ideally provide an ablation that controls for parameter count (e.g., adding the same number of parameters to the baseline via an extra MLP).

- **The 27× data-efficiency claim is not directly demonstrated within the paper's experimental framework.** The paper claims "27x less data" by comparing its n-gram model trained with 100 goals + histories to the original AD paper's configuration of 2048 goals + 2048 histories (Figure 4 caption, Appendix B). This is a cross-paper comparison: the environments, task distributions, data-generation procedures, and evaluation protocols may differ. **The core result is still valid** — Figure 4 clearly shows the n-gram method outperforming the baseline under identical 100-goal conditions — but the precise 27× multiplier is an extrapolation, not a controlled measurement. The authors should either demonstrate this multiplier directly within their own framework (e.g., train the baseline at multiple data scales to find the crossover point) or temper the claim to "up to ~27× relative to the original AD paper's reported requirements" and clarify the nature of the comparison.

### Minor

- **Training conditions for Table 1 ablations are not specified.** Table 1 reports EMP values around 0.7 for n-gram variants in Miniworld-Dark, while Figure 5 shows the n-gram method reaching EMP ~0.95 in the same environment. These are clearly different experimental conditions (likely different numbers of goals/histories), but the paper does not state what conditions Table 1 was run under. This makes it impossible to reconcile the two sets of numbers and limits the informativeness of the ablations. The authors should report the data conditions for each ablation and explain any discrepancies.

- **Miniworld-Dark experiment uses mismatched training goals (Figure 6, left).** The n-gram model is trained on 50 goals while the baseline is trained on 60 goals. Since the baseline has *more* training data, this actually makes the comparison harder for the proposed method (understating the improvement), so it is not an unfair comparison — but it is methodologically sloppy and should be fixed. Both methods should be trained on the same number of goals for a clean comparison.

- **The two n-gram matching variants (states vs. \([s, a, r]\)) are not adequately compared.** The paper tests matching on full transitions `(s, a, r)` and on states `(s)` only, but the `(s, a, r)` variant consistently underperforms the states variant (Figures 2, 4). The paper does not explain why or provide guidance on when each variant is appropriate. This is a minor gap in the methodology discussion.

### Trivial

- The VQ model details (codebook size, VQ training procedure) used for image-based observations are not specified in the main text. These are minor implementation details but would aid reproducibility.

## Nice-to-Haves

- **Train both methods on identical goals** in the Miniworld-Dark experiment (Figure 6, left) to tighten experimental hygiene.
- **Include longer training runs** to confirm that the baseline's poor performance in some settings (e.g., Key-to-Door with 100 goals) is not an artifact of the fixed 10K gradient step budget.

## Removed Points

The following points from the input reviews were removed with justification:

1. **"Hyperparameter sensitivity conflates search speed with achievable performance"** — The paper's claim is about making search quicker, which is supported by Figure 2. The fact that the baseline never catches up does not undermine this claim; it is a finding the paper already reports, not a conflation.
2. **"No confidence intervals for main results"** — Figure 6 includes shaded confidence intervals, and Table 1 reports standard deviations. The EMP metric by design aggregates over multiple runs.
3. **"Hyperparameter search details missing from main text"** — These are deferred to Appendix C (standard practice); the paper explicitly states "The exact hyperparameter assignment setups are shown in Appendix C" (Section 3.2).
4. **"N-gram in language context taken out of context"** — The paper clearly cites these results to motivate the general claim about n-gram heads reducing perplexity; the connection to ICRL is explicitly argued as a hypothesis, not presented as proven.
5. **"Mismatched goals makes comparison unfair"** — As noted above, the baseline has *more* goals, so the comparison favors the baseline, not the proposed method. This is a real sloppiness but does not undermine the result.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any perspective on the work that the paper itself does not already articulate.

## Suggestions

1. **Clarify the architecture.** State explicitly whether the N-Gram Layer replaces or is added to existing transformer layers. If added, control for parameter count (e.g., add a comparable MLP-only layer to the baseline) to isolate the effect of the n-gram inductive bias.
2. **Ground the 27× claim within the paper's own experiments.** Train the baseline at multiple data scales (e.g., 500, 1000, 1500, 2048 goals) in the same environment to empirically find where it crosses the n-gram method's performance at 100 goals, replacing the cross-paper extrapolation with a direct measurement.
3. **Report ablation conditions explicitly.** For Table 1, state the number of goals, histories, and other relevant data parameters so readers can reconcile the EMP values with those in Figures 5–6.
4. **Match training goals across methods** in the Miniworld-Dark experiment (Figure 6, left) for a clean comparison.
5. **Discuss the states vs. \([s, a, r]\) matching variants.** Explain when each is appropriate and why the states variant consistently performs better.

## Score and Decision

**Calibration anchors (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Memory-Efficient AD (5iWim8KqBR) | 5.50 | 1 | Directly comparable (AD efficiency improvement). Current paper has more novel idea (induction heads vs. applying existing efficient transformers) and cleaner experiments across more domains. **Current paper is stronger.** |
| Distilling RL for In-Context Model-Based Planning (BfUugGfBE5) | 6.67 | 2 | Closely related (improving AD). That paper had slightly cleaner experimental design but was criticized for modest improvements. Current paper has more experimental hygiene concerns but shows clearer improvements. **Current paper is slightly weaker.** |
| How Transformers Implement Induction Heads (1lFZusYFHq) | 6.20 | 1 | Different contribution type (theoretical analysis). Not directly comparable in method quality. |
| Interpretable LM via Induction-head Ngram (Zq8wylMZ8A) | 6.75 | 1 | Similar induction-heads + n-gram idea but in LM domain. Received more favorable reviews. **Not directly comparable.** |
| Actions Speak Louder (b5MCteb3w7) | 4.75 | 2 | ICRL-focused paper with major conceptual flaws (providing goal states bypassing ICRL challenge). **Current paper is much stronger.** |

**Round 1 bracket:** Initial bracketing placed the paper between 4 and 7.

**Round 2 narrowing:** Comparison with the closest anchor (Memory-Efficient AD at 5.50) shows the current paper is clearly stronger due to more novel idea and comprehensive experiments. Comparison with DICP (6.67) shows the current paper is slightly weaker due to experimental rigor gaps. The final score is positioned between these two anchors, closer to the stronger one given the core contribution is well-supported.

**Final score: 6.0 — Accept**

The paper proposes a reasonable and novel idea (n-gram induction heads for ICRL), supports it with experiments across discrete and visual domains, and includes useful ablations. The main weaknesses are a lack of explicit model-capacity control (partially mitigated by the permuted-mask experiment) and an imprecise 27× claim that is not directly demonstrated. These are addressable in revision and do not invalidate the core contribution. The paper would benefit from tightening the experimental controls and grounding the headline claim in within-paper evidence.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>