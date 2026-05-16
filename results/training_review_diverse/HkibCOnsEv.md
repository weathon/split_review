Now I have a thorough understanding of the paper and both reviews. Let me produce the final consolidated review.

---

## Summary

This paper extends the inverse-free natural gradient descent (INGD) framework to create a memory-efficient and numerically stable second-order optimizer for modern architectures. The authors propose (i) IKFAC, an inverse-free variant that recovers KFAC-like updates without matrix inversions, and (ii) SINGD, which imposes structured sparsity on Kronecker factors via Lie-algebraic subspace projections to reduce memory to AdamW-like levels. Experiments on transformer and CNN architectures with mixed-precision (BFloat16) are described, with claims that SINGD matches AdamW performance while KFAC becomes unstable.

## Strengths

- **Well-motivated problem and clear positioning.** The paper convincingly identifies two concrete limitations of KFAC — numerical instability in low-precision training and memory overhead from dense Kronecker factors — that have hindered its adoption for large-scale training. The connection between INGD and KFAC is a natural and worthwhile direction to pursue.

- **Novel approach to structured Kronecker factors via Lie-algebraic projection.** The design of subspace projection maps (Table 1) that are closed under the operations needed for INGD (matrix addition, multiplication, scalar multiplication) is technically interesting. The idea of imposing sparsity on the Kronecker factors **K** and **C** in the logarithm space (rather than on **Sₖ** and **Sₑ** as in prior work) is a principled departure from existing structured KFAC approaches and exploits the structure of the INGD update.

- **Addresses a timely practical need.** Making second-order methods viable for half-precision training is relevant given the dominance of low-precision pipelines in large-scale deep learning. The paper tests on a diverse set of modern architectures (Compact-ViT, Swin-ViT, GC-ViT, Rep-ViT) across both CNN and transformer families, going well beyond the convolution-only evaluation of prior INGD work.

## Weaknesses

### Fatal
None.

### Major

- **The core theoretical contribution (IKFAC's equivalence to KFAC) is asserted but not demonstrated in the extracted text.** Section 3.1 consists of only two paragraphs (lines 153–160) that state "we propose an inverse-free KFAC update scheme" and "IKFAC corresponds to a specific setting of the INGD method," but provide no equations, no theorem statement, and no derivation showing how a specific choice of INGD's parameters recovers the KFAC update (including damping, exponential moving averages, and gradient scaling). Theorem 1 is referenced in the Figure 2 caption but is absent from the text body. Even accounting for content that may reside in figures/images, the paper's **first claimed contribution** — bridging INGD and KFAC — cannot be evaluated from the presented material. This is a structural gap: the central theoretical anchor of the paper is unverifiable.

- **The experimental section reports no quantitative results.** Section 4 (lines 181–197) describes datasets, models, and training configuration, but the only "results" are qualitative statements: "SINGD with the hierarchical structure performs as well as AdamW and outperforms IKFAC" and "KFAC performs unstably." No test-error numbers, standard deviations, memory-footprint values, wall-clock times, or training curves are reported in the text. Figure 5 (an image of test error curves) is referenced, but the text offers no precise quantitative summary. This makes the empirical claims — which are central to the paper's stated contributions — impossible to assess or reproduce from the information provided. The gap is especially concerning for claims about memory efficiency (referenced Table 3, missing) and iteration cost (referenced Table 2, missing).

### Minor

- **The SINGD algorithm is incompletely specified.** Section 3.2 describes the conceptual framework (reparameterization map, subspace projection, Table 1) but does not provide a complete, self-contained algorithm listing. The structured INGD update scheme is referenced to Fig. 4 (an image, not present in the extracted text). Key details such as how **M** is updated, how the matrix exponential truncation integrates with the rest of the loop, and how the projection alternates with the updates of **A**, **K**, **C**, and **μ** are not given in the text. A reader would struggle to implement the method from the text alone.

- **No analysis or reporting of the exponential truncation order.** The paper mentions truncating the matrix exponential for efficiency but does not state how many terms are used or how this choice affects numerical stability, approximation quality, or wall-clock time. This is a meaningful design parameter for the claimed numerical robustness.

- **Hyperparameter sensitivity is underreported.** While the paper states that hyperparameters (other than momentum weight 0.9) were tuned via random search, the search ranges are not reported, and no sensitivity analysis is provided for SINGD-specific parameters (e.g., damping, truncation order, momentum weight for the structured factors). This limits reproducibility and understanding of how robust the method is to its own settings.

- **No discussion of limitations or failure modes.** The conclusions do not address scenarios where SINGD might underperform (e.g., very deep models, very small batch sizes, tasks where the Kronecker approximation is poor). A brief limitations paragraph would improve the paper's scientific rigor.

### Trivial
None.

## Nice-to-Haves

- A table reporting final test error (mean and std over multiple seeds), peak memory, and per-iteration time for each optimizer on at least one representative model.
- An analysis of how the exponential truncation order affects convergence and numerical stability.
- Sensitivity analysis for SINGD-specific hyperparameters (damping, truncation order).

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"SGD best for CNNs, AdamW best for transformers is an oversimplification."** This is a commonly stated practical heuristic used to motivate the paper's architecture-agnostic goal. It is not a central technical claim, and the paper does not rest any result on it as a formal statement. Not a genuine weakness.

- **"Missing comparison to Shampoo."** Per policy, missing related-work comparisons are not raised, as I cannot independently verify the appropriateness or absence of such a baseline.

- **"Missing Tables 2 and 3 (iteration cost, memory consumption)."** These tables are referenced but absent from the extracted text, almost certainly because they were in table-formatting or images that the parser stripped. The instruction is to not penalize for content stripped by the parser.

- **"Missing Theorem 1 proof."** Theorem 1 is referenced in Figure 2 (an image). The proof may reside within that figure. However, the weakness about Section 3.1 being too thin even accounting for figures is retained above as a major weakness (see Major #1), because the text should provide sufficient exposition regardless of what is in images.

- **"Central theoretical contribution [...] referenced [...] but no theorem statement, proof sketch, or equation linking IKFAC to KFAC appears in the extracted content."** — This point is partially addressed by the parser-issue note above, but the retained Major weakness #1 focuses on the core observation: the text itself is insufficiently self-contained.

- **Strength from Strength Finder: "Inverse-free KFAC update with proven equivalence"** — This conflicts with the verified weakness that the equivalence is not demonstrated in the extracted text. The strength is downgraded: the *claim* of equivalence is made, but the *proof* is not verifiable.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no insight about the paper that the paper itself does not state.

## Suggestions

1. **Move the IKFAC derivation into the main text.** Provide explicit equations showing how a specific setting of the INGD update (e.g., disabling Riemannian momentum, setting damping appropriately) recovers the KFAC preconditioner update, including the handling of exponential moving averages and damping. Even if approximate (e.g., up to first-order in β), state the relationship clearly. This is essential for the paper's first contribution to be assessable.

2. **Report at least one table of concrete experimental results in the text.** For example, give final test error (mean ± std over multiple seeds), peak memory (in MB), and iteration time (ms/step) for each optimizer on a representative model (e.g., Compact-ViT on CIFAR-100). This would allow readers to verify the claimed memory efficiency and competitive accuracy without relying solely on figures.

3. **Provide a complete pseudocode listing for SINGD** showing the full update loop (initialization of **A**, **K**, **C**; gradient computation; update of **M**; subspace projection; truncated matrix exponential; update of **μ**). A concrete algorithmic listing is worth far more than references to a missing figure.

## Score and Decision

The paper tackles a well-motivated problem and the proposed approach — structured Kronecker factors in the logarithm space — is technically interesting. However, in its current form, the paper has two critical weaknesses: (1) the central theoretical claim (IKFAC's equivalence to KFAC) is asserted but not demonstrated in the text, and (2) the experimental section lacks any quantitative results, making the empirical contribution unverifiable. These are not minor presentation issues; they prevent a reviewer from assessing the paper's core contributions. The paper would need substantial revision — specifically, adding a proper derivation of IKFAC and concrete numerical results — before it could be accepted.

**Score: 5.0** (borderline reject: promising direction but insufficiently substantiated in the presented form)

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>