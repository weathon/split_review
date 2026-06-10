## Summary
This paper proposes the Language Confusion Gate (LCG), a lightweight two-layer MLP that predicts which language families (Chinese/Japanese, Latin, Symbols, Low-Resource) are permissible at each generation step and masks logits from disallowed families during decoding. The gate is trained via norm-adjusted self-distillation, which debiases the training signal against a systematic embedding norm bias favoring high-resource language tokens. Evaluated across 7 model configurations on FLORES+, INCLUDE, and Humaneval-XL, LCG achieves substantial reductions in language confusion (often order-of-magnitude for CJ confusion) with negligible latency overhead (0.4%) and without degrading task performance.

## Strengths
- **Clear mechanistic insight grounded in geometric decomposition**: Section 3.2 decomposes logit_i = ||h|| · ||e_i|| · cos_sim(h, e_i), showing that embedding norm creates systemic bias toward high-resource languages. Table 1 quantifies this across 5 models, and Figure 2 concretely demonstrates how norm-adjustment reshuffles top-10 logits at a confusion point, eliminating CJ tokens from top ranks. This is a genuinely useful mechanistic contribution that goes beyond a surface-level observation.
- **Empirically grounded confusion-point analysis**: Section 3.1 reports the confusion token is top-1 56.74% of the time (explaining why greedy decoding fails) while correct-language tokens appear within top-3 99.29% of the time. These specific numbers directly motivate the gate's logit-masking design and demonstrate that the model "knows" the correct language but has insufficient probability mass assigned to it.
- **Norm-adjusted self-distillation ablates well**: Table 3 shows LCG-adjusted consistently outperforms LCG-unadjusted across all models (e.g., Llama3.1-8B Latin from 5.7% to 2.9%, CJ from 2.0% to 0.4%), directly validating the core methodological claim.
- **Comprehensive evaluation across diverse models and settings**: 7 model configurations spanning Qwen3, Llama3.1, Gemma3, GPT-OSS across both thinking and no-think modes, with consistent results (Tables 3–4). This breadth strengthens generalizability claims substantially.
- **Practical efficiency with concrete benchmarks**: 0.4% latency overhead in production (15.95ms → 15.99ms), sparse intervention rate of 0.33–0.38% of tokens. Combined with plug-in architecture requiring no model retraining, this supports real deployment claims.
- **Thoughtful evaluation methodology**: FLORES-NO-LATIN / FLORES-WITH-LATIN partitioning distinguishes erroneous Latin intrusion from legitimate code-switching; code-switch preservation validated at both token level (86.7% of human-validated code-switch permitted) and response level (Table 5).

## Weaknesses

### Fatal
None

### Major
- **Missing comparisons against the closest prior inference-time methods**: The Related Work (Section 2) discusses Nie et al. (2025), which suppresses language-switching neurons during inference, and Ji et al. (2025), which proposes post-hoc smoothing to suppress Chinese tokens during decoding. Both are inference-time interventions operating without modifying base model weights—making them the most directly comparable baselines. Yet the experimental comparison (Section 5.3, Figure 3) only tests against ICL, greedy decoding, and ORPO fine-tuning. Without comparing against these closest alternatives, the reader cannot assess whether LCG's advantage is its specific technical contribution or simply that a well-tuned logit-masking approach outperforms prompting tricks.

- **No statistical reliability analysis for confusion rate metrics**: Confusion rates are reported as point estimates (e.g., 0.0%, 0.1%, 0.4%) with no confidence intervals or variance across runs. At FLORES-NO-LATIN's scale (~4,048 samples for no-think models), the difference between "eliminates all confusion" and "reduces to near-zero" is 0–2 sentences. For Humaneval-XL thinking experiments, GPT-OSS CJ% drops from 0.38% to 0.06%—a difference that could shift with different random seeds. The directional result is likely robust, but the precise magnitude claims ("order of magnitude") require statistical support.

### Minor
- **"Order of magnitude" claim overstated for Latin confusion**: The abstract and introduction claim LCG "decreases language confusion significantly, often by an order of magnitude." This is accurate for CJ confusion on several models (Qwen3-30B: 1.0% → 0.0%) but overstated for Latin confusion (e.g., Llama3.1-8B: 8.4% → 2.9%, ~3× reduction, not 10×). The abstract should qualify this claim to say "often by an order of magnitude for CJ confusion" or similar.
- **Coarse four-family grouping not prominently scoped as a limitation in abstract/introduction**: The CJ/Latin/Symbols/LowRes grouping means LCG cannot address Korean-Arabic or Spanish-English confusion. This is honestly acknowledged in the conclusion but the abstract and introduction frame the method more broadly. The evaluation languages (Arabic, Hebrew, Korean, Thai, Greek, Russian, Vietnamese) are mostly low-resource, making the gate essentially a binary CJ/Latin-vs-everything-else filter—a legitimate and useful task, but less general than the framing suggests.

### Trivial
None

## Nice-to-Haves
- Add a failure mode analysis: when does LCG over-mask or produce worse translations? What happens in adversarial scenarios with frequent legitimate code-switching?
- Report training hyperparameters (learning rate, epochs, MLP hidden dimensions) in the main text rather than only appendix for reproducibility.
- Analyze how much of LCG-unadjusted's failures are caused by norm bias vs. other factors (e.g., measuring what fraction of intervened tokens have higher norms than the correct tokens) to strengthen the mechanistic narrative.

## Removed Points
These points are flagged to be removed, treat them with caution:
- "Missing training details in main text" — deferred to appendix, which is standard practice; main text provides dataset composition and loss formulation.
- "Table 4 header says No-Think when it should say Thinking" — parser artifact, not an author error. The paper correctly says "Effectiveness of LCG Intervention on 'No-Think' Models measured on Humaneval-XL" which is likely a copy-paste from Table 3 but the data is for thinking models.
- "Code-switch rate comparison with Claude Sonnet 4 is circular" — the paper explicitly acknowledges these are "just references for comparison but not a ground truth optimal code-switch rate" (line 286) and provides the more informative 86.7% token-level preservation metric.
- "Norm-adjustment not fully validated as mechanism" — the ablation in Table 3 does validate it; deeper analysis would strengthen but is not a weakness.
- "Section 3.2 acknowledgment undermines framing" — the paper honestly notes norm bias "cannot fully explain language confusion" (line 155), which is good scientific practice.
- "Training hyperparameters and top-k/p parameters for pseudo-targets not discussed" — reasonable to defer to appendix given paper length constraints.
- "No evaluation of cross-LowRes confusion" — this is inherent to the method's design and acknowledged; not a flaw but a scope limitation.

## Novel Insights
The norm-bias decomposition (logit_i = ||h|| · ||e_i|| · cos_sim(h, e_i)) and its systematic quantification across 5 models (Table 1) provides a genuinely novel mechanistic lens on language confusion. The key non-trivial insight is that norm-adjustment during self-distillation *training* (not just at inference time) produces a more accurate gate—connecting the geometric insight to a practical training technique. The observation that confusion tokens are top-1 56.74% of the time while correct tokens are in top-3 99.29% is also a useful empirical contribution that precisely motivates logit-masking over other approaches.

## Suggestions
- Add direct comparisons against Nie et al. (2025) and Ji et al. (2025), even if limited to a subset of models. If implementations are not available, discuss expected performance differences based on the methods' mechanisms.
- Report standard errors or run 3–5 seeds, especially for the low-rate CJ confusion results where absolute differences are small.
- Qualify "order of magnitude" in the abstract to note this applies primarily to CJ confusion.
- Add a brief failure mode or error analysis section.

## Score and Decision

### Calibration Anchors
| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Llamas think in English | fSbPwHjdDG | 3.00 | 1 | Mechanistic interpretability, single task, poor presentation. LCG clearly stronger. |
| Crosslingual Capabilities | BCyAlMoyx5 | 5.67 | 1 | Multilingual study with narrower scope and weaker evaluation. LCG has stronger methodology. |
| Babel Tower | eznTVIM3bs | 5.25 | 1 | Multilingual analysis with narrower scope. LCG clearly more complete and practical. |
| MLLM can see? DeCo | 4z3IguA4Zg | 6.00 | 1 | Similar inference-time decoding intervention, comparable quality. LCG has broader model coverage and more novel insight. |
| SADI | 8WQ7VTfPTl | 6.40 | 2 | Inference-time activation intervention, very similar profile. LCG comparable in novelty, broader evaluation (7 vs 4 models). SADI has slightly more theoretical framing. |
| Token-Aware ITI | af2ztLTFqe | 6.00 | 2 | Inference-time intervention with narrower evaluation. LCG has more comprehensive results. |
| DEPT | vf5aUZT0Fz | 8.00 | 1 | Pre-training framework with fundamental contributions. LCG is more applied/incremental. |

**Round 1 bracket:** 5.5–7.0 (LCG clearly above weak papers at 3.0 and 5.25, clearly below strong papers at 8.0)
**Round 2 narrowing:** 6.0–6.5 (comparable to SADI at 6.40 and TA-ITI at 6.00 in profile; LCG has cleaner insight and broader evaluation than both but missing key baselines holds it back)

**Final positioning:** The LCG paper offers a clearer mechanistic insight and broader model coverage than comparable inference-time intervention papers scoring 6.0–6.40, but the missing comparisons against the two most relevant prior methods and the lack of statistical reliability prevent scoring higher. This lands at 6.0—a solid paper that warrants acceptance with revisions to address the missing baselines and add statistical support.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>