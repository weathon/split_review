# Decomposed Learning and Grokking

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 3, 8, 6

## Abstract
Grokking is a delayed transition from memorisation to generalisation in neural networks. It poses challenges for efficient learning, particularly in structured tasks and small-data regimes. This paper explores grokking in modular arithmetic, explicitly focusing on modular division with a modulus of 97. We introduce a novel learning method called Decomposed Learning, which leverages Singular Value Decomposition (SVD) to modify the weight matrices of neural networks. Decomposed learning reduces or avoids grokking by changing the representation of the weight matrix, $A$, into the product of three matrices $U$, $\Sigma$ and $V^T$,  promoting the discovery of compact, generalisable representations early in the learning process. Through empirical evaluations on the modular division task, we show that Decomposed Learning significantly reduces the effect of grokking and, in some cases, eliminates it. Moreover, Decomposed Learning can reduce the parameters required for practical training, enhancing model efficiency and generalisation. These results suggest that our SVD-based method provides a practical and scalable solution for mitigating grokking, with implications for broader transformer-based learning tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the phenomenon of grokking in the context of “decomposed learning” which seeks to optimize the layers of a neural network as independent matrices given by the singular value decomposition of each layer. The authors study decomposed learning in two layer transformers while varying the rank of different layers in the model and present experiments to show when this method works and when it does not.

### Strengths
The authors find that in some cases the total number of parameters can be reduced, as can the rank of each layer, while achieving similar or faster generalization speed in grokking modular division with mod 97, indicating that fewer parameters can be optimized in total while still leading to a generalizable model, which is a desirable thing.

### Weaknesses
Overall I am a bit confused as to the takeaway suggested here. In most cases it seems that increasing the amount of training data enables lower rank decompositions to be as good or maybe a little better than the baseline. On the other hand when 50% of the training data is used it seems that, for the most part, higher-rank decompositions (many of which increase the parameter count except in a couple cases i.e. in the token embeddings for rank 25) generalize faster and lower rank decompositions generalize slower with respect to number of optimization steps. However when increasing the amount of training data it is well known that the delayed grokking phenomenon becomes less delayed and in some cases even vanishes, so I am not convinced it is fair to say that decomposed learning becomes effective at removing grokking at low ranks in these settings if the delayed generalization phenomenon is not even clear there. In those cases maybe we can conclude that low ranks are just as viable as higher ranks when there is sufficient data, and that could help lower the total parameter count needed to train, but I’m not sure what this says about grokking as a phenomenon? Rather a note on some relationship between the amount of training data and parameter count.

I think there are potentially interesting experiments in this paper that could be suggestive of nice principles in deep learning, feature learning, and specifically grokking, but the way it is presented and the conclusions drawn seem quite unclear to me and I think this manuscript would benefit from a rewrite or more clarity as to what is the core argument being made. In its current form I’m not sure if I’ve learned much about why or what is happening to cause grokking, nor have I learned much about when or why low rank adaptations work and what they are promoting (some notion of complexity is missing that is perhaps being optimized for in the decomposition? Or something else? It’s not clear to me at least.)

While the experiments work for modular division mod 97, it seems fairly reasonable and simple to change the prime number as well when varying the amount of training data to further examine data sparse settings. For instance 50% of training data at mod 31 is a lot less data than 50% of training data at mod 97. Maybe these variations don’t impact your conclusions, but I think in the case of training a two layer transformer on <= 31^2 total samples it should be a simple and fast experiment to run, even on a CPU or cheap GPU. However, I understand that experimental work is compute-limited so my main concerns are less about this lack of some experiments rather about the core narrative story being told.

My last note would be that it would be really interesting to study spectral properties of the recomposed weight matrices as well as the decomposed matrices U, Sigma, V^T after being optimized. The authors note that the SVD decomposition leads to three matrices that are independently optimized when training the network, and that they do not enforce that the columns of U or V are orthonormal nor do they enforce that Sigma is still diagonal. It would be really interesting to track some rank measure of A and the reconstituted A (i.e. stable rank can measure this), as well as plot some measures of rank of the individual matrices in a layer that are being optimized. In general there are a lot of things that should still be studied in this setting to really understand what is going on. 

See Questions for further discussion.

### Questions
In many of the experiments in Power et al. (2022) they use weight decay = 1 but note that there are some results presented using weight decay = 0 when increasing the number of optimization steps. As far as I can tell you are using weight decay = 0 throughout, can you comment on the choice and any comparisons? In particular, how could weight decay affect the low-rank decomposition? This seems like an important part of the story given that there is a fair amount of uncertainty as to the role or necessity of weight decay in grokking (or lack thereof in some cases).

You mention a few times that the experimental evidence supports the idea that training the decomposed version of A allows for “more complex transformations to be learned more efficiently” due to there being cases when generalization happens faster than the baseline in a decomposed learning setting and yet there being fewer parameters total. I’m not totally sure what “more complex transformations” or “more efficiently” in this context means. What is the notion of complexity and efficiency that you are using in the context of grokking? Is it possible that simpler transformations are being learned faster? I think this manuscript is missing a fair but of context to make these sort of claims, and while the experiments are presented clearly it is hard to understand what exactly they mean or how it implies something about more complex transformations or more efficient learning.

As for the experiments with decomposing multiple layers simultaneously it would be great to see more ablations on how to choose how low rank you can go with different layers? For instance if I go sufficiently high rank in my token and position embeddings does it let me achieve fast generalization with even lower rank multi-head attention layers than it would otherwise? There are a lot of natural experiments that would really make this story more compelling in understanding how the rank of different layers impacts the overall learning process and interacts with the ranks of other layers.

Does Sigma ever become non-diagonal in training? If so, what does it look like? What is the rank of U, Sigma, V^T after training? 

Are you training the rank-one decomposition of the A matrix and then putting it back together? Or are you training all of U, Sigma, V^T as is, in which case if Sigma becomes non-diagonal then you might end up with a reconstituted A matrix that has a higher rank than the decomposed rank suggested, if I’m not mistaken? Correct me if I’m wrong of course, but in this case it would be interesting to understand the spectral dynamics of the various matrices in play, and/or plotting something like their deviation from initialization.

I think looking into such directions will be very fruitful and lead to numerous insights that would strengthen this paper substantially.

Some line edits I caught while reading it:

Throughout: “grokk” -> “grok”

Line 230: “perfect near-perfect” → “perfect or near-perfect”

Line 238: “data, rank, 12 start to grokk” → “data, rank 12 starts to grok”

Line 289: “Training on…” → “When training on…”

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a method called Decomposed Learning, which modifies the weight matrices of neural networks using Singular Value Decomposition (SVD), in an effort to investigate the grokking phenomenon and its connection to the structure of the weights. There is a growing body of work suggesting that grokking is linked to poor training setups; conversely, previous research has also explored different weight-matrix decompositions and their impact on training dynamics and efficiency, albeit in larger-scale, non-grokking contexts. 

The authors apply their Decomposed Learning method to Transformers trained on the task of division mod 97, which is known to exhibit grokking under certain hyperparameter settings. Through empirical evaluations, the authors demonstrate that Decomposed Learning can be applied to different weight matrices of a Transformer, reducing or even eliminating grokking. The authors further study the effect of rank reduction in the decomposition, finding that different ranks of SVD can significantly affect the efficiency and generalization capability of learning, especially when coupled with different training set fractions.

### Strengths
1. The experimental section is clear and straightforward, and the results are easy to interpret. The experimental setup is well-designed and thorough within its *specific context*, that is, the single task of division mod 97. The authors evaluate Decomposed Learning on that single task and systematically apply different ranks to various Transformer layers. This consistent and controlled analysis provides good empirical evidence to support the claims about mitigating grokking on this task.
2. The authors find a simple strategy (SVD-based decomposition of the weight matrices) to mitigate grokking on their specific task.
3. If Decomposed Learning can be extended beyond this simple setting, it could be impactful for improving the training and efficiency of 
models.

### Weaknesses
While this paper has an interesting result in that it finds a simple SVD-based strategy to mitigate grokking in this toy setting, I think that some more work is needed to justify the broader claims.

1. The paper does not thoroughly position itself in the broader context, so it is somewhat difficult to assess the contribution in relation to prior works. Explicitly discussing how Decomposed Learning differs from or advances previous techniques would be helpful. **Comparing and contrasting**, providing more explicit comparisons to prior methods using SVD or other decomposition techniques. This is important since SVD and other decomposition methods have been previously used for dimensionality reduction, parameter efficiency and reducing training times.
2. The paper has limited experimental scope (single task of division mod 97) despite claiming that the method has implications for Transformers more broadly. The method should be tested on more realistic tasks to see whether it offers the same benefits, otherwise it is hard to generalize the findings to broader tasks (e.g. vision, NLP).
3. The introduction of SVD and its impact on grokking isn't explained in a very thorough way. More intuition on why this decomposition works (beyond the empirical results) and why it was chosen as opposed to other decompositions could be beneficial. More theoretical justification could be useful.
4. The relevance of grokking in practical settings is unclear. Section 4 seems to imply that it can be induced for MNIST, but it is "contrived" and "forced". Is grokking a widespread phenomenon in practical settings then or not? Are there works showing how widespread and relevant it is? It would be important to answer this to better understand the broad applicability of your method, since it focuses on grokking settings exclusively.
> Decomposed learning is explored in grokking using the division mod 97 task matching the original experimental setup by Power et al. (2022). This task is explored as it is the foundational grokking experiment and, therefore, is the most appropriate case to explore as artificial cases, such as grokking induced MNIST (Liu et al., 2023), could impact the training mechanisms as it is contrived and forced example.
5. Even if your paper will only focus on the specific phenomenon of grokking, it would be important to show how your method works on these other examples (e.g. MNIST) which *are* known to grok.

### Questions
1. Did you compare SVD to other decomposition methods? What made you consider SVD specifically? Could you provide more intuition on why the SVD decomposition specifically aids in reducing grokking? It would be helpful to understand the theoretical basis behind this effect.
2. Did you test your Decomposed Learning method on non-grokking tasks to see how it would affect training dynamics, sample efficiency and performance? This would also give insight on whether the method is applicable more broadly outside the context of grokking (since it's not clear how widespread and relevant grokking is in the first place). Additionally, how sensitive is your method to hyperparameter settings? Grokking itself is sensitive to hyperparameter settings.
3. Is this method applicable to larger and more varied datasets beyond the current setup?
4. Would you consider grokking to be a form of "slow" learning speed due to suboptimal training conditions? If so, would mitigating grokking  mean that your method speeds up training? How would this differ from other decomposition methods that have been shown to speed up training? E.g. the paper says:
> This suggests the strengths of changing the representation of the weight matrix to ease training, which is supported by work by Paul & Nelson (2021), who proposed a learning method using SVD on dense linear layers to reduce the rank progressively and, by extension, the dimensionality of the network during training. This method reduced the training times up to 50% with minimal impact of accuracy on audio classification problems.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper illustrates how parameterizing the layer in neural networks, using SVD decomposition can mitigate the phenomemon of grokking to some extent. Grokking refers to the phenomenon where neural networks achieve perfect training accuracy, far before they achieve greater than random test accuracy. This paper conducts a detailed empirical study using a simple 2-layer transformer and a simple task i.e. modular arithmetic and investigate the effects of decomposing the weight matrix using SVD decomposition at the initialization. The approach is to decompose the weight matrix after initialization into U S V matrices, reduce rank by having a sparse S matrix and not explicitly preserve the SVD decomposition during training. They conduct comprehensive experiments on the different components of the 2-layer transfomer (token embedding / positional embedding / feed-forward / multi-head attention / output layers) independently and together, varying the rank & volume of training data used.

### Strengths
- Systematic and scientific approach to studying the problem of grokking: the paper does a careful controlled study of the effect of rank on various components.
- Illustrating conclusively that there are strong correlations between decomposing layers into U S V  and mitigating the phenomonen of grokking.

### Weaknesses
 - Insufficient discussion of connections to prior work: the idea of leveraging SVD decomposition for better generalization as well as more parameter-efficient learning has been discussed in several different bodies of work in ML: pruning (Compressing Neural Networks: Towards Determining the Optimal Layer-wise Decomposition etc.), low-rank gradients (GaLore: Memory-Efficient LLM Training by Gradient Low-Rank Projection etc.: to name a few.  A thorough discussion of this related work will help place this paper appropriately in the current body of work.

### Questions
Since the decomposed learning doesn't explicitly preserve the orthogonality of the columns of U and V, I would be curious to know what the structure of the low-rank decomposed is at the end of the training. In particular, 
1. Do they retain some orthogonality between columns throughout training, are there any trends here? 
2. The paper mentions the need for "high rank" decompositions. Can the authors verify, that training with this high rank, truly "uses" the full rank i.e. the final weight matrix has rank = the constraint placed by the decomposition? If not, this might point to further inefficiencies in training (such as the one the authors discover) that may contribute towards grokking?

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
3

### Summary
The authors propose a method to alleviate grokking in modular arithmetic tasks by applying SVD to decompose the model’s weights. They investigate the effect of this decomposition across different network components, such as token embeddings and multi-head attention, to identify where it has the most impact. Additionally, they explore how dataset size affects grokking, finding that larger datasets and decomposing certain layers can significantly reduce the delay in generalization.

### Strengths
The paper is well-structured and generally clear to follow. It studies an interesting topic (at least intellectually -- but maybe not practically).

### Weaknesses
The paper’s motivation is not strongly established. The framing suggests that grokking is a problem to be mitigated. For example, the authors state, “...poses challenges for efficient learning…,” “...inefficiencies in how neural networks learn…,” and suggest grokking might apply to datasets like MNIST. They also highlight achieving "superior results with fewer parameters." However, grokking research is generally focused on inducing this phenomenon in artificial setups to study generalization in overparameterized models. I am not convinced that grokking is an issue requiring solution; rather, it is a phenomenon that reveals dynamics in certain models under specific conditions.

Another limitation of this paper is the inconsistency in empirical results across different network components. While the authors suggest that larger datasets enable lower ranks in decomposed learning, behaviors vary notably across network layers without sufficient explanation. For instance, the embedding layer might show a different rank reduction pattern compared to the attention layers, and these differences are not thoroughly investigated. These variabilities make it challenging to draw robust conclusions about the general applicability of the proposed method. The lack of a clear theoretical framework to explain these layer-specific behaviors further weakens the analysis.

The discussion section mainly reiterates empirical results without offering deeper insights. Strengthening the paper would require further analysis and clearer connections to existing theoretical work. For instance, Kumar et al. (2024, https://arxiv.org/pdf/2310.06110) frame grokking as a transition from "lazy" to "rich" learning dynamics. Similarly, the “Dichotomy of early and late phase implicit biases” paper suggests grokking is tied to gradient flow. How would authors pose their results in existing literature? For example, the authors might consider analyzing the rate of weight or representation changes under low-rank settings or analyzing gradients and arguing that they support or disprove some of the existing perspectives. This way, they could go beyond presenting empirical results and engage in a deeper discussion.

### Questions
In Section 3, it would improve clarity to define the SVD dimension “r” as the true rank of matrix $A$ $(r \leq \min(m, n))$ – current notation $(r < m < n)$. Then, for $k < m$ or $k << m$, simply using $k < r$ may enhance clarity.

The Author Contributions and Acknowledgments sections appear to be copied from the ICLR template. Please remove or update them.

Minor typos: The word “grokk” should be “grok” (e.g., lines 289, 295 — "I grok" vs. "I am grok-king"), and “artefact” should be “artifact” (line 499).

### Soundness
3

### Presentation
3

### Contribution
2
