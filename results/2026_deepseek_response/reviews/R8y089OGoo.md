Now let me write the final consolidated review with all the calibration and filtering applied.

## Summary

This paper proposes DIPOLE, an RL algorithm for diffusion policy optimization that decomposes the KL-regularized objective into positive (reward-maximizing) and negative (reward-minimizing) dichotomous policies using bounded sigmoid weights, replacing the unstable exponential weighting of prior methods. The optimal policy is recovered via linear combination of the two policy scores during inference, enabling controllable greediness through a single parameter ω. Empirical evaluation spans 39 tasks on ExORL and OGBench benchmarks plus a real-world autonomous driving experiment on NAVSIM with a 1B-parameter VLA model.

## Strengths

1. **Clean and principled theoretical derivation**: The paper derives a closed-form optimal solution (Theorem 1, Eq. 6) from a greedified KL-regularized objective and shows how it naturally decomposes into dichotomous policies with bounded sigmoid weights (Eq. 7–8), avoiding the loss explosion of exponential weighting. The connection to classifier-free guidance (Eq. 10) is insightfully drawn.

2. **Strong empirical results across diverse RL benchmarks**: On ExORL (Table 1), DIPOLE achieves the best score in 8 of 9 tasks (e.g., Walker stand 953 vs. best prior 873, Walker walk 910 vs. 844). On OGBench (Table 2), it obtains the best aggregate in 4 of 6 categories. These results are supported by 8 random seeds with standard deviations reported.

3. **Controllable inference via greediness factor**: The linear combination of dichotomous policy scores controlled by ω (Eq. 10) provides an interpretable knob to adjust the optimality of generated actions, with a principled connection to classifier-free guidance.

4. **Demonstrated scalability to real-world tasks**: Fine-tuning a 1B-parameter VLA model on the NAVSIM autonomous driving benchmark yields a PDMS improvement from 88.3 to 89.7 (navtrain split), outperforming prior methods. This demonstrates the method works at a scale where training stability is non-trivial.

5. **Transparency via DIPOLE w/o rs variant**: The paper includes a variant without rejection sampling, enabling partial isolation of the core method from the inference-time sampling procedure.

## Weaknesses

### Major

1. **Rejection sampling confound not fully controlled**: DIPOLE w/o rs (no rejection sampling) underperforms IFQL on several ExORL tasks (Cheetah run: 194 vs. 269; Jaco reach-top-right: 84 vs. 193; Walker run: 256 vs. 406), while full DIPOLE (with rejection sampling) outperforms IFQL everywhere. The baselines IFQL and IDQL also use rejection sampling during inference. The paper does not compare all methods under equivalent inference procedures (all with rejection sampling or all without), so it is unclear how much of DIPOLE's gains come from the dichotomous decomposition versus the rejection sampling strategy applied on top. A controlled comparison—DIPOLE vs. an exp-weighted baseline with matched rejection sampling, or all methods without rejection sampling—would cleanly isolate the contribution of the core objective.

2. **NAVSIM navtest result is not comparable to prior work on a level playing field**: The headline result of 94.8 PDMS (+6.5 over the baseline) is obtained by training on the navtest split, which is not the standard training split used by prior methods in Table 4. The paper acknowledges this but presents the 94.8 alongside baselines trained on navtrain, creating an apples-to-oranges comparison. The fair comparison—training on the standard navtrain split—yields a more modest 89.7 (+1.4 over the 88.3 baseline). The DP-VLA w/ DPPO navtest row (89.0) shows that training on navtest alone does not explain the entire gap, but the absence of navtest-trained versions of prior methods (UniAD, Hydra-MDP, etc.) means the 94.8 number cannot be taken as a 6.5-point improvement over the state of the art.

### Minor

3. **Computational cost of training two diffusion models is not reported**: Maintaining both a positive and a negative policy doubles model parameters and per-step updates compared to single-policy methods (FQL, IFQL). For the RL benchmarks, two full diffusion models are trained; for the VLA model, two LoRA modules are used. The paper provides no runtime, memory, or FLOPs comparison with baselines, making it difficult to evaluate the practical trade-off of the method's design.

4. **Hyperparameter sensitivity of β and ω not discussed**: Both β (temperature) and ω (greediness factor) are critical parameters that control the behavior of DIPOLE. The paper does not report how performance varies with these parameters or justify the chosen values, which limits practical reproducibility and understanding of robustness.

5. **Limited offline-to-online evaluation**: The offline-to-online experiments (Table 3) cover only 4 tasks (one per domain). While the AD experiment provides complementary evidence, the scope of the online fine-tuning analysis is narrow for drawing general conclusions.

### Trivial

6. The paper states "poor-quality samples still retain positive weight" as a limitation of exp-weighted regression; the exponential weighting makes these weights near-zero, so this framing slightly overstates the issue.

## Nice-to-Haves

- An ablation that compares DIPOLE against a single diffusion model trained with sigmoid-weighted regression (no decomposition, no negative policy) would more directly isolate the benefit of the two-policy architecture.
- For the AD experiment, training the baselines on the navtest split (or restricting DIPOLE to navtrain as the primary comparison) would allow a clean, fair comparison.

## Removed Points

These points were identified by the reviewer but removed after cross-checking against the paper: they are either factually inaccurate, reflect speculative concerns, or are otherwise not valid weaknesses as judged against the paper's actual content.

- "Section 3.2 justification is thin": The paper provides a full mathematical derivation from Eq. 5 to Theorem 1 with cited supporting works (Singh et al., 2022; Hong et al., 2023; Xu et al., 2025). The derivation is sound and the references are appropriate.
- "Critic learning details missing from main text": The paper explicitly states "we can set G(s,a) as the advantage function A(s,a)" and defers full critic implementation details to Appendix C and D, which is standard practice given page limits.
- "DIPOLE w/o rs underperforms IFQL" as a standalone weakness: The paper includes this variant precisely for transparency; the asymmetry in inference procedures (DIPOLE w/o rs uses no rejection sampling while IFQL uses rejection sampling) actually makes DIPOLE w/o rs's competitive performance on tasks like Quadruped and Walker stand more impressive.
- Speculative concerns about rejection sampling prevalence between baselines: The paper explicitly states IFQL and IDQL use rejection sampling, so this is not an omission.
- "Missing related works" and "missing appendix details": These sections are stripped by the PDF parser and exist in the original submission.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a controlled ablation with matched inference procedures: compare DIPOLE (with rejection sampling) against an exp-weighted diffusion baseline (Eq. 4) using the same rejection sampling strategy.
2. Restructure Table 4 to clearly separate navtrain-trained results (fair comparison) from navtest-trained results (additional demonstration), or add navtest-trained baselines.
3. Report training wall-clock time and GPU memory relative to a single-policy method (e.g., IFQL or FQL) on one ExORL task.
4. Include a sensitivity analysis (even brief) showing performance as a function of β and ω on 2–3 representative tasks.

## Score and Decision

**Round 1 (Bracketing)** — Three queries across score bands:
- Weak band (avg < 3.5): `mc97L2QVIa.md` (3.00, offline MARL diffusion), `cXxfVkRCHJ.md` (3.00, O2O RL diffusion), `k1qVBh5fnb.md` (3.40, latent diffusion planning), `PiHGrTTnvb.md` (3.00, closed-loop diffusion control — note one 10-rating outlier makes this noisy)
- Middle band (3.5–7.5): `CKqiQosLKc.md` (3.75, energy-based policies), `svp1EBA6hA.md` (6.50, CTRL — RL for diffusion conditioning), `o2uHg0Skil.md` (6.25, KL regularization in RL), `peNgxpbdxB.md` (6.00, discrete diffusion samplers)
- Strong band (>7.5): `pISLZG7ktL.md` (8.00, data scaling laws in IL), `8BAkNCqpGW.md` (8.00, POMDP policy gradient), `uKZdlihDDn.md` (7.60, latent diffusion for fluids), `9pW2J49flQ.md` (8.00, LTL in RL)

**Initial bracket**: The paper clearly sits between 5.0 and 7.0 — above the rejected weak-band papers (which have narrow scope or flawed reasoning) but below the 7.5–8.0 strong-accept papers (which are exceptionally clean methodologically).

**Round 2 (Narrowing)** — Two queries inside the bracket:
- `ldVkAO09Km.md` (6.50, DAC — KL-constrained diffusion policy for offline RL): Similar theoretical framing (KL-constrained policy iteration for diffusion policies), strong D4RL results. DIPOLE has a more novel decomposition and broader scope but less controlled evaluation. Comparable quality, slight edge to DIPOLE on originality.
- `tGQirjzddO.md` (6.33, LDCQ — latent diffusion for offline RL): DIPOLE's theoretical contribution (dichotomous decomposition, CFG connection) is stronger than LDCQ's incremental combination of BCQ + LDM.
- `svp1EBA6hA.md` (6.50, CTRL): RL for conditioning diffusion models. DIPOLE has stronger empirical evaluation on RL benchmarks and a cleaner theoretical derivation.
- `o2uHg0Skil.md` (6.25): KL regularization theory paper — different kind of contribution.

**Final score positioning**: The paper's contributions (clean theoretical decomposition, strong empirical results across 39 tasks, real-world AD scalability) place it at the upper end of the bracket, comparable to DAC (6.5) and CTRL (6.5). The rejection sampling confound and navtest fairness concern are real but do not invalidate the core contribution — they primarily weaken the clarity of the empirical conclusions, not the theoretical foundation. The paper would benefit from a cleaner controlled experiment but the core method is solid and broadly evaluated.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>