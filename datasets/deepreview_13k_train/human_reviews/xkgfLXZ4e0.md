# Correlating instruction-tuning (in multimodal models) with vision-language processing (in the brain)

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
Transformer-based language models, though not explicitly trained to mimic brain recordings, have demonstrated surprising alignment with brain activity. Progress in these models—through increased size, instruction-tuning, and multimodality—has led to better representational alignment with neural data. Recently, a new class of instruction-tuned multimodal LLMs (MLLMs) have emerged, showing remarkable zero-shot capabilities in open-ended multimodal vision tasks. However, it is unknown whether MLLMs, when prompted with natural instructions, lead to better brain alignment and effectively capture instruction-specific representations. To address this, we first investigate the brain alignment, i.e., measuring the degree of predictivity of neural visual activity using text output response embeddings from MLLMs as participants engage in watching natural scenes. Experiments with 10 different instructions (like image captioning, visual question answering, etc.) show that  MLLMs exhibit significantly better brain alignment than vision-only models and perform comparably to non-instruction-tuned multimodal models like CLIP. We also find that while these MLLMs are effective at generating high-quality responses suitable to the task-specific instructions, not all instructions are relevant for brain alignment. Further, by varying instructions, we make the MLLMs encode instruction-specific visual concepts related to the input image. This analysis shows that MLLMs effectively capture count-related and recognition-related concepts, demonstrating strong alignment with brain activity. Notably, the majority of the explained variance of the brain encoding models is shared between MLLM embeddings of image captioning and other instructions. These results indicate that enhancing MLLMs' ability to capture more task-specific information could allow for better differentiation between various types of instructions, and hence improve their precision in predicting brain responses.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper studies brain-encoding fits of instructions-tuned MLLMs in comparison with traditional methods for designing multimodal embeddings such as via CLIP. To study this question, the paper feeds different types of instructions to the MLLMs in comparison to other baselines like CLIP or vision encoders. The paper finds that instruction-tuned MLLMs have much better fits with visual areas of the brain than vision embedding models and similar performance to CLIP. The authors break down the instructions by type to identify which type of instructions have stronger correlation with visual areas of the brain and do the same with visual concept groups. The authors also include a shared variance experiment that aims to characterize whether shared features were used for each instruction group that were relevant for encoding model performance. 

Overall, I liked this paper and would vote for acceptance outside of a few concerns. It answered a relevant question about instruction-tuned MLLMs that haven’t really been explored before.

### Strengths
* Novelty with instruction-tuned MLLMs: Overall, I haven’t seen too much work on brain encoding models with instruction-tuned MLLMs. This work is highly timely.
* Well-designed and controlled experiment: The paper uses a controlled and well designed experiment for exploring brain fits.
* Instruction breakdown: I really appreciated Figure 3 and 4. I thought it was pretty interesting to see how different instruction types fit responses in the visual cortex. This was a fairly novel result. 
* I also really liked Figure 6 which focused on shared variance. This was an interesting result that showed which instruction types had a higher degree of shared features which resulted in a higher degree of brain similarity.

### Weaknesses
 * Comparisons: Overall, I think it would be better to include a baseline with a non-instruction-tuned MLLM that has the same architecture. For example, maybe BLIP-2 instead of InstructBLIP? This would have really explored the role of instruction tuning more thoroughly in comparison. BLIP-2 should be available off the shelf and I believe this would be a salient comparison. I would also be curious about how a language model of similar size would do. 
* Another concern here is that improvement over ViT-H could be due to an increase in parameters. See questions. 
* Nit: Could Figure 3 be sharpened? The text is quite blurry and difficult to read. 
* Figure 3: I still find the text in figure 3 really hard to read since it's too bright on the page. Could a different color scheme be used where the colors aren't so bright?
* I generally agree with reviewer 6bnp that some more discussion on the performance of mPLUG-Owl would be very useful. The trends are a bit difficult to see but I think having some additional text would be useful.

### Questions
* The paper focuses on the visual areas of the brain. How would the results look if the entire brain was used? A small discussion would suffice. 
* How many parameters are ViT-H and CLIP? Are they comparable?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper investigates the alignment of instruction-tuned multimodal Large Language Models (MLLMs) with brain activity, particularly focusing on how these models process visual information when prompted with natural language instructions. The study explores the brain alignment of MLLMs compared to unimodal and non-instruction-tuned multimodal models and assesses the effectiveness of various task-specific instructions on brain alignment. The paper presents a comprehensive analysis of how different instructions from MLLMs capture visual concepts and their correlation with brain activity, using fMRI data from the Natural Scenes Dataset (NSD).

### Strengths
- The paper introduces a novel approach to evaluating the brain alignment of instruction-tuned MLLMs, providing valuable insights into how these models process multimodal information in relation to human brain activity.
- The findings have implications for understanding how brain activity corresponds to the processing of multimodal information, which could be valuable for cognitive neuroscience and AI research.

### Weaknesses
 - The study relies on the NSD dataset, where subjects passively view images, which may not fully capture brain activity aligned with task-specific instructions. Active task engagement during fMRI scans could provide a more comprehensive evaluation.
- How do the authors address ethical considerations regarding the use of fMRI data, especially in relation to participant privacy and data security?

### Questions
None

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors test the ability of instruction tuned multimodal LLMs to match human visual cortex responses to static scenes in the NSD. They compare instruction tuned models to one standard multimodal model (CLIP) and a unimodal vision model.

The findings reveal that all multimodal models match visual cortex responses better in both low- and high-level visual regions. There does not seem to be a difference between CLIP and instruction-tuned models in any region. Within the instruction tuned models, there seem to be differences between tasks that best explain different parts of visual cortex, with lower-level tasks (e.g., color) better describing retinotopic areas and higher-level tasks (e.g., image captioning) better explaining higher-level tasks. Variance partitioning reveals that there is shared variance between many pairs of tasks, but some tasks like food labeling and scene recognition are more unique.

It is difficult to draw strong comparisons about these models compared to unimodal vision models though, because of the many differences (architecture, training data, task). As others have pointed out in prior work, advantages of multimodal models in visual cortex significantly decrease when you consider more balanced pairs (e.g., SLIP family models in Wang et al, and Conwell et al) and it seems likely that many of these differences would also diminish in more controlled modeled comparisons. If there are matched vision transformers trained on the same dataset, including them would strengthen the claims of the paper. 

The task comparisons are interesting, but it would help for the authors to spell out what is at stake in these investigations. Does better fit of one type of instruction mean tell us what tasks to train neural networks on for improving human-aligned AI, or does it tell us something about the tuning properties of visual cortex. It would help to clarify this, particularly in the paper introduction and discussion.

### Strengths
-	Instruction-tuned multimodal models are an interesting way to investigate task tuning, as they have higher performance than prior fine-tuned models like the taskonomy set
-	The comparison of retinotopic versus category-selective tuning is interesting, and may yield novel insights into high-level vision.
-	Variance partitioning allows a more fine-grained look into the contribution of different task tuning

### Weaknesses
- While the instruction model-brain comparisons are very interesting, it is not entirely clear what is at stake. Is the central question spelled out in the intro (lines 83-85) important for better human-alignment of AI, or in order to reveal tuning properites of the human brain? If the latter, the authors should flesh this out, and state some limits of this model comparison approach (see below). The primary goal of the study should be clarified in the introduction.
- The authors make a distinction between the advantage of multimodal models in high- versus low-level visual cortex. The results look very qualitatively similar in early versus late ROIs in Figures 2 (and also compared to other category selective regions in Figure 10) so if this is a major point, it should be backed up with a statistical analysis, (e.g., non-parametric anova, or permutation-based comparison of the vision-multimodal difference in both regions).
- Prior work has shown that when architecture and training set are matched (e.g., the SLIP family models) advantages of multimodal models largely go away. It seems likely that the advantage of the multimodal models over unimodal vision models in this paper is similarly due to different/richer training data, rather than multimodality itself. The authors should include a more controlled comparison, such as a vision transformer trained on the same dataset as the multimodal models, to strengthen their claims about the role of multimodality.
- The distinction between the different instructions/tasks could be made clearer. It seems like the tasks vary from low- high-level and many of the papers claims suggest this distinction. It would help to explicitly order the instructions and make this distinction clear early in the paper (e.g., Table 1). Without a priori labels for low- versus high-level tasks, some of the conclusions seems somewhat circular (eg a task that best explains retinotopic cortex is low-level). This ordering could also help make the results in Figure 3 more clear.
- It is difficult to see trends that are constant across the two different instruction-tuned models in Figure 3 and 11. InstructBLIP seems to show the trends highlighted in the paper, mPLUG-Owl looks quite random. Perhaps the re-ordering of the tasks/color bar suggested above will help. Alternatively, perhaps small differences across the models are being magnified in the winner-take-all plot. Either way, the authors should address these discrepancies, possibly by including quantitative metrics of similarity between the models' brain maps or by visualizing the distribution of encoding scores for each task and model.
- As a small point, the ROI labels in Figure 2 could be more intuitive. I believe “whole brain” refers to the NSDGeneral mask? If so, this should clarify that it is only visual cortex, not whole brain. pRF-Visual and FLOC-PLACES would be more clear as “retinotopic early visual cortex” and “scene-selective” or something similar
- It is unclear what Figure 5 is adding to the paper. Layerwise comparisons in different transformer networks are somewhat confusing and also seem dependent on the structure of encoders/decoders. The authors should consider moving this to the supplement. If it is important to the main findings, the author should clarify how the layerwise comparisons relate to the main text, and how they should be interpreted in light of any architectural differences across models (eg encoder vs decoder layers)
- The variance partitioning is a major strength of the paper, but it seems to only investigate shared variance between pairs of tasks. The more important question seems to be how much (if any) unique variance is explained by models tuned on any one task? And what these results can tell us about the brain. The authors should extend their variance partitioning analysis to quantify the unique variance explained by each task individually, and discuss the implications for understanding task-specific neural processing.

### Questions
-	In Figure 2 it seems like CLIP is far outperforming the randomly initialized network. Why is there no asterisks?
-	Is Figure 6 summarizing the results across NSD-General? Why show only for one representative subject rather than the average of all?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper studies the correlation between multimodal LLMs (MLLMs) and fMRI from the Natural Scenes Dataset (NSD). Specifically, they feed images and instructions to the MLLMs, cache the embeddings, and fit a linear model to map from MLLM embeddings to fMRI. They find that MLLMs exhibit higher brain alignment than vision-only models and CLIP. They also analyze the correlation of specific instructions and specific MLLM layers with brain regions. Finally, they do a variance partitioning analysis to quantify the overlap between different pairs of instructions.

### Strengths
- The central question the paper studies (the alignment of MLLMs and fMRI) is novel, as MLLMs have not been studied in prior work. The paper is also interesting because it presents some insights into the internals of MLLMs, for example, the fact that image captioning overlaps highly with other instructions.
- The presentation of the paper is good. The experiments are well-motivated and interpreted with precise language. The paper is also thorough in its setup and appropriately references prior work.
    - The ablations relating specific instructions or model layers to brain regions (Sec. 6.2) were interesting, even if for some instructions the association was inconclusive.
    - Ablations, such as the baseline “cross-subject prediction accuracy” (L174) and “variance partitioning approach” (L262), are motivated by prior work. The usage of a ridge regression based model (L242) and Pearson Correlation as a metric (L252) for brain alignment is also standard practice.

### Weaknesses
 - The experiments could include additional ablations for the input to the MLLM.
    - For example, similar to the setup in Sec. 6.1, one could ablate feeding only the image or only the instruction to the MLLM, which reduce to “vision-only” or “LLM-only” baselines. This could help control for model size / other model statistics, i.e., ViT-H might also perform worse because it is a smaller model.



### Questions
- How does the CLIP baseline work?
    - L235 states “we input both image and ground truth caption pairs” — are the CLIP image and CLIP text embeddings simply concatenated? Are you using the final pooled output from CLIP, or some intermediate layer? If you are using an intermediate layer, how do you pool across image patches / tokens?
- In L29, what does “effectively capture” mean?
    - Does this mean that the MLLM embedding correlates with the “expected” brain region that is known to do a certain type of processing? This is not obvious from the discussion in L365.
- Below are a few minor comments.
    - L280: typo; “random **initialization** of the 3 MLLMs”
- Below is a comment on the limitations section, although this note is not important for my rating and I leave this to the discretion of the authors.
    - I wish the paper would also briefly discuss the limitations of fMRI itself, and how it is not exactly synonymous with “processing in the brain.” Specifically, fMRI is imprecise, as it “measures a surrogate signal” where the “spatial specificity and temporal response” is constrained [1].
    - Nevertheless, fMRI is the most available / accessible brain signal to study, and it is still interesting to study the relation between machine learning models and fMRI.

References

[1] Logothetis, N. What we can do and what we cannot do with fMRI. *Nature* 453, 869–878 (2008).

### Soundness
3

### Presentation
3

### Contribution
3
