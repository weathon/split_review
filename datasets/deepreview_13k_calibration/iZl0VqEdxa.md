# Uncertainty modeling for fine-tuned implicit functions

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 8, 3

## Abstract
Implicit functions such as Neural Radiance Fields (NeRFs), occupancy networks, and signed distance functions (SDFs) have become pivotal in computer vision for reconstructing detailed object shapes from sparse views. Achieving optimal performance with these models can be challenging due to the extreme sparsity of inputs and distribution shifts induced by data corruptions. To this end, large, noise-free synthetic datasets can serve as shape priors to help models fill in gaps, but the resulting reconstructions must be approached with caution. Uncertainty estimation is crucial for assessing the quality of these reconstructions, particularly in identifying areas where the model is uncertain about the parts it has inferred from the prior. In this paper, we introduce Dropsembles, a novel method for uncertainty estimation in tuned implicit functions. We demonstrate the efficacy of our approach through a series of experiments, starting with toy examples and progressing to a real-world scenario. Specifically, we train a Convolutional Occupancy Network on synthetic anatomical data and test it on low-resolution MRI segmentations of the lumbar spine. Our results show that Dropsembles achieve the accuracy and calibration levels of deep ensembles but with significantly less computational cost.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces 'Dropsembles', an approach to uncertainty modeling in fine-tuned neural implicit functions. 'Dropsembles' combines dropout-based methods with ensemble learning to balance computational efficiency and robust uncertainty estimation.
The authors conduct experiments on synthetic anatomical datasets and MRI segmentation tasks, demonstrating that 'Dropsembles' maintains predictive accuracy comparable to deep ensembles while reducing computational demands.

### Strengths
Key contributions include:

(1) A method for modeling epistemic uncertainty in fine-tuned implicit functions.  

(2) The application of Elastic Weight Consolidation (EWC) to address distribution shifts. 

(3) Experimental validation across toy and real-world datasets.

### Weaknesses
 (1) **Questionable motivation for EWC**:

**Lack of task distinction**: The dense and sparse datasets (Tasks A and B) are similar in content, which doesn’t align well with the typical use case for EWC in continual learning. EWC is usually applied to preserve knowledge across distinct tasks, so its application here appears unjustified or artificial. The datasets, while having different densities, represent the same underlying anatomical structures. This raises concerns about whether EWC is truly necessary or if it's being used as an ad-hoc regularization technique. The authors should clarify the specific distribution shift they are addressing with EWC, as the shift from dense to sparse data might not warrant the use of a method designed for distinct task transitions.

(2) **Limited novelty in dropsembles**:

**Lack of specificity to NIR**: Dropsembles combines dropout with ensembling in a straightforward way without tailoring it for neural implicit representations. This method may not provide significant innovation for uncertainty estimation in 3D reconstruction, particularly if it doesn’t leverage the unique characteristics of implicit functions. The approach seems to apply dropout and ensembling in a generic manner, without considering the specific properties of neural implicit representations, such as their continuous nature or spatial encoding. This raises questions about whether the method is truly optimized for this type of representation or if it's simply a standard application of existing techniques.

(3) **Insufficient baseline comparisons**:

Dropsembles is not compared to other standard uncertainty estimation techniques such as Bayesian neural networks, or other methods tailored to implicit representations [1]. This limits the evidence for Dropsembles’ effectiveness. The lack of comparison to Bayesian Neural Networks (BNNs) and variational inference methods, which are standard in uncertainty quantification, makes it difficult to assess the relative performance of Dropsembles. The authors should have included these baselines to provide a more comprehensive evaluation of their method's strengths and weaknesses.

(4) **Limited dataset diversity**:

**Narrow generalizability**: The experiments are focused on synthetic anatomical data and sparse MRI segmentation, which may not fully demonstrate Dropsembles' robustness across various domains or types of data shifts. The evaluation is limited to a narrow set of datasets, which raises concerns about the generalizability of the method to other types of 3D data and tasks. The authors should have included more diverse datasets to demonstrate the robustness of Dropsembles across different scenarios.

References:

[1] Stochastic Neural Radiance Fields: Quantifying Uncertainty in Implicit 3D Representations, 3DV 2021

### Questions
**Q1**: Why is EWC necessary if Tasks A and B are similar?

Could you clarify why EWC is used in this context, given that Task A (dense dataset) and Task B (sparse/noisy dataset) do not appear to be significantly different? Is the intent to quantify uncertainty in a continual learning setting, or is EWC applied simply as a regularization tool?
What makes Dropsembles particularly suited to neural implicit representations?

**Q2**: Dropsembles seems like a standard dropout-ensemble approach. Are there specific adaptations that make it uniquely effective for implicit functions in 3D reconstructions, especially regarding spatial consistency or grid-based predictions?
Considering Dropsembles combines well-known methods, why weren’t additional baselines, like Bayesian neural networks or variational inference-based [1], tested to provide a clearer comparison?

**Q3**: How does Dropsembles handle spatial dependencies?

Neural implicit representations often require spatial coherence across grid or voxel predictions. 
Does Dropsembles include any mechanism to maintain this spatial consistency in its uncertainty estimation, like [2]?

Could you discuss the limitations of Dropsembles in more detail?

**Q4**: Given that Dropsembles simply ensembles thinned models from dropout, what are its limitations in terms of computational cost, reliability, or adaptability to different 3D tasks?

**Minor**: The term "thinned network" isn’t a standard term in the field and may lead to confusion. It could be misinterpreted, as it doesn't clearly indicate that dropout is being applied.

**References**:

[1] Stochastic Neural Radiance Fields: Quantifying Uncertainty in Implicit 3D Representations, 3DV 2021

[2] Stochastic Segmentation Networks: Modelling Spatially Correlated Aleatoric Uncertainty, NeurIPS 2021

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
5

### Summary
The paper presents Dropsembles, a novel uncertainty quantification technique for neural implicit functions such as Neural Radiance Fields (NeRFs) and Occupancy Networks. This method aims to achieve the high accuracy and calibration of deep ensembles while significantly reducing computational overhead. By integrating Monte Carlo dropout with ensemble strategies, and leveraging Elastic Weight Consolidation (EWC), Dropsembles effectively handles distribution shifts and sparse, noisy data.

The primary focus is on addressing the challenges of 3D shape reconstruction from sparse and corrupted inputs. The method leverages high-quality, densely sampled synthetic datasets as shape priors to fill gaps and correct corruptions in the target data, even when distribution shifts occur due to noise and corruption. The premise is that these priors can guide the reconstruction process, ensuring more reliable outputs.

Initially, a Convolutional Occupancy Network is trained on high-quality synthetic data. During testing, the network is fine-tuned on individual sparse and noisy samples using EWC, which regularizes the adaptation process to prevent forgetting the original training data and to transfer prior knowledge effectively. This method involves creating ensembles through dropout, where binary masks generate multiple network instances. Each instance is then fine-tuned independently on the testing sample, forming an ensemble of networks initialized with correlated weights.

The paper validates the method through extensive experiments on toy datasets and low-resolution MRI segmentations of the lumbar spine. Results demonstrate that Dropsembles maintains accuracy and reliable uncertainty estimation and efficiently handles computational constraints and distribution shifts.

### Strengths
- The focus on uncertainty modeling in fine-tuned neural implicit functions addresses an underexplored area, contributing valuable insights into this challenging problem space.

- Dropsembles combines dropout and deep ensembles, offering a computationally efficient  training method for uncertainty estimation specifically tailored to neural implicit functions. This application of established uncertainty quantification and continual learning techniques to neural implicit functions is considered a novel contribution to neural implicit functions.

- The paper provides a rigorous experimental evaluation across synthetic and real-world spine datasets, effectively demonstrating that Dropsembles maintain prediction accuracy and uncertainty calibration under varying conditions.

- The method achieves significant reductions in computational costs during training compared to traditional deep ensembles, without compromising performance. However, computational demands during inference remain comparable to those of ensemble methods.

- The integration of Elastic Weight Consolidation (EWC) effectively mitigates the impact of distribution shifts, enhancing the model's robustness to noisy and sparse inputs.

- The approach is straightforward and versatile, capable of being integrated into various neural implicit networks and adapted to different task-specific training objectives, making it broadly applicable.

- The strategy of training on synthetic data while addressing distribution shifts between synthetic and real data is a pragmatic solution, particularly in scenarios where real-world data is scarce and noisy.

- The paper is clearly written, well-structured, and easy to follow.

### Weaknesses
 - While the method shows promise in specific tasks like lumbar spine reconstruction, broader application beyond medical imaging is not thoroughly explored or validated. The experiments primarily focus on shape reconstruction, and it's unclear how well Dropsembles would generalize to other tasks such as novel view synthesis or scene completion, which are also common applications of neural implicit functions. The lack of experiments on datasets with varying object topologies and complexities limits the assessment of the method's robustness.
- Despite reduced costs compared to deep ensembles, Dropsembles still require significant resources during fine-tuning, especially on high-resolution data. The fine-tuning process involves multiple network instances, each requiring individual optimization, which can be computationally demanding for large-scale datasets or high-resolution inputs. The paper does not provide a detailed analysis of the computational cost scaling with respect to input resolution or dataset size.
- Although Dropsembles handle sparse inputs well, the effectiveness on highly varied real-world scenarios with extreme data corruption could have been examined more comprehensively. The current experiments primarily focus on simulated noise and erosion, which may not fully capture the complexities of real-world data corruption, such as artifacts, occlusions, or non-uniform noise patterns. The method's performance under such conditions remains unclear.
- While Dropsembles generally outperform baselines, the improvements in some scenarios, particularly when using EWC, are not consistently significant across all metrics. The paper does not provide a detailed analysis of the scenarios where EWC provides minimal benefit, nor does it explore potential reasons for these inconsistencies. The lack of a clear understanding of when EWC is most effective limits the practical guidance for applying the method.

### Questions
- Could you provide more details on how the EWC regularization strength was selected? Is there a rationale beyond the empirical ablation studies, or could a more systematic method be developed?

- Have you tested Dropsembles on other types of neural implicit functions or datasets beyond those presented? How do you anticipate the method will perform in domains with significantly different characteristics?

- While the method reduces training costs, inference demands remain comparable to traditional deep ensembles. Are there potential strategies to also optimize inference efficiency?

- Given that synthetic data might not capture all real-world complexities, how do you ensure the generalization of the model to highly variable or unseen real-world data?

- Can you elaborate on the effectiveness of Dropsembles in handling extreme distribution shifts? Are there specific limitations or edge cases where the method struggles?

- How easily can Dropsembles be integrated into existing neural implicit networks? Are there any specific prerequisites or limitations that practitioners should be aware of?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper explores the topic of uncertainty modeling for decoder fine-tuning in implicit neural representations for occupancy representations. The presented method employs a combination of widely used uncertainty modeling concepts (i.e., dropout, ensembling) and the elastic weight consolidation concept stemming from continual learning, with the notion of fine-tuning, allowing to obtain multiple (fine-tuned) models at less training cost, with partially improved or comparable performance in modeling the uncertainty. This is demonstrated in experiments with toy examples (Sinusoidal decision boundary, MNIST) to medical shapes with the perseverance of reconstruction accuracy.

### Strengths
Originality: While the paper builds upon technical concepts from the uncertainty modeling community and does not introduce novel technical components, I believe the explored application and conclusions are novel and impactful.

Quality: The paper is very well structured and intuitive. The presentation and writing of the method are very clear, and in combination with the experiments, the method is sound.  

Clarity: The paper is well written in all sections, especially in related work and methods, making it a charm to read. It really flows. I also really enjoyed how well the method was put into the context of related work (i.e. very thoroughly research in different areas) and how the method was described in a simple and comprehensive way. Moreover, the authors detail every aspect of the experimental design in the main paper, and together with the supplementary this makes the evaluation of the presented method easy to follow. This, together with the accessibility of the source code, facilitates reproducability of the experiments. 

Significance: While implicit neural representations are often trained - individually - for (single) images and other signals, cohort-based training is quite common for shape completion in SDFs and occupancy representations. Given the prevalence of encoder-/decoder in these settings, this paper constitutes a meaningful exploratory study in the modeling of decoder uncertainty.

### Weaknesses
1) Related Work:

As detailed above, the paper is very well written and conducts a very thorough related work section. However, I think it would be important to touch upon one more area - i.e. the more recent architectures used in cohort-based training that also use encoder frameworks. Specifically, it would be interesting to discuss the advancements in [1,2], given that these constitute more recent alternatives to the DeepSDF architecture. As both works [1,2] use encoder-/decoder settings in combination with weight modulation approaches, this would also add emphasis to the relevance of this work.

2) Experimental Design: While the experimental design is sound, I believe the paper could have explored a higher variation of datasets and application scenarios.

(a)  Experiments not only for Re-LU-based networks but also for other activation functions:
While ReLU networks were routinely used in [3,4,5] medical applications, the INR community has shifted towards other activation functions [6] or embedding/projection functions [7,8] (particularly for images). While not all (novel) shape modeling applications use these (yet?), I believe it would have been interesting to explore if the same holds true for, e.g., SIREN [6]. This ablation would have been simple, as it merely requires a change in the MLP and DeepSDF [3], which also works well with sinusoid activation functions [6]. Moreover, it has been comparatively less explored if dropout and other anomaly detection frameworks are useful in this context. Thus, for decoder-based uncertainty modeling, for example, in the context of [2], such an ablation study would be ultimately interesting and relevant.

(b) Experiments on more common (shape) datasets, especially with SDFs: The authors state that their method is relevant for both SDF and occupancy representations but only conducts experiments for occupancy networks. Given that the training setup would not change much, I believe it would have been interesting to show experiments in an established shape dataset as well (e.g. (Med-) ShapeNet).

### Questions
Importance of encoder design / Application in auto-decoder setting:

Q1: Given the suitability of INRs for non-grid data, it is sometimes challenging to design an encoder for non-grid data. How was the encoder used/designed for the MNIST case, where some pixels are occluded? Did the encoder see the entire image (e.g., with a CNN-based encoder)? Sorry if I missed this; I would really appreciate an answer, even if it does not change the comparability of the different methods/baselines.

Q2: In the INR community, auto-decoder settings are quite common as well (see DeepSDF or Mehta et al.). Could the same method also be used in this case, given that the encoding of, e.g., the shape or instance stems from the same MLP, or are there any theoretical limitations that prohibit a meaningful uncertainty in this case?

### Soundness
3

### Presentation
4

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
In this work, authors introduce Dropsembles, a novel method for uncertainty estimation in tuned implicit functions. They demonstrate the efficacy of this approach through a series of experiments, starting with toy examples and progressing to a real-world scenario. Our results show that Dropsembles achieve the accuracy and calibration levels of deep ensembles but with significantly less computational cost.

### Strengths
1.  The topic of this work is really interesting. By utilizing an implicit shape model, points with sparse shapes can be densified with refined shape representations.
2.  This is the first work to model epistemic uncertainty in the implicit decoder during finetuning from synthetic data.

### Weaknesses
1.  The core concept of this work is uncertainty modeling. There are two innovative designs proposed in this paper. For the Elastic weight consolidation strategy, it seems that no remarkable improvements are done. Authors simply employ EWC to adapt pretrained models from dataset A. The other component is Dropsembles, please provide a more detailed description on its contribution.
2.  Since Dropsembles is aimed for the tradeoff between computational costs and accuracy. However, no quantitative results are given in the experimental part. Authors should carefully list out the comparison between dropsembles and other methods on uncertainty estimation.
3.  The improvement on lumbar spine seems to be marginal, maybe a detailed analysis is required.
4.  The effectiveness of this method is highly required for the evaluation on more challenging datasets, such as Medshapenet, etc.

### Questions
Please refer to the weakness part.

### Soundness
2

### Presentation
3

### Contribution
2
