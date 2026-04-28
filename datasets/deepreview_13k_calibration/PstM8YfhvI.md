# MorphoDiff: Cellular Morphology Painting with Diffusion Models

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 3, 8, 8

## Abstract
Understanding cellular responses to external stimuli is critical for parsing biological mechanisms and advancing therapeutic development. High-content image-based assays provide a cost-effective approach to examine cellular phenotypes induced by diverse interventions, which offers valuable insights into biological processes and cellular states. In this paper, we introduce MorphoDiff, a generative pipeline to predict high-resolution cell morphological responses under different conditions based on perturbation encoding. To the best of our knowledge, MorphoDiff is the first framework capable of producing guided, high-resolution predictions of cell morphology that generalize across both chemical and genetic interventions. The model integrates perturbation embeddings as guiding signals within a 2D latent diffusion model. The comprehensive computational, biological, and visual validations across three open-source Cell Painting datasets show that MorphoDiff can generate high-fidelity images and produce meaningful biology signals under various interventions. We envision the model will facilitate efficient in silico exploration of perturbational landscapes towards more effective drug discovery studies.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a novel generative model framework called MorphpDiff, which produces high-resolution cell morphology images in response to a drug or genetic perturbations. The authors leverage the use of latent diffusion models combined with perturbation-specific embeddings to simulate cellular response.  This model provides an alternative to traditional lab assays/screens by generating silicon drug and genetic responses in the cell. MorphoDiff is validated using three publicly available datasets (RxRx1, BBBC021, and Rohban et al. l Cell painting dataset)  ensuring that they have cell shape and state variability and perturbations. These models are evaluated with common image fidelity and metrics including Frechet Inception Distance (FID) and kernel Inception Distance (KID) showing improvements over the standard stable diffusion. Most importantly, the authors were able to capture cell morphology changes using CelProfiler for PCA and other morphology-based metrics.

### Strengths
MorphoDiff method shows novel methods combining latent diffusion models with perturbation embedding to predict cellular morphologies. The model generalizes across different cell types, drugs, and genetic alterations better than the standard stable diffusion model. It performs better than the standard diffusion model showing that the perturbation embedding helps the model learn and has the dual capability with gene knock-in/out and small molecule perturbations. 
The authors use public and diverse datasets to validate their model and have clear reporting on how these were used. The model seems to generalize across different perturbations. The authors use generative metrics as well as biological meaningful metrics to evaluate the performance of their model. The models are tested using tools like CellProfiler to get interpretable and comparable results to the ground truth biological data.

This method scales and enables larger high-content screens for drugs. It provides a tool for simulating the effects of drugs or other genetic perturbations.

### Weaknesses
MorphoDiff fails to generalize to compounds that are out-of-distribution, and seems like it performs better at the lower frequency than the high-frequency features. How accurate is this model and how consistent is it at capturing other cellular structures across the cell? In many of these stages, cell cycle plays a big role. Here, the paper lacks exploring how their model handles more complex events in the fields of view such as cell division. This method relies on RGB images, it would be interesting to do an ablation study and see the performance with fewer channels.

### Questions
- Could the authors clarify the failure modes of MorphoDiff and the range of validity? How does the model perform across a broad range of drugs and genetic perturbations? Is there a category of drugs where the performance drops?

- What kind of data augmentations were made and how do these impact the generalization across different drugs and genetic perturbations? I suggest ablations to improve the model's robustness. Additionally, could the authors consider conducting ablation studies to identify which augmentations make the model more robust?

- What are the other factors were included in the selection of perturbation conditions? Did you add prior information such as concentrations of chemicals?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper addresses the challenge of virtual phenotypic screening for drug discovery.  The authors train a guided 2D latent diffusion model on microscopy images (with Cell Painting markers) to generate images of cells, as they would appear after treatment with a genetic or chemical perturbation.  In order to guide the model, they use embeddings of the corresponding perturbation: RDKit for compounds and scGPT for genes.

The authors fine-tune the publicly available Stable Diffusion v1.4 on three different Cell Painting datasets: Rxrx1 (siRNA), BBC021 (compound) and Rohban (over-expression), and compare the impact of the Perturbation Identifier Module for guiding the image generation process.  In addition to standard image quality metrics (FID and KID), the authors also use the popular Cell Profiler framework to extract engineered features from both real and generated images, and compare their ability to cluster perturbations by perturbation ID (ie, replicate) and mechanism of action (MOA).  The authors also evaluate correlation of Cell Profiler features extracted from real and generated images, demonstrating the impact of guiding the image generation process with perturbation embeddings.

### Strengths
The paper is clearly described, including a thorough description of the model, datasets and training procedure.  It also includes links to code for data conversion, the pre-trained Stable Diffusion model, and author's fine-tuning script, which taken together provide a high level of reproducibility.

One of the main contributions of the paper is to apply state-of-the-art guided diffusion models to the task of virtual phenotypic screening.  Other papers have similarly applied generative models (GANs and flow-based models); however, this is the first application of diffusion models (that I'm aware of) to this task.  The generated images look high quality, despite fine-tuning on a relatively small training set of Cell Painting images.

In addition, the authors evaluate their method on 3 independent open-source datasets: Rxrx1, BBBC021 and Rohban.

### Weaknesses
Major concerns:

My primary concern with the paper is regarding benchmarking of the MorphoDiff model against other methods.  In particular, the only comparison that is included throughout the paper is a baseline of Stable Diffusion (without guidance by the Perturbation Identifier module).  While this comparison is positive in all cases, in my view it is equivalent to an ablation study, demonstrating that the model is leveraging the information in the perturbation embeddings.  It doesn't demonstrate if the model accuracy is sufficiently high to be useful in virtual phenotypic screening, or compare the model performance against other published models such as Mol2Image, IMPA, or GRAPE (https://arxiv.org/pdf/2406.07763).  I suggest including additional discussion and comparisons of other published methods, and expanding the analysis of MOA inference to a larger set of MOA classes, as it's a core evaluation metric for phenotypic screening.

In addition, while the method is nicely implemented and clearly explained in the paper, I find it does not have high novelty compared to other methods (Mol2Image, IMPA, GRAPE) for generating images of cellular morphology under perturbation, and therefore a rigorous comparison of MorphoDiff's performance relative to the existing state-of-the-art would be very important to demonstrate a significant contribution from the paper.

Additional concerns:

The MorphoDiff model was fine-tuned on very small datasets, each on the order of 1000 perturbations.  Much larger Cell Painting datasets have been released in recent years, such as JUMP (120,000 perturbations) and Rxrx3 (20,000 perturbations).  Demonstrating the capability of MorphoDiff on these datasets would make it more impactful related to the current state-of-the-art for virtual phenotypic screening, such as MoCoP (https://www.biorxiv.org/content/10.1101/2023.05.01.538999v3.full.pdf).  I suggest the authors discuss the potential challenges of applying diffusion models to large Cell Painting datasets, and how these could be overcome to advance the field of generative virtual phenotypic screening.

The images generated based on perturbations seen during training look quite good.  However, in each case, they are shown for very strong drug treatments, such as cytoskeletal destabilizers.  It would be informative to demonstrate if MorphoDiff can capture more subtle phenotypes that are typically present in phenotypic screens.

In the conclusion, the authors suggest that future work could establish standardized evaluation frameworks for this emerging field.
 I recommend to check out the following paper that provides a framework and numerous metrics for evaluating perturbative maps: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1012463

In Figure 3b, very few MOA clusters were considered.  I suggest leveraging datasets with a larger number of available MOAs / gene clusters.  One such option would be to show the 1108 siRNA perturbations in Rxrx1 (used in the paper); however, due to the large off-target effects of siRNA that may not be very meaningful.  In which case, JUMP would provide another option.

In Figure 3c, comparing NMI of morphoDiff on Perturbation ID doesn't seem meaningful.  I may have misunderstood this point, but it seems that the variation in Cell Profiler features extracted from morphoDiff with a constant Perturbation ID should reflect only the noise in the generation process.  Whereas the real data will have large technical effects between replicates.  As such, I would expect a generative model to be more self-consistent than the raw data (which is known to be very noisy at the replicate level).  I suggest focusing evaluation on the MOA clustering (ideally on an expanded MOA set), and perhaps investigating the effect of diversity/noise in the generation process on the accuracy of MOA clustering.

In Figure 4a, the correlation coefficient between CellProfiler features extracted from MorphoDiff vs features extracted from real images for the same perturbation is close to zero.  I suggest including a separate measure of the correlation of CellProfiler features between replicates (real images) of the same perturbation, to provide a rough upper-limit for how strongly we could expect the model to correlate with real data.  If the model correlation is similar to the replicate correlation, then it can be argued more meaningfully that the model generated images are "interchangeable" with real data.

Finally, the authors observe that the similarity of images generated by MorphoDiff relies on the similarity of the output from the perturbation embedding module.  In other words, the model does not learn an improved perturbation embedding from the data, as for example Mol2Image and GRAPE do. As such, it's not clear to me that this approach would be informative in a virtual screening setting, where the goal is to learn a predictive embedding of unseen perturbations that improves generalization beyond eg, the performance of RDKit.  I suggest additional discussion on the implications of this limitation for virtual screening, and how they might be addressed through modifications to the Perturbation Embedding Module.

### Questions
Suggestions (summarized from above):
1. Train the MorphoDiff model on larger CellPainting datasets, to improve the learned relationship between perturbation and phenotype
2. Evaluate model performance in the harder case of more subtle phenotypes
3. Conduct additional evaluations on datasets with a larger number of MOA clusters, leveraging the evaluation framework from: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1012463
4. Explore the possibility of updating the Perturbation Identifier Module with learned perturbation embeddings, which would provide a more useful output in the scenario of virtual phenotypic screening.

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
The paper introduces MorphoDiff, a novel generative model designed to predict high-resolution cellular morphologies in response to different chemical and genetic perturbations. Using a latent diffusion model and a perturbation projection module, MorphoDiff generates images that mimic cellular phenotypes across multiple datasets. The model is validated through common generative modelling metrics, visual assessments, and biologically interpretable feature analysis, showing its ability to capture perturbation-specific and mechanism-of-action (MOA)-specific morphology. MorphoDiff aims to support drug discovery by enabling in silico exploration of large perturbational landscapes.

### Strengths
1. **Proposed Impact:**

The MorphoDiff framework’s potential to generate biologically meaningful cellular images based on perturbations could greatly impact drug discovery and cellular profiling. This innovation might streamline in silico analysis of large drug libraries and provide a baseline for future generative work in this domain.

2. **Writing and Accessibility:**

The paper is well-organised and clearly written, allowing readers from diverse backgrounds to follow the technical details of the diffusion model, perturbation embedding, and validation steps.

3. **Thorough Experimental Validation:**

The authors provide comprehensive computational, visual, and biological validations across multiple datasets, which demonstrates the versatility and robustness of MorphoDiff. The quantitative metrics, qualitative results, and the consistent comparative performance against Stable Diffusion enhance the reliability of their claims.

4. **Biological Insight:**

By clustering CellProfiler features, the authors demonstrate that the generated images capture perturbation-specific cellular morphology that aligns with real biological signals. 

5. **Generality Across Chemical and Genetic Perturbations:**
MorphoDiff’s capacity to handle diverse perturbation types — both genetic and chemical — indicates potential applications across a wide range of experimental conditions, making it a versatile tool in cellular morphology prediction.

### Weaknesses
1. **Statistical Significance Lacking Clarity:**

The term "statistically significant" is used frequently (e.g., in results regarding FID and KID metrics) without detailing which statistical tests were applied or providing p-values. The methodology section would benefit from specifying these statistical tests to support the significance claims convincingly. Please could the authors specify which statistical tests were used for comparing FID and KID metrics between MorphoDiff and the baseline, and to provide p-values where applicable. It is crucial to know whether the comparisons are based on paired or unpaired data, as this will affect the choice of statistical test (e.g., t-test, Wilcoxon test). Furthermore, reporting effect sizes alongside p-values would provide a more complete picture of the magnitude of the differences observed.

2. **Missing Citations for Established Findings:**

 Statements that reference existing biological knowledge, such as "MorphoDiff images revealed biological evidence that corroborates established findings," should include appropriate citations. This would anchor these statements in established literature. Please provide specific examples of relevant literature or established findings that support the claims about biological evidence. Specifically, the authors should clarify which specific biological pathways or mechanisms are being corroborated and provide references to studies that have previously identified these mechanisms.

3. **Limited comparison to other methods:**

The authors compare MorphoDiff to Stable Diffusion, however, overlook other methods like PhenDiff. Although PhenDiff was proposed for cropped images, this can easily be extended. Could the authors extend their comparison to include PhenDiff? If not, could the authors discuss why this was left out of comparison? Furthermore, the authors should consider comparing against other relevant generative models that have been applied to similar biological image generation tasks, such as those based on GANs or VAEs, to provide a more comprehensive benchmark of their method's performance. A comparison to Mol2Image would also be beneficial, given its focus on generating images from molecular structures.

4. **Minor:**

- There are occasional instances of incorrect citation formatting, which might distract readers or reduce clarity. For example, “...generative models in computer vision Rombach et al. (2022) and integrating state-of-the-art…”. Rombach et al. (2022) should appear in parentheses here. There are numerous other examples of this. Furthermore, citations like “Saha et al.” are missing the publication year, which should be updated to 2024​.
- The sentence “comparing standard-processed and cropped images in the BBBC021 experiments showed a slight improvement…”, should point to the results. I assume this is referring to Appendix Table 5.

### Questions
1. **Clarity on Clustering Technique:**

The term “KNN clustering” is ambiguous. It’s unclear if the authors mean k-means clustering or a different method. Given the context of CellProfiler feature clustering, clarifying this point would improve readability and understanding of the methodology.

2. **Assessing Combination Therapies:**

Combination therapies, where multiple drugs or genetic modifications are applied simultaneously, are increasingly important in personalised medicine and complex disease treatment strategies. Assessing cellular responses to these combinations is crucial, as interactions between therapies can lead to synergistic effects, enhanced efficacy, or reduced side effects that might not be observed with single agents alone. Given MorphoDiff's promising results with single perturbations, could the model be adapted or extended to predict morphology for combination therapies? Specifically, what modifications would be necessary to capture the interactions between therapies accurately, and are there unique challenges in validating these predictions with current datasets?

### Soundness
4

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
The authors propose MorphoDiff, a perturbation-based conditional latent diffusion model designed to generate high-resolution images of drug-treated cell morphologies. The model incorporates both chemical and genetic perturbations as conditioning inputs, enabling it to generalise across diverse interventions. Evaluations indicate that MorphoDiff exceeds the performance of a conventional Stable Diffusion model in replicating biologically realistic cellular responses, with strong results in both visual fidelity and biological interpretability.

### Strengths
## Clear Structure and Motivating Background: 
The paper is well-organised, with each section contributing logically to the overall narrative. The background provides a thorough review of core concepts in conditional diffusion modeling, highlighting the advantages of diffusion models for image generation tasks in biological contexts. 

## Innovative Use of scGPT for Perturbation Conditioning: 
This integration of a large, pre-trained transformer model to embed meaningful genetic perturbation features enables MorphoDiff to generalise across complex perturbations with improved accuracy, potentially opening new avenues for generative applications in cellular biology. 

## Comprehensive Biological Validation Beyond Standard Generative Metrics: 
The authors go beyond typical generative metrics such as FID by evaluating MorphoDiff’s performance on biological realism through CellProfiler, a tool widely used in biological research. This thorough approach highlights the biological validity of generated samples by extracting quantitative morphological features, offering a layer of interpretability and trustworthiness that is essential for practical applications in drug discovery. The use of CellProfiler also strengthens the model’s credibility by demonstrating the relevance of the generated images in a real biological context, not just in terms of visual fidelity.

### Weaknesses
## Limited Range of Comparative Baselines: 
While MorphoDiff is evaluated in terms of biological interpretability and generative quality, the paper lacks a sufficient range of comparative baselines, particularly given the advancements in conditional latent diffusion models. The authors mention MO2Image, yet they do not compare their approach to several other conditional diffusion models that could have served as relevant baselines. For instance, competing methods like PhenDiff [1] offer similar approaches in generating drug-treated cellular images using conditional diffusion. Expanding the range of baselines would solidify MorphoDiff’s competitive advantage and contextualise its performance relative to other SOTA models. 

## Clarification on Novelty Claims: 
The claim that MorphoDiff is the first to handle both chemical and genetic perturbations in a conditional latent diffusion model is somewhat overstated, as methods like PhenDiff [1] have previously addressed similar challenges. Citing these comparable methods (or similar) and clearly articulating MorphoDiff’s unique contributions (e.g., specific model adaptations, or validation approach) would improve the transparency of the novelty claim. 

## Insufficient Detail in Key Methodological Components: 
Certain methodological sectionsc lack sufficient depth, making it difficult to reproduce the model. The perturbation projection module, which appears to be a crucial element of MorphoDiff’s design, is only briefly discussed. Given that this module enables MorphoDiff to conditionally generate diverse morphological responses, more information on how it was adapted for this task would enhance clarity and allow for reproducibility. Furthermore, the absence of code or a repository also hinders reproducibility.

## Overlooked Metrics for Sample Variability: 
The paper does not address generated sample variability or uniqueness within the output set for each condition. Evaluating generated sample uniqueness is particularly important in high-fidelity generation, as latent diffusion models can sometimes suffer from mode collapse, resulting in overly similar or even identical samples across iterations. Implementing additional metrics such as Structural Similarity Index (SSIM) could quantify the variability of generated samples within each condition, helping to ensure MorphoDiff generates a diverse range of morphologies. These metrics would also provide insight into the model's robustness and its ability to capture subtle differences in morphological responses across varying treatments.

### Questions
## Sensitivity to Diffusion Model Selection: 
How sensitive is MorphoDiff to the choice of latent diffusion model? The authors use Stable Diffusion as a baseline, but further exploration into alternative pre-trained diffusion models could provide valuable insights.

### Soundness
3

### Presentation
4

### Contribution
3
