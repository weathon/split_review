- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6
Now I have all the information I need. Let me compile the final consolidated review.

## Summary

This paper proposes CoST, a framework for graph reasoning that alternately trains a Graph Neural Network (GNN) and a Pre-trained Language Model (PLM) guided by a variational objective. The key idea is to avoid the computational burden of joint GNN+PLM optimization by introducing a text-only variational distribution $q_\theta$ and treating the alternating updates as optimizing an evidence lower bound. Experiments are reported on nine benchmark datasets spanning homogeneous and heterogeneous graphs, with claims of state-of-the-art results across all of them.

## Strengths

- **Broad and systematic evaluation across diverse benchmarks.** The paper evaluates on six homogeneous graph datasets (AmazonSports, AmazonClothing, MAGGeology, MAGMath, CitationV8, GoodReads) and three heterogeneous graph datasets (FB15k237, WN18RR, Wikidata5M), covering different graph sizes and modalities. Results for both GNN-based and text-based baselines are reported, and the pretrained GNN model within CoST serves as an internal control — the "blue" indicators in the tables mark improvement from alternating training over the pretrained baseline, providing a direct test of the paper's core claim.

- **Architecture-agnostic improvement.** Ablation experiments (Figure 3a) apply CoST's alternating training on top of three different GNN backbones (RGCN, CompGCN, NBFNet) on FB15k237 and WN18RR, showing consistent improvements across architectures. This demonstrates that the alternating framework is not tied to a specific GNN design.

- **Convergence evidence for the alternating scheme.** Figure 3b empirically shows that the alternating optimization converges to high performance within a small number of update steps on two datasets. This is important because alternating training schemes can be unstable or slow to converge, and the paper provides direct evidence to the contrary.

## Weaknesses

### Fatal
None.

### Major

- **Undefined term $\mathcal{O}(\theta^2)$ in Theorem 2.1 (Equation 6).** The core theoretical result — Theorem 2.1 — contains the term $+\mathcal{O}(\theta^{2})$ that is never defined, derived, or explained in the paper. The theorem claims "optimizing the objective function $O(\phi)$ in Equation (3) is equivalent to optimizing" the expression in Equation (6), but this term makes the claimed equivalence ambiguous. Is $\mathcal{O}(\theta^2)$ a residual/approximation error (big-O notation), a separate objective term, or a typographical error? A reader cannot determine whether the theorem states an exact equivalence or an approximate one, and the distinction matters for the theoretical grounding of the entire framework. This is not a parser artifact — the term appears in the extracted equation on line 91 and is never clarified in the surrounding text.

- **Gap between variational derivation and implemented loss functions.** The paper motivates PLM optimization by minimizing $D_{\mathrm{KL}}(q_\theta || p_\phi)$ (Section 2.3.1, line 104), then abruptly replaces this with "hard pseudo targets" sampled from $p_\phi$ and a contrastive loss (Equation 9). The justification is a single sentence: "We can alternatively optimize the PLM model with the utilization of hard pseudo target produced by the GNN model" (line 114). The leap from minimizing KL divergence to multinomial sampling + contrastive learning is not explained — no derivation shows why the contrastive loss approximates the KL objective, nor is there a citation making this connection. Similarly, the GNN optimization (Section 2.3.2) jumps from maximizing the ELBO to sampling from $q_\theta$ and using Equation (12) without showing how the sampling-based loss relates to the ELBO. These gaps make the theoretical framework feel disconnected from the actual algorithm.

### Minor

- **Hyperparameters $\gamma,\tau$ introduced but neither defined nor reported.** These appear on line 149 controlling "different term weights" in the GNN objective (Equation 12), but their values are never stated for any dataset, and no sensitivity analysis is provided.

- **No runtime, memory, or scalability analysis despite scalability being a core motivation.** The paper repeatedly motivates alternating training by citing "the immense scale of real-world graphs" (lines 19, 57) as the obstacle to joint training, yet provides no comparison of training time, memory usage, or convergence speed against either joint-training baselines or single-modality methods. The largest dataset (Wikidata5M) is mentioned but no runtime numbers are given. The claim that alternating training "alleviates" scalability challenges is left unquantified.

- **Multinomial sampling over the full candidate set is unaddressed.** Equations (8) and (11) define multinomial distributions over $H_{(h,r)}$, which the paper defines as $\mathcal{V}_{/O_{(h,r)}}$ — i.e., all nodes except observed answers. On graphs with millions of nodes (e.g., Wikidata5M), this sampling step would be computationally prohibitive. The paper does not discuss whether negative sampling, subsampling, or approximation strategies are used, nor how this is made tractable in practice.

- **No error bars or statistical significance.** All reported results appear as point estimates with no indication of variance across runs. This is a concern especially for smaller datasets (e.g., AmazonSports with 1,820 nodes reported in Table 1). Without error bars, it is difficult to assess whether the reported improvements are statistically reliable.

- **Several notations are used without definition.** The operator $\mathcal{E}_{/\{(h,r,\hat{t})\}_{\hat{t}\in O_{(h,r)}}}$ appears in Equations (3), (6), and elsewhere but is never explicitly explained. The sets $O_{(h,r)}$ and $H_{(h,r)}$ are defined but their sizes in the experimental datasets are not reported, making the scaling discussion harder to ground.

- **Generic conclusion with no limitations or future work.** Section 5 is a single paragraph that restates the contribution without discussing any limitations of the approach, failure cases, or directions for future work.

### Trivial
None.

## Nice-to-Haves

- Provide a direct comparison between CoST and a "naive joint training" baseline (fine-tuning GNN+PLM end-to-end, even if only on a small dataset) to quantify the computational savings and performance difference that motivated the alternating design.
- Report hyperparameter values ($\gamma,\tau$) and include a sensitivity analysis.
- Clarify how the multinomial sampling in Equations (8) and (11) is implemented at scale (negative sampling? top-k truncation?).

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Section 2.3.2 truncated / Equation (12) missing"** — The text at line 104 ("which is equiv") is a parser truncation (the sentence continues after an inline image). Equation (12) is rendered as an image in the PDF (line 147) that was not extracted as text; it exists in the original submission. Both are parser artifacts, not author errors.

2. **"Experimental results not verifiable (tables garbled)"** — Tables 2–5 and Figure 3 are embedded as images in the PDF; the extracted text cannot display their contents. These are parser artifacts. The original submission contains the complete tables with numerical results.

3. **"Missing proof for Theorem 2.1"** — Proofs deferred to an appendix are standard in ML conference papers. The paper's main text states the theorem and explains the alternating optimization intuition. The absence of a full proof in the main text is not a flaw.

4. **"Baseline unfairness: structure-based methods may not use text"** — The paper explicitly states that for homogeneous graphs, "GNN-based methods [use] the embeddings produced by BERT following original papers" (line 166–167). For heterogeneous graphs, the pretrained GNN model within CoST serves as the controlled baseline that isolates the effect of alternating training (blue indicators). The comparison against structure-only baselines is standard practice.

5. **"Not specifying what makes scale an obstacle (memory, compute, gradient instability?)"** — While this could be more precise, the paper's high-level framing ("the scale of real-world graphs, characterized by a large number of nodes, relations, and edges") is a reasonable motivation for an alternating approach. This is a presentation preference, not a substantive weakness.

6. **"Multinomial denominator in Equation (9) is pointwise, not ranking"** — The loss in Equation (9) contrasts one positive against multiple negatives, which is a standard contrastive / pairwise ranking loss (InfoNCE-style). The criticism misunderstands the loss formulation.

## Novel Insights

Neither reviewer fully captures a tension at the heart of the paper: the variational motivation posits $q_\theta$ as a text-only distribution approximating the GNN's posterior $p_\phi$, yet the actual PLM optimization (Equation 9) is a contrastive loss over pseudo targets sampled from $p_\phi$. This is more reminiscent of self-distillation or co-training than standard variational inference — the PLM is learning to imitate the GNN's predictions using text alone, while the GNN learns from the PLM's text-conditioned samples. The paper would benefit from positioning CoST in this light rather than framing the alternating updates strictly as ELBO optimization with pseudo-code, because the gap between the variational theory and the implemented losses is wider than acknowledged.

## Suggestions

1. **Clarify Theorem 2.1 and $\mathcal{O}(\theta^2)$.** Define what $\mathcal{O}(\theta^2)$ means in Equation (6) explicitly. If it denotes higher-order terms from a Taylor expansion or a constant, say so. If it is a different objective, rename it to avoid confusion with big-O notation.

2. **Bridge the theory–practice gap.** Add a paragraph explaining how the contrastive loss in Equation (9) follows from the KL minimization objective (Equation 7) when using hard pseudo targets, or cite prior work that establishes this connection (e.g., knowledge distillation methods).

3. **Report hyperparameters across datasets.** At minimum, provide the values of $\gamma$ and $\tau$ for all datasets in a table.

4. **Add a scalability section.** Report training time per epoch, memory usage, and number of alternating steps for at least one large dataset (e.g., Wikidata5M). This directly validates the paper's central motivation.

5. **Add error bars or multi-run statistics.** Report means and standard deviations over at least 3 random seeds for the main results (Tables 2–5).

6. **Discuss how negative sampling is handled.** Clarify whether the multinomial distributions in Equations (8) and (11) are over the full node set or a subsample, and if the latter, describe the sampling strategy.
