# In-context learning and Occam's razor

- Decision: Reject
- Avg Score: 5.60
- Scores: 6, 6, 6, 5, 5

## Abstract
A central goal of machine learning is generalization. While the No Free Lunch Theorem states that we cannot obtain theoretical guarantees for generalization without further assumptions, in practice we observe that \emph{simple} models which explain the training data generalize best---a principle called \textit{Occam's razor}. Despite the need for simple models, most current approaches in machine learning only minimize the training error, and at best indirectly promote simplicity through regularization or architecture design. Here, we draw a connection between Occam's razor and in-context learning---an emergent ability of certain sequence models like Transformers to learn at inference time from past observations in a sequence. In particular, we show that the next-token prediction loss used to train in-context learners is directly equivalent to a data compression technique called prequential coding, and that minimizing this loss amounts to jointly minimizing both the training error \emph{and} the complexity of the model that was implicitly learned from context. Our theory and the empirical experiments we use to support it not only provide a normative account of in-context learning, but also elucidate the shortcomings of current in-context learning methods, suggesting ways in which they can be improved.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper first provide theoretical understanding that the success of ICL lies in its implicit optimization for both data fit and model simplicity through the lens of data compression. It then examine the case where the training objective is changed to minimize training error alone instead of the prequential code length, and found that it exhibits worse generalization performance compare to the standard next-token prediction error.

### Strengths
The paper is well-written, the theory is interesting and the experiments are well serving the points.

### Weaknesses
Some of the experiments are not rigorous enough. Please see questions below.

1. Figure 2b: Why does the Transformer without a bottleneck perform worse than the one with a bottleneck? Intuitively, one would expect that a Transformer with a bottleneck would lose essential information necessary for predicting the query’s label, making this result seem suspicious.
2. Regarding experimental details: I found that the Transformer without a bottleneck and the Transformer with a bottleneck were presented with different input formats—one with (x,y) concatenated and the other without. Why is this the case? This setup does not provide a fair comparison between the two models.
3. In the setting where the Transformer is trained with train-risk ICL: Given a total sequence length k (following the notation in line 265), do you break the sequence into k subsequences of length j, where $j\in [k]$, or pass it as a whole sequence, relying on causal attention to prevent future information leakage? If it’s the latter, how do you select the query x? If x is not x_i in the sequence, then it’s not guaranteed that the query x is included in the context x_{1:j}. If it is x_1, would this allow the model to learn a shortcut solution, potentially biasing its predictions?
4. Following the previous question: If a sequence of length k is always broken into k subsequences, why use a decoder-only Transformer? If my understanding is correct, there should be no causality requirement in the context.
5. Regarding the gap observed in performance: Why is the performance gap smaller for linear regression but larger for sinusoid regression and Mastermind? The authors attribute this to task difficulty, but the explanation feels vague. Fixing the function class and varying the problem dimension (as a more concrete indicator of task difficulty) might clarify this point, rather than relying on a vague explanation.
6. Why does the MLP baseline generalize worse than the Transformer? Was model complexity minimized through regularization techniques, such as weight decay, in the MLP? This baseline offers limited insight into the results and seems to introduce some ambiguity. Additionally, what would be the Bayesian optimal model’s generalization error?

### Questions
1. Figure 2b: Why does the Transformer without a bottleneck perform worse than the one with a bottleneck? Intuitively, one would expect that a Transformer with a bottleneck would lose essential information necessary for predicting the query’s label, making this result seem suspicious.
2. Regarding experimental details: I found that the Transformer without a bottleneck and the Transformer with a bottleneck were presented with different input formats—one with (x,y) concatenated and the other without. Why is this the case? This setup does not provide a fair comparison between the two models.
3. In the setting where the Transformer is trained with train-risk ICL: Given a total sequence length k (following the notation in line 265), do you break the sequence into k subsequences of length j, where $j\in [k]$, or pass it as a whole sequence, relying on causal attention to prevent future information leakage? If it’s the latter, how do you select the query x? If x is not x_i in the sequence, then it’s not guaranteed that the query x is included in the context x_{1:j}. If it is x_1, would this allow the model to learn a shortcut solution, potentially biasing its predictions?
4. Following the previous question: If a sequence of length k is always broken into k subsequences, why use a decoder-only Transformer? If my understanding is correct, there should be no causality requirement in the context.
5. Regarding the gap observed in performance: Why is the performance gap smaller for linear regression but larger for sinusoid regression and Mastermind? The authors attribute this to task difficulty, but the explanation feels vague. Fixing the function class and varying the problem dimension (as a more concrete indicator of task difficulty) might clarify this point, rather than relying on a vague explanation.
6. Why does the MLP baseline generalize worse than the Transformer? Was model complexity minimized through regularization techniques, such as weight decay, in the MLP? This baseline offers limited insight into the results and seems to introduce some ambiguity. Additionally, what would be the Bayesian optimal model’s generalization error?

---
Updated after the discussion:
Thank you for the authors in taking time to explain the results. My concern has been addressed, therefore I raise the score from 5 to 6.

Reason for not a higher score: This paper primarily focuses on small-scale experiments. While it provides an explanation from the perspective of Occam’s razor, it does not offer additional insights on improving small-scale training, let alone addressing real LLM cases (which may involve out-of-distribution scenarios and deviate from the meta-ICL format). Therefore, I don’t believe it merits an 8.

Reason for not a lower score: The paper presents an interesting perspective on how in-context learning works in controlled experimental settings. The experiments are well-conducted, and the findings contribute to the literature on understanding in-context learning in small-scale experiments.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper draws a connection between the objective used to minimize the next-token prediction loss, when training with iid data, and a compression algorithm called prequential coding. They show that, if the model is updated after predicting each token, then the minimization of the cumulative loss corresponds to the minimization of the objective of prequential decoding, which serves as an upper bound for jointly minimizing the compression of the data plus the complexity of the model used. The authors also provide a set of experiments to corroborate their theoretical observations.

### Strengths
The proposed connection between the minimization of the next-token prediction loss and the prequential coding algorithm is interesting. Intuitively as an observation, it makes sense that as the model is trained, it should learn to represent new data better, if there is any overlapping information between the different data points. In the specific setting, the data are iid and so the model should get better with each training point. It is also interesting that this loss can be connected with minimizing the complexity of the model.

### Weaknesses
1. In general, the ICL properties of models arise when training the next-token prediction loss, without iid data. The current results do not cover the next-token prediction in general. 
2.  It seems that the current setting assumes that the model is updated each time a token is predicted, but isn’t it the case that when training a model auto regressively, the model is updated with a gradient step over the cumulative loss over all the tokens of the sequence.



### Questions
1. How is it ensured that $T_\phi$ in section 2.3 does not memorize? “To forbid $T_\phi$ from memorizing a single dataset, ..”
2. Could the authors clarify what would change if the data were not iid ? Does any of the results hold? In general ICL properties arise by simply training the next-token prediction loss without iid data. Could any of the results be generalized? 
3. It seems that the current setting assumes that the model is updated each time a token is predicted, but isn’t it the case that when training a model auto regressively, the model is updated with a gradient step over the cumulative loss over all the tokens of the sequence. And so, the loss is not the objective of the prequential code (eq. 4). Could the authors elaborate on why these two are equivalent? 
4. What is standard SGD vs ICL? Do the authors mean that they simply use an MLP in which the examples are concatenated and given as Input to the MLP, rather than having them in the sequence length? I am not sure I understand this distinction since the minimization of the cumulative loss over the next token prediction is also requires to train a model with SGD. Could the authors clarify more this setting? 
5. In section 3.2 the authors state: “For instance, when $T_\phi$ is a Transformer, the expressivity of the model it implicitly fits to the context scales with the number of activations in the network ($N$), whereas the expressivity of a DNN trained through SGD scales with the number of weights ($N^2$). A Transformer in the attention layer has the multiplication of two $d\times n$ matrices, while it also has $d^2$ parameters for each weight matrix. Could the authors elaborate on how they deduce that the expressivity of a Transformer scales with the number of activations ($N$) and why for a DNN with the number of weights ($N^2$)? 
6. Could the authors think of some other setting, which would not require to alter the architecture for training with the target of only minimizing the training loss?
7. In figure 3b, is the x-axis the data points seen during training or the context length? In the y-axis is it the prequential code lengths or the error measured over some batch on the next token only?If the x-axis is the context length, how is it exactly the generalization error measured? 
8. I think the paper would be improved, by focusing more on the last setting of experiments, in which the theory does not provide any guarantees, to understand whether similar results would hold in the case of non-iid data.

### Soundness
2

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
[edited: in response to the revision, I have raised my score]

In this paper the authors propose to re-examine the next-token prediction loss used to train sequence models such as transformers from the perspective of compression, and in particular prequential coding. This is an attractive idea that has been the subject of several recent works, including Delétang et al “Language modeling is compression” published in ICLR 2024, and it holds significant promise as a theoretical and empirical means to understand in-context learning (ICL) and more generally the generalisation behaviour of large language models.

The paper has three main components:

(1) The observation that the next-token prediction loss is related to prequential code length

(2) The relation between this code length and Kolmogorov complexity, which begets the claim that training transformers “explicitly” optimises an objective jointly minimising training error and model complexity (line 248), and

(3) Experiments that aim to validate these theoretical claims, and suggest potential improvements to the design of transformers which will incentivise better ICL.

### Strengths
- I find the prequential code-length perspective on the pre-training objective of transformers useful, it is relatively novel, and I think it is a promising route to understanding ICL. I did not think any of these things before reading this paper, which introduced me to the idea.

### Weaknesses
I find the perspective adopted by the paper intriguing, however in its current form I do not think it has achieved its stated aims in any of three main components identified above:

- The relation between next-token prediction loss and prequential code length appears not to be novel, as it is explained clearly in Delétang et al Section 2, and I think this is not sufficiently emphasised in the paper (their work is cited on line 250 for other reasons).
- While Kolmogorov complexity is presented as playing a significant role in the framing of the theoretical contributions, I am not convinced of this in its current form. The inequality in (4) is of course true, but the major claims (about e.g. transformer training “explicitly” optimising some objective involving model complexity) seem to rely on this inequality being an approximate equality. This is justified in passing, very briefly, around line 162 and a reference is made to Blier-Ollivier (presumably to the discussion in Section 2.4) but I do not understand how this amounts to a strong justification of the approximate equality. The authors' framing suggests that minimizing the prequential code length is equivalent to minimizing the sum of training loss and model complexity, but the connection relies on the tightness of the bound in equation (4), which is not adequately justified. The leap from an inequality to an approximate equality is not trivial and requires a more rigorous argument, either theoretical or empirical. Without this justification, the claim that transformers are explicitly optimizing for a combination of training error and model complexity remains unsubstantiated.
- The experimental results seem a bit scattered, and I am unsure of how strongly they corroborate the theoretical claims. Taking Section 3.1 as an example, I think too much is left implicit about how this connects to the theoretical claims. I do not understand how these findings “follow directly from our theory” (line 312). I do not know how to judge whether or not a gap in performance between prequential and train-risk ICL below 10 datapoints in-context is actually significant. The experiments in Section 3.1, while showing a performance gap in low-data regimes, do not provide a clear mechanism for how this gap arises from the minimization of prequential code length. The connection between the observed empirical results and the theoretical framework is not sufficiently explicit, making it difficult to assess the validity of the claims. The experiments need to more directly demonstrate the link between prequential code length and the observed generalization behavior, rather than just presenting the performance differences.

### Questions
Some small suggestions/questions:

- Section 2.4 stops short of actually writing down the next-token prediction loss and doing the simple calculation that connects it to the prequential code length. Since this is claimed in the summary as one of the key contributions, it seems worthwhile to make this explicit.
- Section 3.4 has a reference to Figure 2a (line 392) that should be 3a
- Perhaps I’m confused but is line 1245 backwards? Isn’t your proposal that models trained with maximal length contexts should lead to worse generalisation? Perhaps I am misunderstanding what “need less tokens to arrive at simple models” means.

In conclusion, while I believe prequential coding is a promising direction to understand ICL, I cannot agree with the authors that their theoretical arguments succeed in linking the next-token prediction objective to Occam’s razor (line 502), in their current form.

Things that might change my views:

- A more detailed explanation of why I should believe (4) is an approximate equality (either theoretical or empirical)
- A stronger link between the empirical work in Section 3 and the theory, explaining exactly how the experiments are predicted (as it stands, it reads to me as a few somewhat confirmatory pieces of evidence, but not strongly so).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper examines in-context learning (ICL) through the lens of Occam’s razor, which suggests that the simplest model that explains the data is most likely to be the true one. This paper proposes that ICL's next-token prediction loss functions similarly to prequential coding. The authors argue that by training models on this principle, ICL can produce models that generalize well across tasks without overfitting, especially in low-data scenarios. 

This paper shows that ICL aligns with Occam’s razor more closely than traditional methods that only focus on training error. They also reveal limitations of current ICL methods, which may underfit in large-data regimes and have varying performance based on model architecture. This paper suggests refining architectures and data distribution controls to improve ICL’s generalization and task adaptability.

### Strengths
1. Novel Perspective. Instead of studying the algorithmic aspect or mechanistic aspect of how LLMs perform in-context learning, this paper proposes a different yet novel perspective --- contrasting ICL with most current approaches in machine learning, and conclude with occam razor's principle that ICL generalize well across tasks without overfitting.

2. Innovative Use of Prequential Coding for Complexity and Generalization. By framing prequential coding, the paper introduces a novel approach to balance model complexity and training accuracy. This insight offers a practical metric for understanding model simplicity.

3. Comprehensive Empirical Validation. The paper validates its theoretical claims through a variety of experiments across different tasks, architectures, and training conditions.

### Weaknesses
1. Limited Generalization to Non-IID and Complex Real-World Tasks. While the paper effectively applies its theory to IID data, the assumptions might limit its relevance to more complex, non-IID real-world tasks, such as language data or continuously evolving data streams. Specifically, the paper does not address how the prequential coding framework would handle situations where the data distribution changes over time, or where there are complex dependencies between data points, which are common in real-world scenarios. The current analysis seems to assume that the data can be treated as a sequence of independent and identically distributed samples, which is a strong assumption that does not hold for many practical applications.

2. Underexplored Architectural Dependencies. Although the paper observes that model architecture significantly influences the effectiveness of ICL, especially in low-data and high-complexity settings, it does not thoroughly explore or analyze which architectural features are most beneficial. A deeper investigation could be interesting. For example, the paper does not discuss how different types of attention mechanisms, or the depth and width of the network, affect the model's ability to minimize prequential code length. It would be valuable to understand whether certain architectural choices inherently lead to better compression and generalization properties within the ICL framework.

### Questions
N/A. See weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper discusses an interesting topic to connect the Kolmogorov complexity, prequential coding with In-context learning. The authors first show the prequential code is a “good” algorithm” to compress both data and model. And through meta learning, the prequential code length could be minimized. In the setting of ICL, the meta learner and inner model for each task are unified as the sequence model. And the next token prediction is equivalent to the prequential coding algorithm. Thus through the next token prediction, the training error and model complexity are jointly minimized.

### Strengths
Overall I like the perspective of this paper. Kolmogorov complexity nicely poses the learning and generalization problem as a compression of data and model. It is surprising to see nowadays the modern LLMs, trained simply on next token prediction, generalizes so well in downstream tasks with or without some fine-tuning. Any effort connecting the two is always welcome.

### Weaknesses
Unfortunately the draft, to me, lacks a sense of rigor. The connection stated in the draft looks like a good story, but there is not much guarantee. How well prequential code length approximates the Kolmogorov complexity is always a question mark. I feel it is a very loose bound. In the prequential coding algorithm, it is assumed that as the learner T sees more data, it will generalize better on the new data. However there is no quantitative analysis on how this is measured. Any assumptions on the distribution of data? What is the sample complexity here?


Specifically, the paper does not sufficiently address the practical limitations of using prequential coding as a proxy for Kolmogorov complexity. The theoretical connection is interesting, but the paper needs to delve deeper into the conditions under which the prequential code length provides a meaningful approximation. The current analysis feels more like a high-level intuition rather than a rigorous mathematical argument. The assumption that the learner improves monotonically with more data is also not universally true, especially in the context of complex models and non-stationary data distributions. The paper needs to provide a more detailed discussion on the potential for overfitting and how the proposed approach mitigates this issue. Furthermore, the lack of a concrete sample complexity analysis makes it difficult to assess the practical applicability of the method, particularly in data-scarce scenarios.




### Questions
1. Figure 1.a: in the description of the prequential coding algorithm, there is a line D+= decode(d_next_encoded,p). I do not see where that decode function is defined. Can you add more details?
2. Equation (4): the first equality says the code length is the sum of bits for all the data based on the learner. Do we also need extra bits to represent the learner itself? Maybe I missed something here. Please feel free to comment.
3. Can you also provide some details on the approximation in (6). Why it is an approximation and what have we missed here. Thanks. 


Finally something minor: The first sentence in the abstract is a bold claim. Even though I agree generalization is a key to machine learning, I would be cautious claiming that the (only) goal of machine learning is generalization.

### Soundness
1

### Presentation
1

### Contribution
2
