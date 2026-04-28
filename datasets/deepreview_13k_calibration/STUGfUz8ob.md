# When can transformers reason with abstract symbols?

- Decision: Accept
- Avg Score: 7.60
- Scores: 8, 8, 8, 6, 8

## Abstract
We investigate the capabilities of transformer models on \textit{relational reasoning} tasks. In these tasks, models are trained on a set of strings encoding abstract relations, and are then tested out-of-distribution on data that contains symbols that did not appear in the training dataset. We prove that for any relational reasoning task in a large family of tasks, transformers learn the abstract relations and generalize to the test set when trained by gradient descent on sufficiently large quantities of training data. This is in contrast to classical fully-connected networks, which we prove fail to learn to reason. Our results inspire modifications of the transformer architecture that add only two trainable parameters per head, and that we empirically demonstrate improve data efficiency for learning to reason.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work studies the ability / inability of transformers to learn certain symbolic reasoning tasks, specifically real valued (“a=+1, print(a)” -> +1) and symbolic valued (“a = `q’ , print(a)” => q) template tasks. To study whether models can learn a rule for an arbitrary new input symbols, they invoke a slightly different concept of generalization under distribution shift known as “generalization to the unseen.” This measures the intuitive notion of generalization of a rule to arbitrary inputs rather than inputs from the same distribution used for training (which is the usual notion of generalization in ML).  For both of these symbolic tasks, the authors argue that the permutation symmetry of multi-layer perceptrons (MLPs) trained with SGD prevents them from generalizing to unseen symbols (Appendix I). For transformer architectures, an analysis of the initial feature kernel under random Gaussian weights reveals that transformers can generalize on real-valued symbolic reasoning tasks by training the readouts only. The reason for this generalization follows from an approximation of the empirical kernel matrix as block diagonal with each block representing the inputs from a single template: K(x_a, x_{a’}) = K(x_b,x_{b’}) for x_a, x_b from template 1 and x_a’ , x_b’ from template 2. This approximation becomes increasingly valid as the “data diversity” metric introduced by the authors increases. This approximation allows the authors to work with a # template x # template gram matrix N, which they show to be non-singular. The importance of having a well-conditioned the N matrix suggests a possible improvement to transformers where an identity matrix is added to the weight innerproducts WK WQ -> WK Wq +  a * Identity, etc. The authors show this improves generalization in their task. For symbolic tasks, the authors show that the gradient descent updates are orthogonal to the directions which would reduce the loss when the embedding dimension is large. They provide experiments verifying that large embedding dimension worsens performance on copy tasks.

### Strengths
This paper studies an important problem of generalization to unseen symbols in transformer architectures. Much of the contribution is formalizing a set of symbolic reasoning tasks which can be analyzed in different architectures. The authors give a theoretical analysis that suggests implementation tweaks (adding the identity matrices) which improve performance on real-valued template tasks and preserve good performance on natural language modeling. They also give an important separation result between multi-layer perceptrons and transformer architectures and explain why the transformers can learn the real-valued regression tasks at large width. Lastly they observe that large embedding dimension can be harmful in transformers on copy tasks. I appreciate the effort the authors took in performing experiments (several in the Appendix) to evaluate their theoretical claims, which are often lacking in theory papers.

### Weaknesses
Though the paper provides some generic results about architectures for MLPs, the main result for transformers relies on operating the model in the kernel regime. It is unclear at the moment if any of the results would change (1) at finite width or (2) in the feature learning regime (see questions below). Specifically, the theoretical analysis hinges on the Neural Network Gaussian Process (NNGP) kernel, which assumes infinite width. The practical implications of this assumption need further exploration, as real-world networks operate at finite widths where the kernel approximation may not hold. Furthermore, the paper does not fully explore the transition from the kernel regime to the feature learning regime, where the network's internal weights are updated. This transition could potentially alter the observed generalization behavior, and it is not clear if the block diagonal structure of the kernel would still be preserved when the network learns its own features. Further, the proposed theory bounds the generalization error in terms of the data diversity metric, which does not have an obvious scaling with samples n, making it hard to reason about the number of samples needed to attain good generalization. The data diversity metric, while useful for characterizing the input space, lacks a clear connection to the number of training samples needed to achieve a desired level of generalization. This makes it difficult to assess the practical sample complexity of the proposed method. It would be beneficial to have a more explicit relationship between the data diversity metric and the number of training samples required for the model to generalize effectively.

### Questions
1. Do the sample complexity results / rank of N matrix change if you allow the network to learn its internal weights rather than just the readout weights? 
2. Do the authors have any empirical evidence showing the emergence of this block diagonal structure in the NNGP kernel at initialization (I imagine this would be easy to compute)? The block-diagonal approximation seems reasonable, but some empirical support + visualization could be useful. A similar comparison of the predictor from kernel regression and the average of the labels over a template could also be useful. 
3. Do the authors have a sense of how wide the transformer must be compared to samples n, templates r, etc for the theory to be accurate (N non-singular etc)? Wouldn’t the kernels become singular at some finite width? What if every layer is trained at large width (NTK vs NNGP)? Do real networks (which learn features) have to be as wide as kernel analysis would suggest? 
4. The perplexity improvements on GPT + Wikitext seem rather small. Does this suggest that transformers trained in practice evolve to have well conditioned N matrices, removing the need to add an explicit identity matrix? Is this related to the pronounced diagonals in Wv Wo the authors report in the next section? Or is the idea that real data behaves differently than the proposed template tasks? 
5. In Theorem 1.1 it may be helpful to clarify that the gradient flow is only performed on the last layer. 


Small typos
1. Figure 3b caption should read W_V W_O^T  (transpose dropped in second writing)
2. Page 28 d/dx in the Wronskian should be d/dt

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this work, the authors aim to establish and understand the abilities of self-attention architecture to solve variable binding tasks. I find the targeted problem both valuable and exciting---indeed, variable binding is a core intelligence capability and yet we have not seen sufficient work in the community targeting it as a direct benchmark for understanding limitations of existing models. I think this work is a step in the right direction therefore.

### Strengths
As noted in the summary, I find the targeted problem valuable and exciting. The theoretical framework itself involves several assumptions that are arguably impractical (making this essentially a kernel regression take on LLMs paper), but nonetheless the tasks established earlier in the paper are very well described and the results are accordingly insightful.

### Weaknesses
1. I think the authors are over-claiming their results at several points. The simplified architecture that is studied in this work, i.e., a self-attention + MLP model, is not justified to be labeled a Transformer. Residual connections, layer normalization, and multi-head attention all play a crucial role in both optimization stability and, e.g., some of the seemingly emergent abilities of Transformers. The absence of these components significantly alters the model's behavior and learning dynamics. In this sense, I would argue the paper is actually focused on understanding inductive biases and limitations of a feedforward, MLP model with self-attention. This is totally fine, but the over-claiming can yield, in my opinion, an incorrect takeaway that Transformers broadly cannot perform the variable binding tasks. It may also be worth mentioning that the results focus on a inference with a single pass through the model, i.e., tools like in-context learning or chain-of-though can impact the results. The latter is just a nitpick to better contextualize the paper's findings.

2. Lack of experimental details: While the authors often state that their theoretical claims focus on a simplified architecture, it is unclear to me if the experiments involve this simplified architecture or an actual Transformer, i.e., with residual connections, layer normalization, and multi-head attention, is used. The specific hyperparameters, optimization algorithms, and training procedures are not clearly detailed. For example, the learning rate, batch size, and number of training epochs are not specified. Generally, I think the experimental details can be improved to ensure reproducibility and allow for a more thorough evaluation of the results.

3. Relation with prior theoretical works on inductive biases of self-attention: A specific work that addresses a similar question as this paper is Edelman et al. [1]. Therein, the authors show a self-attention model can express sparse boolean circuits and performs implicit variable creation during forward inference. I think the work deserves thorough discussion in the current paper's related work. A few more empirical works also exist on this problem, e.g., Davies et al. [2], that will be worth discussing. Specifically, the paper should discuss how the current work's findings relate to the implicit variable creation and the ability to express boolean circuits shown in [1]. The paper should also discuss how the current work's empirical results compare to the findings in [2].

4. Discussion with Systematic generalization: I would argue the tasks that the authors studied are extremely related to what NLP community has studied under the label of systematic generalization before. I think such papers warrant discussion as well (e.g., see [3]). Specifically, the paper should discuss how the current work's tasks relate to the SCAN benchmark and other tasks used to study systematic generalization. The paper should also discuss how the current work's findings relate to the various approaches proposed to improve systematic generalization in neural networks.

### Questions
The proposed changes based on the theoretical models involve addition of a scaled identity matrix to parts of the attention matrices. This looks, at a surface, like addition of a residual connection in fact. Can the authors clarify this further? I found the discussion of this point to be quite unclear.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This manuscript studies the ability of transformers to reason with abstract binding --- or symbol binding. The authors contrast MLPs and transformers and argue how MLPs trained with gradient descent are incapable of abstract reasoning. They then show how transformers on the other hand are capable of abstract reasoning given lots of data. Finally, they propose an a transformer variant that generalizes faster to the symbol binding task and verify the same empirically.

### Strengths
The paper was a great read! The authors conduct a thorough theoretical analysis with practical insights suggesting changes to the transformer architecture. The work studies if transformers are capable of symbol binding, which is very important question and of broad interest to the community. The paper presents a diverse set of results, but makes them easy to understand to a broader audience too.

The template tasks are elegant and easy to understand. It grounds the problem in a concrete scenario that can be studied. The authors present concrete insights for real labels and symbolic labels and identify different sample complexity behaviors for both scenarios. The work identifies important factors like data diversity or transformer embedding size that change the convergence behavior.

The authors use their theory to develop practical insights for developing transformer architectures. In particular, they show experiments on a synthetic dataset and on Wikitext to validate their proposed modification.

### Weaknesses
The theory for the transformers seems to rely on training only the final layer of the transformer. Does that mean that there are other architectures that can also do symbol binding? It is unclear which aspect of transformers are important for symbol binding: is the attention, the MLP, the invariance properties or something else? It isn't entirely clear to me how

A limitation of most theory that uses the PAC framework often has vacuous bounds. While the paper derives asymptotic trends, it is unclear if they will predictive of what happens in practice as a result. However, I also acknowledge that this is the case for lot of theorems about deep networks. It is unclear if this probabilistic framework is the right tool for analysis.

### Questions
1. The proof for the failure of MLPs relies on taking an expectation over $\theta_t$ obtained through gradient descent. Does this also hold for a single run of an MLP training. Is it possible for MLPs to converge some of the time (and not with probability at least $1 - \delta$ )?
2. The proof seems to rely on the kernel ridge regression estimator. Does this mean that representation learning is not critical for symbol binding?
3. If the data diversity is small (data follows a Zipf distribution), then do these results hold? In practice we expect datasets to follows such distributions and I am unsure if I am misunderstanding the theorem incorrectly. 
4. Are there technical reasons for using the kernel regression with gradient flow in section 4, but the cross-entropy loss with next-token prediction for section 5? Is it possible to conduct an analysis similar to section 4 if we consider next token prediction?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
The paper investigates the "variable-binding" capability of transformers from a theoretic perspective, which refers to the generalization ability to handle unseen symbols during training. To formulate the variable-binding ability, the authors propose a framework called template tasks. Then the authors prove that a simplified transformer block can generalize to unseen input symbols when the output is a binary label, but cannot generalize when the output label is also dependent on novel input symbols. Finally, the authors propose a simple mechanism to augment the attention layer in transformers which is empirically shown to be effective.

### Strengths
- The author provides a theoretical formulation of variable-binding tasks called template tasks.
- Proofs are provided for the capability and limitations of a simplified transformer architecture on two instantiations of template tasks. 
- Extensive empirical experiments are conducted on the template task framework.

### Weaknesses
My main concern lies in the assumption of the proof. Throughout the whole paper, the authors assume a simplified depth-1 transformer architecture without residual connections and layer normalization. However, residual connections and layer normalization are known to be crucial for the performance of transformers [1,2]. The simplification limits the applicability of the main theoretical conclusions to more practical settings. On the other hand, all empirical results use a vanilla depth-2 transformer without modification. This makes it hard to draw direct parallels to justify the practical implications of the theoretical results. Specifically, the theoretical analysis focuses on a single self-attention layer followed by an MLP, which neglects the impact of multi-layered architectures and the stabilizing effects of residual connections and layer normalization. The absence of these components in the theoretical model raises questions about the generalizability of the proven claims to more complex, real-world transformer models. The empirical results, while demonstrating the effectiveness of the proposed attention modification, do not directly validate the theoretical findings due to the architectural discrepancies.

### Questions
As I mentioned in the weakness section, I am especially interested in authors' opinions about how to extend the main proof in the paper to more practical transformer architecture with residual connections and layer normalization.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work presents an analysis of the abstract reasoning capability of the transformer architecture. The analysis yields a novel modification that improves out-of-distribution reasoning in symbolic tasks. The proposed modification also yields improved performance in an LLM (GPT-2) on a more realistic task.

### Strengths
- The paper presents a formal analysis of OOD symbolic reasoning in both transformers and MLPs, finding that transformers, but not MLPs, are theoretically capable of a form of abstract symbolic reasoning, given sufficient training data diversity. This provides interesting insights into the source of reasoning capabilities in LLMs, and contrasts with the common view that their capabilities are due exclusively to scale. This sort of analysis is less common in reasoning papers, so it is a very welcome contribution.
- The analysis yields a novel modification to transformers that further improves their abstract reasoning capabilities, improving sample efficiency on one class of tasks, and enabling generalization on another. 
- The proposed modification also yields improved performance in a pretrained LLM (GPT-2) on a realistic task (wikitext).

### Weaknesses
I think this paper provides a strong contribution. My comments are primarily about clarification and presentation:
- The abstract and introduction refer to 'transformer large language models'. However, if I understand correctly, the experiments in Figures 1 and 2 are performed on transformers trained from scratch, not on LLMs (though an LLM is tested later on). If this is correct, I think it would be clearer to simply refer to transformers (rather than LLMs) in the abstract and introduction. This distinction is important because the training regime and scale of LLMs can introduce different inductive biases than smaller transformers trained from scratch.
- It would be helpful if an intuitive characterization of the proposed modifications ($aI$ and $bI$) could be provided earlier in the paper, along with some sense of why this modification helps. Currently, the paper dives directly into the mathematical formulation without providing a clear conceptual picture of what these modifications represent in terms of attention mechanisms or information flow within the transformer.
- Do the wikitext experiments involve OOD generalization in any sense (in the same way that the reasoning tasks do)? If not, I wonder whether this partly explains the smaller relative improvement from the modified models vs. GPT-2. The lack of explicit OOD generalization in the wikitext experiments makes it difficult to directly compare the impact of the proposed modifications on abstract reasoning capabilities, which are the focus of the theoretical analysis.
- I was somewhat confused by the distinction between GPT-2 and 'GPT-2 pretrained' -- isn't GPT-2 by default pretrained (since this term refers to the trained model)? Just to clarify, do the results in Figure 4 reflect pretrained GPT-2, which is then fine-tuned on the wikitext datasets, or both of the models in this figure are trained from scratch only on wikitext?

Minor comment:
- The legend is cut off in figure 3a. In general the figure text is very small and difficult to read.

### Questions
I found it interesting that GPT-2 already contains heads that implement a strategy similar to the modifications proposed in this paper. A preliminary investigation of GPT-4 suggests that it has a very strong ability to perform the abstract reasoning tasks from this paper based on just a few in-context examples. Do the authors expect that larger models (e.g. GPT-3 and GPT-4) may be able to perform these tasks without the proposed modifications, and if so how does that relate to the theoretical results? Do the authors expect that this capability would similarly depend on the emergence of heads that implement a diagonal attention strategy? Does the analysis in this paper have anything to say about the ability to learn these kinds of abstract reasoning tasks through *in-context* learning (as opposed to direct training of the model parameters)?

I am also curious how the proposal in this work might relate to the idea of 'induction heads' [1]. Intuitively these seem to be related, in that both exploit the inductive biases of transformers to perform abstract tasks involving copying.

[1] Olsson, C., Elhage, N., Nanda, N., Joseph, N., DasSarma, N., Henighan, T., ... & Olah, C. (2022). In-context learning and induction heads. arXiv preprint arXiv:2209.11895.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent
