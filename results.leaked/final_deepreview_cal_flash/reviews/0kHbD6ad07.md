Now I have a thorough understanding of the paper and both reviewer inputs. Let me compose the final consolidated review.

## Summary
This paper proves that decoder-only Transformer language models are almost-surely injective (distinct prompts yield distinct last-token hidden states) under standard initialization and training, by exploiting the real-analyticity of Transformer components. It introduces SIFT (also called SIPIT), an algorithm that recovers the exact input prompt from per-position hidden states with provable linear-time guarantees, and validates both claims empirically through a large-scale collision search (no collisions found across billions of comparisons) and successful exact inversion on multiple models up to 70B parameters.

## Strengths

1. **Novel theoretical perspective on Transformer representations.** The paper is the first to rigorously argue that Transformer hidden states are almost surely injective (lossless) by leveraging real-analyticity, transforming the conventional intuition that non-linearities and normalization make representations inherently lossy. This reframing is valuable independently of how far the proofs are fleshed out in the main text.

2. **Large-scale empirical collision search with clear results.** The collision search (100k prompts, ≈5B pairwise comparisons) across six model families including Gemma-3, Llama-3.1-70B, Mistral-7B, GPT-2, Phi-4, and TinyStories finds zero collisions with minimum L₂ distances far above the collision threshold. This is the strongest empirical evidence to date that different prompts practically always produce distinct hidden states.

3. **SIFT/SIPIT algorithm with practical exact-inversion capability.** The algorithm recovers the full input sequence token-by-token with 100% accuracy while exploring less than 0.22% of the vocabulary on average, running orders of magnitude faster than brute-force search. The linear-time worst-case guarantee and the robustness analysis under quantization add concrete value beyond what approximate inversion methods offer.

4. **Robustness to weight quantization.** The finding that FP4/INT8 quantization does not introduce collisions and actually more than doubles the minimum pairwise distances is practically relevant and somewhat surprising, extending the injectivity claim to common deployment scenarios.

## Weaknesses

### Major

1. **Theorem 2.3 (training preservation) proof sketch is too thin for a central theoretical claim.** The sketch states that det Dφ is "not identically zero (one can check this by evaluating at a simple parameter setting)" without giving even a hint of the construction, and asserts that local invertibility implies preservation of absolute continuity without measure-theoretic justification. While the paper defers to Appendix C for the full proof (which is stripped from the available text), the sketch in the main body is unusually terse — even for a sketch — for a result on which the paper's flagship guarantee depends. A reader cannot assess whether the proof strategy is sound from the main text alone.

2. **Mismatch between the theoretical injectivity result and the inversion algorithm's access model.** The theoretical result concerns the map from prompts to the *last-token* state. The SIFT algorithm, however, requires access to *all per-position hidden states* at a given layer, which is a substantially stronger access model. The paper acknowledges this ("designing an efficient algorithm for that setting is nontrivial and left to future work"), but the title ("hence invertible") and abstract ("first algorithm that provably and efficiently reconstructs the exact input text from hidden activations") elide this distinction. The algorithm works from a richer signal than the theory directly covers, and the injectivity of the last-token map is not strictly necessary for SIFT to operate.

### Minor

3. **HARDPROMPTS is not a meaningful inversion baseline.** HARDPROMPTS was designed for prompt *optimization* (finding a prompt that achieves a performance objective), not for *inverting* a given hidden state. Its 0% accuracy is expected and does not illuminate SIFT's performance. The paper discusses this distinction in the related work but still presents it as a comparative result. A comparison with Thomas et al. (2025) or another method operating on internal states would be more informative.

4. **Inconsistent naming of the algorithm.** The algorithm is introduced as SIFT in the abstract/intro, formally named SIPIT (Sequential Inverse Prompt via ITerative updates) in Section 3, and then appears as SIpIT, SiPT, and SIFT in various places (Algorithm 1, Table 4, Table 5, experiment text). This inconsistency is confusing for a central contribution.

5. **Quantization robustness experiment lacks noise-level quantification.** Theorem 3.2 gives a precise condition (‖eₜ‖ < Δ_{π,t}/2) for robust inversion, but the quantization experiments do not report Δ_{π,t} or the effective noise level, so it is unclear whether the theoretical condition was satisfied or the empirical success occurred despite its violation.

### Trivial

6. **The collision search (100k prompts, ≈5B pairs) does not specify prompt lengths or confirm that all 100k prompts are distinct.** This is a minor reporting gap.

## Nice-to-Haves

- An ablation comparing the gradient-guided candidate policy with greedy sweep (enumerate candidates without gradient ranking) would help isolate the source of SIFT's efficiency gains more cleanly than the current BRUTEFORCE (random) baseline.
- A discussion of why the proof of Theorem 2.3 cannot rely on standard push-forward results for diffeomorphisms (e.g., change-of-variables formula) and what additional argument is needed, even in a sketch, would help the reader follow the reasoning.
- The privacy implications section (Discussion) could more carefully delineate what SIFT enables (inversion from per-position states, e.g., leaked KV-cache) vs. what remains an open threat (inversion from only last-token states or logits).

## Removed Points

*The following points from the harsh critic were removed after cross-checking against the paper:*

- **"The paper does not provide a valid proof of Theorem 2.3, and the central guarantee is not established."** — The paper explicitly states that the full proof is in Appendix C (Theorems C.1 and C.5), which was stripped by the PDF parser. Under the rules, the paper cannot be penalized for appendix content being absent in this format. The criticism of the sketch's brevity is retained as a Major weakness, but the claim that the proof is entirely missing or invalid is removed.
- **"The construction showing h(θ) is not identically zero is sketched too briefly to be convincing."** — The full proof is in Appendix C (Theorem C.2). The sketch in the main text is brief but gives the intuitive construction. Retained as a Nice-to-Have rather than a Weakness, since the intuition is clear even if the formal verification requires the appendix.
- **"The invertibility claim is misaligned—the algorithm would work even if the last-token map were not injective."** — This overstates the mismatch. The paper explicitly defines the threat model (per-position states) and acknowledges that inversion from only the last-token state is left to future work. The theoretical injectivity result implies injectivity of the full hidden matrix (since the last row is a deterministic function of the matrix), so the connection is logically sound. Retained as a Major weakness but reframed as an access-model mismatch.
- **"The paper does not report the number of tokens per prompt or whether the prompts are all distinct."** — Retained as Trivial.
- **"The baseline BRUTEFORCE is trivial; a more meaningful baseline would be a linear scan without gradient guidance."** — BRUTEFORCE *is* the ablation without gradient guidance (random ordering vs. gradient-guided ordering). The critic misread this.
- **"The robustness condition from Theorem 3.2 was not verified."** — Retained as Minor (point 5).
- **Claims about model/tool non-existence or unreleased status.** — None of the cited models or benchmarks are questioned in the inputs, so no removal needed.

## Novel Insights

The synthesis of the reviews surfaces a tension that neither the paper nor the individual reviews fully resolve: the paper's headline contribution is a *mathematical guarantee* of injectivity, but the central training-preservation theorem receives only a cursory sketch in the main text, while the inversion algorithm that "operationalizes" injectivity relies on a richer access model (per-position states) than the theory targets (last-token state). This creates an awkward hybrid: the theory is presented with the ambition of a rigorous mathematical contribution, but the main-text proofs are too terse to satisfy that ambition, and the algorithm's success does not directly validate the most novel part of the theory (training preservation). The paper might be more convincing if it either (a) committed fully to a rigorous theoretical treatment with the full proof structure visible in the main text, or (b) repositioned as an empirical-theoretical paper where the theory motivates but does not solely carry the contribution, and the experiments (which are genuinely strong) take center stage.

## Suggestions

- Expand the sketch of Theorem 2.3 to at least outline the key steps: a candidate parameter setting where det Dφ ≠ 0, a brief discussion of the area-formula/change-of-variables justification for absolute-continuity preservation, and how composition of finite steps avoids the measure-zero pitfalls.
- Align the algorithm's name consistently throughout the paper.
- Replace or supplement the HARDPROMPTS baseline with a method that targets a comparable access model (e.g., Thomas et al. 2025).
- Add a table or note reporting Δ_{π,t} and effective noise levels for the quantization robustness experiments.

## Score and Decision

Let me run the calibration to finalize the score.

**Round 1 bracket:** Based on the initial search, the paper plausibly sits between 5.5 and 7.5. The weak anchors (avg 3.0) were on less relevant topics and clearly weaker. The middle anchors (5.6–6.67) were transformers papers with theoretical+empirical components. The strong anchors (7.6–8.67) were top-tier papers with more complete theoretical treatments.

**Round 2 narrowing:** Pulled additional anchors in the 5.5–7.5 range. Comparing against:
- *When Can Transformers Count to n?* (5.60): This paper has weaker experiments (limited to simple counting) and oversimplified architecture. The current paper is empirically stronger and the theoretical claim is more novel. → Current paper is stronger.
- *Vocabulary In-Context Learning* (6.00): Primarily theoretical with limited experiments. Current paper has stronger experiments. → Current paper is slightly stronger.
- *How Transformers Implement Induction Heads* (6.20): Solid theoretical analysis but limited to a specific mechanism with synthetic experiments. Current paper has broader scope and stronger empirical validation. → Current paper is stronger.
- *Transformers are Universal In-context Learners* (6.67): Accepted paper with a clear universality proof but limited experiments. Comparable novelty. Current paper has stronger experiments. → Comparable, with current paper slightly ahead on empirical depth.
- *On the Learn-to-Optimize Capabilities of Transformers* (7.00): Strong theoretical convergence proofs but the bridge between theory and experiments was questioned by reviewers. Current paper has cleaner experimental validation but thinner theory in the main text. → Slightly weaker than this anchor due to the sketchy Theorem 2.3.

The paper is stronger than the 5.6–6.2 range and roughly comparable to the 6.67 anchor, but the incomplete proof sketch in the main text prevents it from reaching the 7.0+ tier. I place it at **6.5**.

**Anchors considered across rounds:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| uOnElfFuey | 3.00 | 1 | Very different topic (regular language extraction), much weaker |
| fSbPwHjdDG | 3.00 | 1 | Causal intervention study, much narrower scope |
| 4y3GDTFv70 | 3.25 | 1 | Latent space theory, limited experiments |
| z3DMFpaP6m | 3.00 | 1 | Entropy metric paper, weaker contribution |
| NSBP7HzA5Z | 3.00 | 1 | Inductive bias proposal, limited validation |
| WULjblaCoc | 5.60 | 1, 2 | Counting paper with weaker experiments; current paper stronger |
| 1lFZusYFHq | 6.20 | 1, 2 | Induction head theory, limited experiments; current paper broader |
| YE6N8htoFQ | 6.00 | 2 | In-context learning theory, no practical algorithm; current paper stronger empirically |
| b5lXUwZiD3 | 5.25 | 2 | HMM learning limitations, narrower scope |
| 6S4WQD1LZR | 6.67 | 2 | Universality proof, comparable novelty but weaker experiments |
| fp77Ln5Hcc | 4.50 | 2 | Depth extrapolation, less relevant |
| STUGfUz8ob | 7.60 | 1 | Reasoning with symbols, more complete theory; current paper weaker on theory rigor |
| n2NidsYDop | 8.67 | 1 | Parity+CoT theory, very strong theoretical contribution |
| Tzh6xAJSll | 7.60 | 1 | Scaling laws, different type of contribution |
| d8w0pmvXbZ | 8.00 | 1 | Training stability proxies, different focus |
| tcsZ9tZNKD | 8.20 | 1 | Sparse autoencoders, different focus |
| EytBpUGB1Z | 8.00 | 1 | Retrieval heads, more empirical |
| VoLDkQ6yR3 | 6.67 | 2 | Reconstruction attacks (different setting) |
| KSBx6FBZpE | 6.25 | 2 | Latent memories, different focus |
| NHhjczmJjo | 7.00 | 2 | L2O capabilities, stronger theory in main text but more limited experiments |
| 1ExfUpmIW4 | 6.00 | 2 | Knowledge unlearning, different topic |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>