Now let me finalize my calibration. Let me compare my paper against the Round 2 anchors:

- **BGnm7Lo8oW (5.50, rejected)**: Studies reward functions for reasoning during pretraining but the method doesn't work at scale. Our paper is clearly stronger — it demonstrates convincing results at 8B/1T-token scale.
- **GtpubstM1D (5.71, accepted)**: Similar topic (CPT vs SFT for reasoning), but math-only, proprietary data, and more cluttered findings. Our paper has cleaner design, budget control, multi-domain scope — clearly stronger.
- **1hQKHHUsMx (6.75, accepted)**: Uses influence functions to study pretraining data for reasoning. Methodologically novel but narrow scope (80 questions). Our paper is more comprehensive and practically impactful. Comparable quality through different contribution types.
- **3OyaXFQuDl (7.00, accepted)**: "Smaller, Weaker, Yet Better" — cleaner, more surprising finding with well-executed experiments. Our paper is below this.

**Final score: 6.0.** The paper is a solid, well-executed empirical study with clear takeaways; its limitations (RL phase limited, architecture, confounds) keep it from the 7+ tier but don't undermine the core contribution. Decision: Accept.

Now let me write the final review.

---

All anchor papers across rounds:

Round 1:
- OdoS6cH8MP (2.00): Data valuation metrics — completely different topic, much weaker paper
- qgLyKwXVDs (2.00): Fine-tuning-free LM — unrelated topic
- MGceYYNvXp (1.50): LLM benchmark aggregation — unrelated
- 506Sxc0Adp (4.00): Diversity coefficient for pretraining — related but more theoretical, rejected
- kDakBhOaBV (4.00): Similar diversity coefficient paper
- qUJsX3XMBH (4.40): Random selection for SFT — somewhat related but limited
- eNbA8Fqir4 (6.00): DataMan — data quality for pretraining, accepted
- huuKoVQnB0 (6.00): Perplexity correlations for data selection, accepted
- EDoD3DgivF (6.00): Linear representations and pretraining data frequency
- 3OyaXFQuDl (7.00): Compute-optimal sampling for reasoning, accepted
- WoPovNkM5h (6.50): Tabular prediction — less related
- rTCJ29pkuA (6.33): Knowledge graph reasoning — less related
- jOmk0uS1hl (8.00): Training on the test task — very clean, strong paper
- 07yvxWDSla (8.00): Synthetic continued pretraining — strong contribution
- WyEdX2R4er (8.00): Visual data-type understanding

Round 2:
- GtpubstM1D (5.71): Mathematical reasoning CPT vs SFT — most comparable paper, our paper is stronger
- cijO0f8u35 (5.25): Scaling laws for math reasoning — somewhat related
- 28gMnEAgl9 (5.33): Abstract reasoning benchmark — less related
- BGnm7Lo8oW (5.50): Reasoning at pretraining scale — our paper is stronger
- S6cBH99BhB (6.50): Multilingual reasoning data proportions — our paper has broader scope
- 1hQKHHUsMx (6.75): Pretraining data influence on reasoning — different type, comparable quality
- w6nlcS8Kkn (6.67): CoT meta-analysis — related but different

Our paper is clearly above the 5.5-5.7 papers and below the 7.0 paper. Sitting at 6.0.## Final Review

### Summary
This paper conducts the first systematic study of when to inject reasoning data across the LLM training pipeline (pretraining vs. SFT), controlling for total reasoning-token budget while varying data diversity, quality, and scale. The authors pretrain 8B-parameter hybrid models from scratch for 1T tokens under four reasoning-data conditions, then cross each with multiple SFT recipes and push two variants through RL. The central finding is an asymmetric allocation principle: pretraining benefits most from diverse, large-scale reasoning data, while SFT is dominated by data quality. The paper also demonstrates that pretraining advantages compound through SFT and RL, that SFT cannot "catch up" to reasoning-pretrained models, and that high-quality pretraining data can have latent benefits that only emerge after SFT.

### Strengths
- **Fully-crossed, budget-controlled experimental design.** The paper trains four distinct base models (M_base, M_SHQ, M_LDQ, M_LMQ) under a fixed 80B reasoning-token budget, then crosses each with multiple SFT recipes (SFT_SHQ, SFT_LDQ, SFT_LMQ), producing the 12-model matrix in Table 2 and the ablations in Tables 4–5. This design enables clean attribution of performance differences to *when* and *what kind* of reasoning data is introduced, rather than confounding with data volume (Section 2.3, Eq. 2).

- **Multi-phase evaluation demonstrates compounding advantages.** The paper evaluates at three checkpoints — after pretraining (Table 1), after SFT (Table 2), and after RL (Table 3) — showing the gap between reasoning-pretrained and baseline models widens at each stage. The baseline M_base trails M_LMQ by ~11 points after pretraining, ~21 points after SFT (M_base+SFT_SHQ at 29.92 vs M_LMQ+SFT_SHQ at 50.95 in Table 4), and ~19 points after RL (37.92 vs 56.66 in Table 3), directly refuting concerns about overfitting or washout.

- **Clean refutation of the "catch-up" hypothesis (Table 4).** Doubling SFT epochs for M_base on the same high-quality data D_SHQ yields 34.01 average, which still falls short of the weakest reasoning-pretrained model M_SHQ + SFT_SHQ at 37.33. This holds SFT data constant and varies only pretraining history plus SFT compute, providing direct counterfactual evidence.

- **Compelling asymmetric principle: diversity in pretraining, quality in SFT (Tables 1 and 5).** After pretraining, the diverse-data model M_LDQ (64.09) substantially outperforms the high-quality-but-narrow model M_SHQ (54.98) — a ~9-point gap showing diversity dominates early. In SFT, the pattern reverses: M_res + SFT_SHQ (high-quality) achieves 44.99 while M_res + SFT_LDQ (diverse, lower-quality) reaches only 31.54 — a ~13-point gap showing quality dominates late. This phase-dependent reversal of which data property matters is non-obvious and practically actionable.

- **Latent-effects finding (Table 4).** M_LMQ and M_LDQ are essentially tied after pretraining (64.07 vs 64.09), yet after identical SFT_SHQ treatment, M_LMQ pulls ahead by +4.25 points (50.95 vs 46.70). This demonstrates that high-quality data mixed into a diverse pretraining corpus can have benefits invisible at the pretraining checkpoint that SFT later reveals.

- **Multi-domain evaluation breadth.** Evaluation spans math (GSM8K, MATH-500, AIME24/25), science (MMLU, MMLU-Pro, GPQA-Diamond), code (HumanEval, MBPP, LiveCodeBench), general reasoning (ARC, HellaSwag, WinoGrande, RACE), and instruction following (IFEval), showing the front-loading advantage generalizes across domains beyond math where most prior work has concentrated.

### Weaknesses

#### Fatal
None.

#### Major
None.

#### Minor
- **RL-phase evidence is limited to two extreme models.** Table 3 compares only M_base + SFT_SHQ + RL against M_LMQ + SFT_SHQ + RL. The paper is transparent that these are selected as "extreme pretraining backbones" (line 193), but the headline "+19% gain" claim in the abstract rests on this single comparison. The paper cannot speak to how M_LDQ or M_SHQ would perform through RL, which limits the generality of the "compounding returns" narrative. The SFT-stage results (Tables 2, 4) provide stronger support for compounding, but the RL phase — presented as the culminating demonstration — is underpowered relative to the claims made.

- **The "latent effect" interpretation is not the only explanation.** The finding that M_LMQ ≈ M_LDQ at pretraining but M_LMQ > M_LDQ after SFT is interesting and well-documented. However, the paper frames this as data with "dormant benefits that SFT later unlocks" and a "deeper synergy where pretraining can instill a latent potential" (lines 215–216). An alternative and simpler explanation is that the 1.2M extra high-quality samples in M_LMQ provide complementary benefits that the pretraining evaluation suite (which tests general QA and knowledge, not deep reasoning) does not detect, but which become visible when the model is later fine-tuned for reasoning. The paper would be strengthened by acknowledging this alternative interpretation.

- **Quality/scale confound in SFT data comparison (Table 5).** D_SHQ contains 1.2M samples while D_LDQ contains 268M samples — a ~223x difference. The paper concludes that SFT is "dominated by data quality, not diversity" (line 226), but the confound between quality and dataset size is not addressed. It is possible that the SFT advantage of D_SHQ partly reflects that smaller, focused datasets avoid overfitting or interference in SFT, rather than purely reflecting quality.

- **Hybrid architecture limits generalizability claims.** The model uses a hybrid Mamba-2/attention/FFN design (Section 2.1), which is non-standard compared to the dense Transformer architectures used in most LLM research. The paper mentions a 1.2B pure-Transformer validation (line 172, Table 14 in appendix), but an 8B hybrid model and a 1.2B dense transformer differ in both scale and architecture. The paper's claims about data strategy may not fully transfer to standard Transformer architectures at comparable scale.

#### Trivial
- **Small numerical discrepancy in abstract.** The abstract claims an "11% average gain" from diversity in pretraining, while the paper body (line 211) reports a +9.09% average gain for M_LDQ over M_SHQ. The discrepancy is small and does not affect the paper's conclusions, but should be corrected for consistency.

- **SFT data repetition not specified.** The SFT protocol uses 4.8M reasoning samples from D_res (line 124), but D_SHQ contains only 1.2M samples, implying ~4x repetition for that dataset. The paper should clarify how repetition is handled across datasets.

### Nice-to-Haves
- **No variance or confidence intervals reported.** The evaluation uses 4–16 runs per task (Section 3.2) but reports no standard deviations. While single-point estimates are common in large-scale LLM training papers, reporting variance would strengthen confidence in the finer-grained comparisons (e.g., the 4.25-point latent effect gap).

- **Running all four pretraining variants through RL** would strengthen the compounding claims and allow testing whether the latent effect persists through RL.

- **Additional catch-up strategies** beyond doubling SFT epochs (e.g., varying SFT data composition) could further test the robustness of the "SFT cannot compensate" conclusion.

### Removed Points
These points are flagged to be removed, treat them with caution.

- **"No statistical significance or variance is reported anywhere" (Harsh Critic #3):** While true that no variance is reported, this is standard practice in large-scale LLM pretraining papers where training cost makes multiple training runs prohibitive and evaluation-run variance is typically reported only when it would change conclusions. Demoted from "methodological gap that weakens all quantitative claims" to Nice-to-Have.

- **"The claim about science domain prominence should account for relative improvement" (Harsh Critic section-by-section):** The paper's claim about science-domain prominence refers to absolute percentage-point gaps, which is standard. The 13.85-point absolute gap in science is indeed the largest across domains. Relative improvement is a different metric that would answer a different question.

- **"Missing related work on data mixing ratios or curriculum learning" (Harsh Critic Related Work):** Per instructions, I do not flag missing related works since I cannot verify their existence externally.

- **Strength Finder "The paper addressed an important problem":** Generic and superficial; the paper's contribution is the empirical findings, not the problem selection.

- **"Asymmetric aggregation in Table 2" (original draft):** M_res is defined as the average of three models, and its comparison to M_base in Table 2 is simply the definitional consequence of having three reasoning-pretrained variants vs one baseline. The direction of the effect is unambiguous from individual model comparisons in Table 4. Removed as not a substantive weakness.

### Novel Insights
The asymmetric allocation principle — that diversity matters more in pretraining while quality matters more in SFT — is genuinely novel and practically impactful. While each half of this principle has been discussed separately in the literature (diverse pretraining data is helpful; high-quality SFT data is helpful), the paper's demonstration of a phase-dependent *reversal* through a controlled, budget-equated experimental design provides a principled, actionable framework that was previously absent. The latent-effects finding — that high-quality data mixed into pretraining can show no immediate benefit but substantial gains after SFT — is also a novel empirical observation with practical implications for how practitioners evaluate pretraining data mixtures.

### Suggestions
- Acknowledge alternative interpretations of the latent-effect finding (e.g., that it reflects measurement limitations of pretraining benchmarks rather than a truly "dormant" capability).
- Clarify in the RL section that only two extreme models were evaluated through RL and temper the generality of the compounding claims accordingly, or note this as a limitation.
- Address the quality/scale confound in the SFT data comparison by discussing whether dataset size (not just quality) may contribute to the observed SFT advantage of D_SHQ.
- Correct the minor numerical discrepancy between the abstract (11%) and body (9.09%) for the diversity gain in pretraining.

### Score Calibration

**Round 1 bracket: 5.5 – 7.0.** Based on comparison against:
- DataMan (6.00) and Perplexity Correlations (6.00): our paper has more systematic design and larger scale.
- Compute-Optimal Sampling (7.00): our paper is below this — less surprising finding, more limitations.
- Strong anchors at 8.00: our paper is clearly below.

**Round 2 narrowing:**
- GtpubstM1D (5.71): Most comparable paper (CPT vs SFT for math reasoning). Our paper has cleaner design, budget control, and broader domain scope — clearly stronger.
- BGnm7Lo8oW (5.50): Reasoning at pretraining scale. Our paper actually demonstrates what it claims at meaningful scale — clearly stronger.
- 1hQKHHUsMx (6.75): Different type of contribution (interpretability-focused). Comparable quality but our paper has more practical impact.
- 3OyaXFQuDl (7.00): Cleaner, more surprising finding. Our paper is below this tier.

**Final score: 6.0.** The paper is a solid, well-executed empirical study with clear, actionable takeaways. The core asymmetric principle is well-supported by the pretraining and SFT experiments. Minor limitations (RL phase limited, architecture generalizability, confounds, latent-effect interpretation) prevent it from being in the 7+ tier but do not undermine the core contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>