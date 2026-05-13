# Let Me Grok for You: Accelerating Grokking via Embedding Transfer from a Weaker Model

- Decision: Accept
- Scores: 5, 3, 6, 8, 3

## Abstract
''Grokking'' is a phenomenon where a neural network first memorizes training data and generalizes poorly, but then suddenly transitions to near-perfect generalization after prolonged training. While intriguing, this delayed generalization phenomenon compromises predictability and efficiency. Ideally, models should generalize directly without delay. To this end, this paper proposes GrokTransfer, a simple and principled method for accelerating grokking in training neural networks, based on the key observation that data embedding plays a
crucial role in determining whether generalization is delayed. GrokTransfer first trains a smaller, weaker model to reach a nontrivial (but far from optimal) test performance. Then, the learned input embedding from this weaker model is extracted and used to initialize the embedding in the target, stronger model. We rigorously prove that, on a synthetic XOR task where delayed generalization always
occurs in normal training, GrokTransfer enables the target model to generalize directly without delay. Moreover, we demonstrate that, across empirical studies of different tasks, GrokTransfer effectively reshapes the training dynamics and eliminates delayed generalization, for both fully-connected neural networks and Transformers.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper studies ways to reduce the "delayed generalization" in grokking, by first learning embeddings in a smaller, faster model where generalization isn't delayed, and then transferring the embeddings to a larger model. This is shown empirically in various examples including modular addition, multiplication and parity with fully-connected nets or transformers. The authors also show theoretically that fast generalization occurs in XOR when applying the GrokTransfer technique on top of a weak solution that was found with only 3 neurons (this solution is shown to be found empirically).

### Strengths
Grokking is a surprising phenomenon that leads to seemingly unpredictable outcomes. The proposed GrokTransfer method seems like an empirically effective to mitigate this. The theoretical claims also justify why good embeddings obtained from a small model can help accelerate generalization in a larger model. Overall, this makes the work interesting and significant.

### Weaknesses
 * The theory on XOR would benefit from a better understanding of the "weaker model", which is currently mostly empirical. It would great to have even partial results for this part, even in a simpler setting (e.g. training a single neuron on this data might be tractable and similar to previous work?) Specifically, the analysis seems to rely heavily on the empirical observation that a 3-neuron network will learn 3 out of the 4 possible features. A more rigorous analysis of why this occurs, and whether this is a stable property across different initializations and training runs, would strengthen the theoretical claims. Furthermore, the theoretical analysis does not seem to address the case where the weak model learns a suboptimal representation, which may still be useful for transfer learning but is not covered by the current theory.

* The presentation could be improved in various ways, in particular the notion of "small model" considered isn't very precisely defined and would benefit from clarification. It's unclear what the precise criteria are for a model to be considered "small" beyond having fewer parameters. This makes it difficult to reproduce the results or to apply the method to new problems. Other aspects that could be discussed further include trade-offs between width and iterations needed to generalize: it seems that smaller models reduced the "delayed generalization" but also slow down convergence in terms of epochs. Perhaps this changes when looking at "compute/flops", and it would be good to include such plots. The paper should also explore the sensitivity of the method to the size of the weak model, and whether there is a sweet spot for the size of the weak model that balances generalization speed and transfer performance. It would also be helpful to see how the performance of GrokTransfer varies with different weak model architectures, not just different sizes of the same architecture.

See also the questions below.

### Questions
* Could you comment on why you chose a weak model with 3 neurons in Section 3.2? Would the story change if you had 4 of them and achieve perfect accuracy? My impression is that the delayed generalization mostly happens when you are heavily over-parameterized and can very quickly memorize all the training data in early epochs, which still wouldn't happen with 4 neurons. Also, would the transfer still work if the weak model had fewer than 3 neurons?

* For the modular addition/multiplication problems, what would be the smallest weak model that can lead to good transferrable embeddings (in practice, but also in theory with an appropriate construction?)

* For Theorem 3.2, is this in a kernel regime? Would training only the second layer instead give similar guarantees? Regardless, a brief discussion after the statement would be a good addition.

Other, minor:
* Figure 4: Should I infer from the caption that the test accuracy becomes high around the same point (near 100 epochs), while the larger model also displays the property that training accuracy is high very quickly? Also, is it reasonable to say that the small model does not exhibit grokking here? Please clarify these points since they seem important for the story.
* L 298: Do you mean that whenever the test accuracy is around 75% or above, you found empirically that the neurons consist of three such features? Please rephrase as this is not very clear.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a method to accelerate grokking via embedding transfer from a week model. The authors first observe that data embedding plays a crucial role in determining whether generalization is delayed. Then they initialize the embedding weights extracted from  training a smaller and weaker model to the target, strong model. Finally, the authors give rigorous proof on a synthetic XOR task with simple network settings, and provide empirical studies showing the effectiveness of the proposed GrokTransfer method on fully-connected network and transformers.

### Strengths
1) This paper is clearly written and the idea is easy to follow.
2) The choice of the task (XOR) and the setting of the model (very simple network) is easy to interpret for the purpose of the finding of this paper.

### Weaknesses
1) the key observation which is that the data embedding plays a crucial role in the generalization delay is not well studied. As the proposed accelerating method is based on this observation, it would be better to provide more evidence to say this observation is indeed the correct one. In addition to the modular addition task, providing more results on other tasks would make this observation more convincing. Also, instead of data embedding layer only, is the initialization of other layers a possible reason to cause the delay? An ablation study on other possible reasons to cause the delay would be better.

2) In addition to simple settings, verification on more complicated tasks would make the finding more general and solid.

3) In the theoretical analysis, the proof seems a little bit limited because the choice of very simple setting.

4) It would be better if the authors make a clearer study on how to choose the "weaker and smaller" model to get the acceleration with good test performance.

### Questions
1) In section 3.2, could you add more details on getting the SNR with different embeddings?

2) The intuition on why the data embedding  make a difference on the generalization speed is still not very clear. 

If we take all layers beyond the last linear layer (which includes data embedding layer and some hidden layer) as doing feature engineering, as mentioned in [1], will this claim (in section 3.2, ``with this new embedding, data points are well separated in a three-dimensional space with a relatively high signal-to-noise ratio (SNR) compared to the original embedding'') still hold if we pass this data embedding into above hidden layers? Does the separation among the feature vectors got from the last hidden layer make more sense than the one among data embeddings?



[1] Papyan, V., Han, X. Y., & Donoho, D. L. (2020). Prevalence of neural collapse during the terminal phase of deep learning training. Proceedings of the National Academy of Sciences, 117(40), 24652-24663.

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
3

### Summary
This paper investigates "grokking," a phenomenon where neural networks initially struggle to generalize, only to suddenly achieve near-perfect generalization after extended training. To accelerate generalization, the authors propose GrokTransfer. GrokTransfer leverages the embedding from a smaller, preliminary model that achieves moderate test performance, transferring it to a stronger target model to speed up generalization. This approach successfully eliminates delayed generalization on a synthetic XOR task and performs well across various algorithmic tasks on both fully connected networks and Transformers. The results suggest that GrokTransfer could reshape training dynamics, enabling models to generalize without delay.

### Strengths
- The proposed method is interesting and novel to my knowledge. It first trains an under-parameterized model that is incapable of perfectly interpolating the data, and then uses the learned data embedding to facilitate the grokking of an over-parameterized model. It’s like approaching a problem by first crafting a simple but general solution that works well for most cases and then refining the solution to cover all the rest of the cases. Intuitively, this eliminates a lot of unnecessary competition among various not-so-simple solutions in an over-parameterized model, hence accelerating the learning process.
- The paper is very well written. It includes an extensive discussion of the related work, a clear presentation of the motivation behind the proposed method, and a detailed case study that explains how and why the method works.

### Weaknesses
 - It is unclear how well the method would generalize and scale to more complicated problems where such acceleration can make a real impact. The algorithmic problems are useful for analysis but are too simple in comparison with real-world problems which often involve high-dimensional inputs. For high-dimensional inputs with many redundant features, it is likely for the weaker model to lock onto degenerate solutions that would hinder the stronger model from grokking. It would be interesting to see if this is really the case or not.
- The paper does not provide much insight on how to design or choose the weaker model. Clearly, the weaker model can neither be too weak nor too strong, i.e. there is a trade-off. If it is too weak, the solution may degenerate and thus make it harder for the stronger model to grok. If the weaker model is too strong, then it may take too much time to train the weaker model. Therefore, for this method to be truly useful, there should be some general rule of thumb for choosing the weaker model, otherwise, much time could be wasted on trial and error.
- As the authors have mentioned in the paper, the theoretical result only considers a relatively simple XOR task. There does not seem to be any clear indication if the analysis could potentially be applied to more general problems. Therefore, the significance of this result is in doubt.

### Questions
- Would a “smoother” version of the proposed method work even better? For example, one could start from a single embedding layer with a small number of neurons and gradually deepen/widen it, i.e., adding more layers and adding more neurons to each layer.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces GrokTransfer, a method that expedites grokking by transferring embeddings from a weaker model. Through a simple XOR classification task, the authors offer both theoretical and empirical justification for GrokTransfer. Experiments on other algorithmic tasks show its effectiveness in embedding transfer from FNN to FNN/transformers.

### Strengths
1. The authors provide a sensible justification for the core idea of their method through a motivating experiment in Section 2.1. 
2. They demonstrate its effectiveness both empirically and theoretically, highlighting improvements in computational costs and performance.
3. The proposed method is simple and straightforward, and if it can generalize to broader tasks and architectures, it has significant potential.

### Weaknesses
1. The authors tested three algorithmic tasks—modular addition, modular multiplication, and the (40,3)-parity task—for FNN->FNN transfers. However, they provided results for only one task (modular addition) in the FNN->transformers setting. Given that FNN->transformer transfers are more practical and high in potential, there seems to be no reason to exclude modular multiplication and the (40,3)-parity task. Without these experiments, I can't help but think that the generalizability of GrokTransfer is limited.

2.  Grokking is known to occur beyond algorithmic data [1], which is already cited in the paper. I would like to see how GrokTransfer performs on non-algorithmic tasks, such as image classification with MNIST, as explored in [1].

3. A new paper [2] has been recently released on accelerating grokking through weight transfer based on the Kolmogorov-Arnold (KA) representation theorem. Your approach seems simpler, but the approach in [2] can even handle two non-standard arithmetic tasks—composition of operations and systems of equations. How does GrokTransfer compare to [2], in terms of theoretical basis, performance, and practicality?

Minor
- Typo at line 255: “need [to] learn”
- There are reference mistakes in the paper, concerning arXiv citations that should point to conference proceedings. Here is an example of wrong references:

Tanishq Kumar, Blake Bordelon, Samuel J Gershman, and Cengiz Pehlevan. Grokking as the transition from lazy to rich training dynamics. arXiv preprint arXiv:2310.06110, 2023.
(Published in ICLR 2024)

Note: the minor points did not influence my final score.

### Questions
1. Regarding W1, the FNN->transformer setting was tested on only one task. I would like to see GrokTransfer's performance on more algorithmic tasks in this setting, especially in comparison to GrokFast. According to Table 1, training is very fast with GrokTransfer, so it should be quick to perform experiments on additional tasks (including those not tested in the paper). 

2. Grokking is known to occur beyond algorithmic data [1], which is already cited in the paper. I would like to see how GrokTransfer performs on non-algorithmic tasks, such as image classification with MNIST, as explored in [1].

3. A new paper [2] has been recently released on accelerating grokking through weight transfer based on the Kolmogorov-Arnold (KA) representation theorem. Your approach seems simpler, but the approach in [2] can even handle two non-standard arithmetic tasks—composition of operations and systems of equations. How does GrokTransfer compare to [2], in terms of theoretical basis, performance, and practicality?

[1] Ziming Liu, Eric J Michaud, and Max Tegmark. Omnigrok: Grokking beyond algorithmic data. In The Eleventh International Conference on Learning Representations, 2023.

[2] Yeachan Park, Minseok Kim, & Yeoneung Kim. Acceleration of Grokking in Learning Arithmetic Operations via Kolmogorov-Arnold Representation. arXiv preprint arXiv:2405.16658, 2024

Minor
- Typo at line 255: “need [to] learn”
- There are reference mistakes in the paper, concerning arXiv citations that should point to conference proceedings. Here is an example of wrong references:

Tanishq Kumar, Blake Bordelon, Samuel J Gershman, and Cengiz Pehlevan. Grokking as the transition from lazy to rich training dynamics. arXiv preprint arXiv:2310.06110, 2023.
(Published in ICLR 2024)

Note: the minor points did not influence my final score.

### Soundness
2

### Presentation
2

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
The paper introduces a method to mitigate grokking, which describes the scenario in which models overfit to the training dataset long before it begins to generalize to unseen test data. This is done by training a smaller model with a much lower embedding (number of features in first layer) dimension, which converges quicker and without grokking. The architecture of the original model is then modified by replacing the first embedding layer with the product of two matrices $E_T = AB$ where $A$ and $B$ are of much lower rank. $A$ is initialized with the embedding layer of the smaller model. This model is evaluated on several synthetic tasks -- modular addition, modular multiplication, and a (40,3)-parity task defined as learning $y = \Pi_{i \in \{1,2,3\}} x_i$ where $x \in \{\pm 1\}^{40}$. Experiments show that compared to the original model that is randomly initialized, the resulting model mitigates grokking and converges faster. Theoretical analysis is also provided for a specific case involving learning $y = x_1$  XOR $x_2$ for a 80K dimensional vector $x$.

### Strengths
- The method is clearly described and easily understandable and implementable.
- The combined time for the proposed method appears much faster than the baseline method of training the original target model from scratch. Table 1 suggests it is more than 5x faster. However ablations are needed to determine whether the speedup comes from architectural modifications, or from the proposed method.
- For the tasks studied, the model performs well in terms of reducing grokking and accelerating convergence (although comparisons are not apples-to-apples -- see Weakness 1)

### Weaknesses
 - My main concern is that all the numbers reported for GrokTransfer and the target model (Large) are not directly/fairly comparable. The model used for GrokTransfer parameterizes the first layer with $E_T = AB$ where $A$ and $B$ are (very) low-rank matrices. On the other hand, the original target model uses the full $d_v \times d_T$ matrix which is significantly larger. The number of parameters present in this layer is now much larger than that of $E_T = AB$ . A fair comparison should not even consider target models with the full $d_v \times d_T$ embedding layer, but only those parametrized with $AB$ , where, for instance, $A$ can be randomly initialized instead of being initialized from the weaker model. As such, it is difficult to conclude anything regarding whether the improvement comes from weak model initialization, or simply from architectural modifications, from any of the existing results.
- This defeats the purpose of studying/mitigating grokking in the first place, where the goal is to be able to train over-parametrized models with minimal grokking. This method instead replaces the over-parametrized model with one of more manageable complexity, which ties to the next weakness
- Method also greatly reduces the expressivity of the original target model, by adding a very low-rank bottleneck to the first layer. While this works for the synthetic closed-form tasks considered in the paper, it suggests that (1) the original target model architecture is clearly ill-suited, since it converges perfectly even after introducing a very low-rank bottleneck, and (2) ability of the method to generalize to more complex tasks which require greater expressivity is limited and questionable.
- The general motivation of the method appears to be applying dimensionality reduction to pre-process inputs that have very low SNR. This opens up questions regarding how the method compares to classical techniques like LDA?
- Method introduces an additional layer of complexity in the training pipeline, due to having to train an additional model which would require its own architectural and hyperparameter sweeps.
- Minor comments on notation: Inconsistent notation switching between $d_{embed}$ and $d_W$  / $d_F$, which makes it hard to look up. Notation on line $y=x_1 x_2$ is also ambiguous, I assume the multiplication operation here is XOR. Also overloaded notation for $p$ for modulo and dimension of input in XOR task.

### Questions
- Do the conditions in the theoretical analysis, under which grokking is mitigated for the XOR task, have any implications on what are the causes of grokking? For instance, it possibly suggests several several causes of grokking, including the SNR, overparametrization (A5), initialization (A3), etc. 
- Are there failure cases of the method? I do not see mentions of them in the limitations.

### Soundness
2

### Presentation
4

### Contribution
2
