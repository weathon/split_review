Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper proposes HiSo, a method that integrates diagonal Hessian-informed preconditioning into the scalar-only communication framework for federated zeroth-order optimization. The key technical contributions are: (1) a generalized FL framework that decouples scalar-only communication from vanilla ZO-SGD, enabling richer update rules; (2) a specific algorithm (HiSo) that uses a running average of squared ZO gradient updates as a diagonal preconditioner, learned and shared without extra communication cost; (3) convergence theory showing that under a "well-approximated condition" the rate becomes independent of model dimension \(d\) and the Lipschitz constant \(L\), and extends to \(\tau > 1\) local updates — a setting DeComFL could not handle; and (4) empirical results across OPT-125M to OPT-2.7B on SST-2, QQP, and SQuAD, showing 1.4–5.4× speedup in communication rounds over DeComFL with 29%–80% communication savings.

## Strengths

1. **Generalized scalar-only communication framework (Algorithm 1).** The paper correctly observes that dimension-free communication via ZO does not require ZO-SGD specifically — any update expressible as scalars × pseudo-random vectors works. This decoupling is a clean architectural contribution that future FL methods can build on.

2. **Consistent and substantial empirical acceleration over the state-of-the-art ZO-FL baseline.** Table 2 reports that HiSo requires 1.4×–5.4× fewer communication rounds to reach DeComFL's best accuracy across OPT-350M, OPT-1.3B, and OPT-2.7B on three NLP tasks. The communication savings (29%–80%) are meaningful for the TB-level budgets that first-order methods require.

3. **Convergence guarantee for \(\tau > 1\) local updates.** DeComFL's theory could not handle multiple local steps under the low-effective-rank assumption. Corollary 3 derives a rate for HiSo that remains dimension-independent when \(\tau > 1\), resolving this open limitation. This is a non-trivial theoretical advance.

4. **Robustness to the Hessian smoothing hyperparameter.** Fig. 5 (left) shows that varying \(\nu\) over {0.9, 0.95, 0.99} has negligible effect on convergence speed and final accuracy, demonstrating practical robustness.

5. **Variance reduction analysis using the whitening framework.** The paper formalizes how preconditioning reduces the ZO gradient variance from \(O(Ld)\) to \(O(\zeta)\) via the whitening matrix \(H^{-1/2}\Sigma H^{-1/2}\) (Eq. 16, Table 1). The numerical illustration in Fig. 4 (where \(\zeta \approx 100 \ll L\kappa \approx 3400 \ll Ld \approx 120000\)) makes the intuition concrete.

## Weaknesses

### Major

1. **Narrative mismatch between "Hessian-informed" branding and the actual update rule.** The paper's title, abstract, and core framing present HiSo as a Hessian-aware method that "captures curvature information through diagonal Hessian approximation." However, the actual \(H\)-update (Eq. 12) is a running average of squared gradient updates — structurally identical to the second-moment estimate in RMSProp/Adam. Footnote 2 acknowledges this ("More accurately, our method resembles RMSProp"), and Footnote 1 cautions that "Hessian-informed" does not imply full Hessian computation. Nevertheless, the central analogy the paper sells is that the preconditioner \(H_r\) approximates the Hessian, yet no algebraic or empirical link is established between \(\text{Diag}(|\Delta x|^2)\) and the true Hessian diagonal. The paper calls the method "Hessian-informed ZO optimization" in the title and throughout, when "ZO adaptive gradient method with scalar-only communication" would be more accurate. This framing overreach undermines the paper's credibility and conflates two different motivations. *Evidence: the paper states at line 22 "Hessian-informed ZO federated optimization method," at line 36 "captures curvature information through diagonal Hessian approximation," while footnote 2 at line 155 says "More accurately, our method resembles RMSProp."*

2. **The 90-million-times communication savings claim is unsupported by the reported data.** The abstract and introduction (line 41) state "Compared to first-order baselines, up to 90 million times communication savings can be gained." The largest ratio between any first-order baseline and HiSo that can be derived from Table 3 is approximately 20 million (FedAdam at 0.30 TB vs. HiSo at 14.69 KB for OPT-125M SST-2: 0.30 TB / 14.69 KB ≈ 20.4M). No entry in Table 3 supports the 90M figure. This is a factual inaccuracy in a headline performance claim. *Evidence: Table 3, rows for OPT-125M and OPT-1.3B first-order methods vs. HiSo.*

### Minor

3. **No convergence curves for the main LLM experiments.** The paper's central empirical claim is that HiSo converges faster than DeComFL, yet the only convergence plot in the main paper is for the small MNIST CNN (Fig. 5). For the LLM experiments (OPT-350M through OPT-2.7B), the evidence is limited to Table 2 (rounds to match DeComFL's best accuracy) and Table 3 (final accuracy). Without learning curves, the reader cannot verify that HiSo genuinely converges faster (rather than achieving higher final accuracy, which would make the matching metric easier to satisfy) or assess training stability. *Evidence: Section 6 and Tables 2–3; the only convergence plot is Fig. 5 (MNIST CNN).*

4. **The well-approximated condition (Eq. 17) is not analyzed for the actual \(H\)-update (Eq. 12).** Corollaries 1–3 derive dimension-independent rates conditional on \(\text{Tr}(H^{-1/2}\Sigma H^{-1/2}) \le \zeta\) with \(\zeta\) independent of \(d\). The paper does not analyze whether the \(H_r\) produced by the RMSProp-style update rule (Eq. 12) satisfies this condition on realistic loss landscapes. The paper acknowledges this ("it is hard to determine if this approximation holds in the context of LLMs") and notes that in the worst case performance degenerates to DeComFL. This is a transparent treatment, but it leaves a substantial gap between the theory and the algorithm — the claimed dimension-free rate is a property of an unverified condition, not a proven property of the algorithm itself. *Evidence: Corollaries 1–3 require the well-approximated condition; the remarks at line 298 acknowledge the gap.*

5. **Stopping criterion is not defined.** Tables 2–3 report communication cost "until convergence" without specifying the stopping criterion (e.g., validation loss plateau, fixed number of rounds, early stopping threshold). This makes the communication cost numbers difficult to reproduce or compare fairly. *Evidence: Table 2 description says "total number of communication rounds required to fully converge" without defining convergence; Table 3 says "until convergence" without definition.*

### Trivial

6. The update rule (Eq. 12) for the general \(\tau > 1\) case uses \(\Delta x_{r,\tau}^{(i)}\) without clarifying whether this is the cumulative local update over the round or the last local-step update. The simplified \(\tau = 1\) presentation is clear, but the general case needs specification.

## Nice-to-Haves

- **Provide convergence curves (rounds vs. accuracy/F1) for at least one representative LLM experiment** (e.g., OPT-350M on SST-2) to visually confirm the claimed speedup and show training dynamics.
- **Ablation comparing HiSo against a version with fixed (non-learned) \(H\)** (e.g., identity, or the first-round estimate frozen) would isolate the benefit of the Hessian update mechanism.
- **Statistical significance tests** for the accuracy improvements in Table 3. Several entries show overlapping standard error bars (e.g., OPT-1.3B SST-2: HiSo 90.34±0.12 vs. DeComFL 90.22±0.10); a significance assessment would strengthen the claims.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism that the Hessian connection is "not justified" as a fatal flaw.** The paper does provide a mathematical derivation (Eqs. 5–9) showing that if \(H_r\) approximates the Hessian, the update approximates Newton's method, and it acknowledges the RMSProp resemblance. The issue is better characterized as a narrative overreach than a foundational error. — *Demoted from "fatal" to Major severity.*
- **Criticism that the theoretical acceleration is "not a property of the algorithm."** The paper transparently acknowledges the well-approximated condition is hard to verify and discusses the worst-case degeneration to DeComFL (line 298). This is standard practice in optimization theory; theoretical results conditional on unverified assumptions are common. — *Demoted from Major to Minor.*
- **Generic "insufficient empirical support" claim.** The empirical evaluation covers three model sizes (OPT-125M, 350M, 1.3B, plus 2.7B in Table 2) and three tasks. The missing convergence curves are a specific gap (retained above) but the overall evaluation is not insufficient. — *Removed as overbroad.*
- **Strength Finder claims about "rigorous variance analysis" and "first dimension-independent convergence rate."** The former is somewhat overstated (the analysis depends on the well-approximated condition), and the latter is partially preempted by DeComFL's own dimension-independent rate under the effective-rank assumption. These are retained in modified form above (Strengths 3 and 5). — *Merged into existing strengths.*
- **Strength Finder's "robustness" claim.** This is a valid strength and retained. — *Not removed.*
- **Strength Finder's generic strength about "addressing an important problem."** Removed as generic/superficial.

## Novel Insights

The most interesting observation from the reviews is the tension between two valid framings of the same algorithm. The paper presents HiSo as "Hessian-informed," but the harsh critic correctly identifies that the update rule is structurally identical to adaptive gradient methods (RMSProp). A more honest framing — "ZO adaptive gradient method with scalar-only communication" — would better align the narrative with the algorithm while preserving all technical contributions. The re-framing would also tighten the theory: rather than assuming \(H_r\) approximates the true Hessian, the analysis could be recast in terms of gradient covariance, for which the running-squared-update heuristic has a known justification (diagonal Fisher approximation). This reframing would make the paper stronger without changing a single line of code.

## Suggestions

1. **Re-frame the method:** Change the title and narrative from "Hessian-informed" to "ZO adaptive gradient method" (e.g., "ZO-RMSProp with Scalar-Only Communication for Federated Learning"). Adjust the theoretical motivation accordingly, replacing Hessian language with gradient covariance / Fisher information matrix language. The technical content and results remain unchanged.
2. **Correct the 90-million claim:** Either provide the specific baseline/task achieving 90M savings, or replace it with the actual observed maximum (~20M from Table 3).
3. **Add convergence curves** for at least one LLM experiment in the main paper.
4. **Define the stopping criterion** used for "convergence" in all experiments.
5. **Clarify the \(\tau > 1\) Hessian update:** specify whether \(\Delta x_{r,\tau}^{(i)}\) in Eq. 12 is the cumulative or per-step update.

## Calibration

**Round 1 bracketing (all queries parallel):**  
- Low band (avg < 3.5): Papers on Hessian-related FL (scores 2.50–3.40) — clearly weaker than HiSo.  
- Middle band (3.5–7.5): Papers on dimension-free ZO-FL, including DeComFL (6.25), FeedSign (5.25), and others (3.67–5.25).  
- High band (7.5+): Papers on optimization theory (7.6–8.0) — different scope; not directly comparable.  
→ Initial bracket: **between 4 and 7**.

**Round 2 narrowing:**  
- **DeComFL (omrLHFzC37, 6.25)** — The direct baseline. HiSo extends DeComFL with preconditioning and shows clear empirical gains. However, DeComFL had a clean narrative (ZO-SGD → scalar communication), while HiSo's "Hessian-informed" framing creates a tension. HiSo is slightly weaker on narrative quality but stronger on technical breadth. → HiSo is below DeComFL.  
- **FeedSign (DJRd4IQHGQ, 5.25)** — Another ZO-FL communication-efficiency paper, rejected. HiSo has better empirical support, cleaner theory, and a less problematic narrative (FeedSign's theory had a bias/flaw issue). → HiSo is clearly stronger than FeedSign.  
- **FedDA (kjn99xFUF3, 6.00)** — Adaptive FL theory paper, accepted. Comparable in theoretical contribution; HiSo is stronger on the empirical/applied side. → Roughly comparable, slight edge to FedDA on theoretical rigor.  
→ Final bracket: **between 5.25 and 6.25**.

HiSo sits between the two most relevant anchors. The narrative mismatch and inflated claim prevent it from matching DeComFL's 6.25, while the solid empirical results and generalized framework clearly place it above FeedSign's 5.25. **Final score: 5.5.**

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>