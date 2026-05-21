Now I have all the information needed. Let me compile the final consolidated review.

## Summary

This paper introduces a novel problem formulation for machine unlearning by decoupling the class label from the target concept. It identifies three new mismatch scenarios (target mismatch, model mismatch, data mismatch) beyond the conventional all-matched setting, provides a theoretical analysis of representation-level "gravity effects" in forgetting dynamics, and proposes TARF (TARget-aware Forgetting)—a framework combining annealed gradient ascent on forgetting data with target-aware gradient descent on hard-to-affect retaining data. Experiments on CIFAR-10/100, ImageNet, and real-world applications (stable diffusion, TOFU) demonstrate competitive performance.

## Strengths

1. **Novel problem formulation that genuinely expands the scope of machine unlearning.** The paper systematically formalizes the decoupling of class labels from target concepts in unlearning, introducing three new scenarios (target mismatch, model mismatch, data mismatch) that are well-motivated by practical concerns (privacy, copyright, fairness). This is a genuinely new conceptual contribution—previous work universally assumed the target concept coincides with the class label. The taxonomy in Figure 1 and Table 1 clearly defines the four scenarios.

2. **Extensive empirical evaluation across multiple benchmarks and applications.** The paper evaluates TARF on CIFAR-10, CIFAR-100, Tiny-ImageNet, and ImageNet-1k, comparing against 8 baselines including SCRUB, GA, FT, and L1-sparse. TARF achieves the lowest Gap to the Retrained reference on 6 of 8 tasks across CIFAR-10 and CIFAR-100 (Table 3). On ImageNet-1k, TARF achieves the best Gap across all four settings (Table 4). The paper also includes real-world case studies on stable diffusion concept removal and TOFU, demonstrating practical relevance beyond classification.

3. **Scalability demonstrated on large-scale datasets.** Unlike many unlearning papers that only evaluate on CIFAR-10/100, this paper validates on ImageNet-1k with ResNet-18, showing TARF achieves competitive results (e.g., Gap=3.66 on all-matched, Gap=3.97 on target mismatch) while maintaining reasonable computational cost (~600 seconds, vs. ~7000 seconds for retraining).

4. **Ablation studies that illuminate mechanism design choices.** Figure 7 systematically investigates the effect of annealing strength, constant vs. dynamic gradient ascent, different model architectures, and operations on identified false retaining data. The ablation showing that gradient cleaning (zeroing gradients) on identified false retaining data outperforms gradient ascent is informative and non-trivial.

## Weaknesses

### Major

1. **Ambiguity in the retrained reference definition for mismatch scenarios.** The paper states "the retrained model for every task is trained using D_r = D \ D_f" (Section 2). In target/data mismatch, D_f ⊂ D_t, so D \ D_f includes the false retaining data D_fr. The Retrained model thus still knows D_fr. Table 3 reports Retrained UA = 0.00 for target/data mismatch, which is consistent if UA measures accuracy on D_f (the given forgetting data) rather than the full target concept D_t. However, the paper never explicitly defines what "unlearning targeted subset" (Section 4.1) means in mismatch settings. This ambiguity creates a tension between the paper's rhetoric about "forgetting the target concept" and an evaluation that actually measures approximation of retraining without D_f. The paper needs to: (a) clearly state that UA is evaluated on D_f specifically in all settings, and (b) clarify whether the goal is to forget D_f (matching exact unlearning) or the full D_t (which would require a different retrained reference). This is not a fatal flaw—the results are internally consistent under the interpretation that UA is on D_f—but the lack of clarity undermines the reader's ability to interpret the paper's claims.

2. **Model mismatch evaluation methodology is underspecified.** In model mismatch, the model is trained on superclass labels (e.g., "people"), while the target concept is fine-grained classes (e.g., "boy," "girl"). Table 2 reports fine-grained accuracies (UA-F, UA-R) for this setting, including for the Retrained model. However, a model trained on superclass labels cannot output fine-grained predictions by default, and the paper does not specify how these fine-grained accuracies are computed (e.g., via a k-NN classifier on features, probing, or some other mechanism). This makes the evaluation methodology in Table 2 unverifiable. The paper should describe the procedure for obtaining fine-grained predictions from a superclass-trained model, or explain how the Retrained reference for UA-F/UA-R is obtained.

### Minor

3. **TARF is not consistently state-of-the-art across all settings.** On all-matched forgetting (CIFAR-100), SCRUB achieves Gap=0.71 vs. TARF's 1.11. On model mismatch (CIFAR-10), SCRUB achieves Gap=2.60 vs. TARF's 2.90. TARF's primary advantage is in target/data mismatch, where the Gap gaps are large (e.g., TARF Gap=0.21 vs. next best GA 8.86 on CIFAR-100 target mismatch). This is honest reporting, but the paper's framing ("TARF performs well across various tasks") could better acknowledge when baselines are competitive.

4. **Theoretical analysis is suggestive rather than predictive.** Theorem 3.2 provides an upper bound on the loss-change gap that depends on representation distance, but the O(η²) term and dependence on the Jacobian eigenvalue make it descriptive rather than quantitatively predictive. The "gravity" metaphor is useful as a conceptual tool, and the empirical validation in Figure 3 is consistent with the theory, but the theorem does not provide tight bounds or actionable predictions. The paper would benefit from acknowledging this limitation more explicitly.

5. **The threshold β for identifying hard-to-affect data is heuristic.** The paper sets β as the "lowest value of top-10% data" (Section 3.3), which is a somewhat arbitrary choice. The paper mentions a robustness study in the appendix (which is not available in the main text), but the heuristic nature of this choice is a limitation. The assumption that the number of classes in D_un belonging to the target concept is known (Section 2) is also strong.

### Trivial

6. **Table 5 (TOFU results) has formatting issues.** The table has duplicated rows and the column structure is confusing, making it difficult to interpret which results correspond to which settings. The "QA Prob" metric is not explained in the main text.

## Nice-to-Haves

- An ablation study that separately evaluates the contribution of each phase (GA only, GA + identification without Phase III, full TARF) for target/data mismatch would help clarify what drives the near-zero UA results.
- A discussion of computational cost for the identification step (multiple forward passes to compute I_con for all remaining data) on large-scale datasets like ImageNet would be useful.
- For the model mismatch scenario, a clearer operational definition of what "forgetting" means here (e.g., is the goal to change predictions away from the superclass prediction, or to affect the internal representation in a specific way?) would strengthen the paper.

## Removed Points

- **Harsh critic's Point 1 (fatal inconsistency claim):** The critic argues that Retrained UA=0.00 for target/data mismatch is contradictory because the retrained model (trained on D \ D_f) includes D_fr in its training data. However, this is only contradictory if UA measures accuracy on the full target concept D_t. If UA measures accuracy on D_f (the given forgetting data)—which is the natural interpretation of "unlearning accuracy" on the data the user actually provides for forgetting—then Retrained UA=0.00 is consistent because D_f was excluded from retraining. The paper should clarify this, but it is not a fatal inconsistency. **Moved from weakness to removed because the critic's framing as a "contradiction that invalidates the comparison" is not supported by the text—the paper is internally consistent under a reasonable interpretation.**

- **Harsh critic's Point 2 (unclear forgetting mechanism for D_fr):** The mechanism is implicitly described: Phase I uses GA on D_f, which spills over to D_fr via gravity effects; Phase II excludes D_fr from gradient descent (τ=0 for high-I_con data); the forgetting is sustained by not reinforcing D_fr. The ablation (Figure 7, right) explicitly compares gradient operations on D_fr. **Downgraded from major to minor insight—the mechanism is present in the paper, just not explained in a single clear sentence.**

- **Harsh critic's claim about "weak gravity" in Theorem 3.2 contradicting results:** The critic asserts that "representation gravity is weak (large d_h)" in target/data mismatch, which would prevent GA on D_f from affecting D_fr. However, Figure 3 (right panel) shows that in target/data mismatch, the concept-aligned data (D_fr) does experience loss increase during GA on D_f, albeit less than the forgetting data. The paper's own analysis (Remark 3.2) acknowledges the weak gravity but the empirical results show it's still sufficient for identification. The critic's claim that this creates a "gap" is not supported by the paper's actual data. **Removed.**

- **Harsh critic's claim about missing appendix sections:** The critic mentions robustness studies and details that "cannot be seen" because the appendix is stripped. Per the hard rules, these are parser artifacts. **Removed.**

- **Strength Finder's claim about "consistent state-of-the-art" across all settings:** TARF does not win on all-matched (CIFAR-100) or model mismatch (CIFAR-10). **Softened in the actual strengths section above.**

## Novel Insights

None beyond the paper's own contributions. The calibration review process did not surface any observation about this paper that the paper itself does not articulate.

## Suggestions

1. **Clarify the UA definition for mismatch scenarios.** Explicitly state that UA evaluates accuracy on D_f (the given forgetting data) in all settings, and discuss how this relates to the "target concept forgetting" framing. If the paper intends to evaluate forgetting of the full D_t, then the retrained reference should be trained on D \ D_t and the results should be recomputed accordingly.

2. **Specify the model mismatch evaluation procedure.** Describe how fine-grained accuracies (UA-F, UA-R) are computed for models trained on superclasses. If a probing classifier is used, provide details of its architecture and training.

3. **Add a direct analysis of D_fr forgetting.** Track the loss/accuracy on D_fr during Phase I and Phase II to empirically demonstrate that the gravity effect from GA on D_f is sufficient to drive forgetting of D_fr, even without explicit gradient ascent on D_fr.

4. **Acknowledge limitations more explicitly.** The paper would be strengthened by a clearer statement that: (a) TARF is not always superior to SCRUB on all-matched and model mismatch, (b) Theorem 3.2 is a descriptive bound rather than a tight predictive result, and (c) the β threshold for identification is heuristic.

## Score and Decision

**Round 1 bracket:** I queried for weak anchors (score < 3.5), middle anchors (3.5–7.5), and strong anchors (> 7.5). The weak anchors (avg 2.5–3.0) are papers with withdrawn/reject decisions and limited contributions. The middle anchors include rejected papers at 4.75–5.25 and accepted papers at 6.60–6.67. The strong anchors (avg 8.0–9.0) are oral-level papers with very strong contributions. The initial bracket placed this paper in the 5.0–7.0 range.

**Round 2 narrowing:** I queried for papers in the 5.0–7.5 range on similar topics. The retrieved anchors include:
- **"Unlearning via Sparse Representations"** (avg 5.25, Reject): A zero-shot method limited to a specific architecture (DKVB). The current paper is clearly stronger—it has a more novel problem formulation, more extensive experiments, and a generalizable method.
- **"The Utility and Complexity of In- and Out-of-Distribution Machine Unlearning"** (avg 6.60, Accept Poster): A theoretical paper with rigorous analysis but limited experiments. The current paper has broader experiments and a more practical contribution but weaker theory. Comparable overall quality.
- **"Controllable Unlearning for I2I Generative Models"** (avg 6.67, Accept Poster): Good contribution with theoretical guarantees and solid experiments. The current paper is comparable in empirical breadth but has less rigorous theory.
- **"Machine Unlearning for Streaming Forgetting"** (avg 4.75, Reject): Interesting streaming setup but weak experimental validation. The current paper is clearly stronger.

**Final score:** 6.0. The paper has a genuinely novel and valuable problem formulation, extensive experiments, and a reasonable algorithm. The evaluation ambiguities (particularly around UA definition in mismatch settings and model mismatch evaluation methodology) are real but addressable. The paper is stronger than the 5.25 rejected papers but not as clean as the 6.60–6.67 accepted papers. It is a solid contribution that would benefit from a revision to clarify the evaluation.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>