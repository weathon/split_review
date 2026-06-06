## Summary

This paper introduces a deletion-based probing framework for evaluating how faithfully LLMs rely on chain-of-thought (CoT) scratchpads in physics problem-solving. The authors intercept CoT traces mid-generation, apply three deletion strategies (end, random, physics-aware) across a range of fractions, and measure effects on accuracy and final-answer length. Their central empirical finding is that models maintain accuracy under 40–60% deletion while final answers grow longer ("cramming"), and that information-overlap metrics show increasing recovery of deleted physics content in final answers — from which they conclude that CoT reliance is "shallow and opportunistic."

---

## Strengths

- **Controlled deletion framework with three complementary strategies.** Sweeping deletion fractions from 0–100% via end, random, and physics-aware strategies creates a detailed and systematic picture of the accuracy-deletion relationship. Figures 4–6 and 11 consistently show the X-shaped accuracy/length pattern across all three models and three benchmarks, providing robust empirical documentation of the cramming phenomenon.

- **Cramming behavior is a genuine, reproducible finding.** The X-shaped pattern — accuracy stable until ~40–60% deletion while final-answer length rises monotonically — appears consistently across Phi-4, Qwen-A3B, and Magistral on UG Physics, PhysReason, and PhyBench. This is the paper's strongest contribution and is well-supported by evidence.

- **Calibration study establishes baseline rigour.** The convergence analysis on 50 UG-Physics questions with 5 re-runs (§3.2) justifies the sampling configuration and demonstrates methodological care before the main sweep experiments.

- **Well-motivated scope: physics as a structured testbed.** Physics problems impose precise constraints (equations, units, constants) that make token-level intervention and domain-aware deletion tractable. The physics-aware deletion strategy (using Claude-4 Sonnet to tag structured spans) is a sensible use of the domain's structure.

---

## Weaknesses

### Fatal
None.

### Major

- **Interpretive overclaiming: "shallow and opportunistic reliance" is not uniquely supported by the evidence.** The abstract and §4.3 conclude that models show "shallow and opportunistic reliance on CoT," but the deletion evidence is equally consistent with a simpler explanation: models have internalized sufficient physics knowledge through RL-based training that they can solve many problems without their scratchpad. The paper itself acknowledges in §4.1 that "we do not probe internal mechanisms directly" and that "LLMs may draw on internalized physics knowledge." A discriminating test — comparing deletion-heavy final answers against §3.1's direct-prompting outputs on the same problems — is already within reach given the paper's design, but is never executed. Without this comparison, the "shallow reliance" narrative is one plausible interpretation among several, not an established finding.

- **Information overlap metric conflates answer length with content recovery.** The description in §2.4 states the metric captures "the fraction of deleted CoT elements that reappear in the final answer," but the formal definitions (Eqs. 1–2) compute Jaccard similarity and Manhattan distance between the **full original CoT** and the **full final answer** — not between the *deleted span* and the final answer. This distinction is material: as final-answer length grows (cramming), its vocabulary naturally overlaps more with *any* physics reference, including the retained 40% of the scratchpad. The increasing overlap curves in Figure 7 may largely reflect answer-length growth rather than targeted recovery of deleted content. The paper presents these curves as evidence that "models often reintroduce deleted content" without controlling for length or restricting the reference to the actually-deleted span. This undermines one of the paper's three stated contributions.

### Minor

- **Sample sizes for main deletion sweep experiments are not reported.** The calibration study is on 50 UG-Physics questions (§3.2), but the number of problems evaluated in the main deletion experiments (Figures 4–7) is never stated. The 40% and 60% thresholds are the primary quantitative claims; the reliability of these thresholds is hard to assess without knowing the denominator. A per-condition counts table would directly address this.

- **The Claude-4 Sonnet scoring rubric includes "formatting and clarity" alongside correctness.** In the cramming regime, longer final answers may score better on formatting/clarity even if physics reasoning is partially incorrect. The partial accuracy uptick noted for UG-Physics at high deletion fractions (§3.2, Figure 6 panels b, c, f) could reflect this. The paper does not validate the judge against a format-agnostic criterion (e.g., symbolic/numerical answer matching on closed-form problems).

### Trivial

- The related-work section is placed after the conclusion (§6), making it harder to position the contribution against Lanham et al. (2023) upfront. The paper cites Lanham et al. but does not explicitly state what its deletion methodology adds beyond applying their approach to the physics domain.

---

## Nice-to-Haves

- The paper would be substantially strengthened by restricting the overlap metric to the *actually-deleted span* (rather than the full original CoT) and normalizing by final-answer length. This would convert the current observation into a proper recovery-efficiency measure and allow strategy comparisons that are currently confounded.

- A direct comparison of final answers at ~40–60% deletion against §3.1's direct-prompting outputs (content similarity, not just accuracy) would sharply distinguish "parametric bypass" from "crammed recovery" and lend much stronger support to the faithfulness-gap narrative.

- The choice of medium-reasoning prompts as default for deletion experiments (§2.3) is reasonable but unvalidated. Showing that the X-shaped accuracy/length pattern holds similarly under full-reasoning prompts would confirm the result is not an artifact of the already-concise scratchpad.

- Significance tests on the 40% vs. 60% accuracy thresholds across deletion strategies, or at minimum confidence intervals discussed relative to noise levels, would make the quantitative claims more precise.

---

## Removed Points

*These points are flagged for removal; treat them with caution.*

- **Harsh Critic: "This is not fixable by adding experiments under the current design"** — Demoted. The confound between parametric bypass and genuine cramming is real but the fix (comparing to direct-prompting outputs already in hand) is straightforward. This is Major, not Fatal.

- **Harsh Critic: The medium-reasoning prompt choice is not justified** — Removed as a standalone weakness. The paper does explain the choice in §2.3 ("medium reasoning by default") and the concern applies weakly given that the X-shaped pattern appears consistently across all three benchmarks.

- **Harsh Critic: §4.3 observation that "not all intermediate steps are faithfully required" is not new, given Lanham et al.** — Removed per soft rules: evaluating domain novelty (physics / AI-for-science) is the stated contribution scope. The paper does not claim the abstract observation is new; it claims the methodology and domain application are new.

- **Strength Finder: "Rigorous information-overlap analysis" as a strength** — Removed. The metric has the length-confound issue identified above; presenting it as rigorous without length controls is not a strength.

- **Strength Finder: The problem is important / AI for science is important** — Removed as generic. Retained only domain-specific motivating aspects (equations/units as structured testbed).

---

## Novel Insights

The "cramming" phenomenon — models spontaneously lengthening final answers to compensate for deleted scratchpad content — is a concrete, named, and robustly documented behavioral pattern that had not previously been characterized systematically in scientific reasoning benchmarks. The finding that physics-aware deletion (targeting equations and constants specifically) degrades accuracy more steeply than random deletion, but produces a sharp final-answer spike only at 70–80% deletion, suggests that physics-structured tokens are especially redundant until a critical mass is lost. This implies an asymmetry in reasoning robustness that has practical implications for efficient inference: CoT generation could potentially be truncated earlier than currently assumed without proportional accuracy loss.

---

## Suggestions

1. **Fix the overlap metric.** Restrict the reference text for Jaccard/Manhattan to the *deleted span only*, and normalize by final-answer length. This converts Figure 7 into a per-deleted-token recovery rate, which is the quantity the authors actually intend to measure.

2. **Run the discriminating comparison.** On the same question set, compare final answers at 40–60% deletion against no-CoT (direct) prompting outputs. Measure content overlap *between those two conditions*. If they are near-identical, parametric bypass is supported. If deletion-heavy answers uniquely recover deleted steps, that is evidence of genuine cramming. Either result strengthens the paper.

3. **Report per-condition sample sizes and mean ± SE in a results table** alongside the figures, so the reliability of the threshold claims can be assessed.

4. **Tone down the interpretation in the abstract and §4.3.** Replace "shallow and opportunistic reliance on CoT" with a more hedged framing such as "accuracy under heavy deletion is consistent with CoT being partially bypassable, though the mechanism remains unclear." This is more accurate and more defensible.

5. **Add an LLM-judge validation study.** For a subset of UG-Physics problems with closed-form numerical answers, compare the Claude-4 Sonnet judge scores against exact numerical match. This would validate that the score is tracking physics correctness rather than length/formatting.

---

## Score and Decision

**Originality:** The deletion framework adapted for physics, the three-strategy sweep design, and the cramming characterization represent incremental but concrete methodological novelty over Lanham et al. (2023). (3/5)

**Importance:** CoT faithfulness for AI-for-science is a timely and important question. The paper correctly identifies a real evaluation gap. (4/5)

**Claims supported:** The cramming finding (accuracy stable, length increases, X-shaped pattern) is well-supported. The faithfulness-gap narrative and the "shallow and opportunistic reliance" claim are overclaimed relative to the evidence, and the overlap metric has a verifiable confound. (2/5)

**Soundness:** The core design is reasonable, but the overlap metric description contradicts its formal definition, and the key interpretive test (direct-prompting comparison) is absent despite the baseline being available. (2/5)

**Clarity:** Writing is generally clear and organized. The discrepancy between metric description and formal definition in §2.4 is a meaningful inconsistency, not a parser artifact. (3/5)

**Community value:** The paper provides a reusable deletion-probing methodology and the first systematic characterization of cramming in physics benchmarks — useful for the AI-for-science and CoT faithfulness communities. (3/5)

The paper has a real and interesting empirical contribution, but the gap between the headline claim ("shallow and opportunistic reliance") and what the experiments actually establish is too wide for the paper to stand as-is. The overlap metric issue is particularly concerning because it affects one of the three stated contributions. These are fixable in revision, and the core cramming finding remains compelling, but the paper needs revision before it can support its stated conclusions.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>