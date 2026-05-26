## Summary

This paper studies how the sparsity hyperparameter \(L_0\) (average number of active latents per token) affects the quality of features learned by sparse autoencoders (SAEs) for LLM interpretability. Using controlled toy models with ground-truth features and experiments on Gemma‑2‑2B and Llama‑3.2‑1B, the authors show that (i) an \(L_0\) that is too low forces the SAE to mix correlated features (feature hedging), corrupting monosemanticity, while an \(L_0\) that is too high also mixes features; (ii) the common sparsity–reconstruction trade-off is misleading because a ground-truth SAE can have *worse* reconstruction than a "cheating" SAE at low \(L_0\); and (iii) the decoder pairwise cosine similarity \(c_{\text{dec}}\) can serve as a proxy to detect when \(L_0\) is too low, with its "elbow" aligning with peak sparse-probing performance.

## Strengths

- **Toy model experiments cleanly demonstrate the mechanism of feature mixing under low \(L_0\).** Section 3.1 shows that when SAE \(L_0\) is set below the true \(L_0\), the decoder latents mix positive (or negative) components of correlated (or anti-correlated) features. The setup with known ground-truth features and initialization at the correct solution (Section 3.1, para 2) rules out local-minimum explanations and isolates gradient pressure as the cause.

- **The MSE comparison in Section 3.3 is the paper's strongest single piece of evidence.** A trained low-\(L_0\) SAE achieves MSE 2.73 while the ground-truth SAE (correct latents, same \(L_0\)) achieves MSE 4.88 — directly showing that the MSE loss *incentivises* feature mixing and that better reconstruction does not imply a better SAE. This is a clean, impactful demonstration that undermines a widespread evaluation methodology.

- **Results generalise across SAE architectures (BatchTopK and JumpReLU).** Section 3.6 replicates the core toy-model findings with JumpReLU SAEs (Figure 7), confirming the phenomenon is not an artifact of a specific activation function. The interesting "sticking" behavior of JumpReLU near the correct \(L_0\) is a valuable observation.

- **The paper is transparent about \(c_{\text{dec}}\)'s limitations.** Section 6 explicitly states that the metric is "not a perfect guide" and "can sometimes remain nearly flat for a wide range of \(L_0\)," while still being useful for avoiding clearly too-low \(L_0\). This honest assessment strengthens the credibility of the main claims.

- **The sparsity–reconstruction trade-off critique (Section 3.4) is important and well-supported.** Figure 4 shows the trained SAE outperforming the ground-truth SAE on variance explained at low \(L_0\), directly validating the claim that reconstruction quality alone cannot distinguish correct from incorrect SAEs when \(L_0\) is too low.

## Weaknesses

### Major

- **The claim that "most commonly used SAEs have an \(L_0\) that is too low" is not adequately substantiated.** This claim appears in the abstract (line 9) and conclusion (line 240), yet the sole support provided is "a cursory search of open source SAEs on Neuronpedia" (line 240) referenced to Appendix A.13. For a claim of this strength and potential practical impact — one that could lead practitioners to discard existing SAEs — a systematic survey with reported \(L_0\) values, dictionary sizes, and training setups is needed. The paper should either provide this analysis or substantially soften the claim (e.g., "our results suggest that many SAEs may benefit from a higher \(L_0\)").

### Minor

- **The "elbow" of \(c_{\text{dec}}\) lacks an objective operational definition.** The paper identifies the elbow by visual inspection (e.g., "around \(L_0\) 200" in Figures 8 and 9). For Gemma‑2‑2B layer 5 (Figure 8, top-left), \(c_{\text{dec}}\) drops sharply then flattens over a broad range, making the elbow location ambiguous without a formal rule (e.g., threshold on the derivative, or the point where \(c_{\text{dec}}\) exceeds its minimum by a fixed fraction). This limits the metric's reproducibility as a practical tool. While the paper acknowledges \(c_{\text{dec}}\) is "not a perfect guide," it does not provide a way to make the elbow detection systematic.

- **The "correct \(L_0\)" framing is imprecise for real LLMs.** The paper uses "correct \(L_0\)" throughout (title, abstract, main text) in a way that suggests a single optimal value. In toy models this is well-defined (the true \(L_0\)), but for real LLMs the notion is less clear — the paper's own Section 4.2 shows that different latents may have different firing thresholds, implying an optimal *range* rather than a single value. Sparse-probing F1 in Figure 8 is also relatively flat (e.g., 0.78–0.82 for Gemma layer 5), consistent with a broad optimum rather than a precise point. The evidence best supports the claim that *too low* \(L_0\) is harmful and that an optimal region exists; the "correct \(L_0\)" language overstates the precision.

- **Limited LLM evaluation scope.** The LLM experiments cover only 3 layers across 2 models (Gemma‑2‑2B layers 5 and 12, Llama‑3.2‑1B layer 7), each with a single dictionary size (32k). While the results are suggestive, adding more layers, a third model, or a sweep over dictionary sizes would substantially strengthen confidence that the observed patterns generalize.

### Trivial

- The paper does not discuss the computational cost of \(c_{\text{dec}}\) for large dictionaries. Computing all pairwise cosine similarities is \(O(h^2)\); for dictionaries exceeding 1M latents this may be prohibitive. Mentioning potential approximations (random sampling of pairs, Gram matrix methods) would be a useful addition.

## Nice-to-Haves

- **Provide an objective rule for detecting the \(c_{\text{dec}}\) elbow.** A simple rule (e.g., the \(L_0\) where the derivative of \(c_{\text{dec}}\) crosses a threshold, or where \(c_{\text{dec}}\) exceeds its minimum by a fixed fraction) applied consistently across toy and real models would make the metric reproducible and practically useful.

- **Directly test the practical benefit of the recommended \(L_0\).** The paper currently shows correlations between \(c_{\text{dec}}\) shape and sparse-probing performance. A stronger demonstration would be to compare interpretability metrics (autointerp, patching) for SAEs trained at the elbow-recommended \(L_0\) vs. a commonly used low \(L_0\) (e.g., \(L_0=50\)).

- **Investigate the effect of dictionary size on the optimal \(L_0\).** Varying dictionary size (e.g., 16k, 32k, 64k) would reveal whether optimal \(L_0\) scales linearly or interacts with dictionary capacity, and would make the claims about existing SAEs more broadly applicable.

- **Provide the proposed systematic survey of existing open-source SAEs** (Gemma Scope, Llama Scope, etc.) with their \(L_0\) and dictionary sizes, rather than relying on a "cursory search."

## Removed Points

The following points from the reviewers were removed after verification against the paper:

- **Criticism about Figure 8 misattributing Gemma/Llama plots and claiming the drop ends at \(L_0=100\).** The harsh critic stated "The Gemma‑2‑2B top‑right plot shows \(c_{\text{dec}}\) dropping sharply… the drop ends around \(L_0\) 100." This is factually wrong: the figure caption identifies the top-right plot as Llama‑3.2‑1B, not Gemma, and the paper states the drop ends by \(L_0=250\). Removed for factual inaccuracy.

- **Criticism about missing appendix content and missing proofs.** The harsh critic noted "the appendix with theoretical justification and additional plots is referenced but not available in the extracted text." This is a PDF-parser artifact; the original submission contains these sections. Removed per hard rule.

- **Criticism framed as "the metric is not validated as a practical guide for setting \(L_0\)"** as a broad claim. The paper only claims \(c_{\text{dec}}\) can "help guide" and "give hints" — modest claims. The specific sub-critique about the subjective elbow definition is retained (Minor weakness); the broader framing is removed.

- **Strength Finder's generic/superficial framing.** The Strength Finder's statements about the problem being "important" were not used; concrete, evidence-anchored strengths were retained.

## Novel Insights

None beyond the paper's own contributions. The synthesis of the reviews confirms that the paper's core strength is the clean toy-model demonstration that low \(L_0\) incentivises feature mixing through the MSE loss (Section 3.3), and that the sparsity–reconstruction trade-off can reward incorrect solutions. The proposed \(c_{\text{dec}}\) metric is a plausible diagnostic but its practical utility is limited by the subjective elbow definition and flat curves in some settings.

## Suggestions

1. **Soften or properly support the "most commonly used SAEs" claim.** Either provide a systematic survey of existing SAEs with their \(L_0\) values, or replace the strong blanket statement with a more measured claim such as "our results suggest that many SAEs may benefit from a higher \(L_0\)."

2. **Define the \(c_{\text{dec}}\) elbow objectively.** Propose a concrete rule (e.g., the \(L_0\) where the derivative exceeds a threshold, or where \(c_{\text{dec}}\) rises a fixed fraction above its minimum) and apply it consistently.

3. **Reframe "correct \(L_0\)" as "appropriate \(L_0\) range"** for real LLMs, to better align with the evidence (flat F1 curves, Section 4.2's per-latent variation). The title and abstract would benefit from this nuance.

4. **Expand LLM evaluation** to at least one more model (e.g., Pythia‑1B or a larger Llama model) and a few more layers per model, to increase confidence in generalisation.

5. **Add a brief note on computational cost** of \(c_{\text{dec}}\) for large dictionaries and mention potential approximations.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>