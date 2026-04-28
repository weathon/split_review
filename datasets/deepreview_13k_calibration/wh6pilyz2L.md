# Chronicling Germany: An Annotated Historical Newspaper Dataset

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
The correct detection of dense article layout and the recognition of characters in historical newspaper pages remains a challenging requirement for Natural Language Processing (NLP) and machine learning applications on historical newspapers in the field of digital history. Digital newspaper portals for historic Germany typically provide Optical Character Recognition (OCR) text, albeit of varying quality. Unfortunately, layout information is often missing, limiting this rich source’s scope. Our dataset is designed to enable the training of layout and OCR models for historic German-language newspapers. The Chronicling Germany dataset contains 693 annotated historical newspaper pages from the time period between 1852 and 1924. The paper presents a processing pipeline and establishes baseline results on in- and out-of-domain test data using this pipeline. Both our dataset and the corresponding baseline code are freely available online. This work creates a starting point for future research in the field of digital history and historic German language newspaper processing. Furthermore, it provides the opportunity to study a low-resource task in computer vision.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents the Chronicling Germany dataset. It consists in an annotated dataset of historical newspapers in German language. The dataset has been constructed after 1,500 hours of human annotation of the layout components. It consists of 693 pages. The dataset also includes 1,900 individually annotated advertisements. According to the authors, it the largest fully annotated collection of historic German newspaper pages. The motivation of creating this dataset is that the problem of historical newspapers understanding lacks of enough data, in particular in some languages like German. The newspapers of the dataset have some singular features. Among others, the particular use of the Fraktur font, the presence of some characters and combinations, and the dense layout.
In addition to the dataset, the paper presents a  processing pipeline for layout analysis and text recognition, and experimentally evaluates the pipeline on in- and out-of-domain test data.

### Strengths
A useful dataset for the community of digital humanities, covering a gap of low resources data. The dataset has been rigorously constructed, with layout annotations. In addition to the language, the documents in the dataset have some particularities that make it interesting to tackle language-independent document layout analysis and recognition problems.

The complementary pipeline processing that is presented is a good way to illustrate the value of the dataset, comparing the processing with other datasets.

### Weaknesses
Annotated data is important for the scientific community. But presenting a new dataset in a conference requires a solid justification on how useful is this dataset in contributing in the progress of the state of the art in the main problems addressed by the community. In this case, an annotated historical newspaper dataset is not in the mainstream of the representation learning community nor the scope of the conference. Its interest is addressed to a marginal audience of the representation learning community.

Comparison with the pipeline developed by Dell et al. (2024) analyzed in table 3. It is not clear to me if there is a crossfold validation, i.e. if the  proposed pipeline is tested with the American Stories dataset, as well as the Dell et al. pipeline is tested on the proposed German dataset. It would be good to have different datasets and different methods for the comparison.

### Questions
I believe that the contribution of this dataset is interesting, however as indicated above, it is addressed to a narrow audience, considering the scope of the conference. I am open to be persuaded on the relevance of this contribution in the context of the representation learning area. Beyond the interest in the problem of historical document layout analysis and recognition, from a wider perspective, authors should identify other points that make this dataset interesting for a larger audience.

Comparison with the pipeline developed by Dell et al. (2024) analyzed in table 3. It is not clear to me if there is a crossfold validation, i.e. if the  proposed pipeline is tested with the American Stories dataset, as well as the Dell et al. pipeline is tested on the proposed German dataset. It would be good to have different datasets and different methods for the comparison.

======================== AFTER THE REBUTTAL

After interacting with the authors, and looking at the other reviewers' revisions, I will keep the score of the first review. I thank the authors for their clarifying responses, and the effort to consider the comments. Authors provided interesting new material, and I encourage them to include in a potential revised version of the paper.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents a new dataset called "Chronicling Germany", consisting of 693 annotated historical German newspaper pages from 1852 to 1924. The dataset includes layout annotations and ground truth text transcriptions. The authors establish baseline results for layout detection, text line recognition, and OCR tasks using the dataset. They also test generalization on an out-of-distribution test set.

### Strengths
This paper presents a new historical German newspaper dataset, providing layout information and text line annotations, and also offers some baselines for layout detection and OCR tasks.

### Weaknesses
1. The novelty and contribution of this paper is limited. The main contribution of this paper is the historical German newspaper dataset itself. However, compared to existing datasets [1][2][3], this dataset does not have significant uniqueness in dataset size and diversity.
[1] Christian Clausner, Christos Papadopoulos, Stefan Pletschacher, and Apostolos Antonacopoulos.
The enp image and ground truth dataset of historical newspapers. In 2015 13th International
Conference on Document Analysis and Recognition (ICDAR), pp. 931–935. IEEE, 2015.
[2] UB-Mannheim. Ground truth for neue zürcher zeitung black letter period. https://github.
com/UB-Mannheim/NZZ-black-letter-ground-truth, 2023a.
[3] UB-Mannheim. reichsanzeiger gt. https://github.com/UB-Mannheim/reichsanzeiger-gt/, 2023b.

2. Lack of quantitative comparison with existing datasets, which fails to show the superiority of the Chronicling Germany dataset.

3. Lack of detailed assessment of the annotation quality, such as the review of annotation consistency.

4. Section 5 does not provide detailed results of testing on OOD data, which is insufficient to reflect the generalizability of the pipeline.

5. The paper incorrectly used the ICLR 2024 template instead of the ICLR 2025 one.

### Questions
1. In comparison to other German historical newspaper datasets, how does the quantitative aspects of your dataset fare in terms of size, annotation quality, and diversity?

2. Have the authros explored employing more advanced baseline methods for your tasks?

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
5

### Summary
This paper addresses the challenges of article layout detection and text recognition in historical German newspaper pages. The authors present the "Chronicling Germany" dataset, containing 693 annotated pages from 1852 to 1924, and establish a baseline pipeline for layout detection and OCR tasks. The authors aim to address the challenges of article layout detection and text recognition in historical German newspaper pages, which are essential for NLP and machine learning in digital history. They validate the model's performance on an out-of-distribution set of 112 pages from 1785-1866. Both the dataset and the baseline code are publicly available.

### Strengths
The paper makes a significant contribution by providing a new, large, and annotated dataset of 693 high-resolution historical newspaper pages in German Fraktur, addressing a crucial gap in resources for processing German-language historical documents.

### Weaknesses
The paper does not cite significant existing projects that contributed to newspaper recognition:
- Newseye  https://www.newseye.eu/open-science/research-datasets/
- Impresso  https://impresso-project.ch/outputs/datasets/

While the OCR-D project, which develops advanced tools for processing German historical documents https://ocr-d.de/en/, is mentioned in the annex, it should be highlighted in the main text

The study does not leverage high-performance OCR systems such as Pero-OCR https://pero-ocr.fit.vutbr.cz/, which could have enhanced baseline OCR results. This choice limits the impact of the paper’s findings, as more modern and effective systems are overlooked.

The paper’s reliance on an OCR system that requires baseline detection is questionable. These systems are typically designed for non-horizontal or curved text, which is rare in newspaper layouts. A retrained OCR model, especially one leveraging pre-existing models on platforms like HuggingFace https://huggingface.co/Teklia/pylaia-newseye-austrian , would likely have been more suitable.

The use of a relatively older UNet model for layout detection is debatable, given that more recent and effective models like YOLO-based architectures outperform UNet in similar tasks. Table 3's comparison, which references Dell et al., highlights these limitations, suggesting the paper's choice of model may not be optimal. As a result, the evaluation of layout analysis show poor generalization capabilities, as reflected in Table 3.

The full evaluation of the pipeline is limited; the paper only reports a Character Error Rate of 6% without providing further details. Furthermore, article separation is not assessed, making the results appear preliminary and potentially incomplete. Comprehensive evaluation metrics are needed for a stronger validation of the approach.

The legend for Table 3 lacks clarity, especially regarding what is meant by "F1 Score in distribution"

### Questions
No specific question.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents an annotated historical newspaper dataset that was written in German between the 19 and 20th centuries.

The dataset contains 693 pages where each page is manually labelled with both transcriptions of the text and layout elements, such as background, table, etc. 

The authors also provided baseline methods assess the layout segmentation, OCR recognition accuracies as well as the performance of the full pipeline.

The authors hope that researchers could build upon the Chronicling Germany dataset to improve historical newspaper processing methods.

### Strengths
* Chronicling Germany dataset introduces OCR as well as polygon layout analysis problem for historical newspaper scans
* Compared to Dell 2024, Chronicling Germany appears to have much more complex layouts. This could introduce a new line of problems in historic document analysis 
* The paper is well written and easy to follow

### Weaknesses
 * The authors claim that modern human readers will struggle reading the contents of Chronicling Germany however, only provided examples of font differences. As layout analysis is also the primary focus of this dataset, it will be nice if the authors could also focus more on the difficulties for modern readers to understand the layout differences.
* The authors did not provide information regarding the image sizes or DPI. This could help researchers evaluate the usefulness of the dataset.
* The benchmark methods doesn’t seem very well justified. Have you explored how existing pipelines trained on modern newspaper perform on your dataset? 
* There is no information about the legibility of the data
* As the authors mentioned that comprehending the pages is not trivial for modern German readers, why is the reading order within scope of this dataset?
* Follow up: how was the reading order automatically assigned and evaluated to have “satisfactory results”?

### Questions
* As the authors mentioned that comprehending the pages is not trivial for modern German readers, why is the reading order within scope of this dataset?
* Follow up: how was the reading order automatically assigned and evaluated to have “satisfactory results”?

### Soundness
3

### Presentation
3

### Contribution
2
