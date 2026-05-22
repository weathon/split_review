Now I have sufficient evidence to produce the consolidated final review. Let me construct it.

---

## Summary

This paper proves that decoder-only Transformer language models are almost-surely injective — distinct prompts map to distinct last-token hidden states — at initialization and under gradient descent training, using a real-analyticity argument. It then introduces SIPIT (SIFT), the first algorithm that provably recovers the exact input sequence from per-position hidden states in linear time. The theoretical claims are backed by extensive empirical collision searches (≈100k prompts, 5 billion pairwise comparisons, six model families) and exact-inversion experiments on GPT-2 Small, Mistral-7B, and Llama-3.1-8B.

---

## Strengths

1. **First proof that injectivity persists under training (Theorems 2.2 and 2.3).** The paper goes beyond prior work (Sutter et al. 2025) that only addressed initialization. The argument is built on real-analyticity of the architecture, measure-zero collision sets, and the fact that gradient-descent update maps preserve absolute continuity. The proof extends naturally to SGD and mini-batch GD (Corollary 2.3.1).

2. **Large-scale empirical collision search with clean results (Section 4.1, Figure 3, Table 1).** On ≈100k prompts across GPT-2, Gemma-3, Llama-3.1-8B, Mistral-7B, Phi-4-mini-instruct, and TinyStories-33M — spanning many layers — minimum pairwise L2 distances are orders of magnitude above the collision threshold (10⁻⁶). The search extends to FP4/INT8 quantized models and 70B-parameter models, all confirming no collisions.

3. **SIPIT: first algorithm with provable linear-time exact recovery (Theorems 3.1, 3.2, Algorithm 1).** The algorithm exploits causal structure to recover the prompt token-by-token in at most T·|𝒱| steps. Theorem 3.2 provides a robustness guarantee under bounded noise. Empirically, SIPIT achieves 100% token-level accuracy while exploring <0.22% of the vocabulary on FP4-quantized Mistral-7B (Table 4), and runs in 28s on GPT-2 Small vs. 3890s for brute force (Table 5).

4. **Honest discussion of failure modes (Section 2, "Failure cases").** The paper explicitly states that collisions can be manufactured via non-analytic choices such as identical embedding vectors or identical positional embeddings. This clarifies the boundary conditions of the theorem and strengthens credibility.

5. **Practical and regulatory relevance.** The paper connects injectivity to privacy and data-protection obligations, arguing that hidden states "are not abstractions but the prompt in disguise." This is a concrete and actionable implication.

---

## Weaknesses

### Fatal
None.

### Major

1. **Weight tying (tied input/output embeddings) is not discussed.** Many LLMs (including GPT-2 and Llama) tie input and output embedding matrices, constraining the parameter space to a linear subspace of the full embedding-matrix space. The paper's measure-zero argument is relative to the *full* parameter space; on a lower-dimensional subspace, a measure-zero set in the ambient space could inherit positive measure if the real-analytic function vanishes identically on the subspace. The proof's construction of a separating parameter setting may or may not respect the tying constraint — the paper simply does not address this. This is a genuine gap in the theoretical scope that the authors should either close or explicitly acknowledge and circumscribe.

### Minor

2. **The theoretical guarantee covers only gradient descent, not Adam/adaptive optimizers (Theorem 2.3).** The paper is transparent about proving for GD ("train for any finite number T of GD steps"), and the abstract's "preserved during training" is a reasonable high-level summary. Nevertheless, all tested models were trained with Adam or similar adaptive optimizers, so there is a gap between the formal guarantee and the empirical regime. Most ML theory papers face this discrepancy, but the paper would benefit from an explicit caveat: "proved for GD; we verify empirically that injectivity holds for models trained with Adam."

3. **No dedicated limitations section.** Several important scope clarifications are scattered across the paper (e.g., threat model in §3, failure cases in §2) but a consolidated limitations discussion would help readers. Points that should be explicitly listed include: (a) the algorithm requires per-position hidden states, not just the final hidden state; (b) the theoretical guarantee is for GD, not Adam; (c) weight tying is not analyzed; (d) the analysis is restricted to decoder-only architectures.

4. **The threat model for SIPIT is narrow.** The algorithm requires access to the full per-position hidden-state sequence at a given layer (e.g., via a leaked KV-cache). The paper is honest about this ("designing an efficient algorithm for [inversion from only the final embedding] is nontrivial and left to future work"), but the framing as a breakthrough for transparency should be tempered by the acknowledgment that many practical settings (e.g., API access with logprobs only) are outside its scope. This is a scope limitation, not a flaw, but it affects the significance claim.

### Trivial

5. **Acronym inconsistency.** The abstract introduces "SIFT," the algorithm section defines "SIPIT" (Sequential Inverse Prompt via ITerative updates), and the experiments use "SiPT" and "SIFT" interchangeably. These should be harmonized throughout.

6. **Collision search methodology could be clearer.** The paper states that representations were "systematically checked" via "5 billion pairwise comparisons." It is not fully specified whether hashing, exact floating-point equality, or threshold-based comparison was used. The minimum distances reported are well above 10⁻⁶, but clarifying the exact procedure (e.g., "no two prompts produced hidden states with L2 distance below machine epsilon") would improve precision.

---

## Nice-to-Haves

- An explicit discussion of whether the theoretical result extends to tied embeddings, and a report of which tested models use weight tying.
- A short paragraph noting that the theoretical proof covers GD, and that the empirical validation on Adam-trained models provides supporting evidence beyond the formal scope.
- A sketch of the gradient-guided candidate policy (Algorithms 2 and 3, currently in the stripped appendix) in the main text, even at a high level.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that Algorithms 2 and 3 are missing from the main paper.** These are in the appendix, which is stripped by the PDF parser. Per the instructions, weaknesses about missing appendix content are removed.
- **Criticism that the paper does not confirm which activations are analytic in tested models.** The paper states in §5 and Appendix F that all activation functions in tested models are analytic. Removed as the paper addresses this.
- **Criticism about the HardPrompts comparison being unfair.** The paper explicitly notes that HardPrompts is designed for a different task and uses the comparison only to show that approximate methods fail at exact inversion. Removed as the paper already addresses this.
- **Strength about layer-depth runtime analysis (Figure 6) being a major contribution.** This figure is nice supporting evidence but not a core contribution; moved here to avoid inflating strength count.

---

## Novel Insights

The rigorous connection between the standard argument (real-analytic functions → zero sets are measure-zero → random initialization avoids them) and the preservation under gradient descent via absolute continuity of the parameter-law pushforward is well-executed but follows a known template in theoretical ML (e.g., Kileel et al. 2019 on injectivity of deep ReLU networks; Sutter et al. 2025 on Transformers at initialization). The genuinely novel operational contribution is SIPIT — the insight that injectivity + causal structure enables a simple iterative search with a provable linear-time guarantee transforms a theoretical property into a concrete tool. The robustness guarantee (Theorem 3.2) and its empirical confirmation on quantized models are the most practically significant results.

---

## Suggestions

1. Add a discussion of weight tying and its effect on the measure-zero argument, either proving the result still holds on the constrained subspace or explicitly stating it as a scope limitation.
2. Add a sentence in the abstract or main result qualifying that the formal proof covers GD (with empirical verification on Adam).
3. Add a dedicated limitations section consolidating the scope boundaries (optimizer coverage, threat model, architecture class, weight tying).
4. Harmonize the acronym (SIFT/SIPIT/SiPT) throughout.

---

## Score and Decision

### Calibration Report

**Round 1 (bracketing):** Queried for papers on transformer injectivity/invertibility/hidden-states reconstruction across three bands.

- Weak band (avg < 3.5): returned scores 3.00–3.40 (papers on circuit analysis, knowledge recovery, inductive transformers)
- Middle band (3.5–7.5): returned scores 4.67–7.00
- Strong band (avg > 7.5): returned scores 7.60–8.67

Initial bracket estimate: **5.5–7.5**.

**Round 2 (narrowing):** Queried for papers on (a) transformer theory/proof results and (b) provable language model inversion/reconstruction, both within (5.5–7.5).

- Anchor `6S4WQD1LZR` — "Transformers are Universal In-context Learners" — avg 6.67, Accept. Pure theory, no experiments. This paper is stronger because it combines theory with extensive experiments.
- Anchor `VoLDkQ6yR3` — "Understanding Reconstruction Attacks with the NTK" — avg 6.67, Accept. Theory + experiments on data reconstruction. Structurally comparable, similar balance of theoretical and empirical contributions.
- Anchor `YzxMu1asQi` — "Scaling Laws for Adversarial Attacks on Language Model Activations" — avg 6.50, Accept. Empirical + theory on LLM activation attacks. This paper has a cleaner theoretical core.
- Anchor `1lFZusYFHq` — "How Transformers Implement Induction Heads" — avg 6.20, Reject. Theory paper with some gaps.
- Anchor `YE6N8htoFQ` — "Vocabulary In-Context Learning" — avg 6.00, Reject.
- Anchor `WULjblaCoc` — "When Can Transformers Count to n?" — avg 5.60, Reject.
- Anchor `GlPVnuL66V` — "Provable Privacy Attacks on Trained Shallow Neural Networks" — avg 6.00, Reject.

**Comparison against anchors:** The paper under review is clearly stronger than the 5.6–6.2 papers, which were rejected. It is comparable to the 6.50–6.67 anchors, which were accepted. The paper has stronger empirical support than the 6.67 theory-only anchor, and a cleaner theoretical contribution than the 6.50 adversarial-attacks anchor. The weight-tying gap and GD/Adam gap are real but addressable and do not sink the core contribution.

**Final score: 6.5** — solid contribution with clearly articulated theoretical results, strong empirical validation, and a practical algorithm, held back from a higher score by the weight-tying omission and the unacknowledged GD/Adam gap.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>