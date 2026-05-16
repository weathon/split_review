Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper proposes TempMe, a progressive multi-granularity token-merging framework for efficient text-video retrieval. The key idea is to reduce temporal redundancy by first merging spatial tokens within frames (ImgMe) and then progressively merging tokens across frames/clips (ClipMe) via a clip aggregation hierarchy. The method is designed as a drop-in module compatible with both parameter-efficient (LoRA-based) and full fine-tuning setups. Experiments on four benchmarks (MSRVTT, ActivityNet, DiDeMo, LSMDC) show that TempMe reduces GFLOPs by 35–51% and output tokens by 84–95% while improving retrieval accuracy over baselines like LoRA and ToMe by 4–8 R-Sum points.

## Strengths

1. **Novel and well-motivated approach to a real problem.** The paper identifies temporal redundancy across video frames as a source of inefficiency that existing token compression methods (designed for single images) fail to address. The progressive multi-granularity merging framework — starting from within-frame merging (ImgMe) and escalating to cross-frame clip merging (ClipMe) — is a clean architectural response to this observation.

2. **Large and consistent efficiency–accuracy gains.** On MSRVTT with ViT-B/16, TempMe reduces output tokens to just **5%** (127 vs. 2364) and GFLOPs to **57%** (121.4 vs. 211.3) while improving R-Sum by 5.3 points over ToMe and 5.3 points over LoRA (Table 1). These gains are consistent across B/32 and B/16 backbones and across all four benchmark datasets (Tables 1–2).

3. **Functional ablation disentangles temporal modeling from token reduction.** Table 5 cleanly separates the two functions: temporal modeling alone (cross-frame attention without merging) boosts R-Sum from 193.0 to 199.7; token reduction alone (merging without cross-frame attention) drops it to 188.8; their combination (TempMe) retains 198.6 R-Sum while cutting GFLOPs from 53.0 to 34.8. This decomposition confirms that the accuracy gain comes from enabling cross-frame spatiotemporal learning, while the merging provides the efficiency — together they achieve a Pareto-superior trade-off.

4. **Generalization to full fine-tuning.** Applied to CLIP4Clip, TempMe achieves a 7.9 R-Sum improvement (210.2 vs. 202.3), trains 1.57× faster, and uses 75% of the GPU memory (Table 4b). This demonstrates the method is not limited to parameter-efficient settings and that temporal redundancy is a general bottleneck.

5. **Qualitative visualization confirms the intended mechanism.** Figure 6 shows that TempMe merges semantically related regions (e.g., body parts of the same subject) across contiguous frames, while ToMe only merges within individual frames — directly illustrating the reduction of temporal redundancy.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims are supported by the evidence presented, and none of the weaknesses identified threaten the validity of the contribution.

### Minor

1. **The "Temporal Modeling" ablation variant is not clearly specified.** Table 5 reports a "Temporal Modeling" row (54.3 GFLOPs, 199.7 R-Sum) and a "Token Reduction" row (34.7 GFLOPs, 188.8 R-Sum), then TempMe combining both (34.8 GFLOPs, 198.6 R-Sum). The paper describes Temporal Modeling as "aggregat[ing] clips progressively to enhance spatio-temporal learning" and notes that "self-attention...in later layers [operates] on tokens across frames." This strongly implies Temporal Modeling is cross-frame attention without token merging — but it never states this explicitly. Since this ablation is central to validating the paper's mechanism claim, the exact setup (e.g., "concatenate all frame tokens, apply self-attention, no merging") should be stated in the ablation paragraph, not left to inference from GFLOPs. This is a clarity issue, not a missing experiment: the comparison the critic claims is absent actually exists in the paper.

2. **No per-layer efficiency breakdown is provided.** The paper reports final token counts (e.g., 1×97 for B/32) and overall GFLOPs, but the relationship between the two is nontrivial because merging is progressive — early layers process many tokens, later layers few. A per-layer plot or table of token counts and GFLOPs would clarify why the GFLOPs reduction (~35%) is smaller than the final token reduction (~84%) and would strengthen the efficiency analysis. (For context: this is fully consistent with progressive merging — early-layer costs dominate — but showing the breakdown would eliminate doubt.)

3. **The CLIP4Clip + TempMe full fine-tuning result lacks an architectural detail.** Table 4b shows CLIP4Clip$^\dag$ achieving 202.3 R-Sum and CLIP4Clip$^\dag$+TempMe achieving 210.2 R-Sum. CLIP4Clip has its own temporal aggregation module (e.g., sequential transformer). The paper should clarify whether TempMe *replaces* CLIP4Clip's temporal aggregation, *supplements* it, or whether the reimplementation uses a simpler aggregation. The +7.9 R-Sum gain is impressive either way, but readers need to know what is being compared.

4. **Temporal redundancy is not quantified.** The paper motivates temporal redundancy with a qualitative example (Figure 1a, a cat and monkey fighting) but provides no quantitative measure — e.g., average frame-wise CLIP feature similarity or token-level correspondence across consecutive frames. A simple analysis would ground the motivation and could help explain why certain datasets benefit more than others.

5. **ClipMe block placement within the backbone is deferred to the appendix.** The paper mentions that "with ViT-B/32 and 12 frames, the clip merging stage includes a total of 4 ClipMe blocks" only in an appendix reference. The mapping from backbone layers to merging stages should be specified in the main body for reproducibility.

6. **No comparison to a "single-shot" cross-frame merge baseline.** The paper's progressive multi-granularity claim implies that gradual merging is beneficial over merging all tokens at once. A comparison to a variant that performs one ClipMe block at the final layer with the same target token count would directly test this claim. The existing ablations (Table 4–5) already show the framework works, so this is not a critical gap, but it would strengthen the progressive claim.

### Trivial

None.

## Nice-to-Haves

- A comparison of similarity-based merging to random merging or uniform subsampling in the ClipMe stage, to verify that the bipartite soft matching captures meaningful cross-frame correspondences beyond what blind subsampling would achieve.
- Quantitative analysis of merge quality (e.g., measuring whether merged tokens correspond to the same semantic region across frames against annotations).
- A controlled comparison of VoP/DGL with *and without* prompt generation cost factored into GFLOPs, to make the accounting fully transparent (the paper already states the omission).

## Removed Points

The following points from the reviews are removed with justification:

- **"GFLOPs appear inconsistent with token reduction claims" (Critical Issue #2)**: This criticism assumes GFLOPs should scale linearly with output token count, ignoring that (a) transformers have both O(n²) self-attention and O(n) MLP costs, and (b) progressive merging means early layers still process near-full token sets. A 35% GFLOPs reduction despite 84% final token reduction is fully consistent with this architecture. The critic's rough calculation is incorrect.

- **"Comparison to VoP/DGL mixes incomparable inference costs" (Critical Issue #3)**: The paper explicitly states: "For fairness, prompt generation in VoP and DGL is omitted when evaluating throughput and complexity." This is transparent and, if anything, *favors* VoP/DGL by understating their true inference cost. The critic misread this passage.

- **"Improvement over ToMe is large and unexplained" framed as a critical flaw**: The ablation in Table 5 already provides the explanation. Temporal modeling (cross-frame attention) drives the accuracy gain; merging provides the efficiency. TempMe combines both. This is described in the ablation section. The critic's framing as "unexplained" is inaccurate, though the request for a single-shot merge baseline is reasonable and moved to Minor #6 / Nice-to-Haves.

- **"UMT experiments are tangential with mixed results"**: The UMT experiments demonstrate generalization to video foundation models and show TempMe achieving near-UMT accuracy at one-third the GFLOPs and training time — this is not tangential; it directly supports the generalization claim. Results are not "mixed": retrieval improves from 206.7 to 209.2; QA drops minimally from 44.9 to 44.6 (within noise) while cutting cost by 2/3.

- **"Missing ablation on merging strategy for ClipMe"**: The paper states "we thoroughly conduct an exhaustive analysis of the merging strategy" in the "More Ablation Analysis" section. The appendix (stripped by parser) contains this analysis.

## Novel Insights

The reviews surface one genuinely insightful observation: the paper's ablation reveals that the accuracy gain from TempMe comes primarily from enabling cross-frame *attention* (temporal modeling), not from the merging operation itself (which slightly hurts accuracy when applied alone). This is a nuanced finding that the paper partially acknowledges but does not fully emphasize. The combination works because cross-frame attention learns video-level features, while merging removes redundant tokens that would otherwise be wastefully processed — the two functions are complementary, not additive. This insight is actually a strength: the paper's design intentionally couples attention across frames with token reduction, and the ablation validates that both are needed. Future work in this area could further explore decoupling these functions or applying cross-frame attention more flexibly to improve the accuracy–efficiency frontier even further.

## Suggestions

1. In the Ablation Study (Section 4.4), explicitly state what the "Temporal Modeling" variant is — e.g., "cross-frame self-attention on the full token set without any token reduction." This would eliminate any ambiguity about what is being compared.
2. Add a per-layer token count or GFLOPs breakdown (as a figure or table) to clarify the efficiency story and explain the relationship between final token count and overall GFLOPs reduction.
3. In Table 4b, clarify whether TempMe replaces or supplements CLIP4Clip's temporal aggregation module.
4. Add a simple quantitative measure of temporal redundancy (e.g., average cosine similarity between consecutive frame token sets) to ground the motivation.
5. Move the ClipMe block placement specification (which layers use ClipMe vs. ImgMe) into the main body.

## Score and Decision

**Originality**: Good. The progressive multi-granularity framework for cross-frame token merging is a novel application of token compression to the video temporal domain.

**Importance of research question**: High. Efficient text-video retrieval is practically important as videos become the dominant media format and CLIP-based methods incur high inference costs.

**Claims well-supported**: Yes. The core claims (TempMe reduces complexity while maintaining or improving accuracy) are supported by extensive experiments and ablations across multiple datasets and settings. Some clarity issues in ablation descriptions are minor.

**Soundness of experiments**: Good. Four benchmarks, multiple backbones, both efficient and full fine-tuning, architectural and functional ablations. The experimental design is thorough.

**Clarity of writing**: Adequate but could be improved — the "Temporal Modeling" ablation description, ClipMe placement, and CLIP4Clip interaction details need clarification.

**Value to the research community**: High. The method is practical, achieves significant efficiency gains, and the code will be released. The progressive merging idea could generalize to other video tasks.

This is a solid paper with a clear contribution, strong empirical support, and only minor clarity issues. None of the concerns raised in the reviews threaten the paper's core claims after careful verification against the paper text.

**Score**: 8.0

**Decision**: Accept

MY FINAL SCORE: <pineapple>8.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>