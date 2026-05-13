# Locality Sensitive Avatars From Video

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
We present locality-sensitive avatar, a neural radiance field (NeRF) based network to learn human motions from monocular videos. To this end, we estimate a canonical representation between different frames of a video with a non-linear mapping from observation to canonical space, which we decompose into a skeletal rigid motion and a non-rigid counterpart. Our key contribution is to retain fine-grained details by modeling the non-rigid part with a graph neural network (GNN) that keeps the pose information local to neighboring body parts.
Compared to former canonical representation based methods which solely operate on the coordinate space of a whole shape, our locality-sensitive motion modeling can reproduce both realistic shape contours and vivid fine-grained details. We evaluate on ZJU-MoCap, ActorsHQ, SynWild, and various outdoor videos. The experiments reveal that with the locality sensitive deformation to canonical feature space, we are the first to achieve state-of-the-art results across novel view synthesis, novel pose animation and 3D shape reconstruction simultaneously. For reproducibility, the code will be available upon publication.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This work presents a neural radiance field (NeRF) based network to learn human motions from monocular videos. The key argument is its method that can improve the local details of humans. They evaluated on ZJU-MoCap, ActorsHQ, SynWild, and various outdoor videos.

### Strengths
1. Human modeling from monocular video is an important task.
2. The method is clearly presented.
3. The code will be released.

### Weaknesses
1. Visual Quality. (1) In the demo video,  the gap between this work and SOTAs can not be clearly seen, especially for HumanNeRF. Samples at least on HumanRF/Synwild are also expected in the demo to better evaluate the universality of the work.  In the paper, the visual compassion is done on cases with simple textures and topologies. Other publicly available in-door datasets (e.g., AIST++, DNA-Rendering, MVHumanNet) with rich texture, and diverse/complex clothes should be evaluated. Also, the reconstruction difference with Vid2Avatar is hard to differentiate, which is also demonstrated in Table G, page 19.  (2)Whats the setting of the demo video is also not clear. Are they nvs, np, or just seen view reconstruction? The setting should be clarified.

2. Comparison to SOTAs. (1) Many state-of-the-art methods are missing in the comparison or discussion, such as MonoHuman in Tab.3 and the demo video, gaussian splatting based methods GaussianAvatar, 3DGS-Avatar (CVPR2024). (2) For the animation ability, it would be better to show driven poses that are out-of-distribution, like the MDM setting in MonoHuman. 

3. Motivation of the method. The pipeline looks like a combination of different modules.  As the key of this work, details are improved by GNN. However, the motivation is not clear. What are the challenges of other feature extraction paradigms to model in detail? Why does GNN work? Why are other methods not working? If you add GNN to their implementation, will they also work?

### Questions
See Weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Locality-Sensitive Avatar, a novel neural radiance field (NeRF) based network for learning human motions from monocular videos. The key innovation lies in using a graph neural network (GNN) to model non-rigid deformations while preserving fine-grained, locality-sensitive details.

### Strengths
The model demonstrates superior rendering performance compared to other approaches, particularly evident through enhanced normal rendering results. It is also capable of learning from a small amount of data and remains effective even for novel poses, showcasing its robustness and versatility.

### Weaknesses
The model struggles with accurate reconstruction of detailed areas such as the face or hands. Additionally, the visualization of non-rigid motion is insufficient, making it unclear what this component represents, and it is difficult to clearly understand the difference between considering and not considering non-rigid motion.

The core idea is to utilize non-rigid motion, which could effectively express the fluttering of loose-fit clothes. The current examples capture only person-specific details.

### Questions
1. What are the differences between the proposed model and GauHuman or HUGS?
@inproceedings{hu2024gauhuman,
  title={Gauhuman: Articulated gaussian splatting from monocular human videos},
  author={Hu, Shoukang and Hu, Tao and Liu, Ziwei},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={20418--20431},
  year={2024}
}

@inproceedings{kocabas2024hugs,
  title={Hugs: Human gaussian splats},
  author={Kocabas, Muhammed and Chang, Jen-Hao Rick and Gabriel, James and Tuzel, Oncel and Ranjan, Anurag},
  booktitle={Proceedings of the IEEE/CVF conference on computer vision and pattern recognition},
  pages={505--515},
  year={2024}
}

2. Does using SMPL pose parameters as LBS weights result in any artifacts?

3. What is the rendering speed of the proposed model?

4. Can you show the qualitative and quantitative results if the non-rigid Δx component is omitted?

5. Does considering non-rigid deformations help in accurately representing effects like the flapping of clothes?

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
3

### Summary
This paper studies the problem of learning 3D neural avatars from 2D videos. It is based on several prior works that decompose the dynamic neural human avatar into canonical space, rigid deformation, and non-rigid deformation. The major contribution lies in the modeling of the non-rigid deformation part. Specifically, it trains a pose-conditioned non-rigid deformation prediction network with a GNN architecture. Some experiments show improvement of the proposed method.

### Strengths
- The studied problem in this paper is important. Reconstructing neural human avatars from videos has been a long-standing problem in the community, with several different applications in the movie industry, AR/VR, and gaming industry.
- The proposed method basically follows the framework set by the prior works, which is sound. Modeling the non-rigid deformation with a pose-conditioned network is also a sound and widely used method in the community.

### Weaknesses
 - The major concern is the generalizability of the pose-conditioned GNN. The multi-view human data is sparse in the community, therefore the GNN might overfit on those training and struggle to generalize to the in-the-wild dataset. Specifically, the limited diversity of poses within typical multi-view datasets could lead to the GNN learning a mapping that is highly specific to the training distribution, rather than a generalizable representation of pose-dependent non-rigid deformations. This could manifest as artifacts or unrealistic deformations when the model encounters poses significantly different from those seen during training.
- Most results presented are with tight clothes, which might not fully demonstrate the effectiveness of the proposed method. It would be interesting to see more large-scale results on more challenging clothes, such as THUman2.1 dataset. The lack of results on loose or flowing clothing makes it difficult to assess the robustness of the method to complex deformation patterns. The method's ability to handle self-occlusions and intricate folds in clothing remains unclear.
- The major contribution of this paper can be seen as incremental. The only major change of this paper's pipeline compared to prior works is to use GNN to model non-rigid deformation, which is a sound but not-so-exciting technical contribution. The use of a GNN for pose-conditioned deformation is not novel in itself, and the paper does not provide a compelling argument for why this particular GNN architecture is superior to other existing methods for modeling non-rigid deformations.
- Some baselines are not compared, e.g. [Li et al. 2023], so it's hard to say whether the proposed method is truly the state-of-the-art. The absence of a comparison with PoseVocab [Li et al. 2023], which also focuses on learning pose-conditioned embeddings for human avatars, makes it difficult to position the proposed method within the current landscape of research. This lack of comparison leaves open the question of whether the proposed approach offers a significant advantage over existing techniques.
- Some experiment settings are not clear. See questions for details.

### Questions
- For the experiments on the ActorsHQ dataset, is it rendered under a novel pose or training pose?
- For the videos rendered in the supplementary material, is it under novel pose or training pose?

### Soundness
3

### Presentation
2

### Contribution
2
