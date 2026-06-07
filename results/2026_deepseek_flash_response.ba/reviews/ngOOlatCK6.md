Now I have all the information needed. Let me produce the final review.

## Summary

This paper studies the conditional causal bandit problem, where arms are single-node conditional interventions on a known causal graph. The central contribution is a complete graphical characterization of the minimal set of nodes guaranteed to contain the optimal intervention node — the mGISS (minimal Globally Interventionally Superior Set). The paper proves this set equals the LSCA closure of the parents of the reward variable Y (Theorem 13), provides an elegant $\Lambda$-structure reformulation (Theorem 12), and proposes the C4 algorithm that computes this set in $O(|V|+|E|)$ time (Theorem 16). Empirical results demonstrate substantial search space pruning on random and real-world graphs, and improved regret convergence when combined with a UCB-based bandit algorithm.

## Strengths

1. **Complete graphical characterization of the mGISS (Theorems 12 & 13)** — The paper establishes that the mGISS equals the LSCA closure of $\mathrm{Pa}(Y)$, which is a clean and non-trivial result. The $\Lambda$-structure characterization (Theorem 12) replaces a recursive definition with a simple, visual, non-recursive graphical condition, going well beyond the trivial "parents of Y" answer that holds for multi-node hard interventions (Lee & Bareinboim 2018). This is a genuine theoretical advance for the single-node conditional setting.

2. **Linear-time C4 algorithm (Theorem 16)** — The connector mechanism (Definition 14) is elegant: a node belongs to the mGISS exactly when its children have multiple distinct connectors. The resulting algorithm runs in $O(|V|+|E|)$ and is clearly explained. This bridges the gap between theory and practice.

3. **Proposition 4 — equivalence of conditional and deterministic atomic superiority** — This equivalence (stated as Proposition 4, proved in the appendix) reduces the analysis from the complex conditional-intervention setting to the simpler deterministic atomic setting. That the paper proves this reduction and then leverages it throughout is a nontrivial theoretical step.

4. **Uniqueness of the mGISS (Proposition 6)** — The paper proves the minimal GISS is unique, which is important because without uniqueness the "minimal" search space would not be well-defined as a target for C4.

5. **Careful problem formalization** — The conditioning set constraints ($\mathrm{An}(X)\setminus\{X\} \subseteq \mathbf{Z}_X \subseteq \mathbf{V}\setminus\mathrm{De}(X)$) and the "observable conditioning set" condition are rigorously defined and well-motivated with concrete examples (train delays, kidney function).

6. **Supporting empirical evidence** — Search space reduction experiments on random graphs (20–500 nodes, varying degrees) and real-world `bnlearn` graphs show substantial pruning, especially for sparse graphs where the method is most relevant. Regret curves on 4 datasets show faster convergence with mGISS pruning.

## Weaknesses

### Major

1. **Regret computation uses an empirical oracle, not the true optimal arm (Footnote 11)** — The paper states: "For the computation of regret, we use the estimated best arm, defined as the arm that most runs concluded to be the best at the end of training." This means the regret values represent convergence to a *consensus empirical best* from finite samples, not regret relative to the *true* optimal intervention under the unknown SCM. The absolute regret values are therefore uninterpretable. While the *comparison* between mGISS and brute-force remains informative (both use the same empirical oracle, so the relative advantage is real), the claim about "accelerating convergence rates" is only established relative to this empirical proxy, not the ground truth. For a paper whose abstract claims "substantially accelerates convergence rates," this gap weakens the experimental evidence.

### Minor

2. **No proof sketch of Proposition 4 in the main text** — The equivalence between conditional-intervention superiority (Definition 1) and deterministic atomic-intervention superiority (Definition 2) has substantially different quantifier structures (existential choice over policies vs. existential choice per noise realization). The paper states this equivalence without any intuition or proof sketch in the main text. Including even a paragraph explaining the main idea would increase reader confidence in what is the linchpin of the entire analysis.

3. **Limited bandit experiment scope** — Only 4 datasets from `bnlearn` are used for the bandit evaluation, all from the same repository. The paper does not include any ablation of the conditioning set choice (experiments use $\mathbf{Z}_X = \mathrm{An}(X)\setminus\{X\}$), so it is unclear whether the relative performance of mGISS vs. brute-force is robust to different conditioning set specifications.

4. **Conservative characterization over all possible $\mathbf{Z}_X$** — The paper's definition quantifies over *all* observable conditioning sets simultaneously. This means the mGISS is guaranteed to be sufficient for any choice of $\mathbf{Z}_X$, which is safe, but the theory does not discuss whether tighter pruning is possible when the practitioner commits to a specific, fixed $\mathbf{Z}_X$. The paper acknowledges this implicitly but never discusses the gap between the worst-case theoretical guarantee and the potential for instance-specific tighter pruning.

### Trivial

5. **Figure 3 caption lacks numeric mGISS/brute-force sizes** — The figure visually shows "X nodes" vs "Y nodes" but the actual node counts for each dataset are not reported in the main text or caption. These numbers would help readers calibrate the difficulty of each problem instance.

## Nice-to-Haves

- A comparison between mGISS-pruned UCB and UCB with a random subset of nodes of the *same size* as the mGISS would test whether the structural selection is better than simply having fewer arms, strengthening the empirical case.
- Statistical tests (e.g., confidence intervals for regret differences at specific round counts) would strengthen the bandit results.
- An ablation varying the conditioning set $\mathbf{Z}_X$ (not just the minimal $\mathrm{An}(X)\setminus\{X\}$) would clarify robustness.

## Removed Points

These were flagged during review synthesis but removed with justification:

- **Harsh Critic Point 1 (Proposition 4 unverifiable due to missing appendix/missing proof sketch as a fatal concern):** The criticism that Proposition 4 "appears to conflate universal and existential quantifiers" and that the reviewer "could not verify this claim" is fundamentally a complaint about the appendix being stripped by the parser. Per the hard rules, weaknesses about missing appendix proofs are removed. The mathematical observation about quantifier structure is noted in Minor Weakness 2 above (as a missing proof *sketch* in the main text), but the characterization of this as a potentially fatal structural flaw is removed because the paper explicitly states proofs are in the appendix which exists in the original submission.
- **Harsh Critic Point about "tightness" of mGISS characterization:** The criticism that "The paper does not provide a constructive counterexample showing that removing any node from the mGISS could cause the optimal node to be missed" is addressed by the paper's own definition — the mGISS is *defined* as minimal w.r.t. set inclusion (Definition 5: "a GISS which is minimal with respect to set inclusion"), and Theorem 13 proves the LSCA closure *is* the mGISS. Proving minimality is the standard mathematical way to show this; explicit counterexamples per node are not required. This criticism misunderstands what the paper already establishes.
- **Strength Finder strengths about "important problem" and generic praise:** Generic statements about the problem being "important" or "well-motivated" without specific evidence are removed. Concrete strengths (the specific theorems and algorithmic contributions) are retained.
- **Various minor formatting/style nitpicks** are removed per the hard rules.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Provide a proof sketch of Proposition 4 in the main text** — Even a brief paragraph explaining the main idea of the equivalence would substantially increase reader confidence in the linchpin result and make the paper more self-contained.

2. **For a camera-ready version, run the bandit experiments with a known ground-truth optimal arm** — For small enough graphs (e.g., `asia` with 8 nodes), the true optimal conditional intervention can be computed by enumerating policies given the known CPTs, enabling regret relative to the true optimum.

3. **Report numeric mGISS sizes in the main text alongside the figure** — Add a table or text listing the exact node counts for each dataset's brute-force and mGISS sets.

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| IPayPEGwdE (Causal Contextual Bandits with Adaptive Context) | 5.00 | R1 mid | Our paper is stronger: complete characterization vs. restrictive assumptions |
| YcW8i9VCf5 (Adversarial Causal Bayesian Optimization) | 6.00 | R1 mid/R2 low | Our paper has cleaner theory, comparable contribution |
| ZXs3pkmrRG (Test-Time Learning of Causal Structure) | 5.50 | R1 mid | Different sub-area, our paper is stronger in theoretical completeness |
| w50MQ9Vfty (Independent-Set Design of Experiments) | 5.50 | R2 low | Not closely related topic |
| u63OVngeSp (Deriving Causal Order from Single-Variable Interventions) | 7.00 | R1 high/R2 high | Comparable theoretical contribution; our experiments are weaker |
| M0xK8nPGvt (Exploiting Causal Graph Priors for RL) | 7.50 | R2 high | Stronger paper overall (regret bounds, broader experiments) |
| Bp0HBaMNRl (Differentiable Causal Discovery for Latent Hierarchical Causal Models) | 6.75 | R2 high | Similar tier: clean theory with experimental limitations |

**Round 1 bracket:** Between 6.0 and 7.5.

**Round 2 narrowing:** The paper is clearly above the 5.0–6.0 anchors (which had more restrictive assumptions or weaker theory). It is below the 7.5 anchor (which had stronger theoretical analysis with regret bounds). It is comparable to the 7.0 and 6.75 anchors — papers with clean theoretical contributions but some experimental limitations. The experimental weakness (empirical oracle for regret) prevents the paper from reaching the 7+ tier but does not undermine the core theoretical contribution.

**Final score:** 6.5 — a solid theoretical contribution with an elegant characterization and practical algorithm, held back primarily by the regret computation issue and limited bandit experiment scope.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>