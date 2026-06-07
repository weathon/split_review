## Summary

The paper proposes IDS-Agent, an LLM-powered agent for intrusion detection in IoT networks. The system uses a ReAct-style pipeline where a core LLM iteratively reasons and acts using tools for data extraction, preprocessing, ML classification (six classifiers), knowledge retrieval (RAG over a curated document base + search engines), and aggregation. The agent includes short-term and long-term memory modules and supports prompt-based sensitivity adjustment. Experiments on ACI-IoT'23 and CIC-IoT'23 report detection F1 of 0.97 and 0.75, zero-day attack recall of 0.61, and clean ablation results demonstrating the contribution of each module.

## Strengths

- **Outperforms multiple SOTA baselines on two benchmark datasets (Sec. 4.4, Table 1)**: IDS-Agent with GPT-4o achieves detection F1 of 0.97 on ACI-IoT'23 and 0.75 on CIC-IoT'23, outperforming the GPT-4 in-context learning baseline (Zhang et al., 2024), a quantum-annealing ML-based IDS (Davis et al., 2024), a majority-vote ensemble of six ML classifiers, and each individual classifier.

- **Zero-day attack recall exceeds specialized anomaly detection methods (Sec. 4.5, Table 2)**: IDS-Agent achieves 0.61 recall on nine unseen attack types from CIC-IoT'23, compared with ACGAN (0.45) and RealNVP (0.37) — methods specifically designed for zero-day/OOD detection.

- **Ablation study cleanly quantifies individual component contributions (Sec. 4.6, Tables 3–4)**: Removing the Knowledge Retrieval module drops zero-day recall from 0.61 to 0.42 (31% relative decrease); removing Long-Term Memory drops overall accuracy from 0.733 to 0.702. The ablations are well-designed and directly support the claimed utility of each module.

- **Concrete case study of LLM reasoning resolving classifier disagreement (Sec. 4.4, Figs. 1–2)**: The paper provides a specific example where 3/6 ML models predict "benign" but IDS-Agent correctly detects a reconnaissance attack by recognizing that "Host Discovery" and "OS Scanning" are both reconnaissance subcategories — a capability no individual classifier or majority vote can provide.

- **Prompt-based detection sensitivity tuning works as expected (Sec. 4.6, Table 5)**: Three sensitivity levels (aggressive/balanced/conservative) produce the intended trade-off (attack recall 0.97→0.85, benign recall 0.90→0.98) without expert reconfiguration.

## Weaknesses

### Fatal
None.

### Major

- **Zero-day evaluation is potentially compromised by knowledge base content (Sec. 4.2, 4.5)**: The Knowledge Retrieval module's database is built from "50 online blogs and 50 research papers" about IoT attacks (Sec. 4.2). Nine attack types are held out from classifier training for zero-day evaluation. If these documents describe the held-out attack types — which is highly probable for well-known CIC-IoT'23 categories — then the system gains indirect access to information about "unknown" attacks during the aggregation step. The ablation result (zero-day recall dropping from 0.61 to 0.42 when knowledge retrieval is removed) is entirely consistent with this alternative interpretation: the knowledge module provides textual descriptions of the attacks themselves, not just general context. The paper does not verify whether the knowledge base contains information about the held-out attacks, nor does it discuss this confound. This does not invalidate the known-attack results, but it substantially weakens the zero-day generalization claim.

- **No variance or statistical significance reported despite small test sets and LLM stochasticity (Sec. 4.1, 4.4–4.6)**: Test sets have only 10–20 samples per class for known attacks (50 for zero-day). A single misclassification shifts per-class metrics by 5–10 percentage points. No confidence intervals, standard deviations, or multiple runs are reported anywhere. Given that the system uses stochastic LLM API calls (GPT-4o, GPT-4o-mini, GPT-3.5-turbo) with unspecified temperature, the reported point estimates (F1=0.97, 0.75) cannot be assumed stable. This is a basic evidential requirement for papers involving LLM-based pipelines — LLM output variance alone could shift reported numbers by meaningful margins on test sets of this size.

### Minor

- **Explanation quality is claimed as a contribution but never evaluated (Sec. 1, Sec. 4)**: The paper prominently claims explainability as a key advantage over ML-based IDSs (abstract, introduction, contributions). Yet no evaluation of explanation accuracy, faithfulness, or usefulness is provided. The case studies show two cherry-picked successful examples, with no failure cases or systematic assessment. An LLM can generate plausible-sounding but incorrect justifications; this should at minimum be acknowledged as a limitation or evaluated.

- **No cost or latency analysis despite practical deployment implications**: Each IDS-Agent inference runs six ML classifiers, makes multiple LLM API calls, queries a vector database, and potentially calls search engines. For a practical IDS, per-sample cost and latency are critical deployment constraints (especially in IoT settings). These are not quantified or discussed.

- **Search engine API usage is ambiguous (Sec. 3.3 vs. Sec. 4.2)**: The method section describes knowledge retrieval via Google and Wikipedia APIs (Sec. 3.3), but the implementation (Sec. 4.2) describes only a pre-curated vector database of 100 documents. It is unclear whether live search was actually used in experiments. If it was not, claims about "up-to-date knowledge" (Sec. 2) are overstated.

- **Davis et al. (2024) quantum-annealing baseline is only evaluated on ACI-IoT'23, not CIC-IoT'23 (Table 1)**: The paper does not explain why this SOTA baseline is missing from the harder dataset, leaving an incomplete comparison.

- **No limitation section or failure mode discussion**: The paper identifies no limitations of the approach despite reliance on proprietary LLMs (API deprecation risk, cost, dependence on OpenAI), potential for hallucinated explanations, prompt sensitivity, and the high latency of iterative tool-calling.

### Trivial
None.

## Nice-to-Haves

- The paper uses only 10% of training data for both baselines and IDS-Agent. A brief justification or sensitivity analysis on training data size would strengthen the evaluation, though it affects all methods equally.
- The case studies could be complemented by a few failure case analyses to give a more balanced picture of the system's behavior.

## Removed Points

These points were flagged by reviewers but removed after verification against the paper; they are recorded here for completeness but should not be considered valid weaknesses:

- **"Comparison baseline setup makes headline results substantially less informative"** — The paper compares against individual ML classifiers and majority voting (subcomponents of IDS-Agent), but it also includes two external baselines: the Zhang et al. (2024) GPT-4 in-context learning method and the Davis et al. (2024) quantum-annealing method. Comparing a full system against its subcomponents is standard practice in system-building papers, and the external baselines provide an independent anchor. This criticism overstates the issue.

- **"10% training data may disadvantage ML baselines relative to IDS-Agent"** — The same 10% training data is used for all methods, including IDS-Agent's own classifiers. If anything, limited training data hurts both sides equally. This is speculative and unsupported by any reasoning about why the effect would be asymmetric.

- **"Case studies are cherry-picked"** — Case studies are illustrative by design in virtually every ML/system paper. The paper does not make statistical claims based on them.

- **"Method section is over-described relative to its novelty"** — Subjective stylistic judgment. The level of detail in Sec. 3 is appropriate for reproducibility.

- **"Detection sensitivity result is not surprising"** — Subjective assessment of result novelty, not a weakness.

- **"Related work treats difference as engineering scale"** — Subjective framing critique without a concrete anchor in the text.

## Novel Insights

The most interesting finding not fully developed by the paper is the quantitative measurement of how external knowledge (retrieved documents) contributes to zero-day detection — the ablation shows a 0.19 recall gap when knowledge retrieval is removed. If this gap is genuine (not confounded by the contamination issue), it provides concrete evidence that RAG-augmented LLM agents can flag OOD traffic patterns more effectively than purely statistical anomaly detectors. This is potentially the paper's most novel empirical contribution and deserves tighter experimental controls. Conversely, if the gap is driven by knowledge base contamination, it illustrates a subtle pitfall in evaluating "zero-day" capabilities for knowledge-augmented systems that deserves broader discussion in the community.

## Suggestions

1. **Verify and report the content of the knowledge base** with respect to the nine held-out attack types. If any document describes these attacks, either filter the knowledge base or reframe the zero-day evaluation as "detection of attacks unseen by the ML classifiers (but potentially described in external documents)" and discuss the distinction transparently.
2. **Run the full evaluation pipeline at least 5 times** with different seeds and report means ± standard deviations. Use a fixed temperature for reproducibility (e.g., t=0) or vary temperature and report stability.
3. **Add an explanation quality evaluation**: at minimum, have annotators rate whether generated explanations are factually consistent with the classifiers' actual outputs (faithfulness).
4. **Report per-sample cost in USD and latency in seconds** for the full pipeline.
5. **Explicitly state whether search engine APIs were used in the experiments**. If not, remove or qualify method claims about "up-to-date knowledge."
6. **Add a limitations section** discussing reliance on proprietary LLMs, potential hallucination, prompt sensitivity, and latency/cost constraints.

## Score and Decision

The paper presents a well-engineered system with clean ablations and strong performance on two datasets. However, at ICLR's bar, the evaluation has significant gaps: the zero-day claim — the most novel aspect — is potentially undermined by knowledge base contamination that is not discussed or controlled for, and no variance is reported despite small test sets and stochastic LLM outputs. The technical contribution is primarily in system integration of existing techniques (ReAct, RAG, memory-augmented LLMs) applied to IDS, rather than new methodology. These issues place the paper below the acceptance threshold for a top-tier venue.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>