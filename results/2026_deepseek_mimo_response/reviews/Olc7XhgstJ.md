## Summary
This paper proposes Steady Thought (ST), a three-stage framework to mitigate "under-thinking" in Large Reasoning Models: (1) entropy-based segmentation of model responses into thoughts, (2) thought completion via switch-token suppression to generate correct continuations, and (3) thought-level preference optimization (STPO) that trains models to commit to promising reasoning trajectories. Experiments across three model sizes (1.5B, 8B, 14B) and four benchmarks show accuracy improvements up to 5.3% with token reductions up to 39.3%, including on an OOD code benchmark.

## Strengths
- **Consistent improvements across three model scales and four benchmarks including OOD**: Table 1 shows ST improves overall accuracy by +1.9%, +3.12%, and +2.52% for the 1.5B, 8B, and 14B models respectively, while simultaneously reducing token counts by 24.9%, 25.5%, and 17.3%. The OOD LiveCode results (trained only on math data) are compelling, with +5.3% accuracy on Qwen3-8B, demonstrating transferable reasoning behavior.
- **Effective ablation of training methods (Table 4)**: STPO outperforms both SFT (which drops accuracy from 82.2→80.4 on MATH500) and DPO (which fails to reduce length: 4273 vs 4385 tokens) on the same preference data. STPO achieves both (84.4 acc, 2809 tokens), providing clean evidence that thought-level conditioning and length normalization are key.
- **Mechanistic evidence via reduced invalid switching (Table 2)**: ST consistently reduces the Percentage of Correct Thoughts before the final answer (e.g., DeepSeek-1.5B on MATH500: 54.90%→40.40%), directly demonstrating models learn to commit to promising trajectories.
- **Clean problem formalization**: The Commit Trajectory vs. Switch Trajectory distinction (Section 2.1) and its grounding in the Bradley-Terry preference model provides a principled theoretical foundation connecting under-thinking to preference optimization.
- **Insightful difficulty-dependent behavior analysis**: Section 4.4.1 shows that for easy problems ST reduces thought count, but for hard problems (e.g., DeepSeek-1.5B on AIME) the model generates *more* thoughts while achieving higher accuracy and shorter length — supporting the claim that ST teaches *when* to switch rather than merely suppressing switching.

## Weaknesses

### Fatal
None

### Major
- **NOWAIT baseline anomaly on Qwen3-8B is unexplained and inflates ST's relative advantage**: In Table 1, NOWAIT on Qwen3-8B *increases* tokens by 84.6% (6122→11300) and drops accuracy by 21.2% (80.23→59.03). On the other two models, NOWAIT reduces tokens (−38.5% on 1.5B, −6.1% on 14B). The per-dataset breakdown is striking: NOWAIT on Qwen3-8B increases MATH-500 tokens from 4724 to 13274 and GSM8K tokens from 1759 to 12369 — strongly suggesting misconfiguration or model-specific incompatibility with the trigger words. The paper presents this without comment. Since NOWAIT is one of only three baselines, this anomaly weakens the comparative narrative on Qwen3-8B.
- **No variance or confidence intervals reported**: The paper states "We took the average of eight test runs for the AIME 2024 test set" (line 143) but reports only point estimates. AIME has only 30 problems — the difference between ST (31.2%) and Vanilla (27.5%) on DeepSeek-1.5B corresponds to ~1.1 additional problems solved per run. MATH-500 and GSM8K appear to be single-run evaluations. For headline claims of "up to 5.3% accuracy improvement," the lack of error bars on small test sets undermines statistical confidence.

### Minor
- **STPO objective novelty is overstated**: Equation 7 is SimPO applied with conditioning context (Q, T_i) instead of the full prompt x. The temperature β, margin γ, and length normalization are identical to SimPO (Equation 3). The paper describes STPO as "a novel preference optimization framework operating at the level of thoughts" (line 270), but the real contribution is the pipeline (how preference pairs are constructed), not the loss function.
- **Entropy threshold tuning shown only for 1.5B model**: Table 3 shows threshold tuning for DeepSeek-R1-Distill-Qwen-1.5B only. The paper defers tuning for other models to Appendix D (line 243), but the main text does not state what threshold values were used for Qwen3-8B and 14B.
- **"Overall" column equally weights datasets of different sizes**: Table 1's Overall accuracy averages across MATH-500 (n=500), AIME 2024 (n=30), GSM8K (n=1319), and LiveCode (n=400) with equal weight, giving AIME the same influence as GSM8K and inflating the contribution of noise-prone small-set evaluations.
- **Chosen vs. rejected response style asymmetry**: The chosen response was generated under switch-token suppression while the rejected was generated naturally. The preference signal may partially encode a style difference (absence of switching tokens) rather than purely a quality difference.

### Trivial
None

## Nice-to-Haves
- A direct comparison between "NOWAIT applied during training data generation + SFT" vs. the full ST pipeline would isolate whether preference optimization or the data generation approach is the key ingredient.
- Reporting the fraction of problems/thoughts producing valid preference pairs would substantiate scalability claims.
- Comparison with training-based baselines (e.g., RL with sustained-reasoning rewards) would better position the contribution.

## Removed Points
These points are flagged to be removed, treat them with caution:
- "Missing training hyperparameters" — likely in stripped appendix.
- "Trigger word list is vaguely specified" — "wait" and "alternatively" (line 99) are sufficient examples; full list may be in appendix.
- Criticisms about missing appendix content — the parser strips appendices; they exist in the original.
- Criticisms questioning existence of cited works — removed per policy.

## Novel Insights
The key insight is that under-thinking can be reframed as a thought-level preference optimization problem: rather than globally suppressing switching tokens (overcorrection), the model is taught *when* to commit via fine-grained preference pairs constructed automatically through entropy-based segmentation and thought completion. The OOD generalization (math-only training transfers to code tasks) is particularly noteworthy, suggesting the method teaches a meta-reasoning behavior rather than domain-specific patterns.

## Suggestions
- Investigate and explain the NOWAIT anomaly on Qwen3-8B; re-run with proper configuration if misconfigured.
- Report standard deviations or confidence intervals, especially for AIME 2024 (n=30).
- Reframe the STPO contribution: the novelty is in the thought-level preference pair construction pipeline; the loss function is SimPO with different conditioning context.
- Report entropy thresholds used for Qwen3-8B and 14B in the main text.

---

## Calibration Report

**Anchors retrieved (all rounds):**

| Paper | Score | Round | Comparison |
|-------|-------|-------|------------|
| pXIbcRPxWR (Supervised CoT) | 2.50 | 1 | Much weaker than ST — no preference optimization, no empirical rigor |
| EVZnnhtMNX (CVX-DPO) | 3.00 | 1 | Weaker — lightweight DPO variant, limited evaluation |
| jOuHjFw71C (Planning in Strawberry Fields) | 3.00 | 1 | Weaker — evaluation-only, no method contribution |
| BjZP3fTlVg (HCMA deployment) | 3.00 | 1 | Different focus, weaker contribution |
| jRZ1ZeenZ6 (Rational Metareasoning) | 5.00 | 1 | Similar topic (reasoning efficiency), but ST has broader eval and cleaner pipeline |
| bGGMLWAGMc (IUPO) | 5.50 | 1 | Closest comparison — iterative preference optimization for reasoning. ST has broader eval (3 models, 4 benchmarks vs. limited), OOD generalization IUPO lacks |
| rpbzBXdo4x (Mind Your Step) | 5.00 | 1 | Different scope — CoT analysis, not a method |
| zpENPcQSj1 (Length Generalization) | 6.33 | 2 | Theoretical work, different contribution type |
| O0sQ9CPzai (TPO) | 6.33 | 1+2 | Key anchor — tree-based preference optimization for math reasoning. ST has broader eval and OOD, but TPO's objective has more novelty. Comparable overall |
| 1Xg4JPPxJ0 (Connecting Knowledge) | 6.00 | 2 | Synthetic task study, different scope |
| GtpubstM1D (Math reasoning data) | 5.71 | 2 | Math data curation paper; ST has clearer pipeline contribution |
| w6nlcS8Kkn (To CoT or not to CoT) | 6.67 | 2 | Stronger — comprehensive meta-analysis with 100+ papers, much broader scope |
| v9CDpLpjiE (Visual-O1) | 6.67 | 2 | Different domain (multi-modal reasoning) |
| AmEgWDhmTr (Sparse Attention CoT) | 7.00 | 2 | Stronger — theoretical contribution on CoT sample efficiency |
| r3DF5sOo5B (Multi-step GD CoT) | 7.33 | 2 | Stronger — theoretical CoT analysis |
| rfdblE10qm (Rethinking Reward Modeling) | 8.00 | 1 | Much stronger — novel theoretical contribution |
| OfjIlbelrT (FlexPrefill) | 8.00 | 1 | Much stronger — different domain |
| 3bq3jsvcQ1 (Take a Step Back) | 8.00 | 1 | Much stronger — influential prompting technique |
| mMPMHWOdOy (WizardMath) | 8.00 | 1 | Much stronger — major math reasoning advancement |

**Round 1 bracket**: 5.5–7.0 (between IUPO at 5.5 and accept-level papers at 6.67+)

**Round 2 narrowing**: ST is comparable to TPO (6.33) but slightly weaker due to the NOWAIT anomaly and lack of variance reporting. It is clearly stronger than IUPO (5.5) but weaker than the comprehensive "To CoT or not to CoT" (6.67). Score: **6.0**.

**Decision**: Accept. The paper addresses a well-motivated problem with a clean, principled framework, consistent results across three model scales and four benchmarks, and genuine OOD generalization. The ablation studies (Tables 2 and 4) provide meaningful mechanistic evidence. While the NOWAIT anomaly and missing variance reporting are real concerns that should be addressed, they do not invalidate the core contribution, which is the thought-level preference optimization pipeline itself.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>