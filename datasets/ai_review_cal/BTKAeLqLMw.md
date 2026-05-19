- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 6, 5
Now I have all the information needed. Let me construct the final consolidated review.

## Summary

This paper investigates automatic data selection for instruction tuning by systematically studying three dimensions — complexity, quality, and diversity. It proposes evolution-based scorers (Evol Complexity, Evol Quality) trained on a small 2K seed dataset and an embedding-based diversity filter (Repr Filter), combined into a "score-first, diversity-aware" selection strategy called DEITA. Models trained on 6K–10K automatically selected samples match or outperform models trained on 10–30× more data (e.g., DEITA-Mistral-7B at 6K achieves 7.22 MT-Bench vs. Zephyr-SFT's 5.32 using 200K samples), and the selected datasets and models are released.

## Strengths

1. **Extreme data efficiency convincingly demonstrated.** DEITA-Mistral-7B trained on only 6K SFT samples achieves 7.22 MT-Bench, surpassing the official Zephyr-beta-SFT (200K, 5.32) and Vicuna-13B-v1.3 (125K, 6.39). The scaling curve (Figure 4) shows DEITA with 3K samples matches the full 300K pool — a 100× reduction. These results are clearly presented in Tables 5–6 and verified against the paper.

2. **Novel evolution-based complexity metric consistently outperforms all baselines.** The proposed Evol Complexity achieves MT-Bench scores of 6.27 on \(X_{sota}\) and 5.57 on \(X_{base}\), beating the strongest baseline (Instag Complexity, 6.18 / 4.98) on both data pools (Table 1). This is a genuine empirical advance.

3. **Comprehensive controlled study across three dimensions with multiple baselines.** Sections 3.3–3.5 systematically evaluate 7 complexity metrics, 4 quality metrics, and 3 diversity metrics on two distinct data pools (\(X_{sota}\) and \(X_{base}\)), providing the community with a structured empirical understanding of what drives alignment performance.

4. **Score-first diversity-aware selection works across multiple backbones.** DEITA models based on LLaMA-1-13B, LLaMA-2-13B, and Mistral-7B consistently outperform random-selection baselines and most same-backbone SFT models (Table 5), demonstrating the method's generality.

## Weaknesses

### Fatal
None.

### Major

1. **No statistical significance / error bars reported anywhere.** Every table presents a single run per condition. MT-Bench uses GPT-4 as judge (known non-determinism), and the data selection pipeline itself (scorer training, sample ordering) introduces randomness. Without multiple seeds or confidence intervals, we cannot assess whether differences between, say, Evol Complexity (6.27) and Instag Complexity (6.18) on \(X_{sota}\) are meaningful or noise. The paper's central quantitative claims rest entirely on point estimates. While single-run reporting is common practice in this area, the paper positions itself as a *controlled study* making fine-grained comparisons — this demands error characterization.

2. **Scorer reliability is unvalidated.** The Evol Complexity and Evol Quality scorers are trained on only 2K seed examples to predict ChatGPT scores, but the paper never reports (a) the correlation (Pearson/Spearman) between the trained scorer's outputs and ChatGPT's scores on a held-out subset, or (b) any analysis showing that the learned scores correspond to intuitive notions of complexity/quality. The scorers are central to the method; without validation, the possibility remains that they capture correlated artifacts (e.g., response length, topic cues) rather than the intended construct. This weakens the causal interpretation of the controlled studies.

### Minor

1. **Missing ablation isolating the combination's contribution.** The paper advocates combining complexity, quality, and diversity, but the controlled studies test each dimension *in isolation* (only that dimension for selection), while the full DEITA method uses all three together. There is no experiment directly comparing Complexity-only → Quality-only → Complexity+Quality → Complexity+Quality+Diversity in the same setting. The controlled studies individually demonstrate each dimension helps, but the final ablation — comparing the three-dimensional combination against a two-dimensional (complexity+quality without diversity filtering) variant — is absent, making it harder to attribute the final gains to the multi-dimensional design specifically.

2. **Repr Filter encoding details underspecified.** The diversity filter encodes sentences using LLaMA-1-13B, but the paper does not specify which layer's representation is used, how the sentence is constructed (instruction only, response only, or concatenation), or what pooling method (e.g., last-token, mean) is applied. This affects reproducibility.

### Trivial
None.

## Nice-to-Haves

- A sensitivity analysis of the diversity threshold \(\tau\) (the paper states \(\tau\) is set to a value that was truncated in the PDF extraction) showing performance for 2–3 values would demonstrate robustness.
- A few example high- and low-scored samples from the trained scorers would help readers intuitively validate what the complexity/quality metrics capture.
- Adding scalar comparisons for the "over 10× fewer data" claim (e.g., "6K vs. WizardLM's 70K = 11.7×, vs. Vicuna's 125K = 20.8×") would strengthen the presentation in the abstract.

## Removed Points

- **τ threshold missing value**: The text "We set threshold τ as 0." is almost certainly a PDF parsing truncation (the numeric suffix was lost). The hard rules mandate removing criticisms about missing/extra symbols that are formatting artifacts. *The sensitivity analysis request is preserved as a Nice-to-Have above.*
- **"Over 10× less data" claim too broad**: Checked against the SOTA baselines in Table 5 (WizardLM 70K → 11.7×, Vicuna 125K → 20.8×, Zephyr 200K → 33.3×). The claim holds for all stated baselines; LIMA (1K) is not a SOTA model. The criticism is unfounded.
- **Why 13B backbone for controlled studies**: This is a reasonable design choice and not a weakness — the paper would not be improved by justifying every architecture decision.
- **50K subset arbitrary**: The paper explicitly explains this is a cost-saving measure since Direct Scoring and Instruction Node require ChatGPT annotation of the entire pool. This is standard practice.
- **DPO data clarification**: The paper transparently states "we randomly sample 10K comparison data pairs used in Zephyr."
- **AlpacaEval/MT-Bench inconsistency analysis**: The paper provides a radar plot analysis attributing differences to coding/math/reasoning skills. This is a reasonable qualitative explanation.
- **TruthfulQA dominating average**: Checked Table 6 — the average is not dominated by a single task; improvements are distributed across multiple benchmarks.
- **Missing training hyperparameters for scorers**: The hard rules specify removing nitpicks about undisclosed hyperparameters or trivial implementation details.
- **Missing related works**: Hard rule prohibits mentioning missing references without external verification.
- **Various formatting and presentation nitpicks**: Hard rule prohibits these.

## Novel Insights

Both reviewers identify the same core tension: the paper's empirical results are impressive (6K samples achieving performance comparable to models trained on 200K+), but the evidence foundation has gaps in statistical rigor and internal validation. The most interesting insight from the cross-review is that the controlled studies individually validate each dimension, but the absence of a *combined ablation* (e.g., Complexity+Quality vs. the full three-dimensional method) means the paper's strongest result — DEITA's performance — cannot be fully decomposed into its proposed components. This is a solvable empirical gap, not a structural flaw, and the paper's released datasets enable the community to fill it.

## Suggestions

1. **Add error bars for key results.** Run the main comparisons (Tables 1, 2, 5) with at least 3 random seeds and report the mean and range, or provide bootstrapped confidence intervals for MT-Bench scores. This is the single most impactful improvement.
2. **Validate the scorers.** Report Pearson/Spearman correlation between the trained scorer's outputs and ChatGPT's scores on a held-out subset of the seed data. Show at least 3–5 example pairs with high and low scores to ground what the metrics capture.
3. **Add the missing ablation.** Train models on subsets selected by (1) Evol Complexity alone, (2) Evol Quality alone, (3) s = c × q sorting only (no diversity filter), (4) full DEITA (score-first + diversity). This directly tests whether all three dimensions contribute beyond pairwise combinations.
