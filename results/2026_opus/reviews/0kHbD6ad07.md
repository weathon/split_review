I have a good initial bracket. The paper sits between solid theoretical contribution territory (6-7) and accepted theoretical analysis papers (7.5-8). Let me narrow.I have enough evidence to score. Now let me write the final review.

## Summary
The paper proves that decoder-only Transformer language models are almost surely injective from prompts to last-token hidden states, both at random initialization and after any finite number of (S)GD steps with step sizes in (0,1). It supports the theorem with billions of pairwise collision tests across six model families (up to 70B parameters, including FP4/INT8 variants), all yielding zero collisions, and introduces SIPIT, a training-free algorithm that exactly recovers the input prompt from per-position hidden states at a chosen layer in worst-case O(T|V|) time.

## Strengths
- **Injectivity extended from initialization to the whole training trajectory** (Theorem 2.3 and Corollary 2.3.1). Prior work (Sutter et al. 2025) handled only initialization; the analytic-Jacobian argument here pushes it through any finite number of (S)GD steps with η∈(0,1) and arbitrary (even adversarial) batch selection, with a proof sketch that is clean and convincing.
- **Constructive exact-recovery algorithm with a provable linear-time bound** (Algorithm 1, Theorems 3.1 and 3.2). SIPIT is training-free, exact, and includes a noise-robustness statement tied explicitly to Δ_{π,t}. In Tables 4 and 5 it achieves 100% accuracy while exploring 0.19–0.22% of the vocabulary on Mistral-7B and Llama-3.1-8B, well below the worst-case bound.
- **Empirical collision search at non-trivial scale** (Section 4.1, Figure 3, Tables 1–3). ≈5 billion pairwise comparisons across GPT-2, Gemma-3, Llama-3.1, Mistral, Phi-4, TinyStories, plus FP4/INT8 variants and 14B/70B models, with all minimum distances orders of magnitude above the 10⁻⁶ threshold. The empirical regime is well-matched to the theorem's scope.
- **Explicit, honest characterization of failure cases** (end of §2). The paper names the concrete adversarial constructions (tied embeddings of distinct vocabulary items, identical positional embeddings) under which injectivity fails, which is unusual and useful.

## Weaknesses

### Fatal
None.

### Major
- **The abstract's "exact input text from hidden activations" rhetorically conflates the central theorem (last-token injectivity) with what SIPIT actually does (inversion from full per-position hidden states at some layer ℓ).** The threat-model paragraph in §3 and Eq. 5 are explicit that SIPIT "assume[s] access to all per-position states at a given layer ℓ" and defers single-last-token inversion to future work, but the abstract and §1 ("the first algorithm that provably and efficiently reconstructs the **exact** input text from hidden activations") leave the impression that the algorithm operationalizes the headline theorem. This is a real framing gap and the abstract should be tightened to state SIPIT's access model.
- **The most informative baseline is missing from Table 5.** Thomas et al. (2025) is cited in §5 as "[m]ost closely related" — sequential prompt recovery from hidden states using an LLM-based policy — yet Table 5 compares only against HardPrompts (Wen et al. 2023, a discrete prompt-optimization method that targets downstream behavior, not hidden-state inversion) and an internal BRUTEFORCE ablation. HardPrompts scoring 0.00 is uninformative because it was not built for this task. Without a comparison against Thomas et al., the empirical claim of unique exact-recovery capability rests largely on an off-target baseline plus a self-ablation.

### Minor
- **The activation/quantization caveats are softer in the abstract than in the body.** Theorem 2.1 assumes real-analytic activations (tanh, GELU, SiLU), excluding ReLU; quantization breaks the absolute-continuity assumption on parameters. The paper acknowledges this at the end of §2 ("collisions can be manufactured … through deliberate non-analytic choices (quantization, non-smooth activations)"), and the FP4/INT8 results in §4.1 carry the empirical weight there. Still, the abstract would be sharper if it stated which activation classes the formal guarantee covers.
- **The "linear time" framing understates the |V| factor.** Theorem 3.1's bound is T|V|, and the empirical demonstrations on Llama-3.1-8B (|V|≈128k) depend on the gradient-guided POLICY exploring 0.19–0.22% of vocabulary (Table 4). The paper is honest in §4.2, but a reader of the abstract may assume T is the binding cost when in practice |V| (combined with the POLICY heuristic) is.
- **Threat-model loose phrasing.** §3 lists "leaked KV-cache" as an access vector, but KV caches store K and V, not residual-stream hidden states. The result presumably extends because K, V are deterministic functions of the hidden states, but the paper does not state this.
- **Figure 5 caveat.** The "collisions unlikely at any sequence length" reading (§4.1) is over a sampled mixture of prompts of varying length, not the same prompt extended in a controlled way. The empirical pattern is reassuring but the conclusion is slightly broader than the design supports.
- **FP4/INT8 interpretation.** Calling "more than doubles the minimum distance … thereby preserving the integrity of the representation space" overstates what the larger L2 gap shows; quantization noise scattering representations is consistent with the same observation. The genuinely supported claim — "no collisions appear under quantization" — is what the tables actually establish.

### Trivial
- §6's leap from injectivity of inference-time hidden states to the regulatory framing (Hamburg DPA / HmbBfDI) extrapolates somewhat beyond what the technical results support, since the exact hidden state is rarely the object stored or transmitted. Useful as motivation, but should not be weighted as a contribution.

## Nice-to-Haves
- A worst-case-exponential algorithm that inverts from the single last-token state alone, even on small models, would more directly operationalize the central theorem and dramatically sharpen the headline.
- Tracking minimum pairwise distance along a real training run (rather than only init + already-pretrained checkpoints) would directly stress-test the dynamical claim of Theorem 2.3.
- A one-paragraph technical contrast with Sutter et al. (2025) explaining precisely what their proof covers and what the delta here is would help readers locate the theoretical novelty.
- Practical characterization of *near*-collisions: which architectural choices (tied embeddings, normalization variants, particular tokenizer constructions) are most likely to push the min-distance close to (but not exactly at) zero.

## Removed Points
*These points were flagged from the harsh review and removed; treat them with caution.*
- "The §2.3 Corollary 2.3.1 Jacobian step needs the η-vs-Hessian tie-in" — the paper restricts η∈(0,1), states the determinant is nonzero by evaluating at a constructed point, and defers details to the appendix. The parser strips appendices, so we cannot adjudicate the bound. Demoted per the speculative-fatal rule.
- "Quantization breaks the proof" — the paper explicitly scopes quantization out of the formal guarantee and treats it as a separate empirical study with consistent findings; this is acknowledged scoping, not a hidden flaw.

## Novel Insights
None beyond the paper's own contributions. The paper's framing — viewing decoder-only Transformers as real-analytic functions of parameters and using the zero-set dichotomy to lift injectivity from a single parameter setting to almost-sure guarantees throughout training — is itself the insight, and the reviewers' useful observations are about how to communicate that result more sharply rather than additions to it.

## Suggestions
- Rewrite the abstract to (i) state that SIPIT inverts from per-position hidden states at a chosen layer, and (ii) explicitly note the activation class (real-analytic; ReLU excluded) and that quantization is studied empirically rather than covered by the formal theorem.
- Add Thomas et al. (2025) as a baseline in Table 5 under matched conditions. This is the comparison readers will look for.
- In §3, clarify whether SIPIT can run from K, V only or requires the residual-stream hidden states, and tighten the "leaked KV-cache" example accordingly.
- Reframe the FP4/INT8 finding around what the data supports ("no collisions observed under quantization") rather than the integrity-of-representation-space language.

## Evaluation Axes
- **Originality**: High. Lifting injectivity from init-only to the full training trajectory via a real-analytic-Jacobian argument is genuinely new relative to Sutter et al. (2025), and SIPIT is, to the reviewer's knowledge, the first training-free exact-recovery algorithm for decoder hidden states with a worst-case bound.
- **Importance**: High. The result clarifies a recurring informal claim about Transformers and has direct implications for interpretability, probing, and the privacy/regulatory treatment of cached hidden states.
- **Claim support**: Mostly strong. The theorems are stated carefully; the empirical sweep is large and well-designed. The main mismatch is the abstract's framing of SIPIT.
- **Soundness of experiments**: Strong on the collision sweep; weaker on the inversion baseline choice.
- **Clarity**: Good overall; abstract/§1 framing should be tightened.
- **Value to the community**: High — provides both a clean theorem and a reusable, training-free inversion algorithm with open code.

## Anchors
Across all rounds:
- `NSBP7HzA5Z.md` (3.00, round 1, weak band) — inductive bias for transformer concepts; clearly weaker, mostly opinion-driven, far below this paper.
- `89wVrywsIy.md` (3.40, round 1, weak band) — circuit-tracing framework with thin evaluation; weaker.
- `fSbPwHjdDG.md` (3.00, round 1, weak band) — Llama "thinks in English"; substantially less rigorous.
- `q541p2YLt2.md` (2.50, round 1, weak band) — softmax attention instability; substantially less rigorous.
- `WULjblaCoc.md` (5.60, round 1+2, middle band) — When Can Transformers Count to n; clean theoretical+empirical paper, narrower than this paper's scope.
- `YE6N8htoFQ.md` (6.00, round 1+2, middle band) — VICL positional encoding UAP, comparable theoretical flavor; this paper has broader empirical sweep and a working algorithm.
- `1lFZusYFHq.md` (6.20, round 1, middle band) — induction-heads approximation/optimization; comparable theoretical paper, narrower scope.
- `6S4WQD1LZR.md` (6.67, round 1+2, middle band) — Transformers are Universal In-context Learners; comparable in clean-theorem style; this paper has stronger empirics + algorithm.
- `gbrHZq07mq.md` (5.60, round 2, middle band) — Logical languages by transformer encoders; theoretical, narrower.
- `U49N5V51rU.md` (6.80, round 2, **read in full**) — Length generalization formal framework; theoretical + empirical validation; the paper under review has comparable rigor with broader empirical reach and a working algorithm — I rate it slightly above this anchor.
- `VoLDkQ6yR3.md` (6.67, round 2, **read in full**) — Reconstruction attacks via NTK; combines provable recovery + empirics, structurally very similar; the paper under review is at least at parity in rigor and clarity.
- `bVTM2QKYuA.md` (6.75, round 2) — Representation geometry of features; similar formal-+-empirical flavor.
- `d63a4AM4hb.md` (7.00, round 2) — "Not All Language Model Features Are Linear"; this paper is at least comparable.
- `KSBx6FBZpE.md` (6.25, round 2) — Latent memories in LLMs; weaker theory.
- `7erlRDoaV8.md` (7.50, round 2) — Deleting sensitive info from LLMs; closely related privacy theme.
- `GlPVnuL66V.md` (6.00, round 2) — Provable privacy attacks on shallow nets; narrower scope.
- `STUGfUz8ob.md` (7.60, round 1, strong band) — When can transformers reason with abstract symbols; cleanly accepted strong paper.
- `n2NidsYDop.md` (8.67, round 1, strong band) — Parity via CoT; very strong theoretical contribution.
- `Tzh6xAJSll.md` (7.60, round 1, strong band) — Scaling laws for associative memories.
- `d8w0pmvXbZ.md` (8.00, round 1, strong band) — Small-scale proxies for training instabilities.

**Round 1 bracket**: between 5.5 and 8 — clearly above the weak band, plausibly in the upper-middle to lower-strong range.

**Round 2 narrowing**: The paper compares favorably to the 6.67–7.00 accepted anchors (`VoLDkQ6yR3` 6.67, `U49N5V51rU` 6.80, `d63a4AM4hb` 7.00). Like those, it combines a clean theorem with substantive empirics; unlike most of them, it also ships a working, exact-recovery algorithm with linear-time guarantees and code. It is not quite at the level of the 8.0+ anchors which are either deeply technical training-dynamics analyses or very tight single-axis results. The framing issues (abstract overreach, missing Thomas et al. baseline) are real but not structural. Final bracket narrowed to 7.0–7.5; the framing gaps push to the lower end of that.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>