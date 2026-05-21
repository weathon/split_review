---
job_id: 48d28f5b-6be9-4ce6-9486-d368c4de39f2
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 1EdAn5gMVv.pdf
paper: SpatialBoost: Enhancing Visual Representation Through Language-Guided Reasoning
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, centered on representation learning for vision, multimodal learning, and applications to 3D understanding and robotics.

## Minimum Quality
Pass ✅. The paper contains the expected core sections, presents a concrete method and broad experiments, and does not exhibit an immediate fatal flaw such as missing empirical validation, obvious data leakage from the provided text, or a structurally incomplete submission.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, instructions to automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes SpatialBoost, a framework for improving pre-trained vision encoders by injecting spatial knowledge expressed in language. The method builds a multi-turn spatial reasoning dataset from single-view and multi-view images using depth estimation, segmentation, and 3D reconstruction, aligns a vision encoder with an LLM, and then fine-tunes the encoder using a dual-channel attention mechanism intended to preserve pre-trained knowledge while acquiring spatial understanding. The paper evaluates the approach on a broad set of tasks including depth estimation, semantic segmentation, 3D-centric reasoning, robot learning, image classification, retrieval, and VQA.

## Strengths
The paper aims at a meaningful and timely problem, namely how to retrofit stronger 3D and spatial awareness into strong 2D-trained vision encoders without requiring large-scale native 3D pretraining. That is a useful direction for the ICLR community, especially because it bridges representation learning, multimodal supervision, and embodied/3D downstream tasks.

The empirical scope is unusually broad for this kind of paper. The main text covers dense prediction tasks (Tables 1 and 2), 3D-centric tasks (Table 3), robot learning (Table 4), and general visual tasks such as classification and retrieval (Table 5). This breadth makes the central claim easy to understand: the authors are not just chasing gains on a single spatial benchmark, they are arguing that the encoder itself becomes more useful across multiple families of tasks.

Several of the reported gains are large enough to be hard to dismiss as noise. In Table 1, the depth improvements are consistent across four encoder families, and for DINOv3 the NYUd linear RMSE improves from 0.31 to 0.25, which is substantial. In Table 2, the segmentation gains are also systematic, for example DINOv3 on ADE20K improves from 55.9 to 59.7 in linear probing. Table 4 further suggests that these representation changes matter for downstream control, not just probing, with average gains across all CortexBench domains.

Figure 1 does a good job of conveying the full pipeline at a glance. In particular, the split between spatial knowledge extraction, language conversion, and encoder fine-tuning makes the intended dataflow understandable even before reading Section 3. Figure 2 is also useful because it clarifies that the supervision is hierarchically organized across pixel-level, object-level, and scene-level reasoning rather than just being generic caption tuning.

The dual-channel attention idea is at least a plausible mechanism for preserving pre-trained capabilities during adaptation. Equation (1) is simple and interpretable, and Figure 3 communicates the architectural modification clearly. The ablation in Figure 6, although limited, is directionally consistent with the authors’ claim that naive full fine-tuning degrades general capabilities more than the proposed parameterization.

The paper also deserves credit for testing whether the method harms non-spatial performance. Table 5 is important here: the fact that ImageNet linear probing and several retrieval benchmarks improve rather than collapse supports the claim that the method is not merely overfitting to spatial supervision.

## Weaknesses
1. **The paper does not convincingly isolate what actually causes the gains, and this matters for the scientific claim.**  
The central narrative is that *language-guided multi-turn spatial reasoning* is the key to improving spatial representations. However, the method changes many things at once: new synthetic supervision, LLM-based decoding, a three-stage training pipeline, extra multi-view data, dual-channel attention, and appended scene captions. The ablations do not cleanly disentangle these factors. For example, Table 6 compares the LLM against pixel-level heads, but these baselines are not obviously matched in expressive power, supervision structure, or optimization stability. A linear head for depth or segmentation is a very weak straw baseline relative to an autoregressive LLM that can absorb structured multi-turn supervision. Likewise, the SAM/VGGT baselines are only loosely described, and it is not clear whether they are granted equally rich supervision and equally fair tuning. As a result, the paper currently supports the weaker claim that “this whole training recipe helps,” but not the stronger claim that the gain specifically comes from language-based CoT supervision.

2. **The synthetic data pipeline is the real heart of the method, but it is underspecified in the main paper.**  
Section 3.2 and the appendix make clear that the supervision is generated using multiple pre-existing models, including depth estimation, segmentation, 3D reconstruction, CLIP filtering, and GPT-4o. But the exact quality controls, failure rates, and label noise properties are not characterized in the main paper. This is important because the paper’s headline idea is knowledge transfer from language, yet much of the useful signal may simply come from distilling outputs of strong geometry and segmentation systems into the encoder. The paper does not quantify how often the generated pixel/object/scene labels are correct, how object descriptions are resolved when segmentation is imperfect, or how often GPT-generated multi-view questions are actually grounded in both views rather than hallucinated. Without that, it is hard to know whether the gains come from reasoning structure, from synthetic geometry labels, or from sheer scale of pseudo-annotation.

3. **Some of the largest empirical jumps are so dramatic that they need deeper scrutiny and stronger methodological support.**  
Table 3 is the clearest example. SigLIPv2 jumps in 3D semantic understanding from 9.2 to 55.5 mIoU, and OpenCLIP jumps from 6.9 to 54.9 mIoU. Those are not mild improvements, they are regime changes. Such large changes are possible, but when a frozen 2D encoder augmented by this training recipe suddenly becomes competitive on 3D semantic understanding, the paper needs much more explanation of the probing pipeline, feature lifting, and whether the task head or preprocessing advantages are doing part of the work. The appendix states that 3D semantic understanding uses projected point features and a linear head, but the main paper leaves too much ambiguity about how 2D features are aggregated into 3D points, how visibility/multi-view fusion is handled, and whether the evaluation protocol exactly matches prior work. These details are not cosmetic; they determine whether the huge numbers in Table 3 reflect genuine representational improvement or evaluation/projection choices.

4. **The mathematical formulation is too thin relative to the strength of the claims, and some notation is sloppy enough to hinder verification.**  
Equation (1) defines
\[
\mathrm{Attn}^{\text{final}}(\mathbf{x})=\boldsymbol{\alpha}\cdot \mathrm{Attn}(\mathbf{x}) + (1-\boldsymbol{\alpha})\cdot \mathrm{Attn}^{+}(\mathbf{x}),
\]
with \(\alpha=\sigma(\mathbf{a})\in(0,1)^d\). This is straightforward, but several critical details are omitted. Is \(\boldsymbol{\alpha}\) shared across heads, tokens, or layers, or is it a hidden-dimension-wise gate broadcast over tokens? If \(\mathbf{x}\in\mathbb{R}^{N\times d}\), how exactly is \(\boldsymbol{\alpha}\in\mathbb{R}^d\) applied, and before or after output projection? Since \(\mathrm{Attn}(\cdot)\) denotes a full attention block rather than a raw attention map, the exact insertion point matters. Also, the formal definition of the training objective is underspecified. Section 3.1 says all stages use SFT/autoregressive loss, but the loss over multi-turn data is never written explicitly. A clearer expression such as
\[
\mathcal{L}_{\text{SFT}} = -\sum_{t=1}^{T}\sum_{i=1}^{|A^t|}\log p_\theta(a^t_i \mid \mathbf{x}, Q^{1:t}, A^{1:t}_{<i})
\]
would make it much easier to verify what the model is trained to predict and how prior turns enter the context. There are also notation glitches in Section 3.1, such as \((\mathbf{x}_q^1,\mathbf{x}_x^1,\dots)\), which appears malformed, and \(\{\mathbf{x}_1,\dots,\mathbf{x}_{tt}\}\), which looks like a typo for \(t\). These are not fatal individually, but they accumulate and make the technical presentation harder to trust.

5. **The paper overclaims “reasoning” relative to what is demonstrated.**  
Figure 2 and the text repeatedly frame the dataset as multi-turn CoT reasoning that progressively builds spatial understanding. But in practice, the turns appear to be a sequence of synthetic QA pairs derived from extracted geometry, often template-based, and then fed into supervised training. That is not the same as demonstrating that the vision encoder itself learned a compositional reasoning process, rather than just features useful for tasks correlated with those labels. Table 7 shows that forward order helps somewhat over reverse/random order, which is interesting, but the differences are modest and do not establish that CoT is the crucial mechanism. The framing should be more careful: this looks more like hierarchical structured supervision than evidence of genuine chain-of-thought reasoning inside the encoder.

6. **The comparisons to prior work and neighboring approaches are not sharp enough.**  
The related work section is broad but somewhat generic. The paper positions itself against self-supervised learning, multimodal learning, and multi-view learning, but it does not sharply distinguish itself from recent efforts that inject geometry, depth, or spatial reasoning into VLMs/MLLMs. Even within the references included by the authors, works such as SpatialVLM, SpatialRGPT, and 3D-LLM are mentioned piecemeal, but the paper does not clearly explain whether SpatialBoost’s contribution is a new adaptation mechanism, a new synthetic data pipeline, a new recipe for representation tuning, or all of the above. This matters because the method risks reading as an engineering combination of existing ingredients unless the novelty boundary is drawn much more carefully.

7. **Several experimental choices are described too loosely in the main paper for a method paper making broad claims.**  
A few examples: in robot learning (Section 4.4), the paper reports “the mean of best performance across 5 evaluation runs,” which is not the cleanest protocol and may bias upward depending on selection. In dense prediction and classification, the appendix says hyperparameters are selected by grid search on validation performance, but the main paper gives almost no information about compute budgets or whether the same search budget is used for all backbones and all compared methods. In Stage 3, the model is trained for only one epoch on 300K reasoning samples, which sounds simple, but it is unclear how sequence length, conversation truncation, image resolution, and multi-view tokenization differ across settings. These details matter because they affect whether the method is broadly reproducible or highly sensitive to a specific training recipe.

8. **Figure-based evidence is weaker than it should be for a paper arguing structured spatial learning.**  
Figure 5 is supposed to support scalability, but the plots use fairly compressed ranges and only show three dataset sizes. The trends are positive, but the figure does not fully establish scaling behavior, especially since training is normalized to one epoch and larger datasets therefore also imply more distinct examples rather than a pure scaling-law analysis. Figure 6 supports the dual-channel claim, but it only visualizes a narrow slice of tasks and compares against a small set of adaptation baselines. More importantly, Figure 2 is visually persuasive but not fully faithful to the methodological ambiguity: it presents a clean story of pixel \(\rightarrow\) object \(\rightarrow\) scene reasoning, while the paper does not quantify how frequently later turns truly depend on earlier turns versus simply coexisting in the same conversation. In short, the figures are helpful for intuition, but not yet evidentiary enough for the paper’s strongest claims.

9. **Table 6 is interesting, but the conclusion drawn from it is too strong.**  
The authors state that “LLM consistently outperform pixel-level supervision methods, validating that language provides superior dense information transfer.” That is stronger than what Table 6 justifies. The table does show the LLM row performing best overall, but the baselines differ in modality, architecture, and likely optimization characteristics. For example, the SAM decoder is naturally more segmentation-oriented, the linear depth head is naturally more depth-oriented, and the VGGT setup uses a different data source and appears not fully matched. So Table 6 supports that the authors’ LLM-based recipe works better *in this implementation*, but it does not cleanly validate a general principle that language is superior to dense supervision for transferring spatial information.

10. **The presentation is readable at a high level, but there are many local errors and ambiguities that reduce confidence.**  
Examples include malformed notation in Section 3.1, inconsistent capitalization and phrasing, some citation mismatches, and textual slips such as “visual spatial reasoning conservation” in Figure 2, “visial representations” on Page 3, “isn’t SpatialBoost overfitted” in the experiment questions, and the mismatch in Table 3 discussion where the text says “SigLIPv2's 3D semantic segmentation dramatically improves from 6.9 to 54.9 mIoU,” but the table row with 6.9 to 54.9 actually corresponds to OpenCLIP, while SigLIPv2 goes from 9.2 to 55.5. None of these alone sinks the paper, but collectively they make the paper feel less polished than it should be for an ICLR main-track submission.

## Questions
1. The most important rebuttal point is causal attribution: can the authors provide cleaner evidence separating the gains from (a) dual-channel attention, (b) additional synthetic data, (c) multi-turn hierarchical ordering, (d) language supervision itself, and (e) appended scene captions? A more factorial ablation, even on one backbone, would materially increase my confidence.

2. For Equation (1), please specify precisely how \(\boldsymbol{\alpha}\) is parameterized and broadcast. Is it per layer, per hidden dimension, per head, or shared globally? At what exact point in the transformer block are the two channels merged?

3. Please write the Stage 3 training loss explicitly. Is the model trained to predict all answer tokens autoregressively over the entire multi-turn conversation, including previous answers in context? Are question tokens masked from the loss? This is currently only described verbally.

4. The 3D semantic understanding gains in Table 3 are extremely large. Please clarify the exact feature lifting pipeline from 2D images to 3D points, including projection, fusion across views, visibility handling, and whether any task-specific normalization or preprocessing differs between base and SpatialBoost models.

5. In Table 6, were all alternative supervision heads trained with the same reasoning dataset, same data budget, same optimization budget, and same dual-channel adaptation mechanism? If not, please provide a more carefully matched comparison or at least state the mismatches explicitly.

6. For Figure 2 and Table 7, can the authors quantify whether later QA turns genuinely depend on earlier turns, rather than merely being co-present in the same serialized conversation? For instance, what happens if earlier answers are masked or corrupted at training time?

7. The paper relies on several external models and GPT-4o for data generation. Can the authors provide statistics on filtering rates, failed generations, object-description quality, and estimated label noise? This would help assess how robust the pipeline is and whether the method depends on unusually clean pseudo-labels.

8. In Section 4.4, what exactly does “mean of best performance across 5 evaluation runs” mean? Is “best” selected per seed, per checkpoint, or per task? A stricter reporting protocol would improve credibility.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None beyond standard considerations for synthetic data generation and benchmark usage, which do not rise to the level of an ethics flag based on the main paper.

## Soundness Rating
2: fair. The empirical results are broad and often compelling, but the paper does not sufficiently isolate the source of improvements, and some central methodological details are under-specified.

## Presentation Rating
2: fair. The high-level story is understandable and several figures help, but the paper has enough notation issues, local inconsistencies, and missing methodological precision to hinder careful verification.

## Contribution Rating
2: fair. The problem is important and the experimental scope is strong, but the paper does not yet make a sufficiently clean scientific case for what is new and why the observed gains should be attributed to the proposed language-guided spatial reasoning mechanism rather than the overall training recipe.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is ambitious, empirically broad, and clearly promising, but the current version overstates causal claims and under-specifies the mechanism enough that I do not think it fully clears the bar for an ICLR main-track paper in its present form.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain; the paper is in my area and I checked the methodological and empirical details carefully, but some implementation ambiguities remain unresolved from the text alone.