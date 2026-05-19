- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5
Now I have a thorough understanding of the paper and both reviews. Let me construct the final consolidated review.

---

## Summary

The paper proposes a procedure based on the proximal point method (PPM) to generate an entire set of approximate Pareto-efficient robust solutions in essentially two algorithmic passes — one for the most-robust solution, one for the nominal problem. The key insight is that the PPM trajectory (starting from the robust solution and iterating toward the nominal solution) traces out the efficiency-robustness Pareto frontier. For robust linear programs with simplex domain and ellipsoidal uncertainty, the paper proves exact equivalence (Theorem 1). A probabilistic bound extends support to random polyhedron domains (Corollary 1). Experiments on portfolio optimization and adversarially robust deep learning provide empirical validation.

## Strengths

1. **Rigorous exact equivalence for a nontrivial problem class.** Theorem 1 proves that under linear objectives, simplex domain, and ellipsoidal uncertainty sets (with Σ⁻¹e ∈ ℝⁿ₊), every PPM iterate is *exactly* a Pareto-efficient robust solution. This is not a heuristic or approximation — the trajectory coincides with the true Pareto frontier. This provides a strong theoretical foundation for the method.

2. **Meaningful computational savings demonstrated with transparent cost breakdown.** Table 1 reports concrete costs: generating 100 robust networks costs 15.12 + 0.25×99 = 39.87 minutes with Algorithm 1 vs 15.12×100 = 1512 minutes with re-solving. The cost structure is fully disclosed (line 323), showing savings that grow linearly with N. The reduction is real and substantial even if the $2T$ framing is slightly loose (see Weaknesses).

3. **Portfolio experiment convincingly shows the method works beyond its theoretical guarantees.** The portfolio experiment (Section 5.1) shows excellent match between the PPM trajectory and the exact Pareto frontier, even when the Σ⁻¹e ∈ ℝⁿ₊ condition of Theorem 1 is *not* satisfied, and when the domain is extended beyond the simplex (Markowitz++). Both in-sample and out-of-sample results are provided, making this the strongest empirical evidence for the method.

4. **Probabilistic performance bounds for random polyhedron domains.** Corollary 1 provides a theoretical guarantee (with probability 1−1/m) that the robustness of random-polyhedron Pareto solutions is sandwiched between two simplex-based (hence PPM-trajectory) solutions, extending theoretical support beyond the exact simplex case.

5. **Integration of distinct technical ideas.** The paper connects proximal point methods, central paths, mean-variance risk minimization, and robust optimization into a single coherent framework, revealing a structural relationship not previously exploited for efficient Pareto frontier generation.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The "$2 \times T$" cost claim in the abstract and introduction is imprecise.** The abstract states the reduction is "from $N \times T$ to $2 \times T$ where $T$ is the time to obtain one robust solution." However, the second pass (standard/nominal training) is not a robust optimization problem and has a different cost structure. In the adversarial ML experiment (Table 1), the actual total cost for N=100 is $15.12 + 0.25(N-1) = 39.87$ minutes, whereas $2T = 2 \times 15.12 = 30.24$ minutes — a 32% difference. The paper is fully transparent about the actual costs in Table 1 and line 323, so this does not mislead a careful reader, but the headline framing overstates the reduction. The paper should replace "$2 \times T$" with a more precise expression such as "$T_{\text{robust}} + T_{\text{nominal}}$" and note that nominal training is cheaper per iteration.

2. **The adversarial ML experiment has limited scope and statistical rigor.** (a) Only one random seed is used; no standard deviations or confidence intervals are reported. (b) Adversarial robustness is evaluated only with PGD attacks; results under AutoAttack or other attacks would strengthen the claim that the robustness is real (not gradient masking). (c) The comparison baseline uses only four discrete radii $\{2,4,6,8\}$, and no attempt is made to interpolate between them (e.g., early-stopping adversarial training at different epochs). The trajectory matches/surpasses the $r=8,6,4$ points but then degrades; without denser baselines, it is unclear whether the trajectory truly approximates the full Pareto frontier or merely passes near the four evaluated points.

3. **The adversarial ML trajectory only covers part of the Pareto frontier.** The paper acknowledges (line 321) that later epochs produce networks with both lower clean and adversarial accuracy than the $r=2$ baseline. The trajectory thus yields useful networks only for the high-robustness portion of the frontier (roughly corresponding to $r \ge 4$). The claim of generating "100 Pareto efficient robust networks" is misleading if many of those networks are dominated. The paper attributes this to learning rate choices but does not demonstrate that retuning could recover the full frontier — a natural follow-up that should at least be discussed.

4. **Constant learning rates do not satisfy the theoretical PPM condition.** Algorithm 1 requires $\sum \lambda_k^{-1} = \infty$ for the PPM-central-path equivalence (Proposition 1). The experiments use constant learning rates, which do not meet this condition. The paper does not discuss whether this gap affects the quality of the approximation. This is a standard practical heuristic, but it deserves comment.

5. **No formal definition of "approximate" Pareto efficiency.** The paper describes the method as generating "approximate Pareto efficient robust solutions" but never defines an approximation metric (e.g., distance to true frontier, domination gap). For the adversarial ML experiment, quantifying the discrepancy between the trajectory and a denser baseline would make the approximation claim more precise.

### Trivial
- The multiple-constraint section (Proposition 4, Algorithm 2) is presented as an extension, but it requires solving a saddle-point problem for each $\alpha$ separately and does not achieve the one-pass benefit. The paper is honest about this (line 233: "running for a set of $\alpha$ values"), so this is not a flaw, but the section feels disconnected from the main contribution and could be shortened or moved to an appendix.

## Nice-to-Haves
- Reporting results under AutoAttack (or another attack) for the adversarial ML experiment would strengthen the robustness evaluation.
- Adding standard deviations / confidence intervals to both experiments would improve statistical rigor.
- The paper could compare against simple baselines such as linear weight-space interpolation between robust and nominal networks, or multi-objective optimization methods.
- A discussion of how to select the number of PPM iterations (i.e., when to stop generating networks) would be practically useful.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about missing proof for Corollary 1**: The harsh critic states "the paper does not include the proof or even an outline, making it unverifiable." The appendix (which is present in the original submission but stripped by the PDF parser) likely contains this proof. Removed per instructions: remove criticisms about missing appendix content.

- **Criticism that Proposition 2 is not novel and should cite Markowitz's critical line algorithm**: Per instructions: "DO NOT mention missing related works, as you do not have external sources to confirm their existence and could be making things up." Removed.

- **Criticism about the cost per network in Table 1 being $0.25$ when it should be amortized**: The table presents marginal cost (0.25 min per additional network after the initial robust pass). The total cost formula (15.12 + 0.25(N-1)) is correct and fully transparent. The "cost per network" of $0.25$ for Algorithm 1 could be read as marginal cost, which is a reasonable presentation choice. Not a genuine weakness.

- **Criticism that the theory is too narrow and does not generalize to adversarial ML**: The paper explicitly states (line 167) that the adversarial ML experiment tests "general problems where the conditions for our exact results in Theorem 1 no longer hold." The paper is transparent about the theory-practice gap. Removed because the paper addresses this explicitly.

- **Multiple constraints section described as "does not contribute to the main claim"**: The paper frames this as an extension (line 218-233) and does not claim it achieves the one-pass benefit. Not a valid criticism of the paper's core contribution.

- **Strength Finder claim #4 about "integration of multiple distinct technical ideas"**: This strength is kept in a reduced form in the Strengths section because it has concrete content (the paper indeed synthesizes PPM, central paths, and mean-variance/robust optimization connections). The version presented here is specific and evidence-backed.

- **Strength Finder claim #6 about "extension to multiple uncertain constraints"**: This is a valid but tangential contribution. It is not strong enough to be a core strength since it does not support the main one-pass claim. Moved to Removed Points.

## Novel Insights

None beyond the paper's own contributions. The two reviews do not surface a perspective on the paper's significance that is not already articulated by the authors.

## Suggestions

1. Rewrite the cost claim in the abstract and introduction to say "$T_{\text{robust}} + T_{\text{nominal}}$" or "$T + (N-1)C$ with $C \ll T$" rather than "$2 \times T$." The actual cost structure in Table 1 is correct — just align the headline language with it.

2. Add statistical confidence (multiple seeds, error bars) to the adversarial ML experiment. Report results under a second attack (e.g., AutoAttack) to confirm robustness is not due to gradient masking.

3. Add a denser set of baseline points for the adversarial ML Pareto frontier (e.g., by early-stopping adversarial training at different epochs, or by using linear scalarization with random weights) so the reader can assess how well the PPM trajectory approximates the true frontier between the anchor points.

4. Discuss why constant learning rates are used despite the theory requiring $\sum \lambda_k^{-1} = \infty$, and explain what impact (if any) this practical choice has on the quality of the approximation.

5. Provide a formal definition of "approximate Pareto efficiency" with a quantifiable metric, and report it in the experiments.
