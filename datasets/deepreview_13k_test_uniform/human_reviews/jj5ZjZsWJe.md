# Stochastic Controlled Averaging for Federated Learning with Communication Compression

- Decision: Accept
- Scores: 8, 8, 8

## Abstract
\noindent\footnote{The work is conducted at LinkedIn --- Bellevue, 98004 WA, USA. Xinmeng Huang is currently a Ph.D. student in the Graduate Group of Applied Mathematics and Computational Science at the University of Pennsylvania.}
Communication compression, a technique aiming to reduce the information volume to be transmitted over the air, has gained great interest in Federated Learning (FL) for the potential of alleviating its communication overhead. However, communication compression brings
forth new challenges in FL due to the interplay of compression-incurred information distortion and inherent characteristics of FL such as partial participation and data heterogeneity.
     Despite the recent development,  
     the performance of compressed FL approaches has not been fully exploited.    
     The existing approaches either cannot accommodate 
     arbitrary data heterogeneity or partial
participation, or require stringent conditions on compression.

\vspace{0.2in}
\noindent In this paper, we revisit the seminal stochastic controlled averaging method by proposing an equivalent but more efficient/simplified formulation with halved uplink communication costs. Building upon this implementation, we
propose two compressed FL algorithms, \scallion and  \scafcom, to support unbiased and biased compression, respectively.
Both the proposed methods outperform the existing compressed FL methods in terms of communication and computation complexities.
Moreover, \scallion and \scafcom accommodate arbitrary data heterogeneity and do not make any additional assumptions on compression errors.
Experiments show that \scallion and  \scafcom can match the performance of corresponding full-precision FL approaches with substantially reduced uplink communication, and outperform recent compressed FL methods under the same communication budget.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper suggests a federated learning algorithm that finds a stationary point while handling arbitrary client heterogeneity, partial client participation, local updates, and gradient compression. This work introduces an algorithm based on SCAFFOLD which communicates to the server only a single compressed vector. The paper shows convergence to a stationary point under very weak communication and compression assumptions and provides results for both biased and unbiased compressors.

### Strengths
* The proof looks sound.
* I believe that the results for biased compressors are a substantial contribution.

### Weaknesses
1) I believe the paper lacks comparison (both theoretical and experimental) with "MARINA: Faster Non-Convex Distributed Learning with Compression". Both papers pursue the same goals, namely handling the following FL issues:
* arbitrary client heterogeneity,
* partial client participation,
* gradient compression.

Overall, as far as I know, MARINA (one of itsvariations) is the closest result in terms of settings (and I think it achieves similar bounds), and I'm not sure whether the authors are aware of it.

2) Theorems 1 and 2: "set learning rates $\eta_l$ and $\eta_g$ as well as scaling factor $\alpha$ properly" - the parameters should be specified in the main body.

3) The paper handles local updates (K local updates per round), but this is achieved by dividing the learning rate by a factor of K. In other words, local updates don't provide provable improvement compared to a single larger gradient step.

### Questions
How does your paper compare with MARINA?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this work, the authors propose two new algorithms SCALLION and SCAFCOM. Those new FL algorithms show robustness to data heterogeneity, partial participation, local updates and use communication compression. They are based on SCAFFOLD algorithm.

The authors provide convergence analysis for these two algorithms in non-convex case and show that the convergence rate is faster than rates of previous algorithms. The experiments support theoretical guarantees obtained by the authors.

### Strengths
1. Interesting idea related broadcasting the compressed difference. This new view on the updates from SCAFFOLD help to design new proposed algorithms and to understand why the work.
2. Only two assumptions are used for convergence analysis.
3. Well written paper and good presentation of results. It is easy to follow.

### Weaknesses
1. For me there is no reasonable weaknesses. Possible, in camera ready version it would be better compare your methods with this work
https://arxiv.org/pdf/2310.07983.pdf .

### Questions
I do not have questions. Probably, I will ask some questions during the discussion period. 

Typos:
1. In the third row of the chain of inequalities, $L^2$ is missed in the second term.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper delves into the challenge of minimizing the objective, which is defined as a finite sum of smooth, and potentially non-convex, functions within a Federated Learning setting. The primary focus is addressing the significant workers-to-server communication costs arising in a centralized distributed framework, which involves one main server and multiple nodes. The authors' contributions can be summarized as:

- They present a novel formulation of the foundational SCAFFOLD algorithm, which effectively cuts uplink communication expenses by half. This lays a more straightforward foundation for integrating communication compression.
- The SCALLION algorithm is introduced, leveraging the new SCAFFOLD formulation combined with unbiased compressors.
- The SCAFCOM algorithm is developed to facilitate biased compressors in Federated Learning via local momentum. Convergence analysis for standard contractive compressors is provided.
- It is demonstrated that both SCALLION and SCAFCOM either match or surpass the communication and computation complexities of current compressed FL baselines.
- Through experiments, it's evident that SCALLION and SCAFCOM deliver performance akin to full-precision techniques, boasting compression savings exceeding 100x.

### Strengths
- The writing of the paper is clear, the main claims are outlined, and the text is easily read;
- Literature review is solid and contains relevant papers on the topic;
- Proposed novel FL algorithms, SCALLION and SCAFCOM, are provably shown to be robust to heterogeneous data and partial participation and require only standard assumptions to establish first-order stationary point guarantees;
- SCALLION attains superior convergence guarantees compared to prior compressed FL methods with unbiased compression under minimal assumptions;
- Local momentum in SCAFCOM overcomes the adverse effects of biased compression. SCAFCOM improves communication complexity by a factor of 1/(1-q) over the prior art;
- Both SCALLION and SCAFCOM exhibit robustness to heterogeneous data and partial participation, unlike existing approaches;
- The paper provides a principled way to integrate communication compression into federated learning through the new SCAFFOLD formulation;
- Algorithms are simple to implement and empirically achieve significant compression savings.

### Weaknesses
1) Some potentially relevant papers are missing in the references. See "Suggestions" below. 

## Typos:
1) In the RELATED WORK section, instead of "TurnGrad" it should be "TernGrad".

## Suggestions:
I would recommend authors to reconsider some of the phrases that they wrote, in particular

>>Can we design FL approaches that accommodate arbitrary data heterogeneity, local updates, and partial participation, as well as support communication compression?
>>
>>In the literature, none of the existing algorithms have successfully achieved this goal, to the best of our knowledge.

To the best of my knowledge, this is true, but for the general class of non-convex loss functions. However, this is not true for strongly convex functions. There are already some works [1, 2, 3, 4] on that topic, providing a provably beneficial combination of compression, partial participation, and local updates.

[1] Grudzień, M., Malinovsky, G., & Richtárik, P. (2023). Improving Accelerated Federated Learning with Compression and Importance Sampling. _arXiv preprint arXiv:2306.03240_.

[2] Youn, Y., Kumar, B., & Abernethy, J. (2022, October). Accelerated Federated Optimization with Quantization. In _Workshop on Federated Learning: Recent Advances and New Challenges (in Conjunction with NeurIPS 2022)_.

[3] Condat, L., Malinovsky, G., & Richtárik, P. (2023). TAMUNA: Accelerated federated learning with local training and partial participation. _arXiv preprint arXiv:2302.09832_.

[4] Sadiev, A., Malinovsky, G., Gorbunov, E.A., Sokolov, I., Khaled, A., Burlachenko, K., & Richt'arik, P. (2022). Federated Optimization Algorithms with Random Reshuffling and Gradient Compression. _ArXiv, abs/2206.07021_.

### Questions
There are several questions related to the prof of the Theorem 3:
1) (Page 25) Could authors please clarify why this inequality holds?

$$9 e^2 K^2 \eta_l^2 L^2\left(24+\frac{4(1+\omega) \alpha^2}{S}+\frac{522(1+\omega) \alpha}{N}\right) \leq \frac{\alpha(1+\omega)}{N} \leq \frac{1}{4}$$

2) Why does this property hold?
$$\| {x^0 - x^1}\|=0$$

## Conclusion
I would happily give this paper a higher grade for its theoretical contributions and reliable experiments. However, at this moment, I can not do so since the paper still contains things that need to be clarified. I am ready to reconsider my current rate during rebuttals once you respond to me on Weaknesses and Questions.

## Update after the author's rebuttal
I increased the score.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent
