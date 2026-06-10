## Summary

This paper provides provable guarantees for privacy attacks on trained 2-layer ReLU neural networks, marking the first such rigorous results in this non-convex setting. It shows: (i) in the univariate case, an attacker can construct a candidate set of which at least 1/4 are training points (Theorem 5, Algorithm 1); (ii) in high dimensions, a membership inference attacker can distinguish training from test points with high probability by thresholding the network output against the margin (Theorem 4, Corollaries 1–3). Both results rely on the implicit bias characterization where trained networks converge to a KKT point of the max-margin problem.

## Strengths

1. **First provable (not merely empirical) guarantees for privacy attacks in this non-convex setting.** Prior work (Haim et al. 2022, Buzaglo et al. 2023) demonstrated reconstruction empirically but could not explain *why* it works. This paper provides rigorous lower bounds showing that any network parameter vector satisfying the KKT conditions of the max-margin problem necessarily encodes identifiable information about the training set. This is clearly scoped and distinguished from prior work (lines 51–52 contrast with Attias et al. 2024, which covers only convex models).

2. **Clean and intellectually satisfying high-dimensional membership inference result.** Theorem 4 — showing that training points satisfy $|\Phi(\theta; x)| = m$ while fresh points satisfy $|\Phi(\theta; x)| = o_d(m)$ — has a conceptually clear proof: near-orthogonal data combined with the KKT parameterization forces a separation in output magnitude. The progression of corollaries (known margin → leaked data point → bounded margin) demonstrates the attack's robustness to varying attacker knowledge.

3. **Black-box attack capability.** Remark 1 (lines 190–192) explicitly notes the membership inference attack requires only querying $\Phi(\theta;\cdot)$, not knowing $\theta$, making it applicable in realistic threat models where the attacker has only API access.

4. **Honest about limitations throughout.** The paper repeatedly flags where assumptions may not hold: the local-minimum requirement for univariate results (line 178), the restricted high-dimensional regime (line 318), and the gap between convergence-in-direction and exact KKT satisfaction (implicit in the structure). This transparency strengthens the paper's scholarly value.

## Weaknesses

### Fatal
None.

### Major
- **1. Gap between "converges in direction" and "exactly satisfies the KKT conditions" is acknowledged but not formally addressed.** Theorem 1 (lines 77–82) guarantees that gradient flow converges *in direction* to a KKT point — i.e., $\theta(t)/\|\theta(t)\| \to \theta^*/\|\theta^*\|$. Assumption 1 (lines 86–95) assumes the parameters $\theta$ *exactly* satisfy the KKT conditions, including equality constraints on $\theta$ itself (not just its direction). For homogeneous networks ($\Phi(b\theta; x) = b^c\Phi(\theta; x)$), the scaling of $\theta$ matters for the margin $m$, so convergence in direction does not imply finite-time exact KKT satisfaction. The paper acknowledges this only through the experiment's "approximate KKT point" phrasing (line 304) with no formal analysis of how approximation error propagates to attack guarantees. This means all theoretical results are contingent on an assumption that is not formally justified by the cited theorem.

- **2. Univariate reconstruction (Theorem 5) requires substantial additional assumptions whose status in the literature is uncertain.** Beyond the KKT conditions, Theorem 5 requires: (a) an always-active neuron, and (b) that $\theta$ is a *local minimum* of the max-margin problem, not just a KKT point. The paper acknowledges (line 178) that "not all critical points... are also local minima, and that gradient flow may converge to a critical point which is not a local minimum." It further states "it is not clear what is the 'typical' behavior of gradient flow in this context." For the always-active neuron, the paper suggests "modifying our architecture to have a linear neuron" (line 145), which changes the model to fit the theorem rather than proving the theorem for the architecture under study. Since the local-minimum question is unresolved, the univariate result's explanatory power for practical attacks is limited.

### Minor
- **3. Experiments lack standard reporting rigor.** The experimental section (Section 5) reports results for only one architecture (10,000 hidden neurons), one data distribution ($\sqrt{d}\cdot\mathbb{S}^{d-1}$), one training set size ($n=20$), and with no reported error bars, variance, or multiple random seeds. For a top-venue paper, at minimum means and standard deviations over several independent trials should be reported, even for a theory paper's sanity-check experiments.
- **4. No experiment on the univariate reconstruction claim.** The experiments only test the high-dimensional membership inference case. An experiment demonstrating the $1/4$ reconstruction fraction from Algorithm 1 on random univariate data would meaningfully strengthen the paper.
- **5. The claim "our theory is expected to hold more generally" (line 320) overreaches the empirical evidence.** The limited experimental scope (one architecture, one distribution, one $n$) does not justify broad generalization across settings.
- **6. The "modify architecture to add a linear neuron" suggestion (line 145) sidesteps the theoretical difficulty rather than resolving it.** While pragmatic, this effectively changes the object of study to make the theorem apply.

### Trivial
- None.

## Nice-to-Haves
- A perturbation/approximation analysis formalizing how the attack guarantees degrade when $\theta$ is within $\varepsilon$ of a KKT point (in some norm). This would bridge the central gap and convert the theory from a statement about idealized objects to one about realistically trained networks.
- A discussion of whether the max-margin KKT conditions are compatible with any level of differential privacy, or whether they inherently imply leakage exceeding any finite DP guarantee.

## Removed Points
- *"The constant fraction (≥ 1/4) is weaker than framing suggests"*: The paper states this result forthrightly ("a constant fraction $p \geq 1/4$"). A provable lower bound on the fraction of true training points in the candidate set is a legitimate theoretical contribution; the paper does not oversell it.
- *"The high-dimensional regime is too restrictive"*: The paper transparently states the regime and the experiments explicitly test below it, showing robustness. The theory covers its stated regime; the broader empirical phenomenon is presented as a bonus, not a claim.
- *"Differential privacy discussion not quantified"*: The paper explicitly notes results "are not directly comparable." Quantification would require bridging incomparable settings, which is outside the paper's scope.
- *"Univariate case analysis coverage is incomplete"*: The paper excludes degenerate cases ("at most two different intervals") with explicit justification — a standard practice for piecewise-linear analysis.

## Novel Insights

The harsh critic's central observation — that the gap between "converges in direction" and "exactly satisfies KKT conditions" is structural, and that the paper offers no formal bridge — is the most penetrating insight from the reviews. This is not merely a minor presentational gap; it is a missing link in the theoretical chain from the cited implicit bias literature to the paper's attack guarantees. The critic's suggestion to develop a perturbation analysis (quantifying how attack guarantees degrade under approximate KKT satisfaction) is the single most impactful improvement the paper could pursue. Beyond this, no genuinely novel insight emerges from the reviews beyond the paper's own contributions.

## Suggestions
1. **Address the KKT convergence gap formally.** The highest-leverage improvement would be a perturbation analysis: if $\theta$ is within $\varepsilon$ of a KKT point in an appropriate norm, how much do the attack guarantees (margin separation in Theorem 4, candidate-set purity in Theorem 5) degrade? This would convert the theory from conditional (on an idealized assumption) to operational.
2. Report means and standard deviations over multiple random trials in the experiments (even 5–10 trials).
3. Add a small-scale experiment on univariate reconstruction to demonstrate the $1/4$ fraction empirically.
4. Tone down the "expected to hold more generally" claim (line 320) to better match the limited experimental scope.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>