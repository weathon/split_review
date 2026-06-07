Now I have a clear picture. Let me now finalize the review.

**Anchor comparison summary:**

| Anchor | Score | Round | Comparison to MoEP |
|--------|-------|-------|--------------------|
| NanoMoE | 3.00 | R1 | MoEP is clearly stronger — has real LM evaluation (BabyLM), multiple baselines, code release, vs. toy problems only |
| SP-LoRA | 4.50 | R2 | Different topic (PEFT), but similar level of validation |
| Q-Sparse | 4.75 | R2 | Most comparable — novel sparsity method for LLMs, reasonable but thin validation, no efficiency measurements, rejected. MoEP has a more novel architectural idea but thinner validation (single seed, no ablations) |
| MoLEx | 6.33 | R1 | Clearly stronger — comprehensive experiments across benchmarks, theoretical analysis, better validation |
| Diff Transformer | 8.00 | R1 | Far stronger — large-scale, thorough ablations, multiple downstream evaluations |

**Bracket:** Round 1 placed MoEP in 4.0–5.5. Round 2 narrowed this: MoEP is comparable to Q-Sparse (4.75) but slightly weaker due to the missing routing analysis claim, single-seed evaluation, and lack of ablations. I'd place it at **4.5**.

---

## Summary

MoEP (Modular Expert Paths) proposes a decoder-only language model architecture that adds sparsity while keeping total parameter count fixed. It combines (i) layer-level top-k routing across parallel Transformer blocks operating at reduced hidden dimension, with (ii) Mixture-of-Experts projection blocks that handle the shrink/grow dimension transitions between full and reduced dimensions. The authors evaluate on the BabyLM strict-small track (~10M words, 28M parameters) and report that MoEP matches or slightly exceeds their GPT-2 baseline while reaching peak evaluation performance earlier in training (30M words vs. less stable convergence for GPT-2).

## Strengths

- **Layer-level MoE is genuinely underexplored and the paper identifies a clear architectural gap.** Section 2.2.2 provides a well-organized taxonomy of MoE placement strategies (FFN-level, attention-level, hybrid, layer-level) and correctly notes that layer-level expert networks remain largely unstudied, with MoLE (Wu et al., 2024) being the only prior work at that level — and it uses LoRA on frozen models, making MoEP's from-scratch training approach distinct.

- **Parameter-matched comparison at 28M parameters.** Table 2 confirms MoEP and GPT-2 both use 28M parameters, and Table 1 shows MoEP achieves a higher macro average than the BabyLM GPT-2 baseline (49.00 vs. 46.60 excluding AoA; 44.50 vs. 37.40 with AoA). The comparison is direct and controlled for parameter count.

- **Evidence for accelerated early learning under sparse routing.** The training dynamics analysis (Appendix A.3) reports that MoEP reaches peak evaluation performance at 30M words with broadly stable task scores, while GPT-2 shows different tasks peaking at different checkpoints and less stable convergence. This provides concrete support for the claim that modular routing improves sample efficiency.

- **The SwiGLU variant provides a useful negative result.** The MoEP-SwiGLU variant (38M params, Table 2) underperforms the simpler linear-expert MoEP and converges more slowly (80M words to peak vs. 30M), supporting the paper's claim that lightweight linear experts are more effective at small scale.

- **Reproducibility infrastructure.** The paper releases code (PyTorch + Hugging Face), trained model weights, uses a fixed random seed (42), and follows the official BabyLM evaluation pipeline without modification.

## Weaknesses

### Fatal

None.

### Major

- **Single-seed evaluation with a marginal gap.** All models are trained with a single random seed (42, Table 3). MoEP's advantage over the authors' own GPT-2 is 0.9 macro-average points (49.00 vs. 48.10 excluding AoA). With no error bars, variance estimates, or multiple-seed runs, there is no statistical basis for concluding that MoEP genuinely outperforms GPT-2 rather than reflecting training noise. Running 3–5 seeds would be inexpensive (1–2 hours per run on a single A100 per Section 4).

- **No ablations.** MoEP is a compound architecture combining (a) MoE shrink/grow projection blocks with gated linear experts, (b) parallel layers with top-k routing among P blocks, and (c) dual load-balancing losses. None of these components is ablated. There is no comparison to a version without MoE blocks (using simple fixed projections), no variation of P or top-k, and no non-routed parallel stack. The paper provides no evidence to attribute the gains to any specific mechanism, making it impossible to assess which architectural ideas are actually valuable.

- **The claimed routing-behavior analysis does not exist in the paper.** Contribution #3 states: "We analyze expert networks routing behavior and show that layer level parallelism enable fast and stable training." The paper contains zero analysis of routing behavior — no examination of which tokens are assigned to which parallel blocks, no expert utilization statistics beyond what the load-balancing loss enforces, no evidence for functional specialization, and no comparison of routing patterns across layers. What the paper calls "routing behavior analysis" is training-dynamics curves (checkpoint-level evaluation scores over training, Appendix A.3 / Section 5.1), which measure training outcomes, not routing. This is a claimed contribution that is absent from the paper.

- **No computational efficiency analysis despite efficiency being the central motivation.** The paper's framing ("compact and efficient sparsity," "without overloading computation") and title explicitly center efficiency. Yet there is no measurement of training FLOPs, inference FLOPs, latency, throughput, or active parameters per token relative to the GPT-2 baseline. Parameter count alone is an incomplete efficiency metric when architectures differ in routing overhead (top-k gating in both MoE blocks and parallel layers).

### Minor

- **Introduction overclaims relative to the full results.** The introduction states that MoEP "was able to outperform all BabyLM strict-small baseline models, including the GPT-2 and GPT-BERT models as well" without qualification. On the AoA-exclusive macro average, GPT-BERT (causal) scores 54.10 vs. MoEP's 49.00 — a 5-point gap favoring the baseline. The qualification that the claim holds only under the AoA-inclusive metric appears in Section 5.1 but not in the introduction, where the unqualified claim is misleading.

- **Checkpoint selection protocol raises data-leakage concern.** The paper selects the best checkpoint based on "fast evaluation" performance (Section 4) but does not specify whether this fast evaluation uses the same tasks as the final evaluation or a held-out subset. If the former, reported scores may be inflated by implicit test-set optimization.

- **MoEP-SwiGLU comparison is confounded by parameter count.** MoEP-SwiGLU has 38M parameters vs. 28M for MoEP and GPT-2 (Table 2). The paper attributes its worse performance to "SwiGLU complexity," but the parameter-count difference confounds this interpretation.

- **Training dynamics analysis is qualitative rather than quantitative.** The early-learning claim (Section 5.1, Appendix A.3) describes MoEP as showing "more comprehensive early learning" and reaching peak at 30M words, but provides no per-task quantitative metrics at each checkpoint beyond visual inspection of figures.

### Trivial

None.

## Nice-to-Haves

- Running 3–5 seeds and reporting mean ± std for macro averages would address the most pressing weakness at negligible computational cost.
- A minimal ablation set — MoEP without MoE blocks (fixed linear projections), and P=1 (no routing in parallel layers) — would isolate the contribution of each component.
- Even basic routing diagnostics (histograms of block/expert selection frequencies, routing entropy per layer) would fulfill the promised routing-analysis contribution.
- Computing and reporting training/inference FLOPs would substantiate the efficiency motivation directly.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Grammatical issues in the introduction.** Removed per instructions: pure formatting/style nitpicks carry no weight in evaluation.

- **MoLE PEFT distinction allegedly overlooked.** Removed as factually incorrect: the paper explicitly states MoLE "applies LoRA weights at the layer level to a frozen pre-trained model" (line 90), demonstrating awareness of the PEFT distinction.

- **Missing λ values for load-balancing losses.** Removed per instructions: these likely appear in Appendix A.2, which was stripped by the parser; criticisms about absent appendix content are not valid.

- **Authors' GPT-2 outperforms BabyLM GPT-2 baseline (48.10 vs. 46.60).** Removed: this asymmetry favors the baseline, making MoEP's comparison harder, not easier. Per instructions, asymmetry that favors the baseline is not a valid weakness.

## Novel Insights

The paper's combination of layer-level parallelism with sparse top-k routing at reduced dimension — keeping total parameter count fixed while adding sparsity — is a genuinely novel direction. More interesting than the raw performance numbers is the finding that sparse routing appears to accelerate early-stage learning: MoEP's training dynamics show it extracts useful patterns more quickly than the dense baseline, even when final scores converge. The negative result with SwiGLU experts at small scale (slower convergence, worse final performance despite more parameters) is also practically useful for anyone exploring MoE at small computational budgets.

## Suggestions

- The paper's strongest contribution is the architectural idea and the early-learning observation, not the marginal final-performance delta. Restructure the framing to emphasize sample efficiency and the design space rather than a blanket "outperforms all baselines" claim.
- The routing-behavior analysis claim should either be removed from the contribution list or actually delivered — even simple utilization histograms would satisfy it.
- The checkpoint selection procedure needs clarification: if "fast evaluation" used the same tasks as final evaluation, the paper should acknowledge and discuss this limitation, or ideally use a separate validation split.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>