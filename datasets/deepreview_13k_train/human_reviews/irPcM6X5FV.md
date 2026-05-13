# Leveraging Submodule Linearity Enhances Task Arithmetic Performance in LLMs

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Task arithmetic is a straightforward yet highly effective strategy for model merging, enabling the resultant model to exhibit multi-task capabilities. Recent research indicates that models demonstrating linearity enhance the performance of task arithmetic. In contrast to existing methods that rely on the global linearization of the model, we argue that this linearity already exists within the model's submodules. In particular, we present a statistical analysis and show that submodules (e.g., layers, self-attentions, and MLPs) exhibit significantly higher linearity than the overall model. Based on these findings, we propose an innovative model merging strategy that independently merges these submodules. Especially, we derive a closed-form solution for optimal merging weights grounded in the linear properties of these submodules. Experimental results demonstrate that our method consistently outperforms the standard task arithmetic approach and other established baselines across different model scales and various tasks. This result highlights the benefits of leveraging the linearity of submodules and provides a new perspective for exploring solutions for effective and practical multi-task model merging.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper shows that by identifying submodules that exhibit linearity, more granular and effective merging can be achieved. After defining these submodules, they approximate the true objective with a linear interpolation, which holds when the submodules behave linearly. The objective is defined as minimizing the loss on the joint dataset by adjusting the weighting coefficients $\alpha$. This approach outperforms existing parameter merging methods, such as Task Arithmetic. They also perform insightful ablations to determine the optimal level of merging granularity—whether at the model, MLP/attention, or head level.

### Strengths
Clear presentation, and interesting proposition of understanding which set of weights are more amenable to being merged. Novel idea of relaxing the original optimization with a linear approximation, which provides a fast and closed form solution. Good experimentation, and valuable ablation study on granularity of merging. The paper also shows impressive results with only 30 datapoints per task, making it highly efficient in terms of data and computational demands. It performs well across different scales like Llama-2-7B and Llama-2-13B, highlighting scalability for both small and large models. The approach is flexible, enabling merging at different granularities such as layer-level and attention/MLP-level, and delivers consistent performance across these structures.

### Weaknesses
The authors overlook referencing Mixture of Experts (MoE) merging approaches, such as in https://arxiv.org/abs/2402.00433, where merging also involves linearly weighting submodules. However, in traditional MoE, this weighting occurs at the activation level, rather than directly on model parameters. Since the authors allow for optimization of the weighting coefficients on the joint dataset, then the idea in this paper can be a useful baseline to run: https://arxiv.org/pdf/2410.13025.

That said, it’s unclear why the proposed method would surpass a router-based approach in performance, as a trained router can achieve task-specific specialization without approximations to the objective. While the linear interpolation method is efficient, a router's task-based dynamic routing could potentially allow finer-grained adjustments in response to specific inputs or task demands, leveraging the submodule structures without relying on assumptions of linearity. Adding comparisons or addressing these differences in the paper would clarify the potential advantages and trade-offs between the approaches.

### Questions
An interesting direction for improvement could be incorporating second-order information into the optimization process rather than updating each weighting parameter independently. Currently, the approach adjusts the coefficients linearly, assuming each weighting parameter can be optimized in isolation. However, second-order information, such as Hessian-based adjustments or other curvature-aware methods, could potentially capture interactions between weighting parameters, especially when submodules exhibit interdependencies. This is why routing methods could be more powerful, as by iteratively optimizing each layer they can better account for submodule interdependency.

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
This paper conducted a statistical analysis to examine the linearity of model-level and decomposed submodule-level components. The authors discovered that submodules (e.g., layers, self-attentions, and MLPs) demonstrate significantly higher linearity compared to the overall model. Based on this finding, they introduced a new model merging strategy that independently merges these submodules. Experimental results indicate that the proposed method surpasses the standard task arithmetic approach and other baselines across various model scales and tasks.

### Strengths
1. The paper is elegantly written and easy to comprehend. The motivation, proposed method, and experiments are all well elucidated. 
2. The authors focus on an important issue in model merging, and proposed a principled approach to address this issue.
3. The authors offer detailed explanations of the proposed method and experimental outcomes in the appendix, which is highly commendable.

### Weaknesses
1. The observation that submodules exhibit higher linearity than the overall model may be deemed rather obvious. Since the overall model is constructed from these submodules, the nonlinearity of each submodule contributes to the overall model's nonlinearity. Consequently, the comparison results presented in Figure 1 and Figure 2 are unsurprising. The linearity of the model is fundamentally inferior to that of its submodules.

2. Building upon the first comment, the proposed method could be interpreted as a straightforward extension of previous global linearization approaches. The authors introduce a layerwise linearization version, which has been explored in prior studies, such as Git Re-Basin [1], Zipit! [2], and MuDSC [3]. It would be beneficial if the authors could provide comparisons with these works.

3. Furthermore, it is conceivable to decompose the model into more finely-grained components, such as different groups, channels, or even neurons. I posit that the linearity of these components is more pronounced than that of layer-level submodules. However, this would necessitate a greater number of merging parameters, similar to the method proposed in this paper. Could the authors engage in discussions regarding this aspect?

4. The three properties outlined in Section 2 are somewhat redundant and could benefit from simplification.

5. The performance improvement is not so impressive. As the proposed method adopts a layerwise merging strategy, it is expected to be much more performant than others. However, experiments demonstrate that the proposed method is still outperformed by prior methods. For example, coding & translate, math & coding in Table 1 and Table 2.

### Questions
Please see the Weaknesses

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
4

### Summary
The paper tackles task vector-based model merging, following a line of approaches that obtain a multi-task model by adding to a pretrained model the differences between fine-tuned models and their pretrained base.  In particular, the work builds on top of previous work relating the effectiveness of task vectors to a particular kind of linearity such that if a model is taken on the line connecting pretrained and fine-tuned, its output features should be on the line connecting the features of the pretrained and those of the fine-tuned. The treatment starts by defining a non-linearity score that measures how much this linearity property is violated, showing this score to be much lower for individual layers than for the whole model. The authors then leverage this finding and propose merging individual layers, deriving a closed form for the layer weights based on the linearity requirement.  Experiments show the approach to be slightly beneficial for two LLAMA-based architectures when merging a model with math, coding, and translating capabilities.

### Strengths
- The paper is generally clear and easy to read. The experiments make intuitive sense and are well explained, with enough details to be reproduced.
- The layer-wise linearity perspective is novel. Overall, I find layer-wise approaches to better leverage the structure of the network when compared with standard vanilla task vectors. The proposed non-linearity score is novel, well-motivated, and intuitive.

### Weaknesses
 - First and foremost, I am not convinced that the results warrant the added complexity: overall, the performance of the approach is in the same ballpark as vanilla task arithmetic while not inheriting its intuitiveness and simplicity. While it exhibits some slight improvements in a portion of the (limited) evaluation settings, these are not substantial nor consistent enough.
- Still on the evaluation, the paper only considers two LLAMA-based architectures and only a subset of the evaluation settings considered by the previous works. For instance, Task Arithmetics also considers the GLUE benchmark and a suite of computer vision benchmarks, while DARE considers GLUE and OpenLLM. An exhaustive evaluation is necessary to rule out possibly lucky choices of models and datasets that do not guarantee the effectiveness of the approach in general.
- The baselines are also somewhat limited, some possible works to consider are *e.g.* [1], [2] and [3].
- The main finding of the paper, that is the fact that modules show more linearity than the whole model, obtained as a composition of all those intermediate modules, is not surprising. In fact, if the intermediate modules have non-zero non-linearity scores, the overall non-linearity score will grow as these ones accumulate.
- Experiments have shown that merging three models exhibits a lower projection distance than merging just two, highlighting the potential of merging even more models. However, the experiments only merge up to three models. Can the trend be confirmed? More experiments would help clarify this aspect.

### Questions
- The requirement of a small set of data per task is reasonable in practice, but what if no data is available? Can you still do something?
- Maybe add a few more compatible tasks so that merging more than three models reveals some interesting trends as the number of tasks increases. Maybe your framework works even better compared to the baselines when the number of tasks is raised? Or perhaps the advantage becomes less pronounced?
- Minor suggestion: In Property 2, I would really avoid using footnotes over equations as these look like powers instead.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work is inspired by models demonstrating linearity that can improve the performance of task arithmetic, and hypothesize that linearity already exists within the model’s submodules. Linearity refers to the linear relationship between the differences in model weights and the differences in output features caused by fine-tuning. A model framework that independently merges these submodules is proposed to enhance task arithmetic and hence lead to superior multi-task models. The author justify their motivation by comparing the non-linearity scores between the full model and the submodules. Using submodules instead full models requires computation of the optimal merging weights after splitting the models into submodules that exhibit linear characteristics. Experiments are conducted on fine-tuned models based on Llama-2 and the results indicate superior merging performance with task arithmetic.

### Strengths
The paper propses an interesting idea of decomposing the models into submodules that exhibit linear characteristics. The non-linearity score is proposed and merging the weights this way is novel. In particular, Figure 1 and Figure 3 clearly illustrate the motivation behind this paper and the weight merging is well-defined. The results and the ablation study support the author's claim well. The contribution of Layer level and Attention/MLP level weight merging is convincing.

### Weaknesses
One relevant topic concerning linearity is the non-linear activation function. This paper focused on the submodules and weight merging, but lacks a thorough discussion on activation functions. Figures show that the non-linearity score for all different submodeules are near zero. Why is that? Have you discarded all non-linear activation functions in submodules? If that is not the case, how do they affect the linearity assumptions and why do they not contribute to a larger non-linerarity score? Please include a discussion of activation functions.

Merging weights in head level appears to give unstable outcomes in Table 3, and the hypothesis here is that the representation functionalities can be averaged out. Is there any potential method to avoid that?

The fine-tuned models are based on Llama-2, and the 7B model tends to show stronger non-linearity than the 13B model. Have you considered the influence of the varying depth of the model and data size, and the implications with repect to universal approximation theorem?

Is there any family of activation function more suitable for your model framework than others (e.g. ReLU, GELU, Swish) and what is their impact on the linearity of submodules and overall merging performance?

### Questions
1. Merging weights in head level appears to give unstable outcomes in Table 3, and the hypothesis here is that the representation functionalities can be averaged out. Is there any potential method to avoid that?

2. The fine-tuned models are based on Llama-2, and the 7B model tends to show stronger non-linearity than the 13B model. Have you considered the influence of the varying depth of the model and data size, and the implications with repect to universal approximation theorem?

3. Is there any family of activation function more suitable for your model framework than others (e.g. ReLU, GELU, Swish) and what is their impact on the linearity of submodules and overall merging performance?

### Soundness
2

### Presentation
2

### Contribution
2
