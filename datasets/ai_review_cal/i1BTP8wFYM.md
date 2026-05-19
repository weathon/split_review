- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5
Now I have a solid understanding of the paper and the reviews. Let me produce the final consolidated review.

## Summary

This paper proposes PDEDER, a pre-trained dynamics encoder built by fine-tuning a PLM on diverse observations from multiple complex systems. The idea is to learn a generalizable encoder that maps system states into a latent space where dynamics modeling becomes easier. The authors collect 153 sets of observations from 24 systems (14 synthetic + 10 real-world), pre-train PDEDER on reconstruction and forecasting tasks per-object (without graph structure), and then fine-tune with a GNN-ODE learner for specific dynamics. They evaluate on long/short-term forecasting under in-domain and cross-domain settings, showing competitive results against five graph-based ODE baselines.

## Strengths

1. **Large-scale multi-domain pre-training data**: The paper collects 153 sets of observations from 24 complex systems spanning physics, fluid, biology, climate, and traffic domains (Section 4.2, Table 1). This diversity is a deliberate and substantial effort toward learning a generalized encoder, going well beyond typical single-system benchmarks.

2. **Cross-domain forecasting validates generalization**: The leave-one-out experiments (Table 3) show that PDEDER pre-trained without a target system ("PDEDER-sys") achieves performance on par with in-domain pre-training across 10 real-world datasets (LA, SD, PEMSxx, etc.). This directly demonstrates that the encoder captures transferable dynamics representations, not just memorizes training systems.

3. **Ablation evidence that pre-training is crucial**: Table 4 compares full PDEDER with "PDEDER w/o pre" (no pre-training) and "PDEDER freeze Θ*" (frozen pre-trained weights). Full PDEDER consistently outperforms both, and the frozen version beats no-pre-training in most settings. This quantifies the specific benefit of the proposed pre-training procedure.

4. **Two complementary pre-training objectives**: Joint reconstruction of input states and forecasting of future states (Eq. 3, Section 4.2) is a principled design for learning dynamics-enriched embeddings that encode both historical dynamics and predictive structure.

## Weaknesses

### Major

1. **Which PLM was actually used is never specified**: The paper repeatedly refers to "a PLM" and claims "we can employ any PLM" (Abstract, Section 4.2), but never states which specific pre-trained language model (e.g., GPT-2, BERT, T5, LLaMA) was employed in the experiments. Architecture size, number of layers, tokenizer, pre-trained checkpoint source—none are provided. This is a basic reproducibility requirement, not a trivial detail, since the choice of PLM dramatically affects capacity, computational cost, and empirical behavior. Without it, the results cannot be properly interpreted or reproduced.

2. **The main evaluation does not isolate the contribution of pre-training from the encoder architecture**: The primary results (Table 2) compare the full PDEDER (PLM encoder + patching + convolutional adapter + projection modules) against baselines (GNS, NDCN, ST-GODE, MT-GODE, TANGO). The ablation in Table 4 compares PDEDER with and without pre-training, but only on a subset of datasets and not in the main comparison table. Since PDEDER's encoder architecture differs substantially from the baselines' encoders, the reader cannot determine whether Table 2's gains come from the pre-training procedure or simply from having a more powerful (Transformer/PLM-based) encoder. Including "PDEDER w/o pre" as a baseline in Table 2 would directly address this gap; the paper's central claim is about *pre-training*, not the encoder architecture alone.

3. **Pre-training is interaction-free while fine-tuning is interaction-aware, creating an open question about alignment**: The paper states that pre-training is performed "without graph" (Section 4.4) — each object's trajectory is processed independently via reconstruction and forecasting losses. Yet the downstream fine-tuning uses a GNN-ODE that models multi-object interactions in the latent space. The ablation (Table 4) partially addresses this by showing pre-training helps empirically, but it does not resolve why this is the case or whether an interaction-aware pre-training objective would be more effective. This leaves a conceptual gap between the pre-training task and the downstream usage that is not discussed or analyzed.

4. **Unfulfilled claim about SINDy dynamics learner**: The methodology section (lines 58, 88) explicitly introduces "two examples of learning specific dynamics by fine-tuning PDEDER... including a black-box GNN-based neural method and a white-box method SINDy." However, only the GNN-ODE variant is evaluated in the experiments. SINDy is never tested, making this an unfulfilled claim rather than a demonstrated capability. If the paper claims PDEDER works with "any dynamics modeling method," at least two should be demonstrated.

### Minor

1. **Inconsistency in system count**: The abstract states "We evaluate PDEDER on 18 dynamic systems" (line 4), but the experiments section (line 124) lists "17 dynamics owning object interactions for validation" — 7 synthetic + 10 real-world = 17. The discrepancy is unexplained.

2. **No variance or significance measures reported**: All results (Tables 2, 3, 4, 5) are reported as point estimates without standard deviations, confidence intervals, or number of seeds. Given that pre-training and fine-tuning involve stochasticity (random initialization, data sampling, etc.), this is a non-trivial omission. At minimum, reporting averages over 3–5 seeds is standard practice for this type of work.

3. **SINDy not tested** (also listed above; listed here to indicate that the severity is minor — it does not invalidate the paper's core claims, but it is an unfulfilled claim).

### Trivial

- Abstract says "18 dynamic systems" while experiments use 17 (inconsistency noted above under Minor, but fixable with a single edit).

## Nice-to-Haves

- **Comparison against a non-ODE baseline** (e.g., a simple LSTM or MLP dynamics model) would help test whether PDEDER's embeddings genuinely make dynamics "easier to capture" or whether the gains depend on the GNN-ODE architecture specifically.
- **A simpler downstream** demonstration (e.g., linear dynamics model on top of PDEDER embeddings vs. raw states) would directly validate the claim that the encoder makes dynamics easier to model.
- **Ablation of the PLM choice** (e.g., compare GPT-2 vs. BERT vs. randomly initialized Transformer) would provide insight into whether pre-trained language model weights are actually beneficial or whether a random Transformer of similar size suffices.
- **Computational cost** (GPU hours for pre-training and fine-tuning) would help contextualize the method's practical value.

## Removed Points

These points from the input reviews were removed (with justification):

1. **"Section 4.1 is missing"** (Harsh Critic) — Removed as a parser artifact. Per instructions, missing sections stripped by the parser exist in the original submission.
2. **"Missing pre-training hyperparameters (LR, batch size, optimizer)"** (Harsh Critic) — Removed per filter rules about "trivial implementation details" and "nitpicks about reproducibility such as undisclosed hyperparameters." The paper states details are in Algorithm 1 and 2 (Section 4.4).
3. **"Related work is a dense list without critical differentiation"** (Harsh Critic) — Removed as a presentation/style nitpick. The related work does cite relevant works and situates the paper in context.
4. **"Evaluation is narrow — only tested on forecasting, not system identification"** (Harsh Critic) — Removed as scope creep. The paper is about dynamics modeling for forecasting; demanding other tasks is outside its stated scope.
5. **"IP experiment is derivative"** (Harsh Critic) — Removed. The IP experiment is a valid additional evaluation on real-world traffic data that shows practical utility; it is not derivative.
6. **"No comparison with TimeLLM, AutoTimes, LLM4TS"** (Harsh Critic) — Removed. Those are generic time-series forecasting methods, not dynamics/modeling methods. The chosen baselines (graph-based ODE methods) are appropriate for the problem setting.
7. **"Figure descriptions insufficient"** (Harsh Critic) — Removed as a likely parser artifact (figures and their detailed captions are stripped).
8. **"Pre-training does not incorporate interaction — fatal flaw"** (downgraded from Fatal to Major) — The evidence in Table 4 shows pre-training helps empirically even without interaction information, so this is not fatal. It remains a valid design concern at the Major level.
9. **Generic strengths** from Strength Finder (e.g., "addressed an important problem") — Removed. Only concrete, specific strengths are kept.
10. **"Missing variance"** — Kept as Minor (it is a legitimate concern for a machine learning paper).

## Novel Insights

Both reviews largely converge on the same observations: the paper's ambition (a generalized dynamics encoder via PLM pre-training) is timely and the data collection effort is substantial, but the evidence for the pre-training contribution specifically is not cleanly separated from architectural choices. The most interesting observation from synthesizing the reviews is that the cross-domain leave-one-out experiments (Table 3) — where PDEDER is pre-trained on all systems *except* the target — actually provide stronger evidence for generalization than the in-domain results do, yet the paper under-analyzes this finding. The fact that "PDEDER-sys" often matches in-domain performance (and sometimes beats it) is arguably the paper's most compelling result, but it is presented as a secondary experiment rather than the headline claim.

## Suggestions

1. **Specify the PLM explicitly** (which model, size, checkpoint source, which parameters are frozen/updated). This is essential for acceptance.
2. **Add "PDEDER w/o pre" to the main comparison (Table 2)** to disentangle architecture gains from pre-training gains. This data likely already exists from the ablation study.
3. **Discuss the pre-training / fine-tuning alignment gap** — explain why interaction-free pre-training benefits interaction-aware fine-tuning, or add a graph-aware pre-training objective.
4. **Either test the SINDy variant or remove the claim** from the methodology section.
5. **Report results with variance** (mean ± std over 3+ seeds).
6. **Fix the 18 vs. 17 system inconsistency** in the abstract.
