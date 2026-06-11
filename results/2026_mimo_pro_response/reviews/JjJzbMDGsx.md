Now I have enough data. Let me finalize the review and score.

**Round 1 bracket**: 6.0–7.0, based on comparison to:
- "Token-Aware ITI" (6.00, reject) — similar inference-time intervention approach, but our paper has stronger evaluation breadth and more novel mechanistic motivation
- "The Same but Different" (6.60, accept) — mechanistic multilingual analysis, our paper is more practical
- "CREMA" (6.80, accept) — practical multi-modal framework, our paper has more focused scope with stronger deployment evidence
- "DetoxiGen" (5.75, reject) — similar inference-time token filtering, but our paper is stronger across all dimensions

**Round 2 narrowing**: 6.0–7.0 confirmed. Our paper is clearly above the 5.75 rejects (DetoxiGen, Approximately Aligned Decoding) and comparable to or slightly below the 6.6–7.0 accepts.

Final score: **6.5** — The paper has a clear, practical contribution with strong evaluation breadth and mechanistic grounding. The code-switching suppression issue and lack of variance reporting are real concerns that prevent a higher score, but neither invalidates the core contribution.

## Summary
This paper proposes the Language Confusion Gate (LCG), a lightweight two-layer MLP that predicts permissible language families at each decoding step and masks tokens from disallowed families to reduce language confusion in multilingual LLMs. The gate is trained via norm-adjusted self-distillation on the frozen model's own predictions, exploiting the mechanistic insight that output token embedding norms create systematic bias toward high-resource languages. Evaluation across Qwen3, Llama3.1, Gemma3, and GPT-OSS demonstrates large reductions in confusion rates with minimal latency overhead (0.4%).

## Strengths
- **Mechanistically grounded design**: The paper decomposes logits into norm and cosine similarity (Section 3.2, Eq. 2: `logit_i = ||h|| · ||e_i|| · cos_sim(h, e_i)`) and demonstrates with concrete data (Table 1: CJ tokens occupy 10.74% of top-5% norm group in Qwen3-8B vs 0.14% for Low-Res) and visualization (Figure 2: top-10 tokens flip from CJ to Hebrew after norm adjustment) that embedding norm bias drives confusion. This principled insight directly motivates the norm-adjustment training technique and the ablation confirms its importance (Table 3: Llama3.1-8B Latin confusion 5.7%→2.9% with norm-adjustment).

- **Large, consistent confusion reduction across diverse models**: Table 3 shows LCG-adjusted reduces CJ confusion from 4.5%→0.1% and Latin from 12.1%→2.0% on Qwen3-8B, from 1.0%→0.0% CJ and 4.4%→0.4% Latin on Qwen3-30B, with consistent improvements across four model families and both thinking/no-thinking modes. Table 4 shows similar gains for thinking models (e.g., GPT-OSS CJ% 0.38%→0.06%).

- **Practical efficiency with production validation**: Section 6 reports production benchmarks showing 15.95ms vs 15.99ms per step (0.4% overhead), and the intervention is sparse (0.33–0.38% of generated tokens), substantiating the "lightweight plug-in" claim with concrete deployment measurements.

- **Comprehensive baseline comparison**: Figure 3 compares against ICL, greedy decoding, ORPO tuning, and "No Rule" ablation, demonstrating that greedy decoding is nearly ineffective (CJ% 4.5%→4.2%) — well-motivated by the Section 3.1 finding that the confusion token is top-1 56.74% of the time — and that ORPO degrades general accuracy (61.4→57.3 on INCLUDE), highlighting the trade-offs LCG avoids.

- **Honest treatment of trade-offs**: The paper openly acknowledges that LCG's code-switching suppression is "more cautious" (Section 5.3), that norm bias "can't explain language confusion between English and Chinese" (Section 3.2), and that script-level granularity is a limitation (Section 6). The 86.7% token-level preservation rate is reported alongside the response-level code-switching metrics, giving readers a full picture.

## Weaknesses

### Fatal
None

### Major
- **Significant suppression of legitimate code-switching not adequately acknowledged**: Table 5 shows Qwen3-8B's code-switch rate on FLORES-WITH-LATIN drops from 46.34% to 25.90% with LCG-adjusted, when the ground-truth answer rate is 38.36%. This is a ~44% relative decrease, and the post-intervention rate falls substantially below the answer rate. The paper states at line 288 that post-intervention rates are "not much lower than the ground-truth answer rate (38.36%)" — but 25.90% vs 38.36% is a meaningful gap (32% relative). While the 86.7% token-level preservation rate sounds high, the cumulative effect on response-level code-switching is significant. The paper's central claim that LCG distinguishes harmful confusion from legitimate code-switching is its core differentiator from simpler single-language enforcement, yet the quantitative evidence shows substantial suppression of legitimate behavior. A more candid discussion of this gap, ideally with human evaluation of output quality, would substantially strengthen the paper.

- **No variance or confidence intervals reported**: Several headline results involve confusion rates below 1% (e.g., Gemma3-12B CJ% 0.2%→0.1%, GPT-OSS CJ% 0.38%→0.06%). With finite evaluation sets — FLORES+ has ~1012 sentence pairs per language — a CJ% of 0.1% corresponds to roughly 1 sentence. Differences at this scale could reflect sampling noise. Standard error bars or bootstrap CIs would clarify which improvements are robust, particularly for models where the baseline confusion rate is already very low.

### Minor
- **Table 4 mislabeled**: Table 4 is titled "Effectiveness of LCG Intervention on 'No-Think' Models measured on Humaneval-XL" (line 273) but the preceding section heading is "Experiments on Thinking Model Intervention" (line 269). The Pass@1/Pass@10 metrics and reasoning token length columns confirm these are thinking model results. This is a copy-editing error that creates confusion.

- **Confusion point statistics only reported for Qwen3-8B**: The key finding motivating the method — confusion token is top-1 56.74% of the time, correct-language token in top-3 99.29% (Section 3.1) — is validated on only one model. Since the method's effectiveness depends on this distributional property holding broadly, confirming it across at least one more architecture would strengthen the motivation.

- **"Order of magnitude" claim is selectively supported**: The abstract claims confusion is reduced "often by an order of magnitude," which holds for Qwen3-30B CJ% (1.0→0.0) but not for Llama3.1-8B Latin% (8.4→2.9, ~3x). The introduction's examples (line 72) cite only the best-case model.

### Trivial
None

## Nice-to-Haves
- Human evaluation of code-switching quality (with bilingual annotators) would directly evaluate the core distinguishing claim
- Error analysis of interventions: what fraction of the 0.38% of masked tokens are correct (suppressing genuine confusion) vs. erroneous (masking legitimate tokens)?
- More fine-grained language family classification (acknowledged in Section 6 as future work)

## Removed Points
These points are flagged to be removed, treat them with caution:
- Harsh critic's concern about BLEU improvements being marginal (0.1-0.2 points): The paper's claim is "maintaining task performance," not improving BLEU. The BLEU scores serve to show no degradation, which they successfully do. Not a real weakness.
- Strength Finder's claim that "post-intervention code-switch rates remain comparable to the ground-truth answer rate": This is invalidated by the verified weakness — 25.90% vs 38.36% is not "comparable" for Qwen3-8B.
- Harsh critic's concern about training hyperparameters not in Section 4.2: The top-k/p values appear in Section 4.3 and the training procedure clearly references using them to construct pseudo-targets. This is a minor presentation issue, not a reproducibility gap.

## Novel Insights
The decomposition of logit contributions into embedding norm and cosine similarity (Section 3.2), combined with the empirical demonstration that norm bias systematically favors high-resource language tokens (Table 1), provides a genuinely novel mechanistic explanation for language confusion. The key insight — that norm adjustment reveals correct-language tokens in the top-k predictions, enabling self-distillation pseudo-targets without manual annotation — is both elegant and practically validated by the ablation showing consistent improvement from LCG-unadjusted to LCG-adjusted.

## Suggestions
- Add confidence intervals (bootstrap or otherwise) for all confusion rate measurements, especially those below 1%
- Revise the framing of Table 5 to more honestly acknowledge the gap between post-intervention code-switch rates and ground-truth answer rates, particularly for Qwen3-8B (25.90% vs 38.36%)
- Fix the Table 4 title from "No-Think" to "Thinking"
- Report confusion point statistics (top-1 rank, top-3 coverage) for at least one additional model architecture to confirm generalizability

## Calibration Report

**Anchors retrieved across all rounds:**

| Round | Paper Path | Avg Score | Comparison |
|-------|-----------|-----------|------------|
| 1 | fSbPwHjdDG ("Llamas think in English") | 3.00 | Mechanistic LLM paper, rejected — much weaker contribution than our paper |
| 1 | KBixkDNE8p ("MIND SCRAMBLE") | 3.00 | LLM psychology paper, rejected — unserious methodology |
| 1 | 4y3GDTFv70 ("Latent Space Theory") | 3.25 | Theory paper, rejected — speculative, not empirical |
| 1 | uOnElfFuey ("Recovering Knowledge") | 3.00 | Regular language knowledge recovery, rejected — very different scope |
| 1 | eznTVIM3bs ("Babel Tower") | 5.25 | Multilingual pre-training analysis, accepted — less practical than our paper |
| 1 | T2h2V7Rx7q ("Scaling Laws Multilingual") | 5.25 | Scaling law paper, rejected — different focus |
| 1 | r3GxWNGpSj ("XTransplant") | 4.75 | Multilingual capability probe, rejected — less concrete method |
| 1 | cif0JVXJ3b ("Qualifying Knowledge") | 5.25 | Knowledge analysis in multilingual models, rejected |
| 1 | BCyAlMoyx5 ("Crosslingual Capabilities") | 5.67 | Crosslingual evaluation, rejected — less practical |
| 1 | NCrFA7dq8T ("The Same but Different") | 6.60 | Mechanistic interpretability, accepted — different focus, our paper more practical |
| 1 | HMa8mIiBT8 ("Cross-Lingually Consistent") | 6.00 | Cross-lingual consistency, rejected — less actionable |
| 1 | FrFQpAgnGE ("Unified Representation Space") | 7.00 | Representation alignment, accepted — strong but different |
| 1 | vf5aUZT0Fz ("DEPT") | 8.00 | Decoupled embeddings, accepted — stronger theoretical contribution |
| 1 | SPS6HzVzyt ("Context-Parametric Inversion") | 8.00 | Instruction finetuning, accepted — different scope |
| 1 | tyEyYT267x ("SAR diffusion") | 8.00 | Diffusion language models, accepted — very different |
| 1 | I4e82CIDxv ("Sparse Feature Circuits") | 8.00 | Interpretability, accepted — different scope |
| 1 | af2ztLTFqe ("Token-Aware ITI") | 6.00 | Inference-time intervention for alignment, rejected — similar approach but weaker evaluation |
| 1 | zpVPhvVKXk ("Get What You Want") | 6.00 | Image content suppression, accepted — different domain |
| 1 | Igm9bbkzHC ("Controllable Context Sensitivity") | 6.75 | Context sensitivity control, accepted |
| 2 | vG9dVXwXQV ("VLM Selection") | 6.33 | Model selection for VLMs, rejected |
| 2 | 3UaOlzDEt2 ("CREMA") | 6.80 | Multimodal modular fusion, accepted — our paper has more focused impact |
| 2 | Zkq4fsyjfp ("CLIP Ensembling") | 6.25 | CLIP backbone diversity, accepted |
| 2 | NDLmZZWATc ("DeMul") | 6.40 | Prompt learning, accepted |
| 2 | 9WbNpFuS ("Approximately Aligned Decoding") | 5.75 | Constrained decoding, rejected — less practical |
| 2 | TOveLu4O51 ("DetoxiGen") | 5.75 | Inference-time detoxification, rejected — similar approach, weaker evaluation |
| 2 | 0JjsZC0w8x ("COrAL") | 5.75 | Order-agnostic LM, rejected |
| 2 | c61unr33XA ("Dataset Distillation KD") | 7.00 | Dataset distillation, accepted |
| 2 | h57gkDO2Yg ("Self-Supervised DD") | 6.20 | Self-supervised distillation, accepted |
| 2 | 2RfWRKwxYh ("Boost Self-Supervised DD") | 6.25 | Self-supervised distillation, accepted |

**Round 1 bracket**: 6.0–7.0. The paper is clearly above the 5.25–5.75 band (rejects with limited practical impact) and comparable to the 6.0–7.0 band (accepted papers with focused contributions).

**Round 2 narrowing**: 6.0–7.0 confirmed. Compared to "DetoxiGen" (5.75, reject) — the most methodologically similar anchor — our paper has stronger evaluation breadth, more novel mechanistic grounding, and production deployment evidence. Compared to "The Same but Different" (6.60, accept) and "CREMA" (6.80, accept), our paper has comparable contribution scope and evaluation quality.

**Final score**: 6.5. The paper has a genuinely useful, well-motivated contribution with strong evaluation breadth. The code-switching suppression concern (Qwen3-8B post-intervention rate 25.90% vs ground truth 38.36%) is a real limitation that prevents a higher score, but it is partially acknowledged by the authors and does not invalidate the core contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>