Now I have all the information needed. Here is my consolidated final review:

---

## Summary

This paper proposes **AMADEUS**, a training-free framework for RAG-based role-playing agents, consisting of three components: Adaptive Context-aware Text Splitter (ACTS), Guided Selection (GS), and Attribute Extractor (AE). It also introduces **CharacterRAG**, a manually constructed dataset of persona documents for 15 fictional characters (976K characters, 450 QA pairs). The method is evaluated on in-knowledge QA (CharacterRAG) and out-of-knowledge personality prediction (MBTI/BFI), showing benefits over Naive RAG, CRAG, and LightRAG baselines.

## Strengths

- **Substantial improvement on out-of-knowledge personality prediction (MBTI/BFI).** Table 1 shows AMADEUS achieving 85.00% MBTI accuracy and 81.33% BFI accuracy across 15 characters, compared to the next-best CRAG (68.33% MBTI, 76.00% BFI). The total deviation (∑|d|) is also much lower (9 vs. 19+ for MBTI). This demonstrates genuine ability to handle questions beyond explicit character knowledge — the paper's central claim.

- **First dataset designed specifically for RAG-based role-playing agent evaluation.** CharacterRAG fills a real gap: existing RAG datasets target factual QA, and existing role-playing datasets are not built for RAG evaluation. The manual construction (removing extraneous content like popularity polls, preserving hierarchical structure) is thorough. The "w/o RAG" results in Table 4 (18.89%–49.56%) confirm that the dataset cannot be trivially solved by LLMs' parametric knowledge.

- **Consistent improvements across multiple LLMs and embedding models.** The method is evaluated on GPT-4.1, Gemma3-27B, and Qwen3-32B, with ACTS validated across BGE-M3, Qwen3-0.6B, and mE5-large-instruct. The framework maintains the best ACC, ACC_L, and HS scores on CharacterRAG across all three LLMs, and the lowest HS on MBTI/BFI for GPT-4.1 and Gemma3.

- **Human evaluation validates attribute extraction quality.** Table 3 reports Cronbach's alpha of 0.825 (BFI) and 0.810 (MBTI), with mean Likert scores near 4 (out of 5). This provides direct evidence that GS+AE outputs are reasonable from a human perspective.

## Weaknesses

### Major

- **No ablation studies isolating the contributions of ACTS, GS, and AE.** The paper claims three synergistic components, but never tests (a) Naive RAG + ACTS only, (b) Naive RAG + ACTS + GS (no AE), or (c) any subset. Without these, it is impossible to tell whether the marginal gains on CharacterRAG QA come from ACTS alone (a chunking improvement) or from the full pipeline. The chunk similarity analysis (Table 2) evaluates ACTS in isolation, but this is a proxy metric — it is not linked to downstream role-playing quality.

- **Marginal improvement on the primary in-knowledge task (CharacterRAG QA).** On GPT-4.1, AMADEUS achieves 92.67% ACC vs. Naive RAG's 91.33% (+1.34%). On Qwen3-32B, the gap is only +0.45% (78.89% vs. 78.44%). These differences are within the noise floor of single-run LLM evaluations, and no confidence intervals, repeated trials, or statistical significance tests are reported. The paper's strongest quantitative results are on the MBTI/BFI out-of-knowledge task, not on the dataset it introduces.

- **MBTI/BFI ground truth relies on crowd-sourced fan votes with no validation.** The ground-truth labels come from personality-database.com, a crowd-sourced fan site with no peer-reviewed validity established in the paper. Following prior work (Wang et al., 2024b) is acknowledged, but this does not address the underlying concern: the "accuracy" metric measures agreement with an unvalidated external source. The MBTI instrument itself is also controversial in psychometrics (low test-retest reliability, binary categories). While the paper follows community conventions, readers should be aware that the strongest quantitative claim (85% MBTI accuracy) rests on this foundation.

- **Hyperparameter values reported without sensitivity analysis.** Slot size M=2, iteration limit N=30, and overlap coefficient α=2 are used throughout, but no ablation explores how results change with M=1, M=5, N=10, or α=5. The α=2 choice is justified via log-density plots (Figure 4) under a normality assumption, but this optimization is on a proxy (similarity scores), not on downstream role-playing quality (ACC, HS). Performance could be highly sensitive to these choices without the paper establishing robustness.

### Minor

- **GS fallback behavior not reported.** Algorithm 1 specifies that if the slot remains empty after N iterations, the system falls back to Top-(K+1) chunks from semantic similarity. The paper does not report how often this fallback occurs, which is critical: if it triggers frequently, GS adds little value over Naive RAG for those queries.

- **LLM-based evaluation uses the same model class (GPT-4.1) for both generating responses and evaluating them.** The metrics (ACC, ACC_L, HS) are assessed by LLMs of the same family as the generator. This introduces potential self-evaluation bias. No calibration against human judgments is provided for these metrics.

- **Human evaluation (Table 3) evaluates GS+AE outputs in isolation, not final response quality.** The Likert scores show that extracted attributes are "reasonable" (mean ~4), but this does not directly demonstrate that the final generated responses are better. The connection from "attributes are reasonable" to "final responses are more persona-consistent" is assumed rather than tested.

- **Dataset scope is limited to 15 characters from a single Korean source (Namuwiki).** While manual construction is labor-intensive, the narrow genre base (anime/manga from one wiki) and the small total (450 QA pairs) limit the generality of conclusions about RAG-based RPA performance. Per-character persona size varies widely (32K–145K characters), and this imbalance is not controlled in the experiments.

### Trivial

None.

## Nice-to-Haves

- An ablation study isolating ACTS, GS, and AE on the CharacterRAG QA task would substantially strengthen the paper. If ACTS alone accounts for most of the gain, the method simplifies to a better chunker; if GS+AE are needed, the paper should show a meaningful gap.
- Reporting the frequency of GS fallback to Top-(K+1) would help assess whether GS is actually selecting informative chunks or frequently defaulting.
- Adding statistical significance or confidence intervals (e.g., bootstrap over 450 questions) would clarify whether the 1–2% ACC gains are real.

## Removed Points

These points from the reviewers were removed after verifying against the paper:

- **"Circularity: GS uses the same LLM that generates responses"** — The reviewer's concern is noted but the paper's design is defensible: GS uses the LLM to judge whether a chunk *allows attribute inference*, which is a different capability from generating the final response. The same LLM performing both roles is not circular in a strict sense, though the paper could discuss potential bias.

- **"CRAG and LightRAG baselines are unfair comparisons"** — The paper explicitly selects these to investigate the effects of web search and graph-based systems on role-playing. The finding that they underperform is a stated goal of the experiment, not a bug. The claim "graph-based RAG and web search-based RAG are unsuitable for role-playing" is framed as a finding supported by the comparison.

- **"Example in Figure 3 uses character (Yuu) not in the dataset"** — Valid observation but trivial. The figure is a framework illustration, not an evaluation sample. Using a distinct character for illustration is common practice.

- **"No details about annotator qualifications or inter-annotator agreement"** — Valid point but relatively minor; many dataset papers provide similar-level descriptions of construction procedures.

- **"The in-knowledge/out-of-knowledge framing is confusing"** — The paper clearly distinguishes between CharacterRAG QA (in-knowledge) and MBTI/BFI (out-of-knowledge). This is stated explicitly in Sections 5.2 and 5.3.

- **"No details about prompt design for AE"** — The paper describes AE as extracting "Belief and Value" and "Psychological Traits" from chunks. While the exact prompt is not shown, the human evaluation in Table 3 validates the quality of these extractions, partially addressing this concern.

## Novel Insights

None beyond the paper's own contributions. The paper's most novel insight — that hierarchical context augmentation coupled with LLM-driven chunk selection and attribute extraction can help RAG-based RPAs answer out-of-knowledge queries — is well-motivated by Figure 1's observation about chunk duplication in Naive RAG, but the lack of component ablation means this insight remains suggestive rather than proven.

## Suggestions

1. Add a systematic ablation study on the CharacterRAG QA task: Naive RAG → +ACTS → +ACTS+GS → +ACTS+GS+AE (full AMADEUS). This is the single most important addition to validate the framework's architecture.
2. Report confidence intervals or standard deviations from repeated runs (or bootstrap resampling) for the main results in Tables 1 and 4.
3. Report how often the GS fallback (line 14–16 of Algorithm 1) is triggered, and show that the method still outperforms baselines when controlling for this frequency.
4. Provide a sensitivity analysis for M (slot size), N (iteration limit), and α (overlap coefficient) on downstream metrics (ACC, HS), not just proxy similarity scores.

## Score and Decision

**Calibration (3 rounds, 10 anchors):**

Round 1 bracketing placed the paper between weak anchors (avg 2.33–3.00) and strong anchors (avg 8.00). Weak anchors (Reward-RAG 3.00, Multimodal RAG QA 2.50, EDU-RAG 2.33) had significant methodological flaws; this paper is clearly stronger. Strong anchors (Trustworthiness in RAG 8.00, Retrieval Head 8.00) are methodologically rigorous papers well above this paper's current standard.

Round 2 narrowing pulled anchors in the 3.5–7.5 range. *PersonaEval* (4.00) is a benchmark paper with limited scope — our paper is stronger, with a full method + dataset. *Late Chunking* (4.75) proposes a chunking method with clean evaluation but narrower scope — comparable overall, but our paper has more ambitious claims. *CtrlA* (4.50) has similar evaluation gaps (ablation missing, hyperparameters unexamined) — our paper is slightly stronger because of its dataset and human evaluation. *RPA Refusal* (5.20) has a similar scope to our paper (RPA benchmark + method) with comparable rigor — roughly equivalent. *SubgraphRAG* (6.00, Accept) has stronger evaluation with ablation studies and multiple datasets — clearly above our paper. *ChatEval* (5.60, Accept) has thorough evaluation and multi-model validation — somewhat above our paper.

Round 3 was not needed.

**Positioning relative to anchors:** The paper is above Late Chunking (4.75) and CtrlA (4.50) due to the dataset contribution and human evaluation, comparable to RPA Refusal (5.20), but below SubgraphRAG (6.00) and ChatEval (5.60) due to the absence of ablation studies, the marginal improvement on the primary task, and reliance on unvalidated ground truth for the strongest result.

**Final score: 5.0**

The paper tackles a real and under-explored problem, proposes a plausible framework, contributes a manually constructed dataset, and shows promising results on the out-of-knowledge personality prediction task. However, the evaluation has significant gaps: no ablation studies, marginal (sub-2%) gains on the in-knowledge QA task without statistical significance, unvalidated ground truth for the headline result, and no hyperparameter sensitivity analysis. These weaknesses collectively prevent the paper from meeting the acceptance bar in its current form, though the core ideas are worth pursuing with stronger evaluation.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>