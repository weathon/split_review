- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5
Now I have thoroughly verified the claims against the paper. Let me produce the consolidated review.

## Summary

This paper introduces MeCo, a fine-tuning-free plug-in module that uses representation-level probes (via the RepE framework) to detect "meta-cognition" signals in LLMs — defined as the model's self-assessment of whether it can answer a query independently or needs external tools. A dual-threshold decision strategy based on probe scores determines when to invoke tools or retrieval. The paper also introduces MeCa, a new human-verified benchmark with 7,000 queries across 6 tool-use and RAG tasks. Experiments on Llama-3-8B/70B and Mistral-7B show consistent decision-accuracy improvements over two baselines (Naive first-token classification and a confidence-adjusted variant, P_Yes) on both Metatool and MeCa, including in an adaptive RAG setting.

## Strengths

1. **Consistent, non-trivial gains across models and benchmarks.** Tables 1–3 show MeCo improving over the Naive and P_Yes baselines across Llama-3-8b, Llama-3-70b, Mistral-7b, and their fine-tuned variants, under both with-context and without-context settings. The improvements are typically 5–10 percentage points and hold across tool-use and RAG tasks. (Tables 1, 2, 3)

2. **Fine-tuning-free and lightweight.** MeCo requires no fine-tuning of the backbone LLM and only a small number of query-response pairs to train its linear probe. This makes it orthogonal to fine-tuning — the paper shows gains even on already fine-tuned models (e.g., Llama-3-8b-sft). (Section 3.1, Tables 1–2)

3. **New benchmark (MeCa) addressing a gap.** MeCa provides 7,000 human-verified queries across 6 tasks spanning Tool Usage Assessment, Provided Tool Evaluation, Multi-turn Interaction, and RAG. Existing benchmarks like Metatool are limited to single-tool, no-context settings. (Section 4)

4. **Threshold transferability demonstrated.** Thresholds fitted on Metatool transfer effectively to MeCa-Tool Tasks 1 and 4, showing that the decision strategy generalizes across different tool sources and query styles. (Section 6.1, Table 2)

5. **Unified framing of adaptive tool use and adaptive RAG.** The paper treats RAG as a specific instance of tool use and validates MeCo in both settings, lending generality to the approach. (Section 6.2, Table 3)

## Weaknesses

### Fatal
None.

### Major

1. **Probe training procedure is underspecified.** The paper states that a "leading proprietary LLM" generates tool-use queries and Yes/No responses, and that training follows the RepE pipeline from Section 2. However, Section 2's generic pipeline (contrastive instruction pairs T_f^+ / T_f^- for "honesty"/"confidence") is not clearly translated to the meta-cognition setting. What specifically constitutes the experimental condition (strong meta-cognition) versus the reference condition (weak meta-cognition)? Without specifying the contrastive instructions used to elicit these two states, the probe could be learning a spurious correlation (e.g., distinguishing query types rather than meta-cognition). The paper's core claim depends on this probe capturing a meaningful internal signal, yet the training protocol is not reproducible from the description as given. (Section 3.1, Section 2)

2. **No comparison to any established adaptive retrieval method.** The paper compares MeCo only against Naive (first-token) and P_Yes (logit-rescaling) baselines. While these baselines help isolate the value of representation-level information, the paper frames adaptive RAG as a special case of tool use and claims MeCo is "superior" — yet does not benchmark against any existing adaptive retrieval approach (e.g., Self-RAG, FLARE, or even a simple entropy-threshold baseline). Without such contextualization, it is unclear whether the reported gains are meaningful relative to prior work or whether existing methods already achieve similar or better accuracy. (Section 5, Section 6.2)

### Minor

1. **No ablation of design choices.** The decision strategy reduces the (m × n) meta-cognition array to a single scalar by: (a) keeping only the first token, and (b) selecting a single layer from layers -5 to -2 based on validation accuracy. The paper provides some justification (first token = Yes/No, shallower layers are more effective) but no ablation comparing alternatives (e.g., averaging across layers, using the last token, or a learned combination). The selected layer is also data-dependent; without quantifying variance across choices, the reported performance could partly reflect fortuitous hyperparameter selection. (Section 3.2)

2. **No statistical significance or variance reporting.** Tables 1–3 report only point accuracies. No confidence intervals, standard deviations, or multiple-run averages are provided. Given that some test sets are as small as 100 queries (hold-out sets for Tasks 2, 3, 5, 6 in MeCa-Tool), differences of a few percentage points may not be significant. (Tables 1–3, Section 6.1)

3. **Human verification of MeCa is not quantified.** The paper states that MeCa queries underwent "rigorous human review" but provides no details on the number of queries reviewed, inter-annotator agreement, or how disagreements were resolved. This limits confidence in benchmark quality claims. (Section 4)

### Trivial
None.

## Nice-to-Haves

- **Comparison to a representation-based uncertainty baseline.** For instance, training a logistic regression on the last-layer hidden state of the first token to predict tool need, and comparing MeCo's probe to that, would more directly isolate the value of the meta-cognition direction versus any representation-level signal.
- **Error analysis / confusion matrices.** The paper reports only accuracy. Showing when MeCo makes mistakes (false positives vs. false negatives, per task category) would strengthen the claims.
- **Computational overhead measurement.** The paper claims MeCo incurs "minimal cost" but provides no runtime measurements. Quantifying the probe inference overhead relative to the model forward pass would substantiate this claim.
- **More systematic transfer experiments.** Threshold transferability is shown for only two tasks (MeCa-Tool Task 1 and Task 4). Expanding to additional tasks or different backbone models would strengthen the robustness claim.

## Removed Points

These points were identified by the reviewer(s) but are not valid weaknesses upon verification:

- **"Probe classification accuracy near 100% is suspicious"** — The meta-cognition probe is evaluated on held-out examples from its own training distribution; near-optimal accuracy on a well-separated binary classification task is expected for a linear probe in a high-dimensional representation space, not suspicious. The comparison to honesty/confidence probes (Figure 3) uses different datasets, but the paper explicitly acknowledges this difference (Section 3.1).
- **"GPT-4-turbo's more up-to-date information lowers accuracy on MeCa-RAG — this is a red flag"** — The paper's explanation is coherent: GPT-4-turbo has a later training cutoff, so it answers more queries from internal knowledge (saying "No" to retrieval), but some of those queries require retrieval, causing more errors. This is a known phenomenon, not a benchmark artifact.
- **"Benchmark evaluation selectively uses only parts of MeCa"** — The paper evaluates on all 6 MeCa-Tool tasks, using threshold-transfer for Tasks 1 and 4, and sampling 100 queries per task as hold-out for the remaining tasks (where thresholds do not transfer). The full 7,000-query dataset is used for threshold fitting and evaluation; the paper describes this split explicitly.
- **"Missing related works / unfair comparison without Self-RAG/FLARE"** — Partially addressed in Major weakness #2 above, but the critic's framing as "existing methods are ignored" is too strong. Self-RAG and FLARE involve fine-tuning and substantially different setups; the paper's scope is a fine-tuning-free plug-in.
- **"Multi-turn scenarios invalidate the first-token strategy"** — The paper uses a "Yes/No + Explanation" prompting strategy (Section 5), so even in multi-turn settings the first token is Yes or No by instruction design.
- **"First-token reduction not justified for multi-turn"** — See above; the prompting strategy addresses this.
- **"The 'recent news' vs. 'common facts' split conflates recency with necessity"** — The paper explicitly ensures recent news postdates LLM training data. The critic's speculation that "many recent news items are already in LLM training data" has no evidence and contradicts the paper's stated methodology.
- **Formatting, style, and reproducibility nitpicks about missing appendix content, hyperparameters, etc.** — The appendix was stripped by the parser; these sections exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the paper's strengths (consistent gains, new benchmark) and weaknesses (probe training underspecification, missing ablations) without producing a novel synthesis.

## Suggestions

1. **Specify the contrastive instruction pairs for meta-cognition explicitly.** State what T_f^+ and T_f^- are (e.g., "Answer honestly about whether you need a tool" vs. "Overestimate your capabilities and claim you don't need a tool"), or explain if and how the generated Yes/No responses are labeled as correct/incorrect and used as positive/negative examples.
2. **Add at least one established adaptive retrieval baseline** on the MeCa-RAG task — e.g., Self-RAG, FLARE, or a simple confidence-threshold baseline — to contextualize MeCo's gains relative to prior work.
3. **Conduct an ablation study** comparing the chosen configuration (first token, single best layer from -5 to -2) against alternatives (average across layers, last token, all layers averaged, learned combination) and report variance across design choices.
4. **Report confidence intervals or standard deviations** from multiple runs, especially for the 100-query hold-out sets where small sample sizes amplify variance.
5. **Quantify human verification of MeCa** — report the number of queries reviewed, inter-annotator agreement statistics, and resolution protocol for disagreements.
