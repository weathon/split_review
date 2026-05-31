## Summary

Blueprint-Bench is a benchmark that evaluates spatial intelligence in AI systems by asking models to convert apartment interior photographs into 2D floor plans in a standardized format. The authors evaluate leading LLMs, image generation models, and agent systems using a graph-based scoring metric that measures connectivity and room-size rankings against ground-truth floor plans drawn from actual apartment listings. The main finding is that most current AI systems perform at or below a random baseline on this task, while a human participant substantially outperforms all tested models.

---

## Strengths

- **Timely and creative task design.** Choosing floor-plan reconstruction from photographs as a proxy for spatial intelligence is imaginative: the input modality (interior photographs) is squarely within modern multimodal training distributions, while the structural reconstruction task is not, enabling a meaningful blind-spot test. The analogy to ARC is apt.
- **Cross-class comparison.** Evaluating LLMs, image generation models, and agent-based scaffolds on the same benchmark with the same scoring is a novel framing that allows otherwise incommensurable systems to be compared directly.
- **Broad model coverage with frontier systems.** The paper tests GPT-5, Gemini 2.5 Pro, Grok-4, Claude Opus 4, plus image and agent variants, making the empirical snapshot timely and practically relevant to the community.
- **Open-source code and community leaderboard.** Releasing generation code and accepting submissions positions the benchmark as a living evaluation resource rather than a one-shot paper artifact.

---

## Weaknesses

### Fatal

*None that fully invalidate every claim*, but the following major issues collectively undermine the benchmark's credibility.

### Major

1. **Instruction-following is conflated with spatial intelligence.** The paper itself notes that GPT-4o and NanoBanana scored poorly due to failing to follow formatting rules (wrong colors, furniture included, missing dots) rather than failing at spatial reasoning. Yet the same metric is applied to all models without any mechanism to separate these two failure modes. A model that genuinely understands spatial layout but cannot produce syntactically valid SVG or adhere to pixel-color rules will be penalized for the wrong reason. This fundamentally undermines the paper's central claim that Blueprint-Bench measures spatial intelligence.

2. **Dataset is extremely small.** Fifty apartments with approximately 20 images each is an unusually small scale for a benchmark paper at ICLR. The human comparison is restricted to only 12 apartments with a single annotator—this is not sufficient to establish a reliable human baseline or to support statistical claims about model-vs-human gaps.

3. **Scoring metric weights are unjustified.** The composite score combines six components with a fixed weighting scheme (50% edge overlap, 20% degree correlation, 10% density, 10% room count, 5% door count, 5% orientation). No ablation or human-judgment validation is provided to show these weights reflect actual perceptual similarity. A different weighting could substantially change model rankings.

4. **Random baseline is ill-defined.** The paper says it is computed by "generating typical floor plans using LLMs and image generation models without any image input," but the resulting single number (0.279 in Figure 5; 0.322 in Figure 7 for the subset) is never explained: how many samples, which models, what variance? The discrepancy between the two figures' random baseline values is unexplained.

5. **"Epochs" are never defined.** Results are described as "averaged across epochs and apartments" throughout, but the term "epoch" is never introduced or explained. The number of independent runs per apartment per model is nowhere stated.

6. **Model category labels are inconsistent and incorrect.** In the table extracted from Figure 5, Claude Code is labeled "Image model" and CodeX is labeled "Agent," while their bar styles in the figure description (dotted = agent, striped = image model) suggest the opposite. Several other rows carry the wrong category label. This introduces confusion about what is actually being compared.

### Minor

- The statistical significance methodology is not described. The paper says "statistically perform better than the random baseline" but gives no test statistic, p-value, or confidence-interval procedure.
- The human study used only one participant. Even if that person's spatial reasoning is representative, a single annotator cannot provide inter-rater reliability or variance estimates.
- The scoring metric penalizes size-ranking errors doubly (directly and through cascading connectivity mismatches), as the authors acknowledge, but no correction or alternative is evaluated empirically.

### Trivial

- Some figure captions appear three times in the extracted text (original, alt-text, and repeat), likely a parser artifact.

---

## Nice-to-Haves

- A two-stage evaluation—first checking rule compliance (instruction following), then scoring only compliant outputs for spatial accuracy—would cleanly separate the two failure modes.
- Even a small (N=3–5) inter-annotator study for the human baseline would significantly strengthen the human–AI comparison.
- A sensitivity analysis on the weighting scheme and on the room-labeling-by-size-rank decision would help establish metric robustness.

---

## Novel Insights

The most genuinely novel observation is that agent scaffolding with iterative self-refinement (Claude Code with Opus 4) does not yield meaningful gains over single-pass generation, and that the agent's self-assessment is unreliable (it claims success when the output still contains errors). This suggests that the limiting factor is not access to a feedback loop but rather the quality of the model's internal spatial representation—a finding that, if replicated at scale, has implications for agentic spatial reasoning research. Beyond that, the comparison of image-generation models against the LLMs they are based on is a useful framing, though the sample size is too small to draw firm conclusions here.

---

## Suggestions

- Expand the dataset to at least several hundred apartments to support reliable statistical claims; even a staged release (current 50 + future additions) should be disclosed with power-analysis reasoning.
- Define and report the number of independent runs ("epochs") per model per apartment, and include variance estimates in all results.
- Add a compliance-filtering step so that models penalized purely for instruction-following failures are analyzed separately from those penalized for poor spatial reasoning.
- Validate the scoring metric against human judgments of floor-plan similarity on a small held-out set to show the weights are not arbitrary.
- Expand the human baseline to at least 3–5 independent annotators and report inter-annotator agreement.

---

## Score and Decision

Blueprint-Bench addresses a real and underexplored gap—numerically comparing spatial intelligence across heterogeneous model families—with a creative task and broad frontier-model coverage. However, the benchmark's core credibility rests on a dataset of just 50 apartments, a single human annotator, an unjustified and unvalidated scoring metric, and a fundamental confound between instruction following and the spatial intelligence the paper claims to measure. The statistical methodology is inadequately described. As currently presented, the evidence does not reliably support the benchmark's claims about measuring spatial intelligence, and the scale and rigor fall short of ICLR norms for benchmark papers.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>