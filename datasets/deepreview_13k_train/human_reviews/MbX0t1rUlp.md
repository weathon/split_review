# MLPs Learn In-Context on Regression and Classification Tasks

- Decision: Accept
- Scores: 6, 8, 8, 6, 3

## Abstract
In-context learning (ICL), the remarkable ability to solve a task from only input exemplars, is often assumed to be a unique hallmark of Transformer models. By examining commonly employed synthetic ICL tasks, we demonstrate that multi-layer perceptrons (MLPs) can also learn in-context. Moreover, MLPs, and the closely related MLP-Mixer models, learn in-context \textit{competitively with Transformers given the same compute budget} in this setting. We further show that MLPs \textit{outperform} Transformers on a series of classical tasks from psychology designed to test relational reasoning, which are closely related to in-context classification. These results underscore a need for studying in-context learning beyond attention-based architectures, while also challenging strong prior arguments about MLPs' limited ability to solve relational tasks. Altogether, our results highlight the unexpected competence of MLPs, and support the growing interest in all-MLP alternatives to task-specific architectures.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents experiments to argue that MLPs and MLP-Mixers are almost as effective as Transformer on many in-context learning (ICL) problems. Experiments in various settings like in context linear regression, classification and relational tasks from the field of psychology like sample match (akin to nearest neighbors in context), and finding the odd example out. In all of these settings, the paper presents experiments showing that MLP, MLP-Mixers and Transformers, by and large, perform similarly on these tasks at the same FLOPs spent on training. In particular, MLPs are slightly worse on the standard ICL problems, whereas they are better on the psychology inspired problems. Overall, through synthetic experiments, the paper makes that case that architectural biases may not play a huge role for ICL with enough compute.

### Strengths
1. This is the first paper, to my knowledge, that highlights that MLPs alone can lead to incontext learning. This is an interesting finding since, at least intuitively, the belief is that self attention helps with ICL. Verification of in-weight to in-context transition with task diversity, for all architectures, was also an interesting finding

2. Presentation and discussion of results is clear

3. For the set of ICL problems considered, the analysis seems quite extensive

### Weaknesses
1. The analysis is mostly in stylized and restricted settings. It is not entirely clear what this means for kinds of ICL that is observed in realistic settings (this is also mentioned in the limitations section of the paper). Even within simplistic settings, some more complex problems can be considered to make the claim that MLPs are competitive with Transformers. See questions 5 and 6 below.

2. Some useful description of the experimental setup, like input distribution,  how MLP and MLP-Mixer were used, were either missing or in the appendix. There is also some theoretical discussion in the appendix that are not referred to in the main paper. See question 1 below.

3. The paper mostly shows empirical evidence that MLPs can be competitive, however there is not much discussion about why this might be the case. See questions 2, 4 below


### Questions
1. What is the distribution of inputs $x_i$ for Section 2.1 What could happen if the tasks were even more diverse by changing the data covariance? This is important because for a fixed input covariance, even a 1-layer Transformer suffices to solve incontext linear regression.

2. Any understanding/analysis of why Transformers fair poorly in the relational tasks and why MLPs might be better? These seem right up the alley for Transformers, especially match-to-sample since attention directly computes all inner products.

3. Are there previous papers that argue that attention is required for ICL?

4. These experiments mix the role of expressivity (how large the model needs to be to solve this task) and optimization (can standard algorithms learn a good solution fast enough). 

5. Any reason to look at linear regression/classification and not other ICL (like decision trees, or fitting MLPs like considered in Garg et al.)? It raises the question whether the findings are an artifact of simplicity of the chosen problems.

6: One strength of Transformers is the ability to handle different context lengths n with a single model. Is this property also true for MLPs?

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
4

### Summary
This paper provides more evidence that in-context learning (ICL) is a unique capability of Transformer models by demonstrating that Multi-Layer Perceptrons (MLPs) and MLP-Mixer models can also effectively learn in-context. The authors show that:

1) On well studied regression and classification ICL tasks , MLPs perform competitively with Transformers when given the same compute budget. 
2) On classical relational reasoning tasks from psychology, MLPs actually outperform Transformers both in compute efficiency and out-of-distribution generalization. This challenges prior beliefs about MLPs' limitations in relational reasoning.
3) The authors demonstrate that MLPs, like Transformers, show a transition from in-weight learning to in-context learning as data diversity increases across their experimental tasks.

The findings support the growing interest in Transformer alternatives, and studies there capabilties in controlled synthetic tasks  while acknowledging that their findings align with existing results showing MLPs' competitiveness on more complex natural language and vision tasks.

### Strengths
The paper is quite well writtin and in my opinion easy to follow. The experiments seems well executed and believable, some questions remain, see below.

### Weaknesses
The paper in my opinion overclaims the signifiance of the work, of how surprising the findings are. MLPs are universal function approximators, and ofc, can to some extend approximate self-attention layers. Its nevertheless somewhat interesting that gradient descent can install such solutions into architectures purely consisting of MLPs. 
It is, especially on tractable problems such as linear regression / classification, clear that, if optimized well, neural networks will find / approximate the (known) Byaes optimal solution of these problems. I therefore not find the results very surprising. 

I would benefit the authors to highlight that Transformers architectures dynamically allocating compute / memory based on its in-context length. This is a unique feature, when comparing to RNNs or MLPs. Even if they might be performing similarlry to MLPs for a given sequence length given a fixed memory, compute budget, the flexiblity of Transformers is their strength.  

The authors, afaiu, do not run experiments in an autoregressive model as e.g. Garg et al., 2022 (What Can Transformers Learn In-Context? A Case Study of Simple Function Classes) or von Oswald et al. 2023 (Uncovering mesa-optimization algorithms in Transformers). I find this setting very important, see Questions below.

### Questions
1) Can you please provide additional experiments and provide analyses of these results when training autoregressively as Garg et al., 2022 or  von Oswald et al. 2023. 

2) If the MLPs / MLP mixers networks are chaning from in-weights to in-ciontext learning, do they approximate  e.g.  gradient descent in their archicture or mimic functionally of the self-attention layers. For the MLP mixer variants, I would find an analyses of functional similarity between architectures interesting. Can you e.g. train read-out layers at different depths of the trained network which approximate the solution / optimal prediction similarly when going down the network. It would be interesting to see if the networks are comptuing similar things at the same depth of the network (and gradually approximating the final solution). One could even try to see if the output of the self-attention and MLP mixers are similar.

### Soundness
3

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
This paper studies the in-context learning capabilities of MLPs and mixer-MLP models, comparing them to Transformers on tasks such as synthetic regression and classification. The models are evaluated on limited training data and larger test sets to determine when they shift from in-weight learning to in-context learning. The authors also introduce unique relational tasks—match-to-sample, sphere oddball, and line oddball—revealing that MLPs and relationally bottlenecked MLPs outperform Transformers on these tasks. They suggest that the results may stem from the inductive biases of these architectures.

### Strengths
1. Every experiment in the paper is designed thoroughly. 
2. This is the first work encountered that explores the ICL capabilities of MLPs, which could be relevant to the literature on foundation models, especially in time series.
3. The addition of relational tasks to the existing synthetic regression and classification experiments contributes valuable insights into Transformer limitations. Transformers perform poorly when test exemplars differ significantly from the training data.

### Weaknesses
The paper could have included real regression data. Most existing literature focuses on synthetic tasks, and exploring real data (even simple regression datasets) with somewhat complex underlying distributions would have added valuable insights.

### Questions
Can you provide more insights on why transformers are failing in relational tasks?

### Soundness
3

### Presentation
4

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
The authors empirically study the performance of MLPs, MLP Mixer Models, Transformers and some hand crafted models on a range of small synthetic in-context learning tasks. By carefully designing the tasks the authors show a transition from in "weight learning" to in "context learning (ICL)".

### Strengths
The paper is thought provoking, well written and does a good job a questioning common assumptions, such as which Models can exhibit ICL? and what ICL even is?

### Weaknesses
The paper compares transformers applied auto-regressively against MLP and MLP mixer models that access the data all at once (are not auto-regressive). This seems like a strange choice for a fair comparison especially when trying to compare training FLOPs required. I strongly suggest including a bi-directional transformer as a fairer baseline. This would greatly strengthen any claim made about computational efficiency.

The paper does not really offer a concrete definition of what ICL is. “In-context learning (ICL) refers to a task paradigm where exemplars from a novel task are presented during inference time rather than during training. ” One could argue working out a linear projection for a “new point” is a new task and hence standard linear regression is “in-context learning”. For clarity I think promoting this sort of discussion about what is and isn’t ICL is a strength of the paper, but I would like to the see the authors add more discussion on this.

The paper only consider small toy problems which makes it hard to know if these observation generalise to more real world problems.

Similar to the above two points I'm fairly confident some researchers might not consider the problems tackled in the paper "real in-context learning", due to the scale and high levels of structure. I would like to see the authors add more discussion and try and push for a more concrete definition of ICL. The fact that MLP can learn a mapping that corresponds to the linear regression algorithm (or similar) is not that surprising. In my opinion the strength of the paper is questioning the existing definition of ICL and trying to push for a more rigours definition, I would like to see the authors lean into this a bit more.

### Questions
Did you try comparing against a bi-directional transformer?

Did you try applying the MLP or MLP mixer auto-regressively?

If you had to give a concrete definition of ICL what would it be? 

Why is working out a linear projection for a “new point” not a new task (and not ICL) where as working out the projection of a point in a new linear regression problem ICL? To me the only different seem to be be how you define a "task"?

Did you consider trying to get even more "meta" so each X,Y pair represents a type of regression problem? (say polynomials of a different order, or a mix of classification and regression problems). Each X would represent the concatenation of m examples of a different problems of the same type. The task is to in-context learn the class of the problem then work out the solution to a new point according to the class of problem? In other words apply the construction figure 1, recursively so X=(((x111,x112,...x11d,y11),....,(x1n1,x1n2,...x1nd,y1n)),....,((xm11,xm12,...xm1d,ym1),....,(xmn1,xmn2,...xmnd,ymn))(xqq1,xqq2,...xqqd)) Y = yqq. here you have m examples of problems from the same class each with n points with dimension d.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the in-context learning ability of MLP and MLP-Mixer, and find it learns in-context competitively with Transformers given the same compute budget in some simple settings.

### Strengths
This paper is well written. The connection with related works are clearly presented.

### Weaknesses
The contribution of this work is hard to identify, and the results are not novel nor inspiring. First, it has been widely studied that MLP can learn relational data, i.e., can predict for set/sequence inputs, i.e., can learn in-context. Thus the studied topic is not novel. Second, it is also known that naive MLP for relational prediction (concatenating input) has disadvantages, e.g. lack of capturing permutation-invariance or variant input number. But this paper does not point out this keys, which would be helpful to explain why the MLP-Mixer and RB MLP can learn in-context better. Third, the result that MLP competitively with Transformers given the same compute budget is obtained with a synthetic setting, considering above nature of MLPs, it is not convincing enough to be generalizable.

In playful but intuitive words, while RB MLP and MLP-Mixer can be viewed as MLP Pro for relational data (including ICL), Transformer can be viewed as MLP Pro Max. So while it is mainstream to study ICL with transformer, it is not meaningful enough to study ICL with MLP.

### Questions
Could the authors provide empirical results on real-world few-shot learning data?

### Soundness
2

### Presentation
3

### Contribution
1
