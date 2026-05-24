Now I have enough calibration data. Let me compile the final consolidated review.

## Summary

The paper proves that decoder-only Transformer language models are almost surely injective: distinct prompts map to distinct last-token hidden states. This is established theoretically (using real-analyticity, first at initialization, then preserved under gradient descent), validated empirically through billions of pairwise collision tests across six model families (zero collisions found), and operationalized via SIFT — an algorithm that recovers the exact input text from per-position hidden states with provable linear-time guarantees.

## Strengths

1. **Novel and nontrivial theoretical result about a fundamental property of Transformers.** The paper proves that decoder-only Transformers are almost surely injective at initialization (Theorem 2.2) and that this property is preserved under any finite number of gradient descent steps (Theorem 2.3). This goes cleanly beyond prior work (Sutter et al., 2025), which only established injectivity at initialization and only for the full hidden-state matrix rather than the task-relevant last-token state. The proof framework — leveraging real-analyticity to show collisions are measure-zero events and then showing GD preserves absolute continuity of the parameter distribution — is elegant and rigorous.

2. **First provably exact inversion algorithm with linear-time guarantees.** SIFT (Section 3, Algorithm 1) is proven correct (Theorem 3.1) and robust to perturbations (Theorem 3.2). In practice it explores <0.22% of the vocabulary on average (Table 4), while prior methods (HARDPROMPTS, Morris et al.) are approximate and lack guarantees.

3. **Extensive and convincing empirical validation.** The collision search (~5 billion pairwise comparisons across GPT-2, Gemma-3, Llama-3.1-8B, Mistral-7B, Phi-4-mini, TinyStories-33M) finds zero collisions, with minimum L2 distances far above the 10⁻⁶ threshold. The validation extends to FP4/INT8 quantized models and models up to 70B parameters, where injectivity is again confirmed (Tables 2, 3). This provides strong support that the measure-zero collision set is indeed avoided in practice.

4. **Clear practical and conceptual significance.** The result reframes the common intuition that Transformer nonlinearities cause information loss: the discrete-to-continuous map from prompts to hidden states is structurally lossless. This has direct implications for interpretability (probes failing because information is absent is not a concern), privacy (hidden states are lossless encodings of user text), and safe deployment.

## Weaknesses

### Fatal
None.

### Major

1. **The adversarial batch claim in Corollary 2.3.1 is not supported by the sketched argument.** The proof sketch asserts that "at the point θ_* from the single-sample proof . . . the batch Jacobian coincides with the single-sample one by linearity of differentiation, and its determinant is therefore also nonzero." The Jacobian determinant of I − ηH_B is not linear in the Hessian, and the reasoning that it is "sample-independent" at θ_* is not justified. More importantly, "adversarial" batch selections where B_t depends on θ_t would mean the overall update is not a composition of fixed maps φ_B, breaking the absolute-continuity argument. The core result for full-batch GD and fixed-batch SGD remains intact, but the claim about "adversarial" batches overreaches. This should be corrected by restricting to non-adaptive batches. *(Verification: seen in lines 129–131 of the paper.)*

2. **Mismatch between the optimizer covered by the theory (GD) and the models used in experiments (trained with Adam).** Theorem 2.3 is proved for gradient descent with step sizes in (0,1). The experiments, however, use pretrained models (GPT-2, Gemma, Llama, Mistral, Phi) that were trained with Adam, not GD. While the empirical observation of injectivity on these models is reassuring and useful, it is not covered by the theoretical guarantee. The paper would benefit from explicitly acknowledging this gap and framing the experiments as empirical evidence for the injectivity property itself (which is independent of optimizer), rather than as validation of the training-preservation theorem specifically.

### Minor

1. **SIFT requires per-position hidden states, not just the last-token state.** The paper acknowledges this clearly in the threat model (Section 3: "here we assume access to all per-position states at a given layer ℓ"), but the abstract and title ("exact input text from hidden activations") could mislead readers into thinking inversion works from a single last-token vector. Adding an explicit caveat to the abstract would set correct expectations.

2. **Proof sketches in the main text are sparse at critical junctures.** The argument for Theorem 2.3 requires showing det(Dϕ) ≠ 0, but the sketch merely says "one can check this by evaluating at a simple parameter setting" without providing even a brief intuition (e.g., "when all gradients vanish, ϕ is the identity and det(Dϕ)=1"). While the full proof is in the appendix (which is stripped from this review), a self-contained sketch would build trust.

3. **No failure analysis for the inversion experiments.** SIFT achieves 100% accuracy on the tested prompts. It would strengthen the paper to test adversarial or stress-case prompts (e.g., very long sequences, repeated tokens, code, mathematical formulas) to probe the boundaries of practical inversion.

### Trivial
None.

## Nice-to-Haves
- A discussion of when non-analytic components (e.g., ReLU activations, tied embeddings) could cause injectivity to fail in practice, and whether failures are probable or pathological.
- An analysis of the gradient-guided candidate policy used in SIFT — why it works so well (exploring <0.22% of vocabulary) is currently only empirical; a theoretical bound or comparison to random search would deepen the contribution.
- Reporting the empirical margin (minimum distance / tolerance) across all tested pairs to assure readers that no near-collisions occur at the resolution relevant to detection.

## Removed Points
- **"The training-preservation argument does not support adversarial batch selections (Corollary 2.3.1)"** — RETAINED as Major weakness 1, but only the core criticism (the sketched determinant argument is sloppy; "adversarial" is overclaimed). The implication that it "weakens the paper's theoretical scope" is overstated since full-batch GD and fixed-batch SGD (the practically relevant cases) remain intact.
- **"The real-analyticity assumption for attention with causal masking"** — REMOVED. The paper acknowledges that in practice models use a finite large negative number (e.g., −1e9) rather than −∞, which suffices for analyticity. The reviewer's speculation about −∞ is addressed by the paper's modeling choice.
- **"HARDPROMPTS comparison is not directly comparable"** — REMOVED. The paper explicitly acknowledges this ("acknowledged as not directly comparable") and still reports the comparison. Including a known-weak baseline alongside the strong method does not harm the paper.
- **"Overstating legal implications"** — REMOVED. The Discussion section separates what the paper proves from what it suggests for policy, and the tone is measured. The claim that hidden states are lossless encodings is a direct consequence of the proved injectivity.
- **"The algorithm requires query budget up to |V| per token"** — REMOVED. This is the stated worst-case guarantee of the algorithm (Theorem 3.1: "at most T|V| steps"). It is presented honestly, not as a weakness.
- **"Lack of failure analysis"** — Demoted to Minor weakness 3. Valid but does not threaten the core claim.
- **All formatting/style nitpicks, missing appendix complaints, and pure reproducibility nitpicks** — REMOVED per hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the paper that the paper itself does not already articulate.

## Suggestions

1. **Correct the adversarial batch claim.** Restrict Corollary 2.3.1 to non-adaptive batch selections or provide a separate rigorous argument. This is a small fix that substantially improves credibility.

2. **Explicitly note the optimizer gap.** Add a sentence in the experimental section: "Our theorem covers GD training; the models tested were trained with Adam, so these experiments validate the injectivity property rather than the training-preservation theorem specifically."

3. **Add a caveat to the abstract.** E.g., "Our inversion algorithm assumes access to per-position hidden states (e.g., leaked KV-cache); recovery from a single last-token state remains an open problem."

4. **Include a simple concrete parameter setting for det(Dϕ) ≠ 0** in the sketch of Theorem 2.3.

## Score and Decision

### Calibration Summary

**Round 1 — Bracketing (bands: <3.5, 3.5–7.5, >7.5):**
- Weak band (avg 2.5–3.0): Papers on unrelated Transformer topics (training instability, optimization alternatives) — clearly inferior.
- Middle band (avg 5.25–7.33): "On Limitation of Transformer for Learning HMMs" (5.25, Reject), "What Does It Mean to Be a Transformer?" (7.00, Spotlight), "Understanding Factual Recall" (7.33, Spotlight), "Transformers can optimally learn regression mixture models" (6.80, Poster).
- Strong band (avg 7.60–9.00): "When can transformers reason with abstract symbols?" (7.60, Poster), "Transformers Provably Solve Parity" (8.67, Oral), "The mechanistic basis of data dependence" (9.00, Oral).

**Round 1 bracket:** The paper clearly sits in the 6–9 range — stronger than the rejected HMM paper (5.25) and the single-layer Hessian paper (7.00), but the question is where relative to the 7.33–8.67 anchors.

**Round 2 — Narrowing (6.0–8.0 and 7.0–9.5):**
Key comparisons:
- **"When can transformers reason with abstract symbols?" (avg 7.60)** — Studies reasoning under significant architectural simplifications (depth-1, no residual connections/LayerNorm). The current paper handles the full architecture, has more extensive experiments, and has a practical algorithm. The current paper is stronger.
- **"Wide Neural Networks Trained with Weight Decay Provably Exhibit Neural Collapse" (avg 7.60, Oral)** — Strong theory but requires multiple linear layers and pyramidal architecture assumptions. The current paper's injectivity result has fewer assumptions (standard architecture) and broader scope (theory + algorithm + experiments). Comparable quality.
- **"Understanding Factual Recall in Transformers via Associative Memories" (avg 7.33, Spotlight)** — Shallow transformers on synthetic tasks. Current paper is substantially stronger in scope and empirical validation.

The paper is clearly above the 7.00–7.33 range. It is comparable to the 7.60 anchors (which include Oral-level papers) but has a modestly broader contribution (theory of a fundamental property + practical algorithm + extensive real-model experiments). The weaknesses (adversarial batch overclaim, optimizer mismatch) are real but do not threaten the core contribution.

**Final score: 8.0** — an strong paper with a novel theoretical result, extensive empirical validation, and a practical algorithm, held back from a higher score by the overclaimed adversarial batch statement and the need to better scope the theoretical claims.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>