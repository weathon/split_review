- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 8, 5, 6
Now I have a thorough understanding of the paper and the reviews. Let me produce the consolidated final review.

## Summary

This paper proposes ToRA (Tool-integrated Reasoning Agents), which trains open-source LLMs (LLaMA-2, CodeLLaMA) to interleave natural language reasoning with programmatic tool use for mathematical problem solving. The training pipeline consists of (1) collecting GPT-4-generated interactive tool-use trajectories on GSM8k and MATH, (2) imitation learning on these trajectories, and (3) output space shaping—a correction procedure that samples valid self-generated trajectories and fixes invalid ones using a teacher model. The resulting models achieve substantial improvements across 10 mathematical reasoning datasets, with CodeToRA-34B becoming the first open-source model to exceed 50% on MATH (50.8%), surpassing GPT-4's CoT result and rivaling GPT-4 Code.

## Strengths

1. **Tool-integrated reasoning format yields large, controlled improvements.** Figure 4 (and lines 217–219) shows that when training LLaMA-2 on the same amount of MATH data, the interleaved format outperforms rationale-only by 29.0% absolute and program-only by 6.7% absolute. This controlled comparison, using the same base model and data, cleanly isolates the benefit of the format itself.

2. **Output space shaping provides consistent and nontrivial gains across model scales.** Figure 5 (and lines 234–237) demonstrates that the sampling + correction strategies together improve accuracy by 3.4% (GSM8k) and 4.0% (MATH) on average. Correction alone adds up to 4.5% without using more training data, and even the 70B model improves from 47.3% to 49.7% on MATH. The ablation design (separating sampling from correction) is clean and the gains are convincing.

3. **Competitive results on the challenging MATH dataset, beating strong closed-source baselines.** CodeToRA-34B achieves 50.8% on MATH—the first open-source model above 50%—surpassing GPT-4's CoT result (42.5%) and closely approaching GPT-4 Code (51.8%). ToRA-7B (44.6%) also exceeds the previous best open-source model WizardMath-70B by 22% absolute (lines 52–53).

4. **Strong out-of-distribution generalization on TabMWP.** While WizardMath-70B degrades relative to base LLaMA-2 on TabMWP (49.8% vs. 57.5%), ToRA-70B achieves 74.0% (line 196), demonstrating that the tool-integrated format and shaping avoid the overfitting that can plague rationale-only SFT.

5. **Detailed error analysis with manually annotated failure modes.** Table 4 (referenced at line 273) categorizes 100 failure trajectories into reasoning errors (38%), diagram misinterpretation (21%), and various tool-use issues (28%), providing concrete, actionable bottlenecks for future research.

6. **Interpretable library-usage analysis.** Figure 6 (lines 258–264) shows per-subtopic library frequencies and accuracies—e.g., sympy solvers dominate Algebra, algorithms (gcd/lcm) dominate Number Theory—demonstrating that the model learns meaningful, topic-specific tool-use strategies rather than generic code generation.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Incomplete specification of the trajectory-correction search process.** Section 2.3 (lines 140–143) states that the algorithm enumerates "possible preceding portions" of wrong trajectories and uses a teacher model to complete them, but does not specify: (a) how many prefixes are evaluated per invalid trajectory, (b) whether there is a maximum prefix length, or (c) the computational cost of this enumeration. This is a genuine reproducibility gap for the correction step, though the overall pipeline remains reproducible with reasonable effort.

### Trivial
None.

## Nice-to-Haves

- **Deeper qualitative analysis of diversity from output space shaping.** The paper demonstrates that shaping improves accuracy (Figure 5) but does not characterize *how* the sampled/corrected trajectories differ qualitatively from the original GPT-4 trajectories. A few illustrative examples of corrected reasoning paths would strengthen the motivational narrative for the correction step.
- **Exploration of multi-sample decoding at test time.** All main results use greedy decoding (line 159). Since output space shaping encourages trajectory diversity, testing whether majority voting or Best-of-N further improves results would be a natural follow-up.
- **Positioning relative to additional tool-use methods.** The paper compares to Toolformer (line 184) and a broad set of rationale/program baselines, but not to other tool-augmented approaches such as PoT (Program of Thoughts) or ART. The existing comparisons are already strong, but situating ToRA in a fuller tool-use landscape would strengthen the positioning.

## Removed Points

- **"Output space shaping is incremental novelty / effectively rejection sampling"** — The harsh critic notes this as a framing concern, but the empirical gains are real, the ablation cleanly separates sampling from correction, and the paper explicitly cites prior rejection-sampling work (RFT, Yuan et al. 2023). This is an observation about framing, not a concrete weakness. Removed as it does not identify an actual flaw.
- **"Potential train/test contamination"** — No evidence of contamination is presented, and the paper trains only on GSM8k and MATH training sets while testing on held-out portions and additional datasets. Removed as speculative.
- **Missing related works** — Removed per instructions (cannot verify existence from external sources).
- **Formatting/style nitpicks** — Removed per instructions (parser artifacts, not author errors).
- **"Missing comparison to PoT/ART"** — The paper already includes a comprehensive set of baselines; this is a scope-expansion suggestion, not a weakness that undermines the existing claims. Removed; folded into Nice-to-Haves.

## Novel Insights

The reviews' most useful synthesis is that the paper's contribution sits at the intersection of two design choices that independently matter: (a) the *format* of interleaving rationale with tool calls (ablated in Figure 4, yielding 29% improvement over rationale-only), and (b) the *correction strategy* for invalid self-generated trajectories (ablated in Figure 5, adding up to 4.5%). Neither reviewer points to a flaw in either finding. The observation that the correction step is effectively teacher-guided completion of partial trajectories is fair, but the paper's key insight is that this specific combination—imitation learning followed by shaping—produces open-source models that cross the 50% MATH threshold, which neither reviewer disputes.

## Suggestions

- In the final version, augment Section 2.3's description of trajectory correction with the specific number of prefixes tried per invalid trajectory (or the stopping criterion), the maximum prefix length, and the total computational cost. This information may already exist in the stripped appendix; if so, a forward-reference suffices.
- Consider adding 2–3 qualitative examples contrasting a corrected trajectory with its invalid original, to illustrate the types of errors the teacher model fixes.
- Add a brief statement (1–2 sentences) confirming that training and test sets from the same source (e.g., GSM8k, MATH) are the standard train/test splits, to preempt contamination concerns.
