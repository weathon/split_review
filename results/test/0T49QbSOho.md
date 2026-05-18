Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper introduces the notion of *list replicability* to multi-armed bandits (and linear bandits). An algorithm is $(\ell,\delta)$-list replicable if with probability $\ge 1-\delta$, its traces (sequences of played arms) come from a set of size at most $\ell$. The paper provides three upper-bound algorithms achieving different trade-offs between list complexity and regret: Algorithm 1 ($(2^k,\delta)$-list replicable, $\widetilde{O}(\sqrt{kT})$ regret), Algorithm 2 ($(O(k/\delta),\delta)$-list replicable, $\widetilde{O}(\frac{k}{\delta}\sqrt{kT})$ regret), and Algorithm 3 ($((k+1)^{B-1},\delta)$-list replicable, $\widetilde{O}(k^{3/2}T^{\frac12+2^{-(B+1)}})$ regret). A matching lower bound (Theorem 6.1) shows that no $(k-1,\delta)$-list replicable algorithm can achieve $o(T)$ regret when $\delta\le 1/(k+1)$, establishing optimal list complexity $k$ in the sublinear-regret regime. The results extend to $d$-dimensional linear bandits.

## Strengths

1. **Novel and well-motivated definition.** The paper defines $(\ell,\delta)$-list replicability for MAB (Definition 2.2) and demonstrates non-trivial achievability — Algorithm 1 achieves list complexity independent of $T$ with near-optimal regret. This opens a new axis of analysis for bandit algorithms.

2. **Tight lower bound establishing optimal list complexity.** Theorem 6.1 proves that no $(k-1,\delta)$-list replicable algorithm can have $o(T)$ regret (for $\delta\le 1/(k+1)$), while a $(k,0)$-list replicable algorithm with $O(T^{2/3})$ regret exists. This sharp characterization is the paper's strongest theoretical contribution.

3. **Systematic trade-off between list size and regret.** The three algorithms (plus the linear bandit extension) exhibit a clear design space: from $(2^k,\delta)$ with near-optimal regret, through $(O(k/\delta),\delta)$ with $\widetilde{O}(\text{poly}(k)/\delta)$ regret, to $((k+1)^{B-1},\delta)$ with parametrically interpolated regret. The polynomial-in-$k$ list complexity of Algorithm 3 is particularly elegant.

4. **Extension to linear bandits.** Section 7 generalizes the batched-elimination approach to $d$-dimensional linear bandits, yielding $((2d+1)^{B-1},\delta)$-list replicability with $\widetilde{O}(d^2 T^{\frac12+2^{-(B+1)}})$ regret (Theorem 7.4), demonstrating the techniques' broader applicability.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Incorrect intermediate claim in Algorithm 2's analysis.** The paper states (line 107) that "the length of the approximation interval of $\Delta_i$ at round $b$ is exactly equal to the distance between consecutive shifts $\mathfrak{D}_{b,r}$ and $\mathfrak{D}_{b,r+1}$." From the definitions given ($\tau_b = 4C\varepsilon_b/(3(\sqrt2-1))$, $\mathfrak{D}_{b,r}=3\tau_b+(r-1)\cdot 3(\tau_{b-1}-\tau_b)/C$), the distance between shifts is $4/(\sqrt2-1)(\varepsilon_{b-1}-\varepsilon_b)=16\varepsilon_b/(\sqrt2-1)\approx 38.6\varepsilon_b$, which is *not* equal to the "bad" interval length $4\varepsilon_b$. The "exactly equal" claim is therefore mathematically incorrect. However, this does **not** affect the validity of the paper's conclusion: since the actual spacing ($\approx 38.6\varepsilon_b$) is *larger* than $4\varepsilon_b$, the claim that "at most 2 $\mathfrak{D}_{b,r}$s" lie in $[\Delta_i-2\varepsilon_b,\Delta_i+2\varepsilon_b]$ follows even more easily. The error is in the intermediate justification, not the result itself, and does not threaten the main claims. The authors should correct this statement in a revision.

2. **Unspecified constants in error bounds.** The constant $c$ in $\varepsilon_b$ definitions (e.g., $\varepsilon_b = \sqrt{\frac{c\,k}{5^{2b}C^2}\log\frac{2kB}{\delta}}$) is introduced but never assigned an explicit value. While common in theoretical papers, the derivation of Algorithm 2's shift spacing would benefit from explicit numeric relations, especially since the spacing constants are central to the argument. This is a minor expositional concern.

### Trivial
None.

## Nice-to-Haves

- The description of Algorithm 1 in Section 5.1 is quite brief (a single paragraph). While the full algorithm and analysis are in the appendix (as is standard for main-text space constraints), even a slightly more detailed sketch of the trace-counting argument in the main text would help readers follow the core idea without consulting the appendix.
- The lower bound sketch (Theorem 6.1) is compact; a slightly expanded description of how the Sperner/KKM coloring argument applies could improve readability.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism that Algorithm 1's analysis is missing from main text.** The critic claimed the algorithm is "unsubstantiated" and that the analysis appears only in the appendix. Per policy, the parser strips appendix content from all papers; the full algorithm and analysis exist in the original submission. **Removed** (per Hard Rule: missing appendix content).
- **Criticism that the lower bound sketch is insufficiently detailed.** The critic states the proof sketch is "too brief to verify critical steps" and calls for a "complete, rigorous proof." The full proof exists in the appendix (stripped by parser). **Removed** (per Hard Rule: missing appendix content).
- **Criticism that lemmas 5.6 and 5.9 are stated without proof.** These proofs are in the appendix. **Removed** (per Hard Rule: missing appendix content).
- **Criticism that Algorithm 1 pseudocode is missing from extracted text.** The parser stripped the pseudocode (likely an image or formatted block); it exists in the original submission. **Removed** (per Hard Rule: parser artifact).
- **Claim that the critic's own constant calculation gives ≈ 96ε_b/(√2-1).** My independent verification shows the correct value is 16ε_b/(√2-1). The critic's arithmetic is incorrect, but the underlying point (that the "exactly equal" claim is wrong) remains valid — kept as Minor weakness 1 above with corrected constants.
- **Generic strength from Strength Finder about "important problem."** Dropped as generic/non-specific.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Fix the erroneous "exactly equal" statement in Section 5.2.1 (line 107). Replace it with something like: "The distance between consecutive shifts $\mathfrak{D}_{b,r}$ and $\mathfrak{D}_{b,r+1}$ is sufficiently large ($\gg 4\varepsilon_b$) that at most 2 shifts can lie in the interval $[\Delta_i-2\varepsilon_b,\Delta_i+2\varepsilon_b]$." The conclusion remains correct; only the intermediate claim needs correction.
2. Consider providing explicit numeric values (or ranges) for the constant $c$ in $\varepsilon_b$ definitions to make the derivations more self-contained.

## Score and Decision

This is a solid theoretical paper that introduces a well-motivated notion, provides multiple algorithmic constructions with non-trivial guarantees, and establishes a matching lower bound that is essentially tight. The only verifiable weakness in the main text is a minor mathematical inaccuracy in an intermediate claim of Algorithm 2's analysis that does not affect the correctness of the paper's conclusions. All other criticisms raised by the harsh critic pertain to content that exists in the appendix (stripped by the parser) and are therefore inapplicable. The core contributions — the definition, the upper/lower bound interplay, and the linear bandit extension — are genuine and significant.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>