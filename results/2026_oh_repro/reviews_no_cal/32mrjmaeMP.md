## Summary
The paper proposes **TAK**, a training-time regularizer for task-vector fine-tuning that aims to improve **task arithmetic** (addition/negation) by discouraging cross-task **representation drift**. The key idea is to rewrite a drift objective (under model linearization) into a quadratic form involving a Jacobian Gram/GGN-like matrix, then approximate it efficiently with **KFAC**, and further propose an **accumulated Kronecker heuristic** to make the regularizer’s cost constant in the number of tasks.

## Strengths
- **Clear technical route from drift regularization to a tractable curvature surrogate.** The intro frames drift as a Jacobian Gram/GGN object and motivates KFAC as a structured approximation (“The Jacobian Gram matrix is an instance of the generalized Gauss-Newton… we adopt KFAC…” in Sec. 1; and the method section’s Eq. (7)/(8) + Algorithm 1 operationalize it).  
- **Practical efficiency analysis and artifact/compute budgeting.** The paper quantifies the one-time cost to estimate curvature factors (“estimating all KFAC matrices for the 8 Vision tasks (128 examples per task) takes only 4 minutes,” Training costs) and studies estimation/compression tradeoffs (Fig. 7: examples/MC samples; storage vs accuracy).
- **Evidence that the constant-complexity accumulation heuristic is usually close to the idealized multi-task formulation.** Table 3 explicitly compares “Exact” vs “MC=1 (ours)” and the text discusses where the gap appears (notably ViT-B/32) and why (“smaller architectures tend to be more sensitive…”).

## Weaknesses

### Fatal
None.

### Major
- **“Dataless” is overstated/misalleading given the method requires task data to build KFAC.** The abstract claims “a dataless approach” and the introduction states the goal is to work “without requiring access to the training data,” but the paper later relies on *task datasets* for curvature estimation and studies how many examples are needed: Fig. 7 varies “#examples (MC=1) (2 to 128)” and the text states “using 128–256 examples is already sufficient to saturate performance” and that KFAC estimation for 8 tasks uses “128 examples per task” (Training costs; KFAC estimation).  
  *Why it matters:* This is central framing (title/abstract) and affects the claimed practicality/privacy/modularity advantage. As written, it reads like “no task data required,” whereas the actual benefit is closer to “no **cross-task** data access during regularization once per-task curvature stats are computed.” The paper hints at this “shared instead of the data” framing (Intro), but the headline wording remains too broad.

- **The paper’s mechanistic claim (“weight disentanglement” / reduced interference) is only weakly validated beyond improved merged accuracy, and the main probe is not independent of the regularizer.** The key mechanistic evidence is “task localization” via the Jacobian score \( \|J_\theta f(x,\theta_0)\tau_t\|_2^2 \) (Fig. 5 and the surrounding text: “With our regularization (Eq. (3)), these scores are indeed forced to remain low…”).  
  *Why it matters:* Because the regularizer is explicitly designed around this linearized/Jacobian-based quantity (derivation around Eq. (7) and the Jacobian term), demonstrating separation in exactly the same metric risks circularity: it shows the penalty does what it penalizes, but does not directly quantify *behavioral* interference (e.g., how adding task \(j\) harms task \(i\) performance across pairs) as the mechanism for improved task arithmetic. The paper gestures to a “complementary analysis in the non-linear fine-tuning regime… in App. F.5” (text after Fig. 5), but in the main body the mechanistic support remains mostly tied to the same Jacobian notion used in the method.

### Minor
- **The accumulated Kronecker heuristic is not uniformly reliable across architectures, but the practical guidance is limited.** The paper notes that for ViT-B/32 there is “a small but consistent gap in favor of the idealized training objective” (Table 3 discussion) and attributes this to architecture sensitivity.  
  *Why it matters:* Since constant-in-#tasks complexity is a headline benefit, users would benefit from clearer criteria/diagnostics for when the approximation is safe vs when storing per-task factors (or using the exact multi-task objective) is warranted.

- **Monte Carlo sampling behavior is surprising and under-explained.** The KFAC estimation section reports: “only a few samples per example (1–2) are sufficient… Surprisingly, performance deteriorates beyond this point, with variance across seeds increasing as the number of MC samples grows” (KFAC estimation, Fig. 7a discussion).  
  *Why it matters:* This is a concrete, counterintuitive empirical finding that affects recommended settings; some explanation/diagnosis would increase trust in the estimator/implementation and help practitioners choose MC budgets.

### Trivial
None.

## Nice-to-Haves
- Add a **behavioral interference matrix** experiment: for many task pairs \((i,j)\), measure task \(i\) performance drop when adding \(\tau_j\), with/without TAK; optionally correlate improvements with the localization score to connect mechanism to real behavior without using the same metric as the objective.
- Include an ablation replacing KFAC with a **diagonal/identity** curvature surrogate to isolate how much of the gain comes from “curvature structure” vs “generic quadratic penalty.”

## Removed Points
These points are flagged to be removed, treat them with caution:
- **“Comparisons are unfair because TAK is training-time while ISO/TSV/TIES are post-hoc.”** The paper already frames these as complementary and even mentions applying merging techniques to TAK-produced checkpoints (“optional: merge KFACs, Eq. (8)” in Algorithm 1; and discussion that TAK makes simple summation competitive). Without a specific, demonstrable apples-to-oranges claim in the paper text (e.g., a stated theorem or headline that directly equates them under identical training), this remains more of a framing preference than a concrete methodological error.
- **Speculation about linearization vs non-linear regimes being “unclear” as a flaw.** The paper explicitly states it demonstrates applicability “in linearized and non-linear regimes” (conclusion) and references an appendix analysis for non-linear localization. Without pinpointing a specific incorrect claim that relies on linearization while only non-linear evidence is provided, this is not retained as a substantive weakness.

## Novel Insights
The strongest risk to the paper’s impact is not raw performance but **credibility/expectation management**: the work is best interpreted as an approach that replaces *cross-task data access during regularization* with *a small, per-task curvature artifact* (potentially shareable), rather than being “dataless” in the ordinary sense. Tightening this framing would also make the paper’s longer-term vision—shipping extra training-time statistics (like KFAC factors) alongside model weights—feel like a coherent systems contribution rather than an overclaimed privacy story.

## Suggestions
- Rename/rephrase throughout (title/abstract/intro) to something like **“no cross-task data at regularization time”** or **“data-free regularization given per-task curvature factors”**, and explicitly state the per-task requirement (e.g., “KFAC estimated from ~128 examples per task”).
- Add one main-body experiment that directly measures **cross-task interference in task performance** (not Jacobian scores), ideally across many task pairs, to substantiate “disentanglement” as behavior rather than only as the linearized sensitivity quantity.

## Score and Decision
Originality: high (curvature/KFAC view for TA disentanglement + accumulated Kronecker heuristic).  
Importance: moderate-to-high for modular adaptation / task arithmetic practice.  
Claim support: good on performance/efficiency; weaker on headline “dataless” framing and mechanistic disentanglement evidence.  
Experimental soundness: generally solid with good efficiency studies; one counterintuitive MC result needs explanation.  
Clarity: mostly clear, but key terminology (“dataless”) is currently misleading.  
Community value: high if reframed accurately; could become a practical recipe for producing merge-friendly task vectors.

MY FINAL SCORE: <score>6.5</score>  
MY FINAL DECISION: <decision>Accept</decision>