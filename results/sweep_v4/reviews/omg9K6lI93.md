Now I have everything I need. Let me write the consolidated final review.

## Summary

This paper investigates whether translating benchmark data into Arabic can mask data contamination in LLMs. The authors fine-tune four open-weight models on varying proportions of Arabic-translated test data alongside the original English test data, evaluate on the original English benchmarks, and probe memorization via an extended TS-Guessing method with choice-reordering. They find that MMLU accuracy rises monotonically with added Arabic contamination while standard English-only detection checks (TS-Guessing) show limited signal, and propose a Translation-Aware Contamination Detection (TACD) framework as a forward-looking blueprint.

## Strengths

- **Choice-reordered TS-Guessing provides a concrete, non-trivial contamination signal.** The extension of TS-Guessing with choice reordering for multiple-choice questions (Section 3.3) is methodologically sound. The IDR metric in Table 3a captures genuine memorization: LLaMA-3.2-1B-Instruct reaches IDR = 0.643 at 50% contamination on MMLU, far above chance, indicating memorization that surface-form checks would miss.

- **Identification of task-dependent contamination patterns.** Table 2 reveals an interesting divergence: MMLU accuracy rises monotonically with Arabic contamination across all models, while XQuAD/MLQA (extractive QA) exhibits consistently non-monotonic trends (e.g., Qwen's MLQA spikes at 10% then collapses below baseline). This nuanced observation shows that contamination effects depend on task format (closed-book MCQ vs. extractive QA), which a monolithic contamination narrative would miss.

- **The paper raises a timely and underexplored question.** The issue of multilingual contamination — whether translation can inadvertently create a blind spot in benchmark evaluation — is important and understudied. The paper correctly identifies that current detection pipelines are overwhelmingly English-centric and that the community needs multilingual-aware approaches.

## Weaknesses

### Fatal

- **The experimental design trains on the test set and evaluates on the same test set, invalidating the core comparison.**  
  Equation (1) and the surrounding text (lines 134–146) define the training set as  
  `D_train^d(p) = D_EN^d ∪ D_AR^d(p)`, where for MMLU, `D_EN^d` is explicitly described as "English test items." The Arabic portion `D_AR^d(p)` is defined as "Arabic translations of the test items." Every condition — including the p=0 baseline — therefore trains on the English test data itself. The model is then evaluated on "the standard evaluation split(s)" (Section 3.2), which for MMLU/XQuAD/MLQA is the same test split. This means the p=0 condition is already fully contaminated with the evaluation data, and the entire comparison (p=0 vs. p>0) compares training on the test set against training on the test set plus more of it. The paper never acknowledges this. Consequently, the central claim that "translation conceals contamination" is comparing degrees of contamination from a baseline that is already circular. The evaluation scores at p=0 cannot separate genuine model ability from test-set memorization, and adding Arabic contamination on top does not produce a clean measure of whether translation "masks" contamination — it simply adds another layer of test-set exposure.

### Major

- **The paper lacks a necessary control: fine-tuning on the original English test set alone as the upper-bound contamination condition.**  
  Without comparing the Arabic-contaminated conditions against a condition where the model is fine-tuned on exact English duplicates (same language, same content), the claim that translation "masks" contamination is unsupported. A meaningful experiment would compare: (1) clean model → evaluate on English benchmark, (2) model fine-tuned on English test set → evaluate, (3) model fine-tuned on Arabic-translated test set → evaluate. The difference between (2) and (3) would quantify how translation affects both performance gains and detectability. The current setup only compares different proportions of Arabic contamination on top of a fully English-contaminated baseline, which cannot separate the masking effect of translation from the general effect of having more training data on the test content.

- **The TS-Guessing results are contradictory to the paper's own narrative.**  
  The paper argues that translation "conceals contamination signals" because TS-Guessing (Table 3) shows low scores while evaluation gains are observed (Table 2). However, Table 3a shows that some models produce clearly non-zero IDR scores (LLaMA at 50%: 0.643; Gemma at 10%: 0.350), indicating that the method *does* detect contamination even through translation. The paper never systematically explains why the method works on some model/contamination-level combinations and not others. The claim that translation uniformly masks detection is contradicted by the data in the same table.

- **Results are reported without variance or significance.**  
  Table 2 reports single-point accuracy numbers with no error bars, confidence intervals, or replication. The non-monotonic patterns in XQuAD/MLQA (e.g., Mistral XQuAD: 0.455 → 0.272 → 0.114) could reflect random variation, and the paper over-interprets these as "fragile transfer" and "overfitting to distributional quirks" without any statistical grounding. With only one run per condition, the observed patterns cannot be distinguished from noise.

### Minor

- **No pre-existing contamination audit.** The paper does not check whether the base models (Mistral-7B, LLaMA-3.2-1B, etc.) were pre-trained on the original English benchmarks. This means some of the observed performance at p=0 could reflect prior contamination rather than the fine-tuning. An audit using Min-K% Prob or similar methods would strengthen the analysis.

- **The TACD framework (Section 5) is presented as a contribution but is only a verbal sketch.** The paper openly states it is a "forward-looking blueprint rather than a complete implementation." While the direction is reasonable, including it as a major section inflates the claimed contribution without supporting evidence. Removing or substantially shortening this section and focusing on the empirical analysis would produce a stronger paper.

- **The claim that models with "stronger Arabic capabilities" benefit more from Arabic contamination is not supported by any quantitative Arabic proficiency measure.** The paper relies on model size as an implicit proxy, but provides no Arabic-language benchmark scores (e.g., ArabicMMLU, ACVA) to substantiate this specific claim.

### Trivial

- The literature review (Section 2) is disproportionately long (~40% of the main text) and largely generic, covering known contamination taxonomies without tightly connecting them to the paper's multilingual angle until the final paragraph.

## Nice-to-Haves

- A cross-lingual transfer control: fine-tune on Arabic translations of *different* benchmarks (not the evaluation set) to measure whether Arabic fine-tuning improves English benchmark performance through language alignment rather than content memorization.
- Per-sample analysis of the non-monotonic XQuAD/MLQA trends to explain whether the 10% spikes are driven by a subset of questions.
- Concrete embeddings similarity figures (histogram of cosine similarities between Arabic→English translations and originals) to support the semantic preservation claim in the discussion.

## Removed Points

- **"The contamination setup is not a realistic contamination scenario"** — The harsh critic argues this is unrealistic. However, intentional contamination is a standard way to study detection methods in controlled settings (see the Evading Contamination Detection paper at avg 4.25, which uses a similar deliberate-contamination paradigm). The unrealistic setup is not itself a flaw; the flaw is that the design is circular (training on the test set). This point is subsumed by the fatal weakness above.

- **"TACD is not a contribution"** — The paper explicitly calls it a "blueprint," so claiming it is not a contribution is stating the obvious. I have downgraded this to a Minor weakness about overclaiming, not a fatal omission.

- **"Pre-existing contamination not controlled"** — Kept as Minor rather than Major, since the paper's design is already fatally flawed by training on the test set, making this a secondary concern.

- **Strength Finder claims about TACD being a strength** — Removed as a strength because the framework is unimplemented. The paper's own description ("blueprint rather than a complete implementation") disqualifies it as a strength.

- **Generic strengths from Strength Finder** ("the paper addresses an important problem", "timely topic") — Removed as too generic.

## Novel Insights

None beyond the paper's own contributions. The observation that MCQ accuracy and extractive QA accuracy respond differently to Arabic-translated contamination is genuine but cannot be interpreted as a robust finding given the fatal design flaw.

## Suggestions

1. Restructure the experiment so that the p=0 baseline is a genuinely clean model (no exposure to the English test set during fine-tuning). The Arabic-contaminated conditions should be compared against this clean baseline, not against a model already trained on the English test data.
2. Add an English-contamination control: fine-tune on the English test set (same language, same content) and compare detection rates against the Arabic-contaminated condition. This would quantify the degree to which translation reduces detectability.
3. Report all results with variance (multiple seeds or bootstrapped confidence intervals). Without this, the non-monotonic patterns cannot be distinguished from noise.
4. Provide quantitative Arabic proficiency scores for each model to support the claim that stronger Arabic models benefit more from Arabic contamination.
5. Either implement TACD as a proof-of-concept on a small scale, or remove the section and let the empirical findings speak for themselves.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Nk1MegaPuG.md` | 4.25 | Similar topic (evading contamination detection), same style of deliberate contamination experiments. That paper at least had a non-circular experimental design; this paper is weaker. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Nsms7NeU2x.md` | 6.75 | Stronger paper with controlled experiments, theoretical framework, and proper training-from-scratch setup. This paper is substantially weaker. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/m2NVG4Htxs.md` | 6.75 | Strong longitudinal analysis with proper methodology. This paper is substantially weaker. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/KS8mIvetg2.md` | 7.50 | Rigorous statistical framework for contamination detection. This paper is far weaker. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/jOmk0uS1hl.md` | 8.00 | Clean experimental design, clear contribution. Not comparable in methodological rigor. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/rAylWUIKtu.md` | 4.25 | Methodological concerns but at least a non-circular design. Comparable in overall quality level. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/JL42j1BL5h.md` | 3.50 | Multilingual safety paper with superficial analysis. Similar quality level — both have major methodological gaps. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/lwtaEhDx9x.md` | 4.75 | Better-executed memorization study for tabular data. Slightly stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ICwdNpmu2d.md` | 1.50 | Truly weak paper — completely different domain. This paper is better than that. |

The paper has a fatal design flaw that undermines its central claim: training on the evaluation test set and then evaluating on it. Compared to anchors like Nk1MegaPuG (4.25, same topic area but with a valid experimental design) and rAylWUIKtu (4.25), this paper is weaker because its fundamental comparison (p=0 vs p>0) compares a contaminated baseline to a more-contaminated condition. The TS-Guessing extension is a genuine methodological contribution, and the task-dependent contamination pattern is interesting, but these cannot rescue a fatally flawed central experiment.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>