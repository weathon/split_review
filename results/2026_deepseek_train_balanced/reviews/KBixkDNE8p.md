## Summary

This paper proposes "LLM Psychology," a framework that applies the Typoglycemia (scrambled text) phenomenon from human psychology to study large language models. It introduces TypoPipe, a systematic pipeline for generating scrambled text at character, word, and sentence levels with multiple operation types (reorder, insert, delete) and positional variants, then tests 8 LLMs across several datasets. The paper reports accuracy degradation patterns, anomalous cases where scrambled text *improves* accuracy (notably GPT-4o on BoolQ), increased computational costs, and hidden-layer representation analyses. The core contribution is a systematic multi-granularity stress-test benchmark for LLM robustness.

## Strengths

1. **Multi-granularity experimental design goes beyond prior work.** The paper extends Typoglycemia from character-level scrambling (the sole focus of prior work like Cao et al. 2023 and Singh et al. 2024) to word- and sentence-level perturbations, with three operation types (reorder, insert, delete) each applied at multiple positions (ALL, INT, BEG, END, ADJ, REV). This yields over 20 distinct scrambling conditions across three granularities — a genuinely more comprehensive probe than any existing single-level test. The formalization in Sec. 3.1 (Eq. 1–2) and the TypoFunc taxonomy (lines 148) make the space of operations explicit.

2. **Documentation of anomalous accuracy improvements.** The paper identifies cases where scrambled text *improves* accuracy — most strikingly, GPT-4o on BoolQ achieves a T_rel of 101.1% (Table 1, line 291), meaning it performs better on scrambled prompts than on the original. This finding is replicated across both reordering (Table 1) and insertion/deletion experiments (Table 2, lines 450–451: 90.9% of gray-marked entries appear on BoolQ). This counter-intuitive result is non-trivial and provides a concrete anchor for discussing the difference between LLM and human processing.

3. **Cross-task convergent validity.** The paper designs two task families — TypoC (completion) and TypoP (perception, including Rectify). Accuracy rankings across LLMs on TypoP-Rectify match those on TypoC for 7 out of 8 models (Sec. 4, Obs.5, line 406). This demonstrates that the observed effects are robust to task format and not a prompt-engineering artifact.

4. **Computational cost measurement provides a parallel behavioral signal.** The paper measures both token and time consumption ratios under scrambling (Figure usage, lines 356–362), finding that all models show ratios > 1 in 100% of cases. This adds a dimension beyond accuracy — cost — that can be used to characterize model behavior under perturbation.

## Weaknesses

### Fatal

None. The paper has major issues but nothing that invalidates the entire empirical contribution.

### Major

1. **No human-subject data despite explicit "Human" performance comparison.** The Figure 1 caption (line 22) claims a "performance comparison among Human, Llama-3.1, GPT-4 on BoolQ dataset," RQ4 asks "Why do LLMs align with human performance," and the paper repeatedly claims LLMs exhibit "human-like behaviors." Yet the paper presents **zero human-subject data**. Every claim about human performance is supported only by citations to psychology literature (Rayner 2006, Ferreira 2002, etc.), which used different stimuli and tasks than those in this paper. Without measuring human accuracy on scrambled BoolQ, GSM8k, and CSQA under the *same* scrambling conditions, the "human-like" framing is empirically unsupported. The paper would be substantially stronger if it dropped this framing and presented the work as a systematic robustness benchmark.

2. **MBPP dataset listed but results entirely absent.** The Datasets section (line 146) lists MBPP for code generation as one of five datasets. The main results table (Table 1) only includes GSM8k, BoolQ, and CSQA. The INS/DEL table (Table 2) also excludes MBPP. SQuAD appears only in the hidden-layer analysis (Figure 5) with accuracy numbers mentioned in passing (line 517), but not in the main table. **MBPP never appears in any result.** The paper claims "comprehensive experiments... across 5 datasets" (line 36) but reports full results on only 3. This gap undermines the claim of comprehensiveness.

3. **Central interpretive claim does not follow from the evidence.** The paper's headline finding is that LLMs' human-like abilities are "fundamentally statistical and data-driven, rather than genuinely resembling human cognition" (line 30). The evidence offered: (a) scrambled text sometimes yields slightly *higher* accuracy than unscrambled text (≤0.7% average increase on BoolQ); and (b) hidden-layer representations of scrambled and unscrambled text are cosine-similar. Neither supports the conclusion. A small accuracy increase on a specific dataset does not logically imply "data-driven, not cognitive" — it could equally reflect the model using different features that happen to be more informative. Finding that representations are similar across scrambling conditions is neutral with respect to whether the model has anything worth calling cognition. The paper conflates "using a different mechanism than humans" with "merely statistical, not cognitive." This is a philosophical assertion, not an empirical finding.

4. **No variance or statistical testing.** All results are reported as means over 3 runs with no standard deviations, confidence intervals, or significance tests. Many effects the paper discusses are small (e.g., 0.7% improvement on BoolQ, differences of 1–3% between conditions). Without variance estimates, the reader cannot assess whether these are real effects or noise. This is especially problematic given the strong comparative and interpretive claims being made.

### Minor

1. **"Cognitive pattern" claim overinterprets a trivial finding.** The paper claims each LLM has a "unique and consistent cognitive pattern" based on a cosine similarity of 0.9994 between heatmaps of hidden-layer representations across SQuAD and BoolQ for Llama-3.1-8B (line 519). A cosine similarity of 0.9994 between two heatmaps from the *same model* (same weights, same architecture) on two different datasets means the representations are nearly identical — which is expected. This does not reveal a model-"unique" pattern (no cross-model comparison is shown — the heatmaps are only for one model) and calling it a "cognitive pattern" is dramatic overinterpretation. The finding of representation stability across tasks is valid but mundane.

2. **"Encoder" analysis uses an external embedding model, not the LLM's internal representations.** The "encoder" analysis (Table embedding sim, lines 486–493) uses text-embedding-3 to embed text and compute cosine similarity between original and scrambled versions. This is a black-box embedding model, not an analysis of the LLM's own internal processing. The "decoder" analysis (Figure hidden sim, lines 497–509) is more direct, but the paper does not explain how representations are extracted or pooled from individual tokens to a single vector per input. Different pooling strategies could yield different results.

3. **No analysis of BPE tokenizer interaction with character-level scrambling.** The paper mentions BPE tokenization (line 28) but never analyzes how character-level scrambling interacts with the tokenizer. Character scrambling can produce tokens that are extremely rare or unknown, which is a fundamentally different phenomenon from human Typoglycemia (where letters are rearranged but sublexical units remain familiar). This is a significant missed opportunity for the mechanistic analysis.

4. **The TypoPipe formalism (Eq. 1–9) is not actually used.** Equation 1 defines dataset selection as an optimization problem but is never optimized — the paper says "we heuristically select tailored datasets" (line 82). The formal apparatus adds notation but is not used in any subsequent analysis or implementation. It could be removed without affecting the paper.

5. **"Pioneer" claim is overstated.** The paper claims to be "the pioneer to systematically transfer cognitive psychology methodologies and experiments to LLMs" (line 35). Prior work (Cao et al. 2023, Singh et al. 2024) has tested LLMs on scrambled text, though the paper's multi-granularity extension and deeper mechanistic analysis do constitute a meaningful advance. The claim should be qualified.

6. **Exact-match evaluation for free-form responses.** The paper uses exact-match accuracy (line 97: "a response correct only when the LLM's output exactly matches the correct answer") but does not describe how answers are parsed/extracted from free-form LLM outputs. This matters because LLMs can produce correct answers embedded in different formats or additional text.

### Trivial

- The color-coding scheme in Table 1 (red, blue, green, gray) uses somewhat inconsistent criteria: gray marks values "higher than BASE," but on BoolQ many gray entries are trivially higher because BASE accuracy is relatively low, diluting the informativeness of the highlighting.

## Nice-to-Haves

- A cross-model comparison in the hidden-layer analysis (comparing representation geometries of different models on the same tasks) would substantially strengthen the "unique cognitive pattern" claim if it held up, or clarify that the pattern is architecture-driven rather than model-specific.
- Analyzing how different scrambling operations interact with the BPE tokenizer's byte-pair merges would provide a concrete mechanistic explanation for why some models are more robust than others.
- Error bars or confidence intervals for the main results would be straightforward to compute from the 3 runs already conducted.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **From Harsh Critic:** "The paper claims 'we are the pioneer'... contradicted by the paper's own Related Work which cites Cao et al. (2023) and Singh et al. (2024) doing exactly this." — Cao et al. and Singh et al. test LLMs on scrambled text but do not present a systematic multi-granularity framework grounded in cognitive psychology methodology. The "pioneer" claim is overstated but not factually contradicted by these references. Moved here because the criticism is slightly inaccurate; the claim has been redressed as a Minor weakness instead.
- **From Harsh Critic:** "The mathematical formalism could be removed without affecting the paper" — This is a valid presentation critique but is not a weakness of the science. Retained as Minor #4.
- **From Strength Finder:** "Hidden-layer 'cognitive pattern' consistency across datasets (cosine similarity of 0.9994)" as a strength — This finding does not support what the paper claims it supports. Near-identical heatmaps from the same model on two datasets is expected, not a "unique cognitive pattern." Moved here because it conflicts with a verified weakness (Minor #1).
- **From Strength Finder:** Generic praise about the importance of the problem — removed per policy.

## Novel Insights

Beyond the paper's own contributions, the main novel insight that emerges from the reviews is that the paper's strongest contribution (the systematic scrambling benchmark) is orthogonal to its most overreaching claim (that LLMs are "data-driven, not cognitive"). The experimental methodology — testing 8 models across 3 granularities with 20+ operation variants — is a genuinely useful resource for robustness evaluation, independent of any psychological interpretation. The anomalous accuracy improvements on BoolQ deserve deeper investigation: because they replicate across two independent scrambling families (reordering and insertion/deletion), they are unlikely to be noise, and understanding why certain scrambling operations help on simple QA tasks could yield insights into how LLMs use positional cues.

## Suggestions

1. **Remove or substantially revise the human-cognition framing.** Drop the unsubstantiated "Human" data points from Figure 1, remove claims about "LLM Psychology" as a new field, and present the work as a systematic robustness benchmark. The empirical contribution stands on its own.
2. **Add MBPP results** or remove MBPP from the dataset list.
3. **Report standard deviations or confidence intervals** for the 3-run averages, and use statistical tests for comparative claims (e.g., "position X matters more than position Y").
4. **Add an analysis of how character-level scrambling interacts with the BPE tokenizer** — this would strengthen the mechanistic analysis and clarify the relationship (or non-relationship) to human Typoglycemia.
5. **Clarify the representation extraction methodology** — how are token-level representations pooled to a single vector per input? What pooling strategy was used and why?

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>