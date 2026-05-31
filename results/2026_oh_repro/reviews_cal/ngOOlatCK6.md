## Summary
The paper studies *conditional* causal bandits where an arm corresponds to intervening on a *single node* \(X\) but allowing the chosen value of \(X\) to depend on observed covariates (“conditional interventions”). It claims (i) an exact graphical characterization of the **minimal** set of candidate intervention *nodes* guaranteed to contain an optimal conditional intervention, and (ii) a linear-time \(O(|V|+|E|)\) algorithm to compute that set, with experiments showing that using this pruning speeds up standard bandit routines.

## Strengths
- **Clear, concrete headline contribution (graph-only pruning + linear-time computation).** The abstract states a fully-graphical characterization and an \(O(|V|+|E|)\) algorithm to compute the “minimal set of nodes” containing an optimum (Abstract, lines 7–10), which—if correct—would be a practically useful preprocessing step for causal bandit solvers.
- **Addresses the practically important jump from hard to conditional interventions.** The paper explicitly motivates conditional interventions as more realistic than hard interventions, by “allowing the value of the intervened variable to be chosen based on the observed values of other variables” (Abstract, line 9), situating the contribution as a generalization beyond the standard hard-intervention causal bandit setup (Intro, lines 13–16).

## Weaknesses

### Fatal
None.

### Major
- **The information structure for “conditional interventions” is not stated crisply enough to make the main guarantee unambiguous.** The paper defines conditional interventions only at a high level as choosing the intervened value “based on the observed values of other variables” (Abstract, line 9). As written (at least in the accessible main text), it does not clearly pin down *which variables are observed before acting*, whether conditioning can include descendants/mediators of the target node, and whether these observations are available under interventions. This matters because the existence/location of an optimal conditional intervention can change with the decision-time observability/temporal ordering; without an explicit model, the claim “guaranteed to contain the optimal conditional intervention” is not fully well-defined.
- **“Minimal set” is asserted prominently but (in the accessible text) the minimality notion is not operationally specified.** The abstract repeatedly emphasizes *minimality* (“minimal set of nodes guaranteed to contain the optimal conditional intervention,” Abstract line 9), but the accessible text does not yet clarify whether minimality is meant in the strong sense (no strict subset can guarantee containing an optimum over all SCMs compatible with the graph) versus minimality only relative to the paper’s sufficient criterion/closure procedure. Because “minimality” is the main novelty claim, the paper needs an explicit definition of the quantifiers (minimal w.r.t. what model class and what intervention/policy class). Without that, the contribution risks being interpreted as a sound-but-not-necessarily-minimal pruning rule.

### Minor
- **Experimental claims (as currently visible) are plausibly supportive of pruning usefulness but not clearly tied to the *guarantee/minimality* claim.** The abstract claims “significantly prunes the search space and substantially accelerates convergence rates when integrated into standard multi-armed bandit algorithms” (Abstract, line 9–10). Speedups after pruning are expected for many reasonable prunings; to support the *guarantee* aspect, experiments should explicitly report that the pruned node set retains the true optimal intervention target across many SCM parameterizations per graph family (not just regret improvements on a few instances).

### Trivial
None (style/typos/formatting issues intentionally ignored).

## Nice-to-Haves
- Add an explicit “problem setting” box: (i) what is observed before choosing the conditional rule, (ii) what class of policies \(\pi\) is allowed, (iii) whether the intervention is single-node only, and (iv) whether conditioning on descendants of the intervened node is disallowed by design. This would also help readers map the theory to the empirical “standard MAB algorithms” integration.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **Removed (not verifiable from the accessible text):** The Strength Finder’s detailed claims about specific technical results (e.g., “Proposition 4,” “Theorem 12/13,” “LSCA closure,” “Algorithm 1 (C4),” “Lemma 15,” and Figure 1d) were not independently verified here because the tool output provided only partial paper visibility; I cannot responsibly affirm those exact theorem statements/numbering without directly quoting the corresponding sections.
- **Removed (speculative):** Any claim that the experiments are “hand-picked” or that “standard MAB algorithms” necessarily treat each conditional policy as an arm; this depends on implementation details not confirmed from the visible portions.

## Novel Insights
The paper’s core risk is not whether a pruning rule can help empirically (it often will), but whether the *optimality guarantee* is even a well-posed statement without fully specifying the observation/conditioning regime for conditional interventions. In this topic, small differences in what is observed before acting (e.g., allowing conditioning on variables downstream of the intervention target) can qualitatively change which intervention nodes can be optimal—so the paper’s theoretical claim needs the information structure to be elevated to a first-class assumption, not left implicit in prose.

## Suggestions
- State the conditional intervention class formally (e.g., single-node \(do(X:=\pi(S))\)), explicitly define the observed set \(S\) (and its timing), and use that exact definition consistently in theorems and proofs.
- Define “minimal” with explicit quantifiers (over SCMs compatible with the DAG; over allowed policies \(\pi\); over what observation model), and add a short explanation of why nodes outside the set can be excluded (e.g., necessity/adversarial construction if that is what is claimed).
- In experiments, in addition to regret curves, add a “retains optimum” diagnostic over many random parameterizations for fixed graphs, plus at least one natural competing pruning heuristic to demonstrate that the specific characterization (not just pruning) is doing the work.

## Score and Decision

### Round 1 — Bracketing (anchors)
Retrieved anchors:
- **MVpvyeVeyI (avg 3.40, Round 1 weak band)**: different topic (CBO) and mixed-quality; not a good topical match; lower methodological clarity than this submission’s stated goal.
- **fSxiromxAq (avg 3.00, Round 1 weak band)**: unrelated causal discovery on sparse data; clearly weaker than this submission.
- **JzFLBOFMZ2 (avg 3.20, Round 1 weak band)**: LLM-supervised causal structure learning; weaker/more heuristic than this submission’s claimed theory.
- **AvXrppAS2o (avg 3.00, Round 1 weak band)**: outcome prediction via causal structure; not comparable, but weaker contribution density.

- **IPayPEGwdE (avg 5.00, Round 1 mid band)**: causal contextual bandits with theory+experiments; comparable band; this submission’s *claimed* contribution is narrower but potentially more “exact characterization”-oriented.
- **ZXs3pkmrRG (avg 5.50, Round 1 mid band)**: test-time causal structure learning; different but mid-quality anchor.
- **2pEqXce0um (avg 4.50, Round 1 mid band)**: root cause analysis; different.
- **oVVLBxVmbZ (avg 5.25, Round 1 mid band)**: conditional intervention in recourse/RL; different.

- **xByvdb3DCm / 3cuJwmPxXj / A3YUPeJTNR / 5t57omGVMw (all avg 8.00, Round 1 strong band)**: strong accepts but mostly different topics; useful only as “high bar” anchors.

**Round-1 bracket:** based on the paper’s *apparent* technical ambition but with a real major ambiguity about the setting/minimality definition visible in the text, the plausible range is **between 5.0 and 7.0**.

### Round 2 — Narrowing (anchors inside bracket)
Retrieved anchors:
- **ZXs3pkmrRG (avg 5.50, Round 2)**: comparable overall rigor; this paper’s central theoretical claim seems more self-contained, but the ambiguity about the policy/observation model is a similarly serious clarity gap.
- **w50MQ9Vfty (avg 5.50, Round 2)**: design of experiments under interference; solid but different; this submission’s contribution could be comparable if its assumptions/minimality are crisply formalized.
- **lnMQGBHYRt (avg 5.33, Round 2)** and **Lxst78Rrwj (avg 5.00, Round 2)**: mid-quality causal-method papers; this submission’s stated theory contribution is potentially stronger, but the current underspecification blocks confidence.

- **u63OVngeSp (avg 7.00, Round 2)** and other 6.5–6.75 anchors (SThJXvucjQ 6.67, FCMpUOZkxi 6.75, 0oWGVvC6oq 6.50): these typically pair clear assumptions with complete theorem statements/guarantees and well-aligned empirical validation. Relative to these, the present paper (as visible) falls short on *problem specification clarity* for its central guarantee.

**Final score rationale:** The paper is above generic mid-tier work in ambition (exact characterization + linear-time algorithm + pruning integration), but the main accept-level bar for such a theory paper is crisp formalization of the conditional-intervention observation/policy model and an explicit minimality definition aligned with the claimed guarantee. Given the major ambiguity visible in the text, I place it closer to the **5.5** anchors than to the **7.0** anchor.

**Score: 5.5 — Decision: Reject (borderline, could move with clarified formalization if the full version already contains it clearly).**

Anchors list with one-line comparisons (all retrieved across rounds):
- MVpvyeVeyI (3.40, R1): weaker/more assumption-restricted; not close topically.
- fSxiromxAq (3.00, R1): weaker and off-topic.
- JzFLBOFMZ2 (3.20, R1): weaker/more heuristic.
- AvXrppAS2o (3.00, R1): weaker and different.

- IPayPEGwdE (5.00, R1): similar band; this paper’s claimed characterization is sharper, but clarity gaps remain.
- ZXs3pkmrRG (5.50, R1 & R2): similar quality/rigor; both have notable clarity/assumption issues.
- 2pEqXce0um (4.50, R1): different.
- oVVLBxVmbZ (5.25, R1): different.

- xByvdb3DCm (8.00, R1): much stronger and clearer theoretical framing.
- 3cuJwmPxXj (8.00, R1): much stronger.
- A3YUPeJTNR (8.00, R1): much stronger.
- 5t57omGVMw (8.00, R1): much stronger.

- w50MQ9Vfty (5.50, R2): similar overall strength; this paper could surpass it with crisper formalization.
- lnMQGBHYRt (5.33, R2): this paper’s claimed theory is stronger, but presentation/definition gaps reduce confidence.
- Lxst78Rrwj (5.00, R2): this paper is likely stronger if assumptions/minimality are properly nailed down.
- u63OVngeSp (7.00, R2): stronger accept-level clarity/guarantees than this paper as currently specified.
- SThJXvucjQ (6.67, R2): stronger overall completeness.
- FCMpUOZkxi (6.75, R2): stronger overall completeness.
- 0oWGVvC6oq (6.50, R2): stronger overall completeness.

MY FINAL SCORE: <score>5.5</score>  
MY FINAL DECISION: <decision>Reject</decision>