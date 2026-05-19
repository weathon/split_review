## Summary

This paper proposes SwitchLoRA, a parameter-efficient pre-training method for LLMs that extends LoRA by frequently and incrementally swapping individual column/row vectors of the LoRA matrices with pre-maintained candidate vectors. The key idea is that by switching only a few dimensions at a time and resetting corresponding optimizer states, the method can update the effective subspace much more frequently than prior approaches like ReLoRA or GaLore, allowing it to more closely approximate full-rank training behavior. Experiments on LLaMA models (130M–1.3B) trained on C4 show that SwitchLoRA consistently outperforms GaLore across settings and, at rank 512 on the 1.3B model, achieves a perplexity of 15.01 vs. the full-rank baseline of 15.23.

## Strengths

- **Consistent and substantial improvement over GaLore across diverse settings (Table 4)**: This is the paper's strongest empirical result. SwitchLoRA beats GaLore in all five configurations tested (Standard, 130M, Rank=128, Rank=32, Seq.len=512). The gap at rank=32 is particularly large (25.26 vs. 34.09), which provides concrete evidence that the switching strategy preserves more information at very low ranks than SVD-based gradient projection.

- **Clean methodological motivation and design**: The paper identifies a real limitation in prior work (coarse subspace updates cause optimizer state inconsistency, forcing large intervals between updates) and designs an elegantly targeted solution—vector-level switching with per-vector optimizer state reset and temporary freezing. Algorithms 1 and 2 provide a precise specification. The mechanism is pragmatic and well-reasoned.

- **Outperforms ReLoRA with far fewer full-rank warm-up steps (Figure 7)**: SwitchLoRA with only 200 warm-up steps achieves lower loss than ReLoRA with 5,000 warm-up steps, and when both methods use 1,000 warm-up steps, SwitchLoRA shows a significant advantage. This is a meaningful improvement over a directly comparable prior method.

- **1.3B model results show promise on both perplexity and downstream tasks**: On the 1.3B model, SwitchLoRA (rank=512) achieves perplexity of 15.01 vs. full-rank 15.23, and after fine-tuning on GLUE (Table 6), outperforms the full-rank pre-trained checkpoint on 4 of 5 tasks with ~1% average improvement. These results, while limited in scale, are self-consistent and directionally positive.

## Weaknesses

### Fatal
None.

### Major

- **Placeholder text left in the manuscript (Section 5.3, line 364)**: The sentence reads: "SwitchLoRA outperforms GaLore by [insert performance difference], and outperforms the full-rank model by [insert performance difference]." This is unacceptable in a submission under review. It indicates the manuscript was not fully prepared before submission and undermines confidence in the care with which all reported numbers were verified.

- **The claimed 54% communication overhead reduction is asserted without direct measurement**: The abstract states SwitchLoRA "reducing communication overhead by 54%," and the Conclusion claims "the computational overhead and memory usage are nearly identical to those of LoRA." Yet the paper provides **zero** measurements of actual communication time, memory usage, or runtime. The 54% figure is derived purely from trainable parameter count (609.7M vs. 1339.5M), but communication overhead in distributed training depends on many factors beyond parameter count (gradient all-reduce for LoRA parameters, CPU offloading of candidate vectors, synchronization of the switch operation itself). The paper's own motivation centers on communication reduction, making this evidential gap structural.

- **350M GLUE results are misrepresented**: The paper states (Section 5.3) that for the 350M model, "except for the CoLA task, SwitchLoRA outperforms... the full-rank model." Table 5 directly contradicts this. SwitchLoRA underperforms the full-rank checkpoint on **4 out of 5** GLUE tasks (CoLA: 23.13 vs. 42.95; MRPC: 76.86 vs. 79.16; RTE: 56.24 vs. 59.86; SST2: 90.83 vs. 90.88). Only STS-B is slightly better (87.71 vs. 87.26). This error in the narrative, combined with the placeholder text in the same paragraph, suggests the downstream analysis was not carefully reviewed.

- **ReLoRA comparison lacks quantitative perplexity numbers**: The ReLoRA comparison (Figure 7) presents only loss curves. No final perplexity table is reported for this baseline, even though perplexity is the primary evaluation metric throughout the rest of the paper. This makes it difficult to assess the magnitude of improvement over ReLoRA. Given that ReLoRA is one of the two closest prior methods (alongside GaLore), this is a notable omission.

- **Surpassing full-rank only holds at a high rank (512, 45.5% of full parameters) on the 1.3B model**: SwitchLoRA with rank=256 (370.7M parameters) achieves perplexity 15.89 vs. full-rank 15.23—it is *worse* than full-rank. The headline result (15.01 vs. 15.23) only emerges at rank=512. While rank=512 is still parameter-efficient in an absolute sense (609.7M vs. 1339.5M), the paper's framing as "surpassing full-rank training" overstates the robustness of this result. The method's advantage is contingent on using a relatively high rank, and the transition point where it becomes beneficial is not characterized.

### Minor

- **The claim that the update "ensures updated parameters are full-rank" (line 93) conflates two things**: The candidate set has min(m,n) distinct vectors, but at any given step, the instantaneous update BA is still rank at most r. What is "full-rank" is the space spanned by the candidate set over the course of training, not the update itself. This distinction should be clarified.

- **Experimental scale is very small**: Training is limited to 40k steps on 46M samples from C4. The perplexities reported (e.g., 27.71 for a 130M model) are high relative to well-converged models of these sizes. While this scale is consistent with prior low-rank pre-training work (ReLoRA), the paper should more clearly acknowledge that claims about "surpassing full-rank" and "full-scale pre-training" are extrapolations from an undertrained regime.

- **SwitchLoRA uses a different learning rate (0.02) than full-rank (0.001) and LoRA (0.01)**: While hyperparameter tuning is reasonable, the paper does not discuss whether the full-rank baseline could have benefited from a higher learning rate or whether the SwitchLoRA advantage partly reflects better-tuned optimization.

### Trivial
None.

## Nice-to-Haves

- Direct measurement of communication time, memory footprint, and per-step runtime would substantially strengthen the paper's central motivation.
- Reporting final perplexity numbers (with variance) for the ReLoRA comparison would make that experiment complete.
- A more precise characterization of the rank vs. performance trade-off (at what rank does SwitchLoRA cross over full-rank?) would be informative.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Full-rank baseline perplexity of 15.23 is high, suggesting undertraining"** — While the training scale is small, the critic's specific claim that the advantage "may simply be noise or an artifact of incomplete training" is speculative. The paper uses a fixed 40k-step budget consistent with prior work; the claim that results would "vanish with longer training" is not grounded in evidence presented or cited.

2. **"GaLore perplexity discrepancy (20.29 here vs. ~18.5 in GaLore paper)"** — Cannot be verified without direct access to the GaLore paper's exact experimental setup. The paper states it "strictly follow[s] the setup in Galore." This criticism depends on information not present in the submitted paper and is removed.

3. **"Initialization formulas appear dimensionally inconsistent"** — The critic asserts a technical claim about the derived standard deviation formulas (the paper's eq. 5) without providing a dimensional analysis. The formulas are presented as heuristic extensions of Xavier/Kaiming initialization; whether they are "dimensionally inconsistent" requires a specific mathematical argument the critic does not provide.

4. **"Not parameter-efficient" characterization of rank=512** — Using 609.7M vs. 1339.5M parameters (45.5%) is still a significant reduction. Calling this "not parameter-efficient in any practical sense" is an overstatement.

5. **Generic strengths from Strength Finder removed**: "Addressed an important problem," "targeted an interesting question" — these lack specific evidentiary anchoring.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Remove the placeholder text** and fill in the missing performance differences (or correct the narrative to match the data in Table 5, which shows the 350M GLUE results do not support the claimed advantage over full-rank).
2. **Measure and report actual communication overhead and runtime** (or reframe the claim from "communication reduction" to "trainable parameter reduction," which is factually supported).
3. **Add a perplexity table for the ReLoRA comparison**, matching the format of Table 4 for GaLore.
4. **Correct the 350M GLUE discussion** to honestly reflect Table 5: SwitchLoRA underperforms full-rank on this model size, suggesting the method's benefits are size-dependent.
5. **Acknowledge the rank dependence explicitly**: state that surpassing full-rank is observed at rank=512 on the 1.3B model, and characterize the cross-over point more carefully.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>