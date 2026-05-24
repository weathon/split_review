## Summary
The paper introduces **Free-Form HOI Generation**, constructs **WildO2**, an in-the-wild pseudo-3D hand-object interaction dataset with 4,414 inspected samples across 92 intents and 610 object categories, and proposes **TOUCH**, a text-conditioned contact-guided diffusion/refinement framework for generating static hand-object interaction poses. The core technical idea—predicting hand/object contact maps and using them to condition pose diffusion, followed by physical/contact refinement—is coherent and supported by meaningful ablations, but the paper’s claims about real-world 3D accuracy, physical plausibility, semantic controllability, and “action” generation are stronger than the evidence warrants.

Overall, this is an original and useful direction with clear value to the HOI generation community, especially because it moves beyond grasp-centric datasets and contact priors. However, the claims are only moderately well supported: the dataset and quantitative evaluation depend heavily on the same reconstruction/refinement pipeline used to produce pseudo-ground truth, and the method generates static contact-pose snapshots rather than dynamic free-form interactions.

## Strengths
- **Concrete dataset contribution for diverse non-grasping hand-object contact snapshots.** WildO2 contains 4,414 inspected 3D HOI samples, over 44k annotations, 92 intents, and 610 object categories, with dense hand/object contact maps and 17 hand-part labels including finger pads, nails, knuckles, palmar, and dorsal regions (Sec. 3.2–3.3, Fig. 3). This is a meaningful resource for studying static hand-object contact beyond stable grasps.
- **The O2HOI frame-pairing strategy is a sensible way to scale in-the-wild reconstruction.** Sec. 3.1 uses an object-only frame for object reconstruction and transfers the object mask to the interaction frame, directly addressing the severe occlusion problem that makes hand-object reconstruction difficult in internet videos.
- **The method design is coherent and well aligned with static contact-pose synthesis.** TOUCH first predicts contact maps, then uses contact-selected local features and multi-level text/object conditioning in diffusion, and finally refines the pose with contact/penetration constraints (Sec. 4.1–4.3).
- **Quantitative results on WildO2 show clear gains over adapted baselines.** In Table 1, TOUCH improves over ContactGen and Text2HOI on contact accuracy, MPVPE, penetration volume, P-FID, VLM score, and user perceptual score; for example, P-IoU improves to 0.776 and MPVPE drops to 2.97.
- **Ablations substantiate the importance of major components.** Table 2 shows large drops when contact guidance is removed (`✗ hoc.`, P-IoU 0.492 vs. 0.728 without TTA), when the refiner is removed (`✗ refiner`, P-IoU 0.513), and when the multi-level architecture is removed (`✗ mul.`, P-IoU 0.525), supporting the paper’s claim that explicit contact modeling and multi-level conditioning matter.

## Weaknesses

### Fatal
None.

### Major
- **The dataset and the main evaluation depend on the same unvalidated pseudo-3D reconstruction/refinement pipeline.** Sec. 3.2 reconstructs the object from an object-only frame, aligns it to the interaction frame via differentiable rendering in Eq. 1, and then refines the hand using mask, 2D joint, ICP contact, contact, penetration, anatomy, and self-contact losses in Eq. 2. The paper then states that these outputs “constitute the ground truth of our dataset” (line 103), and Sec. 5 evaluates contact accuracy, MPVPE, penetration, and semantic/geometric metrics against this WildO2 test set. This is a substantive limitation: strong agreement with WildO2 demonstrates consistency with the reconstruction-and-regularization pipeline, but does not by itself establish that the recovered 3D contacts, object poses/scales, or hand poses are accurate measurements of real-world interactions. Manual inspection/refinement helps, but the paper does not report independent validation against calibrated captures, multi-view data, human-labeled contacts, known object models, or a manually verified 3D subset.
- **The paper’s framing as free-form interaction/action generation overstates what the method outputs.** Sec. 4 states that the method generates a hand pose parameterized by `H` and contact maps `C_H, C_O` conditioned on text and an object mesh (line 113). There is no object trajectory, force, temporal phase, action outcome, or dynamic sequence. This is acknowledged in the limitations (“currently focuses on static HOI snapshots,” line 274), but the abstract and introduction repeatedly invoke pushing, poking, rotating, and daily interactions as if the method generates full interactions. For many non-grasping actions, the action semantics are not only in a static contact pose but also in motion direction, object displacement, timing, and causal effect. The contribution is better described as **text-conditioned static HOI contact-pose generation**, not full free-form HOI/action generation.
- **The evaluation metrics only partially support the physical and semantic claims.** Sec. 5.1 lists MPVPE under “Physical Plausibility,” but MPVPE is an error to a single reconstructed test pose, not a physical plausibility metric. The authors themselves note in Sec. 5.3 that low penetration can be misleading when the hand drifts away from the object. Contact IoU/F1 are useful, but they are evaluated against pseudo-labels and can partially reflect following explicit contact-part information in the DSC format rather than understanding the action. P-FID is distributional and does not directly test whether distinctions such as push vs. pull, firm vs. gentle, or rotate vs. tip are semantically realized. The user/VLM scores help, but the evaluation remains weaker than the paper’s broad claims about fine-grained semantic controllability and physical plausibility.
- **The baseline comparison does not fully isolate the proposed architectural contribution.** Sec. 5.2 adapts ContactGen and Text2HOI and adds post-processing, which is appreciated, but the paper does not clearly show that baselines receive the same detailed DSC-style conditioning, contact-part information, and refinement capacity as TOUCH. Since TOUCH’s advantage may come from a combination of richer textual/contact conditioning, contact prediction, multi-level injection, and test-time refinement, Table 1 is suggestive but not fully diagnostic. Table 2 is more convincing for component-level evidence, but all ablations still rely on WildO2 pseudo-ground truth.

### Minor
- **The accepted WildO2 subset may be biased toward easier reconstruction cases.** Fig. 3(a) reports 55% success from the initial clips, with many failures due to pose estimation or reconstruction. This does not invalidate the dataset, but it suggests the final 4,414 samples may underrepresent hard viewpoints, severe occlusions, difficult geometries, and interactions where the reconstruction pipeline fails.
- **Out-of-domain generalization is supported only qualitatively.** Sec. 5.4.2 and Fig. 7 show plausible examples on Objaverse meshes and some verbs outside the primary annotated intents, but the paper states that this demonstrates “strong generalization capability” without quantitative OOD tests on held-out object categories or held-out intents.
- **The force-expression analysis should be interpreted cautiously.** Sec. 5.4.3 correctly says the model does not explicitly model physical forces, but the surrounding discussion suggests semantic grounding of “firm” and “gentle.” The reported 22–25% larger contact area for “firm/tight” prompts is interesting, but it shows a correlation with contact extent, not force understanding.
- **The refiner is central rather than merely a final polish step.** Sec. 4.3 introduces the refiner to address global pose drift, and Table 2 shows that removing it substantially reduces contact accuracy. This is not a flaw by itself, but the paper should be clearer that final performance depends heavily on post-generation optimization/refinement.

### Trivial
None.

## Nice-to-Haves
- Add an independently validated subset of WildO2 with manually labeled contact regions, calibrated/multi-view captures, known object models, or another external source of 3D verification.
- Include controlled prompt-edit experiments: fix the object and vary only the action verb, hand contact part, object contact region, or force adjective, then quantitatively measure whether the predicted contact maps and poses change as intended.
- Present a stronger apples-to-apples baseline: e.g., a diffusion model using the same object geometry, same DSC/SSC text encodings, and same refinement/TTA, but without the proposed contact-map prediction or coarse-to-fine conditioning.
- Add held-out object-category and held-out intent splits if the paper wants to make stronger semantic and object-level generalization claims.

## Removed Points
These points are flagged to be removed or treated with caution.

- **Generic “the problem is important” strength.** The motivation is reasonable, but importance alone is not a paper-specific strength unless tied to the concrete dataset/method contribution.
- **Claims that the evaluation is broadly comprehensive.** The paper does evaluate contact, penetration, diversity, P-FID, VLM, and user scores, but this conflicts with the verified weakness that these metrics only partially support the claimed physical and semantic properties.
- **Strong OOD generalization as a main strength.** Fig. 7 provides useful qualitative examples, but no quantitative OOD evaluation; therefore this should not be treated as strong evidence.
- **Strong force-understanding as a main strength.** Fig. 9 and Sec. 5.4.3 show larger contact areas for “firm/tight” prompts, but not modeled force or physical force understanding.
- **Overly speculative concerns about the cycle-consistency mappings.** Eq. 7 defines the cycle loss conceptually, but further details may be in the appendix, which is stripped from the parsed paper. This is at most a clarification request, not a substantive weakness here.
- **Pure presentation/style concerns and missing-reference concerns.** These are not considered in this review per the instructions.
- **Claims that the dataset scale alone is too small for 92 intents and 610 categories.** The scale is not huge, but 4.4k curated 3D HOI samples is meaningful for this setting; the stronger issue is validation of pseudo-ground truth, not raw size.

## Novel Insights
The most important synthesis is that the paper’s actual contribution is strong but narrower than its framing: it provides a scalable pseudo-3D dataset and a contact-guided generator for **static hand-object contact snapshots**, not a validated generator of dynamic free-form actions. The key methodological idea—using predicted contact as an intermediate representation for text-conditioned pose generation—is well supported internally, but the evidential bottleneck is external validity: both the dataset and most quantitative claims rest on pseudo-ground truth produced by the same reconstruction and physical-regularization pipeline.

## Suggestions
- Reframe the title, abstract, and introduction around **static free-form HOI contact-pose generation** rather than action generation.
- Add independent validation of WildO2, even on a small subset, reporting hand pose error, object pose/scale error, and contact annotation reliability.
- Separate metrics into “agreement with WildO2 pseudo-labels” versus “physical plausibility” and avoid treating MPVPE to a single pseudo-ground-truth pose as a physical metric.
- Add controlled semantic tests where one prompt factor changes at a time and the expected contact/pose change is measured quantitatively.
- Clarify exactly what information each baseline receives and whether the same refinement/TTA is available to all methods.
- Report held-out object and held-out intent evaluations if generalization is a central claim.

## Score and Decision

### Calibration and Anchors
**Round-1 bracket:** The first retrieval round placed this paper above weak 2.5–3.0 anchors with severe soundness/novelty issues, and broadly in the 5.5–7.0 region. It is stronger than the 5.25 HOI-Diff anchor because it has a more concrete dataset contribution and clearer component ablations, but below strong 7.5–8.5 anchors that have more decisive validation and fewer central overclaiming issues. Initial bracket: **5.5 to 7.0**.

**Round-2 narrowing:** The closest anchors are the 6.0 internet-video 6D pose paper, the 6.25 pseudo-label affordance grounding paper, and the 6.5 TapMo paper. TOUCH is comparable to the 6.0–6.25 anchors: it has a valuable pseudo-labeled resource and strong internal results, but its core quantitative evidence depends on pseudo labels and its claims exceed what is directly measured. It is weaker than the higher 6.5–7.0 motion-generation anchors because those have more convincing task alignment or validation despite limitations. Final score: **6.0**.

| Anchor path | Avg score | Round | Comparison |
|---|---:|---|---|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/xcHIiZr3DT.md` | 2.50 | R1 | Much weaker; this anchor has more fundamental soundness/validation problems. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/KWo4w1UXs8.md` | 3.00 | R1 | Weaker; TOUCH has a clearer dataset/method contribution and stronger experiments. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/U6UPhLBTcv.md` | 3.00 | R1 | Weaker; TOUCH is more coherent and better evaluated internally. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Fk4Op9wpEp.md` | 3.00 | R1 | Weaker; TOUCH has more direct evidence and a more substantive contribution. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/nTNElfN4O5.md` | 5.50 | R1/R2 | Comparable but slightly weaker; TOUCH has a stronger dataset contribution, but both have limited novelty/validation concerns. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ZYwLfi50GI.md` | 5.25 | R1/R2 | Slightly weaker; TOUCH has better contact-specific modeling and dataset novelty, though both suffer from physical/semantic evaluation limitations. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/OWIk5E4lJs.md` | 5.20 | R1/R2 | Slightly weaker; TOUCH’s ablations and 3D contact formulation are more convincing. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/J4D5WVoc5g.md` | 4.50 | R1 | Weaker; this anchor has more serious comparison/presentation/soundness concerns. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/LbEWwJOufy.md` | 8.50 | R1 | Much stronger; it has more decisive empirical validation and fewer central claim/evaluation mismatches. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/vaEPihQsAA.md` | 7.60 | R1 | Stronger; despite limitations, this anchor is closer to a clearly accepted systems/generation contribution. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/u1cQYxRI1H.md` | 10.00 | R1 | Far stronger and not directly comparable; included as a high-score retrieval anchor. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/7gUrYE50Rb.md` | 8.00 | R1 | Stronger; broader dataset/task validation and clearer acceptance-level contribution. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/7652tHbbVE.md` | 5.20 | R2 | Slightly weaker; TOUCH has a more concrete dataset contribution and clearer contact ablations. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/mm0cqJ2O3f.md` | 7.00 | R2 | Stronger; despite scope concerns, it has stronger task alignment and persuasive interaction-generation results. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/OeH6Fdhv7q.md` | 6.50 | R2 | Somewhat stronger; it has notable novelty and compelling qualitative breadth, though also limited evaluation. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/IZMPWmcS3H.md` | 6.67 | R2 | Stronger but less topically close; its score suggests acceptance-level evidence despite artifacts. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/pZISppZSTv.md` | 7.50 | R2 | Stronger; stronger physical/task grounding through closed-loop simulation and control. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/yBZd6mCWXd.md` | 5.33 | R2 | Slightly weaker; both use pseudo labels, but TOUCH’s task/dataset contribution is more compelling. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/1CIUkpoata.md` | 6.00 | R2 | Very comparable; both extract structure from internet videos with useful pipelines but have validation/novelty limitations. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/0823rvTIhs.md` | 6.25 | R2 | Comparable to slightly stronger; both leverage pseudo labels, but this anchor’s pseudo-label evaluation concerns are less central to its whole claim. |

**Final assessment:** Originality is good, the research question is valuable, and the dataset/method combination is useful. The experiments are internally coherent and show clear gains, but the strongest claims are not fully supported because pseudo-ground-truth validation and static-vs-dynamic framing remain major issues. I would lean **Reject** at ICLR in its current form, though it is close to the borderline and could become much stronger with independent dataset validation and narrower claims.

## Score and Decision
**Score: 6.0**  
**Decision: Reject**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>