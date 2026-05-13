# PaLD: Detection of Text Partially Written by Large Language Models

- Decision: Accept
- Scores: 6, 5, 8, 6

## Abstract
Advances in large language models (LLM) have produced text that appears increasingly human-like and difficult to detect with the human eye. In order to mitigate the impact of misusing LLM-generated texts, e.g., copyright infringement, fair student assessment, fraud, and other societally harmful LLM usage, a line of work on detecting human and LLM-written text has been explored. While recent work has focused on classifying entire text samples (e.g., paragraphs) as human or LLM-written, this paper investigates a more realistic setting of mixed-text, where the text's individual segments (e.g., sentences) could each be written by either a human or an LLM. A text encountered in practical usage cannot generally be assumed to be fully human or fully LLM-written; simply predicting whether it is human or LLM-written is insufficient as it does not provide the user with full context on its origins, such as the amount of LLM-written text, or locating the LLM-written parts. Therefore, we study two relevant problems in the mixed-text setting: (i) estimating the percentage of a text that was LLM-written, and (ii) determining which segments were LLM-written. To this end, we propose Partial-LLM Detector (PaLD), a black-box method that leverages the scores of text classifiers. Experimentally, we demonstrate the effectiveness of PaLD compared to baseline methods that build on existing LLM text detectors.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors introduce PALD-PE and PALD-TI, methods that estimate the percentage of LLM-generated content in a piece of text, and an approach to identifying the LLM-generated segments, respectively. PALD-PE provides MAP estimates of the percentage of LLM-generated text, and using gaussian kernel density estimation, they provide intervals that cover the ground-truth percentage. PALD-TI runs a combinatorial search over all possible segments using a score from a text-classifier to identify the LLM-generated segments. Furthermore, a greedy version of the PALD-TI approach is introduced. The authors evaluate their approach on the Writing Prompts and Yelp Dataset.

### Strengths
•	It is one of the first papers to address the more realistic mixed-text scenario and proposes to estimate the amount of text that is machine-generated, as well as to identify the segments that are machine-generated. This is a departure from the usual machine-or-human detection. 

•	The paper includes rigorous ablations of the PALD-PE method, which greatly led credence to the observations that methods with a higher quantile slope were more useful in mix-text scenarios.

### Weaknesses
o	The fine-tuned RoBERTa baselines were trained to identify between fully human and fully-LLM texts that are larger than a single sentence in length, but then tested on individual sentences. This introduces a distribution mismatch during testing that might make the baselines weaker than they really should be. Specifically, RoBERTa's architecture is designed to process longer sequences, and training it on paragraph-level text while testing on individual sentences could lead to suboptimal performance due to the model not being exposed to the shorter text during training. This discrepancy could artificially deflate the performance of the RoBERTa baselines.

o	For DetectGPT, and FastDetectGPT, the threshold should’ve been derived from a validation set to maximize their performance at the segment level identification task. The current approach of using a fixed threshold may not be optimal for the segment-level task, as the ideal threshold could vary depending on the specific characteristics of the text segments. Without a validation set to tune the threshold, the performance of these methods may be limited.

o	In Table 3, PALD TI relies on a supervised model, whereas DetectGPT and FastDetectGPT do not so it’s unfair to compare one against the other. It would be good to have a zero-shot version of PALD. It would’ve been interesting to test them against a version of PALD-TI which relies upon an unsupervised T-score. The comparison is not entirely fair because PALD-TI leverages a supervised classifier, giving it an advantage over the unsupervised methods. A more comprehensive evaluation would include a zero-shot variant of PALD-TI, perhaps using an unsupervised T-score, to provide a more balanced comparison.

o	The datasets and testing conditions considered are not sufficient. In particular, the work could’ve also been easily evaluated on the RoFT dataset (https://arxiv.org/abs/2212.12672), and it could’ve also been built off of RAID (https://arxiv.org/abs/2405.07940) and the M4 dataset (https://github.com/mbzuai-nlp/M4), both of which include more realistic testing domains. The evaluation lacks diversity in terms of datasets and domains. The inclusion of datasets like RoFT, RAID, and M4, which offer more realistic and varied testing conditions, would strengthen the evaluation and demonstrate the generalizability of the proposed methods.

o	Only GPT-4o was used when infilling. More LLMs should’ve been considered, including non-instruction-tuned LLMs. The reliance on a single LLM for infilling limits the scope of the evaluation. Exploring other LLMs, including non-instruction-tuned models, would provide a more robust assessment of the methods' performance across different generation styles and capabilities.

•	The PALD-TI approach relies heavily on a T-Score from literature such as a trained RoBERTa model, FastDetectGPT, DetectGPT, etc. It uses them to perform a combinatorial search of 2^n – 2. A more efficient method for search that is not just greedy would make the method much stronger. The combinatorial search used in PALD-TI is computationally expensive, scaling exponentially with the number of segments. Exploring more efficient search algorithms, beyond the greedy approach, could significantly improve the method's practicality and scalability.

### Questions
•	Line 191, wrong notation? X_i instead of X?

•	Typo 297: performnace -> performance

•	What was the reason for having different fractions set for the testing split than for the training split? 

•	Any insights as to why the quantile slope of DetectGPT is smaller, but the segment accuracy is stronger than that of GhostBuster and FastDetectGPT?

•	Were PALD-TI and PALD-PE evaluated on cases where there were no machine segments? How about in cases where there are only machine segments?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces Partial-LLM Detector (PaLD), a method designed to estimate what percentage of a text is generated by an LLM and identify which specific segments are machine-generated. This approach uses black-box methods leveraging scores from text classifiers to achieve these tasks. It offers a more nuanced detection capability compared to previous methods that only classify texts as either human or machine-generated in entirety.

### Strengths
1. This method allows for a more detailed understanding of the text composition by identifying LLM-generated segments.
2. The proposed method can handle texts of mixed origin, reflecting more realistic scenarios than those handled by traditional binary classifiers.
3. Provides statistically robust methods to back its detections, including confidence intervals and likelihood measures.

### Weaknesses
1. Some of the concepts and mathematical notations need further explanation for readers' better understanding. For instance, the definition of 'robust' in the context of human-written/LLM-text detection is unclear, particularly regarding the types of input perturbations considered. The use of terms like 'Bayesian framework,' 'MAP estimation,' and 'mixture Gaussian models' without specific references makes it difficult to assess the novelty of their application in this context. Additionally, the notation $\chi$ is used without prior definition, leaving the reader to guess its meaning. The explanation of how the number of decomposed segments is determined in real applications is also lacking, and it is unclear whether the parameters $\eta$ and $\delta$ are segment-specific or global.
2. The experimental setup needs improvement. Currently, experiments are conducted on only two specific datasets, limiting the assessment of generalizability. The method's reliance on prior distributional information, specifically the assumption that each segment is either entirely human or LLM-generated, could further limit its applicability in more complex scenarios where mixed content within segments is possible. The paper does not explore the impact of mismatched segmentation, where the assumed segmentation does not align with the actual boundaries between human and LLM-generated text. Furthermore, the paper does not address the performance of the proposed method in more challenging cases, such as humans mimicking LLM style or LLMs imitating highly stylized human writing.

### Questions
1. Line 93, could you please define the term 'robust' in a human-written-/LLM-text detection problem (e.g., what types of changes, uncertainties, and unexpected perturbations in input data are considered)?
2. Lines 90-100, Bayesian framework, MAP estimation, mixture Gaussian models, and greedy policy algorithm have already been widely used in text detection or related NLP problems, please provide some references to them.
3. Line 112, '..., and x \in \chi ...' \chi needs to be defined before the first time use it (e.g., is it a set or list).
4. Line 154, how do you determine the number of decomposed segments in real applications? Is it equal to the number of sentences in a paragraph?
5. Lines 190-193, are \eta and \delta different from each segment Xi? Or they are calculated over the entire mixed-text paragraph?
6. Lines 205-206, is \epsilon a pre-defined hyperparameter? Since it determines the range of p, will the optimal \epsilon depend on the distributions P_llm and P_human, and how to choose the optimal \epsilon?
7. The example in Fig. 6 only consists of 3 sentences. If the text has more sentences, will the T-score of all the combinations be computed? Or just 2-sentence combinations will be considered?
8. Lines 324-326, a greedy algorithm is employed to approximately solve the problem and reduce complexity. Could you briefly discuss the approximation errors introduced by this algorithm and whether or not they impact detection accuracy?
9. In section 4.2, the cross-domain detection experiment is particularly intriguing, and I can somewhat understand that this test is generally more challenging compared to in-domain detection. Could you please briefly describe whether the WP and Yelp data are correlated (or consist of some similar information) before we can safely reach the conclusion?
10. The experiments are conducted on only two specific datasets, so additional validation is required to assess generalizability. I am also curious about the performance of detection in more challenging cases, such as humans mimicking the LLM style or LLM imitating highly stylized human writing. These can be mentioned in future works or current limitations.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work challenges traditional binary views of machine-generated text detection for classifying entire text samples as either human or LLM-written, and instead studies detecting texts partially written by LLMs. The experiments consist of two main parts: a) estimating the percentage of LLM-written texts; b) identifying LLM-written segments.

### Strengths
1. The problem raised by this paper is very interesting and worth studying. This makes this paper have great academic impacts.
2. This paper overall is well-written. The presentation and structure are clear and concise, with well-crafted figures and only a few typos.
3. In-depth theoretical formulation and justification of the statistical method chosen.

### Weaknesses
1. Computational complexity: As the authors have acknowledged, scaling this method over many segments could be challenging. This poses limits to its applicability. In my opinion, this is a relatively minor issue as this partial detection problem is inherently harder, and we should encourage solutions to hard problems. This should be left for future works to work on.

2. Need more robustness analysis: My main criticism is that this method lacks more sensitivity analysis regarding to segment lengths and various forms of perturbation attacks. How would it perform when there are adversarial attacks trying to undermine the detection is another main problem we should consider. I understand the paper has limited scope and cannot study everything, but I would assign a more affirmative rating had the paper dedicated a section for robustness analysis.

3. This method also requires training with regards to the specialized domain, which makes it less generalizable. Although the authors have studied cross-domain performance, the results are less convincing as only two domains have been studied, and maybe domains with more distinct writing styles have more drastic performance difference. I point it out not because I want to ask the authors to do additional experiments on new domains (although you are welcomed to!), but it’s just that I think it is that the nature of the methods makes training necessary, and this weakness cannot be easily avoided.

4. A minor point: I would suggest to have the related work section review every existing work studying partially LLM-written text detection (I’ve searched for some and did not find too many), and reduce the part on watermarking methods as they are less relevant to this paper. A literature review in this understudied area would be very helpful!

### Questions
No further questions. Overall, I like the paper and would like to give positive ratings. Although there are imperfections, I think this work is valuable, memorable, and should be encouraged.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores methods for detecting human and LLM-generated text in a mixed-text environment. A detector called PaLD is proposed, which is used for estimating the proportion of LLM-generated content in a text and determining which passages are written by LLMs.

### Strengths
The paper tackles the mixed text problem through the PaLD method, which is an innovation in current LLM detection techniques. Above all, this paper has a complete structure and provides relatively comprehensive experiments.

### Weaknesses
1. The effectiveness of this method seems contingent upon accurate segmentation of text into LLM and human-written parts. It would be helpful to explore how it performs under less ideal segmentation conditions or how it handles errors in segmentation.

2. The article mentions the performance of cross-domain detection, but just two types are involved here, which seems to be insufficient to validate the generalization ability of the model.

### Questions
1. The paper used quantitative T-score and KDE to analyze or differentiate text. It is suggested that the authors provide more detailed basis for parameter setting, such as the choice of bandwidth for KDE and how to determine the threshold of T-score.

2.  Authors provide performance metrics of the algorithm such as accuracy and coverage-accuracy trade-offs, but lacks the analysis of misclassifications (false positives and false negatives). It is recommended to explore or discuss in detail the possible causes of misclassification.

### Soundness
3

### Presentation
3

### Contribution
3
