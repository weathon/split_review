Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper addresses Byzantine attacks in Vertical Federated Learning (VFL) under a realistic threat model where attackers cannot tamper with transmitted values (due to TEE/MAC protections) but can manipulate their input training data. It classifies feasible data-only attacks, identifies sign-flipping as the most potent, and proposes CC-VFed — a defense that uses Grad-CAM-style client contribution scores to detect and neutralize malicious clients. Experiments on BCW and CIFAR10 show accuracy recovery under sign-flipping attacks.

## Strengths

- **Realistic threat model that tightens prior assumptions.** The paper correctly identifies that prior Byzantine attack work (Yuan et al., 2022) assumed attackers could tamper with transmitted values — a capability preventable via TEE and MAC. Section 3.1 explicitly enumerates defense measures and constrains the attacker to training-data-only manipulation. This addresses a genuine gap in the VFL security literature.

- **Systematic taxonomy of feasible data-only Byzantine attacks in VFL.** Section 3.2 classifies three attack types (random, permutation, sign-flipping) under the constrained threat model and provides qualitative reasoning — via Maclaurin expansion and activation-function analysis — for why sign-flipping is the most disruptive. The taxonomy provides structure that prior VFL-specific threat analyses lacked.

- **Defense evaluated on real-world datasets (BCW, CIFAR10), not toy data.** This directly addresses a limitation of Yuan et al. (2022), who only evaluated on simplistic synthetic data. The paper shows CC-VFed restores accuracy from attack-degraded levels, and Tables 3–4 indicate that non-attacked accuracy is largely preserved.

## Weaknesses

### Fatal
None.

### Major
- **No comparison against any existing VFL defense method.** The paper motivates its contribution by criticizing prior work — Yuan et al. (2022), Chen et al. (2024), and Lai et al. (2023) — but the experimental evaluation contains zero comparisons against any of these methods. Tables 3–5 only show "before defense → after defense" for CC-VFed itself. A defense improving over an undefended baseline is the minimum bar; without any comparison to existing defenses, the central claim that CC-VFed is a *better* or *more practical* approach is unsupported. The paper cannot claim to advance the state of the art without demonstrating that it outperforms or complements known methods on the same datasets and metrics.

- **Only the "best" results across four defense variants are reported, without specifying which variant produced them.** Section 4.1.2 describes 2 methods for per-input detection × 2 methods for per-batch aggregation = 4 defense variants. Line 194 states: "We tested all four defense methods ... and present the best experimental results here." This is a serious reporting flaw. Without knowing which variant produced which result — and without seeing all four — the reader cannot assess robustness, understand sensitivity to design choices, or reproduce the work. This constitutes post-hoc selection on the test set.

- **Activation function changed from ReLU to eLU specifically to make the defense work.** Line 112 and lines 182–184 state that eLU was used "to enhance the effectiveness of the defensive method" because with ReLU "nodes whose active state flips and output becomes zero will no longer be trained." While the paper is transparent about this choice, it means the evaluation does not reflect performance on standard VFL architectures. Whether the defense is effective on unmodified ReLU-based models remains unknown. This limits the generality of the experimental conclusions.

### Minor
- **Detection heuristic can conflate normal training error with malicious activity.** The detection logic (Section 4) flags low-contribution clients when the label is correct, and high-contribution clients when the label is incorrect. This equates "benign client contributing strongly to a wrong prediction during normal training" with "malicious client." The paper acknowledges false detection (lines 180–181) but its fallback — that replacing a falsely-flagged benign client's signal with random noise is "approximately the same as a normal random attack" — is not reassuring, as any signal loss degrades model quality. Batch-level aggregation partially mitigates this, but the heuristic's behavior during early training epochs is not analyzed.

- **Maclaurin expansion analysis is heuristic, not rigorous.** Section 3.2 truncates a multivariate Maclaurin expansion to second order and treats higher-order terms as negligible in the context of neural network loss landscapes, which are highly non-convex. The paper presents this as qualitative reasoning, which is acceptable, but the theoretical grounding is weaker than claimed.

- **No statistical significance or variance reported.** All experiments appear to be single runs. Reporting means and standard deviations over multiple random seeds is standard practice.

- **Limited scalability evaluation (2–3 clients, always exactly 1 malicious).** Real VFL deployments may involve many clients with varying malicious-to-benign ratios. The detection mechanism's behavior under different ratios is unexplored.

### Trivial
None.

## Nice-to-Haves
- Ablation of the contribution measure (Grad-CAM dot product) against simpler alternatives (gradient norm, activation norm, random assignment) would strengthen the claim that this specific choice matters.
- Testing against additional attack types beyond sign-flipping (e.g., label-flipping, backdoor triggers) would clarify the defense's scope.
- Analysis of how the detection threshold \( t=0 \) was chosen and whether results are sensitive to this choice.

## Removed Points
These points are flagged for removal; treat them with caution.

**Harsh Critic Claim 4 (threat model tension):** The critic argues that the sign-flipping attack requires clients to "compute forward passes" to anticipate the effect of input manipulation, and that this conflicts with model encryption. This misreads the paper: the model in TEE still accepts input and produces output — the client simply feeds modified input data \( -c \cdot x_{i,j} \) to the TEE, which naturally computes a different output. No model access or forward-pass computation is needed. The threat model is coherent.

**Harsh Critic Section 2.2 criticism:** The critic claims the adaptation of Ma et al.'s HFL attacks to VFL "is asserted rather than justified." The paper clearly describes the adaptation (manipulating input data rather than output values) and the reasoning is straightforward. This is an overly nitpicky criticism that does not identify a real issue.

**Strength Finder Strength 2 (principled detection logic):** The strength describes the detection logic as "principled," which conflicts with the verified weakness about the heuristic's limitations. Heuristics can be reasonable without being "principled"; the strength has been moderated accordingly in the main review.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Run a direct experimental comparison against Yuan et al. (2022) on the same VFL defense setup. If Yuan et al.'s method cannot handle non-linear models or the CIFAR10 dataset, demonstrate this explicitly and approximate it fairly. Without this, the central contribution claim is unverifiable.
2. Report all four defense variants separately, not just the best one. Show which variant dominates under which conditions.
3. Repeat experiments using standard ReLU activation to establish that the defense works on unmodified architectures, or clearly separate the eLU results as a preliminary proof-of-concept.
4. Add multiple-seed runs with standard deviations.
5. Include an explicit analysis of false-positive rates for the detection heuristic, showing how often benign clients are flagged as malicious during normal training.

## Score and Decision

**MY FINAL SCORE:** <score>4.0</score>
**MY FINAL DECISION:** <decision>Reject</decision>