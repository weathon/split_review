Now I have robust calibration context. Let me construct the final review.

## Summary

This paper proposes OML, a brain-inspired hierarchical modular neural network for online multimodal learning. The architecture uses ascending/descending/lateral pathways between feature neurons (FN), unimodal association neurons (UAN), and multimodal association neurons (MAN) to learn multimodal associations incrementally. Key novel components include: (1) a reference extraction algorithm using coefficient-of-variation to identify which feature dimensions a word refers to (e.g., color vs. shape), (2) conflict detection and question-generation mechanism for human-in-the-loop interaction, and (3) frequency-based signal routing (via Fourier transforms) to enable cross-modal activation. Experiments on small fruit and home-object datasets with hand-crafted features are reported across three settings (baseline, precise referring, and modal extension), comparing against five offline and two online methods.

## Strengths

1. **Precise reference extraction is a genuine novel contribution (Sec 3.4, Fig 3a, Eq 7, Table 2).** The coefficient-of-variation method that automatically identifies which feature dimensions a word refers to is technically novel and clearly demonstrated. In Table 2, when color-referring words are added to the dataset, offline methods drop significantly (e.g., DAE from 67.0→60.7, NRCH from 92.3→81.6) while OML maintains 87.3% V→A on E-Fruits close. Prior online methods (ART, AEN) cannot distinguish name words from attribute words — the paper provides a concrete mechanism and shows it works.

2. **Demonstrated stability against catastrophic forgetting in open environments (Table 1, Open rows).** OML is the only method whose accuracy stays stable or improves when trained incrementally on disjoint subsets. For Fruits V→A open, OML achieves 89.8% while the best offline method (NRCH) drops to 86.5% from 92.3% in the close setting. This directly supports the continuous-learning claim.

3. **Novel hierarchical modular architecture (Sec 3, Fig 2).** The three-layer structure (FN→UAN→MAN) with ascending, descending, and lateral pathways, combined with Fourier-based signal routing for cross-modal activation (Eq 6), provides a principled architectural framework that is distinct from standard joint or coordinated representation approaches. The frequency-based λ parameter for routing signals across modalities (used in the modal extension experiment, Table 3) is a specific, testable design choice.

4. **Comprehensive evaluation across multiple experimental settings.** The paper tests three distinct capabilities — baseline cross-modal recall (Table 1), precise referring under attribute-word interference (Table 2), and modal extension to a novel taste channel (Table 3) — covering close and open environments in each case. This goes beyond single-setting evaluations common in this sub-area.

## Weaknesses

### Fatal

None.

### Major

1. **No ablation or sensitivity analysis for a complex architecture.** OML has many interacting components: multiple neuron types with different activation modes (OIAM/ODAM), lateral connections with threshold 2θ, Fourier transform for signal routing (Eq 6), reference extraction with threshold r=0.5 (Eq 7), descending Gaussian probability threshold ϑ=0.8 (Eq 2), and four distinct learning scenarios (Sec 3.5). The paper sets all hyperparameters to fixed values without any ablation study. It is impossible to determine which components drive performance — whether gains come from the novel reference extraction, the frequency routing, the lateral pathways, or simply from the incremental neuron-creation mechanism. This is the most significant gap given the architectural complexity.

2. **Conflict detection and human-interaction claims are not rigorously evaluated.** The paper states "when we randomly add 10% of word-image or word-taste data pairs with incorrect matches, OML is able to detect all conflicts and raise appropriate questions" (Sec 4.1 point 3), but provides no precision, recall, or F1 metrics for conflict detection, no baseline comparison, and no characterization of false positives/negatives. Additionally, "if the question posed to the user by OLM remains unanswered for a certain period of time, we set the answer to be positive" (end of Sec 4) — meaning the human-in-the-loop interaction is simulated with uniformly positive answers, so there is no evidence that the learned network actually benefits from real interactive feedback. This is a core claimed capability that remains unvalidated.

### Minor

1. **Small, hand-crafted datasets.** Experiments use Fruits (fruit images + uttered Chinese names) and HomeF (home objects), with visual features being Fourier descriptors of object boundaries and mean color values — not raw pixels or modern embeddings. This is far from modern multimodal benchmarks (Flickr30K, MS-COCO, Conceptual Captions) and limits the conclusiveness of claims that the method "learns like the way humans do."

2. **No variance or statistical significance reported.** All tables report single accuracy numbers. Given the small dataset sizes and the stochastic nature of online learning (random sample order, neuron creation), results could be highly variable. Confidence intervals or multiple-run statistics are needed.

3. **Limited online baselines.** The only online multimodal methods compared are ART and AEN, both from the same research group. General continual learning methods (EWC, SI, GEM, LwF) that could be adapted to multimodal input are not considered. The offline methods include outdated ones (DAE 2011, DBM 2014), though DJSRH (2019), NRCH (2024), and FUME (2025) are recent.

4. **Some method details are underspecified.** For example, in learning scenario (3) when ${}^A N \cap {}^V N = \emptyset$, the network "selects a neuron ${}^V N_i^A$ whose referring is same with that of $N_n^A$" — how "same referring" is determined is not formalized. The role of the Fourier transform in "matching the λ parameter" to find correct descending pathways (Sec 4.1 point 3) is stated but the concrete matching mechanism is not defined.

### Trivial

None.

## Nice-to-Haves

- Apply standard continual learning methods (EWC, SI, GEM) adapted to multimodal features as additional baselines.
- Report confusion matrices for the recall tasks to directly verify that color words retrieve only color features for OML vs. all features for baselines.
- Show learning curves over the sample sequence in the open environment to visualize forgetting dynamics.
- Provide a case study or t-SNE visualization of how the reference extraction identifies correct feature dimensions over time.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Evaluation metric does not measure what it claims (precise referring)" — REMOVED.** The Harsh Critic claims the comparison is "systematically biased in favor" of baselines because they are credited with correct recall even when returning all features. However, the paper explicitly states this counting convention (Sec 4.1 point 2), and the baselines *still perform worse than OML* (Table 2: DAE 60.7 vs. OML 87.3 on E-Fruits V→A close). The lenient counting favors baselines, not OML, making OML's outperformance *more* impressive, not less. The metric measures retrieval accuracy, which is the correct metric for the task; the precise-referring property is what enables OML's higher accuracy despite identity interference. The critic's factual premise is correct (baselines return all features) but the conclusion that this invalidates the comparison is wrong.

2. **"Inadequate baseline comparison — offline methods are heavily outdated" — PARTIALLY REMOVED.** Only DAE (2011) and DBM (2014) are outdated; DJSRH (2019), NRCH (2024), and FUME (2025) are recent. This is partially addressed in the Minor weaknesses section. The critic's claim that "the offline methods are heavily outdated" is overstated.

3. **"Figure 1 is vague"** — REMOVED. This is a subjective presentation nitpick, not a substantive weakness.

4. **"Related work is very brief"** — REMOVED. The related work adequately covers both joint and coordinated representation methods and cites the relevant online multimodal methods. Conciseness is not a weakness when the key limitations are identified.

5. **Various speculative concerns** (e.g., "cannot tell if OML truly separates the modalities without examining false positives" in Table 3) — REMOVED as speculative without specific evidence in the paper.

6. **"The paper does not report the number of classes per subset"** — This is a minor procedural detail that does not affect the validity of results. The open environment design is clearly described: four equal parts, each containing different classes.

7. **Strength about conflict detection from Strength Finder** — REMOVED because it conflicts with the verified Major weakness that conflict detection is not properly evaluated. The statement "OML is able to detect all conflicts" is asserted without evidence.

## Novel Insights

The most interesting observation emerging from cross-referencing the reviews is the asymmetry between the paper's two main claimed capabilities. The reference extraction mechanism (identifying which features a word refers to) is well-supported: the coefficient-of-variation method is clearly described, the mechanism is testable, and Table 2 provides indirect but clear evidence that it works (OML maintains accuracy while baselines drop when attribute words are added). In contrast, the conflict-detection and interaction capability — presented as equally central — has no systematic evaluation whatsoever. This creates a strange split: one core contribution is reasonably evidenced, the other is entirely asserted. A revision that properly evaluates conflict detection (precision/recall on injected mismatches, quality of generated questions, comparison to a rule-based baseline) and either drops or substantially tempers the interaction claims would make the paper significantly stronger.

## Suggestions

1. **Add ablation studies.** At minimum: (a) remove lateral connections, (b) replace the Fourier routing with simple concatenation, (c) remove the reference extraction (treat all words the same), and (d) use a fixed threshold instead of the coefficient-of-variation method. Report the impact on Tables 1 and 2.

2. **Rigorously evaluate conflict detection.** For the 10% mismatched-pair setting, report precision, recall, and F1 for conflict detection. Show examples of generated questions and characterize failure cases. Compare to a simple baseline (e.g., always flag a conflict when the input word is not the top-1 recalled word).

3. **Report variance.** Run each experiment at least 5 times with different random seeds and report mean ± std.

4. **Scale to a larger dataset** with modern features (e.g., use CLIP or DINO features as visual backbones and word embeddings as text features on a standard multimodal dataset) to demonstrate that the approach works beyond hand-crafted Fourier descriptors.

## Score and Decision

**Calibration anchors (from retrieval):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| TPZRq4FALB.md | 8.00 | Multi-modal TTA paper with strong motivation, extensive experiments, ablation studies. OML is substantially weaker on experimental rigor. |
| HnhNRrLPwm.md | 8.00 | Large-scale multimodal benchmark with 20K queries. OML operates on a much smaller scale with hand-crafted features. |
| sb7qHFYwBc.md | 6.50 | C-CLIP: multimodal continual learning with solid ablation, comprehensive benchmarks. OML lacks ablation and has smaller-scale evaluation. |
| UstOpZCESc.md | 6.25 | Privacy-aware lifelong learning with extensive experiments and baselines. OML is weaker in evaluation completeness. |
| BZWssJoYEv.md | 5.50 | Multimodal interaction theory paper. Different type, but similar mid-tier score range. |
| Pa6SiS66p0.md | 4.33 | Multimodal lifelong learning with weak baselines and limited experiments. Similar profile to OML — interesting idea, incomplete evaluation. |
| gNoqEdT2wO.md | 2.33 | MCIL benchmark with insufficient contribution. OML has more substance. |
| YrxhSkfHh0.md | 3.33 | Fast multimodal feature extraction with unclear contributions. OML is stronger in novelty. |

Relative to these anchors, OML sits near the Pa6SiS66p0 level (4.33) but with stronger methodological novelty, giving it a slightly higher score. However, it falls well short of C-CLIP (6.50) due to the absence of ablation studies and limited evaluation scale.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>