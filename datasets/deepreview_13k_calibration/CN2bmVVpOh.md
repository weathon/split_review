# Transformer Mechanisms Mimic Frontostriatal Gating Operations When Trained on Human Working Memory Tasks

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 3, 5

## Abstract
Models based on the Transformer neural network architecture have seen success on a wide variety of tasks that appear to require complex ``cognitive branching''-- or the ability to maintain pursuit of one goal while accomplishing others. In cognitive neuroscience, success on such tasks is thought to rely on sophisticated frontostriatal mechanisms for selective \textit{gating}, which enable role-addressable updating-- and later readout-- of information to and from distinct ``addresses'' of memory, in the form of clusters of neurons. However, Transformer models have no such mechanisms intentionally built-in. It is thus an open question how Transformers solve such tasks, and whether the mechanisms that emerge to help them to do so bear any resemblance to the gating mechanisms in the human brain. In this work, we analyze the mechanisms that emerge within a vanilla attention-only Transformer trained on a simple sequence modeling task inspired by a task explicitly designed to study working memory gating in computational cognitive neuroscience. We find that, as a result of training, the self-attention mechanism within the Transformer specializes in a way that mirrors the input and output gating mechanisms which were explicitly incorporated into earlier, more biologically-inspired architectures. These results suggest opportunities for future research on computational similarities between modern AI architectures and models of the human brain.

\textbf{Keywords:} 
transformers; neural networks; working memory; computational neuroscience; gating; computational cognitive science; mechanistic interpretability

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores how Transformers, when trained on human working memory tasks, develop mechanisms that relate to frontostriatal gating operations observed in human cognition. The study focuses on understanding whether Transformers can solve working memory tasks using self-attention to mimic input and output gating, which are key to human working memory function. By training a small, attention-only Transformer model on tasks requiring selective memory gating, the authors find that certain task conditions lead to the emergence of gating-like behaviors in the model. The results suggest that these emergent mechanisms enhance the model’s generalization and task performance, potentially bridging cognitive neuroscience and artificial intelligence.

### Strengths
Originality: The study’s focus on emergent mechanisms in Transformer models trained on working memory tasks is novel. The observation that Transformers struggle with the three-register task is surprising. This research adds a unique perspective to both AI and cognitive science by applying Transformers to a working memory framework typically explored in neuroscience.

Quality: The study employs a simplified, attention-only Transformer, enhancing interpretability and enabling the identification of specific mechanisms within the model. The identification of Transformer mechanisms sheds light on how these models might solve working memory tasks and how specific task demands can trigger such emergent functionality. Control tasks are designed to isolate the conditions necessary for mechanistic emergence, strengthening the quality of the findings.

Clarity: The analysis and results are clearly presented, making it accessible for broad readers.

Significance: Understanding how Transformers solve tasks requiring working memory could substantially impact Transformers interpretability and development. By drawing parallels between Transformer mechanisms and human frontostriatal gating, this paper contributes valuable insights for interdisciplinary research. The study’s findings bridge AI with cognitive neuroscience, offering a model that informs both fields and fosters further exploration into the intersection of biological and artificial intelligent systems.

### Weaknesses
•	While the use of a small Transformer model with few heads allows for easier interpretability, the study does not fully analyze or demonstrate the distinct functions of each attention head in each layer. For instance, why exactly are two heads required per layer, and what distinct functions do each head serve? More detailed analyses of each head’s role (e.g., see below) would enhance the interpretability of the model’s mechanisms, and thus the impact of the work.

•	A comparative diagram for understanding “working memory” mechanisms between Transformers and RNNs—often used in biological working memory research—would provide useful context for readers.

•	In Figure 2, while path patching examples are shown, it is implied rather than explicated stated which layer and head are depicted, making it somewhat unclear which specific head is involved.

•	For brevity, I use x^0_i, x^1_i, x^2_i to specify the residual stream at tuple i before the first layer's output, after the first layer's output, and after the second layer's output, respectively. The layer 1 head appears to bind the components (Ins_i, Reg_i, Sym_i) into a tuple and write it to the residual stream x^1_i of Sym_i. However, it is not fully explained if the layer 1 head writes the Store or Ignore Ins_i to different directions within the residual stream. If so, it may function as part of the "input gating" mechanism (suggesting that the Store direction in layer 1 head’s output, but not Ignore direction, is similar to a "working memory" space). Further, do the two heads function similarly or differently? 

•	The functions of the layer 2 head, especially how it compares Reg_i and Reg_j (based on Ins_j=Store), are not fully elucidated. A detailed explanation of how the layer 2 head compares the current Sym_i and a prior Sym_j to output same/different answers would clarify its role in “output gating”. Do the two heads function similarly or differently? The study could use mechanistic interpretability tools, such as analyzing QK and OV circuits, or examining the geometric alignment of vectors in key, query, and value subspaces to address these gaps.

•	While transformers can be trained on working memory tasks, they inherently differ from biological systems as they have access to all previous residual stream positions. The most suitable counterpart of “working memory” might be x^1_i, which layer 1 head writes into and layer 2 head reads from. However, x^1_i is different for each position i, different from a true hidden-state-like "working memory". This divergence raises significant concerns about labeling the mechanisms as "input gating" and "output gating" or referring to Transformer mechanisms as "working memory". Using different terms across the manuscript, or discussing the limitations of these analogies would make the paper’s framing more precise.

•	The introduction lacks a review of previous work on comparing Transformers to brain/neuroscience (to name a few, https://arxiv.org/abs/2112.04035, https://arxiv.org/abs/2405.14992), which could more accurately depict the gap and contextualize the paper’s contributions.

### Questions
1.	Given that the layer 2 head primarily computes functions linearly (Elhage et al 2021), has the author considered potential failure modes? For example, layer 2 head attends more to the Store tuples than Ignore tuples (based on layer 1 head's output?), and attend more to the most recent Store tuples than more distant Store tuples (based on position embedding?). Consider the scenario of a Store tuple followed by many Ignore tuples—could a recent Ignore tuple receive higher attention than distant Store tuples if position embedding outweighs the Store feature (due to linearity in key-query operation)? Such a failure mode would be significant, as RNNs, unlike Transformers, are less susceptible to this (assumed learned attractor dynamics within the hidden state representation).

2.	Could the authors consider using mechanistic interpretability tools, such as QK and OV circuit analysis, or representational geometry mapping of key, query, and value spaces? These analyses help further clarify how the mechanisms are implemented within each head and layer.

3. For other questions please see weaknesses.

### Soundness
3

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
3

### Summary
In their paper “Transformer mechanisms mimic frontostriatal gating operations when trained on human working memory tasks” the authors train simple transformer-based networks a task used in cognitive neuroscience to study working memory. By using behavioural analysis in combination with some derivative tasks and the path-patching technique from MechInterp they show that transformers can learn to solve the task with Gating operations. They draw conceptual conclusions to human neuroscience where Frontostriatal circuits are believed to implement gating operations as part of working memory as well.

### Strengths
I personally enjoyed the authors investigations on identifying how task-dependent gate mechanisms develop through training and how it can be identified through behavioural investigations using thoughtfully constructed task variants. I do not necessarily find their findings surprising, but I acknowledge that having evidence for expected mechanisms is worthwhile scientific work and hence would not let that influence my rating.

### Weaknesses
Unfortunately, I do see quite major weaknesses in this paper in its current state. In the following I group my concerns into a block of neuroscience-related concerns and Mechanistic Interpretability concerns.

*Neuroscience-related concerns*

The authors spend quite a bit of their manuscript making conceptual links to the brain’s gating mechanism in working memory but I struggle to see the relevance of their investigations to the brain’s working memory system, for the following reasons:

- Using transformers for working memory investigations: The authors declare themselves that a weakness of their investigations is that transformers have access to the entire input sequence, unlike the brain. In fact, the very idea of working memory is that the immediate past needs to continually compressed into a latent state of activations or rapid connectivity changes (e.g. see Stokes 2015 TICS). I wonder why the authors would not opt to use Mamba-like State Space Models which would seem to be much closer to brain like processes while also allowing for input dependent processing, and potentially slots through the distinct hidden states in Mamba. I see that models need to be abstractions and that one can in principle study working memory with transformers, but I am not aware of any prior investigations showing such links and hence the study here would need to provide such links themselves, which brings me to my next point:
- Comparison to the brain is purely conceptual: Given that the authors focus on the brain so much in both their title, abstract, and introduction I would have expected to see some actual data comparisons to cognitive neuroscience data, but the authors do not seem to provide any. The only data-like comparison they have is that the model struggles more to learn the task with more working memory items which supposedly is similar to humans but that simply seems like a general task difficulty effect and does not link to gating specifically. The authors should provide a more detailed analysis of how their model's performance scales with increased working memory load, and compare this to the well-established capacity limits observed in human studies. This would require a quantitative comparison, not just a qualitative statement about increased difficulty.
- Poorly referenced neuroscience work: The authors heavily rely on the idea of ‘Stripes’ in frontal cortex for working memory for their model to be relevant, as it is about recalling content from distinct memory slots. Recent neuroscientific investigations call the idea of discrete slots implemented through distinct groups of cells into question and instead think of working memory as being implemented by dynamic and distributed population codes (Meyers 2018 JNeurophys; Miller 2013 Dialogues in ClinNeuro). In case that authors make to want a serious link to neuroscience I think they should discuss how their model could be reconciled with the dominant idea of population codes. Also, the 3-4 chunks given as working memory capacity is on the lower end on the scale though I acknowledge that there is some discussion around it. Of course, the classical number to use is 7 +/- 2 (as discussed in the reference the authors give).

*MechInterp-related concerns*

So, the above points are to be taken seriously to make a believable link to neuroscience. Of course, the neuroscience-link is only conceptual, and the main work of the paper actually is in the MechInterp world showing how gating mechanisms develop in trained transformers. As said in the strengths section, that seems to be an interesting analysis though I am not really well qualified to judge how new that finding is. It seems intuitive to me that this should happen and, as the authors mention themselves, models like LSTM were actually constructed specifically with such ideas in mind. If the authors see their main contribution in studying how a gating mechanism develops in transformers, then I would suggest to strongly deemphasize the neuroscience narrative and instead contextualise the research more in the context of existing MechInterp findings. For example, work like [1] from earlier in the year looks at reasoning mechanisms which at least partially seem to rely on mechanisms similar to the ones proposed in this paper and I assume there is additional other work which I am not aware of.

### Questions
Major question:
- Do the authors see their key contribution in understanding transformers of making a strong point that transformers work like the brain? If it is the latter, I would expect a more detailed discussion of neuroscientific theories, at least a comparison of Transformers with models which are more typically considered working memory models with hidden states, and ideally some direct comparison with data from cognitive neuroscience. If it is the former, then I suggest the neuroscience link should be heavily deemphasized to not be misleading about the similarity to the brain. At the same time, I think in that case a reviewer who is well-versed in the MechInterp field should be included in the decision around acceptance. At the very least, the neuroscience content should largely be replaced by an actual overview of related MechInterp papers.

Minor questions:

- Can you add more infos on the actual setup of the data, for example how many timesteps does one trial have? I do not find that information.
- Is there any control to make sure the trials in the validation set are sufficiently different from the training set? Given you use a finite set of symbols with no noise, I wonder whether there are trials identical across datasets? The probability of this is hard to judge given the information about the length of trials seems to be missing. I am sorry if it is there and I just cannot locate it.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This manuscript aims to understand the conditions by which interpretable gating mechanisms emerge in self-attention using attention-only transformers. The authors train simple, attention-only transformers on a simple reference-back-2 task. Using path-patching approach to interpret transformer mechanisms, the authors characterize what the query and key vectors do/implement during the reference-back-2 task and related control tasks. Overall, they find that the query vector accesses information from specific tokens within the context window (output gating), whereas the key vector provides the address to store an item to gate information (input gating).

### Strengths
Altogether, the results form an intuitive and helpful story to improve the understanding of the transformer’s self-attention mechanism. The combination of the simplicity of the task, and the path-patching approach on the attention-only transformer are instructive tools for understanding.

### Weaknesses
Much of the paper focuses on trying to understand the mechanisms of self-attention. Besides a general concern that I find the results somewhat unsurprising, I have three other weaknesses I’d like to highlight.

1. Novelty. There are a number of papers in mechanistic interpretability that aim to study how transformer mechanisms (including self-attention) influence output/performance via path-patching, e.g., Meng et al., 2023a, 2023b; Olsson et al., 2022, Li et al., 2023 etc. However, most the background in the paper references neuroscience theories (which is fine, but perhaps misleading as to existing work in mechanistic interpretability). A more thorough contextualization of mechanistic interpretability papers would be beneficial.

2. Though the paper is geared towards understanding self-attention mechanism through experimentation, I found the manuscript to be difficult to understand. For example, I found the presentation of the task (both text description and figure 1) to be quite confusing. Only when I reviewed the text and figure from another paper (Rac-Lubashevsky & Frank, 2021) did I understand the task. It shouldn’t be necessary to review a prior paper to understand the experiment. I found figure 2 to be also quite dense and confusing. (I have previously found the figure presentation in Meng et al., 2022, Fig 1 to be quite instructive.) Finally, many of the analyses (e.g., Queries gate outputs; keys gate inputs) are only reported in text. Would it be possible to include a visual figure/understanding that is intuitive as to what the query and key vectors are actually computing?

3. The pretraining result is generally unsurprising (fig 5), and is consistent with prior results in curriculum learning, which is not mentioned.
This is perhaps more of a comment than an explicit suggestion, and something for the authors to consider: In some ways, I think contextualizing the work using the background of ‘frontostriatal gating’ mechanisms may be confusing to some readers. I understand that trying to demonstrate this biological/neural mechanism in transformers may have been the motivation to the authors, yet to a reader who is unfamiliar with neuroscience, this may not add much. The explanation of gating mechanisms via path-patching should in theory computationally sufficient, and doesn’t require reference to neuroscience (which can often be obscure).

### Questions
My questions revolve around addressing the 3 primary weakness I mention above.

1. Besides neuroscience, how does this current work relate to past and ongoing work in mechanistic interpretability? E.g., Meng et al., 2023a, 2023b; Olsson et al., 2022; Li et al., 2023. More specifically, how does the path patching approach used here compare to methods and insights in those papers?

2. Is it possible to include additional figures/visualizations to improve understanding of the paper? More specifically, is it possible to create a clearer visual explanation of the reference-back-2 task or a diagram showing how the query and key vectors function as gating mechanisms? Since the paper aims to interpret mechanisms of transformers, the contribution of the paper hinges on its clarity and presentation.

3. What is the relation of the final result (Fig 5) to curriculum learning?

Minor question: What do the authors hypothesize would happen for multiheaded transformers? What does each attention head do?

### Soundness
3

### Presentation
1

### Contribution
1
