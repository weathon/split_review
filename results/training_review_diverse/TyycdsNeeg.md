Here is the final consolidated review.

---

## Summary

This paper introduces Zebra, a generative autoregressive transformer that leverages in-context pretraining (ICP) for solving parametric PDEs. The method uses a VQ-VAE to discretize physical states into tokens, then trains a causal transformer to predict next tokens in sequences of trajectories that share underlying dynamics. This enables zero-shot and few-shot adaptation at inference without any gradient updates, as well as uncertainty quantification through sampling. The paper evaluates Zebra across seven parametric PDE datasets (1D and 2D), showing competitive or superior performance against gradient-based meta-learning baselines (CODA, CAPE) and the fixed-frame baseline MPP.

## Strengths

1. **First in-context pretraining approach for parametric PDEs that eliminates gradient adaptation at inference.**  
   The paper introduces a novel pretraining strategy: training an autoregressive transformer on tokenized trajectory sequences that share PDE parameters, then adapting at inference purely by conditioning on context trajectories or history frames. No gradient updates are needed, unlike meta-learning baselines (CODA, CAPE) that must tune environment-specific parameters. This is a genuine architectural and training contribution. Evidence: Table 1 (comparison table) shows Zebra is the only method supporting both adaptive and temporal conditioning without gradient computation; Table 2 shows Zebra matches or outperforms CODA/CAPE on 6 of 7 datasets, with particularly large margins on 2D problems where gradient-based methods diverge (e.g., 0.119 vs. 0.678 relative L2 on Vorticity 2D).

2. **Flexible conditioning supporting variable-length contexts and multiple input types within a single pretrained model.**  
   Zebra's use of special tokens (`<bot>`, `<eot>`, `<bos>`, `<eos>`) and its autoregressive architecture allows it to accept arbitrary numbers of context trajectories (up to 6) and arbitrary numbers of initial frames, unlike MPP which is pretrained with a fixed number of input frames. The paper demonstrates this flexibility concretely: Zebra works with 2 frames in the temporal conditioning setting, while MPP[3] (pretrained on 3 frames) degrades drastically when tested on 2 frames. Evidence: Section 4.3 and Table 3 show Zebra's strong results from 2 frames; Figure 3 shows further improvement when an example trajectory is added.

3. **Generative nature enables principled uncertainty quantification.**  
   Unlike deterministic solvers, Zebra's generative sampling allows users to tune a temperature parameter to trade off between prediction accuracy and reliable confidence intervals. Section 4.4 demonstrates this: at low temperature (τ=0.1) the mean prediction is accurate but confidence intervals capture ≤80% of ground truth; at higher temperature (τ>0.5) confidence levels exceed 95%. This is a practical capability for risk-sensitive downstream applications.

4. **Comprehensive evaluation across diverse parametric PDE families, including challenging 2D problems.**  
   The paper tests on 1D (Advection, Heat, Burgers, Wave-b, Combined) and 2D (Wave 2D, Vorticity 2D) datasets with variations in coefficients, boundary conditions, and forcing terms. The consistent results across this variety—especially on 2D where CAPE diverges entirely—demonstrate robustness.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Ambiguity in Wave-b testing protocol.**  
   Table 1 reports Wave-b has only 4 environments (4 combinations of Dirichlet/Neumann boundary conditions). The paper then states (line 186): "For testing, we evaluate all methods on trajectories with new initial conditions on unseen environments. Specifically, we used ... 12 for the 1D datasets." It is unclear how 12 unseen test environments can exist for Wave-b if there are only 4 total environments. This needs clarification: are the 4 environments all used for training and evaluation is on new *initial conditions* only (not new boundary-condition environments)? Or were some held out? The paper should state explicitly what constitutes an "unseen environment" for Wave-b and how the test split is constructed. This does not invalidate the results (Zebra's strong performance on Wave-b still demonstrates adaptation to new initial conditions), but it obscures exactly what form of generalization is being measured.

2. **Overstated novelty claims.**  
   The paper claims (line 27) "the first successful application of generative modeling using quantized representations of physical systems" and (line 128) "the first adaptation of generative auto-regressive transformers to the modeling of physical dynamics." These are unnecessarily broad. VQ-VAE + transformer approaches for physical dynamics have been explored in video prediction and scientific ML contexts. The genuine novelty—and it is sufficient—lies in the *in-context pretraining strategy* for parametric PDEs, not in the VQ-VAE + transformer combination itself. The paper would be stronger by claiming "first in-context pretraining approach for parametric PDEs," which is more precise and harder to dispute.

3. **Empty Limitations section.**  
   The `\section{Limitations}` heading (line 307) contains no substantive content in the parsed text. While this may be a parser artifact, the paper should include a discussion of limitations such as: VQ-VAE compression loss potentially discarding fine-grained spatial information, the need for temperature tuning, the relatively narrow PDE families tested, and the computational cost of pretraining. The paper does acknowledge some limitations in passing (e.g., "room for improvement" on Heat, line 216), but a dedicated section is expected.

4. **Uncertainty calibration evaluated with only 10 samples.**  
   The confidence intervals and calibration metrics in Section 4.4 are based on 10 generations per configuration. Ten samples is quite small for reliable empirical coverage estimation, especially for 3-sigma intervals. The paper does not acknowledge this limitation. This does not invalidate the qualitative trend (higher temperature → wider intervals → higher coverage), but the specific claim that confidence level "exceeds 95% for τ>0.5" should be interpreted cautiously.

5. **No error bars or variance reporting on main results.**  
   Tables 2 and 3 report single-point relative L2 values without standard deviations or confidence intervals. Since Zebra uses stochastic sampling (even at τ=0.1), and baselines may have their own variability from gradient-based adaptation, reporting variance across multiple runs would strengthen the comparison and help assess statistical significance of the observed differences.

### Trivial

- The MPP[3] row in Table 3 is presented without a footnote or explicit caveat in the table itself. The surrounding text (line 261) does explain that MPP[3] degrades because it was pretrained on 3 frames and tested on 2—so this is not a misleading comparison. However, to prevent a skimming reader from misinterpreting the table, a brief footnote or notation like "†" next to MPP[3] clarifying "pretrained with 3 frames" would be helpful.

## Nice-to-Haves

- A compute/efficiency comparison (e.g., wall-clock time or FLOPs) between Zebra's single forward pass and the gradient-based adaptation of CODA/CAPE would quantify the practical benefit of not requiring gradient updates.
- An ablation of VQ-VAE codebook size and spatial compression ratio's effect on downstream transformer performance would help readers understand the representational trade-offs.
- A discussion of why Zebra underperforms MPP[2] on the Heat equation specifically would provide useful insight into the method's limitations.

## Removed Points

- **"Unfair baseline comparison with MPP[3]":** Removed as a misunderstanding. The paper explicitly explains (line 261) that MPP[3] was pretrained on 3 frames and tested on 2, causing degradation; the row is included to illustrate the inflexibility of fixed-frame methods, not as a head-to-head performance comparison. The fair baseline (MPP[2]) is included alongside it. The paper is transparent about this.
- **"No discussion of max sequence length / VQ-VAE details in main text":** Removed as a scope issue. The cited paper clarifies nmax=6 and m=9 (line 113), and further architectural details are deferred to the appendix (which the parser may have stripped). This is standard practice.
- **"Missing related works":** Removed per instructions — I cannot verify the existence of specific missing citations without external sources.
- **"Formatting and grammar nitpicks":** Removed per instructions.
- **"Reproducibility concerns about undisclosed hyperparameters":** Removed — the paper provides architectural pointers (Llama architecture, Appendix reference) which is standard for this venue.
- **Strength Finder's generic strengths filtered**: Removed strengths that were generic (e.g., "addressed an important problem") and kept only those with specific evidence citations.

## Novel Insights

The reviews surface one genuinely useful structural observation: the paper's flexibility argument (variable-length contexts, no gradient updates) is its strongest differentiator, and this is best evidenced by the 2D results where gradient-based methods simply fail. However, the paper's main results tables (Tables 2 and 3) bury this narrative somewhat by presenting all datasets in a flat comparison without highlighting the cases where baselines diverge. The most persuasive framing would lead with the 2D results and the zero-shot → one-shot improvement (Figure 3) as the headline evidence, then present the 1D results as additional support. None of the individual reviews articulate this re-framing clearly.

Beyond the paper's own contributions, no fundamentally novel insights emerge from the reviews.

## Suggestions

1. **Clarify the Wave-b testing protocol explicitly.** Add a sentence or footnote: e.g., "For Wave-b, since only 4 boundary-condition environments exist, we train on 3 and test on 1 (unseen) environment. The 12 test environments mentioned for 1D datasets apply to the other four datasets (Advection, Heat, Burgers, Combined)."

2. **Tone down the "first" claims.** Replace "first successful application of generative modeling using quantized representations of physical systems" with a more precise claim like "first in-context pretraining approach for parametric PDEs." The latter is novel enough and defensible.

3. **Fill the Limitations section.** Include discussion of: VQ-VAE reconstruction loss effects, the 10-sample limitation for calibration, the types of PDEs not tested (e.g., stiff or chaotic systems), and the pretraining cost.

4. **Add error bars to main tables** (at least a small number of repeated runs) to ground the comparisons.

5. **Add a footnote to MPP[3] in Table 3** clarifying "pretrained on 3 frames" to prevent misinterpretation.

## Score and Decision

**Overall assessment:** The paper presents a genuinely novel application of in-context pretraining to parametric PDE solving. The method is well-motivated, the architecture is sound, and the empirical evaluation is reasonably thorough (7 datasets, 2 settings). The core claims—flexible conditioning without gradient updates, strong results on 2D problems, uncertainty quantification—are well-supported. The weaknesses identified are clarifications and presentation improvements, not structural flaws that undermine the contribution.

**Originality:** Good. ICP for parametric PDEs is novel.
**Importance:** Good. Solving parametric PDEs without gradient adaptation is practically valuable.
**Claim support:** Adequate. Competitively supported with room for methodological tightening.
**Soundness:** Adequate. No fatal errors, but a few ambiguities and missing details.
**Clarity:** Good. Well-written overall, with minor ambiguities.
**Value to community:** Positive. The approach opens a new direction for physics ML.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>