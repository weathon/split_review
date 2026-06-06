---

## Summary

Pctx proposes a personalized context-aware tokenizer for generative recommendation (GR). Rather than mapping each item to a fixed semantic ID derived from item features alone, Pctx conditions tokenization on a user's full interaction history: an auxiliary DuoRec model encodes user-context representations, which are clustered per item, fused with item feature embeddings, and quantized via RQ-VAE into multiple personalized semantic IDs. An autoregressive GR model is then trained on these IDs with data augmentation and multi-facet beam-search decoding. Experiments on three Amazon Review datasets report up to 8.9% improvement in NDCG@10 over the best prior static and context-aware tokenization baselines.

---

## Strengths

- **Consistent, statistically significant gains across all three datasets and four metrics** (Table 2): NDCG@10 improvements of +7.23% (Instrument), +8.90% (Scientific), and +3.67% (Game) over ActionPiece, all significant at $p < 0.05$. The gains are not dataset-specific flukes.
- **Comprehensive ablation that isolates every design decision** (Table 3): removing clustering (2.1), redundant semantic ID merging (2.2), data augmentation (3.1), or multi-facet generation (3.2) all degrade performance. Notably, removing redundant-ID merging causes a catastrophic drop (NDCG@10: 0.0341 → 0.0221 on Instrument), concretely validating the sparsity-balancing strategy as essential.
- **Ensemble control experiment rules out the multi-model-combination hypothesis** (Table 4): TIGER+DuoRec (voting) achieves NDCG@10 of 0.0314 on Instrument, while Pctx achieves 0.0341—an 8.6% relative gap—demonstrating that the gains arise from personalized tokenization, not from combining complementary model signals.
- **Non-obvious insight about DuoRec**: as shown in Tables 2 and 3, DuoRec performs *worse* than SASRec as a standalone recommender, yet its representations enable substantially better personalized tokenization than SASRec's (0.0341 vs. 0.0330 NDCG@10). This correctly identifies that representation discriminability—not next-item prediction accuracy—is what matters for tokenization quality.
- **Effective sparsity management** (Figure 3 and Section 2.2.2): the redundant-ID merging strategy keeps most items at two personalized IDs, preventing the over-personalization failure mode, which the paper explicitly acknowledges and addresses as Challenge C2.

---

## Weaknesses

### Fatal
None.

### Major

- **Missing MTGRec direct comparison.** Section 2.4 explicitly names MTGRec (Zheng et al., 2025) as the closest competing paradigm—a multi-identifier tokenizer that also breaks one-item-to-one-semantic-ID mapping. Yet MTGRec is absent from Table 2. The paper's conceptual argument for why Pctx is different (context-conditioned vs. epoch-sampled IDs that still assume universal similarity) is well-stated, but without an empirical head-to-head comparison, readers cannot verify whether the *personalization mechanism* or merely the *one-to-many ID mapping* drives the gains. The ablation variant (3.4) w/ Random Target is a partial substitute—Pctx leads it by 5.2% and 2.4% NDCG@10 on Instrument and Scientific respectively—but Random Target is not MTGRec. Including MTGRec would definitively locate the value of Pctx's context-conditioning versus the structural advantage of multi-ID mapping.

- **No discussion of computational cost.** Pctx is a multi-stage pipeline: train DuoRec → compute context representations over all training instances → cluster per item → fuse and run RQ-VAE → train GR model. The paper reports no training time, memory footprint, or inference latency relative to baselines such as ActionPiece or TIGER. For a method that requires an auxiliary pretrained model as a mandatory preprocessing step, this omission is a meaningful gap for practical adoption; a reviewer cannot assess whether the accuracy gains justify the added complexity.

### Minor

- **Ablation Table 3 covers only two of three datasets (Instrument and Scientific), excluding Game**, where the improvements are the smallest (3.67% NDCG@10). The excluded dataset is precisely where ablation results would be most informative about component contributions under a harder improvement regime. The omission does not invalidate the ablation but narrows its generality.

- **The α hyperparameter in Equation (2) lacks main-body discussion.** α directly controls the balance between item-feature signal (the baseline for non-personalized methods) and context signal (the novel part). If α is small, Pctx degenerates toward TIGER. The implementation details are deferred entirely to Appendix C.3; the main body should at minimum report the chosen value and note whether performance is sensitive to it.

### Trivial

- The case study (Section 3.5) presents a single selected example (StarCraft II) to illustrate context-dependent tokenization. The GPT-4o discriminator experiment used to support explainability claims is mentioned only in the LLM use statement, with all details in the appendix. A one-sentence summary of its scale (number of items examined, agreement rate) in the main body would ground the explainability claim.

---

## Nice-to-Haves

- Report variance over multiple training runs, or at minimum confirm that the paired t-test is computed over per-user scores rather than a single aggregate number. Given that Pctx vs. (3.4) w/ Random Target differences are modest, this would strengthen the personalization-over-randomness claim.
- Provide a more fine-grained analysis of *when* personalized IDs change recommendation outcomes—e.g., whether the semantic ID chosen by Pctx is more predictive of a user's subsequent behavior than the random-target variant assigns. This would move the personalization claim from aggregate metrics to a mechanism-level demonstration.
- The fusion Equation (2) uses a simple concatenation with scalar weighting; an exploration of alternative fusion mechanisms (e.g., gating, cross-attention) as a sensitivity analysis would be a natural extension.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Statistical variance / single-run evaluation** (Harsh Critic): Single-run evaluation is the norm in the recommendation community at large-scale benchmarks. Requesting confidence intervals across multiple runs is a methodological standard not universal in this field. Moved to Nice-to-Have (partially retained there as a suggestion rather than a weakness).
- **Temporal leakage concern with DuoRec training** (Harsh Critic): This is speculative; the paper uses the same training split for both DuoRec and the GR model, which is standard practice. No concrete evidence of leakage exists in the paper. Removed as a speculative reproducibility concern.
- **Score-level ensemble could narrow the Table 4 gap** (Harsh Critic): The gap between TIGER+DuoRec (0.0314) and Pctx (0.0341) is substantial, and the paper's point—that Pctx is not a naive ensemble—holds convincingly at these margins. This is speculation about a stronger ensemble that wasn't run. Removed.
- **Generic strength about "addressing an important problem"** (Strength Finder): Removed as non-specific.

---

## Novel Insights

The finding that DuoRec, a *worse* next-item predictor than SASRec on these benchmarks, produces *better* context representations for personalized tokenization is the paper's most intellectually interesting empirical observation. It suggests that sequence-encoder quality for tokenization should be evaluated by representation discriminability (via contrastive objectives) rather than by downstream prediction accuracy—a principle with implications for how auxiliary encoders should be selected or trained in other context-conditioned pipeline systems. The paper correctly identifies and discusses this result, but its broader implication for encoder design in multi-stage GR systems deserves emphasis.

---

## Suggestions

1. Add MTGRec to Table 2 (or provide a rigorous explanation why it cannot be evaluated on these three datasets, with an alternative empirical surrogate). This is the single highest-leverage addition.
2. Add a "Computational Cost" row or paragraph comparing training and inference time of Pctx vs. ActionPiece and TIGER.
3. Expand the ablation in Table 3 to include the Game dataset.
4. Report the chosen value of α and a sensitivity curve (e.g., α ∈ {0.2, 0.4, 0.6, 0.8}) in the main body, since α is architecturally central.
5. Summarize the GPT-4o explainability experiment outcome (scale and result) in one sentence in the main body.

---

## Score and Decision

**Originality:** The first personalized tokenizer for GR, with a well-motivated technical design; high originality within the GR tokenization subfield.
**Importance:** Personalization is a core bottleneck in GR; addressing it at the tokenization stage is a structurally significant contribution.
**Claims supported:** The main claims (personalization improves GR, components each contribute) are well-supported. The specific attribution of gains to the *personalization mechanism* vs. *multi-ID mapping* is less cleanly established due to the absent MTGRec comparison, but the Random Target ablation provides a non-trivial partial answer.
**Soundness:** The pipeline is methodologically coherent; the ablation is thorough; the ensemble control is well-designed. Missing computational analysis is the main gap.
**Clarity:** Well-written and clearly structured. The theoretical motivation in the introduction is precise.
**Community value:** Provides actionable insights (DuoRec vs. SASRec for encoding, redundancy merging as critical) and an open-source codebase, making the work reproducible and extendable.

Overall, this is a solid, well-executed paper with genuine novelty and consistent empirical evidence. The most significant weakness—the missing MTGRec comparison—is addressable and does not invalidate the contribution. The paper merits acceptance with a strong expectation that the MTGRec comparison be added in revision.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>