## Summary
The paper proposes RedGrape, a federated long-tailed learning method that performs classifier re-balancing on clients during local training by mixing local real samples (for classes with ≥T local examples) with server-aggregated global gradient prototypes (for missing classes). A second supplementary classifier $\widehat{W}$ is added during training and the two heads' logits are summed, in order to mitigate the optimization conflict introduced by simultaneously training under the long-tailed local distribution and re-balancing $W$.

## Strengths
- **Reasonable critique of CReFF and a clean mechanism**: The intuition that abundant real local samples are a stronger signal than server-synthesized pseudo-features is sensible, and the mixed mechanism (real data ≥ T, otherwise fall back to a shared global gradient prototype) is a natural way to handle locally-missing classes (Sec. 3.3.1, Fig. 3 with $T=\infty$ showing large degradation).
- **Two-head ablation is informative**: Fig. 4 ("Ours w/o Extra Classifier") shows that re-balancing $W$ locally without the auxiliary head $\widehat{W}$ converges to a worse optimum, providing concrete evidence that the two-stream design matters in practice.
- **Empirical gains across IR and participation regimes**: Tables 1–2 report consistent improvement over FedAvg, Fed-Focal, Ratio Loss, CLIMB, and CReFF on MNIST-LT, CIFAR-10-LT, CIFAR-100-LT at IR=10/50/100 in both full and partial participation, and Fig. 2 shows faster convergence on CIFAR-10-LT.

## Weaknesses

### Fatal
None.

### Major
- **The "no extra server requirements" / privacy framing is overstated.** The abstract and Sec. 4.2 positions RedGrape as needing "no extra requirements on the server" relative to CReFF, but the algorithm itself requires each sampled client to compute and send $\{g^{pro}_{W^{t-2},k,c}\mid c\in\mathcal{L}_k\}$ (Eq. 10–11), and the server must aggregate and broadcast a global gradient prototype *per class per round* (Eq. 15). This (i) is a non-trivial communication overhead — 100 per-class gradient vectors per client per round on CIFAR-100-LT — that is not quantified anywhere, and (ii) exposes each client's local label set $\mathcal{L}_k$ and class-conditioned gradients. Class-conditioned gradients (especially over tail classes where $|\mathcal{D}_{k,c}|$ is small) are precisely the regime in which gradient-inversion attacks are strongest. Since CReFF's privacy posture is explicitly used to motivate RedGrape, the absence of any communication-cost or privacy analysis weakens the central pitch.
- **Eq. 13's update rule is a heuristic, not a derivation from Eq. 6.** The Lagrangian formulation in Eq. 6 is invoked to justify combining $g^{local}$ and $g^{bal}$, but the actual update introduces an *ad-hoc* norm-matching factor $\|g^{local}\|/\|g^{bal}\|$ with a fixed $\lambda$ (Eq. 13). The justification given ("$g^{pro}$ is a constant, its scale must follow the decreasing scale of real gradients") is reasonable as engineering but is not what Eq. 6 prescribes. The paper should either (a) state Eq. 13 honestly as a heuristic with empirical justification (and study sensitivity to $\lambda$ and to the norm-matching schedule), or (b) provide a derivation linking the Lagrangian to the rescaled gradient sum.
- **The ablation does not isolate the claimed mechanism.** Fig. 4's "Ours w/o Extra Classifier" simultaneously removes $\widehat{W}$, the additive-logits training scheme, and the regularization effect of an over-parameterized head. It supports "two-head helps" but does not specifically show that the *contradictory optimization* explanation (Sec. 3.2) is the correct one; a sequential decoupled baseline (FedAvg representation then local re-balancing of $W$ only) or a logit-adjustment-style baseline would isolate the mechanism much better.

### Minor
- **Threshold $T$ is dataset-tuned (8 for MNIST/CIFAR-10-LT, 2 for CIFAR-100-LT).** Fig. 3 shows non-trivial sensitivity. The mechanism is thus a different blend (mostly real data on CIFAR-100, mostly mixed on CIFAR-10) across datasets; this should be acknowledged as a hyperparameter with practical implications, and Fig. 3-style sweeps should be reported for CIFAR-100-LT as well.
- **Federation scale and non-i.i.d. strength are mild.** Experiments use N=10 (full participation) or 50 with 10 sampled, and Dir($\alpha=1$). The local-class-missingness phenomenon that motivates global gradient prototypes is much more severe under Dir(0.1) or Dir(0.05) and N≥100; results under stronger non-i.i.d. would strengthen the motivation.
- **No head/medium/tail accuracy breakdown.** For a long-tailed paper, overall accuracy alone makes it hard to verify that gains come from tail-class improvement rather than head-class preservation.
- **Sensitivity to $\lambda$ is not reported.** $\lambda$ is described as fixed; a sweep would clarify whether the heuristic in Eq. 13 is brittle.

### Trivial
None substantive (formatting artifacts disregarded).

## Nice-to-Haves
- An empirical reconstruction-attack study (or DP-style analysis) on the gradient-prototype channel to either substantiate or refute the implicit privacy claim.
- A direct sequential-decoupling baseline (FedAvg representations + local classifier re-balancing only) to test the joint-training framing.
- Communication cost broken down per round and per dataset vs. CReFF; this directly bears on the "no extra requirements" claim.
- Evaluation on a larger long-tailed FL benchmark (e.g., a federated split of ImageNet-LT or iNaturalist) with a contemporary backbone.

## Removed Points
These points are flagged to be removed; treat them with caution.
- *"Contradictory optimization is mathematically incoherent / Eq. 6 not solved."* Partially overlaps with the Major point on Eq. 13 being heuristic, which is the substantive part. The deeper "the contradiction is not removed, only shared" framing is interpretive — the paper does propose a concrete mechanism (combined logits + selective gradient on $W$) and the claim that $\widehat{W}$ absorbs head-class bias is at least empirically tested via Fig. 4. Kept the heuristic-derivation criticism; removed the stronger "structurally incoherent" framing as overreach.
- *"Unfair comparison to CReFF because no hyperparameter search reported for baselines."* Tuning $T$ for one's own method while using published baseline settings is standard; this asymmetry is not enough to count as a real weakness.
- *"Comparing only on small datasets."* MNIST/CIFAR-10/CIFAR-100-LT at IR=10/50/100 with two participation regimes is the standard evaluation suite established by CReFF and prior FL-LT work; criticizing it as "toy" is a generic complaint rather than a defect of this paper. Kept the more targeted concern about federation size and non-i.i.d. strength.
- *Strength: "principled optimization formulation via Lagrange multipliers."* Conflicts with the verified weakness that Eq. 13 is a heuristic not derived from Eq. 6; dropped per the rules.
- *Strength: "faster convergence."* Kept implicitly (Fig. 2) under the empirical-gains strength; not duplicated.
- *Strength: "effective reuse of global gradient prototypes... requires no extra data."* Conflicts with the verified weakness about server coordination/communication cost being non-trivial; dropped.

## Novel Insights
None beyond the paper's own contributions. The core observation that real local samples can be exploited for classifier re-balancing — and the mixed real-data-plus-gradient-prototype scheme — is the paper's own contribution; the reviewer commentary does not surface independent insights beyond identifying that the framing vs. CReFF deserves a real cost/privacy analysis.

## Suggestions
- Reframe the comparison to CReFF as a *quality-of-re-balancing* improvement rather than a cost/privacy improvement, *or* provide explicit communication-cost tables and an empirical privacy analysis (reconstruction/membership attacks on $g^{pro}_{W^{t-2},k,c}$, particularly for tail classes).
- Present Eq. 13 as a principled heuristic: motivate the norm-matching schedule directly and add a sensitivity study on $\lambda$ and on alternative rescaling choices.
- Add a sequential-decoupling baseline and a logit-adjustment baseline to disambiguate the role of $\widehat{W}$ from generic two-head/over-parameterization effects.
- Run at least one configuration with N≥100 clients and Dir($\alpha\le 0.1$); this is the regime where the gradient-prototype fallback is most relevant and where the method's story is most convincing.
- Report per-class (head/medium/tail) accuracy to make the gains interpretable.
- Report a $T$ sweep on CIFAR-100-LT.

## Score and Decision
The paper makes a reasonable, well-executed empirical contribution: a sensible critique of CReFF, a clean fallback mechanism using gradient prototypes, and consistent gains across the standard FL-LT benchmark suite with a useful ablation. The two real concerns are that (1) the "no extra server requirement / more privacy-friendly than CReFF" framing is not substantiated and is somewhat contradicted by the algorithm's own communication pattern, and (2) the headline update rule (Eq. 13) is a heuristic that doesn't follow directly from the stated Lagrangian. These are correctable in revision but do dent the contribution as currently framed. Soundness of experiments and clarity are adequate for the scope claimed; originality and value to the community are modest but real.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>