- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 3, 8
Now I have all the information I need. Let me construct the final consolidated review.

## Summary

This paper identifies a non-obvious pitfall in mechanistic interpretability: a 1-dimensional subspace found via activation patching (e.g., DAS) can appear to encode a feature when it actually combines a *causally disconnected* direction (in the kernel of an MLP's down-projection) with a *dormant* direction (causally effective but not differently activated between conditions). The authors demonstrate this mathematically via a toy model, then empirically in GPT-2 Small on the IOI task and GPT-2 XL on factual recall. They further show an approximate equivalence between 1D subspace interventions and rank-1 model edits (ROME), providing a mechanistic explanation for why ROME can "work" in layers where facts are not stored. A success case in the residual stream contextualizes the findings.

## Strengths

1. **Formal decomposition of the illusion into causally disconnected and dormant subspaces** — Section 3.2 (Eq. 4) gives a precise, algebraically tractable characterization of how a subspace patch can work by activating a dormant direction through a disconnected one, rather than intervening on a feature the model actually uses. The toy model (Section 3.3) cleanly instantiates the same mechanism.

2. **Empirical demonstration in the IOI task** — Table 1 shows that patching the DAS-found direction $\mathbf{v}_{MLP}$ gives 46.7% FLDD, which drops to 13.5% when only the rowspace component is patched and to 0% for the nullspace component alone. Full-MLP patching actually hurts performance (−8%), directly contradicting the claim that this MLP layer encodes the position feature. Figure 3 further shows the patch moves the MLP output off-distribution, activating a previously dormant effect on name-mover head attention.

3. **Formal and empirical connection between 1D activation patches and rank-1 weight edits (ROME)** — Section 6 develops an optimization-based equivalence and validates it on the CounterFact dataset. The subspace intervention approximates ROME's rewrite score closely across layers 20–35, yet removing the kernel component destroys the effect (rewrite scores < 10⁻³). This provides a mechanistic explanation for prior observations (Hase et al.) that ROME works in layers where the fact is not stored.

4. **Contrastive success case in the residual stream** — Section 4 shows that patching $\mathbf{v}_{resid}$ and $\mathbf{v}_{grad}$ in the residual stream achieves FLDD > 100% and interchange accuracy > 45%, and removing the nullspace component has little effect. This provides a grounded benchmark for what a faithful subspace looks like and shows the illusion is location-specific.

5. **Clear practical recommendations** — Section 8 provides actionable advice for practitioners: use activation bottlenecks (especially the residual stream) and validate beyond end-to-end effects.

## Weaknesses

### Fatal
None.

### Major
- **The prevalence claim is not fully supported by the evidence.** The abstract states the paper "present[s] evidence for its prevalence in practice," and the title/contributions lean toward prevalence being a central claim. However, the evidence only shows the illusion *can* occur (in two settings: IOI and factual recall). Section 7's theoretical argument is plausible but relies on heuristic assumptions ("pre-nonlinearity activations approximately preserve linear separability through GELU and projection onto ker W_out") without rigorous empirical validation beyond the two case studies. A broader survey across tasks, layers, and models would be needed to establish prevalence, or the claims should be toned down. This is an evidential gap rather than a structural flaw, but it creates a mismatch between the paper's framing and its empirical scope.

### Minor
1. **No confidence intervals or uncertainty measures for key metrics.** The paper reports point estimates (FLDD, interchange accuracy, rewrite scores, cosine similarities) without error bars or statistical tests. For example, the difference between 46.7% (full $\mathbf{v}_{MLP}$) and 13.5% (rowspace-only) is central to the argument, but the reader cannot assess whether the 13.5% could be noise. Histograms in figures show distributions, but aggregate metrics lack variance estimates.

2. **The rowspace-only patch for $\mathbf{v}_{MLP}$ still yields 13.5% FLDD.** The paper attributes this to "approximate dormancy" but does not explore whether this residual effect has a different mechanism (e.g., the rowspace component carries some weak real signal). A simple control — patching along a random direction in the rowspace, scaled comparably — would strengthen the claim that the rowspace component is "dormant."

3. **The residual stream success case uses a different and weaker notion of "causally disconnected" than the MLP case.** For the MLP, $\ker W_{out}$ is *provably* causally disconnected. For the residual stream, no such provably disconnected subspace exists; the paper uses the kernel of the name-mover heads' query matrices as a proxy. The paper acknowledges this asymmetry (Section 4.2), but the comparison is not symmetric, and the "nullspace" of $v_{resid}$ is not guaranteed to be causally disconnected in the same sense.

4. **The ROME equivalence uses a modified subspace intervention** ($\mathbf{x} - (\mathbf{v}^\top \mathbf{x})\mathbf{v}$ rather than standard activation patching $\mathbf{x} + (p_A - p_B)\mathbf{v}$). The paper notes this is a "closely related" variant, but the practical effects could differ because the magnitude of change differs from standard patching. The core intuition about the illusion transferring from IOI to factual recall is sound, but the difference should be flagged more prominently.

5. **The centrality of component boundaries as meaningful analytic units** is an implicit premise of the paper's framing. The paper transparently discusses this in Section 8, acknowledging that a rotation crossing component boundaries could make the "illusory" subspace appear meaningful. The arguments for why component boundaries are meaningful (qualitatively different functions, parsimony) are reasonable but not definitive. This limits the scope of the illusion's practical significance to the extent that the community agrees on component-level analysis.

### Trivial
None.

## Nice-to-Haves
- A broader empirical survey (across multiple layers, tasks, models) of how often DAS finds illusory subspaces in MLP layers vs. the residual stream would substantially strengthen the prevalence claim. Without this, the paper should more carefully calibrate its language about prevalence.
- A concrete example from published literature of how this illusion could mislead an actual circuit analysis (beyond the ROME connection) would increase practical impact.
- A clearer diagnostic threshold (e.g., "ratio of nullspace FLDD to full FLDD should be less than X to rule out illusion") would be practically useful.

## Removed Points
These points were identified by reviewers but are removed from the main evaluation for the following reasons:
- *"Figures and tables are not embedded in the extracted text"* — This is a limitation of the review format, not a problem with the paper itself.
- *"The Section 6 derivation is not fully explained in the main text"* — The paper explicitly refers readers to the appendix for derivations; appendices are stripped by the parser. The main text provides the key takeaway (Eq. for $\mathbf{v}$ form). This is standard practice.
- *"The ROME connection should be more explicit about using a variant"* — The paper already states it is "a closely related subspace intervention" and notes the similarities. The paper is sufficiently explicit.
- *Pure formatting or presentation nitpicks* — Removed per filtering rules.

## Novel Insights
The harsh critic notes that "the paper does not show that real interpretability practitioners have been misled by this in a published analysis (beyond the ROME connection, which is indirect)." However, the reviewer overlooks that the ROME connection *is* the primary practical demonstration of how this illusion matters — it directly explains published puzzling observations (Hase et al. 2023) and shows that a well-known method (ROME) can succeed via the same dormant-pathway mechanism. The synthesis of the two reviews reveals a subtle point the individual reviews miss: the paper's strongest non-obvious contribution is showing that *even if* a subspace intervention successfully changes model outputs *and* the optimization finds it, that subspace may still be causally spurious. This is a qualitatively different kind of failure from known issues (e.g., backup behavior via the hydra effect) because it arises from linear-algebraic necessity rather than learned redundancy.

## Suggestions
1. Add confidence intervals or standard deviations to the main FLDD and interchange accuracy metrics.
2. Include a control experiment for the 13.5% rowspace residual effect (random direction of comparable norm in the rowspace).
3. Either provide broader empirical evidence for prevalence (e.g., scanning more layers/tasks/models) or soften the prevalence claims in the abstract and title to match the evidence.
4. More prominently flag the asymmetry between the MLP's provably disconnected $\ker W_{out}$ and the residual stream's proxy-based "nullspace."
5. Make the difference between standard subspace patching and the $\mathbf{x} - (\mathbf{v}^\top \mathbf{x})\mathbf{v}$ variant used for the ROME connection more explicit.
