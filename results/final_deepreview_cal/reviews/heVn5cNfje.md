Now let me write the full consolidated review.

## Summary

The paper proposes High-Entropy Sum (HES), a simple, training-free metric that computes the sum of token-level entropy for only the top 0.5% highest-entropy tokens in a reasoning sample, focusing on critical "forking points." HES is validated as a data selection tool across SFT, RFT, and RL training paradigms. The core finding is that HES-based selection in SFT allows training on only 20% of data to match full-dataset performance, while pruning the lowest-HES 20% consistently improves over the full dataset.

## Strengths

1. **Strong and consistent SFT results across models, datasets, and domains.** Tables 1–4 show that training on the top 20% of HES-ranked data closely matches full-dataset performance (e.g., 31.14% vs 32.61% avg on Qwen3-8B), and training on the top 80% (pruning the bottom 20%) surpasses it (35.36% vs 32.61%). This holds across Qwen3-8B, DeepSeek-R1-distilled-7B, and across math, code, and STEM domains. The Lowest-HES-20% baseline achieves only 14.90%, confirming that HES identifies genuinely harmful data.

2. **HES consistently outperforms existing training-free selection metrics.** In SFT, Highest-HES 20% (31.14%) beats the next-best training-free baselines (Highest-ES 30.92%, Length 30.67%, Highest-Difficulty 29.88%). In RFT, HES beats random, length, and difficulty baselines in both per-query and global-pool settings across all k values.

3. **Small-to-large model transfer is demonstrated.** Using a tiny 0.6B model to compute HES and select data for an 8B model yields 32.12% average — comparable to the 8B's self-selection (31.14%) — substantially reducing inference cost. This shows HES captures intrinsic properties of the data rather than model-specific artifacts.

4. **HES generalizes beyond math to code and STEM domains.** Tables 3–4 show HES selection yielding 39.54% (vs Fullset 36.28%) on Code and 49.56% (vs Fullset 44.42%) on STEM, confirming the metric captures reasoning quality signals common across logic-intensive tasks.

5. **Sensitivity analysis confirms robustness.** Experiments across four high-entropy token ratios (0.005, 0.05, 0.5, 1.0) show that the smallest ratio (0.005) consistently delivers the best performance, and the benefit of HES-based selection is stable across different data selection ratios.

## Weaknesses

### Major

1. **RL experiments are too weak to support the paper's unified claim.** The paper claims HES provides a "unified" framework across SFT, RFT, and RL, but the RL evidence is unconvincing. The best HES strategy (Pos-High, Neg-Rand) achieves 21.30% vs Full-Batch's 20.63% — a 0.67-point gain on a 1.5B model trained for only 628 steps. On HMMT25, this strategy scores *lower* (11.88%) than Full-Batch (15.21%). The paper reports no variance or statistical significance. The paper positions HES as surpassing "existing training-free selection methods" in RL, but the comparison set is limited (only difficulty and length), and the closest non-HES baseline (Pos-Difficulty, Neg-Rand at 20.27%) is only 1.03 points behind. The absolute accuracy levels (Full-Batch AIME24 at 33.33%) suggest the RL setup is not operating at standard performance levels, making the generalizability of the claimed improvements uncertain.

2. **The relationship between HES and "quality" is under-explained.** Figure 1 shows incorrect responses have substantially *higher* mean HES (0.68) than correct responses (0.29). This is a critical point: if HES is a measure of "quality" or "learning value," why do incorrect samples score higher? The paper says HES captures "diversity and complexity of reasoning patterns," which is a plausible explanation — incorrect samples exhibit confused/conflicting reasoning (high complexity, wrong), while among correct samples, higher complexity means better learning. However, the paper never explicitly reconciles this tension. The reader is left to infer that HES is applied only to correct/filtered samples in practice (RFT and RL explicitly filter for correctness first; SFT uses correct demonstrations), but the paper's conceptual framing conflates "quality" (correctness-linked) with "complexity" (uncorrelated with correctness). A controlled analysis showing how HES ranks correct solutions and why high-HES correct solutions are better would significantly strengthen the paper's internal coherence.

### Minor

3. **No variance or statistical significance reported anywhere.** All results are reported as point estimates (average pass@1 over 16 samples) without confidence intervals, standard deviations, or significance tests. Given that the RFT improvements are +0.97 to +1.69 points on average, and individual benchmarks sometimes show random outperforming HES (AIME25 k=4 global: Random 38.13 vs HES 33.13; GPQA k=2 per-query: Random 40.50 vs HES 40.30), the reader cannot assess whether the reported gains are robust or within the noise. This is a standard reporting expectation for empirical ML papers.

4. **RFT gains are modest and inconsistently positive at the per-benchmark level.** While HES consistently beats random on average across settings, individual benchmarks show small or negative margins. For k=2 per-query, the average gap over random is +1.01 points, but on AIME25 it's essentially zero (34.58 vs 34.17) and on GPQA it's negative (40.30 vs 40.50). The per-query vs global pool analysis is interesting, but the paper's claim of "significantly superior" performance is not supported by the raw numbers.

5. **No computational cost analysis is provided despite efficiency claims.** The paper repeatedly describes HES as "training-free" and "efficient," but computing token-level entropy requires a full forward pass of the model over each candidate response. For long CoT sequences (up to 32k tokens), this cost is non-trivial. No wall-clock time, FLOPs, or cost comparison against baselines (length, difficulty) is reported, leaving the efficiency claim unsubstantiated.

### Trivial

6. Table 1 row labels are slightly confusing: "Highest-HES (0.6B)" in the table refers to a transfer experiment using a 0.6B proxy model, but this is not entirely clear from the table alone without reading the caption and text.

## Nice-to-Haves

- The sensitivity analysis on the high-entropy token ratio could be extended. Only four values (0.005, 0.05, 0.5, 1.0) are tested; a finer-grained sweep (e.g., 0.001, 0.005, 0.01, 0.05, 0.1) would better establish the optimal range.
- A qualitative analysis showing examples of high-HES vs low-HES correct solutions, with the high-entropy tokens highlighted, would make the mechanism more concrete and help validate the "forking point" intuition.
- The per-query vs global pool comparison in RFT is confounded by coverage: per-query guarantees every query appears, while global pool may drop some queries entirely. A controlled experiment matching coverage would isolate the effect of HES from coverage effects.
- The Forking-Only baseline (gradient masking on high-entropy tokens) deserves a more detailed description in the main text rather than just a citation.

## Removed Points

These points were identified by the reviewers but are either inaccurate, speculative, or nitpicks that do not affect the paper's core evaluation:

- **"The Forking-Only baseline is underspecified"** — This is an implementation detail of a baseline drawn from another paper. The interested reader can consult the cited work.
- **"Only three token ratios tested (should test 0.001, 0.01)"** — Four ratios are tested (0.005, 0.05, 0.5, 1.0), and the paper already shows a clear trend with 0.005 being optimal. A finer sweep would strengthen but is not necessary.
- **"The threshold might interact with model size/domain"** — The sensitivity analysis already tests across math, code, and STEM domains (Figures 3–4). This criticism is factually incorrect.
- **"Confusing formatting in Table 1"** — Minor presentation issue, clarified by the table caption and surrounding text.
- Several strengths from the Strength Finder were too generic or overstated: e.g., "HES provides a single metric that improves training across all three paradigms" overstates the RL evidence and is weakened above.

## Novel Insights

None beyond the paper's own contributions. The core insight — that summing the entropy of only the highest-entropy tokens produces a more discriminative signal than averaging across all tokens — is well-motivated and verified. However, the observation that this metric is most effective when applied among correct samples (not across the full distribution) is something the paper hints at but does not fully develop into an analysis.

## Suggestions

1. **Strengthen the RL section or rescope claims.** Either scale up the RL training (longer training, larger model like 7B) to produce convincing evidence, or rescope the paper's claims to "SFT and RFT" where the evidence is solid. A paper with strong SFT+ RFT results is still a meaningful contribution without the unified framing.

2. **Add statistical significance throughout.** Report confidence intervals (e.g., bootstrap over the 16 samples) for at least the key comparisons (Highest-HES vs Random in SFT and RFT). This is essential for assessing whether the modest RFT gains are robust.

3. **Explicitly address the HES-quality relationship.** Add a paragraph discussing why incorrect samples have higher HES but HES still selects good training data among correct samples. A simple analysis showing within-correct ranking behavior would clarify the mechanism.

4. **Report computational cost.** Even a rough estimate (e.g., "computing HES for a 10k-sample dataset takes X GPU-hours, which is Y% of the training cost") would substantiate the efficiency claims.

5. **Add a controlled RFT experiment** that matches query coverage between per-query and global pool settings to isolate the effect of HES quality from coverage effects.

## Score and Decision

### Calibration Details

**Round 1 (Bracketing):**
- Weak anchors (score <3.5): z3DMFpaP6m (3.0), OdoS6cH8MP (2.0), EOPLy80bBm (3.0), g4VGwNqzpB (3.0) — Rejected papers on data selection/entropy, clearly inferior to HES paper.
- Middle anchors (3.5-7.5): Fty0wTcemV/DELIFT (6.0, Accept), qUJsX3XMBH (4.4, Reject), gdzpnRBP4F (4.5, Reject), uO0itv7XFa (4.67, Reject) — Relevant comparison papers.
- Strong anchors (>7.5): f4gF6AIHRy (8.0), WbWtOYIzIK (8.0), UHPnqSTBPO (8.0), GGlpykXDCa (8.0) — Top-tier papers well above the HES paper.

**Round 1 bracket:** 5.0–6.5

**Round 2 (Narrowing):**
- ouRX6A8RQJ/Understanding CoT through Information Theory (6.4, Reject) — Similar information-theoretic framing but more theoretical and less applied. HES paper is more practical but less rigorous.
- I5p1Gm8GFS/3DS (5.75, Reject) — Data selection for medical domain. HES paper is broader but 3DS has cleaner evaluation. HES paper is slightly stronger.
- FAfxvdv1Dy/STAFF (6.5, Accept) — Coreset selection using speculative scoring. Stronger methodology and clearer results than HES paper.
- BTKAeLqLMw/DEITA (6.33, Accept) — Data selection for alignment with GPT-4-based scoring. Stronger evaluation but narrower scope. HES paper is comparable in quality but weaker in RL.

**Comparison to Fty0wTcemV/DELIFT (6.0, Accept):** DELIFT shares the closest scope — data selection across multiple training stages. Both papers propose a metric and validate across three settings. DELIFT's method is more complex (submodular functions on pairwise utility) while HES is simpler. The HES paper has stronger SFT evidence (matching full-dataset with 20% data, surpassing with 80%) than DELIFT shows for its settings. However, DELIFT is more methodologically rigorous. On balance, the HES paper is slightly below DELIFT due to weak RL evidence and lack of significance testing.

**Final score:** 5.5

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>