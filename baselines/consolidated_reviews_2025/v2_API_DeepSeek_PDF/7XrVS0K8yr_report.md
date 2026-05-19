## Summary
# Final Review Report

## Summary

This paper proposes Secure-FLOATING, a framework that integrates Verifiable Federated Learning (VFL), addition-based Secure Multi-Party Computation (SMPC), and blockchain consensus to establish real-time trust in trajectory data shared among Connected and Autonomous Vehicles (CAVs) and other road users. The system enables nearby nodes to collaboratively validate each other's mobility data without revealing raw trajectories, storing endorsement results on a tamper-proof distributed ledger via IPFS. Evaluated on simulated NYC traffic data with up to 8,000 nodes, the framework demonstrates that VFL with SMPC can maintain trajectory prediction accuracy (MAE ~6-7 meters) while reducing per-node training time compared to centralized training.

**Core Contributions (C1-C3):**  
- **C1:** A VFL algorithm with zero-knowledge-proof-based integrity verification of model updates.  
- **C2:** A lightweight addition-based SMPC protocol for secure model aggregation with formal differential privacy guarantees.  
- **C3:** A scalable blockchain-based consensus mechanism for trajectory validation with claimed linear in node count.

**Overall Assessment:** The paper addresses an important practical problem — real-time trust in CAV trajectory data — and combines several existing technologies (FL, SMPC, blockchain) into an integrated architecture. However, the manuscript has several significant weaknesses that must be addressed before publication: (1) a critical mathematical inconsistency in the central scalability proof (Theorem 4.2), (2) experiment design that conflates distributed-training speedup with SMPC-specific benefits, (3) overclaimed novelty language including unverifiable "first" claims, (4) missing specification of key SMPC protocol parameters (threshold k, gradient clipping for DP), and (5) grammar/writing issues throughout. Novelty verification is deferred due to external retrieval being unavailable in this run. The paper has potential but requires substantial revision.

## Strengths
1. **Practical problem with high stakes.** The paper addresses a timely and important problem: real-time verification of trajectory data in CAV networks where malicious data could cause collisions. This is a genuinely safety-critical application with clear practical motivation.

2. **Comprehensive system integration.** Secure-FLOATING combines three complementary technologies (VFL for privacy-preserving collaborative learning, SMPC for secure aggregation, and blockchain/IPFS for tamper-proof endorsement storage) into a single architecture. This integration is non-trivial and addresses a realistic multi-dimensional requirement set (privacy, integrity, scalability, attack resilience).

3. **Realistic-scale evaluation.** The evaluation uses simulated trajectories based on real NYC traffic data with up to 8,000 heterogeneous nodes (cars, trucks, buses, e-bikes), using SUMO for traffic simulation and NS3 for wireless networking. This scale is substantially larger than typical FL-for-CAV evaluations and demonstrates feasibility at city-scale density.

4. **Multiple lightweight model comparisons.** The paper evaluates four trajectory prediction models (LSTM, RNN, GRU, Informer transformer, ODA) and provides FLOPs, CPU utilization, and parameter counts, enabling practical deployment decisions for resource-constrained CAVs.

5. **Robustness analysis under attacker ratio.** Figure 1b reports successful endorsement rate under varying attacker penetration (up to 50%) and communication ranges (50-300m), showing ~75% successful endorsement at 50% attacker ratio. This provides initial robustness evidence is valuable for safety-critical applications.

6. **Differential privacy proof attempt.** The paper includes a formal DP proof (Theorem 4.1, Appendix A.1) attempting to provide privacy guarantees for the SMPC aggregation protocol, which is appropriate for the claimed privacy-preserving objectives.

## Weaknesses
1. **Critical mathematical error in Theorem 4.2 (scalability proof).** The theorem statement defines $f(n) = 2n-1$ but the induction proof uses $f(n) = 3n-2$, and the proof function does not match the stated function. Furthermore, it is ambiguous whether $f(n)$ represents per-node or total-network overhead. If per-node, total network overhead is $O(n^2)$, not $O(n)$. This error undermines the central scalability claim. [Page 6 - Theorem 4.2]

2. **Experiment design conflates distributed speedup with SMPC benefit.** Table 3 compares VFL (with SMPC) vs. centralized training, but the dramatic training time reduction at scale (e.g., 17.01s VFL-LSTM vs. 699.87s LSTM at n=100) is primarily due to data distribution across nodes, not the SMPC protocol. No FedAvg-without-SMPC baseline is provided to isolate SMPC overhead. [Page 8 - Table 3]

3. **Unverifiable novelty claims.** The introduction states "we are the first ones to set the basis for reducing message exchange rounds" and Related Work states "There exist no paper in the literature to address real-time CAVs data validation." These absolute claims cannot be verified without exhaustive literature search. The "first" claim is especially risky given the extensive prior work on FL+SMPC and CAV trust. [Page 2 - Introduction, Page 3 - Related Work]

4. **Missing SMPC protocol specifications.** The method section describes additive secret sharing but does not specify the threshold $k$ (how many shares are needed for reconstruction), whether $k=n$ is required, or how the protocol handles node dropouts. The reconstruction formula $\theta_{\text{global}} = \sum_{v_j} \theta_{v_j}$ holds only if all $n$ nodes participate and all shares are correctly distributed. [Page 4 - VFL section]

5. **DP proof incomplete.** The privacy proof (Appendix A.1) lacks gradient clipping assumption (sensitivity is bounded only if updates are clipped), uses an undefined variable $\Delta x$, and has circular composition reasoning at the end. The proof uses $\ell_2$ sensitivity with $\ell_1$ Laplace mechanism but does not discuss the $\sqrt{d}$ factor degradation for high-dimensional models. [Page 13 - Appendix A.1]

6. **Simulation-only evaluation scope not explicitly bounded.** All results are from SUMO + NS3 simulations; real V2X communication involves packet loss, fading, hardware constraints, and unpredictable interference not modeled. The paper does not prominently state this as a limitation. [Page 9 - Limitations]

7. **Grammar and writing quality.** Multiple subject-verb agreement errors ("such approaches focuses," "our theoretical analysis show," "This indicate"), inconsistent capitalization, and vague qualitative language ("robust," "reliable," "trustworthy" without operational definitions) reduce manuscript quality. [Pages 1-2 - Introduction]

8. **Limitations section lacks specificity.** While present, the limitations are generic (heterogeneous data, intermittent connectivity) and miss concrete issues that the paper's own evidence reveals: single geography (Brooklyn only), 51% consensus vulnerability, and model-dimension-dependent SMPC overhead. [Page 9-10 - Limitations and Future Work]

## Key Issues
### Ranked Error Board (Top-5 by Severity × Impact)

| Rank | Issue | Location | Severity | Risk | Confidence | Fixable? |
|------|-------|----------|----------|------|------------|----------|
| 1 | Theorem 4.2: f(n)=2n-1 vs proof uses 3n-2, plus per-node vs total ambiguity | Page 6 - Theorem 4.2 | **Critical** | Invalidates claimed linear scalability proof | High | Yes |
| 2 | Training time comparison conflates distributed speedup with SMPC benefit; no FedAvg-only baseline | Page 8 - Table 3/analysis | **Major** | Overclaims SMPC benefit, misleads about core contribution | High | Yes |
| 3 | DP proof missing gradient clipping, undefined Δx, circular composition | Page 13 - Appendix A.1 | **Major** | Privacy guarantee unsubstantiated | High | Yes |
| 4 | SMPC parameters unspecified (threshold $k$, dropout handling, share dimension) | Page 4 - VFL section | **Major** | Protocol not reproducible | High | Yes |
| 5 | Unverifiable "first" and "no paper" novelty claims | Pages 2-3 - Intro/Related Work | **Major** | Risk of rejection during review if counterexamples exist | Medium | Yes (remove/qualify) |

### Root-Cause Analysis

The common pattern across these issues is that the paper makes strong claims (provable linearity, first-of-its-kind, formal DP guarantees) but the technical substantiation for these claims is incomplete or incorrect. The Theorem 4. The Theorem 4.2 error appears to be a copy-paste artifact from a different problem (the induction template belongs to $f(n)=3n-2$ while the stated problem yields $f(n)=2n-1$). The experiment design issue reflects a misunderstanding of what constitutes a controlled baseline for isolating SMPC overhead. The DP proof issue stems from incomplete familiarity with standard DP-SGD assumptions (clipping). These are fixable but require careful revision.

## Actionable Suggestions
### S1 — Fix Theorem 4.2 (Critical, Must)
**Problem:** The theorem states $f(n)=2n-1$ but the induction proof uses $f(n)=3n-2$.  
**Action:** 
- Clarify whether $f(n)$ is per-node or total-network overhead. If per-node: $f(n) = 2n-1$, and the induction should prove $f(k+1) = f(k) + 2$ (not $+3$). The correct base case: $f(1) = 2(1)-1 = 1$. Inductive step: $f(k+1) = 2(k+1)-1 = 2k+1 = (2k-1) + 2 = f(k) + 2$.
- If total-network: $f(n) = n(2n-1) = 2n^2 - n$, which is $O(n^2)$, not $O(n)$. Acknowledge this correctly.
- **Mentor Revision:** "Theorem 4.2 (Per-Node Communication Overhead). Each node sends $(n-1)$ trajectory messages, $(n-1)$ secret shares, and 1 ledger update. Hence per-node overhead is $f(n) = 2n-1 = O(n)$. The total network overhead is $n \times f(n) = 2n^2 - n = O(n^2)$, which is acceptable for permissioned blockchain with thousands of nodes."

### S2 — Add FedAvg-without-SMPC baseline (Major, Must)
**Problem:** Table 3 compares VFL+SMPC vs. centralized training, but the speedup is mainly from distributed computation.  
**Action:** Add standard FedAvg (without SMPC) as a baseline at the same node counts. Report both training time and model accuracy. Calculate SMPC overhead as: $\text{Overhead}_{\text{SMPC}} = (T_{\text{VFL}} - T_{\text{FedAvg}}) / T_{\text{FedAvg}} \times 100\%$.

### S3 — Fix DP proof gaps (Major, Must)
**Problem:** Missing gradient clipping, undefined $\Delta x$, circular composition.  
**Action:**
- Add: "Each node clips its model update to have $\ell_2$ norm at most $C$, so $\Delta\theta_{\text{global}} = C$."
- Fix: Replace $\lambda = \Delta x / \epsilon$ with $\lambda = \sqrt{d} C / \epsilon$ (clarifying the $\ell_1$–$\ell_2$ conversion).
- Composition: Specify per-round $(\epsilon_0, \delta_0)$ and compute total $(\epsilon', \delta')$ explicitly for $T$ rounds.

### S4 — Specify SMPC protocol parameters (Major, Must)
**Action:** 
- State the sharing threshold $k$: is it $k=n$ (all nodes required) or $k$-out-of-$n$ threshold secret sharing?
- Explain how the protocol handles dropped nodes (one node failing prevents global model reconstruction).
- Define the share generation process for vector parameters: "Each element $\theta_{v_i}^{(r)}$ is split into $n$ additive shares over a finite field $\mathbb{F}_p$."

### S5 — Remove or qualify absolute novelty claims (Major, Must)
**Action:** 
- Replace "we are the first ones" with "to the best of our knowledge, this is the first integrated framework combining addition-based SMPC, VFL, and blockchain for real-time CAV trajectory validation."
- Replace "There exist no paper in the literature" with "We are not aware of prior work jointly addressing real-time trajectory validation, malicious adversary models, and scalable SMPC for CAV networks."
- Add a literature comparison table after revision.

### S6 — Bound abstract and conclusion claims (Major, Must)
**Action:** In the abstract and conclusion, replace unqualified "robust," "efficient," "significant step" statements with evidence-grounded claims:
- Instead of "achieves lower delays and overhead," say "reduces per-node training time compared to centralized training while maintaining MAE of 6-7 meters."
- Instead of "significant step towards trustworthy autonomous transportation," say "demonstrates feasibility of privacy-preserving trajectory validation for simulated CAV networks with up to 8,000 nodes."

### S7 — Fix grammar and writing (Minor, Nice-to-have)
**Action:** Proofread for subject-verb agreement ("approaches focuses" $\rightarrow$ "approaches focus"; "analysis show" $\rightarrow$ "analysis shows"; "This indicate" $\rightarrow$ "This indicates"). Fix lowercase start after period ("and finally").

### S8 — Expand limitations section (Minor, Nice-to-have)
**Action:** Add: (a) simulation-only scope with no real V2X hardware, (b) single geographic area (Brooklyn), (c) 51% consensus vulnerability, (d) model-dimension-dependent SMPC overhead ($O(d \times n)$ per node).

## Storyline Options + Writing Outlines
### Current Storyline Analysis

The current introduction follows this structure:
- P1: CAV vision + problem scenario (mixed motivation and stakes)
- P2: Centralized trust model limitations + privacy-utility tradeoff
- P3: Secure-FLOATING description + four design aspects
- P4: VFL/consensus overview + theory claims
- P5: Paper organization

**Problems with current storyline:**
1. P1 blends scenario, problem, and motivation into one paragraph, making the research gap hard to identify quickly.
2. The contribution summary (paragraph 3) is too long and lists design aspects without a unifying narrative.
3. The privacy-utility tradeoff critique (P2) is asserted without citation or quantification.
4. The technical details (VFL, ZKP, SMPC, blockchain) are introduced before the reader understands what fundamental challenge the paper solves.

### Alternative Storyline Candidate (Recommended)

**Abstract Outline (5 sentences):**
- S1 (Problem): "Connected and Autonomous Vehicles (CAVs) and micro-mobility devices require real-time trust in shared trajectory data to navigate safely, but malicious data injection can cause collisions, especially endangering vulnerable road users."
- S2 (Gap): "Existing trust models either rely on centralized authorities (creating single points of failure and privacy risks) or use encryption that is computationally too expensive for real-time V2X latency budgets."
- S3 (Proposed method): "Secure-FLOATING is a decentralized framework that combines Verifiable Federated Learning with addition-based Secure Multi-Party Computation and blockchain consensus, enabling nearby nodes to validate each other's trajectories without revealing raw data."
- S4 (Key result): "Evaluated on simulated NYC trajectories with up to 8,000 heterogeneous nodes, the framework maintains trajectory prediction MAE of 6-7 meters while scaling per-node communication linearly with network size."
- S5 (Claim scope): "These results demonstrate the feasibility of privacy-preserving real-time trajectory validation at city-scale density, though real-world V2X deployment requires further validation under packet loss and hardware constraints."

**Introduction Outline (Paragraph-by-Paragraph):**

**P1 — Motivation and stakes (was current P1 but tightened):**
- Role: Establish the safety-critical need for trajectory trust in CAV networks.
- Claim: A single malicious node injecting false trajectories can cause collisions.
- Transition: Lead into why current solutions are inadequate.
- *Mentor text:* "Connected and Autonomous Vehicles coordinate navigation by sharing intended trajectories with nearby road users. A malicious node that injects false trajectory data can cause other vehicles to misjudge speed, distance, or intent, potentially leading to collisions that disproportionately harm vulnerable road users such as pedestrians and cyclists. Real-time verification of trajectory authenticity is therefore a safety-critical requirement."

**P2 — Gap and prior work limitations (was current P2 but with citations):**
- Role: Show why centralized models, encryption-only approaches, and existing FL/SMPC solutions fail.
- Claim: Prior work addresses privacy OR trust, but not both under real-time constraints with malicious adversaries.
- *Mentor text:* "Centralized trust models aggregate trajectory data at a single server, creating privacy risks and a single point of failure. Cryptographic approaches (homomorphic encryption, differential privacy) protect privacy but introduce latency exceeding typical V2X budgets of 100ms. Federated learning preserves data locality but existing protocols assume honest-but-curious adversaries rather than malicious nodes that inject false trajectories. Secure Multi-Party Computation can enable privacy-preserving aggregation, but conventional SMPC protocols incur prohibitive communication overhead for real-time vehicular networks."

**P3 — Solution overview and key idea (was current P3 but condensed):**
- Role: State the core idea and the three design principles.
- *Mentor text:* "We present Secure-FLOATING, a framework that integrates three components specifically for real-time CAV trajectory validation: (i) Verifiable Federated Learning for collaborative trust model training without sharing raw data, where zero-knowledge proofs verify update integrity; (ii) addition-based SMPC for secure model aggregation, whose linear complexity avoids the multiplicative overhead of conventional SMPC; and (iii) permissioned blockchain/IPFS consensus for tamper-proof endorsement recording. The key insight is that additive secret sharing, combined with lightweight trajectory predictors, reduces communication and computation overhead to meet real-time constraints without compromising privacy or security."

**P4 — Contributions (was end of P3):**
- Role: Three explicit, bounded contribution statements.
- *Mentor text:* "Our contributions are: (1) a VFL protocol with ZKP-based update verification tailored to CAV trust model building, (2) an addition-based SMPC aggregation protocol with formal DP guarantees, and (3) experimental validation on simulated NYC data with 8,000 nodes demonstrating linear per-node communication scaling."

**P5 — Organization (keep brief).**

### Alternative Storyline 2: Application-First

Lead with a concrete attack scenario: a malicious e-scooter sharing a fake trajectory at an intersection → CAV misjudges → near-collision. Use this to motivate the need for real-time validation. Then explain why existing solutions fail, then present Secure-FLOATING. This is more engaging for a general audience but requires space for the scenario.

### Recommended Choice: Storyline Candidate 1

Candidate 1 is preferred because it maintains scientific conciseness while clearly separating motivation → gap → solution → evidence → contributions. It fits within the page limit and addresses the three core questions (prior insufficiency, paper-specific problem, method advantage) more effectively than the current version.

## Priority Revision Plan
### P0 — Publication-Critical (Must fix before acceptance)

| # | Task | Issue Addressed | Effort | Expected Impact
--- | --- | --- | ---
Fix Theorem 4.2: resolve 2n-1 vs 3n-2 inconsistency, clarify per-node vs total overhead | Critical error | Low (1-2 hours) | Restores scalability claim credibility
Add FedAvg-without-SMPC baseline + recompute SMPC overhead | Major error | Medium (1-2 days experiments) | Enables fair SMPC contribution evaluation
Add gradient clipping to DP proof; fix undefined Δx; clarify composition | Major error | Low (<1 day) | Makes privacy guarantee valid
Specify SMPC threshold k, dropout handling, share generation for vectors | Major error | Low (text revision) | Makes protocol reproducible
Remove or qualify "first" and "no paper" claims | Major error | Low (text revision) | Reduces rejection risk

### P1 — High Priority (Strongly recommended)

 Task | Issue Addressed | Effort | Expected Impact
--- | --- | --- | ---
Bound abstract/conclusion claims to evidence | Overclaiming | Low | Improves credibility
Add real-world V2X limitations | Missing limitations | Low | Demonstrates scope awareness
Restructure Related Work around axes | Weak organization | Medium | Strengthens positioning
Restructure Introduction per recommended storyline | Narrative clarity | Medium | Improves engagement

### P2 — Nice-to-Have

 Task | Issue Addressed | Effort | Expected Impact
--- | --- | --- | ---
Fix grammar (subject-verb agreement) | Writing quality | Low | Professional polish
Add simulation-scope disclosure upfront | Transparency | Low | Manages expectations
Compare SMPC vs multiplication-based alternatives | Context | Medium | Strengthens lightweight claim

### Revision Sequencing

```text
Stage 1 (P0 items — 1-2 weeks):
  Fix Theorem 4.2 → Fix DP proof → Specify SMPC params → Qualify claims
Stage 2 (P0 experiment + P1 items — 2-4 weeks):
  Run FedAvg baseline → Rewrite Abstract/Conclusion → Restructure Related Work
Stage 3 (P2 items — 1 week):
  Grammar proofread → Add limitation details → Optional SMPC comparison
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|--------------------------------------|---------|--------------|-----------------|-------------------|
| E1 | Trajectory prediction accuracy of different models | NYC SUMO trajectories; LSTM/RNN/GRU/Transformer/ODA | MAE, Accuracy | All models achieve MAE 0.7-7.2; Transformer lowest MAE (0.7) | Lightweight models comparable to complex ones | Transformer MAE 0.7 vs LSTM 6.3 — large gap; "comparable" is overstated |
| E2 | Computational efficiency (FLOPs/CPU) | Same models as E1 | FLOPs, CPU utilization, Params | Lightweight models (RNN: 10.78 FLOPs) much lower than Informer (59.12) | Lightweight models are efficient | CPU% only measured; no GPU/memory/latency |
| E3 | Training time: VFL vs centralized at varying node counts | 1-100 nodes; VFL variants vs vanilla ML | Training time (s) | VFL training time near-constant (~12-17s) while vanilla grows to ~700s | VFL+SMPC reduces training time | Missing FedAvg baseline; conflates distributed speedup with SMPC |
| E4 | MAE: VFL vs centralized at varying node counts | Same as E3 | MAE | VFL MAE stable (~6.4-6.7); vanilla MAE degrades at high node counts | VFL maintains accuracy at scale | Expected from FL; not SMPC-specific |
| E5 | Communication overhead vs message size/frequency | 1kb/100kb messages at 1s/10s/1min intervals | Bytes/overhead | Small messages negligible; 100kb+1s worst | Less frequent exchanges reduce overhead | No comparison with baselines |
| E6 | Robustness under attacker ratio | Attacker ratio 0-50%; range 50-300m | Successful endorsement rate | ~75% endorsement at 50% attackers | Robustness against malicious data | No comparison to non-SMPC defense; no false positive rate |

### Research-Theme Gap Diagnosis

1. **New knowledge gap:** The paper's primary claimed novelty is the integration of VFL+SMPC+blockchain for real-time CAV trust. However, each component individually is well-studied. The novel contribution is the specific integration and the addition-based SMPC for low latency. The experiments do not isolate what new knowledge this integration generates beyond what individual components already provide.

2. **Reproducibility gap:** Key SMPC parameters (threshold k, share generation for vectors, dropout handling) are unspecified. The DP proof lacks gradient clipping. Without these, the protocol cannot be independently reproduced.

3. **Impact on practice gap:** All results are simulation-based (SUMO+NS3). Without real hardware-in-the-loop testing or real V2X trace data, the claimed "real-time" feasibility for actual CAV deployment is unsubstantiated.

### Proposed Research Experiments (P0/P1/P2)

#### P0 Experiments (Critical, Must for acceptance)

**P0-E1: FedAvg Baseline Comparison**
- Target Claim: SMPC-based VFL reduces training time
- Hypothesis: A significant portion of the training time reduction is from distributed computation, not SMPC
- Design: Run standard FedAvg (without SMPC) on the same NYC trajectory data at n={1,5,10,30,50,100}
- Controls: Same model architectures (LSTM, RNN, GRU), same data splits, same compute hardware
- Metrics: Training time, model accuracy, convergence rounds
- Success Criterion: SMPC overhead = (T_VFL - T_FedAvg)/T_FedAvg < 20%
- Estimated Cost: 1-2 days (reuse existing code infrastructure)
- Expected Gain: Enables fair attribution of SMPC-specific overhead

**P0-E2: SMPC Protocol Parameter Sensitivity**
- Target Claim: Addition-based SMPC is lightweight
- Hypothesis: SMPC communication cost scales with number of nodes n and model dimension d
- Design: Vary n={10,50,100} and d={100,1000,10000} parameters, measure per-node communication and computation time
- Controls: Same network setup, same message frequency
- Metrics: Per-node overhead (bytes, seconds), total network overhead
- Success Criterion: Linear in n for fixed d, linear in d for fixed n
- Estimated Cost: 1-2 days
- Expected Gain: Validates or refines the complexity claim in Theorem 4.2

**P0-E3: DP Privacy Accounting with Clipping**
- Target Claim: (ε,δ)-DP guarantee for aggregation
- Hypothesis: With gradient clipping at norm C, the protocol achieves (ε,δ)-DP for ε chosen per-round
- Design: Implement gradient clipping with norm C, estimate privacy budget using Renyi DP accounting for T rounds
- Controls: Compare with and without clipping; report spent ε at T rounds
- Metrics: ε spent, δ, accuracy tradeoff for different C values
- Success Criterion: Accuracy loss ≤5% for ε ≤1 after T rounds
- Estimated Cost: 2-3 days
- Expected Gain: Makes DP guarantee valid and quantitative

#### P1 Experiments (High Priority)

**P1-E1: Realistic V2X Channel Simulation**
- Target Claim: Real-time feasibility
- Hypothesis: Packet loss and interference degrade endorsement rate
- Design: Add NS3 error models (packet loss rate 1-10%, fading) to current simulation
- Controls: Compare with ideal channel results
- Metrics: Endorsement success rate, latency per endorsement round
- Success Criterion: <20% relative degradation at 5% packet loss
- Estimated Cost: 3-5 days
- Expected Gain: Bridges simulation-to-reality gap

**P1-E2: False Positive and False Negative Analysis**
- Target Claim: Robustness against attackers
- Hypothesis: The 51% threshold and ω threshold jointly determine false positive/negative rates
- Design: Sweep ω and majority threshold (40-60%), measure TPR and FPR across attacker ratios
- Controls: Ground truth labels from simulation (known malicious nodes)
- Metrics: TPR, FPR, endorsement consistency
- Success Criterion: AUC > 0.85 across ω settings
- Estimated Cost: 2-3 days
- Expected Gain: Quantifies trust model reliability

#### P2 Experiments (Nice-to-Have)

**P2-E1: OOD Generalization** — Evaluate on trajectories from different city (e.g., SUMO-based LA traffic) to test geographic generalization.
**P2-E2: Multi-modal Sensor Integration** — Simulate LiDAR/camera-based trajectory prediction alongside GPS to validate multi-modal claim.
**P2-E3: Incentive Mechanism Simulation** — Implement the Q-learning-based incentive mechanism (mentioned in Future Work) and compare endorsement participation rates vs. no incentives.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5 / 10**

**Rationale:** The paper addresses an important real-world problem with a reasonable system integration, and the evaluation scale (8,000 nodes) is commendable. However, the score is constrained by the following critical weaknesses:

- **Research Value (weight: high):** The problem is relevant but the incremental contribution over existing FL+SMPC+blockchain work is unclear. The core claimed novelty (integration for real-time CAV trust) is plausible but unverified against literature (Retrieval-Disabled Mode). **Score: 5/10**
- **Validity/Soundness (weight: high):** A critical mathematical error in Theorem 4.2 undermines the central scalability proof. The experiment design conflates distributed speedup with SMPC benefit. The DP proof is incomplete (missing gradient clipping, undefined variables). **Score: 4/10**
- **Novelty (weight: high):** The component technologies are well-studied; the specific integration may have value but is not clearly differentiated from prior work in terms of technical depth. The "first" claims are unverifiable and should be removed. **Score: 5/10** (deferred manual verification needed)
- **Reproducibility (weight: medium):** SMPC threshold k, dropout handling, loss function, gradient clipping are unspecified. Cannot be reproduced from current description. **Score: 4/10**
- **Presentation (weight: medium):** Grammar errors, listing-style related work, and verbose writing reduce clarity. The storyline is functional but can be improved. **Score: 6/10**

**Post-Revision Target: [6.5, 7.5] / 10**

If the authors address all P0 items (fix Theorem 4.2, add FedAvg baseline, fix DP proof, specify SMPC params, qualify novelty claims) claims) and selected P1 items (bound claims, restructure Related Work/Introduction), the paper could reach 6.5-7.5/10. The upper bound assumes that the novel integration claim holds up after a thorough literature check (manual verification deferred) and that the additional baselines confirm acceptable SMPC overhead. The remaining gap to 8+ would require real-world validation (hardware-in-the-loop or real V2X trace data) and a novel technical insight beyond the integration of existing components.