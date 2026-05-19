Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper connects GNN feature propagation to Dynamic Mode Decomposition (DMD) from Koopman theory, proposing a family of DMD-GNN models that estimate a low-rank linear operator from GNN feature dynamics and use the resulting DMD modes as a spectral filter basis. The method is evaluated on node classification, long-range benchmarks, spatiotemporal prediction, and link prediction, with theoretical analysis linking DMD outputs to slow spectral subspaces.

## Strengths

- **Novel conceptual integration of DMD/Koopman theory with GNN dynamics.** While DMD is a standard algorithm, applying its spectral decomposition to GNN feature snapshots and using the resulting modes as a learnable filter basis is a genuinely new idea that bridges two previously separate lines of work (dynamical systems and graph representation learning).

- **Theoretical grounding via Lemma 1** (Section 6) establishes that the DMD-estimated operator locally approximates the linearized dynamics on a slow attracting spectral submanifold, with error bounded by the fast-decaying subspace. This provides principled justification beyond a heuristic application of DMD.

- **Flexible framework with consistently improved variants.** Four DMD variants (DMD-GCN, DMD-SGC, DMD-ACMP, DMD++) are derived from different initial dynamics, and each outperforms its non-DMD counterpart (e.g., DMD-GCN vs. GCN, DMD-SGC vs. SGC) across multiple datasets, demonstrating that DMD extraction adds value regardless of the base propagator.

- **Interpretable hyperparameter tuning guided by spectral theory.** The paper derives (Section 6) that narrower eigenvalue ranges in the initial dynamics favor homophilic graphs and wider ranges favor heterophilic ones. The sensitivity analysis (Section 6.4) validates this empirically — optimal truncation rate ξ is larger for homophilic graphs (Cora, Citeseer) and smaller for heterophilic ones (Texas, Cornell) — providing actionable guidance for practitioners.

## Weaknesses

### Fatal
None.

### Major

1. **The training procedure integration of DMD is underspecified, undermining reproducibility.** The paper describes how DMD takes "multiple system states, e.g., h(ℓ) and h(ℓ+1)" to produce DMD modes, but it never clarifies whether (a) the DMD computation (which involves SVD and pseudoinverses) is performed **once as a preprocessing step** from the initial dynamics before training, or (b) **recomputed during training** as features evolve. If the latter, no account is given of how gradients flow through the SVD-based estimation. If the former, the DMD modes depend on the initial random feature snapshots, making the approach sensitive to initialization — yet no analysis of this sensitivity is provided. This ambiguity makes it impossible to reproduce or fully trust the reported results. (Related: the paper provides no training details whatsoever — no optimizer, learning rate, epochs, or loss function are mentioned.)

2. **Missing important baselines on two of the four evaluation tasks.** On the long-range benchmarks (Table 2), the comparison set is limited to MLP, GCN, GPRGNN, and SGC — none of the established LRGB methods (e.g., GPS, CRaWl, SAN) are included, making it impossible to judge whether the reported Macro-F1 scores (~0.09 on COCO-SP) are competitive. On the spatiotemporal prediction task (Table 3), the paper uses three small epidemiological datasets (Chickenpox, Covid, WikiMath) and omits the standard traffic benchmarks (METR-LA, PEMS-BAY) and established spatiotemporal models (DCRNN, STGCN, GWNet) that are the norm in the STGNN literature. These omissions significantly weaken the evaluation of what is presented as a general-purpose method.

3. **The claim of "state-of-the-art performance" in the abstract is not uniformly supported by the evidence.** On several datasets, DMD-GNNs are within error bars of or worse than simpler baselines: on Citeseer, APPNP achieves 75.9±0.6 vs. the best DMD variant at 73.2±0.4; on Chickenpox, all models are within ~0.01 MSE of each other; on link prediction (Chameleon), all DMD variants underperform GraphSAGE. Many of the reported improvements have overlapping error bars with baselines, and no statistical significance tests are provided. The paper would benefit from calibrated language that accurately reflects where DMD-GNNs truly excel vs. where they are competitive but not clearly superior.

### Minor

- **The theoretical result (Lemma 1) is adapted from prior work (Haller et al. 2024) and is not empirically validated.** The conditions (rank(H)=d, fast-decaying subspace) are never checked in experiments, and the "topologically conjugate" claim is invoked but never connected to any observable behavior. It currently functions as a conceptual justification rather than a verifiable part of the paper's evidence.

- **No analysis of computational cost or model size.** DMD involves an SVD of the feature matrix (O(N·d²) in the typical case). For large graphs like OGB-arXiv (~170K nodes), the computational implications are non-trivial, yet runtime and memory comparisons are entirely absent. This is relevant for a method whose practical value depends on efficiency.

- **The physics-informed DMD extension (PIDMD-GNNs, Section 8) is too preliminary to support claims.** It is evaluated on only two directed graphs (Computer, Photo), results are presented only in a figure without numerical values or baseline comparisons, and the single observation (PIDMD-GNNs underperform/outperform DMD-GNNs on directed/undirected graphs) is insufficient to draw conclusions.

- **Missing some relevant heterophily and spectral baselines.** LINKX, GGCN, and ACM-GCN are established methods for heterophilic node classification and are absent from Table 1. While the included baselines (GPRGNN, H2GCN, APPNP) are reasonable, the comparison set could be strengthened.

### Trivial
None.

## Nice-to-Haves

- Adding statistical significance tests (paired t-tests) would clarify which improvements are reliable given the overlapping error bars.
- An ablation comparing DMD modes against random eigenvectors or graph Laplacian eigenvectors would directly test whether the DMD dynamics extraction provides unique value.
- Adaptive rank selection (per layer or per task) rather than a single fixed ξ could improve flexibility.

## Removed Points

The following points from the reviewers were removed after cross-checking against the paper:

- **"No mention of spectral GNNs like ChebNet, BernNet, JacobiConv"** — ChebNet **is** included in the spatiotemporal experiments (Table 3). The paper also includes GPRGNN and Framelets, which are spectral methods. The broader criticism about missing spectral filter comparisons is partially valid, but the factual claim is incorrect; this point was merged into the minor weakness about missing heterophily/spectral baselines rather than kept as a standalone criticism.

- **"On Texas, MLP (92.3%) is a strong baseline — the paper does not explain why MLP performs so well"** — This is a well-documented characteristic of small heterophilic datasets (high feature informativeness, small graph size) and is not a flaw specific to this paper. The DMD++ result (92.6%) surpasses MLP anyway.

- **"The discussion of Graph Neural Diffusion Models cites only a narrow slice"** — Generic framing, no specific missing work identified. The paper's related work section is appropriate for its scope.

- **"The informal Lemma lacks a rigorous proof"** — The paper explicitly labels it "Informal" and cites Haller et al. (2024) for the full derivation. This is standard practice for conference papers adapting known results.

- **"Comparisons are unfair because DMD may favor certain datasets"** — No evidence provided; this is speculative.

## Novel Insights

The most interesting observation emerging from juxtaposing the reviews is that the paper's core strength (a principled dynamical-systems approach to GNN feature propagation) is also the source of its main weakness: the theoretical framing demands a level of methodological specificity about how DMD integrates with training that the paper does not provide. The sensitivity analysis showing that ξ aligns with graph homophily in a theoretically predictable way is the paper's cleanest empirical result, yet it is presented as a secondary experiment rather than the centerpiece. A revision that strengthens this dynamical interpretation — for example by directly measuring whether DMD modes correspond to the slowest-decaying frequency components of the learned features — could significantly raise the paper's impact.

## Suggestions

1. **Most critical:** Explicitly clarify the training procedure. State whether DMD modes are computed once as a preprocessing step or recomputed during training. If recomputed, describe how gradients flow (or explain why DMD is treated as a fixed preprocessing transform). Provide training hyperparameters (optimizer, learning rate, epochs, loss function).

2. Add the missing LRGB baselines (GPS, CRaWl, SAN) and spatiotemporal baselines (DCRNN, STGCN, GWNet) to properly contextualize the results. If computational constraints prevent re-running, clearly state the limitations.

3. Tone down the "state-of-the-art" claim to match the evidence. The paper's contribution is better framed as demonstrating that DMD provides a useful inductive bias for spectral filtering in GNNs, with competitive results across several tasks.

4. Add a runtime/memory comparison to show how the SVD-based DMD computation scales with graph size, especially for OGB-arXiv.

5. Run a simple diagnostic experiment comparing DMD-GNN using true DMD modes vs. random eigenvectors vs. Laplacian eigenvectors to confirm that the DMD dynamics extraction is the source of improvement.

## Score and Decision

**MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>**