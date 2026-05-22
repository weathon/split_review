Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper proves that decoder-only Transformer language models are almost-surely injective — different prompts almost always yield different last-token hidden representations — at initialization and that training preserves this property. It then introduces SIFT, an algorithm that leverages injectivity to recover exact input text from hidden states with provable linear-time guarantees, and provides empirical validation through large-scale collision searches (~5B comparisons) and limited-scale inversion experiments.

---

## Strengths

1. **Real-analyticity framework (Theorem 2.1).** The paper proves that decoder-only Transformers with analytic activations (GELU, tanh, etc.) are real-analytic functions of their parameters, establishing the foundation for all subsequent measure-zero arguments. This goes beyond prior work that analyzed injectivity only at initialization and only with respect to inputs (e.g., Sutter et al., 2025).

2. **Generic injectivity proof (Theorem 2.2).** Using the real-analyticity of the difference function \(h(\theta) = \|\mathbf{r}(s;\theta) - \mathbf{r}(s';\theta)\|_2^2\), the paper shows that collisions are confined to a measure-zero parameter set. The construction of a witness parameter setting (freezing layers for last-position differences, isolating the first mismatching position via attention for earlier differences) is a clever and non-obvious argument that moves beyond intuitions about Transformers being "lossy."

3. **Large-scale collision search (Section 4.1).** The paper validates injectivity empirically across ~5 billion pairwise comparisons from 100k prompts on six models (GPT-2, Gemma-3, Llama-3.1-8B, Mistral-7B, Phi-4-mini, TinyStories-33M), observing zero collisions. Minimum distances are orders of magnitude above the \(10^{-6}\) threshold (e.g., 0.620 for Llama-3.1-8B final layer). This is substantial supporting evidence that goes well beyond what most theory papers provide.

4. **SIFT algorithm and its correctness guarantees (Theorems 3.1, 3.2).** The paper operationalizes injectivity into a concrete, training-free algorithm for exact input recovery from hidden states. The robustness bound (tolerance up to half the minimum pairwise distance) and the clear sequential search procedure are clean consequences of the theory.

5. **Clear identification of when injectivity can fail.** The paper is upfront about limitations: non-analytic activations (ReLU), tied embeddings, quantization, and deliberately engineered parameters are all identified as potential failure modes. This honest characterization helps scope the result appropriately.

---

## Weaknesses

### Fatal
None.

### Major

- **Insufficient justification of the batch Jacobian argument in Corollary 2.3.1 (SGD/mini-batch extension).**  
  The paper states: "at the point \(\theta_*\) from the single-sample proof (where the Jacobian determinant is sample-independent and nonzero) the batch Jacobian coincides with the single-sample one by linearity of differentiation, and its determinant is therefore also nonzero." This reasoning as presented is incomplete. The batch update map is \(\phi_{\mathcal{B}}(\theta) = \theta - \eta \frac{1}{|\mathcal{B}|}\sum_i \nabla \mathcal{L}_i(\theta)\); its Jacobian is \(I - \eta \frac{1}{|\mathcal{B}|}\sum_i \nabla^2 \mathcal{L}_i(\theta)\). For this to "coincide" with the single-sample Jacobian at \(\theta_*\), all individual Hessians must be equal — a condition not justified by "linearity of differentiation." The paper does not explain how \(\theta_*\) is constructed to satisfy this, nor does it argue why the determinant remains nonzero under averaging. Since the paper's overall claim (including the main result statement and abstract) advertises injectivity for SGD/mini-batch training, this gap affects a substantively advertised part of the contribution. The authors should provide a complete, self-contained justification or carefully restate which training procedures are covered.

### Minor

- **Inversion experiments are limited in scale.** The main inversion evaluation uses 100 prompts of length 20 tokens (GPT-2 Small), and the quantization evaluation uses 50 prompts of length 10. While the paper is primarily theoretical and the collision search is large-scale, the inversion results are thin enough that claims about "exact invertibility in practice" rest on a small sample. Testing on longer prompts (50–200 tokens) and more diverse models would strengthen confidence that the algorithm scales robustly.

- **The robustness bound (Theorem 3.2) depends on \(\Delta_{\pi,t}\) which is not directly measured.** The paper measures related quantities (minimum pairwise distances between entire prompts in Tables 1–3), but \(\Delta_{\pi,t}\) — the minimum distance between hidden states for different candidate tokens given a fixed prefix — is the quantity that determines the noise tolerance. Directly characterizing these values for several models and layers would connect the theoretical robustness guarantee to the empirical observations.

- **The construction to avoid \(h \equiv 0\) (Theorem 2.2 sketch) is quite brief in the main text.** The paper describes freezing the network or setting an attention head to isolate the first mismatching position, but does not address architectural subtleties (e.g., whether the construction can always be realized given finite width \(d\) and context length \(K\), or how LayerNorm is handled). The full proof is deferred to Appendix C (stripped by the parser); but the main text would benefit from a more detailed sketch or a note about why the construction is always feasible.

- **Step-size restriction to (0,1) is stated without justification.** The paper restricts GD step sizes to (0,1) but does not explain whether this is required by the proof or is an artifact. The justification could be as simple as noting that the gradient map is a contraction only in this range, but it is not provided.

### Trivial
- The paper switches between "SIFT" and "SIPIT" in the text (Section 3 heading uses "SIPIT," Section 4 uses "SIFT," and the acronym is spelled differently in places). The authors should pick one spelling and use it consistently.

---

## Removed Points

These points were flagged by reviewers but removed from the main assessment under the filtering rules described in the review instructions. They are listed here for completeness but should be treated with caution.

1. **The critic's statement that the proof sketch in Theorem 2.2 is "insufficiently justified" and the appendix is "unavailable for verification."** The paper explicitly states that the full proof is in Appendix C (Theorem C.2). The parser strips appendices from all papers; the full proof exists in the original submission. Under the hard filtering rules, this criticism is removed as it targets missing appendix content. *(Retained as a **Minor** weakness only insofar as the main-text sketch could be clearer — see Weaknesses section above.)*

2. **The critic's claim that the pushforward/absolute continuity argument in Theorem 2.3 is "imprecise and insufficient."** The paper provides a sketch and references Appendix C (Theorems C.1 and C.5) for the full proof. The sketch correctly identifies the three components: real-analyticity of \(\phi\), non-identically-zero Jacobian determinant, and preservation of absolute continuity. The mathematical framework (real-analyticity → local diffeomorphism a.e. → pushforward preserves absolute continuity) is standard in analysis. The criticism largely reflects the absence of the appendix. *(The one surviving sub-point — the batch Jacobian gap in Corollary 2.3.1 — is kept as a **Major** weakness above.)*

3. **The critic's complaint about the HARDPROMPTS comparison being "misleading."** The paper explicitly acknowledges (Section 4.2, lines 309–310) that other inversion methods "tackle a different setting altogether" and "are complementary but not directly comparable." The HARDPROMPTS comparison is included redundantly alongside this caveat, so the paper is not being misleading.

4. **The critic's comment that the "linear-time guarantee" (O(T|V|)) is "trivial and not a meaningful contribution."** An O(T|V|) algorithm that provably recovers the exact input from hidden states is not trivial given that no prior work provided such a guarantee. The guarantee matters even if the brute-force bound is obvious in retrospect — the novelty is in establishing that exact recovery is possible at all, not in the complexity class.

5. **The Strength Finder's claim that "Corollary 2.3.1 extends [injectivity] to SGD and mini-batch GD... a significant improvement over prior theoretical work."** This strength is overstated given the gap in the batch Jacobian justification (see **Major** weakness above). The claim is demoted rather than fully removed, as the intention (extending to SGD) is a valid goal; the execution has a gap.

---

## Nice-to-Haves

- **Characterize \(\Delta_{\pi,t}\) empirically.** Computing the minimum distance between candidate token hidden states given a prefix, across many prefixes and layers, would directly connect Theorem 3.2 to the observed quantization robustness and show whether the theoretical tolerance is large or tiny in practice.
- **Scale the inversion experiments** to longer prompts (50–200 tokens) and more diverse model families beyond GPT-2 Small.
- **Show failure-case analysis for the gradient-guided policy** — report the distribution of candidates explored per position (histograms) rather than just the mean.
- **Extend SIFT to work from only the last-token state**, as the paper notes this is left to future work. A preliminary attack would increase practical relevance.

---

## Novel Insights

The Strength Finder and Harsh Critic converge on a mostly standard reading of the paper, but one insight emerges from their interaction: the tension between the theoretical elegance of the measure-zero argument and the practical fragility of the discrete+continuous construction. The paper argues that collisions are measure-zero in parameter space, but the inversion algorithm (SIFT) requires discrete search over the vocabulary at each position — meaning the "invertibility" the paper establishes is fundamentally combinatorial, not analytic. This distinction is under-explored: injectivity guarantees a unique preimage in principle, but the actual search cost depends on how well the hidden-state geometry separates tokens (the gradient heuristic's efficiency) rather than on the analytic property itself. The paper's framing of "invertibility" as a direct consequence of injectivity elides this gap between existence of the inverse and efficient computation of it, though SIFT does provide a concrete (linear-time) bridge.

---

## Suggestions

1. **Clarify the batch Jacobian argument.** The proof of Corollary 2.3.1 needs a proper justification for why the determinant of \(I - \eta \nabla^2\mathcal{L}_{\mathcal{B}}\) is not identically zero. If a single \(\theta_*\) works for all batch components, explain how it is constructed. If the argument requires additional assumptions (e.g., all data points contribute identical Hessians at \(\theta_*\)), state them explicitly and justify their plausibility.
2. **Add at least a brief note in the main text about why the construction in Theorem 2.2 is always feasible** given architectural constraints (finite width \(d\), context length \(K\), LayerNorm, etc.). Even a sentence acknowledging that the full construction in Appendix C handles these details would improve reader confidence.
3. **Justify the step-size restriction (0,1)** briefly, or remove it if it is not essential.
4. **Pick a single spelling for the algorithm name** (SIFT vs. SIPIT) and use it consistently.
5. **Include a small-scale measurement of \(\Delta_{\pi,t}\)** (minimum distance between candidate token states given a prefix) to directly support the robustness theorem.

---

## Score and Decision

**Originality:** High — the injectivity result is non-obvious and goes against common intuition.  
**Significance of the research question:** High — understanding whether representations preserve input information is foundational for interpretability, privacy, and safety.  
**Support for claims:** Moderate-strong — the theoretical framework is sound, the collision search is thorough, but the SGD/mini-batch extension has a gap in its presented justification, and the inversion experiments are limited in scale.  
**Soundness of experiments:** Good for the collision search; adequate but limited for inversion.  
**Clarity of writing:** Good — the main ideas are presented clearly despite some deferred details.  
**Value to the community:** High — provides a theoretically grounded, empirically verified property with direct algorithmic consequences.

The paper has a genuinely interesting and well-motivated core contribution. The main structural weakness is the insufficient justification of the batch Jacobian argument in the SGD/mini-batch extension (Corollary 2.3.1), which affects a substantively advertised part of the result. This is addressable in a rebuttal (e.g., by providing a correct construction or by scoping the main result to full-batch GD). The collision-search experiments are unusually thorough for a theory paper. With clarification of the batch argument, the paper would be a strong contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>