Now I have a thorough understanding of the paper and calibration. Let me compile the final review.

---

## Summary

This paper identifies and formally studies Dual-level Noisy Correspondence (DNC) in multi-modal entity alignment (MMEA) — the problem of misaligned entity-attribute pairs (intra-entity) and misaligned entity-entity / attribute-attribute pairs (inter-graph). The authors propose RULE, a framework that estimates correspondence reliability via a joint uncertainty-consensus principle, uses those reliabilities for robust intra-entity attribute fusion and robust inter-graph discrepancy elimination, and incorporates a test-time correspondence reasoning (TTR) module that leverages a multimodal LLM to uncover latent attribute connections across graphs. Extensive experiments on five benchmarks across inherent and synthetic noise settings show consistent and often substantial improvements over seven baselines.

## Strengths

- **Well-motivated and clearly defined DNC problem.** The paper convincingly demonstrates that noisy correspondences exist at two levels in MMEA (intra-entity and inter-graph), and Figure 1(b) empirically shows how both noise types degrade fusion and alignment. The problem is both novel and practically important for the MMEA community.

- **Principled reliability estimation via uncertainty-consensus.** The two-fold principle (Eq. 1) combining Dirichlet-based uncertainty (Eqs. 2–3) with consensus (Eq. 5) is well-justified. Theorem 1 formally establishes that uncertainty alone is insufficient, and Figure 4 provides compelling empirical separation of clean, low-consensus, and high-uncertainty pairs. This dual-signal approach is the paper's core technical contribution.

- **Comprehensive empirical validation across diverse settings.** Tables 1–2 cover five benchmarks (ICEWS-WIKI, ICEWS-YAGO, three DBP15K variants), three noise levels (inherent, 20%, 50%), and two evaluation protocols (Non-name, All-attributes). RULE consistently achieves best results; average H@1 gains over the strongest baseline range from +5.2% (inherent, Non-name) to +10.3% (50% DNC, Non-name). Figure 3(a) confirms slower degradation as noise increases.

- **Thorough ablation and analysis.** Table 3 validates the necessity of DRL, DRF, and TTR modules. Figure 3(b) shows reliability distributions cleanly separating clean from noisy pairs. Figure 5 qualitatively demonstrates that noisy attributes receive lower reliability scores than clean ones. These analyses support the paper's mechanistic claims.

## Weaknesses

### Fatal

None.

### Major

- **Missing comparison with the most directly relevant noise-robust baseline.** Chen et al. (2024), "Tackling Uncertain Correspondences for Multi-modal Entity Alignment," is cited in the references and explicitly addresses uncertain/noisy correspondences in MMEA — the same problem setting as this paper. It does not appear in any of the experiments (Tables 1–2, Figure 3). Without this comparison, it is impossible to assess whether RULE's uncertainty-consensus mechanism actually outperforms prior noise-handling designs for MMEA specifically, or whether gains come from other components. The paper already compares against seven strong baselines, so this omission does not invalidate the contribution, but it leaves a significant evidential gap for the core claim of robustness against DNC.

- **Headline results include the TTR module, which uses a 72B-parameter MLLM unavailable to baselines.** The test-time correspondence reasoning (TTR) module (Section 2.5) uses Qwen2.5-VL-72B-Instruct to refine attribute similarities at inference. No baseline receives any analogous test-time resource. While Table 3 provides an ablation showing RULE without TTR ("w/o TTR") still outperforms baselines (e.g., 56.5 vs. 54.0 MEAformer on Non-name 50% DNC), the main Tables 1–2 present RULE+TTR as the method, inflating the apparent gap. The paper should present "RULE w/o TTR" alongside the full model in the main tables, or at minimum discuss this asymmetry explicitly. The training-time contributions are strong enough to stand on their own and the TTR module is a genuine contribution, but the current presentation overstates the margin.

### Minor

- **Test-time reliability estimation is insufficiently specified.** Section 2.2.2 describes estimating the correct correspondence at inference via a greedy marginal-contribution strategy (Eqs. 6–7, Assumption 1), but Section 2.5 then uses reliability weights \(\hat{w}_i^m\) for test-time reasoning without clarifying how attribute-level reliabilities are derived without ground-truth correspondences. A reader cannot reconstruct the full test-time pipeline. A standalone description of the test-time reliability computation would resolve this.

- **The claim that real-world benchmarks contain "over 50%" NC is not verifiable from the main text.** The supporting statistics are deferred to Appendix B (stripped in review). While the inherent DNC results in Tables 1–2 do show RULE outperforming baselines even without injected noise — supporting the existence of real NC — the specific magnitude claim lacks evidence in the presented text.

- **No statistical variation reported.** The results rely on stochastic training and noise injection (random reassignment of entities/attributes). Given the high noise levels (50%), variance could be non-trivial. Reporting error bars or multiple-run statistics would increase confidence, particularly for the high-noise regime where baseline degradation is dramatic.

### Trivial

- The description of how attribute-level reliability \(w_i^m\) is computed (mentioned in Section 2.4) lacks detail in the main text; the reader is told to assume a parallel to the entity-entity case but the specific adaptation is not shown.

- Figure 1(b) caption labels one axis with an unmarked metric (0.00–0.06) without clarifying what it represents; this makes the observation charts harder to interpret at a glance.

## Nice-to-Haves

- A comparison with Chen et al. (2024) under the same noise settings would complete the evaluation narrative.
- A lightweight test-time refinement alternative (e.g., a small learned scorer) could make the TTR contribution less dependent on a resource-heavy external model and increase practical applicability.
- Ablating the test-time greedy correspondence estimation (showing performance with and without the estimated \(y_i\) at inference) would isolate whether this component adds value or introduces circularity.
- Experiments under mixed or dynamic noise severity would better reflect real-world deployment conditions.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Harsh Critic #1 about missing Chen et al. (2024) baseline was retained (Major)** — after verification, Chen et al. (2024) appears in the reference list but is not compared against experimentally. This is a legitimate gap.

- **Harsh Critic #2 about "unfair comparison" due to TTR** — partially retained as Major but weakened: the paper *does* provide the w/o TTR ablation (Table 3), so the criticism that "no baseline is allowed any analogous post-hoc reasoning step" is factually correct but the paper is transparent about the breakdown. The retained version focuses on the headline table presentation rather than claiming the evaluation is fundamentally unfair.

- **Harsh Critic #3 about "circular reliability estimation"** — retained as Minor because the paper does describe the greedy estimation strategy (Eqs. 6–7); the problem is insufficient clarity, not a demonstrated circularity. The criticism that "the paper never clarifies how these weights are obtained" is partially addressed by Section 2.2.2 itself, though the connection to Section 2.5's \(\hat{w}_i^m\) is indeed unclear.

- **Harsh Critic claim about "Figure 1(b) and its caption are ambiguous"** — partially valid (the second y-axis label is unclear) but demoted to Trivial, as it does not affect the paper's substance.

- **Harsh Critic claim about "Cristiano Ronaldo/Mexico example being conceptually separate from DNC"** — removed. This example illustrates the motivation for the TTR module (test-time misidentification due to seemingly similar attributes), which is a distinct but complementary contribution to the DNC robustness. It is not claimed to be part of DNC itself.

- **Strength Finder: "over 50% in ICEWS benchmarks" claim** — partially retained as Minor weakness because the supporting statistics are in the stripped appendix rather than the main text, though the inherent DNC results provide indirect evidence.

- **Harsh Critic claim about All-attributes results being "extremely high" reducing task difficulty** — removed. High scores on All-attributes is a well-known phenomenon in MMEA (due to name attribute dominance) and the paper correctly also reports Non-name results where scores are lower and gaps are larger. This is not a weakness of this paper specifically.

- **Strength Finder generic strengths about "clearly motivated," "well-defined," "important problem"** — removed from strengths as these are generic framing strengths without specific evidence beyond what's already captured in the retained strengths.

## Novel Insights

The paper's key insight is that uncertainty and consensus provide complementary signals for identifying noisy correspondences, and that using both jointly (rather than either alone) enables robust learning. Theorem 1 formalizes why uncertainty alone is insufficient — low uncertainty does not guarantee the belief mass concentrates on the correct correspondence — which justifies the consensus term as a necessary complement. This formal observation, combined with the empirical demonstration in Figure 4 that the two principles cleanly separate noise types, is the paper's most transferable conceptual contribution beyond the MMEA domain.

## Suggestions

- Add Chen et al. (2024) as a baseline in the experiments or explicitly explain why a comparison is not possible (e.g., incompatible settings, code unavailable). If the method is contemporaneous and the authors were unaware during submission, acknowledge this limitation.
- Present the "w/o TTR" variant in the main Tables 1–2 alongside the full RULE to make the training-time vs. test-time contribution transparent upfront, rather than only in the ablation table.
- Add a clear subsection or paragraph describing how attribute-level reliability \(\hat{w}_i^m\) is computed at test time without ground-truth correspondences, explicitly connecting the greedy estimation from Section 2.2.2 to the TTR weights in Section 2.5.

## Score and Decision

**Bracket:** Round 1 placed the paper between roughly 6.0 and 8.0 based on comparison with entity alignment and multi-modal noise-robust learning papers. Round 2 narrowed further with anchors at 6.67 (GEEA — generative EA, similar domain but fewer experiments and less novelty), 7.00 (M3C — graph matching/clustering, similar reception profile), and 7.33 (weighted point cloud for contrastive learning, strong theory but limited practical novelty). RULE is stronger than the 6.67 GEEA paper (more benchmarks, more baselines, clearer problem framing) but weaker than the 8.00 anchors (Norton, READ — also from the same lab, with near-universal reviewer praise and no significant weaknesses). The missing baseline and TTR presentation concerns prevent RULE from reaching the 8.0 tier. RULE sits at approximately 7.0: a solid accept with real but addressable weaknesses.

**Anchor list:**
- a4O528mek9 (3.00, Round 1) — multi-modal incomplete data; RULE is substantially stronger
- rwdeKOdAwY (3.00, Round 1) — multimodal retrieval; different domain, much weaker
- YrxhSkfHh0 (3.33, Round 1) — multimodal feature extraction; much weaker
- 4qRCiEZGKd (3.40, Round 1) — description logic over incomplete KGs; much weaker
- jy6Lj3JaOf (4.50, Round 1) — multimodal attributed graphs benchmark; not directly comparable
- NNUiUwQWx6 (5.75, Rounds 1–2) — neuro-symbolic EA; RULE is clearly stronger
- QQYpgReSRk (6.25, Round 2) — noisy entity annotated images; different task, RULE stronger
- ue1Tt3h1VC (6.60, Rounds 1–2) — MoE for MMKG completion; comparable but RULE has more comprehensive experiments
- z3dfuRcGAK (6.67, Rounds 1–2) — generative EA; RULE is slightly stronger with broader evaluation
- AXC9KydyZq (7.00, Round 2) — graph matching/clustering; RULE is comparable
- ftGnpZrW7P (7.00, Round 2) — Gramian multimodal alignment; different domain
- bqoHdVMIbt (7.00, Round 2) — multimodal unsupervised DG; different domain
- uSz2K30RRd (7.33, Round 2) — weighted point cloud contrastive; RULE has more practical impact but similar novelty
- 9Cu8MRmhq2 (8.00, Round 1) — Norton (same lab); RULE is weaker due to the identified evaluation gaps
- TPZRq4FALB (8.00, Round 1) — READ (same lab); RULE is weaker
- uAFHCZRmXk (8.00, Round 1) — modality gap analysis; different task
- z8sxoCYgmd (8.00, Round 1) — synthetic data detection; different domain

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>