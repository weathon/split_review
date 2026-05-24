Now I have a thorough understanding of the paper and the reviews. Let me construct the final consolidated review.

---

## Summary

Pi-CCA reframes forgetting in vision-language continual learning (VL-CL) as drift of the cross-modal alignment geometry (canonical correlations and subspaces), and introduces a replay-free framework that preserves these invariants via a compact sketched certificate updated through streaming EMAs. The method also incorporates prompt-invariance via projector averaging over perturbation. Across four VL-CL benchmarks (MTIL, X-TAIL, VLCL, ConStruct-VL), Pi-CCA achieves state-of-the-art results among replay-free methods, with thorough ablations confirming the importance of each component.

## Strengths

- **Principled reframing of forgetting as alignment-geometry drift.** The paper identifies a genuine gap in prior VL-CL work: regularizing proxy signals (similarities, logits, parameters) rather than the cross-modal alignment object itself. Pi-CCA directly preserves the whitened cross-covariance's top-\(k\) spectrum and subspaces, which is the quantity that underpins CLIP's zero-shot generalization. This conceptual contribution is substantial and well-motivated (Section 1, gap statement). The ablation study (Table 3) validates this: removing either the spectral or subspace term causes the largest performance drops (2.2–2.7 points).

- **State-of-the-art results across four diverse VL-CL tracks.** Pi-CCA outperforms all prior replay-free methods on MTIL (Avg 76.8, Last 75.5), X-TAIL (Avg 68.1), VLCL retrieval (I2T R@1 48.6), and ConStruct-VL (FA 75.2, AF 2.7). On VLCL it even surpasses a synthetic-replay method (GIFT), despite being fully replay- and generator-free (Tables 1, 2). This establishes that direct geometry preservation can match or exceed data-based distillation approaches.

- **Efficient, constant-memory certificate via random sketches and streaming EMA.** The certificate uses random orthonormal sketches (\(h \ll d_v, d_t\)) and streaming EMA updates to maintain constant storage independent of feature dimensionality (Section 3.2, 3.4). The Pareto analysis (Figure 2) identifies a broad efficient frontier around \((k,h) = (64,256)\) with modest memory/time cost, confirming the "small yet sufficient" certificate hypothesis.

- **Thorough robustness and ablation analysis.** Component ablations (Table 3, 8 variants), hyperparameter sensitivity (Appendix A.3), task-order sensitivity across 20 random sequences (Figure 5, narrow IQRs), and prompt-invariance stress tests (Figure 4) collectively demonstrate that the method's performance is robust and not contingent on a single configuration or task order.

- **Prompt-invariance mechanism is well-motivated and validated.** The \(\mathcal{L}_{\text{pi}}\) loss (Eq. 11) averages text projectors over prompt perturbations and contracts their dispersion. Stress tests (Figure 4) show it flattens degradation: at the strongest perturbation level, R@1 improves by +2.44 p.p. (ID) and +2.51 p.p. (OOD) over the ablated variant, with AF reductions of \(\approx 1.0\).

## Weaknesses

### Major

- **Baseline comparison transparency is incomplete.** The paper does not state whether the numbers for competing methods in Tables 1 and 2 come from controlled re-implementations under identical conditions (same backbone, LoRA configuration, batch size, learning schedule) or from original publications. Table 1 reports no confidence intervals — in contrast to Table 2, which does — further complicating assessment of whether observed gaps are statistically significant. If numbers are drawn from prior publications, differences in training protocols (full fine-tuning vs. LoRA, different image resolutions, different evaluation pipelines) could account for some of the reported margins. The paper should either re-run all baselines in a controlled setting, or transparently state the source of each number and justify why the comparison is fair. Given that the paper's own ablations already demonstrate the importance of the geometry-preservation losses (removing them drops 2.2–2.7 points), the core claim does not collapse — but the empirical support for "state-of-the-art" is weaker than it should be.

- **No "pure task loss + LoRA" baseline is reported.** The ablations (Table 3) remove individual certificate losses but always retain at least some of \(\mathcal{L}_{\text{spec}}, \mathcal{L}_{\text{sub}}, \mathcal{L}_{\text{pi}}\). Without a baseline of "just training with \(\mathcal{L}_{\text{task}}\) and no certificate losses at all," the reader cannot calibrate how much of the overall performance is driven by the geometry-preservation losses vs. the task objective and LoRA structure alone. This lower bound is standard practice for continual learning papers and would strengthen the ablation story.

### Minor

- **Figure 3's near-perfect correlations need clarification.** The reported Pearson/Spearman correlations of 0.99–1.0 between geometry drift and performance drop are unusually high. The paper states it "sweeps realistic perturbations" but does not clarify whether the drift measures (\(D_{\text{ang}}, D_{\rho}\)) are computed on the same mini-batch statistics used during training or on a held-out evaluation set. If the former, the correlation is partly self-referential (the optimizer reduces both the loss and the drift it measures). If the latter, the near-perfect linearity still warrants explanation given the diversity of swept hyperparameters. The paper should explicitly state the measurement protocol and consider whether this analysis adds value beyond the ablation study (Table 3), which already cleanly demonstrates the causal role of geometry preservation.

- **Inconsistent error bar reporting.** Table 1 (MTIL, X-TAIL) reports no variance or confidence intervals, while Table 2 (VLCL, ConStruct-VL) reports \(\pm\) intervals. The paper should either add error bars across multiple seeds for Table 1 or explain why they are omitted (e.g., deterministic single-run setup). Without this, the reader cannot assess the stability of the reported classification results.

- **Hyperparameter complexity with limited guidance.** The full method involves streaming EMAs with rates \(\alpha\) and \(\beta\), four loss terms with weights \(\lambda_1, \lambda_2, \lambda_3\) and an additional \(\eta\), a balance parameter \(\xi\) for spectral loss, optional spectral moment order \(J\), sketch factor \(h\) and rank \(k\), multiple power-iteration steps, and ridge parameters \(\gamma_v, \gamma_t\). While the Pareto analysis (Figure 2) shows a broad ridge for \((k,h)\) and Appendix A.3 conducts sensitivity experiments, the main paper gives no concrete advice for setting the loss weights (\(\lambda_{1:3}, \eta\)) or ridge parameters on new benchmarks. The risk is that the reported results may depend on careful tuning that is not easily reproducible.

- **Memory usage comparison with baselines is absent.** The Pareto analysis (Figure 2) reports Pi-CCA's own memory and time, but the paper does not compare the memory footprint of competing methods. Since Pi-CCA claims "constant-memory" and "replay-free" as advantages, showing that baselines (e.g., GIFT uses a diffusion generator, C-CLIP uses a reference corpus) have substantially higher memory would strengthen this message. Without this, the memory advantage claim is only self-referential.

- **Whitening sensitivity is not studied.** The entire method rests on stable estimation of \(\Sigma^{-1/2}\), yet the paper only mentions that ridge parameters \(\gamma_v, \gamma_t\) can be fixed or adapted via Ledoit–Wolf. No sensitivity analysis of these ridge parameters is reported, and the "stable whitening" description (eigendecomposition with eigenvalue floor or Newton-Schulz iteration) is not evaluated for its impact on downstream performance. Given that covariance inversion is known to be sensitive, this gap should be addressed.

### Trivial

- The hyperparameter \(\eta\) in the dispersion term of \(\mathcal{L}_{\text{pi}}\) (Eq. 11) is never discussed in the experiments (its value, sensitivity, or whether it was tuned). Providing its default value and a brief sensitivity note would improve reproducibility.
- The stop-gradient on the certificate during SVD is important for training stability but only appears in the appendix algorithm; a brief comment in the main text (Section 3.4) would help readers understand the gradient flow.

## Nice-to-Haves

- A theoretical justification (even heuristic) for why preserving top-\(k\) CCA structure suffices for zero-shot recognition/retrieval under domain shifts. The paper alludes to this (Appendix A.4 references a theoretical section), but a brief intuitive argument in the main text would strengthen the conceptual contribution.
- Direct measurement of text projector variation under perturbations (e.g., Frobenius norm of \(Q_t\) with and without \(\mathcal{L}_{\text{pi}}\)) to confirm that the prompt-invariance loss reduces sensitivity at the representation level, not just downstream.
- A brief Johnson-Lindenstrauss-type guarantee for the required sketch dimension \(h\) relative to subspace rank \(k\) and target distortion \(\epsilon\) would improve the theoretical grounding of the sketch-based subspace preservation.

## Removed Points

- *"The correlation analysis is potentially misleading and should be removed"* (Harsh Critic). — Demoted to Minor. The high correlations are worth questioning, but the paper's description of the sweep (over realistic perturbations of the same method) makes them partly expected. The weakness is the lack of clarification about measurement protocol, not that the analysis is fundamentally flawed.
- *"The method has too many hyperparameters"* (Harsh Critic). — Demoted to Minor. The Pareto analysis and Appendix A.3 partially address this, and the ablation study isolates each component's contribution. The remaining concern is about loss-weight guidance, which is minor.
- *"The prompt-invariance loss is evaluated only on retrieval and forgetting metrics"* (Harsh Critic's "Missing Parts"). — Moved to Nice-to-Haves. The downstream evaluation is sufficient; representation-level analysis would be a bonus.
- Strength Finder's strength about "Direct empirical evidence linking geometry stability to downstream retention" — Kept but the caveat about the unclear measurement protocol is noted in Weaknesses.
- *"The paper does not explicitly state the required sketch dimension h relative to subspace rank k"* — Moved to Nice-to-Haves. A theoretical guarantee would improve the paper but is not required for empirical validation.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- **Clarify baseline sources**: In a revision/rebuttal, explicitly state which numbers come from re-implementations vs. publications. If numbers are from publications, justify that the comparison is fair (same backbone, same LoRA usage, same evaluation pipeline) or add a controlled re-run.
- **Clarify Figure 3 measurement protocol**: State whether \(D_{\text{ang}}\) and \(D_{\rho}\) are computed on training batches, streaming EMAs, or a held-out evaluation set. If on training data, acknowledge the self-referential component and consider re-doing the analysis with held-out drift measurement, or simply rely on Table 3's ablation which is cleaner evidence.
- **Add "pure task loss" baseline**: Report performance of training with only \(\mathcal{L}_{\text{task}}\) (no certificate losses) to calibrate the absolute contribution of the geometry-preservation losses.
- **Add error bars to Table 1**: Run at least 3 seeds for MTIL and X-TAIL and report \(\pm\) intervals, consistent with Table 2.
- **Report memory comparison with baselines**: Add a column or footnote showing the memory footprint of key baselines (especially replay-based ones) to substantiate the constant-memory/replay-free advantage.
- **Provide default values and sensitivity for \(\lambda_{1:3}, \eta, \xi, \gamma_v, \gamma_t\)**: At minimum, report the values used in the main experiments and whether performance is stable over a 2×–5× range.

## Score and Decision

**Calibration report:**

**Round 1 (bracketing):** Three queries on "continual learning vision-language CLIP replay-free forgetting" with score bands:
- <3.5: papers avg 2.0–3.0 (e.g., "LVLM-CL" 2.50, "A Multimodal Class-Incremental Learning benchmark" 2.33)
- 3.5–7.5: papers avg 3.8–6.5 (e.g., "C-CLIP" 6.50 Accept, "PROOF" 5.67 Reject, "Vision and Language Synergy" 5.00 Accept, "CLIP model is an Efficient Online Continual Learner" 3.80 Reject)
- >7.5: papers avg 8.0–9.0 (e.g., "Function Vectors for Catastrophic Forgetting" 9.00, "Compositional Entailment Learning" 8.00)

Initial bracket: [5.5, 7.5].

**Round 2 (narrowing):** Two targeted queries in the (5.5, 7.5) and (6.0, 8.0) bands retrieved:
- C-CLIP (6.50, Accept) — most directly comparable VL-CL paper. C-CLIP introduces LoRA+contrastive consolidation for VL-CL. Pi-CCA has stronger conceptual novelty (geometry-first vs. distillation) and broader evaluation (4 tracks vs. retrieval+classification), but C-CLIP is more transparent about baseline comparisons. Pi-CCA is slightly stronger overall.
- TiC-CLIP (6.25, Accept) — benchmark contribution for continual CLIP training. Pi-CCA has stronger methodological novelty.
- PROOF (5.67, Reject) — projection fusion for VLM CIL. Pi-CCA is substantially stronger in novelty, evaluation breadth, and empirical support.
- Spurious Forgetting (6.33, Accept) — conceptual analysis of forgetting in LLMs. Pi-CCA is comparable in novelty but stronger in empirical validation.

Pi-CCA sits comfortably above the rejected anchors (~5.67) and is comparable to or slightly above accepted anchors in the 6.25–6.50 range. The main factors preventing a 7+ score are the baseline transparency issue and the unclarified Figure 3 correlation analysis, both of which are fixable.

**Final score: 6.5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>