# Do Generated Data Always Help Contrastive Learning?

- Decision: Accept
- Avg Score: 5.60
- Scores: 8, 3, 5, 6, 6

## Abstract
Contrastive Learning (CL) has emerged as one of the most successful paradigms for unsupervised visual representation learning, yet it often depends on intensive manual data augmentations. With the rise of generative models, especially diffusion models, the ability to generate realistic images close to the real data distribution has been well recognized. These generated high-equality images have been successfully applied to enhance contrastive representation learning, a technique termed ``data inflation''. However, we find that the generated data (even from a good diffusion model like DDPM) may sometimes even harm contrastive learning. We investigate the causes behind this failure from the perspective of both data inflation and data augmentation. For the first time, we reveal the complementary roles that stronger data inflation should be accompanied by weaker augmentations, and vice versa. We also provide rigorous theoretical explanations for these phenomena via deriving its generalization bounds under data inflation. Drawing from these insights, we propose \textbf{Adaptive Inflation (AdaInf)}, a purely data-centric strategy without introducing any extra computation cost. On benchmark datasets, AdaInf can bring significant improvements for various contrastive learning methods. Notably, without using external data, AdaInf obtains 94.70\% linear accuracy on CIFAR-10 with SimCLR, setting a new record that surpasses many sophisticated methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper challenges the common belief of generated data being always helpful to contrastive learning and empirically show that this need not always be the case. The paper identifies, two issues that control if generated data would be helpful or not to learn good representations, namely the discrepancy between generated and real data distributions and the mixing ratio of real and generated data. Based on these insights, the authors propose AdaInf which does a grid search over different mixing ratios and augmentation levels to find the best combination for downstream tasks. The authors also give theoretical justifications as to the empirical trends they observe.

### Strengths
The insights and results provided by this paper seem novel, creative and significant. I believe the results would greatly help in our understanding of contrastive learning both theoretically and empirically.

The paper is very well-written in general except some proofs in the appendix which I will describe in detail in the weaknesses section.

### Weaknesses
The proposed Adainf method seems to rely on the downstream task to find the optimal weighing factor and augmentation strength. This might limit it's use in practice since the goal of self supervised learning is to learn a good representation from training data that can be useful in future downstream tasks, I do not know a priori. Some discussion on this would be useful, either as a limitation or clarifying the exposition in case I misunderstood something.

Eq (7) in proof of theorem 4.1: I think the steps need to be explained. It is not clear to me how the indicator function is swapped from I(y(x) \neq y(x')) to I(y(x) \neq y(\bar{x})) in the second equality, why is the first inequality true, and how the sum disappeared in the third equality. 

What is the difference between the definition of \alpha and equation 8? Shouldn't they be equal?

The statement of theorem 4.1 should be qualified with what exactly is the optimal encoder? What is the objective here? Lemma D.1 indicates this is some population spectral contrastive loss. The precise definition of this loss should be made clear in the paper. Similarly, eq 5 should be in the main text since it defines the prediction function using the linear classifier on top of Pretrained features. The paper makes no mention that this is really majority voting over prediction made on all possible augmentations of the sample point. 

I would suggest the authors use Markov's inequality to obtain equation 11 to make the proof rigorous. 

Minor Typo: Eq (12) second equality, shouldn't it be P_t instead of P_g?

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies whether synthetic data generated with a diffusion model can help self-supervised learning. By reweighting the ratio of generated and real data, and re-tuning the augmentation strength used on the positive pairs, the authors are able to show that gains are possible on CIFAR10, CIFAR100 and Tiny Imagenet.

### Strengths
The paper is generally well written, and the results are interesting (albeit limited in scale, see below, which limits signficance). Some theoretical intuition is given, although clarity in the connection of theory and empirical results could be improved.

### Weaknesses
Theory and empirical experiments are not well connected, in my opinion. Here is how I read the paper: Leveraging synthetic data requires to define how it will be mixed with real data. Also, as image statistics of synthetic data might be different from real data, the existing augmentations applied to contrastive learning might be suboptimal --- hence, re-tuning both aspects of the model could help to boost performance. If the authors would have a better way to connect theory and empirical observations, this could be interesting --- but in the current outline of the paper, both tracks seem pretty independent to me.

Another weakness are the empirical results: These results are fairly small scale with limited evaluation of different generative models. A lot of evaluations are performed on CIFAR-10 where one would expect the possibility to run extensive experiments and analysis of various factors. To make the statements in the paper more convincing, it would help to extend these experiments, compute error bars, study the influence of other parameters, and extend the most promising models towards full ImageNet-scale.

Additional weaknesses/concerns:

- The InfoNCE loss on (1) is incorrect. It misses a "-" in front of the positive loss, and also typically in InfoNCE, there is a sum vs. a mean over the negative examples, as the number of negatives influences embedding quality (this only yields a $\log N$ difference in the value of the loss but does not influence the gradients) --- I think it is still better to re-state the loss as common in the literature.
- "significantly" is used at different places in the paper. Please check the usage, and remove where it is not backed up by a statistical test. I would strongly encourage the authors to run multiple (I would suggest at least 5) seeds of their models and report error bars on every CIFAR-scale experiment reported in the paper.
- in Table 1, the FID scores of the used generative models on the respective dataset should be added, this seems to be a major influence on experiment outcome.

Minor

- Theorem 3.1, was the total variation introduced before? If not, clarify the abbreviation (TV) where it first appears in the text.
- for the theorems, it might be useful to link to the respective section where the proof is stated, for easier navigation through the document
- The notation in 4.1 should be double checked. E.g. $\mathcal{\overline{X}} = {\overline{x}}$, is that correct? or $D_{xx}$.
- Sec 4.2, "an downstream" -> "a downstream"

### Questions
- could you add some samples from the diffusion models to the supplement for a better visual impression at different FID levels? ideally compared to a set of samples from the real datasets.
- do you use different diffusion models (with different training datasets) for each of the considered subtasks? in particular, is e.g. the CIFAR model only trained on CIFAR, etc?
- Sec 4.2, how is $P_d \approx P_g$ a reasonable assumption in the light of your argument for stating Theorem 3.1?
- How do you connect Lemma 4.2 to your observed empirical results, what is it signifiance?
- In Fig 6., Vanilla data inflation *always* helps or keeps results the same. How does this relate to the statements in Figure 3(b)? It seems like the number of training steps is an important confounder we need to control for?
- datasets like ImageNet have a "photographer"/object centric bias. Do the generated samples also have such a bias? If not, could this be a possible explanation for the difference in the optimal augmentation strategy?
- Is the augmentation strategy in the base setup optimal with respect to the selection metric? If so, how was this confirmed?

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper discovered the failure mode of data inflation, a technique that augments real data with synthetic data, for contrastive learning. The finding was that data reweighting and weak augmentation can help improve the performance of contrastive learning on the combined dataset. Based on that, they proposed a method, called Adaptive Inflation (AdaInf), to train contrastive learning by adaptively adjusting augmentation strength and mixing ratio for data inflation. In addition, the authors provided the first theoretical guarantees for inflated contrastive learning. Empirically, AdaInf improved downstream accuracy significantly.

### Strengths
- This paper is well-structured.
- The theoretical results and findings are interesting.
- The experimental design is good. Experiments and ablation studies successfully verify theoretical results.

### Weaknesses
- The preliminary section is not well-written. Specifically, Eq. (1) is incorrect, and the citation is not appropriate. A more suitable reference would be "Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere" [1]. Similarly, Eq. (2) is also incorrect, and "Ho et. al 2020" would be a better citation.
- There is a concern about the generality of AdaInf. While the authors claim it to be adaptive, the method appears to be hand-crafted. The hyperparameters in Section 3.3 seem to be manually chosen rather than automatically adjusted or learned, which makes the term "adaptive" misleading.
- There is a lack of motivation for considering diffusion models in this paper. Although the authors focus on diffusion models in their experiments, all theoretical results can be generalized to any generative model. This raises the question of why diffusion models are specifically chosen and whether the findings are applicable to other generative models.
- Some notation and experimental results are not consistent. For instance, in Section 5.1, the min scale of random resized cropping (0.2) differs from the optimal value (0.3) in Figure 3. The result in Table 3 is also slightly different from that in Figure 3, where 0.3 yields the best performance.
- The definition of labeling error seems unconventional. Defining it as in Eq. (8) would make the term $\phi^y$ in Eq. (6) less than $2\alpha$. If the current definition in Theorem 4.1 is kept, then $\phi^y = \alpha$. It's worth noting that $\alpha$ in HaoChen et al. 2021a has a different meaning.
- The paper uses the notation N for replication times in Section 3.1 but uses it again in Section 4.1 with a different meaning. It is unclear what N represents in Section 4.1. Additionally, in Eq. (6), the meaning of $\mathcal{X}$ is not defined. The notation $w_{x x'}$ is used in the main text, but it is not clear if it is defined as $A_{x, x'}$.
- There are numerous typos throughout the paper, including in the description of diffusion models in Section 2, Theorem 4.1, Lemma 4.2, and Equations (7), (9), and (12).

### Questions
- Eq. (1) is wrong. In addition, the authors should cite this paper for Eq (1): “Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere”.
- Eq. (2) is also wrong. Again, the citations are not chosen well. Ho et. al 2020 should be a better reference here.
- Why do we need to sample 1M data while CIFAR-10 has only 60k samples? Speaking of which, instead of increasing $\beta$ we can decrease $|\mathcal{D}_g|$. 
- Section 3.1: Is the ratio $10:1$ true for all datasets? And is it universal for different diffusion models?
- Section 3.2: Are there any intuitions or reasonings why larger data size needs weaker data augmentation? Or do generated images need weaker data augmentation and they dominate the inflated data set?
- Section 3.3: How to choose the correct strength of data augmentation in AdaInf? The word "adaptive" seems misleading here because the hyperparameters are chosen manually rather than auto adjusted or learned.
- Section 5.1: Why is the min scale of random resized cropping (0.2) different from the optimal value (0.3) in Figure 3?
- The result in Table 3 is slightly different from that in Figure 3 where 0.3 yields the best performance.
- Figure 8: Is the replication N fixed to 10? Again, the question is whether N = 10 is universal.
- The labeling error definition seems weird. It is better to define it as Eq (8). Then, the term $\phi^y$ in Eq (6)  is less than $2 \alpha$. If the definition is kept as in Theorem 4.1, we have $\phi^y = \alpha$. Note that $\alpha$ in HaoChen et al. 2021a has a different meaning.

**Minors**:
- The usage of $B^\star$ can be safely removed.
- There are a lot of typos: Diffusion models in Section 2, Theorem 4.1, Lemma 4.2, Eq (7), Eq (9), and Eq (12) just to name a few.
- Notation:
  - N is used for replication times in Section 3.1 but later used in Section 4.1 with different meanings. What is the meaning of N in Section 4.1?
  - Eq (6), what is $\mathcal{X}$?
  - Is $w_{x x'}$ defined as $A_{x, x'}$ in the main text?
  - Overall, the notation is similar to HaoChen et al. 2021a. However, the way the authors use them is not good and sufficient.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the problem of using of synthetic data from generative models (e.g. diffusion models) for contrastive learning (CL). Firstly it finds that naively inflating CIFAR-10 with 1M generated images can in fact hurt linear probe performance of CL. The paper delves deeper in the role of (a) weight of inflated data, (b) augmentation strength. Interestingly the paper finds two simple fixes, (a) upweighting real data by 10x, (b) using weaker augmentations with more data. Based on this finding, the paper proposes adaptive Inflation (AdaInf) strategy that adjusts augmentation strength based on dataset size. Experiments on CIFAR and TinyImageNet evaluate AdaInf data strategy with SimCLR, MoCo V2, BYOL, Barlow Twins. Overall AdaInf does better than no data inflation and data inflation w/ standard augmentation. It achieves accuracy as high as 94.7% on CIFAR-10 with SimCLR. Ablations on smaller training horizon and smaller training data further shows the benefit of AdaInf.

The paper provides theoretical analysis using augmentation graph framework introduced in HaoChen et al. and shows a complementary benefit of inflation and augmentation. Stronger augmentation improve "graph connectivity" at the cost of "labeling error". More data also improves graph connectivity, thus we can get away with weaker augmentation that has smaller labeling error. Synthetic example with gaussian distribution verifies this insight.

### Strengths
Significance: The paper studies an interesting problem of role of synthetic data from generative models on contrastive learning. Given the increasing of procuring high quality data, effectively using synthetic data is a important problem to study

Novelty: The perspective on interplay between larger data and augmentation strength is interesting and novel to my knowledge. The value of real data being more than synthetic data is intuitive but not surprising. The theory, although a simple application of HaoChen et al., does provide interesting insights.

Clarity: The paper is overall well written and easy to follow. Experimental results are also presented well.

### Weaknesses
- It would have been useful to have some more discussion on the issues of using synthetic data, e.g. bias

- Some clarification and cleanup of the theory parts would be useful. See comments below

Overall the paper makes a positive contribution in studying the interplay between synthetic data and augmentation for contrastive learning. I have currently assigned weak accept, but I'd be happy to raise the score after clarification on the theory.

- Role of reweighting: Theorem 3.1 and 4.1 do not fully explain that there’s an optimal weighting. In light of mismatch between $P_s$ and $P_d$ Theorem 3.1 basically suggests that \beta=1 is best. I believe the argument in Theorem 4.1 is that $\lambda_{k+1}$ is larger when $P_g$ has larger support. It would be nice to make this point more clear. Overall it would help to more carefully deal with the case of $P_s \neq P_g$ and why would one pick $\beta < 1$.

- Lemma 4.2 uses random sub-graph with probability $p$ of selecting each edge. Is random edge selection reflective of subsampling data? Random node selection seems more appropriate.

- Thm 4.1 argues about connectivity and non-zero $\lambda_{k+1}$ for the training set, but Saunshi et al. 2022 show lack of connectivity in the training set for standard augmentations, implying $\lambda_{k+1}=0$. This would make the bound in Theorem 4.1 vacuous without any . Does that contradict the claims? The results in HaoChen et al. are non-vacuous because that uses the eigenvalue of the population distribution in the bound rather than eigenvalue of training data.

### Questions
- Role of reweighting: Theorem 3.1 and 4.1 do not fully explain that there’s an optimal weighting. In light of mismatch between $P_s$ and $P_d$ Theorem 3.1 basically suggests that \beta=1 is best. I believe the argument in Theorem 4.1 is that $\lambda_{k+1}$ is larger when $P_g$ has larger support. It would be nice to make this point more clear. Overall it would help to more carefully deal with the case of $P_s \neq P_g$ and why would one pick $\beta < 1$.

- Lemma 4.2 uses random sub-graph with probability $p$ of selecting each edge. Is random edge selection reflective of subsampling data? Random node selection seems more appropriate.

- Thm 4.1 argues about connectivity and non-zero $\lambda_{k+1}$ for the training set, but Saunshi et al. 2022 show lack of connectivity in the training set for standard augmentations, implying $\lambda_{k+1}=0$. This would make the bound in Theorem 4.1 vacuous without any . Does that contradict the claims? The results in HaoChen et al. are non-vacuous because that uses the eigenvalue of the population distribution in the bound rather than eigenvalue of training data.


Saunshi et al. 2022. Understanding Contrastive Learning Requires Incorporating Inductive Biases

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper explored the reason for the performance degradation when utilizing synthetic data from a generative model to enhance contrastive learning (CL). The authors found that the strengths of the data augmentation and the mixing ratio or the size of data inflation are the two critical factors that affect performance through theoretical analysis and empirical results. Based on the observation, the author proposed AdaInf, which adapts the weight of synthetic data and the strengths of the data augmentation to achieve the best performance. Experimental results on multiple datasets showed that AdaInf can outperform the plain CL method and the CL method with naive data inflation.

### Strengths
The strengths of the paper are listed as follows.   
1. This paper is well-motivated. Data inflation is an important method to improve the performance of CL. The reason for the unexpected performance degradation is worth exploring.   
2. The conclusions about the data inflation and data augmentation are analyzed theoretically and proved with a simple synthetic dataset empirically.    
3. The paper is well-written, where the problem is clearly defined and the analysis is easy to follow.

### Weaknesses
 The weaknesses of the paper are listed as follows.   
1. It would be better if the authors could compare AdaInf with the other existing data inflation methods for CL.   
2. The description of AdaInf is in qualitative way. For example, it claims to use different weights on real and generated data and adopt milder data augmentation. However, how to get an appropriate weighted and the strengths of the data augmentation remains unknown.  
3. It would be better if the authors could provide some experiments on more generative models like GAN.

### Questions
The questions of the paper are listed as follows.   
1. For equation (1), should there be a negative sign before the first term?   
2. Are there any experiments to show that the two tricks in AdaInf can also improve the performance of CL with data generated by more generative models like GANs?   
3. On page 3, there is a statement that better generative quality often requires larger models and/or slower sampling. What does the slower sampling mean?   
4. Are there any experiments to show the trade-off between the size of generated data for inflation and the strength of augmentation on real-world datasets? It looks like all the experiments used the same size of generated data.   
5. The purpose of Figure 4 is a little bit confusing to me. Why can this figure be used to show stronger augmentations create more overlap between different training samples?  
6. For the experiments of Figure 6, is the batch size for CL, CL with vanilla data augmentation and CL with AdaInf the same? If this is the case, does it mean the training cost is the same when the total training steps are the same for the three methods?   
7. What is the pertaining cost of the diffusion model on the evaluated datasets?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
