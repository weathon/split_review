Now I have all the information I need. Let me produce the consolidated review.

## Summary

The paper proposes IntentGPT, a training-free method for few-shot intent discovery that leverages LLMs (GPT-3.5, GPT-4, Llama-2) through in-context learning. It combines an automatic In-Context Prompt Generator, a Semantic Few-Shot Sampler, and Known Intent Feedback to discover and reuse intents without fine-tuning model weights. Experiments on CLINC and BANKING datasets report competitive or superior results against unsupervised and semi-supervised baselines.

## Strengths

- **Training-free paradigm avoids multi-stage training pipelines.** IntentGPT requires no weight updates, using only frozen LLMs with prompting. On CLINC (50-shot, GPT-4) it achieves NMI 96.06, ARI 84.76, ACC 88.76, surpassing semi-supervised methods like LatentEM (NMI 95.01, ARI 83.00) and SCL (NMI 94.75, ARI 81.64) that require training (Table 1). This is a genuine practical advantage if the evaluation is valid.

- **Ablation study convincingly isolates the contribution of each component.** Table 2 shows that removing Known Intent Feedback (KIF) causes the number of discovered intents to explode (e.g., 1484 vs. ground-truth 150 on CLINC with GPT-3.5), and that combining KIF, SFS, and ICP yields the best results. This is a clean demonstration of why each design choice matters.

- **Model-agnostic framework validated across three LLM families.** Results are reported for GPT-3.5, GPT-4, and Llama-2, with consistent trends (GPT-4 > GPT-3.5 > Llama-2), showing the method is not tied to a single API or model.

- **Automatic prompt generation (ICP) demonstrably improves results.** The In-Context Prompt Generator eliminates manual prompt engineering. Table 2 shows that adding ICP on top of KIF+FS+SFS raises NMI from 93.89 to 94.99 (GPT-4, CLINC), validating the approach.

## Weaknesses

### Fatal
None.

### Major

1. **Evaluation protocol is critically underspecified, potentially invalidating comparisons with baselines.** The paper states (line 86): *"We compute SBERT embeddings on predicted and ground truth intents and perform K-Means clustering."* This is ambiguous: "intents" could mean the predicted **intent-name strings** (e.g., "change_password") or the **utterances** with their intent labels. The baselines (DeepAligned, SCL, DSSCC) cluster **utterance embeddings** — a fundamentally different operation. If IntentGPT clusters intent-name embeddings rather than utterance embeddings, the evaluation measures whether predicted names are semantically similar to ground-truth names, not whether utterances are correctly assigned to intent clusters. These are different quantities, and the paper provides no justification that they are comparable. The paper claims to *"adopt the evaluation framework proposed by Zhang et al. 2021"* (line 203), which uses utterance-level clustering, but the actual description on line 86 suggests a different procedure. **This must be resolved for the core empirical claims to be verifiable.** The authors should either (a) confirm they follow the standard utterance-level clustering protocol, or (b) acknowledge that intent-name clustering is a different evaluation and justify why the comparison to baselines is valid.

2. **Mentioned datasets (SNIPS, StackOverflow, multilingual) appear in the Datasets section but no results are ever presented for them.** The paper says *"We also evaluate our method on datasets with less number of intents like SNIPS and StackOverflow, and multilingual data"* (line 201), yet Tables 1 and 2 only report CLINC and BANKING. No appendix or note explains their absence. This suggests incomplete experimentation or selective reporting.

### Minor

1. **The "training-free" framing obscures the extent of labeled data used.** The Few-Shot Pool contains 10% of training samples per known intent (line 74), which on CLINC with 150 intents amounts to hundreds/thousands of labeled utterances. The actual number injected into the prompt (2-50) is smaller, but the pool itself is a labeled resource larger than what "few labeled examples" in the abstract suggests. The paper should state the total labeled data required more prominently.

2. **DBSCAN with fixed ε=0.5 is used to determine K for K-Means without any sensitivity analysis.** The number of clusters K is critical for clustering metrics, and DBSCAN's output is known to be sensitive to ε. The paper provides no analysis of how results change with different ε values or whether the fixed ε works across datasets.

3. **Llama-2 variant (70B) is only specified in figure captions, not in the method description or main text.** The reader has to find it in captions (lines 220, 227). The main text should state the variant explicitly.

4. **No qualitative analysis of discovered intent names.** The paper reports NDI (count) but does not analyze whether discovered names are semantically meaningful, consistent across utterances, or overlapping with ground-truth names. A qualitative analysis would strengthen the contribution.

5. **No discussion of potential data leakage.** LLMs like GPT-4 may have been exposed to CLINC and BANKING during pre-training. This could artificially inflate results (the model may "remember" intent names rather than genuinely discovering them). The paper should acknowledge this limitation.

6. **No cost/feasibility analysis.** Running GPT-4 on thousands of test examples has real monetary and environmental cost. A brief discussion of average API cost per experiment would help readers assess practical feasibility.

### Trivial
None.

## Nice-to-Haves

- A controlled experiment removing the Few-Shot Pool entirely (pure zero-shot with only KIF) to test whether the retrieval-based sampling adds value beyond the LLM's own knowledge.
- Reporting standard deviations or error bars, especially for the 0-shot setting where variance may be lower.
- Analysis of how the LLM's context length limits the number of shots and discovered intents that can be included in a single prompt.

## Removed Points

- **Criticism that evaluation is "fundamentally inconsistent" / "not measuring the same thing":** Kept and elevated to Major Weakness #1 because it raises a legitimate ambiguity. However, the critic's characterization of it as definitively fatal is softened — the paper's description is genuinely ambiguous and could be clarified. The critic's claim that "every number in Tables 1 and 2 reports a different quantity" assumes a particular reading that may not match the authors' actual implementation.

- **Criticism about "Known Intent Feedback" showing fragility of zero-shot prompting:** This is already discussed by the paper (lines 232–233). The paper acknowledges that KIF is essential for reasonable NDI, and the ablation table is presented precisely to show this. Not a weakness — it's an intended feature of the design.

- **"Baseline asymmetry favors the author's method":** The critic argues the evaluation paradigm favors IntentGPT. This is folded into Major Weakness #1 since the actual evaluation protocol is unclear.

- **Strength about outperforming prior methods:** Kept as a strength with the caveat that it depends on evaluation validity.

## Novel Insights

None beyond the paper's own contributions. The reviews jointly surface the key unresolved question (evaluation protocol) but do not add a new conceptual angle.

## Suggestions

1. **Clarify the evaluation protocol immediately.** State explicitly: (a) what exactly is being clustered — intent-name strings, utterance embeddings, or something else; (b) how the predicted and ground-truth clusterings are aligned for NMI/ARI/ACC computation; (c) whether this matches the protocol used by all baselines cited in Table 1. If the evaluation deviates from the standard, provide a justification or adopt the standard instead.

2. **Include results for SNIPS, StackOverflow, and multilingual data** or remove them from the Datasets paragraph. Omitting results for datasets you claim to evaluate on is a clear omission.

3. **Provide a DBSCAN ε sensitivity analysis** (e.g., a sweep over 0.1–1.0 showing NMI/NDI stability) to demonstrate that results are not artifacts of a particular parameter choice.

4. **Explicitly compare the total labeled data budget** between IntentGPT and each semi-supervised baseline, so readers can assess the claimed data efficiency fairly.

## Score and Decision

The paper proposes a clean, conceptually appealing approach to intent discovery using frozen LLMs. The ablation study is thorough, and the framework's model-agnostic nature is a genuine strength. However, the evaluation protocol — the very foundation of the empirical claims — is critically underspecified. The central ambiguity about whether intent-name embeddings or utterance embeddings are clustered, and how this relates to the standard evaluation used by all baselines, must be resolved before the results can be trusted. Until this is clarified, the paper's main claim of "outperforming prior methods" is unverifiable. Together with the missing results for mentioned datasets, these issues require a significant revision.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>