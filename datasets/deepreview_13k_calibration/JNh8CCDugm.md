# Retrieval Information Injection for Enhanced Medical Report Generation

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 3, 3, 6

## Abstract
Automatically generating medical reports is an effective solution to the diagnostic bottleneck caused by physician shortage. Existing methods have demonstrated exemplary performance in generating high-textual-quality reports. Due to the high similarity among medical images as well as the structural and content homogeneity of medical reports, these methods often make it difficult to fully capture the semantic information in medical images. To address this issue, we propose a training-free Retrieval Information injectioN (RIN) method by simulating the process of Multidisciplinary Consultation. The essence of this method lies in fully utilizing similar reports of target images to enhance the performance of pre-trained medical report generation models. Specifically, we first retrieve images most similar to the target image from a pre-constructed image feature database. Then, the reports corresponding to these images are inputted into a report generator of the pre-trained model, obtaining the distributions of retrieved reports. RIN generates final reports by integrating prediction distributions of the pre-trained model and the average distributions of retrieved reports, thereby enhancing the accuracy and reliability of the generated report. Comprehensive experimental results demonstrate that RIN significantly enhances clinical efficacy in chest X-rays report generation task. Compared to the current state-of-the-art methods, it achieves competitive results.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this work, the authors introduce a training-free Retrieval Information injectioN (RIN) method to enhance the accuracy and effectiveness of medical report generation. Inspired by the Multidisciplinary Consultation process, where multiple experts collaboratively diagnose and analyze a patient's condition, the method retrieves similar images from a database and uses their corresponding reports as references. This method proposes an innovative decoding strategy that enhances the quality of the decoded text by injecting retrieved similar reports into the decoding process. This method has been validated through extensive experiments, demonstrating the effectiveness of both the model and the proposed specific strategies.

### Strengths
1.The proposed method is simple and straightforward, distinct from traditional contrastive decoding strategies, and its effectiveness has been demonstrated. The fact that it requires no training makes it particularly attractive.
2.The experiments are comprehensive. In addition to the state-of-the-art (SOTA) analysis, the authors conducted extensive analytical experiments, including ablation studies and evaluations of various parameters within the method.

### Weaknesses
1.Although the improvement in results is significant, there is a lack of intuitive explanation or insight into the source of this improvement. Additionally, it remains unclear whether this decode strategy can be applied to other report generation methods.
2.If space permits, I suggest moving the details of the INFORMATION INJECTION (currently at the end of the supplementary materials) into the Methods section. Additionally, the current pseudocode is not detailed enough and should be elaborated further.
3.The experimental results in Table 1 do not reach the current state-of-the-art (SOTA) level [1]. The authors could try to combine more advanced methods to verify the stability of the proposed decoding strategy.
4.In Table 3, it appears that the proposed retrieved-reports average distribution may introduce noise during the decoding process (as discussed in section 3.3), also evidenced by comparing it with the results in the full version (the last row), which included the report filter. Although it achieved significant improvement compared to the baseline (the first row), addressing such adverse effects in certain situations could further strengthen this method.
5.Does this decoding strategy heavily rely on retrieval accuracy?

### Questions
refer to the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work discusses the challenge of automatically generating medical reports to alleviate the diagnostic bottleneck caused by physician shortage. Existing methods excel at producing high-textual-quality reports. However, the high similarity among medical images and the homogeneity of medical reports' structure and content hinder the full capture of semantic information in images. To overcome this, the authors propose a training-free Retrieval Information injection (RIN) method, which enhances pre-trained medical report generation models by utilizing similar reports of target images. This approach aims to improve the accuracy and clinical efficacy of the generated reports without requiring additional training.

### Strengths
1. This work complements the results of the expert model by introducing retrieval information as additional knowledge. Unlike previous generation methods that rely only on image or text information, this method incorporates information from retrieved similar reports and injects the retrieved information into a pre-trained medical report generation model by adjusting the decoding process. This way of combining retrieval and generation is relatively novel in the field of medical report generation.

2. The structure of the manuscript is clear, logical and coherent, and the connection between the contents of each part is natural. When introducing the method, the authors elaborate on the key steps of retrieval information acquisition, injection, and adjustment of decoding process, so that the reader can clearly understand the working principle of the method.

### Weaknesses
1. In Section REPORTS RETRIEVAL, the authors claim that medical reports are often noisy, which increases the difficulty of processing and understanding model reports, making it more difficult to retrieve useful retrieval reports from medical images. This work infuses the retrieved information into the pre-trained medical report generation model, which means that the quality of report generation is affected by the retrieval effect. If the retrieved information is inaccurate or not highly relevant, then the injected retrieved information may not be effective in improving the quality of report generation, and may even have a negative impact. This work does not further explain the design and effectiveness of the retrieval method. The authors are advised to further validate the effectiveness of the retrieval model.

2. In the ablation study, as shown in Table 4, the model using Pre-trained Model Prediction Distribution, Retrieved-reports Average Distribution, and Report Filter did not achieve the best results in BLEU-2, BLEU-3, and BLEU-4. The authors are advised to further analyze the reasons for the poor performance of the model

3. The authors are advised to supplement the setting details of hyperparameters, as well as a discussion of model effects using different hyperparameters.

### Questions
1. Please further explain the differences between the proposed retrieval module and the existing report retrieval methods.
2. Report generation needs to retrieve k highly relevant reports, how to determine the value of k, and what is the specific value of k used in this paper.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents a retrieval-augmented style of generation (RAG) of radiology reports for chest X-rays. Specifically, radiology reports from similar chest X-rays are used to refine the output of a report generative model using contrastive decoding RAG approaches. A selection is then made between the refined textual output,and  the original predicted report without RAG from image directly by comparing to the retrieved reports from similar chest X-rays. 

The base report generator used is CV2DistilGPT2, the chest x-image image similarity is computed using Bio-VLP encoding, and contrastive decoding is implemented using greedy beam search of width 4. 

Overall, the paper offers limited novelty with a rehash of many of the ideas used in other contemporary papers. Added to this, the use of 14 finding label based training limits the practical utility of such methods also seen from the low F-1 scores even for these 14 findings.

### Strengths
The basic idea that RAG improves report generation has been shown for the chest X-ray report case. 
Extensive experiments (take up nearly 50% of the paper) have been performed analyzing factors they deemed important to test. Lexical, semantic and clinical efficacy scores were used for evaluation.

### Weaknesses
There are multiple methods that have taken the RAG (retrieval augmented generation) approaches to report generation that haven't been mentioned in related work nor compared to them. These include methods those that first classify the findings in chest X-rays and retrieve related reports that match in terms of findings which are more likely to be better in the selection of reports than those based purely on image features[1]-[2]. At least a comparison to these is validated. Similarly, two other papers referenced below use RAG for chest X-ray report generation which will need comparison[2]-[3]. Finally, the differences with other contrastive decoding approached to RAG may have to be discussed [3]-[4]. In general, the relation of retrieval injection to RAG will have to be explained.



### Questions
1. The terminology used to explain Figure 1 is confusing. You mention text decoders and report generators. Are there referring to the same module or two different modules. If different, this is not reflected in Figure 1. 

2. The use of image encoding features to retrieve similar images needs to be evaluated to see the type of reports retrieved. What is the ratio of overlap of findings of such retrieved reports with the ground truth reports associated with these chest X-rays. Since MIMIC dataset is used, all the chest X-ray images (train-test-validate) should have ground truth reports.

3. Line 296 - Average F-1 score should be based on match to ground truth. Is that what is meant in line 296 or F-1 score is computed relative to which report?

4. Steps 1-6 described in Figure 1 are not very clear. Is image information used only in step 3 or also in step 5?

5. Instead of using Bio-VLP for image-to-image matching why not use it directly to retrieve radiology reports as done in earlier papers with CLIP-based retrieval (https://proceedings.mlr.press/v158/endo21a/endo21a.pdf) since Bio-VLP is a multimodal model?

6. The use of the term 'distribution' to refer to the generated output from report generator is confusing. Are multiple reports coming out in one step from the report generator?

7. Were the results from CheXBert freshly generated for the datasets by the authors or a reuse of numbers quoted from previous work since the ChexBert using the Allen NLP has some dependencies on older CUDA libraries.

### Soundness
2

### Presentation
1

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
This paper presents a novel method called Retrieval Information injection (RIN) aimed at enhancing the accuracy and efficacy of automatically generated medical reports. RIN involves retrieving similar images from a pre-constructed database and integrating corresponding report information with the predictions of a pre-trained model. By simulating the process of Multidisciplinary Consultation, the proposed method explores the issues related to cross-modal consistency between medical images and reports, showing competitive clinical efficacy and textual quality (evaluated via CE metrics and NLG metrics).

### Strengths
The paper is well-written and insightful. Extensive results demonstrate that RIN improves clinical efficacy in generating reports for chest X-rays, which provides a practical solution to the diagnostic bottleneck caused by physician shortages.

### Weaknesses
Despite the paper's clarity, several imprecise arguments and overstatements necessitate revision and clarification:
* The effectiveness of the retrieval process depends heavily on the quality and diversity of the pre-constructed image feature database, which might limit the method's applicability in poorly-documented medical fields.
* The implementation of a report filter in the workflow does not significantly improve the situation where false positive information still exists.
* The paper does not extensively explore the impact of errors in the retrieval process itself as a comparison.

### Questions
* Has the method been tested on modalities other than chest X-rays, such as MRIs or CT scans, to assess its adaptability and effectiveness?
* Since medical images are highly similar as mentioned in the paper, is it possible for the workflow to retrieve images that are similar but have distinct symptoms, leading to inaccurate diagnosis?

### Soundness
2

### Presentation
3

### Contribution
2
