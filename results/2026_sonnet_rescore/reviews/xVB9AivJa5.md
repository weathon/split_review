## Summary

Blueprint-Bench introduces a benchmark for evaluating spatial reasoning in AI models by requiring them to reconstruct 2D floor plans from apartment interior photographs. The benchmark covers LLMs, image-generation models, and agent scaffolds, producing a model-agnostic numerical comparison. The central empirical finding—that most frontier models score at or near a "no-input" baseline while human performance remains substantially higher—is interesting and plausibly directionally correct.

---

## Strengths

- **Novel, practically motivated task design.** Using in-distribution input modality (photographs) but an out-of-distribution objective (spatial 2D reconstruction) cleanly exposes a reasoning capability gap without relying on synthetic or alien inputs (Section 1, Figure 1). This mirrors the spirit of ARC while grounding it in real-world perception.

- **Model-agnostic evaluation across heterogeneous architectures.** The same task, inputs, and scoring protocol are applied to LLMs (GPT-5, Claude, Gemini, Grok), image-generation models (GPT Image, NanoBanana), and agent scaffolds (Codex CLI, Claude Code) — enabling a rare side-by-side comparison, including between a base LLM and its image-generation derivative (Section 2.2, Figure 5).

- **Clear and reproducible extraction pipeline.** The automated scoring pipeline — HSV filtering, contour detection, flood-fill segmentation, and connectivity scanning — is fully rule-based and reproducible given compliant floor plans, avoiding the LLM-based extraction pitfalls the authors explicitly tested and rejected (Section 2.3–2.4).

- **Empirically demonstrated AI blind spot.** Figure 5 shows most tested models at or below the no-input baseline (0.279), with Figure 7 establishing human performance (0.547) as a clear upper bound. This provides a concrete, quantified demonstration of a current failure mode across diverse model types.

- **Qualitative agent analysis reveals distinct failure modes.** Section 3 and Figure 8 document that Claude Code makes multiple self-correction attempts yet still fails, and that Codex never inspected its own output at all — uncovering two qualitatively different patterns of inability rather than a single undifferentiated failure.

---

## Weaknesses

### Fatal

None that are unambiguously verifiable from the paper as written.

### Major

- **The scoring metric conflates area estimation with spatial topology in a documented but unresolved way.** Section 2.4 explicitly states "the penalty of making a mistake in the size ranking causes additional penalties when scoring the connectivity." Because room IDs are assigned by size rank, a model that reconstructs correct topology but mislabels which room is second vs. third largest will have its edge-overlap score (50% of the composite) heavily penalized even though its spatial understanding is correct. The paper's own human results directly illustrate this: Section 3 reports that "all human floor plans were drawn such that the connectivity between the rooms was correct. However, they did not always get the size ranking correct," leading the authors to comment "we suspect that one similarity scoring model would make the human's lead over the AI models much larger." This is not a peripheral disclaimer — it is an admission that the primary metric does not cleanly measure what the benchmark claims to measure. For a benchmark paper whose scientific product *is* the metric, this is the central validity problem. No correlation study, alternative metric comparison, or sensitivity check is provided to show the ranking errors are small or that conclusions hold under a metric that decouples area from topology.

- **The weighting scheme is stated without justification or sensitivity analysis.** Section 2.3 assigns 50% to edge overlap, 20% to degree correlation, 10% to density, 10% to room count, 5% to door count, 5% to door orientation. No principled derivation or empirical validation of these weights is offered. A brief ablation (e.g., edge-only vs. full composite vs. equal weights) showing that model rankings are stable would substantially strengthen confidence in the benchmark, but this is absent.

- **The "random" baseline is not a statistical random baseline, and its two reported values differ without explanation.** Section 2.2 describes it as "generating typical floor plans using LLMs and image generation models without any image input" — this is a *no-input baseline*, not a randomly sampled one. The number of runs, the specific models used, and the prompts are unspecified. More critically, the baseline score differs between Figure 5 (0.279 over all 50 apartments) and Figure 7 (0.322 over the 12-apartment human subset), and neither value is characterized with variance. The claim that "most models perform at or below a random baseline" (abstract) therefore rests on a comparison whose distributional properties are unknown.

- **The ground-truth annotation process is insufficiently described for a benchmark paper.** Section 2.1 states ground truths are "adapted from the apartment listing's official floor plan image" but provides no information about annotator process, number of annotators, inter-annotator agreement, or how ambiguous cases (open-plan spaces, alcoves, half-walls) were handled. For a benchmark whose validity depends on the reliability of ground truth, this section is underspecified to the point where the reliability cannot be assessed.

### Minor

- **"Epochs" is used but never defined.** Section 3 states results are "aggregated across apartments and epochs" but nowhere defines what an epoch is in this context (presumably multiple runs of the same model on the same apartment). The number of runs per apartment per model is never stated, which affects how error bars across Figure 5 should be interpreted.

- **The conclusion about iterative refinement overreaches the evidence.** The abstract states "agent-based approaches with iterative refinement capabilities show no meaningful improvement." However, Section 3 itself acknowledges that Codex never examined its own output — it is not an iterative refinement agent in practice. The only agent that demonstrably iterated was Claude Code on one underlying model. One data point is too thin to support a general conclusion about agent refinement.

- **The 12-apartment subset used for human comparison is unexplained.** Figure 7 compares model and human performance on 12 apartments rather than all 50. It is not stated how these 12 were selected. If the human chose simpler or more visually distinctive apartments, the human baseline and the subset scores may not be representative of the full benchmark.

- **The benchmark cannot separate instruction-following ability from spatial intelligence for low-scoring models.** Section 2.4 acknowledges this as a limitation, and Section 3 attributes GPT-4o's and NanoBanana's poor scores explicitly to instruction-following failures rather than spatial reasoning failures (Figure 6). A benchmark that conflates the two has reduced diagnostic value, particularly for image-generation models — the model class whose evaluation is a stated motivating goal.

### Trivial

None.

---

## Nice-to-Haves

- A correlation study between the composite metric and human-ranked spatial quality would substantially validate the metric. Even a small-scale version on 10–15 apartments would help establish that the metric's ordering agrees with human judgment.
- A separate sub-score for topology-only (ignoring size-rank matching) alongside the current composite would let users disentangle spatial understanding from area estimation performance.
- A statistically proper random baseline (e.g., randomly sampled graphs from the empirical distribution of room counts and edge densities in the dataset) would sharpen the "at or below random" interpretation.
- Providing a summary statistic for how often size-rank errors actually occur in model outputs would let readers calibrate how much the cascade problem affects practical interpretation.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"First numerical framework" claim is unsubstantiated** (Harsh Critic, Abstract): The critic notes there are multiple spatial reasoning benchmarks. Per the hard rules, I cannot cite specific prior works I cannot verify; and the paper's specific scope (cross-architecture numerical comparison of image-generation models vs. their base LLMs) is narrow enough that the claim may be accurate within its scope. Removed to avoid speculative prior-work claims.

- **Strength: "Automated scoring is robust to LLM-based judgment failures"** (Strength Finder): This is partially valid — the authors did try LLM extraction and found it worse (Section 2.4). However, the harsh critic's point about the cascade flaw means the scoring is not as robust as claimed. The strength conflicts with a verified weakness, so it is removed per the filtering rule.

- **Strength: "Private test set fosters overfit-resistant tracking"** (Strength Finder): Generic reproducibility claim without specific evidence beyond what the paper states. Removed as insufficiently specific.

---

## Novel Insights

The most genuinely novel observation surfaced by the reviews is the interplay between the benchmark's metric design and the human-performance results: the paper's own data shows humans produce topologically correct floor plans but imprecise area rankings, causing the metric to penalize human performance asymmetrically relative to what it claims to measure. This is not merely a limitation note — it is a natural experiment that, if analyzed directly, could yield a principled argument for separating topology scoring from area-rank scoring. No prior spatial benchmarking work (to the extent cited in the paper) appears to have quantified this specific cascade effect, and the paper is in a position to contribute this insight but currently sidesteps it.

---

## Suggestions

1. **Decouple topology from area rank in the metric.** Run all models with both the current score and a topology-only score (edge overlap matching by approximate area proximity rather than strict size rank). Report both. If the relative model orderings are stable, the current metric is vindicated. If they differ substantially, the topology-only score should be the primary metric.

2. **Characterize the no-input baseline properly.** Specify exactly which models and prompts were used, how many runs, and report the variance. Alternatively, replace it with a graph-theoretic random baseline sampled from the empirical distribution of room counts and connectivity densities observed in the 50 ground-truth floor plans.

3. **Describe the ground-truth annotation process.** Add a paragraph specifying who annotated the floor plans, how ambiguous cases were resolved, and — ideally — a brief inter-annotator agreement estimate from two annotators on a small subset (5–10 apartments).

4. **Define "epochs."** Add one sentence in Section 2.2 or 3 clarifying how many runs per apartment per model were performed and how scores were aggregated.

5. **Soften the agent-refinement conclusion.** Revise the abstract and Section 3 conclusion to reflect that only Claude Code genuinely demonstrated iterative refinement, and state that one agent using one underlying model is insufficient to conclude refinement is broadly ineffective.

6. **Add a weight-sensitivity ablation.** A table showing composite scores under 2–3 alternative weight schemes (edge-only, equal weights, current) would take minimal space and substantially increase confidence in the benchmark's stability.

---

## Score and Decision

**Originality:** The task of using photos-to-floor-plans as a spatial intelligence probe is creative and distinct, but the evaluation methodology is largely ad hoc. *(3/5)*

**Importance of research question:** Evaluating spatial reasoning across heterogeneous AI architectures, including image-generation models without numerical benchmarks, is a meaningful and timely contribution. *(4/5)*

**Claims well supported:** The directional finding (models fail badly) is supported. But the specific quantitative claims—"at or below random baseline," human superiority—rest on a metric with a documented cascade flaw and an ill-defined baseline. *(2/5)*

**Soundness of experiments:** The evaluation coverage is broad; however, annotation, epochs, and baseline methodology are all underspecified, and the scoring metric conflates two distinct sub-tasks. *(2/5)*

**Clarity of writing:** Generally readable and well-structured; key definitions ("epochs") are absent and the limitations section downplays material problems. *(3/5)*

**Value to the research community:** The task, dataset, and leaderboard idea are genuinely useful; the paper would be more valuable with metric validation. *(3/5)*

The paper makes a real contribution by surfacing a concrete spatial-reasoning blind spot and constructing a practical, model-agnostic evaluation task. However, the central scientific product of a benchmark paper is the metric, and Blueprint-Bench's metric has a documented and unresolved cascade flaw, arbitrary unvalidated weights, and a poorly characterized baseline. The paper's own human results directly demonstrate the cascade problem produces unfair penalties. These are not stylistic issues; they go to whether the benchmark reliably measures what it claims. The work is fixable and the underlying task design is sound, but the paper does not yet meet the standard required of a benchmark paper at this venue.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>