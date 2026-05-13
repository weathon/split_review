# UniG: Modelling Unitary 3D Gaussians for View-consistent 3D Reconstruction

- Decision: Reject
- Scores: 6, 5, 8, 5

## Abstract
In this work, we present UniG, a view-consistent 3D reconstruction and novel view synthesis model that generates a high-fidelity representation of 3D Gaussians from sparse images. 
Existing 3D Gaussians-based methods usually regress Gaussians per-pixel of each view, create 3D Gaussians per view separately, and merge them through point concatenation. Such a view-independent reconstruction approach often results in a view inconsistency issue, 
where the predicted positions of the same 3D point from different views may have discrepancies.
To address this problem, we develop a DETR (DEtection TRansformer)-like framework, which treats 3D Gaussians as decoder queries and updates their parameters layer by layer by performing multi-view cross-attention (MVDFA) over multiple input images. In this way, multiple views naturally contribute to modeling a unitary representation of 3D Gaussians, thereby making 3D reconstruction more view-consistent. 
Moreover, as the number of 3D Gaussians used as decoder queries is irrespective of the number of input views, allow an arbitrary number of input images without causing memory explosion.
Extensive experiments validate the advantages of our approach, showcasing superior performance over existing methods quantitatively (improving PSNR by 4.2 dB when trained on Objaverse and tested on the GSO benchmark) and qualitatively.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces UniG, a new 3D reconstruction and novel view synthesis model leveraging unitary 3D Gaussians for view-consistent 3D scene representation from sparse posed image inputs. Existing 3D Gaussians-based methods usually regress per-pixel 3D Gaussian for each view, create 3D Gaussians per view separately, and merge them through point concatenation. Such a view-independent reconstruction, which often results in a view inconsistency issue. UniG addresses view inconsistency in existing methods by DETR (DEtection TRansformer)-like framework, treating 3D Gaussians as decoder queries updated layer by layer
by performing multi-view cross-attention over multiple input images. This design allows UniG to maintain a single 3D Gaussian set, supporting arbitrary input views without memory expansion and ensuring consistency across views.
Experiments validate UniG's superior performance in 3D reconstruction on Objaverse and GSO datasets, achieving better results than the selected baselines qualitatively and quantitatively.

### Strengths
1. The motivation is sound and clear.
2. The proposed methods demonstrate improved performance in 3D reconstruction on the Objaverse and GSO datasets, achieving better results both qualitatively and quantitatively compared to selected baselines.
3.  The proposed methods exhibit scalability with arbitrary views: despite being trained on a fixed number of views, UniG can handle an arbitrary number of input views without a significant increase in memory usage.
4. The paper presents adequate experiments and provides a thorough ablation of the design choices in the methods.

### Weaknesses
1. The visual results are blurry and have obvious artifacts. The resolution is low (no larger than 512)
2. Under some cases, the improvements are not obvious compared with previous methods, as shown in Table 2, the PNSR improvement is only ~0.5dB.

### Questions
1. In Fig. 5, the authors demonstrate that PSNR performance improves as the number of input views increases (from 2 to 8). I am curious about the effect of continuing to increase the number of input views beyond 8. Will performance decline after reaching this point? We can observe that the performance gain diminishes when the input view count increases from 6 to 8, suggesting a potential decline in performance if this number exceeds 8.

2. In line 374, the authors state that "previous methods rely on fixed views as input," which leads to a performance drop when random input views are used. By comparing Tables 1 and 2, it appears that this method also experiences a notable performance decline (a reduction of approximately 4 dB in PSNR) with random inputs. Interestingly, however, the baseline method Splatter Image does not show this performance drop (its PSNR increases slightly from 25.6 to 25.8). This suggests that Splatter Image demonstrates superior generalization regarding input view pose distribution compared to this method. I am interested in the authors’ explanation for this difference.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces UniG, a novel 3D reconstruction and novel view synthesis model that creates high-fidelity 3D Gaussian Splatting from sparse images while maintaining view consistency. To tackle the view inconsistency issue  in traditional 3D Gaussian-based methods which directly regressing Gaussians per-pixel for each view, the authors proposed to employ a DETR-like framework that uses 3D Gaussians as decoder queries, refining their parameters through multi-view cross-attention (MVDFA) across input images. This design allows for an arbitrary number of input images without causing a memory explosion, as the number of 3D Gaussians used as queries is independent of the input views. Comprehensive experiments demonstrate UniG's superiority over existing methods in terms of quantitatively and qualitatively.

### Strengths
1. he pipeline in this submission is technically sound and is clearly written and well organized.

2. The authors, drawing inspiration from DETR, propose a Gaussian-based 3D reconstruction and novel view synthesis approach which can achieve SOTA performance. Extensive experiments have validated the model's effectiveness and outstanding performance.

3. For the comparison, the numerical results show a significant performance improvement over the baseline method in GSO data. And for the ablation study, the authors show the importance of some designs like the coarse stage initialization and refinement.

### Weaknesses
 1. Overall, the structure of this paper resembles a multi-view version of a combination between TriplaneGaussian and Instant3D and the importance of the MVDFA module and the two stages is not very convincing.

 2. Although the authors have proposed the MVDFA module to integrate coarse and refine information, attempting to address the inconsistency issue of LGM when predicting from each perspective. However, aside from Figure 1, there are no more images demonstrating the severity of this inconsistency. Additionally, what would be the result by using a simple mask on the LGM or Splatter Image prediction.

 3. A minor thing is that in Table 2, Splatter Image appears to show promising performance, similar to the results of the coarse stage proposed in the paper, but there is a lack of visual comparison with it.

[1] Zi-Xin Zou, et al., Triplane Meets Gaussian Splatting: Fast and Generalizable Single-View 3D Reconstruction with Transformers, CVPR 2024

[2] Jiahao Li, et al., Instant3D: Fast Text-to-3D with Sparse-View Generation and Large Reconstruction Model, ICLR 2024

### Questions
1. In Figure 2, why does the feature extractor of the coarse network output 3D GS, while the same module in the refinement network outputs multiview feature maps?

2. In line 152, the paper states that "during the coarse stage, one or more images are randomly selected." This raises questions about whether a frontal view image is necessary at the coarse stage, or if an arbitrary view would suffice? If an arbitrary view is acceptable, how is the correctness of the coarse output ensured? Furthermore, the paper lacks an ablation study on the number of images used during the coarse stage.

3. In the refinement stage, the 3D GS output by the coarse network are used as input for the MVDFA module. However, since the coarse model only uses a single view image as input, the 3D GS generated during the coarse stage may not align with the structure of the four-view input in the refinement stage. This raises the question of whether this discrepancy could impact the MVDFA model? In other words, how can we address the consistency issue between the 3D GS from the coarse stage and the multi-view images in the refinement stage?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a method for 3D object reconstruction (with 3D Gaussians) by employing a novel encoder-decoder framework. The method operates in a two-stage process: (a) A coarse initialization provides initial 3D Gaussians leveraging only a small subset of the input images. (b) In the refinement stage, the Gaussians are optimized using multi-view deformable attention and spatially efficient self-modules. The final 3D Gaussians are obtained by updating initial estimates based on the multi-view features.

### Strengths
- The experimental results seem particularly strong with large improvements over the baselines.

### Weaknesses
 - The introduction and the first part of the paper, in general, are badly written. It gives the feeling that it was blindly polished by an LLM that had no idea about the topic. There are many unexplained concepts or ones that seemingly mean nothing. It uses fancy words and expressions that ultimately mean nothing and only make it harder to understand what is going on in the paper. I detail this in the minor comments section.
- The title is misleading. What the authors do is 3D Object Reconstruction and not general 3D Reconstruction. I also have a hard time accepting 3DGS as a reconstruction method since, to me, reconstruction would involve estimating the camera parameters as well (which is considered given here). However, this is only my concern, and I am fine if the authors go with "3D Object Reconstruction".
- Missing comparison to other sparse-view methods, e.g., MVSplat and pixelSplat. The authors propose a sparse-view pipeline so it would be fair to compare with other similar methods. I know that MVSplat and pixelSplat reconstruct the entire scene while the proposed method only has an object. However, they should still be compared as I see no fundamental limitation that would prevent MVSplat/pixelSplat from being applied here.

The most important comment here from my side is: (a) There are missing comparisons that should be added. (b) The introduction and beginning of the paper should be rewritten. (c) The title and narrative should be changed a bit. 

Minor comments:
- L040 "view inconsistency" I am a bit unsure what this means here. I suggest the authors explain clearly here what this issue is as they build the rest of their introduction on this. 
- L044 "view-specific camera space" What is a view-specific camera space?
- L045 "These Gaussians are then converted to world space". This sentence makes no sense.
- L049 This paragraph is full of abbreviations without any explanation for them. The authors state that they use a DETR-like Transformer and they are inspired by DIG3D and TAPTR, but this says nothing without having to read all these papers. This is not a good way of writing an introduction. The authors should make sure that the general concepts and ideas are understandable just from reading the text they provide. 
- L070 "More specifically, MVDFA utilize camera modulation techniques (Karras et al., 2019; Hong et al., 2024) to diversify queries based on views." Similary as before, I have no idea what camera modulation techniques are, the authors don't even provide a single example. I had to open the cited papers and read about it, which really does break the flow of reading the introduction.
- L074 "our model prioritizes multi-view distinctions to achieve a more precise 3D representation." - Again, what does "multi-view distinction" mean? This entire thing sounds like it was polished by an LLM that had no idea what really happens. 
- L140 "In total" This is not needed. 
- L151 The authors say that they use a "unitary 3D Gaussians representation" but they never explain what such a representation is. Also, typo: "3D Gaussians representation" -> "3D Gaussian representation"
- L158 "Spatially efficient self-attention" -> What is a spatially efficient self-attention?

### Questions
See in the weaknesses section.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces a feed-forward method for 3D object reconstruction from sparse input views, utilizing 3D Gaussian Splatting (3D GS) as its scene representation. This method predicts a unified set of 3D Gaussians from multiple input images rather than generating per-view, pixel-aligned Gaussians as in previous approaches. This approach utilizes a DETR-like transformer framework, treating 3D Gaussians as decoder queries and updating their parameters through multi-view cross-attention layers. The results on several benchmark datasets demonstrate promising quality and better than some previous pixel-aligned approaches.

### Strengths
A key strength of this paper lies in its application of a DETR-like transformer framework to predict an independent unitary set of 3D Gaussians for 3D reconstruction. This method shows promise in applying such a network architecture to solve the sparse-view reconstruction problem, leading to promising results.

### Weaknesses
1. There are multiple highly relevant prior works that are neither cited nor discussed in the paper. This includes works on per-pixel Gaussian splatting prediction, such as 
    * GS-LRM: Large Reconstruction Model for 3D Gaussian Splatting 
    * GRM: Large Gaussian Reconstruction Model for Efficient 3D Reconstruction and Generation
    * pixelSplat: 3D Gaussian Splats from Image Pairs for Scalable Generalizable 3D Reconstruction
    * MVSplat: Efficient 3D Gaussian Splatting from Sparse Multi-View Images

    Additionally, other works on sparse-view 3D reconstruction and generation are also absent, including 
    * Instant3D: Fast Text-to-3D with Sparse-View Generation and Large Reconstruction Model
    * One-2-3-45++: Fast Single Image to 3D Objects with Consistent Multi-View Generation and 3D Diffusion
    * MeshLRM: Large Reconstruction Model for High-Quality Mesh
    * MeshFormer: High-Quality Mesh Generation with 3D-Guided Reconstruction Model
    * TripoSR: Fast 3D Object Reconstruction from a Single Image. 

    Without proper citation and discussion of these papers, I am highly concerned about the positioning of the proposed approach.

2. The paper criticizes the design of per-pixel Gaussian prediction in previous works (LGM, MVGamba, etc), attributing it to the low quality and view inconsistency issues. However, this argument overlooks the success of other per-pixel methods listed above, such as GS-LRM and GRM, which demonstrate high-quality, view-consistent results, which, to me, look even more visually realistic than the results shown in the paper. The paper compares primarily against weaker baselines like LGM (or others with similar or lower quality), showing improvements over LGM. However, I've seen many existing papers that have demonstrated significantly better quality than LGM, including GS-LRM, GRM, Mesh-LRM, MeshFormer, as listed above. In general, the paper fails to compare with or even discuss these stronger, state-of-the-art methods. In particular,  GS-LRM and GRM also employ per-pixel strategies yet seem to achieve even greater improvements when seeing their results in their paper and website. This kind of suggests that the design choice of per-pixel prediction may not be the main issue with the baselines (like LGM) discussed in the paper, and that there could be the other architectural factors in those models that led to the lower quality. As a result, the paper's argument for its method being inherently superior to per-pixel techniques is less convincing.

### Questions
While I think the unitary Gaussian prediction technique in the paper is promising, I am really concerned about the paper's positioning due to the absence of numerous relevant prior works. I understand that direct comparisons can be challenging, especially given that many of these previous works have not released code. However, at minimum, a thorough discussion is needed to place this work in context, and any feasible comparisons would significantly strengthen the paper. I feel, at least, the paper needs to tone down and moderate its claim by incorporating and discussing all these relevant works properly.

### Soundness
3

### Presentation
3

### Contribution
3
