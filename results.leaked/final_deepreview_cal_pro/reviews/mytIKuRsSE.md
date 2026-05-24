Now I have a thorough understanding of the paper and the calibration anchors. Let me produce the final consolidated review.

---

## Summary

This paper identifies and formalizes Dual-level Noisy Correspondence (DNC) in multi-modal entity alignment (MMEA) — noise at both intra-entity (entity–attribute) and inter-graph (entity–entity, attribute–attribute) levels. The authors propose RULE, which estimates correspondence reliability via an uncertainty-and-consensus principle, uses those reliability scores to guide robust intra-entity fusion (DRF) and inter-graph discrepancy elimination (DRL), and adds a test-time correspondence reasoning (TTR) module that leverages a large multi-modal language model (MLLM) to uncover latent cross-graph attribute connections. Experiments on five benchmarks with seven baselines under inherent and injected noise (up to 50%) show substantial gains.

## Strengths

- **Well-motivated problem formulation.** The DNC concept (Fig. 1a) is clearly defined and practically grounded. The paper demonstrates through experiments that both intra-entity and inter-graph noise degrade existing MMEA methods (Fig. 1b, Tables 1–2), establishing the problem's urgency.

- **Principled reliability estimation.** The two-fold principle combining evidential uncertainty (Eqs. 2–3) with a consensus signal (Eq. 5) is genuinely novel for MMEA. Theorem 1 provides theoretical motivation for why uncertainty alone is insufficient. Figures 3b and 4 empirically validate that the resulting reliability scores cleanly separate clean from noisy pairs and that the three subsets (S_U, S_I, S_C) occupy distinct regions of the uncertainty–consensus space.

- **Strong training-time contributions with clear ablation evidence.** The DRL and DRF modules are well-motivated and effective. Removing DRL drops Non-name H@1 from 58.2 to 31.6 at 50% DNC (Table 3). Removing DRF drops it by 7.8 points. The "Only Unc." and "Only Cons." variants each outperform the baseline, confirming both uncertainty and consensus contribute independently. On the Non-name setting, the training-time components alone (w/o TTR: 56.5 H@1) substantially outperform the best baseline (MEAformer: 42.4).

- **Extensive experimental scope.** Five diverse benchmarks (ICEWS-WIKI, ICEWS-YAGO, three DBP15K pairs), seven baselines, three noise levels (inherent, 20%, 50%), and both Non-name and All-attributes protocols. The baseline selection covers recent MMEA methods well (EVA, MCLEA, XGEEA, MEAformer, UMAEA, PMF, HHREA).

## Weaknesses

### Major

- **Test-time MLLM module creates an uneven comparison in headline results.** The TTR module (Section 2.5) uses Qwen2.5-VL-72B-Instruct, a 72-billion-parameter model, to refine similarity scores at inference time. None of the compared baselines have access to any comparable test-time reasoning module. The main results in Tables 1 and 2 include TTR, meaning the reported margins conflate the training-time method's contribution with the MLLM's contribution. The ablation in Table 3 helps disentangle this: on ICEWS-WIKI at 50% DNC, removing TTR reduces All-attributes H@1 from 97.7 to 94.0 — and at 94.0, RULE actually performs slightly *below* the best baseline MEAformer (94.7). This means the claimed superiority on the All-attributes setting depends substantially on the MLLM that baselines lack. The Non-name results are more robust (w/o TTR still beats all baselines by 14+ points), but the current presentation overstates RULE's fair advantage. The paper should either provide baselines with the same MLLM-based post-processing or report main results using only the training-time components, with TTR clearly presented as a separate, optional enhancement.

### Minor

- **Circular threshold estimation for pair division.** The thresholds β_u and β_c (Eq. 8) are computed using S^{TP}, the set of pairs where the model's own argmax prediction matches the ground truth. This creates a dependency loop: the pair division quality depends on the model's current accuracy, but the model's training depends on the pair division. Early in training, when the model is weak, S^{TP} may be noisy and produce poorly calibrated thresholds. The paper would benefit from discussing how this circularity affects training dynamics, or from a warm-up strategy analysis. (This is not fatal — many self-training and bootstrapping methods face similar challenges, and the method works empirically — but it warrants acknowledgment.)

- **Inherent noise measurement methodology is opaque.** The paper claims real-world benchmarks contain "over 50% noise in ICEWS" and refers to Appendix B (stripped by the parser). Without access to this appendix, the reader cannot assess what "over 50%" refers to (entity-entity? entity-attribute? all types combined?), how it was measured, or how synthetic noise composes with inherent noise. This makes it difficult to evaluate whether the experimental noise levels are realistic. The synthetic-noise experiments are independently valuable and clearly show robustness, so this does not threaten the core contribution, but the claim about inherent noise rates needs substantiation in the main text.

- **Gap between training-time consensus and inference-time estimation.** The training-time consensus definition (Eq. 5) uses ground-truth labels y_i, while inference-time estimation (Eqs. 6–7) uses a greedy marginal-contribution strategy justified only by Assumption 1. The paper does not empirically validate whether the greedy-estimated correspondence approximates the true consensus. An experiment comparing estimated vs. ground-truth correspondence on a held-out clean set would strengthen confidence in this approximation.

- **DRF's cross-graph-to-intra-entity proxy assumption is unstated.** The DRF module (Eq. 14) uses inter-graph reliability w_i^m to weight intra-entity attribute fusion. The logic — that an attribute is unreliable intra-entity if its cross-graph correspondence is unreliable — is reasonable but rests on an assumption that cross-graph attribute alignment quality proxies for intra-entity attribute relevance. The paper should state this assumption explicitly.

### Trivial

- Theorem 2 (upper-bound property of the Dirichlet integral in Eq. 11) is referenced but stated only in the appendix. A brief statement in the main text would help readers evaluate the claim without depending on supplementary material.
- The claim that "vanilla prompts fail to fully activate the deep reasoning capabilities of MLLM" (line ~227) is asserted without empirical comparison of prompt strategies in the main text; a brief summary of what the CoT prompt adds would improve readability.

## Nice-to-Haves

- Report inference cost (MLLM calls per query, wall-clock time) for the TTR module, since it uses a 72B-parameter model and may be a practical bottleneck.
- Report standard deviations across multiple runs for the main results, especially given the stochastic nature of noise injection.
- Compare with one representative general noisy-label or noisy-correspondence method adapted to MMEA, to contextualize the contribution beyond MMEA-specific baselines.
- Show how the three subsets S_U, S_I, S_C evolve over training epochs to demonstrate that reliability estimation improves as the model learns (addressing the circular-threshold concern dynamically).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Label refinement in Eq. 12 may cause error propagation."** The harsh critic argued that blending one-hot labels with model predictions weighted by consensus could reinforce errors. However, consensus-weighted label refinement is a standard bootstrapping technique used widely in robust learning (e.g., label smoothing, self-training with confidence weighting). The paper's specific instantiation — blending proportionally to consensus — is a reasonable mitigation, and the critic's concern is speculative without empirical evidence of error propagation. Removed.

- **"The paper does not report whether the MLLM-based TTR module was used for baselines."** The paper explicitly states TTR is part of RULE only (Section 2.5). The concern about unfair comparison is already captured in the Major weakness above, so this framing is redundant. Removed as a separate point.

- **"Comparison with general noisy-label methods is missing."** This is scope creep for an MMEA paper. Moved to Nice-to-Haves.

- **"DRF ablation w/o DRF (test) vs. w/o DRF (train) distinction is confusing."** The ablation table distinguishes training-stage and test-stage ablations, which is appropriate. Removed.

## Novel Insights

The most novel insight emerging from this work is that *uncertainty and consensus are complementary rather than redundant signals for identifying noisy correspondences in entity alignment.* Prior work in noisy correspondence learning has primarily used uncertainty-based filtering, but RULE demonstrates (Theorem 1 and Fig. 4) that low uncertainty alone does not guarantee correct correspondence — the belief mass may concentrate on the wrong candidate. Adding a consensus term that measures alignment with the annotated (or estimated) correspondence creates a more discriminative reliability score. This two-fold principle is clean, well-motivated, and likely applicable beyond MMEA to other cross-modal alignment tasks where both intra-modal and cross-modal noise coexist.

## Suggestions

- **Restructure the main results to isolate training-time contributions.** Report Tables 1–2 using RULE without TTR (i.e., DRL + DRF only), and present TTR results in a separate table or as a clearly marked "+ TTR" enhancement. This would make the comparison unambiguously fair and would not diminish the paper — the Non-name training-time results are already dominant.
- **Add a brief description of inherent noise measurement methodology to the main text** (even a one-paragraph summary of Appendix B), since the claim of "over 50% inherent noise" is central to the problem motivation.
- **Validate the consensus approximation** with a simple experiment: on a held-out clean subset, compare the greedy-estimated correspondence (Eq. 7) against ground-truth labels and report agreement rate.

## Score and Decision

**Round 1 bracket:** Based on the initial retrieval, the paper sits between weak anchors (avg ~3.0, clearly irrelevant or lower-quality papers) and strong anchors (avg 8.0, like Norton — a thoroughly polished paper with unified theoretical framework and comprehensive experiments). The plausible range is 5.5–7.5.

**Round 2 narrowing:** I compared against anchors within this bracket:
- NeuSymEA (5.75, Reject): entity alignment paper with weaker experiments and clarity issues. RULE is clearly stronger.
- MOFI (6.25, Accept): large-scale dataset contribution with fairness concerns about comparison. RULE has comparable quality — more novel method, similar fairness concern (MLLM advantage).
- TjhUtloBZU (6.25, Accept): noisy model learning paper with thorough experiments but modest gains (~1%). RULE has larger performance margins and more principled method design but shares comparable evaluation concerns.
- GEEA (6.67, Accept): entity alignment with generative perspective, theoretical contribution. RULE has more extensive experiments (5 datasets vs. typical 3, more noise settings) but weaker theoretical grounding.

RULE is somewhat stronger than MOFI and TjhUtloBZU in terms of methodological novelty and experimental thoroughness, but shares similar evaluation fairness concerns. It is not quite at the GEEA level due to the MLLM fairness issue and less theoretical rigor, but the training-time components are genuinely effective and well-ablated. I place RULE at **6.5**, between MOFI/TjhUtloBZU (6.25) and GEEA (6.67).

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>