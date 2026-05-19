- Decision: Accept
- Avg Score: 5.00
- Scores: 6, 3, 6
Now I have all the information I need. Let me verify the key claims against the paper and write the consolidated review.

---

## Summary

This paper introduces SysBench, a benchmark for evaluating how well LLMs follow system messages across multi-turn conversations. It constructs a dataset of 500 system messages with 5-turn user conversations, covering six constraint types (format, style, role, background, safety, output) and two alignment relationships (aligned/misaligned). It proposes three-level metrics (CSR, ISR, SSR) measuring constraint-level, instruction-level, and session-level satisfaction, and evaluates 16 diverse LLMs. The paper also conducts investigative experiments linking attention distributions to system message following.

## Strengths

1. **First systematic benchmark for system message following.** The paper identifies a genuine gap — no existing benchmark targets multi-turn system message adherence — and constructs a purpose-built dataset with 500 sessions, covering six constraint types, aligned/misaligned instructions, and dependent/parallel multi-turn conversations (Section 3.1–3.2, Table 1). This fills a clear niche relative to prior single-turn instruction-following benchmarks (Section 2.2).

2. **Three-level granularity evaluation metrics (CSR, ISR, SSR).** The metrics are well-defined and capture different granularities: constraint-level (CSR), instruction-level satisfaction (ISR), and session-level stability (SSR). SSR in particular explicitly measures degradation across consecutive turns, which is a useful design choice for the multi-turn setting (Section 3.3, Equations 1–3). The results in Table 4 (e.g., GPT-4o SSR=54.4% vs. GPT-3.5 SSR=33.9%) demonstrate that the metrics produce differentiated rankings.

3. **Broad evaluation across 16 LLMs from diverse families.** The paper evaluates models from GPT, Claude, Qwen, GLM, Llama, Moonshot, Mixtral, ERNIE, and DeepSeek (Table 2), covering both API-based and open-source models. The constraint-level breakdown (Figure 4) reveals interpretable patterns — e.g., Qwen2-7B performs well on role constraints (81.0%) but poorly on style constraints (43.3%) — providing actionable diagnostics.

4. **Investigative experiments on attention mechanisms.** The analysis linking attention score proportions to system message following (Figure 6a–6b) and the marker token experiment (Figure 6b) are informative exploratory findings. The observation that replacing system-message markers with user-message markers produces minimal attention shift (suggesting "no strict distinction between system and user messages during inference") is a concrete, testable claim that could guide future research.

5. **Explicit taxonomy of instruction alignment and multi-turn dependency.** The paper distinguishes aligned vs. misaligned instructions and dependent vs. parallel conversations, which enables structured analysis (e.g., Table 3 showing most models degrade on misaligned instructions, Table 4 showing dependent dialogues have steeper decay slopes). This goes beyond simple aggregate scoring.

## Weaknesses

### Fatal
None.

### Major

1. **Verifier validation is insufficiently detailed.** The paper claims "over 94% consistency with human evaluations" (Section 3.1) and mentions a "consistency experiment" (Section 3.3, footnote reference), but provides no breakdown: no sample size, no confusion matrix by constraint type, no inter-annotator agreement for the human labels, and no characterization of where the verifier disagrees. For a benchmark whose scores depend entirely on an LLM-as-judge protocol, this level of detail is thin. The community needs to know whether the verifier performs uniformly across constraint types (e.g., style vs. format) and alignment categories, or whether it has systematic blind spots. A single aggregate accuracy number does not establish this.

2. **Dataset construction pipeline lacks transparency on key quality-control dimensions.** The pipeline is described as: collect from online logs → filter via heuristic rules and clustering → 21 annotators refine → GPT-4o assists in generating conversations → annotators rewrite → multi-round expert checking (Section 3.2). However, the heuristic rules and clustering details are unspecified, inter-annotator agreement is unreported, and there is no analysis of potential biases introduced by using GPT-4o in the data generation step itself (which could create distributional alignment between the data and the verifier). The dataset is the bedrock of the benchmark; the current description makes it difficult to assess systematic biases.

### Minor

3. **No confidence intervals or significance tests.** All reported results (Tables 2–4, Figure 4) are presented as point estimates without standard deviations, confidence intervals, or significance tests. For a benchmark that aims to differentiate model capabilities, knowing whether a 2% gap (e.g., CSR between adjacent models in Table 2) is reliable is important. Single-run evaluation without error bars is common in this space, but the paper's claims of "significant differentiation" would be stronger with uncertainty estimates.

4. **Single verifier model (GPT-4o).** Using only GPT-4o as the judge raises the concern that its own outputs may be rated more favorably (a self-enhancement bias), and that the verifier may have systematic blind spots shared across all evaluations. A secondary verifier (e.g., Claude-3-as-judge) on a subset of data would increase confidence that rankings are not artifacts of a single judge model.

5. **Attention analysis lacks statistical rigor.** The paper states a "strong correlation" between attention score proportions and system message following ability (Section 4.5), but provides no quantitative correlation measure (e.g., Spearman rank correlation coefficient) or significance test. The analysis is based on visual inspection of three models, which is insufficient to support a correlational claim. The marker token experiment (Figure 6b) is also not controlled for positional effects — the system text is always at the beginning of the context, so the marker change confounds position with label.

6. **SSR definition overpenalizes early mistakes.** SSR requires perfect constraint satisfaction from turn 1 onward (Equation 3). A model that fails on the first turn but recovers thereafter receives SSR=0 for that session, regardless of later performance. While this is a deliberate design choice that measures stability from the start, an alternative metric (e.g., longest consecutive correct streak, or average prefix length allowing a skip) would provide a complementary view.

### Trivial
None.

## Nice-to-Haves
- An alternative SSR formulation that allows early mistakes (e.g., longest suffix of correct turns) for comparison.
- An explicit limitations section addressing: 5-turn conversation limit, English-only coverage, and dataset size (500 sessions).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Definition of misaligned instructions conflates two scenarios"** — REMOVED. The paper clearly defines misaligned instructions as those that *contradict* the system message (Section 3.1: "contradict the system messages"). The critic's suggestion that "simply not about the domain" is conflated is not supported by the text.
- **"Overstated novelty"** — REMOVED. The paper acknowledges prior work (Mu et al., Wallace et al.) in Section 2.1 and explicitly positions SysBench as more comprehensive, which is a reasonable framing.
- **"Missing limitations section"** — REMOVED. While a dedicated section would be nice, its absence is not a substantive weakness; many papers integrate limitations throughout.
- **"Reproducibility details for generation parameters"** — REMOVED. The paper specifies temperature=0 and "default settings" for other parameters, which is standard practice.
- **"Dataset accessibility / license not mentioned"** — REMOVED. The paper lists "Accessible Dataset" as a contribution; the hard rules direct reviewers to assume cited entities exist.
- **"Missing appendix content"** — REMOVED. The parser strips footnotes and appendix content; the original submission likely contained these details.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Provide verifier validation at constraint-level granularity.** Include a confusion matrix or per-constraint-type accuracy breakdown for the GPT-4o verifier against human judgments, with sample size and inter-annotator agreement statistics. This is the single highest-leverage improvement.

2. **Add confidence intervals or bootstrap estimates** for the main results (CSR, ISR, SSR) to enable readers to assess the reliability of model rankings.

3. **Include a second verifier model** (e.g., Claude-3) on a subset of the data to check whether rankings are robust to verifier choice.

4. **Report a quantitative correlation measure** (e.g., Spearman's ρ) for the attention-to-performance relationship, and control for position effects in the marker token experiment by placing system text at different context positions.

5. **Document the dataset filtering heuristics and clustering procedure** more explicitly, and report inter-annotator agreement for the manual refinement step.
