- Decision: Reject
- Avg Score: 5.67
- Scores: 3, 6, 8
I have now carefully read the paper. Let me verify each reviewer claim against the actual paper text before writing the review.

---

## Verified Findings

**Claim check: "Algorithms 1 and 2 are never shown—only referenced."** The paper references "Algorithm 1" (line 115) and "Algorithm 2" (line 224). Line 121 shows an image placeholder `![](images/d21444d158cf2d8d408802e2bfe02379b88f7bdf4c717ece42aa5ef4a195cc00.jpg)` with garbled numeric content in lines 122–176 — consistent with an algorithm figure corrupted during text extraction. The algorithms exist in the original submission as figures. **This criticism is a parser artifact. REMOVED.**

**Claim check: "The method is under-specified... Section 3.2 is fragmented and contains broken sentences."** Line 113 ends with an orphaned "Since" — this is in the running text, not from a figure. The prose transitions between subsections (inverting masked models → noise injection → inverting multinomial diffusion) are abrupt. **Partially valid — the prose is fragmented, but the core equations (z_t = y_0 − ŷ_{0|t} at lines 179–180, and the three injection strategies at lines 182–206) are present. KEPT as a minor weakness.**

**Claim check: "Strawman baselines."** The paper acknowledges at line 268: "Since there is no discrete diffusion inversion exists, we compare our method with masked generation." The reconstruction baseline (masked inpainting = replace all tokens randomly) is showing what happens without any inversion — it's a "before" comparison, not a competitor. For editing (Table 2), the comparison to continuous methods (SD+DDIM) is valid as those are alternative approaches to the same task. **The criticism is overblown. The paper correctly identifies the lack of prior discrete inversion work. However, adding an adapted continuous-to-discrete baseline would strengthen the evaluation. KEPT as a minor weakness (not major).**

**Claim check: "Mask-free claim contradicts masked evaluation."** The paper says the method works "without the need for predefined masks" (abstract, line 4). The editing evaluation (lines 270–271) uses "annotated editing mask" from PIE-Bench to compute background preservation metrics (PSNR, LPIPS, etc. outside the mask). This is standard practice — the method does not require user-provided masks as input; the evaluation uses ground-truth masks from the benchmark to compute metrics. **No contradiction exists. REMOVED as a misunderstanding, but noted as a minor clarity issue.**

**Claim check: "Theoretical analysis disconnected."** Section 3.3 (lines 231–239) computes mutual information for a continuous Gaussian DDPM and acknowledges this in the first sentence ("prototypical example"). The paper uses this to motivate scheduling strategies. The connection to discrete models is acknowledged as loose even by the authors (future work, line 320). **Valid but minor — the paper is transparent about the limitation. KEPT as minor.**

**Claim check: "Text experiments shallow; RoBERTa claims overblown."** The contributions list (line 77) claims the approach can "transform a model primarily trained for understanding tasks, such as RoBERTa, into a **competitive** generative model." The evidence is: reconstruction hit rate (Table 4) and sentiment editing on a single synthetic dataset evaluated by ChatGPT (Table 5). There is no comparison to any actual text generation model (no GPT, BART, T5), no perplexity, no diversity, no fluency metrics. **VALID — this is a significant overclaim. KEPT as major.**

Now let me write the final review.

---

## Summary
2-3 sentence summary of the paper's contribution.

The paper proposes Discrete Inversion, the first extension of stochastic inversion (DDPM Inversion) to discrete diffusion models, including multinomial diffusion and masked generative models. The core idea is to use the Gumbel-Max trick to record residuals (z_t) between predictions and targets during the forward process, then inject these residuals during reverse sampling to enable reconstruction and controlled editing. Experiments on image models (Paella, VQ-Diffusion) and a text model (RoBERTa) demonstrate the feasibility of the approach.

## Strengths

1. **First inversion method for discrete diffusion** — The paper addresses a genuine gap: existing inversion techniques (DDIM inversion, DDPM inversion) operate in continuous spaces, and no prior work has extended inversion to discrete diffusion models. The Gumbel-Max trick is a principled way to port the residual-recording idea from continuous SDE-based inversion to the discrete setting (Section 3.2, lines 111–112).

2. **Near-perfect reconstruction validated empirically** — Table 1 reports PSNR = inf, LPIPS = 0.0, MSE = 0.0, SSIM = 1.0 for both Paella and VQ-Diffusion, demonstrating exact reconstruction after the VQ-VAE pipeline. This is non-trivial because it requires the residuals to capture the full information of the input, and the ablation confirms the recorded z_t indeed carries that information.

3. **Better structural preservation than continuous diffusion editing** — Table 2 shows Discrete Inversion with Paella achieves the lowest structure distance (11.34) compared to DDIM+SD1.4 methods (13.10–14.90), while maintaining competitive CLIP similarity. This is a concrete advantage over continuous approaches on the specific axis of structural fidelity, which is directly relevant to the paper's claims about controlled editing.

4. **Repurposing a non-generative LM for text editing** — Using RoBERTa (a masked language model not trained for generation), Discrete Inversion achieves 0.88 reconstruction hit rate vs. 0.17 for masked generation (Table 4), and 0.93 structure preservation in sentiment editing (Table 5). While the scope of the text experiments is limited, the concept of inverting a BERT-style model for controlled editing is novel.

## Weaknesses

### Fatal
None.

### Major

1. **Overclaim about RoBERTa becoming a "competitive generative model"** — The contributions list (line 77) states the approach can "transform a model primarily trained for understanding tasks, such as RoBERTa, into a competitive generative model for text generation and editing." The evidence does not support this. The text experiments consist solely of (a) reconstruction hit rate on a single synthetic dataset and (b) sentiment editing evaluated by ChatGPT with no comparison to any actual text generation model (GPT, BART, T5, or any fine-tuned seq2seq model). No perplexity, diversity, fluency, or human evaluation is reported. The term "competitive generative model" implies performance competitive with dedicated generative systems, which has not been demonstrated. This claim should be substantially toned down to match what was actually shown: that inversion residuals enable a masked LM to perform controlled editing.

2. **Limited text evaluation scope** — Beyond the overclaim issue, the text experiments are shallow even as a proof of concept. The dataset is described only in the supplementary materials (line 294: "please refer to supplementary materials"), the evaluation uses a single classifier (ChatGPT-4) without discussion of its reliability or bias, and the baseline (masked generation) is a "without inversion" ablation rather than a competitive alternative. For a paper claiming to advance "text generation and editing," this is insufficient. At minimum, the main paper should describe the dataset size and construction, and comparisons should include at least one existing editing approach.

### Minor

1. **Fragmented presentation of the core method** — Section 3.2 (Discrete Inversion) contains an orphaned sentence fragment ("Since... Since" at line 113) and transitions abruptly between subsections on masked generative models, noise injection strategies, and multinomial diffusion. While the key equations (z_t definition at lines 179–180, injection strategies at lines 182–206) are present, the narrative flow does not clearly walk the reader through the inversion algorithm step by step. This is the central technical section of a methods paper, and the exposition needs to be more coherent. The algorithms appear to be relegated to figures (which were corrupted during parsing), but the prose alone should enable a reader to understand the procedure.

2. **Theoretical analysis (Section 3.3) does not directly address the discrete case** — The mutual information analysis in Section 3.3 is explicitly for a continuous Gaussian DDPM (Remark 3.1, line 233), not for the discrete models the paper studies. The paper acknowledges this as a "prototypical example" and mentions it "motivates" scheduling strategies, but the section does not contribute analysis for the discrete setting. This is not a fatal issue (the paper is honest about the limitation and flags it as future work), but it weakens the theoretical grounding of the main contribution.

3. **Ablation on control parameters (λ₁, λ₂, τ) is missing** — The paper introduces λ₁ (information injection strength), λ₂ (random noise strength), and τ (starting timestep) as knobs for control (line 119) but reports results for only a single configuration. A plot showing structure distance vs. CLIP similarity as these parameters vary would convincingly demonstrate the claimed controllability and help users understand the trade-off landscape.

4. **"No mask needed" framing could mislead readers** — The paper repeatedly states the method works "without the need for predefined masks" (abstract, lines 4, 68, 320). This is true in the sense that the method does not require a mask as user input. However, the editing evaluation (Table 2) relies on ground-truth masks from PIE-Bench to compute background preservation metrics. The paper should clarify this distinction more explicitly to prevent the impression that masks play no role at all.

### Trivial
None.

## Nice-to-Haves

- **Continuous-to-discrete adaptation baseline**: For image editing, compare against DDIM inversion applied to the continuous VQ-VAE latent space before discretization, to isolate the benefit of performing inversion in the discrete space itself.
- **Computational/storage cost**: Report the overhead of storing residuals for all timesteps (memory per image, time overhead for inversion), as this is a practical consideration for deployment.
- **Analyze robustness of noise injection strategies**: The paper notes the linear strategy works best (line 206) but does not quantify the differences between linear, variance-preserving, and max strategies across metrics.

## Removed Points

These points were flagged for removal; treat them with caution.

- **"Algorithms 1 and 2 are never shown"** — The algorithms were likely present as figures in the original submission and were corrupted during text extraction (image placeholder at line 121). This is a parser artifact, not a missing contribution.
- **"Baselines are strawmen"** (in the strong sense of being unfair or invalid) — The paper correctly identifies that no prior discrete inversion methods exist (line 268) and compares against the closest available alternatives. The reconstruction baseline (masked generation) is an ablation showing what happens without inversion, which is meaningful. The criticism about comparing continuous and discrete models is valid as a scope note but does not constitute a strawman comparison.
- **"Mask-free claim contradicts experimental setup"** — The method does not require user-provided masks as input. The evaluation uses ground-truth masks from a benchmark to compute standard metrics. This is standard practice and not a contradiction. A minor clarity issue remains (kept above).
- **"The paper should cite YAGO, BAGEL text benchmarks"** — Cannot verify these exist; treating as speculative.
- **"The theoretical section should be removed"** — The section is transparent about its scope limitation and serves as motivation. Keeping it is reasonable.
- **Formatting/style nitpicks about garbled text, missing appendix content** — These are parser artifacts.

## Novel Insights

The core observation that the Gumbel-Max trick can serve as the discrete analogue of the Gaussian reparameterization trick for inversion is the paper's most interesting contribution. This connection is not obvious and opens up a clear path for future work: any model that samples from a categorical distribution via perturbation arguments (Gumbel-Softmax, concrete distributions) can, in principle, be inverted by recording the perturbation residuals. This unifies the continuous and discrete inversion stories under a single conceptual framework (record the random noise that turns a deterministic prediction into a sample), which the paper touches on but does not fully develop into a general principle.

## Suggestions

1. **Rewrite Section 3.2** with a clear step-by-step narrative: (a) forward trajectory construction, (b) residual recording via Gumbel-Max, (c) reverse process with injected residuals. Move algorithm pseudocode into the main paper body (not just figures). Fix the broken "Since" sentence.
2. **Tone down the RoBERTa claim**: Replace "competitive generative model" with something like "demonstrates that a masked language model can be repurposed for controlled text editing via inversion residuals."
3. **Add an ablation plot** varying λ₁, λ₂, and τ to show the controllability trade-off (structure distance vs. CLIP similarity).
4. **Expand text evaluation** to include at least one comparison method (e.g., prompt-based editing with an LLM) and basic quality metrics (perplexity, diversity). Describe the dataset in the main paper.
5. **Acknowledge the evaluation's use of masks explicitly** in the abstract/introduction to avoid the impression of contradiction.
