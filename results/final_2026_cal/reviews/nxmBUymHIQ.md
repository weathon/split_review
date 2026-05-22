Now let me write the final consolidated review.

## Summary

The paper proposes LoLoRA, a hybrid fine-tuning method that updates the LoRA adapter matrix *A* via local unsupervised Hebbian-like rules (HPCA or autoencoder loss) during the forward pass, while training matrix *B* via standard backpropagation. This design avoids storing activations for *A*'s backward pass, reducing activation memory. The paper also provides a theoretical characterization (Theorem 4.4) showing that optimal *A* initialization spans the top-*r* principal eigensubspace of the input covariance matrix. Experiments on GLUE, GSM8K, and LLaVA evaluate the method against LoRA and LoRA-FA variants.

## Strengths

1. **Clean theoretical characterization of optimal *A* initialization (Theorem 4.4).** The paper formally proves that, under a random-target regression assumption, the optimal frozen *A* must span the top-*r* principal eigensubspace of the input covariance matrix. This provides principled theoretical backing for the previously empirical EVA initialization (Paischer et al., 2024) and explains why PCA-based methods work.

2. **Novel hybrid local-global update scheme (Algorithm 1).** Combining Hebbian-like local updates for *A* with backpropagation for *B* is a genuinely underexplored design in the LoRA setting. The paper correctly identifies and addresses the known tension between local learning and end-to-end training (Lagani et al., 2022) by restricting local updates to the *A* adapter while keeping *B* on the global loss.

3. **Comprehensive ablation study (Tables 5–6).** The comparison of five local update rules (HPCA, HPCA no mean, HPCA svd-first, AE, SoftHebb) across three ranks (r=2,4,8) on TinyLlama provides useful practical guidance: methods that converge to the PCA subspace all perform similarly, and SoftHebb underperforms. This validates the theoretical choice of HPCA.

4. **Memory reduction demonstrated across multiple scales.** The paper reports memory savings consistent with LoRA-FA (~13% on 8B models, ~4 GB; ~3% on LLaVA-7B) and shows that comparable performance to standard LoRA can be maintained while cutting memory.

## Weaknesses

### Fatal
None.

### Major

1. **No demonstrated advantage over the simpler LoRA-FA+EVA baseline.** This is the paper's central evidential gap. Across all three main experiments, LoLoRA HPCA performs essentially identically to LoRA-FA with EVA initialization: GSM8K accuracy 0.829 vs 0.829 (Table 3); LLaVA loss 1.075 vs 1.070 (Table 4); on GLUE the two methods trade small leads within overlapping confidence intervals (Tables 1–2). LoRA-FA+EVA is simpler — it requires no online update rule, no per-step local optimizer state, and no extra forward-pass computation. The paper does not identify any setting where LoLoRA's online adaptation yields a clear win over a one-shot PCA initialization. This undermines the core claim that the local updates "mitigate the trade-off" between memory and performance that LoRA-FA suffers from.

2. **The local update mechanism is incompletely specified, harming reproducibility.** Algorithm 1 accepts an optimizer `Opt_loc` for the local *A* updates, but the paper never states what this optimizer is (SGD? Adam? what learning rate?) nor provides the explicit HPCA update equation. The description "stream SNL with running mean subtraction (smoothing factor 0.98)" (Section 5.4) is too vague to reproduce. Since the local updates *are* the method's primary novelty, this omission is a serious barrier to independent verification and adoption.

3. **The paper overstates its empirical results.** The conclusion claims "HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups." This is misleading. On GLUE (Tables 1–2), LoLoRA HPCA is numerically *worse* than LoRA-FA (uniform) on 6 of 8 tasks. On GSM8K, the difference (0.829 vs 0.826 for LoRA-FA uniform) is within one standard error. The only clear win is on LLaVA (loss 1.075 vs 1.087 for LoRA-FA uniform), and even there LoRA-FA+EVA (1.070) is better. The paper's own data does not support this claim as phrased.

### Minor

1. **Memory savings are modest and identical to LoRA-FA, with added optimizer cost.** The paper claims memory reduction, but on LLaVA (Table 4) LoLoRA uses 24.1 GB vs 23.9 GB for LoRA-FA — slightly *more*. The paper acknowledges adding "a small amount of extra optimizer state for the local updates" (Conclusion) but does not quantify this overhead or discuss whether it meaningfully offsets the claimed memory benefit.

2. **The theoretical result (Theorem 4.4) supports EVA initialization, not the online update mechanism specifically.** The theorem characterizes the optimal *frozen* *A* under stationary inputs. The paper's main argument for online updates is that the input distribution shifts as *B* changes, but no experiment tests this non-stationarity scenario (e.g., a domain-shift or multi-stage training setting where EVA's initial estimate would become stale). The online advantage over EVA is asserted but not experimentally demonstrated.

### Trivial

None.

## Nice-to-Haves

- Specify the local optimizer (type, learning rate, schedule) used for all HPCA/AE experiments to enable reproduction.
- Report the rank *r* used in each main experiment (GLUE, GSM8K, LLaVA) in the main text rather than deferring entirely to Appendix C.
- Add a direct statistical comparison (e.g., paired tests or effect sizes) between LoLoRA and LoRA-FA+EVA to substantiate any claimed advantage.
- Analyze when the online adaptation would theoretically help — e.g., a synthetic experiment with a controlled distribution shift during training where EVA's one-shot estimate becomes suboptimal but HPCA tracks the shift.

## Removed Points

These points were considered but removed as invalid, noise, or misreadings:

- *Missing rank values in main text*: The paper refers to Appendix C for hyperparameter details, which the parser stripped. The rank values exist in the original submission.
- *Critique that LoRA-FA+EVA comparison is unfair*: The comparison is fair; the issue is that the asymmetry favors the baseline, not the author's method, which is valid to note.
- *Missing related work*: Per policy, this cannot be verified.
- *Formatting/typo nitpicks*: These are parser artifacts, not author errors.
- *Criticism about unrelated downstream architectures (MLA)*: This is speculation about a future direction mentioned in the conclusion, not a core claim.
- *Claim that the paper's results are not reproducible due to missing appendix*: The appendix exists in the original submission; the parser stripped it.
- *Several generic area-of-concern sweeps from the harsh critic* (e.g., "could the metric be measuring a proxy?", speculative concerns about what the appendix "may" contain) that lack concrete anchors in the paper as written.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Identify a setting where LoLoRA clearly beats LoRA-FA+EVA.** The most impactful revision would be to test a scenario with substantial input distribution shift during fine-tuning (e.g., a multi-task curriculum, or a domain-adaptive fine-tuning setup) where a one-shot EVA initialization would become stale and HPCA's online tracking could shine. Without this, the method's complexity over a frozen *A* with good initialization is unjustified.

2. **Fully specify the local update mechanism.** Provide the exact HPCA update equation (is it the standard Oja rule or a normalized variant?), the local optimizer used (SGD with what learning rate?), and any hyperparameters of the update (smoothing factor, whether running mean is subtracted). Without these details the method cannot be reproduced.

3. **Tone down the performance claims.** The current conclusion overstates the empirical results relative to the data in Tables 1–4. The paper's actual contribution — a theoretically grounded combination of local learning with LoRA that matches LoRA-FA+EVA without requiring a pre-training PCA pass — is still a valid contribution, but the text should reflect what the data actually shows.

4. **Quantify the overhead of the local optimizer state.** Report the additional memory and compute cost of the local updates (optimizer state for *A*, extra forward-pass FLOPs, wall-clock time per step) versus LoRA-FA, so readers can make an informed cost-benefit judgment.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing).** Queried for LoRA / memory-efficient fine-tuning papers. Weak anchors (score < 3.5): OP-LoRA (3.00), DASP (3.00), DaRA (3.00), SoLoRA (3.00) — all rejected/withdrawn, more limited in contribution than LoLoRA. Middle anchors (3.5–7.5): ReLoRA (4.00, Reject), LoRAct (4.00, Reject), GIDA/RaLoRA (5.50, Accept Poster), LoFT (6.00, Accept Poster). Strong anchors (> 7.5): Polar Express (8.00), Transducing LMs (8.00) — not comparable topics. **Initial bracket: 3.5–5.5.**

**Round 2 (Narrowing).** Queried within (3.5, 5.5). LoRAct (4.00, Reject), CERSA (4.50, Reject), PrefixMemory-Tuning (5.00, Accept Poster), ScaLoRA (4.80, Reject), Understanding LoRA (4.67, Reject). Read LoRAct, CERSA, ScaLoRA, and GIDA in full.

**Comparison to anchors:**
- **LoRAct (4.00, Reject):** Both address activation memory. LoRAct claims 80% memory reduction vs LoLoRA's ~13%, but LoLoRA has stronger theory. LoLoRA is somewhat stronger.
- **CERSA (4.50, Reject):** Both have clean theory but limited experimental evidence. CERSA has broader evaluation (vision + text). LoLoRA and CERSA are similar in quality; LoLoRA has a more novel architecture but weaker empirical differentiation.
- **ScaLoRA (4.80, Reject):** Theoretical analysis of optimal scaling with modest gains over baselines. LoLoRA's theory is cleaner but its empirical gap is larger — ScaLoRA consistently improves over baselines, while LoLoRA does not clearly beat LoRA-FA+EVA. LoLoRA is slightly weaker.
- **GIDA/RaLoRA (5.50, Accept Poster):** Stronger empirical results with consistent gains across tasks. LoLoRA's weaker empirical differentiation places it below this anchor.

**Final score: 4.0.** The paper has a genuine theoretical contribution and a novel architecture, but the central evidential gap — failing to demonstrate an advantage over the simpler LoRA-FA+EVA baseline — combined with incomplete specification of the core algorithm, significantly limits its impact. The paper is below the bar set by the Accept anchors (GIDA at 5.5, LoFT at 6.0) and comparable to or slightly weaker than mid-range Reject anchors (CERSA at 4.5, ScaLoRA at 4.8).

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>