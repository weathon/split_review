# Exploring mechanisms of Neural Robustness: probing the bridge between geometry and spectrum

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 3, 3, 6

## Abstract
Backpropagation-optimized artificial neural networks, while precise, lack robustness, leading to unforeseen behaviors that affect their safety. 
Biological neural systems do solve some of these issues already.
Thus, understanding the biological mechanisms of robustness is an important step towards building trustworthy and safe systems.
Unlike artificial models, biological neurons adjust connectivity based on neighboring cell activity. 
Robustness in neural representations is hypothesized to correlate with the smoothness of the encoding manifold. 
Recent work suggests power law covariance spectra, which were observed studying the primary visual cortex of mice, to be indicative of a balanced trade-off between accuracy and robustness in representations.
Here, we show that unsupervised local learning models with winner takes all dynamics learn such power law representations, providing upcoming studies a mechanistic model with that characteristic.
Our research aims to understand the interplay between geometry, spectral properties, robustness, and expressivity in neural representations.
Hence, we study the link between representation smoothness and spectrum by using weight, Jacobian and spectral regularization while assessing performance and adversarial robustness. 
Our work serves as a foundation for future research into the mechanisms underlying power law spectra and optimally smooth encodings in both biological and artificial systems. 
The insights gained may elucidate the mechanisms that realize robust neural networks in mammalian brains and inform the development of more stable and reliable artificial systems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
### Summary

The authors conducted a series of carefully designed analyses on 2-layer NN models trained by hopfield-like local learning rules vs backpropagation with regularization, and they examined their representation spectra, local manifold geometry, decision boundary and robustness to white box attack. Through the analyses, they found the networks learned through local biologically plausible learning rules are indeed robust and have "optimal" spectra, while some other models trained via backprop can also achieve comparable robustness without the 1/n spectra, questioning the necessity of this 1/n spectral feature.

### Strengths
### Strength

- The detailed dissections of these models are ****applaudable.****
- Providing evidence that the 1/n spectrum of the representation is not necessary for model robustness, (though the evidence is relatively few data points) .
- The latent geometry analysis and its relation to decision boundary is illuminating, esp. by showing the similarity of KH model and L2 and Jacobian regularization model.
- Figures are well made, clean and easy to understood.

### Weaknesses
### Weakness

- The biggest issue maybe the paper at its current stage is kind of explorative data analysis in many directions—— so I’m not sure about the central contribution and conclusion. The 1/n spectrum, the geometry of represntation and decision boundary and adversarial robustness are all interesting, but currently they have not connect to form an overall story. It will be better to form a few central claims and then back it up with experiments and data.
- The writing and overall organization of the paper could be improved…
    - In the method section, it will benefit from a more streamlined organization. Currently it’s jumping between method, results and some interpretations…. Some paragraph (Figure 1 and its interpretation) should go to the results section. Adding headings e.g. paragraph titles can also help. e.g. model architecture, unsupervised training, supervised training, spectral analysis etc.
    - Similarly in the result section, better headings for the experiments could be added to guide the readers.
- Generally the paper’s experiment is relatively small scale, majorly with 2 layer MLPs. The generalization to deeper networks or CNNs is desirable for bigger impact.
- For the decision boundary and  analysis, it may be worthwhile to refer to some previous works.
    - For example, the Frob norm of jacobian plot vs the decision boundary is interesting, and [1] devotes the whole paper to understand this. The technical difference is they plotted the volume element, which is the sum of log eigenvalues, instead of sum of squared eigenvalues in your case.
    - Though outside image classification, for GAN networks, [2] analyzed the homogeneity / flatness of the Jacobian eigenframe across the space. which maybe useful for quantification in your case.

[1]: ****Neural networks learn to magnify areas near decision boundaries****  https://arxiv.org/abs/2301.11375 

[2]: ****The Geometry of Deep Generative Image Models and its Applications**** https://arxiv.org/abs/2101.06006  

### Minor Weakness and typos

- “*Because principal components correspond to the eigenvectors of the respective*
*covariance matrix Cov(h,h)*” should it be $\hat{h},\hat{h}$ ?
- In Figure 2 and Figure 3, what does different color shades mean? is it different runs of the model?
- The notation in Eq. 9 in appendix is not clear, $D$ seems to mean differential operator, but it’s not standard and not defined anywhere, using partial differential or more standard notation may be easier for reader.
- Eq. 10 in appendix is also confusing or even wrong. $\sigma’(Wx)$ seems to be a vector, how do you take the absolute value and time it with the L2 norm of $W$? Are you using some special properties of $\sigma$?
- What is *SHLP?*

### Questions
### Questions

- The decision landscape analysis is super interesting, but also quite local and qualitative, do you have more quantitative population statistics for them?
- **Comments:** 
Covariance spectrum is a quite global measure of representation; on the other hand, the jacobian norm and adversarial property are super local property [3], so it makes sense that controlling the spectrum is not enough for getting adversrial robust…

[3]: **[Adversarial training is a form of data-dependent operator norm regularization](https://proceedings.neurips.cc/paper/2020/hash/ab7314887865c4265e896c6e209d1cd6-Abstract.html)**

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper seeks to investigate the relationship between the smoothness of the representation and the spectra of its covariance matrix.  

I found the paper to be not particularly well organized, and somewhat difficult to follow. While the paper described a series of analyses, these analyses are overall preliminary. There is not a clear key result emerging from these analyses that would fundamentally change our understanding of the problem. In sum, I feel that while the question studied in the paper is potentially interesting, the results need to be substantially strengthened.

### Strengths
— Understanding the robustness of the representation is an important problem.
— The attempt to leverage insights from neuroscience to improve machine learning algorithms should be applauded.

### Weaknesses
- The main problem that I see with the current version of the paper is that there isn’t a clear and impactful result reported in the paper. 

- The presentation is not particularly well organized and needs major improvements. The descriptions of the analyses and results are messy. 

- Various statements are not rigorous. For example, the paper stated, “biological neurons adjust connectivity based on neighboring cell activity”. What is the evidence for this? Also, the brain has abundant long-range connections.

- The paper is motivated by Stringer et al (Nature, 2019). However, the interpretation of their results seems to be somewhat misleading. The paper stated “They prove that this smoothness is linked to the functional form of a power law decay in the manifold’s covariance spectrum. In particular, balancing accuracy and robustness, a sweet spot lies close to a 1/n power law, with n denoting the index of the ordered spectral component. ” But I don’t think Stringer et al 2019 proved a connection between the 1/n spectrum with the robustness. It was a conjecture described in the last paragraph of that paper. Also, Stringer et al predict different power-law relationships depending on the properties of the stimulus set (e.g., natural scene v.s. gratings). It is unclear whether the current results are consistent with theirs.

### Questions
-- It would be helpful if the paper could be systematically revised to make the analysis more systematic and the key points more clear. 

-- What is the point of the left panel of Fig 1c? The pruned version mainly differed from the Raw in the power of the first few components while the scaling-law concerns the properties of the tails. So I am not sure why this difference would matter for the scaling-law. 

-- The analysis in Fig 4 is interesting. But it’s just one example. Would there be a systematic way to quantify this?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors investigate whether a neural network trained on CIFAR with biologically inspired local learning rules contains activations with a power-law-like spectrum, which has been proposed as a property of biological systems. They compare this network to others trained with spectral regularization and Jacobian regularization, which explicitly induce power-law-like spectra in the network. The adversarial robustness of these networks is also investigated.

### Strengths
The authors' experiments bridge many lines of work in machine learning and neuroscience. The question of power-law spectra in biological and artificial neural networks is topical and of interest to neuroscience and machine learning practitioners interested in adversarial robustness.

### Weaknesses
1) The paper is difficult to follow. In some places, there are many methodological details presented, but the experiment hypothesis and conclusions need to be better described. In general, the writing could be clearer and more precise. 
2) Many of the experiments seem preliminary, which makes it hard to draw conclusions. For instance, the authors state in the discussion “we could not reproduce Nassar et. al. (2020)’s results, probably due to the differences in our modeling choices”, and in the appendix “most of our results suggest that we might have made sub-optimal choices in our methods regarding competitive results with spectral regularizers”. While I appreciate the authors being honest about these limitations, this leaves more questions than answers. What would change if models were made that *did* reproduce these previous results? Is there something fundamentally non-reproducible about the previous work? This makes the presented results difficult to interpret, and in the words of the authors “we ought to be cautious with generalizing them beyond the scope of this work”. 
3) There was not enough relation to previous literature. For instance, the authors motivate adversarial robustness with an example from cancer diagnosis, but there are many papers in the NeuroAI world that have directly looked at the robustness of models compared to human observers. This seems like it would be more relevant to the neuroscience audience that this paper is targeted towards. I encourage the authors to look at this work (some places to start would be Geirhos et al. 2018, Geirhos et al. 2021, Guo et al 2022, Harrington et al. 2022, Feather et al. 2023 but there are many many more). 
4) Minor: The citation format in the text seems to be incorrect with missing “()” around the text citations.
5) Minor: In the first two sentences of section 3.2 the authors state that Figure 3 shows the spectrum of the KH layer, but this is not in Figure 3 (although it is in Figure 2).

### Questions
a) The authors introduce the acronym “BNN” and refer to these as “models.” When the authors refer to “BNNs” are they talking about true biological systems or models of biological systems? “BNN” is not a common acronym to my knowledge. 

b) How do the authors handle the fitting for the “alpha” value? In Stringer et al. I believe that the first few and last few eigenvalues are ignored. How does that play into the fitting here? 

c) Which points (scales) are used for fitting the alpha value in Figure 2? Additionally, the different colored dots are not defined in the plot. A legend should be included. 

d) It would be helpful to show the non-normalized robustness plots. Because the clean performance significantly differs these are hard to interpret as shown. 

e) Figure 4 is interesting, however the statements about “smoother” decision landscapes should be quantified if one is to directly compare the results to the adversarial robustness curves.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper analyses the robustness of Krotov-Hopfield networks to noise by analyzing the eigenvalue spectrum of their internal representations. They find that it naturally produces a power-law spectrum, as had been observed in the brain by Stringer et al.

### Strengths
This study provides some useful information on the robustness of the Krotov-Hopfield model

### Weaknesses
The question of robustness and eigenvalue spectra is certainly interesting, but the focus on the KH model limits the impact of this work.  The study would have been stronger with a more general analysis of this for several learning rules.  For example, the KH model generates its hidden layer in a unsupervised manner.  Do other unsupervised rules act similarly?  There is some analysis of multiple rules in Figure 5, but not much in the way of a general theory, and the paper would have been stronger with more of this.

### Questions
There are two papers cited by Krotov and Hopfield, but you don’t always say which one you are referring to.  Please distinguish them by adding a year every time!

The matrix S is not clear.  What does “synaptic adjacency” mean?  Is it defined by W=S ||S||^p-2?   Also the norm ||S|| is not defined.  Do you actually mean absolute value |S|?

\lambda means learning rate in equation (4) but covariance eigenvalue in figure 1c.

What are the multiple curves in Figure 2?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
