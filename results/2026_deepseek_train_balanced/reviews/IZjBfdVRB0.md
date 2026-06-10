Now let me produce the final review.

## Summary

The paper proposes C³A (Circular Convolution Adaptation), a PEFT method that replaces LoRA's low-rank matrix decomposition with circular convolution (equivalently, circulant matrices) to model delta weights during fine-tuning. By leveraging FFT for efficient computation, C³A decouples the rank of the delta matrix from the number of trainable parameters — unlike LoRA where rank *r* directly caps both. A block-circular extension handles non-square weight matrices and provides control over parameter count. Experiments span GLUE (RoBERTa), instruction tuning (LLaMA2/3), and image classification (ViT).

## Strengths

- **Disentangling delta-matrix rank from parameter count**: The paper formally establishes (Sections 3.2, 3.4) that C³A's circulant matrix can achieve rank up to *d* (full rank) regardless of parameter count, whereas LoRA's rank *r* directly constrains both. The formula rank(𝒞(Δ𝐰)) = *d* − Deg(gcd(*f*(*x*), *x^d*−1)) provides a theoretical upper bound of *d* that is not linearly tied to the *d₁d₂/b* learnable parameters. This is a genuine conceptual advance over LoRA.

- **FFT-based computation keeps efficiency competitive**: Sections 3.2–3.3 derive that both forward and backward passes reduce to FFT operations (O(*n* log *n*)) via diagonalization of the circulant matrix. The commutativity property 𝒞(Δ𝐰)𝐱 = 𝒞(𝐱)Δ𝐰 is exploited so that ∂ℒ/∂Δ𝐰 also takes the form of a circular convolution (Equation 7), keeping backpropagation within the same efficient FFT framework — unlike VeRA which achieves high rank at prohibitive O(*rᵥ*(*d₁*+*d₂*)) time.

- **Clean synthetic experiment demonstrating expressiveness advantage**: The controlled experiment (Section 4.1, Figure 2) directly demonstrates C³A overcoming LoRA's fundamental limitation: a circulant layer with the same parameter count as LoRA_{*r*=1} achieves perfect 8-way classification where LoRA_{*r*=1} fails, matching a full-rank standard linear layer. This isolates the expressiveness benefit of the circulant structure from confounding factors present in downstream evaluations.

- **Block-circular extension is principled and practical**: Section 3.4 generalizes circular convolution to non-square weight matrices (e.g., LLaMA3-8B's 4096×1024 layers) and provides fine-grained control over parameter count via block size *b*, solving two limitations that would otherwise prevent application to modern LLM architectures. The parameter count formula *d₁d₂/b* cleanly separates rank from parameter count.

- **Multi-domain evaluation**: The paper validates C³A on RoBERTa-Base/Large (GLUE), LLaMA2-7B/13B, LLaMA3-8B (instruction tuning), and ViT-Base/Large (image classification across 6 datasets), providing breadth of evidence that the approach transfers across architectures and modalities.

## Weaknesses

### Fatal
None.

### Major

1. **No statistical significance or variance reported for any result.** Every result is described as if from a single run. Given the well-known sensitivity of PEFT methods to random seeds, learning rates, and initialization, the absence of error bars, confidence intervals, or multi-seed averages makes it impossible to determine whether reported differences between methods are meaningful or simply noise. This is a significant gap for a top-venue submission.

2. **The *b* value (block size) for C³A is not specified in the instruction tuning experiments (Section 4.3), nor in the image classification experiments (Section 4.4).** The paper states "C³A only utilizes less than half of the parameter count compared to LoRA" (instruction tuning) and "comparable performance to LoRA while utilizing only half of the parameter count" (image classification), but does not state what *b* was used for C³A in either setting. Since the paper's central practical claim is that C³A achieves better-or-comparable performance at lower parameter counts, these omissions make the claims unverifiable. All experimental configurations should report exact *b* values and corresponding parameter counts.

### Minor

3. **No ablation study on block size *b*.** The block size *b* is the core hyperparameter controlling the parameter-efficiency trade-off, but the paper does not study how performance varies with *b*. Does the rank of the learned delta matrix correlate with downstream performance? Is there a "sweet spot" for *b* across tasks? Without this, the reader cannot understand how to choose *b* for a new task, limiting practical utility.

4. **Missing DoRA baseline.** DoRA (Liu et al., 2024) is cited in related work as a significant LoRA variant but is not included as a baseline in any experiment. Since LoRA is the primary point of comparison and DoRA is widely used, its omission weakens the empirical comparison.

5. **Single epoch for instruction tuning (Section 4.3).** All instruction tuning experiments use only a single pass over the dataset. This is unusually short for instruction tuning and raises questions about whether results generalize to the standard multi-epoch setting, or whether C³A's advantage would persist with longer training.

6. **The "full rank = maximal capacity" framing overstates the benefit.** The paper states "nearly all circulant delta matrices discovered by C³A are full rank, indicating maximal capacity... providing theoretical support for the impressive results" without addressing whether full rank could lead to overfitting in the low-data regime (the very reason PEFT methods constrain the delta matrix). The rank advantage is strongest when interpreted as "rank is not artificially capped by parameter count" — the current wording reads as if full rank is unconditionally beneficial, which is not established.

7. **The notation "*b*=768/6" is used in results but never explained in the method section.** The method section defines *b* as block size, but the notation "*b*=768/6" (which apparently means *b* = 768/6 = 128) is not defined. A reader encountering C³A_{*b*=768/6} cannot decode what parameter count this implies without reverse-engineering. This should be replaced with explicit block sizes or the convention should be explained.

8. **Hyperparameter search for GLUE experiments is underspecified.** The paper states shared hyperparameters are "found by hyperparameter search" without specifying the search space, method (grid/random/Bayesian), or budget. Since baseline hyperparameters are taken "as suggested in the original papers" — potentially without the same tuning effort — this asymmetry could confound the comparison.

### Trivial
None.

## Nice-to-Haves

- An ablation showing empirical rank (or singular-value decay) of C³A delta matrices across layers, tasks, and *b* values would directly support the central argument.
- Wall-clock time or FLOP comparisons for actual training runs would ground efficiency claims beyond asymptotic complexity.
- A comparison with LoRA at matched parameter budgets (not just default *r* values) would more directly test the expressiveness advantage.
- A study of whether the circulant structure's inductive bias provides meaningful regularization in the low-data regime (addressing the overfitting concern raised in Weakness #6).

## Removed Points

These points were removed from consideration; treat them with caution:

- **"Missing tables via \input{} commands" (Harsh Critic #1)**: The tables are included in the original submission via LaTeX \input{} commands; their absence in the extracted text is a parser artifact, not an author error. Per meta-review instructions, parser-formatting criticisms are removed.
- **"Complexity analysis appears incorrect" (Harsh Critic #2)**: The paper's formula O((*d₁*+*d₂*)log *b* + *d₁d₂/b*) is correct when FFT of input blocks (𝐱ⱼ) is shared across all output blocks — a standard optimization. The harsh critic's counter-calculation (O((*d₁d₂/b*) log *b*)) assumed independent FFTs per block pair, which would be a naive, unoptimized implementation. The formula does not need correction, though the paper could be more explicit about computation sharing.
- **"LoRA_{r=1} is a weak baseline" (regarding synthetic experiment)**: The synthetic experiment uses LoRA_{*r*=1} because it matches C³A's parameter count at that setting. The experiment is designed to show that with identical parameter budgets, the circulant structure is more expressive — this is precisely the right comparison for the claim being made. A higher-*r* LoRA would have more parameters, breaking the controlled comparison.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Report all results with standard deviations across at least 3 random seeds.
- Specify exact *b* values and corresponding parameter counts for every experiment (instruction tuning, image classification, and GLUE).
- Add an ablation study showing performance as a function of *b* (or parameter count), and include DoRA as a baseline.
- Clarify the "b=768/6" notation in the method section — either replace with explicit block sizes or explain the convention.
- Add a brief discussion of whether the full-rank property could cause overfitting in low-data regimes and how the circulant structure's inductive bias may provide regularization.
- Report wall-clock time comparisons to ground efficiency claims empirically.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>