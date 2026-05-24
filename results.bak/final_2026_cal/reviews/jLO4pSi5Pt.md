Now I have all the information I need. Let me write the final consolidated review.

## Summary
This paper introduces L-TTA, the first test-time adaptation method specifically designed for vision-language models under long-tailed test distributions. It proposes three co-designed mechanisms: Synergistic Prototypes (combining Deterministic and Exclusionary Prototypes to enrich tail-class representations), Rebalancing Shortcuts (learnable cross-attention vectors with class re-allocation loss), and Balanced Entropy Minimization (a theoretically-motivated variant of entropy minimization that reduces head-tail gradient imbalance). Extensive experiments across 15 datasets at three imbalance ratios (10, 20, 50) and multiple backbones show consistent improvements over 12 baselines, with ablation studies confirming each component's contribution.

## Strengths
- **First systematic study of long-tailed TTA for VLMs with clearly identified failure modes.** The paper pinpoints two VLM-specific challenges under long-tailed test streams: *Text-induced Tail Erosion* (pre-trained text biases compounding head-tail imbalance) and *Modality-bias Amplification* (unimodal LT-TTA applied to VLMs damaging cross-modal alignment). These go beyond generic long-tailed analysis and directly motivate the bi-modal design of L-TTA.

- **Consistent and significant improvements across 15 datasets at three imbalance ratios (Tables 1–3).** L-TTA outperforms all 12 baselines, with gains that are especially pronounced in macro-F1 (e.g., +1.70% Mac. on OOD Average at imb=10, +2.20% on Cross-Domain Average, +2.64% on Corruption Average). The macro-F1 gains directly support the claim of improved class balancing, and the pattern holds at imb ∈ {10, 20, 50}.

- **Theoretical motivation for Balanced Entropy Minimization (Propositions 1 & 2).** Proposition 1 formally shows that standard EM creates a gradient imbalance favoring head classes; Proposition 2 proves BEM reduces the absolute gap between head and tail class gradients. This provides principled justification beyond heuristic loss design.

- **Robustness across backbone scales and architectures (Table 5).** L-TTA maintains ~1.5% Acc / ~1.8% Mac gains over strong baselines on ViT-L/14, ViT-H/14, SigLIP-L/16, and MetaCLIP-BigG, showing the method is not brittle to a particular backbone size or pretraining strategy.

- **Comprehensive ablation and sensitivity analysis (Table 6, Figure 4).** Every component is ablated (on two backbones), and hyperparameters λ₁, λ₂, η, K, β are systematically explored with clearly documented trade-offs. The dynamic ordering robustness test (Table 7) further strengthens the claim that L-TTA is not sensitive to tail-sample arrival order.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **The $K$ hyperparameter (number of hyper-class vectors in Rebalancing Shortcuts) is inconsistently specified.** In the method section (Sec. 3.2), $K$ is introduced as an integer count of hyper-class vectors. But the implementation details give $K=0.3$, and the ablation study varies $K$ from 0.1 to 1.0 and reports $K=0.2$ as optimal. A count cannot be 0.3. The paper should clarify whether $K$ is a fraction (e.g., of the number of classes) that is then rounded to an integer, or something else. The figure caption labels this as "$b$" while the text uses "$K$," adding further confusion. This does not invalidate the method, but it impairs reproducibility.

- **The Exclusionary Prototype update (Eq. 5) uses a non-standard formulation whose behavior is not analyzed or justified.** The EMA-like update uses a counter-based weight $(N - \phi_c)$ in the numerator with L2 normalization, where $\phi_c$ varies per-sample per-class. The effective contribution of a new sample to the EP is $1/(N - \phi_c + 1)$, which changes dynamically. The paper does not explain the rationale for this specific formulation, how it differs from a controlled momentum, or what advantages it provides over simpler alternatives (e.g., storing only the least-confident views per class). The empirical ablation (Table 6) shows EPs help, but the mechanism is underspecified.

- **No measure of variance in main results.** All tables report single numbers; the paper states "5 runs for each experiment" but provides no standard deviations, confidence intervals, or significance tests. Given the comparison scale (13 methods × multiple datasets × 3 imbalance ratios), readers cannot assess whether the 1–2% gains are reliable or within noise. This is a common omission in the field, but including variance would substantially strengthen the evidence.

- **Several notation gaps in key equations.** (i) Eq. 6's cross-attention notation $\text{Attn}([\mathbf{v}_c, \mathbf{t}_c], \mathbf{q}_j)$ is underspecified — it is unclear which arguments serve as query, key, and value, and how the attention output is combined with $\mathbf{q}_j$. (ii) Eq. 9 uses $\tilde{\mathbb{P}}$ without definition — it appears to be $\sigma(z)$ (the softmax of original logits), but this should be explicit. (iii) The figure caption for Fig. 4c uses "$b$" while the text uses "$K$" for the same hyperparameter.

### Trivial
- The paper lacks a limitations section. Obvious candidates include: the method requires online estimation of class priors; the number of hyper-class vectors $K$ is a free parameter that may vary per dataset; performance at the most extreme imbalance (imb=50) shows some degradation.

## Nice-to-Haves
- Visualizing what EPs actually store (e.g., nearest neighbors to EP centroids for tail classes) would strengthen the claim that they capture meaningful cross-class knowledge rather than simply accumulating head-class features.
- Including a baseline that combines TPT with simple test-time logit adjustment (using estimated class frequencies) would help isolate the benefit of the full L-TTA pipeline.
- Adding pairwise statistical significance tests against the strongest baseline would address the variance concern without requiring full confidence intervals.

## Removed Points
The following points from the input reviews were removed after cross-checking against the paper:
- *"The denominator $(N_{c,s}^{EP} - \phi_c)\mathbf{u}_c + \tilde{\mathbf{u}}_c$ … creates an ill-defined cumulative weight"* — The update is mathematically defined (it is a counter-based EMA with class-specific offset and L2 normalization); it is non-standard and unexplained, but not ill-defined. Downgraded from the critic's framing to Minor.
- *"Proposition 1 and 2 proofs in appendix"* — Standard practice for conference papers; not a weakness.
- *"The paper does not state the size of the test set after subsampling"* — A standard experimental detail not essential for evaluating the method's contribution.
- *"Baseline hyperparameter tuning may be unfair"* — The paper states baselines use "their provided hyperparameters," which is standard and fair.
- Several generic strengths from the Strength Finder (e.g., "the paper addresses an important problem") were removed for lacking specific grounding.

## Novel Insights
The most interesting observation that emerges across both reviews is the tension between the paper's creative-but-complex EP design and the relatively simple motivation: the EP update stores features from *all* images into *every* class's prototype, weighted by how improbable they are for that class. The paper's narrative glosses over the fact that tail-class EPs are primarily updated from head-class images (since most samples are head-class). Yet the ablation shows EPs do help. This suggests the benefits may come from a mechanism other than "enriching tail class representations with inter-class knowledge" as claimed — perhaps EPs provide a form of distributed representation that regularizes the decision boundary holistically. The paper would be stronger if it directly analyzed this gap between claimed mechanism and observed effect.

## Suggestions
- **Resolve the $K$ ambiguity.** Clarify whether $K$ is a fraction or an integer, and ensure consistent notation between text and figures. State the actual integer values used for each dataset.
- **Add standard deviations to all main tables** (Tables 1–3) or provide them in an appendix with a summary in the main text.
- **Define $\tilde{\mathbb{P}}$ in Eq. 9 explicitly** and specify the attention mechanism in Eq. 6 (query/key/value roles).
- **Add a brief limitations paragraph** discussing the reliance on estimated class priors and the sensitivity of $K$ to dataset scale.

## Score and Decision

**Calibration Report.**

*Round 1 (Bracketing):* Queried three bands on topics related to VLM test-time adaptation and long-tailed learning. Weak band (avg ≤ 3.5) returned withdrawn/rejected papers — L-TTA clearly stronger. Strong band (avg ≥ 7.5) returned Oral papers on different topics (text-to-3D, embodied navigation, multimodal reasoning) — L-TTA not at that tier. Middle band (3.5–7.5) returned anchors at 4.50–6.00. **Initial bracket: [4.5, 6.5]**.

*Anchors retrieved in Round 1 (partial list):* HeGMugkCOH (3.00, Withdrawn), CFAYmfjd4v (3.20, Withdrawn), snbY9Uj0Gx (2.67, Withdrawn), CUmbgiiNff (3.00, Reject), 8L83ZbFDjk (6.00, Poster), DX2POJEk8C (4.50, Reject), dHj8hC081K (4.50, Poster), OdWkyqnkiS (4.50, Reject).

*Round 2 (Narrowing within bracket):* Queried (5.5, 7.5) and (6.0, 8.0) bands. Read in full: dHj8hC081K (ADTE, 4.50 Poster) — L-TTA is stronger (greater novelty, broader experiments, first to address this specific problem); 8L83ZbFDjk (Conformal Prediction for Long-Tailed, 6.00 Poster) — comparable quality but different subfield; rMHZfCznhZ (RLAP-CLIP, 6.00 Poster) — similar structure (multi-component VLM adaptation with prototypes), L-TTA compares favorably (broader datasets, new problem); 1c6Ao3CpKt (TTT theory, 6.80 Poster) — more theoretically deep, L-TTA has stronger empirical breadth.

*Final bracket:* [6.0, 6.5]. L-TTA is above the 4.50-level papers (its weaknesses are all minor, its novelty clearer) and comparable to the 6.00-level posters. It is not as theoretically deep as the 6.80 paper but has outsized empirical breadth. The paper's weaknesses (notation gaps, missing variance) are common and fixable; no fatal flaw exists. **Score: 6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>