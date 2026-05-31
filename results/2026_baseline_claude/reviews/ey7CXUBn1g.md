## Summary

AdaSVD proposes two adaptive components for SVD-based LLM compression: (1) **adaComp**, which minimizes post-truncation reconstruction error by alternately updating the singular matrices $\mathcal{U}_k^\sigma$ and $\mathcal{V}_k^\sigma$ via the Moore-Penrose pseudoinverse (reformulated as a Least Squares Estimation problem), together with a "stack-of-batch" trick to exploit more calibration data within fixed GPU memory; and (2) **adaCR**, which assigns layer-specific compression ratios using a cosine-similarity-based importance score linearly interpolated between a minimum and target retention ratio. Experiments on LLaMA2-7B, OPT-6.7B, Mistral-7B, Vicuna-7B, and LLaVA show consistent perplexity/accuracy improvements over vanilla SVD, FWSVD, ASVD, and SVD-LLM across compression ratios from 40% to 80%.

---

## Strengths

- **Technically sound core method.** adaComp's reformulation of the bilinear optimization as alternating LSE problems with Moore-Penrose pseudoinverse is principled and demonstrably more stable than direct matrix inversion (evidenced by the smooth convergence curve in Figure 3a vs. the unstable direct approach).
- **Consistent empirical gains.** Table 1 shows AdaSVD improving WikiText-2 perplexity over SVD-LLM across all 5 tested compression ratios (40%–80%) on LLaMA2-7B, with especially large margins at 60%+ compression. Table 2 confirms generalization across four model families.
- **Comprehensive ablation.** Tables 3a–3d separately validate adaComp, adaCR, number of iterations, and mrr sensitivity, giving clear attribution of each design choice.
- **Practical orthogonality.** Table 4 shows AdaSVD + GPTQ-INT4 outperforms SVD-LLM at high compression, confirming the method composes well with quantization.
- **VLM extension.** Figure 5 demonstrates applicability to LLaVA, broadening the contribution beyond decoder-only models.

---

## Weaknesses

### Fatal
None.

### Major

1. **No latency or throughput analysis.** The paper's core motivation is deployment on resource-constrained devices, and SVD compression's practical value hinges on actual inference speedup—not just parameter count reduction. The two-matrix multiplication $\mathcal{U}_k^\sigma (\mathcal{V}_k^\sigma)^\top \mathcal{X}$ can be slower than the original matrix-vector product at low-to-moderate rank ratios due to memory access patterns and kernel overhead. The paper reports no wall-clock latency, FLOPs, or throughput numbers, making it impossible to verify the deployment claims.

2. **Thin algorithmic novelty.** adaComp is essentially classical alternating least squares (ALS) for bilinear matrix factorization, a technique with decades of history in collaborative filtering and NMF. Applying it post-SVD with a Moore-Penrose solve is a natural engineering step rather than a novel algorithmic contribution. The paper does not differentiate its formulation from standard ALS or discuss what, if anything, makes this setting fundamentally different from prior ALS literature.

3. **Limited model scale.** All experiments are conducted on ≈7B-parameter models. At these scales, the Graham-Schmidt-like SVD updates and pseudoinverse solves are tractable, but it is unclear whether adaComp's per-layer alternating solve is computationally feasible for 70B+ models, which are a primary target of LLM compression research.

4. **No cross-paradigm comparison at equivalent memory.** A 60% SVD compression reduces parameter count to 40% of the original. INT4 quantization also reaches ≈25% memory. The paper never contextualizes SVD-based compression against quantization or structured pruning at matched memory budgets, making it difficult for practitioners to assess when AdaSVD is the right tool.

### Minor

1. **adaCR formula is ad hoc.** Equation (19), $\text{CR}(\mathcal{W}) = mrr + \mathcal{I}_n(\mathcal{W}) \cdot (trr - mrr)$, is a linear interpolation with no theoretical justification for why a linear mapping from normalized cosine similarity to retention ratio is optimal. The mrr hyperparameter also requires tuning (Table 3d), and guidance for setting it is absent.

2. **Stack-of-batch aggregation.** Averaging activations across samples collapses distributional information. Other aggregations (e.g., concatenation with random subsampling, PCA reduction) are not explored or compared, and there is no theoretical argument for why the mean is the correct sufficient statistic for the LSE objective.

3. **Overfitting at low compression with multiple iterations.** Table 3c shows that going from 1 to 3 iterations degrades performance at 40% compression, and the paper attributes this to overfitting with 256 calibration samples. No adaptive early-stopping criterion is proposed; the practitioner must guess the right iteration count per compression ratio.

### Trivial
- Equation (7) for the update of $\mathcal{V}_k^\sigma$ does not involve $\mathcal{X}$ explicitly—the final closed form in Eq. (13) appears to simplify away the input distribution, which seems inconsistent with the activation-aware motivation. A brief clarification would help.

---

## Nice-to-Haves

- Report actual inference latency (ms/token) on the target hardware (e.g., A100 for fair comparison, or an edge GPU/mobile SoC for the deployment scenario) alongside perplexity.
- Evaluate on at least one larger model (e.g., LLaMA-2-13B or LLaMA-3-8B) to probe computational scalability of the alternating pseudoinverse solves.
- Provide convergence guarantees or a bound on the number of iterations needed for adaComp to reach ε-optimality.
- Explore non-linear mappings for adaCR (e.g., softmax-based allocation) and compare to the linear scheme.

---

## Novel Insights

The paper's most practically useful observation is that post-truncation error compensation via alternating pseudoinverse updates is significantly more stable and effective than the direct closed-form update that involves a regular matrix inverse—a distinction that is easy to overlook but empirically impactful (Figure 3a). The stack-of-batch aggregation, while simple, offers a transferable trick for calibration-constrained post-training compression workflows. The bowl-shaped importance profile of LLaMA layers (Figure 4) is an interesting empirical finding, supporting allocating higher rank to early and late layers, consistent with observations in the pruning literature.

---

## Suggestions

- Include an end-to-end wall-clock benchmark (compression time + inference latency) vs. SVD-LLM, ASVD, and an INT4 quantization baseline at equivalent memory to substantiate the deployment motivation.
- Clarify the relationship between adaComp and classical ALS, and explicitly position the contribution relative to that literature.
- Add an experiment with LLaMA-2-13B or LLaMA-3-8B to demonstrate scalability.
- Provide a practical rule (or sensitivity analysis) for selecting mrr and the number of iterations jointly, rather than treating them as independent hyperparameters.
- Report the actual runtime overhead of adaComp (compression time in minutes) vs. baselines to help practitioners weigh the quality-cost tradeoff.

---

## Score and Decision

AdaSVD presents genuine, reproducible improvements over existing SVD-based LLM compression methods, backed by comprehensive ablation studies and multi-model evaluation. The alternating pseudoinverse approach is technically sound and pragmatically useful. However, the core algorithmic ideas (alternating least squares, importance-based adaptive allocation) are not novel at the level expected at ICLR, and the absence of latency data leaves the paper's central practical claim—suitability for resource-constrained deployment—unsupported. The limited model scale (all ≤7B) and missing cross-paradigm baselines further constrain the paper's impact.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>