## Summary

This paper establishes that decoder-only Transformer language models are "almost surely injective" — distinct prompts map to distinct last-token hidden representations, under any continuous random initialization and after any finite number of gradient descent steps. The proof leverages real-analyticity of transformer components together with the measure-zero dichotomy for real-analytic functions. Building on this theory, the paper introduces SIFT (SIpIT), a sequential algorithm that exploits causal structure to exactly reconstruct input tokens one-by-one from hidden states at a fixed layer, with provable O(T|V|) worst-case complexity and linear-time empirical behavior.

---

## Strengths

- **Clean and rigorous theoretical contribution.** The three-theorem sequence (Thm 2.1: real-analyticity; Thm 2.2: almost-sure injectivity at init; Thm 2.3: preservation under GD) is well-structured. The use of the real-analytic zero-set dichotomy is elegant and correctly applied — once real-analyticity is established, the collision set being measure-zero follows cleanly, and the Jacobian-determinant argument for preserving absolute continuity under GD is sound.

- **Thorough empirical validation.** Approximately 5 billion pairwise comparisons across six model families (GPT-2 S/M/L, Gemma-3 1B/4B/12B, Llama-3.1-8B, Mistral-7B, Phi-4-mini, TinyStories-33M), finding zero collisions with minimum distances far above threshold. The stress-test against 10 closest-prefix prompts (Fig. 4) is particularly compelling.

- **Practical algorithm with provable guarantees.** SIFT achieves 100% token-level exact recovery on both GPT-2 and FP4-quantized Mistral/Llama (Table 4/5), exploring on average only ~0.22% of the vocabulary, while BRUTEFORCE requires orders-of-magnitude more compute and HARDPROMPTS fails entirely (accuracy = 0.00, Table 5). The robustness theorem (Thm 3.2) providing a perturbation tolerance is a useful complement to the exactness guarantee.

- **Timely implications for privacy and interpretability.** The identification of hidden states as lossless representations of user input, with a constructive recovery procedure, has clear and concrete implications for KV-cache privacy, regulatory compliance, and mechanistic interpretability baselines.

---

## Weaknesses

### Fatal
None. The core theoretical claims are sound under their stated assumptions.

### Major

1. **Gap between theory and practice: Adam/AdamW not covered.** Theorem 2.3 and Corollary 2.3.1 cover GD and mini-batch SGD with step sizes in (0, 1). However, virtually all modern LLMs in the experimental evaluation (Llama-3.1, Mistral, Gemma-3, Phi-4) are trained with Adam or AdamW, which introduces momentum and per-parameter adaptive learning rates. The GD update map φ(θ) = θ − η∇L(θ) is real-analytic; the Adam update ψ is not straightforwardly real-analytic due to square-root normalization of second moments and ε-stabilization. The paper does not address whether the absolute-continuity-preservation argument extends to Adam, leaving a meaningful gap between the proved training scenario and practical training pipelines.

2. **Inversion requires all per-position hidden states, not just the last-token representation.** The introduction and abstract state that SIFT "reconstructs the exact input text from hidden activations," and the main injectivity theorem focuses on the last-token state. However, the algorithm (Algorithm 1) requires access to the full hidden state matrix H^(ℓ) ∈ R^{T×d} at layer ℓ — specifically, the hidden state at every token position. This is a significantly stronger access requirement than just the last-token state (or model output), and it limits the scenarios in which SIFT applies. The abstract and introduction should clearly distinguish "injectivity from the last-token state" (theoretical result) from "exact recovery using all-position intermediate states" (the SIFT algorithm).

### Minor

1. **Quantization observation unexplained.** Table 2 reports that FP4 and INT8 quantization consistently *increases* minimum pairwise distances between representations compared to FP32 (e.g., Llama FP32 min-dist = 1.274, FP4 = 2.281, INT8 = 6.597). This is counterintuitive — quantization reduces numerical precision and should in principle increase the risk of collisions, not decrease inter-representation distance. No explanation is offered for this phenomenon.

2. **Collision threshold of 10^-6 is ad hoc.** The threshold is used consistently but without justification. At FP32 machine epsilon (~1.2×10^-7), a threshold of 10^-6 is reasonable, but across FP16/BF16 inference (where most evaluations run), the natural rounding floor is ~10^-3. A brief discussion of how the threshold relates to floating-point precision would strengthen confidence in the empirical findings.

3. **Algorithm naming inconsistency.** The algorithm is referred to as SIFT, SIPIT, SIpIT, SiPIT, and SiPT across different sections (abstract, §3, §4.2, §6). This makes the paper harder to follow.

### Trivial

- The URL for the implementation in footnote 3 is blank in the text.

---

## Nice-to-Haves

- A proof sketch or empirical argument addressing Adam: e.g., showing that Adam's update map has nonzero Jacobian determinant a.e., or at minimum a discussion of why absolute continuity likely persists.
- A clarification upfront distinguishing the weaker requirement (injectivity proven for last-token states) from the stronger requirement for SIFT (all-position hidden states at layer ℓ).
- An explanation for the surprising quantization-distance effect in Table 2.

---

## Novel Insights

The most genuinely novel element is the combination of (a) showing the collision set is measure-zero via real-analytic structure, and (b) proving that this measure-zero property is preserved under gradient descent via absolute continuity of the pushforward measure. Prior work by Sutter et al. (2025) established almost-sure injectivity at initialization with respect to the full hidden-state matrix; this paper extends that to the task-relevant last-token state and, crucially, proves the property survives training. The SIFT algorithm's exploitation of causal structure for exact sequential inversion — achieving 100% accuracy while exploring <0.22% of the vocabulary — is a practically significant realization of the theoretical guarantee. The framing of hidden states as "the prompt in disguise" with direct legal/regulatory implications is a useful conceptual contribution to the interpretability and safety communities.

---

## Suggestions

- Extend or discuss the Adam case explicitly, even if informally. A simple numerical experiment showing that Adam-trained models remain far from collision sets would mitigate this concern significantly.
- Add a single sentence in the abstract/intro clarifying that SIFT requires all per-position hidden states at a given layer, so readers are not misled by the "from hidden activations" phrasing.
- Investigate and explain the quantization distance-increase effect; it may reflect a regularization phenomenon worth reporting as a standalone finding.

---

## Score and Decision

The paper establishes a clean, rigorous result on a question of genuine theoretical and practical importance. The proof strategy is well-chosen, the empirical validation is unusually thorough (5B comparisons, multiple model families, quantized variants), and the algorithm delivers on its guarantees in practice. The main limitation — that the training-preservation theorem does not formally cover Adam — is a real gap but does not invalidate the core contribution, as the empirical results hold for all tested Adam-trained models. The distinction between injectivity (last token) and invertibility (all positions) should be communicated more clearly in the abstract and introduction.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>