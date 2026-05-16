Now I have a thorough understanding of the paper. Let me construct the consolidated review.

## Summary

This paper proposes MoFO (Momentum-Filtered Optimizer), a fine-tuning algorithm that updates only the parameters with the largest momentum magnitudes at each iteration, operating as a form of block coordinate descent (BCD) built on top of Adam. The key idea is that keeping parameters closer to the pretrained model during fine-tuning mitigates forgetting, and MoFO achieves this by selectively updating the most impactful parameters. The paper presents a convergence analysis of a simplified GD variant, and evaluates on instruction fine-tuning (MetaMathQA, Code-Alpaca with Llama-2-7B) and continual fine-tuning (TRACE with TinyLlama-1.1B), comparing against Full FT, HFT, L1/L2 regularization, GEM, and Replay.

## Strengths

1. **Novel and well-motivated optimization approach.** The idea of using momentum magnitude as a selection criterion for BCD is clean and non-obvious. The motivation—connecting the distance the model travels in parameter space to forgetting severity—is supported by an initial experiment comparing Adam vs. Lion on Pythia-160m, and the paper carries this thread through to the algorithm design.

2. **Ablation study convincingly validates momentum-based selection.** Table 3 (Table 6 in the critic's numbering) is the strongest empirical contribution: MoFO (momentum-filtered BCD) achieves GSM8K 45.4, substantially outperforming gradient-filtered BCD (40.2) and randomized BCD (35.0), while all three methods maintain comparable forgetting levels. This directly shows that momentum magnitude is a better selection criterion than the more naive gradient-based alternative.

3. **Consistent performance across diverse settings.** MoFO demonstrates competitive fine-tuning performance while better preserving general capabilities across two different base models (Llama-2-7B, TinyLlama-1.1B), two fine-tuning paradigms (instruction and continual), and multiple datasets. The continual learning results (Table 4) are particularly clean: MoFO improves OP from 38.4→41.3 and BWT from -10.3→-5.4 over Full FT, and combines well with Replay and GEM.

4. **Replay-free and regularization-free.** MoFO achieves forgetting mitigation without requiring access to pre-training data (addressing a practical limitation of many methods) and without modifying the loss function. This is a meaningful combination of advantages not jointly offered by most existing approaches.

## Weaknesses

### Fatal
None.

### Major

1. **Missing EWC baseline weakens the comparative claim.** The paper claims "superiority over existing methods" and argues that modifying the loss function "may impair the model's performance on the fine-tuning task." Yet the only regularization-based baselines evaluated are simple L1 and L2 penalties. Elastic Weight Consolidation (EWC) is a standard regularization baseline in the forgetting literature (cited in the paper's related work) and is a natural competitor for testing whether the claimed advantage of MoFO over loss-modification methods holds against a stronger regularization approach than L2. Without this comparison, the paper's broader "superiority" claim is incompletely supported. The paper compares against Full FT, HFT, L1, L2, GEM, and Replay, which is a reasonable set, but EWC is a noticeable omission given the paper's positioning against regularization-based methods.

### Minor

1. **No variance or significance reporting.** All experimental results appear to be from single runs. While single runs are common for 7B-scale models due to computational cost, several key comparisons involve small margins (e.g., MoFO average +0.4% vs. HFT -0.1% in Table 1; MoFO -1.1% vs. HFT -1.8% in Table 2). Without any indication of variance, the reader cannot assess whether these differences are meaningful or within the noise of benchmark evaluation. The paper should at minimum acknowledge this limitation.

2. **The α% selection procedure is not documented.** The update fraction α% is a critical hyperparameter with a sharp performance-forgetting trade-off revealed by the ablation study (Figure 3). The paper uses different values across experiments (15% for MetaMathQA, 10% for Code-Alpaca, 5% for continual) without explaining how these were chosen. Was a validation set used? Was a combined metric optimized? Without a stated selection criterion, the results could reflect cherry-picking.

3. **Key methodological details for reproducibility are missing.** The distance metric used to claim "MoFO converges to a point 20% of the Adam travel distance" is not specified (Euclidean? per-layer? over all parameters?). The method for generating the 2D loss landscapes (Figure 1 and 2) is not described—what interpolation direction, step size, or projection method was used? These omissions hinder reproducibility.

4. **The convergence theorem covers a simplified variant, not the actual algorithm.** Theorem 1 proves convergence for a gradient-descent version of MoFO (no momentum) at rate O(T^{-1/2}) under an ∞-norm clipping assumption. The paper acknowledges this gap, but the theoretical contribution remains modest and does not provide insight into the distinctive behavior of the momentum-based selection rule.

5. **The mechanistic explanation (Section 5) is an intuition, not a rigorous explanation.** The 2D toy example illustrates attractor interference in a highly constructed setting. The section title "Why MoFO Converges to a Closer Point" overpromises. The paper should more clearly frame this as illustrative intuition rather than a definitive explanation for behavior in deep LLMs.

### Trivial
None.

## Nice-to-Haves

- Report wall-clock time or training cost compared to Full FT and HFT. MoFO adds a top-k selection per block per iteration, and readers would benefit from knowing the practical overhead.
- Discuss the per-partition vs. global filtering trade-off: partitioning by weight matrices means some blocks with uniformly small momentum magnitudes may rarely receive updates—whether this matters in practice is worth commenting on.
- Include a discussion of cases where MoFO still shows negative forgetting (e.g., Code-Alpaca: -1.1% average) to give a more complete picture of the method's limitations.

## Removed Points

- **"Missing LoRA and SI baselines"**: LoRA is an architecture-based PEFT method (not an optimizer) with a fundamentally different parameter budget; comparing a 7B full-parameter optimizer against a low-rank adapter is comparing apples to oranges. SI is a less common baseline and its absence is not a structural gap given that L1 and L2 regularization are already included. These are disagreements about baseline preference, not genuine experimental gaps.
- **"Per-partition rather than global filtering is a concern"**: The paper explicitly states this design choice is made for computational efficiency. This is a valid engineering decision, not a weakness.
- **"The motivating experiment does not directly motivate MoFO"**: The paper first shows different optimizers yield different distances (Section 3.1), then shows MoFO achieves a closer distance than Adam (Section 3.3). The causal chain is: (a) closer distance → less forgetting, (b) MoFO → closer distance. The motivation is coherent.
- **"Computational cost discussion missing"**: Moved to Nice-to-Haves.
- **Formatting and style nitpicks**: Removed per instructions.

## Novel Insights

The reviewer discussion surfaces an interesting subtlety: the paper's strongest evidence for the momentum-based selection mechanism (the ablation in Table 3) and its weakest evidence (the missing EWC baseline) point in opposite directions for evaluating the paper. The ablation is genuinely compelling—it shows a 5-10 point gap over alternatives—but the small-margin comparisons against HFT in the main tables raise questions about how much of the reported benefit is due to the selection mechanism vs. simply the BCD framework. A productive future direction would be to isolate the "BCD effect" (any sparse update method helps forgetting) from the "momentum filtering effect" (momentum-based selection helps fine-tuning performance), which the ablation partially does. The paper could strengthen its framing by leaning more on this distinction.

## Suggestions

1. Add EWC as a baseline in the instruction fine-tuning experiments. This directly tests the paper's claim that loss-modification methods impair fine-tuning performance and would substantially strengthen the comparative claims.
2. Report results over multiple seeds (at least 3) for the main experiments, or at minimum acknowledge the single-run limitation and provide estimated variance from the literature.
3. Document the α% selection procedure for each experiment (e.g., "chosen by maximizing GSM8K on a held-out validation set") or demonstrate robustness by showing results for multiple α values.
4. Specify the distance metric and landscape-generation method in the main text or appendix.
5. Soften the "superiority" language in the abstract and conclusion to match the scope of the experimental comparison ("outperforms Full FT, HFT, and L1/L2 regularization in mitigating forgetting").

## Score and Decision

The paper makes a genuine contribution: MoFO is a novel, well-motivated optimization method, and the ablation validating momentum-based selection over gradient-based and random BCD is clean and convincing. The method is simple, practical (replay-free, regularization-free), and the experiments consistently show benefits across multiple settings. However, the evaluation has meaningful gaps—most notably the missing EWC baseline and the lack of variance reporting—that prevent the paper from fully substantiating its broader claims of superiority. These are addressable gaps, not fatal flaws.

The paper is a solid contribution that would benefit from a stronger experimental section. It should not be rejected, but it also cannot be accepted in its current form without addressing the major weakness. A revision adding the EWC baseline and tempering the claims would make this a strong paper.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>