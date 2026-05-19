- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8
Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper introduces ProFS (Projection Filter for Subspaces), a tuning-free weight-editing method that reduces toxicity in LLMs by identifying a low-rank toxicity subspace (via SVD on centered embedding differences between toxic/non-toxic pairs) and projecting MLP-value weights orthogonal to it. The paper claims ProFS is more sample-efficient than DPO (requiring orders of magnitude less data), is robust to label noise, and can be interpreted as a denoised version of a single DPO step. Experiments span GPT-2, Mistral, OPT, and GPT-J.

## Strengths

1. **Sample efficiency is convincingly demonstrated** — The paper shows (Section 7, line 247) that ProFS achieves measurable toxicity reduction with as few as 5 datapoints and significant reductions with 50, while DPO requires orders of magnitude more data. The core comparison (Table 1, lines 245-246) uses ProFS@500 vs DPO@2000, and ProFS almost always achieves lower toxicity despite less data.

2. **Robustness to label noise is empirically validated** — Figure 3 (lines 249-252) shows ProFS maintains essentially flat toxicity reduction even when 50% of labels are flipped, while DPO degrades sharply. This is a clear and practically important advantage for real-world alignment where annotation noise is common.

3. **Theoretical connection to DPO is formalized and empirically supported** — The factor analysis framework (Section 5, Eq. 5-6) provides a principled justification for why SVD on embedding differences recovers a toxic subspace. The empirical correlation analysis (Section 8, lines 291-296) shows that DPO's initial gradient and ProFS's projection are positively correlated (exceeding a random-matrix baseline), especially in later layers and with more data — supporting the claim that ProFS can be viewed as a denoised single-step DPO.

4. **Centering ablation (Table 4) confirms a key design choice** — Including the corpus mean direction in the projection catastrophically increases perplexity (from 35 to 1160+ on GPT-2), cleanly demonstrating why the centering step is critical. This is a well-executed ablation that validates a non-obvious algorithmic detail.

5. **Generalization to multiple preferences is evaluated** — The HH-Golden experiment (Table 4, line 266) shows ProFS achieves a higher win rate against the original model than DPO when both use the same 500 samples, demonstrating the method extends beyond toxicity to broader alignment preferences.

6. **Layer-wise analysis provides actionable guidance** — Figure 4 (lines 278-281) systematically shows that editing only higher layers best reduces toxicity while preserving perplexity, consistent with prior findings about semantic encoding in later layers.

## Weaknesses

### Fatal
None.

### Major

1. **The choice of $k$ (number of singular vectors) is not justified** — The paper states (line 225) $k=2$ for GPT-2 and $k=10$ for all other models, with no sensitivity analysis, no singular-value spectrum plot, and no rationale for why $k$ changes across model scales. Since $k$ directly controls how much of the weight matrix is projected out, this is a key hyperparameter. Without showing the singular value spectrum or evaluating toxicity/perplexity under different $k$ values, it is unclear whether 10 is near-optimal or if performance degrades significantly beyond it. This affects reproducibility and trust in the claimed noise robustness.

2. **The DPO connection is overstated in the title relative to what is actually shown** — The title presents ProFS as "a Robust and Denoised variant of DPO," but ProFS is algorithmically very different from DPO: one is a one-shot orthogonal projection on weights, the other is iterative gradient descent over a preference loss. What the paper actually establishes is a *conceptual* connection — that the DPO gradient under a heavily simplified log-linear model (Eq. 7-8) has a related mathematical form, and that the two methods' update directions are partially correlated (Figure 4). The paper's own body is more careful ("can be interpreted as," "conceptually similar to"), suggesting the title would be more accurate as something like "Model Editing through Toxic Subspace Projection: Sample Efficiency, Noise Robustness, and Connections to DPO."

### Minor

1. **The factor model assumption (shared context component) is plausible but unvalidated** — The central assumption in Eq. (5) — that toxic and non-toxic sentence pairs share an *identical* context component and differ only in toxicity plus noise — is not directly tested. While the vocabulary projection (Table 1) provides partial evidence that the top singular vectors correspond to toxic words, there is no analysis of whether the identified subspace captures *only* toxicity versus other correlates (e.g., topic differences between Wikitext-2 and PPLM-generated toxic sentences). The paper would be strengthened by evaluating the model on tasks related to toxicity-adjacent topics (e.g., medical drug descriptions, historical violence) to check what is lost beyond perplexity.

2. **The sample-efficiency comparison is not fully apples-to-apples** — The main comparison (Table 1) uses 500 datapoints for ProFS vs. 2,000 for DPO. While this asymmetry is intentional (to show ProFS can match or beat DPO with far less data), the paper does not report DPO performance with only 500 datapoints. This would clarify whether ProFS's advantage is purely due to algorithmic efficiency or partly because 500 is sufficient for DPO as well. (The HH-Golden experiment does use equal data, partly addressing this.)

3. **The DPO gradient derivation relies on a heavily simplified model** — Equation (7) assumes a log-linear output distribution with normalization factor independent of $\mathbf{W}$, which is not true for real transformers. The paper acknowledges this implicitly but does not discuss how far this toy model is from the actual dynamics of DPO on a neural network. The theoretical connection is therefore suggestive rather than established.

4. **Computational cost is not reported** — The paper claims ProFS is "tuning-free, lightweight and computationally cheap" but does not report runtime, memory usage, or FLOPs for either ProFS or DPO for any model size. This would help contextualize the practical advantage.

5. **No random-projection baseline** — The paper does not compare against a random projection of the same rank applied to the weights. The correlation analysis has a random-matrix baseline for one specific experiment, but the main editing results lack a baseline that would help isolate whether the benefit comes from *which* directions are removed versus simply removing *any* low-rank subspace.

### Trivial
- The HH-Golden experiment (Table 4) uses 500 samples for both methods, while the main toxicity experiment uses 500 for ProFS vs. 2,000 for DPO — the paper could briefly explain this design choice for consistency.
- The data pairing process (Wikitext-2 vs. PPLM-generated toxic counterparts) is not discussed in terms of potential mismatches that could violate the shared-context assumption.

## Nice-to-Haves
- Performing a sensitivity analysis on $k$ (vary around the chosen value and report toxicity + perplexity) would substantially address the main methodological gap.
- Evaluating on tasks correlated with toxicity (medical writing, historical contexts involving violence) would strengthen the claim that the method preserves desirable capabilities.
- Reporting DPO results with 500 datapoints would make the sample-efficiency comparison fully apples-to-apples.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"Standard deviations are mentioned but not shown in the tables"** — The paper explicitly states (line 231) it reports mean and standard deviation over three runs. The tables are imported via `\input{}` from external files that were not rendered in the parsed text. This is a parser artifact, not an author omission.
- **HH-Golden data size inconsistency framed as a flaw** — The paper uses 500 samples for both methods in this experiment. The inconsistency in data sizes across experiments is a design choice (different experimental goals), not a weakness.

## Novel Insights

The most interesting observation from the reviews is the tension between the paper's two contributions: (1) ProFS as a practical editing method, and (2) the claimed DPO connection. The practical method is well-supported empirically; the DPO connection is more suggestive than rigorous. The correlation between ProFS's projection and DPO's initial gradient (Figure 4) is a genuinely interesting empirical finding that could motivate future work on unifying editing and training-based alignment, but the paper's title overstates the strength of this connection. The factor-analysis framing is a genuinely novel theoretical lens that distinguishes ProFS from prior activation-editing work and provides a principled explanation for why SVD works here.

## Suggestions
- Revise the title to better reflect what is established (e.g., "Sample-Efficient and Noise-Robust Model Editing via Toxic Subspace Projection: Connections to DPO").
- Add a sensitivity analysis on $k$ with singular-value spectrum plots for at least one representative model.
- Include DPO results at the same data size (500 samples) in the main comparison table.
- Add a random-projection baseline to isolate the effect of removing the *toxic* subspace vs. any low-rank subspace.
- Discuss potential limitations of the shared-context assumption in the factor model more explicitly.
