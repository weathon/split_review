Now let me write the final consolidated review.

## Summary

This paper proposes AdaBoN, a two-stage adaptive budget allocation method for Best-of-\(N\) alignment. Given a batch of prompts and a fixed per-prompt inference budget \(B\), AdaBoN first spends a fixed exploration budget \(d\) per prompt to estimate each prompt's reward distribution via Gaussian KDE, then greedily allocates the remaining budget across prompts based on estimated marginal gains from additional sampling. The method is evaluated across 12 LM-RM pairs, 3 datasets, and 50 batches per condition. Results show that AdaBoN consistently outperforms uniform allocation (BWR 0.55–0.62) and achieves a median Expected Survival Time of 150–153 against a per-prompt budget of \(B=120\), corresponding to ~25–28% compute savings.

## Strengths

- **Extensive and well-structured evaluation.** The paper tests across 12 LM–RM pairs (4 LMs × 3 RMs), on 50 distinct batches drawn from 3 datasets (AlpacaEval, HH-RLHF, PKU-SafeRLHF), with 100 runs per batch. This breadth directly supports the claim that AdaBoN "consistently outperforms the uniform allocation" — for most pairs, it beats uniform on ≥90% of batches. The evaluation goes well beyond what is typical in this line of work.

- **Quantified compute savings via Expected Survival Time.** Table 2a reports median ESTs of 150–153 for \(B=120\), meaning AdaBoN with budget 120 matches a uniform allocation with budget ~150. This is a concrete, interpretable measure of efficiency — ~25–28% compute savings — and the result is consistent across all 12 LM–RM pairs.

- **Clean, practical two-stage design with theoretical grounding.** The method requires no auxiliary training, works for any LM–RM combination, and has only one hyperparameter (the exploration budget \(d\)). Proposition 3.1 provides a theoretical justification for the greedy allocation when marginal gains are computed from the *true* distributions, and the paper honestly acknowledges the gap when using *estimated* distributions.

- **Demonstrated scalability with batch size.** Figure 3 shows average BWR increasing with \(K\) for all 12 LM–RM pairs (e.g., Qwen–Mistral improves by ~0.15 from \(K=3\) to \(K=20\)), supporting the claim that the method benefits from larger batches.

- **Honest discussion of limitations.** Section 5 candidly acknowledges the assumptions (Gaussian KDE, two-stage design, batch setting) and sketches concrete future directions.

## Weaknesses

### Minor

- **The exploration budget \(d=0.75B\) leaves only 25% of the total budget for adaptive reallocation, and the paper tests only large \(d\) values.** The main experiments use \(d=0.75B\), and the tuning sweep is restricted to \(\{0.60B, 0.70B, 0.75B, 0.80B\}\). Since the paper itself finds that reward distributions are "smooth and easy to learn" (Contribution 1), it is plausible that a substantially smaller exploration budget (e.g., \(d=0.2B\) or \(0.3B\)) would suffice for estimation, freeing more budget for adaptive allocation and potentially yielding larger gains. Without testing smaller \(d\), the observed improvements may reflect the particular (conservative) exploration-allocation trade-off chosen rather than the full potential of the approach. The paper should be clear that the gains are capped by design.

- **No empirical comparison against any adaptive baseline.** The paper identifies Damani et al. (2024) as the closest work and discusses differences in regime (small-batch/large-budget vs. large-batch/small-budget), but provides no empirical comparison. The stated reasons — no public implementation and computational cost — are understandable, but the absence of *any* alternative adaptive baseline (even a simple heuristic such as "allocate all remaining budget to the prompt with the highest observed maximum after exploration") makes it difficult to assess whether AdaBoN's simplicity comes at a performance cost relative to other adaptive strategies. The contribution is measured only against uniform allocation, which the paper itself frames as a weak non-adaptive baseline.

- **The latency claim is imprecise.** The paper claims AdaBoN "minimizes latency" because it requires only two sequential calls to the base LM (exploration, then allocation). This is true relative to fully sequential adaptive methods that allocate one sample at a time. However, the uniform baseline requires only *one* parallel call (generate \(B\) samples per prompt simultaneously). AdaBoN's two-stage design introduces a round-trip dependency and thus has strictly higher latency than uniform allocation. The framing conflates the comparison class; the claim should be explicitly qualified as "minimizes latency among adaptive allocation strategies."

- **No analysis of how estimation error propagates through the greedy allocation.** Proposition 3.1 shows that the greedy algorithm is optimal when the marginal gain vectors \(V_i\) are known exactly. The paper runs the greedy algorithm on Monte Carlo estimates \(\hat{V}_{i,j}\) derived from KDE-based distribution estimates, but provides no analysis or diagnostic of how estimation error affects the quality of the final allocation. The paper acknowledges this ("While the greedy procedure may not be optimal when run on the estimated vectors, it still serves as an efficient heuristic"), but the lack of any bound or diagnostic is a gap for a method whose core is the allocation decision.

### Trivial

- Figure 1 shows only three reward histograms for one LM–RM pair on one dataset. The paper appropriately references Appendix F for more, but the main-text justification for the Gaussian KDE choice rests on thin visual evidence.

## Nice-to-Haves

- **Test smaller exploration budgets** (e.g., \(d \in \{0.1B, 0.2B, 0.3B\}\)) to isolate whether the method's gains come from estimation quality or from the adaptive headroom. This would directly address the central question of how much budget the method actually needs to estimate distributions.
- **Add a simple adaptive baseline** such as "allocate all remaining budget to the prompt with the highest observed maximum after exploration" to help isolate the value of the full greedy procedure with estimated marginal gains.
- **Run a synthetic experiment** with known reward distributions to validate the greedy algorithm's behavior under perfect estimation, then degrade the estimate to show how KDE estimation error affects performance.

## Removed Points

These points were flagged during review but are excluded from the main assessment for the reasons given:

- **"The results would benefit from showing within-batch variance (SD over 100 runs)"** — The paper already reports median, Q1, Q3 across *50 batches*, each estimated from 100 runs. The across-batch distribution is more informative than within-batch SD for the claims made (consistency across batches). This is a reasonable design choice, not a gap.

- **"The Bernoulli example uses extreme parameters far from real reward distributions"** — The example is an illustrative toy intended to demonstrate the *concept* of adaptivity. Its purpose is pedagogical, not empirical. This is standard practice and not a weakness.

- **"The paper should cite properties of reward distributions from preference model training"** — The paper shows real histograms, which is more direct evidence than citing prior theoretical claims. No citation would add materially to the justification.

## Novel Insights

None beyond the paper's own contributions. The reviewers' observations largely recapitulate what the paper claims about its own limitations.

## Suggestions

1. Add a small-\(d\) ablation (e.g., \(d \in \{0.1B, 0.2B, 0.3B\}\)) to the exploration budget study. This would clarify whether the current \(d=0.75B\) is genuinely optimal or simply the safest choice within the range tested.
2. Implement and compare against a trivial adaptive heuristic (e.g., one-step greedy) to provide a sanity check on the value of the full KDE+greedy pipeline.
3. Qualify the latency claim explicitly: "AdaBoN minimizes latency *among methods that adaptively allocate across prompts*" or similar.
4. Add a brief diagnostic: how often does the greedy allocation on estimated \(\hat{V}\) agree with the allocation that would be chosen under perfect knowledge (e.g., on a synthetic distribution)?

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Three queries for papers similar to "adaptive Best-of-N alignment budget allocation language models" returned:
- **Weak anchors** (score <3.5): BjZP3fTlVg (3.00), aYYZBPoSHb (3.40), 28TLorTMnP (2.50), cywG53B2ZQ (2.50) — all substantially weaker than AdaBoN.
- **Middle anchors** (3.5–7.5): 6qUUgw9bAZ = Damani et al. (6.50, Accept), 77gQUdQhE7 (5.67, Accept), ksBhCsSUaE (6.25, Reject), aqok1UX7Z1 (5.50, Accept).
- **Strong anchors** (>7.5): 1oijHJBRsT (8.00), BPgK5XW1Nb (8.67), UHPnqSTBPO (8.00) — substantially stronger papers (self-alignment, preference annotation with human studies).

**Round 1 bracket:** Between 4.0 and 6.5. The paper is clearly above the weak anchors but below the strong ones, and comparable to the middle band.

**Round 2 (Narrowing):** Queries targeting 4.5–7.5 and 4.0–6.5 returned:
- Damani et al. (6.50) — most directly comparable. AdaBoN is simpler and more broadly evaluated but shows smaller gains and no adaptive baseline comparison. **AdaBoN is weaker.**
- CUABD2qIB4 (6.50, Accept), 7iuFxx9Ccx (6.00, Reject), 0vtftmYQGV (5.75, Reject) — less topically relevant.
- VNckp7JEHn = Inference Scaling Laws (5.75, Accept) — different contribution type (empirical study vs. new method). AdaBoN has a cleaner contribution but more modest gains. **Comparable.**
- JLDAWbzTUg = C2MAB-V (5.50, Reject), DfTWrTwLzD (5.00, Reject) — less topically relevant.

**Final calibration:** AdaBoN sits between the 5.5 and 6.0 anchors. It is a well-executed paper with a practical method and unusually broad evaluation, but the modest improvement magnitude (BWR 0.55–0.62, EST 150–153) and the absence of any adaptive baseline comparison make it weaker than the Damani et al. anchor at 6.5 and comparable to the mid-5 anchors. Score = **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>