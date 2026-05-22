Now I have all the information I need. Let me synthesize the final review and determine the score.

Here's my round-1 bracket and round-2 analysis:

**Round-1 bracket**: 4.0 - 6.5

The paper sits between the weak anchors (3.0-3.25, papers on unrelated topics that were rejected) and the strong anchors (7.75-9.0, exceptionally well-executed papers). The most relevant anchors are the contamination-themed ones:

- Nk1MegaPuG (4.25, Reject) - "Evading Data Contamination Detection" - similar theme but less clean execution
- rAylWUIKtu (4.25, Reject) - "Benchmark Inflation" - contamination, rejected
- BCyAlMoyx5 (5.67, Reject) - "Crosslingual Capabilities" - multilingual eval, rejected
- m2NVG4Htxs (6.75, Accept) - "Longitudinal Contamination" - stronger experimental design
- Nsms7NeU2x (6.75, Reject) - "Forgetting Contamination" - stronger empirical work

**Narrowing**: The paper has a genuine contribution but a fundamental experimental gap: it claims translation conceals contamination but never tests detection methods on English vs Arabic-contaminated models. This is more severe than the issues that got BCyAlMoyx5 (5.67) rejected. The paper is better executed than Nk1MegaPuG (4.25) though. So the score should be between these: 4.5.

**Final score: 4.5 - Reject**

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial
## Nice-to-Haves
## Removed Points
## Novel Insights
## Suggestions
## Score and Decision

Let me write the full review now.## Summary

This paper investigates whether translating benchmarks into Arabic can mask data contamination in LLM evaluation. The authors fine-tune four open-weight LLMs on Arabic-translated test sets (MMLU, XQuAD, MLQA) at varying proportions, evaluate on the original English benchmarks, and probe memorization via TS-Guessing with a choice-reordering extension. The central claim is that translation "conceals traditional contamination signals" while still allowing models to benefit from exposed data, creating a blind spot in current evaluation practices.

## Strengths

- **Multi-model, multi-dataset, multi-level experimental design**: The paper fine-tunes four models (LLaMA-3.2-1B, Mistral-7B, Gemma-3-1B, Qwen3-1.7B) on three datasets at four contamination levels (0%, 10%, 50%, 100%). This goes beyond prior contamination studies that typically examine a single model or language pair, providing a broader empirical basis for understanding multilingual contamination dynamics.

- **TS-Guessing with choice-reordering is a genuine methodological extension**: The paper extends TS-Guessing (Deng et al., 2024) by adding a choice-reordering step before masking options (Section 3.3, Figure 1). This measures index-recall rate (IDR)—whether a model reproduces the pre-shuffle answer letter after random reordering. Table 3a reports IDR values up to 0.643 (LLaMA-3.2-1B at 50% contamination on MMLU), providing concrete evidence of memorization that goes beyond surface-form overlap. This adaptation is a meaningful improvement over prior TS-Guessing applications that did not control for answer position.

- **Empirical demonstration that Arabic-translated contamination inflates English benchmark scores**: The core experimental results (Table 2) show that MMLU accuracy rises monotonically with Arabic contamination across all models (e.g., Mistral: 0.577→0.690, LLaMA: 0.332→0.431, Gemma: 0.220→0.284). This finding itself is useful—it demonstrates that semantic content from translated benchmarks can leak through to improve English performance, which is a non-trivial observation about cross-lingual contamination.

- **Raises an important and underexplored question**: The paper identifies a legitimate blind spot—contamination detection methods focus overwhelmingly on English, and the possibility that translation could mask contamination is a real concern that deserves community attention.

## Weaknesses

### Major

- **The central claim that translation "conceals traditional contamination signals" is untested.** The paper claims that standard detection methods fail to catch contamination when it passes through translation. However, the experiments never actually apply any existing detection method (e.g., Min-K% Prob, guided prompting, TS-Guessing in its original English form) to the contaminated models and compare detection success rates between English-contaminated and Arabic-contaminated models. What the paper demonstrates is that contamination *through translation works* (it inflates scores), not that detection methods *fail* on translation-mediated contamination. To support the concealment claim, the authors would need to (a) contaminate models with the original English test sets at the same proportions, (b) apply standard detection methods to both English-contaminated and Arabic-contaminated models, and (c) show that detection succeeds on English-contaminated models but fails on Arabic-contaminated ones. Without this comparison, the paper's central finding is an observation about contamination *efficacy*, not about detection difficulty.

- **No within-language contamination baseline.** The paper has no condition where models are contaminated with English-translated or original English test data to compare how performance and detection signals differ. Without a direct comparison between same-language and cross-language contamination, the paper cannot attribute the observed effects to translation *specifically*. The non-monotonic behavior on XQuAD/MLQA might occur with English contamination too. The absence of this baseline makes the attribution to translation unsubstantiated.

- **TACD framework is unimplemented and presented as a contribution.** Section 5 proposes a Translation-Aware Contamination Detection framework, but it is a high-level outline with no implementation, no experiments, and no validation. The abstract and conclusion treat it as part of the paper's contribution, which inflates the claimed scope. A proposal without any empirical support should be presented as a discussion point, not a contribution.

### Minor

- **Framing conflates deliberate fine-tuning with natural contamination.** The paper investigates deliberate fine-tuning on translated test sets (Section 3.1), which is a worst-case scenario that does not reflect how contamination typically arises in pretraining. The introduction and motivation (Section 1) discuss the problem of benchmarks inadvertently appearing in pretraining corpora, but the experiments study intentional test-set fine-tuning. These are different phenomena. The paper should either use models contaminated during pretraining or clearly reframe as a study of deliberate contamination through fine-tuning.

- **No variance estimates.** Results in Tables 2 and 3 are based on single fine-tuning runs per condition with no error bars or statistical significance tests. It is impossible to assess whether the non-monotonic XQuAD/MLQA trends (e.g., Mistral XQuAD: 0.455→0.272→0.114) are reliable patterns or noise.

- **The "near-flat" claim in Section 4.2 is ambiguous and partially contradictory.** The text states "across contamination levels p ∈ {10, 50, 100}%, the models exhibit approximately equal performance on all evaluated benchmarks." This directly contradicts the clear monotonic MMLU trends visible in Table 2 (e.g., Mistral 0.577→0.690). The prose appears to be referring to TS-Guessing results or some other aggregate, but the phrasing is unclear and misleading.

- **The embedding analysis (Section 4.3) is too brief to be meaningful.** The paper asserts that "Arabic→English translations remain close to their English originals in representation space, with high cosine similarity" but provides no figure, no quantitative results, and no details about which representations were used or how similarity was computed. An "embedding figure" is referenced but does not appear in the main text.

### Trivial

None.

## Nice-to-Haves

- Reporting results across multiple random seeds would strengthen confidence in the observed patterns.
- Evaluating the models' Arabic-language capabilities (e.g., Arabic MMLU or Arabic QA benchmarks) would help contextualize which models have "stronger Arabic capabilities" as claimed in the abstract.
- A comparison with other detection methods (Min-K% Prob, guided prompting) applied to the contaminated models would directly test the concealment hypothesis and is the most impactful addition the paper could make.

## Removed Points

The following points were raised by reviewers but are removed with justification:

- **"TS-Guessing results are inconsistent with the narrative"** (Harsh Critic Point 3): The critic claims near-zero TS-Guessing on XQuAD contradicts the paper's claims. In fact, this supports the paper's thesis—models benefit from contamination (Table 2 shows XQuAD gains for Gemma and LLaMA) while TS-Guessing detection remains near-zero, which is exactly the "concealment" pattern the paper describes. For MMLU, where contamination is clearest, TS-Guessing IDR values are meaningfully non-zero (up to 0.643). The results are consistent with the narrative.

- **"The experiments never actually test any detection method"**: The paper does use TS-Guessing (a detection method) on the contaminated models and reports results in Table 3. The missing comparison is English-contamination vs Arabic-contamination detection rates, not the total absence of detection.

- **"Choice-reordering extension is not clearly motivated / not novel"**: The paper clearly explains the motivation—shuffling choices before masking controls for position-based recall—and this is a valid methodological extension of Deng et al. (2024).

- **Questions about model/dataset availability or existence**: All cited models and datasets are publicly available. Per review guidelines, any criticism questioning the existence of cited resources is removed.

- **Missing appendix content / lack of hyperparameters**: The appendix is stripped by the PDF parser. The original submission contains hyperparameters and other details in the appendix, per the reproducibility statement.

- **Formatting nitpicks and typos**: Parser artifacts, not author errors.

- **Strength Finder items that are generic or conflict with verified weaknesses**: The claim about "embedding-space analysis confirming semantic persistence" is removed because the embedding analysis is too brief (a single sentence with no quantitative backing) to qualify as a confirmed strength.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Run the critical control experiment**: Contaminate models with original English test sets at the same proportions, apply standard detection methods (Min-K% Prob, guided prompting, original TS-Guessing) to both English-contaminated and Arabic-contaminated models, and compare detection success rates. This is the single highest-leverage experiment and directly tests the paper's central claim.

2. **Reframe the contribution accurately**: The paper's actual contribution—demonstrating that fine-tuning on Arabic-translated benchmarks boosts English evaluation scores—is still valuable. Frame it as a study of cross-lingual contamination *efficacy* rather than detection *evasion*, or add the experiments needed to support the stronger claim.

3. **Add an English contamination baseline** to Tables 2 and 3 so readers can directly compare whether the patterns (especially non-monotonic QA trends) are specific to translation or general to any contamination.

4. **Implement or demote TACD**: Either provide actual experiments evaluating the TACD components, or move it to a discussion/future work section and remove it from the abstract and conclusion claims.

5. **Report variance** across multiple fine-tuning runs to establish whether the non-monotonic QA patterns are reliable.

## Score and Decision

**Score calibration report:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| fSbPwHjdDG | 3.00 | 1 | Unrelated topic (latent language in LLMs), rejected |
| OdoS6cH8MP | 2.00 | 1 | Unrelated (textual data valuation), rejected |
| 4y3GDTFv70 | 3.25 | 1 | Unrelated (emergent abilities theory), rejected |
| MyotJECv0D | 2.50 | 1 | Unrelated (MT evaluation metrics), rejected |
| BCyAlMoyx5 | 5.67 | 1 | Crosslingual capabilities paper, rejected. Similar scope but better executed; current paper has more severe experimental gap |
| k3gCieTXeY | 7.25 | 1 | INCLUDE multilingual benchmark, accepted. Much stronger contribution |
| QiyQJqpcYe | 4.75 | 1 | Linguini benchmark, rejected. Similar score zone but tighter execution |
| m2NVG4Htxs | 6.75 | 1 | Longitudinal contamination study, accepted. Much cleaner experimental design using natural experiment |
| jOmk0uS1hl | 8.00 | 1 | Training on test task paper, accepted. Far stronger |
| syThiTmWWm | 7.75 | 1 | Cheating automatic benchmarks, accepted. Very clean execution, far stronger |
| Nk1MegaPuG | 4.25 | 2 | "Evading Data Contamination Detection" — rejected. Similar theme, similar experimental gap; current paper is somewhat better executed (more models, clearer methodology) |
| rAylWUIKtu | 4.25 | 2 | "Benchmark Inflation" — rejected. Weaker scope |
| Nsms7NeU2x | 6.75 | 2 | "Forgetting Contamination" — rejected. Stronger empirical + theoretical contribution |
| zWqr3MQuNs | 6.25 | 2 | Min-K% Prob detection paper — accepted. Clean method, well-executed |

**Round-1 bracket**: 4.0–6.5  
**Round-2 narrowing**: Compared to Nk1MegaPuG (4.25, "Evading Detection") which had a similar claim-evidence gap but worse execution, the current paper is slightly stronger—its experiments are more systematic (4 models, 3 datasets, clean protocol). However, compared to BCyAlMoyx5 (5.67, rejected crosslingual paper) and m2NVG4Htxs (6.75, accepted contamination study), the current paper has a more fundamental experimental design gap: the claim about detection failure is not tested at all, whereas those papers at least tested what they claimed. The paper thus sits between 4.25 and 5.67, closer to 4.25 due to the severity of the claim-evidence mismatch.

**Final score: 4.5** — The paper identifies a legitimate research question and provides some useful empirical observations about cross-lingual contamination, but the central claim is unsupported by the experimental design. The key experiment—comparing detection success on English vs. Arabic contamination—is entirely missing. This structural gap prevents the paper from delivering on its stated contribution.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>