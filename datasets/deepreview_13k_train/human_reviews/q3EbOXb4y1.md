# Retri3D: 3D Neural Graphics Representation Retrieval

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
Learnable 3D Neural Graphics Representations (3DNGR) have emerged as promising 3D representations for reconstructing 3D scenes from 2D images. Numerous works, including Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and their variants, have significantly enhanced the quality of these representations. The ease of construction from 2D images, suitability for online viewing/sharing, and applications in game/art design downstream tasks make it a vital 3D representation, with potential creation of large numbers of such 3D models. This necessitates large data stores, local or online, to save 3D visual data in these formats. However, no existing framework enables accurate retrieval of stored 3DNGRs. In this work, we propose, Retri3D, a framework that enables accurate and efficient retrieval of 3D scenes represented as NGRs from large data stores using text queries. We introduce a novel Neural Field Artifact Analysis technique, combined with a Smart Camera Movement Module, to select clean views and navigate pre-trained 3DNGRs. These techniques enable accurate retrieval by selecting the best viewing directions in the 3D scene for high-quality visual feature embeddings. We demonstrate that Retri3D is compatible with any NGR representation. On the LERF and ScanNet++ datasets, we show significant improvement in retrieval accuracy compared to existing techniques, while being orders of magnitude faster and storage efficient.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces Retri3D, a novel framework for text-to-3D scene retrieval from repositories of neural graphics representations (NGRs). Retri3D leverages pretrained Vision-Language Models (VLMs), like CLIP, to generate embeddings of both text and rendered images, enabling efficient retrieval across a wide range of 3D scene representations, such as NeRF and 3D Gaussian Splats (3DGS). The core contributions include a Neural Graphics Noise Analysis (NGNA) and a Smart Camera Movement Module (SCMM), which collectively enhance the quality of view selection by detecting and avoiding artifacts, thus improving retrieval accuracy. The system demonstrates compatibility with multiple datasets (LERF, ScanNet++) and achieves superior retrieval speed and storage efficiency.

### Strengths
1. Retri3D introduces a novel approach to 3D retrieval by using a two-pronged methodology: noise analysis via Neural Graphics Noise Analysis and selective viewpoint rendering through the Smart Camera Movement Module. These elements enable the retrieval of high-quality embeddings from rendered images given the typical noise in the NGRs.

2. By leveraging pretrained VLMs, Retri3D achieves efficient and accurate retrieval without the need for extensive retraining or dataset-specific tuning, which is an improvement over previous methods. The noise analysis method proposed is demonstrated to outperform traditional NeRF uncertainty estimation techniques, emphasizing the robustness of the framework in achieving high-quality feature extraction under diverse conditions​.

3. The paper is overall well-written and well-organized. The proposed pipeline is clean yet effective, with potential for a significant number of downstream applications.

### Weaknesses
1. Comparative Analysis Limitations: While Retri3D shows strong results on LERF and ScanNet++ datasets, the paper lacks comparative results with more recent methods such as TIGER[1] or N2F2[2]. Including these would provide a broader context for Retri3D’s advancements and its relative strengths and weaknesses across a more diverse set of models and techniques​. The author should also include ConDense[3] in the related works and have a dedicated discussion/comparison, since it could also be applied to this specific task.

2. Dependency on VLM Embeddings: Retri3D relies heavily on VLMs for generating text and visual embeddings, which inherently limits its performance to the capabilities of the underlying VLM model. This dependency means that Retri3D’s retrieval quality might suffer in cases where the VLM struggles with certain text-visual correlations, particularly in scenes with complex or subtle object relations.

3. Potential Generalizability Issues with Scene Complexity: Although Retri3D demonstrates high performance on scenes with distinct and identifiable objects, its retrieval accuracy in complex scenes (compositional) with overlapping or occluded objects is less explored. A detailed discussion of how Retri3D would handle such scenarios or results comparing its retrieval accuracy in simple versus complex scenes would clarify its effectiveness across varying levels of scene complexity​.

### Questions
1. Adding recent works as mentioned in W1 in the relevant section (related works, experiments, and/or discussions), especially [2] and [3].
2. Adding a dedicated discussion/analysis on the model robustness as mentioned in W2 and W3.
3. The paper presents a robust noise analysis technique, yet an interesting avenue might be replacing NGNA with NeRF uncertainty estimation methods. How would this alternative affect the accuracy, speed, and storage efficiency of Retri3D?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors propose a novel framework for text-based retrieval of NGR representations (NeRFs, Splats and derivatives).
They approach the problem by utilizing an off-the-shelf VLMs to extract feature embeddings from clean scene renders and match them with query text embeddings. Clean scene renders are obtained by iteratively applying Noise Analysis (using the same VLMs) to identify the direction towards clean scene and using smart camera movements module to converge to a cleaner render.

### Strengths
* To my knowledge, the concept of iteratively refining camera positions to achieve cleaner renders appears to be novel.
* The use of SMCC is well-supported by the evidence:
  * The retrieval quality is demonstrated to be significantly higher than previous baselines or random views.
  * Section 4.5 effectively highlights that the smart camera approach offers high coverage of the scene and the training portion of the scene
  * Strong speed / memory benchmarks
* It is well-proven that proposed solution is compatible with various VLMs
* Overall, the paper is concise, and the conclusions are mainly well-supported.

### Weaknesses
1. Two major assumptions of the paper are not well-addressed (please refer to the Questions section), namely:
* *noise features remain consistent across different scenes and models*
* *Some content can be noise-free, but they constitute only small portions of the images.*



### Questions
1. (line 303) Major claim of the paper:
 > noise features remain consistent across different scenes and **models**

  While it is clear and safe to assume noise features are of the same distribution within the same model family, it's not clear why the same holds for various models, e.g. are NeRFs and Splats features distributed the same? Maybe a mixture of gaussians suit better here? Please discuss.

2. (Claim on line 288) Major claim of the paper:
 > [*...about sampling random view-points in pre-trained NGR scenes...*] Some content can be noise-free, but they constitute only small portions of the images.

  I would expect a robust retrieval pipeline to work on both noisy and clean scenes. For example, how would it handle "ground-truth" scenes? With recent advancements in Splats, I would assume that the percentage of clean renders from random camera viewpoints could be significantly higher. As you train on increasingly clean datasets, SMCC’s performance may degrade. Please discuss how this issue could be mitigated.

3. Could you clarify how cameras are initialized in the SMCC module? If they are initialized randomly, does SMCC consistently converge, or is there a risk of getting stuck in local minima?

### Soundness
4

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
This paper aims to solve a 3D radiance field retrieval problem using text inputs and queries from the dataset constructed by multiview embedding a trained 3D radiance field. The key challenge is to obtain high-quality multiview image embeddings for the database. To solve this problem, the author proposes a noise analysis module to qualify the rendering quality of each rendering view and a camera moving module to guarantee viewpoints that render less noise images. With the powerful Visual-Language model, the method extracts rich information from a constructed database and text embedding for the retrieval task. The authors com

### Strengths
1. The overall framework is well-motivated. The authors pay more attention to utilizing the multiview images as the data representation and propose several following designs to conduct the retrieval tasks, which is reasonable.
2. The experiment results are extensive to cover different aspects of the proposed framework as in the main draft and supplementary.

### Weaknesses
1. The effectiveness of the smart camera moving module in Tab.1. As shown in Tab.1, using 20 training views almost outperformed every design. In some real applications, storing the radiance field with 20 training views for the following retrieval tasks would still be possible. It only introduces a tiny storage overhead while benefiting the tasks. This makes the setting only suitable if we don't have the training view. 
2. The authors propose to quantify the noise in Sec. 3.3 with a heuristic-designed viewpoint selection to determine the noise and clean features, which is counterintuitive for me. It would be better to include more details like how such random viewpoints are generated, and why the random viewpoints will contain valid noise for GMM training.
3. The initial value of the smart camera movement module should also influence the quality. How does it initialize and if we initial from the training views, will the module converge to a bad choice in the test set?

### Questions
1. It would be more helpful for the readers to understand why we need a retrieval task by providing detailed applications. 
2.  Why not compare with some retrieval method based on conversion 3D representation as listed in lines 45-46? It would also be possible to convert the radiance field representation like 3DGS to a simplified point cloud for this task.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents Retri3D, a novel framework for retrieving 3D Neural Graphics Representations (3D NGRs) using text queries. The system leverages cosine similarity between embeddings generated by a pretrained Visual Language Model (VLM) from text queries and RGB renderings of 3D scenes. To enhance the quality of visual feature embeddings, Retri3D introduces two key techniques: Neural Field Artifact Analysis, which uses a multivariate Gaussian model to differentiate clean from noisy pixels using activation maps of VLM, and a Smart Camera Movement Module that iteratively samples new camera angles to reduce noise. Experiments show that Retri3D excels in accuracy, training time, embedding size, and retrieval performance on the LERF and ScanNet++ datasets, outperforming existing baselines.

### Strengths
1. This paper addresses a novel problem in retrieving 3D NGRs that previous works have not covered.

2. Retri3D is the first framework capable of efficiently retrieving 3D scenes from large datasets using text queries without requiring training views or camera poses.

3. The proposed Artifact Analysis effectively distinguishes clean and noisy regions in RGB renderings, while the Smart Camera Movement Module identifies cleaner viewpoints.

4. Extensive experiments validate that Retri3D generates accurate embeddings and retrieves 3D scenes efficiently, utilizing moderate storage and training time compared to baseline methods.

In conclusion, the paper's contributions are significant, establishing a novel framework for 3D NGR retrieval. The introduction of two innovative modules enhances embedding quality, and the experiments comprehensively evaluate retrieval accuracy, computational efficiency, and scene coverage, clearly demonstrating advantages over baselines that integrate language features into scene representation.

### Weaknesses
1. The experiments focus on only two types of text queries (object labels and LLaVA-generated queries). Testing more complex queries—such as those describing object shapes, textures, environmental styles, materials, lighting, and specific object arrangements—could further reveal the retrieval limits. The current evaluation does not fully explore the nuances of language understanding in relation to 3D scene content. For instance, queries involving spatial relationships between multiple objects or requiring an understanding of fine-grained material properties are not tested, which could expose limitations in the VLM's ability to connect text descriptions to the 3D scene. 

2. While the authors evaluate two NGRs (Splatfacto and Nerfacto), many other NGRs may present different artifact patterns, potentially impacting the neural graphics noise analysis. Additionally, noisy or blurred regions could be more pronounced with fewer training views, especially in few-shot reconstruction settings or if the model underfits, which may hinder the noise analysis module's effectiveness in new scenes. The reliance on a single noise model derived from two specific NGRs could limit the generalizability of the approach. The effectiveness of the noise analysis module in scenarios with significantly different noise characteristics, such as those arising from different rendering techniques or underfitting, remains unclear.

3. The framework's understanding of 3D scenes relies on 2D renderings, treating embeddings from different viewpoints independently. This approach may fail to answer queries about 3D-specific structures or details. Furthermore, since the current retrieval operates at a uniform resolution, querying localized small areas could result in inaccuracies due to the limitations of 2D rendering resolution. The independent processing of 2D renderings from different viewpoints may lead to a loss of crucial 3D structural information. The system's inability to directly reason about 3D geometry could limit its capacity to handle queries that require an understanding of spatial relationships or occlusions. Additionally, the fixed rendering resolution could hinder the retrieval of small or detailed regions within a scene.

### Questions
1. Do tightly clustered noisy features consistently affect all VLMs, and how might performance vary with different architectures?

2. Are the results only applicable to indoor scenes, or does the framework also extend to complex outdoor environments?

3. How are initial cameras set up for a given NGR, and what happens if the initial pose is poorly sampled?

4. As the Smart Camera Movement Module seeks cleaner viewpoints, how does it ensure comprehensive coverage of the entire 3D scene? Will some important parts, such as a corner in the scene, be neglected in all the sampled viewpoints?

5. What field of view (FOV) is used for rendering RGB images, and could wider FOV (such as a fisheye lens or a panorama image) improve feature capture in 3D scenes?

### Soundness
4

### Presentation
4

### Contribution
4
