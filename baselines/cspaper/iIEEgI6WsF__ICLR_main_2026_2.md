---
job_id: 3e48a784-cdd7-4513-97b3-eddb83d5e9b6
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: iIEEgI6WsF.pdf
paper: Revisiting Parameter Server in LLM Post-Training
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is squarely within ICLR scope under large-scale learning, optimization, infrastructure for ML, and reinforcement learning / language model training systems.

## Minimum Quality
Pass ✅. The submission contains an abstract, introduction, background/method, experiments with quantitative results, discussion, and conclusion; it presents a coherent systems contribution with substantial empirical evidence, even though some methodological and exposition issues remain.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, manipulative instructions, or suspicious embedded text targeting automated review behavior in the provided paper content.

# Expected Review Outcome:
## Summary
This paper revisits the parameter-server perspective for LLM post-training under sequence-length-induced workload imbalance, and proposes On-Demand Communication (ODC), which replaces FSDP’s per-layer collective all-gather/reduce-scatter with point-to-point gather and scatter-accumulate operations. The key claim is that this relaxes synchronization from layer level to minibatch level while preserving synchronous optimization semantics, thereby reducing idle time from stragglers and enabling simpler minibatch-level load balancing. Experiments on SFT and RL workloads with Qwen-based models report throughput gains of up to 36% over standard collective-based FSDP.

## Strengths
1. **The paper identifies a real and timely systems bottleneck in LLM post-training.**  
   The motivation is convincing and well aligned with current practice: sequence-length variance in SFT and RL causes persistent compute imbalance, and the paper correctly points out that FSDP’s fine-grained collectives make this especially painful. This is not a contrived problem setup.

2. **The core systems idea is simple and conceptually clean.**  
   Recasting FSDP as a decentralized parameter server by colocating server and worker roles is a neat perspective. The proposal is easy to explain and, at least at a high level, easy to reason about. I appreciated that the paper does not oversell this as a completely new training algorithm, but rather as a communication/synchronization redesign.

3. **The figures do a good job of communicating the central intuition.**  
   In particular, **Figure 1 on Page 2** clearly illustrates how collective communication in FSDP inserts repeated layer-level barriers, while **Figure 2 on Page 2** makes the proposed relaxation to minibatch-end synchronization visually obvious. This pair of figures is effective because it directly supports the main thesis of the paper: the inefficiency comes from synchronization granularity, not merely from raw communication volume.  
   Likewise, **Figure 6 on Page 5** helps anchor the “decentralized PS” interpretation by showing how parameters, gradients, and optimizer states are colocated across devices. This makes the architecture much easier to parse than the text alone.

4. **The empirical evaluation is broad across tasks, model scales, and batching regimes.**  
   The paper includes both SFT and RL, covers models from 1.5B to 32B, and tests several batching/packing strategies. This is stronger than a single-workload anecdote.

5. **Some of the reported gains are substantial and consistent in the intended regime.**  
   The SFT results are particularly strong. For example, in **Table 5 on Page 18**, ODC+LB-Mini improves over Collective+LB-Micro by large margins in the higher-imbalance settings, such as 14B LongAlign at minibatch size 4, where throughput rises from 45.1 to 61.4 samples/sec/device, a reported +36%. This is a meaningful gain, not noise-level improvement. The fact that gains largely disappear at minibatch size 1 is also a good sign, because it matches the claimed mechanism instead of looking like a generic implementation-speed trick.

6. **The paper does a useful job separating communication design from load balancing.**  
   The inclusion of Collective/ODC crossed with LocalSort/LB-Micro/LB-Mini is helpful. It lets the reader see that ODC is not merely “winning because of a better packer,” and that the communication scheme and balancing granularity interact in an interpretable way.

7. **The communication microbenchmark adds important nuance instead of just cherry-picking end-to-end wins.**  
   **Figure 11 on Page 8** is valuable because it shows a limitation rather than hiding it: ODC primitives are comparable to collectives intra-node, but worse inter-node. This honesty strengthens the paper overall.

8. **The paper is generally readable and pragmatic.**  
   The implementation section is concise but informative, and the discussion section usefully acknowledges inter-node inefficiency and possible mitigations rather than pretending the method dominates in every networking regime.

## Weaknesses
1. **The main technical claim, “preserving synchronous optimization semantics,” is asserted more than it is formally established.**  
   This is central to the paper, but the treatment in the main text is too hand-wavy. On **Page 4, Section 3**, the paper states that ODC “relaxes synchronization to a much coarser granularity without altering the training semantics,” yet there is no formal statement of equivalence between collective-FSDP and ODC-FSDP. At minimum, the paper should specify the exact invariant being preserved, for example that for each parameter shard \(p_j\), the optimizer update uses the same accumulated gradient
   \[
   \bar g_j = \sum_{m=1}^{M} w_m g^{(m)}_j
   \]
   as standard FSDP at minibatch end, and explain under what ordering and atomicity assumptions this remains true when gradient contributions arrive asynchronously through scatter-accumulate.  
   This matters because the method relies on a daemon-based accumulation path (**Page 5, Section 3.2**) and remote writes; without a precise statement of race-handling, accumulation ordering, and visibility guarantees, the reader has to take correctness on faith. The appendix may contain convergence verification, but the main paper’s central semantic claim should not rest on “see appendix.”

2. **The mathematical model of runtime on Page 3 is too crude for the conclusions the paper later draws.**  
   **Equation (1) on Page 3** defines
   \[
   T(\mathcal{P}_M)=\sum_{m=1}^{M}\sum_{l=1}^{L}\max_d T_{m,d,l}(\mathcal{P}_M).
   \]
   This is used to motivate the burden of per-layer synchronization in FSDP. The problem is not that the intuition is wrong, it is that the notation collapses communication, overlap, prefetching, and pipeline effects into a single per-layer scalar without saying what exactly \(T_{m,d,l}\) includes. Earlier in Section 2.2 the authors explicitly state that communication can be overlapped with computation, which means the step time is not generally a simple sum of per-layer maxima. If \(T_{m,d,l}\) already includes overlap, then the dependence on collectives versus point-to-point is underspecified; if it does not, then the model mismatches actual FSDP execution.  
   This matters because the paper later interprets performance improvements as reductions in synchronization bubbles. A more careful decomposition such as
   \[
   T_{m,d,l} = T^{\text{comp}}_{m,d,l} + T^{\text{comm}}_{m,d,l} - T^{\text{overlap}}_{m,d,l}
   \]
   or an explicit statement that Equation (1) is a stylized upper bound would make the argument more rigorous and less slippery.

3. **The load-balancing comparison is not entirely clean, because the strongest new balancing method is only available to ODC.**  
   The paper is explicit that **LB-Mini** can produce different numbers of microbatches per device and therefore “applies only to ODC” (**Page 6, Section 5.1**). That is fair from an implementation standpoint, but it complicates attribution. When the best numbers compare ODC+LB-Mini against Collective+LB-Micro, the improvement mixes two factors: a communication redesign and an enlarged feasible space for batching.  
   To the authors’ credit, they do include ODC+LB-Micro. Still, the discussion in **Section 5.2 on Page 7** occasionally blurs whether the paper’s win should be read as “ODC is better than collectives under the same balancing strategy” or “ODC enables a better balancing strategy.” These are both interesting, but scientifically they are different claims.

4. **Some experimental evidence is thinner than it should be for a systems paper making strong practical claims.**  
   The paper reports throughput extensively, but the evaluation is missing several pieces that would increase confidence:
   - no run-to-run variability or error bars,
   - no wall-clock breakdown in the main paper separating compute, communication, idle time, and optimizer-step time,
   - no sensitivity to different network regimes beyond the microbenchmark,
   - no direct comparison against hybrid or hierarchical collective variants in the main experiments.  
   This matters because end-to-end speedups of 5% to 10%, especially in RL (**Figure 9 on Page 7**, **Table 3 on Page 17**), can be fragile to implementation details. For example, **Table 3** even shows a regression for 14B AIME at minibatch size 2, where ODC LB-Micro is 101.0 versus 106.4 for Collective LB-Micro, a reported \(-5\%\). That is actually useful information, but it highlights that the story is more conditional than the headline suggests.

5. **The paper’s strongest evidence for correctness is relegated out of the main paper.**  
   The main text says, on **Page 6, Section 5.1**, that correctness is validated by “verifying the training convergence in Appendix F.” But in the main paper there is no loss curve, no equivalence check on gradients/updates, and no direct sanity check beyond the throughput story. Since ODC changes the communication and gradient accumulation path in a nontrivial way, a compact correctness figure or quantitative parity check really belongs in the main paper, not only in the appendix.

6. **The inter-node story is a meaningful limitation, and the paper only partially closes the loop.**  
   The communication benchmark in **Figure 11 on Page 8** shows that ODC is “significantly slower than collective” across nodes. The discussion on **Page 9, Section 6.1** gives plausible reasons and mitigations, but these are mostly argued rather than demonstrated in the main body. The paper claims that long-sequence compute can hide the extra communication, which is plausible, but then the practical message becomes more narrow: ODC seems best suited to long-context, imbalance-heavy workloads with enough compute to amortize its weaker inter-node communication pattern. That is still useful, but more conditional than the paper’s framing sometimes suggests.

7. **The implementation assumptions are quite specialized, which limits the portability of the claimed simplicity.**  
   Section 3.2 on **Page 5** relies on CUDA IPC, NVSHMEM, RDMA behavior, and a daemon-based accumulation design. The paper says integration into FSDP is “straightforward,” but that is true only after one accepts a fairly specialized communication substrate and nontrivial systems engineering. I do not object to an engineering-heavy contribution, but the paper undersells the deployment complexity relative to off-the-shelf collective-based FSDP.

8. **The paper does not sufficiently quantify the overheads introduced by ODC itself.**  
   Appendix B mentions extra per-client buffers and a lightweight daemon. In the main paper, however, there is no accounting of additional memory overhead, daemon CPU cost, contention behavior under many concurrent clients, or how much of the end-to-end gain disappears when overlap is imperfect. This matters because the method is not a free lunch; it trades synchronization barriers for a more complex accumulation path.

9. **Presentation is generally good, but there are several imprecisions and underdefined choices.**  
   A few examples:
   - On **Page 3**, the notation alternates between \(\mathcal{P}_M\) and \( \mathcal{P}_{\mathcal{M}}\), which looks inconsistent.
   - The phrase “without altering training semantics” is stronger than what is actually demonstrated in the main paper.
   - On **Page 6**, “Unless otherwise specified, the maximum number of tokens in a microbatch is constrained by the maximum sequence length of a single sample in the dataset” is an important experimental constraint, but its practical effect on comparability across methods is not really unpacked.
   These are not fatal, but for a paper hinging on a precise systems argument, imprecision costs credibility.

10. **The benchmark framing could do a better job distinguishing throughput gains from generality of usefulness.**  
   The paper’s best results come from long-sequence SFT with substantial imbalance, and that is exactly where I would expect ODC to shine. But the paper sometimes drifts toward a broader narrative that PS-style communication is simply a “superior fit” for LLM post-training. The data in the main paper support a more nuanced statement: ODC is a better fit in imbalance-heavy, sufficiently compute-dominant regimes; outside those regimes, the case is weaker and can even reverse, as seen in the RL table for some settings.

11. **The figures showing dataset distributions are useful, but they also expose a gap in the analysis.**  
   **Figure 7 on Page 6** nicely shows that LongAlign is much more long-tailed than the other datasets, which helps explain why the gains are larger there. However, the paper never quantitatively links distributional skew statistics, such as variance or tail mass, to the observed acceleration. That would have been much more informative than only saying “less long-tailed” or “more long-tailed.” Since the central claim is about robustness to imbalance, an explicit correlation analysis would strengthen the scientific contribution.

12. **Some key table-based claims deserve more careful interpretation.**  
   In **Table 5 on Page 18**, ODC+LB-Mini often strongly outperforms Collective+LB-Micro, but the improvements flatten or shrink at larger minibatch sizes, and sometimes ODC+LB-Micro is barely better or even slightly worse at small minibatches, for example 32B LongAlign at minibatch size 2, where ODC LB-Micro is 17.0 versus 17.3 for Collective LB-Micro. This is not a deal-breaker, but it means the method is not uniformly advantageous even within the paper’s preferred workloads. The discussion on **Page 7** gestures at this, but the take-home message should be calibrated more carefully.

## Questions
1. The main paper claims that ODC preserves synchronous optimization semantics while allowing asynchronous shard fetch/push within a minibatch. Can the authors provide a concise formal argument in the rebuttal for why the parameter update after each minibatch is exactly equivalent to standard FSDP under the same data ordering and weights \(w_m\)? In particular, what assumptions are required about atomicity and ordering of scatter-accumulate operations?

2. Can the authors clarify the exact meaning of \(T_{m,d,l}(\mathcal{P}_M)\) in **Equation (1) on Page 3**? Does it include communication, overlap, prefetching, and waiting, or is Equation (1) intended only as a stylized upper bound? A more precise definition would increase my confidence in the analytical framing.

3. Could the authors add, in the rebuttal if possible, a small main-paper-quality correctness check beyond the appendix, for example gradient parity at minibatch end or a short loss-equivalence plot? This would materially improve confidence because the method changes the communication and accumulation pathway in a nontrivial way.

4. How sensitive are the results to imperfect overlap between communication and computation? The paper argues on **Page 9** that long-sequence workloads hide communication costs, but a direct ablation varying sequence length or communication overlap quality, tied to end-to-end throughput, would make this much more convincing.

5. Can the authors quantify ODC’s additional overheads, specifically extra buffer memory, daemon cost, and any observed contention pathologies as world size grows? Even a compact table would help readers understand when the trade-off is favorable.

6. The communication benchmark in **Figure 11** suggests a clear cross-node disadvantage. Do the authors have end-to-end numbers on a more communication-dominated regime, or with shorter sequences, in the main experimental setting? This would help define the boundary where ODC stops being attractive.

7. For the load-balancing story, it would help to separate the claims more sharply. Could the authors report, or at least discuss explicitly, the improvement from ODC under the same packing strategy only, versus the additional improvement unlocked by LB-Mini? Right now the reader has to reconstruct this from multiple plots and tables.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No ethics concerns that require dedicated review were evident from the submission. The paper is a systems/infrastructure contribution for LLM training efficiency and does not introduce a new dataset collection, human-subject protocol, or obviously sensitive deployment pipeline in the main paper.

## Soundness Rating
3: good. The central empirical claims are mostly supported, and the results are coherent with the proposed mechanism, but the main-paper treatment of semantic equivalence/correctness and the simplified analytical model leave some technical gaps.

## Presentation Rating
3: good. The paper is readable and well organized, and several figures are effective, but there are important imprecisions in notation, claim strength, and methodological exposition.

## Contribution Rating
3: good. The paper addresses an important practical bottleneck and offers a useful communication redesign with meaningful throughput gains in the target regime, though the contribution is somewhat conditional and not as broadly settled as the framing implies.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected.  
This is a useful and well-motivated systems paper with a clear practical contribution and credible gains on imbalance-heavy LLM post-training workloads. I am positive on the main idea and the empirical trend, but I am not fully satisfied with how the paper substantiates semantic equivalence, handles the analytical model, and characterizes the limits of the method under inter-node and less compute-dominant regimes.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The systems idea and experimental evidence are clear, and I checked the main technical claims and equations carefully, but some implementation-level correctness details are not fully available in the main paper.