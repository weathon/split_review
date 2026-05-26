Here's my final consolidated review.

## Summary

This paper presents a systematic large-scale study of how reasoning data — varying in diversity, quality, and scale — should be allocated across pretraining, SFT, and RL stages. The authors pretrain an 8B model from scratch under 4 data conditions and evaluate across 12 combined PT×SFT configurations plus RL on extreme conditions. Key findings: (1) front-loading reasoning data into pretraining creates durable gains that SFT cannot erase, (2) an asymmetric allocation principle where diverse data helps pretraining while quality dominates SFT, (3) high-quality pretraining data exhibits latent effects activated only after SFT, and (4) naive scaling of SFT data is harmful. The paper addresses a timely and practically important question with a commendably broad experimental scope.

## Strengths

1. **Systematic, fully-crossed experimental design.** The 4 pretraining conditions × 3 SFT conditions (= 12 models) plus RL on the extremes provides a level of coverage rare in the literature. This allows causal attribution of performance differences to the stage and type of data injection — a genuine step beyond prior work that studies post-training or mid-training in isolation.

2. **Clean evidence that reasoning-rich pretraining creates a durable advantage.** Table 4 shows that even doubling SFT epochs on the baseline (M_base + 2× SFT_SHQ) fails to match the weakest reasoning-pretrained model (M_SHQ + SFT_SHQ), and Table 3 shows the gap widens to 18.57% after RL. This directly and convincingly refutes the "catch-up" hypothesis.

3. **Novel finding of latent effects from high-quality pretraining data.** M_LMQ (which adds high-quality D_SHQ to diverse D_LDQ) shows minimal immediate benefit at pretraining (+0.02% overall, Table 1) but gains an additional +4.25% over M_LDQ after SFT (Table 4). This non-obvious synergy supports the claim that pretraining quality can have deferred benefits — a practically actionable insight.

4. **Demonstration that naive SFT scaling is harmful while targeted quality addition helps.** Table 8 shows that doubling mixed-quality SFT data reduces math accuracy by 4.92%, whereas adding a marginal 0.4% of long-chain-of-thought data yields consistent gains. This provides concrete guidance for practitioners.

5. **Evaluation breadth across math, science, code, and instruction-following at all three training stages.** The gains generalize beyond math to science (Table 2, SCIENCE_SFT AVG from 34.48 to 40.61) and code, strengthening the generalizability claims.

## Weaknesses

### Fatal

None.

### Major

- **The central claim that "diversity drives pretraining gains" is confounded with the number of unique examples.** The key comparison is M_SHQ (1.2M high-quality examples, repeated to match token budget) vs M_LDQ (268M diverse-quality examples seen approximately once). These datasets differ simultaneously in size (unique count), diversity, and quality. The observed 9.09% gain for M_LDQ could come from the sheer number of unique reasoning examples, from cross-domain diversity, or from a combination of both — the design does not isolate these factors. The paper's abstract and conclusion attribute the effect to "broad diversity in reasoning patterns (11% average gain)," which oversells what the evidence supports. The paper should either (a) acknowledge this confound transparently and temper the diversity claim, or (b) run a control with a large-but-narrow dataset (e.g., 268M math-only examples) to separate the two factors. This weakness does not invalidate the paper's core finding that front-loading reasoning data helps, but it substantially weakens the precision of the "asymmetric principle" attribution.

### Minor

- **The headline "19% gain" is from the most favorable slice and is presented without context.** The 19% figure cited in the abstract comes from the RL stage on expert-level benchmarks (Table 3). Gains at pretraining (+8.35%, Table 1) and post-SFT (+9.3%, Table 2) are substantially smaller. The paper should specify that 19% is the compounded upper bound after RL on expert tasks, and report the range of gains across stages.

- **The catch-up test is limited to doubling SFT epochs.** Table 4 tests only a single level of catch-up effort (2× epochs). A more aggressive catch-up attempt (e.g., more data, different SFT recipes, or multiple SFT rounds) might eventually close more of the gap. The paper's conclusion that "catch-up is impossible" is stronger than the evidence warrants; it should acknowledge that the hypothesis is refuted only within the tested budget.

- **The "overfitting" hypothesis is invoked but never directly tested.** The paper claims to refute the overfitting hypothesis (§1, §4), but provides no direct evidence such as pretraining loss curves on held-out reasoning data or analysis of generalization decay on non-reasoning tasks when reasoning data is repeated. The claim rests entirely on the observation that reasoning-pretrained models perform well after SFT, which is indirect.

- **Data overlap between D_base and D_res is not discussed.** D_base already contains mathematics and code sources. D_res also contains these domains. If D_base already includes similar reasoning data, the apparent benefit of adding D_res could be inflated. The paper should at minimum acknowledge this and discuss the potential effect.

- **SFT data composition is underspecified.** The paper states that each model is finetuned on 4.8M reasoning samples from D_res, but D_SHQ has only 1.2M examples and D_LDQ has 268M. How the 4.8M figure was derived (subsampling, mixture ratios, repetition) is not explained. This matters because differences in repetition rates across conditions could affect results.

- **The RL comparison is limited to two conditions.** Only M_base and M_LMQ were taken through RL, both with the same SFT recipe. The claim that "pretraining strategy dictates final accuracy on expert-level tasks" would be stronger if additional PT conditions (e.g., M_LDQ, M_SHQ) were also evaluated after RL. As it stands, this is a single comparison rather than a systematic demonstration.

- **The pretraining schedule (600B base, then 400B mix at 80/20) is not ablated or justified.** The paper does not discuss whether the ordering matters (reasoning introduced only after 60% of training) or whether interleaving from the start would change the conclusions.

### Trivial

- The ALF selection criterion (answer length >4096 tokens) is a reasonable proxy for reasoning complexity, but the paper occasionally treats it as a direct measure of "quality" without acknowledging the proxy nature. A brief caveat would clarify.

## Nice-to-Haves

- **Multiple training seeds or statistical characterization.** Each condition is a single training run. For an empirical study making quantitative comparative claims, this is a limitation, though we acknowledge that pretraining an 8B model from scratch is extremely expensive. At minimum, the paper should explicitly acknowledge this and calibrate the precision of its claims.
- **A cleaner test of the diversity hypothesis** would compare a large-but-narrow condition (e.g., 268M math-only examples) against M_LDQ under the same token budget. If the broad-domain condition outperforms the narrow-large condition, the diversity claim would be cleanly supported.
- **Direct overfitting evidence** (e.g., loss curves on held-out reasoning data) would strengthen the "durable foundation" claim.
- **An expanded catch-up experiment** using more aggressive SFT scaling (more data, different recipes) would strengthen the conclusion that pretraining advantages are truly irrecoverable.

## Removed Points

These points were raised in the input reviews but are removed after verification:

1. *"No runs with different random seeds"* — Moved to Nice-to-Have. Multiple training seeds at this scale (1T tokens, 8B model) are not standard practice in the field. The paper reports evaluation variance (16 runs for AIME, 4 for others).
2. *"The reader does not know until §2.2 that diversity is confounded"* — Redundant with the Major weakness about the confound. Subsumed into the first weakness entry.
3. *"The 19% may not be the typical benefit"* — This is already addressed in the Minor weakness about the 19% figure, but the framing in the critic is somewhat overstated. The paper does specify "expert-level benchmarks" in the introduction bullet, though the abstract is ambiguous. Kept as a Minor weakness.

## Novel Insights

The reviews surface one genuinely novel observation beyond what the paper itself contributes: the finding that M_LMQ (adding high-quality data to a diverse mix) shows no immediate pretraining benefit but a deferred +4% SFT gain suggests a form of "pretraining latency" that the community has not systematically characterized. The reviews do not surface a fundamentally different interpretation of the data — the confound between diversity and unique-example count is the main critical insight, and it acts to temper rather than overturn the paper's narrative.

## Suggestions

1. **Acknowledge the diversity/scale confound explicitly** in §5 when discussing the asymmetric principle. Replace "diversity drives pretraining gains" with "large-scale diverse data (which jointly varies both dimensions) outperforms small high-quality data at pretraining." Frame the finding as evidence that *scale+diversity* matters at pretraining, not diversity alone.
2. **Contextualize the 19% headline** by specifying the stage (RL, expert benchmarks) and reporting the gain range across stages (8–19%).
3. **Add a brief discussion of data overlap** between D_base and D_res, even if only to state that the overlap is believed to be minimal and why.
4. **Explain how the 4.8M SFT samples** relate to the individual dataset sizes.
5. **Soften the "catch-up refutation" language** to acknowledge that the test was against a specific level of catch-up effort (2× epochs). Frame as "catches up under our tested conditions" rather than a universal impossibility.

## Score and Decision

**Score:** 6.0 / 10
**Decision:** Accept

### Calibration Anchors

| Anchor | Path | Avg Score | Round / Bucket | Comparison to This Paper |
|--------|------|-----------|----------------|-------------------------|
| "At Which Training Stage Does Code Data Help LLMs Reasoning?" | KIPJKST4gw | 7.25 | r1-topic-mid / r1-topic-high | Stronger: cleaner experimental design without the diversity/scale confound, though narrower scope |
| "What Kind of Pretraining Data Do LLMs Rely on When Doing Reasoning?" | 1hQKHHUsMx | 6.75 | r1-topic-mid | Comparable in quality but different contribution type (analytical vs prescriptive) |
| "Enhancing Multilingual Reasoning in LLMs" | S6cBH99BhB | 6.50 | r2 | Comparable: both have systematic designs with notable but not fatal weaknesses |
| "Advancing Mathematical Reasoning in Language Models" | GtpubstM1D | 5.71 | r1-topic-mid / r2 | Slightly weaker: more mixed reviews, some reviewers scored very low (1, 3) |
| "Amuro and Char: Analyzing PT-FT Relationship" | 8uXkyWFVum | 4.20 | r1-topic-mid | Weaker: only 1B model, limited novelty, insufficient experiments |
| "Towards Learning to Reason at Pre-Training Scale" | BGnm7Lo8oW | 5.50 | r2 | Weaker: limited effectiveness of the proposed method, narrower contribution |
| "On the Diversity of Synthetic Data" | oqsQbn4XfT | 5.80 | r1-weakness-diversity | Similar confound issues but different topic; rejected despite decent scores |
| "PolyPythias: Stability across 50 Pre-Training Runs" | bmrYu2Ekdz | 6.50 | r1-weakness-singlerun | Stronger on statistical rigor; less directly comparable |

### Calibration Narrative

**Round 1 bracket:** 5.0–7.0, based on topical anchors showing relevant papers range from ~5.7 (mixed-quality accept) to ~7.25 (strong accept with clean design). The code-data paper at 7.25 is the closest topical analogue — both ask "when to introduce X data during training" — but our paper has a confound that the code paper avoids.

**Round 2 narrowing:** Within the 5.0–7.0 bracket, the Enhancing Multilingual Reasoning paper (6.50) is the closest comparator in methodological profile: both are systematic data-allocation studies with notable but non-fatal weaknesses. Our paper has more novel findings (latent effects, asymmetric principle) but also has the diversity/scale confound, placing it just below the Multilingual paper. The "Advancing Mathematical Reasoning" paper (5.71) had very mixed reviews and confound issues of its own; our paper is stronger methodologically and less controversial, placing it above 5.71.

**What the low-band anchors (3–4) failed at:** Insufficient experimental scope, trivial or unsurprising findings, only testing small models. Our paper clearly exceeds these bars by pretraining an 8B model from scratch with a fully-crossed design and multiple novel findings. **Does our paper share any of their failures?** It shares the confound issue that some rejected papers had (e.g., the diversity-coefficient papers scoring 4.0), but the confound is peripheral to the paper's main contribution (front-loading is beneficial), not central to it. The core front-loading and catch-up findings are not affected by the confound, which primarily weakens one specific sub-claim about diversity attribution.

**Final score:** 6.0 — reflecting a solid accept with a notable but non-fatal methodological weakness that the authors should address.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>