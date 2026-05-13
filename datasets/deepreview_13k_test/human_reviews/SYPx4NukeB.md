# SSL Framework for Causal Inconsistency between Structures and Representations

- Decision: Reject
- Scores: 3, 5, 6

## Abstract
The cross-pollination of deep learning and causal discovery 
  has catalyzed a burgeoning field of research, 
  seeking to elucidate causal relationships within 
  non-statistical data forms like images, videos, and text. 
  Such data, often being named `indefinite data',
  exhibit unique challenges—inconsistency between causal structure 
  and representation, which are not common in conventional data forms.
  To tackle this issue, we theoretically develop intervention 
  strategies suitable for indefinite data and derive 
  causal consistency condition (CCC). Moreover, 
  we design a self-supervised learning (SSL) framework 
  that considers interventions as  `views' and CCC 
  as a `philosophy' with two implement examples on 
  Supervised Specialized Models (SSMs) and Large Language Models 
  (LLMs), respectively. To evaluate pure inconsistency manifestations, 
  we have prepared the first high-quality causal dialogue dataset-
  \textit{Causalogue}. Evaluations are also performed 
  on three other downstream tasks. Extensive experimentation 
  has substantiated the efficacy of our methodology, 
  illuminating how CCC could potentially play an influential role 
  in various fields. Our code is available in~\href{https://anonymous.4open.science/r/ICLR_Anonymous_submission_575_new_dataset_Causalogue_and_codes/Causalogue_Dataset/Fork_I_demo.py}{url of 
  anonymous code and data}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a causally motivated self supervised learning framework. In particular, the paper focuses on indefinite data, which refers to data that requires deep networks to represent them like text, videos, images etc. The authors show that current methods do not learn consistent structure and representations from a causal perspective, while their proposed method based on causal consistency outperforms existing SOTA methods on different benchmarks

### Strengths
The idea of considering consistency between representation and structure as a way of learning causal relations in an unsupervised manner is interesting.

### Weaknesses
I feel the paper is poorly written. Without the Appendix, the technical contributions of the paper is very difficult to understand. Ideally, the paper should be complete with the Appendix dedicated to extra information that complements the contents of the paper. The experimental setup is not clearly explained which makes appreciating them difficult. More details in questions.

### Questions
1. The paper studies the inconsistency problem between causal structure and representation. However, what is structure and representation is never formally defined in the paper. I understand from Definition 1, structure refers to the graph and representation is simply the output of a deep network operating on the data, like word embeddings of text. However, the authors consider two causal models one with the representation and one with the structure, which is confusing. A concrete example with the same data, but the two different U and V causal models for the structure and the representation would go a long way in making the presentation more clear.

2. Hypothesis 2 is not clear. What does the notation E(\hat{x}_{s,m,n}) = x_{s,m,n} mean? The E operator has not been defined, is it the expectation? If so, what is the expectation over?

3. Section 2.2 is incomprehensible. What is causal consistency has not been defined so far, What is been plotted in Figure 1. The caption says it is the MSE between similarity matrices of representation and structure. What are these similarity matrices? Appendix A.3 does not give these details. What is the reconstruction loss the authors are referring to here? For example, lines 130-133, the authors say in the M > 1 or D > 1 case, the optimization of causal strength f changes to a weighted linear combination of f_m for the different M structures. However, this optimization problem has never been defined. Numerous such issues plague the readability of the paper.

4. Eq 3 is unclear. What is L_k, what is being optimized? I understand at a high level we have 2 causal models, we intervene on both of them, and then have a way of checking the consistency of the two models. But beyond this high-level details, exact specifics of how the authors carry out the interventions and check for consistency is not present in the paper. 

5. The authors propose a Causalogue dataset for causal discovery. However, it is not clear how this dataset was construcuted. The appendix gives some details. However, the authors handcraft 10 causal structures. It is not clear how GPT-4 was prompted to respect this causal structure while generating the utterances. 

I think the entire paper needs significant restructuring to make the presentation clear and allow readers to understand the main contributions and needs more details to reproduce the results.

### Soundness
2 fair

### Presentation
1 poor

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
The paper performs research on the intersection of deep learning and causal discovery. By so-called causal consistency, it proposes a self-supervised learning framework which provides potential support for the LLM. with some test results on a new dataset.

### Strengths
1. The idea is novel, and the viewpoint of consistency is important.
2. The proposed new dataset may serve the community.

### Weaknesses
1. Some definitions need to be more accurate.
2. Experimental section can be improved.

### Questions
1. The definition of "non-statistical data" forms like images, videos, and text is vague. These data still contains statistical information, and what do you mean by "non-statistical"?
2. Definition 1 (Causal Data). I still think the definition of "Indefinite Data" "Semi-definite" based on D and M only is weak. How to quantify causal consistency is still an open question. This also applies to section 2.3.
3. Def 3. The symbols looks slightly wired. 
4. Section 6. I am still puzzled that how you evaluate the "causal graph" and "structure" both. It seems that these two things basically align with the same aspect of the algorithm. Why not evaluate "variance of learning results" or ”scalability of the algorithm“？

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the author proposes a SSL framework to make the causal structure be the same as causal representation by regulating their strength set. The author further introduces a dialogue dataset which could serve as a potential benchmark.

### Strengths
1. The author showcases implementations under different frameworks. 

2. The dataset could be useful. 

3. The experimental results are promising.

### Weaknesses
1. The presentation and the readability of the paper can be improved. 

The author points out the inconsistency between causal structure and causal representation.  However, there is no formal definition of causal consistency in the paper.  In theory 1, the author gives the causal consistency condition as if it is equivalent under any intervention, these two causal models are consistent. But still, it is not a definition and there is a lack of intuition and motivation of why inconsistency is a problem to be solved. 


2. The hypothesis 2 is confusing. 

In images or text, people project the original data into latent space, where each dimension does not have to be entangled. Even in the feature space, they do not have to be entangled. The pixel one may not relate to pixel two.

### Questions
1. What is the causal inconsistency between causal representation and causal structure and why do we want to optimize it. 


2.  How do you adapt your method to other datasets where the intervention cannot be done, for example, celebA.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
