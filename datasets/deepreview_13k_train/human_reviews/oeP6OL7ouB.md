# OMG: Opacity Matters in Material Modeling with Gaussian Splatting

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
Decomposing geometry, materials and lighting from a set of images, namely inverse rendering, has been a long-standing problem in computer vision and graphics. Recent advances in neural rendering enable photo-realistic and plausible inverse rendering results. The emergence of 3D Gaussian Splatting has boosted it to the next level. An intuitive finding is that the models used for inverse rendering do not take into account the dependency of opacity w.r.t. material properties, namely cross section, as suggested by optics. Therefore, we develop a novel approach that adds this dependency to the modeling itself. Inspired by radiative transfer, we augment the opacity term by introducing a neural network that takes as input material properties to provide modeling of cross section and a physically correct activation function. The gradients for material properties are therefore not only from color but also from opacity, facilitating a constraint for their optimization. Therefore, the proposed method incorporates more accurate physical properties compared to previous works. We implement our method into 3 different baselines that use Gaussian Splatting for inverse rendering and achieve significant improvements universally in terms of novel view synthesis and material modeling.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a plug-and-play approach for enhancing Gaussian Splatting in material modeling by explicitly modeling the relationship between opacity and material properties using the Bouguer-Beer-Lambert law. The authors validate this insight through various analyses, demonstrating its correctness. Qualitative results across different methods and datasets show consistent improvements, as evidenced by performance gains across multiple metrics.

### Strengths
1. The core idea is pretty simple and straightforward, which I personally enjoyed. The authors have demonstrated the validity of their formulation from multiple perspectives, making the approach theoretically sound and insightful.
2. The proposed formulation leads to improved reconstruction quality across various datasets and methods.
3. This paper is well written and easy to follow. The entire formulation is physically sound and all the theoretical details are explained in an intuitive way for readers.
4. Given the simplicity of this method, it should be broadly applicable to future 3DGS-based material modeling approaches, potentially making a significant impact to the community.

### Weaknesses
1. While the reported quantitative metrics indicate improvement, I struggled to notice significant visual differences in the rendered RGB images. The geometric variations are more apparent in some normal renderings. Maybe additional results or visualizations could be provided to better illustrate the quality difference.
2. As mentioned by the authors, the impact of lighting frequency/spectrum is not considered, which could be an interesting future direction to model more complex materials.

### Questions
Given the simplicity of this formulation and the well-written manuscript, I don't have further questions regarding this submission. In general I enjoy reading this paper and love this simple yet effective solution. Just look at some minor issues in Weaknesses.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes to model opacity, as derived from the existing material properties, to improve Gaussian Splatting for better rendering. The work is inspired by the physical phenomenon that light intensity decays at different rates as it travels through different absorbing media. The authors map existing terms in the  GS formulation to terms in the Bouguer-Beer-Lambert law and add a new term predicted from albedo, metalness, and roughness, to cover the additional cross-section term. 

The authors also provide nice interpretations of their formulation from other perspectives such as Nerf and Taylor expansion, thereby stressing the correctness of their approach.

Since the method is plug-and-play, it was run on synthetic datasets containing glossy objects and also on real-world datasets such as Mip-nerf 360. Both the qualitative and quantitative results show that the method achieves high visual quality.

### Strengths
I like how this work incorporates a physically-based factor into the existing GS formulation. The additional term required to cover cross section also makes sense, since that should indeed be material-dependent and disentangled from geometry.

I also like the interpretations the authors provide, to view their proposed approach from other perspectives. That facilitated understanding and also boosted the reader’s confidence to a certain degree.

The method is plug and play, so if working well, it can have a big impact on how people model Gaussian Splats.

### Weaknesses
It’s surprising that this paper shows no result of transparent/translucent objects. I don’t think it suffices for a method designed to handle transparent/tanslucent appearance to show improvements on opaque objects but not on the original objects of interest. Ideally, there should be videos of view synthesis results on translucent objects as evidence to what this paper claims.

Assuming this method does handle translucency well, the big question mark in my head then is how the model deals with shape-material ambiguity. As a specific example: a cup could be due to regular cup geometry paired with regular cup material or cube geometry paired with a translucent material that’s transparent everywhere and opaque around/in the center cup shape. There should be some analysis on why this is not happening if the paper properly models transparency/translucency. A specific experiment the authors can do is setting up a synthetic scene where a shape is enclosed by some translucent material. Does the model reconstruct the translucent part or just ignore it, reconstructing the object directly?

Also, current improvements reported in the paper on opaque objects may simply be due to a bigger model / gaussian formulation with more parameters we can optimize. If this is actually the case, the whole BBL law inspiration no longer stands.

I am not fully convinced that the cross section network is really learning cross section from albedo, metalness, and roughness. In fact, I don’t think that makes sense.  Consider a translucent material that has some cross section parameter for the network to learn. This material may not have well-defined albedo, metalness, or roughness, which are properties in opaque appearance BRDFs. I hope the authors can provide some clarifications around this (see also my questions below).

### Questions
Related to the biggest weakness IMO above, have the authors tried this on translucent objects? If this doesn’t work on those objects, the basis of this paper is fundamentally challenged.

Related to my final point in Weaknesses, have the authors tried to understand what the cross section network is learning? This can be done in many ways, but the one I have in mind is seeing how a trained network responds to varying inputs of roughness, metalness, and albedo. Again, I’m very skeptical of the network learning anything physically-based. Why would albedo inform cross section? Again, they seem to be from two different worlds of material properties.

Nit: I like Figure 1a, but Figure 1b is misleading until I got to the very end of the paper, where the authors said their approach didn’t model the dependency on light frequency. I recommend removing Figure 1b if color of the light doesn’t matter in the entire paper.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper draws inspiration from the Bouguer-Beer-Lambert law in radiative transfer theory, and applies this theory to 3D Gaussian Splatting. The paper analyzes the alpha blending in 3DGS, considering it as an absorbing body. Based on this analysis, the paper proposes to add a material-affected term into the computation of $\alpha$ value, namely the cross section modeling, predicted by an MLP from the material parameters. The paper's design can be plugged into exisiting 3DGS-based inverse rendering pipelines, and experiments show that it can achieve superior performance compared with the original inverse rendering method.

### Strengths
1. Good paper writing and analysis. The paper explains its motivation and idea very clearly and intuitively, with mathematical derivations. I like the analysis subsection, which makes the paper's design even more reasonable.
2. Technical contribution and novelty. The paper points out the limitation of existing methods that disentangle opacity from material, and develops a method to add the dependency between opacity and material. I think this is a very meaningful and valuable point of view.
3. The paper experiments on 3 baseline methods in 3 different datasets, demonstrating the proposed method's applicability in different scenarios.

### Weaknesses
1. Some designs of the paper requires further explanation. See the "Questions" section for my confusion.
2. Citations. Some suggestions of additional citations:
    - Huang, Binbin, et al. "2d gaussian splatting for geometrically accurate radiance fields." ACM SIGGRAPH 2024 Conference Papers. 2024
    - Yariv, Lior, et al. "Volume rendering of neural implicit surfaces." Advances in Neural Information Processing Systems 34 (2021): 4805-4815.
    - Miller, Bailey, et al. "Objects as volumes: A stochastic geometry view of opaque solids." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.
    - Munkberg, Jacob, et al. "Extracting triangular 3d models, materials, and lighting from images." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022.
3. Subtle improvement in Fig. 4. The comparison with R3DG on Synthetic4Relight dataset demonstrates little difference. I wonder if the authors can highlight some areas with more significant differences in the figure.
4. Needs more geomentry comparison. The proposed cross section modeling provides a more physical constraint on the opacity, which I think can improve the constructed geometry. The experiment section has demonstrated qualitative results on normal maps, and I think the paper should include more quantitative comparisons on the reconstructed geometry, including normal accuaracy, and the extracted mesh if possible.
5. Lack of interpretability in the cross section modeling. The paper simply uses an MLP to predict $\sigma_\nu$, which is an implicit mapping and lacks interpretability. Since the intuition of cross section modeling is based on the law of physics, the design should also be more reasonable.
6. A minor suggestion: It will be better to use vector graphics (e.g. PDF or SVG) instead of bitmaps (e.g. PNG or JPG) in the figures.

### Questions
1. Notation for Guassian covariance matrix. What does the $R_\theta$ mean in the Gaussian covariance matrix expression $R_\theta(\Sigma_i)^{-1}$ in Eq. 2 and 9?
2. L275-277. The explanation on why the path length $s$ can be simply set to constant 1 is not clear and convincing. The authors should provide a more detailed explanation on it.
3. Implementation details of the MLP. Does it use positional encoding for the material properties, or just directly feed the properties into the MLP?
4. Experimental results show improvements on normal estimation. Will the proposed method work better on surface-based Gaussian Splatting methods, e.g. 2D Gaussian Splatting, which has a more well-defined normal and surface geometry representation?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This manuscript introduces a 3D Gaussian Splatting (3D-GS) based inverse rendering task, where opacity is conditioned on material properties as suggested by the Bouguer-Beer-Lambert law. Comparisons within 3D-GS based inverse rendering tasks and ablation studies validate the effectiveness of this approach.

### Strengths
1. The Bouguer-Beer-Lambert law is interesting and technically sound.
2. Experiments validate the effectiveness of the proposed cross-section dependency.

### Weaknesses
1. Minor improvements have been observed compared to the baseline.
2. A comparison with NeRF-based inverse rendering is missing.
3. The claim "The emergence of 3D Gaussian Splatting has boosted it to the next level" in Line 15 is not convincing. GS-based inverse rendering has proven to be far less effective than SDF-based inverse rendering frameworks like NeRO[1] in terms of performance.
4. The case presented in Figure 1 considers translucent objects, where opacity is influenced by materials. However, the experiments conducted use opaque objects.

### Questions
1. Maybe experiments on transparent or translucent objects can support the theory.

### Soundness
2

### Presentation
2

### Contribution
2
