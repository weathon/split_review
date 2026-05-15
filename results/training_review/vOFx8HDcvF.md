I have thoroughly verified all claims against the paper. Now let me produce the consolidated review.

## Summary
This paper studies stochastic multi-armed bandits under adversarial attacks, where an attacker observes the learner's action before corrupting the reward. The authors propose four algorithms (SEWCR, SEWCRST, PEWCR, MSSEWCR) covering known/unknown attack budgets and additive/multiplicative regret dependence on the attack budget \(C\), and provide matching lower bounds establishing near-optimality in most cases. The work systematically quantifies the separation between the corruption (medium adversary) and attack (strong adversary) models, showing the attack model is fundamentally more harmful.

## Strengths
- **Tighter analysis for known-attack case that improves over prior work**: Theorem 1 gives \(O(\sum_{k\neq k^*} \frac{\log T}{\Delta_k} + KC)\) for SEWCR, removing the multiplicative \(\Delta_k^{-1}\) dependence on \(C\) present in Lykouris et al. (2018) — a genuine technical improvement explicitly stated and contrasted with prior work.
- **Matching lower bounds establishing near-optimality across multiple settings**: Proposition 1 gives \(\Omega(\sqrt{KT} + KC)\) and \(\Omega(\sum_{k\neq k^*} \frac{\log T}{\Delta_k} + KC)\) general lower bounds, matched (up to log factors) by SEWCR and SEWCRST. For the unknown-attack case, Propositions 3–4 give class-specific lower bounds \(\Omega(T^\alpha + C^{1/\alpha})\) and \(\Omega(C^{1/\alpha-1}T^\alpha)\) that are matched by PEWCR and MSSEWCR respectively.
- **Clear separation between corruption and attack models**: The paper demonstrates that attack is fundamentally more harmful — the additive regret term is \(\Theta(KC)\) vs. \(\Theta(C')\) for corruption, a factor of \(K\) worse — supported by the model discussion in Section 2.
- **Novel algorithms for unknown attack budget with tight theoretical bounds**: PEWCR achieves \(\tilde{O}(\sqrt{KT} + KC^2)\) (matching the \(\Omega(\sqrt{T}+C^2)\) lower bound at \(\alpha=1/2\)), and MSSEWCR achieves \(\tilde{O}(KC\sqrt{T})\) (matching \(\Omega(C\sqrt{T})\)). The multi-phase and model-selection techniques used to handle unknown attack budgets are technically nontrivial and clearly explained.
- **Comprehensive coverage of four algorithmic cases**: The paper systematically addresses all combinations of known/unknown attack budget and additive/multiplicative regret forms, summarized in Table 1, providing a complete typology of achievable regret under different information regimes.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Empty Experiments section (structural)**: The paper contains a section titled "Experiments" with no content — the text ends immediately after the header and jumps to the Conclusion. The paper's contributions are theoretical (algorithms with proven regret bounds and matching lower bounds), and many theory papers do not include experiments. However, the presence of an empty section header is unusual and the paper would be strengthened by even simple synthetic simulations (e.g., verifying regret scaling with \(C\) and \(T\) in a controlled setting). This does not invalidate the theoretical results but is a notable omission.
- **Tightness claims for unknown-attack case are slightly over-ambitious**: The paper states PEWCR's bound is "tight in terms of both \(T\) and \(C\)" (line 366) and MSSEWCR's bound "matches" the lower bound (line 407). While the paper does flag these as class-specific lower bounds via a footnote in Table 1 (the \(\ddagger\) marker) and in the text (Propositions 3–4), the language could create the impression of full optimality. The general lower bound (Proposition 1: \(\Omega(\sqrt{KT}+KC)\)) has a \(K\) dependence that differs from the \(C^2\) term in PEWCR's bound, and the class-specific bounds do not preclude better algorithms outside those classes. The claims are technically accurate relative to the class-specific bounds they reference, but clearer hedging would improve precision.

### Trivial
- The stopping condition derivation for SEWCRST's multiplicative bound (Section 4.2) is presented concisely; a reader unfamiliar with the standard gap-to-gap-independent conversion may need to fill in intermediate algebraic steps. The derivation is correct (the condition \(N_k \le T/K\) is obtained by plugging the optimal \(\epsilon\) into the parameterized condition), but the paper could show this simplification explicitly.

## Nice-to-Haves
- A concrete example of an attack policy (e.g., the one sketched in Section 2 where pulling the optimal arm triggers a reward perturbation below suboptimal means) with a simulated cost analysis would help illustrate the practical relevance.
- A cross-comparison between SEWCR and SEWCRST in simulation (the paper remarks SEWCR should perform better in practice) would be informative but is not required for a theory paper.

## Removed Points
These points are flagged to be removed, treat them with caution:

1. *"Unsupported claim that corruption-model algorithms do not work under attack"* (Harsh Critic Issue 3): The paper states (lines 173, 326) that corruption-robust algorithms rely on randomized action mechanisms, which are invalid under attacks because the adversary observes the pulled arm before corrupting. This is a straightforward logical argument (if the adversary sees which arm was pulled, randomization does not hide it), not an unsupported technical claim requiring a theorem. The paper provides this as motivation, and it is sound reasoning. **Removed: criticism misunderstands the nature of the claim.**

2. *"Incomplete specification of SEWCRST stopping conditions"* (Harsh Critic Issue 4): The reviewer claims the stopping condition \(N_k \le T/K\) "does not contain \(C\)" and the derivation is unclear. However, the paper explicitly derives this condition: starting from \(N_k \le (\log(KT/\delta)+C)/\epsilon^2\) and choosing \(\epsilon = \sqrt{(K\log(KT/\delta)+KC)/T}\), the condition simplifies to \(T/K\). The \(C\) dependence is absorbed into the optimized \(\epsilon\). The derivation is correct and self-contained. **Removed: criticism is based on a misreading of the derivation.**

3. *Strength Finder's "Identification of the core challenge"* (Supporting strength 2): The point about why prior corruption algorithms fail under attacks is already covered in the "Clear separation" strength above. This is redundant and generic when stated separately. Moved here for conciseness.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a perspective absent from the paper itself.

## Suggestions
1. Add a brief empirical section with synthetic experiments on stochastic MAB instances with varying \(K, T\), and \(C\) (both known and unknown cases) to demonstrate that the theoretical bounds translate to practice. This would significantly strengthen the paper for venues that expect empirical validation.
2. Add an explicit note in the tightness discussion (Section 5 and 6) clarifying which comparisons are relative to general lower bounds vs. class-specific lower bounds, even though the current footnote in Table 1 already flags this.

## Score and Decision

This is a solid theoretical paper with clean algorithmic contributions, nontrivial technical analysis, and matching lower bounds that establish near-optimality across multiple settings. The central claims are well-supported by theorems and proofs. The primary weakness — the absence of any experiments — is not fatal for a theory paper but is a notable gap given the presence of an "Experiments" section header. The slight over-claiming on tightness is minor and largely pre-empted by existing footnotes.

**Originality**: High — first comprehensive treatment of robust bandits under the strong adversary model.  
**Importance**: High — addresses a practically motivated and theoretically distinct problem from the corruption model.  
**Claims support**: Strong — theorems with proofs, matching lower bounds.  
**Soundness**: Good — derivations appear correct; no methodological flaws identified.  
**Clarity**: Generally clear; the algorithm exposition is well-structured.  
**Value**: Significant contribution to the theory of robust bandits.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>