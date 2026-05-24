## Summary

This paper investigates how compression methods (quantization, distillation, pruning) affect the reasoning capabilities of large reasoning models (LRMs), focusing on DeepSeek-R1 and its distilled variants. It combines broad performance benchmarking across four diverse reasoning tasks with a mechanistic interpretability approach that computes per-linear-module importance scores using steering vectors and gradient-based attribution. The key practical finding—validated through selective protection experiments—is that current quantization methods systematically under-protect the final-layer MLP modules, and preserving just ~2% of weights in full precision improves 3-bit average accuracy by 6.57%.

## Strengths

- **Comprehensive benchmarking across compression strategies.** The paper evaluates eight compression approaches (dynamic quantization, distillation, SparseGPT, AlphaPruning, AWQ, GPTQ, GPTAQ, ANY4/3) on four reasoning datasets at multiple bit-widths and sparsity levels. Tables 1 and 2 provide a rare comparative picture of collapse points and task-difficulty effects across all three major compression paradigms.

- **Fine-grained mechanistic finding with empirical validation.** The importance score analysis identifies `mlp.up_proj` in the final layer as the most critical component across both Llama-8B and Qwen-7B distilled models. This is validated in Table 3: quantizing only that single matrix (0.7% of weights) to 3-bit reduces average accuracy by 16.3%, confirming its outsized role.

- **Actionable bottleneck discovery with a practical remedy.** The importance-shift heatmaps (Figures 3, 6, 7) reveal that AWQ and GPTQ both excessively compress final-layer MLP modules and gate projections. The protective experiment in Table 4—keeping only the final-layer MLP modules in 16-bit during 3-bit AWQ—raises average accuracy by 6.57%, outperforming all 3-bit baselines in Table 1 by substantial margins. This is the paper's most compelling piece of evidence.

- **Clear finding that distillation, not the base model, creates reasoning-critical weights.** The lower panel of Figure 2 (and Figure 5 for Qwen) shows that the important modules in the distilled model are products of SFT fine-tuning, not inherited from the original Llama-3.1-8B. This explains why these weights deserve special treatment during subsequent compression.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The importance score is a linear approximation that lacks direct empirical validation against its claimed foundation.** The paper calls the score an adaptation of attribution patching (Syed et al., 2023), but the standard technique replaces activations with corrupted versions and measures loss change. What the paper computes (Eq. 2) is the absolute dot product of a steering vector with the gradient of the loss w.r.t. activations—a first-order Taylor approximation whose accuracy relative to actual activation patching is never measured. The selective quantization experiments (Table 3) provide orthogonal validation, but they validate whether the identified modules are important, not whether the importance *scores* accurately quantify causal contribution. A correlation analysis against actual activation patching or steering-vector intervention would substantially strengthen the method's credibility.

- **The mechanistic analysis is confined to 7B/8B models while generalization claims are made broadly.** All steering vector extraction, importance scoring, and validation experiments are conducted on DeepSeek-R1-Distill-Llama-8B and DeepSeek-R1-Distill-Qwen-7B. The paper repeatedly asserts that findings generalize "across both R1 and non-R1 LRMs" and "across model families," but evidence from larger distilled models (32B, 70B) is deferred to Appendix J (not visible in the submitted main text). The cross-model replication across Llama and Qwen at the 7B/8B scale provides some evidence, but the claim that the final-layer `up_proj` finding applies to all LRMs is not fully substantiated by the presented experiments.

- **The importance-shift analysis only visualizes decreases, which limits interpretability of the redistribution.** The paper sets all increases in relative importance to zero on the grounds that relative importance sums to one, so increases merely offset decreases (Section 2.3). While this is technically correct for relative values, a decrease in relative importance for a module could arise because (a) its absolute importance genuinely dropped, (b) another module's absolute importance rose, or (c) the total variance changed. Without reporting absolute importance values or including the full redistribution, the "over-compression" interpretation of the heatmaps rests on the assumption that relative decreases correspond to genuine degradation—an assumption the paper does not verify.

- **The knowledge-vs-reasoning claim is observational rather than experimentally isolated.** The finding that "weight count has a greater impact on LRMs' knowledge memorization than their reasoning capabilities" is inferred from MuSiQue (closed-book) scores dropping more sharply than AIME/FOLIO/Temporal under smaller models and pruning. This is a reasonable interpretation of the data, but no experiment isolates knowledge retention from multi-step reasoning (e.g., probing factual recall independently, or using the same questions with and without retrieval). The claim is stated more strongly than the experimental design warrants.

- **The 1_up anomaly in Table 3 weakens the ranking-to-accuracy correlation.** While the overall component rank correlates with accuracy drops, quantizing `1_up` (ranked lowest among up_proj layers) yields the worst AIME score at 6.7%, below even the top-ranked `32_up` at 20.0%. The paper acknowledges this but does not explore why the lowest-ranked component produces the steepest drop on the hardest benchmark, leaving a gap in the validation narrative.

### Trivial

None.

## Nice-to-Haves

- Validating the importance score against actual activation patching (replacing activations with those from a run on a corrupted or different input) and reporting the correlation would transform the method from an unverified approximation into a properly grounded attribution tool.
- Running the interpretability pipeline on at least one larger distilled model (32B or 70B) would substantially strengthen the generalization claim.
- An experiment that directly evaluates factual recall under the same compression regimes, decoupled from multi-hop reasoning, would firm up the knowledge-vs-reasoning claim.
- A robustness analysis of steering vectors to the small annotation dataset (120 examples, GPT-4o labeled) would address sensitivity concerns.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic claim that the importance score formula is unexplained or unmotivated.** The formula in Eq. 2 is a standard first-order sensitivity measure (directional derivative of the loss), and the paper explicitly states it is an adaptation. This criticism overstates the gap. Removed as a fatal/major claim; retained in weakened form as a minor weakness about missing empirical validation.

- **Harsh critic claim that the protective experiment baseline (3-bit AWQ) is not representative.** The paper runs 3-bit AWQ with default calibration data and compares against the same method with protection—the internal comparison is clean. The paper also compares the protected model against other 3-bit methods from Table 1 (GPTQ, GPTAQ, ANY3), which use different base quantizers. While not perfectly matched, this is a reasonable comparison given that the goal is to show the protected model outperforms existing 3-bit approaches, not to isolate the quantizer effect. Removed.

- **Harsh critic demand for controlled experiment isolating knowledge from reasoning.** This is partially a scope concern—the paper's contribution is primarily about locating important weights for reasoning, and the knowledge claim is a secondary observation. Retained as minor, but the critic's framing as a fatal flaw is removed.

- **Harsh critic claim that the paper should acknowledge limitations about model size, approximation, and observational nature.** The paper does not have a limitations section. This is a fair observation but not a weakness per se; many papers in this area omit formal limitations sections. Moved to Nice-to-Haves implicitly.

- **Strength Finder claim that the paper demonstrates generalization across non-R1 models.** The generalization claim is not demonstrated in the main text (deferred to Appendix J). This strength is weakened accordingly.

- **Harsh critic claim about the interpretation of "greatly surpassing state-of-the-art" being weak.** The protected model (avg 52.57) does outperform all 3-bit baselines in Table 1 (best 3-bit avg for Llama-8B: GPTAQ at 43.5, a gap of ~9 points). The claim is numerically accurate. Removed.

## Novel Insights

The paper offers a genuinely useful integration of mechanistic interpretability with compression analysis: rather than treating compression methods as black boxes and only measuring final accuracy, it uses steering-vector-based importance scores to trace *which specific weight matrices* are degraded by each compression strategy. The finding that both AWQ and GPTQ independently converge on over-compressing the same modules (final-layer MLP and gate projections) suggests a systematic blind spot in current quantization methods that is independent of the specific algorithm. This approach—using interpretability to diagnose compression failures rather than just to explain model behavior—is a promising direction that could inform future compression algorithm design.

## Suggestions

- Add a direct empirical comparison between the gradient-dot-product importance score and actual activation patching (or steering vector intervention) on a subset of modules, reporting correlation. This single experiment would substantially strengthen the paper's core methodology.
- Include a brief limitations subsection acknowledging the model-size restriction for interpretability experiments and the approximate nature of the importance score.
- Consider reporting at least one larger-model interpretability result (even if partial) in the main text rather than relying entirely on the appendix for the generalization claim.

## Score and Decision

**Calibration anchors consulted:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| LOLAMEME (73dhbcXxtV) | 3.00 | R1 bracketing | Much weaker; thin evaluation, unclear contribution |
| Mind Scramble (KBixkDNE8p) | 3.00 | R1 bracketing | Much weaker; exploratory, limited validation |
| Pruning via Ranking (rO62BY3dYc) | 3.75 | R1 bracketing | Weaker; narrow pruning method, limited scope |
| PALMBENCH (xzSUdw6s76) | 5.80 | R2 narrowing | Weaker; pure benchmarking, no mechanistic analysis |
| LLM Pruning & Distillation (mMmzHS28ht) | 5.00 | R2 narrowing | Weaker; incremental method, limited novelty |
| LLM-KICK (B9klVS7Ddk) | 6.75 | R2 narrowing | Closest comparison; similar benchmarking scope but no mechanistic interpretability. This paper adds interpretability but has methodological gaps LLM-KICK avoids |
| Function Vectors for CF (gc8QAQfXv6) | 9.00 | R1 bracketing | Much stronger; rigorous theory, thorough validation, novel training method |
| Sparse Feature Circuits (I4e82CIDxv) | 8.00 | R1 bracketing | Much stronger; novel interpretability method with downstream applications |
| Retrieval Heads (EytBpUGB1Z) | 8.00 | R1 bracketing | Much stronger; clean mechanistic finding with broad validation |

**Round 1 bracket:** Between 5.5 and 7.5. The paper is clearly above the 3.0–5.0 range (weak benchmark-only or incremental papers) and clearly below the 8.0–9.0 range (highly novel mechanistic interpretability contributions with rigorous validation).

**Round 2 narrowing:** The closest anchor is LLM-KICK (6.75), which benchmarks compression methods on knowledge-intensive tasks. The paper under review is comparably comprehensive in benchmarking and adds mechanistic interpretability with a validated protective remedy. However, the interpretability methodology has gaps (unvalidated linear approximation, limited model scope, debatable importance-shift visualization choices) that LLM-KICK—a cleaner, purely empirical paper—does not face. The paper under review is more ambitious but less methodologically tight. I assess it as slightly below LLM-KICK overall, landing at **6.5**.

The protective experiment (Table 4) and the selective quantization validation (Table 3) are genuine contributions that distinguish this work from a pure benchmark. However, the mechanistic interpretability component—which the paper positions as its core contribution—would benefit from stronger methodological grounding before the claims can be considered fully reliable.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>