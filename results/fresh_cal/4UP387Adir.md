Now I have a complete understanding of the paper. Let me synthesize the final review.

## Summary

This paper studies the robustness of graph contrastive learning (GCL) methods under weak/noisy labels and proposes WSNet, a method that incorporates signals from both graph communities and weak label distributions into a two-part contrastive objective (\(L_S + L_{\text{SupCon}}\)). The authors provide a systematic empirical evaluation of 8 GCL methods at three noise levels (RQ1), then demonstrate that WSNet + downstream classifier outperforms SSL, NLL, and supervised-GCL baselines, particularly under high noise (53%) and on non-homophilous graphs (RQ2).

## Strengths

1. **First systematic robustness study of GCL under weak supervision.** Table 2 evaluates 8 GCL methods (DGI, GRACE, MVGRL, GCA, GraphCL, GMI, SUGRL, iGCL) across three noise levels and five datasets, quantifying each method's performance degradation. This fills an explicit gap and provides practical guidance (e.g., neighborhood-based positive sampling methods like SUGRL and iGCL are more robust under high noise).

2. **Novel method WSNet with clear two-part design.** The paper proposes a principled combination of a community-aware structural loss (selecting positives via Louvain communities + weak-label frequency similarity) and a supervised contrastive loss using aggregated labels. Both components are clearly specified in Equations 3–4 and Algorithm 2.

3. **Strong SOTA results under high label noise.** In the 53% noise setting (Table 3a), WSNet+RF achieves weighted F1 of **0.815** on Cora (next best: NRGNN at 0.680), **0.745** on Texas (next best: 0.627), and **0.740** on Wisconsin (next best: 0.675). These margins are substantial and demonstrate that weak labels combined with community structure can be highly effective.

4. **Ablation confirms both loss components are necessary.** Removing either \(L_S\) or \(L_{\text{SupCon}}\) consistently degrades performance across noise settings (Table 3, ablation rows), providing internal validation that the two-part design drives the reported gains, not just the encoder.

5. **Strong and consistent performance on non-homophilous graphs.** WSNet outperforms all baselines on Texas and Wisconsin (low-homophily datasets) at every noise level, supporting the paper's hypothesis that community-based sampling is beneficial when neighborhoods are not class-homogeneous.

6. **Scalability consideration.** For Pubmed, the authors limit negative sampling to 1,000 random out-of-community nodes without practical performance loss, addressing a common practical concern.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Encoder architecture not controlled across methods.** WSNet uses a simple encoder (one graph convolution layer averaging neighbor features, followed by a linear layer, Equation 1), while GCL baselines were used with their official code and default (often deeper) architectures. This architectural difference means the observed gains cannot be fully attributed to the contrastive loss design versus the encoder choice. The ablation studies validate the loss components within WSNet's architecture, but a controlled comparison using a shared encoder backbone across all methods would more cleanly isolate the contribution of the contrastive objective. The paper does not acknowledge this as a potential confound.

2. **Transparency gap in supervised GCL baseline adaptation.** The experimental setup (line 96) states that all methods—including supervised GCL baselines SupCon, ClusterSCL, and JGCL—only had access to weak labels during training. However, the paper does not describe how these methods (which natively require clean labels) were adapted: were the aggregated labels fed directly into the SupCon pairing logic? Was the loss function modified? Were label-abstention cases handled? This makes it difficult for readers to assess whether the baselines were adapted fairly or optimally.

3. **Community-based positive selection mechanism not probed.** The structural loss \(L_S\) selects positives from the same Louvain community by maximizing dot-product similarity of weak-label frequency vectors. When weak labels are highly noisy (53% noise), this similarity measure itself may be unreliable, yet the paper does not analyze (a) the purity of detected communities against ground-truth labels, (b) how noise level affects the quality of community-based positive selection, or (c) whether the benefit comes from community structure, weak-label similarity filtering, or simply having more positive pairs. An ablation replacing community-based selection with random neighborhood sampling would sharpen the attribution.

### Trivial
None.

## Nice-to-Haves

- A controlled experiment using a **shared encoder backbone** (e.g., fixed 2-layer GCN) across all methods would strengthen the claim that the contrastive loss, not architecture, drives performance.
- **Statistical significance tests** (e.g., paired t-tests across splits) would help assess whether the reported advantages are reliable given the variance observed on small datasets like Texas.
- An ablation of the **weighting hyperparameter** between \(L_S\) and \(L_{\text{SupCon}}\) (currently fixed at equal weight without justification).
- Discussion of the **independence assumption** in the synthetic label generation process (Algorithm 3 generates weak labels independently conditioned on the true label), which may differ from real-world programmatic weak supervision where labeling functions often have complex dependencies.

## Removed Points

These points from the original reviews are removed with justification:

- **"Missing Algorithm 1"** (Parser artifact — the algorithm is referenced in the paper and exists in the original submission; the PDF-to-text extraction does not include it.)
- **"Table 4 is missing from the extracted text"** (Same parser artifact.)
- **"No works systematically study robustness — claim too strong"** (The critic acknowledges this is defensible for the GCL-specific angle. The paper's claim is appropriately scoped.)
- **"Weak labels independence assumption may affect generality"** (This concerns the synthetic data generation used for controlled experiments, which is standard practice. The paper does not claim the synthetic data reflects all real-world scenarios.)
- **"High variance on Texas with LR is unsatisfactorily explained"** (The paper's explanation — small dataset, LR sensitive to noise, RF does not show the issue — is empirically grounded and reasonable.)
- **Generic strengths from Strength Finder** about "important problem" and "addresses interesting question" — dropped as superficial.
- **Strength about first systematic study** and **ablation confirmation** — kept, as they are specific and evidence-supported.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel observation that is absent from the paper itself.

## Suggestions

1. **Conduct a controlled encoder experiment** — replicate the main comparison with all methods using a common 2-layer GCN backbone. This would cleanly isolate the effect of the contrastive loss and directly address the most significant methodological concern.
2. **Explicitly describe baseline adaptation** — add a sentence or table explaining how each supervised GCL baseline was supplied with weak labels (e.g., "SupCon was given aggregated labels as if they were true labels, with no modification to the pairing logic").
3. **Probe L_S mechanism via ablation** — replace community-based positive selection with random neighborhood sampling to test whether the benefit comes from community structure or from having additional positives. Also report community purity against true labels across datasets.

## Score and Decision

This paper tackles a well-motivated, under-explored problem and presents both a useful empirical study and a promising method. The results under high noise are compelling, and the ablation studies support the design choices. The weaknesses are real but addressable — the core methodological concern (encoder confound) does not invalidate the paper's contributions, though it limits the strength of the attribution claims. With the suggested controlled experiments and transparency improvements, the paper could be made substantially stronger.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>