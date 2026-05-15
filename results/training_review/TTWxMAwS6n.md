Now I have all the information needed to write the final consolidated review.

## Summary

X-PlugVid proposes a unified framework to adapt pretrained image-based spatial-control plugins (e.g., ControlNet, T2I-Adapter) for video diffusion models by training a single spatial-temporal adapter, without per-plugin retraining. The method introduces three technical components: (1) a spatial-temporal adapter that bridges the modality gap and ensures temporal coherence, (2) a high-pass filter that removes low-quality low-frequency components from the image model's feature maps before feeding them to the adapter, and (3) a timestep remapping strategy that maps later (information-richer) timesteps of the image model to earlier timesteps of the video model to improve guidance during critical early denoising steps.

## Strengths

- **Unified single-adapter framework eliminates per-plugin retraining.** X-PlugVid trains one generic adapter that enables all pretrained spatial-control image plugins to work with video models, whereas prior methods like Control-A-Video and ControlVideo require plugin-specific retraining. This core advantage is well-supported by the task definition (Sec. 3.1, Fig. 1) and by quantitative results (Table 1) showing X-PlugVid outperforming prior methods on both I2VGen-XL and Hotshot-XL backbones.

- **Timestep remapping is a novel and well-motivated idea.** The paper identifies a genuine problem — early-timestep features from the image diffusion model are information-poor for guidance — and provides both diagnostic evidence (PCA denoising trajectories in Fig. 6) and ablation results (Table 2, Fig. 8, Fig. 9) to validate the proposed solution. The ablation showing n=2 as the optimal remapping factor is informative and clearly demonstrates the trade-off between guidance strength and degradation from low-quality components.

- **Mechanistic analysis of ControlNet and X-Adapter motivates design choices.** The frequency analysis (Fig. 3) and feature-map visualizations (Fig. 2) provide an intuitive grounding for why high-pass filtering is needed (adapting image model features, which contain low-quality low-frequency content, rather than ControlNet's high-frequency outputs). This distinguishes the method from a purely empirical approach.

- **Training efficiency.** The method trains only the adapter (5 epochs on 100K videos with batch size 8 on 4 A100 GPUs) rather than retuning each plugin, which is a practical advantage well-supported by the paper.

## Weaknesses

### Fatal
None.

### Major

- **No direct metric for condition adherence.** The paper's central claim is "controllable video generation," yet the quantitative evaluation (Table 1) uses only FID (visual distribution similarity) and optical flow L2 distance (motion consistency). Neither metric directly measures whether the generated video actually respects the input condition (e.g., depth RMSE between the generated frames' estimated depth and the input depth, or edge accuracy for canny conditions). While the qualitative results (Fig. 7) provide some evidence, the quantitative backbone of the paper lacks a task-appropriate evaluation of the core claim. This is the most significant gap in the submission.

- **Limited breadth of plugin evaluation.** The paper claims "broad compatibility" with "over twenty" ControlNet plugins, yet the quantitative comparison (Table 1) tests only two conditions (depth and canny), and the qualitative results (Fig. 7) add only T2I-Adapter. The paper argues that depth and canny represent "dense and sparse conditions...which covers most cases," but this is an assertion rather than a demonstrated fact. Without testing on at least 4–6 diverse conditions (e.g., pose, segmentation, normal maps, HED), the "universal" framing remains unsubstantiated.

### Minor

- **Missing critical baseline: per-frame image ControlNet without temporal adaptation.** Applying a pretrained image ControlNet independently to each frame is the simplest baseline for evaluating whether the temporal adapter and remapping strategy provide any benefit over naive frame-wise application. Its absence makes it hard to isolate the contribution of the temporal modeling component.

- **Reproducibility gaps: temporal attention and high-pass filter unspecified.** The temporal attention module (Sec. 3.3.2) is mentioned by name only — no details on type (self-attention vs. cross-frame attention, causal or bidirectional), number of heads, position within the adapter layers, or parameter count. Similarly, the high-pass filter \(\mathcal{H}()\) in Eq. 1 is defined symbolically with no implementation details (cutoff frequency, kernel size, whether learned or fixed). These are necessary for reproducibility.

- **Ablations conducted on only one backbone.** All ablation studies (Table 2, Fig. 8, Fig. 9) use only I2VGen-XL. Results on Hotshot-XL or the mentioned SVD backbone are absent. This weakens the claim of generalizability across backbones.

- **Quantitative results lack error bars or significance tests.** Table 1 and Table 2 report single point estimates. Given the stochasticity of diffusion sampling, variance bars are standard practice for establishing that differences are meaningful.

- **Generalization to X-Adapter and video editing is only qualitative.** Sec. 5.1 claims that the strategies generalize to image model upgrade (X-Adapter) and video editing, but provides no quantitative evidence — only a single qualitative example (Fig. 10) for video editing and a statement of "better results" without numbers for X-Adapter.

- **Training for SVD backbone is mentioned but never evaluated.** Line 144 states "we also train our method for SVD," but the paper presents no SVD results (quantitative or qualitative), which is a dangling claim.

### Trivial

- The justification for the specific ceiling-based remapping function \( \lceil t_{vid}/n \rceil \) could be stated more clearly; the paper motivates the general idea but not the exact functional form.

## Nice-to-Haves

- Report SVD results to support the claim of backbone generality.
- Test on 4–6 diverse plugin conditions (e.g., pose, segmentation, normal maps) to substantiate the "broad compatibility" claim.
- Add a simple per-frame ControlNet baseline.
- Provide implementation details for the temporal attention module and high-pass filter.
- Include error bars or confidence intervals on quantitative metrics.
- Quantify the computational overhead of the two-stage inference procedure relative to synchronous inference.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Two-stage inference more than doubles compute at early steps"** (Harsh Critic, Sec. 3.3.4): Factually incorrect. For n=2, the image model runs T/2 steps alone, then T/2 steps with the video model (total T steps for image model, T/2 for video model). This is strictly less compute than the synchronous alternative where both run for T steps. The criticism is removed.

- **"Frequency analysis is reductive; ControlNet also injects mid-/low-frequency content"** (Harsh Critic, Sec. 3): An opinion about interpretation rather than a factual error. The paper provides spectral evidence (Fig. 3) supporting its "primarily high-frequency" claim. Removed as it is an unsubstantiated opinion.

- **Claims that reproducibility hinges on undisclosed hyperparameters typical for the field** (Harsh Critic, various): The critic requests training logs, batch-size comparisons, and similar implementation trivia that are not standard to include in a conference paper.

- **"n=1000 in ablation is extreme and inflates the apparent benefit of n=2"** (Harsh Critic, Sec. 4.4): The paper explicitly includes n=1000 as an upper-bound analysis and correctly concludes that n=2 is optimal. Including an extreme condition for analysis does not inflate anything; it strengthens the ablation.

- **"Missing related works"** — I do not have external sources to verify omissions, so this cannot be included per instructions.

- **Criticism about the paper not distinguishing itself from training-free alternatives in the introduction** — The paper does distinguish itself: it explicitly notes that ControlVideo is training-free but lacks flexibility across backbones (line 13), and frames X-PlugVid as a trainable adapter offering universal plugin compatibility. The distinction is present.

- **Strength Finder: "Generalization beyond core task is demonstrated"** — This is dropped because the supporting evidence is only qualitative/missing. It is moved here rather than kept as a strength, since it partly conflicts with verified weaknesses (no quantitative evidence for X-Adapter generalization, single example for video editing).

## Novel Insights

Beyond what the Strength Finder's strengths already capture, the most interesting aspect of the reviews is the tension between the paper's genuinely clever technical components (timestep remapping is a simple yet effective insight grounded in entropy-based reasoning; the high-pass filter is a clean fix for a real spectral mismatch between adapter inputs and ControlNet's outputs) and an evaluation that undersells these contributions by using the wrong metrics. The reviewers consistently agree that the method's core ideas are sound and practical, but the FID+optical-flow evaluation does not directly test what the paper claims to deliver. This is a case where the paper would be significantly stronger not by adding more compute or scale, but by swapping to more diagnostically appropriate metrics (depth RMSE, edge accuracy, perceptual condition fidelity) — a relatively low-effort fix that would directly address the main concern.

## Suggestions

1. **Add direct condition-fidelity metrics.** Replace or complement FID with metrics that measure whether the generated video respects the input condition: depth RMSE for depth control, edge F1/accuracy for canny, structural similarity against the condition map. This is the single most impactful improvement.

2. **Add the per-frame ControlNet baseline.** Run the image ControlNet independently on each frame of the same backbones with the same conditions. This directly tests whether the temporal adapter provides measurable benefit.

3. **Add at least 2–3 more plugin types** (e.g., OpenPose pose, HED/segmentation) to the quantitative evaluation. Even if only on one backbone, this would substantially strengthen the "broad compatibility" claim.

4. **Specify the temporal attention architecture** (type, position within adapters, number of heads, causal/bidirectional) and **high-pass filter implementation** (cutoff frequency, kernel size, learned or fixed) for reproducibility.

5. **Include error bars** on all quantitative results and report SVD results if trained.

## Score and Decision

The paper presents a well-motivated framework with genuine technical novelty (timestep remapping, high-pass filtering for adapters, spatial-temporal bridge). The method is practical and training-efficient. However, the evaluation has a significant gap: the core claim of "controllable" generation is not directly measured, and the quantitative evaluation covers only 2 of the "over twenty" plugins the method claims to support. These weaknesses are addressable but currently prevent the paper from fully substantiating its claims. The paper is borderline.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>