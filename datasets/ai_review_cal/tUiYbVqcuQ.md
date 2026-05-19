- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3
Now I have all the information needed. Let me synthesize the final review.

## Summary

The paper proposes A2FC (Advantage Actor Federated Critic), a federated multi-agent A2C algorithm that aggregates only critic models on a central server while keeping actor models local. This design is meant to handle heterogeneous action spaces (where agents have different action sets), reduce communication overhead, and preserve policy privacy. The method is evaluated on an adaptive traffic signal control (ATSC) simulation with 25 intersections against MA2C (which shares policies between neighbors) and IA2C (fully independent).

## Strengths

1. **Principled design for heterogeneous action spaces.** By aggregating only critic models (which estimate the shared reward structure) and keeping actor models local, A2FC naturally accommodates agents with different action sets (Section 3.4, Algorithm 1). This cleanly sidesteps the architectural mismatch problem that arises when FedAvg is applied to actors with heterogeneous output dimensions. The design is conceptually sound and directly addresses a real limitation of prior federated A2C work (cited at line 210).

2. **Positive empirical results in a homogeneous ATSC benchmark.** In the ATSC experiment (which assumes all 25 intersections have the same 5-phase action space), A2FC converges to a training reward comparable to MA2C (~−490 vs. ~−500) and achieves the best numerical values across all three evaluation metrics (queue length: 10.20, intersection delay: 36.70, vehicle speed: 3.65) per Table 1. Critically, A2FC shows less reward fluctuation at convergence than MA2C (Figure 3), suggesting that critic-only aggregation yields more stable training even in homogeneous settings.

3. **Communication architecture is inherently lighter.** A2FC only transmits critic parameters to a central server every 720 steps, whereas MA2C requires agents to share policy information with neighbors at every training step (Section 4.3). This architectural reduction in communication is a genuine advantage of the design, independent of any quantitative measurement.

## Weaknesses

### Major

1. **The central claim — handling heterogeneous action spaces — is not evaluated.** The paper is motivated by and titled for heterogeneous action spaces, and the method is explicitly designed to "allow agents to have distinct action options" (line 74). Yet the experiment uses a 5×5 traffic grid where "each intersection within this grid comprises five possible phases" (line 172), i.e., homogeneous action spaces. The paper never tests a scenario where agents have different numbers or types of actions, so the primary distinguishing contribution of A2FC remains unvalidated. This is not a missing ablation; it is a gap between what the paper claims as its core contribution and what it actually measures.

2. **Results lack statistical rigor.** All results (Figure 3–6, Table 1) appear to come from single training runs. No error bars, standard deviations, confidence intervals, or multi-seed statistics are reported. In reinforcement learning, where variance from random seeds, environment stochasticity, and initialization is high, single-run comparisons are insufficient to support claims of superiority. The paper's conclusion that A2FC "ultimately converges to a higher reward" than MA2C (line 188) could fall within noise.

3. **Communication overhead and privacy benefits are asserted but never quantified.** The paper claims A2FC "significantly reduces communication overhead" (Section 4.3, line 195) and "preserves agents' privacy" (Section 3.5, line 158) as two of its three stated benefits. However, no quantitative measurements are provided: no byte counts, messages per step, or bandwidth comparisons for communication; no differential privacy analysis, attack-resistance evaluation, or leakage comparison for privacy. These remain qualitative assertions.

### Minor

4. **Unsubstantiated claim that critic aggregation "doesn't result in any private information leakage."** Section 3.5 states categorically that "the aggregation of critic models doesn't result in any private information leakage from the agents." This is a strong assertion with no supporting analysis. Since the critic takes agent observations as input, its parameters could encode information about visited states; no argument or experiment is given to rule this out. A more defensible claim would be that critic aggregation leaks *less* information than actor aggregation.

5. **Questionable claim about consistent value-function gradients.** Section 3.3 states: "the gradient of the value function ΔL(ω_i) remains consistent for each agent. This consistency arises from the fact that R̂_{t,i} is sampled using the same stationary policy π_{θ_i^-} for each agent i." In a multi-agent system, agents do not share the same policy (each learns its own π_{θ_i}), and even if they nominally did, different local observations would produce different sampled returns. The claim as written is unclear at best and likely incorrect.

6. **Advantage estimation not specified in the algorithm.** Algorithm 1 (line 10) says "Estimate R̃_{τ,i}, R̂_{τ,i}" but does not specify whether a truncated n-step return, TD(λ), or Monte Carlo return is used — a detail needed for reproducibility.

### Trivial

7. **"Agents do not need to communicate with each other" is technically true but slightly misleading** — A2FC still requires communication with a central server, which is itself a form of communication, albeit reduced (Abstract, line 16).

8. **Minor notation inconsistency:** The `π_{θ_i^-}` notation used in Section 3.3 (line 96) to describe the "same stationary policy" is introduced but not defined.

## Nice-to-Haves

- An ablation comparing A2FC against a version with independent critics (no aggregation) would isolate the benefit of the federated critic.
- A sensitivity analysis on the aggregation frequency hyperparameter `E` (currently fixed at 720 steps) would strengthen the paper.
- Per-intersection performance metrics (e.g., spatial distribution of congestion) would complement the current grid-wide averages.
- A controlled comparison against FedAvg (which aggregates both actor and critic) in a homogeneous setting would clarify whether critic-only aggregation is sufficient or deficient.

## Removed Points

These points from the reviewers were identified as not suitable for the main review:

- **Missing related work on other heterogeneity approaches** (population-based training, action masking) — Per guidelines, I cannot confirm the existence or relevance of unmentioned works.
- **Speculation about model inversion attacks on the critic** — The harsh critic's speculation about hypothetical attacks goes beyond what can be verified from the paper's content; the core concern (unsubstantiated privacy claims) is already captured in Major weakness #3 and Minor weakness #4.
- **"Table 1 is an image and cannot be read"** — This is a PDF-parser artifact, not a paper flaw.
- **"No code or detailed experimental configuration"** — Network architecture details are partially given (LSTM layer, learning rates, line 174), and the reward structure is from a cited reference; full configuration disclosure is standardly deferred to appendices.
- **Harsh critic's Section-by-section notes about convergence properties, stationarity, and theoretical grounding of the "global view" claim** — These are reasonable suggestions for improvement but already covered in spirit by the Nice-to-Haves; the "global view" concern is too general to stand as a concrete weakness without a specific error to point to.
- **Strength Finder's generic strength about "addressing an important problem"** — Generic; lacks a specific anchor in the paper's content.

## Novel Insights

The most interesting observation that emerges across the reviews is a tension in the paper's framing: A2FC is motivated by heterogeneous action spaces, but its advantages are demonstrated in a homogeneous setting. This juxtaposition actually suggests an alternate narrative — that critic-only aggregation is beneficial *even when action spaces are homogeneous* because it provides more stable convergence and avoids the personalization loss that comes from averaging actor models. The paper would be stronger if it explicitly reframed its contribution around this finding (stable critic aggregation without actor averaging) and treated heterogeneous action spaces as an additional structural benefit rather than the primary focus, since the latter is untested.

## Suggestions

1. **Run experiments with heterogeneous action spaces.** This is the single most important revision. For example, assign different intersections different subsets of available traffic phases (some get 3, others get 5). Show that baselines fail (architectural mismatch in FedAvg) or degrade, while A2FC handles this naturally.

2. **Report results over multiple random seeds** (at least 5) with mean learning curves and shaded standard deviations or confidence bands.

3. **Quantify communication overhead** — e.g., total bytes transmitted per agent over the full training run for A2FC vs. MA2C.

4. **Tone down the absolute privacy claim.** Replace "doesn't result in any private information leakage" with a more measured statement about reduced policy exposure, and discuss what information the critic could potentially leak.

5. **Clarify Algorithm 1** by specifying the advantage estimation method (n-step return, TD(λ), etc.) and defining π_{θ_i^-}.

---
