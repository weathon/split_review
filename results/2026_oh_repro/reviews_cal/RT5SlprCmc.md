## Summary
The paper proposes **MadDist / TDMadDist**, a self-supervised framework to learn a state embedding whose (quasi)metric distance approximates the **Minimum Action Distance (MAD)**—the minimum number of actions needed to move between states—**using only state trajectories** (no rewards and, crucially, no action labels). The method combines trajectory-based distance regression with quasimetric constraints and (for TDMadDist) a TD-style bootstrapping objective, and evaluates on multiple environments with “known MAD” and a small downstream planning test.

## Strengths
- **Clear problem formulation and objective design for learning (a)symmetric distances from trajectories.** The paper explicitly frames MAD as potentially asymmetric and provides both symmetric and asymmetric variants (“accommodating both symmetric and asymmetric approximations,” Abstract; see also the quasimetric discussion in the main method sections).
- **Nontrivial objective construction beyond a single loss.** The framework combines multiple terms (trajectory-distance scaling + constraints/contrastive structure, and a TD bootstrapping extension), which is a substantive algorithmic contribution rather than a single regression baseline (the paper’s method section lays out multiple equations for these components).
- **Includes at least one downstream sanity check rather than only correlation metrics.** The paper reports a goal-directed planning experiment (Table 1) in PointMaze variants, intended to show that the learned distance is operationally useful, not only numerically correlated with labels.

## Weaknesses

### Fatal
None.

### Major
- **The “learn MAD without actions” claim is not made well-posed in general, and the paper does not clearly state the assumptions under which MAD is identifiable from state-only trajectories.**  
  The Abstract makes a broad claim: “learned solely from state trajectories… requiring neither… the actions executed” and proposes MAD as “the minimum number of actions required to transition between states” (Abstract). However, the paper does not (in the main text provided) clearly distinguish whether it is recovering (i) the environment’s action-graph MAD under optimal control, or (ii) a **behavior-policy-induced shortest-path distance on the observed state-transition graph**. Without explicit assumptions on coverage/full support (or determinism / action-agnostic transition support), state-only trajectories generally do not determine the underlying action graph. This is a substantive gap because it affects what the method is actually guaranteed to learn and when the evaluation is meaningful.

- **Stochastic-environment definition mismatch: “minimum number of actions required” needs a precise convention, otherwise MAD can be degenerate.**  
  The paper explicitly claims evaluation over “deterministic and stochastic dynamics” (Abstract) while keeping the same MAD definition (“minimum number of actions required”). In stochastic MDPs, whether MAD is defined by **support** (nonzero probability) vs **probability threshold** vs **expected steps / hitting time** changes the metric drastically. The paper’s own framing (“MAD … fundamental metric”) combined with stochastic evaluations requires a precise definition and justification of why that definition is appropriate for downstream planning/shaping; otherwise “ground-truth MAD” in stochastic settings is underspecified.

### Minor
- **Evaluation protocol is missing a targeted stress test for behavior-policy / coverage shift, despite the headline “no actions needed” claim.**  
  Since the method trains from trajectories, the learned distance can depend strongly on the data-collection policy’s coverage. The paper claims broad effectiveness across environments (Abstract), but (in the main text available) does not clearly report experiments where the same environment is trained under systematically different trajectory generators (narrow vs exploratory) to show when the method succeeds/fails and how robust it is.

### Trivial
None (style/formatting issues intentionally ignored).

## Nice-to-Haves
- Add an explicit section disentangling and naming the three objects: **(1) environment MAD (action-graph, optimal), (2) dataset-graph distance (behavior-induced), (3) stochastic reachability/expected-time variants**, and empirically show when they coincide in the chosen benchmarks.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **“The paper lacks downstream evaluation.”** Removed because Table 1 does include a downstream planning experiment; while limited, it exists.
- **Any criticism about cited benchmarks/models/datasets being unreleased or unverifiable.** Removed per hard rule (all cited entities assumed to exist/released).

## Novel Insights
A key synthesis is that the paper’s strongest empirical story (high correlation to “known MAD” and strong PointMaze planning) is consistent with two very different interpretations: learning **true action-distance under optimal control**, or learning **shortest-path structure of the behavior-induced transition graph**. The paper would be substantially stronger if it explicitly positioned MadDist as estimating one of these objects (or proved conditions under which they coincide), especially because the stochastic setting forces a careful definition choice that determines whether “MAD” is a meaningful planning heuristic or a degenerate support-based quantity.

## Suggestions
- **Make identifiability assumptions explicit** (e.g., coverage/full support over one-step transitions, determinism, ergodicity) and align claims to those assumptions (Abstract + Introduction).
- **Precisely define MAD in stochastic MDPs** (support-based vs threshold vs expectation) and ensure the “ground-truth MAD” computation matches that definition.
- **Add a behavior-policy/coverage shift experiment**: fix an environment and train on (i) exploratory trajectories and (ii) narrow trajectories; report how the learned distances and downstream planning degrade.

## Score and Decision

### Calibration: Round 1 (bracketing)
Anchors retrieved:
- **Weak band (<3.5)**:  
  - FjifPJV2Ol (avg 3.40, R1) — weaker/less grounded than this paper.  
  - NRRHkJE03w (avg 3.00, R1) — weaker/less relevant.  
  - OcTUquFXfx (avg 2.60, R1) — weaker.  
  - 5AbtYdHlr3 (avg 3.00, R1) — weaker.
- **Middle band (3.5–7.5)**:  
  - TOiageVNru (avg 6.00, R1) — comparable topic; clearer framing but mixed reviews.  
  - qofh48zW3T (avg 6.00, R1) — conceptually careful about stochastic “distance vs probability”.  
  - oEzY6fRUMH (avg 4.75, R1) — weaker/more presentation-level issues.  
  - NlBuWEJCug (avg 4.50, R1) — weaker with scalability/justification gaps.
- **Strong band (>7.5)** (not very topically aligned):  
  - agPpmEgf8C (avg 8.00, R1) — much stronger overall, different topic.  
  - 9pW2J49flQ (avg 8.00, R1) — much stronger, different topic.  
  - 6PbvbLyqT6 (avg 8.00, R1) — much stronger, different topic.  
  - stUKwWBuBm (avg 8.00, R1) — much stronger, different topic.

**Round-1 bracket:** based on topic-relevant anchors (≈4.5–6.75), this paper plausibly sits **between 5.5 and 6.5**: it has a concrete method + results, but has a major conceptual/definition gap around what is identifiable from state-only trajectories and what “MAD” means in stochastic domains.

### Calibration: Round 2 (narrowing within bracket)
Anchors retrieved:
- (4.5, 6.0): qg5JENs0N4 (avg 5.50), Uxm7DxPwrZ (avg 4.80), OjCWG58ZyY (avg 5.50), oEzY6fRUMH (avg 4.75)  
- (6.0, 7.5): 41WIgfdd5o (avg 6.25), skGSOcrIj7 (avg 6.80), s9SVlWOcLt (avg 6.75), EW6bNEqalF (avg 7.00)  
- (5.5, 7.0): TOiageVNru (avg 6.00), I7DeajDEx7 (avg 6.75), wPhbtwlCDa (avg 6.50), qofh48zW3T (avg 6.00)

Comparisons:
- Compared to **TOiageVNru (6.0)** and **qofh48zW3T (6.0)**: this paper is similar in ambition, but **weaker in conceptual precision** (especially stochastic definition / identifiability), so should be **at or below 6.0**.
- Compared to **qg5JENs0N4 (5.5)**: this paper feels **similarly solid empirically**, but has a sharper core-contribution ambiguity; net **around 5.5–6.0**.
- Compared to **I7DeajDEx7 (6.75)**: that anchor’s acceptance-tier score suggests stronger justification/positioning; this paper is **not as well nailed down**, so below 6.5.

**Final score:** **5.5** (borderline accept quality, but the major well-posedness/definition issues weigh against acceptance at ICLR without clarification and/or assumption-aligned evaluation).

MY FINAL SCORE: <score>5.5</score>  
MY FINAL DECISION: <decision>Reject</decision>