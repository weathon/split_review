- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 6, 6
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

The paper presents the LAM Simulator, a framework for automated generation of agentic training data through online exploration with programmatic (non-LLM-based) intermediate action and final task evaluators. The framework comprises 30 human-crafted abstract tasks, 166 hand-built tools plus 3,420 from ToolBench, and a Content Dataset of 400 entries. Two applications are demonstrated: generating preference data for DPO training (on xLAM models) and generating high-quality SFT data (from Mixtral-8x7B-Instruct-v0.1). Results on ToolEval show LAM-Sim-8x7B achieving 52.05% pass rate (18.54% relative improvement over its base), and the SFT-trained Mixtral model showing "doubling or tripling" of pass rates.

## Strengths

1. **Fully programmatic evaluators without LLM dependence** — The Intermediate Action Evaluator (Section 3.2.1) uses only rule-based checks (syntax, tool-name validity, argument correctness), and the Final Task Evaluator (Section 3.2.2) uses internal solution trajectories to derive gold labels programmatically. Table 0 explicitly marks this as a distinguishing feature from prior frameworks that rely on LLM-based or human-involved evaluation. This design enables consistent, scalable, and cost-effective feedback.

2. **Concrete, measurable performance gains** — LAM-Sim-8x7B achieves a 52.05% average pass rate on ToolEval-Cleaned, an 18.54% relative improvement over its base model xLAM-8x7B-r (43.91%), and outperforms GPT-4-0125-preview (45.46%) (Table 2). These are specific, quantified improvements that support the paper's central claims.

3. **Error breakdown ties improvement to specific error types** — Table 3 reports a 56.19% reduction in average errors for LAM-Sim-7B (from 11.67 to 5.11) and 34.21% for LAM-Sim-8x7B (from 8.44 to 5.56), with the largest gains in Tool Arguments Errors. This provides direct evidence linking the framework's feedback mechanism to concrete error correction beyond aggregate pass rates.

4. **Ablation study isolating each evaluator's contribution** — Figure 3 shows that adding low-quality intermediate data (LQ-Interim) to HQ-Data essentially nullifies agentic capability, while low-quality final responses cause ~30% relative performance decline. This supports the necessity of both evaluator types and validates the framework's design.

5. **SFT experiment shows large gains from a generic LLM** — Using only ~1,000 automatically collected SFT data points, the base Mixtral-8x7B-Instruct-v0.1 model (initially very weak at agentic tasks) achieves pass rates "doubled or tripled" on ToolEval and ToolEval-Cleaned (Tables 4, 5). This demonstrates the framework's ability to bootstrap agentic capability with minimal human annotation.

## Weaknesses

### Fatal
None.

### Major
- **DPO experiment is critically underspecified (Section 4.2.1).** The paper states it is "utilizing the action rewards" to generate preference data but never defines what constitutes an action reward. The Multi-Turn preference data generation method describes how trajectories are generated ("randomly select one response to add to the conversation history"), but it never explains how preference *pairs* (chosen vs. rejected) are constructed from these trajectories. Are pairs derived from the multiple action variations at a single step? From full-trajectory outcomes? What reward signal (binary? continuous? from which evaluator?) is used to determine preference direction? Without this information, the DPO results (Table 1, Table 2) are not reproducible and their interpretation is ambiguous — the reported improvements could arise from multiple confounded factors. This is a significant gap in a dedicated experimental section.

### Minor
- **Upfront human cost is acknowledged but under-discussed as a limitation.** The paper describes 30 human-crafted tasks, 166 manually crafted tools with detailed specifications, and a curated 400-entry Content Dataset openly, but the abstract and conclusion use phrases like "minimal human intervention" and "self-learning" without qualifying the substantial one-time engineering investment required. A more explicit discussion of the effort needed to build and maintain this infrastructure, and how it might be reduced or amortized at scale, would make the framing more accurate.

- **Ablation study does not control for dataset size (Section 4.3.3).** LQ-Interim and LQ-Final are constructed by *adding* rejected data to HQ-Data, producing datasets of different sizes and class compositions. The observed performance drop could partly reflect increased noise or training on more data rather than cleanly isolating the effect of lower-quality data. A size-controlled ablation (e.g., replacing rather than adding, or subsampling to constant size) would strengthen the conclusion.

- **No measures of statistical reliability.** No confidence intervals, significance tests, or variance across runs are reported for any experiment. Given the modest test-set sizes and the stochasticity of LLM-based evaluation and training, readers cannot assess whether the reported improvements are stable. Reporting single-run results without error bars is common practice in this area but limits the strength of the claims.

- **Error analysis methodology is underspecified (Table 3).** The paper reports "average errors (count)" but does not specify whether errors are counted per trajectory, per step, or per inference call. The denominator and aggregation method are unclear, making it difficult to interpret the absolute values.

- **ToolEval-Cleaned construction is not described.** The paper says it filters out "non-functional tools" (Section 4.1) but provides no criteria, threshold, or procedure for identifying them. This could introduce selection bias; a clearer specification is needed for reproducibility.

- **SFT data collection lacks detail on initial prompting strategy (Section 4.3.1).** The paper notes that Mixtral-8x7B-Instruct-v0.1 initially "struggles to generate any valid structured data" yet collects ~1,000 successful data points in 12 hours. No information is given about how the model is prompted, whether few-shot demonstrations or system prompts are used, or how the selection process might bias the resulting dataset.

### Trivial
- **"Table 0" numbering** is unusual and breaks convention (tables are typically numbered starting from 1). Minor formatting issue.

- **Exact-parameter template matching (Section 3)** is acknowledged as brittle (triggers an error on any mismatch) but is not discussed as a limitation. Acceptable for a first version but worth noting.

## Nice-to-Haves
- A direct quantitative comparison against data generated from prior frameworks (ToolTalk, WebArena, APIGen) on a shared evaluation benchmark would strengthen the contribution.
- A discussion of how the 30 human-crafted tasks and 166 tools might be scaled or generalized to new domains.

## Removed Points

**Criticisms removed and why:**

1. **"GPT-4 judge not validated"** — The paper follows the standard ToolEval methodology (GPT-4-0125-preview as judge), which is the established evaluation protocol for this benchmark. This is not a paper-specific flaw; it applies to every paper using ToolEval. The request to compare against the framework's own programmatic evaluators conflates internal training feedback with external benchmark evaluation, which serve different purposes.

2. **"No quality metrics for tools"** — The paper describes the 166 tools as "carefully curated" with "detailed specifications." This is a descriptive claim about design effort, not an empirical claim requiring inter-annotator metrics.

3. **"Missing related works"** — Cannot be verified without external sources. Removed per instructions.

4. **Reproducibility nitpicks about undisclosed hyperparameters, trivia** — The paper provides sufficient information for reproducibility of the core framework. Minor missing details (initial prompting for Mixtral) are covered in the Minor section above.

5. **Formatting nitpicks** (e.g., garbled text, citation style) — These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The two reviewers' analyses largely converge on the same set of issues (DPO underspecification, upfront human cost framing, lack of statistical rigor) and the same strengths (programmatic evaluators, concrete gains on ToolEval, ablation isolating evaluator contributions). No reviewer identified a perspective on the paper that the paper itself does not articulate.

## Suggestions

1. Define the reward signal and preference-pair construction procedure for the DPO experiment explicitly. Even one paragraph formalizing the process (e.g., "the Intermediate Action Evaluator's error categories are mapped to a scalar reward \(r \in \{0,1\}\); at each step, the highest- and lowest-reward action variations form a preference pair") would resolve the main reproducibility gap.

2. Report variance across multiple training/evaluation runs for at least the main result (Table 2), or provide a justification for single-run reporting.

3. Rephrase "minimal human intervention" to clarify that it refers to the data-generation *process*, not the construction of the framework itself. Acknowledge the upfront infrastructure cost as a limitation and discuss paths to reducing it (e.g., automating task/tool creation with LLMs, community contributions).

4. Add dataset-size control to the ablation study: compare LQ-Interim against HQ-Data of equal size to isolate data quality from dataset size.

5. Specify how ToolEval-Cleaned was constructed (criteria for "non-functional tools"), and clarify the error-counting methodology for Table 3 (per-trajectory? per-step?).
