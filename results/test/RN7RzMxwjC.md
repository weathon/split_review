I now have thorough verification of all claims. Let me produce the final consolidated review.

---

## Summary

This paper identifies an overlooked multi-task imbalance in world model learning for model-based RL: observation modeling dominates reward modeling under default equal-weighting (Dreamer's w_r=1), which can lead to spurious correlations and poor sample efficiency. The authors propose Harmony World Models (HarmonyWM), which introduces learnable loss weights with a rectified log(1+σ) term to dynamically balance observation, reward, and dynamics losses. Experiments on Meta-world, RLBench, and DMC Remastered show 10%–55% absolute performance gains over default DreamerV2, with generality to DreamerV3 and DreamerPro.

## Strengths

- **Novel multi-task perspective on world model learning, supported by empirical evidence of task domination.** The paper systematically analyzes world models as a multi-task learning problem (observation vs. reward modeling) and provides empirical evidence (Fig. 2, Findings 1–3 in Sec. 2.3) that default equal-weighting in DreamerV2 causes observation modeling to dominate, severely hurting sample efficiency. Simply increasing the reward loss coefficient yields dramatic improvements, revealing an oversight in prior MBRL literature.

- **HarmonyWM achieves strong empirical gains across three domains and multiple base methods.** The proposed harmonizer (Sec. 3, Eq. 5) uses learnable weights to automatically balance losses. This is validated across Meta-world, RLBench, and DMC Remastered using DreamerV2, DreamerV3, and DreamerPro, with absolute performance gains of 10%–55% (Sec. 4 intro) and up to 74% on the Push task (Sec. 4.1).

- **Concrete demonstration of spurious correlations from observation domination, with partial quantitative support.** Figure 5 (Sec. 2.3) shows a trajectory where default DreamerV2 learns a spurious correlation between robot actions and lever movement, incorrectly predicting rewards. Properly emphasizing reward modeling (w_r=100) corrects these hallucinations. Figure 4 provides quantitative evidence that emphasizing reward modeling produces representations that better predict ground-truth states.

- **Generality to multiple base MBRL methods and comparison against implicit MBRL.** Section 4.4 (Fig. 9) demonstrates that HarmonyWM improves DreamerV3 and DreamerPro, the latter outperforming its manually tuned default weight (w_r=1000). Figure 10b shows HarmonyWM outperforming the implicit MBRL method TD-MPC on Meta-world.

## Weaknesses

### Major

- **No comparison to a fixed high reward weight (e.g., w_r=100) in the main DreamerV2 experiments.** The analysis in Sec. 2.3 shows that raising w_r from 1 to 100 dramatically improves sample efficiency on Meta-world tasks (Fig. 2). Yet the main experimental results (Figs. 7–8) compare HarmonyWM only against default DreamerV2 (w_r=1). Without this baseline, the reader cannot tell whether the improvement comes from the *dynamic* aspect of HarmonyWM or simply from using a higher, well-chosen fixed weight. The generality experiments (Fig. 9) do include one comparison against a tuned weight (DreamerPro with w_r=1000), but this involves a different base architecture (reconstruction-free) and is a single point of comparison. This gap directly undermines the paper's claim that dynamic equilibrium is the key mechanism and that HarmonyWM avoids exhaustive tuning.

- **No empirical comparison to uncertainty weighting (Kendall et al., 2018).** The paper's harmonious loss is closely related to uncertainty weighting, and Sec. 3's Discussion lists conceptual differences (e.g., treating observations as a whole vs. per-pixel uncertainty, ability to handle the KL loss). However, no experimental comparison is provided. Without empirical evidence that the specific form chosen here is superior, the claimed advantage over this well-known baseline remains unsubstantiated.

### Minor

- **Incomplete theoretical justification for the rectified loss.** Proposition 3.1 characterizes the optimal σ for the *unrectified* loss (Eq. 4: log σ term), showing σ* = E[L]. However, the method uses the *rectified* loss (Eq. 5: log(1+σ) term). No analogous proposition is provided for the rectified version, and the paper does not discuss how rectification changes the optimum. While this does not invalidate the method (the rectification is motivated by practical stability), it weakens the theoretical grounding.

- **Slightly overstated novelty claim.** The paper states it is the "first time" to "systematically identify the multi-task essence of world models." The Discussion in Sec. 2.3 acknowledges that prior decoder-free MBRL work (Nguyen et al., 2021; Deng et al., 2022) manually tuned reward loss weights to high values (100 or 1000), implicitly recognizing the imbalance. The contribution is better framed as a *systematic* study and *dynamic* solution rather than a first discovery.

### Trivial

- **Spurious correlation analysis is qualitative.** The analysis in Fig. 5 (Sec. 2.3) is based on a single trajectory and is illustrative rather than quantitative. The paper would be strengthened by measuring reward prediction error or state regression accuracy across multiple seeds, though the nearby quantitative analysis in Fig. 4 partially mitigates this concern.

## Nice-to-Haves

- Ablate the rectification term by comparing the unrectified (Eq. 4) and rectified (Eq. 5) versions on tasks where stability is a concern, to demonstrate the rectification is necessary.
- Provide wall-time or parameter-count comparison to quantify the "lightweight" claim of the harmonizer.
- Extend the fixed-weight baseline (DreamerV2 + w_r=100 or a per-task tuned value) across multiple tasks in the main figures, which would directly support or qualify the claim about avoiding exhaustive tuning.

## Removed Points

- *The critic's concerns about the method being "not yet released" or "cannot be independently verified":* The paper cites existing benchmarks and methods; reproducibility concerns rooted in doubting cited entities are not valid.
- *The critic's implication that the paper's contribution is "reduced to 'up-weighting the reward loss helps,' which is already known":* This conflates problem identification with solution. The paper's identification of the imbalance in *decoder-based* world models and its proposed dynamic balancing method are substantive, even if prior decoder-free work tuned weights.
- *The critic's suggestion that the paper does not properly acknowledge prior work on the imbalance:* The paper explicitly discusses this in the Discussion of Sec. 2.3 (line 108), noting that Finding 1 "coincides with high reward loss weights manually tuned...in decoder-free model-based RL (Nguyen et al., 2021; Deng et al., 2022)."

## Novel Insights

The reviewer cross-reading reveals a pattern — several MBRL papers have quietly used high reward weights (100, 1000) without formally studying why. The key insight here is not merely that high weights help (which prior decoder-free work knew empirically), but that this practice is entangled with the architecture type: decoder-based world models (DreamerV2) suffer from observation domination more severely than decoder-free methods, yet the community had not systematically characterized the multi-task tension as a general property of world model learning. The paper's contribution is thus less about discovering the imbalance (which was used implicitly) and more about naming it, measuring its dynamics across architectures, and providing a plug-in method that works without per-task tuning. The most underexploited finding is the demonstration that even on visually simple tasks (Meta-world), observation domination hurts — this contradicts the intuition that reconstruction is harmless when the visuals are clean.

## Suggestions

1. **Add a DreamerV2 + fixed w_r=100 baseline** to the main experiments (Figs. 7–8) across all tasks where the analysis in Sec. 2.3 shows this weight helps. If HarmonyWM matches or exceeds this fixed-weight baseline, the dynamic-tuning claim is credible. If not, the contribution should be reframed around problem identification and automatic tuning rather than superior performance over a well-chosen static weight.

2. **Include an empirical comparison to uncertainty weighting (Kendall et al., 2018)** on at least one representative task per domain. Even if the result is comparable, showing that the method is at least as good while being simpler or more generally applicable (e.g., handling KL loss) would substantiate the claimed advantages.

3. **Provide a brief analysis of what the rectified loss optimizes** — even if the optimum is not as clean as in the unrectified case (e.g., a bound or a discussion of how the regularization shifts the equilibrium), this would bridge the gap between the theory and the practiced method.

4. **Tone down the "first time" novelty claim** in the contributions to better reflect the acknowledged prior work on decoder-free methods, e.g., "first systematic study in decoder-based world models" or "first dynamic balancing approach for this setting."

## Score and Decision

**Originality:** Good — the multi-task framing of world model learning is novel, though related ideas exist in prior work on loss weighting in decoder-free MBRL.  
**Importance of question:** High — sample efficiency in MBRL is a central problem, and the observation/reward imbalance is an underexplored axis.  
**Claims supported:** Partially — the problem identification is well-supported, but the claim that *dynamic* balancing is the source of improvement over *simply using a higher fixed weight* is not adequately supported by the main experiments.  
**Soundness of experiments:** Good overall but with a significant gap (missing fixed high-weight baseline in main experiments) and one missing baseline (uncertainty weighting).  
**Clarity of writing:** Clear and well-structured.  
**Value to community:** Moderate to high — the problem identification alone is useful, and the method is simple enough to be adopted by practitioners. However, the value depends on whether the dynamic aspect adds meaningful benefit over a tuned static weight, which remains unvalidated for the primary setting.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>