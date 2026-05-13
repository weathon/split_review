## Summary
PEARL trains LLMs to be robust to demonstration order in in-context learning by formulating fine-tuning as a distributionally robust optimization (DRO) problem over the set of permutation-induced distributions. A "P-Net" parameterizes a distribution over permutations via entropy-regularized Sinkhorn + Gumbel sampling and is co-trained adversarially with the LLM to mine hard orderings. Experiments on synthetic linear-function ICL and instruction tuning on Super-NaturalInstructions show worst-case performance gains over ERM and several baselines.

## Strengths
- **Clean technical mechanism for adversarial permutation mining.** Casting hard-permutation generation as differentiable OT via Sinkhorn + Gumbel (§4.2, Eqs. 11–12) is a principled way to search a combinatorial $n!$ space without enumeration, and is directly responsible for the empirical gains.
- **Substantial worst-case improvements on the controlled setting.** On synthetic linear regression ICL, worst-case normalized MSE drops from 0.0142 (ERM+CL) to 0.0049 at 3 shots (Table 1), and the worst-case gap continues to grow with more shots — a credible signal because the synthetic setup permits direct measurement of worst-case behavior.
- **Defense gain on instruction tuning.** On Llama-3-8B with Super-Natural Instructions, worst-case ROUGE-L improves 14.2–29.4% over ERM across 2–4 shots (Table 2), and PEARL is complementary to inference-time methods (additional 3–5%).
- **Correct positioning relative to prior work.** §2 accurately characterizes order-optimization and output-calibration approaches as not fundamentally addressing inherent robustness, motivating a training-stage solution.

## Weaknesses

### Fatal
None.

### Major
- **The threat-model metric (ASR, Eq. 1) is relative-drop only, which inflates the headline 80% number.** ASR is $(\mu_i - \omega_i)/\mu_i \ge \delta$, with no floor on $\mu_i$. Because ROUGE-L on generation tasks frequently produces very small $\mu_i$, samples that the base model cannot really do receive arbitrarily large relative drops from any perturbation. The paper does not report an absolute-drop threshold or a $\mu_i$ floor, so the "almost imperceptible … 80% success rate" claim conflates "model is weak on this sample" with "permutation attack succeeded." The motivation in §3, abstract, and Figure 1 all rest on this metric.
- **DRO formalism does not match the algorithm.** §4.1 defines the ambiguity set $\mathcal{Q}$ as the convex hull of distributions obtained by applying *one* permutation $\Pi$ to all of $\hat{P}$ (Eqs. 7–8). The sup of a linear functional over a convex hull is attained at a vertex, so this formal problem reduces to finding a single $\Pi$ worst on average. The actual P-Net (§4.3) instead picks a *per-instance* worst permutation, which corresponds to a strictly larger (per-example) ambiguity set. The DRO derivation therefore does not justify the algorithm being run; the gap should be acknowledged and either the formalism tightened or the algorithm framed against the broader per-instance ambiguity set.
- **The "neural search attack" used to motivate the threat is the same architecture/training procedure as PEARL's P-Net.** §3's neural attacker and §4's defender are the same object, so neural-attack defense numbers in Figure 4 are partially circular. The exhaustive-search columns in Table 2 partially mitigate this for the worst-case metric, but cross-attacker robustness (independently trained adversary, black-box order search) is not evaluated.
- **Missing the obvious enumerate-all-permutations ERM baseline.** Since $n \in \{2,\dots,5\}$, all $n!$ ($\le 120$) permutations are tractable per example. ERM+DS samples only one permutation per epoch, and ERM+IM is mixup, neither of which matches "uniform coverage of the ambiguity set." Without this control, one cannot conclude that adversarial mining beats dense uniform augmentation — which is the central methodological claim.
- **The "hundreds of LoRA updates" efficiency framing omits the P-Net cost.** The P-Net is FLAN-large (§6.1), trained jointly. Compute should be reported as P-Net + LLM update FLOPs/wall-clock vs. a compute-matched ERM (e.g., ERM trained on randomly sampled permutations for the same budget). The current framing materially understates training cost.

### Minor
- **Figure 2 illustration mismatches the instruction-tuning setup.** It depicts ERM concentrating mass on training-seen permutations of a fixed $(p,x,y)$, but in instruction tuning each example has its own demonstrations; the "seen vs. unseen permutation per example" picture is not what ERM actually does at scale.
- **Soft vs. hard permutation in training is not specified.** §4.2 introduces Gumbel-Sinkhorn with temperature $\tau$, but it is unclear whether the $\Pi$ applied to demonstration embeddings during LLM training is the soft doubly stochastic matrix or a hard sample. Soft mixing of demonstration embeddings is not a permutation and changes what the LLM is being made robust to.
- **No variance/significance reporting** in Tables 1–2 across seeds or across permutations, despite worst-case being inherently a tail statistic. A bootstrap or seed-level standard deviation would strengthen the claims.
- **Convergence claim in §4.3 is unsupported.** "At convergence, the P-Net represents a uniform distribution" is asserted but neither proven nor diagnosed empirically; minimax dynamics frequently fail to converge.
- **Entropy term framing is loose.** The element-wise term $\sum_{ij}\Pi_{ij}(1-\Pi_{ij})$ pushes $\Pi$ toward $\{0,1\}$, i.e., toward a hard permutation — fine — but the prose ("prevents trivial uniform matrices that dilute semantic content") conflates this with a different concern.
- **Held-out evaluation is narrow** (4 of 17 tasks). Acceptable as a sanity check, but a held-out-task split this small limits generalization claims.

### Trivial
- Eq. 17 reads $\arg\max_\theta$ for what the surrounding text describes as the LLM minimization step. Should be $\arg\min$.

## Nice-to-Haves
- Cross-attacker generalization: evaluate against an independently trained P-Net (different seed/architecture) and a gradient-free black-box order search.
- Re-report §3 with an absolute-drop threshold and a $\mu_i$ floor (e.g., only samples with $\mu_i \ge 0.3$) so the 80% headline is interpretable.
- Examples / qualitative analysis of which permutations the P-Net selects (e.g., whether it consistently buries the most relevant demo).
- Compute-matched ERM baseline (e.g., random-permutation augmentation for the same wall-clock as PEARL).
- Convergence diagnostics for the P-Net distribution over training.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- *§3 worst-over-$n!$ is a "biased lower-bound estimator."* — Misleading: at $n \le 6$, $n!$ is small and the paper does evaluate exhaustively. The bias-of-min concern is real only at the level of variance reporting, which is already captured in the Minor tier.
- *"Adding demonstrations is a double-edged sword conflates context-length effects with order sensitivity."* — Within scope: §3 measures both average and worst-case under the same shot count, which isolates order from context length.
- *Curriculum learning is the wrong synthetic baseline.* — ERM+CL is the standard baseline in the Garg et al. linear-regression ICL setup that §5 explicitly follows; using it is appropriate. The missing enumerate-all baseline (already kept in Major) is the substantive version of this concern.
- *Strength: "Identifying the gap between worst-case and average … is well-motivated."* — Generic framing strength; folded into the technical-mechanism strength.
- *Strength: "Thorough empirical motivation."* — Largely overlaps the ASR-metric concern; if the metric is shaky, the motivation is too. Kept implicitly via the synthetic-setting strength.

## Novel Insights
None beyond the paper's own contributions. The genuinely novel idea is the use of Gumbel-Sinkhorn as an adversarial permutation generator co-trained with an LLM under a DRO framing — this is the paper's own contribution rather than a meta-observation.

## Suggestions
- Re-define ASR with both a relative threshold and an absolute-drop floor; restrict the headline number to samples with non-trivial baseline performance.
- Either tighten the DRO ambiguity set to per-instance permutations (and re-derive) or change the algorithm to match the convex-hull formulation in §4.1.
- Add an "all-permutation uniform augmentation" ERM baseline at matched compute.
- Add cross-attacker evaluation: independently trained P-Net (different init/architecture) and a black-box order search.
- Report seed/permutation variance in Tables 1 and 2; report total training compute including P-Net.
- Clarify whether the LLM sees soft Sinkhorn matrices or hard permutation samples; if soft, justify why this still constitutes order robustness.
- Fix the $\arg\max \to \arg\min$ in Eq. 17 and add a P-Net convergence plot.

---

**Axis evaluation.** *Originality:* high — first DRO-over-permutations formulation with a Sinkhorn-based differentiable permutation miner for ICL. *Importance:* well-motivated; permutation sensitivity is a real and acknowledged ICL failure mode. *Claim support:* mixed — the worst-case metric on the synthetic setup is convincing; the threat-model framing rests on a problematic ASR metric, the DRO theory does not match the algorithm, and the strongest baseline (uniform permutation augmentation) is missing. *Soundness of experiments:* adequate scale but no variance, narrow held-out split, partial circularity in the neural attack evaluation. *Clarity:* generally clear; some notational/derivational gaps. *Value to community:* the Sinkhorn-based adversarial permutation generator is reusable and likely to influence subsequent ICL-robustness work.

Net: a real contribution with a clean technical core, but the headline threat metric, the theory–algorithm mismatch, the missing uniform-augmentation baseline, and the misleading efficiency framing are substantive issues that should be fixed before acceptance.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>