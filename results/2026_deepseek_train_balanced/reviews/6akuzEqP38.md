## Summary

This paper proposes Articulate Anything, a pipeline that converts rigid 3D meshes into articulated objects by combining VLMs (GPT-4o, SAM) with geometric reasoning, without training on existing articulated object datasets. The pipeline consists of three stages: movable part segmentation via VLM-assisted labeling of SAM masks, articulation estimation via geometry-aware visual prompting of GPT-4o, and a refinement stage using SDS with randomized part transformations. The method demonstrates broader category coverage than prior articulated object generation methods and shows real-to-sim-to-real transfer on three manipulation tasks.

## Strengths

- **Zero-shot articulation estimation matching trained methods (Table 3).** On PartNet-Mobility, the geometry-aware visual prompting approach (using GPT-4o with SDF-derived keypoints and DBSCAN clustering) achieves articulation estimation accuracy comparable to CAGE, a diffusion model trained on that dataset, while significantly outperforming NAP. This is the paper's strongest quantitative evidence and directly supports the claim that open-vocabulary articulation estimation is feasible without category-specific training.

- **Randomized SDS refinement (Section 3.4, ablation in Section 4.2).** The technique of randomly transforming movable parts during SDS optimization addresses a real technical challenge: standard SDS causes parts to grow into each other and lose semantic identity. The ablation shows this qualitatively (e.g., a handle disappearing without randomization). This is a concrete, practical improvement over naively applying diffusion-based refinement to articulated objects.

- **Real-to-sim-to-real transfer on physical objects (Section 4.3).** Three real-world objects (drill trigger, microwave door, steering wheel) were scanned, run through the pipeline, and manipulated by a robot arm in simulation and reality. This demonstrates that the generated articulated objects are functional, not merely visually plausible — a bar few prior generative methods meet.

- **Consistent quantitative improvement over open-vocabulary segmentation baselines (Table 1).** The VLM-enhanced segmentation component outperforms PartSlip and PartDistill in mIoU on PartNetE, validating that GPT-4o semantic labeling helps resolve the oversegmentation/undersegmentation issues of prior lifting-based approaches.

## Weaknesses

### Fatal
None.

### Major

- **The end-to-end evaluation metric (CLIPscore/VQAscore) does not directly measure articulation correctness, and the paper's core claim rests partly on this metric.** The paper itself acknowledges "there is no ideal metric that directly evaluate the visual quality and structural correctness" (Section 4, Metrics) and uses image-text correspondence under an unvalidated assumption: that a better-articulated object will yield higher correspondence. A static render of a visually plausible but non-functional object could score just as high. The paper's unconditional generation evaluation (Table 4) therefore conflates visual quality (which the refinement stage boosts via RichDreamer) with articulation quality (which is the paper's claimed contribution). The textureless comparison against NAP and CAGE partially mitigates this, but the metric still does not measure whether the joints are correct or the object is functional. A task-oriented evaluation (e.g., whether generated objects function correctly in simulation) would be far more convincing for a pipeline whose end goal is generating functional articulated assets.

- **GPT-4o reliability is entirely unquantified despite being the pipeline's central reasoning engine.** The pipeline's part segmentation (Section 3.2) and articulation estimation (Section 3.3) both hinge on GPT-4o outputs. The paper acknowledges "GPT4o demonstrates bias in some situations" as a limitation (Section 5) but provides no quantitative analysis of failure rates, no confusion matrices for joint type classification, no per-category breakdown of success/failure, and no measurement of output consistency across repeated calls. Given that GPT-4o is a black-box API with unknown consistency characteristics, the reader cannot assess whether the pipeline works on 90% of objects or 30%. This gap weakens the paper's central claim of "open-vocabulary generalization" — the reader has no sense of where the method fails.

### Minor

- **The real-to-sim-to-real demonstration (Section 4.3) is limited to 3 objects with no quantitative success/failure rates reported.** The paper claims "minimal error in part segmentation and joint prediction" but provides no numbers, success rates, or failure analysis for the real-world transfer. Three successful demonstrations are encouraging but insufficient to assess the pipeline's robustness.

- **The segmentation evaluation (Table 1) uses PartNetE with predefined categories, which does not fully test the "open-vocabulary" claim.** An evaluation on categories outside the training distribution of the baselines, or on objects with free-form part labels, would better support the open-vocabulary claim.

- **The articulation parameter estimation results (Table 3) are not broken down by joint type (revolute vs. prismatic).** Given that the method uses fundamentally different strategies for each, per-type accuracy would reveal where the approach is strong vs. where it systematically fails.

### Trivial
None.

## Nice-to-Haves

- A human evaluation of articulation correctness (e.g., "does this object's movement match its expected function?") would strengthen the end-to-end claim considerably by testing what the metric cannot.
- Adding variance/confidence intervals across GPT-4o runs would help quantify reliability without requiring a dedicated failure analysis.

## Removed Points

- **"The articulation parameter estimation comparison against CAGE/NAP compares fundamentally different tasks"** — This criticism misunderstands the experimental setup. The paper clearly states that NAP is conditioned on ground-truth vertices with edges (joint parameters) generated, and CAGE is given certain attributes while others (including joint axes) are generated. Both are conditional generation setups where the task is to output articulation parameters given part information. The paper also retrained NAP on the same train-test split for fairness. This is a reasonable comparison design. **Removed (misunderstands the paper).**

- **"The refinement stage introduces an uncontrolled confound"** — The paper explicitly compares textureless results against textureless baselines (NAP, CAGE) in Section 4.2 ("for fair comparison, we compare our results to NAP and CAGE in a textureless manner") and conducts an ablation on refinement. The textured comparison is only made against PartNet-Mobility objects, which also have textures. The concern about confound is partially valid but the paper already takes steps to disentangle the effects. **Removed (partially addressed in paper, merged into the metric weakness above).**

- **"No statistical significance or variance reported"** — Many papers at the venue do not report variance for every metric; this is a generic criticism. **Removed (generic).**

- **Strengths about "addressing an important problem" or generic praise** — The Strength Finder's claims about problem importance are not specific evidence. Only the concrete, evidence-backed strengths are retained above. **Removed (generic/superficial).**

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- **Replace or supplement CLIPscore/VQAscore with a task-oriented evaluation for the end-to-end setting.** For generated articulated objects, measure whether the joint axes enable correct motion in simulation, whether the joint ranges are physically plausible, and whether physics-based interaction succeeds. This directly tests articulation quality rather than render quality.
- **Report GPT-4o reliability statistics:** per-category success rates for part segmentation, joint type classification, and joint parameter estimation. A confusion matrix for joint type classification would be particularly informative.
- **Expand the real-to-sim-to-real evaluation** with more objects, quantitative success rates per object, and documentation of failure modes.

## Score and Decision

The paper addresses a genuine gap — converting rigid 3D meshes to articulated objects without category-specific training data — and proposes a pipeline with several clever components, particularly the geometry-aware visual prompting for joint estimation and the randomized SDS refinement. The strongest evidence is Table 3, showing zero-shot articulation estimation matching a trained method.

However, two major weaknesses undermine the paper's claims. First, the end-to-end evaluation metric (CLIPscore/VQAscore) does not measure articulation correctness, and the paper's headline claim of generating "high-quality articulated objects" relies partly on this metric. Second, the pipeline's reliance on GPT-4o is treated as a solution without any quantitative reliability analysis, leaving the reader unable to assess robustness or generalization boundaries.

These are real gaps but not fatal — the paper provides other evidence (articulation estimation accuracy in Table 3, segmentation in Table 1, real-world transfer demos) that partially compensates. A revision addressing these issues could make this a strong contribution.

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Reject</decision>