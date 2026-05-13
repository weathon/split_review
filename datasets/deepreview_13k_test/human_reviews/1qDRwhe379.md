# Refining Corpora from a Model Calibration Perspective for Chinese Spelling Correction

- Decision: Reject
- Scores: 6, 6, 5

## Abstract
Chinese Spelling Correction (CSC) commonly lacks large-scale high-quality corpora, due to the labor-intensive labeling of spelling errors in real-life human writing or typing scenarios. Two data augmentation methods are widely adopted: (1) \textit{Random Replacement} with the guidance of confusion sets and (2) \textit{OCR/ASR-based Generation} that simulates character misusing. However, both methods inevitably introduce noisy data (e.g., false spelling errors), potentially leading to over-correction. By carefully analyzing the two types of corpora, we find that though the latter achieves more robust generalization performance, the former yields better-calibrated CSC models. We then provide a theoretical analysis of this empirical observation, based on which a corpus refining strategy is proposed. Specifically, OCR/ASR-based data samples are fed into a well-calibrated CSC model trained on random replacement-based corpora and then filtered based on prediction confidence. By learning a simple BERT-based model on the refined OCR/ASR-based corpus, we set up impressive state-of-the-art performance on three widely-used benchmarks, while significantly alleviating over-correction (e.g., lowering false positive predictions).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper gives a clear picture of 2 mainstream techniques to create mis-spelling dataset for chinese characters, Random Replacement and OCR/ASR. However, each approach of corruption brings its own inherent bias that may lead to problems in training. For example, OCR/ASR way of corrupting characters gives very calibrated scores, as shown as Figure-1, while the Models trained on Random Replacement data has less calibration issues. The authors propose a recipe to train on both Random Replacement and OCR/ASR data, but with some scheduling and post-process steps, which include prioritize Random Replacement training to learn calibration, and then do OCR/ASR training to improve over-all performance. 

There is a typo in the Table-2 SIGHAN15, but overall, the proposed method achieves SOTA performance on benchmark datasets.

### Strengths
The strength of the paper lies in its clear presentation of the problem, robust experiment designs, and strong performance on benchmark datasets. The problem of calibration vs overall performance is laid out as the bottleneck, and the authors offer a recipe to combine the two methods. 

First, the paper is well-written.

The illustration of the problem is made clear by Figure-1, where Calibration on both models are weak, but the OCR/ASR is much worse. However, the overall performance shows OCR methods is better across-the-board. 

The final results is validated on 3 benchmark Chinese spelling datasets, with 6 existing spelling model benchmarks, and 3 Generative AI benchmarks. The performance gain is significant. 

Lastly, the issue of mis-spelling in Chinese is a practical and important problem. It will be a waste of resources to rely on a 10 billion parameter ChatGPT to do it on everyday use cases, though the paper shows not so great Zero-Shot performance by ChatGPT.

### Weaknesses
The authors made direct reference of "Random Replacement" and "OCR/ASR" methods as the two mainstream way to construct mis-spelling datasets. The fact that we can train on data created by both methods isn't a source of novelty. 

The paper uses a model trained on Random Replacement to filter/"refine" OCR/ASR corpus is kind of interesting, but may be a step that introduces another layer of inductive bias. 

The author mentions that "We use the optimal threshold that achieves the best performance on each dataset." This is not a good idea, because it runs the risk of leaking test data to model developers. The final performance gain should be reported on 1 uniform threshold(might be proportion if different datasets have different absolute values) determined by running ablation on a separated dev-set . In that case, we can be sure that whatever gain that we see in Table-2 is from the novel method.

### Questions
1. Are there other works that combine Random Replacement and OCR methods in training? 

2. Is there a leak of test-set when determining the threshold for filtering? 

3. Is there a reason to choose different threshold for each dataset? Can you report Table-2 using one uniform cut-off, and report the dev-set/test-set performance separately?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper centers its attention on addressing the calibration problem within the realm of Chinese Spelling Check (CSC). Due to the lack of large corpus in the field of CSC, two data augmentation methods of random replacement and OCR/ASR-based generation is proposed to generate large-scale corpora. These methods introduce noise into the data, which subsequently causes over-correction. The authors analyze the calibration of the CSC models trained in the two corpora, and observe that random replacement results in better-calibrated CSC models. The authors then propose a corpus refining strategy to filter OCR/ASR-based data. Utilizing a BERT-based model trained on this refined corpus, the authors achieve commendable performance on CSC benchmarks, affirming the efficacy of the proposed method in mitigating over-correction.

### Strengths
1.	The paper makes a valuable contribution by highlighting the differences in generalization performance between OCR/ASR-based and random replacement data augmentation techniques. This insight has the potential to inspire further research in the CSC domain.
2.	The paper proposes a novel data filtering method after carefully observation of the two data augmentations in CSC. The method effectively filters the noisy examples, and the model trained on the refined corpus can achieve impressive performance.
3.	The motivation behind the research is clearly justified and based on empirical observations. The proposed methodology is presented in a comprehensible manner, making it suitable for adaptation to other models in the field.

### Weaknesses
1.	The statistical data presented in Table 2 appears to contain an error, as the reported F1 score for the SIGHAN 15 dataset does not align with the provided precision and recall values. This discrepancy requires clarification.
2.	Missing citations of ChatGLM. It remains unknown that which version of ChatGLM (ChatGLM or ChatGLM2?) is used in this paper. A more comprehensive citation and elaboration on the fine-tuning procedure are needed.
3.	Excessive white space around tables, maybe the layout can be adjusted.

### Questions
1.	How do you design the prompt of the LLMs to generate the corrected results? Have you tried other templates to generate?
2.	The issue of varying output lengths generated by LLMs is mentioned. Could you provide additional information on the strategies employed to mitigate this problem and ensure consistent results?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes an amazingly simple formula (eq 7) for combining observations with pseudo-labels.  The proposed method is shown to be effective for Chinese spelling correction.

### Strengths
The method is amazingly simple, and appears to be effective.

### Weaknesses
The approach seems too good to be true.  

There is a huge literature on pseudo-labels, self-training, co-training, EM, etc.  These methods have many applications that go way beyond Chinese spelling correction.

Here are a few highly cited examples:

https://arxiv.org/pdf/1905.02249.pdf 
https://arxiv.org/pdf/1908.02983.pdf
https://www.cs.cmu.edu/~avrim/Papers/cotrain.pdf

There are a number of baselines in table 4, but I found it difficult to understand what each of them do.  I wonder if the description of the method could be shortened in order to make more space available for related work and baselines.

Many readers may not appreciate the challenges in spelling correction for Chinese.  I might start with a discussion like Jurafsky's book (https://web.stanford.edu/~jurafsky/slp3/B.pdf), where they have a language model and a channel model.  You assume errors are just one character for one.  Chinese may be simpler than English in that respect.

As for the channel model, I'm surprised that you have just two models in mind: (1) random and (2) similar in OCR space.  I might have thought of some others like (3) similar in pinyin space, (4) dependencies involving dialects, (5) dependencies involving input methods (6) similar in distribution.  

It is well known that spelling correction depends a lot on the context.  We should expect to see very different errors depending on the keyboard.  Typos are different when the user is on a laptop or a phone.  Within phones, there are different keyboards.

The method of estimating the channel model is somewhat similar to the proposed method here.  They used a boot strapping method where they started with a very simple method to find typos that had just one reasonable correction.  They found  enough of those that they could then estimate confusion matrices.  That probably wouldn't work for Chinese, but it isn't that different from your proposal of training on cases where the probability of the correction is reasonably high.

### Questions
Can you generalize your work so the paper could be of interest to a larger community of people interested in pseudo-labels, self-training, co-training, etc.?

Can you say more about the baselines?

Can you say more about how spelling correction is different in Chinese from spelling correction is other languages?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
