# How transformers learn structured data: insights from hierarchical filtering

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
Understanding the learning process and the embedded computation in transformers is becoming a central goal for the development of interpretable AI. In the present study, we introduce a hierarchical filtering procedure for generative models of sequences on trees, allowing us to hand-tune the range of positional correlations in the data. Leveraging this controlled setting, we provide evidence that vanilla encoder-only transformers can approximate the exact inference algorithm when trained on root classification and masked language modeling tasks, and study \emph{how} this computation is discovered and implemented. We find that correlations at larger distances, corresponding to increasing layers of the hierarchy, are sequentially included by the network during training. Moreover, by comparing attention maps from models trained with varying degrees of filtering and by probing the different encoder levels, we find clear evidence of a reconstruction of correlations on successive length scales corresponding to the various levels of the hierarchy, which we relate to a plausible implementation of the exact inference algorithm within the same architecture. \vspace{-0.3cm}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper investigates how transformer models make predictions on samples coming from a structured data distribution, focusing on the hypothesis that transformers implement belief propagation to make predictions. 

Contributions:
1. The authors propose a novel family of synthetic data distributions based on PCFGs to test the hypothesis empirically. 
2. The authors present experimental results on two tasks, root prediction and masked language modeling, which the authors claim to support their hypothesis.
3. The authors present a construction for how to implement belief propagation for a tree-structured factor graph of depth $l$, using only $l$ layers.

### Strengths
1. The work is well-placed in the context of other mechanistic interpretability work for transformers, as well as other work looking into the effect of structured data on machine learning models.
2. Understanding what strategy is learned by transformer models trained on structured distributions is an important problem.
3. The family of synthetic distributions is interesting and has a hyperparameter that allows one to control the locality of correlations between tokens in the sequence.
4. The authors present a novel construction for how to implement BP on a depth $l$ tree using only $l$ layers of a transformer, whereas previous constructions required $2l$ layers.

### Weaknesses
1. It’s not clear how much the observations made in this work generalizes to larger models, and more complicated data distributions.
2. The empirical evidence presented has alternative interpretations that haven't been ruled out. (Please see Questions.)
3. The construction for implementing BP on depth-$l$ tree using a transformer of only $l$-layers could benefit from a bit more details, especially on the root-to-leaf message passing part. (Please see Questions.)



### Questions
W2.1: In both the supervised root prediction task and the MLM task, the authors argue that the transformer performs similar in accuracy to BP is evidence that the transformer is implementing an approximation to BP. While it is very intriguing that the accuracies are so systematically similar, there are plausible alternative explanations (that additional experiments or analysis could rule out):

W2.1.1: Similar accuracy doesn’t imply similar behavior on individual inputs. Have authors considered measuring the match between BP and transformer predictions on individual inputs? If the match is high, this would strengthen the authors’ claim that the model actually behaves like BP. 

W2.1.2: Similar behavior on individual inputs doesn’t imply similar implementation. For example, in figure 1(c), the authors show accuracy of a model trained on k=0 (and for root classification) data and evaluated on k>=0 data, whose accuracy is similar to running BP on the k=0 graph. The authors claim this is evidence in support of model having learned to implement BP. Why couldn’t the model have model the k=0 data well without implementing BP? BP on k=0 graph is optimal for k=0 data, so the transformer that was trained on lots of k=0 data would necessarily behave like BP on individual inputs, which (without necessarily implementing BP) would make similar predictions to BP on out-of-sample data as well.

W2.2 In the supervised root prediction task, the authors write that (line 314-316) “We interpret this as a consequence of the weaker correlations between distant tokens—and therefore the lower signal-to-noise ratio during learning—that must be resolved to match the BP prediction.” Since the task is to predict the root, could the authors elaborate more on why they believe the weaker correlations among **tokens within a sequence** is causing difficulty for learning? An alternative interpretation is that this is due to the weaker correlation between the **root** and the **entire sequence** of tokens.	

W3. Following up on the BP construction, could the authors elaborate more on the leaf-to-root passing? In particular, what do the $r$’s represent? It looks like all $r$’s are initialized to uniform distribution, and they each get updated with the same formula (eqn 22), so would $r^{(a,m)}_i$ ever be different from $r^{(a’,m)}_i$ for $a \neq a’$? A walkthrough of the formulas on a minimal example with small $l$, and $q$ may be helpful here.

Other: Did the authors mean to refer to figure 3 instead of 1c on lines 337? In the caption of figure 1c it says it’s for MLM instead of root classification, and the scale of the x-axis suggests it’s MLM too.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper evaluates encoder-only transformers on a synthetic task, where data is sampled from a complete binary tree-structured generative model of fixed depth $\ell$. There is a knob $k$ that determines at which layer that subtrees are forced to be conditionally independent. This generative process is equivalent to a PCFG, although it is framed mostly in terms of factor graphs and belief propagation. The authors find that transformers can predict the root node type given the leaves with high accuracy. They find that they can do MLM prediction with high accuracy, and that using MLM as a pretraining step improves sample efficiency for root prediction. They analyze attention patterns and see that they attend in a hierarchical fashion as expected.

### Strengths
Some of the experimental results are quite interesting. For example, Fig 4 shows the expected attention patterns, and Sec 3.4 is interesting in that it shows that MLM pretraining improves sample efficiency.

### Weaknesses
Although the paper includes some interesting visualizations, I am not quite convinced that the contributions of this paper are particularly novel or rise to the level of a full ICLR paper. At times I also found the paper difficult to read, and its claims unclear.

1. In terms of novelty, there seems to be significant overlap with Allen-Zhu & Li (2023), and the experiments seem to be a simpler case of that paper. Like this paper, Allen-Zhu & Li (2023) trained transformers on data generated from CFGs of fixed depth and showed that the the transformer layers learned to attend to constituents as expected.
2. In terms of the significance of the contribution, independently of the question of whether it is novel, this is a very simple synthetic task that seems a bit contrived so that transformers are successful on it (an issue that is also in Allen-Zhu & Li (2023)), and it is not clear that we learn very much about transformers from these experiments. The strings in the training data are all of the same length, and the depth of the underlying parse tree is also fixed and does not exceed the number of transformer layers. It is not surprising that a transformer encoder with the same number of layers as the underlying parse tree can learn to mimic the structure of the underlying complete binary tree. It would be more interesting to test the transformer on a CFG with parse trees of varying depths. Do we see similar behavior, and does the fact that the number of layers is finite matter then?
3. In terms of clarity, it is not clear at the beginning of the paper what its primary goal is. Is the paper primarily about proposing a new data model, and if so, what is the purpose and significance of $k$? Are you primarily interested in analyzing the transformer architecture, and if so, how will the analysis on this synthetic task help us understand the behavior of transformers on real tasks such as natural language?
4. One of the main claims of the paper is that the transformer learns to implement a belief propagation algorithm, but I don't see significant evidence that shows that it is learning to implement BP vs. another algorithm, e.g., some version of the inside algorithm. I don't think the analysis of accuracy on OOD examples and attention patterns rules this case out.
5. Major figures supporting the paper's claims are only in the appendix (Fig 7, App C.3 and C.4).

### Questions
1. Intuitively, what "knob" does the filtering parameter $k$ represent? Is it the case that lower $k$ result in more long-range correlations in the data?
1. 035: Another relevant paper: https://arxiv.org/abs/2305.02386
1. Is there a particular reason why you chose to frame the paper mostly in terms of factor graphs and belief propagation, rather than CFGs and standard parsing algorithms (e.g., the inside algorithm)? Is there an advantage to presenting it this way? Is there an advantage in time complexity vs. using a CFG parsing algorithm?
1. 119: What would the equivalent PCFG be, incorporating the depth constraint and $k$?
1. 133: What is $\mathcal{O}_a$? What is $q$? This part is very unclear to me.
1. 144: It's not clear to me what this means. Can you express this in equations?
1. Can the root always be uniquely determined by the input symbols? According to my understanding, the underlying CFG can be ambiguous. How is it possible to get 100% accuracy?
1. How does the BP algorithm described in the main text relate to the experiments? In what way is it used? I don't think this is stated explicitly.
1. Fig 3: Why do you report validation accuracy but not test accuracy? Why does the accuracy go up and then down? Did you not use the best checkpoint when evaluating on OOD data?
1. Why use accuracy instead of perplexity for MLM? Since the CFG can be ambiguous, there isn't only one correct answer, right?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors build a binary-tree CFG with a filtering mechanism that the nodes on layer k is sampled only conditioned on the root node. 

A transformer encoder is then trained to predict the root node. With k=0, the prediction is perfect. And the performance decreases as k increase. It is also shown that the model's performance on out-sample k exactly matches the performance from BP. The authors then conduct experiments on masked prediction (like BERT). Finally, the authors propose an exact implementation of the BP algorithm through the transformer computation.

### Strengths
It's a novel viewpoint to study transformer learning from belief propagation.

The CFG construction with filtering is interesting.

The study is from multiple perspective: prediction accuracy, probing, and manual construction.

### Weaknesses
I'm not sure whether the transformer accuracy matches that of belief propagation is surprising, could it be a natural consequence that the transformer is simply learning the "optimal" prediction function (which is the prediction made by belief propagation)?

I think the writing of this paper can be improved.

While the construction sec3.5 is interesting, it does not mean that the learned transformer is actually doing that (if I understand correct). Specifically, the authors propose a theoretical implementation of belief propagation within a transformer architecture, but it's unclear if the trained model is actually converging to this specific implementation or if it's just one of many possible solutions that achieve similar performance. The paper would benefit from a more rigorous analysis demonstrating that the learned attention patterns and weight matrices align with the proposed BP implementation, rather than just demonstrating the existence of such an implementation.

I may consider raise my score if other two reviewers show strong interest.

### Questions
Line355 I did not quite understand why the accuracy would have a drop in the middle of training.

Also I hope the writing for section3.3 can be improved by giving more easy-to-understand intuition.

### Soundness
3

### Presentation
2

### Contribution
2
