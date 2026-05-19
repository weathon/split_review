- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 6
Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

## Summary

This paper proposes BrainMixer, an unsupervised framework that jointly learns representations from voxel-level activity timeseries and functional connectivity graphs using MLP-based encoders with domain-specific patching and mutual-information-based pre-training. The core idea—bridging two typically separate scales of brain analysis (voxel activity and functional connectivity) in a unified unsupervised framework—is well-motivated and timely, especially given the availability of large-scale datasets like THINGS.

## Strengths

- **Consistent and substantial empirical gains across diverse tasks and datasets**: The paper reports BrainMixer achieving the best accuracy on all multi-class brain classification datasets (14.3% average improvement over the strongest baseline) and consistent AUC-PR gains in anomaly detection tasks (6.2%, 5.7%, 4.81% for edge, voxel, and brain AD respectively). These results span six datasets and 13 baselines, directly supporting the claim that jointly modeling voxel activity and functional connectivity is beneficial.

- **Biologically meaningful interpretability via case studies**: Figure 2 shows that when subjects view non-recognizable (GAN-generated) images, BrainMixer detects reduced activity in higher-level visual cortex (V3) while V1/V2 remain similar—consistent with hierarchical visual processing. Figure 3 localizes 78% of detected abnormal voxels in ADHD to Frontal Pole, Temporal Poles, and Lingual Gyrus, regions previously implicated by diffusion tensor imaging and curvature studies. This provides qualitative evidence that the learned representations capture meaningful biological patterns.

- **Domain-specific architectural innovations tailored to brain data**: Functional patching (§3.1) uses Schaefer parcellation to create variable-size patches with interpolation, addressing the non-grid topology of the brain. Temporal patching via biased random walks (§3.2) explicitly models the temporal evolution of functional connectivity with a recency bias—designs that are grounded in neuroscience domain knowledge rather than generic MLP-Mixer adaptations.

- **Comprehensive ablation study**: Table 3 systematically evaluates 11 ablation variants (removing/replacing pre-training, VA encoder, FC encoder, functional patching, temporal patching, TPMIXER, dynamic attention, time encoding, biased sampling). Every modification degrades performance, confirming that all designed components contribute to the reported results.

## Weaknesses

### Fatal
None.

### Major

- **Method description is too unclear to fully evaluate or reproduce**: The core equations (§3.1, §3.2) contain unresolved dimensional ambiguities and undefined operations. Specifically: (a) In functional patching (line 56), the paper states X̃ ∈ ℝ^{|V|×t_max} as "the matrix of X̃_i" after interpolating patches of size N_p×t_max, but the total rows after concatenating |F| interpolated patches would be |F|×N_p, not |V|, and there is no explanation of how these dimensions reconcile. (b) In the Learning Dynamic Mixer equation (line 61), the SOFTMAX operation direction is unspecified (row-wise or column-wise?), and the variable Ĥ̂ appears without definition (the equation references Ĥ̂ but the preceding line defines Ĥ̂). (c) In the Dynamic Self-Attention equation, √T̃ references a scalar that is not clearly defined (the notation section defines T̃(t) as a function of t, but the equation uses T̃ without argument). These are not mere formatting artifacts—they prevent the reader from verifying the soundness of the architecture. A method section this central to the paper's contribution must be interpretable.

- **Theorem 1 stated without proof or proof sketch**: The paper claims "TPMIXER is permutation invariant and a universal approximator of multisets" (line 97) with no justification whatsoever. For a conference paper, a theorem of this strength (universal approximation) requires at minimum a proof sketch indicating how the operations can simulate a sum-deep-set architecture or similar known universal approximator. As written, this is an unsupported assertion, not a theorem.

- **Experimental protocols are critically underspecified**: (a) The BVFC and BVFC-MEG datasets—presented as a contribution—are described in a single sentence: "3 subjects when looking at the 8460 images from 720 categories" with no information about preprocessing, parcellation used, how voxel timeseries were extracted from raw THINGS data, how functional connectivity graphs were constructed (full correlation, partial correlation, sliding window?), or the number of trials per subject. For BVFC-MEG, essentially no details are given. (b) The anomaly injection procedure is mentioned ("inject 1% and 5% anomalous edges") but it is not specified whether anomalies are random or structured, nor how ground-truth voxel-level anomalies are derived from "brain responses to not recognizable images." (c) Baseline adaptation is not documented: the paper states "We may exclude some baselines in some tasks as they cannot be applied in that setting" without specifying which baselines were excluded for which tasks, making the comparison unverifiable. (d) The pre-training/fine-tuning split is not specified—what percentage of labeled data is used for fine-tuning? Are the same subjects used in pre-training and fine-tuning? If pre-training uses the entire dataset, representations may encode test-specific information; this data leakage concern is not addressed.

### Minor

- **No discussion of computational cost or scalability**: The VA Encoder's W_flat matrix has dimensions ℝ^{d|V|×|V|}, which would be enormous for high-resolution fMRI (100k+ voxels). The temporal random walks require backward traversal in time with access to past timestamps. Neither the parameter count, training time, nor memory usage is reported or analyzed.

- **Parameter sensitivity is reported in a single sentence**: The paper states "Results show that increasing the number of walks results in better performance... The effect of the walk length on performance peaks at a certain point" without any supporting figure, table, or quantitative analysis. This is insufficient for a core hyperparameter (number/length of walks) to lack any visualization or ablation.

- **BVFC dataset has only 3 subjects**: While the number of trials (8460 images × 3 subjects) is large, 3 subjects is unusually small for fMRI studies and raises questions about cross-subject generalizability. The paper calls it "large-scale" without clarifying that this refers to the trial count.

- **Brain-level anomaly detection vs. classification distinction is unclear**: The paper separates brain AD from brain classification but only notes "based on the nature of the data, we separate these two tasks" without explaining why ADHD/Seizure/ASD detection is treated as anomaly detection (one-class on control group) rather than binary classification.

### Trivial
- The notation uses both T̃ and T̃(t) interchangeably without clear distinction in the equations.
- The time encoding section (line 99) has a garbled formula rendering that makes it unreadable in the extracted text.

## Nice-to-Haves
- Including confidence intervals or standard deviations across multiple random seeds (the tables are reported in the text as images, so error bars cannot be verified from the extracted text).
- Reporting results on held-out subjects (separating training and test subjects in pre-training) to rule out data leakage concerns.
- A comparison of parameter counts and training time against baselines.

## Removed Points
These points are flagged to be removed; treat them with caution.

1. **"Figures and tables are embedded as images"** — The extracted PDF text shows tables as images, but this is a PDF parsing artifact; the original submission likely contained LaTeX tables.
2. **"Schaefer parcellation is at the region level, not voxel level"** — This is factually incorrect. The Schaefer parcellation assigns each voxel to a parcel, so it operates at the voxel level.
3. **"Code/data link not provided in main text"** — The paper states "Supplementary materials can be found in this link" (line 23); the link was likely in the supplementary appendix which is stripped by the parser.
4. **"p-values cannot be read from images"** — The paper explicitly states p-value thresholds and maximum p-value (line 142); the tables being images is a parser artifact.
5. **Strength: "Theoretical guarantee for permutation-invariant pooling"** — This strength conflicts with the verified weakness that Theorem 1 is stated without proof; a theorem without justification is not a strength.
6. **"12.5% average improvement"** — The paper actually reports 14.3% average improvement (line 148); this is a factual error by the reviewer but the magnitude of the claim remains noteworthy either way.
7. **Criticism about missing related works** — I cannot verify the existence or absence of specific related works given my lack of access to external databases.

## Novel Insights
None beyond the paper's own contributions. The reviews surface a clear pattern: the paper has a promising and well-motivated core idea with apparently strong empirical results, but the presentation of the method and experimental protocols is insufficiently detailed to allow a reviewer to verify the claims. This is a case where the contribution is potentially significant but the execution in writing and experimental documentation falls short of publication standard in its current form.

## Suggestions
1. **Rewrite Section 3 with clarity as the primary goal**: Replace dense equation blocks with annotated pseudocode, explicit tensor dimension annotations at every step, and a clear explanation of what each operation does and why. Include a diagram showing the data flow with tensor shapes.
2. **Substantiate or downgrade Theorem 1**: Either provide a proof sketch (can be deferred to appendix) or reframe the claim as a design intuition rather than a formal theorem.
3. **Provide complete experimental protocols**: Add a table describing each dataset (subjects, voxels/channels, time windows, preprocessing), specify the anomaly injection procedure precisely, document baseline adaptation per task, and report the labeled data fraction used for fine-tuning.
4. **Address data leakage**: Explicitly state whether pre-training and fine-tuning use disjoint subjects, or conduct an experiment with subject-wise separation to validate that no leakage inflates results.
5. **Add scalability analysis**: Report model parameter counts, training time, and GPU memory usage, and briefly discuss how the method would scale to higher-resolution fMRI data.
