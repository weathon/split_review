# Directed Graph Generation with Heat Kernels

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
Existing work on graph generation has, so far, mainly focused on undirected graphs. In this paper we propose a denoising autoencoder-based generative model that exploits the global structure of directed graphs (also called digraphs) via their Laplacian dynamics and enables one-shot generation.  Our noising encoder uses closed-form expressions based on the heat equation to corrupt its digraph input with uniform noise. Our decoder reconstructs the corrupted representation by exploiting the global topological information of the graph included in its random walk Laplacian matrix. Our approach generalizes a special class of exponential kernels over discrete structures, called diffusion kernels or heat kernels, to the non-symmetric case via Reproducing Kernel Banach Spaces (RKBS). This connection with heat kernels provides us with a geometrically motivated algorithm related to Gaussian processes and dimensionality reduction techniques such as Laplacian eigenmaps. It also allows us to interpret and exploit the eigenproperties of the Laplacian matrix. We provide an experimental analysis of our approach on different types of synthetic datasets and show that our model is able to generate directed graphs that follow the distribution of the training dataset even if it is multimodal.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents an novel approach to crate a one-shot generative model for directed graphs.
The approach represents the graph through their heat diffusion with a forcing term Q(t) that forces the limit distribution to be uniform over the nodes. 
To generate the graph, they train an edge decoder that, given a noisy representation of the heat diffusion, predicts the presence of the edge.
With the decoder to hand, they generate a Erdos-Renyi random graph, and add some Bernoulli noise to the adjacency matrix, then obtain the directed Laplacian for the result and compute the heat kernel under the mentioned forcing term and feed it to the edge decoder.

### Strengths
- Novel approach to cast the one-shot generation of graph
- can handle directed as well as undirected graphs

### Weaknesses
 - The experimental evaluation is a bit substandard given the relatively large recent literature on the topic. The authors should at least match SPECTRE (cited) for the evaluation protocol.

 - The evaluation of the Erdos-Renyi graph generation is not sufficiently justified. While the authors claim to match the in-degree distribution, it is not clear if other structural properties of the generated graphs are similar to the training set. The approach should demonstrate that it can capture more than just the in-degree distribution, such as clustering coefficients, average path lengths, or other relevant graph statistics. The current evaluation only focuses on the in-degree MMD, which is a limited view of the graph structure.

### Questions
While it is clear that the link predictor tries to match what it has seen in the training set, it is not clear how their approach changes the Erdos-Renyi distribution to one more similar to the training set.

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper describes a generative approach for directed graphs. It loosely follows the idea of denoising autoencoders: a trained input function in R^d over nodes is corrupted through a heat diffusion process as to produce an almost constant function over the graph nodes. This function is then given as input to an encoder that is tasked to project the node representation into a latent space and a decoder that, given two node embeddings, predicts the presence of an edge.

### Strengths
This paper deals with an interesting problem, the one of directed graph generation, which seems to be partially neglected by the main body of literature in graph generation but that is nevertheless relevant.
To the best of my knowledge, the proposed methodology is original. It adapts some ideas from denoising autoecoders and the more recent denoising diffusion to the domain of directed graphs, building a principled and sound method.

### Weaknesses
One of the drawbacks of the paper is that the mathematical notation is a bit intricate. Many quantities are redefined during the method description and is difficult to keep track of all of them. Some equations are also defined but I missed if or where they were used, for eq 6 or the node loss (where is the model \phi used in the sampling process?).
Personally, until section 3, I was imagining some sort of denoising diffusion technique (especially after eq 5 and 6). It took me a while to change my “expectations” about the following sections.

The other weakness is about the comparisons. Even if there aren’t many works dealing with directed graphs, it is still worth providing a solid testbench that could possibly be used also from future works that want to compare with the proposed method. Isn’t there more datasets that can be considered or comparative methods that could be adapted

### Questions
- The diffusion time is set to 1 in the experiments, but is it a dataset-dependent parameter? I guess that it might be somehow dependent on the graph radius?

- It took me a while to figure out what a kind of node function N had to be. Maybe making it clear from the beginning that it is learned could help the reading. 

- Still regarding N, permutation invariance is not an easy thing to learn. How much could it be a problem for the training convergence?

- Your method consists of diffusing an initial random graph. How much important is the starting graph family? Since your noise converges to a constant function, would it be possible to sample directly M?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The focus of the manuscript is on directed graphs (digraphs) generative process. The authors propose an encoder-decoder architecture. Their encoder is based on the heat diffusion (defined by the graph Laplacian), and does not require any training. The representation is then perturbed such that it corresponds to a nonhomogeneous process. The denoiser is then trained to reverse the diffusion, i.e. to match the initial condition of the process. They then provide experiments to validate their claims.

### Strengths
- The proposed method is well motivated from a theoretical point of view. 
- Focusing on digraphs is interesting as most methods are on undirected graphs.

### Weaknesses
 - The overall writing and organization could be improved. In particular, section 3, which lack continuity. 
- I found the experiments a bit limited, I think a few things are missing:
    - The authors should report the standard deviation in the table. 
    - I think it is important to report other distances than the current MMD with RBF kernel, either with different kernels and / or with different variance parameters. 
    - In the tables, it is hard to understand the magnitude of the scores. It would be great to add a row for a random method (e.g. random adjacency matrix used in line 2 of Alg.1). 
    - The results in 5.3 could be in the main body of the text by shortening other sections (e.g. related work).

### Questions
- How do you choose the initial node representation $X(0)$ ?
- In eq.1, you also need to specify the initial condition at $t=0$. You could also explain $X(0)$ has $d$ signals that you diffuse following the heat equation (it might give more intuition).  
- >Finally, some denoising decoder is trained to predict the nodes and/or edges when given only X(T ) as input (see details in Section 3.1).
    
    I don't fully understand this sentence. Looking at $\mathcal{L}_{node}$ it is trained to reverse the diffusion process. It is not trained to predict the node, but rather the initial $d$ signals. 
    
- Is the decoder conditioned on the noise level (e.g. like in score matching) ?
- Possible typo: "our decoders are learned " $\to$ "our decoders are trained "

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a generative model, similar to denoising autoencoders, for directed graph generation. The encoder adds noise based on a heat equation expression to generate a perturbed representation, which the decoder denoises to reconstructs the desired generated graph via the random walk Laplacian. The authors test their approach in empirical evaluations.

### Strengths
- Originality and Novelty: The approach that the authors propose is, to the best of my knowledge, original and novel. 
- Significance: Nowadays it is certainly an interesting and important topics to study graphs, as well as generative models on graphs. The topic of directed graph generation has indeed been underappreciated in the literature, so this is a welcome addition. 
- Quality: The technical claims are, to the best of my knowledge, sound and reasonable. Details and questions are given below in the next section. 
- Clarity: The article is written moderately clearly, with ample room for improvement in its exposition. Suggestions are given in the section below.

### Weaknesses
 - The main weakness is in the presentation and empirical evaluation: 

1. I suggest that the authors provide more background and motivation on the mathematical prerequisites to make the paper more self contained. Specifically, the use of the heat equation as a noise model is not sufficiently motivated, and the connection to graph diffusion processes could be made more explicit. The choice of the random walk Laplacian, while standard, could also benefit from a brief explanation of its properties and why it is suitable for this task.

2. The decision to set M to be a constant matrix should be further motivated and explained (to people familiar with this, this is a natural choice, but this can be unclear to the less initiated readers). It is not immediately clear why a uniform distribution is the appropriate choice for a non-informative prior, especially when considering that the node representations are constrained to be column stochastic. A discussion of alternative choices for M and their potential impact would be beneficial.

3. Crucial concepts rely on very recent work such as the Set Transformer in 2019 and the work of Veerman and Lyons in 2020. This makes the article more difficult to read...I suggest that the authors try their best to make this work more self contained in the presentation. The paper should provide a more detailed explanation of the Set Transformer architecture and its relevance to the problem of directed graph generation. The specific aspects of the Set Transformer that make it suitable for handling node representations should be highlighted.

4. The empirical evaluation is limited to very simple models (ER and SBM) under the squared MMD distance for various descriptors, under hyperparameter settings of 3 blocks and p as 0.6, seemingly without much justification. The choice of these specific models and parameters should be justified with respect to the goals of the paper. The evaluation should also include a wider range of graph types and sizes, as well as a more diverse set of evaluation metrics to assess the quality of the generated graphs beyond simple structural properties.

### Questions
1. Is there a concrete reason/justification for why the empirical evaluation is so focused on disconnected digraphs? My impression is that many interesting applications concerns connected/strongly connected digraphs. Is there a possibility where the evaluation metrics (clustering coefficients etc) are just capturing the disjointness of the generated graph, rather than the more fine-grained properties of connectivity within a single connected/strongly connected digraph?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
