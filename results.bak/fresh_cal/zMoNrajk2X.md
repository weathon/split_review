Here is my consolidated final review.

---

## Summary

This paper introduces Condition-Annealed Diffusion Sampler (CADS), a method that adds scheduled, monotonically decreasing Gaussian noise to the conditioning signal during diffusion model inference. By corrupting the condition early in sampling (when the model is forming the coarse structure of the output) and annealing the noise to zero by the end, CADS breaks the overdependence on the conditioning signal that causes diversity collapse at high guidance scales. The method requires no retraining, works with any off-the-shelf sampler, and is evaluated across four tasks: class-conditional ImageNet (using DiT-XL/2), pose-to-image generation, identity-conditioned face generation, and text-to-image (Stable Diffusion).

## Strengths

1. **Simple, well-motivated method with a clear theoretical footing.** The idea of adding and annealing noise to the conditioning signal is intuitive and is connected to Bayes' rule: when the noise is large early in sampling, the conditional score term vanishes, allowing the model to explore the unconditional data distribution, with a gradual return to conditional fidelity. The piecewise linear schedule (with cutoffs $\tau_1, \tau_2$) is straightforward to implement.

2. **Consistent empirical gains across four diverse tasks without retraining.** CADS improves FID and Recall on class-conditional ImageNet, pose-to-image (DeepFashion and SHHQ), identity-conditioned face generation (ID3PM), and text-to-image (Stable Diffusion), compared apples-to-apples against DDPM sampling on the same backbone with the same random seeds (lines 102–104, Table main-results). Precision is largely preserved, confirming that diversity gains do not come at the cost of quality.

3. **Outperforms the natural baseline of Dynamic CFG.** Dynamic CFG (underweighting the guidance term early in sampling) is a reasonable alternative approach to improving diversity. CADS substantially outperforms it: FID 9.47 vs. 18.42 and Recall 0.62 vs. 0.39 on class-conditional ImageNet (Table cads-vs-Dynamic CFG). This demonstrates that adding structured noise to the condition is more effective than simply modulating the CFG weight.

4. **Systematic ablations of key hyperparameters.** The paper ablates the noise scale $s$, the cutoff threshold $\tau_1$, and the rescaling mixing parameter $\psi$, providing practical guidance (lines 170–179). The trade-offs are clearly described: too little noise produces minimal diversity improvement; too much noise degrades quality. The recommendation to start with $\psi=1$ is concrete and actionable.

5. **Preserves condition alignment.** Despite injecting noise into the conditioning signal, class accuracy drops only from 0.98 to 0.96, MPJPE stays at 0.02, and CLIP-Score remains 0.31 (Table alignment), confirming that the annealing restores sufficient conditional fidelity.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The SOTA FID claim compares across different backbone architectures.** CADS applied to DiT-XL/2 achieves FID 1.70 (ImageNet 256×256), surpassing MDT's published result. Since MDT and DiT-XL/2 are different architectures, the improvement may partly reflect the base model's strength rather than the sampling method alone. The paper is transparent about using DiT-XL/2 (line 87) and explicitly notes that SOTA is achieved "solely through improved sampling" on a *pretrained* model (line 107). However, the comparison would be cleaner if contextualized as "CADS on DiT-XL/2 achieves the best reported FID to date" rather than an unconditional SOTA claim, and the counterfactual (CADS applied to MDT's own model) would strengthen the evidence. The apples-to-apples comparisons against DDPM on DiT-XL/2 (which *do* isolate the effect of CADS) are convincing and well-presented — the SOTA framing is the part that needs tightening.

2. **Hyperparameters for the SOTA result are adjusted per guidance scale.** The paper states that for higher $w_{\text{CFG}}$, parameters $s$ and $\tau_1$ are adjusted to "fully leverage the potential of CADS" (line 113). This is sensible but means the SOTA FID likely involved selecting an optimal combination of $(w_{\text{CFG}}, s, \tau_1, \psi)$. While the ablations explore each parameter individually, a joint sensitivity analysis (e.g., a small grid showing the range of FIDs obtainable across reasonable settings) would strengthen confidence that the result is not a product of cherry-picking. The core claim — that CADS consistently improves diversity — does not depend on this particular combination, but the SOTA number would benefit from robustness evidence.

3. **The $\psi$ value used for the main results is not explicitly stated.** The paper recommends $\psi=1$ (line 179) and the ablation shows its effect, but the text does not say "all main results use $\psi=1$" (or another value). Since $\psi$ controls the regularization-diversity trade-off, the reader should know this setting for the headline numbers. (The relevant tables are stripped by the parser, so the exact value may be listed there; the main text should state it explicitly.)

### Trivial

- **No variance/statistical uncertainty reported for any metric.** FID and Recall are reported as point estimates without multiple runs or bootstrap intervals. This is standard practice in the field for large-scale benchmarks (ImageNet), so it is not a flaw per se, but noting whether repeated evaluations yield stable numbers would be a small improvement.

## Nice-to-Haves

- **Quantify computational overhead explicitly.** The paper says CADS involves "minimal" overhead (line 19), which is true (one elementwise addition and multiplication per step), but a concrete statement (e.g., "less than X% runtime increase") would be helpful.
- **Joint hyperparameter grid.** A small grid over $(w_{\text{CFG}}, s, \tau_1)$ showing FID ranges (similar to what is suggested above) would make the SOTA result more robust.
- **Discussion of other diversity-enhancing approaches.** The paper covers Dynamic CFG; other methods like likelihood-based rejection sampling or truncation could be acknowledged, even if briefly, to position CADS more precisely. The paper does cite truncation in the related work (line 27), so this is partially addressed.

## Removed Points

*These points are flagged to be removed — treat them with caution.*

- **"Effect of CADS on the number of sampling steps"** — Speculative question not presented as a flaw; the paper is about diversity, not convergence speed. Removed as it asks a question the paper never claimed to address.
- **"Clarity on what is being noised"** — The paper explicitly states (lines 93–94): noise is added to class embeddings (DiT), face-ID embeddings (ID3PM), text embeddings (SD), and pose images (pose-to-image). The method is clearly described. This criticism reflects a misreading.
- **"Comparison with prior diversity-enhancing methods (truncation, rejection sampling)"** — The paper cites truncation in related work (line 27) and compares against the most relevant baseline (Dynamic CFG). Requesting exhaustive comparisons is scope creep. Removed.
- **"Missing comparison of CADS applied to MDT's own model"** — The paper's claim is about "CADS + an existing pretrained model beats MDT," not "CADS would improve MDT." Requesting this counterfactual exceeds the stated scope.
- **Any formatting/style/typo criticisms** — These are parser artifacts, not author errors. Removed per instructions.

## Novel Insights

The harsh critic's speculation about over-tuning and the strength finder's catalog of claimed strengths largely echo the paper's own claims. Beyond the paper's own contributions, a genuinely novel observation from the reviewer pipeline is the tension between the cross-architecture SOTA claim and the apples-to-apples evidence: the paper's most robust result (CADS consistently improves diversity on the *same* backbone, same seeds) is stronger than its flashiest result (SOTA FID), and the paper would benefit from emphasizing the former. This is a framing insight, not a technical one.

## Suggestions

1. **Reframe the SOTA claim.** State it as: "Applying CADS to a pretrained DiT-XL/2 model achieves FID 1.70, the best reported result on ImageNet 256×256 among methods that do not require retraining," or simply report the apples-to-apples FID gain (CADS vs. DDPM on DiT-XL/2) as the primary evidence, with the comparison to MDT as a secondary observation.
2. **Explicitly state $\psi$ values for each experiment in the main text**, not just in the ablation section.
3. **Add a small joint sensitivity table** (e.g., 3×3 grid over $s$ and $\tau_1$ at a fixed $w_{\text{CFG}}$) to demonstrate that CADS's improvement is robust across reasonable hyperparameter ranges, not just at the optimal point.
4. **Add a sentence quantifying computational overhead** (e.g., "CADS adds one elementwise operation per step, incurring <1% wall-clock overhead").

## Score and Decision

The paper presents a simple, novel, and well-motivated method that consistently improves the diversity of conditional diffusion models across multiple tasks, backbones, and samplers without retraining. The core contribution is clearly demonstrated through apples-to-apples comparisons, and the ablation studies are thorough. The weaknesses are bounded and addressable: the SOTA framing is slightly inflated across architectures, hyperparameter sensitivity is not explored jointly, and $\psi$ values could be stated more explicitly. None of these undermine the paper's main claims.

**Score: 8.0/10** — Strong paper with clean contributions and convincing evidence. The method is immediately useful to the community.

**Decision: Accept**

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>