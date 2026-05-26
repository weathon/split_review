Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

---

## Summary

The paper proposes ZNet, a deep learning method that learns instrument (Z) and confounder (C) representations from observed covariates X by optimizing a multi-part loss designed to enforce the three standard IV conditions (relevance, exclusion restriction, unconfoundedness). The learned representations can then be plugged into downstream IV estimators (TSLS, DeepIV, DFIV) for causal effect estimation. The paper evaluates ZNet across ten semi-synthetic data-generating scenarios spanning linear/non-linear relationships and various instrument existence conditions (disjoint, mixed, latent, no candidate).

## Strengths

- **Comprehensive and structured empirical evaluation.** The paper evaluates ZNet across 10 distinct data-generating settings (4 DGP classes × linear/non-linear, plus no-U variants) with 3 downstream IV estimators, comparing against 4 baseline methods (AutoIV, VIV, GIV, TARNet) and the ground-truth instrument (TrueIV). This breadth is a genuine step beyond prior work in the IV-generation subarea.

- **Strong ablation study establishing necessity of each loss component.** Figure 5(c) independently ablates each of the three IV constraints and shows that every one degrades instrument recovery (R² for predicting true instrument X15 drops from ~0.84 to 0.30 when unconfoundedness is ablated, ~0.36 when exclusion restriction is ablated, ~0.33 when relevance is ablated, and ~0.05 when all are ablated). This empirically validates that the multi-objective design is not gratuitous.

- **Consistent competitive ATE estimation.** In Table 1, ZNet achieves the best or runner-up ATE error in the majority of settings. In several challenging no-candidate settings (where no observed variable is a valid instrument), ZNet+DeepIV produces the best ATE estimates, supporting the claim that learned proxy instruments can reduce confounding bias.

- **Demonstrated recovery of latent categorical instruments.** Figure 4 shows near-perfect recovery of a 5-cluster latent categorical instrument via ZNet representations, connecting the method to an important use case (e.g., provider-based instruments in healthcare).

## Weaknesses

### Major

- **Lemma 1 proof is mathematically flawed, undermining the theoretical justification for the unconfoundedness loss.** The proof in Section 3 contains the step  
  `E[Z·E[e_Y|X,T]] = E[Z]·E[e_Y|X,T]`.  
  This is incorrect: the left side is a deterministic scalar, the right side (with E[e_Y|X,T] a random variable) is dimensionally inconsistent. Tracing through correctly: since Z = g(X) is X-measurable, E[Z·E[e_Y|X,T]] = E[E[Z·e_Y|X,T]] = E[Z·e_Y], so Cov(Z, e_Y − E[e_Y|X,T]) = E[Z·e_Y] − E[Z·e_Y] = 0 *automatically* under the stated conditions (E[Z]=0, Z=g(X)). The premise of Lemma 1 is therefore tautological and the lemma does not provide a non-trivial link between the covariance of Z with residuals and Cov(Z, e_Y)=0. This breaks the claimed theoretical chain justifying L_{Z↔ε_Y}^{PC}. The empirical approach may still be reasonable as a heuristic, but the paper's argument that it "enforces" unconfoundedness via Lemma 1 is not supported.

- **The loss functions enforce unconditional (or at best marginal) covariance constraints, while the IV conditions require conditional independence.** The paper defines unconfoundedness as Z ⟂ e_Y | C and exclusion restriction as Z ⟂ Y | C, T (through C). The losses enforce Cov(Z, e_Y)=0, Cov(C,Z)=0, and PC(C,Y)>0 — i.e., unconditional or pairwise correlations. The paper provides no argument that zeroing these unconditional covariances implies the required conditional independences. The footnote on p.2 notes that the paper aims to construct Z and C to be "independent" (the losses only enforce zero pairwise correlation), which still falls short of conditional independence given C. The Discussion's claim (p.9) that "solutions to the ZNet loss minimization problem will always give a representation that serves as an instrument since IV constraints are explicitly embedded in the loss function" overstates what the loss terms actually guarantee. The method should be framed as using covariance-based heuristics that empirically approximate the IV conditions, not as theoretically enforcing them.

- **The loss term MSE(C, Y) in Equation (7) is underspecified for multi-dimensional C.** C is described as a learned representation with dimensionality set by hyperparameter, while Y is a scalar. The paper does not specify how MSE(C, Y) is computed when C has more than one dimension — whether C is projected to a scalar, whether the MSE is summed or averaged across dimensions, or whether C is effectively constrained to be one-dimensional. This ambiguity affects reproducibility of the training objective.

### Minor

- **Architecture does not fully match the claimed SCM.** The paper's SCM states T = ψ'(C, Z) + e_T (p.3), yet the ZNet architecture (Figure 3) learns π(Z) → T with no C → T pathway during representation learning. The network π takes only Z as input. The paper argues that the decorrelation loss L_{Z↔C}^{PC} forces Z to absorb all T-relevant information and C to capture Y-relevant information, but this is an indirect workaround rather than a principled encoding of the SCM. Adding a C → T pathway (or explaining why it is unnecessary) would strengthen the connection between architecture and claimed causal model.

- **ZNet sometimes outperforms the ground-truth instrument without discussion.** In several settings (e.g., Linear Mixed DeepIV: ZNet 0.381 vs TrueIV 0.429; Non-linear No Candidate DFIV: ZNet 0.049), ZNet beats TrueIV. The paper presents this as straightforward validation but does not discuss likely mechanisms (e.g., the learned composite instrument may be stronger than any individual observed candidate, or ZNet's representations may provide regularization). Since "beating the oracle" could also raise concerns about confounding leakage in the evaluation, the paper should explicitly address this pattern.

- **In no-U (no unobserved confounding) settings with no candidate instrument, ZNet+DeepIV outperforms TARNet**, which is the statistically appropriate estimator when there is no unobserved confounding. The paper says ZNet "is comparable to TARNet" (p.8), but the results show ZNet clearly better (e.g., Linear No Candidate no-U: TARNet −0.169 vs ZNet DeepIV −0.033; Non-linear No Candidate no-U: TARNet −0.068 vs ZNet DeepIV −0.012). While not a fatal anomaly, this merits explanation — is DeepIV simply a more powerful estimator, or do the learned representations provide beneficial regularization?

- **The choice between Pearson Correlation and Mutual Information constraints is tuned per dataset via Bayesian optimization without a default configuration or principled selection rule.** This makes the method incompletely specified as presented (the reader does not know under what conditions to prefer PC or MI).

### Trivial

- The caption of Table 1 truncates "DFIV" to "DF IV" inconsistently.

## Nice-to-Haves

- **Ablation on downstream ATE, not just instrument recovery.** Figure 5(c) ablates constraints and measures instrument recovery (R² for predicting true instruments), but showing the effect on downstream ATE error would more directly connect the ablation to the paper's main claim of improved causal effect estimation.

- **Explicit acknowledgment that the unconfoundedness check in Figure 6(c) (correlation with U) is only possible in semi-synthetic data.** The paper acknowledges this implicitly by using synthetic data for evaluation, but a clear statement that this check is unavailable in real-world applications would appropriately calibrate expectations.

## Removed Points

The following points from the reviewers are removed with justification:

- *Criticism that the "unconfoundedness check requires U which is unknown in real settings" is presented as a weakness.* **Removed:** The paper evaluates on semi-synthetic data precisely so that U is known, which is standard practice. The paper does not claim this check is possible in real data.

- *Criticism that hyperparameter search for PC vs MI is left unspecified.* **Moved to Minor** (above) with a weakened framing — it is a specification gap, not a fatal design flaw.

- *Criticism about the paper claiming to "relax assumptions" about U influencing X.* **Removed:** The paper explicitly states the standard assumption that observed variables are not influenced by U (p.3, line 85), and Lemma 1 is an attempt to relax this. Whether it succeeds is addressed in the Major weakness above, but the critic's specific framing mischaracterizes the paper's stated position.

- *"The test for unconfoundedness checks correlations with U — in real settings U is unknown, so this check is not available."* **Removed:** This is true by definition and the paper never claims otherwise. The evaluation uses semi-synthetic data exactly so that this check can be performed.

- *Style/formatting nitpicks, speculation about missing proofs in the appendix, and comments about what "at the time of writing" is or is not released.* **Removed** per policy.

## Novel Insights

None beyond the paper's own contributions. The reviews did surface one genuine analytical finding not fully articulated in the paper: the Lemma 1 proof error means the unconfoundedness loss lacks the claimed theoretical foundation, and the method's success relies on heuristic covariance minimization rather than a provable guarantee. This reframing — from "enforcing IV conditions" to "learning representations via empirically motivated covariance constraints" — would make the paper more honest and still preserve the value of its empirical results.

## Suggestions

1. **Fix or remove Lemma 1.** If the lemma can be correctly proved with additional assumptions, do so. If not, honestly reframe the unconfoundedness loss as a heuristic covariance penalty without claiming theoretical guarantees via Lemma 1.
2. **Reframe the paper's claims about enforcing IV conditions.** Replace "enforces" and "always gives a representation that serves as an instrument" with language like "encourages" or "empirically approximates." Explicitly acknowledge the gap between unconditional covariance constraints and conditional independence requirements.
3. **Specify the computation of MSE(C, Y) and PC(C, Y)** for multi-dimensional C in Equation (7).
4. **Add a discussion section** addressing the "beating TrueIV" and "outperforming TARNet in no-U" results. Provide plausible mechanisms.
5. **Consider adding a C→T pathway** to the architecture during representation learning, or justify theoretically why the decorrelation approach suffices without it.
6. **Provide a default configuration** for PC vs MI constraints, or clearer guidance on when each is appropriate.

## Score and Decision

The paper tackles an important problem (automated instrument construction for causal inference) and presents an extensive empirical evaluation that demonstrates competitive performance. However, the theoretical foundation has a significant flaw (Lemma 1 proof error) and the paper's central claims about "enforcing" IV conditions and "always" producing valid instruments are not supported by the presented theory. The loss terms are covariance-based heuristics that empirically work well, but the framing overstates what is guaranteed. A major revision that corrects the theoretical claims, fixes the Lemma 1 issue, and clarifies the ambiguous loss specification could result in a strong paper. In its current form, the gap between the claims and the evidence is too wide for acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>