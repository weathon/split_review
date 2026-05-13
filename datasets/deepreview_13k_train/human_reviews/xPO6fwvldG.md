# UniRestore3D: A Scalable Framework For General Shape Restoration

- Decision: Accept
- Scores: 5, 6, 8, 8

## Abstract
Shape restoration aims to recover intact 3D shapes from defective ones, such as those that are incomplete, noisy, and low-resolution. Previous works have achieved impressive results in shape restoration subtasks thanks to advanced generative models. While effective for specific shape defects, they are less applicable in real-world scenarios involving multiple defect types simultaneously. Additionally, training on limited subsets of defective shapes hinders knowledge transfer across restoration types and thus affects generalization. In this paper, we address the task of general shape restoration, which restores shapes with various types of defects through a unified model, thereby naturally improving the applicability and scalability. Our approach first standardizes the data representation across different restoration subtasks using high-resolution TSDF grids and constructs a large-scale dataset with diverse types of shape defects. Next, we design an efficient hierarchical shape generation model and a noise-robust defective shape encoder that enables effective impaired shape understanding and intact shape generation. Moreover, we propose a scalable training strategy for efficient model training. The capabilities of our proposed method are demonstrated across multiple shape restoration subtasks and validated on various datasets, including Objaverse, ShapeNet, GSO, and ABO.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a unified model for general shape restoration, aiming to recover 3D shapes with various defects, such as incompleteness and noise. By standardizing data representation and constructing a large-scale dataset of diverse shape defects, the authors develop an efficient hierarchical generation model and a noise-robust encoder, demonstrating improved applicability and scalability across multiple restoration subtasks on various datasets.

### Strengths
The problem is useful, for preprocessing noisy 3D scans. 
The results seem good.

### Weaknesses
There are no visual comparisons for other methods, making it hard to compare the improvements. 
All data is from the proposed dataset, how about results on real noisy 3D scans?
How about the results on other datasets? Does the network overfits on training set?
There is no overview figure of the whole method, from Figure 3-4, it is still hard to follow the method design. 
For different noises, like low-resolution, noisy completion, noisy refinement etc., do they share the same pipeline/network?

### Questions
See above.

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
4

### Summary
A unified shape restoration model is proposed for handling multiples types of defects (e.g., incompleteness, noise, sparsity) present in scans of 3D objects. The unified shape restoration model is composed of a patch-wise encoder for locally encoding defective shapes, improving generalization capabilities, and a hierarchical latent diffusion model used for generating intact shapes. To enable robustness to various defect types and improve generalization to novel objects, the proposed model is trained on a newly constructed large scale dataset which contains a variety of shape restoration subtasks. Furthermore, a two-staged training scheme is proposed for accelerating training on high-resolution shapes.

### Strengths
- The proposed dataset is an improvement over many of the existing datasets used for evaluating shape completion. Many previous datasets are constructed from the few largest categories from the ShapeNet or PartNet dataset and typically only contain a single type of defect (i.e., incompleteness).  On the other hand, the proposed dataset is much larger scale and contains greater diversity as it is constructed from a diverse set of shape datasets, while also modeling more realistic shape defects present in object scans (e.g., noise + incompleteness).

- The qualitative results seem to suggest the proposed approached does a better job than previous approaches at respecting the fine geometric details present in the partial scans while producing higher quality completions of the missing regions.

### Weaknesses
 - While a high level description of the H-VAE encoder, H-VAE decoder, and H-LDM are provided, there is no description of the actual architectures for these modules. I would expect to see a more detailed description of what the architectures are at the very least in the appendix.

- A scalable training strategy is posed as a contribution; however, there does not exist any evidence that the proposed strategy is more efficient. A table containing training times between the two strategies would demonstrate the benefits more clearly. If the model truly can’t be trained using the normal/standard strategy, the authors could always train on a subset of the data and report training times for that subset or extrapolate what the training time would be for the entire dataset.

- The model does not seem to generalize all that well or be robust to unknown categories. In Table 1, the model obtains a 2-5x worse MMD/AMD on ABO across the different tasks and about a 100x worse MMD/AMD on GSO. This large drop in performance is observed even for the noisy refinement task which should be an easier task than noisy completion.

- The quantitative results don’t really demonstrate that the proposed model is better. In Table 2, the proposed approach is the only model pre-trained on the large scale dataset, which isn’t really a fair comparison for evaluating model performance. Even when pre-trained on their dataset the model performs similarly or worse to NeuSDFusion, and to actually outperform NeuSDFusion they had to artificially add more task specific examples (noise-free completions) to the pre-training data. It’s not clear whether all baseline methods would improve and outperform the proposed method from a similar pre-training. Instead the authors should add a comparison of their approach with no pre-training to Table 2 to fairly evaluate model performance.

- Similarly in Table 3, a comparison needs to be added with no pre-training. The model slightly outperforms SC-Diff, but this improvement could just be from pre-training on a large scale dataset.



### Questions
Questions:
- Given that the patch-wise encoders produce sparse feature grids, how is the feature alignment being computed? A shape that has missing geometry will not have the same sparse voxel grid as the intact shape, so is the feature alignment loss only being computed for voxel indices which exist in both sparse feature grids?

- Since all the encoders, decoders, and LDM use sparse convolutions, how is the model able to generate missing structures from the sparse feature grid? Is some form of structure prediction module, similar to Ren et al. (2024) and Huang et al. (2023), being used in the decoder?


Corrections to make:
- In Table 6 of appendix, the best CD for the Lamp category and the best IoUs for the Bed and Bench category are incorrectly bolded.
- In Table 7 of appendix, the best IoUs for the Bathtub, Basket, and Printer categories are incorrectly bolded. 

References:
- Jiahui Huang, Zan Gojcic, Matan Atzmon, Or Litany, Sanja Fidler, and Francis Williams. Neural kernel surface reconstruction. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 4369–4379, 2023. 
- Xuanchi Ren, Jiahui Huang, Xiaohui Zeng, Ken Museth, Sanja Fidler, and Francis Williams. Xcube: Large-scale 3d generative modeling using sparse voxel hierarchies. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 4209–4219, 2024.

### Soundness
3

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
3

### Summary
The paper presents a dataset/benchmark that unifies shape completion, denoising and superresolution on TSDFs and a hierarchical latent diffusion based method to solve all those tasks jointly.
The dataset is assembled from a variety of dataset, including Objaverse using a unique pipeline to get from non-manifold-meshes to ground-truth and different versions of incomplete or corrupted TSDF grids.
Their unified restoration method uses two main modules: A hierarchical (multi level) Variational Autoencoder and a hierarchical (multi level) latent diffusion model. All models (except for the coarsest level) are implemented using sparse convolutions, which only act on SDF-values close to the surface. The VAE is trained separately from the diffusion model in two stages. First on the clean shapes. In a second step the VAE is refined on the corrupted shapes, where the latents are guided to be close to the ground-truth latents of the clean objects.
The latent diffusion model runs from coarse to fine. It is conditioned on the latents of the corrupted shape and the occupancy grid predicted in the next coarser level. The diffusion model is trained to denoise the latents into the clean grond truth latents. The occupancy grid for the next level is extracted by decoding the latents into a TSDF using the VAE-decoder and extracting the geometry. On the finest level the decoded TSDF is the final result of the method.
The method is validated on a test-split of the own dataset and also on the 3DQD and PatchComplete benchmarks and demonstrate sota performance.

### Strengths
* Sane method with reasonable justification for each step.
* The paper presents a new benchmark for shape completion using TSDFs, which could potentially be very useful in the field, as currently used benchmarks are either not tailored to TSDFS or extremely low resolution. 
* The detailed account for all the work necessary to compare to the existing 'benchmarks' beautifully highlight the hideous sate of the benchmarks in this field. Every single paper that is published uses their own internal representation and rely on a very specific data preprocessing. They all have to compare to absolutely terrible benchmarks like Patch Complete or 3DQD - burning so much time and brain of talented people just to figure out how to correctly recreate the benchmark to work with their internal data and somehow stay comparable to the 32^3 numbers. It is an absolute shame. I think the paper did this well, still I wonder what brilliant work the authors could have done with the time they had to waste on this.
* Diffusion based method can produce multiple suggestions which the user can chose from.

### Weaknesses
 * The shape representation (TSDF) is mentioned for the first time on page 4. Your readers might have very different backgrounds and very different understanding of 3D-Shapes. Some might think you work on 3D-Pointclouds, others think you work with meshes, yet others might think you for sure use binary occupancy grids or unsigned distance fields neural representations or whatever. In the related works you put yourself next to all kind of methods without pointing out this major difference. In my humble opinion the choice of shape representation is a central feature, which defines it's usefulness for different problems. It should be communicated very clearly - if not in the Title at least in the Abstract or at least in the Introduction. Also your resolution of 256 is really nice and also could be mentioned earlier. 
* No information about training time of the modules is given. No information of inference time and memory requirement for inference are given.
* Diffusion based method is not usable for online real-time applications (during 3D-scanning).
* Paper claims that the denoiser can be conditioned on "text or images", which was never demonstrated. Claim must be removed or proven in the given context. If it is not used it should be removed from the method (especially equation 1). If it is used its effect must be evaluated. This is my biggest concern currently.

### Questions
* Line 429: typo: tsdf -> TSDF
* Please provide training hardware, memory and time requirements. Same for inference.
* Paper claims that the denoiser can be conditioned on "text or images", which was never demonstrated. Claim must be removed or proven in the given context. If it is not used it should be removed from the method (especially equation 1). If it is used its effect must be evaluated. This is my biggest concern currently.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposed a new framework for general shape restoration, which aims to handle multiple types of defection in a single framework. The proposed framework supports four types of shape defection, namely noise / noise-free completion, noise refinement (i.e., denoising), and super-resolution. The proposed new framework including a new large-scale dataset with various types of defections, a multi-scale defection-robust shape encoder, and a conditional latent diffusion model for shape generation. Experiments on multiple shape restoration tasks demonstrated the effectiveness of the proposed framework.

### Strengths
- The attempt of unified framework for 3D shape restoration under different defections is interesting.

- The proposed large-scale shape restoration dataset is very useful to the community.

- Outstanding results on multiple shape restoration tasks which outperforms state-of-the-art.

- Good writing and enough details in the appendix for reproducible research.

### Weaknesses
 - While I really appreciate the efforts for building such a large and general framework (and the result is really promising), I found it hard to understand the key challenge and insights for building such a framework. Specifically, 

(1) What is the key challenge for building the large scale dataset for shape restoration? The process mainly consists of randomly adding different type of pre-defined perturbation on existing large-scale 3D object datasets. It is surprising (or maybe I missed some work?) that no one ever did this before.

(2) As mentioned in the introduction section, "These diverse tasks require different model capabilities, making it challenging to design a 
unified model for general shape restoration" - how does the proposed framework addressed this capabilities requirement? It reads something like "we just merged all the data with different task together for training, and it worked."  For example, one direct approach of training a unified framework would be just simply merging all existing dataset for different tasks and then perform joint training. I wonder what the result would be, as it would give us more insight regarding why the proposed framework has good performance - is it simply because of the amount of dataset in the proposed framework is larger, or because of the carefully designed method of defection synthesizing pipeline, or other factors? 

- There are some unclear part regarding the dataset and the experiment setup. Please see the "Questions" section below.

### Questions
(1) For dataset creation, does every intact shape in the database only employs one of the four subtasks, or some shape will be simultaneously corrupted by multiple subtasks together? Also, for the ablation study in table 4, does the "joint training" has the double amount of data compared to "noisy refinement only" and "noisy completion only"? In other words, does the improvement of the proposed method comes from scale-up of data amount or from joint subtasks learning? 

(2) I found it hard to understand the importance of the "scalable training strategy" proposed in section 4.1. Why it is "scalable"? It is mentioned in the paper that "it significantly slows down training due to the need to load high-resolution defective shapes". Isn't it true that loading intact shape should also slows down training in the first stage? Also, the proposed method still requires loading defective shapes in the second stage - so what is improved here?

(3) Will the proposed dataset open-sourced in the future?

### Soundness
3

### Presentation
3

### Contribution
3
