## Summary
The paper analyzes state-space models (SSMs) through the lens of Hankel-operator theory, using Hankel singular values as a diagnostic for SSM expressiveness. Building on this lens, the authors propose HOPE, a parameterization of LTI layers via the Markov parameters of a finite Hankel matrix (rather than $(\mathbf{A},\mathbf{B},\mathbf{C})$), and prove it is almost-surely high-rank and globally perturbation-stable. Empirically, HOPE-SSM trains stably from random init, exhibits non-decaying memory within a length-$n$ window on noise-padded sCIFAR, and is benchmarked on the Long-Range Arena.

## Strengths
- **A genuine unifying lens for SSM training pathologies.** Connecting initialization and training difficulties to Hankel-singular-value decay (Sec. 3, Fig. 2–3) and invoking ROM/Adamyan–Glover bounds gives a principled, quantitative diagnostic that explains why both random init and HiPPO-LegS can be expressiveness-bottlenecked when the LTI is trained.
- **A sharp dual pair of theorems.** Theorem 3.1 shows high-rank LTI systems are scarce in $(\mathbf{A},\mathbf{B},\mathbf{C})$-space (rank scales as $n^\beta$ with $\beta<1$), while Theorem 4.1 shows the opposite under HOPE: a random Hankel parameterization is almost-surely $\Omega(n)$-rank. This is a non-trivial structural insight, not just a re-skinning of prior work.
- **Global, parameter-free perturbation bound.** Theorem 4.2 ($\|G-\tilde G\|_\infty \le \sqrt n \|\mathbf h-\tilde\mathbf h\|_2$) is in contrast to the parameter-dependent bound in Theorem 3.2 (which scales with $|b_jc_j|/|\mathrm{Re}(a_j)|^2$), and operationally justifies training without learning-rate scaling or log-reparameterization. Experiment I empirically corroborates this (Fig. 4).
- **Efficient implementation with fewer parameters.** Algorithm 1 evaluates the transfer function on a nonuniformly resampled $z$-grid in $\tilde{\mathcal O}(L+n)$ time, matching S4/S4D complexity while using $n$ (vs. $3n$) parameters per LTI block.
- **Variable-length-friendly parameterization.** By keeping the continuous-time system and discretizing with a trainable $\Delta t$, HOPE retains the variable-sequence-length property that direct-kernel parameterizations lack.

## Weaknesses

### Fatal
None.

### Major
- **Finite, hard-cutoff memory is sold as "non-decaying" without an honest accounting.** Section 4 / Eq. (8) and Experiment II emphasize that $|\overline{\mathbf{H}}_{0,t}| = \mathbf{h}_t$ does not decay for $t<n$, but the paper itself acknowledges $\overline{\mathbf{H}}_{0,t}=0$ for $t\ge n$. The suggested remedy (shrink $\Delta t$) just rescales the time axis — the total continuous-time memory window remains $n\Delta t$. So HOPE replaces an exponentially-decaying-but-unbounded memory with a finite hard cutoff. Which is preferable is task-dependent; the paper should quantify the trade-off (e.g., effective memory of S4D/S5 at matched compute vs. $n\Delta t$) rather than framing the comparison as strict improvement.
- **The diagnostic in Section 3 and the gains of HOPE are not isolated by ablation.** Section 3 attributes S4D weaknesses to (a) rank collapse and (b) parameter perturbation sensitivity. HOPE is presented as fixing both, but no experiment isolates which mechanism drives the LRA/noisy-sCIFAR gains (e.g., S4D with rank-preserving init alone, or with Wang & Xie 2023-style stability reparam alone, at matched compute). Without this, the empirical advantage is consistent with the Hankel story but not uniquely attributable to it.
- **Section 3's causal language outruns the evidence.** The text consistently says the Hankel SV histograms "explain" downstream accuracy, but the evidence is correlational across three init schemes (Fig. 2–3). Theorem 3.1's assumptions (diagonal $\overline{\mathbf A}$ with i.i.d. entries on the unit disk, $\overline{\mathbf B}\circ\overline{\mathbf C}^\top$ Gaussian) describe a random init no one actually uses; concluding from it that "high-rank systems are scarce in S4D parameter space" overgeneralizes from the i.i.d. case to the trained regime.

### Minor
- **Theorem 3.2(b) tightness is worst-case, not typical-case.** The lower bound exhibits *some* perturbation realizing the bound, not that typical SGD updates exhibit this sensitivity. The supporting Fig. 4 uses adversarial random perturbations of fixed relative magnitude, not actual gradient steps; tying the bound to observed gradient-step deltas would strengthen the link to "training instability."
- **Finite-matrix rank vs. operator rank.** Theorem 4.1 is a statement about the $n\times n$ random Hankel matrix, but the LTI HOPE instantiates extends the kernel with zeros beyond $n$. The numerical rank of the finite matrix and the rank of the implied operator on $\ell^2(\mathbb N)$ under zero-extension are related but distinct; the text could be more precise.
- **Bounds in Theorem 3.2 and Theorem 4.2 are not in the same units.** Theorem 3.2 perturbs $(\mathbf A,\mathbf B,\mathbf C)$; Theorem 4.2 perturbs $\mathbf h$. The headline contrast is intuitive but not a direct apples-to-apples comparison; framing them as such risks overselling the gap.
- **Experiment II compares only against S4D.** Liquid-S4, S5, Mamba, Spectral SSM are all mentioned in the introduction as long-memory targets; including at least one as a baseline on noisy-sCIFAR would substantially strengthen the long-memory claim.
- **Per-task analysis on LRA is missing.** Long-memory claims would be more credibly supported by a per-task breakdown on Path-X / Pathfinder / ListOps than by averages.
- **Hyperparameter / budget reporting for LRA baselines.** If LRA baseline numbers are taken from prior papers under their own tuning while HOPE-SSM was tuned in-house, a brief note on matched budgets would help readers calibrate the comparison.

### Trivial
None substantive.

## Nice-to-Haves
- Apply the Hankel-rank diagnostic to selective/time-varying SSMs (e.g., Mamba) — the paper invokes them in the intro but stays in LTI land. Even a discussion of why the Hankel lens does/doesn't extend would be valuable.
- Direct experimental comparison with kernel-parameterized models (since with $\Delta t=1$ HOPE is exactly a length-$n$ zero-padded kernel) would clarify where the gains come from beyond resampling.
- Quantify total effective memory $n\Delta t$ vs. effective memory of competing SSMs at matched compute on a task where the trade-off bites.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"HOPE-SSM row is missing from Table 1, so the headline claim is unverified."** The parsed table is missing the HOPE-SSM row (only baselines visible), but the surrounding text and caption indicate the row exists in the submission; this is a parser artifact, not an authorial omission. Per the hard rules on formatting/parser issues, removed.
- **"HOPE-SSM is not meaningfully distinguished from direct-kernel parameterizations (Fu et al. 2023)."** The paper explicitly addresses this in Related Work: HOPE parameterizes the underlying continuous-time system and discretizes with a trainable $\Delta t$, enabling variable-length inputs; a direct-kernel method does not. The addressal is reasonable, so this is downgraded to a nice-to-have (direct empirical comparison would still strengthen the paper).
- **"Theorem 4.2 is just the obvious $\sqrt n$ bound, not as strong as framed."** The bound is elementary, but it is the *parameter-independent* nature (no dependence on $\|h\|$, pole locations, or magnitudes) that the paper uses — that claim is correct as stated. Removed.
- **"Comparison is against weakest baselines (S4/S4D)."** Table 1 in fact includes S5, Liquid-S4, Reg. S4D, Spectral SSM, DSS, and S4++. Removed as factually mistaken in framing.
- **Strength: "important problem / unified explanation"** as written by the Strength Finder — superficial framing kept only when backed by concrete evidence (which I did above).

## Novel Insights
The dual statement that high-rank LTI systems are *scarce* in $(\mathbf A,\mathbf B,\mathbf C)$-space yet *generic* in Markov-parameter space is a clean and non-obvious observation, and it ties the long-standing reliance on HiPPO/log-scale reparameterization to a single quantitative signal (Hankel SV decay). The framing of every prior init/training trick as "an effort to avoid fast-decaying Hankel SVs" is a useful unifying perspective for the SSM literature.

## Suggestions
- Run an ablation training S4D with a rank-preserving init and/or Wang–Xie-style stability reparam alone, vs. HOPE, under matched compute, to isolate which advantage drives downstream gains.
- Add at least one modern long-memory baseline (S5, Liquid-S4, or Spectral SSM) on the noise-padded sCIFAR experiment.
- Frame the memory claim as "constant-magnitude memory inside a length-$n\Delta t$ window, zero outside," and analyze the regimes where this is/isn't preferable to exponentially decaying unbounded memory.
- Compare empirical sensitivity to actual gradient-step perturbations (not just adversarial random perturbations) to support the "S4D training is numerically unstable" claim.
- Report a per-task LRA breakdown with seed variance and clarify whether baseline numbers used matched hyperparameter budgets.

---

**Axis evaluation.** *Originality:* the Hankel-operator viewpoint and Markov-parameter parameterization are original within the SSM literature. *Importance:* understanding init/training pathologies of SSMs and obtaining stable-training/long-memory parameterizations is a meaningful question. *Claim support:* core theoretical claims are supported; the "non-decaying memory" claim is partially overstated relative to its finite-window reality; the LRA/noisy-sCIFAR results support the parameterization but lack isolating ablations. *Experimental soundness:* adequate on LRA, but Experiment II's single-baseline comparison and the absence of mechanism-isolating ablations are limitations. *Clarity:* generally clear; the connection between Theorem 3.2 (parameter-space units) and Theorem 4.2 ($\mathbf h$-space units) should be stated more carefully. *Community value:* the Hankel diagnostic is a useful tool the community can reuse independently of HOPE itself.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>