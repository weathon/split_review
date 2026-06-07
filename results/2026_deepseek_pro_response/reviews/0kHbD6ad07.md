Now I have a clear picture. Let me finalize the review.

**Bracket from Round 1:** 5.5–7.0 (between "Language Model Inversion" at 5.50 and "Understanding Factual Recall" at 7.33)

**Round 2 narrowed:** The paper is comparable to "Training Nonlinear Transformers for CoT" (6.50) and "Scaling Laws for Adversarial Attacks on LM Activations" (6.50), both of which have strong contributions with notable limitations. Our paper's theory is more general than the CoT paper's (arbitrary-depth vs. single-layer) and has more extensive empirics, but the algorithmic evaluation is thin. It sits below "Understanding Factual Recall" (7.33) because that paper's theoretical depth (storage capacity scaling laws) exceeds this paper's, and its contributions are more tightly integrated. The paper is clearly above "Language Model Inversion" (5.50) which had weaker theory and weaker results.

**Final score: 6.5**

---

## Summary
This paper proves that decoder-only Transformer language models are almost-surely injective — distinct input prompts produce distinct last-token hidden representations — a property that holds at random initialization and is preserved throughout gradient-based training. The proof establishes Transformers as real-analytic functions, constructs explicit non-collision parameter configurations, and shows that gradient descent updates preserve absolute continuity of the parameter distribution. The authors then introduce SIpIT, an algorithm that reconstructs exact input text from per-position hidden states via greedy token matching with a gradient-guided search policy. Empirical collision searches across ~5B pairwise comparisons on six model families find zero collisions, and SIpIT achieves 100% token-level recovery on GPT-2 Small.

## Strengths
- **Training-preserved injectivity (Theorem 2.3) is a genuine theoretical advance.** Prior work (Sutter et al., 2025) established injectivity only at initialization. The proof that each GD step preserves absolute continuity of the parameter distribution, using the real-analyticity of the update map and its non-identically-zero Jacobian determinant, is elegant and directly addresses the practical concern that training might create collisions. The extension to SGD/mini-batch GD (Corollary 2.3.1) strengthens practical relevance.
- **The explicit non-collision construction in Theorem 2.2 is architecture-specific and non-trivial.** Rather than invoking generic measure-zero properties of real-analytic functions, the paper constructs explicit parameter settings where two arbitrary distinct prompts yield different last-token states — using distinct embedding rows for last-position mismatches and an attention-head construction for earlier mismatches. This is the critical step that prevents the difference function from being identically zero, making the measure-zero argument go through.
- **Large-scale collision search provides strong empirical backing.** Approximately 5 billion pairwise comparisons across six model families (GPT-2, Gemma-3, Llama-3.1, Mistral, Phi-4, TinyStories) found zero collisions, with minimum L2 distances consistently far above machine precision and growing with depth. The sequence-length analysis (up to 500 tokens, Figure 5) and quantization results (Tables 2-3) add further robustness evidence.
- **Counterintuitive quantization result.** FP4 and INT8 quantization not only introduces zero collisions but substantially increases minimum pairwise distances (e.g., Llama-3.1-8B from 1.274 to 6.597 under INT8, Table 2). This finding has practical implications for compressed deployment.
- **The noise-tolerance guarantee (Theorem 3.2) is practically meaningful.** It provides an explicit margin-based condition (perturbations less than half the minimum pairwise distance between distinct-token hidden states) for exact recovery, operationalizing injectivity beyond a binary property.

## Weaknesses

### Fatal
None.

### Major
- **The algorithmic evaluation is too thin to support the strong practical claims.** The main SIpIT inversion results (Table 5) are on a single model (GPT-2 Small, 124M parameters) with only 100 prompts of 20 tokens each. The quantized-model results (Table 4) use only 50 prompts of 10 tokens each. No non-quantized inversion results are reported for models larger than GPT-2 Small. For a paper claiming that "any system that stores, caches, or transmits hidden states is effectively handling the user's verbatim text" (line 349), the gap between what is evaluated and what is claimed is substantial. Either the evaluation should be deepened or the practical claims calibrated.
- **The gradient-guided candidate policy — the core algorithmic contribution over brute force — is not described in the main text.** It is relegated to Appendix Algorithms 2 and 3. The main text (Section 3) only mentions "gradient-guided search" without specifying how gradients are used, what loss is optimized, or how candidates are selected. This makes Section 3 incomplete as a standalone description of the method. The ~500× speedup from this policy is the algorithmic headline, yet a reader of the main text cannot understand how it works.

### Minor
- **"Linear time" language in the abstract is loose.** The actual worst-case bound is O(T·|V|) forward passes (Theorem 3.1) — linear in sequence length T but multiplied by vocabulary size |V| (up to 128K). While the gradient policy reduces the constant factor empirically (~0.2% of vocabulary explored, Table 4), this reduction is heuristic and not covered by the theoretical guarantee. The abstract should use "O(T·|V|)" rather than the unqualified "linear time."
- **The HARDPROMPTS baseline is a category mismatch.** HARDPROMPTS (Wen et al., 2023) performs prompt optimization (finding a prompt that elicits a target output), not prompt inversion from hidden states. Its 0% accuracy is expected and uninformative. The paper would benefit from a comparison that actually tests the same task, such as the method of Thomas et al. (2025) which the paper itself identifies as most closely related.
- **Early-layer margin tightness is underexplored.** Table 1 shows minimum L2 distances as low as 0.001 at layer 1 for Llama-3.1-8B. Theorem 3.2 requires perturbations below Δ/2 for guaranteed recovery — with Δ ≈ 0.001 this means ~5e-4 tolerance, which is tight for floating-point arithmetic. The paper does not discuss what ε value was used, whether false-positive matches were observed, or how the algorithm behaves when margins are this small.

### Trivial
- **Naming inconsistency:** The abstract uses "SIFT" while the body consistently uses "SIpIT" (and sporadically "SiPT" / "SIPIT"). This should be unified.

## Nice-to-Haves
- Specify the ε value used for matching and discuss its relationship to observed L2 distances across layers.
- Report per-token margins and any failure modes observed during inversion, particularly the source of the high runtime variance (28s mean with 36s std in Table 5).
- The privacy/regulatory discussion in Section 6 overreaches relative to the empirical evidence. The claim about hidden states being "lossless encodings of the user's exact input, recoverable in full via SIpIT" (line 349) should be tempered to match what has been demonstrated (GPT-2 Small at 20 tokens) versus what is claimed (all models at all scales).

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"Generic rather than Transformer-specific result":** REMOVED. The explicit non-collision construction in Theorem 2.2 is architecture-specific — it uses attention heads, embeddings, and positional encodings in ways that do not transfer to arbitrary smooth architectures. The critic's framing that "any architecture composed of real-analytic building blocks would yield the same conclusion" misses that Theorem 2.2 requires constructing a non-collision parameter setting, which is architecture-dependent work, not a generic consequence.
- **"Structural gap between last-token injectivity and per-position algorithm not bridged":** PARTIALLY REMOVED / DEMOTED. The paper explicitly addresses this gap at lines 143-148: since the last-token state is a deterministic function of the hidden matrix at any layer, injectivity of the last-token map implies injectivity of the full hidden-state matrix. The critic's claim that the paper does not bridge this gap is factually incorrect. The remaining concern about local separation margins has been retained as a minor weakness.
- **"Proof sketch for Theorem 2.2 glosses over architectural details":** REMOVED. The paper explicitly references Appendix C for the full proof. The sketch in the main text is appropriate for a conference paper and the harsh critic's demand is a presentation nitpick.
- **"The paper changes the question from continuous to discrete and answers the easier one":** REMOVED. The paper explicitly frames its contribution as addressing the discrete-input question (lines 13-16, 43, 332-333). It acknowledges that individual components are non-injective in the continuous sense and positions its contribution as addressing the discrete mapping specifically.
- **Strength Finder "global distinctness and SGD robustness":** REMOVED from strengths. These are straightforward corollaries that follow directly from the main theorems and do not represent independent contributions.
- **Strength Finder "layer-wise and sequence-length analyses":** REMOVED from strengths. These are standard empirical analyses supporting the main claim, not independently significant.

## Novel Insights
The paper's most genuinely novel conceptual move is reframing the injectivity question from the continuous domain (can two nearby embedding-space points map to the same state?) to the discrete domain (can two distinct token sequences produce identical hidden states?). This shift is what makes the real-analytic framework applicable: with a finite discrete input space, collisions become a measure-zero event that can be ruled out by a single non-collision construction, whereas continuous-domain injectivity would require stronger structural arguments. Prior work that characterized Transformers as "lossy" was operating in the continuous frame; this paper shows that for the practically relevant question of whether distinct inputs can collide, the answer is no. The quantization result — that aggressive compression strengthens rather than weakens representation separation — is a genuinely surprising empirical finding.

## Suggestions
- Either extend inversion evaluation to at least one non-quantized model in the 7B+ range with longer prompts, or recalibrate claims about practical invertibility to match the current GPT-2 Small evidence.
- Move the gradient-guided policy description into the main text (even in abbreviated form) so Section 3 is self-contained.
- Replace HARDPROMPTS with a baseline that actually performs the same task, or clearly frame HARDPROMPTS as an illustrative contrast rather than a competitive baseline.
- Use "O(T·|V|)" in the abstract rather than unqualified "linear time."

## Score and Decision

**Calibration anchors referenced:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| t9dWHpGkPj (Language Model Inversion) | 5.50 | R1 | Our paper has stronger theory and better inversion results; clearly above |
| 1lFZusYFHq (Transformers Implement Induction Heads) | 6.20 | R1 | Comparable theory depth; our paper has more general results and better empirics |
| hwSmPOAmhk (Understanding Factual Recall) | 7.33 | R1 | Deeper theory in that paper; we are below this |
| n7n8McETXw (Training Transformers for CoT) | 6.50 | R2 | Comparable: both have theoretical contributions with simplified-setting limitations |
| YzxMu1asQi (Scaling Laws for Adversarial Attacks) | 6.50 | R2 | Comparable: strong empirical story with practical implications; our theory is stronger |
| GeUK3zGreN (Taming Transformer Without Warmup) | 6.50 | R2 | Different topic; comparable score range |
| LbJqRGNYCf (JoMA dynamics) | 5.75 | R2 | Our paper is stronger theoretically and empirically |

**Round 1 bracket:** 5.5–7.0
**Round 2 narrowing:** The paper sits near 6.5 — above the 6.20 Induction Heads paper (rejected, more limited scope) and comparable to the 6.50 anchors (accepted, all with strong contributions but notable limitations). It is below the 7.33 Factual Recall paper, which offered deeper theoretical analysis. The thin algorithmic evaluation prevents a higher score despite the solid theoretical contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>