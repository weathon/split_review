I have all the information I need. Let me produce the final review.

## Summary

This paper presents an RL-based macro placement method that jointly optimizes wirelength and peak temperature by extending MaskPlace with a heat mask input and a temperature-weighted reward term. It also contributes 15 open-source macro thermal placement benchmarks built from RISC-V designs through a complete EDA flow (logic synthesis with real power data). The benchmark is a genuine and reusable contribution, but the method's core claim—that joint optimization outperforms two-stage thermal-aware approaches—is not tested by the experiments, and several methodological gaps undermine the reported results.

## Strengths

- **First open-source macro thermal placement benchmark with real per-component power data.** The paper constructs 15 benchmarks (80–2184 macros) by running a complete EDA pipeline: RISC-V SoC designs from Chipyard, SRAM compilation, and Synopsys Design Compiler logic synthesis at SMIC 55nm (Section 5, lines 137–145). This produces gate-level netlists with per-macro dynamic power rather than random power densities used in prior work. This is a reusable community resource that demonstrably lowers the barrier to entry for thermal-aware placement research.

- **Well-motivated joint optimization formulation.** The reward function r_t = (HPWL_{t-1} − HPWL_t) + α(Tmax_{t-1} − Tmax_t) and the heat mask input (Section 4.2, lines 126–132; Figure 2) directly implement single-step joint optimization, addressing a real limitation of prior two-stage pipelines that first optimize wirelength then adjust for temperature (Figure 1(a)). The qualitative results in Figure 4 provide visual evidence that early heat optimization spreads macros more evenly.

- **Demonstrated temperature reduction on most benchmarks.** Table 2 shows that with α=1 the method achieves the lowest max temperature on 13 of 15 benchmarks (e.g., 25.76 K reduction on HwachaRocket), and the trade-off analysis in Figure 5 explores the wirelength–temperature Pareto frontier.

## Weaknesses

### Major

1. **The central claim is untested because the evaluation lacks the appropriate baseline.** The paper's thesis is that joint optimization avoids the local optima of two-stage thermal-aware methods (Ma et al., 2021; Chiou et al., 2023), which "divide the optimization process into two steps...leading to local optima" (line 14, contribution 1 on line 27). However, the experiments compare only against **MaskPlace**—a wirelength-only method that does not optimize temperature at all. The reported "α=0" results are the authors' own architecture with the temperature term zeroed out (line 155), not an independent implementation of MaskPlace, and certainly not a two-stage thermal-aware method. The comparison therefore only shows that including a temperature term in the reward trades wirelength for temperature, which is trivial and expected. **Without comparing against a two-stage thermal-aware baseline** (e.g., optimize wirelength with MaskPlace, then apply SA-based thermal post-processing as in Ma et al.), the paper provides **no evidence** for its claimed advantage over the prior methods it criticizes. This is a structural gap in the evaluation that directly undermines the paper's core method contribution.

2. **Training procedure for large benchmarks (>300 macros) is critically underspecified, making those results uninterpretable.** The paper states: "we select 256 macros in train process then generate all macros finally" (line 155). It provides no detail on: (a) how the 256 macros are selected, (b) how remaining macros are placed at test time, or (c) whether the policy trained on a subset generalizes to the full set. The two benchmarks where the method fails to achieve lowest temperature (SbusRingNoC, MempressRocket) are attributed to this procedure post-hoc (line 157). Since 8 of 15 benchmarks have >300 macros, **a majority of the experimental results are uninterpretable**—it is unclear whether reported wirelength and temperature numbers reflect the RL-optimized portion or the uninstructed remainder.

3. **The baseline comparison conflates the method's own architecture with the cited baseline.** The paper claims to "compare with MaskPlace" (line 155), but Table 2 only reports results for α=0 and α=1—both are variants of the authors' own model. The α=0 variant uses the same architecture (heat mask, PPO framework, encoder-decoder) with only the temperature weight zeroed out. This is not a re-implementation or independent validation of MaskPlace. The comparison therefore controls for the reward weight but does not compare against a method that differs in architecture, making it unclear whether any observed differences are due to the reward change or architectural choices.

### Minor

4. **The temperature reward signal is likely sparse with no analysis provided.** The reward uses the change in *global* max temperature after placing a single macro. The global max temperature is determined by the current hottest hotspot, which is unlikely to change meaningfully when a macro is placed far from it. For most placement steps, the temperature reward will be zero, so the policy receives no learning signal about temperature for most actions. The paper does not analyze this sparsity, does not report the fraction of steps with non-zero temperature reward, and does not discuss alternative formulations (e.g., average temperature change, local temperature around the placed macro). This is a methodological gap that undermines confidence in whether temperature optimization actually drives the learned behavior.

5. **Overlap and congestion constraints are in the objective but never evaluated.** Equation 1 (lines 55–57) formalizes the placement problem as minimizing HPWL + α·MaxT subject to Overlap=0 and Congestion≤C. The experiments report only HPWL and MaxT; overlap and congestion results are absent. It is unclear whether these constraints are satisfied by construction or violated.

6. **The trade-off analysis (Figure 5, line 173) is internally inconsistent.** The paper observes chaotic results as α→1, speculates about "expansion of configuration...in phase space," and then selects α=1 as the trade-off coefficient—the very value associated with chaotic behavior. No ablation over training duration per α value is provided to distinguish genuine phase-space effects from insufficient training.

7. **Random pin placement (line 144) reduces the benchmark's realism and its conclusions may not transfer to real designs.** HPWL is computed from pin positions, and thermal distribution depends on where power is dissipated within macros. Random assignment decouples the benchmark from real chip design where pin locations are determined by standard cell libraries and floorplans. The paper does not discuss the implications of this simplification for the validity of the reported wirelength and temperature results.

8. **The method's delta from MaskPlace is modest but the paper positions it as a new model.** The method uses the same PPO framework, same masking scheme (position mask, wire mask, view mask), and same encoder-decoder architecture, with two additions: a heat mask input channel and a temperature-weighted reward term. This is not a weakness per se, but the paper would benefit from clearly scoping the contribution as an extension.

### Trivial

None.

## Nice-to-Haves

- **Construct and compare against a two-stage baseline.** This is the single highest-leverage improvement: e.g., optimize wirelength with MaskPlace, then apply SA-based thermal post-processing (translation/rotation) analogous to TAP-2.5D or Chiou et al. (2023). This directly tests the paper's central hypothesis.
- **For large benchmarks**, either train on all macros, provide ablation over subset sizes and selection strategies, or restrict evaluation to chips where full training is feasible.
- **Report overlap and congestion metrics** to verify that the constraints in Equation 1 are satisfied.
- **Analyze reward sparsity**: report the fraction of placement steps with non-zero temperature reward and consider denser alternatives (e.g., change in average temperature or local hotspot temperature).
- **Report computational cost**: number of FEA solves per placement step, total training time per benchmark, and epochs used.
- **Report results with multiple random seeds** to account for PPO training variance.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that Tables 1 and 2 are images in the parsable text** — Removed per hard rule: this is a parser artifact; the original submission has proper text tables.
- **Criticism about missing repository URL or release mechanism for the benchmark** — Removed per hard rule: do not question the availability of cited resources.
- **Criticism about writing quality (run-on sentences, missing spaces before citations, grammatical errors)** — Removed per hard rule: these are PDF-to-text parser artifacts, not author errors.
- **Criticism about lack of statistical evidence / no error bars** — Demoted to Nice-to-Have. Single-run evaluation is standard in the chip placement literature (MaskPlace and similar works); requesting it is reasonable but not a genuine weakness given field practice.
- **Strength Finder's generic strengths** ("addressed an important problem," "targeted an interesting question") — Removed as generic/superficial; they lack specific evidence anchored in the paper's content.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no observation about the method or benchmark that the paper itself does not already state or imply.

## Suggestions

1. **Add a two-stage thermal-aware baseline.** This is the single most important experiment needed to substantiate the paper's core claim. Without it, the contribution reduces to "MaskPlace with a temperature term," which is a much narrower point than claimed.
2. **Clarify the 256-macro training procedure** for large benchmarks: specify selection criteria, test-time placement of remaining macros, and provide ablation studies validating the approach.
3. **Report overlap and congestion results** to verify the constraints in Equation 1.
4. **Analyze the sparsity of the temperature reward** and consider whether denser alternatives would provide a stronger learning signal.

## Score and Decision

The benchmark contribution is genuine and valuable, but the method contribution is inadequately supported. The paper's central claim (joint optimization beats two-stage thermal-aware methods) is untested—the evaluation compares only against a wirelength-only baseline, the training procedure for large benchmarks is underspecified, and several methodological concerns are unaddressed. As presented, the evidence does not support acceptance at ICLR.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>