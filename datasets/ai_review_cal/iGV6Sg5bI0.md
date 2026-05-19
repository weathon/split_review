- Decision: Reject
- Avg Score: 5.20
- Scores: 6, 8, 1, 3, 8
Now I have a thorough understanding of the paper. Let me construct the consolidated review.

---

## Summary

This paper introduces BRIDGE, a framework for text-guided time-series generation (TG²). It combines a multi-agent LLM system that creates and refines textual descriptions of time series with a diffusion model conditioned on "semantic prototypes" (a fixed set of learnable basis vectors). The paper also proposes a multi-agent collaborative framework to generate a benchmark of text-time-series pairs. Experiments across 12 univariate datasets show that BRIDGE achieves state-of-the-art MDD and KL divergence on most datasets, and synthetic data from BRIDGE enables forecasting performance competitive with real data on two benchmarks.

## Strengths

- **Strong empirical performance across diverse domains (Table 3).** BRIDGE (with text) achieves the best MDD on 9/12 datasets and best KL divergence on 10/12 datasets, substantially outperforming existing TSG methods (TimeGAN, TimeVAE, DDPM, TimeVQVAE). The ablation BRIDGE (w/o Text) often ranks second, confirming the core architecture is robust and text provides additional gains.

- **Demonstrated few-shot cross-domain generalization (Table 5).** BRIDGE applied to an unseen stock dataset with 5 or 10 shots achieves the best MDD and KL divergence among all baselines. This directly supports the claim that the semantic prototype mechanism enables transfer across domains—a key challenge existing single-domain TSG methods do not address.

- **Ablation on text attributes provides actionable guidance (Table 2).** The paper systematically analyzes which text features (conciseness, statistics, background, pattern descriptions) improve zero-shot forecasting. Results showing that concise direct pattern descriptions outperform decomposed trend descriptions are non-trivial and practically useful for anyone designing text prompts for time-series tasks.

- **Synthetic data utility validated on downstream forecasting (Table 4).** Forecasting models (Time-LLM, GPT4TS, LLM4TS, TEMPO) trained on BRIDGE-generated data achieve results close to those trained on real data on ILI and M4 benchmarks, demonstrating practical value for data augmentation and privacy.

## Weaknesses

### Fatal

None.

### Major

- **The semantic prototype mechanism is poorly explained and the description in Figure 4 contradicts the stated definition.** Section 4.2 states that prototypes *P* are "initially set with random orthogonal vectors and then fixed." Yet Figure 4 claims to show prototypes capturing specific temporal patterns (cyclical, trend, volatility). The paper does not clarify what Figure 4 actually visualizes. If it shows the raw random vectors, they cannot exhibit meaningful temporal structure. If it shows learned effective representations (e.g., *Wₖ·P* or *Wᵥ·P* after training via the learnable cross-attention projections), that is not stated. **This is not a structural flaw** — the mechanism of fixed random basis vectors with learned projections (*Wₖ, Wᵥ* are trained) and learned prototype weights (φ) is a valid design. However, the exposition is misleading and leaves the reader unable to understand what the prototypes actually are or how they come to represent temporal patterns. The authors must clearly explain the relationship between the fixed prototypes, the learned projections, and the visualized patterns.

- **The multi-agent benchmark contribution lacks sufficient analysis.** The multi-agent framework (Section 3) is presented as a core contribution, but the evaluation is thin: Table 1 reports only MAE comparisons between strategies, and the paper claims "at least a 15% performance boost over original text" without defining what "original text" is or providing error bars. There is no analysis of the benchmark's diversity, coverage, or comparison to human-written descriptions. The connection to the BRIDGE experiments is also unclear — it is not specified whether BRIDGE uses the multi-agent refined text or some other text source for the main generation results (Table 3). This weakens the paper's narrative and makes it hard to assess the benchmark independently.

- **Missing implementation details severely limit reproducibility.** The paper does not specify: (1) which LLM is used for generating text embeddings or in the multi-agent framework, (2) the architecture of the feature extractor φ, (3) the number of diffusion steps, (4) training hyperparameters (learning rate, batch size, optimizer), or (5) the dimensionality *d* of embeddings and prototypes. These are essential for a methods paper proposing a new architecture. Without them, other researchers cannot reproduce or build on this work.

### Minor

- **No variance or confidence intervals reported for any result.** Tables 1–6 report single-point estimates. Generative models and LLM-based systems are inherently stochastic; standard deviations or confidence intervals across multiple seeds are needed to assess whether differences are meaningful. This is especially important when claiming improvements of small magnitude (e.g., MDD 0.032 vs 0.036 on Solar in Table 3).

- **The comparison against unconditional baselines is not fully isolated.** Table 3 compares BRIDGE (text-conditioned) against unconditional methods (TimeGAN, TimeVAE, DDPM). While BRIDGE (w/o Text) partially controls for this, a cleaner evaluation would include text-conditioned variants of existing baselines. The authors note that no such methods exist (which is part of the contribution claim), but the framing of "outperforms all baselines on 10/12 datasets" conflates the advantage of having an extra modality with the specific architectural contribution.

- **The claim that synthetic data "can replace real data" is over-extrapolated.** Table 4 shows comparable performance on only 2 datasets (ILI and M4). This is a useful demonstration but insufficient to support a general claim about data replacement. The paper should acknowledge this limitation.

### Trivial

- Equation (1) uses φ(*x₀*, *t₀*) but the notation *x₀*/*t₀* versus the earlier *x*/*t* in the text is inconsistent. Clarify the inputs to the feature extractor.
- The text in Section 6.2 (analysis of text features) reports MAE values (1.6, 48.64, 59.91) without the corresponding dataset or condition name being immediately clear from the narrative; labeling could be improved.

## Nice-to-Haves

- The multi-agent benchmark, if released with analysis of its quality (diversity, human evaluation), would substantially strengthen the paper. As it stands, this contribution is preliminary.
- Adding an analysis of failure cases (datasets where BRIDGE w/o Text outperforms BRIDGE with text, such as Pedestrian in Table 3) would improve the paper's scientific rigor and help the community understand when text helps or hurts.

## Removed Points

These points from the inputs are excluded from the main review with justification:

- **"Semantic prototyping is internally incoherent / structures flawed" (harsh critic's #1, framed as fatal):** Removed as an overstatement. The mechanism (fixed random basis + learned projections + learned weights) is valid. The paper's *explanation* is problematic, not the method itself. Reframed as a Major weakness about clarity/exposition above.
- **"The paper provides no release of the benchmark":** Removed per rule: criticisms questioning the release status of cited resources are not permitted.
- **"Cannot be independently verified" and similar reproducibility concerns founded on doubting existence of cited entities:** Removed per rules.
- **"Placeholder-like sentences (3., 4., 7.)":** These are parser artifacts from PDF extraction, not author errors. Removed per rules.
- **"Missing related works":** Removed per rules (cannot verify without external sources).
- **"Missing appendix / proofs":** Removed per rules (parser strips appendices; they exist in original submission).
- **Pure formatting/style nitpicks:** Removed per rules.

## Novel Insights

None beyond the paper's own contributions. The two reviews surface known tensions in multimodal generation papers (the gulf between claiming a method works and explaining *why* it works, the difficulty of fair evaluation when introducing a new modality). Neither reviewer identified a genuinely new perspective not already evident from the paper itself.

## Suggestions

1. **Clarify the prototype mechanism.** State explicitly: (a) Are the prototypes *P* shown in Figure 4 the raw random vectors or some learned transformation (e.g., *Wₖ·P*)? (b) Add a sentence explaining that while *P* is fixed, the projections *Wₖ, Wᵥ* in cross-attention are learned, so the effective prototype representation is trained. (c) Consider a small synthetic experiment showing that the learned weight patterns φ(*x*) correlate with interpretable properties of the input time series.

2. **Add variance/confidence intervals.** Report results over at least 3 random seeds for all main tables. This is standard practice for generative modeling papers.

3. **Specify implementation details.** State the LLM used, the φ architecture, diffusion hyperparameters (steps, schedule), and training configuration. This is essential for reproducibility.

4. **Restructure the evaluation narrative.** Either (a) frame the contribution as "text conditioning improves TSG" and compare BRIDGE (w/o Text) vs. BRIDGE (with Text) as the primary comparison, with unconditional baselines as a secondary reference, or (b) implement text-conditioned variants of existing baselines for a fairer head-to-head comparison.

5. **Be more precise about the benchmark.** Either release it with analysis, or downgrade the claim from "creating a benchmark" to "a method for generating text descriptions."
