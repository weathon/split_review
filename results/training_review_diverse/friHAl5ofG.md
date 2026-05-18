Now I have a thorough understanding of the paper and the reviews. Let me synthesize the final consolidated review.

---

## Summary

This paper introduces Generative Value Learning (GVL), a method that uses frozen vision-language models (VLMs) as universal value functions by shuffling video frames and auto-regressively predicting task completion percentages. The key insight is that naively prompting a VLM with ordered video frames produces uninformative monotonic outputs, but shuffling the frames forces the model to ground its predictions in semantic content rather than chronology. Evaluated on 51 datasets spanning 20 embodiments and over 300 real-world tasks, GVL shows positive value-order correlations (VOC) zero-shot and improves further via in-context examples from the same task, different tasks, or even human videos. Three downstream applications are demonstrated: dataset quality estimation, success detection, and advantage-weighted regression for policy learning.

## Strengths

- **Shuffled-frame value prediction is a genuinely novel and well-motivated technique for breaking temporal bias.** The paper identifies a real failure mode of naive VLM prompting (monotonic, uninformative values) and shows that shuffling frames forces the VLM to produce varied, semantically grounded value curves. The ablation in Section 4.4 provides direct evidence: removing shuffling collapses predictions onto linear patterns (Figure 7 right), while GVL produces value curves that discriminate success from failure (Figure 5). This is a clean and creative solution to a nontrivial problem.

- **Large-scale evaluation across diverse tasks and embodiments.** GVL is tested zero-shot on 50 OXE datasets (1,000 trajectories) and a 250-task bimanual ALOHA dataset (500 trajectories), covering 20 distinct robot embodiments. The VOC histograms in Figure 3 skew strongly positive on OXE, and the comparison to LIV — a prior fine-tuned value model — shows clear advantages, especially on language-goal tasks where LIV produces near-random predictions. This breadth of evaluation is rare in the value learning literature.

- **Flexible multi-modal in-context learning with cross-embodiment transfer.** GVL improves with in-context examples (Figure 2 right, median VOC from 0.12 to 0.37 on bimanual tasks), and this improvement scales with the number of examples without saturation up to 5 shots. The cross-embodiment result — human video demonstrations improving robot value predictions (Figure 6) — is particularly striking and demonstrates a capability unique among VLM-based value models.

- **Three concrete downstream applications with quantitative real-world results.** The paper goes beyond value prediction metrics to show practical utility: dataset quality estimation (Table 1, VOC scores matching human intuitions), success detection (Table 2, 0.75 accuracy vs. 0.62 for SuccessVQA), and advantage-weighted regression on real robots (Table 3, GVL+DP outperforms DP on 5 of 7 real-world tasks). These applications are tested on real data, not simulation only.

## Weaknesses

### Fatal
None.

### Major

1. **The central evaluation metric (VOC) is validated only partially, and its limitations are under-explored relative to the weight placed on it.** The paper relies on VOC — the rank correlation between predicted values and ground-truth timestep order — as the primary measure of value quality across hundreds of tasks. The underlying assumption is that monotonicity on expert trajectories implies good value estimates. While the paper provides some validation — the AWR experiment (Table 2/3) shows correlation between VOC and policy improvement on 7 real-world tasks, and the success detection experiment (Section 4.3) shows VOC distinguishes success/failure trajectories — this validation is narrow in scope. VOC is fundamentally a measure of whether predicted values are increasing, not whether they are *correct* or *useful* in settings beyond expert monotonicity. A model that produces plausible-but-wrong values on a non-expert trajectory would be undetected. The paper's large-scale claims about OXE performance (1000 trajectories, 50 datasets) rest almost entirely on VOC without ground-truth verification that high-VOC trajectories correspond to sensible, task-grounded value estimates. A controlled experiment in simulation comparing VOC against known ground-truth value functions would substantially strengthen the evidence.

2. **The zero-shot framing overstates capability on challenging tasks.** The abstract claims GVL "can in-context zero-shot and few-shot predict effective values for more than 300 distinct real-world tasks," and the title emphasizes zero-shot. However, on the bimanual ALOHA dataset — 250 of those 300+ tasks — zero-shot GVL achieves a median VOC of only 0.12, with roughly 40% of trajectories producing non-positive VOC (worse than or equal to random). The paper acknowledges this is "worse than the performance on the OXE datasets" (line 156), but this caveat appears deep in the text, well after the strong zero-shot claims in the abstract and introduction. The one-shot results (median VOC 0.37, 90% positive) are genuinely impressive, but these are few-shot, not zero-shot. The paper would benefit from being upfront about the domain-dependence of zero-shot capability rather than leading with it as a primary contribution.

### Minor

1. **The comparison to LIV is confounded by different input conditions.** GVL receives the entire shuffled video (30 frames) as context and predicts values auto-regressively with access to all frames simultaneously, while LIV processes one frame at a time via embedding similarity to a goal. The paper frames this as GVL solving "the more difficult task of frame re-shuffling" (Figure 3 caption), which is debatable — having all frames available allows cross-frame comparisons that are unavailable to LIV. The Single Frame ablation (VOC -0.08 on RT-1) shows that without multi-frame context, GVL's performance collapses. A fairer framing would acknowledge that GVL's advantage comes partly from multi-frame reasoning, which is a genuine strength but not directly comparable to LIV under the same information constraints. A baseline that provides LIV with trajectory-level context (where LIV's architecture allows) or that restricts GVL to single-frame predictions would clarify the comparison.

2. **The first-frame conditioning is never ablated.** The paper conditions the VLM on the first frame as a temporal anchor (line 87) to resolve arrow-of-time ambiguity. This design choice is motivated but never tested — there is no experiment showing what happens without it. Given that the VLM might infer temporal direction from visual cues (e.g., objects moving in a physically plausible direction) or from the task description, ablating this component would clarify whether it is essential or merely helpful.

3. **The AWR real-world results (Table 2/3) lack error bars or statistical tests.** The paper acknowledges "noisiness in model checkpoints performance" (line 336) and reports average success over the last 10 checkpoints, but the table entries (e.g., "7/10" vs. "6/10") are presented as point estimates without confidence intervals. For 10 trials per task, binomial confidence intervals would be wide, and most observed differences may not be statistically significant. Reporting exact binomial confidence intervals or per-checkpoint variance would allow readers to assess the reliability of the claimed improvement.

4. **OXE results are presented only as histograms without summary statistics.** The OXE evaluation (Figure 3) shows aggregate histograms but does not report median, mean, or fraction of trajectories with positive VOC for the OXE datasets. These statistics would allow readers to calibrate the zero-shot claims quantitatively, as was done for the bimanual dataset.

### Trivial
None.

## Nice-to-Haves

- A controlled simulation experiment comparing VOC against ground-truth value functions (e.g., mean absolute error or downstream policy success) would directly validate the metric.
- Reporting approximate API cost per trajectory (tokens, latency) would help practitioners assess feasibility.
- A qualitative failure analysis for the low-VOC OXE datasets (e.g., DROID, RoboNet) — beyond the brief discussion in Section 4.2 — would make VOC scores more interpretable.
- Testing the VOC threshold for success detection across different failure rates and environments would strengthen the generality claim.

## Removed Points

- **"The paper provides almost no evidence that VOC tracks what we care about"** — This is an overstatement. The paper does provide evidence: the AWR experiment shows VOC correlates with policy improvement, and the success detection experiment shows VOC distinguishes success/failure. The concern about *limited* validation is kept in Major #1, but the "almost no evidence" framing is removed.
- **"The no-shuffling baseline inflated VOC, and the paper doesn't check whether the same inflation occurs in the shuffled case"** — This misunderstands the method. With shuffling, a linear ramp output would assign random values to random frames and produce low VOC. The shuffling mechanism prevents the inflation the critic describes. The broader concern about VOC measuring only monotonicity (not value correctness) is kept in Major #1.
- **"In-context learning looks more like few-shot regression than in-context learning of a general value concept"** — This is a semantic distinction. Providing shuffled frame-value pairs as context and observing performance gains is the standard operational definition of in-context learning used throughout the LLM literature. The fact that more examples help (scaling) is consistent with in-context learning, not contradictory to it.
- **Weaknesses about the paper needing to cover additional domains/tasks or use different preferred baselines/methods** — These are scope-creep demands that would turn the paper into something broader rather than stronger.
- **Any criticism about missing appendix content** — The parser strips appendix sections; these exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a recurring tension: the paper's evaluation is impressive in breadth but the central metric (VOC) receives only narrow validation relative to the weight it carries. The most novel observation across the reviews is that the gap between zero-shot (median 0.12 on bimanual) and one-shot (median 0.37) is large, which may suggest that the VLM's pre-trained world knowledge alone is insufficient for challenging tasks and that the in-context examples are doing most of the work — a hypothesis the paper could productively investigate.

## Suggestions

1. **Conduct a direct validation of VOC** by evaluating GVL on simulated tasks where ground-truth value functions are known (e.g., via access to simulator state or reward). Compare VOC against mean absolute error in value prediction and/or downstream policy improvement. This would either confirm that VOC is a reliable proxy or reveal its limitations, and in either case substantially strengthen the paper's empirical contribution.

2. **Recalibrate the zero-shot claims** to match the evidence. Be upfront about the domain dependence: zero-shot works well on OXE-style data but substantially worse on fine-grained bimanual tasks. The one-shot and few-shot results are strong enough to stand on their own as contributions.

3. **Report summary statistics** (median, mean, % positive VOC) for the OXE results alongside the histograms, as was done for the bimanual dataset. This gives readers a quantitative baseline.

4. **Add an ablation of the first-frame conditioning** to confirm its role. A simple comparison of GVL with and without the first-frame anchor on a representative subset would suffice.

5. **Add binomial confidence intervals or per-checkpoint variance** to the AWR real-world results (Table 2/3) so readers can assess statistical significance.

## Score and Decision

**Originality:** 8/10. Shuffling frames to break temporal bias in VLM-based value prediction is a genuinely novel and clever idea.  
**Importance of research question:** 8/10. Universal value estimation is a key bottleneck in generalist robot learning.  
**Claims support:** 5/10. The central metric (VOC) is only partially validated, and some claims (especially zero-shot) outpace the evidence.  
**Soundness of experiments:** 7/10. Broad in scope but the LIV comparison has a confound and the AWR results lack error bars.  
**Clarity of writing:** 8/10. Well-structured and clearly written.  
**Value to community:** 7/10. The method is practical and the in-context learning findings are practically useful.

The paper presents a genuinely novel method and an impressively broad evaluation. The core weakness is that the paper leans heavily on VOC — a metric whose limitations are acknowledged but not fully addressed — to support large-scale claims. The zero-shot framing overstates what the data show. These are addressable in revision: direct validation of VOC and recalibrated claims would substantially strengthen the paper. The method itself is interesting, the in-context learning results are compelling, and the downstream applications demonstrate real utility.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>