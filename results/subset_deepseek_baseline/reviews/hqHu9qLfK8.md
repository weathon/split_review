## Summary

The paper introduces the task of *inverse protocol prediction* (IPP)—inferring experimental conditions (cell line, medium, seeding density, timepoint, formation method, microscope, magnification) from a single bright-field spheroid image. The authors benchmark five architectures (ConvNeXt, ViT, CoAtNet, a fusion model, and a hierarchical multi-task transformer) on the SLiMIA dataset (~8,000 images), achieving an average accuracy of 95.23% across protocol components. They also evaluate segmentation models and spatiotemporal prediction models (ConvLSTM, PredRNN++, PhyDNet). Grad-CAM analysis is used to interpret model decisions and reveal reliance on both biologically meaningful cues and dataset artifacts.

## Strengths

- **Novel problem formulation.** Framing the recovery of experimental protocols from spheroid images as a structured multi-label prediction task is original and potentially useful for reproducibility checks and automated experiment validation.
- **Comprehensive benchmarking.** The paper systematically tests a wide range of architectures (convolutional, transformer, hybrid, feature-augmented, dependency-aware) for segmentation, IPP, and temporal prediction, providing comparisons across multiple metrics.
- **Interpretability analysis.** Grad-CAM visualisations offer qualitative insight into what the models attend to, and the authors honestly identify cases where predictions rely on dataset artifacts rather than biology (e.g., microscope, magnification, replicates).

## Weaknesses

### Fatal
None.

### Major

1. **Overclaiming accuracy and contribution.** The headline accuracy of 95.23% is an average across all protocol components, but per-label analysis (referenced to appendix) shows that microscope and magnification predictions are near-perfect *because of dataset-specific artifacts*, while harder labels like seeding density, timepoint, and replicate are much weaker. This masks the true difficulty of the task and inflates the apparent contribution. The temporal prediction results are poor (SSIM < 0.40, PSNR ~18 dB), yet “first temporal modelling” is listed as a main contribution—this is unconvincing given the weak performance and limited temporal depth of the data.

2. **Unjustified causal ordering in HMTT.** The hierarchical multi-task transformer enforces a fixed causal order among labels (cell line → medium → seeding density → magnification → microscope → timepoint → replicates). The paper calls this “biologically motivated”, but no biological justification is provided. For example, seeding density is an independent experimental choice, not caused by cell line; magnification and microscope are unrelated to cell line or medium. Without a principled causal graph or evidence that this ordering improves plausibility over alternatives, the design choice appears arbitrary and undermines the claimed contribution.

3. **Poorly motivated and explained cross-dataset validation.** The IPP models trained on spheroid images (SLiMIA) are tested on RxRx1, which contains monolayer cells—a completely different morphology. The paper does not specify which protocol attributes are being predicted on RxRx1, how those labels map to SLiMIA’s labels, or what the task even means for a different biological system. The results (65–77% accuracy) are presented as a robustness test, but without clarification of the label space or task definition, the experiment is uninterpretable and does not support claims about generalisation.

4. **Temporal prediction experiments are underdeveloped.** The temporal models achieve low SSIM (< 0.40). Only two frames are used as input, and the dataset has short, irregular sequences. This section reads as an add-on rather than a substantive contribution. The cross-dataset validation on CTC (different cell types, different imaging) does not directly support the paper’s claims about spheroid growth dynamics and the experimental protocol is insufficiently described (e.g., how are labels matched?).

5. **Unclear integration of morphological features.** The Image–Shape Fusion Transformer concatenates nine manually computed shape descriptors with deep embeddings. However, the paper does not clearly state whether segmentation masks are used during inference of the IPP models or only during training. The workflow figure (Figure 2) suggests segmentation is a separate, preliminary step, but it is ambiguous how the shape features are generated and whether they come from ground-truth or predicted masks. This ambiguity affects reproducibility.

### Minor

- The claim that domain-adversarial training and morphologically informed augmentation are used is stated in the abstract but not described or evaluated in the main text. No ablation study for these components is presented, making it impossible to assess their contribution.
- The paper provides excessive low-level implementation details for standard architectures (e.g., batch size, learning rate scheduler, loss function specifics for each of eight segmentation models) that are well-known and not novel. This obscures the core IPP contribution.
- Some terminology is inconsistent or imprecise: “inverse protocol prediction” versus “reverse inference”; “Image–Shape Fusion Transformer” referenced with generic citations (Luo et al. 2025) that seem unrelated to this specific design.

### Trivial
- Figure captions are sometimes repeated verbatim (e.g., Figure 1 caption appears three times in the extracted text).
- The “LLM Usage Declaration” states LLMs were used only for polishing, but the paper’s prose is occasionally repetitive.

## Nice-to-Haves

- An ablation study isolating the contribution of domain-adversarial training, morphometric augmentation, and the fusion of shape features would strengthen the paper.
- A clearer justification or ablation of the causal ordering in HMTT (e.g., comparing random orders against the proposed order) would make the contribution more credible.
- The cross-dataset validation on RxRx1 should be redesigned: either test on a dataset with the same protocol labels, or clearly frame it as a zero-shot domain-adaptation experiment with careful description of how labels are aligned.

## Novel Insights

None beyond the paper’s own contributions. The insight that morphological cues in bright-field spheroids are partially recoverable for protocol inference is interesting but is already implicit in the problem formulation. The observation that models exploit dataset-specific artifacts (e.g., microscope fingerprint) is not new but is worth documenting.

## Suggestions

1. Remove or substantially strengthen the temporal prediction section. If kept, clarify the dataset construction (number of sequences, length, how labels are used) and consider whether predicting individual frames is meaningful given the small temporal horizon.
2. Clearly define the cross-dataset validation task: what labels are predicted on RxRx1? How do they correspond to SLiMIA’s label space? If there is no correspondence, either remove the experiment or frame it as a different task (e.g., batch-effect detection).
3. Provide a per-label breakdown of accuracy (not just in the appendix) and explicitly discuss why microscope/magnification predictions are high but driven by artifacts, to avoid overclaiming overall accuracy.
4. Describe the pipeline for morphometric feature extraction: are shape descriptors computed from ground-truth masks or predicted masks? If from predicted masks, how robust is this to segmentation errors?
5. Ablate the HMTT causal ordering: compare against a flat multi-task baseline and against a random order to show that the biologically-motivated order actually improves consistency.
6. Reduce the lengthy segmentation and model training details (most are standard) and instead focus space on clarifying the novel aspects of the IPP formulation and the experimental designs that are unique to this work.

## Score and Decision

The paper proposes a novel task and provides a broad benchmark, but several core claims are overstated (overall accuracy, temporal contribution, causal ordering justification) and key experimental details are missing or ambiguous (cross-dataset validation, morphometric integration). The weaknesses are major enough that the paper in its current form cannot be accepted.

**MY FINAL SCORE:** <score>4.0</score>
**MY FINAL DECISION:** <decision>Reject</decision>