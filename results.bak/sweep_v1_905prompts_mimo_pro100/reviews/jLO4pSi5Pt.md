Now I have enough calibration data. Let me synthesize the final review.

**Round 1 bracket**: 5.5–7.5 (paper is clearly above rejected TTA papers at 4.67–6.00, and comparable to accepted TTA papers at 6.25–7.00).

**Round 2 anchors** (read in full): 
- DeYO (7.00) — TTA with novel confidence metric, broader but less focused problem; our paper is more targeted and has better empirical breadth
- RLCF (6.67) — actually a baseline in this paper; our paper is stronger
- Concept drift MLLM (7.00) — similar topic but at pre-training level, mixed reviews (6,8,6,8); our paper is more focused and empirically consistent
- Multi-Label TTA BEM (6.25) — narrower scope, weaker experimental validation; our paper is stronger
- DOTA (6.00) — same VLM TTA domain, rejected; our paper is substantially stronger with better novelty

Final calibration places this paper at **7.0** — above the 6.25–6.75 anchors, on par with the 7.00 anchors but with better empirical consistency.

---

## Summary

This paper proposes L-TTA, the first method for long-tailed test-time adaptation of vision-language models. It consists of three co-designed components: Synergistic Prototypes (Deterministic + Exclusionary Prototypes) for enriching tail-class representations, Rebalancing Shortcuts with a Class Re-Allocation loss for dynamic class balancing, and Balanced Entropy Minimization (BEM) for countering head-class bias in standard entropy minimization. The paper identifies two novel failure modes unique to this setting (Text-induced Tail Erosion and Modality-bias Amplification) and demonstrates consistent improvements over strong baselines across 15+ datasets, three benchmark types, and three imbalance ratios.

## Strengths

- **Novel and well-characterized problem formulation.** The paper identifies and empirically demonstrates two specific failure modes for long-tailed TTA with VLMs: (1) text embeddings carry pre-training biases that exacerbate tail erosion (Figure 1b.1), and (2) unimodal LT-TTA methods like SAR fail catastrophically when applied to VLM backbones (Figure 1b.2, with "significant performance drop and instability"). These are concrete, illustrated observations rather than abstract motivation.

- **Consistent and significant empirical improvements across diverse settings.** Tables 1–3 show L-TTA achieves the highest accuracy AND macro-F1 across OOD, Cross-Domain, and Corruption benchmarks under all three imbalance ratios (10, 20, 50). Critically, macro-F1 improvements consistently exceed accuracy improvements (e.g., 1.70% macro-F1 vs 1.47% accuracy on OOD Average at imb=10), confirming class-balancing rather than just head-class gains. The robustness gap is particularly striking: L-TTA's macro-F1 drops only 1.40% from imb=10 to imb=50 on OOD Average, versus 4.22% for TDA and 3.59% for SCAP (Table 1).

- **Well-designed multi-component method with ablation support.** Each component (DP, EP, RS, BEM) contributes measurably: Table 6 shows dropping EPs causes −3.22% macro-F1 and dropping BEM causes further degradation. The synergy between components is validated rather than asserted.

- **Strong efficiency profile.** Table 4 shows L-TTA achieves 1.45h runtime and 1.89G memory — comparable to DPE (1.38h/1.81G) and vastly faster than RLCF (18.30h) or WATT (27.70h), while achieving the highest harmonic mean of accuracy and macro-F1 (67.20).

- **Generalization across multiple stronger backbones.** Table 5 confirms L-TTA maintains ~1.5% Acc. / 1.8% Mac. improvements over baselines on ViT-L/14, ViT-H/14, SigLIP-L/16, and MetaCLIP-BigG, including cases where SCAP produces invalid outputs on MetaCLIP-BigG.

## Weaknesses

### Fatal
None

### Major
None

### Minor

- **Baselines use only their published hyperparameters without any long-tailed adaptation.** The paper states "methods for comparison are reproduced with their provided hyperparameters" (§4). While this is standard practice in TTA — where methods are deployed without test-label access — L-TTA is purpose-built for the long-tailed setting while baselines carry balanced-setting hyperparameters. Even a single baseline with a modest hyperparameter sweep under long-tailed conditions would clarify how much of L-TTA's advantage is methodological versus tuning-based. The consistency of gains across 15+ datasets mitigates this concern, but it remains the most significant question about the evaluation.

- **Head/tail class accuracy not reported in main tables.** For a paper whose central claim is improved tail-class performance, the main tables (Tables 1–3) show only overall accuracy and macro-F1. Head/tail accuracy is deferred to Appendix C. This is the single most important diagnostic for validating the paper's core claim and should be front-and-center. The macro-F1 improvements do provide indirect evidence of tail-class gains, but direct head/tail columns would make the case much more compelling.

- **Pseudo-label feedback loop in BEM class prior estimation is not empirically addressed.** BEM uses class priors π that are "continually updated based on the current predicted pseudo-labels" (§3.2). Since pseudo-labels are the model's own predictions — already biased toward head classes — using them to estimate the priors that correct that same bias creates a circular dependency. An ablation comparing fixed cardinality priors versus dynamically estimated ones would clarify whether this feedback helps or hurts.

### Trivial

- **BEM penalty term $\tilde{\mathbb{P}}$ is not explicitly defined.** In Eq. 9, the penalty term $(1 - \tilde{\mathbb{P}})^\beta$ uses $\tilde{\mathbb{P}}$ without a clear definition. Based on context ("drastically reduces the contribution of confident classes"), it appears to be $\max_c \mathbb{P}(y_c|x)$. This should be stated explicitly.

- **Corruption benchmark (Table 3) only uses imb=10.** The OOD and Cross-Domain benchmarks test imb ∈ {10, 20, 50}, but the corruption benchmark uses only the mildest imbalance ratio. Testing at imb=50 would strengthen the corruption robustness claims.

- **Propositions say "with certain measurements" for the head/tail split.** The split criterion (top-20% as head) is stated in §4 but not referenced in the propositions themselves.

## Nice-to-Haves

- A visualization or quantitative analysis of what Exclusionary Prototypes encode (e.g., cosine similarity between EPs and DPs per class, effective update magnitude for head vs. tail classes) would strengthen the EP contribution beyond the ablation.
- Ablation of the entropy threshold θ for DP updates, which is mentioned but never varied.
- Failure mode analysis: when does L-TTA fail? Are there cases where the prototype-based approach introduces its own biases?
- The corruption benchmark with higher imbalance ratios (imb=50).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Unfair comparison" framing from harsh critic.** The critic frames using published hyperparameters as a structural flaw, but this is standard TTA methodology. In TTA, methods must work without access to test labels, so using published hyperparameters is the fair protocol. L-TTA's own hyperparameters are also not dataset-tuned — they're fixed across all 15+ datasets and imbalance ratios. The critic's concern is real but overstated; it's a minor limitation, not a structural flaw.

- **Theoretical propositions called "weak and under-specified."** The critic dismisses Propositions 1 and 2 as "obvious," but they formalize a claim that is not trivial — that EM amplifies the head-tail gradient gap — and prove that BEM narrows it. The proofs are in the appendix (stripped by parser). The "certain measurements" phrasing is imprecise but the criterion is stated in §4. This is a presentation nitpick, not a substantive weakness.

- **Claim about EP data leakage.** The critic's concern that EPs for tail classes store "noise" is theoretically plausible but empirically contradicted: the ablation shows EPs contribute −3.22% macro-F1 when removed. The mechanism works, even if the theoretical motivation for why could be strengthened.

- **Table 7 insensitivity interpreted as a problem.** The critic suggests that insensitivity to temporal ordering (ε) means the method isn't leveraging temporal information. But stable performance across different orderings is a desirable robustness property, not a flaw.

## Novel Insights

The paper makes two genuinely novel observations that extend beyond its methodological contribution: (1) Text embeddings in VLMs carry pre-training biases that create "rich classes" which consistently yield higher accuracy regardless of head/tail status, and when these coincide with head classes, tail erosion is intensified — this is a VLM-specific phenomenon not captured by existing long-tailed learning theory. (2) Applying unimodal LT-TTA methods to VLM backbones actually makes things worse compared to using a pure visual backbone (Figure 1b.2), demonstrating that the multi-modal nature of VLMs is not merely an additional challenge but actively amplifies the long-tailed problem through modality-bias amplification.

## Suggestions

1. Add head/tail accuracy columns to all main result tables (Tables 1–3). This is the most direct way to validate the paper's central claim and costs only table space.
2. Provide one baseline (e.g., TDA or DPE) with a modest hyperparameter sweep (e.g., 3 learning rates × 3 temperatures) under the long-tailed protocol to bound the tuning gap concern.
3. Add an ablation of fixed vs. dynamic class priors in BEM to address the pseudo-label feedback loop.
4. Explicitly define $\tilde{\mathbb{P}}$ in Eq. 9 (appears to be $\max_c \mathbb{P}(y_c|x)$ based on context).
5. Add imb=50 results for the Corruption benchmark in Table 3.

## Score and Decision

**Evaluation axes:**
- **Originality**: High — first to identify and tackle long-tailed TTA for VLMs, with two novel failure modes and three co-designed components.
- **Importance**: High — long-tailed distributions are ubiquitous in real-world deployment, and TTA for VLMs is a growing area.
- **Claims well-supported**: Mostly — empirical claims are strongly supported by consistent results across 15+ datasets; theoretical claims are reasonable but deferred to appendix; EP benefit for tail classes is validated empirically but not mechanistically analyzed.
- **Soundness of experiments**: Good — broad coverage (datasets, backbones, imbalance ratios, benchmarks), but baseline fairness could be strengthened and head/tail diagnostics should be in main tables.
- **Clarity**: Good — well-structured, clear motivation with illustrated failure modes; some notation gaps (tilde P, certain measurements).
- **Value to community**: High — opens a new research direction with a strong baseline and code release.

**Reporting calibration results:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| pdzHpQbGrn | 2.50 | 1 | Far weaker — rejected, fundamental issues |
| HfJxXbXlYJ | 3.00 | 1 | Far weaker — rejected, tangential topic |
| ZaudLwn0Hm | 2.50 | 1 | Far weaker — rejected |
| gNoqEdT2wO | 2.33 | 1 | Far weaker — rejected |
| BUDxvMRkc4 | 4.67 | 2 | Weaker — rejected, similar topic but less novel |
| eXrUdcxfCw | 4.80 | 2 | Weaker — rejected, similar domain but sparse |
| Z2dVrgLpsF | 5.25 | 2 | Weaker — rejected, prototype methods |
| k9NYnsC4Mq | 5.67 | 2 | Weaker — rejected, VLM continual learning |
| yD2JMeKumt | 6.00 | 2 | Weaker — same VLM TTA domain, rejected; our paper is substantially stronger |
| 75PhjtbBdr | 6.25 | 2 | Comparable but weaker — TTA with BEM for multi-label, narrower scope |
| TD3SGJfBC7 | 6.25 | 2 | Comparable but weaker — few-shot TTA for CLIP |
| kIP0duasBb | 6.67 | 2 | Similar — TTA with CLIP Reward (actually a baseline in this paper); our paper is stronger |
| RzY9qQHUXy | 6.75 | 2 | Similar level — long-tailed data augmentation; our paper has broader scope |
| b20VK2GnSs | 7.00 | 1,2 | Similar — concept drift in MLLMs; our paper is more focused with stronger empirical consistency |
| 9w3iw8wDuE | 7.00 | 2 | Similar — DeYO TTA with novel metric; comparable novelty, our paper has broader benchmarks |
| g1fkhbhHjL | 7.00 | 2 | Similar — VLM adaptation; comparable contribution level |
| uAFHCZRmXk | 8.00 | 1 | Stronger — analysis paper on VLM modality gap |
| TPZRq4FALB | 8.00 | 1 | Stronger — multi-modal TTA with new paradigm and benchmarks; all 8s |
| WyEdX2R4er | 8.00 | 1 | Stronger — comprehensive VLM analysis |

**Round 1 bracket**: 5.5–7.5 (above rejected papers at 4.67–6.00, comparable to accepted papers at 6.25–7.00).

**Round 2 narrowing**: Paper is clearly above DOTA (6.00, rejected) and above the 6.25 anchors (ML-TTA BEM, frozen CLIP adaptation). It is comparable to the 7.00 anchors (DeYO, concept drift MLLM, Black Sheep) but with superior empirical breadth (15+ datasets, 3 imbalance ratios, 3 benchmarks, multiple backbones). The main limitations (baseline tuning, head/tail in main tables) are real but not severe enough to place it below 7.0. It does not reach 7.5+ because the theoretical analysis lacks explicit head/tail diagnostics and the pseudo-label feedback loop is unaddressed.

**Final score: 7.0** — A solid paper that introduces a genuinely new problem with a well-designed solution and convincing empirical breadth, limited by some evaluation gaps that could be addressed in revision.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>