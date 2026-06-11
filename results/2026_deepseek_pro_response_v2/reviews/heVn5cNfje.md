Now I have a clear picture for calibration. Let me synthesize and produce the final review.

**Anchor comparison summary:**

| Anchor | Score | Comparison to HES paper |
|--------|-------|------------------------|
| EOPLy80bBm (Data Pruning survey) | 3.00 | HES paper is clearly stronger — proposes a novel method with broad validation |
| qUJsX3XMBH (Random Selection) | 4.40 | HES paper is stronger — demonstrates a method that consistently beats random and full-dataset |
| I5p1Gm8GFS (3DS Medical) | 5.75 | HES paper is comparable or slightly stronger — broader domain and paradigm coverage |
| Fty0wTcemV (DELIFT) | 6.00 | Comparable — both propose lightweight selection metrics; HES has broader validation, DELIFT has stronger theoretical framing |
| BTKAeLqLMw (DEITA) | 6.33 | DEITA is somewhat stronger — more sophisticated method, deeper analysis of data dimensions |
| FAfxvdv1Dy (STAFF) | 6.50 | STAFF is somewhat stronger — more methodologically novel speculative selection approach |
| f4gF6AIHRy (Submodular File Selection) | 8.00 | Clearly stronger — more theoretically grounded, accepted with all 8s |

**Bracket:** 5.5 – 6.5. The paper sits near DELIFT (6.0) — comparable novelty, broader but somewhat noisier empirical validation. The three Major weaknesses (Figure 1 tension, unspecified model, missing perplexity) keep it from the 6.33+ tier. **Final score: 6.0, Decision: Accept.**

---

## Summary
This paper proposes High-Entropy Sum (HES), a training-free metric that ranks reasoning samples by summing the entropy of only the top 0.5% highest-entropy tokens, motivated by the idea that these rare "forking tokens" capture reasoning complexity. The method is validated across three training paradigms — SFT, RFT, and RL — with the strongest result being that pruning the bottom 20% of data by HES consistently outperforms training on the full dataset across four model/dataset/domain configurations.

## Strengths
- **Broad, multi-paradigm validation with consistent results**: HES is tested in SFT (Tables 1–4, covering math, code, and STEM), RFT (Table 5, 8 configurations across per-query and global-pool settings), and RL (Table 6). Across all four SFT setups, HES-80% (discarding the bottom 20%) surpasses full-dataset training — a replicated, cross-domain finding that strongly supports the claim that HES identifies genuinely harmful low-quality samples.
- **Comprehensive ablation design**: Table 1 alone compares HES against 11 alternatives (Random, Difficulty-High, Difficulty-Medium, Length, Forking-Only, AvgE, AvgHE, ES, HES_absolute, Lowest-HES), isolating the contribution of the relative-threshold formulation. This density of comparison is rare and valuable.
- **Strong negative control validates the metric**: Training on Lowest-HES-20% produces dramatically degraded results across all tables (14.90 vs. 25.89 Random in Table 1; 20.78 vs. 30.38 in Table 2; 13.39 vs. 27.83 in RFT Table 5), establishing a clear monotonic relationship between HES ranking and downstream training utility.
- **Practical small-to-large model transfer**: Using Qwen3-0.6B as a proxy to rank data for Qwen3-8B training achieves 32.12% average accuracy, comparable to 8B self-selection at 31.14% (Table 1), demonstrating that HES signals transfer across model scales and enabling cost-efficient data curation.
- **Method simplicity**: HES requires only forward passes to compute token-level entropy, with no auxiliary models, reward signals, or training — making it readily adoptable.

## Weaknesses

### Fatal
None.

### Major
- **Unresolved tension between Figure 1 and the selection logic**: Figure 1, the paper's central motivating evidence, shows that incorrect samples have *dramatically higher* HES than correct samples (normalized means: 0.68 vs. 0.29). Yet the paper selects *highest*-HES samples for training, and the theoretical motivation (line 115) claims high HES reflects "successful navigation of more numerous and intense forks." If high HES signals quality, why do incorrect samples score higher? The paper works around this by correctness-filtering data in all paradigms (SFT uses only correct demonstrations; RFT and RL filter to successful trajectories first), but it never acknowledges or reconciles this conceptual contradiction. This leaves unclear whether HES measures reasoning competence or merely confused exploration, and it undermines the theoretical framing.
- **Model used to compute HES is unspecified**: Token entropy requires running inference through a language model, but the paper never states which model computes HES for the main SFT experiments (Tables 1–4). Figure 1 uses Qwen3-14B, and the small-to-large transfer experiment (line 216) implies 8B self-selection — but this critical detail is never made explicit. This affects both reproducibility and the "training-free" characterization, since the choice of model materially affects entropy values.
- **Missing perplexity baseline**: Perplexity is a standard data selection metric discussed in the paper's own introduction (line 17) and related work (line 389), and is closely related to the ES baseline that is tested. Its absence weakens the claim that HES is "superior to all baselines" (line 159), since perplexity (cross-entropy with ground-truth tokens) captures a different signal than sampling-time entropy and is the most natural lightweight competitor.

### Minor
- **Small margins without variance reporting**: Key comparisons have narrow gaps — HES vs. ES: 31.14 vs. 30.92 (0.22 points, Table 1); HES vs. Length in RFT k=8: 31.13 vs. 30.67 (0.46 points, Table 5); Pos-High/Neg-Rand vs. Full-Batch in RL: 21.30 vs. 20.63 (0.67 points, Table 6). No confidence intervals or multi-seed variance is reported for any experiment, making it difficult to assess whether these differences are statistically meaningful.
- **Abstract overstates one result**: The abstract claims "training on just the top 20% of data ranked by HES matches full-dataset performance," but in Table 1 (the primary SFT result), HES-20% (31.14) trails Full-Dataset (32.61) by 1.47 points. The claim holds in Tables 2–4 but not for the main table.
- **Length baseline is competitive in RFT**: In per-query k=8, Length (30.67) trails HES (31.13) by only 0.46; in global pool k=8, Length (30.45) trails HES (31.07) by 0.62 (Table 5). The paper does not include a length-controlled analysis to disentangle how much of HES's signal derives from preferring longer, more elaborate responses rather than from specifically identifying forking tokens.
- **Sensitivity analysis Figure 4 shows identical values across all ratios**: MMLU STEM and LiveCodeBench report identical average scores (0.855 and 0.544) across all four high-entropy token ratios, which suggests either a reporting issue or that these benchmarks are insensitive to the metric — either case warrants explanation.

### Trivial
- Related work in the main text is limited to two paragraphs, with fuller discussion deferred to the appendix.
- The "Forking-Only" baseline (Table 1, 32.51 at 100% data, very close to Full-Dataset at 32.61) is a strong and directly relevant baseline but receives minimal discussion.
- Difficulty-based baselines (Highest-Difficulty at 29.88, Medium-Difficulty at 23.29 in Table 1) produce notably poor results that go undiscussed.

## Nice-to-Haves
- Qualitative examples of high-HES correct vs. high-HES incorrect reasoning samples would help readers develop intuition for what HES captures and would partially address the Figure 1 tension.
- A length-controlled experiment (bucketing by response length, then selecting top-HES within each bucket) would clarify HES's signal beyond response length.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"HES does not actually measure what it claims to measure — Figure 1 falsifies the theory" (Harsh Critic structural/fatal claim)**: The Harsh Critic argued the Figure 1 tension is fatal. However, the paper consistently applies HES only within correctness-filtered pools, and Figure 1 does demonstrate discriminative power (the paper's explicit claim about Figure 1). The tension is real (kept as Major) but does not invalidate the method's empirical utility.
- **"The RL strategy description is inconsistent with Table 6"**: Line 137 description ("select half with the highest HES from the pool of successful trajectories") is fully consistent with the Pos-High/Neg-Rand strategy in Table 6. No inconsistency exists.
- **"No comparison with influence functions or gradient-based data selection"**: These are computationally expensive methods in a fundamentally different class from lightweight metrics like HES. Demanding their inclusion is scope creep.
- **"Garbled tables / formatting artifacts"**: Parser issues, not author errors. The original submission does not have these problems.
- **"Cannot evaluate appendix claims"**: The parser strips the appendix from all papers. This is not an author error.
- **"Highest-Difficulty baseline result (29.88) is below Random-20% (25.89)" — factual error**: The Harsh Critic stated 29.88 is "noticeably below" 25.89, which is incorrect (29.88 > 25.89). Removed as factually wrong.

## Novel Insights
The most interesting emergent insight from the RL experiments is the asymmetry between positive and negative sample selection: HES-guided positive selection helps (Pos-High, Neg-Rand > Full-Batch), but HES-guided negative selection hurts (Pos-Rand, Neg-Low < Pos-Rand, Neg-Rand). This suggests HES captures something about reasoning *competence* (useful for selecting positive examples to learn from) rather than error *informativeness* (for which diversity matters more). The paper notes this pattern but does not develop it into a theoretical claim; doing so would strengthen the contribution.

## Suggestions
- Explicitly state which model was used to compute token-level entropy for each experiment table — this is a reproducibility requirement, not a nice-to-have.
- Add a perplexity baseline to at least one experiment table to substantiate the claim of superiority over existing lightweight metrics.
- Reconcile the Figure 1 tension: either reframe the theoretical motivation to acknowledge that HES captures a signal whose direction differs for correct vs. incorrect samples (e.g., high-HES incorrect = confused exploration, high-HES correct = complex successful reasoning), or provide a principled explanation for why high-HES correct samples are better training data despite incorrect samples exhibiting even higher HES.
- Report standard deviation across at least 2–3 training seeds for the closest comparisons (HES vs. ES, RL Pos-High vs. Full-Batch) so readers can assess whether differences are meaningful.

## Score and Decision

**Round 1 bracket:** 5.0 – 7.0 (based on weak anchor EOPLy80bBm at 3.0 being clearly weaker, middle anchors qUJsX3XMBH at 4.40 being weaker, and strong anchor f4gF6AIHRy at 8.00 being clearly stronger).

**Round 2 narrowing:** Compared against DELIFT (6.00), DEITA (6.33), and STAFF (6.50). The HES paper is comparable to DELIFT in novelty and validation breadth, somewhat below DEITA in methodological sophistication and depth of analysis, and below STAFF in novelty of approach. The three Major weaknesses (Figure 1 tension, unspecified model, missing perplexity baseline) prevent a score in the 6.5+ tier.

**Final score: 6.0 — Accept.**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>