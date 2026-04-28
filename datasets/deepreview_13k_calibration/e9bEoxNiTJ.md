# TransCues: Boundary and Reflection-empowered Pyramid Vision Transformer for Semantic Transparent Object Segmentation

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5

## Abstract
Although glass is a prevalent material in everyday life, most semantic segmentation methods struggle to distinguish it from opaque materials. We propose $\textbf{TransCues}$, a pyramidal transformer encoder-decoder architecture to segment transparent objects from a color image. 
To distinguish between glass and non-glass regions, 
our transformer architecture is based on two important visual cues that involve boundary and reflection feature learning, respectively. 
We implement this idea by introducing a Boundary Feature Enhancement (BFE) module paired with a boundary loss and a Reflection Feature Enhancement (RFE) module that decomposes reflections into foreground and background layers. 
We empirically show that these two modules can be used together effectively, leading to improved overall performance on various benchmark datasets. In addition to binary segmentation of glass and mirror objects, we further demonstrate that our method works well for generic semantic segmentation for both glass and non-glass labels. Our method outperforms the state-of-the-art methods by a large margin on diverse datasets, achieving $\textbf{+4.2}$\% mIoU on Trans10K-v2, $\textbf{+5.6}$\% mIoU on MSD, $\textbf{+10.1}$\% mIoU on RGBD-Mirror, $\textbf{+13.1}$\% mIoU on TROSD, and $\textbf{+8.3}$\% mIoU on Stanford2D3D, demonstrate the effectiveness and efficiency of our method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces an efficient transformer-based segmentation architecture TransCues, which exhibits strong performance in segmenting transparent objects. This capability is attributed to the innovative integration of the Boundary Feature Enhancement module and the Reflection Feature Enhancement module. 
The authors show solid results on various transparent object segmentation and generic semantic segmentation benchmarks and conducts comprehensive ablation studies on their core design choices.

### Strengths
The content is well-organized and easy to follow. The motivation is well-established and the effectiveness of their solution is verified by extensive experiment. The proposed architecture achieved competitive performance on a wide range of tasks, while maintaining competitive efficiency.

### Weaknesses
The authors regard the boundary loss as their contribution, but do not provide an ablation of this module. Similarly, the reflection loss also has not been ablated.
The authors claim that their proposed approach is robust to generic semantic segmentation tasks, but do not evaluate on the most widely used semantic segmentation datasets, such as ADE20K and cityscapes.
The influence of different pretraining of the backbone is not properly assessed;
The authors claim that most semantic segmentation models struggle to distinguish between glass and non-glass regions, but does this assertion still hold true for the state of the art generic semantic segmentation model, such as SAM?

### Questions
see weakness

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes the TransCues, a transformer encoder-decoder network for the segmentation of glass, mirrors, and transparent objects. The main idea of this paper is to model the boundary and the reflection cues. Accordingly, a Boundary Feature Enhancement (BFE) module and a Reflection Feature Enhancement (RFE) module are proposed. The BFE module is implemented based on the ASPP module and the RFE module has an encoder-decoder structure. The paper runs experiments on eight existing datasets, and the comparisons show that the proposed method achieves impressive results, but with different models.

### Strengths
The paper has certain merits. 
Although the boundary and reflection cues have been explored in previous works, the paper shows that a better network design that focuses on low-level features may improve the segmentation of mirrors and glass surfaces/objects.
The paper provides extensive comparisons on eight benchmarks, which shows an overall picture of this topic.
The paper is generally easy to read and understand.

### Weaknesses
However, I have some concerns.
The first concern is about the results. The paper creates a lot of models, I.e., TransCues -T, -S, -M, -L, -B1, -B2, -B3, -B4, -B5, while some of them are based on PVTv1, and the others are based on PVTv2. During the comparisons, Table 1 uses B4, Table 2 and 5 use B2, Table 3 and 4 use B3, and the Table 6 uses B1. This makes the comparisons very messy, which may not provide meaningful analysis/discussions. What are the criterion of such selections? I note that there are only one Table (Table 13 in the supplemental) includes all nine TransCues models, from which it seems that B1 and B2 outperforms Ours-L with less parameters. How often and why does this happen is not known. 
The Abstract mentions that the RFE module ``decomposes reflections into foreground and background layers’’, however, in section 3.3, I do not find corresponding designs and the motivations of such designs. Second, section 3.4 uses pseudo ground truth reflection masks, but it is not mentioned how these pseudo labels are created. Third, the paper only discuss RFE with (Zhang et al., 2018) regarding the reflection modeling. The ICCV’21 paper ``Location-aware Single Image Reflection Removal’’ detects the strong reflections. Would it be better to use reflection removal methods to generate pseudo labels?
The boundary loss seems not a novelty. If so, I suggest to move it onto the supplemental. Otherwise, the paper needs to explain where the novelty is and provides discussions with existing methods. For example, the IJCV’22 paper ``Learning to Detect Instance-level Salient Objects Using Complementary Image Labels’’ uses canny operators to enhance the boundary information. The PMD (Lin et al. 2020) also uses ground truth boundary information for the supervision.
The feature flow in the RFE module (Figure 7 of supp.) is rather complicated and more explanation is helpful, in order to evaluate its novelty.
The placements of RFE and BFE seems casual. I can only guess the reason might be that the authors try to focus the whole network on low-level features. More explanation is helpful.
The ablation study only includes the RFE and BFE, while it is not known how much contributions the FEM, FPM and the final MLP have made to the segmentation performance.
The model relies on the detection of reflections, while for glass surface/objects segmentation, the question is whether reflections can always be detected, and if not, how does it affects the final results? The paper shows failure cases on the Trans10K-v2, but such cases seem dataset-specific. It is better to show failure cases that caused by the limitations of the proposed model.

### Questions
Please see above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a hierarchical architecture for transparent object segmentation. Boundary and reflection cues are incorporated in the module designs. Extensive experiments are conducted on multiple benchmarks, which shows the effectiveness of the proposed model. The paper is overall well-written and nicely structured.

### Strengths
1. The proposed model achieves state-of-the-art performances on multiple datasets.
2. Failure cases are well studied.
3. The paper is overall well-written and nicely structured.

### Weaknesses
1. In Fig. 5, does it show that the proposed method is consistently effective for different backbones? This should be better discussed.
2. In Table 6, it would be nice to show the computation complexity of the two designed modules for analysis.
3. How to theoretically verify that the proposed method did really make use of reflection cues? This could be better discussed.
4. It is hard to find any novel operations in the proposed reflection feature enhancement module as it simply combines existing mechanisms. It would be nice to clarify the technical novelty and theoretical contributions of the proposed modules.
5. There are extensive segmentation methods that introduce boundary-relevant loss designs or other designs. Please consider incorporating some existing boundary-relevant designs for a comparison. This can better show the superiority of your proposed boundary feature enhancement module. 
6. The related work follows that of Trans4Trans. It would be nice to add more recent related state-of-the-art works.

### Questions
Would it be possible to incorporate your model with the RGB-D modalities for an experiment? This could be discussed.

When the proposed model works on images without any transparent objects, would it create false positives? This could be assessed.

Sincerely,

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
