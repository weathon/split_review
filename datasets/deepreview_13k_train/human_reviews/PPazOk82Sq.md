# Label Noise Gradient Descent Improves Generalization in the Low SNR Regime

- Decision: Reject
- Scores: 5, 8, 6, 6, 3

## Abstract
The capacity of deep learning models is often large enough to both learn the underlying statistical signal and overfit to noise in the training set. This noise memorization can be harmful especially for data with a low signal-to-noise ratio (SNR), leading to poor generalization. Inspired by prior observations that label noise provides implicit regularization that improves generalization, in this work, we investigate whether introducing label noise to the gradient updates can enhance the test performance of neural network (NN) in the low SNR regime. Specifically, we consider the learning of a two-layer NN with a simple label noise gradient descent (GD) algorithm, in an idealized signal-noise data setting. We prove that adding label noise during training suppresses noise memorization, preventing it from dominating the learning process; consequently, label noise GD enjoys rapid signal growth while the overfitting remains controlled, thereby achieving good generalization despite the low SNR. In contrast, we also show that NN trained with standard GD tends to overfit to noise in the same low SNR setting and establish a non-vanishing lower bound on its test error, thus demonstrating the benefit of label noise injection in gradient-based training.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper analyses generalisation error of gradient descent with and without label noise in a binary classification problem setting where the input is split into patches, with only one patch being dependent the class label and the other patches being random noise. The results mainly apply to the setting where the input norm in a noisy patch is much larger than the signal patch and where the number of training points is small relative to the dimension of an input patch. The model is a simple one hidden layer MLP, which is applied separately to all patches and added.


The main result of the paper shows that gradient descent with artificial label noise acts as a regulariser and generalises in low SNR setting while standard gradient descent fails.

### Strengths
The setting and the failure of gradient descent to generalise in such low SNR settings is well known, the viewpoint of label noise as regulariser is less studied however and the paper gives a detailed analysis and a reasonable proof sketch. It also demonstrates the result with a simple synthetic setup and demonstrates the message of the theorems. The analysis of the signal and noise coefficients with label noise is technically complex and intricate piece of work.

### Weaknesses
1. The theorem and results are quite believable, as they are also demonstrated with simple examples. But the setup of the results in the main paper seems to lack rigour. As evidenced in the haphazard way the order notation is used.

e.g Assumption 3.1 says n is Omega(1) but d is Omega(n^2). I am not sure how that is possible if Omega and O and Theta only hide absolute universal constants (like 2 and pi and not problem dependent constants like d,n, m etc). There are several other places where this issue pops up, like Theorem 3.2 has some constants C1 and C2 inside the Theta notation. As written now, the Theorems 3.1 and 3.2 sound vacuous, even though the underlying message is likely true. I would recommend replacing O, Theta and Omega with explicit absolute constants in the main paper, and give these constants in the appendix. The issue is that the constants hidden by the asymptotic notation seem to depend on the problem parameters themselves, which makes the theorems difficult to interpret and verify. For example, if the hidden constant in $d = \Omega(n^2)$ depends on $n$, then the statement is not very useful.


2. The two main results are Theorems 3.1 and 3.2. But Theorem 3.1 proves the same result as Cao et al.for q=2 while they prove for q>2. This is not a significant extra contribution. The authors should clarify if the result of Cao et al. applies to real values of q>2, and if so, whether Theorem 2.1 could be derived via an approximation argument, such as using ReLU^{2.0001} and arguing this is close to ReLU squared. If the result of Cao et al. does apply to real values of q, then the contribution of Theorem 3.1 is further diminished.


3. The final weakness has to with the artificiality and extreme simplicity of the entire setup. While it is true that several papers have been published under similar setups (two layer networks with fixed last layer) I believe we need more realistic setups to make progress and for practitioners to actually take notice of the work done by theoreticians.

### Questions
I would appreciate a simplified version of Assumption 3.1 and Theorems 3.1 and 3.2 (even if it is less general) where several of the constants (like $\sigma_p, \mu, m, n $ ) are fixed and only the dimension $d$ is present as a symbol. The assumptions and theorem statement should be capable of being computed instead of just being given in order terms. 

The label noise fraction seems to be a crucial parameter and is not given sufficient detail in the assumptions (it is bounded by some undefined C) and in the proofs and also in the synthetic experiments. Some details on this is needed.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper explores the effects of label noise gradient descent (GD) on improving generalization in deep learning models under low signal-to-noise ratio (SNR) conditions. The authors argue that neural networks trained with standard gradient descent tend to overfit noise in the low SNR regime, leading to poor generalization. In contrast, label noise GD, where random label noise is introduced during training, mitigates noise memorization and leads to improved generalization performance. The authors present theoretical analysis and empirical experiments to support their claims, demonstrating that label noise GD effectively enhances signal learning while controlling overfitting in noisy settings.

### Strengths
Theoretical Contributions: The authors offer rigorous theoretical analysis, demonstrating that label noise GD can effectively balance the trade-off between noise memorization and feature learning in challenging settings. The use of supermartingale arguments and concentration inequalities adds depth to the theoretical framework.

### Weaknesses
Practical Applications: While the theoretical analysis and synthetic experiments are thorough, adding experiments on more complicated simulations or real-world datasets would significantly strengthen the practical relevance of the findings. The current experiments, while illustrative, do not fully capture the complexities of real-world data distributions or the nuances of practical deep learning scenarios. For example, the synthetic data used appears to be generated from a relatively simple model, which may not accurately reflect the challenges encountered in real-world applications where data is often high-dimensional, noisy, and exhibits complex dependencies.

Data Generating Process Complexity: The current data generating process appears to be relatively simple, which may limit the generalizability of the results. I suggest exploring more complex data generation functions, such as staircase functions and parity functions, to test the robustness of the proposed method in capturing more intricate relationships. The use of a simple linear model with added noise might not fully expose the limitations or strengths of the proposed label noise gradient descent method when dealing with more complex, non-linear relationships or higher-dimensional feature spaces. This raises concerns about the method's applicability to real-world datasets that often exhibit such complexities.

### Questions
Data Generating Process Complexity: The current data generating process appears to be relatively simple, which may limit the generalizability of the results. I suggest exploring more complex data generation functions, such as staircase functions and parity functions, to test the robustness of the proposed method in capturing more intricate relationships.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper investigates the performance of a variant of Gradient Descent (GD), termed Label Noise Gradient Descent (LNGD), in scenarios with low signal-to-noise ratios. 
LNGD introduces label flipping as a stochastic process before performing GD iterations, maintaining a computational cost comparable to standard GD. 
The authors demonstrate a scenario where GD fails while LNGD is effective. 
I find the paper to contain intriguing concepts, but some sections necessitate further elucidation. 
With proper clarification of these points, I would recommend acceptance.

### Strengths
1. The authors establish a theoretical separation between the performance of GD and LNGD under specific signal-to-noise ratio (SNR) settings.
2. The proposed LNGD method does not introduce additional computational costs.
3. The paper is well-structured and presented clearly.
4. The synthetic experiments corroborate the theoretical findings well.

### Weaknesses
1. [Major Concern] Theorem 3.1 suggests that GD fails with a threshold of $t = \Theta(m^3 n /d)$, where $m$ is the number of neurons, while Theorem 3.2 indicates that LNGD succeeds with a threshold of $t = \Theta(m)$. This discrepancy raises concerns about the failure conditions and the comparative performance when both algorithms are evaluated within the same time frame. Additionally, it is unclear how varying the number of iterations for GD and LNGD affects their success or failure. To summarize, it requires:
- Clarify if the different time thresholds for GD and LNGD are directly comparable, and if not, explain why.
- Provide a more detailed comparison of how GD and LNGD perform when run for the same number of iterations.
- Analyze or discuss how the performance of both algorithms changes as the number of iterations varies.
2. How does LNGD perform under different forms of noise? I am concerned that LNGD might only be effective in specific noise regimes. The authors should provide empirical or theoretical evidence to address this concern.
3. For larger values of $m$, it appears that reaching the generalizable region as per Theorem 3.2 becomes slower. Could the authors offer insights into this phenomenon?

### Questions
See above

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper analyzes a data model introduced in prior work on 2-layer convolutional network training dynamics, and shows that training such networks using label noise can allow for generalization even in low signal-to-noise (SNR) settings. The main contribution of this work is to show that previous negative results on noise memorization in low SNR settings can be avoided with very little additional computational overhead.

### Strengths
**Significance:** This paper addresses the important problem of learning in low SNR settings, and shows that introducing a small amount of label noise can mitigate noise memorization issues, which is an observation with potentially significant practical ramifications given the ease with which label noise can be introduced.

**Quality:** Overall the results and techniques in this paper are interesting, and the work seems sound as it operates in a now well-established theoretical setting and appropriately builds off/draws comparisons to the prior related work.

**Clarity:** The paper is well-written; the key ideas are introduced properly and the results are contextualized well.

**Originality:** Although the paper is working in an identical setting to prior work [1], the label noise analysis is new and uses techniques that did not appear in the previous results.

[1] Cao, Yuan et al. “Benign Overfitting in Two-layer Convolutional Neural Networks.” ArXiv abs/2202.06526 (2022).

### Weaknesses
Overall, I find the paper to be successful in what it sets out to do and thus favor acceptance; however, I do feel the paper could be stronger with a more practical verification of the introduced ideas. Additionally, some aspects related to clarity could be improved -- these are outlined below.

**Experiments:** The paper only contains synthetic experiments, which serve to verify the theory directly. However, several of the prior works in this direction (analyzing conv nets on multi-feature/multi-view data) have included experiments at least on image classification benchmarks to show that their theoretical observations still transfer (to an extent). For example, it seems to me that one could practically mimic Definition 2.1 by concatenating random noise to images from standard datasets (randomly to either the front or back).

**Clarity of Theory:** Theorem 3.1 has an analogous result in [1] (Theorem 4.4) and it would be helpful to compare the two more directly. It would also be useful to provide more motivation for using squared ReLU as opposed to other modifications -- for what pieces of the analysis is this necessary? Lastly, it would be nice to sketch some intuition for proving the supermartingale property in Lemma D.4; I looked at the proof but it's hard to get a sense from the calculations themselves.

### Questions
- My main question is regarding the choice of activation (as mentioned above) -- in prior work, using higher power polynomials of ReLU was important for making sure noise was suppressed while the signal was learned, and I'm curious how important the choice of using squared ReLU is here?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a very specific example where there is large noise in the data and the number of samples is smaller than the dimensions, so that standard GD cannot be better than random guess, but GD with label noise can achieve 100% accuracy. The authors proved for this specific scenario that label noise GD can achieve small error while standard GD cannot, and validated it with a synthetic experiment.

### Strengths
1. Reproducibility: I have done the experiment myself and the results can be reproduced
2. Intellectually, there exists such an example is a fun fact to know
3. The authors proved their theorems with complicated techniques, so there might be technical novelties though I cannot check the proof carefully

### Weaknesses
Over the years I have seen a number of papers claiming to "prove" some big or surprising results, by means of a very specific, sometimes even toyish, example. I am not a big fan of this class of papers. Unfortunately, this paper belongs to this class. My main concern of this type of papers is that they cannot show whether the results they prove only work for the very specific example they study, and whether these results can be generalized to a more, even slightly, general situation. After all, one can prove that something does not work by giving a counter-example, but one cannot prove that something works by just giving one example. Thus, the conclusions these papers make are usually misleading, and since they make big claims, these papers are often much more misleading than others.

In the case of this particular submission, I did some experiments and came to the conclusion that the claim of this paper "label noise GD can be better than standard GD" only works for very limited situations. Even for the very example the authors provided, changing just one parameter can break the whole story. 

I used the exact same setting as the authors in Section 5. I always used the parameters in the code in the supplementary material if it disagrees with the paper. For instance, the paper used $\eta=0.5$ (line 465) while in the code $\eta = 1.0$, so I used $\eta = 1.0$. The paper didn't say what flip probability was used, and $p=0.1$ was used in the code so I used that too. My code: https://pastecode.io/s/r6epwvx7

I always used fixed random seeds so my results are fully reproducible. I encourage the authors and my fellow reviewers to play with my code on their own.

First, I reproduced the results in the paper, using the exact same set of parameters. In the following plots, the blue curves are the training loss, while the orange curves are the test accuracy. 

- Standard GD: https://i.postimg.cc/YC0LGM7z/1.png
- Label noise GD: https://i.postimg.cc/C1TRQ8qc/2.png

I managed to reproduce the exact same results as the authors.

Next, when I stared at the code, the first thing that struck me was that the model architecture looked quite strange. First, I couldn't understand what the authors mean by "two patches" $x = \{ x^{(1)}, x^{(2)} \}$ (line 144), and I couldn't understand why there should be a "patch" that is just Gaussian noise. Second, I don't think the model in lines 172-174 is a "CNN" because I don't see any convolution here. Third, the squared ReLU activation is not usually used. Anyway, I tried to change the model a little bit and see if it could help, and the very first thing I did was to use a smaller $m$ (that is, making the network narrower), which I believe is a very reasonable and very natural thought. Here are the results:

- Standard GD, with $m=3$: https://i.postimg.cc/br6NpSZc/3.png
- Label noise GD, with $m=3$: https://i.postimg.cc/7Ydw9k7V/4.png

Standard GD now achieves 100% test accuracy. Thus, by simply changing $m=20$ to $m=3$, the problem is immediately solved.

Plus, when $m=3$, standard GD still works with a larger noise. I changed $\sigma_p = 0.5$ to $\sigma_p = 2.0$, and ran the two methods again with $m=3$. Here are the results:

- Standard GD, with $m=3, \sigma_p = 2.0$: https://i.postimg.cc/HLCHG968/5.png
- Label noise GD, with $m=3, \sigma_p = 2.0$: https://i.postimg.cc/zDPrDrdr/6.png

In this case, standard GD can achieve 90-ish% test accuracy, while the performance of label noise GD is miserable. Thus, I've shown a case where label noise GD is much worse than standard GD.

The authors might argue: "Our theory only works when $m$ is not too small (Assumption 3.1 (ii))." I don't think this is a valid argument, because one is free to choose whatever model architecture they want. And if a narrower network can work so well, why bother using a wider one that is much worse? Moreover, when we couldn't get expected results in deep learning, we should always start with trying something straightforward like changing the network architecture, optimizer, loss, etc., before trying something very unnatural like "adding label noise during training".

To sum up, the experimental results I present here establish the fact that the claim of this paper, that is "label noise GD is better than GD", is not very robust and not very sound. I am not convinced that label noise can improve generalization in any practical regime.

As a final remark, I am not saying that the authors should not get credit for constructing this particular example in the paper. I think it is a fun fact to know that such an example exists. However, I think the conclusion of this submission is unsound, and the paper is quite misleading due to its catchy claim "label noise GD improves generalization". The claim can be easily invalidated by just changing one parameter. Imagine a PhD student who read this paper, got attracted by the idea, and tried to add label noise on a number of tasks, only to find out that it didn't work at all and lots of time and work went down the drain. For the sake of that student and the learning theory community, I must insist on rejecting this submission.

### Questions
If the authors really want to argue that label noise GD has its merits in some situations, they need to provide general sufficient or necessary conditions under which label noise GD is better than standard GD, instead of just a toy example. If you can provide a sufficient condition that is weak enough, then the results you established will be much more useful.

I also think that the authors ought to do experiments on some real-world experiments, to show that your theory can be at least useful in some situations. You also need to show that simple solutions such as changing the network width cannot solve the problem, and thus using label noise is necessary.

### Soundness
1

### Presentation
3

### Contribution
1
