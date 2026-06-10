Now let me write the final review.

## Summary

This paper proposes **progressive subnetwork training**, a stagewise framework where only subnetworks of the model are trained at each step, with subnetwork size progressively *increasing* over time. The key instantiation, **Random Part Training (RAPTr)**, randomly drops layers (via residual skip) with a scheduled increase in inclusion probability. The paper provides a theoretical stability analysis for stage transitions (using linear residual networks as an illustrative setting), demonstrates 1.2–1.33× FLOPs reduction on BERT-Base and UL2-1.6B, and reports that RAPTr improves UL2 downstream performance by 1.5% despite matching baseline perplexity.

## Strengths

- **Principled correction of a fundamental flaw in prior dropping methods.** The paper identifies that progressive layer dropping (PLD) *decreases* model capacity over training, contradicting the well-established principle that neural networks learn functions of increasing complexity (Kalimeris et al. 2019, Abbe et al. 2022). The proposed P2 principle (increasing subnetwork size across stages) is a theoretically grounded fix, not an arbitrary heuristic. The polynomial-data analysis (Section 2) formally demonstrates why this matters.

- **First theoretical analysis of loss stability at stage transitions for dropping-based training.** Section 3 provides a formal bound (Theorem 1) relating the loss gap across stages to the network's output stability under layer removal, and Lemma 1 characterizes how residual connections and layer normalization jointly yield O(1/√L) scaling of this gap in linear residual networks, while removing either component leads to Ω(1) gaps. This analysis goes beyond the informal understanding from prior work on stochastic depth.

- **Empirical validation on models up to 1.6B parameters with competitive FLOPs savings.** The paper tests RAPTr on BERT-Base (1.33× FLOPs reduction, competitive to stacking) and UL2-1.6B (1.2× FLOPs reduction, matching perplexity). Evaluating at billion-parameter scale adds credibility that the method works beyond small models.

- **Transparent limitations section.** The paper explicitly acknowledges that schedule selection is not well understood, the downstream improvement is unexplained, and the observed loss decrease at transitions is not accounted for theoretically. This honesty strengthens the paper's credibility.

## Weaknesses

### Fatal
None.

### Major

- **Schedule sensitivity criticism of stacking applies equally to RAPTr.** The paper motivates RAPTr by arguing stacking methods "are sensitive to stacking schedules and require careful tuning" (line 19). Yet the limitations section concedes "schedule selection is not well understood due to expensive compute necessity and deserves more exploration" (line 219). Both methods require heuristic schedule tuning; the paper provides no evidence that RAPTr's schedules are more robust or easier to set. This undercuts a central motivation for the proposed approach over stacking.

- **The downstream improvement — the paper's most striking result — is presented as a contribution but left entirely unanalyzed.** The abstract (line 6) and contribution list (line 54) highlight that RAPTr "improves QA tasks and SuperGLUE by 1.5%" and "provides evidence of better inductive bias." However, the limitations section (line 219) admits that the paper "does not explain" this effect. There is no hypothesis, ablation, diagnostic experiment, or analysis of *why* random subnetwork training would improve downstream performance while perplexity stays flat. Without this, the claim of "better inductive bias" is an empirical observation without characterization — it is impossible to tell whether the improvement is robust, replicable, or an artifact of a particular schedule/evaluation setup. Furthermore, the visible text does not report how the 1.5% figure is computed (average? median? best across tasks?), the consistency across the 12 benchmarks, or the number of seeds used.

- **The theoretical contribution is narrower than the "first theoretical basis" framing suggests.** The paper claims to establish the "first theoretical basis for stagewise training based on dropping of layers" (lines 58, 132). In reality, the core formal result (Lemma 1) is derived for *linear residual networks at random initialization* — a setting that omits attention mechanisms, nonlinear activations, and learned weights that move far from initialization. The paper acknowledges this as an "illustrative example" (line 171), but the framing of the contribution (contribution list item 5, line 58) does not reflect this limitation. Assumption 1 (Relative-Lipschitzness) is stated without verification or reference for the transformer setting; Theorem 1's bound depends on this unverified assumption. The paper's theoretical contribution is real but modest, and the gap between what is proved (linear networks at initialization) and what is claimed (basis for stagewise dropping in transformers) is substantial.

### Minor

- **Insufficient experimental transparency for the downstream results.** The abstract cites "a suite of 12 downstream benchmarks" but the visible text only names "QA tasks and SuperGLUE" without per-task breakdown, effect size variance, or seed information. While some of these details may reside in the appendix (which the parser strips), the main text should include basic information about variability and consistency.

- **The theoretical analysis assumes uniform subnetwork selection** (line 154: $\mathcal{L}_1(F) = \frac{1}{L}\sum_\ell \mathcal{L}(F_{-\ell})$), but RAPTr uses a more general schedule with fixed layers and non-uniform probabilities. The paper does not discuss how non-uniform selection affects the stability bound.

### Trivial
None.

## Nice-to-Haves

- A diagnostic analysis of the downstream improvement (e.g., which task types benefit most, correlation with subnetwork size during training, comparison to stochastic-depth baselines with matched randomness) would substantially strengthen the paper's most surprising claim.
- A sensitivity analysis for RAPTr's schedule hyperparameters ($p_s$, stage boundaries) on a smaller model would test whether the method genuinely reduces the tuning burden relative to stacking — a claim the paper currently makes but cannot support.

## Removed Points

These points were flagged by the reviewers but filtered out under the filtering rules:
- **Missing algorithm file / scaling details**: The paper uses `\input{Algorithms/layerdrop_alg}` for pseudocode and scaling. This is part of the original submission; parser-stripped content should not be criticized.
- **Missing comparison to GaLore/DoRA**: These are optimization methods, not stagewise training approaches. Requesting them is scope creep.
- **Absence of comparison to varying-schedule stochastic depth**: The paper discusses this in Related Work and distinguishes its approach. The critic's framing minimizes this distinction, but the paper does address it.
- **Pure formatting/style nitpicks**: Removed per instructions.
- **Strength about "general framework that subsumes prior work"**: This is a descriptive claim rather than a demonstrated strength; the paper states it but does not formally prove the subsumption.

## Novel Insights

None beyond the paper's own contributions. Both the harsh critic and the strength finder largely recapitulate the paper's stated claims and limitations rather than surfacing genuinely new observations about the work.

## Suggestions

1. **Tone down the theoretical framing.** Replace "first theoretical basis" with a more precise description such as "a stability analysis for dropping-based stagewise training in linear residual networks, identifying conditions under which smooth transitions occur." This would better match what Lemma 1 and Theorem 1 actually deliver.

2. **Either analyze the downstream improvement or reframe the claim.** The "better inductive bias" language in the abstract and contributions implies a systematic understanding that the paper does not have. A descriptive analysis (e.g., per-task breakdown, correlation with training dynamics, comparison to an explicit regularization baseline) would either substantiate the claim or reveal its limits.

3. **Address the schedule sensitivity tension directly.** Acknowledge that both stacking and RAPTr require schedule tuning, and provide at least a small-scale analysis showing RAPTr is comparably or more robust to schedule choices. Alternatively, reframe the motivation to focus on other advantages (anytime algorithm property, full-model parameter updates throughout).

4. **Report variance and per-task breakdown for downstream results** in the main text. A reader cannot assess the reliability of the 1.5% improvement without knowing its consistency across tasks and seeds.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>