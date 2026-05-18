Now I have all the information I need. Let me write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper proposes In-Context Risk Minimization (ICRM), a framework that bridges domain generalization (DG) and in-context learning. The central idea is to treat unlabeled test-time examples arriving sequentially from a test environment as "context" for a next-token predictor, allowing the model to dynamically "zoom in" on the test environment risk minimizer. The paper provides theoretical guarantees for this approach and demonstrates strong empirical results across four image classification benchmarks (FEMNIST, Rotated MNIST, WILDS Camelyon17, Tiny ImageNet-C).

## Strengths

- **Novel conceptual bridge between DG and ICL.** The paper cleanly draws the parallel between "environment" in domain generalization and "context" in next-token prediction, proposing a framework that goes beyond the two existing DG paradigms (invariance and marginal transfer). This reframing is genuinely insightful and opens a new direction for the field.

- **Consistent and substantial empirical gains.** Table 1 shows ICRM outperforming ERM, ARM, and TENT on all four benchmarks at non-zero context sizes, often by large margins (e.g., on Tiny ImageNet-C with 25 context samples, ICRM achieves 19.2% worst-case accuracy vs. ERM's 9.5% and TENT's 1.2%). These results are consistent across diverse benchmarks spanning different types of distribution shift (writer identity, rotation, hospital style, image corruptions).

- **Theoretical guarantees for the zoom-in effect.** Theorems 1–3 provide formal proofs that in-context conditioning converges to the environment-specific risk minimizer (with full context), improves monotonically with context length, and can generalize OOD under Gaussian latent assumptions. While idealized, these results provide a formal foundation that many empirical DG papers lack.

- **Controlled ablations to isolate the in-context mechanism.** The paper introduces ERM$^+$ and ARM$^+$ (same transformer backbone, different context usage) to show that the transformer architecture alone is not responsible for the gains. The ICRM-Mix ablation (Table 2) demonstrates that environment-specific context matters on FEMNIST and Rotated MNIST, supporting the thesis that context functions as environment.

- **Attention visualizations show the amortization function at work.** Figure 4 provides qualitative evidence that ICRM learns to attend to semantically relevant features in context (curved arcs for digit queries, same-class images, semantically related categories). This goes beyond aggregate metrics to illustrate the mechanism.

## Weaknesses

### Fatal
None.

### Major

- **The framing is misleading regarding the evaluation setting and the "bitter lesson" of DG.** The abstract and introduction invoke the well-known finding that no DG algorithm outperforms ERM on DomainBed benchmarks, and present ICRM as an answer to this failure. However, the evaluation uses a sequential test-time protocol where the model accesses a stream of unlabeled test samples from the target environment as context — this is fundamentally different from the standard DG evaluation (i.i.d. test points, no access to other test samples). ERM is evaluated without this advantage, making the comparison asymmetric. The paper does clearly describe its test protocol in Section 3, but the broad framing in the abstract and introduction is likely to mislead readers into thinking ICRM solves the standard DG problem. The authors should clearly delimit their setting upfront and discuss its practical relevance.

- **Large gains at zero test context are not explained by the paper's core theoretical narrative and suggest the training procedure itself is a major driver of performance.** On Camelyon17, ICRM with *no* test context achieves 92.0% vs. ERM's 68.6% — a 23.4% gap. On Tiny ImageNet-C: 38.3% vs. 31.8%. The paper attributes this (line 430) to the training regimen producing "a better featurizer," but the theoretical results (Theorems 1–3) all describe the benefit of test-time context, not gains from the autoregressive training procedure alone. The ERM$^+$ ablation (same transformer, no context) performs worse (50.1% on Camelyon17), confirming that ICRM's training objective is a major source of improvement. The paper does not isolate the contribution of test-time context from the training procedure, making it impossible to attribute the full gains to the claimed "zoom-in" effect. An experiment with *random* (non-informative) test context would clarify whether context per se drives the improvement.

- **Architecture control baselines are inconclusive due to poor performance on key datasets, raising tuning concerns.** On Camelyon17, ERM$^+$ (transformer, no context) achieves only 50.1% vs. ERM's 68.6% (convnet). On Tiny ImageNet-C, ARM$^+$ achieves just 5.5% vs. ARM's 30.8%. These large performance drops suggest the transformer backbone was not properly tuned or initialized for standard training on these datasets, rather than reflecting a fundamental architectural limitation. This makes the architecture ablation difficult to interpret: ICRM's advantage may partly reflect recovering from an architecture-induced deficit rather than a genuine in-context adaptation advantage. The paper needs to demonstrate that the transformer baselines received adequate hyperparameter tuning, or use a different control (e.g., a non-autoregressive sequence objective) to separate the effect of sequence training from attention over context.

### Minor

- **Standard deviations and statistical reliability.** The main results (Table 1) report "average across three independent runs" but no standard deviations are shown in the table (they are mentioned in text but not displayed). DomainBed protocols typically use 10–20 seeds. Three seeds with no visible variance measures raise concerns about result reliability.

- **ICRM-Mix results weaken the environment-specific context claim.** On Camelyon17 and Tiny ImageNet-C, ICRM and ICRM-Mix perform nearly identically (e.g., 92.0% vs. 92.9% at 0 context on Camelyon17). The paper's post-hoc explanation (classes distributed uniformly across domains) is reasonable but not empirically tested. This weakens the claim that ICRM's success derives primarily from extracting environment-specific information from context — on these datasets, simple within-class similarity suffices.

- **Theory-experiment gap.** The theoretical results (Gaussian latents, identity mapping, infinite context assumptions, Voronoi cell conditions) are far removed from the experimental setting (image classification with CNNs+transformers). The theory is not used to predict or interpret any experimental outcome. While this does not invalidate either the theory or the experiments, it limits the value of the theory in supporting the core claims.

- **Missing comparison with standard test-time adaptation methods.** Given the sequential test-time setting where models access unlabeled test samples, comparisons with methods like Test-Time Training (TTT), online entropy minimization, or gradient-based adaptation on test inputs would be informative. The paper compares with TENT but not with other online adaptation methods.

- **Computational cost not discussed.** The transformer decoder processes all context examples with quadratic attention. The paper does not discuss the practical scaling of this approach for long context streams or provide timing comparisons.

### Trivial
None.

## Nice-to-Haves
- An experiment with *random* (non-informative) test context (e.g., shuffling the test sequence or replacing it with data from a different environment) would cleanly isolate the effect of test-time context from the training procedure.
- Reporting results under the standard i.i.d. DG protocol (single test points, no context) after sequence training would clarify whether training procedure alone yields better OOD features — the 0-context results in Table 1 already partially address this, but a true i.i.d. evaluation without sequential structure would be cleaner.
- A non-autoregressive sequence training baseline (predicting each label with access to all other examples in the sequence but without causal masking) would help separate the effect of the autoregressive objective from the effect of context.
- Synthetic experiments matching the theory's assumptions (Gaussian latents, known environment parameters) would demonstrate the predicted monotonic improvement and connect theory to experiments.

## Removed Points
- *Criticism about missing appendix/proofs* — The parser strips these sections; they exist in the original submission.
- *Criticism about "not yet released" code/models* — Per guidelines, cited resources are assumed to exist.
- *Formatting/style nitpicks* — These reflect parser artifacts, not author errors.
- *Request for larger datasets or more models* — The benchmark suite is already diverse and sufficient for the paper's claims.

## Novel Insights
None beyond the paper's own contributions. The key insight — treating environment as context for next-token prediction — is the paper's own contribution, and the reviews do not add a new observation beyond it.

## Suggestions
1. **Reframe the paper to clearly state the evaluation setting upfront** — explicitly say that ICRM operates in a sequential test-time setting with access to unlabeled samples from the test environment, and discuss the practical relevance of this setting. Do not invoke the "bitter lesson" of standard DG without this caveat.
2. **Isolate the contribution of test-time context** by comparing ICRM with a version evaluated on random/non-informative context. If gains persist, the focus should shift to explaining why sequence training itself improves features.
3. **Revisit the ERM$^+$/ARM$^+$ baselines** with proper hyperparameter tuning for the transformer backbone on all datasets, or replace them with a more informative control (e.g., a non-autoregressive sequence objective).
4. **Report standard deviations** in the main table and increase the number of seeds to at least 5–10 for the primary results.
5. **Add basic TTA baselines** (online adaptation methods) to situate ICRM in the broader test-time adaptation literature.

## Score and Decision

**Calibration anchors used:**
- **TPZRq4FALB.md** (avg 8.0, TTA with multi-modal reliability bias) — Stronger execution, cleaner experiments, but less conceptual novelty than the current paper.
- **yOhNLIqTEF.md** (avg 6.67, ICL generalization study) — Comparable in scope; the current paper has more conceptual novelty but messier experimentation.
- **TD3SGJfBC7.md** (avg 6.25, Few-shot TTA with CLIP) — Similar tier; the current paper has stronger theoretical backing and greater conceptual novelty but more significant experimental confounds.
- **Rc3RP9OoEJ.md** (avg 5.0, In-context prompt learning) — The current paper is substantially stronger in theory, experimental breadth, and conceptual clarity.
- **ZbOSRZ0JXH.md** (avg 3.0, Data-free DG with LLMs) — The current paper is far stronger across all dimensions.

The paper presents a genuinely novel conceptual contribution and strong empirical results across diverse benchmarks. However, the misleading framing regarding the evaluation protocol, the failure to isolate the effect of test-time context from the training procedure (with large 0-context gains unexplained by the theory), and inconclusive architecture controls are significant weaknesses that prevent this from being a top-tier contribution in its current form. The core idea is promising and the empirical results are substantial, but the experimental evidence does not fully support the central narrative about "zooming in" via test-time context.

**Score:** 6.0

**Decision:** Reject

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>