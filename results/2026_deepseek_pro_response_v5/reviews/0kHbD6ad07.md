Now let me synthesize everything. Here's my comparison:

| Anchor | Score | Comparison |
|--------|-------|------------|
| WULjblaCoc ("When Can Transformers Count?") | 5.60 | Our paper is stronger — broader theoretical scope, training preservation, algorithm, and larger-scale empirical validation. |
| 8p3fu56lKc ("One Step of GD is Optimal ICL") | 6.00 | Our paper is stronger — more comprehensive theory, algorithm contribution, richer empirical section. |
| 1lFZusYFHq ("How Transformers Implement Induction Heads") | 6.20 | Our paper has broader theoretical scope (all decoder-only vs. specific mechanism), training preservation result, plus an algorithm. Slightly stronger. |
| NHhjczmJjo ("L2O Capabilities of Transformers") | 7.00 | Comparable pattern (theory + construction + empirical). Our paper has a broader empirical section but the theory-algorithm gap is more pronounced. Roughly similar or slightly weaker. |
| hwSmPOAmhk ("Factual Recall via Associative Memories") | 7.33 | Strong theory elegantly presented. Our paper's theory is broader but the presentation has more rough edges (naming, algorithm-theory gap, HARDPROMPTS baseline). Our paper is weaker. |
| STUGfUz8ob ("Reasoning with Abstract Symbols") | 7.60 | Strong theory with architecture modifications and clean empirical validation. Our paper is clearly weaker. |

Our paper lands at approximately **6.5** — above the 6.0-6.2 papers but below the 7.33 paper due to the algorithm-theory gap, weaker baseline comparison, and presentation issues.

---

## Summary
This paper proves that decoder-only Transformer language models are almost-surely injective — distinct prompts map to distinct last-token hidden representations — and that this injectivity is preserved through gradient-based training. The proof uses real-analytic function theory: Transformer components are real-analytic in parameters, so collision sets have Lebesgue measure zero and GD steps preserve absolute continuity of the parameter distribution. The authors then introduce SIPIT, a sequential algorithm that reconstructs the exact input text from per-position hidden states with provable O(T|V|) worst-case guarantees. Empirical collision searches across 5 billion prompt pairs and six model families find zero collisions, and SIPIT achieves 100% token-level recovery on GPT-2 Small.

## Strengths
- **Rigorous theoretical framework (Theorems 2.1–2.3):** The paper builds a clean chain of reasoning from real-analyticity of Transformer components → zero sets have measure zero → collisions are probability-zero events at initialization → GD preserves absolute continuity so training cannot create collisions. The training-preservation result (Theorem 2.3, Corollary 2.3.1) is a genuine advance over prior initialization-only injectivity results (e.g., Sutter et al., 2025), and the extension to SGD/mini-batch GD with arbitrary batch selection is non-trivial.
- **Comprehensive empirical collision search (Section 4.1, Figure 3, Tables 1–3):** Approximately 5 billion pairwise comparisons over 100k prompts across six model families (GPT-2 S/M/L, Gemma-3 1B/4B/12B, Llama-3.1-8B, Mistral-7B, Phi-4-mini, TinyStories-33M), with zero collisions observed. Tests cover FP4/INT8 quantization and scale to 70B models, where minimum distances remain well above the 10⁻⁶ threshold. The finding that quantization *increases* minimum distances is an interesting and non-obvious result.
- **SIPIT algorithm with formal guarantees (Theorems 3.1–3.2):** The algorithm correctly exploits causal structure for sequential token-by-token recovery, with a worst-case O(T|V|) bound and a robustness guarantee under bounded additive noise. The 100% recovery rate on GPT-2 Small (28s for 20 tokens) and near-constant vocabulary exploration percentage (~0.2%) empirically confirm the theoretical scaling.
- **Training-preservation as a structural guarantee:** The argument that GD steps are diffeomorphisms almost everywhere and therefore cannot collapse parameter distributions onto measure-zero collision sets transforms injectivity from an initialization curiosity into a property that standard training pipelines preserve. This has real consequences for how we think about information preservation in deployed models.

## Weaknesses

### Fatal
None.

### Major
- **Algorithm–theory gap is elided in presentation:** The theory proves injectivity of the *last-token representation* at the final layer, but SIPIT requires access to *all per-position hidden states* at a given layer. The paper acknowledges this (line 141: "designing an efficient algorithm for that setting is nontrivial and left to future work") and argues that injectivity extends transitively (line 143: "Since the last state is itself a deterministic function of the hidden matrix at any layer ℓ, injectivity extends to the full representation"). However, the paper's framing throughout the abstract and introduction (e.g., "SIFT, the first algorithm that provably and efficiently reconstructs the exact input text from hidden activations") does not clearly distinguish between the theoretically-guaranteed injectivity of the last-token state and the per-position access the algorithm actually requires. The algorithm depends on local one-step injectivity, which follows from the theory but is a weaker property than the global last-token injectivity the paper's headline result establishes. The paper would benefit from an explicit statement of what the algorithm requires beyond what the theory proves, and whether an algorithm using only the last-token state is possible in principle.

### Minor
- **HARDPROMPTS comparison is of limited informativeness:** HARDPROMPTS (Wen et al., 2023) is a prompt optimization method using gradients to discover prompts maximizing a downstream objective — it was never designed for exact inversion from hidden states. While the paper's text (line 339) correctly describes HARDPROMPTS as a gradient-based prompt discovery method, presenting it as a primary baseline in Table 5 and highlighting its 0% accuracy creates an impression of superiority over a strawman. The more relevant comparison would be against Thomas et al. (2025), which the paper cites in Section 5 as doing sequential recovery from hidden states. The brute-force ablation already provides a meaningful baseline.
- **Privacy and regulatory claims overreach (Section 6):** The argument that "any system that stores, caches, or transmits hidden states is effectively handling the user's verbatim text" (line 349) and should face equivalent data-protection obligations does not acknowledge the practical requirements for inversion: white-box model access, non-trivial computation (e.g., ~550s for 10 tokens on Llama-3.1-8B), and access to all per-position hidden states — not just the last-token embedding that the theory guarantees is injective. The legal analysis citing the Hamburg DPA decision is a brief paragraph that does not engage with the distinction between theoretical possibility and practical accessibility.
- **Collision threshold of 10⁻⁶ is not justified:** The paper uses 10⁻⁶ as the threshold below which two representations are considered colliding, but never discusses why this value is appropriate given floating-point numerical precision. In practice, genuine collisions could produce differences below machine epsilon while numerical noise could produce differences above 10⁻⁶. A brief discussion of this threshold relative to fp32 precision would strengthen the empirical claims.
- **Efficiency framing is somewhat overstated:** The paper describes SIPIT as "efficient" and highlights the 28s runtime for 20 tokens on GPT-2 Small (124M parameters). However, Table 4 shows ~550s for 10 tokens on Llama-3.1-8B, making the per-token cost substantial. The O(T|V|) guarantee is formally correct but the constant factor (one forward pass per candidate token in the worst case) limits practical scalability.

### Trivial
- **Algorithm naming inconsistency:** The algorithm is called "SIFT" in the abstract and introduction, "SIPIT" / "SIpIT" in Section 3, and "SiPT" / "SIFT" / "SIPT" in Section 4 and tables. Consistent naming would improve readability.

## Nice-to-Haves
- Expand the Theorem 2.2 proof sketch in the main text with a more detailed description of how the distinguishing signal propagates through all subsequent layers in the constructive parameter setting.
- Report variance or distribution of minimum pairwise distances (e.g., across different prompt subsets), not just the single minimum across all pairs, to characterize how close representations can get in practice.
- Acknowledge explicitly that the 100k-prompt collision search, while large, covers a vanishing fraction of all possible prompts, and frame the results as "consistent with" rather than "confirming" the theory.
- Add a paragraph to Section 3 explicitly reconciling the per-position access assumption with the last-token injectivity guarantee, clarifying what the algorithm needs beyond what the theory guarantees.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Theorem 2.2 construction under-specified / missing appendix:** The Harsh Critic argued that the proof sketch for Theorem 2.2 (lines 87–88) does not account for later layers collapsing distinguishing signals, and that the full proof is in the stripped Appendix C, making the sketch unevaluable. Removed because the paper states the full proof is in Appendix C, which exists in the original submission. The parser strips appendices from all papers. Under the rules, criticisms dependent on missing appendix content are removed.
- **Jacobian determinant claim unverified:** The Harsh Critic noted that the claim "one can check this by evaluating at a simple parameter setting" (line 107) is asserted without concrete verification. Removed for the same reason — the full proof is in the (stripped) appendix. The main-text sketch stating the existence of such a setting is a reasonable summary of a technical lemma.
- **Discrete-to-continuous injectivity being less surprising:** The Harsh Critic argued the paper oversells the counter-intuitiveness of the result since mapping a discrete set to ℝᵈ is inherently less collapsible. Removed because this is a framing preference, not a factual error. The paper does acknowledge in Section 5 that Transformer components are non-injective as continuous-to-continuous maps and that their contribution is the discrete-domain perspective. The novelty claim is about proving this property formally, with training preservation, and operationalizing it — which the paper does.
- **"The paper does not compare against Thomas et al. (2025)" as an independent major flaw:** The Harsh Critic raised this separately, but it is merged into the minor weakness about the HARDPROMPTS comparison being uninformative. The absence of this comparison is noted there.
- **Pure formatting/typo complaints from Harsh Critic:** Removed per hard rules.

## Novel Insights
The paper's most genuinely novel observation is that injectivity is not merely an initialization curiosity but a structurally preserved property throughout training — the real-analytic framework cleanly shows that GD steps are diffeomorphisms almost everywhere and therefore cannot collapse an absolutely continuous parameter distribution onto the measure-zero collision set. This transforms the result from a "random models happen to be injective" statement into a guarantee that standard training pipelines cannot break injectivity, which has real consequences for how we think about information preservation in deployed models.

## Suggestions
- Replace or supplement the HARDPROMPTS baseline with a comparison against Thomas et al. (2025) or simply present SIPIT's performance as a standalone demonstration, with the brute-force ablation already providing a meaningful baseline.
- Briefly discuss the 10⁻⁶ collision threshold in relation to fp32/fp16 numerical precision.
- Temper the privacy discussion in Section 6 by acknowledging the practical requirements for inversion (white-box access, computation cost, and the per-position state requirement that goes beyond what the last-token injectivity theorem guarantees).

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Reject</decision>