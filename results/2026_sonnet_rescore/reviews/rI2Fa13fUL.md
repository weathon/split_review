## Summary

Generative Trajectory Policies (GTP) frames offline RL policy learning as learning the entire solution map of a continuous-time ODE. The paper synthesizes diffusion models, flow matching, consistency models (CM), consistency trajectory models (CTM), shortcut models, and mean flows under this unified lens, then introduces two practical adaptations: (1) a score approximation that replaces costly ODE-solver-generated supervision with a linear-path surrogate (Theorem 1), and (2) an advantage-weighted generative training objective derived from KL-regularized policy optimization (Theorem 2). The method is evaluated on D4RL Gym locomotion and AntMaze benchmarks, achieving the highest reported averages among compared methods.

---

## Strengths

- **BC expressiveness results are genuinely striking.** Table 1 shows GTP-BC achieves 66.3 average on AntMaze without any value guidance, versus 44.1 for C-BC and 41.2 for D-BC. On antmaze-medium-diverse it reaches 85.0 vs. D-BC's 29.8. This gap isolates an architectural benefit from the advantage weighting and is the paper's sharpest piece of evidence.

- **Score approximation is both theoretically justified and empirically validated.** Theorem 1 formally bounds the objective difference at O(h^p), and Table 3 confirms the practical benefit: removing the approximation (using an ODE solver instead) raises training time from 4.26 h to 5.23 h and drops hopper-medium-expert score from 112.2 to 99.7. Both the theory and the ablation pull in the same direction.

- **Offline RL results achieve the top reported average on both Gym (89.0) and AntMaze (80.6).** GTP outperforms D-QL (87.9/69.6) and QGPO (86.6/78.3) on both domains. The margin over IDQL-A on AntMaze (80.6 vs. 79.1) and over QGPO (78.3) is modest but consistent, and all three comparators have complete results over all six tasks.

- **Variational guidance ablation is decisive.** Table 3 shows that replacing advantage-weighted training with a linear Q-term causes divergence at λ=0.1 and λ=1.0, and fragility at λ=0.01, whereas GTP is stable across seeds without task-specific tuning.

- **Inference efficiency is demonstrated.** All GTP results use only K=5 sampling steps, while diffusion policies typically require many more, and consistency policies with K=2 consistently underperform.

---

## Weaknesses

### Fatal
None.

### Major

- **The "unified ODE framework" is substantially a restatement of CTMs rather than an independent theoretical invention.** Section 3.3 explicitly states the surrogate parameterization φ is "inspired by (Kim et al., 2024)." Section 3.4 states CTMs "instantiate *both* core components of our unified framework" — meaning both Eq. (5) and Eq. (6) already appear in CTMs. The paper's most accurate characterization is: GTP is CTM applied to offline RL with two domain-specific adaptations (score approximation and advantage weighting). Presenting the framework in Sections 3.1–3.3 as novel theoretical scaffolding without clearly stating the starting point overstates the theoretical contribution and may mislead readers. The actual novelty — applying this to offline RL with these specific adaptations — is real and should be foregrounded more honestly.

- **The abstract's claim of "perfect scores on several notoriously hard AntMaze tasks" is factually inaccurate.** Only antmaze-umaze achieves 100.0, and antmaze-umaze is the *easiest* AntMaze configuration, not notoriously hard. The large-maze tasks score 53.5 and 71.0, far from perfect. The contributions list repeats the same phrase. The body of the paper (Section 5.2) is more precise: "on the antmaze-umaze task, our method achieves a perfect score of 100.0." The abstract must be corrected to avoid a clear factual misrepresentation.

### Minor

- **Theorem 2 presents the advantage-weighted regression result (Eq. 12) as if it were newly derived, when it is a standard result from AWR/AWAC.** The genuinely novel step is Eq. (12) → Eq. (13) — showing that matching π\* with a generative model reduces to an advantage-weighted generative loss. This connection is worth labeling as a theorem, but Eq. (12) should be attributed clearly as a known result. The current presentation conflates the two steps.

- **Theorem 1's O(h^p) claim is technically correct but creates a misleading impression for the actual implementation.** In the implementation, xᵤ = x + u·z is a point on the linear-interpolation path (Eq. 11). Under flow matching with straight-line conditional paths, this surrogate f̃ coincides with the true conditional vector field f\*, making the approximation essentially *exact* — a stronger and simpler result than the general O(h^p) bound. The paper defers the connection to flow matching to Appendix B.4; this intuition belongs in the main text as the primary justification, replacing the somewhat misleading general bound.

- **Ablation study covers only a single environment (hopper-medium-expert-v2).** The score approximation is a structural change (substituting linear-path supervision for ODE-path supervision), and the most dramatic GTP gains appear on AntMaze, which has multimodal, long-horizon behaviors. Demonstrating that the approximation holds on at least one AntMaze task would substantially strengthen the evidential case for the method's most impressive empirical domain.

### Trivial

None beyond the abstract wording issue already noted.

---

## Nice-to-Haves

- **Direct inference latency comparison.** Table 3 provides training time but not per-action inference time against D-QL and QGPO under matched hardware. The claim that K=5 steps bridges the expressiveness-efficiency gap would be quantitatively sharper with timing data.
- **Explicit discussion section on GTP vs. CTM.** A dedicated paragraph precisely stating what GTP adds to CTMs beyond the offline RL application — and why those additions matter — would clarify the contribution for readers familiar with the generative modeling literature.
- **Broader ablation.** Extending Table 3 to include one or two AntMaze tasks would show whether the score approximation advantage generalizes to the domain where GTP's BC gains are largest.
- **Visualization of full trajectory vs. one-step policy.** Bringing the multi-goal environment visualization (Appendix D) into the main paper, even compactly, would make the expressiveness argument concrete rather than purely numerical.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Including offline RL methods in BC comparison is confusing" (Harsh Critic, Section 5.1).** The paper explicitly acknowledges these are offline RL methods and includes them to show that GTP-BC is competitive even against value-function-augmented methods. This is a fair and informative comparison, not a methodological flaw. Removed.

- **"Unfair AntMaze average" (Harsh Critic, Section 5.2).** Looking at Table 2, the averages for BDM and C-AC are not computed by the paper (shown as "-") because of missing entries. The primary comparisons cited in the text — QGPO (78.3 over 6 tasks) and IDQL-A (79.1 over 6 tasks) — both have complete numbers for all six AntMaze tasks, making GTP's 80.6 a fair comparison. The marginal 1-2 point lead being "slim" is a matter of degree, not unfairness. Removed.

- **Strength Finder — "highest average return among all compared offline RL methods": generic framing.** Retained as a concrete strength with table citation rather than a generic statement.

- **Strength Finder — "principled unification": overstated as independent contribution.** The synthesis is pedagogically useful (correctly) but not a new mathematical invention (per Major weakness above). Partially retained in Strengths but with the caveat captured in the Major weakness.

---

## Novel Insights

The paper's most genuinely useful insight — underemphasized in the writing — is that intermediate ODE trajectory points needed for consistency training can be obtained for free by sampling xᵤ = x + u·z from the same Gaussian perturbation already used for standard generative training. This collapses what would otherwise be a computationally prohibitive inner loop (running a numerical ODE solver at every training step) into a zero-cost closed-form operation. The O(h^p) theorem formalizes this, but the sharper intuition — that under flow-matching-style linear paths the approximation is exact — is the real insight and deserves to be the lead argument in Section 4.1. Combined with advantage weighting, this makes CTM-style trajectory learning practically accessible in the offline RL setting, which is a non-trivial engineering and conceptual contribution even if the individual components are known.

---

## Suggestions

1. **Correct the abstract and contributions list** to say "achieves a perfect score on antmaze-umaze" (singular, specific task) rather than "perfect scores on several notoriously hard AntMaze tasks."
2. **Reframe Section 3** as "a synthesis and exposition of the unified ODE framework, following CTMs" and explicitly state that GTP's contribution begins in Section 4 with the offline RL adaptations.
3. **In Theorem 1**, note that under linear conditional paths (flow matching), the surrogate f̃ equals f\* conditioned on data, making the approximation exact (h=0 case). Lead with this as the primary justification; present the O(h^p) bound as a generalization.
4. **Attribute Eq. (12)** in Theorem 2 to AWR/AWAC and label it accordingly; present Eq. (13) as the new step connecting this to generative training objectives.
5. **Extend Table 3** to include at least antmaze-medium-play or antmaze-medium-diverse to validate score approximation benefit on AntMaze.

---

## Score and Decision

**Originality:** The unified framework is largely a restatement of CTMs, which limits novelty. The genuine original contribution lies in the two offline RL adaptations (score approximation and advantage weighting) and their integration. Moderate originality.

**Importance of research question:** High. Resolving the expressiveness-efficiency tradeoff in offline RL generative policies is a timely and significant problem.

**Claims support:** The main empirical claims are well-supported by Tables 1–3. However, the abstract's "perfect scores on several hard AntMaze tasks" is factually wrong (only one task, the easiest one), and the theoretical novelty claims in the contributions list overstate the framework's independence from CTMs.

**Soundness of experiments:** Solid. Five seeds, standard D4RL protocol, ablations on the two key components, competitive baselines with full results for main comparators. The narrow ablation (single task) is a limitation.

**Clarity:** Generally clear and well-organized. The misleading abstract and the underexplained relationship to CTMs are the main clarity issues.

**Community value:** High for both offline RL and generative modeling communities. The BC results (66.3 vs. 44.1 on AntMaze without value guidance) are a striking demonstration of what trajectory-map learning offers.

The paper's core empirical contribution is real and the methodology is sound. The main issues — overclaimed novelty in the framework and the inaccurate abstract — are correctable in a revision. Neither invalidates the central finding that learning the full ODE solution map improves expressiveness in offline RL.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>