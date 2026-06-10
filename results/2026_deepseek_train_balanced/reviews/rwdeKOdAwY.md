## Summary

This paper proposes RetFormer, a retrieval-augmented framework for long-tailed recognition and noisy-label learning. The key idea is to construct an external knowledge base of image-text pairs, retrieve nearest neighbors for each query image, and use a cross-attention module that fuses both image and text modalities from the retrieved samples to augment the classifier's predictions. The method is evaluated on CIFAR-100-LT, ImageNet-LT, and WebVision, achieving competitive results against prior retrieval-augmented methods.

## Strengths

- **Cross-modal retrieval fusion is genuinely shown to outperform image-only retrieval.** The ablation study (Table 4) directly compares the full RetFormer against variants that retrieve only images ("Ours w/o text") or only text ("Ours w/o image"). The full model outperforms both, providing concrete evidence that the cross-modal fusion — the paper's central architectural novelty — is responsible for gains beyond what single-modality retrieval methods like RAC and MAM achieve. This is the strongest piece of evidence supporting the paper's core claim.

- **Practical efficiency analysis of the retrieval system is useful.** Table 5 quantifies the speed/accuracy trade-off of approximate nearest-neighbor search (HNSW vs. exact k-NN), showing a 3× speedup with minimal accuracy loss. Section 3.2.4 provides explicit time and spatial complexity estimates (O(log N) query time, ~30GB for ImageNet-LT). This goes beyond what comparable retrieval-augmented vision papers typically report, making the engineering trade-offs transparent.

- **Awareness and documentation of data leakage risks is a methodological strength.** The paper explicitly avoids ImageNet-21K pre-trained weights for CIFAR-100-LT experiments due to class overlap (Table 1 caption, Section 4.1), and replaces the text embedding of the query image itself with a zero vector in the cross-attention module (Section 3.2.2) to prevent trivial self-retrieval leakage. This careful documentation is above the norm for this area.

## Weaknesses

### Major

- **The knowledge base configuration used for each main result is not specified.** Section 3.2.3 describes three KB options (Downstream dataset only, DataComp subset, or "All" combining both), and Figure 4 (right) shows their ablation. However, the main results tables (Tables 1, 2, 3) never state which configuration was used. Since the "Downstream" and "All" configurations include the training set itself, the KB could in principle provide the model with multiple views of training samples that competing methods lack. While prior work such as RAC also uses the training set as a retrieval source (making this less unusual than the critic suggests), the paper must specify the KB for each result. The authors should also report the main results with a purely external KB (e.g., DataComp-only) to cleanly separate the contribution of genuinely external knowledge from within-training-set retrieval.

- **The "theoretical perspective" is overstated.** Contribution (4) claims to provide "an intuitive explanation... from a theoretical perspective based on gradient propagation." Section 3.2.5 shows that the retrieval module introduces gradient terms ∂Lᵢ/∂x₀ from retrieved samples, and concludes this acts like virtual data augmentation. This is an architectural observation — a straightforward consequence of the chain rule — not a theoretical analysis. There are no formal statements, convergence guarantees, or testable predictions. The paper itself uses the word "intuitive" (twice) to describe this section. Framing it as "theoretical" overstates what is provided. Present it clearly as an intuitive explanation.

### Minor

- **Potential overlap between CLIP pre-training data and the knowledge base is not discussed.** The vision encoder is initialized with CLIP pre-trained on DataComp-1B (Section 4.1), while the KB uses "the subset of DataComp... comprised of 1.4B samples" (Section 3.2.3). The paper does not address whether this subset is disjoint from the DataComp-1B data used to train CLIP. Since the encoder is frozen, this does not create training leakage, but it does affect how the retrieval results should be interpreted. A brief discussion or an experiment with a provably disjoint KB would address this cleanly.

- **No variance or confidence intervals reported for any result.** All tables report single-run accuracy. Given the stochasticity in both k-NN retrieval (the retrieved set varies with initialization choices) and training (random augmentations, Mixup, label smoothing), this makes it impossible to assess whether reported margins over baselines are statistically significant. Reporting at least 3-run means with standard deviations is standard for this class of experiments.

- **The computational cost of building the 1.4B-sample KB index is not reported.** The paper claims RetFormer operates "without incurring significant computational overhead" (Contribution 2) and provides useful complexity analysis for query-time (Section 3.2.4). However, the one-time cost of pre-computing CLIP embeddings for 1.4B image-text pairs and building the HNSW index is a substantial engineering undertaking. Reporting GPU-hours, wall-clock time, and storage for this pre-processing step would give readers a realistic picture of the total resource footprint.

### Trivial

- In Section 3.2.5, the notation for the gradient sum uses `:=` which is non-standard — this should be `=` (the derivative on the left is exactly the sum of terms on the right by the chain rule, not a definitional assignment).

## Nice-to-Haves

- The WebVision evaluation follows the "mini" setting (50 classes out of 1000), which is standard in prior work on this dataset. Extending to the full 1000-class setting would increase confidence in the method's scalability.
- The cross-attention module output is a tuple of two matrices (image and text). The paper could clarify how this tuple is consumed by the classifier `h(⋅)` — whether both branches are concatenated, summed, or otherwise combined before the final classification layer.

## Removed Points

These points from the reviewers were flagged to be removed; treat them with caution:

- **"The ablation does not isolate the marginal benefit of retrieval"** — REMOVED. The paper's ablation (Table 4) does include a "CLIP full FT" baseline, which is precisely fine-tuning the same CLIP ViT-B/16 backbone under the same protocol without retrieval. The gap between CLIP full FT and the full RetFormer is the marginal benefit. The Harsh Critic's demand to move this into the main comparison tables alongside published SOTA methods is not standard practice; the ablation section is the correct location for this controlled comparison.

- **"The scale of the knowledge base undermines the claimed motivation"** — REMOVED. The paper's motivation is about model parameters (increasing parameters vs. using external retrieval), not about eliminating all resource costs. The paper provides explicit complexity analysis (Section 3.2.4) including storage and query time. Shifting the resource burden from model parameters to an external store is a legitimate architectural trade-off, not a contradiction of the stated motivation.

- **"The WebVision mini setting is a weak test"** — REMOVED. The 50-class "mini" setting is the standard benchmark used by prior work on WebVision for noisy-label learning. Demanding the full 1000-class setting is scope creep beyond what the paper's comparison targets require.

- **Strength from Strength Finder about "gradient-based theoretical framework grounded in optimization theory"** — REMOVED. As noted in the Weaknesses section, the gradient analysis is an intuitive architectural observation, not a theoretical framework. Keeping this strength would conflict with the verified weakness about the overclaimed theoretical contribution.

- **"The introduction discusses LLMs at length, which is tangential"** — REMOVED. This is a formatting/rhetorical choice, not a substantive weakness.

- **"Garbled text at line 51 with missing variables"** — REMOVED. This is a parser artifact from PDF extraction, not present in the original submission.

- **"Missing related works"** — REMOVED per instructions (cannot confirm existence of external sources).

- **"Code release concern"** — REMOVED per instructions (reproducibility concerns about unreleased artifacts should not be counted).

## Novel Insights

None beyond the paper's own contributions. The two reviews essentially converge on the same picture: the core idea (multimodal retrieval via cross-attention) is sensible and supported by ablation evidence, but the paper's reporting is missing a critical detail (which KB for each result) and overplays the theoretical framing of the gradient analysis. No novel synthesis emerges beyond what the paper states and what the weaknesses clarify.

## Suggestions

1. **Explicitly state which KB configuration was used for each main result.** Preferably run the main tables with a clean DataComp-only KB (excluding the downstream dataset) and report those as the primary results, with the "All" KB as an ablation showing the effect of adding the training set. This would cleanly address the confound concern.

2. **Rephrase Contribution (4) as an intuitive explanation** rather than a "theoretical perspective." The gradient flow observation is useful for intuition but does not constitute theory.

3. **Add a brief discussion** of whether the DataComp subset used for the KB is disjoint from the DataComp-1B data used for CLIP pre-training, and if it is not, discuss whether this affects interpretation.

4. **Report means and standard deviations** across at least 3 runs for the main results.

## Score and Decision

The paper presents a reasonable method (multimodal retrieval augmentation for long-tail/noisy-label tasks) with solid experimental support for its core architectural claim (cross-modal > image-only retrieval). The ablation evidence is the paper's strongest asset. However, the unclear KB specification for main results is a non-trivial reporting gap that prevents the reader from fully assessing the claims, and the "theoretical" overclaim weakens the paper's credibility on closer inspection. These issues are addressable in revision but detract from the paper in its current form.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>