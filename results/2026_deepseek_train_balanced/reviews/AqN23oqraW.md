Now let me produce the final review.

## Summary

KoLA is a benchmark for evaluating world knowledge in LLMs, organized around a four-level cognitive taxonomy (Knowledge Memorization, Understanding, Applying, Creating) covering 19 tasks. Its key design innovations are (1) a continuously refreshed "evolving data" source to prevent test-set leakage and (2) a self-contrast metric that compares a model's free-form generation against its own knowledge-grounded generation to evaluate knowledge hallucination. The authors evaluate 28 models across two seasons and report rankings and findings about model size and alignment effects.

## Strengths

- **Self-contrast metric with human validation**: The paper proposes a novel metric (Eq. 4) that isolates knowledge faithfulness from writing style by contrasting a model's free completion against its own knowledge-grounded completion. Human evaluation shows a 0.61 Spearman correlation between the self-contrast component and human-judged faithfulness, and removing it causes a 32% drop in correlation with human overall quality (§4, line 247). This addresses a genuine open problem with non-trivial validation evidence.

- **Evolving data mechanism addresses test-set leakage**: The seasonal refresh design (≥500 newly crawled articles every 3 months, §2.2, lines 58–62) directly confronts the problem of static benchmarks where test data may leak into training. The paper validates this empirically by showing a linear correlation between evolving and non-evolving task results (§4, line 245), confirming that the evolving data measure related constructs while remaining unseen.

- **Four-level taxonomy with empirical grounding**: The Bloom's-inspired hierarchy (KM→KU→KA→KC) is supported by within-level task correlations and cross-level dependency patterns (§4, lines 243–244), providing evidence that the taxonomy captures genuine ability structure rather than being an arbitrary grouping.

- **Large-scale comparison yielding non-trivial findings**: Evaluation of 28 models reveals substantive patterns — the alignment tax on memorization, the correlation between model size and KM for non-aligned models (Spearman 0.79), and the relative decline of open-source models across seasons — that go beyond confirming known trends.

## Weaknesses

### Fatal
None.

### Major

- **Severe floor effects on KU tasks undermine rankings for the majority of models**: Inspection of Table 1 (lines 167–194) shows that 15/28 models score exactly 22.0 on COPEN-CSJ (2-1), 13/28 score exactly 18.4 on COPEN-CPJ (2-2), 11+ score exactly 18.3 on COPEN-CiC (2-3), and 21+ of 28 models score exactly 25.0 on ETU (2-8). These are standardized scores (0–100 scale after z-score + min-max scaling), meaning raw performance collapsed to indistinguishable values for most models. For ETU (the evolving task at KU level), essentially every model except the top three receives the same score. This means the KU-level rankings for the bottom ~75% of models provide no meaningful signal. The paper does not acknowledge or discuss this pattern, and it raises questions about whether these tasks should be weight-bearing in the overall benchmark. When most models produce identical scores, conclusions about relative KU performance across the model set are unsupported.

- **Test set sizes are too small to support fine-grained ranking claims**: Almost every task uses 100 test instances or fewer (Table 1: ETM: 100, COPEN tasks: 100 each, DocRED: 100, MAVEN: 100, HotpotQA: 100, 2WikiMultihop: 100, MuSiQue: 100, KQA Pro: 100, KoRC: 100, ETA: 49, KC tasks: 95). The paper's headline output is a ranked list of 28 models with fine-grained distinctions (e.g., rank 7 vs. 8), but no variance estimation, confidence intervals, or bootstrapped ranking distributions are reported. With N=100 per task, the difference between adjacent ranks could easily flip with a different sample. This is a widespread issue in the benchmark literature, but the confident, precise tone of the claims (e.g., "InstructGPT davinci v2 ranks 7th in KM") outpaces what the evidence can statistically support.

- **Archive of Our Own (AO3) as the evolving data source is conceptually mismatched with the stated goal of "world knowledge" evaluation**: The paper cites `archiveofourown.org` (primarily a fanfiction archive) as the evolving data source (§2.2, line 61). The ETM task extracts knowledge triplets from these articles — but when articles contain fictional events and characters, the "correct" knowledge triplet is fictional, not world knowledge. The paper's title and framing commit to evaluating "world knowledge." While the paper explicitly includes fiction in its scope for KC tasks (line 99: "narrative texts such as history, news, and fiction"), the KM and KU evolving tasks extract factual claims from narratives where ground truth is defined by a fictional universe. The paper does not acknowledge or address this tension. This undermines the construct validity of the evolving-knowledge evaluation for KM and KU levels.

### Minor

- **Self-contrast metric has a partially unresolved circularity concern**: The metric contrasts a model's free completion T with its knowledge-grounded completion Tk (given gold knowledge K). The paper acknowledges (§2.3, lines 130–136) that if the model ignores K, Tk ≈ T due to self-consistency rather than knowledge correctness. The mitigation (averaging in ∂(T,R) and ∂(Tk,R)) uses ROUGE-L similarity, which correlates poorly with factual correctness. The human validation (0.61 correlation, 32% drop) provides some empirical support, but a cleaner control experiment (e.g., giving the model scrambled or irrelevant K) would substantially strengthen the validity claim.

- **"Known data" assumption is cleaner in principle than in practice**: The paper assumes all LLMs are trained on Wikipedia and uses Wikidata5M (2019 dump). This is reasonable as a first approximation, but: (i) different models use different Wikipedia snapshots; (ii) the known tasks reformat Wikipedia content into probing templates and extraction schemas unseen during pre-training, so poor performance may reflect format mismatch; (iii) models like T0++ and FLAN-T5 were fine-tuned on instruction datasets that may include KU/KA-like tasks. The claim that known-data evaluations "fairly compare the learning efficiency of LLMs" (§1, line 30) overstates the design's precision.

- **Small-N correlations used for key claims without disclosure**: The Spearman correlation of 0.79 between model size and KM for "models without alignment or instruction tuning" (§3, line 149) is computed on roughly 7 models. The alignment analysis (KA correlation from 0.02 to 0.53, line 151) uses an undisclosed subset. These are suggestive observations, not robust findings, and the limited Ns should be explicitly noted alongside the correlations.

- **Missing prompt templates and evaluation details**: The paper does not describe how prompts were designed for any of the 19 tasks, whether they varied across models, or what default prompting strategy was used. For benchmark results highly sensitive to prompt phrasing, this is a reproducibility concern.

### Trivial
None.

## Nice-to-Haves

- Report confidence intervals or bootstrapped ranking distributions to quantify ranking stability.
- Replace or rigorously justify the AO3 data source; using recent news articles would directly align with the "world knowledge" framing.
- Add a control experiment for the self-contrast metric (scrambled/irrelevant K) to validate it measures knowledge faithfulness, not self-consistency.
- Release full prompt templates and annotation instructions for all tasks.
- Report raw (non-standardized) scores alongside standardized scores so readers can diagnose floor/celling effects.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Context length as a confound"** (harsh critic): The paper marks "---" for models whose context length prevents evaluation on long-document tasks. This is transparent data reporting, not a confound. REMOVED: paper handles this appropriately.
- **"No analysis of model family effects"** (harsh critic): This is a nice-to-have extension. REMOVED: scope creep beyond the paper's stated contribution.
- **"No discussion of whether scores are computed per-example or aggregated"**: Standard implementation detail. REMOVED: nitpick.
- **"Human evaluation only reports a single number, not distributions"**: The paper states annotation details are in the appendix (§4, line 247). The parser strips appendices from all papers. REMOVED: missing appendix content is not a valid criticism.
- **"Blurred boundaries between KM and higher levels undermine the taxonomy"**: The paper explicitly discusses cross-level correlations (line 243: "KM level shows notable correlations with other levels") and frames this as an empirical finding about ability structure, not a design flaw. REMOVED: the paper treats this as a finding, not a weakness.
- **Strength Finder's generic strengths** (e.g., "addressed an important problem", "targeted an interesting question"): REMOVED: generic/superficial, not backed by specific evidence.

## Novel Insights

The harsh critic's observation about the floor effects on COPEN tasks and ETU — where 15–21+ of 28 models receive identical standardized scores — reveals a blind spot in the paper's own analysis. The paper reports "high correlation among tasks within each level" as evidence of taxonomic coherence, but this within-level agreement may be artifactually inflated by floor effects: when most models score identically at the bottom of a task, any two such tasks will mechanically correlate. This suggests the KU level needs a more careful treatment: some tasks (COPEN probing) may be operating below the discrimination threshold for most current LLMs, and mixing them with better-ranging tasks (FewNERD, some relation extraction) in a single standardized score may produce misleading KU rankings. This is a concrete diagnostic finding that the paper should investigate, not a fatal flaw.

## Suggestions

1. Report raw (non-standardized) scores for all tasks in a supplementary table and explicitly discuss which tasks exhibit floor/celling effects.
2. Add bootstrapped confidence intervals around task-level and aggregate rankings.
3. Provide a clear justification for the AO3 source in the context of world knowledge, or replace it with a more directly aligned source (e.g., recent news articles from a news API).
4. Add a control experiment giving the model irrelevant/scrambled K to validate the self-contrast metric.
5. Release full prompt templates for all 19 tasks.
6. Disclose the number of models used for each correlation claim (e.g., N=7 for the 0.79 Spearman).

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>