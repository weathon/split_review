Now I have all the information I need. Let me compose the final review.

**Round 1 bracketing**: I placed the paper between roughly 3.5 and 8. The low anchors (score 3.0–3.25, e.g., NSBP7HzA5Z, fSbPwHjdDG) had unclear or weak contributions. The paper is clearly above those. The high anchors (score 6.67–7.60, e.g., STUGfUz8ob, hwSmPOAmhk) are accepted papers with tight theory-practice alignment and strong experiments. The current paper has gaps preventing it from reaching that tier. This brackets the score to roughly (4.5, 6.5).

**Round 2 narrowing**: I examined anchors in (4.5, 6.0) and (6.0, 7.5). The strongest comparison is to "Language Model Inversion" (5.50, Accept): that paper is empirically oriented with weaker theory but better alignment between claims and experiments. The Induction Heads paper (6.20, Reject) has solid theory on simplified models but was rejected for practical relevance gaps — similar to the dynamic here. The current paper has stronger theory than the LM Inv paper but worse claim–experiment alignment. I judge it comparable to the Induction Heads paper but slightly weaker due to the mismatch between what the theory proves and what the experiments test.

Final score: 5.5, Decision: Reject.

## Summary

This paper proves that decoder-only Transformer LMs are almost-surely injective (different prompts → different last-token hidden states) at initialization and that GD-based training preserves this property. It then introduces SIFT, an algorithm that recovers the exact input prompt from per-token hidden states. The theoretical argument — using real-analyticity to show collision sets have measure zero — is clean and mathematically sound under its stated assumptions. The empirical collision search over six models and the inversion experiments demonstrate the phenomenon holds in practice.

## Strengths

- **Provably establishes injectivity at initialization (Theorem 2.2).** The proof uses the real-analyticity of the transformer map (Theorem 2.1) plus a constructive argument to rule out the identically-zero case, showing the collision set has measure zero. The argument is rigorous under standard assumptions (analytic activations, LayerNorm with ε>0, etc.) and does not rely on asymptotics.

- **Proves injectivity is preserved under GD-based training (Theorem 2.3, Corollary 2.3.1).** The paper shows that a GD step is a real-analytic map with non-identically-zero Jacobian determinant, so by the Inverse Function Theorem it preserves absolute continuity of the parameter distribution, preventing concentration onto the measure-zero collision set. Corollary 2.3.1 extends this to SGD and mini-batch GD with arbitrary batch selections. This goes beyond prior work (e.g., Sutter et al. 2025) which only covered initialization.

- **Introduces SIFT, a practical algorithm for exact prompt recovery from hidden states.** The algorithm exploits causal structure and local injectivity to reconstruct the input token-by-token. Empirical results show 100% token-level accuracy on GPT-2 Small, with gradient guidance reducing search to a small fraction of the vocabulary (Table 5). The algorithm is robust to FP4/INT8 quantization noise (Table 4) and scales gracefully to large models.

- **Empirical evidence of injectivity on real models up to 70B parameters.** The collision search covers six state-of-the-art models (GPT-2, Gemma-3, Llama-3.1, Mistral, Phi-4, TinyStories) across billions of pairwise comparisons, with minimum L2 distances consistently far above any plausible collision threshold (Tables 1–3, Figures 3–5). This includes FP4-quantized models up to 70B parameters.

## Weaknesses

### Major

- **The training preservation theorem covers gradient descent, but all experimentally tested models were trained with Adam.** Theorem 2.3 and Corollary 2.3.1 are proven for GD, SGD, and mini-batch GD with step sizes in (0,1). Every model evaluated in §4 (GPT-2, Llama, Mistral, Phi, Gemma) was trained with Adam or a similar adaptive optimizer, which uses element-wise scaling and moving averages — dynamics not covered by the proof. The paper never acknowledges this gap and states the theory applies to "standard training procedures." Since the proof relies on the update map being a local diffeomorphism (a property that may not hold for Adam's update rule), the theoretical guarantee does not formally extend to any of the models on which experiments are run. The empirical results in §4 thus serve as independent validation of the phenomenon, but not as confirmations of the theorem. The authors should either extend the theory to cover Adam, or explicitly bound the theoretical claims to GD and explain why the experiments on Adam-trained models remain relevant.

### Minor

- **The algorithm uses per-token hidden states, not the last-token state that the theory is about.** The paper's headline claim is that *last-token* representations are injective. Yet SIFT assumes access to the full hidden-state matrix at some layer. The paper acknowledges this ("designing an efficient algorithm for that setting is nontrivial and left to future work"), which is commendable honesty, but it means the constructive inversion result does not operationalize the paper's core theoretical finding. The algorithm works with strictly more information than the theory concerns.

- **The comparison against HARDPROMPTS is uninformative.** HARDPROMPTS (Wen et al., 2023) is a method for *prompt optimization* (finding a new discrete prompt that maximizes an objective), not for reconstructing an existing input from hidden states. Reporting that it achieves 0% accuracy is expected and does not constitute a meaningful baseline. A more informative comparison would be against embedding similarity / nearest-neighbor search in embedding space, or against a simple linear probe decoding the hidden state.

- **The "provable linear-time guarantee" (Theorem 3.1: at most T|V| steps) is a trivial worst-case bound** that any enumeration algorithm would satisfy. There is no analysis of when the gradient-guided policy improves on this bound, and no expected runtime guarantee. The paper would benefit from either a non-trivial theoretical analysis of the gradient guidance or a more measured characterization of the guarantee.

- **The empirical search for collisions (100k prompts from 4 datasets) samples an infinitesimal fraction of the astronomically large prompt space.** This is not a flaw in the paper since the theory already establishes injectivity formally, but the paper frames these experiments as "validating" or "confirming" the theory (§4: "extensive empirical evidence supporting our theory"), which oversells what random sampling can demonstrate. The experiments are better described as sanity checks or demonstrations of practical separation margins, not confirmatory evidence for a measure-zero claim.

- **The inversion experiments (Table 5) use only 100 prompts of 20 tokens each.** This is a small-scale proof-of-concept. While SIFT achieves 100% accuracy, the scale is too limited to draw strong conclusions about general applicability.

### Trivial

- Algorithm 1 does not specify the POLICY function in the main text (referring instead to appendix algorithms). The main text would benefit from at least a sketch of how candidates are selected.

## Nice-to-Haves

- Ablate the gradient guidance by comparing SIFT with different candidate-selection policies (embedding similarity, random, gradient-guided) to quantify the speedup.
- Discuss the computational cost of verifying a single candidate token (requires a forward pass from the prefix) more explicitly.
- Mention that the theoretical results assume deterministic forward pass (no dropout at inference) — the paper already excludes this implicitly but would benefit from making it explicit.

## Removed Points

These points were flagged but removed because they are speculative, factually incorrect, or nitpicks that do not survive verification against the paper:

- **Critique about "unrealistic training assumptions" (dropout, LR schedules, weight decay):** The paper's Corollary 2.3.1 already handles stochastic/mini-batch batch selection. The critic's concerns about dropout during training and LR schedules violating the (0,1) step-size assumption are conjectures about what the theory *doesn't* cover rather than actual errors in what it *does* cover. The paper states its assumptions clearly; criticizing it for not covering settings outside those assumptions is scope creep.

- **Critique about insufficient experimental evidence for global injectivity (100k samples from huge space):** The paper's theory already proves injectivity; the experiments are illustrative demonstrations of practical separation margins, not formal proof. The critic's demand for "adversarial optimization to find collisions" is reasonable as a suggestion but does not constitute a weakness since the theoretical result already provides the guarantee.

- **Claim that the proof sketch's "freeze the network" construction ignores LayerNorm's ε>0:** This is speculative without seeing the full appendix. The main text describes a construction to show h is not identically zero; whether this construction respects LayerNorm details would need to be checked in the full proof, which is stripped from this version.

- **Strength Finder claims about "5+ billion pairwise comparisons":** This is a numerically correct framing of 100k prompts choose 2, matching what the paper reports. Kept as a genuine strength.

## Novel Insights

None beyond the paper's own contributions. The reviews largely agree on the strength of the theoretical core and raise similar concerns about practical alignment.

## Suggestions

1. **Acknowledge the GD/Adam gap explicitly and either**: (a) extend the theory to cover Adam by showing that Adam's update map also preserves absolute continuity under similar assumptions, or (b) clearly limit the theoretical claim to GD/SGD-trained models and explain why the experiments on Adam-trained models are still informative (e.g., as independent empirical evidence of the phenomenon, not confirmation of the theorem).

2. **Provide a meaningful baseline for the inversion experiments** — at minimum, compare SIFT against nearest-neighbor search in embedding space and against a simple argmax over token embeddings from the hidden state.

3. **Either demonstrate inversion from the last-token state only** (even if less efficient), since that is the setting the theory directly addresses, or restructure the paper's narrative so the algorithm is framed as a separate contribution that exploits causal structure rather than as a direct operationalization of the last-token injectivity theorem.

4. **Avoid framing trivial bounds as contributions.** The T|V| guarantee is correct but carries no information. Instead, highlight the practical efficiency (empirical ~0.2% vocabulary exploration) and provide an expected-case analysis.

## Score and Decision

**Bracketing and narrowing summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| NSBP7HzA5Z (Inductive Transformers) | 3.00 | R1 | Weaker — unclear contribution, rejected. Current paper much stronger. |
| 4y3GDTFv70 (Latent Space Theory) | 3.25 | R1 | Weaker — emergent abilities theory, limited rigor. Current paper stronger. |
| YE6N8htoFQ (Vocabulary ICL) | 6.00 | R1/R2 | Similar tier — strong theory with practical gaps, rejected due to proof gaps. Current paper has fewer proof gaps. |
| 1lFZusYFHq (Induction Heads) | 6.20 | R1/R2 | Strong theory on simplified models, rejected for practical relevance gaps. Comparable dynamic. |
| t9dWHpGkPj (Language Model Inversion) | 5.50 | R2 | Weaker theory but better claim–experiment alignment, accepted. Current paper stronger theoretically but weaker empirically. |
| STUGfUz8ob (Abstract Symbols) | 7.60 | R1 | Stronger — tight theory-practice link, good experiments. Current paper's gaps prevent reaching this tier. |
| hwSmPOAmhk (Factual Recall) | 7.33 | R1/R2 | Stronger — clean theoretical claims with clear empirical support. Current paper has larger theory-practice gaps. |

**Round 1 bracket:** The paper sits well above the weak 3.0–3.25 band but below the 7+ strong-accept band, placing it between 4.5 and 6.5.

**Round 2 narrowing:** Against the R2 anchors, the paper is most comparable to the Induction Heads paper (6.20, Reject) and the LM Inversion paper (5.50, Accept). It has stronger theory than the LM Inv paper but weaker claim–experiment alignment than either. The GD/Adam gap and the per-token vs last-token algorithm issue are structural mismatches that prevent a higher score. I therefore place it at 5.5.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>