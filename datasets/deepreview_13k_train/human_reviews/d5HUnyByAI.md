# CLIBD: Bridging Vision and Genomics for Biodiversity Monitoring at Scale

- Decision: Accept
- Scores: 3, 6, 6, 3

## Abstract
Measuring biodiversity is crucial for understanding ecosystem health. 
    While prior works have developed machine learning models for taxonomic classification of photographic images and DNA separately, in this work, we introduce a \textit{multimodal} approach combining both, using CLIP-style contrastive learning to align images, barcode DNA, and text-based representations of taxonomic labels in a unified embedding space. 
    This allows for accurate classification of both known and unknown insect species without task-specific fine-tuning, leveraging contrastive learning for the first time to fuse DNA and image data. 
    Our method surpasses previous single-modality approaches in accuracy by over 8\% on zero-shot learning tasks, showcasing its effectiveness in biodiversity studies.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors present a paper on a CLIP-based approach combining images, DNA barcodes and textual taxonomic description for biological classification (specifically of insects) in an open-set setting. Experimental results show that the method is effective and outperforms dual-modality contrastive learning approaches, as well as other approaches from the literature on this specific task.

### Strengths
1) The paper is well-written and and organized. The proposed approach and the experiments are clearly described.

2) The proposed approach is effective in tackling the problem at hand, while being simpler than common alternatives in the field.

### Weaknesses
1) The paper presents no methodological novelty, and mostly applies existing techniques in a standard way to a particular use case.

2) In Tab. 1, what is the point of comparing non-aligned embeddings? It seems intuitive that there should be no correspondence in the learned representations.

3) The attention visualization is not discussed in detail. Also, as mentioned above, what information comes from checking classification before alignment? Wouldn’t correct predictions be random in that case?

### Questions
1) In Tab. 1, what is the point of comparing non-aligned embeddings? It seems intuitive that there should be no correspondence in the learned representations.

2) The attention visualization is not discussed in detail. Also, as mentioned above, what information comes from checking classification before alignment? Wouldn’t correct predictions be random in that case?

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The approach proposes multimodal contrastive learning between image, DNA and text (taxonomic labels) as opposed to Image+TaxonomicLabel only approach followed by previous work (BioCLIP). The usage of DNA is claimed to be better because, (1) classifying unseen species would be difficult with a taxonomic-label-only model because the species name would not have been seen during training, (2) DNA is easier to obtain compared to taxonomic label which requires careful examination by human experts.

### Strengths
1.	Incorporation of DNA as a modality to align the image embedding against instead of text is well motivated.
2.	Extensive experiments and ablations are provided.

### Weaknesses
1.	The accuracy when doing image to DNA on unseen species is not quite significant although it is better than BioCLIP’s approach of doing image to text. This indicates the image encoder is still not strong enough to generate a good DNA aligned embedding just from the image. Perhaps this can improve with more data.


### Questions
Some suggestions and questions,

1.	Comparison with BioCLIP at different taxa levels: Going by the works claim, incorporation of DNA embeddings could help with classifying unseen species up to species level, but I’m guessing at higher taxonomic levels the BioCLIP performance should be comparable to CLIBD. It would be interesting to see a comparison.
2.	From Table 1, Image-to-DNA performance on seen species reduces going from (I+D) to (I+D+T), why is this happening? I would have expected the performance to improve.
3.	I’m also curios to know why BIOSCAN-5M was not used, considering that foundational models such as these can greatly benefit from more data.
4.	I personally felt Figure 7 was more informative to understand the data partitioning than Figure 2 (Just to consider in the future revisions).

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
This paper proposes a CLIP-based method to jointly embed images, DNA barcodes, and taxonomic strings for different insect species. The method is evaluated on cross-modal matching and species classification, with qualitative and quantitative results provided. The paper compares against one external method (BIOCLIP) in one set of experiments and one external method (BZSL) in a second set of experiments. The key claim of the paper is that jointly learning from the modalities of images, DNA, and taxonomic information leads to stronger representations for downstream use.

Note: Score increased after rebuttal.

### Strengths
* The idea of jointly embedding DNA barcodes with images and taxonomic information is interesting.
* The experiments in the paper are extensive - there is a lot of technical content, and it's clear that a lot of effort went in to this work. There are many quantitative results, in addition to interesting qualitative results (e.g. Fig. 3, Fig. 5).
* The paper is very well-written. 
* The hyperparameters and training procedures are clearly spelled out.

### Weaknesses
My major issue with the paper is missing baselines:
* The paper compares their multimodal representation learning approach against the unimodal pretrained models they start with. They show that their method is better, and conclude that multimodality is important. However, this claim is not justified - couldn't the benefit be from the additional training each modality received? It seems to me that the fair comparison would be to take the unimodal models and run unimodal CLIP-style training (with a similar computation / # steps budget) for each. If the multimodal model beats these CLIP-fine-tuned unimodal models, then that provides stronger evidence of the benefit of multimodal learning. Specifically, the authors should perform contrastive learning on each modality separately, using the same training budget as their multimodal approach, to isolate the effect of multimodality. This would involve training an image encoder with image-image contrastive loss, a DNA encoder with DNA-DNA contrastive loss, and a text encoder with text-text contrastive loss, all using the same dataset and training steps as the multimodal model. Without these baselines, it's unclear if the performance gain is from multimodality or simply from more training on the target dataset.
* For the image encoder, wouldn't a model pretrained on BIOSCAN-1M be a more appropriate starting point / baseline than an ImageNet-pretrained model? The use of an ImageNet pretrained model may introduce a domain gap, and a more relevant pretraining dataset such as BIOSCAN-1M could lead to better performance or serve as a more appropriate baseline for comparison. This is especially important given that the authors are using a dataset from the BIOSCAN project.

The paper should address a few items that were not discussed:
* Are there confounders we need to worry about in this data, e.g. the facility the data was collected by? While the authors mention the data is from BIOSCAN-1M, they do not discuss potential biases that could arise from the data collection process. For example, if the data was collected at different times or by different teams, this could introduce confounding variables that affect the results. It would be important to discuss the data collection protocols and any potential sources of bias.
* The DNA to DNA matching results are very high, but shouldn't we expect this? Would simple homology methods based on string matching do a very good job at this task? What is the benefit of using deep embeddings to solve this problem? The authors should compare their method to simple homology-based methods like BLAST, which are commonly used for DNA sequence matching. If these methods perform similarly well, the added complexity of deep embeddings may not be justified for this specific task. The paper should clarify the advantages of using deep embeddings over simpler, more established methods for DNA matching.
* Doesn't adding a modality increase the number of steps of training the model receives? Couldn't this be partly responsible for the differences between 1, 2, and 3 modalities in Table 1? The authors should clarify whether the number of training steps or epochs is kept constant when adding modalities. If the number of training steps increases with the number of modalities, this could be a confounding factor in the results. The authors should control for this by ensuring that all models are trained for the same number of steps, regardless of the number of modalities used.
* Image-DNA and Image-text matching don't seem very good based on Fig. 4, with the average being pulled up by a few good cases. What are those cases, and why are they different? Is there any insight to be gained there? The authors should provide a more detailed analysis of the cases where the model performs well and poorly. It would be helpful to understand what characteristics of the images, DNA, or text lead to successful or unsuccessful matching. This could provide insights into the limitations of the model and areas for improvement.

A few claims made in the paper were not clear to me:
* The paper claims that "BIOCLIP... requires taxonomic labels to be available in order to obtain text descriptions. These labels can be expensive and time-consuming to obtain" and that "DNA barcodes can be obtained at scale more readily than taxonomic labels". These claims are not intuitive to me. How much does DNA barcoding cost per individual, compared to the cost of having an expert inspect an image to identify the species? The authors should provide a more detailed comparison of the costs and time involved in obtaining taxonomic labels versus DNA barcodes. This should include specific cost estimates and time requirements for each process. The claim that DNA barcoding is more readily available needs to be supported by concrete evidence.
* The training data for BarcodeBERT is claimed to be "different from, but highly similar to" the data used in this paper  - can you expand on what this means, and the implications for the results presented? The authors should clarify the exact nature of the BarcodeBERT pretraining data and how it differs from the data used in this paper. This should include details about the species, genes, and geographic locations of the samples used in each dataset. The implications of this similarity should also be discussed, including any potential for data leakage or bias.

### Questions
Please see weaknesses for primary questions. 

Minor comments / questions (no need to respond):
* This work focuses on the cases where aligned data is available: images and DNA barcodes from the same individuals. It might be useful to extend the method to also take advantage of abundant unpaired data: images and DNA barcodes that are not paired. 
* Figure 2 could be clearer. Why are there different shades of blue and orange? Why don't the numbers in the boxes sum up to 36729? Generally, this figure did not aid my understanding (though many of my confusions were clarified in later text and figures). 
* It would be nice to have a chance-level baseline in Table 1. 
* Down the road, it might be interesting to try to integrate additional modalities, e.g. geospatial location (https://arxiv.org/abs/1906.05272).

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes CLIPBD, a tri-modal embedding space consisting of image, text and DNA of insect specimens. CLIPBD is trained using a three-way contrastive learning objective between image, text and DNA on the BIOSCAN-1M dataset. Using a reference database of images and DNA, CLIPBD is able to classify images of seen and unseen species. Results reported in the paper show superior performance as compared to BioCLIP and other state-of-the-art DNA encoder models.

### Strengths
- The motivation and problem formulation is sound and interesting.
- The proposed model fuses images, text and DNA into a contrastive embedding space enabling zero-shot image classification of unseen species.
- The flow of paper and writing is good in general.

### Weaknesses
 - The abstract claims the paper is the first to use contrastive learning to fuse DNA and image. However, there are existing works [1, 2, 3] which have done this for other applications and they should be discussed in the related works.
- The claim that *DNA is a better target than taxonomic labels* (**Line 316**) is highly questionable. This claim is reiterated in **Lines 359-362**. The paper clearly mentions that majority of the BIOSCAN-1M dataset does not have taxonomic labels. In fact only 3.36% pretraining data has labels upto the species level (**Line 321**). It is clearly seen from **Table-1** that aligning with taxonomic labels outperforms aligning with DNA at the order level. I believe if the authors used an **unbiased dataset** containing the same proportions of DNA labels and taxonomic labels, the results would have been similar if not worse. This is more of a problem of the dataset and not the modality itself. The authors should also consider the computational cost of processing long DNA sequences compared to short taxonomic labels.
- Following the previous point, why does Image-to-DNA retrieval performance improve at the species level when aligning all three modalities (**Table 1**)?
- For inference to work on unseen species during training, the framework assumes that their DNA and/or images are available in the lookup database. This is an unrealistic assumption. If the images and DNA are already available for unseen species, they might as well should have been used for training. The paper does not clearly define the size and composition of this reference database.
- Limited technical novelty considering no new representation learning technique has been proposed. The paper uses an existing dataset containing 1M insect specimens and unbalanced DNA and taxonomic labels, raising questions on the effectiveness of the method on other real-world datasets. Majority of the experiments and evaluations are only shown for a single dataset. The authors should also consider the storage cost of maintaining a database of long DNA sequences compared to short taxonomic labels.
- The authors correctly pointed that BioCLIP was trained on diverse set of species including natural images. However, one easy way to utilize the BioCLIP embedding space would be to align the DNA modality with frozen BioCLIP vision and text encoders. Have the authors compared their method with this ImageBind-style training?

### Questions
Details about the reference database is missing. How many images and DNA barcodes are present in the reference database during inference?

### Soundness
1

### Presentation
3

### Contribution
2
