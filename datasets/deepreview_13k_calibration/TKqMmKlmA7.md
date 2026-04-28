# Modulate Your Spectrum in Self-Supervised Learning

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Whitening loss offers a theoretical guarantee against feature collapse in self-supervised learning (SSL) with joint embedding architectures. Typically, it involves a hard whitening approach, transforming the embedding and applying loss to the whitened output. In this work, we introduce Spectral Transformation (ST), a framework to modulate the spectrum of embedding and to seek for functions beyond whitening that can avoid dimensional collapse. We show that whitening is a special instance of ST by definition, and our empirical investigations unveil other ST instances capable of preventing collapse. Additionally, we propose a novel ST instance named IterNorm with trace loss (INTL). Theoretical analysis confirms INTL's efficacy in preventing collapse and modulating the spectrum of embedding toward equal-eigenvalues during optimization. Our experiments on ImageNet classification and COCO object detection demonstrate INTL's potential in learning superior representations. The code is available at \textcolor[rgb]{0.33,0.33,1.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a new approach, Spectral Transformation (ST), for self-supervised learning, and proposes a new training algorithm named IterNorm with trace loss (INTL). The basic idea of the paper is to balance the spectrum of the covariance matrices for the learned features which is often ill-posed. Theoretical and empirical results are provided as well for demonstrating the performance.

### Strengths
Clear writing with many experimental results.

### Weaknesses
To me, I do not see any obvious weakness of the proposed approach. Motivated by the whitening, the paper presents a nice and logical development of the approach. However, I do not see a very strong point neither that can make this paper stand out compared with the literature. I suggested the authors to further emphasize the key contributions: What really makes your approach better than others such as MoCo and SimCLR? How about computational speed (this seems not to be discussed in both paper and appendix)?

I’d like to increase my rate if the authors can convince me at this point.

### Questions
see my comment

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a new self-supervised learning framework called spectral transformation (ST) to modulate the spectrum of embedding to avoid dimensional collapse. To be specific, they introduced a novel ST instance named IterNorm with trace loss (INTL). Theoretically, this paper proved that INTL can modulate the spectrum of embeddings toward equal eigenvalues and prevent dimensional collapse. Empirically, the authors showed that INTL can obtain state-of-the-art performance for SSL on real-world datasets.

### Strengths
1. The dimensional collapse is an important problem in contrastive learning and the analysis in this paper is insightful.
2. The theoretical analysis and empirical results cooperate well. The improvements on real-world datasets are significant, especially in transfer learning tasks.

### Weaknesses
1. As analyzed in this paper, both whitening methods and INTL are instances of spectral transformations. However, it seems that INTL outperforms whitening in every task. So what are the disadvantages of whitening methods? It would be better to provide more theoretical and empirical comparisons between them.
2. The motivation behind the trace loss is a little confusing. Is it possible to provide a more detailed discussion?
3. It seems that INTL shows superior performance in 5-nn accuracy than linear probing accuracy. Are there any intuitive explanations for that?
4. There are some typos. For example, in p.4, ‘Eqn. 13 can be viewed as an optimization problem over …’ should be replaced with ‘Eqn.6 …’.

### Questions
see my comments above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- The authors propose a framework referred to as Spectral Transformation (ST) to modulate the spectrum of embedding and to seek functions beyond whitening that can avoid dimensional collapse.
- Additionally, The authors introduce a novel ST instance named IterNorm with trace loss (INTL) to prevent collapse and modulate the spectrum of embedding toward equal eigenvalues during optimization.
- The extensive experiments on ImageNet classification and COCO object detection demonstrate the effectiveness of INTL in learning superior representations.

### Strengths
- (+) The authors show the novel points of the proposed methods, INTL, while comparing them with previous methods such as hard and soft whitening.
- (+) The authors show the empirical observations of IterNorm, which map all non-zero eigenvalues to approach one, with large enough iterations (T).

### Weaknesses
 - (-) The authors seem to have a missing baseline [1] in SSL. The baseline looks similar to INTL from the viewpoint of spectral adjusting.
    - [1] Exploring the Gap between Collapsed & Whitened Features in SSL-ICML2022

### Questions
- Could the authors compare the INTL method with the baseline [1] if possible?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
