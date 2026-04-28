# AdaFlow: Efficient Long Video Editing via Adaptive Attention Slimming And Keyframe Selection

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
Text-driven video editing is an emerging research hot spot in deep learning. Despite great progress, long video editing is still notoriously challenging mainly due to excessive memory overhead. To tackle this problem, recent efforts have simplified this task into a two-step process of keyframe translation and interpolation generation, enabling the editing of more frames. However, the token-wise keyframe translation still plagues the upper limit of video length. In this paper, we propose a novel and training-free approach towards efficient and effective long video editing, termed AdaFlow. We first reveal that not all tokens of video frames hold equal importance for keyframe-consistency editing, based on which we propose an Adaptive Attention Slimming scheme for AdaFlow to squeeze the $KV$ sequence of extended self-attention. This enhancement allows AdaFlow to increase the number of keyframes for translations by an order of magnitude. In addition, an Adaptive Keyframe Selection scheme is also equipped to select the representative frames for joint editing, further improving generation quality. With these innovative designs, AdaFlow achieves high-quality long video editing of minutes in one inference, i.e., more than 1$k$ frames on one A800 GPU, which is about ten times longer than the compared methods. To validate AdaFlow, we also build a new benchmark for long video editing with high-quality annotations, termed LongV-EVAL. The experimental results show that our AdaFlow can achieve obvious advantages in both the efficiency and quality of long video editing. Our code is anonymously released at https://anonymous.4open.science/r/AdaFlow-C28F.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the text-based video editing problem from a new angle compared to prior work, emphasizing keyframe selection and efficiency for generating longer videos. Building on keyframe translation and interpolation approaches from previous studies, the authors propose an Adaptive Keyframe Selection and Adaptive Attention Slimming scheme to enhance quality and handle longer videos with more transitions. The proposed method achieves superior results and efficiency compared to TokenFlow and other baselines. Additionally, the authors introduce a benchmark, LongV-EVAL, for evaluating long video editing tasks.

### Strengths
- Keyframe selection is an important topic in video editing and remains underexplored in prior work. The proposed adaptive keyframe selection based on dynamic content is a valuable contribution.
- The proposed Long-V-Eval benchmark is valuable for advancing future video editing research.
- The evaluation results in Table 1 and Table 2 outperform prior methods. Additionally, the supplementary videos demonstrate the proposed method's ability to achieve high visual quality.

### Weaknesses
 - Additional examples of keyframe selection would clarify the approach, such as cases where changes in object angle or the appearance of new objects lead to their selection as keyframes. Specifically, it would be beneficial to see visualizations of the DIFT (Diffusion Features) used for keyframe selection, showing how changes in these features trigger the selection. The current description lacks the granularity to fully understand the adaptive selection mechanism.
- The results appear quite similar to TokenFlow; further clarification on this similarity would be beneficial. Also, the videos in the supplementary materials look slightly oversmoothed, with some detail loss and minor color mixing from the background compared to TokenFlow. This raises concerns about whether the method truly surpasses TokenFlow in visual quality, or if the improvements are marginal and come at the cost of some visual fidelity. A more detailed analysis of the differences in visual artifacts would be valuable.
- The ablation study is somewhat limited. There is no analysis of adaptive attention slimming, and it would be beneficial to include quantitative results from the ablation study. The lack of a detailed ablation for the attention slimming component makes it difficult to assess its individual contribution. It is unclear how much each component contributes to the overall performance, and whether the attention slimming is truly necessary or if it is a minor optimization.

### Questions
- What is the maximum number of frames each baseline can handle?
- For the longer videos in the supplementary materials, are the baseline videos created by simply concatenating shorter clips?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces AdaFlow, a training-free method designed to address memory constraints in long video editing. AdaFlow incorporates two key strategies: Adaptive Attention Slimming, which selectively reduces token use in self-attention to decrease memory requirements, and Adaptive Keyframe Selection, which optimizes frame selection for enhanced editing quality. According to the authors, these techniques enable AdaFlow to handle videos exceeding 1,000 frames on a single A800 GPU, reportedly achieving lengths ten times greater than prior methods. The paper also presents LongV-EVAL, a benchmark for assessing long video edits, where AdaFlow demonstrates potential advantages in both efficiency and quality over existing approaches.

### Strengths
- The paper presents AdaFlow, a training-free approach that effectively addresses memory constraints, offering a feasible alternative for handling longer videos compared to traditional methods.

- AdaFlow combines Adaptive Attention Slimming and Adaptive Keyframe Selection to optimize memory usage and frame selection, respectively. This combined approach not only reduces computational load by focusing on essential tokens in self-attention but also enhances editing quality by selecting keyframes that capture critical scene changes.

- The introduction of LongV-EVAL provides the field with a dedicated benchmark for long video editing, complete with detailed annotations and varied scenarios, which can serve as a valuable tool for assessing future developments in this area.

- Initial results on LongV-EVAL indicate that AdaFlow may outperform existing methods in both efficiency and quality, positioning it as a promising approach for text-driven long video editing.

### Weaknesses
1. **Insufficient Evidence for Claimed Contributions:** Although the paper lists three main contributions, some are not substantiated in sufficient detail. For instance, the claim of “effective” memory optimization mainly references spatial memory savings, with no discussion of runtime performance or the extra computation that Adaptive Keyframe Selection  and Adaptive Attention Slimming might add. Additionally, the benchmark’s description in the paper is limited, with definitions for key evaluation metrics lacking clarity.

2. **Limited and Incomplete Experiment Comparisons:** The experiments primarily compare AdaFlow to methods focused on consistency in short video editing, lacking comparisons to dedicated long video editing techniques. Furthermore, the ablation study is minimal, with few quantitative measures and no in-depth analysis of other components within the approach. Relying on visual clarity in a few cases does not provide sufficient evidence of AdaFlow’s overall performance.

3. **Unclear Visualization and Algorithm Details:** The pipeline visualization, particularly for the AKS module, is difficult to interpret, and specific steps like the "window_check" are not well-explained, leaving some ambiguity regarding the AKS process and its impact on overall results.

4. **Limitations of Feature-Matched Latent Propagation:** If the intended edits involve adding new content or altering major background elements, rather than just subtle changes (e.g., color or style shifts), the proposed feature-matched propagation approach may fail to preserve coherence, potentially limiting its applicability for more complex or structural video modifications.

### Questions
See weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The proposed AdaFlow enables 1k frames editing in one inference. This is realized with adaptive keyframe selection and attention slimming. In addition, this paper developed a new benchmark, LongV-EVAL, for long video editing evaluation. Experiments proves its efficient editing performance and diversity of editing types. However, this paper avoids shape editing of the video content and only shows the effect of recoloring, which is less intensive and difficult than shape editing. Considering the importance and practical value of shape editing, it is necessary to explain whether this paper can achieve this function. If this method cannot edit shape of the objects well, then the statement in the paper about "supports foreground changes" is wrong and needs to be corrected.

### Strengths
1. The proposed AAS is interesting, which only focuses on the the area to be edited in KV sequences, greatly increasing GPU memory.
2. The task is meaningful and the performance is practical. By combining keyframe editing/propagation and attention slimming, this method enables 1k frames editing on a single GPU, which is impressive.

### Weaknesses
1. Lacking some necessary discussion. As far as I know, some neural representation based video editing can also achieves consistent long video editing (I listed some of them in Questions). These methods attempts to resolve long video editing via neural representation rather than adjusting attention in diffusion model, which also achieves impressive performance. It is necessary to discuss the advantages and disadvantages of AdaFlow and these methods.

2. Lack of necessary editing results, mainly editing the shape of objects. Although authors claimed that AdaFlow supports various editing tasks. In the paper, I only found some results of the color changing, including style transfer, background or foreground recoloring. However, various SOTA video editing methods enables deformation, that is, changing the shape of the specified objects. I believe this is a very significant function and it is much more difficult to edit than recoloring. The author should provide adequate results of editing the shape of the object (e.g. removing the foreground of a video, or turning the bird in Fig.2 into a squirrel, etc.). If this is not possible, it should be acknowledged that good deformation results cannot be achieved due to the limitations of the paper's technology.

### Questions
1. What are the respective advantages and disadvantages of this paper and previous neural representation-based long video editing methods in terms of performance? Some methods should be discussed [1-3].

2. Why not show the effect of shape editing on video content? This kind of editing is much stronger than the recoloring shown in the paper, and it is more difficult to achieve, but more practical.

[1] Huang J, Sigal L, Yi K M, et al. Inve: Interactive neural video editing[J]. arXiv preprint arXiv:2307.07663, 2023.

[2] Kasten Y, Ofri D, Wang O, et al. Layered neural atlases for consistent video editing[J]. ACM Transactions on Graphics (TOG), 2021, 40(6): 1-12.

[3] Yang S, Mou C, Yu J, et al. Neural video fields editing[J]. arXiv preprint arXiv:2312.08882, 2023.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes an efficient long video editing method capable of performing video appearance editing on 1k frames within minutes. To accomplish this, the authors developed an attention slimming + key-frame selection approach and established a long-video editing benchmark.

### Strengths
1. The chosen problem setting is novel, as currently there are no video-editing solutions that can handle thousands of frames effectively.

2. The efficiency optimizations are noteworthy, particularly the single correspondence computation requirement compared to other methods.

### Weaknesses
1. The results appear to differ from traditional video editing, resembling more appearance editing focused on texture-level modifications. Even Token-Flow, which addresses similar tasks, demonstrates more ambitious edits (e.g., woman > Pixar animation, car > ice sculpture).

2. The feature similarity-based keyframe selection doesn't appear particularly innovative.

3. Several concerns regarding the attention slimming operation:
   - The KV token selection strategy appears static regardless of the editing prompt (e.g., not specifically selecting tokens from editing-relevant regions)
   - The paper lacks comparison with other extended self-attention slimming methods, such as random sampling in StoryDiffusion
   - The correspondence-based filtering may not necessarily capture representative compressed features for the entire video (compared with random sampling)

### Questions
The paper's novelty appears limited when compared to Token-Flow, with results showing minimal differentiation except for the bike case (Fig.3, the last case). I recommend:

1. Providing 2-3 comparative examples using Token-Flow's official cases
2. Including a discussion on how different attention-slimming strategies impact the results

### Soundness
3

### Presentation
3

### Contribution
2
