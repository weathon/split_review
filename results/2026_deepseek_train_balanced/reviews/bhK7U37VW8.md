## Summary

This paper proposes AutoDAN-Turbo, a black-box jailbreak framework that uses a "lifelong learning agent" to autonomously discover, store, retrieve, and evolve jailbreak strategies from scratch (starting from an empty library) without human intervention. The system has three modules — attack generation/exploration, strategy library construction, and strategy retrieval — that iteratively generate attack prompts, extract generalizable strategies by comparing successful vs. unsuccessful attack logs, and retrieve relevant strategies for new attacks. The paper reports large gains over existing jailbreak methods, claiming an 88.5 ASR on GPT-4-1106-turbo.

## Strengths

- **Autonomous strategy discovery from scratch.** The paper demonstrates that AutoDAN-Turbo can start with an empty strategy library and, through interaction with a small warm-up set (50 requests), discover reusable jailbreak strategies without any human-provided strategy templates or predefined strategy categories. This goes beyond prior strategy-based methods (Rainbow Teaming's 8 predefined strategies, PAP's 40 persuasion schemes) that rely on human-designed starting points.

- **Strong transferability evidence across models and datasets.** Section 3.3 provides clean evidence that a strategy library learned on one model (Llama-2-7B-chat, 21 strategies) transfers to 7 different attacker models and 7 different target models (Table 3), and that Harmbench-trained strategies transfer to unseen datasets with <4% ASR degradation (Figure 3). These transferability experiments are cleaner than the main results and directly support the claim that the library captures generalizable patterns, not test-set-memorized artifacts.

- **Large and consistent performance margin in main comparisons (to be interpreted with the caveat in Weaknesses).** Across all 8 victim models in Table 1, AutoDAN-Turbo outperforms every baseline individually. The runner-up (Rainbow Teaming) is surpassed on every model, and the margins are substantial throughout.

- **Plug-and-play integration of external strategies works.** Table 4 shows that injecting 7 human-designed strategies boosts ASR (e.g., from 88.5→93.4 on GPT-4-1106-turbo with Llama-3-70B), demonstrating the framework can unify automated and human-designed strategies.

## Weaknesses

### Major

**1. Evaluation protocol asymmetry: the method learns from the test set (Harmbench) during lifelong learning, then is evaluated on that same set; baselines have no equivalent mechanism (structural unfairness).**

The implementation (lines 120–121) proceeds as: (a) warm-up on 50 separate requests → initial library; (b) lifelong learning on **all 400 Harmbench requests** for 5 rounds, extracting strategies from attack logs and storing them in the library; (c) evaluation on the **same Harmbench dataset** with the fixed library. This means strategies derived from attacking specific Harmbench prompts are available when attacking those same prompts during evaluation, while baselines (Rainbow Teaming with 8 fixed strategies, PAP with 40 fixed persuasion schemes, GCG-T, PAIR, TAP) have no equivalent cross-instance learning mechanism. Running "the same total iterations" for baselines (as the paper claims) does not address this asymmetry because those iterations do not build a reusable strategy library.

The headline claims — 74.3% higher ASR than the runner-up, 88.5 ASR on GPT-4 — rest on this comparison. While the strategies are general textual patterns (not memorized prompts), and the transferability experiments (Section 3.3) provide cleaner supporting evidence, the main results in Tables 1 and 2 fundamentally conflate training and evaluation in a way that the baselines cannot match. A valid comparison would either (a) hold out a subset of Harmbench that the method never sees during any learning phase, or (b) build the library solely from the warm-up set and a separate training set, then evaluate on Harmbench with the fixed library.

**2. No ablation studies isolating any of the three interacting modules.**

The system has three modules (attack generation, strategy library construction, retrieval) with several design choices: the retrieval mechanism (embedding-based similarity search + score-difference ranking), the strategy extraction procedure (pairwise comparison via summarizer LLM), the thresholding rules (S_T=8.5, score difference 2–5), and the warm-up vs. lifelong learning stages. Not a single ablation isolates any of these. Without ablations, it is impossible to attribute the reported performance to specific design choices — it could be driven primarily by the retrieval mechanism, the summarizer quality, the raw query budget, or the scorer LLM calibration. This is a significant evidential gap for a paper presenting a complex multi-module system.

**3. The strategy extraction procedure is unvalidated — no examples, no human evaluation, no verification that extracted strategies are causal rather than correlational.**

Strategies are defined operationally (line 71: "text information that, when added, leads to a higher jailbreak score") and extracted by asking a summarizer LLM to describe the difference between two attack records where one scored higher than the other (Section 3.2). The paper reports only TSF (Total Strategies Found) without showing a single example of a discovered strategy, its name, or its definition. There is no human evaluation of whether the extracted strategies are coherent, reproducible, novel, or genuinely causal. For a paper whose central contribution is *automatic strategy discovery*, this is a serious omission — we cannot evaluate what was actually discovered.

### Minor

**4. No variance or statistical significance reported.** All results (Tables 1–5, Figures) are single numbers with no standard deviations, confidence intervals, or runs with different random seeds. Given the stochasticity of LLM sampling, the random pair selection for strategy extraction, and the embedding-based retrieval, results could vary substantially across runs. The large reported gaps relative to baselines should invite scrutiny rather than precluding the need for error bars.

**5. Total query cost is not reported; the "query-efficient" claim is misleading.** Table 5 reports only test-stage queries (avg 6.72 per successful jailbreak) and claims an 87% reduction vs. PAIR/TAP. However, the total cost of building the strategy library — warm-up (50 requests × 150 iterations = 7,500) plus lifelong learning (400 requests × 5 rounds × up to 150 iterations ≈ 300,000) — is not reported or discussed. The method is query-efficient only at test time because it amortizes a massive training cost across the library. The paper should report and acknowledge the total cost.

**6. The embedding model for retrieval keys is not identified by name.** Line 85 cites generic "text embedding model" references without naming the specific model used. This affects reproducibility and evaluation of retrieval quality.

### Trivial

- Several hyperparameter values (S_T=8.5, score-difference threshold 2–5) are stated without sensitivity analysis. Not a core flaw, but a missed opportunity.

## Nice-to-Haves

- Show qualitative examples of discovered strategies with human evaluation of their novelty and quality.
- Report the total query budget (warm-up + lifelong learning + test) alongside test-stage queries to contextualize the efficiency claims.
- Run the evaluation with a held-out partition of Harmbench that the method's library was never trained on.
- Add an ablation that replaces embedding-based retrieval with random retrieval to isolate the retrieval module's contribution.

## Removed Points

- **"Prompt templates not included in parsed text"** — This is a parser artifact; the original submission likely contains these in an appendix.
- **"Characterization of existing methods as lacking jailbreak knowledge is slightly overdrawn"** — This is a matter of framing, not a substantive weakness.
- **"The paper should not be accepted in its current form" from the harsh critic** — This is a conclusion, not a weakness; the substance has been incorporated into the Major weaknesses above with appropriate nuance.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the evaluation asymmetry clearly but do not contribute additional analytical insight beyond what a careful reader would notice.

## Suggestions

1. **Fix the evaluation protocol**: Construct the strategy library using only the 50-request warm-up set plus a separate held-out training set of malicious requests, then freeze the library and evaluate on the standard Harmbench benchmark. This would directly assess whether cross-prompt strategy transfer works without data leakage.
2. **Add ablation studies**: At minimum, ablate (a) the retrieval mechanism (random vs. embedding-based), (b) the lifelong learning stage (warm-up only vs. warm-up + lifelong), and (c) the strategy extraction (direct use of attack logs vs. structured strategies).
3. **Provide qualitative analysis**: Show 5–10 example strategies with their names, definitions, and example applications. Include a human evaluation of strategy quality and a sanity check (do the extracted strategies demonstrably improve attack success on unseen prompts?).
4. **Report variance**: Run the main experiment at least 3 times with different random seeds and report mean ± std for ASR and StrongREJECT scores.
5. **Report total query cost**: Provide the total number of LLM queries across all phases (warm-up, lifelong learning, test) so readers can judge the efficiency claim in context.

## Score and Decision

The paper presents an interesting and ambitious idea — autonomous jailbreak strategy discovery via a lifelong learning agent — and the transferability experiments provide genuine evidence that the method captures generalizable patterns. However, the headline results (Tables 1 and 2) suffer from a structural evaluation asymmetry: the method learns from the test set during lifelong learning while baselines do not have an equivalent mechanism. Combined with the complete absence of ablation studies, unvalidated strategy extraction, and lack of variance reporting, the evidence is insufficient to support the paper's strongest claims at a top-venue standard. The core idea has merit, but a valid evaluation protocol and ablations are prerequisites.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>