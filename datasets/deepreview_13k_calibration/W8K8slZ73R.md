# Adaptive Transformer Programs: Bridging the Gap Between Performance and Interpretability in Transformers

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
Balancing high performance with interpretability in increasingly powerful Transformer-based models remains a challenge. While mechanistic interpretability aims to specify neural network computations in explicit, pseudocode-like formats, existing methods often involve laborious manual analysis or struggle to fully elucidate learned internal algorithms. Recent efforts to build intrinsically interpretable models have introduced considerable expressivity and optimization challenges. This work introduces Adaptive Transformer Programs, an enhanced framework building upon RASP language and Transformer Programs to create more robust and interpretable models. The proposed method increases expressivity by redesigning two primary attention modules to improve categorical and numerical reasoning capabilities. To overcome optimization hurdles, we introduce a novel reparameterization scheme that enhances the exploration-exploitation trade-off during training. We validate our approach through extensive experiments on diverse tasks, including in-context learning, algorithmic problems (e.g., sorting and Dyck languages), and NLP benchmarks such as named entity recognition and text classification. Results demonstrate that Adaptive Transformer Programs substantially narrow the performance gap between black-box Transformers and interpretable models, enhancing transparency. This work advances the development of high-performing, transparent AI systems for critical applications, addressing crucial ethical concerns in AI development.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper builds off previous work, "Learning Transformer Programs", which presents a Transformer variant which uses discretization and other simplifications so that the learned network can be represented as programs. The present work adds three modifications to the original architecture to improve representational ability and learning optimization. 

1. they replace Gumbel-Softmax with a smooth transition between Gumbel-Softmax and Sparsemax, a sparse version of softmax. 
2. They expand the representational capacity of the program-compatible attention by giving the model the option to use score-based attention in lieu of the representationally limited but interpretable and program-compatible categorical attention. To give the model the option, there is an uncertainty-aware gating between categorial attention and score attention which is based on the Jensen-Shannon Divergence. 
3. They add position embeddings.

The authors show that this improved model performs better or equal to the previous model, while having increased interpretability (fewer lines of code in the learned model).

### Strengths
Originality: I looked on Google Scholar for work that cites the original Learning Transformer Programs that this work builds upon, and did not see anything. So, it seems like an original contribution.

Quality and Significance: The authors back up their proposed modifications with a solid array of experiments: in context learning, RASP tasks, and two NLP tasks. They show a scalability result and conduct an ablation study on one RASP task. The main way in which the new model improves over the previous model is learning programs with fewer lines of code that are slightly more accurate. However, the new model also scales slightly better (performance degrades less as you increase vocab size and max sequence length). 

Clarity: the paper is well written and presented. In particular, the authors do a good job explaining their Gumbel-Sparsemax and uncertainty aware attention contributions. There are some typos that should be fixed. I have some suggestions to improve the presentation, but nothing that would detract from my overall score of the paper.

### Weaknesses
I find the main weakness to be that the evaluation is focused on accuracy and number of lines of code. Without seeing the programs, it is hard to understand what "lines of code" means for the simplicity of the program. See the questions.

Another main weakness is that there is no appendix giving further details.

I think the paper would be much stronger with a section that looks at an example program found, and compares it to the program found by the original method, to understand the improvements of the modifications presented.

### Questions
1. What is the intuition for how Gumbel-Sparsemax improves the optimization process? Is the main benefit that the final programs learned are simpler (fewer lines?) How does transitioning between Gumbel-Softmax and Sparsemax differ from what Gumbel-Softmax already does when the temperature is annealed over time for Gumbel-Softmax? One big difference seems to be that Sparsemax is deterministic? If i understand correctly, temperature annealing changes how discrete the Gumbel-Softmax is, but does not affect the randomness. even when fully discrete, one's sample might change each time. With sparsemax, the choice is deterministic (basically choose the most likely option?) — some explanation here would be helpful. 

2. Is there any mathematical relation between pure Gumbel-Softmax and pure sparsemax? It seems like they might not "mix" perfectly well, and there could be a more principled version of one or the other such that you can smoothly interpolate between the two and get both, but not have to just mash up the formulas with equation (8) (like imagine a second temperature parameter that controls randomness in the gumbel-softmax calculation)

3. What is A_ref? it is "introduced" but I don't see how it is calculated during training.
4.  "In low uncertainty (low JSD), CatAttention is preferred, as it is more confident in its categorical decisions" — I'm confused why this would be true. can't ScoreAttention regular attention? shouldn't it's performance be >= CategorialAttention's performance? so if the only objective is accuacy, I don't see why CategoricalAttention would ever be used.

5. "Our preliminary experiments with separate binary and continuous functions revealed scenario-dependent performance variations, motivating the development of a hybrid mechanism to create more Adaptive Transformer Programs" What are "performance variations", and how did they motivate this development? — I'm assuming this means that for some tasks, categorial worked better than score-based, and for others, the opposite was true. I think this should be stated more directly. this line would also be clearer if you clearly say that the hybrid mechanism can be both binary or continuous depending on how it is trained. 

6. The original Learning Transformer Programs paper mentions the possibility of using score-based attention, but says "It would be relatively straightforward to extend Transformer Programs to include score-based attention modules, but this would also result in longer and more complex programs, because each query must now be defined in terms of an ordering of all |K| possible keys, instead of a single key" — but in the ablation in your paper, adding uncertainty-aware attention (which has the possibility of score-based attention) decreases lines of code. Maybe having an ablation for just score-based would be a helpful comparison too. How can I square what the previous paper says with your results?

7. Is there no appendix to the paper? No examples of learned programs, or attempts to interpret a learned program? Or compare a program with the new method vs the old method? 

8. how are the programs extracted? I assume this is the same as the previous paper, but maybe something different is needed for the new modifications? what does "lines of code" even mean? this is not really made clear in the paper. 

9. how can lines of code differ between trained models?

# Suggestions
1. Fom the ablation study, it looks like just switching on Gumbel-Sparsemax indeed dramatically decreases lines of code, but also hurts performance a bit. Maybe this should be mentioned when motivating/justifying how it helps, or when analyzing the ablation.
2. some typos in citations — line 109
3. Line 178: citation for the claim that " Gumbel-Softmax often yields sub-optimal programs due to local optima and fails to encourage sparsity, hindering interpretability and efficiency" ?
4. score based attention is never clearly defined. it is confusing because categorical attention also uses a score function. so you should define it clearly as being called score-based attention (line 214 I believe)
5. typos in line 235-236.
6. lines 235-236: is the "simple neura network layer" a MLP? aren't MLP's multiple layers? I would maybe call it a network module, not a layer.
7.line 310 "we tested our models on small-scale datasets" — what does small-scale mean? reference appendix for more details?

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
3

### Summary
This paper introduces Adaptive Transformer Programs, an enhanced framework that improves upon existing Transformer Programs to create more interpretable AI models.

Specifically, the authors introduce three innovations: (1) a Transition Mechanism that combines Gumbel-Softmax and Sparsemax. (2) an dynamic attention mechanism that combined categorical and score-based attention using Jensen-Shannon Divergence. (3) a integrated attention mechanism that leveraging both Learnable and Sinusoidal positional encoding.

Then the authors conduct the experiement on various benchmark against the original Transformer Programs and achieve clear improvement. Meanwhile, the ablation study shows the effectiveness of the proposed components.

### Strengths
- The proposed method removes the limitations of previous Transformers Programs from different perspectives, which can potentially bring huge benefits for improving the community's understanding of transformer models.
- The experimental results are solid and the proposed method clearly surpasses the Transformers Programs baseline in both accuracy and "lines of code."
- The experimental setting is comprehensive, consisting of both RASP and NLP tasks.
- This paper is well-written and easy to follow.

### Weaknesses
The main concern to me is that the novelty is marginal. This paper proposes no new method, and all three methodologies are the integration of existing methods in this area. It either proposes a transition or direct combination of two existing methods. To me, these direct "transitions" are not interesting enough and are not fully supported by a simple ablation study on one benchmark. And at least one interpretation of "SMOOTH TRANSITION" is necessary to show the readers when the proposed transition takes effect and why it can be helpful.



### Questions
(1) Why can reducing the "lines of code" be directly considered as improving interpretability?  
To me, the connection between "reduced program length" and better interpretability is not obvious enough. It would be helpful to provide a representation comparison example of the proposed model and original Transformer Programs to clarify that it can learn better representations.  

(2) Regarding sparsity, how does the proposed method behave better than Gumbel-Softmax?  
In section 3.2, one of the motivations is that Gumbel-Softmax fails to encourage sparsity, but I see no discussion following this point.  For example, some direct comparisons (like sparsity rate) between these two methods would be expected.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces the Adaptive Transformer framework, designed to develop robust, expressive, and interpretable Transformer models that can be translated into human-readable programs. The authors address challenges in finding optimal solutions and promoting sparsity, limitations seen in the original framework's use of Gumbel-Softmax reparameterization. To overcome these, they propose a Smooth Transition Mechanism for discrete optimization, alongside Uncertainty-Aware Categorical Attention and Position-Aware Numerical Attention. Experiments on both synthetic and real-world NLP tasks demonstrate that this approach achieves superior performance over benchmarks and provides concise, insightful interpretability analysis.

### Strengths
This paper is well-organized, presenting the concept of Adaptive Transformer clearly, from problem setting through to challenges and proposed solutions. Building upon the Transformer Programs framework, the authors introduce novel designs to address its limitations: the Smooth Transition Mechanism addresses the local optima issue in Gumbel-Softmax, Uncertainty-Aware Attention improves handling of categorical and contextual information, and Position-Aware Attention captures nuanced positional information and enables processing of non-integer values. Together, these enhancements expand the model’s numerical capabilities, supporting tasks that require fine-grained representations.

These methods are well-motivated and shown to be effective through ablation studies. Experiments on both synthetic and real-world NLP tasks demonstrate impressive performance compared to current baselines. The proposed method shows great potential for interpretable and reliable AI systems and is broadly applicable across transformer-based models, suggesting substantial future impact.

### Weaknesses
While the overall performance is promising, the paper lacks case analysis for failure instances in the benchmarks, and the evaluated NLP tasks are limited to classification and NER. Including generative tasks would provide a more comprehensive understanding of the method’s impact.

**Minor issues:**

1.  In line 96, the MHA computation omits the normalization factor $\frac{1}{\sqrt{n}}$, where $n$ is the hidden dimension.
2.  In line 99, the double quotes before “Transformer” need correction.
3.  In line 109, please insert a space between "RASP" and "Weiss et al."

### Questions
1.  In Figure 1's RASP accuracy comparison, why does the Adaptive Transformer Program outperform Standard Transformers on the Sort task but not on the Most Frequent task?
2.  In Table 2, accuracy appears to decrease after integrating the Smooth Transition Mechanism. How should this be interpreted?    
3.  How does the proposed method perform on generative tasks beyond NER and text classification?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes Adaptive Transformer Programs, which are a method to increase the expressive capability of transformer programs (interpretable transformers which can be converted into succinct code). 

The main architectural modification proposed by the paper are:
1. Providing a method to smoothly switch between Gumbel-softmax and sparsemax as a method to control switching between exploration and exploitation.
2. A method to weight between categorical attention and score-based attention
3. A position-aware attention which allows numerical Value, while keeping Q, K categorical.

The paper includes experimental results on synthetic tasks on formal languages and natural language tasks. An ablation study is provided to determine the contribution of each architectural modification to the performance of the model.

### Strengths
- The paper considers an important problem: that of making intrinsically interpretable models more expressive.
- The architectural modifications are well-motivated and largely well described in the paper.
- Experimental results across a wide range of tasks provide evidence for the performance of the model.
- A thorough ablation study is provided.
- The use of lines of code generated for the transformer program as a measure of interpretability is interesting.

### Weaknesses
 - There are sections of the paper which could do with more details. Section 3.3 in particular could provide more details about the reference attention e.g.

- Given that a stated goal of the proposed architecture is to make intrinsically interpretable models more performant, I would have liked to see experimental results which supported the claim of adaptive transformer programs narrowing the gap between standard transformers and transformer programs. Results are shown where the proposed architecture outperforms adaptive transformers (Table 1), but often adaptive transformers themselves already outperformed standard transformers (Tables 3, 4). I believe the paper would be greatly improved by the inclusion of results on a task in which a performance gap between standard transformers and transformer programs was narrowed by the proposed arch.

- In line 377 and the following line, it is said that removing all enhancements results in the lowest accuracy (76.44). This does not appear true however, as keeping only the smooth transition mechanism yielded lower accuracy (73.61), as shown in table 2.

### Questions
- Could more details be provided about the hyperparameters and optimizers used for the various experiments?

### Soundness
3

### Presentation
3

### Contribution
3
