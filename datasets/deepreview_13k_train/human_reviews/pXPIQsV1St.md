# Dynamical Similarity Analysis uniquely captures how computations develop in RNNs

- Decision: Reject
- Scores: 5, 5, 8, 3

## Abstract
Methods for analyzing representations in neural systems have become a popular tool in both neuroscience and mechanistic interpretability. Having measures to compare how similar activations of neurons are across conditions, architectures, and species, gives us a scalable way of learning how information is transformed within different neural networks. In contrast to this trend, recent investigations have revealed how some metrics can respond to spurious signals and hence give misleading results. To identify the most reliable metric and understand how measures could be improved, it is going to be important to identify specific test cases which can serve as benchmarks. Here we propose that the phenomena of compositional learning in recurrent neural networks (RNNs) allows us to build a test case for dynamical representation alignment metrics. By implementing this case, we show it enables us to test whether metrics can identify representations which gradually develop throughout learning and probe whether representations identified by metrics are relevant to computations executed by networks. By building both an attractor- and RNN-based test case, we show that the new Dynamical Similarity Analysis (DSA) is more noise robust and identifies behaviorally relevant representations more reliably than prior metrics (Procrustes, CKA). We also show how test cases can be used beyond evaluating metrics to study new architectures. Specifically, results from applying DSA to modern (Mamba) state space models, suggest that, in contrast to RNNs, these models may not exhibit changes to their recurrent dynamics due to their expressiveness. Overall, by developing test cases, we show DSA's exceptional ability to detect compositional dynamical motifs, thereby enhancing our understanding of how computations unfold in RNNs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The work studies a recently proposed "Dynamical Similarity Analysis" (DSA) and benchmarks it against prior methods such as Centered Kernel Alignment (CKA) and Procrustes for analyzing the dynamical representations within neural networks, particularly in Recurrent Neural Networks (RNNs). Through systematic test cases that simulate both noise and compositional learning, the study argues that DSA provides a more robust and behaviorally relevant measure of dynamical alignment compared to established metrics like . Furthermore, the paper explores DSA’s application to new architectures such as Mamba models, suggesting that their internal dynamics operate differently from RNNs.

### Strengths
- The designed benchmark is novel and much needed to bridge the fields of computational neuroscience and mechanistic interpretability. Even though both fields look at similar problems, their languages have been very distant from each other for some time. I believe this work is a necessary step towards bringing them closer.

- The study of compositional learning in this context, as far as I am aware, is quite novel as well.

### Weaknesses
 - The biggest weakness is the missing methods section. I see there is a supplementary file (which can be at the end of the original submission as an appendix), but this file does not contain the necessary information to reproduce these experiments. As a rule of thumb, by reading the methods section, without looking at the specific code, one should be able to reproduce the work. The public code is to help facilitate the process of reproduction, but is not a substitute for the writing. For example, what were the learning rates? How long were networks trained etc.? 

 - Though [1] is cited, I would have loved to see the method of finding and identifying the fixed points for categorizing the similarity of computation between RNNs as a baseline. I understand that not all problems will be solved by fixed points, but it is needed to show that DSA CAN recover the computational structure as efficiently in the benchmarks of [1]. For example, you can consider the 3-bit flip flop task and/or the sine generation task, in which we know the solutions and therefore can test whether DSA would be as effective as the fixed-point finders.

### Questions
I believe I understood most of the work adequately. My score is based on the current submission and the weaknesses described above. If you can address them, it is likely that my score will increase to match the strengths I described above. 

[1] Maheswaranathan, Niru, et al. "Universality and individuality in neural dynamics across large populations of recurrent networks." Advances in neural information processing systems 32 (2019).

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper has two main contributions. First, the authors suggest a benchmark framework in which to evaluate dynamic similarity metrics. Second, they use this framework to compare three specific metrics: Procrustes, CKA and DSA. They conclude that DSA is the best one. Finally, applying DSA to a more recent architecture MAMBA, they report little change to the dynamical component through training.
Specifically, the benchmark has two parts. The first is sampling from noisy ODEs and comparing between different noisy versions. The expectation is that the metric will be robust to noise, but capture genuine differences in the non-noisy dynamics. Further, when combining data from two ODEs, the authors expect a specific form of linearity.
The second part is using trained RNNs on a compositional task. Here the authors ask whether pretraining or constrained training induces representational similarities that are expected by task structure. These expectations are what makes RNNs a benchmark: task structure should induce similarity structure.

### Strengths
The paper addresses an important problem – comparing dynamical systems. It is valuable both for neuroscience and potentially for ML (e.g. MAMBA and other state space models). With the introduction of new metrics, there is a need for benchmarks to evaluate such metrics.
Using RNNs in a systematic manner is a good and original approach for achieving such a benchmark.
The authors simulate a large number of networks, while changing training schedule or task composition in a very systematic manner. This provides opportunities for teasing apart subtle differences between various metrics.

### Weaknesses
The results are somewhat preliminary. In particular, there are no insights or proofs on why there are differences between the metrics. The benchmark itself is rather qualitative.


1.	The paper lacks more rigorous expectations on how the benchmark results should look like. Why should we expect linearity in the attractor case? The RNN expectations are somewhat crude, as they only dictate whether one group is more dissimilar than another (also see point 2).
2.	All comparisons in the RNN are to the master network, and yet conclusions are drawn regarding their similarity to each other.
3.	Clarity of writing can be improved. There were several places where it was quite hard to understand what exactly was done.


4.	If this benchmark is widely used, and metrics are optimized to be good at it. Will they be good metrics? In other words, how can we be sure that passing this benchmark generalizes to the broader objectives of metrics? 
5.	The objectives of metrics are not fully elaborated. There is some mention of ratios, but this is not fully developed. This is not a trivial question, and not necessarily easy to answer. But it should be properly discussed in a paper suggesting benchmarks.
6.	The writing in the results section 4.1 is a bit jumpy. Definition of ratio. Then noise.
7.	Does the ‘+ and ‘1/2’’ notation in Fig 2a represent numerical addition and scaling, or a union of data sets from A/B/noise with different ratios? The main text (and appendices) failed to clarify this crucial point making subsequent results difficult to interpret with confidence.
8.	Results in Fig 3G are interesting. Why Procrustes and CKA can’t discriminate the untrained network? Is it possible that they do discriminate it, but because we are only measuring dissimilarity to the master, we can’t see it?
9.	Why do you compare groups and not individual networks?
10.	“The relative relevance of Attractor B” – number of trials? Amplitude?
11.	The Untrained network is a good control to have, as it illustrates how statistics of input can dominate dynamics and similarity measures.
12.	 Violin plots could be more informative than bars in the various plots.
13.	Figure 3: the expectations cartoon is confusing. The grey and purple have a specific order, despite the text saying they are expected to be the same. Furthermore, the order in the actual plots is opposite.
14.	The DSA paper uses dimensionality reduction and classification to quantify distances between networks. It could be useful to visualize all networks of figure 3 using multi dimensional scaling as in that paper. For instance, that might help understand whether pretrained networks are really similar to untrained networks (in CKA and Procrustes), or are simply equally distant from the master.
15.	Figure 4 – why are the values at 0 accuracy difference so distant from zero? Shouldn’t this include networks that are almost identical?
16.	Lines 429-431: are purple and green in the figure?
17.	Line 431: the pattern is inverted for zero percent. What about the decline from 70% training to 100% training?
18.	Line 467 “This means that all training groups produce roughly the same dynamics” – can this conclusion be reached when only comparing models to master, and not one to another?


### Questions
4.	If this benchmark is widely used, and metrics are optimized to be good at it. Will they be good metrics? In other words, how can we be sure that passing this benchmark generalizes to the broader objectives of metrics? 
5.	The objectives of metrics are not fully elaborated. There is some mention of ratios, but this is not fully developed. This is not a trivial question, and not necessarily easy to answer. But it should be properly discussed in a paper suggesting benchmarks.
6.	The writing in the results section 4.1 is a bit jumpy. Definition of ratio. Then noise.
7.	Does the ‘+ and ‘1/2’’ notation in Fig 2a represent numerical addition and scaling, or a union of data sets from A/B/noise with different ratios? The main text (and appendices) failed to clarify this crucial point making subsequent results difficult to interpret with confidence.
8.	Results in Fig 3G are interesting. Why Procrustes and CKA can’t discriminate the untrained network? Is it possible that they do discriminate it, but because we are only measuring dissimilarity to the master, we can’t see it?
9.	Why do you compare groups and not individual networks?
10.	“The relative relevance of Attractor B” – number of trials? Amplitude?
11.	The Untrained network is a good control to have, as it illustrates how statistics of input can dominate dynamics and similarity measures.
12.	 Violin plots could be more informative than bars in the various plots.
13.	Figure 3: the expectations cartoon is confusing. The grey and purple have a specific order, despite the text saying they are expected to be the same. Furthermore, the order in the actual plots is opposite.
14.	The DSA paper uses dimensionality reduction and classification to quantify distances between networks. It could be useful to visualize all networks of figure 3 using multi dimensional scaling as in that paper. For instance, that might help understand whether pretrained networks are really similar to untrained networks (in CKA and Procrustes), or are simply equally distant from the master.
15.	Figure 4 – why are the values at 0 accuracy difference so distant from zero? Shouldn’t this include networks that are almost identical?
16.	Lines 429-431: are purple and green in the figure?
17.	Line 431: the pattern is inverted for zero percent. What about the decline from 70% training to 100% training?
18.	Line 467 “This means that all training groups produce roughly the same dynamics” – can this conclusion be reached when only comparing models to master, and not one to another?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper demonstrates that Dynamical Similarity Analysis (DSA), a recently introduced metric for comparing dynamical systems, outperforms related techniques such as Procrustes and CKA. DSA operates by projecting system trajectories into a high-dimensional space, where the vector fields governing the dynamics become approximately linear. It then aligns the two vector fields through an orthogonal transformation. The authors show that DSA consistently outperforms CKA and Procrustes across all tested tasks and suggest that DSA may be uniquely capable of capturing the computational processes underlying the tasks.

### Strengths
This paper is timely and addresses an important challenge in neuroscience and AI: comparing dynamic trajectories across neural systems. The paper makes a nice contribution by empirically evaluating several widely used techniques for comparing dynamical trajectories and identifying the most effective one as DSA. The comparisons appear to me to be done fairly and objectively.

### Weaknesses
The paper is at times quite hard to read, in particular when the authors are describing the tasks. The paper would benefit from a streamlining of the explanations of the experiments. Also (as I'll argue below), the title is a bit misleading, and should be changed to reflect the actual contributions of the paper.

- The title suggests that you have shown/proved that DSA is unique among all similarity metrics in its ability to capture how computations evolve. You have not shown this. In reality, you have shown that DSA is better at two other metrics on a range of tasks. This is still an important contribution, but the title should be toned down to reflect the actual contributions of the paper. 
- Is the appendix missing? There is a reference to it (L152), but it doesn't appear to go anywhere. 
- L118: "... the momentum of traces in instead of..." I'm not sure what this is trying to say.

### Questions
- The title suggests that you have shown/proved that DSA is unique among all similarity metrics in its ability to capture how computations evolve. You have not shown this. In reality, you have shown that DSA is better at two other metrics on a range of tasks. This is still an important contribution, but the title should be toned down to reflect the actual contributions of the paper. 
- Is the appendix missing? There is a reference to it (L152), but it doesn't appear to go anywhere. 
- L118: "... the momentum of traces in instead of..." I'm not sure what this is trying to say.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors investigate how three metrics, Dynamical Similarity Analysis (DSA), Procrustes distance, and linear Centered Kernel Alignment (CKA), quantify diffferences in RNN dynamics. They attempt to provide benchmarks, which illustrate favorable properties of DSA over the other two.

### Strengths
I think the intent and framing of the paper in the introduction is well written. The topic is interesting. Unfortunately, I have serious concerns about the execution of the project as outlined below.

### Weaknesses
This paper does not present a new technique or method, but is rather aiming to deepen our understanding of existing metrics. I really like this idea, but in my mind it means that the paper needs to be impeccably written and ideally involves some concrete mathematical results or guarantees about the methods being compared. I think the paper does not succeed on these terms and therefore does not meet the bar for publication at ICLR at its current level of polish and detail.

Let me summarize major weaknesses briefly:

* There are many places where the authors claim that there is an "expected" result that aligns with what DSA shows, but why these things are "expected" is not clearly described. I suspect that what one "expects" in many of these cases is debatable.
* The test cases shown are bespoke. It is not clear whether any of this generalizes to a broader variety of settings. There is also a relatively small number of tasks considered. I think they consider roughly 2-3 tasks, most being variants of Driscoll et al's study. In comparison, [Klabunde et al.'s recent benchmark](https://arxiv.org/abs/2408.00531) considers six different tests across six different datasets.
* There is a relatively small number of metrics considered. The authors consider three (DSA, CKA, and Procrustes). In comparison,  Klabunde et al's study linked above contains 23 similarity measures.
* Related to the point above, Procrustes and CKA were never meant to be applied to dynamical time series so the comparison seems a little unfair and expected that DSA comes out "ahead" in certain respects. At the same time, the authors do not include Diffeomorphic vector field alignment as a comparison to DSA (even though they do cite it). Additionally, I would point the authors to stochastic shape distances as a viable metric for comparing dynamical flow fields: [Lipshutz et al. (2024)](https://openreview.net/forum?id=Fykvxdv2I8)
    * For these reasons, the claim that "DSA **uniquely** captures" anything seems unjustified! I would only say that a method *uniquely* captures something if I had a mathematical proof that no other approach could work.


Below I unpack some of these weaknesses further with a bit more specificity:

* Regarding Fig 2C, there is no clear motivation why we would want a metric to respond "ratio-like" when we combine attractors. Furthermore, DSA only has marginally better linear R^2 (0.99 vs 0.97 or 0.96), yet this is somehow treated as a "win" for DSA over these other measures. 
* Regarding Figure 3, the authors use the term "normative predictions" multiple times in relation to Driscoll et al.'s modeling work. I strongly encourage the authors to rephrase this. A normative model has a very specific meaning in theoretical neuroscience -- it involves predicting an attribute of a network on the basis of some functional or evolutionary principle (efficient coding is a classic example, see for e.g. [Mlynarski & Hermundstad, 2021](https://www.nature.com/articles/s41593-021-00846-0)). Driscoll et al. never use the term "normative model" in their paper and it is confusing to see the term applied here.
* Moreover, I am hestitant to treat the results of Driscoll et al. &mdash; which, while interesting, is only one empirical study of a very specific family of RNN tasks &mdash; as a foundational way to benchmark metrics on neural representations. The authors state at the conclusion of this section that "DSA is the only metric with correctly identifies the compositional representation that we expect." But it is not well explained what I should "expect" to see, and I suspect that what one "expects" to see could be debatable. In any case, the panel corresponding to DSA in Fig 3G does not seem to do a good job distinguishing the final 3-4 categories (only the yellow box plot seems substantially higher than the rest).
* The horizontal axis in Figure 2 is confusing. Epochs often refer to training epochs. The horizontal axis should be labeled "noise" or something similar.
* How noise impacts the simulation in Figure 2 is unclear. The authors don't show, for example, trajectories of neural firing rates. Also why plot only three levels of noise rather than a more fine scale grid?

### Questions
None

### Soundness
1

### Presentation
2

### Contribution
2
