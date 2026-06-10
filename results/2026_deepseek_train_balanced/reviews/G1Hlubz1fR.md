Here is my synthesized final review:

---

## Summary

This paper proposes C-Poly, an extension of Polytropon (Poly) for parameter-efficient multi-task learning. C-Poly separates modular adapters into **task-common skills** (shared across tasks) and **task-specific skills** (exclusive per task), with a learned allocation matrix combining both per task. The mathematical formalization is clean, and the design intent — reducing negative transfer by giving each task dedicated capacity while still sharing — is well motivated.

---

## Strengths

- **Clean mathematical formalization that sharply distinguishes C-Poly from prior MoE-PEFT methods.** Equation 1 and Table 1 explicitly contrast the architectures: prior methods (MoLoRA, Poly, MHR) use only a task-common summation Σ wᵢᵗ φᵢ(xᵗ), while C-Poly adds the explicit task-specific term wᵗ φᵗ(xᵗ). The allocation matrix decomposition in Equation 2 further formalizes the block-diagonal structure of W_B. This provides a concrete basis for understanding what is new.

- **Ablation on (A, B) combinations under a fixed total parameter count** (Section 3.4). The paper acknowledges the design trade-off between common and task-specific capacity and reports that both components are needed — excessive task-specific allocation can cause overfitting. This analysis gives practitioners useful guidance, though it only explores within C-Poly variants, not across methods.

- **Parameter efficiency analysis** (Figure 6, described in Section 3.3) showing C-Poly outperforming other PEFT methods under varying parameter magnitudes. The explicit separation is genuinely a more efficient use of parameters for multi-task settings, if the gains can be confirmed with proper controls.

---

## Weaknesses

### Major

- **The central experimental comparison is confounded by a large parameter count mismatch.**  
  The paper states (line 189) that the design was chosen "to ensure a comparable number of training parameters across all methods." This is false. Baselines (Poly, MHR, MoE-LoRA) use **4 total LoRA adapters** with rank r=2. C-Poly uses **A + T×B = 3 + T adapters** (since B=1 per task). For SuperGLUE (T=7), that is 10 adapters (2.5× the baseline); for SuperNI (T=100), it is 103 adapters (~26× the baseline). All adapters have the same rank (r=2), so the parameter multiplier is direct.  

  This confound alone could explain C-Poly's superior performance: the method has 2.5× to 26× more tunable adapter parameters than anything it is compared against. The pattern of results is actually consistent with this — the largest gains appear where the parameter advantage is largest (SuperNI T5-Large: +5.10; SuperGLUE GLM-10B: +5.27), and on the one setting where C-Poly has the largest parameter advantage (SuperNI FLAN-T5-Large, ~26× more adapters), it *loses* to MHR on rouge1 (68.84 vs. 68.69), consistent with the idea that capacity alone does not determine performance but that the comparison is nonetheless unfair.  

  The paper's narrative cannot be accepted without a controlled comparison where C-Poly and the baselines use a matched total parameter budget (e.g., give Poly/MHR 3+T adapters, or restrict C-Poly to 4 total adapters by sharing the task-specific adapters differently).

- **Single-epoch training with one random seed and no variance reporting.**  
  All models are trained for exactly 1 epoch (line 191). No standard deviations, confidence intervals, or multiple-run averages are reported. The Gumbel-sigmoid sampling (Equation 3) and random uniform draws introduce inherent stochasticity. With a single epoch and no repeated trials, every numerical difference between methods is a point estimate with unknown variance, making it impossible to assess which differences are reliable. At a top venue, this is insufficient.

### Minor

- **The paper claims "constant improvement over all sub-tasks" (line 208) but the data contradict this.**  
  On FLAN-T5-Large / SuperGLUE (Table 2), C-Poly underperforms the best baseline on 3 of 7 sub-tasks: CB (85.71 vs. 87.50), COPA (90.00 vs. 91.00), and WSC (75.00 vs. 76.92). The overall average is higher (83.21 vs. 82.31), which is a reasonable aggregate claim, but "constant improvement over all sub-tasks" is factually incorrect. Similarly, the paper states C-Poly "achieved optimal performance... on the SuperNI datasets" (line 255) while C-Poly's rouge1 on FLAN-T5-Large/SuperNI (68.69) is below MHR (68.84). These overclaims should be corrected.

- **The claimed "explicit separation" of task-specific skills is only partially enforced.**  
  The paper initializes W_B as a unit diagonal matrix but then states that "entries off the diagonal are also subject to potential updates" (line 155). While the paper frames this as a beneficial side-effect (allowing cross-task routing without modifying the exclusive skill parameters), it means the claimed separation is only an initialization bias, not a structural guarantee. If off-diagonal weights grow large, a task could primarily route through another task's "exclusive" adapter, weakening both the interpretability claims and the stated motivation. The paper should either enforce diagonal-only W_B or clarify the design as "MoE with per-task dedicated experts + cross-task routing."

- **Qualitative clustering analysis without quantitative metrics.**  
  Section 3.4 presents dendrograms comparing task hierarchies learned by C-Poly vs. Poly, claiming "a more balanced task hierarchy" (line 313). No quantitative cluster metrics (silhouette score, purity, etc.) are provided. The interpretability benefit is asserted but not measured.

### Trivial

- The paper says "In total, there are |Φ_A| + T × |Φ_B^t| = A + T × B adapters" (line 73) — but then does not reflect this in the experimental design, leading to the confound above. At minimum, this parameter count consequence should have been acknowledged and discussed.

---

## Nice-to-Haves

- Repeat experiments with multiple random seeds and report variance to establish statistical reliability of the reported differences.
- Compare against baselines with matched total adapter counts (e.g., 3+T adapters in an MMoE configuration) to isolate the benefit of the architectural separation from the benefit of additional capacity.
- Evaluate zero-shot generalization to held-out tasks, a key promise of modular methods that is not tested here.
- Provide quantitative metrics (silhouette score, etc.) for the task-clustering analysis.

---

## Removed Points

- **"AdaMix baseline missing"**: Removed per the rule that missing related works should not be mentioned without external verification that the work exists and should have been cited.
- **"No code release"** and **"hyperparameter underspecification"**: Removed per rules about reproducibility nitpicks and code release.
- **"Typos/formatting artifacts (e.g., \ru in Eq. 3)"**: Removed per rule that parser artifacts should not be treated as author errors.
- **"Generic weakness about 100/1600 tasks being a small fraction"**: This is a generic scope concern that applies to most benchmark sampling; removed as not a specific identified flaw that harms the core claim.
- **"Strength: consistent empirical gains across benchmarks"**: Removed because this strength conflicts with the verified parameter-count confound weakness. The gains may simply reflect more capacity.
- **"Strength: interpretable skill hierarchies"**: Downgraded from a kept strength to mentioned under Minor weaknesses, because the analysis is purely qualitative with no quantitative supporting metrics.
- **"The paper does not acknowledge the reversal on SuperNI FLAN-T5-Large rouge1"**: Absorbed into the Minor weakness about overclaiming (merged with the "constant improvement" issue).

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel observation about the method or problem that the paper itself does not make.

---

## Suggestions

1. **Redo the main experiments with controlled total parameter budgets.** The cleanest fix: give each baseline (Poly, MHR, MoE-LoRA) the same number of adapters that C-Poly uses (3+T), distributed as an MMoE with T+3 shared experts. If C-Poly still outperforms baselines at equal parameter counts, the architectural contribution is validated.
2. **Report means and standard deviations over at least 3 random seeds.** If computational constraints are severe, justify single-run results with a variance analysis on a subset.
3. **Correct the factual overclaim on line 208** ("constant improvement over all sub-tasks") and the claim on line 255 about "optimal performance" on SuperNI.
4. **Clarify whether W_B off-diagonal updates are intentional or accidental.** If intentional, re-frame the method accordingly and explain the design rationale.

---

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>