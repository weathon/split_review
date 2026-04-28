# Time2Image: A Unified Image Representation Framework for Time Series Classification

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
Time Series Classification (TSC) is a crucial and challenging task that holds significant importance across various domains, of which one of the kernel ingredients is to construct a suitable time series representation for better feature capture. However, extracting informative and robust time series representation with good generalization potential is still a challenging problem. To address this issue, we propose Time2Image, a novel image-based representation framework for TSC. At the heart of our framework is a proposed Adaptive Time Series Gaussian Mapping (ATSGM) module for robust time series encoding in 2D image structure, based on which we employ Vision Transformer (ViT) for subsequent classification tasks considering its prominent long-dependency modeling capability. Experiments were conducted on all 158 public time series datasets from UCR/UEA covering diverse domains, among which our method achieves top 1 performance in 86 datasets compared with existing State-Of-The-Art (SOTA) methods. In addition, our framework flexibly allows handling both univariate and multivariate time series with unequal length across different domains and takes inherent advantage of generalization ability due to our proposed ATSGM representation method. The source code will be publicly available soon.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work presents a method for time series feature representation that enables the use of transformers on multivariate time series classification problems in a new, performant way. This representation, Adaptive Time Series Gaussian Mapping frames the representation as a packing problem for Gaussian distributions, where all channels in a multivariate time series are represented by an individual Gaussian distribution projected onto a 16x16 patch. A single patch represents each time step in the sequence and a matrix of all the patches represents the entire sequence. Classification is then completed on the final representation with evaluation on standard benchmarks showing improvement over current methods on univariate classification and matching performance on multivariate classification.

### Strengths
Thanks to the authors for their submission: it contains useful research that shows good research practices while explaining an interesting and novel idea within multivariate time series classification. The results of this work will be informative to other researchers and are significant in improving our understanding of applying deep learning methods within time series work - a field where such applications have proved difficult. 

This paper adds to a small but growing literature around the use of Transformer-based models on multivariate time series classification. While previous large-scale benchmarks have shown that the best deep neural network-based methods use convolutional methods (ResNet, InceptionTime), this approach shows how to combine time series with Vision Transformers, which have shown improvements over ResNet in computer vision. The ATSGM framework which packs each time stamp into a patch representation that can then be fed into ViT, provides a reasonable way to represent the time series. 

Evaluation of the method against other leading approaches is thorough, using the standard UCI univariate and multivariate benchmarks. Conducting full benchmarking across all the tasks is an accomplishment which few papers in time series choose to complete and the authors should be lauded for this! The evidence provided shows that ATSGM+ViT outperforms existing methods in the univariate setting and has matching performance with the best methods in the multivariate setting.

Finally the construction of this paper was strong. The writing was well put-together with helpful diagrams elucidating the more difficult parts of the provided methods. It was easy to read and to the point.

### Weaknesses
There are two key weakness that I see in this paper:

One is the lack of comparison with other encoding and representation methods combined with transformers. There is previous work [1, 2] that uses normalized and learnable linearly projected representations of the multivariate time series with learnable positional encodings. Additional ablation studies that separate out the normalization and projection methods and compare against additional encoding types could help shine a light on the specific benefits of the ATSGM framework. One concern I have is that the improvement may be primarily due to ViT using positional embeddings and a linear projection of the flattened patches rather than due to the Gaussian projection itself and the Gaussian method may be adding more unnecessary complexity.

Second is the lack of motivation for the main method. While it is a novel method which performs well in the standardized benchmarks, it is not clear what the bounds or weaknesses of method might be. I have suggested a number in the questions below. In short: how does the Gaussian representation restrict the information available as time series scale up in size? How might the method be flexible enough to accommodate different data needs?

[1] “TST”  https://arxiv.org/pdf/2010.02803.pdf 
[2] “CropTransformer” https://arxiv.org/pdf/1905.11893.pdf 


Additional Nits: 
- Page 5: the link to the best packings of equal circles in a square returns 404. The correct link should include a ‘#’ before ‘Results’.
- Algorithm 1 does not define L anywhere in the paper though I believe it is simply equal to 196.
- Table 1: Incorrect based on the results of Table 6. In Table 6 ResNet shows 4 wins instead of 3, Time2Image shows 11 wins instead of 13, and Time2Image+ResNet shows 2 wins which should not be conflated with Time2Image+ViT in this table.
- Figure 4 should include InceptionTime

### Questions
These questions will help clarify my understanding of the paper. Some of these could benefit from additional analysis in the paper itself:

1/ What are the author’s intuitions for why Time2Image underperforms the regular ResNet? Is there something about the Gaussian representation that is particularly suited to Transformers over Convulational approaches?

2/ The results of InceptionTime seem to worse in this evaluation compared with the results of the Time Series Benchmark and Redux. Is this because T2I is better at the same categories as inception time? While the paper explains the generalization ability of T2I across domains it does not shine any light on where (if any) the gains may come from.

3/ Are the authors concerned that the method  for selecting the standard deviation parameter could allow overfitting on the benchmark datasets? Were there any held-out datasets for parameter selection that could be used for evaluation?

4/ Given the restrictions of the algorithm, in that finding a packing for the gaussian distributions in the patches will reduce the resolution of the final sample as the number of channels increases, would it make sense to evaluate the performance of the model as the number of channels increases? From quick observation on the datasets with high number of channels (Crop-7200, phalangesOutlinesCorrect-1800, Ford*-3600, ElectricDevices-8926, NonInvasive*-1800, DuckDuckGeese-1345) it seems that in this collection the T2I win-rate is lower (~50%). A similar analysis would be on sequence length. EigenWorms contains the longest sequences by an order of magnitude in the MTS set and Time2Image performance is much worse than ResNet or InceptionTime. Helping understand these performance bounds would be very useful for practical applications and understanding the generalization from the test benchmark to other evaluations. This could also help inform how the additional parameters for series normalization and patch size can be set.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a method to transform time series data into images, subsequently employing an image classifier to classify the time series data. This image representation derives from calculating the Gaussian distribution for each subsequence. The primary objective of the proposed method is to enhance time series classification.

### Strengths
Paper is very well written and structured.

### Weaknesses
Missing some related works:

A recent survey, as seen in [https://arxiv.org/pdf/2304.13029.pdf], found that InceptionTime, detailed at [https://link.springer.com/article/10.1007/s10618-020-00710-y], achieves higher accuracy than ResNet. A comparison of the proposed method with the InceptionTime model could provide further insights into the proposed method performance.

Furthermore, the paper omits some pertinent related work, such as methods based on the Fast Fourier Transform (FFT) and the Continuous Wavelet Transform (CWT).
1-Meintjes, A., Lowe, A., & Legget, M. (2018, July). Fundamental heart sound classification using the continuous wavelet transform and convolutional neural networks. In 2018 40th annual international conference of the IEEE engineering in medicine and biology society (EMBC) (pp. 409-412). IEEE.
2- Hatami, N., Gavet, Y., & Debayle, J. (2018, April). Classification of time-series images using deep convolutional neural networks. In Tenth international conference on machine vision (ICMV 2017) (Vol. 10696, pp. 242-249). SPIE.

### Questions
The core goal of transforming time series data into images is to boost accuracy. Although the authors demonstrate that their method outperforms other networks that utilize raw time series data, such as the Fully Connected Network (FCN) and ResNet, this superiority isn't primarily due to the image transformation. Instead, it's attributed to the disparity in network size. For instance, the FCN comprises 396,550 parameters, and ResNet contains 580,486 parameters. In contrast, the network featured in this paper, VIT-16, encompasses a staggering 86,859,496 parameters. Despite its immense size, VIT-16 significantly surpasses the other networks. However, given the smaller size of the other networks, they still yield commendable results. One must question the computational feasibility of transforming time series data into images and then training a model on it. Wouldn't a larger ResNet or FCN model potentially produce comparable results?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new approach to time series classification (TSC). The method, Time2Image, involves producing image-based representations of time series, and then classifying the image representations using a vision transformer (ViT). The encoding process uses a  novel technique called Adaptive Time Series Gaussian Mapping (TSGM). Time2Image is able to process both univariate and multivariate time series, and can handle time series of unequal lengths. The approach is evaluated against SOTA methods on 158 datasets from the UCR/UEA collection.

### Strengths
**Originality**  
O1. The novelty of the methods lies in the time series to image encoding process (ATSGM), which is a novel way of encoding time series. 

**Quality**  
Q1. Compared to existing time series image representation methods (GAF, MTF, and RP) using the same classifier (ViT), Time2Image is shown to have improved performance on UTS datasets (Figure 3).  
Q2. Compared to two baseline methods (FCN and ResNet), Time2Image is shown to have the best performance on UTS (Table 1 and Figure 3).  
Q3. For the MTS datasets, Time2Image wins on the most datasets when compared to five baselines (ResNet, ROCKET, CIF, HIVE-COTE, and InceptionTime).  
Q4. The results are shown to generalise across different univariate TSC domains (Table 2).  

**Clarity**  
C1. I appreciate the inclusion of Algorithm 1 to aid understanding and clarity of the method.

**Significance**  
S1. Time series image representation methods are well motivated, as powerful methods for computer vision can then be utilised. As existing approaches are behind SOTA, improving on them helps move the general family of methods forward.

### Weaknesses
 **Originality**  
O1. Further comparison to existing time series to image encoding methods is required, demonstrating the benefits of ATSGM. e.g. evaluation on MTS.   
O2. The classification method (ViT) is unchanged from its existing design, so originality only appears in the image encoding process.  

**Quality**  
Q1. **My biggest criticism of the work is the selection of SOTA baselines to compare to.** A recent study [1] identified HIVE-COTEv2 and Hydra+MultiROCKET as the new SOTA for univariate time series. These methods would be better comparisons for UTS than FCN and ResNet, and help better position the work.  
Q2. I am unsure why only FCN and ResNet were used for the UTS evaluation. The other SOTA baselines that are used for MTS can be applied to UTS as well, but are not used.

**Clarity**  
C1.  It needs to be made more clear that all time series are resized to fixed length L (which is set to 196 for the experiments). I could not see L explicitly defined.  
C2. The link in footnote 1 does not work (404 not found). Visual examples of "circle packing in a square" would aid understanding.  
C3. Figures 1 and 2 need improvement. Additional information in the caption and further explanation of the patch -> matrix reshaping (step 11 in Algorithm 1) would be helpful.  
C4. I believe the ECG results are incorrect in Table 2. ResNet has an accuracy of 94.98%, while Time2Image has an accuracy of 94.67%. However, Time2Image is highlighted as the best score. 

**Signifiance**  
S1. Due to the choice of baselines, it is difficult to determine how significant the development of Time2Image is.  
S2. Many of these datasets are imbalanced, so only evaluating with accuracy can be misleading. A further evaluation using balanced accuracy, AUROC, etc. would be beneficial.  
S3. While grouping by domain does show generalisation, it would be more insightful to analyse by dataset properties, e.g. time series length, number of classes etc. This would help identify where the method is strong and where it is weak.  
S4. In addition to providing the critical difference diagram and number of wins, it would be helpful to see the average accuracy over all datasets.

### Questions
Q1. Why were ROCKET, CIF, HIVE-COTE, and InceptionTime not evaluated for UTS?  
Q2. Other than improved performance, what are the benefits of ATSGM over existing image encoding methods? E.g. are the other methods able to deal with multivariate time series?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes adaptive time series Gaussian mapping that converts a multivariate time series into 2D images with multiple channels. ATSGM gets a datapoint at a timestamp as a input and outputs sub-patches containing an image with a circle gaussian. Sub-patches are then merged to become a patch, the input for ViT architecture.

### Strengths
1. Novel idea to convert a time series into an image to exploit recent vision architecture ViT's generalization power.
2. The method is general to various time series domains.

### Weaknesses
1. No recent TSC baselines such as TimesNet[1], just using vision architectures although the task is time series classification.
2. No justification about why Gaussian should be used to generate subpatches. 
3. Flaws in preprocessing. In preprocessing, resizing reduces the number of timestamps and can bring information loss. For example, a periodic pattern longer than the window size can vanish and a evolving pattern after a distribution shift can also be erased.

### Questions
1. Is there any specific reason for the conversion from time series to gaussian image? It is straightforward to use segmented times series as the patches to ViT.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor
