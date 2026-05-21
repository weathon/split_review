---
job_id: 37f609ed-b310-4107-882c-4d6814bb90d2
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: Kw2mvnzCoc.pdf
paper: TSPULSE: Tiny Pre-Trained Models With Disentangled Representations for Rapid Time-Series Analysis
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies self-supervised representation learning and transfer learning for time-series, with an explicit focus on disentangled embeddings and downstream diagnostic tasks.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction, related work discussion, methodology, experiments, results, and conclusion; despite several important methodological and clarity issues, it meets the minimum bar for full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, manipulative instructions, or other signs of attempted review manipulation in the provided paper content.

# Expected Review Outcome:
## Summary
This paper proposes TSPulse, a family of very small pre-trained time-series models built around disentangled representations across temporal, spectral, and semantic views. The method combines dual-space masked reconstruction, semantic signature prediction, task-specific post-hoc fusers for classification and anomaly detection, and a hybrid masking strategy, and evaluates these ingredients on anomaly detection, classification, imputation, and similarity search benchmarks.

## Strengths
The paper addresses a practically relevant problem, namely whether tiny pre-trained models can be competitive for diagnostic time-series tasks without the deployment burden of much larger TSFMs. That is a useful direction, and the emphasis on CPU-friendly inference is not just marketing fluff, it matters in many industrial and edge settings.

The empirical scope is broad. The paper evaluates on four downstream task families and a large number of datasets overall, and this breadth is stronger than many time-series representation papers that optimize for a single benchmark. In particular, the anomaly detection evaluation on TSB-AD and the classification evaluation on UEA cover standard public benchmarks that readers will recognize.

The efficiency story is one of the more convincing parts of the paper. Table 3 in the appendix reports substantial reductions in parameter count, CPU inference time, GPU inference time, and memory relative to larger pre-trained baselines, and the central claim that the model is genuinely tiny is supported. Even if one debates some of the comparison framing, the raw efficiency numbers are valuable.

The architecture is intuitively motivated. Figure 2 gives a reasonably complete overview of how the time patches, FFT patches, and register tokens flow through the encoder, backbone, decoder, and multiple heads. The segmentation of the embedding into temporal, spectral, and semantic parts is one of the more concrete aspects of the paper, and the figure helps the reader understand what the authors mean by “disentangled” operationally.

I also found Figure 3 useful from a systems perspective. It makes clear that the paper is not really proposing one monolithic downstream recipe, but rather a backbone plus task-specific downstream differentiators, namely hybrid masking for imputation, semantic register embeddings for search, TSLens for classification, and multi-head triangulation for anomaly detection. Ironically, this figure helps reveal a weakness in the generality claim, but as a communication device it is effective.

Some ablations are informative. Table 1(b) suggests that TSLens, the two embedding scales, dual-space learning, and identity initialization of channel mixing all contribute to classification performance. Table 1(c) and Table 22/Table 23 also indicate that hybrid masking helps imputation substantially under the paper’s chosen irregular masking evaluation. Those trends are useful, even if they do not fully isolate the core contribution.

The sensitivity analysis is directionally aligned with the intended roles of the three embeddings. Table 2 reports that the semantic embedding is less sensitive to missingness, noise, and phase shifts than the temporal embedding, while the temporal embedding is highly sensitive to shifts. This at least offers some evidence that the learned views behave differently, which is a necessary condition for the paper’s representation story.

## Weaknesses
1. **The “general tiny pre-trained model” framing is overstated, because the paper actually relies on task-specialized pre-training choices and task-specific downstream modules.**  
   This is the biggest issue for me. In Section 3.1, the authors explicitly state that they “specialize the pre-training for every task through reweighting loss objectives” and Appendix A.9 goes further, describing different head weighting and even different masking strategies for different tasks, including block masking for classification-oriented pre-training and hybrid masking for imputation / AD / retrieval. That means the headline framing of one tiny versatile pre-trained model is materially inaccurate. The model family is better described as several small task-specialized checkpoints with shared design principles. This matters because most of the comparisons are against more general-purpose models such as MOMENT or UniTS. A task-specialized pre-training recipe can absolutely be useful, but it is not an apples-to-apples basis for claiming a broad advantage in “versatility” or “general-purpose” transfer.

2. **The paper bundles many ideas at once, and the experiments do not isolate which idea is actually responsible for the gains.**  
   The method includes, at minimum, dual-space learning, embedding disentanglement via segment-specific heads, semantic signature prediction, optional next-point prediction, hybrid masking, register tokens, a TSMixer backbone, identity-initialized channel mixing at fine-tuning, TSLens for classification, and multi-head triangulation for anomaly detection. That is a lot of moving parts. The ablations in Table 1 help, but they are still task-specific and incomplete. For example, there is no clean decomposition of how much gain comes from using TSMixer versus the disentanglement losses, or from hybrid masking versus raw-level masking token design, or from task-specific pre-training versus the architecture itself. Figure 3 visually reinforces how much of the paper’s performance comes from downstream specializers rather than from a single core representation-learning contribution. As written, the paper feels over-engineered, and the scientific message is blurrier than it should be.

3. **The evidence for “disentanglement” is suggestive, but not strong enough to justify the strength of the claim.**  
   The main evidence is the sensitivity analysis in Section 6 and Table 2, plus appendix PCA plots. But these results mainly show differential robustness properties under a few synthetic perturbations, not disentanglement in any rigorous representation-learning sense. Different heads trained for different targets will unsurprisingly produce embeddings with different sensitivities; that alone does not establish that the latent factors are disentangled rather than simply separated by supervision. A more convincing evaluation would quantify cross-view redundancy, linear probing for factor-specific information, or interference between views. As it stands, the paper demonstrates “role specialization” more than true disentanglement. The distinction matters because disentanglement is a strong claim in representation learning, and the paper leans on it throughout the title, abstract, and Section 6.

4. **Several mathematical definitions and losses are underspecified or awkwardly formulated, which weakens confidence in the method description.**  
   The main training objective is described only as “a weighted sum of all the above losses” at the end of Section 2, but the actual weights are not specified in the main paper, despite being central to the task-specialization story. This is not a minor omission, because those weights apparently differ across tasks and likely affect performance substantially.  
   The semantic loss definition is also murky. On Page 5, the paper defines $\mathcal{L}_{\text{sign}}=\mathrm{CE}(\mathbf{X}^{f}_{\text{sign}}, \mathbf{Y}^{f}_{\text{sign}})$, where $\mathbf{X}^{f}_{\text{sign}}$ is itself produced by applying softmax to a log-magnitude spectrum. If the target is already a soft distribution, the precise cross-entropy convention should be stated clearly, e.g., whether this is standard soft-target cross-entropy $\mathcal{L}=-\sum_i p_i \log q_i$, KL divergence, or something else. Right now, “CE” is underspecified.  
   There is also a mismatch between the rhetoric of “disentangled reconstruction across spaces and abstraction levels” and the actual mechanism, which is basically assigning different losses to disjoint segments of $\mathbf{Decoder}_{\mathrm{E}}$. That can induce specialization, but it is not a mathematically explicit disentanglement objective. If that is the intended meaning, the paper should say so more plainly.

5. **There are questionable or at least insufficiently justified signal-processing choices in the FFT branch.**  
   On Page 4 and Appendix A.10, the paper constructs $\mathbf{X}_m^f$ by applying `rfft`, discarding the last frequency bin, separately normalizing real and imaginary parts by their maximum absolute values, and concatenating them back to a length-$S$ representation. This is a fairly specific preprocessing pipeline, but there is no argument for why this normalization preserves meaningful amplitude relationships across examples or channels. Since reconstruction loss $\mathcal{L}_{\text{fft}}=\mathrm{MSE}(\mathbf{X}^f,\mathbf{Y}^f)$ is then computed in this transformed space, the exact scaling matters. The decision to discard the last bin is also asserted for dimensional consistency, not justified from a modeling perspective. These are not necessarily fatal choices, but the FFT path currently looks more hand-crafted than principled.

6. **The anomaly detection evaluation uses labeled tuning data to select the best head per dataset, which muddies the zero-shot story.**  
   Section 4.1 and Appendix A.11 state that the official tuning sets with labels are used for hyperparameter selection, including choosing the best scoring mechanism among Head\_{time}, Head\_{fft}, Head\_{pred}, and Head\_{ensemble}. This is permitted by the benchmark protocol, so it is not improper in the benchmark sense. But the presentation in the paper occasionally glosses over this and describes the results as strong “zero-shot” anomaly detection. That is only partially true. The representation is zero-shot with respect to the target training data, but the final scoring mechanism is selected using labeled tuning data. For a paper making strong zero-shot claims, this nuance should be highlighted more explicitly, especially because Figure 4 presents a dramatic advantage over trained baselines.

7. **The comparisons are not always apples-to-apples across tasks, and some baseline choices favor the paper’s setup.**  
   Imputation is the clearest example. In Section 4.3, TSPulse is evaluated zero-shot, MOMENT is evaluated zero-shot, but UniTS is prompt-tuned with 10% of the data, and some comparisons also include statistical interpolation methods. Then in the fine-tuned setting, TSPulse is compared to supervised models. These are all relevant baselines in some sense, but the framing of percentage improvements becomes slippery because the training regimes differ. Table 19 makes this especially obvious by mixing zero-shot, prompt-tuned, statistical, and supervised systems in the same table.  
   Similarly, for similarity search, the paper compares to MOMENT and Chronos but not to simpler or more directly comparable representation-learning baselines specialized for retrieval. Since retrieval is one of the claimed strengths of semantic embeddings, stronger direct retrieval baselines would have increased confidence.

8. **The classification results are strong on average, but the per-dataset table reveals a more mixed picture than the main text suggests.**  
   Table 17 shows TSPulse winning on mean accuracy, but it is not dominant across datasets. It loses to MOMENT, VQShape, T-Rep, TS2Vec, or TS-TCC on multiple datasets, sometimes by nontrivial margins, for example CharacterTrajectories, Cricket, Epilepsy, Handwriting, Heartbeat, LSST, Libras, PEMS-SF, SelfRegulationSCP1/2, SpokenArabicDigits, and UWaveGestureLibrary. That is fine, no method wins everywhere. But the paper’s main-text phrasing on Page 8, which emphasizes state-of-the-art accuracy and 5–16% gains, reads more sweeping than the detailed table supports. This matters because the central story is not “sometimes competitive,” it is “consistently strong across tasks.”

9. **The presentation has multiple clarity and notation issues, some of them surprisingly distracting for a paper with many architectural details.**  
   A few examples:  
   - Figure 2 is informative, but it is also crowded to the point of being hard to parse without repeated zooming; the six numbered annotations help, but the figure still tries to do too much.  
   - Table 1(a) contains labels such as “Headcziang.”, “Headscramble”, “Headclim”, and “Headcjtr”, which appear corrupted or inconsistent with the actual head names described in Section 3.3 and Appendix A.11. This is not just cosmetic, it makes the ablation table confusing.  
   - The paper alternates between “register embeddings,” “semantic embeddings,” and “short embeddings”; similarly, Table 1(b) uses “short” and “long” embedding terminology that is not aligned cleanly with the main-method terminology of temporal, spectral, and semantic embeddings.  
   - There are a number of grammatical issues and small inconsistencies, for example “meaningful insights in time-series often arises” on Page 2, and notation around $c$ versus $C$ in Section 3.1. None alone is fatal, but cumulatively they reduce readability.

10. **The paper’s own appendix weakens some of its strongest claims.**  
    Table 30 in Appendix A.15 is actually quite revealing: a unified model remains competitive, but task-specialized models still perform better on classification and anomaly detection. This supports a more modest conclusion, namely that the design is good and specialization helps, not that the paper has established a single compact general-purpose TSFM. Likewise, Table 22 and Table 23 show that hybrid pre-training is excellent for hybrid-mask evaluation, but under regular block masking, the variant without hybrid pre-training can actually be better. So the benefit of hybrid masking is conditional, not universal. I would have appreciated a more restrained discussion of such trade-offs in the main paper.

11. **The paper is weakly positioned with respect to disentangled and masked time-series representation literature.**  
    The related work includes some relevant papers, but the positioning around disentanglement is still thin. Given how central disentanglement is to the title and contributions, I expected a stronger discussion of prior work on disentangled time-series representation learning and how this paper differs conceptually and empirically. The current discussion on Page 2 and in Appendix A.6 is brief and tends to frame prior work as addressing isolated pieces, without deeply comparing objectives, guarantees, or evaluation protocols. This makes it harder to judge what is actually new beyond combining several ideas in a tiny model.

## Questions
1. The most important clarification I need is about the exact pre-training setup used for each downstream task. Please provide a concise table in the rebuttal that lists, for anomaly detection, classification, imputation, and retrieval: the checkpoint used, masking strategy, patch length, active heads, and loss weights. This would substantially improve my confidence because the current “family” versus “single model” story is too blurry.

2. Can the authors report a cleaner comparison between a single unified TSPulse checkpoint and the task-specialized checkpoints in the main paper, not only in Appendix Table 30? Right now the strongest results seem to rely on task-specific specialization, and I would like to know how much of the headline gains survive under a genuinely unified setting.

3. Please specify the exact combined pre-training loss in mathematical form, for example
   $$
   \mathcal{L} = \lambda_1 \mathcal{L}_{\text{time1}} + \lambda_2 \mathcal{L}_{\text{time2}} + \lambda_3 \mathcal{L}_{\text{fft}} + \lambda_4 \mathcal{L}_{\text{sign}} + \lambda_5 \mathcal{L}_{\text{pred}},
   $$
   along with the values of $\lambda_i$ used in each task-specialized model. Without this, the method is not fully specified.

4. For the semantic signature target, what exactly is the implementation of $\mathrm{CE}(\mathbf{X}^{f}_{\text{sign}}, \mathbf{Y}^{f}_{\text{sign}})$? Is $\mathbf{Y}^{f}_{\text{sign}}$ a softmax output over frequency bins and the loss a soft-label cross-entropy, or something else? If it is soft-label cross-entropy, please state it explicitly.

5. Could the authors provide a more direct test of disentanglement than the current robustness/sensitivity analysis in Section 6? For example, probing whether each embedding type selectively retains or discards specific controlled factors, or measuring redundancy / mutual predictability across embeddings. A stronger evaluation here could change my opinion on the strength of the representation-learning claim.

6. For anomaly detection, can the authors report performance of the fixed ensemble rule without per-dataset head selection from labeled tuning data? Figure 4 and the current text give the impression of broad zero-shot strength, but the extent to which head selection contributes to the gain is not obvious from the main paper.

7. For classification, Table 17 suggests the gains are uneven across datasets. Could the authors discuss failure modes, especially on datasets where TSPulse underperforms prior methods? This would help understand whether the model is especially suited to some sequence lengths, channel counts, or class structures.

8. The FFT branch includes several specific preprocessing steps, including dropping the last frequency bin and normalizing real and imaginary parts separately. Can the authors justify these choices more carefully, or provide ablations showing that the gains are not an artifact of this handcrafted representation?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No ethics review needed based on the content presented in the main paper.

## Soundness Rating
2: fair. The empirical study is broad and many claims are supported directionally, but the central claims about disentanglement and general-purpose transfer are only partially supported, and several methodological details are underspecified.

## Presentation Rating
2: fair. The paper has a clear high-level narrative and useful figures, but the exposition is crowded, some tables and notations are inconsistent, and important setup details are buried or ambiguously described.

## Contribution Rating
2: fair. The paper is practically interesting and the tiny-model results are valuable, but the contribution is diluted by heavy task-specific engineering and by a mismatch between the broad framing and the actual specialized setup.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper has real practical value, especially in showing that very small pre-trained models can be competitive on several diagnostic time-series tasks. However, the scientific story is less clean than the headline suggests: the work relies on task-specialized pre-training and downstream modules, the disentanglement evidence is not strong enough for such a central claim, and the method is described with too many moving parts and not enough isolation of what really matters. I can see why some readers would value the empirical package, but for me it falls short of the bar for a clear ICLR main-track contribution.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. It is unlikely, but not impossible, that I missed some implementation detail or intended framing.