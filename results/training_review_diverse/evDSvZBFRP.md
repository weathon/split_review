Now I have a thorough understanding of the paper and can authoritatively evaluate the reviewer claims against the actual paper content. Let me produce the final consolidated review.

## Summary

This paper proposes a non-convex, set-based verification approach for transformers using polynomial zonotopes. The core technical contribution is preserving nonlinear dependencies across attention heads through exact matrix-set multiplication (Proposition 2), which generalizes prior convex-relaxation approaches (Bonaert et al., 2021) via a tunable precision parameter ρ_lim. The method is evaluated on four small binary-classification transformer models (medical safety and Yelp datasets), demonstrating 1.33×–1.82× larger verified embedding spaces than the zonotope baseline.

## Strengths

1. **Exact nonlinear dependency preservation in attention is novel and principled.** Unlike prior convex-relaxation methods that lose dependencies at each nonlinearity, Proposition 2 (Sec. 3.3) shows that the set-multiplication in attention (Eq. 11) is computed exactly using polynomial zonotopes. This is a genuine technical advance — the attention mechanism is the hardest part of transformer verification, and preserving its nonlinear structure is the right direction.

2. **Clean generalization of prior work with tunable precision.** The parameter ρ_lim controls how many higher-order terms are retained (Sec. 3.5, Algorithm 1). Setting ρ_lim=1 recovers the zonotope method of Bonaert et al. (2021), while increasing ρ_lim yields progressively tighter enclosures. Table 2 shows this monotonic improvement across all models and datasets, directly supporting the claim of a precision–speed trade-off.

3. **Provable complexity bounds.** Theorem 1 (Sec. 3.5) bounds overall computational complexity by O(t·h·d_V·d_model·g_max·κ), while Lemma 3 shows that without order reduction the generator count would grow as O(g_𝒳^{3^κ}). The paper then introduces g_max to keep this tractable, providing clear theoretical justification for the practical algorithm.

4. **Demonstrated improvement across multiple models and datasets.** The evaluation covers four models trained on two different datasets, with up to 27 tokens per sentence (Table 2). In every configuration, the polynomial-zonotope approach with ρ_lim≥2 achieves a larger verified embedding volume than both interval bound propagation and the zonotope baseline.

## Weaknesses

### Fatal
None.

### Major

1. **The connection between ℓ∞-ball verification and the motivating synonym-substitution threat model is assumed, not validated.** The paper motivates verification as a safety shield against adversarial synonym substitution, and Table 1 lists 96 synonym words for an example sentence. However, no experiment tests whether those synonyms actually lie inside the verified ℓ∞ ball at the reported radii, nor whether the ℓ∞ ball excludes non-synonymous embeddings. The paper acknowledges this assumption in the Limitations section ("we cannot guarantee that we capture all synonyms"), but this acknowledgment does not substitute for empirical validation. Since the paper's title and abstract frame the contribution as a step toward verifying LLM safety, the gap between the formal guarantee (no unsafe point in an ℓ∞ ball) and the intended safety property (no synonym sentence is unsafe) weakens the practical relevance of the results. This is not fatal — the core methodological contribution stands independently — but it limits what the evaluation can claim.

### Minor

2. **Model architecture details are absent from the main text.** The paper does not report the number of transformer blocks (κ), embedding dimension (d_model), number of attention heads (h), hidden dimensions of feedforward layers, or the activation function used for the four models evaluated. "Up to 27 tokens" is the only architectural detail provided. These details may reside in the appendix (which was not available in the parsed submission), but their absence from the main text makes it difficult for readers to assess the experimental setup or compare with future work. The paper would also benefit from a controlled ablation varying κ or d_model to show how the method scales along these axes.

3. **The softmax enclosure error is not isolated from the order-reduction error.** The paper's central advantage is exact matrix-set multiplication, but the softmax layer (Lemma 2) necessarily introduces outer approximation. The paper states "we found that, in practice, our method works well as long as the dependencies between dimensions are sufficiently well preserved" — this is asserted, not demonstrated. An ablation comparing (a) polynomial zonotopes with no order reduction, (b) polynomial zonotopes with ρ_lim=1 (convex relaxation), and (c) zonotopes as in Bonaert et al. would isolate where the precision gain comes from. Without this, it is unclear how much of the improvement is due to dependency preservation vs. other factors.

4. **The zonotope baseline implementation could be better documented.** The paper states that setting ρ_lim=1 recovers the zonotope approach, which is a reasonable way to implement the baseline within the same framework. However, the paper does not confirm whether key parameters (g_max, order-reduction strategy) were held consistent between the zonotope and polynomial-zonotope runs, or describe how operations from Bonaert et al. were mapped to the CORA framework.

### Trivial
- The reformulated softmax equation (Eq. 12) contains a notational issue: `1/(Σ_i exp(l_(i)) − l_(j))` appears to be missing parentheses in the exponential argument.

## Nice-to-Haves
- **Validate the synonym-ℓ∞ link empirically.** For a handful of sentences, compile actual synonym lists and check whether the verified ℓ∞ ball at the reported radius covers them. This would ground the formal guarantee in the real-world threat model.
- **Report actual generator counts after order reduction** (g_max was not reported in the main table), which is a key parameter for understanding the precision–time trade-off.
- **Vary κ (number of blocks) and report the fraction of time spent in order reduction vs. layer operations.** This would clarify practical bottlenecks.

## Removed Points
These points were raised by reviewers but are removed with justification:
- **"Softmax enclosure needs a validity condition"** — The paper explicitly states (line 187) that the inverse function requires positive inputs and references Singh et al. (2018, Thm. 3.2) for ensuring this via the exp enclosure. The paper already addresses this.
- **"Unfair baseline comparison / timeout discrepancy"** — The paper implements the baseline within the same CORA framework by setting ρ_lim=1, which is a standard and fair approach. Timeouts on the baseline (if they occurred) would disadvantage the baseline, not the proposed method.
- **"Exposition assumes familiarity with CORA"** — The paper targets the neural network verification community, for whom set-based computing and the CORA toolbox are standard. This is a stylistic preference, not a weakness.
- **"Complexity bound is suspiciously clean"** — Theorem 1 bounds Alg. 1's forward pass, which is standard practice. The order-reduction cost is a separate concern.
- **Not applicable to modern-size LLMs** — The Limitations section explicitly states this, and the title uses "Towards." The paper is a proof-of-concept on small models, which is an honest scope.

## Novel Insights

The most interesting observation emerging from the reviews is that the paper's core technical contribution (exact polynomial-zonotope multiplication for attention) is compelling enough to stand on its own merits, but its packaging — as a safety shield against synonym substitution — creates an expectations gap. The evaluation convincingly shows tighter enclosures for ℓ∞ balls, which is the standard metric in neural network verification. However, the paper would be stronger if it either reframed the contribution more narrowly ("tighter transformer verification") or invested in validating the synonym-embedding connection. This tension between verification precision and real-world threat-model relevance is not unique to this paper; it reflects a broader challenge in the formal verification of language models.

## Suggestions

1. Add a small-scale validation experiment: for 3–5 sentences, compile synonym lists and compute the minimal ℓ∞ radius that covers all synonyms of each token, then report how the verified radius compares. Even a negative result (some synonyms fall outside the verified ball) would be informative and more honest than silence.
2. Report architecture details for all four models (κ, d_model, h, d_ff, activation function) and actual generator counts after order reduction.
3. Conduct a single-block ablation (κ=1) with and without the softmax enclosure to isolate the precision contributions from different components.

## Score and Decision

**Originality:** The use of polynomial zonotopes for transformer verification is novel and extends the prior art in a non-trivial way.  
**Importance:** Formal verification of LLMs is an important and timely problem.  
**Claims support:** The core claim (tighter enclosures via dependency preservation) is well supported. The practical claim (verification against synonym substitution) is less well supported.  
**Soundness:** The methodology is sound; the softmax enclosure follows prior work; the complexity analysis is rigorous.  
**Clarity:** The writing is clear for its target audience, though some details (model architectures) are missing.  
**Value:** The paper makes a solid methodological contribution to the transformer verification literature.

The paper presents a technically sound and novel method for preserving nonlinear dependencies in transformer verification. The evaluation demonstrates consistent improvements over strong baselines. The main weakness is a gap between the motivating application (synonym-substitution safety) and what is actually evaluated (ℓ∞-ball volume). This gap is acknowledged by the authors but not addressed. With relatively modest additions (validating the synonym-ℓ∞ link empirically, reporting architecture details), the paper would be significantly stronger. In its current form, the technical contribution is solid and the paper is a good fit for the venue.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>