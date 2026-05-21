---
job_id: 68608637-e079-4a98-b239-7a6ea4ce35cb
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: yR5QX5cTEy.pdf
paper: Efficient Allreduce with Stragglers
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly about distributed ML infrastructure and collective communication for training/inference, which fits ICLR’s scope on large-scale learning, optimization, and ML systems/software.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, presents a concrete algorithmic contribution with complexity analysis and experiments, and is sufficiently complete to merit full review, even though I have substantial concerns about some assumptions, comparisons, and clarity.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, manipulative instructions, or other signs of review-targeting content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies ALLREDUCE under straggler-induced temporal asymmetry and proposes StragglAR, an exact straggler-aware algorithm that overlaps a REDUCESCATTER among non-straggler GPUs before the final rank reaches the barrier, then completes the reduction using a custom communication schedule. The paper gives a communication-complexity analysis for power-of-two world sizes, argues that the exposed bandwidth cost can drop from roughly \(2s\beta\) to \(s\beta\) in ideal straggler settings, and presents both hardware experiments on 4- and 8-GPU systems and larger-scale simulations.

## Strengths
1. The paper attacks a real and important systems bottleneck for distributed ML. The motivating data in **Figure 2(a), Page 2** is useful because it shows that straggler delay is not merely a datacenter-scale pathology or a fault scenario, but appears even in relatively small multi-GPU settings during LLM fine-tuning. That makes the problem relevant to ICLR practitioners working on training and inference systems, not just HPC specialists.

2. The core idea is interesting and well framed. The paper’s main conceptual move, exploiting temporal asymmetry rather than assuming simultaneous collective start, is a meaningful reframing of the design space. **Figure 1, Page 1** communicates the intuition clearly: the left panel shows pure idle waiting, while the right panel makes the “use the waiting time to do useful work” idea immediately understandable.

3. The contribution is not merely heuristic. The paper provides an explicit schedule-generation procedure in **Algorithm 1, Page 4**, and a communication-complexity claim in **Theorem 1, Section 3.2**. Even though I have concerns about clarity and some proof presentation choices, I appreciate that the authors try to formalize the regime in which the algorithm beats classical synchronous lower bounds instead of stopping at an implementation anecdote.

4. The algorithm appears to have a favorable upside-downside tradeoff in the intended regime. **Table 1, Page 6** is one of the more convincing parts of the paper because it makes the target claim precise: best-case StragglAR reduces exposed bandwidth complexity to approximately \(s\beta\), while worst-case it returns to approximately \(2s\beta\). If this framing is correct, it is a compelling operating point for settings where moderate straggler delays are common.

5. The experimental section contains both microbenchmark and end-to-end evidence. **Figure 5(a,d), Page 8** shows that StragglAR is strongest for large buffers, which is consistent with the \(\alpha\)-\(\beta\) story. **Table 2, Page 9** also gives some end-to-end training gains on three LLM fine-tuning workloads, which is important because a communication optimization that does not move wall-clock training time is not that interesting to the ICLR audience.

6. The algorithm visualization is helpful. **Figure 4(a,b), Pages 5-6** does more than decorate the text: panel (a) gives a concrete 4-GPU execution trace, and panel (b) explains why arbitrary pairings fail because of the “critical window.” That figure materially helps interpret the schedule invariant.

## Weaknesses
1. The paper’s strongest claim, that it “surpasses the lower bound for bandwidth-optimal synchronous ALLREDUCE,” is correct only under a carefully qualified model, but the presentation often blurs the qualification in a way that overstates the result. The lower bound being beaten is repeatedly described as the known bandwidth-optimal ALLREDUCE lower bound, but StragglAR’s advantage comes from changing the model of when communication may begin, not from improving synchronous ALLREDUCE under the same start-time assumptions. This distinction is mentioned, but not emphasized consistently enough in the main text, especially in the abstract and **Section 1, Pages 1-2**. Why this matters: without very explicit qualification, readers may infer a stronger algorithmic result than what is actually shown, namely an improvement over the classical bound in the same synchronization model.

2. The evaluation compares StragglAR against baselines implemented with the same NCCL P2P substrate rather than against the production-quality collective kernels users would actually deploy, which weakens the practical claim. The paper states in **Section 4, Page 7** that all baselines are reimplemented using NCCL P2P plus the same CUDA kernels “for fair comparison of the algorithmic contribution.” I understand the motivation, but this is still a materially different question from whether StragglAR beats mature NCCL collectives in practice. This matters because the headline claim in the abstract and introduction is framed operationally, as accelerating distributed training and inference, while the experimental setup mostly demonstrates superiority over a controlled algorithmic reimplementation, not necessarily over the best tuned library path available to practitioners.

3. Real-hardware validation is limited to very small scale, while the most ambitious benefits are shown only in simulation. The strongest scaling claims, including the near-\(2\times\) advantage, come from **Figure 6(c), Page 10** and **Figure 2(b), Page 2**, both derived from an analytical \(\alpha-\beta\) model rather than hardware measurements. The actual hardware experiments are on 4- and 8-GPU systems. This matters because the paper’s central narrative is about scaling behavior with cluster size, yet the empirical support for that scaling is indirect. For a systems paper making asymptotic efficiency claims, simulation is fine as supporting evidence, but it does not fully substitute for at least one larger-scale real deployment or a stronger validation that the simulator tracks measured behavior across more than a handful of points.

4. The practical success of the method depends heavily on straggler identification and sufficient overlap, but the end-to-end experiment uses a static profiled straggler and therefore does not validate the fully dynamic setting emphasized in the motivation. In **Section 4.2, Page 9**, the runtime fixes one likely straggler rank ahead of time, and **Table 2** explicitly notes that the reported gains are “worst-case speedups on the given VM due to static straggler detection.” That is a fair stress test, but it leaves a significant gap between the paper’s broad framing and what is actually shown. This matters because for non-persistent or workload-dependent stragglers, the implementation complexity and scheduling overhead of conditional execution could dominate the benefit, and the paper does not quantify this.

5. Several claims extend beyond the demonstrated application surface. The paper repeatedly positions StragglAR as useful for both data-parallel and tensor-parallel training/inference, but the end-to-end experiments in **Section 4.2, Page 9** cover only data-parallel fine-tuning on 8 GPUs. There is no tensor-parallel experiment, no inference experiment, and no model-parallel activation aggregation case. This matters because tensor-parallel collectives can have different timing structure, message sizes, and overlap opportunities. A paper can certainly claim applicability beyond its experiments, but here the breadth of the claim is stronger than the evidence.

6. The mathematical exposition in the main paper is not as clean as it needs to be, and there are places where the notation or derivation is shaky enough to reduce confidence. A concrete example is **Algorithm 1, Page 4**, where the loop is written as “for round \(r = 0\) to \(n-2+\log n\) do,” which conventionally suggests an inclusive upper bound, implying \(n+\log n-1\) rounds, while **Theorem 1, Page 6** states \(n+\log n-2\) rounds. Perhaps this is a pseudocode convention issue, but in a paper whose core contribution is a carefully counted communication schedule, off-by-one ambiguity is not a cosmetic issue. Similarly, the notation in the pseudocode is rough in several places, for example the initialization of \(A\) and the line “Each rank with a reduced chunk sends to any rank \(g > 2(\log n - 1)\) without a chunk,” which is not formal enough to serve as a complete executable specification.

7. The derivation of the critical delay in **Appendix B, Pages 21-22**, which is referenced substantively in the main paper, relies on an approximation step that is too casual for a threshold claim. The paper moves from
\[
\frac{2(n-2)+\log n}{n-1}s\beta
\]
to an approximate expression
\[
\frac{2(n-1)+\log n}{n}s\beta,
\]
and then derives the simple threshold
\[
T_{\text{straggler}} \ge (\log n - 2)\alpha + \frac{\log n}{n}s\beta.
\]
If this threshold is later used to explain why the critical delay approaches zero and why worst-case behavior is competitive, I would like a precise inequality, not a heuristic approximation. This matters because the paper uses “critical delay” as a key practical decision quantity in **Figure 5(c,f), Page 8** and **Figure 7(a), Appendix Page 21**.

8. The assumption about GPU communication capability is stronger than the paper acknowledges, and the evidence for it in the main paper is weak. In **Section 3, Page 4**, the authors assume each GPU has a single effective connection and therefore “can fully utilize bandwidth by sending data to one peer at a time,” while also comparing to MSCCL allpairs, which explicitly relies on splitting bandwidth across peers. This is a consequential modeling assumption, not a side detail. It matters because StragglAR’s round structure and the comparison to multi-peer collectives depend on how bandwidth sharing behaves on the actual interconnect and NCCL runtime. The paper says this is “confirmed empirically in §4,” but the main paper does not provide a dedicated measurement that isolates and validates this assumption.

9. The exposition around chunking is unconventional and easy to trip over. In **Section 3.1, Page 4**, the buffer is divided into \(n-1\) chunks of size \(s/(n-1)\), whereas classical ring-style analyses often use \(n\) chunks of size \(s/n\). That is not necessarily wrong, because the straggler precondition changes the combinatorics, but the paper does not do enough to explain the normalization and to reassure the reader that all later cost comparisons in **Table 1, Page 6** are truly apples-to-apples. Given that the headline contribution is a bandwidth-cost reduction, this should be handled more carefully.

10. Some figure and table interpretations are less convincing than the surrounding text suggests. For example, **Figure 5(a,d), Page 8** indeed shows StragglAR leading at large buffers, but it also shows regimes where RHD, Broadcast, and MSCCL are better for smaller sizes, which reinforces that the method is specialized rather than generally superior. Likewise, **Table 2, Page 9** reports only modest end-to-end gains, \(2.39\%\) to \(4.75\%\), despite the much larger algorithmic gains emphasized elsewhere. That does not invalidate the contribution, but it should temper the narrative. The practical impact is positive, but not yet at the level implied by some of the more aggressive framing.

11. The paper does not compare against other straggler-resilient training-level approaches in a way that clarifies when an exact collective-layer solution is preferable. The related work section mentions approximation or dropping-based methods and some systems approaches, but the empirical section does not contain even a qualitative comparison of regimes where StragglAR wins or loses relative to such alternatives. This matters because the paper’s contribution is partly a problem-formulation contribution, exact straggler-aware collectives instead of approximate mitigation, and the practical tradeoff boundary remains underdeveloped.

## Questions
1. Can the authors clarify the counting convention in **Algorithm 1** versus **Theorem 1**? If the loop bound in Algorithm 1 is inclusive, it appears to give \(n+\log n-1\) rounds rather than \(n+\log n-2\). If it is exclusive, please state that explicitly and clean up the pseudocode. This would increase my confidence in the schedule specification.

2. Can the authors provide a precise, non-approximate derivation of the critical delay threshold, rather than the approximation used in **Appendix B**? In particular, I would like the exact inequality for the delay at which StragglAR matches Ring, and ideally a comparison between the exact and approximate thresholds for the hardware settings in **Figure 5(c,f)**.

3. The paper claims practical gains for distributed training and inference, but the implementation comparisons are against P2P-based baseline reimplementations. Can the authors report, in the rebuttal if possible, how StragglAR compares against production NCCL `ncclAllReduce()` on at least the large-buffer regimes where the paper expects gains? Even a limited comparison would help separate algorithmic merit from implementation-substrate effects.

4. Can the authors show at least one experiment for tensor-parallel training or inference, or explain more concretely why the data-parallel results should transfer? Right now the claim of broad applicability is stronger than the empirical evidence.

5. The paper assumes that a GPU effectively utilizes bandwidth by sending to one peer at a time in the targeted topology. Can the authors provide a dedicated measurement, ideally in the main paper or rebuttal, that quantifies throughput for one-peer versus multi-peer sends on the tested DGX systems? This would make the comparison to MSCCL and the design choice in **Section 3, Page 4** much more convincing.

6. For **Table 2**, can the authors break down the end-to-end speedups into percentage of time spent in ALLREDUCE, average realized overlap of the precondition, and rate of correct straggler prediction? That would make the modest but real training gains easier to interpret and would help assess generalizability.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns identified from the paper content. The work studies communication efficiency for distributed ML systems and does not introduce obvious issues related to privacy, fairness, human subjects, or harmful deployment beyond standard dual-use considerations for compute acceleration.

## Soundness Rating
3: good. The core idea is plausible and supported by a reasonable mix of analysis and experiments, but some mathematical details, modeling assumptions, and evaluation choices reduce my confidence in the full strength of the claims.

## Presentation Rating
2: fair. The paper is readable at a high level and the figures are helpful, but the mathematical and algorithmic exposition needs tightening, especially around pseudocode, notation, and careful qualification of the main claims.

## Contribution Rating
3: good. The temporal-asymmetry viewpoint and exact straggler-aware ALLREDUCE design are valuable contributions, though the empirical scope and some practical assumptions keep this from feeling fully settled.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a real idea and enough evidence to make it interesting for ICLR, but it overreaches in a few places, the main-paper exposition is not as crisp as the claim strength requires, and the practical validation is narrower than the framing.

## Reviewer Confidence
4: confident. I am confident in the main assessment and checked the technical narrative carefully, though I did not fully verify every appendix proof line-by-line.