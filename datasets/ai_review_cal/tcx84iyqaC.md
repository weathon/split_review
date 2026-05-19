- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5
Now I have all the information needed to produce the final consolidated review.

---

## Summary

This paper documents "reward collapse" in RLHF reward model training — the observation that, during the terminal (interpolating) phase, the distribution of learned rewards becomes independent of the prompt. The authors show that this arises from the ranking-based objective decoupling into identical per-prompt optimization problems, characterize the limiting reward distributions in closed form for several utility families (Beta distributions, probability mass at endpoints), and propose prompt-aware utility functions that break the symmetry. Experiments on a controlled synthetic dataset (reward = response length) demonstrate collapse under fixed utilities and mitigation under prompt-aware ones.

---

## Strengths

1. **Theoretical prediction with closed-form characterization** — Section 2.1 derives that optimizing a fixed ranking-based utility yields prompt-independent reward distributions in the interpolating regime. Theorems 1–3 provide exact Beta distributions (as a function of a single parameter \(\gamma\)) and endpoint mass for several utility families. This analytical control goes well beyond prior empirical observations of reward model behavior and gives practitioners principled knobs to shape reward distributions.

2. **Prompt-aware optimization as a principled alternative to early stopping** — Rather than relying on the "somewhat arbitrary" heuristic of early stopping (cited as the default mitigation in InstructGPT), Section 2.2 proposes adapting the utility function to the prompt's open-endedness and provides three parametric families whose limiting distributions are fully characterized. This reframes the problem from "when to stop" to "which utility to use," which is a conceptually cleaner approach.

3. **Extension to pairwise comparisons with a consistency guarantee** — Theorem 4 (Section 5) generalizes the framework to the Bradley-Terry-Luce setting, proving that the optimal rewards preserve the order of underlying scores and are Lipschitz in score differences. This shows the approach is not limited to full rankings and maintains theoretical guarantees under a more practical data model.

4. **Clean controlled experimental design** — Section 3.1 constructs a synthetic dataset where ground-truth reward (response length) is known and controllable, with 8 responses per prompt and two clearly separated length distributions. This design cleanly isolates the collapse phenomenon from the noise and confounds of real preference data, allowing unambiguous attribution of the observed collapse to the optimization objective.

---

## Weaknesses

### Fatal
None.

### Major

1. **No quantitative evaluation — all claims rest on visual inspection** — The paper contains zero tables of numerical results. Reward collapse and its mitigation are demonstrated solely through reward distribution plots (Figures 1–4). No distributional distance metric (e.g., KL divergence, Earth Mover's Distance) is computed to quantify how much the reward distributions of different prompt types diverge under fixed vs. prompt-aware utilities. No statistics such as confidence intervals, standard deviations, or multiple-seed runs are reported. This makes it impossible for a reader to assess whether the observed "collapse" and "mitigation" are significant, reproducible, or merely visually suggestive.

2. **No experimental comparison to early stopping despite claiming superiority** — The paper mentions early stopping as a "rudimentary strategy" and "somewhat arbitrary" (line 35) and later claims its method is "superior to early stopping" (line 354). However, no experiment compares the prompt-aware method against early stopping (e.g., train to different stopping points and compare reward distribution shape, or measure downstream performance). Without this comparison, the claimed advantage over the default mitigation strategy is unsupported.

3. **Mismatch between theoretical assumptions and experimental utility functions** — The convergence theory (Theorem 4, Lemma 4.1) assumes \(U\) is strictly or strongly concave. However, one of the primary experimental utility functions is \(U(x)=x\) (linear, not strictly concave). The paper uses \(U(x)=x\) to empirically illustrate polarized reward distributions (line 215: "employing \(x\) as the \(U\) function results in a polarized reward distribution"), but does not address whether the theoretical predictions apply to this function or why the empirical match is expected despite the assumption violation. This gap weakens the claimed connection between theory and experiment.

### Minor

4. **Manual selection of utility function per prompt** — In the experiments, prompts are pre-split into "open-ended" and "concrete" categories and \(U=x\) and \(U=-1/x\) are manually assigned accordingly. The paper acknowledges this as future work ("developing a method to choose a utility function based on prompts… poses an intriguing avenue for further exploration," line 358). While this does not invalidate the theoretical contribution, it means the proposed mitigation pipeline is incomplete as presented — a practitioner would need to solve the prompt-classification problem to deploy it.

5. **No ablation testing the core theoretical mechanism** — The theory predicts that collapse arises from overparameterization (interpolation). A natural and direct test would be to train reward models of varying capacity (small to overparameterized) and measure whether collapse weakens as capacity decreases. This experiment is absent. Similarly, the paper does not study how the number of responses per prompt \(n\) (only \(n=8\) is used) affects the degree of collapse, despite the theory being asymptotic in \(n\).

6. **No downstream RLHF evaluation** — The reward model trained with prompt-aware utilities is never used to fine-tune an LLM. The paper therefore cannot demonstrate that avoiding reward collapse improves generation quality, calibration, or any practically relevant metric. The practical motivation (better LLM alignment) remains untested.

### Trivial
7. Theorem numbering inconsistency: the harsh critic refers to "Theorem 5" but the paper's numbering is Theorem 4 for the BTL consistency result.

---

## Nice-to-Haves
- A more automated method for choosing the utility function \(U_\prom\) from the prompt text (e.g., based on estimated response entropy or topic diversity), rather than manual category assignment.
- Quantitative distributional distance metrics (KL divergence, EMD) with confidence intervals.
- An experimental check: early-stop the reward model at various points and compare the reward distribution shape to the prompt-aware method's output.
- Vary model capacity (e.g., DeBERTa-small vs. large) to test whether collapse depends on overparameterization as the theory predicts.

---

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **Missing citation of reward overoptimization literature (e.g., Gao et al. 2023)** — Removed per rule: "DO NOT mention missing related works, as you do not have external sources to confirm their existence and could be making things up."

2. **"The paper does not use human-written preferences" / "no real RLHF pipeline" framed as fatal** — Downgraded from fatal to minor (point 6). The paper explicitly scopes itself as a controlled investigation of a phenomenon in reward model training. Demanding a full RLHF pipeline is outside this scope; acknowledging it as a limitation (as the authors do in Section 6) is appropriate.

3. **"Speculative claim about GPT-4 calibration"** — The paper's footnote says "we suspect… although we are unable to verify" — this is properly caveated speculation, not an unsubstantiated claim. Removed as a misunderstanding of the paper's hedging.

4. **"Cannot be independently verified" / reproducibility concerns about cited entities** — Removed per hard rule: all cited models, datasets, and tools are assumed to exist as of the review date.

5. **Pure formatting nitpicks** — Removed per hard rule: parser artifacts are not author errors.

---

## Novel Insights

A genuinely novel observation emerging from the combination of the two reviews is that the paper's theoretical machinery (decoupling the per-prompt optimization problem under overparameterization) makes a sharp, testable prediction that was not tested: collapse severity should vary monotonically with model capacity, disappearing at low capacity where interpolation fails. The absence of this experiment is a significant missed opportunity to validate the core causal mechanism. Conversely, the decoupling argument itself — that a shared reward model trained on rankings inevitably converges to prompt-independent reward distributions in the interpolation regime — is a clean conceptual contribution that reframes reward model training dynamics in a way that existing work on reward overoptimization (which treats collapse as a consequence of overfitting or proxy misspecification) does not.

---

## Suggestions

1. Add a table reporting a quantitative metric (e.g., Wasserstein-1 distance between the reward distributions of open-ended and concrete prompts) for each utility function, with standard deviations across multiple random seeds (at least 3–5 runs). This would transform the evaluation from suggestive to rigorous.
2. Run an early-stopping baseline: train to several checkpoints and compare the reward distribution shapes and the distance metric — this is a low-cost experiment that would either support or undermine the claimed superiority over early stopping.
3. Train reward models of varying capacity (e.g., DeBERTa-V3-small vs. -base vs. -large) under a fixed utility and measure collapse severity to test whether overparameterization is the causal mechanism, as the theory predicts.
4. Address the \(U(x)=x\) inconsistency in the main text: explain whether the theory's concavity assumption is necessary or whether the predictions are robust to linear utilities.
5. Provide a simple proof-of-concept for automatic prompt classification (e.g., measure response length variance from a few LLM samples per prompt to estimate open-endedness, or use a small classifier) to make the method more actionable.

---
