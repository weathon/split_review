- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3
Now I have a thorough understanding of the paper and can verify every claim made by the reviewers. Let me construct the final consolidated review.

---

## Summary

This paper proposes a benchmark process for creating FL benchmarks on multi-semantic datasets, addressing a gap where existing FL benchmarks focus on single-label tasks (e.g., MNIST, CIFAR). The pipeline has two steps: (1) discover semantic clusters by applying K-means to a "category tensor" constructed from multi-label annotations, and (2) partition data across clients using shard-based or Dirichlet-based strategies on the cluster labels, enabling controllable semantic heterogeneity. As a proof-of-concept, the authors construct an FL benchmark for Panoptic Scene Graph Generation (PSG) and evaluate four PSG models (IMP, MOTIFS, VCTree, GPS-Net) across six partition configurations, finding that performance degrades as semantic heterogeneity increases. The paper also tests FedAvg vs. FedAvgM and varies total clients and participation rates.

## Strengths

- **First FL benchmark for multi-semantic vision tasks (SGG/PSG).** The paper correctly identifies that prior FL benchmarks handle only one-hot labels (e.g., image classification), while tasks like scene graph generation require managing multiple semantics (objects, subjects, predicates, relations) per sample. The related work survey (Section 2.1) confirms no prior FL benchmark exists for PSG, and the paper fills this gap with a concrete instantiation.

- **Task-agnostic clustering method without extra pretrained models.** The category tensor K-means approach (Section 4.1) converts multi-label annotations into a tensor by allocating each label type to an orthogonal axis, then clusters via K-means. This is contrasted with FedNLP, which requires a pretrained language model. The method is demonstrated on PSG data, producing 5 interpretable clusters (Section 4.3) with coherent semantics (animals, daily people, urban transport, sports, nature+urban).

- **Controllable semantic heterogeneity via cluster-label partitioning.** By reducing multi-semantic labels to cluster labels (one-hot), the paper extends standard label-based partition strategies (shard and Dirichlet) to multi-semantic data. The experiments in Table 1 test 6 distinct partition types (Random, Shard-IID, Shard-nonIID, Dirichlet with α=10, 1, 0.2), demonstrating that the benchmark can induce different levels of semantic heterogeneity. The ordering CL ≥ IID ≥ Random ≥ non-IID is largely supported, confirming that random partitioning (used in prior work) fails to impose meaningful non-IID structure.

- **Varying total clients and participation rates.** Tables 3 and 4 systematically vary total clients (50/100/200) and participation rates (5/20), revealing interesting patterns such as VCTree's sensitivity to per-client data volume. This provides useful guidance for the research community on how PSG models behave under different FL resource configurations.

## Weaknesses

### Fatal

None.

### Major

- **Very limited FL algorithm evaluation.** The paper presents itself as an "FL benchmark," yet only two FL algorithms are tested: FedAvg and FedAvgM. The latter is a minor variant of the former (adding server momentum). Other FL algorithms designed for heterogeneity (FedProx, SCAFFOLD, FedDyn, FedSAM — all cited in Section 2.1) are not evaluated. For a benchmark paper to demonstrate usefulness for the FL community, it must show that the benchmark can discriminate between meaningfully different FL algorithms. As it stands, the experiments overwhelmingly compare PSG model architectures under an FL *training schedule*, not FL algorithms. The paper's claim that the benchmark is for "evaluating federated learning algorithms" is not well-supported by the evidence.

- **Underspecified category tensor construction.** The paper states that the category tensor is formed by "allocating each label y_i into an orthogonal axis of the tensor" (Section 4.1), resulting in a 13×13×7 = 1183-dimensional tensor for PSG. However, it is not specified how a single image with *multiple* scene graph relations (multiple object-subject-predicate triplets) is converted into a single tensor. Are entries binary indicators of whether a triplet type appears? Counts? Normalized frequencies? This is a critical reproducibility gap. Without this detail, the clustering pipeline cannot be independently reimplemented on other multi-semantic datasets, which limits the claimed generality of the benchmark process.

- **No variance or statistical significance reporting.** The paper reports only point estimates (single numbers) for all experiments. Given that each client has only ~114 images (Section 5.2), the 5 participating clients per round see ~570 images per round, and total training runs for only 100 rounds. The reported differences between settings (e.g., -0.64% to -0.77% mR@20 between IID and non-IID) are smaller than typical standard errors in similar low-data FL settings. Without standard deviations over multiple seeds, it is impossible to determine whether the observed performance ordering reflects genuine semantic heterogeneity effects or random noise. This undermines the statistical reliability of the benchmark's results.

- **No quantitative validation of cluster quality.** The 5 discovered clusters are characterized only qualitatively (Section 4.3 and Figure 3). No cluster quality metrics (silhouette score, purity against held-out metadata, stability across K-means initializations) are provided. The cluster sizes are highly imbalanced (one cluster occupies 58% of data), and the paper does not justify why K=5 is the correct choice or what happens with different K. Since the entire benchmark pipeline hinges on these clusters being semantically meaningful, the lack of validation weakens confidence that the induced "semantic heterogeneity" is actually semantic.

### Minor

- **Moderate non-IID ordering is not perfectly consistent.** The paper claims the expected ordering CL ≥ IID ≥ Random ≥ non-IID, but MOTIFS shows non-IID (α=0.2) mR@20 = 4.28% vs. moderate non-IID (α=1) = 4.09%, and α=0.2 is actually *higher* than α=1 (Section 5.2). The paper acknowledges this ("the moderate non-IID can be a little shaky") but does not investigate further. While this is not a fatal inconsistency, it weakens the claim that the benchmark imposes a monotonic relationship between α and performance.

- **Low absolute performance is not discussed as a limitation.** The reported mR@20 values (4–6%) are far below centralized PSG performance (~28% for GPS-Net). The paper attributes this to the FL setting and limited per-client data, but does not discuss whether this floor-level performance makes fine-grained comparisons unreliable. While not as dire as the critic claimed (the random baseline over 56 predicate classes is far below 4%, not the ~14% the critic asserted), the question of whether the regime is too data-constrained to be informative deserves explicit discussion.

- **No comparison to the natural (unequalized) cluster setting.** The paper equalizes cluster sizes to isolate semantic heterogeneity from the long-tailed problem, which is a reasonable design choice. However, never running the *unequalized* baseline means readers cannot evaluate the trade-off: does equalization remove meaningful signal along with confounds? Adding this comparison would help the community understand the impact of this design decision.

- **Missing convergence analysis.** Training runs for only 100 rounds with 1 local epoch. No learning curves are shown, so it is unclear whether models have converged. The low absolute performance could be partially due to insufficient training.

### Trivial

- The paper's title and abstract refer to "Scene Graph Generation" (SGG), but the experiments use only Panoptic Scene Graph Generation (PSG). The distinction is mentioned but the title/abstract are not fully aligned.
- Figure 3 (cluster visualization via PCA) is referenced but the actual figure is not accessible in the text version.
- Minor punctuation/capitalization inconsistencies in the text (e.g., "esaily" for "easily" on line 45).

## Nice-to-Haves

- **Test with more FL algorithms (FedProx, SCAFFOLD, FedDyn)** to validate that the benchmark can discriminate between heterogeneity-handling methods. This alone would significantly strengthen the paper's claim to be an "FL benchmark."
- **Report results over multiple random seeds (≥3) with standard deviations** to establish that observed differences are statistically meaningful.
- **Run the natural (unequalized) cluster setting** and show how results change when cluster imbalance is present.
- **Provide cluster validation metrics** (silhouette score, purity, stability) to quantitatively verify that the clustering captures meaningful semantic structure.
- **Show learning curves** (mR@K vs. communication rounds) to verify convergence and allow readers to assess whether 100 rounds is sufficient.

## Removed Points

These points from the reviewers were evaluated and removed with justification:

- **"Absurdly low absolute performance invalidates comparisons"** (Harsh Critic's Critical Issue #2, including the ~14% random baseline claim). **Removed because factually wrong.** The critic claimed random baseline for mR@20 is ~14% based on 7 predicate super-categories. However, mR@K is computed over "every predicate category" (Section 5.1 Metrics) — the PSG dataset uses 56 *fine-grained* predicate classes for evaluation, not the 7 super-categories used for clustering. A random baseline over 56 classes would be far below 14%. The critic's arithmetic undermines the severity of this claim. The underlying concern about statistical reliability is preserved above as a minor weakness (missing variance reporting) and a minor weakness (low performance deserves discussion), but the "absurdly low" framing is removed.
  
- **"~12 images per client in shard non-IID"** (Section 4.2 note). **Removed because calculation error.** The critic computed ~12 images per client, but the correct figure is ~122 images per client (2,450 images per cluster ÷ 20 clients per cluster = ~122). The paper itself states "Each client has approximately 114 images" (Section 5.2), confirming the critic's calculation is off by an order of magnitude.

- **"Cluster equalization fundamentally undermines realistic semantic heterogeneity"** framing as a fatal flaw. **Demoted to a minor weakness.** The paper explicitly justifies equalization as necessary to isolate semantic heterogeneity from the long-tailed problem (Section 4.2). This is a design *trade-off*, not a flaw. However, the paper's failure to also test the unequalized setting is kept as a minor weakness above.

- **Strengths that are generic or conflict with verified weaknesses.** The Strength Finder's claim of "Validation with multiple FL algorithms" is dropped from strengths — only 2 FL algorithms (FedAvg, FedAvgM) are tested, which is insufficient for the claimed breadth. The claim about "Cluster balancing to isolate heterogeneity from long-tail effects" is acknowledged as a design choice but dropped as a named strength because the trade-off is substantial.

- **Formatting/style nitpicks, missing appendix content, missing related works.** Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviewer analyses do not reveal a pattern or insight about the paper that the paper itself does not express.

## Suggestions

1. **Expand FL algorithm testing.** Add at least 2–3 more FL algorithms (FedProx, SCAFFOLD, or FedDyn) and show that the benchmark produces meaningful rank-orderings correlated with the α heterogeneity parameter. This is the single most impactful change to validate the benchmark as an "FL benchmark" rather than a "PSG-model-under-FL evaluation."

2. **Specify the category tensor construction in detail.** Provide a precise algorithm or formula for converting a scene graph with multiple triplets into the 13×13×7 tensor (binary indicators vs. counts, normalization, handling of images with varying numbers of relations). This is essential for reproducibility and for applying the process to other multi-semantic datasets.

3. **Report results with multiple seeds (≥3) and standard deviations.** Without variance estimates, the small performance gaps between settings cannot be distinguished from noise. This is particularly important given the low per-client data volume.

4. **Add a comparison to the natural (unequalized) cluster baseline.** Running experiments without the equalization step would demonstrate the impact of this design choice and help the community understand the trade-off.

5. **Include cluster quality metrics** (e.g., silhouette score, stability across K-means restarts) and a sensitivity analysis on the number of clusters K. This would strengthen confidence that the clustering captures genuine semantic structure.

6. **Include convergence plots** (mR@K vs. communication rounds) and consider increasing the number of rounds or local epochs if the models have not converged at 100 rounds.
