Now I have a thorough understanding of both the paper and the reviews. Let me produce the consolidated meta-review.

## Summary

This paper introduces Online Continual Graph Learning (OCGL), a framework that bridges Online Continual Learning and Continual Graph Learning for node-level streaming environments. It formalizes the problem setting, constructs four benchmark datasets with class-incremental node streams, adapts six CL methods (ER, EWC, A-GEM, LwF, MAS, TWP) to the task-free online graph setting, and evaluates them. The paper additionally identifies the neighborhood expansion problem in GNNs as a challenge for OCGL and provides preliminary results with fixed-size neighbor sampling.

## Strengths

- **Clear formalization of a previously underspecified setting.** Section 3 defines the evolving graph stream, online mini-batching constraints, bounded compute/memory requirements, and the Past Information Store (PIS). This bridges a genuine gap between the OCL and CGL literatures (both of which exist but have not been systematically connected for node-level online learning).

- **Comprehensive benchmark with adapted CL baselines.** The paper adapts six methods (ER, EWC, A-GEM, LwF, MAS, TWP) from their original task-boundary formulations to the task-free online graph setting — e.g., running-average Fisher for EWC, reservoir sampling for replay buffers, periodic teacher updates for LwF. The hyperparameter selection protocol (Chaudhry et al., 2018b) using only the first 20% of tasks is more realistic than full-grid-search and is properly documented.

- **Empirical characterization of neighborhood expansion as a concrete obstacle.** Figure 2 quantifies how multi-hop neighborhoods grow with graph evolution (e.g., two-hop Reddit neighborhoods covering most nodes), and the paper is transparent about being forced to single-layer GCNs on Reddit as a consequence. This diagnosis is useful for the community even if the proposed sampling solution is simple.

- **Detailed per-task analysis of stability-plasticity tradeoffs.** Figure 1 provides breakdowns of per-task accuracy over time for selected methods, going beyond aggregate metrics. The observation that A-GEM shows both abrupt forgetting at task boundaries and backward transfer, while MAS stabilizes performance at the cost of plasticity, gives actionable insight for method selection.

## Weaknesses

### Fatal
None.

### Major

- **Temporal causality concern from the transductive evaluation setting.** The formal definition (Section 3) states that at time *t*, graph $\mathcal{G}^t$ contains only nodes $\{v_1, \dots, v_t\}$ that have arrived so far. However, the experimental setup (Section 5) uses "a transductive setting: validation and test nodes are not used for loss computation, but they are still used for message passing." This means that all nodes — including validation and test nodes whose class labels belong to *future* tasks in the stream — are present in the graph from the start. When the GNN processes a training mini-batch at time *t*, its message passing can aggregate features from nodes belonging to classes that have not yet appeared in the stream. This violates the temporal isolation that the OCGL definition implies. The concern is not that the comparison between methods is invalid (all methods share the same setting), but that the absolute accuracy numbers may be inflated relative to a genuinely online deployment where future nodes' features are inaccessible. The paper does not acknowledge or discuss this limitation.

- **Buffer sizes for replay methods (ER, A-GEM) are not reported.** The paper states that reservoir sampling is used for memory buffers but never specifies the buffer capacity. Performance of replay methods is highly sensitive to this parameter, and its absence prevents reproducibility and meaningful comparison with future work.

### Minor

- **Tension between the "seen only once" definition and the multi-pass hyperparameter.** The paper defines OCGL as requiring that "minibatches are seen only once and, after prediction and/or training is performed the mini-batch is discarded" (Section 3), yet the experimental setup (Section 5) lists "whether to perform multiple passes (5) on each batch" as a tuned hyperparameter. The hyperparameter selection protocol also "allow[s] the model to perform multiple passes" over the first 20% of tasks. While this relaxation has precedent in the OCL literature (Aljundi et al., 2019; Chaudhry et al., 2018b), the paper's framing as a strict online setting would benefit from acknowledging and justifying this tension, or presenting single-pass results as the primary setting.

- **Computational cost of neighborhood sampling is not measured.** The paper motivates sampling as necessary to maintain bounded compute and memory per batch (Section 3.2, Section 7), but provides no quantitative measurements of time per batch, peak memory, or speedups compared to full-neighborhood processing. Without this data, the claimed efficiency benefits remain unsubstantiated.

- **Guidance on the LwF teacher update frequency hyperparameter is absent.** The paper introduces "the number of batches after which the teacher is updated with the current model" as an additional hyperparameter for LwF in the task-free setting, but provides no discussion of reasonable values, sensitivity, or how it was tuned across datasets. Since this parameter can strongly affect distillation quality, its treatment is opaque.

- **Limited analysis of the A-GEM batch-size effect.** The paper notes that A-GEM "consistently benefits from a smaller batch size" (Section 6) and speculates it "could thus be a regularizing factor," but offers no further analysis or hypothesis testing. Given that this is one of the paper's more surprising results (counter to the usual intuition that larger batches stabilize gradient projection), deeper investigation would strengthen the contribution.

### Trivial
None.

## Nice-to-Haves

- An ablation study comparing single-pass vs. multi-pass training would clarify how much the results depend on this relaxation of the online definition. If competitive performance requires multi-pass, that is itself an important finding.
- Including computational benchmarks (time per batch, memory per batch) for the sampling experiments would substantiate the efficiency claims.
- A brief discussion of how the transductive setting differs from a fully inductive / temporally isolated evaluation, and what this implies for the absolute accuracy numbers.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. *"Neighborhood sampling is trivial / not a novel contribution."* — The paper explicitly frames sampling as "a first, simple solution" (Section 1), "the simplest solution" (Section 3.2), and concludes that "more research is required to properly address this issue" (Section 7). The contribution is in identifying and diagnosing neighborhood expansion as a problem, not in claiming novelty for the sampling technique itself. The critic's framing as an overclaimed contribution is a strawman.

2. *"The paper does not distinguish its approach from temporal graph learning works (Cini et al., Kazemi et al.)."* — Per the rules, missing related works cannot be raised as a weakness since we cannot independently verify whether the comparison is warranted. The paper does mention these works in Section 2 (line 27) and positions OCGL as focused on task-induced distribution shifts (new classes) rather than time-induced shifts, which is a defensible distinction.

3. *"Without buffer sizes the experiments are not reproducible."* — This is kept (moved to Minor) but is not fatal; buffer size is one of several reproducibility omissions.

4. *"The fixed ordering of classes is a limitation that should be acknowledged."* — Fixed class order is standard practice in CL benchmarks. Criticizing this is scope creep.

5. *"Statistical comparison across methods should use pairwise confidence intervals."* — The paper reports means and standard deviations over 5 runs, which is the standard in this community. Demanding formal hypothesis testing exceeds typical expectations for a benchmark paper.

6. *"EWC and TWP adaptations may be responsible for poor performance rather than the methods themselves."* — The paper acknowledges these are modifications and presents them transparently. All methods face the same adaptation challenge, and the paper is explicit about which modifications were made. This is not a weakness — it is honest reporting of the adaptation choices.

7. *"Sampling rationale not quantified against average degrees."* — The paper states the rationale: choosing numbers significantly lower than average degree. While a quantitative comparison would strengthen the presentation, the rationale is stated. This is a minor point kept in Minor above indirectly (computational cost not measured).

8. *"The PIS is mentioned but not used in experiments to enforce temporal isolation."* — The PIS is used to store the up-to-date graph snapshot; it is the mechanism by which the model accesses neighborhoods. The critic's expectation that PIS should "enforce temporal isolation" misunderstands its role — the temporal issue stems from the transductive setting, not from PIS design.

## Novel Insights

The harsh critic's observation about the transductive setting creating temporal leakage is the most important novel insight from the reviews. The formal OCGL definition describes an evolving graph $\mathcal{G}^t$ that only contains nodes observed up to time *t*, but the experiments place all nodes (including future-class val/test nodes) in the graph from the start. This mismatch means the model at time *t* can, through message passing, access feature information from nodes whose class labels belong to tasks that have not yet appeared in the stream. This is a genuine methodological concern that the paper should address. Beyond this, the reviews do not generate substantial insights beyond what the paper itself provides — the paper's core value is in the formalization and benchmark, not in any surprising empirical finding.

## Suggestions

1. **Acknowledge and discuss the transductive temporal issue.** Either switch to an inductive message-passing scheme (masking future nodes at each time step) or add a clear paragraph explaining that the transductive setting is standard practice, noting its implications for temporal causality, and discussing whether the relative rankings are likely to hold under stricter temporal isolation.

2. **Report memory buffer sizes for replay methods.** Specify the buffer capacity for ER and A-GEM on each dataset. This is essential for reproducibility.

3. **Clarify whether multi-pass was actually selected by the hyperparameter protocol, and present single-pass results as the primary OCGL setting** (with multi-pass as a clearly separated ablation). This aligns experiments with the stated definition.

4. **Add computational efficiency measurements** (time per batch, peak memory, with and without sampling) to support the efficiency motivation that drives the sampling experiments.

## Score and Decision

The paper makes a genuine contribution: it formalizes a previously ambiguous setting, provides a reasonably constructed benchmark, and systematically evaluates several adapted methods. The weaknesses are real but addressable — the transductive temporal issue is the most significant, but it affects all compared methods equally and does not invalidate the relative comparisons. The paper is a solid benchmark contribution that the community can build on, provided the authors add appropriate caveats and missing hyperparameters.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>