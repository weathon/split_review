Now I have enough calibration to write the final review.

## Summary
The paper introduces *single-node conditional-intervention causal bandits* (without latent confounders), characterizes the minimal set of nodes guaranteed to contain an optimal-intervention node (the mGISS), and proves that this set equals the LSCA closure of $\mathrm{Pa}(Y)$, equivalently the set of Λ-structure roots. A linear-time algorithm (C4) computes it. Empirically, pruning to the mGISS reduces the search space on bnlearn graphs and speeds up cumulative-regret convergence of a UCB-based conditional bandit algorithm versus a brute-force baseline.

## Strengths
- **Clean main theoretical result.** Theorem 13 (Section 4) gives a complete, unique graphical characterization (Proposition 6 establishes uniqueness) of the minimal worst-case search space — the LSCA closure of $\mathrm{Pa}(Y)$ — for single-node conditional interventions. The result is elegant and likely to be reusable.
- **Λ-structure characterization (Theorem 12).** Provides a non-recursive, geometric reading of the LSCA closure that is both proof-enabling and pedagogically clear, with intuition figures (1a–d) chosen to motivate why naive heuristics (parents only, plain LCA) fail.
- **Linear-time algorithm with explicit correctness proof.** Algorithm 1 (C4) computes the closure in $O(|V|+|E|)$ via a single reverse-topological pass over connectors (Definition 14, Lemma 15, Theorem 16), making the method usable at scale.
- **Reduction in Proposition 4.** The equivalence between conditional-intervention superiority (stochastic SCMs) and deterministic atomic-intervention superiority is the technical pivot that makes the rest of the analysis tractable.
- **Careful scoping vs. prior work (Section 7).** The contrast with Lee & Bareinboim (2018; 2020) is precise: this paper handles single-node + conditional (no latents); they handle multi-node + hard interventions (with latents). The non-comparability is correctly identified, not papered over.
- **Search-space reduction validated.** Section 6 documents that on real bnlearn graphs the mGISS is much smaller than $\mathrm{An}(Y)$ (over 90% pruning on some large graphs), with random-graph trends consistent with the Λ-structure intuition (sparser graphs → more pruning).

## Weaknesses

### Fatal
None.

### Major
- **The bandit experiment compares only against the strongest possible strawman (Figure 3).** The only baseline is CondIntUCB with no pruning at all ("brute-force, $X$ nodes"). This conflates two effects: (i) UCB on fewer arms converges faster, and (ii) the *specific* arms removed are the right ones. The paper's intuition (Figures 1a–d) targets (ii), but the experiment only demonstrates (i). The natural intermediate baselines — restricting to $\mathrm{Pa}(Y)$ alone, to $\mathrm{An}(Y)$, or to a random subset of $|\mathrm{mGISS}|$ ancestors — would directly test whether the *closure under LSCAs* is what matters. Without one of these, the empirical case that C4 captures the right search space, rather than just a smaller one, is not made. This is the most important fix because Section 6 is the only validation of practical impact.
- **Non-standard regret in the bandit experiment (footnote 11).** Cumulative regret is computed against "the arm that most runs concluded to be the best at the end of training," i.e. an empirical mode over runs of *both* methods, not the true optimal arm. Since the underlying SCM is the known bnlearn network, true-optimum regret is available and would be the natural choice. The brute-force run may simply have failed to identify the true best arm within the horizon, contaminating the proxy in a direction that favours the proposed method. A sanity check against true-optimum regret on at least one dataset would close this loop.

### Minor
- **The mGISS is a worst-case-over-SCMs object.** Definition 5 and Theorem 13 establish that the mGISS contains an optimal arm *for every* SCM compatible with $G$. For any fixed SCM the per-instance smallest sufficient set can be much smaller, so the "fraction of nodes pruned" numbers measure how restrictive the *graph alone* is, not how many arms a practitioner with partial SCM knowledge could remove. The paper would benefit from making this distinction explicit and discussing when the mGISS is loose vs. tight.
- **No body-level intuition for why Proposition 4 holds.** The equivalence between worst-case stochastic conditional superiority and worst-case deterministic atomic superiority is the central technical pivot; one or two sentences of intuition (presumably about the SCM constructions that witness inferiority in the appendix proof) would make the rest of the paper substantially easier to read.
- **Motivation/scope misalignment.** The kidney-function example (weekly interventions on weight, blood pressure, renal flow over 3 weeks) and the cited medical/gene-network/advertising motivations are exactly the cases where multi-node interventions and latent confounding are routine. The authors acknowledge this and explicitly position single-node + no-latents as a necessary first step, which is fair, but the worked motivating example does not fit the formal scope and slightly inflates perceived applicability.
- **Choice of $Y$ as "the node with the most ancestors" interacts with the reported metric.** Section 6 reports the fraction of $\mathrm{An}(Y)\setminus\{Y\}$ that remains in the mGISS, while $Y$ is chosen to maximise $|\mathrm{An}(Y)|$. Choosing a target with many ancestors inflates the denominator and so the apparent reduction. A second target selected differently (e.g., a clinically meaningful node) would strengthen the empirical claim.
- **The "observable conditioning set" assumption $W \in \mathrm{An}(X) \Rightarrow \mathbf{Z}_W \subseteq \mathbf{Z}_X$ deserves a sentence on restrictiveness.** It implicitly assumes monotone information accrual; in some realistic settings observation has its own cost or constraints. The paper uses the assumption substantively but introduces it only via an example.

### Trivial
- The body reports Erdős–Rényi pruning percentages but defers average degrees and node counts to the appendix bar plot; stating these inline would make Section 6 self-contained.
- Figure 3 caption mentions standard deviations but the figure description is not explicit about whether shaded bands are shown.

## Nice-to-Haves
- A "tightness of the mGISS from a practitioner's view" discussion: when does the worst-case mGISS coincide with the true per-SCM optimal-singleton set, and when is it loose?
- A few lines on how to use C4 under graph uncertainty (the intro one-sentence "apply to each candidate graph and union" remark is the right idea but underdeveloped).
- A body-level paragraph unpacking the intuition behind Proposition 4 — turning a technical lemma into a conceptual centerpiece.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- *Single-node / no-latents restriction is a "structural" weakness.* The paper is explicit about the scope and explicitly argues why the single-node + conditional + no-latent case is itself non-trivial; the harsh critic concedes this. This is scoping, not a flaw.
- *"Strawman baseline is a methodological gap rather than structural."* Already captured under Major; not a separate weakness.
- *Generic Strength Finder claim that "the paper addresses an important problem."* No concrete content beyond what the Strengths section above already documents.
- *Generic "empirical regret improvement"* phrased absolutely. The improvement is real but, as noted in Major Weakness 1, is partly attributable to having fewer arms — so the strength is conditional on the baseline being legitimate.

## Novel Insights
None beyond the paper's own contributions. The Λ-structure characterization, the LSCA closure, and the conditional↔deterministic-atomic reduction are themselves the substantive new ideas; nothing surfaces from the reviews beyond them.

## Suggestions
- Add at least one intermediate baseline in Figure 3 — most naturally $\mathrm{Pa}(Y)$-only and/or $\mathrm{An}(Y)$ — to isolate the value of LSCA-closure pruning over generic pruning.
- Recompute (or supplement) regret in Figure 3 against the true optimal arm on at least one dataset.
- Add a paragraph of intuition for Proposition 4 in Section 3.
- Add a short discussion of mGISS tightness per-SCM and of graph-uncertainty handling.
- Report average degree and node counts for the random and bnlearn experiments inline.

---

**Axis-level assessment.** *Originality:* clearly new — first complete characterization of the minimal search space for single-node, non-hard intervention causal bandits, with a graphical structure (Λ) that has no direct prior analogue in the cited literature. *Importance:* moderate-to-high within causal bandits; the result is a natural search-space pre-processor and connects cleanly to Lee & Bareinboim's program. *Claims well supported:* yes for the theoretical claims (proofs in appendix), only partially for the "accelerates real bandits" claim due to the baseline choice and regret proxy. *Soundness of experiments:* limited; the search-space-reduction experiments are convincing, the bandit experiment is not on the firmest footing. *Clarity:* generally good — Sections 4 and 5 are well-organized, intuition figures help, but Proposition 4's intuition is under-explained in the body. *Value to the community:* solid contribution that is likely to be cited within causal-bandits and structural-search-space work.

---

**Calibration trace.**
- Round 1 (bracketing):
  - AvXrppAS2o (avg 3.00, Reject) — causal structure for outcome prediction, not a bandit paper; much weaker scope/topic match.
  - fSxiromxAq (avg 3.00, Reject) — sparse causal model; off-topic.
  - JzFLBOFMZ2 (avg 3.20, Reject) — LLM-supervised CSL; off-topic.
  - TRHyAnInUC (avg 3.25, Reject) — diffusion-based causal discovery; off-topic.
  - IPayPEGwdE (avg 5.00, Reject) — causal contextual bandits with adaptive context; closest topical match in mid band, more applied/algorithmic than this paper, weaker theoretical core.
  - MVpvyeVeyI (avg 6.50, Reject) — CBO without known graph, focuses on parents of $Y$; mixed reviews.
  - YcW8i9VCf5 (avg 6.00, Accept) — adversarial CBO with regret bounds; comparable strength but with stronger experiments.
  - ZXs3pkmrRG (avg 5.50, Reject) — TICL for interventional causal discovery; tangential.
  - xByvdb3DCm (avg 8.00, Accept) — causal discovery with selection bias; topically distant.
  - 3cuJwmPxXj (avg 8.00, Accept) — intervention extrapolation; tangential.
  - Nx4PMtJ1ER (avg 8.00, Accept) — signature-kernel CI tests for SDEs; topically distant.
  - A3YUPeJTNR (avg 8.00, Accept) — prediction timing; off-topic.

  Round-1 bracket: between 5 and 7. The strong-band anchors are not topically close, so they only set an upper edge.

- Round 2 (narrowing):
  - IPayPEGwdE (5.00, repeat) — re-anchor; conditional bandits with weaker theory than this paper.
  - oVVLBxVmbZ (avg 5.25, Reject) — RL-based conditional intervention for recourse; tangential.
  - BZYIEw4mcY (avg 6.00, Accept) — causal discovery with latents in polynomial time; theoretical + algorithmic, similar acceptance regime.
  - KWO8LSUC5W (avg 5.60, Accept) — DAG structure learning with smooth orientations; clean theoretical contribution.
  - nHkMm0ywWm (avg 6.50, Accept) — partially observed LiNGAM identifiability; clean theoretical contribution.
  - oCdIo9757e (avg 7.00, Accept) — analytic DAG constraints; strong theory, well-supported.
  - M0xK8nPGvt (avg 7.50, Accept) — causal-graph priors for PSRL; strong theory + non-trivial experiments.
  - u63OVngeSp (avg 7.00, Accept) — causal order from single-variable interventions; theoretical guarantees + clear empirical wins on multiple baselines.
  - vrE2fqAInO (avg 7.00, Accept) — fixed-budget DP best-arm-ID; matching upper/lower bounds.

  Round-2 read in detail: IPayPEGwdE (5.0), YcW8i9VCf5 (6.0), MVpvyeVeyI (6.5), u63OVngeSp (7.0). Compared to IPayPEGwdE the paper has a cleaner, more reusable theoretical object and a linear-time algorithm — better. Compared to YcW8i9VCf5 (Accept 6.0) the theory here is sharper and tighter, but the empirical validation is weaker (single baseline, non-standard regret). Compared to u63OVngeSp (Accept 7.0) the empirical evaluation is materially less rigorous (no real baselines beyond brute force). The paper sits above the 5.0 anchor and roughly at the 6.0 anchor, below the 7.0 anchors. Narrowed range: 5.5–6.5. I place it at 6.0 — the elegant theoretical core sits at accept-tier among comparable anchors, but the weak experimental section keeps it from the 6.5–7.0 anchors.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>