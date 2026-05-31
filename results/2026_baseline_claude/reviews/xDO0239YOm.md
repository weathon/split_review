## Summary

HYPOGENEAGENT is an LLM-driven framework for automating clustering resolution selection in single-cell Perturb-seq data. An LLM (GPT-o3) annotates each cluster with ranked GO hypotheses and calibrated confidence scores; sentence embeddings of these hypotheses are used to compute an intra-cluster agreement (ICS) and an inter-cluster distinctiveness (ICD), whose weighted combination yields a "Resolution Score." The resolution maximizing this score is selected as the optimal clustering granularity. The method is demonstrated on a K562 CRISPRi Perturb-seq dataset, with the selected resolution claimed to outperform silhouette and modularity scores in recovering known biology.

---

## Strengths

- **Addresses a genuine and underappreciated gap.** Resolution selection in Leiden/Louvain clustering is widely acknowledged to be subjective, and incorporating biological knowledge (GO/KEGG annotations) into the selection criterion is a well-motivated idea. No existing tool closes this loop between unsupervised partitioning and functional annotation simultaneously.

- **Modular, model-agnostic design.** The framework's Stage 1 benchmark systematically evaluates multiple LLMs (GPT-4o, GPT-o3, GPT-5, Gemini variants), two prompt styles, three embedding methods, and temperature settings. The finding that "thinking LLMs" with hypothesis prompts outperform single-output prompts is a concrete and useful ablation for practitioners choosing a backbone.

- **Self-consistency validation in Stage 1.** The demonstration that GPT-o3's self-assigned confidence scores correlate with the external cosine-similarity ground truth (Figure S3) provides an independent, quantitative sanity check on the agent's calibration — a useful result beyond the main contribution.

---

## Weaknesses

### Fatal

1. **Circular validation loop.** The Resolution Score is derived entirely from LLM-generated annotation texts: a good score is achieved when the LLM produces internally consistent and mutually distinct descriptions. The paper then "validates" this by showing that functional enrichment analysis (ORA/Fisher exact on GO terms) selects a similar resolution. However, enrichment analysis operates on the same gene sets that were annotated by the LLM in the first place. The LLM effectively selects the partition that makes its own summaries look most coherent, and this is then corroborated by a method that processes the same inputs. There is no independent biological ground truth — e.g., known pathway membership, genetic interaction labels, or held-out perturbation outcomes — used to confirm that the chosen resolution is biologically superior. The central claim ("selects clustering granularities that exhibit alignment with known pathways compared to classical metrics") is therefore not established by the evidence presented.

2. **The comparison against silhouette and modularity does not demonstrate superiority.** The paper observes that silhouette peaks at r ≈ 0.5–0.6, modularity peaks at r = 0.7, and HYPOGENEAGENT selects r = 0.4 (GEX level). But the paper does not show that r = 0.4 is biologically *better* — it only shows that it is *different*. To support the superiority claim, one would need a quantitative evaluation, such as: fraction of known CRISPRi effects correctly assigned to the same cluster, ARI against a curated pathway-based ground-truth partition, or number of statistically significant GO terms recovered per cluster. None of these evaluations are performed.

### Major

1. **Single-dataset validation.** The entire Stage 2 evaluation relies on one public K562 Perturb-seq dataset. HYPOGENEAGENT is presented as a general-purpose framework applicable to single-cell and multi-omics studies broadly, but no second dataset (e.g., a different cell line, a different perturbation type, or a standard scRNA-seq atlas) is used to demonstrate generalizability or reproducibility of the resolution-selection behavior.

2. **Unjustified weight hyperparameter w = 1/3.** The paper states this weight "was chosen by a small grid search and found to give a stable ordering of resolutions across data sets." However, the grid search appears to have been performed on the same K562 dataset used for evaluation (there is no separate validation set mentioned). This constitutes implicit tuning on the test data. Figure S5 also shows that the resolution ordering changes substantially with w for individual clusters, raising concerns about the robustness of the single-dataset conclusion.

3. **No statistical significance assessment for score differences across resolutions.** The box plots in Figures 3 and 4 show overlapping distributions across many resolution values. There is no test for whether the score at the chosen resolution is statistically distinguishable from adjacent resolutions. Without this, the "selection" of a single optimal r is not well-justified.

### Minor

1. The Stage 1 curated GOBP benchmark contains only 100 gene sets. Whether these are representative of the full GO space and free from selection bias toward well-annotated pathways is not discussed.

2. The cost and latency of running GPT-o3 across 10 resolutions × up to 20 clusters × 5 hypotheses per cluster is not reported. For users with larger datasets this is practically important.

3. The weighting formula RS_k = w·ICS_k + (1−w)·(1−ICD_k) is stated but not derived from first principles, and the asymmetry (one-third vs. two-thirds) is not intuitively motivated.

### Trivial

None worth noting beyond parser artifacts already excluded from evaluation.

---

## Nice-to-Haves

- An evaluation on at least one additional Perturb-seq or scRNA-seq dataset with an independent biological ground truth (e.g., known pathway clusters) would substantially strengthen the paper.
- Reporting the dollar cost and wall-clock time per resolution sweep would help practitioners assess feasibility.

---

## Novel Insights

The core idea of using the *semantic consistency of LLM-generated annotations* as a proxy for cluster quality — rather than geometric or graph-theoretic properties of the data — is a genuine conceptual innovation. If properly validated, this would represent an important bridge between statistical clustering methodology and biological interpretability in single-cell genomics. The observation that GPT-o3's self-confidence scores are well-calibrated against external semantic similarity (Figure S3) is also a mildly novel finding with broader implications for LLM-assisted annotation tasks.

---

## Suggestions

1. Add a held-out quantitative evaluation using an independent ground truth: e.g., cluster-level recovery of CRISPRi perturbation effects known from literature, or ARI against a pathway-annotated reference partition.
2. Validate on a second dataset (different cell type, different assay) to substantiate the generality claim.
3. Separate the w hyperparameter grid search from the evaluation data, or fix w at a principled value (e.g., w = 0.5) and report sensitivity.
4. Add a permutation or bootstrap test to assess whether the score differences between resolutions are statistically significant.

---

## Score and Decision

The paper addresses a real problem and the core concept is novel. However, as an ICLR submission, the central empirical claim — that HYPOGENEAGENT is superior to traditional resolution-selection metrics — is unsupported. The validation is circular (LLM annotation quality is verified by related annotation-based methods on the same gene sets), relies on a single dataset, and lacks any quantitative comparison against a biological ground truth. These are not minor presentation issues; they call into question whether the claimed contribution is actually demonstrated. The work is better suited, in its current form, for a domain-specific workshop or preliminary application note.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>