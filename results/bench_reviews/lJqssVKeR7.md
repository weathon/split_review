Now I have everything I need. Let me write the final consolidated review.

## Summary

This paper proposes HiSo, a federated zeroth-order optimization method that integrates a Hessian-informed (diagonal) preconditioner into a scalar-only communication framework for LLM fine-tuning. The key idea is to enable dimension-free communication by transmitting only gradient scalars and random seeds, while using a running estimate of squared ZO updates (Eq. 12) as a diagonal Hessian approximation to precondition the random search direction. Theoretically, the paper proves a convergence rate that—under an unverified "well-approximated" condition on the Hessian approximation—can be independent of the model dimension \(d\) and Lipschitz constant \(L\). Empirically, HiSo achieves 1.4–5.4× speedups in communication rounds over DeComFL across LLM fine-tuning tasks (OPT-350M/1.3B/2.7B on SST-2, QQP, SQuAD) while maintaining KB-level total communication.

## Strengths

- **First theoretical convergence analysis for ZO-FL with multiple local updates (\(\tau > 1\)):** The paper provides a convergence bound (Theorem 1) that extends DeComFL's analysis to the multi-local-update setting, resolving an open limitation of prior work. Corollary 3 shows that with \(\tau > 1\), HiSo's rate remains independent of \(d\) and \(L\) under the well-approximated condition, while DeComFL's becomes \(d\)-dependent again. This is a genuine theoretical advance.

- **Novel whitening-rank variance analysis:** The introduction of \(\zeta = \mathrm{Tr}(H^{-1/2}\Sigma H^{-1/2})\) (the low whitening rank) provides a principled way to connect Hessian preconditioning to ZO gradient variance. This goes beyond a simple effective-rank bound and offers structural insight into why preconditioned ZO methods can escape the worst-case \(\mathcal{O}(d)\) variance scaling (Section 5.1, Table 1).

- **Consistent empirical acceleration over DeComFL:** Across all 9 model×task combinations (OPT-350M/1.3B/2.7B on SST-2, QQP, SQuAD), HiSo requires fewer communication rounds than DeComFL to reach the same accuracy, with speedup factors of 1.4–5.4× (Table 2). The experiments cover multiple LLM scales and diverse NLP tasks, making the empirical case reasonably broad.

- **Massive communication savings over first-order FL:** Table 3 shows that HiSo achieves test accuracy close to or exceeding first-order methods (FedAvg, FedAdam, etc.) while using KB-level communication instead of TB—up to ~90 million times reduction. This quantifies the practical significance of ZO-based FL when communication is the bottleneck.

## Weaknesses

### Fatal
None.

### Major

1. **Overclaimed "Hessian-informed" framing without establishing the connection between the learned \(H\) and the true Hessian \(\Sigma\).** The paper brands HiSo as "Hessian-informed" and claims it "utilizes global Hessian information to speed up convergence" (Abstract, Introduction). However, the Hessian approximation \(H\) is learned via Eq. 12, which is an exponential moving average of squared ZO updates \(\mathrm{Diag}(|\Delta x|^2)\). The paper never derives or empirically demonstrates that this quantity approximates the Hessian diagonal—the mechanism is essentially RMSProp-style adaptive scaling operating on noisy ZO updates. The derivation in §4.1 (Eq. 5–10) shows that if one had a well-approximated Hessian \(H\), the update \(z \sim \mathcal{N}(0, H^{-1})\) gives a Newton-like direction. But §4.2 provides no justification that the specific rule in Eq. 12 produces such an \(H\). The paper references Adam/RMSProp as precedent, but those methods use squared *gradients* (which relate to Fisher information under certain conditions), while HiSo uses squared ZO updates that mix gradient and noise. Calling this "Hessian-informed" misattributes the mechanism: the observed acceleration may come from adaptive per-coordinate scaling rather than curvature exploitation. Footnote 1 clarifies that the paper does not compute the full Hessian, but this does not bridge the gap between Eq. 12 and a Hessian approximation.

2. **The dimension-free convergence rate (Corollary 1) rests on an unverified assumption with no empirical validation.** Corollary 1 claims \(\mathcal{O}(\sqrt{\zeta/mR})\) independent of \(d\) and \(L\) *if* the well-approximated condition (Definition 17) holds. The paper acknowledges "it is hard to determine if this holds in the context of LLMs" (line 298) and provides no experiment that measures or bounds \(\zeta = \mathrm{Tr}(H^{-1/2}\Sigma H^{-1/2})\) for the learned \(H\) on any real model. The only illustrative evidence (Fig. 4) uses a synthetic log-normal eigenvalue distribution chosen arbitrarily, not derived from any actual neural network. Without validation—even approximate—that the learned \(H\) whitens the Hessian in practice, the theoretical acceleration claim is purely conditional. Theorem 1 itself is robust (it does not require the condition), but the headline dimension-free claim in Corollary 1 is the main advertised theoretical contribution and it is not substantiated.

3. **Missing ablations that would separate curvature effects from general adaptive scaling.** HiSo's update combines two elements: (a) a preconditioned random direction \(H^{-1/2}u\) instead of \(u\), and (b) per-coordinate scaling via the running average of squared updates for \(H\). The paper compares only to DeComFL (identity preconditioning with no adaptive scaling), which conflates both effects. Critical missing ablations include:
   - A version using the same scalar-only framework with an adaptive per-coordinate scaling that does *not* claim to be Hessian-informed, e.g., using a running average of squared gradient scalars \(g^2\) to scale the global step size (which would still be communicable within the framework).
   - A version that uses a *fixed* \(H\) (e.g., a precomputed Hessian diagonal on a small proxy dataset) rather than the learned adaptive \(H\), to isolate whether the benefit comes from the direction change vs. the per-coordinate scaling adaptation.
   
   Without these controls, the observed acceleration could be entirely due to adaptive learning rates (a well-known technique), and the paper's central attribution to Hessian information is unsupported.

### Minor

- **The generalized scalar-only communication framework (Algorithm 1) is not a meaningful contribution beyond DeComFL.** The abstract claims "[a] flexible FL framework... supports a broader class of optimization algorithms beyond vanilla ZO-SGD." In practice, Algorithm 1 states: "Find \(\Delta x_{r,k}^{(i)}\) that 1) is ascent direction; 2) can be represented by scalars + state." This is a design guideline rather than a formal framework. The core mechanism—shared random seeds plus scalar gradient counters—is exactly DeComFL's mechanism. The "generalization" amounts to noting that the update direction can be \(H^{-1/2}u\) instead of \(u\), and that \(H\) can be updated from scalars. This is a minor extension, not a general framework. The paper would be better served by positioning this more modestly.

- **Some communication costs for HiSo are higher than DeComFL in the same communication class.** Table 3 shows that on OPT-1.3B+QQP, HiSo incurs 96.67 KB total communication vs. DeComFL's 43.95 KB—roughly 2× more. The paper notes this ("only a little higher") but the higher cost undermines the claim of "lowest communication cost in almost all tasks" since the cost is driven by more rounds in some settings. This is a minor empirical caveat.

- **The number of clients (6 total, 2 sampled per round) is small.** While common in LLM fine-tuning benchmarks, this limits the generalization of the FL-specific claims (e.g., about client heterogeneity, \(\sigma_G\)). The paper would benefit from a discussion of how client scaling would affect the results.

### Trivial
None.

## Nice-to-Haves

- An empirical evaluation of the well-approximated condition using Hessian-vector products on a small model to estimate \(\zeta\) would greatly strengthen the theoretical claims.
- Including DeComFL with momentum (which the paper notes is feasible within the framework) as a baseline would help isolate whether HiSo's gains go beyond what momentum could provide.
- Convergence curves (accuracy vs. rounds) for the LLM tasks would be more informative than the summary speedup table alone.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"Generalized scalar-only communication framework" claimed as a strength** — The verified weakness shows this is not clearly distinguished from DeComFL and does not enable algorithmic flexibility beyond what HiSo uses. Per the rule that weaknesses win when they conflict with strengths, this strength is removed.

2. **Criticism about Theorem 1 being stated without proof (deferred to appendix)** — The parser strips appendix content. The proofs exist in the original submission. Removed per hard rule.

3. **Criticism about missing appendix content or references to appendix sections** — Parser artifact. Removed per hard rule.

4. **Criticism about "optimal learning rates" not being specified** — Minor hyperparameter tuning detail. Removed per hard rule about reproducibility nitpicks.

5. **Criticism that the "free variable" claim is misleading** — The paper's statement is reasonable: Δx is already computed for model reconstruction, so using it for H requires no extra communication. The critic's objection is overly pedantic.

## Novel Insights

The harsh critic's observation about the disconnect between the "Hessian-informed" branding and the actual Adam/RMSProp-like mechanism is the most incisive point across the reviews. This is not merely a terminology quibble—it cuts to the core contribution claim. The paper's actual algorithmic novelty (preconditioned ZO within a scalar-only FL framework) is genuine, but the paper consistently over-attributes the mechanism to "Hessian information" when the experimental design does not isolate curvature from generic adaptive scaling. The whitening-rank concept is a theoretically elegant way to characterize preconditioner quality, but until the paper validates that the learned \(H\) actually achieves whitening on real models, it remains a theoretical framing device rather than an explanatory mechanism. An honest reframing—acknowledging the method as "adaptive ZO-FL" with a Hessian-inspired preconditioner update, plus credible ablations—would substantially strengthen the paper.

## Suggestions

1. **Reframe the contribution:** Acknowledge that the Hessian approximation is a heuristic inspired by Adam/RMSProp, and rebrand HiSo around the more accurate contribution: "adaptive preconditioned ZO-FL with scalar-only communication." This honest framing would make the paper stronger, not weaker, because it aligns the claims with what is actually demonstrated.

2. **Add ablations separating curvature from adaptive scaling:** Within the scalar-only framework, compare against (a) a variant using squared gradient scalars \(g^2\) to update \(H\) (testing whether the mechanism is the adaptive scaling vs. the direction \(\Delta x\) squared), and (b) a variant where \(H\) is fixed to a precomputed value (testing whether the benefit is the direction change vs. the online adaptation).

3. **Empirically evaluate the well-approximated condition:** On a small model (e.g., OPT-125M or a CNN), compute approximate Hessian-vector products to estimate \(\zeta = \mathrm{Tr}(H^{-1/2}\Sigma H^{-1/2})\) for the learned \(H\) and show that it is indeed much smaller than \(d\). This would turn the speculative theoretical claim into a supported one.

4. **Include DeComFL with momentum as a baseline** to show that HiSo's gains are not merely momentum-like effects.

5. **Add convergence curves** for the LLM experiments to illustrate training dynamics, not just final round counts.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `SdUMIXCG2a` (FL with Hessian similarity) | 3.50 | Weaker: smaller-scale experiments, less novel contribution. Current paper is stronger empirically. |
| `H4okZ5imHB` (ZO+FL hybrid, split learning) | 3.20 | Similar weakness set (few clients, unverified assumptions) but current paper has cleaner theory and stronger LLM validation. Current paper is stronger. |
| `eX8qI83Z2z` (Newton-type FL, low-rank Hessian) | 3.00 | Weaker: more serious issues with reference quality, unclear assumptions. Current paper is clearly stronger in clarity and empirical work. |
| `Zk5jinDNGE` (ZO with skewed Hessian spectra) | 4.00 | Similar level: both have conditional theoretical claims and moderate-scale experiments. Current paper has broader empirical validation. |
| `0eM74HjPQA` (Newton method, convergence rates) | 5.20 | Stronger in theoretical depth and rigor, but limited to deterministic convex settings. Current paper has more applied relevance. |
| `Epu8Lm6VMK` (Gradient-normalized smoothness) | 6.50 | Stronger overall: elegant theoretical framework with clear contributions. Current paper is substantially weaker in theory and in the honesty of its framing. |

The paper sits below the accept-quality anchors (5.2–6.5) but above the clearly weak rejected papers (3.0–3.5). It is closest in quality to the 4.0-range papers that were rejected primarily due to gaps between claims and evidence. The core empirical contribution (adaptive ZO-FL speedups) is real, but the overclaimed Hessian framing and unvalidated theoretical condition prevent acceptance at the current bar.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>