- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6
Now I have a thorough understanding of the paper. Let me produce the final consolidated review after carefully verifying each claim against the paper.

## Summary

This paper investigates how continued pre-training on domain-specific raw corpora (DAPT) affects large language models. It finds that DAPT improves domain knowledge (benefiting fine-tuning and knowledge probing) but degrades prompting ability. To address this, the authors propose converting raw corpora into "reading comprehension texts" — each raw text followed by self-mined question-answering-style tasks (summarization, NLI, paraphrase detection, etc.) — and mixing them with general instructions. Experiments across biomedicine, finance, and law show the method consistently recovers and improves prompting performance while retaining domain knowledge, achieving results competitive with much larger domain-specific models.

## Strengths

1. **Clear empirical identification of a nontrivial phenomenon**: Section 2 and Table 1 demonstrate that vanilla DAPT on raw corpora consistently improves fine-tuning and knowledge probing across three domains but *lowers* prompting scores (e.g., biomedicine prompting drops substantially while fine-tuning rises). This finding — that DAPT hurts prompting for LLMs even though it helps for BERT-era models — is non-obvious and motivates the paper well.

2. **The proposed method (reading comprehension texts) consistently recovers and improves prompting across all three domains**: Table 4 shows AdaptLLM-7B outperforms both the general LLaMA-7B and the DAPT model on every domain-specific prompting benchmark. For example, in finance, AdaptLLM-7B (47.6) improves over LLaMA (42.5) and DAPT (39.7), approaching BloombergGPT-50B (48.3). The pattern holds in biomedicine and law.

3. **Evidence that domain knowledge is retained after switching to reading comprehension texts**: Figure 2 (left panel) shows that fine-tuning performance on domain tasks after training on reading comprehension texts is higher than after training on raw corpora in all three domains. This confirms the method does not sacrifice domain knowledge while fixing the prompting deficit — a nontrivial result.

4. **Reading comprehension texts improve general-domain prompting as well**: Figure 2 (right panel) reports that training on domain-specific reading comprehension texts (without general instructions) boosts zero-shot performance on general task types (reading comprehension, closed-book QA, FLAN-style clusters) compared to both the general LLaMA and raw-text training. This directly supports the paper's claim of potential for broader applicability.

5. **Well-structured ablation study isolating each component's contribution**: Table 5 shows that reading comprehension texts alone already outperform raw texts and raw+general instructions. Adding general instructions further improves results. This clean decomposition makes the attribution clear.

6. **Reproducible method description**: Tables 2 and 3 provide complete regex-based mining patterns, input-output templates, and verbalizers for all six task types. The method is fully automatic, self-supervised, and applicable to any domain corpus without manual annotation.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported by the evidence presented. All issues below are bounded and addressable.

### Minor

1. **The mechanism behind DAPT-induced prompting degradation is hypothesized but not verified.** The paper attributes the drop to "limited diversity of input-output patterns" (Section 2) but does not test this hypothesis with probing experiments (e.g., tracking perplexity on held-out instructions during DAPT, measuring representation shifts). While this does not weaken the paper's core contribution (the method works regardless of mechanism), it leaves the motivation for *why* the reading comprehension format works somewhat speculative. The paper would be stronger with a few targeted probes.

2. **The DAPT analysis is demonstrated on a single base model (LLaMA-7B).** While the AdaptLLM method is later shown on LLaMA-13B and GPT-J-6B, the core observation that raw DAPT hurts prompting is only established for LLaMA-7B. The paper frames this as a general finding about "domain-adaptive pre-training for large language models" (Section 2 and contribution list), which is broader than the evidence supports. This is a bounded limitation, not a fatal one — the finding is replicated across three domains, which provides some generality.

3. **Data mixing ratio tuning protocol is not described.** Section 4 states optimal ratios for mixing reading comprehension texts with general instructions (1:1, 1:2, 1:1) were found by "exploring different ratios," but the tuning procedure is not specified (validation sets used? metric optimized? search range?). This is a reproducibility gap.

4. **Hyperparameters for continued pre-training are absent.** The paper does not report learning rate, batch size, number of training steps, or optimizer settings for the domain-adaptive pre-training or the reading comprehension training. While code is promised at a GitHub repository, the paper should specify these in the main text or appendix for independent reproducibility.

5. **No variance or statistical significance information for main results.** All tables report single-score averages without standard deviations, confidence intervals, or significance tests. Given that some evaluation sets are small (e.g., USMLE has a few hundred examples), it is unclear whether observed differences between conditions are robust.

6. **"Drastically" overstates the prompting drop for law.** Table 1 shows the law domain has a small prompting drop (the paper's text says "drastically hurts its prompting ability"), making this characterization too strong for at least one of the three domains. The abstract and introduction should qualify the claim with the actual magnitudes.

### Trivial
- The claim "competitive performance with domain-specific models of much larger scales, such as BloombergGPT-50B" could note that BloombergGPT additionally maintains general-domain performance (as reported in its original paper), providing fuller context for the trade-off. However, the paper's framing as "efficiency" is appropriate and not misleading.

## Nice-to-Haves
- **Per-task breakdowns** alongside the averages in Table 1 and Figure 2 would help readers assess whether the reported trends are consistent across individual tasks or driven by outliers.
- **Ablation of individual reading comprehension task types** (e.g., removing summarization, NLI, etc. one at a time) would reveal which tasks are most responsible for the prompting improvement and provide practical guidance for applying the method to new domains.
- **Coverage statistics** for the mining patterns (fraction of raw texts yielding at least one mined task, average number of mined examples per document) would help readers assess scalability and potential failure modes in new domains.
- **General-domain task performance after DAPT** (e.g., MMLU, HellaSwag) would directly confirm whether the prompting degradation is specific to domain prompts or a broader phenomenon. However, this is beyond the paper's stated scope.

## Removed Points

These points were flagged by the reviewers but are removed after cross-checking against the paper:

- **BloombergGPT comparison inflates results** (Harsh Critic #3): Removed. The paper says "competitive performance" and "approaches" — it does not claim superiority. The critic's claim that "general capability after domain adaptation is not systematically evaluated" is contradicted by Figure 2 (right panel), which evaluates general task performance after reading comprehension adaptation. The comparison is honestly framed as an efficiency advantage (7B vs. 50B).
- **MedAlpaca comparison is weak** (Harsh Critic): Removed. MedAlpaca is presented as an auxiliary reference for instruction fine-tuning, not as a direct baseline for the continued-pretraining method. The paper's primary baselines are LLaMA and DAPT, which are appropriate.
- **Conclusion claim about "general model" not tested** (Harsh Critic): Removed. The paper says "suggesting potential" and "we hope" — these are explicitly forward-looking/aspirational statements, not claims of having built a general model.
- **General-domain tasks after DAPT not reported** (Harsh Critic): Removed. This is scope creep — the paper's focus is domain-specific prompting, and the relevant comparison (general tasks after reading comprehension adaptation) is provided in Figure 2.
- **Domain-specific tuning of mining patterns** (Harsh Critic): This is a reasonable question but the patterns in Table 2 are mostly domain-agnostic (regex for words like "Therefore", "However"). The Word-to-Text task uses domain vocabulary but that's by design. Moving to Nice-to-Have as a curiosity rather than a weakness.
- **Strength Finder claim about "50× larger"**: Removed/corrected. BloombergGPT-50B is ~7× larger than AdaptLLM-7B, not 50×.

## Novel Insights

None beyond the paper's own contributions. The two reviewers' observations are primarily evaluative rather than generative of new insights.

## Suggestions

1. Add a brief probing experiment (e.g., tracking perplexity on held-out instructions during DAPT) to directly test the hypothesized mechanism for prompting degradation.
2. Report hyperparameters (learning rate, batch size, steps) for continued pre-training and specify the ratio-tuning protocol.
3. Include per-task scores alongside averages in a table or appendix to allow readers to assess consistency.
4. Soften "drastically" in the abstract to something like "can substantially reduce" given the law domain's small drop, or report the domain-specific magnitudes.
