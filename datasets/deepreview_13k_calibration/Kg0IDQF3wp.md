# LegoMT2: Non-Blocking Federated Learning for Massive Multilingual Machine Translation

- Decision: Reject
- Avg Score: 4.67
- Scores: 5, 6, 3

## Abstract
What is the maximal number of languages that a single machine translation model can translate? It is a critical challenge to learn a single model for massive languages. Prior methods focus on increasing the model size and training data size. However, large models are difficult to optimize efficiently even with distributed parallel training and translation capacity can interfere among languages. To address the challenge, we propose LegoMT2,  an efficient approach with a tailored model architecture for massive multilingual neural machine translation.  LegoMT2 organizes 435 languages into 8 language-centric groups and attributes one local encoder-decoder for each group and a global encoder-decoder for all languages. LegoMT2 then trains each local and global encoder-decoder on a group-dedicated set of clients through asynchronous updating of parameters. We trained LegoMT2 on a large dataset with 25 billion sentence pairs beyond English-centric. LegoMT2 is 16.2$\times$ faster than the distributed training method for the same-size NLLB while improving the translation results by an average of 2.2 BLEU on \textit{Flores-101}~\footnote{We will release the model and code to the public.}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a novel approach called LegoMT2 for multilingual neural machine translation. It addresses the challenge of learning a single model for a large number of languages by organizing languages into groups and using a multi-way model that includes multiple encoder-decoders – each for a certain language group and another global encoder-decoder. LegoMT2 trains these encoder-decoder pairs on dedicated server clients using asynchronous updating of parameters.

### Strengths
The proposed LegoMT2 supports over 400 languages for machine translation with one single encoder-decoder model, doubling the number of NLLB while significantly faster in training.

### Weaknesses
The paper did not conduct specific verification experiments on parameter interference to demonstrate that the performance improvement of LegoMT2 over finetuned NLLB-200-1.3B indeed stems from the alleviation of parameter interference phenomena.

### Questions
1. Which of Single-FT or Single-FT + MoE in Table 3 is used for the experiments in Table 1 and Table 2? Have the translation performance of both been evaluated?
2. Have any other methods for MERGE operation of non-blocking federated learning, apart from simple averaging, been tried and evaluated?
3. How about LLMs for Multilingual Machine Translation？

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
To train a single model for massive languages is known for a challenging problem. This paper tackles the problem of how to efficiently train a neural machine translation for massive multilingual languages and proposed LegoMT2 that consists of local encoder-decoder models for language groups and a global encoder-decoder for all languages, where 435 languages are grouped into 8 language-centric category. The experimental results show the training efficiency and translation accuracy improvement, achieving 16.2x faster than the distributed training method for the same-size NLLLB and improving the translation accuracy by 2.2 BLEU on Flores-101 dataset averagely.

### Strengths
- The idea of asynchronous model parameter update that are language-group dependent is straightforward. Extensive experiments show that the proposed approach yields improvements in translation accuracy across languages. The proposed approach also helps the multi-way model to get trained faster.

### Weaknesses
 - Extensive experimental results and analyses are not fit in 9 pages. There are some description overlaps in Section 1 and 3 so the authors can move the contents from Appendix to the main pages.

### Questions
- Reg Section 3.3; how helpful is the parameter initialization with NLLB-200-1.3B? Have you ever looked into this effect, without having the NLLB initialization?
- Have you ever tried with different language grouping? 
- Why do you think Dec-Flows is better in the low-resource language groups?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes an efficient approach with a tailored model architecture for massive multilingual neural machine translation. LegoMT2
organizes 435 languages into 8 language-centric groups and attributes one local encoder-decoder for each group and a global encoder-decoder for all languages. LegoMT2 then trains each local and global encoder-decoder on a group-dedicated set of clients through asynchronous updating of parameters.

### Strengths
- federated learning used in MNMT to solve the parameter interference problem is somewhat novel
- This paper is well-written, and experiments show their improvements over baselines.

### Weaknesses
 - The authors should present the key features of the traditional federated learning methods in the related works. The authors claim an efficient approach with a tailored model architecture for massive multilingual neural machine translation. What are the key attributes of the tailored model? In other words, what is the key difference between the federated learning used in this paper compared to the traditional federated method? 
- The experimental results are somewhat less convincing. Actually, the model size of the model should be viewed as 10.4B rather than 1.6B. And the final model used in inference is the averaged version of the 8 local models. Therefore, the model should be compared to the same-size finetuned model.
- Why the model is finetuned from the pre-trained model? Why not training from scratch?

### Questions
- See above

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
