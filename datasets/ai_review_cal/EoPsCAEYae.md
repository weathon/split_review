- Decision: Reject
- Avg Score: 3.80
- Scores: 5, 3, 3, 5, 3
Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

HyperLLaVA introduces a dynamic tuning strategy for Multimodal Large Language Models (MLLMs) by equipping the projector and LLM with visual and language experts whose parameters are generated on-the-fly by HyperNetworks conditioned on input features. The method replaces the static parameter paradigm of LLaVA with input-adaptive parameter generation for both the vision-language projector (visual expert) and the LLM blocks (language expert). Experiments on 12 benchmarks show HyperLLaVA outperforms LLaVA-1.5 on 11 of them, with ablation studies confirming the contribution of each expert component.

## Strengths

1. **Strong and broadly consistent empirical results.** HyperLLaVA (7B and 13B) outperforms LLaVA-1.5 on 11 out of 12 diverse benchmarks spanning VQA, knowledge-based QA, scene text understanding, and multimodal benchmarks, while also beating larger models like 80B IDEFICS. This provides direct evidence that the dynamic tuning paradigm benefits multimodal task performance.

2. **Clean ablations isolating component contributions.** The paper quantifies that removing the visual expert drops mean accuracy by 2.61% and removing the language expert drops it by 0.94% (Section 4.3, referring to Table 1 rows 11–13). This empirically validates that both experts contribute positively and that the gains are not driven by a single component.

3. **Systematic analysis of design choices.** The paper investigates multiple design dimensions: three alternatives for visual expert placement (Eq. 5), different blocks for language expert insertion (anterior 16, all 32, posterior 16), expert structure comparisons (MLP vs. adapter vs. HyperNetwork+Adapter vs. proposed), and dimension sensitivity (Figure 5). These analyses give practical guidance beyond the core claim.

4. **Object hallucination improvements.** HyperLLaVA achieves the best POPE scores (accuracy, precision, recall, F1) among compared methods including LLaVA (Table 6), with a balanced "yes ratio" suggesting reduced hallucination behavior—a known pain point for MLLMs.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Abstract vs. experimental text inconsistency on MME.** The abstract states that HyperLLaVA "significantly surpasses LLaVA on existing MLLM benchmarks, **including MME**" (line 10), but Section 4.2 explicitly says "Except for the MME benchmark" (line 222). Whether or not the abstract intends "including" to list evaluated benchmarks rather than outperformed ones, the phrasing creates a direct contradiction with the later caveat and should be corrected. The paper also provides no analysis of *why* MME is the exception—a gap that weakens the generality narrative given that MME is a multi-task benchmark where dynamic tuning should in principle excel.

2. **No variance or uncertainty information.** All results are reported as single point estimates with no standard deviations, confidence intervals, or significance tests, despite the abstract using the word "significantly" (line 10). The reported ablation gaps are small in absolute terms (e.g., 0.94% for the language expert), and without variance estimates the reader cannot assess whether these gaps are reproducible. While single-run evaluation is common practice in large-scale MLLM benchmarking due to computational cost, the paper should at minimum avoid causal language like "significantly" and could include variance from a small number of runs (e.g., 3 seeds) for the core comparison.

3. **"Parameter-efficient" claim is not substantiated with concrete numbers.** The paper describes the visual and language experts as "parameter-efficient" (abstract, contributions, Section 4.5, conclusion) but never reports the exact number of added trainable parameters, the total parameter count versus baseline LLaVA, or the memory/inference overhead. Since LLaVA-1.5 already fine-tunes the full LLM in stage 2 (7B/13B parameters), the adapter-based experts add parameters on top of full fine-tuning—the paper should clarify the magnitude of these additions. A simple table of trainable parameter counts for baseline vs. HyperLLaVA would turn an asserted claim into a verifiable one.

### Trivial

1. **SwiGLU is misidentified as GeLU.** Line 163 states: "SwiGLU... is the activation function, Gaussian Error Linear Unit." SwiGLU and GELU are different functions (SwiGLU = Swish(Wx) ⊗ (Vx) is a gated variant; GELU = xΦ(x) is not gated). The paper uses SwiGLU in its forward equations (Eq. 4, Eq. 6), which is a valid design choice, but the description in line 163 is technically incorrect.

## Nice-to-Haves

- **MME sub-task breakdown.** A per-category analysis of MME performance would clarify whether the method helps or hurts on specific perceptual/cognitive sub-tasks, and could reveal boundary conditions for dynamic tuning.
- **Wall-clock inference overhead.** The dynamic parameter generation (HyperNetwork forward pass per input) adds latency. Reporting tokens-per-second or time-per-sample for both LLaVA and HyperLLaVA would help practitioners evaluate the trade-off.
- **Visualization of generated parameters.** A t-SNE or PCA plot of the generated adapter weights across different inputs/tasks would concretely illustrate the "unique parameters for every input" claim.
- **Limitations section.** A brief paragraph acknowledging that the dynamic mechanism may not benefit all tasks (MME) and adds computational overhead would strengthen the paper's completeness.

## Removed Points

- **Criticism that "static tuning constrains performance" conflates issues.** This is a conceptual nitpick about framing; the paper's motivation is sufficiently clear, and the claim is reasonable.
- **Related work described as "perfunctory" / lacking positioning against conditional adapters.** The paper covers relevant work (HyperNetworks, adapters, MLLMs). A more extensive review would be nice but is not a weakness.
- **"No direct reference or experiment showing vanilla HyperNetwork fails on projector."** Table 5 (expert structure ablation) empirically compares different variants including vanilla HyperNetwork; this criticism is invalid.
- **"z^{(n)} notation dropped without explanation."** The paper explicitly explains the transition: "replacing the learned latent vector z with specific input" (lines 133–134). The criticism misreads the paper.
- **"Choice of 1st visual expert not justified conceptually."** It is justified empirically via Table 5, which is standard practice for an empirical paper.
- **"x_L definition is vague."** Line 194 defines it: "features generated from RMS normalization and self-attention in LLM's block." This is sufficiently clear for an LLM architecture description.
- **Code/reproducibility details about dimensions of e^{(n)}, number of HyperNetwork layers.** The paper provides optimizer settings, batch sizes, learning rates, and training data composition—a standard level of detail for a conference paper. Exact dimensions are partially addressed via the dimension analysis (Figure 5).
- **Formatting/style nitpicks** and parser artifacts.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a useful empirical observation—that the MME exception may reveal a boundary condition for input-adaptive parameters—but this is a gap the paper itself should address, not a novel insight from the reviews.

## Suggestions

1. Fix the abstract-to-experiment contradiction: either remove MME from the list in the abstract or add a qualifier (e.g., "including MME, where performance is maintained").
2. Add a small table reporting trainable parameter counts for baseline LLaVA vs. HyperLLaVA (total and added) to substantiate the "parameter-efficient" claim.
3. For the main result table, report mean ± std over 3 runs with different random seeds for the core comparison (HyperLLaVA vs. LLaVA-1.5) on at least 2–3 representative benchmarks.
4. Correct line 163 to accurately describe SwiGLU (or simply cite it without equating it to GELU).
5. Add a brief discussion of the MME exception—even a sentence hypothesizing why dynamic tuning may not benefit that particular benchmark would address the gap.
