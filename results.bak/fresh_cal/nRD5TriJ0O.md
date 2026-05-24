Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper investigates active learning on heterophilic graphs, finding that existing GAL methods (designed for homophilic graphs) select training sets with incorrect homophily distributions — causing them to underperform even random sampling. The authors propose KyN, which labels entire subgraphs rather than isolated nodes ("know your neighbors") and selects subgraphs via ℓ₁ Lewis weight sampling with a relative-error coreset guarantee. Empirical results show consistent gains across six heterophilic datasets, three labeling budgets, and two backbone architectures.

## Strengths

1. **Novel diagnosis of why prior GAL methods fail on heterophilic graphs.** Figure 2 and the analysis in Section 3.1 reveal that previous GAL methods produce training sets whose local homophily distribution is left-skewed (homophilic) even on heterophilic graphs, while the ground-truth distribution is right-skewed. This is a clear, well-illustrated insight that identifies the root cause of the performance gap.

2. **First principled active learning method for heterophilic graphs with strong empirical results.** KyN consistently outperforms all prior GAL methods across six datasets and three budgets (Table 1), with improvements up to 12.1% on Roman-empire. It is the only method that reliably beats random sampling, and the gains hold when using heterophilic-specific GNN backbones (FAGCN, M2M-GNN; Table 2).

3. **Novel theoretical contribution extending coreset theory to graph active learning.** Theorem 3.6 provides a relative-error guarantee for ℓ₁ Lewis weight subgraph sampling under cross-entropy loss with a one-layer linear SAGE-Mean encoder. This is the first application of Lewis weight sampling to GAL, and the coreset framework gives the sampling strategy a principled foundation.

4. **Robustness and scalability demonstrated.** KyN is stable across a wide range of the partition hyperparameter \(c\) (Figure 5), scales to a 2M-node graph (snap-patents, Table 3) where several baselines time out, and maintains competitive runtime (Figure 4).

## Weaknesses

### Fatal
None.

### Major

1. **Theory–practice gap weakens the theoretical contribution.** Theorem 3.6 is proved for a **one-layer linear** SAGE-Mean encoder, but experiments use a **three-layer non-linear** SAGE-Mean (the SAGE formula at line 171 includes a non-linearity \(\sigma\)). The paper claims "the results are similar on any multi-layer linear GNNs" (line 133), but the experimental encoder is non-linear, and no verification experiment with a one-layer linear encoder is provided. This means the coreset guarantee does not directly cover the evaluated setting. The theoretical section is presented as a formal guarantee for KyN, but the disconnect between the theory's assumptions and the experiments' configuration is not acknowledged. At minimum, the paper should explicitly state that the theory applies to a simplified linear setting and serves as principled intuition rather than a guarantee for the full method.

### Minor

2. **Framing inflation in the abstract and conclusion.** The abstract and conclusion state that prior GAL methods "fail to outperform the naive random sampling" on heterophilic graphs. However, the evidence section (5.2) correctly uses the qualified phrase "fail to *consistently* outperform." Since some prior methods may beat random on some datasets, the unqualified claim overstates the case. The weaker, correct version should be used throughout.

3. **Missing "label node + neighbors" baseline.** The paper's central principle is that labeling nodes along with their neighbors is crucial for heterophilic GAL. However, no baseline that directly implements this (e.g., randomly selecting seed nodes and labeling all their 1-hop neighbors within budget) is compared against. Such a baseline would isolate whether KyN's gains come from the Lewis-weight subgraph sampling strategy or merely from the general principle of labeling more neighbors. Including it would sharpen the attribution of the method's success.

4. **Theorem 3.2 (Hoeffding bound) assumes random neighbor sampling, which does not match KyN's subgraph-selection mechanism.** The bound assumes \(n_i\) neighbors are sampled uniformly at random from a node's neighborhood. In KyN, neighbors are obtained via METIS subgraph selection — a concentrated, non-random set. The theorem is presented as a motivating principle, so this gap does not invalidate the method, but it should be noted that the theorem's formal assumptions are not satisfied by KyN's actual sampling process.

### Trivial
5. The homophily level of snap-patents is not reported. Since it is used as a "large heterophilic graph," stating its global homophily value would help readers calibrate the difficulty of the dataset.

## Nice-to-Haves

- A small-scale verification experiment with a one-layer linear SAGE-Mean encoder to directly validate Theorem 3.6.
- An ablation replacing ℓ₁ Lewis weight sampling with uniform subgraph sampling in the main text (if the "More detailed component analysis" in the original submission does not already cover this).
- Replace the average-pooling subgraph representation (Eq. 6) with the proposed central-node representation (Eq. 8) to isolate the value of the Jordan center design.
- A limitations/discussion section addressing edge cases (e.g., extremely sparse partitions, very small-diameter graphs, or large budgets where subgraph size grows).

## Removed Points

These points were considered and removed with justification:

- **"Missing essential ablations"** — The paper has a "More detailed component analysis" section header (line 259); content was likely in the appendix, which the parser strips. Following the rule to not penalize missing appendix content, this criticism is removed.
- **"Proposition 3.1's 'necessary' is too strong"** — The critic claimed "correlated with" would be more precise. However, the proposition proves a bound D ≤ (1/n)Σ(1−Acc\(_i\)) + (1−Acc), which correctly shows that high accuracy implies small D. This is a valid necessary condition; the criticism is factually incorrect.
- **"Parser-garbled notation in theoretical analysis"** — This is a PDF-extraction artifact, not a flaw in the submission.
- **"Full table in text"** — The table appears as an image in the original PDF, which is standard practice; the text description in Section 5.2 provides sufficient numerical context.

## Novel Insights

Beyond the paper's own contributions, the most valuable observation emerging from the review process is that **the framing-disconnect pattern (stronger claims in abstract/conclusion vs. qualified claims in the body) mirrors a broader tension in the paper between theoretical rigor and practical validation.** The theory claims a formal coreset guarantee, but the practical evaluation uses a more complex encoder; the sampling theorem assumes i.i.d. neighbors, but the method uses structured subgraph selection. The paper's empirical strength is clear, but the narrative would benefit from acknowledging these gaps rather than papering over them. This is a calibration issue — the paper is stronger when it honestly delineates what the theory covers vs. what the experiments validate.

## Suggestions

1. **Harmonize the central claim.** Replace "fail to outperform" with "fail to consistently outperform" in the abstract and conclusion to match the body.
2. **Acknowledge the theory-practice gap explicitly.** Add a sentence in the theoretical analysis section stating that Theorem 3.6 is proved for a simplified (one-layer linear) setting, and that the empirical results demonstrate the method's effectiveness in the more complex (multi-layer non-linear) setting beyond the scope of the guarantee. Optionally, add a small-scale verification.
3. **Add a "label neighborhoods" baseline.** Randomly select seed nodes and label their 1-hop neighbors (within budget). This would directly test whether the benefit comes from "knowing neighbors" generally or from KyN's specific sampling strategy.
4. **Report the global homophily value** for snap-patents in Table 3 or in the experimental setup.

## Score and Decision

**Summary evaluation across axes:** The paper addresses an important, under-studied research question (GAL on heterophilic graphs) with originality in both diagnosis (homophily distribution mismatch) and methodology (subgraph labeling + Lewis weight sampling). The central claims about method performance are well-supported by extensive experiments. The main weaknesses are a theory-practice disconnect that undermines the theoretical contribution's scope, and some framing inflation. These are addressable in revision and do not invalidate the core empirical contribution. The writing is clear and the value to the community — opening a new direction in heterophilic GAL — is substantial.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>