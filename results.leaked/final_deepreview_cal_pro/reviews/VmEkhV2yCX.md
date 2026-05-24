Now I have a thorough understanding of both the paper and the calibration anchors. Let me write the final consolidated review.

---

## Summary

This paper conducts the first systematic study of how reasoning data — varying in scale, diversity, and quality — should be allocated between pretraining and supervised fine-tuning (SFT) of LLMs. The authors pretrain four 8B-parameter models from scratch for 1T tokens under a fixed reasoning-token budget (80B tokens), then evaluate them through SFT and reinforcement learning (RL) across math, science, code, and instruction-following benchmarks. The central findings are: (1) front-loading reasoning data into pretraining creates a durable advantage that SFT alone cannot recover; (2) an asymmetric principle where diversity and scale drive pretraining gains while quality dominates SFT; (3) high-quality pretraining data has latent benefits unlocked only after SFT; and (4) naïve SFT scaling with mixed-quality data harms reasoning.

## Strengths

- **Controlled large-scale experimental design.** All models are pretrained from scratch for 1T tokens, with every reasoning-injected model receiving exactly 80B reasoning tokens (Section 2.3). This fixed token budget enables clean isolation of the effect of reasoning data composition at the pretraining stage, which is rare in the literature given the computational cost.

- **Empirical refutation of the "catch-up" hypothesis.** Table 4 provides compelling evidence: doubling the SFT data for the baseline model (M_base + SFT_SHQ 2× epochs = 34.01 avg) still fails to match the weakest reasoning-pretrained model (M_SHQ + SFT_SHQ = 37.33 avg). This directly demonstrates that post-training alone cannot compensate for the absence of reasoning data during pretraining.

- **Discovery of the asymmetric principle with convergent evidence.** Tables 1 and 5 together reveal a phase-dependent pattern: large, diverse pretraining data (M_LDQ) yields a substantial +9.09 avg gain over small, high-quality pretraining data (M_SHQ) at the base model stage, yet fine-tuning on that same large, diverse data during SFT degrades reasoning compared to high-quality SFT (Table 5). This provides an actionable, evidence-backed heuristic for data allocation across training phases.

- **Latent effect of high-quality pretraining data.** M_LMQ and M_LDQ show near-identical pretraining averages (64.07 vs 64.09 in Table 1), but after identical high-quality SFT, M_LMQ achieves a +4.25 avg gain over M_LDQ (Table 4), revealing that quality in pretraining creates dormant capabilities activated only by alignment — a surprising and practically significant finding.

- **Demonstration that naïve SFT scaling harms reasoning.** Table 8 shows that doubling mixed-quality SFT data causes a 4.92-point drop in math reasoning, while a marginal (0.4%) injection of high-quality data yields consistent improvement — a clear warning against quantity-driven SFT expansion.

- **Multi-domain, multi-phase evaluation.** Benchmarks span math, science, code, and instruction-following across base, SFT, and RL stages, providing a holistic view of reasoning capability and generalization rather than optimizing for a single metric.

## Weaknesses

### Fatal

None.

### Major

- **RL evaluation restricted to two models weakens the "compounding advantage" claim.** The paper's strongest headline claim — a +19% compounding advantage through RL (Table 3) — rests on a single comparison between M_LMQ and M_base, both fine-tuned on D_SHQ and then RL-trained. No other pretrained variant (M_LDQ, M_SHQ) is evaluated under RL, so we cannot observe whether the pretraining performance ranking is preserved, amplified, or altered by RL. The SFT-level evidence across all model variants (Tables 2, 4) already shows that pretraining advantage persists and amplifies; however, the specific claim that pretraining advantage "compounds" through RL and that "Pretraining Strategy Dictates Final Accuracy on Expert-Level Tasks" (Section 4) is overstated relative to the evidence. Evaluating M_LDQ and M_SHQ through the same RL protocol would convert this from an anecdotal observation into a pattern.

- **Confounds between diversity, scale, and data quality in the key pretraining comparison.** The paper's "asymmetric principle" is tested by comparing M_SHQ (1.2M high-quality, narrow-coverage examples) against M_LDQ (268M mixed-quality, broad-coverage examples). These datasets differ simultaneously in size (223×), diversity, and average quality. The observed advantage of M_LDQ at pretraining could be attributed to scale rather than diversity, or to their interaction. The paper partially mitigates this by including M_LMQ (which adds high-quality data to the diverse mix) and showing it provides minimal additional pretraining benefit — suggesting scale/diversity rather than quality drives the difference. However, a cleaner isolation (e.g., subsampling D_LDQ to match D_SHQ in token count while preserving topical breadth) would substantially strengthen the central claim that diversity, not merely data volume, is the driver.

### Minor

- **Headline percentages in the abstract are not clearly traceable to specific comparisons.** The abstract cites 19% (front-loading gain), 11% (diversity gain in pretraining), and 15% (quality gain in SFT). While the 19% is traceable to Table 3 (56.66 − 37.92 = 18.74), the 11% and 15% figures are not straightforwardly derivable from any single row in Tables 1–8 without post-hoc averaging across conditions that is not described. For instance, the 11% diversity gain appears closest to M_LDQ vs M_base in Table 1 (11.39%) but that comparison conflates diversity with the presence of any reasoning data. The paper would benefit from explicitly mapping each headline number to the exact comparison and arithmetic that produced it.

- **"Front-loading" terminology is somewhat misleading.** The paper describes injecting reasoning data into "pretraining," but in practice all reasoning data is introduced only during the final 400B of the 1T-token pretraining run (Section 2.3). The paper is transparent about this, but the term "front-loading" suggests early injection; the findings are more accurately about injecting reasoning data during (late) pretraining vs. during SFT, rather than about timing within pretraining itself. The paper acknowledges this implicitly but should state the limitation explicitly.

- **Reasoning ratio ablation is conducted on only one pretraining variant with one SFT recipe.** Section 5 explores how varying the reasoning-token ratio (10%, 20%, 40%) affects pretraining and downstream SFT, but this is tested only with M_LMQ and SFT_SHQ. The interaction between reasoning ratio and data composition (e.g., whether higher diversity at lower ratio matches lower diversity at higher ratio) is not explored, limiting the generality of the ratio-sensitivity findings.

### Trivial

- Some language in the introduction (e.g., "proves," "refutes," "dictates") overstates what a single 8B-training setup can establish. The empirical evidence is strong but does not constitute proof. More measured language (e.g., "demonstrates," "provides evidence against," "strongly influences") would better match the strength of the evidence.

## Nice-to-Haves

- Evaluate at least M_LDQ and M_SHQ under the same RL protocol to observe whether pretraining rankings are preserved through RL, and whether the asymmetric principle extends to the RL stage.
- Construct a size-matched subset of D_LDQ (equal token count to D_SHQ, preserving topic diversity) to isolate the effect of diversity at constant scale.
- Report variance estimates (e.g., over multiple evaluation runs with different seeds) to help the reader judge which differences are likely meaningful, especially given that models are trained from scratch once.
- The Table 2 averaging across three distinct SFT corpora obscures more than it reveals; focusing on the best SFT condition per model (as in Table 4) gives a fairer picture of what each pretrained foundation can achieve.

## Removed Points

These points were flagged for removal. Treat them with caution.

- **"No analysis of variance or sensitivity to RL hyperparameters is provided."** The critic demands confidence intervals and hyperparameter sensitivity analysis. This is a generic methodological criticism. While it would strengthen the paper, reporting variance for large-scale pretraining experiments (where models are trained from scratch once due to cost) is not standard in this field, and demanding it here would hold the paper to an inconsistently higher bar than comparable work. Moved out — this is a nice-to-have, not a flaw.

- **"The RL result is heavily featured in the abstract and introduction makes this gap particularly damaging."** The RL result is indeed featured prominently, but the gap (only 2 models evaluated in RL) is a real limitation. However, the critic frames this as "damaging" when the SFT-level evidence across all 12 model variants (Table 13, appendix-stripped) already demonstrates the persistence of pretraining advantage. The RL result provides additional validation, not the sole pillar of the claim. The criticism is partially retained as a Major weakness above, but the "damaging" framing is demoted.

- **"Table 2 averaging... produces a summary that obscures rather than illuminates."** The critic argues that averaging across three distinct SFT corpora mixes fundamentally different learning signals. This is a reasonable observation, but the paper also reports per-SFT-corpus breakdowns and Table 4 provides the cleaner comparison. The averaging in Table 2 provides a coarse aggregate that is still informative, and the detailed breakdown exists in the (stripped) appendix. Moved to Nice-to-Haves.

- **"The paper would be stronger if it either expanded the RL evaluation or moved it out of the primary narrative and treated it as a preliminary observation."** This is a judgement about narrative placement, not a substantive weakness in the methodology. Retained as part of the Major weakness about RL scope but the "preliminary observation" framing is the critic's preference, not a requirement.

- **"The decision to inject all reasoning data only during the final 400B tokens... means the study cannot speak to whether *when* reasoning data appears within pretraining... matters."** This is a scope limitation, not a weakness. The paper explicitly studies pretraining vs. SFT allocation, not intra-pretraining timing. The term "front-loading" is discussed above as a Minor weakness (misleading terminology). The scope criticism itself is removed — papers should be evaluated on what they study, not on what they don't study.

## Novel Insights

The paper's most distinctive contribution is the empirical demonstration that the optimal data profile for pretraining and SFT is *asymmetric in opposite directions* — diversity/scale for pretraining, quality for SFT — and that naïvely applying the "right" strategy at the wrong stage (e.g., diverse data during SFT) actively degrades performance. This challenges the intuitive assumption that what works at one stage should work at the other. The latent-effect finding — that high-quality pretraining data provides no immediate advantage but "unlocks" substantial gains after SFT — is a genuinely surprising result that suggests pretraining instills representations whose value is only realized through downstream alignment, a phenomenon that merits further investigation beyond this paper.

## Suggestions

- Map each headline percentage in the abstract to a specific row in a table with the exact arithmetic used. This will substantially improve the paper's credibility and reproducibility.
- Replace "front-loading" with a more precise term (e.g., "pretraining-stage reasoning injection") throughout, or add an explicit statement that the reasoning data is injected in the final 40% of pretraining tokens.
- Temper the language in the introduction and abstract: replace "proves" with "demonstrates," "refutes" with "provides strong evidence against," and "dictates" with "strongly influences." This will align the claims with the evidence while preserving impact.

## Score and Decision

**Calibration anchors considered:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| `KIPJKST4gw` ("At Which Training Stage Does Code Data Help LLMs Reasoning?") | 7.25 | R1/R2 | Most comparable in topic. Uses 2.6B model, less rigorous token control, no RL. Paper under review is more comprehensive but has confound issues KIPJKST4gw avoids. |
| `3OyaXFQuDl` ("Smaller, Weaker, Yet Better") | 7.00 | R2 | Clean contribution, well-executed but narrower scope (math only, Gemma only). Paper under review is broader but less methodologically tight. |
| `zpDGwcmMV4` ("How Can Language Models Learn from Mistakes") | 6.75 | R1/R2 | Focused on synthetic data for pretraining, limited to single synthetic dataset. Paper under review is broader and more practically relevant. |
| `1hQKHHUsMx` ("What Kind of Pretraining Data Do LLMs Rely on When Doing Reasoning?") | 6.75 | R1/R2 | Interpretability-focused, small-scale analysis. Different type of contribution. |
| `GtpubstM1D` ("Advancing Mathematical Reasoning in Language Models") | 5.71 | R2 | Similar topic (CPT vs SFT for reasoning) but less rigorous experimental design, high score variance. Paper under review is clearly stronger. |
| `07yvxWDSla` ("Synthetic continued pretraining") | 8.00 | R1 | Very clean methodology with theoretical model. Paper under review is less methodologically elegant. |

**Round 1 bracket:** 6.0 – 7.5. The paper is clearly above the weak-band anchors (2.0–2.5) and the 5.71 anchor, but below the 8.0 anchors that combine methodological clarity with theoretical depth.

**Round 2 narrowing:** The paper is most comparable to `KIPJKST4gw` (7.25) and `3OyaXFQuDl` (7.00). It is more comprehensive than both (multi-stage evaluation including RL, larger models, more benchmarks, controlled token budgets) but has more significant confounds in its key comparison (diversity conflated with scale) and an RL evaluation limited to two models. On balance, it is comparable to these 7.0-range papers — slightly above 3OyaXFQuDl in scope and ambition, slightly below KIPJKST4gw in methodological cleanliness. The paper is a solid accept with real contributions but would benefit from the suggested refinements.

**Final score: 7.0**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>