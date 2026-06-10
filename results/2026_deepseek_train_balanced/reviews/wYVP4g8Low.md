## Summary

This paper proposes Local Control Networks (LCNs), which replace the uniform fixed activation function at each MLP neuron with a learnable B-spline activation—each neuron outputs a weighted sum of B-spline basis functions evaluated at its pre-activation value. The aim is to improve flexibility over standard MLPs while offering a simpler alternative to KANs. The paper claims ~5% improvement over KANs on vision tasks, ~1% over MLPs on basic ML tasks, and better computational efficiency.

## Strengths

- **Clear architectural specification.** Equation (89) precisely defines the per-neuron B-spline activation: $h_i^{(l)} = \sum_n w_{l,i,n} B_{N_l,p_l,n}(z_i^{(l)})$. This is a concrete, implementable proposal that cleanly distinguishes LCNs from KANs (which parameterize functions on edges rather than at nodes).
- **Controlled parameter comparison.** The authors standardize total parameters across LCN, MLP, and KAN and perform grid search hyperparameter tuning (Section 5.1.2), lending more credibility to the accuracy-vs-parameter curves than a comparison at arbitrary model sizes would.
- **Multi-domain evaluation scope.** Tests span basic ML tasks (4 datasets), computer vision (2 datasets), and symbolic regression—broader coverage than a single-benchmark study (Section 5.1.1).
- **Candid acknowledgment of limitations.** Section 5.2.5 explicitly notes that improvements are marginal and that simpler datasets leave little room for advantage, helping calibrate reader expectations honestly.

## Weaknesses

### Fatal
None.

### Major

- **No numerical results reported in the text.** The paper makes specific quantitative claims (LCNs outperform KANs by ~5% on vision, ~0.6% on basic ML; ~1% over MLPs on basic ML) but provides zero accuracy values, standard deviations, confidence intervals, or any numerical table anywhere in the paper. Results are described only qualitatively ("LCN consistently have higher accuracy," "slight improvements") and deferred entirely to figures (Figures 3–5). For an empirical comparison paper whose core contribution is claimed performance improvement, this is a severe evidentiary gap—readers cannot independently verify any of the paper's headline numbers, and the results cannot be quantitatively compared against future work.

- **"Mathematical analysis" does not constitute theoretical insight.** Section 3.3 presents the chain rule applied to the LCN architecture and a generic MSE loss function. There are no theorems, bounds, convergence guarantees, approximation-error results, or expressiveness analysis. The gradient expression in Equation (128) is standard backpropagation applied to this specific architecture, not a theoretical discovery. The paper is repeatedly framed as providing "theoretical findings" (abstract, Section 1, Section 3 header) but delivers only elementary calculus. This framing is misleading.

- **MLP parameter capping biases the comparison.** Section 5.2.2 states: "The number of parameters for MLPs is capped because they achieve convergence at lower parameter counts than LCNs and KANs." If MLPs plateau at lower parameter counts while LCNs/KANs continue to improve with more parameters, capping MLPs while extending the others makes the accuracy-vs-parameter curves appear to favor LCNs/KANs by construction. This is a methodological fairness concern that could reverse the paper's efficiency narrative—it may simply be that MLPs are *more* parameter-efficient, a strength the paper inadvertently obscures.

- **Missing standard baselines from related work.** The related work cites PReLU, Swish, Mish, and per-neuron heterogeneous activation methods (Hagg et al. 2017, Dushkoff & Ptucha 2016), yet none of these are included as experimental baselines. Without comparing against existing learnable-activation approaches, it is impossible to determine whether observed gains come from per-neuron B-spline diversity specifically, or from having *any* learnable activation at all.

- **Insufficient reproducibility.** The paper specifies no learning rate, optimizer, batch size, number of epochs, train/validation/test splits, grid search ranges, or architecture sizes (beyond controlled parameter counts). The specific KAN implementation version is unnamed. The MLP baseline activation function is not stated. These omissions render the experiments effectively non-reproducible.

### Minor

- **Overclaimed and imprecise phrasing.** The conclusion states LCNs "allow each neuron to dynamically select the most suitable activation function"—but the B-spline weights are learned via gradient descent and fixed after training, not dynamically selected per input. The claim that "using fixed activation functions causes every weight to be updated whenever a new data point is introduced" (Section 1) is misleading because this is true of all gradient-based learning, not specific to fixed activations.
- **Notation error in output layer.** Equation (104) gives $W^{(L+1)} \in \mathbb{R}^{O \times N_L}$, but $h^{(L)}$ is a vector of $M_L$ scalar neuron outputs, not $N_L$ (the number of B-spline bases per neuron). The dimension should be $\mathbb{R}^{O \times M_L}$.
- **No ablation isolating per-neuron diversity.** A natural baseline is an LCN variant where all neurons in a layer share the same B-spline weight vector. Without this, the paper's central selling point (per-neuron activation diversity) is experimentally untested.
- **Qualitative efficiency claims without measurement.** Sections 4.2 and 5.2 claim faster convergence, lower memory usage, and sparser computations, but no training time, inference time, FLOPs, or memory measurements are reported.

### Trivial
- Section 5.2.5 states "MLPs already achieve strong performance, leaving limited room for improvement"—this undercuts the importance of the claimed 1% improvement that the paper relies on as evidence.

## Nice-to-Haves
- Ablation study of shared vs. per-neuron B-spline weight vectors to isolate the effect of per-neuron diversity.
- Comparison against simpler learnable activation methods (PReLU, Swish) as baselines.
- Computational efficiency measurements (training time, inference speed) to support the qualitative efficiency claims.
- Sensitivity analysis for the number of B-spline bases ($N_l$) and spline degree ($p_l$).

## Removed Points
- **Harsh critic's "figures are images that I cannot view":** This is a PDF parsing artifact, not a paper flaw. The underlying criticism (no numerical results in text) is retained as a Major weakness.
- **"No code release mentioned":** Code release is not expected during anonymous submission; removed.
- **"No discussion of limitations":** Section 5.2.5 partially addresses this by acknowledging dataset simplicity limits the observed gains.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions

1. **Report complete numerical results in a table.** For every dataset and model, provide mean accuracy and standard deviation over at least 5 independent runs, with properly matched parameter counts. Without this, the paper's central empirical claims are unverifiable.
2. **Remove or substantially reframe the "mathematical analysis."** Delete Section 3.3 (standard chain rule is not a contribution) or replace with a genuine theoretical result (approximation bounds, VC dimension, or expressiveness analysis).
3. **Fix the MLP parameter capping** by either showing MLP accuracy at the same parameter ranges as LCNs/KANs, or analyzing whether the "convergence at lower parameter counts" claim holds across all datasets.
4. **Add standard learnable-activation baselines** (PReLU, Swish, Mish) to establish whether LCNs' advantage comes from per-neuron diversity or simply from having a learnable activation.
5. **Provide experimental details** (optimizer, learning rate schedule, batch size, epochs, splits) and release code for reproducibility.

## Score and Decision

The paper proposes a coherent architectural idea—per-neuron learnable B-spline activations—but fails to provide the minimal evidentiary support required for its empirical claims at a top conference. The complete absence of numerical results in the text, the misleading "theoretical analysis" framing, the comparison fairness concern from MLP parameter capping, and the absence of standard learnable-activation baselines collectively undermine the paper's central contribution. The architectural idea has genuine merit, but the submission in its current form does not meet the evidentiary standard for acceptance.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>