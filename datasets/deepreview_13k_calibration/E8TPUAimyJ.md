# Context-Scaling versus Task-Scaling in In-Context Learning

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 6, 6, 3

## Abstract
Transformers exhibit In-Context Learning (ICL), where these models solve new tasks by using examples in the prompt without additional training.  In our work, we identify and analyze two key components of ICL: (1) context-scaling, where model performance improves as the number of in-context examples increases and (2) task-scaling, where model performance improves as the number of pre-training tasks increases.  While transformers are capable of both context-scaling and task-scaling, we empirically show that standard Multi-Layer Perceptrons (MLPs) with vectorized input are only capable of task-scaling.  To understand how transformers are capable of context-scaling, we first propose a significantly simplified transformer architecture without key, query, value weights. We show that it performs ICL comparably to the original GPT-2 model in various statistical learning tasks including linear regression, teacher-student settings.  Furthermore, a single block of our simplified transformer can be viewed as data dependent ``feature map'' followed by an MLP. This feature map on its own  is a powerful predictor that is capable of context-scaling but is not capable of task-scaling. We show empirically that concatenating the output of this feature map with vectorized data as an input to MLPs enables both context-scaling and task-scaling.  This finding provides a simple setting to study context and task-scaling for ICL.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors study an important question: how does in-context learning in Transformers depend on the number of in-context examples as well as the number of overall tasks? They draw a connection to kernel smoothing and demonstrate that a simplified version of the Transformer architecture can implement this algorithm equally well. They show that in contrast to Transformers, MLPs do not exhibit scaling with in-context examples, but that a feature map inspired the Transformer's mechanism can yield successful improvement with more in-context examples.

### Strengths
- I really liked the introduction and thought that the question of context-scaling was nicely set up.
- I appreciated the authors considering a wide range of different tasks that they collected from the relevant literature.
- Building part of the SGPT into the MLP was a neat method for illustrating the origin of the distinct mechanism between either.

### Weaknesses
Unfortunately, I do not think this work is ready for publication in its current state. Primarily, I believe that the paper does not provide sufficiently novel insight from the prior literature.

Notably, improvement of Transformer performance with the number of in-context examples was already noted (as the authors lay out in the related work section), e.g. in Bai et al. (2023) and the prior theoretical literature also explains why this would be the case, as it draws the connection between ICL in Transformers and gradient descent and kernel smoothing --- both of which improve with the number of samples. I do not understand why previous theoretical results (e.g. Proposition 1 in von Oswald et al. (2023)) would only apply to fixed context length.

It is also unclear to me how SGPT provides a novel insight into the mechanism of ICL compared to, say, the construction in von Oswald et al. (2023), who also explicitly draw the connection to kernel smoothing and use a similar set of simple key, query, and value matrices (especially when $W_0=0$ in their construction in Appendix A.1). The authors argue that the simplicity of SGPT is a substantial strength of this paper, as it demonstrates that there are many problems such a simple architecture can solve. But it is unclear to me whether this a theoretical argument (which seems to make the connection to kernel smoothing, in which case I'm unsure how this is different from the insight by von Oswald et al.) or an empirical argument (in which case I think the authors would have to demonstrates concretely that SGPT outperforms kernel smoothing algorithms).

As I noted, I think the contrast to MLPs and providing the modified features to the MLPs was interesting. I think it would be important, however, to provide insight into *how* the vectorized component enables them to scale with the number of examples.

Taken together, I think the paper in its current form is not sufficiently distinct from existing work --- or at least does not explain sufficiently clearly how it is different. As I noted above, I do think that the authors focus on a really interesting question (context scaling) that provides a different angle from prior work. However, I think for the paper to be ready for publication, I think this investigation would have to further explore how this angle can change our theoretical understanding of context scaling.

### Questions
- Why do previous theoretical results only apply to fixed context length, as stated in l.157-159? (See weaknesses.)
- The SGPT as defined in Eq. 13 appears to be more specific than the generic feature map $\psi$ you are then introducing in Equation (9). Is that true and if so, can you explain how this generalized version connects to the SGPT as well as the generic Transformer architecture?
- Tong & Pehlevan (2024) also show that MLPs cannot context scale (Fig. 1d). This is currently not reflected in your related work section (l. 143-146). Could you please clarify and explain how your findings relate to these prior findings?

Minor comments:
L. 51: “an non-exhaustive” -> “a non-exhaustive”
L. 157: typo?
L. 213: “identify” -> “identity”

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies context-scaling and task-scaling of ICL, under multiple ICL regression tasks, including linear regression with fixed and multi noise level, two-layer ReLU neural networks, decision trees, and sparse linear regression. Experiments are conducted on GPT2 and Simplified GPT (SGPT) by taking key, query and value matrices to be identify matrices and removing batch normalization. Under those tasks, GPT2 and SGPT both demonstrate context-scaling ability and the performances of GPT2 and SGPT are very close to each other. SGPT allows a kernel smoothing perspective interpretation of transformer's ICL capability. Specifically, the authors demonstrate the capability of ICL capability of transformer by showing a single layer SGPT can perform kernel smoothing (including the consistent Hilbert estimate as special case) with appropriate feature map corresponding to the attention. To see what statistics are the essence of task-scaling and context-scaling, experiments on MLP with different inputs , such as vectorized input data with or without kernelized features are conducted. Specifically, task-scaling attributes to the vectorized data and context scaling attributes to the kernelized features, and combining both inputs provide both task-scaling and context scaling.

### Strengths
The SGPT considered and its experiments are novel. And it is quite surprising and interesting to see that its performance is comparable to GPT2. I suppose it is due to the simplicity of the ICL tasks conducted in the paper. 

The idea of connecting ICL and kernel smoothly is clearly presented and is of insight. 

The separation of context-scaling and task-scaling via feature from kernel estimate and vectorized input is novel and can potentially help us understand their impacts better individually.

### Weaknesses
Though with the consistency of Hilbert estimate, how exactly the transformer performs Hilbert estimate i.e., via the construction of activation function in attention, is not straightforward. 

What is the major intuition of taking key, query, and value matrices to be identity? Such intuition is vital since it is shown that the context-scaling capability is attributed to the attention, and task-scaling is to the MLP with vectorized data. I wonder if key, query, and value matrices are learnable, will they also provide sufficient task-scaling ability? 

What is the theoretical or explanatory justification for the capability of the task-scaling ability of transformer and MLP, generalization?

### Questions
What is the task-scaling performance for single-layer SGPT (a task-scaling counterpart of Fig 5)?

Could you explain more on the right panel of Fig 3? 

Could you explain more on the Fig 4(B), 2-layer NN, SGD?

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
This study examines task versus context scaling in various in-context regression tasks, finding that Transformers (but not MLPs) can scale with increasing context sizes, as well as tasks. The authors suggest that a Transformer's ability to context-scale stems from its ability to implement kernel smoothers in the attention matrix. Equipping an MLP with features derived from these kernel smoothers enable it to also context-scale.

### Strengths
I found the paper overall to be very well-written and a pleasure to read. The topic is extremely important, particularly in our post-ChatGPT era, and deals with a critical ability in Transformers. The contrast to MLPs sparks a fascinating discussion about the relative merits of different architectures.

### Weaknesses
I would love to see this manuscript published at ICLR, but there are a few oversights that prevent me from assigning a higher score. If these are able to be addressed, I will be delighted to raise my score.

The discussion on context-scaling in MLPs appears to be drawing from prior work by Tong and Pehlevan (https://arxiv.org/abs/2405.15618). The authors claim that MLPs do not context-scale, but Tong and Pehlevan seem to be showing otherwise. I may be misunderstanding both sides here, but Fig 1d and 1i of Tong and Pehlevan appear to demonstrate that at least MLP-Mixers continue to do well for arbitrary contexts. While MLP performance decays as context length increases in ICL regression, it doesn't appear to be the case for ICL classification. Were you able to look at classification tasks as well? Further, it looks like Tong and Pehlevan made the choice of plotting *excess* MSE above Bayes optimal rather than raw MSE. Because Bayes optimal MSE falls as context length increases, zero excess MSE would imply context-scaling. Looking at Figure 6b, for fewer dimensions than the $d= 8$ you tested, it does appear that MLPs adhere to the Bayes optimal level before failing at longer contexts. 

Overall, it would appear that context-scaling in MLPs does happen, but is bottlenecked by some aspect of insufficient data and long inputs, rather than some inability to implement kernel smoothers. MLP-Mixers, which do not have any product interactions that could implement a kernel smoother in an obvious way, continue to do well also. Indeed, it looks like in your Figure 7B, you do demonstrate some context-scaling in unmodified MLPs for 5M-pretraining tasks (top row), quite similar to using $\psi_L$ features.

Additionally, I thought that kernel smoothers are weak in high dimensions, and require a dataset size that is exponential in the input dimension in order to interpolate well -- a classical curse of dimensionality. However, modern Transformers routinely handle token embeddings with dimensions that number in the tens of thousands, which would presumably defeat a kernel smoother even if it were exposed to an Internet-scale corpus -- and in-context, no less! It's quite possible I misunderstand this aspect of your analysis, but it seems implausible that a kernel smoother interpretation of attention is applicable to real-world Transformers?

Finally, you mention there is a theoretical connection between having identity KQV matrices and the Hilbert estimate kernel, but I couldn't find the derivation in your manuscript. This could very well be a blatant oversight on my part, but could you point me to its location?

### Questions
See weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In recent years, there has been a growing interest in the community to understand and build better in-context learning capabilities. In this work, the authors study in-context learning through the lens of two separate abilities: context scaling and task scaling. Context scaling refers to the capability to improve predictions as the number of in-context examples grow while keeping the number of tasks fixed. Task scaling refers to the capability to improve predictions as the number of task grows while keeping the number of in-context examples fixed. The authors show that a lot of in-context learning capabilities arise from the behavior of attention as a kernel smoother. To show this, the authors consider a simplified version of the GPT architecture, which they call SGPT, where the attention blocks are not trained and key, query, and value matrices are set to identity. The authors compare GPT-2 like architecture with SGPT and show that on synthetic in-context   learning tasks from the literature, the performance of the two models match. Further, the authors study context scaling and task scaling in MLPs. First, they show that MLPs with vectorized inputs are capable of task scaling and not capable of context scaling. They show that MLPs with featurized inputs are capable of context scaling but not of task scaling. Finally, they combine the two types of inputs to show MLPs exhibit both context scaling and task scaling.

### Strengths
1. I like the lens that the authors use in the paper, i.e., separating in-context learning into task scaling and context scaling. Even though this lens is not completely new, its a useful one. 

2. The authors propose a simplification of GPT which is referred to as SGPT. This simplification is a useful one from two perspectives -- it gives way to a model that can be understood theoretically and it possibly indicates that we could simplify the architectures for in-context learning. 

3. Overall, the paper is easy to read and reasonably well presented.

### Weaknesses
I have several concerns with the paper that I highlight below.

1. **On feature maps for context-scaling:**
 a) If you construct a Kernel based mapping of the form in equation 11, then of course due to sheer consistency argument one can say that the map in equation 12 converges to the true function. This would require infinite examples in-context. The whole point of in-context learning is to learn in-context as quickly as possible. From an asymptotics point of view, all the consistent estimators in equation 4 can learn the function. Thus the experiments you conduct in Figure 5 are not really interesting. If you took the model in equation 4 itself, then so long as the Kernel you use gives a consistent estimate, one could argue that as sequence length n increases in equation 4 the performance will improve and this model will context scale. Would you elaborate, what is really the important and new insight one should take from Figure 5?

    b) In the first part of Section 5.1, the authors construct a mapping which is based on linear attention and show the equivalence to one step of gradient descent. This result is already known from previous works such as Von Oswald's work.  Can the authors explain what is truly new in Section 5.1?


2. **On the results with simplified transformer:** As i stated in the strengths section, I found the result with simplified transformer intriguing. However, there are few important ablations that would have helped understand this section better. First of all, the authors change the attention to a linear attention l1 normalization operation. What would have happened if the authors only used linear attention and no normalization? While the model is close to standard GPT in terms of performance, how much of this is due to learning that happens due to the MLPs at different depths? Put differently, can the authors show the impact of depth on the performance, i.e., as depth increases model learns more complex hierarchy of features that allow it to match GPT? If that is the case, then this should be clearly stated in the paper too, that depth was crucial to match the performance of GPT at short context lengths. In some sense, if depth is crucial to match the performance, then the role of kernel smoothing alone is not a crucial one.

3. **On Section 5.2**: In this section, the authors study various variants of MLPs to study context scaling and task scaling capabilities. I find somethings unclear here.


   a) Firstly, I find the fact that vectorized MLPs with sufficient capacity not able to context scale not clear. The training data takes the form P, x, where P is the prompt that contains (x,y) pairs from the task of interest, x is the current query. In the case, where the model class is unrestricted, then the learner should ideally learn E[y| P,x], where y is the true label and expectation is over the distribution of prompts and query, label pairs. If the task of interest is linear regression (studied in Garg et al.), the coefficients of the regression are drawn from an isotropic Gaussian, and the features are drawn from an isotropic Gaussian as well, then   
   E[y| P,x] = ((X.t X + sigma I)^{-1} X.t Y).t x, where sigma is noise. This is solution to standard ridge regression. Provided the model class be it transformer or be it MLP is sufficently expressive and contains ((X.t X + sigma I)^{-1} X.t Y).t x, then in principle MLP should also be capable of context scaling. So my question to the authors is "If MLP has sufficient capacity, what stops it from implementing a ridge regression solution at different context lengths up to the maximum context length determined by size of vectorized input?" Basically, if the MLP is not able to learn, then it has to be an argument that is not explained by expressivity but by learnability. Perhaps the optimization cannot find the global minimum in the above case easily?

     b) Secondly, the authors show that MLPs with features from kernel smoothes can context scale. I don't quite get what's the surprise here. Isn't the input feature to these MLPs itself guaranteed to be consistent in infinite context limit?


4. **On the role of context-length:** The authors state that existing works fail to explain the context scaling capabilities of transformers.  In the example, I gave in 3a), the Bayes optimal predictor is implemented by the transformer. This Bayes optimal predictor of course improves with context length. In this sense, I don't quite get why do the authors say that existing works fail to explain context scaling capabilities.

5. **On MLPs and context scaling**: The authors also mention that it is unclear whether MLPs scale with context and they are the first to dive into this. Perhaps the authors have missed https://arxiv.org/pdf/2311.18194.

Overall, I don't feel I learned something insightful from the paper, the only thing I liked was the experiment with SGPT.

### Questions
In the weakness section, I provide both the concerns and the questions for the authors.

### Soundness
2

### Presentation
2

### Contribution
1
