Now I have all the information needed. Let me construct the consolidated review.

## Summary

This paper introduces Dynamic Adapter Merging (DAM) for rehearsal-free domain-incremental VidQA learning. The approach combines a frozen large-scale video-language backbone (1.2B-parameter FrozenBiLM), sequentially trained domain-specific adapters (<5% of total parameters), a non-parametric cosine-similarity router, and instance-wise weighted merging of top-k adapters. On a benchmark of 6 VidQA datasets, DAM outperforms the best prompt-based baseline (S-Prompts) by **9.1% average accuracy** while exhibiting **1.9% less forgetting**, and generalizes to image VQA using BLIP-2 (4.1B parameters). The key insight is that dynamic merging compensates for inaccurate router predictions — the analysis in Figure 4 and Table 3 shows the benefit grows as router accuracy drops.

## Strengths

- **Novel formulation and evaluation of domain-incremental VidQA learning.** The paper is the first to systematically study rehearsal-free DIL for VidQA with large models, constructing a benchmark of 6 diverse VidQA datasets (iVQA, MSVD-QA, MSRVTT-QA, LSMDC, ActivityNet-QA, TGIF-QA). This is a realistic and previously underexplored setting, clearly motivated by the Barbie movie example.

- **Dynamic adapter merging demonstrably compensates for inaccurate router predictions.** Table 3 and Figure 4 provide well-controlled empirical evidence that merging helps most when the router is least accurate. When router accuracy is 51.0% (MSVD), merging yields +4.9% downstream accuracy; when router accuracy is 96.2% (LSMDC), the gain is only +0.2%. Figure 4 shows a 30% relative gain when router accuracy drops to 0%. This causal analysis is the paper's strongest empirical contribution.

- **Scalability to growing numbers of domains and generalization to VQA.** Figure 3 shows DAM consistently outperforms S-Prompts as the number of domains increases from 2 to 6, with normalized accuracy gaps growing from 1.7% to 4.8% on in-domain data and 2.9% to 7.1% on OOD domains. Table 4 extends DAM to image VQA with a 4.1B BLIP-2 backbone, achieving +4.8% over S-Prompts, demonstrating generality beyond video.

- **Parameter-efficient design with practical motivation.** Domain-specific adapters contain <5% of total backbone parameters, making the approach feasible for billion-parameter models. The continual weight initialization scheme is a simple yet effective mechanism grounded in model merging theory (Yadav et al., 2023; Jin et al., 2022).

## Weaknesses

### Fatal
None.

### Major

- **The Individual Fine-tune upper bound being comparable to or lower than DAM is unexplained and undermines the claim that it is a true upper bound.** According to Table 1, DAM's average accuracy (67.9%) matches or slightly exceeds the Individual Fine-tune baseline (67.7%). The paper labels this baseline as establishing the "upper bound" for continual learning — meaning a set of independently trained adapters that don't suffer from forgetting. If DAM outperforms it, then either (i) the individual adapters are undertrained (same hyperparameters, insufficient epochs), or (ii) cross-domain knowledge from merging genuinely helps, which would contradict the notion that this is an upper bound. The paper provides no discussion of this anomaly, despite it being a clear first-order question a reader would ask. At minimum, the authors need to report convergence checks, training curves, or a learning rate search for the individual fine-tune baseline. Without this, the headline 9.1% improvement over S-Prompts cannot be fully trusted, because S-Prompts itself may have been suboptimally configured relative to a properly tuned upper bound.

- **The forgetting metric is not defined and the reported "1.9% less forgetting" cannot be verified from the described evaluation protocol.** The paper states it "use[s] the average accuracy and forgetting as the evaluation metrics" citing Wang et al. (2022c,b), but never defines how forgetting is computed. It also says "evaluate the final checkpoint on all domains." Standard forgetting in CL requires evaluating each task immediately after learning it and again at the end; a single final evaluation across all domains does not capture forgetting. The paper does not describe any per-task evaluation protocol. Without this, the claim of "1.9% less forgetting" is essentially unverifiable from the text. This is fixable by clarifying the protocol or providing per-task accuracy curves, but as submitted it is a gap in the evidence.

### Minor

- **Baselines may be suboptimally configured.** The paper uses L=10 prompt tokens for all prompt-based methods (L2P, CODA-Prompt, S-Prompts) following (Wang et al., 2022b). However, CODA-Prompt's original design uses a much larger prompt pool (100+ prompts), and the paper reports no hyperparameter search (learning rate, prompt length, pool size) to verify that these methods are fairly tuned on the VidQA task. Since these methods were designed for image classification, the same prompt length may not transfer optimally to video-language QA. A small tuning study (or justification for why L=10 is appropriate) would strengthen the comparison.

- **The number of adapters per layer (N) and adapter architecture details (bottleneck dimension, placement) are not specified.** The paper writes "inject N domain-specific adapters" and "contain less than 5% of total parameters" but never states N or the adapter dimensions. This hurts reproducibility. These are small details that should be in the experimental setup.

- **Only a single fixed training order is evaluated.** The paper trains domains in the order iVQA → MSVD → MSRVTT → LSMDC → ActivityNet → TGIF. Standard CL practice includes testing at least one additional order (or random orders with multiple seeds) to verify results are not order-dependent. Without this, the 9.1% gain could partially reflect a favorable ordering.

- **The choice of k=2 over k=3 for top-k merging is not justified.** Table 3 apparently shows top-3 slightly outperforming top-2 (64.7% vs. 64.6%), yet the paper selects k=2 without explanation. The difference is tiny, but the choice appears arbitrary.

- **No wall-clock, FLOP, or inference-time comparison is provided despite the paper claiming "parameter-efficient" and "negligible computational overhead."** The paper reports <5% parameter count but does not quantify actual inference cost (latency, memory, FLOPs) for the merging operation, especially as the number of domains grows. This would help substantiate the efficiency claims.

### Trivial

- **Figure 3 reports averages over 5 runs but shows no error bars or variance.** Standard practice is to include variance visualization.
- **The paper does not include a comparison with uniform-weight merging (static averaging of all adapters)** — this would isolate the benefit of router-based weighting. (This is more of a missing ablation than a flaw.)

## Nice-to-Haves

- **Ablation on continual weight initialization vs. random initialization** for adapters. The paper claims this helps merging but provides no direct evidence.
- **Training order ablation** using at least one alternative order or random orders.
- **Qualitative examples** showing cases where the router predicts incorrectly but merging corrects the answer — would strengthen the central claim.
- **Comparison with uniform-weight adapter merging** as a lower bound to quantify the router's added value.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"Router features not aligned with adapted model"** — The router uses features from the *frozen* backbone (f(x)), not adapter-modified features. The paper's design is intentional and the criticism reflects a misunderstanding of the architecture. REMOVED.
- **"CODA-Prompt's router accuracy reported as N/A is a flaw"** — The paper explicitly explains why: "We cannot calculate CODA-Prompts' router's accuracy as it does not explicitly predict the domain identity." This is a reasonable explanation. REMOVED.
- **"Stale centroids as adapters learn"** — Centroids are computed from the frozen backbone, which does not change during adapter training. The criticism is based on a misunderstanding. REMOVED.
- **"The paper should discuss why prompt methods might not transfer to VidQA beyond domain gaps"** — The paper does discuss this: it notes that prior prompt-based methods are "tailored for image classification" and that VidQA requires "comprehend both video and language." This is adequate. WEAKENED/REMOVED.

## Novel Insights

The most valuable insight from the reviews clarifies an observation already latent in the paper but never explicitly stated: the paper's core finding — that dynamic adapter merging provides the largest gains precisely when the router is least accurate — has an interesting corollary. If the individual fine-tune upper bound is genuinely comparable to DAM, it suggests that parameter-efficient adapters may be capacity-limited enough that cross-instance merging across domains effectively *increases* model capacity beyond what a single individually-trained adapter can achieve. This would be a meaningful nuance for the continual learning community: upper bounds based on isolated fine-tuning of small modules may not be true ceilings, because merging can exploit complementary knowledge across domains. The paper should engage with this possibility rather than treating the upper bound as an unquestioned gold standard.

## Suggestions

1. **Address the Individual Fine-tune anomaly directly.** Either (a) verify that individual adapters are trained to convergence (longer training, learning rate sweep) and report the results, or (b) explicitly argue why DAM can legitimately exceed individually trained adapters (e.g., weight inheritance + cross-domain knowledge from merging effectively increases expressivity). This is the single most important fix.

2. **Define the forgetting metric explicitly** and describe the evaluation protocol (per-task evaluation after each training stage). Report per-domain forgetting numbers, not just an aggregate.

3. **Add a brief hyperparameter sensitivity study** for the prompt-based baselines (e.g., vary prompt length L in {5, 10, 20, 50} for at least one method) to demonstrate that the reported results are not artifacts of under-tuning.

4. **Report adapter architecture details** (N, bottleneck dimension, insertion points) for reproducibility.

5. **Add error bars to Figure 3** and consider including a second training order in the appendix.

## Score and Decision

The paper makes a solid contribution — it opens up a realistic new problem setting (domain-incremental VidQA with large models), proposes a clean and well-motivated method, and provides insightful analysis of when/why dynamic merging helps. The two major issues (unexplained upper bound behavior and unverifiable forgetting metric) are real and would need to be addressed, but they are fixable and do not invalidate the core contributions. The remaining concerns are minor. I recommend **acceptance** contingent on the authors addressing the major weaknesses in a revision.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>