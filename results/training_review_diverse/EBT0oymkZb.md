Now I have all the evidence I need. Let me write the final consolidated review.

---

## Summary

This paper studies zero-shot generalization (ZSG) in offline RL. It first proves (Proposition 4) that without context information, a merged offline dataset from multiple environments is indistinguishable from an average MDP, explaining why standard offline RL fails to generalize. It then proposes two meta-algorithms — PERM (model-based) and PPPO (model-free) — built on a Pessimistic Policy Evaluation (PPE) subroutine with an oracle that returns an empirical Bellman operator and uncertainty quantifier. Theorems 9 and 14 provide suboptimality bounds decomposed into a supervised learning error (decaying with more environments) and an RL error (controlled by uncertainty quantification). Experiments on Procgen test a heuristic approximation (IQL with multiple value networks) that outperforms IQL and BC baselines.

## Strengths

- **First theoretical justification for the necessity of context information in offline RL ZSG (Proposition 4).** The proof that a merged dataset without context is compliant with an average MDP, combined with the concrete 2-context counterexample (Figure 1) showing the average-MDP optimal policy can achieve zero expected return while the true optimal achieves 0.5, provides a clean and principled explanation for the empirical failures observed in prior work (Mediratta et al., 2023). This is a genuine contribution.

- **Provable suboptimality bounds for ZSG in offline RL with explicit SL/RL decomposition.** Theorems 9 and 14 give rigorous bounds for both PERM and PPPO, and Table 1 summarizes them cleanly. The decomposition into a supervised learning error ($I_1$, decaying as $\widetilde O(1/\sqrt{n})$) and an RL error ($I_2$, controlled by coverage) is conceptually informative and, to the best of the paper's claims, the first such analysis for offline RL with ZSG.

- **Unified algorithmic framework.** Both PERM and PPPO are built on the same PPE subroutine (Algorithm 1), providing a modular template that can be instantiated with different uncertainty quantifiers (e.g., bootstrapping for nonlinear MDPs as in Remark 7, or explicit constructions for linear MDPs as cited in the appendix).

- **Empirical improvement over IQL and BC on Procgen.** The IQL-nV heuristic with multiple value networks achieves higher mean and median min-max normalized returns than IQL and BC on both expert and mixed datasets (Table 2). The ablation on Miner (Table 3) shows a trend of increasing performance with more value networks. These results are interesting as an independent finding.

## Weaknesses

### Fatal
None.

### Major

- **Structural disconnect between theory and experiments.** The paper's central theoretical contribution is PERM and PPPO, built on an oracle $\mathbb{O}$ (Definition 5) that returns an empirical Bellman operator and uncertainty quantifier. The experiments, however, do not implement PERM or PPPO. Instead, they modify IQL with multiple value networks (IQL-nV) and state that "this isn't exactly the same optimization objective as we proposed in Algorithm 2, but nonetheless a first-order approximation" (line 217). No analysis is provided of what this approximation entails, which theoretical guarantees are preserved, or how the pessimism mechanism in IQL (expectile regression) relates to the explicit subtractive penalty in PPE (Algorithm 1, line 124). The tested algorithm shares no structural connection with PERM beyond using separate value functions for groups of environments. This means the empirical section provides **no evidence for the effectiveness of PERM or PPPO** and does not validate the paper's central claims. The theory and experiments are, in effect, two separate contributions, but the paper presents them as a unified validation. The authors should either (a) implement a faithful version of PERM or PPPO (even in a simplified setting), or (b) explicitly separate the empirical section as an independent ablation on multiple value functions and remove the claim that it validates the theoretical framework.

- **The theoretical bounds depend on an uninstantiated oracle in the main text.** Definition 5 assumes an oracle $\mathbb{O}$ that returns $(\widehat{\mathbb{B}}V, \Gamma)$ satisfying a high-probability guarantee. While Remark 7 mentions bootstrapping as a practical approach and line 205-206 references a linear MDP instantiation in the appendix, the main text does not sketch how $\Gamma_{i,h}$ scales with $K$ (number of trajectories per environment) or function class complexity for any concrete setting. The $I_2$ term in both Theorems 9 and 14 is left entirely abstract. This does not invalidate the theory — oracle-based analysis is standard practice — but it makes the bounds qualitative rather than quantitative at the level of the main text. A brief sketch of how $\Gamma_{i,h}$ is bounded for at least one function class (even a note that this appears in the appendix) would significantly improve readability and allow readers to assess the framework's substance.

### Minor

- **Limited baselines.** The experiments compare only against IQL and BC. Other offline RL methods (CQL, BCQ, etc.) or multi-environment approaches from the cited literature (Mediratta et al., 2023) are not included as baselines. This makes it difficult to assess where IQL-nV sits in the broader landscape.

- **Arbitrary grouping of environments.** The 200 training levels per Procgen game are grouped into 4 environments of 50 levels each, with no justification for why 50 levels form a coherent environment. The paper states it is done "for practical reason" (line 223), but the choice directly affects the architecture design and the interpretation of results.

- **No statistical significance testing.** Standard deviations in Table 2 are large (e.g., 0.599 ± 0.108 vs. 0.567 ± 0.120 on expert mean). Statistical significance is not reported, making it unclear whether the observed improvements are reliable.

- **Ablation study limited to one game.** The value-network count ablation (Table 3) is conducted only on Miner. Generalizability of the trend to other Procgen games is unknown.

- **Missing baseline: separate full models per environment.** The paper does not compare against training completely separate IQL models (separate Q and V networks) for each environment group and then averaging their outputs. This would be a more direct baseline for the "multiple models" idea and would control for the effect of the shared Q network in IQL-nV.

### Trivial
None.

## Nice-to-Haves

- A faithful implementation of PERM or PPPO in a simplified setting (tabular MDPs or linear MDPs) would bridge the theory-experiment gap and demonstrate that the theoretical machinery is realizable.
- A discussion of what the IQL-nV approximation preserves from the PERM guarantees (and what is lost) would help readers understand the connection between theory and practice.
- Reporting the practical scaling of $\Gamma_{i,h}$ (e.g., as $O(1/\sqrt{K})$ for linear MDPs) briefly in the main text would make the bounds more tangible.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Oracle not instantiated in main text; linear MDP case omitted.** The paper explicitly references a linear MDP instantiation (Algorithm 5, Section D) in lines 205-206. This content was in the appendix, which the PDF parser stripped. Removed per instructions (missing appendix content).
- **Garbled notation in Algorithm 3 pseudocode.** This is a formatting artifact from PDF extraction, not an author error. Removed per instructions.
- **Missing related works (Bose et al., Ishfaq et al.).** Per instructions, missing-related-work criticisms are removed.
- **Data-splitting trick "not explained clearly."** The paper provides a clear explanation in Remark 13 (line 187-188). Removed.
- **Random policy selection in PPPO "not discussed."** Line 203 explicitly discusses why the random selection leads to better SL error scaling. Removed.
- **Proposition 4 does not rule out non-Markovian policies.** The paper explicitly restricts to Markovian policies, which is the standard setting. Not a weakness.
- **"The paper does not compare to a version that simply trains separate IQL models per environment and then averages their outputs."** This was moved to Minor — IQL-nV with separate V networks and shared Q is structurally different from fully separate models, but the concern is reasonable and retained at reduced severity.

## Novel Insights

The reviews surface a clear structural tension: the paper's theoretical machinery (oracle-based PPE → PERM/PPPO) and its empirical evaluation (IQL-nV heuristic) operate on different planes, and the bridge between them is asserted rather than built. An insight not fully explored in the paper is whether the oracle abstraction itself could be profitably instantiated via ensemble/bootstrapped uncertainty estimates in a way that directly connects to the IQL-nV heuristic — the current gap may be narrower than it appears if the multiple value networks in IQL-nV are interpreted as approximating the uncertainty quantifier $\Gamma$, but the paper does not make this argument. The impossibility result (Proposition 4) stands on its own as a clean and well-motivated contribution regardless of the experimental disconnect.

## Suggestions

1. **Reframe the paper's contributions.** Either (a) implement a faithful version of PERM or PPPO (even on a simple benchmark), or (b) separate the theory and experiments into distinct contributions, clearly stating that the empirical section is a heuristic ablation on multiple value functions in offline RL that is *inspired by* (rather than validated by) the theoretical framework.
2. **Briefly instantiate the oracle in the main text.** Even one paragraph showing how $\Gamma_{i,h}$ scales for linear MDPs (or how bootstrapping provides it) would give readers a concrete sense of the bounds.
3. **Add standard offline RL baselines** (CQL, etc.) to the experimental comparison.
4. **Report confidence intervals or statistical tests** for the main results in Table 2.

## Score and Decision

**Originality:** 6/10 — The impossibility result and ZSG framework are novel, but the oracle-based analysis is a fairly standard extension of Jin et al. (2021) to multi-environment settings.

**Quality:** 5/10 — Theory is sound but high-level; experiments are disconnected from the theory; empirical methodology has several gaps (limited baselines, no significance testing, arbitrary grouping).

**Clarity:** 6/10 — The paper is generally well-written but would benefit from a clearer exposition of the theory-experiment relationship.

**Significance:** 5/10 — The problem is important, but the paper does not yet provide a cohesive validation of its proposed solution.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>