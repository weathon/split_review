- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3
Now I have all the information I need to produce the final consolidated review. Let me synthesize everything carefully.

---

## Summary

This paper systematically explores the design space of Speech-Conditioned LLMs (SLMs) through controlled experiments on adaptor architecture, masking strategy, LLM choice, and training data. Its central contribution is identifying that existing SLMs fail to follow spoken instructions because their training data contains only text-form instructions with speech as context, never speech-form instructions. Using a synthetic 50K spoken-instruction dataset, the authors build **SiM**, which significantly outperforms prior SLMs on spoken instruction following (e.g., >125% higher scores on AudioBench datasets) while achieving competitive ASR with less training data.

## Strengths

1. **Systematic controlled comparison of SLM design choices** — The paper runs alignment-training experiments with consistent setups across adaptor architecture (MLP vs. Q-Former vs. C-abstractor), masking strategy, LLM type (instruction-tuned vs. base), and training data (Tables 3–5, Section 3.1). This provides actionable findings that prior SLM works, which vary multiple factors simultaneously, could not isolate. Key result: a simple 2-layer MLP adaptor outperforms more complex architectures.

2. **Identification and remediation of a genuine capability gap** — The paper demonstrates that models like SALMONN and Qwen Audio Chat cannot handle speech-form instructions because they were never trained on them (Section 3.2.1). This is a novel finding with practical significance. By generating synthetic spoken-instruction data (50K samples via Amazon Polly + a strong private LLM), the paper enables SiM to achieve substantially better spoken instruction following than existing SLMs (Table 6).

3. **Human evaluation corroborates automated metrics** — The paper validates its main claim with human preference annotations on 100 test prompts from both OpenHermes Audio and Alpaca Audio datasets (Figure 2). Human judgments show SiM preferred over baselines, confirming the trend from the Llama3-70B-as-judge evaluation.

4. **Finding that simpler adaptors are superior** — The empirical result that a 2-layer MLP adaptor yields lower WER than more elaborate Q-Former or C-abstractor designs (Section 3.1, Experiment #1) directly challenges the default complex-adaptor design in prior SLMs and provides a clear, cost-saving recommendation for practitioners.

5. **Competitive ASR with substantially less data** — SiM achieves WER comparable to Qwen and WavLLM on LibriSpeech test-clean while using less than one third of the ASR training samples (Section 3.2.2, Table 8), demonstrating data efficiency.

## Weaknesses

### Fatal
None.

### Major

1. **LLM backbone confound in head-to-head comparisons** — SiM uses Llama3 8B Instruct as its backbone, while existing SLMs (SALMONN, Qwen Audio Chat, WavLLM) are built on older, weaker backbones (Vicuna, Llama2). The paper acknowledges this (line 44: "While some existing SLMs are built upon Vicuna or Llama2") but does not control for it. This means the large performance gaps in Tables 6 and 7 may partially reflect backbone strength rather than the proposed training recipe. A controlled comparison using the same backbone across methods is needed to cleanly attribute improvements.

2. **Missing controlled ablation isolating instruction modality** — The paper claims that "spoken instruction following data is crucial" and that existing SLMs fail because "instructions are provided in text form." To substantiate this, the paper compares SiM (trained with spoken instructions) to existing SLMs (trained with text instructions). However, these differ in backbone, training data composition, and data scale — not just instruction modality. A controlled experiment training SiM variants with (a) spoken instructions vs. (b) text instructions (with speech as context, mirroring the baseline training setup) would directly quantify the value of the speech modality. Without this, the central claim that speech modality per se is the enabling factor is not fully isolated from the effect of adding instruction-tuning data in any form.

### Minor

1. **Automated judge shares model family with SiM** — The evaluation uses Llama3 70B Instruct as the automated judge for response quality (Table 6). Since SiM is built on Llama3 8B Instruct, there is a potential stylistic familiarity that could inflate scores. The human evaluation (Figure 2, 100 prompts/dataset) corroborates the trend and partially mitigates this concern, but the human sample is modest and no inter-annotator agreement is reported.

2. **Synthetic data generation details are incomplete** — The paper generates synthetic responses using "one of the top-performing private LLMs" (line 114) without disclosing which model. This limits reproducibility. Releasing the generated dataset or specifying the model would substantially improve the paper's value to the community.

3. **Cross-reference errors** — Section 3.1, Experiment 5 says "More details of these datasets are presented in Section TBD" (line 87), and line 81 references "Table 7" when discussing the LLM choice experiment (should refer to Table 4). These are minor but should be corrected.

### Trivial
None.

## Nice-to-Haves

- **Error bars / significance tests**: The paper reports all WER and instruction-following scores from single training runs without variance or significance tests. Reporting standard deviations across multiple runs or seeds would strengthen confidence in the conclusions, though single-run evaluation is common in this space.
- **Scaling exploration**: The alignment experiments use 100K–200K samples; it would be useful to know whether the design-choice conclusions (e.g., MLP > Q-Former) hold at larger data scales.
- **Analysis of residual gap**: On Alpaca Audio, SiM still lags 0.74 behind the text-input Llama3 baseline. The paper notes this but does not analyze the cause (e.g., ASR errors, loss of prosodic nuance). Such analysis could guide future work.

## Removed Points

- *"Unfair evaluation of existing SLMs (testing them on spoken instructions is OOD)"* — **Removed.** The paper is explicitly testing the capability of spoken instruction following, which is a natural and reasonable evaluation for speech-conditioned LLMs. The paper's entire point is to identify that these models fail at this task and why. The evaluation is not unfair; it reveals a genuine limitation. The critic's suggestion (testing with text-form instructions alongside speech) would be a useful additional analysis but the current evaluation is valid as-is.
- *"Overclaiming in abstract"* — **Removed.** The abstract's claim that "current SLMs struggle to follow speech instructions" is directly supported by the paper's experiments with SALMONN, Qwen Audio Chat, and WavLLM on spoken queries.
- *"Missing error bars"* — **Demoted to Nice-to-Have.** Single-run evaluation is standard practice in this area; requesting variance is reasonable but not a weakness in the reject sense.
- *Generalized scope-creep criticisms* (e.g., demanding larger datasets, more baselines, larger human eval without specific justification) — **Removed.** The paper's experimental scope is adequate for its claims; additional scale would strengthen but is not required.

## Novel Insights

The most interesting observation that emerges from the review process is that the paper's core value proposition has two separable parts: (1) the systematic, controlled exploration of SLM design choices (which is well-supported), and (2) the specific finding about speech-form instructions (which is plausible and practically important but under-validated due to the backbone confound and missing ablation). These two contributions have different evidential strengths. The design-space exploration findings are clean and well-executed; the speech-instruction claim is more suggestive than conclusive. The review process surfaces that the paper would be more persuasive if these two threads were either better disentangled or if the second thread received the same controlled experimental treatment as the first.

## Suggestions

1. **Address the backbone confound**: Train a version of SALMONN or Qwen Audio Chat using Llama3 8B Instruct as the backbone (or train SiM with an older backbone) to enable a fairer comparison of the training recipe rather than the LLM strength.
2. **Add the speech-vs-text instruction ablation**: Train a SiM variant using the same 50K instruction samples but with text-form instructions (speech as context), holding all other factors constant. Report the gap in spoken instruction following between this variant and the spoken-instruction variant.
3. **Specify the private LLM** used for synthetic data generation and commit to releasing the 50K spoken-instruction dataset.
4. **Fix cross-references**: Replace "Section TBD" with the correct section and fix the "Table 7" → "Table 4" error.
