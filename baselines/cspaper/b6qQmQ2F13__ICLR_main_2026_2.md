---
job_id: 8daf83ed-8f29-4d9a-a395-d83cfad98b06
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: b6qQmQ2F13.pdf
paper: Not All Bits Are Equal: Scale-Dependent Memory Optimization Strategies for Reasoning Models
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This paper is clearly within ICLR scope: it studies memory-performance trade-offs for reasoning LLM inference, including quantization, KV-cache compression, and test-time scaling, all of which fall under general machine learning, language modeling, and efficient ML systems.

## Minimum Quality
Pass ✅ The paper contains the expected scientific components, including Abstract, Introduction, related-work discussion, experimental setup, quantitative results, and Conclusion/Limitations. The work is empirical rather than methodological in the algorithmic sense, but it presents a reasonably complete large-scale study with clear claims supported by extensive experiments, despite some limitations in positioning and rigor.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find any hidden prompts, reviewer-targeted instructions, or suspicious manipulative text in the provided paper content.

# Expected Review Outcome:
## Summary
This paper studies memory-accuracy trade-offs for reasoning LLMs under fixed deployment budgets, focusing on how memory should be allocated across model weights, token budget, parallel sampling, and KV-cache compression. Using mainly the Qwen3 family, with additional experiments on DeepSeek-R1-Distill and OpenReasoning-Nemotron, the authors argue that the optimal strategy is scale-dependent: smaller effective models benefit more from spending memory on model capacity and precision, while larger models benefit more from longer generations, parallel scaling, and KV-cache optimization.

## Strengths
The main strength is that the paper asks a practically important question that is surprisingly underexplored in the reasoning-model setting. A lot of prior discussion around low-bit deployment implicitly assumes that model weights dominate memory, and this paper makes a credible case that for long-generation reasoning workloads, KV cache changes the optimization problem substantially. That framing is useful and timely.

The empirical scope is substantial. The paper varies model size, weight precision, token budget, sampling group size, and KV strategy, and it does so over a fairly broad grid. Even restricting the judgment to the main paper, the study covers several axes that many papers would treat in isolation. This breadth is valuable because the central message is precisely about interactions across these knobs.

Several figures communicate the core findings effectively. In particular, **Figure 1** on Page 1 is a strong overview figure: it directly visualizes the memory versus accuracy frontier for serial test-time scaling and makes the paper’s central claim legible at a glance, namely that the preferred allocation of memory shifts with scale. **Figure 2** on Page 5 is also quite useful, because it goes beyond the frontier itself and decomposes what actually lies on that frontier, token budget in panel (a), effective model size in panel (b). That is the kind of figure that turns an empirical observation into an actionable guideline rather than just a collection of curves.

The task-dependent precision story is interesting and reasonably supported in the main paper. The contrast between **Figure 3** (LiveCodeBench) and **Figure 4** (GPQA-Diamond) strengthens the claim that the 4-bit prescription is not universal across reasoning tasks. I appreciated that the authors do not overclaim a single universal rule, and instead separate math/code from knowledge-intensive reasoning.

The analysis of parallel scaling is another strong point. **Figure 5** shows a fairly clean separation where parallel scaling helps only once models are sufficiently large, and **Figure 6** suggests this is not unique to Qwen3. Even if the exact threshold is somewhat heuristic, the qualitative pattern is useful for practitioners. I also appreciate that the paper evaluates an external verifier in **Figure 7** rather than assuming verifier-based methods are always preferable.

The KV-cache section adds real value rather than feeling like an appendix-level extra. **Figure 8** clearly shows that both eviction and quantization move the Pareto frontier beyond the no-compression baseline, and **Figure 9** is particularly informative because it explains *why* the two strategies behave differently: quantization shifts curves leftward while eviction produces near-vertical trade-offs due to the hard memory ceiling. That is a concrete, interpretable insight.

There is also good use of tabular information. **Table 1** on Page 4 is not just bookkeeping, it is central to the paper’s argument because it makes explicit how quickly KV cache can dominate total memory, especially under long generations and parallel sampling. The jump from single-sample 30k generations to “30k tokens × 16 samples” makes the paper’s motivation much more convincing. The table also helps interpret why some apparent “small-model plus more compute” strategies are not actually cheap in memory terms.

Overall, the paper is well motivated, mostly well written, and practically useful. It does not introduce a new training algorithm, but it does provide a fairly systematic empirical characterization that many users of reasoning models would find actionable.

## Weaknesses
1. **The main claims are framed as general “findings,” but the evidence is still narrower than the rhetoric suggests.**  
   The paper’s headline claims are broad, for example the scale threshold around “8-bit 4B” in Section 4 and the general prescriptions summarized on Pages 2 to 3. However, the main-paper evidence is still concentrated on a small set of model families and a limited set of benchmarks, with the core narrative driven mostly by Qwen3 and especially AIME25. Yes, other families and tasks are included, but much of the strongest support is deferred to appendices or only shown for one or two figures in the main paper. This matters because the central contribution is not a single benchmark win, it is a deployment “rule of thumb.” Rules of thumb need broader stress testing than what is shown here. In particular, reasoning workloads with different context structures, multilingual reasoning, tool-augmented settings, or tasks with shorter but more sensitive chains of thought may alter the trade-offs substantially.

2. **The threshold story is useful but too heuristic, and the paper does not really turn it into a predictive law.**  
   A central message is that there is a phase transition around an effective size threshold, usually described as “8-bit 4B” in Section 4 and in **Figure 2**. But the threshold is presented more as an empirical motif than as something one could predict from the memory model in Section 3. The main text gives
   \[
   M = M_{\text{weights}}(N,P_W) + M_{\text{kv}}(N,\pi_{\text{kv}},T,G),
   \]
   on Page 4, and then says the KV term is “roughly proportional” to \(N, G, T\), but there is no analytical argument for why the crossover should happen near a particular effective size. Without a more formal derivation, the threshold risks reading as a dataset- and model-family-specific observation dressed up as a principle. This is not fatal for an empirical paper, but it lowers my confidence in how transferable the threshold itself is.

3. **There is a noticeable inconsistency in the claimed threshold for KV-cache strategy selection.**  
   Earlier findings emphasize a threshold around **8-bit 4B**. However, in Section 5 on Pages 9 to 10, the text says eviction is better for models with effective size smaller than an **8-bit 8B** model, and **Finding 5** is phrased using that larger threshold. This is not a trivial wording nit. The paper’s central framing is that effective size governs strategy selection, so changing the threshold by a factor of about two in effective model size is conceptually significant. If different subproblems truly have different thresholds, that needs to be stated explicitly and justified, rather than leaving the reader with two different decision boundaries. As written, this weakens the “principled guidelines” pitch from the abstract.

4. **Some experimental choices are not fully justified, and they may materially affect the conclusions.**  
   The paper fixes temperature at 0.6 and uses budget forcing with the “Wait” continuation prompt and then a forced final-answer pattern on Page 4. These choices are reasonable, but they are not innocuous. For example, the paper itself acknowledges non-monotonicity under budget forcing in Appendix C.4 for MATH500, which already hints that forced continuation can distort the scaling curve. If the conclusions depend strongly on this forcing mechanism, then the guidance may be less about “memory-optimal reasoning” and more about “memory-optimal budget-forced decoding.” Likewise, majority voting is only one parallel-scaling protocol. The paper does test one external verifier in Section 4.1, which is good, but this is still a fairly small slice of the broader test-time scaling landscape.

5. **The evaluation metric and averaging protocol are somewhat unusual and under-discussed in the main text.**  
   On Page 4, the paper states that, unless otherwise specified, accuracy is averaged over **32 generations per instance**. Later, the KV-compression section averages over **8 generations per instance**. This is understandable for compute reasons, but it complicates direct comparison across sections. More importantly, it is not entirely clear whether this averaging protocol is estimating expected single-run accuracy, stabilizing high-variance sampling, or effectively smoothing over the very trade-offs the paper wants to expose. Since many deployment settings care about pass@1 under one actual run with a fixed sampling protocol, the relation between the reported accuracy and practical deployment performance deserves a clearer explanation in the main paper.

6. **The paper’s comparison space for KV-cache methods is still limited, which weakens the strength of the strategic recommendation in Section 5.**  
   The authors compare R-KV and StreamingLLM on the eviction side, and HQQ-style symmetric per-channel quantization on the quantization side. That is already something, but the paper’s resulting recommendation, “eviction for small models, quantization becomes competitive for larger ones,” risks being overgeneralized given the method set. Newer or more specialized KV quantizers, especially methods designed to preserve reasoning accuracy under very low precision, could plausibly change the frontier. Since Section 5 is explicitly about choosing *between* eviction and quantization, the limited method coverage matters directly for the validity of the recommendation, not just for completeness of related work.

7. **The treatment of memory is practical, but the accounting is not always fully aligned with real deployment constraints.**  
   The main text uses total memory as the objective, which is sensible. But some deployment scenarios care about peak memory, fragmentation, batching dynamics, prefill versus decode asymmetry, or throughput-constrained serving. The paper acknowledges latency and throughput only later, largely outside the core argument. This matters because the practical recommendation “increase weights” versus “increase token budget” depends not just on total bytes but on how those bytes are consumed over time. For instance, **Table 1** usefully reports static footprints, but real serving systems do not experience all memory costs identically. A strategy that is Pareto-optimal in total memory may still be unattractive under throughput or peak-memory constraints.

8. **The mathematical presentation in the main paper is a bit too coarse for a paper whose entire contribution depends on cost accounting.**  
   The memory equation in Section 3 is intentionally high level, but because the entire paper is about memory-optimal allocation, I would have liked a cleaner main-text derivation. For example, the statement that \(M_{\mathrm{kv}}\) is “roughly proportional” to \(N, G, T\) is serviceable, but it suppresses the architecture-dependent terms that actually determine the slopes of the curves across families. The exact formulas appear only in Appendix B, including
   \[
   M_{\rm kv}=G \cdot T \cdot n_{\rm layers}\cdot n_{\rm kv\_heads}\cdot d_{\rm head}\cdot 2\cdot \frac{P_{\rm native}}{8},
   \]
   and analogous expressions for eviction and quantization. Since these equations are central rather than peripheral, at least one exact version should be in the main paper, especially because the practical conclusions hinge on those scaling relations. Right now, the main text asks the reader to accept several “principled” takeaways while the precise accounting is deferred.

9. **The paper sometimes slips from Pareto-frontier observations to stronger causal interpretations.**  
   For example, Section 4 argues that for small models allocating memory to larger effective size is “strictly dominant,” partly invoking latency analysis from the appendix. That wording is too strong. What the figures establish is that, under the tested setups and metrics, certain configurations dominate others in measured memory-accuracy space. That is not the same as a general dominance statement over deployment objectives or decoding protocols. The paper would be stronger if it stayed closer to the empirical claim and avoided turning observed frontiers into universal prescriptions too quickly.

10. **Some claims are supported visually, but the quantitative reporting in the main paper could be sharper.**  
    Several key conclusions rely on visual inspection of frontier plots rather than explicit numerical comparisons or uncertainty estimates. For example, **Figure 5** supports the parallel-scaling threshold claim, but the exact margin by which parallel scaling overtakes serial scaling for large models is not quantified in the main paper. Similarly, **Figure 8** and **Figure 9** are persuasive visually, yet the robustness of “eviction better for small models” would be easier to assess with more explicit tabulation of frontier improvements or areas under the frontier. The paper is not statistically careless, but it leans heavily on qualitative curve reading for a paper making fairly categorical recommendations.

## Questions
1. The paper repeatedly emphasizes an effective-size threshold around **8-bit 4B**, but Section 5 shifts to **8-bit 8B** for the eviction-versus-quantization recommendation. Can the authors clarify whether these are genuinely different thresholds for different subproblems, or whether one of them is an artifact of the particular benchmark/model subset? A clearer unifying explanation would substantially increase my confidence.

2. How sensitive are the main conclusions to the specific **budget forcing** protocol on Page 4, especially the “Wait” continuation and forced final-answer injection? It would help to know whether the same qualitative frontier structure appears under natural stopping or under alternative continuation prompts.

3. Can the authors provide a more explicit quantitative definition of the “threshold” rather than identifying it visually from frontier plots? For example, is there a reproducible criterion based on the sign of the marginal gain per extra GB allocated to weights versus KV cache?

4. The paper reports accuracy averaged over 32 generations in some sections and 8 generations in the KV-compression section. Could the authors clarify what exactly this averaging estimates, and whether the frontier rankings remain stable under a stricter pass@1-style single-run evaluation?

5. For the KV-compression study, how much of the conclusion depends on the chosen quantizer and parameterization, such as symmetric per-channel quantization with group size 64 and residual buffer 128? If the authors have even a small robustness check in this direction, that would help.

6. In **Figure 5**, parallel scaling seems ineffective for smaller models, but it is not fully obvious whether this is due to majority voting specifically, increased KV cost, or the lower diversity/quality of small-model samples. Can the authors disentangle these effects more explicitly?

7. **Table 1** is useful, but it would help to know whether the reported memory numbers are measured peak allocations in the actual system or analytic estimates from architecture specifications. Since deployment guidance is the target, this distinction matters.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the paper. The work is primarily about memory-efficient deployment of reasoning models and does not introduce a dataset, human-subject protocol, or a clearly harmful application beyond standard LLM deployment considerations.

## Soundness Rating
3: good. The empirical methodology is generally careful and the main qualitative claims are supported by substantial experiments, but several recommendations are broader than the evidence strictly warrants, and some threshold claims remain heuristic rather than fully pinned down.

## Presentation Rating
3: good. The paper is readable, well organized, and the figures are largely effective, especially Figures 1, 2, 5, and 8. The main weakness is that some central quantitative details, especially the exact memory accounting, are pushed out of the main text, and there is a notable threshold inconsistency that should be resolved.

## Contribution Rating
3: good. This is a useful and timely empirical contribution on deployment trade-offs for reasoning LLMs. It does not establish a new theory or method, but it does provide actionable evidence that challenges the simplistic “4-bit is always best” narrative.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper addresses an important practical question, the empirical study is broad and mostly convincing, and several findings are useful for the community. I am positive overall, but only mildly so, because the core thresholds are more heuristic than principled, some conclusions are stated too categorically, and the evidence base is still narrower than the paper’s general framing suggests.

## Reviewer Confidence
4: confident. I am confident in the assessment and familiar with the relevant literature on LLM quantization, KV-cache optimization, and test-time scaling, though I did not independently verify every implementation detail beyond the paper’s presentation.