Now I'll write the final consolidated review.

## Summary

This paper presents MobileLLM-R1, a family of sub-billion-parameter reasoning models (140M, 360M, 950M) trained on only 4.2T tokens (~2T unique) of carefully curated open-source data. The authors propose a benchmark-free data mixture optimization using influence scores (self- and cross-capability), a data-model co-evolution strategy for mid-training compression, and release a complete open training recipe. MobileLLM-R1-950M achieves an AIME24 score of 15.5 and LiveCodeBench score of 19.9, matching or surpassing Qwen3-0.6B (trained on 36T tokens) while using only 11.7% of the token budget. The paper challenges the assumption that small reasoning models require massive corpora.

## Strengths

- **Token efficiency breakthrough with strong empirical results.** MobileLLM-R1-950M achieves 15.5 AIME24 and 19.9 LiveCodeBench using only 4.2T tokens — 11.7% of Qwen3-0.6B's 36T corpus — while matching or exceeding its performance (Table 9). The 140M model achieves 16.3% GSM8K vs. 1.8% for SmolLM2-135M (Table 8). These results are consistent across three model scales and multiple benchmarks, providing strong evidence that data quality, not just scale, drives reasoning in small models.

- **Comprehensive open release.** The paper releases model weights, training code, complete data sources with URLs and mixing ratios (Tables 5, 6), and the full training recipe. This level of transparency is rare and practically valuable for the community — it enables full reproduction and serves as a concrete reference for practitioners building small reasoning models.

- **Mid-training data-model co-evolution is sound and well-demonstrated.** The iterative influence-based compression (Section 3) uses the model *itself* (θ_t) to filter samples — not separate domain-specialized models. Figure 5 shows influence histograms converging toward zero, and Figure 6 shows the subsampled data avoids the performance dip seen with the original data on MMLU. This contribution is methodologically clean and not affected by the cross-influence concern.

- **Strong ablation and analysis.** Table 1 thoroughly ablates the post-training pipeline (staged Tulu-3 → reasoning SFT outperforms joint training). Table 2 controls for reasoning SFT data across models, isolating pretraining quality. Appendix D.1 provides interesting RankMe analysis connecting learning rate to representation quality. Appendix D.2 investigates RL applicability for small models.

- **On-device profiling validates practical motivation.** Table 10 shows the 140M model sustains >100 tokens/s up to 8k context on a Samsung Galaxy S22, while larger models hit OOM — directly supporting the paper's deployment motivation.

## Weaknesses

### Major

- **Cross-influence computation using domain-specialized models is not theoretically grounded.** Section 2.2 computes cross-influence of a code sample on math performance using θ_{M,t} — a model trained exclusively on math data. The influence function in Equation 2 requires θ* to have been trained on the sample x_i. When a code sample's influence on math is evaluated using a math-only model θ_{M,t} that has never seen any code data, the theoretical assumptions of influence functions are violated. The resulting scores do not measure "how a code sample affects math performance in a joint model" — they measure how a code sample would affect a *math-only* model. The paper presents this as a principled extension of AutoMixer but provides no justification or analysis of why this approximation should be valid. The claim of a "principled, benchmark-free" data mixture optimization is therefore overstated. This does not invalidate the empirical recipe (the resulting mixture empirically works better than uniform, per Figure 4), but it undermines the methodological contribution as currently framed.

- **Data mixture optimization lacks competitive baselines.** Figure 4 compares the influence-derived mixture ("Datamix") only against uniform sampling ("Original"). There is no comparison against simple heuristics (e.g., up-weighting math/code by fixed factors, perplexity-based weighting, or the REGMIX-style methods common in the literature). Without these controls, it is unclear whether the improvement comes from the specific influence computation or simply from identifying that math/code data should be up-weighted — a finding that the LOO analysis (Figure 3) already suggests. Similarly, the mid-training compression (Figure 6) compares only "original" vs. "subsampled" but does not include random subsampling or perplexity-based filtering baselines.

- **Leave-one-out analysis scale is unspecified and likely mismatched.** Appendix D.3 reports LOO costs at ~400 GPU hours total (~50 per dataset), versus ~28,000 GPU hours for final pretraining — roughly a 70× compute ratio. The paper never states the model size or token budget used for these LOO experiments. If the LOO was conducted on a 140M model with a small token budget, the conclusions about dataset importance (e.g., FineWeb-Edu as "glue," StarCoder benefiting math) may not transfer to the 950M / 4.2T regime. This concern is reinforced by recent work (e.g., "Can Small Training Runs Reliably Guide Data Curation?") showing that data recipe rankings can shift with model scale and hyperparameters.

### Minor

- **No empirical link between NLL improvements and downstream accuracy.** The entire pre-training optimization pipeline (LOO analysis, influence-based mixing) is guided by NLL on capability-probing datasets. But the paper never validates that NLL reductions on these probing sets correlate with final accuracy on MATH, GSM8K, HumanEval, etc. A scatter plot across ablations would strengthen the pipeline's credibility.

- **Normalization of NLL is undefined.** Figure 3's y-axis is "normalized NLL" but the paper never specifies what normalization is applied. Equation 1 defines a raw loss difference. This makes the figures difficult to interpret precisely.

- **Data repetition is not discussed.** The model sees 4.2T tokens drawn from ~2T unique tokens, implying ~2.2T repeats. How does repeated data affect reasoning emergence? This is not discussed despite being central to the "far less data" claim.

- **Cross-influence histograms shown only for two of three domains.** Figure 5 shows influence histograms for "general knowledge" and "math" but not for "code." The code domain is critical since coding is a key benchmark where the model excels.

- **Table 2 comparison has a confound.** Baseline models use their "instruct checkpoints" with unknown prior instruction-tuning distributions, while MobileLLM-R1 uses its own Tulu-3-SFT checkpoint. The paper acknowledges this (denoted with *), but it means the comparison is not perfectly controlled — differences in prior instruction-tuning could affect reasoning SFT outcomes.

### Trivial

- "Normalized NLL" in Figure 3 is not defined in the text or caption.
- Figure 7's y-axes span different ranges (HumanEval 3.0–4.5, GSM8K 3.0–5.0), making magnitude comparison difficult.

## Nice-to-Haves

- Controlled pre-training mixture comparison: train the same 950M model from scratch using a simple heuristic mixture (e.g., up-weighting math/code by 5×) and compare to the influence-based mixture.
- Validate the cross-influence approach by computing influence scores from a single joint model (original AutoMixer protocol) and comparing the resulting mixture ratios.
- Scatter plot showing correlation between NLL on probing sets and downstream accuracy across ablations.
- Qualitative examples of model-generated reasoning chains from AIME or GSM8K.

## Removed Points

These points are flagged to be removed, treat them with caution:
- **"Abstract compares post-trained to base models"**: The harsh critic claimed AIME 15.5 vs 0.6/0.3 mixes post-trained with base models. Verified against Table 9 — ALL three are post-trained models. This criticism is factually incorrect and removed.
- **"Base model gap is smaller"**: The critic claimed "the gap is smaller (e.g., OLMo-2-1.48B has 5.2 MATH vs 26.8 for MobileLLM-R1-950M-base)." A 5.2 vs 26.8 gap (5×) is large, not small. Removed as misleading.
- **"Missing appendix/proofs"**: Parser artifact; these exist in the original submission.
- **"Missing related works"**: Cannot verify without external sources.
- **Various formatting/typo nitpicks**: Parser artifacts.
- **Generic strength claims** from Strength Finder: Some claimed strengths are generic or overlap with actual strengths listed above.

## Novel Insights

The cross-influence criticism reveals an interesting tension in this paper: the influence-based data mixing framework is presented as a principled, theoretically-grounded contribution, but the use of domain-specialized models for cross-influence computation violates the assumptions of influence function theory. However, the empirical recipe itself (Tables 5 and 6 showing what specific mixtures work at each training stage) is independently valuable and does not depend on this theoretical scaffolding. The most novel takeaway may be that the mid-training data-model co-evolution (Section 3) — which uses the model itself to iteratively compress data — is methodologically clean, demonstrably effective (Figure 6), and could be adopted independently of the pre-training mixture contribution. The overarching insight that ~2T unique tokens of carefully curated data suffice to elicit strong reasoning in sub-1B models is empirically validated and practically significant.

## Suggestions

1. **Reframe the contribution**: Either fix the cross-influence computation (compute influence from a joint model as per the original AutoMixer protocol) or substantially downgrade the "principled" claim and present the data mixture as an empirically derived recipe (which is still a valuable contribution).

2. **Add competitive baselines**: Compare against simple heuristics (uniform, 5× math/code up-weighting) for the pre-training mixture, and against random subsampling for mid-training compression.

3. **Specify LOO experiment scale**: State the model size and token budget used for LOO experiments, and discuss potential limitations in transferring conclusions to the 950M/4.2T regime.

4. **Show the NLL-to-accuracy correlation**: Provide a scatter plot linking NLL improvements on probing sets to downstream accuracy across ablations.

5. **Discuss data repetition**: Address how the 2.2T tokens of repeated data in the 4.2T budget affect the results.

## Score and Decision

**Calibration Anchors Used:**
- **TiKMiX** (avg 3.0, /home/wg25r/review_agent/human_reviews_2026/H8JAWv0HNr.md): Similar topic (influence-based data mixture optimization). TiKMiX was rejected due to unclear methodology, missing baselines, and weaker empirical results. Current paper has stronger results and a more complete recipe. **Current paper is stronger.**
- **AttentionInfluence** (avg 4.0, /home/wg25r/review_agent/human_reviews_2026/xPxoZuosIe.md): Similar (influence-based data selection). Rejected partly because results were comparable to baselines. Current paper dominates baselines by large margins. **Current paper is stronger.**
- **Unraveling Indirect ICL** (avg 4.5, /home/wg25r/review_agent/human_reviews_2026/14pg6z2RoP.md): Different domain but also uses influence functions with methodological concerns. Rejected. **Current paper has stronger empirical validation.**
- **Predicting LLM Reasoning with Small Proxy** (avg 5.5, /home/wg25r/review_agent/human_reviews_2026/JSE40ljyKm.md): Accepted as Poster despite limited scope and concerns about trace quality. **Comparable; current paper has broader contribution.**
- **DUET** (avg 6.0, /home/wg25r/review_agent/human_reviews_2026/9QpBwvTfBh.md): Data mixture optimization via BO+IF. Accepted as Poster. **Comparable; current paper has more thorough ablations.**
- **Can Small Training Runs Reliably Guide Data Curation** (avg 6.5, /home/wg25r/review_agent/human_reviews_2026/2FZC0c06jP.md): Strong theoretical+empirical paper about proxy model validity. **Current paper has less theoretical grounding.**
- **How to train data-efficient LLMs** (avg 6.8, /home/wg25r/review_agent/human_reviews_2026/yKUbw7q1IA.md): Thorough empirical study of data curation. **Comparable in thoroughness.**
- **Why Less is More** (avg 7.5, /home/wg25r/review_agent/human_reviews_2026/8KcjEygedc.md): Strong theoretical framework for data curation. **Current paper is much weaker on theory.**
- **Detecting IF Attack** (avg 2.0, /home/wg25r/review_agent/human_reviews_2026/KMFotFeGjJ.md): Different domain, weaker paper. **Current paper is substantially stronger.**

**Score rationale**: The paper has a genuine and significant methodological issue in the cross-influence computation that undermines the "principled" claim for pre-training mixture optimization. However, the empirical recipe is independently valuable, the mid-training contribution is sound, and the results (matching Qwen3-0.6B with 11.7% of tokens) are genuinely impressive. The open release is a major practical contribution. Compared to accepted anchors (DUET at 6.0, Predicting LLM Reasoning at 5.5) which were accepted despite similar-level methodological concerns, this paper sits slightly below due to the cross-influence problem being more central to a claimed contribution. Positioned between the reject-level anchors (3.0–4.5) and accept-level anchors (5.5–6.0+).

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>