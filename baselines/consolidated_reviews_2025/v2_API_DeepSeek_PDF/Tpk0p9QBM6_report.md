## Summary
# Final Review Report

## Summary

This paper addresses the problem of computing low-entropy couplings (minimum-entropy joint distributions with given marginals) for distributions with very large supports, where standard log-linear MEC approximation algorithms are intractable. The authors make three contributions: (1) they unify existing iterative minimum-entropy coupling (IMEC) algorithms under a single formalism using sets of partitions over the support of one marginal; (2) they derive ARIMEC (Autoregressive IMEC), a new algorithm using a prefix tree partition set that — unlike prior IMEC variants — can handle arbitrary discrete distributions without requiring factorization or small-support assumptions, introducing lazy posterior updates and entropy-based pruning for efficiency; (3) they empirically demonstrate ARIMEC's utility in Markov coding games and steganography, showing improved communication rates.

The paper is well-structured, technically sound in its algorithmic derivations, and addresses a genuine gap: prior IMEC algorithms (TIMEC, FIMEC) were limited to specific distribution classes. The unified formalism is an elegant intellectual contribution. However, the experimental evaluation has weaknesses — most notably asymmetric baselines that conflate prior correctness with algorithmic advantage, missing quantitative reporting, and limited analysis of the interesting FIMEC-vs-ARIMEC trade-off in steganography. The runtime guarantee depends on an unconstrained pruning parameter Z, making worst-case complexity unclear. Novelty verification is deferred due to external retrieval unavailability in this run.

## Strengths
1. **Clear problem identification and gap analysis:** The paper correctly identifies a genuine limitation in prior IMEC algorithms: they require either small support or factorable distributions. The motivation for a general large-support coupling algorithm is well-articulated.

2. **Elegant unified formalism:** The unification of TIMEC and FIMEC under a single partition-set framework (Algorithm 3, Section 3) is a non-trivial conceptual contribution. Expressing both existing methods as special cases of a single algorithm with different partition sets U provides clarity and enables systematic derivation of new variants.

3. **Novel algorithmic design (ARIMEC):** The prefix tree partition set (Definition 4.4) is a creative solution to the problem of constructing partitions that capture autoregressive structure. The pruning bound (Proposition B.2) and lazy update strategy (Proposition B.1) are well-motivated techniques to address the exponential complexity of naive prefix tree enumeration.

4. **Two diverse application domains:** The experiments span Markov coding games and two types of steganography (information-theoretic and unencrypted), demonstrating breadth of applicability. The 95% bootstrap confidence intervals from 100 samples suggest reasonable statistical practice.

5. **Theoretical grounding:** Propositions 3.1 (Coupling) and 3.2 (Greediness) provide formal guarantees that any IMEC instance (including ARIMEC) produces a valid coupling and greedily minimizes conditional entropy. The runtime analysis in Appendix B is thorough.

## Weaknesses
1. **Weak experimental baselines (Major):** The MCG experiments compare ARIMEC against only one baseline — a deliberately weakened FIMEC variant that uses an incorrect uniform prior. The unencrypted steganography comparison similarly conflates prior correctness with algorithmic advantage. Without a fair comparison where both methods use the same prior (correct), the claimed superiority of ARIMEC over FIMEC cannot be fully attributed to the algorithmic mechanism.

2. **Missing quantitative reporting (Major):** The text states ARIMEC produces "substantially more efficient encoding" but provides no numerical error rates, entropy values, or information throughput numbers. Readers must visually estimate from figures. Key quantities from Figures 3-5 should be reported numerically in the text or a table.

3. **Unbounded worst-case runtime (Major):** Proposition 4.1 expresses ARIMEC's runtime in terms of Z (nodes checked), which under naive implementation is O(N^n) — exponential. Practical efficiency hinges entirely on the pruning bound (Proposition B.2), whose condition q < 1 - 1/N may not hold in early iterations or for small-alphabet distributions. No worst-case analysis or empirical variance of Z is reported.

4. **Speculative explanation for key finding (Major):** The observation that ARIMEC achieves lower decoding error than FIMEC despite higher joint entropy (Figure 4) is attributed to a hypothesized mechanism ("ARIMEC focuses on certainty earlier in the string") without any supporting per-position analysis.

5. **Missing limitations discussion (Minor):** The conclusion does not acknowledge ARIMEC's limitations: no optimality guarantee, worst-case exponential complexity, requirement for autoregressive factorization of one marginal.

6. **Novelty verification deferred (System constraint):** External literature comparison could not be performed in this run due to retrieval unavailability. The "first general approach" claim for arbitrary distributions requires manual verification.

## Key Issues
### Issue 1 (Major): Experimental Baselines Do Not Isolate Algorithmic Advantage
**Evidence:** Page 8, Section 5.1 — The only baseline in MCG experiments is FIMEC with a deliberately misspecified uniform prior. Page 9, Section 5.2 — Unencrypted steganography comparison also uses FIMEC with uniform prior vs ARIMEC with correct prior.  
**Mechanism:** The reported gains conflate two factors: (a) the benefit of using the correct message prior, and (b) the benefit of ARIMEC's prefix tree coupling mechanism over FIMEC's component-wise coupling.  
**Risk:** Without clean ablation, readers cannot assess whether ARIMEC's algorithmic mechanism provides meaningful gains beyond correct prior usage.  
**Fix:** Add an ablation where both methods use the same (correct) prior when FIMEC can tractably use it.

### Issue 2 (Major): No Quantitative Results in Text
**Evidence:** Page 8, line 44-46: "ARIMEC produces a substantially more efficient encoding" — no numbers given.  
**Risk:** Readers cannot independently verify claims without estimating from figures. This is particularly problematic for confidence-interval comparisons.  
**Fix:** Add a results table with key metrics (error rates, joint entropies) at representative message sizes.

### Issue 3 (Major): Pruning Efficiency Not Characterized
**Evidence:** Page 7, lines 80-82: Pruning claim with "less than one to slightly more than two" partitions checked per iteration. Page 6, Proposition 4.1: Runtime expressed in terms of unbounded Z.  
**Risk:** Practical applicability of ARIMEC hinges on pruning; without variance or worst-case reporting, users cannot predict performance in new settings.  
**Fix:** Report per-iteration Z statistics (mean, median, max, variance) across experiments, and discuss regimes where pruning may be less effective.

### Issue 4 (Major): Decoding Error vs Joint Entropy Paradox Unexplained
**Evidence:** Page 9, lines 4-8: FIMEC produces lower joint entropy but ARIMEC produces lower decoding error. Explanation is speculative ("could be because").  
**Risk:** This counterintuitive result may indicate a subtle evaluation bias or metric mismatch that undermines claims about ARIMEC's practical utility.  
**Fix:** Add per-position error analysis or conditional entropy per-token analysis to validate the hypothesized mechanism.

### Issue 5 (Minor): Missing Limitations Section
**Evidence:** Page 9, Section 6: Conclusion discusses three contributions and future work but no limitations.  
**Risk:** Reduces scientific transparency; readers may overestimate ARIMEC's maturity.  
**Fix:** Add a brief limitations paragraph covering worst-case complexity, heuristic nature, and autoregressive requirement.

## Actionable Suggestions
### S1: Add Fair Baselines with Matched Priors [Must]
In Section 5.1 (MCG experiments), add a comparison where FIMEC uses the correct GPT-2 message prior while ARIMEC also uses the correct prior. If FIMEC becomes computationally intractable with the correct prior (because the message distribution is not factorable), state this explicitly and note that the comparison is inherently asymmetric. In Section 5.2 (unencrypted steganography), add an ablation: ARIMEC with incorrect (uniform) prior vs. FIMEC with incorrect prior, to isolate the algorithmic effect from the prior effect.

### S2: Report Key Numerical Results [Must]
Add a table (or amend Figure 3 caption) reporting at minimum: (a) token-wise error rates at key message sizes (e.g., 10, 50, 100 tokens) for both CodeCart and CodePong under both ARIMEC and FIMEC; (b) joint entropy values for information-theoretic steganography (Figure 4) at key ciphertext sizes; (c) confidence interval widths.

### S3: Characterize Pruning Effectiveness [Must]
Add a new figure or table showing per-iteration Z statistics (nodes checked) across the MCG and steganography experiments. Report: mean, median, standard deviation, and maximum Z across iterations. Discuss whether the pruning condition q < 1 - 1/N was ever violated and how the algorithm behaved in that case.

### S4: Analyze the Entropy-Error Paradox [Must]
Add per-position error analysis for the information-theoretic steganography experiment (Figure 4). Plot the per-token conditional entropy H(X_i | Y) and per-token decoding error for both ARIMEC and FIMEC. This will validate or refute the hypothesized mechanism that ARIMEC concentrates certainty on early tokens.

### S5: Add Limitations Paragraph [Nice-to-have]
Insert a paragraph in Section 6 (Conclusion) acknowledging: (a) ARIMEC's worst-case complexity is exponential without effective pruning; (b) no optimality or approximation guarantees on final coupling entropy; (c) requires one marginal to be autoregressively specified; (d) heuristic greedy selection of partitions may be suboptimal.

### S6: Clarify "First" Claims [Nice-to-have]
Throughout the paper (abstract, page 2 contribution paragraph, conclusion), qualify "first algorithm for arbitrary distributions" with "to our knowledge" or similar hedging, since comprehensive external verification is pending.

### S7: Fix Grammatical Error [Nice-to-have]
Page 8, line 35-36: "To illustrate the benefits of MEME's extended we perform experiments" — change to "To illustrate the benefits of MEME's extended applicability" or "To illustrate the benefits of extending MEME."

## Storyline Options + Writing Outlines
### Current Storyline Assessment
The current introduction flows as: MEC definition and applications (P1) -> NP-hardness and provable approximations (P2) -> IMEC heuristics and their limitations (P3) -> Contributions (P4). This structure is adequate but could be more engaging by foregrounding the practical problem earlier.

### Abstract Outline (Revised)
- **S1 (Problem):** A minimum-entropy coupling (MEC) is a joint distribution with minimum entropy for given marginals, but exact MEC is NP-hard and provable approximations scale with support size.
- **S2 (Gap):** Existing iterative MEC (IMEC) heuristics handle large supports but require restrictive assumptions (small support or factorable distributions).
- **S3 (Solution):** We unify existing IMEC algorithms under a partition-set formalism and derive ARIMEC, which uses a prefix tree partition set to handle arbitrary discrete distributions.
- **S4 (Techniques):** We introduce lazy posterior updates and entropy-based pruning for efficient implementation.
- **S5 (Results):** ARIMEC achieves substantially improved communication rates in Markov coding games and steganography compared to prior IMEC approaches.

### Introduction Outline (Revised — Paragraph-by-Paragraph)

**P1 — Big Picture and Problem Definition (current P1, modified):**
Open with the practical importance of coupling distributions with minimum entropy across diverse domains (causal inference, steganography, communication). Quickly introduce the MEC problem and state the scalability challenge: real-world distributions (deep generative models, natural language) have exponentially large supports.

**P2 — Existing Methods and Their Limitations (merge current P2+P3):**
State that provable MEC approximation algorithms scale as O(N log N) in support size N, which is intractable for large-support distributions. Introduce the IMEC class of heuristics (Sokota et al., 2022) that work well empirically but only under either small-support or factorization assumptions. Clearly articulate the core barrier: without factorization, the posterior over X does not decompose tractably.

**P3 — Unified Formalism (current contribution 1, expanded):**
Present the key insight: existing IMEC algorithms can be unified as instances of a generic algorithm parameterized by a set of partitions over X. Show that TIMEC uses all partitions (equivalent to the trivial partition) and FIMEC uses component-wise partitions. This framing reveals the design space for new partition sets.

**P4 — ARIMEC (current contribution 2):**
Introduce the prefix tree partition set and explain the intuition: each tree node induces a partition that separates elements by whether they extend a given prefix, are that exact prefix, or do not contain the prefix. Explain the lazy posterior update and pruning strategies at a high level before the formal definitions in Section 4.

**P5 — Empirical Validation and Contributions (current contribution 3):**
Preview the key empirical results: ARIMEC outperforms prior IMEC in both Markov coding games and steganography. State the three contributions explicitly and concisely.

## Priority Revision Plan
### P0 (Must — Before Resubmission)
| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P0 | Weak baselines (Issue 1) | Add fair ablation with matched priors; clearly separate algorithmic advantage from prior advantage | Core evaluation validity |
| P0 | Missing quantitative results (Issue 2) | Add results table with key error rates and entropy values at representative sizes | Readability, verifiability |
| P0 | Pruning characterization (Issue 3) | Report per-iteration Z statistics; discuss boundary conditions | Trust in practical efficiency |

### P1 (High Priority — Strengthen Paper)
| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P1 | Entropy-error paradox (Issue 4) | Add per-position error/entropy analysis | Scientific insight, strengthens contribution |
| P1 | "First" claim hedging (S6) | Add "to our knowledge" qualifiers throughout | Defensibility |
| P1 | Missing limitations (Issue 5) | Add limitations paragraph to conclusion | Scientific transparency |

### P2 (Nice-to-Have — Polish)
| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P2 | Grammatical error (S7) | Fix "MEME's extended" typo | Professional presentation |
| P2 | Heuristic justification footnote (Suggestion) | Clarify that max-entropy partition heuristic is plausible but not provably optimal | Theoretical rigor |

```text
ASCII Diagram — Revision Strategy Roadmap

[Weak baselines]
    -> [Add matched-prior ablation]
    -> [Show ARIMEC advantage independent of prior correctness]
    -> [Strengthened evaluation validity]

[Missing quantitative results]
    -> [Add results table with error rates + entropy values]
    -> [Readers can verify claims without estimating from figures]
    -> [Improved reproducibility]

[Unbounded Z / pruning not characterized]
    -> [Report per-iteration Z statistics]
    -> [Discuss regimes where pruning may fail]
    -> [Realistic efficiency expectations]

[Entropy-error paradox unexplained]
    -> [Per-position error analysis]
    -> [Validate or refute hypothesized mechanism]
    -> [Deeper scientific contribution]

[Missing limitations]
    -> [Add limitations paragraph to conclusion]
    -> [Improves scientific transparency]
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Limitation |
|--------|-----------|-------|---------|--------------|-----------------|------------|
| E1 (Fig 3) | MCG: CodeCart + CodePong | 2 MaxEntRL policies, GPT-2 messages, 100 games, 95% CI | Token-wise error rate | ARIMEC < FIMEC error rate; both maintain perfect return | ARIMEC improves encoding efficiency | Weak baseline (uniform-prior FIMEC); no numerical reporting |
| E2 (Fig 4) | Info-theoretic steganography | 100 GPT-2 tokens covertext, ciphertext varying size | Joint entropy (bytes), byte-wise error rate | FIMEC lower entropy but ARIMEC lower error | ARIMEC useful even when Assumption 2.4 holds | Paradox unexplained; no per-position analysis |
| E3 (Fig 5) | Unencrypted steganography | GPT-2 prompts, 100 tokens, ARIMEC (correct prior) vs FIMEC (uniform prior) | Token-wise error rate | ARIMEC dramatically outperforms FIMEC | ARIMEC achieves high throughput | Asymmetric comparison (prior + algorithm conflated) |

### Proposed Research Experiments (P0/P1)

**P0-E1: Matched-Prior MCG Ablation**
- **Target Claim:** ARIMEC's prefix tree mechanism provides gains beyond correct prior usage.
- **Hypothesis:** ARIMEC with correct GPT-2 prior outperforms FIMEC with correct prior (if tractably computable) or a variant of ARIMEC using a simpler partition set.
- **Design:** (a) If FIMEC is tractable with the true GPT-2 prior, add that comparison. (b) Add a variant of ARIMEC that uses random partitions (same number of blocks) to isolate the effect of prefix tree structure.
- **Controls:** Same temperature hyperparameters, same message distributions.
- **Success Criterion:** ARIMEC (prefix tree) achieves lower error rate than ARIMEC (random partitions) with statistical significance.
- **Expected Gain:** Clarifies whether contributions are algorithmic or prior-driven.

**P0-E2: Per-Position Error Analysis**
- **Target Claim:** ARIMEC reduces error by concentrating certainty on early tokens.
- **Hypothesis:** Per-token conditional entropy H(X_i | Y) decreases faster with position for ARIMEC than FIMEC.
- **Design:** For the information-theoretic steganography experiment, compute per-token entropy and per-token decoding error for positions 1 through m. Plot for both ARIMEC and FIMEC.
- **Success Criterion:** ARIMEC shows lower per-token entropy in early positions compared to FIMEC, with statistical significance.
- **Expected Gain:** Validates the hypothesized mechanism; strengthens the paper's scientific contribution.

**P1-E1: Pruning Efficiency Characterization**
- **Target Claim:** Proposition B.2 enables practical efficiency across diverse settings.
- **Hypothesis:** Z (nodes checked per iteration) remains small across varying sequence lengths, alphabet sizes, and posterior concentrations.
- **Design:** Run ARIMEC on synthetic data with controlled sequence length (m=2,5,10,20) and alphabet size (N=2,4,8,16). Record Z per iteration.
- **Success Criterion:** Mean Z stays below 5 for all tested configurations; worst-case Z is reported.
- **Expected Gain:** Provides users with realistic efficiency expectations; identifies failure regimes.

```text
ASCII Diagram — Experiment Upgrade Plan

P0-E1: Matched-Prior MCG Ablation           P0-E2: Per-Position Error Analysis
    [Current: ARIMEC+correct FIMEC+uniform]      [Current: aggregate error only]
    |                                              |
    v                                              v
    [Add: ARIMEC+correct vs ARIMEC+random]        [Add: per-token H(X_i|Y) plots]
    [Add: FIMEC+correct if tractable]              [Add: per-token decoding error]
    |                                              |
    v                                              v
    [Isolate algorithmic mechanism]               [Validate hypothesized explanation]

P1-E1: Pruning Efficiency Characterization
    [Synthetic: vary m (2-20), N (2-16)]
    [Record Z per iteration: mean, median, max]
    |
    v
    [Practical efficiency guidance for users]
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5/10**

The paper presents a meaningful algorithmic contribution (ARIMEC) and a clean unified formalism for IMEC algorithms. The core ideas — prefix tree partition set, lazy posterior updates, pruning bound — are technically sound and well-motivated. However, the score is tempered by:

- **Experimental evaluation (moderate weakness):** The baselines are asymmetric, key quantitative results are missing from the text, and the interesting entropy-error paradox is left as speculation.
- **Novelty verification (deferred):** The "first general approach" claim could not be externally verified in this run due to retrieval unavailability. The score assumes this claim holds pending verification.
- **Theoretical completeness (minor weakness):** The runtime guarantee depends on an unconstrained parameter Z; no worst-case analysis is provided.

**Post-Revision Target: [7.5, 8.0]/10**

Achievable if the authors:
1. Add matched-prior ablations to isolate algorithmic advantage (P0)
2. Report numerical results in text (P0)  
3. Characterize pruning effectiveness empirically (P0)
4. Analyze per-position error/entropy for the steganography paradox (P1)
5. Add limitations and hedge "first" claims (P1)

With these revisions, the paper would provide a convincing empirical story alongside its solid theoretical framework, reaching the quality expected at top-tier venues (ICLR, ICML, NeurIPS).