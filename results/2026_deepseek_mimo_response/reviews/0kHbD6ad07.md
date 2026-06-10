Now I have enough calibration data. Let me write the final review.

**Round 1 Bracket:** 6.5 to 8.0 — The paper has a novel theoretical contribution (injectivity persistence under training), massive empirical validation (~5B comparisons), and a practical algorithm (100% exact recovery). Clearly above weak theory papers (score 2-3.5) and clearly in the accepted range.

**Round 2 Narrowing:** The paper sits above the 6.67–6.80 anchors (pure theory papers on expressivity/learnability with limited experiments) and is comparable to the 7.33–7.50 anchors (strong theory papers on memorization/expressivity with real-world implications), with the proof sketch gap for mini-batch GD preventing it from reaching 7.5+.

**Final comparison:**
- Above U49N5V51rU (6.80): stronger theory, vastly more extensive experiments, practical algorithm
- Above hwSmPOAmhk (7.33): works on real models at scale rather than simplified synthetic tasks
- Slightly below MrR3rMxqqv (7.50) and NjNGlPh8Wh (7.50): the proof sketch gap for the practically relevant mini-batch regime is a real weakness that these cleaner proofs don't have
- Below STUGfUz8ob (7.60): which has a cleaner proof chain despite its own issues

**Final score: 7.0**

---

## Summary
This paper proves that decoder-only Transformer language models are almost-surely injective maps from discrete input sequences to continuous last-token hidden states — different prompts yield different representations with probability one under standard initialization and training. The proof uses real-analyticity of Transformer components to confine collisions to measure-zero parameter sets and shows gradient-based training preserves this. The paper provides SIpIT, a constructive algorithm that recovers exact input prompts from per-position hidden states with provable linear-time guarantees, and validates both claims across 8+ model families (33M–70B parameters) with ~5 billion pairwise comparisons yielding zero collisions.

## Strengths
- **Novel theoretical advance over prior work on Transformer injectivity**: The key contribution beyond Sutter et al. (2025) is proving injectivity *persists under training*, not just at initialization, and at the task-relevant *last-token state* rather than the full hidden-state matrix. Theorem 2.3 (lines 101–109) uses the absolute-continuity argument (GD steps are real-analytic maps with non-degenerate Jacobians, preserving absolutely continuous parameter distributions), which is a substantive technical advance.
- **Clean mathematical framework executed well**: The three-step strategy — establish real-analyticity (Theorem 2.1, lines 67–73), show collision sets have measure zero (Theorem 2.2, lines 77–89), prove GD preserves absolute continuity (Theorem 2.3) — is well-structured. The constructive argument for ruling out h≡0 (lines 86–87) is concrete: freeze the network for last-position differences, or set one attention head to attend to the first mismatch for earlier differences.
- **Massive empirical collision search confirming theory**: ~5 billion pairwise comparisons across 100k prompts and 8+ model families (GPT-2 S/M/L, Gemma-3 1B/4B/12B, Llama-3.1-8B/70B, Mistral-7B, Phi-4-mini/14B, TinyStories-33M) find zero collisions. Tables 1–3 show minimum pairwise distances are consistently orders of magnitude above any collision threshold (≥0.001 at layer 1, growing to ≥0.620 at final layer).
- **SIpIT algorithm with formal guarantees and strong practical results**: Theorem 3.1 proves correctness with O(T|V|) worst-case time; Theorem 3.2 proves robustness under perturbation. Table 5 shows SIpIT achieves 100% exact recovery in 28s on GPT-2 Small vs. 0% for HARDPROMPTS and ~3900s for BRUTEFORCE. Table 4 shows less than 0.22% vocabulary exploration on 128K-vocabulary Llama-3.1-8B.
- **Quantization robustness extends practical relevance**: Tables 2–3 demonstrate that FP4 and INT8 quantization not only preserves injectivity but *increases* minimum pairwise distances (e.g., Llama-3.1-8B: 1.274 in FP32 → 6.597 in INT8), up to 70B parameters. This is directly relevant since deployed models are typically quantized.

## Weaknesses

### Fatal
None.

### Major
- **Proof sketch gap for mini-batch GD (Corollary 2.3.1)** — Lines 113–115 argue that for the batch update map φ_B, "at the point θ* from the single-sample proof (where the Jacobian determinant is sample-independent and nonzero) the batch Jacobian coincides with the single-sample one by linearity of differentiation, and its determinant is therefore also nonzero." This reasoning is flawed: differentiation is linear in the *function* (D(Σfᵢ) = ΣDfᵢ), so the batch Jacobian I - η∇²L_B(θ*) equals the average of per-sample Jacobians I - η∇²Lᵢ(θ*). Even if each per-sample Jacobian has nonzero determinant at θ*, the determinant of their *average* need not be nonzero (the determinant is not a linear function). Since stochastic training is the practically relevant regime, this gap matters. The conclusion is almost certainly true — for any fixed batch, the zero set of det(I - η∇²L_B) is measure-zero and one just needs to show it is not identically zero — but the sketch as written does not establish this. The paper should either fix this argument (e.g., show directly that det(I - η∇²L_B(θ)) is not identically zero at some convenient θ) or explicitly note that the full appendix proof handles this more carefully.

### Minor
- **Naming inconsistency for the algorithm** — The algorithm is called "SIFT" in the abstract (line 9), introduction (lines 17, 23, 25), Figure 1 caption, and §4.2 (line 291); "SIPIT" in line 45; "SIpIT" in §3 (lines 139, 167, 171); "SiPT" in §4 tables (lines 234, 309, 319, 321); and "SiPIT" in §6 (lines 345, 347). This is genuinely confusing and should be unified.

- **Gap between theory (last-token injectivity) and algorithm (requires per-position states)** — The injectivity theorems establish that s ↦ r(s; θ) (last-token state) is injective. SIpIT (§3) requires the full hidden-state matrix H^(ℓ) ∈ ℝ^{T×d}. The paper honestly acknowledges this (line 141: "designing an efficient algorithm for [last-token-only] setting is nontrivial and left to future work") but the connection between the two contributions could be more explicit. SIpIT's correctness primarily relies on one-step causal injectivity (a weaker condition following from the same analytic framework), while the training-persistence result (Theorem 2.3) is most relevant to the theoretically cleaner but algorithmically harder last-token-only inversion setting.

### Trivial
None.

## Nice-to-Haves
- Brief justification that the collision threshold 10⁻⁶ is an arbitrary small positive constant (any finite threshold above machine epsilon would serve, given the theory predicts exact collisions h(θ) = 0).
- Explicit note that ReLU-based models fall outside the theoretical guarantee (ReLU is not real-analytic), since ReLU is still used in some architectures.
- Brief comparison of SIpIT's cost to the original forward pass, to calibrate the practical threat: Table 5 shows ~28s for 20-token prompts on GPT-2 Small — how does this compare to inference cost?

## Removed Points
These points are flagged to be removed, treat them with caution:
- (No weaknesses were removed — all were verified against the paper text and retained at appropriate severity tiers.)

## Novel Insights
The paper's most notable observation beyond its core theoretical contribution is that quantization (FP4, INT8) *increases* minimum pairwise distances rather than degrading them (Table 2: Llama-3.1-8B goes from 1.274 in FP32 to 6.597 in INT8). This is counterintuitive — one might expect quantization to introduce collisions by discretizing the continuous representation space — and has practical implications for the robustness of injectivity in deployed systems.

## Suggestions
- Fix the naming inconsistency by choosing one name (e.g., "SIpIT") and using it consistently throughout.
- Revise the proof sketch for Corollary 2.3.1 to avoid the flawed determinant-of-average argument. A cleaner approach: show directly that det(I - η∇²L_B(θ)) is not identically zero by evaluating at some convenient θ (e.g., far from any stationary point where gradients are large), or simply reference the appendix proof if it handles this correctly.
- Add a brief paragraph in §3 explicitly clarifying that SIpIT's correctness rests primarily on one-step injectivity (weaker than last-token injectivity), while the full training-persistence theorem is most relevant to the harder last-token-only inversion setting.

## Calibration Anchors Retrieved

**Round 1 (bracketing):**
| Path | Avg Score | Band | Comparison |
|------|-----------|------|------------|
| JNZ3Om6NPS | 2.00 | Weak | Much weaker — flawed mathematical reasoning about LLM limitations |
| 4y3GDTFv70 | 3.25 | Weak | Much weaker — speculative latent space theory, no rigorous proofs |
| uOnElfFuey | 3.00 | Weak | Much weaker — limited contribution recovering knowledge from LMs |
| t9dWHpGkPj | 5.50 | Middle | Weaker — approximate prompt inversion (27% exact match, no guarantees) vs. this paper's exact recovery with provable guarantees |
| YE6N8htoFQ | 6.00 | Middle | Weaker — vocabulary ICL theory, rejected despite reasonable quality |
| GFua0WEYGF | 5.25 | Middle | Weaker — provable OT with transformers, rejected |
| NHhjczmJjo | 7.00 | Middle | Comparable — L2O with transformers, strong theory + experiments |
| STUGfUz8ob | 7.60 | Strong | Comparable — abstract reasoning with transformers, noted over-claiming |
| Tzh6xAJSll | 7.60 | Strong | Comparable — scaling laws for associative memories |
| aWXnKanInf | 8.00 | Strong | Stronger — TopoLM with brain-like organization, unique and impactful |
| oYjPk8mqAV | 8.00 | Strong | Stronger — theorem proving premise selection, major practical impact |

**Round 2 (narrowing):**
| Path | Avg Score | Band | Comparison |
|------|-----------|------|------------|
| 6S4WQD1LZR | 6.67 | Narrow | Weaker — pure theory on universal in-context learning, no empirical validation at scale |
| 4ikjWBs3tE | 6.75 | Narrow | Weaker — low sensitivity theory, limited practical implications |
| U49N5V51rU | 6.80 | Narrow | Weaker — length generalization framework with limited experiments |
| uBai0ukstY | 7.00 | Narrow | Comparable — NFN for transformers, systematic but narrower scope |
| hwSmPOAmhk | 7.33 | Narrow | Comparable — factual recall via associative memories, works on simplified models |
| MrR3rMxqqv | 7.50 | Narrow | Slightly stronger — memorization capacity with cleaner proof chain |
| NjNGlPh8Wh | 7.50 | Narrow | Slightly stronger — CoT expressivity, clean theoretical contribution |

**Bracket:** Round 1 placed the paper between 6.5 and 8.0. Round 2 narrowed to between 6.8 and 7.5. The paper is clearly above the 6.67–6.80 theory papers (which lack the extensive real-model experiments and practical algorithm) and comparable to the 7.33–7.50 papers, with the proof sketch gap for mini-batch GD preventing a score at the upper end.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>