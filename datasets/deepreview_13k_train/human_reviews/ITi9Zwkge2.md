# HATFormer: Historic Handwritten Arabic Text Recognition with Transformers

- Decision: Reject
- Scores: 6, 5, 6, 5

## Abstract
Arabic handwritten text recognition (HTR) is challenging, especially for historical texts, due to diverse writing styles and the intrinsic features of Arabic script.
Additionally, Arabic handwriting datasets are smaller compared to English ones, making it difficult to train generalizable Arabic HTR models. To address these challenges, we propose \proposedSystemName{}, a transformer-based encoder--decoder architecture that builds on a state-of-the-art English HTR model. 
By leveraging the transformer's attention mechanism, \proposedSystemName{} captures spatial contextual information to address the intrinsic challenges of Arabic script through differentiating cursive characters, decomposing visual representations, and identifying diacritics.
Our customization to historical handwritten Arabic includes an image processor for effective ViT information preprocessing, a text tokenizer for compact Arabic text representation, and a training pipeline that accounts for a limited amount of historic Arabic handwriting data.
\proposedSystemName{} achieves a character error rate~(CER) of 8.6\% on the largest public historical handwritten Arabic dataset, with a 51\% improvement over the best baseline in the literature.
\proposedSystemName{} also attains a comparable CER of 4.2\% on the largest private non-historical dataset.
Our work demonstrates the feasibility of adapting an English HTR method to a low-resource language with complex, language-specific challenges, contributing to advancements in document digitization, information retrieval, and cultural preservation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents an improvement on the transformer-based encoder-decoder architecture of the TrOCR OCR model. These improvements are designed to address the challenges of Arabic handwritten text recognition, particularly for historical texts. The architecture includes a custom image processor for ViT information pre-processing, a specialized text tokenizer for Arabic text representation, and a training pipeline optimised for limited historical Arabic data. The system is compared with several other HTR systems based on 3 public databases and generally outperforms them.

### Strengths
- Original use of line warping: The paper presents an innovative approach using line warping techniques to adapt elongated rectangular text lines into a square format suitable for Vision Transformers (ViTs). This adaptation is a solution to the challenges posed by the non-uniformity and the specific shape of handwritten text.

- Extensive pre-training on Arabic data: HATFORMER benefits from extensive pre-training on a synthetic Arabic dataset, which is critical given the limited availability of such data compared to English datasets. Note that using the English pre-training is still beneficial as showed in Table3

- Performance: The model outperforms a state-of-the-art model on one dataset, and is on par on 2 other datasets.
- Open-source : the code and dataset will be released

### Weaknesses
Ablation study results: The ablation study presents some unusual results that need further investigation. The finding that the removal of block processing leads to a significant performance degradation suggests that the novel image packing technique is beneficial. However, the fact that removing the custom byte pair encoding (BBPE) improves the results - almost to the level of the original model - raises questions. This behaviour is counterintuitive and should be investigated further. The authors should conduct additional experiments to clarify these results and rule out the possibility of bugs or unintended interactions within the model.

Generalisability: Although the aim is to develop a generic HTR model, the system has not been trained on all available datasets to assess its generalisation ability. Testing this generic model on different datasets would provide valuable insights into its robustness and adaptability to different handwriting styles and historical contexts.

L56 : "First, Arabic is written in cursive, making characters visually harder to distinguish"  English is also cursive
L68 : The number of handwritten pages in the RIMES data base is not 12500, because only a fraction of the database is fully handwritten
The OpenHART database is not mentioned in this section but it is composed of more than 40 000 annotated pages of handwritten Arabic https://catalog.ldc.upenn.edu/LDC2012T15. However, it is used in the experiments.


Related work section

References to full page recognition (for example DAN Coquenet, D., Chatelain, C., Paquet, T.: DAN: a segmentation-free document attention network for handwritten document recognition. IEEE Trans. Pattern Anal. Mach. Intell. 45(7), 8227–8243 (2023). https://doi.org/10.1109/TPAMI.2023.3235826)  are missing


L200 : "the proposed BLOCKPROCESSOR works by first horizontally flipping a text-line image"  : since the usage of the pre-trained English weights is capital, we can see that changing the order of the patches in the Vit would be doomed to failure. However, the approach of returning the image of the line is not very satisfactory because, on the one hand, it does not adapt the model to the specific characteristics of Arabic, even though the authors' objectives are to take these specific characteristics into account, and on the other hand, it poses serious problems in the event of mixing text in Arabic and Latin alphabets.

L201 : "finally warping it to fill in the ViT’s 384×384-pixel image container from left to right and top to bottom" : this means that the system could decode paragraphs

### Questions
L56 : "First, Arabic is written in cursive, making characters visually harder to distinguish"  English is also cursive
L68 : The number of handwritten pages in the RIMES data base is not 12500, because only a fraction of the database is fully handwritten
The OpenHART database is not mentioned in this section but it is composed of more than 40 000 annotated pages of handwritten Arabic https://catalog.ldc.upenn.edu/LDC2012T15. However, it is used in the experiments.


Related work section

References to full page recognition (for example DAN Coquenet, D., Chatelain, C., Paquet, T.: DAN: a segmentation-free document attention network for handwritten document recognition. IEEE Trans. Pattern Anal. Mach. Intell. 45(7), 8227–8243 (2023). https://doi.org/10.1109/TPAMI.2023.3235826)  are missing


L200 : "the proposed BLOCKPROCESSOR works by first horizontally flipping a text-line image"  : since the usage of the pre-trained English weights is capital, we can see that changing the order of the patches in the Vit would be doomed to failure. However, the approach of returning the image of the line is not very satisfactory because, on the one hand, it does not adapt the model to the specific characteristics of Arabic, even though the authors' objectives are to take these specific characteristics into account, and on the other hand, it poses serious problems in the event of mixing text in Arabic and Latin alphabets.

L201 : "finally warping it to fill in the ViT’s 384×384-pixel image container from left to right and top to bottom" : this means that the system could decode paragraphs

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper presents a transformer based method, HATFormer, to analyze historic handwritten Arabic. The authors proposed the BlockProcessor that effectively allows the vision transformer to learn from Muharaf Arabic dataset. The method beats existing CRNN methods in the Muharaf dataset.

### Strengths
* The authors described the BlockProcessor which helps preprocess the handwritten texts images for the ViT, substantially improves the performance. Although the authors applied this processor to Arabic, it could potentially help with other scripts
* The proposed model had significant improvement in the Muharaf dataset compared to existing methods (CER=17.6 -> 8.6)
* The model trained with the Muharaf dataset could also be generalised to other datasets

### Weaknesses
 * The authors emphasized the importance of pre-training with synthetic data however details regarding of this pre-training procedures was very limited.
* The authors mentioned the model was optimised for the Muharaf dataset, but, only provided one existing method for comparisons using this dataset

### Questions
* When you retrained the Saeed 2024 model for evaluation, did you also perform pretraining with synthetic printed data?

### Soundness
3

### Presentation
3

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
This manuscript presents a historical handwritten Arabic line recognition based on transformers. This manuscript is well written and organised. This approach is evaluated on some datasets and promising results are reported.

However, there are some problems with the presentation and experimental results.

### Strengths
This paper improves the results of the current state of the art in this field.

### Weaknesses
- This approach focuses on the extracted line to recognise the documents and this should appear in the title. It is part of a document analysis system and this may lead to errors in the related subsystems.

- It is better to explain the records in detail in the appendix. The reader does not get an idea of which datasets are historical and how the datasets differ from other document analysis datasets. Also, we do not have detailed information about the generated dataset, which should be explained in detail.

- I can see that the authors provide an analysis in the appendix to show the three intrinsic challenges. But that is not enough. They should provide a comprehensive analysis to show how effective the method is in overcoming the challenges.

- I can not see any analysis that shows the limitations of the approach. The flaws of the approach are not shown in the experimintal results.

### Questions
My comments are explained in the weaknesses section.

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
This paper describes a model for handwritten OCR of historic texts in Arabic script. The proposed model uses finetunes the TrOCR approach, first on a large synthetic and then on a small real dataset. To feed the large non-square images to the model, they are written in multiple lines when presented to the vision encoder. The model seems to obtain state-of-the-art results on 2/4 datasets and shows strong performance in cross-dataset evaluation.

### Strengths
The paper describes the approach to obtaining state-of-the art performance in a particular domain of OCR on historic datasets in Arabic script. The writing is clear and the approach seems to be easy to reproduce.

### Weaknesses
Novelty: The main novelty cited in the paper are the BlockProcessor and Arabic BBPE tokenizer. However, block processing of the images for transformer vision encoder has already been studied in several works (ex. Fuyu-8B in https://www.adept.
ai/blog/fuyu-8b or "Representing Online Handwriting for Recognition in Large Vision-Language Models", Fadeeva et al.) and the BPE tokenizer is a standard solution for VLMs. Furthermore, according to Table 3, the use of BlockProcessor actually decreases the model performance. The paper could be strengthened by offering a comparison to those approaches, or to other approaches targeted at solving a similar problem differently (ex. Pack'n'Patch in https://arxiv.org/abs/2307.06304 or Pix2Struct in https://arxiv.org/abs/2210.03347)

Beyond the aforementioned improvements, the proposed approach performs a (two-stage) fine-tuning of the base model, which does yield good performance, but may not be a significant enough contribution in itself. The paper could be strengthened by releasing the model weights or training code, which would be an additional contribution. Alternatively, perhaps open-sourcing some parts, like the synthetic data generation pipeline or dataset, could also be a good contribution. UPD: authors provided the link to their model, and I am increasing the rating based on that.

### Questions
I don't have particular questions to the authors but I believe that one way to strengthen the manuscript could be to open-source the model. UPD: authors provided the link to their model, and I am increasing the rating based on that.

### Soundness
2

### Presentation
3

### Contribution
2
