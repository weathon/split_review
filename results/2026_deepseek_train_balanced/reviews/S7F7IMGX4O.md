## Summary

Mora proposes a multi-agent pipeline for video generation that chains off-the-shelf open-source models (LLM → Stable Diffusion → InstructPix2Pix → Stable Video Diffusion / Open-Sora-Plan → video connection module) and fine-tunes them jointly via a "self-modulated" mechanism that learns per-agent modulation embeddings. Three claimed technical contributions: (1) self-modulated multi-agent fine-tuning, (2) data-free synthetic-data training, (3) human-in-the-loop + MLLM data filtering. The paper evaluates on six video generation tasks and reports that Mora achieves a VBench Video Quality score of 0.800, surpassing Sora's reported 0.797.

## Strengths

1. **Self-modulated fine-tuning produces measurable gains over the untuned pipeline.** Mora (Open-Sora-Plan) improves Video Quality from 0.767 to 0.800 over the untuned variant on VBench (Table 1), and shows improvements on Image-to-Video metrics (VideoTI 0.88→0.90, Imaging Quality 0.66→0.67 in Table 2). This demonstrates that the training procedure has a non-trivial effect.

2. **Evaluation across six video generation tasks is broader than typical.** The paper covers Text-to-Video, Image-to-Video, Video Extension, Video Editing, Video Connection, and Simulation, which is more comprehensive than most single-task video generation papers.

## Weaknesses

### Major

1. **The Sora comparison does not support the paper's central claim of "surpassing Sora."** The paper states (Section 4.1): "For comparison with Sora, we utilized videos featured on its official website and technical report." Comparing systematically generated outputs against a closed-source model's curated promotional demos is not a controlled comparison. The VBench Sora scores are "derived from the Hugging Face leaderboard" (Table 1 caption) under unknown evaluation conditions and prompt distributions, while Mora's scores come from the authors' own pipeline. For the five non-T2V tasks in Table 2, Sora is the primary baseline, but the paper does not specify how Sora's scores were obtained for tasks like "Connect Videos" or "Simulate Digital Worlds." The headline claim that Mora "surpasses Sora" is not supported by a valid comparison protocol.

2. **The abstract and conclusion directly contradict each other.** The abstract states that Mora "surpassing Sora's 0.797" and claims Mora "surpasses Sora." The conclusion (Section 5) states: "Nonetheless, it still faces a significant performance gap compared to OpenAI's Sora." These are mutually exclusive statements about the paper's main result. This inconsistency undermines the paper's coherence and suggests the authors overstate in the abstract while undercutting themselves in the conclusion.

3. **The three claimed technical contributions are not isolated by ablation.** The paper presents three distinct claimed innovations: (a) self-modulated multi-agent fine-tuning, (b) data-free training (self-training on synthetic data), and (c) human-in-the-loop + MLLM filtering. The only ablation is a binary "with vs. without Self-Modulated Multi-Agent Finetuning" marker ($^\mp$), which conflates all three techniques. There is no ablation isolating the self-modulation factor specifically (vs. standard fine-tuning), the data-free training strategy (vs. training on real data), the human-in-the-loop filtering (vs. random selection), or the iteration count N. Without these, it is impossible to tell which technique drives any observed improvement.

4. **The self-defined metrics for Tasks 2–6 (VideoTI, TCON, Tmean) are never defined.** The paper states these were designed "due to the lack of quantitative metrics" (Section 4.1) but provides no equations, no computation procedures, no implementation details, and no validation showing they correlate with human perception. These metrics are used to draw all quantitative conclusions for five of the six tasks in Table 2, yet a reader cannot interpret or reproduce them. This makes the core quantitative evidence for most of the evaluations unverifiable.

5. **The training procedure is critically under-specified.** The loss function is given only as $L(O_n, V_{\text{target}})$ with no specification of its form (MSE? diffusion loss? perceptual loss?). The pipeline chains heterogeneous models (an LLM, Stable Diffusion, InstructPix2Pix, SVD/Open-Sora-Plan) with entirely different architectures and output spaces. How gradient flow is maintained through these components—which parameters are frozen or trainable, and how non-differentiable operations are handled—is not addressed. Algorithm 1 lists hyperparameters ($\eta_{\theta_i}$, $\eta_{z_i}$, $B$, $K$, $N$) without reporting their actual values.

### Minor

1. **Training uses only 96 synthetic data points with no overfitting analysis.** The paper states "a total of 96 data were generated" (Section 4.1). Training on 96 self-generated, self-filtered examples—with no analysis of whether the model overfits, whether diversity collapses across iterations, or whether improvement generalizes to unseen prompts—is a significant gap. The iterative self-training loop (generate → filter → train → repeat) can reinforce narrow distribution biases.

2. **The claimed "perfect Dynamic Degree" is inherited from the base model, not Mora's contribution.** In Table 2 (Image-to-Video), Open-Sora-Plan alone already achieves Dynamic Degree 1.00. Mora (Open-Sora-Plan) also achieves 1.00. The paper's framing (e.g., abstract: "achieved a perfect Dynamic Degree score of 1.00, demonstrating exceptional capability") implies this is a Mora achievement, but the base model already attains it.

3. **The multi-agent pipeline without fine-tuning provides negligible improvement over base models.** Mora (SVD)$^\mp$ has nearly identical scores to vanilla SVD across all metrics in Table 2 (VideoTI: 0.88 vs 0.88, Motion Smoothness: 0.97 vs 0.97, Dynamic Degree: 0.75 vs 0.75). This indicates the pipeline architecture alone contributes little; the gains come entirely from fine-tuning, which is itself a self-training loop.

### Trivial

None.

## Nice-to-Haves

- A human evaluation study would strengthen the subjective quality claims (Aesthetic Quality, Imaging Quality) where the paper claims to surpass Sora.
- Reporting computational cost (GPU hours, training time) would substantiate the unquantified claim of "minimal computational resource requirements."
- The self-modulation mechanism's effect on coordination could be clarified with an analysis of how $\alpha_i$ differs across agents and tasks.

## Removed Points

These points were surfaced by the reviewers but removed during filtering:

- **Missing code / model weights / dataset release**: Removed per instructions about reproducibility nitpicks for large artifacts.
- **Criticism that "data-free training strategy is misnamed"**: A framing preference, not a substantive flaw.
- **Generic evaluation rigor / confounder speculation**: Removed because not anchored to specific text in the paper.
- **Strength about "Perfect Dynamic Degree as a Mora contribution"**: Removed because Open-Sora-Plan base model already achieves 1.00.
- **Strength about "iterative data-free training with demonstrable improvement curves"**: Removed as generic; figures are image files without accessible data.
- **Strength about "outperforming Sora on VBench aggregate"**: The numerical claim exists but the comparison methodology is invalid, so it cannot stand as a strength.
- **Concerns about missing related works**: Removed per instructions (external knowledge not available).
- **Complaints about formatting, typos, missing appendix content**: Removed per instructions (parser artifacts).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Drop the "surpassing Sora" framing. Honestly position the work as a multi-agent pipeline that improves over open-source baselines (Open-Sora-Plan, SVD) through self-training. Compare against accessible models under controlled conditions.
2. Conduct proper ablations isolating each claimed contribution: self-modulation vs. standard fine-tuning, data-free training vs. real data, with vs. without human-in-the-loop filtering.
3. Provide full definitions (equations, implementations) for all evaluation metrics, especially VideoTI, TCON, and Tmean.
4. Specify the loss function form and clarify how gradient flow is achieved through the heterogeneous pipeline.
5. Report overfitting analysis and generalization checks for the 96-example training set.

## Score and Decision

The paper's central claim—that Mora surpasses Sora—is not supported by a valid comparison protocol. Combined with the internal contradiction between the abstract and conclusion, missing ablations for all three claimed contributions, undefined metrics that underpin most quantitative results, and critically under-specified training details, the paper falls well short of the standards required for a top venue. The underlying idea of composing open-source models into a trainable pipeline has some engineering merit, but the evidence is insufficient to support the strong claims made.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>