# DSPart: A Large-scale Diffusion-generated Synthetic Dataset with Annotations from 3D Parts

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
Object parts provide representations that enable a detailed and interpretable understanding of object structures, making part recognition crucial for various real-world applications. However, acquiring pixel-level part annotations is both expensive and time-consuming. Rendering 3D object models with their 3D part annotations is a promising solution since it allows the generation of unlimited synthetic data samples with precise 3D control and accurate part segmentation masks. Nevertheless, these synthetic datasets suffer from a lack of realism, resulting in large domain gaps. In this paper, we present a large-scale realistic synthetic dataset with part annotations, namely Diffusion-generated Synthetic Parts (DSPart), for both rigid objects and animals. For images in DSPart, we obtain 2D part masks from 3D part annotations by leveraging recent advances in diffusion models with 3D control. In addition to offering more diverse and realistic textures, prior knowledge of diffusion models enables the object to exhibit more physically realistic interactions with the ground plane and other spatial contexts. We annotate $475$ representative shape instances from $50$ object categories for DSPart-Rigid and use $3,065$ high-quality SMAL models fitted poses from $40$ animal categories for DSPart-Animal. Experimental results demonstrate the potential of our dataset in training robust part segmentation models, effectively bridging the gap between synthetic and real-world data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a framework (DSPart), including a filtering approach (PRF), for generating a large-scale synthetic dataset for 2D object part segmentation (DSPart-Rigid and DSPart-Animal). The results demonstrate that training on the generated dataset achieves superior performance compared to existing synthetic datasets (UDAPart and CC-SSL), in both supervised (SegFormer) and unsupervised (DAFormer) setups.

### Strengths
1.	The paper is well-written and easy to follow.

2.	The paper presents an effective and easily applicable method (DSPart) for utilizing an existing generation approach (3D-DST) and existing 3D CAD models (e.g., ShapeNet and Objaverse), along with additional annotations (e.g., 3D parts), to generate pixel-level part-based datasets.

3.	The scale and diversity of the generated dataset (DSPart-Rigid and DSPart-Animal) are impressive, comprising 100k images, 90 object categories, and over 3.5k 3D models.

4.	Training on the generated dataset, whether or not UDA is applied, typically demonstrates superior results on real part-based datasets (e.g., PartImageNet) compared to training on existing synthetic datasets.

### Weaknesses
Major:

1.	Despite its simplicity, the proposed framework (DSPart) shows limited novelty from a technical perspective. It appears more like a direct application of an existing framework (3D-DST), enhanced by incorporating additional annotations (e.g., 3D parts) and a wider variety of 3D models (e.g., animals). Although the paper claims that the extension is non-trivial (Line 107), it would be beneficial if the paper could justify this claim by highlighting its technical innovations. Specifically, the paper does not clearly articulate how the integration of 3D part annotations into the 3D-DST pipeline introduces any novel algorithmic or mathematical challenges, or how the use of animal models necessitates any significant modifications to the existing framework beyond simply using different 3D assets.

2.	The paper demonstrates that the proposed filtering mechanism (PRF) outperforms the existing one (KCF). However, this comparison seems unfair and potentially lacks meaningful insight for several reasons. First, PRF trains models for filtering using reliable human-filtered data (e.g., 13k images) that KCF does not have access to, making it unsurprising that PRF performs better. Additionally, the paper does not quantify the contribution of each component within PRF, such as the use of two PARE models, three different metrics, and various thresholds. It is possible that PRF’s superior performance is simply due to its access to more reliable data. Furthermore, the paper does not analyze the sensitivity of PRF to the amount of human-filtered training data, nor does it explore the impact of different choices of 3D pose estimation models. Finally, the paper does not provide visual examples to illustrate why PRF outperforms KCF. Including examples of data filtered by PRF but not by KCF, or showcasing PRF's failure cases, would add clarity and strengthen the explanation.

3.	Although the paper shows that using the DSPart dataset for training generally yields better performance than other existing synthetic datasets, it does not fully explain why the DSPart dataset is superior, which is essential for the community to understand the results. For example, as shown in Table 2, training models on DSPart-Rigid consistently outperforms training models on UDAPart. Is this advantage due to the realism of the generated images, the diversity of the 3D CAD models, the increased number of viewpoints, or the total number of generated images? The paper does not provide a systematic ablation study to disentangle these factors. For instance, it would be beneficial to investigate the impact of varying the number of 3D CAD models, the number of viewpoints per model, and the diversity of textures, while keeping other factors constant. Investigating different versions of DSPart-Rigid could be insightful, such as generating DSPart-Rigid with the same set of 3D CAD models used by UDAPart, varying the number of viewpoints, generating different numbers of images, or controlling texture diversity through varied prompts.

Minor:

4.	In Table 5, the paper shows that PRF is more efficient (20 minutes for inference) compared to KCF (50 training hours). However, since PRF requires human-filtered data for training 3D pose estimation models, it would be fairer to include this as part of PRF’s overall cost (e.g., 100 hours human labor). While the paper mentions that PRF only needs a pre-trained model and can be applied to the generated images at scale, this is true only if the human-filtered data used by PRF effectively captures the entire animal pose space, which may not be the case. The paper does not address the potential for bias introduced by the limited pose space covered by the human-filtered data, nor does it discuss the impact of this bias on the generalizability of the filtered dataset.

5.	The paper defines five super-categories (car, airplane, bicycle, boat, and tool) for rigid objects in the proposed dataset (DSPart-Rigid). However, the tool category is never used in the paper.

6.	The paper utilizes only a single architecture for both the fully supervised setup (SegFormer) and the UDA setup (DAFormer). Including additional architectures or UDA methods would strengthen some of the paper’s claims, such as the claim that DSPart-Rigid enables better knowledge transfer from the synthetic to the real domain for UDA (Lines 355-357). The paper should explore the performance of DSPart on a wider range of architectures to demonstrate the robustness of the dataset across different model types.

### Questions
1.	Please clarify the technical novelty of the proposed framework in response to Weaknesses-1. Highlighting the key advancements distinguishing 3D-DST from the proposed framework would be beneficial.

2.	Please provide additional details about PRF in response to Weaknesses-2 and Weaknesses-4. This may include explaining why PRF outperforming KCF is still meaningful, even if PRF has access to more reliable data, quantifying the contribution of each component within PRF, and providing visual examples.

3.	Please fully justify why the DSPart dataset is superior. As suggested in Weaknesses-3, exploring different versions of DSPart-Rigid could be insightful.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a new part-segmentation synthetic dataset via 2D diffusion models, the results show that it is possible to use diffusion models to generate more diverse data samples for part segmentation task.

### Strengths
1. Show the potentional on using synthetic data for part segmentation.

### Weaknesses
1. Lack of details on how to use diffusion models to generate data samples, which base model is used. Why not use a ControlNet to generate controllable data pairs.

2. The scale of the generated data is relatively small, which makes it hard to verify the generalization capability of the model when trained on  larger data scales.

### Questions
1. Given the categories included in DSPart-Rigid and DSPart-Animal, to what extent is this dataset likely to be generalizable to other object categories or part segmentation tasks?

### Soundness
2

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
4

### Summary
The paper introduces a synthetic dataset called DSPart, designed to improve part-based recognition models. DSPart includes synthetic images with part-level annotations derived from 3D models, specifically addressing two key groups: rigid objects (DSPart-Rigid) and animals (DSPart-Animal). With annotating 3.5K 3D models, it generates 100K realistic synthetic images with masks. Extensive experiments demonstrate that DSPart surpasses existing synthetic datasets in part segmentation tasks.

### Strengths
1. The paper introduces an innovative approach that utilizes 3D part annotations to generate realistic synthetic images with corresponding part masks. This method enables the generation of an unlimited number of synthetic data samples using a limited set of annotated 3D shapes, significantly reducing the cost and time required for annotating large quantities of 2D images.
2. Sufficient experiments on the 2D part segmentation task to demonstrate the effectiveness of the DSPart dataset.
3. DSPart addresses limitations in previous synthetic datasets by using diffusion models to generate realistic textures and physically consistent contexts, making the synthetic images more reflective of real-world conditions.

### Weaknesses
1. The method is challenging to generalize due to the difficulty in defining annotations for parts in other categories. For instance, providing semantic-level part definitions for data in the large-scale 3D dataset Objaverse[1] is particularly challenging. Is it able to consider a part definition approach similar to SAM?
2. Generating images with 2D part annotations using standard 3D parts can increase data volume; however, annotating 3D data is more challenging and requires annotators to possess advanced tool usage skills. This, in turn, limits the scalability of the data to some extent.
3. Each generated image contains a single, clear object positioned in the center. However, in real images, there may be multiple objects that are not necessarily centered or clearly defined. This indicates that some domain gaps still exist.

### Questions
1. Is it able to adjust poses of 3D shapes to increase the diversity of 3D data?

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
This paper proposes two datasets of 3D object parts, DSPart-Rigid and DSPart-Animal. For DSPart-Rigid, it annotates 475 representative shape instances from 50 object categories. For DSPart-Animal, it creates one single 3D part annotation since all SMAL models share the same vertex IDs, and uses 3,065 SMAL models fitted poses from 40 animal categories. It uses a diffusion model, 3D-DST (Ma et al., 2024), to render the realistic images. To further filter out low-quality images for animals, this paper proposes a filter, Part-attention Regressor Filter, which estimates the accuracy of articulations. In total, this data sets contains 48K synthetic images of rigid objects and 52K synthetic images of animals. To evaluate the quality of the dataset, this paper trains the models on its datasets in both synthetic-only and synthetic-to-real scenarios to evaluate their performance on PartImageNet (He et al., 2022) and PascalPart (Chen et al., 2014).

### Strengths
1. The proposed filter for animals, Part-attention Regressor Filter, significantly improves the quality of the generated data, as shown in Table 5.

### Weaknesses
1. If we compare the results of the model trained only on real-world data and the model trained only on synthetic data, the difference is huge, especially for animals (Table 3 & 4). This might mean that the proposed dataset and dataset creation methods are still far behind the real-world hand data, and might not be scalable as described. The large performance gap suggests that the synthetic data, despite the filtering, does not capture the complexity and nuances of real-world data, particularly in the context of animal part segmentation. This raises concerns about the practical utility of the dataset for tasks requiring high accuracy.
2. Although the proposed filter, PRF, takes a significant portion of the paper, it seems not used in producing the final datasets (see numbers in Table 3 "DSPart-Animal" and Table 5 "Human"). Therefore, it is questionable whether the method is scalable as claimed. I wish it could be further clarified. The paper highlights the PRF's effectiveness in filtering, but the final dataset appears to be generated using a different, potentially less rigorous, approach. This discrepancy undermines the claim of scalability, as the most effective filtering method is not consistently applied, and the paper lacks a clear explanation of why the PRF was not used for the final dataset generation.

### Questions
1. In Table 5, it shows that the PRF-filtered result under the UDA setting is close to the human-filtered result, except background. Is there any insights why background is special?
2. It is interesting that, in Table 4 (Syn-only), the IoU of back legs and the tails are significantly worse than the previous synthesized dataset, CC-SSL. Is there any insights on that?

### Soundness
2

### Presentation
3

### Contribution
2
