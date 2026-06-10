## Summary

This paper proposes InsTag, an automatic fine-grained instruction tagging method that uses ChatGPT to annotate SFT queries with intention tags, followed by a systematic normalization pipeline (frequency filtering, rule aggregation, semantic aggregation via DBSCAN, and association aggregation via FP-Growth) that reduces over 100K raw unique tags to 6,587 clean tags. Using these tags, the paper operationalizes instruction diversity (unique tag coverage rate) and complexity (average tags per query) as quantifiable metrics, analyzes popular open-source SFT datasets, and proposes a complexity-first diverse sampling method that selects 6K samples from a 306K pooled dataset. LLaMA-13B models fine-tuned on this selected data achieve 6.44 on MT-Bench, surpassing several open-source models trained on substantially more data.

## Strengths

- **Novel operationalization of diversity and complexity via fine-grained tags.** Prior work on SFT data collection discussed diversity and complexity only qualitatively. This paper provides concrete, quantifiable definitions: diversity as unique tag coverage rate and complexity as average tag number per query (Section 2.4, lines 244–247). The scatter plot in Figure 2a shows that datasets known to produce strong models (ShareGPT, UltraChat, OpenChat-v1) occupy the upper-right (high diversity, high complexity) region — a direct, testable validation of the proposed metrics that goes beyond hand-waving.

- **Well-designed, systematic four-stage tag normalization pipeline with quality validation.** The paper identifies three concrete noise types in open-set LLM annotations (lexical noise, uncontrolled granularity, spurious correlations) and designs corresponding normalization stages. Quality is validated via GPT-4 on 4,000 cases (96.1% precision, 86.6% consistency) and human annotators on 40 cases, with Fleiss-κ reported and counterfactual probes included (Table 1, lines 178–217). This evaluation rigor is a meaningful step beyond prior work that assumes ChatGPT annotations are adequate without verification.

- **Controlled decoupled analysis separates the effects of diversity and complexity.** Rather than reporting only the combined final result, the paper conducts controlled experiments: varying average tag number from 6.7 to 16.6 while holding tag coverage at 100% (complexity), and varying tag coverage from ~45% to 100% while holding average tag number at 5.0 (diversity). Both dimensions show positive correlation with MT-Bench performance (Figures 3a, 3b). This within-pipeline controlled experimentation provides genuine evidence for the paper's thesis.

- **Impressive data efficiency.** The LLaMA-2-based model (v2.0) trained on only 6K samples achieves 6.55 on MT-Bench, approaching Llama-2-13b-chat (6.65) which additionally uses RLHF. Even the LLaMA-1-based model (v1.0) at 6.44 exceeds several models trained on 70K–125K samples. While the comparison has caveats (discussed below), the data efficiency is noteworthy and consistent across the paper's controlled experiments.

## Weaknesses

### Major

- **The headline comparison against third-party models is not controlled, leading to an overclaimed causal inference.** The paper's most prominent result (Table 2) compares *lmname*-13b-v1.0 (6K, 6.44) against models trained by other groups — Vicuna-13b-v1.3 (125K, 6.39), WizardLM-13b (70K, 6.35), etc. — and presents this as evidence that "diversity and complexity do matter" and that InsTag-based selection drives the improvement. However, these baselines differ in training hyperparameters (learning rate, batch size, epochs, optimizer), base model checkpoints, prompt templates, response formats, and training code — not just in data selection. A model trained on 6K carefully selected samples with one training recipe can outperform a model trained on 125K with a different recipe for reasons entirely unrelated to data selection. The controlled experiments in the decoupled analysis (Section 3.3) do provide genuine evidence for the diversity/complexity thesis, but the paper positions the uncontrolled comparison as a headline result and the language ("echoing the importance of query diversity and complexity," line 10; "surpassing a group of LLMs aligned with considerably more SFT data," line 44) implies a causal interpretation that the comparison cannot support. The paper would be substantially strengthened by a within-pipeline comparison where only the data selection method varies (e.g., random 6K, InsTag-selected 6K, baseline-selected 6K from simpler methods).

### Minor

- **Source dataset composition of the selected 6K is not reported, leaving a response-quality confound unexamined.** The four pooled datasets (WizardLM(Alpaca), WizardLM(ShareGPT), UltraChat, ShareGPT) differ substantially in response quality — ShareGPT and UltraChat contain GPT-4 responses, while WizardLM variants use ChatGPT/self-instruct responses. The average tag number of the selected 6K (16.56) is 3.7× the pool average (4.48), indicating massive selection skew. If InsTag disproportionately selects samples from ShareGPT and UltraChat, the observed performance gain could partly reflect response quality rather than query diversity/complexity. Reporting the source-dataset breakdown of the selected subset would allow readers to assess this confound.

- **Margins over the closest baselines are small and statistical significance is unaddressed.** *lmname*-13b-v1.0 (6.44±0.04) exceeds Vicuna-13b-v1.3 (6.39) by 0.05 points and WizardLM-13b (6.35) by 0.09 points. MT-Bench with GPT-4 as judge is known to have non-trivial variance; the paper reports standard deviations from three judgments for its own models but provides single-point baseline numbers from the leaderboard. A significance test (even a paired bootstrap) would help calibrate confidence in these small margins. (The v2.0 result at 6.55 against Llama-2-13b-chat at 6.65 is a larger gap in the opposite direction.)

- **Human annotation sample for tagging quality is too small for the reported 100% correctness to be informative.** The human evaluation is based on only 40 cases (1% of 4,000). A single error would change 100% to 97.5%. The Fleiss-κ of 0.47 (precision) between human annotators indicates only "basic agreement," which is somewhat at odds with the 100% correctness claim. The primary validation rests on the 4,000 GPT-4 evaluations (96.1%/86.6%), which is more substantial, but the human-layer validation should be presented with more measured confidence given the sample size.

- **No sensitivity analysis for normalization hyperparameters.** The tag normalization pipeline uses several critical hyperparameters (α=20 frequency cutoff, DBSCAN threshold=0.05, minimum support=40, minimum confidence=99%) without any analysis of how varying these affects the resulting tag set or downstream performance. The DBSCAN threshold of 0.05 in particular — described as "minimum semantic similarity" — is tight enough that the reader cannot assess whether the semantic aggregation step is meaningfully merging related tags or just consolidating near-duplicates. A sensitivity analysis showing the impact on tag set size and downstream MT-Bench scores would strengthen confidence in the pipeline's robustness.

### Trivial

- "datsets" typo on line 92.

## Nice-to-Haves

- Comparing the complexity-first diverse sampling algorithm against simpler alternatives within the same training pipeline — e.g., greedy complexity-only (top 6K by tag count), diversity-only (maximizing coverage without complexity preference), and embedding-based diversity (Sentence-BERT without the tagging pipeline) — would directly test whether InsTag's tag-based metrics add value over cheaper proxies.
- The paper could discuss potential MT-Bench data contamination, since the pooled dataset includes ShareGPT (real user conversations with GPT-4) and UltraChat (GPT-4-generated), which may overlap with MT-Bench queries.
- The diversity metric (unique tag coverage) is sensitive to the total tag set size; a brief discussion of this sensitivity would be helpful.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **"Decoupled analysis lacks necessary controlled comparisons"** (Harsh Critic issue 2): The paper *does* run controlled experiments in Section 3.3 that vary diversity while holding complexity constant and vice versa. The critic's request for ablations comparing complexity-first sampling against greedy complexity-only or embedding-based selection addresses a different question (does the *specific* algorithm matter vs. do the *metrics* matter). The decoupled analysis as designed is a valid test of the core thesis. Demoted to Nice-to-Have.

- **"No discussion of multi-turn conversation handling"**: The paper explicitly states "we separately annotate each query in a chat session" (line 105) and defines session-level metrics as average tags per session (line 383). Handling is minimally documented but not absent.

- **"DBSCAN threshold of 0.05 is remarkably tight"**: The paper reports that semantic aggregation reduces tags from 7,157 to 6,587 — about 570 merges — so the step does do measurable work. The critic's speculation that the step "may not do much work" is unsupported by the paper's own numbers. The threshold choice would benefit from sensitivity analysis (listed as a Minor weakness), but the claim that the step is ineffective is not justified.

- **"Data contamination not discussed"**: Speculative and standard for the era; moved to Nice-to-Have.

- **Strength Finder strength 3 ("SOTA for model scale")**: This strength overstates the evidence given the uncontrolled comparison. Merged into the data-efficiency observation in Strengths but rephrased more cautiously.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Run a controlled within-pipeline experiment: train LLaMA-13B on (a) random 6K from the pooled dataset, (b) InsTag-selected 6K, (c) 6K selected by a simpler embedding-based diversity baseline, and (d) 6K selected by greedy top-tag-count complexity-only. This would directly test whether InsTag's tag-based pipeline adds value over cheaper alternatives and would address the core weakness about uncontrolled comparisons.

2. Report the source-dataset breakdown (ShareGPT vs. UltraChat vs. WizardLM variants) of the selected 6K subset and of each decoupled-analysis subset.

3. Add a sensitivity analysis for the normalization hyperparameters — particularly the DBSCAN threshold and the frequency cutoff α — showing their impact on tag set size and on downstream MT-Bench scores for at least one condition.

4. Include confidence intervals or a bootstrap significance test for the main MT-Bench comparisons.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>