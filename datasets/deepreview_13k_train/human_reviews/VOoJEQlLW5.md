# Bayesian Regularization of Latent Representation

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
The effectiveness of statistical and machine learning methods often depends on how well data features are characterized. Developing informative and interpretable latent representations with controlled complexity is essential for visualizing data structure and for facilitating efficient model building through dimensionality reduction. Latent variable models, such as Gaussian Process Latent Variable Models (GP-LVM), have become popular for learning complex, nonlinear representations as an alternative to Principal Component Analysis (PCA). In this paper, we propose a novel class of latent variable models based on the recently introduced Q-exponential process (QEP), which generalizes GP-LVM with a tunable complexity parameter, $q>0$. Our approach, the \emph{Q-exponential Process Latent Variable Model (QEP-LVM)}, subsumes GP-LVM as a special case when $q=2$, offering greater flexibility in managing representation complexity while enhancing interpretability. To ensure scalability, we incorporate sparse variational inference within a Bayesian training framework. We establish connections between QEP-LVM and probabilistic PCA, demonstrating its superior performance through experiments on datasets such as the Swiss roll, oil flow, and handwritten digits.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper extends Gaussian Process Latent Variable Models (GP-LVM) by replacing the Gaussian Process with a more general Q-exponential process, thereby obtaining a series of new LVMs, Q-exponential Process LVMs (QEP-LVM). The author points out the relationship between QEP-LVM and non-linear probabilistic PCA, derives the ELBO of Bayesian QEP-LVM, and introduces a mechanism to optimize the ‘q’ of q-exponential distribution. Experiments prove the effectiveness of the proposed QEP-LVM.

### Strengths
1.	The motivation of this paper is intuitive and reasonable.
2.	The research on the proposed QEP-LVM is very solid. Not only does it reveal the relationship between QEP-LVM, GP-LVM and non-linear PCA, but it also derives the tractable ELBO of Bayesian QEP-LVM. In addition, a Bayesian approach is developed to obtain the optimal q.
3.	This paper is clearly written.

### Weaknesses
1.	The paper includes numerous visualization experiments; however, some, like Figure 5, do not reveal significant performance differences between QEL-LVM and GP-LVM. It is recommended to incorporate more numerical comparisons. For instance, for the cluster formed by the two numbers in Figure 5, utilize evaluation metrics from clustering algorithms, such as the Adjusted Rand Index (ARI) or Normalized Mutual Information (NMI), to assess and compare the proposed QEP-LVM and GP-LVM. The lack of quantitative metrics makes it difficult to objectively assess the improvement of QEP-LVM over GP-LVM.
2.	It appears that the proposed QEP-LVM requires additional training during the testing phase to compute the ELBO. How long does this training take, and will it impact the practicality of QEP-LVM? The computational overhead of this additional training step is not clear, and it is important to understand its impact on the overall efficiency of the method.

### Questions
In the visualization of the latent representation in Figure 3, it seems that the separation of points is not as good as in Figure 2 when q=1.5. Is this an illusion? If not, what is the reason for it?

### Soundness
3

### Presentation
3

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
This paper proposes a model that extends the Gaussian Process Latent Variable Model (GP-LVM) to a non-Gaussian framework by employing the Q-exponential process (QEP). Specifically, the authors replace the Gaussian log-likelihood’s $ l_2 $ norm component with an $ l_q $ norm for $q > 0$, introducing an alternative to Gaussian assumptions. They derive both Maximum Likelihood Estimation (MLE) and variational Bayesian inference methods for this model. Experimental evaluations are conducted on the Swiss roll, oil flow, and MNIST datasets, and the results are compared with those of the GP-LVM.

### Strengths
- **Clarity**: The paper is well-organized and clearly written, making it accessible for readers.
- **Contextualization**: The authors provide a thorough review of related work.
- **Theoretical Derivation**: While I haven't exhaustively verified here, the paper appears to present a sound derivation of the ELBO within the variational Bayesian framework.

### Weaknesses
 - **Significance of Contribution**: The experiments focus on datasets with limited scale and relatively artificial characteristics, which limits the persuasiveness of the findings. The results do not convincingly demonstrate a substantial improvement over the GP-LVM. Testing the proposed method on larger datasets or more practical tasks (e.g., robotics) could improve the impact of the results. The current experiments do not adequately explore the parameter space of the q-exponential process, particularly how different values of 'q' affect the learned latent space and the model's performance. A more thorough investigation into the sensitivity of the model to this parameter is needed to justify its introduction.
- **Comparison with Other Methods**: The experimental comparisons are restricted to the GP-LVM. To better assess the advantages of the QEP-LVM, it would be valuable to include comparisons with other methods suited for non-Gaussian or manifold data, such as Isomap for Swiss roll or neural networks for classification tasks like MNIST and oil flow. The lack of comparison with other dimensionality reduction techniques, especially those designed for manifold learning, makes it difficult to ascertain the specific benefits of the proposed approach. Furthermore, the absence of a quantitative comparison with methods like Isomap, which are also designed for manifold learning, makes it hard to evaluate the quality of the learned latent space beyond visual inspection.

### Questions
For more detailed points, please refer to the weaknesses section above.

Minor Comments:
- The notation $ q-ED $ could be improved as it might be misinterpreted as "q minus ED." A clearer notation, such as $ q_{ED} $, might enhance readability.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces a generalisation of the GP-LVM with the novel Q-Exp process. The training ELBO is derived and the performance is shown in multiple experiments to be improved upon GP-LVM.


After the first rebuttal answer, I have raised my score by one point.

### Strengths
Disclaimer: I am not familiar with QEP and am only partially familiar with GP-LVM. Thus my judgement is at times more superficial.

- The generalisation of GP-LVM offers more flexibility and improved performance
- While I have not managed to check all the mathematical details, they seem to be well executed.
- Experiments in small-scale toy problems demonstrate the performance of the method.

### Weaknesses
 - The main weakness for me lies in the presentation which is hard to follow and at places unclear. See the questions below for more details on this point.
- Some claims such as the regularization effect and the connection to probabilistic PCA are not sufficiently worked out and need improvement.

- Definition 1:
  - Can you give an intuition on how the q-exp distribution is different from the Gaussian potentially with examples? How does the distribution change with $q$?
  - What values can $q$ take in theory and what values are suitable in practice? You mainly focus on $0<q<2$ in the experiments, why is that?
- Remark 1: "more regularization". What form does the regularization take and where do I see this in the mathematical expressions? How does it connect to other commonly known forms of regularization?
- Section 2.2: can you clarify what the latent variables are here? With $Q\ll D$, I assume that $f$ is the latent but in (1) we have $y=f(x)+\varepsilon$. Then, in line 184 $X$ is the latent variable. This is confusing. Please clarify. 
- Section 2: Can you give a brief overview on GP-LVM? This can help to compare your development more directly and see the differences.
- Line 161: How does replacing the GP with Q-EP impose more regularization?
- Remark 2: 
  - How does $q>0$ regularize the singular values? Which singular values do you mean explicitly?
  - $c(q)$ is not defined?
- Figure 1: 
  - What is the colour scale?
  - In the rightmost plot what is the artifact in the bottom left corner?
- Line 220: "can automatically determine the dimensionality of the nonlinear latent space". Can you explicitly clarify how this is achieved and show this in experiments? Currently, this claim is not fully supported.
- Line 261: "in two stages". Please clarify which stages.
- Line 264: What is $M$?
- Section 3.2.2: 
  - The summary in section 3.2.2 is highly appreciated but can you additionally provide an algorithmic overview of how the model is trained and how it is used during inference?
  - What is the computational complexity of your method and how does it compare to GP-LVM? How does it scale larger sample sizes? What does this imply in practice for the use of your algorithm compared to GP-LVM? Please discuss.
  - What are the hyperparameters, e.g. $\beta$ and how are they chosen, what effect do they have, and how robust is the training towards those hyperparameters? Please discuss and if possible show in experiments.
- Remark 4: With $q=2$ you claim that the Gaussian case is recovered. But here you show that there is an extra term. What am I missing or where does this discrepancy arise from? This would affect all your experiments since then $q=2$ is not exactly the GP-LVM case anymore.
- Line 363: "superior" in what sense?
- Line 377: "best" in what sense?
- Line 377: "regularization effect", can you explicitly state how we can see this? Does this mean an axis alignment effect similar to Lasso regularization?
- Figure 2 (bottom): What is the x-axis of the right plots, $q$?
- Figure 3: Why is the 2d latent subspace so different with $q=1.57$ to the one in Figure 2 with $q=1.5$? How is the representation with $q=1.57$ good, the colours of the datapoint are overlapping?
- Table 2: The results of the Gaussian case are within the standard errors (at least in terms of AUC). Please highlight and discuss that.
- Line 528: The connection to probabilistic PCA is not made explicit. Please work that out to support your claim here and from the abstract.

Smaller details:
- Citations need to be revisited:
  - Line 42: Schö[l]kopf. Please check all citations for correctness.
  - Line 82: Lowercase the citation KLEPPE & SKAUG
  - E.g. Line 141: Citations that are used within the text should not contain brackets such as "(Li et al., 2023, in Theorem 3.5) prove...".
  - E.g. Shuyi Li, ... Bayesian Learning via q-exponential process, has the NeurIPs and arXiv reference.
- Wording needs improving in some places:
  - Line 161: "[The] GP..."
  - Line 411: "of [the] kernel"
- Introduce non-standard notation for easy understanding:
  - Line 179: $\bigotimes$
  - Line 196: $\wedge$
- Table 1/2: Why is the caption font size smaller?

### Questions
- Definition 1: 
  - Can you give an intuition on how the q-exp distribution is different from the Gaussian potentially with examples? How does the distribution change with $q$?
  - What values can $q$ take in theory and what values are suitable in practice? You mainly focus on $0<q<2$ in the experiments, why is that?
- Remark 1: "more regularization". What form does the regularization take and where do I see this in the mathematical expressions? How does it connect to other commonly known forms of regularization?
- Section 2.2: can you clarify what the latent variables are here? With $Q\ll D$, I assume that $f$ is the latent but in (1) we have $y=f(x)+\varepsilon$. Then, in line 184 $X$ is the latent variable. This is confusing. Please clarify. 
- Section 2: Can you give a brief overview on GP-LVM? This can help to compare your development more directly and see the differences.
- Line 161: How does replacing the GP with Q-EP impose more regularization?
- Remark 2: 
  - How does $q>0$ regularize the singular values? Which singular values do you mean explicitly?
  - $c(q)$ is not defined?
- Figure 1: 
  - What is the colour scale?
  - In the rightmost plot what is the artifact in the bottom left corner?
- Line 220: "can automatically determine the dimensionality of the nonlinear latent space". Can you explicitly clarify how this is achieved and show this in experiments? Currently, this claim is not fully supported.
- Line 261: "in two stages". Please clarify which stages.
- Line 264: What is $M$?
- Section 3.2.2: 
  - The summary in section 3.2.2 is highly appreciated but can you additionally provide an algorithmic overview of how the model is trained and how it is used during inference?
  - What is the computational complexity of your method and how does it compare to GP-LVM? How does it scale larger sample sizes? What does this imply in practice for the use of your algorithm compared to GP-LVM? Please discuss.
  - What are the hyperparameters, e.g. $\beta$ and how are they chosen, what effect do they have, and how robust is the training towards those hyperparameters? Please discuss and if possible show in experiments.
- Remark 4: With $q=2$ you claim that the Gaussian case is recovered. But here you show that there is an extra term. What am I missing or where does this discrepancy arise from? This would affect all your experiments since then $q=2$ is not exactly the GP-LVM case anymore.
- Line 363: "superior" in what sense?
- Line 377: "best" in what sense?
- Line 377: "regularization effect", can you explicitly state how we can see this? Does this mean an axis alignment effect similar to Lasso regularization?
- Figure 2 (bottom): What is the x-axis of the right plots, $q$?
- Figure 3: Why is the 2d latent subspace so different with $q=1.57$ to the one in Figure 2 with $q=1.5$? How is the representation with $q=1.57$ good, the colours of the datapoint are overlapping?
- Table 2: The results of the Gaussian case are within the standard errors (at least in terms of AUC). Please highlight and discuss that.
- Line 528: The connection to probabilistic PCA is not made explicit. Please work that out to support your claim here and from the abstract.

Smaller details:
- Citations need to be revisited:
  - Line 42: Schö[l]kopf. Please check all citations for correctness.
  - Line 82: Lowercase the citation KLEPPE & SKAUG
  - E.g. Line 141: Citations that are used within the text should not contain brackets such as "(Li et al., 2023, in Theorem 3.5) prove...".
  - E.g. Shuyi Li, ... Bayesian Learning via q-exponential process, has the NeurIPs and arXiv reference.
- Wording needs improving in some places:
  - Line 161: "[The] GP..."
  - Line 411: "of [the] kernel"
- Introduce non-standard notation for easy understanding:
  - Line 179: $\bigotimes$
  - Line 196: $\wedge$
- Table 1/2: Why is the caption font size smaller?

### Soundness
3

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
4

### Summary
This paper extends the GP-LVM to a more general form, known as QEP-LVM, which regularizes the model using an Lq penalty. It establishes the equivalence between GP-LVM and a specific case of QEP-LVM. The experimental results conducted on three real-world datasets demonstrate the good performance of the proposed approach.

### Strengths
The paper is well-organized and easy to read.

### Weaknesses
1. It would be beneficial to include the time complexity analysis and a comparison of the running times between GP-LVM and QEP-LVM, especially for a relatively large data set -- MNIST.
2. For me, it represents a natural combination of QEP and LVM. While the creativity is incremental, I would like to see more applications in other areas where Gaussian processes are typically utilized.

### Questions
1. What is the practical meaning of q? Also, the author mentioned that it's based on the Lq penalty, but I'd like more explanation, like why q ranges from 1 to 2.
2. Does the choice of kernel impact the performance of the QEP-LVM?

### Soundness
3

### Presentation
4

### Contribution
2
