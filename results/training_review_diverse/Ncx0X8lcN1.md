Now I have thoroughly verified all claims against the paper. Let me produce the final consolidated review.

---

## Summary

The paper presents HiReview, a two-stage framework for automatic literature review generation (LRG). In the first stage, it retrieves a relevant subgraph from a citation network using neighbor-aggregated BM25, then produces a hierarchical taxonomy tree via a jointly-trained GNN-based clustering module and a fine-tuned LLaMA topic generator. In the second stage, GPT-4o generates review content for each topic guided by this taxonomy. Experiments on a dataset of 518 annotated literature reviews show HiReview outperforming AutoSurvey and other baselines on LLMScore and BERTScore metrics. Code and dataset are released.

## Strengths

1. **Graph-context-aware retrieval demonstrably improves relevance.** The neighbor-aggregated BM25 scoring (Eq. 1) is a simple but effective augmentation of standard retrieval. Ablation in Table 2 confirms this: removing the retrieval module drops Coverage from 0.9163→0.6705 and Relevance from 0.9428→0.7073, establishing its critical role.

2. **Hierarchical clustering with adaptive soft-to-hard strategy is novel and well-motivated.** The clustering function uses soft clustering (overlap allowed) at the first level and hard clustering (disjoint components) at higher levels — a design choice directly motivated by the structure of literature reviews, where papers can belong to multiple subtopics but higher-level topics must be exclusive (Section 4.2.1). Table 3 shows this outperforms LLM-based and K-means clustering baselines.

3. **End-to-end integration of GNN clustering with LLM topic generation via graph-embedded prompts.** The framework jointly pre-trains the GNN for hierarchical clustering and then fine-tunes the PLM (LLaMA via LoRA) with graph embeddings from the GNN to generate central topics per cluster (Eq. 13–14). The ablation shows removing the taxonomy tree degrades Structure from 0.9484→0.8790 (Table 2), supporting the value of this integration.

4. **Consistent empirical gains across all metrics and low variance.** HiReview achieves the highest scores across all LLMScore dimensions (Coverage 0.9163, Structure 0.9484, Relevance 0.9428, Average 0.9358) and BERTScore (0.8449), with lower standard deviations than all baselines (e.g., ±0.02 Structure vs. AutoSurvey ±0.05), indicating superior consistency.

5. **New annotated dataset.** A dataset of 518 literature reviews with extracted taxonomy trees and 2-hop citation networks (average 6,658 papers and 11,632 edges per review) provides a structured benchmark for future LRG research.

6. **Clear problem decomposition.** The paper explicitly formulates three key challenges (retrieval from large citation networks, joint text+topology clustering, hierarchical taxonomy generation) and designs dedicated modules for each, making the contribution easy to follow.

## Weaknesses

### Fatal
None.

### Major

1. **No human evaluation; primary metric (LLMScore) uses LLM evaluators with potential same-family bias.** The paper relies on LLMScore, evaluated by "multiple LLMs" (unspecified which ones, line 203), while the content generator for HiReview and AutoSurvey is GPT-4o. Even though the paper cites AutoSurvey's finding that "LLM-based evaluations of literature review align well with human preferences," this does not rule out a relative bias when the same model family both generates and judges. Without any human evaluation (expert ratings, user studies, or even small-scale annotations), the central claim that HiReview produces *superior* reviews rests on a single automated metric class whose calibration for this specific comparison is untested. This is the most consequential weakness for the paper's credibility.

2. **Ablation confound prevents isolating the contribution of hierarchical clustering.** The "w/o clustering*" variant removes clustering *and* switches from fine-tuned LLaMA to GPT-4o as the topic generator (the paper acknowledges this on line 211: "It is marked with * because the topic generator in this case is an LLM i.e., GPT-4o, rather than a fine-tuned LLaMA"). Two variables change simultaneously. The variant still achieves 0.8612 Coverage and 0.9078 Relevance — close to AutoSurvey's 0.8646 and 0.9093 — so it is unclear whether the gain of the full HiReview over AutoSurvey comes primarily from graph-context-aware retrieval, from hierarchical clustering, from the fine-tuned topic generator, or from their interaction. A cleaner comparison (e.g., using HiReview's own fine-tuned LLaMA with and without clustering) is needed to attribute gains.

3. **Only paper titles are used as textual input throughout the pipeline.** The retrieval step (Section 4.1) computes BM25 between query and paper *titles*. The clustering step (Section 4.2.1) uses "the title of nodes to initialization text embedding." The topic generation step (Section 4.2.2) uses "the titles of all papers under node j." No abstracts or full-text content are incorporated at any stage. A literature review is expected to discuss methods, results, and findings — information rarely conveyed fully by titles alone. This limitation constrains the depth and informativeness of the generated reviews and weakens the practical significance of the claimed results.

4. **Dataset construction and clustering evaluation metrics are underspecified.** (a) The 518 taxonomy trees were "extracted" from review articles (line 199), but the extraction methodology is not described (manual? automated from ToC/section headings? with what criteria?). No inter-annotator agreement is reported. (b) The clustering evaluation in Table 3 reports "Accuracy" without defining it in the text. The paper states "As shown in Table 3, when considering the clustering task alone, both baselines underperform" — but without knowing what Accuracy measures or what the ground-truth clusters are (how were the reference hierarchical clusters derived from the 518 reviews?), the clustering results are not interpretable.

### Minor

1. **BERTScore is not informative for this task.** It measures token-level n-gram overlap with a single human-written reference review, which is only one possible valid organization of the same papers. The score differences are small (0.8449 vs. 0.8256) and the paper does not interpret them. This metric adds little evidentiary value.

2. **Hyperparameter α in the graph context-aware retrieval (Eq. 1) is not specified or ablated.** The paper says the aggregation of neighbor scores "leads to a significant improvement" (line 100) but reports no α value, sensitivity analysis, or selection procedure. This impacts reproducibility.

3. **Number of hierarchical levels in the taxonomy is not reported.** The clustering process recurs "until a stopping criterion is met" (line 108), but the actual number of levels used in experiments — a basic architectural parameter — is not stated.

4. **Training details are sparse.** LoRA rank, learning rates, batch sizes, GNN architecture (number of GAT layers, hidden dimensions), and hardware are not reported. This hinders reproducibility.

5. **No qualitative examples or failure analysis.** The paper would benefit from at least one concrete example comparing a HiReview-generated taxonomy/review with an AutoSurvey output, to help readers assess quality qualitatively and understand failure modes.

### Trivial

- Notation mismatch in the preliminaries: Eq. 3 uses $\bar{C}_l = \bar{f}(\bar{G}_l)$ while the method section uses $C_l = f(G_l, X_{G_l})$. The meaning is clear but inconsistent.
- The claim that existing methods "overlook critical prior knowledge, such as citation relationships" (line 23) is slightly overstated — AutoSurvey's retrieval pipeline could incorporate citation patterns implicitly — though the paper's broader point that no prior work explicitly models citation topology for LRG stands.

## Nice-to-Haves

- Incorporating abstracts (in addition to titles) for retrieval and clustering would substantially strengthen the generated reviews' informativeness and the paper's practical relevance.
- A human evaluation study — even modest in scale (e.g., 20 queries × 3 expert judges on coverage, structure, factual accuracy) — would transform the strength of the empirical evidence.
- A comparison of the proposed neighbor-aggregated BM25 against the exact retrieval method used by AutoSurvey would help disentangle the contributions of retrieval vs. hierarchical taxonomy.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Criticism about "the same LLM family used for both generation and evaluation is a well-known risk of superficial agreement"* — Retained (Major #1) but in a softened form. The concern is real but the paper does cite prior validation and uses "multiple LLMs" (not just GPT-4o). The core issue is the absence of human evaluation, not that the metric is invalid.
- *Complaint that standard deviations are not used for statistical significance testing* — Removed. Significance testing with overlapping ±1σ ranges is not the standard in this benchmark-driven line of work, and the paper's improvements are consistent across all metrics.
- *Claim that "the primary evaluation metric (LLMScore) is inadequate and introduces systematic bias" framed as structural/fatal* — Downgraded to Major. The metric is standard in the field (used by AutoSurvey itself) and the paper cites validation. The real gap is the absence of human evaluation, not that LLMScore is invalid.
- *"The method is good at organizing paper titles but does not generate depthful, content-rich reviews"* — Retained as Major #3 but stated as a limitation rather than a fatal judgment.
- *Criticism that "the paper's claim that existing methods 'overlook critical prior knowledge, such as citation relationships' is too strong"* — Downgraded to Trivial. The claim is defensible: AutoSurvey does not explicitly model citation topology, even if it may capture some relationships implicitly through retrieval.
- *"The formal definition of hierarchical graph clustering (Equation 3) uses notation that does not match the method section"* — Moved to Trivial.
- *Strength Finder's item 6 ("Systematic ablation validating each component")* — Kept but note the confound in w/o clustering* weakens the "systematic" characterization.
- *Strength Finder's item 7* — Kept.
- *"No discussion of how many levels are used"* — Moved to Minor.
- *"No failure analysis or qualitative examples"* — Moved to Minor.
- *"Training details are sparse"* — Moved to Minor.
- *"Computational cost not discussed"* — Moved to Nice-to-Haves.
- *Complaint about "no ablation showing the effect of the soft-to-hard design choice"* — Removed as scope creep; the ablation already covers retrieval, clustering, and taxonomy removal.
- *Criticism about table 3 only showing "Accuracy" with no NMI/ARI/F1* — According to the Strength Finder, the table may include NMI and ARI values (the table is an image). The issue is the text doesn't define "Accuracy," which is retained as Major #4b.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a clear tension: the paper presents a well-designed and well-motivated pipeline with consistently positive results, but the evaluation framework — no human study, a confounded ablation, and titles-only input — does not match the strength of the claims. The most valuable observation from the cross-review is that fixing these evaluation gaps (especially the human evaluation and the ablation confound) is largely an engineering/effort problem, not a methodological flaw, meaning the paper's core technical contribution is likely sound but currently undersupported.

## Suggestions

1. **Add a human evaluation.** Even a modest study (20 queries, 3 judges) rating coverage, structure, and factual accuracy would substantially strengthen the empirical foundation and address the most serious weakness.
2. **Disentangle the ablation confound.** Compare HiReview against a variant that uses graph retrieval *with* the fine-tuned LLaMA topic generator but *without* hierarchical clustering (i.e., flat topic generation). This isolates the marginal contribution of the hierarchical taxonomy.
3. **Describe the taxonomy extraction process** for the 518 reviews and define the clustering evaluation metric. Report inter-annotator agreement if extraction was manual.
4. **Add abstract-level information** to at least one pipeline stage and discuss the current titles-only limitation explicitly.
5. **Report key hyperparameters** (α, number of hierarchical levels, LoRA rank, learning rates, GNN layers/hidden size, hardware).

## Score and Decision

The paper presents a technically sound and well-motivated framework for an important problem. The core ideas — graph-context-aware retrieval and soft-to-hard hierarchical clustering for taxonomy generation — are novel and clearly explained. The results are consistently positive across all metrics. However, the evidence for the central claim is weakened by three structural gaps: no human evaluation, an ablation confound that prevents isolating the key contribution, and titles-only input that limits depth. These are addressable, but in their current form, the paper's claims outpace its support.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>