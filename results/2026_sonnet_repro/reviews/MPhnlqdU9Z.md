Now let me do the calibration search. First, let me search for similar papers.Let me read some anchors to calibrate more precisely:Round 1 bracket: **4.0 to 6.0**. The paper is clearly above the 3.0 range (has novel concept + multi-domain empirical study), but below the 6.5+ range (lacks theoretical rigor, circularity concern). Let me narrow within this bracket.Now I have sufficient calibration to write the review. Let me compose the final assessment.

---

## Summary

This paper introduces *monitorability* as an intrinsic neural network property — the capacity of a model's internal activations to reveal inference errors at runtime — and proposes the MIRA Score to quantify it. MIRA is computed by applying FGSM perturbations to in-distribution data, measuring the Mahalanobis-based chi-square surprisal of the resulting penultimate-layer features, and integrating this over a range of perturbation magnitudes. Since no ground-truth monitorability signal exists, the authors validate MIRA against the best achievable OoD detection performance (max AUROC across ODIN, Mahalanobis, and Energy scoring) across vision, tabular, and NLP architectures.

---

## Strengths

- **Genuine novelty in concept and formalization.** Definition 1 is the first formal definition of monitorability as an intrinsic NN property — parameterized by layer, loss function, and threshold — clearly separating it from inference accuracy and detector-specific performance (Section 3.2). The paper correctly identifies that equally accurate models can differ in monitorability (Figure 1, toy dataset).

- **Practical, self-contained metric.** MIRA (Eq. 4) requires only in-distribution data and fast FGSM perturbations. The chi-square surprisal normalization (Eq. 3) is a principled dimension-calibration step that makes the score unbounded and independent of layer dimensionality.

- **Multi-domain empirical validation.** Experiments across CIFAR-10/100 (4 architectures), a tabular benchmark (5 models), and NLP fine-tuning (4 transformer models) all show a preserved rank ordering between MIRA and the best achievable AUROC. This consistency across modalities is a genuine empirical contribution.

- **Feature-space visualizations.** The t-SNE plots in Figure 2 provide intuitive qualitative corroboration: higher MIRA corresponds to more compact, well-separated cluster structure in penultimate activations. This is independent evidence that the metric tracks something real about representation structure.

---

## Weaknesses

### Fatal
None.

### Major

- **Structural evaluation circularity.** MIRA is derived from Mahalanobis distance in penultimate feature space (Eq. 3–4). The validation proxy — "best achievable OoD detection" — is the maximum AUROC across ODIN, Mahalanobis, and Energy scoring. Inspecting Tables 1–3, Mahalanobis detection dominates: it is bolded (as the best method) for virtually every model in the tabular experiments (Table 2, all five models) and NLP experiments (Table 3, all four models), and is the plurality winner in vision (Table 1). The best-of aggregate is therefore almost always the Mahalanobis AUROC. This means MIRA (Mahalanobis-based) is being validated against a proxy that is itself dominated by Mahalanobis performance. A model that produces Gaussian-distributed features will naturally score high on both MIRA *and* Mahalanobis detection, explaining the observed correlation through shared mathematical structure rather than through the usefulness of monitorability as an independent concept. The authors should either exclude Mahalanobis from the proxy and show the correlation holds with ODIN and Energy alone, or explicitly acknowledge this structural dependency and argue why it does not impair the evaluation.

- **No quantitative correlation analysis.** The paper claims MIRA "correlates with" the best achievable OoD detection performance, but no Spearman rank correlation, Kendall's τ, or statistical test is reported anywhere. With 4 models (CIFAR-10 vision), 5 (tabular), and 4 (NLP), the sample sizes are small. The qualitative statement "higher MIRA = higher AUROC" could mask a modest or unstable relationship. For a *metric paper* whose central empirical claim is a correlation between MIRA and detection performance, the absence of any quantitative correlation statistic is a significant gap.

### Minor

- **Formal definition disconnected from metric.** Definition 1 is binary: a model is *l-monitorable* if there *exists* a set Z^l satisfying a biconditional. The MIRA Score (Definition 2) is a continuous real value. The paper itself acknowledges "Definition 1 provides an abstract formalization of monitorability, but it does not quantify how monitorable a neural network is." However, it never provides even an informal argument that a higher MIRA Score implies a "tighter" or "more robust" Z^l, or that crossing some MIRA threshold implies l-monitorability in the sense of Definition 1. The definition functions as philosophical motivation rather than a scaffold for the metric, which weakens the claim of "theoretical grounding."

- **Technical imprecision in Definition 1.** The paper states that for cross-entropy loss, the threshold ε must satisfy ε < log(C) to ensure L(f(x), y) ≤ ε implies a correct prediction. But cross-entropy L = −log p_y, so L ≤ ε implies p_y ≥ e^{−ε} > 1/C. This ensures the true class has above-random probability but does **not** guarantee the argmax is y — the model could still assign higher probability to a wrong class. The condition is necessary but not sufficient for guaranteed correct prediction.

- **Unexplained MIRA scale divergence across domains.** MIRA values span −0.07 to 89 in vision, 4 to 63 in tabular, and 2015 to 3793 in NLP. Section 3.3 states the surprisal normalization removes dimension dependence, but the cross-domain discrepancy is enormous (~40× between NLP and vision). This suggests the normalization is only partially effective, which limits the claim that MIRA provides a principled cross-architecture measure.

### Trivial

- Table 1 omits CustomNet from CIFAR-100 experiments without explanation, creating an asymmetry relative to CIFAR-10 (4 vs. 3 models).

---

## Nice-to-Haves

- Repeating the validation with *only* ODIN and Energy-based detectors (excluding Mahalanobis entirely) would be the most impactful addition — it would directly test whether MIRA generalizes beyond its own mathematical family.
- Reporting Spearman rank correlations (with the data already in hand from Tables 1–3) would substantially strengthen the "MIRA correlates with detection performance" claim.
- An experiment holding architecture constant while varying training procedure (loss function, regularization) — to show that models of equal capacity can differ in MIRA — would decouple monitorability from general model capacity and make the contribution more distinct.
- An informal proposition connecting higher MIRA to a "tighter" Z^l in the sense of Definition 1 would close the gap between the formal definition and the continuous metric.

---

## Removed Points

*These points are flagged for removal; treat them with caution.*

- **Harsh Critic: "RQ3 argument is self-defeating."** The critic argues that if Mahalanobis fails on Places365 for DenseNet but MIRA (Mahalanobis-based) still gives DenseNet a high score, the detector-agnostic claim is undermined. However, MIRA is a model-level pre-deployment metric integrating over FGSM perturbations on ID data — it does not measure per-OoD-dataset detection, so one dataset where Mahalanobis underperforms does not contradict MIRA's score. The argument is a strawman; removed.

- **Harsh Critic: "Model capacity confound."** The critic notes that larger/more capable models score higher on both MIRA and AUROC, potentially making MIRA redundant with architectural priors. While raising an interesting research question, there is no evidence in the paper that model capacity alone predicts the ranking (e.g., the tabular results show WideMLP beating DeepMLP, which is not obviously a capacity ordering). Retained only as a nice-to-have suggestion, not a weakness.

- **Strength Finder: "MIRA is detector-agnostic."** The paper makes this claim, and the point is partially valid, but the circularity concern (Mahalanobis dominates the "best-of" proxy) conflicts with a strong version of this strength. Removed as a standalone strength; folded into the circularity concern.

- **Strength Finder: "Empirical correlation is convincing across models."** This is partially invalidated by the circularity weakness. Retained in weakened form as a supporting observation, not a headline strength.

---

## Novel Insights

The paper's central insight — that monitorability is an *intrinsic* model property distinguishable from accuracy and from the performance of any single detector — is genuinely novel and practically important. The use of FGSM perturbations as a probe of decision-boundary sensitivity, rather than as an adversarial attack, is a creative application of existing tools. The observation that models with equivalent classification accuracy (Figure 1) can differ dramatically in feature-space separability for anomalous inputs opens a meaningful direction for pre-deployment model evaluation. The main open question the paper raises but does not resolve is whether monitorability, as captured by MIRA, is truly independent of "how Gaussian-distributed are the features" — answering this would consolidate the theoretical contribution considerably.

---

## Suggestions

1. Re-run the validation proxy using only ODIN and Energy-based scoring (drop Mahalanobis) and report whether MIRA still predicts the ranking. If it does, the circularity concern is resolved empirically.
2. Add a table of Spearman rank correlations between MIRA and average AUROC, computed separately for each domain.
3. Correct or clarify the cross-entropy threshold condition in Definition 1 — ε < log(C) is necessary but not sufficient for guaranteed correct prediction.
4. Provide an informal argument or proposition connecting higher MIRA to a "more useful" Z^l as in Definition 1.
5. Add a brief discussion explaining the cross-domain MIRA scale discrepancy (NLP values ~2000–3800 vs. vision ~0–89).

---

## Evaluation on Key Axes

- **Originality:** High. First formal definition of monitorability; novel application of adversarial perturbations as a measurement probe rather than an attack.
- **Importance of research question:** High. Pre-deployment assessment of monitoring potential is practically relevant for safety-critical systems.
- **Claims well-supported:** Moderate. The rank ordering is observed qualitatively across domains, but the evaluation is structurally circular and lacks quantitative correlation statistics.
- **Soundness of experiments:** Moderate. Multi-domain coverage is a strength; the evaluation proxy design is a real weakness.
- **Clarity of writing:** Good. The paper is clearly organized and the motivation is well-presented.
- **Value to research community:** Moderate-to-high as a concept paper; the validation gaps prevent it from being a definitive empirical result.

---

## Score and Decision: Calibration

**Round 1 bracket: 4.0–6.0**

Retrieved anchors:
- `/home/wg25r/.../l5ouuojPGe.md` (avg 3.0, Round 1): Threshold optimization for NN monitoring — empirical study only, no formal definition, rejected. MIRA is clearly stronger than this (novel concept, formal definition, multi-domain).
- `/home/wg25r/.../eN0RyRVbSm.md` (avg 6.5, Round 1): OoD risk + double descent — has theoretical bounds via Random Matrix Theory, broader experiments. Stronger theoretical grounding than MIRA. MIRA is weaker on validation rigor.
- `/home/wg25r/.../hlijRgXTDK.md` (avg 4.75, Round 2): "Pathologies of OoD Detection" — critical analysis paper, proposes no new method, rejected due to limited originality. MIRA is more original (first formalization).
- `/home/wg25r/.../CHGcP6lVWd.md` (avg 6.2, Round 2, Accepted): "Energy-based Automated Model Evaluation" — proposes a novel metric for evaluating models without labels, similar framing to MIRA. Validated across modalities. Accepted at 6.2. Weaknesses include method similarity to existing uncertainty estimation and limited real-world evaluation.

**Round 2 narrowing:** MIRA is more original than hlijRgXTDK (4.75) — it proposes something new rather than just critiquing existing work. Compared to CHGcP6lVWd (6.2), MIRA's circularity concern is more severe: the validation proxy is almost entirely dominated by Mahalanobis, which shares the mathematical family of MIRA itself. CHGcP6lVWd, despite its weaknesses, has a cleaner validation setup (predicting classifier accuracy on unlabeled shifted data, a distinct signal from the energy score). The absence of quantitative correlation statistics in MIRA further widens this gap. MIRA sits below CHGcP6lVWd (6.2) and is somewhat above hlijRgXTDK (4.75).

**Final score: 5.0** — the paper introduces a novel and practically relevant concept with multi-domain empirical support, but the structural circularity in the evaluation and the absence of quantitative correlation analysis are real methodological gaps that prevent a confident acceptance recommendation at this stage.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>