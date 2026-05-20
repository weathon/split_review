Now I have a clear picture. Let me write the consolidated review.

## Summary

The paper proposes Secure-FLOATING, a framework that combines verifiable federated learning (VFL), lightweight addition-based secure multi-party computation (SMPC), and blockchain (IPFS) storage to enable real-time, privacy-preserving trust validation of trajectory data among CAVs and other road users. The framework lets nearby nodes predict and endorse each other's future trajectories using local models, aggregate updates via SMPC-based secret sharing, and record endorsements on a distributed ledger. The paper provides a theoretical scalability analysis and evaluates the system on realistic NYC trajectory data with up to 8,000 nodes.

## Strengths

- **Large-scale realistic evaluation data**: The trajectory data is derived from the NYC Connected Vehicle Pilot Program (~8,000 real vehicles), with mobility simulation via SUMO and wireless simulation via NS3. This is a concrete step beyond synthetic toy data and shows genuine effort toward realistic evaluation.

- **Attacker resilience demonstrated across communication ranges**: Figure 1b evaluates the endorsement success rate at attacker ratios from 0.1 to 0.5 across four communication ranges (50–300m). The system maintains ~75% trusted-group endorsement even at 50% attacker penetration with 300m range, which is a non-trivial robustness result, even accounting for how "trusted groups" are defined.

- **Multi-model comparison on several axes**: Tables 1–2 compare six models (RNN, LSTM, GRU, Transformer/Informer, ODA) on MAE, accuracy, parameters, FLOPs, and CPU utilization. GRU achieves 95.37% accuracy with only 251.65K parameters and 32.54 FLOPs, providing a concrete basis for the claim that lightweight models suffice for trajectory prediction in resource-constrained settings.

- **Clear six-step endorsement workflow**: Section 3.3 defines the endorsement process with specific criteria (51% majority, threshold ω, time-window Δt), making the framework's operational logic reproducible and testable.

## Weaknesses

### Fatal
None.

### Major

- **The theoretical scalability proof is internally inconsistent.** Theorem 4.2 states the communication overhead as `f(n) = 2n - 1`, but the inductive proof that follows uses `f(k) = 3k - 2` as the inductive hypothesis and proves `f(k+1) = 3(k+1) - 2`. The theorem and its proof are proving different formulas. While the core O(n) claim is unaffected (both `2n-1` and `3n-2` are linear), the paper presents this as a formal proof and the inconsistency means the reasoning as written does not support the stated result. This undermines one of the paper's two principal theoretical claims (scalability). The proof must be corrected to match the theorem statement.

- **Zero-knowledge proofs are claimed but never described, implemented, or evaluated.** The introduction states that Secure-FLOATING "leverages zero knowledge proof as 'trust-but-verify' mechanism," and the conclusion claims the system includes "a tailored VFL algorithm that preserves privacy while ensuring the integrity of model updates through zero-knowledge proofs." However, the entire method section (Section 3) describes only SMPC-based secret sharing for model updates — there is no description, protocol, or implementation of ZKP anywhere. This is not a minor oversight; it means a feature advertised as part of the framework's contribution simply does not appear in the technical description.

- **The "blockchain" is IPFS, a distributed file system, not a consensus-based ledger.** The paper calls its mechanism "blockchain based consensus" but Section 3.1 clarifies that the system uses IPFS for storage, and the consensus is achieved through peer-level comparison of predicted vs. shared trajectories (Section 3.3, Steps 1–6). IPFS is a distributed hash table / file system; it does not provide blockchain consensus. The description conflates decentralized storage with blockchain consensus, which misrepresents what the system actually does.

- **No comparison to any existing trust model from the literature.** Despite citing several prior works on decentralized trust, blockchain-based trust, and SMPC for CAVs (Sections 2), the experimental evaluation (Section 5) compares only VFL models against vanilla versions of the same models (i.e., same architecture without VFL+SMPC). There is no baseline comparison to any prior trust model, reputation system, or secure aggregation method from the literature. This makes it impossible to assess whether Secure-FLOATING improves over existing approaches.

- **"Real-time" is claimed throughout but never measured.** The paper repeatedly emphasizes real-time operation (abstract, introduction, Section 5 results) but reports zero end-to-end latency measurements. The only time-related metric is training time (Table 3), which does not measure how long the full endorsement pipeline takes from trajectory sharing to ledger update. Without latency data, the central claim of real-time feasibility is unsupported.

### Minor

- **Theorem 4.1 (differential privacy) proof is deferred to the appendix**, which was stripped during processing. Because the privacy guarantee is one of two formal theoretical contributions, deferring the entire proof makes this claim unverifiable from the main text.

- **Table 3 (training time) lacks a clear definition of what is being measured.** The vanilla ML training times grow roughly linearly with n (e.g., LSTM: 7.03s at n=1 → 699.87s at n=100 ≈ 100×), suggesting centralized training on pooled data, while VFL times stay nearly flat (12.32s → 17.01s), consistent with per-node local training plus communication. This pattern is interpretable but the paper never specifies whether vanilla ML is centralized or per-node, nor whether VFL time is per-node or total. The comparison conflates the effect of parallelization (FL vs. centralized) with the effect of the proposed framework.

- **Table 4 (MAE across network sizes) shows erratic vanilla ML values** (6.24 → 13.63 → 20.88 → 13.4 → 26.96 → 21.71 across n=1,5,10,30,50,100) that are not discussed. If these are per-node MAE values, network size should not affect prediction accuracy. If they are aggregate metrics, the metric definition is needed. The paper simply states the table "proves the scalability" without explaining this variation.

- **Threat model is narrow.** The paper only considers compromised trajectory data. Realistic attacks such as model poisoning during FL aggregation, Sybil attacks (authentication is stated as out of scope), and nodes that behave honestly during training but maliciously during inference are not addressed.

- **Figure 1b's "Percentage of Trusted Groups" is not defined.** The paper does not explain how a "trusted group" is defined, how attackers are injected, or what it means for 75% of groups to be trusted when 50% of nodes are attackers. The reviewer concern that this could represent a security failure (many malicious nodes still being trusted) rather than a success is reasonable given the absence of a definition.

### Trivial
- Theorem 4.2 proof base case writes `f(1) = 3(1) - 2 = 1` when the theorem states `f(n) = 2n - 1` (both evaluate to 1, but the expression used in the proof is inconsistent with the theorem).
- The toy SMPC example in Section 3.2 has an inconsistency: node v3's distance of 4.5 is split into 5, -1, 0.5, but the sum 5+(-1)+0.5 = 4.5, while the text says "v3 randomly generates 5, -1 and 0.5" without clarifying the arithmetic.

## Nice-to-Haves
- Include one well-controlled end-to-end latency measurement for the full endorsement pipeline (prediction → comparison → share exchange → ledger update) to substantiate the "real-time" claim.
- Add an ablation study that separates the contribution of each component (VFL alone, VFL+SMPC, VFL+SMPC+endorsement protocol) to isolate what each layer adds.
- Compare against at least one existing trust model from the cited related work (e.g., a baseline reputation system or a prior blockchain-based trust framework).

## Removed Points

These points from the reviewers were considered but removed or demoted from the main weakness list:

1. **"Training time comparison is fundamentally misleading / uninterpretable"** (Harsh Critic #2) — Removed. The pattern in Table 3 is consistent with vanilla ML = centralized training on all pooled data (time scales with n) and VFL = per-node local training plus aggregation (near-constant). The paper does not state this explicitly, which is a valid minor clarity concern, but the critic's assertion that "this result is uninterpretable and cannot be used to support any conclusion about efficiency" is incorrect. The comparison primarily demonstrates parallelism benefits, which is a fair criticism of the claim, not of the data.

2. **"No existing prior work identified that Secure-FLOATING builds upon"** — Removed. The related work section identifies gaps in existing approaches and positions the paper's contribution relative to those gaps. This is a reasonable way to establish context; the paper is not required to name a single prior work it directly improves upon.

3. **"The MAE comparison is poorly explained"** — Demoted to Minor and merged. The critic's stronger claim that the table "cannot be used to support scalability" overstates the problem; the VFL MAE column is stable (6.43–6.69) across all n, which is the main point. The erratic vanilla ML values are a secondary issue noted above.

4. **"Zero-knowledge proof component is missing / not implemented"** — Kept as Major. However, the critic's framing that this makes the evaluation "fatally flawed" is too strong — the paper can be evaluated on what it does implement (VFL+SMPC+endorsement), and the ZKP claims can be corrected in revision. The issue is overclaiming, not that the method fails without ZKP.

5. **"Permissioned blockchain assumption out of scope is central to security"** — Removed. The paper explicitly states this is out of scope, which is a reasonable scoping choice for a first framework proposal. Many papers assume authenticated nodes as a precondition.

6. **"SMPC toy example conflates privacy with Byzantine fault detection"** — Removed. The paper's description of the toy example and the endorsement process (where mismatch indicates untrustworthy nodes) is a design choice. It may not be the most robust approach but it is not "incorrect" as stated.

7. **"No latency or throughput results"** — Kept as Major (merged with the real-time measurement gap above).

8. **"Strength: Formal proof of linear scalability with rigorous empirical validation"** — Removed as a strength. The proof has an inconsistency (see Major weakness #1), and the "rigorous empirical validation" conflates parallelism with framework benefit (see Minor weakness on Table 3).

9. **Strength: "Comprehensive multi-metric comparison across trust baselines"** — Removed. There are no trust baselines from the literature, only vanilla versions of the same models. The comparison is comprehensive in model types but not in baselines.

## Novel Insights

None beyond the paper's own contributions. The two reviews reinforce each other on the core issues (overclaimed contributions, evaluation gaps, proof errors) without adding genuinely novel observations. The key takeaway that emerges from reading the paper directly is that the framework is better described as VFL + SMPC secret sharing + IPFS storage + peer-level trajectory endorsement, and the claims about ZKP and blockchain consensus should be recalibrated.

## Suggestions

1. **Correct Theorem 4.2 to be internally consistent.** Either adjust the statement to `f(n) = 3n - 2` (which matches the inductive proof) or rewrite the proof to prove `f(n) = 2n - 1`. Both are O(n), but the version presented must be self-consistent.

2. **Remove or implement the ZKP claim.** Either describe and evaluate the zero-knowledge proof component, or remove all references to it from the abstract, introduction, and conclusion.

3. **Recalibrate the "blockchain" terminology.** Describe IPFS honestly as a distributed storage backend, and clarify that consensus is achieved via peer-level trajectory matching, not through blockchain mining or BFT.

4. **Add at least one baseline from the literature.** For example, compare against a simple reputation-based trust model or a prior FL-based trust framework.

5. **Measure and report end-to-end latency** — the time from trajectory sharing to ledger update for a single endorsement round. Without this, the "real-time" claim is unsupported.

6. **Clarify what Table 3 is measuring.** State explicitly whether vanilla ML training is centralized (all data pooled) or per-node, and whether VFL times are per-node or total. This will make the results fully interpretable.

## Score and Decision

**Calibration Summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| `/home/wg25r/review_agent/human_reviews/oA5GmyvMUY.md` | 3.00 | R1 (weak) | FL defense for AVs; similar scope, similar evaluation gaps (no baselines, weak experiments), but our paper is more ambitious with more overclaim issues |
| `/home/wg25r/review_agent/human_reviews/E3qIInyTgL.md` | 3.33 | R1 (weak) | VFL Byzantine defense; similar level of rigor issues, our paper is broader but less focused |
| `/home/wg25r/review_agent/human_reviews/b8hRudcKQ3.md` | 3.50 | R2 (narrow) | FL marketplace; better defined scope but narrow evaluation (CIFAR-10, 2-3 clients). Our paper is weaker on claims substantiation |
| `/home/wg25r/review_agent/human_reviews/r1IbewSnqq.md` | 4.00 | R2 (narrow) | FedQV; has theoretical analysis, clear methodology, misses baselines. Our paper has more severe overclaim issues and weaker execution |
| `/home/wg25r/review_agent/human_reviews/tqYx8DgL0u.md` | 3.67 | R1 (mid) | PPFL via HANs; security claims without proof, similar overclaim issues, but more thorough evaluation |
| `/home/wg25r/review_agent/human_reviews/J1SGf2lyr6.md` | 2.50 | R1 (weak) | FL anomaly detection; very limited evaluation. Our paper is more ambitious and has more data |
| `/home/wg25r/review_agent/human_reviews/2cF3f9t31y.md` | 6.50 | R1 (mid) | MPC data markets; strong evaluation, clear contribution. Our paper is substantially weaker |
| `/home/wg25r/review_agent/human_reviews/jj5ZjZsWJe.md` | 8.00 | R1 (strong) | FL communication compression; rigorous theory, thorough experiments. Not comparable in quality |

**Round 1 bracket:** 2.5 – 4.0. **Round 2 narrowing:** Compared against anchors in 1.5–5.5 range, the paper is closest to the 3.0–3.5 anchors but with more severe overclaim issues (unimplemented ZKP, IPFS-as-blockchain) that place it below the 3.5 anchors.

The paper tackles an important and timely problem, uses realistic data, and provides a multi-dimensional model comparison. However, the execution has significant issues that prevent the paper from supporting its own claims: the theoretical proof is internally inconsistent; zero-knowledge proofs and blockchain consensus are claimed but not implemented; the "real-time" claim has no supporting latency measurements; and there are no baselines from the existing literature. The paper would need substantial revision — particularly correcting the proof, recalibrating claims, and adding proper baselines and latency measurements — before it could be considered for acceptance.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>