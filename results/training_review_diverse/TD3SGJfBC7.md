Now I have all the information needed. Let me compose the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
// Leave empty if none apply.
### Major
### Minor
### Trivial
## Nice-to-Haves
## Removed Points
## Novel Insights
## Suggestions
## Score and Decision

Let me draft this carefully.

---

**Summary:** This paper tackles Few-Shot Test-Time Domain Adaptation (FSTT-DA) by introducing L2C, which attaches a lightweight parallel CPNet that learns dataset-specific visual features from the input space to complement frozen CLIP, combined with a greedy text ensemble for enhanced label semantics and domain-aware fusion that adapts both modalities to target domains. The method achieves strong results on 5 large-scale benchmarks (WILDS and DomainNet), notably improving over VDPG on weaker backbones like ViT-B/16.

**Strengths:**
1. Strong empirical results on 5 benchmarks with clear improvements over VDPG, especially on ViT-B/16 where prior methods struggle (e.g., +5.1 F1 on iWildCam, +3.1% WC Acc on FMoW — Table 1).
2. Clean ablation study (Table 3) validates each component individually, showing CPNet contributes substantially (+13.1 F1 on iWildCam over zero-shot CLIP), revert attention further improves, and text components add incremental gains.
3. Efficient design: CPNet uses only 3 transformer blocks for ViT-B/16 on DomainNet; the text encoder is discarded after preprocessing (cost <0.01% of total training); CLIP backbone is never fine-tuned.

**Weaknesses:**
### Major
- **Confounded attribution of gains over VDPG.** The paper's central narrative claims that "learning from the input space" via CPNet is the key departure from VDPG. However, L2C simultaneously introduces text features (greedy ensemble + refinement + cross-modal fusion) that VDPG entirely lacks. The main results (Tables 1, 2) compare a vision+text pipeline (L2C) against a vision-only one (VDPG), so gains cannot be cleanly attributed to input-space learning versus the addition of text modality. The ablation (Table 3, Index 1 vs. 2) shows CPNet improves over zero-shot CLIP, but zero-shot CLIP ≠ VDPG (which is a trained method with source-domain learning). A comparison of a vision-only L2C variant against VDPG is missing. (Note: the requested ablation is nontrivial because removing text features would also require replacing the CLIP contrastive loss, but the attribution question remains.)

### Minor
- **No statistical significance or variance reported.** Main results and ablations lack standard deviations or confidence intervals across multiple runs or few-shot draws. Given variability in domain splits and few-shot sampling, this limits reliability assessment.
- **Computational cost analysis is incomplete.** The paper claims the method is "lightweight" but reports no FLOPs, parameter counts, or inference-time overhead versus baselines. CPNet's depth is given for DomainNet (3 layers) but final per-dataset depths used for reported results are not explicitly stated (Fig. 4 shows a sweep, but the chosen values are not named in the main text).
- **Domain cache size L not specified in main text.** The cache is a key architectural component (Eq. 5), but its size is only analyzed in the (stripped) appendix. A typical value or range should appear in Section 4.3.

### Trivial
- **"Gradient-free" phrasing is imprecise.** The paper states "Our work introduces a practical, gradient-free adaptation method" (Related Work). At test-time, adaptation indeed requires no gradients (domain prompt uses only forward passes through CPNet + cache). However, the training pipeline (CPNet, text refinement, domain cache) is trained with SGD. Clarify that *test-time adaptation* is gradient-free, not the overall method.
- **Table 3 index ordering is confusing.** The indexing (Index 1→2, 2→3, 3→4, 4→5, 5→6, 7→8) jumps between component additions, making it hard to follow cumulative contributions at a glance.

**Nice-to-Haves:**
- Analysis of what CPNet actually learns versus what CLIP already captures (e.g., feature similarity or attention visualization) would strengthen the "complementary learning" claim.
- Ablation comparing L2C against a version of VDPG augmented with text features would help disentangle the sources of improvement.

**Removed Points:**
- *Criticism about missing comparisons with prompt-based methods (CoOp, CoCoOp, ProDA).* The paper explicitly references these comparisons (line 166): "we further compare with prompt-based methods: CoOp, CoCoOp and side branch-based DTL." Results are in the appendix (stripped by parser), so this criticism is invalid.
- *Claim that "gradient-free" is a factual error.* The test-time adaptation phase is gradient-free — no gradients flow through any component at inference. The phrase could be more precise, but it is not false.

**Novel Insights:** None beyond the paper's own contributions.

**Suggestions:**
1. Add a controlled comparison isolating CPNet's contribution from text features. At minimum, compare against VDPG augmented with the same text features (if feasible), or explicitly acknowledge the confound and reframe the contribution as a multimodal adaptation system rather than solely attributing gains to input-space learning.
2. Report results with variance estimates (at least 3 runs).
3. Add a brief complexity table (parameters, FLOPs, wall-clock time).
4. Clarify "gradient-free" to specify test-time adaptation.

**Score and Decision:** The paper presents a well-engineered system with strong empirical results and thorough component-level validation. The main weakness is a confound in attributing improvements to the claimed core contribution, but the overall contribution (the full L2C pipeline) is clearly demonstrated and advances the state of the art. I recommend **Accept** with minor revisions.

Score: 7.0

Let me double-check my reasoning against all the rules.

1. ✓ REMOVE criticisms questioning existence/release of cited entities - No such criticisms.
2. ✓ REMOVE factually wrong criticisms - The "gradient-free" criticism is partly wrong; I moved it to Trivial and clarified why it's not false.
3. ✓ REMOVE unfair comparison criticism - Not applicable.
4. ✓ DO NOT mention missing related works - I didn't add any; I removed the critic's mention of missing CoOp/CoCoOp comparisons.
5. ✓ REMOVE formatting/style nitpicks - I kept only substantive issues.
6. ✓ REMOVE typos/grammar/etc. - None kept.
7. ✓ REMOVE reproducibility nitpicks - The cache size L is reasonable to mention since it's a key architectural parameter, not an implementation nitpick.
8. ✓ REMOVE strawman weaknesses - Checked.
9. ✓ REMOVE missing appendix content - The critic mentioned missing appendix comparisons; I removed those.
10. ✓ Filter Strength Finder - I kept only verified, substantive strengths.
11. ✓ FUNDAMENTAL ISSUES check - The confound is real but not fatal. The paper still shows clear improvements.
12. ✓ Paper type check - The paper is a method paper; I evaluated it as such.
13. ✓ Scope creep - I didn't add demands for broader coverage.
14. ✓ Inflated weaknesses - I downgraded the "gradient-free" from "false" (fatal-sounding) to Trivial.
15. ✓ Sentence-level pedantry - None kept.
16. ✓ Wishlist vs. core issues - The confound is a core issue, not a wishlist item.
17. ✓ Hidden severity - The critic's softened language hid nothing.
18. ✓ Methodological taste - I didn't penalize for using different methods than preferred.
19. ✓ Soft rules applied - I weakened the "gradient-free" criticism appropriately.

The score of 7.0 feels right - solid work with one real but not fatal weakness.

Actually, let me reconsider. The confound issue is quite central to the paper's narrative. If the paper's main claim is that "learning from input space is the key" but the evidence doesn't cleanly support this, it's a significant weakness. But the paper still makes four contributions (line 30), only one of which is CPNet. The text ensemble and domain-aware fusion are separate contributions. So the paper is still valuable.

Let me finalize the score at 6.5 to be more conservative. Actually, 7.0 is fine. The paper has strong empirical results and a well-validated system. The attribution issue is real but doesn't invalidate the contribution.

Final score: 7.0, Accept.Here is my consolidated final review after carefully cross-referencing all claims against the actual paper.

---

## Summary

This paper addresses Few-Shot Test-Time Domain Adaptation (FSTT-DA) by introducing L2C (Learning to Complement), a framework that attaches a lightweight parallel network (CPNet) to learn dataset-specific visual features from the input space alongside frozen CLIP, combined with a greedy text ensemble for enhanced label semantics and domain-aware fusion that adapts both modalities toward unseen target domains. The method achieves strong empirical results on 5 large-scale benchmarks (WILDS and DomainNet), notably improving over prior work on weaker backbones like ViT-B/16 where VDPG struggles.

## Strengths

- **Strong and consistent empirical gains over prior methods.** L2C substantially outperforms VDPG and other baselines on 5 benchmarks, especially with ViT-B/16 (+5.1 F1 on iWildCam, +3.1% WC Acc on FMoW in Table 1; +1.4% average accuracy on DomainNet in Table 2). These are precisely the settings where the paper identifies existing methods as underperforming.
- **Clean ablation validates each component individually.** Table 3 shows that CPNet alone improves over zero-shot CLIP (+13.1 F1 on iWildCam), revert attention adds further gains (Index 4 vs. 5), and text/greedy components incrementally improve. The domain information aggregation (Table 5) and domain prompt (Table 4) ablations are similarly informative.
- **Efficient and black-box compatible design.** CPNet uses only 3 transformer blocks for ViT-B/16 on DomainNet (Section 4.1); the text encoder is discarded as a preprocessing step costing <0.01% of total training cost (Section 4.2); CLIP remains frozen and unmodified throughout, making deployment possible without accessing CLIP's internal weights.

## Weaknesses

### Fatal
None.

### Major

- **Confounded attribution of gains over VDPG.** The paper's central narrative positions "learning from the input space" via CPNet as the key departure from VDPG (Abstract: "Departing from the state-of-the-art of inheriting the intrinsic OOD capability of CLIP, this work introduces learning directly on the input space"). However, L2C simultaneously adds text features (greedy ensemble + refinement + cross-modal fusion in DAF) that VDPG entirely lacks — VDPG is explicitly described as "vision-only encoder" (Section 1). The main results (Tables 1, 2) therefore compare a vision+text pipeline against a vision-only one, so the reported gains cannot be cleanly attributed to input-space learning versus the addition of text modality.

  The ablation (Table 3, Index 1 vs. 2) shows CPNet improves over zero-shot CLIP, but zero-shot CLIP is not VDPG (which itself uses source-domain training). A comparison isolating CPNet's contribution against a controlled baseline that also uses text features (or a vision-only L2C variant vs. VDPG) is missing. While the requested "vision-only L2C" ablation is nontrivial (removing text features would also require replacing the CLIP contrastive loss), the attribution question remains unresolved and undermines the paper's headline claim. The contribution is better framed as a *multimodal adaptation pipeline* whose individual components are each validated, rather than attributing gains specifically to input-space learning.

### Minor

- **No statistical variance reported.** Main results and ablations lack standard deviations or confidence intervals across multiple runs or few-shot draws. Given variability in domain splits and few-shot sampling, this limits reliability assessment. The broader FSTT-DA literature often reports single runs, but given the complexity of the pipeline, at least 3 runs on key results would strengthen the claims.
- **Computational overhead not quantified.** The paper claims the method is "lightweight" but provides no FLOPs, parameter counts, or inference-time latency compared to baselines. CPNet's depth is given for DomainNet (3 layers), but depths used for reported results on other datasets (Fig. 4 shows a sweep) are not stated in the main text. A brief complexity table would substantiate the efficiency claims.
- **Domain cache size L not specified.** The cache is a key architectural component (Eq. 5: K∈ℝ^{L×d}, V∈ℝ^{L×d}), but its value is not mentioned in the main text. Sensitivity analysis is deferred to the (stripped) appendix.

### Trivial

- **"Gradient-free" phrasing is imprecise.** The Related Work section states: "Our work introduces a practical, gradient-free adaptation method, enabling model deployment in black-box environments." At test-time, adaptation indeed requires no gradients (domain prompt generation uses only forward passes through CPNet and cache queries). However, the training pipeline (CPNet, text refinement, domain cache) is trained with SGD. The claim should specify that *test-time adaptation* is gradient-free — as currently worded, it risks confusing readers.
- **Table 3 index ordering is hard to follow.** The ablation references jump between Index 1→2, 2→3, 3→4, 4→5, 5→6, 7→8, making it difficult to track cumulative contributions without constantly referring back to the table.

## Nice-to-Haves

- An analysis of what CPNet actually learns versus what CLIP already captures (e.g., feature similarity maps or attention visualizations) would substantiate the "complementary" claim beyond the revert attention formulation.
- A comparison against VDPG augmented with text features (if feasible to construct) would directly disentangle the source of improvement.

## Removed Points

*These points were flagged during review and are removed with justification.*

- **Criticism about missing comparisons with prompt-based methods (CoOp, CoCoOp, DTL).** The paper explicitly states (line 166): "we further compare with prompt-based methods: CoOp, CoCoOp and side branch-based DTL." These results exist in the appendix, which was stripped by the parser. The criticism is invalid.
- **Claim that "gradient-free" is factually false.** As noted above, the test-time adaptation phase genuinely requires no gradient computation — the critique overstates the issue. The point is retained at Trivial severity for precision, not because the claim is false.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Resolve the attribution confound.** Either (a) add a comparison against a version of VDPG that also uses the text features, (b) construct a vision-only L2C variant (using a classification head instead of CLIP contrastive loss) and compare against VDPG, or (c) honestly reframe the contribution as a multimodal adaptation pipeline and de-emphasize the "input-space learning" attribution claim. The current gap between narrative and evidence will be the first thing sharp readers notice.
2. Add variance estimates for key results (at least 3 runs).
3. Include a brief complexity table (parameters, FLOPs, wall-clock time) to support efficiency claims.
4. Specify typical cache size L and per-dataset CPNet depths in the main text.
5. Rephrase "gradient-free" to clarify that it applies to test-time adaptation.

## Score and Decision

The paper presents a well-engineered, empirically validated system that advances the state of the art on challenging FSTT-DA benchmarks. The individual components are sensibly designed and cleanly ablated. The primary weakness is a mismatch between the central narrative (attributing gains to input-space learning via CPNet) and the experimental design (which introduces text modality simultaneously, confounding attribution). This weakens but does not invalidate the contribution — the full pipeline clearly works and the component-level ablations are credible.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>