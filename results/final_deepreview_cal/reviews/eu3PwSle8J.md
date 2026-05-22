Now I have sufficient context. Let me produce the final consolidated review.

## Summary

This paper proposes Augmented Intermediate Representations (AIR), a method for enforcing instruction hierarchy (IH) in LLMs by injecting trainable privilege-level embeddings at every decoder layer, rather than only at the input layer (as done by existing methods Delim and ISE). The core insight is that input-only IH signals degrade as they propagate through the network, and injecting them at each layer preserves better separation. Experiments across three models (3B–8B), two training methods (SFT, DPO), and multiple attack types (static, GCG, Astra, SEP) show AIR consistently achieves lower attack success rates than prior methods, with 1.6×–9.2× reduction on gradient-based attacks and minimal utility degradation (<2% win rate drop).

## Strengths

- **Well-motivated architectural insight with diagnostic evidence.** Figure 3 empirically validates the paper's motivating hypothesis — that input-level IH signals degrade as they propagate through deeper layers — by showing that cosine similarity between privilege-level representations increases across layers for Delim and ISE, while AIR maintains lower similarity throughout. This diagnostic evidence directly supports why layer-wise injection should be more effective.

- **Consistent and substantial robustness improvements across diverse settings.** Table 1 shows that AIR achieves the lowest or tied-lowest ASR on every model × training method × attack combination. On GCG attacks, the improvement over the next-best defense ranges from ~1.6× (Qwen-2.5-7B SFT: 22.6% vs ISE 36.6%) to ~9.2× (Llama-3.2-3B SFT: 4.1% vs Delim 38%). On Astra, AIR achieves near-zero ASR on multiple settings (e.g., 0.1% on Llama-3.2-3B SFT, 0.1% on Llama-3.1-8B SFT).

- **Minimal utility degradation with negligible parameter overhead.** Figure 6 shows AIR win rates on AlpacaFarm are within <2% of the non-adversarial baseline across nearly all settings (e.g., Llama-3.1-8B DPO: AIR 87.1% vs None 89.5%). The parameter overhead is only ~0.4M parameters for a 8B model (0.005% increase), making the approach practical.

- **Comprehensive evaluation covering multiple dimensions.** Experiments span 3 model families (3B–8B), 2 training methods (SFT, DPO), 4 static attacks, 2 gradient-based attacks (GCG, Astra), and the SEP benchmark. AIR consistently outperforms baselines or matches the best, providing strong evidence of generalizability.

## Weaknesses

### Major

- **GCG/Astra ASR is measured via logit-likelihood proxy, not actual generation, with no stated threshold.** The paper states gradient-based attack ASR is "measured using the likelihood (from model's logits) of generating the target phrase 'hacked!'" (Section 5.4), with no threshold specified for binarizing likelihood into success/failure. For static attacks, ASR is measured by actual decoded output (string match). This inconsistency means the headline 1.6×–9.2× reduction claim rests on a metric whose relationship to real-world attack success is not validated. While logit-likelihood is correlated with generation probability, the missing threshold and lack of decoded-output verification are a genuine evidential gap. This is a **Major** issue because it weakens confidence in the paper's central quantitative claim. The authors should (a) specify the threshold and justify it, and ideally (b) report ASR based on actual generation as well.

### Minor

- **No ablation isolating the effect of layer-wise injection from increased parameter count.** AIR adds ~0.4M trainable parameters across all layers (0.005% of model). The baselines (Delim, ISE) also add parameters (trainable tokens/embeddings at the input), but fewer. The paper attributes AIR's improvement to the layer-wise injection mechanism, but does not control for the possibility that additional trainable capacity — even if tiny — partly contributes. An ablation that adds comparable extra trainable embeddings at the input layer only (or increases ISE's embedding dimension) would strengthen the mechanistic claim. The effect is likely small given the 0.005% overhead, but the absence of this control is a methodological gap.

- **Limited GCG optimization budget without convergence analysis.** GCG attacks run only 50 steps (SFT) or 200 steps (DPO). Figure 7 shows loss curves for AIR are still decreasing at the final step for several settings (e.g., Llama-3.1-8B DPO). While Delim and ISE curves are also still decreasing and AIR maintains a gap throughout, the paper does not demonstrate that the gap persists after convergence. Longer attack trajectories (e.g., 500–1000 steps) would substantiate the robustness claim.

- **The "up to 145×" Astra claim is technically correct but gives an inflated impression without absolute context.** The 145× figure comes from a single cell (Llama-3.2-3B SFT: Delim 14.5% / AIR 0.1%), but in several other settings the improvement is much more modest (e.g., Llama-3.1-8B SFT: ISE 0.2% vs AIR 0.1%, a 2× reduction). The paper reports "up to" which is accurate, but the factor claim would benefit from reporting absolute ASR values alongside and explicitly noting the range of improvements across settings.

- **Diagnostic analysis (Figure 3) shown for only one model.** The cosine similarity analysis motivating AIR is only shown for Llama-3.2-3B. Replicating across other models would strengthen the claim that input-level IH degradation is a general phenomenon.

### Trivial

- The paper states AIR trains "without significantly degrading the model's utility" (abstract). While generally true, Figure 8 shows that for some SFT settings (e.g., Qwen-2.5-7B SFT, Llama-3.1-8B SFT), AIR's SEP utility score is lower than the *None* baseline. The paper acknowledges this in Section 6.2 but the abstract's phrasing could be qualified to reflect this nuance.

- The DPO stage uses LoRA while the SFT stage uses full fine-tuning (Section 5.2). This asymmetry prevents clean comparisons between SFT and DPO results, though the paper's main comparisons (across injection methods within each training approach) are unaffected.

## Nice-to-Haves

- Evaluation against adaptive attacks that specifically target the added layer embeddings (as the critic notes, standard GCG/Astra are effectively adaptive since gradients flow through AIR, but a tailored attack targeting the embeddings directly could be informative).
- Analysis of the learned layer embeddings (visualization, similarity across layers) to provide insight into what privilege information they encode.
- Reporting of inference latency impact (the paper states it's "negligibly small" but does not quantify it).
- Evaluation on longer adversarial prefixes or different attack configurations.

## Removed Points

These points were surfaced in the inputs but are excluded from the main review as invalid, speculative, or already addressed:

- **"Overclaiming on Astra results — 145× is cherry-picked."** The 145× figure is verifiably correct for Llama-3.2-3B SFT (Delim 14.5% / AIR 0.1% = 145). The paper says "up to 145×," which is an accurate characterization of the maximum across settings. The harsh critic's calculation of "29" for Qwen-2.5-7B is itself incorrect (69.0/2.4 ≈ 28.75, not ~29, and that's still a large number). The critic misread the table for Llama-3.1-8B SFT (next best is ISE at 0.2, not Delim). This criticism is factually inaccurate.

- **"Figure 3 motivation — similarity increase for AIR from ~0.55 to ~0.88 still shows substantial mixing."** Figure 3 is a diagnostic showing relative comparison: AIR consistently maintains lower cosine similarity than ISE across all layers. The claim is not that AIR achieves perfect separation, but that it preserves more separation than alternatives, which the data supports.

- **"All three IH methods achieve near-zero ASR on static attacks — advantage only appears under gradient-based attacks."** This is a correct observation about the results, not a weakness. The paper's contribution is specifically about improving gradient-based attack robustness, which is a meaningful and harder problem.

- **"Utility degradation characterization."** The paper acknowledges the degradation in Section 6.2 and the <2% drop on AlpacaFarm is accurately characterized.

- **Formatting/style nitpicks** — excluded per hard rules.

## Novel Insights

The key insight that input-level IH signals degrade as they propagate through decoder layers (validated via cosine similarity analysis and the AIR method's layer-wise injection) draws a clean analogy to the evolution of positional embeddings from input-only (sinusoidal/learnable) to layer-wise (RoPE). The paper is the first to apply this principle to security — showing that privilege information, like positional information, benefits from being reinforced at every layer. This framing could influence future work on embedding other types of structural signals throughout LLM architectures for security purposes.

## Suggestions

1. **Report actual decoded ASR** for gradient-based attacks alongside the logit-likelihood metric, and specify the binarization threshold.
2. **Run GCG attacks for longer** (e.g., 500–1000 steps) on at least one model to demonstrate that AIR's advantage persists after convergence.
3. **Add a parameter-count ablation** by training an ISE variant with comparable total trainable parameters (e.g., larger input embeddings or multiple input-level tables) to isolate the effect of layer-wise injection.
4. **Replicate the cosine similarity diagnostic** (Figure 3) on at least one additional model to show the degradation pattern is general.

## Score and Decision

**Calibration summary:**

| Anchor | Avg Score | Round | Comparison to this paper |
|--------|-----------|-------|------------------------|
| 3MDmM0rMPQ (Inverse Prompt Engineering) | 3.00 | R1 | Much weaker — very limited evaluation, unclear contribution |
| KyKTjRtyNG (Incremental Exploits) | 3.00 | R1 | Much weaker — jailbreak attack, not defense |
| 5kMwiMnUip (NEMESIS) | 1.40 | R1 | Much weaker — low-quality jailbreak paper |
| lUyYX9VFgA (Code-of-Thought Prompting) | 3.00 | R1 | Much weaker — unrelated safety probing |
| l3bUmPn6u5 (PFT) | 4.25 | R2 | Weaker — limited attack evaluation, unclear problem scope, fewer models |
| INXZOxYsLd (Safeguard User Privacy) | 4.83 | R1 | Different topic, lower quality |
| V01FPV3SNY (RA-LLM) | 5.33 | R2 | Weaker — limited evaluation, computational concerns, less clean contribution |
| PNHGYziAsL (SPIN) | 5.50 | R2 | Comparable — similar topic but different approach; SPIN evaluated on fewer models (2), this paper has cleaner architectural contribution |
| iKgQOAtvsD (Deciphering the Chaos) | 5.75 | R2 | Different topic (attack, not defense) |
| kUH1yPMAn7 (Safety Layers) | 6.00 | R1 | Comparable — similar quality and evaluation scope; different topic |
| s20W12XTF8 (Jailbreak Antidote) | 6.25 | R2 | Slightly stronger — evaluated on more models (9) and attacks (10), but this paper has a cleaner architectural contribution |
| 7erlRDoaV8 (Can Sensitive Information Be Deleted) | 7.50 | R2 | Stronger — more thorough evaluation and analysis; different topic |
| syThiTmWWm (Cheating LLM Benchmarks) | 7.75 | R3 | Different topic, stronger evaluation |

**Round 1 bracket**: between ~4.5 and ~7.0 (paper is clearly stronger than the weak-anchor band and clearly weaker than top-tier papers with comprehensive evaluation).

**Round 2 narrowing**: anchored primarily against PFT (4.25, weaker), SPIN (5.50, comparable), Safety Layers (6.00, comparable), and Jailbreak Antidote (6.25, slightly stronger). The paper has a cleaner contribution than SPIN, with more consistent results than Safety Layers, but fewer models attacked than Jailbreak Antidote.

**Final score**: 6.0 — A solid paper with a well-motivated, clean architectural contribution, consistently positive results across models and training methods, and minor evidential gaps (ASR metric, convergence analysis, parameter count ablation) that are addressable and do not undermine the core claim.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>