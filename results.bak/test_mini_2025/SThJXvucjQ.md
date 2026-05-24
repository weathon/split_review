Now I have all the evidence I need. Let me write the consolidated review.

## Summary

This paper extends Conservative Contextual Bandits (CCBs) — where the learner must not underperform a baseline policy by more than a (1+α) factor — to general non-linear cost functions. The authors propose two algorithms, C-SquareCB and C-FastCB, that use Inverse Gap Weighting (IGW) exploration with an online regression oracle instead of the UCB-style confidence bounds used in prior linear-only work. C-SquareCB achieves sub-linear regret in horizon T, while C-FastCB achieves a first-order (data-dependent) regret bound in the optimal policy's cumulative loss L*. The framework is instantiated with neural networks and Online Gradient Descent to give end-to-end regret bounds, and the algorithms are validated on real-world datasets against the linear baseline C-LinUCB.

## Strengths

1. **First reduction of conservative bandits to online regression for non-linear functions.** Theorem 3.1 provides the first regret bound for CCBs beyond linear representations: \(O(\sqrt{KT}(\sqrt{\text{Reg}_{\text{sq}}(T)}+\sqrt{\log(1/\delta)}) + K(\text{Reg}_{\text{sq}}(T)+\log(1/\delta))/(\alpha y_l(\Delta_l+\alpha y_l)))\). The analysis is a genuine technical contribution — it relates the number of baseline fallback rounds (n_T) to squared-loss regression regret (Lemmas 3.2, 3.3), overcoming the challenge that general function classes do not admit the confidence bounds used in the linear setting (Remark 3.3).

2. **First-order (data-dependent) regret guarantee.** Theorem 4.1 (C-FastCB) gives expected regret scaling with \(\sqrt{L^*}\) instead of \(\sqrt{T}\), using an episodic γ_t schedule to avoid \(\sqrt{T}\) dependence (Remark 4.2). This is the first such bound for conservative bandits under non-linear functions.

3. **End-to-end neural network bounds.** Theorems 5.1 and 5.2 instantiate the regression oracle with OGD on a neural network, yielding explicit bounds \(\tilde{O}(\sqrt{KT}+K/\alpha)\) and \(\tilde{O}(\sqrt{KL^*}+K(1+1/\alpha))\) under standard NTK assumptions. This avoids the \(\Omega(T)\) worst-case issue of Neural UCB-based extensions (cited as Deb et al., 2024a), which the paper explicitly identifies as a motivation for the IGW-based approach.

4. **Empirical validation of regret and safety.** Figures 1 and 2 show that on six OpenML datasets, C-SquareCB and C-FastCB achieve sub-linear regret and maintain constraint violations below 2% across perturbation levels, while their vanilla (non-conservative) counterparts violate constraints up to 25% and the linear baseline C-LinUCB exhibits linear regret.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims are well-supported by the theory and the experiments are appropriate for a first work in this area.

### Minor

1. **Theorem 5.1 contains a self-reference that should be corrected.** The statement reads: "with γ_t as in Theorem 5.1" (line 287), which clearly should refer to Theorem 3.1 (or Lemma 3.4/3.5). This is a straightforward copy-editing error but affects readability.

2. **Inconsistency in the γ_t definition across Lemma 3.4 and the Theorem 3.1.** Lemma 3.4 (line 176) defines γ_t using \(\text{Reg}_{\text{sq}}(T)\), while Theorem 3.1 (line 136) and Lemma 3.5 (line 184) use \(\text{Reg}_{\text{sq}}(m_T)\). Since \(\text{Reg}_{\text{sq}}(T) \geq \text{Reg}_{\text{sq}}(m_T)\), both are valid upper bounds, but the inconsistency is confusing. The proof sketch in Lemma 3.4 should use \(\text{Reg}_{\text{sq}}(m_T)\) to be consistent with the rest of the analysis.

3. **The neural-network instantiation for the KL-loss case (Theorem 5.2) is not fully specified.** Theorem 5.2 states it instantiates "Sq-Alg" (a likely typo — should be "KL-Alg") with OGD using the update in Equation (17). However, Equation (17) explicitly uses the squared-loss objective from Equation (16). The paper does not specify the loss function or OGD update for the KL-loss case, nor does it justify that O(log T) regret for neural regression with log-loss follows from the same analysis as the squared-loss case. The cited Deb et al. (2024a) focuses on squared loss, so at minimum a reference or brief argument for the log-loss extension is needed.

4. **The regret experiments compare only against a single baseline (C-LinUCB).** While this is the only existing conservative bandit baseline in the literature and the comparison is valid (C-LinUCB is the natural benchmark from prior work), a comparison against a simple non-linear heuristic (e.g., a conservative version of SquareCB/FastCB with a naive safety rule) would help isolate the value of the paper's specific algorithmic design. The safety-violation experiments (Figure 2) already compare against vanilla SquareCB/FastCB, and a similar regret comparison would strengthen the empirical story.

### Trivial

1. **Notational typo in Algorithm 1 (line 109).** The formula for p_{t,a} uses "∀ k∈[K]\{z_t\}" where the quantifier variable should be 'a' to match the left-hand side.

2. **Minor typo in Remark 4.2 (line 239).** The remark says "as in Theorem 5.1" when discussing challenges for C-FastCB; this appears to be a cross-reference error (should refer to the C-SquareCB analysis rather than Theorem 5.1 specifically).

3. **The experimental caption text appears duplicated** (parser artifact visible in the extracted text, lines 281-285 and 307-311), though this does not affect the paper's content.

## Nice-to-Haves

- **Provide a self-contained description of the γ_t schedule for C-FastCB in the main text.** Remark 4.2 defers the episodic schedule to Appendix C. While understandable for space, including the general form of the schedule in the main paper would improve readability without needing the appendix.
- **Briefly discuss the computational cost of the safety condition.** The term \(\sum_{i \in \mathcal{S}_{t-1}} \sum_{a \in [K]} p_{i,a} \hat{y}_{i,a}\) requires only O(m_t) storage (one scalar per IGW round, not a K×m_t matrix), which is benign in practice but mentioning this would head off concerns.
- **A comparison with a non-linear heuristic baseline** (as noted in Minor weakness 4) would add empirical rigor but is not essential for the paper's acceptance.

## Removed Points

- **Claim about weak experimental baseline being "critical":** The harsh critic characterized the lack of non-linear baselines as a critical weakness. This is an overstatement. The paper is the first to address non-linear conservative bandits; there are simply no existing non-linear conservative baselines. The comparison against C-LinUCB (the only existing baseline) and against vanilla SquareCB/FastCB (for safety, Figure 2) is appropriate for a first work. I have downgraded this to a Minor weakness and a Nice-to-Have.

- **Safety condition computational cost (memory-intensive K×m_t matrices):** The harsh critic claimed the safety condition requires storing all past ŷ matrices (size K×m_t). This is incorrect: \(\sum_{a\in[K]} p_{i,a}\hat{y}_{i,a}\) is a scalar per round, requiring O(m_t) storage, not O(K m_t). The criticism misunderstands the implementation cost.

- **Assumption 2 (baseline gap bounds) limitation:** The harsh critic suggested this should be stated as a limitation. The paper already acknowledges that "this assumption is standard in conservative bandits" (line 83). This is not a weakness — it is shared with all prior work in this area.

- **Missing related works:** Removed per policy (no external sources to verify existence of unmentioned works).

- **Formatting/style nitpicks about figure captions and parser artifacts:** Removed per policy; these are extraction artifacts, not submission errors.

- **Strength Finder's generic/superficial strengths:** The Strength Finder's overall framing strengths were generic (e.g., "the problem is well-motivated"). I have kept only strengths with specific citations and concrete content that directly support the paper's claims.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the paper's contributions or weaknesses that a careful reader of the paper would not already have, beyond pointing out the specific self-reference and notational inconsistencies that are verified above.

## Suggestions

1. Fix the self-reference in Theorem 5.1 ("γ_t as in Theorem 5.1" → "γ_t as in Theorem 3.1").
2. Align the γ_t definition in Lemma 3.4 to use Reg_sq(m_T) for consistency with Theorem 3.1 and Lemma 3.5.
3. Clarify the OGD loss function for the neural KL-loss case (Theorem 5.2) or add a brief justification that the squared-loss OGD analysis extends to log-loss under the sigmoid-ensemble predictor.
4. Add a single non-linear heuristic baseline to the regret experiments (e.g., a conservative variant of SquareCB/FastCB without the formal safety guarantee) to further demonstrate the practical value of the safety condition.

## Score and Decision

**Calibration Report**

*Round 1 (Bracketing):* Retrieved anchors in three bands on the topic of conservative/safe bandits with theoretical guarantees.
- Weak band (avg < 3.5): Scores 2–3 — rejected papers with fundamental issues (e.g., "Regret measure in continuous time limit" avg 2.33, "Dynamic Assortment Selection" avg 3.0). Our paper is clearly above these.
- Middle band (3.5–7.5): Scores 5–7 — accepted/rejected papers with solid contributions but some limitations (e.g., "Second Order Bounds for Contextual Bandits with Function Approximation" avg 6.0, accepted poster; "High Probability Contextual Bandits for Optimal Dosage Selection" avg 6.0, rejected; "ActSafe" avg 6.75, accepted poster).
- Strong band (7.5+): Scores 8 — oral/spotlight papers with exceptional contributions. Our paper is not at this level.

*Round-1 bracket:* 5 to 7.5.

*Round 2 (Narrowing):* Retrieved anchors inside the (5, 7.5) bracket on safe/constrained bandits and IGW-based bandits.
- "Second Order Bounds for Contextual Bandits with Function Approximation" (avg 6.0, accepted poster) — pure theory, no experiments, some presentation issues. Our paper has experiments and is more clearly written; slightly stronger → ~6.5.
- "Almost Optimal Batch-Regret Tradeoff for Batch Linear CB" (avg 7.0, accepted poster) — matching upper/lower bounds. Our paper's theory is less tight but addresses a practically motivated problem (safety) and has experiments; slightly weaker → ~6.5.
- "Variance-aware Regret Bounds for Stochastic Contextual Dueling Bandits" (avg 6.0, accepted poster) — similar theoretical paper with synthetic experiments. Our paper has real-world experiments and a more novel setting; slightly stronger → ~6.5.
- "ActSafe" (avg 6.75, accepted poster) — safety in RL with both theory and experiments. Comparable quality → ~6.5.
- "High Probability Contextual Bandits for Optimal Dosage Selection" (avg 6.0, rejected) — had split reviews (8,5,6,5) and was rejected, partially due to concerns about technical novelty relative to prior linear bandit work. Our paper's reduction-based approach is more novel relative to existing work; stronger → ~6.5.

*Final placement:* The paper is a solid ICLR-level contribution. The theoretical analysis is novel and clean, the experiments are adequate for a theory-first paper, and the writing is clear (with minor issues). It is comparable to accepted poster papers in the 6–7 range. I place it at **6.5**, slightly above the median accepted poster anchor (6.0) and below the very strong anchors (7.0+).

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>