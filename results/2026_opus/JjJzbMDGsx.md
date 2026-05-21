Now I have enough context to write the final review.

## Summary
The paper proposes the Language Confusion Gate (LCG), a two-layer MLP attached to a frozen LLM that classifies which of four language families (CJ, Latin, Symbols, Low-Res) are permissible at each decoding step and masks the disallowed logits. The gate is trained by norm-adjusted self-distillation, using the model's own top-k/p tokens (debiased against output-embedding norm) as pseudo-labels. Across Qwen3, Llama3.1, Gemma3, and GPT-OSS, LCG reduces CJ/Latin confusion roughly an order of magnitude on FLORES-NO-LATIN, INCLUDE, and HumanEval-XL with negligible BLEU/accuracy/Pass@1 cost and ~0.4% latency overhead.

## Strengths
- **Mechanistic norm-imbalance observation (Sec 3.2 / Table 1).** The decomposition `logit = ‖h‖·‖e‖·cos_sim` and the per-model statistics showing the top-5% norm bucket dominated by Latin/CJ tokens give a concrete, evidence-based explanation for a systematic bias toward high-resource scripts. Figure 2 demonstrates the bias removal on a real Qwen3-8B Hebrew → CJ confusion case.
- **Empirically strong cross-model reductions.** Table 3 shows order-of-magnitude drops in confusion rates (e.g., Qwen3-30B Latin 4.4%→0.4%, Qwen3-8B Latin 12.1%→2.0%) without BLEU/accuracy regressions on FLORES-NO-LATIN and INCLUDE.
- **Norm adjustment ablation is real.** LCG-adjusted consistently beats LCG-unadjusted in Table 3 (e.g., Llama3.1 Latin 5.7% → 2.9%; Qwen3-8B CJ 0.5% → 0.1%), substantiating the central claim that the norm-adjusted distillation signal helps the gate.
- **Practical deployment story.** Measured 0.4% latency overhead in a production-style configuration (Sec 6, 2000-token prompt × 100-output × concurrency 8), plus a sparse intervention rate (~0.33–0.38% of tokens), make the method genuinely deployable.
- **Top-k locality result motivating logit masking (Sec 3.1).** The 99.29% top-3 coverage of language-consistent tokens directly motivates masking-based intervention without weight modification.

## Weaknesses

### Fatal
None.

### Major
- **The 4-class taxonomy collapses every non-CJ/non-Latin script into a single "Low-Res" bucket, and the evaluation only probes confusion that this taxonomy is structurally able to catch.** Section 4.1 defines exactly four classes (CJ, Latin, Symbols, Low-Res); FLORES-NO-LATIN targets Arabic/Hebrew/Korean/Thai, INCLUDE targets Arabic/Hebrew/Greek/Russian/Vietnamese, and HumanEval-XL is Arabic/Hebrew — every target sits in Low-Res, and the "erroneous" scripts being measured are CJ and Latin. So the headline order-of-magnitude reductions are for exactly the cases the gate can in principle distinguish. The paper acknowledges this only as a single sentence of future work in Sec 6 ("the gate cannot resolve more nuanced confusion between languages that share the same script... or between two different low-resource languages"). The framing in the abstract and intro ("LCG decreases language confusion significantly") is broader than what is tested, and the limitation is structural to the labeling pipeline rather than a future-work footnote.
- **The closest published baselines from related work are not compared against.** Sec 2 explicitly identifies Nie et al. (2025) language-switching-neuron suppression and Ji et al. (2025) post-hoc Chinese-token smoothing as inference-time interventions, but Sec 5.3 / Figure 3 only compares against ICL, greedy decoding, and an authors-reproduced ORPO. ICL and greedy are very weak baselines, and the ORPO degradation claim ("INCLUDE accuracy drops from 61.4 to 57.3") is against a locally synthesized ORPO setup, not the original Lee et al. configuration — so the "more targeted and effective than … decoding-based interventions" conclusion is not really tested against the most relevant decoding-based interventions.

### Minor
- **Norm-bias story does not cleanly apply to Gemma3-12B and GPT-OSS.** Table 1 shows Gemma3-12B has CJ at 0.94% in the top-5% norm group (below Low-Res at 2.40%) and GPT-OSS has 0.00% CJ in that bucket. The mechanistic figure (Fig 2) is a Qwen3-8B-specific demonstration. Yet the same norm-adjusted pipeline is applied uniformly and LCG-adjusted still beats LCG-unadjusted on these models. The paper would be stronger with a parallel analysis showing why the method still helps where the proposed mechanism is weakest. The paper itself partly acknowledges this in Sec 3.2 ("Norm bias can account for a subset of such errors but cannot fully explain language confusion"), but does not audit how often the pseudo-label signal is correct on models where the mechanism is weak.
- **Code-switch suppression cost is real and slightly underweighted.** Table 5 shows Qwen3-8B's Latin rate on FLORES-WITH-LATIN drops from 46.34% to 25.90% — below the ground-truth answer rate (38.36%). The token-level 86.7% allow rate means 13.3% of human-validated legitimate code-switch tokens are blocked. The paper frames this as "moderation," but the post-intervention rate sits below the reference distribution rather than between it and the baseline. A small Pareto curve across the gate's confidence threshold would let readers pick an operating point.
- **Pass@1 consistently dips on thinking models without variance estimates (Table 4).** Qwen3-8B 83.81→83.13, Qwen3-30B 91.25→90.50, GPT-OSS 85.88→84.56. With 10× repeated prompts per problem, variance should be reportable; the "competitive Pass@1" framing is honest in magnitude but the direction is uniformly down.
- **Persistence-of-previous-language rule is not separately ablated.** Sec 4.3 lists three intervention rules but Figure 3's "No Rule" condition removes all of them together, so the contribution of each individual rule (especially the persistence rule, which does meaningful work for coherence) is not identifiable.
- **Top-3 99.29% feasibility statistic is measured on Qwen3-8B only (Sec 3.1).** The same pipeline is applied across models with very different norm-imbalance profiles. A per-model version of this measurement would tighten the case that the method's basic premise holds everywhere it is applied.

### Trivial
- The category labeling pipeline conservatively classifies BPE-ambiguous tokens as "Symbols" (Sec 4.1 / Appendix A). It is worth surfacing how many vocab tokens end up in this fallback bucket per tokenizer, since misclassified Symbols tokens cannot be masked by Rule (1).

## Nice-to-Haves
- A direct gate-accuracy report at confusion points (precision/recall of the 4-way label conditioned on a true confusion) would convert "it works" into "it works for the stated reason."
- Even an exploratory single-pair language-specific head (e.g., Arabic vs. Hebrew on the same self-distillation principle) would meaningfully extend the contribution along the axis the paper itself identifies as the main limitation.
- A reasoning-mode code-switch analysis (English jargon inside Chinese reasoning chains, etc.) would mirror the FLORES-WITH-LATIN analysis for thinking models.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"ORPO comparison uses authors' own reproduction"** — kept in Major as part of the "missing closest baselines" point. The standalone framing as a separate weakness was duplicative.
- **"Norm story coherence gap = method may train the gate to allow the script it later masks"** (from harsh critic): this is speculative — the paper does not audit pseudo-label noise rate, but Table 3's LCG-adjusted > LCG-unadjusted result is empirical evidence the signal is net positive. Demoted from a critical issue to the Minor "norm story does not cleanly apply to Gemma3/GPT-OSS" point.
- **Generic strength: "Comprehensive evaluation across diverse models and modes"** — kept implicitly but not as a standalone strength bullet; the cross-model evaluation matters mainly via Table 3, already covered.
- **Generic strength: "Principled handling of legitimate code-switching"** — partially conflicts with the verified code-switch-suppression weakness (FLORES-WITH-LATIN drops below the answer rate); the weakness wins, so this is dropped from the headline strengths.

## Novel Insights
None beyond the paper's own contributions. The most original observation — that output-embedding-norm imbalance systematically biases high-resource scripts and that dividing by ‖eᵢ‖ debiases the top-k for distillation — is the paper's own contribution and is well-evidenced in Table 1 and Figure 2.

## Suggestions
- Tighten the abstract/intro to scope claims to script-family confusion rather than "language confusion" generically; surface the four-class limitation up front rather than as a Sec 6 footnote.
- Add at least one comparison against a re-implementation of Nie et al. (2025) neuron-suppression and Ji et al. (2025) post-hoc smoothing on the same models and benchmarks.
- Provide variance bars on Pass@1 and INCLUDE accuracy across the 10× repetitions to determine whether the small dips are within noise.
- Per-rule ablation of the three intervention rules in Sec 4.3, in addition to the current "No Rule" sweep.
- Report gate precision/recall at confusion points (not just downstream confusion rate) and per-model versions of the Sec 3.1 top-3 statistic.
- An exploratory same-script gate (e.g., Spanish vs. English, or Arabic vs. Hebrew/Persian) would directly answer the most-cited limitation.

---

**Axis-by-axis assessment.** *Originality:* the norm-imbalance observation and norm-adjusted self-distillation are genuinely novel and well-grounded; the gate itself is engineering. *Importance:* mid-to-high — language confusion is a real production problem in widely deployed multilingual LLMs, and a lightweight plug-in fix has clear utility. *Claim support:* good for the four-class confusion the method is designed to address, weaker for the broader "language confusion" framing in the abstract. *Soundness of experiments:* solid breadth across models and tasks; missing variance, missing closest baselines, no per-rule ablation. *Clarity:* clean prose, well-structured tables, mechanism explained clearly. *Value to the community:* concrete and deployable, with measured production-system overhead; the main contribution is bounded but real.

**Calibration anchors retrieved:**

| Path | Avg | Round | Comparison to this paper |
|---|---|---|---|
| fSbPwHjdDG.md (Llamas think in English) | 3.00 | R1 | Weaker — speculative interpretability, this paper has clear engineering wins. |
| KBixkDNE8p.md (Mind Scramble) | 3.00 | R1 | Weaker — limited contribution, this paper is more grounded. |
| 4y3GDTFv70.md (Latent Space Theory) | 3.25 | R1 | Weaker — abstract theory, this paper is concrete. |
| uOnElfFuey.md (LaMFA) | 3.00 | R1 | Weaker — narrow setting, less practical. |
| BCyAlMoyx5.md (Crosslingual Knowledge Barriers) | 5.67 | R1 | Comparable scope; this paper has more concrete engineering deliverable. |
| NCrFA7dq8T.md (Same but Different) | 6.60 | R1 | Comparable — multilingual interpretability with clean experiments; this paper has more practical impact but narrower analysis. |
| eznTVIM3bs.md (Babel Tower) | 5.25 | R1 | Similar level; this paper has stronger empirical reductions. |
| FrFQpAgnGE.md (Unified Representation Space) | 7.00 | R1 | Stronger conceptual contribution than LCG's engineering one. |
| vf5aUZT0Fz.md (DEPT) | 8.00 | R1 | Stronger — broader systems contribution. |
| tyEyYT267x.md (SAR diffusion LMs) | 8.00 | R1 | Stronger — novel methodology with broader impact. |
| SPS6HzVzyt.md (Context-Parametric Inversion) | 8.00 | R1 | Stronger — important new phenomenon documented. |
| I4e82CIDxv.md (Sparse Feature Circuits) | 8.00 | R1 | Stronger — broader interpretability methodology. |
| 0KHW6yXdiZ.md (Logits Watermarking) | 5.25 | R2 | Comparable — logit-level intervention; LCG has cleaner motivation and stronger evaluation. |
| 8WQ7VTfPTl.md (SADI activation intervention) | 6.40 | R2 | Closest analog — also inference-time intervention with steering; comparable methodological depth, LCG has cleaner production-system numbers. |
| NgCNMlTXx9.md (HiddenGuard) | 5.25 | R2 | Comparable — also a gate/router approach; LCG has stronger and more diverse empirical results. |
| jY5oml9fe9.md (SASA Self-Detoxifier) | 6.00 | R2 | Very close analog — lightweight controlled decoding for a related steering problem; LCG broader empirical sweep, similar scope. |
| 8wjWm5jr1w.md (Multi-Granularity Distillation) | 6.00 | R2 | Comparable — distillation contribution. |
| uZ5K4HeNwd.md (Self-Distillation Through Time) | 7.00 | R2 | Stronger — novel paradigm with broader implications. |
| CP6CAqxAGJ.md (UnifyVocab) | 5.67 | R2 | Comparable — practical vocab/tokenization-related contribution. |
| zl3pfz4VCV.md (MMTEB) | 7.00 | R2 | Stronger — community benchmark with broad utility. |

**Round-1 bracket:** between 5.0 and 7.0.
**Round-2 narrowing:** the closest analogs are SADI (6.40, accept) and SASA (6.00, accept) — both inference-time intervention papers. LCG has stronger empirical reductions (order-of-magnitude) and a cleaner production-system overhead claim, but bounded scope (script-level only) and missing closest-prior-work baselines. This places it around the SADI/SASA cluster, slightly below SADI because of the missing direct comparisons and the taxonomy-evaluation alignment issue. Final score: 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>