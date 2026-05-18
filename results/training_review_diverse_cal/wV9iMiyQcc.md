Now I have all the information I need. Let me synthesize the final review.

---

## Summary

RotPruner introduces a conceptually clean idea: instead of pruning LLMs in the original weight space, learn orthonormal rotation matrices that transform weights and activations into a space with more pronounced outliers, then apply standard pruning methods (Wanda, SparseGPT) in that rotated space. The approach is evaluated on OPT, LLaMA-2, and LLaMA-3 across unstructured, 2:4 semi-structured, and structured sparsity, consistently outperforming the one-shot baselines by modest but visible margins (0.1–0.5 perplexity). The paper also demonstrates that the overhead of the extra rotation multiplications is negligible (~1.006×).

---

## Strengths

1. **Novel and principled motivation for the rotation.** Section 3.1 provides a concrete 2×2 example where pruning in the original space always causes error, but a specific orthogonal transformation makes the pruning exact (zero loss). This cleanly demonstrates that the original weight space can be suboptimal for pruning and that a better rotation exists — a simple but effective pedagogical argument.

2. **Consistent empirical gains across models, sizes, and sparsity patterns.** Table 2 shows RotPruner outperforms SparseGPT and Wanda on all reported model×sparsity combinations (OPT 125M–6.7B, LLaMA-2-7B, LLaMA-3-8B). For example, LLaMA-2-7B at 50% unstructured sparsity improves from 7.72 (SparseGPT) to 7.51. This breadth directly supports the claim that rotating the space is beneficial across diverse model families.

3. **Critical controlled comparison: learned rotation beats random rotation.** Table 1 reports that applying Wanda in a learned rotated space on OPT-125M achieves perplexity 35.02, while a random rotated space yields 40.54 — worse than the original space (37.99). This confirms that the benefit comes from the learned rotation specifically, not from any arbitrary transformation.

4. **Comprehensive ablation study.** Tables 5–9 systematically test training loss composition (auto-regression + cosine best), STE variants (SR-STE best), optimization method (Cayley SGD > Cayley Adam), calibration set size (128 sufficient), number of Q matrices (performance degrades gracefully), and compatibility with different base pruners (magnitude, Wanda, SparseGPT). This builds confidence in the design choices.

5. **Inference overhead is quantified and shown to be small.** Table 4 measures per-layer latency on a single LLaMA layer and reports only 1.006× slowdown with attention residual rotation, dropping to 1.003× with parameter sharing. This addresses a practical concern that could otherwise undermine the method's usefulness.

6. **Interesting artifact at low sparsity.** Figure 4 shows that RotPruner's pruned OPT-1.3B achieves lower perplexity than the dense model at sparsity ratios below 50%, an observation not reported by prior one-shot methods. While not fully explained, this is a noteworthy empirical finding.

---

## Weaknesses

### Fatal
None.

### Major

1. **No comparison with training-based pruning methods that use similar data budgets.** RotPruner is described as a "training-based pruning framework" (abstract, introduction) and optimizes rotation matrices over multiple epochs with calibration data. Yet the baselines are exclusively one-shot methods (SparseGPT, Wanda, SliceGPT). The paper discusses ADMM-pruner and FISTAPruner in Section 2.2 — methods that also use a small calibration set and update model weights — but provides no experimental comparison. The ablation in Table 1 (learned vs. random rotation) partially addresses the concern that the gains come from training rather than rotation, but it does not fully isolate the effect because the random rotation baseline is untrained. A comparison against a training-based method operating in the original space (even a simplified one) would tell the reader whether the rotation itself or merely having multiple gradient steps drives the improvement. *Why it matters*: this is the most significant gap in experimental design; it weakens the ability to attribute the gains to the paper's central claim (rotation) rather than to the training procedure.

2. **No statistical significance or variance reporting.** The reported improvements are modest (0.1–0.4 perplexity, 1–2 percentage points in zero-shot accuracy). The paper reports a single run per setting with no standard deviations, confidence intervals, or inter-run variance. Given the stochastic elements (Cayley SGD, STE-based mask updates) and the small calibration set (128 samples), it is unclear whether the observed gains are robust or fall within evaluation noise. The claim that "pruned OPT-6.7B can outperform the dense model" is striking but (a) the dense perplexity for OPT-6.7B is not shown alongside in Table 2, and (b) without error bars, one cannot assess whether this is a reliable effect or a single-seed artifact. *Why it matters*: variance reporting is necessary to establish that the improvements are real and reproducible, especially when gains are small.

### Minor

1. **Number of Q matrices used in main experiments is not specified.** The ablation in Table 8 studies how varying the number of Q matrices affects performance, but the main results (Tables 2, 3) do not state how many Q matrices were used for each model. Since this parameter directly affects both performance and computational cost, omitting it leaves the experimental setup incompletely defined and harms reproducibility. The paper says "for LLMs with larger scale, we suggest to use less number of Qs" but does not disclose the actual configuration.

2. **Inference speed is measured only on a single layer, not end-to-end.** Table 4 benchmarks a single LLaMA layer with 2:4 sparsity. While the per-layer overhead is small, the cumulative effect of residual rotations across all decoder layers is not reported. For structured pruning in particular, where RotPruner adds rotation matrices on the residual stream, end-to-end latency or throughput numbers would be more informative for practitioners evaluating the method's practical value.

3. **Dense perplexity for OPT-6.7B is not explicitly shown alongside the claim.** The paper states that "the pruned OPT-6.7B can outperform the dense model" (Section 4.1.1), but the dense perplexity value for that model is not reported in Table 2. Figure 4 provides the dense baseline for OPT-1.3B, so the same treatment should be given to the OPT-6.7B claim. Without seeing the dense number, the reader cannot evaluate how meaningful the "outperforms" claim is.

4. **Structured sparsity comparison with SliceGPT could be clarified.** The paper reports "30% structured sparsity" for both methods, but SliceGPT removes principal components (reducing hidden dimension), while RotPruner prunes bottom rows/columns of weight matrices. The paper states "we hold the same setting of structured pruning as SliceGPT" and initializes Q matrices via SliceGPT's PCA, but it is not spelled out whether 30% sparsity in RotPruner corresponds to the same effective parameter/FLOP reduction as SliceGPT's dimension reduction. A brief clarification of how the sparsity budgets are matched would strengthen the comparison.

### Trivial

None.

---

## Nice-to-Haves

- **Analysis of the learned rotation matrices.** The paper motivates rotation via the "outlierness" intuition (Figure 2) but does not analyze the learned Q matrices (e.g., their similarity to activation SVD, spectral properties, or which dimensions get emphasized). Such analysis would turn the outlier intuition into concrete evidence and help the community understand what constitutes a good pruning space. This is a natural follow-up that would deepen the contribution but is not required to validate the current claims.
- **Discussion of sensitivity to calibration data.** The ablation in Figure 5 shows RotPruner is more sensitive to calibration set size than baselines, but the paper does not explore why. A brief comment on whether this sensitivity stems from training the Q matrices or the mask updates would be useful.
- **Theoretical analysis connecting rotation to the pruning objective.** The motivation in Section 3.1 is heuristic (toy 2×2 followed by the L₁ norm argument). A formal link between the learned rotation and the pruning loss being minimized would strengthen the paper, but the existing motivation is acceptable for an empirical systems paper.

---

## Removed Points

- **Criticism about theoretical motivation being "incomplete."** The harsh critic argued the theoretical motivation is heuristic and not formally connected to the optimization objective. This is a reasonable observation but reflects expectations more appropriate for a theory paper than an empirical systems paper. The paper provides a concrete toy example, an intuitive outlier-based motivation, and empirical validation. Moved to Nice-to-Haves above.

---

## Novel Insights

Beyond the paper's own contributions, the most interesting synthesized observation is that the value of the 2×2 toy example in Section 3.1 is not just pedagogical — it structurally mirrors the paper's overall approach: find a transformation that makes the weight matrix sparser without changing the function, then prune. This framing makes the paper's contribution clearly distinct from methods that design better pruning metrics (which operate in the original space) and aligns it instead with the line of work on reparameterizing the model for compression (similar in spirit to SliceGPT for pruning and QuIP for quantization). The key insight — that one can *learn* the transformation rather than hand-design it — is the bridge between the theory and the practical algorithm. The reviewers converged on the experimental gaps but agreed that the core idea has merit.

---

## Suggestions

1. **Add at least one training-based baseline** (e.g., ADMM-pruner or FISTAPruner, or even a simplified version that runs multiple gradient steps in the original space without rotation) under identical data and sparsity settings. This is the single most impactful addition.
2. **Report variance** (standard deviation over 3–5 runs) for the main perplexity and zero-shot results. At minimum, clarify whether the results are from a single run, and if so, why the stochastic elements (Cayley SGD, STE) are expected to be stable.
3. **Specify the number of Q matrices used** for each model in the main experiments (Tables 2, 3), and state the sharing strategy.
4. **Include dense model perplexity in Table 2** for all models, especially OPT-6.7B where the "outperforms dense" claim is made.
5. **Clarify how the sparsity budget is matched** between RotPruner and SliceGPT for structured pruning — whether by parameter count, FLOPs, or dimension reduction ratio.

---

## Score and Decision

**Originality**: Good. The idea of learning a rotation before pruning is genuinely novel and not a straightforward extension of prior work.  
**Importance of research question**: High. LLM pruning is practically important, and the paper addresses a real limitation of current methods.  
**Claims support**: Adequate but not airtight. The core claim (rotation improves pruning) is supported, but the lack of training-based baselines and variance reporting weakens the evidence.  
**Soundness of experiments**: Solid in coverage (multiple models, sparsity patterns, ablations) but has specific gaps described above.  
**Clarity**: Good overall. The method is explained clearly, though some experimental details are missing.  
**Value to community**: Moderate. The idea of reparameterizing the pruning space is likely to inspire follow-up work.

The paper makes a genuine contribution with a novel idea and consistent empirical support. The weaknesses are real but addressable — they do not invalidate the core claim, they mainly limit the strength of the attribution. The improvements are modest but consistent across a wide range of settings, and the ablations are thorough.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>