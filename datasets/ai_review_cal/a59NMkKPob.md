- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5
Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes DRL (Discriminative Representation Learning), a non-rehearsal class incremental learning method built on frozen pre-trained ViT. DRL consists of two components: (1) an Incremental Parallel Adapter (IPA) that adds lightweight per-stage adapters with a learnable transfer gate to selectively inherit features from the previous stage, and (2) a Margin-CE loss that introduces a logit anchor *k* to push positive/negative logits apart, aiming to narrow the gap between stage-wise training and global inference. Experiments on six benchmarks show consistent SOTA performance, and the method is extremely parameter-efficient (0.6% trainable parameters per new stage).

## Strengths

1. **Consistent SOTA across six diverse benchmarks (Table 1, Table 2).** DRL outperforms all compared methods on every dataset. With ViT-B/16-IN21K, it achieves +3.45% on ImageNet-A, +2.12% on VTAB, and +1.85% on ObjectNet over the prior best method EASE. The advantage holds with a different backbone (ViT-B/16-IN1K) as well (+2.37% on ObjNet, +3.68% on ImageNet-A).

2. **Extreme parameter efficiency (Section 3.2, Figure 2).** IPA adds only 0.6% trainable parameters per stage relative to the ViT-B/16 backbone, and inference uses only (1+0.006t)B parameters versus tB for EASE or (t+1)B for DER. This directly supports the claimed efficiency advantage.

3. **Margin-CE loss generalizes to other methods (Table 5).** Plugging Margin-CE into three representative CIL methods (APER, ESN, EASE) consistently boosts performance. For example, EASE's average accuracy on ImageNet-A rises from 65.34% to 66.80% (+1.46%), demonstrating that the loss is transferable and not tied to the IPA architecture.

4. **Component-wise ablation isolates contributions (Table 3).** The paper separately evaluates IPA architecture (comparing IPA+CE vs. Baseline+CE) and Margin-CE loss (comparing DRL vs. IPA+CE+KD). IPA alone contributes a meaningful gain (e.g., IPA+CE at 65.83% vs. Baseline+CE at 64.19% on ImageNet-A, a +1.64% improvement), and Margin-CE adds a further +1.45% improvement.

5. **t-SNE visualizations support the discriminative claim (Figures 5–8).** The visualizations compare DRL with and without Margin-CE, showing tighter intra-class clustering and clearer inter-class separation in the full DRL model.

## Weaknesses

### Fatal
None.

### Major

1. **No statistical significance or variance reporting.** All results are reported as single numbers without standard deviations, confidence intervals, or multi-seed trials. Given that the reported improvements over the closest competitor EASE range from ~1.5% to ~3.5% (Table 1), plausible run-to-run variance could meaningfully affect these margins. This is particularly relevant for the ablation results — the claimed +1.45% improvement from Margin-CE (Table 3) and the generalization improvements (Table 5) need to be assessed with uncertainty. The paper should report results over at least 3 random seeds with standard deviations.

2. **Margin-CE loss is not compared against existing margin-based losses.** The proposed loss (anchor-based push of positive/negative logits) is a departure from standard margin-based softmax losses (e.g., ArcFace, CosFace, additive margin softmax), which work by modifying the softmax itself to enforce angular margins. The paper does not compare against any such standard margin loss within the same IPA pipeline. Since the core claim is that the *margin mechanism* improves discriminability, a comparison against a well-established margin loss (e.g., CosFace with tuned margin *m*) is necessary to determine whether the improvement stems from the specific anchor formulation or simply from any loss that pushes positive/negative logits apart. This would strengthen the paper's contribution claim.

### Minor

3. **Attention matrix reuse (Aᵉ = Aᵒ) is not ablated.** A core design choice in IPA is reusing the PTM's attention matrix Aᵒ instead of learning a new one for the adapter sub-network. This removes the Q,K computation, saving parameters. The paper asserts this is "without losing the plasticity" but provides no ablation comparing learned vs. fixed attention. Given that this design decision affects both efficiency and plasticity, a comparison (e.g., learned Aᵉ with bottleneck Q,K layers vs. fixed Aᵒ) would be informative.

4. **The claimed "smooth representation shift" is not directly measured.** The paper motivates the transfer gate by arguing it addresses "non-smooth representation shift" between stages, but the evaluation only reports overall accuracy. The paper would benefit from directly measuring feature drift (e.g., CKA similarity or cosine distance between class centers across stages) with and without the transfer gate, to validate whether the gate actually produces smoother shifts.

5. **The iCaRL baseline included in non-rehearsal evaluation is uninformative.** Table 1 and its caption state "All methods are implemented without using exemplars," which includes iCaRL — a method whose core design relies on exemplar memory. Running iCaRL without exemplars produces a version never intended to work under these conditions. While this is transparent and does not inflate results (the paper's main competitors are clearly EASE, APER, and other PTM-based methods), it is an odd inclusion that adds little. The paper should either remove iCaRL from this table or add a note clarifying the setting mismatch.

### Trivial

6. **Ambiguous scope of the sum in p^{neg} (Eq. 7).** The term "∑_{j,j≠i}^{C} e^{z_j}" does not explicitly specify whether C ranges over current-stage classes or all seen classes. From context, it is current-stage classes (since only those are available during training), but this should be stated explicitly.

## Nice-to-Haves

- Adding a comparison against a standard margin-based loss (e.g., CosFace) in the same IPA pipeline would strengthen the novelty claim of Margin-CE.
- The "semantic-guided prototype complement strategy" used during inference is deferred entirely to the supplementary. A brief summary in the main paper (even a sentence or equation) would improve self-containedness.
- A plot of accuracy vs. total parameters across stages (cumulative overhead) would better illustrate the efficiency advantage over EASE and DER over long task sequences.

## Removed Points

The following points from the reviewers are excluded or reformulated:
- *"IPA contributes only +0.32%"* — The reviewer compared IPA+CE+KD (64.10%) vs Baseline+CE+KD (63.78%). This comparison is confounded by KD hurting both baselines. The fair comparison for isolating IPA's contribution is IPA+CE (65.83%) vs Baseline+CE (64.19%), which yields +1.64%. The paper transparently provides both comparisons.
- *"Low epochs (20) compared to baselines"* — Speculative. No evidence is provided that baselines use more epochs. The paper states all methods use the same PTM initialization.
- *"Semantic-guided prototype complement strategy is unreviewable"* — This detail is in the supplementary (stripped by the parser), which is standard practice.
- *"Margin-CE loss ambiguity about training-inference inconsistency mismatch"* — The critic claimed a "mismatch" between using only current-stage negatives during training and global inference. This is the *very problem* Margin-CE is designed to address; describing it as a flaw misreads the paper's motivation.

## Novel Insights

None beyond the paper's own contributions. The combination of parallel adapter with transfer gate for stability-plasticity trade-off and an anchor-based margin loss for training-inference consistency is well-motivated, and the empirical evidence across six benchmarks is consistent. The most interesting finding for practitioners is that Margin-CE — which is a simple drop-in replacement for standard CE — provides consistent gains across three completely different CIL methods (Table 5), suggesting it is a generally useful technique beyond the specific IPA architecture.

## Suggestions

1. **Add multi-seed results** (at least 3 seeds with standard deviations) to all main tables — the comparisons and ablations are too tight to evaluate without variance.
2. **Add an ablation comparing Margin-CE against a standard margin loss** (e.g., CosFace with tuned margin m) in the IPA pipeline to justify the novel formulation.
3. **Add an ablation comparing learned attention (Aᵉ learned) vs. fixed attention (Aᵉ = Aᵒ)** in the adapter sub-network.
4. **Remove iCaRL from the non-rehearsal comparison table** or add a clarifying footnote.
5. **Clarify the scope of C in Eq. 7** and add a brief description of the semantic-guided prototype complement strategy in the main paper.
6. **Directly measure representation shift** (e.g., CKA similarity) with and without the transfer gate to validate the smooth-shift claim.
