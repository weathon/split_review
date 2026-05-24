Now I have sufficient calibration. Let me write the final review.

**Round 1 bracket:** Between 4.5 and 5.5 (above the weak anchors at ~2.5-3.0, below the zigzag spaghetti paper at 6.33 and the LLM geometry paper at 6.75).

**Round 2 narrowing:** The paper is comparable to the Node-Level TDA paper (5.33, Reject) and the ECLayer paper (5.20, Reject) — similar in proposing a novel TDA descriptor but with evaluation gaps. Slightly weaker than the Zigzag Spaghetti paper (6.33, Poster) which has theoretical guarantees. I place the paper at 5.0.

**Final score: 5.0**

---

## Summary

This paper applies zigzag persistence, a topological data analysis (TDA) tool for tracking features across dynamically changing spaces, to analyze internal representations of large language models (LLMs). The authors introduce *persistence similarity*, a descriptor that measures what fraction of topological cycles alive at one layer survive through all intermediate layers to another. They analyze several LLMs (Llama 2, Llama 3, Mistral, Pythia) and observe a consistent peak in average persistence similarity at roughly the same relative depth across all models, suggesting common topological structure. As a practical application, they prune layers with highest persistence similarity and report comparable performance to existing pruning methods (Gromov et al., 2024; Men et al., 2024).

## Strengths

- **Novel application of zigzag persistence to LLM internal representations.** The paper is the first (to the reviewer's knowledge) to use zigzag persistence — which is designed for tracking topological features through a sequence of spaces — to study how LLM representations evolve across layers. This framing of "layers as discrete time steps in a dynamical system" (Section 3) is well-motivated and opens a genuinely new direction for TDA in LLM interpretability. Section 3.2 and Figure 1 clearly convey the construction.

- **Persistence similarity is a trajectory-aware descriptor that offers richer information than static similarity measures.** Unlike traditional layer-wise comparisons (cosine similarity between activation matrices), the proposed descriptor $\mathcal{S}_p(\ell_1, \ell_2)$ (Equation 5) considers whether a cycle that exists at $\ell_1$ survives through all intermediate layers to $\ell_2$, encoding path information rather than just endpoint states. This conceptual advance is clearly articulated in Section 3.4.

- **The universal peak finding is genuinely interesting and well-demonstrated.** Figure 4 (right panel) shows that $\bar{\mathcal{S}}_1$ peaks at approximately the same normalized depth across seven models spanning different families, sizes (7B–70B), and datasets. The curves from Llama 2 7B/13B/70B, Llama 3 8B/70B, Mistral 7B, and Pythia 6.9B all collapse onto a similar trajectory, which is a striking empirical observation.

- **The pruning results in Table 1 are competitive.** For Llama 3 8B, persistence-similarity-based pruning matches the compared methods exactly (53.44 on MMLU, 41.60 on HellaSwag, 70.00 on Winogrande). For Mistral 7B on MMLU, it substantially outperforms them (53.17 vs. 38.20). This suggests the topological criterion has practical value even if the experimental design has limitations.

## Weaknesses

### Major

- **The claim that two different pruning methods produce identical output is unsubstantiated and suspicious.** The paper states (Section 4.3) that "both considered methods from (Gromov et al., 2024) and (Men et al., 2024) give the same result at fixed $N_{prune}$" and the Table 1 caption asserts "The chosen layers turn out to be the same for the two methods, so the results are condensed in one column." Angular similarity and Block-Influence similarity are distinct metrics operating on different principles; it is extremely unusual for them to select identical layer subsets across multiple models and pruning ratios. The paper provides no separate evidence — no table, no figure showing the selected layers per method, no discussion of why this coincidence occurs. If the claim is incorrect, the entire experimental comparison in Table 1 collapses into comparing apples and oranges. At minimum, the authors need to disclose the specific layers selected by each method and explain why they coincide.

- **The pruning evaluation does not establish that the persistence-similarity criterion is meaningfully better than random.** Algorithm 2 removes layers whose $\bar{S}_1$ is within 10%/20% of the maximum — these are layers near the peak in the middle of the model (Figure 4). The paper compares against methods that identify redundant layers via other criteria, but never includes a random baseline that removes the same *number* of middle layers. Without this control, it is unclear whether the method's success reflects genuine informativeness of the persistence criterion or simply that removing a few middle layers (which many pruning methods target) does not strongly degrade performance. (Note: the comparison against Gromov et al. and Men et al. is legitimate but incomplete without a random baseline.)

### Minor

- **The "universal structure" claim is overstated relative to the evidence.** All seven models tested are decoder-only transformers. The paper acknowledges this implicitly but the claim of universality would be considerably strengthened (or appropriately scoped) by testing on encoder-decoder (T5) or encoder-only (BERT) architectures. As presented, the evidence supports "similar structure across the decoder-only models tested" rather than "universal structure in LLM internal representations."

- **No comparison to simpler geometric baselines.** The paper does not show that zigzag persistence captures information beyond what simpler measures (e.g., cosine similarity between adjacent layer representations, Betti number evolution across layers, or the fraction of $k$-NN edges preserved between layers) already capture. An ablation comparing persistence similarity to these simpler alternatives would help justify the added complexity of the zigzag framework. Without it, the value added by the topological machinery is asserted but not demonstrated.

- **The asymmetry of $\mathcal{S}_p$ is noted but not motivated.** Equation 5 defines $\mathcal{S}_p(\ell_1, \ell_2)$ by normalizing by $\beta_p(\ell_1)$ only, making the measure asymmetric. The paper notes this asymmetry (Section 3.4) but does not explain its utility. Since the plots in Figure 3 show $\mathcal{S}_p$ is "approximately symmetric," the asymmetry seems incidental rather than intentional.

- **No uncertainty quantification.** All results (pruning in Table 1, similarity curves in Figures 3–4) are reported as point estimates without error bars, confidence intervals, or discussion of variance. While single-run evaluation is common in LLM pruning work, the claims of "comparable performance" and "universal structure" would be strengthened by some measure of stability (e.g., across dataset subsets or $k_{NN}$ choices).

### Trivial

- The sum notation in Equation 5 uses $\ell_1, \ell_2$ as both function arguments and bound variables in the summation, which could cause confusion. Clarifying with different variable names (e.g., $b$ for birth, $d$ for death) would improve readability.

## Nice-to-Haves

- Testing on encoder-decoder or encoder-only architectures would help scope the "universality" claim.
- A synthetic toy example validating that persistence similarity recovers known ground-truth feature evolution would strengthen confidence in the descriptor.
- Reporting which specific layers are selected by each pruning method (Gromov vs. Men) would resolve the coincident-result concern.
- An analysis of computational cost at scale (e.g., how runtime grows with the number of tokens or layers) would help practitioners assess practicality.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that Equation 5 is inconsistent with its stated meaning (Harsh Critic #2).** The critic claimed that the equation "only considers cycles whose birth and death coincide perfectly with the endpoints." This is factually incorrect. The sum is over birth $\leq \min(\ell_1,\ell_2)$ and death $> \max(\ell_1,\ell_2)$, which correctly captures all cycles alive throughout the interval between $\ell_1$ and $\ell_2$. The critic's own example (birth=2, death=10 evaluated at $\ell_1=3,\ell_2=9$) would be *counted* under the equation, contrary to the critic's assertion. *Removed as factually wrong.*

- **Claim that the pruning evaluation is "structurally flawed" because high persistence similarity could indicate important features to preserve (Harsh Critic #1).** The paper's logic is that high $\bar{S}_1$ indicates a "stationary" phase where "the relations among points are relatively stationary" (Section 3.4), making those layers redundant. This reasoning is implicit but coherent. The comparison to established pruning methods that select redundant layers via different similarity measures is a valid experimental approach. A random baseline would strengthen the paper, but calling the design "structurally flawed" overstates the issue. *Demoted from "structural" to "minor" (incorporated above as the missing random baseline point).*

- **Criticisms about missing appendix content, typos, formatting, and reproducibility details.** The parser strips appendix sections; the original submission contains them. Typographical issues are parser artifacts. *Removed per hard rules.*

- **Criticisms about the $k_{NN}$ tuning procedure being "circular."** The paper selects $k_{NN}$ to maximize the number of cycles but this is a standard heuristic in TDA applications. While it could be more principled, it is not a fatal flaw. *Demoted; incorporated as a minor reproducibility note.*

- **Strength Finder claim about "persistence similarity capturing the entire trajectory between layers."** This is accurate and supported by the paper's definition. *Retained in strengths.*

## Novel Insights

The most interesting observation from the reviews is the tension between the paper's genuinely novel TDA framework and the weakness of its experimental validation. The harsh critic correctly identified that the pruning comparison's credibility depends on an unsubstantiated claim about two methods producing identical outputs, while also making a serious mathematical error in reading Equation 5. This asymmetry suggests that the paper's core technical contribution is sounder than the critic's most severe attack would suggest, but the empirical evaluation — especially the pruning showcase — has real weaknesses that are independent of the core framework. The paper would benefit from treating the pruning experiment as a demonstration rather than a validation, and focusing more on descriptive topological analysis (the universal similarity peak) where the evidence is stronger.

## Suggestions

1. **Acknowledge the coincidence of the two pruning methods and provide evidence.** Show the specific layers selected by Gromov et al. and Men et al. separately, or explain why they coincide. If the claim is correct, it may itself be an interesting observation about the redundancy structure of LLMs.

2. **Add a random pruning baseline** at the same number of removed layers to establish that persistence-similarity-based selection outperforms chance.

3. **Include an ablation against a simpler baseline** such as cosine similarity between consecutive layer representations or the evolution of Betti numbers alone, to quantify what the zigzag machinery adds.

4. **Add uncertainty quantification** — at minimum, error bars across dataset subsets — for the pruning results.

5. **Soft-scope the "universal" claim** to "consistent across the decoder-only models tested" unless encoder-decoder/encoder-only verification is added.

6. **Clarify the notation in Equation 5** by using distinct variable names for the birth/death indices and the function arguments.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>

**Calibration anchors used (across rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/review_agent/human_reviews/mYgoNEsUDi.md | 6.33 | 1,2 | Zigzag spaghetti paper — stronger on theory (stability guarantees) and experiments; paper under review is weaker |
| /home/wg25r/review_agent/human_reviews/bVTM2QKYuA.md | 6.75 | 1 | LLM geometry paper — more rigorous theory and experiments; paper under review is weaker |
| /home/wg25r/review_agent/human_reviews/sq5gkjC9jv.md | 5.67 | 1,2 | TDA+NN paper — comparable; both have compelling core ideas but mixed review reception |
| /home/wg25r/review_agent/human_reviews/NiCSyYOfex.md | 5.33 | 1,2 | Node-level TDA — comparable; novel TDA method with some evaluation gaps |
| /home/wg25r/review_agent/human_reviews/RKXcTwWqVa.md | 5.20 | 2 | ECLayer — comparable; new topological descriptor with evaluation weaknesses |
| /home/wg25r/review_agent/human_reviews/L7gyAKWpiM.md | 5.80 | 2 | NN manifold topology — stronger theory but narrower scope |
| /home/wg25r/review_agent/human_reviews/QMQBza9BCx.md | 4.50 | 1,2 | PH for high-dim data — weaker; less novel application |
| /home/wg25r/review_agent/human_reviews/f7aWmxgSN4.md | 3.00 | 1 | Weak anchor — paper under review is clearly stronger |
| /home/wg25r/review_agent/human_reviews/EzjsoomYEb.md | 8.00 | 1 | Strong anchor — far stronger theory and experiments |
| /home/wg25r/review_agent/human_reviews/1M0qIxVKf6.md | 5.33 | 2 | LLM geometry — comparable; similar analysis of LLM representations |
| /home/wg25r/review_agent/human_reviews/q5lJxCXjiY.md | 5.40 | 2 | LLM geometry — comparable; geometric analysis of representations during training |
| /home/wg25r/review_agent/human_reviews/R4gqcDRJ9l.md | 5.75 | 2 | Topology + FR — stronger on application validation |
| /home/wg25r/review_agent/human_reviews/jsvvPVVzwf.md | 5.00 | 2 | Pruning theory — comparable quality; different domain |
| /home/wg25r/review_agent/human_reviews/TXvaWOBuAC.md | 4.25 | 2 | Compression theory — weaker; less clear contributions |