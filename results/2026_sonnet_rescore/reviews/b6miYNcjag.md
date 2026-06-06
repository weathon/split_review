## Summary

The paper introduces the *Gram Determinant Score*, a task-agnostic and experiment-agnostic metric for assessing dataset reliability from potentially manipulated reports and auxiliary observations, without access to ground truth. The central contributions are: (1) formalization of ground-truth-based reliability orderings (exact match, Blackwell dominant, dist/Hamming) and their refinement relations; (2) impossibility results that scope the feasible regime; (3) proof that the Gram Determinant Score preserves these orderings under mild conditions; and (4) a uniqueness result (experiment agnosticism) showing the score is, up to scaling, the only score that induces consistent dataset rankings regardless of the unknown experiment.

---

## Strengths

- **Clean formalization of reliability orderings and their refinement hierarchy**: Section 2.3 defines three distinct partial orders (exact match, Blackwell dominant, dist/Hamming) and Proposition 2.1 formally proves their nesting, providing a rigorous benchmark framework that does not rely on ground truth. This is a concrete and novel structural contribution.

- **Elegant proof technique via the multiplicative decomposition of the determinant**: The key algebraic insight — $\Gamma(PQ) = \det(P^\top P)\det(Q)^2$ — cleanly decouples the unknown experiment quality from the misreport severity. This provides both an interpretable geometric intuition (volume of a parallelepiped) and a clean technical basis for all subsequent results.

- **Impossibility results are rigorous and operationally tight in spirit**: Proposition 3.1 correctly demonstrates that no score can preserve Hamming or dist orderings under $\mathcal{P}_\text{indep}$ and $\mathcal{Q}_\text{dom}$, directly motivating the paper's restriction to $\mathcal{Q}_{L,\delta}$. These negative results prevent the paper from overclaiming and properly delimit the feasible scope.

- **Uniqueness/experiment agnosticism (Proposition 4.3)**: The result that the Gram Determinant Score is the unique continuous, scaling-equivariant experiment-agnostic score (up to scaling) under $GL_d$ is a non-trivial characterization result. This positions the determinant not merely as a convenience, but as the canonical choice in its class.

- **Kernel extension enabling continuous observation spaces**: Definition 4.6 generalizes the score to arbitrary $\mathcal{Y}$ (e.g., $\mathbb{R}^8$ SimCLR embeddings), and Experiment 2 demonstrates the extension works in practice on CIFAR-10, significantly broadening practical applicability.

- **Diverse empirical validation**: Three qualitatively distinct settings — synthetic categorical data (6 manipulation policies), CIFAR-10 embeddings (continuous $\mathcal{Y}$), and real CES employment data — all show the score correlating correctly with corruption level, demonstrating consistent behavior across data types.

---

## Weaknesses

### Fatal
None.

### Major

- **The dist/Hamming ordering guarantee applies only in a regime far narrower than the experiments test, with no acknowledgment of this gap.** Theorem 4.2, part 3, requires $Q \in \mathcal{Q}_{L, 1/64L^2d^2}$, which bounds the Hamming distance between reported and true data to at most $N/(64L^2d^2)$. For Experiment 1's setup ($d=5$, $L=1$, $N=4000$), this caps corruption at roughly $4000/1600 \approx 2.5$ mismatched entries, i.e., ~0.06% corruption. The experiments sweep corruption from 0% to 50%. The paper does not acknowledge that the theoretical guarantee for part 3 of Theorem 4.2 does not apply in the experimental regime. This is not fatal — empirical performance can exceed theoretical bounds — but claiming the positive result is "nearly matching" the impossibility results (Section 4.1) requires more care: $\mathcal{Q}_\text{dom}$ allows unlimited corruption while $\mathcal{Q}_{L,1/64L^2d^2}$ allows only a vanishingly small fraction, and the paper presents this as a near-tight relationship without quantifying the gap.

- **The experiments provide no comparison against any baseline dependence measure.** All three experiments evaluate the Gram Determinant Score in isolation — its monotone correlation with corruption level is established, but it is never compared against simpler alternatives (e.g., mutual information between $\hat{x}$ and $y$, classifier accuracy, or basic correlation measures). The theoretical uniqueness result (Proposition 4.3) argues the score is the canonical choice, but the experiments do not demonstrate empirically *why* experiment-agnosticism matters or whether simpler measures would behave differently. Without this, readers cannot assess whether the score provides practical advantages over off-the-shelf dependence measures.

### Minor

- **The "nearly tight" claim in Section 4 is imprecise.** The text states the conditions in Theorem 4.2 are "nearly matching our impossibility results." But the gap between $\mathcal{Q}_{L,1/64L^2d^2}$ (tiny corruption budget) and $\mathcal{Q}_\text{dom}$ (unlimited corruption) is large and depends on $d$ polynomially. The claim that these sets are "nearly" comparable deserves quantification or qualification rather than being stated as if the tightness is self-evident.

- **The uniqueness result in Proposition 4.3 is restricted to $|\mathcal{Y}| = |\mathcal{X}|$, and the paper offers no discussion of the over-determined case.** The proof requires $Q, P \in GL_d$, which forces $|\mathcal{Y}| = |\mathcal{X}|$. Yet the kernel extension in Section 4.3 and Experiment 2 explicitly operate with $|\mathcal{Y}| \gg |\mathcal{X}|$ (8-dimensional embeddings, 10 classes). The paper acknowledges the restriction briefly but does not discuss whether a similar uniqueness characterization holds in the over-determined regime, leaving experiment agnosticism formally uncharacterized for the setting where it is most practically relevant.

- **Proposition 4.5 establishes only asymptotic preservation; the conclusion claims "finite-sample guarantees."** The main body proves only that the plug-in estimator asymptotically preserves the orderings in Theorem 4.2. The conclusion states "We develop plug-in and stratified-matching estimators with finite-sample guarantees," which suggests finite-sample bounds exist but are not shown in the main body (deferred to appendix). This creates a disconnect between the abstract claims and what is verifiable from the main paper.

### Trivial

None.

---

## Nice-to-Haves

- **An experiment directly exhibiting experiment agnosticism**: Take the same corrupted dataset, evaluate under two different experiment matrices $P$ and $P'$; show that a non-agnostic baseline (e.g., mutual information) produces different reliability rankings under $P$ vs. $P'$, while the Gram Determinant Score produces the same ranking. This would directly convert the theoretical uniqueness result into a visible empirical distinction.

- **Discussion of whether Proposition 4.3's uniqueness extends to $|\mathcal{Y}| > |\mathcal{X}|$**: Even an informal conjecture would be valuable given how prominently experiment agnosticism is featured as the key differentiator.

- **A broader gap discussion on the $\mathcal{Q}_{L,\delta}$ restriction**: A brief bound showing, e.g., how $\delta$ scales with $d$ and $L$ to maintain guarantees would contextualize the "nearly tight" claim more rigorously.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Harsh critic" framing criticism: introduction oversells generality by describing multi-agent, temporal, and spatial scenarios.** The paper explicitly scopes to a single agent and i.i.d. data in Section 2.1, and the introduction correctly states "we assume access to outcomes of unknown statistical experiments." The examples (insurance telematics, COVID counts) are illustrative motivations, not formal claims. Removed as a framing non-issue.

- **Criticism of Experiment 3 (CES): the result is "qualitatively expected."** The harsh critic argues that revisions bringing data closer to truth is trivially expected. While the result is intuitive, it demonstrates the score works on real economic data with no ground truth available to the scorer — exactly the paper's claimed setting. The result is informative as a proof-of-concept, not trivial. Partially retained as a "nice-to-have" (noting that the conditions assumed by the theory are not verified for this dataset), but the core observation that the result is "not surprising" is removed.

- **Missing comparison with Kong (2024) in the main body.** The harsh critic asks for a summary of the distinction. However, the paper explicitly defers this to the appendix (which the parser strips). Per rules, criticisms about missing appendix content are removed.

- **Strength: "addresses an important problem."** Generic; removed. Concrete strengths about formalization, uniqueness, and kernel extension retained instead.

---

## Novel Insights

The paper's most genuinely distinctive insight is the algebraic decoupling $\Gamma(PQ) = \det(P^\top P) \cdot \det(Q)^2$, which converts experiment-agnostic reliability scoring into a pure question about $\det(Q)$, freeing the score from dependence on the unknown $P$. The uniqueness proof (Proposition 4.3) then shows this decoupling is not an accident but a *characterization*: up to scaling and continuity, the Gram Determinant Score is the only score with this property. This connection between geometric volume, matrix factorization, and reliability ordering is clean and non-obvious. The impossibility results further clarify that no score can achieve the same ordering preservation with weaker structural assumptions, making the framework's boundaries precise.

---

## Suggestions

1. **Acknowledge the gap between the $\mathcal{Q}_{L,1/64L^2d^2}$ regime and the experimental corruption range.** A short paragraph noting that the score works well empirically beyond the theoretical regime, and conjecturing why (e.g., monotone decay of the determinant), would strengthen the paper's intellectual honesty and empirical discussion.

2. **Add a direct experiment-agnosticism demonstration.** Fix a corrupted dataset, evaluate under two distinct P matrices, show that a natural non-agnostic alternative (e.g., $\hat{x}$-$y$ mutual information) gives inconsistent rankings while the Gram Determinant Score does not. This would be the most impactful addition to the experimental section.

3. **Clarify the scope of "finite-sample guarantees" in the abstract/conclusion.** If these are in the appendix, a brief forward reference in Section 4.2 (e.g., "finite-sample bounds are in Appendix E") would align the claim with what appears in the main body.

4. **Quantify the gap in the "nearly tight" claim.** For Theorem 4.2, part 3, include a brief comparison: "the impossibility requires $\mathcal{Q}_\text{dom}$ (no bound on corruption); our positive result requires corruption $\leq N/(64L^2d^2)$, a factor of $64L^2d^2$ below the threshold." This makes the tightness claim precise.

---

## Score and Decision

**Originality**: The problem of experiment-agnostic reliability scoring is newly introduced, and the Gram Determinant Score's characterization as the unique such score is non-trivial. The algebraic insight is clean and original. **4/5**

**Importance of research question**: Data reliability assessment without ground truth is a practically significant problem across many real-world domains. The formalization fills a genuine gap. **4/5**

**Claims well-supported**: The core theoretical claims (Theorem 4.2, Proposition 4.3) are proven under clearly stated conditions. However, the major theory-practice gap in the dist ordering guarantee (applies at <0.1% corruption; tested up to 50%) undermines the claimed connection between theory and experiments. No baselines limit empirical claim support. **3/5**

**Soundness of experiments**: Three diverse datasets, 6 manipulation policies, convergence study — methodologically sensible. The critical missing element is any baseline comparison, which leaves the score's practical advantage undemonstrated. **3/5**

**Clarity of writing**: The paper is generally well-organized with a clear logical flow from impossibility → positive result → estimators → experiments. Minor imprecision in the "nearly tight" framing. **4/5**

**Value to research community**: The formal framework and impossibility results are valuable independent contributions. Experiment agnosticism is a practically motivated and theoretically grounded property. The paper opens a new line of work. **4/5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>