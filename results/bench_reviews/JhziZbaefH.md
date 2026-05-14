Now I have all the material I need. Let me construct the final review.

---

## Summary

This paper presents OML, a brain-inspired neural network for online multimodal learning. The architecture is hierarchically modular with feature, unimodal-association, and multimodal-association layers connected by ascending, descending, and lateral pathways. Two key algorithmic contributions are: (1) a reference-extraction function that uses the coefficient of variation of descending signals to identify which feature dimensions a word refers to (e.g., distinguishing that "red" refers to color, not shape), and (2) a conflict-detection procedure that checks consistency between ascending and descending activations and queries a human user when conflicts arise. Experiments on small fruit/home-object datasets with vision-audition and vision-audition-taste modalities show that OML avoids catastrophic forgetting in open-environment settings and outperforms prior online methods (ART, AEN) on cross-modal retrieval.

## Strengths

- **Genuine algorithmic novelty in reference extraction**: The coefficient-of-variation-based method in Section 3.4 for identifying which feature dimensions a word refers to is a concrete, well-motivated solution to an underexplored problem in online multimodal learning. Table 2 demonstrates that this mechanism yields consistent accuracy gains when color-referring words are added — OML maintains retrieval accuracy while offline methods degrade and online baselines (ART, AEN) cannot distinguish name words from attribute words.

- **Consistent empirical advantage in online settings**: Across all three experiment types (baseline, precise referring, modal extension), OML outperforms the two closest online competitors (ART and AEN) in open-environment settings (Tables 1–3), demonstrating robustness to catastrophic forgetting. The modal-extension experiment (Table 3) in particular shows that frequency-based pathway routing successfully prevents cross-modal interference, a problem that causes AEN to confuse taste-referring and vision-referring words.

- **Integrated system with multiple interacting capabilities**: The paper combines online concept acquisition, cross-modal recall, reference disambiguation, and conflict detection with human-in-the-loop correction into a single architecture. This integration of capabilities — each addressing a concrete limitation of prior online multimodal methods — is a meaningful step beyond prior work (Xing et al. 2019, 2021; ART).

## Weaknesses

### Fatal

None.

### Major

- **No quantitative evaluation of conflict detection and human-in-the-loop interaction**: The paper's second claimed attribute is that the network "can detect conflict between the current input and the learned ones [and] ask the user appropriate questions." The only experimental evidence is one sentence: "when we randomly add 10% of word-image or word-taste data pairs with incorrect matches, OML is able to detect all conflicts and raise appropriate questions." There is no precision/recall measurement, no ablation over different mismatch ratios, no evaluation of whether the questions raised are actually appropriate, and no analysis of how user answers affect downstream task performance. The user simulation (default "yes" after timeout) is also unrealistic and biases the system toward accepting all associations. This leaves a core claimed contribution substantially unevaluated.

- **The method stores rather than learns representations**: Feature-neuron weights are set directly to input feature vectors (Section 3.5, case 1), association neurons are added with hard-coded connectivity when novel inputs arrive, and the only parametric adaptation is the incremental computation of running means and variances (Eq. 8). There is no gradient-based optimization, no training objective, and no mechanism for learning features that generalize beyond memorized instances. The method is functionally an online growing associative memory with similarity-based generalization through lateral connections. While this is a legitimate paradigm (akin to ART-based systems), the paper would benefit from acknowledging these limits explicitly and discussing what "learning" means in this context versus representation learning in standard ML.

- **Experiments are limited to two small datasets with hand-crafted features**: The Fruits and HomeF datasets use Fourier descriptors, color means, and MFCCs extracted by fixed backbones. There is no demonstration with learned feature extractors (e.g., a CNN), raw data, or any dataset beyond these two domain-specific collections. This limits confidence in the method's generality across modalities, feature types, and problem scales.

### Minor

- **No ablation study isolating the reference-extraction mechanism**: The paper does not report what happens when the `re()` function is disabled. Without this ablation, we cannot determine how much of OML's advantage in Table 2 comes from the reference-extraction component versus other architectural differences from ART/AEN. An ablation comparing OML with and without reference extraction would substantially strengthen the paper.

- **Comparison with offline methods in the open environment is expected but overemphasized**: The offline methods (DAE, DBM, DJSRH, etc.) are trained sequentially on class-disjoint data splits — a protocol they were never designed for. Their performance collapse confirms they are not continual-learning methods, which is already known. While this serves as a sanity check, it does not provide meaningful evidence for OML's superiority. The comparison with ART and AEN is the informative one.

- **No hyperparameter sensitivity analysis**: Key thresholds (*θ*, *ϑ*, *r*) are set to fixed values with no sensitivity study. For a method that relies heavily on hand-set thresholds for activation gating, similarity matching, and reference extraction, reporting how performance varies with these parameters is important for assessing robustness.

### Trivial

- The mathematical notation is dense in places (particularly Eqs. 1, 5, 6) and would benefit from clearer indexing conventions and intuitive explanations alongside the formal definitions. This is a readability issue, not a correctness problem — the accompanying natural-language descriptions generally convey the intended meaning.

- The anthropomorphic framing ("makes our method do learning like the way humans do") is an overclaim. The connection to human learning is metaphorical and not supported by behavioral or neuroscientific evidence. This is a presentation issue that inflates reader expectations unnecessarily.

## Nice-to-Haves

- Testing the method with a learned visual backbone (e.g., a small pretrained CNN) instead of hand-crafted Fourier descriptors and color means would demonstrate that the approach does not depend on engineered features.
- A visualization of the mean/variance evolution for example words (e.g., "red," "apple") as more samples are learned would make the reference-extraction mechanism more interpretable.
- Quantitative measurement of forgetting (e.g., how performance on earlier classes degrades as new classes are added) would complement the open-environment protocol.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh Critic: "The comparison in Table 2 is uninformative because ART/AEN metrics are inflated."** — REMOVED per hard rules. The paper explicitly states that returning all features (shape + color) is counted as correct for ART/AEN, which inflates *baseline* performance. This asymmetry favors the baselines, not OML. The comparison is thus conservative in OML's direction.

- **Harsh Critic: "There is no gradient-based optimization, no training objective — not a machine learning model."** — WEAKENED and reframed. The paper operates in the ART / self-organizing neural network paradigm, which is a legitimate subfield of neural-network-based machine learning. The criticism has been reframed as a Major weakness about the method's representational limitations rather than a dismissal of the paradigm.

- **Strength Finder: "Biologically inspired hierarchical architecture with ascending, descending, and lateral pathways."** — Dropped as generic. The architecture description is accurate but every brain-inspired paper claims this; it is not an evidenced strength.

- **Strength Finder: Generic praise about "interesting problem" and "plausible architectural template."** — Dropped as superficial. These are descriptions, not specific, evidenced strengths.

## Novel Insights

The paper's use of the coefficient of variation of descending signals to autonomously identify which feature dimensions a word refers to is genuinely novel. The insight that attribute-referring words produce stable signals in their target feature dimensions (low variance) while varying in irrelevant dimensions (high variance) is intuitively appealing and algorithmically operationalized. This addresses a real problem — distinguishing object names from attribute words — that prior online multimodal methods (ART, AEN) simply ignore by treating all word types identically. While the experimental validation is limited, the core idea is sound and could inspire further work in grounded language learning.

## Suggestions

1. Add a quantitative evaluation of conflict detection: report precision and recall at multiple mismatch ratios (e.g., 5%, 10%, 20%), test with different simulated user policies (always-yes, always-no, random), and measure the downstream effect on retrieval accuracy.

2. Include an ablation where the `re()` function is disabled (or replaced with an all-features baseline) on the E-Fruits / E-HomeF datasets to isolate the contribution of reference extraction.

3. Report hyperparameter sensitivity for *θ*, *ϑ*, and *r*, or at minimum justify the chosen values with a brief empirical motivation.

4. Replace the anthropomorphic claims ("learning like humans") with more precise language about what the system does: online associative memory with structural plasticity, reference disambiguation, and consistency-based conflict detection.

5. Discuss the scope of "learning" explicitly — acknowledge that the method stores instances and adapts connectivity rather than optimizing a loss function or learning feature transformations, and clarify why this design is appropriate for the targeted online multimodal setting.

---

**Anchor comparison for score calibration:**

| Anchor | Avg Score | Comparison to paper under review |
|--------|-----------|----------------------------------|
| `/home/wg25r/review_agent/human_reviews_2026/BNZnqTlQjZ.md` | 2.50 | Same research lineage (Xing et al.), similar hierarchical architecture. Our paper adds reference extraction and conflict detection — genuine algorithmic contributions beyond that work. Both share limitations of small datasets and hand-crafted features. This paper is clearly stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/6Kfbi3ngT1.md` | 2.67 | Multimodal continual learning with CLIP. More modern infrastructure but criticized for minimal novelty. Our paper has more concrete algorithmic novelty (reference extraction, conflict detection) but less modern methodology. |
| `/home/wg25r/review_agent/human_reviews_2026/Mn6Q4LWyiv.md` | 4.00 | Brain-inspired multimodal emotion recognition. Similar level of neuroscience-inspired framing and some concerns about superficial borrowing. Our paper has more concrete algorithmic contributions and is roughly comparable in quality. |
| `/home/wg25r/review_agent/human_reviews_2026/KjxS4AgFol.md` | 5.00 | Bio-inspired continual learning (MSCN), accepted as poster. Much more comprehensive experiments (4 benchmarks, SNN+ANN variants). Our paper has narrower experimental scope and less rigorous validation. This anchor is stronger than our paper. |
| `/home/wg25r/review_agent/human_reviews_2026/pBb25np2bD.md` | 5.00 | LMM continual learning with extensive experiments across model families and benchmarks. Much stronger experimental validation than our paper. |
| `/home/wg25r/review_agent/human_reviews_2026/eCrvaO0WVF.md` | 4.50 | Dynamic alignment for multimodal CL. Withdrawn but had mid-range scores. More standard ML methodology, comparable novelty. Our paper is slightly weaker in experimental rigor. |
| `/home/wg25r/review_agent/human_reviews_2026/F4dntnOqDE.md` | 5.50 | NeuMoSync — neuromodulatory control for CL. Rejected despite strong scores. More principled approach with clearer mechanism. Our paper is weaker. |

The paper makes real, concrete contributions (reference extraction, conflict-detection mechanism) that advance a specific research niche, with consistent but limited experimental support. It is clearly stronger than the 2.50–3.00 anchors, comparable to the 4.00 anchor (Mn6Q4LWyiv), but falls meaningfully short of the 5.00+ anchors in experimental scope and rigor. The insufficient evaluation of the conflict-detection claim and the hand-engineered nature of the system are the main limiting factors.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>