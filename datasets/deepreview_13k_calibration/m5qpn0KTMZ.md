# Bridging the Gap Between $f$-divergences and Bayes Hilbert Spaces

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
We introduce a novel framework that generalizes $f$-divergences by incorporating locally non-convex divergence-generating functions.
Using this extension, we define a new class of pseudo $f$-divergences, encompassing a wider range of distances between distributions that traditional $f$-divergences cannot capture.
Among these, we focus on a particular pseudo divergence obtained by considering the induced metric of Bayes Hilbert spaces.
Bayes Hilbert spaces are frequently used due to their inherent connection to Bayes's theorem. They allow sampling from potentially intractable posterior densities, which has remained challenging until now.
In the more general context, we prove that pseudo $f$-divergences are well-defined and introduce a variational estimation framework that can be used in a statistical learning context.
By applying this variational estimation framework to $f$-GANs, we achieve improved FID scores over existing $f$-GAN architectures and competitive results with the Wasserstein GAN, highlighting its potential for both theoretical research and practical applications in learning theory.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies a more general class of f-divergences that does not need to be convex on the whole domain and can be concave on the interval of $[0, a)$ and convex on $[a, \infty)$, called pseudo-divergence-generating function. The authors also link the pseudo f-divergence with the metric induced by the Bayes Hilbert space. The paper uses the proposed framework to extend f-GANs to include their locally non-convex divergence function, showing comparable results with older methods.

### Strengths
The idea of generalizing the convex divergence functions to locally non-convex is interesting and is a step towards a more general family of divergences. The paper is well-motivated and the connection to Bayes Hilbert space (BHS) is neat. I enjoyed this connection as it helps with the challenge of estimating the distributions using some samples (something that BHS is not good at while the f-divergences use optimization tools and are more flexible).

### Weaknesses
While the idea is interesting, the experimental setup does not show a big advancement in having locally concave functions, and one can see that WGAN is still outperforming the proposed method. Did the authors try to have some synthetic example that clearly shows the benefit of the pseudo f-divergence family?

On another note, I think the paper's writing could improve, particularly some details could help the reader. For example:
- Line 201, Equation 1 refers to a wrong equation, I believe the authors wanted to point to the equation line 196.
- Line 221, is the constant c, dependent on A? If yes, maybe the authors could specify that by writing $c_A$.
- Jumping from Eq. 2 to Corollary 4.4's result could seem surprising as it seems to be a jump from sup and inf to only sup. Checking the appendix, I believe explaining the relation between $T$ and $\tilde{T}$ would clarify this.
- Double Equation in line 431
- The images of Fig 2(a) are barely distinguishable. It would help if the authors could change the size of the image.

### Questions
The authors say that their framework helps with the high-dimensional sampling for Bayes Hilbert space distributions. I am not sure if I could follow how the proposed framework solves this problem. I would appreciate if the authors could elaborate on that.

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
4

### Summary
The paper proposes a new way to generalize $f$-divergence where the divergence-generating function may not be convex on the whole domain, which they coined as pseudo $f$-divergence. Furthermore, the authors provide a nice connection between the introduced pseudo $f$-divergence and the metric induced by the Bayes Hilbert Space. An illustration of using pseudo $f$-divergence in Bayes Hilbert space GAN demonstrates the potential usefulness of such a generalization.

### Strengths
1) The presentation of the submitted manuscript is very clear and its goals are well articulated.

2) Generalization of $f$-divergence and its close connection to Bayes Hilbert Space provides a nice insight as well as practically useful theory to extend existing Bayesian inferences, or probabilistic machine learning tasks.

3) Illustration of introduced methods in GAN further provides soundfulness of the established results.

### Weaknesses
No major weakness. Minor weakness below:

1) For the sake of improving the presentation, I would suggest reducing Section 1 and include more details about Bayes Hilbert Space in Section 3—for instance, the paragraph before 1.1 contributions (lines 64-72), the Second paragraph in Bayes Hilbert Spaces part in Section 1(lines 124-131), the second paragraph of section 1.3 (lines 156-160) all substantially overlap. One could summarize three paragraphs into one and just give a high-level depiction in the introduction and provide more details in Section 3 on Bayes Hilbert Space.

2) Many prepositions, or phrases missing in front of references. For instance, in lines 128-129, it is better to write "including" before you list the references. Or perhaps include references inside the brackets [ ].

3) In the Fenchel conjugate definition, I believe it should be x^Ty, not just xy.

### Questions
Thanks for the interesting work. Two questions I have are

1) I wonder if the authors could clarify how the pseudo-divergence could yield a new sampling approach at a high level. I understand that these could serve as an alternative approach to measuring the difference between distributions, but it's not clear to me if any sampling procedures can be based on them. Perhaps the more natural way to utilize this result would be variational inference, but I am not sure about the sampling strategies, so any clarification would help.

2) Could authors perhaps include any concrete example where the generalization of $f$-divergence significantly improved or robustified the performance of learning? Or at least, an extensive numerical comparison with the existing divergences to further gain insights (even for simple tasks).

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
3

### Summary
This work proposes novel connections between Bayes Hilbert spaces and a modified version of $f$-divergences (namely pseudo $f$-divergences) requiring $f$ to be concave on $[0,a)$ and convex on $[a,+\infty), a>0$ instead of convexity on all $[0,+\infty)$. More precisely. 

- Basic results and definition for both Bayes Hilbert spaces and $f$-divergences are recalled in Sections 2 and 3.
- Extensions of classical results of $f$-divergences for pseudo $f$-divergences are proposed in Section 4.1 
- Authors unveil a connection between a specific pseudo $f$-divergence and a Bayes Hilbert Space
- Experiments on GANs are proposed in Section 5, showing the pseudo $f$-divergence approach on a certain learning problem outperforms the classical $f$-GAN approach and matches the performance of Wasserstein GANs

### Strengths
- The three first sections are well-written and pedagogical.
- The theoretical connection of Section 4.2 looks strong and promising.

### Weaknesses
 - The precise nature of the contribution would gain to be clearer
- The experimental section is poorly written and does not exploit the flexibility provided by the proposed theoretical framework.

- Can you precise why the addition, multiplication and substraction in the Bayes Hilbert is well-defined only if we consider $B(\lambda)$ and not $\mathcal{M}(\lambda)$ ?
- You said in the abstract that your framework 'generalizes f -divergences by incorporating locally non-convex divergence-generating functions'. This should be clarified as, to my understanding of Section 4, you only consider a certain type of local non-convexity, being functions concave on $[0,a)$ and convex on $[a,+\infty)$? Do you think it is possible to consider functions $f$ with several areas of non-convexity, eg  a function convex on $[0,a], [b,c], [d,+\infty)$ and concave on $(a,b), (c,d)$?
- Experiments: can you please detail the nature of your experiment? It is not clear to understand what you are doing and why you are doing it?
- You mentioned in your intro (l.104) that in case of heavy-tail distribution, Wasserstein distance is unsuitable to modeling distributions with heavy-tails. Given that your experiments shows similar performances with WGAN, it seems that you do not consider heavy-tailed distributions, could you think of an experiment (even a toy one) with such a heavy-tailed measure where the WGAN would fail and your approach succeed?
- l 431 typo for 'equation'
- I find the nature of your theoretical contribution unclear: you claim that you are bridging the gap between Bayes Hilbert space and $f$-divergences. However, you are not creating such a link as you focus only on pseudo divergences, with $f$ concave on $[0,a], a>0$ and convex on $[a,+\infty]$ with $a>0$. As this does not encompass the case $a=0$ (ie the case of a true $f$-divergence, if we add a lower semicontinuous assumption), I don't know whether:
	1. the case $a=0$ has already been dealt with in the literature, then it would be good to precise such links more clearly and that your contribution is an extension of those links to the case of pseudo-divergences
	2. The case $a=0$ has not been previously considered, but you were only able to design theoretical links for pseudo $f$-divergences. In this case you are not truly reaching $f$-divergences
	In both cases, claiming that you are bridging the gap between Bayes Hilbert space and $f$-divergences seems inaccurate.

### Questions
- Can you precise why the addition, multiplication and substraction in the Bayes Hilbert is well-defined only if we consider $B(\lambda)$ and not $\mathcal{M}(\lambda)$ ?
- You said in the abstract that your framework 'generalizes f -divergences by incorporating locally non-convex divergence-generating functions'. This should be clarified as, to my understanding of Section 4, you only consider a certain type of local non-convexity, being functions concave on $[0,a)$ and convex on $[a,+\infty)$? Do you think it is possible to consider functions $f$ with several areas of non-convexity, eg  a function convex on $[0,a], [b,c], [d,+\infty)$ and concave on $(a,b), (c,d)$?
- Experiments: can you please detail the nature of your experiment? It is not clear to understand what you are doing and why you are doing it?
- You mentioned in your intro (l.104) that in case of heavy-tail distribution, Wasserstein distance is unsuitable to modeling distributions with heavy-tails. Given that your experiments shows similar performances with WGAN, it seems that you do not consider heavy-tailed distributions, could you think of an experiment (even a toy one) with such a heavy-tailed measure where the WGAN would fail and your approach succeed?
- l 431 typo for 'equation'
- I find the nature of your theoretical contribution unclear: you claim that you are bridging the gap between Bayes Hilbert space and $f$-divergences. However, you are not creating such a link as you focus only on pseudo divergences, with $f$ concave on $[0,a], a>0$ and convex on $[a,+\infty]$ with $a>0$. As this does not encompass the case $a=0$ (ie the case of a true $f$-divergence, if we add a lower semicontinuous assumption), I don't know whether:
	1. the case $a=0$ has already been dealt with in the literature, then it would be good to precise such links more clearly and that your contribution is an extension of those links to the case of pseudo-divergences
	2. The case $a=0$ has not been previously considered, but you were only able to design theoretical links for pseudo $f$-divergences. In this case you are not truly reaching $f$-divergences
	In both cases, claiming that you are bridging the gap between Bayes Hilbert space and $f$-divergences seems inaccurate.

### Soundness
3

### Presentation
3

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
This paper introduces a new loss for GANs, which builds on a connection between so-called Bayes Hilbert spaces and pseudo f divergences. First, Bayes Hilbert space are introduced, which is a linear space with additive and multiplicative structure coherent with Bayes theorem. Then, pseudo f divergences, which do not require f to be convex everywhere are introduced. The main part is that for a certain choice of f. the pseudo f divergence can be written as a sum of the BHS norm and some other 'entropy' term. Then, it is verified numerically, how well this certain choice of GAN performs in image generation.

### Strengths
The paper deals with a niche topic, but does it so very nicely. The definitions and theorems are perfectly clear, although I did not check the proofs. The connection between pseudo f divergences and Bayes Hilbert spaces is very interesting. The paper comes with code and seems reproducible. It is also nice that the paper rediscovers the log variance loss used in Richter et al and motivates it more theoretically.

### Weaknesses
1) My biggest problem apart from some nitpicks is that I do not really see the point of all this formalism. It is nice that there is an intrinsic connection between pseudo f divergences and Bayes Hilbert spaces, but there are no additional insights based on that. One could just introduce pseudo f divergences and use the specific f. One thing that seems a bit odd and might yield additional insights is that in Lemma 4.5, there is an additional entropy like term. Does this give any other interpretation?

2) Numerically, the results are okayish, mostly due to the use of the GAN algorithm. Unfortunately GANs suffer from many problems: unstable training, mode collapse,... Did you find if your loss alleviates some of these problems? 

3) The interpretation of the numerical results is also a bit bold: The difference between WGAN and BHS-GAN "is on a par", while the BHSGAN "outperforms traditional f-GANs". Looking at the table, f-GANs (Pearson) are 2 FID away from BHS-GAN, so I would say there is not really anything conclusive about outperforming. In particular, the table states that the results are "over 100 seeds", which i interpret as you draw with one trained model a lot of images and calculate the FID and average this 100 times? Then, to say anything conclusive, one should try to get different training runs. However, I see this paper more of a theory paper and therefore I would suggest to tone the claims a bit down.

### Questions
1) Can the connection between Bayes Hilbert spaces and f divergences be leveraged for other generative models? (GANs are not in fashion anymore, due to well-known stability, mode collapse and interpretability reasons). Many generative models have a loss that can be bounded via the KL. I guess this goes in the direction of Richter et al.?

2) Bayes Hilbert spaces are introduced as they adhere to the structure of Bayes theorem, i.e., the likelihood is the radon nikodym derivative of posterior with prior. Can you somehow use these ideas to reformulate the distance between posterior and generation measure in terms of BHS losses?

### Soundness
3

### Presentation
3

### Contribution
2
