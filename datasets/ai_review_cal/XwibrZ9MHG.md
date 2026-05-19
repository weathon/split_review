- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3
Now I have all the information needed. Let me construct the final consolidated review.

## Summary

PokeFlex is a real-world multimodal dataset of 18 deformable volumetric objects undergoing poking and dropping deformations. It provides synchronized 3D textured meshes, point clouds, RGB-D images (from professional MVS and lower-cost cameras), and contact forces/torques. The paper also presents baseline online mesh reconstruction models (106–215 Hz inference) trained on this data as a proof-of-concept use case. The key contribution is filling a gap in deformable-object robotics: a real-world dataset combining volumetric mesh ground truth with multi-view RGB-D and force sensing.

## Strengths

- **First real-world dataset with paired 3D meshes, point clouds, RGB, depth, and contact forces for deformable volumetric objects.** Table 1 (tab:comparison) shows PokeFlex uniquely includes all of these modalities, whereas prior real-world datasets (HMDO, Chen et al., DOT) each miss at least one. This directly enables tasks like online mesh reconstruction and sim-to-real transfer that require synchronized multimodal real-world data.

- **Online-capable mesh reconstruction is demonstrated as a concrete use case.** Section 4.2 reports inference rates of 106–215 Hz (on RTX 4090), in contrast to prior image-based methods (e.g., Xu et al., requiring ~10 s per frame). This shows the dataset can support real-time robotic control loops.

- **Strong reproducibility provisions.** The paper releases 3D print files for 5 objects, provides detailed specifications for the rest (purchasable globally), and documents the full capture pipeline. This is higher-effort reproducibility than most robotics datasets, which rely on non-reproducible commercial items.

- **Well-described synchronized multi-sensor capture pipeline.** Section 3.1 provides thorough details on LTC-based synchronization across the MVS, two Azure Kinects, two RealSense D405s, and the robot — a non-trivial engineering contribution that others can build on.

- **Two complementary deformation protocols (poking and dropping).** The poking protocol produces local contact deformations with force data, while dropping captures global dynamic motion at 60 fps, extending coverage beyond prior datasets that focus on only one deformation type.

## Weaknesses

### Fatal

None.

### Major

1. **The experimental demonstration of the dataset's utility is substantially limited in scope.** The multi-object mesh reconstruction experiment uses only 5 of the 18 objects (Section 4.2, Table 4), and the camera-comparison experiment uses only a single object (foam dice, Section 4.2). No error bars, confidence intervals, or multiple random seeds are reported for any experiment. The paper's claim that "well-performing models can be trained using camera sensors external to the professional capture system" rests on a 1-object experiment, which does not support the stated generality. For a dataset whose value proposition depends on enabling downstream tasks, the evaluation is noticeably thin relative to the breadth claimed in the conclusion. This does not invalidate the dataset but weakens the paper's evidence that PokeFlex enables something that prior data could not.

2. **Ground-truth mesh quality for small objects is acknowledged but unquantified, reducing transparency for downstream users.** The paper notes (Section 5, Figure 12) that fine-grained details of small objects (e.g., the 3D-printed armadillo) are not well captured by the MVS, but provides no per-object reconstruction fidelity metric (e.g., deviation from a reference scan). Without this, users cannot judge which objects are reliable for their task, which limits the dataset's usability despite its genuine value.

### Minor

1. **No ablation of architectural choices in the baseline models.** The paper uses DINOv2, FoldingNet, self/cross-attention, a conditional-NVP, and a region-of-interest loss with heuristically chosen thresholds (ε, scaling factor 0.2). None of these components are ablated. While dataset papers are not required to produce state-of-the-art methods, ablations (even on a single object) would help users understand which design choices matter and whether the ROI loss is beneficial.

2. **Dropping protocol data is collected but not used in any experiment.** The paper collects 3.2k dropping frames (Section 4.1), which include ground-truth meshes at 60 fps, but all baseline experiments use only poking sequences. The paper notes this is due to richer modalities in poking, but a brief discussion of how the dropping data could be used (or a simple baseline on it) would strengthen the dataset's completeness claim.

3. **Camera comparison experiment uses only one object (foam dice).** The conclusion about training with lower-cost cameras needs validation across multiple objects with different geometries and stiffnesses to be broadly convincing.

### Trivial

None.

## Nice-to-Haves

- Provide per-object ground-truth quality metrics (e.g., Chamfer distance between a static MVS scan and a high-quality reference) so users can judge which objects are reliable for their task.
- Include a simple cross-dataset comparison (e.g., train on HMDO or a synthetic dataset, test on PokeFlex or vice versa) to contextualize PokeFlex's value relative to prior data.
- Characterize variance across sequences for the same object (e.g., reconstruction accuracy across different poking sequences), which would set realistic expectations for generalization.

## Removed Points

- **"No experiment showing multimodal data improves over simpler inputs"** — Removed because it is factually incorrect. Table 4 shows that Images+Robot data outperforms Images alone and Robot Data alone on all metrics (L_PFD: 3.08 vs. 3.90/4.82; RPFD: 0.548 vs. 0.649/0.747). The paper explicitly discusses this in the Discussion section (lines 316–317).
- **"Architectures are not novel"** — Removed. For a dataset paper, the baseline models are meant as proof-of-concept demonstrations, not as novel methods. Lack of architectural novelty is not a weakness in this context.
- **"No baseline such as a simple linear model or always predict the template"** — Removed because the RPFD metric inherently compares against the undeformed template. An RPFD below 1 means the prediction is closer to ground truth than the template is. This is a template baseline built into the evaluation.
- **"Viewpoint-agnostic claim is a stretch"** — Removed. The paper mentions "viewpoint-agnostic online 3D mesh reconstruction methods" in the Conclusion's future-work paragraph, not as a claimed contribution. The harsh critic misreads a forward-looking statement as an empirical claim.
- **"Missing comparison table not included in parsed version"** — Removed. The table is imported via `\input{tables/table-comparison}`; its absence is a parser artifact, not an author omission.
- **"Inference rate contextualization needed"** — Removed. The main text (line 61) reports 106–215 Hz, which is well above typical robot control loop rates (30–100 Hz). The critic's request for explicit contextualization is a minor presentation preference, not a substantive gap.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the same observations that the paper itself makes: the dataset fills a clear gap in real-world multimodal deformable-object data, the baseline experiments are proof-of-concept in nature, and the primary limitations are scale and the unquantified quality of certain ground-truth meshes. The most useful insight from the review process is the structural tension between the paper's ambitious claims about enabling new application areas (sim-to-real, closed-loop control, policy learning) and the narrow scope of the demonstration (mesh reconstruction on 5 objects), which is a gap the authors should address to make the paper stronger on its own terms.

## Suggestions

1. Add per-object ground-truth quality metrics (e.g., static scan fidelity). This is the single highest-impact addition — it turns an acknowledged limitation into actionable information for users.
2. Add a simple experiment or analysis using the dropping data — even a single object — to show the 60 fps meshes are usable.
3. Report variance across validation sequences or random seeds for at least the main multi-object experiment (Table 4). Given the small validation set (1 sequence per object), readers need to know the stability of the reported numbers.
4. Tone down the forward-looking claims in the conclusion ("push the boundaries," "drive innovation in both simulation-based and real-world applications") since the paper provides no evidence for these applications. Replace with a concrete, constrained description of what the dataset is currently known to support.
