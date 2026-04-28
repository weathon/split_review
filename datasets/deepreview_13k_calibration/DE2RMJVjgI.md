# Fine-grained Separation of Action-Background for Point-Level Temporal Action Localization

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 3, 5

## Abstract
Due to the limitation of coarse-grained video-level labels, the action-background confusion is a tough problem for the weakly-supervised temporal action localization. Point-level temporal action localization recently utilizes point-level labels to overcome this difficulty to some extent. However, considering the sparsity of point-level labels, existing methods still lack the ability to effectively eliminate false positive action proposals. To address this issue, in this paper, we propose a new framework to provide guidance for fine-grained separation of action-background for the model. Specifically, the framework relies on annotated single frame labels to extend the original action features and generate dense pseudo labels, providing the model with more precise position information. Based on this information, the framework generates pseudo segment-level labels from video sequences and utilizes our proposed score contrast module and feature separation module, which are different from the previous works,to amplify the differences in scores and features between segment labels. Extensive experiments on four benchmarks verify the effectiveness of our proposed framework, and demonstrate that our method is significantly superior to previous state-of-the-art methods and obtains 3.9\% performance gains in terms of the average mAP on THUMOS’14.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper address the task of temporal action localization under point-level supervision. The authors focus on the observation that existing approaches have difficulty in discriminating the action and background, leading to significant localization and background errors. To tackle this, the authors introduce FS-PTAL, a new framework that aggregates pseudo labels based on sparse point-level annotations and enhances the contrast between the action and background. Experiments on benchmark datasets confirm the superiority of the proposed model over existing state-of-the-arts.

### Strengths
+ The manuscript is overall well-organized and easy to follow.
+ The motivation behind the work is clear and reasonable; enlarging the discrepancy between action and background frames is the key challenge in the weakly-supervised setting.
+ The proposed model surpasses the prior arts by non-trivial margins, which manifests its effectiveness well.

### Weaknesses
- The technical novelty of the paper is limited. The overall two-step framework strictly follows that of LACP (Lee & Byun, 2021), with improvements made to the original loss (i.e., Feature Separation loss), a correction to the overlapping issue between action instances during loss calculation (i.e., Score Contrast loss), and addition of new elements (i.e., Label Extension Module). While these contribute to the paper, from my view, this work seems an extension of the previous work (Lee & Byun, 2021), and the newly introduced contributions are slightly under the standard bar of top-tier conferences. Specifically, the Feature Separation loss, while using cosine similarity, is conceptually similar to contrastive learning approaches already explored in weakly supervised action localization. The Label Extension Module, relying on upsampling based on point labels, appears to be a straightforward application of known techniques rather than a novel methodological contribution. The Score Contrast loss, while addressing a practical issue, seems more like an implementation detail than a core algorithmic innovation.
- This paper lacks comprehensive analyses to substantiate the effectiveness of the proposed components. As noted in the above weakness, the model improves the previous approach with modifications and additions. However, their actual effects and how they help are not analyzed in the experiments. Also, apple-to-apple comparisons with the original method would be desirable. For example, the paper should include experiments that isolate the impact of the Feature Separation loss by comparing it directly to the original loss function in LACP, while keeping all other components constant. Similarly, the effectiveness of the Label Extension Module should be demonstrated by comparing the performance with and without this module, again while keeping other parts of the model identical. The same applies to the Score Contrast loss; its isolated contribution needs to be shown through controlled experiments. Without these comparisons, it is difficult to assess the true value of each component.
- The paper is not self-contained in its current form, distracting the readers by making them alternate between the main paper and the appendix. Also, only the two kinds of experimental results are provided in the manuscript, while the remaining ones are in the appendix. It is strongly encouraged for the authors to trim the inappropriately long content in Introduction and Related work (e.g., Figure 1 occupies too much space), and add more experimental results in the main text.

(Minor)

The reference format to PointTAD is wrong; it should be formatted as (Tan et al., 2022). Additionally, PointTAD is not a weakly-supervised approach, so the comparison with it in Table 1 is inappropriate.

### Questions
Please refer to Weakness section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the author proposes a new method for point-level temporal action localization. The proposed method utilizes multiple modules including label extension module, pseudo label mining and score contrast module to enhance the performance of point-level supervised temporal action localization. The proposed method achieves performance gain over the standard benchmark temporal action localization datasets.

### Strengths
In general, I think this paper has clear definitions, good illustrations, and exhaustive experiments to verify the effectiveness of the proposed method. The proposed method has superior performance on major benchmark datasets.

### Weaknesses
However, I still have some little concerns about this paper: 

1. The writing should be polished. There are some grammatical errors like "genearting" on page 5. Also, some abbreviations should be re-introduced like OIC on page 6, though the author introduces it on page 2. Also, all formulas should end with a comma or period, and space after the bracket, etc.

2. I think the experiment part could be revised to provide a clear comparison. First, in Table 1, the author could provide provides more recent fully supervised temporal action localization methods like ActionFormer, TriDet, etc. They can easily achieve around 66+ mean mAP@[0.3,0.7] on THUMOS14. Don't claim those state-of-the-art methods will make the result table not convincing. Also, Table 1 reports mean mAP@[0.1,0.5] and mean mAP@[0.3,0.7]. While in Table 2, the author only reports the mean mAP@[0.1,0.7]. It is confusing here. Also, Table 2 should become a step-to-step ablation, the current form is somehow weird.

### Questions
Please mainly see the weaknesses section for details.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper tackles the problem of weakly supervised temporal action detection with point-level supervision. The proposed method follows a similar pipeline to LACP and introduces design on label extension, pseudo label mining, feature separation and score contrasting to improve detection performance. Extensive experiments on popular benchmarks show improvements based on previous state-of-the-art point-level weakly-supervised methods.

### Strengths
The proposed method achieves non-trivial improvement on Thumos14 compared to previous weakly supervised method. The ablation study supports the effectiveness of each component in the framework.

### Weaknesses
 - The proposed method looks incremental on LACP (Lee & Byun (2021)). The overall pipeline, pseudo label mining, feature separation and score contrast module are very similar to LACP.  The technical contributions look like modifications to each LACP component from the engineering side. There should be more in-depth analysis to explain the motivation of each proposed design.
- Experiments: 
  - Missing important benchmark results (ActivityNet) in the main paper.
  - Missing important methods in comparison table (tab.4). Is there a reason to not compare with other point-level supervision methods (SF-Net, BackTAL and Ju et.al. ) method on ActivityNet?
  - The performance on Activitynet against video-level supervision methods does not look competitve. If this is due to the sparsity of action in activitynet videos, then the authors should provide  comparison with video-level approaches on other benchmarks (GTEA and BEOID), as GTEA and BEOID has denser action distributions and should be better according to the authors' claim. 
- Generally, the paper suffers from bad writing, including grammatical errors (subject-verb agreement, verb tense, etc), confusing wording, poor organization (introduction too long, and experiments too short), and inconsistent citation style (e.g. for pointTAD). The overall paper feels repetitive and lacks flow. The authors need to revise the whole paper thoroughly and properly organize the content in the main paper (eg. move important comparison results from supp. to main paper).
- There's a factual error in Introduction, Related Work and Comparison table, that pointTAD is in fact not a weakly supervised approach to TAD, but a fully-supervised method.

### Questions
- Figure 3 is confusing and lacking important captions. The meaning of R(S_c) and how to compute the inner and outer score is not clear in the figure. Although section 3.4 seems to explain figure 3, we don't see consistent notations in the text and figure, for example the notations in text (s_n^c , e_n^c  and R(SL_c)) do not have corresponding illustration in the figure.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a framework to mine pseudo point-level labels for improving the performance of weakly supervised temporal action localization. There are four components, including label extension, pseudo label mining, score contrast module and feature separation module. Extensive experiments on four benchmarks verify the state-of-the-art performance of the proposed framework.

### Strengths
The proposed method is well-motivated with the error analysis and is also technically sound. Extensive experiments on four benchmarks verify the state-of-the-art performance of the proposed framework.

### Weaknesses
1. The major drawback of this paper is its incremental novelty. The proposed components are all modified versions of the off-the-shelf methods, for example, label extension originates from dynamic sampling, pseudo label mining modifies the one of LACP [1], score contrast module and feature separation module also borrow the idea of OIC loss [2] and Co-Activity Similarity [3]. The modifications, while present, lack substantial technical depth and appear to be minor adjustments rather than significant innovations. The label extension, for instance, seems to be a straightforward application of dynamic sampling principles, and the pseudo-label mining, while adapted from LACP, does not introduce a fundamentally new approach to the problem. Similarly, the score contrast and feature separation modules, while inspired by OIC loss and Co-Activity Similarity, respectively, do not demonstrate a significant departure from these established methods.
2. Some important references are missing, for example, Zhou et al. [4] also explore generating high-quality pseudo labels for weakly supervised temporal action localization.
3. More ablation studies are needed, for example, the performance with a single proposed component. The absence of individual component ablation makes it difficult to assess the unique contribution of each module. It is unclear if each component is necessary for the reported performance gains, or if a subset of the proposed modules would suffice. Without this analysis, the necessity of the entire framework is questionable.
4. Qualitative results are needed to show the performance. The lack of visualizations makes it difficult to understand the practical impact of the proposed method. Visual examples of how the pseudo-labels align with ground truth, or how the feature separation module operates, would greatly enhance the paper's clarity and credibility.

### Questions
1. There are too many hyper-parameters in the proposed method, which may increase the difficulty of reproduction. How much would these hyper-parameters affect the model? Please show more sensitivity analysis of hyper-parameters.
2.  In Formula 1, why $τ_2$ is only assigned to the nearest frame of the boundary but not the outer segment like OIC loss?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
