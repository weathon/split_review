- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6
Now I have a thorough understanding of the paper and can cross-check all reviewer claims against the actual text. Let me compile my final review.

## Summary

This paper proposes DeGEM, a decoupled energy-based model for node-level out-of-distribution detection on graphs. The key idea is to split the EBM into a graph encoder (trained via DGI and classification) and an energy head (trained via MLE in latent space), which avoids both the intractable MCMC sampling over graph structure and the energy-propagation step that degrades performance on heterophilic graphs. The paper also introduces a Multi-Hop encoder, Conditional Energy, Energy Readout, and a Recurrent Update mechanism. Experiments on seven datasets show large improvements over prior methods, especially on heterophilic graphs (+20.29% AUROC), and strong performance under limited labels.

## Strengths

- **Decoupled architecture that simultaneously solves two problems**: By moving MCMC sampling to the latent space, DeGEM avoids sampling adjacency matrices (a known intractability for EBMs on graphs) and eliminates the energy-propagation step that causes a 16% AUC drop on heterophilic graphs (Table 4, Row 2). This is a clean design insight — the theoretical motivation is laid out in Section 3.2–3.3, and the empirical evidence for both benefits is clear in the ablation study.

- **Large and consistent empirical gains across settings**: DeGEM raises average AUC by 6.71% on homophilic graphs and 20.29% on heterophilic graphs over prior methods (Tables 1–2), and these improvements hold across three OOD types (Structure manipulation, Feature interpolation, Label leave-out). The method also outperforms methods trained with OOD exposure (OE, Energy-FT, GNNSafe++) despite not using OOD data itself.

- **First systematic evaluation of node OOD detection on heterophilic graphs**: The paper identifies that prior work exclusively evaluates on homophilic graphs, constructs benchmarks on Chameleon, Actor, and Cornell, and shows that existing graph-based methods (especially GNNSafe) severely degrade on them (Figure 1, Table 2). This benchmarking contribution is valuable for the community.

- **Robust to limited labels**: When ID label ratios drop to 10%, DeGEM maintains high AUC while all baselines (including OOD-exposure methods) suffer significant declines (Table 3, Figure 4). This is practically relevant since labeling graph nodes is expensive.

- **Thorough ablation isolating the DGI+MLE synergy**: The ablation study (Table 4, Observations 1–4) shows that neither DGI alone nor MLE-Energy alone works (both below 74% AUC), but their combination jumps to 87.82%. The paper further tests GRACE and SUGRL with MLE (Table 5) and shows they do not achieve the same effect, supporting the claim that DGI's global-vs-local contrastive objective has a specific alignment with EBM training (Section 3.5).

## Weaknesses

### Fatal

None.

### Major

- **OOD exposure setup for synthetic-OOD datasets is underspecified**: For the five single-graph datasets where OOD is synthetically generated (Cora, Amazon, Chameleon, Actor, Cornell), the paper explicitly describes the OOD *synthesis* methods (Structure manipulation, Feature interpolation, Label leave-out) but **does not specify how the OOD exposure baselines (OE, Energy-FT, GNNSafe++) obtained their OOD training data** separate from the test OOD instances. For Twitch and ogbn-Arxiv, the paper clearly describes separate exposure/test splits. For the synthetic datasets, this is absent from the main text (line 203). The headline claim — "DeGEM, without OOD exposure, outperforms methods trained with OOD exposure" — depends on the fairness of this comparison. The paper follows the protocol of prior work (Wu et al., 2021, 2023b), so the comparison is *likely* fair, but the paper must explicitly state the separation. This is the single most important clarification the authors need to provide.

### Minor

- **No variance or confidence intervals reported**: All results in Tables 1–5 are single numbers without standard deviations or significance tests. Given the large claimed improvements (e.g., +20.29% on heterophilic graphs), it is important to know whether these wins are consistent across random seeds, data splits, or OOD synthesis runs. Reporting mean and std over at least 3–5 trials for the main tables would substantially increase confidence.

- **Conditional Energy architecture is underspecified**: The paper gives "for instance" examples of possible CE forms (line 149: "$f_{\omega}(h_{i},s)=\mathbf{W}[h_{i}\|\rho s]+b$, $f_{\omega}(h_{i},s)=h_{i}^{\top}\mathbf{W}s$, and etc.") but does not state which specific form is used in the experiments. This harms reproducibility — the exact architecture of $f_\omega$ should be specified.

- **Hyperparameter tuning for baseline methods is unclear**: The paper states Optuna was used for hyperparameter search (line 207) but does not describe the search space or tuning protocol for each baseline. This makes it difficult to assess whether baselines were reasonably tuned, especially given the large performance gaps claimed.

### Trivial

None.

## Nice-to-Haves

- **Deeper analysis of why DGI works and other GCL methods do not**: The paper notes (Table 5, Observations 1–4) that DGI succeeds with MLE-Energy while GRACE and SUGRL do not, and provides a theoretical connection in Section 3.5. A more detailed empirical analysis (e.g., probing the representation geometry learned by each GCL method, or measuring how close the learned representations are to a valid EBM) would strengthen the scientific contribution from an interesting observation to a principled design principle.

- **Computational cost comparison**: The method involves DGI pre-training, MCMC sampling (K=20 per epoch), and recurrent updates. A brief comparison of training time vs. baselines would help assess practical deployability.

- **Limitations discussion**: The paper does not discuss potential failure cases (e.g., sensitivity to the quality of the encoder, impact of graph size on MCMC efficiency, or scenarios where the decoupling assumption might break down).

## Removed Points

These points are flagged to be removed — treat them with caution:

1. **"MCMC sampling in latent space claim is oversimplified (critic says representations are still correlated)"** — Removed. The paper's phrase "latent space without interdependence" (line 17) refers to being *operationally free from the adjacency matrix* during MCMC sampling, not to statistical independence of representations. The critic's reading is overly literal.

2. **"2D Gaussian toy example is not direct evidence for graph data"** — Removed. The paper uses this as an illustrative motivation (Figure 3), not as experimental evidence. The graph experiments provide the actual evidence.

3. **"First to evaluate on heterophilic graphs may be inaccurate"** — Removed. The critic speculates without evidence. The paper's related work section surveys prior node OOD detection methods, none of which evaluate on heterophilic graphs. There is no external evidence to contradict this claim.

4. **"DGI/EBM derivation not rigorous / not standard DGI"** — Removed. Section 3.5 presents this as an *interpretation* ("can be understood as learning an EBM..."), not a formal proof. The reformulation of DGI's loss (contrasting real vs. shuffled) in density-ratio form is a known and valid interpretation from noise-contrastive estimation.

5. **"Computational cost / convergence of recurrent update"** — Moved to Nice-to-Haves. These are reasonable suggestions for improvement but not weaknesses that affect the current evaluation.

## Novel Insights

The harsh critic's implicit observation — that the paper's ablation study (Table 4) showing neither DGI alone nor MLE-Energy alone works, but their combination does — is genuinely important and the paper correctly elevates this. The strength finder's recognition that the decoupled architecture simultaneously solves two distinct problems (MCMC intractability *and* heterophily degradation) captures a non-obvious design insight that is the paper's core contribution. No additional novel insight emerges beyond what the paper itself articulates.

## Suggestions

1. **Clarify the OOD exposure setup for synthetic datasets**: Explicitly state whether a separate held-out set of synthetic OOD instances was used for training exposure baselines, and if so, how many instances, how they were generated, and whether they were disjoint from the test OOD instances. This is essential for the headline claim to be verifiable.

2. **Report variance**: Add standard deviations over multiple runs (even 3–5 seeds) to the main tables (1, 2, 4) and the limited-labels study.

3. **Specify the exact CE architecture**: State which form of $f_\omega(h_i, s)$ was used (e.g., concatenation with linear projection, or bilinear form), and provide the value of $\rho$.

4. **Soften the "first to evaluate" claim** to something like "To the best of our knowledge, we are the first..." to account for potential oversights in the literature survey.
