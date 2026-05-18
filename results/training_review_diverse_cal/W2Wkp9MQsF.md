Here is my final consolidated review:

---

## Summary

This paper introduces **model folding**, a data-free neural network compression technique that merges structurally similar neurons (channels) within a single network using k-means clustering, then repairs the disrupted activation statistics via two novel data-free methods: Fold-AR (approximate REPAIR assuming uncorrelated inputs) and Fold-DIR (Deep Inversion–based REPAIR). The paper provides a theoretical justification for k-means as the optimal clustering approach for minimizing Frobenius-norm reconstruction error, including a formulation that accounts for cross-layer interdependence. Experiments are conducted on ResNet18, VGG11, and ResNet50 on CIFAR10/100 and ImageNet, and on LLaMA-7B for LLM compression.

## Strengths

1. **Novel combination of k-means clustering with data-free variance repair.** The idea of using k-means (rather than greedy iterative matching) for within-network neuron merging, paired with theoretically motivated repair methods (Fold-AR and Fold-DIR), is a clean and well-motivated contribution. The derivation in Section 3.1 (Eqs. 4–9) showing that k-means minimizes the Frobenius reconstruction error provides a principled foundation.

2. **Data-free variance correction methods achieve near-data-driven performance on vision benchmarks.** Figure 5 shows that both Fold-AR and Fold-DIR achieve accuracy very close to the data-driven REPAIR (Fold-R) across sparsity levels on ResNet18/CIFAR10, while substantially outperforming IFM. Figure 4 demonstrates that Fold-AR and Fold-DIR maintain variance ratios near 1, unlike naive averaging (collapse) or IFM (overshooting). This is the paper's strongest empirical contribution.

3. **Consistent outperformance of the state-of-the-art data-free method IFM across multiple architectures and datasets.** Figure 6 shows model folding (with repair) outperforming IFM on ResNet18 and VGG11-BN on both CIFAR10 and ImageNet, with the gap widening at higher sparsity and on the more challenging ImageNet dataset.

4. **Ablation on network width confirms the method's operating principle.** Figures 8–9 demonstrate that wider architectures (MLP and ResNet50 with 1×/2×/3× width) benefit more from folding, consistent with the insight that increased channel redundancy improves folding effectiveness.

5. **Theoretical treatment of cross-layer interdependence.** The derivation of the combined approximation error J_{l,l+1} for concatenated weight matrices (Eqs. 10–18) provides a clean rationale for why clustering should consider adjacent layers jointly, beyond independent per-layer clustering.

## Weaknesses

### Major

1. **Unsubstantiated claim about outperforming INN.** The contribution list (line 26) states that model folding surpasses INN (Solodskikh et al., 2023), yet INN never appears in any experimental comparison (neither Tables nor Figures). A claim about beating a specific method must be either (a) backed by experimental evidence or (b) removed from the claims.

2. **IFM comparison fairness is not discussed.** The paper states (Fig. 1 caption) that "all methods were evaluated... at the same weight sparsity level, applied uniformly across all layers." IFM is an iterative greedy method that naturally produces *non-uniform* per-layer sparsity — its strength is adapting compression per layer. The paper does not explain how IFM was coerced into achieving uniform per-layer sparsity (e.g., stopping merging per layer at a target, or some other mechanism), nor does it discuss whether this handicaps IFM. Reporting IFM's performance under its natural sparsity distribution alongside the uniform version would make the comparison more informative.

3. **Missing ablation: concatenated vs. independent per-layer k-means.** The paper's theoretical claim (Section 3.1) is that concatenating W_l and W_{l+1}^T and clustering jointly accounts for cross-layer interdependence. However, Figure 3 compares k-means against spectral clustering, agglomerative clustering, and iterative greedy — *not* against independent per-layer k-means. Without this ablation, the reader cannot attribute the gains to the "concatenation trick" specifically. This is a central claimed advantage that remains unvalidated.

### Minor

4. **LLM results are overstated without appropriate qualification.** The paper claims (abstract, line 28, Table 1 caption) that model folding achieves "comparable performance to data-driven methods" on LLaMA-7B. However, the paper explicitly states (line 240) that "as there is no batchnorm layer in LLaMA-like LLMs, we just applied clustering in LLMs without REPAIR." This means the LLM results use only half the method (clustering without any repair). The claim of "comparable" should be tempered to reflect that these are preliminary results using only the clustering step, with repair mechanisms not applicable due to architectural constraints. Additionally, the paper should report which specific data-driven methods' results are being compared against and acknowledge any gap explicitly rather than using the ambiguous term "comparable."

5. **Fold-AR validated only on CIFAR10.** Fold-AR's uncorrelated-inputs assumption (which is a strong approximation — activations in deep networks are typically correlated) is evaluated only on CIFAR10 (Fig. 5). For ImageNet experiments (Fig. 6), the paper does not specify which variant of model folding was used. Fold-AR's viability as a genuinely data-free method (no synthetic data generation) on harder, higher-resolution datasets remains unestablished. The paper should either report Fold-AR separately on ImageNet or explicitly acknowledge this limitation.

6. **CIFAR100 experiments are limited to the width-ablation setting.** CIFAR100 is listed as a benchmark but is only evaluated on wider MLP and ResNet50 architectures (Fig. 9), not on standard ResNet18/VGG11 comparisons. Standard-benchmark results on CIFAR100 with these architectures would strengthen the paper's empirical scope.

### Trivial

7. **No discussion of actual computational speedup.** The paper reports sparsity (proportion of weights removed), but since compression is channel-level (structured), the actual speedup depends on hardware and implementation. A brief discussion of estimated speedup (or FLOPs reduction) would be helpful for practitioners.

8. **Limitations section is too brief.** The paper lists only two limitations (low-redundancy networks, no per-layer sparsity optimization). Other limitations worth mentioning: the dependence on BatchNorm for Fold-AR/Fold-DIR, Fold-AR's independence assumption, and the fact that LLM results use only clustering without repair.

## Nice-to-Haves

- An ablation comparing **concatenated (cross-layer) k-means vs. independent per-layer k-means** at multiple sparsity levels on at least CIFAR10/ResNet18.
- Reporting **Fold-AR and Fold-DIR separately on ImageNet** to establish whether the data-free approximations hold on more complex data.
- A more **carefully qualified claim** for the LLM experiments (e.g., noting that only the clustering step is applied, making these preliminary results that are competitive *given the constraint of no data/no fine-tuning and no repair mechanism*).
- Reporting IFM under its **natural (non-uniform) sparsity distribution** alongside the uniform-sparsity comparison.
- A brief discussion of **computational overhead** for the k-means clustering procedure on large models like LLaMA-7B.

## Removed Points

These points were flagged by reviewers but are removed (or moved here) for the following reasons:

- **Criticism about garbled sentence / incomplete reporting at line 240:** "Tab. Results of folding LLaMA2-7B (Touvron et al..." — This is a PDF text-extraction artifact, not an author error. The original submission does not have this issue.
- **"The term 'folding' is used in an overloaded way"** — Pure terminology nitpick; does not affect the paper's technical contribution.
- **"The zero-shot task averages are referenced but the actual numbers are not presented in the extracted text"** — The numbers are in Table 1 (an embedded image), which was stripped during PDF-to-text extraction. They exist in the original submission.
- **"Sparsity vs speedup not discussed"** — Moved to Trivial (not a core weakness).
- **"No discussion of computational overhead for k-means clustering"** — Moved to Nice-to-Haves.
- **Specific numerical claims about LLM perplexity values (7.96 vs 5.68):** These numbers are only visible in the image of Table 1 and cannot be independently verified from the extracted text. The underlying concern about the claim's strength is retained in Minor Weakness #4.

## Novel Insights

The reviews collectively surface an important structural critique: the paper's headline claim — that concatenated k-means with data-free repair is a complete solution — contains a hidden contingency. The "data-free" label actually bundles two separate claims (clustering without data + repair without data), and for LLMs, only the first is operationalized. This means the paper's scope (BatchNorm-equipped vision models) is narrower than its title suggests. A stronger paper would either adapt the repair method to LayerNorm/RMSNorm architectures or explicitly re-scope the contribution.

## Suggestions

1. **Add the missing ablation** comparing concatenated k-means vs. independent per-layer k-means on at least one dataset (e.g., CIFAR10/ResNet18 at several sparsity levels). This directly validates the claimed advantage of cross-layer interdependence.
2. **Report Fold-AR and Fold-DIR separately on ImageNet** (Fig. 6), so readers can assess whether the independence assumption in Fold-AR holds beyond simple datasets.
3. **Remove or substantiate the INN claim.** Either add an experimental comparison or delete the claim.
4. **Clarify the IFM setup.** Explain how IFM was configured for the uniform-sparsity comparison, or supplement with IFM's natural sparsity distribution results.
5. **Temper the LLM claims.** Replace "comparable" with more precise language that acknowledges: (a) no REPAIR was applied, (b) the gap to data-driven methods, and (c) that these are preliminary results for the clustering-only variant.
6. **Expand CIFAR100 evaluation** to include standard ResNet18/VGG11 comparisons, not just the width-ablation setting.

## Score and Decision

The paper introduces a genuinely novel compression method with a principled theoretical foundation and strong empirical results on vision benchmarks. The core contributions — k-means for within-network merging and data-free variance repair — are solid and well-supported. However, several issues weaken the paper in its current form: unsubstantiated claims (INN), a missing key ablation (concatenated vs. independent clustering), insufficient clarity about a central comparison (IFM), and overclaimed LLM results. These are addressable in revision but nontrivial.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>