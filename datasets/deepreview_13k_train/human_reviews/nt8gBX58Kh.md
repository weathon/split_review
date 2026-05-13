# Neuron-based Multifractal Analysis of Neuron Interaction Dynamics in Large Models

- Decision: Accept
- Scores: 6, 8, 5

## Abstract
In recent years, there has been increasing attention on the capabilities of large models, particularly in handling complex tasks that small-scale models are unable to perform. Notably, large language models (LLMs) have demonstrated ``intelligent'' abilities such as complex reasoning and abstract language comprehension, reflecting cognitive-like behaviors. However, current research on emergent abilities in large models predominantly focuses on the relationship between model performance and size, leaving a significant gap in the systematic quantitative analysis of the internal structures and mechanisms driving these emergent abilities. Drawing inspiration from neuroscience research on brain network structure and self-organization, we propose (i) a general network representation of large models, (ii) a new analytical framework — *Neuron-based Multifractal Analysis (NeuroMFA)* - for structural analysis, and (iii) a novel structure-based metric as a proxy for emergent abilities of large models. By linking structural features to the capabilities of large models, NeuroMFA provides a quantitative framework for analyzing emergent phenomena in large models. Our experiments show that the proposed method yields a comprehensive measure of network's evolving heterogeneity and organization, offering theoretical foundations and a new perspective for investigating emergence in large models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a new metric to capture emergence within a network by analyzing the structure of neurons within the network. The score depends on the width and peak of the multifractal spectrum overall quantifying the variance in the local structure of the network. This metric is shown to correlate with metrics depending on the behavior of the model, which have traditionally used to measure emergence.

### Strengths
1. Writing is clear, explains the new metric clearly.
2. Moving the discussion away from only scaling model size is important
3. The metric is well defined, making it replicable.

### Weaknesses
1. Text in Fig 1 is very small making it hard to read and there is a lot of white space that can be used to increase text size.
2. "While our NeuroMFA framework demonstrates correlations between the emergence metric and
downstream performance by studying the self-organization of LLMs, it has not yet established a
clear causal relationship. Future work should focus on identifying specific linguistic phenomena
captured by LLMs and demonstrating how our analysis methods can reveal the learning process of
these phenomena during training, thereby establishing a stronger causal connection." This should be in the main paper.
3. While figure 6 shows the correlation between this metric and previous ones (based on the behavior), I find little reason to use this metric over the behavior (encoded by the previous metrics) of the model itself. At best this metric is correlated with those behavioral methods, at worst they disagree where the behavior would still be more convincing.
4. We see no reason why this property isn't just linked to a further amount of training. For example, if there is a dataset that when an LLM is trained on it, there is a low performance on the behavior based metrics would we still expect to see the proposed metric increase?
5. In figure 6 as the accuracy goes up, the proposed metric increases (across models). This is no longer always true in Appendix D.2. For example in fig 19, the 410M model has lower performance but the proposed metric is higher than both the 1B and 1.4B models. This makes sense as the score is normalized with initial training but then you cannot compare across models. This is possible for all of the traditional behavioral metrics. 
6. Fig 8 shows that the scores are lower in the beginning of training than the end for all metrics, and that the model size is only recovered at the later end. How does this address the problem in Fig 1b? As the other metrics have a similar low score after 500 epochs do they also not only rely on the model size?

Overall it is unclear to me the benefit that this metric provides, especially when the paper itself acknowledges that the metric is only validated through its correlation.

### Questions
1. What are the behaviors for Pythia 14m and 31m fig 6? Do they also agree with Lambada/PIQA?
2. Are there examples where the performance on behavioral metrics decreases significantly and the proposed metric also decreases?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
In this paper the authors ask the question, is there a better metric than raw parameter number to capture why qualitatively new skills develop when scaling up large transformer models. They introduce the network structural / topological measure of ‘NeuroMFA’ and show that this measure can capture how skills develop throughout training, something which raw parameter numbers necessarily cannot capture. They propose that their measure introduces a new way of studying learning of skills across time in large scale neural network architectures.

### Strengths
I genuinely enjoyed reading this paper. It introduces a new measure to study the training of LLMs that I have not seen in this way before. The paper generally is very thorough in its analyses / experimentation. I am sure this will be work that is of interest to the ICLR community.

### Weaknesses
*Baseline calculation*

This is my only comment about a possible analysis to add. As you are proposing a new measurement, I think it would be helpful to provide measurements in untrained networks. Of course, Figure 8 shows the effect of training on the metric, but I wonder whether it actually would be zero across all models at the start of training? If it isn’t, should be somehow standardise the metric so that it is zero before training? If this was explore in more detail I would be happy to raise my ‘soundness’ rating to ‘excellent’.

*Communication of methods*

Given the number of results in this paper and the resulting length of the appendix, I think the authors should really aim to communicate the core information in the main text. I think the following would help:

- Given that you use transformers with attention, I imagine the author analyse the effective interaction of model parts conditioned on specific dataset. Naturally the attention weights are going to change how different parts of the models interact and so it seems one could not analyse the structure of the attention weights in general but instead would look at the effective communication when processing specific samples? Or do authors actually just use the weights? It would be great if this could be clarified, ideally at the start of the methods.
- I think I generally got the metric development, but I did find it somewhat hard to follow. I wonder whether this could be improved if every new part of the method introduced would start with a sentence or two on the high-level intuition behind the measure / what the current analyses step is for – take section 3.2 for example. It starts with “To perform multifractal analysis of LLMs, we extend the box-covering and box-growing methods (Song et al., 2005; Evertsz & Mandelbrot, 1992; Salat et al., 2017; Xiao et al., 2021) to capture the local neuron-based fractal properties of NINs.”, followed by plenty of details on methods. If you lead into this section by first giving the reader an idea why it is interesting to decompose the graph into fractals in the first place, then maybe this would be easier to follow. Generally speaking, motivate the method before jumping into details. I know that the paper is already on the page limit but frankly the appendix is so long, moving a bit more of the methods to appendix in lieu of giving readers a better intuition in the main text is probably beneficial.
- Given there already is a bunch of structural measures which have successfully been used for structural analyses in neuroscience and neural network models (e.g. standard ones like modularity / small worldness, or entropy-based ones or Ricci curvature) I wonder whether authors could somehow motivate why their new measure was needed? Given it works, I do not want to say that the new measure was not needed but I would be curious to know why they specifically took the route they took with the development of the metric.

*Stylistic choices*

- I think the font on Figure 6 is very close to unreadable small.
- Across figures, could you either use a serif or sans serif font but not mix that up?
- I wonder whether your strong emphasize of the word ‘emergence’ is actually needed and helpful in communicating your results? In my experience it does put off some researchers and, as you make a link to neuroscience, the development of language and reasoning skills from a newborn to a teenager would simply be considered as part of ‘development’ and ‘learning’. So, I wonder whether you want to deemphasize the concept of emergence a bit here and just call it ‘the development of skills’?

### Questions
*Baseline calculation*

This is my only comment about a possible analysis to add. As you are proposing a new measurement, I think it would be helpful to provide measurements in untrained networks. Of course, Figure 8 shows the effect of training on the metric, but I wonder whether it actually would be zero across all models at the start of training? If it isn’t, should be somehow standardise the metric so that it is zero before training? If this was explore in more detail I would be happy to raise my ‘soundness’ rating to ‘excellent’.

*Communication of methods*

Given the number of results in this paper and the resulting length of the appendix, I think the authors should really aim to communicate the core information in the main text. I think the following would help:

- Given that you use transformers with attention, I imagine the author analyse the effective interaction of model parts conditioned on specific dataset. Naturally the attention weights are going to change how different parts of the models interact and so it seems one could not analyse the structure of the attention weights in general but instead would look at the effective communication when processing specific samples? Or do authors actually just use the weights? It would be great if this could be clarified, ideally at the start of the methods.
- I think I generally got the metric development, but I did find it somewhat hard to follow. I wonder whether this could be improved if every new part of the method introduced would start with a sentence or two on the high-level intuition behind the measure / what the current analyses step is for – take section 3.2 for example. It starts with “To perform multifractal analysis of LLMs, we extend the box-covering and box-growing methods (Song et al., 2005; Evertsz & Mandelbrot, 1992; Salat et al., 2017; Xiao et al., 2021) to capture the local neuron-based fractal properties of NINs.”, followed by plenty of details on methods. If you lead into this section by first giving the reader an idea why it is interesting to decompose the graph into fractals in the first place, then maybe this would be easier to follow. Generally speaking, motivate the method before jumping into details. I know that the paper is already on the page limit but frankly the appendix is so long, moving a bit more of the methods to appendix in lieu of giving readers a better intuition in the main text is probably beneficial.
- Given there already is a bunch of structural measures which have successfully been used for structural analyses in neuroscience and neural network models (e.g. standard ones like modularity / small worldness, or entropy-based ones or Ricci curvature) I wonder whether authors could somehow motivate why their new measure was needed? Given it works, I do not want to say that the new measure was not needed but I would be curious to know why they specifically took the route they took with the development of the metric.

*Stylistic choices*

- I think the font on Figure 6 is very close to unreadable small.
- Across figures, could you either use a serif or sans serif font but not mix that up?
- I wonder whether your strong emphasize of the word ‘emergence’ is actually needed and helpful in communicating your results? In my experience it does put off some researchers and, as you make a link to neuroscience, the development of language and reasoning skills from a newborn to a teenager would simply be considered as part of ‘development’ and ‘learning’. So, I wonder whether you want to deemphasize the concept of emergence a bit here and just call it ‘the development of skills’?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a new approach to studying the internal property of large language models. I got really excited by the discussion but a bit disappointed by the results. I believe the efforts in this paper should be generalized across the field. 

The parallel between the brain and LLMs in terms of their complexity and emergent characteristics is fascinating. This paper aims to establish a connection with network analysis in neuroscience by characterizing the evolution of organizational patterns within the network during training and linking these to different (emerging) performances.

I disagree with the article’s use of “emergence,” although I understand the rationale. You state that your measure is intended to quantify network regularity. The main conclusion of the article should be that this measure appears sufficient as a proxy for the emergent properties of LLMs.

The results are interesting but quite weak and merit further development. In particular I felt like many network properties could correlate (positively or negatively) with the training stages of LLMs. Nonetheless, this is an intriguing direction towards understanding network local properties and their link to emergent properties.

### Strengths
The paper is extremely well contextualized and the presentation of the ideas and results are solids. The quality of the writing makes it really pleasant to read. 

It gives a really interesting direction of research by trying to bridge a gap with neuroscience and trying to create a new framework to link emerging properties and network topologies.

### Weaknesses
Some mathematics would have deserved better explanation in the article itself and not the appendix.

You are measuring the degree of organisation in the networks and show that :
1. it increases during training
2. it correlates with previous definitions of emergence

Your are yourself comparing it with the averaged weighted degree distribution of the network in the appendix which seem to correlates as well with emergence.

I feel like your "degree of emergence" is itself one dimensional as well, which makes it way less interesting as if it was not. It would be a bit outrageous if we were able such a complex reorganisation with only one global metric. It would much more interesting if you were able to link certain network properties with specific emerging properties.

Your description of the neural network as blocks and layers seems unnecessary. Simply stating that the neural network can be described as a graph with  w_{ij}  values between neurons is sufficient for your further definitions. The layer and block definitions are not used later, except to describe weights that ultimately serve as connections between two nodes.

A reference is missing in the appendix on page 39.

Emergence is, by definition, a property observable at a higher scale that is not explainable by its components. You are measuring network properties, which is interesting, but is it truly the appropriate scale to discuss emergence? I am not convinced the term “emergence” is wisely used in this article. Instead, the focus should be on providing a quantification of network structure that enables or correlates with emergent properties.

On the more serious problems :

You don’t explain how  |P(i,j)|  is calculated. Do you add +1 for each edge along the shortest path? This leaves it unclear whether your distance is calculated exactly.

I feel that many regularity properties would undergo the same type of increase as the one you noted, such as an irregularity, heterogeneity metric or average weighted degree distribution . What were the results (Figure 5 and 24) ? If simpler metrics correlate with emergence similarly, what additional value does your metric provide?

As noted in my initial review and echoed by other reviewers, the use of the term “emergence” in the paper is inconsistent with its accepted definition. Your metric, as described, characterizes the degree of self-organization rather than directly quantifying emergence. For example, your conclusion correctly notes that self-organization properties can lead to emergence, but the title and much of the text do not make this distinction clear. For instance, the title (“Assessment of the Degree of Emergence Across Various Datasets”) is misleading. What does it even mean since your "degree of emergence" is the same for every datasets (since you are showing the exact same curve of degree of emergence here) . I realize that this misuse of the term make the whole paper rather confusing.

II also notice that you have replaced some mentions of accuracy with “emergent abilities,” but then the two terms are the same for really different aspects. This is detrimental to the clarity of your paper. and this inconsistency makes the manuscript confusing.

While the proposed structural metric is interesting, its practical utility as a proxy for model performance requires stronger evidence. For instance:
   * Figure 16 for instance. After epoch 6000 or 8000, your metric decreases. Does this imply a decline in model performance ?
   * Same Figure 16, the metric values differ between two models. Does this mean one model outperforms the other, based solely on this metric and their parameter counts?.
If the goal is to propose your metric as a proxy for accuracy (what other people would call emergence), it is essential to provide a clear comparative analysis and explicitly connect metric trends with performance outcomes.

A consolidated graph that overlays performance across all datasets would also help make this connection clearer, rather than presenting results in five separate figures. (For presentation of the results, should do a single graph that shows all those datasets rather 5 different ones. ).

### Questions
* Your description of the neural network as blocks and layers seems unnecessary. Simply stating that the neural network can be described as a graph with  w_{ij}  values between neurons is sufficient for your further definitions. The layer and block definitions are not used later, except to describe weights that ultimately serve as connections between two nodes.

* A reference is missing in the appendix on page 39.

* Emergence is, by definition, a property observable at a higher scale that is not explainable by its components. You are measuring network properties, which is interesting, but is it truly the appropriate scale to discuss emergence? I am not convinced the term “emergence” is wisely used in this article. Instead, the focus should be on providing a quantification of network structure that enables or correlates with emergent properties.

On the more serious problems :

* You don’t explain how  |P(i,j)|  is calculated. Do you add +1 for each edge along the shortest path? This leaves it unclear whether your distance is calculated exactly.

* I feel that many regularity properties would undergo the same type of increase as the one you noted, such as an irregularity, heterogeneity metric or average weighted degree distribution . What were the results (Figure 5 and 24) ? If simpler metrics correlate with emergence similarly, what additional value does your metric provide?

### Soundness
2

### Presentation
3

### Contribution
3
