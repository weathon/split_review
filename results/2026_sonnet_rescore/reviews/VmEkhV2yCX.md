---

## Summary

This paper presents the first systematic empirical investigation of how reasoning data—varying in scale, diversity, and quality—should be allocated between pretraining and supervised fine-tuning (SFT) to maximize downstream reasoning performance. Using four 8B hybrid models pretrained from scratch on 1T tokens (with three distinct reasoning data mixtures) and evaluated through pretraining, SFT, and RL phases, the paper argues for an asymmetric principle: pretraining benefits from diversity and scale, while SFT is dominated by data quality. Key findings include the "front-loading" advantage (reasoning-pretrained models retain and amplify their lead through SFT and RL), a "latent effect" where high-quality pretraining data only manifests post-SFT, and the harm of naive SFT data scaling.

---

## Strengths

- **Front-loading advantage demonstrated with substantial computational backing.** Every reasoning-pretrained model outperforms M_base after SFT by 9.3% on average (Table 2), and doubling SFT epochs for M_base still leaves it 3.32% behind even the weakest reasoning-pretrained model M_SHQ (Table 4). The RL phase extends the gap to 18.74% overall and a 39.32% absolute improvement on AIME-24/25 (Table 3). The four 1T-token pretraining runs on 512 H100s constitute a significant computational investment that credibly backs these claims.

- **Asymmetric principle supported by concrete, cross-stage evidence.** In pretraining, M_LDQ (268M diverse samples) yields +9.09% over M_SHQ (1.2M high-quality samples, Table 1). In SFT, the same M_res models fine-tuned on large diverse D_LDQ drop 13.45% relative to those fine-tuned on small high-quality D_SHQ (Table 5). The reversal of which dataset type wins depending on training stage is a concrete and actionable finding.

- **Latent effect of high-quality pretraining data: a genuinely novel observation.** M_LMQ and M_LDQ are statistically tied after pretraining (64.07 vs. 64.09, Table 1), yet M_LMQ leads by +4.25% after SFT with the same high-quality recipe (Table 4). This "sleeping" benefit is surprising and has practical implications for pretraining corpus design.

- **Harm of naive SFT scaling quantified with a clean ablation.** Table 8 directly shows that doubling mixed-quality D_LDQ in SFT yields no average gain and drops math accuracy by 4.92%, while adding only 0.4% of high-quality D_ALF* improves both average and math. The contrast is sharp and internally replicable.

- **Multi-domain, multi-stage evaluation prevents cherry-picking.** The benchmark suite covers math, science, code, general reasoning, and instruction-following across base, SFT, and RL phases. The advantage of reasoning pretraining is most pronounced in science (Table 2), a domain typically neglected in reasoning-focused work, which adds to the generality of the finding.

---

## Weaknesses

### Fatal
None.

### Major

- **Repetition confound undermines the quality-versus-diversity claim in pretraining.** D_SHQ contains 1.2M samples and D_LDQ contains 268M samples; both are expanded to fill the same 80B reasoning token budget. As Section 2.3 states, "when a reasoning dataset is small, it is repeated." This means M_SHQ is trained on data repeated approximately 50–70× (80B tokens / ~1.2M samples × average token length), while M_LDQ sees each example very rarely. Heavy repetition in pretraining is known to degrade generalization independently of data quality. The paper attributes M_SHQ's underperformance entirely to lower diversity, but the repetition effect confounds this interpretation. The paper acknowledges repetition as an implementation detail in Section 2.3 but does not treat it as the alternative explanation it is. A subsampled D_LDQ experiment (matched repetition rate to D_SHQ) would clarify whether diversity per se or repetition drives the gap. **Note:** This confound actually strengthens the SFT quality finding (D_SHQ repeated ~4× in SFT still beats D_LDQ), but it meaningfully complicates the pretraining diversity conclusion.

- **Absence of variance estimates for key quantitative claims.** The paper's two most novel, fine-grained findings—the +4.25% latent effect of M_LMQ over M_LDQ post-SFT (Table 4), and the +4.09% gain from doubling SFT epochs (Table 4)—rest on absolute differences of 3–5% with no reported confidence intervals or standard deviations. The paper does average AIME over 16 runs and other benchmarks over 4 runs, which is commendable, but without reporting variance the reader cannot assess whether the latent effect finding is robust or within run-to-run noise. Given that AIME pass@1 is inherently high-variance and contributes meaningfully to the composite "average" score, the absence of error bars is a material gap for evaluating statistical reliability.

### Minor

- **Budget-equivalence framing (Equation 2) is not enforced in the catch-up experiment.** Equation 2 frames the study as optimizing reasoning data allocation under a fixed total budget B = |D_res^PT| + |D_res^SFT|. The catch-up test for M_base doubles SFT epochs (≈9.6M samples) but does not match the 80B reasoning tokens invested in pretraining for the reasoning-trained models—a substantially larger token intervention. The paper concludes that "SFT cannot compensate for a weak foundation," which is directionally supported by the results, but the experiment does not formally test equal-budget reallocation as Equation 2 implies. This is a framing inconsistency rather than a fatal flaw: the paper convincingly shows that even doubled SFT is insufficient, but cannot claim this under a strict equal-budget allocation argument.

- **RL phase covers only two extreme models.** Table 3 selects M_LMQ + SFT_SHQ and M_base + SFT_SHQ as "two extreme pretraining backbones," omitting M_LDQ and M_SHQ from the RL comparison. The paper's claim that "pretraining strategy dictates the final accuracy ceiling" extrapolates from a two-point comparison. Whether the relationship between pretraining quality and post-RL performance is monotonic, or exhibits diminishing returns, cannot be assessed from this data.

### Trivial
None beyond parser artifacts in the extracted text.

---

## Nice-to-Haves

- A budget-matched catch-up experiment (shifting tokens from pretraining to SFT while keeping total reasoning tokens constant) would make the central budget-framing claim airtight and is the experiment the paper implicitly promises.
- For the latent effect finding, probing whether the +4.25% gain is concentrated in specific benchmarks (e.g., AIME) or broad across domains would help characterize whether it is a reasoning-specific or general alignment effect.
- A brief mechanistic probe of the latent effect (e.g., representation similarity between M_LMQ and M_LDQ before/after SFT) would elevate this from an observation to an insight.
- Reporting variance on all main tables (even just ±σ) would substantially increase confidence in the fine-grained numerical claims.
- Table 6 shows 60/40 pretraining outperforms 80/20; a follow-up on whether the 60/40 ratio changes the optimal SFT recipe (beyond Table 7's single data point) would better characterize interaction effects.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Calling 19% an 'average gain' is misleading"** (Harsh Critic, Abstract). The abstract's "19% average gain" refers to the RL comparison between the best reasoning-pretrained model and the baseline (Table 3: 56.66 − 37.92 = 18.74%). The label "average gain" is imprecise (it is a specific model comparison, not an average across strategies), but the number itself is accurate and the context in Section 4 clarifies it. Minor framing imprecision; not a substantive error.

- **"D_LMQ is overwhelmingly D_LDQ (99.6%), so 'balanced diversity with quality' overstates the quality contribution"** (Harsh Critic). The paper itself says D_LMQ = D_LDQ + D_SHQ (269.2M total). The characterization of D_LMQ as "balanced" is indeed a mild overstatement, but the paper's key claim is that even the small fraction of high-quality data in D_LMQ produces a latent effect—which is the more interesting finding, and not undermined by the labeling.

- **"The 80/20 schedule only in the final 400B tokens is unexplored"** (Harsh Critic). The paper's Section 2.3 explicitly describes this design choice and notes the 600B+400B split is for fair comparison. Criticizing the absence of alternative schedules is scope creep; the paper doesn't claim optimality of this schedule.

- **"Related work characterization of Wang et al./Ai et al. as 'math-centric' is undercut by paper's own RL focus on math"** (Harsh Critic). The RL evaluation in Table 3 includes GPQA, MMLU, MMLU-Pro, and LiveCodeBench alongside AIME/MATH-500. The framing is not undercut—the multi-domain evaluation is genuine. Criticism removed.

- **"Architecture generalizability not established"** (Harsh Critic). The paper explicitly cites Table 14 (1.2B Transformer) in Section 4: "Our experiments with a 1.2B Transformer (see Table 14) demonstrate that this front-loading strategy yields consistent, scalable performance gains." The concern is addressed; criticism removed.

- **SFT repetition of D_SHQ weakens the quality-dominates-SFT finding** (Harsh Critic). This claim is actually backwards. If D_SHQ must be repeated 4× in SFT (while D_LDQ is subsampled), repetition would be expected to hurt D_SHQ, yet it still dramatically outperforms D_LDQ. This makes the quality finding more robust, not less. Removed as a weakness.

- **Strength: "controlled experimental design with fixed budget"** (Strength Finder). This is partially valid (pretraining uses a fixed 80B reasoning token budget) but overstated given the budget-framing inconsistency in the catch-up test. Retained as a partial strength with the caveat noted above.

---

## Novel Insights

The most genuinely novel contribution of this paper is the "latent effect" observation: that high-quality pretraining data (in D_LMQ) shows no measurable advantage over large diverse data (D_LDQ) at the base model stage (64.07 vs. 64.09), yet produces a +4.25% differential after the same SFT treatment. This suggests that high-quality pretraining data shapes the model's parameter space in a way that is only revealed when alignment data provides the right "activation signal"—a kind of phase transition in capability expression. This is conceptually distinct from the standard "better pretraining → better model" story and opens a meaningful research direction: what representations does high-quality pretraining data install, and what SFT properties unlock them? The asymmetric principle itself (diversity-then-quality) is also a clean, actionable finding that the community can directly apply without the full experimental apparatus.

---

## Suggestions

1. **Add variance reporting to all main tables.** Even a single ±σ column would substantially increase confidence in the latent effect finding and the catch-up result.
2. **Explicitly discuss the repetition confound.** Section 2.3 should acknowledge that D_SHQ's 50–70× repetition rate is an alternative explanation for M_SHQ's underperformance and present it as a limitation or motivate a subsampled D_LDQ control.
3. **Run a budget-matched catch-up experiment.** Fine-tune M_base with a reasoning token count matching the 80B tokens used in pretraining (not just 2× SFT epochs). This would make the core budget-framing claim falsifiable and airtight.
4. **Characterize the latent effect by benchmark.** Report whether the +4.25% post-SFT gain of M_LMQ over M_LDQ is distributed across all tasks or concentrated (e.g., AIME). This determines whether the latent effect is a narrow or broad phenomenon.
5. **Include M_LDQ and M_SHQ in the RL phase.** Even a partial RL comparison across all pretraining configurations would enable a monotonicity assessment of the pretraining-to-RL relationship.

---

## Score and Decision

**Originality:** High. The paper addresses a genuinely underexplored question (reasoning data allocation across the full pretraining → SFT → RL pipeline), and the latent effect finding is a novel empirical observation not anticipated by prior work.

**Importance:** High. Pretraining decisions are expensive and irreversible; an actionable principle about when to deploy what kind of reasoning data has direct practical value.

**Claims supported:** Moderate-to-good. The headline claims (front-loading helps, asymmetric principle, naive SFT scaling harms) are well-supported. The latent effect claim and the quality-vs-diversity attribution are partially confounded (repetition issue) and lack variance estimates.

**Soundness:** Moderate. The experimental design is systematic and the scope is ambitious, but the repetition confound in pretraining comparisons and the missing variance reporting are genuine methodological gaps that affect the interpretability of specific claims without undermining the overall direction.

**Clarity:** Good. The paper is well-organized, the research questions are clearly stated, and the tables present results accessibly. Some framing imprecision in the abstract (e.g., "average gain") should be tightened.

**Community value:** High. A principled blueprint for reasoning data allocation is immediately applicable by anyone training LLMs, and the results on science domain improvements from reasoning pretraining add breadth beyond the math-centric focus of most prior work.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>