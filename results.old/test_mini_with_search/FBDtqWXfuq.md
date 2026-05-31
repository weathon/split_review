Now I have sufficient anchor comparisons. Let me write the final review.

**Round 1 bracket (initial):** I placed the paper between 4.5 and 7.0, guided by the observation that it was clearly stronger than the ~3.0-4.5 multi-modal FL papers but weaker than Co-LoRA (7.00).

**Round 2 narrowing:** I queried inside [4.5, 6.5] and [5.5, 7.5]. The 5.0-5.5 anchors (Feroma, Bridging Generalization Gap, HyperFedZero, RESFL) are all accepted posters with novel methods but clear limitations—comparable quality to FedCola. Co-LoRA (7.00) is stronger (40-task benchmark, broader evaluation). Papers at 4.0-4.57 (UniFLoW, BoMM, TAP, pFedMMA) all have weaker contributions or more serious issues.

**Final score:** 5.5. This paper makes a genuinely novel contribution (defining MCFL) and has a well-structured methodology. Its weaknesses (no variance reporting, underspecified text embedding pipeline) are real but addressable and do not undermine the core contribution.

---

## Summary

This paper introduces a novel federated learning setting called Modality-Collaborated Federated Learning (MCFL), where each client holds data of only one modality and collaboration occurs via parameter-sharing rather than requiring multi-modal clients or aligned data. The authors propose FedCola, a framework based on a modality-agnostic transformer (ViT-Small) that systematically addresses three design questions: which parameters to share across modalities (attention layers only), how to aggregate with modality compensation (aligning layer-level training sample counts), and temporal modality arrangement (warm-up on one modality). Experiments on vision+language datasets (CIFAR-100/AGNEWS and OrganAMNIST/MTSamples) show consistent improvements over Uni-FedAVG and CreamFL baselines across 12 FL scenarios.

## Strengths

1. **Novel, well-motivated problem setting (MCFL).** The paper clearly distinguishes MCFL from prior FMML work (Figure 1, Section 1) and makes a compelling case that eliminating the requirement for multi-modal clients is practically important. The problem definition in Section 2 formalizes this setting precisely, specifying the objective, parameter decomposition, and evaluation metric.

2. **Systematic empirical investigation of three design dimensions.** The paper poses RQ1–RQ3 (Section 5) and conducts targeted experiments for each: parameter-sharing strategies (Table 1), aggregation with modality compensation (Figure 5), and temporal modality arrangement (Table 3). The finding that attention-sharing recovers vision accuracy from 3.58% to 56.17% (Table 1) is supported by head-to-head comparisons against sharing all, sharing none, sharing only FFN, and uni-modal attention variants.

3. **Consistent performance gains over strong baselines.** FedCola outperforms both Uni-FedAVG (standard uni-modal baseline) and CreamFL (prior state-of-the-art) across all 12 reported FL scenarios (Table 4), with improvements over CreamFL up to 8.58% in average accuracy.

4. **Resource efficiency without additional computation or communication.** FedCola maintains the same computation and communication costs as Uni-FedAVG, while CreamFL requires 1.97× computation (Figure 6). Modality warm-up further reduces resource costs. This is a practical advantage over methods requiring public datasets or feature extraction.

5. **Clean ablation isolating each component's contribution.** Table 5 shows attention sharing provides the largest gain (45.76% → 72.92%), while modality compensation and warm-up add marginal but consistent improvements. The compensation effect is larger under imbalanced data (71.41% → 73.01%), validating its purpose.

6. **Direct verification that cross-modal collaboration occurs.** Figure 7 shows a positive correlation between one modality's model capacity and the other modality's performance, providing evidence beyond aggregate accuracy that the framework leverages out-of-modality knowledge.

## Weaknesses

### Fatal
None.

### Major

1. **No variance reporting across runs.** Table 4 reports results for all 12 FL scenarios with no standard deviations, confidence intervals, or multiple runs. Federated learning results are known to vary substantially with client sampling, data partitioning, and random seeds. Without knowing whether improvements (e.g., +2.4% average accuracy on CIFAR-100/AGNEWS) are stable, the claim that FedCola "significantly outperforms" baselines is under-supported. The ablation study (Table 5) and warm-up comparison (Table 3) also lack variance. This is the single highest-leverage improvement the authors should make.

### Minor

2. **Text-to-ViT embedding pipeline is underspecified.** The paper states "texts are embedded with a BERT tokenizer" (line 182) and then "fed into a ViT-Small." It does not specify how tokenized BERT outputs are projected into the ViT's patch embedding space (e.g., linear projection of [CLS], per-token embeddings mapped to patches, or learned projections). This is a genuine reproducibility gap that must be addressed for independent implementation and validation.

3. **Theoretical grounding for modality compensation is superficial.** The paper invokes Rademacher complexity (line 128) as a motivation for layer-level misalignment, then proposes modality compensation (copying missing weights from the previous round). The connection between the complexity argument and the proposed fix is not formally established—the claim that "aggregation with modality compensation will have the same layer-level alignment as applying FedAVG for all parameters" is stated without proof (the footnote reference is a parser artifact). The empirical gain from compensation is small (0.5–1.6%), and while the mechanism is intuitive, the paper would benefit from a more rigorous analysis.

### Trivial

4. **Pre-trained initialization control is not fully explicit.** The paper states "all methods use the same model architecture" (line 184) and employs a pre-trained ViT-Small. It does not explicitly state that all baselines also initialize from the *same pre-trained checkpoint*. Given that this is standard practice when "the same model architecture" is specified, this is a clarification rather than a flaw, but it should be stated unambiguously.

## Nice-to-Haves

- **Deeper study of data imbalance with modality compensation.** The paper shows compensation helps more under imbalanced data (Table 5, 71.41% → 73.01%). A systematic study varying the imbalance ratio would strengthen the case that compensation genuinely addresses misalignment rather than being a negligible tweak.
- **Limitations paragraph.** The paper acknowledges extension to more modalities as future work but does not discuss potential challenges (e.g., increased communication cost with multiple warm-up stages, modality-specific optimization conflicts, scalability of the compensation mechanism).

## Removed Points

- **Missing hyperparameter details (learning rate, optimizer, batch size, warm-up lengths).** These details are typically in the appendix, which the parser strips from all papers. Not a valid criticism.
- **Missing footnote about alignment proof.** The superscript "1" (line 132) referencing additional justification is a parser artifact; footnotes in the original PDF were stripped.
- **Claim that CreamFL's poor performance is "expected" and should be acknowledged more.** The paper already provides context for CreamFL's degraded performance in MCFL (absence of multi-modal clients for direct feature alignment, Section 6.2).
- **Criticism that only two modalities are studied.** The paper explicitly scopes to vision+language as "the most popular modalities" and acknowledges extension as future work. This is within scope.
- **Various section-by-section presentational observations** (e.g., "the objective should be justified," "the paper could better quantify resource reduction"). These are either already addressed or reflect reviewer framing preferences, not substantive flaws.
- **Strength Finder strengths about the problem being "important" or the paper "addressing an important problem."** These are generic and lack specific evidence from the paper. Dropped.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Report mean ± std over at least 3 independent runs** for all main tables (Tables 3, 4, 5). This single change would substantially strengthen the paper's credibility.
2. **Specify the text embedding pipeline** in sufficient detail: how BERT tokenizer outputs are converted to the input format expected by ViT-Small (dimensionality, projection layer, any learned embeddings).
3. **Explicitly state** that all baselines use the same pre-trained ViT-Small checkpoint, so the comparison cleanly attributes FedCola's gains to its collaboration mechanisms rather than initialization.
4. **Add a brief limitations discussion** covering potential challenges with more than two modalities and scenarios where modality collaboration might not help.

## Score and Decision

**Round 1 bracket:** [4.5, 7.0] — based on comparisons to low-band (2-3) and mid-band (4-4.57) multi-modal FL papers.

**Round 2 anchor comparisons:**
- Co-LoRA (7.00) — Stronger; broader evaluation with 40 tasks, benchmark contribution.
- HyperFedZero (5.50) — Comparable; similar quality, accepted poster.
- Feroma (5.50) — Comparable; similarly clear contribution with some presentation gaps.
- Bridging Generalization Gap (5.50) — Comparable; accepted poster with novel method and limitations.
- RESFL (5.00) — Slightly weaker; accepted poster with clear trade-off analysis.
- BoMM (4.50) — Weaker; hollow motivation, incomplete baselines.
- We Generate What You Need (5.00) — Comparable; accepted but rejected.

**Final score relative to anchors:** FedCola is stronger than the 4.0-4.5 papers (UniFLoW, BoMM, TAP) due to its genuinely novel MCFL setting and cleaner methodology. It is comparable to the 5.0-5.5 papers (Feroma, HyperFedZero) which also have clear contributions and addressable limitations. It is weaker than Co-LoRA (7.00), which has substantially broader evaluation and an additional benchmark contribution. I place the paper at **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>