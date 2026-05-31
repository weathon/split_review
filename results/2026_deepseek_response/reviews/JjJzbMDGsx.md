## Summary

The paper proposes Language Confusion Gate (LCG), a lightweight two-layer MLP that attaches to any LLM and predicts allowed language families (CJ, Latin, Symbols, Low-Res) at each decoding step, masking disallowed tokens. LCG is trained via norm-adjusted self-distillation: the frozen LLM's norm-debiased top-k/p predictions serve as pseudo-targets. The method is motivated by three findings — language confusion is rare, correct-language tokens appear in the top-3 at 99.29% of confusion points, and output token embedding norms are biased toward high-resource languages. Evaluated across Qwen3, Llama3.1, Gemma3, and GPT-OSS on FLORES, INCLUDE, and Humaneval-XL, LCG reduces confusion by an order of magnitude with minimal overhead (0.4% latency increase) while largely preserving legitimate code-switching.

## Strengths

1. **Norm-adjusted self-distillation is grounded in a clear mechanistic finding.** The paper identifies and quantifies token embedding norm imbalance (Table 1: CJ and Latin tokens dominate the top 5% of norms while Low-Res tokens are heavily underrepresented, e.g., 0.07% for Qwen3-30B) and shows that removing this bias via norm adjustment makes confusion tokens vanish from the top-10 logits (Figure 2). The ablation (Table 3) confirms LCG-adjusted consistently outperforms LCG-unadjusted across all models and metrics — e.g., Latin confusion on Llama3.1-8B drops from 5.7% to 2.9%.

2. **Extreme intervention sparsity preserves computational and generative efficiency.** On FLORES-NO-LATIN, LCG intervenes on only 0.38% of tokens for Qwen3-8B (523/139,354) and 0.33% for Llama3.1-8B (Section 5.3). The paper reports a mere 0.4% latency overhead in a production setting (15.95ms → 15.99ms per step, Section 6), making the method practical for deployment.

3. **Demonstrably preserves legitimate code-switching.** On the FLORES-WITH-LATIN subset, LCG permits English tokens at 86.7% of human-validated code-switch points (Section 5.3). Post-intervention code-switch rates (e.g., 25.90% for Qwen3-8B) remain below the ground-truth answer rate (38.36%) and close to the Claude Sonnet 4 baseline (23.29%), showing the gate does not eliminate natural language mixing.

4. **Broad and consistent effectiveness across diverse model families and reasoning modes.** Tables 3 and 4 show that LCG reduces CJ and Latin confusion by an order of magnitude on five different models (Qwen3-8B, Qwen3-30B, Llama3.1-8B, Gemma3-12B, GPT-OSS) in both standard and thinking modes, without degrading BLEU, accuracy, or Pass@1/Pass@10.

5. **Confusion-point analysis directly motivates logits-based intervention over weight modification.** Section 3.1 shows that at confusion points the correct-language token appears in the top-3 at 99.29% frequency, proving the confusion is not due to absent correct tokens but to insufficient probability mass. This directly supports LCG's masking strategy over methods that require model retraining.

6. **Comprehensive comparison against multiple baselines.** Figure 3 compares LCG against ICL, greedy decoding, ORPO, and a no-rule ablation on both FLORES-NO-LATIN and INCLUDE. LCG consistently achieves the lowest confusion rates while maintaining task performance, whereas ORPO degrades accuracy (e.g., Qwen3-8B INCLUDE accuracy drops from 61.4 to 57.3) and ICL/greedy provide minimal improvement.

## Weaknesses

### Major

- **Human evaluation of code-switch preservation is underspecified.** The 86.7% token-level preservation rate (Section 5.3) is a central claim supporting that LCG distinguishes confusion from legitimate code-switch. However, the paper states only that "human annotators" judged cases of English use as "natural, appropriate code-switch" without reporting: the number of annotators, inter-annotator agreement, how many examples were annotated (or the total pool from which they were sampled), or what annotation guidelines were used. Without this information, the reliability and generalizability of the 86.7% figure cannot be assessed. The paper should report a confusion matrix showing both correct-preservation and correct-suppression rates on annotated data.

- **Limited thinking-model evaluation weakens the reasoning-model claim.** The thinking-model experiments (Table 4) use only Humaneval-XL (Python coding in Arabic and Hebrew). Confusion rates are already very low without intervention (e.g., Qwen3-30B: 0.12% CJ), and the Pass@1/Pass@10 differences between No LCG and LCG-adjusted are within noise (e.g., Qwen3-30B Pass@1: 91.25 vs. 90.50). The claim that LCG "effectively reduces language confusion on thinking models" rests on reducing already-low rates to near-zero on a single task type. Additionally, the framing that reasoning models "reintroduce" language confusion is not fully supported by the paper's own data: Qwen3-8B no-think shows higher confusion (4.5% CJ) than Qwen3-30B thinking (0.12% CJ).

### Minor

- **The link between training signal and evaluation is not independently validated.** The training pseudo-targets are derived from norm-adjusted logits, and the evaluation relies on the same script-level classification. While the norm-adjustment ablation (LCG-adjusted vs. LCG-unadjusted) provides some evidence that the gate learns more than the raw signal, there is no direct test of whether the gate is learning a *semantic/functional* distinction between confusion and code-switch rather than a refined script-level heuristic. An evaluation on explicitly constructed adversarial examples (clearly legitimate vs. clearly illegitimate code-switch) would strengthen the discrimination claim.

- **~0.7% of confusion points cannot be fixed by LCG.** The finding that correct-language tokens appear in top-3 at 99.29% of confusion points (Section 3.1) implies ~0.71% of cases lack any correct-language candidate. LCG cannot create allowed tokens that are not present in the candidate set — an acknowledged but undiscussed limitation that sets an upper bound on the method's recall.

- **Norm bias's contribution to confusion is not quantified.** Section 3.2 states norm bias "can account for a subset of such errors but cannot fully explain language confusion" without estimating how large this subset is. This matters for understanding whether the gate primarily learns to correct norm-bias-induced errors or something more complex.

- **ORPO baseline implementation lacks detail.** The paper states it "synthesize[s] samples with language confusion as rejected samples similar as Lee et al. (2025)" without specifying how confusion was injected, ORPO hyperparameters (β, learning rate), or training steps. The observed accuracy degradation (e.g., 61.4→57.3 on Qwen3-8B INCLUDE) may partly reflect suboptimal training rather than an inherent limitation.

- **Training data language distribution not analyzed.** The 78,000 samples over 200 languages are described but not broken down per language family or per source. Imbalance could cause the gate to learn shallow language-from-hidden-state correlations rather than a general discrimination rule. Evaluation covers specific scripts (Arabic, Hebrew, Korean, Thai, Chinese, Greek, Russian, Vietnamese) despite training on "over 200 languages."

- **Training-stage top-k/p hyperparameters not stated.** The k and p values used during training (Section 4.2) are not reported in the main text. These determine whether pseudo-targets are sparse or noisy, directly affecting gate quality. The intervention-rule values (k=5, p=0.999; k=20, p=0.95) are stated, but training values are not.

### Trivial

- BLEU scores on FLORES-NO-LATIN (11.3–17.1) are noted without comment on whether confusion reduction meaningfully improves utility at such low translation quality.

## Nice-to-Haves

- Partition confusion points by whether norm-adjustment helps (high-norm confusion tokens) vs. doesn't (low-norm confusion tokens) and report LCG's performance on each subset.
- Report LCG MLP parameter count and training compute cost to fully substantiate the "lightweight" claim.
- Add error bars or confidence intervals for the confusion rate measurements.

## Removed Points

*The following points from the Harsh Critic were removed because they do not hold up against the actual paper:*

- **"The evaluation fundamentally conflates two different measurement problems — LCG uses script-level detection to both define the problem and evaluate the solution"** — Mitigated. The paper explicitly addresses this by: (a) using FLORES-WITH-LATIN to specifically test code-switch preservation (a different measurement task from FLORES-NO-LATIN), (b) reporting token-level preservation on human-validated examples (86.7%), and (c) comparing against ground-truth answer rates and Claude Sonnet 4 baselines (Table 5). The norm-adjustment ablation further disentangles the training signal from the raw script-level classifier. The criticism overstates the circularity.

- **"The training signal for LCG is circular with the evaluation"** — Mitigated. The norm-adjustment is a principled geometric correction (removing norm magnitude from dot products), not just a heuristic. The ablation showing LCG-adjusted > LCG-unadjusted demonstrates the gate learns something beyond the unadjusted signal. The criticism that there's "no out-of-distribution test" is true but overstated as a fatal flaw — the paper evaluates on held-out datasets (INCLUDE, Humaneval-XL) that differ from the training distribution.

- **"The ORPO baseline comparison is potentially unfair"** — Partially valid but kept as a Minor weakness rather than Major since both methods are compared as reported, and the paper does not claim to be a comprehensive ORPO tuning study.

- **"The claim that reasoning models reintroduce confusion is contradicted by the paper's own data"** — Partially valid. Kept as part of the thinking-model evaluation weakness but not as a standalone fatal flaw, since DeepSeek-R1 (the cited source) is a different model from Qwen3.

- **"Missing parts and places to improve" list** — Some points (parameter count, per-language training analysis, hyperparameter sensitivity) are kept; others (not reporting training k/p values, limited evaluation languages) are kept as minor weaknesses.

- **Strength Finder strengths that were filtered** — Generic/superficial strengths removed (e.g., "training data covers over 200 languages" — kept as a genuine strength; "comprehensive comparison against diverse baselines" — merged into strength 6).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Expand the human evaluation** with explicit annotation guidelines, inter-annotator agreement scores, and a confusion matrix showing both correct-preservation and correct-suppression rates.
2. **Add a breakdown of training data by language family** to demonstrate coverage is not superficial.
3. **Report LCG's performance on explicitly constructed adversarial examples** that test the confusion-vs.-code-switch distinction (e.g., clearly legitimate technical terms vs. clearly erroneous character insertions).
4. **State the training-stage top-k/p values** for reproducibility.
5. **For the thinking-model claim**, add at least one more task type beyond Humaneval-XL to increase confidence.
6. **Acknowledge the ~0.7% recall ceiling** explicitly as a limitation.

## Score and Decision

**Calibration Summary:**

| Anchor Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| Llamas (mostly) think in English | fSbPwHjdDG.md | 3.00 | R1 (low) | Much weaker; fundamentally a correlation study with limited causal evidence and narrow scope |
| Mind Scramble / Typoglycemia | KBixkDNE8p.md | 3.00 | R1 (low) | Much weaker; speculative methodology |
| Babel Tower (multilingual code LLMs) | eznTVIM3bs.md | 5.25 | R1 (mid) | Weaker; limited to code LLMs, methodological concerns |
| Crosslingual Capabilities & Knowledge Barriers | BCyAlMoyx5.md | 5.67 | R1 (mid) | Weaker; significant methodological issues (non-multilingual models in multilingual study) |
| MBR & QE Finetuning | bkNx3O0sND.md | 6.00 | R2 (narrow) | Comparable; both propose practical decoding-time improvements with solid empirical support |
| Is Knowledge Multilingually Consistent? | HMa8mIiBT8.md | 6.00 | R1 (mid) | Comparable; similar score but LCG has stronger empirical results and clearer contribution |
| VocADT (Vocabulary Adapters) | KxQRHOre9D.md | 6.25 | R2 (narrow) | Slightly stronger in evaluation breadth (11 languages) but comparable contribution quality |
| The Same but Different (mechanistic interp) | NCrFA7dq8T.md | 6.60 | R2 (narrow) | Stronger in analytical depth but narrower scope (2 languages, 2 tasks) |
| DEPT / Sparse Feature Circuits / etc. | various | 8.00 | R1 (high) | Clearly stronger; these are breakthrough contributions with broader impact |

**Round 1 Bracket:** The paper clearly sits in the middle band (between 3.5 and 7.5). It is substantially stronger than the low-band papers (avg 3.0–3.25) and does not approach the elite 8.0-level papers.

**Round 2 Narrowing:** Comparing against the mid-band anchors: this paper is stronger than Babel Tower (5.25) and Crosslingual Capabilities (5.67), comparable to MBR Finetuning (6.00) and VocADT (6.25), and somewhat weaker than The Same but Different (6.60) in terms of analytical depth. The norm-adjusted self-distillation is a genuinely novel contribution, the empirical evaluation is broad (5 models, multiple datasets), and the method is practical. The main gap is the underspecified human evaluation for the discrimination claim and the thin thinking-model evaluation, which prevent this from being a stronger paper.

**Final Score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>