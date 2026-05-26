## Summary

This paper proves that decoder-only Transformers are almost surely injective: different prompts map to different last-token hidden states, both at random initialization and after training with gradient descent. The proof uses real-analyticity to establish that collisions occur only on a measure-zero parameter set, and that GD/SGD training preserves this property. The paper validates this empirically across 5 billion pairwise comparisons on six model families (GPT-2, Gemma-3, Llama-3.1, Mistral-7B, Phi-4, TinyStories), finding zero collisions with margins far above machine epsilon. It then introduces SIFT, an algorithm that exploits injectivity to recover the exact input prompt from per-position hidden states with O(T|V|) worst-case guarantees, and demonstrates 100% exact recovery at modest computational cost. The paper connects these findings to implications for interpretability and data-protection law.

## Strengths

- **Elegant and rigorous theoretical framework**: The proof strategy (real-analytic parameter-to-representation maps, measure-zero collision sets via the zero-set dichotomy, preservation under diffeomorphic training dynamics) is clean and well-motivated. Theorems 2.1–2.3 form a coherent argument that injectivity is a structural property, not an asymptotic or initialization-only one. The key technical step—showing that the function h(θ) = ‖r(s;θ) − r(s′;θ)‖² is not identically zero—is sketched with constructive parameter settings, and the full details are deferred to the appendix.

- **Extensive and convincing empirical validation**: The collision search on ~100k prompts (≈5 billion pairwise comparisons) across six model families reports zero collisions, with minimum L2 distances always above 10⁻⁶ and typically much larger (Figures 3–4, Tables 1–3). The experiments cover models from 33M to 70B parameters, multiple layers, and FP4/INT8 quantization, which significantly strengthens the claim. The fact that quantization *increases* minimum pairwise distances (Table 2) is a particularly striking robustness check.

- **First provable exact inversion algorithm from hidden states**: SIFT is presented with formal correctness (Theorem 3.1) and robustness (Theorem 3.2) guarantees. While the algorithm is a straightforward sequential-matching procedure given injectivity, the provable guarantee and empirical demonstration (100% accuracy, <0.22% vocabulary explored) are valuable. The paper correctly distinguishes SIFT from prior approximate inversion methods (Morris et al., Nazir et al., HARDPROMPTS) that operate under different threat models or lack exactness guarantees.

- **Clear articulation of practical implications**: Section 6 connects the theoretical and algorithmic findings to concrete consequences for interpretability ("if probes or inversion methods fail, it is not because the information is missing") and data-protection compliance (hidden states as lossless encodings of user input). This elevates what could be a purely theoretical result into a paper with broad relevance.

## Weaknesses

### Major

None. The paper's core claims are well-supported by both theory and evidence. No verified weakness threatens the validity of the main results.

### Minor

- **Scope gap between the training theorem and the experimental models**: Theorem 2.3 and Corollary 2.3.1 prove injectivity is preserved under **GD and SGD** (full-batch, mini-batch, and single-sample). Every pretrained model evaluated in Section 4.1 (GPT-2, Gemma-3, Llama-3.1, Mistral-7B, Phi-4) was trained with **Adam or AdamW**, whose element-wise adaptive scaling involves non-analytic operations (division by √(v̂ₜ)) that fall outside the proof's assumptions. The paper states "in practical training pipelines, injectivity is guaranteed" (Section 2, conclusion) and "across all practically relevant parameter settings and training procedures" (Significance, Section 1) without flagging that the formal guarantee covers only GD/SGD. This is a framing issue, not a technical error — the experiments provide strong evidence that injectivity generalizes beyond the proven setting — but the narrative would be strengthened by an explicit statement such as: "Our proof covers GD and SGD; adaptive optimizers involve non-analytic operations not formally covered, but our empirical results suggest the property holds more broadly."

- **SIFT's operational footprint is narrower than the narrative suggests**: The algorithm requires access to per-position hidden states at a chosen layer in full precision. The paper acknowledges this ("here we assume access to all per-position states at a given layer ℓ," Section 3) but frames SIFT as an operational tool for realistic settings repeatedly. In practice, an adversary with access to a leaked KV cache, a shared inference API, or intermediate representations would typically face quantized states, partial information, or logits-only access — scenarios where SIFT's exactness guarantee may not apply. A paragraph discussing this gap between the assumption and realistic adversarial constraints would make the contribution more self-contained and honest about scope.

- **Comparison to HARDPROMPTS is uninformative**: HARDPROMPTS (Wen et al., 2023) is designed for black-box adversarial prompt discovery, not for exact hidden-state matching. The paper acknowledges this difference but still presents it as a comparative baseline in Table 5, where it predictably achieves 0% accuracy. This comparison adds no useful signal and could be removed or moved to a "not directly comparable" note without loss.

- **Step-size constraint η ∈ (0,1) is stated without motivation**: Theorem 2.3 introduces this constraint but provides no intuition for why it is needed or how it interacts with the proof (e.g., whether it arises from spectral-radius considerations or from the specific construction showing det Dφ is not identically zero). A sentence of motivation would help readers gauge the proof's generality without needing to reconstruct the argument from the appendix.

### Trivial

- **Naming inconsistency**: The algorithm is introduced as "SIPIT" (Sequential Inverse Prompt via ITerative updates) in Section 3 but called "SIFT" in the abstract, introduction, Figure 1, and all experimental sections (Tables 4, 5, Section 4.2). These should be unified. (The acronym "SIFT" is never expanded, and "SIPIT" does not cleanly match its spelled-out name.)

## Nice-to-Haves

- A discussion of realistic adversarial settings that SIFT *cannot* handle (e.g., KV-cache leakage with quantized states, API exposing only logits, access only to the final-layer embedding) would clarify the boundary between the theoretical result and its practical deployability.
- The collision search tests 100k prompts — a vanishingly small sample of |𝒱|^{≤K} — but the paper correctly frames this as a consistency check rather than a proof. Adding a note that the empirical results serve as a sanity check on the theory, not as exhaustive verification, would prevent misinterpretation.

## Removed Points

These points from the harsh critic or strength finder were flagged for removal; treat them with caution:

- **Harsh critic's concern about proof hardness of Theorem 2.3**: The critic questions whether the step-size constraint η ∈ (0,1) guarantees det Dφ ≠ 0. This misinterprets the proof structure — the argument does not claim η ∈ (0,1) guarantees non-zero determinant everywhere, but rather that det Dφ is real-analytic and not identically zero (which can be checked at a single parameter setting). The critic's eigenvalue concern (1/η) misses that the construction can pick a point where the Hessian is zero, avoiding the issue. This concern is not well-supported given the sketched argument.
- **Critic's claim that the collision-search sample is too small**: The theory predicts measure-zero collision sets, so even a single counterexample would refute the claim. The empirical validation is correctly framed as a consistency check; sample size is not a meaningful weakness here.
- **Critic's claim that the paper does not honestly discuss SIFT's limitations**: The paper explicitly states the assumption of access to per-position states (Section 3, "Threat model"). The limitation is acknowledged, though the discussion could be expanded — this is kept as a Minor weakness rather than removed entirely.
- **Strength finder's generic framing of "clear practical implications"**: The paper's Section 6 does articulate concrete implications for interpretability and data-protection law, which are specific and well-supported. This strength is retained.

## Novel Insights

None beyond the paper's own contributions. The key observation — that the discrete-to-continuous map from prompts to hidden states is almost surely injective despite non-injective components — is the paper's own central claim. The proof technique of leveraging real-analyticity to establish measure-zero collision sets and diffeomorphic training dynamics to preserve them is clean but is rightly presented as the paper's contribution, not a meta-observation.

## Suggestions

1. **Add a scope clarification paragraph in Section 2** explicitly noting: "Our proof of training preservation covers full-batch and mini-batch SGD. Adaptive optimizers (Adam, AdamW) involve non-analytic scaling operations not covered by the formal guarantee. However, our empirical results on Adam-trained models (§4) suggest the property generalizes beyond the formally covered cases." This transforms a narrative weakness into an honest scientific contribution.

2. **Expand the threat-model discussion** in Section 3 to address realistic constraints (quantized states, logits-only access, KV-cache partial leakage) and explain which settings SIFT does and does not apply to.

3. **Remove or reframe the HARDPROMPTS comparison**: Either drop it entirely or add an explicit disclaimer that HARDPROMPTS solves a different problem and is included only to illustrate that black-box gradient-based methods are not designed for exact recovery.

4. **Add a brief justification for η ∈ (0,1)** in Theorem 2.3, explaining its role (e.g., ensuring the Jacobian is invertible at a particular parameter setting used to show det Dφ is not identically zero).

5. **Unify the algorithm name** throughout the paper (SIFT or SIPIT, but not both inconsistently).

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>