- Decision: Reject
- Avg Score: 3.50
- Scores: 1, 5, 5, 3
Now I have a thorough understanding of the paper and all the reviewer claims. Let me write the consolidated review.

## Summary

The paper proposes DP-ZeRO, a system that integrates differential privacy (DP) into the ZeRO distributed optimizer, enabling DP training of models up to 100B parameters with throughput and memory efficiency matching standard (non-DP) ZeRO. The technical contributions include: (1) extending ZeRO's model state partitioning to support per-sample gradient clipping and noising, (2) identifying and analyzing a fundamental incompatibility between mixed-precision loss scaling and DP gradient clipping, and (3) demonstrating that DP-ZeRO achieves >95% of ZeRO's throughput at scale (256 GPUs, 26B-parameter models).

## Strengths

- **DP-ZeRO matches ZeRO efficiency at unprecedented scale**: Figure 7 (scalability experiments) shows that on 256 GPUs training a 26B-parameter model, DP-ZeRO achieves >95% of standard ZeRO's throughput across model sizes from 7B to 26B. At these scales, prior DP distributed methods (DDP, pipeline parallelism) either cannot fit the model or suffer 2–9× slowdowns. This directly supports the primary claim of "same computation and communication efficiency as the standard ZeRO" at scales where no prior DP solution existed.

- **Enables DP optimization at model sizes previously impossible**: Figure 1 shows existing DP models top out around 800M parameters (GPT-2 Large, ViT-Huge), while DP-ZeRO supports ViT-Gigantic (1.84B), GPT2-XL (1.56B), ViT-10B, and GPT-100B. This is a qualitative leap in the scale of models that can be trained with DP, enabled by the algorithmic integration of ZeRO's model partitioning with DP's per-sample gradient computations.

- **Identifies a genuine practical issue with mixed-precision DP training**: Section 3.4 and Table 3 give a clear, step-by-step analysis of why standard loss scaling (typical in fp16 training) causes overflow in per-sample gradient norms or underflow in final parameter gradients when combined with DP clipping. The analysis is conceptually sound and backed by an accuracy comparison on ViT-Large/CIFAR100 (Figure 6). This is a practical barrier that prior DP libraries (Opacus, GhostClip) did not address.

- **Detailed time complexity decomposition**: Table 2 breaks down the per-iteration time into forward, backward (output grad, param grad, DP clip/noise), and communication components, with the DP-specific overhead quantified as ~0.666·BT·Ψ_train. Equation (1) then expresses relative speed as a ratio, explaining why DP-ZeRO's overhead shrinks as communication or other costs dominate — a useful analytical contribution.

- **Robust across architectures, ZeRO stages, and precision formats**: Figures 4 and 6 demonstrate consistent efficiency on ViT-Gigantic, ResNet152, and GPT2-XL across ZeRO stages 1/2/3 and fp32/fp16 formats, with the gap narrowing from ~83% (ZeRO1) to 95–97% (ZeRO3).

## Weaknesses

### Fatal
None.

### Major

- **The paper claims to "train" billion-parameter models with DP but provides no validation of training outcomes.** The title, abstract, and contribution list (Contribution 3: "we are the first to train the full GPT2-XL, ViT-Gigantic, ViT-10B and GPT-100B with DP") strongly imply that DP-ZeRO produces usable models. Yet every experiment measures only system metrics — throughput and memory — not whether DP-ZeRO actually produces models with reasonable accuracy, loss curves, or convergence behavior. There is no training loss curve, no validation accuracy, no comparison of DP-trained model quality to a known baseline. This matters because distributed training introduces subtleties (gradient partitioning across GPUs, accumulation over micro-batches, per-sample norm computation in sharded settings) that could silently alter the DP algorithm. While this weakness does not invalidate the core systems efficiency results (which are genuine), it creates a gap between the paper's claims and its evidence. The authors should either (a) validate DP-ZeRO on a moderately large model (e.g., GPT2-XL or ViT-Gigantic) against known single-GPU DP accuracy at a given privacy budget, or (b) reframe the claims more narrowly as enabling the *efficient distributed execution* of DP optimization at scale, not as training models with demonstrated utility.

### Minor

- **The mixed-precision loss scaling analysis, while conceptually sound, rests on thin empirical evidence.** Section 3.4 argues that DP mixed-precision training "must not use loss scaling" — a strong prescriptive recommendation. This is supported by a conceptual table (Table 3) and one experiment on ViT-Large/CIFAR100. The analysis is plausible and the reasoning (per-sample gradient clipping already provides scaling; loss scaling causes overflow or underflow through the interaction with clipping factors) is well explained. However, a single architecture/dataset combination and a single loss scale value (10³) is insufficient to establish a universal "must not." A sweep over loss scales on a few diverse architectures (e.g., a GPT-style model and a ResNet) would substantially strengthen the practical utility of this claim. As it stands, the evidence is suggestive but not conclusive for the strength of the prescription.

- **Scalability results lack absolute throughput numbers.** The paper reports only the ratio (DP-ZeRO throughput / standard ZeRO throughput). While this ratio is the right metric for the paper's main claim (comparable efficiency), reporting absolute samples/second or seconds/iteration would allow readers to compare against prior DP distributed work and make the contribution more concrete. This is particularly relevant for the large-scale experiments (256 GPUs, 26B model) where the absolute numbers would be most informative.

### Trivial
None.

## Nice-to-Haves
- A comparison of DP-ZeRO against DP-DDP (Opacus or similar) on a model that fits in one GPU (e.g., ResNet50 or GPT2-small) would quantitatively calibrate the overhead of ZeRO's sharding relative to data-parallel DP, strengthening the motivation.
- The mixed-precision analysis would benefit from a plot of accuracy vs. loss scale on 2–3 architectures beyond ViT-Large/CIFAR100.

## Removed Points

- **"No error bars / statistical variance for throughput measurements"** — Systems throughput benchmarks at this scale are standardly reported as single runs; absence of error bars is not a meaningful weakness.
- **"Hyperparameters deferred to appendix"** — The paper explicitly states "We leave the experimental details in \Cref{app:settings}." The appendix is stripped by the PDF parser; this is a formatting artifact, not a paper flaw.
- **"No comparison to DP-PipeP"** — The paper already addresses this: "We cannot compare to DP-PipeP... because the codebase and experiment details... are not publicly available." This is a genuine external constraint, not an author omission.
- **"Scalability experiments don't specify whether measurements include noise addition"** — The algorithm description (Section 3) explicitly includes DP noise and clipping in the backward pass decomposition ("backward = output gradient → clipping factor → parameter gradient → noising"), so these operations are included in the system measurements.
- **"Time efficiency analysis doesn't report absolute times"** — Already covered in the Minor weakness above. The reviewer's framing as a separate omission is redundant.
- **Criticisms about missing absolute throughput numbers — merged into Minor weakness above (not a separate point).**
- **Strength Finder's generic praise ("this paper addressed an important problem")** — Dropped; only concrete, evidence-grounded strengths are retained.

## Novel Insights

The most interesting observation that emerges from the reviews — beyond the paper's own contributions — is the tension between the systems contribution and the validation standard. The paper's efficiency claims are strong and well-supported, yet the language used throughout (especially "train the full GPT2-XL... with DP") sets an expectation of model-level validation that the experiments do not meet. This gap illuminates a broader challenge in the DP systems literature: papers that enable DP training at scale are often evaluated purely on system metrics, but the DP community typically expects validation that the privacy-accuracy tradeoff is preserved. Resolving this tension — either by adding model-level validation or by calibrating the claim language — would significantly strengthen the paper.

## Suggestions

1. **Add a concrete DP training validation**: Train a model like GPT2-XL (1.56B) or ViT-Gigantic (1.84B) with DP-ZeRO on a standard benchmark (e.g., E2E for GPT or ImageNet for ViT) and report accuracy/loss curves at a known privacy budget (e.g., ε=8). Compare to published single-GPU DP results for the same model to confirm the distributed version matches within the noise. This single addition would validate the entire "learning" framing.

2. **Soften or remove the "must not" language in the loss scaling claim**: Replace "must not use loss scaling" with a more cautious recommendation like "should generally avoid" or "we recommend against," since the evidence is limited to one architecture.

3. **Include absolute throughput numbers** (samples/sec or seconds/iteration) alongside the relative ratios, especially for the large-scale experiments, to enable direct comparison with future work.

4. **Report the gradient numerical fidelity**: A small ablation showing that the DP gradient computed by DP-ZeRO (across partitions) is identical within floating-point tolerance to the gradient from a single-GPU reference would rule out subtle numerical errors from sharding or mixed precision.
