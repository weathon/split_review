Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes Causal Differential Networks (CDN), a two-step approach for predicting perturbation targets from paired observational and interventional transcriptomics data. CDN first uses a frozen, pretrained amortized causal discovery model (SEA) to featurize each dataset into graph-structured hidden representations, then trains a learned axial-attention classifier to identify which variables were intervened upon. The method is evaluated on seven real single-cell transcriptomics datasets (five Perturb-seq, two Sci-Plex) and on synthetic benchmarks, consistently outperforming baselines including GEARS, PDGrapher, and GenePT, while also surpassing dedicated causal discovery algorithms on synthetic data at a fraction of the runtime.

## Strengths

- **Decoupled two-step architecture enabling scalability to transcriptomic scale.** By separating causal graph inference (via a frozen amortized featurizer) from target prediction (via a supervised classifier), CDN scales to thousands of variables where joint-search algorithms like DCDI and BaCaDI are intractable (requiring hours even for N=10). This design decision is the key enabler for the method's applicability to real biological data.

- **State-of-the-art perturbation target prediction across seven real transcriptomics datasets.** CDN consistently achieves the highest mean rank and recall@k compared to GEARS, PDGrapher, GenePT, Linear, and MLP baselines on five Perturb-seq datasets (Table I) and ranks targets higher than PDGrapher on all six drugs in two Sci-Plex datasets (Table II). The paper also demonstrates that CDN "is the only model that consistently ranks the ground truth perturbation targets higher than would be expected by random."

- **Strong performance on synthetic soft-intervention benchmarks with informative ablation.** On soft interventions with nonlinear mechanisms, CDN achieves an mAP of 0.78, far exceeding DCI (0.25) and its own MLP variant (0.45) (Table III). The ablation replacing axial attention with an MLP cleanly demonstrates that graph-level edge information is essential for soft interventions, validating the architectural motivation.

- **Transfer to unseen cell lines without retraining.** CDN maintains competitive performance on held-out cell lines (e.g., mean rank 0.58 on unseen RPE1 vs. 0.49 for PDGrapher), indicating that the amortized causal featurizer generalizes across biological contexts.

- **Release of curated benchmark datasets.** The paper curates seven transcriptomics datasets with careful filtering procedures (excluding perturbations with low statistical power, minimal effect, or failed CRISPR targeting), providing a standardized evaluation resource for future work.

## Weaknesses

### Fatal
None.

### Major

- **The causal featurizer's specific contribution is not validated on real data via direct ablation.** The paper attributes CDN's success to causal structure captured by the SEA-based featurizer, but provides no ablation on real transcriptomics data that isolates whether the *causal* nature of the pretraining matters. The existing ablations (Table III) compare axial attention vs. MLP within the differential network, but do not test what happens when the SEA featurizer itself is replaced with a non-causal alternative (e.g., correlation/covariance difference matrices, PCA-derived features, or a randomly initialized version of the same aggregator network). Given that the featurizer was trained purely on synthetic Erdős–Rényi graphs with different structural properties than real gene regulatory networks, it is possible that the method works for reasons orthogonal to causal structure (e.g., the featurizer acts as a learned dimensionality reducer that captures distributional shifts). A simple real-data ablation comparing CDN against a version with a non-causal or randomly initialized featurizer would substantially strengthen the causal claims. This is the paper's most significant gap, though it does not invalidate the empirical contribution — the method works well regardless of the exact attribution.

### Minor

- **No uncertainty estimates on real-data results.** Tables I and II report point estimates for rank, recall@k, and Pearson r without confidence intervals, standard deviations, or significance tests. Given variability across perturbations and the relatively small number of evaluations per dataset, the strong comparative claims (e.g., "CDN is the only model that consistently ranks ground truth targets higher than random") would be more compelling with distributional evidence such as bootstrapped intervals.

- **The "without using any external knowledge" claim (line 53) is slightly imprecise.** While the paper correctly notes that CDN does not use biological knowledge graphs (unlike GEARS and PDGrapher), the method does use a pretrained model trained on thousands of synthetic datasets. This is a different *kind* of external knowledge, and the contrast with baselines like GenePT (which also uses pretrained embeddings) blurs the distinction. This is a minor presentation issue, not a technical flaw.

- **The informal theoretical claims (Section 3.5) are acknowledged as unprovable and do not connect to experimental predictions.** The paper candidly states that it "cannot 'prove' that a pretrained model extracts correct graphs on real data," and the informal claims about well-specifiedness neither derive testable predictions nor guide model design decisions. This section adds little and could be condensed or removed.

### Trivial
None (the paper is generally well-written and the presentation is clean).

## Nice-to-Haves
- A brief analysis of the soft-intervention transfer result (trained on hard interventions only, performs well on soft interventions) — the paper notes this positive result but does not discuss what features of the featurizer enable this robustness.
- A failure analysis section discussing common failure modes across datasets (e.g., the doxorubicin/T98G case is noted but not systematically analyzed).
- Additional reproducibility details about dataset normalization, QC, and gene subset selection could be useful for the claimed benchmark resource.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"The causal featurizer's contribution is not validated" as a fatal-level weakness.** Demoted from fatal to major. The paper's core empirical contributions (SOTA performance, scalability, synthetic benchmarks) stand regardless of whether the success is fully attributable to the causal objective. The method demonstrably works; the attribution question is an important but secondary concern that does not invalidate the paper's contributions.

- **Criticisms about the synthetic experiment training/evaluation gap (hard→soft transfer).** The paper explicitly discusses this result (lines 341-343) and provides a plausible explanation — that graph-level information is essential for soft interventions. The reviewer's suggestion for further analysis is a nice-to-have, not a weakness.

- **Criticisms about the preprocessing selection bias (filtering to >10 DE genes).** The paper transparently describes this filtering as a quality-control step to exclude perturbations with low statistical power or no effect. This is standard practice and not a methodological flaw.

- **Criticisms that the theoretical context section is "too vague to be useful."** Moved to minor/nice-to-have. The paper is upfront about the limitations of theoretical guarantees in this setting. The section is not harmful even if it adds limited practical value.

- **The baseline asymmetry criticism implying unfair comparison.** While the pretrained featurizer is a genuine difference, the comparison is not asymmetric in a way that disadvantages CDN's competitors — GEARS uses gene ontology, PDGrapher uses the human interactome, GenePT uses LLM embeddings. Each method brings different priors. The comparison is fair; the specific concern about CDN's pretraining advantage is subsumed into the Major weakness about the missing featurizer ablation.

- **Strength Finder's generic strengths.** Removed vague strengths like "this paper addressed an important problem" and "the paper is well-written" — kept only concrete, evidence-grounded strengths.

## Novel Insights
None beyond the paper's own contributions. The key insight — decoupling combinatorial graph+target search into independent featurization followed by supervised classification — is the paper's own contribution and is already well-articulated. The reviews do not surface a genuinely novel perspective that the paper itself does not express.

## Suggestions
1. **Add a real-data ablation replacing the SEA featurizer with a non-causal alternative.** The single highest-value addition would be comparing CDN against a version where the featurizer is replaced with (a) correlation difference matrices between obs and int data, (b) PCA of the pooled expression used as node features, or (c) a randomly initialized (frozen) version of the same SEA architecture. If CDN significantly outperforms these, the causal framing is directly supported.
2. **Report bootstrapped confidence intervals** for the key metrics (rank, recall@k) on real datasets to quantify variability and support comparative claims.
3. **Clarify the "external knowledge" language** to distinguish between biological knowledge graphs (not used) and synthetic-data pretraining (used).
4. **Add a brief discussion of the hard→soft transfer result** in the main text, explaining what properties of the featurizer or classifier enable this generalization.

## Score and Decision

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>