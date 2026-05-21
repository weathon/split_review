---
job_id: 455083e8-ae00-4019-b599-b0b9cffeaf1d
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: IdJakw2jta.pdf
paper: Towards Long-Form Spatio-Temporal Video Grounding
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This paper is clearly within ICLR scope, specifically representation learning for vision-language video understanding, transformer architectures, and datasets/benchmarks for long-form spatio-temporal grounding.

## Minimum Quality
Pass ✅ The submission contains the expected scientific components, including abstract, introduction, related work, method, experiments with quantitative results, and conclusion. While there are important methodological and presentation issues, they do not rise to the level of an immediate desk rejection based on the provided text alone.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find hidden prompts, reviewer-targeted instructions, or other obvious manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies long-form spatio-temporal video grounding (LF-STVG), where the input videos span minutes rather than the usual tens of seconds considered in prior STVG benchmarks. The authors propose ART-STVG, an autoregressive transformer that processes frames sequentially, maintains separate spatial and temporal memory banks with selection strategies, and uses a cascaded spatial-to-temporal decoder so that spatial localization informs temporal localization. The paper also constructs extended long-form versions of HCSTVG-v2 by enlarging the validation videos to 1 to 5 minutes, and reports gains over existing STVG methods on these extensions while remaining competitive on the original short-form setting.

## Strengths
The paper tackles a relevant and underexplored problem setting. Moving STVG from short clips to multi-minute videos is a natural and important direction, and the paper articulates this motivation clearly in Section 1. I appreciated that the problem is not framed as a tiny variation of existing STVG, but as a setting where the standard "process all frames jointly" recipe becomes both computationally and statistically problematic.

The proposed high-level design is sensible. The autoregressive streaming formulation in **Figure 1** and the full architecture in **Figure 3** make the main idea easy to follow: process one frame at a time, retain history in memory banks, and use a cascaded decoder so temporal grounding can benefit from spatially localized cues. Even though I have concerns about some implementation details and missing formalization, the core architectural story is coherent and practically motivated.

The empirical trend on long videos is interesting. In **Table 1**, the advantage of ART-STVG over prior STVG baselines becomes larger as videos get longer, especially from 2 to 5 minutes. This is consistent with the paper's central claim that sequential processing with memory is more suitable than all-at-once short-form STVG models when the temporal context becomes very long. **Figure 2** also visualizes this trend clearly, and in this case the figure genuinely supports the paper's argument rather than merely decorating it.

The qualitative analysis around memory selection is useful. **Figure 5** gives an intuitive illustration that selective spatial memory can sharpen attention on the foreground target, and **Figure 6** offers a plausible explanation for the temporal-memory mechanism by showing lower similarity around event boundaries. These figures do not prove correctness on their own, but they help explain why the memory-selection heuristics could help.

The ablation section is reasonably broad. The paper does not stop at comparing the final model with prior work, but also studies temporal memory selection, spatial memory selection, cascaded vs. parallel decoding, and the effect of the number of selected spatial memories in **Tables 2 to 5**. That breadth is helpful for understanding which components matter.

The method appears computationally motivated for long videos. Although the efficiency comparison is relegated to the supplementary material, the reported low GPU memory usage compared with full-sequence baselines is at least directionally aligned with the architectural design.

## Weaknesses
1. **The optimization objective is missing from the main paper, and this is not a minor omission here.**  
   Section **3.5 on Page 7** states, "Due to limited space, please see our loss function in supplementary material." For a paper whose central contribution is a new autoregressive grounding framework with coupled spatial and temporal outputs, the training objective is part of the method, not an optional implementation detail. The reader cannot properly assess soundness from the main paper because key questions are left unanswered there: how are temporal start/end targets represented per frame, whether the probabilities in Equation **(7)** are normalized over time, how positives/negatives are balanced, and how losses are aggregated across frames.  
   Even after checking the supplementary Equation **(12)**, the formulation remains underexplained. The paper uses KL divergence between ground-truth timestamp sequences and predicted start/end probabilities, but does not define whether $\mathcal{H}_s^*$ and $\mathcal{H}_e^*$ are one-hot, softened, Gaussian-like, or otherwise distributed. This matters a lot, because a KL loss behaves very differently depending on target smoothing and normalization. A method paper should not ask the reader to simply trust that the target distributions are well defined.

2. **There is a concrete inconsistency in the temporal decoder description that makes the cascaded design hard to trust as written.**  
   In Section **3.2 on Page 5**, Equation **(5)** defines a RoI-pooled feature
   $$
   \bar{f}_i^m = \texttt{RoI}(\tilde{f}_i^m, b_i),
   $$
   and the text explicitly says this fine-grained target motion feature is extracted from the predicted box and is beneficial for temporal localization. But in the very next paragraph, Equation **(6)** feeds the temporal decoder with $[\tilde{f}_i^m, \tilde{f}_i^t]$, not $[\bar{f}_i^m, \tilde{f}_i^t]$. This is not cosmetic notation noise; it goes to the core claim that the temporal decoder is helped by spatially localized motion cues. If the actual input is the global motion feature $\tilde{f}_i^m$, then the claimed cascade is weaker than advertised. If the actual input is $\bar{f}_i^m$, then Equation **(6)** is wrong. Either way, the paper needs correction and clarification.

3. **The memory-selection mechanisms are described at a very high level, but the mathematical specification is too vague for reproducibility and for assessing whether the gains come from principled modeling or heuristic tuning.**  
   In Section **3.3, Page 6**, spatial memory selection is described as computing "the similarity between each spatial memory and the textual feature" and selecting the top-$N_s$ memories. But this is underspecified. If a memory is a query vector and the text is a sequence of token embeddings $\tilde{f}_i^t \in \mathbb{R}^{N_t \times C}$, what exact score is used,
   $$
   s_j = \max_n \cos(m_j, \tilde{f}_{i,n}^t), \quad \text{or} \quad s_j = \frac{1}{N_t}\sum_n m_j^\top W \tilde{f}_{i,n}^t,
   $$
   or something else? Which representation of the textual feature is compared against memory? Is the similarity computed per decoder block or shared across blocks?  
   The temporal memory selection in Section **3.4, Page 7** is even less formal. The paper says adjacent-memory similarities are computed, low-similarity points are treated as event boundaries, and the event closest to the current frame is selected. But there is no threshold, no segmentation rule, no handling of noisy similarity fluctuations, and no definition of "closest" when multiple segments exist. **Figure 6** is intuitive, but a figure is not a definition. These are central parts of the method, yet the paper leaves them in prose.

4. **The experimental setup for the new long-form problem is weaker than the claims suggest, because evaluation is done on extended validation videos only, with no public test split and no evidence that the extensions form a robust benchmark.**  
   On **Page 8**, the paper states that only the HCSTVG-v2 validation set is extended to 1 to 5 minutes, and all results are reported there. I understand the practical reason that source videos are only available for this dataset, but scientifically this creates a fragile evaluation protocol. There is no held-out long-form test set, no information about inter-annotator verification for the extended portions, no statistics on how often the queried event remains unique in the longer video, and no breakdown of whether extension adds truly hard distractor events or merely more irrelevant padding.  
   This matters because the central contribution is partly benchmark-oriented. If LF-STVG is to be introduced as a meaningful new setting, the benchmark construction should be described much more rigorously in the main paper, not just summarized as "we manually review the extended videos to ensure quality."

5. **The baseline story is somewhat shaky, and the very weak performance of the authors' own baseline raises fairness questions rather than strengthening the case.**  
   In **Table 1**, the "Baseline (ours)" is often dramatically worse than ART-STVG and, in the 1-minute setting, worse than strong published methods by a large margin. On the short-form setting in **Table 7**, the gap is also huge, with the baseline at 46.2/29.9 versus ART-STVG at 59.2/39.2. Since the baseline is described as architecturally similar but without memory, this seems intended to isolate the memory contribution. However, because the baseline details are pushed to the supplement, the reader cannot tell from the main paper whether the baseline is genuinely competitive or whether key capacity/design choices handicap it.  
   This matters because several claims in Section **4.1** lean heavily on comparisons to this baseline to justify the importance of memory. If the baseline is under-tuned or structurally weak for reasons beyond "no memory," those conclusions become less convincing.

6. **The comparison to prior work does not fully establish that the gains come from the proposed ideas rather than from simply using an architecture that can process long videos at all.**  
   The paper compares against short-form STVG models on multi-minute videos in **Table 1**, and unsurprisingly those models collapse badly as duration increases. That comparison is informative, but it is also somewhat stacked: those methods were not designed for streaming inference with bounded memory. The more revealing question is how much of ART-STVG's gain comes from the autoregressive long-video formulation itself, versus the selective memory modules, versus the cascaded spatial-temporal design.  
   The ablations help somewhat, but not enough. For example, **Table 4** shows only a modest gain for cascaded over parallel decoding, and **Tables 2 and 3** show memory selection matters, but the paper still lacks a stronger decomposition such as: streaming without memory, streaming with non-selective memory, streaming with simple recurrent summarization, streaming with a fixed sliding window, etc. Without such controls, the scientific contribution is harder to localize.

7. **There are important evaluation details missing from the main paper, and some of the reported tables have visible presentation/notation issues that reduce trust.**  
   **Tables 2 and 3** label a metric as "m_vIoT" instead of "m_vIoU", and the first two columns use symbols like "0" and "∅" in a way that is not self-explanatory. This sounds minor, but these ablation tables are doing real argumentative work, so sloppy notation matters.  
   More broadly, the main paper omits important implementation choices that affect interpretation: memory-bank growth over long videos, whether there is any cap on memory size, how training with 64-frame clips transfers to 5-minute videos at inference, whether gradients propagate through the entire autoregressive history during training or are truncated, and how VidSwin is applied causally when "previous frames are also used as input" on **Page 4**. A method that markets itself as streaming should be very explicit about what is and is not causal.

8. **The claimed efficiency advantage is not integrated into the main experimental case, even though it is one of the paper's selling points.**  
   A substantial part of the motivation in Section **1** is computational, namely that full-sequence STVG models face GPU-memory bottlenecks on long videos. Yet the main paper does not provide a runtime or memory table. The only such comparison is in supplementary **Table 8**, which is not supposed to carry the paper's core evidentiary burden. If efficient scaling is a central claim, there should be a main-paper comparison showing memory/runtime as video length increases, not just for 64-image inference on a single GPU.

9. **The qualitative figures are helpful but also expose that some evidence is still anecdotal rather than systematic.**  
   I liked **Figure 5**, but it compares attention maps "with" and "without" selective spatial memory for a single example. That is illustrative, not decisive. Similarly, **Figure 6** gives an appealing segmentation picture for temporal memory, but the paper does not quantify boundary-detection quality or show failure frequency when similarity dips do not correspond to true event boundaries. The figures support plausibility, but the paper occasionally leans on them as if they are stronger evidence than they really are.

10. **The paper's positioning against related work is decent inside STVG, but thinner than it should be for long-video modeling.**  
   The Related Work section mentions long-term video understanding and memory-based transformers, but the experimental section does not compare against stronger generic long-video strategies adapted to STVG, such as chunking/sliding-window variants, memory transformers without the proposed selection heuristics, or hierarchical temporal aggregation baselines. Since the paper's main claim is not just "another STVG model" but "a model suited to long-form video," stronger long-video baselines would make the case much more convincing.

## Questions
1. In Section **3.2**, should Equation **(6)** take $\bar{f}_i^m$ from Equation **(5)** instead of $\tilde{f}_i^m$? If yes, please correct the notation and explain exactly how the RoI-pooled motion feature is represented before entering the temporal decoder. If no, please explain what information is actually passed from spatial to temporal grounding, because the current text suggests a stronger cascade than the equations show.

2. Please define the temporal supervision precisely. In Equation **(12)**, what are $\mathcal{H}_s^*$ and $\mathcal{H}_e^*$? Are they one-hot vectors over frames, softened distributions, or something else? How are $h_i^s$ and $h_i^e$ normalized so that KL divergence is well defined?

3. Please formalize the memory-selection rules. For spatial selection, what exact similarity function is used between memory entries and text? For temporal selection, what is the segmentation algorithm, what threshold or criterion identifies a boundary, and how sensitive are results to that choice?

4. What is the size growth of the memory banks as video duration increases? Do you keep all past memories forever, as the text on **Page 6** suggests, or is there pruning/compression? A complexity analysis as a function of video length would substantially increase confidence.

5. Can the authors provide stronger evidence that the newly extended LF-STVG datasets are not just padded versions of HCSTVG-v2 validation videos? For example, statistics on event density, distractor frequency, target-event position within the longer video, and annotation consistency would help.

6. Since all methods are trained on 20-second clips for the main long-form comparison, have the authors tried adapting stronger baselines with simple long-video strategies, such as sliding windows or chunked inference with temporal aggregation? That would help separate the benefit of the ART-STVG architecture from the benefit of merely being streamable.

7. The main motivation includes efficiency, but the main paper does not show memory/runtime scaling. Could the authors include a main-paper table or plot of GPU memory and inference time versus video length for ART-STVG and at least one representative full-sequence baseline?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics issues are apparent from the paper itself. The work uses an existing video dataset and extends it for a new benchmark setting. My concerns are scientific rather than ethical, centering on benchmark construction detail and evaluation rigor rather than harm, privacy, or fairness.

## Soundness Rating
2: fair. The core idea is plausible and supported by promising experiments, but key parts of the method are underspecified in the main paper, there is a notable equation-level inconsistency around the cascaded decoder, and the benchmark/evaluation protocol leaves nontrivial questions unanswered.

## Presentation Rating
2: fair. The paper is readable at a high level and several figures, especially **Figures 1, 3, 5, and 6**, are helpful, but important technical details are missing from the main text, notation is occasionally inconsistent, and some tables contain labeling issues that weaken clarity.

## Contribution Rating
2: fair. The long-form STVG setting is meaningful and the empirical trends are interesting, but the paper does not yet provide enough methodological precision and benchmark rigor for me to view the contribution as clearly above the ICLR bar in its current form.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper asks a good question and has a potentially useful architecture, but too many core pieces are underdefined or internally inconsistent, and the experimental case for a new long-form benchmark is not yet rigorous enough for a confident positive recommendation.

## Reviewer Confidence
4: confident. I am confident in this assessment and checked the method description, equations, figures, and result tables carefully, though some missing implementation details in the paper prevent full verification.