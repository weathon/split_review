## Summary

This paper proves that decoder-only transformer language models are almost surely injective (distinct prompts yield distinct last-token representations with probability one), that this property is established at initialization and preserved under gradient-based training, and introduces SIFT/SiPIT, the first algorithm to provably recover the exact input text from internal hidden states in linear time. The theoretical framework rests on real-analyticity of transformer components; the empirical validation covers ~5 billion pairwise comparisons across multiple model families with zero observed collisions.

---

## Strengths

- **Rigorous training-preservation of injectivity (Theorems 2.1–2.3):** The key advance over Sutter et al. (2025) — who establish injectivity only at initialization — is the argument that gradient descent maps are real-analytic with non-vanishing Jacobians, so they preserve absolute continuity of the parameter distribution and cannot push parameters into the measure-zero collision set. This is a clean and valid argument, and the distinction is important: injectivity as a transient initialization artifact would be much less interesting than injectivity as a structural property.

- **Large-scale empirical collision search with zero failures:** Across six primary models (GPT-2 S/M/L, Gemma3 1B/4B/12B), ~5 billion pairwise comparisons, and extended experiments on Llama-3.1-8B, Mistral-7B, Phi-4, TinyStories-33M, Phi-4 14B, and Llama-3.1-70B (Tables 1–3, Figure 3), no collisions are observed. Minimum distances are consistently orders of magnitude above the collision threshold of 10⁻⁶. This is a thorough, multi-scale empirical confirmation.

- **Provably correct and efficient inversion algorithm (SiPIT/SIFT):** Theorems 3.1 and 3.2 prove correctness and robustness with probability one in at most *T|V|* steps. Empirically, the algorithm achieves 100% token-level accuracy on GPT-2 Small in ~28 seconds mean time (Table 5), while BRUTEFORCE takes orders of magnitude longer and HARDPROMPTS fails entirely. Table 4 further demonstrates 100% accuracy on FP4-quantized Mistral-7B and Llama-3.1-8B while exploring less than 0.22% of the vocabulary, confirming linear-time scaling in practice.

- **Explicit acknowledgment of theory-algorithm access gap:** The paper explicitly notes in §3 (Threat Model): *"Our injectivity result guarantees that exact recovery from only the final embedding is possible in principle, but designing an efficient algorithm for that setting is nontrivial and left to future work; here we assume access to all per-position states at a given layer ℓ."* The gap is real but consciously scoped.

---

## Weaknesses

### Fatal
None.

### Major

- **Theory-algorithm access gap insufficiently foregrounded.** Theorems 2.1–2.3 target the *last-token* representation `r(s; θ)` as the injective encoding. The algorithm (§3, Algorithm 1) requires **all per-position hidden states** `H^{(ℓ)} ∈ ℝ^{T×d}` — a strictly richer access model. While the paper mentions this in the threat model paragraph, the introduction, abstract, and discussion sections repeatedly use phrasing like "recovering the exact prompt from hidden activations" or "hidden states are not abstractions but the prompt in disguise" without adequately distinguishing the single-last-token setting (what the theorem guarantees) from the full-matrix setting (what the algorithm exploits). This matters both for the paper's conceptual framing and for the practical privacy claims in §6: an adversary who possesses **all** per-position hidden states of a complete forward pass has already obtained far more than the last-token embedding. The headline theorem and the headline algorithm target different objects, and this conflation persists throughout.

- **No empirical comparison with Thomas et al. (2025).** Section 5 identifies Thomas et al. (2025) as "most closely related" — it recovers prompts from hidden states via a sequential algorithm operating in the same setting. Yet no empirical comparison appears. The paper explains qualitatively that Thomas et al. must score all vocabulary tokens before committing, which makes it a weaker variant, but this contrast is made only in prose rather than in numbers. Given that §4.2's central claim is that SiPIT's gradient-guided policy is both exact and efficient, situating it against Thomas et al. on even a small benchmark would substantially strengthen that claim.

- **Adaptive optimizers are unaddressed.** Theorem 2.3 explicitly requires step sizes η ∈ (0, 1) under vanilla GD. Corollary 2.3.1 extends to mini-batch and SGD. However, all of the models tested empirically — GPT-2, Gemma-3, Llama-3.1, Mistral-7B, Phi-4 — were trained with Adam or AdamW, whose per-coordinate effective updates can violate the η ∈ (0, 1) constraint in both direction and magnitude. The theorem's assumptions do not cover the actual training procedures of any model tested. The paper does not acknowledge this mismatch in the failure-cases or limitations discussion, and the empirical results cannot substitute for this because they test already-trained models rather than the training process itself.

### Minor

- **Unexplained and counterintuitive quantization distance increase (Table 2).** FP4 and INT8 weight quantization *increase* minimum pairwise distances compared to FP32 for all three tested models (e.g., Llama-3.1-8B: FP32 = 1.274, INT8 = 6.597, FP4 = 2.281). The paper presents this only as confirmation of "no collisions," without analysis. A plausible explanation is that quantization modifies representation scale or norm in ways that inflate L2 distances without reflecting genuine semantic separation; without normalization by representation magnitude or a mechanistic account, the meaning of this finding is unclear.

- **Collision threshold ε = 10⁻⁶ is unjustified.** This threshold is used universally across models ranging from TinyStories-33M to Llama-3.1-70B, at representations of vastly different dimensionalities and floating-point precisions. No justification is given for why 10⁻⁶ is the appropriate universal boundary. A threshold that depends on representation dimension *d* and typical representation norm would be more principled.

### Trivial

- **Algorithm naming inconsistency.** The algorithm is called SIFT (abstract, §1), SIPIT (§3 header), SIpIT (Algorithm 1), SiPT (§4.1, §4.2, Table 4, Table 5), and SiPIT (§6) throughout the paper. This is clearly an artifact of revisions and should be unified.

---

## Nice-to-Haves

- **Jacobian non-vanishing argument for Theorem 2.3.** The proof sketch says "one can check this by evaluating at a simple parameter setting." Even a one-sentence sketch of what that parameter setting is and why det Dφ(θ) ≠ 0 there would strengthen the intuition for readers, even if the full argument is in the appendix.
- **Brief mention of whether the framework extends to encoder-only models** (BERT-family) or encoder-decoder models, which also produce hidden states of practical interest for privacy analyses.
- **Normalization of Table 2 distances** (e.g., by per-layer representation norm) to disambiguate whether the quantization-induced distance increase is semantically meaningful or a scale artifact.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Framework is more about real-analytic functions on finite domains than transformers specifically"** (harsh critic, §2 note): While technically accurate that the measure-zero argument applies to any real-analytic family over a finite input domain, the paper's Theorem 2.1 establishing real-analyticity of the full transformer architecture is non-trivial and architecture-specific. The framing adds no actionable criticism.

- **"The training-preservation step may be fragile near convergence in overparameterized networks"** (harsh critic): This is speculative and not verifiable from the paper. The proof delegates to an appendix that is stripped; absent evidence that the argument fails, this should not be retained.

- **Comparison unfairness concern for HARDPROMPTS** (inferred from harsh critic): The paper is explicit that HARDPROMPTS targets approximate prompt optimization, not hidden-state inversion. The comparison is included to contextualize, not to claim superiority over a peer. Per the hard rules, comparisons where asymmetry favors the baseline should not be penalized.

- **Strength Finder's generic strength "establishes an important and interesting problem"**: Removed per filtering rules — no specific content anchor.

---

## Novel Insights

The most underappreciated contribution of this paper may be the precise scope of what the last-token injectivity guarantee *does* and *does not* imply for practical algorithms. The theory establishes that a single vector `r(s; θ) ∈ ℝ^d` uniquely encodes the entire input sequence, which is a remarkable information-theoretic statement — it says, in principle, that this one vector "contains" the full prompt. Yet the paper's own algorithm never inverts from that vector alone; it exploits the sequential structure token-by-token using all positions. This gap is not a failure of the paper but an open research frontier: constructing an efficient algorithm that inverts from the last-token state alone (perhaps by running the model autoregressively from a candidate sequence and comparing) would close the loop between the theory's headline claim and practical prompt extraction, and would constitute a substantially more threatening privacy result than the current one.

---

## Suggestions

1. **Rewrite the abstract and introduction** to clearly distinguish the access model of the theorem (last-token state) from the access model of the algorithm (full per-position hidden matrix). One sentence of disambiguation would prevent misreading.
2. **Add an explicit "Limitations" paragraph** in §6 noting: (a) the algorithm requires full per-position access, not just the last-token embedding; (b) the training-preservation proof covers GD and SGD but not Adam/AdamW; (c) the collision threshold ε = 10⁻⁶ is heuristic.
3. **Compare with Thomas et al. (2025)** on a small benchmark. Even a 10-prompt qualitative comparison would be informative.
4. **Provide even an informal account of the quantization distance phenomenon** in Table 2 — whether it is a norm/scale artifact or something more meaningful.
5. **Unify the algorithm name** across the entire manuscript before final submission.

---

## Evaluation on Core Axes

- **Originality:** Meaningful — the training-preservation result is new over Sutter et al. (2025), and the SiPIT algorithm is the first with provable exact recovery guarantees from hidden states.
- **Importance of research question:** High — touches injectivity as a foundational property of LLMs, with direct consequences for privacy and interpretability.
- **Claims well-supported:** Largely yes — proofs are present and empirical validation is extensive. The adaptive optimizer gap is the main unsupported claim in Theorem 2.3 relative to empirical practice.
- **Soundness of experiments:** Strong — multi-model, multi-scale, well-controlled. The baseline comparison is thin (no Thomas et al.), but what is there is convincing.
- **Clarity of writing:** Good, modulo the naming inconsistency and the conflated access models in the framing.
- **Value to research community:** High — provides theoretical grounding for a widely assumed but unproven property, operational tool for exact inversion, and a clear privacy implication.

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>