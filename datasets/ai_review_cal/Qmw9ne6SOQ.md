- Decision: Accept
- Avg Score: 6.50
- Scores: 5, 8, 5, 8
Now I have a thorough understanding of the paper. Here is my consolidated final review.

---

## Summary

This paper adapts Causal Mediation Analysis to text-to-image diffusion models (Stable Diffusion) to trace where knowledge about visual attributes (style, object, color, action) resides in the UNet and the CLIP text-encoder. The key findings are that (a) the UNet distributes attribute knowledge across distinct sets of layers in an attribute-specific way, and (b) the text-encoder contains *only* one causal state — the first self-attention layer — across all tested attributes, sharply contrasting with LLMs where mid-MLP layers are causal. Leveraging this text-encoder finding, the authors propose DiffFix, a closed-form editing method that updates the causal layer's output projection matrix to ablate or update concepts in under a second.

## Strengths

- **Causal tracing reveals a clear, non-trivial contrast with LLMs in both UNet and text-encoder.** Figures 2 and 3 show that UNet causal states are distributed and attribute-specific (e.g., early self-attention is causal for style but not objects/color/action), while the text-encoder has a single causal state at the first self-attention layer. This directly extends the causal-mediation methodology from LLMs to multimodal generative models and produces surprising, well-visualized findings (Section 4, Figs. 2–3).

- **DiffFix achieves 1000× speedup over fine-tuning methods with comparable editing efficacy.** The closed-form update (Eq. 2) requires under a second. Figure 5(b) reports CLIP-Scores for DiffFix that are similar to Concept Erase and Concept Ablation, while the paper documents multi-concept editing (up to 10 concepts simultaneously) in the same figure (Section 5.3, Fig. 5(c)).

- **Ablation experiment directly validates the interpretability finding.** Figure 5(a) shows that editing only the causal layer (layer 0) produces the intended concept-ablation effect, while editing layers 1–11 yields scores nearly identical to the unedited model. This explicitly connects the causal-tracing insight to a practical editing outcome, going beyond pure observational analysis.

## Weaknesses

### Fatal

None.

### Major

1. **The text-encoder "single causal state" claim may be partially confounded by the corruption methodology.** The paper corrupts the *token embedding* of the subject and then restores individual layer activations. Restoring the *first* layer (layer 0) fixes the corrupted representation before it propagates to downstream layers; restoring a later layer inherits corrupted information from earlier layers. As the authors themselves note (Section 4, "adding Gaussian noise to the entire text-embedding" as an alternative control), this interpretation concern exists. While the paper claims this alternative test supports the same conclusion (referenced only in the appendix, which is stripped by the parser), a more thorough discussion of this confound in the main paper — and ideally, the full control results — would substantially strengthen the central interpretability claim. The reader needs to be convinced that the finding is not primarily an artifact of where in the pipeline the corruption is introduced.

2. **Threshold selection for causal-state identification uses only 10 validation prompts per attribute.** The human-validated CLIP-Score threshold (Section 3.3) is derived from 10 prompts per attribute — a very small sample given the diversity of prompts within each attribute class. The paper does not report how stable this threshold is (e.g., variance across different 10-prompt subsets, bootstrapped confidence intervals, or sensitivity analysis). Because the threshold directly determines which layers are labeled "causal," a fragile threshold could change the paper's central claims. This should be addressed with a larger validation set, a statistical significance test against a null distribution, or at minimum a sensitivity analysis showing the main findings are robust to reasonable threshold perturbations.

3. **Editing evaluation lacks comparison to concurrent closed-form editing methods.** The paper compares DiffFix only to UNet fine-tuning methods (Concept Erase, Concept Ablation), but acknowledges in the related work (Section 2) that concurrent works (Gandikota et al. 2023 unified; Arad et al. 2023 refact) also use closed-form updates on cross-attention or text-encoder layers. Without quantitative comparison to these equally fast methods, the reader cannot determine whether DiffFix's advantages (speed, multi-concept capability) stem from the specific design informed by causal tracing, or simply from using a closed-form update on *any* text-encoder or cross-attention layer. This is a significant gap in the evaluation of the editing method.

### Minor

1. **Surrounding-concept preservation results are relegated to the appendix.** The paper mentions that editing does not harm surrounding concepts (Section 5.3, "surrounding_concepts") but only cites the appendix for quantitative evidence. Given that non-destructiveness is essential for practical deployment, at least a summary measure (e.g., FID on a held-out set or CLIP-Score for non-target concepts) should be in the main paper.

2. **The restoration operation lacks precise specification regarding classifier-free guidance.** The paper describes restoring layer activations and then running CFG, but it is ambiguous whether both the conditional and unconditional forward passes are restored, or only the conditional one. The phrase "including CFG" (Section 3.2) is too terse to be reproducible. This matters because CFG combines two forward passes; if only one is restored, the effective intervention is diluted.

3. **The 1000× speedup claim is not grounded with absolute runtimes for baselines.** The paper says DiffFix takes "under a second" (Section 5.1) but never states how long Concept Erase or Concept Ablation take. Without even approximate numbers (e.g., "fine-tuning takes ~10 minutes on an A100"), the factor-1000 claim is not verifiable.

4. **The human validation study lacks basic documentation.** The thresholding procedure involves a user study (Section 3.3), but the paper gives no details on the number of participants, interface design, instructions, or inter-rater agreement. This matters because the threshold directly affects the core interpretability result.

5. **No failure case analysis.** DiffFix is demonstrated on single-subject concepts (e.g., "Van Gogh," "tennis racket"). The paper does not discuss what happens with multi-word styles, compound concepts, or concepts where the last subject token does not adequately capture the attribute.

### Trivial

None.

## Nice-to-Haves

- **Tighten the coupling between UNet causal tracing and editing.** The paper edits only the text-encoder; the UNet analysis is purely observational. If the paper demonstrated that its UNet findings can also guide editing (e.g., predicting from causal tracing which UNet layers to fine-tune for a given attribute), this would significantly elevate the contribution from "we found where knowledge is" to "we used these findings to design better editing." This is a natural next step rather than a current weakness.
- **A null-model baseline for causal state identification.** Randomly corrupting a different layer than the subject token, or using a permutation test, would establish the CLIP-Score distribution under "no causal effect" and allow statistical significance testing rather than thresholding.

## Removed Points

The following points from the inputs were removed or downgraded from their original framing:

- **"Editing non-causal layers test is not fully independent because the text-encoder is causal (GPT-style)"** — Removed. This criticism misunderstands the editing setup: DiffFix modifies weight matrices (W_out) directly, not corrupted activations. The causal attention structure does not prevent editing later layers via weight modification. The paper's ablation (Fig. 5a) is a valid test of which layers' parameters actually affect the output, not a test of the corruption methodology.
- **"Restoration at every timestep is a major difference from LLM causal tracing"** — Demoted to Minor (point 2 above). The paper describes this clearly; it is not a flaw but a methodological choice worth clarifying, not a weakness.
- **"Comparison to LLM findings is apples-to-apples" and other framing points** — Removed as they are discussion points rather than weaknesses.
- **Generic strength-finder praise ("this paper addresses an important problem")** — Removed. Only concrete, evidence-anchored strengths (Sections 4–5 results) are retained.
- **Missing related works** — Not included, as I cannot verify absent references.

## Novel Insights

The most interesting observation emerging from the intersection of the two reviews is the potential *methodological asymmetry* between interpretability and editing: the paper's causal tracing reveals rich, attribute-specific structure in the UNet, yet the editing application only targets the text-encoder (where localization is trivial). This suggests a gap — the UNet findings are currently observational, and the paper would be significantly stronger if it demonstrated that those UNet-level distinctions (e.g., self-attention layers for style vs. cross-attention layers for action) can *predict* editing outcomes or guide efficient fine-tuning. The reviews collectively surface that the paper's two halves (interpretability and editing) are less coupled than they could be, even though the claimed contribution is precisely their coupling.

## Suggestions

1. Add a more thorough alternative corruption test (e.g., corrupting the full text embedding, or the UNet latent) and report the results in the main paper to address the confound concern.
2. Expand the validation set for CLIP-Score thresholding to at least 50–100 prompts per attribute, or replace thresholding with a statistical significance test.
3. Add quantitative comparison to the concurrent closed-form editing methods the paper already cites (Gandikota et al. unified; Arad et al. refact).
4. Report surrounding-concept preservation metrics (e.g., FID on MS-COCO prompts, or CLIP-Score on non-target concepts) in the main paper.
5. Clarify the restoration mechanics for CFG (both passes or one) and provide absolute runtime numbers for the fine-tuning baselines.
