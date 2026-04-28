# Learning positional encodings in transformers depends on initialization

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 6, 3

## Abstract
The attention mechanism is central to the transformer's ability to capture complex dependencies between tokens of an input sequence.
Key to the successful application of the attention mechanism in transformers is its choice of positional encoding (PE).
The PE provides essential information that distinguishes the position and order amongst tokens in a sequence.
Most prior investigations of PE effects on generalization were tailored to 1D input sequences, such as those presented in natural language, where adjacent tokens (e.g., words) are highly related.
In contrast, many real world tasks involve datasets with highly non-trivial positional arrangements, such as datasets organized in multiple spatial dimensions, or datasets for which ground truth positions are not known, such as in biological data.
Here we study the importance of learning accurate PE for problems which rely on a non-trivial arrangement of input tokens. 
Critically, we find that the choice of initialization of a learnable PE greatly influences its ability to discover accurate PEs that lead to enhanced generalization.
We empirically demonstrate our findings in a 2D relational reasoning task and a real world 3D neuroscience dataset, applying interpretability analyses to verify the learning of accurate PEs.
Overall, we find that a learned PE initialized from a small-norm distribution can 1) uncover interpretable PEs that mirror ground truth positions, 2) learn non-trivial and modular PEs in a real-world neuroscience dataset, and 3) lead to improved downstream generalization in both datasets.
Importantly, choosing an ill-suited PE can be detrimental to both model interpretability and generalization.
Together, our results illustrate the feasibility of discovering accurate PEs for enhanced generalization.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies how initialization of learnable positional encodings (PEs) in transformers affects their ability to learn meaningful position information and generalize. The paper tests different PE initialization schemes on two tasks: a 2D spatial reasoning task called the Latin Square Task (LST) and a 3D brain activity (fMRI) self-supervised prediction task. On the Latin Square Task, the paper finds that initializing learnable PEs with small-norm distributions leads to better generalization and more interpretable learned encodings (measured via similarity to 2D cosine embeddings) compared to larger norm initializations. On the fMRI prediction task, the paper also finds that learned positional encodings with small initialization work best, and leads to more structured encodings (measured by computing similarity matrices across tokens aka brain regions, and comparing this similarity matrix to one estimated using functional connectivity). Overall, the paper highlights the importance of learned positional encodings along with proper initialization.

----

[score updated after rebuttal]

### Strengths
- The paper is well motivated.
- The experimental setup with the 2D spatial task (LST) is a nice way to evaluate whether learned PEs capture 2D spatial relationships.

### Weaknesses
Motivation / assumptions:
- The paper appears to mischaracterize the role of traditional sinusoidal PEs, which are meant to provide general spatial information rather than encode specific task-relevant patterns. The paper's argument that standard PEs are mainly suited for tasks with local dependencies overlooks their successful use in capturing long-range dependencies in language models. It would be more accurate to state that sinusoidal PEs provide a general, task-agnostic positional encoding, rather than being inherently limited to local dependencies. The success of these PEs in language models, which often require capturing long-range relationships, directly contradicts this claim.
- The connection to NTK theory feels tenuous and not rigorously established for transformers. Have the cited theoretical results on the lazy and rich regimes been shown to apply to transformers? or even specifically to the positional encoding parameters in transformers? The paper should acknowledge the limited theoretical support for applying NTK concepts to transformers, especially concerning positional encodings. The cited works primarily focus on simpler architectures, and it's unclear if their conclusions directly translate to the complexities of transformer models.

LST Task
- I disagree with the characterization of the 2D sinusoidal patterns as "ground truth". I can think of multiple methods for encoding 2D spatial information (for example, any rotation of the 2D sinusoidal basis). This matters because the paper uses similarity to the 2D fixed encoding as a measure of how "optimal" the learned embeddings are. The paper should clarify that the chosen 2D sinusoidal encoding is just one possible representation of 2D space, and that other valid encodings exist. The use of similarity to this specific encoding as a measure of optimality is therefore questionable without further justification.

fMRI task
- The paper states that there isn't a ground truth positional structure available for the fMRI task, but then treats functional connectivity as ground truth when interpreting the learned positional encodings' similarity matrices. This is a contradiction, as functional connectivity is an estimated property of the data, not an inherent ground truth positional structure. The paper should acknowledge that functional connectivity is an approximation, and that interpreting learned PEs based on this approximation is not the same as having a true ground truth.
- Overall, I'm not sure what I'm supposed to take away from the fMRI results. Functional connectivity is estimated using correlations across brain regions. In this paper, the task is to predict masked fMRI, and one would expect the most relevant regions to pay attention to when predicting a masked region would be the regions that are highly correlated to the masked region. So in that sense, the positional encodings are really just a roundabout way of estimating the correlational structure of the data? What have we really learned here? The paper needs to better articulate the significance of the fMRI results beyond simply recovering functional connectivity patterns. The connection between the learned positional encodings and the task performance needs to be more clearly established.

Missing experiments that limit the impact of the findings
- No investigation of how PE initialization interacts with other architectural choices. The paper should explore how the findings generalize to different transformer architectures, such as varying the number of layers or the dimensionality of the embedding space. This would provide a more robust understanding of the impact of PE initialization.
- Limited exploration of optimization hyperparameters or different optimization algorithms beyond Adam/SGD (which are very likely to matter when changing things like the norm of the weight init). The paper should investigate how different optimization algorithms and hyperparameters affect the results, especially given the sensitivity of training to initialization scales. This would help determine if the observed effects are robust to different training procedures.

Interpretations / conclusions
- I feel like claims about "discovering" position information are overstated –– the model may just be finding a convenient internal representation. Perhaps if we had a stronger understanding of how a particular positional encoding allowed the network to generalize better on the LST task, or some analysis of why building in the brain's functional connectivity into the PE for the fMRI task is beneficial. The paper should provide a more in-depth analysis of how the learned PEs contribute to improved generalization, rather than simply stating that they are "discovered". A causal link between the specific learned encodings and task performance needs to be established.
- Put another way, the connection between PE learning and downstream task performance is correlational, not causal. The paper needs to be more careful in its interpretation of the results, acknowledging that the observed relationships are correlational and not necessarily causal. Further analysis is needed to establish a causal link between the learned PEs and the observed performance improvements.

### Questions
- If I'm reading the results correctly, the effect of the weight init scale ($\sigma$) across the two tasks is slightly different. For the LST task, it mainly affects generalization, but training is unaffected (all scales train to 100% accuracy). For the fMRI task, it looks like both train and test performance vary with the weight init value. How should I interpret this?
- What is your viewpoint on the role of positional encodings? Are they supposed to provide generic spatial information to the network (but then subsequent layers in the network can learn to use this regardless of the task)? Or are they supposed to provide a particular inductive bias about the spatial information required to solve the task? (I feel like the paper is arguing the latter, but I want to confirm).
- I noticed you trained networks with a single attention head. What happens if you scale up the network (in particular, add additional attention heads)? I'm wondering if these findings might be in part due to the fact that the network only has access to limited attention mechanisms.
- Are there other toy tasks that you could design and train on that would help shed light on the role of positional encodings?

### Soundness
3

### Presentation
3

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
The authors apply rich vs lazy learning theory to positional encodings (PEs) to show that they can get better generalization in a sudoku-like task and fMRI data from learned PEs with "rich" starting norms compared to many other relevant PE variants. They also show that the learned PEs are most similar to "ground truth" 2d PEs in the sudoku-like task and they show that the learned PEs in the fMRI data captures relevant aspects of the organization of the brain.

### Strengths
- successfully apply rich vs lazy learning theory to improve PEs in a reasoning task and in neural data
- they provide some deeper analyses into what structures the PEs are learning when thy are successful
- the figures are aesthetically pleasing while also being successful in their informational goals
- the paper is a positive contribution to better understanding PEs which are an extremely important aspect of transformers

### Weaknesses
 - authors are unclear about the contents of their testing data. More specificity is needed and I couldn't find it in the methods or section 3.
    - please provide details into how the samples differed from the training data in both LST and the neural data
    - Generalization could refer to unseen data within the same distribution, or it could refer to completely held out combinations of shapes, or expansions of the grid size
- paper would be improved with qualitative visualizations of the learned PEs in the LST experiments
- surprisingly low results with RoPE with no further explanation as to why RoPE would fail in the presented cases
    - RoPE should be able to at least overfit the training data due to its absolute PE component. 
    - Or maybe its poor performance was due to the inability to adapt the relative component to the multiple dimensions of the tasks?
- issue with small norm claim in introductory contributions. there are other ways to adjust learning regime.
    - Consider increasing/decreasing the gain of the output as a way to adjust the learning regime
- The broader impact of this work is perhaps diminished by the fact that it is an application of lazy vs rich learning theory

### Questions
- It seems like there could be more ways than a 2d variant of the sinusoidal PEs introduced in Vaswani et. al. 2017 to encode two dimensional positional information that would still lead to good generalization in the LST. Maybe I'm simply wrong about that intuition, but in the case that there are more ways, why do your models learn an encoding scheme that is similar to the 2d baseline? In the case that my intuition is wrong and there is only one way to properly do the PE, how could you prove that this is only one way? Do you think it would be affected by different forms of regularization? Or from training on different types of generalized versions of the LST (like expansions of the grid)?
- Expanding on the previous point, the very notion of "ground truth" PEs seems limiting in scope. It is possible that there are a variety of performance-equivalent ways for any given task that 2d information can be encoded. Of course, within these possibilities, there might be encoding schemes that are more likely to be learned for any given dataset/training objective/update rule. And there might be encoding schemes that generalize better to various distribution shifts. A greater treatement of this idea would improve the work.
- It's really surprising that RoPE is performing so poorly as RoPE provides absolute positional information in addition to relative. Thus, you would expect that the transformer could use the absolute positional information and ignore the relative information if that was useful for the task. In order to trust the results from RoPE, you should provide a further analysis of why the RoPE models are performing so poorly. Are they overfitting in some way? Is there some reason that the absolute PE component in RoPE is worse than the 1d baseline? Otherwise, the simpler explanation is that you implemented RoPE incorrectly.
- I don't understand why you would do a procrustes alignment in section 3.4/figure 4. The model operates on unaligned versions of the PEs in the same context window, no?

### Soundness
4

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
The authors study Transformer position encodings in tasks beyond language where the dimensionality of the input sequence is no longer inherently one-dimensional, and the correlation structure may be more complex. They find that initialization of the position encoding is important in these more complicated contexts, and demonstrate the benefits of small-norm initialization empirically, taking inspiration from the feature learning regime of theoretical work. They ultimately study the generalization properties of learned position encodings, implying that by initializing weights to small values, transformers can learn 'rich' features in position encodings, allowing them to generalize to novel situations as opposed to overfitting on the training data distribution.

In part, one of the core contributions of this paper is the empirical analysis of the idea that the rich feature learning regime of neural networks may also apply to positional encodings. The insight that this specific modification can have dramatic improvements to generalization, especially on complex relational tasks where position is crucial, is both clever and relevant to the machine learning community broadly. It is therefore a valuable contribution in my opinion.

### Strengths
- S1: The paper is well written and very well organized, making contributions clear. 
- S2: While the 'method' of the paper is as simple as it could get (a single hyperparmeter setting), the authors do perform a rigorous set of experiments across different positional encoding types, making the scientific contribution sound. 
	- Examples of this rigorous analysis include the results for Figures 2C&F, comparing the generalization accuracy of the learned position encodings as a function of their similarity to the 'optimal' 2D grid encoding, known a-priori. 
- S3: The discussion of the performance impacts of the optimizer choice is a valuable nuance that the authors aptly address.

### Weaknesses
 -  W1: The number of tasks which this initialization is evaluated on is limited to 2, which makes some of the conclusions tentative (although the analysis is rigorous).
- W2: Figure 3D seems to be in conflict with some of the results in the appendix (Figs A10, A11 & A12). See Question Q3. If the authors could comment on this, that would help significantly.

### Questions
- Q1: Can you explain the significant difference in performance of the relative embedding method between the first and second tasks?
- Q2: Can you explain the reason why you don't see the 'generalization gap' in the second set of experiments (fmri), between train and validation, like you do see in the first set of results (LST)? 
- Q3: (Related to Q2) Can you explain why in Figures A10, A11 & A12, the random position encoding now seems to work equivalently well to the learned methods? This seems to be quite different than the result presented in Figure 3D and makes that result look a bit cherry picked.

### Soundness
3

### Presentation
4

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
This paper investigates learning positional information directly from data by training transformers with learnable positional encodings (PE) for two distinct tasks: (1) the Latin Squares task, a 2D spatial reasoning task, and (2) predicting resting-state fMRI data for masked brain regions based on activity in other regions. The authors report that (1) initializing learnable PEs with a small norm improves generalization, and (2) the learned PEs closely align with the 2D grid structure in the Latin Squares task and the known brain connectivity patterns in the neuroscience task.

### Strengths
1. Originality: The paper explores the impact of PE initialization on novel tasks, specifically brain activity prediction, which differs from typical applications.
2. Quality: The empirical evidence is strong, with various experimental settings and adequate seeding.
3. Clarity: The writing is clear.
4. Significance: The findings reveal that learned PEs capture interpretable context structures.

### Weaknesses
1. The motivation for 1D tasks is limited, as it does not clarify why the positional encoding (PE) approach for 2D or higher-dimensional tasks would differ fundamentally (see question). It would be helpful to explain what unique considerations are required for PE in 2D spaces. Specifically, the paper lacks a rigorous definition of what constitutes 'ground truth' positional information. The current framing suggests a fixed, predefined 2D sinusoidal encoding as the 'ground truth,' which is not necessarily optimal or even appropriate for all 2D tasks. The authors should instead frame 'ground truth' in terms of task-dependent biases, such as specific distance measures or properties that positional encodings should preserve, rather than relying on a single, predefined encoding.

2. The finding that small-norm PE yields better test performance is unsurprising. The alternative hypothesis—that, unlike in feedforward networks, large-norm PE initialization might improve task performance—is weak. The paper does not adequately explore the potential for large-norm PE initialization to offer benefits in specific scenarios, such as when the task requires a more distributed representation of positional information.

3. Using only a single attention head is uncommon in practice, as it restricts the model to a single processing path. Discussing how results might change with varying numbers of attention heads, or more broadly, how PE effects might differ with multiple heads, would enhance this aspect. The new observation that models with multiple attention heads reduce generalization performance is counterintuitive and requires further investigation. This result could stem from insufficient regularization or some other underlying factor, and the paper should explore these possibilities.

4. Learning PE is expected to outperform predefined PE, as it is optimized specifically for the task. This result would be more meaningful if learned PE provided consistent benefits across a wider range of tasks untrained. For example, for the neuroscience task, can the PE learned from resting state data be useful for predicting the brain in other states?

### Questions
1. Could you clarify the gap you've identified, specifically regarding prior work focusing mainly on 1D input sequences? It seems that once the input is flattened, the tasks considered here also operate in a 1D manner. 
2. Could you explain what you mean by "ground-truth" position information? It's unclear why you consider a 2D "ground-truth" position encoding (PE) based on sines and cosines. Are you suggesting that all tasks on a 2D grid should share the same "ground-truth" PE? If we're training on a single task, shouldn't the PE, or the contextual information, reflect specific geometric constraints imposed by that task? Is there a singular "ground-truth" PE? For instance, in Figure 2C, the attention map accuracy seems to plateau around a cosine similarity of 0.7, implying that this "ground-truth" PE may not be optimal for the task. The entire concept of "ground-truth" PE needs a more substantial rationale.

Some minor points: 
1. 2D Reasoning Task Explanation: The explanation of the 2D reasoning task could be clearer. For example, why is the solution in Figure 1B specifically a circle? This introduces a new shape, but does it mean that any shape (e.g., a star) would also be a valid answer?
2. Optimizer Differences: The differences in behavior between SGD and Adam optimizers raise concerns about the robustness of the results.
3. Color Shading in Figures: The meaning of the color shading in Figures 2BE and 4CD was not explained and could use clarification.
4. The authors report that PEs initialized from small-norm has the highest overall network modularity and segregation (Figure 4CD). Is higher modularity considered beneficial, and if so, why?
5. The training loss for the learnable PE is lower. How was the total parameter count controlled when comparing learnable PE to fixed PE, particularly given the small model size?

### Soundness
3

### Presentation
3

### Contribution
2
