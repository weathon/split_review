Now I have sufficient calibration data. Let me compile the final review.

## Round 1 Bracket

Comparing our paper against anchors:
- **Weak band (< 3.5):** Paramanu-Ganita (2.33), Don't Pre-train (3.00) — much weaker methodology, clearly below our paper
- **Middle band (3.5–7.5):** Textbooks/phi-1 (6.00), RegMix (7.20), Studying Effects of Training Data on Small LMs (5.50) — our paper sits in this range
- **Strong band (> 7.5):** DiSF (8.00), Temporal Dependence of Influence (8.00) — these are cleaner, more focused contributions

**Initial bracket: 6.0–7.2**

## Round 2 Narrowing

- **Aioli (6.25):** Data mixing optimization. Our paper has broader scope, stronger results, better validation — we are above Aioli.
- **Training Mice (6.00):** Fine-tuning study. Our paper has novel methodology and more rigorous experiments — clearly above.
- **RegMix (7.20):** Cleaner contribution, more thorough empirical validation of core method. Our paper has confounded headline comparisons that pull it down relative to RegMix.

**Final assessment:** The paper sits between Aioli (6.25) and RegMix (7.20), closer to RegMix in ambition and results but pulled down by the confounded Qwen3 comparison and unqualified benchmark-free claim. **Score: 6.5, Accept.**

---

## Summary

This paper introduces MobileLLM-R1, a series of sub-billion-parameter reasoning models trained with a data-centric framework emphasizing data quality over massive token budgets. The core contributions are: (1) a benchmark-free, influence-score-based method for optimizing pre-training data mixtures using capability-probing datasets derived from training corpora, and (2) a data-model co-evolution strategy for mid-training that iteratively filters negative-influence samples and re-weights datasets. The strongest evidence is a controlled SFT comparison (Table 2) where MobileLLM-R1 models fine-tuned on identical reasoning data as OLMo-2 and SmolLM-2 baselines substantially outperform them despite fewer parameters.

## Strengths

- **Well-designed controlled experiment isolating pre-training from post-training (Table 2):** By fine-tuning all models on an identical reasoning SFT corpus, the paper cleanly shows that pre-training and mid-training data curation—not the post-training recipe—drives the reasoning gains. MobileLLM-R1-950M achieves 57.8 MATH vs. 53.0 for OLMo-2-1.48B and 41.4 for SmolLM2-1.7B under identical SFT. This experimental design is unusually rigorous for the space and provides the paper's strongest evidence.
- **Principled influence-based data mixing methodology (Section 2.2, Figure 4):** The extension of AutoMixer to compute cross-capability influence scores between training samples and capability-probing datasets, followed by dataset-level re-weighting (Eqs. 4–5), provides a grounded alternative to heuristic mixture ratios. Figure 4 shows the resulting "Datamix" consistently lowers perplexity versus uniform sampling across Code, Math, and Knowledge benchmarks.
- **Data-model co-evolution mid-training with convergence evidence (Section 3, Figures 5–6):** The iterative process of influence-score filtering and re-weighting shows empirical convergence (influence distributions collapse toward zero/negative values), and the subsampled data avoids the pronounced performance dip seen with original mid-training data on MMLU.
- **Empirically grounded leave-one-out analysis (Section 2.1.2, Figure 3):** Training models from scratch excluding one dataset at a time reveals non-obvious cross-domain contributions—e.g., FineWeb-Edu removal causes the largest degradation across all capabilities, and StarCoder benefits math more than OpenWebMath benefits code (a reversal of the common belief from Lewkowycz et al., 2022).
- **Multi-scale validation (140M, 360M, 950M):** The methodology is demonstrated across nearly an order of magnitude in parameter count, with the 140M and 360M models showing substantial gains over SmolLM baselines, indicating the approach generalizes across sub-billion scales.

## Weaknesses

### Fatal
None.

### Major

- **The Qwen3-0.6B comparison overstates what is controlled.** The headline claim—matching Qwen3-0.6B with only 11.7% of the tokens—is repeated in the abstract (line 9), introduction (line 46), and conclusion (line 400). However, the comparison does not control for architecture, tokenizer, post-training recipe, or the fact that Qwen3-0.6B was trained as part of a larger model family on a shared 36T-token corpus (likely undertrained relative to what a dedicated 0.6B run could achieve). The 4.2T token figure also excludes post-training SFT data (3.2M reasoning samples + 866K Tulu-3 samples), while Qwen3's post-training data volume is not discussed. The paper would be stronger by either controlling for these factors or explicitly framing the result as a demonstration that curated data can close the gap rather than as a controlled efficiency comparison. The cleaner, more rigorous evidence is the identical-SFT comparison against SmolLM2 and OLMo-2 (Table 2), and the paper should center that evidence rather than the Qwen3 comparison.

### Minor

- **The "benchmark-free" claim would benefit from qualification.** The capability-probing datasets are constructed via hierarchical rejection sampling with Ask-LLM filtering that explicitly targets "reasoning relevance" for code, math, and general knowledge (Section 2.1.1). While the literal benchmark test sets are not used, the probing datasets are designed as benchmark proxies, and the Ask-LLM model used for filtering may have been trained on data overlapping with reasoning benchmarks. The paper should acknowledge that "benchmark-free" means "without direct access to test-set examples" rather than "without benchmark-relevant optimization signals."
- **No variance estimates are reported.** None of the experimental results include error bars, standard deviations, or results from multiple training runs. For small benchmarks like AIME (30 problems), a few correct answers can swing results substantially. While multiple full training runs are computationally prohibitive, at minimum the AIME and MATH results should include variance estimates across evaluation seeds or configurations.
- **LOO-to-mixture transferability is assumed rather than demonstrated.** The LOO experiments (Section 2.1.2) use equal-probability sampling of datasets, which differs from the optimized mixture used in final training. The paper does not demonstrate that LOO findings transfer to the optimized mixture regime.
- **Mid-training evaluation limited to MMLU.** Figure 6 shows mid-training improvements only on MMLU (a general-knowledge benchmark), while the paper's core claim is about reasoning. Analogous plots for math or code benchmarks during mid-training would strengthen the connection between mid-training and downstream reasoning performance.
- **Influence convergence has an undiscussed alternative explanation.** The paper interprets shrinking influence scores (Figure 5) as evidence that "the dataset's information has been largely exhausted." An alternative explanation is that the model is simply memorizing the probing distribution, causing gradients with respect to probe samples to naturally shrink over training. The paper should discuss this possibility.

### Trivial
- The "R1" naming may cause initial confusion with RL-based reasoning approaches, though the paper clearly describes its SFT-only methodology. (The critic's claim that DeepSeek-R1-Distill-Qwen-1.5B uses RL is factually incorrect—distill variants are trained via SFT on R1 outputs.)
- Model architecture is not described in the main text (deferred to the appendix); a brief summary in the main body would aid readability.

## Nice-to-Haves
- Quantify the computational cost of influence score computation relative to the training budget.
- Discuss whether the data curation recipe generalizes beyond sub-billion scales (e.g., to 3B+ models).
- Add a controlled comparison that isolates the influence-based data mixing from a baseline using the same token budget without curation (e.g., using the uniform Dolma or FineWeb-Edu mixture directly).

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"R1 framing is misleading — no RL is used" (Harsh Critic #1):** REMOVED. The paper never claims to use RL; it explicitly describes its post-training as SFT. The critic's factual claim that DeepSeek-R1-Distill-Qwen-1.5B "does use RL-based reasoning training" is incorrect—distill models are trained via SFT on R1 outputs. The naming "R1" does not imply a specific training method, and the methodology is transparently described. Retained as trivial at most.
- **"Circularity risk in influence-based optimization" (Harsh Critic #4):** REMOVED as a distinct weakness. The capability-probing datasets are small (~10K examples) evaluation sets distinct from the training data. Computing influence of training samples against a held-out probing set is standard practice analogous to using a validation set. The concern about influence convergence reflecting memorization is retained as a minor weakness (alternative explanation).
- **Parser-garbled tables (Figures 8, 9):** REMOVED. These are parser artifacts, not author errors, per the hard rules on formatting artifacts.
- **Architecture not in main text / appendix-deferred content:** DEMOTED to trivial. The appendix exists in the original submission and the paper explicitly references it (line 408). Not a substantive weakness per hard rules.
- **Generalization beyond sub-billion scales:** MOVED to nice-to-have. The paper's scope is explicitly sub-billion-parameter models (line 40–42). Demanding generalization to larger scales is scope creep.
- **Missing statistical significance as a fatal flaw:** DEMOTED to minor. Multiple full training runs are prohibitively expensive in this setting and rarely reported in the LLM training literature. A reasonable concern but not a fatal omission.
- **Generic framing strengths ("important problem," "timely question"):** REMOVED. Not concrete or verifiable strengths of this specific paper.
- **Computational cost not quantified:** MOVED to nice-to-have. Useful but not a core weakness.

## Novel Insights
None beyond the paper's own contributions. The LOO finding that StarCoder benefits math more than OpenWebMath benefits code (reversing Lewkowycz et al., 2022) is an interesting empirical observation but is presented as a side finding rather than systematically investigated.

## Suggestions
- Reframe the Qwen3 comparison more carefully, acknowledging the architectural and post-training confounds, and center the cleaner identical-SFT comparison (Table 2) against SmolLM2 and OLMo-2 as the primary evidence for token efficiency.
- Qualify the "benchmark-free" claim to acknowledge that capability-probing datasets are designed as benchmark proxies, and that the Ask-LLM filter introduces indirect benchmark-relevant signals.
- Add variance estimates for at least the AIME and MATH results, either through multiple evaluation seeds or bootstrap resampling.
- Discuss the alternative explanation for influence convergence (memorization of probing distribution rather than data exhaustion).
- Briefly describe the model architecture in the main text (e.g., transformer variant, layers, hidden dimension, attention type, tokenizer, context length).

## Anchor Comparison

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Paramanu-Ganita | 2.33 | 1 (weak) | Much weaker methodology; our paper is far above |
| Don't Pre-train, Teach Your Small Model | 3.00 | 1 (weak) | Different approach, less rigorous; our paper above |
| Textbooks Are All You Need (phi-1) | 6.00 | 1 (middle) | Our paper has more rigorous methodology, multi-domain evaluation, cleaner experiments |
| RegMix | 7.20 | 1 (middle) | RegMix has a cleaner, more self-contained contribution; our paper has broader scope but confounded headline comparison |
| Studying Effects of Training Data on Small LMs | 5.50 | 1 (middle) | Less ambitious; our paper clearly above |
| Aioli | 6.25 | 2 (narrow) | Our paper has broader scope, stronger results, better validation |
| Training Mice to Compete with Elephants | 6.00 | 2 (narrow) | Our paper has novel methodology and more rigorous experiments; clearly above |
| MiniPLM | 6.40 | 2 (narrow) | Different approach (KD); comparable quality but our paper more novel |

**Round 1 bracket: 6.0–7.2.** Round 2 narrowed to **6.25–7.0**. Final score of **6.5** reflects the paper's genuinely strong methodology and controlled experimentation, tempered by a confounded headline comparison and an unqualified benchmark-free claim.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>