## Summary

This paper introduces GraphFM, a multi-graph pretraining framework that uses a Perceiver-based encoder with learned latent tokens ($K=512$) to compress graphs of varying sizes into a fixed-size shared latent space, enabling a single model to be trained across diverse graph datasets. The authors curate 152 graph datasets (80 real + 72 synthetic) spanning 7.4M nodes and 189M edges — an unprecedented scale in the multi-graph pretraining literature — and demonstrate that fine-tuning this pretrained model on held-out node classification benchmarks achieves competitive performance with individually-tuned specialist models. The paper also contributes a distributed snake-strategy sampler that yields a 5.53× training speedup.

---

## Strengths

1. **Perceiver-based architecture with latent tokens is a principled solution for variable-size graphs.** The encoder compresses arbitrary-size graphs into $K=512$ latent tokens via cross-attention, with complexity $K\cdot N_g + L\cdot K^2 \ll N_g^2$ (Section 2.1.1). This is a well-motivated architectural contribution that directly enables multi-graph pretraining across graphs with vastly different node counts — from small citation networks to large product graphs — within a single unified model.

2. **DistributedSSSampler yields a concrete 5.53× measured training speedup.** The snake-strategy distributed sampler (Section 2.2.2) pairs large and small graphs across GPUs, achieving near-100% GPU utilization. The paper reports specific timing numbers: ~56 minutes per epoch with the sampler vs. ~299 minutes without, reducing total training time from ~33 days to ~6 days on 8 A40 GPUs (line 98). This is a practical engineering contribution essential for reaching 152-dataset scale.

3. **The domain-stratification experiment (Figure 4B) cleanly demonstrates that cross-domain diversity improves OOD performance.** By fixing the model architecture at 75M parameters and varying the data composition (Social-only → Social+Biology → All including synthetic), the paper shows that adding biological data improves accuracy on *both* Coauthor-CS (citation) and Amazon-Photo (co-purchasing). This experiment is well-controlled and provides causal evidence that cross-domain pretraining, not just scale, drives generalization — a central claim of the paper.

4. **Best average rank across 10 diverse held-out datasets.** GraphFM (NFT) achieves the highest average rank among all methods on the 10-dataset benchmark (Table 1), and GraphFM (MFT) ties for second with significantly lower rank variance than NAGphormer. This demonstrates that a single pretrained model can match individually-tuned specialists across homophilic and heterophilic datasets.

5. **Rapid convergence and low variance with fixed hyperparameters.** The paper shows (Figure 5, Section 4 Q3) that GraphFM reaches near-optimal performance within 10–20 fine-tuning steps using the same learning rate and weight decay across all datasets, while 100 random configurations of GCN and NAGphormer exhibit wide performance swings. This substantiates the practical value of the pretrained initialization.

---

## Weaknesses

### Fatal
None.

### Major

1. **The scaling analysis (Figure 4A) confounds model size and data size.** The three configurations compared are: (389K params, 200K tokens) → (18M, 2M) → (75M, 7.3M). Model size and data size are simultaneously varied, making it impossible to attribute the observed 2.1% improvement to either factor individually. The paper's contribution list (line 24) claims "the first scaling analysis for multi-graph pretraining on different domains, showing that larger models pretrained on more diverse graph datasets result in better generalization," but the experiment as designed cannot separate the effects. This weakness is partially mitigated by Figure 4B (which fixes model size and varies data composition), but the headline "scaling analysis" claim about model scale specifically is not properly supported. A proper analysis should at minimum train the same model size on multiple data sizes and/or train multiple model sizes on the same data size.

### Minor

1. **No error bars or variance estimates on main results.** Table 1 and Figure 4 report accuracy and ranks without standard deviations or confidence intervals. For small datasets like Texas and Wisconsin (a few hundred nodes), variance across random splits can be substantial. Without this information, it is unclear whether the reported differences between GraphFM and baselines are statistically significant.

2. **No ablation of the Perceiver encoder architecture.** The paper attributes success to the Perceiver-based design but never compares it against a direct transformer (without latent compression) or a message-passing encoder trained on the same 152-dataset corpus. The reader cannot determine whether the architecture matters or whether any shared-encoder approach would benefit from the scale of pretraining data.

3. **The term "out-of-distribution" is used imprecisely.** The held-out datasets (Coauthor-CS, Amazon-Photos, Texas, etc.) are distinct datasets not seen during training, but they come from the *same domains* as the pretraining data (citation networks, product recommendation, webpage graphs). The paper asserts OOD generalization without quantifying distribution shift (e.g., via graphlet frequency, homophily distances, or feature-space divergence). The results are better described as "held-out dataset generalization" rather than demonstrably out-of-distribution generalization.

4. **Decoder complexity claim is not universally true.** The paper states $N_g M (K+T+1)^2 \ll N_g^2$ (line 73). With $K=512$ and $T\approx10$–$20$, $(K+T+1)^2\approx 280{,}000$. For a graph with $N_g=100{,}000$ nodes and $M=2$ decoder layers, the left side ($\approx 5.6\times 10^{10}$) exceeds $N_g^2$ ($10^{10}$). The claim holds only when $N_g \gg 280{,}000 \cdot M$, which is not qualified in the paper.

5. **No discussion of potential data leakage.** The pretraining data draws from PyTorch Geometric and Network Repository, and several held-out datasets (e.g., Coauthor-CS, Amazon-Photos) are also standard PyTorch Geometric datasets. The paper does not verify that no node or graph-level overlap exists between pretraining and test sets, which is important given the OOD framing.

6. **Supervised pretraining (per-dataset linear classifiers $\mathbf{W}_g$) requires labeled data for all 152 datasets.** The paper uses multi-task supervised learning, not self-supervised learning. This is a practical limitation: curating labeled data at this scale is expensive, and the approach cannot leverage unlabeled graphs. The "foundation model" narrative in the paper implicitly borrows from LLM-style pretraining (which is typically self-supervised), but the actual methodology is supervised multi-task learning — a distinction the paper does not discuss or justify.

### Trivial

1. Text truncation artifacts: line 114 reads "163.1 for a detailed description" and line 116 begins with "4)" — garbled text likely from a broken cross-reference or parser issue.
2. Edge count discrepancy: the abstract reports 189M edges, while the datasets section (line 114) suggests approximately 163M (the text is truncated, making the exact number unclear).

---

## Nice-to-Haves

- An analysis of what the latent tokens learn (e.g., do specific latent tokens consistently activate for structural patterns like triangles, hubs, or bridges?). This would substantiate the "shared vocabulary" claim.
- Comparing a baseline architecture (e.g., GCN or NAGphormer) under the *same* pretrain-then-fine-tune paradigm, to disentangle whether GraphFM's advantage comes from the architecture, the pretraining data, or both.
- Quantifying the distribution shift between pretraining and held-out datasets (e.g., homophily ratio distances, degree distribution divergences) to justify the "OOD" terminology.

---

## Removed Points

*These points were flagged by reviewers but removed after verification against the paper. Treat them with caution if referenced elsewhere.*

- **"Generalist vs. specialist comparison is unfair"** — Removed. The comparison is standard for transfer learning papers: a pretrained model is compared against per-dataset baselines trained from scratch. The paper's claim is that a single generalist model achieves competitive results with individually-tuned specialists, which is precisely what this comparison tests.
- **"Per-dataset MLP$_g$ details insufficient"** — Removed. The paper states (line 40) that MLP$_g$ projects node features from each graph's original dimensionality to the common embedding dimension. This is adequate description for a paper of this scope.
- **"Synthetic graphs not described"** — Removed. The paper cites Tsitsulin et al. and notes the synthetic graphs add heterophilic examples. The reference provides the generation procedure; full reproduction in the main text is unnecessary.
- **"Table 1 not readable in text"** — Removed. The table is embedded as an image; this is a PDF parsing artifact, not a paper flaw.
- **"Two different optimizers used for pretraining and fine-tuning"** — Removed. Using different optimizers for different training phases is standard practice (LAMB for large-scale pretraining, AdamW for fine-tuning). The paper transparently reports both.

---

## Novel Insights

The most novel observation from the combined reviews is the structural weakness in the scaling analysis: the paper claims to study the effect of "scale" but simultaneously varies model size and data size in Figure 4A. However, the domain-stratification experiment (Figure 4B) — which *does* properly control model size — provides a clean, separate demonstration that cross-domain diversity improves OOD performance. This means the paper's core claim about cross-domain pretraining is supported, but the specific claim about model scaling requires additional experiments. The reviews also surface an interesting tension: the paper's strengths (large-scale pretraining, distributed sampler, competitive benchmark results) are largely empirical and engineering-driven, while the evaluation methodology (no error bars, no ablations, no distribution shift quantification) does not match the rigor expected for a "scaling analysis" contribution. This suggests the paper would benefit from repositioning its contributions away from the scaling-law narrative and toward the empirical demonstration that multi-domain pretraining + fine-tuning works.

---

## Suggestions

1. **Unconfound the scaling analysis.** At minimum, train the 75M model on 200K and 2M token subsets, and train the 389K model on 2M and 7.3M subsets. This would disentangle model capacity from data volume and allow the paper to properly support its scaling claims.
2. **Add error bars to main results.** Report mean and standard deviation over at least 3–5 random seed runs for Table 1 and Figure 4, particularly for the smaller datasets (Texas, Wisconsin, Actor) where variance is expected to be high.
3. **Include an ablation of the Perceiver encoder.** Compare against a variant with a standard transformer (same parameter count, no latent compression) or a GCN-based encoder trained on the same data, to isolate the contribution of the architecture.
4. **Quantify distribution shift** between pretraining and held-out datasets (e.g., using homophily ratio distributions, degree distributions, graphlet frequency vectors) to substantiate or replace the "OOD" claim with more precise language.
5. **Verify and disclose data leakage.** State explicitly whether any nodes or graphs from the held-out datasets overlap with the pretraining corpus.

---

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>