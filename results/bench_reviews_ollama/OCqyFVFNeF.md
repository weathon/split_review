## Summary
The paper observes that existing AND/OR interaction-based explanations of DNNs are under-determined: the decomposition $v(\mathbf{x})=v_{\text{and}}(\mathbf{x})+v_{\text{or}}(\mathbf{x})$ has a free parameter $\gamma_T$ per subset, and sparse extraction yields different interactions under different initializations or different DNNs. To address this, the authors define "generalizable interaction primitives" as those shared across $m$ DNNs trained for the same task (Definition 3.1) and propose a coupled optimization (Eq. 7) that uses a row-max + ℓ₁ penalty plus a shared/individual γ split and a bounded error term $\epsilon_T$. Experiments on BERT-base/large (SST-2), LLaMA/OPT (SQuAD), and ResNet-20/VGG-16 (MNIST "3 vs. not 3") report higher cross-model overlap than a per-model sparse baseline.

## Strengths
- The formal exposure of the ambiguity in the AND/OR decomposition via a single free parameter $\gamma_T$ per subset (Sec. 3.3) is a clean diagnosis of a real under-specification in prior interaction-explanation work, including a concrete toy Boolean example showing two valid decompositions of the same function.
- The redundancy short-cut analysis around Eq. 6→Eq. 7 (Sec. 3.3.2) — that a pure row-max penalty can hide mass in unselected entries — is a thoughtful observation, and the α-weighted ℓ₁ term is a sensible fix.
- Empirically, cross-architecture comparison (ResNet-20 vs. VGG-16) is the right shape of experiment, and the order-wise analysis in Fig. 5 (low-order interactions are more frequently shared) is a non-obvious finding worth keeping.

## Weaknesses

### Fatal
None that conclusively invalidate the paper, but the issues below collectively undermine its central empirical claim.

### Major
- **Headline metric is essentially what the loss optimizes.** Definition 3.1 measures generalization as $|\Omega_{\text{shared}}|/|\Omega^{(i)}|$, and Eq. 7 directly penalizes $\|\mathrm{rowmax}(\mathbb{I})\|_1$, which is minimized exactly when interactions overlap across the $m$ models. Reporting higher overlap against a baseline (Eq. 4) that has no cross-model coupling is structurally guaranteed and does not by itself demonstrate that the shared interactions are more *faithful* or more *primitive*. An independent test of faithfulness — held-out perturbations, transfer to a third model, downstream task usefulness, or human semantic judgment — is needed.
- **No null/control coupling baseline.** Because the decomposition has $2^n$ free parameters $\gamma_T^{(i)}$ per model plus a learned residual $\epsilon_T^{(i)}$, the formulation has enough degrees of freedom to find overlapping sparse structure in many settings. Running the same coupled loss on pairs of models trained for *different* tasks would test whether the discovered "shared" interactions are actually task-specific or are an artifact of joint optimization. This control is absent.
- **All experiments use $m=2$.** The framework's value proposition is intersection across many DNNs, but $m=2$ reduces $\bigcap_i \Omega^{(i)}$ to pairwise overlap and $\mathrm{rowmax}$ to a max of two values. The claim of extracting common task-level primitives is not tested in the regime that motivates the definition. Scaling to $m\ge 4$–5 with mixed architectures would substantially strengthen — or weaken — the contribution.
- **Universal matching is trivially preserved by construction and is presented as evidence.** With $v_{\text{and}}(\mathbf{x}_T)=0.5v(\mathbf{x}_T)+\gamma_T$ and $v_{\text{or}}(\mathbf{x}_T)=0.5v(\mathbf{x}_T)-\gamma_T$, $v_{\text{and}}+v_{\text{or}}=v$ holds for any $\gamma_T$; once $\epsilon_T$ is added with $|\epsilon_T|<0.02|v(\mathbf{x})-v(\mathbf{x}_\emptyset)|$, residual mismatch is absorbed by design. Reporting low matching error (Sec. 3.3.2/Fig. universal_matching) is therefore not informative about whether interactions are meaningful.

### Minor
- **The "image classification" claim overreaches.** Task 3 is binary "3 vs. not-3" on MNIST with a handful of pre-labeled important patches as input variables. The conclusion that ResNet/VGG "converge to ultimate interactions for a task" (Sec. 4) is far stronger than the setup supports.
- **No variance reporting.** No seeds, error bars, or input-sample variance for the generalization-power metric in Fig. 4, despite the paper itself motivating the work with the observation that different seeds yield 21% overlap (Sec. 3.3.1).
- **Sharing-decomposition prior ($\gamma_T^{(i)}=\bar\gamma_T+\hat\gamma_T^{(i)}$ with bounded $\hat\gamma$) is not ablated.** Forcing a shared mean $\bar\gamma$ mechanically increases cross-model overlap; isolating its effect from the row-max loss would clarify which component is doing the work.
- **The Occam's-razor argument for "sparsest = most faithful" is asserted, not justified.** Two models with similar inductive biases can share spurious sparse patterns; the paper conflates "non-arbitrary across models" with "faithful," and Sec. 3.2 does not engage with this.

### Trivial
- The bound $|\hat\gamma_T^{(i)}|<0.5\cdot\mathbb{E}|v-v_\emptyset|$ is loose relative to the full output magnitude; tighter ablations on this constraint would be informative but are not critical.

## Nice-to-Haves
- Side-by-side qualitative comparison of interactions where the coupled method and Traditional disagree, with at least informal human judgment about which is semantically coherent.
- A real image-classification setting (e.g., ImageNet subset) using a consistent input-variable scheme, rather than MNIST patches.
- An identifiability statement: under what conditions on $v^{(1)},\dots,v^{(m)}$ is the minimizer of Eq. 7 unique?

## Removed Points
*These points are flagged to be removed; treat them with caution.*
- "Theorem 3.2 footnote on p. 6 admits matching holds trivially" — kept in spirit under Major weakness above but the precise wording about "footnote on p.6" is a presentation nitpick.
- Generic strength-finder claims about "principled loss design" and "robustness to noise" were dropped because they essentially restate that the method exists and that the bounded $\epsilon_T$ absorbs residuals, which is in tension with the verified weakness that $\epsilon_T$ also weakens the universal-matching evidence.
- Strength about "consistent experimental evidence of improved generalization" was dropped/folded into a weakness because the metric is what the loss optimizes.

## Novel Insights
The cleanest novel observation is the explicit parameterization of the AND/OR ambiguity by a single scalar $\gamma_T$ per subset, which makes the under-determination of prior interaction-based explanations precise. Beyond this, the paper's substantive claim (that joint optimization recovers "common knowledge") is not independently validated, so no novel empirical insight survives the structural critique.

## Suggestions
- Add a different-task coupling control: jointly optimize Eq. 7 over (BERT-SST2, BERT-NLI) or (LLaMA, ResNet) and report cross-model overlap. If overlap is still much higher than Traditional, the metric is measuring the loss, not the models.
- Run at least one experiment with $m\ge 4$ DNNs spanning more than two architectures.
- Define and report an independent faithfulness criterion — e.g., predictive accuracy on held-out masked samples *for a third model not in the coupled set*, or perturbation-based necessity/sufficiency for the discovered interactions.
- Ablate the $\bar\gamma_T + \hat\gamma_T^{(i)}$ split and the $\alpha$ term separately to attribute the gain.
- Report variance across seeds and inputs in Fig. 4; the paper's own Sec. 3.3.1 motivates this.

---

**Axis-by-axis assessment.** *Originality:* the explicit $\gamma_T$ characterization and the cross-model coupling formulation are moderately novel. *Importance:* faithful, transferable concept extraction is a genuinely important question. *Claim support:* weak — the central claim ("more generalizable / more faithful") is shown by a metric the loss directly optimizes, with no independent validation, no $m>2$ regime, and no null control. *Soundness of experiments:* limited — three tasks but each with only two models, no variance reporting, and a toy MNIST setup labeled as "image classification." *Clarity:* the formal sections are clear; the experimental claims are over-generalized relative to evidence. *Value to the community:* the diagnosis of decomposition ambiguity is useful; the proposed remedy needs more convincing validation before it can be relied upon.

## Score and Decision
The paper makes a real contribution by formally characterizing the AND/OR decomposition ambiguity, but its central empirical claim — that joint optimization yields *faithful* generalizable primitives — is established with a metric the loss directly optimizes, against a baseline structurally guaranteed to lose, in the worst regime ($m=2$) for the underlying definition. This is a structural rather than incremental gap, but the formal contribution and the redundancy analysis still have value.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>