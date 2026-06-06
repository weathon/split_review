---

## Summary

DIST (Diffuse and Steer) is a plug-in corrective sampling module for 3D molecular diffusion models. The paper formalizes the "dense-concentrated (DC) structure" of molecular distributions (Definition 3.1), analyzes how reverse-diffusion trajectories can overshoot narrow valid regions, provides theoretical error bounds under selective correction (Corollary 3.1, Proposition 3.1), and proposes an inference-time procedure: run one shared prefix from $T$ to a chosen $t$, branch into a batch of perturbed candidates, run "pilot" continuations to $0$, filter by valence-based chemistry score, and propagate only survivors. Applied to EDM, GeoLDM, and RADM on QM9 and GEOM-Drugs, DIST consistently improves atom/molecule stability and validity while reducing inference timesteps to roughly 40–60% of the 1000-step baseline.

---

## Strengths

- **Concrete formalization of DC-structure (Definition 3.1, Eqs. 6–7):** The paper provides an explicit Gaussian-mixture model with bounded covariance $\Sigma_{k,t} \preceq \sigma_*^2 I$ and separation $\Delta$, and derives a precise overshoot condition $\beta_t\Delta/\sigma_*^2 > c\sigma_*$ (Eq. 7) under which a reverse step exits the valid region. This is a specific, anchored theoretical contribution.

- **Consistent empirical gains across diverse backbones and datasets:** Table 2 shows that DIST lifts molecule stability by +7.9% (EDM), +4.0% (GeoLDM), +4.1% (RADM) on QM9, with validity improvements of +3–5% across all three architectures. Gains replicate on GEOM-Drugs. The plug-in claim is convincingly verified because the underlying model weights are unchanged.

- **Genuine efficiency improvement:** Table 3 shows actual average inference steps of 413–637 vs. the 1000-step baseline across all model/dataset pairs—a real halving in most settings, not just a theoretical claim.

- **Informative ablation:** Table 4 demonstrates monotonic quality improvement with pilot subset size (30→50→100), confirming the method is robust even at smaller budgets (428 steps, still superior to baseline).

- **Motivating empirical diagnostic (Table 1):** The starting-timestep sweep shows monotonically degrading quality from $t=0$ to $t=1000$, directly motivating mid-trajectory correction. This is a simple but effective piece of evidence.

---

## Weaknesses

### Fatal
None.

### Major

- **Missing rejection-sampling control experiment.** DIST's operational core is: generate many candidate trajectories from a shared prefix, filter by validity, and keep the passing ones. The essential question is whether the benefit stems from *trajectory steering at intermediate $t$* versus the much simpler mechanism of *generating many candidates and culling failures*. The natural control — run the backbone independently $k$ times with identical total function evaluations as DIST, then keep the valid fraction — is absent. Without it, one cannot attribute the observed gains to the correction-at-$t$ mechanism rather than to candidate selection per se. The ablation in Table 4 varies pilot subset size within DIST but does not compare against the independent-sampling baseline. This is the most important missing experiment; it does not invalidate the method but leaves the mechanism claim unsubstantiated.

### Minor

- **"First to highlight" overclaim (Contribution Bullet 1, p.2).** The paper states "we are the first to highlight that molecular data distributions are highly concentrated and dense." However, it also explicitly cites Cao et al. (2023) for having "analyzed the re-entry problem and demonstrated the benefits of stochastic samplers," and Bohde et al. (2025) and Choi et al. (2025) for related fragility observations. The contribution is the *formalization* of DC-structure and the resulting corrective method—that narrower framing is accurate and should replace the broader "first to highlight" claim.

- **Evaluation metrics capture only valence-based validity.** The paper's central claim is that DIST "steers trajectories toward the true data distribution $p_0$" (Corollary 3.1 motivation), but the reported metrics—atom stability, molecule stability, and valence-rule validity—are all valence-rule checks. They do not measure 3D geometric quality (strain energy, RMSD to equilibrium), drug-likeness (QED, SA score), or distributional diversity. The gap between the formal claim (distributional alignment with $p_0$) and the metrics that actually measure it is not addressed. This is a real, specific concern about the evidence supporting the strongest stated claims.

- **Headline efficiency figure is a lower-bound example, not the operational average.** Section 4.3 calculates "307 steps" for $t=300, |B|=100$ and uses it to claim "nearly half." The 307 excludes the pilot inference cost from $t$ to $0$. The actual measured averages in Table 3 are substantially higher (416–637), and the paper attributes the discrepancy to Appendix G.1. The text as written leads readers to the 307 figure as the operative number; the prose should be revised to foreground Table 3 values and present 307 as a structural lower bound.

### Trivial

- The overshoot condition in Eq. 7 ($\beta_t\Delta/\sigma_*^2 > c\sigma_*$) is stated as a risk but not verified against the actual noise schedules of EDM/GeoLDM/RADM. Table 1's monotonic degradation is consistent with the claim but does not distinguish the overshoot mechanism from ordinary score-estimation error accumulation. This is a theoretical loose end rather than an error.

---

## Nice-to-Haves

- **Direct experiment isolating correction timing:** Show that applying the same valence filter *post-hoc* at $t=0$ (i.e., generate 100 samples, keep valid ones, same compute as DIST) underperforms DIST's mid-trajectory filter. If mid-$t$ steering is meaningfully better than endpoint selection, this experiment is convincing on its own; if not, it reframes the contribution more honestly.
- **Additional drug-likeness metrics (QED, SA score) on GEOM-Drugs:** Would directly support the claim that DIST produces higher-quality molecules beyond satisfying valence rules.
- **Verification that overshoot condition (Eq. 7) is satisfied for EDM's actual $\beta_t$ schedule:** A brief numerical check would sharpen the theoretical narrative.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "Baselines exclude corrective sampling / SMC methods."** The paper explicitly states (Section 2, final paragraph): "a detailed discussion on the comparison of our work with corrective method is provided in Appendix B." Per the rules, criticisms of absent appendix content are removed—the appendix exists in the original submission. Removed.

- **Harsh Critic: "Proposition 3.1's key function $f(\cdot)$ is in the appendix and cannot be evaluated."** The paper states the exact form is in Appendix E.2. This is a standard appendix deferral; removed per the rule on missing appendix content.

- **Harsh Critic: "Corollary 3.1 is standard."** The corollary is correct and clearly stated; "standard" is not a defect. The paper uses it as a motivating lemma, not a novel result. Not a weakness; removed.

- **Harsh Critic: "Framing article between pilot and actual samples is a framing artifact."** Reading Section 3.2 carefully: the pilot subset is indeed the full continuation from $t$ to $0$ used to score each batch. The paper is describing a single procedure; the "pilot" terminology is about the scoring role, not a distinct computational phase. The framing is unusual but not incorrect.

- **Strength Finder: "Consistent improvement confirms the DC-structure issue."** While the improvements are real, they do not strictly confirm the DC-structure *mechanism*—they confirm that DIST improves results. This specific strength claim overreaches the evidence; dropped in favor of the weaker (and accurate) strength that gains are consistent across diverse architectures.

---

## Novel Insights

The most genuinely novel observation, which neither reviewer developed fully, is that the shared-prefix amortization trick (run one trajectory from $T$ to $t$, branch into $|B|$ perturbed copies) transforms what would otherwise be $|B|\times T$ function evaluations into $(T-t) + |B|\cdot t$ evaluations, creating a meaningful efficiency dividend that *enables* candidate selection without proportional cost. This structural insight—that the redundancy of independent sampling from scratch is the real inefficiency, not the number of function evaluations per se—is the cleanest engineering contribution of the paper, distinct from the DC-structure theoretical story. However, whether the mid-trajectory branch point matters (versus branching at $t=0$) remains an open question the paper does not answer.

---

## Suggestions

1. **Add the key control:** Generate independently $\sim 100$ samples per target using the backbone, keep the valid fraction, and report total timesteps alongside DIST results in Table 2/3. This single experiment either vindicates the mid-trajectory mechanism or clarifies what the true contribution is.
2. **Fix the contribution bullet:** Replace "first to highlight" with "formally characterize" or "provide the first quantitative formalization of DC-structure"—a claim that is accurate and defensible given the cited prior work.
3. **Revise Section 4.3:** Lead with Table 3 actual step counts (416–637) as the efficiency claim, then explain 307 as the structural lower bound from the formula, noting that pilot costs bring the operational average higher (with Appendix G.1 providing the full accounting).
4. **Add at least one drug-likeness metric (e.g., SA score or QED) on GEOM-Drugs:** This would meaningfully close the gap between the distributional-alignment claim and the evidence.

---

## Evaluation on Key Axes

| Axis | Assessment |
|---|---|
| **Originality** | Moderate — DC-structure formalization is novel, but shared-prefix rejection sampling is a known technique; the combination is new in this context. |
| **Importance of research question** | High — 3D molecular generation quality and efficiency are active, practical problems. |
| **Claims supported** | Partially — performance improvement claims are well-supported; mechanism attribution is not. |
| **Soundness of experiments** | Adequate for the performance claim; missing one key control experiment for the mechanism claim. |
| **Clarity of writing** | Good — the paper is well-organized, the method is described clearly, and the theoretical setup is readable. |
| **Value to the community** | Real — a model-agnostic plug-in that consistently improves three backbone models has practical value regardless of the theoretical story. |

---

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>