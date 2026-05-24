Now I have all the information I need. Let me write the final consolidated review.

**Bracket from Round 1:** The paper sits well above the low anchors (2.5–3.0) and the middle-band papers (4.5–5.5), and is most comparable to the upper middle anchors (6.0–6.5). The closest topical anchors are CfFj68C9Cn (Learning to Recall, 6.50) and utSqpxQHXq (Signal Propagation, 6.00).

**Narrowing (Round 2):** CfFj68C9Cn (6.50) has cleaner theory-to-experiment alignment (3 GD steps analyzed, 3 steps validated) but is much narrower (single-layer, synthetic recall task). The paper under review is broader (multi-layer, natural language, Pythia validation) but has a larger gap between theoretical guarantee (~5–6 steps) and experimental regime (100 epochs). This tradeoff makes the papers comparable in overall quality, with the paper under review's greater ambition partially offset by less precise alignment between theory and experiment. I place it at 6.0.

**Anchors consulted:** l8eWnNH7qN (3.00), 466gVY2sBQ (2.67), ymidNjoH4V (2.50), 7kLRpAH5at (2.67), 7CAvzaRUkH (4.50), utSqpxQHXq (6.00), XfO8npR1fb (4.50), HA85FbDxFV (4.50), UJ2UUjT2ko (8.00), qOyF214xmg (8.00), VKGTGGcwl6 (8.00), 248ysaRatx (8.00), 1pTzWVvwEd (4.50), EAfMzT8ZLy (4.50), CfFj68C9Cn (6.50), l3lneCvc0K (5.50), 7SLtElfqCW (6.00), BC7YLA0zJ0 (5.50).

---

## Summary

This paper develops a theoretical framework for how semantic associations emerge in attention-based transformers trained on natural language data. By analyzing gradient leading terms under small initialization, the authors derive closed-form expressions for weight matrices (output, value, query-key, positional) as compositions of three interpretable basis functions: bigram mapping, interchangeability mapping, and context mapping, which reflect corpus statistics. The theory is validated on a controlled 3-layer transformer (TinyStories) showing cosine similarities >0.99 between predicted and learned weights, and on Pythia-1.4B where covariance matrices of attention/embedding mappings align with the predicted features, especially early in training.

## Strengths

1. **First closed-form weight characterization for transformers on natural language data with explicit error bounds.** Theorem 4.1 and Eqs. 5–8 provide analytic expressions for each weight matrix (output, value, query-key, positional) as simple compositions of corpus statistics (bigram \(\bar{\mathbf{B}}\), context \(\bar{\Phi}\), interchangeability \(\Sigma_{\bar{\mathbf{B}}}\)) with Frobenius-norm error bounds. This goes well beyond prior work that relies on synthetic languages or heavily simplified architectures.

2. **Direct empirical verification on a 3-layer transformer with sustained agreement.** Table 1 and Figure 4 show that cosine similarity between learned weights and theoretical leading terms stays above 0.9 for 30 epochs and above 0.7 for 100 epochs on TinyStories. The fact that the closed-form expressions remain informative far beyond the provably guaranteed early-stage window is a striking empirical finding.

3. **Validation on a production-scale LLM (Pythia-1.4B).** Figure 6 demonstrates strong agreement between covariance matrices of Pythia-1.4B attention/embedding mappings and the leading-term features computed from OpenWebText, particularly in early training. The MLP ablation (Figure 6 middle) and per-head analysis (Figure 7) further show that the theory captures not just aggregate behavior but also the differentiated evolution of attention heads.

4. **Interpretable basis functions with concrete linguistic grounding.** Figure 5 lists top-correlated tokens under each basis function (e.g., "red" → "truck"; "fish" → "pond"; "happy" → "excited"), showing that the theoretical features capture genuine semantic and grammatical associations that align with linguistic intuition.

## Weaknesses

### Major

- **Mismatch between theoretical guarantee window and experimental regime.** Theorem 4.1 provides rigorous bounds for \(s \leq O(1/\eta)\) steps — with \(\eta=0.005, T=200, L=3\), this guarantees only about 5–6 gradient steps. Yet the experiments run 100 epochs (thousands of steps) and Section 5.1 is titled "Verification of theory" while presenting results at 30+ epochs. The paper does mention that features "remain informative beyond" the proven regime, but this important caveat should be foregrounded earlier and more prominently. A reader could easily conclude the theorem itself guarantees agreement at 100 epochs. The honest framing would be: *Theorem 4.1 proves closeness for \(O(1/\eta)\) steps; we then empirically observe that this approximation remains useful far beyond that window, suggesting the leading-term features dominate even when the error bound no longer applies.* This does not invalidate the contribution but is a significant clarity issue.

### Minor

- **Architectural gap in Pythia validation under-discussed.** The theory assumes a shared query-key matrix \(W^{(l)}\) (no separate K and Q), no MLPs, and relative positional encodings as in T5. Pythia-1.4B uses separate K/Q projections, MLPs, and learned absolute positional embeddings. The paper acknowledges this ("Unlike our theoretical setting, Pythia includes additional components…") and uses a covariance-based approximation, but does not discuss how violation of the shared-key assumption specifically could drive the observed similarities or differences. This is especially relevant since the comparison relies on averaging key-query products across heads — a quantity that has no exact counterpart in the theory.

- **First-layer anomaly in Pythia attention mapping.** In Figure 6 (left heatmap), layer 1 attention mapping has low similarity throughout training. The paper notes this in passing ("excluding only the first layer") and offers a brief MLP-related hypothesis, but this is a notable discrepancy that deserves deeper discussion. One would expect the theory to hold best for early layers where attention is simplest, yet layer 1 deviates from the pattern.

- **Cosine similarity metric for covariance matrices not explicitly defined.** For the Pythia experiments, the paper states "compute cosine similarities between the corresponding covariance matrices" but does not give the formula (e.g., \(\mathrm{Tr}(C_1^\top C_2) / (\|C_1\|_F\|C_2\|_F)\)) or justify why this measure is appropriate for comparing matrices with spectral structure.

### Trivial

- **"Min. cosine" in Table 1.** The table reports "Minimum cosine similarities between theoretical and actually learned weights across all epochs." Clarifying that this is the minimum across both layers and epochs (as Figure 4's "range across layers" suggests) would avoid ambiguity.

## Nice-to-Haves

- A brief analysis of why the leading-term features persist beyond the provably guaranteed regime — e.g., does the leading term saturate, or does the error term remain small for a particular structural reason?
- A more detailed discussion of why layer 13 heads diverge dramatically in Figure 7 while layers 2 and 24 do not, and what this implies about where and when head specialization happens relative to the theory.

## Removed Points

- **Criticism that the paper relies "entirely on an appendix for derivations."** This is standard for theory papers at ICLR; the main text presents the theorem, basis function definitions, and interpretation, which is appropriate.
- **"Lemma D.1 cited but never introduced in main text."** It is standard to reference an appendix lemma for a minor technical point about positional encodings.
- **Presentation nitpicks about Figure 2 density and caption length.** These are formatting preferences, not substantive issues.
- **Criticism about "first explicit characterization" novelty claim.** The paper's related work section carefully distinguishes its realistic assumptions from prior work; the claim is defensible.
- **Question about whether the Pythia product is \(K^\top Q\) or \(Q^\top K\).** This is a clarification question, not a verified weakness.
- **Strength Finder claims about "important problem" or "well-motivated."** These are generic and removed per filtering instructions; only concrete strengths are retained.

## Novel Insights

None beyond the paper's own contributions. The review process did not surface a new synthesis that the authors themselves have not already articulated.

## Suggestions

1. **Explicitly demarcate theoretical vs. empirical scope in Section 5.1.** Restructure the "Verification of theory" subsection to clearly state: (a) Theorem 4.1 guarantees closeness for ≤ O(1/η) steps; (b) experiments go far beyond this; (c) the empirical observation that features persist is interesting in its own right and suggests the leading-term approximation is more broadly informative than the formal bound guarantees. This would eliminate the misleading implication that the theorem covers the 100-epoch regime.

2. **Define the covariance cosine similarity metric formally.** Add a sentence specifying the formula (Frobenius inner product) and briefly note why it is appropriate for this comparison.

3. **Expand discussion of the Layer 1 anomaly and the shared-key architectural gap.** Even a paragraph of speculation (e.g., does the input embedding or initial LayerNorm disrupt the clean match? Could the separate K/Q break the theory's predictions for specific heads?) would substantially strengthen the Pythia analysis.

4. **Clarify Table 1** by adding a note like "minimum across all layers and all checkpoint epochs."

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>