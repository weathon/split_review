## Summary
The paper proposes an Empirical Bayesian framing of existing group-robustness methods (JTT, LfF, DFR, SELF, etc.) as different choices of $\hat p(\theta)$ and $\hat p(g\mid x,\theta)$, and introduces *Learn from Known Unknowns* (LKU), which uses Dirichlet/evidential epistemic uncertainty $u(x)=K/S(x)$ as the empirical prior to reweight last-layer retraining. Experiments on Colored MNIST, Waterbirds, CelebA, MultiNLI, and CivilComments show competitive worst-group accuracy versus group-label-free baselines.

## Strengths
- Using evidential-deep-learning epistemic uncertainty as a cheap, no-group-label proxy for minority-group identification is a plausible and lightweight alternative to error-based heuristics like JTT (Section 4.2).
- The two-phase pipeline (evidential ERM → last-layer retraining only) is genuinely cheaper than methods like CnC or JTT that retrain from scratch (Section 5.4, "Computational and Memory Efficiency").
- The Colored MNIST demonstration (3.74% → 84.58% on the minority group while leaving majority groups largely unaffected, Section 5.3) is a clean controlled illustration of the mechanism.
- The qualitative GradCAM finding in Section 5.5 — high-uncertainty samples attend to spurious backgrounds while low-uncertainty samples attend to the bird — is a suggestive piece of evidence for the proposed mechanism.

## Weaknesses

### Fatal
None — the core empirical claim (uncertainty-weighted last-layer retraining gives competitive WGA without group labels) is plausibly supported, but several major issues weaken the framing.

### Major
- **Theorem 3.1 is disconnected from the proposed estimator.** Theorem 3.1 (Section 3.3) gives a Tweedie-style formula $\mathbb{E}[g\mid x,y,\theta]\approx \mathbb{E}[g] + \sigma^2 \partial_y \log p(y\mid x,\theta)$ that requires $y$ to be a continuous variable in an exponential family (so $\partial/\partial y$ is well-defined and $\sigma^2$ is meaningful). All experiments are categorical classification; the assumptions are asserted without justification for that setting. More importantly, the method in Section 4.2 simply *defines* $\hat p(g\mid x,\theta) := u(x) = K/S(x)$. Nothing in the paper shows this Dirichlet-uncertainty quantity approximates the Tweedie estimator or any object the theorem produces. The "theoretical guarantee" therefore guarantees nothing about the proposed method.
- **The "reduced hyperparameter tuning" claim is contradicted by the protocol.** The abstract and Section 4 emphasize reduced reliance on hyperparameter tuning, but Section 5.2 states: "We sample ten different hyperparameter configurations and select the best one based on validation performance" — for learning rate, the $\lambda$ annealing schedule, etc. This is the same regime as the criticised baselines. Furthermore, model selection uses the highest *average* validation accuracy, which is a poor proxy for worst-group accuracy and is not justified.
- **The retraining set already incorporates a JTT-style error-set heuristic, never ablated against the uncertainty signal.** Section 5.2: "The retraining samples are randomly sampled from the misclassified portion of the training set and the validation set." The pipeline therefore (i) restricts retraining to misclassified samples *and* (ii) reweights with $u(x)$. The paper attributes its gains to the uncertainty signal but never isolates these two factors. This is a serious confound for the headline claim.
- **The central mechanistic claim is asserted, not measured.** Section 5.5 states "Quantitative analysis showed correlations between uncertainty values and true group labels across all datasets" but reports no numbers — no AUC of $u(x)$ vs. minority-group membership, no correlation coefficient, no histogram split by true group. The single plot that would establish the method's premise is missing.
- **Conceptual issue with $\hat p(g\mid x,\theta) := u(x)$.** $p(g\mid x,\theta)$ should be a distribution over groups; $u(x)\in(0,1]$ is a scalar epistemic uncertainty, and $u(x)$ being high also fires on OOD, ambiguous, or label-noisy samples — not just minority-group samples. The paper does not argue why $u(x)$ is a better proxy for group membership than, e.g., loss (which JTT already uses). Combined with the missing quantitative correlation in §5.5, the mechanistic claim is under-defended.

### Minor
- The "Empirical Bayesian unification" is closer to a re-description than a unification: any reweighting/sample-selection scheme can be relabeled as a different $\hat p(g\mid x,\theta)$, and the framework yields no constraints on, or derivation of, the proposed $u(x)$. The paper would be more honest framing it as an interpretive lens rather than a primary contribution.
- Equation 2 (Section 3.1) writes $\mathrm{WGA}:=\min_g \mathbb{E}[\ell_{0-1}]$ — this is the worst-group *error*, not worst-group *accuracy*. The metric the entire paper rides on is mis-defined notationally.
- Equation 5 (Section 3.2) treats $p(g\mid x,\theta)$ as the quantity to estimate from a frozen ERM $\theta$, but the latent group $g$ is a property of $(x,y)$, not of $\theta$; the conditioning is muddled.

### Trivial
- Section 5.4 sentence "Learn from Known Unknowns consistently achieves worst-group accuracy across three datasets" appears to be missing a word ("the best"). (Plausibly a parser issue; ignore if not.)

## Nice-to-Haves
- Add a quantitative AUC (or histogram, or rank correlation) of $u(x)$ vs. true minority-group membership on each benchmark — the cleanest test of the mechanism.
- Add an ablation that decouples (a) restricting retraining to the misclassified subset, (b) evidence regularization, and (c) uncertainty reweighting; in particular, compare against JTT/AFR run on the *same* error-set retraining base so the only difference is the weighting signal.
- Either prove $K/S(x)$ approximates the Tweedie posterior under the paper's setting or drop the theorem and present the method as a direct empirical proposal.
- Make the explicit form of $\hat p(g\mid x,\theta)$ attributed to JTT/LfF/SELF/DFR in Table 1 readable in equation form, to substantiate the unification claim.
- Use group-labeled worst-group validation (as DFR/SELF disclose using) for model selection, or justify average-accuracy selection in a worst-group benchmark.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- *Harsh critic, Issue 5 (baseline coverage thinness, mention of CnC/SELF treatment).* This shades into evaluative judgment about what counts as state-of-the-art rather than a verifiable factual error in the paper, and the paper does engage with JTT/LfF/AFR/CnC explicitly.
- *Harsh critic, comments about Table 1 being "not parseable" and tables being "not legible."* These are parser artifacts, not paper defects.
- *Strength Finder, claim that the framework "cleanly interprets" prior methods.* Conflicts with the verified weakness that the framework is a re-description that imposes no constraints; the weakness wins.
- *Strength Finder, "theoretical result gives a formal justification."* Conflicts with the verified Theorem-vs-method disconnect; removed.
- *Strength Finder, generic "robustness across vision and language" item.* Kept implicit in WGA strength but removed as a standalone, generic point.

## Novel Insights
None beyond the paper's own contributions. The most genuinely novel observation across the reviews is the surfacing of the (a) misclassified-only retraining base + (b) uncertainty reweighting confound, which is a serious — but already implicit — methodological concern about how to credit the uncertainty mechanism.

## Suggestions
- Quantify $u(x)$ as a group-membership classifier (AUC or rank correlation per dataset) and report it; this is the single highest-leverage addition.
- Run an explicit ablation: ERM retraining on the misclassified subset (uniform weights) vs. + uncertainty reweighting vs. + evidence regularization, on Waterbirds/CelebA.
- Restate Theorem 3.1 honestly: either restrict it to a continuous latent treatment of $g$ and explain how $u(x)$ relates, or drop it and present LKU as an empirically motivated method.
- Fix the WGA definition (Eq. 2) and reconsider model selection by worst-group validation accuracy.
- Reframe the "unified framework" as an interpretive lens, since it does not derive the proposed estimator or constrain the design.

## Evaluation by axis
- **Originality:** Modest — using evidential epistemic uncertainty as a JTT-style group proxy is a sensible new combination, but neither the framework nor the theorem add genuine theoretical novelty.
- **Importance:** The group robustness without group labels problem is well-motivated.
- **Claim support:** Weak. The headline claim about uncertainty enabling group inference is asserted (§5.5) without quantitative evidence; the "less hyperparameter tuning" claim is contradicted by §5.2; the theorem is decorative.
- **Soundness of experiments:** Mixed. Reasonable benchmark coverage, but a JTT-style heuristic confound and average-accuracy-based selection cloud the results.
- **Clarity of writing:** Mostly readable; the framework section is muddled (Eq. 5 conditioning, WGA mis-definition, scalar-vs-distribution conflation in §4.2).
- **Value to community:** The lightweight evidential reweighting recipe is potentially useful, but in current form readers cannot tell what is doing the work.

## Score and Decision
The paper makes a plausible empirical proposal but its two flagship contributions — the Bayesian unification and the Tweedie-style theoretical guarantee — do not survive scrutiny, and the central mechanistic claim is unmeasured while a JTT-style heuristic is silently bundled in. With a rebuilt theoretical story, a clean ablation, and quantitative validation that $u(x)$ correlates with group membership, this could become a solid paper.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>