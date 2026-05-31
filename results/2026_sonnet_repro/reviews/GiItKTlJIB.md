Now let me run calibration searches to properly score this paper.**Round 1 bracket: 4–6** (directionally useful methodology paper for physics CoT faithfulness, but with notable methodological gaps and overclaimed interpretations)Now I have enough to write the final review. Let me synthesize everything.

---

## Summary

This paper introduces a deletion-based probing framework to evaluate chain-of-thought (CoT) faithfulness in physics problem solving. The authors systematically intercept CoT scratchpads mid-generation, remove tokens under three strategies (end, random, physics-aware), and measure accuracy, answer length, and information overlap across three open-source models (Phi-4, Qwen-A3B, Magistral) and three physics benchmarks (UG Physics, PhyBench, PhysReason). The central finding is that accuracy remains stable under 40–60% deletion while final answer length increases ("cramming"), suggesting models can partially bypass their CoT traces, which the authors interpret as evidence of shallow and opportunistic CoT reliance.

---

## Strengths

- **Controlled deletion framework enabling causal probing of CoT dependence.** The paper introduces a clean mid-generation intervention across three deletion strategies, sweeping deletion fractions from 0–100%. This design enables a systematic, quantitative picture of CoT dependence — a genuine methodological contribution over prior correlation-based faithfulness work.

- **Consistent cramming behavior across models and datasets.** The X-shaped pattern — accuracy stable until ~40–60% deletion while answer length steadily increases — is demonstrated consistently across all three models and three benchmarks (Figures 4, 5). This cross-model, cross-benchmark consistency is a real empirical finding that is hard to dismiss as noise.

- **Physics-aware deletion strategy.** The use of Claude-4 Sonnet to tag physics-specific spans (equations, constants, units) for selective deletion is a domain-informed contribution that goes beyond prior perturbation-based approaches and produces meaningfully different results: accuracy declines gradually while answer length spikes only at very high deletion (70–80%), adding a richer characterization than uniform deletion alone.

- **Informative baseline calibration.** Figure 2 demonstrates clearly that CoT (Full Reasoning) outperforms direct answering across models and datasets, confirming that CoT is beneficial when present and making the deletion experiments a meaningful test of dependence rather than just redundancy.

---

## Weaknesses

### Fatal
*None.*

### Major

- **Core interpretive claim is underdetermined by the evidence.** The paper's abstract and §4.3 claim that results "expos[e] shallow and opportunistic reliance on CoT," but the deletion experiments cannot distinguish between (a) models that bypass CoT and answer from parametric memory and (b) models that are capable reasoners with internalized physics knowledge and simply fill in gaps when their scratchpad is truncated. The paper does acknowledge this in §4.1 ("these results suggest that LLMs may draw on internalized physics knowledge") but then makes stronger statements throughout. Critically, the paper already runs direct-prompting experiments (§3.1, Figure 2) but never uses them to test this confound: comparing cramming answers (under 40%+ deletion) to direct-prompted answers would directly probe whether the model is doing the same thing under both conditions. This comparison is available in the paper's own design but is omitted, leaving the central interpretive claim unresolved.

- **Information overlap metric measures against the full original CoT, not the deleted portion.** Section 2.4 states the metric captures "the fraction of deleted CoT elements that reappear in the final answer," but Eq. 1–2 and §4.2 explicitly compute Jaccard similarity and Manhattan distance between (i) "the original CoT prior to deletion" (i.e., the full scratchpad) and (ii) the generated final answer. This means content from the *retained* portion of the scratchpad — which the model directly attended to during final answer generation — inflates the overlap score without any recovery of deleted content occurring. In a physics domain where the retained CoT already contains equations, constants, and units that will naturally appear in a correct final answer, this confound is substantial. The Figure 7 curves therefore cannot reliably distinguish "model recovered deleted equations" from "model used retained equations (plus domain vocabulary) in the final answer." Without controlling for this, the overlap analysis cannot support its stated interpretation.

### Minor

- **Main experiment sample sizes are not reported.** The calibration study (§3.2) justifies using 5 prompts over 50 UG-Physics questions for stable estimates, but the paper does not report the sample counts used in the main deletion sweep experiments (Figures 4–7). Without this, it is not possible to assess the reliability of the 40% and 60% threshold claims, which are the paper's primary quantitative findings. Error bars are shown (Figure 7 includes standard error shading), but absent denominator counts the evidence is incomplete.

- **The scoring metric conflates correctness with formatting and clarity.** Per §2.4, the Claude-4 Sonnet judge scores on "correctness of the final answer, accuracy of the physics derivation, logical coherence, formatting, and clarity." When cramming produces longer answers, the formatting and clarity component may reward verbosity even if the underlying physics is incorrect. The paper notes a "partial offset" of accuracy at very high deletions for UG-Physics — this uptick could partially reflect the rubric rewarding longer, more formatted answers rather than genuine accuracy recovery. No validation against a simpler exact-match or formula-matching criterion is provided.

- **Differentiation from Lanham et al. (2023) is underdeveloped.** The paper cites Lanham et al. in §6 and shares their qualitative finding that "not all intermediate steps are faithfully required." The novelty claim rests primarily on the physics domain shift and the physics-aware deletion strategy, both legitimate contributions, but §6 does not directly compare methodology or findings against Lanham et al. A brief comparison would sharpen the contribution.

- **Medium reasoning as the default deletion setting is not justified.** Section 2.3 states "we use the medium reasoning prompt by default" without motivation. Deleting 40% of an already-concise trace is a qualitatively different intervention than deleting 40% of a verbose trace; effect sizes may differ substantially. Consistency with other prompting levels is not shown.

### Trivial

*None beyond the above.*

---

## Nice-to-Haves

- The direct comparison the paper is missing (cramming answers vs. direct-prompted answers on the same problems) would be the single most valuable addition: if cramming answers under 40% deletion are statistically indistinguishable from direct-prompted answers in content and quality, that would substantially strengthen the "parametric bypass" interpretation. If they differ, that would be equally interesting.
- Restricting the overlap metric to the *specifically deleted* span (rather than the full original CoT) and normalizing by answer length would convert the current confounded overlap curves into a proper recovery-efficiency measure, enabling comparison across deletion strategies.
- Scaling analysis: do larger models exhibit more faithful CoT usage, or stronger cramming? The three models span 14–30.5B parameters, which could yield preliminary evidence.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "This confound is not fixable by adding experiments"** — The critic characterizes the parametric-memory confound as structural and unfixable. In fact, the paper already has the direct-prompting baseline in hand (§3.1), and comparing cramming answers to direct-prompted answers would directly address it. The concern is real but not irremediable; demoted to Major.

- **Harsh Critic: "The paper cannot be published as written" / "contribution does not yet support publication"** — This sweeping dismissal goes beyond what is supported; the cramming finding and deletion framework are real contributions. Removed as framing; the specific concerns are retained separately.

- **Strength Finder Strength 3: "Rigorous faithfulness analysis"** — The paper's own description calls the analysis "rigorous," but Weakness 2 shows the overlap metric has a specific methodological flaw. Claiming rigor for an analysis with an uncontrolled confound is not supportable; this strength is removed.

- **Strength: Physics provides a unique testbed enabling precise quantification** — This is partially true (structured equations and units are easier to tokenize than prose) but generic enough to apply to any mathematical domain. The physics-specific deletion strategy *is* a genuine contribution and is retained in the Strengths section in that form.

---

## Novel Insights

The "cramming" phenomenon — where deletion of CoT tokens causes a compensatory increase in final answer length — is a genuinely interesting and consistent observation that has practical implications (early stopping of CoT may be cost-efficient without proportional accuracy loss). The strategy-dependent recovery patterns in Figure 7 (smooth under end deletion, delayed under random, noisy with spikes under physics-aware) suggest that the *structure* of how reasoning is removed matters for model recovery, which is a novel empirical finding even if the headline interpretation ("shallow reliance") is not yet established. The physics-aware deletion strategy, where a model identifies physics-relevant spans, offers a template for domain-informed CoT probing that could be generalized to other scientific disciplines.

---

## Suggestions

1. Run the direct-prompting comparison: take final answers from the deletion experiments at the 40–60% deletion mark and compare their content/correctness to direct-prompted answers on the same problems. This would directly address the parametric-memory confound.
2. Revise the overlap metric to measure against the deleted span specifically, and normalize by answer length. Report raw sample counts for all main experiments.
3. Report all main experiment sample counts alongside error bars in figures.
4. Add a brief targeted comparison to Lanham et al. (2023) explaining what the deletion framework adds methodologically (the physics domain, the three-strategy design, the physics-aware annotation).
5. Soften the abstract and §4.3 claims from "shallow and opportunistic reliance on CoT" to language that accurately reflects the hedging already present in §4.1: results are *consistent with* shallow reliance and *suggest* models may draw on internalized knowledge.

---

## Calibration Anchors and Score Reasoning

**All retrieved anchors:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| pXIbcRPxWR | 2.50 | R1 (weak) | Far below; supervised CoT task with superficial methodology |
| RuY1r1PDdQ | 3.00 | R1 (weak) | Below; benchmarking paper with no novel methodology |
| EXaKfdsw04 | 3.25 | R1 (weak) | Below; step-by-step verification without systematic evaluation |
| qit4pa6PpY | 3.00 | R1 (weak) | Below; instruction-following benchmark paper |
| 1OyE9IK0kx | 5.00 | R1 (mid)/R2 | Close reference: comprehensive multi-method faithfulness evaluation, also rejected; slightly stronger than paper under review |
| awtd0XhzKQ | 5.75 | R1 (mid)/R2 | Above paper under review; proposes concrete neuro-symbolic method |
| w6nlcS8Kkn | 6.67 | R1 (mid) | Above; meta-analysis of 100+ papers across 14 models and 20 datasets |
| asGQQc7gNo | 6.67 | R1 (mid) | Above; proposes factuality/context-faithfulness trade-off with new method |
| KIgaAqEFHW | 8.00 | R1 (strong) | Far above; neural theorem proving with long contexts |
| 3bq3jsvcQ1 | 8.00 | R1 (strong) | Far above; introduces step-back prompting with strong STEM gains |
| CIN2VRxPKU | 5.33 | R2 | Slightly above; deep unlearning evaluation paper with systematic metric design |
| rpbzBXdo4x | 5.00 | R2 | Closest match: when CoT hurts, empirical probing framework, rejected |
| 71kocBuhNO | 5.40 | R2 | Slightly above; systematic logical reasoning evaluation across 25 patterns |
| 4L0xnS4GQM | 5.50 | R2 | Above; chain-of-table reasoning with a concrete new method |
| qGL6fE1lqd | 4.40 | R2 | Below; physical reasoning evaluation paper, rejected for limited methodology |

**Round 1 bracket: 4–6.**

**Round 2 narrowing:** The closest anchors are 1OyE9IK0kx (5.0, rejected) and rpbzBXdo4x (5.0, rejected). The paper under review has real findings and a clear methodology, but compared to these anchors it is weaker:

- 1OyE9IK0kx has more comprehensive experiments (three intervention approaches) and a clearer research question. The paper under review has the overlap metric flaw and underdetermined interpretive claims that 1OyE9IK0kx does not.
- rpbzBXdo4x has stronger theoretical motivation (cognitive psychology parallel) and a tighter empirical story.
- qGL6fE1lqd (4.4) is a physics reasoning evaluation paper that was rejected for limited methodology — a closer peer in setting but the paper under review is more systematic.

The paper under review sits just below the 5.0 cluster because of the two Major weaknesses (the interpretation ambiguity and the overlap metric confound), placing it at **4.5**.

---

## Score and Decision

**Originality:** Moderate. The deletion framework applied to physics is new, and the physics-aware deletion strategy is domain-novel. However, the qualitative findings extend Lanham et al. (2023) without sufficient differentiation.  
**Importance:** The research question (does CoT faithfully reflect reasoning in AI-for-Science?) is genuinely important.  
**Claims supported by evidence:** Partially. The cramming behavior is well-supported. The interpretation as "shallow reliance" is not.  
**Soundness of experiments:** The experiments are consistently designed and reproducible in principle, but the overlap metric has a specific flaw and sample sizes are not reported.  
**Clarity:** Generally readable, with one significant inconsistency between §2.4's description and §4.2's metric definition.  
**Value to research community:** The deletion framework and cramming phenomenon are valuable contributions; the paper's weaknesses limit rather than eliminate that value.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>