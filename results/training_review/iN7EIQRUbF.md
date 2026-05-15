Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

The paper proposes Selective Knowledge Transfer (SKT), a framework for few-shot continual learning that uses transferability measures (specifically LogME) to select and aggregate relevant past task parameters while discarding irrelevant ones. It instantiates this as Log-evidence Progressive Prompts (LePP), which modifies Progressive Prompts by selecting the K most transferable previous prompts and aggregating them via weighted averaging. Experiments on few-shot CL benchmarks with BERT and T5 models show consistent improvements (1.7%–4.46% higher average accuracy) over existing baselines.

## Strengths

- **Novel application of transferability measures to continual learning with LMs**: The paper is the first to apply LogME and related transferability measures (PARC, TransRate, ETran) for prompt selection in CL with language models. The idea is well-motivated—LogME requires only a single forward pass per stored prompt, avoiding the backward-pass overhead of prior task-similarity approaches (e.g., training task keys or probe soft prompts). This is a meaningful efficiency gain over predecessors like PTCC or AdapterCL.

- **Consistent empirical improvements across diverse settings**: LePP outperforms Progressive Prompts across model sizes (BERT-base 110M, T5-small 60M, T5-large 770M), shot counts (10, 20, 100), and task orders. The improvements are substantial: up to 4.46% on T5-small 10-shot, 3.07% on BERT-base 10-shot, and 1.73% on T5-large. These gains hold over 5 runs and across multiple random task orders, suggesting robustness.

- **Thorough ablation suite**: The paper investigates selection strategies (random, most recent, least transferable, most transferable), aggregation mechanisms (concatenation vs. weighted averaging), number of selected prompts K, and different transferability measures. Figure 3a demonstrates that selection itself (via c-LePP concatenation) outperforms Progressive Prompts, and Figure 3c shows that weighted averaging of ALL prompts degrades relative to weighted averaging of selected prompts—both findings support that selection matters.

- **Interpretable task correlations**: Table 3 shows that LePP's selections align with human intuition (e.g., AG News frequently selects DBPedia and Yahoo, which are also topic-classification tasks). This provides useful interpretability and suggests the TM-driven selection captures meaningful task relatedness.

- **Model-agnostic framework**: SKT is formulated generally (Section 3.1) to work with Prompt Tuning, Adapter, or LoRA, and is validated on both encoder-only (BERT) and encoder-decoder (T5) architectures.

## Weaknesses

### Fatal
None.

### Major

- **The method is underspecified regarding how the weighted-averaged prompt is used architecturally, creating ambiguity about the comparison with Progressive Prompts.** Section 3.1 states that θ_t^past (the weighted average of selected prompts) is "employed jointly with θ_t to maximize the log-likelihood" (Eq. 2), but never specifies how this averaged prompt interacts with the new prompt P_t at the implementation level. In Progressive Prompts, all previous prompts are **concatenated** with the new prompt and the input embeddings, growing the prefix length linearly with task index. In LePP, the weight-averaged prompt produces a single vector of fixed length. The paper does not state whether this averaged prompt is concatenated with P_t, used as initialization for P_t, added to P_t, or treated as a separate prefix alongside P_t. This matters because a shorter prefix is architecturally different from a growing one—it could perform better simply by introducing less noise in self-attention, independently of selection. Reproducibility and proper interpretation both require this detail.

- **The comparison between Progressive Prompts and LePP in the main results confounds two changes: selection and aggregation method.** The main results (Tables 1, 2) compare LePP (selection + weighted averaging) against Progressive Prompts (all prompts + concatenation). The ablation in Figure 3a shows that switching from concatenation to weighted averaging (c-LePP → LePP) yields a 2.93% gain, while the total improvement over Progressive Prompts in the same setting is 3–4%. This means a substantial fraction of the reported gains comes from the aggregation change rather than from selection. Although Figure 3c partially addresses this by comparing K=all vs K=selected with weighted averaging, the paper should report a version of Progressive Prompts that uses weighted averaging of all prompts in the main tables to fully isolate the contribution of selection.

### Minor

- **PTCC is discussed in related work but not included as a baseline in the experiments.** PTCC (Zhang et al., 2024b) also performs similarity-based prompt weighting for CL, making it a natural competitor. While the paper argues its method is more computationally efficient (single forward pass vs. training a probe model), it does not empirically demonstrate that this efficiency-accuracy tradeoff is favorable. Including PTCC or at least explaining its omission would strengthen the evaluation.

- **Results tables omit standard deviations or confidence intervals.** All results are reported as means over 5 runs, but no variance measures are provided. With few-shot data (10–20 samples per class) and small numbers of runs, variability could be non-negligible, and without error bars it is difficult to assess whether reported improvements (e.g., 1.7% on T5-large) are statistically significant.

- **The novelty claim about being "the first exploration of applying TMs in CL with LMs" is narrow and somewhat overstated.** PTCC (cited in related work) also uses task similarity to weight prompt contributions for CL, albeit through context/label-space similarity rather than through LogME-like transferability measures. The contribution is better framed as introducing a specific class of transferability estimators (LogME, PARC, etc.) to CL, rather than the broader notion of selective knowledge transfer based on task relatedness.

- **The selection ablation in Figure 3a uses concatenation for the selection-strategy comparisons, not the weighted averaging used in the main method.** While this is understandable as a controlled comparison within the Progressive Prompts framework, it means the benefit of selection is demonstrated only with the concatenation aggregation scheme, not with the actual aggregation used in LePP. The combination of selection + weighted averaging is benchmarked only against the selection random/most-recent baselines indirectly.

### Trivial
None.

## Nice-to-Haves
- Evaluate on longer task streams (e.g., 50+ tasks) to better support scalability claims.
- Report per-task forgetting (backward transfer) to directly assess the mitigation of catastrophic forgetting.
- Analyze selection stability across different random draws of few-shot samples to confirm LogME is not overly sensitive to sampling noise.
- Include an explicit baseline that applies weighted averaging to ALL previous prompts (no selection) in the main Tables 1 and 2 for cleaner attribution.
- A concrete example or case study showing which prompts are selected vs. discarded for a specific target task.

## Removed Points
*These points were identified during review but do not reflect genuine weaknesses of the paper. They are preserved here only for completeness.*

- "There is no experiment that uses weighted averaging of all previous prompts (no selection) to measure what selection adds beyond the aggregation change." — **Factually incorrect.** Figure 3c explicitly compares K=all (weighted averaging of all prompts, i.e., no selection) with K=2,5,7,10 (weighted averaging of selected prompts) and reports that "the system's performance degrades substantially when we utilize all previous prompts." This comparison isolates the effect of selection under the same aggregation method.
- "The central experimental design cannot support the paper's central claim as stated." — **Overstated.** While the confound between selection and aggregation weakens the attribution in the main tables, the ablation studies (Fig 3a with c-LePP vs PP, Fig 3c with K=all vs K=selected) do provide supporting evidence that selection contributes positively.
- "The paper does not establish that Progressive Prompts actually suffers from this problem [lack of scalability] in the evaluated settings... the longest stream has 15 tasks." — **Scope creep.** The 15-task long benchmark is standard in this line of work (Razdaibiedina et al., 2023). Demanding longer streams is a nice-to-have, not a weakness.
- "The characterization of CAT and CTR as 'only tested on either NLP tasks or CV tasks' is a non-criticism." — This is an observation about prior work scope, not a claim about the proposed method.
- Various requests for additional experiments (e.g., T5-small ablation on K, forgetting curves, user studies) — These are suggestions for future work, not flaws in the current submission.
- Pure repetition of the confound concern in different forms — condensed into the Major weaknesses above.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the reviews is that the paper inadvertently exposes a subtle architectural sensitivity in prompt-based continual learning: the aggregation scheme (concatenation vs. weighted averaging) appears to have a larger effect on performance (~2.93%) than the selection mechanism itself. This suggests that future work on prompt-based CL should pay at least as much attention to *how* past knowledge is combined as to *which* past knowledge is selected—an insight that is orthogonal to the paper's own framing but potentially more impactful. The paper's ablation that "learning from the least transferable tasks [via concatenation] slightly improved overall performance (0.32% over Progressive Prompts)" further suggests that even noisy aggregation of all past prompts can be useful, and that the real value of selection may depend heavily on the aggregation mechanism used.

## Suggestions

1. **Specify the architectural mechanism.** Clearly state how θ_t^past (the weighted-averaged prompt) is combined with the new prompt P_t and the input embeddings. Is the averaged prompt concatenated with P_t? Used as initialization? Added to P_t? Without this, the method is not fully reproducible and the comparison with Progressive Prompts is hard to interpret.

2. **Disentangle selection from aggregation in the main results.** Include a "Progressive Prompts with weighted averaging" baseline (i.e., weighted average of all previous prompts, no selection) in Tables 1 and 2 alongside Progressive Prompts and LePP. This would allow readers to directly attribute the gains to selection vs. aggregation.

3. **Add standard deviations or confidence intervals** to all result tables, especially given the small number of runs (5) and few-shot settings where variance can be high.

4. **Include PTCC as a baseline**, or provide a clear explanation—ideally with a small-scale comparison—for why it was excluded.

5. **Tone down the novelty claim** from "first exploration of applying TMs in CL with LMs" to something like "first to apply LogME and related modern TMs for prompt selection in CL with LMs," acknowledging that PTCC uses a related (but distinct) similarity-based selection approach.

## Score and Decision

The paper addresses an important problem and presents a well-motivated approach with consistent empirical gains. However, the central experimental design conflates selection with a change in aggregation method, and the method itself is underspecified at a critical architectural level. These issues are addressable in revision but diminish the strength of the current submission's evidence. The contribution is solid but incremental.

**Score**: 6.0

**Decision**: Accept

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>