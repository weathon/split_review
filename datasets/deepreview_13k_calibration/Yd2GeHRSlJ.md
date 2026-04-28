# Open-Set Domain Adaptation Under Background Distribution Shift: Challenges and A Provably Efficient Solution

- Decision: Reject
- Avg Score: 4.60
- Scores: 5, 5, 3, 5, 5

## Abstract
In Open-Set Domain Adaptation (OSDA) we wish to perform classification in a target domain which contains a novel class along with $k$ non-novel classes. This work formally studies OSDA under the assumption that classes are separable, and the supports of source and target domains coincide, while other aspects of the distribution may change. We term such a distribution shift as background shift. 
We develop a simple and scalable OSDA method that attains robustness to background shift and is guaranteed to solve the problem, while showing that it cannot be solved under weaker conditions for OSDA studied in the past, particularly in the presence of covariate shift. We formally define the realistic assumptions of background shift within the scope of OSDA problem that the previous literature has either overlooked or not explicitly addressed. In a thorough empirical evaluation on both image and text data, we observe that existing OSDA methods are not robust to the distribution shifts we consider.
Our proposed solution jointly learns representations via concurrently learning to classify known categories and detect novel ones using methods with formal guarantees. The results demonstrate that optimizing these two objectives in unison leads to mutual performance improvements contrary to what might be expected when objectives are considered independently. Our rigorous empirical study also examines how OSDA performance under distribution shift is affected by parameters of the problem such as the novel class size. 
Taken together, our observations emphasize the importance of formalizing assumptions under which OSDA methods operate and to develop appropriate methodology that is capable of scaling with large datasets and models for different scenarios of OSDA.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses a gap in Open-Set Domain Adaptation (OSDA): handling both novel class detection and distribution shifts in known classes ("background shift"). The authors propose a scalable solution combining principled novelty detection with shared representation learning, demonstrating strong results across multiple domains.

### Strengths
- identification and formalization of understudied OSDA challenges
- Specific attention to challenging real-world scenarios like low-proportion novel classes

### Weaknesses
 - All datasets are semi-synthetic. It would be interesting if authors can show results on practical datasets. 
- While the problem addressed is quite interesting theoretically, practical relevance is unclear. As mentioned above, the paper may benefit from including results on datasets which inherently satisfy the problem discussed in the paper
- The paper may also benefit from discussing how using stronger CLIP models alters the behavior of the baselines and the proposed method.

### Questions
NA

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
3

### Summary
This paper addresses Open-Set Domain Adaptation under a specific scenario referred to as "background shift," where known classes have partial overlap between source and target domains, while novel classes remain distinct. The authors introduce CoLOR (Constrained Learning for Open-set Recognition), a multitask learning framework that applies constraints on target data to reduce bias in the feature extractor. The key insight is that traditional partial domain alignment methods struggle when source-private classes significantly outnumber common classes. CoLOR addresses this by jointly optimizing for closed-set classification and novel class detection through a constrained learning approach. The method is evaluated comprehensively across three datasets (CIFAR100, SUN397, Amazon Reviews), demonstrating improved performance, particularly in scenarios with low novel class ratios. The theoretical contributions include a formal analysis of necessary/sufficient conditions for OSDA under background shift.

### Strengths
- Strong theoretical foundation with formal analysis of background shift in OSDA, including necessary/sufficient conditions and limitations of existing approaches.
- Comprehensive empirical evaluation across multiple modalities (images and text) and varying novel class ratios.

### Weaknesses
 - While background shift is justified with potential applications in medical imaging (e.g., identifying known and novel tumor cells), this application is not addressed in the experiments. Including other real-world cases would strengthen the relevance of background shift beyond this initial mention.

- The abstract could be improved by defining “background shift” and avoiding vague phrases like "principled methods."

- The claim “we observe that existing OSDA methods are not robust to the distribution shifts we consider” is strong, but the baselines used are limited. Adding recent OSDA and UniDA baselines would support this claim.
Suggested OSDA baselines: Adjustment and Alignment for OSDA [1], Open-Set Domain Adaptation for Semantic Segmentation [2], Source-Free Progressive Graph Learning for OSDA [3].
Suggested UniDA baselines: Compressive Attention Matching for UniDA [4], Classifiers of Prototypes and Reciprocal Points for UniDA [5].

- The paper assumes “notable separability” between known and novel classes, which might be feasible for images or text using pretrained models like ViT-CLIP. However, this separability may not hold in fields like medical imaging, where pretrained models aren’t available.

- The authors should clarify how they determine the number of classes (k) for any additional classifier head and discuss the impact of varying k.

- In Table 2, BODA outperforms CoLOR on CIFAR100, but this result isn’t highlighted in bold.

- In Table 3, only one baseline is used, which is outdated. The chosen method isn’t clear either, given the three references listed (‘These baselines are domain discriminator (DD), Elkan & Noto (2008); du Plessis et al. (2014); Garg et al. (2021)’).

- Is the “OSCR” metric referring to the commonly used H-score in open-set papers?

- The method is sensitive to hyperparameters like the FPR; details on selecting FPR and setting the threshold  β for optimization should be included.

-  The code is missing .

### Questions
See Weaknesses

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work suggests a new Open-Set Domain Adaptation (OSDA) scenario, “background shift” which is a distribution shift with overlapping supports between source and target distributions exists within the known classes. Also, the existing OSDA methods are experimentally shown to be insufficient in addressing background shifts. To handling this new scenario, this work proposes a new method dubbed as CoLOR. Experimental results show the effectiveness of the proposed method.

### Strengths
1. Introducing background shift in OSDA community is interesting and novel.

2. Proposed method is based on theoretical evidence.

3. Experiments are well structured to verify the effectiveness of background shift.

### Weaknesses
1. This work has limited novelty and originality since it relies heavily on [1], which provide theoretical analysis of OOD novel category detection. Lemma 1 and Theorem 1 in this manuscript are quite similar claim with Proposition 3.1 and Theorem 4.3 in [1] though they focus different task. Furthermore, it is unclear that Theorem 1 in this manuscript can be easily extended on OSDA since there is no proof in the manuscript and supplementary material. Specifically, Lemma 1, while introducing an additional assumption of strong positivity, appears to be a weaker result than Proposition 3.1 in [1], which does not require this assumption and thus encompasses the conditions of Lemma 1. Therefore, Lemma 1 seems redundant, and its proof as a corollary of Proposition 3.1 should be explored. The authors claim Theorem 1 is a restatement of Theorem 4.3 in [1], further diminishing the theoretical contribution. The core novelty of Lemma 1 is questionable, and the extension of Theorem 1 to OSDA lacks explicit proof, raising concerns about the overall theoretical contribution.

2. Proposed method is rather incremental. I think it is concatenate the cross-entropy loss on [1]. The proposed loss function appears to be a simple combination of cross-entropy loss for known classes and a loss for novel class detection, similar to [1]. The method does not introduce a fundamentally new approach to learning, and it is unclear how the proposed method addresses the computational challenges of scaling to high-dimensional data and large models, which is a limitation of the approach in [1].

3. Baselines for performance comparison is insufficient and outdated. I think several recent UDA methods should be included. The experimental evaluation lacks a comprehensive comparison with state-of-the-art methods. The authors should include recent UDA methods, as the problem setting shares similarities with OSDA. The baselines from PULSE [2], such as UAN, DANCE, STA, and CMU, are also missing, which are essential for a thorough evaluation. Furthermore, the paper does not explore the performance of the proposed method across different modalities, particularly in the table modality, which was addressed in PULSE [2].

### Questions
1. Why did the authors define background shift not as a distinction between support of $P_{T,[k]}$ and $P_S$ i.e. $Supp(P_{T,[k]}) \neq Supp(P_S)$ but rather as $Supp(P_{T,[k]}) \subseteq Supp(P_S)$???? 

2. Could you elaborate on the differences in assumptions and results between Theorem 1 in this manuscript and Theorem 4.3 in [1]? If there are differences, please explain how these differences are reflected in the proof process of Theorem 1.

3. I am curious whether the recent UDA methods demonstrate low performance even when applied in OSDA with background shift.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work sets out to address the open set domain adaptation (OSDA) problem under so-called background shifts. This problem amounts to solving the domain adaptation problem while also identifying datapoints which are novel classes which were not seen in the source domain. Domain adaptation is the problem of finding a model which performs well in a target domain when it has been trained on labeled data from some source domain and unlabeled data from the target domain. Background shifts are defined as any distribution shift between source and target domains which retains overlapping support between source and target domain distributions with the non-novel label set. 

The authors show that strong positivity and overlapping support is not a sufficient condition to ensure better than random performance. 
The work proposes a model partly based on previous work in OOD detection. The work proposes to use this method to detect the novel classes while at the same time learning to do the classification. The architecture of the model has a shared base structure which is used for both the detection and classification heads.

The model is then compared on image and text dataset benchmark against several baselines. It performs favourably on these tasks compared to baselines, especially when the ratio of novel class datapoints is low.

### Strengths
- The setting of OSDA is both an important and challenging area  

- The paper uses an OOD method in combination with learning a classifier to do OSDA which is a reasonable approach which seems to work well

- Method performs well on chosen datasets compared to baselines

### Weaknesses
 - The introduction and related work together makes up ~3 pages which is a substantial part of the paper.

- It seems rather inefficient to solve the problem for a large number of possible values of $\alpha$. How does this compare to the other baseline methods?


- The experimental details are somewhat unclear. Some things are not clearly stated. 
    * How many repetitions of experiments were done?
    * How is the separability of the novel classes ensured? 

- Why does the amount of 'wins' not tally up to the total number of repetitions? I assume that this is what the Wins column in table 2 means, since I cannot find it explained in the text. Does this mean that the models tie in performance in some runs? 

- Not clear to me how the choice of $\beta$ threshold impacts the results. 

Typos and other comments:

- Unclear what the bolding in table 3b means, it almost seems random.

- Figure 2 is small and admits a large amount of white space for seemingly little reason.

- The bullet points headers for the paragraphs in the introduction seem distracting to me


line 283: largrangian
line 355: Expertiments
line 385: table table
line 480: Refer 5,6,7,10 in for further results. - Supposed to be reference to some section here?
line 481: AUORC

### Questions
See questions posed in the above section.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper investigates Open-Set Domain Adaptation (OSDA) under a background distribution shift. In OSDA, the objective is to classify known categories while detecting novel, previously unobserved classes in the target domain. This study addresses background shifts, where the distribution of known classes in source and target domains differs. The authors present a scalable method named CoLOR (Constrained Learning for Open-Set Recognition) to robustly classify known classes and detect novel ones under this shift. They demonstrate that CoLOR outperforms existing baselines by jointly learning representations for both classification and novelty detection.

### Strengths
1. This paper addresses the overlooked issue of background distribution shifts in OSDA, relevant for dynamic applications like medical imaging and autonomous systems.

2. Extensive experiments across diverse datasets validate CoLOR's performance and robustness against strong baselines.

3. The paper is well-organized, with clear explanations, detailed methodology, and effective visual aids for complex concepts.

### Weaknesses
1. The separability assumption (Assumption 1) is central to CoLOR’s effectiveness. Could you discuss scenarios where this assumption might not hold in practical applications? How would CoLOR perform if the separability or background shift assumptions were relaxed or violated?

2. The writing quality could be enhanced by ensuring consistency in formatting, particularly in the Related Works section, where the subheading styles appear inconsistent. Standardizing these subheading formats would improve the paper’s overall readability and professionalism.

### Questions
Please see Weaknesses above.

### Soundness
3

### Presentation
2

### Contribution
3
