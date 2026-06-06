Now I have a thorough reading of the paper. Let me write the draft review and submit it before calibration searches.Now let me run the 5 calibration searches across all bands simultaneously:Let me read the most topically comparable papers more carefully:Now I have enough to select anchors and finalize the review. Based on the calibration search:

- **GtpubstM1D** (5.71): most topically comparable — CPT vs SFT data for math reasoning, training stages comparison
- **1hQKHHUsMx** (6.75): pretraining data effects on LLM reasoning, related question
- **3OyaXFQuDl** (7.00): quality vs diversity trade-off in LLM training data, compute-budget framing
- **Eo7kv0sllr** (6.50): decoupling pretraining knowledge from fine-tuning knowledge in LLMs

---

## Summary
This paper presents the first systematic empirical study of how reasoning data — varying in scale, diversity, and quality — should be allocated between pretraining and supervised fine-tuning (SFT) to maximize LLM reasoning performance. Using four 8B-parameter hybrid models each pretrained from scratch on 1T tokens under a fixed 80B-token reasoning budget, the authors demonstrate an asymmetric principle: pretraining benefits most from diverse, large-scale data, while SFT performance is governed by data quality. Key contributions include empirical refutation of the "catch-up" hypothesis, the discovery of a latent effect of high-quality pretraining data that only manifests after SFT, and quantitative evidence that naive SFT data scaling with mixed-quality data actively harms math performance.

---

## Strengths

- **Large-scale, fully controlled pretraining experiments**: Four complete 1T-token pretraining runs with carefully varied reasoning data configurations (D_LDQ: 268M diverse samples; D_SHQ: 1.2M high-quality samples; D_LMQ: combined; M_base: none), all under the same 80B reasoning token budget in the final 400B tokens. This experimental scale is rarely achieved in academic work and enables unusually clean between-condition comparisons.

- **Asymmetric principle supported across multiple evaluation stages**: Table 1 shows M_LDQ outperforming M_SHQ by +9.09% at pretraining; Table 5 shows the reversal — M_res + SFT_SHQ outperforms M_res + SFT_LDQ by 13.45%. The asymmetry is consistent across base, SFT, and RL stages, and survives through Tables 1–8.

- **Empirical refutation of the "catch-up" hypothesis with concrete numbers**: Doubling SFT epochs for M_base still leaves it 3.32% below the weakest reasoning-pretrained model M_SHQ (Table 4: 34.01 vs. 37.33), and 16.94% below M_LMQ. The widening gap at the RL stage (M_LMQ + SFT_SHQ + RL: 56.66% vs. M_base + SFT_SHQ + RL: 37.92%, Table 3) is a striking, practically relevant finding.

- **Novel latent effect discovery**: M_LMQ and M_LDQ are statistically indistinguishable at the end of pretraining (64.07 vs. 64.09, Table 1), yet M_LMQ jumps to +4.25% after SFT with D_SHQ (50.95 vs. 46.70, Table 4). This non-obvious finding suggests that high-quality pretraining traces modify internal representations in ways that amplify SFT receptiveness, rather than improving intrinsic capability directly.

- **Quantified harm of naive SFT data scaling**: Table 8 shows 2× D_LDQ during SFT yields −4.92% math regression with negligible overall gain, while 0.4% additional high-quality data (D_ALF*) consistently improves performance. The contrast is stark and actionable.

- **Broad multi-domain evaluation spanning all three training phases**: Unlike prior mid-training work that focuses narrowly on mathematics, the evaluation covers math, science, code, and instruction-following across pretraining, SFT, and RL stages, strengthening the generalizability claim.

---

## Weaknesses

### Fatal
None.

### Major

- **Budget equivalence constraint (Equation 2) is stated but not enforced in the key "catch-up" experiment**: The paper frames the problem with an explicit budget constraint B = |D_res^PT| + |D_res^SFT| (Eq. 2), implying that a fair comparison would hold total reasoning tokens constant while shifting between stages. However, the catch-up experiment (Table 4) gives M_base 2× SFT epochs (approximately doubling SFT samples, perhaps ~9.6M), while the reasoning-pretrained models received 80B pretraining reasoning tokens *plus* 4.8M SFT samples — a vastly higher total reasoning token count. The paper correctly shows that SFT cannot catch up under this condition, but the conclusion "pretraining instills a foundational reasoning capability that cannot be fully replicated by simply scaling the SFT phase" is established only under a condition that is strongly biased toward the pretraining group. A genuinely budget-controlled test (reallocate ~80B reasoning tokens from pretraining to SFT) would either make the central claim bulletproof or require important nuance.

- **Repetition confound in the pretraining quality-vs-diversity comparison**: Section 2.3 states "when a reasoning dataset is small, it is repeated so that the model still observes the same total volume of reasoning tokens." D_SHQ has 1.2M samples; at ~2,000 tokens/sample this is ~2.4B tokens, requiring roughly 33× repetition to fill 80B pretraining tokens. D_LDQ with 268M samples fills 80B tokens with near-zero repetition. The paper attributes M_SHQ's −9.09% lag behind M_LDQ (Table 1) to quality vs. diversity, but repeated training on identical examples is a known source of performance degradation independent of data quality. The confound is acknowledged as an implementation detail in Section 2.3, but its contribution to the quality–diversity gap is neither analyzed nor bounded. This is the paper's most prominent conclusion and the one most affected by this design ambiguity.

### Minor

- **Absence of confidence intervals on key small effect-size claims**: The paper reports averaging over 16 runs for AIME and 4 runs for other benchmarks, which helps but is not sufficient in isolation. The latent effect finding rests on a +4.25% gap between M_LMQ and M_LDQ after SFT (Table 4), and the catch-up residual gap is 3.32% (Table 4). On volatile benchmarks like AIME (pass@1 in the 10–45% range), these differences may or may not be statistically reliable. Error bars or standard deviations on all main tables, particularly the AIME-based averages, are needed for the reader to assess which specific effect-size claims are robust.

- **RL phase evaluates only two extreme models**: Table 3 compares only M_LMQ + SFT_SHQ vs. M_base + SFT_SHQ. The claim that "pretraining strategy dictates the final accuracy ceiling" is drawn from a two-point comparison. Whether the pretraining-quality → post-RL advantage is monotonic (e.g., does M_SHQ or M_LDQ sit between the two endpoints?) is unknown. Including the intermediate models would convert a two-point claim into a proper trend.

### Trivial

- **Imprecise "average gain" framing in the abstract**: The "19% average gain" refers to the M_LMQ + SFT_SHQ + RL vs. M_base + SFT_SHQ + RL difference (Table 3: 56.66 − 37.92 = 18.74%), which is a single pairwise comparison, not an average across multiple conditions. Similarly, "11% average gain" for diversity compares M_LDQ to M_SHQ. Calling these "average gains" slightly overstates the breadth of evidence for each headline number.

---

## Nice-to-Haves
- A budget-controlled version of the catch-up experiment — hold total reasoning tokens constant and shift 80B tokens from pretraining to SFT — would convert Equation 2 from motivating framing into verified claim. Either outcome (gap persists or closes) would be highly informative.
- Error bars or standard deviations for all main tables, especially for AIME results, to allow readers to assess which specific effect-size claims are statistically reliable.
- Inclusion of M_LDQ and M_SHQ in the RL phase comparison (Table 3) to characterize whether the pretraining-to-RL performance relationship is monotonic.
- Brief main-text mention of the 1.2B Transformer experiment (currently Table 14 in the appendix) to strengthen the claim that the asymmetric principle generalizes beyond the specific hybrid 8B architecture.

---

## Removed Points
*These points are flagged as removed; treat them with caution.*

- **Harsh Critic: Reasoning schedule design (injection only in final 400B vs. uniform across 1T)**: Removed. The scheduling choice is reasonable and its impact on qualitative conclusions is speculative. The 80/20 ratio in the final 400B is a design choice with sensible motivation (controlled injection); criticizing its absence of alternatives is scope creep.

- **Harsh Critic: Related work characterization as unfair because the paper's own RL results are "math-centric"**: Removed. The paper evaluates 8 benchmarks across math, science, code, and instruction following. The AIME headline is prominent, but the paper is not appropriately characterized as "math-centric."

- **Harsh Critic: D_LMQ's framing as "balanced diversity with quality"**: Kept only as Trivial. The paper later corrects the impression when discussing the latent effect; this is a minor presentation issue, not an evidential flaw.

- **Harsh Critic: Table 5 SFT repetition confound (D_SHQ ~4× repetition in SFT)**: Merged into the Major repetition confound weakness above; this is the same issue in the SFT phase.

- **Strength Finder: "Controlled experimental design with fixed budget"**: Kept in Strengths but scoped to the within-phase fixed budget, which is real. The cross-phase budget constraint (Eq. 2) is addressed as a Major weakness.

---

## Novel Insights
The paper's most non-obvious finding is the latent effect: high-quality pretraining data (D_SHQ embedded in D_LMQ) leaves no measurable trace at the end of pretraining (M_LMQ: 64.07 vs. M_LDQ: 64.09, Table 1), yet reveals a +4.25% post-SFT advantage (M_LMQ: 50.95 vs. M_LDQ: 46.70, Table 4). This suggests that high-quality reasoning traces may not improve the model's evaluable capabilities during pretraining, but instead alter internal representations in ways that enhance receptiveness to alignment signals — a form of pretraining–SFT coupling not previously documented at this scale. Combined with the finding that naive SFT scaling with diverse data actively erodes math performance (−4.92%, Table 8), the paper collectively establishes that each training phase has distinct and phase-specific sensitivity to data quality, and that these sensitivities interact across phases in non-additive ways. This phase-dependent sensitivity framework is the paper's most broadly applicable intellectual contribution.

---

## Suggestions
- Run a budget-controlled experiment: give M_base approximately 80B SFT tokens (matching the pretraining reasoning budget) using D_SHQ. If the gap persists under equal total reasoning token budgets, the catch-up claim becomes unambiguous. If the gap closes, the paper should reframe the central claim from "SFT cannot compensate" to "SFT requires proportionally equivalent investment."
- Report standard deviation across runs for all main table results. Even a footnote noting SD ranges would allow readers to assess which findings (especially the +4.25% latent effect) are statistically reliable.
- Extend Table 3 to include M_LDQ and M_SHQ after RL to test whether the pretraining quality → post-RL performance relationship is monotonic.
- Analyze whether the latent effect is consistent across individual benchmarks or concentrated in specific domains, to begin characterizing the mechanism.

---

## Score and Decision

**Evaluation on key axes:**
- **Originality**: High. First systematic study of reasoning data allocation across the full pretraining–SFT–RL pipeline at this scale. The latent effect is a genuinely novel observation.
- **Importance of research question**: High. With pretraining costs growing, understanding when to inject reasoning data is practically critical and scientifically fundamental.
- **Whether claims are well-supported**: Moderate. Core findings (pretraining with reasoning helps; diversity before quality; naive SFT scaling harms) are well-supported across multiple tables. Specific quantitative claims (latent effect magnitude, catch-up impossibility) are weakened by the budget constraint and repetition confound.
- **Soundness of experiments**: Moderate-to-good. The pretraining design is careful, but the catch-up test has the budget mismatch issue and the quality-vs-diversity comparison has the repetition confound.
- **Clarity of writing**: Good. The paper is well-structured and the findings are clearly communicated.
- **Value to the research community**: High. The asymmetric principle and latent effect finding provide actionable, practically relevant guidance at a level of detail the community currently lacks.

The paper is comparable in scope and methodology to GtpubstM1D (5.71 avg), which asks a similar question (problem-solving data in CPT vs. SFT for math) but is more narrowly scoped (math only, CPT not full pretraining from scratch). The paper under review is broader in domain, more computationally expensive, covers more training phases, and has more novel findings — which pushes it above 5.71. However, the budget constraint mismatch in the central "catch-up" test and the unanalyzed repetition confound prevent it from reaching 7.0 (where 3OyaXFQuDl sits with cleaner budget-controlled methodology and a stronger latent mechanism story). Score: **6.0**.

# Selected Anchors

<related>["GtpubstM1D", "1hQKHHUsMx", "3OyaXFQuDl", "Eo7kv0sllr"]</related>

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>