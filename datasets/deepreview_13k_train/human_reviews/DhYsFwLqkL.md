# Well-NeRF: Ensuring Well-Posed Neural Radiance Fields via View Frustum and Shadow Zone Based Regularization

- Decision: Reject
- Scores: 6, 6, 5, 3, 6

## Abstract
Neural Radiation Field (NeRF) often produces many artifacts with sparse inputs. These artifacts are primarily caused by learning in regions where position inference is not feasible. We assume that the main cause of this problem is the incorrect setting of boundary conditions in the learning space. To address this issue, we propose a new regularization method based on two key assumptions: (1) the position of density and color cannot be inferred in regions where the view frustum does not intersect, and (2) information inside opaque surfaces cannot be observed and inferred, and thus cannot contribute to the rendering of the image. Our method aims to transform the NeRF model into a well-posed problem by regularizing learning in regions where position inference is not possible, allowing the network to converge meaningfully. Our approach does not require scene-specific optimization and focuses on regions where position inference is not possible, thereby avoiding degradation of model performance in main regions. Experimental results demonstrate the effectiveness of our method in addressing the sparse input problem, showing outstanding performance on the Blender synthetic datasets. Our method is designed to integrate seamlessly with existing techniques, providing an effective solution for sparse input scenarios and offering a foundational approach that serves as the first clue in addressing sparse input problems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Well-NeRF, a method addressing sparse input problems in NeRF models. The proposed approach includes Frustum Score and Shadow Zone to constrain learning to well-posed regions in order to reduce artifacts. Experimental results on synthetic and real-world datasets demonstrate the method’s improvement over traditional models.

### Strengths
1. The two key assumptions are insightful and crucial. 

2. Authors did well in the organization of the paper.

3. The idea of exploring view frustum seems interesting. It would be a great point for solving problems of sparse inputs in NeRFs.

### Weaknesses
1. **Incremental Contribution**. The authors did not give enough theoretical proofs and arguments for effectiveness of their method. In the Experiment part, as the experiments largely focus on synthetic data, the contribution of this work seems incremental. Please see Question 2 for more information on this weakness.

2. **The proposed method**. Although the authors give a good and novel assumption, the proposed methods seems simple and incremental without insightful design. More validation can contribute to the soundness of your method.

3. **Insufficient Experiments**. The authors did not provide sufficient experiment about comparisons with prior works to show their performances. The experiments are mainly conducted on **NeRF Synthetic Dataset**. However, the huge amount of experiments on synthetic datasets would weaken the effectiveness of the proposed methods for real world applications. I would encourage authors to conduct more experiment to improve the soundness of the paper. 

4. **Writing**. Writing could be improved for clarity and soundness. Some typos and mistakes could be corrected i.e.  L45, 47, 50  incorrect quotation marks. L406 the sentence is not clear.

5. **Figures**. More detailed figures can improve the clarity of the paper and make your paper more understandable. Figures in the submission seem too simple for reader to fully understand your methods and arguments.

### Questions
1. Can you give the **Frustum Score** of the input views in your training settings? Also can you give a statement with **Frustum Score** to explain what kind of inputs improves the most with your method?
2. Can you give more experiments on near/far plane setting? Is the proposed method still work well or does it still improve over baselines with near/far settings other than [0.05,1000] (such as [2,6] in Figure. 5, 6)?
3. Can you provide ablation studies on lambda of Equation. 9? You can set lambda as a pre-set hyperparameter which do not change in the training. It seems interesting to detach part of the loss as another parameter. How much does this design contribute to the convergence speed?
4. Can you give the ablation studies on the number of sampling points? In Equation. 7, it seems that the parameters depend on the number of sampling points. Does the number of sampling points influence the training results?
5. Can you give more results on large-scale datasets? The datasets with sparse inputs can further demonstrate the efficacy of your method.
6. Can you provide the experimental results on comparisons with similar works with Gaussian splatting? If the results still improve greatly compared with them, it would greatly improve the performances of the work.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a simple method to improve nerf results under sparse input views (as few as 6). This method captures two intuitions: (1) points that only appear in just one input view are not learnable because the mass to learn can lie anywhere along the rays (paired with a specific scale) to show up correctly in the camera, and (2) points inside the object are not learnable since they don’t contribute to the final observed colors. The authors argue that explicitly making the network not learn those points improves the sparse-view performance.

For (1), the authors compute a mask indicating the times each point is included in all input views’ frustums, and use it to mask the loss and scale the gradients. For (2), the authors encourage nearby points to have similar colors, by gradually blending each point’s RGB with the previous point along the ray and also computing loss between the current RGB and the blended RGB.

The method is compared against nerfacto as a plug-and-play module, and the results show nerf results get improved in general with this trick. It also gets compared with FreeNerf, where near and far planes need selecting carefully when input views are sparse; this limitation can be eliminated with this paper, and similar results can be acheived.

The authors also test their method on real-world datasets including the well-known “nerf datasets” and a real in-the-wild dataset captured by the authors themselves (in the supplemental PDF).

### Strengths
This paper is strong in how it turns simple observations/intuitions into concrete implementations that improve nerf results in general. The intuitions make sense, and the end results indeed look improved.

The paper presents the ideas clearly with helpful visuals such as Figures 1 and 3.

The experiments from baseline comparisons to ablation studies are extensive and cover questions people may have very well.

### Weaknesses
I like the simplicity and modularity of this approach but the real-world, in-the-wild results shown in the supplemental material PDF are of concerning quality. Admittedly, high-quality view synthesis from just 6 input views of an in-the-wild scene is hard, but the method is shown to work well for the famous real-world “nerf datasets”. Clearly a gap here, one that needs closing before this approach is useful for any real use case.

A bigger question follows: Under sparse input views, do such per-scene learning approaches still make sense? I think when input views are sparse like this, and the quality presented is bad like this, one may be better off with learning-based approaches that learn from many scenes and generalize reasonably to the test scene at hand.

### Questions
Related to my point above about learning-based approaches that learn from multiple scenes, have the authors compared this approach against those approaches. There’s PixelNerf, and many nice works that followed. My intuition is the fewer input views you have, the better-suited a learning-based approach becomes, with priors learned from many scenes.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes, Well-NeRF, which leverages view frustum and shadow zone-based regularization to make NeRF a well-posed problem under sparse view setting. Authors show outstanding performance across various test datasets.

### Strengths
+: The paper introduces the idea of addressing sparse input issues through frustum score and shadow zone regularization, which is highly simple and reasonable.
+: The experimental results are impressive, across different scenes.
+: The analysis is fundamental in 3D reconstruction community, which may inspire other 3D research task.

### Weaknesses
-: The dataset are too small to well demonstrate the upper bound of the proposed method. And then the results are sensitive to the experimental setting, making the results less convincing. Specifically, the paper lacks a rigorous exploration of how the method performs with varying scene complexities and object sizes. The current datasets, while showing promising results, do not sufficiently cover the range of real-world scenarios where sparse view reconstruction is critical. The sensitivity to experimental settings, particularly the near and far plane parameters, is concerning. The paper needs to demonstrate that the method is robust to changes in these parameters, as the current results suggest a potential for overfitting to specific configurations.
-: Lack enough comparisons to other methods, like RegNeRF[1], ZeroRF[2], etc. The paper should include a more comprehensive comparison with state-of-the-art methods, particularly those designed for sparse view reconstruction. The absence of these comparisons makes it difficult to assess the true novelty and performance gains of the proposed method. A direct comparison with methods like RegNeRF and ZeroRF is essential to understand the relative strengths and weaknesses of the proposed approach.
-: Lack experiments on various number of views, making me unclear about the sensitivity and scalability. The paper does not adequately explore the performance of the method under varying numbers of input views. This is a critical aspect, as the method's applicability in real-world scenarios depends on its ability to handle a wide range of input data. The paper should include experiments that systematically vary the number of views to assess the method's sensitivity and scalability. This would provide a better understanding of the method's limitations and potential for practical use.
-: (not totally a weakness, but a suggestion) The whole analysis seems independent of how we represent the scene. So, why not enhance the paper with experiments on 3DGS?

### Questions
Please refer to the weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The work addresses NeRF reconstruction using sparse inputs. The authors assume that the primary cause of reconstruction artifacts is the incorrect setting of boundary conditions in the learning space. To tackle this issue, they propose a new regularization method based on two assumptions: (1) the position of density and color cannot be inferred in regions where the view frustum does not intersect, and (2) information inside opaque surfaces cannot be observed or inferred, and therefore cannot contribute to the rendering of the image. The proposed method can be seamlessly integrated with existing techniques.

### Strengths
1. The proposed regularization methods, along with the propositions to develop them, are logical and well-founded.
2. The proposed method automatically adjusts the training space without requiring additional parameter tuning, making it easy to combine with other approaches.

### Weaknesses
1. Regarding Shadow Zone Regularization, the authors claim that Equation 7 blends the opaque surface's color into the object's interior. However, there is no explicit determination of the opaque surface. How does this effect apply only to the interior of the object as claimed, without affecting other regions? Specifically, the lack of a clear opacity threshold or mechanism raises concerns about how the method avoids blending colors in regions outside the intended object interior. The method's reliance on implicit opacity from the NeRF model makes it unclear how the regularization is constrained to only the interior, especially with sparse views.
2. No video results are presented to demonstrate the reconstruction accuracy and view-consistency of the rendering. Additionally, the comparison baseline only involves nerfacto and FreeNeRF, which is insufficient. The lack of comparisons with other state-of-the-art methods, particularly those that also address sparse view reconstruction, makes it difficult to assess the true contribution of this work. Furthermore, the absence of video results makes it hard to evaluate temporal consistency and rendering quality.
3. Manually adjusting the bounding box is straightforward with popular NeRF frameworks and may achieve the same or even better results than the proposed Frustum Score Regularization. The claim that the proposed method automatically adjusts the training space is not entirely convincing, as bounding box adjustments are a common practice. The benefit of the proposed method over manual bounding box adjustments is not clearly demonstrated, especially considering the potential for fine-tuning bounding boxes to achieve similar or superior results.
4. Quotation marks are not used correctly. (Minor issue, not considered in my rating).

### Questions
1. Could the authors provide additional frustum score visualizations, especially those associated with the presented qualitative results? This would aid in understanding the proposed regularization.
2. Could the authors include loss curves for the proposed regularizers?
3. Could the authors also provide visualizations of RGB values of samples along the ray to illustrate the behavior of Shadow Zone Regularization?
4. Could the proposed approach be combined with 3D Gaussian Splatting? This is significant, as 3DGS is becoming the mainstream approach for novel view synthesis, surpassing NeRF.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper explores two key factors that lead to artifacts when training NeRF from sparse viewpoints. The first is that the regions cannot be inferred where the view frustum does not cover, and the second is that the opaque areas inside objects cannot be well constrained by the RGB loss, resulting in a NeRF that does not fully represent scene information. To address these issues, the paper proposes two regularization terms to constrain the training, focusing the network on areas with higher reliability for better results. Experiments demonstrate that the proposed method effectively resolves the two issues mentioned above.

### Strengths
The paper proposes two different strategies to address the underfitting issues caused by sparse viewpoints, which are actually quite common. These strategies involve designing regularization terms to constrain the training of NeRF, and have been proven to be very effective in experiments. On the other hand, the proposed approach is very intuitive and relatively concise, and it can achieve better results without altering other network settings. Additionally, from what I've observed, the current design is essentially a plug-and-play module that can be used in any existing NeRF. If possible, the author could also emphasize this point and validate it with some experiments.

### Weaknesses
For writing, firstly, regarding the paper's title, since the core problem addressed is how to regularize NeRF training under a "sparse perspective" to achieve better results, it's recommended that the title reflects the concept of "sparsity". Next, concerning the literature review section of the paper, I believe there should be relevant studies from the latest year (2024), and the author needs to thoroughly research the most recent advancements in this field. Additionally, there are issues with some of the formulas where the symbols are not clearly described, and there is inconsistency in their use. For example, the symbol (\sigma) in equation (3) should be consistent with equation (1). Also, it's unclear how (S_norm) in equation (6) is calculated—is it (S / num_views)?

For technical part, some design choices have not provided reasonable explanations for certain aspects.

In equation (3), the Frustum Score is a constant value for each sample point when the camera parameters are fixed. Therefore, the obtained \sigma_masked could be directly used in the integration calculation for RGB. Why then is there a need to further constrain its sparsity? Similarly, in equation (6), clipping is performed in the calculation of gradients. If, as previously mentioned, \sigma_masked is directly used in the integration, constraining both RGB and the gradients, wouldn't a similar effect be achieved with reduced computational effort? I hope the author can explain the design principles. 

Additionally, during the RGB blending process, introducing RGB values near the surface into internal sample points through blending might cause color bleeding in other views. Is it also possible that the color of sample points after weighting could bring noise from unconstrained foreground areas into the interior?

Furthermore, in terms of experimental design, the paper only compares with FreeNeRF, but the settings of FreeNeRF are completely different from this study (network structure, use of hash acceleration, etc.), making the comparison potentially unfair. Lastly, I hope the author could add a few examples of novel view synthesis, because having constrained NeRF, theoretically, the results of NVS should improve. Otherwise, it might be possible that the training data was overfitted through regularization strategies.

### Questions
As discussed above.

### Soundness
3

### Presentation
2

### Contribution
2
